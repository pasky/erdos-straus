r"""s4_selling: path forms Q_w = v x^2 + t y^2 + u z^2 - 2xy - 2yz as Selling-reduced (obtuse superbase) forms.
(1) identity: Q_w = sum_{i<j} p_ij (x_i - x_j)^2 with x_0 = 0 and conorms
    p12 = p23 = 1, p13 = 0, p01 = v-1, p02 = t-2, p03 = u-1  (checked symbolically on random words);
(2) invariance: Selling-reduce random GL3(Z)-conjugates of Q_w and compare the conorm multiset (incl. the 7th = 0).
usage: s4_selling.py trials"""
import sys, random

def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def transpose(A): return [list(r) for r in zip(*A)]

def rand_unimodular(rng, steps=12):
    U = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for _ in range(steps):
        i, j = rng.sample(range(3), 2); c = rng.choice([-2, -1, 1, 2])
        E = [[int(a == b) for b in range(3)] for a in range(3)]; E[i][j] = c
        U = mat_mul(U, E)
    return U

def selling(G):
    """G Gram of basis e1,e2,e3; superbase e0=-(e1+e2+e3). Return sorted conorms (6 values + the 7th, 0)."""
    # vectors as coefficient rows in the e-basis; inner product via G
    B = [[-1, -1, -1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    ip = lambda a, b: sum(a[i] * G[i][j] * b[j] for i in range(3) for j in range(3))
    for _ in range(10000):
        done = True
        for i in range(4):
            for j in range(i + 1, 4):
                if ip(B[i], B[j]) > 0:
                    bi = B[i]
                    B = [[-x for x in bi] if k == i else (B[k] if k == j else [B[k][r] + bi[r] for r in range(3)]) for k in range(4)]
                    done = False; break
            if not done: break
        if done: break
    return sorted([-ip(B[i], B[j]) for i in range(4) for j in range(i + 1, 4)] + [0])

rng = random.Random(1); T = int(sys.argv[1]); bad_id = bad_inv = 0
for _ in range(T):
    t = rng.randint(2, 40); u = rng.randint(1, 40); v = rng.randint(1, 40)
    if t * u * v - u - v <= 0: continue
    G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
    for _k in range(5):
        x = [0] + [rng.randint(-9, 9) for _ in range(3)]
        p = {(1, 2): 1, (2, 3): 1, (1, 3): 0, (0, 1): v - 1, (0, 2): t - 2, (0, 3): u - 1}
        lhs = sum(x[a] * G[a - 1][b - 1] * x[b] for a in range(1, 4) for b in range(1, 4))
        rhs = sum(c * (x[i] - x[j]) ** 2 for (i, j), c in p.items())
        bad_id += lhs != rhs
    ref = sorted([1, 1, 0, v - 1, t - 2, u - 1, 0])
    U = rand_unimodular(rng)
    G2 = mat_mul(mat_mul(transpose(U), G), U)
    bad_inv += selling(G2) != ref
print(f"trials {T}: identity failures {bad_id}, conorm-multiset (Selling) mismatches {bad_inv}")
