"""R175 from-scratch check of bsB_zolotarev_transpose items 1-3 for certificates with n = 1 mod 4 <= NMAX."""
import sys
def perm_sign(perm):
    seen = [False] * len(perm); s = 1
    for i in range(len(perm)):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = perm[j]; L += 1
            if L % 2 == 0: s = -s
    return s
NMAX = int(sys.argv[1]); cnt = tr = bad = 0
for n in range(5, NMAX + 1, 4):
    for g in range(3, n + 3, 4):
        for f in range(3, 10 ** 9, 4):
            m = g * f - 1
            if m - f > n: break
            if (n + f) % m: continue
            c = (n + f) // m
            if c < 1: continue
            mpp = c * g - 1; cnt += 1
            assert m * mpp == g * n + 1 and m % 4 == 0 and mpp % g == g - 1
            sn = perm_sign([(k * m) % n for k in range(n)])
            sg = perm_sign([(k * m) % g for k in range(g)])
            sn2 = perm_sign([(k * mpp) % n for k in range(n)])
            if not (sn == -1 and sg == -1 and sn2 == -1): bad += 1
            if m * mpp <= 2000:
                M = m * mpp - 1
                # transpose of m x m'' row-major array
                T = [0] * (M + 1)
                for i in range(m):
                    for j in range(mpp):
                        T[i * mpp + j] = j * m + i
                ok = all(T[k] == (k * m) % M for k in range(M)) and T[M] == M
                s_formula = (-1) ** ((m * (m - 1) // 2) * (mpp * (mpp - 1) // 2))
                if not ok or perm_sign(T) != s_formula or s_formula != 1: bad += 1
                tr += 1
print("certificates", cnt, "explicit transposes", tr, "violations", bad)
