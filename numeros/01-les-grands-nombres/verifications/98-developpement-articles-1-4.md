# Vérification du développement — articles 1 à 4

**Date** : 15 août 2026. **Portée** : ce que le développement en articles de deux pages (15 août 2026) a ajouté aux quatre premiers rangs du Top 10 — solde naturel, vieillissement, ALD, prestations sociales. Les chiffres déjà couverts par `verifications/01-demographie.md`, `verifications/04-sante-ald-et-depenses.md`, `verifications/03-protection-sociale-retraites.md` et `verifications/99-passe-finale.md` ne sont pas refaits ; seule leur reprise fidèle est contrôlée.

**Méthode** : confrontation systématique de chaque nombre non couvert par ces quatre rapports à `collecte/01-demographie.md`, `collecte/04-sante-ald-et-depenses.md` et `collecte/03-protection-sociale-retraites.md`. Deux publications primaires rouvertes pour trancher un doute né du texte : IGAS/IGF, *Revue de dépenses relative aux affections de longue durée*, juin 2024 (recherche ciblée sur l'ALD 12 et le terme « résiduel ») ; DREES, *La protection sociale en France et en Europe en 2024*, éd. 2025 (recherche ciblée sur le taux de croissance du risque santé). Budget : 2 publications sur 6 autorisées ; les 4 restantes n'ont pas été nécessaires, le reste du contrôle portant sur la traçabilité vers `collecte/`, conformément au brief.

---

## Problèmes relevés

**[ERREUR — chiffre non tracé dans la collecte, mais confirmé exact à la relecture de la source] « santé de 4,0 % » (article 4, contrepoint)**

Le texte publié : « Les cinq autres progressent — vieillesse-survie de 6,5 %, famille de 4,7 %, santé de 4,0 %, emploi de 3,8 %, logement de 1,9 % ». Les quatre autres taux (6,5 / 4,7 / 3,8 / 1,9 %) sont bien dans `collecte/03-protection-sociale-retraites.md`, littéralement cités. Le taux du risque santé, « 4,0 % », n'y figure **nulle part** — la fiche du risque santé (338,9 Md€) ne donne aucun taux de croissance 2024. Recherche confirmée par grep sur l'ensemble du fichier de collecte.

À la relecture directe de la source primaire (DREES, *La protection sociale en France et en Europe en 2024*, éd. 2025, tableau 2 : « Santé 338,9 4,0 36,3 »), le chiffre s'avère exact. Ce n'est donc pas une erreur de fond, mais un chiffre apparu à l'écriture sans passer par la collecte — exactement le mode de défaillance que ce contrôle est chargé de repérer, et qui aurait pu tout aussi bien produire une valeur fausse. Le CLAUDE.md (règle 7) interdit tout chiffre « de mémoire » indépendamment de son exactitude a posteriori.

**Correction** : ajouter la ligne au dossier de collecte a posteriori, ou a minima signaler la source dans le texte (DREES, tableau 2) plutôt que de la laisser sans trace.

---

**[NIVEAU DE CONFIANCE MAL DÉCLARÉ] Cinq valeurs ajoutées par le développement, présentes en collecte mais non couvertes par un rapport de vérification, et non marquées « niveau collecté »**

Le numéro s'engage lui-même (section Méthode) : « les valeurs qu'il fait apparaître et qu'aucun rapport de vérification ne couvre portent dans le texte la mention "niveau collecté" ». Les cinq valeurs suivantes tracent proprement à `collecte/`, mais ne figurent dans aucun des rapports thématiques de `verifications/` (qui portent, pour la santé et la protection sociale, sur une liste fermée et explicitement bornée de chiffres « retenus au triage ») et ne portent pas la mention requise :

1. **Article 3** — « 256 320 assurés du régime général y étaient encore rattachés » (ALD 12, hypertension artérielle sévère). Présent dans `collecte/04-sante-ald-et-depenses.md` (ligne 70, en `CONTEXTE`, non en `EXTRAIT` cité mot pour mot), absent de la liste « Chiffres confirmés » de `verifications/04-sante-ald-et-depenses.md`.
2. **Article 4** — « 381,6 Md€ de vieillesse et 45,1 Md€ de survie » (décomposition du risque vieillesse-survie). Cité littéralement en collecte, absent de la liste « Chiffres confirmés » de `verifications/03-protection-sociale-retraites.md`.
3. **Article 4** — « composé à 82 % du sous-risque maladie, soit 278 Md€ à lui seul, l'équivalent de 9,5 % du PIB » (décomposition du risque santé). Cité littéralement en collecte, non vérifié.
4. **Article 4** — « dont 16,3 millions résidant en France » (sur les 17,2 millions de retraités de droit direct). Présent en collecte, mais seulement en `CONTEXTE` non cité mot pour mot, non vérifié.
5. **Article 4** — « 4,4 millions percevaient une pension de réversion, dont 87 % de femmes, et pour 884 000 d'entre elles c'était l'unique pension. » Cité littéralement en collecte (fiche 03, `EXTRAIT`), non vérifié.

Aucune de ces cinq valeurs n'est fausse au regard de ce que rapporte la collecte — ce n'est pas une invention. Mais leur absence de marquage donne au lecteur une fausse garantie : il croit lire une ligne au niveau « vérifié » (rouvert par le fact-checker) alors qu'elle est au niveau « collecté ». Comparer avec les lignes voisines du même article, correctement marquées : « 58,8 % du revenu d'activité net moyen des personnes en emploi (niveau collecté) », « 64 % d'entre eux ont dépassé 60 ans […] (niveau collecté) », « 73 980 assurés (niveau collecté pour cette répartition) », « la Finlande deviendrait […] (niveau collecté, comme la comparaison des rythmes de progression) ». Le marquage a donc été appliqué par endroits dans les deux mêmes articles, ce qui exclut un oubli systémique de convention et pointe vers cinq omissions ponctuelles.

**Correction** : ajouter « (niveau collecté) » aux cinq occurrences, ou les faire vérifier avant publication.

---

**[POINT DEMANDÉ — ALD 12] La formulation corrigée dit bien l'inverse de l'erreur signalée, mais attribue au rapport un mot qu'il n'a pas été possible d'y retrouver**

Le texte actuel : « Il n'a pas éteint les droits ouverts : onze ans après, 256 320 assurés du régime général y étaient encore rattachés, au titre d'un effectif que le rapport qualifie de résiduel. »

Sur le fond, la correction va dans le bon sens : 256 320 est bien, dans le tableau 3 de l'IGAS/IGF (millésime 2022, régime général), l'effectif **encore rattaché** à l'ALD 12 onze ans après son retrait de la liste (2011) — et non un effectif de personnes qui auraient « cessé d'être comptées », comme l'affirmait la version antérieure. La direction de la correction est la bonne, et l'ordre de grandeur (256 320, 2022, régime général) est correctement reproduit depuis `collecte/04-sante-ald-et-depenses.md`.

En revanche, l'attribution « que le rapport qualifie de résiduel » n'a pas pu être confirmée : une relecture ciblée de l'IGAS/IGF autour du tableau 3 et de sa note 20 (p. 8-9) fait apparaître que le rapport documente une décroissance de l'effectif (« taux de croissance 2010-2022 : −79,0 % ») et le fait que ces patients sont « maintenus en ALD malgré le retrait officiel de 2011 », mais le mot « résiduel » n'apparaît pas dans le passage retrouvé. Dans la collecte elle-même, ce mot figure uniquement dans une parenthèse du journaliste, en `CONTEXTE` non cité mot pour mot (« HTA sévère (ALD 12, retirée de la liste en 2011 mais effectif résiduel) 256 320 »), pas dans l'`EXTRAIT` entre guillemets. Le texte publié transforme donc une caractérisation du journaliste en citation implicite du rapport lui-même. Extraction PDF imparfaite (flux compressé) : je ne peux pas exclure à 100 % que le mot figure ailleurs dans le rapport, mais il n'a pas pu être confirmé avec le budget alloué à ce point précis.

**Correction** : écrire « … un effectif que la collecte qualifie de résiduel » ou simplement « … un effectif résiduel » sans l'attribuer nommément au rapport, sauf à retrouver la citation exacte.

---

**[MILLÉSIME / précision mineure] Année de création du dispositif ALD : 1945 dans le texte, 1947 dans la source**

Le texte publié (article 3, « L'ancrage ») : « Le dispositif date de 1945 et n'a que peu changé : quatre pathologies sévères à l'origine, vingt-neuf aujourd'hui. »

La collecte cite l'IGAS/IGF : « Mis en place en 1947 à la création de la Sécurité Sociale, le dispositif ALD n'a que peu évolué depuis sa création. […] la liste des ALD s'est considérablement étendue, passant de quatre pathologies sévères en 1945 à trente affections "liste". » La source distingue donc deux dates : 1945 est l'année des quatre pathologies d'origine (avant la création de la Sécurité sociale elle-même), 1947 celle de la création du dispositif ALD. Le texte publié fusionne les deux en une seule date, 1945, pour qualifier « le dispositif ». Écart mineur mais évitable au regard de l'exigence de millésime précis du numéro.

**Correction** : « Le dispositif date de 1947 » (ou : « conçu à la création de la Sécurité sociale en 1947, sur une liste de quatre pathologies sévères dès 1945 »).

---

## Chiffres contrôlés et conformes

**[OK — déjà validé, correctement repris] 13,8 millions de bénéficiaires ALD, 2022, sourcés « article scientifique reprenant les données CNAM »**

Ce point avait été explicitement discuté par `verifications/04-sante-ald-et-depenses.md` (NON VÉRIFIÉ tant que le *Points de repère* n° 54 de la CNAM reste inaccessible) puis tranché par `verifications/99-passe-finale.md`, qui atteste que la valeur publiée est « créditée à l'article scientifique reprenant les données CNAM, jamais au *Points de repère* n° 54 que personne n'a ouvert ». Le texte développé reprend exactement cette attribution, sans glisser vers une fausse impression de source CNAM directe. Conforme à ce qui a déjà été validé — pas un problème introduit par le développement.

**[OK] Ratios recalculés** — ×2,1 (80 ans et plus), ×4,3 (centenaires, 160 000/37 000 = 4,32), +55 % (rapport de dépendance, 62/40), écart européen de 4,6 points (31,9 − 27,3), écart 8,7 → 0,3 point (25,1−16,4 ; 22,5−22,2), part cumulée 82,1 % (426,7+338,9)/932,5. Tous se recalculent exactement à partir des valeurs affichées dans les tableaux qui les portent.

**[OK] Éléments de mécanisme de l'article 2** — effet « boule de neige », pyramide en « toupie », recomposition hommes-femmes du grand âge (38 % → 44 % pour les 80 ans et plus ; 15 % → 30 % pour les centenaires), « 7 des 27 pays » à solde naturel positif en 2024 contre 16 dix ans plus tôt, +308 000 → −343 000 en un siècle : tous retrouvés littéralement dans `collecte/01-demographie.md`, elle-même intégralement rouverte et confrontée au texte primaire par `verifications/01-demographie.md` (« aucun `EXTRAIT : non lu`… toutes les citations recopiées correspondent mot pour mot au texte source »). Ce blanc-seing méthodologique, propre à ce seul rapport de vérification, couvre l'ensemble de la fiche de collecte démographie — ce qui n'est pas le cas des rapports santé et protection sociale, bornés à une liste fermée de chiffres.

**[OK] Répartition des 45,8 % / 43 % (risque vieillesse-survie)** — le texte expose correctement l'erreur de dénominateur de la source DREES et publie la valeur recalculée (45,8 %), conformément au verdict de `verifications/03-protection-sociale-retraites.md`.

**[OK] Pluralité des trois valeurs de part du PIB pour les retraites (13,1 / 13,9 / 14,6 %)** — champs et millésimes exposés fidèlement, avec l'élément de réconciliation (92 %) repris tel que validé par `verifications/03-protection-sociale-retraites.md`.

**[OK] Répartition des quatre principales ALD (27,1 / 21,4 / 15,5 / 9,9 %)** — le texte publie la version du tableau 3, écarte explicitement la version du texte courant (32/27/19/12 %), conformément au verdict `[ERREUR]` de `verifications/04-sante-ald-et-depenses.md`.

---

## Ce qui n'a pas été recontrôlé

Conformément au budget (6 publications maximum, doute-déclenché) : je n'ai pas rouvert le rapport DREES *Les retraités et les retraites* ni le rapport COR pour la section retraites de l'article 4, ni la publication Eurostat/Destatis/ISTAT de l'article 1 — ces sources ont déjà été rouvertes et confrontées ligne à ligne par `verifications/01-demographie.md` et `verifications/03-protection-sociale-retraites.md`, et le texte développé n'en modifie pas la teneur. Je n'ai pas non plus tenté une seconde fois d'accéder au *Points de repère* n° 54 de la CNAM (déjà signalé bloqué à deux reprises). Sur les cinq valeurs signalées « niveau de confiance mal déclaré » ci-dessus, je n'ai rouvert aucune source supplémentaire au-delà de ce qui figure déjà en `collecte/` : leur exactitude n'est donc pas mise en doute, seul leur marquage l'est.

---

## VERDICT GLOBAL : PUBLIABLE APRÈS CORRECTIONS

Bloquant :

1. Retrouver la source du taux « santé de 4,0 % » (article 4) et l'ajouter à la collecte, ou a minima la citer en note — le chiffre s'avère exact (DREES, tableau 2) mais n'était traçable par aucun document du dépôt avant cette vérification.
2. Ajouter la mention « (niveau collecté) » aux cinq valeurs listées : 256 320 (ALD 12, article 3) ; 381,6/45,1 Md€ (vieillesse/survie, article 4) ; 82 % / 278 Md€ / 9,5 % du PIB (sous-risque maladie, article 4) ; 16,3 millions résidant en France (article 4) ; 4,4 millions de pensions de réversion / 87 % / 884 000 (article 4).

Non bloquant :

3. Ne pas attribuer nommément au rapport IGAS/IGF le mot « résiduel » (ALD 12, article 3) tant que la citation exacte n'est pas retrouvée — écrire « effectif résiduel » sans attribution, ou retrouver la citation.
4. Corriger « le dispositif date de 1945 » en « 1947 » (année de création de l'ALD à la création de la Sécurité sociale), en distinguant de la date des quatre pathologies d'origine (1945).

Aucun de ces points ne remet en cause la fiabilité d'ensemble des articles 1 à 4 : les corrections nécessaires sont de traçabilité et de marquage, pas de fond. Aucun chiffre substantiellement faux n'a été trouvé dans le périmètre contrôlé.
