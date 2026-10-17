"""z17_penum2.py (O242): sharded, checkpointing, progress-logging version of the ac / cd regimes of z17_penum.py
(= m17b_penum.py, ET four-regime cover of the P-data at level K, r from env ZR).

Completeness: an N-point (a<=b) has e<=Xe or ad<=Xad or ac<=Xac or cd<=Xcd whenever Xe^2*Xad*Xac*Xcd >= n^2
(M17B Lemma 2.1).  z17_penum.py K e ad already ran with Xe = Xad = Xo (its own default); here the remaining two regimes are
run with freely chosen Xcd and Xac := ceil(n^2 / (Xo^3 * Xcd)), asserted to satisfy the cover inequality.
Sharding: pair (x, y) (= (a, c) resp. (c, d)) belongs to shard j iff (x + y) % S == j.  Each shard appends the data found in
every factor chunk to OUT (flushed), and logs one progress line per chunk to stderr; a killed shard loses <= 1 chunk
(rerun it from scratch, or resume with START = number of chunks already logged).
usage: ZR=17 python3 z17_penum2.py K REGIME Xo Xcd S j OUT [START]      REGIME in {ac, cd}"""
import sys, os, subprocess, time
R = int(os.environ.get("ZR", "17"))
K, REG, Xo, Xcd, S, J, OUT = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
START = int(sys.argv[8]) if len(sys.argv) > 8 else 0
n = R ** K
Xac = -(-n * n // (Xo ** 3 * Xcd))
assert Xo ** 3 * Xac * Xcd >= n * n
CH = 200000

def pairs_ac():
    for a in range(1, Xac + 1):
        c0 = (J - a) % S or S                    # least c >= 1 with (a + c) % S == J
        for c in range(c0, Xac // a + 1, S):
            if c % R: yield (a, c), n * c + a
def pairs_cd():
    for c in range(1, Xcd + 1):
        if c % R == 0: continue
        d0 = (J - c) % S or S
        for d in range(d0, Xcd // c + 1, S):
            if d % R: yield (c, d), 4 * c * c * d * n + 1
def total():
    X = Xac if REG == "ac" else Xcd
    t = 0
    for x in range(1, X + 1):
        if REG == "cd" and x % R == 0: continue
        y0 = (J - x) % S or S; m = X // x
        if m >= y0: t += (m - y0) // S + 1
    return t                                     # upper bound (ignores the y % R filter)

def divisors(fac):
    ds = [1]
    for p, e in fac.items(): ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def run():
    tot = total(); gen = pairs_ac() if REG == "ac" else pairs_cd()
    out = open(OUT, "a"); t0 = time.time(); done = 0; ch = 0; found = 0
    while True:
        keys, nums = [], []
        for k, m in gen:
            keys.append(k); nums.append(m)
            if len(nums) >= CH: break
        if not nums: break
        ch += 1; done += len(nums)
        if ch <= START: continue
        res = subprocess.run(["factor"], input="\n".join(map(str, nums)) + "\n", capture_output=True, text=True, check=True).stdout.split("\n")
        sols = []
        for (x, y), M, line in zip(keys, nums, res):
            lhs, rhs = line.split(":"); assert int(lhs) == M
            fac = {}
            for p in rhs.split(): p = int(p); fac[p] = fac.get(p, 0) + 1
            L = 4 * x * y
            for f in divisors(fac):
                if REG == "ac":
                    a, c = x, y
                    if (f + 1) % L == 0: sols.append((a, M // f, c, (f + 1) // L))
                else:
                    c, d = x, y; g = M // f
                    if (f + 1) % L == 0 and (g + 1) % L == 0: sols.append(((f + 1) // L, (g + 1) // L, c, d))
        for a, b, c, d in sols:
            if a >= 1 and b >= a and c >= 1 and d >= 1 and 4 * a * b * c * d == a + b + n * c and c % R and d % R:
                out.write(f"{a} {b} {c} {d}\n"); found += 1
        out.flush()
        el = time.time() - t0
        print(f"[{REG} {J}/{S}] chunk {ch} pairs {done}/{tot} ({100*done/tot:.1f}%) found {found} elapsed {el/3600:.2f}h "
              f"eta {el/max(1, done - START*CH)*(tot-done)/3600:.2f}h", file=sys.stderr, flush=True)
    print(f"[{REG} {J}/{S}] DONE K={K} Xo={Xo} Xac={Xac} Xcd={Xcd} pairs={done} found={found}", file=sys.stderr, flush=True)

run()
