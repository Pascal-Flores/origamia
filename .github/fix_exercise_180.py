import re
from pathlib import Path

base = Path("src/exercises/pil-conception-algorithmes-sequence-repetition/cmp-repetition-n")

ops = [
("left",90),("forward",150),("right",90),("forward",70),("right",90),
("forward",150),("right",90),("forward",70),("right",90),
("penup",None),("forward",30),("right",90),("pendown",None),("forward",70),("backward",70),("left",90),
("penup",None),("forward",30),("right",90),("pendown",None),("forward",70),("backward",70),("left",90),
("penup",None),("forward",30),("right",90),("pendown",None),("forward",70),("backward",70),("left",90),
("penup",None),("forward",30),("right",90),("pendown",None),("forward",70),("backward",70),("left",90),
("penup",None),("right",90),("forward",90)]
solution = [
"# Solution de l'exercice 180 - L'échelle de la cabane",
"# Le programme reste développé : aucune boucle.",
"",
"from turtle import *",
""]
for name, value in ops:
    solution.append(f"{name}()" if value is None else f"{name}({value})")
(base / "180/solution.py").write_text("\n".join(solution) + "\n", encoding="utf-8", newline="\n")

(base / "180.md").write_text("""---
nom: L'échelle de la cabane
description: Dans l'interface Turtle, un programme sans boucle trace le cadre d'une échelle puis répète quatre fois le même groupe de sept instructions pour ajouter les quatre barreaux intermédiaires. L'élève indique le nombre de répétitions.
competence: cmp-repetition-n
attendu: att-repetition-n-cm1
type: free
statut: wip
essais: 2
situation: rit-dessiner-pictogramme-echelle
media: interface
link: N/A
---

# Contexte

Pour une affiche représentant une cabane en hauteur, un programme Turtle trace une **échelle à six barreaux**.

Le programme commence par tracer le cadre de l'échelle : les deux montants, le barreau du bas et le barreau du haut. Ensuite, le même morceau de sept instructions revient plusieurs fois pour ajouter les barreaux du milieu.

# Consigne

Combien de fois ce morceau est-il répété ? Écris uniquement le nombre.

# Solution

4

# Feedback essai 1

Après le tracé du cadre, repère chaque morceau qui commence par `lever le stylo` et se termine par `tourner à gauche de 90°`.

# Feedback

Le morceau `lever le stylo` → `avancer 30` → `tourner à droite de 90°` → `baisser le stylo` → `avancer 70` → `reculer 70` → `tourner à gauche de 90°` apparaît **4 fois**. Chaque répétition ajoute un barreau intermédiaire. Le cadre et les quatre barreaux intermédiaires forment une échelle complète à six barreaux.
""", encoding="utf-8", newline="\n")

section = """## Variante 180

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

"""
wip_path = base / "10-wip.md"
wip = wip_path.read_text(encoding="utf-8")
wip = re.sub(r"## Variante 180\n.*?(?=## Retours utilisateur pris en compte)", section, wip, flags=re.S)
note = "- 2026-09-02 : le rendu suivant présente une échelle cassée : le montant droit s’arrête avant le dernier barreau et le montant gauche dépasse sous celui-ci. Refonte géométrique : cadre fermé de 70 × 150 pixels, quatre barreaux intermédiaires ajoutés par le motif répété, aucun segment au-delà du cadre.\n"
if note not in wip:
    wip = wip.replace("\n## Validations utilisateur", "\n" + note + "\n## Validations utilisateur")
wip_path.write_text(wip, encoding="utf-8", newline="\n")
