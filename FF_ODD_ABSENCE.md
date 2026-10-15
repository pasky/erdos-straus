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

**Theorem 1.4 (k = 1 Case A law; PROVED).** Let q = 3^r and let (a1', b1, K) be k = 1 Case A data (FF_STERILE_SMALL Lemma 7.2:
T^α ∥ a1 = T^α a1', a1', b1 monic, lc K = lc E ∈ {1, 2}, T ∤ a1'b1K, E = a1'b1K − 1, F = (a1 + b1)/E a polynomial) whose
cylinder lies on a slice u₀ = −E(0) ∉ F₃^*. Then E(0) = b1(0)/F(0) and
  E(0)^α = (−1)^{t + tκ + κ(1+α) + tα} · λ^{κ + 2β − α} · (lc K)^{α − t} ∈ F₃^*,
(t = deg z, λ = lc z, z := (F + b1)/a1', β = deg b1, κ = deg K); in particular **E(0)^{2α} = 1**.
*Proof.* E ≡ −1 (mod a1') and EF = T^α a1' + b1 give F + b1 ≡ 0 (mod a1'), so z is a polynomial, and
b1·K·F = T^α + z, F + b1 = a1'·z (DEPTH_ASPECT Lemma 2.3 (A0), (A3): pure algebra from E = a1'b1K − 1, EF = T^α a1' + b1).
At T = 0: E(0)F(0) = b1(0) ≠ 0 and E(0) ≠ 0 (E(0) = −u₀), so F(0) ≠ 0 and z(0) = b1(0)K(0)F(0) ≠ 0. Lemma 1.1 with
(M, W, C, G, V, s) = (K, b1, F, a1', z, α) gives the formula (μ_W = 1, μ_M = lc K). lc K ∈ F₃^*. For λ: lc(T^α a1' + b1) ∈ {1, 2}
(sum of monics; deg F = α − β − κ ≥ 0 forces α + λ_deg ≥ β), so lc F ∈ F₃^*; hence λ = lc(F + b1) ∈ F₃^* unless deg F = β
and lc F = −1 (top coefficients cancel). In that case deg F = α − β − κ = β, i.e. κ + 2β − α = 0, and λ does not occur.
So the right side lies in F₃^* = {±1}. ∎
*Check (EVIDENCE):* `zc_caseA_enum` (fz1_caseA_enum + dump), all Case A data unfiltered: q = 9, α ≤ 6 (745 data, plus a partial
α = 7) and q = 27, α ≤ 4 (+ partial α = 5): E(0)^{2α} = 1 in every case; the cancellation case λ ∉ F₃ occurs (4 data at q = 9) and
is harmless as proved. q = 9 distribution: odd α only E(0) = 1; α ≡ 2 (4): {1, ±i}; α ≡ 0 (4): all values ≠ −1 — the same
shape as Case B.

**Corollary 1.5 (the vanishing law; PROVED).** For q = 3^r, on the slices u₀ ∈ F_q^* ∖ F₃^* every k = 1 linear family (Case A of
depth α, or Case B of parameter s; FF_STERILE_SMALL Prop 6.1 handles depth 1) has cylinder in a slice with (−u₀)^{2n} = 1,
n = α resp. s. Hence the slice u₀ carries **no family of level n unless ord(−u₀) ∣ 2n**. For q = 27 the first possible level is
n = 13 (ord(−u₀) ∈ {13, 26} for −u₀ ∉ F₃); for q = 9 the slices u₀ = ±i need 2 ∣ n and the four primitive slices
(u₀⁴ = −1) need 4 ∣ n.
This explains both O220 observations exactly (q = 27: nothing for s ≤ 12, α ≤ 4; q = 9: nothing at odd s).
*Interpretation.* The law is a reciprocity statement: the "local symbol" w(0)/C(0) of the curve-data at T = 0 is a product of
local symbols at the other places (roots of v, w, m', and ∞), where the defining equation makes every symbol a power of T^s.
Galois descent plays no role (the law is the same over every field); the F₃-flavour comes only from lc's ∈ {±1}.

## 2. Closing q = 9, k = 1

**Lemma 2.1 (union bound on a sub-family of slices; PROVED, as FF_STERILE_SMALL §7).** Let P ⊂ F_q^* ∖ F₃^* be a set of slice
labels u₀. If Σ_{Case B tuples with −E(0) ∈ P} q^{−⌈(s−1)/2⌉} + Σ_{Case A data with −E(0) ∈ P} q^{−α} < |P|, then some slice u₀ ∈ P
has covered relative measure < 1, so O(q, T) ≠ ∅ and ES_q(T, ·) has no finite linear covering.
*Proof.* The covered measure of the slice u₀ is at most the sum of the masses of the cylinders lying in it (FF_STERILE_SMALL §7:
on u₀ ∉ F₃^* every cylinder has depth ≥ 2 and the stated relative mass; a family lies in exactly one slice, u₀ = −E(0)). Sum
over u₀ ∈ P and average. The rest (positive uncovered measure ⇒ O ≠ ∅ ⇒ no finite linear covering) is verbatim §7 of
FF_STERILE_SMALL. ∎

**Choice of P at q = 9.** F₉^* ∖ F₃^* = {±i} ∪ P₈, P₈ := {u₀ : u₀⁴ = −1} (the four primitive 8th roots; −P₈ = P₈). By Corollary
1.5 a family of level n lies on P₈ only if 4 ∣ n, and (Case B) only if its pattern has ε(s; a, z, t) = (−1)^{s/4} (since
E(0)^s = (E(0)⁴)^{s/4} = (−1)^{s/4} for E(0) ∈ P₈). Exact masses (s ≤ 12, from §1's dump): the six slices carry 3.927 in total,
of which 2.168 on {±i} (> 1 per slice: the union bound cannot work there) and 1.759 on P₈ (0.44 per slice). So P = P₈ with
budget |P| = 4.
