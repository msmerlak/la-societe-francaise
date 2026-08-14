"""Rendu Markdown → HTML pour « La société française ».

Sous-ensemble volontairement restreint : titres, paragraphes, tableaux,
citations, listes, blocs de code, emphase, liens, images, filets. C'est
exactement ce que les contraintes de diffusion du CLAUDE.md autorisent dans un
fichier de numéro — rien de plus n'a à être rendu, et tout ce qui ressemble à
du HTML brut est échappé plutôt qu'interprété.

Aucune dépendance : un dépôt de contenu doit pouvoir publier sans installer
quoi que ce soit.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field

# Espaces qui ne doivent jamais être normalisées : elles portent la typographie.
INSECABLE = " "
INSECABLE_FINE = " "

# Caractères admis dans une cellule que l'on considère comme numérique, et donc
# alignée à droite. Une cellule qui contient un mot reste alignée à gauche.
CARACTERES_NUMERIQUES = set(
    "0123456789"
    " .,;:/()[]%€$‰×~≈<>=+±−–—*'’"
    "MdMtkbn²³₂ᵉʳ"
    + INSECABLE
    + INSECABLE_FINE
)


@dataclass
class Titre:
    """Une entrée du sommaire."""

    niveau: int
    texte: str
    ancre: str


@dataclass
class Document:
    """Un numéro analysé, prêt à être inséré dans un gabarit."""

    titre: str = ""
    titre_html: str = ""
    chapo_html: str = ""
    chapo_texte: str = ""
    corps_html: str = ""
    sommaire: list[Titre] = field(default_factory=list)


def ancrer(texte: str) -> str:
    """Fabrique une ancre d'URL stable à partir d'un titre français."""
    sans_balise = re.sub(r"<[^>]+>", "", texte)
    decompose = unicodedata.normalize("NFKD", sans_balise)
    sans_accent = "".join(c for c in decompose if not unicodedata.combining(c))
    minuscule = sans_accent.lower()
    tirets = re.sub(r"[^a-z0-9]+", "-", minuscule).strip("-")
    return tirets or "section"


def echapper(texte: str) -> str:
    """Neutralise le HTML. Appelé avant toute autre transformation inline."""
    return (
        texte.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def cellule_numerique(texte: str) -> bool:
    """Vrai si la cellule ne porte qu'une valeur, et mérite un alignement à droite."""
    nu = texte.strip()
    if not nu or not any(c.isdigit() for c in nu):
        return False
    return all(c in CARACTERES_NUMERIQUES for c in nu)


class Rendu:
    """Analyseur de blocs. Une instance par document."""

    MOTIF_TITRE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
    MOTIF_FILET = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
    MOTIF_SEPARATEUR_TABLEAU = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
    MOTIF_PUCE = re.compile(r"^(\s*)[-*+]\s+(.*)$")
    MOTIF_NUMERO = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
    MOTIF_CITATION = re.compile(r"^\s*>\s?(.*)$")
    MOTIF_CLOTURE = re.compile(r"^\s*```")

    def __init__(self) -> None:
        self.sommaire: list[Titre] = []
        self._ancres: set[str] = set()

    # ------------------------------------------------------------------ inline

    def inline(self, texte: str) -> str:
        """Rend l'emphase, les liens et le code d'une portée de texte."""
        html = echapper(texte)

        # Le code littéral est mis de côté : rien ne doit s'y appliquer.
        litteraux: list[str] = []

        def garder(correspondance: re.Match[str]) -> str:
            litteraux.append(correspondance.group(1))
            return f"\x00{len(litteraux) - 1}\x00"

        html = re.sub(r"`([^`]+)`", garder, html)

        html = re.sub(
            r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+&quot;([^&]*)&quot;)?\)",
            lambda m: '<img src="{}" alt="{}"{}>'.format(
                m.group(2), m.group(1), f' title="{m.group(3)}"' if m.group(3) else ""
            ),
            html,
        )
        html = re.sub(
            r"\[([^\]]+)\]\(([^)\s]+)\)",
            lambda m: '<a href="{}"{}>{}</a>'.format(
                m.group(2),
                ' rel="noopener"' if m.group(2).startswith("http") else "",
                m.group(1),
            ),
            html,
        )

        html = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", html)
        html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
        html = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", html)
        html = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])", r"<em>\1</em>", html)

        for indice, litteral in enumerate(litteraux):
            html = html.replace(f"\x00{indice}\x00", f"<code>{litteral}</code>")
        return html

    # ------------------------------------------------------------------- blocs

    def blocs(self, lignes: list[str]) -> str:
        """Rend une suite de lignes Markdown en HTML."""
        morceaux: list[str] = []
        i = 0
        while i < len(lignes):
            ligne = lignes[i]

            if not ligne.strip():
                i += 1
                continue

            if self.MOTIF_CLOTURE.match(ligne):
                i = self._bloc_code(lignes, i, morceaux)
                continue

            if self.MOTIF_FILET.match(ligne):
                morceaux.append("<hr>")
                i += 1
                continue

            titre = self.MOTIF_TITRE.match(ligne)
            if titre:
                self._titre(titre, morceaux)
                i += 1
                continue

            if "|" in ligne and i + 1 < len(lignes) and self.MOTIF_SEPARATEUR_TABLEAU.match(lignes[i + 1]):
                i = self._tableau(lignes, i, morceaux)
                continue

            if self.MOTIF_CITATION.match(ligne):
                i = self._citation(lignes, i, morceaux)
                continue

            if self.MOTIF_PUCE.match(ligne) or self.MOTIF_NUMERO.match(ligne):
                i = self._liste(lignes, i, morceaux)
                continue

            i = self._paragraphe(lignes, i, morceaux)

        return "\n".join(morceaux)

    def _titre(self, correspondance: re.Match[str], morceaux: list[str]) -> None:
        niveau = len(correspondance.group(1))
        contenu = self.inline(correspondance.group(2))
        ancre = ancrer(contenu)
        base, compteur = ancre, 2
        while ancre in self._ancres:
            ancre = f"{base}-{compteur}"
            compteur += 1
        self._ancres.add(ancre)
        if niveau in (2, 3):
            self.sommaire.append(Titre(niveau, re.sub(r"<[^>]+>", "", contenu), ancre))
        morceaux.append(f'<h{niveau} id="{ancre}">{contenu}</h{niveau}>')

    def _bloc_code(self, lignes: list[str], i: int, morceaux: list[str]) -> int:
        langue = lignes[i].strip().lstrip("`").strip()
        i += 1
        contenu: list[str] = []
        while i < len(lignes) and not self.MOTIF_CLOTURE.match(lignes[i]):
            contenu.append(lignes[i])
            i += 1
        classe = f' class="langue-{ancrer(langue)}"' if langue else ""
        morceaux.append(
            f"<pre><code{classe}>" + echapper("\n".join(contenu)) + "</code></pre>"
        )
        return i + 1

    def _tableau(self, lignes: list[str], i: int, morceaux: list[str]) -> int:
        def cellules(ligne: str) -> list[str]:
            nu = ligne.strip()
            if nu.startswith("|"):
                nu = nu[1:]
            if nu.endswith("|"):
                nu = nu[:-1]
            return [c.strip() for c in nu.split("|")]

        entetes = cellules(lignes[i])
        alignements = []
        for marque in cellules(lignes[i + 1]):
            if marque.startswith(":") and marque.endswith(":"):
                alignements.append("center")
            elif marque.endswith(":"):
                alignements.append("right")
            else:
                alignements.append("")

        i += 2
        corps: list[list[str]] = []
        while i < len(lignes) and "|" in lignes[i] and lignes[i].strip():
            corps.append(cellules(lignes[i]))
            i += 1

        html = ["<div class='tableau'>", "<table>", "<thead><tr>"]
        for indice, entete in enumerate(entetes):
            style = self._style_alignement(alignements, indice)
            html.append(f"<th{style}>{self.inline(entete)}</th>")
        html.append("</tr></thead>")
        html.append("<tbody>")
        for rangee in corps:
            html.append("<tr>")
            for indice, valeur in enumerate(rangee):
                aligne = alignements[indice] if indice < len(alignements) else ""
                if not aligne and cellule_numerique(valeur):
                    aligne = "right"
                style = f' class="al-{aligne}"' if aligne else ""
                html.append(f"<td{style}>{self.inline(valeur)}</td>")
            html.append("</tr>")
        html.append("</tbody></table></div>")
        morceaux.append("".join(html))
        return i

    @staticmethod
    def _style_alignement(alignements: list[str], indice: int) -> str:
        aligne = alignements[indice] if indice < len(alignements) else ""
        return f' class="al-{aligne}"' if aligne else ""

    def _citation(self, lignes: list[str], i: int, morceaux: list[str]) -> int:
        interieur: list[str] = []
        while i < len(lignes):
            correspondance = self.MOTIF_CITATION.match(lignes[i])
            if correspondance:
                interieur.append(correspondance.group(1))
                i += 1
            elif lignes[i].strip() and interieur:
                interieur.append(lignes[i].strip())
                i += 1
            else:
                break
        classe = " class='precaution'" if "⚠" in "".join(interieur) else ""
        morceaux.append(f"<blockquote{classe}>{self.blocs(interieur)}</blockquote>")
        return i

    def _liste(self, lignes: list[str], i: int, morceaux: list[str]) -> int:
        ordonnee = bool(self.MOTIF_NUMERO.match(lignes[i]))
        articles: list[str] = []
        while i < len(lignes):
            puce = self.MOTIF_PUCE.match(lignes[i])
            numero = self.MOTIF_NUMERO.match(lignes[i])
            if not puce and not numero:
                if lignes[i].strip() and articles and lignes[i].startswith(("  ", "\t")):
                    articles[-1] += " " + lignes[i].strip()
                    i += 1
                    continue
                break
            articles.append((numero.group(3) if numero else puce.group(2)))
            i += 1
        balise = "ol" if ordonnee else "ul"
        contenu = "".join(f"<li>{self.inline(a)}</li>" for a in articles)
        morceaux.append(f"<{balise}>{contenu}</{balise}>")
        return i

    def _paragraphe(self, lignes: list[str], i: int, morceaux: list[str]) -> int:
        tampon: list[str] = []
        while i < len(lignes) and lignes[i].strip():
            if (
                self.MOTIF_TITRE.match(lignes[i])
                or self.MOTIF_FILET.match(lignes[i])
                or self.MOTIF_CITATION.match(lignes[i])
                or self.MOTIF_PUCE.match(lignes[i])
                or self.MOTIF_NUMERO.match(lignes[i])
                or self.MOTIF_CLOTURE.match(lignes[i])
            ):
                break
            tampon.append(lignes[i].strip())
            i += 1
        if tampon:
            texte = "\n".join(tampon)
            # Deux espaces en fin de ligne = saut de ligne, convention Markdown.
            html = self.inline(texte).replace("  \n", "<br>\n").replace("\n", " ")
            morceaux.append(f"<p>{html}</p>")
        return i


def analyser(markdown: str) -> Document:
    """Analyse un `index.md` de numéro et en extrait titre, chapô et corps.

    Le titre est le premier `#`. Le chapô est le premier paragraphe entièrement
    en italique qui le suit — c'est la convention du CLAUDE.md, et elle évite
    d'imposer un front-matter aux fichiers de numéro, qui doivent rester du
    Markdown standard pour rester portables vers la plateforme d'envoi.
    """
    lignes = markdown.replace("\r\n", "\n").split("\n")
    rendu = Rendu()
    document = Document()

    debut = 0
    for indice, ligne in enumerate(lignes):
        titre = Rendu.MOTIF_TITRE.match(ligne)
        if titre and len(titre.group(1)) == 1:
            document.titre = re.sub(r"[*_`]", "", titre.group(2)).strip()
            document.titre_html = rendu.inline(titre.group(2))
            debut = indice + 1
            break

    reste = lignes[debut:]
    curseur = 0
    while curseur < len(reste) and not reste[curseur].strip():
        curseur += 1

    bloc: list[str] = []
    while curseur < len(reste) and reste[curseur].strip():
        bloc.append(reste[curseur].strip())
        curseur += 1
    texte_bloc = " ".join(bloc)
    italique_complet = (
        texte_bloc.startswith("*")
        and texte_bloc.endswith("*")
        and not texte_bloc.startswith("**")
    )
    if italique_complet:
        document.chapo_html = f'<div class="chapo">{rendu.blocs(bloc)}</div>'
        document.chapo_texte = re.sub(r"[*_`]", "", texte_bloc).strip()
        reste = reste[curseur:]

    document.corps_html = rendu.blocs(reste)
    document.sommaire = rendu.sommaire
    return document
