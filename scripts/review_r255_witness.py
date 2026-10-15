"""R255: from-scratch check of MENU_LADDER Prop 3.1 on O240 Theorem B (n = 48X^4+1 = 3Y^4+1, Y = 2X).
Theorem B as Type II: a = 3, b = 2X^2+2X+1, d = 2X^2-2X+1, c = 2(X^2+X+2)/11 (lambda = 1); f = 4acd - 1.
Checks the identity, then W(f) = prod_{v|2} (alpha, beta)_v and the full product formula split
(2-part, c0-part, other odd places, real places) with beta = theta(theta-1), A = Q[Y]/(3Y^4+1)."""
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**8, silent=True)
X = pari('X')
a, b, d, c = pari(3), pari('2*X^2+2*X+1'), pari('2*X^2-2*X+1'), pari('2*(X^2+X+2)/11')
n = pari('48*X^4+1')
assert c*n - (4*a*b*c*d - a - b) == 0
for sgn in (-1, 1):
    f = 4*a*c*d + sgn   # sgn = -1: the actual witness; sgn = +1: constant sign changed (author's control)
    fY = pari.subst(f, 'X', pari('y/2'))
    # monic model: eta = 3*theta, eta^4 + 27 = 0 ; theta = eta/3
    gm = pari('y^4+27'); K = pari.nfinit(gm)
    alpha = pari(f'Mod(subst({fY}, y, y/3), {gm})')
    beta = pari(f'Mod((y/3)*(y/3-1), {gm})')
    num, den = pari.idealfactor(K, alpha), None
    primes = set(int(p) for p in pari.factor(pari.idealnorm(K, alpha))[0]) | {2, 3}
    parts = {}
    for p in sorted(primes):
        for pr in pari.idealprimedec(K, p):
            h = int(pari.nfhilbert(K, alpha, beta, pr))
            key = '2' if p == 2 else ('c0' if p == 3 else 'odd')
            parts[key] = parts.get(key, 1) * h
    print('constant', sgn, 'parts', parts, 'product', parts['2']*parts['c0']*parts.get('odd', 1))
