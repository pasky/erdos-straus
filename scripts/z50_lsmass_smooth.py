"""z50 lsmass: smooth first moments M(y) = sum_{P(G)<=y} (class count at G)/G, truncated at G <= X.
U/ES5 W1 core: tau(M+1)/M ; W2 core: tau(m)/m (ordered pairs uv=m) ; ES R(M): tau(A_M^2)/M (M==3 mod 4).
Growth in log y: expect exponent 2 for W1/W2 (Theorem 3.2 input) and 3 for R(M)."""
import numpy as np, math, json, sys
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
L = X + 2
spf = np.zeros(L + 1, dtype=np.int64)
for i in range(2, int(L**0.5) + 1):
    if spf[i] == 0:
        s = spf[i*i::i]; s[s == 0] = i; spf[i*i::i] = s
idx = np.nonzero(spf == 0)[0]; spf[idx] = idx
# largest prime factor and tau via iterative division (vectorized)
n = np.arange(L + 1, dtype=np.int64)
lpf = np.ones(L + 1, dtype=np.int64)
tau = np.ones(L + 1, dtype=np.int64)
tau2 = np.ones(L + 1, dtype=np.int64)   # tau(n^2)
rem = n.copy(); rem[0] = 1
while True:
    act = rem > 1
    if not act.any(): break
    p = spf[rem]
    e = np.zeros_like(rem)
    while True:
        dv = act & (rem % np.where(p > 0, p, 1) == 0)
        if not dv.any(): break
        rem[dv] //= p[dv]; e[dv] += 1
    tau[act] *= (e[act] + 1); tau2[act] *= (2 * e[act] + 1)
    lpf[act] = np.maximum(lpf[act], p[act])
M = np.arange(2, X + 1)
w1 = tau[M + 1] / M
w2 = tau[M] / M
r3 = np.where(M % 4 == 3, tau2[(M + 1) // 4] / M, 0.0)
out = []
for y in (5, 10, 30, 100, 300, 1000):
    sm = lpf[M] <= y
    out.append({"y": y, "W1": float(w1[sm].sum()), "W2": float(w2[sm].sum()), "R": float(r3[sm].sum())})
for i in range(1, len(out)):
    a, b = out[i-1], out[i]
    r = math.log(math.log(b["y"]) / math.log(a["y"]))
    b["slope_W1"] = math.log(b["W1"]/a["W1"])/r; b["slope_W2"] = math.log(b["W2"]/a["W2"])/r; b["slope_R"] = math.log(b["R"]/a["R"])/r
for o in out: print({k: round(v, 3) for k, v in o.items()})
json.dump({"X": X, "rows": out}, open("data/z50_lsmass/smooth.json", "w"), indent=1)
