# y3_salie_angle — Type II as a Salié angle at a rational point: roots of quadratic congruences (O211 (b))

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
Salié sums are the one classical exponential sum with an exact closed form that mixes the two worlds through a
square root: for h ≡ 3 (mod 4) prime, S(a,b;h) = Σ_x (x/h) e((ax + bx̄)/h) = i√h (b/h) Σ_{y² ≡ ab} e(2y/h).
(bsB_salie_duality used modulus p; here the modulus is the ES firing prime h, where the root is the datum.)

## Dictionary (PROVED, elementary; checked)
Type II at prime h with (c, d, j): h = 4cdj − 1, h | p + 4c²d. Then y₀ = 2cd is a root of y² ≡ −pd (mod h) and
2y₀ j = h + 1. Hence the **root angle** y₀/h = 1/(2j) + 1/(2jh) and
`S(1, −pd; h) = i√h (−pd/h) · 2cos(2π(1/j + 1/(jh))).`
Conversely, Type II fires at (c, d, h) iff some root y ∈ (0, h) of y² ≡ −pd (mod h) satisfies 2d | y and
2y | h + 1 (then c = y/2d, j = (h+1)/2y). So **Type II at prime h ⟺ a root angle ν/h of ν² ≡ −pd (mod h) sits at
one of the points (1 + 1/h)/(2j)** (with 2d | ν): an exact hit of a rational point of denominator 2j, at
distance 1/(2jh) — Planck scale 1/h, not a fixed-interval event. scripts/y3_salie.py 400: 0 failures (all prime-h
certificates p < 400, Salié closed form verified on 300 of them); odd squares: 0 certificates.

## Literature
Salié (1932); Iwaniec, *Topics in Classical Automorphic Forms*, §4.3; Hooley, Acta Math. 110 (1963) 97–114
(roots of ν² ≡ D mod n equidistribute, D fixed); Duke–Friedlander–Iwaniec, Ann. Math. 141 (1995) 423–441 (prime
moduli, D < 0); Tóth, IMRN 2000 (joint equidistribution). All are equidistribution at fixed scale, averaged over h.

## Barrier screen
* B3/H-A: the event is a hit at scale 1/h of a set of ≍ Σ_j (#d) points; summed over h it is the ET bilinear count;
  DFI-type equidistribution with fixed D = −pd gives the main term but the error at Planck scale is not controlled
  (same as PARITY_FIXED_P's R(p)).
* B2: the target set {(1 + 1/h)/2j} depends on h (moving modulus = moving target).
* B6: the classical theorems average over h for fixed D; we need one h for fixed D — fine — but the hit must be exact.
* T1: at n = m², the dictionary holds verbatim; the failure is in the arithmetic (no root ever hits): consistent.
* Iteration (violate "exact hit"): replace exact hit by |ν/h − 1/(2j)| ≤ δ — that is the ES^{(S)}/near-miss relaxation
  (shots with Q | (r+1)/4 vs rad Q; EXPONENT_CAP), already PROVED for relaxations and not transportable back.

## Assessment
PROVED dictionary, plausibly new in this form (Salié angle ≈ 2π/j), but it is the root-of-quadratic-congruence
version of the box: COLLAPSES to H-A (Planck-scale hit). Mildly useful as a language: ES Type II = "the CM points of
discriminant −4pd reduced mod h hit the cusp-adjacent rational points 1/(2j)" (cf. DFI's Heegner-point proof).
