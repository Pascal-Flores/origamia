# Direction des illustrations Origamia

Source : charte graphique fournie par l’utilisateur, `Charte graphique Origmia 0926.pdf` (septembre 2026). Les pages 2 et 4 sont conservées dans `references/` pour les prochains appels imagegen. Les pages 5 et 6 complètent les exemples d’univers et d’interface.

## Règles de génération

- Générer uniquement l’objet de l’exercice, isolé sur un vrai fond transparent. Le cercle et le fond sont ajoutés par le script de composition.
- S’inspirer de la charte pour les formes simples et arrondies, les silhouettes lisibles et les aplats colorés.
- Ne conserver que les détails utiles pour reconnaître l’objet. Aucun motif géométrique, pli, reflet ni décoration ajouté par principe. Privilégier les silhouettes colorées et les lignes internes discrètes ; éviter un contour extérieur épais systématique.
- Utiliser le minimum de couleurs : deux par défaut, choisies dans `palette.json`. N’ajouter une couleur que si elle est nécessaire à la compréhension du sujet. Inscrire explicitement les codes HEX et leur rôle dans le prompt. Interdire toute couleur supplémentaire pour les aplats et les traits.
- Conserver une lecture immédiate dans la zone de 96 × 96 px. Éviter les détails minuscules, décors, personnages additionnels, logos et textes.
- Demander des aplats sans texture, dégradé, ombre portée, reflet métallique ni rendu 3D. Il s’agit de la direction retenue pour cette série de miniatures à partir des exemples de la charte, qui comporte aussi certains rendus avec dégradés.
- Contrôler la transparence réelle et le résultat assemblé. Les couleurs demandées à imagegen sont des contraintes de génération ; elles ne garantissent pas des valeurs HEX exactes pour tous les pixels de l’illustration. L’anticrénelage crée également des couleurs intermédiaires. Le fond et le disque, eux, sont déterministes.

## Prompt réutilisable

> Générer uniquement [OBJET], pour une miniature d’exercice Origamia. Utiliser la planche de couleurs comme référence de palette et la planche « Univers Origamia » comme référence de style. Illustration 2D très simple : formes arrondies, aplats nets et silhouette immédiatement lisible. Garder uniquement les détails nécessaires à la reconnaissance de l’objet. Palette strictement limitée à deux couleurs [CODES HEX ET RÔLES] : aucune autre couleur pour les aplats et les traits. Aucun motif géométrique, pli décoratif, reflet, trait de mouvement ou ornement inutile. Sans dégradé, texture, ombre portée, rendu 3D, contour épais systématique ni texte. Objet complet, seul, centré avec une marge transparente, sur un vrai fond PNG alpha, y compris ses ouvertures. Aucun fond coloré, rond blanc, badge ou décor : le gabarit est assemblé séparément par code.

## Cloche — exercice 1

- Corps : jaune #ffee4d.
- Intérieur et battant : ocre #9a6f03.
- Aucun ornement ni trait de sonnerie.

Le prompt réellement utilisé est conservé dans `illustrations/1-cloche-prompt.md`.
