"""R188: checks of STERILE_STEER Sec. 4 Lemma 4.2, Sec. 5 Prop 5.1(b) + its Reading, Sec. 6 table.

usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_ss_misc.py
"""
from math import gcd
import sympy
import review_ss_lib as L

# --- Lemma 4.2: pushed-forward Haar measure of ET classes on Lambda_k, brute force over mu mod ord ---
def ordmod(a, m):
    if m == 1:
        return 1
    k, x = 1, a % m
    while x != 1:
        x = x * a % m; k += 1
    return k

cls = list(L.classes_upto(400))
for k in (9, 27, 105):
    for c in (1, -1):
        bad = n0 = 0
        for fam, P, M, rho in cls:
            s = (M & -M).bit_length() - 1; Mo = M >> s
            if gcd(k, Mo) != 1:
                continue
            if (c - rho) % (2 ** s):          # 2-component of nu(mu) is c
                meas = 0.0
            else:
                o = ordmod(2, Mo)
                hit = sum(1 for mu in range(o) if (k * pow(2, mu, Mo) + c - rho) % Mo == 0)
                meas = hit / o
                if hit > 1:
                    bad += 1
            n0 += meas > 0
        print(f'Lemma 4.2 k={k} c={c:+d}: classes M<=400 with positive measure {n0}, with >1 solution g: {bad}')

# --- Sec. 6 table ---
print('Sec.6 C_adm(r,K1) = 0.45 / sum_{K>=K1 odd} 2 r^{2K/5-(K+1)/2}; and 0.225(1-r^-0.2) r^{0.1K1+0.5}')
for K1 in (1, 7):
    row = []
    for r in (17, 101, 1009, 10007, 10 ** 6 + 3, 10 ** 9 + 7):
        S = sum(2 * r ** (2 * K / 5 - (K + 1) / 2) for K in range(K1, 400, 2))
        row.append(f'{0.45 / S:.3g} [{0.225 * (1 - r ** -0.2) * r ** (0.1 * K1 + 0.5):.3g}; r^(.1K1+.1)={r ** (0.1 * K1 + 0.1):.3g}]')
    print(' K1 =', K1, ' | '.join(row))

# --- Sec. 5: V_phi at split primes q | l, l = +-1 mod 5 ---
def leg(a, l):
    return pow(a % l, (l - 1) // 2, l) == 1
tot = chi_m = i1 = 0; S = 0.0; small_ord = 0; frac_ok = True
for l in sympy.primerange(11, 200000):
    if l % 5 not in (1, 4):
        continue
    for ph in sympy.sqrt_mod(5, l, all_roots=True):
        phi = (1 + ph) * pow(2, -1, l) % l           # root of x^2 - x - 1
        assert (phi * phi - phi - 1) % l == 0
        tot += 1
        o = sympy.n_order(phi, l)
        small_ord += o * o < l
        if leg(-phi, l):
            continue
        chi_m += 1
        o2 = sympy.n_order(phi * phi % l, l)
        i = ((l - 1) // 2) // o2
        assert ((l - 1) // 2) % o2 == 0
        i1 += i == 1; S += 1 / i
        if l < 3000:   # shot residues -4 phi^(2k+1) cover exactly 1/i of the non-residues
            shots = {(-4 * pow(phi, 2 * kk + 1, l)) % l for kk in range(l)}
            frac_ok &= all(not leg(s, l) for s in shots) and len(shots) * i == (l - 1) // 2
print(f'V_phi split primes l<2e5: {tot} primes q; chi_(-phi)(q)=-1: {chi_m}; of these i_q=1: {i1} '
      f'({i1 / chi_m:.3f}); sum 1/i_q = {S:.1f}; ord(phi)<sqrt(l): {small_ord}; shot-fraction 1/i_q exact (l<3000): {frac_ok}')
