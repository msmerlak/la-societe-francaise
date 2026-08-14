# La société française — magazine quantitatif

## Ce qu'est ce projet

Magazine en ligne (site + newsletter) qui brosse un **portrait quantitatif de la société française**. Chaque numéro part de sources publiques primaires et cherche les **ordres de grandeur qui déterminent réellement le pays**, indépendamment de leur saillance médiatique.

La ligne éditoriale tient en une phrase : *le poids réel d'un phénomène et son poids médiatique sont deux grandeurs distinctes, et l'écart entre les deux est lui-même un objet d'enquête.*

Langue de publication : **français**. Tout le contenu, les titres de fichiers et les messages de commit sont en français.

---

## Règles non négociables

Ces règles priment sur toute considération de style ou de fluidité.

1. **Aucun chiffre sans source primaire nommée.** Institution + titre exact de la publication + date de publication. Jamais « selon une étude », jamais un média secondaire comme source. Sources admises : INSEE, DREES, Santé publique France, CNAM, CépiDc-Inserm, DARES, DEPP, SSMSI, ONISR, Citepa, ANSES, IGAS/IGF, Cour des comptes, AFT, Eurostat, OCDE, observatoires et commissions publiques (CIIVISE, MIPROF, ONS), rapports d'associations quand ils sont la seule source existante (Fondation pour le logement des défavorisés) — dans ce dernier cas, le signaler.
2. **Millésime ≠ date de publication.** Toujours indiquer l'année de mesure. L'écart est couramment de 2 à 4 ans et c'est un fait éditorial en soi (cf. §6 du n° 1, « le décalage temporel »). Écrire « 41 000 décès (données 2015, publiées 2019) », pas « 41 000 décès ».
3. **Ne jamais additionner des décès attribuables.** Les fractions attribuables se recouvrent (un fumeur qui boit et habite un boulevard est compté trois fois). Tout tableau de facteurs de risque porte la mention « périmètres partiellement recouvrants — ces chiffres ne s'additionnent pas ».
4. **Distinguer comptage administratif et réalité épidémiologique.** 13,8 M de personnes en ALD = 13,8 M *dans un dispositif d'exonération*, pas 13,8 M de malades chroniques. Idem : « faits enregistrés » ≠ « faits commis » ; les séries de délinquance mesurent en partie la propension à porter plainte, les enquêtes de victimation sont plus fiables sur les niveaux, moins sur les tendances courtes.
5. **Exposer les chiffres contestés comme contestés.** Quand une estimation fait l'objet d'un débat méthodologique documenté (mortalité alcool : 41 000 sur volumes vendus vs ~23 000 sur consommation déclarée), donner les deux et dire ce qui change — et ce qui ne change pas — selon l'estimation retenue.
6. **Symétrie obligatoire.** Tout numéro qui documente des dégradations doit chercher activement les améliorations, et inversement. La rubrique « Les faux grands nombres : ce qui va mieux qu'on ne le croit » n'est pas un ornement, c'est la garantie que l'exercice n'est pas un catastrophisme déguisé.
7. **Jamais de chiffre inventé, extrapolé ou « de mémoire ».** En cas de doute sur une valeur, vérifier la source ou ne pas publier le chiffre. Un chiffre repris d'un numéro antérieur est **revalidé** (le millésime a pu changer) avant réutilisation.
8. **Pas d'arrondi silencieux.** « ~9 560 € », « de l'ordre de 100 000 à 150 000 », « ≈ 20/an en moyenne 2012-2025 » : la précision affichée doit refléter la précision disponible.

---

## Méthode de classement

Quand un numéro hiérarchise des phénomènes hétérogènes (un décès, un euro et une personne exposée ne sont pas la même unité), il applique quatre critères, énoncés explicitement au lecteur :

| Critère | Question posée |
|---|---|
| **Masse** | Combien de personnes, combien de milliards ? |
| **Durée** | Décennies ou saison ? |
| **Irréversibilité** | Peut-on revenir en arrière ? |
| **Effet de levier** | Ce chiffre en commande-t-il d'autres ? |

**Critère explicitement écarté** : la fréquence de citation médiatique — c'est l'objet de l'exercice, pas son instrument.

### Indice de sous-exposition

Échelle fixe, à ne pas modifier ni étendre :

| Symbole | Signification |
|---|---|
| ⚪ | correctement traité / très exposé |
| 🟡 | exposé par à-coups, ou sur-exposé en polémique et sous-exposé en structure |
| 🟠 | sujet visible, ampleur invisible |
| 🔴 | quasi invisible — écart maximal entre poids réel et couverture |

L'indice se justifie en une ligne accolée au symbole (« 🟠 traité comme une curiosité statistique annuelle »), jamais posé sans motif.

---

## Forme d'un numéro

Structure de référence, établie par le n° 1. Un numéro peut en omettre des sections, pas en inventer de nouvelles sans raison :

1. **Titre + chapô** — sous-titre qui annonce l'angle, puis un paragraphe en italique donnant l'état des données, la nature des sources et l'avertissement sur les millésimes.
2. **Méthode** — critères de classement, avertissements méthodologiques numérotés.
3. **Le corps** — entrées numérotées (1️⃣ à 🔟 pour un top 10), chacune bâtie sur le même gabarit (ci-dessous).
4. **Tableau de synthèse** — masse réelle contre saillance médiatique.
5. **Le peloton juste derrière** — rangs 11 à 20, un paragraphe dense chacun, chiffre en gras, source entre parenthèses en italique.
6. **Les faux grands nombres** — tableau « peur répandue » / « ce que disent les données », suivi des indicateurs qui se dégradent réellement.
7. **Ce que l'enquête révèle sur la structure du biais** — analyse, pas énumération.
8. **Sources primaires** — regroupées par domaine, référence complète.
9. **Avertissement de clôture** en italique (intervalles de confiance non reproduits, renvoi aux publications sources).

### Gabarit d'une entrée

```markdown
### 3️⃣ **13,8 millions de personnes en affection de longue durée** — soit un Français sur cinq

**Indice de sous-exposition : 🔴 quasi invisible**

| Donnée | Valeur (millésime **2022**) | Source |
|---|---|---|
| … | … | … |

> **⚠️ Précautions de lecture** (quand le chiffre est piégeux)

**Pourquoi c'est structurant :** … (2 à 4 paragraphes d'analyse)
```

Le titre de l'entrée = **le chiffre**, pas le thème. « 20 148 morts par chute chez les 65 ans et plus » et non « les chutes des personnes âgées ». Ajouter une comparaison d'ancrage dans le titre quand elle existe (« — six fois la route »).

---

## Style

- **Le tableau porte les données, le texte porte l'argument.** Ne jamais paraphraser en prose un tableau qu'on vient de donner.
- **Ancrer par le ratio.** Un grand nombre isolé ne dit rien ; « ×3 400 vs terrorisme », « six fois la route », « un facteur 50 » sont ce qui rend le nombre lisible.
- **Phrases déclaratives, pas d'emphase rhétorique.** Les chiffres suffisent. Pas de point d'exclamation, pas d'indignation explicite, pas d'appel à l'action.
- **Pas de conseil, pas de prescription politique.** Le magazine décrit des ordres de grandeur et des écarts entre objectif affiché et résultat mesuré (plan antichute : objectif −20 %, résultat +18 %). Il ne recommande pas de politique.
- **Nommer les biais, pas les coupables.** Biais d'événement, d'identification, d'agentivité, d'âge, décalage temporel. L'invisibilité de ces chiffres est expliquée comme un désajustement perceptif, jamais comme une faute morale du public ou un complot médiatique.
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
| **journaliste** | Haiku | ratisse les sources publiques primaires, relève valeur + millésime + champ + référence, rapporte aussi ses pistes non abouties | `collecte/NN-theme.md` |
| **fact-checker** | Sonnet | rouvre chaque source, applique sept contrôles (existence, millésime, champ, cohérence, additivité, nature de la mesure, contestation), rend un verdict par chiffre | `verifications/NN-theme.md` |
| **editeur** | Opus | hiérarchise, attribue les indices de sous-exposition, ancre par les ratios, applique les verdicts, assemble le numéro | `index.md` — seul à y écrire |

Le modèle croît avec l'irréversibilité de la décision : la collecte est large et bon marché, la vérification demande de la rigueur, l'assemblage engage le numéro. Corollaire de ce choix — **le fact-checker n'est pas une formalité, c'est le filet du journaliste** : ratisser large avec un modèle rapide produit mécaniquement des relevés de champ approximatifs, et c'est le contrôle n° 3 qui les rattrape.

Les frontmatters portent les alias `haiku` / `sonnet` / `opus`, pas des identifiants figés : le dépôt suit ainsi les montées de version sans intervention. Au moment où ce choix a été fait (août 2026), ils désignaient respectivement Haiku 4.5, Sonnet 5 et Opus 5. Ce qui compte est le rang relatif, pas la génération — si un jour la collecte doit être épinglée pour reproduire un numéro à l'identique, c'est une décision de numéro, pas de dépôt.

Le journaliste dépose lui-même sa collecte ; ni lui ni le fact-checker ne peuvent écrire dans `index.md`. Le fact-checker n'a aucun outil d'écriture — il rend son verdict en sortie d'agent, et c'est l'éditeur ou la session principale qui le classe dans `verifications/`.

**Ordre d'intervention** : journaliste → fact-checker → editeur → fact-checker (passe finale sur le texte assemblé) → publication. Un verdict `NON PUBLIABLE` bloque ; un chiffre `[NON VÉRIFIÉ]` est retiré ou renvoyé au journaliste, jamais publié au pari.

Le journaliste peut être lancé en plusieurs exemplaires en parallèle sur des thèmes distincts. Le fact-checker aussi, un par entrée.

## Organisation du dépôt

**Un dossier par numéro.** Le texte publié n'est que la pointe : la matière collectée et les vérifications restent avec lui, dans le même dossier, pour que tout chiffre reste traçable jusqu'à sa source des mois après la parution.

```
numeros/
  01-les-grands-nombres/
    index.md            le numéro publié — seul fichier diffusé
    collecte/           rapports du journaliste : matière brute sourcée
      NN-theme.md
    verifications/      rapports du fact-checker : verdicts par chiffre
      NN-theme.md
    media/              graphiques et images, si le numéro en a (optionnel)
.claude/agents/         journaliste, fact-checker, editeur
CLAUDE.md               ce fichier
```

Toute autre arborescence (site statique, gabarits de newsletter, scripts de collecte) est à créer au moment où elle sert, pas par anticipation.

**Nommage** : dossier `NN-slug/` — numérotation sur deux chiffres, slug en minuscules sans accents. Le fichier publié s'appelle toujours `index.md`, quel que soit le numéro.

**Ce qui est diffusé** : `index.md` uniquement. `collecte/` et `verifications/` sont des archives de travail — versionnées, jamais publiées, jamais élaguées. Un rapport de collecte dont les pistes n'ont pas abouti se garde : il dit au numéro suivant où l'on a déjà cherché.

**Réutiliser un chiffre d'un numéro antérieur** se fait en repartant de son `verifications/`, pas de son `index.md` — et en revalidant le millésime, qui a pu changer depuis.

**Commits** : en français, à l'impératif, portée en préfixe — `n°1 : corrige le millésime des données ALD`, `méthode : ajoute la règle de non-additivité`.

**Branches** : développer sur une branche dédiée, jamais de push direct sur la branche par défaut.

---

## Travailler sur un numéro

**Ajouter ou modifier un chiffre** — le circuit est toujours le même :

1. Aller à la publication primaire (site de l'institution), pas à un article de presse qui la cite.
2. Relever : valeur, millésime, champ (France entière ou métropole ? tous régimes ou régime général ? ménages ordinaires ou population totale ?), date de publication, référence exacte.
3. Vérifier que le champ est compatible avec les autres chiffres de la même entrée. **Les changements de champ sont la première cause d'erreur** : le *Points de repère* CNAM raisonne tous régimes / France entière, la série open data annuelle porte sur le seul régime général — les deux ne sont pas superposables.
4. Ajouter la ligne au tableau de l'entrée **et** la référence en §7 « Sources primaires ».

**Mettre à jour un numéro publié** : préférer la mise à jour explicite (« données 2023, actualisées en juin 2026 ») à la réécriture silencieuse. La date d'état des données en chapô doit être mise à jour en même temps.

**Vérification avant publication** :

- [ ] chaque chiffre a un millésime et une source primaire listée en §7
- [ ] aucun total obtenu en additionnant des estimations attribuables
- [ ] les champs statistiques sont homogènes à l'intérieur de chaque tableau
- [ ] les comptages administratifs sont signalés comme tels
- [ ] les estimations contestées présentent la contestation
- [ ] la section « ce qui va mieux » existe et est nourrie
- [ ] typographie française vérifiée (insécables, guillemets, `−`, ordinaux)
- [ ] chaque indice de sous-exposition est motivé

---

## Contraintes de diffusion

Le même Markdown sert le site et la newsletter. Conséquences pratiques :

- **Les tableaux larges passent mal en e-mail.** Trois colonnes maximum (`Donnée | Valeur | Source`) ; au-delà, scinder en deux tableaux.
- **Pas de HTML brut, pas de CSS, pas de JavaScript** dans les fichiers de numéros — Markdown standard uniquement, pour rester portable entre le générateur de site et la plateforme d'envoi.
- **Les émojis d'indice et de rang sont porteurs de sens**, pas décoratifs ; ils doivent rester lisibles en texte brut. N'en introduire aucun autre.
- **Pas d'image indispensable à la compréhension** : un numéro doit se lire intégralement en texte.
