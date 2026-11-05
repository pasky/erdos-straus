"""z59 CONV2 validation.
(1) Independent brute force of the zero sets of the c = 1 line ((★)), the a = 1 (∪ b = 1) line and their union,
    numerator K, for odd n <= N, by direct enumeration of solutions (no target sets, no witnesses).
(2) Compare with the engine scripts/z59_conv2_lines.c (run with FMAX = K-1, i.e. every n through the exact path,
    and with a normal FMAX).
(3) Verify every LATE line in the given data files: K abcd = a + b + n c, line membership, f = K acd - 1.
Usage: python3 z59_conv2_check.py N K engine_binary [datafiles...]
"""
import sys, subprocess, math

def brute(N, K):
    star = bytearray(N + 1); a1 = bytearray(N + 1)
    # c = 1 line: K a b d = a + b + n  -> n = K a b d - a - b, a <= b (symmetric)
    a = 1
    while K * a * a - 2 * a <= N:
        d = 1
        while K * a * a * d - 2 * a <= N:
            b = a
            while True:
                n = K * a * b * d - a - b
                if n > N: break
                if n >= 1: star[n] = 1
                b += 1
            d += 1
        a += 1
    # a = 1 line: K b c d = 1 + b + n c  -> n = (K b c d - 1 - b)/c, need c | b + 1
    c = 1
    while True:
        if K * c * 1 * 1 - 1 > N * c + 2 and c > N + 2: break
        # b ≡ -1 mod c, b >= 1
        any_c = False
        d = 1
        while True:
            # smallest b >= 1 with c | b+1
            b = c - 1 if c > 1 else 1
            if b < 1: b += c
            n0 = (K * b * c * d - 1 - b) // c
            if n0 > N: break
            any_c = True
            while True:
                num = K * b * c * d - 1 - b
                n = num // c
                if n > N: break
                if num % c == 0 and n >= 1: a1[n] = 1
                b += c
            d += 1
        if not any_c: break
        c += 1
    return star, a1

def issq(n):
    r = math.isqrt(n); return r * r == n

def main():
    N = int(sys.argv[1]); K = int(sys.argv[2]); eng = sys.argv[3]
    star, a1 = brute(N, K)
    for lines, name in ((1, "c=1"), (2, "a=1"), (3, "union")):
        bz = [n for n in range(1, N + 1, 2) if n % 4 == 1 and not issq(n)
              and not ((lines & 1 and star[n]) or (lines & 2 and a1[n]))]
        for fmax in (K - 1, 2000):
            out = subprocess.run([eng, str(K), str(lines), "1", str(N + 1), str(fmax), "0", "1"],
                                 capture_output=True, text=True, check=True).stdout
            ez = [int(l.split()[1]) for l in out.splitlines() if l.startswith("ZERO")]
            print(f"K={K} {name} N={N} FMAX={fmax}: brute zeros {len(bz)}, engine zeros {len(ez)}, identical={bz == ez}")
            if bz != ez:
                print("  MISMATCH", sorted(set(bz) ^ set(ez))[:20]); sys.exit(1)
        if lines == 3: print("  union zeros:", bz)
    nbad = nlate = 0
    for fn in sys.argv[4:]:
        Kf = None
        for l in open(fn):
            if l.startswith("# K="): Kf = int(l.split()[1][2:]); L = int(l.split()[2][6:])
        for l in open(fn):
            if not l.startswith("LATE"): continue
            p = l.split(); n = int(p[1]); f, a, b, c, d = (int(x.split("=")[1]) for x in p[3:8])
            ok = Kf * a * b * c * d == a + b + n * c and f == Kf * a * c * d - 1
            onl = (L & 8) or ((L & 1) and c == 1) or ((L & 2) and (a == 1 or b == 1)) or ((L & 4) and d == 1)
            nlate += 1
            if not (ok and onl): nbad += 1; print("BAD", fn, l.strip())
    print(f"LATE witnesses checked: {nlate}, bad: {nbad}")
    if nbad: sys.exit(1)

main()
