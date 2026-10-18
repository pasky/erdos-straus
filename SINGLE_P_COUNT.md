# SINGLE_P_COUNT — counting at one prime: the height-dependent target (task O260, route (a))

Status: O260 working draft. **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z30_*`, memos `BRAINSTORM/z30_*.md`, tiny logs `logs/z30_*`.

**Prior work this builds on (and does not redo).** CONDITIONAL_ES ((I)2: Prop 2.3 scale constraint, Prop 3.1 "|S₁| < S₀ must
be square-sensitive", Prop 7.3 local-data hypotheses fail at odd squares, Prop 9.1 termwise GRH misses by p^{1−o(1)}, §5 ranked
table of standard hypotheses); POINTWISE_SPECTRAL ((I)3: "a sufficient statement must be Planck-scale, polylog-accurate and
genus-aware"); PARITY_AUDIT ((J)87: R = M + E, |E| ≪ p^{2/5+o(1)}, tied modulus ⟺ height-dependent target); SYNTHESIS_SPARKS8
((J)89) and B1_LINE ((J)90: census, overdispersion D growing 2.2 → 3.6); s7_lvalue_proxy (hardness ≈ QR-richness, EVIDENCE).
What is new here is listed in §0.

## 0. Summary of new content

**ES is not solved; no conditional theorem "standard conjecture ⟹ R(p) ≥ 1" was found.** New relative to the prior work:
* §1 (PROVED): exact forms of (★): coprime-pair congruence form R(p) = #{(u, B) : p ≡ −(u+B) (mod 4uB)}, divisor form
  (the brief's (★) corrected: no √-cut; R(p) is even), and an SL₂(ℤ) form with fixed upper-right entry p (−γ ∈ Γ₁(c(γ))).
* §2 (PROVED): **genus split** R(n) = M_gen(n) + X(n) for every odd n: M_gen ≥ 0 is exactly the order-≤2 character part
  (explicit, depends only on n mod 8 and the Legendre symbols of n), X the order-≥3 part. **T1 lives entirely in M_gen:**
  M_gen(m²) = X(m²) = R(m²) = 0. So the conditional target splits into (L) M_gen(p) large (a statement about χ_p) and
  (U) |X(p)| < M_gen(p), which — unlike CONDITIONAL_ES's |S₁| < S₀ — is not refuted at squares.
* §3 (EVIDENCE): variance decomposition of R(p) at 10⁵–10⁷: genus removes ≈ 25 % of the excess variance, bounded-modulus
  local data + genus brings the residual to ≈ 1.1 × swap-Poisson; the non-local part keeps an overdispersion ≈ 1.7–1.9.
  A bounded-modulus local main term M_Q (p mod 720720 + χ_p) ranks 577 and 409 as the two most endangered primes < 4·10⁵
  (both are failures). T1 control: all 499 odd squares ≤ 10⁶ give 0 for R and every main term.
* §4: (L) under GRH: M_gen(p) ≥ (1 − o(1)) log log p (Prop 4.1, CONDITIONAL). (U): audit of GRH, EH/BFI for τ,
  Selberg–Linnik/Hooley R*, Kuznetsov/θ, Hardy–Littlewood single-N — none applies, each for an exact reason;
  Conjecture 4.2 (local main term + CLT-scale error) stated for calibration only (not standard, ES-(★)-strength).
* §5 (PROVED): main term uniform on the log-simplex (no critical range; every dyadic box ≍ 1); **bounded-order sieve
  minorants are nonpositive** (Lemma 5.2) — positivity needs characters of order up to λ(4uB).
* §6 (PROVED + Assessment): Bruhat reading — one Γ_∞-double coset per level c, or one level p with height-dependent target;
  no Σ_c S(m, n; c) with fixed (m, n) arises at fixed p, so Kuznetsov/θ = 7/64 never enters (it does after averaging over p).

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
(T1 control: all 499 odd squares 9 ≤ m² ≤ 10⁶ have R = M_gen = M_loc,30 = M_Q = 0, `logs/z30_squares.txt`; exact rational check for odd m < 40 in `scripts/z30_check_forms.py`). Summary statistics
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
* **Residual dispersion depends on the bookkeeping, and the honest reading is "mostly local, plus a non-local factor
  ≈ 1.7–1.9".** Against the all-pairs baseline 2·M_loc the residual is at swap-Poisson level (var(R − M_loc,30)/(2M_loc)
  = 0.99; 0.72 at Y = 100). But M_loc,Y reproduces the hits with Y-smooth modulus exactly (R_sm,Y), which then carry no
  variance; against the baseline 2(M_loc − R_sm) of the genuinely random pairs the residual is 1.66 (Y = 30) and 1.89
  (Y = 100), not falling with Y. So the non-local part is still overdispersed by a factor ≈ 1.7–1.9. Hypothesis (Assessment,
  not tested to a conclusion): divisor-sharing correlation — hits sharing u, B or C come from divisors of the same integer
  p + u, p + B or 4Cp + 1 (at p = 10007 and 1000033 there are ≈ 2.4 and 4.5 ordered pairs of distinct hits sharing a coordinate per hit,
  beyond the swap partners; `z30_rgen.c` columns WC, WU; the independence null for these was not computed). This would also
  fit the slow growth of the overdispersion with p (4.05 → 4.52 here; 2.2 → 3.6 for the b = 1 line, B1_LINE).
* **A non-circular, bounded-modulus local main term.** M_Q(p) := Σ_{𝒫(p)} Prob[p ≡ a (q) | p mod gcd(q, Q), square class of
  p mod q] = Σ 1[p ≡ a (gcd(q,Q))]·1[pa ∈ □ (q)]·s(q)φ(g)/(s(g)φ(q)), g = gcd(q, Q), uses only p mod Q and the Legendre
  symbols of p (M_1 = M_gen; vanishes at squares by the argument of Prop 2.2(b)). On all 12 117 primes p ≡ 1 (4) in
  [10⁵, 4·10⁵) (`logs/z30_dispersion.txt`): var(R − M)/(2·mean M) = 1.88 (M₀), 1.84 (M₂), 1.375 (M_gen), 1.10
  (M_Q, Q = 720720), 0.86 (Q = 2⁶3³5²7²·11·13·17·19·23·29; this Q makes many small-q pairs exact, so the same caveat as for
  R_sm applies); corr(R, M) = 0.16, 0.17, 0.55, 0.65, 0.74. All main terms underestimate the mean by ≈ 2.1–3.2 (≈ 10 %), a
  prime-specific singular-series effect not modelled here.
  On the 3642 primes p ≡ 1 (4) in [10⁶, 1.1·10⁶) the same ratios are 2.02 (M₀), 1.99 (M₂), 1.52 (M_gen), 1.01 (M_Q with
  the large Q; corr 0.71): the genus share and the local share persist at the larger height.
* **Failure prediction (`scripts/z30_failpred.py`, `logs/z30_failpred.txt`; all 16 899 primes p ≡ 1 (4), 13 ≤ p < 4·10⁵;
  8 observed failures 409, 577, 5569, 9601, 23929, 83449, 102001, 329617).** Negative-binomial lower tail for R/2 with mean
  M/2 and the dispersion fitted on [10⁵, 4·10⁵):

  | main term | predicted failures < 10⁴ / [10⁴,10⁵) / [10⁵,4·10⁵) | observed | rank of 409, 577 by predicted risk |
  |---|---|---|---|
  | M₀ (no arithmetic of p) | 30.3 / 11.5 / 4.0 | 4 / 2 / 2 | not in top 8 (top = 13, 17, 29, …) |
  | M_gen | 18.2 / 5.8 / 1.7 | 4 / 2 / 2 | not in top 8 |
  | M_Q, Q = 720720 | 18.0 / 6.1 / 1.6 | 4 / 2 / 2 | **577, 409 are the top two** |
  | M_loc,30 with exact smooth hits (semi-circular) | 3.1 / 2.6 / 1.2 | 4 / 2 / 2 | **577, 409 top two**; 5569 sixth |

  Reading (EVIDENCE/Assessment): at p ≥ 10⁵ every model is consistent with the 2 observed failures (too few to
  discriminate). Below 10⁴ only the model that counts the small-smooth hits exactly is calibrated; the NB tail with a
  dispersion fitted at larger p overpredicts there. The arithmetic of p enters the risk ranking sharply: with p mod 720720
  and the Legendre symbols of p alone, 409 and 577 come out as the two most endangered primes below 4·10⁵.
* The 14 known (★)-failures ≤ 10¹⁰ (all ≤ 8.9·10⁶) have M_gen/M₀ ∈ [0.57, 0.92] and M_loc,30/M₀ ∈ [0.09, 0.70] (sample mean ≈ 1.0): low local
  main terms, but for p > 10⁵ still M_loc,30 ≈ 10–26, so the failures are not explained by the local term alone.
* Calibration for goal 4 (Assessment): at 10⁶–10⁷ the actual error |R − M_loc| has standard deviation ≈ 1.3·√(2M), i.e.
  ≈ log p in absolute size, against a main term ≈ (log p)²/8. Nothing in the data suggests |E(p)| ≍ M(p) generically; the
  failures are lower-tail events of a moderately overdispersed count.

## 4. The two halves of the conditional target, and what standard hypotheses give for each (goal 1)

### 4.1 The genus half (L): GRH reaches it, at log log scale

**Proposition 4.1 (CONDITIONAL on GRH for the Dirichlet L-functions mod 4p).** For primes p ≡ 1 (mod 4),
M_gen(p) ≥ (1 − o(1))·log log p.
*Proof.* Let ε := +1 if p ≡ 5 (mod 8) and ε := −1 if p ≡ 1 (mod 8), and let ℓ ∤ 2p be a prime with χ₋₄(ℓ) = ε and
(ℓ/p) = ε, ℓ ≤ (p + 1)/6. Then the pairs (u, B) = (1, 2ℓ) and (2ℓ, 1) lie in 𝒫(p) (6ℓ − 1 ≤ p) and are genus-matched by
Prop 2.2(a): the 2-adic condition p ≡ −(1 + 2ℓ) (mod 8) reads 2ℓ ≡ 2 (resp. 6) (mod 8), i.e. ℓ ≡ 1 (resp. 3) (mod 4); the odd
condition is (p/ℓ) = (−1/ℓ), i.e. (ℓ/p) = χ₋₄(ℓ) by reciprocity (p ≡ 1 (4)). Each has q = 8ℓ, s(q)/φ(q) = 8/(4(ℓ − 1)), so
M_gen(p) ≥ 4·Σ 1/ℓ over such ℓ. The indicator of the two conditions is (1 + εχ₋₄(ℓ))(1 + ε(ℓ/p))/4, and under GRH
Σ_{ℓ ≤ x} ψ(ℓ) log ℓ ≪ √x·log²(px) for each non-principal ψ mod 4p; partial summation over (y, (p+1)/6] with
y = (log p)⁵ gives Σ 1/ℓ = (1/4)(log log p − log log y) + o(1) = (1/4 − o(1)) log log p. ∎
(Positivity alone, M_gen(p) > 0 for all large p ≡ 1 (8), also follows unconditionally but ineffectively from a single such
ℓ ≪ p^{1/4+ε}, Pollack 2014 as used in (J)66.) The true size is M_gen(p) ≍ (log p)² (§3: M_gen/M₀ ∈ [0.67, 1.46] on
[10⁶, 1.1·10⁶]); a matching lower bound would need Σ over all u of L(1, χ)-type quantities for the characters
(−u p/·) (heuristic: the u-slice of M_gen is ≈ L(1, (−up/·))·log(p/u)/u up to bounded local factors), with secondary terms
L(1, ψ)L(1, ψχ) of the same order as the main term for small u. Not pursued (Assessment): (L) is not where ES is stuck.

### 4.2 The order-≥3 half (U) and the named hypotheses

(U) asks |X(p)| < M_gen(p), where X(p) = Σ_{𝒫(p)} φ(q)^{−1} Σ_{χ (q), χ² ≠ 1} χ(p)χ̄(a): a sum, at ONE argument p, over
≍ p log p moduli q = 4uB and all their characters of order ≥ 3, of size (data) ≈ √(3M) ≈ log p, needed < M ≍ (log p)².

| hypothesis (as in the literature) | what it controls | applied to (U) | exact missing piece |
|---|---|---|---|
| GRH (Dirichlet) | Σ_{n ≤ x} Λ(n)χ(n) for each χ: sums over n at fixed χ | X is a sum over χ at fixed n = p; termwise GRH misses by p^{1−o(1)} (CONDITIONAL_ES Prop 9.1); GRH does give (L) (Prop 4.1) | a statement about Σ_χ χ(p)c(χ) over χ of all moduli ≤ p at one point; GRH is about the dual sum |
| Elliott–Halberstam / BFI-type for τ (divisors in APs, Σ_{q ≤ x^{1−ε}} max_a \|Δ_τ(x; q, a)\| ≪ x(log x)^{−A}) | the box {(q, N) : q ≤ Q, N ≤ x} | divisor form: the needed pairs (q, N) = (4C, 4Cp + 1) lie on the line N = pq + 1, ≍ Q points of a box of ≍ Qx points; the class modulus is a function of the integer, q = (N − 1)/p | equidistribution on a line of relative density 1/x inside the averaged box; any box error ≥ 1 per q already exceeds the line's total main term |
| Selberg–Linnik / Hooley R* (Σ_{c ≤ X} S(m, n; c)/c ≪ (mnX)^ε; incomplete Kloosterman sums with N^{1/2}q^ε) | complete Kloosterman sums S(m, n; c) with (m, n) fixed, averaged over c | via Lemma 1.1(3): N_c(p) = c^{−1}Σ_{h mod c} e(h/c)Σ_{x \| cp+1} e(hx/c) — additive characters summed over the DIVISORS of the single integer cp + 1, not over all residues; transposing γ (Lemma 1.1(3)) makes the modulus fixed (= p) and the target height-dependent (PARITY_AUDIT Remark 3.1) | completion of the divisor-restricted sums needs a sum over N ≡ 1 (c) in an interval, i.e. over p (B6). At fixed p no complete Kloosterman sum with fixed (m, n) appears |
| Kuznetsov + Kim–Sarnak θ = 7/64 | spectral expansion of Σ_c S(m,n;c)φ(c) | as the previous row; θ enters only after averaging over p ((D)32: Σ_p f_I(p)) | same |
| Hardy–Littlewood (Goldbach-type single-integer asymptotic r(N) ~ 𝔖(N)·J(N)) | named, single-N; main term a power N/log²N | not a statement about (★); its (★)-analogue would be "R(p) = M_loc(p)(1 + o(1))" (Conjecture 4.2) | (★)'s main term is polylog (B3) and its "singular series" must contain the genus factor (Prop 2.2(b)), i.e. a Brauer–Manin-type correction (Bright–Loughran's order-2 algebra; Assessment) |

**Conjecture 4.2 (CONJECTURE; stated for calibration, NOT a standard conjecture).** With M_loc,Y as in §3 and Y = Y(p) → ∞
slowly, R(p) = M_loc,Y(p) + O((M_loc,Y(p))^{1/2+o(1)}) for all large primes p ≡ 1 (mod 4).
It implies R(p) ≥ 1 for all large p **only together with** a lower bound M_loc,Y(p) → ∞ (a type-(L) statement about
the local data of p; for Y = 0 this is Prop 4.1 under GRH; for growing Y not attempted). It is consistent with T1: at n = m²,
every pair term of M_loc,Y vanishes (it would force a ≡ m² mod the Y-smooth part of q and a ∈ □ mod the rest, i.e. a ∈ □
mod q, excluded by Prop 2.2(b)), as does R. The data of §3 fit the error scale (sd ≈ 1.3√(2M)), but the
count is still Poisson-scale: Conjecture 4.2 is ES-(★)-strength in the sense of CONDITIONAL_ES §6 (X_slice), with an
explicit main term. **Answer to goal (1): no named, standard conjecture was found that implies R(p) ≥ 1 (or N₁(p) ≥ 1,
f_II(p) ≥ 1); what is new relative to CONDITIONAL_ES is the location of the missing statement — the order-≥3 characters,
with T1 removed (Lemma 2.1, Prop 2.2) — and that GRH does reach the order-2 half (Prop 4.1).**

## 5. Where the main term lives, and why sieve minorants of bounded character order give nothing (goal 2)

**Lemma 5.1 (main-term density on the log-simplex; PROVED, elementary; refines PARITY_AUDIT Lemma 2.1 and SYNTHESIS_SPARKS8
Lemma 1.5).** Write u = p^α, B = p^β (so C ≈ p^{1−α−β}/4). For fixed 0 ≤ α₀ < α₁, 0 ≤ β₀ < β₁, the naive main term
Σ 1/(4uB) over pairs with u ∈ [p^{α₀}, p^{α₁}], B ∈ [p^{β₀}, p^{β₁}], 4uB − u − B ≤ p equals
(log p)²/4 · Area([α₀, α₁] × [β₀, β₁] ∩ {α + β ≤ 1}) + O(log p).
*Proof.* For fixed u the B-range is B ≤ (p + u)/(4u − 1); Σ_{B ∈ I} 1/B = log-length of I + O(1/min I), and Σ_u 1/(4u)·(…) is
a Riemann sum for (log p)²/4 ∫∫ dα dβ with O(log p) total error (the O(1) per u sums to O(log p) against weights 1/u). ∎
So the main term (log p)²/8 is spread uniformly over the triangle {α, β ≥ 0, α + β ≤ 1} (total area 1/2): there is no
critical range; every dyadic box (u ~ U, B ~ V, C ~ W, UVW ≍ p) carries main term ≍ 1 (≈ (log 2)²/4 ≈ 0.12). In the balanced
box U ≍ V ≍ W ≍ p^{1/3} the pair count is ≍ p^{2/3} and the divisor-enumeration count ≍ p^{1/3+o(1)}; any method whose
error is a power of the box's trivial bound fails in every box, and summed over the ≍ (log p)² boxes the total error must be
o((log p)²) (B3). The 1/φ-weighted main terms of §3 differ from Σ 1/(4uB) by bounded factors on average.
*Decoupling (the brief's question).* In each of the three slicings (fix u: one integer p + u, one modulus 4u; fix B: likewise;
fix C: one integer 4Cp + 1, one modulus 4C) the averaging variable moves both the integer and the modulus; in the pair form
the modulus 4uB and the class −(u + B) move together. No range of the simplex decouples them (Assessment; this is PARITY_AUDIT
Remark 3.1 in coordinates — the only fixed-modulus picture is the transposed one of §6, with height-dependent target).

**Lemma 5.2 (bounded-order minorants are nonpositive; PROVED, elementary).** Let G be a finite abelian group, a ∈ G, k ≥ 1,
and F : G → ℝ with Fourier support in {χ ∈ Ĝ : χ^k = 1} and F ≤ 1_{a} pointwise. If G^k ≠ {1} (i.e. the exponent of G does
not divide k), then F ≤ 0 on all of G.
*Proof.* χ^k = 1 ⟺ χ is trivial on G^k, so F is constant on cosets of G^k. Pick g ∈ G^k \ {1}; F(a) = F(ag) ≤ 1_a(ag) = 0, so
F ≤ 0 on aG^k; off aG^k, F ≤ 1_a = 0. ∎
*Consequence.* A "sieve lower bound" R(p) ≥ Σ_{pairs} F_{pair}(p), with each F_pair a minorant of the point indicator
1[· ≡ a (q)] on (ℤ/q)^×, is ≤ 0 unless the F_pair use characters of order up to the exponent λ(q) (Carmichael) of (ℤ/q)^×; in
particular the genus part (k = 2, Lemma 2.1) supports no positive per-pair minorant: M_gen is a mean-correct
redistribution (Prop 2.2(d)), not a lower bound. Positivity has to come from the full character group, i.e. from (U).

## 6. The spectral reading (goal 3): one double coset per level, or one level per prime

**Proposition 6.1 (PROVED, elementary).** (a) For c ≥ 1, the matrices γ = (a b; c d) ∈ SL₂(ℤ) with a ≡ d ≡ −1 (mod c) form
exactly one double coset Γ_∞ γ_c Γ_∞, γ_c = (−1 0; c −1) (Γ_∞ = {±Tⁿ}), and inside it b(Tᵘγ_cTᴮ) = ucB − u − B. Hence
R(p) = Σ_{c ∈ 4ℕ} N_c(p), N_c(p) = #{(u, B) ∈ ℕ² : ucB − u − B = p} = #{x | cp + 1 : x ≡ −1 (mod c)}.
(b) In the Kloosterman sum S(m, n; c) = Σ_{ad ≡ 1 (c)} e((ma + nd)/c) this double coset is the single term (a, d) ≡ (−1, −1),
and isolating it costs the full frequency average: c^{−2}Σ_{m, n mod c} e((m + n)/c)·S(m, n; c) = 1.
(c) Transposing by S = (0 −1; 1 0): Sγ S^{−1} = (d −c; −b a), so {γ : b(γ) = p} ↔ {γ′ : c(γ′) = −p}: a single level p,
i.e. the pairs (a, d) on ad ≡ 1 (mod p) (the modular hyperbola 𝓗 of PARITY_AUDIT), with the condition a ≡ d ≡ −1 modulo
the height c = (ad − 1)/p of the point (the height-dependent target).
*Proof.* (a) Γ_∞γΓ_∞ is determined by (c, a mod c, d mod c); Tᵘ(−1 0; c −1)Tᴮ = (uc − 1, (uc−1)B − u; c, cB − 1) as in
Lemma 1.1(3); a, d ≥ 1 ⟺ u, B ≥ 1. (b) Orthogonality: Σ_{m,n} e((m(a+1) + n(d+1))/c) = c²·1[a ≡ d ≡ −1]. (c) Direct. ∎

**Assessment (what Kuznetsov / θ = 7/64 can see).** Kuznetsov's formula controls Σ_c S(m, n; c)φ(4π√(mn)/c)/c for FIXED
(m, n), averaged over the level c. In picture (a)–(b) the level c runs, but each level contributes one fixed double coset
(all frequencies m, n ≤ c are needed to select it, (b)) and inside that double coset the b-entry constraint b = p is the
divisor problem for the single integer cp + 1 — not a Kloosterman sum. In picture (c) the frequencies are free but the
level is the single prime p: the only tool is Weil (p^{1/2+o(1)} per box), and the target is height-dependent. So at
fixed p no sum Σ_c S(m, n; c) with fixed (m, n) and c in a long range arises, and the exceptional-eigenvalue parameter
θ never enters. It enters after averaging over p, where the campaign already used it ((D)32: Σ_{p ≤ N} f_I(p) ≪ N log²N,
now unconditional by (D)32b). This is the same tied/height-dependent dichotomy (PARITY_AUDIT Remark 3.1), now in
Bruhat coordinates: "tied" = picture (a)–(b), "height-dependent" = picture (c).
