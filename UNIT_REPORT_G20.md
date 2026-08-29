# UNIT G20 report — paper v6

## Outcome

Absorbed source notes §§51–53 into `paper/espaper.tex` and advanced `paper/README.md` to v6 (2026-08-29, wave 20). The paper is a 66-page source-only consolidation; the v6 queue is cleared and the v7 queue names sibling-wave §§54–55.

## Paper changes

- Added the witness-modulus section: exact `W(p)` definition; parameterized truncated assembly; both master-tail variants and windows; polylogarithmic tails; `H_MOD(A)` and its nonimplication relation with `H_SPF(A)`; PW truncation credit; Dahan cubic-shape priority; Vaughan-access caveat; and the blind protocol/adjudication.
- Added the effectivity chain: Lenstra–Pomerance JEMS 2019 Lemma 11.2 in its direct-corollary scope, induced-character accounting, single-dyadic-conductor selection, conductor-deletion tolerance, effective downstream class supply, and the exact ancillary-`o(1)` exclusion.
- Added the proved fixed-slice sieve: exact exponent `1+2/phi(4ck)`, elementary remainder, effective fixed-slice scope, the no-third-congruence-law corollary, and the proved but ineffective polylog-uniform Siegel–Walfisz proposition.
- Preserved the §52 finite register: composite witness shapes include semiprimes, three-or-more-factor products, and prime powers; the displayed stable anticorrelations prevent a blanket independence claim.
- Added the stacked sieve: duplicate-radicand quotient and `(5,2)/(20,1)` example; corrected mass `m_#(C)`; fixed-box exponent `1+m_#(C)`; exact independent genus bits; permission-pair mass; the uniform-in-dimension Friedlander–Iwaniec beta-sieve input; Landau–Page-deleted Siegel–Walfisz; the effective growing theorem and almost-all `H_SPF` corollary.
- Updated the abstract, introduction, §50 frontier, internal review pedigree, end-status register, and bibliography. Added Dahan, Friedlander–Iwaniec, and Lenstra–Pomerance; no Xylouris/Heath-Brown or unsupported explicit-Chebyshev citation was added.
- Registered verifier blocks `(ax)`–`(az)`, all three hostile reviews, and the §51 maximum-severity adjudication.

## Fidelity judgments

- Every displayed `W` tail counts primes only. The fixed-polylog variant is unconditional only in the no-unproved-hypothesis sense and retains the §39 review qualification; the cubic variant inherits source Theorem 34.8/paper `thm:pruned` and remains **CLAIMED/PROVISIONAL**.
- Source Theorem 51.6 is explicitly record-adjacent **CLAIMED/PROVISIONAL**. It effectivizes class-supply conclusions and Theorems 16.4/39.7/51.2, not Theorem 34.8's ancillary absolute-error `o(1)` over all low-congestion triples.
- Dahan is credited immediately at the cubic polylog tail as an exponent-shape antecedent for a different two-parameter statistic with an ineffective printed error. No priority equivalence with `W` is claimed.
- Source Theorem 52.1 and Corollary 52.2 are proved and nonprovisional; fixed-slice constants are effective in principle. Proposition 52.3 remains proved but ineffective and is not used as a naive growing stack.
- Duplicate radicands are quotiented before the fixed-stack exponent. The growing theorem uses distinct canonical squarefree-core radicands, exact CRT genus independence, the reviewed large-dimension fundamental lemma, and the no-exception branch deletes nothing.
- Source Theorem 53.3 and Corollary 53.4 are proved and effective. The corollary uses the repaired `A'<A` inclusion on top dyadic intervals.
- The Type-I/Type-II asymmetry is preserved: Type II has no genus-permission gate; Type I pays the square-root penalty through escape classes. No pointwise `H_MOD`, pointwise `H_SPF`, conspiracy-depth bound, parity-breaking lower bound, or proof of Erdős–Straus is claimed.
- Blind adjudication remains **CONVERGED-WITH-DIVERGENCES**; the blind-side overclaim was rejected and no correctness label changed.

## Validation

- `pdflatex -interaction=nonstopmode -halt-on-error espaper.tex` ×2: clean, 66 pages, zero TeX errors, zero undefined references/citations.
- Control bytes / CR / NUL: zero. Eaten-`\\r` (`{` + newline + lowercase), `egthickspace`/bare-`nmid`, and line-fragment corruption scans: zero. `git diff --check` is clean.
- Label/citation audit: no duplicate labels and no missing bibliography keys.
- `uv run --with sympy,numpy,scipy python verify.py`: all checks passed through `(az)` in one foreground run.
