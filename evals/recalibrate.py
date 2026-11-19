#!/usr/bin/env python3
"""Post-hoc recalibration: keep the reviewer's ranking, spread its scores to the human scale.

The skill (and a bare prompt) put almost every paper in the middle: of 430 skill reviewer
Overalls only 4 are 5, and the bare prompt never gives ICLR 8. The ranking carries signal
(Spearman ~0.44 with the human mean); the scale does not. This script fits, on the train split
only, a monotone map from a raw signal to the human mean rating (ICLR scale), and reports on the
test split what changes and what does not.

Maps (all fitted on train):
  quantile   the paper's mid-rank in the train signal distribution -> the same quantile of the
             train human means. Spreads the scores to the human distribution.
  linear     least squares of human mean on the signal (shrinks toward the mean; for reference)
Accept rule: accept when the signal is at or above the train threshold that accepts the train
accept rate (the venue's rate), i.e. the top fraction by signal.

Spearman and AUC are invariant to a monotone map; they say how much of the ranking survives
on test. Spread, MAE and accept-side agreement are what the recalibration changes.

Input: evals/iclr2026_full_scores.json (skill signals), the bare results dir (summary.json
rating, confidence as the tie-breaker), the sample (split, decision, human scores).
Output: numbers and paper ids only.
"""
import argparse
import bisect
import glob
import json
import os
import random
import statistics
from pathlib import Path

ICLR = (0, 2, 4, 6, 8, 10)


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


def spearman(a, b):
    ra, rb = rank(a), rank(b)
    ma, mb = statistics.mean(ra), statistics.mean(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
    return num / den if den else None


def auc(score, label):
    pos = [s for s, l in zip(score, label) if l]
    neg = [s for s, l in zip(score, label) if not l]
    if not pos or not neg:
        return None
    w = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return w / (len(pos) * len(neg))


def boot(rows, stat, reps, seed=0):
    rnd = random.Random(seed)
    vals = []
    for _ in range(reps):
        s = [rows[rnd.randrange(len(rows))] for _ in rows]
        v = stat(s)
        if v is not None:
            vals.append(v)
    vals.sort()
    return [round(vals[int(0.025 * len(vals))], 3), round(vals[int(0.975 * len(vals)) - 1], 3)]


def quantile_map(train_sig, train_hum):
    """Mid-rank of x among the train signals -> that quantile of the train human means."""
    sig = sorted(train_sig)
    hum = sorted(train_hum)
    n = len(sig)

    def f(x):
        lo, hi = bisect.bisect_left(sig, x), bisect.bisect_right(sig, x)
        q = (lo + hi) / 2 / n            # mid-rank quantile, ties share one value
        pos = min(max(q * (n - 1), 0), n - 1)
        i = int(pos)
        frac = pos - i
        return hum[i] if i + 1 >= n else hum[i] * (1 - frac) + hum[i + 1] * frac
    return f


def linear_map(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    vx = sum((a - mx) ** 2 for a in x)
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / vx if vx else 0.0
    return lambda v: my + b * (v - mx)


def hist(vals):
    """Rounded to the ICLR grid (0/2/4/6/8/10)."""
    out = {str(g): 0 for g in ICLR}
    for v in vals:
        out[str(min(ICLR, key=lambda g: abs(g - v)))] += 1
    return out


def r3(x):
    return None if x is None else round(x, 3)


def evaluate(name, train, test, reps):
    """train/test rows: {pid, sig, hum, acc}. Fit on train, report on test."""
    ts, th = [r["sig"] for r in train], [r["hum"] for r in train]
    qm, lm = quantile_map(ts, th), linear_map(ts, th)
    rate = statistics.mean(r["acc"] for r in train)
    k = max(1, round(rate * len(train)))
    # with ties, the distinct value whose accept count on train is closest to k
    thr = min(sorted(set(ts)), key=lambda t: (abs(sum(v >= t for v in ts) - k), -t))
    sig = [r["sig"] for r in test]
    hum = [r["hum"] for r in test]
    acc = [r["acc"] for r in test]
    q = [qm(s) for s in sig]
    lin = [lm(s) for s in sig]
    pred = [s >= thr for s in sig]

    def side(rows):
        return statistics.mean((r["sig"] >= thr) == r["acc"] for r in rows)

    def sp(rows):
        return spearman([r["sig"] for r in rows], [r["hum"] for r in rows])

    def au(rows):
        return auc([r["sig"] for r in rows], [r["acc"] for r in rows])
    tp = sum(p and a for p, a in zip(pred, acc))
    return {
        "signal": name, "n_train": len(train), "n_test": len(test),
        "train_spearman": r3(spearman(ts, th)),
        "test_spearman": r3(sp(test)), "test_spearman_ci": boot(test, sp, reps),
        "test_auc_accept": r3(au(test)), "test_auc_ci": boot(test, au, reps),
        "distinct_raw_values_test": len(set(sig)),
        "accept_rule": {"train_accept_rate": r3(rate), "threshold_signal": thr,
                        "test_predicted_accept": sum(pred), "test_true_accept": sum(acc),
                        "true_accept_hit": tp, "false_accept": sum(pred) - tp,
                        "accept_side_agree": r3(side(test)),
                        "accept_side_ci": boot(test, side, reps)},
        "spread_sd": {"human_mean": r3(statistics.pstdev(hum)),
                      "quantile": r3(statistics.pstdev(q)),
                      "linear": r3(statistics.pstdev(lin))},
        "mae_vs_human_mean": {"quantile": r3(statistics.mean(abs(a - b) for a, b in zip(q, hum))),
                              "linear": r3(statistics.mean(abs(a - b) for a, b in zip(lin, hum)))},
        "hist_test": {"human_mean": hist(hum), "quantile": hist(q), "linear": hist(lin)},
        "test_papers": [{"pid": r["pid"], "raw": r["sig"], "quantile": round(v, 2),
                         "human_mean": r["hum"], "accepted": r["acc"]}
                        for r, v in sorted(zip(test, q), key=lambda t: -t[1])],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--sample", default="evals/work/benchmarks/iclr2026/sample.jsonl")
    ap.add_argument("--skill", default="evals/iclr2026_full_scores.json")
    ap.add_argument("--bare", default="evals/work/dl/bare86/x")
    ap.add_argument("--json")
    ap.add_argument("--reps", type=int, default=2000)
    a = ap.parse_args()
    sample = {x["paper_id"]: x for x in map(json.loads, open(a.sample))}
    skill = {p["paper_id"]: p for p in json.loads(Path(a.skill).read_text())["papers"]}
    bare = {}
    for d in glob.glob(os.path.join(a.bare, "*")):
        f = Path(d) / "summary.json"
        if f.exists():
            s = json.loads(f.read_text())
            if isinstance(s.get("rating"), (int, float)):
                # confidence breaks ties: a confident 4 is lower than an unsure 4
                c = s.get("confidence") or 3
                bare[s["id"].split("-")[-1]] = s["rating"] + (0.01 * (3 - c) if s["rating"] <= 4
                                                             else 0.01 * (c - 3))

    def rows(get):
        out = {"train": [], "test": []}
        for pid, x in sample.items():
            v = get(pid)
            if v is None:
                continue
            out[x["split"]].append({"pid": pid, "sig": float(v), "hum": x["mean_human"],
                                    "acc": bool(x["accepted"])})
        return out

    signals = {
        "skill.final_overall": lambda p: skill.get(p, {}).get("final_overall"),
        "skill.panel_rating_1_6": lambda p: skill.get(p, {}).get("panel_rating_1_6"),
        "skill.eic_rating_1_6": lambda p: skill.get(p, {}).get("eic_rating_1_6"),
        "skill.reviewer_pool": lambda p: skill.get(p, {}).get("reviewer_pool"),
        "skill.eic_pool": lambda p: skill.get(p, {}).get("eic_pool"),
        "bare.rating(+confidence)": lambda p: bare.get(p),
    }
    out = {"note": "Post-hoc monotone recalibration fitted on the train split, evaluated on the "
                   "test split (sample.jsonl splits). Human target: mean ICLR rating. Numbers "
                   "and paper ids only.", "results": []}
    for name, get in signals.items():
        r = rows(get)
        if len(r["train"]) >= 10 and r["test"]:
            out["results"].append(evaluate(name, r["train"], r["test"], a.reps))
    txt = json.dumps(out, indent=1)
    if a.json:
        Path(a.json).write_text(txt + "\n")
    for res in out["results"]:
        ar = res["accept_rule"]
        print(f"{res['signal']:28s} rho_tr {res['train_spearman']} rho_te {res['test_spearman']} "
              f"{res['test_spearman_ci']} auc {res['test_auc_accept']} {res['test_auc_ci']} "
              f"sd hum/q/lin {res['spread_sd']['human_mean']}/{res['spread_sd']['quantile']}/"
              f"{res['spread_sd']['linear']} mae q/lin {res['mae_vs_human_mean']['quantile']}/"
              f"{res['mae_vs_human_mean']['linear']} acc pred {ar['test_predicted_accept']} "
              f"hit {ar['true_accept_hit']}/{ar['test_true_accept']} FA {ar['false_accept']} "
              f"side {ar['accept_side_agree']}")
        print("   hist q", res["hist_test"]["quantile"], "human", res["hist_test"]["human_mean"])


if __name__ == "__main__":
    main()
