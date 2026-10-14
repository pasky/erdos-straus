"""R210: numerical anatomy of PHASE_DIAGRAM Thm 5.1's final bound (all in log space).

For log10 x = L, A given: S = first k odd primes (n = 1 here; n only removes O(1) primes), P = prod S <= (log x)^A
maximal, B = x^{1/(k+1)} / (3 log^{(A+5)/(k+1)} x), bound 2L_cov <= 2k * x / B^{k-1}.  Report k, the claimed main
term exponent 2/(k+1), the asymptotic proxy 2 log3 x/(A log2 x), and log(bound)/log(x) (must be < 1 to be
non-vacuous and -> 0).  Also checks the sieve-vs-exclusion sizes of Steps 1-3 in log space.
"""
from math import log, exp
from sympy import prime


def anatomy(L10, A):
    lx = L10 * log(10)
    l2 = log(lx)
    l3 = log(l2)
    cap = A * l2  # log of (log x)^A
    k, lP, i = 0, 0.0, 2
    while True:
        p = prime(i)
        if lP + log(p) > cap:
            break
        lP += log(p)
        k += 1
        i += 1
    if k < 4:
        return f"L10={L10} A={A}: k={k} < 4, theorem not yet active"
    lB = lx / (k + 1) - log(3) - (A + 5) / (k + 1) * l2
    if lB < 0:
        return f"L10={L10} A={A}: B < 1"
    lbound = log(2 * k) + lx - (k - 1) * lB
    sieve = lx - (A + 3) * l2            # log of x / log^{A+3} x
    step3 = (k + 1) * (log(3) + lB) + log(lP)
    step2 = k * log(6) + (1 + 1 / k) * (0.75 + 0.01) * lx + log(2 * lP)
    return (f"L10={L10:.0e} A={A}: k={k}, 2/(k+1)={2/(k+1):.4f}, proxy 2log3/(A log2)={2*l3/(A*l2):.4f}, "
            f"log e/log x <= {lbound/lx:.4f}; sieve {sieve:.4g} vs excl2 {step2:.4g}, excl3 {step3:.4g}")


if __name__ == "__main__":
    for A in (1, 2, 10):
        for L10 in (1e2, 1e4, 1e8, 1e16, 1e32, 1e64):
            print(anatomy(L10, A))
