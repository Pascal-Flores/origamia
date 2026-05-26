# Blockly DSL

Ce petit DSL sert a decrire des blocs Blockly en texte, puis a les convertir en SVG.

## Format de base

Chaque ligne suit la forme :

```text
type: libelle du bloc
```

Exemple :

```text
event: DEBUT
move: AVANCER
end: FIN
```

## Imbrication

Utilise `2` espaces pour mettre des blocs dans une boucle ou un bloc de controle.

```text
event: DEBUT
repeat: REPETER (3) FOIS
  move: PRENDRE (1) feuille
  move: POSER la feuille sur la pile
end: FIN
```

## Parametres inline

- `(...)` : parametre standard, fond clair
- `{...}` : variable, fond variable
- `"..."` : texte litteral
- `[...]` : nombre explicite

Exemples :

```text
move: ENTRER le code (5074)
move: ENTRER le code (???)
set: mettre {score} a [10]
say: ecrire "bonjour"
```

## Types de blocs connus

- `event` : bloc de debut
- `move` : action
- `wait` : attente
- `say` : texte / affichage
- `set` : affectation
- `if` : condition
- `repeat` : boucle
- `controla` : bloc simple de controle
- `control` : bloc de controle avec contenu
- `fin` ou `end` : bloc de fin

Tu peux aussi inventer d'autres types : ils seront rendus avec un style par defaut, ou redefinis via le front matter YAML.

## Front matter YAML optionnel

Tu peux personnaliser les couleurs et les formes au debut du fichier.

```text
---
types:
  event:
    colour: "#22b573"
  fin:
    shape: cap
    colour: "#22b573"
---
event: DEBUT
move: AVANCER
fin: FIN
```

Formes disponibles :

- `stack`
- `hat`
- `cblock`
- `cap`

## Regles utiles

- indentation en multiples de `2` espaces
- pas de tabulations
- un bloc enfant doit etre sous un bloc parent reel
- `cap` termine une pile de blocs
- `hat` ne peut apparaitre qu'en haut d'un programme
