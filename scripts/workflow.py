"""Reproducible deterministic retrieval checks; LLM synthesis is reviewed input, not an API call."""
import argparse,datetime,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
QUERIES=[
 ('員工筆電出現奇怪程式，先看哪種工具？','endpoint'),
 ('密碼被偷，登入那關如何加強？','identity'),
 ('進了公司內網，就可以直接信任嗎？','zero-trust'),
 ('要怎麼看員工可以使用哪些資源？','identity'),
 ('連線到不明應用時怎麼管？','network'),
 ('如何從年度合約理解經常性收入？','metrics')]
ALIASES={'筆電':'端點','奇怪程式':'EDR','密碼被偷':'MFA','公司內網':'零信任','員工可以':'授權','年度合約':'ARR','經常性收入':'ARR'}

def retrieve(query,entries,mode='improved'):
    if mode=='baseline':
        terms=query.lower().split() # v1: whitespace tokens; poor for Chinese questions
    else:
        vocabulary={t for e in entries for t in e['tags']}
        terms={t.lower() for t in vocabulary if t.lower() in query.lower()}
        terms.update(v.lower() for k,v in ALIASES.items() if k in query)
    scores=[]
    for e in entries:
        text=(e['title']+' '+e['body']+' '+' '.join(e['tags'])).lower()
        score=sum(1 for t in terms if t and t in text)
        # Exact concept tags take priority over incidental mentions in prose.
        if mode!='baseline': score+=sum(2 for t in terms if t in [x.lower() for x in e['tags']])
        if score: scores.append(dict(id=e['id'],score=score,sources=e['sources']))
    return sorted(scores,key=lambda d:-d['score'])[:3]

def run(mode):
    sources=json.loads((ROOT/'intake/sources.json').read_text())
    entries=json.loads((ROOT/'wiki/entries.json').read_text())
    errors=[]
    ids={s['id'] for s in sources}
    if len(ids)<5: errors.append('來源不足五篇')
    for s in sources:
        for k in ['url','locator','publisher','retrieved','kind','summary','caveat']:
            if not s.get(k): errors.append(s['id']+' 缺少 '+k)
    for e in entries:
        if not e['sources'] or not set(e['sources'])<=ids: errors.append(e['id']+' 來源無效')
    rows=[]
    for query,expected in QUERIES:
        results=retrieve(query,entries,mode)
        rows.append(dict(query=query,expected=expected,results=results,top1_correct=bool(results and results[0]['id']==expected)))
    log=dict(mode=mode,executed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_count=len(sources),wiki_count=len(entries),metadata_errors=errors,queries=rows,
        zero_hits=sum(not r['results'] for r in rows),top1_correct=sum(r['top1_correct'] for r in rows),
        input_sha256=hashlib.sha256((ROOT/'wiki/entries.json').read_bytes()).hexdigest(),
        scope='固定六題的關鍵字檢索測試，不代表完整語意搜尋品質；不檢驗事實真偽。')
    (ROOT/'runs'/f'{mode}.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:log[k] for k in ['mode','source_count','wiki_count','zero_hits','top1_correct','metadata_errors']},ensure_ascii=False))
    return log

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['baseline','improved'],default='improved');a=p.parse_args();run(a.mode)
