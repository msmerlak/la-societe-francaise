# Le site et la newsletter

Générateur du site de *La société française*. Il transforme le `index.md` de chaque numéro en pages HTML, et le même Markdown en version e-mail.

**Aucune dépendance** : Python 3.9 ou plus récent, rien d'autre. Un dépôt de contenu ne doit pas dépendre d'une installation de paquets pour publier — le jour où l'on publie, l'outil doit marcher.

## Usage

```sh
python3 site/construire.py                 # construit le site dans public/
python3 site/construire.py --controler     # contrôle seulement, n'écrit rien
python3 site/construire.py --strict        # échoue si un contrôle remonte une erreur
python3 site/construire.py --newsletter    # produit aussi la version e-mail
```

Options : `--source` (racine du dépôt), `--sortie` (dossier de destination), `--base` (URL publique, pour le flux RSS).

Sortie produite :

```
public/
  index.html                      accueil, liste des numéros
  numeros/NN-slug/index.html      le numéro
  numeros/NN-slug/media/          images du numéro, si le numéro en a
  newsletter/NN-slug.html         version e-mail, styles en ligne (option)
  styles/societe.css
  flux.xml                        flux RSS
```

`public/` est régénérable et n'est pas versionné.

## Ce que le générateur publie, et ce qu'il ne publie pas

Il ne lit qu'un fichier par numéro : **`index.md`**. Le `dispositif.md`, la `collecte/` et les `verifications/` sont des archives de travail — versionnées, jamais publiées. Ce n'est pas une consigne, c'est une propriété du programme : il ne va chercher aucun autre chemin, et un dossier de numéro sans `index.md` est simplement absent du site.

Le seul autre fichier qu'il ouvre est le `dispositif.md`, en lecture seule, pour y relever les émojis que le numéro s'autorise (voir plus bas). Rien n'en est publié.

## Les contrôles

`site/controles.py` rend exécutable la partie mécanique de la liste « Vérification avant publication » du `CLAUDE.md`. Il ne vérifie **aucun chiffre** — c'est le travail du fact-checker, et aucun programme ne peut le faire à sa place.

Deux niveaux : les **erreurs** (`✖`) bloquent avec `--strict`, les **avertissements** (`▲`) sont signalés sans bloquer.

| Contrôle | Niveau | Ce qu'il applique |
|---|---|---|
| `html-brut` | erreur | « Pas de HTML brut, pas de CSS, pas de JavaScript » dans un fichier de numéro |
| `tableau-large` | erreur | trois colonnes maximum — au-delà, illisible en e-mail |
| `squelette` | erreur | titre, section « Méthode », section « Sources primaires » |
| `emoji-hors-dispositif` | avertissement | aucun émoji hors de ceux que le dispositif du numéro définit |
| `insecable-avant` | avertissement | espace insécable avant `: ; ! ?` `»` et `%` |
| `insecable-guillemet` | avertissement | espace insécable après `«` |
| `insecable-milliers` | avertissement | séparateur de milliers insécable |
| `insecable-unite` | avertissement | espace insécable entre le nombre et son unité |
| `guillemet-droit` | avertissement | guillemets français `« »` |
| `signe-moins` | avertissement | signe moins `−`, pas le trait d'union, devant une valeur négative |

Les émojis autorisés sont lus dans le `dispositif.md` du numéro : le dispositif déclare les siens, le contrôle signale tout le reste. Les touches numérotées forment une famille — un dispositif qui écrit « 1️⃣ à 🔟 » les autorise toutes sans avoir à les énumérer. Les flèches, le signe moins et le signe multiplié ne sont pas traités comme des émojis : c'est de la typographie, et le `CLAUDE.md` l'impose.

**Le contrôle ne corrige rien**, volontairement. Une correction automatique dans `index.md` contournerait la règle qui veut que l'éditeur soit seul à y écrire, et une typographie réparée en silence est exactement le genre de modification qu'on ne relit jamais.

## Le rendu

`site/rendu.py` implémente un sous-ensemble de Markdown : titres, paragraphes, tableaux, citations, listes, blocs de code, emphase, liens, images, filets. C'est exactement ce que les contraintes de diffusion autorisent dans un numéro. Tout ce qui ressemble à du HTML est échappé plutôt qu'interprété — le contrôle `html-brut` le signale, et le rendu le neutralise, de sorte qu'aucun balisage ne peut traverser par accident.

Deux détails qui servent un magazine quantitatif :

- **les cellules qui ne portent qu'une valeur sont alignées à droite**, automatiquement, et les tableaux composés en chiffres tabulaires — sans quoi une colonne de nombres ne se compare pas d'un coup d'œil ;
- **les espaces insécables sont transmises telles quelles**, jamais normalisées : elles portent la typographie et leur perte casserait les nombres en fin de ligne.

Le titre et le chapô sont déduits du document — premier `#`, puis premier paragraphe entièrement en italique. Aucun front-matter n'est demandé à l'éditeur : le `index.md` doit rester du Markdown standard pour rester portable vers la plateforme d'envoi.

Les dates de publication et de mise à jour viennent de l'historique git du fichier (`--diff-filter=A` pour la première, dernier commit pour la seconde). Rien à tenir à jour à la main.

## La version e-mail

`--newsletter` produit le même contenu avec les styles repliés dans les balises, une largeur fixe de 620 px et une mise en page en tableaux : les clients de messagerie ignorent les feuilles de style externes, et une partie ignore `<style>`. Les alignements de colonnes sont repliés en `text-align` en ligne, sans quoi les tableaux de chiffres se désalignent à l'envoi.

## À faire quand ça servira

Le déploiement n'est pas câblé : rien n'est encore publié, et le `CLAUDE.md` demande de créer l'arborescence au moment où elle sert. Quand un numéro sortira, il restera à choisir un hébergement pour `public/` et, si l'on veut un garde-fou, à lancer `--controler --strict` en intégration continue.
