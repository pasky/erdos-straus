"""R181: per-point checks on complete solution sets (solutions() from review_dr_bl, own code):
 (S) Lemma 2.1 Steinberg identity place by place: inv_v(alpha) = inv_v(y,-1) + inv_v(x,y), x = lam*u1 - 1, y = -u2/u3;
 (C) Cor 2.3: c=(1,1,1), P prime, X1 P-free, P | X2, X3: inv_P(alpha) = class of -f, f = A X2/P - 1 (either sign conv.);
 (L) Lemma 3.2: if deg X1 > n - deg A: inv_inf(alpha) = class of c1^{dX2-dX3} (c3/c2)^{degA+dX1-n} (odd m).
Usage: review_dr_checks.py p m Acoeffs n mode [c1 c2 c3]"""
import sys, collections
from review_dr_ff import FF
from review_dr_bl import solutions

def main():
    p, m = int(sys.argv[1]), int(sys.argv[2]); A = tuple(int(t) for t in sys.argv[3].split(','))
    n = int(sys.argv[4]); mode = sys.argv[5]
    c = tuple(int(t) for t in sys.argv[6:9]) if len(sys.argv) > 6 else (1, 1, 1)
    F = FF(p); k = len(A) - 1; st = collections.Counter()
    if mode == 'irr':
        Ps = [(P, P) for P in F.monics(n) if F.is_irred(P) and F.gcd(P, A) == (1,)]
    else:
        e = int(mode.split(':')[1])
        Ps = [(F.pw(Q, e), Q) for Q in F.monics(n // e) if F.is_irred(Q) and F.gcd(Q, A) == (1,)]
    ic = F.inv
    for P, Q in Ps:
        for X in solutions(F, A, P, c, n):
            u = [(X[i], (c[i],)) for i in range(3)]   # u_i = X_i / c_i as (num, den)
            a = (F.scal((-c[2]) % p, X[0]), F.scal(c[0], X[2]))
            b = (F.scal((-c[2]) % p, X[1]), F.scal(c[1], X[2]))
            # x = (A/P)(X1/c1) - 1 = (A X1 - c1 P)/(c1 P); y = b
            x = (F.sub(F.mul(A, X[0]), F.scal(c[0], P)), F.scal(c[0], P))
            if not x[0]: st['x=0'] += 1; continue
            inv_a = F.all_invariants(a, b, m)
            inv_s1 = F.all_invariants(b, ((p - 1,), (1,)), m)
            inv_s2 = F.all_invariants(x, b, m)
            places = set(inv_a) | set(inv_s1) | set(inv_s2)
            ok = all((inv_a.get(v, 0) - inv_s1.get(v, 0) - inv_s2.get(v, 0)) % m == 0 for v in places)
            st['S ok' if ok else 'S FAIL'] += 1
            if c == (1, 1, 1) and mode == 'irr':
                vs = [F.val(t, P)[0] for t in X]
                if vs[0] == 0 and vs[1] >= 1 and vs[2] >= 1:
                    f = F.sub(F.mul(A, F.divmod(X[1], P)[0]), (1,))
                    z = F.powmod(F.neg(f), (p ** n - 1) // m, P)
                    sym = F.dlog(z[0], m); got = inv_a.get(P, 0)
                    st['C ok' if got == sym else ('C ok(inv conv)' if got == (-sym) % m else 'C FAIL')] += 1
                    st['C value', sym] += 1
            if m % 2 and len(X[0]) - 1 > n - k:
                d1, d2, d3 = (len(t) - 1 for t in X)
                val = pow(c[0], (d2 - d3) % (p - 1), p) * pow(c[2] * ic[c[1]] % p, (k + d1 - n) % (p - 1), p) % p
                pred = F.dlog(pow(val, (p - 1) // m, p), m); got = inv_a['inf']
                st['L ok' if got == pred else ('L ok(inv conv)' if got == (-pred) % m else 'L FAIL')] += 1
    print(f"p={p} m={m} A={A} n={n} {mode} c={c}:", dict(sorted(st.items(), key=str)))

if __name__ == "__main__":
    main()
