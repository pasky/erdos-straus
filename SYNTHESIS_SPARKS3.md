# SYNTHESIS_SPARKS3 — cross-combinations of (J)13–(J)38 aimed at the two exits (task O208, spark synthesis III)

Exits (STATUS "Spark-relay wave", Assessment): **(E1)** transport ES^{(S)} / ES^□ / V_φ / ES^{(y)} certificates back into
the O(p²) box; **(E2)** a genuinely new finite-search mechanism. Memos: `BRAINSTORM/s3_*.md`; scripts `scripts/s3_*`.
Earlier syntheses: SYNTHESIS_SPARKS.md (O171, (J)1–(J)10), SYNTHESIS_SPARKS2.md (O192, (J)13–(J)25); their combinations
are not repeated. ES is not solved; nothing below claims an infinite case of ES.

## 0. Iteration log (construction → kill → which hypothesis → modification)

(I1) Seed: "(J)23/(J)28 relaxations × (J)31/(J)32 numerator data". Question: is the □/mute relaxation sensitive to
whether the exact finite problem is solvable? Test case: the numerator M = 8, whose exact problem 8/n FAILS at
3, 11, 17, 131, 241 (Pomerance–Weingartner; (J)31/(J)32). Construction: the shot identity with 4 → M (§1). Result:
**M^□ is a theorem for every M ≡ 0 (mod 4) at every odd non-square coprime to M, with T1 exact** (Thm 1.1), and it
holds at all 278 known failing pairs (M, p), M ∈ {8, 12, 16, 20, 24} (also with a FIXED mute set S = {3,5,7,11}).
So the relaxation is *numerator-blind* while the exact problem is not: a relativisation-type barrier for (E1) and
(E2) (§2, Cor 2.1). This is the main finding; it is a barrier, not a route.
(I2) Steering: the barrier's hypothesis is "the argument is valid with 4 replaced by M". Known 4-specific inputs:
(J)32 (five slices = a χ-fibre only for m = 4), the parity split f₄ = f₈ + f₄^{odd} ((J)32 Lemma 2.1), and the
empirical absence of failures. §3 examines transports that use them.

## 1. The M-shot identity and M^□ at every non-square (PROVED, elementary)

**Lemma 1.0 (M-shot identity; PROVED, algebra).** Let M ≥ 1, n ≥ 1, Q ≥ 1, and g ≥ 1 with g | n + MQ², g ≡ −1 (mod M).
Put m′ := (n + MQ²)/g, x := (n + m′)/M, y := n(g+1)/M, z := nx(g+1)/(MQ²). Then x, y ∈ ℤ_{>0} and
`M/n = 1/x + 1/y + 1/z`, den(z) | Q².
*Proof.* m′g = n + MQ² ≡ n and g ≡ −1 (mod M) give m′ ≡ −n (mod M), so x ∈ ℤ. Mx − n = m′, so
M/n − 1/x = m′/(nx), and m′/(nx) − M/(n(g+1)) = (m′g + m′ − Mx)/(nx(g+1)) = (m′g − n)/(nx(g+1)) = MQ²/(nx(g+1)) = 1/z.
z = n·x·k/Q² with k = (g+1)/M ∈ ℤ. ∎ (For M = 4 this is UNIT_ORBIT_ES Prop 2.1.)

Definition. **M^□(n)**: M/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, den(z) an odd square coprime to n.
**M^{(S)}(n)**: the same with den(z) = Q², Q ∈ ⟨S⟩ (S a finite set of odd primes ∤ n). M^□ ⊇ M^{(S)} ⊇ (M/n).

**Theorem 1.1 (M^□ is numerator-blind; PROVED, relative to Dirichlet's theorem only).** Let M ≡ 0 (mod 4) and let
n > 1 be odd with gcd(n, M) = 1.
(a) If n is not a square, there are a prime g ≡ −1 (mod M), g ∤ n, and an odd Q prime to n with g | n + MQ²; hence
M^□(n) holds (Lemma 1.0), with a solution of Type II shape.
(b) (T1 for M-shots.) If n = k² is a square, there is NO pair (g, Q) with g > 1, g ≡ −1 (mod M), gcd(Q, k) = 1 and
g | n + MQ².
*Proof.* Key computation: for every odd g ≡ −1 (mod M), the Jacobi symbol (M/g) = +1. Indeed (4/g) = 1; if 8 | M then
g ≡ 7 (mod 8) and (2/g) = 1; for an odd prime ℓ | M, reciprocity gives (ℓ/g) = (g/ℓ)(−1)^{((ℓ−1)/2)((g−1)/2)}
= (−1/ℓ)(−1)^{(ℓ−1)/2} = 1, since g ≡ −1 (mod ℓ) and (g−1)/2 is odd. Also (−1/g) = −1 (g ≡ 3 mod 4). Hence
**(−M/g) = −1 for every odd g ≡ −1 (mod M).** (∗)
(a) Write n = n₀k², n₀ > 1 squarefree, gcd(n₀, M) = 1. For a prime g ≡ −1 (mod M), g ∤ n:
(n/g) = (n₀/g) = ∏_{ℓ|n₀} (g/ℓ)(−1)^{(ℓ−1)/2} = (g/n₀)(−1/n₀). The Jacobi character (·/n₀) is non-trivial, so there is
a class a (mod n₀) with (a/n₀) = −(−1/n₀); CRT (gcd(n₀, M) = 1) and Dirichlet give a prime g ≡ −1 (mod M), g ≡ a (mod n₀),
g ∤ k. Then (n/g) = −1, so by (∗) (−Mn/g) = 1: −n/M ≡ s² (mod g). Choose Q ≡ ±s (mod g), Q odd, Q ≢ 0 mod every prime
of n (CRT modulo 2g·rad n; g ∤ 2n). Then g | n + MQ², gcd(Q, n) = 1, and Lemma 1.0 applies; den(z) | Q² is odd and
prime to n.
(b) Let ℓ be a prime dividing n + MQ² = k² + MQ². ℓ ∤ 2 (the number is odd), ℓ ∤ M (else ℓ | k, and gcd(k, M) = 1),
ℓ ∤ Q (else ℓ | k). So −M ≡ (k/Q)² (mod ℓ): (−M/ℓ) = 1. By multiplicativity (−M/g) = 1 for every divisor g, contradicting
(∗) for g ≡ −1 (mod M), g > 1. ∎

*Remarks.* (i) (b) is the M-shot form of ET Prop 1.6 / UNIT_ORBIT Cor 1.2; for M = 8 it matches (J)31 Prop 5.1 (8/n has
T1). (ii) For the fixed mute set version, the Gupta–Murty sieve of (J)23 Thm 2.4 should transfer verbatim with the
sifted prime r ≡ −1 (mod M) in place of r ≡ 3 (mod 4) (for r ≡ 3 (mod 4) squares and 4th powers coincide, so the index-2
case of ⟨S⟩ is handled as there). This transfer is an **Assessment (not re-derived)**; the EVIDENCE below is independent
of it.

**EVIDENCE / CERTIFIED examples (`scripts/s3_numerator_blind.py 60`, < 1 s; `scripts/s3_mute_S.py 100000`, < 1 s;
every solution verified in exact rational arithmetic).** For all 278 failing pairs (M, p) of the census
`data/ms/prime_fail_1e8.txt` with M ∈ {8, 12, 16, 20, 24}, p ∤ M (5 + 20 + 37 + 62 + 154 primes; p ≤ 10⁸, the exact
problem M/p has NO solution there — MODEL_SPECIFIC §1, CERTIFIED, reproduced by R197), Thm 1.1(a)'s Dirichlet
certificate exists with g ≤ 239. Smallest example:
`8/131 = 1/20 + 1/131 + 9/2620`   (g = 7, Q = 3; 8/131 itself has no solution in unit fractions).
With the FIXED mute set S = {3, 5, 7, 11}: every failing pair with p ∉ S has an M^{(S)} shot solution, Q ≤ 385.
T1 control: odd squares k² (k < 120, gcd(k, M) = 1), Q < 40, M ∈ {4, 8, …, 24}: 0 shots g ≡ −1 (mod M) (as proved).
Overflow profile: the least overflow Q₁ = Q/gcd(Q, (g+1)/M) over shots with Q ≤ 60 is ≥ 3 at every failing pair
(necessarily: Q₁ = 1 would be an M/p solution); it equals 3 at 131 and 241 (M = 8).
