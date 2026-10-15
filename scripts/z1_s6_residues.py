"""z1: S_6 on norm-one triples (1,a+1,b+1),(a+1,1,b),(b+1,1,a): no mixed residue pair (a,b) mod 6 with n = ab-1 coprime to 6."""
# S6 on norm-one triples: all (a,b) mod 6 with ab even, ab-1 coprime to 6
bad = 0
for a in range(6):
    for b in range(6):
        if (a*b) % 2 or (a*b - 1) % 3 == 0: continue
        P = [(1,a+1,b+1,a,b), (a+1,1,b,a,(a+1)*b-1), (b+1,1,a,b,(b+1)*a-1)]
        s = {any(x % 6 == 0 for x in q) for q in P}
        if len(s) > 1: bad += 1; print('mixed', a, b)
print('S6 norm-one residue check: mixed residue pairs', bad)
