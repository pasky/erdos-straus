# R280 — hostile review of O269 (METAPLECTIC_ES.md, BRAINSTORM/z39_*.md, AGENT_REPORT_O269)

Reviewer: R280 side agent (branch side-agent/review-metaplectic). Merged side-agent/metaplectic-es at the start
(README conflict resolved keeping main's rows and adding only the z39 section). **ES is not solved here.**
From-scratch scripts: `scripts/review_r280_*.py` (none of the author's `z39_*` code reused).

## Summary verdicts
Repairs applied: none (author agent still alive and waiting; defects to be forwarded by the parent). No FATAL; MAJOR: D4 (Assessment headline), D9 (H-E screen); D6 = unconditional upgrade of Prop S(3); rest MINOR. Table at the end.

## Claim 1 — Theorem K (identity (K1), coefficient form (K2), "no cusp form at any level")

**Verdict: SOUND (identity and (K2)); "no cusp form" SOUND as an arithmetic statement and as a modular statement
about the odd part; modular reading correctly labelled Assessment. Two MINOR presentation defects (D1, D2).**

*Re-derivation.* Kronecker: for |Q| < |x|, |y| < 1,
Σ_{r,s≥0} x^r y^s Q^{rs} − Σ_{r,s≥1} x^{−r} y^{−s} Q^{rs} = (Q;Q)²θ(xy)/(θ(x)θ(y)), θ(x) = (x;Q)(Q/x;Q).
With x = y = X = q^{t−1}, Q = q^t (|Q| < |X| < 1 for 0 < |q| < 1; θ(X²) is entire in X² so X² outside the annulus
is harmless): t(r+1)(s+1) − (r+1) − (s+1) = trs + (t−1)(r+s) + t − 2, so q^{t−2}·(positive quadrant, r, s ≥ 1) = P_t,
the r = 0 or s = 0 terms give 2/(1−X) − 1 = (1+X)/(1−X); and t(ρ+1)(σ+1) − (t−1)(ρ+σ+2) + t − 2 = tρσ + ρ + σ, so
q^{t−2}·(negative quadrant) = Q_t. (K2): tuv − u − v = n ⟺ (tu−1)(tv−1) = tn+1 =: N; every divisor d ≡ −1 (t) of N
has N/d ≡ −1 (t) (N ≡ 1); u ≥ 2 ⟺ d ≥ 2t − 1; the only d ≡ −1 (t) below 2t − 1 is t − 1, so the boundary is
{d = t − 1} ∪ {N/d = t − 1}, i.e. **β_t(n) = 2·1[(t−1) | (n+1)] − 1[n = t − 2]** (since tn + 1 ≡ n + 1 mod t − 1; the
author's min(d, N/d) = t − 1 form is equivalent because no divisor ≡ −1 (t) is < t − 1). Character formulas:
1[d ≡ 1] ± 1[d ≡ −1] = φ(t)⁻¹ Σ_χ (1 ± χ(−1)) χ(d). All correct.

*From-scratch numerics* (`scripts/review_r280_thmK.py 10 3000`, 13 s):
(a) (K1) cleared of denominators, as an **exact integer power-series identity** to q^3000, t = 2..10 — 0 mismatches
(negative control `NEGCTRL=1`, sign of Q_t flipped: ~300 mismatches per t);
(b) Kronecker's identity itself at Q = 0.25e^{0.7i} and *x ≠ y* (0.5e^{0.3i}, 0.6e^{−1.1i}): |L − R| = 1.6·10⁻¹⁵;
(c) (K2), the even/odd character formulas with characters mod t built from scratch (brute-force dual group), the
closed form of β_t, and R_t = ½E_t + ½O_t − β_t against direct (u, v) enumeration: t ≤ 10, n ≤ 3000, 0 failures;
(d) see D1: the theta quotient alone has coefficients exactly D⁻_t − D⁺_t — 0 failures.

*"No cusp form at any level."* Correct. Arithmetic form: R_t(n) is a ℚ-combination of σ_χ(tn+1), constants and
β_t (itself a divisor indicator). Modular form, odd part: by (d), q^{t−2}(Q;Q)²θ(X²)/θ(X)² = Σ_n (D⁻ − D⁺)(tn+1)qⁿ is
the progression-N ≡ 1 (t) restriction of a combination of weight-1 Eisenstein series E₁^{1,χ} (χ odd), and
restriction to a progression / q^{1/t} rescaling are slash operators by elements of GL₂⁺(ℚ), which preserve the
Eisenstein subspace; so no cuspidal component. Even part: Maass Eisenstein data (unnormalised E(z, s) vanishes at
s = ½ for the principal character, so the τ(N) data are the s-derivative/completed series, as the author says).
Assessment label is appropriate for the normalisations.

*Literature.* Kronecker's identity is classical (Kronecker 1881; Weil 1976; Zagier 1991). I could **not** access
Weil Ch. VIII or Zagier Invent. Math. 104 §3 in `sources/` to check the chapter/section numbers; the identity
itself was verified numerically for general x ≠ y (b), so nothing rests on the citation.

**D1 (MINOR) — the ±2 is attributed to the theta quotient but is an artefact of the O_t normalisation.**
Location: METAPLECTIC §1 "(it is an elementary correction present in every coefficient …)", Reading bullet 1
("the odd part … O_t(N) − 2"), z39_kronecker_levels "PROVED: its coefficient content is the odd-character divisor sum
… plus an elementary ±2 per coefficient", §7.1. Fact (check (d)): the boundary series q^{t−2}(1+X)/(1−X) has
coefficients exactly β_t(n), so
`q^{t−2}(Q;Q)²θ(X²)/θ(X)² = Σ_{n≥0} (D⁻_t − D⁺_t)(tn+1) qⁿ = −(2/φ(t)) Σ_{n≥0} Σ_{χ odd} σ_χ(tn+1) qⁿ`
**with no ±2 and no boundary term**; equivalently P_t + β-series = D⁻ = ½(D⁻ + D⁺) + ½(D⁻ − D⁺). The ±2 and the
β_t appear only because the author removes the trivial divisors 1, N from E_t and moves the u = 1 words to β_t.
*Repair:* state the clean form above as (K1′); say "the theta quotient is exactly the odd-character divisor sum on
N ≡ 1 (t)"; drop "plus an elementary ±2 per coefficient" from the memo; keep the ±2 only as a bookkeeping remark.

**D2 (MINOR) — novelty/SHARP framing.** The coefficient content of (K2) is the long-standing campaign reformulation
"level-t words ↔ divisors d ≡ −1 (mod t) of tn + 1 with d, N/d ≥ 2t − 1" (QUESTION_R Prop 1.1 / DEDEKIND §1 /
Mordell–Type II); the even/odd split is orthogonality. What Thm K adds is only the q-series packaging as a
Kronecker quotient at a torsion point (classical: Hecke; Borisov–Gunnells, see D9). *Repair:* in §7.1 and the
report's SHARP 1, say "classical identity, new only as a packaging in the campaign"; promise 1/5 as stated is fine.

## Claim 2 — Corollary K1 (T1 as exact E_t + O_t = 0 on 4 | t at squares; sizes; "where the main term lives")

**Verdict: K1.1 SOUND (but tautological, D3); K1.2 numbers SOUND (reproduced exactly at 10⁵, D5 for 10⁶);
the "Reading" (log² in weight 0, holomorphic part ≈ 0) GAP — normalisation-dependent (D4, MAJOR on an Assessment).**

*K1.1 re-derived independently (no Jacobi symbol in n needed, any m):* let 4 | t and d | tm² + 1 with d ≡ −1 (t),
d > 0. Then gcd(d, tm) = 1 and −t ≡ (m⁻¹)² (mod d), so (−t/d) = 1. But d ≡ 3 (4) gives (−1/d) = −1, and writing
t = 4s: for s odd, (s/d) = (d/s)(−1)^{(s−1)/2·(d−1)/2} = (−1/s)(−1)^{(s−1)/2} = 1; for 2 | s, d ≡ −1 (8) so (2/d) = 1 and
the same computation on the odd part gives 1. Hence (−t/d) = −1, contradiction. So D⁻_t(tm² + 1) = 0 for **every** m
(odd or even), hence R_t(m²) = β_t(m²) = 0 (β_t ≠ 0 iff t − 1 | m² + 1, impossible for t − 1 ≡ 3 (4)). Since
E_t + O_t = 2D⁻_t **identically** (definitions), "E_t + O_t = 0" is literally "D⁻_t = 0".
From scratch (`scripts/review_r280_corK1.py`): (1a) 4 | t ≤ 64, 1 ≤ m ≤ 800 (odd and even): 0 numbers t m² + 1
with a divisor ≡ −1 (t); (1b) every d ≡ −1 (t), d < 200t, 4 | t ≤ 400, has (−t/d) = −1: 0 exceptions.

*K1.2 reproduced exactly (same script, 19 s):* odd squares 317², 319², 321², 323²: 𝔈 = 127, 124, 109, 139;
𝔒 = −29, −50, −83, −81; 𝔒_{4|t} = −𝔈_{4|t} = −19, −11, −18, −16; 𝔒_{t≡3(4)} = −24, −47, −55, −43 (so the bulk of the
square deficit is indeed at t ≡ 3 (4), not at 4 | t); N₋ = 0. First 12 primes > 10⁵: means 𝔈 = 115.92,
𝔒 = 3.75, 𝔅 = 52.67 (author: "≈ 54"), R = 67.00 — matches the author's re-run.

**D3 (MINOR) — K1.1 is a relabelling, and the proof is routed unnecessarily through (A/n).** Location: METAPLECTIC
§1 Cor K1 item 1, report SHARP 2 ("T1 is an exact cancellation E_t + O_t = 0"), §7.2. E_t + O_t ≡ 2D⁻_t by
definition, so the "weight-1 term equals minus the weight-0 term" carries no information beyond D⁻_t(tm²+1) = 0 (the
classical (A)3 / Mordell obstruction; the author does say "Equivalently"). *Repair:* lead with "D⁻_t(tm² + 1) = 0
for 4 | t, all m (classical); in the even/odd language this reads E_t + O_t = 0", use the direct Jacobi argument above
(works for all m, no appeal to DEDEKIND Thm 4.5 / QUESTION_R Prop 1.4), and drop "exact cancellation" from the
SHARP headline.

**D4 (MAJOR, on an Assessment headline) — "log² main term in the weight-0 part, holomorphic part ≈ 0" depends on a
non-modular renormalisation of size ≍ n.** Location: Cor K1 "Reading", §7.2, §7.4 ("B3 is visible as main term in
weight 0, oscillation in weight 1"), report SHARP 2 and Results (1), z39_kronecker_levels barrier screen B3.
The genuinely modular per-level pieces are ½(D⁻ + D⁺) (weight-0 Eisenstein data) and ½(D⁻ − D⁺) (exactly the
Kronecker quotient, D1). Summed over the 2 ≤ t ≤ (n + 4)/4 levels these are ≈ +n/4 and ≈ −n/4 respectively (every
level has the trivial divisors 1, N ≡ +1); e.g. at n = 100003, Σ_t ½(D⁻ − D⁺) = 𝔒 − #levels = 1 − 25000. The
author's 𝔈, 𝔒 are obtained by moving the trivial divisors (±1 per level) between the two parts — a non-modular
operation (on the progression N ≡ 1 (t) the divisors 1, N contribute the constant sequence 2, generating function
2/(1 − q)), on a sum truncated at an n-dependent level. After that renormalisation, "𝔒 ≈ 0
on average, 𝔈 ≈ main term" is simply the statement that non-trivial divisors of tn + 1 are on average equally split
between the classes +1 and −1 (mod t), which is elementary equidistribution, not an automorphic fact; with another
symmetric renormalisation (e.g. interior divisors 2t − 1 ≤ d ≤ N/(2t − 1) on both sides) the same split appears for the
same elementary reason. *Repair:* state the Reading as "after removing the trivial divisors 1, N at every level (an
elementary, non-modular renormalisation of total size ≍ n, forced by the truncation t ≤ (n + 4)/4), the even part
carries the log² and the odd part averages ≈ 0 — i.e. the non-trivial divisors are equidistributed between ±1 mod t";
remove "B3 is visible as main term in weight 0, oscillation in weight 1" from §7 or attach this caveat; demote the
corresponding clause of SHARP 2 to Assessment-with-caveat.

**D5 (MINOR) — 10⁶ sizes corrected by a mean bias instead of the exact per-n correction.** Location: Cor K1 item 2
("the 10⁶ ones are corrected by the stated mean bias"; "𝔒 = −97, −35, −19, −68 before the … t = 2 correction"). The
t = 2 `elif` bias is exactly τ(2n + 1)/2 for each n (my script prints it), so the correction is trivially exact per n;
applying a mean (3.92) to per-prime and per-square values is unnecessary noise, and leaving the squares uncorrected
is inconsistent. Also "R ≈ 113 (115.9 × (6/5)² ≈ 167 …)" juxtaposes R with a scaling prediction for 𝔈 — confusing.
*Repair:* subtract τ(2n+1)/2 from 𝔒 and add it to 𝔈 per n (no rerun needed, only τ(2n+1)), and reword the scaling
sentence as "𝔈 ≈ 163 vs 115.9·(log 10⁶/log 10⁵)² ≈ 167".

## Claim 3 — Prop S (Serre–Stark supports; T1 squares = supp θ; the five-slice failure set Z is not a weight-½ support)

**Verdict: S(1), S(2) SOUND; S(3) SOUND as stated, and in fact PROVABLE UNCONDITIONALLY (D6: the SQ₅ conditional
and the period bound are unnecessary); scope wording GAP-minor (D7).**

*Serre–Stark.* The statement used (M_{1/2}(Γ₁(N)), 4 | N, is spanned by θ_{ψ,t} = Σ_{m∈ℤ} ψ(m)q^{tm²}, ψ even
primitive, 4 r(ψ)² t | N) is Serre–Stark Theorem A (LNM 627); I could not access the paper in `sources/`, but this is
the standard statement and the author uses nothing beyond it. On the class t₀·□ (t₀ squarefree) the coefficient of
t₀m² is Σ_{k|m, t₀k² ∈ F} c ψ(m/k) — periodic in m. S(1) (support ⊂ finitely many square classes, ≪ X^{1/2} points
up to X) and S(2) (θ(z) − θ(4z) = 2Σ_{m odd>0} q^{m²}, level 16; Z ∩ □ = odd squares because (A/m²) = +1 for every
A prime to m) are correct.

*Census re-done from scratch* (`scripts/review_r280_census.c`, C, enumerates all 1.3·10¹⁰ words with n ≤ 10⁸ and
all length-2 certificates b | n + 1, 43 s; checked against brute force at n ≤ 3000): **Z \ □ = {105} for n ≤ 10⁸**
(author/DEDEKIND: 10⁶); the interior-only zero set {N₋ = 0} \ □ = {5, 105} for n ≤ 10⁸; no odd square is
certified; λ(105m²) ≤ 3 (indeed with an interior certificate) for every odd 3 ≤ m ≤ 975. So the author's period
argument is correct and extends to periods M ≤ 974 — but see D6, which makes it moot.

**D6 (MAJOR-positive: label upgrade; the CONDITIONAL is unnecessary) — S(3) holds unconditionally.**
Location: METAPLECTIC §2 item 3, §7.3, z39_serre_stark_support item 3, report SHARP 3 and Labels ("PROVED for periods
≤ 96, CONDITIONAL (SQ₅) in general"). *Proof.* Let ℓ be a prime with ℓ ≡ 3 (4) and (ℓ/105) = −1 (e.g. ℓ = 11, 19, 31,
43, …; infinitely many by Dirichlet, being a union of classes mod 420). By quadratic reciprocity
(−105/ℓ) = (−1/ℓ)(ℓ/105) = +1, so 105m² ≡ −1 (mod ℓ) has solutions m ≡ ±r_ℓ (mod ℓ) (r₁₁ = 3). For any odd m in such a
class, n = 105m² has b = ℓ | n + 1, 2 ≤ ℓ ≤ (n + 1)/2, and (ℓ/n) = (ℓ/105)(ℓ/m)² = −1; n/ℓ = (n+1)/ℓ − 1/ℓ is an HJ
length-2 certificate, so λ(n) ≤ 2 and n ∉ Z. Now if supp g = Z with period M on the class 105·□: M odd is excluded by
parity (author); for M even pick ℓ ∤ M from the infinite list and, by CRT, m ≡ 1 (M), m ≡ r_ℓ (ℓ) — m is odd, a(105m²)
≠ 0, but 105m² ∉ Z. Contradiction for **every** M, no census and no SQ₅ needed. (The same argument shows Z ∪ F is not
a support for any finite F with 105 ∈ Z ∪ F.) Checked: `scripts/review_r280_propS_uncond.py` (symbol identities for
ℓ < 200, certificate for all odd m < 20000 in the classes, 6 primes ℓ: 0 failures). *Repair:* replace the
"M even ≤ 96 … census … Under SQ₅" sentences by the argument above and relabel S(3) PROVED (unconditional).
Note this also slightly *weakens* the rhetorical point "105 is not metaplectic": the obstruction is not deep — Z
misses entire residue classes of m on 105·□ for elementary reasons.

**D7 (MINOR) — scope: "holomorphic modular form" must be kept in every restatement.** Location: §2 closing
paragraph ("at weight ½, no success set can be a support"), §7.3 ("only square classes can be supports of weight-½
forms"), memo Assessment ("no weight-½ object can certify non-square failures"), §7.3 "any non-square failure (105) is
provably not metaplectic". Serre–Stark covers holomorphic forms (holomorphic at the cusps). Weight-½ *mock* theta
functions, weakly holomorphic forms (e.g. η-quotients with poles at cusps) and harmonic Maass forms of weight ½ have
supports of positive density, so "no weight-½ object" is false as written; and "105 is not metaplectic" overstates
the exact-support statement (θ_{1,105} = Σ q^{105m²} contains 105). *Repair:* add "holomorphic" (and "exact
support of Z") in each restatement; replace "provably not metaplectic" by "Z is not the exact support of any
holomorphic weight-½ form".

## Claim 4 — §3 matrix side (Bruhat cell, ν_θ ≡ −i, not a semigroup)

**Verdict: SOUND (dictionary); one MINOR imprecision (D8).**

Re-derived: γ_w = [[tu−1, n],[t, tv−1]] has det (tu−1)(tv−1) − tn = 1 and γ_w ≡ −[[1, −n],[0, 1]] (mod t), so
γ_w ∈ −Γ₁(t); T^kγT^l keeps c = t and changes a, d by multiples of t, so the condition is ⟨T⟩-bi-invariant; the
double cosets ⟨T⟩\{c = t}/⟨T⟩ are indexed by (a, d) mod t with ad ≡ 1, i.e. one Kloosterman term each; the ES words
are the b = n, a, d ≥ 2t − 1 part of the (−1, −1) cell; the +I cell contains [[1, n],[t, tn + 1]]; D⁻ − D⁺ is the
signed positive count over the two cells. ν_θ(γ) = ε_d⁻¹(c/d): for 4 | t, d ≡ −1 (t) one has (t/d) = +1 (computation in
Claim 2), ε_d = i, so ν_θ = −i. On positive γ ∈ Γ₀(4) with b odd, ad ≡ 1 (b) and bc ≡ −1 (d) give, by reciprocity,
(c/d) = (a/b) if d ≡ 1 (4) and (c/d) = −(−1/b)(a/b) if d ≡ 3 (4).
From scratch (`scripts/review_r280_matrix.py`): (a) 0 of the 4096 products for t, u, v ∈ [2, 5] is self-levelled
(confirms author), also 0 of 117 649 for [2, 8], and none lies in +Γ₁(c) either; (b) ν_θ = −i on all 168 200 ES
matrices with 4 | t ≤ 200, u, v < 60; (c) both reciprocity formulas on 20 000 random positive Γ₀(4) matrices, b odd:
0 failures; (d) the a, d ≥ 2t − 1 part of the −I cell with b = n, c = t has exactly R_t(n) elements (t < 12, n < 400),
and [[3,5],[4,7]] is the boundary word (4, 1, 2) of n = 5.

**D8 (MINOR) — §3's last sentence is not a statement.** Location: METAPLECTIC §3 "T1 = imaginary multiplier on the
−I cell is incompatible with b = □"; also "on positive elements of Γ₁(4) ν_θ = (a/b)" (needs b odd; (a/b) is
undefined as a Jacobi symbol for even b). *Repair:* replace by the precise lemma (verified in (c)): "for positive
γ ∈ Γ₀(4) with b odd and d ≡ 3 (4), (c/d) = −(−1/b)(a/b); if b = m² this is −1, whereas self-levelling with 4 | c forces
(c/d) = +1 — this is T1 at 4 | t" (the memo's item 4 says this, correctly; §3 should too), and add "b odd" to the Γ₁(4)
formula. Note also that the "not a semigroup" observation only shows the self-levelled set is not *kernel ∩ positive
cone* of a multiplier; that is what is claimed, fine.

## Claim 5 — §4 GL(3) / level sum

**Verdict: SOUND (identities); readings correctly labelled Assessment.** `scripts/review_r280_gl3.py`: (i)
Σ_{t,u,v≥2} q^{tuv−u−v} = Σ_{u,v≥2} q^{2uv−u−v}/(1 − q^{uv}) to q^3000, (ii) #{t, u, v ≥ 2 : tuv = n} = d₃ − 3d₂ + 3 − [n = 1]
(n ≤ 400), (iii) R(n) = #{(u, v) ≥ 2 : uv | n + u + v, n ≥ 2uv − u − v} (n ≤ 600): 0 mismatches each. Σ_{n≤X} d₃ ~ ½X log²X
is standard; (15/64) is (J)39 Lemma 2.1 (R204-refitted; not re-checked here). One remark for §5 consistency: §4's
GL(3) object is Eisenstein (d₃ = 1∗1∗1, abelian), so it does not touch H-D's "GL₃ or higher automorphic forms" —
worth saying explicitly, since (J)39 lists GL(3) *cuspidal* contributions as not excluded.

## Claim 6 — §5 red team 2 Thm 2.2 hypothesis analysis

**Verdict: GAP (MINOR-to-MAJOR presentational, D9).** The finite-level part is right in substance: for a fixed finite
set of levels the witness is a divisor ≡ −1 (t) of the fixed linear polynomials tp + 1, so Thm 2.2(iii)'s proof
(bounded, correct witness procedure → POINTWISE_SIZE Thm C) applies, CONDITIONAL on H as stated. The H-D remark
(per-level content is congruence data; ν_θ takes congruence values) is a fair Assessment with the stated scope.

**D9 — the screen omits hatch H-E, which is the one Thm K actually touches; and "violates only the finiteness
hypothesis" conflates hypotheses with hatches.** Location: §5 bullets 2–3, §7.4, report Results (1). Thm 2.2(iii)
has essentially one hypothesis (Θ₀ finite, plus H for the conclusion); the meaningful screen is against the escape
hatches H-A … H-G of red team 2 §3. Thm K/Cor K1 produce exactly an *exact signed expansion of the aggregated count*,
R = 𝔈 + 𝔒 − 𝔅 with a positive main term 𝔈 — the shape that red team 2 lists as **H-E** ("Open for an exact identity
with a positive main term"). §5 should say why this instance does not open H-E: to use it one needs |𝔒 − 𝔅| < 𝔈 at a
single prime, i.e. a pointwise bound on ≍ n/4 weight-1 Eisenstein coefficients at different levels and points, and the
per-level modular pieces are of size ≍ n before the non-modular renormalisation (D4) — so the "cancellation" is
termwise-elementary and the remaining sum is the H-A/B2 object again. *Repair:* rewrite §5 as a hatch screen
(H-A: touched, quantitatively blocked as assessed; H-D: not opened in the examined constructions; **H-E: the even/odd
identity is a signed exact expansion with positive main term, but its error term is the same single-n level sum —
not opened**; H-B, H-C, H-F, H-G: not engaged), and replace "violates only the finiteness hypothesis" by "touches
only H-A (and, formally, H-E)".

## Claim 7 — §6 quartic (χ₄(A) inverted by u ↔ v)

**Verdict: SOUND (narrow no-go PROVED, numbers reproduced exactly).** AA* = tp + 1 ≡ 1 (p) ⇒ χ₄(A*) = χ₄(A)⁻¹; on k | t
(4 | k) slices (A/p) = −1 ⇒ χ₄(A) = ±i, so the swap u ↔ v exchanges i and −i: no symmetric sign of the form χ₄(A).
From scratch (`scripts/review_r280_quartic.py 20000`, own word enumeration, own i = a/b mod p): k = 4: constant 127
(value i in 60), mixed 413, empty 16; k = 8: 264 (134), 190, 102; k = 16: 242 (125), 39, 275 — **identical** to the
memo; χ₄(A*)χ₄(A) = 1 on every word. Side facts checked: 17, 241, 97, 193, 401, 433, 449 are all ≡ 1 (16) with 2 a
quartic non-residue; 131 ≡ 3 (4). (The list of numerator-8 exceptions itself is QUESTION_R §4.1's and was not
re-checked.) Note the balance count depends on the arbitrary choice i := a/b (vs −a/b); only "balanced" is
convention-free, which is all that is claimed. Scope "other quartic invariants not excluded" is correctly stated.

## Claim 8 — labels, citations, novelty

**Verdict: mostly SOUND; D10–D11 MINOR.**
* Labels: Thm K identity/(K2) PROVED ✓; modular reading Assessment ✓; Cor K1.1 PROVED ✓ (D3: tautological);
  K1.2 EVIDENCE ✓ but the Reading's headline needs D4's caveat; Prop S(3) can be upgraded to PROVED (D6); §3 PROVED
  dictionary ✓; §6 PROVED (narrow) + EVIDENCE ✓; §4/§5 Assessment ✓ (D9). No overclaim of ES anywhere ✓.
* Novelty: Kronecker's double-series identity and the fact that Kronecker quotients at torsion points are weight-1
  Eisenstein series are classical (Kronecker; Hecke; Weil 1976; Zagier 1991); the ES-specific content is the
  substitution, which the author correctly calls "classical ingredients, new to the campaign". Fine with D2.

**D10 (MINOR) — Borisov–Gunnells citation.** Location: METAPLECTIC §1 Reading ("Borisov–Gunnells, Invent. Math. 144
(2001), 'toric modular forms'"), z39_kronecker_levels Literature ("'Toric modular forms', Invent. Math. 144 (2001)
297–325"), report Sparks 1 ("weight-1/2 forms from Kronecker quotients"). Verified (Springer / arXiv math/9908138):
the Invent. Math. 144 (2001) 297–325 paper is titled **"Toric varieties and modular forms"**; its abstract: a
complete rational fan in ℝ^r with a degree function gives a holomorphic modular form **of weight r** on Γ₁(l), and
the resulting ring 𝒯(l) is Hecke-stable. "Toric modular forms and nonvanishing of L-functions" is a different paper
(J. reine angew. Math. 539 (2001), arXiv math/9910141, weight 2), and "Toric modular forms of higher weight" another
(arXiv math/0203242). *Repair:* fix the title; replace "weight-1/2 forms" in Spark 1 by "weight-r forms (r = rank;
the 2-dimensional ES pentagon fans give weight 2)" — in a document about half-integral weight "weight-1/2" reads as
weight ½, which BG forms never have.

**D11 (MINOR) — unverified section/chapter pointers.** Weil Ch. VIII, Zagier 1991 §3, Diamond–Shurman Thm 4.8.1 and
Serre–Stark Thm A could not be checked against the texts (not in `sources/`); the mathematical statements used were
re-verified independently (numerically for Kronecker, standard for Serre–Stark and weight-1 Eisenstein series), so
nothing depends on them. *Repair:* none required; optionally mark the pointers "(not re-checked)".

## Minor remarks (no defect number)
* §0 C6 (levels with φ(t) = 2): R_t = ½(τ(N) − σ_χ(N)) − β_t holds because every divisor of N ≡ 1 (t) is a unit ≡ ±1
  (t) when φ(t) = 2 ✓; "r_K(N)" there means σ_χ(N), not the representation number (which is wσ_χ) — say so.
* 𝔅 ≈ 2τ(n + 1): exactly 𝔅 = 2·#{e | n + 1 : 1 ≤ e ≤ ⌊(n + 4)/4⌋ − 1} (t = e + 1; the n = t − 2 correction never
  occurs in range), i.e. 2τ(n + 1) minus the few large divisors n + 1, (n + 1)/2, (n + 1)/3 cut by the truncation;
  harmless.
* README conflict: on merge, main's README already had the z37 rows; I kept main's and added only the z39 section.

## Summary table

| claim | verdict | defects |
|---|---|---|
| Thm K identity (K1) | SOUND (exact series check t ≤ 10, q^3000; Kronecker at x ≠ y) | D1, D2 (minor) |
| Thm K coefficients (K2), even/odd formulas | SOUND (t ≤ 10, n ≤ 3000, characters from scratch) | D1 |
| "no cusp form at any level" | SOUND (arithmetic + modular for the odd part) | — |
| Thm K modular reading | Assessment, appropriately labelled | D1 |
| Cor K1.1 (E_t + O_t = 0, 4 \| t, squares) | SOUND, tautological (= D⁻ = 0; holds for all m) | D3 (minor) |
| Cor K1.2 sizes | SOUND (10⁵ and squares reproduced exactly) | D5 (minor) |
| Cor K1 Reading ("log² in weight 0, holomorphic ≈ 0") | GAP — normalisation-dependent | **D4 (MAJOR)** |
| Prop S(1), S(2) | SOUND | D7 (minor) |
| Prop S(3) (Z not an exact weight-½ support) | SOUND, and **unconditional** (census to 10⁸ also re-done) | **D6 (upgrade)**, D7 |
| §3 Bruhat cell / ν_θ ≡ −i / not a semigroup | SOUND | D8 (minor) |
| §4 level sum / GL(3) | SOUND identities; Assessment | — |
| §5 red team 2 screen | GAP (omits H-E) | **D9** |
| §6 quartic | SOUND (numbers reproduced exactly) | — |
| labels / citations | mostly SOUND | D10, D11 (minor) |

**No FATAL defects.** Two substantive items: D4 (the "main term in weight 0 / T1 as weight-1 vs weight-0
cancellation" headline is a renormalisation artefact plus a tautology — keep as Assessment with caveat) and D6
(Prop S(3) becomes unconditional by a two-line residue-class argument). D9 asks for an H-E line in §5.
