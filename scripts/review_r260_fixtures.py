"""R260 independent fixture extraction from Astra markdown (read-only) and classification.

Scans every ../erdos-straus-astra/*.md for integer triples "(a,b,c)" (a,b,c >= 1), computes
N = 4/(1/a+1/b+1/c); keeps triples with N integral, N = p*n^2 for a prime p = 1 (4) (n >= 1).
For n = 1 (ES points of p) classifies: Type I level e (one coordinate p*H, H=(pe+1)/4) or Type II window
w = 4x - p (x the p-free coordinate, the other two divisible by p).  Compares with the author's list.
Usage: review_r260_fixtures.py ASTRA_DIR AUTHOR_TRANSLATED_FILE
"""
import sys, re, glob, os
from fractions import Fraction as F
from math import isqrt, gcd
from sympy import isprime, factorint

TRI = re.compile(r"\((\d+)\s*,\s*(\d+)\s*,\s*(\d+)\)")


def classify(N):
    """N = p n^2 with p prime = 1 mod 4: return list of (p, n)."""
    out = []
    for n in range(1, isqrt(N) + 1):
        if N % (n * n) == 0:
            p = N // (n * n)
            if p > 3 and p % 4 == 1 and isprime(p):
                out.append((p, n))
    return out


def main():
    adir, auth = sys.argv[1], sys.argv[2]
    found = {}
    for f in sorted(glob.glob(os.path.join(adir, "*.md"))):
        txt = open(f, encoding="utf-8", errors="replace").read()
        for mt in TRI.finditer(txt):
            t = tuple(int(v) for v in mt.groups())
            if min(t) < 1:
                continue
            s = sum(F(1, v) for v in t)
            N = F(4) / s
            if N.denominator != 1:
                continue
            for (p, n) in classify(int(N)):
                found.setdefault((p, n, tuple(sorted(t))), set()).add(os.path.basename(f))
    es = [(k, v) for k, v in found.items() if k[1] == 1]
    tw = [(k, v) for k, v in found.items() if k[1] > 1]
    print(f"independently extracted exact triples: {len(found)} ({len(es)} twist-1 ES points, {len(tw)} twisted)")
    levels, windows = {}, {}
    for (p, n, t), files in sorted(es):
        pd = [v for v in t if v % p == 0]
        if len(pd) == 1:
            H = pd[0] // p
            e = F(4 * H - 1, p)
            assert e.denominator == 1 and e % 4 == 3
            levels.setdefault(int(e), []).append((p, t))
            kind = f"TypeI e={int(e)}"
        elif len(pd) == 2:
            x = [v for v in t if v % p][0]
            w = 4 * x - p
            windows.setdefault(w, []).append((p, t))
            kind = f"TypeII w={w}"
        else:
            kind = "??"
        print(f"  p={p} {t} {kind}  [{','.join(sorted(files))}]")
    print("Type I levels:", {e: len(v) for e, v in sorted(levels.items())})
    print("Type II windows:", {w: len(v) for w, v in sorted(windows.items())})
    for (p, n, t), files in sorted(tw):
        print(f"  twisted p={p} n={n} {t} [{','.join(sorted(files))}]")
    # compare with author's translated file
    A = set()
    for line in open(auth):
        m = re.search(r"p=(\d+) N=p\*(\d+)\^2 triple=\((\d+), (\d+), (\d+)\) exact=True", line)
        if m:
            p, n, a, b, c = map(int, m.groups())
            A.add((p, n, tuple(sorted((a, b, c)))))
    mine = set(found)
    print(f"author exact distinct: {len(A)}; mine: {len(mine)}; author-only: {sorted(A - mine)}")
    print(f"mine-only ({len(mine - A)}):", sorted(mine - A))
    scope = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else set()
    if scope:
        miss = [(k, sorted(found[k] & scope)) for k in sorted(mine - A) if found[k] & scope]
        print(f"mine-only inside the author's {len(scope)} files ({len(miss)}):")
        for k, f in miss:
            print("   ", k, f)


if __name__ == "__main__":
    main()
