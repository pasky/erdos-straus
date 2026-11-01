# Z3090 follow-up: for the sample primes with no level-4C word for C <= 10, find the least C (scan C <= 3000).
import sys
sys.path.insert(0, 'scripts')
from z52d_p2_NC3_kappa import has_words
bad = [3201409, 9110641, 9626137, 9107881, 7878289, 6189361, 8598817, 5124529, 5126929, 3714769, 1135009, 5624137, 3384529, 5923681, 1549321, 1559617, 9013729, 1044697, 1868617, 3919057]
for p in bad:
    least = None
    for C in range(1, 3001):
        if has_words(p, C) > 0:
            least = C; break
    print(p, "least C:", least, " (p mod 840 =", p % 840, ")")
