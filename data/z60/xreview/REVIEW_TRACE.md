# z60 cross-model hostile review — TRACE

**Verdict: ACCEPT-WITH-FIXES.** The narrowed outcome (“no positivity mechanism obtained”) survives; the general trace identity is **not proved**. ES and (MS) remain OPEN.
Reviewed `side-agent/z60-trace` at `11e84de67196c80ba22eb3c9f343fbadc59bc7ac`, including its internal review and literature report. No memo/source files were modified.

## Per-claim findings

| Claim | Classification | Independent check / limitation |
|---|---|---|
| Lemma 1(i–iv), line/root dictionary | CORRECT | `det(Qγ−I)=Q²s−Qw+1`, `tr=Qw−2`, discriminant `Q²(w²−4s)`. Square discriminant has the parity needed for integral roots. Mixed signs make `(Qu−1)(QB−1)<0`; repeated roots give even n. Ordered roots are not matrix conjugacy classes. |
| Lemma 1(v), odd-square exclusion | CORRECT | Put `d=4Cu−1`. Then `n≡−u (d)`, `gcd(u,d)=1`, and quadratic reciprocity gives `(u/d)=1`, `(-1/d)=−1`. A square cannot have Jacobi symbol −1. |
| Lemma 1(vi), corrected elliptic orientation | CORRECT | The associated definite binary forms have two orientations; positive forms alone give H. Thus total PSL-centraliser weight is **2H**, including imprimitive forms. Explicit J and −J each have PSL-centraliser 2 and are not SL-conjugate: an anticommuting matrix has determinant `−a²−b²`. |
| Lemma 2, level splitting | CORRECT | Normality gives `2μ/|Z_SL|=μ/|Z_PSL|` level classes per SL-class. The finite centraliser intersects torsion-free Γ(Q) trivially. At C=1,n=4, the two orientations give 24 Γ(4)-classes, not 12. Total is **2μH**. |
| Spectral character decomposition / normalisation | CORRECT | Conjugation by `diag(1,Q)` gives `Γ₀(Q²)∩Γ₁(Q)` and quotient `(Z/QZ)×`. Its characters have parity k. The positive determinant-N correspondence is ordinary T_N since N≡1 (Q); negation multiplies by `(−1)^k`. No extra φ(Q). The stated slash matches Popa (1.5). |
| Theorem 2, scalar / cusp / degree terms | CORRECT relative to the displayed C–S formula | Orthogonality gives φ(Q)/2 times the two ±1 indicators. `ψ(Q²)φ(Q)/2=μ`; the cusp sum is `Σ_{a|Q²}φ(gcd(a,Q²/a))=ψ(Q)`, hence coefficient `−μ/(2Q)`. Diagonal pairs retain weight one. The trivial-character k=2 correction is σ(N). |
| Theorem 2, elliptic term / Lemma 3 | GAP, honestly CONDITIONAL | The root support and the change of variables are correct, but the f-sum/embedding-number identity is not proved. Re-running all 21,044 cases is evidence, not a proof. Conditional on that identity, the coefficient is **−μE**, not −2μE. |
| Popa cross-check of orientation | CORRECT as a sketch, not a replacement proof | Reflection `diag(−1,1)` preserves Γ(Q), Δ and trivial character, so Remark 3.2 applies. Popa traces M_k+S_kᶜ, giving elliptic contribution −2μE; subtracting Eisenstein and halving explains −μE on S_k. The complete Eisenstein calculation is still unwritten. |
| Corollary 2.1 | CORRECT conditionally | μ=24, cusps=6 give coefficients 24,3,8 and scalar terms 2 and 4λ/3. For k=3, spectral trace is −a(N), so the sign of a(N) is correct. If N is not a sum of two squares, both CM and scalar terms vanish. |
| Proposition 4.1, parity | CORRECT conditionally | Solving the identity gives `ES=X−(2Q/μ)Tr` in odd weight; even weight has −TRIV. TRIV≥2 because 1,N are distinct. “As hard” is an assessment, not a reduction theorem. |
| Proposition 4.2, slack | CORRECT conditionally | With c=2Q/μ, `X−cB=ES−c(B−Tr)`. Positivity iff `B−Tr<(μ/(2Q))ES` is exactly a rearrangement, not a lower bound on attainable slack. |
| Corollary 4.3 | CORRECT conditionally, with wording caveat | Away from level, old/new eigenvalues obey Deligne; χ(N)=1 makes them real. `ρ≤(τ(N)−2)/τ(N)<1`. Dividing the slack inequality by dim gives exactly `6/((k−1)Q−6)`. Only the **ρ-free** threshold is vacuous at (k,Q)=(3,4); the sharper ρ-dependent necessary condition still exists. |
| Proposition 4.4, one-point window | CORRECT | For elliptic s,w, `σ=√s<(1+√N)/Q`, hence `|w|<2(1+√N)/Q≤Q/2`. There is at most one representative of −n modulo Q; the half-open endpoint cannot be elliptic. The trace consequences remain conditional. |
| Proposition 4.4(c), explicit family | CORRECT-WITH-FIX | The formula and uniform-bound counterexample are correct conditionally; add the missing coprimality step in the non-square argument (below). Fixed odd k and all levels/all n are essential; n≡5 (8) is outside the Mordell-hard domain. |
| Remark 4.5, bounded C | CORRECT | Finite global zeros refute a range containing them, not eventual bounded-C positivity. No infinitude proof is supplied or claimed. |
| Remark 4.6, Bruhat identity | CORRECT | Left/right translations l,r give diagonal entries `Q−1+Ql,Q−1+Qr`; positivity means l,r≥0. Their upper-right entry is `Q(l+1)(r+1)−(l+1)−(r+1)`, exactly (★). |
| Second moments / Kuznetsov / “no positivity” | CORRECT as scoped assessments | No independent positivity input is supplied; this is not a proof that one-sided bounds, another C-range, or modified geometric/spectral terms cannot work. |
| §7 “Deligne-type worst-case input … does not give (★) beyond Γ(4)” | GAP / overstatement | The necessary alignment condition plus finite non-firing at C=2,3 does **not** establish universal non-firing beyond Γ(4). This leftover sentence contradicts the otherwise careful narrowing. |

### Explicit family re-derived

For Q=4C≥8, n=2Q−3, `N=(Q−1)(2Q−1)` and `(w*,s*)=(3,2)`, so E=0. The large-C window hypothesis holds already at C=2.
`gcd(Q−1,2Q−1)=1`; if N were square both factors would be squares, impossible since Q−1≡3 (4). This is the missing step in the memo's abbreviated argument; S=0 follows.
Below √N<2Q−1, the only possible ES divisor is Q−1. Below √N<2Q+1, the only nontrivial possible TRIV divisor is Q+1, but `N≡6 (Q+1)` and Q+1≥9.
Thus `ES=2(Q−1)^(k−1)`, `TRIV=2`, and `Tr=−ε∞((Q−1)^(k−1)−1)`.
Since μ≍Q³, ε∞≍Q², dim≍_k Q³ and N≍Q², the ratio to `√dim·τ(N)N^((k−1)/2)` is `≍_k √Q/τ(N)=Q^(1/2−o(1))`. This refutes the stated **level-uniform absolute bound**, conditional on Theorem 2; it does not refute a restricted or one-sided bound.

## Recomputations

All executions used `ulimit -v 4000000`, individual timeouts ≤1200 seconds (hence ≤1800), and Python through uv. PARI spectral allocation was set to 300 MB; computations were scalar/bounded, not Cartesian-product arrays.
Fresh spectral slice, using the archived scripts: `(C,k,nmax)=(1,2,30),(1,3,30),(1,4,30),(1,5,30),(2,3,30),(3,3,30),(4,3,12),(5,3,10)` — **202 exact equalities, zero mismatches**. Dimensions 0,1,3,5,20,72,208,408 agree. This is a sparse slice, not a full C×k grid.
Fresh `z60_trace_locallemma.py 60`: **21,044 cases, zero mismatches**. Its use of canonical representatives is consistent with the source's “lifts” wording: if a lift is a root modulo MM_f, discriminant divisibility forces M_f|(2x−t), making changing x by M harmless.
Independent script `scripts/z60_xrev_trace_check.py` enumerates reduced positive binary forms for H (weights 1,1/2,1/3), uses a closed polynomial for P_k, and separately enumerates divisors and scalar terms. It shares PARI only for integer factorisation/divisors, **not class numbers or trace assembly**.
It verifies all **2,320 stored JSON rows + 202 fresh rows**, and independently reconstructs Tr, ES and TRIV on all **23,600 rows** of the three range TSVs. No mismatch. Stored spectral traces are not all freshly recomputed; only the 202-case slice is.

| Range, k=3 | ES>0 | Deligne fires | Minimum slack ratio (n) | Median |
|---|---:|---:|---|---:|
| C=1, n≤20000 | 12229 | 137 | 454/669 (12655) | 26.0123784262 |
| C=2, n≤3000 | 990 | 0 | 57722/15123 (701) | 96.1602690225 |
| C=3, n≤600 | 109 | 0 | 34086/5041 (491) | 66.2495274102 |

The explicit-family geometric assertions also pass **998 checks**, C=2…500, k=3,5; the fresh spectral slice includes C=2,n=13 (Tr=−1152) and C=3,n=21 (Tr=−5760).
Reproduce the independent checks after archiving the lane and fresh JSON files to `/tmp/xrev_TRACE`: `ulimit -v 4000000; timeout 1200 uv run --with cypari2 python scripts/z60_xrev_trace_check.py /tmp/xrev_TRACE`.

## Mandatory falsifiers

| Screen | Hostile finding |
|---|---|
| F1 odd squares | Correct: all C have ES=0 by the Jacobi argument. The identity and slack equivalence then forbid firing. This is consistency, not a prime-positivity mechanism. |
| F2 numerator-8 / C-even | Correct with the memo's transport and threshold caveats. Independently enumerated **all** root pairs at 10156800001: ordered R=56 and every C odd, hence R₈=0. The remaining 11 supplied zeros were not re-enumerated. An existential argument over all C need not transport to even C. |
| F3 285 non-square composite zeros | Correct but underdocumented in the table. Independently enumerated all ordered-root possibilities (via u≤B and divisors of n+u) for **all 285**: no hits. Their zeros obstruct positivity at these inputs, not the identity. Primality is absent from the identity, not necessarily from future estimates. |
| F4 14 global / 38 restricted zeros | **Incomplete in the memo:** the 38 𝔊*-zeros are omitted. Independently confirmed all 14 global zeros. Among the 38 listed 𝔊*-zeros, exactly **24 have global (★) hits**, e.g. 37=`4·1·2·5−1−2`. Thus 𝔊*-vanishing does not imply ES_k(C,p)=0 at every C; it obstructs only the restricted family. The 𝔊* restriction itself was not re-certified here. |

No HOT LEAD is supported or claimed. “Passes all four trivially” must mean consistency of the identity, not survival of a positivity argument.

## Literature audit and limits

* **Popa 2018**, [arXiv:1408.4998](https://arxiv.org/abs/1408.4998), primary text: checked (1.5), Theorem 1, (1.7), Remark 3.2, Assumption 3.3. Confirms slash normalisation, projective stabilisers, M_k+S_kᶜ rather than S_k, and the coset-bijection hypothesis. For Δ the latter follows by lifting the inverse reduction modulo Q; injectivity follows from both matrices being −I modulo Q. Additivity handles composite N.
* **Shimura 1974**, [Acta 132, 245–281](http://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6170-11511_2006_Article_BF02392117.pdf), primary text: Theorem 4.5 really carries (3.5.1–2), (3.6.1), and normal-subgroup conditions (i–iv). It is not an assumption-free shortcut. Its k=2 auxiliary-space correction is consistent with the degree term; no exact constants were inferred from garbled OCR.
* **Cohen–Strömberg 12.4.11:** original book **not obtained**. Checked the complete displayed quotation in [Cason et al., arXiv:2407.11694, Lemma 2.2](https://arxiv.org/abs/2407.11694), including weighted class numbers, lift conditions, CRT cusp parameter and A₄. It agrees with the memo's derivation. This is a secondary check of C–S, not primary verification; the memo honestly discloses that limit.
* **Kane–Pujahari**, [arXiv:2010.15325](https://arxiv.org/abs/2010.15325), primary Lemma 3.3 and following remark: higher weight 2+2k, arbitrary modulus, corrected Mertens constant; k=0 is quasimodular. **Kane–Pujahari–Yang**, [arXiv:2405.14234](https://arxiv.org/abs/2405.14234), primary Theorems 1.6/1.7 and Corollary 1.8 confirm higher moments and the cited vanishing classification, with `1≤m≤M`. No literature novelty follows from this memo.
* **Eichler–Zagier:** original book **not obtained**; publisher access returned a book landing page. The theorem-number check remains secondary. Formal substitution `qF(Q²τ,−Qτ)` has the right exponent Qn+1, but holomorphic torsion-specialisation alone does not justify the weight-2 nonholomorphic completion or D=0 terms. Keep Remark 2.2 an unproved assessment, not a modularity theorem.
* **Serre 1997:** original AMS PDF returned a challenge, so primary verification remains **unresolved**. The cited fixed-prime, level/weight-aspect equidistribution statement, even if granted, supplies no uniform single-N bound as N=Qn+1 grows. The memo correctly does not use it as such a proof. Do not upgrade LIT_CHECK's confidence.
* LIT_CHECK retains acknowledged convention errors: its Popa dimension sentence needs **projective** index, its Γ(N) dimension quotation needs k≥3, and its KPY divisor interpretation must distinguish d|n from 2d|4n. Its C–S sign warning is not a criticism of sources that define A₂,A₃ as signed terms.

## Required fixes, in priority order

1. Remove §7's universal-sounding “does not give (★) beyond Γ(4)”; replace by the proved necessary alignment condition and the stated finite non-firing evidence. Likewise say **no discriminating positivity input supplied**, not that the identity is intrinsically insensitive to arithmetic/parity. The spectrum and E do depend on the input.
2. Complete F4 with the 38 restricted zeros / 24 global-hit distinction, and explicitly identify F3's 285 certified zeros. Do not extend an all-C obstruction from the 14 global zeros to all 38.
3. Add `gcd(Q−1,2Q−1)=1` in Proposition 4.4(c); qualify the Γ(4),k=3 exception as absence of a **ρ-free** alignment constraint. Keep Theorem 2 and its general consequences conditional everywhere, including “a clean trace formula … exists” in the bottom line.
4. Correct the acknowledged LIT_CHECK convention errors before reusing its formulas. Preserve the primary-source access limitations for C–S, EZ and Serre; EZ's weight-2 completion remains unworked.

After these fixes, accept **narrowed / no positivity mechanism obtained**, with a certified finite identity and a conditional general theorem. Do not export an unconditional trace theorem or a universal “no positivity” obstruction.
