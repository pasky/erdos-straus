# R270 — hostile review of O259 (B1_LINE.md, the b = 1 line)

Reviewer: side-agent/review-b1-line. Scope: B1_LINE.md, BRAINSTORM/z29_*.md, scripts/z29_*, logs/z29_*, sources/lit2026f López
excerpts, AGENT_REPORT_O259. All numerical checks below use FROM-SCRATCH code `scripts/review_r270_*` (author scripts not reused).

**Repairs applied (author parked, no commits after 9a3ae31f):** B1_LINE.md M1, M2, m1–m6 inserted inline, each marked
"(R270 repair)"; one-line repair notes appended to BRAINSTORM/z29_nb_tail_model.md (M2) and z29_lopez_typeA.md (m1).
m7 (resource disclosure) and m8 (optional López footnote) are left to the author/parent.

## Summary verdicts
No FATAL defect. Every computational headline was reproduced exactly with independent code.
| claim | verdict |
|---|---|
| Lemma 1.1 (mutual-shift form, completeness bound min ≤ 1 + √(p + 1)) | SOUND (C1, C5) |
| Census b = 1: no failure in (66529, 10¹¹] | SOUND — independently rerun in full to 10¹¹ with a different algorithm (C2) |
| π(10¹⁰; 4, 1), π(10¹¹; 4, 1) | SOUND — verified via π(10¹⁰), π(10¹¹) (C2; closes the "from memory" caveat) |
| (★): exactly the 14 known failures ≤ 10¹⁰ | SOUND — rerun in full (C4) |
| Smooth-(p − 1) list to 10¹⁵ (216 882 primes, no extra failure) | SOUND — list regenerated exactly; decisions spot-checked (all Y = 11 + 1 500 random) (C8) |
| Lemma 1.2 / Cor 1.3 / Prop 1.4 (pair genus law, trivial classes) | SOUND; Prop 1.4's b = 1 half is López's (m1) (C6) |
| Prop 4.1 (freezing under M_σ | p − 1) | SOUND (minor proof gap m4) (C7) |
| Thm 4.2 (CONDITIONAL on Dickson: least shift unbounded) | SOUND, correctly labelled; numerically illustrated (C7) |
| "Unconditionally, Prop 4.1 explains the census records" | OVERCLAIM — the records are outside Prop 4.1's hypothesis (M1) |
| Lemma 3.1 (incidence form, swap count, main terms) and 1.67 → 1.85 ratios | SOUND as math/EVIDENCE; "Haar main term" mislabelled (m2) (C9) |
| §3 NB heuristic, prediction, Conjecture 3.5 | SOUND-AFTER-REPAIRS: labels right, arithmetic reproduced; premise "D = O(1)" contradicted by data (M2) (C10) |
| §5 forcing negative (χ₋₄(p + 4d) = +1) | SOUND (wording slip m6) (C11) |
| López attribution (2206.10319, 2404.01508) | SOUND-AFTER-REPAIRS — all quotes verbatim-verified; one missing attribution (m1) (C3) |
| Resource note | not verifiable; no disclosure in the documents (m7) (C12) |

## Claim-by-claim

### C1. Lemma 1.1 (mutual-shift form) — SOUND
Re-derived. b = 1 ⟺ a(4cd − 1) = cn + 1. With w = 4cd − 1: 4d(cn + 1) ≡ n + 4d (mod w), gcd(4d, w) = 1, so w | cn + 1 ⟺
w | n + 4d; put g = (n + 4d)/w. Then n + g + 4d = g(w + 1) = 4cd·g, i.e. (g·4d)·c = n + g + 4d: st | n + s + t with
{s, t} = {g, 4d} and quotient c. Converse: n odd ⇒ not both even (else n + s + t odd, st even), so exactly one is ≡ 0 (4)
and it is D = 4d; w := (n + s + t)/g − 1 = (n + D)/g ∈ ℤ, and w | n + D ⇒ w | cn + 1 gives a ∈ ℤ. Odd coordinate
T ≡ −n ≡ 3 (4) (from S | n + T, 4 | S). Coprimality for n = p prime: a common prime divides n, so it is p and s, t ≥ p,
then st ≥ p·max(s,t) > p + s + t (p ≥ 5) — correct (the "s, t < p" wording in the proof is just a paraphrase).
Completeness bound: st ≤ n + s + t ⟺ (s − 1)(t − 1) ≤ n + 1 ⇒ min(s, t) ≤ 1 + √(n + 1). ✓. And st | n + s + t ⟺
(t | n + s and s | (n + s)/t + 1). ✓. Consequences used by the census: s ≡ 1, 2 (4) never occur as a coordinate; s = 1
never occurs either (needs 4 | t | p + 1 ≡ 2 (4)). My engine does NOT use any of these mod-4 consequences (it tests
4 | st and st | p + s + t literally), so agreement below is also a check of them.

### C2. Census, b = 1 line (§2.1) — SOUND (≤ 10¹⁰ independently reproduced; 10¹¹ see below)
Engine `scripts/review_r270_engine.c` (different algorithm from z29_census.c: no factor tables at all).
Phase A: sieve the segment by all residue classes p ≡ −(s + t) (mod st) over the 196 918 useful pairs with st ≤ 3·10⁵,
4 | st. Phase B (only for primes not hit in A): exhaustive over s ≤ 1 + √(p + 1); for each s enumerate the two
arithmetic progressions t ≡ −p (mod s), t ≤ √(p + s) and u ≡ −1 (mod s), u ≤ √(p + s) (t = (p + s)/u), testing
4 | st, st | p + s + t literally. (Complete: any divisor t of p + s has t or (p + s)/t ≤ √(p + s); st | p + s + t forces
t ≡ −p and u ≡ −1 (mod s).)
Results (`logs/review_r270_eng_a.txt`, `_b.txt`): ≤ 5·10⁹: 117 474 981 primes p ≡ 1 (4), failures exactly 193, 2521, 66529;
(5·10⁹, 10¹⁰]: 110 048 294 primes, 0 failures. Sum 227 523 275 = author's figure; ≤ 10⁸ subtotal 2 880 504 = author's;
≤ 10⁶ gives 39 175 + 39 322 (≡ 3 (4)) + 1 = 78 498 = π(10⁶). Runtime 2 × 2.6 min.
**Full rerun to 10¹¹** (`logs/review_r270_eng_1e10.txt`, `_c.txt`, `_d.txt`; 2 cores, ≈ 30 min): failures exactly
{193, 2521, 66529}; primes p ≡ 1 (4): 227 523 275 (≤ 10¹⁰), 933 583 091 ((10¹⁰, 5.5·10¹⁰]), 897 913 914 ((5.5·10¹⁰, 10¹¹]) —
identical to the author's per-range figures, total 2 059 020 280. My sieve also counts p ≡ 3 (4): 227 529 235 ≤ 10¹⁰ and
2 059 034 532 ≤ 10¹¹, so π(10¹⁰) = 455 052 511 and π(10¹¹) = 4 118 054 813 (both the classical values) — this closes the
author's "from memory, not re-checked" caveat for π(10¹¹; 4, 1). Only 238 (≤ 10¹⁰) / 1 641 ((10¹⁰, 10¹¹]) primes needed
the exhaustive Phase B; all were decided positively by explicit pairs except the three.
**Verdict: SOUND.** The headline "no b = 1 failure in (66529, 10¹¹]" is independently confirmed with a different algorithm.

## Defects

### C3. Prior-art attribution to López — SOUND-AFTER-REPAIRS (one missing attribution)
Fetched the arXiv HTML myself (Jina reader, 2026-10-17; saved as `sources/lit2026f/r270-lopez-2404.01508v3-html.md`,
`…2206.10319v4-html.md`). Every quote in `Lopez-2022.md`, `Lopez-2024.md`, `Lopez-2024-TypeB-Thm7.md` is verbatim present:
2206.10319v4 Theorem (a) (p ≡ −4d mod 4dn − 1), (c) (w | k + 1 + t, w ≡ −1 mod 3 + 4t), §3 "up to the value p=4369, only
two prime numbers … 193 and 2521"; 2404.01508v3 Def. 4 / Thm 4 (Type B), Thm 7, Conjecture 1, "among the first 9000 natural
numbers … 193 and 2521", "66529 is another case", "23929 does not have Type B", verification to 104729, "Type A … a=1 or b=1".
Identification re-derived: a Type A solution (du, dv, duv) of a prime p has 4duv = p(u + v + 1); p | d is impossible
(it would give 4 = (u + v + 1)/(d′uv) ≤ 3), so p | v say, v = pv′, and 4duv′ = pv′ + u + 1 is the b = 1 equation with
(a, c, d) = (u, v′, d). ✓ (Note the divisor form is already Thm (a) of 2206.10319, not only Thm 7 of 2404.01508.)
**Missing:** 2404.01508v3 §2 states "In the previous article it was shown that any prime number p such that
p ≢ 1 (mod 24) always has a solution of Type A" (t = 0 case of Thm (c)). That is exactly the b = 1 half of Prop 1.4, which
B1_LINE labels "folklore-level" without citing López (defect m1). Also López 2404 notes 83449 "lacks Type B solutions" and
has "only two Type A solutions" — a data point the author could cite; my engine confirms it (C5).

### C4. (★) census "exactly the 14 known failures ≤ 10¹⁰" — SOUND
Same engine with `R270_LINE=2`: (★) ⟺ ∃ x, y ≥ 1 with 4xy | p + x + y (PARITY_AUDIT's R(p) with N = 4C), complete with
min ≤ (1 + √(4p + 1))/4 (from (4x − 1)(4y − 1) ≤ 4p + 1). `logs/review_r270_star_{a,b}.txt`: failures exactly 409, 577,
5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281 (all ≤ 10⁸), none in
(10⁸, 10¹⁰] (227 523 275 primes). Consistent with López: 23929 and 83449 lack Type B.

### C5. Lemma 1.1 / Lemma 3.1 bijection vs raw ES brute force — SOUND
`review_r270_checks.py brute`: for every prime p ≡ 1 (4) < 400, all solutions of 4/p = 1/x + 1/y + 1/z by raw rational
search, filtered for López's shape (du, dv, duv) in any order, coincide as a set with the solutions built from the pairs
of Lemma 1.1, and their number equals #{(c, d) : 4cd − 1 | p + 4d} (Lemma 3.1). 0 mismatches.
Side remark: López 2404 says 83449 "has only two Type A solutions"; it has N₁ = 4 distinct ones (pairs (11, 52), (11, 1284),
(68, 123), (79, 212); all four triples verified in exact rationals). López presumably counts differently; harmless here.

### C6. Lemma 1.2 (pair genus law), Cor 1.3, Prop 1.4 — SOUND (Prop 1.4 needs a López citation, m1)
Re-proved: S | p + T, T | p + S, gcd = 1; (p/S′) = (−T/S′); (p/T) = −(2/T)^k (S′/T); reciprocity with (T − 1)/2 odd
gives (S′/T) = (−T/S′), so (p/S′T) = −(2/T)^k; k ≥ 3 ⇒ T ≡ −p (8) ⇒ (2/T) = (2/p); k = 2 trivial. (★), k = 1: re-derived
the four cases (p mod 8, x′ mod 4) → y ≡ 5, 1, 1, 5 (mod 8) and (p/x′y) = −1, −1, +1, +1. ✓. Both-odd / both-even (★)
pairs are impossible (parity of p + x + y vs 4xy). From-scratch check (`logs/review_r270_genus.txt`, p < 2·10⁴): 12 717 b = 1
pairs, 7 857 (★) pairs, 2 147 overlaps — exactly the author's counts — 0 violations of T ≡ 3 (4), gcd = 1, (ST/p) = −1,
(S′T/p) = −(2/p)^k, (xy/p) = −1, (x′y/p) = −(2/p)^k; free pairs occur only in (p mod 8, k mod 2) = (5, odd) (2 260 b = 1,
3 399 (★)); 181 has the (★) pair (3, 8). Prop 1.4: 12 | p + 7, 24 | p + 11, 8 | p + 3 ✓, and no b = 1 failure off 1 (24)
/ no (★) failure at 5 (8) for p < 2·10⁴. The b = 1 half is López 2022 (C3, m1).

### C7. Prop 4.1 (freezing) and Thm 4.2 (Dickson ⟹ least shift unbounded) — SOUND (proofs); the "explains the records" reading is an OVERCLAIM (M2)
Definition: e_ℓ = ⌊log_ℓ(σ + 1)⌋ + 1 gives v_ℓ(M_σ) > v_ℓ(m) for all m ≤ σ + 1 ✓; my values M₃ = 72, M₅ = 1800,
M₇ = 176 400, M₁₁ = 64 033 200 match. Re-proof: (1 + s) | p − 1 ⇒ (1 + s) | p + s; v_ℓ((p − 1)/(1 + s)) ≥ 1 for ℓ ≤ σ + 1
⇒ primes of Q_s exceed σ + 1; for ℓ | s, v_ℓ((p − 1)/(1 + s)) = v_ℓ(p − 1) > v_ℓ(s) ⇒ Q_s ≡ 1 (s). tu = p + s ≡ 1 (s)
(s | p − 1) ⇒ u ≡ −1 ⟺ t ≡ −1 (mod s) ✓. (a): needs st | M_σ, which uses gcd(s, t) = 1 (Lemma 1.1, p prime) — fine but
unstated; the proof covers 3 ≤ s < t only, s = 1 is vacuous (no b = 1 pair has a coordinate 1, as 4 ∤ p + 1) — trivial
gap, state it. (b): g ≡ −1 (mod s), g | 1 + s ⇒ g = s − 1 | s + 1 ⇒ s = 3, g = 2, t ∈ {2, 2Q₃}, 4 ∤ 3t ✓.
Thm 4.2: forms 1 + M_σk and 1 + (M_σ/(1 + s))k (3 ≤ s ≤ σ) are distinct, have positive leading coefficients, and equal 1
at k = 0, hence are admissible ✓. Under Dickson, M_σ | p − 1 (so p ≡ 1 (4)), every Q_s prime, shifts 1, 2 carry no pair
(C1), shifts 3..σ dead by (b) ⇒ least shift > σ ✓. Correctly labelled CONDITIONAL.
Numerics (from scratch, `logs/review_r270_freeze.txt`): all primes ≡ 1 (mod M₇) and (mod M₁₁) below 2·10⁹: 16 719 + 47
shift-≤σ pairs, predicted set = actual set, Q_s ≡ 1 (s) with all primes > σ + 1, no pair in all 2 776 + 24 cases with Q_s prime,
no surviving pair with st | M_σ; 0 discrepancies (counts identical to the author's). Dickson examples
(`logs/review_r270_dickson.txt`): 2 250 primes p = 1 + 1800k (k < 3·10⁶) with Q₃, Q₄, Q₅ all prime; the first 60 have least
shift ≥ 7 > σ = 5, as Thm 4.2 predicts. Amusingly, 2521 = 1 + 72·35 with Q₃ = 631 prime is itself a σ = 3 Dickson prime.
**But** the §4 bullet "Unconditionally, Prop 4.1 explains the census records" is not supported: of the six record primes
I re-verified (`logs/review_r270_records.txt`; least shifts 95, 119, 111, 104, 215, 116 all reproduced, witnesses exact),
four (1 683 049, 277 977 001, 6 098 002 681, 58 441 300 009) have 3 ∥ p − 1, so not even M₃ = 72 | p − 1 and Prop 4.1 applies
to NO shift; 22 010 483 881 has M₃ | p − 1 but M₄ = M₅ = 1800 ∤ p − 1 (5 ∥ p − 1), so Prop 4.1 freezes only shift 3 of the 214
empty shifts; only 345 601 (M₅ | p − 1) is in scope, and only for s ≤ 5. The QR claim (every prime < 41 is a QR mod
22 010 483 881; 41 is not) is correct. See M2.

### C8. §2.2 smooth-(p − 1) census to 10¹⁵ — SOUND (list fully regenerated; decisions spot-checked)
`review_r270_checks.py smooth` (pure Python: recursive enumeration of all 1 596 961 m = 4·(19-smooth) with m + 1 ≤ 10¹⁵,
sympy primality): Y = 11, 13, 17, 19 give 14 173 / 41 146 / 99 549 / 216 882 primes, of which 12 781 / 36 517 / 87 216 /
187 500 are ≡ 1 (8) — all eight numbers identical to the author's. Decisions by sympy factorisation of p + s (independent
of both C engines), for ALL 14 173 primes with 11-smooth p − 1 plus 1 500 random ones with 19-smooth p − 1: unresolved
exactly 193, 2521, 66529 (complete decisions, since 2000 > 1 + √(p + 1) for these), all other witnesses verified in exact
rationals, max least shift 95 at 345 601 (`logs/review_r270_smooth.txt`). The statement "every other smooth prime has
s ≤ 95" for the remaining ~2·10⁵ primes rests on the author's run only (not re-run in full by me).

### C9. Lemma 3.1 (incidence form, main term, swap count) and the ratio data — SOUND as mathematics; "Haar main term" mislabelled (m2)
Re-derived: w | cp + 1 ⟺ w | p + 4d (gcd(4d, w) = 1); g ≥ 3 ⇒ 8d ≤ p + 3; a = (cp + 1)/(4cd − 1) < p ⇒ p ∤ x = ad,
so x is identified and the triple determines (a, c, d) ✓ (also checked by brute force, C5). Main-term integral: Σ_d (1/(4d))
log(p/(12d)) over d ≲ p/12 = (log p)²/8 + O(log p) ✓; my numerics M₁ = 13.27, 19.79, 27.64 at 10⁵, 10⁶, 10⁷ reproduce the
author's. Swap involution (u, B) ↔ (B, u) on R(p): fixed point u = B ⇒ u(4uC − 2) = p, impossible ✓; distinct triples ✓.
So "ε ∈ {0, 1}" is really ε = 0 (m3).
**But M₁ (weights 1/w) is not the Haar/random-prime expectation.** For a random prime p, P(w | p + 4d) = 1/φ(w), not 1/w.
`logs/review_r270_mainterm.txt`: M_φ(10⁶) := Σ 1/φ(4cd − 1) = 24.71, against M₁ = 19.79, and the empirical mean of N₁ over
all 4 329 primes p ≡ 1 (4) in 10⁶ ± 6·10⁴ is 27.68 (class p ≡ 1 (24): 22.27). The author's sentence "the class p ≡ 1 (24)
runs ≈ 13 % above the unconditioned M₁: 22.3 against 19.8" is numerically right but misleading: the hard class is ≈ 20 %
BELOW the true all-class mean; it only looks "above" because M₁ underestimates the mean by ≈ the average of w/φ(w) over
odd w (≈ 1.3 asymptotically). The ratio claim "twice the trials" is unaffected (both lines use odd moduli of the same
shape, so the φ-correction is common to both), and the NB model uses empirical means, so nothing downstream breaks.
Ratio data (`logs/review_r270_disp.txt`, from-scratch counts, p ≡ 1 (24), 3 000 consecutive primes from 10⁶, 10⁸, 10¹⁰, 600
from 10¹²): N₁/L² = 0.119, 0.125, 0.130, 0.135 (author 0.117, 0.124, 0.131, 0.135); N_{c1}/L² = 0.072–0.074; ratio N₁/N_{c1}
= 1.66, 1.73, 1.77, 1.84 (author 1.67, 1.69, 1.78, 1.85) ✓. Class means at 10¹² (`logs/review_r270_classes.txt`, 300 primes
each): p ≡ 1 mod 24 / M₅ / M₇ / M₁₁: N₁/L² = 0.135 / 0.127 / 0.117 / 0.108, N_{c1}/L² = 0.073 / 0.070 / 0.065 / 0.061 —
exactly the §3.2 figures (−20 % and −16 %) ✓. Label EVIDENCE is appropriate.

### C10. §3.3–3.6 NB model, prediction, Conjecture 3.5 — labels SOUND; heuristic premise "D = O(1)" GAP (M2)
NB algebra: variance μD ⇒ r = μ/(D − 1), P(0) = (1 + μ/r)^{−r} = D^{−μ/(D−1)} ✓. Back-test arithmetic checked against
`logs/z29_model.txt`: Σ predicted zeros 0.862 + 0.088 + 0.124 + 0.070 + 0.026 + 0.012 = 1.18 vs 2 observed; ≤ 2: 16.65 vs 33;
(★): 3.39 vs 7 ✓. Prediction recomputed from scratch (`scripts/review_r270_nb.py`, `logs/review_r270_nb.txt`; density
e^L/(8L) dL of primes ≡ 1 (24), justified by Prop 1.4): fixed D = 3.24, μ = 0.125L² gives 0.033 / 9.4·10⁻⁵ / 1.1·10⁻¹⁰
beyond 10⁶ / 10⁸ / 10¹¹ (author 0.037 / 1.1·10⁻⁴ / 1.4·10⁻¹⁰; quadrature-level differences), −20 % μ: 0.62 / 0.012 / 6.7·10⁻⁷ ✓.
Poisson tail checks e^{−1.7} ≈ 0.18, e^{−3.5} ≈ 0.03 ✓.
**Problem:** the dispersion is not O(1). In the author's own table D rises 1.7–2.3 (≤ 10⁶) → 2.69 (10⁸) → 3.24 (10¹⁰), and
my class-(1 mod 24) samples give D = 2.20, 2.67, 3.26, **3.62** at 10⁶, 10⁸, 10¹⁰, 10¹² — roughly D ≈ 0.78 + 0.10·log p. So
(i) D = 3.24 is not "the largest observed" once one looks at 10¹², and it is not a conservative constant for extrapolation
beyond 10¹⁰; (ii) Conjecture 3.5's stated heuristic basis "overdispersion D = O(1)" is contradicted by the data. With
D linear in L the predictions become 8·10⁻⁶ (> 10⁸), 5·10⁻¹⁰ (> 10¹¹); with additionally −20 % μ: 1.8·10⁻³ and 2.7·10⁻⁶ —
still negligible, so the CONCLUSION survives at this scale, but the asymptotic finiteness argument needs
μ·log D/(D − 1) ≥ (1 + ε)L, i.e. D/log D ≲ c·log p; if D grew like (log p)² the same NB model would predict infinitely many
failures. The premise should be stated as an explicit growth hypothesis on D, with the data. Labels (CONJECTURE,
Assessment, EVIDENCE) are otherwise correctly applied; the §3.6 wording "if anything, pessimistic … merely consistent"
is self-contradictory within two sentences but correctly retracted.

### C11. §5 forcing negative — SOUND (one wording slip, m6)
χ₋₄(p + 4d) = χ₋₄(p) = +1 trivially (p + 4d ≡ p ≡ 1 (4)); χ₋₄ is odd on (ℤ/4d)^* ✓; any w ≡ −1 (mod 4d) is ≡ 3 (4) hence
has a prime factor ≡ 3 (4) dividing p + 4d ✓. The cited O258 value χ_{−4d}(p + 4d) = (d/p) checked numerically for all
p ≡ 1 (4) < 3000, d < 300, p ∤ d: 62 923 cases, 0 failures (`review_r270_checks.py chi`). (a) duality for elementary
2-groups is standard ✓; d ∈ {1, 2, 3, 6} ⟺ (ℤ/4d)^* of exponent 2 ✓. The scope statement (total-product character data only)
is honest. Slip: in (c) for c = 1, p + 1 is even so χ₋₄(p + 1) = 0; the forced object is the odd part (p + 1)/2 ≡ 3 (4) ⟺
p ≡ 5 (8).

### C12. Resource note — cannot verify; no disclosure in the documents
Neither B1_LINE.md nor AGENT_REPORT_O259 mentions any > 2-core usage; the report only says "≈ 2 × 55 CPU-min" for 10¹¹. If a
3-core burst happened (as the brief indicates), it should be disclosed in the report (m7). Reviewer's own disclosure: all
R270 heavy runs used ≤ 2 processes under `ulimit -v 8000000` + `timeout`; one 1.5-s test run (the (★) engine to 10⁸) briefly
overlapped two background jobs.

## Defects

**FATAL:** none.

**M1 (MAJOR, interpretation) — B1_LINE §4, Reading bullet 2 ("Unconditionally, Prop 4.1 explains the census records. 22 010 483 881 …"), echoed in §2.2 last sentence and memo z29_dickson_least_shift.**
The record primes are essentially outside Prop 4.1's hypothesis: 1 683 049, 277 977 001, 6 098 002 681, 58 441 300 009 have
3 ∥ p − 1 (M₃ = 72 ∤ p − 1, Prop 4.1 applies to no shift); 22 010 483 881 satisfies only M₃ | p − 1 (freezes shift 3 of 214
empty shifts). *Repair:* replace by "The records share the qualitative feature (p − 1 divisible by many small primes, small
primes QR mod p), but satisfy M_σ | p − 1 for σ ≤ 3 at most (345 601: σ = 5), so Prop 4.1 does not literally apply to them;
it is a model mechanism (Assessment)." — consistent with the author's own 193 caveat.

**M2 (MAJOR, heuristic premise) — §3.4 ("D = 3.24 (the largest observed)") and Conjecture 3.5 ("overdispersion D = O(1)"),
memo z29_nb_tail_model.** D grows with p in the author's data and mine (2.20 → 2.67 → 3.26 → 3.62 at 10⁶ → 10¹²).
*Repair:* state D(p) ≈ 0.8 + 0.1 log p as EVIDENCE on 10⁶–10¹²; replace "D = O(1)" by the needed hypothesis
"D/log D = o((log p)·μ/(log p)²)", i.e. D ≲ c log p suffices; add the sensitivity row (D linear in log p: 8·10⁻⁶ beyond 10⁸,
5·10⁻¹⁰ beyond 10¹¹; with −20 % μ: 1.8·10⁻³, 2.7·10⁻⁶) from `logs/review_r270_nb.txt`. Conclusions unchanged.

**m1 — §0 (I1), Prop 1.4, memo z29_lopez_typeA.** López 2404.01508v3 §2: "In the previous article it was shown that any prime
number p such that p ≢ 1 (mod 24) always has a solution of Type A." Cite López for the b = 1 half of Prop 1.4 (and note the
divisor form is already Thm (a) of 2206.10319).

**m2 — §3.1 Lemma 3.1 "Haar main term" and the parenthetical "class p ≡ 1 (24) runs ≈ 13 % above the unconditioned M₁".**
For random primes the weight is 1/φ(w): M_φ(10⁶) = 24.7, empirical all-class mean 27.7, class 1 (24) 22.3. *Repair:* call M₁
"the 1/w main term"; note the prime-conditioned main term carries an extra factor ≈ avg w/φ(w) (common to both lines,
so the factor-2 comparison stands); say the hard class sits ≈ 20 % below the all-class mean.

**m3 — Lemma 3.1.** "ε ∈ {0, 1}" — the proof shows there are no fixed points, so N_{c1} = R/2 exactly. State ε = 0.

**m4 — Prop 4.1(a) proof.** It uses gcd(s, t) = 1 (to get st | M_σ) without saying so and covers only 3 ≤ s < t; add
"(gcd(s, t) = 1 by Lemma 1.1; s ∈ {1, 2} carry no pair)".

**m5 — §2.1 "(the known value, OEIS A091115 — from memory, not re-checked)".** Now verified: R270's sieve gives
π(10¹¹; 4, 1) = 2 059 020 280 and π(10¹¹; 4, 3) = 2 059 034 532, summing (+1) to π(10¹¹) = 4 118 054 813.

**m6 — §5(c) and memo z29_forced_level_characters (c).** For c = 1, p + 1 is even and χ₋₄(p + 1) = 0; say "the odd part
(p + 1)/2 is ≡ 3 (4) iff p ≡ 5 (8)".

**m7 — resources.** Disclose any > 2-core burst in AGENT_REPORT_O259 (none is mentioned).

**m8 (optional) — §0.** López 2404 states 83449 "has only two Type A solutions"; it has N₁ = 4 (pairs (11, 52), (11, 1284),
(68, 123), (79, 212), verified in exact rationals). Worth a footnote if López is quoted on solution counts.

## Scripts / logs (R270)
`scripts/review_r270_engine.c` (sieve-by-pair-congruences + exhaustive AP fallback; `R270_LINE=2` for (★); `least`, `count`
modes), `scripts/review_r270_checks.py` (brute, genus, freeze, dickson, records, randomspot, chi, smooth, mainterm, disp),
`scripts/review_r270_classes.py`, `scripts/review_r270_nb.py`; logs `logs/review_r270_*.txt`. Random spot check: 300 random
primes p ≡ 1 (4) in (10⁹, 10¹¹], all with exact-rational-verified witnesses; least s agrees with a pure-Python divisor
search on 30 of them.
