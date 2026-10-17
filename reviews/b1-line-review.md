# R270 — hostile review of O259 (B1_LINE.md, the b = 1 line)

Reviewer: side-agent/review-b1-line. Scope: B1_LINE.md, BRAINSTORM/z29_*.md, scripts/z29_*, logs/z29_*, sources/lit2026f López
excerpts, AGENT_REPORT_O259. All numerical checks below use FROM-SCRATCH code `scripts/review_r270_*` (author scripts not reused).

## Summary verdicts
(filled in as the review proceeds)

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
