# Collecte — n° 2, passe profonde — rubriques « Ce que l'on mesure du marché » et « Les grandeurs manquantes »

Sept publications ouvertes (borne haute du brief : cinq à sept). Répartition : 5 pour la rubrique marché
(INSEE, OFDT × 2, AGRASC, DGDDI), 2 pour les grandeurs manquantes en propre (Sénat, CAE) — mais l'INSEE
et le CAE fournissent chacun une pièce utile à la rubrique 9, donc le compte réel de « pièces utiles aux
grandeurs manquantes » est de 3 (INSEE, Sénat, CAE). Deux publications ont dû être lues via un lecteur
intermédiaire (r.jina.ai) après échec technique répété (HTTP 503) de l'outil de récupération standard sur
`agrasc.gouv.fr` et sur le PDF volumineux du Sénat — signalé fiche par fiche, avec la réserve méthodologique
que cela implique.

---

## A. Ce que l'on mesure du marché

### A.1 — Estimation officielle INSEE (comptes nationaux)

```
CHIFFRE   : impact sur le PIB de la prise en compte du trafic de stupéfiants : 2,7 Md€ (consommation de
            drogue 3,1 Md€, moins 0,4 Md€ d'importations)
MILLÉSIME : 2014 (donnée publiée pour cette année ; méthode « vieillie » chaque année depuis à partir
            d'une veille documentaire, mais aucun montant postérieur à 2014 n'est donné dans la note elle-même)
PUBLIÉ EN : mai 2018
NATURE    : estimation modélisée
CHAMP     : France entière, comptes nationaux (intégration en base 2014, harmonisation SEC 2010) ;
            cannabis, cocaïne, héroïne, ecstasy/MDMA, amphétamines
SOURCE    : INSEE, note méthodologique « La prise en compte des stupéfiants dans les comptes nationaux en
            base 2014 », mai 2018
URL       : https://www.insee.fr/fr/metadonnees/source/fichier/Stup%C3%A9fiants_base_2014.pdf
EXTRAIT   : « L'impact sur le PIB de la prise en compte du trafic de stupéfiant correspond au total de la
            consommation de drogue (3,1 Md€) minoré des importations (0,4 Md€), soit 2,7 Md€ pour l'année
            2014. »
CONTEXTE  : la méthode part d'un rapport tiers — INHESJ/Mildeca, « L'argent de la drogue en France »,
            2016 — qui donne les montants de consommation 2010 par produit : cannabis 1 117 M€, cocaïne
            902 M€, héroïne 267 M€, ecstasy/MDMA 42 M€, amphétamines 13 M€ (total ~2,3 Md€ en 2010).
            Ces montants sont ensuite « vieillis » jusqu'en 2014 en tenant compte de l'évolution des
            quantités consommées (données OFDT), de la teneur des produits et des prix. Méthode
            « demand-based » : prévalences déclaratives (enquêtes INPES), prix médians constatés (OCRTIS,
            OFDT).
INCERTITUDE : la note cite littéralement l'INHESJ/Mildeca : « l'observation des marchés souterrains n'étant
            que partielle, l'évaluateur utilise différentes hypothèses conduisant à des estimations dont
            l'intervalle de confiance peut être important. » Elle ajoute que l'estimation de prévalence
            « repose sur des enquêtes déclaratives auprès des ménages de l'INPES, or le caractère illicite
            de ce type de consommation peut pousser les répondants à sous-déclarer ou éviter de répondre
            à ces questions ». — Correction à la passe large : le rapport 02-marche.md attribuait au « chef
            du département des comptes nationaux de l'INSEE » une citation qualifiant le chiffre
            d'« évaluation » avec un « risque de sous-estimation », relayée par Europe1. Cette phrase
            n'apparaît **pas** dans le texte de la note INSEE elle-même (lue intégralement, 5 pages) : elle
            vient vraisemblablement d'un entretien de presse distinct de la publication. Le motif « risque
            de sous-estimation » documenté ci-dessus est donc paraphrasé depuis la note, pas cité
            littéralement comme provenant de ce passage précis — la note ne contient pas cette expression
            exacte.
```

### A.2 — L'emploi lié au trafic de stupéfiants selon la même note INSEE

```
CHIFFRE   : environ 1 000 personnes physiques dont le trafic de drogue est l'activité principale (0,004 %
            de l'emploi intérieur) ; près de 21 000 emplois en équivalents temps plein — ETP (0,08 % du
            total ETP) ; un peu plus de 30 millions d'heures travaillées (0,07 % du total)
MILLÉSIME : 2014
PUBLIÉ EN : mai 2018
NATURE    : estimation modélisée
CHAMP     : France entière, emploi lié au trafic de stupéfiants intégré aux comptes nationaux (construit à
            partir des marges de commerce estimées et des salaires/profits déclarés dans le rapport
            INHESJ/Mildeca 2016)
SOURCE    : INSEE, note méthodologique « La prise en compte des stupéfiants dans les comptes nationaux en
            base 2014 », mai 2018
URL       : https://www.insee.fr/fr/metadonnees/source/fichier/Stup%C3%A9fiants_base_2014.pdf
EXTRAIT   : « En personnes physiques, ne sont comptabilisés que les trafiquants dont le trafic de drogue
            est l'activité principale. […] le nombre de personnes physiques rajoutées dans les comptes est
            réduit, de l'ordre de 1 000 personnes physiques soit environ 0,004 % du total de l'emploi
            intérieur. » / « Le nombre d'ETP est ensuite calculé en rapportant le total des marges de
            commerce aux salaires unitaires, ce qui donne près de 21 000 ETP, soit 0,08 % du total d'ETP en
            2014. » / « Les heures travaillées par les trafiquants […] sont estimées in fine à un peu plus
            de 30 millions d'heures, soit environ 0,07 % du total d'heures travaillées en 2014. »
CONTEXTE  : cette fiche répond directement à la question « existe-t-il une estimation publique du nombre
            de personnes vivant du trafic ? » posée en rubrique grandeurs manquantes ci-dessous (section
            B.2) — voir la comparaison avec une seconde estimation, très différente, trouvée dans une autre
            publication publique (CAE).
INCERTITUDE : dérivée d'un rapport tiers non ouvert par moi (INHESJ/Mildeca 2016, voir B.2).
```

### A.3 — Estimation concurrente OFDT (Ben Lakhdar & Massin) — à rattacher à la fiche INSEE

```
CHIFFRE   : chiffre d'affaires du marché français des principales drogues illicites estimé à 6,8 Md€ en
            moyenne en 2023 (fourchette 3,8-9,7 Md€)
MILLÉSIME : 2023
PUBLIÉ EN : décembre 2025
NATURE    : estimation modélisée
CHAMP     : France métropolitaine ; cannabis + cocaïne + crack + héroïne + ecstasy/MDMA + amphétamines ;
            méthode bottom-up basée sur la demande (enquêtes EROPP 2023 et ESCAPAD 2022 de l'OFDT)
SOURCE    : Ben Lakhdar C., Massin S., « Taille des marchés des drogues illicites en France (2010-2023) »,
            OFDT, coll. Notes de méthode, décembre 2025
URL       : https://www.ofdt.fr/sites/ofdt/files/2025-12/note-marches-stupefiants-2025_0.pdf
EXTRAIT   : « En 2023, le marché français des drogues illicites est estimé à 6,8 milliards (Mds) d'euros en
            moyenne, soit plus du triple par rapport à 2010. » / « Après sommation des chiffres d'affaires
            de chaque produit, le chiffre d'affaires du marché français des principales drogues illicites
            est estimé entre 3,8 et 9,7 milliards d'euros pour une valeur centrale de 6,8 milliards d'euros
            en 2023. »
CONTEXTE  : décomposition par produit, valeur centrale 2023 : cannabis 2 734,9 M€ ; cocaïne 3 109,4 M€ ;
            crack 311,1 M€ ; héroïne 231,9 M€ ; ecstasy/MDMA 312,5 M€ ; amphétamines 73,0 M€. Évolution du
            total 2010→2023 : de 2 341,3 M€ à 6 772,8 M€ (valeurs centrales), soit +189,3 %. Pour la
            première fois en 2023, le marché de la cocaïne dépasse en valeur celui du cannabis (47 tonnes
            contre 397 tonnes en volume). — **Cette estimation n'est pas comparée explicitement à celle de
            l'INSEE dans le texte lu** : aucun passage de la note ne mentionne les comptes nationaux ou la
            note INSEE base 2014. Les deux chiffrages portent sur des millésimes très différents (2014 pour
            l'INSEE, 2023 ici) et selon des méthodes proches mais pas identiques (l'INSEE s'appuie sur le
            rapport INHESJ/Mildeca 2010-2014 « vieilli » ; l'étude OFDT reconstruit une équation de demande
            propre, actualisée par enquête). L'écart d'ordre de grandeur (2,7 Md€ en 2014 contre 6,8 Md€ en
            2023, soit ×2,5) n'est pas expliqué par le seul effet millésime au vu des taux de croissance
            documentés (+189 % entre 2010 et 2023 selon cette note) — periodes et méthodes distinctes,
            à ne pas réconcilier soi-même.
INCERTITUDE : la note le dit explicitement : « ces estimations reposent sur des hypothèses fortes
            concernant les fréquences d'usage, les quantités consommées ou encore l'impact des traitements
            médicamenteux […]. Les résultats doivent donc être lus comme des tendances indicatives,
            soulignant la nécessité de renforcer la collecte de données. » Méthode bottom-up qualifiée par
            les auteurs de « la plus robuste méthodologiquement » parmi les approches disponibles, mais
            fondée sur des hypothèses de grammage par prise (ex. 0,11 à 0,3 g par joint) pouvant faire
            varier les estimations « du simple au triple ».
```

### A.4 — Cannabis : saisies 2024 (OFDT, L'offre de stupéfiants en France en 2024)

```
CHIFFRE   : 101 tonnes de cannabis saisies en 2024, soit −19 % par rapport à 2023 (résine : 64,7 t, −26 % ;
            herbe : 36,3 t, −4 %)
MILLÉSIME : 2024
PUBLIÉ EN : février 2026
NATURE    : enregistrement administratif
CHAMP     : France entière, saisies agrégeant douanes, gendarmerie et police (source OCRTIS/OFAST)
SOURCE    : Salhi Y., « L'offre de stupéfiants en France en 2024 », OFDT, coll. Notes de bilan, février 2026
URL       : https://www.ofdt.fr/sites/ofdt/files/2026-02/note-offre-stupefiants-2024.pdf
EXTRAIT   : « L'année 2024 a été marquée par une baisse des saisies de cannabis en France, avec au total
            101 tonnes saisies, soit − 19 % par rapport à 2023, une année qui avait elle aussi connu une
            diminution, quoique moins marquée, de ces saisies. »
CONTEXTE  : deuxième année consécutive de baisse. Teneur moyenne en THC de la résine : 29,6 % en 2024
            contre 15,9 % en 2012 (+86 % en douze ans) ; teneur de l'herbe stable à 14,3 % (14,1 % en 2023).
INCERTITUDE : registre à noter — l'OFDT rappelle ailleurs dans la même note, à propos d'un autre
            indicateur (mises en cause), que « les évolutions observées […] ne traduisent pas les
            dynamiques réelles de trafic ou de consommation, mais reflètent avant tout l'activité des
            forces de l'ordre en matière de contrôle et de répression » — la même réserve vaut par
            construction pour les séries de saisies.
```

### A.5 — Cocaïne : saisies 2024, record (OFDT, même note)

```
CHIFFRE   : 53,5 tonnes de cocaïne saisies en 2024, +130 % par rapport à 2023 — total record
MILLÉSIME : 2024
PUBLIÉ EN : février 2026
NATURE    : enregistrement administratif
CHAMP     : France entière, saisies tous services confondus (douanes, gendarmerie, police), agrégées par
            l'OFAST
SOURCE    : Salhi Y., « L'offre de stupéfiants en France en 2024 », OFDT, coll. Notes de bilan, février 2026
URL       : https://www.ofdt.fr/sites/ofdt/files/2026-02/note-offre-stupefiants-2024.pdf
EXTRAIT   : « En 2024, les saisies de cocaïne en France ont atteint un total record de 53,5 tonnes,
            marquant ainsi une augmentation de + 130 % par rapport à 2023. »
CONTEXTE  : teneur moyenne des saisies : 74,3 % en 2024 contre 52,6 % en 2014 (+41 % en dix ans). Le port du
            Havre est redevenu une porte d'entrée majeure (14,4 t saisies en 2024 contre 5,3 t en 2023).
INCERTITUDE : —
```

### A.6 — Cocaïne : deux indicateurs de prix distincts (pas une divergence)

```
CHIFFRE   : prix de détail COURANT du gramme de cocaïne (chlorhydrate) : 58 € en 2024 contre 66 € en 2023
            (−12 %) ; prix de détail AJUSTÉ DE LA TENEUR (cocaïne « pure ») : 123 € en 2014 contre 77 € en
            2024 (−37 %) ; le même prix « pur », ajusté en plus de l'inflation (base 2012), passe de 64 € en
            2014 à 46 € en 2024 (−28 %)
MILLÉSIME : 2014 à 2024 (série)
PUBLIÉ EN : février 2026
NATURE    : estimation modélisée
CHAMP     : France entière ; le prix courant est celui relevé par l'OFAST (questionnaire annuel aux
            services) ; le prix ajusté de la teneur combine ce relevé et la teneur moyenne mesurée par le
            SNPS (police scientifique)
SOURCE    : Salhi Y., « L'offre de stupéfiants en France en 2024 », OFDT, coll. Notes de bilan, février 2026
URL       : https://www.ofdt.fr/sites/ofdt/files/2026-02/note-offre-stupefiants-2024.pdf
EXTRAIT   : « le prix moyen estimé du gramme de chlorhydrate de cocaïne connaît une baisse inédite de 12 %
            en 2024 atteignant 58 €, contre 66 € en 2023 » / « En 2014, le prix du gramme de cocaïne « pure »
            était de 123 €, contre 77 € en 2024, soit une diminution de 37 % en dix ans. De plus, en tenant
            compte de l'inflation en France depuis 2012, le prix réel ajusté à l'inflation montre une baisse
            de 28 %, passant de 64 € en 2014 à 46 € en 2024. »
CONTEXTE  : c'est précisément le piège de tableau signalé par le triage : le prix courant et le prix ajusté
            de la teneur en principe actif sont deux indicateurs différents, à ne jamais mettre dans le même
            tableau. Table complète OFDT 2022-2024 (prix courant) : 65 €/g (2022), 66 €/g (2023), 58 €/g
            (2024) ; moyenne annuelle 2014-2024 : 65,41 €/g.
INCERTITUDE : —
```

### A.7 — Cannabis : deux indicateurs de prix, résine et herbe

```
CHIFFRE   : résine — prix courant : 6 €/g (2012) → ~8 €/g (depuis 2019, stable) ; prix ajusté de la teneur
            (THC pur) : 38 €/g (2012) → 27 €/g (2024), −28 % ; prix ajusté de l'inflation : 6 €/g (2012) →
            6,38 €/g (2024). Herbe — prix courant : 8 €/g (2012) → ~10 €/g (depuis 2017, stable) ; prix
            ajusté de la teneur : 73 €/g (2012) → 70 €/g (2024) ; prix ajusté de l'inflation : 8 €/g (2012)
            → 7,97 €/g (2024)
MILLÉSIME : 2012 à 2024 (série)
PUBLIÉ EN : février 2026
NATURE    : estimation modélisée
CHAMP     : France entière, prix de détail de la résine et de l'herbe de cannabis (OFAST/TREND)
SOURCE    : Salhi Y., « L'offre de stupéfiants en France en 2024 », OFDT, coll. Notes de bilan, février 2026
URL       : https://www.ofdt.fr/sites/ofdt/files/2026-02/note-offre-stupefiants-2024.pdf
EXTRAIT   : « Le prix moyen de détail de la résine a connu une hausse, passant de 6 € par gramme en 2012 à
            environ 8 € à partir de 2019. Toutefois, cette évolution doit être relativisée en prenant en
            compte les variations de la teneur en THC du produit. En effet, le prix du gramme de THC « pur »
            a diminué d'environ 28 % sur la période, passant de 38 € en 2012 à 27 € en 2024. De plus, en
            tenant compte de l'inflation en France depuis 2012, le prix ajusté à l'inflation montre une
            augmentation modérée, passant de 6 € en 2012 à 6,38 € en 2024. »
CONTEXTE  : même lecture pour l'herbe : prix nominal en légère hausse, prix ajusté de la teneur en légère
            baisse, prix ajusté de l'inflation quasi stable (8 € → 7,97 €).
INCERTITUDE : —
```

### A.8 — AGRASC : saisies et confiscations 2024, tous délits

```
CHIFFRE   : 1,35 Md€ de saisies en 2024 (tous délits confondus) ; 255 M€ de confiscations
MILLÉSIME : 2024
PUBLIÉ EN : 2025 (rapport d'activité 2024)
NATURE    : enregistrement administratif
CHAMP     : France entière, ensemble des saisies et confiscations traitées par l'AGRASC, tous types
            d'infractions (pas seulement narcotrafic)
SOURCE    : AGRASC, Rapport d'activité 2024, 2025
URL       : https://agrasc.gouv.fr/sites/default/files/2025-07/ra_2024_a4_v6.pdf
EXTRAIT   : « Saisies 2024 : 1,35 G€ [...] Confiscations 2024 : 255 M€ »
CONTEXTE  : la passe large (02-marche.md) avait relevé un chiffre de confiscations différent (244 M€, dont
            160 M€ reversés au budget général de l'État), obtenu via un relais de presse (France Bleu /
            France Info). Le montant retrouvé ici (255 M€) diverge — les deux valeurs ne sont pas
            réconciliées, elles portent peut-être sur des périmètres de confiscation légèrement différents
            (brut / net, ou date de clôture d'exercice différente). Ne pas trancher sans réouverture directe
            du PDF.
INCERTITUDE : **limite technique à signaler explicitement.** L'outil de récupération web standard a renvoyé
            une erreur HTTP 503 de façon persistante et répétée sur `agrasc.gouv.fr`, y compris sur deux URL
            différentes du même rapport. Le contenu ci-dessus a été obtenu via un lecteur intermédiaire
            (proxy de lecture r.jina.ai) qui prétend restituer le texte du PDF officiel, mais je n'ai pas pu
            le confirmer par une seconde méthode de lecture indépendante dans le temps imparti. Le
            fact-checker doit impérativement rouvrir ce rapport par ses propres moyens avant toute
            publication de ces chiffres.
```

### A.9 — AGRASC : sous-ensemble narcotrafic 2024

```
CHIFFRE   : saisies liées aux stupéfiants : 95 M€, soit 7 % du montant global des saisies AGRASC ;
            confiscations liées aux stupéfiants : 79 M€, soit 32 % du montant global des confiscations ;
            29 736 biens saisis liés aux stupéfiants, soit 56,9 % du nombre total de biens saisis
MILLÉSIME : 2024
PUBLIÉ EN : 2025 (rapport d'activité 2024)
NATURE    : enregistrement administratif
CHAMP     : France entière, sous-ensemble « stupéfiants » au sein des saisies et confiscations totales de
            l'AGRASC (voir A.8 pour le total)
SOURCE    : AGRASC, Rapport d'activité 2024, 2025
URL       : https://agrasc.gouv.fr/sites/default/files/2025-07/ra_2024_a4_v6.pdf
EXTRAIT   : « Saisies stupéfiants 2024 : 95 M€ représentant 7 % du montant global des saisies [...]
            Confiscations stupéfiants 2024 : 79 M€ soit 32 % du montant global des confiscations [...]
            Nombre de biens saisis (stupéfiants) : 29 736 articles représentant 56,9 % en nombre de tous
            les biens saisis. »
CONTEXTE  : le rapport présente donc bien, à en croire cette extraction, le contraste que la passe large
            avait relevé via un relais de presse (« 57 % du volume, 7 % de la valeur ») — la condition dure
            du triage (le sous-ensemble narcotrafic doit figurer littéralement dans le rapport) semble
            satisfaite, mais **avec la même réserve technique qu'en A.8** : cette citation n'a pas été
            confirmée par une lecture directe et indépendante du PDF officiel, seulement par un lecteur
            intermédiaire. Le montant précis diverge légèrement de celui relayé par la presse pour 2024
            (95 M€ ici contre « plus de 95 M€ avant jugement » et « 79 M€ de saisies effectives récupérées »
            dans le relais France Bleu de la passe large) — les deux formulations sont proches mais pas
            identiques dans leur définition exacte (saisies vs. confiscations).
INCERTITUDE : même réserve qu'en A.8 — extraction non confirmée par une seconde méthode ; à rouvrir
            impérativement en vérification.
```

### A.10 — DGDDI (douane) : résultats 2024

```
CHIFFRE   : 110,8 tonnes de stupéfiants saisies par la douane sur le territoire national en 2024 (+18 % en
            un an), dont : cocaïne près de 21 tonnes (+74 %, meilleur résultat depuis dix ans), cannabis
            66,11 tonnes, drogues de synthèse 3,086 tonnes (+27 %) ; valeur estimée 1 236,66 millions
            d'euros (+44,6 %)
MILLÉSIME : 2024
PUBLIÉ EN : non daté précisément dans la page consultée ; la présentation des résultats annuels de la
            douane a habituellement lieu au premier trimestre de l'année suivante (à confirmer, probablement
            début 2025)
NATURE    : enregistrement administratif
CHAMP     : France entière, saisies réalisées par la seule douane (DGDDI) — champ **plus étroit** que le
            chiffre « tous services » de l'OFDT/OFAST (53,5 tonnes de cocaïne, fiche A.5) : la douane ne
            comptabilise que ses propres opérations, la police et la gendarmerie n'y figurent pas
SOURCE    : Direction générale des douanes et droits indirects (DGDDI), « Amélie de Montchalin présente les
            résultats de la douane française pour l'année 2024 », douane.gouv.fr
URL       : https://www.douane.gouv.fr/actualites/amelie-de-montchalin-presente-les-resultats-de-la-douane-francaise-pour-lannee-2024
EXTRAIT   : « 110,8 tonnes de stupéfiants saisis sur le territoire national, (+18% en un an) » / « Près de
            21 tonnes de cocaïne (+ 74%), meilleur résultat depuis 10 ans » / « 66,11 tonnes de cannabis » /
            « 3,086 t de drogues de synthèse (+ 27 %) » / « 1236,66 millions d'euros (+44,6%) »
CONTEXTE  : 92 organisations criminelles démantelées, 376 trafiquants identifiés par la douane en 2024 ;
            32,67 tonnes supplémentaires saisies à l'étranger grâce à la coopération douanière française.
            Le champ « douane seule » (21 t de cocaïne) explique l'écart avec le chiffre « tous services »
            de l'OFDT (53,5 t) — ce n'est pas une divergence mais deux périmètres de services emboîtés,
            à traiter comme tel dans le numéro.
INCERTITUDE : la valorisation en euros (1 236,66 M€, +44,6 %) n'est assortie d'aucune méthode de
            valorisation publique documentée dans cette page — le dispositif du numéro écarte par principe
            « la valeur en euros des saisies » en l'absence de méthode homogène publiée (« une saisie
            valorisée au prix de détail est un artefact de calcul, pas une mesure », section 9 du triage).
            Signalé pour que l'éditeur tranche l'usage de ce chiffre. Je n'ai pas localisé le « Bilan annuel
            de la Douane 2024 » complet (probablement un document distinct, plus long, référencé par l'OFDT
            en bibliographie de sa propre note) ; seule cette page de résultats a pu être ouverte dans le
            budget imparti.
```

---

## B. Les grandeurs manquantes

### B.1 — Chiffrage public d'une taxation des stupéfiants : CE N'EST PAS UNE ABSENCE

Contrairement à l'hypothèse du triage, une recherche bornée aboutit à un résultat positif, au moins pour le
cannabis : le Conseil d'analyse économique (CAE), organisme public placé auprès du Premier ministre, a publié
une estimation chiffrée détaillée.

```
CHIFFRE   : recettes fiscales annuelles estimées d'une légalisation encadrée du cannabis récréatif en
            France : 2 Md€ (scénario central, 500 tonnes vendues/an, prix cible 9 €/g TTC) à 2,8 Md€
            (scénario alternatif, 700 tonnes/an) ; cotisations sociales associées : 250 à 530 M€ (scénario
            500 t) à 360-740 M€ (scénario 700 t) ; emplois créés (directs + indirects + induits) : 27 500 à
            57 000 (scénario 500 t) à 40 000-80 000 (scénario 700 t)
MILLÉSIME : simulation datée « pour 2017 » (estimation de consommation actualisée par les auteurs à cette
            année de référence) ; hypothèses de prix construites sur des données 2018-2019
PUBLIÉ EN : juin 2019
NATURE    : estimation modélisée
CHAMP     : France entière, cannabis récréatif SEUL (pas les autres stupéfiants), dans l'hypothèse d'une
            légalisation encadrée avec monopole public de production et de distribution
SOURCE    : Auriol E., Geoffard P.-Y., « Cannabis : comment reprendre le contrôle ? », Les notes du Conseil
            d'analyse économique, n° 52, juin 2019
URL       : https://cae-eco.fr/static/pdf/cae-note052.pdf
EXTRAIT   : « En appliquant ce prix à l'estimation des 500 tonnes, cela signifie un niveau de recettes
            fiscales de 2 milliards d'euros. » / « Selon un scénario alternatif de ventes de 700 tonnes par
            an [...], les recettes fiscales représenteraient 2,8 milliards d'euros, les cotisations sociales
            entre 360 et 740 millions, pour un nombre d'emplois dans la filière entre 40 000 et 80 000. »
CONTEXTE  : cette note porte la mention, en première page : « Cette note est publiée sous la responsabilité
            des auteurs et n'engage que ceux-ci. » Le CAE est un organisme public (« créé auprès du Premier
            ministre »), mais cette note formule explicitement une recommandation de légalisation encadrée
            du cannabis (six « Recommandations » numérotées dans le corps du texte) — ce que le dispositif
            du numéro interdit précisément de faire lui-même. La note est donc à traiter comme une source
            officielle qui prend position, pas comme une mesure neutre : à signaler comme telle si elle
            entre dans le numéro. Champ limité au cannabis, alors que la question posée par le brief porte
            sur « ces produits » en général — aucun chiffrage équivalent trouvé pour les autres stupéfiants
            dans le temps imparti. La méthode détaillée est renvoyée à une note technique compagne, non
            ouverte : Geoffard P.-Y., Beuve J., Fize É. (2019), « Une filière du cannabis en France », Focus
            du CAE, n° 34-2019, juin — EXTRAIT : non lu pour cette note technique séparée.
INCERTITUDE : « il est probable qu'elles représentent une borne inférieure » (citation de la note :
            « les estimations de demande [...] et de recettes fiscales sont vraisemblablement
            sous-évaluées »). L'estimation de consommation totale (500 tonnes) part d'une mesure ancienne de
            2005 (276,6 tonnes, Ben Lakhdar & Kopp 2018) actualisée « à dire d'expert » sans méthode
            statistique détaillée dans cette note de synthèse.
```

**Contexte complémentaire de la même note (dépense publique de répression du cannabis seul).** La note cite
un chiffre distinct et non demandé par ce brief mais utile pour la rubrique 4 du numéro : « la dépense
publique engagée pour lutter contre le cannabis est estimée à 568 millions d'euros [...] Si on rajoute les
pertes de revenus, de production et de prélèvements obligatoires liées à l'emprisonnement, le coût social du
cannabis serait supérieur de 40 %, soit 919 millions d'euros » — source secondaire citée : Ben Lakhdar C.,
Kopp P. (2018), « Faut-il légaliser le cannabis en France ? Un bilan socio-économique », *Économie et
Prévision*, n° 213, pp. 19-39 — EXTRAIT : non lu (je n'ai pas ouvert cette publication tierce, seulement la
citation qu'en fait la note CAE).

### B.2 — Nombre de personnes vivant du trafic : DEUX ESTIMATIONS PUBLIQUES TROUVÉES, TRÈS ÉLOIGNÉES L'UNE DE L'AUTRE

Là aussi, l'hypothèse d'absence ne tient pas complètement. Deux publications officielles distinctes donnent
un chiffre, mais elles ne convergent pas — et partagent une source commune non ouverte par moi.

**Première estimation** : voir fiche A.2 ci-dessus (INSEE, mai 2018) — environ 1 000 personnes dont le trafic
de stupéfiants (tous produits) est l'activité principale, ou environ 21 000 emplois en équivalent temps plein
si l'on inclut l'activité partielle, données 2014, France entière, tous stupéfiants.

**Seconde estimation**, très différente :

```
CHIFFRE   : environ 200 000 personnes travaillant occasionnellement ou à plein temps dans les organisations
            de revente de cannabis, pour la France métropolitaine seule
MILLÉSIME : non daté précisément dans la note CAE (probablement autour de 2016, année du rapport source
            cité) — non confirmable sans ouvrir la publication primaire
PUBLIÉ EN : juin 2019 (citée dans la note CAE n° 52 ; le rapport source date de 2016)
NATURE    : estimation modélisée
CHAMP     : France métropolitaine seule (hors outre-mer), cannabis seul (pas l'ensemble des stupéfiants),
            personnes impliquées dans la revente à quelque degré que ce soit (« petites mains » comprises :
            coupeurs, revendeurs, guetteurs, nourrices)
SOURCE    : citée dans Auriol E., Geoffard P.-Y., « Cannabis : comment reprendre le contrôle ? », Les notes
            du Conseil d'analyse économique, n° 52, juin 2019, qui renvoie à : Ben Lakhdar C., Lalam N.,
            Weinberger D. (2016), « L'argent de la drogue en France. Estimation des marchés des drogues
            illicites », INHESJ, Mildeca, Premier ministre — **publication source non ouverte par moi**
URL       : https://cae-eco.fr/static/pdf/cae-note052.pdf (note CAE, qui porte la citation)
EXTRAIT   : « Les derniers travaux sur le sujet insistent sur la professionnalisation accrue de ces
            organisations de revente de cannabis. Ils estiment à 200 000 le nombre de personnes qui y
            travailleraient occasionnellement ou à plein temps, et ce uniquement pour la France
            métropolitaine. »
CONTEXTE  : cette valeur de 200 000 personnes est environ dix fois l'estimation en ETP de l'INSEE (21 000,
            tous stupéfiants confondus, France entière) et environ deux cents fois son estimation en
            « personnes physiques dont le trafic est l'activité principale » (1 000). **Les deux sources —
            INSEE 2018 et CAE 2019 — citent le même rapport souche : INHESJ/Mildeca, « L'argent de la drogue
            en France », 2016.** Je n'ai pas ouvert ce rapport primaire (non lu) : impossible dans le temps
            imparti d'établir si l'écart tient à des définitions différentes (ETP à temps plein équivalent
            contre effectif de personnes impliquées y compris marginalement), à des périmètres différents
            (cannabis seul contre tous stupéfiants), ou à une révision entre les deux citations. Ce rapport
            source est la pièce qu'il faudrait rouvrir en priorité si cette question devient une entrée du
            numéro.
INCERTITUDE : rapport source INHESJ/Mildeca 2016 non ouvert — les deux chiffres cités par des publications
            officielles postérieures divergent d'un facteur 10 à 200 sans que je puisse en expliquer la
            raison exacte.
```

### B.3 — Chiffre d'affaires du narcotrafic selon la commission d'enquête sénatoriale : une déclaration, pas une mesure

```
CHIFFRE   : chiffre d'affaires du narcotrafic en France : « des centaines de millions d'euros — 3,5
            milliards d'euros au minimum »
MILLÉSIME : propos tenu lors d'une audition le 26 mars 2024
PUBLIÉ EN : mai 2024 (rapport n° 588)
NATURE    : ce n'est pas une mesure statistique mais une déclaration orale rapportée dans un compte rendu
            d'audition — à ne pas confondre avec les fiches A.1 et A.3 ci-dessus, de nature différente
CHAMP     : France entière, narcotrafic (tous stupéfiants), déclaration attribuée au ministre de l'Économie
            et des Finances
SOURCE    : Sénat, commission d'enquête sur l'impact du narcotrafic en France, « Un nécessaire sursaut :
            sortir du piège du narcotrafic », rapport n° 588 (session ordinaire 2023-2024), mai 2024
URL       : https://www.senat.fr/rap/r23-588-1/r23-588-1.pdf
EXTRAIT   : « des centaines de millions d'euros – 3,5 milliards d'euros au minimum » — propos attribué au
            ministre de l'Économie et des Finances lors de son audition du 26 mars 2024, selon l'extraction
            faite de ce rapport
CONTEXTE  : je n'ai trouvé, dans les passages retournés par l'outil de lecture utilisé, ni chiffrage d'une
            taxation, ni estimation du nombre de personnes vivant du trafic dans ce rapport — voir
            incertitude ci-dessous sur le caractère non exhaustif de cette recherche.
INCERTITUDE : **limite technique et limite de méthode à signaler.** Le PDF (7,2 Mo, plusieurs centaines de
            pages estimées) n'a pas pu être extrait nativement par l'outil de récupération web dans le temps
            imparti (uniquement des flux binaires compressés) ; le contenu a été interrogé via un lecteur
            intermédiaire (r.jina.ai) avec des questions ciblées, pas lu intégralement. Le résultat négatif
            sur la taxation et sur le nombre de personnes vivant du trafic n'est donc **pas une preuve
            d'absence dans le rapport** — seulement l'absence de résultat dans les passages retournés par
            cette méthode de recherche. Un fact-checker qui rouvrirait le document par sections (table des
            matières, chapitre économique) pourrait trouver un résultat différent.
```

---

## CE QUI CONTREDIT L'ANGLE

- **Baisse marquée de la violence homicide liée au trafic à Marseille et dans les Bouches-du-Rhône en
  2024**, contemporaine d'un pic de saisies de cocaïne : l'OFAST enregistre 45 faits (homicides et
  tentatives) en 2024 contre 86 en 2023 à Marseille (−60 %, avec 24 décès contre 49), et −82 % à l'échelle du
  département des Bouches-du-Rhône, attribués à l'arrestation de figures centrales de deux réseaux rivaux.
  À l'échelle nationale, les homicides et tentatives liés au trafic reculent de 12 % entre 2023 et 2024
  (367 faits, 110 décès), après un pic en 2023 — mais restent supérieurs à 2021 et 2022 (source : OFDT,
  « L'offre de stupéfiants en France en 2024 », citant l'OFAST/OCLCO ; cette matière relève surtout de la
  rubrique 6 du dispositif, pas de mon lot, signalée ici pour mémoire).
- **Recul des saisies de cannabis (−19 % en 2024) l'année même où les saisies de cocaïne explosent
  (+130 %)** : un récit uniforme d'intensification répressive ne rend pas compte de cet écart entre
  produits — déjà noté par la passe large et confirmé par cette passe profonde (fiches A.4 et A.5).
- **Baisse continue des prix réels de la cocaïne et du cannabis malgré des saisies et une répression en
  hausse** (fiches A.6, A.7) : sur ce marché, l'offre ne semble pas se raréfier — à documenter comme fait,
  pas comme jugement sur l'efficacité de la politique.
- **Rappel méthodologique de l'OFDT lui-même**, à propos des mises en cause pour infraction à la
  législation sur les stupéfiants (hors périmètre direct de mon lot, mais utile à la rubrique 4) : « les
  évolutions observées dans les données de mises en cause pour ILS ne traduisent pas les dynamiques réelles
  de trafic ou de consommation, mais reflètent avant tout l'activité des forces de l'ordre en matière de
  contrôle et de répression. »

---

## PISTES NON ABOUTIES

- **INSEE, actualisation post-2018 (base 2020).** Recherché explicitement : aucune publication distincte
  trouvée qui mettrait à jour le montant de 2,7 Md€ (2014) avec un millésime plus récent. La documentation
  méthodologique de la base 2020 (parue en 2024) semble reconduire la méthode de la note base 2014 sans
  publier de nouveau montant identifié dans le temps imparti. À rechercher spécifiquement dans les fichiers
  détaillés des comptes de la Nation 2020-2024 si le numéro retient cette entrée — hors budget de cette
  passe.
- **Bilan annuel complet de la Douane 2024.** Seule la page de résultats (communiqué) a pu être ouverte ;
  le document « Bilan annuel de la Douane 2024 » proprement dit (référencé par l'OFDT en bibliographie,
  probablement un rapport plus long avec méthode de valorisation) n'a pas été localisé et ouvert. La
  valorisation en euros (1 236,66 M€) reste donc sans méthode publique documentée de mon côté.
- **AGRASC — confirmation indépendante.** `agrasc.gouv.fr` a renvoyé une erreur HTTP 503 à chaque tentative
  de récupération directe (quatre tentatives, deux URL différentes). Les chiffres des fiches A.8 et A.9
  viennent d'un lecteur intermédiaire non vérifié par une seconde méthode — priorité haute pour le
  fact-checker, qui devra retenter l'accès direct (peut-être transitoire) avant toute publication.
- **Tracfin.** Non exploré dans cette passe (budget épuisé avant d'y arriver). Le rapport annuel Tracfin
  reste une piste ouverte pour les typologies de blanchiment liées au narcotrafic.
- **Focus du CAE n° 34-2019** (« Une filière du cannabis en France », Geoffard, Beuve, Fize), qui porte la
  méthode détaillée derrière les chiffres de la fiche B.1. Non ouvert — seule la note de synthèse n° 52 l'a
  été, qui reprend les résultats chiffrés mais renvoie la méthode complète à ce Focus.
- **Rapport source INHESJ/Mildeca 2016**, « L'argent de la drogue en France » — cité à la fois par l'INSEE
  et par le CAE avec des chiffres d'emploi très différents (fiche B.2). Non ouvert. C'est la pièce la plus
  utile à rouvrir si la rubrique « grandeurs manquantes » ou une entrée sur l'emploi lié au trafic est
  retenue : sans elle, l'écart entre 21 000 ETP et 200 000 personnes reste inexpliqué.
- **Chiffrage d'une taxation pour les stupéfiants autres que le cannabis** (cocaïne, héroïne, etc.).
  Recherche non menée spécifiquement au-delà de la note CAE (cannabis seul) et du rapport sénatorial (aucun
  chiffrage trouvé, avec la réserve de non-exhaustivité indiquée en B.3). Probable que rien n'existe côté
  produits durs, mais je ne peux pas l'affirmer avec la même solidité que pour le cannabis, faute d'avoir
  cherché spécifiquement ce sous-cas.
- **Rapport sénatorial n° 588 — lecture non exhaustive.** Voir réserve détaillée dans la fiche B.3 : outil
  de lecture intermédiaire, questions ciblées, pas de lecture linéaire du document. Un second passage sur ce
  rapport (chapitre économique, table des matières) pourrait faire apparaître des éléments que cette passe
  n'a pas trouvés.
- **Second rapport sénatorial repéré mais non ouvert** : « Ces dizaines de milliards qui gangrènent la
  société », Sénat, rapport n° 757 (référence trouvée en cours de recherche, sans URL confirmée par un
  outil — non retenu faute de budget). Titre laissant penser à un développement du chiffrage économique du
  narcotrafic ; à vérifier si le numéro veut approfondir ce point.

**Répartition du budget effectivement suivie** : 7 publications ouvertes sur les 5-7 permises. INSEE (1),
OFDT « offre 2024 » (1), OFDT « taille des marchés » Ben Lakhdar/Massin (1), AGRASC (1, lecture dégradée),
DGDDI/douane (1, page de résultats seulement), Sénat n° 588 (1, lecture dégradée et non exhaustive), CAE
note 52 (1, lecture complète). Aucun budget n'a pu être consacré à Tracfin ni au Focus CAE n° 34-2019.
