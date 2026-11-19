import sys, json
t = sys.stdin.read()
try:
    d = json.loads(t)
except Exception:
    print(t[:400])
    sys.exit()
print("Q:", d.get("query"), "returned", d.get("returned"), "kept", len(d.get("kept", [])))
for k in d.get("kept", []):
    print(" -", k["title"][:110], "|", k["date"], "|", k["label"][:26], "|", k["url"], "|", k.get("venue_evidence", "")[:60])
