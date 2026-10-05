"""R42 from-scratch check of Lemma 5.1 (ii),(iii) and (i) as a set equality, m = 4..12, M <= 2500.
Run: PYTHONPATH=scripts uv run python scripts/review_tr_lemma51.py"""
from math import gcd
for m in range(4, 13):
    cnt = 0
    for M in range(m - 1, 2501, m):
        if M < 3:
            continue
        A = (M + 1) // m
        divs = [D for D in range(1, A * A + 1) if (A * A) % D == 0]
        R = {(-m * D) % M for D in divs}
        assert 1 % M not in R, (m, M)                       # (ii)
        for D in divs:                                      # (iii)
            assert gcd(M, m * D + 1) == gcd(M, m * (A * A // D) + 1), (m, M, D)
        R2 = {(-u * pow(v, -1, M)) % M for u in range(1, A + 1) if A % u == 0
              for v in range(1, A // u + 1) if (A // u) % v == 0}   # (i): w = A/(uv)
        assert R == R2, (m, M)
        cnt += 1
    print(f"m={m}: {cnt} moduli OK")
