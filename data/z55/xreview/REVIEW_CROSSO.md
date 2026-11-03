# CROSSO cross-model hostile review

Reviewed `side-agent/z55-crosso` at `34e4d24e`, including `Z55_CROSSO.md`, all three scripts and both saved outputs.
**Verdict: ACCEPT-WITH-FIXES.** Theorem P and the conditional reductions survive; the proposed HW proof has a wrong multiplier.
**ES remains OPEN.** Neither HV nor HW, nor the pointwise target, is established.
All executed shell jobs had `ulimit -v 6000000` (initial status: 4194304), a CPU limit and explicit timeouts.

## Per-claim audit

| Claim | Classification | Independent check / scope |
|---|---|---|
| Lemma 1.1: three equivalent hit conditions and factorisation | CORRECT | Division gives `p+u=2w(4uC−1)`; expansion gives `de=4Cp+1`. Positivity forces `C≥1`; oddness makes `w″` integral and odd. |
| Lemma 1.1: both Jacobi symbols −1 | CORRECT | For `C=2^k c`, reciprocity gives `(c/d)=1`, and `(2/d)=1` when needed; hence `(−C/d)=−1`. The factorisation gives `(−Cp/d)=1`, so `(p/d)=(d/p)=−1`. Same argument for `e`. |
| Corollary 1.2: no odd-square hits | CORRECT | `gcd(m,d)=1` follows from `d` dividing `4Cm²+1`; therefore `(m²/d)=1`, contradicting the preceding sign. No prime assumption enters this contradiction. |
| §2: “exact” divisor fibrations | CORRECT-WITH-FIX | Retain all induced family restrictions, especially integrality of `w=(e+1)/(8C)` in the fixed-C fibre; the displayed divisor class alone is insufficient. See R2. |
| Theorem P: inclusion and first moment | CORRECT | Disjoint prime windows give `u<w<p`, coprimality and injective modulus map. BV applies below `x^(1/2)/log^B x`; Mertens gives `E₁=(μ+o(1))Π` with the stated factor 1/4 in μ. |
| Theorem P: second moment and proportion | CORRECT | The four cases are exhaustive: diagonal `2E₁`; same-w zero; same-u negligible; disjoint factors controlled by BT. Constants re-derived below. |
| Lemma 4.1: primitive-character / dual-sieve reduction | CORRECT | Primes exceed Q; induced characters therefore equal their primitive sources. Conductors dividing 8 give exactly M̃. Duality removes the weight with `φ(f)/f≤1`, not the opposite inequality. |
| Lemma 4.1: exact pair sum and nonnegativity | CORRECT | Character orthogonality gives `4·1[a≡a′ (8)](φ(h)1[a≡a′ (h)]−1)`; coefficient `4/(φ(q)φ(q′))` gives exactly V₈. It is a squared coefficient norm. |
| Lemma 4.2: `M̃≥c₀log²x` | CORRECT | Squarefree AP density and the two weighted union bounds are valid. Directed prime-tail computation below confirms the positive margin and the coefficient 0.002. |
| Theorem A | CORRECT, CONDITIONAL | Chebyshev gives `xV₈/(ε²c₀²log⁴x)`; HV makes this `o(x/log x)`. Dyadic summation yields the stated global exceptional set. Nothing proves HV. |
| §4.3: diagonal `O(log²x)` | CORRECT | Drop the negative diagonal term, separate u,w, and use `Σ_{n≤T}1/φ(n)=O(log T)`. |
| §4.3: Haar variance identity | CORRECT | CRT gives the displayed individual and joint probabilities on units; summing the two mod-8 conditional covariances gives `V₈=Var₁(H)+Var₅(H)`. Independent exact census below. |
| §4.3: large-prime negative-part bound | CORRECT | Squarefreeness gives `Σ_{ℓ∣uw}1/φ(uw)≪log²x/(ℓ−1)`; square and sum. `Σ_{ℓ>z}ℓ⁻²≪1/(z log z)` follows by partial summation from `π(t)≪t/log t`. |
| §4.3: no-cross-sharing estimate / full off-diagonal programme | GAP if promoted to PROVED | Currently under Assessment, correctly not banked. The joint weighted count and summation are not supplied; neither this sketch nor the data establish HV/HW. |
| Lemma 4.3(a): z-local main term | CORRECT | `gcd(q,8P(z))=8m` since uw is odd squarefree. Orthogonality gives a nonnegative term; rough pairs have `m=1` and the asserted weight. |
| Lemma 4.3(b): remainder bounded by W_z | CORRECT | Subtract the smooth common-conductor sum. Its pair bracket is `φ(h)1[h-compatible]−φ(h_s)1[h_s-compatible]`, zero for `h=h_s` and bounded above by its positive term otherwise. Large sieve applies unchanged. |
| Lemma 4.4: rough-family lower bound | CORRECT | Fundamental lemma with `D=t^(1/2)`, `g(ℓ)=1/ℓ` for odd ℓ and AP remainder `O(1)` gives the asymptotic. Squareful loss `O(t/z)` and shared-prime pair weight `O(log²x/z)` are smaller than the respective main terms. |
| Theorem A′ | CORRECT, CONDITIONAL | Threshold `M_z/2` and the preceding lemmas give exception bound `O(xW_z(log z)^4/log⁴x)`; HW suffices. Dyadic conclusion follows; HW is unproved. |
| §4.5: four-cycle congruences | WRONG as printed | `λ₁` is inverted. A fully compatible squarefree counterexample is given in R1; the other three multipliers survive. This occurs only in the proposed proof, not Lemmas 4.3–4.4. |
| §4.5: dyadic lattice count / cofactor scales | CORRECT as tools, not an HW proof | Counting either variable gives `O(VK/m+min(V,K)+1)` for unit λ. For `u≠u′`, `g₂₂∣u−u′` and `g₂₁,g₁₂≤U₁`; thus both w-cofactors exceed `Y/U₁²`. |
| §1 CERTIFIED checks; §4.4 EVIDENCE numbers | AGREE | All saved output reproduced; details below. Finite prime sampling is not a direct asymptotic computation of V₈. |
| §§0,2,5,6: interpretation and verdict | CORRECT-WITH-FIX | Strengthened on average, not a pointwise solution or a killed route. Restrict the identity-construction dismissal and the “HV holds with room” wording (R3). |

## Proof details decisive for banking

1. **Theorem P.** Write `S_u=½log(α₁/α₀)`, `S_w=log(γ/β)`; then `Σ1/φ(q)=S_uS_w/4`, so `μ=S_uS_w/2`.
For equal u, compatibility requires `w′≡w (4u)`; the integer-count bound gives
`O(x log x·x^(−α₀)+x^(2γ)log x+x^(α₁+γ))=o(Π)`, since `2γ<1`.
For distinct u,w, `L=8uwu′w′` and the CRT class is a unit. BT and `log(x/L)≥(1−2θ)log x/2` give
`E₂≤[2μ+32μ²/(1−2θ)+o(1)]Π`. Cauchy–Schwarz gives `μ/(2+32μ/(1−2θ))` among all primes;
doubling for primes 1 mod 4 yields exactly the memo's proportion. Strict `θ<1/2` is essential.
2. **Large sieve.** Apply duality to primitive characters only, then discard nonprime n from the nonnegative square sum.
Use interval length `x/2` (or integer count N with the `N−1+Q²` form) and `Q²≤x/2`.
The extracted conductor-8 part is `8/φ(q)=2/φ(uw)` on the matching class; there is no missing factor of two.
3. **Density bounds.** The squarefree density for the restricted u-set is `κ=0.047164483271…`.
Its bad-weight loss is at most `(5/3)·0.016546991·log(U₁/U₀)+O(1)`; the inner coefficient is `2/π²−3/20`.
Their doubled product exceeds `0.002062124`, leaving the stated 0.002 after endpoint losses.
For the rough variant the sieve error sum is `O(D)=O(√t)=o(t/log z)` uniformly on the required ranges.

## Numerical rechecks

- Recompiled both C engines with `gcc -O2 -Wall -Wextra`; only the variance program's unused `argc` warns.
- Reran `z55_crosso_checks.py`: 60 primes, 29 hits, zero brute mismatches; both symbols −1 for every hit;
  200 squares give zero in both windows; 48/200 nonsquare composites have positive R. Exact agreement.
- Reran the existing `scripts/z53_genusx_bruteR.py` and CROSSO engine at `p=100000049`, window `(4,232,464,53860)`:
  both give R=2; the unique hit is `(u,w,C)=(5,5113,489)`.
- Reran all four §4.4 commands, seed 7, N=10¹⁸, sample sizes 2000/2000/1000/400.
  `diff` against `var_scaling.txt` is empty: prime variance ratios 2.076/1.992/1.996/2.334 and zero rates agree exactly.
- Independent audit script: `scripts/z55_xrev_crosso_check.py` (stdlib only; bounded seven-member Haar family).
  Directed-rounding sieve to 2,000,000 plus the integer tail gives `Σ_{ℓ≥17}ℓ⁻² < 0.016546990740823`.
  Recomputed `μ=0.021307590996`, proportion `0.001180732852`; both admissible example windows pass.
  First window C2/C3 thresholds: `0.28003`, `0.071307275`; second: `0.271354`, `0.0681796875`.
- Exact unit census modulo 120120, toy window `(0,5,5,15)`: `V₈=29543/57600` by direct variance and pair sum.
  At z=7 the smooth-projected residual energy is `1099/2880≤W_z=7/16`; at z=17 it is zero.
  All five tested cutoffs give exact rational agreement, including `M_z=E(R | small-prime residues)`.

## Source verification

Checked actual theorem statements, not search snippets:
- Heath-Brown, [Lectures on sieves](https://arxiv.org/pdf/math/0209360), pp. 18–19: exact Montgomery–Vaughan BT bound and maximal-in-y BV in π/li form. Their hypotheses match §3.
- Tao, [254A Notes 3](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/), Proposition 10 / Remark 12: primitive-character large sieve, weight `q/φ(q)`, and constant-one `N+Q²` form.
- Ford, [Sieve methods notes](https://ford126.web.illinois.edu/sieve2023.pdf), Theorem 3.6, p. 38: fundamental lemma with bounded weights and error `Σ_{d≤D}|r_d|`; applicable to the fixed mod-4/mod-8 unit classes.
The accessible IK PDF was only a contents extract, so its exact theorem/corollary numbering was not independently verified; the formulations above suffice.

## Required fixes, priority order

**R1 — correct the four-cycle before reusing the HW sketch.** Reduction modulo g₂₂ gives
`g₁₂k₁≡g₂₁v`, hence `λ₁=g₂₁/g₁₂ (mod g₂₂)`, not `g₁₂/g₂₁`.
Counterexample: `(u,w)=(33,455)`, `(u′,w′)=(145,399)`, with identical `a=a′=−943`, all family parity/squarefree/coprimality conditions satisfied.
Here `(g₁₁,g₁₂,g₂₁,g₂₂)=(1,3,5,7)` and `(k₁,v,k₂,t)=(11,29,13,19)`.
The printed relation says `4≡2 (mod 7)`; the corrected relation holds. The internal review's “4-cycle ... fixed” claim is therefore inaccurate.
**R2 — make the fibration scope exact.** In the fixed-C fibre retain `u=(d+1)/(4C)`, `w=((4Cp+1)/d+1)/(8C)∈𝔉(p)`.
For example `p=5,C=1,d=7` satisfies the printed divisor class but gives `w=1/2`, not a hit. Retain induced restrictions in the other fibres too.
**R3 — avoid two interpretive overclaims.** Replace §6 “HV holds with room” by “finite prime samples are consistent with Poisson-scale variance; HV remains untested asymptotically”.
The experiments sample primes in fixed non-exponent windows, not Haar units or asymptotic V₈; the 2.334 ratio also warrants sampling uncertainty.
Replace §0 “identity-type constructions ... are excluded by T1” with “identities remaining positive/integral at odd squares are excluded”; §2 itself admits degeneracy at b=0.
Likewise frame “no averaging ... produces an equidistribution statement” as failure to find an applicable argument, not a universal impossibility.

**Bank after these fixes:** Theorem P; Lemmas 1.1/4.1–4.4 and Corollary 1.2; Theorems A/A′ only with HV/HW displayed.
The justified verdict is **strengthened on average / pointwise target not reached**, not dead and not an ES proof.
