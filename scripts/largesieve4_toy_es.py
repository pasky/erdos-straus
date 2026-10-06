"""EVIDENCE: sequential (always-forbid) law for actual ES R(M) classes, M = products of >=2 toy 'rough'
primes (M = 3 mod 4), on Z/(prod primes). Reports per support class S: max|sigma_hat|, P_S, and the
product prediction prod_{l in S} g_l with g_l = E p_l/(1-p_l) (first moment proxy)."""
import itertools, sys
import numpy as np
from math import gcd, prod

def divisors(n):
    ds, i = [], 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return ds

def R_classes(M):
    A = (M + 1) // 4
    out = set()
    for D in divisors(A * A):
        if gcd(D, M) == 1:
            out.add((-4 * D) % M)
    return out

def main(primes, include_single):
    primes = sorted(primes)
    classes = []  # (dict p->res)
    for k in range(1 if include_single else 2, len(primes) + 1):
        for Q in itertools.combinations(primes, k):
            M = prod(Q)
            if M % 4 != 3: continue
            for b in R_classes(M):
                classes.append({p: b % p for p in Q})
    n = len(primes)
    shape = tuple(primes)
    # sequential law via array over prefixes
    sig = np.ones(())
    pmass = []
    for i, l in enumerate(primes):
        tops = [C for C in classes if max(C) == l]
        prev = sig
        new = np.zeros(prev.shape + (l,))
        Epl = 0.0
        for idx in itertools.product(*[range(q) for q in primes[:i]]):
            pr = prev[idx] if i else float(prev)
            if pr == 0: continue
            asg = dict(zip(primes[:i], idx))
            F = {C[l] for C in tops if all(asg[q] == C[q] for q in C if q != l)}
            free = [a for a in range(l) if a not in F]
            Epl += pr * len(F) / l
            for a in free:
                new[idx + (a,)] = pr / len(free)
        sig = new
        pmass.append(Epl)
    F = np.fft.fftn(sig)
    A = np.abs(F)
    print("primes", primes, "#classes", len(classes), "E p_l", [round(x, 4) for x in pmass])
    g = {l: pm / (1 - pm) for l, pm in zip(primes, pmass)}
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            sl = tuple(slice(1, None) if i in S else slice(0, 1) for i in range(n))
            sub = A[sl]
            mx = sub.max(); PS = (sub ** 2).sum()
            pred = prod(g[primes[i]] for i in S)
            print(f"S={[primes[i] for i in S]}: max|hat|={mx:.3e}  P_S={PS:.3e}  prod g={pred:.3e}  max/prod(p)^(-1)... ratio P_S/prod g={PS/pred:.3f}")

if __name__ == "__main__":
    main([11, 19, 23, 31, 43], include_single=False)
