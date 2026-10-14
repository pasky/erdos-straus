# FF_STERILE_PUSH — pushing the large-q no-covering theorem down, and the q = 3 sterile point (O216, wave Y-e)

Status: in progress (O216). **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in DISCOVERIES.md.
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
* (I3) Continuous pattern optimisation (scripts in §3): asymptotic per-s exponent becomes negative from r = 6
  (Lenstra) resp. r = 5 (Coppersmith), against r ≥ 26 (stated constants) / r ≥ 10 (R187 E5).

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
t = s − a − y − z = b − y.
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
Q | σ₀b_y·(multiple), so Q | b_y and some difference has deg u_y ≥ ρ > Y, impossible; so b_x ≠ 0. Substituting into (L)
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
E ↦ x₀ is injective. Asymptotics: with k = τm, (C)/m² → (n + X)/2 + τX + τ²X/2 < (1 + τ)d; minimising over 1 + τ = X^{−1/2}·…
gives the condition √(nX) < d. ∎
(m = 1, k = 0 is the trivial "n − d < ρ" case. Over ℤ this is Coppersmith/Howgrave-Graham/Nagaraj 2008, threshold n^{1/4};
over F_q[T] the LLL loss disappears because (a) is exact.)
