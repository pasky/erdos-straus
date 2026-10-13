# R197 — hostile review of MODEL_SPECIFIC.md (O197)

Reviewer: R197 (side-agent/review-model-specific). Author branch merged: side-agent/model-specific.
From-scratch scripts: `scripts/review_ms_*`. ES is not solved; nothing below changes that.

**Repairs applied** (author silent since the R-O197 repair commit acc1a387; all marked '(R197 repair …)'):
D1, D2, D3, D5, D6, D9, D10 in MODEL_SPECIFIC.md; D1, D4, D9, D10 in AGENT_REPORT_O197.md; `data/ms/tail_1e7.txt`
regenerated with the author's `ms_tail.py 1e7` so it now contains the bin table (non-bin lines byte-identical).
D7, D8 are optional presentation notes, not applied.

## Summary verdicts
**Overall: no FATAL, two MAJOR (D1 wording of the headline reading of Thm 3.1; D9 inherited 8/n novelty — PW Table 1 + Bright–Loughran Rem 1.10), eight MINOR.** Every numerical claim I
re-ran from scratch reproduced exactly.

| claim | verdict |
|---|---|
| Lemma 3.0 (five m-slices → explicit m/n solutions) | SOUND |
| Lemma 3.0′ (cell formula incl. boundary words; relative to DEDEKIND Cor 4.1) | SOUND |
| Thm 3.1 (a) S_4 = {χ = −1}, all odd n; (b) 4 \| m ≥ 8: ∅ ≠ S_m ⊊ {χ = −1}; (c) 4 ∤ m: χ = +1 members and non-members | SOUND |
| Cor 3.2, 131/241: 29 resp. 12 χ = −1 words, none in S_8 | SOUND |
| §3 "Reading" / report SHARP: "T1 is the only obstruction on the length-3 ball, as an identity" | SOUND-AFTER-REPAIRS (D1, MAJOR wording) |
| §7 (C1) reformulation of SQ₅ | SOUND-AFTER-REPAIRS (D1, D6, D8 minor) |
| Lemma 2.1 (parity; all-even ⟺ 8/n) | SOUND |
| §1 censuses (CERTIFIED), PW Table 1 agreement, 2763601, 620929 | SOUND; novelty SOUND-AFTER-REPAIRS (D5, D10) |
| attribution of the 8/n failures / B7 (header, §2, §3, §6, report) | SOUND-AFTER-REPAIRS (D9, MAJOR) |
| §4 coverings and cube shots | SOUND |
| §5 count law / luck (EVIDENCE + Assessment) | SOUND-AFTER-REPAIRS (D2, D3, D4 minor) |
| §6 B7 screen numbers | SOUND |

### Lemma 3.0 (five m-slices give m/n solutions) — **SOUND**
Re-derived by hand: (I) 1/(vd)+1/(A*vd) = t/(A*d), plus 1/(A*dn) gives (tn+1)/(A*dn) = AA*/(A*dn) = m/n;
(T) (n+u+v)/(uvcn) with n+u+v = tuv = mcuv; (U) 1/(wf)+1/(tnw)+1/(tnwf) = (tn+f+1)/(tnwf) = (n+v)/(nwf), and
n+v = u(tv−1) = mwf; (I′),(V) by u↔v. `review_ms_words.py 1500`: every slice solution of every word of every odd
n ≤ 1500, all m = 4..24, checked in exact `Fraction` arithmetic, all denominators > 0: 0 failures.
Remark: gcd(A, n) = 1 is automatic (AA* = tn + 1), so the gcd clause in the word definition is redundant (harmless).

### Lemma 3.0′ (cell formula on all words incl. boundary) — **SOUND** (relative to DEDEKIND Cor 4.1)
Re-derived the reductions: t = 1: (u−1)(v−1) = n+1, n/(u−1) = [[v−1, u−1]] (b₁b₂ − 1 = n), K(b₁) = v−1 = A*,
Σ(b_i−3) = u+v−8 ✓. u = 1, t ≥ 2: n = (t−1)v − 1, n/(t−1) = [[v, t−1]]; the r = 2 right side
n+1−n(t+v−7)−A−v equals the length-3 one n+1−n(t+v−8)−A−(n+v) identically ✓. Corners ((t,1,1), (1,2,v), (1,u,2),
(2,1,v); (2,u,1) by symmetry): RHS = 4n−2 ≡ 2 (mod 8) and (A/n) = 1 ✓. u↔v symmetry ✓ ((A/n)(A*/n) = (1/n)).
Independent numeric check (own Jacobi, not sympy): all 35 179 words of odd n ≤ 1500: 0 mismatches.
The only non-elementary input remains (D2)+(R) behind Cor 4.1 (DEDEKIND: "cited from memory, verified numerically");
the label "relative to Cor 4.1" is honest.

### Theorem 3.1 — **SOUND** (as narrowed: "determined by χ = (−A/n)")
* Cells (`review_ms_cells.py`, own enumeration over (ℤ/L)³, L = lcm(8, m)): every odd-n cell has RHS ∈ {2, 6} (asserted);
  m = 4: χ=−1 cells 240/240 in S_4, χ=+1 cells 0/80 ✓ (a). m = 8: 140/240, m = 12: 2304/6480, m = 16: 600/1920, and
  χ = +1 cells 0 for every 4 | m ≤ 24 ✓ (b). For 4 ∤ m the slice fraction is *identical* on both χ-halves for every
  m = 5..23 (0.712, 0.489, 0.563, 0.421, 0.333, 0.391, 0.339, 0.251, 0.251 for m = 5..15 match the document; also
  17: 0.267, 18: 0.183, 19: 0.242, 21: 0.187, 22: 0.167, 23: 0.203). For odd m this is automatic by CRT
  (cells mod 8m = cells mod 8 × cells mod m, χ depends on the first factor, S_m on the second).
* Example words: (4,1,2) (n=5, A=3, χ=−1) ∈ S_4, ∉ S_m for m ≥ 8 ✓ (note it IS in S_7 via A* = 7 — irrelevant, claim is for
  4 | m ≥ 8); (m,1,2) ∈ S_m with χ = −1 for 4 | m; for 4 ∤ m the t = m members with (u,v) = (2,3)/(1,2)/(1,1) have χ = +1,
  n odd ≥ 3, and the non-members (3,1,2) (m ≥ 6), (3,1,6) (m = 5) have χ = +1 — all verified for every 5 ≤ m < 2000.
* Word level, odd n ≤ 1500 (`review_ms_words.py`): 35 179 words, 23 825 χ = −1 (all in S_4), 11 354 χ = +1 (none in S_4);
  S_8: 12 026 / 0; S_12: 6 573 / 0; S_5: 14 775 / 6 752 — **all of the document's §5 word numbers reproduced exactly**.
  For every 4 | m ≤ 24, no χ = +1 word lies in S_m (as the inclusion predicts).
* Proof logic: χ = (−1/n)(A/n), n mod 4 is a cell function, so χ is a cell function mod 8; S_m a cell function mod m. ✓
  Quantifiers: (a) is for every odd n, every word; (b) properness is per m with one fixed word; (c) per m. No hidden
  uniformity issue.

### Corollary 3.2 and the 131 / 241 statement — **SOUND**
Own enumeration: n = 131: 43 words, 29 with χ = −1 (all in S_4), 0 in S_8; n = 241: 31 words, 12 with χ = −1, 0 in S_8.
(The repaired 29/12 are correct; the original 22/7 was indeed an undercount.)

### §1 censuses — **SOUND** (CERTIFIED label justified for the ranges I re-ran; 10⁸ ranges not re-run)
* Own engine `scripts/review_ms_census.c` (complete smallest-denominator search x ∈ (p/m, 3p/m], divisors of (px)²,
  128-bit + three 61-bit-modulus exact re-verification of every solution; g = gcd(mx − p, px) = 1 for prime p, proved in
  the header). Cross-checked against a naive `Fraction` counter (`review_ms_naive.py`) for m ∈ {4, 5, 8, 12},
  primes ≤ 103: 0 mismatches. Reproduces 4/131 = 32, 4/241 = 8, 8/127 = 23, 8/239 = 58 solutions.
* **Failing odd primes p ∤ m, p ≤ 10⁷, m = 8, 12, 16, 20: 5, 20, 37, 62 — lists identical to the author's
  `prime_fail_1e8.txt` restricted to ≤ 10⁷.** (The author's 10⁸ tails add no failures for these m, so their 10⁸ claims
  rest on their engine only; not re-run here.)
* **2763601 (m = 20): prime (trial division), ≡ 1 (mod 840), complete count f_20 = 0** (`review_ms_census 20 2763601 count`,
  all 414 540 x-values). Likewise f_24(620929) = 0.
* PW Table 1 (sources/pomerance-weingartner-2511.16817v2.pdf, p. 13, read directly): the odd-prime, p ∤ m entries for
  m = 8..15 are exactly the document's lists/counts (8: 5, 9: 3, 10: 7, 11: 2, 12: 20 up to 12241, 13: 9 up to 281,
  14: 8 up to 353, 15: 23 up to 20521). PW's ranges (10¹²–10¹⁸) are as quoted.

### §2 Lemma 2.1 (parity) — **SOUND**
Re-derived: v₂(4/n) = 2 for odd n. Three odd denominators → v₂(sum) = 0 (odd numerator xy+yz+zx over odd xyz).
Exactly two odd (x, y), z even: v₂(1/x + 1/y) ≥ 1 > v₂(1/z) = −v₂(z), so v₂(sum) = −v₂(z) < 0. Hence all even or
exactly one odd ✓. (b) is scaling; sorted order is preserved ✓. (c) In ET/PW coordinates each denominator is (product of
two of a, b, c)·d·(p or 1); with d odd, all three even forces two of a, b, c even, contradicting pairwise coprimality ✓.
p ≡ 3 (mod 4) construction: 1/(k+1) + 1/(k(k+1)) = 1/k, 1/(kp) + 1/k = (p+1)/(kp) = 4/p; whichever of k, k+1 is odd
gives the unique odd denominator ✓.
EVIDENCE re-run (own engine, `review_ms_census m N oneodd|alleven`): one-odd 4/p never fails for primes 3 ≤ p ≤ 10⁷
(664 578 primes; the 10⁸ claim not re-run); counts 4/131: 32 one-odd, 0 even; 4/241: 8 one-odd ✓. All-even share of
f_4 on primes (10⁴, 2·10⁴): 0.448 ✓. No 2- or 3-odd solutions occur in any count I ran (as proved).

### §5 count law — numbers **SOUND**, labels **SOUND-AFTER-REPAIRS** (minor wording)
* §5.1 recomputed (`review_ms_stats.py`, own counts, 1033 primes in [10⁴, 2·10⁴)): m·mean f_m/(4 mean f_4) =
  1.157 (m=5), 0.895 (8), 0.798 (12), 0.737 (16), 0.767 (20) — document 1.16, 0.90, 0.80, 0.74, 0.77 ✓.
  mean f_8 on primes in [150, 260): 15.2 (document "≈ 13 at p ≈ 200" from the fit — fine).
* §5.3 numbers agree with the author's `data/ms/tail_1e7.txt` (1.45/0.84 for m = 4; 1.85/1.06; 2.47/1.35; 2.99/1.57;
  combined 4.82–8.76 ✓; e^{−1.45} = 0.235, e^{−0.84} = 0.43 ✓). I did not re-implement the binned F(μ) model
  (it is an Assessment; the inputs — counts and census — were re-verified above).
* Labels: §5 is "EVIDENCE + Assessment"; the luck statements are inside an explicit Assessment with the Poisson
  assumption and the small-p miscalibration stated. Not overclaimed in substance. Defects D2–D4 below are wording.

### §6 B7 screen — **SOUND** (all spot-checked rows reproduced exactly)
Own engine, primes ≤ 10⁶: 8/p one-odd part fails at {3, 11, 17, 59, 131, 241, 449} ✓; 8/p Type I alone fails at
{3, 11, 17, 131, 241} ✓; 8/p Type II alone at 22 primes, last 35569 ✓; 4/p Type I alone and Type II alone: 0 failures ✓.
S_m(p) = ∅ for primes ≤ 10⁵ (`review_ms_slices.c`, direct word enumeration): m = 4: 0, 5: 0, 6: 25 (last 35911),
7: 10 (last 12601), 8: 23 (last 83449, list contains 3, 11, 17, 131, 241), 12: 156 ✓ — all as in Cor 3.2's EVIDENCE.
To 10⁷: S_4(p) ≠ ∅ for all 664 578 primes; S_8(p) = ∅ at exactly 27 primes, last four 211681, 215297, 252001, 259201 ✓.

### §4 identities / cube shots — **SOUND** (spot-checked)
* §4.1 (`review_ms_cover.py`, own atom enumeration): U_4(840) = {1, 121, 169, 289, 361, 529} exactly (Mordell);
  #U_4(9240) = 34 (30 squares); #U_8(840) = 35 (6 squares, 131 and 241 uncovered); #U_8(9240) = 243 (30 squares), 131 and
  241 still uncovered; for m = 4, 131 and 241 are covered at 840 ✓. Level 120120 not re-run. Atom shapes checked against
  PW Cor 2.2 (Type I: f | ma²d + 1, mad | p + f — read in the PDF); Type II atoms falsification-tested
  (`review_ms_atoms.py`: no failing prime of m = 8, 12, 16, 20, 24 (≤ 10⁷) lies in any atom class with modulus ≤ 3000;
  0 hits over 4.6k–21k atoms per m).
* §4.2 (`review_ms_shots.py`): primes ≤ 10⁶ with all three shots dead: 942 (m = 4), 102 (m = 5; 104 if p = 2, 5 counted),
  4308 (m = 8; 4309 incl. p = 2) ✓. The cube equivalences h | pj + c ⟺ h | p + mc²d ⟺ h | mdj²p + 1 (h = mcdj − 1;
  multiply by mcd resp. mdj, both units mod h) re-derived ✓.

### §7 construction notes — (C1) **SOUND-AFTER-REPAIRS** (D1, D6, D8), (C2)/(C3) Assessment, no defects found
(C1)'s equivalences are correct: χ ∈ {±1} on X_n (gcd automatic), so S_4(n) ≠ ∅ ⟺ χ ≢ +1 by Thm 3.1(a); for
n ≡ 1 (mod 4) χ is never ≡ −1 (word (n+2, 1, 1)), squares have χ ≡ +1 (T1), and λ(105) = 4, hence
SQ₅ ⟺ [χ ≡ +1 on X_n ⇒ n square or 105] ✓. (C3)'s withdrawal of the length-r claim is correct (105 has λ = 4 and no
five-slice certificate).

### Labels — overall **SOUND**
PROVED: Lemma 2.1, Lemma 3.0, Lemma 3.0′ (relative to Cor 4.1, stated), Thm 3.1 (relative, stated) — all re-derived.
CERTIFIED: §1 censuses (re-run to 10⁷ for 8 m-values; exact match), §4.1 coverings (re-run at 840, 9240).
EVIDENCE/Assessment: §2 tail, Cor 3.2 numbers, §5, §6 — numbers reproduced; the Assessment wording issues are D1–D3.
No PROVED/CERTIFIED claim was found to be over-labelled.

## Defects
(numbered; FATAL / MAJOR / MINOR). No FATAL defect found.

1. **MAJOR (overclaimed reading, wording repair).** §3 "*Reading (the sharp point)*": "for ES 'T1 is the only local
   obstruction' is true on the length-3 ball as an identity", and "ES's five-slice lottery has **no residual congruence
   obstruction at all**"; the same sentence is the SHARP headline of AGENT_REPORT_O197 ("on the length-3 ball, 'T1 is the
   only obstruction' is an identity for ES"). What Thm 3.1(a) proves is S_4 = {χ = −1} as *sets of words*. It does not
   say the χ = −1 fibre of X_n is non-empty whenever T1 does not apply: at the non-square n = 105 (≡ 1 mod 4) the fibre
   is empty (λ(105) = 4, DEDEKIND §9.1; §7 (C1)/(C3) of this very document mention it). Read literally, the headline
   says "S_4(n) = ∅ only at T1-obstructed n", which is CONJECTURE SQ₅ (false at 105, open for primes).
   *Repair:* "on the length-3 ball the ES certificate set is exactly a χ-fibre: no congruence condition on the word
   beyond the T1 character; whether the fibre is reached is SQ₅ (open; fails at the non-square 105)". Same edit in the
   report's SHARP paragraph.
2. **MINOR.** §5.3 Assessment (i) quotes "plug-in ≈ 0.02 failures" above p = 100 as "the expected outcome". Re-splitting
   the author's own bin table (obtained by re-running `ms_tail.py 1e7`; the bin table itself is **missing from the
   committed `data/ms/tail_1e7.txt`**, which only has the headers) with the m = 4 fit: p < 100 contributes 1.435 (K/N) /
   1.575 ((K+1)/N) on the 4 | m curve and 0.832 / 0.915 on the 4 ∤ m curve; **p ≥ 100 contributes 0.017 / 0.499 resp.
   0.005 / 0.107**. So above p = 100 the model pins the expectation only to "≲ 0.1–0.5", not 0.02 (zero-failure bins with
   N ≈ 10⁵–10⁶ primes carry all of it). *Repair:* quote "plug-in 0.02, (K+1)/N sensitivity 0.1–0.5", and commit the full
   `ms_tail.py` output (bin table) to `data/ms/tail_1e7.txt` — the rates 2.5·10⁻², 2.5·10⁻³, 2.6·10⁻⁴, ≤ 10⁻⁵ quoted in
   §5.3 are currently not in any committed data file (they do match the re-run).
3. **MINOR.** §5.3 "(iii) … m = 8 is the 4 | m pool's best-predicted member" — only in absolute error (1.46 vs 2). In
   ratio terms it is the *worst* (obs/pred 1.37; 12: 1.34, 16: 0.80, 20: 0.90, 24: 1.14). *Repair:* replace by "and its
   2 observed failures (p ≥ 100) are consistent with the leave-one-out prediction 1.46 (Poisson P(≥ 2) ≈ 0.43)".
4. **MINOR (stale report).** AGENT_REPORT_O197 Honest caveats: "3.4–7.8 expected for m = 4..7 combined" — after the P1
   binning repair the document (and `tail_1e7.txt`) give 4.82–8.76 ("4.8–8.8"). Report Results 1: "241 vs 2/19" (m = 7's
   only PW exception n = 2 is outside the odd-prime population; the document says "none / 19"). *Repair:* update both.
5. **MINOR.** §1: "PW also list n = 2 for m = 7 and 2, 3 for m = 12, outside this population" is incomplete — PW Table 1
   lists n = 1 for every m, n = 2 for m = 7..15, n = 4 (m = 11, 13, 14), 14 (m = 13), 25 (m = 12), 841 (m = 14), and
   composites 8, 16, 34, 122, 226 (m = 15), plus primes dividing m (3 for m = 12, 15; 5 for m = 10, 15; 7 for m = 14).
   And "m = 12, all n ≤ 3000: the 19 failures of PW Table 1 below 3000" — PW has 20 entries ≤ 3000 (incl. n = 1).
   *Repair:* "agreement on the odd primes p ∤ m (PW's remaining entries — n = 1, 2, 4, p | m, odd squares 25, 841 and
   composites — are outside this population)"; "the 19 entries with 2 ≤ n ≤ 3000".
6. **MINOR.** §7 (C1): "Hence 'the positive points of X_p reach every cell mod 8 allowed by χ' is false (at 27 primes
   ≤ 10⁷ at least)". The statement is false for essentially *every* prime for a counting reason: per residue n mod 8 there
   are 60 χ = −1 cells (and 35 S_8 cells), while X_p has only ≍ log² p points (43 at p = 131). The 27 primes are where the
   much weaker "reach *some* S_8-cell" fails. *Repair:* say "'the positive points of X_p reach some S_8-cell' fails at
   27 primes ≤ 10⁷", or drop the parenthesis.
7. **MINOR (presentation).** Thm 3.1(c) "for 5 ≤ m ≤ 15 the slices fill the same fraction of the cells of both χ-halves":
   for odd m this is automatic by CRT (cells mod 8m = cells mod 8 × cells mod m; χ lives on the first, S_m on the second);
   I verified it for every 4 ∤ m ≤ 23 including m ≡ 2 (mod 4), where it is a genuine computation. Optional: say so.
8. **MINOR (presentation).** "words with gcd(A, n) = 1" (§3 setting, §7 (C1)): gcd(A, n) = 1 is automatic from
   AA* = tn + 1, so χ ∈ {±1} on all of X_n(ℤ_{>0}); worth one sentence, since (C1)'s "χ not identically +1" ⟺
   "χ = −1 somewhere" relies on it. Also note that for n ≡ 1 (mod 4) the word (n+2, 1, 1) always has χ = +1, so
   "χ constant" in (C1) can only mean "≡ +1" (the author's equivalence with SQ₅ is then correct; for n ≡ 3 (mod 4) the
   same word has χ = −1, so S_4(n) ≠ ∅ trivially).

9. **MAJOR (inherited novelty / attribution, per R194 now on main).** MODEL_SPECIFIC presents the 8/n facts it builds on
   as campaign findings: header l. 4–5 "Builds on TES_FINITE §5 (O194: Schinzel 8/n has the same ℚ-surface, real anchor
   and order-2 T1 as ES, no BM obstruction at 131, 241, yet no solution there — barrier B7)"; §2 *Reading* "B7 says this
   sub-lottery has non-T1 failures"; §3 *Reading* / §6 / §7 "B7 demands", "B7 sibling"; AGENT_REPORT SHARP "the B7
   sibling". R194 (reviews/tes-finite-review.md D2–D4, merged on main) established: the 8/n failures 3, 11, 17, 131, 241
   are **Pomerance–Weingartner Table 1** (row m = 8, complete to 10¹³ — I re-read the row in the PDF); the absence of a
   BM obstruction for the Schinzel surfaces is **Bright–Loughran Remark 1.10** (the surfaces are ℚ-isomorphic to U_n);
   B7 = TES_FINITE Cor 5.4 is an immediate consequence of these two citations. None of this is new in O194 or here.
   *Repair:* in the header: "the failures of 8/n at 3, 11, 17, 131, 241 are PW Table 1; the absence of a BM obstruction
   for these surfaces is Bright–Loughran Rem. 1.10; B7 (TES_FINITE Cor 5.4) is their immediate consequence"; at the
   first B7 mention in §2: "PW Table 1 shows this sub-lottery has non-T1 failures". The report's SHARP should say
   "the sibling 8/n (known failures, PW Table 1; not BM, BL Rem 1.10)". The genuinely new content of MODEL_SPECIFIC
   (Thm 3.1, Lemma 2.1 framing, §6 screen) is unaffected.
10. **MINOR (factual error in a novelty claim).** §1 "New here (to my knowledge; **PW stop at 15**): m = 16–24 lists"
   and report Results 1 "new lists m = 16–24". PW §6 (p. 12) state that they verified by computer, for **all
   m ∈ [16, 30000] except m = 19**, the existence of a prime p ∈ (m², 2m²) with m/p not a sum of 3 unit fractions
   (their conjecture: every m ≥ 20). So failures for m = 16–18, 20–24 are known; PW publish no lists. What is new here is
   only the *complete* lists to 10⁸/10⁷ and specific values such as 2763601 (m = 20) and 620929 (m = 24).
   Cross-check (worth adding): the census is consistent with PW §6 — every m ∈ {16, 17, 18, 20, …, 24} has a failing
   prime in (m², 2m²) (e.g. 16: 257, 421; 17: 421; 20: 401, …; 24: 577, …), and m = 19's failures all lie below
   19² = 361 (last 353), matching PW's exception m = 19.
   *Repair:* "PW §6 verify that every m ∈ [16, 30000] except 19 has a failing prime in (m², 2m²); the complete lists
   below 10⁸ (m = 16–20, 24) / 10⁷ (21–23) are new here, to my knowledge."

## Work log
* Merged side-agent/model-specific (acc1a387). Own code only for every check: `review_ms_words.py` (word enumeration,
  own Jacobi, exact rationals; brute-force-validated for n ≤ 81), `review_ms_cells.py` (cells mod lcm(8, m), m = 4..24,
  example words for 5 ≤ m < 2000), `review_ms_census.c` (complete m/p search, modes all/t1/t2/oneodd/alleven/count),
  `review_ms_naive.py` (Fraction brute force, cross-check of the C counts and odd-square exceptions 25, 841, 9, 121),
  `review_ms_stats.py` (§5.1 means), `review_ms_slices.c` (S_m(p) = ∅, to 10⁷ for m = 4, 8), `review_ms_shots.py`,
  `review_ms_cover.py`, `review_ms_atoms.py`. Author's `ms_tail.py` run only to read its bin table (D2).
* Censuses ≤ 10⁷ re-run for m = 8, 12, 16, 17, 19, 20, 23, 24: identical lists to the author's data.
* Sources read: PW arXiv 2511.16817v2 (Table 1 p. 13; §6 p. 12; Cor 2.2/2.4); R194 review on main for the BL Rem 1.10
  attribution (BL PDF itself not re-read here — R194 did).
