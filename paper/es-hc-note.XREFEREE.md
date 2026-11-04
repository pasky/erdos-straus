# Cross-model referee report: es-hc-note

Reviewed: `side-agent/z56-paperhc`, commit `22bcb8767a615aa7af0d355c0f2c862aacaa0af3`.
Title: *The least certificate coordinate for the Erdős–Straus equation at a prime*.
Recommendation: **minor revision** (specialist analytic-number-theory journal).

## Summary

The principal statements survive independent re-derivation. I find no GAP or WRONG theorem in this revision. The useful contributions are the exact two-shift formulation, the carefully scoped sieve adaptations E/U, and the nonsquare-class obstruction N; the elementary certificate algebra is principally infrastructure, not a new parametrization of all Erdős–Straus solutions. An independent deep-mode audit of E/U agreed with my checks; I also inspected the key sieve sources myself.

The abstract and introduction accurately separate conditional infinitude, unconditional partial sieving, construction-specific limitations, and finite computation. **Erdős–Straus remains open.** Neither U nor N proves that HC is finite or unbounded on primes; E uses EH, and Proposition 5.1 uses Dickson. The full census has not been independently reproduced here.

## Per-result audit

“CORRECT” for a conditional theorem includes its stated hypothesis; for the computation it means the reported, explicitly limited computational evidence checks out, not a formal proof of the entire range.

| Result | Classification | Re-derivation / decisive check |
|---|---|---|
| Lemma 2.1 (words) | CORRECT | Expand `(tu−1)(tv−1)=t(tuv−u−v)+1`; positivity excludes `tu=1`; split `tu=2` from `tu≥3` to obtain the coordinate bound `n+2`. |
| Proposition 2.2 (slots and identities) | CORRECT | A product divisible by 8 has a factor divisible by 4; the reverse direction's odd cases modulo 8 exhaust the possibilities. All three displayed rational identities and their symmetric versions simplify to `4/n`. |
| Lemma 2.3 (two divisor lines) | CORRECT | U reconstructs `t=(d+1)/c`, `v=(n+c)/d`; T uses `de≡1`, `d≡−1 (c)` to reconstruct both coordinates positively. |
| Proposition 2.6 (small HC) | CORRECT | `d=2` supplies coordinate 3 exactly for `p≡5 (8)`; coordinate 4 is equivalent to a prime factor `3 (4)` in either odd shift. The excluded coordinates `p,p+1,p+2` give `HC≤p−1` when finite. |
| Lemma 2.7 (reciprocity) | CORRECT | Both lines give `(d'/n)=(−c/d')`; for `4∣c`, `(c/d)=1` and `d≡3 (4)`; for odd c, `(2/c)=(2/n)` cancels the power of 2 and leaves −1. Coprimality is proved, not assumed. |
| Corollary 2.8 (squares/support) | CORRECT | Jacobi symbols at odd squares cannot be −1. At `n≡1 (8m)` every prime dividing `2m` has symbol +1; Dirichlet gives infinitely many primes avoiding any fixed finite divisor list. |
| Proposition 3.1 (Mordell classes) | CORRECT | All six words have integral third coordinate and the stated value; CRT leaves exactly the six square unit classes modulo 840. |
| Lemma 4.1 (first threshold) | CORRECT | An odd integer lacks a divisor `3 (4)` exactly when all its prime factors are `1 (4)`; the next allowed coordinate is 7. |
| Remark 4.2 (determinant shell) | CORRECT | The inverse map is integral on the stated lattice; `det M=4(x²+y²)−(u²+v²)=15` and `‖M‖²=16p+34`. Primitive representations, not merely positive representation counts, are essential. |
| Theorem Q | CORRECT | `p+4=5(m²+1)`, `4p+1=5(4m²+1)`; all prime divisors are `1 (4)`. Primality forces `3∣m`, hence `p=720k²+1`; irreducibility and absence of a fixed prime divisor are valid. Only infinitude is conjectural. |
| Lemma 4.4 (weighted errors) | CORRECT | Cauchy–Schwarz with `E(x;q)≪x/φ(q)` and the Euler product for `k^{2ω(q)}/φ(q)` absorbs each fixed divisor weight by increasing the logarithmic saving. |
| Cited Theorems 4.5–4.6 (upper/beta sieve) | CORRECT | Match Ford Theorem 2.4 and Nath–Xie Lemma 3.6/Remark 3.7/§5, including the unusually convenient upper-sieve remainder range `d≤z`, dimensions, and normalizations. |
| Lemma 4.7 (semilinear functions) | CORRECT | Weighted sieve inequalities imply `f≤1≤F`; the delay equations give monotonicity and `(√s(F−f))'≤0`; `F(1)=1.505…<1.51`. The `arccosh` lower bound follows from `tanh t≤t`. |
| Proposition 4.8 (upper bound) | CORRECT | Local root counts are 1, 2 at 3, and 3 on other primes `3 (4)`; dimension 2, `z=x^{1/4}`, and remainder `O(z log²z)` give `O(x/log²x)`. |
| Theorem E | CORRECT | Root collision only at 3; `8D=x^{1−η}`. The linear-sieve parameter is `2+2η/(1−2η)+o(1)` and `f₁(s)≥0.79η`. Parity and `z³>4x+1` leave precisely two bad large factors. The switched dimension is 5/2, giving `O(η^{3/2}x/log²x)` against `≫ηx/log²x`; total elementary remainders are `x^{0.61+o(1)}`. The chosen η₀ closes the argument. |
| Cited Theorem 4.9 (vector sieve) | CORRECT | Nath–Xie Proposition 3.10 includes precisely the presieving products, supremum, and `τ(d₁d₂)^4` remainder quoted here. Zero densities on incompatible pairs are allowed by its proof and its own application (4.3). |
| Theorem U | CORRECT | Local overlap `h(3,3)=1/2`, otherwise zero; the singular factor `9/8` is right. `8D^{1+ε}≤x^{1/2−ε}` eventually permits weighted BV. `S₀≥151²/η` makes the semilinear loss at most `.01F(1)√η`; `s₁=(1−η/2)/(1−η)`. Switching costs `O(η^{3/2})` versus `≫√η`, with remainder exponent at most `11/16+o(1)<0.7`. The fixed positive δ and even bounded Ω conclusion follow. |
| Proposition 5.1 (Dickson) | CORRECT | All forms equal 1 at zero, proving admissibility simultaneously. Their prime values exceed `c+1` and are `1 (c)`, so divisors cannot be `−1 (c)`. The revised primorial lower bound uses only primes `≤X/4`, correctly. |
| Theorem W | CORRECT | Choose one parameter where every nonconstant factor exceeds `ℓ|C|`; divisibility of `P+4k` forces ℓ into a fixed constant and fixes every family member modulo ℓ. Distinct prime values then differ by the primorial, proving the bound except at the least value. It is not a universal upper bound for HC. |
| Theorem N | CORRECT | Valuation truncation gives `s∣c+1`; reciprocity forces `L≥ℓ₀`; `L≡−(c+1)/s (c)`. CRT gives the U/T congruences modulo L. The two elementary eliminations yield respectively `L≤R+1+2R/(i+1)` and `L≤2R+(R+1)/n`, both `≤3R+1<ℓ₀`. The progression is primitive. |
| Corollary 6.1 | CORRECT | Least-nonresidue argument gives `r(r−1)<ℓ`; the four small primes are handled separately. Taking Y to contain the finite divisor supports gives the required progression and excludes squares. |
| Computation 7.1 | CORRECT as computational evidence | Aggregation, all 126 high records, and the sampled reruns below pass; the complete `10¹²` census remains a single-program computation with cross-checks. |
| Closing Linnik observation | CORRECT | `p≡1 (8m)`, `m=∏_{ℓ≤Y}ℓ`, gives `log p≪Y`; reciprocity requires a certificate prime factor `>Y`. This excludes a sufficiently small absolute multiple of `log p`, not every logarithmic bound. |

## Citation and priority audit

- [Ford, *Sieve Methods*](https://ford126.web.illinois.edu/sieve2023.pdf): Theorem 2.4 states `S(A,z)≤O(XV(z))+Σ_{d≤z}μ²(d)|r_d|`; Theorem 3.4 supplies BV; (7.6) and Conjecture 7.3 supply the stronger endpoint-maximal EH formulation. The note's weaker fixed-endpoint hypothesis is sufficient for its proofs.
- [Nath–Xie v1](https://arxiv.org/pdf/2501.16723v1): checked (3.4), Lemma 3.6, Remark 3.7, Proposition 3.10 and its proof, (4.3), and §5. These support the quoted applications. The note explicitly cites *Opera de Cribro*, Theorem 11.12, only through this source; the book theorem was not directly inspected.
- [Friedlander–Iwaniec](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6709-11511_2009_Article_33.pdf): Theorem 4 is the conditional `ΣΛ(n)r(n−2)r(n+2)≍x` result; Theorem 3 is its determinant-one formulation, with the hypothesis of Theorem 2. The upper bound is unconditional. E is a different-shift, primitive-factor analogue, not an immediate quoted corollary.
- [Elsholtz–Tao](https://arxiv.org/pdf/1107.1010): Theorem 1.1 gives the stated prime-solution average after combining Types I/II; Proposition 1.6 is odd-square vanishing; Proposition 2.7 includes `abd` coprime to n. The identification with `c=1` is valid for the prime words in this note. The discussion preceding Proposition 1.9 supports the polynomial square-class obstruction and six Mordell classes, not an obstruction to arbitrary ES solutions.
- [López v3](https://arxiv.org/html/2404.01508v3): Theorem 7 is Type A (`p≡−4d (4dn−1)`), Theorem 4 Type B (`p≡−n (4dn−1)`); Conjecture 1 matches the note's divisible-by-4 subfamily. This is substantial prior overlap with the basic certificate framework, already acknowledged.
- [Yamamoto original](https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_pdf), inspected via bounded OCR: Lemma 4 gives the Kronecker-symbol obstruction for his covering system; Theorem 2 excludes perfect squares; §3 lists the six classes modulo 840. This is particularly relevant prior art for Lemma 2.7, not just general historical context.
- Sorenson–Webster, Theorem 1.1, gives the least strong pseudoprime to twelve prime bases as `318665857834031151167461`; thus the conservative `3.18·10²³` threshold is valid. Heath-Brown (1992), Theorem 6, gives `P(a,q)≪q^{5.5}`, sufficient for the closing observation. Both source texts were inspected.
- [Salez](https://arxiv.org/pdf/1406.6307) and [Mihnea–Dumitru](https://arxiv.org/pdf/2509.00128) report the cited `10¹⁷` and `10¹⁸` verifications. These are not HC censuses; the note does not advertise an ES verification record.
- Verification limits: Mordell and Schinzel's theorem texts were not directly inspected (their relevant statements were checked through ET); Schinzel's publisher record confirms the bibliography but its PDF retrieval returned HTML. Bombieri's historical attribution was checked through Ford, not the 1965 original. Dickson is a conjectural input, not a proved prime-tuples theorem. No blanket “every original source verified” claim is warranted.
- Fresh web/arXiv-indexed searches for the exact pair `p+4,4p+1`, restricted prime factors, and nonsquare certificate coverings found no identical theorem. The nearest checked precedents are FI, Nath–Xie, López, ET, and Yamamoto. This supports only the manuscript's qualified “we did not find” statement; MathSciNet/zbMATH were not searched. A search also surfaced *The Erdös–Straus Conjecture and Pythagorean Primes*, [HAL-04994962](https://hal.science/hal-04994962v1/document), but its text was inaccessible behind an anti-bot page; no overlap conclusion is drawn from its snippet.

## Required changes, in priority order

1. Make the local priority attribution sharper: cite Yamamoto **Lemma 4 and Theorem 2** beside Lemma 2.7/Corollary 2.8, explaining that the new feature is the selected coordinate statistic, not the quadratic-character obstruction itself. Retain the explicit López comparison. This is a minor attribution correction, not a mathematical gap.
2. Harden the computational audit entry points before distributing the supplement: `scripts/z55_hco_verify.py` prints `bad` but exits successfully even when it is positive, and `z55_hco_census.c` likewise reports `fail` without a failing process status. Require nonzero status on failure, or supply a checked wrapper. No bad/fail record appeared in this review; this concerns future reproducibility, not the existing counts.
3. State once in E/U that η is fixed before `x→∞`. Vector-sieve error constants and the comparison `log z₁≍log z₂` may depend on that fixed choice; only the displayed main/switching constants used to choose η must be absolute. The proof has the needed uniformity, but this distinction should be explicit.
4. Provide a stable public supplement or archive when submitting: source commit, commands, block manifest, outputs, and checksums. Repository-relative filenames alone are insufficient for a reader without this working repository. Keep the disclaimer that the complete census was not independently rerun.

## Reproduction record

All executions were timeout-bounded and computational runs used `ulimit -v 6000000`; Python ran through `uv`. Files were extracted from the reviewed commit under `/tmp/xrev_es-hc-note/`, not taken from another branch's working files.

- `timeout 900s uv run --with sympy python paper/es-hc-note.check.py`: **ALL CHECKS PASSED**; 11,709 words, 17,893 certificate divisors, 347 Q examples, 12 record recomputations, and the stated finite N samples.
- `uv run python scripts/z55_hco_aggregate.py` and `uv run --with sympy python scripts/z55_hco_verify.py data/z55/hco/census_*.txt`, under a 900-second outer limit: coverage `[0,10¹²)`, counts `9,401,972,490 + 9,401,951,850`, the exact printed histogram, and **126 HIGH records, bad 0**.
- Built `z55_hco_census.c` with `gcc -O2 -fopenmp -lm`; `OMP_NUM_THREADS=4 timeout 800s ./census 0 1000000000 44`: zero failures, every bin matches `data/z54/upper2/hc_1e9.txt`, total `25,423,491` primes `1 (4)`.
- Built and reran `z54_upper2_hc.c` independently to `10⁷` with a 570-second limit (its sieve allocates approximately 10 MB); reran the segmented program to the same endpoint. All bins match, total `332,180` primes `1 (4)`.
- Inspected the census's factorization, prime-test range, divisor-buffer guard, and coordinate cap. Did **not** rerun the full `10¹²` range or its last block, and did not independently recompute every ancillary numerical remark. No new mathematical proof is inferred from these finite checks.

## Minor comments and recommendation

The strongest story is E/U/N, not the number of elementary named results; shorten repeated warnings and move some computational detail to the supplement while preserving the scope statements. An explicit numerical δ is unnecessary for the existence theorem. The `cosh²(1/2)>1` discussion is correctly limited to the specified symmetric vector-sieve setup, not presented as an impossibility theorem.

**Minor revision:** the main arguments are coherent and the constants/exponents checked above close. The report requests attribution, parameter-dependence clarity, and reproducible failure handling, not a new theorem or a repair of a missing analytic estimate. Novelty is plausible at the precise-statistic/adaptation level, not established exhaustively; this is a specialist-journal contribution, not a resolution of Erdős–Straus or of the unconditional two-shift problem.
