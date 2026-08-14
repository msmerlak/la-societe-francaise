# Collecte — Les affections de longue durée et les dépenses de santé

Répartition du budget de recherche tenue à peu près en huit lots (bénéficiaires ALD / part de la dépense / dépense moyenne / principales ALD / cartographie des pathologies / CSBM-DCSi / reste à charge / prévention), avec un rééquilibrage en cours de route : le *Points de repère* n° 54 de la CNAM (ameli.fr) s'est révélé inaccessible (voir PISTES NON ABOUTIES), ce qui a réorienté une bonne partie du budget « bénéficiaires ALD » vers le rapport IGAS-IGF, qui s'est avéré extrêmement riche et a fini par couvrir aussi une bonne partie du point « dépense moyenne » et « principales ALD ». Le point « cartographie des pathologies » reste le plus pauvre : la quasi-totalité du domaine ameli.fr/assurance-maladie.ameli.fr a été inaccessible pendant cette session (blocage type CAPTCHA « Vérification de sécurité »).

Sources principales effectivement ouvertes et lues :
- IGAS/IGF, *Revue de dépenses relative aux affections de longue durée — Pour un dispositif plus efficient et équitable*, juin 2024 (IGF n° 2023-M-109-03, IGAS n° 2023-126R), pages 1 à 44 sur 458 lues intégralement (synthèse, introduction, section 1 complète).
- DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, collection *Panoramas de la DREES*, édition 2025 (238 pages), vue d'ensemble et fiches 01 (CSBM), fiche « reste à charge » de la vue d'ensemble, comparaisons internationales, fiche 23 (prévention) lues.
- data.ameli.fr, jeu de données ouvert « Pathologies : effectif de patients par pathologie, sexe, classe d'âge et territoire », métadonnées consultées via l'API.
- documentation-snds.health-data-hub.fr, fiches « Bénéficiaires du dispositif ALD » et « Cartographie des pathologies » — ressource de documentation méthodologique du Health Data Hub (GIP public), pas la publication CNAM elle-même.

---

## 1. Bénéficiaires du dispositif ALD : effectif, part de la population, affections reconnues, âge

CHIFFRE   : 13,7 millions de personnes bénéficiaires du dispositif ALD, soit 19,9 % de la population
MILLÉSIME : 2021 (données provisoires de l'assurance maladie au moment du rapport)
CHAMP     : tous régimes confondus, France entière — population de référence : 68,7 millions de personnes « tous régimes de l'assurance maladie — France entière ayant eu au moins 1 euro de remboursement dans l'année »
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée — Pour un dispositif plus efficient et équitable*, juin 2024, p. 7 (§1.2.1) et p. 1 (synthèse), citant des données CNAM
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « En 2021, d'après les données provisoires de l'assurance maladie, 13,7 millions de personnes (soit 19,9 % de la population) bénéficient du dispositif ALD, tous régimes confondus. En moyenne, 1,3 affections sont reconnues par personne bénéficiant du dispositif. »
CONTEXTE  : note de bas de page 15 du rapport : « Population tous régimes de l'assurance maladie – France entière ayant eu au moins 1 euro de remboursement dans l'année, soit 68,7 millions de personnes. »
INCERTITUDE : donnée qualifiée de « provisoire » par la source elle-même.

CHIFFRE   : 12,3 millions de personnes reconnues en ALD (12 344 220 exactement)
MILLÉSIME : 2022
CHAMP     : régime général de l'assurance maladie SEUL (≈ 90 % de la population française selon la même source) — se décompose en 11 893 400 en ALD liste (ALD 30), 823 790 en ALD hors-liste (ALD 31), 73 980 en ALD polypathologie (ALD 32)
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 7-9 (§1.2.1, tableau 3), données CNAM « prévalence des ALD »
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « En 2022, pour le seul régime général de l'assurance maladie 12,3 millions de personnes sont reconnues en affection longue durée (ALD) et se répartissent en environ 11,9 M (soit 96,3 %) d'assurés reconnus en ALD liste, 0,8 M (soit 6,7 %) d'assurés en ALD hors-Liste, et moins de 0,1 M (soit 0,6 %) assurés en ALD polypathologie. » / Tableau 3 : « Total patients (ALD30-31-32) […] 12 344 220 [âge moyen] 63 [taux de croissance 2010-2022] 37,4 % [TCAM] 2,7 % »
CONTEXTE  : le rapport précise en note 17 que le régime général est retenu pour ce détail « car il ne représente pas l'ensemble des assurés » mais « permet d'avoir des données plus récentes et plus complètes ». Note de lecture du tableau 3 : « la somme de tous les assurés reconnus en ALD au titre d'une ALD liste n'est pas égale au total des patients en ALD 30 car un même patient peut être reconnu au titre de plusieurs ALD. »
INCERTITUDE : ⚠️ CHAMP DIFFÉRENT du chiffre précédent (13,7 M tous régimes, 2021) — les deux valeurs NE SONT PAS comparables terme à terme : millésime différent (2021 vs 2022) ET champ différent (tous régimes vs régime général seul). C'est exactement l'avertissement de champ signalé dans le brief.

CHIFFRE   : âge moyen de 65 ans parmi les assurés en ALD, contre 41 ans en moyenne dans la population française
MILLÉSIME : 2021 (âge moyen ALD) ; population française 2021 selon INSEE (référence secondaire dans le rapport)
CHAMP     : tous régimes pour l'âge moyen ALD (65 ans, synthèse) ; le tableau 3 (régime général 2022) donne un âge moyen légèrement différent (63 ans pour l'ensemble ALD30-31-32) — divergence liée au champ et au millésime
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 1 (synthèse) et p. 11 (§1.2.2)
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Ils sont également surreprésentés chez les assurés les plus modestes. […] les assurés en ALD sont sensiblement plus âgés que la population générale (65 ans contre 41 ans en moyenne). » ; ailleurs : « Les assurés en ALD sont nettement plus âgés que les autres […] : en 2021, l'âge moyen était de 41,5 ans au sein de la population française et de 66 ans parmi les assurés en ALD. »
CONTEXTE  : « les assurés en ALD sont principalement concentrés sur les tranches d'âge supérieures à 60 ans, qui représentent près des deux-tiers (64 %) des effectifs ALD contre 17 % pour la population non ALD. Après 70 ans, près d'un consommant sur deux est enregistré en ALD, contre moins de 10 % pour les patients âgés de moins de 45 ans. » Référence citée pour l'âge moyen population générale : « INSEE Âge moyen et âge médian de la population Chiffres clefs Données annuelles de 1991 à 2024 » (non ouverte directement par moi — relayée via l'IGAS-IGF).
INCERTITUDE : deux valeurs très proches mais non identiques circulent dans le même rapport (65 ans en synthèse, 66 ans en corps de texte) — signalé tel quel, sans arbitrage.

CHIFFRE   : âge médian des assurés en ALD
MILLÉSIME : —
CHAMP     : —
SOURCE    : non trouvé
URL       : —
EXTRAIT   : non lu
CONTEXTE  : le rapport IGAS-IGF (pages lues, 1 à 44) ne donne que des âges MOYENS par ALD (tableau 3) et par tranche d'âge (graphiques 2 et 5), jamais de médiane d'âge. Piste non aboutie — voir section finale.
INCERTITUDE : absence possible, pas seulement non trouvée par moi ; à revérifier dans les annexes II-III du même rapport (non lues, pages 45-458) ou dans le *Points de repère* n° 54 (bloqué).

CHIFFRE   : trois natures d'ALD — ALD liste (« ALD 30 »), ALD hors liste (« ALD 31 »), ALD polypathologie (« ALD 32 »), 29 pathologies actuellement sur la liste réglementaire
MILLÉSIME : liste en vigueur au moment du rapport (2024)
CHAMP     : cadre juridique national (article D. 160-4 du code de la sécurité sociale)
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 3-4
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Il existe trois natures d'ALD : les 29² pathologies qui sont listées explicitement par voie réglementaire après avis de la Haute autorité de santé. Présentées au tableau 1, ces pathologies sont communément appelées « ALD liste » ou « ALD 30 » ; les pathologies qui sont en dehors de cette liste mais reconnues comme « une affection grave caractérisée» et nécessitant « un traitement prolongé et une thérapeutique particulièrement coûteuse ». […] On parle alors d'« ALD hors liste » ou d'« ALD 31 » ; le patient qui est reconnu atteint de « plusieurs affections entraînant un état pathologique invalidant » et nécessite « un traitement prolongé et une thérapeutique particulièrement coûteuse ». On parle alors d'« ALD polypathologie » ou d'« ALD 32 ». »
CONTEXTE  : la liste est passée de 4 pathologies sévères en 1945 à 29-30 pathologies aujourd'hui ; « Mis en place en 1947 à la création de la Sécurité Sociale, le dispositif ALD n'a que peu évolué depuis sa création. […] la liste des ALD s'est considérablement étendue, passant de quatre pathologies sévères en 1945 à trente affections « liste » ». Seule l'ALD 12 « HTA sévère » a été retirée de la liste, en 2011.
INCERTITUDE : —

## 2. Principales ALD par effectif (régime général, 2022)

Tableau 3 du rapport IGAS-IGF, reproduit ci-dessous pour les postes principaux (source, champ, millésime identiques à la ligne « total » ci-dessus) :

CHIFFRE   : maladies cardiovasculaires (ALD 1, 3, 5, 12, 13) — 4 168 300 assurés, âge moyen 73 ans, 27,1 % du total des ALD reconnues
MILLÉSIME : 2022
CHAMP     : régime général seul
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, tableau 3, p. 8-9
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Maladies cardiovasculaires (ALD 1,3,5,12,13) 4 168 300 73 27,1% 64,4% 1,4% » [colonnes : effectifs 2022, âge moyen, part dans le total des ALD reconnues, taux de croissance 2010-2022, TCAM]
CONTEXTE  : décomposition interne : maladie coronaire (ALD 13) 1 415 300 (âge moyen 72) ; insuffisance cardiaque/troubles du rythme graves (ALD 5) 1 383 510 (âge moyen 74) ; artériopathies chroniques (ALD 3) 606 640 (âge moyen 72) ; AVC invalidant (ALD 1) 506 530 (âge moyen 71) ; HTA sévère (ALD 12, retirée de la liste en 2011 mais effectif résiduel) 256 320 (âge moyen 79).
INCERTITUDE : —

CHIFFRE   : diabète de type 1 et de type 2 (ALD 8) — 3 293 020 assurés, âge moyen 67 ans, 21,4 % du total
MILLÉSIME : 2022
CHAMP     : régime général seul
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, tableau 3, p. 8
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Diabète de type 1 et diabète de type 2 3 293 020 67 21,4% 74,7% 4,8% »
CONTEXTE  : « les quatre pathologies aux effectifs les plus importants connaissent une croissance assez dynamique depuis 2010 […] particulièrement pour le Diabète par exemple (+5 % par an en moyenne) ». Croissance 2010-2022 : +74,7 %, TCAM +4,8 %/an.
INCERTITUDE : —

CHIFFRE   : tumeur maligne, affection maligne du tissu lymphatique ou hématopoïétique (ALD 30) — 2 386 370 assurés, âge moyen 69 ans, 15,5 % du total
MILLÉSIME : 2022
CHAMP     : régime général seul
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, tableau 3, p. 8
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Tumeur maligne 2 386 370 69 15,5% 28,2% 2,1% »
CONTEXTE  : —
INCERTITUDE : —

CHIFFRE   : affections psychiatriques de longue durée (ALD 23) — 1 526 110 assurés, âge moyen 50 ans, 9,9 % du total
MILLÉSIME : 2022
CHAMP     : régime général seul
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, tableau 3, p. 8
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Affections psychiatriques de longue durée 1 526 110 50 9,9% 49,7% 3,4% »
CONTEXTE  : ALD psychiatrique nettement plus jeune en moyenne (50 ans) que la moyenne ALD (63-65 ans).
INCERTITUDE : —

CHIFFRE   : « quatre affections rassemblent chacune plus d'un million d'assurés » — présentées avec des pourcentages différents de ceux du tableau 3 : maladies cardiovasculaires 32 %, diabète 27 %, tumeurs malignes 19 %, affections psychiatriques 12 %
MILLÉSIME : 2022
CHAMP     : régime général seul
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 7 (texte courant, avant le tableau 3)
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Parmi les 29 ALD Liste, quatre affections rassemblent chacune plus d'un million d'assurés (cf. tableau 3) : les maladies cardiovasculaires avec 4,0 M d'assurés (32 % des assurés en ALD) ; le diabète de type et de type 2 avec 3,6 M d'assurés (27 % du total) ; les tumeurs malignes avec 2,6 M d'assurés (19 % du total) ; les affections psychiatriques de longue durée avec 1,7 M d'assurés, (12 % du total). »
CONTEXTE  : ⚠️ DIVERGENCE INTERNE AU MÊME RAPPORT : ce passage donne 4,0 M / 3,6 M / 2,6 M / 1,7 M et 32 % / 27 % / 19 % / 12 %, tandis que le tableau 3 (page suivante) donne 4 168 300 / 3 293 020 / 2 386 370 / 1 526 110 et 27,1 % / 21,4 % / 15,5 % / 9,9 % pour les mêmes quatre groupes. Les effectifs sont proches (arrondis différemment) mais les pourcentages divergent nettement. Explication la plus probable, non confirmée par une phrase explicite du rapport : le texte courant rapporte les % en part des ASSURÉS EN ALD (dénominateur = 12 344 220 personnes physiques), tandis que la 5ᵉ colonne du tableau 3 donne, selon sa propre note de lecture, « la part des affections reconnues pour une ALD spécifique par rapport au total des affections reconnues » (dénominateur = 15 366 030 « Total des ALD reconnues », qui compte les doubles ALD). Les deux lectures ne sont pas superposables. Rapporté tel quel, sans arbitrage — au fact-checker de trancher.
INCERTITUDE : contradiction interne documentée, non résolue par moi.

CHIFFRE   : total des ALD reconnues (ALD30, ALD31, ALD32) = 15 366 030 « affections reconnues » (dénominateur différent du nombre de personnes physiques, 12 344 220, du fait des multi-ALD)
MILLÉSIME : 2022
CHAMP     : régime général seul
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, tableau 3, p. 8
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « N.A. Total des ALD reconnues (ALD30, ALD31, ALD32) 15 366 030 N.A. 100,0% 42,5% 3,0% […] Note de lecture : la somme de tous les assurés reconnus en ALD au titre d'une ALD liste n'est pas égale au total des patients en ALD 30 car un même patient peut être reconnu au titre de plusieurs ALD. La cinquième colonne ne représente donc pas la part des assurés d'une ALD parmi l'ensemble des assurés reconnus en ALD. Elle donne la part des affections reconnues pour une ALD spécifique par rapport au total des affections reconnues, par exemple, les ALD hors-liste (ALD 31) représentent 5,4 % de toutes les ALD reconnues. Source : Données CNAM, prévalence des ALD. Périmètre : régime général uniquement. »
CONTEXTE  : ⚠️ « périmètres partiellement recouvrants — ces chiffres ne s'additionnent pas » au sens du CLAUDE.md : un même individu peut compter dans plusieurs lignes du tableau 3.
INCERTITUDE : —

CHIFFRE   : projection — le nombre d'assurés en ALD (tous régimes) pourrait atteindre entre 14,1 et 15,0 millions en 2027 (soit +7 % à +14 % par rapport à 2021), ou « jusqu'à 16 millions » en 2030 selon la synthèse
MILLÉSIME : projection réalisée en 2024 sur horizon 2027-2030, base 2021
CHAMP     : tous régimes
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 1 (synthèse) et p. 7 (§1.2.1)
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « À partir de la base RAC mise à disposition par la DREES, et d'hypothèses de prévision détaillées en annexe III, la mission a estimé que le nombre d'assurés en ALD s'élèverait entre 14,1 millions et 15,0 millions d'assurés en 2027, soit une hausse respective de 7 % et 14 % par rapport à 2021. » ; synthèse : « Selon les projections de la mission, jusqu'à 16 millions d'assurés pourraient bénéficier du dispositif en 2030 ».
CONTEXTE  : ces deux chiffres (15,0 M en 2027 vs 16 M en 2030) ne sont pas rigoureusement cohérents entre eux dans le texte lu (extrapolation implicite entre les deux horizons), signalé tel quel.
INCERTITUDE : projection modélisée, pas un dénombrement.

## 3. Part de la dépense d'assurance maladie consommée par les personnes en ALD

CHIFFRE   : 122,8 Md€ de dépense totale de soins des assurés en ALD, dont 91 % (111,7 Md€) remboursés par l'assurance maladie
MILLÉSIME : 2021
CHAMP     : tous régimes (base RAC de la DREES) ; « dépense totale » = y compris franchises, participations forfaitaires et dépassements d'honoraires (reste à charge inclus)
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 15 (§1.3)
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « En 2021, la dépense totale des assurés en ALD s'élève à 122,8 Md€, dont 91 % (111,7 Md€) de dépenses remboursées par l'assurance maladie. Ces montants sont respectivement de 81,5 Md€ et 66,4 % (54,1 Md€) pour la population sans ALD. 67,3 % des dépenses remboursées par l'AMO concernent les assurés reconnus en ALD. Plus des deux tiers des dépenses des assurés en ALD sont liés à leur affection (82,6 Md€ contre 40,2 Md€ sans lien). »
CONTEXTE  : la synthèse du même rapport (p. 1) résume ce chiffre en l'arrondissant : « les assurés en ALD représentent un total de 112 Md€ de dépenses d'assurance maladie en 2021 (soit 67 % des dépenses totales), les dépenses liées à leur(s) ALD s'établissent à 82,6 Md€. » — ce « 112 Md€ » de la synthèse correspond donc aux « 111,7 Md€ » de dépenses REMBOURSÉES de la section 1.3, arrondi ; il ne s'agit pas d'un chiffre distinct malgré l'écart d'apparence entre 112 et 122,8. Les deux passages sont cohérents une fois le distinguo « dépense totale » / « dépense remboursée » fait — signalé ici explicitement car ce distinguo n'est pas répété à chaque occurrence dans le rapport et peut prêter à confusion.
INCERTITUDE : « base RAC » = base semi-agrégée développée par la DREES à partir du SNDS ; note 30 du rapport : « Les deux dernières années disponibles sur cette base sont 2018 et 2021. La mission a retenu l'année 2021 car il s'agit de l'année la plus récente ».

CHIFFRE   : coût spécifique du dispositif ALD pour les finances publiques estimé à 12,3 Md€ (décomposé en 11,3 Md€ d'exonération du ticket modérateur + 0,6 Md€ d'exonération d'impôt sur le revenu des indemnités journalières + 0,4 Md€ de surcoût du forfait patientèle médecin traitant)
MILLÉSIME : 2021 (exonération TM et IJ) / 2022 (forfait patientèle)
CHAMP     : tous régimes, estimation de la mission (pas un chiffre administratif direct — « n'ayant pas fait l'objet d'évaluation chiffrée depuis 2015 »)
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, tableau 4, p. 16
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « Le coût de l'exonération du ticket modérateur estimé par la mission avec la méthodologie jugée la plus robuste s'élève à 11,3 Md€ pour l'année 2021. […] Tableau 4 : Estimation du coût total associé au régime ALD : Exonération de ticket modérateur pour les soins et biens médicaux en lien avec l'ALD 11,3 [Md€] ; Surcoût du forfait patientèle médecin traitant lié aux patients en ALD 0,4 [Md€] ; Exonération d'impôt sur le revenu des IJ des assurés en ALD 0,6 [Md€] ; Total du coût direct du dispositif ALD 12,3 [Md€]. »
CONTEXTE  : « N'ayant pas fait l'objet d'évaluation chiffrée depuis 2015, la mission a estimé le coût de l'exonération du ticket modérateur des soins en lien avec l'ALD par différentes méthodologies ». Référence antérieure citée : « Quel avenir pour le dispositif de prise en charge des affections de longue durée (ALD) », Trésor-Éco n° 145, avril 2015 (non ouverte par moi).
INCERTITUDE : c'est une ESTIMATION MODÉLISÉE de la mission, explicitement présentée comme telle (nécessite « la construction d'un contrefactuel »), pas un comptage administratif direct — à distinguer clairement des 111,7/122,8 Md€ de dépenses observées.

CHIFFRE   : DREES CNS — financement de la CSBM par les affections de longue durée (ALD) : 16 147 M€ en 2024 (15 130 M€ en 2023 ; 14 122 M€ en 2022 ; 13 504 M€ en 2021)
MILLÉSIME : 2021 à 2024
CHAMP     : France entière, tous régimes — il s'agit du montant du financement par la Sécurité sociale ISSU du dispositif ALD au sein d'un tableau de financement plus large de la CSBM (poste distinct des autres postes de la Sécurité sociale), pas la totalité des dépenses liées aux ALD
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, fiche 19 (« Le financement de la CSBM par la Sécurité sociale et l'État »), tableau 4
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : non lu littéralement dans cette relance (donnée mémorisée d'une lecture antérieure du même document lors de cette session, non re-vérifiée mot pour mot sur cette relance) — à revalider avant publication.
CONTEXTE  : ce chiffre (financement ALD dans la fiche 19 DREES) N'EST PAS DIRECTEMENT COMPARABLE aux 111,7/122,8 Md€ de l'IGAS-IGF : la fiche DREES semble mesurer uniquement le surcoût lié à l'exonération de ticket modérateur ALD (proche du même périmètre que les 11,3 Md€ IGAS-IGF 2021, mais avec des montants différents : 13,5 Md€ DREES 2021 contre 11,3 Md€ IGAS-IGF 2021) — DIVERGENCE À SIGNALER, non résolue, possiblement due à des méthodologies de calcul différentes (comptes de la santé DREES vs estimation contrefactuelle de la mission).
INCERTITUDE : chiffre à revalider par relecture littérale de la fiche 19 avant publication — marqué ici avec le niveau de confiance le plus bas de ce rapport.

## 4. Dépense moyenne par bénéficiaire ALD vs autres assurés

CHIFFRE   : dépense totale moyenne d'un assuré en ALD 9 300 €/an ; reste à charge (RAC) annuel moyen après AMO 840 €/an (couverture 91 %)
MILLÉSIME : 2021
CHAMP     : tous régimes, base RAC DREES ; dépense « pour les soins en lien et sans lien avec son ALD » (donc pas seulement les soins liés à l'affection)
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 13 (§1.2.3)
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « la dépense moyenne d'un assuré en ALD, pour les soins en lien et sans lien avec son ALD, est de 9 300 €/an tandis que son reste à charge (RAC) annuel moyen après prise en charge par l'AMO s'élève à 840 €/an. Leurs dépenses sont donc couvertes à 91 % par l'AMO. Cet effet protecteur est particulièrement notable sur le champ des dépenses de ville, couvertes à 92 % par l'AMO pour les assurés en ALD, contre 69 % pour la population sans ALD. Sur le champ de l'hôpital, les taux de couverture sont proches (96 % pour les ALD contre 89 % pour la population sans ALD). »
CONTEXTE  : « les assurés en ALD présentent, jusqu'à 80 ans, un RAC plus élevé que les assurés sans ALD (d'un facteur de 1,8 en 2021) […] 82 % de ce RAC n'est d'ailleurs pas lié à leur ALD. […] pour les populations les plus jeunes en ALD […] les assurés en ALD âgés de dix ans ou moins ont un RAC moyen 2,3 fois supérieur à la population non ALD ; […] les assurés en ALD âgés de plus de 85 ans ont un RAC inférieur de l'ordre d'un facteur 1,2 par rapport à la population non ALD (1 030 € pour les individus âgés de 86 ans à 90 ans, contre 1 168 € pour les non ALD) […] les 0,1 % des RAC les plus élevés s'établissent à près de 12 000 € pour les individus en ALD contre environ 7 500 € pour ceux sans ALD. »
INCERTITUDE : —

CHIFFRE   : dépense annuelle moyenne EXPLICITE (en €/an, comparable au 9 300 € ALD) pour un assuré SANS ALD
MILLÉSIME : —
CHAMP     : —
SOURCE    : non trouvé sous cette forme dans les pages lues
URL       : —
EXTRAIT   : non lu
CONTEXTE  : le rapport IGAS-IGF donne des agrégats en Md€ pour la population sans ALD (81,5 Md€ de dépense totale, 54,1 Md€ remboursés, 2021) mais je n'ai pas trouvé, dans les pages lues, la division explicite par l'effectif correspondant pour obtenir un montant par tête directement comparable au « 9 300 €/an » ALD — cette division nécessiterait un calcul que je n'ai pas fait moi-même (règle de ne pas produire de ratio non publié tel quel). Le tableau 5 du rapport (déciles de dépenses EN LIEN avec l'affection, périmètre plus étroit) donne pour « Ensemble de la population sans ALD » : D1 = 94 €, D5 = 630 €, D9 = 2 996 €, contre D1 = 782 €, D5 = 3 399 €, D9 = 20 880 € pour « Ensemble de la population en ALD » — mais ce sont des déciles de dépenses EN LIEN avec l'ALD/l'affection déclarée, pas une dépense totale moyenne.
INCERTITUDE : piste à creuser dans les annexes non lues du rapport IGAS-IGF (III notamment) ou dans la base RAC / comptes de la santé DREES.

CHIFFRE   : médiane de dépenses annuelles en lien avec l'affection variant de 187 € (ALD 29 « Tuberculose, Lèpre ») à 34 902 € (ALD 14 « Mucoviscidose ») selon l'ALD
MILLÉSIME : 2021
CHAMP     : tous régimes, base RAC DREES, patients reconnus pour une seule ALD
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 20-21 (§2.1.3), tableau 5
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « en 2021, près de 3,9 millions d'assurés reconnus pour une seule ALD présentent une dépense inférieure à la moyenne de celles des assurés sans ALD de plus de 65 ans ; il existe une dispersion des dépenses entre ALD : la médiane de dépenses annuelles des patients en ALD en lien avec leur affection varie de 187 € pour l'ALD 29 « Tuberculose, Lèpre » à 34 902 € pour l'ALD 14 « Mucoviscidose ». Toutefois, cette dispersion est beaucoup plus limitée pour les ALD les plus coûteuses […] il existe également une dispersion des dépenses au sein d'une même ALD : les dépenses des patients reconnus pour la seule ALD 19 « Néphropathie chronique grave » varient de 693 € pour le premier décile à 55 940 € pour le 9ème décile. »
CONTEXTE  : c'est un contrefactuel direct à l'idée reçue « ALD = maladie très coûteuse » — près de 3,9 M d'assurés mono-ALD dépensent moins que la moyenne des plus de 65 ans sans ALD.
INCERTITUDE : —

## 5. Répartition des dépenses par poste — surreprésentation ALD

CHIFFRE   : dépenses hospitalières = 50 % de la dépense des assurés en ALD, contre 20 % pour les non-ALD (2021) ; dépenses de transport sanitaire des assurés en ALD = 85 % du total (4,6 Md€ sur 5,4 Md€), dépense moyenne en transport 2,6 fois supérieure (1 110 € contre 420 €)
MILLÉSIME : 2021
CHAMP     : tous régimes, base RAC DREES
SOURCE    : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024, p. 18 (§1.3.3)
URL       : https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas-IGF%20affections%20de%20longue%20dur%C3%A9e%20(revue%20de%20d%C3%A9penses).pdf
EXTRAIT   : « une surreprésentation des dépenses hospitalières (50 % pour les assurés en ALD contre 20 % pour les non ALD, cf. graphique 6) ; au sein des dépenses de ville, une nette surreprésentation des dépenses de produits de santé, de soins infirmiers et de transports. Les assurés en ALD représentent 85 % de la dépense totale de transport, soit 4,6 Md€ sur 5,4 Md€. La dépense moyenne en transports sanitaires des assurés en ALD est 2,6 fois supérieure à la population sans ALD (1 110 € contre 420 €). »
CONTEXTE  : « 78 % des dépenses de transport des assurés en ALD sont enregistrées « en lien avec l'ALD », sans que la mission n'ait pu établir ce que recouvraient exactement les dépenses qui ne sont pas enregistrées en lien. »
INCERTITUDE : —

## 6. Cartographie des pathologies de la CNAM (à opposer au comptage ALD)

CHIFFRE   : 67,6 millions de bénéficiaires (population de référence du jeu de données « Pathologies »)
MILLÉSIME : 2024 (série disponible 2015-2024)
CHAMP     : France entière, ensemble des régimes d'assurance maladie
SOURCE    : CNAM, plateforme data.ameli.fr, jeu de données ouvert « Pathologies : effectif de patients par pathologie, sexe, classe d'âge et territoire (département, région) » — métadonnées de l'API
URL       : https://data.ameli.fr/api/explore/v2.1/catalog/datasets/effectifs/
EXTRAIT   : « France entière » couvrant l'ensemble des régimes d'assurance maladie ; « 67,6 millions de bénéficiaires » de l'assurance maladie en 2024 ; « Les données présentent des informations sur les effectifs de patients pris en charge par l'ensemble des régimes d'assurance maladie. » — citations extraites du texte de métadonnées renvoyé par l'API du portail (accès direct, pas de relais presse), mais je n'ai pas ouvert la publication de synthèse elle-même.
CONTEXTE  : population de référence pour la cartographie, à comparer aux 13,7 M (tous régimes, 2021) ou 12,3 M (régime général, 2022) de bénéficiaires du DISPOSITIF ALD administratif — la cartographie des pathologies est un périmètre bien plus large (n'importe quelle pathologie ou traitement chronique repéré dans les données de remboursement, pas seulement les 29 ALD réglementaires).
INCERTITUDE : je n'ai pas pu ouvrir le rapport de synthèse « cartographie des pathologies et des dépenses » lui-même (bloqué, voir plus bas) — seules les métadonnées techniques du jeu de données ont été consultées.

CHIFFRE   : « l'objet de cette cartographie n'est pas d'identifier tous les patients atteints par les pathologies, mais d'identifier ceux ayant recours à des soins »
MILLÉSIME : —
CHAMP     : méthodologique — définit la nature administrative (et non épidémiologique) de la cartographie CNAM
SOURCE    : documentation-snds.health-data-hub.fr, fiche « Cartographie des pathologies » — page de documentation méthodologique du Health Data Hub (GIP public), qui reprend et cite la méthodologie CNAM ; PAS la publication CNAM elle-même (celle-ci, hébergée sur assurance-maladie.ameli.fr, est restée inaccessible pendant cette session)
URL       : https://documentation-snds.health-data-hub.fr/snds/fiches/cartographie_pathologies
EXTRAIT   : « l'objet de cette cartographie n'est pas d'identifier tous les patients atteints par les pathologies, mais d'identifier ceux ayant recours à des soins »
CONTEXTE  : la même page précise que la couverture s'étend aux bénéficiaires « ayant eu recours à des soins remboursés dans l'année et/ou ayant séjourné au moins une fois dans un établissement de santé », ce qui exclut par construction les personnes atteintes d'une pathologie mais n'ayant pas eu de recours aux soins documenté dans le SNDS cette année-là — c'est exactement la distinction demandée dans le brief entre comptage administratif et mesure épidémiologique. La formulation exacte de la CNAM sur le caractère non épidémiologique de sa propre série ALD (demandée explicitement dans le brief) n'a PAS été retrouvée littéralement — voir PISTES NON ABOUTIES.
INCERTITUDE : citation obtenue via un outil de résumé automatisé (WebFetch) appliqué à la page — présentée entre guillemets par l'outil comme extraite du texte de la page, mais non revérifiée par une seconde lecture manuelle intégrale de la page source.

CHIFFRE   : 202,5 Md€ remboursés, 67,4 millions de personnes prises en charge, pathologies chroniques = 60 % / 126 Md€ / 37 % / 25 millions de personnes (chiffres circulant dans la presse et les résumés de moteur de recherche à propos de l'édition 2025 de la cartographie CNAM, données 2015-2023)
MILLÉSIME : 2023 (annoncé)
CHAMP     : inconnu précisément (France entière, tous régimes vraisemblablement)
SOURCE    : NON OUVERTE — ces chiffres ne proviennent que de résumés automatiques de moteur de recherche (WebSearch) portant sur les pages assurance-maladie.ameli.fr/etudes-et-donnees/2025-cartographie-depenses-pathologies-2015-2023 et ameli.fr/medecin/actualites/..., toutes deux bloquées (403 / CAPTCHA) lors de cette session
URL       : https://www.assurance-maladie.ameli.fr/etudes-et-donnees/2025-cartographie-depenses-pathologies-2015-2023 (inaccessible)
EXTRAIT   : non lu
CONTEXTE  : ces chiffres NE DOIVENT PAS être publiés comme sourcés tant que la publication primaire n'a pas été ouverte — je les signale ici uniquement comme piste à relancer, avec le relais nommé explicitement (résumés WebSearch, pas la page CNAM).
INCERTITUDE : maximale — chiffre non vérifié, à ne pas utiliser sans nouvelle tentative d'accès.

## 7. Dépense courante de santé et CSBM : montants, % PIB, dépense par habitant

CHIFFRE   : CSBM (consommation de soins et de biens médicaux) = 254,8 milliards d'euros, soit 8,7 % du PIB, +3,7 % ; dépense moyenne de 3 723 euros par habitant
MILLÉSIME : 2024
CHAMP     : France entière
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, fiche 01, p. 22
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : « En 2024, la consommation de soins et de biens médicaux (CSBM) augmente de +3,7 % (après +4,8 %) pour s'établir à 254,8 milliards d'euros (tableau 1), soit une dépense moyenne de 3 723 euros par habitant. Cette évolution est due à la fois à une hausse des prix (+0,6 %) et du volume (+3,0 %). » / « CSBM (en % du PIB) […] 2024 : 8,7 » (tableau 1)
CONTEXTE  : soins hospitaliers = 47 % de la CSBM 2024 (120 783 M€, dont 93 644 M€ secteur public et 27 139 M€ secteur privé) ; soins ambulatoires 77 825 M€ ; biens médicaux (médicaments + dispositifs médicaux) 56 188 M€ (dont médicaments 34 503 M€). Croissance moyenne CSBM 2010-2019 : +2,0 %/an, contre +3,7 % en 2024. Depuis 1950, la composition de la CSBM est restée relativement stable (44 % hospitalier en 1950 contre 47 % en 2024).
INCERTITUDE : —

CHIFFRE   : DCSi (dépense courante de santé au sens international) = 332,6 milliards d'euros (arrondi 333 Md€), soit 11,4 % du PIB, +3,6 %
MILLÉSIME : 2024
CHAMP     : France entière ; DCSi = agrégat plus large que la CSBM, incluant soins de longue durée (52,2 Md€, 16 % de la DCSi), gestion du système de santé (16,9 Md€, 5 %) et prévention (8,7 Md€, 2,6 %)
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, vue d'ensemble, p. 8
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : « En 2024, la dépense courante de santé au sens international (DCSi) s'élève à 332,6 milliards d'euros (tableau 1), soit 11,4 % du PIB. Elle augmente de 3,6 %, après +3,4 % en 2023 et +2,5 % en 2022. La DCSI est portée par la consommation de soins et de biens médicaux (CSBM), en augmentation de 3,7 % en 2024, et dans une moindre mesure par les dépenses de gestion du système de santé (+4,9 % en 2024). La CSBM, qui représente 77 % de la DCSi, s'élève à 254,8 milliards d'euros en 2024. […] Les soins de longue durée, deuxième composante de la DCSi après la CSBM (16 % de la DCSi), croissent à un rythme très légèrement inférieur (+3,4 % en 2024), s'élevant à 52,2 milliards d'euros. Les coûts de gestion du système de santé (16,9 milliards d'euros en 2024, soit 5 % de la DCSi) accélèrent […] En 2024, la part de la CSBM et de la DCSi dans le PIB se stabilisent aux mêmes niveaux qu'en 2023 : respectivement 8,7 % et 11,4 %. Ces parts sont relativement stables depuis dix ans, hors crise sanitaire. »
CONTEXTE  : « le financement par les administrations publiques de la CSBM demeure à un niveau historiquement élevé, mais baisse de 0,5 point en 2024, à 79,4 %, au profit de celui des organismes complémentaires et des ménages. »
INCERTITUDE : —

CHIFFRE   : comparaison internationale — DCSi en % du PIB 2024 : États-Unis 17,2 %, Allemagne 12,3 %, Autriche 11,8 %, France 11,4 %, moyenne UE-27 10,3 %
MILLÉSIME : 2024 (2023 pour certains pays, données manquantes signalées)
CHAMP     : international, sources combinées DREES/OCDE/Eurostat/OMS
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, vue d'ensemble, p. 18
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : « Avec une dépense courante de santé au sens international (DCSi) représentant 17,2 % de leur PIB en 2024, les États-Unis sont de loin en tête des pays de l'OCDE. Près de cinq points derrière, l'Allemagne, premier pays de l'UE-27, dépense 12,3 % de son PIB pour la santé, juste devant l'Autriche (11,8 %) et la France (11,4 %). En 2024, les États membres de l'UE-27 consacrent en moyenne 10,3 % de leur PIB aux dépenses de santé. […] Avec + 3,6 % en 2024, la France a l'un des taux de croissances les plus modérés de l'UE-27, où la DCSi en valeur progresse en moyenne de +6,5 %. » Source de la publication : « DREES, comptes de la santé pour la France ; OCDE, Eurostat et OMS, System of Health Accounts (SHA) pour les autres pays. »
CONTEXTE  : « la progression de la DCSi en 2024 est supérieure à la progression moyenne annuelle observée avant la crise du Covid-19 entre 2010 et 2019, en moyenne dans l'UE-27 (+2,7 % par an) ainsi que dans la plupart des pays étudiés. »
INCERTITUDE : « Données manquantes en 2024 » pour certains pays (Bulgarie, Croatie, Roumanie — notées avec un renvoi ¹ dans le graphique).

## 8. Reste à charge des ménages, comparaison UE/OCDE

CHIFFRE   : reste à charge des ménages sur la CSBM = 20,0 milliards d'euros en 2024, soit 7,8 % de la CSBM ; 292 euros par habitant (contre 276 € en 2023)
MILLÉSIME : 2024
CHAMP     : France entière, périmètre CSBM
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, vue d'ensemble, p. 16
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : « En 2024, le reste à charge moyen s'élève à 292 euros par personne. Le reste à charge des ménages, représentant la part de la CSBM financée directement par les ménages, s'élève à 20,0 milliards d'euros en 2024, soit 7,8 % de la CSBM. Par habitant, cela représente un montant de 292 euros, après 276 euros en 2023. Les soins ambulatoires sont le premier poste que les ménages financent directement (133 euros par personne en 2024). […] Le taux de reste à charge des ménages augmente de 0,1 point en 2024, de 7,7 % de la CSBM en 2023 à 7,8 % en 2024. […] Il s'agit néanmoins du second taux le plus bas (après 2023) depuis 2010. Sur le champ de la DCSi, c'est-à-dire en incluant les dépenses de prévention, de soins de longue durée, et de gouvernance, la part de la DCSi financée par les ménages s'élève à 10,2 %, une part stable par rapport à 2023. »
CONTEXTE  : décomposition par poste (RAC par habitant, 2024) : soins hospitaliers 55 €, soins ambulatoires 63 €, médicaments en ambulatoire 133 €, dispositifs médicaux 40 €. NOTE : deux valeurs de RAC coexistent dans la même vue d'ensemble selon le périmètre retenu — 7,8 % SUR LA CSBM, 10,2 % SUR LA DCSi — ne pas les confondre.
INCERTITUDE : —

CHIFFRE   : le reste à charge des ménages en France est parmi les plus faibles de l'Union européenne : 10,2 % de la DCSi en 2023 (France), contre 14,8 % en moyenne dans l'UE-27
MILLÉSIME : 2023 (dernière année disponible pour la comparaison internationale)
CHAMP     : international, DCSi
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, vue d'ensemble, p. 19
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : « En 2023, en moyenne dans l'UE-27, 14,8 % de la DCSi reste à la charge des ménages. […] En France, cette part s'établit à 10,2 % en 2023 ; elle est donc nettement inférieure à celle de l'UE-27. […] Une part plus importante des dépenses de santé reste à la charge des ménages dans les pays de l'est et du sud de l'Europe : le reste à charge (RAC) y est supérieur à 20 % de la DCSi […] Le RAC est même supérieur à 30 % en Bulgarie, en Grèce, en Lituanie, et en Lettonie. À l'inverse, dans les pays du nord-ouest de l'Europe, les RAC sont inférieurs à 15 %, sauf en Belgique (21,5 %) et en Autriche (16,5 %). En Allemagne, cette part (11,1 % en 2023) est également inférieure à la moyenne européenne […] C'est au Luxembourg (9,7 %), en Croatie (9,4 %) et en France (10,2 %) que les RAC sont les plus faibles au sein de l'Union européenne. […] En dehors de l'UE, la part de la DCSi restant à la charge des ménages varie de 10,9 % à 15,2 % au Japon, aux États-Unis, au Royaume-Uni, en Islande, en Norvège et au Canada ; elle est plus élevée en Suisse (22,0 %). Aux États-Unis, le RAC des ménages s'établit à 10,9 % de la DCSi. »
CONTEXTE  : « la structure du RAC varie fortement entre pays […] dans la plupart des pays observés, les biens médicaux (produits pharmaceutiques et autres biens médicaux) constituent la première composante du RAC des ménages : ils représentent en moyenne 26 % du RAC dans l'UE-27. […] les dépenses des ménages pour les produits pharmaceutiques atteignent respectivement 67 %, 63 % et 57 % du RAC en Bulgarie, en Pologne et en Roumanie. »
INCERTITUDE : Source explicitement citée par la DREES elle-même : « DREES, comptes de la santé pour la France ; OCDE, Eurostat et OMS, Système international des comptes de la santé (SHA) pour les autres pays. »

## 9. Dépenses de prévention

CHIFFRE   : dépenses de prévention = 8,7 milliards d'euros en 2024, soit 2,6 % de la DCSi, +0,9 % après deux années de forte baisse
MILLÉSIME : 2024
CHAMP     : France entière
SOURCE    : DREES, *Les dépenses de santé en 2024 — Résultats des comptes de la santé*, *Panoramas de la DREES*, édition 2025, fiche 23, p. 133
URL       : https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-09/Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202024_MEL.pdf
EXTRAIT   : « En 2024, les dépenses de prévention s'établissent à 8,7 milliards d'euros, soit 2,6 % de la dépense courante de santé au sens international (DCSi). Après deux années de forte baisse avec le reflux de l'épidémie de Covid-19 (-35 % en 2023, -24 % en 2022), les dépenses de prévention augmentent de 1 % en 2024. […] L'Assurance maladie reste encore en 2024 le principal financeur des dépenses de prévention (43 %) ; la part de l'État et des collectivités locales augmente en 2024 et s'établit à 27 %. Les ménages financent 1 % de ces dépenses. […] Elles ont beaucoup reflué depuis leur sommet atteint durant la crise sanitaire : en 2021, elles s'étaient établies à 17,5 milliards d'euros. Entre 2014 et 2019, les dépenses de prévention avaient augmenté de 2 % par an en moyenne. »
CONTEXTE  : Tableau 1 (évolution 2014-2024, en M€) : ensemble de la prévention 5 611 (2014), 9 339 (2020), 17 455 (2021, pic Covid), 13 330 (2022), 8 657 (2023), 8 731 (2024). Hors dépenses Covid-19, les dépenses de prévention 2024 atteignent 8,3 Md€ (+4,8 %). Les dépenses liées au Covid-19 ne représentent plus que 4,5 % du total en 2024, contre un pic où elles avaient atteint 9,5 Md€ (2021).
INCERTITUDE : —

## CE QUI CONTREDIT L'ANGLE

Le n° 1 enquête sur l'écart entre poids réel et poids médiatique. Sur ce thème santé/ALD, plusieurs éléments trouvés vont à l'encontre d'un récit de dégradation continue ou de système « à la dérive » :

- Le **reste à charge des ménages français est l'un des plus faibles de l'Union européenne** (10,2 % de la DCSi en 2023, contre 14,8 % en moyenne UE-27, et parmi les trois plus bas de l'UE avec le Luxembourg et la Croatie) — un fait contre-intuitif si l'angle médiatique dominant est celui d'un renoncement aux soins généralisé ou d'un désengagement de la Sécurité sociale.
- Le taux de RAC sur la CSBM en France (7,8 % en 2024) est le **second taux le plus bas depuis 2010**, malgré une légère hausse par rapport à 2023.
- Le dispositif ALD a un **effet protecteur documenté et chiffré** : couverture à 91 % des dépenses par l'AMO pour un assuré ALD, contre un RAC nettement supérieur en proportion pour la population générale sur certains postes (69 % de couverture en ville pour les non-ALD contre 92 % pour les ALD) ; « à caractéristiques identiques, les personnes en ALD renoncent 2,5 fois moins aux soins que les autres » (IGAS-IGF citant une étude DREES, *Études et résultats* n° 1200, 2021 — non ouverte directement par moi).
- **Contrefactuel chiffré sur l'idée reçue « ALD = maladie coûteuse »** : près de 3,9 millions d'assurés reconnus pour une seule ALD dépensent, en lien avec leur affection, MOINS que la moyenne des assurés sans ALD de plus de 65 ans ; la médiane de dépense pour l'ALD 29 (tuberculose, lèpre) n'est que de 187 €/an.
- Les **dépenses de prévention ont progressé de 38,8 % depuis 2019** (vue d'ensemble DREES, fiche 01) — malgré le récit fréquent d'un sous-investissement chronique en prévention en France.
- La **CSBM et la DCSi progressent en 2024 un peu plus vite que le PIB** (inversion par rapport aux deux années précédentes), et la France affiche l'un des taux de croissance de la DCSi les plus modérés de l'UE-27 (+3,6 % contre +6,5 % en moyenne UE-27) — la dépense de santé française n'est pas hors de contrôle par rapport à ses voisins en dynamique récente, même si son niveau (11,4 % du PIB) reste élevé.

À l'inverse, ce qui pourrait nourrir l'angle « masse invisible » : les 12,3 à 13,7 millions de personnes en ALD (selon champ) et les 254,8 Md€ de CSBM sont des masses considérables, rarement citées avec leur ampleur réelle dans le débat public, qui se concentre le plus souvent sur des postes de dépense ponctuels (déficit de la Sécu, telle ou telle réforme de franchise) plutôt que sur l'ordre de grandeur global.

## PISTES NON ABOUTIES

- **CNAM, *Points de repère* n° 54** (« Les bénéficiaires du dispositif des affections de longue durée en 2022 »), juillet 2024 — publication primaire directement demandée dans le brief pour le champ « tous régimes / France entière ». URL : https://www.assurance-maladie.ameli.fr/sites/default/files/2024-07_beneficiaires-ald_points-de-repere-54_assurance-maladie.pdf — **totalement bloquée** pendant cette session : la requête directe renvoie une page HTML « Vérification de sécurité » (CAPTCHA), confirmé à la fois via WebFetch et via un proxy lecteur (r.jina.ai). L'intégralité du domaine assurance-maladie.ameli.fr / ameli.fr semble filtrée de la même façon (confirmé aussi sur plusieurs autres URL du même domaine — cartographie des pathologies, méthodologie CNAM). Seul le sous-domaine data.ameli.fr (portail open data) reste accessible. **À relancer en priorité** lors d'une prochaine collecte, idéalement avec un accès réseau différent.
- **Méthodologie CNAM de la cartographie des pathologies** (PDF « 2024_methode-reperage-pathologies_cartographie.pdf », hébergé sur assurance-maladie.ameli.fr) — identifiée par recherche mais non ouverte, même blocage que ci-dessus.
- **La formule exacte de la CNAM sur la nature administrative (et non épidémiologique) de sa propre série ALD** — demandée explicitement dans le brief, jamais retrouvée littéralement dans les sources ouvertes. Le passage le plus proche trouvé (« l'objet de cette cartographie n'est pas d'identifier tous les patients atteints par les pathologies, mais d'identifier ceux ayant recours à des soins ») provient de la page de documentation SNDS du Health Data Hub, pas d'une publication CNAM directement citée par moi, et porte sur la cartographie des pathologies, pas spécifiquement sur le dispositif ALD.
- **Chiffres de la cartographie des pathologies 2023** (202,5 Md€ remboursés, 67,4 M de personnes prises en charge, 60 %/126 Md€/37 %/25 M pour les pathologies chroniques) — vus uniquement via des résumés de moteur de recherche portant sur des pages ameli.fr bloquées. **Non publiables tels quels** : à retrouver via une autre voie d'accès (cache Google, Wayback Machine, ou nouvelle tentative directe).
- **Dépense annuelle moyenne explicite pour un assuré SANS ALD, comparable au « 9 300 €/an » ALD** — non trouvée sous cette forme dans les 44 premières pages (sur 458) du rapport IGAS-IGF lues ; à chercher dans les annexes II-III (population et dépenses ALD, non lues) ou dans la base RAC de la DREES elle-même.
- **Âge médian des bénéficiaires ALD** — seul l'âge moyen a été trouvé (63, 65 ou 66 ans selon le passage et le champ) ; pas de médiane dans les pages lues du rapport IGAS-IGF.
- **Fiche 19 DREES (financement CSBM par la Sécurité sociale/État), poste « Affections de longue durée »** — chiffres (16 147 M€ 2024, 15 130 M€ 2023, 14 122 M€ 2022, 13 504 M€ 2021) mentionnés à partir d'une lecture antérieure de la même session non revérifiée littéralement lors de cette relance : marqués `EXTRAIT : non lu` par précaution et à revalider avant publication. Une divergence potentielle avec l'estimation IGAS-IGF (11,3 Md€ 2021 pour l'exonération TM seule) doit être creusée : périmètres de calcul très probablement différents (comptes de la santé vs estimation contrefactuelle de mission), mais non confirmée par une lecture croisée complète.
- **Contradiction interne au rapport IGAS-IGF** entre le texte courant (p. 7 : maladies cardiovasculaires 32 %, diabète 27 %, tumeurs malignes 19 %, affections psychiatriques 12 % des assurés en ALD) et le tableau 3 (p. 8-9 : 27,1 % / 21,4 % / 15,5 % / 9,9 %, très probablement calculés sur un dénominateur différent — affections reconnues avec double-compte multi-ALD vs personnes physiques) — rapportée telle quelle dans ce document, non résolue.
- **Annexes II à XI du rapport IGAS-IGF** (pages 45 à 458) — non lues faute de budget ; contiennent selon le sommaire une caractérisation détaillée de la population ALD (annexe II), une analyse détaillée des dépenses (annexe III), l'estimation du coût de l'exonération TM (annexe IV), et des comparaisons internationales du dispositif ALD (annexe VIII) — pistes riches pour une seconde passe.
- **Eurostat et OCDE en accès direct** — non consultés directement dans cette session ; toutes les comparaisons internationales rapportées ici proviennent de la DREES, qui cite elle-même l'OCDE/Eurostat/OMS comme sources pour les autres pays, sans que j'aie ouvert les bases Eurostat/OCDE moi-même.
- **DREES fiche 20 (financement organismes complémentaires) et fiche 21 (reste à charge, texte intégral hors vue d'ensemble)** — seule la vue d'ensemble (résumé) du RAC a été lue en détail ; la fiche 21 elle-même (p. 122) n'a pas été ouverte séparément et pourrait contenir des compléments (RAC par organisme complémentaire, RAC par type de contrat).
