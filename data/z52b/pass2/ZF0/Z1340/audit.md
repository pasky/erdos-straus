# Z1340 — exact theta-quotient coefficient sign check

ES is OPEN. **PROVED** identities are from METAPLECTIC_ES Theorem K/K1′; numerical ranges are **CERTIFIED (integer sieve)**.

`git grep -il 'theta quotient' -- '*.md'` locates METAPLECTIC_ES.md. Its decisive line is §1 K1′ (lines 77–80):
“q^{t−2}(Q;Q)²θ(X²)/θ(X)² = Σ_{n≥0} (D⁻_t − D⁺_t)(tn+1) qⁿ”.
The following modular-status paragraph explicitly says “the modular identifications below need normalisations that are not carried out here”. Thus this is a Kronecker/Jacobi-function specialisation, not an already-normalised positive Jacobi coefficient formula. The §0 C6 statement only checks t=3,4,6: “D⁻ − D⁺ = −σ_χ(N) ≤ 0 always (theta-series positivity pushes against ES)”. It does not settle signs at arbitrary t; pass1's blanket covered was too broad.

I sieved the exact K1′ coefficients for every t=2,…,64 and n=0,…,100000 (6,300,063 coefficients, arrays of 100001 ints, no dense products). The program counts pairs (d,e) with de=tn+1 and d,e≡±1 (t), so these are the Fourier coefficients themselves, not a proxy.

At t=5 there are 3503 positive, 61151 negative and 35347 zero coefficients, range [−16,8]. The first positive is n=39: N=196, D⁻=3 (4,14,49), D⁺=2 (1,196), hence coefficient +1, whereas n=0 has coefficient −1. In the ES-relevant family 4|t, t=16 already has 1125 positive coefficients (first n=374), 80910 negative and 17966 zero, range [−12,6]. Only t=2,3,4,6,8,12,24 have no positive coefficient in this range. **PROVED** explanation for these exceptions: their unit groups have exponent≤2, so all characters are real and every σχ(N)=∏_{ℓ^v||N}(1+χ(ℓ)+…+χ(ℓ)^v) is nonnegative. K1′ is a negative sum of these for the odd characters; t=2 gives zero.

**Assessment:** no uniform coefficient sign-rigidity exists for the actual quotient. Even the exceptional nonpositive signs oppose, rather than force, positivity of the ES count, which additionally involves the even-character partner and boundary subtraction. QUE of values does not supply a coefficientwise assertion at a prescribed n.

Reproduce: `gcc -O2 -Wall scripts/z52d_p2_ZF0_Z1340_signs.c -o /tmp/z52d_Z1340`; `ulimit -v 8000000; timeout 180s nice -n 10 /tmp/z52d_Z1340 100000`. Full output `signs.csv`. No independent modular normalisation or QUE theorem is asserted.
