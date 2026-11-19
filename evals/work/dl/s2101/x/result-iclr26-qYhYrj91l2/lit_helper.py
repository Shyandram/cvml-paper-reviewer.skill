import json, subprocess, sys, time
S = "/home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/academic-paper-reviewer/scripts/related_search.py"
F = "/home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/evals/work/results/iclr26-qYhYrj91l2/fingerprint.json"
for spec in sys.argv[1:]:
    query, purpose, tag = spec.split("|")
    time.sleep(4)
    out = subprocess.run(["python3", S, "search", "--fp", F, "--query", query, "--purpose", purpose, "--tag", tag, "--mode", "strict"], capture_output=True, text=True)
    t = out.stdout or out.stderr
    try:
        d = json.loads(t)
        print("Q:", d["query"], "returned", d["returned"], "kept", len(d["kept"]))
        for k in d["kept"][:12]:
            print("  -", k["date"], k["label"][:24], "|", k["title"][:100])
    except Exception:
        print("Q:", query, "->", t[:300])
