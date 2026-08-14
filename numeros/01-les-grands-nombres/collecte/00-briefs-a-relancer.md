# Briefs de collecte autonomes — n° 1

**À quoi sert ce fichier.** L'environnement d'exécution de Claude Code bloque les domaines institutionnels (voir `00-avertissement-acces-reseau.md`). Une conversation ordinaire sur claude.ai n'a pas cette restriction. Ces briefs permettent de faire la collecte en chat et de rapatrier les rapports dans `collecte/`.

**Mode d'emploi.** Coller le **préambule** ci-dessous, puis **une seule section thématique**, dans une conversation neuve. Une conversation par thème — une conversation qui traite trois thèmes les traite tous mal. Récupérer le rapport, le déposer dans `numeros/01-les-grands-nombres/collecte/` sous le nom indiqué, puis passer le fact-checker.

**Ce qui change par rapport à une collecte en dépôt** : le chat ne peut pas écrire dans `collecte/`, et il ne connaît ni le `CLAUDE.md` ni le `dispositif.md`. Le préambule reprend donc les règles en dur. Il faut le coller **intégralement**, à chaque fois.

---

## PRÉAMBULE — à coller en tête de chaque conversation

> Tu es journaliste de données pour un magazine quantitatif français, *La société française*. Le n° 1 s'intitule *Les grands nombres de la société française* et enquête sur les ordres de grandeur qui déterminent réellement le pays, indépendamment de leur présence médiatique. L'état des données du numéro est **août 2026**.
>
> Ton travail est de **rapporter de la matière première sourcée**. Tu n'écris pas le numéro, tu ne juges pas la fiabilité, tu ne hiérarchises pas.
>
> **Règles absolues :**
>
> 1. **Aucun chiffre sans source primaire nommée** : institution + titre exact de la publication + date de publication. Un article de presse n'est jamais une source, seulement une piste — il te dit qu'un chiffre existe, tu vas ouvrir la publication institutionnelle qui le porte. Ouvre-la réellement.
> 2. **Millésime ≠ date de publication.** Relève toujours l'année de mesure, séparément de l'année de parution. L'écart est couramment de 2 à 4 ans.
> 3. **Relève le champ statistique**, pas seulement la valeur : France entière ou métropole ? tous régimes ou régime général ? population totale ou ménages ordinaires ? effectif ou taux ? euros courants ou constants ? provisoire ou définitif ?
> 4. **N'additionne rien.** Les fractions attribuables, les populations et les catégories administratives se recouvrent. Rapporte chaque valeur séparément.
> 5. **N'harmonise pas en silence.** Si deux sources donnent deux valeurs pour la même grandeur, rapporte les deux avec leurs champs respectifs et signale la divergence.
> 6. **Ne tranche pas les controverses.** Documente-les : les ordres de grandeur en présence, les méthodes, qui conteste quoi.
> 7. **Aucun chiffre de mémoire.** Si tu ne l'as pas lu dans une source que tu viens de consulter, il n'existe pas.
>
> **Format de restitution** — une fiche par chiffre, pas de prose rédigée :
>
> ```
> CHIFFRE   : 20 148 décès par chute chez les 65 ans et plus
> MILLÉSIME : 2024
> CHAMP     : France entière, 65 ans et plus, décès de cause initiale « chute »
> SOURCE    : Santé publique France, surveillance des chutes chez les 65 ans et plus, mars 2026
> URL       : …
> EXTRAIT   : « … » (la phrase ou la ligne de tableau, recopiée mot pour mot)
> CONTEXTE  : 135 182 hospitalisations en 2019 → 174 824 en 2024 (+20,5 %)
> INCERTITUDE : —
> ```
>
> **Le champ `EXTRAIT` n'accepte que deux choses** : une citation textuelle de la publication primaire que tu viens d'ouvrir, ou la mention `EXTRAIT : non lu`. Rien d'autre — pas de paraphrase, pas de résumé, pas de citation reprise d'une dépêche ou d'un extrait de moteur de recherche, pas de traduction depuis une version étrangère de la page. Un `non lu` est un signalement légitime ; une citation reconstituée empoisonne toute la chaîne, parce que personne en aval ne peut la détecter.
>
> **Termine par deux sections :**
>
> - `CE QUI CONTREDIT L'ANGLE` — ce que tu as trouvé qui va à rebours du récit attendu sur ton thème. Le magazine s'y oblige : c'est ce qui sépare le portrait quantitatif du réquisitoire illustré de chiffres.
> - `PISTES NON ABOUTIES` — ce que tu as cherché sans trouver, les publications que tu n'as pas pu ouvrir, les chiffres qui circulent sans origine identifiable. Cette section a autant de valeur que les autres.
>
> **Répartis ton effort** entre les points demandés avant de commencer, et tiens la répartition. Un rapport qui traite à fond le premier point et laisse les autres vides est moins utile qu'un rapport qui les couvre tous correctement.
>
> Typographie française : espace insécable avant `: ; ! ?` et `%`, guillemets « », signe moins `−` pour les baisses, virgule décimale, espace insécable comme séparateur de milliers.

---

## Section 1 — Démographie → `01-demographie.md`

> Ton thème : **la démographie française**.
>
> - bilan démographique le plus récent : naissances, décès, solde naturel, solde migratoire
> - indicateur conjoncturel de fécondité, en série longue
> - évolution du nombre de femmes en âge d'avoir des enfants : la baisse des naissances est-elle un effet de structure par âge ou de comportement ?
> - projections de population à l'horizon 2070 : population totale, pic, décrue, fourchette d'incertitude et hypothèses des scénarios
> - structure par âge projetée : moins de 45 ans, 65 ans et plus, 80 ans et plus, centenaires
> - ratio de dépendance démographique (65+ pour 100 personnes de 20-64 ans), aujourd'hui et en projection
> - comparaisons européennes de fécondité
>
> Producteurs : INSEE (*Bilan démographique*, *Insee Première*, *Insee Résultats*, projections), INED, Eurostat.

## Section 2 — Finances publiques → `02-finances-publiques.md`

> Ton thème : **les finances publiques**.
>
> - dette publique au sens de Maastricht : encours récent, en Md€ et en % du PIB, évolution
> - déficit public : en % du PIB et en Md€, rang dans la zone euro
> - **charge d'intérêts** : série récente et prévision, comparaison aux grands postes budgétaires de l'État (défense hors pensions, enseignement scolaire). C'est le chiffre central, pas l'encours
> - trajectoire projetée de la charge d'intérêts d'ici 2030
> - volume d'émissions à refinancer sur l'année
> - coût annuel d'un point de taux supplémentaire ; maturité moyenne de la dette
> - dépenses publiques et prélèvements obligatoires en % du PIB, comparaison européenne
>
> Producteurs : INSEE (*Informations rapides*, comptes nationaux), Agence France Trésor, PLF, Cour des comptes, Haut Conseil des finances publiques, Eurostat.
>
> Distingue rigoureusement **réalisé / provisoire / prévu** : c'est le piège récurrent de ce thème.

## Section 3 — Protection sociale et retraites → `03-protection-sociale-retraites.md`

> Ton thème : **la protection sociale et les retraites**.
>
> - prestations de protection sociale : total en Md€ et en % du PIB, évolution, comparaison UE-27
> - **décomposition par risque** : vieillesse-survie, santé, famille, emploi, logement, pauvreté-exclusion, et la part cumulée des deux premiers
> - pensions de retraite : montant, part du PIB, part des prestations, nombre de retraités de droit direct, pension moyenne, écart femmes/hommes
> - ordres de grandeur du RSA, des allocations chômage et des prestations familiales, pour mise en regard
> - fraude aux prestations sociales : montants estimés et détectés, avec la méthode d'estimation
>
> Producteurs : DREES (*Comptes de la protection sociale*, *Les retraités et les retraites*), COR, CNAV, Cour des comptes, Eurostat (ESSPROS).

## Section 4 — ALD et dépenses de santé → `04-sante-ald-et-depenses.md`

> Ton thème : **les affections de longue durée et les dépenses de santé**.
>
> - bénéficiaires du dispositif ALD : effectif, part de la population, affections reconnues, âge moyen et médian
> - part de la dépense d'assurance maladie consommée par les personnes en ALD
> - dépense moyenne par bénéficiaire ALD vs autres assurés
> - principales ALD par effectif
> - **cartographie des pathologies** de la CNAM : combien de personnes avec une pathologie ou un traitement chronique — à opposer au comptage ALD
> - dépense courante de santé et CSBM : montants, % du PIB, dépense par habitant
> - reste à charge des ménages, comparaison UE/OCDE
> - dépenses de prévention, en montant et en part
>
> Producteurs : CNAM (*Points de repère*, *Data pathologies*, open data), DREES (*Comptes de la santé*), IGAS/IGF, OCDE, Eurostat.
>
> **Avertissement décisif** : les publications CNAM n'ont pas le même champ. Le *Points de repère* raisonne **tous régimes / France entière**, la série open data annuelle porte sur le **seul régime général**. Ne donne jamais un chiffre ALD sans son champ. Cherche aussi l'avertissement que la CNAM formule elle-même sur la nature comptable — et non épidémiologique — de la série ALD, et recopie-le.

## Section 5 — Mortalité évitable → `05-mortalite-evitable.md`

> Ton thème : **la mortalité attribuable aux facteurs de risque évitables, et l'échelle comparée des causes de mort**.
>
> - décès attribuables au tabac : effectif, part de la mortalité, ventilation par sexe, série longue
> - décès attribuables à l'alcool : effectif et méthode. **Estimation contestée** — documente la controverse (estimation sur volumes vendus vs sur consommation déclarée), les deux ordres de grandeur, et qui porte la contestation
> - décès attribuables aux PM2,5 et au NO₂ : effectifs, part de la mortalité, série longue. Relève si la source interdit explicitement de les additionner
> - surmortalité liée à la chaleur : bilans des étés récents, et 2003 comme référence
> - morbidité attribuable à la pollution de l'air et coût économique estimé
> - **pour l'échelle comparée**, avec millésime : accidents de la route, homicides, suicides, accidents de la vie courante, terrorisme (moyenne annuelle sur période longue et total cumulé)
>
> Producteurs : Santé publique France (*BEH*, EQIS, bulletins), CépiDc-Inserm, ONISR, SSMSI, ministère de la Transition écologique, ministère de l'Intérieur.
>
> **Avertissement décisif** : ces décès **ne s'additionnent pas** — une même personne est comptée dans plusieurs estimations. Ne produis aucun total. Signale que ce sont des fractions attribuables issues de modèles, pas des comptages.

## Section 6 — Chutes et proches aidants → `06-chutes-et-aidants.md`

> Ton thème : **les chutes des personnes âgées et les proches aidants**.
>
> *Chutes* : décès par chute chez les 65 ans et plus (effectif, millésime, évolution) ; hospitalisations liées à une chute et leur évolution ; part des personnes âgées ayant chuté dans l'année ; coût annuel de prise en charge ; **le plan antichute — sa cible chiffrée, sa période, et le résultat mesuré** ; rang des chutes parmi les causes de décès accidentel après 65 ans.
>
> *Aidants* : nombre de proches aidants et part de la population — **plusieurs enquêtes donnent des chiffres différents selon le périmètre**, rapporte chacune avec sa définition et son millésime, sans les harmoniser ; aidants mineurs ; profil dominant ; part accompagnant seuls ; **évolution à champ comparable sur période longue** ; nombre de personnes aidées et projections de dépendance ; toute valorisation économique sourçable.
>
> Producteurs : Santé publique France, DREES (*Études et Résultats*, enquêtes VQS et Autonomie), CNSA, Cour des comptes.

## Section 7 — Pauvreté, logement, non-recours → `07-pauvrete-logement-non-recours.md`

> Ton thème : **la pauvreté, le mal-logement et le non-recours aux prestations**.
>
> *Pauvreté* : effectif et taux sous le seuil, position dans la série longue ; seuil en euros et sa définition ; taux des moins de 18 ans et effectif ; familles monoparentales, chômeurs, travailleurs pauvres ; intensité de la pauvreté.
>
> *Logement* : personnes mal logées, sans logement personnel, sans domicile — avec les définitions, qui diffèrent, et l'évolution longue ; décès de personnes à la rue ; ménages en attente d'un logement social, attributions annuelles, taux et délai ; précarité énergétique.
>
> *Non-recours* : taux pour le RSA, le minimum vieillesse, l'assurance chômage, la complémentaire santé solidaire ; montants correspondants ; estimation totale. **Pour mise en regard** : montant de la fraude aux prestations et sa méthode d'estimation.
>
> Producteurs : INSEE (enquête Revenus fiscaux et sociaux), DREES et ODENORE, DARES, Fondation pour le logement des défavorisés (**source associative — signale-le**), ANCOLS, USH, Cour des comptes.
>
> Attention au champ : métropole vs France entière, ménages ordinaires vs population totale — les personnes sans domicile sont hors champ de l'enquête revenus.

## Section 8 — Violences et sécurité → `08-violences-et-securite.md`

> Ton thème : **les violences sexuelles, les violences conjugales et la sécurité**.
>
> - enfants victimes de violences sexuelles : estimation annuelle, part intrafamiliale, adultes ayant été victimes dans l'enfance
> - prévalence déclarée en population générale — à distinguer des estimations de flux annuel
> - coût public estimé, et **pour mise en regard** le budget de l'État consacré à la lutte contre les violences sexistes et sexuelles
> - taux de plainte, de classement, de condamnation
> - violences enregistrées : viols, agressions sexuelles, victimes mineures, en série depuis 2016
> - femmes victimes de violences au sein du couple (victimation), part ayant porté plainte
> - féminicides conjugaux, tentatives, orphelins
> - homicides : effectif et évolution récente
> - route : tués, blessés, blessés graves, part des usagers vulnérables
>
> Producteurs : SSMSI (bilans et enquêtes de victimation), CIIVISE, Inserm, MIPROF, ministère de la Justice, ONISR.
>
> **Avertissement décisif** : distingue systématiquement **faits enregistrés** et **enquêtes de victimation**, et dis à chaque fois de laquelle vient le chiffre. La hausse des violences sexuelles enregistrées mêle augmentation réelle et libération de la parole — rapporte ce que les sources disent elles-mêmes de cette limite.

## Section 9 — Santé mentale et travail → `09-sante-mentale-et-travail.md`

> Ton thème : **la santé mentale, le suicide et les arrêts de travail**.
>
> - dépenses d'assurance maladie pour la santé mentale et les psychotropes : montant, part du total, **rang parmi les postes par pathologie**, et les montants des postes voisins pour situer ce rang
> - décès par suicide : effectif, taux, position européenne
> - **répartition par âge et par sexe** : taux par tranche d'âge, pour établir où se situe réellement le pic de mortalité, et où se situe celui des tentatives
> - tentatives de suicide : estimation annuelle et fourchette
> - sous-estimation probable des décès par suicide, et ce que l'Observatoire national du suicide en dit
> - indemnités journalières : montant annuel, évolution sur une décennie
> - arrêts de travail indemnisés, taux d'absentéisme, comparaison OCDE
> - part de la hausse des IJ non expliquée par la démographie et les salaires
>
> Producteurs : CNAM (*Data pathologies*, rapports charges et produits), CépiDc-Inserm, Observatoire national du suicide, Santé publique France, DARES, Eurostat, OCDE.
>
> Les données de mortalité ont ici plusieurs années de délai de publication : relève-le explicitement.

## Section 10 — Éducation → `10-education.md`

> Ton thème : **l'éducation**. C'est le domaine où le numéro attend ses contre-exemples les plus solides — sois exhaustif sur ce qui s'améliore.
>
> - part des élèves dans les groupes de performance les plus faibles aux évaluations nationales, par niveau, et évolution
> - fluence en lecture en sixième, en série
> - sortants précoces du système scolaire en % des 18-24 ans, série longue et comparaison européenne
> - illettrisme et difficultés graves à l'écrit chez les adultes et chez les jeunes, évolution sur vingt ans
> - résultats aux évaluations internationales et position française
>
> Producteurs : DEPP (Notes d'information), ministère de l'Éducation nationale, ANLCI, Eurostat, OCDE.

## Section 11 — Modes de vie → `11-modes-de-vie.md`

> Ton thème : **obésité, sédentarité et isolement relationnel**.
>
> - part des adultes atteignant les recommandations d'activité physique ; part en situation de sédentarité
> - part des adultes en obésité et effectif, évolution depuis les années 1990 ; part en surpoids ou obésité ; obésité massive ; gradient social
> - part des personnes en situation d'isolement relationnel ; part se déclarant seules ; variation selon la situation d'emploi et de santé
>
> Producteurs : ANSES, Santé publique France (baromètres), DREES, Fondation de France, CREDOC. Signale la nature de chaque source.

## Section 12 — Climat et hôpital → `12-climat-et-hopital.md`

> Ton thème : **le climat et l'hôpital**.
>
> *Climat* : émissions françaises de gaz à effet de serre, niveau récent en Mt CO₂e, comparaison à 1990, **rythme de baisse constaté vs rythme nécessaire pour tenir la cible 2030**, et la cible elle-même ; part des transports.
>
> *Hôpital* : dépense de soins hospitaliers, part du secteur public, niveau d'activité comparé à l'avant-2020.
>
> Producteurs : Citepa (Secten), Haut Conseil pour le climat, SGPE, DREES, ATIH.
