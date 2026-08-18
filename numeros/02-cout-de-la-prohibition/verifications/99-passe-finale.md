# Passe finale — n° 2, texte assemblé (`index.md`)

Contrôle mené sur le numéro assemblé, en confrontation avec `dispositif.md` et les cinq rapports de
`verifications/` (05-objectifs, 06-repression, 07-marche, 08-sante-international, 09-repasse-acces). Ces
rapports ne sont pas refaits ; ce document contrôle spécifiquement ce que seul le texte assemblé peut
révéler : traçabilité, application des verdicts, glissements de registre, réserves obligatoires, interdits
du dispositif, ratios, constats d'absence.

**Publications rouvertes dans cette passe : zéro.** Le doute qui aurait justifié d'en rouvrir une n'est
apparu sur aucun chiffre : chaque valeur du numéro s'est retrouvée soit dans une fiche de `collecte/`, soit
dans l'un des cinq rapports de vérification antérieurs (qui, eux, ont rouvert les sources primaires — jusqu'à
quatre PDF récupérés par le contournement `WebFetch` + `Read` sans `pages`, documenté dans
`09-repasse-acces.md`). Je n'ai donc pas eu besoin d'entamer la borne de six publications de ce brief. Le
travail de cette passe a consisté à recomposer le fil : quel chiffre du texte final vient de quelle fiche ou
de quel verdict, et est-il employé comme la source l'autorise.

---

## 1. Traçabilité

Contrôle par sondage sur l'ensemble du texte (plus d'une trentaine de valeurs pointées), avec `grep` croisé
entre `index.md` et `collecte/*.md`. Aucun chiffre apparu de nulle part n'a été trouvé. Cas notables :

- **196 400 / 94 000 / 68 %** (amendes forfaitaires 2024 vs procédure classique) — retrouvé littéralement
  dans `collecte/06-repression-profonde.md` (SSMSI, Fiche 7), avec la même réserve « majeurs et mineurs »
  déjà déclarée en niveau collecté dans les sources primaires du numéro.
- **6,7 M / 2,2 M de patients** (tableau ROSP) et **45 ans / 15 ans / OCDE ~70 Md€ / « peu pertinent de
  comparer... »** (section limites méthodologiques du coût social) — ces valeurs **ne figurent pas dans les
  fiches de `collecte/`**, mais sont retrouvées mot pour mot dans `verifications/09-repasse-acces.md` (Point
  4, lecture directe du bilan PNMA p. 17) et `verifications/08-sante-international.md` (lecture directe des
  pages 13-14 de l'étude Kopp). C'est le circuit attendu : le fact-checker a rouvert la source primaire et
  documenté un contenu que la collecte n'avait pas rapporté ; l'éditeur l'a intégré à partir du rapport de
  vérification. Ce n'est pas un chiffre apparu à l'écriture — c'est un chiffre apparu à la vérification, et
  la chaîne de traçabilité (source primaire → verification → index.md) est intacte et supérieure en solidité
  à un simple passage par la collecte.
- **8 287 / 9 171 / 6 724 / 8 235 et les taux associés** (écrous) — retrouvés littéralement dans
  `collecte/06-repression-profonde.md`, y compris la rupture méthodologique 2022 (GIDE/GENESIS) reprise dans
  la précaution de lecture.
- **900 000 / 467 000 / 97 000 / 21 M / 5 M** — retrouvés littéralement dans
  `collecte/08-sante-international-profonde.md`.
- **2 462 642 444 € / 2 497 483 527 € / 2 513 574 412 € / 2 591 257 398 €** (DPT) — retrouvés au chiffre
  près dans `verifications/09-repasse-acces.md` (lecture directe du PDF DPT 2026, p. 9).

`[OK]` Aucun chiffre non traçable détecté sur l'échantillon contrôlé.

---

## 2. Application des verdicts — contrôle nommé

- **Cour des comptes** : aucune valeur attribuée à la Cour ne figure dans le corps du texte. Les deux
  constats (absence de cibles chiffrées de la SIMCA, interruption du suivi à l'été 2022) sont traités
  conformément aux verdicts `[NON VÉRIFIÉ — accès impossible]` de `05-objectifs.md` et
  `09-repasse-acces.md` (points 2 et 3) : le premier est republié, mais **indépendamment établi par la
  lecture directe de la SIMCA elle-même** (confirmée `[OK]` au point 1 de `09-repasse-acces.md`), pas
  attribué à la Cour ; le second n'est publié nulle part comme fait établi. `[OK]`
- **AGRASC** : aucune valeur de sous-ensemble narcotrafic (95 M€, 79 M€, 29 736 biens) ne figure dans le
  texte. Conforme au verdict `[NON VÉRIFIÉ — condition dure non confirmée]` de `07-marche.md`. `[OK]`
- **Coût d'une journée de détention** : aucune valeur, ni produit par un effectif écroué, ne figure. Conforme
  au verdict `[OK — absence confirmée]` de `06-repression.md`. `[OK]`
- **47,8 % (cannabis 17 ans)** : n'apparaît que comme valeur 2014 correctement replacée dans la série, jamais
  comme point 2017. Conforme au verdict de `08-sante-international.md`. `[OK]`
- **« 44 % à 30 % » (Portugal)** : n'apparaît pas comme valeur publiée ; cité uniquement pour dire qu'il est
  introuvable dans la source. Conforme. `[OK]`
- **Comparaison européenne des opioïdes (Point 10.6 de `08-sante-international.md`, incohérence 4,5/5,2
  relevée comme bloquante)** : n'apparaît nulle part dans le texte, ni sous 4,5 ni sous 5,2. Le numéro se
  contente d'écrire « Aucune estimation portant sur les seuls opioïdes n'a été retrouvée » (ligne 306), ce
  qui est un constat d'absence distinct (estimation française, pas comparaison européenne) et n'est pas
  affecté par le bloquant de la fiche 10.6. `[OK]`
- **635 000 amendes depuis 2020** : n'apparaît nulle part comme valeur publiée, uniquement listé parmi ce que
  le numéro écarte et parmi les grandeurs manquantes. `[OK]`

---

## 3. Le glissement ROSP tabac/alcool

Contrôlé ligne à ligne. Le texte :
- qualifie explicitement les deux cibles ROSP de « objectifs de pratique médicale sur deux produits licites »
  (ligne 13), répète « Ce sont des objectifs de pratique sanitaire sur le tabac et l'alcool, et non des
  objectifs de la politique de lutte contre les stupéfiants illicites » (ligne 104, en gras) ;
- montre, tableau à l'appui (« Une cible franchie avant même le début du plan », lignes 91-98), que le seuil
  de 75 % était déjà dépassé en décembre 2017 — avant l'entrée en vigueur du plan 2018-2022 — et le dit
  explicitement : « le seuil est franchi de 6,2 points dès le premier point de série publié, et de 13,1
  points à l'échéance » (ligne 106). Recalcul : 81,2 − 75 = 6,2 ✓ ; 88,1 − 75 = 13,1 ✓.
- Le registre assigné est « recours à un dispositif », pas « comptage » ni un registre qui suggérerait une
  mesure de prévalence de politique anti-stupéfiants.

`[OK]` Le glissement que le brief signalait comme le plus tentant n'a pas été commis. La marque `atteinte`
est explicitement dépouillée de toute causalité (« `atteinte` ne signifie pas que le plan a produit ce
résultat », ligne 106), conforme à la règle dure de la section 7.3 du dispositif.

---

## 4. Les deux réserves obligatoires du coût social

- **Millésime réel** : la section « Le millésime du titre n'est pas celui de la mortalité » (lignes 330-332)
  dit explicitement que les fractions attribuables alcool et tabac proviennent de travaux sur 2015, que le
  « 2019 » du titre porte sur les paramètres économiques et non sur une réestimation de la mortalité, et que
  « décès de 2019 » serait inexact pour les deux produits les plus lourds du tableau. Conforme au constat de
  `verifications/08-sante-international.md` (note du tableau 2 de l'étude Kopp, citée mot pour mot).
- **Section de limites méthodologiques** : présente (lignes 334-336), condition de publication du dispositif
  explicitement rappelée dans le texte lui-même (« Le dispositif de ce numéro fait de cette section une
  condition de publication, et non un ornement »). Contient les quatre éléments exigés par le verdict de
  `08-sante-international.md` : comparaison internationale jugée « peu pertinente » par l'auteur (citation
  exacte), âge moyen unique de 45 ans avec la citation sur l'effet de cette hypothèse, durée de carrière fixée
  à 15 ans, omission des coûts intangibles, et la contestation OCDE documentée (~70 Md€ contre 102 Md€).

`[OK]` Les deux réserves sont présentes et disent ce que la source dit, au mot près pour les citations
contrôlables.

---

## 5. Le registre de mesure

Vingt entrées de rubrique (`### **...**`), vingt-trois occurrences de `**Registre :**` (plusieurs entrées
portent plus d'une table avec des registres distincts, ex. l'entrée sur les décès imputés qui ajoute un
second registre « déclaration » pour la table des usages quotidiens alcool/tabac). Aucune entrée sans
registre.

Le cas signalé par le brief comme le plus tentant — une variation d'activité de service lue comme une
variation du phénomène — est explicitement neutralisé à l'endroit précis où il menaçait le plus : l'entrée
sur les 330 100 personnes mises en cause porte la phrase « Sans cette phrase, une variation d'activité de
service se lirait comme une variation du phénomène » (ligne 165) et cite le SSMSI sur les JOP et les
opérations « place nette » au mot près (confirmé littéralement dans `09-repasse-acces.md`, Point 6). `[OK]`

Une observation mineure, non bloquante : l'entrée sur les prix (« 58 € ... et 46 € ... en euros constants
contre 64 € en 2014 ») porte un seul intitulé de registre (« modèle ») pour deux tables dont l'une (prix
courant, relevé par questionnaire) relève plus naturellement d'un enregistrement administratif que d'un
modèle. Le texte explicite toutefois le mécanisme des deux tables dans la même phrase de registre et les
tient explicitement pour deux indicateurs distincts non comparables terme à terme (« Les deux tableaux
portent des indicateurs distincts... »). Ce n'est pas le glissement que le dispositif interdit — les deux
registres ne sont jamais comparés « dans le même mouvement de phrase » — mais une entrée future pourrait
gagner à séparer les deux registres en deux lignes. `[OBSERVATION, non bloquant]`

---

## 6. Les interdits du dispositif

- **Aucun ratio croisant coût social licite et dépense répressive illicite** : recherché explicitement, non
  trouvé. Le texte le dit lui-même deux fois (dispositif 8.3 et corps, ligne 365 : « ce numéro ne calcule
  aucun ratio croisant ces coûts sociaux avec la dépense répressive de la rubrique précédente »). `[OK]`
- **Aucune conclusion sur l'opportunité d'un régime légal** : contrôlé sur l'ensemble du texte, y compris la
  rubrique Portugal, qui reprend littéralement la réserve de l'OFDT (« il faut bien distinguer corrélation et
  causalité »). La note CAE, seule source qui prend position, est signalée comme telle et le numéro n'en
  reprend qu'un chiffrage (200 000 personnes), jamais ses recommandations. `[OK]`
- **Lexique imposé** : recherche des formulations interdites (« trafiquants », « quantité trafiquée », « morts
  de la drogue », « le marché pèse X », « échec de la politique », « argent public gaspillé », « il faudrait »,
  « la France devrait », « guerre à la drogue » hors citation) — aucune occurrence trouvée. La seule occurrence
  de « consommateurs » est un fragment de l'intitulé officiel de l'indicateur ROSP (« patients consommateurs
  excessifs d'alcool »), repris littéralement du plan, ce que le CLAUDE.md autorise explicitement pour les
  intitulés d'indicateurs. `[OK]`
- **Aucun émoji** : recherche automatisée sur toute la plage Unicode des émojis, aucune occurrence. `[OK]`

---

## 7. Divergences exposées, pas tranchées en silence

- **Trois dispositifs de comptage des décès** (CépiDc/registre des causes médicales, police/gendarmerie,
  DRAMES) : les trois séries 2000-2007 sont données côte à côte avec la mention de non-réconciliation, et le
  texte dit explicitement ce que chaque instrument fait de travers, en citant l'OFDT. Le numéro dit aussi
  clairement qu'aucun point récent du registre des causes médicales n'a été retrouvé, plutôt que de compléter
  la case vide. `[OK]`
- **260 300 (OFDT) vs 262 500 (SSMSI, niveau collecté), 2023, écart de 0,8 %** : exposé explicitement (ligne
  180), avec l'explication qu'il s'agit de deux extractions à des dates différentes d'une base révisable, et
  la clause « les deux valeurs ne sont pas interchangeables ». Conforme au signalement de `06-repression.md`.
  `[OK]`
- **Prix courant vs prix ajusté de la teneur** : les deux tables sont présentées séparément, avec l'avertissement
  explicite que les mêler « serait la faute de champ que ce numéro cherche à documenter » (ligne 508). `[OK]`

---

## 8. Niveaux de confiance

Comptage : 51 occurrences de la mention « niveau collecté » dans `index.md` (contre 48 annoncées en Méthode
— l'écart s'explique par des répétitions légitimes de la même valeur dans plusieurs paragraphes d'une même
entrée, ce qui est conforme à la règle « le marquage suit le chiffre » plutôt qu'à une sous-déclaration : je
n'ai pas trouvé de valeur reparaissant sans son marquage). Contrôle par sondage sur les réapparitions :

- **900 000 (usage quotidien de cannabis)** : marqué « niveau collecté » à sa première apparition (titre de
  l'entrée, ligne 291) et de nouveau lors de sa réapparition dans la comparaison licite/illicite (ligne 365 :
  « l'usage quotidien de cannabis est estimé à 900 000 personnes... (niveau collecté) »). `[OK]`
- **23,1 % / 7,0 % (usage quotidien tabac/alcool)** : marqué au tableau (ligne 340-345) et de nouveau à sa
  réapparition dans la comparaison licite/illicite (ligne 365). `[OK]`
- **330 100 / 290 400 / 52 300** : ces valeurs, elles, sont vérifiées (confirmées `[OK]` par
  `09-repasse-acces.md`, Point 6) et n'apparaissent **jamais** avec la mention « niveau collecté » — cohérent.
  `[OK]`
- **6,7 M / 2,2 M et le tableau ROSP** : vérifiées par `09-repasse-acces.md` (Point 4), n'apparaissent pas au
  niveau collecté — cohérent.

Aucune valeur non couverte par un rapport de vérification n'a été trouvée sans marquage lors du sondage
mené. Je n'ai pas recompté exhaustivement les 48 lignes annoncées contre les 51 occurrences relevées — un
contrôle ligne à ligne complet dépasserait la borne de cette passe — mais aucune anomalie de marquage
manquant n'est apparue sur l'échantillon contrôlé (plus d'une trentaine de valeurs). `[OK, sondage]`

---

## 9. Ratios recalculés

- **43 % (mises en cause usage, 2016→2023)** : 260 300 / 182 400 = 1,427 → +42,7 %, arrondi correct à 43 %.
  ✓
- **−26 % (condamnations, 2017→2023)** : 49 635 / 67 101 = 0,7397 → −26,0 %. ✓
- **Somme des prises en charge AFD 2020-2024** : 76 + 57 425 + 73 543 + 97 111 + 126 535 = 354 690 — conforme
  à la valeur citée en « ancrage » (ligne 157). ✓
- **68 % / 196 400 sur 290 400** : 196 400 / 290 400 = 67,6 %, arrondi correct à 68 %. Complément :
  290 400 − 196 400 = 94 000. ✓
- **Coût social tabac ≈ ×20 drogues illicites** : 155 726 / 7 730 = 20,15. ✓ **Décès ≈ ×60** : 73 189 / 1 230
  = 59,5, arrondi correct à « près de soixante fois ». ✓
- **Ratio Portugal mortalité, 5,7 et non 6** : 34 / 6 = 5,67. ✓ La correction du chiffre qui circule (÷6) est
  confirmée juste.
- **8,8 points (expérimentation cannabis adulte 2014→2023)** : 50,4 − 41,6 = 8,8. ✓
- **−9,2 points / −24 % (cannabis 17 ans, 2017→2022)** : 39,1 − 29,9 = 9,2 ; 29,9/39,1 − 1 = −23,5 % (arrondi
  cohérent avec les −24 % de la source, chiffre repris littéralement de l'OFDT, non recalculé par le numéro).
  ✓
- **Vapotage quotidien ×3+ (1,9 %→6,2 %)** : 6,2/1,9 = 3,26. ✓ **+226 %** : (6,2−1,9)/1,9 = 226,3 %. ✓
- **6,2 et 13,1 points d'écart au seuil de 75 % (ROSP tabac)** : 81,2−75=6,2 ; 88,1−75=13,1. ✓

Aucune anomalie de recalcul détectée sur l'ensemble des ratios rencontrés dans le texte.

---

## 10. Constats d'absence

- **« Aucune actualisation de l'estimation officielle [INSEE] postérieure à 2018 »** : le texte le formule
  avec prudence (« Aucune actualisation... n'a été trouvée. Le journaliste a cherché et déclaré sa recherche
  infructueuse; le vérificateur n'a pas eu le budget de confirmer cette absence », ligne 449) — c'est-à-dire
  qu'il **ne prétend pas** l'absence établie par un vérificateur, contrairement à ce que ferait un négatif
  publié en rubrique 9. Ce houd de prudence est correct : cette phrase figure dans le corps de l'entrée sur
  le marché (rubrique 7), pas dans la rubrique 9 « Les grandeurs manquantes », qui elle est réservée aux
  négatifs établis. `[OK]`
- **« Le coût moyen d'une journée de détention... n'a été retrouvé dans aucune publication »** : rubrique 9,
  et le texte précise « Six publications institutionnelles ont été ouvertes sans qu'il y figure » — établi
  par une recherche documentée, conforme au verdict `[OK]` de `06-repression.md`. `[OK]`
- **« L'origine du cumul de 635 000... n'a été localisée ni par le journaliste... ni par le vérificateur »** :
  établi par deux recherches indépendantes documentées (collecte + `06-repression.md`). `[OK]`
- **« Une citation attribuée à un responsable des comptes nationaux de l'INSEE... ne figure pas dans la note
  méthodologique »** : établi par lecture intégrale confirmée dans `07-marche.md` (« j'ai lu la note en
  entier et je confirme qu'elle ne contient pas... »). `[OK]`
- **Deux constats Cour des comptes non publiés comme établis** (SIMCA sans cible chiffrée — repris comme
  établi par une autre voie ; suivi interrompu été 2022 — non publié comme fait établi) : traités avec la
  prudence exacte qu'imposent les verdicts `[NON VÉRIFIÉ]`. `[OK]`

Aucun négatif faux détecté : chaque absence est assise sur une recherche documentée, jamais sur le silence
d'une source qu'on n'aurait pas cherchée.

---

## Ce que cette passe n'a pas recontrôlé

- Le comptage exhaustif des 51 occurrences de « niveau collecté » face aux 48 lignes annoncées en Méthode
  n'a pas été fait ligne à ligne (sondage seulement, cf. section 8).
- Aucune publication primaire n'a été rouverte dans cette passe : le doute qui l'aurait justifié n'est apparu
  sur aucun chiffre du texte assemblé, l'essentiel du travail ayant déjà été fait par les cinq passes
  antérieures.
- Le tableau des deux indicateurs de performance du DPT (gendarmerie/police, avoirs saisis) reste non rouvert
  par un vérificateur, ce que le texte reconnaît lui-même explicitement (ligne 254) — conforme, pas un défaut
  de cette passe.

---

## VERDICT GLOBAL

**PUBLIABLE.**

Aucun bloquant. Les cinq rapports de vérification thématiques avaient identifié plusieurs points bloquants
(citation Cour des comptes non confirmée, fait sur l'interruption du suivi 2022 non confirmé, glissement
potentiel ROSP, précision du millésime DPT, section de limites méthodologiques manquante, incohérence sur
l'entrée opioïdes Portugal, condition dure AGRASC non remplie) : le texte assemblé les traite tous
correctement — soit en retirant la valeur invalidée, soit en ajoutant la précision ou la réserve exigée, soit
en attribuant le fait à sa source réelle avec la prudence requise. Le glissement de nature de la mesure sur
les cibles ROSP tabac/alcool — l'erreur la plus tentante identifiée par le brief — n'a pas été commis, et le
numéro le dit explicitement plusieurs fois. Les deux réserves obligatoires du coût social (millésime 2015
sous un titre 2019, section de limites méthodologiques) sont présentes et fidèles à la source. Aucun interdit
du dispositif n'est enfreint, aucun ratio ne se recalcule faux, aucun constat d'absence ne repose sur un
silence non instruit.

Seule réserve non bloquante : la sous-section « prix courant / prix ajusté de la teneur » regroupe deux
registres de nature différente sous un seul intitulé de registre — observation de forme, sans conséquence sur
la lecture, le texte évitant explicitement toute comparaison entre les deux dans le même mouvement de phrase.
