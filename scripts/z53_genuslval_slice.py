"""Proposition C numerics (Z53_GENUSLVAL.md §3): the u-slice of M_gen in closed form.
For prime p = 1 (4) and squarefree u = 1 (4), the eta-components of the u-slice,
  Sig_eta = sum_{w <= X} G(w) eta(w)/w,  G(w) = 2^{omega(w)} [w odd, (w,u)=1, all l|w split in Q(sqrt(-up))] w/phi(w),
are compared with
  eta = 1 :  L(1,chi_D) H_1(1) [log X + gamma + L'/L(1,chi_D) + H_1'/H_1(1)],  D = -4up,
  eta != 1:  L(1,eta) L(1,eta chi_D) H_eta(1),
with H_eta(1) = prod_l h_l(eta(l)/l):  h_l(Y) = 1 - Y (l | 2up);  1 + 2Y/(l-1) - (l+1)Y^2/(l-1) (chi_D(l) = 1);  1 - Y^2 (chi_D(l) = -1).
Then S_u = (1/(2 phi(u))) sum_eta eps_eta Sig_eta (exact, Lemma 2.3) is compared with the closed form.
Usage: uv run --with cypari2 python scripts/z53_genuslval_slice.py p u1 [u2 ...]   (prints one line per u + per eta)
"""
import sys, subprocess, math, os
import cypari2
pari = cypari2.Pari()
pari.allocatemem(1500 * 10**6, silent=True)
pari.set_real_precision(30)
EXE = '/tmp/z53slice'
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'z53_genuslval_slice.c')
LMAX = 2 * 10**6
PRIMES = [int(x) for x in pari.primes([3, LMAX])]
EG = 0.5772156649015329

def kron(D, n):
    return int(pari.kronecker(D, n))

def fund(D):
    """fundamental discriminant of Q(sqrt D) and the square cofactor"""
    return int(pari.coredisc(D))

def Lval(D, der=0):
    L = pari.lfuncreate(D)
    return float(pari.lfun(L, 1, der))

def jac(a, n):
    return int(pari.kronecker(a, n))

def run(p, u):
    if not os.path.exists(EXE):
        subprocess.check_call(['gcc', '-O2', '-o', EXE, SRC])
    out = subprocess.run([EXE, str(p), str(u)], capture_output=True, text=True, check=True).stdout.split('\n')
    X = int(out[0].split()[1]); direct = float(out[1].split()[1])
    comps = []
    for l in out[2:]:
        if l.strip():
            d, j, e, s = l.split(); comps.append((int(d), int(j), int(e), float(s)))
    D = -4 * u * p
    up_primes = set(int(x) for x in pari.factor(2 * u * p)[0])
    chiD = {l: kron(D, l) for l in PRIMES}
    def hloc(l, Y):
        if l in up_primes or l == 2:
            return 1 - Y
        c = chiD[l] if l in chiD else kron(D, l)
        if c == 1:
            return 1 + 2 * Y / (l - 1) - (l + 1) * Y * Y / (l - 1)
        return 1 - Y * Y
    allp = [2] + PRIMES
    for l in up_primes:
        if l > LMAX: allp.append(l)
    LD = Lval(D); LDp = Lval(D, 1)
    phiu = int(pari.eulerphi(u))
    total_pred = 0.0
    rows = []
    for (d, j, e, s) in comps:
        eta = lambda n: (jac(n, d) if d > 1 else 1) * ((0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)) if j else 1)
        H = 1.0; Hd = 0.0
        for l in allp:
            Y = eta(l) / l
            if Y == 0: continue
            H *= hloc(l, Y)
            if d == 1 and j == 0:  # log-derivative of h_l(l^{-s}) at s=1: -log l * Y h'(Y)/h(Y)
                if l in up_primes or l == 2: dh = -1.0
                elif chiD[l] == 1: dh = 2 / (l - 1) - 2 * (l + 1) * Y / (l - 1)
                else: dh = -2 * Y
                Hd += -math.log(l) * Y * dh / hloc(l, Y)
        if d == 1 and j == 0:
            pred = LD * H * (math.log(X) + EG + LDp / LD + Hd)
        else:
            # eta primitive: discriminant dstar (j=0) or -4 dstar (j=1), dstar = (-1)^((d-1)/2) d
            dstar = d if d % 4 == 1 else -d
            De = dstar if j == 0 else -4 * dstar
            Leta = Lval(De)
            # eta*chi_D on odd n coprime to d: chi_{-4}^{j+1} (n/(u/d)) (n/p) -> primitive disc
            e_ = u // d; ep = e_ * p; epstar = ep if ep % 4 == 1 else -ep
            Dg = -4 * epstar if j == 0 else epstar
            Lg = Lval(Dg)
            for l in set([2] + [int(x) for x in pari.factor(2 * d)[0]]):
                Lg *= (1 - kron(Dg, l) / l)
            pred = Leta * Lg * H
        rows.append((d, j, e, s, pred))
        total_pred += e * pred
    via = sum(e * s for (_, _, e, s, _) in rows) / (2 * phiu)
    S_pred = total_pred / (2 * phiu)
    print(f"p={p} u={u} X={X} S_u direct={direct:.6f} (eta-sum {via:.6f}) closed-form={S_pred:.6f} err={direct-S_pred:+.2e}"
          f"  [L(1,chi_D)={LD:.4f}]")
    for (d, j, e, s, pr) in rows:
        print(f"   eta=(./{d})chi4^{j} eps={e:+d}  Sig={s:.6f}  pred={pr:.6f}  err={s-pr:+.2e}")
    return direct, S_pred

if __name__ == '__main__':
    p = int(sys.argv[1])
    for u in map(int, sys.argv[2:]):
        run(p, u)
