"""R233: from-scratch test of Prop F / F' on primes p = 1 (8) < LIMIT.
For s in 1..8 and family kinds 'u' (u = s, fixed side p+s; v = s symmetric) and 't' (t = s, fixed side sp+1):
  enumerate all words, test  X unclean <=> family has certificate <=> family has unforced word."""
import sys
from sympy import primerange
from review_r233_common import spf_sieve, jacobi, clean, divisors, word_data

LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
spf = spf_sieve(20 * LIM)
stats = {}
for p in primerange(3, LIM):
    if p % 8 != 1:
        continue
    for s in range(1, 9):
        for kind in ('u', 't'):
            X = p + s if kind == 'u' else s * p + 1
            words = []
            for D in divisors(X, spf):
                if (D + 1) % s:
                    continue
                if kind == 'u':   # A = D = s t - 1, v = X / D
                    t, u, v = (D + 1) // s, s, X // D
                else:             # A = D = s u - 1, B = X/D = s v - 1
                    B = X // D
                    if (B + 1) % s:
                        continue
                    t, u, v = s, (D + 1) // s, (B + 1) // s
                words.append(word_data(t, u, v, p, spf))
            uncl = not clean(X, p, spf)
            cert = any(c == -1 for c, f, _ in words)
            unf = any(not f for c, f, _ in words)
            key = (s, kind)
            st = stats.setdefault(key, [0, 0, 0, 0])
            st[0] += 1
            st[1] += (uncl != cert)
            st[2] += (unf != cert)
            st[3] += (uncl != unf)
            # Lemma S sanity
            assert not any(c == -1 and f for c, f, _ in words)
print("s kind  #p  [uncl!=cert] [unforced!=cert] [uncl!=unforced]")
for k in sorted(stats):
    print(k, stats[k])
