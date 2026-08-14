# Collecte — n° 1, Finances publiques

État des données : août 2026. Accès réseau direct ouvert et exploité (contrairement à la première tentative d'août 2026, archivée dans `archive-non-sourcee-2026-08/`, qui reste inutilisable comme source). Producteurs effectivement consultés et **ouverts** : INSEE (fetch direct), Cour des comptes (PDF extrait via pypdf après téléchargement), Sénat — commission des finances (PDF extraits via pypdf), Assemblée nationale — projet annuel de performances PLF 2026 (PDF extrait via pypdf), Eurostat (PDF communiqué EDP extrait via pypdf, miroir ksh.hu), Haut Conseil des finances publiques (avis lu via Légifrance, résumé fourni par l'outil de fetch — voir réserve ci-dessous), direction générale du Trésor (Trésor-Éco n° 297).

**Réserve méthodologique générale** : plusieurs documents PDF ont été récupérés en binaire par l'outil de fetch web (échec de rendu HTML), puis leur texte a été extrait localement avec la bibliothèque `pypdf` et relu directement par moi. Pour ces documents (Cour des comptes, Sénat, PAP 2026, Eurostat), les extraits ci-dessous sont des citations littérales du texte ainsi extrait, que j'ai lu ligne à ligne — pas des résumés d'un outil tiers. Pour l'avis du Haut Conseil des finances publiques (Légifrance), le fetch a renvoyé un résumé avec guillemets ponctuels : je le signale explicitement au champ EXTRAIT quand la citation n'est pas garantie mot pour mot.

Répartition du budget de recherche tenue : dette (2 recherches), déficit (inclus avec dette, mêmes documents), charge d'intérêts + trajectoire 2030 (poste central, ~8 recherches/lectures), refinancement + coût d'un point de taux + maturité (5 recherches/lectures), comparaison européenne (4 recherches/lectures), dépenses publiques et PO (couvert par les mêmes documents que dette/déficit).

---

## 1. DETTE PUBLIQUE AU SENS DE MAASTRICHT

### Encours et ratio fin 2025 (donnée provisoire, première estimation)

CHIFFRE   : 3 460,5 Md€, soit 115,6 % du PIB
MILLÉSIME : 2025 (fin d'année), première estimation
CHAMP     : France entière, administrations publiques, dette au sens de Maastricht
SOURCE    : INSEE, *En 2025, le déficit public s'élève à 5,1 % du PIB, la dette publique à 115,6 % du PIB*, Informations rapides n° 78, mars 2026
URL       : https://www.insee.fr/fr/statistiques/8956575
EXTRAIT   : « La dette des administrations publiques au sens de Maastricht atteint 115,6 % du PIB fin 2025, après 112,6 % fin 2024. »
CONTEXTE  : Hausse de 3,0 points de PIB sur un an. Cette première estimation provisoire sera révisée lors de la publication des comptes nationaux annuels (29 mai 2026 annoncée par l'INSEE).
INCERTITUDE : donnée qualifiée de provisoire par l'INSEE elle-même ; à comparer avec la donnée « Comptes de la Nation » ci-dessous, légèrement différente (115,7 %).

### Encours détaillé (recoupement Eurostat, notification EDP avril 2026)

CHIFFRE   : 3 460 465 millions d'euros, soit 115,6 % du PIB
MILLÉSIME : 2025
CHAMP     : France entière, administrations publiques (« General government »), notification pour la procédure de déficit excessif
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf (miroir de la publication Eurostat ; texte extrait et lu directement)
EXTRAIT   : « France [...] Government debt (million euro) [...] 3 460 465 [...] (% of GDP) [...] 115.6 »
CONTEXTE  : Confirmation exacte, à l'unité près, du chiffre INSEE de mars 2026 — cohérence des deux publications sur le même millésime.
INCERTITUDE : —

### Série longue (Insee Première)

CHIFFRE   : 97,9 % (2019) ; 111,4 % (2022) ; 109,5 % (2023) ; 112,6 % (2024) ; 115,7 % (2025)
MILLÉSIME : 2019-2025
CHAMP     : France entière, dette publique brute au sens de Maastricht, en % du PIB
SOURCE    : INSEE, *Le compte des administrations publiques en 2025*, Insee Première n° 2106, mars 2026
URL       : https://www.insee.fr/fr/statistiques/8997691?sommaire=8071406
EXTRAIT   : non lu — donnée obtenue via l'outil de fetch qui a résumé le document (« La dette publique (brute) : 97,9 [2019], 111,4 [2022], 109,5 [2023], 112,6 [2024], 115,7 [2025] »), pas une citation garantie mot pour mot du document source ; le PDF lui-même n'a pas été ouvert directement par moi
CONTEXTE  : Le chiffre 2025 (115,7 %) diverge légèrement du chiffre de l'Informations rapides n° 78 (115,6 %) — écart d'un dixième de point entre deux publications INSEE du même mois, à signaler comme telle une divergence mineure entre deux estimations provisoires du même millésime, pas comme une erreur.
INCERTITUDE : chiffre à revérifier en ouverture directe du PDF Insee Première 2106.

### Ratio Q3 2025 (donnée trimestrielle antérieure, pour mémoire de la dynamique infra-annuelle)

CHIFFRE   : 117,7 % du PIB (Eurostat) — à comparer à 117,4 % (INSEE, Informations rapides n° 322)
MILLÉSIME : T3 2025
CHAMP     : France entière, dette au sens de Maastricht, fin de trimestre
SOURCE    : Eurostat, *La dette publique à 88,5 % du PIB dans la zone euro*, Euro indicateurs, 22 janvier 2026 ; et INSEE, Informations rapides n° 322
URL       : https://ec.europa.eu/eurostat/fr/web/products-euro-indicators/w/2-22012026-ap
EXTRAIT   : « À la fin du troisième trimestre 2025, le ratio de la dette brute des administrations publiques par rapport au PIB dans la zone euro (ZE20) s'est établi à 88,5 %, en hausse par rapport au ratio de 88,2 % enregistré à la fin du deuxième trimestre 2025. »
CONTEXTE  : Ratio trimestriel non directement comparable au ratio annuel définitif (base de calcul différente sur le PIB glissant) ; le point notable est que le chiffre trimestriel Eurostat de la France (117,7 %) et le chiffre INSEE (117,4 %) pour le même trimestre divergent de 0,3 point — illustration de l'écart entre sources y compris sur un même champ.
INCERTITUDE : citation portant sur la zone euro lue directement ; le chiffre France par pays (117,7 %) provient du même document mais n'a pas été confirmé par citation littérale isolée — à vérifier.

---

## 2. DÉFICIT PUBLIC

### 2025 — première estimation (réalisé provisoire)

CHIFFRE   : 152,5 Md€, soit 5,1 % du PIB
MILLÉSIME : 2025
CHAMP     : France entière, administrations publiques, déficit au sens de Maastricht
SOURCE    : INSEE, *En 2025, le déficit public s'élève à 5,1 % du PIB, la dette publique à 115,6 % du PIB*, Informations rapides n° 78, mars 2026
URL       : https://www.insee.fr/fr/statistiques/8956575
EXTRAIT   : « Le déficit public pour 2025 s'établit à 152,5 Md€, soit 5,1 % du produit intérieur brut (PIB), après 5,8 % en 2024 et 5,4 % en 2023. »
CONTEXTE  : Amélioration de 0,7 point par rapport à 2024. Confirmé par Eurostat (notification EDP avril 2026) au chiffre exact de 152 511 millions d'euros.
INCERTITUDE : —

### Recoupement Eurostat

CHIFFRE   : −152 511 millions d'euros, soit −5,1 % du PIB
MILLÉSIME : 2025
CHAMP     : France entière, administrations publiques
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf
EXTRAIT   : « France [...] Government deficit (-) / surplus(+) (million euro) [...] -152 511 [...] (% of GDP) [...] -5.1 »
CONTEXTE  : Coïncide au million près avec le chiffre INSEE.
INCERTITUDE : —

### Prévision précédente de la Cour des comptes (février 2026) — pour illustrer l'écart prévu/réalisé

CHIFFRE   : 161,0 Md€, soit 5,4 points de PIB (estimation à ce stade, non les comptes définitifs)
MILLÉSIME : 2025, estimation publiée en février 2026, donc AVANT le chiffre INSEE définitif de mars 2026 (152,5 Md€ / 5,1 %)
CHAMP     : France entière, administrations publiques
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026 (PDF récupéré via miroir vie-publique.fr, texte extrait et lu par pypdf)
EXTRAIT   : « Le déficit public devrait atteindre 161,0 Md€ en 2025, soit l'équivalent de 5,4 points de PIB, après 5,8 points en 2024. »
CONTEXTE  : **Piège classique prévu/réalisé** : la Cour des comptes anticipait en février 2026 un déficit de 5,4 points de PIB pour 2025 ; le chiffre INSEE publié un mois plus tard (mars 2026) est finalement de 5,1 points — soit 8,5 Md€ de moins que l'estimation de la Cour. Ce n'est pas une erreur de la Cour : à la date de son rapport, « les comptes des administrations locales et sociales n'étaient pas encore arrêtés » (citation ci-dessous).
INCERTITUDE : —

CHIFFRE   : « la marge usuelle d'incertitude prévaut encore à ce stade, les comptes des administrations locales et sociales n'étant pas encore arrêtés »
MILLÉSIME : février 2026
CHAMP     : Cour des comptes sur son propre chiffre 2025
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « la cible d'un déficit ramené à 5,4 points de PIB, qui n'a pas été révisée à l'automne dernier, devrait être atteinte, même si la marge usuelle d'incertitude prévaut encore à ce stade, les comptes des administrations locales et sociales n'étant pas encore arrêtés. »
CONTEXTE  : Justification méthodologique de l'écart constaté avec le chiffre définitif.
INCERTITUDE : —

### 2026 — cible officielle (prévu)

CHIFFRE   : 5,0 points de PIB
MILLÉSIME : 2026 (prévu, texte sur lequel le Gouvernement a engagé sa responsabilité, janvier 2026)
CHAMP     : France entière, administrations publiques
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « le texte sur le vote duquel le Gouvernement a engagé sa responsabilité en janvier 2026 vise un déficit de 5,0 points de PIB, avec une répartition de l'effort plus homogène par rapport à 2025 entre dépenses et recettes. »
CONTEXTE  : Cible relevée de 4,7 à 5,0 points de PIB après le vote de la LFSS 2026 (16 décembre 2025) qui a acté un recul de 0,3 point. Le texte n'est pas passé par un vote ordinaire de l'Assemblée mais par l'article 49.3 (engagement de responsabilité du Gouvernement).
INCERTITUDE : —

### Dette publique fin 2026 — projection

CHIFFRE   : 118,6 points de PIB (Cour des comptes, février 2026) ; 118,4 % (HCFP, avril 2026)
MILLÉSIME : 2026 (prévu)
CHAMP     : France entière, administrations publiques
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026 ; Haut Conseil des finances publiques, avis n° HCFP-2026-3 du 17 avril 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026 ; https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053931090
EXTRAIT   : « le ratio de dette publique continuerait d'augmenter, de plus de deux points, pour atteindre 118,6 points de PIB fin 2026. » (Cour des comptes, cité mot pour mot)
            Pour le HCFP : EXTRAIT non lu au sens strict — le fetch de Légifrance a renvoyé un résumé avec citations ponctuelles (« la France reste ainsi l'un des pays de la zone euro cumulant ratio de dette élevé et solde public dégradé »), non vérifié mot pour mot par moi sur le document intégral.
CONTEXTE  : Deux projections voisines (118,6 vs 118,4) publiées à deux mois d'écart, sur la même trajectoire.
INCERTITUDE : chiffre HCFP à revérifier par lecture directe de l'avis intégral, non accessible en PDF lisible via l'outil de fetch dans cette session.

### Cible 2029 — retour sous 3 % (engagement européen)

CHIFFRE   : retour du déficit sous 3 points de PIB en 2029, nécessitant un rythme de réduction moyen de 0,7 point de PIB par an
MILLÉSIME : trajectoire 2027-2029
CHAMP     : France entière, engagement dans le cadre de la procédure pour déficit excessif (PDE) ouverte le 26 juillet 2024
SOURCE    : Haut Conseil des finances publiques, avis n° HCFP-2026-3 du 17 avril 2026, relatif au rapport d'avancement annuel 2026 du plan budgétaire et structurel à moyen terme 2025-2029
URL       : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053931090
EXTRAIT   : non lu — résumé fourni par l'outil de fetch avec guillemets ponctuels (« faire revenir le déficit sous 3 points de PIB en 2029 », « un rythme de réduction moyen du déficit de 0,7 point de PIB par an »), non vérifié mot pour mot par lecture intégrale du document par moi
CONTEXTE  : Cohérent avec la Cour des comptes (février 2026) qui évoque un effort de réduction de 0,6 point par an « à partir de 2027 » pour un retour, non pas en 2029, mais « en 2035, au niveau atteint en 2025 » si l'effort ne dépasse pas ce rythme — deux horizons distincts (cible réglementaire 2029 vs trajectoire réaliste selon la Cour, 2035 pour un simple retour au niveau de dette de 2025).
INCERTITUDE : à revérifier par lecture directe de l'avis HCFP intégral.

CHIFFRE   : effort budgétaire restant estimé à environ 80 Md€
MILLÉSIME : estimation février 2026, pour ramener le déficit sous 3 % du PIB
CHAMP     : France entière, administrations publiques
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « La France a reporté depuis de nombreuses années les efforts budgétaires, désormais de l'ordre de 80 Md€, nécessaires au retour durable du déficit sous 3 % du PIB, condition indispensable pour assurer la soutenabilité de la dette publique. »
CONTEXTE  : —
INCERTITUDE : —

---

## 3. CHARGE D'INTÉRÊTS — LE CHIFFRE CENTRAL

**Avertissement de champ, décisif sur ce thème** : au moins trois périmètres distincts circulent sous le nom « charge d'intérêts » ou « charge de la dette », avec des valeurs 2026 différentes (58,0 / 60,4 / 73,6 Md€). Ce ne sont pas des estimations concurrentes du même objet mais des objets statistiques différents :
1. **Programme 117** (« Charge de la dette et trésorerie de l'État », comptabilité budgétaire, hors trésorerie) : 58,0 Md€ en 2026.
2. **Mission « Engagements financiers de l'État »** (comptabilité budgétaire, inclut le programme 117 et d'autres programmes annexes comme la charge de la dette SNCF Réseau reprise) : 60,2-60,4 Md€ en 2026.
3. **Charge d'intérêts toutes administrations publiques** (comptabilité nationale, Maastricht, Cour des comptes/INSEE) : 73,6 Md€ en 2026 — c'est ce périmètre que la Cour des comptes compare aux missions budgétaires « Défense » et « Enseignement scolaire ».

### Charge d'intérêts toutes APU — série 2024-2026 (comptabilité nationale)

CHIFFRE   : 60,2 Md€ (2024) ; 64,9 Md€ (2025) ; 73,6 Md€ (2026, prévu)
MILLÉSIME : 2024 (réalisé), 2025 (première estimation), 2026 (prévu, PLF)
CHAMP     : France entière, ensemble des administrations publiques, dépenses de charge d'intérêt en comptabilité nationale
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026, tableau n° 14 « dépense publique de 2024 à 2026, en Md€ (hors crédits d'impôt) »
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « Dépenses de charge d'intérêts 60,2 64,9 73,6 » (ligne du tableau n° 14, colonnes 2024 / 2025 / 2026 (P)) ; ratio associé : « Ratio en points de PIB 2,1 2,2 2,4 »
CONTEXTE  : Sur l'ensemble des administrations publiques, hausse de +22 % entre 2024 et 2026 (deux ans). Les charges d'intérêt représentent 2,1 % du PIB en 2024, 2,2 % en 2025, 2,4 % en 2026 (prévu).
INCERTITUDE : —

### Comparaison directe aux budgets Défense et Enseignement scolaire (2025)

CHIFFRE   : 64,9 Md€ (intérêts, toutes APU, 2025) > 63 Md€ (enseignement scolaire, crédits de paiement PLF, hors CAS Pensions, 2025) > 50 Md€ (défense, crédits de paiement, hors CAS Pensions, 2025)
MILLÉSIME : 2025
CHAMP     : Comparaison entre un agrégat toutes APU (intérêts) et des crédits de paiement budgétaires de l'État hors pensions (défense, enseignement scolaire) — champs non strictement homogènes, la Cour des comptes le fait elle-même et le signale en note
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « Sur l'ensemble des administrations publiques, la charge d'intérêts atteindrait 64,9 Md€ en 2025, soit un niveau de dépenses plus élevé que pour l'enseignement scolaire (63 Md€) ou pour la défense (50 Md€). Avec le refinancement progressif du stock de dette publique à des taux de marché plus élevés, elle devrait dépasser 100 Md€ par an à l'horizon 2029. »
            Note de bas de page de la Cour : « Crédits de paiement prévus en PLF pour 2025, hors contribution au compte d'affectation spéciale (CAS) Pensions » (enseignement scolaire) ; « Montant indiqué hors contribution au CAS Pensions » (défense).
CONTEXTE  : Répété ailleurs dans le même rapport, formulation synthèse : « à près de 65 Md€ en 2025, la charge de la dette publique excède déjà le budget de l'enseignement scolaire ou celui de la défense, et continue à croître inexorablement. »
INCERTITUDE : —

### Budgets Défense et Enseignement scolaire 2026 (mise à jour pour comparaison avec le chiffre 2026 de la charge d'intérêts)

CHIFFRE   : Défense — 57,15 Md€ (crédits de paiement, périmètre LPM hors pensions) ; 66,7 Md€ (CP totaux, y compris pensions) ; 93,1 Md€ (autorisations d'engagement)
MILLÉSIME : 2026 (prévu, PLF)
CHAMP     : Mission Défense du budget de l'État
SOURCE    : Sénat, commission des finances, rapport sur le projet de loi de finances pour 2026 — mission Défense
URL       : https://www.senat.fr/rap/l25-139-38/l25-139-38-syn.pdf
EXTRAIT   : « Les autorisations d'engagement (AE) prévues pour la mission « Défense » s'élèveraient en 2026 à 93,1 milliards d'euros, soit une baisse de 0,5 % par rapport à 2025. Les crédits de paiement (CP) s'établiraient à 66,7 milliards d'euros, soit une hausse de 6,78 milliards d'euros (+ 11,3 %). [...] Sur le périmètre de la LPM (hors pensions), les crédits demandés s'établissent à 57,15 milliards d'euros, en hausse de 6,67 milliards d'euros par rapport à la LFI 2025. »
CONTEXTE  : « La politique de défense constitue, en 2026, la deuxième politique publique de l'État en termes d'effort budgétaire en CP, après l'enseignement scolaire, et la première en AE. »
INCERTITUDE : —

CHIFFRE   : Enseignement scolaire — 64,49 Md€ en CP hors CAS « Pensions » ; 89,64 Md€ en CP y compris CAS « Pensions »
MILLÉSIME : 2026 (prévu, PLF)
CHAMP     : Mission Enseignement scolaire du budget de l'État
SOURCE    : Sénat, commission des finances, *L'essentiel sur… le projet de loi de finances pour 2026, mission « Enseignement scolaire »*, Olivier Paccaud, rapporteur spécial
URL       : https://www.senat.fr/fileadmin/cru-1769414716/Commissions/Finances/2025-2026/PLF_2026/Essentiel/Enseignement_scolaire_Essentiel_post-commission_PLF_2026.pdf
EXTRAIT   : « Les crédits de la mission « Enseignement scolaire » s'élèvent en PLF 2026 à 64,49 milliards d'euros en crédits de paiement (CP) et 64,46 milliards d'euros en autorisations d'engagement (AE) hors contribution au CAS « Pensions », soit une progression de 0,26 % par rapport à 2025 et de 18,8 % (+ 12,13 milliards d'euros) par rapport à 2019. En y incluant la contribution au CAS « Pensions », la mission atteint 89,62 milliards d'euros en AE et 89,64 milliards d'euros en CP. »
CONTEXTE  : « Les crédits de la mission « Enseignement scolaire » ne sont plus le 1er poste de dépenses du budget général de l'État en AE, hors remboursements et dégrèvements, mais sont désormais dépassés par la mission « Défense ». »
INCERTITUDE : —

**Note de non-comparabilité directe** : la charge d'intérêts 2026 de 73,6 Md€ (toutes APU, comptabilité nationale) n'est pas directement comparable aux budgets 2026 de la Défense (57,15 Md€, CP hors pensions, comptabilité budgétaire de l'État) et de l'Enseignement scolaire (64,49 Md€, CP hors pensions, même champ) sans le signaler : la Cour des comptes fait elle-même cette comparaison inter-champs (toutes APU vs crédits budgétaires État hors pensions), avec le millésime 2025 explicitement, en la justifiant en note de bas de page — elle n'a pas republié la comparaison en 2026 dans les extraits consultés ici. Sur la base des chiffres 2026 rassemblés séparément (73,6 Md€ vs 57,15 Md€ vs 64,49 Md€), la charge d'intérêts toutes APU dépasse les deux, mais l'écart de champ doit être conservé dans la présentation.

### Charge de la dette de l'État seul (comptabilité budgétaire, programme 117)

CHIFFRE   : 58,0 Md€
MILLÉSIME : 2026 (prévu)
CHAMP     : France entière, budget de l'État, programme 117 « Charge de la dette et trésorerie de l'État », hors trésorerie
SOURCE    : Assemblée nationale, *Projet annuel de performances — Engagements financiers de l'État*, annexe au projet de loi de finances pour 2026
URL       : https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087975/file/PAP2026_BG_Engagements_financiers_Etat_EB.pdf
EXTRAIT   : « En 2026, la charge budgétaire de la dette (hors trésorerie) du programme 117 atteindrait, sous les hypothèses de financement, de taux et d'inflation présentées précédemment, 58,0 Md€, soit 7,2 Md€ de plus que la charge aujourd'hui prévue pour 2025. »
CONTEXTE  : Décomposition de la hausse 2025→2026 (+7,2 Md€) donnée par le document : « un effet volume de +4,1 Md€ [...] ; un effet taux de +2,8 Md€, principalement en lien avec la hausse des taux de long terme (+2,6 Md€) ; un effet inflation de +0,6 Md€ [...] ; la variation de la charge due aux effets calendaires [...] de -0,4 Md€. »
INCERTITUDE : —

CHIFFRE   : Mission « Engagements financiers de l'État » — 60,4 Md€ en CP, 60,2 Md€ en AE
MILLÉSIME : 2026 (prévu)
CHAMP     : Budget de l'État, mission complète (programme 117 + autres programmes annexes)
SOURCE    : Sénat, commission des finances, rapport sur le projet de loi de finances pour 2026, mission « Engagements financiers de l'État »
URL       : https://www.senat.fr/rap/l25-139-312/l25-139-312_mono.html
EXTRAIT   : « le deuxième poste de dépenses du budget de l'État en crédits de paiement après la mission Enseignement scolaire » ; « le troisième poste en autorisations d'engagement après les missions Défense et Enseignement scolaire » ; crédits de paiement de la mission chiffrés à « 60,4 milliards d'euros » et en autorisations d'engagement à « 60,2 milliards d'euros »
CONTEXTE  : Classement par mission en crédits de paiement 2026 : 1) Enseignement scolaire, 2) Engagements financiers de l'État. En autorisations d'engagement : 1) Défense, 2) Enseignement scolaire, 3) Engagements financiers de l'État.
INCERTITUDE : —

---

## 4. TRAJECTOIRE PROJETÉE DE LA CHARGE D'INTÉRÊTS D'ICI 2030

CHIFFRE   : plus de 100 Md€ par an à l'horizon 2029 (toutes APU)
MILLÉSIME : projection 2029
CHAMP     : France entière, toutes administrations publiques, comptabilité nationale
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « Avec le refinancement progressif du stock de dette publique à des taux de marché plus élevés, elle devrait dépasser 100 Md€ par an à l'horizon 2029. » ; ailleurs dans le même rapport : « les charges d'intérêt, non révisées depuis la version initiale du PLF, atteindraient 73,6 Md€ soit le double de leur niveau de 2019. »
CONTEXTE  : Doublement en sept ans (2019-2026) selon ce même rapport.
INCERTITUDE : —

CHIFFRE   : charge de la dette de l'État pourrait dépasser 70 Md€ en 2027, plus de 90 Md€ en 2029, et la barre des 100 Md€ pourrait être atteinte autour de 2030
MILLÉSIME : projections 2027, 2029, 2030
CHAMP     : France entière — le champ exact (État seul en comptabilité générale, ou toutes APU) n'est pas homogène entre les occurrences de ce rapport ; à vérifier par le fact-checker sur le document intégral
SOURCE    : Sénat, commission des finances, rapport sur le projet de loi de finances pour 2026, engagements financiers de l'État
URL       : https://www.senat.fr/rap/l25-139-312/l25-139-312_mono.html
EXTRAIT   : « la charge de la dette de l'État pourrait dépasser 70 milliards d'euros en 2027 » ; « représenter plus de 90 milliards d'euros en 2029 » ; « la barre des 100 milliards d'euros pourrait être atteinte autour de 2030 » — ces trois citations proviennent d'un résumé produit par l'outil de fetch avec guillemets marqués comme littéraux ; je ne les ai pas revérifiées moi-même sur le document HTML intégral, donc prudence sur leur exactitude mot pour mot
CONTEXTE  : Cohérent en ordre de grandeur avec la trajectoire toutes-APU de la Cour des comptes (>100 Md€ en 2029) mais les niveaux (70/90/100) sont légèrement inférieurs à un rythme d'atteinte de 100 Md€ un an plus tard (2030 vs 2029) — pourrait s'expliquer par un champ plus étroit (État seul plutôt que toutes APU).
INCERTITUDE : citations à revérifier par lecture directe du document HTML du Sénat, non garanties mot pour mot par moi.

CHIFFRE   : la charge d'intérêts augmenterait de près de 12 Md€ en 2026, s'élevant à plus de 78 Md€
MILLÉSIME : 2026 (prévu, réestimé en avril 2026, postérieur au chiffre de 73,6 Md€ de la Cour des comptes de février 2026)
CHAMP     : non précisé avec certitude dans le résumé obtenu — vraisemblablement toutes APU compte tenu du niveau proche de celui de la Cour des comptes
SOURCE    : Haut Conseil des finances publiques, avis n° HCFP-2026-3 du 17 avril 2026
URL       : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053931090
EXTRAIT   : non lu — résumé de l'outil de fetch avec guillemet partiel (« augmenterait de près de 12 Md€ en 2026, s'élevant à plus de 78 Md€ »), non vérifié mot pour mot par moi sur le document intégral ; le résumé attribue une partie de la hausse (+3,6 Md€) au « conflit moyen-oriental », référence non vérifiée non plus
CONTEXTE  : Si confirmé, ce chiffre (>78 Md€) serait supérieur de plus de 4 Md€ à la prévision de la Cour des comptes de février 2026 (73,6 Md€) pour le même millésime 2026 — à vérifier en priorité par le fact-checker : soit une révision à la hausse en deux mois, soit un champ différent.
INCERTITUDE : élevée — nécessite lecture directe du texte intégral de l'avis HCFP-2026-3, non obtenue dans cette session (échec de rendu du fetch sur Légifrance, résumé uniquement).

---

## 5. VOLUME D'ÉMISSIONS À REFINANCER SUR L'ANNÉE

CHIFFRE   : 310,0 Md€ d'émissions de dette à moyen/long terme, pour un besoin de financement 2026 de 305,7 Md€ dont 175,8 Md€ d'amortissements de titres à moyen/long terme et 124,4 Md€ de déficit à financer
MILLÉSIME : 2026 (programme prévisionnel)
CHAMP     : France entière, État, dette négociable à moyen et long terme
SOURCE    : Assemblée nationale, *Projet annuel de performances — Engagements financiers de l'État*, annexe au projet de loi de finances pour 2026
URL       : https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087975/file/PAP2026_BG_Engagements_financiers_Etat_EB.pdf
EXTRAIT   : « Pour 2026. Le besoin de financement est principalement constitué d'un déficit à financer de 124,4 Md€ et d'amortissements de titres à moyen/long terme qui devraient atteindre 175,8 Md€ (173,4 Md€ hors supplément d'indexation, versé aux détenteurs de l'OAT€i qui sera remboursée en 2026). Ce besoin de financement sera principalement couvert par un volume d'émissions de dette à moyen/long terme de 310,0 Md€. »
CONTEXTE  : Tableau associé (montants en Md€) : besoin de financement 2024 exécution = 305,7 ; 2025 LFI = 303,5 ; 2025 révisé = 297,7 ; 2026 PLF = 305,7. Amortissement de titres d'État à moyen et long terme (valeur nominale) : 151,1 (2024) ; 166,1 (2025 LFI) ; 166,1 (2025 révisé) ; 173,4 (2026).
INCERTITUDE : —

CHIFFRE   : 310,0 Md€ (confirmation, communiqué de l'Agence France Trésor)
MILLÉSIME : 2026
CHAMP     : Émissions nettes de titres à moyen et long terme
SOURCE    : Agence France Trésor, *Indicative State financing programme 2026*, communiqué du 30 décembre 2025
URL       : https://www.aft.gouv.fr/en/publications/communiques-presse/30122025-indicative-state-financing-programme-2026
EXTRAIT   : non lu — page bloquée (HTTP 403) à chaque tentative d'accès direct dans cette session (domaine aft.gouv.fr systématiquement inaccessible, y compris en PDF, y compris via curl direct). Le chiffre 310,0 Md€ est confirmé indépendamment par le document budgétaire primaire de l'Assemblée nationale ci-dessus, qui cite lui-même ce montant comme émanant du programme de financement — je considère donc le chiffre robuste malgré l'échec d'accès à la source AFT elle-même.
CONTEXTE  : —
INCERTITUDE : source AFT elle-même non ouverte ; voir PISTES NON ABOUTIES.

### Encours de la dette négociable (série AN/PAP)

CHIFFRE   : 2 601,6 Md€ en valeur actualisée fin 2024 (2 541,6 Md€ en valeur nominale), en hausse de 171,6 Md€ sur l'année 2024, après +152,2 Md€ en 2023
MILLÉSIME : fin 2024
CHAMP     : France entière, dette négociable de l'État (OAT + BTF), hors dette non négociable
SOURCE    : Assemblée nationale, *Projet annuel de performances — Engagements financiers de l'État*, annexe au PLF 2026
URL       : https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087975/file/PAP2026_BG_Engagements_financiers_Etat_EB.pdf
EXTRAIT   : « L'encours de la dette négociable de l'État a progressé de +171,6 Md€ en valeur actualisée en 2024, après +152,2 Md€ en 2023. » Tableau : OAT 1 961,8 (2021) / 2 081,1 (2022) / 2 206,6 (2023) / 2 340,5 (2024) ; BTF 155,4 / 148,5 / 169,2 / 201,2 ; « Ensemble de la dette – valeur nominale » 2 117,2 / 2 229,5 / 2 375,8 / 2 541,6.
CONTEXTE  : Cette dette négociable (2 541,6 Md€ fin 2024) est un sous-ensemble de la dette Maastricht toutes APU (3 306 Md€ fin 2024 selon Eurostat) — elle ne couvre que l'État, pas les collectivités locales ni la sécurité sociale.
INCERTITUDE : —

---

## 6. COÛT D'UN POINT DE TAUX SUPPLÉMENTAIRE ; MATURITÉ MOYENNE

**Trois estimations primaires du coût d'une hausse de taux, à des horizons et sur des scénarios différents — elles ne se recoupent pas terme à terme et ne doivent pas être fusionnées.**

### Estimation Cour des comptes (choc permanent de +1 point sur les OAT 10 ans)

CHIFFRE   : +9 Md€ au bout de trois ans, +16 Md€ au bout de cinq ans, +30 Md€ au bout de dix ans
MILLÉSIME : scénario à partir de 2026
CHAMP     : non précisé explicitement (probablement toutes APU, dans la continuité du chapitre) ; France entière
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « une hausse permanente d'un point du taux d'intérêt sur les obligations d'État à 10 ans se traduirait par un surcroît de charge d'intérêts de 9 Md€ au bout de trois ans, de 16 Md€ au bout de cinq ans et de 30 Md€ au bout de 10 ans »
CONTEXTE  : —
INCERTITUDE : —

### Estimation Sénat (choc sur l'ensemble de la courbe)

CHIFFRE   : +3,2 Md€ à 1 an, +23,5 Md€ à 5 ans, +33,5 Md€ à 9 ans
MILLÉSIME : scénario de choc de taux, sans date de départ précisée dans l'extrait obtenu
CHAMP     : titres négociables de l'État
SOURCE    : Sénat, commission des finances, rapport sur le projet de loi de finances pour 2026, engagements financiers de l'État
URL       : https://www.senat.fr/rap/l25-139-312/l25-139-312_mono.html
EXTRAIT   : non lu au sens strict — chiffres obtenus via un résumé de l'outil de fetch mentionnant « Choc de +1 point sur l'ensemble de la courbe : À 1 an : +3,2 milliards d'euros ; À 5 ans : +23,5 milliards d'euros ; À 9 ans : +33,5 milliards d'euros », non revérifiés mot pour mot sur le document HTML intégral
CONTEXTE  : Diverge sensiblement de l'estimation Cour des comptes ci-dessus, à la fois en niveau (23,5 Md€ à 5 ans contre 16 Md€) et en méthode.
INCERTITUDE : élevée sur l'exactitude littérale ; à confirmer par lecture directe.

### Estimation PAP 2026 (choc de +100 points de base au 1ᵉʳ janvier 2026, comptabilité maastrichtienne)

CHIFFRE   : +3,1 Md€ la première année, environ +18 Md€ la cinquième année
MILLÉSIME : scénario à partir du 1ᵉʳ janvier 2026
CHAMP     : dette négociable de l'État, évaluation en comptabilité maastrichtienne (équivalente à la comptabilité générale de l'État)
SOURCE    : Assemblée nationale, *Projet annuel de performances — Engagements financiers de l'État*, annexe au PLF 2026
URL       : https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087975/file/PAP2026_BG_Engagements_financiers_Etat_EB.pdf
EXTRAIT   : « L'effet d'un choc de +1 % (+100 points de base) par rapport au scénario de référence, qui interviendrait le 1er janvier 2026, sur l'ensemble de la courbe et sur toute la durée de la projection, est présenté ci-dessous. Le surcroît de dépense, par rapport à la prévision de base, serait de 3,1 Md€ la première année, d'environ 18 Md€ la cinquième année. » Précision méthodologique du même document : « Cette évaluation est établie en comptabilité maastrichtienne, équivalente à la comptabilité générale de l'État. Elle tient compte de l'ensemble des flux de paiements associés aux émissions de dette, en répartissant uniformément la dépense d'intérêt sur la durée de vie d'un titre. »
CONTEXTE  : Le même document précise également la sensibilité à l'inflation : « une variation des indices de prix à la consommation de +/-0,1 % induit une variation de la charge d'environ +/-0,3 Md€. »
INCERTITUDE : —

### Choc de taux déjà observé (55 points de base sur deux ans) et son effet chiffré

CHIFFRE   : hausse de 55 points de base des taux à 10 ans sur les deux dernières années, qui se traduirait, si elle perdurait, par un surcroît de charge d'intérêts de plus de 1,6 Md€ en 2026, de 4 Md€ en 2027 et de 8 Md€ en 2029
MILLÉSIME : observation sur deux ans jusqu'à février 2026 ; projection sur les effets jusqu'en 2029
CHAMP     : France entière
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « La hausse de 55 points de base des taux à 10 ans enregistrée depuis deux ans [...] devrait se traduire, si elle devait perdurer, par un surcroît de charge d'intérêts de plus de 1,6 Md€ en 2026, de 4 Md€ en 2027 et de 8 Md€ en 2029 »
CONTEXTE  : « les taux français se situent en effet autour de 3,45 % début 2026, contre 2,90 % deux ans plus tôt. » Comparaison européenne : « Parmi les six pays les plus endettés de la zone euro, la France est donc passée, au cours des deux dernières années, du taux d'intérêt le plus faible au taux le plus élevé avec l'Italie et la Grèce, lesquelles affichent pourtant un ratio d'endettement public encore nettement supérieur à celui de la France. »
INCERTITUDE : —

### Maturité moyenne de la dette

CHIFFRE   : 8 ans (citation Cour des comptes, février 2026) ; 8,2 ans fin 2020 (Trésor-Éco, source plus ancienne mais primaire et datée précisément)
MILLÉSIME : « fin 2020 » pour le chiffre Trésor-Éco (millésime précis) ; non daté précisément pour la citation de la Cour des comptes (rapport de février 2026, donc vraisemblablement proche de cette date)
CHAMP     : durée de vie moyenne des titres de dette publique française (Cour des comptes) / maturité moyenne de la dette de l'État (Trésor-Éco)
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026 (note de bas de page 79) ; direction générale du Trésor, *La stratégie d'émission de la dette souveraine française*, Trésor-Éco n° 297, janvier 2022
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026 ; https://www.tresor.economie.gouv.fr/Articles/aed3274b-b5a2-482d-a02d-09d0b9f339d6/files/dc0bde49-9fd8-4e29-bd30-fe069abb603b
EXTRAIT   : « La maturité moyenne des titres de dette publique français est de huit ans. » (Cour des comptes, note 79) ; « En France, la maturité moyenne de la dette de l'État s'élevait fin 2020 à 8,2 ans » (Trésor-Éco n° 297)
CONTEXTE  : Le chiffre de « 8,5 ans » couramment cité dans la presse pour avril 2026 (sur la base de bulletins mensuels AFT) n'a pas pu être vérifié en source primaire dans cette session — le domaine aft.gouv.fr a systématiquement renvoyé une erreur HTTP 403, y compris pour ses PDF de bulletins mensuels.
INCERTITUDE : le chiffre « 8,5 ans » pour 2026 circule largement dans la presse financière (relayé notamment par l'archive non sourcée du n° 1) mais n'a pu être vérifié en source primaire AFT — à traiter comme non confirmé tant que la source AFT n'est pas rouverte.

### Structure de détention (donnée ancienne, à revalider)

CHIFFRE   : au 2ᵉ trimestre 2021, 18 % de banques centrales ou fonds souverains non-résidents, 5 % de banques non-résidentes, 24 % d'investisseurs non-bancaires non-résidents, 17 % de la Banque de France, 15 % de banques résidentes, 22 % d'investisseurs non bancaires résidents — soit environ 50 % de détention par des résidents contre moins de 38 % fin 2014
MILLÉSIME : T2 2021 (et point de comparaison fin 2014)
CHAMP     : dette publique de l'État français, structure de détention par catégorie d'investisseurs
SOURCE    : direction générale du Trésor, *La stratégie d'émission de la dette souveraine française*, Trésor-Éco n° 297, janvier 2022
URL       : https://www.tresor.economie.gouv.fr/Articles/aed3274b-b5a2-482d-a02d-09d0b9f339d6/files/dc0bde49-9fd8-4e29-bd30-fe069abb603b
EXTRAIT   : « au deuxième trimestre 2021, 18 % de banques centrales ou fonds souverains non-résidents, 5 % de banques non-résidentes, 24 % d'investisseurs non-bancaires non-résidents, 17 % de la Banque de France, 15 % de banques résidentes et 22 % d'investisseurs non bancaires résidents. [...] la croissance de la détention de la Banque de France [...] a fait croître la part des résidents dans la détention de la dette de l'État (à environ 50 % de la dette au deuxième trimestre 2021 contre moins de 38 % fin 2014). »
CONTEXTE  : Donnée datée de 2021, antérieure à la fin des rachats nets d'actifs de la BCE — à ne pas présenter comme une photographie 2025-2026 sans mise à jour. Le chiffre « 56 % non-résidents / 44 % résidents fin 2025-2026 » cité dans l'archive non sourcée n'a pas été retrouvé en source primaire dans cette session.
INCERTITUDE : donnée non actualisée ; nécessite une nouvelle recherche auprès de la Banque de France ou de l'AFT (bloquée dans cette session) pour un point récent.

---

## 7. DÉPENSES PUBLIQUES ET PRÉLÈVEMENTS OBLIGATOIRES EN % DU PIB, COMPARAISON EUROPÉENNE

### France — dépenses publiques

CHIFFRE   : 57,2 % du PIB (2025), après 57,0 % (2024)
MILLÉSIME : 2025 (première estimation)
CHAMP     : France entière, toutes administrations publiques
SOURCE    : INSEE, *En 2025, le déficit public s'élève à 5,1 % du PIB, la dette publique à 115,6 % du PIB*, Informations rapides n° 78, mars 2026
URL       : https://www.insee.fr/fr/statistiques/8956575
EXTRAIT   : « Rapportées au PIB, les dépenses augmentent et s'établissent à 57,2 %, après 57,0 % en 2024 »
CONTEXTE  : Confirmé par Eurostat au chiffre identique (57,2 %, voir ci-dessous).
INCERTITUDE : —

CHIFFRE   : 57,2 % du PIB (2025)
MILLÉSIME : 2025
CHAMP     : France entière, administrations publiques, « Government expenditure »
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf
EXTRAIT   : « France [...] Government expenditure (% of GDP) [...] 57.2 »
CONTEXTE  : À comparer à la moyenne de la zone euro : « In 2025, government total expenditure to GDP ratio in the euro area stood at 49.8 % of GDP » — soit 7,4 points d'écart entre la France et la moyenne de la zone euro.
INCERTITUDE : —

### France — prélèvements obligatoires

CHIFFRE   : 43,6 % du PIB (2025), après 42,8 % en 2024
MILLÉSIME : 2025
CHAMP     : France entière, ensemble des prélèvements obligatoires (impôts + cotisations sociales), comptabilité nationale INSEE
SOURCE    : INSEE, *En 2025, le déficit public s'élève à 5,1 % du PIB, la dette publique à 115,6 % du PIB*, Informations rapides n° 78, mars 2026
URL       : https://www.insee.fr/fr/statistiques/8956575
EXTRAIT   : « Le taux de prélèvements obligatoires augmente et s'établit à 43,6 % du PIB, après 42,8 % en 2024. »
CONTEXTE  : —
INCERTITUDE : —

CHIFFRE   : 43,7 points de PIB (estimation Cour des comptes, février 2026, antérieure au chiffre INSEE définitif de 43,6 %)
MILLÉSIME : 2025, estimation à ce stade
CHAMP     : France entière, prélèvements obligatoires, 1 300,9 Md€
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « Au total, les prélèvements obligatoires s'établiraient à 1 300,9 Md€, en hausse de 50,1 Md€ par rapport à 2024, soit une augmentation de 4,0 % en valeur. Cette progression serait supérieure à celle du PIB (+ 2,0 %) si bien que le ratio de prélèvements obligatoires augmenterait fortement (+ 0,9 point), atteignant 43,7 points de PIB. Il retrouverait un niveau proche de celui connu en amont de la crise sanitaire (44,0 points de PIB en 2019). »
CONTEXTE  : Écart de 0,1 point avec le chiffre INSEE définitif (43,6 %) — même mécanique prévu/réalisé que pour le déficit, mais avec un écart beaucoup plus faible ici.
INCERTITUDE : —

### Comparaison européenne — prélèvements obligatoires, mesure Eurostat

CHIFFRE   : 43,5 points de PIB en 2024, taux le plus élevé de la zone euro (à égalité avec l'Autriche)
MILLÉSIME : 2024
CHAMP     : zone euro, taux de prélèvements obligatoires mesuré par Eurostat (les crédits d'impôt n'en sont pas déduits, à la différence de la mesure INSEE en comptabilité nationale)
SOURCE    : Cour des comptes, *La situation des finances publiques début 2026*, février 2026, citant Eurostat
URL       : https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2026
EXTRAIT   : « la France affichait toujours, en 2024, le taux le plus élevé de la zone euro, à 43,5 points de PIB, tel que mesuré par Eurostat. » Note : « Le taux de prélèvements obligatoires de l'Autriche atteignait le même niveau. » Note méthodologique : « Les prélèvements obligatoires mesurés par Eurostat se distinguent de ceux mesurés par l'INSEE en comptabilité nationale car les crédits d'impôts n'en sont pas déduits. »
CONTEXTE  : Explique l'écart entre le chiffre Eurostat (43,5 %, 2024) et le chiffre INSEE (42,8 %, 2024) pour le même millésime — pas une erreur, une différence de définition du champ.
INCERTITUDE : —

### Comparaison européenne — déficit et dette, données 2025 définitives (Eurostat, avril 2026)

CHIFFRE   : Zone euro (20 pays) — déficit 2,9 % du PIB (après 3,0 % en 2024) ; dette 87,8 % du PIB (après 87,0 % en 2024). Union européenne — déficit 3,1 % du PIB (stable) ; dette 81,7 % du PIB (après 80,7 %).
MILLÉSIME : 2025
CHAMP     : agrégats zone euro et UE, administrations publiques
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf
EXTRAIT   : « In the euro area (EA20) the government deficit to GDP ratio decreased from 3.0% in 2024 to 2.9% in 2025. In the EU, it remained unchanged at 3.1%, the same level as in 2024. In the euro area the government debt to GDP ratio increased from 87.0% at the end of 2024 to 87.8% at the end of 2025, and in the EU from 80.7% to 81.7%. »
CONTEXTE  : —
INCERTITUDE : —

CHIFFRE   : classement des déficits 2025 dans l'UE — les plus élevés : Roumanie (−7,9 %, hors zone euro), Pologne (−7,3 %, hors zone euro), Belgique (−5,2 %), France (−5,1 %)
MILLÉSIME : 2025
CHAMP     : Union européenne, tous pays membres, administrations publiques
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf
EXTRAIT   : « The highest deficits were recorded in Romania (‑7.9%), Poland (-7.3%), Belgium (-5.2%) and France (‑5.1%). Eleven Member States had deficits equal to or higher than 3% of GDP. »
CONTEXTE  : **Dans la zone euro strictement (hors Pologne et Roumanie, non-membres), la Belgique dépasse désormais la France sur le déficit 2025 (−5,2 % contre −5,1 %)** — alors qu'en 2024 la France était le déficit le plus dégradé de la zone euro (voir chiffre détaillé ci-dessous, France 2024 = −5,8 %, Belgique 2024 = −4,4 %). C'est un basculement notable entre les deux derniers millésimes.
INCERTITUDE : —

CHIFFRE   : classement des dettes 2025 dans l'UE — les plus élevées parmi les pays dépassant 60 % de PIB : Grèce (146,1 %), Italie (137,1 %), France (115,6 %), Belgique (107,9 %), Espagne (100,7 %)
MILLÉSIME : fin 2025
CHAMP     : Union européenne, administrations publiques
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf
EXTRAIT   : « Twelve Member States had government debt ratios higher than 60% of GDP, with the highest registered in Greece (146.1%), Italy (137.1%), France (115.6%), Belgium (107.9%) and Spain (100.7%). »
CONTEXTE  : France 3ᵉ pays le plus endetté de l'UE.
INCERTITUDE : —

### Chiffres détaillés par pays (tableau Eurostat, séries 2022-2025)

CHIFFRE   : Allemagne — déficit −2,7 % du PIB (2025, −119 147 M€), dette 63,5 % du PIB (2025, 2 838 239 M€) ; Italie — déficit −3,1 % du PIB (2025, −69 381 M€), dette 137,1 % du PIB (2025, 3 095 888 M€) ; Belgique — déficit −5,2 % du PIB (2025, −33 220 M€), dette 107,9 % du PIB (2025, 692 461 M€) ; France — déficit −5,1 % du PIB (2025, −152 511 M€), dette 115,6 % du PIB (2025, 3 460 465 M€), dépenses publiques 57,2 % du PIB, recettes publiques 52,1 % du PIB
MILLÉSIME : 2025
CHAMP     : administrations publiques, comptabilité nationale ESA 2010, notification EDP
SOURCE    : Eurostat, *Provision of deficit and debt data for 2025 — first notification*, Euro Indicators, 22 avril 2026
URL       : https://www.ksh.hu/en/first-releases/krm/eurostat_press_release_2026_04_22.pdf
EXTRAIT   : « Germany [...] Government deficit (-) / surplus(+) [...] -119 147 [...] (% of GDP) [...] -2.7 [...] Government debt [...] 2 838 239 [...] (% of GDP) [...] 63.5 » ; « Italy [...] -69 381 [...] -3.1 [...] Government debt [...] 3 095 888 [...] (% of GDP) [...] 137.1 » ; « France [...] Government expenditure (% of GDP) 58.4 56.8 57.0 57.2 [...] Government revenue (% of GDP) 53.7 51.4 51.2 52.1 »
CONTEXTE  : France 2024 (pour comparaison historique) : déficit −5,8 % (−169 118 M€), dette 112,6 % ; Belgique 2024 : déficit −4,4 % (−27 057 M€), dette 103,9 %. L'écart de dette France-Allemagne (115,6 % contre 63,5 %) est de 52,1 points de PIB.
INCERTITUDE : —

---

## CE QUI CONTREDIT L'ANGLE (dispositif : sous-exposition, dégradation attendue)

Le thème « finances publiques » est structurellement orienté vers la dégradation (dette et charge d'intérêts en hausse). Éléments trouvés qui nuancent ou contredisent ce récit :

1. **Le déficit 2025 s'est amélioré, et plus que ne le prévoyait la Cour des comptes.** L'INSEE l'établit à 5,1 % du PIB (mars 2026), contre une estimation de la Cour des comptes de 5,4 % (février 2026) et 5,8 % en 2024. C'est la première amélioration depuis 2019 selon la série longue Insee Première (le déficit s'était dégradé sans interruption de 2019 à 2024). Sources : INSEE Informations rapides n° 78 ; Cour des comptes, février 2026.

2. **La France a perdu son rang de pire déficit de la zone euro en 2025.** Sur la base des données Eurostat définitives (avril 2026), la Belgique affiche un déficit plus dégradé que la France en 2025 (−5,2 % contre −5,1 %), alors qu'en 2024 c'était l'inverse (France −5,8 %, Belgique −4,4 %). Ce basculement n'a pas été anticipé par la Cour des comptes en février 2026, qui prévoyait encore la France en tête des déficits de la zone euro pour 2025 sur la base des prévisions de la Commission de novembre 2025 (« le solde public français demeurerait en 2025, comme en 2024, le plus dégradé de la zone euro »).

3. **Le taux de croissance des dépenses publiques primaires ralentit.** Selon la Cour des comptes (février 2026), hors charge d'intérêts, les dépenses publiques ont progressé de 2,5 % en valeur et 1,3 % en volume en 2025, contre 4,0 % en valeur en 2024 — un ralentissement net.

4. **Le spread OAT-Bund et les conditions de marché se sont légèrement détendus début 2026** selon la Cour des comptes : « La perspective de l'adoption d'une loi de finances en janvier 2026 a légèrement détendu les taux français début 2026, si bien que ces derniers se retrouvent légèrement en-dessous des taux italiens et grecs en février 2026 » — nuance dans un tableau par ailleurs alarmant (taux passés de 2,90 % à 3,45 % en deux ans).

Élément à charge (pour équilibrer cette section, conformément à la règle de recherche du contrefactuel dans les deux sens) : **le déficit primaire persiste et se creuse.** La dépense publique primaire (hors charge de la dette) a progressé de 40 Md€ en 2025 selon la Cour des comptes, à un rythme supérieur à la croissance économique, ce qui contribue à creuser le déficit à hauteur de 0,3 point de PIB indépendamment de la charge d'intérêts elle-même — la dégradation ne tient donc pas qu'aux intérêts.

---

## PISTES NON ABOUTIES

1. **Domaine aft.gouv.fr systématiquement inaccessible.** Toutes les tentatives d'ouverture directe (communiqué de presse, bulletin mensuel PDF, page « encours de la dette négociable », version anglaise et française) ont renvoyé une erreur HTTP 403, y compris via `curl` direct par le proxy de l'environnement. Conséquence directe : le chiffre de maturité moyenne « 8,5 ans » pour 2026, largement repris dans la presse, n'a pu être vérifié en source primaire — je n'ai pu confirmer qu'un chiffre plus ancien (8,2 ans fin 2020, Trésor-Éco n° 297) et une citation de la Cour des comptes (« huit ans », sans date précise). De même, la structure de détention de la dette par catégorie d'investisseurs n'a pu être actualisée au-delà de T2 2021 (Trésor-Éco). **Ce point mérite une seconde passe si l'accès à aft.gouv.fr est rétabli.**

2. **Avis du Haut Conseil des finances publiques n° HCFP-2026-3 (17 avril 2026), non lu en intégralité.** Le fetch sur Légifrance n'a renvoyé qu'un résumé avec citations partielles, non garanties mot pour mot. Contient pourtant des données importantes et potentiellement discordantes avec la Cour des comptes de février 2026 (charge d'intérêts 2026 « plus de 78 Md€ » selon le résumé HCFP contre 73,6 Md€ selon la Cour des comptes de deux mois plus tôt — écart à investiguer, soit révision réelle, soit champ différent, soit erreur de résumé). **Point prioritaire pour une seconde passe.**

3. **Rapport Sénat sur les Engagements financiers de l'État (l25-139-312) : citations non revérifiées mot pour mot.** Le fetch initial a produit des citations avec guillemets pour certains chiffres (émissions, sensibilité aux taux, comparaisons budgétaires) et un résumé sans guillemets pour d'autres (trajectoire 2027-2029 de la charge de la dette). Je les ai reproduites en distinguant les deux cas, mais une lecture directe du HTML intégral permettrait de lever le doute sur les citations non garanties.

4. **Rapport Insee Première n° 2106 (*Le compte des administrations publiques en 2025*) : non ouvert directement.** Les chiffres de la série longue dette/PIB (2019-2025) et dépenses/PO en % du PIB proviennent d'un résumé de l'outil de fetch, pas d'une lecture directe par moi du document. Le léger écart constaté (115,7 % contre 115,6 % pour 2025 selon l'Informations rapides n° 78) mérite vérification pour déterminer s'il s'agit d'une véritable divergence entre les deux publications INSEE ou d'une erreur de transcription du résumé.

5. **Comparaison européenne de la charge d'intérêts en % du PIB (France vs Allemagne vs zone euro), citée dans l'archive non sourcée (France 2,2 %, Allemagne 1,1 %, zone euro 1,9 %, source FIPECO) — non revérifiée avec une source primaire dans cette session.** FIPECO n'est pas un producteur public ; à défaut de mieux, la Cour des comptes donne un ratio France seul (2,2 % du PIB en 2025, 2,4 % en 2026 prévu, tableau n° 14) mais pas de comparaison internationale directe en % de PIB pour la charge d'intérêts — seulement une comparaison en taux d'intérêt de marché (§ ci-dessus). Une recherche Eurostat dédiée aux « intérêts versés par les administrations publiques, % du PIB, par pays » n'a pas été menée faute de budget disponible dans cette session — piste pour une seconde passe.

6. **Rang précis de la charge d'intérêts française en % du PIB au sein de l'UE/zone euro** : non trouvé en source primaire directe (Eurostat publie une série « interest payable » par pays dans ses tableaux de finances publiques, non consultée faute de temps).

7. **Détention de la dette par les assureurs français et part des non-résidents pour 2025-2026** (chiffres « 56 % non-résidents / 44 % résidents » et « ~10 % assureurs français » cités dans l'archive non sourcée, sourcés à l'époque sur IFRAP et un site tiers « dettedelafrance.fr ») — non retrouvés en source primaire (Banque de France ou AFT) dans cette session, l'accès à l'AFT étant bloqué. La seule donnée vérifiée en primaire reste celle, ancienne, de Trésor-Éco n° 297 (T2 2021).

8. **PLF 2026 : statut de vote non éclairci de bout en bout.** Le texte examiné a été adopté via l'article 49.3 (engagement de responsabilité du Gouvernement), confirmé par citation Cour des comptes de janvier 2026 ; je n'ai pas vérifié dans cette session s'il a depuis fait l'objet d'une motion de censure rejetée, d'une promulgation formelle en loi de finances, ou d'un nouvel épisode d'instabilité — élément de contexte politique pertinent pour le dispositif « faux grands nombres » ou les précautions de lecture, à vérifier séparément si besoin.

9. **Budget disponible non consacré à une comparaison chiffrée dépenses publiques par fonction (santé, retraites, éducation, défense) en % du PIB, France vs zone euro** — hors du strict périmètre demandé pour cette collecte (dette, déficit, charge d'intérêts), mais mentionné dans le rapport Cour des comptes (graphique n° 6, « ratio de dépenses publiques par rapport au PIB dans les principaux pays de la zone euro en 2024 », non extrait car présenté sous forme de graphique non restituable en texte par l'extraction PDF).
