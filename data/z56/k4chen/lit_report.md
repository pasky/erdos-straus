# Literature report: two-square shift plus almost-prime shift

Scope: source-checked literature as of the cited versions. “Verified” means I inspected the cited paper’s theorem/abstract text; “unverified” flags leads where I did not verify a primary-source theorem. Notation: `P_r` means at most `r` prime factors with multiplicity (`Ω≤r`).

## 1. Exact two-square condition combined with almost primes

### Nath–Xie (direct match)

**VERIFIED.** Kunjakanan Nath and Likun Xie, “Almost primes and primes that are sums of two squares plus one,” arXiv:2501.16723v2 (27 Feb 2025), [arXiv](https://arxiv.org/abs/2501.16723), [HTML source](https://arxiv.org/html/2501.16723v2). Theorem 1.1 states exactly:

> “We have \(\#\{p\leq x\colon p\text{ prime},\ p=m^{2}+n^{2}+1,\ m,n\in\mathbb N,\ \Omega(p+2)\leq 11\}\gg x/(\log x)^{5/2}.\)”

Thus the exact shift condition is `p−1=m²+n²`, and the other shift is `p+2=P_11`; the theorem counts `≫x/log^(5/2)x` such primes. This is an exceptionally close precedent for the target question. Theorem 1.1 is an implicit-constant lower bound, not an asymptotic.

**Method and distribution (VERIFIED in paper).** Remark 1.2 and §§2–5: a mixed-dimensional vector sieve combines a semi-linear/half-dimensional beta sieve (`κ=1/2`, sifting primes `3 mod 4` to force the two-square criterion) with a linear sieve (`κ=1`) and then Richert-style weighted sieve on `p+2`; the proof invokes Iwaniec switching for the large-prime part. Their sieve remainder uses the ordinary Bombieri–Vinogradov range `q≤x^(1/2−ε)`, not a BFI-level improvement. Specifically Lemma 3.2 gives a weighted remainder estimate for `d₁d₂<x^(1/2−ε)`; Proposition 4.1 and the proof of Theorem 1.1 apply it. This answers the combination question positively, but does not provide beyond-1/2 distribution for the half-dimensional weights.

Remark 1.1 says **conditionally**, assuming an Elliott–Halberstam version to `q≤x^(1−ε)` and adapting the argument, one could get `Ω(p+2)≤3`; this is explicitly conditional, not an unconditional theorem.

### Teräväinen

**VERIFIED, but not the same problem.** Joni Teräväinen, “The Goldbach problem for primes that are sums of two squares plus one,” *Mathematika* 64 (2018), no. 1, 20–70; arXiv:1611.08585 (2016), [arXiv](https://arxiv.org/abs/1611.08585). The paper studies Goldbach representations using primes of the form `m²+n²+1`. It is not a theorem that one such prime `p` has a specified almost-prime shift `p+h`; its title/topic should not be cited as an answer to the present simultaneous-shift question. I did not extract theorem statement/number here; **UNVERIFIED** beyond bibliographic identity and abstract/topic.

### Other suggested Chen / vector-sieve references

- **UNVERIFIED.** “Chen’s theorem with `p−1` sum of two squares” / “primes `p` with `p−1=x²+y²` and `p+2=P_r`”: Nath–Xie is the primary verified result I located, and gives the stronger direct, explicit result `r=11`. I did not verify a distinct earlier result or a better `r` under this exact formulation.
- **UNVERIFIED.** Matomäki, Wu Jie, Cai Yingchun, Lu, and the suggested “`p+2=P₂` and `p=x²+y²+1`” lead: searches did not establish a primary source/theorem with that exact joint conclusion. Do not attribute such a theorem without checking its source. The verified Nath–Xie theorem is `P_11`, not `P_2`.
- General vector sieve framework in Brüdern–Fouvry / Iwaniec is methodologically relevant, but no specific theorem combining these exact shifts was independently verified here.

## 2. Nath–Xie arXiv:2501.16723

**VERIFIED from v2 main theorem and proof.** Full title/authors: “Almost primes and primes that are sums of two squares plus one,” Kunjakanan Nath and Likun Xie, arXiv:2501.16723v2. The exact theorem and `P_11` conclusion are quoted above. Here “sum of two squares” means an actual representation `p−1=m²+n²`; it is not merely a weighted count of numbers satisfying a relaxed sieve condition. The paper describes the bound in its abstract as a lower bound for primes `p≤x` with `p−1` a sum of squares and `p+2` having boundedly many prime factors.

The paper’s introductory note identifies the two components as “a semi-linear sieve and a linear sieve” (Remark 1.2); §5 chooses parameters `θ₂=0.011`, `θ=0.23`, `λ=0.14`, yielding `Ω(p+2)<1/λ+1/θ=11.4907`, hence `Ω≤11`. The base level is BV `1/2`. This is a result on `p−1` and `p+2`, not on `p+4` and `4p+1`.

## 3. Beyond-BV distribution for primes in a fixed residue

### BFI

**VERIFIED.** Bombieri–Friedlander–Iwaniec, “Primes in arithmetic progressions to large moduli,” *Acta Mathematica* 156 (1986), 203–251 (the standard BFI theorem). In Theorem A as quoted in Lichtman’s 2023 paper (and stated there as BFI), for fixed integer `a`, `A,ε>0`, and well-factorable weights `λ_q` of level `Q≤x^(4/7−ε)`:

> `∑_{q≤Q,(q,a)=1} λ_q(π(x;q,a)−π(x)/φ(q)) ≪_{a,A,ε} x/(log x)^A.`

This is **fixed `a`**, with implied constant depending on `a`; it is not uniform for `|a|≤x^ε`. Standard linear-sieve upper weights have the requisite well-factorability variant (the linear sieve weights themselves require care; Iwaniec constructs a well-factorable modification). BFI’s `4/7` is a weighted level, not ordinary unweighted BV for every modulus.

### Maynard

**VERIFIED.** James Maynard, “Primes in arithmetic progressions to large moduli II: Well-Factorable Estimates,” arXiv:2006.07088; *Memoirs AMS* 306 (2025), no. 1543. Theorem 1.1 gives level `3/5−ε` for **triply well-factorable** weights (not merely well-factorable). Theorem 1.2 gives `7/12−ε` for the **well-factorable linear-sieve upper-bound weights**. For fixed nonzero residue `a`, the AP discrepancy is bounded `≪_{a,A,ε}x/log^A x`. Maynard’s earlier “Primes in arithmetic progressions to large moduli I: Fixed residue classes,” arXiv:2006.06572v2, has a different fixed-residue result: its abstract says primes are equidistributed over moduli of size `x^(1/2+δ)` having a “convenient sized” factor, yielding an asymptotic for all but `O(δQ)` moduli in a dyadic range and results up to `x^(11/21)`. Do not conflate this with the weighted `3/5` result of Part II; neither is an unweighted all-moduli level `3/5`.

### Lichtman

**VERIFIED.** Jared Duker Lichtman, “Primes in arithmetic progressions to large moduli, and Goldbach beyond the square-root barrier,” arXiv:2309.08522 (2023). Corollary 1.5 states for fixed nonzero `a`, `A,ε>0`, and triply well-factorable weights of level `x^ϑ`, `ϑ<66/107`,

> `∑_{q≤x^ϑ,(a,q)=1} λ_q(π(x;q,a)−π(x)/φ(q)) ≪_{a,A,ε} x/(log x)^A.`

Crucially, Theorem 1.7 gives the uniform version `sup_{0<|a|<x^ε}` with `ϑ=(5−4θ)/(8−6θ)−ε`, where `θ` is the Selberg-eigenvalue exponent; using Kim–Sarnak `θ≤7/32` gives `66/107` (theorem states the formula). So it is uniform in small varying residues, but **only for triply well-factorable weights**. Its Theorem 1.2 additionally gives `7/12−ε` for the linear-sieve well-factorable upper weights. The paper’s statement is not a result for arbitrary half-dimensional beta-sieve weights.

### What about half-dimensional beta-sieve weights?

**VERIFIED as far as source statements go; no extension located.** Nath–Xie apply the semi-linear sieve at the ordinary BV level. The enhanced theorems above name (i) well-factorable weights or (ii) the linear-sieve upper weights / triply well-factorable weights. I found no source establishing that the standard `κ=1/2` beta-sieve weights for the two-square sieve are well-factorable in the needed sense, nor a corresponding BFI `4/7` or `66/107` estimate for them. This is a literature-search negative, not a claim of impossibility. BFI/Maynard/Lichtman improvements cannot simply be substituted into the half-dimensional component without verifying the exact weight factorability and remainder structure.

## 4. Titchmarsh divisor sums / `r(p+h)` in APs

**VERIFIED source, but no matching theorem found.** Emmanuel Assing, Valentin Blomer, Junxian Li, “Uniform Titchmarsh divisor problems,” arXiv:2005.13915; *Advances in Mathematics* 393 (2021), Paper 108076. The paper’s Theorem 1.1 gives an asymptotic for `∑_{Y<n≤X} Λ(n)τ(σn+f)` uniformly in the shift parameter in its stated range, with error `O_A(X(log X)^(−A))`; it does **not** state a progression-restricted asymptotic `p≡a (mod q)` for `τ(p+h)` at moduli `q≤x^η`. Its Theorem 2.1 gives an averaged AP distribution result for primes, with moduli through `x^(1/2+δ)` for some `δ>0`, subject to the displayed structured restrictions on moduli/residues; that is not the requested Titchmarsh sequence level of distribution.

**UNVERIFIED / no explicit η established.** I did not verify an asymptotic of the form
`∑_{p≤x, p≡a (mod q)} τ(p+h)` or `r(p+h)` uniformly for `q≤x^η` with explicit positive `η`, where `r` is the sum-of-two-squares representation function. Nor did I establish an applicable exponent from Fiorilli, Fouvry (1985), or Drappeau. The AB-Li results should not be represented as such an exponent absent a theorem explicitly covering this sequence and progression restriction.

## 5. Lower-bound constants for Iwaniec’s half-dimensional theorem

**UNVERIFIED.** I did not verify the best explicit numerical lower-bound constant for `#{p≤x: p+a is a sum of two squares}≫x/(log x)^(3/2)`, nor a numerical ratio to the conjectural asymptotic. Iwaniec’s “The half dimensional sieve,” *Acta Arithmetica* 29 (1976), 69–95, is the foundational source; no numeric constant is asserted here without direct inspection of its theorem and normalization. Nath–Xie’s paper gives explicit singular factors for its own *two-condition vector-sieve* lower bound (Proposition 4.1), but it is not the requested best standalone Iwaniec constant.

**BFI improvement? UNVERIFIED/no evidence found.** No source was located applying BFI’s `4/7` distribution to improve the constant in Iwaniec’s standalone half-dimensional theorem. BFI’s standard benefit is for well-factorable linear-sieve weights; the half-dimensional weight issue above remains a prerequisite, so it is not safe to claim such an improvement.

## Practical assessment for the stated target

The closest unconditional template is Nath–Xie: exact half-dimensional condition plus a weighted almost-prime sieve on a second shift, with BV-level remainders and a switching treatment. It proves `Ω(p+2)≤11` for `p−1` a sum of two squares. Adapting to `p+4` plus a condition on `4p+1` is not automatic: the second sequence, local congruences, dimension/weight, and the distribution of the bilinear remainders all need rechecking. Current beyond-`1/2` prime-distribution results are powerful for specified well-factorable weights, but the checked sources do not establish that they apply to the required half-dimensional sieve weights or to the weighted sequence `r(p+4)` in APs.
