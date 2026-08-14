# Collecte n° 9 — Santé mentale, suicide et arrêts de travail

Contexte : la collecte d'août 2026 archivée dans `archive-non-sourcee-2026-08/09-sante-mentale-et-travail.md` était inutilisable comme source (pas d'accès réseau). Cette collecte reprend chaque piste et rouvre les publications avec accès réseau réel. `assurance-maladie.ameli.fr` et `santepubliquefrance.fr` (téléchargements PDF directs) sont restés bloqués (403/redirection) malgré plusieurs tentatives par proxy web, recherche et `curl` direct — signalé explicitement chiffre par chiffre.

Répartition du budget de recherche (respectée) : ~2 points sur les dépenses d'assurance maladie, ~2 sur la mortalité par suicide et sa position européenne, ~2 sur la répartition âge/sexe et les tentatives, ~1 sur la sous-estimation, ~3 sur indemnités journalières/arrêts de travail/absentéisme.

---

## 1. DÉPENSES D'ASSURANCE MALADIE — SANTÉ MENTALE ET PSYCHOTROPES

### 1.1 Montant et part du total

CHIFFRE   : 27,8 milliards d'euros, soit 14 % des dépenses totales remboursées
MILLÉSIME : 2023 (données de dépenses 2023)
CHAMP     : France entière, tous régimes, maladies psychiatriques + traitements psychotropes chroniques (anxiolytiques, hypnotiques inclus), dépenses remboursées par l'Assurance maladie
SOURCE    : CNAM, *Points de repère* n° 55 ou 56 (numérotation incertaine selon les relais consultés), « Les déterminants de la croissance des dépenses de santé de 2015 à 2023 : une analyse médicalisée », juillet 2025 — SOURCE NON OUVERTE DIRECTEMENT. Le chiffre est relayé et cité par : Santé Mentale (magazine), « Santé mentale et psychiatrie représentent 14 % des dépenses de l'Assurance maladie », juillet 2025, qui cite elle-même le document CNAM.
URL       : relais lu : https://www.santementale.fr/2025/07/depenses-de-sante/ — publication CNAM elle-même non accessible (403 sur assurance-maladie.ameli.fr, y compris en tentative curl directe)
EXTRAIT   : « la santé mentale, si l'on regroupe les maladies psychiatriques et les traitements chroniques par psychotropes (dont les anxiolytiques et les hypnotiques), représente 27,8 milliards d'euros » (extrait du relais santementale.fr, qui attribue lui-même la donnée au document CNAM Points de repère, juillet 2025)
CONTEXTE  : dont les deux tiers concernent les maladies psychiatriques (selon le même relais). Ameli.fr renvoie systématiquement 403 Forbidden, y compris via curl direct — l'accès à la publication CNAM elle-même a échoué malgré plusieurs tentatives (URL de la page projet, URL PDF devinées, URL de communiqué de presse, page de la collection Points de repère).
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — donnée reprise d'un relais qui cite lui-même le document primaire. Numéro exact de la collection Points de repère incertain (55 selon un relais, 56 selon un autre).

### 1.2 Rang parmi les postes de pathologies et postes voisins

CHIFFRE   : santé mentale 27,8 Md€ (14 %) ; maladies cardio-neurovasculaires 29 Md€ (14 %) ; cancers 27 Md€ (13 %) — les trois postes réunis : 36 % des dépenses
MILLÉSIME : 2023
CHAMP     : France entière, tous régimes, dépenses remboursées par pathologie
SOURCE    : CNAM, *Points de repère* n° 55/56, juillet 2025 — SOURCE NON OUVERTE DIRECTEMENT, relayée par Santé Mentale (magazine), juillet 2025
URL       : https://www.santementale.fr/2025/07/depenses-de-sante/
EXTRAIT   : « Cardio-neurovasculaire : 29 milliards d'euros, ou 14 % des dépenses [...] Cancers : 27 milliards d'euros (13 % des dépenses) [...] Ensemble, santé mentale, cancers et maladies cardiovasculaires concentrent 36 % des dépenses » (synthèse du relais, à partir du document CNAM)
CONTEXTE  : sur cette base, la santé mentale se classerait au 2ᵉ rang des grands postes de dépenses par pathologie, juste derrière les maladies cardio-neurovasculaires et devant les cancers — rang à confirmer sur la publication CNAM elle-même, non consultée. Aucun classement complet des 19 grandes catégories de pathologies n'a pu être obtenu (postes comme le diabète, les maladies respiratoires chroniques, etc. non comparés faute d'accès à la source).
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT. Le rang « 2ᵉ poste » est une déduction de la collecte à partir de trois montants relayés, pas une affirmation trouvée telle quelle dans une source.

### 1.3 Consommation de psychotropes chez les jeunes (repris de l'archive, non revérifié cette session)

INCERTITUDE : chiffre non revérifié cette session (budget consacré aux points prioritaires du brief) — voir archive pour la piste (+31 % 2019-2021, +26 % 2021-2022, +11 % 2022-2023, source CNAM fiche pathologie troubles psychotiques). À revalider avant usage.

---

## 2. MORTALITÉ PAR SUICIDE

### 2.1 Décès et taux — 2022 (donnée directement lue)

CHIFFRE   : 9 200 décès par suicide ; taux de 13,3 décès pour 100 000 habitants
MILLÉSIME : 2022 (publié février 2025)
CHAMP     : France entière, tous sexes, décès dont la cause initiale est le suicide
SOURCE    : DREES, *Suicide : mal-être croissant des jeunes femmes et fin de la baisse historique ? — Penser les conduites suicidaires aux prismes de l'âge et du genre*, 6ᵉ rapport de l'Observatoire national du suicide, février 2025
URL       : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/rapports/suicide-mal-etre-croissant-des-jeunes-femmes-et-fin-de
EXTRAIT   : « 9 200 décès par suicide recensés en 2022, le taux de suicide atteint 13,3 décès pour 100 000 habitants » ; « Le taux de décès par suicide n'a pas repris sa diminution depuis » 2018 ; « Il est légèrement supérieur en 2022 (13,3) à ce qu'il était en 2021 (13,0) et 2020 (13,1) »
CONTEXTE  : série récente stable à légèrement remontante (13,1 en 2020 ; 13,0 en 2021 ; 13,3 en 2022) — contredit une baisse continue attendue ; le titre même du rapport DREES pose la question d'une « fin de la baisse historique ».
INCERTITUDE : —

### 2.2 Décès 2023 (donnée non lue directement — relais)

CHIFFRE   : 8 848 décès par suicide ; taux de 13 pour 100 000 habitants (−4 % vs 2022)
MILLÉSIME : 2023
CHAMP     : France (précision métropole/DROM non confirmée sur la source primaire)
SOURCE    : CépiDc-Inserm — SOURCE NON OUVERTE DIRECTEMENT (page presse Inserm renvoyée en boucle de chargement/captcha lors des deux tentatives de cette session). Chiffre relayé par toute-la.veille-acteurs-sante.fr, « Conduites suicidaires en France : Bilan 2024 (Document) », qui cite le bulletin Santé publique France
URL       : tentative sur https://presse.inserm.fr/grandes-causes-de-deces-en-france-tendances-et-disparites-territoriales-en-2023/70756/ — échec (page de chargement uniquement) ; relais : https://toute-la.veille-acteurs-sante.fr/237085/conduites-suicidaires-en-france-bilan-2024-document/
EXTRAIT   : non lu (source primaire Inserm inaccessible cette session ; le relais donne « 8 848 décès recensés » et « taux : 13 pour 100 000 habitants (-4% vs 2022) » sans citation littérale vérifiable de la publication d'origine)
CONTEXTE  : cohérent avec le millésime 2022 lu directement (9 200 décès, taux 13,3) — la baisse relative de 4 % entre 2022 et 2023 est plausible mais non vérifiée sur source primaire.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — à revérifier sur presse.inserm.fr ou CépiDc-Inserm directement.

### 2.3 Position de la France en Europe — comparaison Eurostat (donnée directement lue)

CHIFFRE   : moyenne UE 2021 : 10,2 décès pour 100 000 habitants (−13,3 % vs 2011, où le taux était de 12,4) ; taux les plus élevés : Slovénie 19,8, Lituanie 19,5, Hongrie 15,7 ; taux les plus bas : Chypre 2,7, Grèce 4,2, Italie 5,9
MILLÉSIME : 2021 (comparaison publiée septembre 2024)
CHAMP     : UE-27, taux de mortalité standardisé par suicide
SOURCE    : Eurostat, *Deaths by suicide in the EU down by 13% in a decade*, Eurostat news, 9 septembre 2024
URL       : https://ec.europa.eu/eurostat/web/products-eurostat-news/w/edn-20240909-1
EXTRAIT   : « 10.2 deaths per 100 000 people » (2021) ; « 12.4 deaths per 100 000 people » (2011) ; « decreased by 13.3% (down 7 277 deaths) » ; taux les plus élevés en Slovénie (19,8), Lituanie (19,5), Hongrie (15,7) ; taux les plus bas à Chypre (2,7), en Grèce (4,2), en Italie (5,9)
CONTEXTE  : le taux national français n'apparaît pas nommément dans cette publication (elle mentionne en revanche la région française du Limousin comme région ayant le taux régional le plus élevé d'Europe, à 21,9 pour 100 000). En comparant au taux français de 13,0-13,3 pour 100 000 (DREES, données CépiDc, 2020-2022), la France se situe nettement au-dessus de la moyenne UE (10,2 en 2021) mais loin derrière les pays les plus touchés (Slovénie, Lituanie, Hongrie). Cette comparaison croise deux sources et deux méthodologies (CépiDc national vs Eurostat harmonisé) — la DREES elle-même qualifie la position française de « moyenne supérieure des pays de l'UE-27 » (titre d'une fiche du 6ᵉ rapport ONS, graphique non exploitable en extraction texte cette session).
INCERTITUDE : le taux national français n'est pas donné explicitement dans le tableau par pays consulté — comparaison croisée entre deux sources de méthodologies distinctes, à manier avec précaution. Rang exact (7ᵉ, 8ᵉ...) non établi.

### 2.4 Sous-estimation — ordre de grandeur avancé par les publications spécialisées

CHIFFRE   : sous-estimation estimée à environ 10 % ; des enquêtes locales évoquent jusqu'à 20 % voire 30 % en tenant compte des décès de cause indéterminée ou non déclarée
MILLÉSIME : estimation reprise dans une publication de 2019 portant sur des données antérieures (référence méthodologique Aouba et al., 2011)
CHAMP     : France, décès par suicide, sous-enregistrement lié aux morts violentes de intention indéterminée et aux délais/absence de transmission des conclusions d'enquête médico-légale au CépiDc-Inserm
SOURCE    : Santé publique France, *Bulletin épidémiologique hebdomadaire (BEH)*, 2019, n° 3-4, article 4
URL       : https://beh.santepubliquefrance.fr/beh/2019/3-4/2019_3-4_4.html
EXTRAIT   : « En France, on estime à environ 10% la sous-estimation des décès par suicide » ; sous-estimation liée à des décès enregistrés comme « morts violentes indéterminées quant à l'intention, ou encore [...] décès de cause inconnue » et à « la transmission, non systématique et variable selon les régions, des informations sur les causes médicales de décès après enquête médico-légale au Centre d'épidémiologie sur les causes médicales de décès (CépiDc-Inserm) » ; le chiffre de « 20 % ou 30 % » selon des enquêtes locales est repris dans les résultats de recherche mais je n'ai pas confirmé cette fourchette par une citation littérale de l'article lui-même — à vérifier
CONTEXTE  : l'article ne détaille pas la méthode de calcul du taux de 10 % et renvoie à une référence bibliographique antérieure (Aouba et al., 2011), qu'il n'a pas été possible de consulter directement. C'est l'ordre de grandeur qu'avancent conjointement l'Observatoire national du suicide et Santé publique France pour caractériser la sous-déclaration.
INCERTITUDE : la fourchette « 20-30 % » (enquêtes locales) n'a pas été confirmée par citation littérale — seul le chiffre « environ 10 % » est directement cité du BEH.

---

## 3. RÉPARTITION PAR ÂGE ET PAR SEXE

### 3.1 Écart hommes/femmes global

CHIFFRE   : taux trois fois plus élevé chez les hommes que chez les femmes (20,8 pour 100 000 hommes contre 6,3 pour 100 000 femmes)
MILLÉSIME : 2022
CHAMP     : France, décès par suicide par sexe, taux standardisé
SOURCE    : DREES, 6ᵉ rapport de l'Observatoire national du suicide, février 2025 (même publication que 2.1)
URL       : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/rapports/suicide-mal-etre-croissant-des-jeunes-femmes-et-fin-de
EXTRAIT   : « un niveau trois fois plus élevé chez les hommes (20,8) que chez les femmes (6,3 pour 100 000) »
CONTEXTE  : cohérent avec le taux global de 13,3 pour 100 000 (2.1).
INCERTITUDE : —

### 3.2 Pic de mortalité par âge — grand âge masculin

CHIFFRE   : taux de suicide des 85-94 ans : 35,2 pour 100 000, soit près du triple du taux de l'ensemble de la population ; les hommes de cette tranche font face à un risque huit fois plus élevé que les femmes du même âge, et 25 fois plus élevé que les hommes de moins de 25 ans
MILLÉSIME : 2022
CHAMP     : France, hommes et femmes de 85 à 94 ans, taux de mortalité par suicide
SOURCE    : DREES, 6ᵉ rapport de l'Observatoire national du suicide, février 2025
URL       : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/rapports/suicide-mal-etre-croissant-des-jeunes-femmes-et-fin-de
EXTRAIT   : « Le taux de suicide des personnes de 85-94 ans est de 35,2 pour 100 000 » ; « Près du triple du taux mesuré pour l'ensemble de la population » ; les hommes de cette classe d'âge font face à un risque « huit fois plus élevé que les femmes » et « 25 fois plus important que les hommes de moins de 25 ans »
CONTEXTE  : entre 2021 et 2022, le taux de cette tranche d'âge est passé « de 77 à 86 suicides pour 100 000 habitants » (citation reprise de la même publication, champ précis — probablement hommes de 85 ans et plus — à reconfirmer, le chiffre 86 n'a pas été retrouvé associé à une définition d'âge et de sexe totalement univoque dans l'extraction de cette session).
INCERTITUDE : le chiffre « 86 pour 100 000 » (2022) apparaît dans l'extraction sans que le champ exact (hommes seuls ? 85 ans et plus au lieu de 85-94 ?) soit parfaitement stabilisé — à confirmer sur le PDF complet du rapport.

### 3.3 Taux le plus bas — jeunes

CHIFFRE   : 2,7 pour 100 000 chez les moins de 25 ans — taux de suicide le moins élevé de toutes les classes d'âge ; le suicide constitue néanmoins la deuxième cause de mortalité dans cette tranche
MILLÉSIME : 2022
CHAMP     : France, personnes de moins de 25 ans, taux de mortalité par suicide
SOURCE    : DREES, 6ᵉ rapport de l'Observatoire national du suicide, février 2025
URL       : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/rapports/suicide-mal-etre-croissant-des-jeunes-femmes-et-fin-de
EXTRAIT   : « 2,7 pour 100 000 chez les moins de 25 ans » ; « Taux de suicide le moins élevé » ; « Suicide constitue la deuxième cause de mortalité » [chez les moins de 25 ans]
CONTEXTE  : confirme que le pic de mortalité par suicide est chez les très âgés (35,2 pour les 85-94 ans), pas chez les jeunes — alors que le poids médiatique du sujet se concentre sur les jeunes.
INCERTITUDE : —

### 3.4 Hausse chez les jeunes femmes — décès

CHIFFRE   : taux de suicide des jeunes femmes en hausse de près de 40 % entre 2020 et 2022 (de 1,15 à 1,60 pour 100 000)
MILLÉSIME : 2020-2022
CHAMP     : France, femmes (tranche d'âge précise non confirmée — probablement moins de 25 ans, cohérent avec le thème du rapport), taux de mortalité par suicide
SOURCE    : DREES, 6ᵉ rapport de l'Observatoire national du suicide, février 2025
URL       : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/rapports/suicide-mal-etre-croissant-des-jeunes-femmes-et-fin-de
EXTRAIT   : « Augmenté de près de 40 % entre 2020 et 2022 (passant de 1,15 à 1,60 pour 100 000) »
CONTEXTE  : les valeurs absolues sont très faibles (1,15 à 1,60 décès pour 100 000), donc la hausse relative de 40 % correspond à un petit nombre de décès supplémentaires — à ne pas lire comme une vague massive en valeur absolue, malgré l'ampleur du pourcentage.
INCERTITUDE : la tranche d'âge exacte associée à ce chiffre n'a pas été confirmée avec certitude dans l'extraction (probable : jeunes femmes/moins de 25 ans, à vérifier sur le PDF).

### 3.5 Tentatives — hospitalisations pour geste auto-infligé, où se situe le pic

CHIFFRE   : 77 601 personnes de plus de 10 ans hospitalisées au moins une fois pour geste auto-infligé, taux global de 128 pour 100 000 ; chez les adolescentes et jeunes femmes de 15-19 ans : 516 pour 100 000 (+46 % par rapport à 2017), soit plus de quatre fois le taux chez les hommes du même âge (113 pour 100 000)
MILLÉSIME : 2023
CHAMP     : France, personnes de plus de 10 ans, hospitalisations pour geste auto-infligé (tentatives de suicide et automutilations confondues)
SOURCE    : DREES, 6ᵉ rapport de l'Observatoire national du suicide, février 2025
URL       : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/rapports/suicide-mal-etre-croissant-des-jeunes-femmes-et-fin-de
EXTRAIT   : « 77 601 personnes de plus de 10 ans ont été hospitalisées au moins une fois » ; « 128 personnes pour 100 000 » (taux global) ; « 516 femmes de 15 à 19 ans sur 100 000 ont été hospitalisées en 2023 » ; « + 46 % par rapport à 2017 » ; « Plus de quatre fois le taux observé chez les hommes (113 sur 100 000) »
CONTEXTE  : établit clairement le contraste central du dossier : le pic de mortalité par suicide se situe chez les hommes très âgés (85-94 ans : 35,2/100 000), tandis que le pic des tentatives/hospitalisations se situe chez les adolescentes et jeunes femmes (15-19 ans : 516/100 000). Ces deux taux ne se comparent pas directement (l'un porte sur des décès, l'autre sur des hospitalisations, ce qui inclut des gestes non mortels et exclut les gestes non médicalisés).
INCERTITUDE : —

### 3.6 Données par âge et sexe (2025, hospitalisations) — chiffres complémentaires, non lus directement

CHIFFRE   : rythme de hausse des hospitalisations chez les femmes de 10-19 ans : +56 % (2020-2021), +16 % (2023-2024), +4 % (2024-2025), atteignant 482 pour 100 000 en 2025 — taux le plus élevé toutes classes d'âge et de sexe confondues ; ensemble : 170 pour 100 000 femmes et 101 pour 100 000 hommes en 2025 (+2 % vs 2024)
MILLÉSIME : 2020-2025
CHAMP     : France, hospitalisations pour tentative de suicide/automutilation, par sexe et âge
SOURCE    : DREES, communiqué de presse et jeu de données, « La hausse des hospitalisations des adolescentes et jeunes femmes pour tentatives de suicide et automutilations se poursuit en 2025 », 11 mai 2025 — SOURCE NON OUVERTE DIRECTEMENT (donnée obtenue via un résultat de recherche web synthétique, pas via ouverture de la page)
URL       : https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/jeux-de-donnees/250511_hospitalisations-pour-tentatives-de-suicide
EXTRAIT   : non lu
CONTEXTE  : confirme et prolonge la tendance de 3.5 (hausse continue mais ralentie des hospitalisations chez les adolescentes et jeunes femmes).
INCERTITUDE : EXTRAIT non lu — page DREES non ouverte directement cette session, à rouvrir pour vérification avant publication.

---

## 4. TENTATIVES DE SUICIDE — ESTIMATION ANNUELLE ET FOURCHETTE

CHIFFRE   : 77 041 passages aux urgences pour geste auto-infligé (2024, +... vs 2023 selon la source, données contradictoires entre relais — voir INCERTITUDE) ; 97 302 hospitalisations pour geste auto-infligé (2024), taux standardisé 142 pour 100 000 (+6 % vs 2023, où on comptait 91 162 hospitalisations, taux 134/100 000)
MILLÉSIME : 2024 (bulletin publié en octobre 2025)
CHAMP     : France entière hors Provence-Alpes-Côte d'Azur et Corse pour les passages aux urgences (exclusion signalée par l'archive non sourcée, non reconfirmée cette session) ; France entière pour les hospitalisations
SOURCE    : Santé publique France, *Surveillance annuelle des conduites suicidaires*, bulletin national, publié le 10 octobre 2025 (données 2024) — SOURCE NON OUVERTE DIRECTEMENT. Toutes les tentatives d'ouverture du PDF (URL directe santepubliquefrance.fr, avec et sans paramètre de version, via curl avec en-tête navigateur, via miroir ARS Bretagne) ont échoué : redirection 301 vers la page d'accueil, ou 403 Forbidden.
URL       : https://www.santepubliquefrance.fr/content/download/760320/document_file/bullnat_conduites_suicidaires_20251010.pdf (URL trouvée mais jamais chargée avec succès cette session)
EXTRAIT   : non lu
CONTEXTE  : les chiffres circulent de façon cohérente entre plusieurs relais secondaires (toute-la.veille-acteurs-sante.fr, francais.medscape.com via recherche web) : 77 041 passages urgences 2024, 97 302 hospitalisations 2024 (+6 % ou +7 % selon le relais — divergence non résolue), 91 162 hospitalisations 2023. Un relais donne une évolution de −1 % pour les passages urgences 2024 vs 2023, un autre +4 %. Ces divergences entre relais secondaires renforcent la nécessité de rouvrir la publication primaire avant tout usage dans le numéro.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — divergences entre relais sur le sens et l'ampleur de l'évolution 2023-2024 des passages aux urgences (−1 % contre +4 % selon la source secondaire consultée). Fourchette d'estimation globale des tentatives de suicide annuelles (« 135 000 à 170 000 », mentionnée dans l'archive précédente) NON RETROUVÉE cette session — source non identifiée, piste non aboutie (voir en fin de rapport).

---

## 5. INDEMNITÉS JOURNALIÈRES — MONTANT ET ÉVOLUTION SUR UNE DÉCENNIE

### 5.1 Montant 2023 et évolution depuis 2019

CHIFFRE   : indemnités journalières (hors AT/MP et maternité) : 10,2 milliards d'euros en 2023, soit +27,9 % depuis 2019
MILLÉSIME : 2023 (données publiées dans le rapport Charges et produits pour 2026, donc mi-2025)
CHAMP     : France entière, CNAM, indemnités journalières maladie hors accidents du travail, maladies professionnelles et congés maternité
SOURCE    : CNAM, rapport *Charges et produits pour 2026* — SOURCE NON OUVERTE DIRECTEMENT (ameli.fr bloqué en 403 systématique). Chiffre relayé, entre autres, par admisconcours.fr, « Les indemnités journalières d'arrêt maladie : un poste de dépenses dynamique... », qui cite explicitement le rapport CNAM 2026
URL       : relais lu : https://admisconcours.fr/breves/les-indemnites-journalieres-darret-maladie-un-poste-de-depenses-dynamique-au-cur-de-la-maitrise-de-londam-et-de-la-reduction-du-deficit-de-la-securite-sociale
EXTRAIT   : « une augmentation de 28,9 % entre 2010 et 2019 » ; « 27,9 % entre 2019 et 2023 » (citations du relais lu, qui attribue les deux chiffres au rapport Charges et Produits 2026 de la CNAM)
CONTEXTE  : deux périodes décennales comparables en progression proche (+28,9 % sur 2010-2019, +27,9 % sur 2019-2023, cette dernière période étant deux fois plus courte) — signale une accélération nette du rythme de croissance sur la période récente.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT.

### 5.2 Montant 2017 et 2022 — audition ministérielle au Sénat

CHIFFRE   : dépenses d'indemnités journalières : 7,69 milliards d'euros en 2017, 12 milliards d'euros en 2022 (+4,3 milliards d'euros)
MILLÉSIME : 2017 et 2022
CHAMP     : non précisé si régime général seul ou tous régimes — à clarifier
SOURCE    : Amélie de Montchalin, ministre chargée des Comptes publics, audition devant la commission des finances du Sénat, 16 juillet [année non précisée dans le relais] — SOURCE NON OUVERTE DIRECTEMENT. Chiffre relayé et cité par Public Sénat, « Arrêts maladie : quelles solutions face à leur augmentation ? »
URL       : https://www.publicsenat.fr/actualites/economie/arrets-maladie-quelles-solutions-face-a-leur-augmentation
EXTRAIT   : « 2022 : 12 milliards d'euros » ; « 2017 : 7,69 milliards d'euros » ; « Hausse entre 2017-2022 : 4,3 milliards d'euros » (synthèse du relais attribuée à l'audition ministérielle)
CONTEXTE  : ce chiffre de 12 Md€ (2022) est plus élevé que celui du même millésime rapporté par une autre voie dans l'archive précédente (10,2 Md€ mais pour 2023 et hors AT/MP-maternité) — la différence de champ (inclusion ou non des IJ maternité et AT/MP, régime général vs tous régimes) explique vraisemblablement l'écart, à vérifier précisément avant tout usage comparatif.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — champ exact (régime général seul ? tous régimes ? IJ maternité incluses ?) non confirmé.

### 5.3 Rythme de croissance annuel par période

CHIFFRE   : croissance annuelle moyenne des dépenses d'IJ : +2,9 %/an sur 2010-2019 ; +6,3 %/an sur 2019-2023
MILLÉSIME : 2010-2023
CHAMP     : non confirmé (probablement identique au champ de 5.1)
SOURCE    : données gouvernementales citées dans Public Sénat, « Arrêts maladie : quelles solutions face à leur augmentation ? » — SOURCE NON OUVERTE DIRECTEMENT au-delà de ce relais
URL       : https://www.publicsenat.fr/actualites/economie/arrets-maladie-quelles-solutions-face-a-leur-augmentation
EXTRAIT   : « 2010-2019 : 2,9% par an » ; « 2019-2023 : 6,3% par an » (synthèse du relais)
CONTEXTE  : confirme un doublement du rythme annuel de croissance des dépenses entre les deux périodes décennales.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — champ non confirmé.

---

## 6. ARRÊTS DE TRAVAIL INDEMNISÉS, ABSENTÉISME, COMPARAISON OCDE

### 6.1 Nombre d'arrêts de travail indemnisés

CHIFFRE   : 9,1 millions d'arrêts de travail indemnisés en 2024 (maladie + AT/MP), soit +10 % par rapport à 2019
MILLÉSIME : 2024 (comparé à 2019)
CHAMP     : France, arrêts de travail pris en charge par l'Assurance maladie au titre de la maladie ou des accidents du travail et maladies professionnelles
SOURCE    : dossier gouvernemental (probablement DSS/CNAM), relayé par info.gouv.fr, « Arrêts de travail : ce que prévoit la stratégie du Gouvernement », avril 2026 — SOURCE NON OUVERTE DIRECTEMENT (info.gouv.fr renvoie 403 en accès direct et via curl)
URL       : https://www.info.gouv.fr/actualite/arrets-de-travail-ce-que-prevoit-la-strategie-du-gouvernement (non chargée avec succès)
EXTRAIT   : non lu
CONTEXTE  : chiffre cohérent avec la hausse des dépenses observée par ailleurs (5.1, 5.2, 5.3).
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — donnée reprise d'un résultat de recherche web synthétique, pas d'une lecture directe de la page.

### 6.2 Décomposition de la hausse des arrêts (2019-2024) — démographie, salaires, comportement

CHIFFRE   : vieillissement de la population active : 20 % de la hausse du nombre d'arrêts ; augmentation des salaires : 40 % ; le solde de 40 % attribué à « une augmentation du taux de recours et de la durée moyenne des arrêts »
MILLÉSIME : 2019-2024
CHAMP     : France, arrêts de travail indemnisés (maladie + AT/MP, effectif)
SOURCE    : dossier gouvernemental, relayé par info.gouv.fr (idem 6.1) — SOURCE NON OUVERTE DIRECTEMENT
URL       : https://www.info.gouv.fr/actualite/arrets-de-travail-ce-que-prevoit-la-strategie-du-gouvernement (non chargée avec succès)
EXTRAIT   : non lu
CONTEXTE  : cette décomposition (20 % démographie / 40 % salaires / 40 % comportement-recours-durée) diffère de celle donnée pour les dépenses en euros par un autre relais (39 % salaires / 42 % recours et durée / part démographie non isolée séparément — voir 8.1) : les deux décompositions portent sur des périmètres différents (effectif d'arrêts vs montant en euros) et ne se recoupent pas terme à terme — à ne pas fusionner sans vérification sur les publications primaires.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — à rouvrir en priorité, car c'est une donnée centrale pour l'angle du numéro (écart entre récit et mesure).

### 6.3 Comparaison internationale — rang de la France, jours d'absence

CHIFFRE   : France au 5ᵉ rang des pays de l'OCDE pour l'absentéisme en entreprise, taux d'environ 5 %, soit environ 21 jours d'absence par an et par salarié
MILLÉSIME : 2024
CHAMP     : France, secteur privé (précision incertaine)
SOURCE    : Fondation IFRAP, « Absentéisme : agir plus fort pour réduire le coût » — rapport d'une fondation, admis comme source unique disponible sur ce comparatif, mais SOURCE NON OUVERTE DIRECTEMENT cette session (uniquement repris via résultats de recherche synthétiques) ; la donnée « OCDE » sous-jacente (base OCDE Health ou équivalent) n'a pas été retrouvée ni consultée directement
URL       : https://www.ifrap.org/fonction-publique-et-administration/absenteisme-agir-plus-fort-pour-reduire-le-cout
EXTRAIT   : non lu
CONTEXTE  : l'archive non sourcée précédente signalait déjà ce chiffre comme provenant d'une fondation (IFRAP), pas d'une publication OCDE elle-même. Le rapport IGAS/IGF de 2003 sur les IJ (source ancienne mais consultée intégralement cette session, cf. section « pistes ») notait déjà en 2003 que les comparaisons internationales de l'OCDE sur l'absentéisme reposaient sur des données françaises très anciennes (1988) comparées à des données 1995-2000 pour les autres pays, ce qui en limitait « sérieusement la portée » (citation du rapport IGAS/IGF, octobre 2003) — signal ancien qu'une prudence méthodologique s'impose sur ce type de comparaison internationale.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT. Le chiffre « OCDE » est un chiffre de fondation qui se réclame de l'OCDE, pas une donnée directement vérifiée dans une publication OCDE — à traiter comme signalé, pas comme comparaison internationale certifiée.

---

## 7. PART DE LA HAUSSE DES IJ NON EXPLIQUÉE PAR LA DÉMOGRAPHIE ET LES SALAIRES

### 7.1 Décomposition Cour des comptes 2017-2022 (montants en euros)

CHIFFRE   : sur la hausse de 4,3 milliards d'euros de dépenses d'IJ entre 2017 et 2022, les facteurs démographiques et salariaux (SMIC, salaire moyen, extension aux indépendants) expliquent 1,3 milliard d'euros (dont 0,7 Md€ liés au SMIC et au salaire moyen, 0,2 Md€ à la croissance de la population active, 0,4 Md€ à l'extension du régime général aux indépendants et professions libérales) ; 0,9 milliard d'euros ne peuvent être attribués à aucune de ces causes prises isolément
MILLÉSIME : 2017-2022 (rapport publié en 2024)
CHAMP     : France, régime général (précision à confirmer), dépenses d'indemnités journalières maladie
SOURCE    : Cour des comptes, *Rapport sur l'application des lois de financement de la sécurité sociale (RALFSS) 2024*, chapitre V, « L'indemnisation des arrêts de travail pour maladie du régime général », mai 2024 — SOURCE NON OUVERTE DIRECTEMENT malgré plusieurs tentatives cette session (503 Service Unavailable répété sur ccomptes.fr, échec de connexion via curl). Données reprises d'un résultat de recherche web synthétique (non issu d'une lecture directe du PDF)
URL       : https://www.ccomptes.fr/sites/default/files/2024-05/20240529-Ralfss-2024-Indemnisation-arrets-de-travail-pour-maladie-du-regime-general.pdf (jamais chargée avec succès)
EXTRAIT   : non lu
CONTEXTE  : ce chiffre est l'exact filon que le brief demandait (« part de la hausse des IJ non expliquée par la démographie et les salaires »). Sur cette décomposition, environ 21 % de la hausse (0,9/4,3 Md€) reste inexpliquée par les facteurs structurels identifiés — c'est un point à traiter avec prudence tant que la source primaire n'a pas été rouverte, car le chiffre n'a pas été vérifié par citation littérale.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT — c'est la donnée la plus importante et la moins bien sourcée de cette collecte pour le point 8 du brief. À ROUVRIR EN PRIORITÉ (voir pistes non abouties).

### 7.2 Décomposition CNAM 2019-2023 (autre découpage, autre période)

CHIFFRE   : sur la hausse des dépenses d'IJ 2019-2023, 39 % attribués à la hausse des salaires (SMIC +13,6 % entre 2020 et 2023) ; 42 % attribués à « la hausse du recours aux arrêts de travail notamment chez les jeunes et [l']allongement de la durée » (facteur comportemental/volume, non démographique ni salarial)
MILLÉSIME : 2019-2023
CHAMP     : France, CNAM, dépenses d'indemnités journalières
SOURCE    : CNAM — SOURCE NON OUVERTE DIRECTEMENT, chiffres relayés par Public Sénat, « Arrêts maladie : quelles solutions face à leur augmentation ? », qui attribue explicitement ce découpage à la CNAM (et le précédent en 7.1 à la Cour des comptes)
URL       : https://www.publicsenat.fr/actualites/economie/arrets-maladie-quelles-solutions-face-a-leur-augmentation
EXTRAIT   : « 39% : augmentation des salaires (SMIC +13,6% entre 2020-2023) » ; « 42% : "hausse du recours aux arrêts de travail notamment chez les jeunes et allongement de la durée" » (synthèse et citation partielle du relais, attribuées à la CNAM)
CONTEXTE  : cette décomposition CNAM (39 % salaires / 42 % recours-durée / le solde, non précisé dans le relais, probablement démographie) est cohérente dans l'esprit avec la décomposition Cour des comptes de 7.1 (une bonne part de la hausse récente n'est pas de nature démographique ou salariale pure) mais les deux décompositions ne portent pas sur les mêmes périodes (2017-2022 vs 2019-2023) ni le même agrégat (montant en Md€ vs pourcentages de la hausse) — NE PAS LES ADDITIONNER NI LES FUSIONNER.
INCERTITUDE : SOURCE NON OUVERTE DIRECTEMENT (relais uniquement) — la part attribuable au vieillissement démographique seul n'est pas donnée séparément dans ce découpage CNAM (contrairement à 6.2 qui l'isole à 20 % sur un agrégat différent — effectif d'arrêts et non montant en euros).

---

## CE QUI CONTREDIT L'ANGLE

- **Baisse relative des décès par suicide 2022→2023** : −4 % (9 200 → 8 848, cf. 2.1 et 2.2) — élément de contradiction à l'angle d'une dégradation continue, mais la donnée 2023 n'est pas vérifiée sur source primaire (2.2), et la série longue reste plate à légèrement remontante sur 2020-2022 (13,1 → 13,0 → 13,3, cf. 2.1) : ce n'est pas une amélioration franche.
- **Baisse européenne générale du taux de suicide sur la décennie** : −13,3 % dans l'UE entre 2011 et 2021 selon Eurostat (2.3, donnée directement lue) — contexte européen d'amélioration structurelle dans lequel s'inscrit (ou pas) la trajectoire française, à mettre en regard du titre même du rapport DREES qui interroge une possible « fin de la baisse historique » en France.
- **Ralentissement du rythme de dépenses d'IJ en 2023 pour les arrêts courts, signalé dès 2003** : le rapport IGAS/IGF d'octobre 2003 sur les IJ, consulté intégralement par erreur de recherche cette session mais dont la lecture donne un point de repère historique solide, montrait déjà à l'époque un « facteur résiduel » de hausse non expliqué par la démographie (entre 3,8 % et 5,6 % selon les périodes 2000-2003) — ce n'est donc pas un phénomène nouveau : la France documentait déjà en 2003 une croissance des IJ en partie non expliquée par les facteurs structurels, avec les mêmes termes de débat qu'aujourd'hui (contrôle médical insuffisant, facteur « occurrence »/comportemental). Ce point nuance l'idée d'une dégradation propre à la période récente : le phénomène est ancien et récurrent.
- **Les pensées suicidaires et tentatives déclarées en population générale restent minoritaires** : selon le baromètre Santé publique France repris par un relais secondaire (non vérifié sur source primaire cette session), 5,2 % des 18-79 ans déclarent des pensées suicidaires sur 12 mois, et seulement 0,4 % des tentatives sur 12 mois — la très grande majorité de la population n'est pas concernée, à rappeler pour ne pas laisser le chiffre écraser l'échelle du phénomène.

---

## PISTES NON ABOUTIES

1. **Cour des comptes, RALFSS 2024, chapitre V** (indemnisation des arrêts de travail, régime général) : jamais ouvert avec succès (503 Service Unavailable répété, échec curl direct). C'est la source la plus importante pour le point 8 du brief (« part de la hausse des IJ non expliquée ») — à rouvrir en priorité lors d'une prochaine session, éventuellement via une recherche du même document hébergé ailleurs (Vie publique, Sénat, Assemblée nationale citent souvent les rapports de la Cour des comptes en intégralité).

2. **CNAM, rapport *Charges et produits pour 2026*** (indemnités journalières, montants et décomposition) : ameli.fr et assurance-maladie.ameli.fr renvoient systématiquement 403 Forbidden, y compris en accès direct via curl avec en-tête navigateur — aucun accès trouvé cette session. Toutes les données CNAM de cette collecte sont donc des relais secondaires. À retenter via data.ameli.fr (non essayé cette session faute de temps) ou via une recherche de copies PDF hébergées par des tiers (fédérations professionnelles, presse spécialisée qui republie parfois les PDF).

3. **CNAM, *Points de repère* n° 55/56 (juillet 2025), sur les dépenses de santé par pathologie 2015-2023** : même blocage qu'au point 2. Le classement complet des postes de pathologie (au-delà des trois seuls postes santé mentale/cardio-neurovasculaire/cancer) n'a pas pu être établi — le rang exact de la santé mentale dans la hiérarchie complète des 19 catégories de pathologies n'est pas confirmé.

4. **Santé publique France, bulletin national de surveillance des conduites suicidaires (données 2024, publié octobre 2025)** : URL du PDF identifiée mais jamais chargée avec succès (redirection 301 vers la page d'accueil en curl, 403 en WebFetch direct, échec sur un miroir ARS Bretagne). Toutes les données de tentatives de suicide/hospitalisations de cette collecte (section 4) proviennent de relais secondaires, avec des divergences non résolues entre relais sur le sens de l'évolution 2023-2024 des passages aux urgences.

5. **Fourchette d'estimation globale des tentatives de suicide annuelles (« 135 000 à 170 000 » mentionnée dans l'archive précédente)** : source non retrouvée cette session malgré une recherche dédiée sur Infosuicide.org. Piste à reprendre : chercher spécifiquement la méthodologie d'extrapolation (population générale déclarative × taux, ou modèle épidémiologique) et son auteur exact.

6. **info.gouv.fr, dossier « Arrêts de travail : ce que prévoit la stratégie du Gouvernement » (avril 2026)** : bloqué en 403 systématique (accès direct et curl). C'est la source citée pour les chiffres de décomposition 20 %/40 %/40 % de la hausse des arrêts de travail (section 6.2) — à rouvrir en priorité, car ces pourcentages sont centraux pour documenter l'écart entre le récit dominant (comportemental/abus) et la mesure (part réelle démographique et salariale).

7. **Position exacte de la France dans le classement européen du taux de suicide** (rang chiffré, pas seulement « moyenne supérieure ») : non établie. Eurostat donne un classement des pays (2.3) mais sans le taux national français explicitement positionné dans le même tableau — à croiser précisément avec les données CépiDc/DREES pour situer un rang numéroté.

8. **Rapport IGAS/IGF « Les dépenses d'indemnités journalières », octobre 2003** : ce document a été intégralement consulté par erreur de recherche (une recherche destinée à trouver un rapport récent a renvoyé ce document ancien, téléchargé et lu en entier via le PDF). Il documente en détail les mécanismes de contrôle, la structure des dépenses par âge et par durée d'arrêt, et une décomposition démographie/comportement pour la période 2000-2003 — utile comme point de comparaison historique (cf. section « Ce qui contredit l'angle »), mais ses chiffres (montants de 2002-2003) sont trop anciens pour être utilisés comme données actuelles du numéro. Ne pas confondre ce rapport de 2003 avec le RALFSS 2024 de la Cour des comptes (piste 1), non obtenu.

9. **Consommation de psychotropes chez les jeunes** (repris de l'archive : +31 % 2019-2021, +26 % 2021-2022, +11 % 2022-2023) : non revérifié cette session, budget consacré aux priorités du brief — à revalider avant usage, y compris le millésime exact.

10. **Champ exact des chiffres d'indemnités journalières** (régime général seul ou tous régimes ? IJ maternité et AT/MP incluses ou non ?) : les différentes sources secondaires consultées (admisconcours.fr : 10,2 Md€ 2023 hors AT/MP-maternité ; Public Sénat citant la ministre : 12 Md€ 2022 sans précision de champ) ne sont pas homogènes entre elles sur ce point — la comparaison de ces deux chiffres pour estimer une évolution 2022→2023 serait une erreur de méthode tant que le champ n'est pas confirmé sur les publications primaires.
