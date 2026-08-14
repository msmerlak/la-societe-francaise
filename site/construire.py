#!/usr/bin/env python3
"""Construit le site de « La société française » à partir des numéros du dépôt.

Ne publie qu'une chose : le `index.md` de chaque numéro. Le `dispositif.md`, la
`collecte/` et les `verifications/` sont des archives de travail — versionnées,
jamais publiées. Cette règle est appliquée ici par construction : le générateur
ne va chercher aucun autre fichier, et refuse de servir un dossier de travail
même s'il en reçoit le chemin.

Usage :
    python3 site/construire.py                  construit dans public/
    python3 site/construire.py --controler      contrôle seulement, n'écrit rien
    python3 site/construire.py --strict         échoue si un contrôle remonte une erreur
    python3 site/construire.py --newsletter     produit aussi la version e-mail
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import controles  # noqa: E402
import rendu  # noqa: E402

RACINE_SITE = Path(__file__).resolve().parent
GABARITS = RACINE_SITE / "gabarits"
STYLES = RACINE_SITE / "styles"

ENSEIGNE = "La société française"
DEVISE = "Portrait quantitatif de la France, à partir des sources publiques primaires"

MOIS = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre",
]

# Styles minimaux réinjectés dans les balises pour la newsletter : les clients
# de messagerie ignorent les feuilles externes, et une partie ignore <style>.
STYLES_COURRIEL = {
    "h1": "font:600 27px/1.25 Georgia,serif;margin:0 0 14px;color:#16202b",
    "h2": "font:600 20px/1.3 Georgia,serif;margin:34px 0 10px;color:#16202b;"
    "border-top:1px solid #d8d2c7;padding-top:16px",
    "h3": "font:600 17px/1.35 Georgia,serif;margin:26px 0 8px;color:#16202b",
    "h4": "font:600 15px/1.35 Georgia,serif;margin:20px 0 6px;color:#16202b",
    "p": "font:16px/1.65 Georgia,serif;margin:0 0 14px;color:#26313d",
    "li": "font:16px/1.6 Georgia,serif;margin:0 0 6px;color:#26313d",
    "table": "border-collapse:collapse;width:100%;margin:0 0 18px",
    "th": "font:600 13px/1.4 Helvetica,Arial,sans-serif;text-align:left;padding:7px 9px;"
    "border-bottom:2px solid #b9b1a3;color:#16202b",
    "td": "font:14px/1.5 Helvetica,Arial,sans-serif;padding:7px 9px;"
    "border-bottom:1px solid #e2ddd3;color:#26313d",
    "blockquote": "margin:0 0 18px;padding:12px 16px;background:#f6f2ea;"
    "border-left:3px solid #9a8f7a",
    "hr": "border:0;border-top:1px solid #d8d2c7;margin:26px 0",
    "a": "color:#8c2f39",
}


# --------------------------------------------------------------------- numéros


class Numero:
    """Un numéro publié : son dossier, son texte, ses dates."""

    def __init__(self, dossier: Path, racine: Path) -> None:
        self.dossier = dossier
        self.racine = racine
        self.slug = dossier.name
        self.source = dossier / "index.md"
        self.dispositif = dossier / "dispositif.md"
        self.markdown = self.source.read_text(encoding="utf-8")
        self.document = rendu.analyser(self.markdown)
        self.publie_le, self.modifie_le = self._dates()

    @property
    def rang(self) -> str:
        correspondance = re.match(r"^(\d+)", self.slug)
        return correspondance.group(1).lstrip("0") if correspondance else ""

    @property
    def url(self) -> str:
        return f"numeros/{self.slug}/index.html"

    def _dates(self) -> tuple[datetime | None, datetime | None]:
        """Première et dernière apparition du fichier dans l'historique git.

        Rien n'est demandé à l'éditeur : la date de publication est celle du
        commit qui a introduit `index.md`, ce qui évite d'imposer un
        front-matter à un fichier qui doit rester du Markdown standard.
        """

        def git(*arguments: str) -> str:
            try:
                return subprocess.run(
                    ["git", *arguments],
                    cwd=self.racine,
                    capture_output=True,
                    text=True,
                    timeout=15,
                    check=False,
                ).stdout.strip()
            except (OSError, subprocess.SubprocessError):
                return ""

        chemin = str(self.source.relative_to(self.racine))
        ajouts = git("log", "--diff-filter=A", "--format=%aI", "--", chemin)
        dernier = git("log", "-1", "--format=%aI", "--", chemin)

        def lire(valeur: str) -> datetime | None:
            ligne = valeur.split("\n")[-1].strip() if valeur else ""
            try:
                return datetime.fromisoformat(ligne) if ligne else None
            except ValueError:
                return None

        publie = lire(ajouts)
        modifie = lire(dernier)
        if publie is None:
            horodatage = self.source.stat().st_mtime
            publie = datetime.fromtimestamp(horodatage, tz=timezone.utc)
        return publie, modifie


def dater(moment: datetime | None) -> str:
    if moment is None:
        return ""
    jour = "1ᵉʳ" if moment.day == 1 else str(moment.day)
    return f"{jour} {MOIS[moment.month - 1]} {moment.year}"


def trouver_numeros(racine: Path) -> list[Numero]:
    """Recense les numéros publiés. Un dossier sans `index.md` n'est pas publié."""
    dossier_numeros = racine / "numeros"
    if not dossier_numeros.is_dir():
        return []
    trouves = []
    for dossier in sorted(dossier_numeros.iterdir()):
        if dossier.is_dir() and (dossier / "index.md").is_file():
            trouves.append(Numero(dossier, racine))
    return trouves


# -------------------------------------------------------------------- gabarits


def appliquer(gabarit: str, **valeurs: str) -> str:
    """Substitution de `{{cle}}`. Pas de moteur de gabarits : rien ne le justifie."""
    resultat = gabarit
    for cle, valeur in valeurs.items():
        resultat = resultat.replace("{{" + cle + "}}", valeur)
    return re.sub(r"\{\{\w+\}\}", "", resultat)


def lire_gabarit(nom: str) -> str:
    return (GABARITS / nom).read_text(encoding="utf-8")


def sommaire_html(numero: Numero) -> str:
    if len(numero.document.sommaire) < 3:
        return ""
    articles = []
    for titre in numero.document.sommaire:
        classe = "niveau-2" if titre.niveau == 2 else "niveau-3"
        articles.append(
            f'<li class="{classe}"><a href="#{titre.ancre}">{titre.texte}</a></li>'
        )
    return (
        '<nav class="sommaire" aria-label="Sommaire du numéro">'
        "<h2>Sommaire</h2><ul>" + "".join(articles) + "</ul></nav>"
    )


def page_numero(numero: Numero, autres: list[Numero]) -> str:
    ligne_date = f"Publié le {dater(numero.publie_le)}"
    if (
        numero.modifie_le
        and numero.publie_le
        and numero.modifie_le.date() != numero.publie_le.date()
    ):
        ligne_date += f" · mis à jour le {dater(numero.modifie_le)}"

    voisins = [n for n in autres if n.slug != numero.slug]
    if voisins:
        liens = "".join(
            f'<li><a href="../{n.slug}/index.html">n° {n.rang} — {html.escape(n.document.titre)}</a></li>'
            for n in voisins
        )
        suite = f'<nav class="autres-numeros"><h2>Les autres numéros</h2><ul>{liens}</ul></nav>'
    else:
        suite = ""

    contenu = appliquer(
        lire_gabarit("numero.html"),
        rang=f"n° {numero.rang}" if numero.rang else "",
        titre=numero.document.titre_html,
        chapo=numero.document.chapo_html,
        date=ligne_date,
        sommaire=sommaire_html(numero),
        corps=numero.document.corps_html,
        autres=suite,
    )
    return appliquer(
        lire_gabarit("base.html"),
        titre_page=f"{numero.document.titre} — {ENSEIGNE}",
        description=html.escape(numero.document.chapo_texte[:180], quote=True),
        racine="../../",
        enseigne=ENSEIGNE,
        devise=DEVISE,
        contenu=contenu,
        annee=str(datetime.now().year),
    )


def page_accueil(numeros: list[Numero]) -> str:
    if numeros:
        articles = []
        for numero in numeros:
            articles.append(
                appliquer(
                    lire_gabarit("carte.html"),
                    url=numero.url,
                    rang=f"n° {numero.rang}" if numero.rang else "",
                    date=dater(numero.publie_le),
                    titre=numero.document.titre_html,
                    chapo=html.escape(numero.document.chapo_texte[:320]),
                )
            )
        liste = "".join(articles)
    else:
        liste = (
            '<p class="vide">Aucun numéro publié pour l\'instant. Le premier est en '
            "cours de fabrication : collecte, vérification, assemblage.</p>"
        )
    contenu = appliquer(lire_gabarit("accueil.html"), numeros=liste)
    return appliquer(
        lire_gabarit("base.html"),
        titre_page=ENSEIGNE,
        description=html.escape(DEVISE, quote=True),
        racine="",
        enseigne=ENSEIGNE,
        devise=DEVISE,
        contenu=contenu,
        annee=str(datetime.now().year),
    )


def flux_rss(numeros: list[Numero], base: str) -> str:
    articles = []
    for numero in numeros:
        publie = numero.publie_le or datetime.now(tz=timezone.utc)
        articles.append(
            "<item>"
            f"<title>{html.escape(numero.document.titre)}</title>"
            f"<link>{base}{numero.url}</link>"
            f"<guid isPermaLink='true'>{base}{numero.url}</guid>"
            f"<pubDate>{publie.strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>"
            f"<description>{html.escape(numero.document.chapo_texte)}</description>"
            "</item>"
        )
    return (
        "<?xml version='1.0' encoding='UTF-8'?>\n"
        "<rss version='2.0'><channel>"
        f"<title>{ENSEIGNE}</title>"
        f"<link>{base}</link>"
        f"<description>{html.escape(DEVISE)}</description>"
        "<language>fr</language>"
        + "".join(articles)
        + "</channel></rss>\n"
    )


def version_courriel(numero: Numero) -> str:
    """Même Markdown, rendu pour la messagerie : styles en ligne, largeur fixe."""
    corps = numero.document.chapo_html + numero.document.corps_html
    corps = corps.replace('<div class="chapo">', "<div>").replace("<div class='tableau'>", "<div>")
    for balise, style in STYLES_COURRIEL.items():
        corps = re.sub(
            rf"<{balise}(?=[ >])((?:[^>](?!style=))*?)>",
            lambda m, b=balise, s=style: f'<{b}{m.group(1)} style="{s}">',
            corps,
        )
        corps = corps.replace(f"<{balise}>", f'<{balise} style="{style}">')

    # Les classes d'alignement n'existent pas en messagerie : il faut les
    # replier dans le style en ligne, sinon les colonnes de chiffres se
    # désalignent — et un tableau de chiffres désaligné ne se lit plus.
    corps = re.sub(
        r'<(td|th) class="al-(right|center)" style="([^"]*)"',
        lambda m: f'<{m.group(1)} style="{m.group(3)};text-align:{m.group(2)}"',
        corps,
    )
    return appliquer(
        lire_gabarit("courriel.html"),
        titre=numero.document.titre_html,
        enseigne=ENSEIGNE,
        date=dater(numero.publie_le),
        corps=corps,
    )


# ---------------------------------------------------------------- construction


def construire(racine: Path, sortie: Path, avec_newsletter: bool, base: str) -> list[Numero]:
    numeros = trouver_numeros(racine)
    sortie.mkdir(parents=True, exist_ok=True)

    (sortie / "index.html").write_text(page_accueil(numeros), encoding="utf-8")

    dossier_styles = sortie / "styles"
    dossier_styles.mkdir(exist_ok=True)
    for feuille in STYLES.glob("*.css"):
        (dossier_styles / feuille.name).write_text(
            feuille.read_text(encoding="utf-8"), encoding="utf-8"
        )

    for numero in numeros:
        cible = sortie / "numeros" / numero.slug
        cible.mkdir(parents=True, exist_ok=True)
        (cible / "index.html").write_text(page_numero(numero, numeros), encoding="utf-8")

        media = numero.dossier / "media"
        if media.is_dir():
            destination = cible / "media"
            destination.mkdir(exist_ok=True)
            for fichier in media.iterdir():
                if fichier.is_file():
                    (destination / fichier.name).write_bytes(fichier.read_bytes())

        if avec_newsletter:
            dossier_courriel = sortie / "newsletter"
            dossier_courriel.mkdir(exist_ok=True)
            (dossier_courriel / f"{numero.slug}.html").write_text(
                version_courriel(numero), encoding="utf-8"
            )

    (sortie / "flux.xml").write_text(flux_rss(numeros, base), encoding="utf-8")
    return numeros


def controler_tout(racine: Path) -> tuple[int, int]:
    numeros = trouver_numeros(racine)
    if not numeros:
        print("Aucun numéro publié — rien à contrôler.")
        return 0, 0

    total_erreurs = total_avertissements = 0
    for numero in numeros:
        dispositif = numero.dispositif if numero.dispositif.exists() else None
        signalements = controles.controler(numero.markdown, dispositif)
        erreurs, avertissements = controles.resumer(signalements)
        total_erreurs += erreurs
        total_avertissements += avertissements

        etat = "conforme" if not signalements else f"{erreurs} erreur(s), {avertissements} avertissement(s)"
        print(f"\n{numero.slug} — {etat}")
        for signalement in signalements:
            print(signalement)
    return total_erreurs, total_avertissements


def principal() -> int:
    analyseur = argparse.ArgumentParser(description="Construit le site de La société française.")
    analyseur.add_argument("--source", default=None, help="racine du dépôt (défaut : le dépôt courant)")
    analyseur.add_argument("--sortie", default=None, help="dossier de sortie (défaut : public/)")
    analyseur.add_argument("--controler", action="store_true", help="contrôle seulement, n'écrit rien")
    analyseur.add_argument("--strict", action="store_true", help="échoue si un contrôle remonte une erreur")
    analyseur.add_argument("--newsletter", action="store_true", help="produit aussi la version e-mail")
    analyseur.add_argument("--base", default="https://lasocietefrancaise.fr/", help="URL publique, pour le flux")
    arguments = analyseur.parse_args()

    racine = Path(arguments.source).resolve() if arguments.source else RACINE_SITE.parent
    sortie = Path(arguments.sortie).resolve() if arguments.sortie else racine / "public"

    erreurs, avertissements = controler_tout(racine)

    if arguments.controler:
        print(f"\n{erreurs} erreur(s), {avertissements} avertissement(s).")
        return 1 if (erreurs and arguments.strict) else 0

    if erreurs and arguments.strict:
        print(f"\nConstruction interrompue : {erreurs} erreur(s) de conformité.")
        return 1

    numeros = construire(racine, sortie, arguments.newsletter, arguments.base)
    relatif = sortie.relative_to(racine) if sortie.is_relative_to(racine) else sortie
    print(f"\n{len(numeros)} numéro(s) construit(s) dans {relatif}/")
    if erreurs:
        print(f"Attention : {erreurs} erreur(s) de conformité non bloquantes (--strict pour bloquer).")
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
