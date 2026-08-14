# Dispositif — n° 1, *Les grands nombres de la société française*

Conventions propres à ce numéro. Elles ne valent que pour lui : le CLAUDE.md porte les invariants du magazine, ce fichier porte la réponse d'un numéro à sa question. Un numéro ultérieur peut s'en inspirer, à condition de le dire et de rejustifier ce qu'il reprend.

## Question

Quels sont les ordres de grandeur qui déterminent réellement le pays, indépendamment de leur présence médiatique ?

**Thèse de travail** : le poids réel d'un phénomène et son poids médiatique sont deux grandeurs distinctes, et l'écart entre les deux est lui-même un objet d'enquête.

## Méthode de classement

Le numéro hiérarchise des grandeurs incommensurables — un décès, un euro et une personne exposée ne sont pas la même unité. Quatre critères sont combinés, et énoncés explicitement au lecteur :

| Critère | Question posée |
|---|---|
| **Masse** | Combien de personnes sont concernées, ou combien de milliards circulent ? |
| **Durée** | L'effet dure-t-il des décennies ou une saison ? |
| **Irréversibilité** | Peut-on revenir en arrière ? |
| **Effet de levier** | Le chiffre en commande-t-il d'autres ? |

**Critère explicitement écarté** : la fréquence de citation médiatique — c'est l'objet de l'exercice, pas son instrument.

Quand deux critères s'opposent, l'arbitrage est dit au lecteur. Le solde naturel négatif est n° 1 non par sa masse (−6 000, c'est petit) mais par son effet de levier et son irréversibilité, et l'entrée le justifie dans un « pourquoi c'est le n° 1 ».

## Indice de sous-exposition

Échelle fixe pour ce numéro, à ne pas modifier ni étendre en cours de route :

| Symbole | Signification |
|---|---|
| ⚪ | correctement traité / très exposé |
| 🟡 | exposé par à-coups, ou sur-exposé en polémique et sous-exposé en structure |
| 🟠 | sujet visible, ampleur invisible |
| 🔴 | quasi invisible — écart maximal entre poids réel et couverture |

L'indice se justifie en une ligne accolée au symbole (« 🟠 traité comme une curiosité statistique annuelle »), jamais posé sans motif.

## Structure du numéro

1. **Titre + chapô** — état des données, nature des sources, avertissement sur les millésimes.
2. **Méthode** — les quatre critères, puis les avertissements méthodologiques numérotés (non-additivité des décès attribuables ; fractions attribuables = modèles et non comptages ; les chiffres de délinquance mesurent en partie la propension à porter plainte ; certaines rassurances sont fondées).
3. **Le Top 10** — entrées 1️⃣ à 🔟, gabarit ci-dessous.
4. **Tableau de synthèse** — masse réelle contre saillance médiatique.
5. **Le peloton juste derrière** — rangs 11 à 20, un paragraphe dense chacun, chiffre en gras, source entre parenthèses en italique.
6. **Les faux grands nombres : ce qui va mieux qu'on ne le croit** — tableau « peur répandue » / « ce que disent les données », suivi des indicateurs qui, eux, se dégradent réellement. C'est l'implémentation de la règle 6 du CLAUDE.md dans ce numéro.
7. **Ce que l'enquête révèle sur la structure du biais** — analyse, pas énumération. Les cinq biais nommés : événement, identification, agentivité, âge, décalage temporel.
8. **Sources primaires** — regroupées par domaine.
9. **Avertissement de clôture** en italique.

## Gabarit d'une entrée du Top 10

```markdown
### 3️⃣ **13,7 millions de personnes en affection de longue durée** — et les deux tiers de la dépense remboursée

**Indice de sous-exposition : 🔴 quasi invisible**

| Donnée | Valeur (millésime **2021**) | Source |
|---|---|---|
| … | … | … |

> **⚠️ Précautions de lecture** (quand le chiffre est piégeux)

**Pourquoi c'est structurant :** … (2 à 4 paragraphes d'analyse)
```

**Le titre de l'entrée est le chiffre, pas le thème.** « 20 148 morts par chute chez les 65 ans et plus » et non « les chutes des personnes âgées ». Ajouter la comparaison d'ancrage dans le titre quand elle existe (« — six fois la route »).

**Millésime du tableau.** Quand toutes les lignes d'un tableau partagent une année de mesure, elle est portée dans l'en-tête de colonne, comme ci-dessus. Quand l'entrée croise plusieurs millésimes, l'en-tête reste « Valeur » et chaque cellule porte son année : un millésime en en-tête vaudrait alors pour des lignes qu'il ne couvre pas.

## Corrections apportées au dispositif le 14 août 2026

Le gabarit ci-dessus donnait pour exemple « 13,8 millions de personnes en affection de longue durée — soit un Français sur cinq », avec un millésime 2022. Les vérifications ont invalidé les deux moitiés de la formule, et l'éditeur corrige ici son propre dispositif plutôt que de laisser un exemple fautif gouverner l'écriture du numéro.

1. **La valeur.** Le 13,8 millions (2022) provient du *Points de repère* n° 54 de la CNAM, publication qui n'a pu être ouverte ni par le journaliste ni par le fact-checker : elle reste `[NON VÉRIFIÉ]` et n'est pas publiable. La valeur vérifiée en source primaire est 13,7 millions, millésime 2021, tous régimes (IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024).
2. **Le ratio.** « Un Français sur cinq » rapportait l'effectif à la population française. Le dénominateur réel de la source est de 68,7 millions de personnes « ayant eu au moins 1 euro de remboursement dans l'année », qui n'est pas la population résidente (67,4 millions au 1ᵉʳ janvier 2021). L'ancrage de titre est donc reporté sur la part de la dépense remboursée, qui est mesurée sur un périmètre unique.

La leçon vaut au-delà de l'exemple : **un gabarit n'est pas une source.** Un chiffre inscrit dans le dispositif d'un numéro suit le même circuit de vérification que les autres, et tombe comme les autres.

## Émojis employés

1️⃣ à 🔟 pour les rangs, ⚪ 🟡 🟠 🔴 pour l'indice, ⚠️ pour les encadrés de précautions. Aucun autre.
