# One ordinary remainder selects an arbitrary bounded integer from negative Pell powers

(§0 block: z74 Opus xreview fix)
```
Result: for odd n with an integral witness x²−ny²=−1, j↦U_(1+4j) mod n^s permutes [0,n^s); one Euclidean remainder of
        a Pell coordinate therefore selects any bounded integer (e.g. any ES denominator).
Label: PROVED (elementary). Replay CERTIFIED (scripts/audit_pell_remainder.py; independently recomputed).
Scope: boundary of the menu barriers (a variable-modulus operation escapes them); gives no rule for WHICH residue
       solves ES; not a statement about ES. Same permutation also in PELL_RESIDUE_INTERFACE_AUDIT.md.
Review: cross-model (Claude Opus), data/z74/xreview/REVIEW_PELLNOGO_OPUS.md — ACCEPT-WITH-FIXES (§0, one pointer).
Triage: METHOD-CX
STATUS delta: none
```

**PROVED.** Let `n>1` be odd, `x²−ny²=−1` with `x,y∈ℤ`, and `s≥1`. Write `(x+y√n)^m=X_m+Y_m√n`, `U_m=Y_m/y`. Then `j↦U_{1+4j} mod n^s`, `0≤j<n^s`, is a permutation. The anchor need not be fundamental and no coprimality of `n` with `y` is needed.

**Digit calculation.** Work in the free integral algebra on `z` with `z²=ny²`. The coefficient of `z` in `(x+z)^m` is `U_m` (equivalently `U_0=0,U_1=1,U_{m+2}=2xU_{m+1}+U_m`). Thus we do not divide by `y` in a residue ring. Modulo `n` we have `z²=0`, `x²=−1`, and `U_m≡m x^(m−1)≡m` for `m≡1 mod 4`. Each odd prime `l|n` is `1 mod 4` by `x²≡−1 mod l`; in particular `l≥5`.

Put `δ=(x+z)^4−1`, so `δ²∈n·ℤ[z]` in this algebra. For `h=d n^k>0` and `k≥0`, expansion gives `(1+δ)^h≡1+hδ mod n^(k+1)`. Indeed the term at `i≥2` has `l`-valuation in **both** coefficients at least `k v_l(n)−v_l(i)+⌊i/2⌋v_l(n)`, using `binom(h,i)=(h/i)binom(h−1,i−1)`. This is at least `(k+1)v_l(n)`, since `v_l(i)≤⌊i/2⌋−1` for `l≥5`. This is why blindly discarding all binomial denominators would not be a valid proof. Multiply by `(x+z)^m`, read the `z` coefficient, and use `U_{m+4}−U_m≡4 mod n` to get the precise rule (also at `d=0`):

`U_{1+4(j+d n^k)} ≡ U_{1+4j} + 4 d n^k mod n^(k+1)`.

Starting with `j=0 mod 1`, if `U_{1+4j}≡b mod n^k`, the unique next digit is `d≡4⁻¹((b−U_{1+4j})/n^k) mod n`. The quotient is integral before reduction. Choose `0≤d<n` and update `j←j+d n^k`. This is elementary base-`n` digit lifting, not a field Hensel argument. It proves existence and uniqueness in the stated range, even for mixed prime and repeated factors of `n`. Positive indices suffice; each selected power has norm `−1`. If positive coordinates are desired take `x,y>0`. For other anchor signs the very same finite index list still gives the permutation for the signed ratio `U_m`.

**Single operation and its precise domain.** With nonnegative Euclidean remainder and `y>0`, the slot expression

`(Y_m rem (y n^s)) / y`

is exactly the least residue of `U_m`: `Y_m=yU_m` for **every power**, so the outer division is exact regardless of the selector. An entirely sign-free expression is `((y Y_m) rem (y² n^s))/y²`. Once `s` is fixed these are fixed expressions with one nonrational operation; they need not be told `m` or `j`. An arbitrary unrelated second Pell witness need not satisfy this exact division, e.g. at `n=5` with anchor `(682,305)` and second witness `(2,1)`. For existential choice the powers of the anchor already suffice; the assertion is not that every pair is of that form.

**What escapes.** On the ramified sequence in `PELL_RAMIFIED_MENU_AUDIT.md` even the least positive negative unit dominates every fixed power of `n`; bounded integer outputs of a rational menu collapse to finitely many functions of `n`. The remainder, by contrast, recovers an entire interval of `n^s` different values as the second witness ranges. It is not a rational slot. This gives one freely selectable bounded scalar, or three freely selectable bounded coordinates with **three** independent powers and **three** remainders (the anchor can be shared). The digit proof can generate the selector *given its target* using modular Lucas powering and inversion of 4, without factoring `n`; it is not a method to find the desired ES denominators. Writing the full integer `Y_m` rather than just computing a residue may take enormous space. This is additive digit control, not a claim about generators of `(ℤ/n^s)^×`, which need not even be cyclic.

**Packing and rational decoding are different.** For example choose `H=n^5>2n⁴`; any three ES denominators could be packed into `b=d₁+H d₂+H² d₃<H³` and selected with one remainder at precision `n^15`. They can be recovered with *additional* quotient/remainder operations or as uniquely defined bounded integer witnesses. There is no uniform fixed rational-function decoder for even the low digit of the full base-`H` box: at a large fixed `n` it would equal `b` at `0≤b<H`, forcing the rational function of `b` to be identically `b` by degree, but at `b=H` the required answer is 0. Fixed exceptional denominator zeros do not enable decoding all inputs.

A stronger scope check allows **arbitrary rational postprocessing with the raw Pell witnesses still available**, on the fixed-prime ramified towers of `PELL_RAMIFIED_MENU_AUDIT.md` (z74 Opus xreview fix: previously misattributed to "the rational-menu audit"). Once the single normalized remainder has produced `b∈[0,n^s)`, repeat the signed exponent-block proof of that audit treating `b` as a coefficient input. Its fixed-degree polynomials and their conjugates still have height `n^O(1)` uniformly in `b`. Every bounded integer slot therefore specializes one of finitely many block ratios `A(√n,b)/D(√n,b)` with `D≠0` there. Its value is rational and hence equals the conjugate average of that ratio, a fixed rational function of `(n,b)`; the norm denominator is nonzero at that point. In particular, even with these extra witnesses and a fixed finite menu, **arbitrary independent pairs** cannot be decoded from this single polynomially bounded scalar: any pair of rational functions of one variable over `ℚ(n)` satisfies a nonzero polynomial relation over `ℚ(n)`. Take the product over the finite menu and clear coefficients. Away from finitely many `n` the resulting nonzero polynomial in the two coordinates cannot vanish on a full growing square grid (one-variable root count in each coordinate). This does **not** rule out a rational parametrization selecting some special ES triples, or all triples on a special subfamily; nor is it a lower bound for all uses of one remainder with unrestricted modulus. Existentially encoding data known to exist is not a proof of ES or an efficient factoring procedure.

**Test.** `uv run --offline --no-project python scripts/audit_pell_remainder.py` verifies 20,725 permutation entries, the digit congruences, and signed exact-remainder cases, including `n=65`, `n=125` and `5|y` at `n=5`.
