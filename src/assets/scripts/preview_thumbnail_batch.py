#!/usr/bin/env python3
"""Build review sheets and an index from already-composed exercise thumbnails."""
import argparse
import csv
import html
import json
import math
import re
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]/'thumbnails'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--first',type=int,default=1)
parser.add_argument('--last',type=int,default=240)
args=parser.parse_args()
tasks=json.loads((ROOT/'alt-texts.json').read_text())
assert [t['id'] for t in tasks]==list(range(1,241)), 'Expected one alternative text per exercise, in order.'
assert len({t['file'] for t in tasks})==240, 'Duplicate thumbnail file.'
assert all(t['alt'].strip()==t['alt'] and t['alt'] for t in tasks), 'Empty or malformed alternative text.'
layout=json.loads((ROOT/'layout.json').read_text())
bg=Image.open(ROOT/'template.png').convert('RGB')
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13)
title_font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
selected=[]
warnings=[]
for t in tasks:
    stem=Path(t['file']).stem
    f=ROOT/(stem+'.png')
    if not f.exists():continue
    with Image.open(f) as image:
        assert image.size==(layout['width'],layout['height']),f
        image=image.convert('RGB')
        assert image.getpixel((0,0))==bg.getpixel((0,0)),f
        diff=ImageChops.difference(image,bg)
        box=diff.convert('L').point(lambda v:255 if v>=8 else 0).getbbox()
        if box is None: warnings.append([t['id'],'empty'])
        else:
            center=((box[0]+box[2])/2,(box[1]+box[3])/2)
            if max(abs(center[0]-layout['circle']['center_x']),abs(center[1]-layout['circle']['center_y']))>1.5:
                warnings.append([t['id'],'visible-center',center])
    with Image.open(ROOT/'illustrations'/(stem+'.png')) as source:
        assert source.mode=='RGBA',stem
        alpha_min,alpha_max=source.getchannel('A').getextrema()
        assert alpha_min==0 and alpha_max>=250,stem
    if args.first<=t['id']<=args.last:selected.append(t)

sheets=[]
for start in range(args.first,args.last+1,15):
    group=[t for t in selected if start<=t['id']<start+15]
    if not group:continue
    end=min(start+14,args.last)
    canvas=Image.new('RGB',(1080,64+math.ceil(len(group)/3)*265),'#f4f5f7')
    draw=ImageDraw.Draw(canvas)
    draw.text((16,16),f'Origamia · Exercices {start} à {end}',font=title_font,fill='#2f3366')
    for i,t in enumerate(group):
        x=16+(i%3)*354;y=58+(i//3)*265
        stem=Path(t['file']).stem
        canvas.paste(Image.open(ROOT/(stem+'.png')).convert('RGB'),(x,y))
        label=f"{t['id']} · {t['alt']}"
        while draw.textlength(label,font=font)>340:label=label[:-2]+'…'
        draw.text((x,y+233),label,font=font,fill='#2f3366')
    dest=ROOT/f'apercu-{start}-{end}.png'
    canvas.save(dest);sheets.append(dest.name)

lines=['# Vignettes Origamia — Exercices 16 à 240','',
       'Gabarit commun : 344 × 227 px, disque blanc de 138 px, illustration centrée dans 96 × 96 px. Fond défini dans `layout.json`.',
       '', 'Illustrations produites avec imagegen intégré ; prompts et originaux transparents conservés pour chaque exercice.', '',
       '## Aperçus', '']
for f in sorted(ROOT.glob('apercu-*.png'),key=lambda p:int(p.stem.split('-')[1])):
    lines.append(f'- [{f.stem}]({f.name})')
lines+=['','## Fichiers','','| Exercice | Texte alternatif | Vignette | Illustration | Prompt |','| --- | --- | --- | --- | --- |']
completed=0
for t in tasks:
    if t['id']<16:continue
    stem=Path(t['file']).stem
    if not (ROOT/(stem+'.png')).exists():continue
    completed+=1
    prompt_name=stem+('-correction-prompt.md' if (ROOT/'illustrations'/(stem+'-correction-prompt.md')).exists() else '-prompt.md')
    lines.append(f"| {t['id']} | {t['alt']} | [PNG]({stem}.png) | [Source](illustrations/{stem}.png) | [Prompt](illustrations/{prompt_name}) |")
lines+=['',f'{completed} vignettes enregistrées sur 225 demandées.','',
        'Interprétations : exercice 112, sonde d’humidité du sol ; exercice 193, pièce de puzzle bleue ; exercice 224, casquette à hélice (correction du mot « élite »).']
(ROOT/'index-16-240.md').write_text('\n'.join(lines)+'\n')
cards=[]
for t in tasks:
    stem=Path(t['file']).stem
    if not (ROOT/(stem+'.png')).exists():continue
    label=html.escape(f"{t['id']} · {t['alt']}")
    alt=html.escape(t['alt'],quote=True)
    cards.append((t['id'],f'<article data-search="{label}"><a href="{stem}.png"><img loading="lazy" src="{stem}.png" width="344" height="227" alt="{alt}"></a><p>{label}</p><a href="{stem}.png" download>Télécharger</a> · <a href="illustrations/{stem}.png">Illustration seule</a></article>'))
gallery='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Vignettes Origamia</title>
<style>body{font:16px system-ui;margin:32px;background:#f4f5f7;color:#2f3366}h1{font-size:26px}input{font:inherit;padding:12px;width:min(90%,420px);border:1px solid #a7cffe;border-radius:8px;margin:10px 0 24px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px}article{background:white;padding:12px;border-radius:12px}article img{width:100%;height:auto}article p{min-height:2.5em}a{color:#3353d6}article[hidden]{display:none}</style>
<h1>Vignettes Origamia — exercices FIRST à 240</h1><p>COUNT vignettes disponibles · 344 × 227 px</p><input type="search" placeholder="Rechercher un numéro ou un sujet" aria-label="Rechercher"><main>CARDS</main>
<script>const norm=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();document.querySelector('input').addEventListener('input',e=>{const q=norm(e.target.value);document.querySelectorAll('article').forEach(a=>a.hidden=!norm(a.dataset.search).includes(q))});</script></html>'''
for first in (1,16):
    subset=[card for number,card in cards if number>=first]
    (ROOT/f'galerie-{first}-240.html').write_text(gallery.replace('FIRST',str(first)).replace('COUNT',str(len(subset))).replace('CARDS',''.join(subset)))

# The JSON is the editable source; regenerate all readable exports from it.
with (ROOT/'alt-texts.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=['id','file','alt'])
    writer.writeheader()
    writer.writerows(tasks)
alt_lines=['# Textes alternatifs des 240 miniatures','',
           'Source : `alt-texts.json`. Le numéro reste une métadonnée ; le texte alternatif décrit uniquement le sujet.',
           '', '| Exercice | Miniature | Texte alternatif |', '| --- | --- | --- |']
for t in tasks:
    alt_lines.append(f"| {t['id']} | [PNG]({t['file']}) | {t['alt']} |")
(ROOT/'alt-texts.md').write_text('\n'.join(alt_lines)+'\n')

# Preserve the production notes in the original 1–15 index.
index=ROOT/'index.md'
content=index.read_text()
for t in tasks[:15]:
    content=re.sub(rf'^(\| {t["id"]} \| )[^|]+',lambda m:m[1]+t['alt']+' ',content,flags=re.M)
content=content.replace('| Exercice | Sujet |','| Exercice | Texte alternatif |')
index.write_text(content)
print(json.dumps({'completed':len(cards),'alternative_texts':len(tasks),'sheets':sheets,'warnings':warnings},ensure_ascii=False))
