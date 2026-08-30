# UNIT I21 report — paper v7

## Outcome

Advanced `paper/espaper.tex` to v7 (74 pages) and absorbed reviewed source §§54–55 plus the auro-zera/Dyachenko related-work register.

- Added the proved, effective Type-II and Type-I logarithmic lower tails, including Xylouris exponent 5.2, the `1/5.2` limsup constants, and the refutations of `H_MOD(A)` and `H_SPF(A)` for every `0 < A < 1`.
- Added the two-sided frontier: almost-all polylog-to-epsilon scale, effective `c log p` infinite lower tail, and an expressly conjectural logarithm-squared-like ceiling/data-guided `[1, ~2]` window.
- Added the general-`m` witness statistic, both truncated tail windows, top-window consistency, polylogarithmic corollary, PW comparison, and finite companion.
- Added the exact `m`-uniform Page-conductor repair. The favorable-sign result is limited to the full Layer-1 family and structured `c`-free fibres; arbitrary sparse subfamilies are expressly excluded. The effectivity table preserves every inherited **CLAIMED/PROVISIONAL** label and excludes the ancillary all-triples error assertion.
- Updated the abstract, introduction, earlier pointwise-hypothesis discussions, verification pedigree through blocks `(ba)`–`(bb)`, bibliography, and `paper/README.md`. The v8 queue now names sibling-wave §56.
- Added Dyachenko's ED2 identity as a conditional-characterization-aware cousin and recorded the auro-zera Lean file as a sound identity/case-split formalization whose one axiom is the open core; compilation remains unverified and no paper result depends on it.

## Validation

- `pdflatex -interaction=nonstopmode -halt-on-error espaper.tex` twice: 74 pages, zero TeX errors, zero undefined references or citations.
- `uv run --with sympy,numpy,scipy python verify.py`: all checks passed through `(bb)` in one foreground run.
- Control bytes, CR/NUL, eaten-backslash/corruption species, duplicate labels, and missing bibliography keys: zero.
- `git diff --check`: clean.
- Generated PDF and auxiliary files were restored to the repository snapshot after validation; only source/documentation changes are committed.
