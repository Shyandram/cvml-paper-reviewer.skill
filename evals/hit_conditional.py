#!/usr/bin/env python3
"""Score agreement conditional on issue hits: does the skill weigh a problem as a human
reviewer does once both have found it?

Input: the `issue_overlap.py prepare` directory, annotated with issues.json (one per paper);
the human ratings and decisions (JerMa88 ICLR 2026 parquet); the skill's results (scores.json
per paper: the panel reviewers' Overall) and its final ratings (evals/iclr2026_full_scores.json).

For every human reviewer, the *first main point* is the first non-minor point of their
weaknesses text. It is a hit when its issue matches an issue the skill raised. Ratings are put
on the skill's 1-6 scale with ICLR 0/2/4/6/8/10 -> 1/2/3/4/5/6 (skill 4 = ICLR 6).

Reported (numbers and paper ids only; no review text):
  reviewers    human reviewers whose first main point was hit vs not: rating, skill final minus
               the reviewer's rating, accept-side agreement (skill >= 4 vs reviewer >= 6)
  strata       the same, within each human rating, so that the hit group is not just the
               negative reviewers (who write more weaknesses and are easier to hit)
  pairs        skill reviewer x human reviewer: the skill reviewer raised the human's first
               main point (same issue) vs did not; the skill reviewer's own Overall against
               the human's rating
  hit_by_rating  hit rate of the first main point by human rating (the selection check)
  papers       Spearman of the skill's panel rating with the mean human rating and with the
               mean rating of the hit reviewers only
  tiers        reject_clear / reject_borderline / accept: the above for the hit reviewers
"""
import argparse
import json
import random
import re
import statistics
from pathlib import Path

SCALE = {0: 1, 1: 1, 2: 2, 3: 2.5, 4: 3, 5: 3.5, 6: 4, 7: 4.5, 8: 5, 10: 6}


def skill_scale(r):
    return SCALE.get(int(round(r)), None)


def mean(x):
    x = [v for v in x if v is not None]
    return round(statistics.mean(x), 3) if x else None


def spearman(a, b):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2
            i = j + 1
        return r
    ra, rb = rank(a), rank(b)
    ma, mb = statistics.mean(ra), statistics.mean(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
    return round(num / den, 3) if den else None


def boot(rows, stat, reps=2000, seed=0):
    """Paper-clustered bootstrap CI of stat(rows); rows carry 'pid'."""
    by = {}
    for r in rows:
        by.setdefault(r["pid"], []).append(r)
    keys = sorted(by)
    rnd = random.Random(seed)
    vals = []
    for _ in range(reps):
        s = [r for _ in keys for r in by[keys[rnd.randrange(len(keys))]]]
        v = stat(s)
        if v is not None:
            vals.append(v)
    vals.sort()
    if len(vals) < 20:
        return None
    return [round(vals[int(0.025 * len(vals))], 3), round(vals[int(0.975 * len(vals)) - 1], 3)]


def summarize(rows, reps):
    def d(s):
        return mean([r["skill"] - r["human"] for r in s])

    def mae(s):
        return mean([abs(r["skill"] - r["human"]) for r in s])

    def side(s):
        return mean([(r["skill"] >= 4) == (r["human"] >= 4) for r in s])
    return {"n": len(rows), "papers": len({r["pid"] for r in rows}),
            "human_mean": mean([r["human"] for r in rows]),
            "skill_mean": mean([r["skill"] for r in rows]),
            "diff": d(rows), "diff_ci": boot(rows, d, reps) if rows else None,
            "mae": mae(rows), "accept_side_agree": side(rows),
            "accept_side_ci": boot(rows, side, reps) if rows else None}


def point_order(pid):
    m = re.match(r"[A-Z](\d+)\.(\d+)", pid)
    return int(m.group(2)) if m else 999


def load(d):
    ann = json.loads((d / "issues.json").read_text())
    key = json.loads((d / "blind_key.json").read_text())
    src = {rid[0]: v[0] for rid, v in key.items()}
    pts = {p["id"]: p for p in ann["points"]}
    issue_of, members = {}, {}
    for letter, lst in ann["issues"].items():
        for i in lst:
            members[i["id"]] = [pts[x] for x in i["points"] if x in pts]
            for x in i["points"]:
                issue_of[x] = i["id"]
    match = {}
    for c in ann.get("cross", []):
        for q in c.get("match", []):
            match.setdefault(c["p_issue"], set()).add(q)
            match.setdefault(q, set()).add(c["p_issue"])
    return ann, key, src, pts, issue_of, members, match


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dir")
    ap.add_argument("--reviews", required=True)
    ap.add_argument("--results", required=True, help="dir of <prefix>-<id> result dirs")
    ap.add_argument("--final", default="evals/iclr2026_full_scores.json")
    ap.add_argument("--json")
    ap.add_argument("--reps", type=int, default=2000)
    a = ap.parse_args()
    import pyarrow.parquet as pq
    base = Path(a.dir)
    ids = sorted(p.name for p in base.iterdir() if (p / "issues.json").exists())
    t = pq.read_table(a.reviews, columns=["paper_id", "reviewer_id", "rating", "decision",
                                          "review_src"],
                      filters=[("paper_id", "in", ids)]).to_pydict()
    rating, decision = {}, {}
    for pid, rid, r, dec, s in zip(t["paper_id"], t["reviewer_id"], t["rating"], t["decision"],
                                   t["review_src"]):
        if s == "openreview" and r is not None:
            rating[(pid, rid)] = float(r)
            decision[pid] = dec
    final = {p["paper_id"]: p for p in json.loads(Path(a.final).read_text())["papers"]}
    res = {d.name.split("-")[-1]: d for d in Path(a.results).iterdir()}

    reviewers, pairs, paper_rows = [], [], []
    for pid in ids:
        if pid not in final:
            continue
        ann, key, src, pts, issue_of, members, match = load(base / pid)
        ai_overall = {}
        sc = json.loads((res[pid] / "scores.json").read_text())
        for r in sc.get("reviewers", []):
            role = r["role"].split()[0]
            if isinstance(r.get("overall"), (int, float)):
                ai_overall[role] = r["overall"]
        skill = final[pid]["final_overall"]
        panel = final[pid]["panel_rating_1_6"]
        hum = [rid for rid, v in key.items() if v[0] == "H"]
        ratings_all = [rating.get((pid, key[h][1])) for h in hum]
        tier = ("accept" if "Accept" in str(decision.get(pid)) else
                "reject_borderline" if any(x is not None and x >= 6 for x in ratings_all)
                else "reject_clear")
        hit_ratings = []
        for h in hum:
            r = rating.get((pid, key[h][1]))
            if r is None:
                continue
            main_pts = sorted([p for p in pts.values() if p["reviewer"] == h and not p.get("minor")],
                              key=lambda p: point_order(p["id"]))
            if not main_pts:
                continue
            first = issue_of.get(main_pts[0]["id"])
            ai_issues = [q for q in match.get(first, ())
                         if any(not m.get("minor") for m in members.get(q, []))]
            raisers = {m["reviewer"] for q in ai_issues for m in members[q]}
            roles = {key[x][1] for x in raisers if x in key}
            hit = bool(ai_issues)
            hs = skill_scale(r)
            reviewers.append({"pid": pid, "tier": tier, "rating": r, "human": hs,
                              "skill": skill, "hit": hit, "n_main": len(main_pts)})
            if hit:
                hit_ratings.append(r)
            for role, ov in ai_overall.items():
                pairs.append({"pid": pid, "human": hs, "skill": ov, "same": role in roles})
        paper_rows.append({"pid": pid, "panel": panel,
                           "all": mean([x for x in ratings_all if x is not None]),
                           "hit": mean(hit_ratings) if hit_ratings else None})

    out = {"note": "Skill 2.10.1 (panel, Sonnet high) vs ICLR 2026 human reviewers, conditional "
                   "on whether the skill raised the reviewer's first main point (issue_overlap "
                   "annotation). Human ratings on the skill scale: ICLR 0/2/4/6/8/10 -> 1..6. "
                   "Numbers and paper ids only.",
           "papers": len(paper_rows)}
    out["reviewers"] = {"hit": summarize([r for r in reviewers if r["hit"]], a.reps),
                        "not_hit": summarize([r for r in reviewers if not r["hit"]], a.reps)}
    strata = {}
    for lo, hi, name in ((0, 2, "rating<=2"), (4, 4, "rating=4"), (6, 6, "rating=6"),
                         (8, 10, "rating>=8")):
        s = [r for r in reviewers if lo <= r["rating"] <= hi]
        strata[name] = {"hit_rate": mean([r["hit"] for r in s]),
                        "hit": summarize([r for r in s if r["hit"]], a.reps),
                        "not_hit": summarize([r for r in s if not r["hit"]], a.reps)}
    out["strata"] = strata
    out["hit_by_main_points"] = {
        name: mean([r["hit"] for r in reviewers if lo <= r["n_main"] <= hi])
        for lo, hi, name in ((1, 2, "1-2"), (3, 4, "3-4"), (5, 99, "5+"))}
    out["pairs"] = {"same_issue": summarize([p for p in pairs if p["same"]], a.reps),
                    "other": summarize([p for p in pairs if not p["same"]], a.reps)}
    both = [p for p in paper_rows if p["hit"] is not None]
    out["paper_spearman"] = {
        "n_all": len(paper_rows), "panel_vs_all_mean": spearman(
            [p["panel"] for p in paper_rows], [p["all"] for p in paper_rows]),
        "n_hit": len(both),
        "panel_vs_all_mean_same_papers": spearman([p["panel"] for p in both],
                                                  [p["all"] for p in both]),
        "panel_vs_hit_mean": spearman([p["panel"] for p in both], [p["hit"] for p in both])}
    out["tiers"] = {}
    for tier in ("reject_clear", "reject_borderline", "accept"):
        s = [r for r in reviewers if r["tier"] == tier]
        out["tiers"][tier] = {"hit": summarize([r for r in s if r["hit"]], a.reps),
                              "not_hit": summarize([r for r in s if not r["hit"]], a.reps)}
    txt = json.dumps(out, indent=1)
    if a.json:
        Path(a.json).write_text(txt + "\n")
    print(txt)


if __name__ == "__main__":
    main()
