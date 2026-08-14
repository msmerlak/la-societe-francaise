# ⚠️ Avertissement — le premier lot de collecte n'a pas eu accès aux sources primaires

**Date du lot** : 14 août 2026.
**Statut** : archivé dans `archive-non-sourcee-2026-08/`. **Aucun chiffre de ces dix rapports n'est publiable, ni citable, ni réutilisable en aval.**

## Ce qui s'est passé

Les dix rapports de ce lot ont été produits dans un environnement dont la politique réseau bloquait les domaines institutionnels dont le magazine dépend : `insee.fr`, `santepubliquefrance.fr`, `drees.solidarites-sante.gouv.fr`, `ec.europa.eu`, `ameli.fr`, `onisr.securite-routiere.gouv.fr`, `citepa.org`, `education.gouv.fr`, `ccomptes.fr`, entre autres. Le proxy d'egress refusait la connexion (`EGRESS_BLOCKED`), pour la recherche web comme pour le téléchargement direct.

Les journalistes ont donc travaillé sur des **relais secondaires** : dépêches, synthèses de presse, extraits de moteurs de recherche. C'est exactement ce que la règle 1 du `CLAUDE.md` interdit.

## Ce que cela implique, concrètement

- Un chiffre de ces rapports peut être exact et rester **non sourcé au sens du magazine** : le relais qui le cite n'est pas la publication qui le porte.
- Le champ `EXTRAIT` est **peu fiable dans ce lot**. Certains contiennent une citation réelle reprise d'un communiqué, d'autres une paraphrase ou un commentaire glissé dans le champ, un autre encore une citation traduite depuis la version anglaise d'une page de presse. Quatre rapports ne portent aucun `EXTRAIT : non lu` alors que leur agent signalait des blocages — leur discipline de citation est à reprendre entièrement.
- Les **millésimes** sont le point le plus exposé : c'est précisément ce que les relais de presse escamotent. Plusieurs valeurs de ce lot sont probablement rattachées à la mauvaise année de mesure.
- Les **champs statistiques** (tous régimes / régime général, France entière / métropole, provisoire / définitif) ont été relevés de mémoire ou par déduction dans une partie des fiches.

## Ce à quoi ce lot sert quand même

Il est conservé, conformément au principe du dépôt : un rapport dont les pistes n'ont pas abouti dit au suivant où l'on a déjà cherché. Sa valeur est celle d'une **carte**, jamais celle d'une source :

- quelle institution publie quoi, sous quel titre et à quelle fréquence ;
- quelles références précises aller ouvrir en priorité ;
- où sont les controverses méthodologiques à instruire (estimation de la mortalité attribuable à l'alcool, écart entre comptage ALD et cartographie des pathologies, faits enregistrés contre enquêtes de victimation) ;
- les pistes non abouties, listées par chaque rapport.

## Ce qui a été fait ensuite

L'accès réseau aux domaines institutionnels a été rétabli. La chaîne a été **relancée intégralement le 14 août 2026** :

1. Le lot non sourcé a été déplacé dans `archive-non-sourcee-2026-08/` — il ne devait plus occuper les noms de fichiers canoniques, où un lecteur pressé l'aurait pris pour de la matière utilisable.
2. Douze journalistes ont été relancés sur les briefs de `00-briefs-a-relancer.md`, avec consigne de rouvrir chaque publication et de ne remplir `EXTRAIT` que par citation littérale, ou d'écrire `non lu`.
3. Les rapports du nouveau lot occupent les noms canoniques `01-*.md` à `12-*.md` de ce dossier.
4. Le fact-checker est passé sur chaque rapport, puis sur le numéro assemblé.

**Règle de lecture** : tout chiffre du n° 1 se trace vers le nouveau lot. Le dossier `archive-non-sourcee-2026-08/` est une archive de travail, sans valeur probante.
