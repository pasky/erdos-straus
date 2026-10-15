# Hostile review R240 of FF_ODD_ABSENCE.md (O226) — round 1

Reviewer: R240 (side agent, branch side-agent/review-ff-odd). Merged author branch side-agent/ff-odd-absence at review start.
From-scratch scripts: `scripts/review_r240_*`.

## Summary verdicts
(filled in as the review proceeds)

## Lemma 1.1 (root-product identity)
Re-derived independently. At a root β of V (multiplicity counted), C(β) = −W(β) and M(β)W(β)C(β) = β^s, so −M(β)W(β)² = β^s;
∏β_i = (−1)^t V(0)/λ. Resultant step: ∏_i W(β_i) = μ_W^t ∏_{i,j}(β_i − γ_j) = μ_W^t (−1)^{ta} λ^{−a} ∏_j V(γ_j), and V(γ_j) = −γ_j^s
because (MWC)(γ_j) = 0; ∏γ_j = (−1)^a W(0)/μ_W. Same for M. Substituting and cancelling M(0)^s via V(0) = M(0)W(0)C(0) gives
  (W(0)/C(0))^s = (−1)^{ts + t + tz + z + zs} μ_M^{s−t} μ_W^{2(s−t)} λ^{z + 2a − s},
which is the stated formula. Roots of W, M are nonzero (W(0), M(0) ≠ 0), so V(γ) = −γ^s ≠ 0 and no division by zero occurs;
G is used only through C(β) = −W(β). Valid over any field, including a = 0 or t = 0 (empty products). **SOUND.**

## Theorem 1.2 (k = 1 Case B law)
Re-derived. Lemma 1.1 with (M, W, C, G, V) = (m', w, C, g', v), μ_M = μ_W = 1. The λ-exponent z + 2a − s equals a − b because
z + a + b = s (FF_STERILE_SMALL Lemma 7.1(i), reviewed in (J)56); λ = lc v = lc(w + C) (g' monic) is 1 for a ≠ b and 2 for a = b,
where the exponent vanishes. E(0) = w(0)/C(0): from Ev = T^s + m'w² at 0 and v(0) = m'(0)w(0)C(0) (re-derived:
E := m'g'w − 1 satisfies EC = g'T^s + w, Ev = T^s + m'w², EE' = 1 + T^s m'g'², E' = m'g'C − 1). E(0) ≠ −1 since w(0) + C(0) =
g'(0)v(0) ≠ 0. The R-O226 λ-repair is correct (λ = 2 is not ±1 for q ≡ ±1 mod 3 with q ≠ 3^r; harmless because the exponent is 0).
The q = 9 filter code (`eps_ok` in zc_sum9.c) uses the char-3 form with an extra (−1)^{z+s} for a = b; z + s = 2(z + a) is even then,
so it coincides with ε. **SOUND.**

## Corollary 1.3 / Corollary 1.5 (vanishing law)
Group theory checked: F₉^* cyclic of order 8, −(±i) = ∓i has order 4 ⇒ 2 | n; P₈ (order 8, −P₈ = P₈ since −1 = ζ⁴) ⇒ 4 | n.
F₂₇^*: elements off F₃^* have order 13 or 26 ⇒ 13 | n. On P₈, E(0)^s = (E(0)⁴)^{s/4} = (−1)^{s/4}, giving the pattern filter
ε = (−1)^{s/4}. On ±i at s ≡ 2 (4): E(0)^s = E(0)² = −1, so only ε = −1, as stated. q = 81: (q−1)/2 = 40 = 2³·5, "s prime to 10"
correct; q = 243: 121 = 11², correct. Depth-1 families (Prop 6.1 of (J)56) all have u₀ ∈ F₃^*. **SOUND.**

## Theorem 1.4 (k = 1 Case A law)
Re-derived. From E = a1'b1K − 1 and EF = T^α a1' + b1: b1KF = (E+1)F/a1' = (T^α a1' + b1 + F)/a1' = T^α + z and F + b1 = a1'z
(z := (F + b1)/a1' is a polynomial: EF = T^α a1' + b1 ≡ b1 and E ≡ −1 (mod a1') give −F ≡ b1 (mod a1')). Lemma 1.1 with (M, W, C, G, V, s) = (K, b1, F, a1', z, α):
μ_M = lc K, μ_W = 1, exponents match the stated formula. z(0) = b1(0)K(0)F(0) ≠ 0 and F(0) = b1(0)/E(0) ≠ 0 as claimed. λ-argument:
lc(T^α a1' + b1) ∈ {1, 2} (sum of monics, never cancels for q odd), lc F = that / lc E ∈ F₃^*; λ = lc(F + b1) ∈ F₃^* unless
deg F = β and lc F = −1, in which case deg F = α − β − κ = β makes the λ-exponent κ + 2β − α = 0. (deg F = α − β − κ uses
Lemma 7.2(a) of (J)56: patterns β > α + deg a1' do not occur.) **SOUND** (q = 3^r is needed only for lc's ∈ F₃^* to give ±1).

## Proposition 1.6 (sharpness)
Re-derived line by line: m' = D + 1 monic of degree z = deg D ≥ 1 (so the +1 does not touch the leading term), m'(0) = D(0) + 1 ≠ 0;
C = (T^s+1)/D monic of degree s − z ≥ 1, D(0)C(0) = 1; (D+1)C = T^s + 1 + C = T^s + v; w + C = v; v(0) = (1 + D(0))/D(0) ≠ 0;
pattern (a, z, y, t) = (0, deg D, 0, s − deg D), b = t; E(0) = D(0). For D = T − ρ, ρ^s = −1: ρ ≠ 1 since q is odd. **SOUND** as a
statement about tuples (B^{k=1}). See MINOR m-1 for the step "tuple ⇒ family".

## Corollary 1.7 (k ≥ 2 parity law)
Re-derived. In (B) of FF_STERILE_PUSH, w = Tw₁, C = TC₁, v = T²v₁, deg w₁ = a − 1, deg C₁ = b − 1, deg v₁ = t − 2, s ≥ 3 (a ≥ 1,
t ≥ 2) so s' = s − 2 ≥ 1 and v₁(0) ≠ 0. w₁(0) = −C₁(0) from w₁ + C₁ = Tg'v₁. λ-exponent z + 2(a−1) − (s−2) = a − b. Parity:
z even ⇒ s ≡ t(1+s) ⇒ s, t even; z odd ⇒ 1 + ts ≡ 0 ⇒ s, t odd; conversely both cases satisfy the identity. **SOUND.**

## Lemma 2.1 (union bound on a sub-family of slices)
The criterion of (J)56 §7 is Σ(masses) < q − 3 with every slice normalised to relative measure 1 (cylinder of depth N + 1 inside
a depth-1 slice has relative mass q^{−N}, N ≥ ⌈(s−1)/2⌉ for Case B, = α for Case A). Each family's cylinder lies in exactly one
slice (depth ≥ 2 off F₃^*, Cor 6.2 of (J)56), so Σ_{u₀∈P} covered(u₀) ≤ Σ_{families on P} mass < |P| forces some u₀ ∈ P to have
covered relative measure < 1; the countable union of all valid cylinders then misses a positive-measure set, so O(9, T) ≠ ∅.
Restricting to P only drops nonnegative terms of other slices — no hidden normalisation issue. The w ↔ C swap (mult 2 for a < b)
maps E(0) ↦ 1/E(0) and preserves (s, z, t) hence ε; P₈ is closed under inversion, so counting oriented tuples with
E(0) ∈ P₈ and doubling is exact. Case A data counted on all six (or all) slices are upper bounds for P₈. The Frobenius remark is
correct (coefficient Frobenius is a measure-preserving bijection of the slice set mapping valid families to valid families since
A = T ∈ F₃[T]); it is not used by the proof. **SOUND.**

## Theorem 2.2 (q = 9, A = T: no finite linear covering)
**Logic.** Lemma 2.1 with P = P₈, |P| = 4. Only 4 | n survives (Cor 1.5), and for Case B only ε(s; z, t) = (−1)^{s/4} (Thm 1.2);
Case A only 4 | α (Thm 1.4). All filters re-derived above. Filter code: `eps_ok` (zc_sum9.c) and `zc_eps_ok` (zc_enum.c) agree
with ε (the extra a = b term is vacuous, z + s even); the slice filter `SLICEF == 2` tests E(0)⁴ ≠ 1 with E(0) computed as
m'(0)g'(0)w(0) − 1 (= E(0), E = m'g'w − 1), which on F₉^* ∖ {±1, ±i} is exactly P₈; `zc_caseA9.py` differs from the reviewed
`fz1_caseA.py` only by `if al % MOD: continue` and fail-closed parsing (diffed).

**Independent recount (from scratch; `scripts/review_r240_enum.gp` + `review_r240_enum.py`, PARI/GP factoring over F₉, five
routes, every candidate re-verified against (B^{k=1}) from scratch; ALL patterns a ≤ b, not only ε-compatible ones):**

| s | patterns (all) | tuples a ≤ b | P₈ tuples | P₈ in ε-incompatible patterns | P₈ mass | author |
|---|---|---|---|---|---|---|
| 4 | 27 | 106 | 70 | 0 | 1.629630 | 1.62963, 70 |
| 8 | 125 | 1 146 | 658 | 0 | 0.1164457 | 0.11645, 658 |
| 12 | 343 | 6 378 | 3 530 | 0 | 0.01317173 | 0.01317, 3 530 |
| 16 | 729 | 46 818 | 26 570 | 0 | 6.319645·10⁻⁴ | 6.3·10⁻⁴, 26 570; 514 incompatible patterns empty |

Per-pattern P₈ counts equal the author's `data/zc/p_{4,8,12,16}.txt` line by line (0 mismatches, no missing pattern).
Cross-route consistency: s = 4 all 5 routes on all 27 patterns; s = 8 every route of cost ≤ 9⁵ (125 patterns); s = 12 every route
of cost ≤ 9⁴ (226 of 343 patterns run by ≥ 2 routes): 0 disagreements. Every tuple found also satisfied E(0)^s = ε (0 law failures,
≈ 54 000 tuples). s = 4 total 106 also equals the independent Python enumerator (`review_r240_law.py`, a third method).
**s = 20:** recounted the 700 ε-compatible patterns of cost ≤ 9⁵ (factoring routes cost +1): 0 mismatches with `p_20.txt`; all
138 136 tuples found are on P₈ (as the law predicts: at s = 20, ε = −1 forces E(0)⁴ = −1). [cost-6 extension: see below.]

**Case A α = 4:** independent enumeration via z = (F + b1)/a1' and ordered factorisations T⁴ + z = b1·K·F (`caseA()` in
the GP file, `review_r240_caseA.py`): per-pattern six-slice counts equal `data/zc/caseA9_4.txt` (325 data, six-slice mass
0.04084743; P₈ alone 0.02652); α = 1, 2, 3 also equal; E(0)^{2α} = 1 on all data.

**Re-summation (`scripts/review_r240_certify.py`, own pattern loop/filter/weights; route-bound values from the reviewed (J)56
`pattern_bound1` via `review_r240_bounds.c`; fails closed on missing/duplicate patterns, law failures, P₈ tuples in incompatible
patterns):**
* Variant A (my counts s ≤ 16 and s = 20 cost ≤ 5, author's s = 20 counts for the rest, SKIPs route-bounded): Case B
  2.9670390099 — identical to the author's figure; tail (re-run `fz1_tail 2 80 8 1e-3 1 1`) 0.025752412; Case A (re-run
  `zc_caseA9.py`) 0.17018962 + 2.7363·10⁻⁴; **certified total ×1.01 = 3.194887 < 4.**
* Variant B (no author count used at s = 20: only my recounted patterns are exact, all other s = 20 patterns route-bounded):
  Case B 3.5850789, **total ×1.01 = 3.819107 < 4.** So the certificate does not depend on the un-cross-checked part of the
  author's s = 20 enumeration (the author's trust point).

**Other checks.** Cor 1.7's archived-data claim reproduced from `data/fz/enum9/e_{3..22}.txt.gz` with my own awk filter
(z ≡ t ≡ s mod 2): 1 830 compatible patterns (793 nonempty), 5 210 violating, all with count 0. Small-q law checks
(`review_r240_law.py`, own GF(q) tables and division-route enumerator, w ↔ C orientation a ≤ b): q = 5 (s ≤ 6), 7 (s ≤ 5),
9 (s ≤ 5), 27 (s ≤ 3): Case B unsimplified Lemma 1.1 form, simplified ε form, λ = 1/2 rule, degree identity z + a + b = s,
y + t = max(a, b): 0 failures; k ≥ 2 tuples (q = 5 s ≤ 7, q = 9 s ≤ 5; few tuples) satisfy z ≡ t ≡ s; Case A (all (a1', b1, K)
of total degree ≤ 3, α ≤ 4, lc K ∈ {1, 2}): Lemma 1.1 form and E(0)^α ∈ {±1} at q = 9, 27: 0 failures; Prop 1.6 construction
for every monic D | T^s + 1 (s ≤ 8): 0 failures. With the GP enumerator: q = 27, s = 13 (160 patterns of cost ≤ 27³): 926 635
tuples, 855 378 with E(0) ∉ F₃^*, law holds for all; q = 27, s = 12 (cost ≤ 27^{3.5}): 99 tuples, none off F₃^*; q = 7, s = 9 and
q = 5, s = 10 (cheap patterns): law holds. Distribution at q = 9, s ≤ 5 (Python): odd s only E(0) = 1; s = 2: {1, ±i}; s = 4:
all values except −1 — as the author reports. Not re-checked: the Cor 1.7 route-sum reductions (41.87 → 11.24, 1466.7 → 389.2;
EVIDENCE, not used) and the q = 27, s = 13 "all 24 classes occur" count (EVIDENCE).

## Defects

No FATAL, no MAJOR.

* **m-1 (MINOR, editorial; header lines 3–4).** The R-O226 insertion split the "Builds on" sentence: line 4 starts with a
  dangling "FF_STERILE_PUSH.md ((J)51), DEPTH_ASPECT.md Lemma 2.3 (Case A identities)." Repair: move it back after
  "Builds on FF_STERILE_SMALL.md ((J)56; …)".
* **m-2 (MINOR, notation; Thm 1.4).** λ denotes lc z here, but in (J)56 Lemma 7.2 and in `zc_caseA9.py`/`caseA9_4.txt` λ ("lam")
  is deg a1'; the proof then writes "λ_deg". t and z are also reused (deg z, the polynomial z vs. deg m'). Repair: call lc z ν
  (say) and write deg a1' explicitly.
* **m-3 (MINOR, citation; Thm 1.4 proof).** "deg F = α − β − κ" needs Lemma 7.2(a) of (J)56 (patterns β > α + deg a1' do not
  occur; otherwise deg(T^α a1' + b1) = β). Repair: cite it at that step.
* **m-4 (MINOR, citation; Prop 1.6 last sentence).** "carries a level-s Case B family" needs tuple ⇒ family. Repair: cite the
  converse in FUNCTIONFIELD_ES3 Lemma 1.1 with L' = m'g' (so g' | L'), E = m'g'w − 1 (monic, E·E' = 1 + T^s m'g'² = D),
  j = N = s − 1, γ = 0 (s = N + 1 + γ); then E ≡ −1 (mod L') and the cylinder is u ≡ −E (mod T^s).
* **m-5 (MINOR, status bookkeeping).** The combined statement "ES_q(T) has no finite linear covering for every q = 3^r, r ≥ 2"
  (Thm 2.2 + (J)56 Thm 8.1) is made only in the agent report; FF_ODD_ABSENCE should state it as a corollary, and on merge
  FF_STERILE_SMALL §7 ("q = 9 (k = 1) is not closed") and §8 ("Open: … q = 9 with k = 1") need a forward pointer.
* **m-6 (MINOR, trust point now discharged).** The s = 20 exact counts were not cross-checked by the author. R240's recount
  (700 + cost-6 patterns, 0 mismatches) and variant B (total 3.819 < 4 without any author s = 20 count) close this; suggest
  citing this review in the Thm 2.2 proof.
