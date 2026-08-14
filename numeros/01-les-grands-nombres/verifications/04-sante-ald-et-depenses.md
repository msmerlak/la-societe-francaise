# Vérification — `collecte/04-sante-ald-et-depenses.md`

**Date** : 14 août 2026. **Verdict global : PUBLIABLE APRÈS CORRECTIONS.** Portée : les douze chiffres retenus au triage, pas la collecte entière.

**Méthode** : sources primaires rouvertes — IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024 (PDF récupéré et relu) ; DREES, *Les dépenses de santé en 2024*, *Panoramas de la DREES*, édition 2025 (PDF récupéré et relu). Le *Points de repère* n° 54 de la CNAM est resté bloqué par CAPTCHA sur toutes les voies tentées — accès direct, proxy lecteur, Wayback Machine — comme pour le journaliste.

---

## Bloquants

**[NON VÉRIFIÉ] Le chiffre d'ouverture : 13,7 M (2021) ou 13,8 M (2022) ?**

L'IGAS/IGF donne littéralement (p. 7) : « 13,7 millions de personnes (soit 19,9 % de la population) bénéficient du dispositif ALD, tous régimes confondus » — millésime 2021. C'est vérifié.

Mais un article académique republiant les données CNAM/SNDS cite le *Points de repère* n° 54 (juillet 2024) avec une valeur plus récente : « En 2022, 13,8 millions de personnes, soit 20,1 % de la population ayant consommé des soins, bénéficiaient de cette prise en charge » — encore un troisième dénominateur, distinct des 68,7 M « ayant eu au moins 1 euro de remboursement ».

La publication primaire n'ayant pu être ouverte, ce 13,8 M reste `[NON VÉRIFIÉ]`. **Le point décisif** : 13,8 M est précisément la valeur qui figure au gabarit d'entrée du `dispositif.md`. Elle ne doit pas être publiée par défaut d'accès à sa source. Le choix entre les deux millésimes doit être explicite, pas subi.

**[ERREUR] Répartition des quatre principales ALD : retenir le tableau 3, écarter le texte courant**

Le tableau 3 est intégralement reproductible : chaque pourcentage vaut effectif / 15 366 030 (« total des ALD reconnues », note de lecture du tableau). 4 168 300/15 366 030 = 27,12 % ; 3 293 020 = 21,43 % ; 2 386 370 = 15,53 % ; 1 526 110 = 9,93 %. Les quatre valeurs se recalculent au dixième de point.

Les valeurs du texte courant (32/27/19/12 %) ne se reconstruisent par aucun dénominateur cohérent : rapportées aux 12 344 220 personnes physiques, elles donneraient 33,8/26,7/19,3/12,4 %, l'écart de 1,8 point sur le cardiovasculaire étant trop grand pour un arrondi. Incohérence interne au rapport, non résolue par lui.

**Publier 27,1 / 21,4 / 15,5 / 9,9 %, jamais 32/27/19/12 %.**

**[COHÉRENCE] Les pourcentages de projection ne se recalculent pas sur la base affichée**

Le rapport annonce 14,1 à 15,0 millions en 2027, « soit une hausse respective de 7 % et 14 % par rapport à 2021 ». Or 14,1/13,7 = +2,9 % et 15,0/13,7 = +9,5 %. Les pourcentages impliquent une base 2021 proche de 13,2 M, non explicitée — vraisemblablement la « base RAC » DREES sur laquelle repose la modélisation, distincte de la population de référence citée en tête de rapport.

Publier « +7 % » ou « +14 % » à côté de « 13,7 millions » donnerait au lecteur un ratio qu'il ne peut pas recalculer. Donner la fourchette sans les pourcentages, ou signaler que la base diffère. Traiter comme une projection modélisée, jamais comme un dénombrement.

**[CHAMP] « Un Français sur cinq » n'est pas exact**

Le dénominateur de 68,7 millions est défini par la note 15 du rapport comme la « population tous régimes de l'assurance maladie — France entière ayant eu au moins 1 euro de remboursement dans l'année ». La population France entière au 1ᵉʳ janvier 2021 est de 67,4 millions (INSEE, *Bilan démographique*). Les deux populations sont proches mais conceptuellement distinctes : l'une compte des bénéficiaires ayant consommé des soins, l'autre des résidents recensés.

Écrire « une personne couverte par l'assurance maladie sur cinq », ou porter la note de champ. La formule du gabarit est à corriger.

**[CHAMP] Âge moyen : trois valeurs, non tranchables**

65 ans en synthèse (p. 1), 66 ans dans le corps (« l'âge moyen était de 41,5 ans au sein de la population française et de 66 ans parmi les assurés en ALD »), 63 ans au tableau 3 (régime général, 2022). Champs et millésimes légèrement différents, que le rapport ne détaille pas assez pour arbitrer. Choisir une valeur en la sourçant par page et par champ, ou exposer l'écart — ne pas le laisser flotter.

---

## Chiffres confirmés

**[CHAMP — correctement traité par la collecte] 12 344 220 personnes en ALD (2022, régime général)** — confirmé au tableau 3. Non comparable au 13,7 M : deux champs **et** deux millésimes. Écrire « de 13,7 à 12,3 millions » serait une erreur de fond, la lecture d'une évolution là où il y a deux périmètres.

**[OK] 122,8 Md€ de dépense totale, 111,7 Md€ remboursés, 67,3 % des dépenses remboursées** — retrouvés littéralement (p. 15) : « la dépense totale des assurés en ALD s'élève à 122,8 Md€, dont 91 % (111,7 Md€) de dépenses remboursées par l'assurance maladie. […] 67,3 % des dépenses remboursées par l'AMO concernent les assurés reconnus en ALD. » Le « 112 Md€ » de la synthèse est le même chiffre arrondi, pas une valeur distincte.

**[OK] 9 300 €/an de dépense moyenne, 840 € de reste à charge, couverture à 91 %** — confirmé littéralement (p. 13). Ratio recalculé : 840/9 300 = 9,03 %, soit une couverture de 90,97 %.

**[OK] CSBM 254,8 Md€, 8,7 % du PIB, 3 723 €/habitant (2024)** — confirmé (DREES, fiche 01, p. 22 et tableau 1).

**[OK] DCSi 332,6 Md€, 11,4 % du PIB** — confirmé (p. 8). CSBM/DCSi = 76,6 %, cohérent avec les « 77 % » que la source donne elle-même.

**[OK] Comparaison internationale** — 17,2 % (États-Unis), 12,3 % (Allemagne), 11,8 % (Autriche), 11,4 % (France), 10,3 % (UE-27), confirmés p. 18, avec les données manquantes 2024 pour la Bulgarie, la Croatie et la Roumanie.

**[OK] Reste à charge 7,8 % de la CSBM et 10,2 % de la DCSi** — confirmés p. 16. Le rapport porte lui-même l'avertissement de non-confusion des deux périmètres ; le conserver dans le numéro.

**[OK] Contrefactuel** — « près de 3,9 millions d'assurés reconnus pour une seule ALD présentent une dépense inférieure à la moyenne de celles des assurés sans ALD de plus de 65 ans » ; médiane de 187 € pour l'ALD 29 (tuberculose, lèpre) contre 34 902 € pour l'ALD 14 (mucoviscidose). Confirmés p. 20.

---

## L'avertissement de la CNAM sur la nature de la série

Retrouvé — non sur le *Points de repère* bloqué, mais sur la fiche « Personnes en affections de longue durée et dépense associée » d'`evaluation.securite-sociale.fr`, données 2022, sourcée CNAM :

> « Il convient d'être prudent dans l'interprétation des évolutions observées qui ne peuvent s'expliquer sous un angle purement épidémiologique. »
>
> « Le nombre d'admission en ALD liste est très sensible aux modifications des règles médico-administratives mais aussi à toutes actions ou programmes nouveaux […] visant à un dépistage plus précoce de certaines pathologies graves et/ou à l'élargissement de la population cible. »

À citer dans les précautions de lecture de l'entrée : c'est la meilleure garantie contre la lecture de la série ALD comme une prévalence épidémiologique alors qu'elle est un comptage administratif (règle 4).

---

## VERDICT GLOBAL : PUBLIABLE APRÈS CORRECTIONS

1. Trancher explicitement entre 13,7 M / 2021 (vérifié) et 13,8 M / 2022 (non vérifié, CNAM inaccessible). Ne pas publier 13,8 M tant que la publication primaire n'a pas été ouverte, malgré sa présence au gabarit du dispositif.
2. Ne pas publier 32/27/19/12 % ; utiliser 27,1/21,4/15,5/9,9 %.
3. Ne pas associer « +7 % » et « +14 % » à la base 13,7 M.
4. Corriger « un Français sur cinq ».
5. Sur l'âge moyen, choisir et sourcer, ou exposer l'écart.

Les autres chiffres sont publiables en l'état.
