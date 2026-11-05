"""z59 CONV2: how does each line rescue the other's zeros?  For n in a list, compute in the one-line form of Lemma 1:
  least T >= 1 with  Tn+1  having a divisor f ≡ -1 (mod 4T)      (a = 1 events; tagged by T mod 4)
  least T ≡ 0 (4) with Tn+1 having a divisor f ≡ -1 (mod T)       ((★) events)
plus the full list of T <= TMAX carrying an event of each kind, and the factorisation of n.
Usage: python3 z59_conv2_rescue.py TMAX file_or_list ...
"""
import sys
from sympy import factorint, divisors

def events(n, TMAX):
    a1 = []; st = []
    for T in range(1, TMAX + 1):
        N = T * n + 1
        ds = divisors(N)
        if any(f % (4 * T) == 4 * T - 1 for f in ds): a1.append(T)
        if T % 4 == 0 and any(f % T == T - 1 for f in ds): st.append(T)
    return a1, st

def main():
    TMAX = int(sys.argv[1]); ns = []
    for a in sys.argv[2:]:
        try: ns.append(int(a))
        except ValueError:
            ns += [int(l) for l in open(a) if l.strip() and not l.startswith('#')]
    hist = {}
    for n in ns:
        a1, st = events(n, TMAX)
        k = (a1[0] if a1 else None, a1[0] % 4 if a1 else None)
        hist[k[1]] = hist.get(k[1], 0) + 1
        print(n, dict(factorint(n)), "a1_T:", a1[:12], "star_T:", st[:8])
    print("# least a=1 T mod 4 histogram:", hist)

main()
