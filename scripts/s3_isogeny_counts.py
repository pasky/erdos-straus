"""O208 memo s3_isogeny_mixing: number of chi = -1 words (five-slice certificates, (J)32/(J)35: certificate edges of the
supersingular 2-isogeny graph) versus the number of vertices N ~ p/12. Usage: s3_isogeny_counts.py"""
import sys
from s3_words_parity import orbits      # noqa: E402
from sympy import nextprime              # noqa: E402
for p0 in (10**3, 10**4, 10**5, 10**6):
    p, rows = p0, []
    for _ in range(20):
        p = nextprime(p)
        ob = orbits(p)
        rows.append(sum(s for c, s in ob if c == -1))
    print('p ~ %8d: chi=-1 words: mean %.1f max %d ; vertices N ~ p/12 = %d ; ratio max/N = %.2e' % (
        p0, sum(rows) / len(rows), max(rows), p0 // 12, max(rows) / (p0 / 12)))
