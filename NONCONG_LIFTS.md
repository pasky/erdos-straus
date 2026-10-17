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
through p mod M, where M = M(w′) is an even integer computed from w′, and its proof establishes validity for
*every* prime p′ ≡ p (mod M) (with the same w′). The level is *slice-level* if M depends only on σ(w′) (then
M ≤ C(σ(w′)) is bounded on each slice — the determined lifts of O253 Thm 3.1 have M = αH′), and *witness-level*
if it genuinely depends on the size parameter d′ (equivalently on q, since q = (N′ − e′) or (N′ − 1)/e′ with
N′ = kH′-multiple k a′b′d′).

**Theorem 1.2 (level dichotomy; PROVED).** Let 4 | k, p an odd prime, M even, and suppose a slice (θ, a, b, c) is
valid at every prime p′ ≡ p (mod M). Then (i) k a b | M, and (ii) p is *not* congruent to a square modulo M.
Consequently: (a) a slice-level lift must, at every supplied source witness, see a non-square residue of p modulo
M(σ(w′)), and O253 Cor 3.3 applies verbatim (lcm of invisible slice-levels is invisible); (b) a witness-level lift
of level M(w′) is valid iff N_θ(p) has the divisor kab | M(w′) with (a + b)/c = e — a divisor event whose modulus is
built from the size d′ of the source solution (B2), and Theorem 1.2(ii) is then no restriction in practice
(M(w′) ≍ q has prime factors ℓ with (p/ℓ) = −1 for all but a thin set of q).
*Proof.* (i) For each prime ℓ | kab, ℓ ≠ p, pick t_ℓ (mod ℓ) with t_ℓ ≢ 0 and p + t_ℓM ≢ 0 (mod ℓ): for ℓ = 2 any odd
t works (M even, p odd); for odd ℓ | M any t ≢ 0 works (p + tM ≡ p ≢ 0); for odd ℓ ∤ M exactly one class t is bad,
leaving ≥ ℓ − 2 ≥ 1 non-zero good classes. (ℓ = p does not divide kab: p ∤ ab by ET normalisation at a prime, and
p ∤ k.) By CRT and Dirichlet there is a prime p′ = p + tM with gcd(t, kab) = 1. Validity at p and p′:
Type II: kab | (p′ + e) − (p + e) = tM, so kab | M. Type I: kab | (p′e + 1) − (pe + 1) = tMe and gcd(e, kab) = 1
(from kab·d = pe + 1), so kab | M. (ii) Then the slice is an ET witness at p with modulus H = kab | M; if p ≡ □ (mod M)
then the classical square-class obstruction (O253 Thm 3.2 = Mordell–Schinzel / ET Prop 1.6, with full T1 for
4 | k) gives a Type I/II solution of an odd square,
impossible. (a) is (i)+(ii) plus O253 Cor 3.3. (b) is (i) restated; the remark on thinness is an Assessment
(a random integer ≍ q has a prime factor ℓ with (p/ℓ) = −1 unless all its prime factors are p-residues, a set of
density 0 among integers ≤ X, by the sieve; not needed below). ∎

So the T1 adversary is *exactly* the statement that slice-level information about p is a finite set of residues,
and the only congruence-mediated escape is to let the level grow with the size of the source solution.

**Proposition 1.3 (polynomial lifts collapse to slice level; PROVED modulo the cited theorem).** Suppose that on a
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

**Proposition 1.4 (exact-share lifts = e-spectrum transport; PROVED, algebra).** Call a witness-level lift
*exact-share* if N_θ(p) = λ·N_θ′(q) identically in q (p = αq + β, λ ∈ ℚ_{>0} independent of q). The complete list:
(II←II) λ = α, e = αe′ − β; (II←I) e′ | α, λ = α/e′, e = α/e′ − β; (I←II) e = 1, αe′ − β = 1, λ = α;
(I←I) e(α − βe′) = e′, λ = αe/e′. For an exact-share relation, *every* slice (a, b, c) of type θ with
(a + b)/c = e is automatically compatible (kab | N_θ(p) = λN′ is the witness condition itself), so the lift is valid
at w′ iff (θ, e) ∈ Spec(p) := {(type, e) of witnesses of p}. A share law "q ∈ S_k ⟹ p ∈ S_k" is total iff
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
  checked, and completeness passes to any L′ with the same prime support and v₂(L′) ≥ v₂(L) when 8 | L or
  v₂(L′) = v₂(L), because a non-square class mod L′ reduces to a non-square class mod L (squareness mod ℓ^v, ℓ odd,
  is squareness mod ℓ; mod 2^v, v ≥ 3, it is ≡ 1 (8)) and a covering class mod H | L lifts.) L = 840 is Mordell's theorem.
* k = 8 and k = 12: **no complete level L = km with m ≤ 400**; at L = 105k and 210k the deficiencies for
  k = 8, 12, 16, 20, 24 are 96/52, 178/213, 276/322, 346/460, 464/699 non-square classes.
* Adelic points (`scripts/z28_adelic_point.py`, slices a ≤ b ≤ 100–150): for k = 8 the points with x = 1 in ℤ₂,
  x = 1 at every prime ≥ 11, and arbitrary non-residues at any non-empty subset of {3, 5, 7} lie in **no** witness
  class with a, b ≤ 100; for k = 4 the point (x₂ = 1, x₃ = 2) is covered (slice (1, 6), e = 7) — Mordell — while
  (x₂ = 1, x₁₁ = 2) is not (Salez's S₁₁ = {7, 8, 10}). For k = 8 the prime 13 does help: (II, 1, 13, e = 7) covers
  x ≡ 6 (mod 13). EVIDENCE only (bounded slices).
*Reading (Assessment).* "Visibility is sufficient" holds for ES exactly at Mordell's levels, and there it is a
4-specific fact (no complete level at all for k = 8, 12). But for p ∈ 𝓜, p is a square modulo every 7-smooth level,
so **at every complete level p is invisible**: the 4-specific resource "complete levels" is used up precisely on
the Mordell classes. Every visible level of a Mordell-class prime involves a prime ℓ ≥ 11, and no such level ≤ 1600
is complete. This is O253's T1 adversary in its sharpest form: for p ∈ 𝓜, determined lifts need favourable
witnesses, never merely visible ones.

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
Entries q(δ): det / visible / all.
```
97   (W=600): 73(+24):5/6/7  313(-216):16/20/21  433(-336):13/17/22  577(-480):9/15/18
193  (W=600): 337(-144):10/18/22  457(-264):12/18/20  673(-480):8/14/18
313  (W=600): 73(+240):6/6/7  97(+216):3/6/8  433(-120):7/16/22  577(-264):8/15/18
3361 (W=600): 3049(+312):3/22/29  3529(-168):9/25/30  3889(-528):6/19/30
5209 (W=600): 4729(+480):0/20/33  5569(-360):4/19/30
```
All 273 Mordell-class primes p ≤ 10⁵ (W = 1000): 1347 matched sources, 106322 source witnesses, 68739 visible
(65%), 20365 transport by a determined lift (all of them visible — Thm 1.2 consistency asserted), exact-share 1606;
**0 sources are total**; visibility is sufficient (every visible witness transports) at 0 sources; the only
fixture source where it happens is 313 ← 73 (6/6 visible, one invisible witness remains, so not total either).
At 265 of 273 primes every matched source has at least one transporting witness — a statement about p's own
witness set (favourable-witness existence), not a law.
*Reading.* Matching the profile removes small-prime invisibility (Lemma 3.1) but the visible inputs still
transport only ≈ 30% of the time, exactly as §2.4 predicts: their levels contain primes ≥ 11 and are incomplete.
No total law appears; the residual question "does a favourable witness always exist" is ES(p) restated (B2).
