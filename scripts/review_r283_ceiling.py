"""R283 from-scratch checks of O272 Thm 3.1 densities, Prop 4.1 (b)/(b')/(c), Lemma 5.1, Cor 6.1 (+ conductor example).
All by direct modular arithmetic (pow), no reuse of z41_* scripts.
"""
from collections import Counter, defaultdict
from sympy import primerange, divisors, isprime


def in_pow(x, e, q):
    """x in F_q^{x e}  (e | q - 1 not required: uses gcd)"""
    from math import gcd
    g = gcd(e, q - 1)
    return pow(x % q, (q - 1) // g, q) == 1


def odd_part_member(x, q):
    o = q - 1
    while o % 2 == 0:
        o //= 2
    return pow(x % q, o, q) == 1


QMAX = 400000
PR = list(primerange(3, QMAX))

print("== Thm 3.1 densities (per forcing class c = q mod l; fraction of l in F_q^{x e} among q = 1 (m)) ==")
for (l, m, M4) in [(7, 3, False), (13, 3, False), (7, 6, True), (11, 4, False), (7, 8, False), (5, 12, True)]:
    # classes q mod lcm(l, 4 if M4) ; stats per class
    mod = l * (4 if M4 else 1)
    st = defaultdict(Counter)
    for q in PR:
        if q % m != 1 or q == l:
            continue
        c = q % mod
        leg = 1 if pow(l, (q - 1) // 2, q) == 1 else -1
        st[c]["n"] += 1
        st[c]["leg+"] += (leg == 1)
        for e in [d for d in range(2, m + 1) if m % d == 0]:
            st[c][e] += in_pow(l, e, q)
    line = []
    for c in sorted(st)[:4]:
        C = st[c]
        legs = "fixed" if C["leg+"] in (0, C["n"]) else f"FREE({C['leg+']}/{C['n']})"
        fr = " ".join(f"e{e}:{C[e]/C['n']:.3f}" for e in sorted(k for k in C if isinstance(k, int)))
        line.append(f"c={c}: n={C['n']} (l/q) {legs} {fr}")
    print(f"l={l} m={m} mod={mod}:\n   " + "\n   ".join(line))

print("== Prop 4.1 ==")
for (n, l) in [(13, 7), (7, 11), (101, 7), (131, 11), (241, 7), (21, 19)]:
    assert l % 4 == 3 and pow(n, (l - 1) // 2, l) == l - 1
    forced = [q for q in PR if (4 * q * n + 1) % l == 0]
    sq = sum(in_pow(-l, 2, q) for q in forced)
    res = [f"m=2: {sq}/{len(forced)}"]
    for m in (4, 8, 16):
        Q = [q for q in forced if q % m == 1]
        res.append(f"m={m}: {sum(in_pow(-l, m, q) for q in Q)}/{len(Q)}")
    # (b') and (c): v2(q-1) = j exactly, -l in odd-order subgroup
    for j in (1, 2, 3, 4):
        Q = [q for q in forced if (q - 1) % (1 << j) == 0 and (q - 1) % (1 << (j + 1)) != 0]
        res.append(f"j={j}: {sum(odd_part_member(-l, q) for q in Q)}/{len(Q)}")
    print(f"(n,l)=({n},{l}): " + "; ".join(res))

print("== Lemma 5.1: n = D m^2, 4D | t  =>  no divisor d = -1 (t) of tn+1 ==")
viol = tests = 0
for D in (3, 5, 7, 9, 15, 17, 21, 45, 255):
    for mm in range(1, 40, 2):
        n = D * mm * mm
        for k in range(1, 25):
            t = 4 * D * k
            N = t * n + 1
            tests += 1
            if any(d % t == t - 1 for d in divisors(N)):
                viol += 1
print(f"tests {tests}, violations {viol}")
# control: odd D with 4D NOT dividing t (t = 4k, D does not divide k) typically has words
ctrl = sum(1 for D in (3, 5, 7) for mm in (1, 3, 5) for k in (1, 2, 4) if k % D
           and any(d % (4 * k) == 4 * k - 1 for d in divisors(4 * k * D * mm * mm + 1)))
print(f"control (4D does not divide t): {ctrl} of 27 (D, m, t) have a divisor = -1 (t)")

print("== Cor 6.1: cubes n = r^3, l = 1 (3), t = 4 q w, forced q = 1 (3): fraction l a cube mod q ==")
for w in (1, 2):
    for (r, l) in [(3, 7), (7, 13), (9, 19), (5, 7), (11, 31)]:
        n = r ** 3
        Q = [q for q in PR if q % 3 == 1 and q != l and (4 * w * q * n + 1) % l == 0]
        print(f"w={w} n={n} l={l}: cubes {sum(in_pow(l, 3, q) for q in Q)}/{len(Q)}")

print("== conductor example: alpha = 1 + 28w, N = 757 ==")
print("757 prime:", isprime(757), "27^2+27+1 =", 27 * 27 + 28, " 7^252 mod 757 =", pow(7, 252, 757))
