# NONCONG_LIFTS — non-congruential lifts and the numerator-model laboratory (O257, spark relay on O253 SHARP 1+2)

Status: **ES is OPEN.** Nothing below proves ES or an infinite case of it. Labels as in DISCOVERIES.md.
Scripts `scripts/z28_*`; memos `BRAINSTORM/z28_*.md`; logs `logs/z28_*` (tiny).
Base: AMPLIFY_EXCEPTION.md (O253): Thm 3.1 (determined lifts, exact gate), Thm 3.2 (T1 adversary: p ≡ □ (mod L) ⟹ no
ET witness with H | L), Cor 3.3 (joint recombination needs a source without invisible witnesses), Thm 2.5 (models).

## 0. Notation (numerator k)

For k ≥ 4 and n ≥ 2: S_k = {n : k/n = 1/x + 1/y + 1/z solvable in positive integers}, E_k = complement.
A *witness* at a prime p ∤ k is w = (θ, a, b, c, d) with e := (a+b)/c ∈ ℤ_{>0} and
N_θ(p) = k·a·b·d, where N_II(p) = p + e, N_I(p) = pe + 1; the solution is
(abd, acdp, bcdp) (Type II) or (abdp, acd, bcd) (Type I) (same algebra as ET with 4 → k; e.g. Type II:
1/(abd) + 1/(acdp) + 1/(bcdp) = (cp + a + b)/(abcdp) = k/p ⟺ p + e = kabd). H(w) := kab is the *modulus*, the *slice*
σ(w) = (θ, a, b, c). For prime p ∤ k every solution is Type I or II (p | all three would force k ≤ 3/1·…, impossible
for k ≥ 4: k/p = (1/x′ + 1/y′ + 1/z′)/p needs k ≤ 3).
**Full T1 for 4 | k** (DISCOVERIES (J)49 SHARP 2, PROVED: ET §4 via d ↦ hd; Schinzel 2000): no odd square m² has a
Type I/II solution of k/m². Hence O253 Thm 3.2 holds verbatim for every k ≡ 0 (mod 4) with H = kab.
(Attribution, per R266 D-T32a: O253 Thm 3.2 is the classical Mordell–Schinzel square-class obstruction in local
form — ET Prop 1.6 and ET p. 8, Schinzel 2000; campaign T1, DISCOVERIES (C)2/(C)7. Only Cor 3.3's recombination
packaging is O253's. Below, Thm 1.2(ii) and Prop 1.3 are therefore classical in substance; what is new here is the
slice-level / witness-level split and its consequences.)
The models k = 8, 12, 16, 20, 24 therefore share T1 *and* the T1 adversary with ES, and have genuine exceptions.

## 1. What a lift is, and which lifts escape Cor 3.3

A *source scheme* gives, for each target prime p, a source prime q = q(p) (e.g. p = αq + β). A *lift rule* Λ maps
(p, w′) with w′ ∈ W_k(q) to a candidate slice (θ, a, b, c); it is *valid* if k·a·b | N_θ(p) (d := N_θ(p)/kab ≥ 1
then gives a witness). A law "q ∈ S_k ⟹ p ∈ S_k" is *proved by Λ* if Λ is valid at every w′ ∈ W_k(q) (totality:
the hypothesis q ∈ S_k supplies *some* witness, not a chosen one; O253 Cor 3.3 scope).

**Definition 1.1 (information level).** Λ is *congruence-mediated of level M* if its output depends on p only
through p mod M, where M = M(w′) is an even integer computed from w′ with gcd(p, M) = 1, and its proof establishes validity for
*every* prime p′ ≡ p (mod M) (with the same w′). The level is *slice-level* if M depends only on σ(w′) (then
M ≤ C(σ(w′)) is bounded on each slice — the determined lifts of O253 Thm 3.1 have M = αH′), and *witness-level*
if it genuinely depends on the size parameter d′ (equivalently on q, since q = (N′ − e′) or (N′ − 1)/e′ with
N′ = kH′-multiple k a′b′d′).

**Theorem 1.2 (level dichotomy; PROVED).** Let 4 | k, p an odd prime, M even with gcd(p, M) = 1 (R-O257 F1: without
it the class of p mod M may contain no other prime — k = 4, p = 17, M = 34, slice (1, 6, 1) is a counterexample to
both conclusions), and suppose a slice (θ, a, b, c) is
valid at every prime p′ ≡ p (mod M). Then (i) k a b | M, and (ii) p is *not* congruent to a square modulo M.
Consequently: (a) a slice-level lift must, at every supplied source witness, see a non-square residue of p modulo
M(σ(w′)), and O253 Cor 3.3 applies verbatim (lcm of invisible slice-levels is invisible); (b) a witness-level lift
of level M(w′) is valid iff N_θ(p) has the divisor kab | M(w′) with (a + b)/c = e — a divisor event whose modulus is
built from the size d′ of the source solution (B2), and Theorem 1.2(ii) is then no restriction in practice
(M(w′) ≍ q has prime factors ℓ with (p/ℓ) = −1 for all but a thin set of q).
*Proof.* (i) For each prime ℓ | kab, ℓ ≠ p, pick t_ℓ (mod ℓ) with t_ℓ ≢ 0 and p + t_ℓM ≢ 0 (mod ℓ): for ℓ = 2 any odd
t works (M even, p odd); for odd ℓ | M any t ≢ 0 works (p + tM ≡ p ≢ 0); for odd ℓ ∤ M exactly one class t is bad,
leaving ≥ ℓ − 2 ≥ 1 non-zero good classes. (ℓ = p does not divide kab: p ∤ ab by ET normalisation at a prime, and
p ∤ k.) The progression {p + tM : t ≡ t_ℓ (mod ℓ) ∀ℓ | kab} is p + M·(t₀ + s·rad(kab)), whose difference
M·rad(kab) is coprime to its first term (primes of M do not divide p since gcd(p, M) = 1; primes ℓ | kab, ℓ ∤ M, do
not divide p + t_ℓM by the choice of t_ℓ); so by Dirichlet there is a prime p′ = p + tM with gcd(t, kab) = 1. Validity at p and p′:
Type II: kab | (p′ + e) − (p + e) = tM, so kab | M. Type I: kab | (p′e + 1) − (pe + 1) = tMe and gcd(e, kab) = 1
(from kab·d = pe + 1), so kab | M. (ii) Then the slice is an ET witness at p with modulus H = kab | M; if p ≡ □ (mod M)
then the classical square-class obstruction (O253 Thm 3.2 = Mordell–Schinzel / ET Prop 1.6, with full T1 for
4 | k) gives a Type I/II solution of an odd square,
impossible. (a) is (i)+(ii) plus O253 Cor 3.3. (b) is (i) restated; the remark on thinness is an Assessment
(a random integer ≍ q has a prime factor ℓ with (p/ℓ) = −1 unless all its prime factors are p-residues, a set of
density 0 among integers ≤ X, by the sieve; not needed below). ∎

So the T1 adversary is *exactly* the statement that slice-level information about p is a finite set of residues,
and the only congruence-mediated escape is to let the level grow with the size of the source solution.

**Proposition 1.3 (polynomial lifts collapse to slice level; PROVED modulo the cited theorem).** Let 4 | k (for
k = 5 it is false: n = 5t + 4, denominators (t + 1, 2n(t + 1), 2n(t + 1)) give an identity on the square class 4 mod 5).
Suppose that on a
source slice σ′ and a class p ≡ r (mod M₀) a lift outputs a solution k/p = 1/X(t) + 1/Y(t) + 1/Z(t), p = M₀t + r,
with X, Y, Z ∈ ℤ[t] of positive leading coefficient, valid for all large t (the output depends on d′ only through
p, which on a fixed slice is affine in d′). Then r is not a square modulo M₀ (Schinzel, Funct. Approx. 28 (2000),
condition (1) for m ≡ 0 (mod 4); campaign citation audit O223, DISCOVERIES (J)49). So a polynomial lift is
"visible-only" exactly like a congruence lift of level M₀, and O253 Cor 3.3 applies to it with L = M₀.
*Proof.* A polynomial identity in t valid for infinitely many t is an identity in ℚ(t); Schinzel's theorem forbids
it on a square class. ∎
The same holds one level finer for polynomials in m = ⌊√p⌋ on p = m² ± j: by NEAR_SQUARE Thm 2.2 (j > 0) and
Thm 3.4 (j < 0; Hilbert reciprocity in ℚ(√j)) every such family misses the ℚ(√j)-adic unit-square set — an
*archimedean* lift has its own T1 adversary, now in ℚ(√j) (DISCOVERIES (J)55).

**Proposition 1.4 (exact-share lifts = e-spectrum transport; PROVED, algebra; repaired after R-O257 F2).** Let
α ≥ 1, β be integers. Call a witness-level lift *exact-share* if N_θ(p) = λ·N_θ′(q) identically in q
(p = αq + β, λ ∈ ℚ_{>0} independent of q). The complete list (for integral α, β; for rational α, β e.g. (I←II) becomes
e(αe′ − β) = 1, λ = αe — example q = 37, p = (q + 2)/3 = 13, e′ = e = 3, λ = 1, slice (1, 5, 2, 2) at both):
(II←II) λ = α, e = αe′ − β; (II←I) e′ | α, λ = α/e′, e = α/e′ − β; (I←II) e = 1, αe′ − β = 1, λ = α;
(I←I) e(α − βe′) = e′, λ = αe/e′. For an exact-share relation the target number λN′ = N_θ(p) and the target e are
fixed by (w′, relation) alone. A *reselecting* share lift — one allowed to output any slice (a, b, c) of type θ with
(a + b)/c = e and kab | λN′ — therefore succeeds at w′ iff (θ, e) ∈ Spec(p) := {(type, e) of witnesses of p}; a lift
prescribing one particular slice can fail even then (q = 23, w′ = (II, 1, 6, 7, 1), e′ = 1, p = 17, e = 7, λ = 1:
(1, 6, 1) works, (1, 13, 2) with e = 7 needs 52 | 24). A reselecting share law "q ∈ S_k ⟹ p ∈ S_k" is total iff
f(Spec(q)) ⊆ Spec(p) for the relevant shift map f — the source witness contributes *only its e-value*.
*Proof.* Compare coefficients of q in N_θ(αq + β) = λN_θ′(q): (II←II) αq + β + e = λ(q + e′); (II←I)
αq + β + e = λ(qe′ + 1); (I←II) (αq + β)e + 1 = λ(q + e′); (I←I) (αq + β)e + 1 = λ(qe′ + 1). ∎
*Reading.* The natural "joint factorisation" lifts lose all size information again: what survives is the
e-spectrum, a finite set of small integers per prime; Type II e-values at p = q + δ are shifted by −δ. With α = 1
only (II←II) e = e′ − δ, (I←II) e′ = δ + 1 and (II←I) e′ = 1, e = 1 − δ (δ < 0) exist.

## 2. The numerator-model laboratory

**2.1 Exact E_k (CERTIFIED, `scripts/z28_lab.c`, logs `logs/z28_Ek_primes_1e{5,7,8}.txt`).** Complete search over the
least denominator n/k < x ≤ 3n/k; for each x the two-term problem A/B = 1/y + 1/z (gcd(A, B) = 1) is solvable iff B²
has a divisor u ≤ B with u ≡ −B (mod A). Verified against the independent Python enumerator `z25_common.W`
(solution counts for k ∈ {4, 5, 8, 13}, n ∈ {97, 121, 241, 1001} agree exactly). Exceptional primes p ≤ 10⁸,
7 ≤ k ≤ 25 (runtime 30 s): identical to the ≤ 10⁷ lists, and (after removing p | k) identical in count and last
element to O194/O197's independent computation (MODEL_SPECIFIC §1; Pomerance–Weingartner Table 1 for k ≤ 15).
Last exceptions: k = 8: 241; 12: 12241; 16: 83449; 20: 2763601; 24: 620929 (and 9: 19, 13: 281, 17: 2081, 21: 14051,
25: 62731). So the model data are *known*; the laboratory's use below is new: it screens lift laws.

**2.2 Local profile of exceptions (EVIDENCE, `scripts/z28_profile.py`).** For 4 | k, every exception p > 3k beyond
the first few is ≡ 1 (mod k) or another square mod k, has p − 1 divisible by a high power of 2 and by 3, 5, and has a
large least quadratic non-residue: e.g. k = 20, p = 2763601 = 1 + 2⁴·3·5²·7²·47 has lqnr 19 and the only non-residue
primes ≤ 29 are {19, 29}; k = 16, 83449: non-residue primes ≤ 29 are {13, 23}; k = 12, 12049: {13, 19, 23, 29}.
*Reading:* model exceptions are exactly the primes the T1 adversary likes — squares modulo every small level —
i.e. "invisible to every slice-level lift built from small moduli".

**2.3 The margin (EVIDENCE; counts f_k(p) for all primes ≤ 5·10⁴, `z28_lab cnts`).** Mean f_k(p)/log³p on
[1.6·10⁴, 4.8·10⁴): k = 4: 0.159; 8: 0.072; 12: 0.043; 16: 0.030; 20: 0.025; 24: 0.019. Minimum f_k on the same range:
k = 4: **23**, k = 8: 4, k ≥ 12: 0 or 1. On Mordell-class primes (p mod 840 ∈ 𝓜) the mean drops by a factor ≈ 3
for k = 4 and ≈ 4 for k = 8, and the minimum is the same. So the k = 4 lottery sits a factor ≈ 2.2 above k = 8 in mean
and ≈ 6 in minimum at this height; exceptions in the models live where the expected count is O(1).
Consequence for screening: a k-uniform law *with a k-dependent threshold* ("every p > P₀(k) …") is not refuted by
model exceptions (Schinzel's conjecture itself is such a law). The screen refutes only threshold-free laws — the
form every lift law of O253 has.

**2.4 Complete levels: where visibility is sufficient (CERTIFIED computations, `scripts/z28_complete_levels.py`).**
For k | L, call L *complete* if every non-square unit class mod L contains a witness class with modulus H = kab | L
(i.e. lies in some class r ≡ −e (mod H) or re ≡ −1 (mod H), e | a + b). By full T1 no square class is ever
covered (asserted in the script at every L; 0 violations). Completeness of L is exactly "visibility at level L is
sufficient for a determined lift".
* k = 4, all L = 4m ≤ 1600 and all 7-smooth L ≤ 6000: the complete levels are 7-smooth (no level ≤ 1600 involving a
  prime ≥ 11 is complete), and a 7-smooth L (4 | L) is complete **iff (3 | L ⟹ 8 | L) and (7 | L ⟹ 24 | L)**
  (CERTIFIED for L ≤ 6000; the "if" direction is PROVED for all L: the 16 base levels 4·s, 8·s, s | 105 are
  checked, and completeness passes to any multiple L′ of L with the same prime support when 8 | L or
  v₂(L′) = v₂(L), because a non-square class mod L′ reduces to a non-square class mod L (squareness mod ℓ^v, ℓ odd,
  is squareness mod ℓ; mod 2^v, v ≥ 3, it is ≡ 1 (8)) and a covering class mod H | L lifts.) L = 840 is Mordell's theorem.
* k = 8 and k = 12: **no complete level L = km with m ≤ 400**; at L = 105k and 210k the deficiencies for
  k = 8, 12, 16, 20, 24 are 96/52, 178/213, 276/322, 346/460, 464/699 non-square classes.
* Adelic points (`scripts/z28_adelic_point.py`, slices a ≤ b ≤ 100–150): for k = 8 the points with x = 1 in ℤ₂,
  x = 1 at every prime ≥ 11, and arbitrary non-residues at any non-empty subset of {3, 5, 7} lie in **no** witness
  class with a, b ≤ 100; for k = 4 the point (x₂ = 1, x₃ = 2) is covered (slice (1, 6), e = 7) — Mordell — while
  (x₂ = 1, x₁₁ = 2) is not (Salez's S₁₁ = {7, 8, 10}). For k = 8 the prime 13 does help: (II, 1, 13, e = 7) covers
  x ≡ 6 (mod 13). EVIDENCE only (bounded slices).
* Single-prime points x_{ℓ,r} (x = 1 in ℤ₂ and at every prime ≠ ℓ, x = r a non-residue at ℓ), slices a ≤ b ≤ 300,
  exact O(1)-per-slice test (`scripts/z28_adelic_fast.py`, `z28_adelic_scan.py`, logs `logs/z28_adelic_scan_k{4,8}.txt`):
  k = 4: every x_{ℓ,r} with ℓ ∈ {3, 5, 7} is covered; for ℓ = 11 exactly r ∈ {2, 6} are uncovered (covered
  {7, 8, 10} = Salez's S₁₁), ℓ = 13: {2, 5, 7, 8} uncovered, …, ℓ = 37: 14 of 18 uncovered. k = 8: **every**
  non-residue at ℓ = 3, 5, 7 is uncovered, and at each ℓ ≤ 37 the uncovered set contains k = 4's. (B = 2500 for
  (k, ℓ, r) = (8, 3, 2), (8, 5, 2), (8, 7, 3), (4, 11, 2), (4, 11, 6): still uncovered.)
  Since a point lies in a class of modulus H | L iff its residue mod L does, **if x_{ℓ,r} is uncovered by all slices
  then no level divisible by ℓ is complete** — so (EVIDENCE) k = 4 has complete levels only on {2, 3, 5, 7}, and
  k = 8 has none at all, because already ℓ = 3, 5, 7 carry uncovered points.
*Reading (Assessment; scope per R-O257 M3).* In the range computed, "visibility is sufficient" holds for ES only at
Mordell-type 7-smooth levels, and that is a 4-specific fact (no complete level km, m ≤ 400, for k = 8, 12). For p ∈ 𝓜,
p is a square modulo every 7-smooth level, so at every complete level found (all ≤ 6000 among 7-smooth ones, all
≤ 1600 in general) p is invisible: in this range the 4-specific resource "complete levels" is used up precisely on the
Mordell classes. Every visible level of a Mordell-class prime involves a prime ℓ ≥ 11; Thm 2.6 (§5) proves that
levels through ℓ ≡ ±3 (mod 8), ℓ ≥ 11, are never complete; for levels through ℓ ≡ ±1 (mod 8) (17, 23, 31, …) only
the computations (≤ 1600) are available. Within these bounds: for p ∈ 𝓜, determined lifts need favourable
witnesses, not merely visible ones.

## 3. Goal (3): sources forced to share p's non-residue primes

**Lemma 3.1 (matched profile forces small-prime visibility; PROVED).** Let 4 | k, p, q odd primes ∤ k with q ≡ p
(mod 8) and (q/ℓ) = (p/ℓ) for every odd prime ℓ ≤ B. If w′ ∈ W_k(q) has a B-smooth modulus H′ (more generally:
if q is a non-square modulo the B-smooth part of H′), then w′ is visible to p (p ≢ □ mod H′).
*Proof.* By the square-class obstruction at q (Thm 1.2(ii) with p := q, M := H′; classical), q ≢ □ (mod H′); since
squareness mod H′ is local, q is a non-square modulo some prime power ℓ^v ∥ H′. If ℓ is odd, (q/ℓ) = −1; if ℓ = 2,
q ≢ 1 (mod 8) (v ≥ 3) or q ≡ 3 (mod 4) (v = 2). Under the hypothesis on that ℓ (ℓ ≤ B, resp. q ≡ p (8)) the same
holds for p. ∎
So a profile-matched source has no B-smooth invisible witness: the O253 adversary must use witnesses whose
modulus carries a prime ℓ > B with (q/ℓ) = −1 ≠ (p/ℓ). Visibility, however, is not sufficiency (§2.4).

**Computation 3.2 (CERTIFIED, `scripts/z28_matched.py`, logs `logs/z28_matched_{fixtures,mordell}.txt`).** Sources
q = p − δ, |δ| ≤ W, q prime, q ≡ p (8), matched Legendre profile at ℓ ∈ {3, 5, 7}; all ET representations of all
witnesses; "det" = p has a witness with H | H′ (O253 Thm 3.1), "share" = exact-share lift (Prop 1.4).
Entries q(δ): det / visible / all. (Rerun after review R-O257 M1/M2/minor: general squareness test incl. non-unit residues,
128-bit printing in the solver, profile test comparing zero symbols; two fixture entries changed by one.)
```
97   (W=600): 73(+24):5/6/7  313(-216):16/20/21  433(-336):13/17/22  577(-480):9/14/18
193  (W=600): 337(-144):10/18/22  457(-264):12/18/20  673(-480):8/13/18
313  (W=600): 73(+240):6/6/7  97(+216):3/6/8  433(-120):7/16/22  577(-264):8/15/18
3361 (W=600): 3049(+312):3/22/29  3529(-168):9/25/30  3889(-528):6/19/30
5209 (W=600): 4729(+480):0/20/33  5569(-360):4/19/30
```
All 273 Mordell-class primes p ≤ 10⁵ (W = 1000): 1347 matched sources, 106322 source witnesses, 68737 visible
(65%), 20365 transport by a determined lift (all of them visible — Thm 1.2 consistency asserted), exact-share 1606;
**0 sources are total**; visibility is sufficient (every visible witness transports) at 0 sources; the only
fixture source where it happens is 313 ← 73 (6/6 visible, one invisible witness remains, so not total either).
At 265 of 273 primes every matched source has at least one transporting witness — a statement about p's own
witness set (favourable-witness existence), not a law.
*Reading.* Matching the profile removes small-prime invisibility (Lemma 3.1) but the visible inputs still
transport only ≈ 30% of the time, exactly as §2.4 predicts: their levels contain primes ≥ 11 and are incomplete.
No total law appears; the residual question "does a favourable witness always exist" is ES(p) restated (B2).

## 4. Screening in the models, and do sizes carry information?

**4.1 Model screen (CERTIFIED, `logs/z28_matched_models.txt`).** At the model exceptions (k = 8: 131, 241;
k = 12: 1129 … 12241; k = 16: 3361, 4801, 8641, 33601, 83449) the profile-matched soluble sources (same window/profile
rules as §3) have many *visible* witnesses — e.g. 8/131 ← 251: 10 of 10 visible; 16/33601: 63 of 109 visible over 7
sources; 12/12241: 28 of 44 — and of course none transports (p has no witness). Hence each of the following
threshold-free laws is false in a model sharing T1 and the T1 adversary with ES, so a proof of its k = 4 form must
use a 4-specific input (or a threshold, §2.3):
(S1) "q ∈ S, q profile-matched to p (ℓ ≤ 7), q ≡ p (8), |p − q| ≤ 600 ⟹ p ∈ S";
(S2) "some visible source witness exists ⟹ some witness transports" (Lemma 3.1 makes visibility automatic for
B-smooth moduli, so (S2) is the visibility-sufficiency question of §2.4);
(S3) the reselecting exact-share laws of Prop 1.4 with α = 1, |β| ≤ 600 and profile-matched sources, as computed.
(R-O257 M5: these counterexamples refute only laws whose antecedent holds at the listed exceptions; a scheme with extra
hypotheses, or one never targeting these primes, is not refuted.)
The only 4-specific resource the laboratory exhibits is *Mordell completeness* (§2.4), and it is exhausted on 𝓜.

**4.2 Size information (EVIDENCE, `scripts/z28_size_info.py`).** The most naive witness-level lift reads a size number
D of a source witness (D ∈ {d′, c′d′, x′-part a′b′d′}) and asks for a witness of p whose p-free denominator abd is
a multiple of D. Over the 83 Mordell-class primes 100 < p ≤ 3·10⁴ (k = 4, sources within ±400, q ≡ p (8)), hit rates
are the same for profile-matched sources and for unmatched sources in the same window (same sizes):
d′: 64.6% vs 69.6%; c′d′: 51.6% vs 50.4%; a′b′d′: 4.4% vs 3.9% (6–7·10³ matched trials, 3–4·10⁴ unmatched;
trials cluster by p; no null distribution or clustered error was computed, so these are descriptive rates only). A shuffled control with sources of a
*different* target gives 67.7%, 54.0% for d′, c′d′ and 11.7% for a′b′d′ (the last difference is *plausibly* a size
confound — partners have different size — not tested). Assessment (descriptive, not a statistical test): **no
visible signal** that the sizes of a profile-matched source solution know more about p's divisor events than
unmatched sources of the same window — consistent with the B2 lottery; independence is not established.

## 5. A proved separation: the point x_{ℓ,2} (complements §2.4)

For an odd prime ℓ let x_{ℓ,2} ∈ Ẑ be the point with x = 2 in ℤ_ℓ and x = 1 in ℤ_q for every prime q ≠ ℓ (q = 2
included). It lies in the witness class (θ, a, b, c) iff its residue mod H = kab does, i.e. iff
H | x + e (II) resp. H | xe + 1 (I) for the integer x ≡ x_{ℓ,2} (mod H), e = (a + b)/c.

**Theorem 2.6 (PROVED, elementary).** Let 4 | k and ℓ ∤ k an odd prime.
(a) If k ≥ 8, x_{ℓ,2} lies in no Type I/II witness class.
(b) If k = 4, x_{ℓ,2} lies in a witness class iff ℓ ∈ {3, 5}; the classes are (II/I, a = 1, b = 6, e = 7) for ℓ = 3 and
(II, 1, 5, c = 2, e = 3), (I, 2, 5, c = 1, e = 7) for ℓ = 5 (Mordell's identities).
(c) Hence, if 2 is a non-residue mod ℓ (ℓ ≡ ±3 mod 8), **no level L with ℓ | L is complete** — for every 4 | k ≥ 8
(including ℓ = 3, 5), and for k = 4 for every such ℓ ≥ 11 (11, 13, 19, 29, 37, 43, …). For k = 8 a complete level
would have to be supported on 2 and primes ≡ ±1 (mod 8).
*Proof.* Write m = v_ℓ(ab). Every prime q | kab other than ℓ sees x ≡ 1 (mod q^{v_q(kab)}).
*Case 0 (m = 0).* Type II: e ≡ −1, Type I: e ≡ −1 (mod kab); so e ≥ kab − 1 > a + b ≥ e (k ≥ 4), impossible.
*Case A (ℓ ∤ a, b = ℓ^m b₀, m ≥ 1; the case ℓ ∤ b is symmetric).* Put L = ℓ^m; ℓ ∤ e (II: e ≡ −2, I: 2e ≡ −1 mod ℓ).
Type II: e ≡ −1 (mod kab₀), e ≡ −2 (mod L), ce = a + Lb₀. Mod L, a ≡ ce ≡ −2c, so a + 2c = Lg (g ≥ 1) and ℓ ∤ c. Then
c(e + 2) = L(g + b₀), so c | g + b₀; with h := (g + b₀)/c, e = Lh − 2 and Lh ≡ 1 (mod kab₀). As Lh ≥ 3,
Lh ≥ kab₀ + 1, and Lh = 2L(g + b₀)/(Lg − a) (c = (Lg − a)/2). If a ≤ Lg/2: Lh ≤ 4(g + b₀)/g ≤ 4 + 4b₀/g, so
kb₀ + 1 ≤ 4 + 4b₀/g, i.e. b₀(k − 4/g) ≤ 3 — impossible for k ≥ 8. If a > Lg/2: Lg − a = 2c ≥ 2 gives Lh ≤ L(g + b₀),
and kab₀ + 1 > (k/2)Lgb₀, so g + b₀ > (k/2)gb₀ ≥ 2gb₀ — impossible for k ≥ 4.
Type I: e ≡ −1 (mod kab₀) gives 2e + 1 ≡ −1 (mod 2kab₀); 2e ≡ −1 (mod L) and ce = a + Lb₀ give 2a + c = Lg, ℓ ∤ c,
c(2e + 1) = L(g + 2b₀), h := (g + 2b₀)/c, 2e + 1 = Lh ≡ −1 (mod 2kab₀), so Lh ≥ 2kab₀ − 1, with Lh = L(g + 2b₀)/(Lg − 2a).
If 2a ≤ Lg/2: Lh ≤ 2 + 4b₀/g, so 2kb₀ − 1 ≤ 2 + 4b₀ — impossible for k ≥ 4. If 2a > Lg/2: Lh ≤ L(g + 2b₀) and
2kab₀ − 1 > (k/2)Lgb₀ − 1, so g + 2b₀ ≥ (k/2)gb₀ — impossible for k ≥ 8 (4gb₀ > g + 2b₀).
*Case B (a = ℓ^i a₀, b = ℓ^j b₀, 1 ≤ i ≤ j, n := j − i).* ℓ ∤ e and ce = ℓ^i(a₀ + ℓ^n b₀) force c = ℓ^i c₀,
c₀e = a₀ + ℓ^n b₀, and e ≡ −1 (mod ka₀b₀). If n = 0, e ≥ ka₀b₀ − 1 > a₀ + b₀, impossible. If n ≥ 1, the Case A
computation with (a, b₀, L, c) → (a₀, b₀, ℓ^n, c₀) applies verbatim (it used only the congruences mod ka₀b₀ and mod
ℓ^n, which are implied), and in addition the congruence mod ℓ^{i+j} = ℓ^{2i+n} forces ℓ^{2i} | h.
This proves (a). (b) For k = 4 the only surviving branches are Type II, Case A, a ≤ Lg/2, and Type I, Case A,
2a > Lg/2 (all other branches above are impossible already for k ≥ 4).
*Type II.* 4ab₀ + 1 ≤ Lh ≤ 4 + 4b₀/g forces a = 1 (a ≥ 2 gives 8b₀ + 1 ≤ 4 + 4b₀). If g = 1: c = (L − 1)/2,
b₀ = hc − 1, and 4b₀ = 4(hc − 1) must divide Lh − 1 = 2(hc − 1) + h + 1 > 0, so h + 1 ≥ 2(hc − 1), i.e.
h(2c − 1) ≤ 3: c = 1 (L = 3), h ∈ {2, 3}, where h = 2 fails (4 ∤ 5) and h = 3 gives b₀ = 2, slice (1, 6), e = 7;
or c = 2 (L = 5), h = 1, b₀ = 1, slice (1, 5, c = 2), e = 3. If g ≥ 2: b₀(4 − 4/g) ≤ 3 forces b₀ = 1, and
c = (Lg − 1)/2 ≤ g + 1 (h ≥ 1) gives g(L − 2) ≤ 3, so L = 3 and g = 3 (Lg odd): c = 4, h = 1, Lh = 3 ≢ 1 (mod 4).
*Type I.* Here g + 2b₀ ≥ 2gb₀ leaves g = 1, or g = 2 with b₀ = 1. If g = 1: since 8ab₀ > 2Lb₀,
L(1 + 2b₀)/c = Lh ≥ 8ab₀ − 1 > 2Lb₀ − 1 forces c = 1 (c ≥ 2 would give b₀ < 1), so a = (L − 1)/2, h = 1 + 2b₀ and
L(1 + 2b₀) + 1 = 4(L − 1)b₀t (t ≥ 1), i.e. L + 1 = b₀(4Lt − 4t − 2L). For t = 1: b₀ = (L + 1)/(2L − 4): L = 3,
b₀ = 2 (slice (1, 6), e = (Lh − 1)/2 = 7) or L = 5, b₀ = 1 (slice (2, 5), c = 1, e = 7); L ≥ 7 gives b₀ < 1. For t ≥ 2,
b₀(6L − 8) ≤ L + 1 is impossible. If g = 2, b₀ = 1: c = 2L − 2a is even and divides g + 2b₀ = 4, so c ∈ {2, 4},
a = L − c/2, h = 4/c, and 8a | Lh + 1 gives 8L − 4c ≤ Lh + 1, i.e. 8L − 8 ≤ 2L + 1 (c = 2) or 8L − 16 ≤ L + 1 (c = 4) — impossible for L ≥ 3.
*Case B for k = 4* reduces to these with ℓ^n ∈ {3, 5} and h ∈ {3, 1} (II) or {5, 3} (I), and the extra condition
ℓ^{2i} | h (i ≥ 1) fails in all four. So exactly ℓ ∈ {3, 5} (m = 1) survive, with the listed classes, which do
contain x_{ℓ,2} (representative x = 17 in both cases: 17 ≡ 1 (8), 17 ≡ 2 (3), 17 ≡ 2 (5); 17 + 7 = 24,
17·7 + 1 = 120 = 5·24, 17 + 3 = 20, 120 = 3·40).
(c) If 2 is a non-residue mod ℓ and ℓ | L, the class of x_{ℓ,2} mod L is a non-square unit class; a covering class
of modulus H | L would contain x_{ℓ,2} itself. ∎
*Numerical check (CERTIFIED, `scripts/z28_x2_check.py`, a ≤ b ≤ 300, k ∈ {4, 8, …, 32}, ℓ < 60, ℓ ∤ k):* hits
occur exactly for k = 4, ℓ ∈ {3, 5}, and they are exactly the four classes of (b).
*Independent check on actual primes (complete solution lists):* the first four primes n ≡ x_{3,2} (mod 60480 = 2⁶·3³·5·7)
(421121, 542081, 1146881, 1570241) have, among all their ET witnesses, those with H | 60480 = exactly the Mordell pair
(II/I, 1, 6, e = 7) for k = 4 and **none** for k = 8, 16 (k = 12 has (1, 6) at H = 72, consistent: 3 | 12 is excluded).

*Reading.* A proved point-classification separating 4 from every 4 | k ≥ 8 (ℓ ∤ k): for k = 4 the small
non-residue primes 3, 5 are "complete-capable" (Mordell), for every 4 | k ≥ 8 no prime ℓ ≡ ±3 (8) ever is. The
reason is an inequality (the slice must satisfy b₀(k − 4/g) ≤ 3), i.e. the archimedean size of 4 — numerator
smallness, not a reciprocity law. For ES it proves part of the §2.4 Assessment: for a Mordell-class p, every level
containing some prime ℓ ≡ ±3 (mod 8), ℓ ≥ 11, is incomplete (levels supported on 2, 3, 5, 7 and primes ≡ ±1 (8) are
not covered by Thm 2.6).
