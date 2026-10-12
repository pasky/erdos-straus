"""R161: search for monic solutions with cancellation at infinity (Lemma 1.2 (iii),(iv)).

mode 'same' (char 3, m=3): monic X<=Y<=Z all of degree d, sum = A/P reduced, A monic, P irreducible, d < n-k.
mode 'two'  (char 2, m=2): monic X<Y of degree d, Z monic of degree > d, sum = A/P with d < n-k.
"""
import sys
from review_ffl_poly import PolyRing

q, mode, d = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
R = PolyRing(q)


def reduce_sum(num, den):
    g = R.gcd(num, den)
    U, V = R.divmod(num, g)[0], R.divmod(den, g)[0]
    c = V[-1]
    return R.scal(R.F.inv[c], U), R.monic(V)


found = 0
mons = list(R.monics(d))
if mode == "same":
    for i, X in enumerate(mons):
        for j in range(i, len(mons)):
            Y = mons[j]
            for Z in mons[j:]:
                num = R.add(R.add(R.mul(X, Y), R.mul(Y, Z)), R.mul(Z, X))
                if not num:
                    continue
                U, V = reduce_sum(num, R.mul(R.mul(X, Y), Z))
                if U and U[-1] == 1 and R.deg(U) >= 1 and R.deg(V) - R.deg(U) > d and R.is_irreducible(V):
                    print("cancel m=3:", R.show(X), R.show(Y), R.show(Z), "A=" + R.show(U), "P=" + R.show(V))
                    found += 1
                    if found >= 5:
                        sys.exit()
else:
    Dz = int(sys.argv[4])
    for i, X in enumerate(mons):
        for Y in mons[i + 1:]:
            for dz in range(d + 1, Dz + 1):
                for Z in R.monics(dz):
                    num = R.add(R.add(R.mul(X, Y), R.mul(Y, Z)), R.mul(Z, X))
                    U, V = reduce_sum(num, R.mul(R.mul(X, Y), Z))
                    if U and U[-1] == 1 and R.deg(U) >= 1 and R.deg(V) - R.deg(U) > d and R.is_irreducible(V):
                        print("cancel m=2:", R.show(X), R.show(Y), R.show(Z), "A=" + R.show(U), "P=" + R.show(V))
                        found += 1
                        if found >= 5:
                            sys.exit()
print("found", found)
