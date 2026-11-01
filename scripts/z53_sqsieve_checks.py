"""z53 SQSIEVE basic checks.
(a) Lemma W: for odd primes q, all c, l mod q, n mod q:
    G_c(l) := sum_{k mod q} ((f(c,k))/q) e(l k/q),  f = (4ck-n)^2-4k,
    |G| <= 2 sqrt(q) unless q|l (then G = K_q(c) in {0,-1,q-1}); and sum_c |G_c(l)| <= 2 q^{3/2}.
(c) BM in strip coordinates: every (*) triple (u,B,C), 4uBC-u-B=n, n odd, gcd(uBC,n)=1, has jacobi(-uB, n) = -1.
Usage: python z53_sqsieve_checks.py QMAX NMAX
"""
import sys, cmath, math
from sympy import primerange, jacobi_symbol

def leg(a, q):
    a %= q
    if a == 0: return 0
    return 1 if pow(a, (q-1)//2, q) == 1 else -1

def check_weil(QMAX):
    worst = 0.0; cases = 0
    for q in primerange(3, QMAX+1):
        tw = [cmath.exp(2j*math.pi*t/q) for t in range(q)]
        for n in range(q):
            for l in range(q):
                tot = 0.0
                for c in range(q):
                    vals = [leg((4*c*k-n)**2-4*k, q) for k in range(q)]
                    G = sum(vals[k]*tw[(l*k) % q] for k in range(q))
                    cases += 1
                    if l % q == 0:
                        K = round(G.real)
                        assert abs(G - K) < 1e-6 and K in (0, -1, q-1), (q, n, c, l, G)
                        if K == q-1: assert (4*c*n+1) % q == 0 and c % q != 0
                    else:
                        r = abs(G)/math.sqrt(q)
                        worst = max(worst, r)
                        assert r <= 2+1e-9, (q, n, c, l, G)
                    tot += abs(G)
                assert tot <= 2*q**1.5 + 1e-6, (q, n, l, tot)
    return cases, worst

def G(c, l, n, Q, tw):
    from sympy import jacobi_symbol
    return sum(int(jacobi_symbol(((4*c*k-n)**2-4*k) % Q, Q))*tw[(l*k) % Q] for k in range(Q))

def check_crt_kloosterman():
    """Lemma W(d): G^(Q)_c(l) = G^(q)_c(l*inv(q',q)) G^(q')_c(l*inv(q,q')); and Lemma W(b) Kloosterman identity
    H(d,l) = sum_x ((x^2-d)/q) e(lx/q) = S(-d, -inv(4)l^2; q) for q not dividing d*l."""
    cases = 0; err = 0.0
    for (q, qq) in [(3, 5), (5, 7), (3, 11), (7, 11)]:
        Q = q*qq
        twQ = [cmath.exp(2j*math.pi*t/Q) for t in range(Q)]
        twq = [cmath.exp(2j*math.pi*t/q) for t in range(q)]
        twqq = [cmath.exp(2j*math.pi*t/qq) for t in range(qq)]
        for n in range(0, Q, 2):
            for c in range(Q):
                for l in range(Q):
                    a = G(c, l, n, Q, twQ)
                    b = G(c % q, (l*pow(qq, -1, q)) % q, n, q, twq)*G(c % qq, (l*pow(q, -1, qq)) % qq, n, qq, twqq)
                    err = max(err, abs(a-b)); cases += 1
    kerr = 0.0; kcases = 0
    for q in primerange(3, 18):
        tw = [cmath.exp(2j*math.pi*t/q) for t in range(q)]
        i4 = pow(4, -1, q)
        for d in range(1, q):
            for l in range(1, q):
                H = sum(leg(x*x-d, q)*tw[(l*x) % q] for x in range(q))
                S = sum(tw[(-d*t - i4*l*l*pow(t, -1, q)) % q] for t in range(1, q))
                kerr = max(kerr, abs(H-S)); kcases += 1
    return cases, err, kcases, kerr

def check_bm(NMAX):
    # enumerate all (*) triples with 4uBC-u-B <= NMAX
    bad = 0; tested = 0; zero_sq = 0
    for C in range(1, NMAX):
        if 4*C - 2 > NMAX: break
        for u in range(1, NMAX):
            if 4*u*C - u - u > NMAX and 4*u*C*1 - u - 1 > NMAX: break
            for B in range(1, NMAX):
                n = 4*u*B*C - u - B
                if n > NMAX: break
                if n < 3 or n % 2 == 0: continue
                if math.gcd(u*B*C, n) != 1: continue
                tested += 1
                if jacobi_symbol((-u*B) % n, n) != -1: bad += 1
                r = math.isqrt(n)
                if r*r == n: zero_sq += 1
    return tested, bad, zero_sq

if __name__ == "__main__":
    QMAX = int(sys.argv[1]); NMAX = int(sys.argv[2])
    cases, worst = check_weil(QMAX)
    print(f"Lemma W: {cases} (q,n,c,l) cases, odd primes q<={QMAX}: all pass; max |G|/sqrt(q) over q∤l = {worst:.4f} (bound 2)")
    c1, e1, c2, e2 = check_crt_kloosterman()
    print(f"Lemma W(d) CRT factorisation: {c1} cases (Q in 15,35,33,77; n even residues), max error {e1:.1e}; Kloosterman identity: {c2} cases (q<=17), max error {e2:.1e}")
    tested, bad, zsq = check_bm(NMAX)
    print(f"BM-in-strip: {tested} coprime (*) triples with odd n<={NMAX}: violations of (-uB/n)=-1: {bad}; triples at odd squares: {zsq}")
