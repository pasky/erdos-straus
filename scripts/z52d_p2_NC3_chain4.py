# Z2782 follow-up (4-chain test of the slot-lemma structure): chains (a,b,c,d), a..d>=2, continuant K(a,b,c,d)=p (prime).
# Cofactor A = K(b,c,d) (so that [[a,b,c,d]] = p/A, A in (0,p)); sign s = (A/p).  Question: is s a function of the
# residues of (a,b,c,d) mod 4 (given p mod 8)?  (The 3-chain analogue is FOREST_CONNECTIVITY Thm 2.1; a naive 4-chain analogue
# is said to fail in Z2852 — test directly.)
import sys
from collections import defaultdict
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
def K(seq):
    # negative continuant K(b1..bk) with K() =1, K(b1)=b1
    if not seq: return 1
    if len(seq) == 1: return seq[0]
    # recursive: K(b1..bk) = b1 K(b2..bk) - K(b3..bk)
    return seq[0]*K(seq[1:]) - (K(seq[2:]) if len(seq) > 2 else 1)
P = int(sys.argv[1]) if len(sys.argv) > 1 else 600
rows = []
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for b in range(2, p+2):
        for c in range(2, p+2):
            for d in range(2, p+2):
                A = K([b, c, d])
                if A >= p: break
                # a*A - K(c,d) = p  -> a = (p + K(c,d))/A
                num = p + K([c, d])
                if num % A: continue
                a = num // A
                if a < 2: continue
                rows.append((p, (a, b, c, d), A, L.legendre(A, p)))
tab = defaultdict(set)
for p, w, A, s in rows:
    tab[(p % 8, tuple(x % 4 for x in w))].add(s)
bad = [k for k, v in tab.items() if len(v) > 1]
print("4-chains:", len(rows), "classes (p mod 8, entries mod 4):", len(tab), "inconsistent:", len(bad))
print("example inconsistent classes:", bad[:6])
multi = [k for k, v in tab.items() if sum(1 for r in rows if (r[0] % 8, tuple(x % 4 for x in r[1])) == k) >= 2]
print("classes with >=2 representatives:", len(multi), " of which inconsistent:", sum(1 for k in multi if len(tab[k]) > 1))
