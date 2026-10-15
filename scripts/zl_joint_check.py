"""zl_joint_check.py -- O228 (STERILE_LOWER.md Lemma 3.1; EVIDENCE check of a PROVED lemma): the P-data of every N in [X, 2X)
are exactly the triples (a, c, d) with N == -4a^2 d (mod 4acd - 1) and cN >= 4a^2cd - 2a (<=> a <= b); the Q-data of every n are
exactly the (a, d, f, c) with f | 4a^2 d + 1, n = 4acd - f, b = (na + c)/f >= a.  Compares joint counts with per-n
enumeration (review_se2_identities.P_data / Q_data) for all n in [X, 2X)."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_se2_identities import P_data, Q_data
X = int(sys.argv[1])
JP = [0] * X; JQ = [0] * X
a = 1
while 4 * a * a - 2 * a < 2 * X:                # P: 4a^2 d - 2a/c <= N < 2X
    d = 1
    while 4 * a * a * d - 2 * a < 2 * X:
        c = 1
        while True:
            f = 4 * a * c * d - 1
            if f - 4 * a * a * d >= 2 * X: break   # least admissible N >= f - 4a^2 d
            N0 = (-4 * a * a * d) % f
            lo = max(X, -((2 * a - 4 * a * a * c * d) // c))   # ceil(4a^2 d - 2a/c)
            N = N0 + ((lo - N0 + f - 1) // f) * f
            while N < 2 * X:
                JP[N - X] += 1; N += f
            c += 1
        d += 1
    a += 1
for a in range(1, 2 * X + 2):                    # Q: 4acd = n + f <= 2n + 1 < 4X + 1
    for d in range(1, (4 * X + 1) // (4 * a) + 1):
        m = 4 * a * a * d + 1
        for f in range(1, min(m, 2 * X + 2) + 1):
            if m % f: continue
            c = (X + f + 4 * a * d - 1) // (4 * a * d)
            while 4 * a * c * d - f < 2 * X:
                n = 4 * a * c * d - f
                if (n * a + c) // f >= a: JQ[n - X] += 1
                c += 1
bad = 0
for n in range(X, 2 * X):
    p, q = len(P_data(n)), len(Q_data(n))
    if (p, q) != (JP[n - X], JQ[n - X]): bad += 1; print("mismatch", n, p, JP[n - X], q, JQ[n - X])
print(f"X={X}: {X} values of n checked, total P {sum(JP)}, Q {sum(JQ)}, mismatches {bad}")
