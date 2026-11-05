# Second referee report: es-count-note

Reviewed `main` at `2ea7968301d4b1d8df8549c98b23bc7405dc5374`, including revision `553a68b9`; 5 November 2026.
Compared the TeX with the first report's `bc6780d144094f41249acdefe4ce0a1c9be37908`, read the revised paper and both review records, re-derived the arguments, and reran the checks.
Recommendation: **MINOR REVISION**. The former major objection is substantially resolved; the new literature paragraph needs a precise distinction between Akaka's full count and his auxiliary family. No GAP or WRONG main theorem found.

## Summary and disposition of the first report

The paper now acknowledges the specific earlier public claim, explains the substantial methodological overlap, and positions Theorem C as a result about the particular `c=1` slice rather than a new best almost-all bound for all solutions. The upper-bound and genus contributions remain separate. Nothing here proves Erdős–Straus or positivity of R at an arbitrary prescribed prime.

| First-report request | Disposition |
|---|---|
| 1. Akaka acknowledgement and comparison throughout | **Substantially addressed, small clarification required.** Abstract, post-Theorem-C paragraph, §§1.4/1.6, §7(4), bibliography and `.REVIEW.md` now acknowledge v0.7 and its stronger claim. The theorem, exceptional-set scale, strict ordering and method comparison match the source. The auxiliary-family disjointness calculation is correct, but “his count is restricted” conflates two different counts; see Required changes 1. |
| 2. Theorem 3.14 rounding and endpoint | **Addressed.** `a∈(0,1]`; `N=ceil(W/Q)≤2W/Q`; `Y/N²≥ℓn/(16W²)≥n^c/4`. Small N is handled trivially. |
| 3. Numerical order and larger-level overclaims | **Addressed mathematically.** Three samples are expressly insufficient to establish the variance order; alternative improvements are listed, and larger-level correlations are required only for enlarging this truncation. One sentence splice remains. |
| 4. HLMLT author order | **Addressed.** Hasanalizade, Lin, Luna Martínez, Martin, Treviño agrees with v2's title/HTML. The review explicitly retracts its former metadata-based response. |
| Reproducibility of historical slice percentages | **Partly addressed.** Generator and output paths are now given and the text expressly says the experiment was not regenerated for the note. Its Python source supplies the invocation. I did not regenerate the PARI-dependent experiment; do not present it as independently reproduced. |
| Preserve earlier scope/proof repairs | **Addressed.** Prime-only Type II qualification, odd-prime pair domain, finite hyperbolic sum, restricted slice asymptotic, both derivative terms, and heuristic status of the balanced-block discussion remain intact. |

## Per-result audit

CORRECT means the argument checks relative to the explicitly stated classical inputs; it does not certify proofs of those inputs. Numbering follows the rebuilt paper. No theorem has changed its mathematical content except the repaired explanation in Theorem 3.14.

| Result | Classification | Decisive re-check |
|---|---|---|
| Lemmas 2.1–2.2 | CORRECT | `n<4uBC≤2n`; prime Type II injection recovers u, B, C; opposite parity and coprimality hold on the odd-prime domain. |
| Lemma 2.3 | CORRECT | `(4Cu−1)(4CB−1)=4Cn+1`; `(C/(4Cu−1))=1`, forcing the claimed nonresidue and odd-square vanishing. |
| Lemma 2.4 | CORRECT | Fix each coordinate, use divisors of `n+u` or `4Cn+1`, then `min(u,B,C)≤(n/2)^(1/3)`. |
| Lemmas 3.1–3.2 | CORRECT | Square detection preserves positivity and parity; multiplicity at most two; the diagonal is ≤τ(n); both sieve constants 4 follow from the positive-square support condition. |
| Lemma 3.4 | CORRECT | Discriminant `16(4cn+1)`; linear and repeated-root cases separate; the nonzero-frequency reduction is Kloosterman; CRT gives `4Q^(3/2)`. |
| Theorem 3.8 / A(a) | CORRECT | Shiu covers both small-coordinate ranges; Vaaler plus third derivatives gives the displayed discrepancy; `P=T^(1/25)`, `η=1/75` yields `n^(74/225)(log n)²`. |
| Lemma 3.10; Proposition 3.11 | CORRECT | Poisson sign, `V/(4CQ)` normalization and Fourier derivative check; zero mode `V/Q+V/W`; remaining powers are `Q n^(1/6)W^(1/2)V^(−1/6)`, `Q^(1/2)V^(1/6)W n^(−1/6)`, `Q^(3/2)`. |
| Theorem 3.12 / A | CORRECT | Affine maxima at the three vertices are `12/37`, `104/333`, `421/1332`; minimum ρ is `4/333`; cube gives `17/54`. |
| Theorem 3.14 / A(b) | CORRECT | The repaired rounding now meets the exponent-pair hypothesis. General vertex deficits have the stated signs for `0≤κ<1/4`; exponent `4/(13−4κ)`, Bourgain instance `21/65`, conjectural limit `4/13`. |
| Lemma 4.2 | CORRECT | Square conditions at 8 and primes dividing u,w give `1/(2φ(u))` per orientation, including nonsquarefree w. |
| Lemmas 4.4–4.5 | CORRECT | Möbius removal, both character tails and both hyperbola identities check; nonprincipal products are constant terms, and the principal derivative sign is positive. |
| Proposition 4.6 | CORRECT | Primitive conductors multiply to `4up`, are cube-free, and the second contains p. Window subtraction cancels nonprincipal constants; h-tails save a power. |
| Proposition 4.7 | CORRECT | Keep the n=1 square term; nonsquares cost `p^(θν−κα₀+o(1))`; squarefree `u≡1 (4)` has density `2/π²`. |
| Theorem 4.8 / B | CORRECT | `H_u/φ(u)≥(4/π²)(p/(p+1))/u`; window product tends to a maximum `1/12`; constant `2/(3π⁴)` is effective after fixing parameters. |
| Proposition 4.10 | CORRECT | Nonsquarefree-w split Euler factor, ramified factors and primitive discriminants check. Both `L′H` and `LH′` are needed; the short-squarefree-slice restriction remains. |
| Theorem 4.12 | CORRECT | AP hyperbola cutoff `4u p^(ϖ+ε)` yields a class-independent main term; C4 controls the large-c tail. Summed error is `O(p^(−δ)log p)`; optimum `α₁=19/120`, constant `121/(640π⁴)`. Only density weighting is controlled. |
| Lemmas 5.1–5.2 | CORRECT | Two orientations do not overlap for `p≥(Q+1)²/4`; harmonic mean ≥`log²Y/8`. |
| Lemmas 5.4–5.5 | CORRECT | CRT classes are reduced at level ≤Q²; multiplicity budgets 5 and 170 fit BV with A=200. |
| Lemmas 5.6–5.7 | CORRECT | Unique primitive-conductor decomposition gives the exact second-moment identity; deleting conductor 1 permits arbitrary centering of each cell. |
| Lemmas 5.8–5.9 | CORRECT | Progression harmonic estimates and finite integral comparisons cover empty cells and retain the displayed error constants. |
| Proposition 5.10 | CORRECT | Corner term ≤`4(1+log Q)²` by `Σφ(d)=m`; two edge terms give the upper constant `8ζ(2)/9`. No matching lower bound is proved. |
| Theorem C | CORRECT | `V/M²≤(2048ζ(2)/9+o(1))/log X`, leading constant `374.313885…`; Chebyshev, discarded prefix and logarithmic truncation justify 1600 and threshold coefficient 1/64. Onset remains ineffective. |
| New auxiliary-family comparison, §1.4 | CORRECT-WITH-FIX | Decoder disjointness is valid; identify its domain as Akaka's F-family, not his full R_II. |

## Required changes (minor, priority order)

1. **Distinguish the full count from the auxiliary construction** (TeX 73–75, 284–293). Akaka's equation (1), p.1, defines `R_II(p)` to count **all** strict Type II triples. His restricted parameter family defines `F(v)` in §2, and (7), p.3, states `F(p)≤R_II(p)`. Thus “his count is restricted to the family” is false if “his count” means the just-defined R_II. Indeed, at an odd prime, sorting the two p-divisible denominators of an R-triple gives a triple counted by R_II, with `R(p)/2≤R_II(p)`; the full counts are not disjoint.
   Replace that phrase by “his proof obtains the lower bound by counting the auxiliary family F…” and say in the abstract that **the construction used in the proof**, not the full Type II family, is disjoint from the c=1 line. For `x=uBC`, `M=BC`, the decoder gives `s/M=(4BC−1)u−p=B`; with `M=uC` it gives u. Akaka's family has `s/M=a/b∈(0,1)`, so the advertised disjointness of the two constructions is proved. No change to Theorem C is needed.
2. **Avoid implying a two-sided almost-all estimate** (TeX 283–284). “It gives the true average order of f_II for almost all primes” should be “it gives an almost-all lower bound on the scale of the known mean of f_II.” The cited theorem is a lower bound; neither it nor the known average upper bound supplies a fixed-constant pointwise upper bound on a density-one set for the full count.
3. **Remove the new sentence splice** (TeX 1876–1877): delete “So the bound of” before “These three values are consistent…”. Prefer “the upper-bound coefficient is about 70 times the observed ratios” to “whose constant is then about 70 times too large”, since no asymptotic variance coefficient is established.

## Sources and priority

- Revisited the [public Akaka record](https://zenodo.org/records/22754703) and read the archived v0.7 PDF, especially Theorem 1, §2/Lemma 2/(7), §3/(10), conductor ranges and §4/Lemma 4. Public metadata: 14 September 2026; MD5 `55595fee13a5cdff54a650e86143ed66`. The theorem and method comparison match; this is **not** a referee report on Akaka's proof or Lean development, neither of which is certified here.
- Freshly downloaded [Elsholtz–Tao v6](https://arxiv.org/pdf/1107.1010v6): Proposition **2.6** and (2.13)–(2.22) do support the c=1 parametrisation; Proposition **2.7** gives solvability equivalents. An auxiliary source reader suggested changing 2.6 to 2.5; I rejected that suggestion after checking v6, whose numbering agrees with the manuscript. Theorem 1.1's Type II prime sum has order `X log²X`, hence prime mean `log³X`.
- Rechecked Bourgain **Theorem 6**, §5, and Trudgian–Yang **§1.1/(1.1)–(1.2)** against the reciprocal phase and repaired rounding; the qualification “relative to Bourgain's theorem” is retained. Re-read IK **Theorem 11.11 / Corollary 11.12** for Kloosterman sums.
- Revisited [HLMLT v2](https://arxiv.org/html/2511.17778v2), **Theorem 1.2**, including its threshold and extra factors: effective fixed-r absorption remains valid; r=1 is separately Pólya–Vinogradov. Title-page author order is now correct.
- Ford's freshly downloaded **Theorem 3.4** gives the maximal π/li version of BV; replacing li by π costs the PNT error times `Σ1/φ(q)≪log q`, absorbable by increasing the logarithmic saving. This independently supports the input even though IK 17.1's original book page was not accessed.
- The first report's source-specific audits of Shiu **Theorem 1**, Titchmarsh **Theorem 5.11**, Vaaler/GK **A.6**, ET **1.6/1.7/1.8**, EP **Theorem 1**, BL **Corollary 1.4**, and the historical citations remain applicable to unchanged claims. I do not relabel those inherited checks as fresh original-source inspections; the access limits in that report remain.
- A new bounded web search for the defining polynomial, c=1 count and Type II almost-all results found no further exact prior match. Akaka is the concrete overlap requiring comparison. This is not a MathSciNet/zbMATH search or a priority certificate; withdrawn counting preprints are not established substitutes.

## Reproduction

Every execution was timeout-bounded; computational runs used `ulimit -v 6000000`; Python ran through `uv`. Code dimensions/allocations were inspected before execution; no quadratic-memory covariance array was built. Build artifacts and probes stayed under `/tmp/z57-reref/`.

- `timeout 180s uv run --with sympy python paper/es-count-note.checks.py`: passed; named vertex values, side conditions, `12/37`, `21/65`, `4/13`, cube `17/54` reproduced. General-κ signs were also checked analytically.
- C checker built with `gcc -O2 -Wall -Wextra`; `timeout 300s … zeros 10000000` reproduced all fourteen listed primes and zero odd-square violations.
- `mgen` reruns reproduced `3.999068, 5.352387, 6.790809, 27.736888, 29.083352` at `409,577,8089,1000033,8813281`, and zero at `961,1225,9801`.
- Rebuilt `scripts/z53_pz_exactV_trial.c`; weighted runs at Q=100,1000,3000 reproduced `V=2.098849,6.943898,10.887322`. The largest run streams 5,089² pair contributions, using linear storage.
- Three bounded `pdflatex -halt-on-error` passes produce the 25-page revised paper without undefined citations/references; nonfatal box/bookmark warnings remain.
- The historical 65-slice PARI/GP experiment was inspected for provenance, not rerun. No universal-prime conclusion follows from these computations.

## Recommendation

**Minor revision**, not major revision: the priority objection is now answered in substance, and the mathematical results survive. Correct the full-count/auxiliary-family wording and the two small presentation issues, then the paper is suitable for consideration by a specialist analytic-number-theory journal, subject to ordinary human editorial/referee assessment. This is an internal computational/model-assisted audit, not external journal certification.
