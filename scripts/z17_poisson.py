"""z17_poisson.py (O242): Poisson/independence calibration of the q = 3 sibling data (SD §3 table, per slice).
Expected number of alive parents with 3 (resp. >= 2) ball children if the b_d balls of depth d were placed uniformly among
the 3^(d-2) cylinders of depth d of a slice: A_{d-1} p_d^3 (resp. 3 A_{d-1} p_d^2 (1-p_d) + A_{d-1} p_d^3), p_d = b_d/3^(d-2).
Beyond depth 9 two extrapolations of b_d: geometric b_d = 26*3^((d-9)/2) (pessimistic) and flat b_d = 30 (census-like)."""
b = {3: 1, 4: 2, 5: 4, 6: 12, 7: 13, 8: 28, 9: 26}
A = {2: 1, 3: 2, 4: 6, 5: 16, 6: 44, 7: 130, 8: 380, 9: 1130}   # alive cylinders per slice (SD §3)
obs2 = {3: 0, 4: 0, 5: 0, 6: 2, 7: 0, 8: 0, 9: 0}; tot3 = tot2 = 0
for d in range(3, 10):
    p = b[d] / 3 ** (d - 2); e3 = A[d - 1] * p ** 3; e2 = 3 * A[d - 1] * p * p * (1 - p) + e3; tot3 += e3; tot2 += e2
    print(f"d={d}: p_d={p:.4f}  E[#alive parents with 3 balls]={e3:.4f}  E[>=2]={e2:.3f}  observed (SD table) >=2: {obs2[d]}")
print(f"depths 3..9: E[triples] = {tot3:.3f} (P(no triple) = {2.718281828**-tot3:.2f}), E[>=2] = {tot2:.2f}, observed >=2: 2 (both at d = 6), triples: 0")
for name, bf in (("geometric", lambda d: 26 * 3 ** ((d - 9) / 2)), ("flat 30", lambda d: 30)):
    t = 0; Aa = 1130
    for d in range(10, 200):
        p = min(1, bf(d) / 3 ** (d - 2)); t += Aa * p ** 3; Aa = Aa * 3 * (1 - p)
    print(f"beyond depth 9, {name}: E[triples] = {t:.4f}")
