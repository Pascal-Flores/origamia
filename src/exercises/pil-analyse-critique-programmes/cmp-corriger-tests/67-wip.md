# Reprise de la progression CM2 — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fourni en blocs textuels pris en charge par le projet (`event:`, `move:`, `say:`, `end:`), résultats de plusieurs tests en langage naturel, corrections proposées sous forme de modifications explicites.
- Représentation(s) interdites : simple choix d'un programme corrigé à partir d'un seul essai, classement binaire `corrige / ne corrige pas` sans comparaison de plusieurs tests, écriture libre de programme.
- Décision : cadrage et pilote validés ; déclinaison réalisée sur 68, 69, 189 et 190 ; review finale effectuée.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu concerné : `att-corriger-tests-cm2`.
- Variantes concernées : 67, 68, 69, 189 et 190.

Le référentiel a été mis à jour pour formuler explicitement la non-régression : `Classer des corrections selon qu’elles réparent un test en échec sans provoquer de régression sur un test déjà réussi.`

## Problème identifié

La forme précédente distinguait surtout le CM1 et le CM2 par le nombre de corrections à examiner :

- CM1 : choisir un programme corrigé parmi trois ;
- CM2 : classer plusieurs programmes corrigés en `Corrige / Ne corrige pas`.

Le geste cognitif restait donc très proche : dans les deux cas, l'élève vérifiait une correction sur une seule situation.

## Progression validée

- **CM1** : un essai échoue ; choisir la correction qui permet d'obtenir le comportement attendu.
- **CM2** : deux tests existent, dont un déjà réussi et un en échec ; évaluer les corrections pour distinguer celles qui réparent le test en échec **sans provoquer de régression** sur le test déjà réussi.
- **6e** : à partir des écarts observés, compléter une explication structurée des modifications nécessaires et du résultat obtenu.

## Forme CM2 validée

Chaque variante comporte :

1. une mission concrète sur un dispositif programmable ;
2. un programme de départ ;
3. deux tests réalisés avec des états initiaux différents ;
4. un test déjà réussi et un test en échec ;
5. cinq corrections proposées ;
6. trois catégories :
   - `Corrige le test 2 sans casser le test 1` ;
   - `Corrige le test 2 mais casse le test 1` ;
   - `Ne corrige pas le test 2` ;
7. l'élève vérifie donc l'effet de chaque correction sur **les deux tests**, et pas seulement sur le cas qui a révélé le bug ;
8. `type: ddu`, `essais: 3`, avec deux feedbacks progressifs puis une explication finale.

Cette forme introduit explicitement l'idée de **régression** : une correction locale n'est pas suffisante si elle dégrade un comportement qui fonctionnait auparavant.

## Déclinaison réalisée

- 67 — `rit-robot-trier-batterie-recyclage` : l'inversion de la trappe réussit si elle est ouverte au départ mais échoue si elle est déjà fermée ; la correction robuste ferme explicitement la trappe.
- 68 — `rit-lampe-liseuse-regler` : une augmentation relative de `20 points` atteint `70 %` depuis `50 %` mais monte à `90 %` depuis `70 %` ; la correction robuste règle directement l'intensité à `70 %`.
- 69 — `rit-convoyeur-remplir-caisse` : ajouter systématiquement `2 colis` atteint la cible depuis `4` mais surcharge une caisse qui en contient déjà `6` ; la correction robuste complète la caisse jusqu'à `6 colis`.
- 189 — `rit-preparer-sac-piscine` : l'inversion du voyant réussit lorsqu'il est rouge au départ mais échoue lorsqu'il est déjà vert ; la correction robuste impose le voyant vert.
- 190 — `rit-lire-cartel-oeuvre` : une augmentation relative de `2 points` atteint la taille `18` depuis `16` mais monte à `20` depuis `18` ; la correction robuste règle directement la taille à `18 points`.

## Review

Verdict : **OK**.

- Les cinq variantes utilisent le même geste cognitif et les mêmes trois catégories.
- Chaque exercice contient un test 1 réussi et un test 2 en échec.
- Chaque exercice possède une seule correction robuste, deux corrections qui réparent le test 2 mais provoquent une régression, et deux corrections qui ne réparent pas le test 2.
- Les solutions sont donc uniformes : catégorie 1 = correction `1`, catégorie 2 = corrections `3` et `4`, catégorie 3 = corrections `2` et `5`.
- Les feedbacks obligent explicitement à rejouer chaque correction sur les deux états initiaux.
- 67, 68 et 69 ont été placés en `wip` puisque leur contenu a changé après leurs tests précédents. 189 et 190 restent en `wip`.
- Aucun passage en `testing`, build publiable ou import SQLite n'est revendiqué.

## Décisions utilisateur

- 2026-09-03 : l'utilisateur juge les variantes CM2 67–69 et 189–190 insuffisamment différenciées du niveau CM1.
- 2026-09-03 : validation explicite du pilote 67 et de la progression fondée sur la non-régression (`oui c'est bien`).

## Validations utilisateur

- Cadrage : validé
- Variante pilote : validée
- Déclinaison : validée
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
