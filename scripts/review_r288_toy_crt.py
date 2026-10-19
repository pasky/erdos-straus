"""R288 from-scratch toy checks of the finite-probability core of the 3/4 note.

Written independently of scripts/c2_threequarter_check.py (not read).
Checks (toy parameters satisfying the *hypotheses* of Lemma 2.2: z^2 < ell,
4H^2 > K, ell > K > y):
  A  multiplier identity (Lemma 2.1) with exact fractions, random atoms
  B  distinctness mod ell across all multipliers (Lemma 2.2(1)) + negative control
  C  exact enumeration of Z/MZ: H = sum_ell I_ell pointwise, fibre activity
     k | u+cv (Lemma 2.2(3)), conditional independence: P(H=0|c,S)=prod(1-p),
     E((H)_m|c,S) = m! e_m(p) <= mu_c^m  (Thm 5.1 core)
  D  Bonferroni identities (Lemma 7.1)
  E  transfer: sum_{n<=N} S_y Q_r(H) == term-by-term class count, and
     |sum - N E nu| <= T_abs   (Thm 7.2 counting step)
Run: ulimit -v 8000000; timeout 900 PYTHONPATH=scripts uv run --with numpy python scripts/review_r288_toy_crt.py
"""
import itertools
import math
import random
from fractions import Fraction
from math import comb, gcd

import numpy as np

FAIL = []


def check(name, ok, info=""):
    print(("PASS " if ok else "FAIL ") + name + (" :: " + info if info else ""))
    if not ok:
        FAIL.append(name)


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(n + 1) if s[i]]


def lcm(a, b):
    return a // gcd(a, b) * b


# ---------------- A: identity -----------------
def check_identity():
    rng = random.Random(288)
    ps = primes_upto(20000)
    cnt = 0
    tries = 0
    while cnt < 500 and tries < 10 ** 6:
        tries += 1
        k = 4 * rng.randrange(0, 50) + 1
        ell = rng.choice(ps)
        if (k * ell) % 4 != 3:
            continue
        A = (k * ell + 1) // 4
        divs = [d for d in range(1, int(A ** 0.5) + 2) if A % d == 0]
        divs = sorted(set(divs + [A // d for d in divs]))
        u = rng.choice(divs)
        rest = A // u
        dv = [d for d in divs if rest % d == 0]
        v = rng.choice(dv)
        w = rest // v
        M = k * ell
        if gcd(v, M) != 1:
            check("A coprimality uvw vs kl", False, str((k, ell, u, v)))
            return
        a = (-u * pow(v, -1, M)) % M
        for _ in range(3):
            n = a + M * rng.randrange(0, 1000)
            if n == 0:
                continue
            s, rem = divmod(n * v + u, M)
            ok = rem == 0 and s > 0 and Fraction(4, n) == Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w)
            if not ok:
                check("A identity", False, str((k, ell, u, v, w, n)))
                return
            cnt += 1
    check("A identity (exact Fractions)", cnt >= 500, f"{cnt} instances")


# ---------------- atoms in toy -----------------
def toy_atoms(Ks, ells, H, z):
    """atoms (k,ell,u,v): k in Ks (k=1 mod 4), H<u,v<=z, (u,v)=(uv,k)=1, 4uv | k ell+1"""
    out = []
    for ell in ells:
        for k in Ks:
            for u in range(H + 1, z + 1):
                for v in range(H + 1, z + 1):
                    if gcd(u, v) == 1 and gcd(u * v, k) == 1 and (k * ell + 1) % (4 * u * v) == 0:
                        out.append((k, ell, u, v))
    return out


def check_distinct():
    K = 13
    Ks = [k for k in range(1, K + 1) if k % 4 == 1]
    H = 2  # 4H^2 = 16 > 13
    ps = primes_upto(5000)
    bad = 0
    natoms = 0
    neg = 0
    for ell in ps:
        if ell <= K:
            continue
        z = math.isqrt(ell - 1)  # z^2 < ell
        while z * z >= ell:
            z -= 1
        at = toy_atoms(Ks, [ell], H, z)
        natoms += len(at)
        cls = [(-u * pow(v, -1, ell)) % ell for (k, _, u, v) in at]
        bad += len(cls) - len(set(cls))
        # negative control: H=0 (u,v>=1) breaks 4H^2>K
        at2 = toy_atoms(Ks, [ell], 0, z)
        cls2 = [(-u * pow(v, -1, ell)) % ell for (k, _, u, v) in at2]
        neg += len(cls2) - len(set(cls2))
    check("B distinct classes mod ell across multipliers", bad == 0 and natoms > 1000, f"{natoms} atoms, {bad} collisions")
    check("B' negative control (H=0) has collisions", neg > 0, f"{neg} collisions")


# ---------------- C: exact enumeration -----------------
def check_enumeration():
    K = 9
    Ks = [1, 5, 9]
    LK = 45
    H = 2
    y = 3
    Py = 6
    z = 7  # z^2=49 < ell
    cand = [p for p in primes_upto(200) if p > 49]
    scored = sorted(cand, key=lambda p: -len(toy_atoms(Ks, [p], H, z)))
    ells = sorted(scored[:3])
    atoms = toy_atoms(Ks, ells, H, z)
    M = lcm(LK, Py)
    for l in ells:
        M *= l
    print(f"   toy: ells={ells}, |A|={len(atoms)}, M={M}")
    n = np.arange(M, dtype=np.int64)
    Htot = np.zeros(M, dtype=np.int32)
    Iell = {l: np.zeros(M, dtype=np.int8) for l in ells}
    for (k, l, u, v) in atoms:
        q = k * l
        a = (-u * pow(v, -1, q)) % q
        hit = (n % q) == a
        Htot += hit
        Iell[l] += hit.astype(np.int8)
    ok_one = all(int(Iell[l].max()) <= 1 for l in ells)
    check("C at most one atom per ell contains n", ok_one)
    S = (np.gcd(n, Py) == 1)
    c = n % LK
    maxdev = 0.0
    mom_ok = True
    act_ok = True
    nfib = 0
    for cc in range(LK):
        mask = S & (c == cc)
        cnt = int(mask.sum())
        if cnt == 0:
            continue
        nfib += 1
        # fibre activity
        p = {}
        for l in ells:
            f = 0
            for (k, l2, u, v) in atoms:
                if l2 != l:
                    continue
                active = (u + cc * v) % k == 0
                # does the class meet the fibre (within S)? brute force
                q = k * l
                a = (-u * pow(v, -1, q)) % q
                meets = bool(((n[mask] % q) == a).any())
                if active != meets:
                    act_ok = False
                f += active
            p[l] = f / l
        Hf = Htot[mask]
        p0 = float((Hf == 0).mean())
        pred = 1.0
        for l in ells:
            pred *= 1 - p[l]
        maxdev = max(maxdev, abs(p0 - pred))
        mu = sum(p.values())
        pv = [p[l] for l in ells]
        for m in range(1, 4):
            fm = np.ones_like(Hf, dtype=np.float64)
            for i in range(m):
                fm *= (Hf - i)
            emp = float(fm.mean())
            em = sum(math.prod(cmb) for cmb in itertools.combinations(pv, m)) * math.factorial(m)
            if abs(emp - em) > 1e-9 or em > mu ** m + 1e-12:
                mom_ok = False
    check("C fibre activity <=> k | u+cv", act_ok, f"{nfib} fibres in S")
    check("C P(H=0|c,S) = prod(1-f_c/ell)", maxdev < 1e-12, f"maxdev {maxdev:.1e}")
    check("C E((H)_m|c,S) = m! e_m(p) <= mu_c^m, m<=3", mom_ok)
    return dict(atoms=atoms, M=M, Py=Py, y=y, Htot=Htot, S=S)


# ---------------- D: Bonferroni -----------------
def check_bonferroni():
    ok = True
    for r in range(0, 31, 2):
        for h in range(0, 120):
            Q = sum((-1) ** j * comb(h, j) for j in range(r + 1))
            exp_ = 1 if h == 0 else comb(h - 1, r)
            if Q != exp_ or not ((1 if h == 0 else 0) <= Q <= (1 if h == 0 else 0) + comb(h, r + 1)):
                ok = False
    check("D Bonferroni Q_r(h)=C(h-1,r), 1_{h=0}<=Q_r<=1_{h=0}+C(h,r+1)", ok)


# ---------------- E: transfer -----------------
def check_transfer(ctx):
    atoms = ctx["atoms"]
    y, Py = ctx["y"], ctx["Py"]
    sp = [p for p in primes_upto(y)]
    classes = []
    for (k, l, u, v) in atoms:
        q = k * l
        classes.append((q, (-u * pow(v, -1, q)) % q))
    for r in (0, 2):
        # terms: (coef, q, a) or None for empty
        terms = []
        for dsub in range(1 << len(sp)):
            d = 1
            mu = 1
            for i, p in enumerate(sp):
                if dsub >> i & 1:
                    d *= p
                    mu = -mu
            for j in range(r + 1):
                for B in itertools.combinations(range(len(classes)), j):
                    q, a = d, 0
                    empty = False
                    for b in B:
                        q2, a2 = classes[b]
                        g = gcd(q, q2)
                        if (a - a2) % g:
                            empty = True
                            break
                        # CRT combine
                        L = q // g * q2
                        t = ((a2 - a) // g * pow(q // g, -1, q2 // g)) % (q2 // g)
                        a = (a + q * t) % L
                        q = L
                    terms.append((mu * (-1) ** j, None if empty else (q, a)))
        Tabs = len(terms)
        Enu = sum(Fraction(cf, qa[0]) for cf, qa in terms if qa)
        # exact mean by enumeration of Z/MZ
        Htot, S = ctx["Htot"], ctx["S"]
        Q = np.zeros_like(Htot, dtype=np.int64)
        for j in range(r + 1):
            Q += (-1) ** j * np.array([comb(int(h), j) for h in range(int(Htot.max()) + 1)], dtype=np.int64)[Htot]
        nu = Q * S
        Enu_enum = Fraction(int(nu.sum()), ctx["M"])
        check(f"E r={r} E nu (term sum) == enumeration over Z/MZ", Enu == Enu_enum, f"Enu={float(Enu):.5f}, T_abs={Tabs}")
        for N in (10 ** 4, 123457, 2 * 10 ** 5 + 3):
            nn = np.arange(1, N + 1, dtype=np.int64)
            Hn = np.zeros(N, dtype=np.int64)
            for (q, a) in classes:
                Hn += (nn % q) == a
            Qn = np.zeros(N, dtype=np.int64)
            for j in range(r + 1):
                Qn += (-1) ** j * np.array([comb(int(h), j) for h in range(int(Hn.max()) + 1)], dtype=np.int64)[Hn]
            direct = int((Qn * (np.gcd(nn, Py) == 1)).sum())
            via = 0
            for cf, qa in terms:
                if qa:
                    q, a = qa
                    # count 1<=n<=N with n=a mod q
                    a0 = a if a > 0 else q
                    via += cf * (0 if a0 > N else (N - a0) // q + 1)
            err = abs(direct - N * Enu)
            check(f"E r={r} N={N} direct==term count, |sum-N Enu|<=T_abs", direct == via and err <= Tabs, f"direct={direct}, err={float(err):.2f}")


if __name__ == "__main__":
    check_identity()
    check_distinct()
    ctx = check_enumeration()
    check_bonferroni()
    check_transfer(ctx)
    print("ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
