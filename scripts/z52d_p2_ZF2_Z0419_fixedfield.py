"""Z0419: (*) certificates as SL2(Z) matrices M = [[d1, p], [4C, d2]], d1*d2 = 4Cp+1, d1 = d2 = -1 (mod 4C).
Trace t = d1+d2, trace field K_M = Q(sqrt(t^2-4)). McMullen-type uniformity lives in ONE fixed real quadratic field.
Test: for fixed K = Q(sqrt(D0)), which primes p = 1 (4) <= X have a (*) certificate with trace field K?
Traces with t^2-4 in D0*squares are t_k = tr(eta^k) (eta = least norm-1 unit with t^2-4 = D0 f^2), a geometric sequence.
For each such t: need 4C | t+2; d1 = -1 (mod 4C), d1 <= t/2, p = (d1(t-d1)-1)/(4C) prime.
Usage: uv run --with sympy python ... X"""
import sys, json, math
from sympy import isprime, primepi
from sympy.ntheory import factorint
def sqfree_ok(D):
    return all(e == 1 for e in factorint(D).values())
def fund_trace(D0):
    """least t>2 with t^2-4 = D0 f^2: from the fundamental solution of x^2 - D0 y^2 = +-1 or +-4 via CF of sqrt(D0)."""
    # enumerate convergents of sqrt(D0); t^2 - D0 f^2 = 4 has t = 2x (x^2-D0y^2=1) or primitive solutions with t,f odd
    best = None
    m, d, a0 = 0, 1, math.isqrt(D0); a = a0
    h1, h0, k1, k0 = 1, 0, 0, 1
    for _ in range(2000):
        h1, h0 = a * h1 + h0, h1; k1, k0 = a * k1 + k0, k1
        v = h1 * h1 - D0 * k1 * k1
        if v in (1, -1, 4, -4):
            # build norm-1 unit eta with trace t: u = (h1 + k1 sqrt D0)/g, g = 1 if |v|=1 else 2
            g = 1 if abs(v) == 1 else 2
            x, y, n = h1, k1, v // (g * g)
            # (x + y sqrtD)/g ; if norm -1 square it
            tr = 2 * x // g
            if n == -1:
                # trace of square = tr^2 - 2*norm = tr^2 + 2
                tr = tr * tr + 2
            if tr > 2 and (best is None or tr < best): best = tr
            if abs(v) == 1: break
        m = d * a - m; d = (D0 - m * m) // d; a = (a0 + m) // d
    assert best is not None and (best * best - 4) % D0 == 0 and math.isqrt((best*best-4)//D0)**2 == (best*best-4)//D0
    return best
def traces(D0, T):
    t1 = fund_trace(D0); a, b = 2, t1; out = []
    while b <= T:
        out.append(b); a, b = b, t1 * b - a
    return out
def divisors(n):
    ds = [1]
    for q, e in factorint(n).items():
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return ds
def certs_in_field(D0, X):
    ps = set(); ncert = 0
    for t in traces(D0, 4 * X + 8):
        if (t + 2) % 4: continue
        for C4 in [4 * c for c in divisors((t + 2) // 4)]:
            d1 = C4 - 1
            while 2 * d1 <= t:
                N = d1 * (t - d1) - 1
                p = N // C4
                if p > X: break
                if N % C4 == 0 and p % 4 == 1 and isprime(p):
                    ps.add(p); ncert += 1
                d1 += C4
    return ps, ncert
if __name__ == '__main__':
    X = int(sys.argv[1])
    Ds = [D for D in range(2, int(sys.argv[2]) if len(sys.argv) > 2 else 200) if sqfree_ok(D)]
    union = set(); res = []
    nprimes = sum(1 for p in range(5, X + 1, 4) if isprime(p)) if X <= 10**7 else None
    for D0 in Ds:
        ps, nc = certs_in_field(D0, X)
        union |= ps
        res.append({'D0': D0, 'fund_trace': fund_trace(D0), 'n_traces_le_4X': len(traces(D0, 4 * X + 8)),
                    'primes_with_cert': len(ps), 'certs': nc, 'largest_p': max(ps) if ps else None})
        print(json.dumps(res[-1])); sys.stdout.flush()
    print(json.dumps({'X': X, 'primes_1mod4_le_X': nprimes, 'union_over_D0_lt_200': len(union)}))
