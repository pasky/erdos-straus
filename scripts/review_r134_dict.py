"""R134 referee: from-scratch checks of Prop 2.8 (Gram determinant of Lambda_{d,m}, Hilbert symbols of
(-d,-d(4dm-1)) on Type I tuples) and Lemma 2.9 ((2ai+j)(2bi-j) = -e(1+2ck)) of the automorphic note."""
from fractions import Fraction as F
from sympy import Matrix, primerange, factorint
from review_r134_slices import tuples


def qmul(x, y, A, B):
    # basis 1,i,j,k with i^2=A, j^2=B, k=ij=-ji, k^2=-AB
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return (a0*b0 + A*a1*b1 + B*a2*b2 - A*B*a3*b3,
            a0*b1 + a1*b0 - B*a2*b3 + B*a3*b2,
            a0*b2 + a2*b0 + A*a1*b3 - A*a3*b1,
            a0*b3 + a3*b0 + a1*b2 - a2*b1)


def gram_det(d, m):
    A, B = -d, -d*(4*d*m-1)
    u = (0, 1, 0, 0)
    v = (0, F(-1, 2*d), F(1, 2*d), 0)            # v = (w-u)/(2d), w=j
    one = (1, 0, 0, 0)
    assert qmul(u, u, A, B) == (-d, 0, 0, 0)
    assert qmul(v, v, A, B) == (-m, 0, 0, 0)
    s = tuple(a+b for a, b in zip(qmul(u, v, A, B), qmul(v, u, A, B)))
    assert s == (1, 0, 0, 0)
    basis = [one, u, v, qmul(u, v, A, B)]
    G = Matrix(4, 4, lambda r, c: 2*qmul(basis[r], basis[c], A, B)[0])
    return G.det()


def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p for odd prime p, or p=2, via standard formulas; p=-1 for infinity."""
    if p == -1:
        return -1 if (a < 0 and b < 0) else 1
    def split(x):
        v = 0
        while x % p == 0:
            x //= p; v += 1
        return v, x
    al, u = split(a); be, w = split(b)
    if p != 2:
        leg = lambda t: 1 if pow(t % p, (p-1)//2, p) == 1 else -1
        eps = (p-1)//2
        return ((-1)**(al*be*eps)) * leg(u)**be * leg(w)**al
    eps = lambda t: ((t-1)//2) % 2
    om = lambda t: ((t*t-1)//8) % 2
    return (-1)**(eps(u)*eps(w) + al*om(w) + be*om(u))


for d in range(1, 8):
    for m in range(1, 8):
        assert gram_det(d, m) == -(4*d*m-1)**2, (d, m)
cnt = 0
for p in primerange(5, 300):
    VI, VII = tuples(p)
    for (a, b, c, d, e) in VI:
        A, B = -d, -d*(4*d*a*b-1)
        assert 4*d*a*b-1 == p*e
        ram = {l for l in list(factorint(2*d*p*e)) + [-1] if hilbert(A, B, l) == -1}
        assert ram == {p, -1}, (p, a, b, c, d, e, ram)
        cnt += 1
    for (a, b, c, d, e) in VII:
        A, B = -d, -p
        lhs = qmul((0, 2*a, 1, 0), (0, 2*b, -1, 0), A, B)
        assert lhs == (-e, 0, 0, -2*c*e)
print('Gram dets ok; B_{p,inf} ramification ok on', cnt, 'Type I tuples; Lemma 2.9 ok')
