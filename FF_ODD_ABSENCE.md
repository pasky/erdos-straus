# FF_ODD_ABSENCE — the odd-r / odd-s absence on the A = T slices, explained (O226, wave Z-c)

Status: checkpoint 1 (O226). Builds on FF_STERILE_SMALL.md ((J)56; §§6–8: k = 1, slices u₀ ∉ F₃^*, tuples (B^{k=1})),
FF_STERILE_PUSH.md ((J)51), DEPTH_ASPECT.md Lemma 2.3 (Case A identities). Scripts `scripts/zc_*`.

## 0. Iteration log

* (I1) Unfiltered dump of all k = 1 Case B tuples at q = 9, s ≤ 12 (`zc_enum`, a copy of fz1_enum with a tuple dump), tabulated
  by E(0): odd s ⇒ E(0) = 1 only; s ≡ 2 (4) ⇒ E(0) ∈ {1, ±i}; s ≡ 0 (4) ⇒ every E(0) ≠ −1. Guess: E(0)^{2s} = 1. At q = 27,
  μ_{2s} ∩ F₂₇^* = {±1} unless 13 ∣ s — exactly the O220 "no tuples s ≤ 12". At q = 7 (s = 3, 6, 9) all of μ₆ ∖ {−1} occurs.
  The quadratic-reciprocity guess (Jacobi symbols) only gives χ(E(0)) and cannot explain q = 27; the right tool is a
  **product over roots** (Weil reciprocity for T against the curve of the tuple), which gives E(0)^s = ±1 exactly.

## 1. The root-product law (PROVED)

**Lemma 1.1 (root-product identity; PROVED, any field).** Let K be a field, s ≥ 1, and M, W, C, G, V ∈ K[T] nonzero with
  M·W·C = T^s + V,   W + C = G·V,   V(0) ≠ 0.                                                     (R)
Let z, a, t be the degrees of M, W, V and μ_M, μ_W, λ their leading coefficients. Then W(0), C(0), M(0) ≠ 0 and
  (W(0)/C(0))^s = (−1)^{t + tz + z(1+s) + ts} · λ^{z + 2a − s} · μ_M^{s−t} · μ_W^{2(s−t)}.
*Proof.* At T = 0: M(0)W(0)C(0) = V(0) ≠ 0. Work in an algebraic closure; V = λ∏_{i≤t}(T − β_i), all β_i ≠ 0. At each β = β_i:
M(β)W(β)C(β) = β^s and C(β) = −W(β), so −M(β)W(β)² = β^s. Multiply over i:
  (−1)^t ∏M(β_i) (∏W(β_i))² = (∏β_i)^s = ((−1)^t V(0)/λ)^s.                                         (1)
For a root γ of W (or of M), (R) gives V(γ) = −γ^s. With W = μ_W∏_{j≤a}(T − γ_j):
  ∏_i W(β_i) = μ_W^t ∏_{i,j}(β_i − γ_j) = μ_W^t (−1)^{ta} ∏_j ∏_i(γ_j − β_i) = μ_W^t (−1)^{ta} λ^{−a} ∏_j V(γ_j)
            = μ_W^t (−1)^{ta} λ^{−a} (−1)^a (∏γ_j)^s = μ_W^t (−1)^{ta+a} λ^{−a} ((−1)^a W(0)/μ_W)^s,
and likewise ∏_i M(β_i) = μ_M^t (−1)^{tz+z} λ^{−z} ((−1)^z M(0)/μ_M)^s. Insert into (1), cancel M(0)^s (V(0) = M(0)W(0)C(0)) and
solve for (W(0)/C(0))^s; the (−1)^{2(…)} factors of the squared W-product drop. ∎
(Equivalently: Weil reciprocity on P¹ for the functions T and W/C restricted to the divisors of V, W, M — the "local symbol at
0" W(0)/C(0) is paid for by the symbols at ∞ and at the roots, where (R) makes everything a power of T. We use the elementary form.)

**Theorem 1.2 (k = 1 Case B law; PROVED).** Let q be odd and (m', g', w, C) a k = 1 Case B tuple (B^{k=1}) of parameter s
(FF_STERILE_SMALL §6: m'wC = T^s + v, w + C = g'v, m', g', w, C monic, T ∤ m'g'wCv; z, a, y, t degrees; λ = lc(v) = lc(w + C)
∈ {1, −1}, λ = −1 iff a = b). Its cylinder lies on the slice u₀ = −E(0) with E(0) = w(0)/C(0) (from Ev = T^s + m'w² at T = 0),
and
  E(0)^s = ε(s; a, z, t) := (−1)^{t + tz + z(1+s) + ts} · λ^{z + s}  ∈ {±1}.
In particular **E(0)^{2s} = 1: E(0) ∈ μ_{2s}(F_q) = μ_{gcd(2s, q−1)}**, and E(0) ≠ −1 (E(0) = −1 means w(0) + C(0) = 0, i.e.
T ∣ g'v).
*Proof.* Lemma 1.1 with M = m', W = w, G = g', V = v (μ_M = μ_W = 1, λ² = 1). ∎
*Check (EVIDENCE, `scripts/zc_law_check.py` on the dump of `zc_enum`; tuples re-verified against (B^{k=1}) independently in
Python, `scripts/zc_field.py`):* q = 9, s ≤ 12: 8 915 tuples; q = 5, 7, 27, s ≤ 9: 305, 645, 340 tuples; 0 failures of the exact sign
formula. (Distribution of E(0) at q = 9: odd s only E(0) = 1; s ≡ 2 (4): {1, ±i}; s ≡ 0 (4): all eight values except −1 — the
law is sharp at q = 9, s ≤ 12.)

**Corollary 1.3 (vanishing theorem for Case B; PROVED).** Let q = 3^r. On the slices u₀ ∈ F_q^* ∖ F₃^* there is no k = 1 Case B
tuple of parameter s with gcd(s, (q − 1)/2) = 1. More precisely a tuple of pattern (s; a, z, y, t) can lie on the slice u₀ only if
(−u₀)^s = ε(s; a, z, t).
*Proof.* μ_{gcd(2s, q−1)} = μ₂ = F₃^* when gcd(2s, q − 1) = 2, i.e. gcd(s, (q−1)/2) = 1. ∎
Instances: q = 9 ((q−1)/2 = 4): **every odd s is empty**; s ≡ 2 (mod 4) only on u₀ = ±i, and only patterns with ε = −1;
s ≡ 0 (mod 8): only patterns with ε = +1. q = 27 ((q−1)/2 = 13): every s with 13 ∤ s is empty (explains O220's "no tuples
s ≤ 12"). q = 3^r with r odd: (q−1)/2 is odd, so parity plays no role and only s sharing a factor with (q−1)/2 survive; e.g. q = 243
((q−1)/2 = 121): only 11 ∣ s. q = 81 ((q−1)/2 = 40): every s prime to 10 is empty.
