"""Contrôles de diffusion et de typographie pour « La société française ».

Ce module ne vérifie pas les chiffres — c'est le travail du fact-checker, et
aucun programme ne peut le faire à sa place. Il vérifie ce qui est mécanique et
donc automatisable dans la liste « Vérification avant publication » du
CLAUDE.md : la typographie française, les contraintes de diffusion (pas de HTML
brut, tableaux à trois colonnes maximum, émojis limités à ceux du dispositif) et
la présence des sections du squelette invariant.

Un contrôle mécanique ne remplace pas une relecture ; il évite seulement qu'une
relecture soit dépensée sur des fautes qu'une machine attrape mieux.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ERREUR = "erreur"
AVERTISSEMENT = "avertissement"

INSECABLE = " "
INSECABLE_FINE = " "

# Émojis, hors flèches et opérateurs mathématiques : « − », « → » et « × » sont
# de la typographie, pas des émojis, et le CLAUDE.md les impose.
MOTIF_EMOJI = re.compile(
    "(?:[0-9#*]️⃣)"
    "|[\U0001f300-\U0001faff]"
    "|[\U0001f000-\U0001f2ff]"
    "|[☀-➿]️?"
    "|[⬀-⯿]️?"
)

# Les touches numérotées forment une famille : un dispositif qui déclare
# « 1️⃣ à 🔟 » les autorise toutes, sans avoir à les énumérer.
FAMILLE_TOUCHES = {f"{chiffre}️⃣" for chiffre in "0123456789"} | {"🔟"}


@dataclass
class Signalement:
    niveau: str
    regle: str
    ligne: int
    message: str
    extrait: str = ""

    def __str__(self) -> str:
        marque = "✖" if self.niveau == ERREUR else "▲"
        fin = f"  │ {self.extrait}" if self.extrait else ""
        return f"  {marque} l. {self.ligne:>4}  [{self.regle}] {self.message}{fin}"


def _lignes_hors_code(markdown: str) -> list[tuple[int, str]]:
    """Retourne les lignes numérotées, blocs de code exclus."""
    resultat: list[tuple[int, str]] = []
    dans_code = False
    for numero, ligne in enumerate(markdown.split("\n"), start=1):
        if ligne.strip().startswith("```"):
            dans_code = not dans_code
            continue
        if not dans_code:
            resultat.append((numero, ligne))
    return resultat


def _sans_code_ni_url(ligne: str) -> str:
    """Retire ce sur quoi les règles typographiques françaises ne portent pas."""
    sans_code = re.sub(r"`[^`]*`", " ", ligne)
    sans_lien = re.sub(r"\]\([^)]*\)", "]( )", sans_code)
    return re.sub(r"https?://\S+", " ", sans_lien)


def emojis_autorises(dispositif: Path | None) -> set[str]:
    """Lit dans le `dispositif.md` du numéro les émojis qu'il se donne le droit d'employer."""
    if dispositif is None or not dispositif.exists():
        return set()
    trouves = set(MOTIF_EMOJI.findall(dispositif.read_text(encoding="utf-8")))
    if trouves & FAMILLE_TOUCHES:
        trouves |= FAMILLE_TOUCHES
    return trouves


def controler(markdown: str, dispositif: Path | None = None) -> list[Signalement]:
    """Applique tous les contrôles à un fichier de numéro."""
    signalements: list[Signalement] = []
    lignes = _lignes_hors_code(markdown)
    autorises = emojis_autorises(dispositif)

    signalements += _controler_html(lignes)
    signalements += _controler_tableaux(lignes)
    signalements += _controler_emojis(lignes, autorises)
    signalements += _controler_typographie(lignes)
    signalements += _controler_squelette(markdown)
    signalements.sort(key=lambda s: (s.niveau != ERREUR, s.ligne))
    return signalements


def _controler_html(lignes: list[tuple[int, str]]) -> list[Signalement]:
    """« Pas de HTML brut, pas de CSS, pas de JavaScript » — contrainte de diffusion."""
    motif = re.compile(r"</?[a-zA-Z][a-zA-Z0-9-]*(?:\s[^<>]*)?/?>")
    trouves = []
    for numero, ligne in lignes:
        for balise in motif.findall(_sans_code_ni_url(ligne)):
            trouves.append(
                Signalement(
                    ERREUR,
                    "html-brut",
                    numero,
                    "balise HTML dans un fichier de numéro — le Markdown doit rester "
                    "portable vers la plateforme d'envoi",
                    balise,
                )
            )
    return trouves


def _controler_tableaux(lignes: list[tuple[int, str]]) -> list[Signalement]:
    """« Trois colonnes maximum ; au-delà, scinder en deux tableaux » — contrainte e-mail."""
    separateur = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
    trouves = []
    for indice, (numero, ligne) in enumerate(lignes):
        if not separateur.match(ligne) or "|" not in ligne:
            continue
        colonnes = len([c for c in ligne.strip().strip("|").split("|") if c.strip()])
        if colonnes > 3:
            trouves.append(
                Signalement(
                    ERREUR,
                    "tableau-large",
                    numero,
                    f"tableau à {colonnes} colonnes — les tableaux larges passent mal "
                    "en e-mail, scinder en deux tableaux",
                )
            )
    return trouves


def _controler_emojis(lignes: list[tuple[int, str]], autorises: set[str]) -> list[Signalement]:
    """« Aucun émoji hors de ceux que le dispositif définit »."""
    if not autorises:
        return []
    trouves = []
    for numero, ligne in lignes:
        for emoji in MOTIF_EMOJI.findall(ligne):
            if emoji not in autorises and emoji.rstrip("️") not in autorises:
                trouves.append(
                    Signalement(
                        AVERTISSEMENT,
                        "emoji-hors-dispositif",
                        numero,
                        f"émoji « {emoji} » absent du dispositif du numéro",
                    )
                )
    return trouves


def _controler_typographie(lignes: list[tuple[int, str]]) -> list[Signalement]:
    """Insécables, guillemets, signe moins — les règles du CLAUDE.md."""
    trouves = []
    regles = [
        (
            re.compile(r"\S \x20?(?=[%:;!?»])"),
            "insecable-avant",
            "espace ordinaire avant « : ; ! ? » » ou « % » — une insécable est due",
        ),
        (
            re.compile(r"«\x20(?=\S)"),
            "insecable-guillemet",
            "espace ordinaire après « « » — une insécable est due",
        ),
        (
            re.compile(r"\d\x20\d{3}(?!\d)"),
            "insecable-milliers",
            "séparateur de milliers en espace ordinaire — une insécable est due",
        ),
        (
            re.compile(r"\d\x20(?:Md€|M€|€|Mt|kt|ans?\b)"),
            "insecable-unite",
            "espace ordinaire entre le nombre et son unité — une insécable est due",
        ),
        (
            re.compile(r'(?<![=\w])"'),
            "guillemet-droit",
            "guillemet droit — les guillemets français « » sont la règle",
        ),
        (
            re.compile(r"(?<![\w–—−-])-\s?\d[\d.,  ]*\s?(?:%|€|Md€|M€|pts?)"),
            "signe-moins",
            "trait d'union devant une valeur négative — le signe moins « − » est la règle",
        ),
    ]
    for numero, ligne in lignes:
        nue = _sans_code_ni_url(ligne)
        if nue.strip().startswith("|") and set(nue.strip()) <= set("|-: "):
            continue
        for motif, regle, message in regles:
            correspondance = motif.search(nue)
            if correspondance:
                trouves.append(
                    Signalement(
                        AVERTISSEMENT,
                        regle,
                        numero,
                        message,
                        nue.strip()[:90],
                    )
                )
    return trouves


def _controler_squelette(markdown: str) -> list[Signalement]:
    """Le minimum commun à tous les numéros, section « Forme d'un numéro »."""
    trouves = []
    lignes = markdown.split("\n")

    if not any(re.match(r"^#\s+\S", ligne) for ligne in lignes):
        trouves.append(
            Signalement(ERREUR, "squelette", 1, "aucun titre de niveau 1 — le numéro n'a pas de titre")
        )

    attendus = {
        "méthode": "section « Méthode » absente — un numéro quantitatif dit comment il s'y est pris",
        "sources primaires": "section « Sources primaires » absente — chaque chiffre doit y avoir sa référence",
    }
    titres = " \n".join(
        ligne.lower() for ligne in lignes if re.match(r"^#{2,3}\s+", ligne)
    )
    for attendu, message in attendus.items():
        if attendu not in titres:
            trouves.append(Signalement(ERREUR, "squelette", 1, message))

    corps = [ligne.strip() for ligne in lignes if ligne.strip()]
    if corps:
        derniere = corps[-1]
        italique = derniere.startswith("*") and derniere.endswith("*") and not derniere.startswith("**")
        if not italique:
            trouves.append(
                Signalement(
                    AVERTISSEMENT,
                    "squelette",
                    len(lignes),
                    "le numéro ne se termine pas par un avertissement de clôture en italique",
                )
            )
    return trouves


def resumer(signalements: list[Signalement]) -> tuple[int, int]:
    """Compte erreurs et avertissements."""
    erreurs = sum(1 for s in signalements if s.niveau == ERREUR)
    return erreurs, len(signalements) - erreurs
