#!/usr/bin/env python3
"""Share of the human *important* issues the skill hit, against the skill's score and its error.

Per paper (skill 2.10.1 panel, issue_overlap annotations, ICLR 2026): the human main issues,
and three definitions of important: raised by 2+ human reviewers (consensus), raised by a
reviewer rating <= 4 (negative), or a reviewer's first or second main point (top). Recall =
share of them that a skill main issue matches. Related to the skill panel rating, the mean
human rating (on the skill scale, rating/2 + 1) and the error panel - human, by Spearman and
by recall tertile. Writes ids and numbers only.
"""
import json
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import hit_conditional as hc  # noqa: E402


def main():
    import pyarrow.parquet as pq
    base = Path(sys.argv[1] if len(sys.argv) > 1 else "evals/work/ov86")
    out = sys.argv[2] if len(sys.argv) > 2 else "evals/iclr2026_important_hits.json"
    ids = sorted(p.name for p in base.iterdir() if (p / "issues.json").exists())
    t = pq.read_table("evals/work/dl/reviews.parquet",
                      columns=["paper_id", "reviewer_id", "rating", "decision", "review_src"],
                      filters=[("paper_id", "in", ids)]).to_pydict()
    rating, dec = {}, {}
    for pid, rid, r, d, s in zip(t["paper_id"], t["reviewer_id"], t["rating"], t["decision"],
                                 t["review_src"]):
        if s == "openreview" and r is not None:
            rating[(pid, rid)] = r
            dec[pid] = d
    final = {p["paper_id"]: p for p in json.loads(Path("evals/iclr2026_full_scores.json")
                                                  .read_text())["papers"]}
    rows = []
    for pid in ids:
        if pid not in final:
            continue
        ann, key, src, pts, issue_of, members, match = hc.load(base / pid)
        hletter = next(k for k, v in key.items() if v[0] == "H")[0]
        major = lambda i: any(not m.get("minor") for m in members.get(i, []))  # noqa: E731
        H = [i["id"] for i in ann["issues"][hletter] if major(i["id"])]
        hit = {i for i in H if any(major(q) for q in match.get(i, ()))}
        rr = {h: rating.get((pid, key[h][1])) for h in key if key[h][0] == "H"}
        top = set()
        for h in rr:
            mp = sorted([p for p in pts.values() if p["reviewer"] == h and not p.get("minor")],
                        key=lambda p: int(re.sub(r".*\.", "", p["id"]) or 0))
            top |= {issue_of[p["id"]] for p in mp[:2]}
        revs = {i: {m["reviewer"] for m in members[i]} for i in H}
        sets = {"all": H,
                "consensus": [i for i in H if len(revs[i]) >= 2],
                "negative": [i for i in H if any((rr.get(r) or 10) <= 4 for r in revs[i])],
                "top": [i for i in H if i in top]}
        hum = statistics.mean(v for v in rr.values() if v is not None) / 2 + 1
        row = {"pid": pid, "panel": final[pid]["panel_rating_1_6"],
               "final": final[pid]["final_overall"], "human": round(hum, 3),
               "accepted": "Accept" in str(dec.get(pid))}
        for k, s in sets.items():
            row["n_" + k] = len(s)
            row["recall_" + k] = round(sum(i in hit for i in s) / len(s), 3) if s else None
        row["error"] = round(row["panel"] - hum, 3)
        rows.append(row)
    res = {"note": __doc__.split("\n")[0] + " Numbers and paper ids only.", "papers": len(rows),
           "by_definition": {}}
    for k in ("all", "consensus", "negative", "top"):
        s = [r for r in rows if r["recall_" + k] is not None]
        x = [r["recall_" + k] for r in s]
        tert = sorted(s, key=lambda r: r["recall_" + k])
        n3 = len(tert) // 3
        groups = {"low": tert[:n3], "mid": tert[n3:len(tert) - n3], "high": tert[len(tert) - n3:]}
        res["by_definition"][k] = {
            "n": len(s), "mean_recall": hc.mean(x),
            "spearman_vs_panel": hc.spearman(x, [r["panel"] for r in s]),
            "spearman_vs_human": hc.spearman(x, [r["human"] for r in s]),
            "spearman_vs_error": hc.spearman(x, [r["error"] for r in s]),
            "spearman_vs_abs_error": hc.spearman(x, [abs(r["error"]) for r in s]),
            "tertiles": {g: {"n": len(v), "recall": hc.mean([r["recall_" + k] for r in v]),
                             "panel": hc.mean([r["panel"] for r in v]),
                             "human": hc.mean([r["human"] for r in v]),
                             "error": hc.mean([r["error"] for r in v]),
                             "abs_error": hc.mean([abs(r["error"]) for r in v]),
                             "accepted": sum(r["accepted"] for r in v),
                             "false_accept": sum((r["final"] >= 4) and not r["accepted"] for r in v)}
                         for g, v in groups.items()}}
    res["papers_rows"] = rows
    Path(out).write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps(res["by_definition"], indent=1))


if __name__ == "__main__":
    main()
