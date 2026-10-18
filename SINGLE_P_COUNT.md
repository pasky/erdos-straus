# SINGLE_P_COUNT — counting at one prime: the height-dependent target (task O260, route (a))

Status: O260 working draft. **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z30_*`, memos `BRAINSTORM/z30_*.md`, tiny logs `logs/z30_*`.

**Prior work this builds on (and does not redo).** CONDITIONAL_ES ((I)2: Prop 2.3 scale constraint, Prop 3.1 "|S₁| < S₀ must
be square-sensitive", Prop 7.3 local-data hypotheses fail at odd squares, Prop 9.1 termwise GRH misses by p^{1−o(1)}, §5 ranked
table of standard hypotheses); POINTWISE_SPECTRAL ((I)3: "a sufficient statement must be Planck-scale, polylog-accurate and
genus-aware"); PARITY_AUDIT ((J)87: R = M + E, |E| ≪ p^{2/5+o(1)}, tied modulus ⟺ height-dependent target); SYNTHESIS_SPARKS8
((J)89) and B1_LINE ((J)90: census, overdispersion D growing 2.2 → 3.6); s7_lvalue_proxy (hardness ≈ QR-richness, EVIDENCE).
What is new here is listed in §0.

## 0. Summary of new content (updated as the work proceeds)

* §1 (PROVED): exact forms of (★): coprime-pair congruence form, divisor form (brief's (★) corrected: no √-cut, R(p) even),
  and an SL₂(ℤ) form with fixed upper-right entry p (γ ∈ −Γ₁(c(γ))).
* §2 (PROVED): **genus split** R(n) = M_gen(n) + X(n) for every odd n, where M_gen ≥ 0 is the exact contribution of all
  characters of order ≤ 2 (an explicit, computable "genus-corrected main term") and X is the order-≥3 part. M_gen(m²) = 0 and
  X(m²) = 0 identically. M_gen(n) > 0 ⟺ (★) is solvable at n·x² for some x (the square-class relaxation).

## 1. Exact forms of the single-p event (★)

For odd n ≥ 3 put R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (Type II with c = 1; PARITY_AUDIT §0, the "c = 1 line" of
SYNTHESIS_SPARKS8, López's Type B).

**Lemma 1.1 (PROVED, elementary).** Let p ≥ 3 be prime. Then
1. (pair form) R(p) = #{(u, B) ∈ ℕ² : gcd(u, B) = 1, p ≡ −(u + B) (mod 4uB)};
2. (divisor form) R(p) = Σ_{C ≥ 1} #{d ≥ 1 : d | 4Cp + 1, d ≡ −1 (mod 4C)}; the cofactor (4Cp+1)/d is then automatically
   ≡ −1 (mod 4C), and R(p) = 2·Σ_C #{d | 4Cp+1 : d ≡ −1 (4C), d < √(4Cp+1)}; in particular R(p) is even;
3. (SL₂ form) R(p) = #{γ = (a p; c d) ∈ SL₂(ℤ) : c ∈ 4ℕ, a, d ≥ 1, a ≡ d ≡ −1 (mod c)}, and every such γ factors as
   γ = Tᵘ·(−1 0; c −1)·Tᴮ with T = (1 1; 0 1), a = uc − 1, d = Bc − 1, c = 4C.

*Proof.* (1) A triple gives 4uB | p + u + B with C = (p+u+B)/(4uB); gcd(u, B) divides p, and gcd = p would force u, B ≥ p and
4uBC − u − B ≥ 4uB − u − B > p. Conversely, if 4uB | p + u + B then C := (p+u+B)/(4uB) is a positive integer (p + u + B > 0).
(2) (4uC − 1)(4BC − 1) = 4C(4uBC − u − B) + 1 = 4Cp + 1, so (u, B, C) ↦ (C, d = 4uC − 1) is a bijection onto pairs
(C, d) with d | 4Cp + 1, d ≡ −1 (mod 4C) (u = (d+1)/(4C), B = ((4Cp+1)/d + 1)/(4C), the latter integral since
d·d′ ≡ 1 and d ≡ −1 force d′ ≡ −1 mod 4C). The swap (u, B) ↔ (B, u) is a fixed-point-free involution (u = B would give
u | p, so u = 1 and 4C − 2 = p, impossible for odd p), and it exchanges d < √(4Cp+1) with d′ > √(4Cp+1).
(3) Tᵘ(−1 0; c −1)Tᴮ = (uc − 1, (uc − 1)B − u; c, cB − 1), whose upper-right entry is ucB − u − B = p for c = 4C.
Conversely, given γ, put u = (a + 1)/c, B = (d + 1)/c; det γ = 1 gives (uc − 1)(Bc − 1) − pc = 1, i.e. ucB − u − B = p. ∎

*Remarks.* (i) The brief's "(★) = Σ_C #{d | 4Cp+1 : d ≡ −1 (4C), d < √(4Cp+1)}" counts unordered solutions = R(p)/2.
(ii) In (3) the condition is −γ ∈ Γ₁(|c|) with c the matrix's own lower-left entry: the SL₂ shadow of the height-dependent
target of PARITY_AUDIT Remark 3.1. Equivalently p is the Hirzebruch–Jung (minus) continuant of the length-3 word (u, 4C, B).
(iii) In (1) the pair set depends on p only through size; the arithmetic of p enters only through the residue p mod 4uB.

## 2. The genus split: where the odd-square obstruction lives in the character expansion

For odd n ≥ 3 let 𝒫(n) := {(u, B) ∈ ℕ² : gcd(u, B) = 1, u + B odd, 4uB − u − B ≤ n}; for (u, B) ∈ 𝒫(n) put q := 4uB,
a := −(u + B) (a unit mod q: gcd(u + B, uB) = 1 and u + B is odd). Put R*(n) := Σ_{𝒫(n)} 1[n ≡ a (mod q)]; by Lemma 1.1(1),
R*(p) = R(p) for primes p (the pairs with 4uB | p + u + B automatically have u + B odd and lie in 𝒫(p)). For a modulus q let
s(q) := |(ℤ/q)^× / ((ℤ/q)^×)²| (= 2^{ω(q odd)}·4 when 8 | q, which always holds here since one of u, B is even).

**Lemma 2.1 (genus split; PROVED).** For every odd n ≥ 3, R*(n) = M_gen(n) + X(n), where
  M_gen(n) := Σ_{(u,B) ∈ 𝒫(n)} (s(q)/φ(q))·1[gcd(n, q) = 1 and n·a ∈ ((ℤ/q)^×)²],
  X(n) := Σ_{(u,B) ∈ 𝒫(n)} φ(q)^{−1} Σ_{χ mod q, χ² ≠ 1} χ(n) χ̄(a).
M_gen(n) is exactly the contribution of the characters of order ≤ 2 to the orthogonality expansion of R*(n), and equals
Σ_{𝒫(n)} Prob_{y ∈ (ℤ/q)^{×2}}[q | n·y + u + B] (the expected count when n is replaced, pair by pair, by a uniformly random
element of its square class mod q).
*Proof.* For gcd(n, q) = 1, 1[n ≡ a] = φ(q)^{−1} Σ_χ χ(n)χ̄(a). The real characters are exactly the characters of
G/G², G = (ℤ/q)^×, a group of order s(q), so their sum is s(q)·1[na ∈ G²] (χ̄ = χ for real χ). If gcd(n, q) > 1 then
n ≢ a (a is a unit) and both sides vanish. For the last formula: |G²| = φ(q)/s(q), and #{y ∈ G² : ny ≡ a} = 1[a n^{−1} ∈ G²]. ∎

**Proposition 2.2 (PROVED).** (a) M_gen(n) ≥ 0; it is a function of the Legendre symbols (n/ℓ) at the odd primes ℓ ≤ n
and of n mod 8 only (explicitly: for (u, B) ∈ 𝒫(n) the indicator is 1[n ≡ −(u+B) (mod 8)]·∏_{ℓ | u odd}1[(n/ℓ) = (−B/ℓ)]·
∏_{ℓ | B odd}1[(n/ℓ) = (−u/ℓ)]).
(b) **(T1 is entirely genus.)** If n = m² then M_gen(n) = 0, R*(n) = 0 and hence X(n) = 0.
(c) M_gen(n) > 0 ⟺ there are (u, B) ∈ 𝒫(n) and y coprime to 2uB with 4uB | n·y² + u + B, i.e. (u, B, C) solves (★) at
the integer n·y² (with the pair in the size range of n).
(d) For each pair, the average of the pair term of M_gen over n in the reduced classes mod q equals 1/φ(q), the same as
the average of 1[n ≡ a]: the split is mean-preserving pair by pair.
*Proof.* (a) Square classes mod q = 2^k·∏ℓ^e (k ≥ 3) are detected by n mod 8 and the Legendre symbols at the odd ℓ | q;
a ≡ −B (mod ℓ) for ℓ | u and a ≡ −u (mod ℓ) for ℓ | B. (b) If gcd(m, q) > 1 the term is 0. Otherwise n·a ∈ G² ⟺ a ∈ G²,
i.e. −(u+B) ≡ x² (mod 4uB) for some x. Then x² + u + B = 4uBC′ with C′ ≥ 1, so f := 4uC′ − 1 ≡ −1 (mod 4u) divides x² + u,
contradicting PARITY_AUDIT Lemma 3.2 (a square plus u has no divisor ≡ −1 (mod 4u)). R*(m²) = 0 by the same lemma
(4uB | m² + u + B gives such an f). (c) n·a ∈ G² ⟺ a ≡ n·z² for a unit z ⟺ q | n z² + u + B; take y = z (any lift). (d) Over n ∈ G,
#{n : na ∈ G²} = |G²| = φ(q)/s(q), so the average of (s(q)/φ(q))·1[na ∈ G²] is 1/φ(q), as is that of 1[n ≡ a]. ∎

**Consequence for the conditional question (Assessment, building on CONDITIONAL_ES Prop 3.1(3) and Prop 7.3).** CONDITIONAL_ES
shows that any proof of "|S₁| < S₀" (principal-character main term against the rest) must fail at odd squares. In the split
R = M_gen + X the square-sensitivity sits entirely in the explicit nonnegative term M_gen, which depends on p only through its
quadratic characters (Prop 2.2(a)); X vanishes at squares, so **any upper bound |X(n)| ≤ g(n) is consistent with T1**. The
single-p problem therefore splits into
  (L) a lower bound M_gen(p) ≥ g(p) — a statement about the real character χ_p alone (L-function territory: L(1, χ_{−up})-type
      quantities, §4), and
  (U) |X(p)| < g(p) — cancellation among the characters of order ≥ 3, where no square obstruction remains.
Neither is proved; §3 measures how much of the actual fluctuation each part carries.

## 3. Numerics: how the fluctuation of R(p) splits (EVIDENCE; goal 4)

Engine `scripts/z30_rgen.c` (C; one pass over 𝒫(p), ≈ (p/4)·log p pairs; aborts if a hit is not genus-matched — never
happened). Columns: R; M₀ = Σ 1/φ(q) (p a uniform unit mod q); M₂ = conditioning on p mod 8; M_gen (Lemma 2.1);
M_loc,Y = conditioning on p modulo the full Y-smooth part of q (all prime powers of primes ≤ Y, incl. 2) and on the square
class of p modulo the rest; R_sm,Y = hits whose q is Y-smooth (these are reproduced exactly by M_loc,Y). Consistency checks:
M_loc,0 = M_gen and M_loc,∞ = R (checked at 409, 101, 10007, 1000033); M_gen(m²) = R(m²) = 0 for the squares tested
(9409, 10201, 2025, 225, 441; exact rational check for odd m < 40 in `scripts/z30_check_forms.py`). Summary statistics
`scripts/z30_stats.py`, output `logs/z30_variance.txt`.

Since R(p) is even (Lemma 1.1(2)), the independent-incidence ("swap-paired Poisson") baseline is var R ≈ 2·E R.

| sample | N | mean R | var(R−M₀)/M₀ | var(R−M_gen)/M_gen | var(R−M_loc,30)/M_loc | resid. var / 2(M_loc − R_sm) |
|---|---|---|---|---|---|---|
| all p ≡ 1 (4) in [10⁶, 1.1·10⁶] | 3642 | 32.0 | 4.05 | 3.04 | 1.99 | 1.66 |
| first 576 of those, Y = 100 | 576 | 31.8 | 4.24 | 3.27 | 1.44 (Y=100) | 1.89 |
| p ≡ 1 (4) in [10⁷, 10⁷+12000] | 343 | 42.2 | 4.52 | 3.60 | — | — |

Findings.
* The quadratic-character (genus) part removes ≈ 24 % of var(R − M₀) (corr(R, M_gen) ≈ 0.5); conditioning on p mod 8
  alone removes nothing. So the genus correction is real but not dominant.
* Full local data at primes ≤ 30 (plus genus) removes ≈ 50 %; corr(R, M_loc,30) = 0.71, and 0.81 at Y = 100. About 37 %
  (Y = 30) to 57 % (Y = 100) of all hits have a Y-smooth modulus 4uB.
* **The residual does not reach the Poisson baseline:** after removing the local part, var(R − M_loc) is still ≈ 1.7–1.9 ×
  2(M_loc − R_sm), and the ratio does not fall from Y = 30 to Y = 100. The excess is therefore not small-prime local
  structure. Hypothesis (Assessment): it is the divisor-sharing correlation (pairs sharing u, B or C test divisibility of the
  same integer p + u, p + B or 4Cp + 1, and divisor counts of one integer are overdispersed like τ); this would also explain
  the slow growth of the overdispersion with p (4.05 → 4.52 here; 2.2 → 3.6 for the b = 1 line, B1_LINE).
* The 14 known (★)-failures ≤ 10¹⁰ (all ≤ 8.9·10⁶) have M_gen/M₀ ∈ [0.57, 0.92] and M_loc,30/M₀ ∈ [0.10, 0.67]: low local
  main terms, but for p > 10⁵ still M_loc,30 ≈ 10–26, so the failures are not explained by the local term alone.
* Calibration for goal 4 (Assessment): at 10⁶–10⁷ the actual error |R − M_loc| has standard deviation ≈ 1.3·√(2M), i.e.
  ≈ log p in absolute size, against a main term ≈ (log p)²/8. Nothing in the data suggests |E(p)| ≍ M(p) generically; the
  failures are lower-tail events of a moderately overdispersed count.
