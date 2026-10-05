"""R48a: from-scratch simulation of the O13 square-class quarantine process (Lemma 3.2).

Events are general: F = {l: (v_l, t_l mod l^v_l)}; ES atoms give t = -4D mod l^v.
State: for each odd prime l: a_l and c_l (class mod l^a_l, a unit square).
Fibre probability of F: prod_l  [a=0: 1/phi(l^v)] [1<=a<v: 1[c=t mod l^a] l^-(v-a)]
                                 [a>=v: 1[c = t mod l^v]].
Checks:
 (A) one-step exact: for random reachable states and EVERY admissible step (l<=Y, a_l<f_l),
     E[sum_F p(F) 2^{u(F)} phi(F)] <= current, per event (stronger than for sums).
 (D) one-step exact for the pair potential Pi = p(F)p(F') R 2^{u(F)+u(F')} with
     agreement-depth rho; plus p p' <= Pi*2^{-u-u'} at every visited state.
 (MC) full process, Monte Carlo: E[log Q_end], E[residual mass], E[w_l(end)^2] for l>Y,
      against the Lemma 3.2 (b),(c),(d) right-hand sides computed directly.
"""
import math, random, sys
from functools import lru_cache

import os
BUGGY = os.environ.get('O13A_BUGGY') == '1'  # variant: rho at depth min(v,v') (also a supermartingale)
NORHO = os.environ.get('O13A_NORHO') == '1'  # sanity: R=1 must FAIL (D)
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 3)


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds


def phi_pp(l, v):
    return 1 if v == 0 else (l - 1) * l ** (v - 1)


def es_events(T):
    ev = []
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fM = factor(M)
        for D in divisors_from({p: 2 * e for p, e in factor(A).items()}):
            ev.append({l: (v, (-4 * D) % l**v) for l, v in fM.items()})
    return ev


def prob(F, st):
    p = 1.0
    for l, (v, t) in F.items():
        a, c = st.get(l, (0, 0))
        if a == 0:
            p /= phi_pp(l, v)
        elif a < v:
            if (t - c) % l**a:
                return 0.0
            p /= l ** (v - a)
        else:
            if (t - c) % l**v:
                return 0.0
    return p


def u(F, st, Y):
    return sum(1 for l in F if l <= Y and st.get(l, (0, 0))[0] == 0)


def supp(F, st):
    return sum(1 for l, (v, t) in F.items() if v > st.get(l, (0, 0))[0])


def children(st, l):
    a, c = st.get(l, (0, 0))
    out = []
    if a == 0:
        sq = sorted({x * x % l for x in range(1, l)})
        for s in sq:
            n = dict(st); n[l] = (1, s); out.append(n)
    else:
        m = l**a
        for k in range(l):
            n = dict(st); n[l] = (a + 1, c + k * m); out.append(n)
    return out


def agree_depth(l, v1, t1, v2, t2):
    j = 0
    while j < min(v1, v2) and (t1 - t2) % l ** (j + 1) == 0:
        j += 1
    return j


def R(F, G, st):
    r = 1
    if NORHO:
        return 1
    for l in F:
        if l in G:
            j = agree_depth(l, *F[l], *G[l])
            if BUGGY:
                j = min(F[l][0], G[l][0])
            a, c = st.get(l, (0, 0))
            if a < j:
                r *= phi_pp(l, j) if a == 0 else l ** (j - a)
    return r


def Pi(F, G, st, Y):
    return prob(F, st) * prob(G, st) * R(F, G, st) * 2 ** (u(F, st, Y) + u(G, st, Y))


def w_l(evs, st, l, beta):
    tot = 0.0
    for F in evs:
        if l in F and F[l][0] > st.get(l, (0, 0))[0]:
            tot += beta ** supp(F, st) * prob(F, st)
    return tot


def remove(F, l):
    return {k: x for k, x in F.items() if k != l}


def main():
    T = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    Y = int(sys.argv[3]) if len(sys.argv) > 3 else 13
    beta = float(sys.argv[4]) if len(sys.argv) > 4 else 1.3
    eta_fac = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
    L = math.log(T)
    evs = es_events(T)
    smallp = [l for l in range(3, Y + 1) if all(l % q for q in range(2, l))]
    f = {l: int(L / math.log(l)) for l in smallp}
    eta = eta_fac * 0.75 * math.log(beta)
    print(f"T={T} Y={Y} beta={beta} eta={eta:.4f} #events={len(evs)}")
    # random pairs for (D), include l-removed variants and same-l pairs
    pairs = []
    for _ in range(400):
        F, G = random.choice(evs), random.choice(evs)
        if random.random() < 0.3:
            G = dict(F); G = {l: (v, (t + (l ** max(0, v - 1)) * random.randint(0, l - 1)) % l**v) for l, (v, t) in G.items()}
        pairs.append((F, G))
    # random walks over reachable states with random admissible steps
    worstA = worstD = worstDom = 0.0
    nA = nD = 0
    for walk in range(60):
        st = {}
        for depth in range(random.randint(0, 12)):
            adm = [l for l in smallp if st.get(l, (0, 0))[0] < f[l]]
            if not adm:
                break
            st = random.choice(children(st, random.choice(adm)))
        adm = [l for l in smallp if st.get(l, (0, 0))[0] < f[l]]
        for l in adm:
            ch = children(st, l)
            for F in random.sample(evs, min(300, len(evs))):
                cur = prob(F, st) * 2 ** u(F, st, Y)
                if cur == 0:
                    continue
                nxt = sum(prob(F, c) * 2 ** u(F, c, Y) for c in ch) / len(ch)
                worstA = max(worstA, nxt / cur); nA += 1
            for F, G in pairs:
                cur = Pi(F, G, st, Y)
                dom = prob(F, st) * prob(G, st) * 2 ** (u(F, st, Y) + u(G, st, Y))
                if dom > 0:
                    worstDom = max(worstDom, dom / cur)
                if cur == 0:
                    continue
                nxt = sum(Pi(F, G, c, Y) for c in ch) / len(ch)
                worstD = max(worstD, nxt / cur); nD += 1
    print(f"(A) one-step E[p 2^u]/(p 2^u): max {worstA:.6f} over {nA} (claim <=1)")
    print(f"(D) one-step E[Pi]/Pi: max {worstD:.6f} over {nD} (claim <=1); max pp'/Pi {worstDom:.4f} (claim <=1)")
    # Monte Carlo of the full process
    runs = int(sys.argv[6]) if len(sys.argv) > 6 else 200
    late = [l for l in range(Y + 1, 60) if all(l % q for q in range(2, l))][:4]
    sumlogQ = sumres = 0.0
    sumw2 = {l: 0.0 for l in late}
    nsteps = 0
    for run in range(runs):
        st = {}
        while True:
            heavy = [l for l in smallp if st.get(l, (0, 0))[0] < f[l] and w_l(evs, st, l, beta) > eta]
            if not heavy:
                break
            st = random.choice(children(st, heavy[0])); nsteps += 1
        sumlogQ += math.log(8) + sum(a * math.log(l) for l, (a, c) in st.items())
        sumres += sum(beta ** supp(F, st) * prob(F, st) for F in evs)
        for l in late:
            sumw2[l] += w_l(evs, st, l, beta) ** 2
    # bounds
    def omega(F):
        return len(F)
    def omY(F):
        return sum(1 for l in F if l <= Y)
    def PH(F):
        return 1.0 / math.prod(phi_pp(l, v) for l, (v, t) in F.items())
    def logMY(F):
        return sum(v * math.log(l) for l, (v, t) in F.items() if l <= Y)
    bb = math.log(8) + sum(PH(F) * 2 ** omY(F) * beta ** omega(F) * logMY(F) for F in evs) / eta
    bc = sum(PH(F) * 2 ** omY(F) * beta ** omega(F) for F in evs)
    print(f"MC runs={runs}, mean steps={nsteps/runs:.2f}")
    print(f"(b) E[log Q_end]={sumlogQ/runs:.4f}  bound={bb:.4f}")
    print(f"(c) E[res mass]={sumres/runs:.4f}  bound S_H^beta={bc:.4f}")
    for l in late:
        Ev = [F for F in evs if l in F]
        B2 = 0.0
        for F in Ev:
            for G in Ev:
                g = 1
                for q in F:
                    if q in G and q != l:
                        g *= q ** min(F[q][0], G[q][0])
                B2 += beta ** (omega(F) + omega(G)) * 2 ** (omY(F) + omY(G)) * PH(F) * PH(G) * math.prod(
                    phi_pp(q, e) for q, e in factor(g).items())
        print(f"(d) l={l}: E[w^2]={sumw2[l]/runs:.6f}  B2={B2:.6f}")


if __name__ == "__main__":
    main()
