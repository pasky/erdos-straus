"""R81: independent re-computation of EXCEPTIONAL_WEIGHTS §5.1 (N=300) and checks of
Prop 5.1(b),(d) on that toy family.

Family: primes l <= 100N, l = 3 mod 4, F_l = R(l) = {-u/v mod l : gcd(u,v)=1, 4uv | l+1}.
  * dense primes: (N+1)|F_l| > l
  * random-translate value N prod_dense (1-p)
  * t=0 count #(A cap [1,N])
  * Montgomery-Vaughan large sieve upper bound (N-1+Q^2)/L(Q), optimised over Q
  * Prop 5.1(d) greedy bound
  * my own local search (exact survivors + smoothed objective), lower bound for M(N)
  * p_l <= 1/4 check for small l (needed by Thm 3.3 / Prop 2.1)
"""
import math
import sys
import numpy as np

rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300


def primes_upto(x):
    s = np.ones(x + 1, bool); s[:2] = False
    for i in range(2, int(x ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def R(l):
    A = (l + 1) // 4
    out = set()
    for u in range(1, A + 1):
        if A % u:
            continue
        for v in range(1, A // u + 1):
            if (A // u) % v == 0 and math.gcd(u, v) == 1:
                out.add((-u * pow(v, -1, l)) % l)
    return sorted(out)


fam = [(int(l), R(int(l))) for l in primes_upto(100 * N) if l % 4 == 3]
print(f"N={N}: family size {len(fam)}")
print("small primes with p_l > 1/4:", [(l, len(F), round(len(F) / l, 3)) for l, F in fam if 4 * len(F) > l])
dense = [(l, F) for l, F in fam if (N + 1) * len(F) > l]
print(f"dense primes: {len(dense)}")
rt = N * np.prod([1 - len(F) / l for l, F in dense])
print(f"random translates N prod(1-p) = {rt:.3e} (saving {math.log(N/rt):.2f})")

j = np.arange(1, N + 1)
alive0 = np.ones(N, bool)
for l, F in fam:
    alive0 &= ~np.isin(j % l, F)
print(f"t=0 count = {alive0.sum()} (saving {math.log(N/alive0.sum()):.2f})")

# large sieve
best = math.inf
for Qs in range(2, 400):
    h = np.zeros(Qs + 1); h[1] = 1.0
    for l, F in fam:
        if l > Qs:
            break
        g = len(F) / (l - len(F))
        for q in range(Qs // l, 0, -1):
            if h[q]:
                h[q * l] += h[q] * g
    best = min(best, (N - 1 + Qs * Qs) / h.sum())
print(f"large sieve: M(N) <= {best:.1f} (saving {math.log(N/best):.2f})")

# Prop 5.1(d) greedy bound
gb = 0
for s in range(1, N + 1):
    prod = np.prod([1 - len(F) / l for l, F in fam if l <= s * len(F)])
    gb = max(gb, math.floor(min(s, N * prod)))
print(f"Prop 5.1(d) greedy lower bound = {gb}")

# local search on dense primes (sparse primes are free by the gap argument)
def kills_matrix(c):
    cnt = np.zeros(N, int)
    for (l, F), cl in zip(dense, c):
        cnt += np.isin((j + cl) % l, F)
    return cnt

best_count = 0
for restart in range(3):
    c = [int(rng.integers(l)) for l, F in dense]
    cnt = kills_matrix(c)
    for sweep in range(12):
        changed = 0
        for i, (l, F) in enumerate(dense):
            own = np.isin((j + c[i]) % l, F)
            other = cnt - own
            wgt = 0.3 ** other  # smoothed objective
            # score[c'] = sum of wgt over j killed by c' ; kill iff (j+c') mod l in F
            score = np.zeros(l)
            for f in F:
                np.add.at(score, (f - j) % l, wgt)
            exact = np.zeros(l)
            for f in F:
                np.add.at(exact, (f - j) % l, (other == 0).astype(float))
            key = exact * 1e6 + score
            cn = int(np.argmin(key))
            if cn != c[i]:
                c[i] = cn; changed += 1
                cnt = other + np.isin((j + cn) % l, F)
        surv = int((cnt == 0).sum())
        best_count = max(best_count, surv)
        if changed == 0:
            break
    print(f"  restart {restart}: survivors {surv}")
print(f"local search: M(N) >= {best_count} (saving {math.log(N/best_count):.2f})")
