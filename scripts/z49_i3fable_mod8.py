import sys, numpy as np
sys.argv=['x','/tmp/i3_1e7','1000000','10000000']
sys.path.insert(0,'scripts')
import z49_i3fable_stats as S
from math import log, isqrt
prefix, LO, HI = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
I3 = np.fromfile(prefix + "_i3.u16", dtype=np.uint16).astype(np.float64)
N = len(I3) - 1; n = np.arange(N + 1, dtype=np.int64)
grid = np.unique(np.round(np.exp(np.linspace(log(LO), log(HI), 60))).astype(np.int64))
M0g = np.array([S.M0_exact(int(g)) for g in grid])
M0 = np.zeros(N + 1); sel = n >= LO; M0[sel] = np.interp(np.log(n[sel]), np.log(grid), M0g)
Z = 1.5198177; Sdiv = np.full(N + 1, Z); done = np.zeros(N + 1, dtype=bool)
for l in range(2, N + 1):
    if done[l]: continue
    Sdiv[l::l] *= (l * l - l + 1) / (l * l + 1)
    if l * l <= N: done[l * l::l] = True
    done[l] = True
sq = np.zeros(N + 1, dtype=bool); r = np.arange(isqrt(N) + 1); sq[r * r] = True
isprime = np.ones(N + 1, dtype=bool); isprime[:2] = False
for l in range(2, isqrt(N) + 1):
    if isprime[l]: isprime[l * l::l] = False
win = (n >= LO) & (n <= HI) & ~sq
print("odd non-squares by n mod 8; primes by p mod 8; and by n mod 3 (odd), n mod 5")
for r8 in (1,3,5,7):
    m = win & (n % 8 == r8); mp = m & isprime
    print(f"n={r8} mod 8: all {np.mean(I3[m]/(Sdiv[m]*M0[m])):.4f}  primes {np.mean(I3[mp]/(Sdiv[mp]*M0[mp])):.4f} (count {mp.sum()})")
for r3 in (0,1,2):
    m = win & (n % 2 == 1) & (n % 3 == r3)
    print(f"odd n={r3} mod 3: {np.mean(I3[m]/(Sdiv[m]*M0[m])):.4f}")
for r4 in (0,2):
    m = win & (n % 4 == r4)
    print(f"n={r4} mod 4: {np.mean(I3[m]/(Sdiv[m]*M0[m])):.4f}")
for r16 in (1,9,5,13,3,11,7,15):
    m = win & (n % 16 == r16)
    print(f"n={r16} mod 16: {np.mean(I3[m]/(Sdiv[m]*M0[m])):.4f}")
