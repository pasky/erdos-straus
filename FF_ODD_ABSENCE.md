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

**Proposition 1.6 (the law is sharp on the classes u₀^s = −1; PROVED).** Let q be odd, s ≥ 2, and D a monic divisor of T^s + 1
with 1 ≤ deg D ≤ s − 1 and D(0) ≠ −1. Then m' = D + 1, w = 1, g' = 1, C = (T^s + 1)/D, v = C + 1 is a k = 1 Case B tuple of
level s (pattern a = 0, z = deg D, y = 0, t = s − z) with E(0) = D(0), i.e. on the slice u₀ = −D(0). In particular (D = T − ρ):
**every u₀ ∈ F_q^* with u₀^s = −1 carries a level-s Case B family.**
*Proof.* (D + 1)C = T^s + 1 + C = T^s + v and w + C = 1 + C = v = g'v; m' = D + 1 is monic of degree z ≥ 1 with m'(0) = D(0) + 1 ≠ 0;
C is monic of degree s − z ≥ 1 with C(0) = 1/D(0); v = C + 1 has lc 1 (= λ, a < b) and v(0) = (1 + D(0))/D(0) ≠ 0. E(0) = w(0)/C(0)
= D(0). For D = T − ρ: D(0) = −ρ ≠ −1 since ρ^s = −1 ≠ 1 = 1^s. ∎
*Exact scope (EVIDENCE beyond Prop 1.6).* Theorem 1.2 says level s can reach only u₀ with u₀^{2s} = 1, u₀ ≠ 1 (E(0) ≠ −1);
Prop 1.6 reaches all u₀ with u₀^s = −1. The enumerations show that the remaining allowed classes (u₀^s = 1, u₀ ≠ 1) are also
populated whenever allowed: q = 9, s ≤ 12 (all allowed E(0) values occur at every level, §1 table); q = 5, 7, s ≤ 9 (same);
q = 27, s = 13 (first allowed level; `zc_enum 27 13 13 4.5 0 1 3 1 1`, patterns of cost ≤ 27^{4.5} only): 118 443 tuples off
F₃^*, and all 24 classes u₀ ∉ F₃^* occur (12 with E(0) of order 13, 12 of order 26). So for q = 27 the first level with families
off F₃^* is exactly 13, and for q = 9 the populated classes are: none at odd s; exactly {±i} at s ≡ 2 (4); all six at s ≡ 0 (4)
(checked s ≤ 12; for s ≡ 2 (4) and P₈ at s ≡ 4 (8) also by Prop 1.6, ρ = ±i resp. ρ ∈ P₈).

**Corollary 1.7 (parity law for k ≥ 2; PROVED).** For q odd and a Case B tuple (B) of FF_STERILE_PUSH (k ≥ 2; m'w₁C₁ = T^{s−2} + v₁,
w₁ + C₁ = Tg'v₁, T ∤ m'w₁C₁v₁) of pattern (s; a, z, y, t): w₁(0) = −C₁(0) (from w₁ + C₁ = Tg'v₁ at T = 0), so Lemma 1.1 with
(M, W, C, G, V, s) = (m', w₁, C₁, Tg', v₁, s − 2) gives the **pattern parity law**
  (−1)^{s'} = (−1)^{t' + t'z + z(1+s') + t's'} · λ^{z+s'},  s' = s − 2, t' = t − 2, λ = −1 iff a = b;
patterns violating it are empty. *Check:* the archived exact q = 9 counts `data/fz/enum9/e_{3..22}.txt.gz` (O220/R221): all 5 210
violating patterns have count 0 (1 830 compatible patterns). *Effect on the route-bound sums* (`scripts/zc_sum_k2.c`, = fz_sum with
the filter; filter off reproduces fz_sum): q = 9, s ≤ 80: 41.87 → 11.24; q = 3, s ≤ 120: 1466.7 → 389.2 (the s₀ of FF_STERILE_SMALL
§5.3, where the bound tail drops below 0.5, moves from 84 to 74, tails up to s = 160). This does not rescue union bounds at q = 3 (they fail
even with exact counts), but it is a free factor ≈ 4 in every k ≥ 2 bound sum.

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

**Theorem 2.2 (no finite linear covering of ES₉(T); PROVED, computer-assisted, O216 certification standard plus exhaustive
enumeration).** For q = 9 and A = T (k = 1), O(9, T) ≠ ∅: ES₉(T, ·) has no finite linear covering. More precisely the covered
relative measure summed over the four slices u₀ ∈ P₈ (u₀⁴ = −1) is ≤ 3.195 < 4, so some u₀ ∈ P₈ has positive uncovered measure.
(The coefficient Frobenius x ↦ x³ maps valid families on u₀ to valid families on u₀³ with the same cylinder masses, since
A = T is defined over F₃; so the covered measure is constant on the orbits {ζ, ζ³}, {ζ⁵, ζ⁷}, and both slices of one orbit
have covered measure < 1.)
*Proof.* Lemma 2.1 with P = P₈. By Corollary 1.5 only levels n ≡ 0 (mod 4) and (Case B) only patterns with
ε(s; a, z, t) = (−1)^{s/4} contribute. `scripts/zc_certify9.sh` (log `data/zc/certify9_k1.txt`):
* Case B, 4 ≤ s ≤ 80, 4 ∣ s (`zc_sum9.c`): exact P₈-counts for s = 4, 8, 12, 16 (all compatible patterns) and s = 20 (933 of 950
  compatible patterns exact; 17 patterns timed out at 60 s each and are bounded by the routes, mass 0.0993), produced by `zc_enum`
  (fz1_enum + slice filter E(0)⁴ ≠ 1 + pattern filter; per-pattern driver `zc_drive.py` for s = 20): exact mass 1.759959
  (s = 4: 1.62963, s = 8: 0.11645, s = 12: 0.01317, s = 16: 6.3·10⁻⁴, s = 20: 8.0·10⁻⁵); route bounds (fz1_sum.c `pattern_bound1`,
  FF_STERILE_SMALL Lemma 7.1, unchanged) for the rest: total 2.9670390;
* tail s > 80: `fz1_tail 2 80` (all patterns, all slices, so an upper bound) ≤ 0.025752 (183 363 boxes, none failed);
* Case A (`zc_caseA9.py`, fz1_caseA.py restricted to 4 ∣ α by Theorem 1.4; α = 4 from the exact six-slice counts of
  `fz1_caseA_enum`, an upper bound for P₈; α ≤ 40 exact rationals, tail Lemma 7.2(b)) ≤ 0.170463.
Certified total ×1.01 = 3.1949 < 4. ∎
*Remark (what did the work).* Without the law the k = 1 bound at q = 9 is 396 (s ≤ 80, all routes); the odd levels carry 2/3 of it.
On P₈ the law removes odd s, s ≡ 2 (4), and at s ≡ 0 (8) the patterns with ε = −1 (s = 16: bound 8.48 → 2.12; s = 24: 1.74 →
0.51); exact enumeration at s ≤ 20 then removes all but 1.11 (s ≥ 24) of the bound mass.
*Validation (EVIDENCE).* (i) Theorem 1.2/1.4 checks of §1. (ii) Unfiltered dump s ≤ 12: the P₈-filtered, pattern-filtered counts
equal the P₈ part of the full dump (70, 658, 3530 tuples at s = 4, 8, 12). (iii) s = 16 with the pattern filter off: all 514
incompatible patterns have 0 tuples on P₈ (26 570 tuples, all in compatible patterns). (iv) Cross-method (candidate-search routes
M2, M3, M5 forced, cost ≤ 9^{6.5}) vs the auto (factoring) counts: s = 12: 214 of 237 patterns covered (cost ≤ 9^{8.5}), 0 mismatches; s = 16: 85 of
215, 0 mismatches; s = 8 totals agree (658) for M2, M3, M5. (v) Independent Python brute force `zc_brute.py` (q = 9, s ≤ 5):
per-pattern P₈ counts equal zc_enum at s = 4; law failures 0. (vi) `zc_certify9.sh 1` regenerates s ≤ 16 and Case A α ≤ 4
byte-identically.
