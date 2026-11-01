# Z53_LATTICE — B2 via geometry of numbers: what lattice pigeonhole can and cannot give

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress toward proving 4/p. Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results are internally reviewed only (not refereed).

Lane: z53 LATTICE (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z53_lanes.md` §LATTICE). Scripts
`scripts/z53_lattice_*`, data `data/z53/lattice/` (< 1 MB).

**Status: final draft (pre-review).** Verdict: **narrowed** (§8).

## 0. Summary

* **Theorem A (PROVED).** For every odd n ≥ 1.34·10¹⁶ there is **no convex Thue scheme** for (★) in the natural coordinates
  (u, B, C), nor in any affine-linear encoding of them: no lattice coset of any index, no exactness modulus D, and no
  convex body K satisfy Thue's three conditions (exactness congruence, size bound on K, volume/covering). This is the
  theorem behind FRONTIER's M1b Assessment ("Thue/Minkowski: target class depends on the exact height").
* **Prop A1 (PROVED; algebraic core).** If 4CuB − u − B ≡ n (mod D) on a coset of index D′ in ℤ³, then
  D′ ≥ D^{4/3}/c₀, c₀ = 2⁶·3^{4/3} < 277. Brute force (CERTIFIED, q ∈ {2,…,9, 11, 16 (n = 1, 3), 25, 27}) finds the true
  minimum to be D′ = q² for q ∈ {5, 7, 11, 25, 27} with ℓ ∤ n, D′ = q^{3/2} (q = 25, 5 | n; q = 9), q^{5/3} (q = 27, 3 | n),
  and D′ = q, 2q at the 2-adic q = 4, 8, 16.
* **Lemma V (PROVED).** A convex body inside the exactness shell {|G| < D} has volume ≤ 15.2·D²/n (D ≤ n/17): the shell
  is thin (thickness ≲ D/n^{2/3}) and curved (the surface is elliptic in the positive octant), so convex pieces are tiny.
* **Theorem A′ (PROVED; fixed C).** At a fixed level C the only Thue schemes are those **handed a divisor of N_C = 4Cn + 1**:
  the exactness modulus D satisfies gcd(D, N_C) ≥ N_C/456 (thin case D ≤ n/7), resp. gcd(D, N_C) ≥ CD/(8 log²(2(n+D+1)))
  (thick case), which gives N_C/gcd(D, N_C) = O(log²n).
* **Prop D (PROVED, elementary).** In the hyperbola coordinates (X, Y, C) (X = 4Cu − 1, Y = 4CB − 1), where the variety is a
  ruled quadric and *does* carry exactness cosets, the class condition 4C | X + 1 holds on no full-rank lattice coset meeting
  the positive region. "No exactness cosets" (natural coordinates) and "tied class" (hyperbola coordinates) are the two
  faces of one obstruction — PARITY_AUDIT Remark 3.1, now with a theorem on each side.
* **Theorem B (PROVED; polynomial encodings).** For a polynomial encoding Φ: ℤ^k → ℤ³ of degree δ, every exactness prime
  ℓ > 3δ (ℓ odd) whose coset has positive dimension mod ℓ either pins Φ to a point mod ℓ (congruence data) or **designates ℓ
  as a prime factor** of u, B, C, X or Y (the five lines of V_n): the transparent-certificate shape of B4.
* **Coppersmith / Lenstra (§5; PROVED + CERTIFIED).** The integer-Coppersmith bound for a fixed-C slice is exactly the CHN regime
  C > (n/64)^{1/3}; asymptotically 1/4 (Lenstra) and 4/9 (CHN) of the mass of R lies in the C-slice regimes, 9/16 in the
  u-slice CHN regime, and every (★) triple is CHN-visible in some slice (35/36 Lenstra-visible). Measured at 10⁷, 10⁹ (shares
  converge slowly to these). The LLL guarantees are uniform in n and hold at odd squares where the root set is empty (T1),
  so they carry no existence content; Howgrave-Graham's lemma is Thue-exactness applied to an *assumed* root.
* **Natural lattice invariants (EVIDENCE).** The Thue-lattice angle (p = a² + b², b/a) is uncorrelated with R(p)/log²p among
  primes p ≡ 1 (24) (corr −0.018 at 10⁷, −0.011 at 10⁹); among the 14 (★)-zero primes it is small (b/a < 0.16) for 6 of 14
  (vs ≈ 20 % expected) — the known near-square (T1-deformation) effect, nothing more.
* **What survives (Assessment).** Non-convex "Thue schemes" are lattice-point counts of sub-lotteries of R(n) in a thin
  curved shell: exactly the §7.1 hyperbola problem with an extra congruence (never easier). Exponent-lattice covering is
  (J)85 (sub-power windows). Nothing else of geometry-of-numbers type is left in the natural, affine-linear or fixed-C
  formulations.

## 1. Statements attacked and why they are not already closed

n odd ≥ 3 (primes p ≡ 1 (24) of interest; odd squares, near-squares and the FRONTIER §4 item-14 primes are controls).

  G_n(u, B, C) := 4CuB − u − B − n,  V_n := {G_n = 0},  R(n) := #(V_n ∩ ℕ³)   (FRONTIER §2.1);

X := 4Cu − 1, Y := 4CB − 1, N_C := 4Cn + 1; then XY = 4C·G_n + N_C, so G_n = 0 ⟺ XY = N_C (with X ≡ Y ≡ −1 mod 4C).

**Thue's mechanism** (p = x² + y², p ≡ 1 (4)): Λ = {x ≡ ιy (mod p)}, ι² ≡ −1, index p; x² + y² ≡ 0 (mod p) on Λ; the disc
K = {x² + y² < 2p} is convex of area 2πp > 4p; Minkowski gives 0 ≠ v ∈ Λ ∩ K; exactness gives x² + y² = p.

**Definition 1.1 (convex Thue scheme for (★) at n).** A quadruple (Λ, t, D, K): Λ ⊆ ℤ³ a lattice of index D′, t ∈ ℤ³,
an integer D ≥ 1, K ⊆ [1, ∞)³ convex, with
* (E) G_n(v) ≡ 0 (mod D) for every v ∈ Λ + t (exactness congruence);
* (S) |G_n(x)| < D for every x ∈ K (size bound on the whole body, as Thue's disc);
* (V) K + Λ = ℝ³ (the covering statement that a translation-uniform geometry-of-numbers theorem delivers; it implies
  vol K ≥ covol Λ = D′, which is all that is used below).
Under (E), (S), (V), (Λ + t) ∩ K ≠ ∅ (take −t ∈ K + Λ) and every point of (Λ + t) ∩ K is a (★) triple (G ≡ 0 mod D and
|G| < D force G = 0; K ⊆ [1,∞)³ gives positivity).

*Scope remarks.* (i) K ⊆ [1, ∞)³ is the convex hull of the positive integer points, the only place a found point may lie.
(ii) Minkowski's *homogeneous* theorem needs K symmetric about a lattice point; in natural coordinates the centre would be
a coset point inside K, i.e. a solution already in hand, so a non-circular use is the covering form (V). (iii) Affine-linear
encodings are covered (Cor 2.6). (iv) Non-convex K and non-linear encodings are treated separately (§3, §4).

**Statements.** (A) no convex Thue scheme exists for n ≥ n₀; (A′) at fixed C, Thue schemes need a divisor of N_C;
(B) structure of exactness primes under polynomial encodings; (C) Coppersmith/Lenstra regimes and their (non-)existence
content; (D) the dual (hyperbola-coordinate) obstruction.

**Why not already closed.** FRONTIER §3's M1b row is an **Assessment** ("target class depends on the exact height;
covering needs sub-power windows"); its theorem part ((J)85 Thm 3.1) concerns *covering by divisor boxes in relation
lattices*, not Thue exactness. `BRAINSTORM/s4_minkowski_sail.md` (Minkowski is sign-blind on Λ_A), `s3_lll_lenstra.md`,
`gon_lll_relation_lattice.md` (Coppersmith has no existence content), `s8_twisted_hyperbola_thue.md` and
`LATTICE_MEETING.md` (class-group walks on L_ρ(g)) are Assessments or concern specific lattices. No statement in the repo
excludes *every* lattice of *every* index with *every* convex body; Theorem A does (natural and affine-linear coordinates).
Closed-list check: none of the z53 "closed" items is a geometry-of-numbers statement.

## 2. Theorem A: no convex Thue scheme in natural coordinates

### 2.1 Taylor data and two facts about V_n

For t = (u, B, C) ∈ ℤ³ and h ∈ ℤ³: G(t + h) = G(t) + L_t(h) + Q_t(h) + T(h), with
L_t(h) = (4CB − 1)h_u + (4Cu − 1)h_B + 4uB·h_C, Q_t(h) = 4(C h_u h_B + u h_B h_C + B h_u h_C), T(h) = 4h_u h_B h_C.

**Fact 2.1 (smoothness; PROVED).** For every prime ℓ and every t with G_n(t) ≡ 0 (mod ℓ), L_t ≢ 0 (mod ℓ). *Proof.*
ℓ = 2: the h_u-coefficient 4CB − 1 is odd. ℓ odd: if 4CB ≡ 4Cu ≡ 1 then C, u, B are units, so 4uB ≢ 0. ∎

**Fact 2.2 (irreducibility; PROVED).** For every field k of characteristic ≠ 2 and every n ∈ k, G_n is irreducible in
k[u, B, C]; in particular V_n contains no plane. *Proof.* G_n = (4uB)·C − (u + B + n) has degree 1 in C and its two
coefficients are coprime in k[u, B] (u ∤ u + B + n, B ∤ u + B + n, 4 ≠ 0). A primitive polynomial of degree 1 in C over the
UFD k[u, B] is irreducible. A plane in V_n would give a linear factor. ∎

### 2.2 The algebraic core

**Proposition 2.3 (A1; PROVED).** Let Λ ⊆ ℤ³ have index D′, t ∈ ℤ³, and suppose G_n ≡ 0 (mod D) on Λ + t. Then
D′ ≥ D^{4/3}/c₀ with c₀ = 2⁶·3^{4/3} (< 276.92).

*Proof.* By CRT, ℤ³/Λ surjects onto ∏_{ℓ^f ∥ D} ℤ³/(Λ + ℓ^fℤ³), so D′ ≥ ∏_ℓ ℓ^{3f}/|H_ℓ| with H_ℓ := image of Λ in (ℤ/ℓ^f)³.
Fix ℓ^f ∥ D, H = H_ℓ; G(t + h) ≡ 0 (mod ℓ^f) for h ∈ H (well defined mod ℓ^f), so G(t) ≡ 0 and
  (∗) L(h)s + Q(h)s² + T(h)s³ ≡ 0 (mod ℓ^f) for all h ∈ H, s ∈ ℤ.
s = ±1 give 2Q(h) ≡ 0 and L(h) + T(h) ≡ 0; s = 2 then gives 2L + 8T ≡ −4Q ≡ 0 (mod ℓ^f, since 4Q = 2·2Q), hence 6T(h) ≡ 0.

*(a) ℓ ≥ 5.* Then L(h) ≡ Q(h) ≡ T(h) ≡ 0 (mod ℓ^f) on H. By Fact 2.1, L is primitive mod ℓ, so W := ker(L mod ℓ^f) ≅ (ℤ/ℓ^f)²
is free and H ⊆ W. Choose a basis e₁, e₂ of W adapted to H (Smith form): H = ⟨ℓ^a e₁⟩ ⊕ ⟨ℓ^b e₂⟩, 0 ≤ a ≤ b ≤ f,
|H| = ℓ^{2f−a−b}. Write Q(s₁e₁ + s₂e₂) = αs₁² + β′s₁s₂ + γs₂² and T(s₁e₁ + s₂e₂) = Σ_{i+j=3} τ_{ij}s₁^i s₂^j. Vanishing of
Q(s₁ℓ^a e₁ + s₂ℓ^b e₂) for all s₁, s₂ (take s₂ = 0, s₁ = 0, s₁ = s₂ = 1) gives αℓ^{2a} ≡ β′ℓ^{a+b} ≡ γℓ^{2b} ≡ 0. For the
cubic, s₂ = 0 and s₁ = 0 kill τ₃₀ℓ^{3a}, τ₀₃ℓ^{3b}; then s₁ = 1, s₂ = ±1 give the sum and difference of the two mixed terms,
so (2 invertible) τ₂₁ℓ^{2a+b} ≡ τ₁₂ℓ^{a+2b} ≡ 0. By Fact 2.2 (over F_ℓ) Q|_W and T|_W are not both ≡ 0 mod ℓ: otherwise
G(t + λ) ≡ 0 identically on the plane t + W mod ℓ (as a polynomial, since G(t+λ) = L + Q + T and L|_W = 0), a linear factor.
If one of α, β′, γ is a unit: α ⇒ a ≥ f/2; β′ ⇒ a + b ≥ f; γ ⇒ b ≥ f/2; in every case a + b ≥ f/2, so |H| ≤ ℓ^{3f/2}.
Otherwise some τ is a unit: τ₃₀ ⇒ a ≥ f/3; τ₂₁ ⇒ 2a + b ≥ f ⇒ a + b ≥ f − a ≥ f − (a + b)/2 (as a ≤ b), i.e.
a + b ≥ 2f/3; τ₁₂ ⇒ a + 2b ≥ f ⇒ a + b ≥ (a + 2b)/2 ≥ f/2; τ₀₃ ⇒ b ≥ f/3. In every case a + b ≥ f/3, so |H| ≤ ℓ^{5f/3}.
Hence ℓ^{3f}/|H| ≥ ℓ^{4f/3}.

*(b) ℓ = 3.* From 2Q ≡ 0: Q ≡ 0 (mod 3^f); from 6T ≡ 0: T ≡ 0 and L ≡ 0 (mod 3^{f−1}). Put g = f − 1, H̄ = H mod 3^g ⊆
ker(L mod 3^g) ≅ (ℤ/3^g)². The argument of (a) with f replaced by g (it used only that 2 is invertible and Fact 2.2) gives
|H̄| ≤ 3^{5g/3}. The kernel of (ℤ/3^f)³ → (ℤ/3^g)³ has order 27, so |H| ≤ 3^{3 + 5(f−1)/3} and 3^{3f}/|H| ≥ 3^{(4f−4)/3}.

*(c) ℓ = 2.* From 2Q ≡ 0 and 6T ≡ 0: Q, T, L ≡ 0 (mod 2^{f−1}). Write Q = 4Q′, Q′(h) = C h_u h_B + u h_B h_C + B h_u h_C,
so Q′ ≡ 0 (mod 2^g), g := f − 3 (if g ≤ 0 the bound below is trivial). On W_g := ker(L mod 2^g), h_u = −κh_B + μh_C with
κ = (4Cu − 1)(4CB − 1)^{−1} ≡ 1 (mod 2), μ = −4uB(4CB − 1)^{−1} ≡ 0 (mod 2), so in the coordinates (h_B, h_C)
Q′|_{W_g} = −Cκ h_B² + (Cμ + u − Bκ) h_B h_C + Bμ h_C², with cross coefficient ≡ u + B (mod 2). Since G(t) ≡ 0 (mod 2)
and 4CuB ≡ 0, u + B ≡ n ≡ 1 (mod 2): the cross coefficient is odd. So the polar form b(x, y) = Q′(x+y) − Q′(x) − Q′(y)
has Gram determinant 4q₁₁q₂₂ − q₁₂² odd, i.e. is unimodular on W_g. H̄ := H mod 2^g satisfies Q′ ≡ 0 on H̄, hence
b(H̄, H̄) ≡ 0, H̄ ⊆ H̄^⊥ and |H̄|² ≤ |H̄||H̄^⊥| = 2^{2g}: |H̄| ≤ 2^g. The reduction kernel has order 2⁹, so |H| ≤ 2^{f+6} and
2^{3f}/|H| ≥ 2^{2f−6} ≥ 2^{4f/3}/2⁶.

Multiplying, D′ ≥ D^{4/3}·2^{−6}·3^{−4/3}. ∎

**Cross-check (CERTIFIED; `scripts/z53_lattice_cosets.c`, exhaustive over all t ∈ V_n(ℤ/q) and all n mod q (n odd for
even q), by a DFS over subgroups generated inside {h : ⟨h⟩ ⊆ S_t}).** Largest coset |H| inside V_n(ℤ/q) and minimal
index D′ = q³/|H| for exactness modulus D = q:

| q | 2 | 3 | 4 | 5 | 7 | 8 | 9 | 11 | 16 (n = 1, 3 only) | 25 (5 ∤ n / 5 \| n) | 27 (3 ∤ n / 3 \| n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| max \|H\| | 4 | 3 | 16 | 5 | 7 | 64 | 27 | 11 | 128 | 25 / 125 | 27 / 81 |
| min D′ | 2 | 9 | 4 | 25 | 49 | 8 | 27 | 121 | 32 | 625 = q² / 125 = q^{3/2} | 729 = q² / 243 = q^{5/3} |

All are consistent with Prop 2.3 (whose exponent 4/3 is not attained in these ranges). The 2-adic planes u + B ≡ −n
(mod 8) have efficiency D′ = D = 8: on them u + B is odd, so uB is even and 4CuB ≡ 0 (mod 8), whence G ≡ −(u + B + n) ≡ 0.
(q = 16 was run for n = 1, 3 only and q = 49 did not finish within the 28-min cap — too slow for the DFS; outputs in
`data/z53/lattice/cosets_*.txt`.)

### 2.3 Convex bodies in the exactness shell

**Lemma 2.4 (V; PROVED).** Let 0 < D < n and K ⊆ (0, ∞)³ convex with |G_n| < D on K. For a, b ∈ K put
α = (u_b − u_a)/(u_a + u_b), β = (B_b − B_a)/(B_a + B_b). Then α² + β² < 4D/(n − D). Consequently, if D ≤ n/17,
vol(K) ≤ (128/9)·D²/(n − D) ≤ 15.12·D²/n.

*Proof.* Put φ = 1/(uB), f = (u + B + n)/(4uB) = ¼(1/u + 1/B + nφ), w = Dφ/4. Dividing by 4uB > 0,
|G| < D ⟺ |C − f(u, B)| < w(u, B). Let m = (a + b)/2 ∈ K. Then C_m = (C_a + C_b)/2 > ½(f(a) − w(a) + f(b) − w(b)) and
C_m < f(m) + w(m), so ½(f(a) + f(b)) − f(m) < w(m) + ½(w(a) + w(b)). Since 1/u and 1/B are convex on (0, ∞), the left side
is ≥ (n/4)(φ̄ − φ_m), φ̄ := ½(φ(a) + φ(b)); so n(φ̄ − φ_m) < D(φ_m + φ̄), i.e. R := φ̄/φ_m < (n + D)/(n − D). With
u_a = u_m(1 − α), u_b = u_m(1 + α), B similarly: R = (1 + αβ)/((1 − α²)(1 − β²)). Claim: R − 1 ≥ (α² + β²)/2. Indeed
R − 1 = Nm/((1 − α²)(1 − β²)) with Nm = α² + αβ + β² − α²β², and
Nm − ½(α² + β²)(1 − α²)(1 − β²) = ½(α + β)² + [½(α² + β²)² − α²β²] − ½(α² + β²)α²β² ≥ 0 + α²β² − α²β² = 0,
using (α² + β²)² ≥ 4α²β² and α² + β² ≤ 2. Hence (α² + β²)/2 < 2D/(n − D).
Volume: put σ² = 4D/(n − D). For any a, b ∈ K, |α| < σ, so u_b/u_a ∈ ((1 − σ)/(1 + σ), (1 + σ)/(1 − σ)): the range of
log u over K has length ≤ λ := log((1 + σ)/(1 − σ)), likewise log B. Each fibre {C : (u, B, C) ∈ K} has length ≤ 2w, so
vol K ≤ ∫_{proj K} (D/2) du dB/(uB) ≤ (D/2)λ². For D ≤ n/17, σ ≤ 1/2 and λ = 2 artanh σ ≤ 2σ/(1 − σ²) ≤ (8/3)σ, so
vol K ≤ (D/2)(64/9)·4D/(n − D) = (128/9)D²/(n − D) ≤ (128·17)/(9·16)·D²/n. ∎

(The inequality R − 1 ≥ (α² + β²)/2 was also checked on a 1999² grid of (α, β) ∈ (−1, 1)², min = 0; `/tmp`-free script
`scripts/z53_lattice_checks.py`.)

**Lemma 2.5 (W; PROVED).** If K ⊆ [1, ∞)³ is measurable with |G_n| < D on K, then vol K ≤ (D/4)·log²((n + D)/2).
*Proof.* Fibres have length ≤ 2w = D/(2uB). A nonempty fibre with C ≥ 1 needs f + w > 1, i.e. 4uB < u + B + n + D ≤
2uB + n + D (u, B ≥ 1), so uB < X := (n + D)/2; and ∫∫_{u, B ≥ 1, uB ≤ X} du dB/(uB) = ½ log²X. ∎

### 2.4 The theorem

**Theorem 2.6 (A; PROVED).** For every odd n ≥ 1.34·10¹⁶ there is no convex Thue scheme (Def. 1.1) for (★) at n.
The same holds for every affine-linear encoding: if Φ(v) = Av + c with A ∈ ℤ^{3×k} of rank 3, Λ + t ⊆ ℤ^k,
G_n∘Φ ≡ 0 (mod D) on Λ + t, K ⊆ ℝ^k convex with Φ(K) ⊆ [1,∞)³, |G_n∘Φ| < D on K and K + Λ = ℝ^k, then
(AΛ, At + c, D, Φ(K)) is a convex Thue scheme in natural coordinates, so none exists for n ≥ 1.34·10¹⁶.

*Proof.* Let a scheme exist. By (V), vol K ≥ D′ ≥ D^{4/3}/c₀ (Prop 2.3).
Case D ≤ n/17: Lemma 2.4 gives D^{4/3}/c₀ ≤ (128/9)D²/(n − D), i.e. n ≤ D + (128/9)c₀D^{2/3} ≤ n/17 + (128/9)c₀(n/17)^{2/3},
false for n ≥ 2.6·10⁸.
Case D > n/17: Lemma 2.5 and (n + D)/2 < 9D give D^{1/3} ≤ (c₀/4)log²(9D), which forces D < 7.84·10¹⁴ (the function
D^{1/3} − 69.23 log²(9D) is negative on [1, 7.835·10¹⁴] and positive beyond); then n < 17D < 1.34·10¹⁶.
Encodings: AΛ ⊆ ℤ³ has finite index and AΛ + (At + c) = Φ(Λ + t); G ≡ 0 (mod D) there; Φ(K) is convex, inside the shell and
in [1, ∞)³; and K + Λ = ℝ^k gives Φ(K) + AΛ = A(ℝ^k) + c = ℝ³. ∎

(Numbers: `scripts/z53_lattice_checks.py`. Since ES is verified to 10¹⁷, the threshold is immaterial; it can be lowered by
using the observed D′ ≥ D^{3/2}.)

**Reading (Assessment).** Thue works because the target p sits at the *bottom* of a definite form: the exactness window
{0 < x² + y² < 2p} is a fat convex disc of area ≍ covolume. For (★) the target n sits far from the bottom of a cubic with an
elliptic level surface: the exactness window {|G| < D} is a shell of thickness ≲ D/n^{2/3}, convex pieces have volume
≪ D²/n, while every exactness coset has index ≥ D^{4/3}/c₀ (and in fact ≥ D^{3/2} in all computed cases). Both halves of
Thue's argument fail, independently.

## 3. Fixed C, the hyperbola coordinates, and the non-convex escape

### 3.1 Theorem A′: at fixed C a Thue scheme must be handed a divisor of N_C

Fix C ≥ 1 and work in (u, B) ∈ ℤ² with g(u, B) := 4CuB − u − B − n. A *fixed-C convex Thue scheme* is (Λ, t, D, K) with
Λ ⊆ ℤ² of index D′, g ≡ 0 (mod D) on Λ + t, K ⊆ [1, ∞)² convex, |g| < D on K, K + Λ = ℝ².

**Theorem 3.1 (A′; PROVED).** For such a scheme: if D ≤ n/7 then gcd(D, N_C) ≥ Cn/114 > N_C/456; if D > n/7 then
gcd(D, N_C) ≥ C·D/(8 log²(2(n + D + 1))).

*Proof.* Local indices. With X_t Y_t = 4C g(t) + N_C and g(t + h) − g(t) = L(h) + 4Ch_uh_B, L(h) = Y_t h_u + X_t h_B,
(∗) with s = ±1 gives 2·4Ch_uh_B ≡ 0, 2L(h) ≡ 0 (mod ℓ^f) on H = Λ mod ℓ^f.
(i) ℓ ∤ 4C, e := v_ℓ(N_C) (e = 0 allowed): then h_uh_B ≡ 0, L ≡ 0; H is isotropic for the hyperbolic form and lies in ker L.
If f ≤ e: |H| ≤ ℓ^f (the polar form of h_uh_B is unimodular). If f > e: let v(X_t) = i, v(Y_t) = j, i + j = e (as
X_tY_t ≡ N_C mod ℓ^f and e < f); the projection h ↦ h_u has kernel {(0, h_B) : X_t h_B ≡ 0}, of order ≤ ℓ^i, and image
ℓ^aℤ/ℓ^f, where for h with v(h_u) = a, L(h) ≡ 0 forces v(h_B) = j + a − i when j + a < f, and then h_uh_B ≡ 0 forces
2a + j − i ≥ f (if j + a ≥ f the same inequality holds as f ≥ e); so |H| ≤ ℓ^{f − a + i} ≤ ℓ^{(f+e)/2}. In both cases
ℓ^{2f}/|H| ≥ ℓ^{min(f,e)}·ℓ^{3(f − min(f,e))/2}.
(ii) ℓ | 4C, c := v_ℓ(4C), ν := v_ℓ(2): h_uh_B ≡ 0 (mod ℓ^{f−c−ν}), L ≡ 0 (mod ℓ^{f−ν}), both L-coefficients ≡ −1
(mod ℓ), so h_B ≡ −κh_u with κ a unit and h_u² ≡ 0 (mod ℓ^{f−c−ν}); counting as in Prop 2.3(c),
ℓ^{2f}/|H| ≥ ℓ^{(3f − c − 3ν)/2}.
Multiplying: D′ ≥ gcd(D, N_C)·(D_∗/gcd(D, N_C))^{3/2}·D_C^{3/2}/(2^{3/2}(4C)^{1/2}), where D = D_∗D_C with D_∗ prime to 4C.
Area. |g| < D ⟺ |B − ĝ(u)| < Dψ(u) with ψ = 1/(4Cu − 1), ĝ = 1/(4C) + n′ψ, n′ = n + 1/(4C). The midpoint argument of Lemma
2.4 (v := 4Cu − 1 is affine, ψ = 1/v) gives, for a, b ∈ K, α² < 2D/(n′ + D), α = (v_b − v_a)/(v_a + v_b). If D ≤ n/7 then
σ := (2D/(n′ + D))^{1/2} ≤ 1/2, log(v_max/v_min) ≤ (8/3)σ and area K ≤ ∫ 2Dψ du ≤ (D/2C)(8/3)σ ≤ (4√2/3)D^{3/2}/(C√n).
Comparing with D′ ≤ area K: C√n ≤ (4√2/3)·2^{3/2}·2√C·gcd(D, N_C)^{1/2} = (32/3)√C·gcd(D, N_C)^{1/2}. If D > n/7: a
nonempty fibre needs u ≤ (n + D + 1)/(4C − 1), so area K ≤ (D/2C)·log(2(n + D + 1)), and the same comparison gives
D/gcd(D, N_C) ≤ 8 log²(2(n + D + 1))/C. Since gcd(D, N_C) ≤ N_C, this forces D ≤ 8(4n + 1)log²(2(n + D + 1)), hence
D ≤ n² for all large n, and then (D > n/7) N_C/gcd(D, N_C) ≤ 56(4 + 1/(Cn))·log²(2(n + D + 1)) ≤ 225·log²(4n²) = O(log²n). ∎

**Reading.** At a fixed level, Thue-exactness is possible only if the scheme's modulus contains a divisor d of N_C with
N_C/d ≤ 456 (thin case; ≪ log²n in the thick case) — i.e. the scheme must be *given* (almost) the factorization of the one
integer N_C whose divisor in the class −1 mod 4C is sought. The lattice contributes nothing beyond the divisor. (B2
verbatim, now as a theorem about the Thue mechanism.)

### 3.2 Prop D: in hyperbola coordinates the class condition is not a lattice condition

In (X, Y, C) the variety XY = 4nC + 1 is a quadric, ruled (C is a quadratic function of (X, Y)); exactness cosets exist
(e.g. X ≡ x₀, Y ≡ x₀^{−1}(1 + 4nC) mod D; index D²). The (★) solutions are the points with 4C | X + 1 (then 4C | Y + 1).

**Proposition 3.2 (D; PROVED).** No full-rank lattice coset Λ + t ⊆ ℤ³ (coordinates (X, Y, C)) has 4C | X + 1 at all of its
points with C ≥ 1, unless all those points have X = −1.
*Proof.* Λ ⊇ D′ℤ³. If (X, Y, C) ∈ Λ + t with C ≥ 1, then (X, Y, C + kD′) ∈ Λ + t for all k ≥ 0, so 4(C + kD′) | X + 1 for
all k; hence X + 1 = 0. ∎

**Reading (Assessment).** In natural coordinates the class condition is built in (linear) and the variety has no exactness
cosets (Thm 2.6); in hyperbola coordinates the variety has exactness cosets and the class condition is tied to the height C
(Prop 3.2); at fixed C the class is linear and exactness costs the factorization (Thm 3.1). These are PARITY_AUDIT Remark
3.1's "two descriptions of one obstruction" (and FRONTIER's M1b), now each a theorem about lattice pigeonhole.

### 3.3 The non-convex escape (Remark A3)

Drop convexity: a coset Λ + t with G ≡ 0 (mod D) and any region S ⊆ {|G| < D} ∩ [1,∞)³ — then every coset point of S is a
(★) triple, so #((Λ + t) ∩ S) ≤ R(n): a **sub-count** of R(n). Its volume heuristic is vol(S)/D′ ≤ (D/4)log²((n + D)/2)/D′
≤ (c₀/4)D^{−1/3}log²((n + D)/2) (Lemma 2.5, Prop 2.3) — never above a constant times the trivial-lattice mass ¼log²n
(the shell |G| < 1 has volume ≈ ¼log²n = twice the all-integer mean ⅛log²n, the factor 2 being the G-window length).
Lower-bounding it is the §7.1 problem (lattice points of a thin curved shell / the height-tied hyperbola) with an extra
congruence. Assessment: **no lattice amplifies the lottery**; the escape from Theorem A is exactly the hyperbola lanes'
problem, never an easier one.

## 4. Theorem B: polynomial (non-linear) encodings

**Lemma 4.1 (polynomial curves on V_n; PROVED).** Let k be a field, char k ≠ 2, n ∈ k. Every polynomial map
s ↦ (u(s), B(s), C(s)) ∈ k[s]³ with image in V_n is constant or has image inside one of the lines
L₁ = {u = 0, B = −n}, L₂ = {B = 0, u = −n}, L₃ = {C = 0, u + B = −n}, L₄ = {B = −n, 4nC = −1}, L₅ = {u = −n, 4nC = −1}
(L₄, L₅ only if n ≠ 0; for n = 0, L₁ = L₂ = {u = B = 0}). The intersection graph of L₁…L₅ is the 5-cycle
L₁–L₃–L₂–L₅–L₄–L₁ (n ≠ 0); in particular no three of them are pairwise concurrent.
*Proof.* If u + B + n ≠ 0 in k[s], then deg C + deg u + deg B = deg(u + B + n) ≤ max(deg u, deg B), so C and one of u, B
are constant; say B = b, C = c: (4cb − 1)u = b + n, so u is constant unless 4cb = 1 and b = −n (line L₄); symmetric (L₅). If
u + B + n = 0 then 4CuB = 0: C = 0 (L₃), u = 0 (L₁) or B = 0 (L₂). Intersections: L₁∩L₃ = (0, −n, 0), L₁∩L₄ = (0, −n, −1/4n),
L₂∩L₃ = (−n, 0, 0), L₂∩L₅ = (−n, 0, −1/4n), L₄∩L₅ = (−n, −n, −1/4n); the other five pairs are disjoint (n ≠ 0). ∎

**Corollary 4.2.** For d ≥ 1, a polynomial map Ψ: A^d → V_n over an infinite field (char ≠ 2) is constant or has image in a
single L_i. *Proof.* Restricting to the line through x, y shows any two distinct image points lie on a common L_i. If
P ≠ Q lie on L_i and R ∉ L_i, the lines through {P, R}, {Q, R} are distinct, distinct from L_i, and the three are pairwise
concurrent — impossible by Lemma 4.1. ∎

**Theorem 4.3 (B; PROVED).** Let Φ ∈ ℤ[x₁, …, x_k]³ have total degree ≤ δ (coefficients arbitrary, e.g. depending on n), ℓ
an odd prime with ℓ > 3δ, and Λ + t ⊆ ℤ^k a coset with G_n∘Φ ≡ 0 (mod ℓ) on Λ + t whose image W ⊆ F_ℓ^k has dim W ≥ 1.
Then Φ(W) (mod ℓ) is a single point or lies in one L_i (mod ℓ). In words: the exactness prime ℓ either pins (u, B, C) mod ℓ,
or forces ℓ | u (L₁), ℓ | B (L₂), ℓ | C (L₃), ℓ | Y = 4CB − 1 with ℓ | N_C (L₄), or ℓ | X (L₅) on the whole coset.
*Proof.* Parametrize W affinely by F_ℓ^d. G_n∘Φ restricted to W has degree ≤ 3δ < ℓ in each variable and vanishes on F_ℓ^d,
hence is the zero polynomial; Cor 4.2 over F̄_ℓ. On L₄: Y = 4CB − 1 ≡ −4Cn − 1 ≡ 0. ∎

**Reading (Assessment).** For positive-dimensional exactness cosets, a polynomial encoding can only (a) fix residues of the
solution or (b) prescribe a prime ℓ dividing one of u, B, C, X, Y — the *transparent certificate* shape of B4
(LONGSHOT_PIGEONHOLE Thm 2.2: certificates built from residues of prescribed small prime factors fail on a positive-density
set). Theorem B is structural only (no volume bound for non-linear encodings); encodings of degree ≥ ℓ/3 (e.g. through
modular inversion x ↦ x^{−1} mod p, which is the hyperbola again) are outside its scope.

## 5. Coppersmith, Lenstra, CHN

**5.1 Regimes (PROVED, elementary).** In the C-slice the target is a divisor of N_C ≡ −1 (mod s = 4C): Lenstra (≤ 11 such
divisors, poly-time) needs s³ > N_C, i.e. 16C² > n + 1/(4C) (C ≳ √n/4); Coppersmith–Howgrave-Graham–Nagaraj (CHN; s > N^{α},
α > 1/4) needs s ≥ N_C^{1/4+ε}, whose boundary s⁴ > N_C is C ≳ (n/64)^{1/3} (we call "CHN-visible" the boundary condition s⁴ > N; the
CHN count bound O((α − 1/4)^{−3/2}) degenerates there). In the u-slice: divisors of n + u ≡ −1 (mod 4u): Lenstra needs 64u³ > n + u, CHN
256u⁴ > n + u. *Coppersmith's integer bivariate theorem* (Coppersmith, J. Cryptology 10 (1997), Thm 2, as restated verbatim in Coron,
EUROCRYPT 2004, LNCS 3027, Thm 2 — read in the source: for irreducible p(x, y) ∈ ℤ[x, y] of degree ≤ δ in each variable,
all integer roots with |x| ≤ X, |y| ≤ Y are found in time poly(log W, 2^δ) if XY < W^{2/(3δ)}, W = max|p_ij|X^iY^j; Coron
§2 treats exactly p = a + bx + cy + dxy, δ = 1, bound XY < W^{2/3}) applied to P_C(u, B) = 4CuB − u − B − n: roots have
uB ≈ n/4C, W = max(4CXY, X, Y, n), and when 4CXY ≥ n, XY < (4CXY)^{2/3} ⟺ XY < 16C²; so the solutions are reachable iff
n/(4C) ≲ 16C², i.e. C ≳ (n/64)^{1/3}: exactly the CHN boundary.
**Mass shares (PROVED, heuristic density 1/(4uB) per pair, all-integer normalization M ∼ ⅛log²n).** In log-coordinates
(x, y) = (log u, log B)/log n the mass Σ 1/(4uB) is ¼log²n times Lebesgue measure on the triangle x, y ≥ 0, x + y ≤ 1 (area ½).
C-Lenstra ⟺ C > √n/4 ⟺ uB < √n ⟺ x + y < ½: share (½·¼)/(½) = 1/4; C-CHN ⟺ uB < n^{2/3}: (2/3)² = 4/9; u-CHN ⟺ u > n^{1/4}: 9/16; u-Lenstra: 4/9; CHN-visible in some slice: all (u, B <
n^{1/4} forces uB < √n, hence C-Lenstra); Lenstra-invisible: x, y < 1/3, x + y > 1/2, share 1/36.
**Measured (EVIDENCE; `scripts/z53_lattice_regimes.c`, `data/z53/lattice/regimes_*.txt`).**

| sample | N | mean R | mean R/log²n | C-Lenstra | C-CHN | u-Lenstra | u-CHN | any Lenstra | any CHN |
|---|---|---|---|---|---|---|---|---|---|
| primes ≡ 1 (24) after 10⁷ | 2000 | 37.5 | 0.144 | 0.286 | 0.509 | 0.541 | 0.672 | 1.000 | 1.000 |
| primes ≡ 1 (24) after 10⁹ | 400 | 62.4 | 0.145 | 0.281 | 0.495 | 0.515 | 0.642 | 0.998 | 1.000 |
| near-squares m² + k ≡ 1 (24), k < 60, m ≈ 3163 | 400 | 33.1 | 0.123 | 0.286 | 0.495 | 0.539 | 0.681 | 1.000 | 1.000 |
| asymptotic | | | | 0.25 | 0.444 | 0.444 | 0.5625 | 0.972 | 1 |

Odd squares (200 values near 10⁷): R = 0 throughout (T1). The 14 (★)-zero primes: R = 0; b = 1 failures 193, 2521, 66529
and 3361, 5101441 have R = 4, 2, 8, 2, 10, all CHN-visible.

**5.2 No existence content (PROVED, elementary; Assessment for the reading).** (a) Howgrave-Graham's lemma — if h(x₀) ≡ 0
(mod N^m) and |h(x₀)| < N^m then h(x₀) = 0 — is Thue-exactness, applied to a root x₀ *assumed* to exist; the method's
guarantee is "every small root of P is a root of the reduced h", whose converse fails. (b) The CHN/Coppersmith lattice for
(N_C, r = −1, s = 4C) has dimension, determinant and LLL bounds depending only on the sizes of N_C, s, X, Y; for n = m² (m odd)
every slice has an empty root set (T1: m² + u has no divisor ≡ −1 mod 4u, FRONTIER B5), with the same guarantees. Hence no
statement deduced from those guarantees implies a root. (c) The visibility result (every triple CHN-visible somewhere) is an
algorithmic statement: ≍ n C-slices and ≍ n^{1/2} u-slices in the CHN regimes, each decided in poly(log n), which is no
better than the lottery picture (s3_lll_lenstra).

## 6. Natural lattice invariants at hard primes vs controls (EVIDENCE)

Thue lattice Λ_ι(p) = ℤ(a, b) ⊕ ℤ(−b, a) (p = a² + b², a > b) is a *square* lattice for every p, so its successive minima carry
no information; its orientation b/a and the near-square defect p − ⌊√p⌋² do.
* Primes ≡ 1 (24) after 10⁷ (2000): corr(R/log²p, b/a) = −0.018, corr(R/log²p, log(1 + defect)) = 0.065; after 10⁹ (400):
  −0.011, −0.004. No signal at the level of individual primes.
* The 14 (★)-zero primes (409 … 8 813 281): b/a = 0.150, 0.042, 0.635, 0.253, 0.304, 0.715, 0.803, 0.674, 0.658, 0.0038,
  0.379, 0.655, 0.052, 0.081: six below 0.16 (b/a < 0.16 has probability ≈ arctan(0.16)/(π/4) ≈ 0.20 for a uniform angle;
  binomial tail P(≥ 6 of 14) = 0.046). Near-squares (k < 60) have mean R/log²p = 0.123 vs 0.144: the known T1 deformation
  ((J)53, (J)55), already in FRONTIER §3 B5.
Assessment: the natural 2-dimensional lattices see near-squareness and nothing else; the successive-minima questions the
kickoff asked about are vacuous for Λ_ι (square) and, for the (★) shell, are replaced by Theorem A.

## 7. Screens (FRONTIER §4) for the lattice route

| screen | lattice pigeonhole (Thue/Minkowski/Coppersmith) |
|---|---|
| T1 (odd squares) | Theorem A holds for all n ≥ n₀ including squares — as it must for a no-go; the *route* would have to fail at squares, and Coppersmith's guarantees (§5.2) visibly do not. Fails screen 1 as a positive mechanism. |
| 8/131 (numerator) | the proofs use only smoothness/irreducibility of 4CuB − u − B − n and its Hessian; the same theorems hold for kCuB − u − B − n, k ≥ 4 (constants change). Numerator-blind, hence no positive mechanism. |
| tied modulus | Theorems 2.6, 3.1 and Prop 3.2 *are* the tied-modulus screen made precise for lattices: linear class ⇒ no exactness cosets; exactness cosets ⇒ class tied to height; fixed C ⇒ factorization needed. |
| fixed p | geometry of numbers is pointwise (passes); no averaged input anywhere. |

## 8. Verdict

**Narrowed.** Killed as scoped theorems:
* every convex Thue scheme in natural coordinates and every affine-linear encoding (Thm 2.6, n ≥ 1.34·10¹⁶);
* every fixed-level Thue scheme not handed a divisor d | N_C with N_C/d ≤ 456 (resp. ≪ log²n) (Thm 3.1);
* lattice cosets carrying the class condition in hyperbola coordinates (Prop 3.2);
* positive-dimensional exactness primes of polynomial encodings beyond "pin or designate a prime factor" (Thm 4.3);
* any existence content of the Coppersmith/CHN/Lenstra lattices (§5.2).
Survives: (i) non-convex counting — the §7.1 shell/hyperbola problem with an extra congruence (Remark 3.3); (ii) encodings of
degree ≥ ℓ/3, e.g. through modular inversion (= the modular hyperbola); (iii) exponent-lattice covering ((J)85, needs
sub-power windows). None is a geometry-of-numbers existence mechanism.

**What it buys.** FRONTIER's M1b row stops being an Assessment: "Thue/Minkowski pigeonhole cannot certify (★)" is now a
theorem with explicit scope, and the reason is quantitative (index ≥ D^{4/3}/c₀ vs convex volume ≤ 15D²/n), not "the target
depends on the height" in words.

## 9. Proposed FRONTIER text (do not edit FRONTIER here)

*§3, M1b row, replace "target class depends on the exact height; covering needs sub-power windows ((J)85)" by:* "Thue/
Minkowski exactness is impossible: no lattice coset of index D′ and convex body K with 4CuB − u − B ≡ n (mod D) on the coset,
|·−n| < D on K and K + Λ = ℝ³ exists for n ≥ 1.34·10¹⁶ (D′ ≥ D^{4/3}/277, vol K ≤ 15D²/n); at fixed C a Thue scheme needs a
divisor of 4Cn + 1 of cofactor ≤ 456; in hyperbola coordinates the class condition is on no lattice coset (`Z53_LATTICE.md`
Thms 2.6, 3.1, Prop 3.2; PROVED). Covering needs sub-power windows ((J)85)."
*§6, add:* "Geometry-of-numbers / Thue / Minkowski / Coppersmith certificates for (★) → no exactness cosets in natural or
affine coordinates, factorization needed at fixed level, class tied in hyperbola coordinates; Coppersmith has no existence
content (T1-uniform) → `Z53_LATTICE.md` (z53)."

**Bottom line.** Lattice pigeonhole proves p = x² + y² because the target sits at the bottom of a definite form, so the
exactness window is a fat disc and the exactness lattice has index equal to the modulus. For (★) both features fail, and
we prove it: every lattice coset on which 4CuB − u − B ≡ n (mod D) has index ≥ D^{4/3}/277 (≥ D^{3/2} in every computed
case), while every convex body on which |4CuB − u − B − n| < D has volume ≤ 15D²/n, so no Thue/Minkowski certificate exists
in natural or affine coordinates (n ≥ 1.34·10¹⁶). At a fixed level the only Thue schemes are those handed most of the
factorization of 4Cn + 1, and in hyperbola coordinates, where exactness is possible, the class condition is not a lattice
condition. Coppersmith/LLL only ever propagate an assumed root. What remains is lattice-point counting in a thin curved shell
— the §7.1 problem — so the LATTICE lane narrows to the hyperbola lanes and adds no independent route. ES remains open.

## 10. Reproduction

* `gcc -O2 -o /tmp/z53cos scripts/z53_lattice_cosets.c; ulimit -v 2000000; timeout 900 /tmp/z53cos q [nstep] [tstep] [nstart]`
  (q = 2…11 in < 10 s each; 25: ≈ 6 min; 27: ≈ 25 min; 16, 49: slow, sampled) → `data/z53/lattice/cosets_*.txt`.
* `gcc -O2 -o /tmp/z53reg scripts/z53_lattice_regimes.c -lm; timeout 900 /tmp/z53reg -f list.txt` (lists: primes ≡ 1 (24)
  after 10⁷ (2000) and 10⁹ (400), odd squares and near-squares near 10⁷, generated by sympy, seed-free `nextprime` walk;
  lists in `data/z53/lattice/`), summary `scripts/z53_lattice_regimes_summary.py`.
* `ulimit -v 6000000; uv run --with numpy python scripts/z53_lattice_checks.py` (inequality grid, constants c₀, D₁, n₀).
