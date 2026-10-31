"""Applies fix-round overrides to data/z52b/pass1/outcome_U03.jsonl (one line per mid)."""
import json
P = "data/z52b/pass1/outcome_U03.jsonl"
OV = {
"Z3183": ("nothing", "No residue class mod 840 is sterile at depth 10: over 96 unit classes (p=1 mod 4, p<=1e5) the fraction of primes with all C<=10 levels failing is at most 0.15 in any class; none is 1.0. Sterility is not a residue-mod-840 phenomenon at this depth.", ["skipped_fix.py"], "Repeat at depth 20-40 with more primes."),
"Z3118": ("nothing", "Window density of R_1(n)>0 (all n=1 mod 4, n<=1e5): mean 0.640 (sd 0.021) for windows of length 500, 0.640 (sd 0.010) for length 2000. Short-interval fluctuation shrinks like H^-1/2.", ["skipped_fix.py", "allN1mod4_RK.npz"], "Compare with multiplicative set density model."),
"Z3089": ("nothing", "Fraction of (p,C), C<=100, p<=1e5 (every 4th prime, n=119600) with a divisor = -1 mod 4C built from primes <= y: 0.0088 (y=5), 0.0136 (y=10), 0.0274 (y=30). Smooth-divisor witnesses are rare and grow slowly in y.", ["skipped_fix.py"], "Model with smooth-number counts over residue classes mod 4C."),
"Z3105": ("nothing", "For p<=1000 (1 mod 4), 89.4% of x in (p/4,p/2] give (4x-p)/(px) that is NOT a sum of two unit fractions (n=9137). Two-unit-fraction representability is the rare case, consistent with Erdos-Graham density.", ["skipped_fix.py"], "Compare with the Erdos-Graham density constant."),
"Z2093": ("nothing", "Schinzel admissibility of {4Cx+1: C<=100} holds at every prime q<=1000 (x=0 mod q always works). But for prime x=p, no prime p<=1e5 (p!=3) has both 4p+1 and 8p+1 coprime to 3, so the prime-variable instance is inadmissible in practice.", ["skipped_fix.py"], "None; the prime-variable version is ruled out by the mod-3 obstruction."),
}
rows = [json.loads(l) for l in open(P)]
n = 0
for r in rows:
    if r["mid"] in OV:
        o, s, e, x = OV[r["mid"]]
        r.update({"outcome": o, "summary": s, "evidence": ["scripts/z52b_p1_U03_" + e[0]] + e[1:] if False else ["scripts/z52b_p1_U03_skipped_fix.py", "data/z52b/pass1/U03/skipped_fix_results.json"], "next": x})
        n += 1
with open(P, "w") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
import collections
print("applied", n, collections.Counter(r["outcome"] for r in rows))
