# Z54_BILINJAC — depth lane BILINJAC (wave z54, gap 1): bilinear (ℓ, C) cancellation for the square sieve at the balanced block; the quadratic-character (Jacobi-symbol) toolbox

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound work only**: even complete success (a power
saving N(balanced) ≪ p^{1/4−η}) says nothing about positivity of R(p); its value is the FRONTIER §7.1 benchmark and method.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results, internally reviewed only.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z54_lanes.md` §BILINJAC. Predecessor: `Z53_SQSIEVE.md`
(Prop B2, §5.2 Remarks 1–3). Scripts `scripts/z54_bilinjac_*`, data `data/z54/bilinjac/`.

*Status: CHECKPOINT 1 (skeleton + first falsifier + first lemma).*

## 0. Notation (as in SQSIEVE)
(★) 4uBC − u − B = n; block 𝔅(U,V,W): u ∈ (U,2U], B ∈ (V,2V], C ∈ (W,2W], N(U,V,W) its count. Strip coordinates
k = uB, s = u + B = 4Ck − n, f(C,k) = s² − 4k = (u − B)² on solutions. χ_Q = Jacobi symbol mod Q = qq′ (q ≠ q′ odd primes
in (P,2P], P₀ of them). Strip weight ω(C,k) = 1_{(W,2W]}(C)Φ((4Ck − n)/V), w(a) = Σ_{f(C,k)=a} ω, 𝒜 = supp ω,
S_Q = Σ ω(C,k)χ_Q(f(C,k)). **Balanced block:** U ≍ V ≍ n^{1/4}, W ≍ n^{1/2}; then |𝒜| ≍ V and each C carries ≤ 1 point.

## 1. Statements attacked
**(T) Target (FRONTIER §7.1 open item).** ∃ η > 0: N(U,V,W) ≪ n^{1/4−η} uniformly in odd n (or at primes p ≡ 1 (24)) for
the balanced block. Trivial: N ≤ n^{1/4+o(1)} (Z52D Thm 1).
**(T′) Square-sieve form.** By SQSIEVE (4.1), (T) follows from max_{q≠q′∈𝒫}|S_{qq′}| ≪ V^{1−η} for some P = V^{c}, c > 0
(or from the average P₀^{−2}|Σ_{q≠q′}S_{qq′}|).
**(B) The bilinear forms** (exact; §2 below): S_Q as (i) a Q-periodic twist of a lattice-point count in a thin hyperbolic
strip, (ii) a χ_Q-twisted divisor sum over divisors near √m of m in an interval of length m^{1/4}, (iii) the Poisson
(ℓ, C) form Σ_{ℓ,C} a_ℓ(C)e(−ℓn/(4CQ))G_C(ℓ) with Kloosterman coefficients, (iv) the additive-twist form
Σ_{(a,b)}ĝ(a,b)T(a,b), and (v) the real-character bilinear form Σ_{Q}Σ_a β_Q w(a)(a/Q) seen by the Jacobi-symbol tools.
**Task:** prove a power saving for (T′), or prove for each tool class (Heath-Brown's real-character large sieve, bilinear
Jacobi-symbol bounds (Friedlander–Iwaniec, Conrey–Farmer–Soundararajan), Duke–Friedlander–Iwaniec bilinear Kloosterman
fractions, Pólya–Vinogradov/Burgess in either variable, the double large sieve) a scoped no-go with the exact deficit.

## 2. Why this is not already closed
SQSIEVE Prop B2 closes only the k-Poisson implementation with triangle inequality over ℓ and c₀ (Q ≤ W) and per-class
C-sum majorants; its Remark 3 (large sieve) is an unproved Assessment; no real-character bilinear tool was examined.
HYPKLOOST covers DFI/Bettin–Chandee for Kloosterman fractions in the hyperbola model (necessary conditions only);
HYP2CYCLE Prop D closes the black-box determinant method. The tools named in the kickoff act on the *character* side
(the modulus Q and the values a = f), which none of these touched.

## 3. First falsifier (EVIDENCE; CERTIFIED for the stated range) — the truth at the balanced block is tiny
`scripts/z54_bilinjac_census.c`: for every odd n ≤ 10⁹, N_bal(n) := #{(★) triples with n^{1/4}/2 < u, B ≤ 2n^{1/4}}
(a union of O(1) dyadic blocks around the balanced block). Output `data/z54/bilinjac/census_1e9.txt`:
mean N_bal = 0.4805 in every decade from 10⁵ to 10⁹ (= (ln 4)²/4 = 0.4805, the density prediction);
**max N_bal = 20 over all odd n ≤ 10⁹** (n = 635 674 641 = 3·7·30 270 221, n^{1/4} = 158.8); 14 over primes p ≡ 1 (24)
(p = 250 810 249); 0 at every odd square (T1). Decade maxima 6, 8, 8, 12, 16, 20. So (T) is true numerically with an
enormous margin (N_bal = n^{o(1)}-like); the question is purely one of proof technology.

## 4. First lemma (PROVED; full proof in §5): square-mimic obstruction for character-side tools
Any square-sieve input that bounds Σ_{q≠q′}S_{qq′}(w) through quantities of w that are shared by a weight supported on
squares — (a) sup-norm, support size and range [1, X]; (b) the square-class ℓ²-mass D(w) = Σ_{aa′=□}w(a)w(a′) used by
Heath-Brown's real-character large sieve — returns at best the trivial bound (a), resp. a bound that needs D(w) ≥ N² as input
(circular) (b). (Statement and proof: §5.)

*(Further sections — computations of the actual bilinear sums at 10¹⁰–10¹⁴, the tool-by-tool deficits, the calibration of
the balanced block against short-interval divisor sums, screens, verdict — to follow.)*
