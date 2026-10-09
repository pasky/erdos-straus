# RA hostile referee report: effective Theorem 2 and its twist

**Verdict:** no FATAL or MAJOR obstruction to the stated large-sieve bounds or constant growth found.
Two MINOR exact-kernel assertions need correction; neither changes the absolute-value estimates.
This verdict is relative to the stated trace-formula, Weil, and Selberg black boxes, not a numerical
certification of the unspecified twisted Weil constants C_W and B_W.

Sources checked directly: DI journal pp. 228–231, 242–245, 253–263 (rendered scan), also pp. 227,
250; Drappeau pp. 10–15, particularly Lemmas 4.2, 4.6 and Proposition 4.7, with (4.26)–(4.27)
checked in the rendered PDF rather than trusting extracted fraction bars.

## Findings requiring edits

1. **MINOR — wrong sign in the “exact” holomorphic kernel.**
   `ttl3_thm2_effective.md:110–115` repeats a sign inconsistency on DI p. 258.
   Petersson with its stated positive off-diagonal prefactor gives
   `E_K(x)=2 Σ_{l≥1}(2l−1)(−1)^l exp(−(2l−1)/K) J_{2l−1}(x)`.
   Consequently `E_K'(0)=−exp(−1/K)`. The displayed positive ξ-integral instead has derivative
   `+exp(−1/K)`, since `∫₀¹w(ξ)ξ dξ=2exp(−1/K)`.
   At K=1, x=0.1, independent series/quadrature give −0.036735759024 and +0.036735759025.
   **Repair:** negate the integral, or define its negative as the kernel and negate the
   off-diagonal prefactor. All subsequent bounds use absolute values and remain unchanged.
   The twisted Step 6 inherits this sign correction.

2. **MINOR — the printed pre-Kuznetsov kernels are not literally identical.**
   `ttl3_thm2_twisted.md:127–129` overstates the correspondence with DI.
   Writing t for the integration parameter and r for the spectral parameter, DI p. 253 has
   `H_DI(r,t)=cosh(πr)/(cosh(π(r−t))cosh(π(r+t)))`, whereas rendered Dr p. 14 prints
   `H_Dr(r,t)=cosh(πt) H_DI(r,t)`.
   Moreover, at weight zero, `I_Dr(x)=−2ix∫K_{2it}(xv)dv/v`, whereas
   `D_DI(x)=−2it/sinh(πt)∫K_{2it}(xv)dv/v`.
   Thus one must also include Dr's prefactor `|Γ(1+it)|²/(4π²)=t/(4π sinh(πt))`:
   its product with I_Dr is `x D_DI/(4π)`, yielding the same geometric Gaussian transform
   up to a fixed factor. The additional printed spectral factor is not a numerical constant.
   **Repair:** write this bridge explicitly instead of asserting identical kernels.
   If using Dr's displayed formula literally, `cosh(πt)≥1` and positivity give the required
   lower bound directly, for real and exceptional r; no upper bound for this factor is needed.
   Alternatively state and source a corrected pre-Kuznetsov normalization explicitly.
   Do not divide out this factor while continuing to claim the unchanged Gaussian Φ identity.
   This discrepancy does not force a K-dependent constant in the inequalities actually needed.

## Checks that survived the attack

### Step 4: the growing-order estimate is valid

Put `d=a−u` and `β=b/(2√N|d|)`. The normalized derivative is
`h(x)=sgn(d)+βx^(−1/2)`, with `|β|≤2(√2−1)` and `x∈[3/4,9/4]`.
The claimed ratio is 0.9565852469524, strictly below 31/32; the real gap is 0.0434147530476.
On a complex disc of radius 2⁻¹² the perturbation is at most
`(√2−1)(3/4−2⁻¹²)^(−3/2)2⁻¹² < 0.000156`.
Thus the complex gap exceeds 0.04325, comfortably above 1/64. Cauchy gives
`|g^(j)|≤64·4096^j j!≤2^{20(j+1)}j!` for `g=1/h`.

After p adjoint integrations by parts there are p factors of g, one derivative of η of some
order, and total derivative order p. Counting uncollected Leibniz terms gives at most `(p+1)!`.
The g constants contribute at most `2^{40p}`; the remaining factorial product is at most
`(p!)²`, including the Gevrey factorial of η. The support length, cutoff constants, term
count, and `(2π)^(−p)` are all dominated by `R_p=2^{100(p+1)}(p!)⁴`.
Hence the displayed `R_p N(N|d|)^(−p)` is justified, without an extra N, c, or p-dependent factor.

Since a has denominator c, `Σ_{u≠a}|a−u|^(−p)≤2ζ(p)c^p≤4c^p`.
The final inequality is exactly `c^(p+1)≤N^(p−1)`, which follows from
`c≤N^(1−s)` and `sp≥2−s`; `p=⌊2/s⌋` does satisfy this. No frequency near resonance is omitted.

### Step 5: resonance and Proposition 3

At resonance the inverse residues coincide, so the remaining sum is an ordinary Ramanujan sum.
The h=0 contribution is at most `2cN‖b‖⁴`. For h≠0, integration by parts costs a fixed cutoff
constant and gives `min(N,cN/(θ|h|))`; summing shifts uses
`Σ_m|b_m b_{m−h}|≤‖b‖²` and `Σ_{h≤N}(h,c)/h≤τ(c)(1+log N)`.
The nonresonant contribution is at most `8R_p cN‖b‖⁴`, not c²N:
`c²` residue pairs multiply the `4R_p/c` frequency bound and `2N‖b‖²` coefficient bound.
The stated `2^{100}` envelope covers these terms. Absorption gives N^(1/2+s) after square roots.
For `N^(1−s)<c<N`, Step 3 is O(A N), whereas `√c N^(1/2+s)≥N^(1+s/2)`;
θ<2 supplies the harmless remaining factor. The final P(s) is more than sufficient.

### Steps 6–9: scalar analytic estimates

Apart from the sign above, the holomorphic ξ-weight bounds, angular split, and choices of Δ work.
The c<N range needs exponent 1+3s, not DI's printed 1+2s; the three ranges do give the common
`c^(−s)N^(1+5s)` bound. Keeping the exact diagonal bounded by 2K² is the correct repair.

For the Gaussian lower bound, the restricted intervals really have Gaussian ≥e⁻⁴.
For example elementary exponential bounds on those intervals already give constants larger than
2⁻²⁰; a separate numerical grid check also found substantial margin. Before Selberg, imaginary
parameters with |Im r|<1/2 contribute nonnegatively; afterwards σ≤1/4 gives a uniform positive
lower bound on [1,2], since the denominator is `cosh²(πt)−sin²(πσ)` and cos(πσ)≥1/√2.
The two Φ representations reproduce DI (5.6)–(5.7), and the four modulus ranges sum as claimed.
In the large-c range one must use its stated smaller multiplier before absorbing τ(c)²; this
avoids charging an extra D(s). The twisted text explicitly makes the analogous provision.

Enlarging the nondecreasing W, rather than W/K, is legitimate. More precisely,
`sup_{X≥1} X exp(−X^(2s)/2)=(1/(es))^(1/(2s))≤G(s)`.
Together with `L³≤4(K³+X^(3s))`, this removes the exponential error with the stated slack.
Partial summation costs only `1+log K`; for K>N, `X≤N` and `3s<1` justify the displayed K²
absorption. For the twist use `√r/L≤1`. No r-dependent enlargement is necessary.
The Selberg limiting argument fixes n,q,σ before taking Y→∞; those constants determine only
an exponent and do not enter K_T2. Alternatively the explicitly permitted Selberg black box
avoids this limiting argument entirely. The endpoint N<1 reduction costs less than 3.

### Constants and character dependence

The only growing-order analytic operation is the audited integration by parts. Substitution into
the explicit K_T2 formula gives the claimed upper bound for log K_T2, hence exp(exp(96/δ)),
a fortiori exp(exp(100/δ)). As a sanity check, δ log log K_T2 is about 44.8355 at δ=0.1 and
44.3667 at δ=0.001; the dominant asymptotic coefficient is 64 log 2, not 100.
No untracked δ,q,N,K dependence was found in the scalar bounds.

Dr Lemma 4.2 supports exactly the stated (W), with absolute but unspecified C_W,B_W.
At resonance `conj(χ(δ₁))χ(δ₂)=1` because inversion is injective on units and r|c.
The conjugation/transposition identities for even χ are correct. Steps 2–5 need no √r;
only the Weil range introduces it. Moduli are L-multiples, producing √r/L, and the diagonal
retains a conductor-free K². The Γ₁(L) restriction used for Selberg introduces no norm/index
factor into an eigenvalue bound. The D_b and B envelopes safely cover the stated dependence.
There is still no numerical value for the twisted final A without numerical C_W,B_W; that is
an acknowledged black-box qualification, not a newly discovered hidden conductor constant.

Validation: memory-limited, standard-library `uv run python` checks of separation, complex-disc
margin, Gaussian lower bounds, kernel sign, and log-log envelopes; no reviewed file modified.
