# Hostile review R49 of POINTWISE_OMEGA14.md (task O49, branch side-agent/junta-third)

Reviewer branch: side-agent/review-omega14. Reviewed state: junta-third @ 12df24b.
Status: IN PROGRESS (claims written one at a time).

## Verdicts (summary; filled in as the review proceeds)

| claim | verdict |
|---|---|
| Lemma 1.1 (planting) | SOUND |
| Thm 1.3 (abstract level barrier) | SOUND (minor: integrability/a.e. remark) |
| Setting 2.0 reduction level ≤D ⇒ 𝒱_k | SOUND |
| §1 numerics (2), toy LP | SOUND-AFTER-REPAIRS (wording: grid values, not thresholds) |

## Claim-by-claim

### Lemma 1.1 (planting) — SOUND

Re-derived independently.
* Marginals: for |K|≤k, z⊆K, the σ_J-mass of {x_K=1_z} is [z⊆J]·Σ_{y'⊆J∖K}(−1)^{|z|+|y'|+1};
  J∖K≠∅ since |J|=k+1>|K|, so the alternating sum vanishes. ✔ (K=∅ gives total mass 1.)
* ν(0)=P_0−P_0Σw_J=0 ✔.
* Positivity: negative atoms are exactly 1_y with |y|=j even, 2≤j≤k+1, receiving
  P_0∏_y r·e_{k+1−j}(s)/e_{k+1}(r). Needs e_{k+1−j}(s)≤e_{k+1}(r). The counting identity
  Σ_{|I|=n−1}∏_I s·Σ_{i∉I}s_i = n·e_n(s) and Σ_{i∉I}s_i ≥ Σs−(n−1)r* give
  n e_n(s) ≥ e_{n−1}(s)(R−jr*−(n−1)r*) ≥ e_{n−1}(s)(R−(2k+1)r*) ≥ (k+1)e_{n−1}(s) ≥ n e_{n−1}(s)
  for n≤k+1 (uses j≤k+1, n−1≤k). Chaining n=k+2−j..k+1 gives e_{k+1−j}(s)≤e_{k+1}(s)≤e_{k+1}(r). ✔
* Edge cases: zero p_i (w_J=0 for J∋i, harmless); k=0 (no even |y|≥2 atoms; only needs
  e_1>0); e_{k+1}(r)>0 argued correctly. p_i<1 required for r_i finite — stated.
* From-scratch check `scripts/review_o14_planting.py` (full 2^n enumeration, exact Fractions,
  n≤10, k≤3; random p incl. exact zeros and one large coordinate p_0∈[0.6,0.9]; plus 18
  *equality* instances R=(k+1)+(2k+1)r*): 97+18 instances satisfying (1.1), **0 failures**
  of ν≥0, ν(0)=0, mass 1, all ≤k-marginals. On 294 instances violating (1.1), the same
  construction has a negative atom in 77 — so the check is not vacuous (positivity is the
  only hypothesis-dependent part).
* Minor: the author's own numerics check only ρ on |y|≤k+1 for n≤22; mine enumerate the
  full cube for n≤10 — consistent.

### Theorem 1.3 — SOUND

Re-derived. Given x_s the bits 1[X_b∈Ω_b(x_s)] are independent with marginals p_b(x_s)
(big coordinates independent of each other and of X_s). In the planted case Lemma 1.1 gives
ν_{x_s}; drawing X_b | bit independently from the true conditionals makes (X_b)_{b∈K} have its
true product law for |K|≤k (bits on K: true product law by k-wise agreement; X_K | bits =
product of own conditionals). So E_νφ=Eφ for every φ(x_s,X_K), hence E B=E_νB≤E_νF, and a
planted bit =1 means X_b∈Γ_E for some E∈𝓕 with x_s∈Σ_E, so F=0. ✔
Points the author leaves implicit (MINOR, m1 below): (a) only finitely many b have p_b>0
(primes ≤T), so Lemma 1.1 is applied to a finite bit vector; bits with p_b=0 get w_J=0 and are
never planted; (b) ν≪P with dν/dP≤2 (from e_{k+1−j}(s)≤e_{k+1}(r), the positive extra charge on
1_y is ≤μ(1_y)), so "B≤F P-a.e." suffices and every integrable φ stays ν-integrable;
(c) measurability of x_s↦ν_{x_s} is trivial (Ω_b depends on x_s through a finite modulus).
Note (strength, not a defect): functions in 𝒱_k may read *all* small coordinates; only the
number of big primes in a modulus is constrained. So the barrier holds even for minorants with
arbitrary dependence on primes ≤T^{0.6}.

### Setting 2.0: level ≤D ⇒ 𝒱_k — SOUND

* O9 Thm 1.1's B is a combination of cells 1[n≡b_i (d_i)], Z=Q·max d_i; O13 Thm 5.1's B ≤ F ≤
  1[W>T] on r′H′ with cells of modulus ≤e^{2τ+3𝓛} (O11 Cor 1.2: products A_iA_{i'}u_ju_{j'}).
  On the fibre these are functions of n mod qQ with q≤max d_i, so O14's "level" matches O9's Z. ✔
* A modulus q≤D has fewer than log D/log(T^{0.6}) prime factors >T^{0.6} ⇒ k=⌊log D/(0.6𝓛)⌋. ✔
  Primes >T (incl. ℓ_aux, fixed by the fibre) are harmless: they carry no event (p_b=0).
* Integer vs Haar: ES events force n coprime to M (ℓ|M ⇒ ℓ∤D), B and F are periodic, so the
  integer statement "B(n)≤1[W(n)>T] for n≡r′(Q′), (n,d_i)=1" implies B≤F Haar-a.e. on the
  fibre; and E_{M,D} ⇒ W(n)≤M (D=u²w, A=uvw with u=t, w=κ, D=κt²) so 1[W>T]≤F. ✔

### §1 numerics (2) — SOUND-AFTER-REPAIRS

From-scratch exact-symmetrised LP `scripts/review_o14_toy_lp.py` (S_n-symmetrisation reduces
the k-junta span to polynomials of degree ≤k in |x|; bisection in p). Optimum E B/E F vanishes at
R≈1.11 (n=10,k=1), **1.25** (n=10,k=2), **2.51** (n=12,k=3); also 1.05/1.11/2.28 (n=20,
k=1/2/3), 2.26 (n=30,k=4). The author's "1.1, 1.8, 3.0" are the first grid points (p step 0.05)
with value 0, not thresholds; their grid values agree with mine (e.g. n=10,k=2,R=1.11: 0.258 vs
my 0.277 at R=1.10). Conclusion "(1.1) conservative by a constant factor" stands. Note the
parity effect: even k is barely stronger than k−1 (Bonferroni of odd order).

## Defects

(none yet)
