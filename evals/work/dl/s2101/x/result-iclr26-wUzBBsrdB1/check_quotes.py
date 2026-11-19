import json, re, sys
base = "/home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/evals/work/"
paper = open(base + "papers/iclr26-wUzBBsrdB1/blinded.txt", encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
p = norm(paper)
ev = json.load(open(base + "results/iclr26-wUzBBsrdB1/evidence.json"))
for q in ev["quotes"]:
    if norm(q) not in p:
        print("MISSING:", q)
json.load(open(base + "results/iclr26-wUzBBsrdB1/summary.json"))
print("checked", len(ev["quotes"]))
