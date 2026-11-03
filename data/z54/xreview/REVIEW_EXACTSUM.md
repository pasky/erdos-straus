# z54 EXACTSUM — independent hostile cross-review

**Verdict: ACCEPT-WITH-FIXES.** The exact identities, square lemma, shell-count lemma, compatible window, and scoped no-go survive. The advertised numerical conductor cutoff does not follow: replace it before recording/exporting the result. ES remains OPEN.

Reviewed `side-agent/z54-exactsum` at `fb3b7a8a8a4eebd2e8440015e53728c774c689d6`, including `Z54_EXACTSUM.md`, its engines/data, and the cited GX/GL proofs. No changes to the source branch.

## Per-claim findings

| Claim | Classification | Independent check / limitation |
|---|---|---|
| Prop. 3.1, frequency identity | CORRECT | Since `0<u<w`, `(p+u)/w=ceil(p/w)=2w″`; the mod-4 condition is `k≡6 (8)`. Additive orthogonality for `u|(w″+1)`, followed by reducing `h/u`, gives precisely the stated `1/u` and phase, including `e(a/q)`. |
| Prop. 3.2, conductor identity | CORRECT | Primitive characters at each odd prime are all characters except the principal one. Their product sum is the stated product; the unique real primitive character at squarefree `f` is the Jacobi character. Summing over `f|u` gives `φ(u)1[m=1]−∏(1+(m/ℓ))`. Coprimality follows from `gcd(u,p)=1`; multiplying by `2/φ(u)` gives `R−G`. |
| Lemma 3.3, square vanishing | CORRECT | At `n=m²`, `gcd(w″,m)=1`; `(u/w″)=(-m²/w″)=-1` for `w″≡3 (4)`. Reciprocity and `u≡1 (4)` give `(-w″/u)=-1`, excluding genus and class hits. The inherited `M=M^cls=0` is checked below, so all three T-layers vanish. |
| Lemma 4.1 | CORRECT | Floor counting, inverse reciprocity, Vaaler, and the exponent-pair scale all check; derivation below. Its stated restrictions, especially `2U≤p`, matter. This is a plain-shell statement, not a squarefree-shell theorem. |
| Cor. 4.2 | CORRECT | Summing residue-class errors costs `φ(q)`; the harmonic sum in one progression is `log(2)/q+O(1/K)`. The displayed endpoint error `φ(q)U/(fK)` must remain. On reconciled windows `K>U`, it is harmless in the stated certified range. |
| Prop. 4.3(a), GX relaxation | CORRECT | Inspected GX Theorem X steps (i)–(iii): `α₁<1/5` is used only to bound the large-convolution-factor tail by `p^(−ε/2+o(1))/u`. Replacing that implication by C4′ preserves the proof. |
| Prop. 4.3(b), explicit window | CORRECT | Exact rational recomputation: all eight slacks are positive; the last is `1/2400`, giving `η=1/2480`. `τ=0.2535`, the smallest-K H-check is `0.0409>1/30`, and `c=9.8553429645·10⁻⁷`. |
| Prop. 4.3(c), window shape | CORRECT | C1+C2* give `3α₁<1−τ−4ε<3/4`. Combining E with `1−β>α₁>α₀` gives `α₀>κ/(1+2κ−λ)` and the stated level exponent. Recomputed A-process pairs and the tabulated bounds; maximum is `0.025`. Empty-pair cases do not assert existence. |
| Prop. 4.3(d), conductor criterion | CORRECT-WITH-FIX | Substituting `f=d,q=8d` gives exponent `(2+κ−λ)/(1+κ)=35/31`, but its numerical cutoff must be **strictly below `1/2800`**, not `0.00036`. EPC gives a limiting exponent `1/3`, not a power-saving result at the endpoint. |
| Theorem N, including constants | CORRECT | Only `u=f` occurs because the next admissible multiplier is 5. Prime `w` in the specified mod-4 class exists; the CRT interval for `w″` is longer than `12f`. The resulting n is `1 mod 24`, all coprimalities hold, and the hit outweighs `O(τ(n+f)/f)` other contributions. PNT mod 4 gives `(1/3−o(1))U₁/log U₁`, and the frequency triangle bound gives half that. |
| CERTIFIED identities / engine agreement | CORRECT to stated rounding | Independent exact rational checks on all 19 hard inputs and five square controls; 12 conductor-engine reruns and two complete frequency-engine reruns agree with saved data. Saved maximum pointwise roundoff is `4.44·10⁻¹⁶`. |
| §6 variance and frequency evidence | CORRECT-WITH-FIX | Main tables and medians reproduce. The strict ceiling `m_f≥16 carries ≤0.003` is false: maximum is `0.003440…`. The empirical `f<u^(1/2)` bucket is not the theorem's certified cutoff; variances are not monotone under taking sub-buckets. |
| Narrowed verdict / labels | CORRECT-WITH-FIX | The blockwise n-uniform triangle strategy is rigorously excluded; prime-sensitive, one-sided, and grouped-block strategies are not. Plain-to-squarefree transfer and extrapolation to reconciled windows remain unproved. Cross-u decorrelation is a finite-sample heuristic, not an established asymptotic or a B2 equivalence. |

## Proof details and decisive sources

For Lemma 4.1 set `A=U/f,B=2U/f`, and choose `v_k≡−p f̄ (k)`. The count is
`(B−A)/k−ψ((B−v_k)/k)+ψ((A−v_k)/k)`.
Since `f̄/k+k̄/f≡1/(fk)`, and `f|q`, the inverse term is constant on `k≡c (q)`.
The error is therefore `S(p+U)−S(p+2U)`, with `S(Z)=Σψ(Z/(fk)−θ_c)` and `p≤Z≤2p`.
Writing `k=c₀+qj`, the Fourier phase is `hZ/[fq(j+c₀/q)]`.
Its negative derivative is close to `y j⁻²`, `y=hZ/(fq)`, and `y/(K/q)²=hZq/(fK²)≥1`.
Dyadic splitting can use scales `K/q` and `K/(2q)`; sufficiently large J₀ handles the shift and derivative tolerances.
Thus `|T_h|≪h^κ p^κ f^(−κ)K^(λ−2κ)q^(κ−λ)`.
Vaaler and `κ>0` give `(K/q)/H+1+H^κ p^κ f^(−κ)K^(λ−2κ)q^(κ−λ)`.
Balancing gives exactly the stated H* and `E_fq=E f^(−κ/(1+κ))q^(−λ/(1+κ))`.
For `q=8d`, the relevant classes have `c≡6 (8)` and `gcd(c,d)=1`, not `gcd(c,8d)=1`; apply Lemma 4.1 directly to these classes. The same error count works (Cor. 4.2 literally sums unit classes only).

Source opened independently: [Trudgian–Yang, arXiv:2306.05599v3](https://arxiv.org/html/2306.05599v3), §1.1 equations (1.1)–(1.2): derivative convention, subinterval uniformity, and `y≥N^σ` agree. §1.2 gives the A/B transformations and attributes the `9/56`, `32/205`, `13/84` pairs to Huxley–Watt, Huxley, Bourgain, with ε-losses. The decisive compatible window uses the classical exact pair, not an ε-free version of those modern pairs.

The inherited square-density assertion can also be checked without accepting it on authority: at `n=m²`, genus matching forces `(−u/w)=1` and `(−2w/u)=1`. Reciprocity implies `χ₋₄(w)=(2/u)`. But `w≡−(m²+u)/2 (4)` gives the opposite sign for each of `u≡1,5 (8)`. Hence every genus-density term is zero; the exact-class factor is supported inside the genus factor, so `M^cls=0` too.

## Recomputations

Reproducer: `scripts/z54_xrev_exactsum_check.py /tmp/xrev_EXACTSUM` after extracting the reviewed files and compiling `cond`/`wsum` there. Run via `timeout 180s uv run --no-project …`, under `ulimit -v 6000000; ulimit -t 180`. Every shell invocation and engine subprocess in this review was time-limited; allocations are bounded (small tabular data, streaming per-input engines, no Cartesian-product arrays).

- Verified all 1,000 random inputs: distinct primes `1 mod 24`, deterministic Miller–Rabin bases valid below `2^64`.
- Recomputed every profile group using sample variances of **summed** buckets, including covariances.
- Dyadic single-integer fractions: `0.896294…` through `1.028811…`; ≤3-integer fractions: `0.962150…` through `1.022356…`.
- Largest ≥16-integer fraction: `0.003440…` (dyad, `10¹³`); `10¹²` also exceeds 0.003 (`0.003326…`).
- Largest low-relative-conductor variance fraction: `0.016251…` (std composites), agreeing with ≤1.7%.
- Cross-u diagonal ratios: std `1.190937,0.969074,0.915783`; dyad `0.985491,0.830539,1.146161`.
- Frequency median rms/benchmark for q≥11: `1.009831,0.984230` at `10¹²`; `1.036290,0.985843` at `10¹⁴`.
- All 19 hard cases agree in exact R and rational G (within stored six-decimal rounding); full conductor and Ramanujan-frequency identities hold pointwise.
- Theorem N example: independently obtained `D₁₉₇=94/49=1.918367…`, `P₁₉₇=189/197=0.959390…` at `n=1000223521`.
- Recompiled engines; all columns agree in one profile per window at each of `10¹⁰,10¹²,10¹⁴`, and in two full q≤99 frequency runs. Only existing misleading-indentation compiler warnings appeared.

## Required fixes, priority order

1. **Correct the certified cutoff everywhere (§§0,4,7).** `η−(35/31)·0.00036=−1/310000<0`. The criterion cannot certify that cutoff, even with δ=0. Use `d≤p^0.00035` (leaving any `0<δ<1/124000`), or state any fixed exponent `<1/2800`. Under EPC, say “limiting reach exponent 1/3”; with power saving use a fixed margin below 1/3, retaining the p-saving and exponent-pair ε-losses.
2. **Separate the measured bucket from the certified range.** The ≤1.7% statistic concerns the summed, relative bucket `f<u^(1/2)` on non-reconciled windows. It neither identifies the variance of the `f≤p^η′` sub-bucket nor proves a transfer to reconciled/GX windows. Variance of a smaller signed bucket need not be smaller. Keep any claimed relevance to the theorem explicitly Assessment (at the measured sizes the explicit cutoff is even below 2).
3. **Fix the strict empirical ceiling.** Replace `≤0.003` by `≤0.0035` (or `≤0.004`) everywhere. Mark two-decimal intervals as approximate; e.g. the ≤3-integer maximum is 1.022356…, not literally ≤1.02.
4. **Preserve scope in exports.** No certified bound for squarefree GX layers is obtained here. “Only random-model cancellation”, extrapolation of variance to 𝔚, and reduction to high-conductor parts of both T-layers must remain heuristic/conditional; a low-D_f estimate alone does not bound `T_w=G−M`. Theorem N does not exclude prime-only or one-sided methods.

After these fixes, **“narrowed” follows**: a genuine plain-shell positive result coexists with a genuine, explicitly scoped blockwise no-go. Neither gives the missing ES-strength remainder estimate.
