# R245 — hostile review #1 of O238 Synthesis VI (SYNTHESIS_SPARKS6.md + BRAINSTORM/s6_*.md)

Reviewer: R245 (side-agent/review-synthesis-six). Base: merge of side-agent/synthesis-six at a472a48b.
From-scratch scripts: `scripts/review_r245_cert.py`, `scripts/review_r245_small.py` (no s6_*/z8/ec_cover code imported;
only the JSON parameters are read).

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| Thm 1.1 (ES for all 4^s + 105), Lemma 1.0, 1.0′ — the mathematics | SOUND (independently re-verified) |
| Thm 1.1 — exposition / labels | SOUND-AFTER-REPAIRS (minor) |

## 1. Headline Thm 1.1 — independent verification

**(a) ET classes, rebuilt from parameters.** `review_r245_cert.py` rebuilds each of the 13 classes from `params` only:
* `II2` = ET Prop 1.9 Type II family 2 ("−4a²d mod f, 4ad | f + 1"; checked against sources/elsholtz-tao-1107.1010.pdf §10:
  sextuple (a, ce − a, (f+1)/(4ad), d, (n+4a²d)/f, f), π^II = (abd, acdn, bcdn)). For all 9 II2 classes: f = M, 4ad | f + 1,
  r ≡ −4a²d (mod f); the sextuple satisfies ET (2.13)–(2.20) identically in n; the rebuilt (x, y, z) equals the JSON
  polynomials; 4/n = 1/x + 1/y + 1/z holds in ℚ(n).
* `D` (divisor) classes M = p ∈ {11, 41, 13, 19}, r = 0: (x, y, z) = (n/p)(X, Y, Z) with 4/p = 1/X + 1/Y + 1/Z checked
  exactly ((3, 34, 1122), (11, 154, 6314), (4, 18, 468), (5, 96, 9120)).
* Integer-valuedness: for every polynomial, g(t) = f(r + Mt) is checked integer at t = 0..deg g (which is equivalent to
  integer-valuedness on the whole class). Positivity: all coefficients ≥ 0 and not all zero, so positive for every n ≥ 1
  (stronger than the doc's "n ≥ 4⁴").
* Periodicity: all M odd, ord_M(4) ∈ {5, 6, 9, 10, 15, 20, 30} all divide 360, so n_s mod M depends only on s mod 360
  **for every s ≥ 0** (pure periodicity, M odd).
* Coverage: uncovered s mod 360 = exactly {34, 124, 214, 304} = {s ≡ 34 (mod 90)}. ✔

**(b) Exponential class.** sympy: 4x − n = 151; 2(32u+33)(u²−u+1) = 151A identically; 4/n = 1/x + 1/y + 1/z in ℚ(u).
A(32 + 151t) = 1459264t³ + 928046t² + 196734t + 13902 (integer coefficients ⇒ A ∈ ℤ_{>0} on the whole class; t ≥ 0 since
u ≥ 1). ord₁₅₁(4) = 15, 4¹⁰ ≡ 32 (mod 151). s ≡ 34 (mod 45) ⇒ s − 4 ≡ 30 (mod 45) ⇒ 3 | s − 4 and (s−4)/3 ≡ 10 (mod 15) ⇒
u ≡ 32 (mod 151). Checked also by brute force for all such s < 1354. Every uncovered residue {34, 124, 214, 304} is ≡ 34 (mod 45). ✔

**(c) Exact solutions.** For every 0 ≤ s ≤ 2000 an exact positive solution 4xyz = n(xy + yz + zx) was built from my
rebuilt classes (1979 by ET classes, 22 by the exponential class) — the doc's own check went to s ≤ 1500.
Independent brute-force (no certificate) found solutions for s ≤ 8 (`review_r245_small.py`).

**(d) T1 / non-square control.** All 9 II2 residues r are non-squares mod M (exhaustive), so those classes contain no square.
The 4 divisor classes (r = 0) contain squares, which is fine (they are not polynomial-in-n-on-a-primitive-class identities that
would contradict Mordell: they are multiples of a fixed solution). Exponential class: see §2 below.

**Verdict on the mathematics of Thm 1.1: SOUND.** I could not find any gap: the proof is a finite, fully explicit certificate
plus one cubic identity, and both halves re-verify from scratch.

## 2. Thm 1.1 — T1 for the exponential class, labels, framing, novelty

**T1 (exp class).** The doc's argument is correct and in fact *rigorous*, not just a sanity check: the exp-class solution is
CAP_DOWN Lemma 1.1 at m = 151 ≡ 3 (mod 4) with K = x = 64(u³+1), d = K/(32(u+1)) = 2(u²−u+1) | K (so every prime of d
divides K), A = (K + d)/151; gcd(K, n) | 4K − n = 151 and 151 ∤ d on the class (2·993 ≢ 0 mod 151), so gcd(K, n) = 1.
CAP_DOWN §3 "T1 for Lemma 1.1" (Jacobi argument, re-read: correct) then shows 256u³ + 105 is never an odd square for
u ≡ 32 (mod 151). Numerically confirmed for t < 10⁶ (`review_r245_t1.py`). For the actual members it is even more trivial:
4^s + 105 = a² ⟺ (a − 2^s)(a + 2^s) = 105 ⟹ 2^{s+1} ∈ {104, 32, 16, 8} ⟹ s ∈ {2, 3, 4} (none ≡ 34 mod 45).

**Mordell-hardness.** Correct for s ≥ 2 (n ≡ 1 mod 8, n ≡ (2^s)² mod 105), as SIGN_FIELDS §1.4 states (R236 repair). s = 0, 1
(106, 109) are not.

**Novelty ("first infinite family of ES, every member Mordell-hard mod 840?").** The doc does NOT literally claim "first", but the
AGENT_REPORT/verdict phrasing ("Mordell-hard-for-all-s offset") invites it, so for the record: it is **not** the first such family.
(J)22 (EXPONENT_COVERING §4) already proved ES for all 315·2^m + 1 (≡ 1 mod 2520 for m ≥ 3) and all 15015·2^m + 1 — every
member Mordell-hard — and trivially n = 11·w with w in a fixed class mod 840 is an infinite Mordell-hard family (divisor class).
What *is* new: (i) the first offset k on 4^s + k for which the ET-class search stalled (k = 105, (J)62 OPEN) is closed; (ii) the
closing ingredient is an identity that is polynomial in the algebraic parameter u = 4^{(s−4)/3}, not in n (a "moving divisor"
u + 1 | u³ + 1 of x = (n + 151)/4). Literature: a cursory web search (Jina) found nothing on ES for 4^s + 105 or for exponential
offset families; I could not do a thorough search. Note also that members with s ≤ 29 (n < 3·10¹⁷) are already covered by
the published computational verifications of ES (Salez 2014, n ≤ 10¹⁷) — irrelevant to correctness, worth one sentence.

## 3. s6_unique_forced_cap0 — SOUND-AFTER-REPAIRS (minor)

Re-derived. In the forced-window setting of CAP_POINTWISE Thm 1.1′ every prime of m is ≡ 3 (mod 4), so the 2-part of
(ℤ/m)^* is elementary (ℤ/2)^r and U = 1 ⟺ φ(q^k)/2 = q^{k−1}(q−1)/2 = 1 for every prime power ⟺ m = 3. (Outside that setting
"U = 1" would NOT imply (ℤ/m)^* = {±1}: e.g. m = 15 has (ℤ/15)^* ≅ C₂ × C₄, odd part trivial — irrelevant here because 5 ≢ 3 (4),
but the memo's "U = 1 ⟹ (ℤ/m)^* = {±1}" should cite the setting.) Converse: the memo's choice "s generating a cyclic factor of
order 2o" is imprecise for composite m (s must be a non-residue modulo EVERY prime of m). Correct choice: s ≡ −u₀ (mod m) with
u₀ ∈ U \ {1}; then K = s is forced (image (−1, …, −1) in E), s ≢ ±1, Σ_m(s) = {1, s, s⁻¹} ∌ −1, and n = 4s − m satisfies
n ≡ 1 (4), m ≡ 4 − n (8) (s odd), (q_i/n) = (n/q_i) = (s/q_i) = −1, n non-square. ✔ Also the statement is about the δ_n = 0
slice (−1 ∈ Σ_m(K), CAP_DOWN Lemma 3.1); the δ_p = ±1 families of Lemma 3.1 are not addressed — say so.

## 4. s6_divisor_pigeonhole — SOUND

* |P| > (q−1)/2 ⟹ P ∩ −P ≠ ∅ (P ⊂ (ℤ/q)^* since gcd(K, q) = 1) ⟹ −1 ∈ Σ_q(K) with |δ_s| ≤ v_s(K) ⟹ cap 0. ✔
* Cauchy–Davenport: cap 0 ⟺ ±log w₀ ∈ Σ_s Σ_{δ=−b_s}^{b_s} δ·ℓ_s, an N-fold sumset of {−ℓ, 0, ℓ} (ℓ ≠ 0) in ℤ/u, u prime ⟹ size
  ≥ min(u, 2N+1), sharp for equal images. The "zero images excluded" repair is correct and necessary (q = 7, K = 3·29^N
  fails for every N: re-checked). Random test (3000 cases, u prime ≤ 31): 0 violations.
* Numerics reproduced exactly from scratch (`review_r245_pigeon.py 200000`): 8 977 primes, criterion 4 870, cap 0 6 149,
  0 cases criterion ∧ ¬cap 0.
* ±-weighted Davenport constant D_{±1}(ℤ/n) = ⌊log₂ n⌋ + 1 (Adhikari–Chen–Friedlander–Konyagin–Pappalardi 2006) — matches my
  recollection of the statement; source not accessed. "Ω(K) ≳ q/4 for structure-free arguments" is an informal reading of the
  worst case; fine as labelled (the PROVED part is the sharpness example).
