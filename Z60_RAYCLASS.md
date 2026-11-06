# Z60_RAYCLASS — norm forms in varying imaginary quadratic fields (checkpoint 1; verdict pending)

**ES is OPEN; (MS), U_II, CONV-II are open. Nothing here proves or disproves them.** Internal, unrefereed. Labels:
PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z60_rayclass_*`, data
`data/z60/rayclass/`.

Notation: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} ((★)); R₈ = C-even half; U_II = (★) ∪ (a = 1 line); N_II = full Type II
count; 𝔐 = {1, 121, 169, 289, 361, 529} mod 840. For a squarefree t₀ ≥ 1 and odd n put ω = √(−t₀n),
K_{t₀} = ℚ(√(−t₀n)), β_r := 1 + rω (r ≥ 1), N(β_r) = 1 + t₀nr².

## 0. Falsifier table (MANDATORY; checkpoint version — final version in §9)

The lane's objects are (i) the *class layer* (anything that factors through ideal classes of orders of K_C, incl. class
number size and splitting of small primes), (ii) the *ray layer* (N𝔞 mod 4C), (iii) *single-field families* (one field
ℚ(√−n), growing conductor).

| Screen | class layer (Cl of any order of K_C; h; small-prime splitting) | ray layer N𝔞 ≡ −1 (4C) | single-field family S₁ (Type II d = 1, all in ℚ(√−n)) |
|---|---|---|---|
| F1 odd squares | binds exactly: at n = m², K_C = ℚ(√−C) ⊂ ℚ(ζ_{4C}) and χ_{−4C}(N𝔞) = 1 ≠ χ_{−4C}(−1) (Lemma 2, PROVED). Class *number* is T1-blind: h(−16Cm²) ≫ m/log log m (§5). | = the event (restatement) | S₁(m²) = 0 (Lemma 2 with t₀ = 1, PROVED) |
| F2 R₈ (C even) | blind to C-parity (genus characters at 2 are the only C-parity-sensitive class data; computed in §4) | restatement | n/a (S₁ is a different family) |
| F3 composites | genus condition satisfiable at every non-square n (Lemma 2(b)); does not see primality | restatement | — (to compute) |
| F4 known zeros | (to compute: class-visible certificates at the 14 (★)-zeros) | restatement | S₁ has its **own** zeros: 133 primes ≤ 3·10⁶ (CERTIFIED, §6), growing per decade |

## 1. Precise statements attacked

**(RC)** For every sufficiently large prime p ≡ 1 (mod 24) [(MS): p > 10¹⁷, p mod 840 ∈ 𝔐] there is C ≥ 1 and an ideal
𝔞 of ℤ[√(−Cp)] with 𝔞 | (1 + 2√(−Cp)) and N𝔞 ≡ −1 (mod 4C). (Lemma 1: (RC) ⟺ R(p) ≥ 1.)

Questions (brief): (Q1) exact correspondence incl. orders, non-split primes, units; analogues for the a = 1 line and for
4mn + 1. (Q2) is N𝔞 ≡ −1 (4C) a ray-class / genus condition? (Q3) can the class group of discriminant −16Cp (size ≍ √(Cp),
Siegel, pointwise), or the splitting of small primes in ℚ(√(−Cp)), force such an 𝔞? (Q4) where do T1 and primality enter?

## 2. Why this is not already closed (what is prior, what is open)

Prior and *not* redone: WINDMILL_REDUCTION Prop 10.3 (per field, ideal classes see N𝔞 mod ℓ, ℓ | t, only mod squares) and
Remark 10.4 (ray class groups mod t see the event fully — a restatement), Computation 10.2 (class map injective on the
divisor hypercube); `BRAINSTORM/bsB_rayclass_norm_pullback.md` (every linear character detector of the event is χ∘N —
"pulled back from ℚ"); B2_ACROSS_FIELDS Lemma 4.1 = z31 (shot family ⟺ ideal divisor of 1 + 2k√−p with norm ≡ −1 (4k));
Z58_TERNARY Lemma D(d); Z58_TRYO Lemmas 8.1–8.2 (square levels = forms of disc −4p; C = 1 is a genus condition);
CLASS_FORCING Thm 2.1 (total product on a fixed line). Z53_WILDCARD row 6 leaves open: joint constraints across the
*varying* fields K_C, and class-group structure/size as a *proof input* (not a detector).

This lane: (a) a single dictionary for the three lines as rays β_r in K_{t₀} with moduli t₀r², 4t₀r², 2t₀r (Lemma 1);
(b) T1 as "K ⊂ ℚ(ζ_M)" and its level-wise version at n = s·m² (Lemma 2); (c) **where the class number enters**:
the expected count of a single-field family is proportional to L(1, χ_{−4n}) (∝ h(−4n)/√n), whereas the varying-field
(★) count is L-blind (§5–6); (d) cross-field constraints (§4).

## 3. Lemma 1 (dictionary) and Lemma 2 (T1 in field language) — statements; proofs in §3 of the final memo

**Lemma 1 (PROVED, elementary).** Let n ≥ 1 odd, t₀ ≥ 1 squarefree, r ≥ 1, O = ℤ[ω], ω = √(−t₀n), β_r = 1 + rω.
(i) N(β_r) = 1 + t₀nr² is prime to 2t₀nr only if … [every prime q | N(β_r) satisfies q ∤ t₀nr and (−t₀n/q) = 1, so q
splits in K_{t₀} (q odd if r even); β_r is primitive in O (coefficient of 1 is 1), so exactly one prime of O above q
divides β_r, to the full power]; hence 𝔞 ↦ N𝔞 is a bijection {ideals of O dividing β_r} → {positive divisors of
N(β_r)}, the ideals being invertible (prime to the conductor of O) and the unit group irrelevant (ideals, not elements).
(ii) (★) at level C ⟺ (t₀, r) with C = t₀(r/2)², r even, and some 𝔞 | β_r has N𝔞 ≡ −1 (mod t₀r²).
(iii) a = 1 line at T (CONV2 Lemma 1(ii)) ⟺ T = t₀r² and some *odd* 𝔞 | β_r has N𝔞 ≡ −1 (mod 4t₀r²); for r even it is
implied by (ii) (CONV2 Prop 3.1), so U_II adds exactly the odd r.
(iv) full Type II (CONV2 Lemma 1(v)) at m = t₀(r/2)², r even ⟺ some 𝔞 | β_r with N𝔞 ≡ −1 (mod 2t₀r)
[modulus 4m/r(m) = 4t₀(r/2) = 2t₀r].
So all three lines are divisor events along the *ray* r ↦ β_r of K_{t₀}; they differ only in the modulus
M(t₀, r) ∈ {t₀r², 4t₀r², 2t₀r}.

**Lemma 2 (T1 = the field lies in the cyclotomic field of the modulus; PROVED).** In the setting of Lemma 1 let n = s·m²
with s squarefree. Let M = M(t₀, r) and K = ℚ(√(−t₀s)). (a) If disc(K) | M — equivalently χ_K is a character mod M — then
no divisor of N(β_r) is ≡ −1 (mod M) [all divisors lie in ker χ_K, χ_K(−1) = −1]. (b) For n = p prime the hypothesis of
(a) needs p | M, i.e. p | r; for all levels with M < p² it fails. (c) At n = m² (s = 1) the hypothesis holds at every
level of all three lines (4t₀ | M in each case) — this is T1 for (★), U_II and N_II simultaneously.

## 4–9 (to be written)

## Checkpoint-1 first falsifier (CERTIFIED counts, EVIDENCE correlations; `data/z60/rayclass/`)

`scripts/z60_rayclass_fam.c` (validated against brute force for all n ≡ 1 (4), 5 ≤ n ≤ 401: 0 mismatches) and
`scripts/z60_rayclass_lcorr.py` (L(1, χ_{−4p}) = π·h(−4p)/(2√p), PARI `qfbclassno`).
* **Single-field family S₁ (Type II with d = 1 ⟺ ideal divisor of 1 + 2c√−p with norm ≡ −1 (mod 4c); all in ℚ(√−p))
  has 133 prime zeros p ≡ 1 (4) ≤ 3·10⁶** (22 in 𝔐, largest in 𝔐 2 476 321); per range: 8 (<10³), 14, 23, 54 (10⁵–10⁶),
  34 (10⁶–3·10⁶). The count per decade is still increasing. CERTIFIED (one engine): `s1_prime_zeros_le3e6.txt`.
* On the 7 254 primes p ≡ 1 (4) in [10⁶, 1.2·10⁶] (`counts_1e6_1.2e6.txt`, `lcorr_1e6_1.2e6.txt`): Spearman(·, L(1,χ_{−4p})):
  S₁ +0.875, (★)-hits with u a square +0.729, with C a square +0.723, all of R +0.426, R minus the two square-level
  slices **−0.354**. Log-elasticity w.r.t. L: S₁ 1.23, Sq_C 1.07, Sq_u 1.10, R 0.32. At the 133 S₁-zeros 42 % have
  L < 0.5 (controls 3.8 %). At the 14 (★)-zeros L ∈ [0.52, 1.24], mean 0.84 (≈ π/4 = L(1, χ_{−4}), the pseudo-square
  value), none < 0.5; 𝔊*-zeros mean 0.82; R₈-zeros mean 1.05 (EVIDENCE).
* Reading (Assessment, to be made precise in §5): in a **fixed** field the expected count is ∝ L(1, χ_{−4p}) ∝ h(−4p)/√p
  (quadratic parametrisation: a divisor f is hit by ρ_f(−p) = #{x² ≡ −p mod f} parameters), so the class number enters
  as a *liability*; in the **varying-field** parametrisation (★) each f meets exactly one level C (linear), and the
  leading mean is L-free. The single-field route therefore fails F4 massively (its own zeros), and "Siegel pointwise"
  cannot help (it gives only L ≫_ε p^{−ε}).
