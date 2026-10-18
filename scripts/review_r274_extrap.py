"""R274 from-scratch recomputation of DISPROOF_AVENUES §4.4/§4.5 numbers from the stated law
P(f = 0) = exp(-a mu^beta), mu = c L^k (L = ln p), prime density 1/L:
E#[A,B) = int_{ln A}^{ln B} exp(L - a (c L^k)^beta) / L dL   (all primes at the same c: 'uniform-c' model).
Done in log-space (mpmath) so tiny values are exact-ish.  Also: floor/mixture counter-model for §4.5."""
import mpmath as mp
mp.mp.dps = 30
LN10 = mp.log(10)

def E(a, beta, c, A, B, k=3, c_at=None):
    """if k == 2, mu = c * L0 * L^2 with L0 = ln 1e8 (matched to c L^3 at 1e8)"""
    L0 = 8*LN10
    def g(L):
        mu = c*L**3 if k == 3 else c*L0*L**2
        return mp.exp(L - a*mu**beta)/L
    lo, hi = mp.log(A), mp.log(B)
    pts = mp.linspace(lo, hi, 60)
    return mp.quad(g, pts)

def show(tag, v): print(f'{tag}: {mp.nstr(v, 3)}')

if __name__ == '__main__':
    a = 0.535
    print('--- §4.5 table (uniform c), and Salez 1e17 variant ---')
    for c, b in [(0.074, 0.91), (0.074, 0.55), (0.074, 0.50), (0.074, 0.45), (0.037, 0.55), (0.037, 0.50), (0.037, 0.6)]:
        lo = E(a, b, c, 1e8, 1e18); hi = E(a, b, c, 1e18, 1e60)
        lo17 = E(a, b, c, 1e8, 1e17); hi17 = E(a, b, c, 1e17, 1e60)
        print(f'c={c} beta={b}: E[1e8,1e18)={mp.nstr(lo,3)} E[1e18,1e60)={mp.nstr(hi,3)} | '
              f'E[1e8,1e17)={mp.nstr(lo17,3)} E[1e17,1e60)={mp.nstr(hi17,3)}  P(none<=1e18)*E[beyond]={mp.nstr(mp.exp(-lo)*hi,3)}')
    # sup over beta of E[beyond] * P(none below) (Poisson): the "conditioned" claim <~ 1e-2
    best = max(((mp.exp(-E(a, b, c, 1e8, 1e18))*E(a, b, c, 1e18, 1e60)), b, c)
               for c in (0.037, 0.074) for b in [0.40 + 0.005*i for i in range(60)])
    print('max over beta in [0.40,0.70], c in {0.037,0.074} of exp(-E_below)*E_beyond:', mp.nstr(best[0], 3), 'at beta', best[1], 'c', best[2])
    best17 = max(((mp.exp(-E(a, b, c, 1e8, 1e17))*E(a, b, c, 1e17, 1e60)), b, c)
                 for c in (0.037, 0.074) for b in [0.40 + 0.005*i for i in range(60)])
    print('same with verification only to 1e17 (Salez):', mp.nstr(best17[0], 3), 'at beta', best17[1], 'c', best17[2])
    print('--- §4.4 uniform-c (hardest cell c = 0.037 for ALL primes; pessimistic vs cell-weighted) ---')
    for tag, aa, b, k in [('fit L3', a, 0.91, 3), ('fit L2', a, 0.91, 2), ('a-30% L3', 0.7*a, 0.91, 3),
                          ('a-30% L2', 0.7*a, 0.91, 2), ('flatter a=.4 b=.8 L3', 0.4, 0.8, 3), ('flatter a=.4 b=.8 L2', 0.4, 0.8, 2)]:
        print(f'{tag}: E[1e8,1e18)={mp.nstr(E(aa,b,0.037,1e8,1e18,k),3)}  E[1e18,1e300)={mp.nstr(E(aa,b,0.037,1e18,1e300,k),3)}')
    print('worst case: mu = 0.0117 L^3 at 1e18:', mp.nstr(0.0117*(18*LN10)**3, 4), ' -ln P =', mp.nstr(a*(0.0117*(18*LN10)**3)**0.91, 4))
    print('--- floor/mixture counter-model for §4.5: P(f=0) = max(exp(-a mu^b), eps) ---')
    for eps in (1e-19, 1e-18, 1e-17):
        below = eps*(mp.li(1e18) - mp.li(1e8)); beyond = eps*(mp.li(1e60) - mp.li(1e18))
        print(f'eps={eps}: E[1e8,1e18) ~ {mp.nstr(below,3)}  E[1e18,1e60) ~ {mp.nstr(beyond,3)}')
    print('--- power-law-in-p mixture: P(f=0) = p^-(1-delta) ---')
    for d in (0.0, 0.05):
        g = lambda L: mp.exp(L - (1 - d)*L)/L
        print(f'delta={d}: E[1e8,1e18)={mp.nstr(mp.quad(g,[8*LN10,18*LN10]),3)}  E[1e18,1e60)={mp.nstr(mp.quad(g,[18*LN10,60*LN10]),3)}')
