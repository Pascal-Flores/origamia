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

- Cible : échelle fermée de 70 × 150 pixels, entièrement contenue dans la zone de dessin, avec deux montants de même longueur et six barreaux alignés.
- Situation : `rit-dessiner-pictogramme-echelle`.
- Le programme trace d’abord un cadre rectangulaire : les deux montants, le barreau du bas et le barreau du haut.
- Motif : `lever le stylo` → `avancer 30` → `droite 90°` → `baisser le stylo` → `avancer 70` → `reculer 70` → `gauche 90°`.
- Répétitions : 4.
- Chaque répétition ajoute exactement un barreau intermédiaire ; aucun montant ni barreau ne dépasse du cadre.
- À la fin, Turtle est déplacée stylo levé à droite de l’échelle pour ne pas masquer le dessin.
- Programme : 40 blocs au total.
- `vittascience.py` utilise exclusivement `turtle_direction`, `turtle_turn` et `turtle_pen`, déjà présents dans les projets fonctionnels de la série.
- Aucun bloc `turtle_goto` n’est utilisé.
- Le XML extrait du fichier final complet est reparsé avant écriture.

## Retours utilisateur pris en compte

- Les anciens triangle/carré/hexagone/pentagone/octogone étaient trop répétitifs.
- Les formes doivent être immédiatement reconnaissables.
- Les projets `.py` Vittascience doivent reprendre la structure réelle d’un export importable et les types/champs officiels des blocs.
- Les mises en situation peuvent être inventées si cela évite de plaquer un rituel sans rapport avec le dessin.
- 2026-09-02 : utilisateur autorise explicitement la déclinaison des variantes 11, 12, 179 et 180 à partir du pilote 10.
- 2026-09-02 : utilisateur modifie les nombres de répétitions et certains paramètres de tracé afin d’éviter une série trop homogène ; conserver ces modifications.
- 2026-09-02 : les premières générations de `180/vittascience.py` échouent dans Vittascience avec `textToDom was unable to parse` ; ne plus fabriquer ce projet à partir d'un XML écrit à la main sans reprendre les structures de blocs validées dans les projets fonctionnels du dépôt.
- 2026-09-02 : la variante « six perles » est refusée car trop proche des hublots ; conserver l’échelle comme cible visuelle.
- 2026-09-02 : le premier rendu de l’échelle ressemblait à une colonne de rectangles empilés. Correction demandée : faire apparaître deux montants distincts et une silhouette immédiatement identifiable comme une échelle.
- 2026-09-02 : une nouvelle tentative fondée sur `turtle_goto` échoue encore avec `textToDom was unable to parse`. L’utilisateur demande explicitement d’utiliser les nombreux exercices déjà fonctionnels comme modèles. Correction : suppression complète de `turtle_goto`, reprise stricte des structures `turtle_direction`, `turtle_turn` et `turtle_pen` des exercices 10, 11, 12, 178 et 179, et validation syntaxique du XML avant commit.

- 2026-09-02 : le rendu suivant présente une échelle cassée : le montant droit s’arrête avant le dernier barreau et le montant gauche dépasse sous celui-ci. Refonte géométrique : cadre fermé de 70 × 150 pixels, quatre barreaux intermédiaires ajoutés par le motif répété, aucun segment au-delà du cadre.

## Validations utilisateur

- Cadrage : validé pour la déclinaison
- Variante pilote 10 : validée
- Déclinaison 11-12/179-180 : à reviewer
- Variante 180 : à revalider après import du projet corrigé dans Vittascience
- Review finale : non validée
- Passage testing : non validé
