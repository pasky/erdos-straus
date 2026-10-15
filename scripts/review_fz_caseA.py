"""review_fz_caseA.py (R220): Case A part of (Σ) for q = 3^r, r >= 2, with FF_STERILE_SMALL Lemma 2.1 as tail.
* exact part alpha <= AMAX: R218's review_fs2_caseA.mass (independent of the author's fs_caseA.py);
* per-pattern check of Lemma 2.1 (alpha <= ACHK): min(route i, route ii, route v) <= q^{(alpha-1)/2} 3^{alpha/2}, checked as
  min(...)^2 <= q^{alpha-1} 3^alpha in integers; and #patterns(alpha) <= (alpha+1)^3;
* tail alpha > AMAX in exact rationals: term(alpha) = (alpha+1)^3 q^{-(alpha+1)/2} 3^{alpha/2}
  = (alpha+1)^3 (3/q)^{alpha/2} / sqrt(q), with sqrt(q) >= sq (rational lower bound) and (3/q)^{1/2} <= u (rational upper
  bound); sum over alpha > AMAX by the geometric majorant with ratio ((AMAX+3)/(AMAX+2))^3 u.
usage: uv run python scripts/review_fz_caseA.py r [AMAX=40] [ACHK=60]"""
import sys
from fractions import Fraction as Fr
from math import isqrt, factorial
sys.path.insert(0, 'scripts')
from review_fs2_caseA import mass

r = int(sys.argv[1]); AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40; ACHK = int(sys.argv[3]) if len(sys.argv) > 3 else 60
q = 3**r
N = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
bad = 0
for al in range(1, ACHK + 1):
    npat = 0
    for be in range(al):
        for ka in range(1, al - be + 1):
            f = al - be - ka
            M = max(be, f)
            for la in range(0, M):
                ze = M - la
                npat += 1
                m = min(N(la) * N(be) * q**(ka - 1), N(la) * q**(ka - 1) * q**f,
                        q**ze * (factorial(al) // (factorial(be) * factorial(ka) * factorial(f))))
                if m * m > q**(al - 1) * 3**al:
                    bad += 1
                    print("LEMMA 2.1 per-pattern VIOLATION", al, be, ka, f, la)
    if npat > (al + 1)**3:
        bad += 1
        print("pattern count violation", al, npat)
print(f"q={q}: Lemma 2.1 per-pattern check alpha<={ACHK}: violations={bad}")
exact, _ = mass(q, AMAX)
sq = Fr(isqrt(q * 10**12), 10**6)                  # <= sqrt(q)
u = Fr(isqrt(3 * 10**12 // q) + 1, 10**6)            # >= sqrt(3/q)
a0 = AMAX + 1
first = Fr((a0 + 1)**3) * u**a0 / sq
rho = Fr(a0 + 2, a0 + 1)**3 * u
assert rho < 1
tail = first / (1 - rho)
print(f"q={q}: exact Case A (alpha<={AMAX}) = {float(exact):.10e}  Lemma 2.1 tail <= {float(tail):.4e}  "
      f"total <= {float(exact + tail):.10e}")
