# Z53_SQSIEVE — depth lane SQSIEVE (follow-up to HYPSUMPROD; FRONTIER §7.1): the square sieve on the tied hyperbola — exponent, reach, reverse direction

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results are internally reviewed only
(not refereed).

Brief: `z52bbriefs/z53_depth.md`, lane kickoff `z52bbriefs/z53_lanes.md` §SQSIEVE. Predecessor: `Z53_HYPSUMPROD.md`
(Theorem 1: R(n) ≪ n^{1/3−1/225}(log n)², cross-reviewed in `data/z53/xreview/REVIEW_HYPSUMPROD.md`). Scripts
`scripts/z53_sqsieve_*`, data `data/z53/sqsieve/`.

*Status: CHECKPOINT 1 (skeleton; statements, why open, first lemmas and first falsifier checks).*

## 0. Notation (as in HYPSUMPROD)

n ≥ 2; R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}. Dyadic block 𝔅(U,V,W): u ∈ (U,2U], B ∈ (V,2V], C ∈ (W,2W]; N(U,V,W) its
count; UVW ≍ n for nonempty blocks; exponents U = n^α, V = n^β, W = n^γ, α + β + γ = 1 + O(1/log n). Trivial bound
N ≤ n^{o(1)} min(U, V, W) (Z52D Thm 1). By the symmetry (u,B,C) ↦ (B,u,C) we may take U ≤ V.
Strip coordinates (HYPSUMPROD Lemma 1.1): k = uB, s = u + B = 4Ck − n, and f(C,k) := (4Ck − n)² − 4k = (u − B)².
χ_Q = Jacobi symbol mod Q = qq′ (q ≠ q′ odd primes).

## 1. Statements attacked

**(S1) Exponent.** Improve the HYPSUMPROD exponent 1/3 − 1/225 ≈ 0.32889 for R(n) ≪ n^{θ+ε}, uniformly in n.
→ Theorem A (target): **R(n) ≪_ε n^{12/37+ε}** (12/37 ≈ 0.32432), PROVED relative to the same textbook inputs as HYPSUMPROD
(third-derivative test) plus Weil's Kloosterman bound; n^{21/65+ε} relative to Bourgain's exponent pair (13/84+ε, 55/84+ε);
n^{4/13+ε} CONDITIONAL on the exponent pair (ε, 1/2).
**(S2) Reach.** Determine the block shapes (α, β, γ) where the square sieve beats min(α, β, γ); does it reach the balanced
block u, B ≍ n^{1/4}, C ≍ n^{1/2}? → Proposition B (target): explicit linear region; at the balanced block the route
is *exactly* at the trivial exponent even under the exponent-pair conjecture (scoped barrier: needs beyond-square-root
cancellation in the dual C-sums).
**(S3) Reverse direction.** Is there a lower-bound, square-sensitive version (must vanish at odd squares n = m²)?
→ Theorem C (target): square-sensitivity is exactly the Brauer–Manin twist (−k/n) (squares of f on the strip at coprime
points lie in 𝒜⁻ = {(−k/n) = −1}, empty at n = m²); every square-sieve datum of fixed (auxiliary) conductor is the same at
odd squares; lower bounds reduce to closed items (low-conductor universality, Cor A′) or to B2.

## 2. Why this is not already closed
HYPSUMPROD proved Theorem 1 with exponent 74/225 using absolute values of per-class discrepancies (Q² residue classes, each
bounded by Vaaler + third-derivative test); it did not use the Fourier structure of the character in the k-variable, did not
smooth the strip, did not optimise per block (it used a single near-cube region with η-loss), and left reach and the
reverse direction open ("not pursued"; §4.3 "not an impossibility theorem"; §5 one sentence). None of the closed items
(one-step dualization at fixed conductor; ET/Fejér with max|S_h| input; Cauchy–Schwarz in the function variable;
low-conductor universality) covers the new step: here Poisson is applied in k *inside* each fixed C with a χ_Q-twist, and
the dual sums are complete Kloosterman sums (mod Q) times exponential sums in C — an upper-bound argument, not a main-term
or positivity argument.

## 3. First lemmas (PROVED; checked numerically)

**Lemma W (complete twisted sums).** For an odd prime q, c, ℓ, n ∈ ℤ let G^{(q)}_c(ℓ) := Σ_{k mod q} (f(c,k)/q) e(ℓk/q).
Then |G| ≤ 2√q if q ∤ ℓ; if q | ℓ, G = K_q(c) ∈ {0, −1, q − 1} (HYPSUMPROD Lemma 1.3). Consequently Σ_{c mod q}|G_c(ℓ)| ≤ 2q^{3/2}
for every ℓ, and for Q = qq′: Σ_{c mod Q}|G^{(Q)}_c(ℓ)| ≤ 4Q^{3/2}.
*Proof sketch (full proof in §4).* For q ∤ c, q ∤ ℓ complete the square in k and open the Legendre symbol by Gauss sums: the sum
becomes a Kloosterman sum S(·,·;q) (or a Ramanujan-type sum of modulus 1 in the degenerate-discriminant case); Weil. For
q | c it is a Gauss sum (modulus √q). CRT for Q.
*Check:* `scripts/z53_sqsieve_checks.py 23 20000`: all 27 962 cases (q ≤ 23, all n, c, ℓ mod q) pass; max |G|/√q = 1.931.

**Lemma P (Poisson in k).** For Φ ∈ C_c^∞(ℝ), C ≥ 1, Q ≥ 1, S > 0:
Σ_{k∈ℤ} Φ((4Ck − n)/S) χ_Q(f(C,k)) = Σ_{ℓ∈ℤ} (S/(4CQ)) Φ̂(ℓS/(4CQ)) e(−ℓn/(4CQ)) G^{(Q)}_C(ℓ).
*Check:* `scripts/z53_sqsieve_poisson.py` (Gaussian Φ): agreement to 10⁻¹¹ at n = 1 000 003, 999 999 937, 998 001 = 999²
(odd square), 8 813 281 (test prime) (`data/z53/sqsieve/poisson_check.txt`).

**Lemma BM (Brauer–Manin twist in strip coordinates).** n odd, (u,B,C) a (★) triple with gcd(uBC, n) = 1 ⇒ (−uB/n) = −1
(Jacobi). [Known content: `BM_CORRECTED_COUNT.md` Thm 1.1 for primes.] Check: 87 388 coprime triples with odd n ≤ 20 000,
0 violations.

## 4–9. (to be written: full proof of Theorem A; block map / Proposition B; Theorem C; computations; screens; verdict)
