# review_r236_screen.py — R236 from-scratch unit-square screen for n_s = 4^s + k and mixed-point facts (§1.4).
# For each residue s mod L: is there an odd prime q < Q with ord_q(4) | L such that (4^s + k) mod q is 0 or a
# quadratic non-residue?  (Then every mu ≡ s (L) in Ẑ has nu(mu)_q not a unit square, since nu(mu)_q mod q depends on
# mu mod ord_q(4) only.)  Prints the residues that survive.
import sys
import sympy as sp


def screen(k, L, Q):
    qs = [q for q in sp.primerange(3, Q) if pow(4, L, q) == 1]
    alive = set(range(L))
    for q in qs:
        o = sp.n_order(4, q)
        bad = {s for s in range(o) if (pow(4, s, q) + k) % q == 0 or sp.legendre_symbol((pow(4, s, q) + k) % q, q) == -1}
        alive = {s for s in alive if s % o not in bad}
        if not alive:
            break
    return len(qs), sorted(alive)


if __name__ == '__main__':
    for k, L, Q in [(105, 360, 3 * 10 ** 6), (33, 360, 3 * 10 ** 6), (33, 360 * 11, 3 * 10 ** 6)]:
        nq, alive = screen(k, L, Q)
        print('k=%d L=%d Q=%d: %d admissible primes; surviving residues: %s' % (k, L, Q, nq, alive[:20]))
    # mixed point mu* ≡ 844 (2520): components 4 (2-,5-,7-adic), -2 (3-adic)
    for q in (181, 919):
        o = sp.n_order(4, q)
        # mu* mod o by CRT of the l-adic components
        f = sp.factorint(o)
        mods = [l ** e for l, e in f.items()]
        rems = [(-2 if l == 3 else 4) % (l ** e) for l, e in f.items()]
        mu = sp.ntheory.modular.crt(mods, rems)[0]
        r = (pow(4, int(mu), q) + 105) % q
        print('q=%d ord=%d (%s) mu* mod ord=%d  n mod q=%d  legendre=%d' % (q, o, f, mu, r, sp.legendre_symbol(r, q)))
