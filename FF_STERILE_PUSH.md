# FF_STERILE_PUSH — pushing the large-q no-covering theorem down, and the q = 3 sterile point (O216, wave Y-e)

Status: checkpoint 2 (O216): Theorem 3.1 (r ≥ 4) PROVED (computer-assisted; R218 repair m-5: one label throughout — floating point with a ×1.01 margin, cross-checked in exact rationals by R218 `scripts/review_fs2_exact.py`); self-reviewed, repairs applied; hostile reviews R217 (`reviews/ff-sterile-push-review.md`) and R218 (`reviews/ff-sterile-push-review-2.md`): no FATAL/MAJOR, minors repaired. **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in DISCOVERIES.md.
Builds on DEPTH_ASPECT.md §2 (Thm 2.5 = (J)26; reviews R178, R187), FUNCTIONFIELD_ES3.md (O173 Lemmas 1.1, 2.1, 2.3),
FUNCTIONFIELD_ES2.md (§0.1 compactness criterion, §0.2 Case A), FF_STERILE_PROOF.md (O179). Scripts `scripts/fs_*`.

Setting (as in DEPTH_ASPECT §2): q odd, A = T^k, k ≥ 2, c ∈ F_q^*, the c-slice {x_u : u ∈ 1 + cT + T²F_q[[T]]} with
relative Haar measure. A Case B tuple of parameter s (DEPTH_ASPECT (B)) is (m', g', w, C) monic with
  m'wC = T^s + v,  w + C = g'v,  T ∥ w, T ∥ C, T ∤ m'g', v ≠ 0,                                  (B)
L' = g'm', E = L'w − 1, E' = L'C − 1; it covers (with all families sharing it) relative mass ≤ q^{1−N(s)},
N(s) = ⌈(s + k − 2)/2⌉. Degrees a = deg w, b = deg C, z = deg m', y = deg g', t = deg v; a + b + z = s.
By the w ↔ C symmetry of (B) we write statements for a ≤ b.

## 0. Iteration log

* (I1) R187 E5 located the slack of Thm 2.5 in the crude divisor bounds δ(n) ≤ 2^n, δ₃(n) ≤ 3^n. These are sharp as
  maxima for n ≤ q, so sharper *maximal* divisor bounds cannot help at q = 3^r with r ≥ 5. What can help: (i) divisor
  counts *of a fixed degree* (binomial instead of 2^n), (ii) divisor counts *in a residue class* with no divisor loss at
  all (function-field Lenstra / Coppersmith), (iii) "loss-free" reconstruction routes. All three are below.
* (I2) A new exact degree identity (Lemma 1.1: y + t = max(a, b) always, and E·v = T^s + m'w²) removes one degree of
  freedom from every pattern and gives four routes with no divisor loss at all.
* (I3) Continuous pattern optimisation (`scripts/fs_rate.py`): the asymptotic per-s exponent becomes negative from r = 6
  (Lenstra only) resp. r = 5 (Coppersmith), against r ≥ 26 (stated constants) / r ≥ 10 (R187 E5).
* (I4) Barrier as steering wheel: the r = 4 obstacle was the hypothesis "all c at once". Each cylinder lives in one c-slice,
  so averaging over c gains q − 1 (Lemma 2.1). With the square-root-class route R10 (average of 2^ω instead of a maximal
  divisor bound) the exponent at r = 4 is −0.027 on the fs_rate grid (R217 repair, m3: a grid maximum under-estimates the sup;
  exact per-level maxima are −0.0262/−0.0236/−0.0224 at s = 300/600/1200, so the continuum value is ≈ −0.021; EVIDENCE) and Theorem 3.1 holds for **all r ≥ 4** (certified, §3).
* (I5) r = 3 and q = 3: the binding hypothesis is located (§3 end, §5): the Coppersmith threshold of route R10 meets the
  multinomial bound of R1; at q = 3 even exact counts violate (Σ) (94/27 > 2). Char 2 and k = 1: §4.
* (I6) Hostile self-review (codex deep reviewer, 2026-10-14): no FATAL; 4 MAJOR (certification rounding/fail-open scripts,
  a false "polynomial count" claim, overstated barrier labels) and minors — all repaired in place ("review repair").

## 1. New exact structure of Case B tuples

**Lemma 1.1 (degree identity; PROVED).** For every tuple (B), with a ≤ b:
(i) E·v = T^s + m'w² and E'·v = T^s + m'C²;
(ii) deg(T^s + m'w²) = s and **y + t = b = max(a, b)**; deg E = s − t = a + y + z, deg E' = b + y + z;
(iii) v = T²v₁ with v₁(0) ≠ 0; w = Tw₁, C = TC₁, and m'w₁C₁ = T^{s−2} + v₁, w₁ + C₁ = T g' v₁; gcd(w₁, T v₁) =
gcd(C₁, T v₁) = 1.
*Proof.* (i) DEPTH_ASPECT Lemma 2.1 (R4) gives C·E·m'w = (E + 1)T^s + m'w². Substitute m'wC = T^s + v:
E(T^s + v) = (E + 1)T^s + m'w², i.e. Ev = T^s + m'w². The second is the same with w ↔ C.
(ii) z + 2a ≤ z + a + b = s. If z + 2a < s the degree is s. If z + 2a = s (a = b), both T^s and m'w² are monic of
degree s and the sum has leading coefficient 2 ≠ 0 (q odd). So deg E + t = s, and deg E = a + deg L' = a + y + z gives
t = s − a − y − z = b − y. (R218 repair m-1: more directly, g'v = w + C with w, C monic and q odd gives deg(w + C) = max(a, b),
hence y + t = max(a, b); the argument above is kept because (i) is used by R4, R4'.)
(iii) T² | v and T ∥ w, T ∥ C are O173 Lemma 2.1(b). Dividing (B) by T²: m'w₁C₁ = T^{s−2} + v₁ and w₁ + C₁ = Tg'v₁. As
T ∤ m'w₁C₁ and s ≥ 3, v₁(0) ≠ 0. A common prime of w₁ and v₁ divides T^{s−2}, i.e. is T, which does not divide w₁. ∎
*Check (EVIDENCE):* y + t = max(a, b) on all 182 tuples of `bsE_famcount` (q = 3, s ≤ 13; q = 5, s ≤ 9; q = 7, s ≤ 8).
So a pattern is (s; a, z, y, t) with s = a + z + y + t, b = y + t ≥ a ≥ 1, t ≥ 2: three free degrees per s.

**Lemma 1.2 (loss-free reconstructions; PROVED).** A tuple is determined by each of the following data:
(T0) (m', g', w); (R4') (m', w, v); (X1) (m', g', v) up to 2 choices; (X2) (g', v, w).
*Proof.* (T0) L' and E = L'w − 1 are known; C = (g'T^s + w)/E by (R3) of DEPTH_ASPECT Lemma 2.1. (R4') E = (T^s + m'w²)/v
by Lemma 1.1(i), then L' = (E + 1)/w, g' = L'/m', C as in (T0). (X1) w + C = g'v and wC = (T^s + v)/m' are known, so
{w, C} are the roots of a quadratic. (X2) C = g'v − w, m' = (T^s + v)/(wC). ∎
With N*(d) := #{monic f, deg f = d, T ∤ f} = q^d − q^{d−1} (d ≥ 1), N*(0) = 1, the counts are
N*(z)N*(y)N*(a−1), N*(z)N*(a−1)N*(t−2), 2N*(y)N*(t−2)N*(z), N*(y)N*(t−2)N*(a−1) (w = Tw₁ with w₁ ∈ N*(a − 1);
v = T²v₁, lc(v) = lc(w + C) fixed, v₁(0) ≠ 0).

**Lemma 1.3 (divisors of a fixed degree; PROVED, elementary).** A nonzero F ∈ F_q[T] of degree n has at most C(n, d) monic
divisors of degree d, and at most n!/(d₁!d₂!d₃!) ordered monic factorisations F = lc(F)·D₁D₂D₃ with deg D_i = d_i.
*Proof.* A monic divisor is determined by its multiset of roots in F̄_q, a sub-multiset of size d of the n roots of F
(with multiplicity). Labelling the n roots, every sub-multiset of size d is the image of at least one d-subset. Same for
ordered triples (images of ordered set partitions). ∎

**Lemma 1.4 (divisors in residue classes, function-field Lenstra; PROVED, elementary).** Let F ∈ F_q[T] be nonzero of
degree n, Q of degree ρ ≥ 1, σ a unit mod Q, and d ≥ 0. If **3ρ > n**, then F has at most 2 divisors E (monic or not)
with deg E = d and E ≡ σ (mod Q). If d < ρ or n − d < ρ, it has at most 1 (no condition on n).
*Proof.* Let σ₀ be the residue of σ mod Q (deg < ρ). If d < ρ then E = σ₀. A divisor E has cofactor e = F/E with
eE = F; if gcd(F, Q) = 1 then e ≡ Fσ^{−1}, and in general e is determined by E. Let τ₀ (deg < ρ) be defined by
F ≡ σ₀τ₀ (mod Q) when such τ₀ exists (it does whenever some E exists: τ₀ := e mod Q); then if n − d < ρ, e = τ₀ and E = F/τ₀.
Otherwise put X = d − ρ ≥ 0, Y = n − d − ρ ≥ 0; X + Y = n − 2ρ < ρ. Write E = σ₀ + xQ, e = τ₀ + yQ, F₁ := (F − σ₀τ₀)/Q;
then deg x = X, deg y = Y and
  xτ₀ + yσ₀ + xyQ = F₁.                                                                           (L)
Let S be the set of (x, y) with deg x ≤ X, deg y ≤ Y solving (L) (E ↦ (x, y) is injective). Differences u of elements of
S lie in Λ = {(u_x, u_y) : u_xτ₀ + u_yσ₀ ≡ 0 (Q)}. For u, u' ∈ Λ, σ₀(u_x u'_y − u_y u'_x) ≡ −τ₀u_x u'_x + τ₀u'_x u_x = 0,
so Q | u_x u'_y − u_y u'_x; for differences of elements of S this determinant has degree ≤ X + Y < ρ, hence vanishes.
So if |S| ≥ 2, S ⊂ {(x₀, y₀) + αb : α ∈ F_q[T]} for one (x₀, y₀) ∈ S and a primitive b ∈ F_q[T]². If b_x = 0 then
every nonzero difference u = (0, u_y) ∈ Λ has σ₀u_y ≡ 0, so Q | u_y (σ₀ a unit), i.e. deg u_y ≥ ρ > Y, impossible; so b_x ≠ 0
(review repair R-O216 m8). Substituting into (L)
gives a polynomial φ(α) over F_q[T] with α²-coefficient b_x b_y Q and, if b_y = 0, α-coefficient b_x(τ₀ + y₀Q) = b_x e₀ ≠ 0
(e₀ ≠ 0 is the cofactor of the divisor σ₀ + x₀Q). Either way φ ≢ 0 has degree ≤ 2, so |S| ≤ 2. ∎
(The ℤ original is Lenstra 1984, threshold Q > F^{1/3}, bound 11. Over F_q[T] the ultrametric degree makes the 2×2
determinant argument exact, and the bound is 2.)

**Lemma 1.5 (function-field Coppersmith–Howgrave-Graham; PROVED, elementary).** Let F, Q, σ be as in Lemma 1.4, ρ ≤ d ≤ n,
X := d − ρ, and let m ≥ 1, k ≥ 0 be integers with
  Δ(m, k) := n·m(m+1)/2 + X·(m(m+1)/2 + km + k(k+1)/2) < (m + k + 1)·m·d.                                (C)
Then F has at most m + k divisors E with deg E = d and E ≡ σ (mod Q). Asymptotically (m, k → ∞) (C) holds whenever
X < d²/n − ε, i.e. **ρ > d(n − d)/n** (≤ n/4, against Lenstra's n/3).
*Proof.* (a) Pigeonhole (Siegel's lemma over F_q[T]): if Λ ⊂ F_q[T]^N is a full-rank submodule with deg det Λ = Δ, then
|F_q[T]^N/Λ| = q^Δ (Smith normal form), the q^{N(μ+1)} vectors with all coordinates of degree ≤ μ := ⌊Δ/N⌋ exceed q^Δ, and
the difference of two congruent ones is a nonzero vector of Λ with all coordinates of degree ≤ ⌊Δ/N⌋.
(b) Let F₁ be the largest divisor of F prime to Q (deg F₁ ≤ n); every E as in the statement is prime to Q, so E | F₁.
Choose Q̄ with QQ̄ ≡ 1 (mod F₁) and set f(x) = x + σ₀Q̄ ∈ F_q[T][x]. For E = σ₀ + x₀Q: Q·f(x₀) ≡ E ≡ 0 (mod E), so
E | f(x₀). Every P in the F_q[T]-span of g_i = f^i F₁^{m−i} (0 ≤ i ≤ m) and h_j = x^j f^m (1 ≤ j ≤ k) has E^m | P(x₀).
Map P = Σ_l p_l x^l to (p_l T^{lX})_{0 ≤ l ≤ m+k}. The images of g_i, h_j form a triangular basis with diagonal degrees
(m − i)deg F₁ + iX and (m + j)X, so deg det ≤ Δ(m, k). By (a) and (C) there is P ≠ 0 with deg p_l + lX < md for all l.
For deg x₀ = X this gives deg P(x₀) < md = deg E^m, so P(x₀) = 0. P has x-degree ≤ m + k, hence ≤ m + k roots, and
E ↦ x₀ is injective. Asymptotics: with k = τm, (C)/m² → (n + X)/2 + τX + τ²X/2 < (1 + τ)d; the gap
f(τ) = (1 + τ)d − (n + X)/2 − τX − τ²X/2 is maximised at τ = ρ/X (1 + τ = d/X), where f = d²/(2X) − n/2; so (C) holds for
large m iff X < d²/n, i.e. nX < d² (R218 repair m-2: sentence was garbled). Only explicit (m, k) are used by the certificate. ∎
(m = 1, k = 0 is the trivial "n − d < ρ" case. Over ℤ this is Coppersmith/Howgrave-Graham/Nagaraj 2008, threshold n^{1/4};
over F_q[T] the LLL loss disappears because (a) is exact.)

**Lemma 1.6 (route bounds; PROVED from Lemmas 1.1–1.5).** Fix a pattern (s; a, z, y, t), a ≤ b = y + t. Write
w = Tw₁, C = TC₁, v = T²v₁ (Lemma 1.1(iii)), N*(d) as in Lemma 1.2, and cls(n, d, ρ) for the class-divisor bound:
1 if d < ρ (or n − d < ρ when the cofactor version is allowed), else the least of 2 (if 3ρ > n, Lemma 1.4) and m + k over
(m, k) satisfying (C) for (n, d, ρ) (or, cofactor version, for (n, n − d, ρ)), and C(n, d) (Lemma 1.3) (R218 repair m-7: the scripts
search m ≤ 60, k ≤ 200 only; any valid (m, k) gives a valid bound, so this is conservative — an unrestricted search over
m + k ≤ 200 never gives a larger value and lowers the r = 4 finite sum from 1.67692 to 1.67548). The cofactor
version is allowed when F is prime to Q (then the cofactor's class F σ^{−1} is a unit). The number of tuples with the
pattern is at most each of:
| route | data fixed (choices) | then | bound |
|---|---|---|---|
| T0, R4', X1, X2 | Lemma 1.2 | — | as in Lemma 1.2 |
| R1 | v₁: N*(t−2) | m'w₁C₁ = T^{s−2} + v₁ | N*(t−2)·(s−2)!/(z!(a−1)!(b−1)!) |
| R2 | m', g' | E ∣ 1 + T^s m'g'² (deg s + 2y + z), E ≡ −1 (TL') | N*(z)N*(y)·cls(s+2y+z, a+y+z, y+z+1) |
| R3 | w₁, g' | E ∣ g'T^{s−1} + w₁, E ≡ −1 (Tw₁g'); E-version only | N*(a−1)N*(y)·cls(s−1+y, a+y+z, a+y) |
| R4 | m', w₁ | E ∣ T^{s−2} + m'w₁² (= Ev₁), E ≡ −1 (Tm'w₁) | N*(z)N*(a−1)·cls(s−2, a+y+z, a+z) |
| R3C, R4C | same with C₁, E' | E' ∣ g'T^{s−1} + C₁; E' ∣ T^{s−2} + m'C₁² | N*(b−1)N*(y)·cls(s−1+y, b+y+z, b+y); N*(z)N*(b−1)·cls(z+2b−2, b+y+z, b+z) |
| R5a (R5b) | v₁, w₁ (C₁) | C₁ ∣ (T^{s−2}+v₁)/w₁ = m'C₁, C₁ ≡ −w₁ (Tv₁) | N*(t−2)N*(a−1)·cls(s−1−a, b−1, t−1) |
| R6a (R6b) | v₁; w₁ ∣ T^{s−2}+v₁ | as R5a | N*(t−2)·C(s−2, a−1)·cls(s−1−a, b−1, t−1) |
| R8a (R8b) | g', v₁; w₁ ∣ T^{s−2}+v₁ | C₁ = Tg'v₁ − w₁ | N*(y)N*(t−2)·C(s−2, a−1) |
| R9a | m', v₁; w₁ ∣ (T^{s−2}+v₁)/m' | — | N*(z)N*(t−2)·C(a+b−2, a−1) |
| R10a | m', v₁; w₁² ≡ −(T^{s−2}+v₁)/m' (Tv₁) | w₁ ∣ (T^{s−2}+v₁)/m' in one of ≤ 2^{ω(Tv₁)} classes | N*(z)·2Σ_{v₁}2^{ω(v₁)}·cls(a+b−2, a−1, t−1) |
| R10b | v₁; m' ∣ T^{s−2}+v₁ | as R10a | 2Σ_{v₁}2^{ω(v₁)}·C(s−2, z)·cls(a+b−2, a−1, t−1) |
with Σ_{v₁ admissible, deg e} 2^{ω(v₁)} ≤ Σ_{v monic, deg e} 2^{ω(v)} = q^e(2 + (e − 1)(1 − 1/q)) (e ≥ 1) (review repair m9: an
inequality, since admissible v₁ have T ∤ v₁).
*Proof.* Each row: the fixed data, then the divisibility/congruence displayed, determine the tuple (Lemma 1.2 and
DEPTH_ASPECT Lemma 2.1). Congruences: E + 1 = L'w = Tw₁g'm', so E ≡ −1 modulo TL', Tw₁g' and Tm'w₁; E is prime to T
(E(0) = −1), so E ∣ g'T^s + w = T(g'T^{s−1} + w₁) gives E ∣ g'T^{s−1} + w₁, and Ev = T^s + m'w² gives Ev₁ = T^{s−2} + m'w₁².
From w₁ + C₁ = Tg'v₁: C₁ ≡ −w₁ (mod Tv₁), a unit by Lemma 1.1(iii). Coprimality for the cofactor version:
1 + T^s m'g'² ≡ 1 (mod TL'); T^{s−2} + m'w₁² is prime to Tm'w₁ (a common prime divides T^{s−2} and does not divide
m'w₁); (T^{s−2}+v₁)/w₁ = m'C₁ and (T^{s−2}+v₁)/m' = w₁C₁ are prime to Tv₁ (Lemma 1.1(iii) and T ∤ m'). For R3/R3C,
gcd(g', w₁) may be nontrivial, so only the E-version is used. R10: w₁C₁ = G₂ := (T^{s−2}+v₁)/m' and C₁ ≡ −w₁ give
w₁² ≡ −G₂ (mod Tv₁); a unit has ≤ 2 square roots modulo each prime power (q odd), hence ≤ 2^{ω(Tv₁)} = 2·2^{ω(v₁)}
classes, and in each class w₁ is a divisor of G₂ of degree a − 1, G₂ prime to Tv₁. v₁ has fixed leading coefficient
lc(w + C) and Σ over such v₁ of 2^{ω(v₁)} is the monic sum: Σ_{deg v = e} 2^{ω(v)} = Σ_{d squarefree, deg d ≤ e} q^{e − deg d}
= q^e(1 + 1 + Σ_{j=2}^{e}(1 − 1/q)). ∎
*Check (EVIDENCE):* `scripts/fs_check_bounds.c` compares the minimum of all rows (as coded in `scripts/fs_sum.c`) with the
exact pattern counts of `bsE_famcount` (q = 3, s ≤ 15; q = 5, s ≤ 11; q = 7, s ≤ 9): 0 violations, max count/bound
1.000. `scripts/fs_lemma_check.py` tests Lemmas 1.4/1.5 by brute force on random highly factorable F over F₃, F₅
(32 591 (degree, class) groups): 0 violations.

## 2. Averaging over c: a free factor q − 1

**Lemma 2.1 (PROVED).** Let 𝓤 = ⋃_{c ∈ F_q^*} (c-slice) (relative mass q − 1 in units of one c-slice). Every Case B tuple
and every Case A datum (a1', b1, E) has its maximal cylinder in exactly one c-slice. Hence if
  Σ_{all Case B tuples} q^{1−N(s)} + Σ_{all Case A data} q^{2−k−α} < q − 1,                                   (Σ)
some c-slice contains a positive-measure set of points in no validity set, so O(q, T^k) ≠ ∅ and ES_q(T^k, ·) has no
finite linear covering (FUNCTIONFIELD_ES2 §0.1). More precisely, the number of c with covered relative mass ≥ θ is at
most (left side of (Σ))/θ.
*Proof.* The cylinder of a Case B tuple is u ≡ −E (mod T^{N+1}) with N ≥ 1, and of a Case A datum u ≡ −E (mod T^{k+α});
both fix u mod T², i.e. c. Summing the covered masses of the q − 1 slices gives at most the left side of (Σ). ∎
*Remark.* DEPTH_ASPECT Thm 2.5 bounded the left side of (Σ) (its counts are over all tuples, all c) by < 1 and concluded
for every c. For the no-covering conclusion, the averaged form (Σ) suffices; it gains the factor q − 1.

**Lemma 2.2 (Case A at small depth; PROVED).** Case A data (DEPTH_ASPECT §2.2) have depth α ≥ 3. Their number per pattern
(α; λ, β, κ) (f = α − β − κ ≥ 0, ζ := max(β, f) − λ ≥ 1) is at most each of the six bounds listed in
`scripts/fs_caseA.py`: (a1', b1, K) ↦ E = a1'b1K − 1; (a1', K, F) ↦ b1 by (A4); (b1, K) with E ∣ T^α + b1²K, E ≡ −1 (b1K)
(Lemma 1.4); (a1', b1) with E ∣ T^α a1' + b1, E ≡ −1 (Ta1'b1) (Lemma 1.4); z then (b1, K, F) by (A3) (Lemma 1.3); (a1', z, K)
with b1 + F = a1'z, b1F = (T^α + z)/K (≤ 2). Only E and α determine the cylinder, so g' is not counted.
*Proof.* The routes are DEPTH_ASPECT Lemma 2.3 (A1)–(A4) with Lemmas 1.3, 1.4. Small depth: T | z and z ≠ 0 give deg z ≥ 1,
and deg z ≤ ζ. α = 1 forces β = f = 0, so ζ ≤ 0: impossible. α = 2: (β, κ, f) ∈ {(0,2,0), (0,1,1), (1,1,0)}; the first has
ζ ≤ 0; in the others λ = 0 (so a1' = 1), z = μT, and (A3), (A0) give b1KF = T(T + μ), F + b1 = μT with K = T, {b1, F} = {1, T + μ}
(monic, as E, F, K are monic by DEPTH_ASPECT Lemma 2.4 since α > β), so T + μ + 1 = μT, i.e. μ = 1 and μ + 1 = 0: impossible
(q odd). ∎ (R218 repair m-6: the small-depth statement α ≥ 3 is not used by the certificate — `fs_caseA.py` sums from α = 1,
which is conservative.)

## 3. The theorem

**Theorem 3.1 (no finite linear covering of ES_q(T^k) for q = 3^r, r ≥ 4; PROVED, computer-assisted, given the inputs of
DEPTH_ASPECT Thm 2.5 (O173 Lemmas 1.1, 2.1 as re-derived by R187; R166 Case A steps; compactness criterion)).**
Let q = 3^r with **r ≥ 4** (q ≥ 81) and k ≥ 2. Then O(q, T^k) ≠ ∅: ES_q(T^k, ·) has no finite linear covering. More precisely:
(a) r = 4: the covered relative measure, summed over the 80 c-slices, is ≤ 2.18; so at least 75 of the 80 c-slices have
    more than half of their measure in O(81, T^k);
(b) r ≥ 5: for **every** c ∈ F_q^*, the c-slice minus a set of relative measure ≤ 0.26 (r = 5), ≤ 0.38 (r = 6) (R218 repair m-3, consolidated with R217 m5:
    these two constants are artefacts of the cutoff S; with larger S, R218 certifies ≤ 0.175 (r = 5, S = 160) and ≤ 0.039
    (r = 6, S = 100), R217 ≤ 0.19 and ≤ 0.039),
    ≤ 0.012 (r = 7), ≤ 0.0033 (r = 8), ≤ 0.0011 (r = 9), and below 10⁻³ for 10 ≤ r ≤ 30, lies in O(q, T^k).
For char ≥ 5 this was known (O140 Prop 4.1); r ≥ 27 was DEPTH_ASPECT Thm 2.5. New: 4 ≤ r ≤ 26.
*Proof.* Take k = 2 (N(s) and the Case A exponent only grow with k). By Lemma 2.1 it suffices to certify (Σ). Its Case B part
is Σ_s q^{1−⌈s/2⌉}·Σ_patterns (mult)·(min of the Lemma 1.6 bounds), mult = 2 for a < b, 1 for a = b (w ↔ C symmetry);
its Case A part is Σ_α q^{−α}·Σ_patterns (min of the Lemma 2.2 bounds) for α ≤ 40, plus DEPTH_ASPECT Lemma 2.4 for α > 40.
(i) Finite Case B part, 3 ≤ s ≤ S (S = 200 for r = 4, 100 for r = 5, 60 for r ≥ 6): `scripts/fs_sum.c` (long double; every
term is exp of a sum of ≤ 10⁴ logarithms of integers, relative error ≪ 10⁻⁶; review repair M1: all components are printed
with ≥ 10 significant digits and the certified total is (finite + tail + Case A)·1.01, which dominates serialisation and
floating-point error; the script fails closed).
Independent check: `scripts/fs_sum_check.py` re-implements the table of Lemma 1.6 in exact integer/rational arithmetic and
agrees with fs_sum to 10 significant digits on every term s ≤ 40 (r = 4). (R218 repair m-7/m-5: fs_sum_check copies fs_sum's restricted
(m, k) search, so it is independent in the arithmetic but not on that point; R218's from-scratch `scripts/review_fs2_sum.c` and
exact-rational `scripts/review_fs2_exact.py` agree with each other to 16 digits (r = 4, s ≤ 60) and give values ≤ fs_sum's.)
(ii) Tail s > S: `scripts/fs_tail.c`. Normalise p = (a, z, y, t)/s. On each dyadic box of p-space (adaptive, minimal width 2⁻⁸),
every route is bounded by exp(s·φ⁺ + const)·(s + 1)^{0 or 1} with φ⁺ an upper bound over the box: N*(d) ≤ q^d,
C(n, d) ≤ exp(n H(d/n)) and multinomials ≤ exp(n H(·)), whose continuum versions B(d, e) = (d + e)log(d + e) − d log d − e log e
are increasing in d and e, so they are bounded at the box's upper corner; binomials with shifted arguments are first
enlarged (C(s−2, a−1) ≤ C(s, a), etc.). The class-count conditions of Lemmas 1.4/1.5 are linear in (n, d, ρ) for fixed
(m, k) (homogeneous of degree 1), so they are checked on the box including the integer shifts of n, d, ρ, uniformly for all
s ≥ S. The number of integer patterns of level s in a box of width w is ≤ (sw + 1)³. Each box contributes
Σ_{s > S} 2(sw + 1)³·min_route[e^{sφ⁺ + const}(s + 1)^{0/1}]·q^{1 − s/2}, summed explicitly until the term ratio (bounded
by ((s+2)/(s+1))^{3 or 4}e^{φ⁺ − (log q)/2}) is < 0.999, then by a geometric series. Boxes with φ⁺ ≥ (log q)/2 would make the
certificate fail; for r ≥ 4 none occurs at minimal width 2⁻⁸.
(iii) Case A: `scripts/fs_caseA.py` (exact rationals, α ≤ 40) plus the geometric majorant of DEPTH_ASPECT Lemma 2.4 for
α > 40 (ratio ≤ (43/42)³·6/√q < 1 for q ≥ 81).
Result (`scripts/fs_certify.sh`, log `data/fs/certify.txt`, certified totals ×1.01): left side of (Σ) ≤ 2.176 (r = 4;
q − 1 = 80), 0.2502 (r = 5), 0.3730 (r = 6), 0.01157 (r = 7), 0.003209 (r = 8), 0.001043 (r = 9), and < 10⁻³ for 10 ≤ r ≤ 30; for r ≥ 27 also DEPTH_ASPECT Thm 2.5. In every
case (Σ) holds; for r ≥ 5 even the left side is < 1, which gives (b) for every c. (R217 repair, m5: for r ≥ 31 the
document's own certificate does not apply; R217's independent certificate `scripts/review_fs_certify.sh` covers r = 4..45
(`data/fs/review_certify_*.txt`; left side ≤ 1.69 at r = 4, ≤ 0.19 at r = 5, ≤ 0.039 at r = 6, < 4·10⁻¹⁴ for 31 ≤ r ≤ 45), and the
DEPTH_ASPECT crude form, decreasing in q, is 5.9·10⁻⁵ at r = 46; so the covered relative measure is ≤ 0.012 for every r ≥ 7.) ∎
*What changed against Thm 2.5 (r ≥ 27):* (1) the exact degree identity (Lemma 1.1) and loss-free routes (Lemma 1.2);
(2) divisor counts by degree (Lemma 1.3) instead of 2^n, 3^n; (3) divisors in residue classes with an absolute bound
(Lemmas 1.4, 1.5) — no divisor function at all on the routes that bind; (4) the square-root-class route R10 with the
average Σ2^{ω(v)} ≪ s·q^{deg v} instead of a maximal divisor bound; (5) averaging over c (factor q − 1, needed only at r = 4);
(6) a rigorous adaptive tail instead of truncation + crude tail.

**Where the method stops: r = 3 (EVIDENCE + Assessment; review repair M3).** At q = 27 the continuum exponent
max_p min_route φ(p) equals (log q)/2 on the grid of `scripts/fs_rate.py` (a finite grid, EVIDENCE), and fs_tail fails to
certify 835 boxes (a failure to certify, not a negative result), mostly near
p ≈ (a, z, y, t)/s ≈ (0.31, 0.325, 0.20, 0.168)). (R217 repair, m1/m2: (i) the method fails at r = 3 already at finite level:
the Lemma 1.6 bound-sum through s = 150 is ≈ 194.6 > q − 1 = 26 (per-s terms 2–2.5; CERTIFIED for the bounds, a statement
about the method, not about the true counts). (ii) There is a second near-critical region p ≈ (0.39, 0.11, 0.10, 0.40) (29 of
the 615 failed boxes of `fs_tail 3 150 8`), where R3, R10b, R4, R2 meet; the per-level maximum of min-route sits there
(−0.0034·log q below (log q)/2 at s = 1200, increasing with s). (R218 repair m-4, consolidating with R217 m1: the bound-sum
already exceeds q − 1 = 26 at s = 36 (27.68; R218's independent code gives 195.06 through s = 150), so the failure of (Σ) with
the Lemma 1.6 bounds at r = 3 is CERTIFIED independently of any tail; that every union bound fails stays Assessment. The
first region has an exact critical point: at (a, z, y, t)/s = (1/3, 1/3, 1/6, 1/6), R1 = 1/6 + log 3/log 27 = 1/2 and the R10
Coppersmith threshold ab/(a + b) = 1/6 = t, both with equality; the quoted grid point approximates it.) Reaching r = 3 therefore also needs a class-divisor bound beyond
the Coppersmith range for R2/R3/R4.) In the first region two routes meet exactly at the exponent 1/2:
R1 (v, then a triple factorisation of T^{s−2} + v₁: exponent τ + H(ζ, α, β)/log q) and R10 (v, m', then w₁ in a
square-root class mod Tv₁ — valid only above the Coppersmith threshold τ > αβ/(α + β)). Below the threshold the class bound is
lost; above it R1 is ≥ 1/2. The finite sums at r = 3 (s ≤ 150) give per-s terms ≈ 2, decreasing only slowly (no
convergence visible; not a proof of divergence of the true sums — but the bound-sum itself already violates (Σ), see above). Assessment: to reach r = 3 *with this union bound* one needs either a divisor-in-class bound beyond the Coppersmith range (for counting, not finding; over ℤ the analogous
1/4-barrier is open), or an *average* bound for triple factorisations of T^{s−2} + v₁ over short families of v₁ — a
short-interval d₃ problem in F₂₇[T]. Both are B3-type inputs. (Other measure arguments are not excluded by this.)

## 4. Contrast: which hypothesis fails where coverings exist (goal 3)

The sterility proof uses exactly three structural inputs: (H1) k ≥ 2 (every cylinder has depth ≥ 2, so validity on the
c-slice forces T ∥ w, T ∥ C and the tuple form (B)); (H2) q odd, through **v ≠ 0** (O173 Lemma 2.1(b): E + E' = m'g'²v − 2, so v = 0 would give
E + E' = −2, impossible for monic E, E' of positive degree when q is odd), and through ≤ 2 square roots modulo prime powers (route R10) and the leading coefficient 2 ≠ 0 (Lemma 1.1(ii));
(H3) a counting exponent < 1/2 (Theorem 3.1 needs r ≥ 4).
* **q = 3, A = T (k = 1): (H1) fails.** FUNCTIONFIELD_ES Prop 1.4(i), (ii) are the constant families E = 1, E = 2; their
  cylinders have depth 1, i.e. each is a whole class P(0) = −E, of relative mass 1. For q = 3 the two classes are all of
  F₃^*, so two families cover R̂^* (that is the (J)4 covering). For k = 1 a single family can carry full mass, and (Σ) fails at
  its first term. (For q = 3^r, r ≥ 2, k = 1, the classes P(0) ∉ {1, 2} are not reached by constants; the slice analysis
  there needs Case B at u(0) ≠ 1, not done.)
* **Characteristic 2: (H2) fails, by Frobenius (PROVED).** For q even, k = 2 and every c ∈ F_q^*, the single family
  F_c = (E; 0, g'; 2, g') with g' = T + c, E = 1 + Tg' = T² + cT + 1 is valid at every point of the c-slice
  (x ≡ 1 off T, u ≡ 1 + cT mod T²). Indeed D = 1 + T²g'² = (1 + Tg')² = E² — a "v = 0" tuple, E = E', s = 2, impossible
  in odd characteristic — and: T²g' ∣ P + E because P + E ≡ u + E ≡ 0 (mod T²) (char 2) and P + E ≡ 1 + 1 = 0 (mod g');
  modulo E, P ≡ 1 and X ≡ T^{−2}, so s = g' + X/g' ≡ (T²g'² + 1)/(T²g') = E²/(T²g') ≡ 0; lc(s) = 1 = lc(E) for deg P large.
  (Sanity check `scripts/fs_char2.py`, over F₂.) More generally for
  k = 2m, the families with E = 1 + T^m g' (cylinder depth 2m) cover every slice point with u ≡ 1 (mod T^m),
  u ≢ 1 (mod T^{m+1}). So in characteristic 2, for k = 2, every c-slice (u(0) = 1, c ≠ 0) — the region where odd-characteristic
  sterility is proved — is covered by one depth-2 family per c (slice points with u(0) ≠ 1 are not addressed; review repair m7).
  This is consistent with the char-2 coverings of (J)4 and FF_MUTE M1, and it locates the odd-characteristic input precisely:
  **v ≠ 0 (E ≠ E'), which in odd characteristic follows from −2 ≠ 0.**
* **ℤ (Assessment).** The ℤ analogues of (H1)–(H3) are: the r-generic line of a Mordell prime r (depth ≥ 1 at r), the
  Type II congruence f ≡ f' ≡ −1 (mod 4cd) (whose "E + E' ≡ −2" is the reason f = f' is rare — a square 1 + 4c²dn), and the
  ET exponent 2/5 < 1/2 with constants. (J)26 Thm 3.1 is the r → ∞ case; the present improvements that are *not* specific to
  F_q[T] are the c-averaging (over ℤ: averaging over the non-residue cells, already used there) and the residue-class divisor
  bounds (Lenstra's theorem holds over ℤ with bound 11; Coppersmith with n^{1/4+ε}). Transplanting Lemmas 1.4–1.6 to the
  ℤ box bounds of MORDELL17 could lower the effective r₀ of (J)26 Thm 3.1 substantially; it cannot reach r = 13, 17, whose
  level-1 term alone is > 1/2 (DEPTH_ASPECT Remark (2)). Not pursued here.

## 5. Conjecture 0.2 at q = 3 (goal 2): what the method can and cannot do

**Reformulation at x*_c (PROVED, elementary).** Let s = 2n be even with n ≥ 2 (R217 repair, m4: used in both directions;
odd s is analogous but not written), N = n (the largest cylinder) and q = 3. A Case B tuple
covers x*_c iff, with v = T²v₁, there is ω ∈ F₃[T] with
  w₁ = c·g'v₁(1 + cT) + T^n ω,  C₁ = −c·g'v₁ − T^n ω,
and, writing P := m'g'²v₁(1 + cT) + 1,
  (S1) T^n ∣ P,  (S2) T^{n−2} ∣ P/T^n + c m'g'ω(cT − 1) =: T^{n−2}Ψ,  (S3) v₁Ψ = −(1 + m'(Tω)²).
*Proof.* Covering means E ≡ −(1 + cT) (mod T^{n+1}). From EC₁ = g'T^{s−1} + w₁ (Lemma 1.6, R3 row) this gives
w₁ ≡ −(1 + cT)C₁ (mod T^{n+1}); with w₁ + C₁ = Tg'v₁ and c² = 1: C₁ ≡ −cg'v₁, w₁ ≡ cg'v₁(1 + cT) (mod T^n), so
w₁, C₁ have the displayed form with a common ω (their sum is exactly Tg'v₁). Then m'w₁C₁ = T^{s−2} + v₁ expands (2 = −1 in F₃) to
−v₁P − cm'g'v₁T^nω(cT − 1) − m'T^{2n}ω² = T^{2n−2}; reducing mod T^n gives (S1) (T ∤ v₁), dividing by T^n gives
v₁(P/T^n + cm'g'ω(cT − 1)) = −T^{n−2}(1 + m'T²ω²), whence (S2), (S3) as T ∤ v₁. Conversely (review repair m5: this is an equivalence), given (S1)–(S3) and the side conditions, w₁ + (1 + cT)C₁ = −cT^{n+1}ω
and EC₁ = g'T^{2n−1} + w₁ give (E + 1 + cT)C₁ = g'T^{2n−1} − cT^{n+1}ω ≡ 0 (mod T^{n+1}) (n ≥ 2), and C₁ is a T-adic unit,
so E ≡ −(1 + cT) (mod T^{n+1}): the tuple covers x*_c. ∎ (R217 repair, m4: the converse uses only the displayed form of
w₁, C₁ and the tuple identities; so for a tuple (B): covers x*_c ⇔ T^n | w₁ − cg′v₁(1 + cT), and given that form,
(S1)–(S3) ⇔ m′w₁C₁ = T^{s−2} + v₁.)
(S3) is the genus condition of FF_STERILE_PROOF Lemma 2.1 made explicit (−m' is a square modulo every prime of v₁); (S1) says
the "small" product m'g'²v₁ is ≡ −(1 + cT)^{−1} to precision n, which by degree forces z + 2y + t ≥ n + 1: one of the four
small polynomials carries about half the degree — the lopsidedness of O175 Lemma 3.2 in one line. I found no further
structure: (S1)–(S3) is a system of two T-adic congruences of length ≈ n and one ∞-adic divisibility, with ≈ n + O(1) free
coefficients — the lottery shape (B2) again.

**Limits of the union-bound route at q = 3 (CERTIFIED census + EVIDENCE/Assessment; review repair M3).** (a) At q = 3 even
*exact* tuple counts make the averaged union bound (Σ) fail: the bsE_famcount census gives left side of (Σ) through s = 15
exactly 94/27 > q − 1 = 2 (exact enumeration, re-derived by the O216 review). So a measure proof of this kind at q = 3 must use overlaps (the exact union to
s = 21 is ≈ 0.49 per slice, FF_STERILE_PROOF §5) plus a tail Σ_{s>21} count(s)·3^{1−⌈s/2⌉} ≲ 1, i.e. an essentially sharp
count of Case B tuples. (b) The exponent of the Lemma 1.6 bounds is far from that: fs_rate (grid, EVIDENCE) gives max_p min_route φ − 1/2 = +0.167
(r = 1), +0.096 (r = 2), 0.000 (r = 3), −0.027 (r = 4) in units of log q (R217 repair, m3: grid values; R217's exact per-level
maxima at s = 1200 are −0.0034 (r = 3), −0.0224 (r = 4), increasing in s, so r = 4 is ≈ −0.021 in the limit). At r = 1 the maximiser is the "thirds corner"
a = z = y = s/3, t → 0 (v₁ of bounded degree, w, C, m' of degree s/3): there every route is ≥ 2/3, while the true count is
subexponential, q^{o(s)}, but **not** polynomial (review repair M2: over F₃, F = T^{3^h−1} − 1, s = 3^h + 1, v₁ = −1, grouping the
(3^h − 3)/h degree-h factors by (f(0), f'(0)/f(0)) and distributing triples among m', w₁, C₁ gives 6^M = exp(Ω(s/log s)) genuine
tuples at a ≈ b ≈ z ≈ y ≈ s/3, t = 2; e.g. ≥ 7.8·10¹⁰ at s = 244). The count is Σ_{v₁} #{m'w₁C₁ = T^{s−2} + v₁ into thirds
with w₁ ≡ −C₁ (Tv₁)}. Beating it needs an average bound for d₃
over the short family {T^{s−2} + v₁ : deg v₁ ≤ t − 2}, uniform in q = 3 — a short-interval divisor problem whose function-
field results (Keating–Rodgers–Roditty-Gershon–Rudnick, Sawin) are large-q statements. This is the function-field face of
B3, now located at a specific corner of pattern space.

## 6. Replay

```
gcc -O2 -o /tmp/fs_sum scripts/fs_sum.c -lm && /tmp/fs_sum 4 200 1 10        # finite part, r = 4 (~3 min)
uv run python scripts/fs_sum_check.py 4 40                                    # independent exact check (~15 min)
gcc -O2 -o /tmp/fs_tail scripts/fs_tail.c -lm && /tmp/fs_tail 4 200 8         # tail, r = 4 (~5 s)
uv run python scripts/fs_caseA.py 4,5,6 40                                    # Case A
./scripts/fs_certify.sh                                                       # all r = 4..30 -> data/fs/certify.txt (~10 min)
python3 scripts/fs_rate.py 1,2,3,4,5                                          # continuum exponents (steering)
gcc -O2 -o /tmp/famcount scripts/bsE_famcount.c -lm && /tmp/famcount 3 2 15 print > /tmp/fc3.txt
gcc -O2 -o /tmp/chk scripts/fs_check_bounds.c -lm && /tmp/chk 3 < /tmp/fc3.txt   # bounds vs exact counts
uv run --with sympy python scripts/fs_lemma_check.py 3,5 150                  # Lemmas 1.4/1.5 brute force
uv run --with sympy python scripts/fs_char2.py
```
