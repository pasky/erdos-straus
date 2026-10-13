"""R167: the local density at an anisotropic prime is NOT >= N^{-o(1)} in general.
Q = x^2+y^2+3z^2+3w^2 (norm form of the quaternion algebra (-1,-3), ramified at 3 and infinity).
Compute r_Q(N) exactly by convolving binary counts r2(m) = #{x^2+y^2=m}; compare r_Q(N)/N for N = 9^k*u
(large v_3(N)) with N coprime to 3. Main term of a quaternary form is ~ const * sigma(N) * N, so a bounded
r_Q(9^k u) means the 3-adic density decays like N^{-1}."""
import numpy as np
NMAX = 9**5 * 2
r2 = np.zeros(NMAX + 1, dtype=np.int64)
s = int(NMAX**0.5) + 1
for x in range(-s, s + 1):
    y = np.arange(-s, s + 1)
    v = x * x + y * y
    v = v[v <= NMAX]
    np.add.at(r2, v, 1)
def rQ(N):
    t = np.arange(0, N // 3 + 1)
    return int(np.sum(r2[N - 3 * t] * r2[t]))
for u in (1, 2, 5, 7):
    row = []
    for k in range(0, 6):
        N = 9**k * u
        if N > NMAX: break
        row.append((N, rQ(N), rQ(N) / N))
    print(f"u={u}:", "  ".join(f"N={N}: r={r} r/N={q:.3g}" for N, r, q in row))
