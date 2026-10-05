"""R38b: sanity of review_o10b_lib against brute-force Walsh transform (uniform bits)
and against G = sum_U lam^|U| ||F^U||^2 consistency."""
import itertools, numpy as np
from review_o10b_lib import level_weights, G_weighted
rng = np.random.default_rng(1)
n = 6
F = rng.integers(0, 2, size=(2,) * n).astype(float)
pts = list(itertools.product([0, 1], repeat=n))
lw_bf = np.zeros(n + 1)
for S in itertools.product([0, 1], repeat=n):
    c = np.mean([F[x] * (-1) ** sum(a * b for a, b in zip(S, x)) for x in pts])
    lw_bf[sum(S)] += c * c
probs = [np.array([.5, .5])] * n
lw = level_weights(F, probs)
print("walsh max diff", np.abs(lw - lw_bf).max())
# q-ary biased: G via levels (uniform lam) vs direct
dims = (3, 2, 4, 3)
F = rng.integers(0, 2, size=dims).astype(float)
probs = [rng.dirichlet(np.ones(q)) for q in dims]
lw = level_weights(F, probs)
lam = 1.37
print("G consistency", abs(sum(lw[d] * lam ** d for d in range(len(lw))) - G_weighted(F, probs, [lam] * 4)))
W = np.einsum('i,j,k,l->ijkl', *probs)
print("Parseval", abs(lw.sum() - (F * F * W).sum()))
# brute-force Efron-Stein: F^{=U} = sum_{S subset U} (-1)^{|U-S|} E[F | x_S]
n = 4
def condexp(S):
    A = F * W
    for v in range(n):
        if v not in S:
            A = A.sum(axis=v, keepdims=True)
    den = np.ones([1]*n)
    for v in S:
        shp=[1]*n; shp[v]=dims[v]; den = den*probs[v].reshape(shp)
    return np.broadcast_to(A/den, dims)
lw_bf = np.zeros(n+1)
for U in itertools.product([0,1], repeat=n):
    Us=[i for i in range(n) if U[i]]
    comp = np.zeros(dims)
    for r in range(len(Us)+1):
        for S in itertools.combinations(Us, r):
            comp += (-1)**(len(Us)-r)*condexp(S)
    lw_bf[len(Us)] += (comp**2*W).sum()
print("biased q-ary ES max diff", np.abs(lw_bf-lw).max())
