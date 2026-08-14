# La société française — magazine quantitatif

## Ce qu'est ce projet

Magazine en ligne (site + newsletter) qui brosse un **portrait quantitatif et pertinent de la société française**, à partir de sources publiques primaires.

Langue de publication : **français**. Tout le contenu, les noms de fichiers et les messages de commit sont en français.

Une exception, et une seule : **le code porte des noms de modules en anglais** (`site/build.py`, `render.py`, `checks.py`), selon l'usage de la programmation. La frontière est celle du lectorat — ce qu'un lecteur voit est en français, ce qui fabrique le site est nommé comme du code.

## Ce qui est constant, ce qui varie

C'est la distinction la plus importante de ce fichier.

**Constant** — l'exigence de méthode : sources publiques primaires, millésime toujours donné, champ statistique toujours contrôlé, aucun chiffre non vérifié, aucune addition abusive, style déclaratif, typographie française, chaîne de production à trois agents. Ces règles valent pour tout numéro, quel que soit son sujet.

**Variable** — le **dispositif** d'un numéro : son angle, sa question, sa façon de hiérarchiser, ses rubriques, ses éventuels indices ou barèmes, la forme de ses entrées. Chaque numéro invente le sien en fonction de ce qu'il veut montrer, et le documente dans son propre `dispositif.md`.

Le n° 1, *Les grands nombres de la société française*, enquête sur l'écart entre le poids réel d'un phénomène et son poids médiatique. Il a produit pour cela un appareil qui lui est propre : quatre critères de classement, un indice de sous-exposition, un top 10, une rubrique de contre-paniques. **Rien de tout cela n'est la norme de la maison** — c'est la réponse d'un numéro à sa question. Un numéro sur les mobilités, les héritages ou le temps libre n'a aucune raison de reprendre cet appareil, et probablement tort de le faire.

Ne jamais transposer le dispositif d'un numéro à un autre par défaut. Le lire comme précédent, oui ; le reconduire sans l'avoir rejustifié, non.

---

## Règles non négociables

Ces règles priment sur toute considération de style ou de fluidité, et s'appliquent à tous les numéros.

1. **Aucun chiffre sans source primaire nommée.** Institution + titre exact de la publication + date de publication. Jamais « selon une étude », jamais un média secondaire comme source. Producteurs de référence : INSEE, DREES, Santé publique France, CNAM, CépiDc-Inserm, DARES, DEPP, SSMSI, ONISR, Citepa, ANSES, IGAS/IGF, Cour des comptes, AFT, Eurostat, OCDE, observatoires et commissions publiques. Un rapport d'association ou de fondation est admis quand il est la seule source existante sur son objet — et il est alors signalé comme tel.
2. **Millésime ≠ date de publication.** Toujours indiquer l'année de mesure. L'écart est couramment de 2 à 4 ans. Écrire « 41 000 décès (données 2015, publiées 2019) », pas « 41 000 décès ».
3. **Ne jamais additionner ce qui se recouvre.** Les fractions attribuables, les populations et les catégories administratives se chevauchent (un fumeur qui boit et habite un boulevard est compté dans trois estimations de mortalité). Tout tableau concerné porte la mention « périmètres partiellement recouvrants — ces chiffres ne s'additionnent pas ».
4. **Distinguer la mesure de la chose mesurée.** Un comptage administratif n'est pas une prévalence, un fait enregistré n'est pas un fait commis, une estimation modélisée n'est pas un dénombrement, une déclaration n'est pas une observation. Le glissement est une erreur de fond même quand le nombre est exact.
5. **Exposer les chiffres contestés comme contestés.** Quand une estimation fait l'objet d'un débat méthodologique documenté, donner les ordres de grandeur en présence et dire ce qui change — et ce qui ne change pas — selon celui qu'on retient.
6. **Chercher activement ce qui contredit l'angle.** Un numéro qui documente des dégradations va chercher les améliorations, et inversement. C'est ce qui sépare le portrait quantitatif du réquisitoire illustré de chiffres. La forme que prend cette contradiction dans le texte relève du dispositif du numéro ; l'obligation de la chercher, non.
7. **Jamais de chiffre inventé, extrapolé ou « de mémoire ».** En cas de doute, vérifier la source ou ne pas publier le chiffre. Un chiffre repris d'un numéro antérieur est **revalidé** avant réutilisation : le millésime a pu changer.
8. **Pas d'arrondi silencieux.** « ~9 560 € », « de l'ordre de 100 000 à 150 000 », « ≈ 20/an en moyenne 2012-2025 » : la précision affichée doit refléter la précision disponible.

---

## Forme d'un numéro

Le squelette ci-dessous est le minimum commun à tous les numéros. Tout le reste — l'organisation du corps, les rubriques, les gabarits d'entrée — appartient au dispositif du numéro.

1. **Titre + chapô.** Le sous-titre annonce l'angle. Le chapô, en italique, donne l'état des données, la nature des sources et l'avertissement sur les millésimes.
2. **Méthode.** Comment ce numéro a été construit : ce qu'il compare, comment il hiérarchise s'il hiérarchise, ce qu'il écarte et pourquoi, et les avertissements de lecture propres à son matériau. Section brève mais jamais omise — un numéro quantitatif qui ne dit pas comment il s'y est pris demande au lecteur de le croire sur parole.
3. **Le corps.** Structure libre, propre au numéro.
4. **Sources primaires.** Regroupées par domaine, référence complète, en fin de numéro.
5. **Avertissement de clôture**, en italique : ce que le texte n'a pas reproduit (intervalles de confiance, marges d'erreur) et renvoi aux publications sources.

### Le dispositif d'un numéro

Chaque numéro documente le sien dans `numeros/NN-slug/dispositif.md`, écrit **avant** le numéro : sa question, son angle, sa méthode de sélection et de hiérarchisation, ses rubriques, ses conventions propres (barèmes, symboles, gabarits d'entrée). C'est ce fichier que l'éditeur applique — le CLAUDE.md ne lui donne que les invariants.

Un dispositif hérite librement d'un numéro antérieur, à condition de le dire et de rejustifier ce qu'il reprend.

---

## Style

Ces traits définissent la voix du magazine et ne varient pas d'un numéro à l'autre.

- **Le tableau porte les données, le texte porte l'argument.** Ne jamais paraphraser en prose un tableau qu'on vient de donner.
- **Ancrer par le ratio.** Un grand nombre isolé ne dit rien. Sa comparaison — à une autre grandeur, à la même série vingt ans plus tôt, au même phénomène chez les voisins européens — est ce qui le rend lisible.
- **Phrases déclaratives, pas d'emphase rhétorique.** Les chiffres suffisent. Pas de point d'exclamation, pas d'indignation explicite, pas d'appel à l'action.
- **Pas de conseil, pas de prescription politique.** Le magazine décrit des ordres de grandeur, des évolutions et des écarts entre objectif affiché et résultat mesuré. Il ne recommande pas de politique.
- **Expliquer, pas accuser.** Ce qu'un numéro met au jour s'explique par des mécanismes — structures, incitations, biais de perception, inerties institutionnelles — jamais par la faute morale d'un groupe ni par un complot.
- **Neutralité sur les personnes.** Pronoms neutres quand le genre n'est pas connu ou pertinent.

### Typographie française

- Guillemets français avec espaces insécables : « comme ceci ».
- Espace insécable avant `: ; ! ?` et `%`, et entre nombre et unité : `5,1 % du PIB`, `932,5 Md€`, `3 515 tués`.
- Séparateur de milliers : espace insécable. Décimale : virgule. `13,8 millions`, `1 337 €`.
- Signe moins typographique `−` pour les valeurs négatives et les baisses (`−6 000`, `−24 %`), tiret cadratin `—` pour l'incise.
- Multiplication : `×3 400`. Ordinaux en exposant : `1ᵉʳ`, `2ᵉ`, `31ᵉ`. Unités : `Md€`, `M€`, `Mt CO₂e`, `PM2,5`, `NO₂`.
- Titres de publications en italique : *Bilan démographique 2025*.

---

## La chaîne de production

Trois agents dédiés se partagent le travail (`.claude/agents/`). La séparation est délibérée : celui qui collecte ne juge pas, celui qui juge ne réécrit pas, celui qui écrit n'invente aucun chiffre.

| Agent | Modèle | Rôle | Sa sortie est classée dans |
|---|---|---|---|
| **journaliste** | Sonnet | ratisse les sources publiques primaires, relève valeur + millésime + champ + référence, rapporte aussi ses pistes non abouties | `collecte/NN-theme.md` |
| **fact-checker** | Sonnet | rouvre chaque source, applique sept contrôles (existence, millésime, champ, cohérence, additivité, nature de la mesure, contestation), rend un verdict par chiffre | `verifications/NN-theme.md` |
| **editeur** | Opus | fixe le dispositif, hiérarchise, ancre par les ratios, applique les verdicts, assemble le numéro | `dispositif.md` et `index.md` — seul à y écrire |

Le modèle croît avec l'irréversibilité de la décision, et l'assemblage est ce qui engage le numéro. Mais la collecte n'est pas pour autant le maillon où économiser : elle est l'entrée de tout le reste, et **le fact-checker ne rattrape que ce qu'on lui présente**. Un chiffre qu'un journaliste n'a pas trouvé, une controverse qu'il n'a pas repérée, un contre-exemple qu'il n'est pas allé chercher ne sont vus par personne en aval — le contrôle porte sur ce qui est écrit, jamais sur ce qui manque.

C'est ce qui a fait passer le journaliste de Haiku à Sonnet, après la première collecte du n° 1 (août 2026). Le motif n'est pas l'exactitude — le fact-checker la couvre — mais **la couverture et l'honnêteté sur les lacunes** : un journaliste rapide s'arrête dès qu'il tient une réponse plausible, épuise son budget de recherche sans le répartir, et remplit le champ `EXTRAIT` par une paraphrase plutôt que d'écrire `non lu`. Cette dernière défaillance est la plus coûteuse, parce qu'elle est **silencieuse** : elle donne à une collecte non sourcée l'apparence d'une collecte sourcée.

Reste le principe : **le fact-checker n'est pas une formalité, c'est le filet du journaliste.** Le contrôle n° 3 rattrape les relevés de champ approximatifs, quel que soit le modèle qui les a produits.

Les frontmatters portent les alias `sonnet` / `opus`, pas des identifiants figés : le dépôt suit ainsi les montées de version sans intervention. Au moment où ce choix a été fait (août 2026), ils désignaient Sonnet 5 et Opus 5. Ce qui compte est le rang relatif, pas la génération — si un jour la collecte doit être épinglée pour reproduire un numéro à l'identique, c'est une décision de numéro, pas de dépôt.

Le journaliste dépose lui-même sa collecte, le fact-checker ses verdicts dans `verifications/` **et nulle part ailleurs**. Ni l'un ni l'autre ne peut écrire dans `index.md`, et le fact-checker ne peut toucher ni `collecte/` ni `dispositif.md` : il ne corrige jamais ce qu'il contrôle. La séparation tient à ce périmètre d'écriture, pas à l'absence d'outil.

Le fact-checker **dépose au fil de l'eau**, thème par thème, sans attendre d'avoir tout fini. Ce n'est pas une commodité : une session interrompue emporte tout ce qui n'est pas sur disque. Le n° 1 a perdu dix vérifications de cette façon — coût engagé, sortie nulle, aucune reprise possible parce que le travail vivait dans le contexte de l'agent.

**Ordre d'intervention** : dispositif → journaliste (passe large) → **triage éditorial** → journaliste (passe profonde, sur les seuls thèmes retenus) → fact-checker (sur la sélection) → editeur → fact-checker (passe finale sur le texte assemblé) → publication.

Un verdict `NON PUBLIABLE` bloque ; un chiffre `[NON VÉRIFIÉ]` est retiré ou renvoyé au journaliste, jamais publié au pari.

Le journaliste peut être lancé en plusieurs exemplaires en parallèle sur des thèmes distincts. Le fact-checker aussi.

### Le budget d'un agent se borne dans son brief

Ce que coûte un agent ne dépend presque pas du modèle ni du nombre de recherches : il dépend de **ce qui entre dans son contexte**. Sur le n° 1, un journaliste a consommé cinq fois plus qu'un autre pour un brief de même structure, et l'agent le plus dépensier n'était pas celui qui avait fait le plus de recherches — c'était celui qui avait téléchargé le plus de PDF entiers.

Deux règles en découlent.

**Borner la lecture, pas la recherche.** Un brief dit combien de publications ouvrir, et demande à l'agent de **déclarer ce qu'il a laissé de côté** quand il atteint la borne. On lit la section qui porte le chiffre, pas le rapport de 458 pages. Un agent sans borne dépense jusqu'à ce que sa tâche lui paraisse finie, et ce seuil varie énormément d'un thème à l'autre.

**Ne pas créer un agent pour trois chiffres.** L'amorçage — lire le CLAUDE.md, le dispositif, la collecte du thème — coûte de l'ordre de 80 000 à 100 000 tokens avant tout travail utile. Sur le n° 1, une revérification portant sur quatre chiffres a coûté autant que la passe finale sur le numéro entier. En dessous d'une quinzaine de chiffres à traiter, grouper avec un thème voisin plutôt que lancer un agent dédié.

### Le triage précède la vérification

C'est la règle qui gouverne le coût de la chaîne, et elle a été apprise à la dure : le n° 1 a fait vérifier 270 fiches pour en publier une soixantaine. Quatre fois trop, parce que la vérification est passée avant qu'on sache ce qui serait publié.

**Ne jamais vérifier ce qui n'est pas encore retenu.** L'éditeur trie d'abord sur la collecte brute, puis le fact-checker travaille sur la sélection. Le triage porte sur **une fois et demie** ce que le numéro publiera : la marge est la réserve dans laquelle on puise quand une entrée s'effondre à la vérification. Une entrée qui s'effondre est remplacée par la réserve, jamais repêchée.

Le risque est réel et assumé : l'éditeur trie sur du non vérifié, et peut retenir une entrée qui ne tiendra pas. C'est précisément ce que la réserve absorbe. Le risque inverse — vérifier tout pour n'en publier qu'un quart — coûte quatre fois plus cher pour la même sortie.

### Deux vitesses de collecte

**Passe large** : sur tous les thèmes envisagés, 2 à 3 recherches chacun. Objectif : savoir ce qui existe, à quel ordre de grandeur, sous quel titre. Pas d'ouverture de PDF, pas de citation littérale. Une passe large qui produit des fiches complètes a dépensé le budget de la passe profonde.

**Passe profonde** : sur les seuls thèmes retenus au triage. C'est là qu'on ouvre les publications, qu'on recopie les extraits et qu'on relève les champs.

### Deux niveaux de confiance, déclarés au lecteur

Tout ce qu'un numéro publie n'a pas à être vérifié au même degré, à condition que la différence soit dite.

| Niveau | Ce qu'il exige | Ce qu'il permet |
|---|---|---|
| **Vérifié** | source primaire rouverte par le fact-checker | les entrées de tête du numéro |
| **Collecté** | fiche du journaliste, extrait littéral, non recontrôlé | les entrées secondaires, si le numéro annonce ce niveau |

Un numéro qui emploie le second niveau le déclare dans sa section « Méthode ». Ce qui reste interdit sans condition : publier une valeur dont personne n'a ouvert la source, quel que soit le niveau affiché.

### Ce qui circule entre les étages

Le journaliste rend des **fiches**, jamais de la prose rédigée. Deux champs sont obligatoires et séparés :

- `MILLÉSIME` — l'année de mesure ;
- `PUBLIÉ EN` — l'année de parution.

Les remplir tous les deux oblige à constater qu'ils diffèrent. C'est la parade structurelle à la confusion millésime/publication, qui est l'erreur la plus fréquente du magazine et la moins visible.

Le champ `NATURE` est une énumération fermée : `comptage exhaustif` | `enregistrement administratif` | `estimation modélisée` | `enquête déclarative`. Il rend la non-additivité contrôlable autrement que par la vigilance : deux estimations modélisées ne s'additionnent jamais, et la règle peut être appliquée sans relire l'argument.

`URL` provient toujours d'un résultat d'outil. Jamais reconstruite de mémoire, jamais déduite d'un motif d'URL.

---

## Organisation du dépôt

**Un dossier par numéro.** Le texte publié n'est que la pointe : le dispositif, la matière collectée et les vérifications restent avec lui, pour que tout chiffre reste traçable jusqu'à sa source des mois après la parution.

```
numeros/
  01-les-grands-nombres/
    dispositif.md       angle, méthode et conventions propres à ce numéro
    triage.md           sélection de l'éditeur : ce qui part en vérification, et la réserve
    index.md            le numéro publié — seul fichier diffusé
    collecte/           rapports du journaliste : matière brute sourcée
      NN-theme.md
    verifications/      rapports du fact-checker : verdicts par chiffre
      NN-theme.md
    media/              graphiques et images, si le numéro en a (optionnel)
site/                   générateur du site et de la newsletter — voir site/README.md
  build.py              construit public/ à partir des index.md ; --controler pour vérifier
  render.py             Markdown → HTML, sous-ensemble autorisé par les contraintes de diffusion
  checks.py             typographie, contraintes de diffusion, squelette du numéro
.claude/agents/         journaliste, fact-checker, editeur
CLAUDE.md               ce fichier — les invariants du magazine
```

Le générateur ne publie que les `index.md` : le `dispositif.md`, la `collecte/` et les `verifications/` lui sont invisibles par construction. `python3 site/build.py --controler` rend exécutable la partie mécanique de la liste de vérification ci-dessous — typographie, tableaux à trois colonnes, absence de HTML, émojis déclarés au dispositif. Il ne vérifie aucun chiffre : c'est le fact-checker, et rien d'autre, qui les vérifie.

Toute autre arborescence (scripts de collecte, gabarits d'envoi) est à créer au moment où elle sert, pas par anticipation.

**Nommage** : dossier `NN-slug/` — numérotation sur deux chiffres, slug en minuscules sans accents. Le fichier publié s'appelle toujours `index.md`, quel que soit le numéro.

**Ce qui est diffusé** : `index.md` uniquement. `dispositif.md`, `triage.md`, `collecte/` et `verifications/` sont des archives de travail — versionnées, jamais publiées, jamais élaguées. Cette règle est appliquée par construction : le site est servi depuis la branche `gh-pages`, qui ne contient que le résultat de `site/build.py` et aucun fichier source. Un rapport de collecte dont les pistes n'ont pas abouti se garde : il dit au numéro suivant où l'on a déjà cherché.

**Réutiliser un chiffre d'un numéro antérieur** se fait en repartant de son `verifications/`, pas de son `index.md` — et en revalidant le millésime, qui a pu changer depuis.

**Commits** : en français, à l'impératif, portée en préfixe — `n°1 : corrige le millésime des données ALD`, `méthode : ajoute la règle de non-additivité`.

**Branches** : développer sur une branche dédiée, jamais de push direct sur la branche par défaut.

---

## Travailler sur un numéro

**Ouvrir un numéro** : créer `numeros/NN-slug/` et y écrire `dispositif.md` avant toute collecte. Un numéro dont l'angle n'est pas écrit produit une collecte sans critère d'arrêt.

**Ajouter ou modifier un chiffre** — le circuit est toujours le même :

1. Aller à la publication primaire (site de l'institution), pas à un article de presse qui la cite.
2. Relever : valeur, millésime, champ (France entière ou métropole ? tous régimes ou régime général ? ménages ordinaires ou population totale ? effectif ou taux ? euros courants ou constants ?), date de publication, référence exacte.
3. Vérifier que le champ est compatible avec les autres chiffres du même tableau. **Les changements de champ sont la première cause d'erreur** : le *Points de repère* CNAM raisonne tous régimes / France entière, la série open data annuelle porte sur le seul régime général — les deux ne sont pas superposables.
4. Ajouter la ligne au tableau **et** la référence en « Sources primaires ».

**Mettre à jour un numéro publié** : préférer la mise à jour explicite (« données 2023, actualisées en juin 2026 ») à la réécriture silencieuse. La date d'état des données en chapô doit être mise à jour en même temps.

**Vérification avant publication** :

- [ ] chaque chiffre a un millésime et une source primaire listée en fin de numéro
- [ ] aucun total obtenu en additionnant des estimations ou des populations qui se recouvrent
- [ ] les champs statistiques sont homogènes à l'intérieur de chaque tableau
- [ ] les comptages administratifs et les estimations modélisées sont signalés comme tels
- [ ] les estimations contestées présentent la contestation
- [ ] le numéro est allé chercher ce qui contredit son angle
- [ ] tous les ratios affichés se recalculent à partir des valeurs données
- [ ] typographie française vérifiée (insécables, guillemets, `−`, ordinaux)
- [ ] les conventions propres du `dispositif.md` sont respectées de bout en bout

---

## Contraintes de diffusion

Le même Markdown sert le site et la newsletter. Conséquences pratiques :

- **Les tableaux larges passent mal en e-mail.** Trois colonnes maximum ; au-delà, scinder en deux tableaux.
- **Pas de HTML brut, pas de CSS, pas de JavaScript** dans les fichiers de numéros — Markdown standard uniquement, pour rester portable entre le générateur de site et la plateforme d'envoi.
- **Les émojis, quand un dispositif en emploie, sont porteurs de sens**, pas décoratifs, et doivent rester lisibles en texte brut. Aucun émoji hors de ceux que le dispositif définit.
- **Pas d'image indispensable à la compréhension** : un numéro doit se lire intégralement en texte.
