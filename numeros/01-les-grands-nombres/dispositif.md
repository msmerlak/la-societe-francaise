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

*Modifiée par la refonte du 16 août 2026, voir plus bas : une « Ouverture » s'intercale entre le chapô et la « Méthode », et le point 7 devient la conclusion du numéro.*

1. **Titre + chapô** — état des données, nature des sources, avertissement sur les millésimes.
2. **Méthode** — les quatre critères, puis les avertissements méthodologiques numérotés (non-additivité des décès attribuables ; fractions attribuables = modèles et non comptages ; les chiffres de délinquance mesurent en partie la propension à porter plainte ; certaines rassurances sont fondées).
3. **Le Top 10** — entrées 1️⃣ à 🔟, gabarit ci-dessous.
4. **Tableau de synthèse** — masse réelle contre saillance médiatique.
5. **Le peloton juste derrière** — rangs 11 à 20, un paragraphe dense chacun, chiffre en gras, source entre parenthèses en italique.
6. **Les faux grands nombres : ce qui va mieux qu'on ne le croit** — tableau « peur répandue » / « ce que disent les données », suivi des indicateurs qui, eux, se dégradent réellement. C'est l'implémentation de la règle 6 du CLAUDE.md dans ce numéro.
7. **Ce que l'enquête révèle sur la structure du biais** — analyse, pas énumération. Les cinq biais nommés : événement, identification, agentivité, âge, décalage temporel.
8. **Sources primaires** — regroupées par domaine.
9. **Avertissement de clôture** en italique.

## Gabarit d'un article du Top 10

*Remplacé par le gabarit de la refonte du 16 août 2026, plus bas. Conservé ici parce que les règles de titre et de millésime qui le suivent restent en vigueur.*

```markdown
### 3️⃣ **13,7 millions de personnes en affection de longue durée** — et les deux tiers de la dépense remboursée

**Indice de sous-exposition : 🔴 quasi invisible**

| Donnée | Valeur (millésime **2021**) | Source |
|---|---|---|
| … | … | … |

> **⚠️ Précautions de lecture** (quand le chiffre est piégeux)

**Le mécanisme.** … comment le phénomène se produit
**L'ancrage.** … la même série vingt ans plus tôt, les voisins européens, une grandeur familière
**Ce que la mesure ne dit pas.** … la limite du chiffre, tirée des verdicts de vérification
**L'objectif affiché et le résultat mesuré.** … quand un objectif public a été chiffré
**Pourquoi ce rang.** … l'arbitrage entre les quatre critères, dit au lecteur
```

**Le titre de l'article est le chiffre, pas le thème.** « 20 148 morts par chute chez les 65 ans et plus » et non « les chutes des personnes âgées ». Ajouter la comparaison d'ancrage dans le titre quand elle existe (« — six fois la route »).

**Millésime du tableau.** Quand toutes les lignes d'un tableau partagent une année de mesure, elle est portée dans l'en-tête de colonne, comme ci-dessus. Quand l'entrée croise plusieurs millésimes, l'en-tête reste « Valeur » et chaque cellule porte son année : un millésime en en-tête vaudrait alors pour des lignes qu'il ne couvre pas.

**Les cinq rubriques d'analyse ne sont pas toutes obligatoires.** « L'objectif affiché et le résultat mesuré » ne s'écrit que si un objectif public a été chiffré ; les quatre autres sont dues. Elles ne sont pas des intertitres mais des amorces de paragraphe en gras, pour que l'article reste lisible d'un trait et que la newsletter n'y ajoute pas de niveau de titre.

## Modification du gabarit le 15 août 2026 — l'entrée devient un article

Le Top 10 était publié en entrées courtes : tableau, précautions, deux à quatre paragraphes de « pourquoi c'est structurant ». Les dix sujets sont désormais développés en articles d'environ deux pages (900 à 1 100 mots). Le peloton (rangs 11 à 20) reste en paragraphes denses : sa fonction dans ce dispositif est de montrer qu'il existe une queue de distribution, pas de la détailler.

**Ce que ce développement n'autorise pas.** Aucun chiffre nouveau qui ne provienne d'une fiche de `collecte/`, aucun ratio non recalculé sur les valeurs des tableaux de l'article lui-même, aucune paraphrase en prose d'un tableau déjà donné. La longueur vient de quatre matériaux, et d'eux seuls : le mécanisme, l'ancrage comparatif, ce que la mesure ne dit pas, l'écart entre l'objectif affiché et le résultat mesuré. Les valeurs ajoutées à cette occasion et qui ne sont couvertes par aucun rapport de `verifications/` portent dans le texte la mention « niveau collecté », comme le prévoit déjà la section « Méthode » du numéro.

**Une correction de fond emportée par la relecture.** L'entrée 3 écrivait que le retrait de l'ALD 12 de la liste en 2011 avait fait cesser de compter « plus de 250 000 personnes ». La fiche de collecte dit l'inverse : les 256 320 assurés relevés au titre de l'ALD 12 en 2022 sont un **effectif résiduel**, c'est-à-dire des droits ouverts avant 2011 et non éteints. Le fait démontre mieux encore la nature administrative de la série, mais dans l'autre sens, et le texte est corrigé.

## Refonte de forme du 16 août 2026 — le numéro devient un journal

Aucun chiffre, aucune source, aucune réserve n'a changé à cette occasion : l'état des données reste celui du 14 août 2026. Ce qui change est l'ordre du texte, la longueur relative des articles, et deux sections nouvelles.

### Le gabarit d'article, refait

Le gabarit de la section « Gabarit d'un article du Top 10 » ci-dessus est remplacé par celui-ci, appliqué aux dix articles. Le motif : dans la version du 15 août, le lecteur traversait une trentaine de lignes d'appareil — indice, trois tableaux empilés, encadré de précautions — avant la première phrase lui disant quoi en penser.

```markdown
### 3️⃣ **titre : le chiffre, puis l'ancrage**

attaque — deux ou trois phrases de prose portent le résultat, avant tout tableau

| tableau principal |

#### intertitre de développement
prose, puis le tableau secondaire au paragraphe qui l'emploie

#### Pourquoi ce rang
l'arbitrage entre les quatre critères

**Indice de sous-exposition : 🔴** — motif en une ligne

> **⚠️ Précautions de lecture.** …
```

Cinq déplacements, éprouvés d'abord sur un spécimen de l'article 1, puis généralisés :

1. **Une attaque avant tout appareil.**
2. **Un tableau à la fois, là où il sert** — les tableaux secondaires descendent au paragraphe qui les emploie.
3. **Les précautions de lecture ferment l'article.** Elles arment un lecteur qui sait déjà de quoi il s'agit ; en tête, elles arrêtent celui qui l'ignore encore. Elles ne sont jamais allégées par ce déplacement, et deux d'entre elles ont au contraire absorbé une réserve qui vivait dans le corps du texte (articles 1 et 9).
4. **Des intertitres de niveau `####`** quand une amorce ouvre un développement. Les amorces en gras du gabarit précédent — « Le mécanisme », « L'ancrage », « Ce que la mesure ne dit pas » — disparaissent quand elles n'annonçaient qu'un paragraphe. La contrainte de newsletter qui les avait fait préférer aux titres est levée : `####` reste du Markdown standard.
5. **La justification du rang ferme l'argument**, avec l'indice de sous-exposition, au lieu de l'ouvrir.

### La hiérarchie de longueur, et son critère

Dix articles de même poids ne font pas un journal. Les articles sont répartis en trois rangs de longueur :

| Rang de longueur | Articles | Motif |
|---|---|---|
| Développé | 1, 3, 7, 8 | le numéro s'y joue, ou la mesure y est la plus piégeuse |
| Moyen | 2, 4, 5, 6 | masses déjà notoires, dont l'apport tient dans une décomposition |
| Brève dense | 9, 10 | une seule opération de lecture, que les tableaux portent presque seuls |

**La longueur ne suit pas le rang** — sans quoi elle ne dirait rien de plus que lui. Elle suit la quantité d'appareil qu'un chiffre exige pour être lu sans contresens, et le nombre d'autres articles qu'il commande. D'où les quatre articles développés : le 1ᵉʳ parce qu'il commande cinq autres et ouvre le numéro ; le 3ᵉ et le 8ᵉ parce qu'ils portent les deux seuls 🔴 et que leur mesure est la plus traîtresse du numéro — un effectif administratif que des règles d'entrée déplacent, une hausse dont la source impute la totalité à l'enregistrement ; le 7ᵉ parce qu'il porte la plus grosse masse de vies, une interdiction d'addition et une estimation contestée, trois choses qu'on ne peut pas écrire vite. Le 2ᵉ, charnière du numéro, est traité en moyen sans contradiction : son argument décisif tient dans une seule ligne de sa source, et une démonstration courte n'a pas besoin d'un texte long.

### Ouverture et conclusion

**Une ouverture** précède désormais la « Méthode ». Ce n'est pas un résumé des dix résultats — le tableau de synthèse le fait — mais une vue d'ensemble problématique : la question, la tension entre poids réel et poids médiatique, et ce que l'enquête a trouvé de contre-intuitif. Elle porte l'argument, pas les données ; les rares chiffres qu'elle cite figurent déjà dans le numéro et emportent avec eux leur niveau de confiance. La « Méthode » en est resserrée d'autant : elle n'a plus la charge d'accrocher le lecteur, et conserve les quatre critères, le critère écarté, les deux niveaux de confiance, les quatre avertissements de lecture et ce que le numéro écarte.

**La section sur la structure du biais devient la conclusion** — dernier texte du numéro avant les seules annexes que sont les sources primaires et l'avertissement de clôture. Elle est réécrite comme telle, sous trois contraintes :

- elle explique par des mécanismes — biais d'événement, d'identification, d'agentivité, d'âge, de décalage temporel — et ne met en cause aucun groupe ; aucun de ces mécanismes ne suppose d'intention ;
- chaque biais nommé est rattaché à des articles précis, plutôt qu'énoncé en général ;
- elle rappelle en ouverture ce que le numéro n'a pas mesuré. La « Méthode » écarte la fréquence de citation médiatique comme instrument : le numéro peut exhiber l'écart entre une masse et le traitement qu'elle reçoit, il ne l'a pas quantifié, et l'indice de sous-exposition est un jugement déclaré. C'est ce qui sépare cette conclusion d'un réquisitoire.

Un sixième mécanisme y est ajouté, tiré de la matière du numéro et non de l'angle : la mesure se déplace en même temps que la chose mesurée — tabac, particules fines, chutes —, et c'est chaque fois le producteur de la donnée qui porte la réserve. Il explique aussi pourquoi la rubrique des contre-paniques existe.

### Une incohérence interne corrigée

Le commentaire du tableau de synthèse annonçait « trois articles » portant l'indice 🔴 quand le tableau n'en porte que deux, et la conclusion comptait « trente pathologies » d'ALD quand l'article 3 en compte vingt-neuf. Deux décomptes internes au numéro, corrigés sans que la valeur d'aucune source soit touchée.

### Ce que la refonte n'a pas obtenu, et pourquoi

La cible de réécriture était d'environ 14 000 mots contre 19 000, à chiffres, sources et réserves constants. Elle n'est pas atteinte : le numéro passe de 19 139 à 18 960 mots, la prose des articles reculant d'environ un cinquième pendant que l'ouverture, la conclusion et les dix attaques ajoutent quelque 1 700 mots.

Le motif est arithmétique et mérite d'être noté pour les numéros suivants. Ce qui n'est pas compressible sans retirer un chiffre, une réserve ou une source — les 36 tableaux, les dix encadrés de précautions, le peloton, les faux grands nombres, les sources primaires — pèse à lui seul de l'ordre de 12 000 mots. Atteindre 14 000 supposerait de ramener la prose des dix articles à moins de 300 mots chacun, c'est-à-dire d'écrire les articles de tête à la densité des entrées du peloton, ou de renoncer à des valeurs. Le dispositif retient l'ordre de priorité du CLAUDE.md : les règles de fond priment sur la forme, la contrainte de longueur cède la première. La hiérarchie de longueur, elle, est tenue en ordre — aucun article moyen n'est plus long qu'un article développé, aucune brève n'est plus longue qu'un article moyen — mais son amplitude reste faible, de 1 000 à 1 550 mots environ.

La leçon pour un numéro futur : un objectif de volume se fixe **avant** la collecte, parce qu'après la vérification il ne peut plus être tenu que par la suppression de chiffres déjà vérifiés.

## Corrections apportées au dispositif le 14 août 2026

Le gabarit ci-dessus donnait pour exemple « 13,8 millions de personnes en affection de longue durée — soit un Français sur cinq », avec un millésime 2022. Les vérifications ont invalidé les deux moitiés de la formule, et l'éditeur corrige ici son propre dispositif plutôt que de laisser un exemple fautif gouverner l'écriture du numéro.

1. **La valeur — corrigée, puis partiellement rétablie.** Le 13,8 millions (2022) était attribué au *Points de repère* n° 54 de la CNAM, publication qu'aucun des trois agents n'a pu ouvrir. Une revérification ciblée l'a finalement retrouvé, littéralement et avec son dénominateur, dans un article scientifique reprenant les mêmes données CNAM : la valeur tient, **mais pas son attribution**. Citer le *Points de repère* aurait créditée une publication que personne n'a lue. Le numéro retient 13,7 millions (2021, tous régimes, IGAS/IGF) comme chiffre de titre — parce que toutes les autres lignes de l'entrée en dépendent, même source, même millésime, même champ — et publie 13,8 millions (2022) comme point plus récent, sourcé sur l'article effectivement consulté.
2. **Le ratio — fautif dans les deux millésimes.** « Un Français sur cinq » rapportait l'effectif à la population française. Le dénominateur réel est de 68,7 millions de personnes « ayant eu au moins 1 euro de remboursement dans l'année » pour 2021, et « la population ayant consommé des soins » pour 2022 — ni l'un ni l'autre n'est la population résidente (67,4 millions au 1ᵉʳ janvier 2021). L'ancrage de titre est donc reporté sur la part de la dépense remboursée, qui est mesurée sur un périmètre unique.

Deux leçons, et la seconde n'est pas celle qu'on attendait. **Un gabarit n'est pas une source** : un chiffre inscrit dans le dispositif d'un numéro suit le même circuit de vérification que les autres, et tombe comme les autres. Mais un chiffre non vérifié n'est pas non plus un chiffre faux : celui-ci a tenu, et c'est son chemin d'attribution qui était mauvais. La distinction mérite d'être tenue, faute de quoi la vérification cesse d'être un contrôle pour devenir une présomption.

## Émojis employés

1️⃣ à 🔟 pour les rangs, ⚪ 🟡 🟠 🔴 pour l'indice, ⚠️ pour les encadrés de précautions. Aucun autre.
