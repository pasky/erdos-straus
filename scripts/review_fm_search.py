"""R195: from-scratch mute-shot search for FF_MUTE (Prop 2.1 / Thm 3.5 / Thm 4.2), any prime power q.
For monic P coprime to sA: search j = 0..J and monic f = -1 (mod A), 1 <= deg f <= dmax, f | P + A s^{2j},
in either degree regime (deg AQ^2 > n + d, or deg AQ^2 < n), build (X, Y, z) of Prop 2.1 and verify exactly:
A X Y Nz = P (Y Nz + X Nz + Q^2 X Y), z = Nz/Q^2, X, Y, Nz monic, v_s(z) even if negative, NC with min = n - k.
Modes:
  irr  q A s nmin nmax J dmax           -- all irreducible P (P != s, P not | A), report unsolved
  list q A s file J dmax                -- P from a file of coefficient strings (high degree first, base-q digits)
  t1   q A s nmax J dmax                -- all monic P coprime to sA: squares vs non-squares (Thm 4.2);
                                           for squares, exhaustive over (j, f) and record the set of deg f that fire
Polynomials on the command line: comma-separated coefficients, LOW degree first (e.g. T^2+1 = 1,0,1)."""
import sys
import itertools
from review_fm_ff import GF


def parse(s):
    return tuple(int(c) for c in s.split(','))


class Searcher:
    def __init__(self, F, A, s, J, dmax):
        self.F, self.A, self.s, self.J, self.dmax = F, A, s, J, dmax
        self.k = len(A) - 1
        mone = F.minus_one
        self.fs = []
        for d in range(1, dmax + 1):
            for f in F.monics(d):
                fp1 = F.padd(f, (1,))
                if F.pmod(fp1, A) == ():
                    self.fs.append(f)
        self.Q2A = []
        Q = (1,)
        for j in range(J + 1):
            self.Q2A.append((Q, F.pmul(A, F.pmul(Q, Q))))
            Q = F.pmul(Q, s)

    def vval(self, a, s):
        F = self.F
        v = 0
        while True:
            qt, r = F.pdivmod(a, s)
            if r:
                return v
            a, v = qt, v + 1

    def verify(self, P, j, f, Q=None):
        F, A, s, k = self.F, self.A, self.s, self.k
        n = len(P) - 1
        if Q is None:
            Q, AQ2 = self.Q2A[j]
        else:
            AQ2 = F.pmul(A, F.pmul(Q, Q))
        d = len(f) - 1
        N = F.padd(P, AQ2)
        E, r0 = F.pdivmod(N, f)
        X, r1 = F.pdivmod(F.padd(P, E), A)
        fp1 = F.padd(f, (1,))
        Y, r2 = F.pdivmod(F.pmul(P, fp1), A)
        Nz, r3 = F.pdivmod(F.pmul(F.pmul(P, X), fp1), A)
        if not (r0 == r1 == r2 == r3 == ()):
            return False
        if not (X[-1] == Y[-1] == Nz[-1] == 1):
            return False
        Q2 = F.pmul(Q, Q)
        lhs = F.pmul(F.pmul(A, X), F.pmul(Y, Nz))
        rhs = F.pmul(P, F.padd(F.padd(F.pmul(Y, Nz), F.pmul(X, Nz)), F.pmul(Q2, F.pmul(X, Y))))
        if lhs != rhs:
            return False
        if j:
            vz = self.vval(Nz, s) - 2 * j
            if vz < 0 and vz % 2:
                return False
        degs = (len(X) - 1, len(Y) - 1, len(Nz) - 1 - 2 * (len(Q) - 1))
        return min(degs) == n - k

    def candidates(self, P):
        """yield (j, f) with f | P + A Q^2, f = -1 mod A, degree regime OK"""
        F = self.F
        n = len(P) - 1
        for j in range(self.J + 1):
            Q, AQ2 = self.Q2A[j]
            m = len(AQ2) - 1
            if m == n:
                continue
            N = F.padd(P, AQ2)
            for f in self.fs:
                d = len(f) - 1
                if m > n and m <= n + d:
                    continue
                if m < n and d > n:
                    continue
                if F.pmod(N, f) == ():
                    yield j, f

    def solve(self, P):
        for j, f in self.candidates(P):
            if self.verify(P, j, f):
                return j, f
            raise AssertionError(("verification failed", P, j, f))
        return self.solve_dlog(P)

    # ---- Lemma 3.1 route: prime f, j found by discrete log of -P/A in <s^2 mod f>, unbounded j ----
    def _tables(self):
        if hasattr(self, "_tab"):
            return self._tab
        F, A, s = self.F, self.A, self.s
        self._tab = []
        for f in self.fs:
            if f == s or not F.is_irred(f):
                continue
            d = len(f) - 1
            s2 = F.pmod(F.pmul(s, s), f)
            tab, x, j = {}, (1,), 0
            while x not in tab:
                tab[x] = j
                x = F.pmod(F.pmul(x, s2), f)
                j += 1
            Ainv = F.ppowmod(A, F.q ** d - 2, f)
            mAinv = F.pscale(F.minus_one, Ainv)
            self._tab.append((f, d, tab, len(tab), mAinv))
        return self._tab

    def solve_dlog(self, P):
        F, k = self.F, self.k
        h = len(self.s) - 1
        n = len(P) - 1
        best = None
        for f, d, tab, order, mAinv in self._tables():
            if f == P:
                continue
            t = F.pmod(F.pmul(P, mAinv), f)
            if t not in tab:
                continue
            j = tab[t]
            while not (k + 2 * j * h < n or k + 2 * j * h > n + d) or k + 2 * j * h == n:
                j += order
            if best is None or j < best[0]:
                best = (j, f)
        if best is None:
            return None
        j, f = best
        Q, b, e = (1,), self.s, j
        while e:
            if e & 1:
                Q = F.pmul(Q, b)
            e >>= 1
            if e:
                b = F.pmul(b, b)
        if not self.verify(P, j, f, Q):
            raise AssertionError(("dlog verification failed", P, j, f))
        return j, f


def is_square(F, P):
    return all(e % 2 == 0 for e in F.factor(P).values())


def main():
    mode = sys.argv[1]
    q = int(sys.argv[2]); F = GF(q); A = parse(sys.argv[3]); s = parse(sys.argv[4])
    assert F.is_irred(s) and F.pmod(A, s) != ()
    if mode == "irr":
        nmin, nmax, J, dmax = map(int, sys.argv[5:9])
        S = Searcher(F, A, s, J, dmax)
        for n in range(nmin, nmax + 1):
            tot = uns = 0
            maxj = maxd = 0
            for P in F.irreds(n):
                if P == s or F.pmod(A, P) == ():
                    continue
                tot += 1
                r = S.solve(P)
                if r is None:
                    uns += 1
                    print("UNSOLVED", P)
                else:
                    maxj = max(maxj, r[0]); maxd = max(maxd, len(r[1]) - 1)
            print(f"q={q} A={A} s={s} n={n}: {tot} irreducible P, unsolved {uns} (max j {maxj}, max deg f {maxd})",
                  flush=True)
    elif mode == "list":
        fn = sys.argv[5]; J, dmax = int(sys.argv[6]), int(sys.argv[7])
        S = Searcher(F, A, s, J, dmax)
        tot = uns = 0
        for line in open(fn):
            line = line.strip()
            if not line:
                continue
            P = tuple(int(c) for c in reversed(line))
            assert F.is_irred(P), line
            if P == s or F.pmod(A, P) == ():
                continue
            tot += 1
            r = S.solve(P)
            if r is None:
                uns += 1
                print("UNSOLVED", line)
        print(f"q={q} A={A} s={s} list {fn}: {tot} P, unsolved {uns}", flush=True)
    elif mode == "t1":
        nmax, J, dmax = map(int, sys.argv[5:8])
        S = Searcher(F, A, s, J, dmax)
        sA = F.pmul(s, A)
        for n in range(1, nmax + 1):
            sq = sqs = ns = nss = 0
            sqdegs = set()
            for P in F.monics(n):
                if len(F.pgcd(P, sA)) > 1:
                    continue
                if is_square(F, P):
                    sq += 1
                    hit = False
                    for j, f in S.candidates(P):
                        assert S.verify(P, j, f), (P, j, f)
                        hit = True
                        sqdegs.add(len(f) - 1)
                    if not hit:
                        r = S.solve_dlog(P)
                        if r is not None:
                            hit = True
                            sqdegs.add(len(r[1]) - 1)
                    sqs += hit
                else:
                    ns += 1
                    nss += S.solve(P) is not None
            print(f"q={q} A={A} s={s} deg P={n}: squares shot-solved {sqs}/{sq} (deg f used: {sorted(sqdegs)}); "
                  f"non-squares shot-solved {nss}/{ns}", flush=True)


if __name__ == "__main__":
    main()
