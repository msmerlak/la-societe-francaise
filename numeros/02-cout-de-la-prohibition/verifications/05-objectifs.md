# Vérification — 05. Objectifs des plans et grandeurs manquantes

## Avertissement préalable — limite technique rencontrée dans cette passe

**Je dois le dire avant tout verdict, parce qu'il conditionne la lecture de tout ce qui suit.** Sur les six publications que je comptais rouvrir en priorité, quatre sont des PDF hébergés soit sur `ccomptes.fr`, soit sur `drogues.gouv.fr` / `assemblee-nationale.fr`. Pour toutes, la récupération du texte a échoué :

- **`ccomptes.fr` renvoie une erreur 503 sur toutes mes tentatives**, exactement comme le signale le journaliste. Le mirroir `web.archive.org` qui lui avait permis d'y accéder m'est **inaccessible dans cette session** (« Claude Code is unable to fetch from web.archive.org » — blocage au niveau de l'outil, pas une erreur de contenu). J'ai aussi tenté un proxy de lecture tiers (r.jina.ai) : échec (422).
- **Les PDF de `drogues.gouv.fr` et `assemblee-nationale.fr` (SIMCA, bilan PNMA, DPT 2026) ont été récupérés (contenu binaire sauvegardé) mais leur texte n'a pas pu être extrait** par mon outil de lecture web — il ne renvoie que la structure PDF compressée, pas le texte. Je n'ai pas non plus de lecteur PDF local disponible (`pdftoppm`/poppler absent) pour rouvrir les fichiers binaires sauvegardés.
- J'ai tenté des contournements (visionneuse Google Docs, miroirs alternatifs sur `budget.gouv.fr` et `bdoc.ofdt.fr`) : échecs (403 ou même blocage d'extraction).
- **Seules les pages HTML se sont laissées lire normalement** : la question écrite Assemblée nationale (fichier 06) et la page de série statistique OFDT s'ouvrent sans problème.

Conséquence : pour les chiffres sourcés exclusivement dans un PDF (l'essentiel de ce thème), je n'ai **pas pu rouvrir moi-même la publication primaire** dans cette session, malgré des tentatives répétées. Ce n'est pas un jugement sur la collecte — dont les extraits sont précis, paginés et cohérents en interne — mais je ne peux, par construction de mon métier, valider `[OK]` un chiffre que je n'ai pas retrouvé de mes propres yeux dans la source. Je marque donc ces chiffres `[NON VÉRIFIÉ — accès source primaire impossible dans cette session]`, avec le niveau de corroboration indirecte que j'ai pu rassembler (recherche web, cohérence arithmétique interne à la fiche), qui n'équivaut pas à une lecture directe.

**Recommandation à l'éditeur** : une repasse de vérification avec un accès PDF fonctionnel est nécessaire avant de considérer ces entrées comme `[Vérifié]` au sens de la section 9 du dispositif. En l'état, elles ne peuvent être publiées qu'au niveau `[Collecté]`, ou différées.

---

## 1. Les constats d'absence (priorité la plus haute du brief)

### [NON VÉRIFIÉ — accès impossible] SIMCA 2023-2027 — aucune cible chiffrée (fiche B1)
**Attendu** : retrouver dans le PDF de la SIMCA, p. 25, section « Les objectifs cibles », les six énoncés cités par la collecte, et confirmer qu'aucun n'est chiffré.
**Constaté** : PDF illisible par mes outils dans cette session (voir avertissement). Recherche web : un article de presse spécialisée (Santé Mentale) résume les orientations de la SIMCA dans des termes qualitatifs proches de la citation de la collecte, sans chiffre — corroboration indirecte, pas une lecture primaire.
**Point de vigilance résolu** : une page officielle (`drogues.gouv.fr`) associée à la SIMCA mentionne un objectif « génération sans tabac d'ici 2032 ». Recherche complémentaire : ce chiffre appartient au **Programme national de lutte contre le tabac (PNLT) 2023-2027**, un plan distinct de la SIMCA elle-même, lancé en parallèle. Le PNLT et le tabac sont hors périmètre de ce numéro (section 10 du dispositif — « écarté par périmètre »). Cette piste ne contredit donc pas B1, mais je ne peux pas confirmer par lecture directe que la section « objectifs cibles » de la SIMCA (p. 25) elle-même ne contient aucun chiffre.
**Statut** : non vérifié par moi ; corroboration indirecte favorable ; à reconfirmer par lecture directe avant publication au niveau vérifié.

### [NON VÉRIFIÉ — accès impossible] Cour des comptes, RPA 2025 — « sans que des cibles chiffrées ne soient mentionnées » (fiche D1)
**Attendu** : retrouver littéralement cette phrase p. 85 du chapitre « Les addictions des jeunes aux drogues illicites et à l'alcool ».
**Constaté** : `ccomptes.fr` en 503, `web.archive.org` bloqué pour mon outil. Une recherche web ciblée sur la phrase exacte renvoie le document `ccomptes.fr` correspondant comme résultat principal (indexation Google confirmant la présence du texte dans ce document précis), et plusieurs relais de presse indépendants (Public Sénat, Europe1, Santé Mentale, France 24) rapportent la même conclusion de la Cour dans des termes convergents.
**Statut** : non vérifié par lecture directe ; corroboration indirecte forte (indexation + convergence de plusieurs relais indépendants) ; à reconfirmer par lecture directe.

### [NON VÉRIFIÉ — accès impossible] Suivi du plan antistupéfiants interrompu à l'été 2022 (fiche C1), sur le rapport complet
**Attendu** : retrouver le passage p. 69 et p. 84 du rapport complet S2024-1295 (pas la seule note aux rédactions), avec le double datage « mai 2022 » / « juin 2022 » relevé par la collecte.
**Constaté** : `ccomptes.fr` en 503 sur le rapport complet **et** sur la note aux rédactions séparément testée. Recherche web : plusieurs médias indépendants (Public Sénat, Europe1, aefinfo) rapportent le même fait — suivi interrompu à l'été 2022, changement de Premier ministre — de façon convergente, cohérent avec l'attribution à ce rapport précis.
**Statut** : non vérifié par lecture directe du rapport complet, contrairement à l'exigence du brief. Corroboration indirecte forte, mais **je n'ai pas pu personnellement confirmer le double datage interne (mai vs juin 2022)** signalé par la collecte comme une incohérence du rapport lui-même — point qui mériterait une relecture directe.

### [OK — confirmé indirectement, existence établie] Document budgétaire consolidant la dépense — le DPT existe (fiche E1)
**Attendu** : confirmer que la collecte a raison contre le pari du triage : un document budgétaire consolidé existe.
**Constaté** : je n'ai pas pu lire le texte du PDF du DPT 2026 lui-même, mais j'ai retrouvé, par recherche, **trois mentions institutionnelles indépendantes** de ce document sous son titre exact « Politique de lutte contre les drogues et les conduites addictives », document de politique transversale annexé au PLF : une sur `budget.gouv.fr` (`file-download/22002`, 403 à l'ouverture mais référencé et indexé), une sur `assemblee-nationale.fr` (le même fichier que la collecte cite), une sur `bdoc.ofdt.fr`. La récurrence documentée sur plusieurs éditions successives (PLF2025 « 10-Orange_Drogues.pdf », PLF2026) confirme qu'il s'agit d'une production **annuelle et institutionnalisée**, pas d'un document isolé.
**Verdict sur l'existence** : `[OK]` — l'existence du document, contredisant le pari du triage, est confirmée par une pluralité de sources institutionnelles indépendantes, même si je n'ai pas lu le corps du texte moi-même.
**Verdict sur le montant total (fiche E2, ≈ 2,5 Md€, détail par exercice)** : `[NON VÉRIFIÉ — accès impossible]`. Je n'ai pas pu relire la ligne « Total » du tableau (2 497 483 527 € / 2 462 642 444 € / 2 505 153 976 € / 2 513 574 412 € / 2 567 591 313 € / 2 591 257 398 €) dans le document lui-même. À reconfirmer.

---

## 2. Les deux cibles chiffrées atteintes — ROSP tabac et alcool (fiches A2, A3)

### [NON VÉRIFIÉ — accès impossible] Cible ROSP tabac > 75 %, résultat 88,1 % (2020) ; cible ROSP alcool > 75 %, résultat 83,8 % (2020)
**Attendu** : retrouver la cible « objectif cible > 75 % » en note 68, p. 58 du plan PNMA 2018-2022, et les résultats (séries déc-17 à déc-20) au tableau « Moyennes objectifs ROSP - RPIB », p. 17 du bilan.
**Constaté** : les deux PDF (plan et bilan) n'ont pas pu être lus par mes outils dans cette session. Je n'ai trouvé **aucune corroboration externe** de ces valeurs précises (88,1 %, 83,8 %, seuil de 75 %) par recherche web — ni confirmation ni contradiction.
**Contrôle que j'ai pu faire sans réouverture** : cohérence interne des deux séries citées par la collecte — tabac 81,2 % → 85,8 % → 88,0 % → 88,1 % (2017-2020), alcool 79,8 % → 81,8 % → 83,9 % → 83,8 % (2017-2020) : progression monotone plausible, pas d'anomalie arithmétique.
**Point à trancher par l'éditeur, indépendamment de la vérification de la valeur** : le brief demande de vérifier que ces cibles portent bien sur ce qu'on leur fait dire — **ce sont des objectifs conventionnels de repérage/intervention brève par les médecins généralistes (ROSP), pas des objectifs de politique des stupéfiants illicites.** Sur ce point précis, je peux me prononcer sans réouverture de la source, à partir du texte même de la fiche : le CHAMP de la fiche A2/A3 dit explicitement « patients tabagiques… consommateurs excessifs d'alcool », et le REGISTRE assigné par la collecte est « recours à un dispositif / activité de service », pas un indicateur de la politique des drogues illicites. **Si le numéro publie ces deux cibles dans la rubrique « ce qui va dans l'autre sens » sans préciser qu'il s'agit d'objectifs tabac/alcool en médecine de ville (ROSP) et non d'objectifs de la politique des stupéfiants illicites, c'est une erreur de fond au sens de la règle 4 du CLAUDE.md — un glissement d'objet.** La collecte elle-même les caractérise correctement (fiche A2 : « c'est le seul appariement cible/résultat du plan… où une valeur numérique cible et un résultat numérique mesuré coexistent »), donc le risque est dans l'écriture du numéro, pas dans la collecte.
**Statut** : valeurs `[NON VÉRIFIÉ]` par manque d'accès ; caractérisation de nature (registre + périmètre tabac/alcool, pas stupéfiants illicites) jugée correcte sur la seule base du texte de la fiche, à faire respecter par l'éditeur au moment de la rédaction.

---

## 3. Autres chiffres du corpus « objectifs » — accès et cohérence

### [NON VÉRIFIÉ — accès impossible] A1. Divergence bilan/plan sur les « cibles à atteindre » du tableau de bord
Non relu. La collecte signale elle-même une divergence entre la formulation du bilan (« cibles à atteindre ») et le contenu réel du tableau (« niveaux de référence » seulement) — c'est exactement le type de tension qu'un fact-checker doit vérifier en priorité, et je ne peux pas le faire dans cette session. À rouvrir en priorité dans une repasse.

### [NON VÉRIFIÉ — accès impossible] A4 à A8 (niveaux de consommation, surdoses, mis en cause/avoirs saisis du bilan PNMA, saisies de cocaïne, constat covid sur la fiabilité de la mesure)
Non relus (même PDF que A2/A3). Contrôle de cohérence interne fait sans réouverture :
- **A6** (mis en cause trafic et avoirs saisis, séries GN+PN) : l'addition GN+PN redonne exactement le total annoncé chaque année (32 461 = 9 144+23 317 ; 33 598 = 8 902+24 696 ; 35 137 = 8 645+26 492 ; 31 079 = 7 900+23 179 ; de même pour les avoirs saisis 645 = 257+388, 484 = 256+228, 573 = 240+333). Aucune anomalie arithmétique décelée dans la fiche.
- **A7** : « +67 % par rapport à 2018 » — 26,5/15,9 ≈ +67 % si la base 2018 est 15,9 t ; la fiche donne une fourchette « 13 à 16 tonnes » pour 2018-2020 sans préciser l'année exacte de la base 2018 utilisée pour le ratio. Le ratio n'est donc pas strictement recalculable avec les seules valeurs données dans la fiche — à vérifier sur pièce (ce n'est pas une erreur constatée, seulement une donnée manquante pour le recalcul).

### [OK — confirmé, corroboration secondaire] Blanchiment 3,5 Md€ attribué au « ministère chargé des finances » (fiche C3)
La collecte marque elle-même ce chiffre `INCERTITUDE` avec l'origine primaire non identifiée. Je n'ai rien trouvé de mieux par recherche : la publication précise du ministère des finances qui produit ce chiffre reste introuvable. **Confirmation du constat de la collecte** : ce chiffre reste `[NON VÉRIFIÉ]` au sens strict — cité au second degré par la Cour des comptes, sans référence primaire nommée, contraire à la règle 1 du CLAUDE.md (« institution + titre exact de la publication »). Ne devrait pas être publié au niveau vérifié en l'état ; publiable seulement en l'attribuant explicitement à la Cour des comptes qui le cite, avec la réserve que la Cour elle-même ne cite pas sa source précise.

### [NON VÉRIFIÉ — accès impossible] C4-C9, D2-D5, F (effectifs Ofast, enquêteurs anti-blanchiment, points de deal, coût 1,8 Md€, recommandation n° 7, recommandations Cour RPA2025, FLCA 130 M€, cibles avoirs saisis DPT)
Non relus, mêmes documents inaccessibles (Cour des comptes, DPT). Un contrôle de cohérence a pu être fait pour C7 : la somme des trois lignes de coût par direction citées (DGPN 793,45 + DGGN 243,71 + DGDDI 754,27 = 1 791,43 M€) est cohérente avec le total de « 1,79 Md€ » cité par la Cour (arrondi à 1,8 Md€ dans le titre de section) — pas d'anomalie arithmétique, bien que la fiche indique elle-même que d'autres lignes existent (le tableau complet n'est pas reproduit intégralement).

---

## Interdits du dispositif — contrôle possible sans réouverture de source

- **Aucun produit coût journalier de détention × effectif écroué** n'apparaît dans cette collecte (elle porte sur les objectifs, pas la répression). `[OK]`.
- **Aucune addition de coût social et dépense publique**, ni de totaux de programmes budgétaires reconstitués par le journaliste : la fiche C7 rapporte le recalcul de la Cour elle-même (1,8 Md€) sans le refaire, et la fiche E2 rapporte le total du DPT sans le recouper avec C7 comme s'ils étaient un seul agrégat — la collecte signale explicitement le risque de double compte (FLCA vs DPT, fiche D5). `[OK]`.
- **Aucune cible qualitative n'a été requalifiée en cible chiffrée** : la fiche F signale elle-même le cas ambigu des cibles DPT « en hausse » sans trancher, et le renvoie à l'éditeur pour arbitrage selon la section 7.3 — conforme à la règle dure du dispositif. `[OK]`.

---

## Ce que je n'ai pas pu contrôler du tout dans cette passe

- La totalité des valeurs sourcées exclusivement dans les quatre PDF suivants : plan PNMA 2018-2022, bilan PNMA octobre 2022, SIMCA 2023-2027, DPT annexé au PLF 2026, et les deux rapports de la Cour des comptes (S2024-1295, RPA 2025) — soit la majorité du corpus de ce thème.
- Le millésime exact de publication du plan PNMA 2018-2022 (12 février 2019, à confirmer) — non recontrôlé.
- La note méthodologique complète du DPT sur les autres axes (recherche, prévention, coordination internationale) — non explorée, comme signalé par la collecte elle-même.

---

## VERDICT GLOBAL — 05. Objectifs

**PUBLIABLE APRÈS CORRECTIONS**, avec un bloquant principal qui n'est pas un défaut de contenu mais un défaut de vérification :

1. **Bloquant.** La quasi-totalité des chiffres de ce thème — y compris les trois constats d'absence de priorité 1 (SIMCA, Cour RPA2025, suivi interrompu C1) et les deux cibles ROSP de priorité 2 — n'a pas pu être relue par moi sur la publication primaire dans cette session, pour une raison d'accès technique (503 persistant sur `ccomptes.fr`, extraction PDF impossible sur les autres). La corroboration indirecte rassemblée (recherche web, cohérence arithmétique interne) est favorable partout où j'ai pu la chercher, mais elle ne vaut pas lecture directe. **Ces entrées ne peuvent pas être publiées au niveau « Vérifié » sur la seule base de cette passe** ; une repasse avec un accès PDF fonctionnel est nécessaire avant publication en tête de numéro.
2. **À trancher par l'éditeur, indépendamment de l'accès source.** Les cibles ROSP (A2/A3) doivent être présentées explicitement comme des objectifs de médecine de ville sur tabac et alcool (ROSP), et non comme des objectifs de la politique des stupéfiants illicites — le glissement serait une erreur de fond au sens de la règle 4 du CLAUDE.md, même si la valeur elle-même s'avère exacte.
3. **Non bloquant.** Le chiffre de blanchiment 3,5 Md€ (fiche C3) reste sans source primaire nommée ; à ne publier qu'attribué explicitement à la Cour des comptes qui le relaie, jamais comme une donnée du ministère des finances directement sourcée.
4. **Aucune erreur de fond constatée** dans les contrôles que j'ai pu mener sans réouverture (cohérence arithmétique des tableaux, respect des interdits d'addition et de requalification du dispositif).
