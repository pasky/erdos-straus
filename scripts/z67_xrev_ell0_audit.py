"""Independent z67 ELL0 audit; no network, no writes, bounded arrays (< 2 MB sieve).
Extract side-agent/z67-ell0 into ROOT and compile ROOT/zsw and ROOT/zlev first.
Run: ulimit -v 6000000; timeout 1800 uv run --with mpmath --with numpy --with sympy \
  python scripts/z67_xrev_ell0_audit.py ROOT [s|t|r]
The t audit replaces the floating cutoff/exponent searches with exact integer inequalities.
"""
import importlib.util
import math
from fractions import Fraction
from pathlib import Path
import subprocess
import sys

from mpmath import iv

ROOT = Path(sys.argv[1]).resolve()


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def endpoint(x, side=1):
    sign, man, exp, _ = x._mpi_[side]
    return (-1 if sign else 1) * Fraction(man) * Fraction(2) ** exp


def s_audit():
    s = load("z67_ell0_sgap")
    s.BIN = str(ROOT / "zsw")
    s.KMAX = 7
    # All small primes and the ten largest recorded gap bounds (including 379).
    from sympy import primerange
    lines = (ROOT / "data/z67/ell0/sgap_102_1e5.txt").read_text().splitlines()
    rows = [line.split() for line in lines if not line.startswith("#")]
    worst = sorted(rows, key=lambda row: float(row[4].split("=")[1]), reverse=True)[:10]
    sample = sorted(set(primerange(11, 102)) | {int(row[0]) for row in worst} | {103, 1009, 99991})
    for p in sample:
        result = s.certify(p)
        assert result[-1] == "CERTIFIED"
        k = result[1]
        production = s.tail_upper(p, k)
        # Exact infinite polynomial-geometric series, independently enclosed at 80 digits.
        iv.dps = 80
        l = iv.mpf(p)
        r = 1 / iv.sqrt(l)
        a, b, m = iv.mpf("2.44") * iv.log(l), iv.mpf("10.15"), k + 1
        q = a * m * m + (2 * a + b) * m + 2 * b
        closed = l / (l - 1) * r**m * (
            q / (1 - r) + (2 * a * m + 2 * a + b) * r / (1 - r)**2
            + a * r * (1 + r) / (1 - r)**3)
        assert production >= endpoint(closed)
        assert production - endpoint(closed, 0) < Fraction(1, 10**35)
        print("S", p, "K", k, "bound", result[4], "tail outward verified")
    # S2' coefficient bounds: each normalized radical decreases for N >= 100000.
    n = iv.mpf(100000)
    z = iv.sqrt(n)
    x = iv.sqrt(2 * n) + 2
    assert (x / z).b < iv.mpf("1.4207").a
    assert ((iv.sqrt(n + x) + 2) / z).b < iv.mpf("1.01").a
    assert ((iv.sqrt(n / 2) + 4) / z).b < iv.mpf("0.72").a
    assert ((iv.sqrt(2 * n) + 4) / z).b < iv.mpf("1.43").a
    assert (1 + iv.log(iv.mpf("1.4207"))).b < iv.mpf("1.3512").a
    assert Fraction("2.02") * Fraction("1.3512") + Fraction("2.8414") + Fraction("1.44") < Fraction("7.02")
    assert Fraction("2.02") * Fraction("1.3512") + Fraction("2.8414") + Fraction("2.86") + Fraction("1.44") < Fraction("9.88")
    p = iv.mpf(100000)
    r, a, b = 1 / iv.sqrt(p), iv.mpf("2.44") * iv.log(p), iv.mpf("10.15")
    all_tail = p / (p - 1) * (a * r * (1 + r) / (1 - r)**3
                + (2 * a + b) * r / (1 - r)**2 + 2 * b * r / (1 - r))
    assert all_tail.b < iv.mpf("0.3655").a
    print("S2' constants and all-level bound at 100000:", all_tail.b)


def cutoff(e, r):
    """Least integer h with h**num >= r**den: all contributing primes are < h."""
    f = Fraction(e)
    target = r**f.denominator
    lo, hi = 1, 2
    while hi**f.numerator < target:
        hi *= 2
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if mid**f.numerator < target:
            lo = mid
        else:
            hi = mid
    return hi


def t_audit():
    t = load("z67_ell0_tbound")
    iv.dps = 60
    # Independent prime list; cutoff and maximizing exponent use exact arithmetic only.
    from sympy import primerange
    cap = max(cutoff(e, r) for r in (2, 3) for e in t.LNC[r])
    primes = list(primerange(2, cap))
    assert [int(p) for p in t._P if p < cap] == primes
    logs = {p: iv.log(p) for p in primes}
    lncs = {2: {}, 3: {}}
    maxa = {2: 0, 3: 0}
    largest_delta = 0.0
    for r in (2, 3):
        for e in t.LNC[r]:
            f, c = Fraction(e), cutoff(e, r)
            num, den = f.numerator, f.denominator
            original_cap = r ** (1.0 / float(e)) * (1 + 1e-9) + 2
            assert Fraction(original_cap) >= c
            eps, total = iv.mpf(e), iv.mpf(0)
            for p in primes:
                if p >= c:
                    break
                pn = p**num
                a = 0
                # Delta f(a+1) >= 0 iff (a+r)**den >= (a+1)**den * p**num.
                while (a + r)**den >= (a + 1)**den * pn:
                    a += 1
                heuristic = 0
                while math.log((heuristic + r) / (heuristic + 1)) - float(e) * math.log(p) >= 0:
                    heuristic += 1
                assert a == 0 or max(1, heuristic - 2) <= a <= heuristic + 2
                maxa[r] = max(maxa[r], a)
                value = iv.log(math.comb(a + r - 1, r - 1)) - a * eps * logs[p]
                total += iv.mpf(value.b)
            lncs[r][e] = iv.mpf(total.b)
            largest_delta = max(largest_delta, abs(float(total.b - t.LNC[r][e].b)))
            assert abs(endpoint(total) - endpoint(t.LNC[r][e])) < Fraction(1, 10**40)
        print("exact Euler-product audit:", r, "epsilons", len(lncs[r]), "max exponent", maxa[r])
    t.LNC = lncs
    s, rows = t.total(iv.mpf(2950), 300)
    tail, gain, ratio = t.tail(iv.mpf(2950), 300)
    total = s + tail
    assert total.b < iv.mpf("0.0408").a
    assert min(endpoint(x[4], 0) for _, row in rows for x in row) > Fraction(2, 2950)
    print("Euler log-constant max discrepancy:", largest_delta)
    print("independently certified total:", total.b)
    print("tail:", tail.b, "pair ratio:", ratio.b)
    print("level-29 A-cd:", iv.exp(rows[28][1][-1][2]).b)


def star(n):
    """All ordered (C,w,d), using 2dCw <= n and symmetry C <= w."""
    out = set()
    for d in range(1, n // 2 + 1):
        for c in range(1, math.isqrt(n // (2 * d)) + 1):
            w, rem = divmod(n + c, 4 * d * c - 1)
            if not rem and w >= c:
                out.add((c, w, d))
                out.add((w, c, d))
    return out


def a_events(p, k):
    run = subprocess.run([str(ROOT / "zlev"), str(p), str(k)], capture_output=True,
                         text=True, check=True, timeout=300)
    out = []
    for line in run.stdout.splitlines():
        tok = line.split()
        if tok[0] == "A":
            params = {key: int(v) for key, v in (s.split("=") for s in tok[2:])}
            out.append((int(tok[1]), params))
    return out


def r_audit():
    for p, k in [(3, 1), (11, 1), (17, 2), (19, 2), (23, 2), (409, 1), (577, 1), (5569, 1)]:
        n = p**(2 * k - 1)
        reps = star(n)
        events = {(v["C"], v["w"], v["d'"]) for _, v in a_events(p, k)
                  if v["k1"] == k - 1 and v["a'"] == 1}
        assert reps == events
        assert all(d * c % p and pow((1 - 4 * d * c) % p, (p - 1) // 2, p) == p - 1
                   for c, w, d in reps)
        print("Prop R", p, k, "ordered solutions", len(reps))
    for n in [9, 25, 49, 121, 225]:
        assert not star(n)
    for p, k in [(17, 3), (17, 4), (19, 3), (23, 3)]:
        parent = {r for r, _ in a_events(p, k - 1)}
        child = [(r, v) for r, v in a_events(p, k) if k - v["k1"] >= 3]
        assert all(r % p**(k - 1) in parent for r, _ in child)
        print("Dilation", p, k, "checked", len(child))


if __name__ == "__main__":
    mode = sys.argv[2] if len(sys.argv) > 2 else "s"
    {"s": s_audit, "t": t_audit, "r": r_audit}[mode]()
