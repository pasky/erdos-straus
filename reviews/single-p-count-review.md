# R277 — hostile review of SINGLE_P_COUNT.md (O260, route (a): counting at one prime)

Reviewer: R277 side agent. Scope: SINGLE_P_COUNT.md as merged from `side-agent/single-p-count`, memos BRAINSTORM/z30_*,
scripts/z30_*, logs/z30_*. From-scratch checks: `scripts/review_r277_*.py` / `.c` (none of the author's code reused).

(work in progress — filled in claim by claim)

## Claim-by-claim verdicts

### Lemma 1.1 (three exact forms of (★); PROVED) — **SOUND**
Re-derived. (1) gcd(u,B) | p and gcd = p is size-excluded; (2) (4uC−1)(4BC−1) = 4C(4uBC−u−B)+1, cofactor ≡ −1 (mod 4C)
since d·d′ ≡ 1, d ≡ −1; swap is fixed-point-free (u = B ⟹ u | p ⟹ 4C − 2 = p, impossible); (3) direct matrix product.
From scratch (`scripts/review_r277_exact.py`, part A): triple count = pair form = divisor form (both halves) = SL₂ form
(enumerating a ≡ −1 (mod c) divisors of cp+1) = R* (coprime, u+B odd), and R(p) even, for every prime p < 300: 0 mismatches.

### Lemma 2.1 (genus split; PROVED) — **SOUND** (it is an identity; the content is the definition of M_gen)
Re-derived: for gcd(n,q) = 1, Σ_{χ²=1} χ(n)χ̄(a) = |G/G²|·1[na ∈ G²]; X is *defined* as the complement, so R* = M_gen + X
is tautological once the real-character sum is evaluated. No convergence/truncation issue: 𝒫(n) is finite and each pair
expansion is a finite orthogonality relation. From scratch (part B): for every odd n < 1600, M_gen computed three ways —
(i) definition with s(q) = |units|/|squares| and membership in a brute-force square set, (ii) Prop 2.2(a)'s explicit
Legendre/mod-8 form, (iii) Σ_{pairs} φ(q)^{−1} Σ_{χ real} χ(n)χ(a) with the real characters enumerated by brute force as
homomorphisms (ℤ/q)^× → {±1} — agree exactly in ℚ; also #real chars = |G/G²| = 4·2^{ω_odd(uB)} for every q met.
An independent C engine (`scripts/review_r277_count.c`) reproduces R* and M_gen of the Python code on all odd n < 1600.

### Prop 2.2 (PROVED) — **SOUND** (two MINOR wording points, D7–D8 below)
(a) re-derived (2-part: na ≡ 1 (8) ⟺ n ≡ a (8); odd ℓ | u: a ≡ −B). Exact check: see Lemma 2.1, (ii) = (i).
(b) re-derived: na ∈ G² ⟹ a ≡ x² (q) ⟹ x² + u = B(4uC′ − 1) with f = 4uC′ − 1 ≡ −1 (4u), f | x² + u, contradicting
PARITY_AUDIT Lemma 3.2 (I re-checked that lemma's proof: every prime ℓ ∤ 2u of x² + u has (−u/ℓ) = 1, while χ_{−4u}(f) = −1).
Exact: R* = M_gen = X = 0 at all odd squares 9 … 1521 (part B, in ℚ) and, by the C engine, at all 86 odd squares ≤ 30001.
(c) correct (any lift y of z). (d) re-derived and checked exactly for all 54 admissible pairs with u, B ≤ 11 (part D).

### §2 "Consequence" — does the genus split evade CONDITIONAL_ES's square obstruction, or relocate it? — **SOUND as bookkeeping; the headline overstates what is gained (D1, MAJOR)**
What is true (re-derived): for the *same* count R the principal-character split R = M₀′ + X₀ has M₀′(m²) > 0 = R(m²),
so CONDITIONAL_ES Prop 3.1(3)'s obstruction has an exact analogue for R, and the order-≤2 split removes it: X(m²) = 0, so an
upper bound |X(n)| ≤ g(n) with g square-insensitive is not refuted by T1. (Note CONDITIONAL_ES Prop 3.1 is about a
*different* count, the Type-I slice S(p) of (3.1)–(3.2); the transfer to R is by analogy, which the document should say.)
What it does NOT do:
1. **The obstruction is relocated into (L), not removed.** Any split R = M + X with M ≥ 0, M(m²) = 0 has X(m²) = 0;
   the non-trivial part is that M_gen is explicit. The conditional target is now "(L) M_gen(p) ≥ g(p) AND (U) |X(p)| < g(p)"
   with the same g. (L) at the strength needed — g ≥ sup|X(p)|, which the document's own data put at sd(X) ≈ √(1.4–1.5·2M_gen)
   ≈ log p (my run: var(R − M_gen)/(2·mean M_gen) = 1.375 on [10⁵, 4·10⁵)) — is not reached by anything in the document:
   Prop 4.1 gives log log p (see D2).
2. **(U) is false at the known failures.** X(p) = −M_gen(p) at 409, 577, …, 329617 (M_gen/M₀ ∈ [0.57, 0.92]); my scan of all
   odd n ≤ 30001 finds 446 non-square n with R*(n) = 0 and M_gen(n) up to 11.5 (n = 17767; M₀ = 14.2) — i.e. X = −M_gen at
   Poisson-lower-tail points of every residue class except n ≡ 5 (8) (where the pair (1,2) always hits). So (U) is only
   meaningful asymptotically ("for all p > p₀") and is then exactly a Poisson-scale lower-tail statement: genus removes ≈ 27 %
   of the excess variance (my run: 1.880 → 1.375), leaving CONDITIONAL_ES Prop 3.1(2)'s "pointwise concentration at Poisson
   scale" requirement fully in place. The memo z30_genus_split says this ("only the square obstruction is relocated"); the
   SHARP headline in AGENT_REPORT_O260 and §0 bullet 2 should say it too.
3. No further structured (non-square) family with R* = 0 was found in n ≤ 30001 (zeros look like lower-tail events; 111 of
   the 306 non-square zeros in (5000, 30001] have a square factor, but none of the families k·m² is identically zero —
   e.g. n ≡ 5 (8) never vanishes). So I see no second "free" obstruction for X. EVIDENCE only.

### §3 numerics (EVIDENCE) — **SOUND-AFTER-REPAIRS** (figures reproduce exactly; one interpretation is semi-circular, D4; one constant mislabelled, D6)
Own engine `scripts/review_r277_count.c` (fresh code: Jacobi-symbol genus test, M_Q with g = gcd(q, Q) and weight
s(q)φ(g)/(s(g)φ(q)), which I re-derived: |G_q² ∩ ker(G_q → G_g)| = |G_q²|/|G_g²|), output `logs/review_r277_p1mod4_*.txt`,
stats `scripts/review_r277_stats.py`.
* All 16 899 primes p ≡ 1 (4), 13 ≤ p < 4·10⁵: failures exactly {409, 577, 5569, 9601, 23929, 83449, 102001, 329617}. ✓
* [10⁵, 4·10⁵), N = 12 117: var(R − M)/(2·mean M) = 1.880 (M₀), 1.843 (M₂), 1.375 (M_gen), 1.098 (M_Q, Q = 720720);
  corr 0.156 / 0.169 / 0.554 / 0.648; mean(R − M) = 3.21 / 2.84 / 2.81 / 2.78. All match §3 (1.88, 1.84, 1.375, 1.10;
  0.16, 0.17, 0.55, 0.65; "≈ 2.1–3.2"). ✓
* [10⁶, 1.1·10⁶), all 3642 primes: var(R − M₀)/M₀ = 4.05, var(R − M_gen)/M_gen = 3.04, ratios to 2M: 2.02 / 1.99 / 1.52,
  genus removes 23.8 % of var(R − M₀), corr(R, M_gen) = 0.52. All match. (Not re-run: M_loc,Y and the large-Q column.)
  New datum: M_Q with Q = 720720 (< p here, so non-circular) gives 1.257, corr 0.61 — the local effect survives at p > Q.
* NB ranking: with a common dispersion D, the NB P(0) = D^{−μ/(D−1)} is monotone in μ, so "rank by predicted risk" = rank by
  smallest M. Own run: the two smallest M_Q are 577 (0.66) and 409 (1.14). ✓ — but see D4 on what this means.
* Failures: M_gen/M₀ ∈ [0.57, 0.92] on the 8 failures < 4·10⁵ ✓ (14 failures ≤ 10¹⁰ not re-run).
* Lemma 1.1-type consistency: the 446 non-square zeros of R* below 30001 and 86 squares were found by the same engine.

### Prop 4.1 (CONDITIONAL on GRH) — **SOUND** as stated; its use in §0/§4.4 is overclaimed (D2)
Re-derived: (1, 2ℓ), (2ℓ, 1) ∈ 𝒫(p) iff 6ℓ − 1 ≤ p; q = 8ℓ, s/φ = 8/(4(ℓ−1)); 2-adic: p ≡ −(1+2ℓ) (8) ⟺ ℓ ≡ 1 (4) for
p ≡ 5 (8), ℓ ≡ 3 (4) for p ≡ 1 (8); odd: (p/ℓ) = (−1/ℓ) ⟺ (ℓ/p) = χ₋₄(ℓ) (p ≡ 1 (4)). Hence M_gen(p) ≥ 4Σ 1/(ℓ−1) over the
class, density 1/4; the three non-principal pieces χ₋₄, (·/p), χ₋₄(·/p) (all mod 4p) contribute, under GRH and partial
summation from y = (log p)⁵, O(log²p/√y) = o(1); Σ_{y<ℓ≤p/6} 1/ℓ = log log p − 5 log log log p + O(1). ✓ (The (χ₋₄) piece
does not even need GRH.) The parenthetical Pollack remark matches PARITY_AUDIT E3 / (J)66 (Frobenius class in ℚ(i, √p),
≪ p^{1/4+ε} for p ≡ 1 (8), ineffective). Note: for p ≡ 5 (8) M_gen(p) ≥ R(p) ≥ 2 trivially (pair (1,2), q = 8), so Prop 4.1
has content only for p ≡ 1 (8) — worth one sentence.

### Conjecture 4.2 — **SOUND** (correctly labelled CONJECTURE, calibration only, ES-(★)-strength)
T1-consistency re-derived (a ≡ m² mod the Y-smooth part and a·m² ∈ □ mod the rest ⟹ a ∈ □ mod q by CRT ⟹ excluded).
"Implies R ≥ 1 only together with M_loc,Y → ∞" is correct. Minor: §3's data are at fixed Y = 30/100, not Y(p) → ∞, and
M_loc,Y with growing Y reproduces Y-smooth hits exactly (the R_sm caveat), so "the data fit the error scale" is weaker
evidence than it reads (D6).
