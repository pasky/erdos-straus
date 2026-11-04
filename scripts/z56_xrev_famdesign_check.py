"""Independent bounded audit of side-agent/z56-famdesign (export it to ROOT first).
Run: ulimit -v 6000000; ulimit -t 300; timeout 300s uv run --no-sync python \
  scripts/z56_xrev_famdesign_check.py /tmp/xrev_FAMDESIGN
Uses prebuilt ROOT/scan, ROOT/decide, and ROOT/slice; no third-party Python dependencies.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt, log, pi
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(sys.argv[1]).resolve()
DATA = ROOT / "data/z56/famdesign"


def run(argv, text="", seconds=120, check=True):
    return subprocess.run(argv, input=text, text=True, capture_output=True,
                          timeout=seconds, check=check)


@lru_cache(None)
def factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            exponent = 0
            while n % d == 0:
                n //= d
                exponent += 1
            result.append((d, exponent))
        d += 1
    if n > 1:
        result.append((n, 1))
    return tuple(result)


def phi(n):
    for q, _ in factors(n):
        n = n // q * (q - 1)
    return n


def squarefree(n):
    return all(exponent == 1 for _, exponent in factors(n))


def weight(p, o, e):
    ep, k = e, 0
    while ep % 2 == 0:
        ep //= 2
        k += 1
    if gcd(o, e) != 1 or (p + o + e) % 8:
        return F(0)
    for m, other in ((o, e), (ep, o)):
        if any(pow(-p * other, (q - 1) // 2, q) != 1 for q, _ in factors(m)):
            return F(0)
    return F(4 * 2 ** (len(factors(o)) + len(factors(ep))),
             2 ** k * phi(o) * phi(ep))


def direct_weights():
    checked = 0
    # Direct unit-square enumeration is independent of Legendre projectors.
    for o in range(1, 32, 2):
        for e in range(2, 34, 2):
            if gcd(o, e) != 1:
                continue
            q = 4 * o * e
            units = [x for x in range(q) if gcd(x, q) == 1]
            squares = {x * x % q for x in units}
            index = len(units) // len(squares)
            for p in (5, 13, 17, 29, 37, 41, 409, 577, 9, 25, 81, 289):
                direct = F(2 * index, len(units)) if -p * (o + e) % q in squares else F(0)
                assert direct == weight(p, o, e), (p, o, e)
                checked += 1
    print(f"Direct unit-square weights: {checked} exact rational comparisons, no mismatch")


def classify(n, o, e, c):
    ep, k = e, 0
    while ep % 2 == 0:
        ep //= 2
        k += 1
    s = squarefree(o) and squarefree(ep)
    u = s and o % 4 == 1 and k == 1
    p, q = sorted((o, e))
    g, lam = q ** 4 > p * n, p ** 15 > n
    w = e // 2
    f0 = u and o ** 12 > n and 8 * o ** 3 <= n and w ** 3 > n and 64 * w ** 3 <= n * n
    return (1, f0, u and e ** 4 > o * n and o ** 15 > n,
            u and g and lam, s and g and lam, u and g, s and g,
            g, g and lam, not g, 64 * c ** 3 <= n, c <= int(log(n) ** 2))


def brute(n):
    totals = [0] * 12
    p = 1
    # Independent pair enumeration, not the scanner's smallest-coordinate split.
    while 4 * p * p - 2 * p <= n:
        for q in range(p, (n + p) // (4 * p - 1) + 1):
            if (p + q) % 2 == 0 or (n + p + q) % (4 * p * q):
                continue
            o, e = (p, q) if p % 2 else (q, p)
            c = (n + p + q) // (4 * p * q)
            totals = [a + b for a, b in zip(totals, classify(n, o, e, c))]
        p += 1
    return totals


def rows(path):
    return [list(map(int, line.split())) for line in path.read_text().splitlines()
            if line and line[0].isdigit()]


def scan_checks():
    ns = list(range(5, 3001, 2))
    output = run([str(ROOT / "scan"), "-"], "\n".join(map(str, ns)) + "\n")
    got = [list(map(int, line.split())) for line in output.stdout.splitlines()]
    assert len(got) == len(ns)
    for row, n in zip(got, ns):
        assert row == [n, *brute(n)], (n, row, brute(n))
    print(f"Independent pair enumeration: all 12 columns agree at {len(ns)} odd n <= 3000")
    stored = rows(DATA / "zeros_le1e8.txt")
    scan = run([str(ROOT / "scan"), "5", "1000000"])
    got = [list(map(int, line.split())) for line in scan.stdout.splitlines()]
    selected = [row for row in got if any(row[j] == 0 for j in (1, 5, 7, 8, 9, 11, 12))]
    assert selected == [row for row in stored if row[0] <= 1000000]
    print(f"Prime scan <= 1e6: {len(got)} primes, {len(selected)} stored zero rows reproduced")
    decision = run([str(ROOT / "decide"), "1000", "1000000"])
    decision_rows = [list(map(int, line.split())) for line in decision.stdout.splitlines()]
    expected = [[r[0], r[1], r[12], r[11], r[8], r[9]] for r in got
                if r[0] >= 1000 and any(r[j] == 0 for j in (1, 12, 11, 8, 9))]
    assert decision_rows == expected
    print(f"Decision engine agrees with full scanner on [1000,1e6]: {len(expected)} zero rows")
    extra = rows(DATA / "decide_1e7_1e10.txt")
    f4 = sorted({row[0] for row in stored if row[8] == 0} |
                {row[0] for row in extra if row[4] == 0})
    f4l = sorted({row[0] for row in stored if row[9] == 0} |
                 {row[0] for row in extra if row[5] == 0})
    print(f"Stored unions: F4={len(f4)}, last={f4[-1]}; F4L={len(f4l)}, last={f4l[-1]}")
    out = run([str(ROOT / "scan"), "-"], "\n".join(map(str, f4)) + "\n")
    got = [list(map(int, line.split())) for line in out.stdout.splitlines()]
    assert [row[0] for row in got] == f4 and all(row[8] == 0 for row in got)
    assert all(row[1] == 1 and row[10] == 1 for row in got if row[0] > 10**7)
    print("All 38 reported F4 zeros rerun; all four above 1e7 have one solution, in K")


def slice_checks():
    stored = [line.split() for line in (DATA / "slicecheck.txt").read_text().splitlines()
              if line.startswith(("1 ", "2 "))]
    job = "\n".join(" ".join(row[:5]) for row in stored) + "\n"
    out = run([str(ROOT / "slice")], job, seconds=180)
    got = [line.split() for line in out.stdout.splitlines()]
    assert len(got) == len(stored) == 46
    for actual, expected in zip(got, stored):
        assert actual[:5] == expected[:5]
        assert abs(float(actual[5]) - float(expected[5])) <= 0.0000056
    ratios = [float(row[5]) / float(old[6]) for row, old in zip(got, stored)]
    print(f"46 slice sums rerun (stored L-value predictions not rerun): ratio range "
          f"{min(ratios):.6f}..{max(ratios):.6f}; within 3%: {sum(abs(x-1)<.03 for x in ratios)}")


def overflow_audit():
    # Only large-C solutions can overflow; n=(4C)oe-o-e >= (4C-2)oe.
    max128 = 2**127 - 1
    threshold = 1
    while 64 * threshold**3 <= max128:
        threshold *= 2
    lo, hi = threshold // 2, threshold
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if 64 * mid**3 <= max128:
            lo = mid
        else:
            hi = mid
    sample = rows(DATA / "sample_1e14.txt")
    triples = []
    for row in sample:
        n = row[0]
        product_bound = n // (4 * hi - 2)
        for o in range(1, product_bound + 1, 2):
            for e in range(2, product_bound // o + 1, 2):
                c, rem = divmod(n + o + e, 4 * o * e)
                if rem == 0 and c >= hi:
                    triples.append((n, o, e, c))
    # Invoke the actual source classifier, without its expensive full enumeration.
    source = ROOT / "scripts/z56_famdesign_scan.c"
    helper = ('#define main scanner_main\n#include "' + str(source) + '"\n#undef main\n'
              'int main(void) { sieve(300000); ll n,o,e,C; '
              'while(scanf("%lld %lld %lld %lld",&n,&o,&e,&C)==4) {'
              'long cnt[NF]={0}; cHC=hccut(n); classify(n,o,e,C,cnt); '
              'printf("%ld\\n",cnt[10]); } return 0; }\n')
    with tempfile.TemporaryDirectory(prefix="famdesign-overflow-") as td:
        src, exe = Path(td) / "check.c", Path(td) / "check"
        src.write_text(helper)
        run(["gcc", "-O2", str(src), "-lm", "-o", str(exe)], seconds=30)
        job = "\n".join(" ".join(map(str, t)) for t in triples) + "\n"
        out = run([str(exe)], job)
        accepted = list(map(int, out.stdout.split()))
        assert len(accepted) == len(triples)
        false = [t for t, a in zip(triples, accepted) if a]
        assert all(64 * c**3 > n for n, o, e, c in triples)
        bad_primes = {t[0] for t in false}
        old = sum(row[11] for row in sample)
        print(f"H3 OVERFLOW: first unsafe C={hi}; {len(triples)} overflowing sample solutions; "
              f"{len(false)} false memberships at {len(bad_primes)}/100 primes")
        corrected = {row[0]: row[11] for row in sample}
        for n, o, e, c in false:
            corrected[n] -= 1
        print(f"Sample H3 hits: stored={old}, corrected={old-len(false)}; "
              f"means={old/100:.2f} -> {(old-len(false))/100:.2f}; "
              f"corrected mean R/log^2={sum(2*h/log(n)**2 for n,h in corrected.items())/100:.8f}; "
              f"remaining zeros={sum(h == 0 for h in corrected.values())}")
        if false:
            print("First actual-classifier counterexample (p,o,e,C):", false[0])
            run(["gcc", "-O2", "-fsanitize=undefined", "-fno-sanitize-recover=undefined",
                 str(src), "-lm", "-o", str(exe)], seconds=30)
            out = run([str(exe)], " ".join(map(str, false[0])) + "\n", check=False)
            assert out.returncode != 0 and "signed integer overflow" in out.stderr
            print("UBSan confirms signed __int128 overflow")


def constants():
    lam = F(1, 15)
    area = F(5, 12) - F(3, 2)*lam + F(5, 4)*lam**2
    # Corner area by shoelace; R1 by the elementary antiderivative.
    vertices = [(F(0), F(0)), (F(1, 4), F(0)),
                (F(1, 3), F(1, 3)), (F(0), F(1, 4))]
    corner = sum(x*v-y*u for (x, y), (u, v) in
                 zip(vertices, vertices[1:]+vertices[:1])) / 2
    r1 = lambda x: F(3, 4)*x-F(5, 8)*x*x
    print(f"Exact areas: K={corner}, G={F(1,2)-corner}, G_1/15={area}, "
          f"R1_1/15={r1(F(3,5))-r1(lam)}")
    print(f"Theorem V constants: {3*float(area)/pi**2:.12f}, {5/(4*pi**2):.12f}; "
          f"square Euler product=12/pi^2={12/pi**2:.12f}")


constants()
direct_weights()
scan_checks()
slice_checks()
overflow_audit()
