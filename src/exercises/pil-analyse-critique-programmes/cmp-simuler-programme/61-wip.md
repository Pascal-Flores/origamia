# Reprise des variantes 6e — simuler un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : mission explicite, même programme fourni en blocs textuels (`event:`, `move:`, `say:`, `end:`), quatre états initiaux en langage naturel ou sur grille.
- Représentation(s) interdites : programme réduit à une opération isolée, syntaxe de variable inventée, situation quotidienne artificiellement transformée en programme, tâche qui ne teste qu'une valeur sans état initial complet.
- Décision : review et harmonisation de 213–214 autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-simuler-programme`.
- Attendu : `att-simuler-programme-6e`.
- Variantes de référence : 61, 62, 63.
- Variantes reprises : 213, 214.

## Forme de référence

Les variantes 61–63 utilisent la même mécanique :

1. une mission définie par un état final précis ;
2. un même programme exécuté dans quatre états initiaux différents ;
3. un véritable robot, appareil ou dispositif programmable ;
4. l'élève simule séparément chaque test ;
5. il sélectionne tous les états initiaux qui conduisent à la réussite (`type: qcm`) ;
6. deux tests réussissent et deux échouent ;
7. trois essais avec deux feedbacks progressifs puis un feedback final.

Dans 62–63, le programme modifie seulement une partie de l'état du dispositif : au moins une information reste inchangée et doit donc être correcte dès le départ. Ce mécanisme oblige l'élève à tenir compte de l'état initial complet.

## Problème des versions précédentes de 213–214

Les exercices respectaient formellement « quatre états initiaux + même programme », mais les situations `niveau sonore` et `activité au parc` étaient des situations ordinaires transformées artificiellement en simulations. Elles ne ressemblaient donc pas réellement aux variantes 61–63, qui portent sur des systèmes programmables concrets.

## Nouvelle reprise de 213–214

- 213 : maquette de feu piéton programmable. Le programme force le feu voitures au rouge et le feu piétons au vert, mais ne modifie pas le signal sonore. La mission exige les trois états corrects. Deux situations initiales réussissent parce que le signal sonore est déjà activé.
- 214 : barrière de parking programmable avec compteur de places libres. Lorsqu'une voiture sort, le programme ajoute une place libre, ouvre la barrière et allume le voyant SORTIE. La mission impose un nombre final précis de places libres et les états de sortie. Deux situations initiales réussissent car elles commencent avec le bon nombre de places.
- Deux nouveaux rituels sont ajoutés au référentiel des situations afin d'éviter de réutiliser une mise en situation existante.

## Validations utilisateur

- Cadrage : validé par la demande d'alignement sur les autres variantes
- Variante pilote : 61–63 servent de références établies
- Déclinaison : autorisée pour 213–214
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 213–214
