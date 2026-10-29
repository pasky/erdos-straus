#!/usr/bin/env python3
"""Driver for z51_linnik_forcing_es.c (EXSET_LINNIK §6): forcing reach of the ES Type II ratio classes R(M) at
Mordell-hard primes p (p mod 840 in {1,121,169,289,361,529}) near 10^k, at the actual p (mode 0) and at the plane
point (mode 1).  Output: data/z51_linnik/forcing_es.json.
Usage: z51_linnik_forcing_run.py k_list nprimes qmax"""
import subprocess, sys, json, math, os
HARD = {1, 121, 169, 289, 361, 529}
def isprime(n):
    if n < 2: return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0: return False
    return True
def hard_primes(start, k):
    out, n = [], start
    while len(out) < k:
        if n % 840 in HARD and isprime(n): out.append(n)
        n += 1
    return out
def run(p, qmax, PB, mode, exe):
    r = subprocess.run([exe, str(p), str(qmax), str(PB), str(mode)], capture_output=True, text=True, timeout=7200)
    rows = []
    for line in r.stdout.split("\n"):
        if not line.startswith("q="): continue
        f = dict(kv.split("=") for kv in line.split())
        rows.append({k: int(v) for k, v in f.items()})
    return rows
def main():
    ks = [int(x) for x in sys.argv[1].split(",")]; npr = int(sys.argv[2]); qmax = int(sys.argv[3])
    here = os.path.dirname(os.path.abspath(__file__))
    exe = "/tmp/z51_fes"
    subprocess.run(["gcc", "-O2", "-o", exe, os.path.join(here, "z51_linnik_forcing_es.c")], check=True)
    res = []
    for k in ks:
        for p in hard_primes(10 ** k, npr):
            for mode in (0, 1):
                rows = run(p, qmax, p, mode, exe)
                qstar = next((r["q"] for r in rows if r["reached"] < r["nonres"]), None)
                bands = {}
                for lo, hi in ((25, 50), (50, 100), (100, 150), (150, 200), (200, 300)):
                    sel = [r for r in rows if lo <= r["q"] < hi]
                    if sel: bands["%d-%d" % (lo, hi)] = round(sum(r["reached"] for r in sel) / sum(r["nonres"] for r in sel), 3)
                lab = [r["labels"] for r in rows if r["q"] >= 25]
                rec = dict(p=p, k=k, mode=mode, qstar=qstar, bands=bands,
                           mean_labels_q25plus=round(sum(lab) / max(1, len(lab)), 1),
                           log3=round(math.log(p) ** 3, 0))
                print(json.dumps(rec), flush=True)
                res.append(rec)
    os.makedirs(os.path.join(here, "..", "data", "z51_linnik"), exist_ok=True)
    with open(os.path.join(here, "..", "data", "z51_linnik", "forcing_es_%s.json" % sys.argv[1].replace(",", "_")), "w") as f:
        json.dump(res, f, indent=1)
if __name__ == "__main__":
    main()
