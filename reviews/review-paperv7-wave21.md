# Paper v7 wave-21 fidelity review

**Overall verdict: FAITHFUL.**  I found no transcription, scope, status, or contamination defect in the v7 absorption.  No fidelity repair was needed.  The TeX preserves the repaired source states of §§54–55, the external-context caveats, and every inherited provisional label.

## Severity-ranked defects

- **Critical / high / moderate / low:** none.
- Consequently there is no TeX/notes defect-line pair to report and no `% wave-21 fidelity repair` marker was added.

## 1. §54 absorption — PASS

- Theorem 54.1 retains the full-lcm construction over every product `k ell`, including composite `ell`; `M(T)`, `log M(T)=psi(floor T)`, the residue-one contradiction, unbounded selected primes, and the `1/5.2` limsup are exact (`paper/espaper.tex:3922-3960`; `notes.md:20145-20201`).
- The Linnik register is correctly **effective**, not numerically explicit: Xylouris supplies exponent `5.2` and an effectively computable constant/threshold; the paper expressly extracts no numerical `C_0` (`paper/espaper.tex:3956-3959,4053-4060`; `notes.md:20195-20201,20325-20336`).  The separate Rosser–Schoenfeld inequalities are correctly called explicit Chebyshev bounds.
- Corollary 54.2 has the pointwise quantifier needed to refute `H_MOD(A)`: infinitely many unbounded primes violate the eventual-every-prime assertion for each fixed `0<A<1`.  It does not refute `A=1` (`paper/espaper.tex:3963-3989`; `notes.md:20203-20237`).
- Theorem 54.3 retains the exact squarefree-prime construction `R(T)`, all even/sign discriminant factors via modulus 24, every-slice vanishing through `ck<=T`, admissibility from `R(T)>4T`, both `ck_pr` and `ck_min`, and the same effective Linnik scale (`paper/espaper.tex:3992-4034`; `notes.md:20239-20302`).
- Corollary 54.4 has the correct hard-prime and every-slice quantifiers.  It refutes `H_SPF(A)` for every `0<A<1`, leaves `A>=1` open, and distinguishes actual genus-forced zero mass from the earlier fixed-divisor non-guarantee (`paper/espaper.tex:4037-4051`; `notes.md:20304-20323`).
- The proved sandwich is exactly “almost-all polylog-to-epsilon typical / effective `c log p` infinitely often extremal.”  The `[1,~2]` panel is visibly data-guided and conjectural; the paper neither identifies the three depth statistics nor promotes the log-squared-like ceiling to a theorem (`paper/espaper.tex:4062-4091`; `UNIT_REPORT_I21.md:8`; `reviews/external-auro-zera-lean-wave20.md:84-94`).  No numerical fit, finite-census ratio, or §56 value is imported.

## 2. §55 absorption — PASS

- `W_m`, `lambda_m`, `theta_m`, both truncated assemblies, both master-tail windows, the top-window consistency checks, and the polylogarithmic corollary agree with source §55.1 (`paper/espaper.tex:4093-4227`; `notes.md:20346-20538`).  Prime scope is restored in both variants.
- The Layer-1 result keeps the §39 review qualification and does not inherit Theorems 34.8/43.7.  Every cubic occurrence remains **CLAIMED/PROVISIONAL**, including the Theorem 43.12 recovery (`paper/espaper.tex:4096-4101,4130-4153,4189-4193,4211-4223`; `notes.md:20348-20354,20396-20429,20460-20511`).
- The progression modulus is literally `q=muv`.  All three conductor cases are present, including shared-but-incomplete prime powers when `r` does not divide `m` (`paper/espaper.tex:4230-4280`; `notes.md:20540-20602`).
- The wave-20 maximum-severity narrowing is preserved character for character in scope: when `r|m`, the favorable-sign argument proves aggregate mass only for the full Layer-1 multiplier family and the structured `c`-free fibres `J_c`, never arbitrary sparse subfamilies (`paper/espaper.tex:4253-4261,4299-4319`; `notes.md:20581-20589,20639-20666`).
- The worst-case correlated fibre subtraction (55.17b), the formal unfavorable `k=1` bookkeeping, low-omega deletion, and low-congestion pruning are all present (`paper/espaper.tex:4300-4314`; `notes.md:20639-20658`).
- The effectivity perimeter table retains all three rows and every inheritance label.  The conductor split is stated immediately after the rows; the cubic rows effectivize only surviving class mass, and the ancillary all-low-congestion-triples absolute-error assertion remains excluded (`paper/espaper.tex:4321-4354`; `notes.md:20668-20706`).
- The Pomerance–Weingartner comparison separates unrestricted formal crossover from the actual fixed-power uniform window, states that PW is proved while the cubic side is provisional, and disclaims finite crossover, pointwise progress, and range extension (`paper/espaper.tex:4356-4373`; `notes.md:20707-20746`).  The finite `(bb)` companion is informational and its entries agree.

## 3. External context — PASS

- The auro-zera paragraph is neutral and precise: sound identity/case-split layer, one `good_divisor_exists` axiom at the open core, local compilation unverified, and no paper dependence (`paper/espaper.tex:184-196`; `reviews/external-auro-zera-lean-wave20.md:18-24,44-64,104-108`).
- Dyachenko is used only at the identity/conditional-characterization level.  The paper quotes the substance of his own Conclusion: the infinite general case is not constructively proved and the finite-covering argument is conditional (`paper/espaper.tex:189-196,304-309,4715-4721`).  Direct extraction from `sources/dyachenko-2511.07465.pdf` confirms that wording.
- The text says §§51–54 quantify what the axiom assumes and makes no campaign-priority claim, no polemic about the formalization, and no theorem dependency on either external artifact.

## 4. Global consistency — PASS

- The abstract’s new sentence has the exact register: effective infinite lower tails, refutation only for `0<A<1`, and exactly `A>=1` left open (`paper/espaper.tex:68-74`; `notes.md:20134-20208,20304-20316`).
- Every earlier `H_SPF`/`H_MOD` frontier passage carries the same sharpening (`paper/espaper.tex:2834-2840,3064-3071,3264-3280`).  Greps found no stale statement that all `A>0` remain open; unrelated `A>0` definitions and almost-all bounds remain legitimate.
- The provisional record register is intact in the abstract/status map and in paper Theorems corresponding to source 34.8, 43.7, 43.12, the cubic witness tail, and the effectivity statements (`paper/espaper.tex:50-67,173-180,1386,2358,2462-2463,3189-3220,3360-3386,4321-4354`).
- The pedigree accurately records both wave-20 reviews, their repaired verdicts, blocks `(ba)`–`(bb)`, the narrowed family scope, and the external review’s uncompiled status (`paper/espaper.tex:2090-2102`).
- Required bibliography entries are real and cited: Dyachenko (`:190,304,4715`), Xylouris (`:3957,4054,4793`), Heath–Brown (`:4055,4744`), and Rosser–Schoenfeld (`:4057,4767`).  Static checking found 20 citation keys, no missing item, no uncited item, and no duplicate label.

## 5. No contamination — PASS

- `paper/espaper.tex` has no `56.*` tag, theorem/section 56 reference, congruence-certificate ceiling, `P_3(T)`, §56 record value, full-scan extension, or (56.16) finite-search panel.
- In particular, none of `383`, `2495`, `954409`, `2031121`, `171481`, or `414241` appears in the TeX.  The v7 frontier contains only the pre-§56 qualitative search window.
- `paper/README.md:10-20` accurately describes v7.  Source §56 appears in the paper metadata only in the v8 queue at `paper/README.md:124-126`.

## 6. Formula-level transcription audit — PASS

The following were checked character by character, allowing only TeX-equivalent spelling (`\lcm` versus `\operatorname{lcm}`, `\frac` versus `\over`) and harmless layout compression:

| Formula / load-bearing item | Paper | Notes / source | Result |
|---|---:|---:|---|
| `M(T)` and `log M(T)` (54.1) | `3924-3927` | `20149-20152` | exact |
| `A<1` contradiction display | `3970` | `20208` | exact constants, order, quantifier |
| `R(T)` and `log R(T)` (54.6) | `3994-3998` | `20243-20247` | exact |
| Type-I logarithmic box (54.10) | `4042-4044` | `20308-20311` | exact |
| proved typical/extremal sandwich (54.11) | `4067-4073` | `20203-20237` | exact synthesis of proved sides |
| data-guided frontier panel (54.12) | `4082-4085` | `UNIT_REPORT_I21.md:8` | exact `[1,~2]` register; conjectural |
| general-numerator datum (55.3) | `4114-4118` | `20374-20378` | exact congruences and factorization |
| both master windows (55.11) | `4183-4190` | `20473-20483` | exact exponents and inequalities |
| displayed exceptional term (55.15) | `4238-4246` | `20559-20566` | exact sign, indicator, maxima, range |
| favorable full-family mass (55.17a) | `4292-4294` | `20632` | exact |
| adversarial fibre subtraction (55.17b) | `4301-4306` | `20642-20646` | exact supports and signs |
| effectivity perimeter rows (55.18) | `4325-4338` | `20673-20691` | all rows and inherited labels intact |

No sign, exponent, denominator, modulus, range, status label, or family quantifier drift was found.

## 7. Build, verifier, and hygiene — PASS

- Ran `pdflatex -interaction=nonstopmode -halt-on-error espaper.tex` twice.  Both exited zero; the first refreshed the repository-restored auxiliary state, and the second/final log has zero undefined references or citations and zero TeX errors.  Output is **74 pages**.
- Ran the full verifier once in the foreground: `uv run --with sympy,numpy,scipy python verify.py`.  All current blocks through `(bc)` passed in 1:46.71 with maximum RSS 333,908 KB.  Thus the v7 `(ba)`/`(bb)` blocks pass, and the post-v7 `(bc)` block adds no regression.
- `espaper.tex`: 0 forbidden control bytes, 0 CR, 0 NUL; corruption-species greps clean; 131 labels with no duplicate; every citation resolves.
- `git diff --check` is clean after restoring generated PDF/auxiliary files.  Only this review artifact is added.

## Scope signature

**Replayed directly:** all §§54–55 theorem statements and displayed formulas above; the residue-one size contradiction; Type-I discriminant/admissibility ledger; both pointwise quantifiers; both general-`m` windows; all conductor branches; favorable-sign and structured-fibre subtraction; perimeter/status table; external-context claims; citation resolution; no-contamination greps; compile and full verifier.

**Accepted cited inputs rather than reproved:** effective Linnik, effective prime number theorem/Chebyshev estimates, quadratic reciprocity, Bombieri–Vinogradov with one displayed exceptional character, and the inherited provisional analytic chains.  Their labels and dependency boundaries, rather than their full proofs, were the fidelity target here.
