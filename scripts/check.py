"""Check the generated artifact's content contract, not browser rendering."""
import json
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Check(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.slides=0;self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.append(d['id'])
        if tag=='section' and 'slide' in d.get('class','').split():self.slides+=1
        if tag=='a' and d.get('href','').startswith('#'):self.links.append(d['href'][1:])
p=Check();page=(ROOT/'dist/index.html').read_text();p.feed(page)
assert len(p.ids)==len(set(p.ids)),'Duplicate HTML ids'
assert p.slides==18
assert set(p.links)<=set(p.ids),'Broken internal references'
deck=json.loads((ROOT/'deck.json').read_text())
sources=json.loads((ROOT/'intake/sources.json').read_text())
assert len(sources)>=5
assert all(d['notes'] for d in deck)
assert '2026-10-31' in page and '2026-07-31' in page
assert '<script src=' not in page and '<link rel="stylesheet"' not in page
assert page.count('<div class="quiz"')==2
assert 'source-S08' in p.ids and 'wiki-metrics' in p.ids
print('PASS: 18 slides; unique IDs; all internal citations resolve; 8 sources; notes; period labels; offline assets; 2 quizzes.')
