# Second independent hostile cross-lab review: `notes/z78/ANALYTIC_WILD.md` §§11–13 (R(n) ≪ n^{272/857+ε})

Reviewer: Claude Opus. Author: GPT Astra. Scope: commits `HEAD~1..f1d33c63c` (merge of lane branch at `2d42c3e6e`;
commits 57aea294c, 7be0f5bb5, ea376720c, 2d42c3e6e). §§7–8 (20/63) were taken as given, per the brief. Every place
where §§11–12 modify §§7–8 was re-checked. I formed my verdict **before** reading `REVIEW_ANALYTIC_WILD_R3_OPUS.md`;
the comparison is in §7 below.

Provider/auth/quota errors: **none**. I used no subagents or external models. All computation was local:
`ulimit -v 6000000; timeout ≤900 uv run --offline --no-project python scripts/z78_review_272857_lp.py`,
with the log in `/tmp/z78_review_272857_lp.log` (excerpted in §3).

ES is OPEN. This is an upper bound on a representation count only.

## Verdict: ACCEPT-WITH-FIXES. The surviving exponent is **272/857** (≈ 0.317386).

I found no FATAL or MAJOR defect. The improvement over 20/63 is 4/53991 ≈ 7.4·10⁻⁵. It comes from a legitimate
change of constraints, and every replacement inequality is proved in the note (§4 below). The defects are MINOR (form,
citation and exposition). None changes an exponent.

## 1. §11: counting clustered frequencies by inverting the phase

**What is proved.** Fix (ℓ, h). The dual frequencies are the integers m in the stationary band [c₁Y, c₂Y], with points
ξ_m = c·m^{4/3}, ξ_m ≍ Z = Yh²/W. Let D₁ be the maximum, over **all** arcs of length N⁻² mod 1 (arbitrary offset η),
of the number of m with ξ_m mod 1 in the arc. Then (10) holds: D₁ ≪ n^ε(1 + Y/N² + Δ + Z^{11/15}Y^{1/15} +
Z^{29/28}Y^{−1/14}), where Δ = Y/(ZN²). This is exactly the multiplicity D₀ that enters the colouring form of the
large sieve. The bound replaces the old D₀ = (1+Z)(1+Δ), and it is the right object.

**Derivation re-done.**
* The map ξ ↦ m = (ξ/c)^{3/4} has derivative ≍ Y/Z. So {m : ξ_m ∈ v+η+[0,N⁻²]} lies in an interval of length ≍ Δ
  starting at f(v) = ((v+η)/c)^{3/4}.
* The old D₀ is always valid, so one can split at Δ = c₀ with no gap at Δ ≍ 1.
  * For Δ ≥ c₀ and Z ≥ 1, D₀ ≪ ZΔ = Y/N².
  * For Δ < c₀, each v contributes at most one m, and only if ‖f(v)‖ ≪ Δ.
* Erdős–Turán on the O(Z) values v gives O(ZΔ + Z/B + Σ_{l≤B} l⁻¹|Σ_v e(l f(v))|) for every integer B ≥ 1.
* f is C^∞ on v+η ≍ Z, with f⁽⁴⁾(v) = −(135/256)c^{−3/4}(v+η)^{−13/4}. This has constant sign, and
  |f⁽⁴⁾| ≍ Y/Z⁴ with comparability ratio (c₂/c₁)^{13/3}, an absolute constant.
* Titchmarsh Thm 5.13, k = 4, K = 8, gives Σ ≪ Mλ^{1/14} + M^{3/4}λ^{−1/14} for b − a = M ≥ 1, λ ≤ |f⁽⁴⁾| ≤ hλ.
  * The hypotheses are real f with continuous derivatives to order 4, a two-sided bound on f⁽⁴⁾ of fixed sign, and
    b − a ≥ 1.
  * There is no smallness condition on λ and no monotonicity condition.
  * It is applied to l·f with λ = lY/Z⁴. At the chosen B, Bλ ≤ (Y/Z⁴)^{14/15} ≤ 1.
* The 1/l sum costs log B ≪ n^ε.
* Balancing Z/B against Z(BY/Z⁴)^{1/14} gives B = (Z⁴/Y)^{1/15}, hence Z^{11/15}Y^{1/15}. The second Titchmarsh term
  gives Z^{3/4}(Z⁴/Y)^{1/14} = Z^{29/28}Y^{−1/14}.
* If Z⁴ < Y, the trivial O(Z) is at most Z^{11/15}Y^{1/15}. If Z ≪ 1, D₀ ≪ 1 + Δ.
* Conclusion: (10) is correct.

**Uniformity.** The bound is uniform in:
* the arc offset η;
* h and ℓ (they enter only through c, Y, Z);
* the Q-range (the ξ_m do not depend on Q);
* n (no arithmetic of n is used; n enters only through A = nℓh/4).

Non-squarefree n are irrelevant to this step. The bound is used **pointwise in h**:
* every term of (10) is a monomial in h, and all of them have an h-exponent > −1;
* the terms with positive exponent are evaluated at h = H;
* Δ^{1/4} ∝ h^{−1/2} is averaged via H⁻¹Σh^{−1/2} ≪ H^{−1/2}.

No average over h, ℓ or Q is assumed silently. All terms increase in Y, so taking Y at its maximum (ℓ ≤ Ln^δ) is
legitimate. The new middle term W^{19/60}Y^{27/60}h^{11/30} = W^{1/2}Y^{1/4}(Z^{11/15}Y^{1/15})^{1/4} checks. So does
the fifth term W^{27/112}Y^{55/112}h^{58/112}.

**The §11 Abel penalty.** Paying the total variation 1 + T(hN/W)⁴ of the quartic residual is legitimate: Abel summation
uses a sup over m of |∂_Q w_m|. K = (d+4j+8r−3γ)⁺ is that variation at h = H and Y = Y_max. Every term is monotone
there, and so is the penalty multiplied by h^{−1/2}. 1472/4637 is correct.

## 2. §12: freezing the quartic phase on short dual bands

* **Taylor coefficient.** Let φ(y,s) = (y²−s)⁻¹ + μy with s = σ². Then:
  * φ_yy(y₀,0) = 6y₀⁻⁴ and φ_ys = −4y₀⁻⁵, so y*′(0) = (2/3)y₀⁻¹;
  * g″(0) = −2y₀⁻⁶(2y₀y*′ − 1) = −(2/3)y₀⁻⁶;
  * hence the σ⁴ coefficient is −(1/3)y₀⁻⁶ ✓;
  * ζ_m = −h⁴m²/(192·Y·W³), a constant times m² ✓.

  The remainder is s³·G(s, m/Y) with G smooth, and Q∂_Q s = 2s. So the sextic remainder and its scaled Q-derivative are
  O(Tσ⁶). The sextic condition d+6j+12r−5γ < 0 is the exponent of T(HN/W)⁶ at Y_max ✓.
* **Bands.** There are J ≍ 1 + T(hN/W)⁴ = 1 + Z(hN²/W)² equal real subintervals of [c₁Y, c₂Y]. Across a band, ζ_mQ⁴
  changes by ≪ T(hN/W)⁴/J = O(1), and the same holds after Q∂_Q. Hence |∂_Q w_m| ≪ 1/N **uniformly in m**, so Abel
  summation now costs O(1) instead of the §11 penalty ✓.
* **Frozen phase.** e(ζ_{m_I}Q⁴) is common to all m ∈ I, so it can sit inside the main polynomial. The squared partial
  sum is Σ_s c_s e(ξ_m s), with c_s = Σ_{Q₁²+Q₂²=s, Q_i≤u, parity} e(ζ_I(Q₁⁴+Q₂⁴)). These coefficients do not depend
  on m ∈ I, and |c_s| ≤ r₂(s) ≤ 4τ(s).
  * The large sieve, by colouring, applies per band with multiplicity D_I.
  * Hölder over all O(Y) indices gives E_h ≪ W^{1/2}Y^{1/4}(Σ_I D_I)^{1/4} ✓.
  * Abel summation uses common Q endpoints for all m ✓.
* **Localised spacing, (11).**
  * Band I's points occupy v-length O(1+Z/J).
  * ET is applied per band with the **same** B. Titchmarsh needs length ≥ 1, and J ≪ 1 + Z/B ensures it. Band
    lengths are then ≳ B ≥ 1; a shorter band would cost O(1), which is the +J.
  * λ = lY/Z⁴ is unchanged, because v ≍ Z throughout.
  * Summing over bands: J·(Z/J)/B, J·(Z/J)(Bλ)^{1/14} and J·(Z/J)Δ are unchanged, and J·(Z/J)^{3/4}λ^{−1/14} gives the
    J^{1/4} factor ✓.
  * For Δ ≥ c₀ the total is (J+Z)(1+Δ) ≪ Z(1+Δ), since J ≪ Z when Z ≫ 1 ✓.
  * The +J is absorbed by Z/B = Z^{11/15}Y^{1/15} ✓.
  * The note's localisation hypothesis (hN²/W)²·max(1, Z^{4/15}) ≪ 1 implies (hN²/W)²B ≪ 1 because B ≤ Z^{4/15} for
    Y ≥ 1 ✓.
* **Signs and positivity.** §12 partitions the m-sum only **after** the absolute values in m that §7 already takes, and
  after the signed Q-average. It introduces no new positivity step, and nothing sign-sensitive is discarded ✓.
* **Ranges.**
  * The vertex check is valid on the triangle β ≥ α ≥ t, γ ≥ t. Every requirement is either an affine inequality or a
    max of affine functions ≤ affine (convex). min(d, j, r, 2r+γ−β) ≥ 0 is concave ≥ 0 and is also decided at the
    vertices.
  * min(α, γ) ≤ t uses the fibre divisor bound, and α > β follows by a ↔ b symmetry.
  * My own grid check (31-point barycentric grid, not only vertices) agrees.
  * Strict side conditions have uniform margins at all three vertices (data file).

## 3. Independent exponent optimisation

`scripts/z78_review_272857_lp.py` is written from the primitive quantities, not from the author's term list:
* P = n^{β−t} (detector) and H = n^{2(r+γ−t)} (diagonal);
* L = MNW/V, A, Y, T, σ, Z, Δ, J;
* the spacing bound recomputed **with its case split** and an optimised B, for derivative order k;
* constraints evaluated on a barycentric grid of the triangle.

In the §12 mode the per-band +J cost is kept inside D, rather than assuming the note's localisation hypothesis, and that
hypothesis is reported separately. Results:

| system | claimed | feasible at t₀+10⁻⁷ | infeasible at t₀−10⁻⁷ | binding at vertex 1 (t,1−2t,t) |
|---|---|---|---|---|
| §8 (D₀, K ≤ 0 required) | 20/63 | ✓ | ✓ | E_h term W^{1/4}Y^{1/2}h^{1/2} **and** quartic K ≤ 0 (both margin 0) |
| §11 (D₁, penalty K on all terms) | 1472/4637 | ✓ | ✓ | middle term + K |
| §12, (10) in every band (J^{1/4} on all) | 286/901 | ✓ | ✓ | middle term + K/4 |
| §12, localised (11) | **272/857** | ✓ | ✓ | middle term W^{19/60}Y^{27/60}h^{11/30}, margin 0; K = 4/857 > 0 |

Bisection thresholds agree to double precision. At vertex 1 with v = t/r, the binding inequality is
(19v+152)/60 ≤ v−2, i.e. v ≥ 272/41, giving t = v/(1+3v) = 272/857. At that point:
* K = 20r−3t = 4/857 > 0, so freezing is genuinely needed;
* the fifth term has slack 33/23996;
* the sextic margin is 212/857;
* the localisation margin is 556/12855.

**Which constraint changed.** The 20/63 system binds at vertex 1 in two places at once:
* the large-sieve term (multiplicity Z) gives t/4 + 3r ≤ t − 2r;
* bounded quartic residual gives 20r ≤ 3t.

272/857 relaxes **both**, and each relaxation is proved:
1. Z → Z^{11/15}Y^{1/15} + Z^{29/28}Y^{−1/14}, proved in §11 via ET and Titchmarsh 5.13.
2. The hard wall 20r ≤ 3t is replaced by freezing on J bands, at the cost of two new strict conditions (sextic and
   localisation), both proved in §12 and both strict at the optimum.

Without (2), (1) alone gives 1472/4637; without (1), (2) alone cannot go below 20/63.

**Robustness (my additions).** The order k = 4 of the derivative test is the best choice in this scheme:
* k = 2 and k = 3 give no gain over 20/63;
* k = 5 gives ≈ 0.317409 and k = 6 gives ≈ 0.317447.

The author's own script replays byte-identically to `data/z78/analytic_r3_lp.txt`, and `z78_analytic_r2.py` to
`analytic_r2_lp.txt`.

**R_M check.** On μ ∈ {0, 1/12, 1/6, 1/4, 3/10, 33/100}, (12) is feasible at t = θ + (1−3θ)μ + 10⁻⁷. It is binding only
at μ = 0. For μ > 0 my system is still feasible at t − 10⁻⁵. So **the M-exponent 231/857 is valid but not sharp for this
method** in the interior; that is optional, not a defect.

## 4. §13 transfers

* **M-uniformity.** With X = n/M:
  * the detector is (Mdk−n)² − 4k, with discriminant 16(Mdn+1) and strip length V/(Md);
  * Poisson gives L = MNW/V and phase ℓX/(Qd), hence A = Xℓh. With M = 4 this reproduces nℓh/4 exactly;
  * the prefactors 1/L and the ℓ-count cancel as in §7, so the goal N·W·X^{γ−j} = X^{2t} is unchanged;
  * p | M gives the linear local polynomial n² − 4k (DC zero, Gauss-sum modulus √p), so Σ_x|G|² ≪ Q² survives;
  * the only change in the exponents is d_* = d + μ ✓;
  * stationary-phase and derivative-test constants are absolute: the phase family is the same compact family in
    (σ, m/Y).
* **Range.** Interpolating in μ is valid, because the vertices are affine in μ and the constraints are jointly convex.
  The coalesced point μ = 1/3 has the strict side conditions with margins ≥ 1/3.
* **Elementary second term.** b(Mad−1) = n+a and (Mda−1)(Mdb−1) = Mdn+1 ✓. Mabd ≍ n with ratio ≥ 1/6 ✓, and
  R_M = 0 for X < 1/6 ✓. The two bounds cross at μ = 1/3, i.e. M = n^{1/4} ✓. The algebra
  X^θ M^{1−3θ} = n^θ M^{1−4θ} with 1−4θ = −231/857 ✓.
* **ES₅.** Native words are a subset of R₁-triples, so the bound is trivially the M = 1 case. It is an upper bound only,
  with no positivity claim ✓.
* **Explicit non-claims confirmed.**
  * N₂ at fourth-root U: min(U, n^θ) = U is vacuous, and the note says so.
  * f_II: R₄(p) ≤ f_II(p) is the wrong direction. Summing the c-slices costs θ + (2−3θ)/5 ≈ 0.527 > 2/5, so there is no
    replacement of n^{2/5}.
  * No exceptional-set or positivity claim is made.

## 5. §0 and the eight fixes requested by `REVIEW_ANALYTIC_WILD_2063_OPUS2.md`

| # | request | status |
|---|---|---|
| 1 | Scope opens with the headline | ✓ (now §§7–8 then §§11–12, §13, §§1–3/6) |
| 2 | Label split for GRH parts | ✓ ("§4 and §9 cap consequences separately CONDITIONAL on Dirichlet GRH") |
| 3 | Run at 20/63+η, keep the endpoint as a remark | ✓ (§8) |
| 4 | Hörmander uniformity clause, fixed K ⊃ critical points, W T^{−3/2} | ✓ (§7) |
| 5 | replay asserts γ+2r ≤ 2t and detector/diagonal; vertex-affinity statement | ✓ asserts added to r2 and r3 scripts; the affinity statement is in the r3 docstring only, not the r2 script (trivial) |
| 6 | "soft Abel loss"; higher moments do not help | ✓ (§8 end, §12 comparison) |
| 7 | cite second review; record declined split; remaining items form-only | partially: the review is cited and "keeping one lane note by request" is there. The R2 "do not promote yet" and "form-only" wording is absent, and the line still reads "Accepted with minor repairs, incorporated" for all reviews |
| 8 | parity split only for odd h | ✓ |

## 6. Defects (all MINOR)

1. **MINOR — §0 Review line.**
   * Problem: at merge time only one review of §§11–13 existed, yet the line reads "Accepted with minor repairs,
     incorporated" for all of them. AGENTS §3 requires two reviews for a record improvement.
   * Repair: cite this file as the second §§11–13 review. Spell out 2063_OPUS2 item 7 (R2 "do not promote yet", split
     declined, remaining items form-only).
2. **MINOR — §11 forward reference and citations.**
   * Problem: §11 applies "the fourth derivative test as quoted in §12". Erdős–Turán is used without a stated form.
   * Repair: move the Titchmarsh 5.13 statement into §11. Cite ET in a quoted form, e.g. Montgomery, *Ten Lectures*,
     ch. 1, Cor. 1.1, or Kuipers–Niederreiter Thm 2.5: #{x_i ∈ I} ≤ M|I| + M/(B+1) + 3Σ_{l≤B}l⁻¹|Σe(lx_i)|.
     State f⁽⁴⁾ = −(135/256)c^{−3/4}(v+η)^{−13/4} explicitly (fixed sign, two-sided bound).
3. **MINOR — §11 case split at Δ ≍ 1.** "Δ ≫ 1 … Δ ≪ 1" leaves the reader to note that D₀ is always valid. Repair: say
   "split at Δ = c₀; for Δ ≥ c₀ the old D₀ ≪ ZΔ suffices".
4. **MINOR — notation.**
   * The Titchmarsh quote in §12 uses "M" for the interval length, which clashes with §13's numerator M (and §6's
     M = [Q_i, Q_j]). Rename it, e.g. to 𝓁 or "length λ₀".
   * B also recurs from §§2/4; that is acceptable because it is local.
5. **MINOR — §11 "Y/Z = W/h² ≫ 1 throughout".** The argument never uses this, beyond the harmless observation that the
   spacing is < 1. Either say where it is used or drop it (the script assertion γ > 2j can stay).
6. **MINOR — §13, why M ≤ X^{1/3} also controls losses.** The n^δ losses (ℓ truncation, logs) are absorbed by strict
   margins measured in base X only because n = XM ≤ X^{4/3}. Say this in one sentence. It is the real reason the
   analytic range stops at μ = 1/3, besides the crossover.
7. **MINOR, optional — localisation hypothesis.** It is sufficient but not needed. Keeping the +J per band explicitly
   gives the same exponent (my script). The (12) exponent 231/857 is not optimal for μ > 0. Neither point needs a
   change.

**No FATAL, no MAJOR.**

## 7. Comparison with `REVIEW_ANALYTIC_WILD_R3_OPUS.md` (read after the above)

* **Agreement.** The first review and I agree on:
  * all three thresholds;
  * the −1/3 coefficient;
  * the validity of Titchmarsh 5.13 at k = 4;
  * J ≪ 1 + Z/B;
  * the frozen-complex-weight fourth moment;
  * vertex sufficiency;
  * M-uniformity;
  * the non-transfers.
* **Its form items, now applied.** Its 10 form items have since been applied:
  * Review/Scope lines;
  * §11 now derived via Titchmarsh instead of an exponent-pair citation;
  * J/Δ resets declared;
  * Taylor terms spelled out;
  * the triangle remark;
  * EXSET_I3 pointers;
  * f_II marked as exponent arithmetic;
  * a replay line;
  * the data-file header;
  * the decimal and the gain in STATUS delta.

  The one partial exception is its item 4: the data file now uses R_M, but the J/Δ clashes are only declared, not
  renamed.
* **New here.**
  * The §12 localisation hypothesis is unnecessary, and the M-exponent is non-sharp for μ > 0.
  * k = 4 is optimal among k = 2…6.
  * Grid (not just vertex) confirmation.
  * Explicit f⁽⁴⁾ and the case split at Δ = c₀.
  * The base-X versus n^δ margin explanation for §13.
  * An audit of the 2063_OPUS2 fix list.
* **Disagreements.** None of substance. One trivial slip in the first review: the f⁽⁴⁾ comparability ratio is
  (c₂/c₁)^{13/3}, not ^{13/4}, because v+η spans a ratio (c₂/c₁)^{4/3}. It is absolute either way.

## Bottom line

R(n) ≪_ε n^{272/857+ε} for every n ≥ 2 is **PROVED** (rel. Weil via z76 §2, uniform stationary phase, the additive large
sieve, r₂ ≤ 4τ, Erdős–Turán, and Titchmarsh Thm 5.13 with k = 4). The same holds for the uniform R_M bound (12) and
the ES₅ word-count corollary. With this second cross-lab review the §§11–13 record meets the AGENTS §3 two-review
gate for promotion, after the MINOR form repairs above. External priority remains unverified. ES is open.
