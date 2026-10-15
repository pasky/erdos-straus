"""review_r250_example.py (R250): re-check the FF_INVERSION_CHECK Prop 1.4 example (q = 3, A = T^2, a = 1, b = T, e = T + 1)
and the review counterexample (a, b, e) = (1, T, 1)."""
from review_r250_gf import Field
F = Field(3); A = F.Tpow(2)
P = (2, 1, 2, 0, 1, 0, 1)  # T^6 + T^4 + 2T^2 + T + 2
a, b, e = (1,), (0, 1), (1, 1)
assert F.irreducible(P)
num = F.add(F.mul(e, P), (1,)); d, r = F.divmod(num, F.mul(A, F.mul(a, b))); assert not r and d[-1] == 1
c = F.exact(F.add(a, b), e)
X1, X2, X3 = F.mul(F.mul(a, F.mul(b, d)), P), F.mul(a, F.mul(c, d)), F.mul(b, F.mul(c, d))
assert F.mul(A, F.mul(X1, F.mul(X2, X3))) == F.mul(P, F.add(F.mul(X1, X2), F.add(F.mul(X2, X3), F.mul(X3, X1))))
E = F.sub(F.mul(A, X2), P)
print("degrees", [F.deg(x) for x in (X1, X2, X3)], "E_FF =", E, "(low->high)")
assert [F.deg(x) for x in (X1, X2, X3)] == [11, 4, 5] and E == (1, 2, 0, 1, 0, 1)
# counterexample: P == -1 mod T^3 is the I4(1, T, 1) class and the validity class of (1; 0, T; 1, 1)
for P in F.monics(5):
    if P[0] == 0 or not F.irreducible(P):
        continue
    i4 = not F.mod(F.add(P, (1,)), F.Tpow(3))
    X, r = F.divmod(F.add(P, (1,)), A)
    lin = (not r) and F.divides((0, 1), X)  # E = 1 divides everything, s = T + P has lc 1
    assert i4 == lin
print("example and counterexample OK")
