# Second referee report: es-hc-note

Reviewed `main` at `2ea7968301d4b1d8df8549c98b23bc7405dc5374`; 5 November 2026.
Compared against the first report's `22bcb8767a615aa7af0d355c0f2c862aacaa0af3`, read the revised TeX and review records, re-derived the proofs and reran the computational entry points.
Recommendation: **MINOR REVISION — supplement completion only**. The mathematical and attribution requests are satisfied; the required stable public supplement still does not exist. I would accept the mathematical content, with no further theorem repair requested.

## Summary and response audit

The revised introduction appropriately foregrounds E/U/N and treats the elementary certificate framework as infrastructure. Yamamoto's priority is now acknowledged locally. The conditional/unconditional distinction is intact: E assumes EH, the infinitude consequence of Q assumes Bunyakovsky, and Proposition 5.1 assumes Dickson. U still leaves boundedly many bad prime factors in the second shift. Neither W nor N proves that HC is unbounded or finite at every prime. **Erdős–Straus remains open.**

| First-report requirement | Disposition |
|---|---|
| 1. Yamamoto attribution beside Lemma 2.7 / Corollary 2.8 | **Addressed.** The added paragraph cites Lemma 4, Theorem 2 and §3; it disclaims novelty of the character obstruction and retains the López comparison. I checked Yamamoto's printed p.41, not only the response letter. |
| 2. Nonzero exit on census/verifier failure | **Addressed by the checked wrapper.** `census-check.sh` uses `set -euo pipefail`, verifies hashes, failure counters, tiling, totals and the exact final record-verifier line. Normal execution passes; five isolated fault injections are rejected with nonzero status. The old scripts still return success on some failures, so the wrapper must be the documented entry point. |
| 3. Fix η before x→∞; distinguish parameter-dependent errors | **Addressed.** Both proofs now state this explicitly. Main/switching constants used to choose η can be absolute; onset, vanishing errors and vector-sieve comparability may depend on fixed η, S₀, δ, ε. |
| 4. Stable public supplement when submitting | **Not yet satisfied.** The manifest and wrapper improve local reproducibility, but §7 and `.REVIEW.md` explicitly say there is no public archive. This is a submission condition, not a mathematical gap. The manifest also omits some files covered by the new phrase “all these files”; see Required change. |
| Minor suggestion: emphasize E/U/N, shorten repetitive caveats | **Main emphasis addressed.** Retaining the scope caveats is harmless. No numerical δ or broad “sieve impossibility” claim has been added. |

## Per-result audit

CORRECT means the displayed proof checks relative to its stated hypotheses and cited analytic inputs. For Computation 7.1 it means the limited computational evidence described here checks, not independent verification of every prime below 10¹². No GAP or WRONG theorem found.

| Result | Classification | Re-derivation / decisive check |
|---|---|---|
| Lemma 2.1 | CORRECT | Expand `(tu−1)(tv−1)=t(tuv−u−v)+1`; positivity and the split `tu=2` / `tu≥3` give coordinates ≤n+2. |
| Proposition 2.2 | CORRECT | Modulo 8, a product divisible by 8 has a factor divisible by 4; the remaining odd cases exhaust the reverse implication. All five unit-fraction identities simplify correctly. |
| Lemma 2.3 | CORRECT | U recovers `(t,v)=((d+1)/c,(n+c)/d)`; T uses `de≡1 (c)` and `d≡−1 (c)` to recover both positive coordinates. |
| Proposition 2.6 | CORRECT | Coordinate 3 occurs for p≡5 (8); coordinate 4 is exactly the bad-prime-factor event in the two odd shifts; the top three coordinate values are excluded. |
| Lemma 2.7 | CORRECT | Both lines give `(d′/n)=(−c/d′)`; 4∣c gives −1 directly, while odd c uses `(2/c)=(2/n)`. Coprimality follows from the line equations. |
| Corollary 2.8 | CORRECT | Square Jacobi symbols cannot equal −1; p≡1 (8m) makes every support prime dividing 2m a residue; Dirichlet gives infinitude. Attribution is now properly scoped. |
| Proposition 3.1 | CORRECT | All six words have positive integral last coordinate; CRT leaves precisely `1,121,169,289,361,529 (840)`. |
| Lemma 4.1 | CORRECT | An odd integer has no divisor 3 (4) exactly when every prime factor is 1 (4). Next allowed coordinate is 7. |
| Remark 4.2 | CORRECT | Inverse lattice map is integral; determinant 15 and norm `16p+34` agree. Primitive sums of two squares are essential, as stated. |
| Theorem Q | CORRECT | `p+4=5(m²+1)`, `4p+1=5(4m²+1)`; all factors are 1 (4). Primality forces 3∣m; `720k²+1` is irreducible without fixed prime divisor. Only infinitude is conjectural. |
| Lemma 4.4 | CORRECT | Cauchy–Schwarz and `E≪x/φ(q)` absorb fixed divisor weights via an Euler product and an increased logarithmic saving. |
| Cited Theorems 4.5–4.6 | CORRECT | Ford 2.4 really has remainder range d≤z; NX 3.6/3.7/§5 gives the beta-sieve normalizations, sifting limits and functions used here. |
| Lemma 4.7 | CORRECT | Weighted sieve inequalities give `f≤1≤F`; delay equations give monotonicity and `(√s(F−f))′≤0`; `F(1)<1.51`; `arccosh y≥√(y²−1)/y`. |
| Proposition 4.8 | CORRECT | Root counts are 1, 2 at 3, and 3 at other bad primes; dimension 2 and z=x^(1/4) give the claimed upper bound. |
| Theorem E | CORRECT, conditional | Collision only at 3; `8D=x^(1−η)`; `f₁(s)≥0.79η`. Parity and `z³>4x+1` leave two bad large factors; the dimension-5/2 switch costs `O(η^(3/2))` against main `≫η`. Remainder exponent ≤0.61+o(1); fixed small η closes the proof. |
| Cited Theorem 4.9 | CORRECT | NX 3.10 supplies the presieving product, supremum and τ(d₁d₂)^4 remainder. Allowing zero densities is justified by its proof and its own (4.3). |
| Theorem U | CORRECT | `h(3,3)=1/2`, singular factor 9/8, `8D^(1+ε)≤x^(1/2−ε)` eventually. `S₀≥151²/η` makes the loss ≤`.01F(1)√η`; `s₁=(1−η/2)/(1−η)`. Switching costs `O(η^(3/2))` against `≫√η`; error exponent ≤11/16+o(1)<0.7. Fixed δ>0 and even bounded Ω follow. |
| Proposition 5.1 | CORRECT, conditional | All forms equal 1 at zero, hence admissible for Dickson; their large prime values are 1 (c), preventing divisors −1 (c). The corrected primorial argument uses only primes ≤X/4. |
| Theorem W | CORRECT | Choose one parameter avoiding all small prime values of the nonconstant factors; each small ℓ must divide a fixed factor, fixing every family member modulo ℓ. Distinct prime values differ by the primorial. Scope is construction-specific. |
| Theorem N | CORRECT | Valuations give s∣c+1; reciprocity forces L≥ℓ₀; `L≡−(c+1)/s (c)`. CRT gives both line congruences; eliminations force `L≤3R+1<ℓ₀`. The progression is reduced. |
| Corollary 6.1 | CORRECT | Least nonresidue satisfies `r(r−1)<ℓ`; four small primes handled separately. Choose Y to include every finite divisor support, retaining 840∣M and excluding squares. |
| Computation 7.1 | CORRECT as evidence | Hashes, tiling, stated totals, all 126 HIGH records and the fresh [0,10⁹) rerun pass. Full 10¹² census not independently rerun. |
| Closing Linnik observation | CORRECT | For `m=∏ℓ≤Y ℓ`, p≡1 (8m) and Linnik give log p≪Y, while every certificate divisor has a factor >Y. This rules out a sufficiently small constant times log p, not all logarithmic bounds. |

## Remaining required change (submission/reproducibility)

**Complete and freeze a public supplement before submission.** Supply a stable URL/DOI and an immutable source revision, together with build/run commands, dependencies, block manifest, outputs, checksums and the current scope disclaimer. The new local files are useful but do not by themselves satisfy the first report's public-access requirement. No permission to publish has been presumed or sought in this review.

There is also a small new mismatch in §7 (TeX 1249–1253): the SHA-256 manifest is described as covering “all these files”, but it does **not** include `paper/es-hc-note.census-rerun.txt`, which the preceding sentence names. Nor does it hash the new wrapper or `paper/es-hc-note.check.py`. Add these audit entry points/transcript to the frozen manifest, or narrow the sentence to the census programs and archived outputs actually listed. The supplement should include all three even if the wording is narrowed. The manifest cannot authenticate itself; record its hash externally in the archive/release metadata.

These are minor deliverable/presentation requirements. I find no need to repeat the analytic revision or to rerun the full 10¹² computation merely to answer this report.

## Sources and novelty

- Re-read Yamamoto's original **Lemma 4 and Theorem 2**, printed p.41, including the scan image, and §3 via the archived OCR. The new attribution correctly identifies his nonresidue obstruction for the covering system and square exclusion; it does not claim he defined HC.
- Freshly downloaded [Ford, Sieve Methods](https://ford126.web.illinois.edu/sieve2023.pdf): **Theorem 2.4**, its (Ω) hypothesis and dependence only on κ₀,B₀ match the switched bounds; **Theorem 3.4** supplies the required BV input. The paper's weaker fixed-endpoint EH hypothesis suffices.
- Freshly downloaded [Nath–Xie v1](https://arxiv.org/pdf/2501.16723v1): **(3.4), Lemma 3.6, Remark 3.7, Proposition 3.10**, its presieving proof and **§5** match the stated inputs. Fixing η before the limit resolves the requested uniformity explanation; it does not alter the source theorem. *Opera de Cribro* 11.12 remains cited indirectly through NX, not inspected directly here.
- Rechecked [Elsholtz–Tao v6](https://arxiv.org/pdf/1107.1010v6), **Propositions 2.6–2.7**, for the Type II map and coprimality condition. The manuscript's Proposition 2.7 citation is correct in v6. The first report's checks of **Theorem 1.1, Proposition 1.6**, López **Theorems 4/7, Conjecture 1**, and FI **Theorems 2–4/§6** remain applicable; the elementary algebra was independently re-derived here.
- The first report's historical/computational-source audit remains the record for Mordell/Schinzel via ET, Salez, Mihnea–Dumitru, Sorenson–Webster **Theorem 1.1**, and Heath-Brown **Theorem 6**. I do not claim a new inspection of every original historical source or a new proof of the Miller–Rabin threshold.
- Fresh bounded web searches for the exact two shifts and certificate statistic found no additional exact prior theorem. The nearest established comparisons remain FI, NX, López, ET and Yamamoto. This is not an exhaustive priority search. Akaka's almost-all solution-count claim does not imply the HC two-shift event and creates no analogous missing priority comparison here.

## Reproduction and failure-path checks

All commands were timeout-bounded; computational commands used `ulimit -v 6000000`; Python ran through `uv`. I inspected allocation and loop sizes first. Temporary builds/probes stayed outside the repository.

- `timeout 900s uv run --with sympy python paper/es-hc-note.check.py`: **ALL CHECKS PASSED** — 11,709 words, 17,893 certificate divisors, 347 Q examples, 12 record recomputations and finite N samples.
- `timeout 900s bash paper/es-hc-note.census-check.sh`: **CENSUS CHECKS PASSED**. All listed hashes match; coverage is `[0,10¹²)`; prime subtotals are `9,401,972,490` and `9,401,951,850`; printed histogram and π(10¹²) match; **126 HIGH records, bad 0**.
- In an isolated temporary git repository containing copies of the supplement, injected (i) a checksum mismatch, (ii) a nonzero fail counter, (iii) a FAIL line, (iv) broken tiling, and (v) a bad certificate divisor. For (ii)–(v) the temporary manifest was recomputed so the downstream checks, rather than checksum rejection, were exercised. All five exit nonzero at the intended stage; the bad-divisor case reaches `checked 126 HIGH records, bad 1` and is rejected. Reviewed files were never modified. The temporary harness first needed two setup corrections (the archived witness is 2431, not the paper's alternative 575; create its paper directory); neither was a manuscript/tool failure.
- Rebuilt the census with `gcc -O2 -fopenmp -lm`; `OMP_NUM_THREADS=4 timeout 800s … 0 1000000000 44` reports zero failures, `12,712,271` primes 5 (8) and `12,711,220` primes 1 (8). Its histogram agrees bin-by-bin with the independent program's archived `data/z54/upper2/hc_1e9.txt`.
- Three timeout-bounded `pdflatex -halt-on-error` passes produce the 21-page revised paper without undefined references/citations. The optional wrapper `RERUN=1` branch was not itself invoked; its census calculation and histogram comparison were executed separately above.
- Not independently regenerated: the full 10¹² census, its final large block in this pass, and ancillary 10¹⁰ Ω statistics. The checks support the explicitly limited computational evidence, not a formal certificate of the entire range.

## Recommendation

**Minor revision, restricted to completing the submission supplement and its description.** All requested mathematical, attribution and error-handling changes are now satisfactory. Once the immutable public supplement accompanies the submission, I have no remaining mathematical objection to specialist-journal consideration. The paper is not a proof of Erdős–Straus or of unconditional infinitude for the exact two-shift problem.
