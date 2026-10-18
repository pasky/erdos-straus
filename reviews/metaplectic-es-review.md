# R280 — hostile review of O269 (METAPLECTIC_ES.md, BRAINSTORM/z39_*.md, AGENT_REPORT_O269)

Reviewer: R280 side agent (branch side-agent/review-metaplectic). Merged side-agent/metaplectic-es at the start
(README conflict resolved keeping main's rows and adding only the z39 section). **ES is not solved here.**
From-scratch scripts: `scripts/review_r280_*.py` (none of the author's `z39_*` code reused).

## Summary verdicts
(filled in claim by claim below; table at the end of the review)

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
operation (Σ_N χ(N)qᴺ is not modular), on a sum truncated at an n-dependent level. After that renormalisation, "𝔒 ≈ 0
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

