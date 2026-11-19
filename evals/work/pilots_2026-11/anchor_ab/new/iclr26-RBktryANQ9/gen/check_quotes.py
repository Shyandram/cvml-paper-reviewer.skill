import json,re,sys
lines=open("reviewer_copy.txt").read().split("\n")
streams={"L":[],"R":[]}
for ln in lines:
    parts=[p for p in re.split(r"\s{6,}",ln.strip()) if p]
    if not parts: continue
    # assign by start column
    starts=[m.start() for m in re.finditer(r"\S+(?:\s{1,5}\S+)*",ln)]
    segs=re.findall(r"\S+(?:\s{1,5}\S+)*",ln)
    for st,sg in zip(starts,segs):
        streams["L" if st<70 else "R"].append(sg)
def norm(t):
    t=" ".join(t); t=re.sub(r"-\s+","",t); t=re.sub(r"\s+"," ",t); return t
full=norm(streams["L"])+" || "+norm(streams["R"])
full2=re.sub(r"\s+"," ",re.sub(r"-\s*\n\s*","","\n".join(lines)))
ev=json.load(open("evidence.json"))
for q in ev["quotes"]:
    qn=q.replace("-","")
    if q in full or q in full2 or qn in full.replace("-",""): continue
    print("MISSING:",q)
