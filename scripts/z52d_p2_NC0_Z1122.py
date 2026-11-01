"""Z1122: scheduling complementary certificate families (G4, NC0).
Jobs = distinct repo residue-certificate charts (Type I/II, s<=60, p=1 mod 4), deduplicated by covered set
(keep cheapest s). Cost proxy per attempt = s (the repo's certificate-size measure).
Schedules are per-prime sequential portfolios: try charts in order until one covers p.
  LCF : global least-cost-first order.
  RR  : round-robin = cyclic rotation of the cost-ordered list, start = (prime index mod K).
  RC  : residue-conditioned = order by train success-rate/cost for class p mod 840 (fallback LCF).
  ORA : oracle lower bound (cheapest covering chart), not a schedule.
Train: primes 1 mod 4 in (1e5, 5e5]; held-out test: primes 1 mod 4 in (1e6, 1.2e6]."""
import sys, json
sys.path.insert(0, "scripts")
import numpy as np
from z52d_p2_NC0_lib import primes_upto, families, covered_mask

ps = primes_upto(1_200_000)
ps = ps[(ps % 4 == 1) & (ps > 5)]
fams = families(60)
# dedupe on the covered set over ALL primes 1 mod 4 up to 1.2e6
seen = {}
for f in fams:
    key = covered_mask(f, ps).tobytes()
    if key not in seen or f["s"] < seen[key]["s"]:
        seen[key] = f
charts = sorted(seen.values(), key=lambda f: (f["s"], f["name"]))
K = len(charts)
cost = np.array([f["s"] for f in charts], dtype=float)
print(f"families s<=60: {len(fams)}; distinct covered sets (p=1 mod 4): {K}")
Cov = np.array([covered_mask(f, ps) for f in charts])  # K x N
train = (ps > 1e5) & (ps <= 5e5)
test = (ps > 1e6) & (ps <= 1.2e6)
Ctr, Cte = Cov[:, train], Cov[:, test]
pte = ps[test]
ptr = ps[train]
print(f"train primes {Ctr.shape[1]}, test primes {Cte.shape[1]}")
print(f"test coverage by union of {K} charts: {Cte.any(0).mean():.5f} (uncovered {(~Cte.any(0)).sum()})")
total = cost.sum()
LCF = np.arange(K)


def run(order_fn, C, pr):
    out = np.empty(C.shape[1])
    for i in range(C.shape[1]):
        order = order_fn(i, pr[i])
        hit = C[order, i]
        if hit.any():
            j = int(np.argmax(hit))
            out[i] = cost[order[: j + 1]].sum()
        else:
            out[i] = total
    return out


def first_hit_cost(order, C, i):
    hit = C[order, i]
    if hit.any():
        j = int(np.argmax(hit))
        return cost[order[: j + 1]].sum()
    return total


res = {}
# LCF
res["LCF"] = run(lambda i, p: LCF, Cte, pte)
# RR: rotation of cost-ordered list by prime index
res["RR"] = run(lambda i, p: np.roll(LCF, -(i % K)), Cte, pte)
# RC: residue-conditioned on p mod 840, learned on train
classes = ptr % 840
rate = {}
for r in np.unique(classes):
    m = classes == r
    rate[int(r)] = Ctr[:, m].mean(axis=1)
# order by rate/cost desc; unseen-classes -> LCF
def rc_order(i, p):
    r = int(p % 840)
    if r not in rate:
        return LCF
    score = rate[r] / cost
    return np.lexsort((cost, -score))  # primary: score desc, tie: cheaper first
res["RC"] = run(lambda i, p: rc_order(i, p), Cte, pte)
# ORACLE
ora = np.array([cost[Cte[:, i]].min() if Cte[:, i].any() else total for i in range(Cte.shape[1])])
res["ORA"] = ora

print(f"{'sched':6s} {'mean cost':>10s} {'median':>8s} {'p99':>8s} {'sum':>12s} {'unresolved':>10s}")
summary = {}
for k, v in res.items():
    unres = int((v == total).sum())
    summary[k] = dict(mean=float(v.mean()), median=float(np.median(v)), p99=float(np.quantile(v, .99)),
                      sum=float(v.sum()), unresolved=unres)
    print(f"{k:6s} {v.mean():10.2f} {np.median(v):8.1f} {np.quantile(v,.99):8.1f} {v.sum():12.0f} {unres:10d}")
print("per-prime regret vs oracle (mean extra cost):")
for k in ("LCF", "RR", "RC"):
    print(f"  {k}: {(res[k] - ora).mean():.2f}")
# residue-conditioned over-fit check: classes seen in train
print("train classes mod 840 seen:", len(rate), "; test primes with unseen class:",
      int(sum(1 for p in pte if int(p % 840) not in rate)))
json.dump(dict(K=K, total_cost=float(total), train=int(Ctr.shape[1]), test=int(Cte.shape[1]), summary=summary),
          open("data/z52b/pass2/NC0/sub/Z1122_sched.json", "w"), indent=1)
