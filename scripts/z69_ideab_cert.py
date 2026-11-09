#!/usr/bin/env python3
"""z69 IDEAB Phase 3.4: constructive finite-level certificates for UCOVER O2.
Search for an integer n, unit mod every prime <= M, with n = 1 (mod 840), n = r (mod 11), n a square modulo every prime
power prime to 11, such that n lies in NO family class (all seven ET families, superset enumeration) of modulus <= M.
Verification of the result does not use the squares-are-uncovered observation.
usage: cert.py M r seed [check_direct_limit] [smooth_survivor.json]
If a survivor file of z69_ideab_smooth.py is given, the coordinates at 2,3,5,7,11 are preset to that cylinder (which meets
no {2,3,5,7,11}-smooth class up to the level of that file) and only the primes >= 13 are searched. NOTE: only ONE lift of the
preset cylinder is tried (deeper digits 0); a failure says nothing about the other lifts."""
import sys, math, random, json, importlib.util
sys.setrecursionlimit(100000); sys.set_int_max_str_digits(0)
M = int(sys.argv[1]); R11 = int(sys.argv[2]); SEED = int(sys.argv[3]); DLIM = int(sys.argv[4]) if len(sys.argv) > 4 else 0
_argv = sys.argv; sys.argv = ["o2", "1e6", "8", "2"]
spec = importlib.util.spec_from_file_location("o2", "scripts/z69_ideab_o2.py"); o2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(o2)
sys.argv = _argv
random.seed(SEED)
PRESET = {}
if len(sys.argv) > 5:
    _J = json.load(open(sys.argv[5])); assert _J["r"] == R11
    PRESET = {int(q): int(v) for q, v in _J["residues"].items()}; PRESET_DEPTH = {int(q): int(v) for q, v in _J["depths"].items()}

def factor(m):
    f = {}; d = 2
    while d * d <= m:
        while m % d == 0: f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    return f

cls = o2.build(M)
primes = [q for q in range(2, M + 1) if all(q % d for d in range(2, int(q ** 0.5) + 1))]
vmax = {q: int(math.log(M, q) + 1e-9) for q in primes}
for q in primes:
    while q ** (vmax[q] + 1) <= M: vmax[q] += 1
    while q ** vmax[q] > M: vmax[q] -= 1
order = [11, 2, 3, 5, 7] + [q for q in primes if q > 11]
pos = {q: i for i, q in enumerate(order)}
groups = {q: [] for q in order}
nrel = 0
for m, S in cls.items():
    if m % 11: continue
    fm = factor(m); g = math.gcd(m, 840)
    key = max(fm, key=lambda q: pos[q])
    for rho in S:
        if rho % 11 != R11 or rho % g != 1 % g: continue
        groups[key].append((m, rho, fm)); nrel += 1
print(f"M={M} r={R11}: {sum(len(v) for v in cls.values())} classes, {nrel} relevant (11 | modulus, compatible with K_r)", flush=True)

def base_ok(q, t):
    if q == 11: return t % 11 == R11
    if q == 2: return t % 8 == 1 if vmax[2] >= 3 else t % (2 ** vmax[2]) == 1
    if q in (3, 5, 7): return t % q == 1
    return pow(t % q, (q - 1) // 2, q) == 1

assign = {}; stats = {"backtracks": 0, "minfrac": (1.0, None)}
def candidates(q):
    if q in PRESET:
        return [PRESET[q] % (q ** vmax[q])] if q ** vmax[q] <= q ** PRESET_DEPTH[q] else [PRESET[q]]
    forb = set()
    for m, rho, fm in groups[q]:
        if all(assign[s] % (s ** e) == rho % (s ** e) for s, e in fm.items() if s != q):
            forb.add((fm[q], rho % (q ** fm[q])))
    mod = q ** vmax[q]
    if not groups[q]:
        return [1] if q != 11 else [R11]
    base = [t for t in range(mod) if base_ok(q, t)]
    ok = [t for t in base if all(t % (q ** i) != r for i, r in forb)]
    frac = len(ok) / max(1, len(base))
    if frac < stats["minfrac"][0]: stats["minfrac"] = (frac, q)
    random.shuffle(ok)
    return ok

def search(i):
    if i == len(order): return True
    q = order[i]
    for t in candidates(q)[:40]:
        assign[q] = t
        if search(i + 1): return True
        stats["backtracks"] += 1
        if stats["backtracks"] > 200000: return False
    assign.pop(q, None)
    return False

ok = search(0)
print("search:", "SUCCESS" if ok else "NO CERTIFICATE FOUND (bounded search: <= 40 candidates per prime, <= 200000 backtracks; this is UNDECIDED, not a proof of coverage)", stats, flush=True)
if ok:
    n, L = 0, 1
    for q in order:
        mod = q ** vmax[q]
        n = (n + L * ((assign[q] - n) * pow(L, -1, mod) % mod)) % (L * mod); L *= mod
    assert n % 840 == 1 and n % 11 == R11 and all(n % q for q in primes)
    bad = [(m, n % m) for m, S in cls.items() if n % m in S]
    print(f"verification against ALL {sum(len(v) for v in cls.values())} classes of modulus <= {M}: violations = {len(bad)}", bad[:3], flush=True)
    nonsq = [q for q in primes if q not in (2, 11) and pow(n % q, (q - 1) // 2, q) != 1]
    print("n has", len(str(n)), "digits; primes (other than 11) where n is a non-residue:", nonsq[:5], flush=True)
    assert not bad, 'candidate violates a class: NOT a certificate (no file written)'
    json.dump({"M": M, "r": R11, "seed": SEED, "n": str(n), "L_is_lcm_of_prime_powers_le_M": True,
               "assign_small": {str(q): assign[q] for q in order if q < 200}, "stats": stats, "violations": len(bad)},
              open(f"data/z69/ideab/cert_M{M}_r{R11}{'_preset' if PRESET else ''}.json", "w"))
    if DLIM:
        cspec = importlib.util.spec_from_file_location("chk", "scripts/z69_ideab_o2_check.py")
        chk = importlib.util.module_from_spec(cspec); cspec.loader.exec_module(chk)
        dl = chk.direct_lambda(n, DLIM)
        print(f"direct test (divisibility conditions only, no table): least modulus of a class containing n, searched up to {DLIM}: {dl}"
              f"  ({DLIM + 1} means none)", flush=True)
