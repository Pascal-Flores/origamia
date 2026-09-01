# Reprise de la série cmp-repetition-n — exercices 10 à 12, 179 et 180

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-02
- Représentation(s) autorisée(s) pour cette série : programme Turtle Vittascience entièrement développé, sans boucle, présenté à l’élève comme support d’observation ; paramètres déjà fixés dans les blocs.
- Représentation(s) interdites pour cette série : demander à l’élève de paramétrer les blocs ; introduire une boucle dans le programme observé ; utiliser cinq polygones réguliers ou des formes abstraites difficiles à reconnaître.
- Décision : déclinaison autorisée après validation explicite du pilote 10 par l’utilisateur.

## Attendu

- Compétence : `cmp-repetition-n`
- Attendu : `att-repetition-n-cm1`
- Geste travaillé : déterminer combien de fois un motif d’instructions est répété dans un programme.
- Série concernée : 10, 11, 12, 179, 180.

## Forme invariante

- Type : `free`.
- Support : interface Turtle montrant un programme entièrement développé, sans boucle.
- Le programme produit une forme immédiatement reconnaissable et nommée dans le contexte.
- Un même groupe d’instructions apparaît plusieurs fois à l’identique.
- Consigne identique : « Combien de fois ce morceau est-il répété ? Écris uniquement le nombre. »
- Réponse attendue : un entier.
- `essais: 2`.
- Feedback essai 1 : aide à repérer les limites du motif sans donner le nombre.
- Feedback final : indique le nombre de répétitions et montre le motif répété.
- Les paramètres Turtle sont déjà fixés ; l’élève n’a rien à modifier. Ils peuvent varier entre variantes puisque la tâche consiste uniquement à observer le programme.
- Les variantes changent de dessin et de motif, mais pas de geste cognitif ni de format de réponse.
- Une mise en situation spécifique peut être inventée quand aucun rituel existant ne correspond au tracé, à condition qu’elle reste concrète et n’ajoute aucune compétence parasite.

## Variante 10 — validée comme pilote

- Cible : escalier simplifié de trois marches.
- Situation : `rit-dessiner-pictogramme-escalier`.
- Motif : `avancer 50` → `gauche 90°` → `avancer 50` → `droite 90°`.
- Répétitions : 3.
- Programme : 12 blocs.

## Variante 11

- Cible : ligne pointillée.
- Situation : `rit-tracer-ligne-pointillee-affiche`.
- Motif : `avancer 10` → `lever le stylo` → `avancer 10` → `baisser le stylo`.
- Répétitions : 4.

## Variante 12

- Cible : peigne simplifié.
- Situation : `rit-dessiner-pictogramme-peigne`.
- Motif : `avancer 10` → `droite 90°` → `avancer 50` → `reculer 50` → `gauche 90°`.
- Répétitions : 5.

## Variante 179

- Cible : hublots ronds alignés.
- Situation : `rit-dessiner-hublots-sous-marin`.
- Motif : `cercle 20` → `lever le stylo` → `avancer 50` → `baisser le stylo`.
- Répétitions : 3.

## Variante 180

- Cible : échelle simplifiée à six barreaux.
- Situation : `rit-dessiner-pictogramme-echelle`.
- Motif : `avancer 50` → `reculer 50` → `gauche 90°` → `avancer 50` → `droite 90°`.
- Répétitions : 6.
- Après les six répétitions, Turtle lève le stylo, rejoint le haut du montant droit, rebaisse le stylo, tourne vers le bas puis avance six fois de 50 pour terminer le second montant.
- Programme : 40 blocs au total.
- `solution.py` et `vittascience.py` ont été réalignés sur les 6 répétitions le 2026-09-02.

## Retours utilisateur pris en compte

- Les anciens triangle/carré/hexagone/pentagone/octogone étaient trop répétitifs.
- Les formes doivent être immédiatement reconnaissables.
- Les projets `.py` Vittascience doivent reprendre la structure réelle d’un export importable et les types/champs officiels des blocs.
- Les mises en situation peuvent être inventées si cela évite de plaquer un rituel sans rapport avec le dessin.
- 2026-09-02 : utilisateur autorise explicitement la déclinaison des variantes 11, 12, 179 et 180 à partir du pilote 10.
- 2026-09-02 : utilisateur modifie les nombres de répétitions et certains paramètres de tracé afin d’éviter une série trop homogène ; conserver ces modifications.
- 2026-09-02 : le projet 180 ne fonctionnait plus car les fichiers de solution étaient restés sur 4 répétitions alors que l’exercice en demandait 6 ; correction demandée.

## Validations utilisateur

- Cadrage : validé pour la déclinaison
- Variante pilote 10 : validée
- Déclinaison 11-12/179-180 : à reviewer
- Review finale : non validée
- Passage testing : non validé
