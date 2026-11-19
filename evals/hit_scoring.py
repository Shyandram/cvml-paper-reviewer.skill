#!/usr/bin/env python3
"""Oracle check: score each paper from only the skill issues that hit a human issue.

Per paper (82 ICLR 2026 papers, skill 2.10.1 panel, issue_overlap annotations): the skill main
issues that match a human main issue (n_hit), those that do not (n_non), hits weighted by how
many human reviewers raised them (hit_w), and the hit share (hit_frac). Spearman against the
mean human rating and AUC for acceptance, raw and as leave-one-out linear fits. An upper bound:
the hit labels come from the human reviews and are not available for a new paper. Writes
evals/iclr2026_hit_scoring.json (ids and counts only).
"""
import json,sys,statistics,random
from pathlib import Path
sys.path.insert(0,"evals")
import issue_overlap as io, hit_conditional as hc
import pyarrow.parquet as pq
base=Path("evals/work/ov86"); ids=sorted(p.name for p in base.iterdir() if (p/"issues.json").exists())
t=pq.read_table("evals/work/dl/reviews.parquet",columns=["paper_id","rating","decision","review_src"],filters=[("paper_id","in",ids)]).to_pydict()
R={};D={}
for pid,r,dec,s in zip(t["paper_id"],t["rating"],t["decision"],t["review_src"]):
    if s=="openreview" and r is not None: R.setdefault(pid,[]).append(r); D[pid]=dec
final={p["paper_id"]:p for p in json.load(open("evals/iclr2026_full_scores.json"))["papers"]}
rows=[]
for pid in ids:
    if pid not in final: continue
    issues,match,revs,role=io.load_paper(base/pid,"issues.json",major_only=True)
    H={i["id"]:i for i in issues["H"]}; A=issues["A"]
    hit=[a for a in A if any(q in H for q in match.get(a["id"],()))]
    # weight of a hit: number of human reviewers raising the matched human issue(s)
    def hw(a): return len(set().union(*[H[q]["revs"] for q in match.get(a["id"],()) if q in H]))
    nrev=len(revs["H"])
    rows.append(dict(pid=pid,human=statistics.mean(R[pid]),acc="Accept" in str(D[pid]),
        panel=final[pid]["panel_rating_1_6"],n_all=len(A),n_hit=len(hit),n_non=len(A)-len(hit),
        hit_w=sum(hw(a) for a in hit)/nrev,hit_frac=len(hit)/max(1,len(A)),
        multi=sum(len(a["revs"]) for a in A),multi_hit=sum(len(a["revs"]) for a in hit),
        nH=len(H)))
sp=hc.spearman
def auc(x,y):
    pos=[a for a,b in zip(x,y) if b]; neg=[a for a,b in zip(x,y) if not b]
    return round(sum((p>n)+0.5*(p==n) for p in pos for n in neg)/(len(pos)*len(neg)),3)
hum=[r["human"] for r in rows]; acc=[r["acc"] for r in rows]
print("papers",len(rows),"accepted",sum(acc))
for k,sign in [("panel",1),("n_all",-1),("n_hit",-1),("n_non",-1),("hit_w",-1),("hit_frac",-1),("multi",-1),("multi_hit",-1),("nH",-1)]:
    x=[sign*r[k] for r in rows]
    print(f"{k:10s} spearman_vs_human={sp(x,hum)}  AUC_accept={auc(x,acc)}  mean={statistics.mean(r[k] for r in rows):.2f}")
# LOO linear fit human ~ a + b*x
def loo(keys):
    import itertools
    err=[];pred=[]
    for i in range(len(rows)):
        tr=[r for j,r in enumerate(rows) if j!=i]
        X=[[1]+[r[k] for k in keys] for r in tr]; y=[r["human"] for r in tr]
        # normal equations
        n=len(X[0]); XtX=[[sum(a[p]*a[q] for a in X) for q in range(n)] for p in range(n)]; Xty=[sum(a[p]*b for a,b in zip(X,y)) for p in range(n)]
        # solve
        M=[row[:]+[v] for row,v in zip(XtX,Xty)]
        for c in range(n):
            piv=max(range(c,n),key=lambda r:abs(M[r][c])); M[c],M[piv]=M[piv],M[c]
            for r in range(n):
                if r!=c:
                    f=M[r][c]/M[c][c]; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
        w=[M[r][n]/M[r][r] for r in range(n)]
        p=sum(a*b for a,b in zip(w,[1]+[rows[i][k] for k in keys])); pred.append(p); err.append(abs(p-rows[i]["human"]))
    return round(statistics.mean(err),3), sp(pred,hum), auc(pred,acc)
for keys in (["panel"],["n_all"],["n_hit"],["n_hit","n_non"],["hit_w"],["panel","n_hit","n_non"]):
    print("LOO",keys,"MAE,spearman,AUC =",loo(keys))
json.dump(rows,open("evals/iclr2026_hit_scoring.json","w"))
