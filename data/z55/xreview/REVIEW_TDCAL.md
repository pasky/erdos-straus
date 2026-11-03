# Hostile cross-review: Z55_TDCAL

**Verdict: ACCEPT-WITH-FIXES.** The main calibration results survive independent derivation.
The conclusion “narrowed (calibrated)” is justified; no pointwise power saving, TD, TS, MIX, or ES result follows.
Reviewed `side-agent/z55-tdcal` at `36c405644bb9540b13454ee66c80e5c149a458b3`, not an evolving checkout.
Sources/scripts/data were extracted to `/tmp/xrev_TDCAL`; all shell executions had timeouts and memory/CPU limits.

## Per-claim audit

| Claim | Classification | Independent check / scope |
|---|---|---|
| Prop A identity and divisor majorant | CORRECT | Bijection uses M=n+u+B; for fixed M both factors divide M, giving ≤τ(M)², without a coprimality assumption. |
| Prop A(a),(b) | CORRECT | For Y≤U², M≪U⁴ and the divisor bound gives (Y+2U)U^ε; for Y>U² use (c). Markov at Y=U gives U^{η+ε}. |
| Prop A(c) | CORRECT | Each pair contributes Y/(uB)+O(1); summing yields O(U²), and the reciprocal-pair sum is ½(log 2)²+O(1/U). |
| Cor A′ | CORRECT | For each U, [U⁴,(U+1)⁴) needs O(U²) length-U windows; O(Z^{1/4}) choices give Z^{(3+η)/4+ε}. Dyadic summation is harmless. |
| Remark A″ | CORRECT | Simultaneous inequalities U<u and B≤2U give precisely the displayed integer interval for U and multiplicity ≤U₀. |
| Remark A‴ | CORRECT | Larger cycle element fixes B=r_u. The block discrepancy computation and 3/56 exponent agree with the checked Titchmarsh theorem; details below. |
| Lemma S(a) | CORRECT | Count multiples of m by floor differences; expanding floors gives the stated ψ signs and 2U log 4+O(1/U). The slice is not the full divisor sum. |
| Lemma S(b) | CORRECT | Two divisibilities imply gcd(u,B) divides p; p>2U forces coprimality and hence product divisibility. Prime restriction is essential. |
| Lemma S(c) | CORRECT | p≡−s mod m gives m divides p²−D; fixed D,m determine positive s. Positivity of p²−D follows from the standing range. Sum τ(p²−D), then take X=U^{1−η}. |
| §6 Fourier identities | CORRECT | Smooth zero extension across D≤0 is justified by Ψ's support away from zero; support is interior to (0,1). Fourier evaluation at θ_m gives e(−νp/m). |
| Thm B(i),(ii) | CORRECT | Coefficients are φ(m/U²)(U/m)Φ̂(νU/m); Schwartz decay controls the absolute tail uniformly under bounded κ_m. |
| Thm B(iii) | CORRECT | ρ=W²/U³, λ=hU³/W give derivative scales Wρ^{−j}, amplitude scales ρ^{−j}, and λρ=hW≥U^σ. Outside the band, integration by parts beats the polynomial count of m,ν. |
| Remark B2 | CORRECT | κ_m can absorb the entire TD oscillation; ν→ν+jm is invisible on the remainder grid. Band separation is representation-dependent, not a nonimplication theorem. |
| Prop C(i),(ii) | CORRECT | Each ℓ² norm is O((1+|ν|/U)^{−A}); positivity and continuity of Φ̂ at zero give ≫1 on ≍U frequencies. Thus total ≍U and deficits U^η, U^{1/2}. |
| Prop C(iii) | CORRECT, scoped | Re-derived BILINDIV 4.3: Parseval mass ≫U, negligible low band, and second-derivative integral bound give maxν‖cν‖₂≪(hU)^{−1/2}; division yields ≫h^{1/2}U^{3/2}. Only its smoothed level weights and declared bound class are covered. |
| Prop C(iv) | Assessment, appropriately labelled | Under quantitative support overlap, mass ≍W²/U, band length ≍hU³/W and max norm ≪W^{3/2}/(h^{1/2}U²) give the stated benchmark. This does not establish actual strip occupancy. |
| Prop D(i) | CORRECT | δ≤1/4 prevents overlapping translates; the sandwich and N₂≤A follow. Enlarging δ to U^{−η+ρ} keeps Fourier cutoff below U^η and proves TD⇒NC with ε loss. |
| Prop D(ii), sufficient bound | CORRECT | Nearest j≥1 gives |D−j²|≤δ(2w+δ)≤9Uδ. The injection proves A≤ΣN^[τ] and the stronger bound suffices. |
| Prop D(ii), “converse fails” | GAP if read as nonimplication of uniform bounds | Strict non-reversibility of the point-set inclusion does not prove that NC cannot imply the τ-window estimate on this arithmetic family. Restrict this sentence as in fix 1. |
| Prop D(iii) | CORRECT | The j-interval has length ≤2T/√D. Dyadic blocks contribute min(X,U)X^{−1/2}U^ε; summing below/above X=U gives U^{1/2+ε}. |
| Prop D(iv) | CORRECT-WITH-FIX | Integer-square levels give N₂²≤P. Expanding Fejér gives the exact identity, and weights ≥½ give the claimed ℓ² bound. Distinguish the two different H cutoffs in its final application (fix 2). |
| Prop E(i) | CORRECT | Additive orthogonality detects m divides p+s; Poisson in s collects ordinary Fourier coefficients, with no inverse-residue phase in this particular completion. |
| Prop E(ii) | CORRECT, scoped reference | Recomputed DFI/BC necessary conditions from their displayed bounds; see source check below. This excludes neither other transforms nor spectral methods. |
| Prop E(iii),(iv) | Assessment, appropriately scoped | Benchmark limitation follows from C; no BI theorem is asserted. The inherited second-derivative term is Nλ^{1/3}≈U²(U^{−2})^{1/3}=U^{4/3}. |
| Theorem H / proposed FRONTIER text | CORRECT with scope retained | Inherit the verified statements. “Carry only” means up to O(U^{−A}), not literal compact Fourier support. Averaging is over integers; the prime assertion is an exceptional-set bound. |
| T1 / tied-modulus screen | CORRECT-WITH-FIX | Composite-valid identities retain the size hypotheses and product-divisibility convention. §12 incorrectly gives the w-tolerance as U^{1−η}; see fix 3. |

## Decisive derivations and citations

- **First-order bound:** on blocks L≈U^{1/2}, f⁽⁴⁾≈h/U with a bounded derivative ratio.
  Titchmarsh 5.13 with k=4, K=8 gives L(h/U)^{1/14}+L^{3/4}(U/h)^{1/14}.
  Erdős–Turán with H=U^{1/15} gives discrepancies O(U^{−1/15}+U^{−3/56}) up to logs.
  The moving threshold costs O(U^{1/2}); integrating 1−U/u over (U,2U] gives (1−log 2)U.
  Checked the theorem itself, printed p.107, in [Titchmarsh](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).
- **Divisor calibration:** [Ivić (1.13)](https://www.numdam.org/item/10.5802/jtnb.669.pdf) explicitly calls the square-root short-difference estimate Jutila's conjecture.
  [Li–Yang v2, Theorem 1.2 and Definition 1.1](https://arxiv.org/pdf/2308.14859v2) give θ*=0.3144831759741… for global Δ.
  Neither citation gives the central-slice asymptotic. The search-limited wording is honest.
  The appended correction in `LIT_CHECK.md` is right: differentiating x log x adds the missing +y, so the interval constant is 2γ, not 2γ−1.
- **Kloosterman calibration:** [Bettin–Chandee](https://arxiv.org/pdf/1502.00769), (1.1), quotes DFI's bound with exponents 3/8 and 11/48; (1.2) is the BC theorem itself.
  With V=uv, the DFI/trivial ratio is ≥p^{3/8}V^{−37/96}, forcing V≳p^{36/37}.
  BC's first summand gives ratio ≥(4C̄)^{1/2}A^{7/20}V^{−1/40}; V=p/(4C̄) forces C̄≲p^{1/21}.
  DFI was checked here through this named secondary quotation, not its original paper; no new DFI application is needed for the verdict.

## Numerical reproduction

Recompiled the supplied C programs with GCC; reran Python through `uv`, after inspecting loop sizes and allocations.
No numerical computation is used to certify an asymptotic theorem.

| Data / operation | Recomputed result | Agreement |
|---|---|---|
| `window.c`, (10⁸,20000,100) | ΣN₂=4662, max=4, M-majorant=4707; histogram 15865,3642,460,32,1 | Exact |
| `window.c`, (10¹²,2000,1000) | ΣN₂=461, max=3, M-majorant=901; histogram 1599,347,48,6 | Exact |
| `check.py`, 200 primes after 10⁸ | 0 failures; mean E1=271.88, E1⁺=151.30 | Exact integer checks reproduced |
| Same, τ-window means T=0,1,4,16,64 | 1.695, 2.760, 5.715, 19.860, 73.835 | Matches |
| Same, NC means δ=.02,.05,.1 | 6.440,15.415,30.785 versus 6.052,15.130,30.260 | Matches; floating-point evidence only |
| Regenerated generic inputs; `tail 32` | 96000 samples; second moment .9962; tails at 1,2,2.5,3,3.5: .3653,.01842,.001875,.0001146,0 | Matches |
| Regenerated three structured families | 48000 samples; second moments .9965 (near squares), .9993 (rational), .9874 (fourth powers) | Matches stored tails |
| Regenerated both square controls | 19200+96000 samples; second moments 1.0052,1.0060; second-set tail at 3.5 = 1/96000 | Matches |
| Independently aggregate stored `td_gen*.out` | Count-error sds 2.79123,3.30747,2.74728,2.16613; pooled rms .99773,.99810,1.00091,1.00557 | Matches §10.4 rounding |

The four-scale aggregation is a recomputation from stored rows, not a fresh rerun of every underlying TD row.
The generic/structured/square tail sums were actually rerun. Their Gaussian compatibility is descriptive only;
correlations and uncalibrated sampling error prevent a significance claim or a proof of TD.

## Required fixes, in priority order

1. **Logical scope, §8(ii):** replace “The converse fails” by “The reverse point-set inclusion fails; no converse implication between the uniform bounds is established.”
   For example p=100000007,U=100,s=298,m=10433 gives D=47072, j=217, τ=−17.
   At δ=.02, |τ|≤13Uδ=26 but |√D−217|≈.039174>δ. This disproves only reverse inclusion, not an asymptotic implication.
2. **Cutoff bookkeeping, §8(iv):** call the Fejér cutoff H₀=⌊U^η⌋ and the Fourier cutoff H₁=U^{η−ρ/2}.
   From Σ_{h≤H₀}|T(h)|≪H₀U^{1−η}, bound the smaller partial sum by the same RHS.
   Multiplication by δ′=U^{−η+ρ} gives O(U^{1−η+ρ}); the main term and tail are handled as in D(i).
   This proves the claimed ε-lossy sufficient implication without identifying two unequal values of H.
3. **Tolerance, §12 item 3 (and clarify §15):** NC's distance in w is U^{−η}, not U^{1−η}.
   The latter is the scale of the relaxed discriminant tie |D−j²| at w≈U.

The fixes are local, not a rejection of the calibration. Keep C(iv) as Assessment and keep the distinction between
sharp TD and smoothed-piece benchmarks. The “narrowed” verdict survives; nothing here touches ES positivity.
