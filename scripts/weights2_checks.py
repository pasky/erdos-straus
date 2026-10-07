"""O90 checks (EVIDENCE / sanity for EXCEPTIONAL_WEIGHTS2.md).

1. every class of R(l) (l prime = 3 mod 4) is a quadratic non-residue (Prop 5.3 premise);
2. prime-slice mass S(Y) = sum_{l<=Y} |R(l)|/l versus (log Y)^2 (Prop 3.1);
3. self-overlap mass O_h(Y) = sum_l |F ∩ (F-h)|/l for small h (Prop 4.3 Assessment).
Usage: weights2_checks.py Ymax
"""
import sys, math


def spf_table(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def R(l, spf):
    A = (l + 1) // 4
    f = {p: 2 * e for p, e in factor(A, spf).items()}
    return {(-4 * D) % l for D in divisors_from(f)}


def main():
    Y = int(sys.argv[1])
    spf = spf_table(Y + 1)
    checkpoints = [10 ** k for k in range(2, 10) if 10 ** k <= Y]
    hs = list(range(1, 11))
    mass = 0.0
    over = {h: 0.0 for h in hs}
    nqr_fail = 0
    for l in range(3, Y + 1, 4):
        if spf[l] != l:
            continue
        F = R(l, spf)
        for a in F:
            if pow(a, (l - 1) // 2, l) != l - 1:
                nqr_fail += 1
        mass += len(F) / l
        for h in hs:
            over[h] += sum(1 for a in F if (a + h) % l in F) / l
        while checkpoints and l + 4 > checkpoints[0]:
            c = checkpoints.pop(0)
            lg = math.log(c)
            print(f"Y~{c:>9}  mass={mass:8.3f}  mass/(logY)^2={mass/lg**2:.4f}  "
                  + " ".join(f"O{h}={over[h]:.3f}" for h in (1, 2, 3, 6, 10)), flush=True)
    lg = math.log(Y)
    print(f"Y={Y:>9}  mass={mass:8.3f}  mass/(logY)^2={mass/lg**2:.4f}  "
          + " ".join(f"O{h}={over[h]:.3f}" for h in (1, 2, 3, 6, 10)))
    print("QNR failures:", nqr_fail)


if __name__ == "__main__":
    main()
