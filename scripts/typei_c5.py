"""O31 (POINTWISE_TYPEI.md Thm 6.1): every class p mod 840 with p=1 (24), p=2,3 (5), 7 not| p has a
Type-I certificate (c,k,D) with ck<=10, D in {3,7}: D = -p (mod 4ck) and D | p^2+4ck^2 (checked mod 840,
which determines both conditions since 4ck | 40 and D | 21)."""
bad = 0
for p in range(1, 840):
    if p % 24 != 1 or p % 5 not in (2, 3) or p % 7 == 0:
        continue
    ok = [(c, k, D) for (c, k) in [(5, 1), (5, 2), (10, 1)] for D in (3, 7)
          if (D + p) % (4 * c * k) == 0 and (p * p + 4 * c * k * k) % D == 0]
    print(p, ok[:1])
    bad += not ok
print("uncovered classes:", bad)
raise SystemExit(1 if bad else 0)
