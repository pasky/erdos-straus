# SQSIEVE hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/z53-sqsieve` at `548ab72f6a597e7543c23e95136b07186454b0e2`.
**Theorem A survives: R(n) ≪ε n^(12/37+ε) for every n≥2, relative to its stated classical inputs.**
**C3 survives under (H), but does not close quadratic-minorant lower bounds using signed inputs.**
ES remains OPEN. The fixes below concern scope and interpretation, not a counterexample to Theorem A.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| §4.1 block cover, Lemma 1′, square sieve | CORRECT | All positive triples covered, diagonal removed; support condition needed only on positive squares. |
| Lemma W | CORRECT | Quadratic completion, Gauss opening, degeneracy, zero frequency and CRT all check; Weil applies to nonzero Kloosterman parameters. |
| Lemma P | CORRECT | Fourier sign, factor V/(4CQ), and frequency argument all check. |
| Proposition D | CORRECT | Re-derived both derivative terms, zero mode, Abel factor and all frequency powers; no primality of n used. |
| Theorem A | CORRECT | Every block and every error term covered; worst block (12/37,13/37,12/37); cube 17/54. |
| Theorem A′ / A″ | CORRECT-WITH-FIX | General-pair derivation works; replace the reused γ≤13/37 by γ≤1−2θ<1/2 in the general-κ argument. Literature/conjectural dependence is honest. |
| §5.1 reach | CORRECT | Independently solved all linear inequalities: the three diagonal intervals agree exactly. |
| B2(a) | CORRECT | Fejér positivity gives max |Xℓ|≥√N/2. |
| B2(b) | CORRECT-WITH-FIX | Proof treats Q≤W, omitted from the implementation definition/statement; also repair the frequency-block rounding inequality. No universal barrier outside this scope is established. |
| C1 / BM | CORRECT-WITH-FIX | Reciprocity proof and square obstruction correct; the Jacobi weight has modulus n, not necessarily conductor n. |
| C3 lemma | CORRECT | Both signs of a₂ give the asserted non-positive diagonal coefficient under (H) and ν≤P₀−1. |
| C3 “closed” reading | GAP / WRONG subclaim | Signed-input routes remain open; the claim that the signed combination must be ≤0 at odd squares is false (exact counterexample below). |
| C4(a), divisor rewrite | CORRECT | Conic factorisation and divisor reformulation are identities, not impossibility results. |
| C4(b), representation-route closure | CORRECT-WITH-FIX | Restrict to the cited divisor-series decomposition and fixed-congruence implication; blanket representation-count exclusions are Assessment. |
| §7 numerical evidence | AGREES | Full lemma/exponent/reach/Poisson/F3 reruns and two decisive balanced strips agree; details below. |

## Independent exponent and coverage derivation

1. Since u+B≤2uB≤2uBC, n≥2uBC and n<4uBC≤2n. Dyadic parameters ≥1/2 give
   n/32≤UVW<n/2 and O(log³n) nonempty blocks, including coordinates equal to 1.
   Symmetry permits U≤V. Fixing u gives B|(n+u); fixing C gives (4Cu−1)|(4Cn+1).
   Hence N≪ε n^ε min(U,W); their divisor arguments are ≤4n².
2. A non-diagonal triple maps at most two-to-one to (C,k), s=u+B∈(V,4V], f=(u−B)².
   Diagonal triples number ≤τ(n). Smoothed support has k≥1 and positive squares f≤25V².
   For m²≤2^P₀, at most P₀/2 auxiliary primes divide m; expanding σ² proves (4.1),
   including negative nonsquares and excluding f=0. S₁ safely includes the latter.
3. For C=c₀+Qj, g‴=(3/2)ℓnQ²/C⁴, so λ₃=(3/32)|ℓ|nQ²/W⁴ with ratio 16.
   The third-derivative test yields
   E≪|ℓ|^(1/6)n^(1/6)W^(1/3)Q^(−2/3)+|ℓ|^(−1/6)n^(−1/6)W^(7/6)Q^(−5/6)+2.
   Abel and the complete-sum aggregate contribute VQ^(1/2)/W. With M=QW/V,
   summing |ℓ|^σΨ(ℓ/M)≪M^(1+σ), also for M<1, gives respectively
   Qn^(1/6)W^(1/2)V^(−1/6), Q^(1/2)V^(1/6)Wn^(−1/6), Q^(3/2).
   The zero mode is O(V/Q+V/W); thus every term of (4.2) is recovered.
4. Put d=1/6+γ/2−β/6 and e=β/6+γ−1/6. The complete list of exponents after sieving is
   β−ρ, β−γ−ρ, d−ρ, e−ρ, −ρ, β−2ρ, β−γ, 2ρ+d, ρ+e, 3ρ, plus τ(n).
   Balance β−ρ=2ρ+d: ρ=(7β/6−1/6−γ/2)/3, leading exponent (11β+1+3γ)/18.
   On α+β+γ=1 this is (12−11α−8γ)/18. Equating its maximum at α=γ=θ to θ gives θ=12/37.
5. Blocks with min(α,γ)≤θ use the divisor bound. The remaining region has vertices
   (α,β,γ)=(12/37,13/37,12/37), (12/37,12/37,13/37), (25/74,25/74,12/37).
   The maxima over ALL listed terms at these vertices are 12/37,104/333,421/1332.
   Here 4/333≤ρ≤1/37 and 2ρ<γ; hence P grows polynomially, enough primes exist,
   2^P₀≥25V² eventually, and Q≤W. O(1/log n) block discrepancies cost constants;
   finitely many small n and log³n are absorbed into the ε-bound. No uncovered block remains.
6. General pair: frequency summation gives Q^(3/2+κ−λ)n^κW^(λ−κ)V^(−κ).
   For λ=κ+1/2, ρ=((1+κ)β−κ−γ/2)/3 and θ=4/(13−4κ).
   Independently factored all vertex deficits as functions of κ: they are nonnegative for 0≤κ<1/4,
   with ρ>0 and 2ρ<γ. The phase condition is |ℓ|n≫W², valid since γ≤1−2θ<1/2.
   κ=13/84 gives 21/65; κ=0 gives 4/13. Solving diagonal inequalities gives exactly
   (4/13,14/41), (55/181,197/575), (1/4,5/14), respectively.

## Required fixes, in priority order

1. **C3 scope and false sign claim (§6, summaries, proposed FRONTIER text).** Retain the lemma,
   but replace “closed for quadratic σ-minorants” by “under (H), no positive diagonal main term;
   a lower bound requires signed auxiliary-sum information.” (H) is only checked on finite strips,
   not proved for arbitrary application weights. It and ν≤P₀−1 must accompany every general summary.
   At the memo's odd square n=10000000200000001, W=6250000, s∈(20000,40000], P=1000,
   independent exact enumeration gives P₀=135, |A|=3561, Λ=502247, Σν=360, max ν=2, (H)=true, no squares.
   The valid minorant D(x)=x²−1681 has diagonal −5505666, **signed part +21872**, full sum −5483794.
   Thus only diagonal+signed must be ≤0 at squares; the signed part need not be. The claimed P₀²
   precision also requires a normalization of D, whose coefficients can otherwise be freely rescaled.
   A finite example even satisfies (H) and certifies positivity with signed inputs: primes {3,5,7,11,13},
   weight 2 at a=1 and weight 1 at a∈{2,19,23,79}, D=(x²−9)/16, yield ΣwD=1>0.
2. **B2 scope/rounding.** State Q≤W for the proved implementation class, or prove the missing Q>W case;
   Proposition D explicitly allows Q>W, so this restriction is not inherited. Replace the false step
   L₀/(2Q)−1≥L₀/(4Q) under L₀≥2Q by counting ≥floor(L₀/(2Q))≥L₀/(4Q) complete integer blocks.
   Use the assumed eℓ(W/Q)≥c√(W/Q) directly, rather than √(W/Q−1), which vanishes at Q=W.
   Balanced-block conclusions and FRONTIER wording must retain the precise implementation restrictions.
3. **C4 and other summaries.** METAPLECTIC_ES §1 explicitly labels modular normalization/“main term”
   readings Assessment; its proved identity is a Dirichlet-character divisor decomposition. HYPSUMPROD
   Cor A′ concerns a fixed congruence implying a tie for *all integers x*, not all possible representation methods.
   Preserve those scopes. Replace §6's “must carry” the BM weight by “one available square-sensitive weight”;
   necessity/uniqueness is not proved. For composite n distinguish modulus n from primitive conductor;
   at squares the character is principal on units. Summaries of Lemma W must allow exceptional frequencies, using the
   proved aggregate ∑c|G_c(ℓ)|≪Q^(3/2), not a uniform individual √Q bound. The large-sieve Assessment
   in B2 Remark 3 is not a proved exclusion either: Heath-Brown's squarefree-variable inequality needs
   grouping these possibly negative f-values by signed squarefree kernels and bounding coefficient L² mass.
4. **Minor labels.** Floating-point Fourier/Poisson checks are numerical evidence, not exact certificates
   without error bounds. This does not weaken their independent analytic proofs. Fix A′'s reused γ-bound as above.

## Reproduction and source verification

All shell invocations had timeout and memory/CPU ulimits (2 GiB virtual-memory cap); no unbounded arrays.
Reran source scripts from an archive of the reviewed commit: `checks.py 23 20000` (27962 Weil,
273594 CRT, 556 Kloosterman, 87388 BM cases), all four Poisson instances, exponents, reach, and F3
(150 primes + 150 squares). Outputs match their committed files byte-for-byte.
Balanced prime/square P=1000 runs reproduce |A|=3403/3561, max |S_Q|=217/221, rms=57.8/59.6 and (H).
F3 reproduces means −2.124/−3.068, standard deviations 4.863/4.868, mean square counts .407/0;
this is finite evidence, not a pointwise impossibility theorem. No claim to rerun all 14 strip samples.
New `scripts/z53_xrev_sqsieve_scope.py` independently streams the odd-square strip and checks the C3 examples exactly.
Primary sources opened: [IK Thm 11.11/Cor 11.12](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf),
[Titchmarsh Thm 5.11, printed p.106, scan p.58](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)
(read rendered formula), and [Bourgain Thm 6](https://arxiv.org/pdf/1408.5794v2), including its phase-class caveats.
**Verdict:** S1 strengthened is justified; S2 narrowed requires the repaired scope; S3 is an unsigned-input
obstruction under (H), not closure of quadratic-minorant methods. ACCEPT-WITH-FIXES before recording the memo's summaries.
