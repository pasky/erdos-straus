"""R212: re-count the mod-8 cells of FOUR_SPECIFIC §2 (100/100/40) from scratch.
Cells (t,u,v) mod 8 with n = tuv-u-v odd; slots A=tu-1, A*=tv-1, t, u, v.  chi=-1 cell <=> some slot = 0 mod 4
(MODEL_SPECIFIC Thm 3.1(a)); additionally chi computed from the Lemma 3.0' cell formula as a cross-check."""
from collections import Counter
c = Counter()
for t in range(8):
    for u in range(8):
        for v in range(8):
            n = (t*u*v - u - v) % 8
            if n % 2 == 0:
                continue
            A, As = (t*u - 1) % 8, (t*v - 1) % 8
            slots = [A, As, t, u, v]
            four = any(s % 4 == 0 for s in slots)
            # Lemma 3.0': 2*(A/n) = n+1 - n(t+u+v-9) - A - A* (mod 8); chi = (-1/n)(A/n)
            r = (n + 1 - n*(t+u+v-9) - A - As) % 8
            An = {2: 1, 6: -1}[r]
            chi = (1 if n % 4 == 1 else -1) * An
            assert (chi == -1) == four
            if not four:
                c['chi+1'] += 1
                continue
            o = any(s % 8 == 4 for s in slots)
            e = any(s % 8 == 0 for s in slots)
            c[('oneodd' if o else '') + ('S8' if e else '')] += 1
print(c)
