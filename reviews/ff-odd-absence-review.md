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
