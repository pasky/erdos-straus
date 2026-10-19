# R290 — hostile review of O279 FRONTIER.md

Reviewer: side-agent/review-frontier. Documents: FRONTIER.md (as merged from side-agent/frontier-doc), AGENT_REPORT_O279.md.
Status: COMPLETE (round 1). **Overall: SOUND-AFTER-REPAIRS; no FATAL; 3 MAJOR, 6 MINOR; no overclaim.**

**Repairs applied** (author quiet — no commits on side-agent/frontier-doc after the O279 report): M1, M2, M3, m1, m2, m3, m4, m5
applied directly to FRONTIER.md, each marked "(R290 repair)" (11 markers). m6 not applied (clarity only). X1–X3 are in other
files and are forwarded to the parent, not edited.


## Task (2): the (★) main-term constants — RESOLVED (no inconsistency; FRONTIER's framing is wrong)

**Derivation (reviewer, from scratch).** Trial form: R(n) = Σ_{(u,C)∈𝓡} 1[m | n+u], m = 4uC − 1. Note gcd(m, u) = gcd(−1, u) = 1,
so −u is a *unit* mod m.
* For **arbitrary integers n**, the density of n with m | n+u is 1/m. Hence PARITY_AUDIT's M(p) = Σ_𝓡 1/m = (log p)²/8 + O(log p)
  is the zero-frequency Fourier term, i.e. the **average of R(n) over all integers n** of size p (correct as stated, as an identity
  R = M + E with E the non-zero frequencies).
* For **primes p**, the density of primes in the unit class −u mod m is 1/φ(m). The prime-adapted trial main term is
  M_φ(p) := Σ_𝓡 1/φ(4uC − 1). For fixed u, the mean of m/φ(m) over m ≡ −1 (mod 4u) is ∏_{ℓ∤2u}(1 + 1/(ℓ(ℓ−1))); summing
  Σ_u (1/(4u))·log(p/4u)·(that factor), the u-average of the local factor at each odd ℓ is
  (1 − 1/ℓ)(ℓ²−ℓ+1)/(ℓ(ℓ−1)) + 1/ℓ = 1 + 1/ℓ², so M_φ(p) ∼ (1/8)∏_{ℓ odd}(1 + ℓ⁻²) L² = (1/8)(12/π²)L² = **(3/(2π²))L²** —
  exactly BM_CORRECTED's M₀ constant, via a different parametrisation. So the two sources describe **different quantities**:
  1/8 = all-integer average (Σ1/m), 3/(2π²) = prime singular series (Σ1/φ(m) in trial form = Σ1/φ(4uB) in pair form).
  Ratio 12/π² ≈ 1.216.

**Numerics (from scratch, `scripts/review_r290_constants.py`, log `logs/review_r290_constants.log`; R validated against brute
force for all 3 ≤ n < 403).** Windows [N, N+2·10⁵), L = log(midpoint):

| N | L²/8 | M_int=Σ1/m | M_φ=Σ1/φ(m) | M₀ (pairs) | 3L²/(2π²) | mean R, all n | mean R, primes | mean R, p≡1(4) |
|---|---|---|---|---|---|---|---|---|
| 10⁶ | 24.19 | 23.65 (0.122L²) | 29.46 (0.152L²) | 28.93 (0.150L²) | 29.41 | 25.72 (0.133L²) | 31.91 (0.165L²) | 32.26 (0.167L²) |
| 10⁷ | 32.51 | 31.85 (0.122L²) | 39.53 (0.152L²) | 39.00 (0.150L²) | 39.53 | 34.24 (0.132L²) | 42.38 (0.163L²) | 42.71 (0.164L²) |

* mean R over all n ≈ M_int + 0.15L; mean R over primes ≈ M_φ + 0.20L (both offsets stable between 10⁶ and 10⁷, i.e. genuine
  O(L) secondary terms). Ratio prime/all = 1.254 → 1.247, drifting toward 12/π² = 1.216.
* So **for primes the right leading constant is 3/(2π²)** (BM_CORRECTED Thm 2.2 / Prop 2.3), and (log p)²/8 underestimates the
  prime mean by ≈ 22 % at leading order (≈ 25 % in range). PARITY_AUDIT's E(p) therefore has a systematic **positive** mean
  ≈ (3/(2π²) − 1/8)L² ≈ 0.027L² at primes (the Ramanujan-sum terms, since p is coprime to every m).
* PARITY_AUDIT's supporting remark "(M(p) reproduces … the observed R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰, where
  (log p)²/8 = 42.4, 53.7, 66.3)" is a coincidence of three single values (sd of R at that size ≈ 1.4·√(2M) ≈ 15): the prime mean
  at 10⁸ is ≈ 0.16·L² ≈ 55. FRONTIER §2.2 repeats these three values as if they supported the constant.
* Five-slice 45/(8π²) (BOARD2_SLATE Prop 3.4): a third, different quantity (ordered five-slice pairs u, v ≥ 2, three
  even sectors automatically active). Arithmetic re-checked: 9/(8π²) + 3·(3/(2π²)) = 45/(8π²); Burgess 45/(32π²) = ¼ of it;
  PV 15/(64π²) = 1/6 of the Burgess value. Consistent with (★)'s 3/(2π²) (ratio 3.75, explained in the source). Not
  recomputed numerically from scratch (source's own fit: mean M₀/L² = 0.450 at 10⁶ vs 0.570 asymptotic, slow k ≥ 3 sector) —
  the Assessment label is appropriate.

**Verdict.** No mathematical inconsistency in the repo's *theorems*; FRONTIER's sentence "These are different expansions; the repo
does not reconcile the constants … nothing below depends on the constant" and §7 item 16 should be replaced by the resolution
above. Additionally PARITY_AUDIT (not FRONTIER's responsibility, but cited by it) should get a note on Lemma 2.1's parenthetical
and on its E2 table row ("heuristic size (log p)²/8"): 1/8 is the all-integer density; the prime heuristic is 3/(2π²).

## Task (3): "PH: EVIDENCE to 3.7·10⁷" (STATUS) vs LONGSHOT_PIGEONHOLE Conj 5.1 — RESOLVED

Source of truth: `LONGSHOT_PIGEONHOLE.md` §3 Table 3.1, reading 5, and Conj 5.1; input list `data/lsa/hard.txt`.
* The evidence for PH (cover with φ(e) ≥ 40, i.e. P20 ≥ 1) consists of three different samples: (a) **all** 2 370 Mordell-hard
  primes < 10⁶ with e ≤ 2000 — exactly two failures, 3529 and 110881 (failures *at E = 2000*; larger e not searched);
  (b) 300 consecutive Mordell-hard primes after 10^k, k = 4…8, e ≤ 5000 (only failure 110881, in the 10⁴ block);
  (c) 14 distinct hand-picked hard primes (`data/lsa/hard.txt`: 2521 … 37 117 609; 5101441 listed twice, hence "15"), e ≤ 20000.
* "3.7·10⁷" is simply the largest prime of sample (c) (37 117 609). STATUS's "(EVIDENCE to 3.7·10⁷)" reads as an exhaustive
  range and is wrong in both directions: nothing is exhaustive above 10⁶, while sampled evidence reaches 10⁸. DISCOVERIES.md:513
  ("all hard primes up to 3.7·10⁷ have one") has the same defect (it is the 14 selected hard primes, not all hard primes).
  AGENT_REPORT_O135:32 / O137:17 are the origin of the phrase.
* **Which file to correct:** STATUS.md:170 and DISCOVERIES.md:513 (not LONGSHOT_PIGEONHOLE, whose Conj 5.1 wording is accurate).
  Suggested text: "EVIDENCE: all Mordell-hard primes < 10⁶ except 3529, 110881 (e ≤ 2000); 300 consecutive Mordell-hard primes
  after 10^k, k = 4…8 (e ≤ 5000); 14 selected hard primes ≤ 3.7·10⁷ (e ≤ 20000)."
* FRONTIER (§3 B4, §5.5) says "EVIDENCE on *sampled* Mordell-hard primes ≥ 10⁶, exceptions below 10⁶: 3529, 110881": faithful
  to the source but undersells that the < 10⁶ range is exhaustive and should say the exceptions are relative to e ≤ 2000.
  MINOR (defect m-PH below).

## Task (1): fidelity sweep

Method: every labelled statement in FRONTIER.md checked against its cited source (three parallel research-mode sweeps over
§§1–2, §3, §4–8, each reporting mismatches; every reported mismatch then re-checked by me), plus my own spot checks of the
highest-risk items, with from-scratch code where computable:
* Theorem K (METAPLECTIC_ES; FRONTIER §2.3): K2 R_t(n) = D_t⁻(tn+1) − β_t(n) and the theta-quotient identity (K1′) verified
  for t = 3…9, n < 150 by brute force / exact power series (`scripts/review_r290_spot.py`, 0 failures).
* E₈ ∩ primes < 2000 = {2, 3, 11, 17, 131, 241} (§1, AMPLIFY_EXCEPTION Thm 2.5): reproduced exactly.
* p = 3361 (§4 item 14): exactly 2 Type II solutions, the two listed (15 solutions total, 13 Type I): reproduced.
* §4 item 1 / Lemma CT ("every denominator prime to p has a prime factor ℓ with (ℓ/p) = −1"): no violation in all 3 498
  solutions of 4/p, p ≡ 1 (4), p < 1500 (`scripts/review_r290_ct.py`).
* Arithmetic of all quoted constants: 3/(16π²) = 0.0190, 1/(32π²), 3/(2π²) = 0.152, 45/(8π²) = 0.570, 45/(32π²), 15/(64π²),
  2^{21.44} ≈ 2.8·10⁶; 8/131 = 1/20 + 1/131 + 9/2620; 8/121 = 1/18 + 1/99 + 1/2178 — all correct.
* Elsholtz–Planitzer (§1): checked against arXiv:1805.02945 Theorem 3 and its proof: for m = 4, f(4,n) ≥ exp((log 6 + o(1))
  log log n) on a density-one set — matches FRONTIER (LITERATURE_2026 had it only second-hand; now confirmed first-hand).
* Census claims (14 (★) failures ≤ 10¹⁰; b = 1 failures 193, 2521, 66529 ≤ 10¹¹; CERTIFIED ≤ 10⁸ by two engines, ≤ 10¹⁰
  by one): match DISCOVERIES (J)89/(J)90 and B1_LINE §3.6. Not re-run.
* Reported-but-rejected: a sweep flagged "3/4 note: three reviews incl. a blind audit" (§1) as contradicted by
  `reviews/wave32-sec76-review.md` defect 1. Rejected: that review (2026-09-06) predates the blind audit
  `reviews/es-threequarter-blind-audit.md` (2026-10-01, SOUND); DISCOVERIES (B)11 lists exactly the three reviews. FRONTIER
  is faithful.

Mismatches found are listed as defects below (M1–M3, m1–m6). Everything else in the sweep matched source + repairs; given that
the author's own deep self-review already repaired 24 fidelity defects, the residual rate is low.

## Task (4): usefulness of §4 and §6

* §4 is honestly scoped (the "Scope (read this)" paragraph correctly says the lines are screens for mapped classes of
  arguments, not necessary conditions for every proof). Each line has a pointer; the pointers resolve. Items 1, 4, 5, 6, 7, 8,
  9, 12 are the load-bearing ones and are correctly stated.
* Missing / under-represented barrier: **B4 (covering certificates / pigeonhole / large fibres)** appears in §3 but has no
  checklist line (items 8 and 10 touch it only obliquely). A newcomer proposing "cover the target coset from the prime
  factors of N_e" will not be stopped by §4. See m4.
* Missing from §4: the **ordered/unordered and integer-vs-prime density** pitfall (the very discrepancy flagged in §2.2): a
  newcomer computing an expected count for (★) at primes with Σ1/m will be off by 12/π². Fold into item 6 (see M1 repair).
* §6 (dead ends): spot-checked ≈ 15 of ≈ 35 one-liners against pointers (GRH-by-character p^{1−o(1)} = CONDITIONAL_ES Prop
  3.1.1; 56×54 identity rank, (I)5/DISCOVERIES:474, CERTIFIED with finite scope stated; Linnik; privacy; signed reflection
  scoped to |d|-preserving; brainstorm "promise ≤ 2/5" = README "nothing scored above 2"). Fair and appropriately hedged
  ("do not repeat without a new ingredient"). Minor: "none LIVE" — the README has one LIVE tag (bsE_et_casework_depth), an
  obstruction-side function-field result, not an ES route; harmless but could say "none LIVE as an ES route".

## Task (5): honesty

* "ES is not solved — not here, not anywhere" is the first boxed statement; "none of it is externally refereed" in the label
  paragraph; §5 header repeats "All internal; none externally refereed." PASS.
* No statement claims ES or a case of ES for all large primes, conditionally on a standard conjecture or otherwise. The only
  implications toward ES (§5.4) are from ES-strength hypotheses and are labelled so. PASS.
* The one-paragraph summary's "every route … ends at one statement" is an unlabelled Assessment (it is the campaign's
  judgement, not a theorem). MINOR (m6).

## Defects

### MAJOR

**M1 — §2.2 "Two normalisations of 'the main term'" paragraph; §7 item 16; §2.2 "M₀ … prime-averaged pair series".**
FRONTIER says the repo does not reconcile 1/8 and 3/(2π²) and calls M₀ "the prime-averaged pair series". Both are wrong framing
(task (2) above): (log p)²/8 = Σ_𝓡 1/m is the density for *arbitrary integers* n (zero Fourier frequency); for *primes* the
singular series is Σ_𝓡 1/φ(m) = M₀ + O(L) ∼ (3/(2π²))L², because −u is a unit mod m. Both count *ordered* triples (u, B, C)
(R(p) is even; distinct (★) solutions = R/2). Measured prime means (0.164 L² at 10⁶–10⁷) confirm 3/(2π²) + O(L); the quoted
"observed R(p) = 44, 52, 68 vs (log p)²/8 = 42.4, 53.7, 66.3" is a three-point coincidence. M₀ is not "prime-averaged": it
depends on p only through its size.
*Repair:* replace the paragraph by the resolution (applied, marked R290 repair); delete §7 item 16 (replace by a one-line
pointer to the resolution); in §4 item 6 add the integer-vs-prime density caution.

**M2 — §3 B4 statement, first sentence.** "Covering certificates built from the prime factors below the modulus fail for a
positive proportion of primes in every slice." LONGSHOT_PIGEONHOLE Thm 2.2 (as repaired by R135) concerns *transparent covering
certificates TCC_θ*: residue information from prime factors < e plus one opaque cofactor, covering a coset of size
≥ φ(e)e^{−θ}/2 with θ < 1/2 (R135 remark: every θ < 1); the failure set is a positive *lower relative density* inside
p ≡ 1 (mod q₀), simultaneously for all e and both types. FRONTIER drops the coset-size hypothesis and the opaque-cofactor
allowance; certificates that merely hit −1, or cover smaller cosets, are not excluded (the source says so explicitly).
*Repair:* "Transparent covering certificates (residues of the prime factors below the modulus, plus one opaque cofactor)
covering a coset of size ≥ φ(e)e^{−θ}/2 (θ < 1/2; R135: any θ < 1) fail, simultaneously in every e-slice of both types, for
a set of primes of positive lower relative density (inside p ≡ 1 mod 8∏_{3≤ℓ≤Y}ℓ)." (applied)

**M3 — §1 Parametrisations / T1: Type I/II defined only by "p divides exactly one (two) denominator(s)".** That gloss is
correct for primes, but T1 is then stated for n = m², where under the gloss it is **false**: 4/9 = 1/3 + 1/18 + 1/18 (9 divides
two denominators) and 4/9 = 1/4 + 1/6 + 1/36 (one). ET's definition (Elsholtz–Tao §1, checked in `sources/`) is: Type I if n | x
and n is coprime to y, z; Type II if n | y, z and n is coprime to x. Since T1 is advertised as "the single most useful test in
this document", a newcomer must get the definition right.
*Repair:* give ET's coprimality definition, note it reduces to the gloss at primes, and add the 4/9 example. (applied)

### MINOR

**m1 — §3 B4 and §5.5, PH evidence.** Faithful to LONGSHOT_PIGEONHOLE but undersells and slightly misstates: the range < 10⁶
is *exhaustive* over Mordell-hard primes (E = 2000), and 3529, 110881 are failures *at that E*. Repair (applied): "EVIDENCE:
all Mordell-hard primes < 10⁶ except 3529, 110881 (e ≤ 2000), 300-prime samples after 10^k up to 10⁸ (e ≤ 5000), 14 selected
hard primes ≤ 3.7·10⁷ (e ≤ 20000)".

**m2 — §8 board memos.** `~/.pi/boards/…/memo.md` exist on this machine but are outside the repository (not git-tracked); a
fresh external reader will not have them. Repair (applied): say so, and point to BOARD2_SLATE / STATUS as the in-repo record.

**m3 — §4 lacks a B4 line.** Repair (applied): new item 17 "Covering certificates must use large prime factors".

**m4 — §6 last bullet "none LIVE".** BRAINSTORM/README has one LIVE tag (bsE_et_casework_depth), an obstruction-side
function-field result. Repair (applied): "none LIVE as an ES route".

**m5 — One-paragraph summary.** "every route … ends at one statement" is the campaign's judgement. Repair (applied): mark
"(Assessment)".

**m6 — §2.4 "It needs p₀ ≥ 8.9·10⁶ (the (★) census)".** Correct, but note it is a necessary lower bound on p₀ (the largest
known (★) failure is 8 813 281), not a value at which H⁻_BM is known to hold. Clarity only; not applied.

### Outside FRONTIER (forward to the parent; not edited by me)
* **X1 PARITY_AUDIT.md** Lemma 2.1 parenthetical "(M(p) reproduces … R(p) = 44, 52, 68 …)" and §1 table row E2 ("its heuristic
  size (log p)²/8 is Lemma 2.1's M(p)"): 1/8 is the all-integer density; at primes the heuristic is 3/(2π²) (task (2)). The
  lemma itself (an identity with E(p) the non-zero frequencies) is correct; at primes E(p) has mean ≈ +0.027L².
* **X2 B1_LINE.md** Lemma 3.1 ("Haar main term (log p)²/8" for the b = 1 line; (log p)²/16 distinct for (★)) and Conj 3.5's
  heuristic basis: same integer-vs-prime issue (w = 4cd − 1 is coprime to 4d, so primes have density 1/φ(w)). The NB model's
  predicted failure counts are therefore pessimistic by construction — which is exactly what §3.6 observed. Suggest a note.
* **X3 STATUS.md:170, DISCOVERIES.md:513** PH evidence wording (task (3)).

## Summary verdicts (per claim / section)

| claim | verdict |
|---|---|
| Banner, labels, honesty (ES unsolved; nothing externally refereed) | SOUND |
| §1 landscape (verification, ET parametrisation, Elsholtz–Planitzer, T1, BL, exceptional set, thin families, 8/n) | SOUND-AFTER-REPAIRS (M3) |
| §2.1 (★) forms, genus split, census | SOUND (forms re-derived; Thm-K-adjacent identities checked) |
| §2.2 M_BM theorem, Linnik two-sided failure | SOUND |
| §2.2 "two normalisations" paragraph / §7 item 16 | GAP → resolved (M1) |
| §2.3 Theorem K | SOUND (verified from scratch t ≤ 9, n < 150) |
| §2.4 H⁻_BM, honest reading, numerics, five-slice constants | SOUND |
| §3 B1–B3, B5, B6, B-fin, tied modulus, reciprocity, privacy, positivity, numerator blindness, disproof, power ladder, M1a–M5, Dickson roots | SOUND |
| §3 B4 | SOUND-AFTER-REPAIRS (M2, m1) |
| §4 checklist | SOUND-AFTER-REPAIRS (m3; scope paragraph is correct) |
| §5 partial / conditional results | SOUND (m1 for PH) |
| §6 dead ends | SOUND (m4) |
| §7 open problems | SOUND-AFTER-REPAIRS (item 16 superseded by M1) |
| §8 pointers | SOUND (all files exist; m2) |

No FATAL defect. No overclaim of ES or of any conditional ES theorem from a standard conjecture.
