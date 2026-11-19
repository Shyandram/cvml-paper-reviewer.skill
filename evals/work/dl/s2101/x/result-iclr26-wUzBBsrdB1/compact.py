import sys, json
t = sys.stdin.read()
try:
    d = json.loads(t)
    print("Q:", d.get("query"), "returned", d.get("returned"), "kept", len(d.get("kept", [])))
    for k in d.get("kept", []):
        print(" -", k["date"], k["label"][:24], "|", k["title"][:110], "|", k["url"])
except Exception:
    print(t[:500])
