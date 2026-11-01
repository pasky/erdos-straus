# Z2788: commute-time / resistance order on words. Network for a word: series–parallel continued-fraction network
# with R_eff = [a1; a2, ...] (regular CF of A/p, unit resistors); here we use R = A/p (its regular CF of A/p; the HJ
# word gives the same rational up to inversion). Test: order words of p by R = A/p (and by its inverse), count sign changes
# along the order, compare with the expected number under random order (sign changes of a random permutation).
import sys, random
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
tot_obs = tot_rand = 0; n_p = 0; ties = 0
random.seed(0)
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    W = L.words(p)
    if len(W) < 3: continue
    pts = sorted(((t*u-1)/p, L.legendre(t*u-1, p)) for (t, u, v) in W)
    s = [x[1] for x in pts]
    obs = sum(1 for i in range(len(s)-1) if s[i] != s[i+1])
    rnd = 0
    for _ in range(200):
        r = s[:]; random.shuffle(r)
        rnd += sum(1 for i in range(len(r)-1) if r[i] != r[i+1])
    tot_obs += obs; tot_rand += rnd/200; n_p += 1
print("primes", n_p, "sign changes along resistance order: observed", tot_obs, "random-order mean", round(tot_rand,1))
# pair-respecting null: words come in pairs (A, A*) with equal sign; shuffle the pairs (keep A,A* together)
tot_pair = 0.0
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    W = L.words(p)
    if len(W) < 3: continue
    items = sorted(((t*u-1)/p, (t*u-1), L.legendre(t*u-1, p)) for (t, u, v) in W)
    # group by unordered pair {A, A*}: A* = tv-1 for the same word
    key = {}
    for (t, u, v) in W:
        A, As = t*u-1, t*v-1
        key.setdefault(frozenset((A, As)), []).append(A/p)
    pairs = sorted(((min(x), frozenset(k)) for k, x in key.items()))
    signs = [L.legendre(min(k), p) for _, k in pairs]
    rnd = 0
    for _ in range(200):
        order = signs[:]; random.shuffle(order)
        seq = [s for s in order]
        rnd += sum(1 for i in range(len(seq)-1) if seq[i] != seq[i+1])
    tot_pair += rnd/200
print("pair-respecting random mean (per run, summed over primes):", round(tot_pair,1))
