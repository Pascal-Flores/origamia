"""Build the proposed pedagogical DAG and its reviewable vector diagram.

Uses only the standard library. It reads the existing referential, never edits it.
Run from anywhere: python output/precedence-referentiel/generate_graph.py
"""
from pathlib import Path
import csv
import hashlib
import html
import itertools
import json
import sqlite3
import textwrap

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
DB = ROOT / 'src/assets/sql/referentiel.sqlite'
esc = html.escape

# Canonical identifiers label the graphic; names and source expectations
# remain available in the JSON, HTML and SVG tooltips.
specs = {
 'F': ('R4','identifier-formes-algorithme','representation',['Identifier les formes','d’écriture'],'Langage naturel · pseudo-code · blocs'),
 'P': ('C4','parametrer-instructions','conception',['Régler les paramètres','d’une instruction'],'Valeur · nom · durée · option'),
 'O': ('C1','ordre-sequence','conception',['Ordonner','une séquence'],'Actions et dépendances entre étapes'),
 'K': ('T1','cartographier-chaine-capteur','technique',['Reconstituer la chaîne','capteur → actionneur'],'Acquisition → traitement → action'),
 'V': ('R2','verifier-forme-representation','representation',['Vérifier la forme','d’une représentation'],'Complétude et cohérence de l’écriture'),
 'E': ('A1','expliquer-programme','analyse',['Expliquer un','programme'],'Actions · ordre · rôle des étapes'),
 'I': ('C2','entrees-sorties-etat','conception',['Repérer les entrées','et les sorties'],'Données initiales et résultat produit'),
 'R': ('C3','repetition-n','conception',['Répéter N fois'],'Motif répété et nombre de répétitions'),
 'M': ('T4','configurer-actionneur','technique',['Commander un','actionneur'],'Commande et réglages fixes'),
 'A': ('R1','associer-representations','representation',['Associer des','représentations'],'Reconnaître un sens équivalent'),
 'S': ('A2','simuler-programme','analyse',['Simuler l’exécution','d’un programme'],'Suivre les états et prévoir le résultat'),
 'L': ('T2','lire-capteur','technique',['Lire une information','de capteur'],'Mesure ou état réel, lié au besoin'),
 'T': ('R3','convertir-representations','representation',['Convertir des','représentations'],'Conserver le sens et la forme cible'),
 'D': ('A3','identifier-erreurs','analyse',['Repérer les erreurs'],'Comparer effets et résultat attendu'),
 'J': ('T3','piloter-actionneur-capteur','technique',['Relier capteur','et actionneur'],'Une mesure devient un réglage'),
 'C': ('A4','corriger-tests','analyse',['Corriger et vérifier','un programme'],'Choisir une correction sans régression'),
}

# An edge means a proposed introductory prerequisite, not mastery of all three
# grade-level expectations. No edges are selected on purely visual grounds.
relations = [
 ('F','V','Reconnaître les conventions d’une écriture pour juger si l’extrait respecte cette forme.','85–90, 201–204'),
 ('P','V','Repérer le rôle d’un paramètre pour détecter une instruction incomplète ou insuffisamment précise.','19–27 ; 82–90'),
 ('O','E','Comprendre que l’ordre des instructions détermine l’ordre des actions décrites.','1–9 ; 46–54'),
 ('O','I','Suivre l’ordre d’une transformation simple pour relier les données de départ à ce qui est produit.','28–30, 163–164'),
 ('O','R','Identifier une séquence avant de délimiter le motif répété et les actions à placer hors de la boucle.','10–18, 151–156'),
 ('K','M','Distinguer l’actionneur et son effet physique avant de choisir sa commande.','136–138 ; 118–120'),
 ('K','L','Distinguer acquisition et action pour reconnaître quel élément fournit la donnée recherchée.','136–138 ; 109–117'),
 ('P','M','Comprendre ce que règle un paramètre avant d’ajuster angle, puissance, volume, durée ou sens.','121–126, 225–228'),
 ('E','A','Interpréter les actions décrites avant de décider que deux écritures expriment la même instruction ou séquence.','46–48 ; 73–81'),
 ('E','S','Lire et comprendre les instructions avant de dérouler leurs effets depuis un état initial.','55–63, 181–186'),
 ('I','L','Distinguer une donnée réellement acquise d’un nombre ou d’un texte fixe affiché en sortie.','109–111, 217–218'),
 ('V','T','Reconnaître une représentation complète et cohérente pour choisir ou compléter la forme cible.','85–90 ; 94–99'),
 ('A','T','Reconnaître l’équivalence sémantique pour conserver les actions, les paramètres et l’ordre lors d’une conversion.','73–81 ; 91–99'),
 ('S','D','Prévoir les effets d’un programme pour les confronter à la mission et localiser ce qui empêche sa réussite.','37–45, 169–174'),
 ('D','C','Identifier le défaut à corriger et son effet pour choisir une modification utile, puis vérifier la réussite.','64–72, 187–192'),
 ('L','J','Identifier la donnée fournie par le capteur avant de la transmettre directement à un réglage.','127–135, 229–234'),
 ('M','J','Comprendre l’effet du réglage de l’actionneur avant de remplacer sa valeur fixe par une mesure.','127–135, 229–234'),
]

palette = {
 'conception': ('#216A8A','#EDF6FC','Conception d’algorithmes'),
 'analyse': ('#A36321','#FFF5E8','Analyse et critique'),
 'representation': ('#77549A','#F4EFFB','Représentations'),
 'technique': ('#267865','#ECF7F2','Objets techniques'),
}

conn = sqlite3.connect(f'file:{DB}?mode=ro',uri=True)
conn.row_factory = sqlite3.Row
source = {r['id_slug']:dict(r) for r in conn.execute('SELECT * FROM competences_referentiel')}
assert {'cmp-'+s[1] for s in specs.values()} == set(source)
pred = {k:[] for k in specs}
for a,b,*_ in relations: pred[b].append(a)
ranks = {}
while len(ranks)<len(specs):
    ready=[k for k in specs if k not in ranks and all(p in ranks for p in pred[k])]
    assert ready, 'Cycle in proposed prerequisites'
    for k in ready: ranks[k]=1+max((ranks[p] for p in pred[k]),default=0)
assert max(ranks.values())==5

# Transitive reduction check: every drawn relation adds reachability.
for a,b,*_ in relations:
    seen={a};pending=[a]
    while pending:
        n=pending.pop()
        for u,v,*_ in relations:
            if (u,v)!=(a,b) and u==n and v not in seen: seen.add(v);pending.append(v)
    assert b not in seen, (a,b,'redundant arc')

# Exact crossing minimization over rank permutations, with virtual vertices
# for long arcs. The result certifies the minimum for this layered routing
# model, not a universal lower bound over arbitrary graph drawings.
chains=[]
allranks=ranks.copy()
for i,(a,b,*_) in enumerate(relations):
    chain=[a]
    for r in range(ranks[a]+1,ranks[b]):
        dummy=f'd{i}_{r}';allranks[dummy]=r;chain.append(dummy)
    chain.append(b);chains.append(chain)
segments=[(a,b) for ch in chains for a,b in zip(ch,ch[1:])]
perms=[list(itertools.permutations([n for n in allranks if allranks[n]==r])) for r in range(1,6)]
costs=[0]*len(perms[0]);backs=[]
for rank in range(4):
    es=[(a,b) for a,b in segments if allranks[a]==rank+1]
    pairs=[(a,b,c,d) for i,(a,b) in enumerate(es) for c,d in es[i+1:] if a!=c and b!=d]
    positions=[{n:j for j,n in enumerate(p)} for p in perms[rank]]
    next_costs=[];back=[]
    for q in perms[rank+1]:
        qp={n:j for j,n in enumerate(q)}
        options=[costs[i]+sum((p[a]-p[c])*(qp[b]-qp[d])<0 for a,b,c,d in pairs) for i,p in enumerate(positions)]
        value=min(options);next_costs.append(value);back.append(options.index(value))
    costs=next_costs;backs.append(back)
index=costs.index(min(costs));ordering=[perms[4][index]]
for rank in range(3,-1,-1):index=backs[rank][index];ordering.insert(0,perms[rank][index])
assert min(costs)==2

# Positions keep the exact optimal top-to-bottom ordering while aligning
# the three longer strands. Virtual vertices route outside the cards.
centers={
 'F':320,'P':720,'K':1210,'O':1780,
 'V':320,'M':720,'d6_2':950,'I':1190,'E':1590,'R':1990,
 'd11_3':320,'d16_3':720,'L':1150,'A':1570,'S':1990,
 'T':420,'J':1150,'D':1990,'C':1990,
}
assert set(centers)==set(allranks)
for layer in ordering:assert list(layer)==sorted(layer,key=centers.get)
W,H=2374,920
NW,NH=326,100
centers={key:80+(position-320)*.45 for key,position in centers.items()}
xs={r:44+(r-1)*490 for r in range(1,6)}

svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
 '<title id="title">Graphe de précédence des 16 compétences</title>',
 '<desc id="desc">Cinq couches de compétences, de gauche à droite, reliées par leurs prérequis directs.</desc>',
 '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8.8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M1,1 L9,5 L1,9 Z" fill="#65798B"/></marker></defs>',
 f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
 '<g font-family="DejaVu Sans, Arial, sans-serif" fill="#1D3044">']
for r in range(1,6):
    svg.append(f'<rect x="{xs[r]-12}" y="18" width="{NW+24}" height="{H-36}" rx="18" fill="#F5F8FA"/>')

# Offset ports within a card according to the neighbouring node order.
def port(node,other,outgoing):
    neighbours=[(ch[1] if outgoing else ch[-2]) for ch in chains if (ch[0] if outgoing else ch[-1])==node]
    if len(neighbours)<2:return centers[node]
    neighbours.sort(key=centers.get)
    return centers[node]+(neighbours.index(other)-(len(neighbours)-1)/2)*22

paths=[]
for edge,chain in zip(relations,chains):
    a,b,reason,_=edge
    command=[]
    for j,(u,v) in enumerate(zip(chain,chain[1:])):
        y1=port(u,v,True) if j==0 else centers[u]
        y2=port(v,u,False) if j==len(chain)-2 else centers[v]
        x1=xs[allranks[u]]+NW;x2=xs[allranks[v]]
        if j==0:command.append(f'M{x1},{y1}')
        else:command.append(f'L{x1},{y1}')
        command.append(f'C{x1+70},{y1} {x2-70},{y2} {x2-4 if j==len(chain)-2 else x2},{y2}')
    path=' '.join(command)
    svg.append(f'<g><title>{esc(specs[a][0]+" → "+specs[b][0]+" : "+reason)}</title>')
    # White casing at intersections creates a visible non-junction bridge.
    svg.append(f'<path d="{path}" fill="none" stroke="#FFFFFF" stroke-width="11" stroke-linecap="round"/>')
    svg.append(f'<path d="{path}" fill="none" stroke="#65798B" stroke-width="2.4" marker-end="url(#arrow)" stroke-linecap="round"/></g>')
    paths.append({'source':a,'target':b,'path':path})

nodes=[]
for k,(code,slug,family,lines,hint) in specs.items():
    full=source['cmp-'+slug];x=xs[ranks[k]];y=centers[k]-NH/2;fg,bg,_=palette[family]
    expect=[dict(r) for r in conn.execute('SELECT id_slug,intitule,niveau FROM attendus_referentiel WHERE competence=?',('cmp-'+slug,))]
    nodes.append(dict(key=k,code=code,layer=ranks[k],short_label=' '.join(lines),prerequisites=[specs[p][0] for p in pred[k]],**full,attendus=expect))
    title=full['nom']+' — '+full['description']
    svg += [f'<g id="{esc(full["id_slug"])}"><title>{esc(title)}</title>',
       f'<rect x="{x}" y="{y+3}" width="{NW}" height="{NH}" rx="13" fill="#DFE6EC" opacity=".5"/>',
       f'<rect x="{x}" y="{y}" width="{NW}" height="{NH}" rx="13" fill="{bg}" stroke="{fg}" stroke-opacity=".32"/>',
       ]
    id_lines = textwrap.wrap(full['id_slug'],width=24,break_long_words=False,break_on_hyphens=True)
    assert ''.join(id_lines)==full['id_slug']
    text_y = y + (43 if len(id_lines)>1 else 57)
    for i,line in enumerate(id_lines):
        svg.append(f'<text x="{x+18}" y="{text_y+i*26}" font-family="DejaVu Sans Mono, monospace" font-size="20" font-weight="600">{esc(line)}</text>')
    svg.append('</g>')

svg.append('</g></svg>')
(OUT/'graphe-precedence.svg').write_text('\n'.join(svg),encoding='utf-8')

assumptions=[
 'Le graphe représente une proposition de progression pour entrer de façon autonome dans les familles de tâches. Il ne provient pas d’une table de prérequis officielle et n’a pas été validé expérimentalement.',
 'Un prérequis signifie disposer du socle introductif utile au niveau visé. Il ne signifie pas réussir tous les exercices CM1, CM2 et 6e de la compétence amont avant de commencer la compétence aval.',
 'La première couche n’exige aucune autre compétence de ce référentiel. Lecture de consignes, vocabulaire usuel, calcul élémentaire et repérage spatial restent des acquis extérieurs à ce graphe.',
 'La couche est calculée par 1 + le maximum des couches des prédécesseurs. Deux compétences d’une même couche n’ont aucune relation de précédence entre elles. Les branches progressent indépendamment.',
 'Le graphe ne conserve que les relations directes. La maîtrise des ancêtres indirects est transitive ; les dessiner de nouveau augmenterait les croisements sans ajouter de contrainte.',
]
decisions=[
 ('Pourquoi quatre points d’entrée ?', 'L’ordre peut s’enseigner avec des actions usuelles ; les paramètres avec une valeur à reporter ; les formes avec leurs indices visibles ; la chaîne technique avec un schéma fourni et un élément manquant. Aucune de ces introductions ne demande de réaliser les tâches des trois autres compétences.'),
 ('Pourquoi la répétition ne bloque-t-elle pas toutes les représentations ?', 'Les attendus CM1 et CM2 d’association et de conversion peuvent porter sur une instruction ou une séquence sans boucle. Ajouter C3 comme prérequis général bloquerait inutilement leur entrée. Pour les attendus att-associer-representations-6e et att-convertir-representations-6e, ajouter le socle C3 avant les tâches avec répétition : cette condition est locale à ces variantes.'),
 ('Pourquoi entrées-sorties et explication sont-elles parallèles ?', 'Ces deux compétences construisent des regards complémentaires à partir de la séquentialité : transformation de données pour C2, rôle des actions pour A1. Leur contenu se recouvre en partie ; les mettre dans une chaîne stricte artificielle ferait attendre un apprentissage qui peut commencer en parallèle.'),
 ('Pourquoi C2 ne bloque-t-elle pas la simulation ?', 'Les simulations de positions, de batterie ou de durée demandent de comprendre l’état initial et les effets des instructions, mais pas de maîtriser la désignation formelle des entrées et sorties. C2 renforce A2 ; A1 constitue ici son prérequis opératoire retenu. Pour lire un capteur, la distinction donnée réelle / valeur fixe devient en revanche centrale, ce qui justifie C2 → T2.'),
 ('Pourquoi reconnaître les formes ne bloque-t-il pas toute lecture ?', 'Il est possible de comprendre les actions d’un extrait présenté avec une légende sans savoir classer toutes ses formes d’écriture. R4 est donc reliée à la vérification formelle R2, où connaître la convention attendue est utile, sans devenir un passage obligé de tous les programmes.'),
 ('Pourquoi commencer la cartographie avant la lecture des capteurs ?', 'Au CM1, T1 demande de choisir l’élément ou l’effet manquant dans un schéma guidé. Ce premier repérage des rôles peut précéder les activités de sélection d’une donnée mesurée et de réglage d’un actionneur. Les tâches avancées de cartographie consolident ensuite ces rôles ; elles ne doivent pas être imposées avant l’entrée dans T2 ou T4.'),
 ('Pourquoi corriger un paramètre ne dépend-il pas de A4 ?', 'Les exercices T4 fournissent la commande et demandent d’en régler les valeurs ; ils n’exigent pas le diagnostic d’une séquence ni le classement de corrections selon leurs effets sur plusieurs tests. Le verbe « corriger » ne suffit donc pas à créer A4 → T4. Le socle C4 et le rôle de l’actionneur T1 sont les antécédents retenus.'),
 ('Pourquoi A3 précède-t-elle A4 ?', 'Pour choisir une correction de façon autonome, il faut relier l’erreur au résultat attendu. Le travail CM2 sur deux tests demande en plus de conserver le test déjà réussi. A2 est déjà un ancêtre via A3 : l’arc A2 → A4 serait redondant.'),
 ('Pourquoi T3 n’exige-t-elle pas de conditions ni de conversion numérique ?', 'Le référentiel limite explicitement les relations capteur–actionneur à une transmission directe, sans condition ni calcul de conversion. Les deux prérequis retenus sont donc la lecture d’une donnée et la compréhension du réglage de l’actionneur.'),
 ('Quelles réserves pédagogiques conserver ?', 'Les compétences sont larges : leurs attendus CM1, CM2 et 6e forment une progression en spirale et ne constituent pas des blocs indivisibles. Les tâches de cartographie CM2 et 6e se recouvrent notamment sur les chaînes à cinq éléments. Pour un moteur adaptatif imposant des blocages, décliner les arcs au niveau des 48 attendus et vérifier le modèle sur les réussites observées avant de l’utiliser comme règle obligatoire.'),
]
data={'title':'Graphe de précédence proposé — ORIGAMIA','date':'2026-10-02','source_sha256':hashlib.sha256(DB.read_bytes()).hexdigest(),
 'assumptions':assumptions,'nodes':nodes,'edges':[{'from':specs[a][0],'to':specs[b][0],'justification':why,'exercise_examples':examples} for a,b,why,examples in relations],
 'conditional_dependencies':[{'from':'C3','to':'R1','only_for':'att-associer-representations-6e'}, {'from':'C3','to':'R3','only_for':'att-convertir-representations-6e'}],
 'layout':{'orientation':'left-to-right','layers':[[specs[n][0] for n in row if n in specs] for row in ordering], 'crossings':2,'method':'Exact enumeration of within-layer permutations with dummy vertices; minimum for the chosen layered drawing model.'}}
(OUT/'graphe-precedence.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (OUT/'relations-precedence.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(['Prérequis','Compétence accessible','Justification','Exemples d’exercices'])
    for a,b,why,examples in relations:writer.writerow([specs[a][0],specs[b][0],why,examples])

htmlrows=''.join('<tr><td>'+str(n['layer'])+'</td><td><b>'+n['code']+'</b></td><td>'+esc(n['nom'])+'<small>'+esc(n['id_slug'])+'</small></td><td>'+(', '.join(n['prerequisites']) or 'Aucun dans le référentiel')+'</td></tr>' for n in sorted(nodes,key=lambda n:(n['layer'],n['code'])))
edgerows=''.join(f'<tr><td><b>{specs[a][0]} → {specs[b][0]}</b></td><td>{esc(why)}</td><td>{esc(examples)}</td></tr>' for a,b,why,examples in relations)
doc='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Précédence du référentiel — ORIGAMIA</title><style>body{font:17px/1.6 system-ui,sans-serif;color:#243647;max-width:1150px;margin:45px auto;padding:0 28px;background:#fff}h1{font-size:40px;line-height:1.2}h2{margin-top:48px}h3{font-size:19px;margin-bottom:8px}p{max-width:1000px}small{display:block;color:#687988;font-size:12px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid #dce4ea;text-align:left;vertical-align:top;padding:12px}th{background:#f3f6f8}img{width:100%;border:1px solid #e3e9ed}a{color:#216a8a}.sub{color:#667b8c}.note{background:#eff5f8;padding:18px 24px;border-radius:10px}</style>
<h1>Un parcours possible, des prérequis explicites</h1><p class="sub">ORIGAMIA · 2 octobre 2026 · 16 compétences, 48 attendus, 17 relations directes</p>
<p>Ce modèle propose une entrée progressive dans les compétences, à partir des attendus et des formats d’exercices du référentiel. Les arcs expriment un choix pédagogique argumenté. Ils ne certifient pas qu’un autre ordre serait impossible avec un accompagnement adapté.</p>
<p><a href="graphe-precedence.svg">Ouvrir le SVG vectoriel</a> · <a href="graphe-precedence.png">PNG pour Google Sheets</a> · <a href="graphe-precedence.json">Modèle et données source</a> · <a href="relations-precedence.csv">Relations en CSV</a></p>
<img src="graphe-precedence.svg" alt="Graphe des compétences en cinq couches">
<h2>Règles de lecture et portée du modèle</h2><ul>'''+''.join('<li>'+esc(a)+'</li>' for a in assumptions)+'''</ul>
<h2>Couches et prérequis directs</h2><table><thead><tr><th>Couche</th><th>Code</th><th>Compétence du référentiel</th><th>Prérequis directs</th></tr></thead><tbody>'''+htmlrows+'''</tbody></table>
<h2>Justification des 17 relations</h2><p>Les numéros renvoient aux exercices présents dans <code>referentiel.sqlite</code>. Ils illustrent la tâche qui motive la relation ; ils ne constituent pas une validation expérimentale du prérequis.</p><table><thead><tr><th>Relation</th><th>Raison retenue</th><th>Exercices</th></tr></thead><tbody>'''+edgerows+'''</tbody></table>
<h2>Choix pédagogiques et dépendances écartées</h2>'''+''.join('<h3>'+esc(q)+'</h3><p>'+esc(a)+'</p>' for q,a in decisions)+'''
<h2>Construction et contrôle du graphe</h2><p>Les 16 identifiants sont couverts une fois chacun. Le graphe est acyclique et chaque arc respecte l’ordre des couches. Aucun arc n’est transitivement redondant. L’ordre des cartes a été optimisé par énumération des permutations dans chaque couche, avec points de passage pour les arcs longs : deux croisements subsistent, minimum dans ce modèle de dessin par couches. Une coupure blanche aux intersections évite de les confondre avec une jonction.</p>
<p class="note">Les couches ne sont pas des classes scolaires. Une branche peut avancer dès que ses propres prérequis sont disponibles. La répétition devient un prérequis supplémentaire pour les variantes avancées de R1 et R3 qui comportent des boucles.</p></html>'''
(OUT/'analyse-precedence.html').write_text(doc,encoding='utf-8')
print(json.dumps({'nodes':len(nodes),'edges':len(relations),'layers':data['layout']['layers'],'crossings':min(costs),'output':str(OUT)},ensure_ascii=False))
