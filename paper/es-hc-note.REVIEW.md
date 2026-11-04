# es-hc-note — review record (lane PAPERHC, wave z56)

Paper: `paper/es-hc-note.tex` / `.pdf` (21 pp.), "The least certificate coordinate for the Erdős–Straus
equation at a prime: a two-shift reduction, partial sieve results, and covering obstructions".
**ES is open; the note proves no case of it beyond what is stated.** Nothing has been posted.

## 1. Sources and what was re-derived

Material written up (each proof re-derived while writing, not copied):

| Paper item | Source memo | Notes on the rewrite |
|---|---|---|
| Lemma 2.1, Prop 2.2 (coordinate in 𝒞_n ⟺ one of t,u,v,A,A* divisible by 4; five explicit identities) | `LOWERTAIL_ROUND2_FABLE.md` §1.1 Thm 1 (coordinate form) | Made self-contained: the original relied on FOREST_DEEP_FABLE Thm A (Jacobi form); the paper proves both directions 2-adically and states the five identities explicitly (all checked symbolically and numerically). |
| Lemma 2.3 (lines), Prop 2.6 | `Z53_UPPER.md` L1.1, L1.2, P2.1 | as source |
| Lemma 2.7 (reciprocity) | `Z53_UPPER.md` L3.1 / `Z54_UPPER2.md` Lemma J | Generalised to all positive n ≡ 1 (4) (coprimality is a conclusion, not a hypothesis); gives HC(m²) = ∞ (Cor 2.8). |
| Prop 3.1 (HC ≤ 8 outside Mordell's classes) | `Z54_UPPER2.md` Prop 3.1 | as source |
| Lemma 4.1 (K(4) ⟺ P(4,15)), Remark 4.2 (det-15 shell), Theorem Q | `Z54_HCKILL.md` Lemma 1.1, Remark 1.3, Thm Q | as source |
| Prop 4.8 (#{HC > 4} ≪ x/log²x) | `LOWERTAIL_ROUND2_FABLE.md` Thm 3.2 | re-proved with Ford Thm 2.4 (dimension 2) |
| Theorem E (CONDITIONAL on EH(1 − η₀)) | `Z54_HCKILL.md` §3.1 (+ REVIEW_HCKILL audit) | Step 4 written with Ford Thm 2.4 (remainders only to d ≤ w) |
| Theorem U (unconditional half of P(4,15)) | `Z55_P415.md` §1 (+ REVIEW_P415) | **Proof simplified**: the switched term now uses an integer-k sieve (dimension 5/2) instead of BV for primes (BV is used only in the vector-sieve main term); the m-sum uses an Euler-product bound plus partial summation instead of Shiu's theorem; the beta-sieve facts F ≥ 1 ≥ f, F decreasing, F − f ≤ 1.51 s^{-1/2} are derived (Lemma 4.7) from the delay equations and V⁻ ≤ V ≤ V⁺, so no unverified "F, f → 1" citation is needed. Explicit choice S₀ = ⌈22801/η⌉, δ = η/(8S₀). Model numerics (δ ≈ 0.031, Ω_𝒬 ≤ 10) deliberately **not** included (unaudited Assessment in the memo). |
| Prop 5.1 (Dickson ⟹ HC unbounded), Theorem W | `LOWERTAIL_ROUND2_FABLE.md` Prop 3.3(a); `Z53_HCSHIFTS.md` Thm W | Theorem W restated with the minimal hypothesis (only the U-lines at x ∈ 4ℕ are used) |
| Theorem N, Cor 6.1 | `Z55_HCF.md` Thm 3.1, Cor 3.2 | notation changed (Λ for the set of primes, 𝒯 for the small primes) |
| Computation 7.1 (HC ≤ 64 below 10¹²) | `Z55_HCO.md` C3.1 | checks listed; see §3 below |

Scope choices: HCF Prop 3.4 / Z53 P3.3 (Linnik-type obstructions) appear only as a one-line argument in Open
Problem 4; HCKILL F1–F6, P415 Lemmas A1–A2 and Prop C, HCO E4.x, HCSHIFTS model computations are not included
(heuristics/model statements or tangential). Every scope restriction of the memos' cross-model reviews was kept
(e.g. Theorem W bounds the *certified* window, not HC; Theorem N excludes fixed finite families only; Theorem E
is conditional; the 10¹² census was not fully recomputed independently).

## 2. Citations and literature

* `paper/es-hc-note.citecheck.md` (research subagent): primary-source check of Nath–Xie, Ford, Friedlander–Iwaniec,
  Rosser–Schoenfeld, Elsholtz–Tao, Salez, Mihnea–Dumitru, Linnik constants. Its corrections were applied
  (FI 2009 Thm 4 is the r(n−2)r(n+2) statement; Nath–Xie v3 has Ω(p+2) ≤ 9; ET Prop 1.6 is the odd-square
  vanishing, Type II characterisation is Prop 2.7). I re-read myself: NX v1/v3 (3.4), Lemma 3.6, Prop 3.10,
  (4.3), §5; Ford Thm 2.4 and the (Ω) condition, Thm 3.4, (7.6), Conj 7.3; ET p. 8 (mod 840) and Prop 1.6, 2.7;
  López arXiv:2404.01508 Defs 3–4, Thms 4, 7, Conj 1. Shiu and Rosser–Schoenfeld are no longer cited.
  Friedlander–Iwaniec *Opera de Cribro* Thm 11.12 is cited only as quoted by NX (stated in the paper).
* `paper/es-hc-note.litcheck.md` (research subagent): priority search (arXiv/web only). No prior statement of
  Theorems Q, E, U, N found; closest: FI 2009 (analogue of E), Nath–Xie (method of U), López 2024 (the 4ℕ part of
  the certificates = his Types A/B and his Conjecture 1 — now cited in Remark 2.5), Salez/Mihnea–Dumitru (ES
  verification to 10¹⁷/10¹⁸, so the census is not an ES verification record). The novelty statement in the paper
  is limited to "we did not find …" with the search scope stated.

## 3. Numerical checks

* `paper/es-hc-note.check.py` (new, independent of the memo code; `uv run --with sympy`, ~10 s): Prop 2.2
  equivalence and all five identities on every word of every n ≡ 1 (4) < 1200 (11 709 words); Lemma 2.3 on all
  c ≤ n+2; HC via lines = HC via words; Lemma 2.7 on 17 893 certificate divisors of all n ≡ 1 (4) < 3000
  (composites included); odd squares; HC = 3 / HC = 4 criteria and Prop 3.1 for p < 2·10⁵; Theorem Q members;
  recomputation of the 12 census records with HC ≥ 52; random Theorem N samples (probable primes, evidence).
  Output: ALL CHECKS PASSED.
* Census: reran `scripts/z55_hco_census.c` on [0, 10⁹) — histogram identical to the independent program
  `scripts/z54_upper2_hc.c` (`data/z54/upper2/hc_1e9.txt`) — and on the last block [9.52·10¹¹, 10¹²) — output
  identical (sorted) to the archived block. Transcript and commands: `paper/es-hc-note.census-rerun.txt`.

## 4. Hostile referee (deep-mode subagent)

Full report: `paper/es-hc-note.referee.md` (reviewed commit `fa3e7a12`). Recommendation: revision required; **no
FATAL issue**; one MAJOR. The referee re-derived every proof (Theorems E, U, W, N step by step, including the
uniformity of the absolute constants in E and U and the remainder bookkeeping), checked all cited statements in
freshly downloaded sources, re-ran the check script, the 126-record verification and the census below 10⁹.

Responses (all applied in the commit after `c0659b5f`):

1. **MAJOR — §5, claim "the Dickson primes are ≡ 1 modulo every prime ℓ ≤ X+1, so log p ≥ (1+o(1))X" is
   false** (Q = lcm(24, x(x+1) : x ∈ 𝒞_X) misses primes ≡ 3 (8) in (X/3, X+1]; explicit counterexample X = 10,
   p = 147 223 441 ≡ 2 (11); log Q ~ 5X/6). *Accepted.* This was my error (it regressed a correction already
   made in the HCSHIFTS review). Replaced by the provable statement: Q is divisible by every prime ℓ ≤ X/4
   (as 4ℓ ∈ 𝒞_X), so log p > (1/4 + o(1))X, and "Theorem W shows that a restriction of this type is forced".
   Proposition 5.1 and Theorem W were unaffected.
2. **MINOR — "solutions of Prop 2.2(c) are Type I or II" is false for composite n** (n = 129, word (4,3,12)), and
   ET Prop 2.7 needs abd coprime to n. *Accepted.* Now stated for primes only, with the coprimality condition and
   the identification (a, b, d) = (u, v, t/4).
3. **MINOR — the quoted vector-sieve theorem did not state 0 ≤ h ≤ 1.** *Accepted;* added "0 ≤ h ≤ 1, h(1,1) = 1".
   The remark that zero values are allowed (NX's own (4.3) uses them; the proof only uses h ≥ 0) stays.
4. **MINOR — computational provenance.** *Accepted.* §7 now lists the program, its c < 4000 cap and failure
   reporting, the block outputs, aggregation/tiling check, prime count, record verifier, the independent 10⁹
   program, and the rerun transcript `paper/es-hc-note.census-rerun.txt` (which the referee had not seen). The
   statement that the full 10¹² range was not independently recomputed is kept.
5. **MINOR — domains.** *Accepted.* Positive n in the abstract and Definition 2.4; "all sufficiently large primes
   p ≡ 1 (mod 4)" and finite-valued F in the introduction and Problems 3–4, with the remark that p ≡ 3 (mod 4) is
   classical.
6. **TYPO — "class consisting of squares".** *Accepted:* "primitive residue class r mod q with r a square".
7. **TYPO — "Theorems Q and E are conditional".** *Accepted:* "the infinitude consequence of Theorem Q and the
   conclusion of Theorem E are conditional".

The referee's small remarks were also handled: Theorem W now states e_{x,i} ∈ ℕ explicitly. (The referee noted
that Ford's Thm 2.4 is printed on p. 18 of the current PDF; the paper cites theorem numbers only.)

## 5. Residual caveats (for the user)

* Theorems E and U are proved *relative to* the quoted sieve theorems (Ford Thm 2.4; NX Lemma 3.6/Prop 3.10, the
  latter quoting FI *Opera de Cribro* Thm 11.12, which nobody here inspected directly). η₀ and δ are not
  computed.
* Internal checks only (one hostile deep-mode referee + the earlier per-memo internal and cross-model reviews);
  not externally refereed.
* The census is a computation by one program, with the cross-checks listed in §7; not a proof-grade certificate
  of the full range.

## 6. Cross-model referee (z56 XREF)

Report: `paper/es-hc-note.XREFEREE.md` (reviewed commit `22bcb876`). Recommendation **minor revision**; every
result classified CORRECT (conditional theorems relative to their hypotheses; the census as computational
evidence); no GAP/WRONG. Required changes and their handling:

1. **Yamamoto attribution (Lemma 2.7 / Cor 2.8).** *Applied.* After Cor 2.8 the paper now says that Lemma 2.7 and
   Cor 2.8 are Yamamoto's quadratic-character obstruction [Yamamoto, Lemma 4] written for the two certificate
   lines, that 2.8(a) corresponds to his Theorem 2 (perfect squares excluded), that he lists the six classes
   mod 840 (§3), and that the only new feature is the statistic HC. The introduction now names Theorems E, U, N
   as the main contributions and §§2–3 as infrastructure (Yamamoto's obstruction, López's 4ℕ-coordinates).
   (Yamamoto's lemma/theorem numbers are taken from the referee's OCR inspection; I did not re-inspect the scan.)
2. **Failure exit status of the census tools.** *Applied via a checked wrapper* (the scripts under `scripts/`
   belong to earlier lanes and are left untouched): `paper/es-hc-note.census-check.sh` exits nonzero on a
   checksum mismatch, any nonzero `fail:` counter or `FAIL` line, a tiling/histogram inconsistency
   (`z55_hco_aggregate.py` asserts), totals differing from those printed in the paper, a π(10¹²) mismatch, or
   any bad record in `z55_hco_verify.py` (whose last line is parsed); `RERUN=1` also recompiles and reruns
   [0, 10⁹) and compares bin by bin with the independent program. Run on this commit: CENSUS CHECKS PASSED.
3. **η fixed before x → ∞.** *Applied* in the proofs of Theorems E and U: x₀, o(1) terms, sieve/EH error
   constants and log z₁ ≍ log z₂ may depend on the fixed parameters; only the main- and switched-term constants
   used to choose η are absolute.
4. **Stable supplement.** *Partially applied.* `paper/es-hc-note.supplement.sha256` is a SHA-256 manifest of the
   census program, aggregator, verifier, prime-count program, independent 10⁹ program and all block outputs;
   §7 lists the files, the wrapper and the manifest, and states that a stable public archive must accompany any
   submission and has not been made (nothing is posted; that is the user's decision).

Minor comments: "the strongest story is E/U/N" — agreed, stated in the introduction (see 1). "Shorten repeated
warnings, move computational detail to the supplement" — not done beyond that: the scope statements are kept
deliberately, and the computational section is already short (≈1 page). "Explicit δ unnecessary", "cosh²(1/2)
correctly scoped" — no change needed. HAL-04994962 (inaccessible to the referee) — not cited.

Akaka, Zenodo 22754703 (`LITERATURE_2026.md` §2.4; an unrefereed almost-all-primes lower bound
R_II(p) ≥ c(log p)³ for strict solution counts): concerns solution *counts* on a density-one set of primes,
which this note does not study (its density statements concern HC > 4, i.e. the two-shift event, and the
census concerns HC). No positioning is needed here; it is relevant to the count note (PAPERCOUNT), not this one.
