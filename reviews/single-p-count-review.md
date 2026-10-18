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

### Prop 4.1 (CONDITIONAL on GRH) — **SOUND** as stated; its use in §0 / §4.2 is overclaimed (D2)
Re-derived: (1, 2ℓ), (2ℓ, 1) ∈ 𝒫(p) iff 6ℓ − 1 ≤ p; q = 8ℓ, s/φ = 8/(4(ℓ−1)); 2-adic: p ≡ −(1+2ℓ) (8) ⟺ ℓ ≡ 1 (4) for
p ≡ 5 (8), ℓ ≡ 3 (4) for p ≡ 1 (8); odd: (p/ℓ) = (−1/ℓ) ⟺ (ℓ/p) = χ₋₄(ℓ) (p ≡ 1 (4)). Hence M_gen(p) ≥ 4Σ 1/(ℓ−1) over the
class, density 1/4; the three non-principal pieces χ₋₄, (·/p), χ₋₄(·/p) (all mod 4p) contribute, under GRH and partial
summation from y = (log p)⁵, O(log²p/√y) = o(1); Σ_{y<ℓ≤p/6} 1/ℓ = log log p − log log log p + O(1). ✓ (The (χ₋₄) piece
does not even need GRH.) The parenthetical Pollack remark matches PARITY_AUDIT E3 / (J)66 (Frobenius class in ℚ(i, √p),
≪ p^{1/4+ε} for p ≡ 1 (8), ineffective). Note: for p ≡ 5 (8) M_gen(p) ≥ R(p) ≥ 2 trivially (pair (1,2), q = 8), so Prop 4.1
has content only for p ≡ 1 (8) — worth one sentence.

### Conjecture 4.2 — **SOUND** (correctly labelled CONJECTURE, calibration only, ES-(★)-strength)
T1-consistency re-derived (a ≡ m² mod the Y-smooth part and a·m² ∈ □ mod the rest ⟹ a ∈ □ mod q by CRT ⟹ excluded).
"Implies R ≥ 1 only together with M_loc,Y → ∞" is correct. Minor: §3's data are at fixed Y = 30/100, not Y(p) → ∞, and
M_loc,Y with growing Y reproduces Y-smooth hits exactly (the R_sm caveat), so "the data fit the error scale" is weaker
evidence than it reads (D6).

### §4.2 conjecture table — **SOUND-AFTER-REPAIRS** (reasons correct; one omission, D5)
* GRH row: correct (X is a sum over χ at the single point p; GRH bounds sums over n at fixed χ). The cited "misses by
  p^{1−o(1)}" is CONDITIONAL_ES Prop 9.1 for its own count S(p); for R it holds by the same argument (should say "analogue").
* EH/BFI-for-τ row: correct. These control Σ_q max_a |Σ_{N≤x, N≡a(q)} τ(N) − main| — sums over N in progressions; (★)
  needs the divisor distribution of the *single* integer N = 4Cp+1 in the class −1 mod 4C, a set of density 1/x in the
  (q, N) box; a per-q error ≥ 1 summed over ≍ p values of q dwarfs the polylog line main term. ✓
* Selberg–Linnik / Hooley R* row: correct; I re-derived N_c(p) = c^{−1}Σ_h e(h/c)Σ_{x | cp+1} e(hx/c) (orthogonality) and
  checked numerically (Prop 6.1). Swapping the order (x ↦ c ≡ −p̄ (mod x), c | x+1) produces Kloosterman fractions
  e(h p̄/x), but still divisor-restricted (c | x + 1): consistent with the row's "exact missing piece".
* Kuznetsov/θ row: correct (θ appears only after summing over p, (D)32).
* HL row: correct that HL is single-N with power main term; the clause "i.e. a Brauer–Manin-type correction" is the
  dictionary of D3 and should be softened.
* Omitted: bilinear forms with Kloosterman fractions (Duke–Friedlander–Iwaniec 1997, Bettin–Chandee; both in sources/).
  At fixed p the pair condition is u | p + B, B | p + u, 4 | p+u+B, i.e. a bilinear Kloosterman-fraction problem in (u, B);
  DFI saves a power of UV over the trivial bound, but each dyadic box has main term ≍ 1 against trivial size ≍ p^{2/3} in
  the balanced box (Lemma 5.1), so it fails for the same B3 reason. Worth a row since the tool is the most natural fixed-p
  one (D5).

### Lemma 5.1 — **SOUND**
Re-derived (Riemann sum in (log u/log p, log B/log p), O(1/u) per u). Numerically (`scripts/review_r277_misc.py`):
(Σ − main)/log p ∈ [−0.048, +0.009] for p = 10⁶, 10⁷, 10⁸ on the full triangle, the box [0.2,0.4]×[0.1,0.5] and the small
balanced box [0.3,0.35]², i.e. error O(log p) with a small constant. Pair/divisor counts in the balanced box ✓.

### Lemma 5.2 — **SOUND** (proof correct and two lines); the "Consequence" has a small false instance (D7)
Re-derived: χ^k = 1 ⟺ χ|_{G^k} = 1, so F is G^k-periodic; F(a) = F(ag) ≤ 1_a(ag) = 0 for g ∈ G^k∖{1}. ✓
But exp(ℤ/q)^× = 2 for q ∈ {8, 24}: the admissible pairs (1,2), (2,1), (1,6), (6,1), (2,3), (3,2) (own enumeration) have
genus indicator = point indicator, so "the genus part supports no positive per-pair minorant" is false for them (they give
R ≥ 2 for p ≡ 5 (8), 17 (24), 19 (24)). Sharper true statement: a minorant F ≤ 1_a with F(a) > 0 forces the Fourier support
to *generate* Ĝ (F is constant on cosets of the annihilator of the generated subgroup) — stronger than "orders up to λ(q)".
Also: per-pair minorants are a narrow class (a sieve lower bound need not be pairwise); the document says "per pair" and the
memo flags the global version as open — fine.

### Prop 6.1 — **SOUND** (Assessment paragraph reasonable, correctly labelled)
(a) double cosets Γ_∞\SL₂/Γ_∞ with c > 0 ↔ (c, a mod c, d mod c) ✓; R = Σ_{c∈4ℕ} N_c checked via the SL₂ form (part A).
(b) checked numerically for c ∈ {4, 8, 12, 20, 24}: value 1.000000. (c) S γ S^{−1} = (d, −c; −b, a) checked on a sample.
The Assessment "θ never enters at fixed p" is a statement about the natural expansions, not a theorem; labelled Assessment. ✓

### Bright–Loughran ↔ order-2 dictionary (Assessment) — **GAP / overclaimed in AGENT_REPORT (D3)**
Checked sources/bright-loughran-1908.02526.pdf: Thm 1.6 Br U_n/Br ℚ ≅ ℤ/2 generated by (−u₁/u₃, −u₂/u₃) ✓; Thm 1.2: every
natural solution has ∏_{p|n}(−u₁/u₃, −u₂/u₃)_p = −1; Thm 1.8: the BM set is NON-empty for every n (squares included);
the square obstruction (Cor 1.4) is to strong approximation / prescribed-divisibility solutions only.
The dictionary "BM-corrected heuristic = exactly M_gen-type main term" does not follow: BL impose ONE ℤ/2 condition per
solution (for n = p: one Legendre symbol mod p, Cor 1.3), whereas M_gen's pair weight is the conjunction of 1 + ω_odd(uB)
independent quadratic conditions with weight s(q) = 4·2^{ω_odd(uB)}; a Peyre/BM-corrected density multiplies by
(1 ± 1) for one class, not by s(q). Every actual hit satisfies both conditions, but whether BL's single symbol is a product of the genus characters
of Prop 2.2(a) on the c = 1 family was not computed (by the author or by me); M_gen is a genus-theory object, not the
BM correction.

## Numbered defects

**No FATAL defects.** Every PROVED statement (Lemma 1.1, Lemma 2.1, Prop 2.2, Lemma 5.1, Lemma 5.2, Prop 6.1) and the
CONDITIONAL Prop 4.1 survived re-derivation and from-scratch checks. The defects are about what the results mean.

**D1 (MAJOR) — §0 bullet 2, §2 "Consequence", AGENT_REPORT SHARP 1: "the obstruction disappears" overstates.** The square
obstruction is moved into (L), not removed (any split with M(m²) = 0 forces X(m²) = 0; what is new is that M_gen is
explicit). The real obstruction — Poisson-scale pointwise concentration (CONDITIONAL_ES Prop 3.1(2)) — is untouched: the
genus part removes only ≈ 24–27 % of the excess variance, (U) fails at all 8 known failures < 4·10⁵ (X = −M_gen there) and
at 446 non-square n ≤ 30001. Also, CONDITIONAL_ES Prop 3.1 is about the Type-I slice S(p), not R; the R-analogue must be
stated. *Repair:* in §0/§2/report say "removes the square obstruction from the X-bound (T1 moves into the explicit term
M_gen); (U) remains a Poisson-scale lower-tail statement, false at the known failures, so only meaningful for p > p₀";
add "the analogue for R of CONDITIONAL_ES Prop 3.1(3)".

**D2 (MAJOR) — §0 last bullet / §4 "Answer to goal (1)" / report: "GRH does reach the order-2 half".** Prop 4.1 gives
M_gen(p) ≥ (1−o(1)) log log p, but (L) is only useful with g(p) ≥ |X(p)| ≍ log p (sd(R − M_gen) ≈ 9.4 at 10⁶, my run).
GRH reaches positivity of M_gen, not (L) at the needed strength. *Repair:* "GRH gives M_gen(p) ≫ log log p, which is below
the empirical size ≈ log p of |X(p)|; (L) at the required polylog strength is open (Spark 2)". Also note Prop 4.1 is
only non-trivial for p ≡ 1 (8) (p ≡ 5 (8) has the hit (1,2)).

**D3 (MAJOR for the report, MINOR in the document) — Bright–Loughran dictionary.** "A BM-corrected counting heuristic for
(★) is therefore exactly 'M_gen-type main term'" (AGENT_REPORT SHARP 1) is unsupported: BL's Br U_n/Br ℚ = ℤ/2 gives ONE
ℤ/2 condition per solution (Thm 1.2, Cor 1.3) and no BM obstruction to existence for any n (Thm 1.8); M_gen imposes
1 + ω_odd(uB) independent quadratic conditions per pair with weight s(q). *Repair:* "Assessment: both are order-2
phenomena; M_gen is a genus-theory refinement; the exact relation (is BL's symbol a product of the genus characters on the
c = 1 family?) is open (Spark 4)". Same softening for "i.e. a Brauer–Manin-type correction" in the §4.2 HL row.

**D4 (MAJOR for the headline, EVIDENCE level) — §0, §3 "non-circular, bounded-modulus local main term", failure table,
report SHARP 2: "577, 409 are the two most endangered primes".** For p < Q = 720720 "p mod Q" IS p, and every pair with
q | Q is then counted exactly (term = 1[p ≡ a mod q], the hit itself). Own measurement (`scripts/review_r277_mq_exact.py`):
for primes p ≡ 1 (4) in (1000, 3000), 55.6 % of M_Q's mass and 50.3 % of the hits come from pairs with q | Q; at 409 and 577
that exact part is 0 because those primes have no hits. The same Q also pushes tiny primes (13, 17, …: all pairs exact)
to M_Q ≥ 2, which is why the global ranking has 409/577 on top. This is the R_sm caveat the author applies to the larger Q
and to M_loc,30 but not to Q = 720720. What survives (my runs, `scripts/review_r277_stats.py`, `/tmp` reruns with smaller
Q): within the window [p/2, 2p], rank of 577 is 1/65 for Q = 720720, 5040, 720 and 2/65 for Q = 240 (Q < p:
non-circular); 409 drops from 2/47 to 8/47 for Q ∈ {720, 240}. And M_gen alone (no circularity) ranks failures well inside
windows: 5569 4/466, 9601 8/763, 83449 37/5438, 409 6/47. At 10⁶ (p > Q) M_Q still lowers the dispersion 1.52 → 1.26.
*Repair:* drop "non-circular" for p < Q; state the exact-share figure; replace the global ranking by within-window ranks
(or Q < p^{1/2}); credit M_gen's within-window ranks.

**D5 (MINOR) — §4.2 table omits DFI/Bettin–Chandee bilinear Kloosterman fractions**, the most natural fixed-p tool (pair
condition u | p+B, B | p+u). *Repair:* add a row: "power saving over the trivial box bound ≍ p^{2/3} vs box main term ≍ 1
(Lemma 5.1) — fails for B3".

**D6 (MINOR) — §3 last bullet / §4.2 / report: "sd(R − M_loc) ≈ 1.3·√(2M)".** The table's own numbers give
√(var/(2M)) = √0.99 ≈ 1.0 for M_loc,30 and √1.01 for large-Q M_Q at 10⁶; 1.3 = √1.66 is against the *different* baseline
2(M_loc − R_sm). My run at 10⁶: 1.23 (M_gen), 1.12 (M_Q, Q = 720720); absolute sd 9.4 / 8.6 ≈ 0.6–0.7·log p. *Repair:*
state which main term and baseline (e.g. "sd ≈ 1.1–1.25·√(2M) for M_Q/M_gen, ≈ 0.65 log p"). Also Conj 4.2's "data fit"
is at fixed Y = 30/100, not Y → ∞.

**D7 (MINOR) — Lemma 5.2 "Consequence": "the genus part (k = 2) supports no positive per-pair minorant"** is false for
q ∈ {8, 24} (pairs (1,2), (2,1), (1,6), (6,1), (2,3), (3,2), where (ℤ/q)^× has exponent 2). *Repair:* "for every pair with
uB ∉ {2, 6}"; optionally strengthen to "the Fourier support must generate Ĝ".

**D8 (MINOR) — Prop 2.2(a) "a function of the Legendre symbols … and of n mod 8 only".** M_gen(n) also depends on n through
the pair range 𝒫(n) (size). *Repair:* "for fixed range 𝒫, …" or "a function of |n|, n mod 8 and the Legendre symbols".

## Summary table

| claim | verdict |
|---|---|
| Lemma 1.1 (three forms, R even) | SOUND (brute-force, primes < 300) |
| Lemma 2.1 (genus split) | SOUND (exact ℚ check with brute-force real characters, odd n < 1600) |
| Prop 2.2 (a)–(d), T1 in M_gen | SOUND (D8 wording) |
| §2 "obstruction disappears" | SOUND-AFTER-REPAIRS (D1: relocated into (L); Poisson-scale (U) untouched) |
| BL ↔ order-2 dictionary (Assessment) | GAP (D3: overclaimed "exactly") |
| Prop 4.1 (GRH ⟹ M_gen ≥ (1−o(1)) log log p) | SOUND; its use overclaimed (D2) |
| Conjecture 4.2 | SOUND (calibration only, correctly labelled) |
| §4.2 table | SOUND-AFTER-REPAIRS (D5 omission; GRH row cites S(p)-analogue) |
| Lemma 5.1 | SOUND |
| Lemma 5.2 | SOUND; consequence D7 |
| Prop 6.1 | SOUND |
| §3/§4 numerics | figures reproduced exactly; interpretation SOUND-AFTER-REPAIRS (D4, D6) |
| Labels | PROVED/CONDITIONAL/CONJECTURE correct; headline overclaims D1–D4 |
