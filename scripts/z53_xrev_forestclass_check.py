"""Independent bounded-memory checks of Z53_FORESTCLASS.
Usage: uv run --with sympy python scripts/z53_xrev_forestclass_check.py /tmp/xrev_FORESTCLASS
The directory contains an archive of the reviewed branch and its compiled `forest` engine.
Run under an external timeout and ulimit. No dense vertex arrays or Cartesian products.
"""
import ast
from collections import defaultdict, deque
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path
import re
import subprocess
import sys

from sympy import divisors, factorint, primerange, sqrt_mod

BASE = Path(sys.argv[1])
DATA = BASE / "data/z53/forestclass"
NAMES = ("ALL", "SM", "SP", "NR", "SMN", "SQ")


def color(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


@lru_cache(maxsize=4096)
def prove_prime(n):
    """Complete-factorization Lucas criterion; recursively prove every factor."""
    if n == 2:
        return True
    assert n > 2 and n % 2
    factors = {int(q): int(e) for q, e in factorint(n - 1).items()}
    assert prod(q ** e for q, e in factors.items()) == n - 1
    for q in factors:
        assert prove_prime(q)
    for a in range(2, 10000):
        if pow(a, n - 1, n) == 1 and all(
            gcd(pow(a, (n - 1) // q, n) - 1, n) == 1 for q in factors
        ):
            return True
    raise AssertionError(("no Lucas witness", n))


def neighbors(p, u):
    # Large vertices have at most the unique smaller neighbor; avoid factoring p+u.
    if u * (u - 1) > p + 1:
        v = (-p) % u
        return [v] if v and (p + u + v) % (u * v) == 0 else []
    return [int(v) for v in divisors(p + u)
            if v != u and (p + u + v) % (u * v) == 0]


def forest_stats(p):
    # Sparse whole graph, edges tested by the original definition, not cofactor residues.
    adj = defaultdict(list)
    bi = []
    edges = 0
    for u in range(1, isqrt(p) + 2):
        for v in neighbors(p, u):
            if v <= u:
                continue
            adj[u].append(v)
            adj[v].append(u)
            edges += 1
            if color(u, p) != color(v, p):
                bi.extend((u, v))
    depth = dict.fromkeys(bi, 1)
    queue = deque(depth)
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in depth:
                depth[v] = depth[u] + 1
                queue.append(v)
    stats = {name: [0] * 6 for name in NAMES}
    for a in range(1, isqrt(p) + 2):
        # General modular-square-root routine, independent of engine's local tests.
        sm = sqrt_mod(-p, a) is not None
        sp = sqrt_mod(p, a) is not None
        nr = color(a, p) == -1
        for name, include in zip(NAMES, (True, sm, sp, nr, sm and nr, isqrt(a) ** 2 == a)):
            if not include:
                continue
            s = stats[name]
            s[0] += 1
            if a in depth:
                s[1] += 1
                s[2] += depth[a] <= 1
                s[3] += depth[a] <= 2
                if not s[4]:
                    s[4:] = a, s[0]
    return stats, edges, len(bi) // 2


def check_failures():
    smn_failures = []
    square_failures = []
    for file in ("census_1e7_summary.txt", "census_1e7_1e8_summary.txt"):
        text = (DATA / file).read_text().split("## class 5mod8")[0]
        smn_failures += ast.literal_eval(re.search(r"SMN:.*?full-fail list.*?: (\[.*?\])", text, re.S)[1])
        square_failures += ast.literal_eval(re.search(r"SQ:.*?full-fail list.*?: (\[.*?\])", text, re.S)[1])
    assert len(smn_failures) == 48 and len(square_failures) == 668
    targets = sorted(set(smn_failures + [17, 41, 269, 19441, 4149601, 78168721,
                                       19231801, 41751889, 23544721, 81326281]))
    output = subprocess.run([str(BASE / "forest")], input="\n".join(map(str, targets)),
                            text=True, capture_output=True, check=True, timeout=120).stdout.splitlines()
    assert len(output) == len(targets)
    for p, line in zip(targets, output):
        assert prove_prime(p)
        stats, edges, bi = forest_stats(p)
        assert int(re.search(r"edges=(\d+)", line)[1]) == edges
        assert int(re.search(r" bi=(\d+)", line)[1]) == bi
        for name in NAMES:
            record = re.search(rf" {name}=(\d+)/(\d+)/(\d+)/(\d+) f=(\d+)@(\d+)", line)
            assert list(map(int, record.groups())) == stats[name], (p, name, stats[name], record.groups())
        assert stats["SP"][1] > 0
        assert (stats["SM"][1] == 0) == (p == 19441)
        assert (stats["SMN"][1] == 0) == (p in smn_failures)
        print(f"FOREST p={p} edges={edges} bi={bi} all six sets agree", flush=True)
    # Re-run every recorded square failure (same engine, separately labelled).
    output = subprocess.run([str(BASE / "forest")], input="\n".join(map(str, square_failures)),
                            text=True, capture_output=True, check=True, timeout=120).stdout.splitlines()
    assert len(output) == 668
    assert all(int(re.search(r" SQ=\d+/(\d+)/", line)[1]) == 0 for line in output)
    print(f"Independent forest checks: {len(targets)}; SMN failures: 48; engine SQ failure reruns: 668", flush=True)


def check_instances():
    count = 0
    for line in (DATA / "thm1_instances.txt").read_text().splitlines():
        if line.startswith("# H="):
            H, K, q, c = map(int, re.search(r"H=(\d+) K=(\d+) q=(\d+) c=(\d+)", line).groups())
        elif line.startswith("INSTANCE"):
            p = int(re.search(r"p=(\d+)", line)[1])
            assert prove_prime(p)
            nr = [a for a in range(1, K * q + 1) if color(a, p) == -1]
            assert nr == [q * j for j in range(1, K + 1)]
            menu = list(range(1, H + 1)) + nr
            seen = set()
            for root in menu:
                queue = deque([root])
                while queue:
                    u = queue.popleft()
                    if u in seen:
                        continue
                    seen.add(u)
                    assert len(seen) < 100000
                    for v in neighbors(p, u):
                        assert color(u, p) == color(v, p), (p, u, v)
                        if v not in seen:
                            queue.append(v)
            if "all_prime=True" in line:
                for x in menu:
                    assert (p + x) % (1 + x) == 0
                    assert prove_prime((p + x) // (1 + x))
            count += 1
            print(f"INSTANCE p={p} Lucas-proved; menu mono; explored {len(seen)} vertices", flush=True)
    assert count == 16


def check_genus_and_forms():
    pairs = square_edges = forms = 0
    for p in primerange(5, 500):
        if p % 4 != 1:
            continue
        for a in range(3, isqrt(p) + 2):
            units = [x for x in range(a) if gcd(x, a) == 1]
            squares = {x * x % a for x in units}
            c = (-p) % a
            target = {c * x % a for x in squares}
            divs = divisors(p + a)
            count = sum(d % a in target for d in divs)
            span = set(squares)
            for ell in factorint(p + a):
                span |= {x * int(ell) % a for x in tuple(span)}
            assert (count > 0) == (c in span)
            if c in squares:
                assert count * (len(units) // len(squares)) >= len(divs)
            if count == 0:
                assert not neighbors(p, a)
            pairs += 1
        for b in range(1, isqrt(p + 2) + 1):
            Cset = set(neighbors(p, b * b))
            predicted = set()
            for A in divisors(p + b * b):
                C = (p + b * b) // A
                if C != b * b and (A + 1) % (b * b) == 0:
                    predicted.add(C)
                    assert color(A, p) == color(C, p)
                    odd = A if A % 2 else C
                    assert (color(C, p) == -1) == (odd % 4 == 3)
                    if b % 2 == 0:
                        assert color(C, p) == -1
                    square_edges += 1
            assert Cset == predicted
        minima = set()
        for a in range(1, isqrt(4 * p // 3) + 1):
            for b in range((-a + 1) // 2, a // 2 + 1):
                if (p + b * b) % a:
                    continue
                c = (p + b * b) // a
                if c < a or (c == a and b < 0):
                    continue
                minima.add(a)
                assert gcd(gcd(a, 2 * b), c) == 1
                if a > 1 and b and b * b < a:
                    assert (b * b in neighbors(p, a)) == ((c + 1) % (b * b) == 0)
                forms += 1
        for a in range(1, isqrt(p) + 1):
            assert (a in minima) == (sqrt_mod(-p, a) is not None)
    print(f"Lemma G brute cases={pairs}; square/form edge cases={square_edges}; reduced forms={forms}")


check_genus_and_forms()
check_instances()
check_failures()
print("ALL CHECKS PASS")
