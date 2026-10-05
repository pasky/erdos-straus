"""O40: local (single-modulus) necessary condition for SPW(C, sigma) at N.

Project an SPW measure to Z/e (e > CN): rho >= 0 on Z/e with the window profile mod every d | e, d <= D,
and rho(s) <= 1 - sigma for every class s mod e' with e' | e, e' > CN (incl. points of Z/e).
Maximise sigma.  The SPW optimum is <= min over e of this local value (UPPER bound; IF2 Lemma 9.3 is
the case e = k q).
usage: spw_local_lp.py N C emin emax [top]
"""
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def cnt(b, d, N):
    b %= d
    first = b if b >= 1 else d
    return 0 if first > N else (N - first) // d + 1

def local_sigma(N, C, e):
    D = N // 2
    x = np.arange(e)
    divs = [d for d in range(1, e + 1) if e % d == 0]
    small = [d for d in divs if d <= D]
    small_max = [d for d in small if not any(m % d == 0 and m != d for m in small)]
    big = [d for d in divs if d > C * N]
    er, ec, beq = [], [], []
    r = 0
    for d in small_max:
        er.append(x % d + r); ec.append(x); beq += [cnt(b, d, N) for b in range(d)]; r += d
    Aeq = coo_matrix((np.ones(e * len(small_max)), (np.concatenate(er), np.concatenate(ec))),
                     shape=(r, e + 1)).tocsr()
    ur, uc, uv = [], [], []
    q = 0
    for d in big:
        ur.append(x % d + q); uc.append(x); q += d
    ur = np.concatenate(ur); uc = np.concatenate(uc)
    rows = np.concatenate([ur, np.arange(q)]); cols = np.concatenate([uc, np.full(q, e)])
    vals = np.concatenate([np.ones(len(ur)), np.ones(q)])
    Aub = coo_matrix((vals, (rows, cols)), shape=(q, e + 1)).tocsr()
    c = np.zeros(e + 1); c[-1] = -1
    res = linprog(c, A_ub=Aub, b_ub=np.ones(q), A_eq=Aeq, b_eq=np.array(beq, float),
                  bounds=[(0, None)] * e + [(None, None)], method="highs")
    if res.status != 0:
        return float("nan"), len(small)
    return -res.fun, len(small)

if __name__ == "__main__":
    N = int(sys.argv[1]); C = float(sys.argv[2]); emin, emax = int(sys.argv[3]), int(sys.argv[4])
    top = int(sys.argv[5]) if len(sys.argv) > 5 else 15
    out = []
    for e in range(max(emin, int(C * N) + 1), emax + 1):
        s, ns = local_sigma(N, C, e)
        out.append((s, e, ns))
    out.sort()
    print(f"N={N} C={C} e in [{emin},{emax}]: worst local sigma:")
    for s, e, ns in out[:top]:
        print(f"   e={e}  sigma_loc={s:.4f}  #small divisors={ns}")
