# R271 — hostile review of O264 (HARD_PAIR.md, side-agent/hard-pair)

**Repairs applied** (author quiet after final commit cf54ce91): D1–D5 applied directly in HARD_PAIR.md, each marked
'(R271 repair)'. All defects were MINOR; no claim or label changed.

Reviewer branch side-agent/review-hard-pair. Merged side-agent/hard-pair at review start. From-scratch scripts:
`scripts/review_r271_*.{c,py}` (no z34_* code reused). Astra text read only at d7300f8 via `git show`.

## Summary verdicts
| claim | verdict |
|---|---|
| Thm 1.2 (a)–(e) (one equation qs = pc + 1; c_q; N₁ = #{q : c_q ∣ h}; integral-on-arrival ⟺ Type A with square c) | SOUND |
| Cor 1.3 (i)–(iv), converse false | SOUND (minor wording) |
| §1 Check numbers (75 658 / 53 716 / 21 942 (29 %) / 22 627 / 314 / failures 193, 2521, 66529) | SOUND — reproduced exactly |
| "Astra source" matches Astra's definition at d7300f8 | SOUND (attribution MINOR, see D1) |
| §2.1–2.3 raw scores and fixture table | SOUND — raw N₁, f_II, m₀, e₀ reproduced on 11 291 primes; fixture raws incl. S, L_I reproduced |
| §2.2 Spearman table, variance shares, residual correlations | SOUND — reproduced to 2 decimals with own code |
| §2.5 smooth-cell 7–11× | SOUND (EVIDENCE; post-hoc caveat D4) |
| §2.4 "Astra's 193 certificate is literally N₁(193) = 0" | SOUND (one-line justification missing, D5) |
| §2.4 2521 scope statements | SOUND |
| Labels (PROVED / EVIDENCE / Goal 3 Assessment) | SOUND |

No FATAL, no MAJOR. Five MINOR defects (D1–D5).

## Goal 1 — Theorem 1.2 / Corollary 1.3

**Re-derivation.** (a) c/(sh) + 1/(psh) + 1/(ph) = (pc + 1 + s)/(psh) = s(q + 1)/(psh) = 4/p. ✓ gcd(c, s) | qs − pc = 1. ✓
(c) Type A cp + a + 1 = 4acd ⟺ (4cd − 1)a = cp + 1, i.e. a generalized source (q, c, s) = (4cd − 1, c, a) with c | cd = h. ✓
Converse via gcd(c, s) = 1. ✓ (d) c ≡ −p⁻¹ (mod q), 1 ≤ c ≤ h < q ⟹ c = c_q. ✓ gcd(q, p) = 1 is automatic from qs − pc = 1.
(e) q | pm² + 1 ⟺ m² ≡ c_q; for composite q the "square unit" condition is (−p/ℓ) = 1 for every prime ℓ | q (c_q and −p
are in the same square class since c_q ≡ −p·p⁻²). Genuine lifts by CRT since gcd(q, h) = 1 (4h ≡ 1 mod q). ✓ The repaired
integrality statement (m² | h, not merely c_q = m²) is correct; 193, q = 79, m = 3, s = 22: c_q = 9, h = 20, ✓ non-integral.
Split slices exist for every p: for prime q ≡ 3 (4), (−p/q) = −(p/q) = −(q/p) (QR, p ≡ 1 (4)). ✓
Cor 1.3(ii): m = 1 ⟹ c_q = 1 | h ⟺ q | p + 1, and any odd prime ℓ ≡ 3 (4) dividing p + 1 is such a q. ✓ (iv): ET Type II
4abcd = a + b + pc with b = 1 is exactly Type A; ET's Type I/II dichotomy for prime p is standard. ✓

**Scan bound (author's "4cd − 1 ≤ p + 4d ≤ (3p+3)/2").** Correct but terse. My own derivation: c(4ad − p) = a + 1 and
4ad − p ≡ 3 (mod 4), so 4ad − p ≥ 3; a = 1 is impossible (c(4d − p) = 2 has no solution with p ≡ 1 (4)); hence
q = (cp + 1)/a ≤ p + (p + 1)/a ≤ (3p + 1)/2, and also c ≤ (p + 7)/12 (the author's m² bound for the source scan). ✓

**From-scratch check** (`scripts/review_r271_dict.c`, `review_r271_dict 100000 2`, ~1 min): Type A enumerated by a
(d is unique per a), independently a slice scan over *all* q ≡ 3 (4) ≤ 2p (composites included) with c_q by extended
Euclid, independently an integral-Astra-source scan q = 4m²H − 1 | pm² + 1, and split/non-split by Euler's criterion on
every prime factor of q. Result: 4783 primes, 75 658 Type A, 53 716 split, 21 942 non-split (0.2900), 22 627 square c,
failures 193, 2521, 66529, **314** primes with Type A but no integral source (first 73, 313, 337, 409, 577, …), 0 mismatches
between the three scans, c = c_q always, c ≤ (p+7)/12 always, Cor 1.3(ii) holds at all three failures. Extending the slice
scan to q ≤ 4p for p ≤ 5000 finds nothing new. All of §1's numbers reproduced exactly.

**Astra definition check.** Astra d7300f8 SQUARE_REMOVAL_STRUCTURAL §1: "q ≡ 3 mod 4, qs = pm²+1, h = (q+1)/4, N = pm²,
A = sh", integral source (A, NA, Nh) at N, composite q allowed, genuineness gcd(A, m) = 1 ⟸ gcd(h, m) = 1 (and ⟺, since
gcd(s, m) = 1). Same as HARD_PAIR's definition (dividing the N-solution by m² gives the stated rational point). ✓

## Goal 2 — statistics (spot-checks)

**Raw scores.** `scripts/review_r271_scores.c` (own brute force: all (a, b, d) with 4abd − p ≤ a + b, c = (a + b)/(4abd − p);
e₀ by brute force over x in e/H = 1/x + 1/y) on all 11 291 primes p ≡ 1 (4) in [4·10⁴, 3.1·10⁵]: N₁, f_II (gcd(a, c) = 1),
m₀, e₀ agree with the author's `z34_scores.c` output on every prime (0 mismatches). `scripts/review_r271_fixtures.py`
reproduces every fixture raw (N₁, f_II, m₀, e₀, L_I) of §2.3, and `scripts/review_r271_S.py` reproduces S for all nine Astra
fixtures (0, 0, 6, 4, 2, 0, 10, 4, 8) and for 66529 (12), plus the factorisations 194, 2522, 66530 of Cor 1.3(ii).

**Correlations.** `scripts/review_r271_stats.py` (own mid-rank percentile in the 1001 nearest primes, own Spearman, own
cell/block residualisation) on the (verified) raw data ≤ 10⁶, p ∈ [5·10⁴, 10⁶], n = 36 626: the whole Spearman table of §2.2,
the variance shares 27/30/47/79/38/36 %, and the residual correlations N₁–f_II 0.72, f_II–S 0.49, N₁–S 0.35, m₀–e₀ −0.09
are reproduced exactly. Smooth cell (my controls: all non-smooth primes in the same p-range, u already size-normalised;
range [5·10⁴, 10⁶] instead of the author's [2·10⁴, 10⁶]): 11-smooth n = 266, joint top-5 % N₁&S ×9.4, N₁&m₀ ×11.0, m₀&e₀
×8.6; 13-smooth n = 440, ×7.8, ×9.3, ×8.3. Consistent with the stated 7–11×. (Not checked: the "1.6–2.3× of cell marginals"
sentence and the −0.20 inside p ≡ 1 (24).)

## §2.4 Astra fixture statements

* POSITIVE_ES_RESEARCH_RESET §3.2 (d7300f8): normalised Type II data 4abcd = nc + a + b, a ≤ b, gcd(a, b, c) = 1,
  gcd(abd, n) = 1; "Exact test 4: … no primitive Type-II target with a = 1, even with c and d unrestricted", tuples (2,5,1,5),
  (2,13,1,2). With a = 1 the normalisation is automatic: gcd(1, b, c) = 1; and p ∤ b, p ∤ d for any Type A solution
  (in HARD_PAIR's letters: p | a gives 0 ≡ a + 1 (mod p), impossible; p | d gives a ≡ −1 (mod p), impossible since
  a ≤ (p + 1)/3). So Astra's statement is exactly N₁(193) = 0. ✓ My brute force gives the same two a ≤ b tuples
  (and Astra's three tuples at 97). ✓
* TWIST_HEIGHT_COMPRESSION §3.2: A = 631…635 = (p + k)/4, k = 3…19, "even allowing every divisor of (pA)² fails"; this is
  the standard criterion for an ES solution containing A, so "Astra excludes every ES solution containing A" is a correct
  reading, and Astra explicitly disclaims anything beyond those anchors. ✓ TWIST_FLOOR_CERTIFICATE_GATEWAY §6.2: e = 3
  (H = 1891 = 31·61) fully sterile, exit at S = 15. e = 7, 11 not tested there. ✓

## Defects

**D1 (MINOR, attribution/scope; HARD_PAIR §0 (I1), Thm 1.2(e), §1 table row 4).** Astra itself (d7300f8
SQUARE_REMOVAL_OPERATIONS §3.3 "Second repair") already notes that sources with m² | h give direct division with a
"primitive a = 1, c = m²" target, and labels them *relaxed* (not genuine) sources. So the integral-on-arrival half of
Thm 1.2(e) (= Type A with square c) is Astra's observation; HARD_PAIR's new content is the general c, the slice residue
c_q, and the N₁ count. Moreover for m > 1 an integral-on-arrival source is never genuine (gcd(m, h) = m; cf.
ASTRA_BRIDGE Lemma 1.3 Remark). *Repair:* cite SQUARE_REMOVAL_OPERATIONS §3.3 in (I1)/Thm 1.2(e) and add "(for m > 1
these are Astra's relaxed, non-genuine sources)" to (e) and to the table row.

**D2 (MINOR, §1 Check, scan bound).** "4cd − 1 ≤ p + 4d ≤ (3p + 3)/2" is correct but its second step uses d ≤ (p + 3)/8,
which needs a ≥ 2, i.e. that a = 1 is impossible; not stated. *Repair:* "(a = 1 is impossible: c(4d − p) = 2 has no
solution for p ≡ 1 (4); hence q = (cp + 1)/a ≤ p + (p + 1)/a ≤ (3p + 1)/2)".

**D3 (MINOR, §2.1 f_II bullet).** The script counts Type II solutions with gcd(a, c) = 1 only (z34_scores.c header);
the document omits this normalisation, and it matters (66529: 36 raw solutions, 20 counted). Astra's normalisation
(gcd(a, b, c) = 1, gcd(abd, p) = 1) gives the same counts at all seven fixtures checked (97, 193, 2521, 3361, 66529,
5209, 233689). *Repair:* add "with gcd(a, c) = 1" to the f_II bullet.

**D4 (MINOR, §2.5 / verdict (i)).** The smooth-(p − 1) cell was chosen after observing that the fixtures have smooth p − 1,
so the 7–11× is a post-hoc association (the label EVIDENCE and the "hypothesis" wording are fine). *Repair:* one clause
"(post hoc: the cell was chosen because the fixtures lie in it)".

**D5 (MINOR, §2.4 first bullet).** "ET a = 1 is Type A (by the a ↔ b symmetry)" should also note that Astra's
normalisation gcd(a, b, c) = 1, gcd(abd, n) = 1 is automatic at a = 1 (argument above); otherwise "literally" is not
yet justified. *Repair:* add that sentence.
