"""R195: counterexample to the FF_MUTE Prop 5.4 'Reading' sentence "an admissible f has a prime divisor g not dividing As".
q = 3, A = T, s = T + 2 (= T - 1, s = -1 mod T): f = s^3 = T^3 - 1 is = -1 (mod A), and with Q = 1 the shot P + A
is divisible by f whenever P = -A (mod s^3). Prop 2.1 then gives a valid mute (indeed ES_q) solution; such P
are unconstrained at every prime g not dividing As, so the set of points 'x with -xA a non-square mod every prime
g not dividing As' is NOT sterile for this shot (it is sterile if the non-square condition is imposed at s too)."""
from review_fm_ff import GF
from review_fm_search import Searcher

F = GF(3)
A, s = (0, 1), (2, 1)
f = F.pmul(s, F.pmul(s, s))
assert F.pmod(F.padd(f, (1,)), A) == (), "f = -1 mod A"
S = Searcher(F, A, s, 0, 3)
cnt = 0
for n in (4, 5, 6):
    for P in F.irreds(n):
        if F.pmod(F.padd(P, A), f) == ():
            assert S.verify(P, 0, f), P
            cnt += 1
print(f"f = s^3 = {f}: {cnt} irreducible P of degree 4..6 with P = -A mod s^3, all solved by the shot (f, Q = 1), "
      f"verified exactly")
