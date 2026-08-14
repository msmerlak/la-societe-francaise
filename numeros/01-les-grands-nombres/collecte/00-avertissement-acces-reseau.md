# ⚠️ Avertissement — cette collecte n'a pas eu accès aux sources primaires

**Date de la collecte** : 14 août 2026.
**Statut** : matière de travail. **Aucun chiffre de ces dix rapports n'est publiable en l'état.**

## Ce qui s'est passé

Les dix rapports de ce dossier ont été produits dans un environnement dont la politique réseau bloque les domaines institutionnels dont le magazine dépend : `insee.fr`, `santepubliquefrance.fr`, `drees.solidarites-sante.gouv.fr`, `ec.europa.eu`, `ameli.fr`, `onisr.securite-routiere.gouv.fr`, `citepa.org`, `education.gouv.fr`, `ccomptes.fr`, entre autres. Le proxy d'egress refuse la connexion (`EGRESS_BLOCKED`), pour la recherche web comme pour le téléchargement direct.

Les journalistes ont donc travaillé sur des **relais secondaires** : dépêches, synthèses de presse, extraits de moteurs de recherche. C'est exactement ce que la règle 1 du `CLAUDE.md` interdit.

## Ce que cela implique, concrètement

- Un chiffre de ces rapports peut être exact et rester **non sourcé au sens du magazine** : le relais qui le cite n'est pas la publication qui le porte.
- Le champ `EXTRAIT` est **peu fiable dans ce lot**. Certains contiennent une citation réelle reprise d'un communiqué, d'autres une paraphrase ou un commentaire glissé dans le champ, un autre encore une citation traduite depuis la version anglaise d'une page de presse. Quatre rapports ne portent aucun `EXTRAIT : non lu` alors que leur agent signalait des blocages — leur discipline de citation est à reprendre entièrement.
- Les **millésimes** sont le point le plus exposé : c'est précisément ce que les relais de presse escamotent. Plusieurs valeurs de ce lot sont probablement rattachées à la mauvaise année de mesure.
- Les **champs statistiques** (tous régimes / régime général, France entière / métropole, provisoire / définitif) ont été relevés de mémoire ou par déduction dans une partie des fiches.

## Ce à quoi cette collecte sert quand même

Elle est conservée, conformément au principe du dépôt : un rapport dont les pistes n'ont pas abouti dit au suivant où l'on a déjà cherché. Sa valeur ici est celle d'une **carte** :

- quelle institution publie quoi, sous quel titre et à quelle fréquence ;
- quelles références précises aller ouvrir en priorité ;
- où sont les controverses méthodologiques à instruire (estimation de la mortalité attribuable à l'alcool, écart entre comptage ALD et cartographie des pathologies, faits enregistrés contre enquêtes de victimation) ;
- les pistes non abouties, listées par chaque rapport.

## Ce qu'il faut faire avant d'en publier une ligne

1. Ouvrir l'accès réseau aux domaines institutionnels dans la configuration de l'environnement.
2. Relancer les journalistes, en leur demandant de **rouvrir chaque publication** et de remplir `EXTRAIT` par citation littérale, ou d'écrire `EXTRAIT : non lu`.
3. Passer le fact-checker sur chaque rapport, avec une attention particulière au contrôle n° 2 (millésime) et au contrôle n° 3 (champ), les deux que ce lot a le plus de chances d'avoir manqués.
4. Seulement ensuite, lancer l'éditeur.
