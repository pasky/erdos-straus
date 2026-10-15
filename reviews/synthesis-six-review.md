# R245 — hostile review #1 of O238 Synthesis VI (SYNTHESIS_SPARKS6.md + BRAINSTORM/s6_*.md)

Repairs applied (R245, author quiet at review end): SYNTHESIS_SPARKS6.md §0 I2, Thm 1.1(a), §1.1 scope, §1.2, §2 table, §3.1, §3.3; memos s6_exp_classes_105, s6_mixed_points_cuberoots, s6_numerator_windows, s6_witness_onesided, s6_unique_forced_cap0, s6_window_independence; BRAINSTORM/README rows; AGENT_REPORT_O238 — all marked "(R245 repair)". Defects 1, 2, 3, 4, 5, 6, 7, 8 (qualifier), 9 (wording), 10 repaired textually; no mathematical change to Thm 1.1.

Reviewer: R245 (side-agent/review-synthesis-six). Base: merge of side-agent/synthesis-six at a472a48b.
From-scratch scripts: `scripts/review_r245_cert.py`, `scripts/review_r245_small.py` (no s6_*/z8/ec_cover code imported;
only the JSON parameters are read).

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| Thm 1.1 (ES for all 4^s + 105), Lemma 1.0, 1.0′ — the mathematics | **SOUND** (independently re-verified from scratch, s ≤ 2000) |
| Thm 1.1 — exposition (s ≥ 64, n ≥ 4⁴, "Mordell-hard for every s", attribution of the 13-class covering) | SOUND-AFTER-REPAIRS (minor) |
| §1.2 / §3.1 / s6_mixed_points_cuberoots: "mixed points were a menu artefact", "sterility is menu-relative", "violated hypothesis of Thm 1.4" | **GAP** (overclaim + internal contradiction; no sterile point on Λ₁₀₅ was ever known; μ* is in an ET class) |
| T1 for the exp class | SOUND (rigorous via CAP_DOWN §3; "new kind of T1" overclaimed) |
| Novelty | not the first all-Mordell-hard infinite family ((J)22: 315·2^m + 1); new as stated in §2 below |
| s6_unique_forced_cap0 | SOUND-AFTER-REPAIRS (minor) |
| s6_divisor_pigeonhole | SOUND |
| s6_numerator_windows | **GAP** (odd ν: K odd impossible; with the correct 2-adic forcing the odd-ν T1 claim is FALSE — ν = 3, 7, 9, 25 counterexamples; 4 \| ν part SOUND) |
| s6_witness_onesided (EVIDENCE) | SOUND-AFTER-REPAIRS (minor; numerics reproduced) |
| s6_ydual_windows | SOUND-AFTER-REPAIRS (minor) |
| s6_window_independence (heuristic) | SOUND (heuristic test consistent) |
| s6_exp_classes_primes | SOUND (Assessment) |

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

## 5. s6_numerator_windows — GAP (odd-ν half of the "window-shape T1" theorem is about the wrong condition; refuted under the correct one)

* ν-version of Lemma 1.1: SOUND (same algebra; needs gcd(m, n) = 1 so that gcd(K, n) = 1). The K-odd repair and the
  counterexample ν = 4, n = 5, m = 67, K = 18 are correct (re-checked: 2^{c₂}3^{c₃} ≡ 49 (mod 67) has no solution with
  c₂ ≤ 2, and ord₆₇(3) = 22).
* **Parity defect.** For odd ν and odd n, m = νK − n is odd ⟺ K is EVEN. So after the K-odd repair the mechanism has **no
  windows at all for odd ν** (at any n, square or not): "works for all ν" (memo §Idea, README row, SYNTHESIS §2 table) is false
  for odd ν, and the odd-ν part of the T1 theorem is vacuously true.
* **The meaningful odd-ν mechanism** is the 2-adic one of CAP_DOWN Thm 1.2: K = 2^t K′, every q_i | m is ≡ 3 (4) with
  (K′/q_i) = −1; then Q² ≡ −K′ with Q ∈ ⟨odd primes of K′⟩, d = 2^t Q² ≡ −K, c₂ = t ≤ 2t, and Lemma 1.1 applies. At n = a² this
  condition reads (ν/q_i)(2/q_i)^t = −1, NOT (ν/q_i) = −1, and the memo's reciprocity computation changes for t = 1
  (m ≡ 1 mod 4, factor (2/m) enters). **Counterexamples** (`review_r245_numwin2.py`, solutions built and verified exactly,
  den z odd, prime to n, rad | y): ν = 3: a = 5, K = 34, m = 77 = 7·11; ν = 7: a = 5, K = 34, m = 213 = 3·71, giving
  7/25 = 1/34 + 1/5666100 + 17⁴/333300; ν = 9: a = 5, K = 26, m = 209 = 11·19; ν = 25: a = 7, K = 10, m = 201 = 3·67. Counts
  (a < 200, m ≤ 400): ν = 3: 60/66 squares, 7: 37/85, 9: 19/66, 25: 44/79 have a valid forced window; ν = 4, 8, 12: 0.
* 4 | ν part: SOUND, and survives the 2-adic correction (8 | νK ⟹ m ≡ 7 (8), (2/m) = 1, so (K′/m) = (K/m)). My own count
  with K odd agrees (0 for ν = 4, 8, 12, …, 24).
* Author's numerics (`s6_numerator_windows.py`) allow even K with the condition (K/q_i) = −1, i.e. exactly the invalid condition;
  the "most squares for ν ∈ {5, 13, 17, 21}" counts are therefore counts of non-mechanisms. (My K-odd count: 0 for every odd ν.)
* Label: "PROVED (only-if)" is also reversed — what is proved is "ν ∈ {4 | ν, ν ≡ 3 (4), □} ⟹ T1" (the *if* direction).
**Repair.** Restrict the theorem to 4 | ν (PROVED); delete "strictly more T1-rigid than the problem" (refuted: ν = 3, 7, 9, 25
have valid forced windows at odd squares); for odd ν state the 2-adic forcing condition (K′/q_i) = −1 and record the
counterexamples; fix the README/§2 rows.

## 6. s6_witness_onesided — SOUND-AFTER-REPAIRS (minor) (EVIDENCE label correct)

* Observation re-derived: at prime q ≡ 3 (4), (K/q) = (p/q) = (q/p); for (q/p) = +1, d ≡ −K is a non-residue and can be
  supplied by an odd-exponent non-residue prime of K with c_s ≤ 2b_s. Nothing forces (q/p) = −1. ✔ (279 counterexamples.)
* Numerics reproduced from scratch (`review_r245_onesided.py 3000 120`): cap 0 at 561 ((q/p) = −1) and 279 ((q/p) = +1, 53
  with K odd) — identical. Pair totals differ slightly: I count 1 635 / 1 530 pairs, the memo 1 655 / 1 531 (rates 34.3 % / 18.2 %
  instead of 33.9 % / 18.2 %; immaterial, but recheck the memo's denominators).
* MINOR: "(q/p) = −1 forces firing at some cap" is only true under Thm 1.1 (ii) (q ≡ 4 − p mod 8, K odd) or CAP_DOWN Thm 1.2 (E)
  / Addendum; in the excluded case (p ≡ 5 (8), q ≡ 3 (8), v₂(K) odd, ord_q(2)/2 > v₂(K)) a (q/p) = −1 window can be dead at every
  cap (CAP_DOWN: n = 5, q = 67). Add the qualifier. Same qualifier needed in s6_ydual_windows (b) ("forced for every p").

## 7. s6_ydual_windows — SOUND-AFTER-REPAIRS (minor)

(a) re-derived from CAP_INTERPOLATION Prop 5.1 (re-read): D ∈ 𝒟_e(M) ⟹ rad D | A ⟹ D ∈ ⟨primes of A⟩ (monoid = subgroup in a
finite group) and p ≡ −4D ⟹ −p/4 ∈ ⟨primes of A⟩. Example M = 7, A = 2: −p/4 ∉ {1, 2, 4} ⟺ p ≡ 1, 2, 4 (mod 7) ✔. The
"converse fails" remark is right (odd exponents above 2σ excluded). (b): needs the 2-adic qualifier of §6. The "phase
boundary = who owns the mute set" is a dictionary/Assessment, fine as labelled; "PROVED dictionary" is acceptable since the
two PROVED pieces are (a) and the Legendre identity in (b).

## 8. s6_window_independence — SOUND (label "PROVED (trivial) + Assessment" correct)

gcd(K_m, K_m′) | (m − m′)/4 ✔ (K_m − K_m′ = (m − m′)/4, both m ≡ −p (4)). Heuristic test (`review_r245_indep.py 200000 63`,
from scratch): per-window cap-0 rates at small m are much higher than the memo's 34 %/18 % (m = 3: 0.88, 7: 0.76, 11: 0.67,
…, 63: 0.22); the independence prediction for #{p < 2·10⁵ with no cap-0 window ≤ 63} is 0.2, observed 0 — consistent, as
claimed. MINOR: the memo quotes the 34 %/18 % (q < 120) rates next to the "≤ 63" fact; the consistency check needs the
small-window rates (much larger), cite those. The sentence "no pigeonhole over windows exists because … almost coprime" is
still phrased as a fact in the Consequence paragraph; prefix "heuristically".

## 9. s6_mixed_points_cuberoots / "sterility is menu-relative" vs EXPONENT_COVERING Thm 1.4 — GAP (framing; overclaim)

* **No sterile point was ever exhibited on Λ₁₀₅.** SIGN_FIELDS §1.4 ((J)62, re-read): "whether some mixed point is sterile …
  is open. No mixed point found so far is sterile", and **μ* itself lies in the ET class II2 (2, 23, 919)**. (J)62's
  obstruction was a computational *stall* (uncovered Haar measure 8.5·10⁻⁸, greedy out of candidates), not sterility.
  Hence: "(J)62's 'mixed points' were an artefact of the fixed-modulus class menu" (§3.1), "(J)62's 'mixed points' are sterile
  only for menus of polynomial-in-n ET identities" (AGENT_REPORT), and the memo's "(c) the absence of a fixed-modulus class at
  μ* is a statement about the menu" are not supported — the last is factually wrong (μ* is in a fixed-modulus ET class).
  Whether ET + divisor classes alone can cover 4^s + 105 is still OPEN after this work (by Thm 1.4 it is equivalent to
  Λ₁₀₅ ∩ S′ = ∅, unknown).
* **Which hypothesis of Thm 1.4 is "violated".** Thm 1.4 is a statement about the menu "ET + divisor classes"; its proof is
  family- and menu-agnostic for clopen classes (EXPONENT_COVERING line 80). The exp class is the clopen set s ≡ 34 (mod 45) in
  exponent space, so Thm 1.4's argument applies verbatim to the enlarged menu (ET + divisor + exponential classes): nothing is
  violated, the menu is enlarged. The document is internally inconsistent: §0 (I2) and §3.1 say the violated hypothesis is
  "classes with fixed moduli"; §1.2, the memo s6_exp_classes_105 and the self-review say (correctly) the classes ARE congruence
  classes and the difference is that the identity is not polynomial in n.
* "Sterility is menu-relative": true, but **by definition** (S′ := complement of the menu's union); the 105 theorem does not
  illustrate a sterile point becoming non-sterile (none is known), it illustrates a covering that is cheaper with a richer menu.
  Keep as Assessment only after rewording.
* T1 remark "a new kind of T1 respect, global, not local": the global Lemma-1.1 T1 is CAP_DOWN §3 ((J)66), not new. Also on the
  family itself T1 is local anyway: (J)62 certified Λ₁₀₅ ∩ Sq^× = ∅, and 4^s + 105 is a square only for s = 2, 3, 4.
* Weil-reciprocity / FF root-product analogy: unverifiable analogy, fine as Assessment; it cites an unmerged branch
  (side-agent/ff-odd-absence) — cite a merged document or mark as such.
**Repair.** Replace "artefact of the fixed-modulus class menu" / "sterile only for polynomial menus" / "violated hypothesis = fixed
moduli" by: "(J)62's ET search stalled near the mixed points (no sterile point known); adding one non-ET clopen class with a
non-polynomial identity closes the covering. Thm 1.4 applies verbatim to the enlarged menu; whether the ET menu alone suffices
remains open." Delete clause (c) about "absence of a fixed-modulus class at μ*".

## 10. s6_exp_classes_primes — SOUND (Assessment, negative). No defects beyond the cross-references above.

## Numbered defects

1. **MAJOR — s6_numerator_windows (memo; SYNTHESIS §2 row; README row; AGENT_REPORT).** For odd ν, odd n, m = νK − n odd forces
   K even, so the K-odd mechanism is empty and "works for every ν/n" is false; the odd-ν "window-shape T1" is about the invalid
   condition (K/q_i) = −1. Under the correct 2-adic forcing ((K′/q_i) = −1, K′ = odd part) forced windows exist at odd squares
   for ν = 3, 7, 9, 25 (explicit, verified solutions in §5), refuting "strictly more T1-rigid than the problem". Label
   "only-if" is the wrong direction. *Repair:* §5.
2. **MAJOR — mixed-point / sterility framing (SYNTHESIS §0 I2, §1.2 last sentences, §3.1; s6_mixed_points_cuberoots (c) and
   Assessment; s6_exp_classes_105 "Barrier screen"; AGENT_REPORT SHARP paragraph; README rows).** No sterile point on Λ₁₀₅ is
   known ((J)62: μ* ∈ II2 (2, 23, 919)); "artefact", "sterile only for polynomial menus" and "violated hypothesis = fixed moduli"
   are unsupported and mutually inconsistent. *Repair:* §9 wording; state that ET-alone coverability of 105 remains OPEN.
3. **MINOR — Thm 1.1(a).** "(for s ≥ 64)" and "positivity (n ≥ 4⁴)" are unnecessary: moduli odd ⟹ pure periodicity for all
   s ≥ 0; all coefficients ≥ 0 ⟹ positive for n ≥ 1. Say "for all s ≥ 0".
4. **MINOR — attribution.** AGENT_REPORT: "(J)62's 13-class ET covering at L = 360 leaves exactly s ≡ 34 (mod 90)": (J)62
   (SIGN_FIELDS §1.4) reports a general search leaving s ≡ 124 (mod 360); the 13-class covering with residual {34, 124, 214, 304}
   is O238's (built with (J)62's z8 code). Reword.
5. **MINOR — "Mordell-hard for every s"** (§0 I2, AGENT_REPORT): s ≥ 2 (106, 109 are not).
6. **MINOR — T1 novelty** (s6_mixed_points_cuberoots Barrier screen): "new kind of T1 respect" — it is CAP_DOWN §3 (J)66; and the
   members of 4^s + 105 are non-squares for s ≥ 5 by (a − 2^s)(a + 2^s) = 105.
7. **MINOR — s6_unique_forced_cap0:** choose s ≡ −u₀ (u₀ ∈ U \ {1}) instead of "s generating a cyclic factor"; state the
   setting (all primes of m ≡ 3 mod 4) for "U = 1 ⟹ (ℤ/m)^* = {±1}"; state the δ_n = 0 slice.
8. **MINOR — s6_witness_onesided / s6_ydual_windows (b):** "(q/p) = −1 forces firing at some cap" needs Thm 1.1 (ii) or
   CAP_DOWN Thm 1.2 (E)/Addendum. Pair totals 1 655/1 531 vs my 1 635/1 530.
9. **MINOR — s6_window_independence:** cite the small-window rates (m = 3: 0.88 … 63: 0.22) for the "≤ 63" consistency check;
   "heuristically" in the Consequence sentence.
10. **MINOR — novelty sentence missing.** Add: not the first infinite all-Mordell-hard family ((J)22: 315·2^m + 1, 15015·2^m + 1);
   members with s ≤ 29 are below published computational verification bounds.
