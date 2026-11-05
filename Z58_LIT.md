# Z58_LIT — 2024–2026 literature, verified, read against (MS) and the z58 falsifiers (wave z58, lane LIT)

**Status: CHECKPOINT 1 (2026-11-05).** ES is OPEN; nothing here proves or disproves it. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Literature statements are quotations from the opened source (theorem
number quoted) unless marked "abstract only"; proofs of cited papers are not re-checked; preprints are unrefereed unless a
journal is named. Source notes: `data/z58/lit/`. Repo arXiv-id snapshot for novelty checks:
`data/z58/lit/repo_arxiv_ids.txt` (1685 ids grepped from *.md/*.txt/*.tex on 2026-11-05).

Prior sweeps NOT repeated here (git-grepped first): `LITERATURE_2026.md` (to 2026-09-28 + Waves Y/Z/AA/z52),
`LITERATURE_2026_UPDATE.md` (2026-10-21), `Z53_LIT.md` (to 2026-11-01: divisors in classes/intervals, modular hyperbola,
Kloosterman, EOS, Zaremba, (J)103 table), `Z56_K4LIT.md`, `LITERATURE_AUTOMORPHIC.md`, `BRAINSTORM/z52_lit_*.md`. This lane
adds (i) a refresh 2026-11-01 → 2026-11-05 and a refereed-status audit, (ii) the items in brief (b)/(c) that those sweeps did
not open, and (iii) — new in z58 — every relevant mechanism read through the mandatory falsifier table.

## 0. MANDATORY FALSIFIER TABLE (literature mechanisms; Assessment unless labelled)

Screens (data `data/z58/screens/`): **F1** R(m²) = 0 for odd m; **F2** R₈ (C-even sub-line) has 12 prime zeros in
[10¹⁰, 1.1·10¹⁰], 4 in 𝔐; **F3** 285 non-square composite zeros n ≡ 1 (4) ≤ 7 999 801; **F4** 14 (★)-zero primes (last
8 813 281, 9 in 𝔐), 38 𝔊*-zeros (last 564 661 441).

*New screen data (CERTIFIED, from the screen file, `awk`/`factor`):* the composite zeros do not thin out — per half-decade
[10^k, 10^{k+1/2}) the counts are 12, 12, 25, 35, 45, 50, 62 for k = 3, …, 6, and 35 in the partial bin [10^{6.5}, 8·10⁶].
71 of the 285 are ≡ 1 (mod 24); **15 lie in Mordell's classes 𝔐**, the largest 3 210 601 = 19·37·4567; the others are
1969 = 11·179, 2641, 5161, 18001, 23881, 90889, 112849, 199369, 345361, 349609, 510169, 539281, 897961, 2956321 = 211·14011.
*Consequence (Assessment, EVIDENCE-based):* any mechanism of the shape "every non-square n except a finite sporadic set"
(Rickards–Stange Thm 2.8 shape) is falsified by F3 as a model for R unless it uses primality: the composite zeros look
infinite (≈ steady growth per half-decade), and they occur inside 𝔐 too, so restricting to Mordell's classes does not
remove them.

| mechanism (literature) | what it proves, pointwise? | F1 odd squares | F2 C-even line | F3 composites | F4 known zeros |
|---|---|---|---|---|---|
| Divisors in classes/intervals (Erdős–Hall, Tenenbaum, Ford, FGK, Koukoulopoulos–Tao) | almost-all n / mean values; pointwise only upper bounds (Lenstra) | invisible (squares density 0) | invisible | invisible (allows exceptional sets) | allows them | 
| Shifted primes p + a: divisor/prime-factor statistics (Titchmarsh divisor problem, BV/BFI) | averages over p | invisible | invisible | n/a (counts primes only, but averaged) | allows them |
| Least prime in AP, explicit Linnik (Xylouris; Bennett–Martin–O'Bryant–Rechnitzer) | pointwise, explicit; produces a *free* prime in a class | not engaged (free prime, no tie to n) | not engaged | not engaged | not engaged — supplies no divisor of p + u |
| Least (prime) QNR: Burgess, GRH (LLS), Pollack (q ≡ 3 (4)) | pointwise | **native**: a non-residue exists iff n is a non-square | blind | **fails**: every non-square composite has one too | proves a *necessary* condition only (every witness d has ℓ | d with (p/ℓ) = −1) |
| Brauer–Manin on ES surfaces (Bright–Loughran; Yamamoto; EST Prop 1.6) | obstruction side; no BM obstruction to ES existence | **explains** T1 (reciprocity) | ? (to check: does BM see the C-even sub-family?) | expected *not* to obstruct at the 285 composites ⇒ "BM is the only obstruction" for the (★) surface would be false (STRUCT lane) | same |
| Thin-orbit / reciprocity local–global (Rickards–Stange Thm 2.8; HKRS; Alkauskas fleas) | every non-square except finitely many (RS, fat case PROVED) | **native** | blind | **fails** (F3 data above: composite zeros not finite-looking) | finitely many sporadic — wrong shape for 14 + 285 |
| Legendre descent: x² − py² = −1 for every prime p ≡ 1 (4) | pointwise, rigid, every p | native (impossible at squares) | n/a | **uses primality** at the factorisation step (x−1)(x+1) = py² | **fails**: no threshold, would "prove" R(p) ≥ 1 at 8 813 281 if ported verbatim |

*Reading (Assessment, checkpoint).* F1 is passed by every T1-native mechanism (characters, reciprocity, Pell); F3 kills all
of them except those that use primality at a rigid step (Legendre-type), and F4 kills rigid steps without a size threshold.
A literature mechanism that survives all four would have to be **prime-specific AND threshold-bearing** (an analytic count
with an error term at one prime, or a size squeeze à la Chebyshev/Zsigmondy). The brief's item (c) search is therefore
narrowed to: *pointwise theorems for primes that fail for composites and have finitely many small exceptions*. This is the
search target handed to the research subagents.

## 1. Precise questions (unchanged brief, sharpened)
* **Q1 (ES 2024–2026).** Every ES / Egyptian-fraction research item 2024-01-01 → 2026-11-05: what it claims, version, refereed?
  Specific: Mihnea–Dumitru 2509.00128 (10¹⁸), Akaka Zenodo, Lean formalisations (formal-conjectures #242, sushaan-k,
  carlok, auro-zera, leochlon), function-field ES, and anything after Cao–Xu 2610.32302 (2026-10-23).
* **Q2 (single-integer existence).** Pointwise results: n has a divisor in a class/interval; shifted primes p + a with a
  divisor/prime factor in a class; least prime/solution in APs with explicit constants; integral Hasse principle /
  strong approximation for affine cubic and log K3 surfaces with an every-parameter conclusion; function-field ES.
* **Q3 (structures obstructed at squares).** Theorems giving existence at each large n (or each large prime) of a
  structure obstructed at squares — and, per §0, especially ones that fail at composites and have small exceptions.

## 2. First finding (checkpoint 1)
The §0 F3 data (CERTIFIED counts) plus the table: the "squares + finitely many" thin-orbit shape is not a model for R; the
rigid Legendre shape is not a model either (F4). Search narrowed accordingly (§0 reading). Research subagents launched on
Q1, Q2 and Q3; results to `data/z58/lit/`.
