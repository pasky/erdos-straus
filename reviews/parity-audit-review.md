# R265 — hostile review of O255 (PARITY_AUDIT.md, branch side-agent/parity-audit)

Reviewer: R265 side agent. Reviewed commit: 282afc57. Scripts: `scripts/review_pa_*` (from scratch).
Status: IN PROGRESS.

## Summary verdicts
(filled in per claim below)

## Claim 7 — census EVIDENCE (§5): **SOUND**

Recomputed from scratch in C (`scripts/review_pa_census.c`, log `logs/review_pa_census_1e6.txt`, 5.4 s, 1 core)
and Python (`scripts/review_pa_small.py`), using only the definitions in §0 (not the author's scripts).
All numbers reproduce exactly:
* (a⁴) fails (u ≤ √p + 2, which suffices by the u ↔ B symmetry of 4uBC − u − B = p) at exactly the 9 primes
  409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321 among the 39 175 primes p ≡ 1 (4) ≤ 10⁶. Independent
  O(p log p) brute force over (u, B) confirms R(409) = R(577) = R(5569) = 0. Least u: median 1, 99th pct 5, max 131
  at p = 427249 (confirmed).
* ES-five u-side, p ≡ 1 (8): 19 552 primes, 0 failures, 17 573 with least u ≤ 2 (89.88 %), median 1, 99th pct 5,
  99.9th pct 11, max 17 at p = 196561. p ≡ 1 (840): 395 primes, 238 at u ≤ 2 (60.25 %). Exactly 3 primes need
  u ≥ n_p.
* Windows (q < 3p; note neither event can hold for q > (p+4)/3 since d ≥ q − 1 and u + v ≤ K_q + 1): sub-event
  fails at 8272 primes, full target −1 event at 2458; max least q for the sub-event 141 971.
* T1 control: 499 odd squares 9 ≤ m² ≤ 10⁶, no (a⁴) hit at u ≤ m + 2.

Minor: "(a) hit" at odd squares (§5 T1 bullet) is undefined for composite n (ψ = Jacobi? the class layer alone?).
State which symbol was used (defect m1).

## Claim 3 — Lemma 2.1 (trial count): **SOUND** (minor sharpening suggested)

Re-derivation. (u, C) ↦ B = (p + u)/(4uC − 1) is a bijection onto solutions; B ≥ 1 ⟺ 4uC − 1 ≤ p + u, which forces
u ≤ (p+1)/3 (the text's "u ≤ p" is harmless). |𝓡| = Σ_{u ≤ (p+1)/3} ⌊(p+u+1)/(4u)⌋ = (p/4) log p + O(p) ✓.
Inner sum Σ_{C ≤ X} 1/(4uC − 1) = (1/(4u))(log X + O(1)), X = (p+u+1)/(4u); summing (1/(4u)) log(p/u) over
u ≤ p/3 gives (log p)²/8 + O(log p) ✓. The Fourier split E(p) is the standard 1[m | n] − 1/m ✓.

From-scratch numerics (`scripts/review_pa_lemma21.py`): R via (u, f) divisor count equals an independent (u, B)
brute force for all 77 primes < 400 and at p = 10007. At p = 10⁴+7, 10⁵+3, 10⁶+3, 10⁷+19 I get M = 10.343, 16.172,
23.329, 31.811 and |𝓡|/((p/4) log p) = 0.922, 0.937, 0.948, 0.955, R = 22, 20, 16 (10⁷+19 not recomputed) — exactly
the author's values. M − (log p)²/8 ≈ −0.04 log p, |𝓡| − (p/4) log p ≈ −0.181 p: consistent with the O-terms.

Minor (m2): the U-version M_U(p) = (log U)(log p)/4 − (log U)²/8 + O(log p) is true but, at the polylog U where it
is used, the O(log p) error (= γ·log p/4 + …) is of the same order as the "main" term up to a factor log log p
(numerically at U = 10 the error is ≈ 0.13 log p against a main term 0.58 log p). Cleaner and sharper:
M_U(p) = (log p/4)·H_U + O((log U)² + 1), |𝓡_U| = (p/4)·H_U + O(U), H_U = Σ_{u≤U} 1/u.
Minor (m3): "restricting u does not shrink 𝓡" — it shrinks it by the factor log U/log p (≍ log log p/log p at
polylog U); the point (still ≍ p, not polylog) is right, the wording "does not shrink" is loose. Also the claim is
parametrisation-dependent: it says the *naive* (u, C) trial set stays of size ≍ p; it is not a theorem that every
complete-sum treatment of (a⁴) at polylog U must face ≍ p trials (Verdict (iii) should say "for the (u,C)/(u,B)
parametrisations", see Claim 8).

## Claim 2 — exact single-p events (§0) and Lemma 0.1: **SOUND**

Re-derived: (tu − 1)(tv − 1) = t(tuv − u − v) + 1 = tp + 1 ✓; min(u,v) ≤ (√(tp+1) + 1)/t ≤ √(p+1) + 1 ✓ (the
bound is decreasing in t); AB ≡ 1 (mod p) gives ψ(A) = ψ(B) so the u ↔ v swap preserves the sign ✓; hence
E_a(p; √p + 2) ⟺ ES-five(p) given (J)9 Thm 4.5 ✓. (a⁴): (4uC − 1)(4BC − 1) = 4Cp + 1 ✓, min(u,B) ≤ (√(4p+1)+1)/4 ✓,
two-variable form R(p) = #{(u,B) : 4uB | p + u + B} ✓, swap form (cofactor of g ≡ −1 (mod 4C) in 4Cp + 1 is again
≡ −1 (mod 4C)) ✓. Window conditions match CAP_POINTWISE Thm 1.1 (i)–(iii) ✓.
Minor (m4): the "class/size layer" of (a) alone is trivially satisfiable (u = 1, A = any divisor of p + 1;
(u−1)(v−1) = p + 1 always has solutions). The text says so only in §5; say it in §0 where the two layers are
introduced, otherwise "two layers" suggests both are obstacles.

## Claim 4 — Lemma 3.2: **SOUND** (two cosmetic remarks)

Re-derived. χ_{−4u} = Kronecker (−4u/·) is a character mod 4u because −4u ≡ 0 (mod 4) is a discriminant, and it is
odd because −4u < 0 ✓. For ℓ | m² + u, ℓ ∤ 2u: (−u/ℓ) = 1 ✓; any f ≡ −1 (mod 4u) is coprime to 4u so all its prime
factors are such ℓ ✓. Prime case: −u ≡ p (mod ℓ) and reciprocity for p ≡ 1 (4) ✓. Free χ-shadow at p ≡ 1 (8) ✓;
p = 13, u = 5 counterexample ✓ ((5/13) = −1, 18 = 2·3², χ_{−20}(3) = +1).
From scratch (`scripts/review_pa_lemma32.py`): no hit for any square m² (m < 300, odd *and even*), u ≤ 60; 92 143
pairs (p ≡ 1 (8) < 4·10⁴, QNR u < 200) all have the required ℓ; 362 counterexamples for p ≡ 5 (8) < 2000, u < 50.
Minor (m5): oddness of m is never used — the lemma holds for every square. Minor (m6): in the prime-case sentence
add "u < p" (needed for ℓ ≠ p, as in the χ-shadow paragraph).

## Claim 6 — Dyachenko 2511.07465 assessment (row E4, §4): **SOUND** (one fairness repair)

Checked against `sources/dyachenko-2511.07465.pdf` (pdftotext). Abstract (l.25) and intro (l.71, 95, 112) cite
"Theorem 10.21"; §10 is "Experimental data [tab.3]" and contains no theorems; the claim is Theorem 9.21 (p. 28) ✓.
9.21(III) defines L = {(u,v) : ub′ + vc′ ≡ 0 (mod g)} with b′ = b/g_b, c′ = c/g_c built from (b, c, δ) satisfying
(I), which already includes (4b − 1)(4c − 1) = 4Pδ + 1 — i.e. a solution is an input ✓. Prop 9.25 is the elementary
"a lattice with diagonal period d′ meets every d′ × d′ box" ✓. The return step (§9.10, l.1550; "Connection with
§7.3", l.1633) needs v with u² − v² = 4A/α, a factorisation of 4A/α in a parity/size class — the divisor event,
not proved ✓. Lemmas/Theorems D.33, D.16 exist (the paper calls them both "Lemma" and "Theorem"; cosmetic).
MINOR (m7): the quotation of §11 is truncated in a way that slightly over-favours the audit: the sentence reads
"is certainly not proven **constructively** in the present work", and the next bullet claims "for any fixed odd
prime P, the existence of a solution is strictly proven". Quote both. Read literally, "for any fixed P" is
"for all P", i.e. ES for P ≡ 1 (4), and is exactly what 9.21(III) does not deliver; the paper is internally
inconsistent rather than conceding. Repair: replace the E4 quote by the two bullets verbatim and add that remark.

## Claim 1 — citation accuracy (§1 table): **SOUND-AFTER-REPAIRS** (no hallucinated item; 3 minor inaccuracies)

Method: primary sources fetched from the web (arXiv PDFs/abstract pages, Leiden PDF of Lenstra, utupub author
version of Matomäki 2016, Borwein–Choi PDF) or local PDFs. Three research subagents did a first pass; **every
discrepancy they reported was re-checked by me against the primary text, and 7 of their 11 "discrepancies" were
false** (A1, B2, B2′, C1, C2, C3, D6 — see below). Verdicts are mine.

| row | primary source checked | verdict |
|---|---|---|
| A1 Lenstra 1984 | Leiden PDF: abstract (11 divisors, s ≥ n^{1/3}), Prop (3.1) p. 340 (c(α) for α > 1/4), and §2 after Table I: "the proof of (2.1) shows that we can take c(α) = O((α − 1/4)^{−2})" | ✓ (O-bound is in Lenstra, not only CHN) |
| A2 CHN 2008 | IACR ePrint abstract, AMS record | ✓ |
| A3 Erdős–Hall 1976 | Cambridge record (title "Proof of a conjecture about the distribution of divisors of integers in residue classes" = excerpt) | ✓ title/journal; Gaussian-tail formula only via author's OCR excerpt (consistent with the authors' remark (3)); not independently verified |
| B1 Shparlinski | arXiv 1103.2879: Thm 13 (p. 14) ✓; §3.1 "out of reach … related to … Selberg–Hooley m ≤ X^{2/3−ε}" ✓; every-a Cp^{3/4} = ref [92] (Garaev) ✓; §6.3 "apparently is very hard" ✓ | **m8**: the almost-all-a bound m^{1/2}(log m)^{1+ε} is ref. [98] = **Garaev–Karatsuba** (PEMS 50 (2007)), not "Garaev" (row B1, §2 ledger row 2, §2 answer paragraph, §3 item 4) |
| B2 KMS 2017 | arXiv 1511.01636 Thms 1.1, 1.3, 1.7 | ✓ (saving q^{1/64} at M = N = q^{1/2} correct; also confirmed by Blomer–Pascadi Rem. 1.2) |
| B2′ Blomer–Pascadi | arXiv 2607.24311 PDF, Thm 1.1 (1.3) and Rem. 1.2 verbatim: saving c^{−1/32}, range N ∈ (c^{13/28+ε}, c^{7/12−ε}) against trivial min(c, N√c), prime record p^{3/8} | ✓ (title: "Bilinear forms with Kloosterman sums via quadratic characters" — add) |
| B3 KMS 2020 | arXiv 1802.09849 Thms 1.2–1.3 | ✓; add pages 1453–1530 |
| B4 KSWX | arXiv 2204.05038 v5 (accepted JLMS) | statement ✓; journal volume still unverified — **m9**: drop "(2) 108 (2023)" or verify |
| B5 Bourgain–Garaev | arXiv 1211.4184 | ✓ |
| C1 Li–Yang | arXiv 2308.14859: Thm 1.2, θ* = 0.3144831759…, "0.3125 is an unbeatable barrier of the existing [methods]" | ✓ |
| C2 Matomäki | utupub author version: abstract "[x, x + √x(log x)^{7/3+δ}] contains … x^ε[-smooth]" verbatim; 2010 note [x, x+C√x], x^{1/(5√e)+ε} (unconditional) | ✓ |
| C3 Younis | arXiv 2409.05761 abstract verbatim (17/30, exp((log x)^{2/3+ε}); RH: 1/2, (log x)^K) | ✓ |
| D4 Lichtman | arXiv 2211.09641 Thm 1.1 (β > 15/(32√e) = 0.2843), 1.4; 2309.08522 Thm 1.2 (G(a) ≤ 3.3907 Π_a(a), every large even a), Cor 1.5 (5/8 under Selberg) / Thm 1.7 ((5−4θ)/(8−6θ), = 66/107 at θ = 7/32) | ✓ |
| D5 Pascadi | 2304.11696 Thm 1.1; 2505.00653 abstract, Thms 1.3, 1.5 and p. 4 ("does not appear to be … a better exponent with current methods"); 2404.04239 Thm 1 | ✓ |
| D6 Merikoski / G–M | 1908.08816 Thms 1–2; 2505.00493 abstract: "at least n^{1.312} infinitely often … unconditional proof for the range previously known under Selberg" | ✓ |
| D9 Assing–Blomer–Li | arXiv 2005.13915, "Uniform Titchmarsh divisor problems", Adv. Math. 393 (2021) 108076 | ✓ (journal data now verified — remove "per the agent, unverified") |
| E1 Borwein–Choi | PDF: Thm 1.1 p. 154, Thm 2.6 p. 156, Thm 3.1 pp. 156–157, r₃ identity p. 156 | ✓ |
| E2 Elsholtz–Tao | local PDF: Thm 1.1, Props 1.4, 1.6 (odd squares), 1.7 (f(p) ≪ p^{3/5+O(1/log log p)}), Thm 1.8 ((log p)^{0.549}, relative density 1) | ✓ |
| E4 Dyachenko | local PDF | ✓ (Claim 6) |

19 rows checked, ≥ 12 required. **No hallucinated or misattributed paper.** Defects: m8 (Garaev–Karatsuba), m9
(KSWX volume), m10 (cosmetic: add B2′ title, B3 pages; D9 journal now verified).

## Claim 5 — Remark 3.1 (tied averaging): **GAP** (Assessment over-stated; one missed precedent)

(i) *Fairness of "the only free variables at one p are u, C, q, each also the modulus".* Not accurate as stated.
In the hyperbola picture the audit itself uses (B1, §2 ledger, (J)6 §3.4), (★) is
x = 4uC − 1, y = 4BC − 1, xy ≡ 1 (mod 4p), and x, y are free variables **independent of the fixed modulus 4p** —
exactly the untied situation of Shparlinski Thm 13. What is tied is not the averaging variable but the *target*:
the point must satisfy x ≡ y ≡ −1 (mod 4C) with C = (xy − 1)/(4p) its own height. So at one p there *is* an untied
averaging available (over 𝓗), and the obstruction is the height-dependent arithmetic target set, not the absence
of a free variable. The two formulations (tied modulus in (u,C) coordinates; height-dependent target in (x,y)
coordinates) are equivalent descriptions of the same obstruction; the Remark should say so instead of claiming no
free variable exists. → **MAJOR-1** (the Verdict (ii) and §3 item 4 lean on the over-stated form).
Repair: "At a single p, either the averaged variable is itself the modulus of the class condition ((u,C), (u,B),
q coordinates), or — on the fixed-modulus hyperbola 𝓗 mod 4p — the class condition depends on the height of the
point (x ≡ y ≡ −1 mod 4(xy−1)/(4p)). No known theorem handles either a moving tied modulus or a height-dependent
target with error below the main term."

(ii) *Missed untied single-modulus results.* The audit does not cite the one line of work that is literally
"parity breaking, at one fixed modulus, for every residue class, existence":
* O. Ramaré, A. Walker, *Products of primes in arithmetic progressions: a footnote in parity breaking*, J. Théor.
  Nombres Bordeaux 30 (2018) 219–225, arXiv:1610.05804 (abstract checked): for q ≤ x^{1/16}, **every** invertible
  class a mod q contains a product of exactly three primes, each ≤ x^{1/3}.
* B. Szabó, *On the existence of products of primes in arithmetic progressions*, arXiv:2208.05762 (abstract
  checked; Warwick repository version 2024): every invertible class mod q contains a product of three primes each
  ≤ q^{6/5+ε}.
These are pointwise in (q, a), unconditional, and break parity, so they falsify the literal wording of §1D's header
"(all averaged)" and §4's "every existence statement found is averaged (over n, p, moduli or residues)". They do
**not** reach events (a⁴)/(b): the primes are free (untied averaging over primes ≤ q^{6/5}, which actually
*supports* Remark 3.1's thesis), whereas E_b needs primes dividing the one integer K_q (and (a⁴) divisors of p + u).
Also not cited: the Erdős–Odlyzko–Sárközy problem/Shparlinski almost-all results on products of two primes. →
**MAJOR-2** (coverage; verdict unaffected). Repair: add a row D11 (Ramaré–Walker; Szabó) with "gives at a single p:
a product of primes ≡ −1 (mod q) exists, but not one composed of prime factors of K_q; gap = the divisibility
constraint, not size", and amend §1D header and §4 bullet 1 to "averaged, or pointwise in the modulus but over free
primes".
Otherwise the remark's list of averaged results (Garaev–Karatsuba, KSWX §3.3, D2–D7, D1/D6/D8, A3–A5, E2) is a fair
reading of the sources checked in Claim 1. Also not mentioned but harmless: Burgess (fixed modulus, averaging over a
free short interval) — it is used implicitly via E3 (least QNR).

## Claim 8 — Verdict, "gap = p^{1/2}": **SOUND-AFTER-REPAIRS** (verdict stands; the quantitative headline is mis-framed)

The qualitative verdict (H-B not feasible with known inputs; SHARP: none; Assessment label) is supported by
Claims 1–7 and I agree with it. Problems with the *numbers* attached to it:

**MAJOR-3 (the p^{1/2} is not the best known pointwise error for (★), and is not derived as an error for (★)).**
(a) (u,B,C) ↦ (x,y,z) = (uBC, pBC, puC) is an injective map into Type II solutions of 4/p = 1/x + 1/y + 1/z
(check: 4/p − 1/(uBC) = (u+B)/(p·uBC)); hence R(p) ≤ f_II(p) ≪ p^{2/5+O(1/log log p)} (Elsholtz–Tao Prop 1.7,
verified in the local PDF) and therefore, with no cancellation at all,
  |E(p)| = |R(p) − M(p)| ≪ p^{2/5+o(1)}.
So the "best known pointwise error scale" for (★) is already p^{2/5+o(1)}, *smaller* than the Weil scale
p^{1/2+o(1)} that §2 ("Answer…") and Verdict (ii) present as the closest pointwise estimate. (Even the naive bound
R ≤ 2Σ_{u ≤ √p/2+1} τ(p+u) gives p^{1/2+o(1)}, i.e. the "Weil gap" is no better than counting divisors.)
(b) No derivation is given (here or, as far as I can see, in (J)6 §3.4) that Thm 13 yields |E(p)| ≪ p^{1/2+o(1)}:
(★) is not a box count on 𝓗; splitting by height C produces ≍ p sub-counts, each with Weil error p^{1/2}. The
p^{1/2} is the error of a *single box count* on 𝓗 — a benchmark of the method, not a bound for E(p).
Repair: in §2 (Assessment 2.2, ledger row 1, "Answer…") and Verdict (ii) replace "error ≍ p^{1/2} against
(log p)²" by: "the best known pointwise bound is |E(p)| ≪ p^{2/5+o(1)}, from the divisor bound (ET Prop 1.7) with
no cancellation; the best class-aware *cancellation* tool, Weil on 𝓗, has error p^{1/2+o(1)} even for a single box
and does not by itself bound E(p). Either way the shortfall is a power of p." Also: "≍ p^{1/2}" with a
p^{o(1)} error should read p^{1/2+o(1)} (§2 Answer, Verdict (ii); minor m11).

**Minor (m12).** Verdict (iii) "for complete-sum methods the restricted events are no easier than (★) (Lemma 2.1)"
— Lemma 2.1 only shows the (u,C) trial set stays ≍ p log U; restate as "in the (u,C)/(u,B) parametrisation" (cf.
m3).
Checked and fine: §3 item 2 (p = 173, q = 7, K = 45: 5·9⁻¹ ≡ −1 (mod 7), no divisor ≡ 6 ✓; the "(q−1)/2"
obstruction ✓; Ω(K_q) ≤ log₃ p, so the stated log₂ is safe); Remark 5.1 ((u/p) = +1 for u ≤ 7 when p ≡ 1 (840) ✓;
CONJECTURE label ✓); Graham–Ringrose/Montgomery are correctly flagged "from memory".

