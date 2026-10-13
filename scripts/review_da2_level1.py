"""R187: size of the level-1 part of S(r) = sum_k 6 f(r^k) r^-k + sum_K 2 f_II^N(r^K) r^-ceil(K/2):
the k = 1 term 6 f(r)/r and the K = 1 term 2 f_II(r)/r, for primes r (EVIDENCE only; shows how far from
S(r) < 1/2 small r are).  f via review_da2_rgeneric.es_solutions (from scratch)."""
import sys
from sympy import primerange
from review_da2_rgeneric import es_solutions
lo, hi, step = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
for r in list(primerange(lo, hi))[::step]:
    f = len(es_solutions(r)); f2 = len(es_solutions(r, only_type2=True))
    print(r, f, f2, round(6 * f / r + 2 * f2 / r, 3))
