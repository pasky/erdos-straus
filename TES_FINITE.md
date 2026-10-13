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
In particular for N(π) = 103 the first coordinate ranges over ≤ 40 lattice points with N ≤ 11.4 (x, y) or N ≤ 45.8
(z): TES(π) is decided by a few hundred factorisations.
*Contrast with SYNTHESIS_SPARKS2 Prop 3.1/Thm 3.5:* the shot family with D = Q³ has z = Z/Q³ ∉ O; it lives in
TES^{□₃}, whose solution set at fixed n is infinite (the mute places q | Q supply the escape that (a) forbids for
integral denominators). So TES and TES^{□₃} differ exactly as ES and ES^{(S)} do (FIXED_MODULUS_SHOTS Thm 6.2(iii)).

## 2. Certified exhaustive search: TES fails at 15 primes outside its T1 set

Implementation. `scripts/tf_core.py` (ℤ[ω] arithmetic and factorisation written from scratch, not importing
`tw_eis.py`), `scripts/tf_exact.py` (**method A**: Cor 1.2 disk for x_i + complete divisor enumeration of
B²c_jc_k, all six associates), `scripts/tf_brute.py` (**method B**, independent code path, numpy, *no factorisation*:
Prop 1.1(a) disk for x_i, then Prop 1.1(b)'s disk N(x_j) ≤ 4N(c_j)N(B)/N(A) for the smaller of the two remaining
weighted denominators — both choices of j — and x_k = c_kBx_j/(Ax_j − Bc_j) tested for integrality; int64 overflow
guarded by assertions). Every reported solution is verified exactly in O (9x₁x₂x₃ = n(Σ c_i ∏_{k≠i} x_k)), all
three coordinates 2-primary. `scripts/tf_compare.py 6000` (4 min): for all 394 primes π of O with N(π) ≤ 6000
(one 2-primary π per conjugate pair of split primes — TES(π) ⟺ TES(−π) ⟺ TES(π̄) by x_i ↦ −x_i, resp. complex
conjugation with x ↔ y — and the inert p ≤ 71) **methods A and B return identical solution sets** (4160 solutions
in total). Cross-check with O182: for N(π) ∈ {307, 439, 601, 1009, 1213, 2011} the O182 window solutions
(`tw_eis_solve.run`, B = 60) are a subset of — in fact equal to — the complete sets.

**Theorem 2.1 (non-T1 failures of TES; CERTIFIED = PROVED Cor 1.2 + two independent exhaustive computations).**
TES(π) has **no solution** for the 2-primary primes π with
`N(π) ∈ {7, 13, 19, 61, 79, 97, 103, 151, 193, 211, 367, 409, 769, 2029, 2239}`
(both conjugates, both signs), and for every other prime π of O with N(π) ≤ 6000, π ∤ 6 (split, or inert p ≤ 71),
TES(π) has a solution. Every solution found at a prime has Type I or Type II shape (3126 Type I, 1034 Type II).
Representatives: N = 103: π = 11 + 2ω; N = 151: −9 − 14ω; N = 7: −1 + 2ω.
Since these n = π are primes, hence not cubes, and satisfy the necessary local condition n ≡ 1 (mod 2) of TWISTED_T1
Lemma 3.1, **the TES-analogue of "T1 is the only obstruction" (the analogue of CONJECTURE SQ) is false**: TES is a
T1-bearing ES analogue whose solvability set is not "everything except the T1 set (cubes)". This is the first
T1-bearing ES-type equation in the campaign with a *proved* failure outside its T1 set.

Count statistics (method A census, one π per pair): mean number of solutions 5.96 for N ≤ 1000 (13 zeros among 85
primes), 9.57 on (1000, 3000] (2 zeros / 130), 13.46 on (3000, 6000] (0 / 179). The failures thin out exactly as a
small-mean count would (lottery picture; analysed in §3–4).
