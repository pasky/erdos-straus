# Second independent hostile cross-lab review: `notes/z78/ANALYTIC_WILD.md` §§6–8 (R(n) ≪ n^{20/63+ε})

Reviewer: Claude Opus (author: GPT Astra). Range: `HEAD~1..HEAD` (merge 097d726c4, i.e. the whole new note plus scripts/data).
I formed this verdict before reading `REVIEW_ANALYTIC_WILD_R2_OPUS.md`; the comparison is in §6 below.
This is internal review only, not external refereeing. It concerns an **upper bound** for the c=1 Type II count
R(n) = #{(a,d) ≥ 1 : (4ad−1) | (n+a)} = #{(a,b,d) : 4abd−a−b = n}. It has no bearing on ES, which remains **open**.
No provider, auth or quota errors occurred.

## Verdict: ACCEPT-WITH-FIXES

**The exponent 20/63 survives.** I found no FATAL or MAJOR mathematical defect in §§7–8. The 7/22 step and the 20/63
step are both correct unconditionally. Their inputs are classical: Weil via z76 §2 / Z53 Lemma W, a uniform 1-D stationary
phase, the Montgomery–Vaughan additive large sieve, r₂(s) ≤ 4τ(s), and divisor bounds. No exponent-pair input, GRH or
Trudgian–Yang is used. The defects are about form, citation and replay completeness (§5).

## 1. Re-derivation of the architecture

**Setup (z76 §2).** Poisson in k gives
S_Q = Σ_ℓ Σ_C a_ℓ(C) G_C(ℓ) e(−ℓn/(4QC)), with a_ℓ(x) = V/(4Qx) Φ̂(ℓV/(4Qx)).
I re-derived this from scratch, sign included. With Q = sN and x = yW one gets a_ℓ = L⁻¹ b(y,s), where L = NW/V, exactly
as in §7. For |ℓ| ≤ Ln^δ the derivatives of b(y,s) are uniformly bounded, since u·Φ̂′(u) is Schwartz. Trivial bounds make
the tails beyond Ln^δ power-negligible.

### (a) Positivity / enlargement: legitimate
The square sieve needs only the **average** over prime pairs of |S_Q|, not the maximum. The chain is:
1. triangle inequality in ℓ, costing n^δ;
2. Cauchy–Schwarz in Q, giving avg|·| ≤ (avg|·|²)^{1/2};
3. z76's shift identity Σ_x g z = H⁻¹ Σ_x g(x) Σ_i z(x+iQ) (g Q-periodic), then Cauchy with ‖g‖² over the support ≪ (W/Q+1)Q² ≪ WN.

Step 3 gives |Σ_x G^Q_x(ℓ) z_Q(x)|² ≤ (WN/H²)·K_ℓ(Q), where **K_ℓ(Q) = Σ_x |Σ_{i≤H} z_Q(x+iQ)|²**. This is the nonnegative
quantity. It is a sum of squared moduli, defined for every real Q ∈ [N,4N], and it contains no G.

The enlargement avg_{Q=qr} K ≤ (N/J)·N⁻¹ Σ_{N≤Q≤4N} K is applied to K before it is expanded. This is the only point where
positivity is used. Only afterwards is the square expanded:
N⁻¹ΣK ≤ HW + 2H Σ_{h<H} E_h,  with E_h = |N⁻¹ Σ_Q Σ_x z_Q(x+hQ) z̄_Q(x)|.

The weights (H−h) are Q-independent, so keeping the Q-sum signed inside E_h is legitimate. No signed sum is ever enlarged.

### (b) Cauchy–Schwarz steps
| step | inside | outside |
|---|---|---|
| Cauchy in Q | the ℓ-fixed sum | the 1/L·#ℓ ≍ n^δ factor and the prime-pair average |
| Cauchy in x | g, through its full-period mass | z, as the H-translate sum |
| §7, (8): Cauchy over m | — | the O(Y) band frequencies |
| §8, (9): Hölder over m | — | the O(Y) band frequencies |

In both of the last two rows, the Q-sum is inside the absolute values and Abel summation in Q is done first. I reproduced
the block bound
avg|S_Q| ≪ n^{δ+o(1)} [V/N + V/W + W√(N/H) + (WN·avg_h E_h)^{1/2}].
With j = 2(r+γ−t), both the diagonal and the off-diagonal target are n^{2t} exactly. That is, E_h must have exponent ≤ γ−j.

### (c) B-process: correct and uniform
- **Phase difference.** It is exactly nℓh/(4x(x+hQ)) = A/(t²−(hQ/2)²), with t = x+hQ/2. The 1/Q cancels, which is the key structural point.
- **Parity.** Poisson over ℤ + hQ/2 gives the sign (−1)^{m·hQ}. This is constant on each parity class of Q (only when h is odd).
- **Scaled phase.** It is T[(y²−σ²)⁻¹ ± (m/Y)y], where T = A/W² = WY and σ = hQ/(2W) ≤ 2HN/W ≪ n^{−c}.
- **Critical point.** For y > σ, φ′ is strictly monotone, so the critical point is unique. At σ = 0 one has φ″ = 6/y⁴, nondegenerate. The singularity at y = σ is far from supp ⊂ (1/2,3).
- **Hörmander 7.7.5.** It is genuinely uniform here. The theorem's constant stays bounded while the phase stays in a bounded C^{3k+1} set and |y−y*|/|φ′(y)| is bounded. Critical points just outside the amplitude support are covered by taking a fixed K ⊃ all y*. The true remainder is W·T^{−3/2}. The note's O(W/T) is weaker but valid. Summed over O(Y) band m it gives O(Y·W/T) = O(1).
- **Non-stationary m.** These include m = 0 and |m| ≫ Y. There |∂_y phase| ≫ T + W|m|, and higher phase derivatives are O(T), so repeated integration by parts gives ≪ W(T+W|m|)^{−B}. This is negligible because T ≥ n^{1−2γ}/4 and γ < 1/2 on the whole triangle (min 1−2γ = 17/63).
- **Expansion in σ.** By the envelope theorem, ∂(critical value)/∂σ² = (y*²−σ²)⁻², so the critical value is φ₀ + y₀⁻⁴σ² + R with R = O(σ⁴). This also holds under s∂_s, since σ² ∝ s². Hence ξ_m = (Ah²/4W⁴)(m/2Y)^{4/3}, ξ_m ≍ Z = Yh²/W, and ξ′_m ≍ Z/Y.
- **Numerical check (mine).** `scripts/z78_review_opus2_sp.py` uses W = 4000, Y = 12 and Q = 20…160, both parities. The exact correlation Σ_x a(t/W) e(A/(x(x+hQ))) agrees with the stationary-phase prediction to about 0.002 absolute, against |S| ≈ 25–80. The quadratic-in-Q model with the note's ξ_m agrees to within ≲ 10·Tσ⁴ (0.002 → 0.05 as Tσ⁴ goes 10⁻⁶ → 10⁻²). This confirms the sign, the parity and the 4/3 power.
- **Ranges.** Q ≤ 4N = n^{2r+o(1)}, with r ≤ 1−3t = 1/21 on the triangle. Then |ℓ| ≤ n^{2r+γ−β+δ}, h ≤ n^j and m ≍ Y ≤ n^{d+δ}.
- **Frequency cases.**
  - Imprimitive or shared-prime ℓ: the only input is Σ_{c mod Q}|G_c(ℓ)|² ≪ Q², uniformly in ℓ including (ℓ,Q) > 1. This is inherited from z76 §2 and was reviewed there.
  - ℓ = 0: costs V/N + V/W.
  - h = 0: this is the HW diagonal.
  - m = 0: non-stationary.
  - There are no "three-conductor" or shared-prime correlations, because Cauchy removes G before any pairing.

### (d) Second and fourth moments: correct, classical
**Arc multiplicity.** In any arc of length 1/N² there are D₀ ≪ (1+Z)(1+Y/(ZN²)) points ξ_m mod 1. Colouring then gives
O(D₀) N⁻²-separated families.

**Second moment, (8).** Montgomery–Vaughan on frequencies Q² ≤ 16N² (fixed parity, partial interval) gives
Σ_m |Σ_{Q∈I} e(ξ_m Q²)|² ≤ D₀(16N² + O(N²))·|I| ≪ N³D₀.
This reproduces all four terms of (8).

**Fourth moment, (9).** The exact inequality is
Σ_m |Σ_{Q∈I} e(ξ_m Q²)|⁴ ≪ D₀(32N² + N²)·Σ_s c_s².
- Here c_s = #{(Q₁,Q₂) ∈ I²: Q₁²+Q₂² = s} ≤ r₂(s) ≤ 4τ(s), and Σ_s c_s = |I|².
- So Σ c_s² = E(I²) ≤ 4 max τ · N² ≪ N^{2+ε}. The true size is ≍ N² log N.
- The inequality is valid for every N ≥ 1.
- The diagonal Q₁²+Q₂² = Q₃²+Q₄² is fully counted by this bound. Square s and small gcds play no role, since only max r₂ is used.

Hölder with Y^{3/4} then gives exactly the four terms of (9).

**Abel summation.** It is done before Cauchy/Hölder, using sup and total variation of w_m(Q/N). These are uniform in m, h
and ℓ, up to the factor (1+Tσ⁴) from the quartic residual.

**Remark (not in the note): 4th is the optimal large-sieve moment.**
- The 2k-th moment for k ≥ 3 is again ≪ N^{2k}D₀, so the saving is (Y/D₀)^{1/(2k)}, which decreases with k.
- The second moment loses a factor N, so its saving is (Y/(ND₀))^{1/2}.
- k = 2 therefore maximises the saving among these moments.

### (e) Weil, Gauss sums and divisor bounds
Weil is used only through z76's uniform second moment of G. I re-derived §6 formula (6), including
a = n/(4c)+1/(8c²) and d = (4cn+1)/(64c⁴); that formula is not used in §§7–8. Divisor bounds are used in three places:
- the detector mass Σ_s τ(n+s) ≪ Vn^ε;
- the fibre bound n^ε·min(U,W) for blocks with min(α,γ) ≤ t;
- r₂ ≤ 4τ in §8.

### (f) Hypotheses
n is arbitrary. I found no use of primality, squarefreeness or smoothness. Primes q | n only change local DC rows, and z76
already treats these. No GRH, exponent pair, Trudgian–Yang, Bourgain or Huxley input enters. The claim "no exponent-pair
input" is correct.

## 2. Independent LP / range coverage
My own script, `scripts/z78_review_opus2_lp.py`, recomputes every exponent from the raw quantities P, N, H, L, Y, Z, T and σ.
It does not copy the author's formulas. It includes:
- the detector, the zero frequency and the diagonal;
- the **O(1) term of E_h**, which the author's script does not assert;
- all four E-terms, with the h-dependence handled correctly: h^{3/2} and h^{1/2} terms are taken at H, and the 1/h and h^{−1/2} terms are averaged;
- the side conditions γ > j+2r, 1 > 2γ, L ≥ 1, r, j ≥ 0, and the quartic condition.

Results:
- **Whole-triangle check.** At t = 7/22 (2nd moment) and t = 20/63 (4th moment), every point of a 30-step barycentric grid over the whole triangle passes. The off-diagonal maximum equals t exactly, and the quartic maximum is −1/22 and 0 respectively. At t − 10⁻⁴ the check fails.
- **Free optimum.** I freed the (r, j) choice at vertex 1 and grid-optimised it. The minimum t comes out ≈ 0.31819 for (8) and ≈ 0.31750 for (9), i.e. 7/22 and 20/63 up to grid resolution. The note's parameter choice is therefore optimal, not merely sufficient.
- **Binding constraints.**
  - For (8), the binding term is h√(NY), giving 5r ≤ t−2r, i.e. t ≥ 7/22.
  - For (9), the binding term is W^{1/4}Y^{1/2}h^{1/2}, giving 20r ≤ 3t. The quartic condition d+4j+8r−3γ = 20r−3t ≤ 0 coincides with it.
  - Dropping the quartic condition does not move the optimum, because the large sieve binds at the same point.
- **Coverage of the dyadic decomposition.**
  - Blocks with U > V are covered by symmetry in (u,B).
  - Blocks with min(α,γ) ≤ t are covered by the fibre divisor bound n^ε·min(U,W).
  - The triangle β ≥ α ≥ t, γ ≥ t is handled entirely by §7/§8.
  - At vertex 2, r = 0 (P = log³n), and every term has margin: off-diagonal 7/36 vs goal 17/63; O(1) term γ+2r = 23/63 vs 2t = 40/63.
  - The ℓ = 0 conditions β−2r ≤ t and β−γ ≤ t hold throughout. The detector diagonal V/P = n^t/log³n holds by choice of r.
- **Replays.** `scripts/z78_analytic_r2.py` replays byte-identically to `data/z78/analytic_r2_lp.txt`. `scripts/z78_analytic_wild.py` replays identically to `data/z78/analytic_wild_checks.txt`.
- **Arithmetic.** 7955/24966 − 20/63 = 205/174762 and 8/25 > 7955/24966 > 7/22 > 20/63 > 4/13 > 3/10 are all correct.

## 3. Numerics (formula sanity only)
`scripts/z78_review_opus2_R.c` sieves all triples with 4abd−a−b ≤ 10⁷ in about 1 s. Brute force over (a,d) with (4ad−1) | (n+a)
agrees for every n ≤ 3000.

| range | max R(n) | log max R / log n |
|---|---:|---:|
| n ≤ 10⁷ | 183 (at n = 7,702,694) | — |
| [10², 10³] | — | 0.437 |
| [10³, 10⁴] | — | 0.397 |
| [10⁴, 10⁵] | — | 0.369 |
| [10⁵, 10⁶] | — | 0.346 |
| [10⁶, 10⁷] | — | 0.329 |

For n > 10³, max R(n)/n^{20/63} is 2.29 (at n = 5354). The decreasing trend looks divisor-like and nothing is absurd.
This cannot test any exponent.

## 4. §0, labels, scope, and consistency with §1
- The PROVED label for §§7–8 is correct. The "rel." list is accurate.
- "External priority unverified" is appropriate. Averaging over moduli after a q-van der Corput step is a classical device (Heath-Brown; Fouvry–Iwaniec-type modulus averaging), so the claim is a campaign record for this count, not a technique.
- §1 Theorem 1 is a model barrier for the **signed z77 dispersion majorant** below 3/10. §§7–8 use only ‖G‖₂ ≪ Q, so they apply equally to the §1 mock rows. Their exponent 20/63 > 3/10 is consistent with §1, and §1 does not obstruct them.
- The comparison with 8/25 and 7955/24966 is correct. The new bound removes the Trudgian–Yang/Bourgain/Huxley/Sargos dependence.

## 5. Defects
No FATAL and no MAJOR defects.

1. **MINOR — §0 Scope, first sentence.** It describes §§1–3 ("a sharp count of eligible integer windows, a floor only for a specified numerical certificate, a norm comparison…") and says nothing about the headline. **Repair:** open with "§§7–8: R(n) ≪ n^{20/63+ε} for every n ≥ 2, unconditional, counting ordered triples 4abd−a−b = n (z76 §0)". Then list the §§1–3, §6 and §§9–10 scopes per section.
2. **MINOR — §0 Result/Label/Triage mix.** There are two RECORDs: one unconditional, and one (§4, the 2√2 constant) CONDITIONAL on GRH. The note has a single PROVED label and a one-sentence Result naming only one of them. The R2 review already asked for a split, and the author declined. **Repair:** either split §§6–8 into their own note, or add to the Label: "§4 and §9 cap consequences CONDITIONAL on Dirichlet GRH". At export, keep them as separate STATUS rows with separate labels. The STATUS delta already does this.
3. **MINOR — §8, quartic endpoint.** The "zero residual exponent is legitimate" argument is correct: the loss is (1+Tσ⁴) ≤ n^{δ+o(1)} in Abel's total variation. It is also unnecessary. The theorem has +ε, so one can run the LP at t = 20/63+η, where 20r−3t < 0 strictly. **Repair:** state it that way and keep the endpoint argument as a remark.
4. **MINOR — §7, stationary-phase citation and error.** **Repair:**
   - quote Hörmander 7.7.5's uniformity clause: C stays bounded for phases in a bounded C^{3k+1} set with |x−x₀|/|f′| bounded;
   - say that K is a fixed interval containing all critical points, so critical points just outside supp(amplitude) are covered;
   - optionally improve O(W/T) to O(W T^{−3/2}). No exponent changes.
5. **MINOR — replay completeness.** `scripts/z78_analytic_r2.py` does not assert three things:
   - the O(1) term of E_h, i.e. γ+2r ≤ 2t;
   - that the detector and diagonal fit (true by construction of r and j);
   - interior points (vertex-only checking is valid by affinity, but the script should say so).
   **Repair:** add one assert for γ+2r ≤ 2t. It holds with the worst value 23/63 ≤ 40/63.
6. **MINOR — §8 "Next step".** The statement is correct as scoped ("with the unchanged bounded-residual requirement"). Two additions would help:
   - the quartic condition is *soft*: it is an Abel loss factor (1+Tσ⁴), not a wall;
   - higher large-sieve moments (k ≥ 3) are strictly worse than k = 2 (§1(d) remark).
   So any further progress must use the arithmetic of ξ_m (spacing in m, or a double large sieve in (m,Q)) or the quartic term. "More moments" will not help.
7. **MINOR — §0 Review line.** It says both reviews were "accepted with minor repairs, incorporated". The R2 review said "do not promote yet", and its split request was not done. **Repair:** at export, cite this second review as well. State that the split was declined and that the remaining items are form-only.
8. **MINOR, form — §7 "Split Q by parity".** The split is needed only when h is odd. It is harmless as written.

Outside §§6–8, I spot-checked only the following and found no new issue:
- §2: the supply bound, and the lower progression example with log D_k = k log(k log k) + O(k), which is consistent with (1+o(1)) k log k;
- §3: the Rankin product bound with z = k log k, and Brun–Titchmarsh plus Markov;
- §4: box injection, Minkowski II and the 2√2 arithmetic, with u = (2+o(1))t and k = 2√(u/log u);
- §6: formula (6) and the (7) counting.

The first Opus review covered §§1–5 in depth, and I did not repeat it.

## 6. Comparison with `REVIEW_ANALYTIC_WILD_R2_OPUS.md` (read only after the above)
**Agreement.** We agree on every substantive point: positivity before expansion, phase centring and sign, ξ_m, (8) and
(9), the uniform Abel step, LP optimality, and no fatal gap. Its form repairs (Hörmander citation, replay line,
"exponent-pair input" wording, triage of §9/§10) have been incorporated into the note. Its split request has not.

**Differences.**
- **Quartic barrier.** R2 says "20/63 is the limit of any method that truncates the Q-phase at quadratic order. Higher moments cannot help unless the σ⁴ term is kept." That is **overstated**. The quartic condition is only a soft loss factor (1+Tσ⁴) in Abel's total variation. Dropping it as a hard constraint does not move the optimum (my LP), but only because the large-sieve term binds at the same point. A sharper Q-sum estimate that exploits the structure of ξ_m, rather than generic spacing, could go below 20/63 while paying a small quartic loss. On "higher moments", I give a separate and sharper reason: 2k-th large-sieve moments for k ≥ 3 save less than k = 2. The note's own §8 formulation, scoped to the bounded-residual requirement, is correct.
- **Endpoint.** R2 accepted the n^δ endpoint argument. I accept it too, but point out that it is redundant given the +ε.
- **Extra checks here.** My LP adds the O(1) E_h term and a full-triangle grid. I also give an explicit inequality for the fourth moment, including the energy count.

**Bottom line:** ACCEPT-WITH-FIXES. R(n) ≪_ε n^{20/63+ε} for every n ≥ 2 is PROVED (rel. Weil via z76 §2, uniform
stationary phase, the Montgomery–Vaughan large sieve, r₂ ≤ 4τ). It is a campaign record, with external priority
unverified. With this second cross-lab review the record is promotable after the MINOR form repairs.
