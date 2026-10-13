"""R195: from-scratch checks of FF_MUTE Prop 2.1 / Cor 2.2 (shot identity, parity, integrality) and the sign
formulas of Lemma 3.2 and Lemma 4.1, by direct exponentiation (no reciprocity used), for
q in {2, 3, 4, 5, 7, 8, 9}. Usage: PYTHONPATH=scripts uv run python scripts/review_fm_signs.py"""
import random
import sys
from review_fm_ff import GF

random.seed(195)
QS = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else [2, 3, 4, 5, 7, 8, 9]
TR = int(sys.argv[2]) if len(sys.argv) > 2 else 300


def rand_monic(F, n):
    return tuple(random.randrange(F.q) for _ in range(n)) + (1,)


def rand_irred(F, n, avoid=()):
    while True:
        f = rand_monic(F, n)
        if F.is_irred(f) and f not in avoid:
            return f


def vval(F, a, s):
    v = 0
    while a:
        qt, r = F.pdivmod(a, s)
        if r:
            return v
        a, v = qt, v + 1
    return 10 ** 9


def divisors(F, N):
    fac = list(F.factor(N).items())
    out = [(1,)]
    for g, e in fac:
        new = []
        for d in out:
            x = d
            for i in range(e + 1):
                new.append(x)
                x = F.pmul(x, g)
        out = new
    return out


def eps_pow(F, e):
    # epsilon^e as field element, epsilon = (-1)^{(q-1)/2} (= 1 in char 2)
    x = F.chi_const(F.minus_one, 2) if F.q % 2 else 1
    return x if e % 2 else 1


def check_identity(F, trials):
    bad = cnt = integ = 0
    for _ in range(trials):
        k = random.randint(1, 3)
        A = rand_monic(F, k)
        h = random.randint(1, 2)
        s = rand_irred(F, h)
        if F.pmod(A, s) == ():
            continue
        n = random.randint(1, 5)
        P = rand_monic(F, n)  # composite allowed
        if len(F.pgcd(P, F.pmul(A, s))) > 1:
            continue
        Pprime = F.is_irred(P)
        j = random.randint(0, max(0, (10 - k) // (2 * h)))
        Q = F.ppow(s, j)
        AQ2 = F.pmul(A, F.pmul(Q, Q))
        if F.deg(AQ2) == n:
            continue
        N = F.padd(P, AQ2)
        for f in divisors(F, N):
            d = F.deg(f)
            if d < 1 or F.pmod(F.padd(f, (1,)), A) != ():
                continue
            if F.deg(AQ2) > n and not F.deg(AQ2) > n + d:
                continue
            E = F.pdivmod(N, f)[0]
            X, r1 = F.pdivmod(F.padd(P, E), A)
            fp1 = F.padd(f, (1,))
            Y, r2 = F.pdivmod(F.pmul(P, fp1), A)
            Nz, r3 = F.pdivmod(F.pmul(F.pmul(P, X), fp1), A)
            ok = r1 == r2 == r3 == () and X[-1] == Y[-1] == Nz[-1] == 1
            lhs = F.pmul(F.pmul(A, X), F.pmul(Y, Nz))
            Q2 = F.pmul(Q, Q)
            rhs = F.pmul(P, F.padd(F.padd(F.pmul(Y, Nz), F.pmul(X, Nz)), F.pmul(Q2, F.pmul(X, Y))))
            ok = ok and lhs == rhs
            vz = vval(F, Nz, s) - 2 * j if j else 0
            ok = ok and (vz >= 0 or vz % 2 == 0)
            nk = n - k
            ok = ok and F.deg(X) >= nk and F.deg(Y) >= nk and F.deg(Nz) - 2 * F.deg(Q) >= nk
            ok = ok and min(F.deg(X), F.deg(Y), F.deg(Nz) - 2 * F.deg(Q)) == nk
            # Cor 2.2: z in R iff f = -1 mod A*Q
            zint = vz >= 0
            corr = F.pmod(fp1, F.pmul(A, Q)) == ()
            ok = ok and (zint == corr)
            integ += zint and j > 0
            if Pprime:
                ok = ok and F.pmod(X, P) != () and F.pmod(Y, P) == () and F.pmod(Nz, P) == ()
            cnt += 1
            if not ok:
                bad += 1
                print("IDENTITY FAIL", F.q, A, s, P, j, f)
    return cnt, bad, integ


def check_signs(F, trials):
    q = F.q
    ells = [l for l in range(2, q) if (q - 1) % l == 0 and all(l % t for t in range(2, l))]
    cnt = bad = 0
    for _ in range(trials):
        k = random.randint(1, 3)
        A = rand_monic(F, k)
        n = random.randint(1, 4)
        P = rand_irred(F, n)
        h = random.randint(1, 3)
        s = rand_irred(F, h)
        d = random.randint(1, 6)
        # random f monic irreducible = -1 mod A of degree d (d >= k needed unless f = A - 1 type)
        f = None
        for _t in range(400):
            g = rand_monic(F, d)
            if F.pmod(F.padd(g, (1,)), A) == () and F.is_irred(g):
                f = g
                break
        if f is None or f in (P, s) or F.pmod(A, s) == () or P == s or F.pmod(A, P) == ():
            continue
        e = (q ** d - 1)
        if q % 2:
            # (ii): -P/A is a square mod f  <=>  (f/P) = tau
            invA = F.ppowmod(A, e - 1, f)
            w = F.pmod(F.pscale(F.minus_one, F.pmul(P, invA)), f)
            issq = F.ppowmod(w, e // 2, f) == (1,)
            tau = eps_pow(F, d * (1 + n + k) + k)
            fP = F.power_symbol_prime(f, P, 2)
            if issq != (fP == tau):
                bad += 1
                print("L3.2(ii) FAIL", q, A, P, f)
            # Lemma 4.1 for this f
            mA = F.pscale(F.minus_one, A)
            if F.power_symbol_prime(mA, f, 2) != eps_pow(F, d * (1 + k) + k):
                bad += 1
                print("L4.1 FAIL", q, A, f)
        for l in ells:
            isl = F.ppowmod(s, e // l, f) == (1,)
            eps_l = F.chi_const(F.minus_one, l) if q % 2 else 1  # (-1)^{(q-1)/l}
            sgn = 1
            for _ in range(d * h):
                sgn = F.mul[sgn][eps_l]
            if isl != (F.power_symbol_prime(f, s, l) == sgn):
                bad += 1
                print("L3.2 ell FAIL", q, l, s, f)
        cnt += 1
    return cnt, bad


def check_L41_composite(F, trials):
    """Lemma 4.1 for composite f (Jacobi symbol), q odd."""
    cnt = bad = 0
    for _ in range(trials):
        k = random.randint(1, 3)
        A = rand_monic(F, k)
        d = random.randint(1, 6)
        g = rand_monic(F, d)
        if F.pmod(F.padd(g, (1,)), A) != ():
            continue
        mA = F.pscale(F.minus_one, A)
        if F.jacobi(mA, g, 2) != eps_pow(F, d * (1 + k) + k):
            bad += 1
            print("L4.1 composite FAIL", F.q, A, g)
        cnt += 1
    return cnt, bad


if __name__ == "__main__":
    for q in QS:
        F = GF(q)
        c1, b1, ig = check_identity(F, TR)
        c2, b2 = check_signs(F, TR)
        c3, b3 = check_L41_composite(F, 2 * TR) if q % 2 else (0, 0)
        print(f"q={q}: Prop2.1/Cor2.2 shots {c1} bad {b1} (ES_q-integral with j>0: {ig}); "
              f"Lemma3.2 sign cases {c2} bad {b2}; Lemma4.1 composite f {c3} bad {b3}", flush=True)
