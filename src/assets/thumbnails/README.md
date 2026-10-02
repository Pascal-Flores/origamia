# Miniatures Origamia

Seule l’illustration est générée avec imagegen, en PNG transparent. Le fond et le disque sont composés par code à partir de `layout.json` et ne doivent jamais être générés.

- Format : 344 × 227 px.
- Fond uni défini dans `layout.json` : actuellement #aa84ff (RVB 170, 132, 255), après modification par l’utilisateur.
- Disque : blanc #ffffff, diamètre 138 px, centre (172 ; 113,5).
- Illustration : marges transparentes retirées, proportions conservées, inscrite dans une zone de 96 × 96 px, centrée sur le disque.
- Recadrage : limites calculées sur les pixels d’alpha ≥ 8/255 pour ignorer les pixels parasites presque transparents qui faussent le centrage. L’anticrénelage dans ces limites est conservé.
- Anticrénelage : suréchantillonnage ×8, identique à chaque export.

## Textes alternatifs

Les 240 textes corrigés sont centralisés dans [alt-texts.json](alt-texts.json). Chaque entrée associe `id` (numéro d’exercice), `file` (nom du PNG, relatif à ce dossier) et `alt` (description française du sujet). Modifier ce fichier pour corriger un texte.

- [Liste à relire](alt-texts.md)
- [Export CSV](alt-texts.csv), en UTF-8 avec marqueur d’encodage
- [Galerie complète des exercices 1 à 240](galerie-1-240.html)

La galerie utilise réellement ces descriptions dans les attributs HTML `alt`, sans ajouter le numéro d’exercice. Pour intégrer une miniature ailleurs, reprendre le champ `alt` correspondant dans la balise image, par exemple :

```html
<img src="1-cloche.png" alt="Cloche" width="344" height="227">
```

L’attribut `alt` appartient à la page qui affiche l’image ; il n’est pas intégré au fichier PNG. Les légendes des aperçus et des index utilisent les mêmes textes corrigés. Les noms des PNG restent stables et les prompts historiques conservent les consignes originales.

## Production

[Télécharger les 240 miniatures sur fond violet en ZIP](origamia-vignettes-1-240.zip).

Les vignettes et les prompts des exercices 1 à 15 sont répertoriés dans [index.md](index.md), avec un [aperçu de la série](apercu-1-15.png).

Les exercices 16 à 240 sont répertoriés dans [index-16-240.md](index-16-240.md). La [galerie filtrable](galerie-16-240.html) s’ouvre dans un navigateur et permet de rechercher un numéro ou un sujet et de télécharger chaque PNG. Les 225 vignettes sont terminées et vérifiées. [Télécharger les 225 PNG en ZIP](origamia-vignettes-16-240.zip). Les illustrations seules et les prompts restent dans `illustrations/` ; les reprises éventuelles disposent d’un fichier `-correction-prompt.md`.

Après une modification de `layout.json`, relancer la composition des illustrations concernées. Pour actualiser les planches d’aperçu, l’index et la galerie à partir des PNG déjà composés :

```bash
python3 src/assets/scripts/preview_thumbnail_batch.py --first 1 --last 240
```

Ce script lit `alt-texts.json`, actualise les aperçus, les index, les deux galeries et les exports Markdown et CSV des textes alternatifs. Il contrôle les dimensions, la transparence de l’original et le centrage visible. Il ne génère aucune illustration. `production-16-240.json` conserve la liste et les consignes initiales ; les fichiers de prompt individuels conservent les consignes réellement utilisées.

1. Suivre `illustration-style.md` : générer uniquement l’objet, dans le style de la charte Origamia, avec un vrai canal alpha. Joindre `references/charte-couleurs.png` et `references/charte-univers.png` à imagegen. Choisir une palette restreinte dans `palette.json` et imposer ses codes HEX dans le prompt : aucun fond, rond ni ombre portée ; texte seulement lorsque le sujet le demande. Vérifier visuellement et contrôler la transparence.
2. Enregistrer l’original dans `illustrations/<numéro>-<sujet>.png`.
3. Exécuter depuis la racine du projet (Python 3 avec Pillow) :

```bash
python3 src/assets/scripts/compose_thumbnail.py \
  src/assets/thumbnails/illustrations/1-cloche.png \
  src/assets/thumbnails/1-cloche.png \
  --save-template src/assets/thumbnails/template.png
```

`template.png` est le fond réutilisable sans illustration. La composition utilise toujours le même gabarit défini dans `layout.json`. Conserver ces paramètres pour toute la série.

Les anciennes versions, dont la première tentative avec un fond généré et la version au fond vert foncé, sont conservées dans `drafts/`.
