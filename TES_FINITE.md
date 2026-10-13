# TES_FINITE — TES(π) is a finite search; certified non-T1 failures of a T1-bearing ES analogue (task O194, spark relay O)

Status: in progress (O194). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on TWISTED_T1.md (O182/R182; TES, Thm 3.2 = order-3 T1), SYNTHESIS_SPARKS2.md §3 (O192; shot identity,
TES^{□₃}), FIXED_MODULUS_SHOTS.md §6 (ES finiteness via positivity). Scripts `scripts/tf_*`.

Notation (TWISTED_T1 §3). O = ℤ[ω], ω = ζ₃, |·| the complex absolute value, N = |·|². TES(n):
`9/n = ω/x + ω²/y + 2/z,  x, y, z ∈ O,  x ≡ y ≡ z ≡ 1 (mod 2O)`, n ∈ O, gcd(n, 6) = 1, n ≡ 1 (mod 2).
c = (c₁, c₂, c₃) = (ω, ω², 2), (x₁, x₂, x₃) = (x, y, z), u_i = x_i/c_i.

## 0. Iteration log
(I1) Brief's premise: "ES is finite at fixed p because of positivity; TES has a complex place, so its solution set
may be infinite". **Killed (Prop 1.1): positivity is not what makes ES(p) finite.** Any equation "constant ≠ 0 =
sum of three reciprocals of integers" over a ring with a single archimedean place is finite, because (i) the
triangle inequality at that one place bounds the smallest denominator, and (ii) a two-term reciprocal equation with
a non-zero right side is a divisor problem. The only escape is a vanishing two-term subsum, which TES excludes
because c_i n/9 ∉ O. There are no Vieta-type moves: the cleared equation is multilinear (degree 1 in each variable).
What positivity gives ES is a *polynomial* bound O(p²) on the certifying moduli; TES gets an equally explicit one.
Consequence: goal (2) of the brief (certified exhaustive search) is available, goal (3) is void.

## 1. Finiteness with an explicit bound

**Proposition 1.1 (finiteness at fixed n; PROVED, elementary).** Let O be ℤ or the ring of integers of an imaginary
quadratic field, t, c₁, c₂, c₃ ∈ O ∖ 0, n ∈ O ∖ 0, and assume c_i n/t ∉ O for i = 1, 2, 3. Then the equation
`t/n = c₁/x₁ + c₂/x₂ + c₃/x₃,  x_i ∈ O ∖ 0`
has finitely many solutions. More precisely every solution satisfies:
(a) for some i: |x_i| ≤ 3|c_i||n|/|t|;
(b) for this i, with r := t/n − c_i/x_i (≠ 0) and {j, k} the other indices, (A x_j − B c_j)(A x_k − B c_k) =
B² c_j c_k where A = t x_i − c_i n ≠ 0, B = n x_i; and min(|x_j|/|c_j|, |x_k|/|c_k|) ≤ 2/|r| = 2|n x_i|/|A|.
*Proof.* (a) |t/n| ≤ Σ |c_i|/|x_i| ≤ 3 max_i |c_i|/|x_i|. (b) r = 0 would give x_i = c_i n/t ∈ O, excluded; so
c_j/x_j + c_k/x_k = r = A/B with A, B ∈ O ∖ 0; clearing denominators, A x_j x_k − B c_k x_j − B c_j x_k = 0, i.e.
(A x_j − B c_j)(A x_k − B c_k) = B² c_j c_k. The left factors are divisors of the fixed non-zero B² c_j c_k, finitely
many up to units, and O^* is finite; each factorisation determines (x_j, x_k). The min-bound is (a)'s argument for
two terms: |r| ≤ 2 max(|c_j|/|x_j|, |c_k|/|x_k|). Finitely many x_i in the disk (a) (O is a lattice). ∎
*Attribution (R194 repair, D1).* Over ℤ this is Bright–Loughran Lemma 3.10 (same argument: min |u_i| ≤ 3n/4, then the
two-term problem; the vanishing-subsum family u_i = −u_j is BL's excluded set). New here: imaginary quadratic O and
coefficients c_i.
*Remarks.* (1) Positivity is not used. For ES over ℤ with signs allowed (4/n = Σ 1/x_i, x_i ∈ ℤ ∖ 0, n odd > 1)
the same proof gives finiteness. (2) The proof needs exactly one archimedean place with O discrete in it: over a
real quadratic O the disk (a) contains infinitely many integers (units), and the argument fails. (3) If some
c_i n/t ∈ O the set is infinite (x_i = c_i n/t, x_k = −(c_k/c_j) x_j, x_j ∈ c_j·O): the only infinite families of
this multilinear equation are vanishing subsums.

**Corollary 1.2 (TES(π) is a finite search; PROVED).** Let n ∈ O, gcd(n, 6) = 1. Every solution of TES(n) (normalised
or not) has
`N(x) ≤ N(n)/9, or N(y) ≤ N(n)/9, or N(z) ≤ 4N(n)/9,`
and given that coordinate x_i, the other two are read off from a factorisation of B²c_jc_k = (n x_i)² c_jc_k with
A = 9x_i − c_i n. The number of solutions is at most Σ_i Σ_{x_i} 6·τ_O((n x_i)² c_j c_k) (τ_O = number of ideal
divisors), a finite, explicit bound. *Proof.* Prop 1.1 with t = 9, |c| = (1, 1, 2); c_i n/9 ∉ O since 3 ∤ n. ∎
In particular for N(π) = 103 the first coordinate ranges over the lattice points with N ≤ 11.4 (x, y) or N ≤ 45.8
(z; 162 points, 42 of them 2-primary): TES(π) is decided by a few hundred factorisations.
*Contrast with SYNTHESIS_SPARKS2 Prop 3.1/Thm 3.5:* the shot family with D = Q³ has z = Z/Q³ ∉ O; it lives in
TES^{□₃}, whose solution set at fixed n is infinite (the mute places q | Q supply the escape that (a) forbids for
integral denominators). So TES and TES^{□₃} differ exactly as ES and ES^{(S)} do (FIXED_MODULUS_SHOTS Thm 6.2(iii)).

## 2. Certified exhaustive search: TES fails at 16 primes (N ≤ 30000) outside its T1 set

Implementation. `scripts/tf_core.py` (ℤ[ω] arithmetic and factorisation written from scratch, not importing
`tw_eis.py`), `scripts/tf_exact.py` (**method A**: Cor 1.2 disk for x_i + complete divisor enumeration of
B²c_jc_k, all six associates), `scripts/tf_brute.py` (**method B**, independent code path, numpy, *no factorisation*:
Prop 1.1(a) disk for x_i, then Prop 1.1(b)'s disk N(x_j) ≤ 4N(c_j)N(B)/N(A) for the smaller of the two remaining
weighted denominators — both choices of j — and x_k = c_kBx_j/(Ax_j − Bc_j) tested for integrality; R-O194 repair: a-priori bounds on every int64
intermediate are asserted in Python integers *before* the vectorised arithmetic, so wrap-around cannot silently
drop a solution; all runs reported here pass these assertions). Every reported solution is verified exactly in O (9x₁x₂x₃ = n(Σ c_i ∏_{k≠i} x_k)), all
three coordinates 2-primary. `scripts/tf_compare.py 6000` (4 min): for all 394 primes π of O with N(π) ≤ 6000
(one 2-primary π per conjugate pair of split primes — TES(π) ⟺ TES(−π) ⟺ TES(π̄) by x_i ↦ −x_i, resp. complex
conjugation with x ↔ y — and the inert p ≤ 71) **methods A and B return identical solution sets** (4160 solutions
in total). Cross-check with O182: for N(π) ∈ {307, 439, 601, 1009, 1213, 2011} the O182 window solutions
(`tw_eis_solve.run`, B = 60) are a subset of — in fact equal to — the complete sets.

**Theorem 2.1 (non-T1 failures of TES; CERTIFIED = PROVED Cor 1.2 + two independent exhaustive computations).**
TES(π) has **no solution** for the 2-primary primes π with
`N(π) ∈ {7, 13, 19, 61, 79, 97, 103, 151, 193, 211, 367, 409, 769, 2029, 2239, 26893}`
(both conjugates, both signs), and for every other prime π of O with N(π) ≤ 30000, π ∤ 6 (split, or inert
p ≤ 173), TES(π) has a solution. Every solution at a prime has Type I or Type II shape — PROVED (R194 repair, D7):
π | 9xyz forces π to divide a coordinate, and π dividing all three would give 9 = ω/x′ + ω²/y′ + 2/z′ with
|9| > 1 + 1 + 2 (N ≤ 30000: 21042 Type I, 7038 Type II; only the proportions are EVIDENCE). [Method B was run on all 16 failures — 0 solutions each, e.g. 13 s for
N = 26893 — and agrees with method A on every prime N ≤ 6000 and on the 4 split primes just below 26893;
`tf_exact.py census 30000`, 63 min, one core, gives the full list.]
Representatives: N = 103: π = 11 + 2ω; N = 151: −9 − 14ω; N = 7: −1 + 2ω; N = 26893: 179 + 36ω.
Since these n = π are primes, hence not cubes, and satisfy the necessary local condition n ≡ 1 (mod 2) of TWISTED_T1
Lemma 3.1, **the TES-analogue of "T1 is the only obstruction" (the analogue of CONJECTURE SQ) is false**: T1₃
obstructs *Type I/II-shaped* solutions at cubes (and cubes are still solvable in other shapes, §4), while at these
primes — where every solution would have Type I/II shape — there is no solution at all, with no T1 reason (R-O194
repair: formerly "solvability set ≠ everything except cubes", which conflated shapes and solvability). This is the
first T1-bearing ES-type equation in the campaign with a *proved* failure outside its T1 locus.

Count statistics (method A census, one π per pair): mean number of solutions 5.96 for N ≤ 1000 (13 zeros among 85
primes), 9.57 on (1000, 3000] (2 zeros / 130), 13.46 on (3000, 6000] (0 / 179). The failures thin out exactly as a
small-mean count would (lottery picture; analysed in §3–4).

## 3. The failures are not Brauer–Manin (with respect to the full Brauer group of the surface)

**Brauer group (PROVED, citing Bright–Loughran 1908.02526 §2, which works over any field k of characteristic 0).**
Over K the TES surface U: 9xyz = n(ωyz + ω²xz + 2xy) ⊂ 𝔸³ becomes BL's U_{n'} (4u₁u₂u₃ = n'(u₁u₂ + u₁u₃ + u₂u₃))
under the K-linear change of variables x_i = c_i·(9/4)·u_i', n' = 16n/81. By BL Prop 2.6 (the classes α_ζ,
ζ ∈ μ(k), represent Br Ũ/Br k) and Cor 2.9 (Br U → Br Ũ is an isomorphism for these affine surfaces:
surjective by Thm 1.7, injective via Pic Ũ → Pic E surjective; R-O194 repair: normality alone does not give
injectivity, cf. BL Remark 2.10), **Br U / Br K ≅ μ(K)^∨ ≅ ℤ/6, generated by α_ω (order 3; TWISTED_T1's α) and α_{−1} (order 2)**, both
transcendental. Constant classes pair trivially with adelic points (reciprocity), so an adelic point is orthogonal
to Br U iff Σ_v inv_v α_ω = 0 and Σ_v inv_v α_{−1} = 0.

Integral model and local conditions. 𝒰: the same equation over O; the TES solution set is 𝒰(O) ∩ U°(K) with the
open condition "x, y, z ≡ 1 (mod 2)" at v = 2, where U° = U ∖ {xyz = 0} (= U minus BL's three lines L_ij). The BM
set is W^{Br U}, W := ∏_{v finite} {P ∈ 𝒰(O_v) ∩ U°(K_v), 2-primary if v = 2} × U(ℂ).

Method (`scripts/tf_bm.py`, own code). Global K-points P = (x, y, z) with x, y ∈ O 2-primary (N ≤ 150) and
z := 2/(9/n − ω/x − ω²/y) ∈ K. For such P let T(P) be the finite places where P ∉ W_v (z not v-integral, or
not ≡ 1 mod 2 at v = 2). Local invariants: tame places from the tame symbol raised to (N𝔭 − 1)/m; the one wild
place per class (λ for α_ω, (2) for α_{−1}) by reciprocity. Convention check: on all complete solution sets of
§2 at N(π) ∈ {307, 439, 1009} (106 solutions) the code reproduces TWISTED_T1's (inv₂, inv_π, inv_λ) = (1, 2, 0) for
α_ω and inv₂ α_{−1} = inv_π α_{−1}, inv_λ α_{−1} = 0, with both quadratic values occurring at N = 439 (27/27).
*Certificate shape.* A base point P₀ with T(P₀) = {𝔮} and, for 𝔮, a second global point P₁ with 𝔮 ∉ T(P₁) and
(inv_𝔮 α_ω, inv_𝔮 α_{−1})(P₁) = (inv_𝔮 α_ω, inv_𝔮 α_{−1})(P₀). Then the adelic point Q_v := P₀ (v ≠ 𝔮), Q_𝔮 := P₁
lies in W, and for β ∈ {α_ω, α_{−1}}: Σ_v inv_v β(Q) = Σ_v inv_v β(P₀) + [inv_𝔮 β(P₁) − inv_𝔮 β(P₀)] = 0 + 0.

**Theorem 3.1 (no Brauer–Manin obstruction at the failures; PROVED for each listed π by an explicit certificate,
modulo the BL citation).** For each of the 16 primes π of Thm 2.1, W^{Br U} ≠ ∅. In particular TES(π) is
everywhere locally solvable (with the 2-primary normalisation), the order-3 T1 class α_ω and the quaternion class
α_{−1} impose no condition that fails, and **the 16 failures of Thm 2.1 are failures of the integral Hasse principle
not explained by the Brauer–Manin obstruction from Br U** (R194 repair, D5: BL's group of the affine surface; Br U°
and étale-BM not considered, see Scope). Certificate for N(π) = 103, π = 11 + 2ω:
P₀ = (x, y) = (−7 − 14ω, 5 + 4ω), z = (630 − 672ω)/(326 − 428ω), T(P₀) = {𝔮 = (49 − 33ω)} (N𝔮 = 5107),
P₁ = (−7 − 14ω, −11 − 12ω, z = (−2282 + 896ω)/(−858 + 548ω)); both have invariants (0, 0) at 𝔮 (cross-checked with O182's independent `tw_eis.tame_symbol`/`tame_symbol2`; P₁'s only bad place has norm 7687).
N(π) = 151: P₀ = (−7 − 14ω, 1), T = {(132 + 13ω)}, P₁ = (−7 − 14ω, −7 − 12ω). All 16 certificates:
`uv run python scripts/tf_bm.py <a b ...>` (≈ 2.5 min for all; each found with |T(P₀)| = 1; N = 26893: T = {(527 − 121ω)}, invariants (0, 0)).
*Scope/caveats.* (i) Br U is BL's group of the affine surface *including* the lines L_ij; classes of Br U° ramified
along the lines are not considered (U°'s integral points are not the integral points of a model of U° — Type II
solutions have π dividing two coordinates — so the standard integral BM set for this problem is the one above, as
in BL Thm 1.1/1.8). (ii) Not excluded: obstructions beyond Brauer–Manin (finite descent / étale BM would need
covers of U; U is geometrically rational with π₁^{ét}(Ū) to be checked), or none at all ("small count").

## 4. T1 control at cubes (complete enumeration) and the count picture

**Cubes (CERTIFIED, method A; `scripts/tf_exact.py a b 3`).** Complete solution sets of TES(π³):
N(π) = 7: 14 solutions, 13: 18, 19: 19, 31: 31, 37: 22, 43: 39 — **all of "other" shape, none of Type I/II**
(Thm 3.2(b), now checked on complete sets rather than windows). Note TES(π³) is solvable for N(π) ∈ {7, 13, 19}
although TES(π) is not (the solutions are not inherited from π; TWISTED_T1's inheritance only goes π ⇒ π³).

**Counts (EVIDENCE).** Mean number of solutions of TES(π) (one π per pair): 5.96 (N ≤ 1000), 9.57 (1000–3000),
13.46 (3000–6000), 14.40 (3000–10000; min 1, 0 zeros among 408), 20.31 (10000–30000; **1 zero among 1007**:
N = 26893, after a gap from 2239). The failures are concentrated at small N and thin out as the mean grows, but
the lower tail is heavy (cf. ES's Mordell-hard classes): a mean of ≈ 20 does not prevent an isolated zero.
Cubic characters (χ_π(ω), χ_π(2), χ_π(λ)) at the 16 failures (R-O194 repair: TWISTED_T1 §5's window observation
"failures only where χ_π(ω), χ_π(2) ≠ 0" does NOT survive): N = 19: (0, 1, 2); N = 13: (1, 2, 0); **N = 26893:
(0, 0, 0)** — ω, 2 and λ are all cubes mod π, the analogue of ES's Mordell-hard class (all small data residues);
the other 13 have both of the first two non-zero. Whether some congruence-class bias explains the failures was not
tested beyond this.
**Assessment.** The failures behave like the zero-count tail of a slowly growing count ("lottery" failures), the
regime ES itself would be in were its counts smaller: no local, Brauer–Manin or T1 reason exists (§3). Whether
TES(π) fails for only finitely many π is the TES-analogue of ES: open (the zero at 26893 shows the last failure, if
any, is not small).

## 5. The same phenomenon over ℚ with positivity: Schinzel's 8/n (order-2 T1 at odd squares, real anchor)

(I2) TES differs from ES in three ways (order 3, complex place, tame anchor). To see whether the failures are an
artefact of these, iterate on the hypothesis "T1-bearing" inside BL's own family: Schinzel's m/n = 1/x + 1/y + 1/z,
x, y, z ∈ ℕ. BL Remark 1.10: these surfaces are ℚ-isomorphic to U_n (so Br U/Br ℚ = ℤ/2 = ⟨α⟩, α = (−u₁/u₃,
−u₂/u₃), BL Thm 1.6) and every natural-number solution satisfies ∏_{p | 2nm} (α)_p = −1.

**Proposition 5.1 (order-2 T1 for 8/n; PROVED, using BL's p-local lemmas verbatim).** Let n be odd. Every solution of
8/n = Σ 1/u_i in ℕ satisfies ∏_{p | n} inv_p α(u) = −1; hence for n = k² (k odd) no solution has Type I or Type II
shape (in BL Lemma 3.9's sense, exponent v_p(n)) at every prime p of n; for n = q^{2j} a prime power: no Type I/II solution. For Type II the conclusion is elementary and in-campaign: POINTWISE_MN Lemma
1.1(d) (m ≡ 0 mod 4 ⇒ the Type II event class −mD is a Jacobi non-residue mod M, so n ≡ −mD (mod M) is not a
square).
*Proof.* Hilbert reciprocity for α(u). ∞: −1 (u_i > 0; BL Lemma 3.1). p = 2: all u_i ∈ ℤ₂; with x := (8/n)u₁ − 1
DRINFELD_ES Lemma 2.1 gives α = (y, −1) + (x, y), and −x ∈ 1 + 8ℤ₂ ⊂ ℚ₂^{*2}, so (x, y) = (−1, y) and
α = 2(−1, y) = 0 — **this is where v₂(8) = 3 is used** (for m = 4 BL need the finer Lemma 3.8). Odd p ∤ n: BL Lemma
3.5 applied to U_{n/2} (8/n = 4/(n/2), n/2 ∈ ℤ_p^*). Squares: BL Lemma 3.9 applied to n/2 at each p | n.
(Checked by reading BL §3.3: the proofs of Lemmas 3.2, 3.4, 3.5, 3.9 are p-local for odd p and use the numerator 4
only as a p-adic unit, via (1.2) and (2.5); they hold verbatim with 8 in place of 4. Numerical check below.) ∎
EVIDENCE: `scripts/tf_schinzel_bm.py` Hilbert symbols (explicit formulas, reciprocity asserted at every point):
on all 679 positive solutions of 8/n for n ∈ {127, 137, 239, 251, 1009, 1053, 105}, ∏_{p|n} = −1, inv₂ = +1,
inv_∞ = −1; `scripts/tf_schinzel_t1.py 8 100`: n = q² (q ≤ 100 prime): 592 solutions, **0 Type I, 0 Type II**.
Controls: m = 16 (q ≤ 100) 0/0 (211 solutions); m = 12 0/0 (124 solutions); m = 5, 6 (no T1): 351/135 resp. 147/63
Type I/II — the last three for q ≤ 60 (R194 repair, D6; at q ≤ 100: m = 12 271, 0/0; m = 5 696/269; m = 6 306/120).

**Theorem 5.2 (non-T1 failures of 8/n; CERTIFIED).** 8/n = 1/x + 1/y + 1/z has **no** solution in positive
integers for n ∈ {2, 3, 11, 17, 131, 241}; these are all such n with 2 ≤ n ≤ 299, and 3, 11, 17, 131, 241 are all such odd primes
≤ 2·10⁵ (`tf_schinzel.py 8 200000`). Every odd square k² ≤ 20000 (k odd, k ≥ 3) is solvable.
**Known (R194 repair, D2):** this reproduces Pomerance–Weingartner (arXiv 2511.16817, Ramanujan J. 69 (2026) Paper 31;
`sources/pomerance-weingartner-2511.16817/`), Table 1, row m = 8: all exceptions n ≤ 10¹³ are 1, 2, 3, 11, 17, 131, 241.
PW Thm 3.1 proves that for every m ≥ 8 more than exp(c φ(m)^{1/3}/(log m)^{2/3}) primes p have m/p insoluble (an
Elsholtz–Tao-type sieve: the "lottery" failures are a theorem for large m). Our computation is an independent check.
*Certification.* Positivity gives x ≤ y ≤ z, n/8 < x ≤ 3n/8 and the divisor equation (Ay − B)(Az − B) = B²
(`scripts/tf_schinzel.py`, divisor enumeration) — the classical ES finiteness; independently
`scripts/tf_schinzel_brute.py` (Fractions, y ≤ 2/r, no divisors): 0 solutions at 3, 11, 17, 131, 241, and the same
counts as method A at controls (e.g. 8/127: 23, 8/239: 58; 4/131: 32, 4/241: 8).

**Theorem 5.3 (not Brauer–Manin; PROVED by certificate, modulo BL Thm 1.6; also BL Remark 1.10, which states the
Thm 1.8 version for m/n — R194 repair, D4).** For n ∈ {3, 11, 17, 131, 241},
(U(ℝ)₊ × ∏_p 𝒰(ℤ_p))^{Br U} ≠ ∅ for the model 𝒰: 8xyz = n(xy + yz + zx). Certificates (`tf_schinzel_bm.py 8 …`):
n = 131: P₀ = (23, 57, 171741/8) > 0, bad only at 2, P₁ = (30, 36, −23580) (2-integral), inv₂α = +1 for both;
n = 241: P₀ = (36, 185, 1605060/19) > 0, bad only at 19, P₁ = (36, 180, −7230), inv₁₉ α = +1 for both.
(Adelic point: P₀ at ∞ and p ≠ q, P₁ at q; its invariant sum equals that of the global P₀, i.e. 0.)
(R194 repair, D4; reviewer's certificates, `scripts/review_tf_schinzel_run.py cert`) n = 3: P₀ = (1, 1, 3/2), T = {2},
P₁ = (−60, −60, 10/27); n = 11: P₀ = (2, 6, 33/2), T = {2}, P₁ = (−60, −60, 330/251); n = 17: P₀ = (3, 8, 408/5), T = {5},
P₁ = (−60, −60, 510/257); equal invariants at q in each case.

**Corollary 5.4 (PROVED, modulo the BL citations above; R194 repair, D3: immediate from BL Remark 1.10 + PW Table 1,
and already witnessed at n = 3, where insolubility is elementary — x ≤ 3n/8 forces x = 1, then y = 1, 1/z = 2/3; what
131, 241 add is that the failure is not a "m/n close to 3" size effect, which is Assessment).** In BL's family of Erdős–Straus-type models of the *same*
ℚ-surface, the member 8/n has (i) the same real anchor and an order-2 T1 at odd squares (Prop 5.1), (ii) no
Brauer–Manin obstruction at n = 131, 241 (Thm 5.3), (iii) no positive integral point at n = 131, 241 (Thm 5.2).
So **"Brauer–Manin + T1 is the only obstruction" is false for Erdős–Straus-type integral models**, already over ℚ
with positivity and order 2; TES (§2–3) shows the same for order 3 over ℚ(ω).

**Counts (EVIDENCE, complete enumeration, x ≤ y ≤ z).** Mean / min number of positive solutions over primes:
| m | p ∈ [100, 300) | p ∈ [1000, 1300) |
|---|---|---|
| 4 (ES) | 32.8 / 6 | 62.2 / 11 |
| 8 | 13.5 / 0 (2 zeros) | 27.4 / 3 |
| 12 | 7.2 / 0 (1 zero) | 15.2 / 0 (1 zero) |
In these ranges failures occur only where the mean count is ≲ 15; ES's counts are ≈ 2.4× those of 8/n and its
minimum over these primes is ≥ 6. Positive solutions of 8/n correspond exactly to positive solutions of 4/n with all three denominators even
(8/n = Σ 1/u_i ⟺ 4/n = Σ 1/(2u_i)), so 8/n is a *sub-problem* of ES at the same n. **Assessment (speculative):** the absence of known ES failures and of 8/n failures in (241, 2·10⁵] is
consistent with a count-size explanation; the data do not exclude an additional qualitative structure specific to
numerator 4.

**Barrier (B7, "sibling barrier").** *Precise content (PROVED = Cor 5.4):* no theorem of the form "for every model
in BL's Erdős–Straus/Schinzel family, (W)^{Br} ≠ ∅ ⇒ a positive integral point exists" (BM is the only obstruction to
the integral Hasse principle, T1 included) is true; so ES cannot be deduced from such a family-uniform principle.
*Context (R194 repair, D3):* nobody would posit the principle for all n (Schinzel's conjecture carries n > n₀(m)); the
meaningful family version — n₀ uniform in m — is refuted by PW Thm 3.1 + BL Rem 1.10 (failures up to exp(m^{1/3+o(1)})).
BL Thm 1.9 already shows U_n(ℚ) is not dense in U_n(𝔸)^{Br}_• for every n; Cor 5.4's increment is that the failing open
set is the specific W of the 8/n problem. The genuinely new part of this document is the TES half (§1–§3).
*Assessment (R-O194 repair: formerly stated as a near-consequence; it is not one):* arguments that use only the data
shared by 4/n and 8/n — local/congruence data, the Brauer class and reciprocity, auxiliary primes with prescribed
symbols — would, if they proved solvability at every prime, also prove it for 8/n, which is false; an ES proof
must therefore use something specific to the integral model 4/n (e.g. a pointwise count lower bound, or structure
of the denominators' parities, since 8/n is the all-even sub-problem of 4/n). Cor 5.4 does not exclude arguments
that prove solvability only for p > p₀ and the failures above are all small; it says nothing about which specific
ingredient must be used.
