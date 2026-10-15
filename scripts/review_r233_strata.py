"""R233: N-/U on the min<=2 strata (union of the six automatic families) for given n; min>=3 = census total - this."""
import sys
from review_r233_common import spf_sieve, divisors, word_data
n = int(sys.argv[1])
spf = spf_sieve(2 * n + 10)
W = set()
for D in divisors(n + 1, spf):
    W |= {(1, D + 1, (n + 1) // D + 1), (D + 1, 1, (n + 1) // D), (D + 1, (n + 1) // D, 1)}
for D in divisors(2 * n + 1, spf):
    W.add((2, (D + 1) // 2, ((2 * n + 1) // D + 1) // 2))
for D in divisors(n + 2, spf):
    W |= {((D + 1) // 2, 2, (n + 2) // D), ((D + 1) // 2, (n + 2) // D, 2)}
Nm = U = 0
for w in W:
    c, f, _ = word_data(*w, n, spf)
    Nm += (c == -1); U += (not f)
print(n, "min<=2 words", len(W), "N-", Nm, "U", U)
