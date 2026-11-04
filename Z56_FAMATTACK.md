# Z56_FAMATTACK — joint attack on positivity of the full (★) count R(p)

Status: z56 lane FAMATTACK (brief `z52bbriefs/z53_depth.md` + `z56_lanes.md` §3). Internal; internally reviewed only
(§8). **ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z56_famattack_*`, data
`data/z56/famattack/` (8 MB).

## 0. Summary

**Verdict: narrowed** (with a modest main-term strengthening). The target — R(p) ≥ 1 for every large prime p ≡ 1 (4) —
is **not** proved. The lane combined the tools jointly and asked specifically whether the *union over windows* gives an
inequality that no single window gives. No such inequality was found. The exact cross-window links analysed here are
positive, size-only, congruence-level or quadratic, and the measured window dependence is net positive.

* **Prop T (PROVED, unconditional, effective; §2.1).** Tiling Thm U over finitely many thin u-strips gives
  **M_gen(p) ≥ (64/(45π⁴) − ε)·log²p ≈ 0.01460·log²p** for p ≥ p₀(ε), i.e. 2.13 × Thm U's 2/(3π⁴). The same tiling of
  GENUSX Thm X windows gives an exact-class density main term **≥ (28/(75π⁴) − ε)log²p ≈ 0.00383 log²p** (1.97 × c_X)
  with T_u = O(p^{−δ}log p) on every tile (Prop T′). These proved lower-bound coefficients are 9.6 % and 2.5 % of the
  full mean coefficient 3/(2π²) ≈ 0.152.
* **Thm J (PROVED reduction; §2.2).** Over a finite tiling 𝒯: R(p) ≥ Σ_t M^cls_t + Σ_t E_t, with E_t = T_w + T_uw the
  exact-divisor layers. So the joint attack reduces (FA ⇐) to the **tiled exact-layer bound** (CU_𝒯):
  Σ_t E_t(p) ≥ −(1 − ε)Σ_t M^cls_t(p). Combining these tools moves only the main term; the residual is the union of the
  same exact layers that were open window by window.
* **Lemma L (PROVED; §2.3): exact cross-window links** for windows in the shift variable u (each window's count is a
  function of the factorisations of its own integers n + u): (a) the switch makes the hit matrix symmetric
  (H_jk = H_kj), a positive link; (b) privacy: a prime ℓ ∤ u − u′ divides at most one of n + u, n + u′; (c) for p ≡ 1 (4),
  p ∤ u, a parity law places an odd number of prime factors of the *odd part* of p + u in the coset {χ_{−4u} = −1} when
  (u/p)(2/p)^{v₂(p+u)} = −1. Small-prime congruences (B1) are the remaining obvious link. Whether other exact links exist
  is not decided here (Assessment: apart from the switch (a), which maps a hit at u to a hit at u′ = B, none of the
  analysed links forces a first hit when all windows are empty).
* **Prop V (PROVED, elementary; §2.4).** A pointwise variance bound across windows that excludes R(p) = 0 implies a
  weighted first-moment lower bound for R(p); a dual-large-sieve variance bound over p gives one prime only the whole
  sum. So a variance criterion is at least as strong as a weighted positivity statement (no claim that it is harder to
  prove).
* **Falsifier F1 (EVIDENCE, pre-registered; §3.2).** All primes p ≡ 1 (4) in [10⁸, 1.04·10⁸] (108 397) and
  [10⁹, 1.002·10⁹] (48 139), hold-out [1.199·10⁹, 1.2·10⁹] (23 928); exact window counts.
  * **Registered outcome: leads triggered, kill condition not met.** Pairs below −4 nominal s.e. within p mod 840:
    u(0,1), u(0,2), u(0,4), C(3,4) at 10⁸; u(0,1), C(3,4) at 10⁹ and in the hold-out.
  * Exploratory follow-up (Assessment): C(3,4) are both congruence-determined windows (4uB ≤ p^{0.4}); u(0,1) shrinks to
    −0.024 under 1330 residue columns, is not explained by the tested linear medium-prime proxies, and couples only the
    small-u lines to the next window. Magnitudes: u-window lead −0.02…−0.08; C(3,4) −0.15 (10⁸, within 840), −0.157 /
    −0.125 with L-proxy controls (10⁸ / 10⁹). Positive pair correlations reach +0.48 (C-windows, disjoint integers
    4Cp + 1; +0.45 after truncated-Euler-product L-value proxies).
  * Multivariate: joint emptiness of k randomly chosen grid windows is *more* frequent than within-mod-840 conditional
    independence predicts, increasingly with k (pooled ratios 1.01 at k = 2 up to 1.6–3.4 at k = 8, all three datasets).
  * Reading: some negative pairs, but net positive residual covariance and excess pooled joint emptiness. EVIDENCE only;
    it says nothing about a pointwise theorem, and it measures full-count windows, not the signed layers E_t.
* **Near-squares (EVIDENCE; §3.4).** At 965 primes p = m² + k ∈ [10⁹, 1.2·10⁹], pooled per-window counts are 0.79–0.95 of
  generic class-matched means (two baselines), total 0.84–0.86: a deficit spread over all windows (not every window for
  every k).
* **Calibration (CERTIFIED counts; §3.5).** Among n ≡ 1 (4), n ≤ 7 999 801: R(n) = 0 at exactly 13 primes (the known
  ones), all 1 413 odd squares, and **285 non-square composites** (60, 95, 97 in the decades from 10⁴). At these R*(n) = 0
  while M_gen(n) reaches 24.3 (n = 810 001 = 241·3361); at the prime zero 8 813 281, M_gen = 29.1. A transfer
  "X ≥ −(1 − ε)M_gen" asserted for all non-square n ≡ 1 (4) is false at these n; an eventual statement is not excluded.
* **Model scale (Assessment; §3.6).** hits ~ Poisson(c log²p): the full count (c ≈ 0.081 measured) predicts ≈ 12.3 zero
  primes ≥ 5 in total (observed 14); a family at c = c_tile/2 = 0.0073 predicts ≈ 10¹⁴, with expected-tail-count
  crossover near 10⁵⁷.

**Where it stops (§4).** Every joint inequality found reduces to (CU_𝒯), a pointwise lower-tail statement for a sum of
exact-divisor layers with total main term ≍ log²p — B2 in tied form. Assessment: the union would help only if the exact
layers of different windows could not be small simultaneously at one p; none of the links analysed here produces that,
and the data show positive dependence. This is not a necessity theorem.

## 1. Statements attacked

R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (FRONTIER §2.1); R is even for odd n (u ≠ B) and R(n) = 2·#{u < B}.

* **(FA)** ∃p₀: R(p) ≥ 1 for all primes p ≡ 1 (4), p > p₀. (CERTIFIED: R(p) = 0 at exactly 14 primes p ≡ 1 (4) below
  10¹⁰; largest 8 813 281.) Not proved.
* **(FA-W), joint-window form.** Partition the solution set into windows 𝒲_j (size conditions on u, B, C), R = Σ_j R_j,
  main terms M_j, remainders X_j = R_j − M_j. FA ⇐ Σ_j X_j ≥ −(1 − ε)Σ_j M_j with Σ_j M_j → ∞. Question (brief): does the
  joint structure give this when no single window does?
* **(CU_𝒯)** (defined in §2.2): Σ_{t∈𝒯} E_t(p) ≥ −(1 − ε)Σ_t M^cls_t(p) for p > p₀. CONJECTURE-strength, not claimed.
  It is the tiled form of CROSSU's (CU).

Why not already closed: Thm U / Thm X / CROSSF / CROSSO / CROSSU each treat one window family. No previous memo treats
the union, the cross-window dependence, or tiles the Burgess windows (GENUSLVAL Remark (1) mentions only a single-window
large-sieve variant). Closed items used, not redone: one-step hyperbola, Fejér/E–T, Cauchy–Schwarz in the function
variable, low-conductor universality, Fourier minorants with proper-subgroup support (CROSSF §2.4(a)).

## 2. Proved

### 2.1 Proposition T (tiling the Thm U windows; PROVED, unconditional, effective)

**Statement.** For every ε > 0 there is an effective p₀(ε) such that every prime p ≡ 1 (4), p ≥ p₀(ε), satisfies
  M_gen(p) ≥ (64/(45π⁴) − ε)(log p)² ≈ 0.014601·(log p)².
More generally, for τ = τ_r = (r+1)/(4r) (r ≥ 3 fixed) the constant is (8/π⁴)·|Ω_τ| − ε with
  Ω_τ := {(a, b) : τ²/(1 − τ²) < a < (1 − τ)/(1 + τ), τ(1 + a) < b < 1 − a}, |Ω_{1/4}| = 8/45.

**Proof.** Inputs: `Z53_GENUSLVAL.md` Lemma 2.3, Props 2.4, 2.5 and the argument of §2.7, used *verbatim per window*.
(i) *Per-window bound.* For fixed exponents (α₀, α₁, β, γ) satisfying (C1) γ < 1 − α₁, (C2) β > τ(1 + α₁) + 4ε′,
(C3) α₀ > τ²(1 + α₁) + 3ε′ (τ = τ_r + rε′), GENUSLVAL §2.7 proves
  Σ_{u∈𝒰}Σ_{w∈𝒮_u∩(Y,X]} 𝔤(u, w) ≥ (c(α₀, α₁, β, γ) − o(1))(log p)²,  c = (8/π⁴)(γ − β)(α₁ − α₀),
where 𝔤(u, w) ≥ 0 is the total genus weight of the two pairs (u, 2w), (2w, u) ∈ 𝒫(p); this is exactly the displayed
chain "M_gen(p) ≥ Σ_{u∈𝒰}Σ_w (genus weight …) ≥ (γ − β)log p·Σ_u H_uL/φ(u) − O(p^{−δ}log²p) ≥ …" with its first
inequality removed. The o(1) is effective and depends only on (r, ε′, α₀, α₁, β, γ).
(ii) *Tiling.* Fix η > 0 and a partition τ²/(1 − τ²) + η = a₀ < a₁ < … < a_K = (1 − τ)/(1 + τ) − η of mesh h. For strip
i put (α₀, α₁) = (a_{i−1}, a_i), β_i = τ(1 + a_i) + 5ε′, γ_i = 1 − a_i − ε′. (C1), (C2) hold by construction; (C3)
needs a_{i−1}(1 − τ²) > τ² + τ²h + 3ε′, which holds for all i once η(1 − τ²) > τ²h + 3ε′; β_i < γ_i needs
a_i < (1 − τ − 6ε′)/(1 + τ), true for ε′ small given the margin η.
(iii) *Disjointness.* Strips have disjoint u-ranges (U₀ < u ≤ U₁ with U = p^{a}), and the pairs (u, 2w) (odd first
entry) and (2w, u) (even first entry) of different (u, w) are distinct. All terms of M_gen are ≥ 0 (GENUSLVAL §1). So
  M_gen(p) ≥ Σ_{i=1}^K Σ_{u∈𝒰_i}Σ_w 𝔤(u, w) ≥ Σ_i (c_i − o(1))(log p)²,
a finite sum (K fixed before p → ∞), hence ≥ (Σ_i c_i − o(1))(log p)² with effective o(1).
(iv) *Limit.* Σ_i c_i = (8/π⁴)Σ_i (γ_i − β_i)(a_i − a_{i−1}) is a Riemann sum (right endpoints) of
(8/π⁴)∫(1 − a − τ(1 + a))da over [a₀, a_K], up to O(ε′); letting h, η, ε′ → 0 and r → ∞ (τ → 1/4) it tends to
(8/π⁴)|Ω_{1/4}|, and |Ω_{1/4}| = ∫_{1/15}^{3/5}(3/4 − 5a/4)da = [3a/4 − 5a²/8]_{1/15}^{3/5} = 9/40 − 17/360 = 8/45.
All choices are made before p → ∞, so for each ε one finite tiling suffices. ∎

*Remarks.* (1) Thm U's single rectangle has (γ − β)(α₁ − α₀) ≤ 1/12; the strip union has area 8/45 ≈ 0.178, ratio 2.13.
(2) GENUSLVAL Remark (1)'s Heath-Brown-large-sieve variant (α₀ → 0, Assessment there) would tile to area 9/40,
c ≈ 0.01848 (Assessment; not proved here). (3) The proved lower-bound coefficient is 0.01460/(3/(2π²)) = 9.6 % of the
full mean coefficient. This is a lower bound, not a ceiling: the proof discards the square terms of Prop 2.5, the Euler
factors ∏(1 − ℓ^{−2})^{−1}, and the other parity/squarefree subfamilies. For orientation only (Assessment): the full
pair density on the ordered-pair region Ω ∪ Ω^T of this window construction is (3/π²)|Ω ∪ Ω^T| ≈ 0.0979, i.e. 64 % of the
mean (`data/z56/famattack/tiling.txt`, grid estimate); the rest of the mean lies outside the windows of this
construction (w-windows below (4up)^{1/4}, or u ≥ p^{3/5}). No barrier for other Burgess-based arrangements is claimed. (4) T1 audit: the
square-sensitive step is GENUSLVAL Prop 2.4(2) in each strip; at n = m² every strip's S_{η_{u,1}} = S_1 cancels exactly
(GENUSLVAL §2.8), consistent with M_gen(m²) = 0.

### 2.2 Proposition T′ and Theorem J (the joint reduction; PROVED)

**Prop T′.** Same construction with GENUSX Thm X's conditions (C1) γ < 1 − α₁, (C2*) β > 2α₁ + τ + 4ε′, (C4) α₁ < 1/5
plus (C3): the strip region is Ω_X = {1/15 < a < 1/5, 2a + 1/4 < b < 1 − a} (τ → 1/4), |Ω_X| = [3a/4 − 3a²/2]_{1/15}^{1/5}
= 9/100 − 13/300 = 7/150. For every ε > 0 there is a finite tiling 𝒯 with, for p ≥ p₀(ε),
  Σ_{t∈𝒯} M^cls_t(p) ≥ (28/(75π⁴) − ε)(log p)² ≈ 0.003833 (log p)²,  Σ_t |T_{u,t}(p)| = O(p^{−δ}log p).
(GENUSX's single-window optimum is c_X = (8/π⁴)·121/5120 ≈ 0.001941; 7/150 ÷ 121/5120 = 1.97.)
*Proof.* As Prop T, with Thm X applied per strip (finitely many; each gives T_u = O(p^{−δ_t}log p), take δ = min δ_t;
M^cls_t = M_t + T_{u,t} and M_t ≥ (c_t − o(1))log²p by (i) above). M^cls ≥ 0 termwise (A ∈ {0,1}, B^gen ≥ 0). ∎

**Theorem J (joint reduction).** For a finite tiling 𝒯 of Prop T′, and every prime p ≥ p₀,
  R(p) ≥ Σ_{t∈𝒯} R_t(p) = Σ_t M^cls_t(p) + Σ_t E_t(p),  E_t := R_t − M^cls_t = T_{w,t} + T_{uw,t},
with Σ_t M^cls_t ≥ (c_𝒯 − o(1))log²p, where c_𝒯 = Σ_t c_t ≥ 28/(75π⁴) − η for a tiling chosen with loss η. Hence
(CU_𝒯) with parameter ε ⇒ R(p) ≥ ε(c_𝒯 − o(1))log²p ≥ ε(28/(75π⁴) − η − o(1))log²p ⇒ (FA).
*Proof.* R(p) counts all ordered triples; the tiles' families are disjoint subsets of 𝒫(p) (Prop T (iii)), so
R ≥ Σ_t R_t. GENUSX Lemma 1: R_t − M_t = T_u + T_w + T_uw and M^cls_t = M_t + T_u, so R_t − M^cls_t = T_w + T_uw. ∎

*Reading (Assessment).* "All tools jointly" = Thm U + Thm X on every tile + disjoint union. What is left is exactly the
union of the per-tile exact-divisor layers. The union helps only if those layers cannot all be small together; §2.3
analyses the exact links found and §3 measures the dependence of the full-count windows (not of the signed E_t).

### 2.3 Lemma L (exact cross-window links; PROVED) and what they can force (Assessment)

Use *ordered* u-windows: a partition ℕ = ⊔_j W_j, R_j(n) := #{(u, B, C) : u ∈ W_j} and H_jk(n) := #{(u, B, C) : u ∈ W_j,
B ∈ W_k}.

**Lemma L.**
(a) For odd n: R_j(n) = Σ_{u∈W_j} #{m | n + u : m ≡ −1 (mod 4u)}, a function of the factorisations of the integers
    {n + u : u ∈ W_j} only; the integer sets of different windows are disjoint.
(b) (switch) For odd n: H_jk = H_kj, and R_j = Σ_k H_jk. The triple (u, B, C) with u ∈ W_j, B ∈ W_k lies in R_j; its swap
    (B, u, C) lies in R_k. Each triple is a divisor event of three integers: n + u = B(4uC − 1), n + B = u(4BC − 1),
    4Cn + 1 = (4uC − 1)(4BC − 1).
(c) (privacy, `SYNTHESIS_SPARKS8.md` Lemma 2.3) a prime ℓ ∤ u − u′ divides at most one of n + u, n + u′; in particular a
    prime ℓ > max(W_j ∪ W_k) − min(W_j ∪ W_k) divides at most one integer of the two windows.
(d) (parity) Let p ≡ 1 (mod 4) be prime, p ∤ u, and write p + u = 2^e·N′ with N′ odd. Every prime ℓ | N′ satisfies
    ℓ ∤ u and (ℓ/p) = χ_{−4u}(ℓ). Consequently (N′/p) = (u/p)(2/p)^e equals χ_{−4u}(N′), the number of prime factors of N′
    (with multiplicity) in the coset {χ_{−4u} = −1} is odd iff (u/p)(2/p)^e = −1, and every divisor m | p + u with
    m ≡ −1 (mod 4u) has (m/p) = χ_{−4u}(m) = −1.
*Proof.* (a) For fixed u, n = 4uBC − u − B ⇔ B | n + u and m := (n + u)/B ≡ −1 (mod 4u) (then C = (m + 1)/(4u) ≥ 1);
this is the trial form of FRONTIER §2.1, valid for every odd n in the triple form (no gcd condition is needed).
(b) (u, B, C) ↦ (B, u, C) is an involution of the solution set (the equation is symmetric in u, B); it maps
{u ∈ W_j, B ∈ W_k} bijectively onto {u ∈ W_k, B ∈ W_j}. The factorisations are expansions of 4uBC − u − B = n.
(c) ℓ | (n + u) − (n + u′) = u − u′.
(d) If ℓ | N′ and ℓ | u then ℓ | p, so ℓ = p | u, excluded; so ℓ ∤ u, ℓ ≠ p, and p ≡ −u (mod ℓ). Quadratic reciprocity
(p ≡ 1 (4)) gives (ℓ/p) = (p/ℓ) = (−u/ℓ), and for odd ℓ the Kronecker symbol χ_{−4u}(ℓ) = (−4u/ℓ) = (−u/ℓ). Multiplying
over the prime factors of N′ (with multiplicity), (N′/p) = χ_{−4u}(N′); and (N′/p)(2/p)^e = ((p + u)/p) = (u/p) since
p + u ≡ u (mod p). A divisor m ≡ −1 (mod 4u) of p + u is odd, so m | N′ and (m/p) = χ_{−4u}(m) = χ_{−4u}(−1) = −1
(χ_{−4u} is odd). ∎ (The hypotheses matter: p = 13, u = 5 has (u/p) = −1 but N′ = 9; p = 11 has the solution
(1, 4, 1) with m = 3, (3/11) = +1.)

*What the analysed links can force (Assessment).* (b) is a positive link: it moves a solution between two windows and
never creates one. (c) involves large primes but only says which integer a large prime divides (sizes), not its class
mod 4u, which is what a hit needs. (d) places an odd number of prime factors of the odd part of p + u in the BM coset
{χ_{−4u} = −1} when (u/p)(2/p)^e = −1; the BM layer is already pointwise free (FRONTIER §2.4, (J)103 Prop 2.2) and the
genus layer is what Thm U bounds. Small-prime congruences are B1. On Thm X tiles the proved statement is only
T_u = O(p^{−δ}log p) (density-level class term); dependence of the exact layers T_w, T_uw across tiles is not
controlled by anything here. The switch (b) is itself an exact cross-class relation: a hit m | n + u, m ≡ −1 (4u), gives
(n + B)/u ≡ −1 (mod 4B) at u′ = B = (n + u)/m; but it only relocates an existing hit. None of the links analysed here
forces a first hit when all windows are empty; beyond (b), small primes and the parity law (d) we found no relation
between divisor classes of different integers n + u, n + u′. CLASS_FORCING Thm 2.1 is the
analogous statement for total-product classes under specified Frobenius information. No theorem excluding other links
is claimed.

### 2.4 Proposition V (single-p variance is a first moment in disguise; PROVED, elementary)

Let R_j ≥ 0, M_j > 0, w_j ≥ 0 (j = 1…J) be reals, V ≥ 0.
(i) If Σ_j w_j(R_j − M_j)² ≤ V then Σ_j w_jM_jR_j ≥ ½(Σ_j w_jM_j² − V).
(ii) If all R_j = 0 then Σ_j w_j(R_j − M_j)² = Σ_j w_jM_j². Hence a pointwise variance bound excludes R = 0 iff
     V < Σ_j w_jM_j², and then (i) gives the weighted first-moment bound Σ_j (w_jM_j)R_j ≥ ½(Σ_j w_jM_j² − V) > 0.
(iii) (extraction from an average) If Σ_{p∈𝒫}|X(p)|² ≤ V_𝒫 over a set 𝒫 of primes, the only pointwise consequence is
     |X(p₀)|² ≤ V_𝒫; to exclude X(p₀) = −M(p₀) one needs V_𝒫 < M(p₀)², i.e. an average variance per prime below
     M(p₀)²/|𝒫|.
*Proof.* (i) (R − M)² = R² − 2RM + M² ≥ M² − 2RM; multiply by w_j and sum. (ii), (iii) immediate. ∎
*Reading.* A pointwise variance criterion across windows implies a weighted lower bound for R(p) itself (a
positivity statement of B2 strength); Prop V does not say that proving such a criterion is harder, only that it is not
a weaker target. CROSSO Lemma 4.1's bound Σ_{x/2<p≤x}|R − M̃|² ≤ x·V₈(x) yields at one prime only |X(p₀)|² ≤ x·V₈(x),
which excludes R(p₀) = 0 only if V₈(x) < M̃(p₀)²/x — far beyond HV (V₈ = o(log³x)). Under a Poisson model,
E Σ_j w_j(R_j − M_j)² = Σ_j w_jM_j, which is below Σ_j w_jM_j² iff Σ_j w_jM_j(M_j − 1) > 0 (M_j > 1 for all j is
sufficient, not necessary; e.g. w = (1, 1), M = (2, 1/2)). (EVIDENCE: F1's u-windows have var/mean 1.1–4.7, C-windows
0.5–2.3, §3.2.)

## 3. Computed

### 3.1 Engine and validation (CERTIFIED for the stated ranges)

`scripts/z56_famattack_wcount.c`: exact R(n) for odd n by factoring n + u (segmented sieve) for u ≤ (√(4n + 5) − 1)/4
(u < B forces 4u² + 2u − 1 ≤ n), enumerating divisors m ≡ −1 (4u) with B = (n + u)/m > u, and asserting
4uBC − u − B = n for each hit; output R and a 5×5 grid of unordered solutions by ia = ⌊10 log u/log n⌋ (u = min(u, B)),
ic = ⌊5 log C/log n⌋ (clamped to 0…4). Validation: equals brute force at every odd n ≤ 3001
(`scripts/z56_famattack_brute.py`); `range 5 10⁷` returns R = 0 at exactly 409, 577, 5569, 9601, 23929, 83449, 102001,
329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281 (the 14 known zeros); R = 0 at all odd squares tested.
`scripts/z56_famattack_mgen.c`: exact M_gen(n) and R*(n) by pair enumeration (square-class test mod q = 4uB, weight
s(q)/φ(q)); checks: M_gen(m²) = 0 (9801, 25, 1002001), R*(p) = R(p) at p = 1000009 (20).
Commands: `gcc -O2 -o wcount scripts/z56_famattack_wcount.c -lm`; `wcount range 100000000 104000000`,
`wcount range 1000000000 1002000000`, `wcount range 1199000000 1200000000`; outputs `data/z56/famattack/wcount_*.txt.gz`.

### 3.2 F1: cross-window association (EVIDENCE; pre-registered in checkpoint 1)

Data: all primes p ≡ 1 (4) in [10⁸, 1.04·10⁸] (N = 108 397), [10⁹, 1.002·10⁹] (N = 48 139); hold-out [1.199·10⁹,
1.2·10⁹] (N = 23 928). No zero of R in any. Scripts `z56_famattack_assoc.py`, `_ext.py`, `_lcontrol.py`, `_split.py`,
`_lead01.py`, `_jointempty.py`; outputs `data/z56/famattack/{assoc_F1*,ext,lcontrol,split,lead01,jointempty}.txt`.
All z-values are nominal (r·√N, an iid approximation); they are not calibrated for stratified arithmetic counts.

F1's u-windows are by u = min(u, B) ∈ [p^{k/10}, p^{(k+1)/10}), k = 0…4: their "own" integers p + min(u, B) are
disjoint across windows, but each solution also involves p + max(u, B) and 4Cp + 1 (Lemma L(b)); the C-windows are by
⌊5 log C/log p⌋ and have disjoint integers 4Cp + 1.

Window means (10⁹): u-windows 15.3, 9.0, 6.1, 3.5, 0.87 (var/mean 4.7, 1.2, 1.1, 1.4, 1.7); C-windows 14.1, 9.1, 6.5,
3.9, 1.2 (var/mean 2.3, 1.5, 1.8, 1.3, 0.50). Total unordered mean 34.7 (var/mean 3.1).

| pair (10⁹) | raw | within p mod 840 | OLS: residues mod 8, 3, …, 31 + L-proxies |
|---|---|---|---|
| u (0,1) | −0.063 | −0.064 (z −14) | −0.064 |
| u (1,2) / (2,3) / (3,4) | +0.10 / +0.26 / +0.45 | +0.08 / +0.24 / +0.42 | +0.065 / +0.21 / +0.40 |
| C (1,2) / (1,3) / (2,3) | +0.50 / +0.37 / +0.38 | +0.48 / +0.34 / +0.35 | +0.45 / +0.27 / +0.27 |
| C (3,4) | +0.10 | −0.05 (z −11) | −0.125 |

"L-proxies" = log of truncated Euler products ∏_{ℓ<20000}(1 − χ(ℓ)/ℓ)^{−1} for χ = χ_p (including ℓ = 2) and χ_{−4p},
their squares and product — proxies, not L-values. (Nominal s.e. 1/√N = 0.0046; 10⁸ and the hold-out agree in sign and
size: `assoc_F1.txt`, `assoc_F1_holdout_1p2e9.txt`, `lcontrol.txt`.)
Zero events: P(W₃ = W₄ = 0)/(P(W₃ = 0)P(W₄ = 0)) = 1.25 (10⁸), 1.31 (10⁹), 1.32 (hold-out); Mantel–Haenszel odds ratio
within p mod 840: 1.87, 1.82, 1.89. C-windows (pairs with both zero rates in (1 %, 99 %)): ratios 1.24–2.12; their MH
odds ratios are degenerate (0.90, 0, undefined) because C-window 4 is nearly constant within a class mod 840. Residual
off-diagonal covariance share after the OLS controls: u-windows +2.9 % / +6.1 %, C-windows +26.4 % / +30.8 %
(10⁸ / 10⁹). The covariates explain R² ≈ 0.33–0.37 of the total; corr(total, log-proxy for L(1, χ_{−4p})) = +0.37 / +0.36,
corr(total, log-proxy for L(1, χ_p)) = −0.19 / −0.17 (the χ_p sign is the one BM_LVALUE's T(p) ∝ L(1, χ_p)² predicts).

**Multivariate joint emptiness** (`jointempty.txt`). Windows = the 25 (u, C) grid cells with empty-rate in [5 %, 95 %]
(12–14 cells). For 300 random k-subsets per k (all kept, including subsets never jointly empty), the pooled observed
number of primes with all k cells empty, divided by the within-p-mod-840 conditional-independence prediction
Σ_s (n_s/N)∏_{i∈S}P_s(cell i empty):

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| 10⁸ | 1.01 | 1.04 | 1.10 | 1.19 | 1.43 | 1.90 | 3.20 |
| 10⁹ | 1.01 | 1.05 | 1.07 | 1.15 | 1.59 | 1.52 | 1.59 |
| hold-out | 1.02 | 1.06 | 1.10 | 1.39 | 1.74 | 2.65 | 3.42 |

(subsets overlap, so the pooled counts are not independent; descriptive only.) The baseline removes only p mod 840, so
global drivers (L-values, near-squareness) are part of what this measures. With richer strata (`_jointempty2.py`,
`jointempty2.txt`: p mod 120 or 24 × 3×3 or 5×5 quantile bins of the two L-proxies, median stratum size 178–767) the
pooled ratios stay above 1: k = 6: 1.35–1.68, k = 8: 2.1–4.1 (10⁸ and 10⁹). Only with very small strata (p mod 840 × 3×3,
median 59 at 10⁹; the per-stratum products are then fitted to the same few primes) does it drop to 1.15 / 1.25. Cells
in the same u-row share their integers p + u (Lemma L(a)), so part of this is the shared-integer link of Lemma L(b).

**Registered outcome.** The rule (checkpoint 1, commit d99773fc) was: a within-stratum pooled correlation below −4 s.e.
in any pair is a lead; all pairs ≥ −2 s.e. kills "compensation through disjointness". The kill condition is **not met**;
leads were triggered in every dataset. Crossings below −4 nominal s.e. within p mod 840: at 10⁸ u(0,1) z −26.0, u(0,2)
−5.0, u(0,4) −6.8, C(3,4) −50.1; at 10⁹ u(0,1) −14.1, C(3,4) −11.1; hold-out u(0,1) −8.8, C(3,4) −8.6. (The registration
named u-windows; C-windows were added in the same run.)

**Exploratory follow-up of the leads (not pre-registered).**
*C(3,4)* (−0.15 at 10⁸, −0.05 at 10⁹, −0.06 hold-out): both windows have C ≥ p^{0.6}, i.e. 4uB ≤ p^{0.4}·(1 + o(1)), so
each count is a function of p modulo the moduli 4uB ≤ p^{0.4} — congruence data. Its sign is a property of the
distribution of residues (competition between cheap pairs; cf. RESIDUE_HARDNESS); B1 says such data carry no pointwise
mechanism. Not pursued further.
*u(0,2), u(0,4)* at 10⁸ (−0.015, −0.021) vanish under the 1330-column residue control (−0.001, −0.001).
*u(0,1)* was pushed:
* it is congruence-sensitive: OLS (no 840 strata) with one-hot residues of p mod 8, 3, …, 31 gives −0.049; with the
  residues mod 16, 9, 25, 49, 11, …, 31 instead −0.038; with 32, 27, 25, 49, 121, 169 and all primes 17…97 (1330 columns)
  −0.024 (z −5.2; 10⁸: −0.027). These designs replace, not extend, the joint mod-840 stratification;
* the tested linear medium-prime proxies do not explain it: S₀, S₁ = numbers of (u, ℓ) incidences with ℓ ∈ (64, 10⁴] in
  windows 0, 1 have corr(S₀, S₁) = −0.098 (privacy is visible), but the partial correlation of W₀, W₁ given S₀, S₁ and
  their log-masses (within 840 strata) is −0.062 (unchanged). Nonlinear or residue-sensitive medium-prime effects are
  not excluded;
* it couples window 0 (u ≤ p^{0.1}, the HC lines, dominated by divisor-richness of p + u: within window 0 the
  C ≥ p^{0.6} and C < p^{0.6} parts correlate +0.50/+0.57) with the C < p^{0.6} part of window 1 only (−0.06…−0.07);
  window 0's correlations with windows 2–4 are within ±0.05 under every control and |r| ≤ 0.006 under the 1330-column
  residue control.
Reading (Assessment): most plausibly a short-range congruence/positional competition between the small-u lines and
the next window (small primes placed in p + u for u ≤ p^{0.1} versus p^{0.1} < u ≤ p^{0.2}); not identified. Its size
(−0.02…−0.08) is small against positive pair correlations up to +0.48; C(3,4) is larger (−0.15 within 840 at 10⁸;
−0.157 / −0.125 with L-proxy controls at 10⁸ / 10⁹) but congruence-determined. The net residual covariance is positive,
and multivariate joint emptiness exceeds the within-840 independence prediction. **Conclusion (EVIDENCE, scoped):** at
this resolution the full-count windows show some negative pairs, but net positive residual covariance and excess pooled
joint emptiness. This is about full-count windows, not
the signed exact layers E_t of Thm J, and about frequencies over primes, not about any single prime.

### 3.3 Why C-windows (disjoint integers 4Cp + 1) are positively linked

By Lemma L(b) each hit is a divisor event of n + u, n + B and 4Cn + 1 at once. A divisor-rich n + u with small u (an HC
line) produces hits at every scale of C (its divisors m = 4uC − 1 of all sizes), so C-windows built on disjoint
integers 4Cp + 1 still share the integers n + u. Within window 0 the two C-halves correlate +0.50…+0.57. In the
partitions tested here (size windows in u = min(u, B), and in C) the three integers of a hit are never all
window-disjoint, since they are tied by the three factorisations of Lemma L(b); no claim is made about every possible
partition.

### 3.4 Near-square primes (EVIDENCE; FRONTIER §4 item 15)

965 primes p = m² + k, k ∈ {1, 5, 9, 13, 21, 45, 105}, p ∈ [10⁹, 1.2·10⁹] (`z56_famattack_nearsq_gen.py`,
`_nearsq.py`, `data/z56/famattack/nearsq_profile.txt`); expected counts = generic means in the same class mod 840, with
two baselines: primes in [10⁹, 1.002·10⁹] and in [1.199·10⁹, 1.2·10⁹] (the near-squares lie between). Ratio
observed/expected, all k pooled: total 0.86 / 0.84; per u-window 0.81–0.90 / 0.80–0.89, per C-window 0.81–0.95 /
0.79–0.95; no zero. By k the totals are 0.78–0.91; individual windows are not all depressed for every k (k = 5, C-window 4:
1.15). Reading (Assessment): the pooled deficit is spread over all windows, consistent with a global driver acting on
every window at once; a causal identification with the T1 deformation is not made (no uncertainty model, mod-840
matching only).

### 3.5 Composite non-square zeros and the genus main term (CERTIFIED counts; EVIDENCE readings)

All n ≡ 1 (4), 5 ≤ n ≤ 7 999 801 (the run hit its 1700 s timeout there; range recorded as reached): R(n) = 0 at 1 711 n:
13 primes (the known ones ≤ 8·10⁶), 1 413 odd squares (all of them), 285 non-square composites
(`data/z56/famattack/zeros_n1mod4_le8e6.txt`, `compzeros_summary.txt`). Per decade (by ⌊log₁₀ n⌋ = 1…6): 1, 8, 24, 60,
95, 97 (the last decade only to 8·10⁶). The composite zeros were known to exist (BRAINSTORM `z52b_fingerprint.md`
#88–#89); new here are the counts to 8·10⁶ and their genus masses: exact M_gen(n) at 299 non-square zeros (all 285 composite zeros ≤ 7 999 801 and the 14 prime zeros incl. 8 813 281;
`mgen_nonsquare_zeros.txt`; R*(n) = 0 at all): composite median 8.0, maximum 24.25 (n = 810 001 = 241·3361), 22.9
(2 956 321 = 211·14011), 21.7 (752 257 = 11²·6217); the 14 prime zeros have M_gen from 4.0 (409) to 29.1 (8 813 281).
Matched controls (`mgen_zero_vs_controls.txt`, 24 triples near 4–8·10⁶): composite zeros mean M_gen/log²n 0.047, the
next composite ≡ same mod 420 0.062, the next prime ≡ 1 (4) 0.156.
*Reading.* At these n, X(n) = −M_gen(n) with M_gen up to 24. So a transfer "X ≥ −(1 − ε)M_gen" asserted for *every*
non-square n ≡ 1 (4) with M_gen above ~24 is false; a union argument whose only square-sensitive input is
non-squareness (e.g. Thm-U-type bounds, which GENUSLVAL §2.8 expects to extend to non-squares with local factors) cannot
be valid uniformly on these n. A finite census does not refute an eventual statement for non-squares, nor show that
primality (rather than some other extra condition) is what is needed (Assessment).

### 3.6 Model scale (Assessment)

Expected tail count T(x) = ∫_x^∞ e^{−c log²t}dt/(2 log t) of zero primes under hits ~ Poisson(c log²p)
(`z56_famattack_model.py`, `model_crossover.txt`; total counts integrate from t = 5; tails integrated directly from
their lower limit): c = 0.0808 (full count, measured mean/log²p at 10⁸–10⁹): 12.3 zeros in total (observed 14),
T = 1 at 10^{3.8} (the observed tail to 8.8·10⁶ is fatter: mean variation across p);
c = 0.0073 (tiled genus family, c_tile/2): 1.1·10¹⁴ zeros, T = 1 at 10^{57}; c = 0.00924: 10^{44.6}; c = 1/(3π⁴):
5.6·10³⁰ zeros, T = 1 at 10^{124.1} (reproduces CROSSF). Assessment: this model, run with the proved coefficient,
suggests an impractical cutoff; a Poisson tail integral is neither a deterministic checking threshold nor a bound on the
true family mean.

## 4. Where it stops — the step that would make it work

1. *Main terms.* The proved lower-bound coefficients are 9.6 % (Prop T) and 2.5 % (Prop T′, with Thm X's class control)
   of the mean coefficient; these are lower bounds from one window construction, not ceilings.
2. *Residual.* By Thm J, FA ⇐ (CU_𝒯). The union of tiles can help only through the joint behaviour of the exact layers
   E_t at one p.
3. *Dependence.* The exact links analysed (Lemma L) are the switch (positive), privacy (sizes only), the parity law
   (BM coset only) and small-prime congruences (B1). The full-count windows show net positive dependence and
   super-independent joint emptiness over primes (F1; EVIDENCE, not a statement about one p or about E_t).
4. *Missing ingredient (Assessment).* An argument that the exact class layers of different windows cannot all be
   small at the same p — e.g. "if the divisors of p + u miss −1 mod 4u for all u ∈ W_j, then some divisor of p + u′,
   u′ ∈ W_k, hits −1 mod 4u′". None of the links analysed here gives this; it would have to relate the classes of large
   prime factors of *different* integers at one p. We know no tool doing that. Absent it, (CU_𝒯) is a pointwise
   lower-tail statement for a sum of tied divisor-in-class counts with main term ≍ log²p — B2 in tied form. This is not
   a necessity theorem: a proof need not go through the union.
5. *Escape hatches left open.* (i) windows defined by non-size conditions (e.g. by the factorisation type of p + u),
   for which Lemma L(a)'s disjointness changes; (ii) signed combinations across windows (not sums of counts), e.g.
   theta-quotient identities (FRONTIER §2.3) mixing levels; (iii) a Type II family with a free variable not attached to p
   (FAMDESIGN (iii)), where cross-window dependence could differ; (iv) links other than those in Lemma L.

## 5. Screens (FRONTIER §4) for the best idea (Thm J + union over tiles)

1. **T1 (odd squares):** at n = m² every tile has R_t = M_t = M^cls_t = E_t = 0 (GENUSLVAL §2.8; GENUSX Remark (3)), so
   (CU_𝒯) is *vacuously true* there (0 ≥ 0); the step that fails at squares is the positive main-term lower bound
   (Props T, T′: the non-principality of ηχ_{−4up}). So the reduction passes T1 through its main term, and (CU_𝒯) itself
   does not distinguish squares. The composite zeros (§3.5) show that a transfer valid uniformly for all non-square
   n ≡ 1 (4) is false; no argument here addresses this.
2. **8/131:** the main-term side is 4-specific through the (★) parametrisation; the residual statement is not proved, so
   no false numerator-8 claim arises; no step here is numerator-uniform in the sense of (J)41. Not tested further.
3. **Tied modulus:** **fails** — the residual is exactly the tied event (divisor of p + u in −1 mod 4u); the union adds
   no untied variable (Lemma L).
4. **Fixed p:** passes for Props T, T′, J and Lemma L (each holds at each prime). F1 is a cross-prime diagnostic only;
   Prop V concerns one p. (B6: CROSSO's large sieve gives nothing pointwise, Prop V(iii).)
Test primes (item 14): all 14 (★)-zero primes have R = 0 in every window (engine), M_gen 4.0–29.1 (§3.5).

## 6. Proposed FRONTIER text (do not edit FRONTIER here)

*§7.3 / §7.4 addendum (z56 FAMATTACK).*
* **Tiling (PROVED, unconditional, effective; `Z56_FAMATTACK.md` Prop T).** Thm U over finitely many thin u-strips:
  M_gen(p) ≥ (64/(45π⁴) − ε)log²p ≈ 0.0146 log²p (2.13 × Thm U); Thm X tiles give M^cls ≥ (28/(75π⁴) − ε)log²p ≈ 0.0038
  log²p (1.97 × c_X) with T_u = O(p^{−δ}log p) (Prop T′). Proved coefficients = 9.6 % resp. 2.5 % of the mean coefficient
  3/(2π²) (lower bounds, not ceilings).
* **Joint reduction (PROVED; Thm J).** Thm U, Thm X and the disjoint union over a finite tiling reduce (★) to the tiled
  exact-layer bound (CU_𝒯): Σ_t (T_w + T_uw)_t ≥ −(1 − ε)Σ_t M^cls_t. (CU_𝒯) is vacuous at odd squares; the main term
  carries T1.
* **Union over windows (Lemma L, Prop V: PROVED; F1: EVIDENCE).** Exact cross-window links found: the switch
  (positive), privacy (sizes only), a parity law for the odd part of p + u (BM coset only; needs p ≡ 1 (4), p ∤ u), small
  congruences (B1); other links not excluded. A pointwise variance criterion across windows implies a weighted lower
  bound for R(p) (not a weaker target). Over ≈ 180 000 primes at 10⁸–1.2·10⁹, the pre-registered falsifier triggered
  leads (negative pairs: the u-window lead |r| ≤ 0.08; C(3,4) up to −0.157, congruence-determined) but full-count windows
  are net positively dependent
  (C-windows up to +0.45 after controls) and joint emptiness of k windows exceeds within-mod-840 independence (pooled
  ratio up to 1.6–3.4 at k = 8). Assessment: a union argument would need a mechanism relating the classes of large prime
  factors of different integers at one p; none is known.
* **Calibration (CERTIFIED counts).** 285 non-square composite n ≡ 1 (4) ≤ 7 999 801 have R(n) = 0, with M_gen up to 24.3
  (810 001 = 241·3361): a transfer X ≥ −(1 − ε)M_gen asserted uniformly for non-squares is false at these n.

*§6 dead-end line (method-scoped, not a theorem killing union or variance routes).* (z56) Positivity from the union over
size windows of the (★) count via the links of Lemma L, or from a pointwise variance across windows →
`Z56_FAMATTACK.md` Lemma L, Prop V, F1: the analysed exact links are positive (the switch only relocates hits), size-only,
quadratic or congruence-level; a variance criterion implies a first-moment statement; the data show some negative pairs
but net positive residual covariance and excess joint emptiness. Not covered:
non-size windows, signed cross-level identities, links outside Lemma L.

## 7. Bottom line

Combining Thm U, Thm X, the switch, the spin dictionary and dual-large-sieve variance does not prove (★) at a single
prime. What it buys: the proved genus main-term coefficient roughly doubles (Prop T: 0.0146 log²p; Prop T′: 0.0038 log²p
of exact-class density), and a clean statement of what the joint attack reduces to, (CU_𝒯). The brief's specific hope —
that windows built on disjoint integers p + u cannot all fail together — found no exact mechanism among the links
analysed (Lemma L); a pointwise variance route is a positivity statement in disguise (Prop V); and in the data the
full-count windows reinforce rather than compensate (F1), a global deficit such as near-squareness lowers all windows
together, and non-square composites with genus mass up to 24 are empty. A union argument would need to relate the
classes of large prime factors of different integers at one prime; nothing checked here does that. ES remains OPEN.

## 8. Review

**Internal hostile review (deep-mode subagent, 2026-11-04), verdict REJECT of the first draft (commit 24918302); all
findings applied in this version.** The reviewer re-derived Props T, T′ (areas 8/45 and 7/150, coefficients 0.0146005081
and 0.0038326334, margins, disjointness, finite-union error handling, no hidden optimal-rectangle assumption in GENUSLVAL
Props 2.4–2.5), the decomposition behind Thm J, the census, genus masses and statistical tables, and found no
result-invalidating bug in either C engine (brute-force and rational square-class checks). Findings and fixes:
1. *Registered F1 rule misreported* (MAJOR): the kill condition was not met; four crossings at 10⁸, not two. → §0 and §3.2
   now report "leads triggered, kill condition not met", list every crossing, and mark the follow-up as exploratory.
2. *Pairwise association does not determine joint emptiness* (MAJOR; counterexample with pairwise-positive but never
   jointly empty vectors). → Added the multivariate joint-emptiness test (§3.2, `z56_famattack_jointempty.py`, no
   selection on observed zeros); removed the claim that negative association is necessary; F1 scoped to full-count windows.
3. *Lemma L(d) false as stated* (MAJOR; p = 5, u = 5 and p = 11). → Hypotheses p ≡ 1 (4), p ∤ u added, multiplicities
   stated, proof written out.
4. *Non-residue factor need not be odd* (MAJOR; p = 13, u = 5, the non-residue factor is 2). → (d) is now about the odd
   part N′, with the factor (2/p)^{v₂(p+u)}; (N′/p) = χ_{−4u}(N′) proved.
5. *(CU_𝒯) is vacuous, not false, at squares* (MAJOR). → §5 item 1 rewritten: T1 is carried by the main term.
6. *Completeness / impossibility overclaims about links* (MAJOR). → "links analysed here"; no completeness claimed; §6
   dead-end line scoped.
7. *Order-≥3 "global driver" claim beyond Thm X* (MAJOR). → Only T_u = O(p^{−δ}log p) on tiles is stated.
8. *"≤ 9.6 %" read as a ceiling* (MAJOR). → Stated as a proved lower-bound coefficient; the 64 % figure labelled as
   orientation for this window construction only.
9. *L-value controls were odd-prime truncated products without the factor at 2* (MAJOR). → Factor at 2 for χ_p restored,
   controls rerun (`lcontrol.txt`), labelled as proxies; numbers updated (corr −0.19/−0.17; C(3,4) −0.125).
10. *Composite census overread* (MAJOR). → Conclusion limited to transfers asserted uniformly for non-squares.
11. *Thm J constant* (MINOR). → Tiling loss η separated from the (CU) parameter ε.
12. *V₈ < M²/x, not M²/π(x)* (MINOR). → Fixed; Prop V reading softened (not "harder", "not weaker").
13. *Ordered vs unordered in Lemma L(b)* (MINOR). → Triple vs its swap distinguished.
14. *Nominal z-values; control designs replace strata* (MINOR). → Stated in §3.2.
15. *Near-square baseline not size-matched; not every window for every k* (MINOR). → Second baseline at 1.2·10⁹ added;
    k = 5 exception noted; causal T1 identification removed.
16. *Model integral cutoff / tail quadrature* (MINOR). → Total from t = 5 (12.3, was 11.8 from t = e²); tails integrated
    from their lower limit; crossover exponents unchanged.


**Cross-model review** (`data/z56/xreview/REVIEW_FAMATTACK.md`, at 9e52e1f3; verdict ACCEPT-WITH-FIXES). Props T, T′,
Thm J, Lemma L and Prop V(i)–(iii) independently reconstructed and judged CORRECT; census, genus masses, F1 statistics,
near-square ratios and model integrals reproduced with independent code (`scripts/z56_xrev_famattack_census.c`,
`_check.py`). Required fixes, all applied: (1) the "−0.02…−0.08 / all |r| ≤ 0.08" compression omitted C(3,4) (−0.15,
−0.157, −0.125) → both reported in §0, §3.2, §6, and "no compensation" replaced by "some negative pairs, but net positive
residual covariance and excess pooled joint emptiness"; (2) the switch is itself an exact cross-class relation → §0,
§2.3 now say no analysed link forces a first hit when all windows are empty; §3.3's "no coordinate system" restricted to
the tested partitions; §6 dead-end line marked method-scoped; (3) Poisson criterion after Prop V corrected to
Σ w_jM_j(M_j − 1) > 0; (4) the "checkable only with mean near the full count" sentence replaced by an Assessment.
