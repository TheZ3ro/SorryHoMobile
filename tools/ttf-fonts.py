import pygame
from collections import OrderedDict
import json
pygame.init()
FONTSIZE=20
surfs={}
fonts = ['../font/GothamRnd-Medium.ttf','../font/GothamRnd-Bold.ttf']

mw,mh=0,0
hs={}

for f in fonts:
	font = pygame.font.Font(f, FONTSIZE)
	surfs[f] = {}

	for c in range(32,256):
		surf=font.render(chr(c),False,(0,0,0))
		surfs[f][c]=surf

	w,h=0,0
	for surf in surfs[f].values():
		w+=surf.get_width()
		h=max(h,surf.get_height())
	mw=max(w,mw)
	mh+=h
	hs[f]=h
	print(mw, mh, hs[f], surf.get_width())

mh+=(len(fonts)-1)*2

out=pygame.Surface((mw,mh))
out.fill((255,255,255))
outfont={}
h=0
for f in fonts:
	x=0
	print(h)
	outfont[f]=OrderedDict()
	for c in sorted(surfs[f].keys()):
		surf = surfs[f][c]
		out.blit(surf, (x,h))
		info=outfont[f][c]=OrderedDict()
		info['x']=x
		cw =info['w']=surf.get_width()
		info['h']=surf.get_height()
		x+=cw
	
	print(surf.get_width())
	h+=hs[f]+2

pygame.image.save(out,'font.png')
with open('font.json','wb') as f:
	json.dump(outfont,f)
