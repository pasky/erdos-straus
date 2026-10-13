# R165 — hostile review of O165 `PARITY_FIXED_P.md` (branch side-agent/parity-fixed-p)

Reviewer: R165. Status: IN PROGRESS. **ES is not solved anywhere; nothing here changes that.**
From-scratch scripts: `scripts/review_pf_*.py` (none of the author's `pf_*` code reused).

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### C1. Lemma 1.1 (row II{a,d} hits ↔ triples (h,k,d) with (4dhk−1) | hn+k) — **SOUND**

Re-derived: with q = 4ad, f = qh−1, g = N/f ≡ −n (mod q) so g = qk−n; fg = n+qa ⇔ qhk − hn − k = a ⇔
a(4dhk−1) = hn+k. h ≥ 1 since f ≥ 1; k ≥ 1 since qk = g+n > 0. Converse: 4adk = n + (k+a)/h > n gives g ≥ 1. Maps are
mutually inverse. Side remark m | hn+k ⇔ m | 4dh²n+1 is correct (4dhk ≡ 1 mod m, gcd(4dh,m)=1).
From scratch (`scripts/review_pf_dict.py`, `logs/review_pf_dict.txt`): with independent a-priori bounds
a,d ≤ n+2, h,k ≤ n+1 for the LHS and a *larger* box a,d ≤ 2n+6 for the RHS (so RHS elements outside the LHS box would
show up as mismatches), the two sets agree exactly for all n ≤ 120.

### C2. Lemma 1.2 (Type I p-free up to one congruence) — **SOUND** (minor presentation defects D1, D2)

Re-derived. gcd(f, cd) = 1: a prime r | gcd(f,cd) divides 4cdk = f+p, so r = p, excluded by p ∤ f. Then f is odd
(f ≡ −p mod 4), so gcd(f, 4c²d) = 1 and f | 4c²d(4dk²+1) ⇒ f | 4dk²+1. Forward direction needs no coprimality.
From scratch: LHS (box dk ≤ 40) and RHS (c ≤ 40+p/4+2, which covers every c = (f+p)/4dk with f ≤ 4dk²+1) agree for
all odd primes p ≤ 60.

### C3. Lemma 1.3 (spin lemma) and its "Consequence" paragraph — **SOUND**

(i) −4a²d ≡ p (mod ℓ), ℓ ∤ 2a ⇒ (−d/ℓ) = (p/ℓ) = (ℓ/p) (p ≡ 1 mod 4); and for odd ℓ ∤ d the Kronecker symbol
(−4d/ℓ) = (−d/ℓ). (ii) −4c²d ≡ p² ≢ 0 (mod ℓ). χ_{−4d} = (−4d/·) is a character mod 4d (−4d ≡ 0 mod 4) with
χ(−1) = −1, so a hit f ≡ −1 (mod 4ad) has χ(f) = −1. Consequence: N = p+4a²d is coprime to 2ad whenever p ∤ ad
(gcd(N,a) = gcd(p,a), gcd(N,d) = gcd(p,d), N odd), so for (d/p) = −1 the QNR prime factor is indeed automatic,
and for (d/p) = +1 the event is "even, nonzero number of QNR prime factors (with multiplicity)". Type I: χ(−p) =
−(−d/p) = −(d/p), test passed iff (d/p) = −1 — correct.
From scratch: 20302 (ℓ, slice) instances over p ≡ 1 (4), p < 400, a < 6, d < 30, both Type II (i) and Type I (ii)
(with c = a): 0 violations.

### C4. §3.3 (★) and §3.4 hyperbola dictionary — **SOUND** (as dictionaries)

(★): (A,B,C) with 4ABC − A − B = p ↦ (j,f) = (A, 4AC−1): B(4AC−1) = p+A, so f | p+j and f ≡ −1 (mod 4j); inverse
B = (p+j)/f. Conversely f ≥ 4j−1 > j forces j = (−p mod f). §3.4: (4AC−1)(4BC−1) = 4C(4ABC−A−B)+1 identity, and the
inverse map from (x,y) is as stated. From scratch, four independent counts — pairs (j,f), b-form, (A,B,C)-triples,
and hyperbola points (x ≡ 3 mod 4, C | (x+1)/4) — agree for every odd prime p < 80.

### C5. Proposition 2.1 (≤ 5/8 + o(1) of II{1,d}, (d/p)=+1 slices are χ_{−4d}-obstructed) — **SOUND-AFTER-REPAIRS** (minor: D3, D4)

Re-derived step by step.
* Reduction: ℓ | N_d odd, ℓ ≠ p ⇒ ℓ ∤ d, so Lemma 1.3(i) applies; obstructed ⇒ no ℓ ∈ 𝒫 divides N_d. ✔
* Σ_{ℓ∈𝒫} 1/ℓ ≥ 1/2 − o(1): Σ_{n≤z, n odd} (n/p) = S(z) − (2/p)S(z/2) = o(z) by Burgess (z/2 ≥ p^{1/4+ε/2}); every odd
  QNR n ≤ z < p has a prime factor in 𝒫; union bound z/4 − o(z) ≤ Σ_{ℓ∈𝒫}(z/(2ℓ) + 1) and π(z) = o(z). ✔ (the text
  compresses the union-bound step and leaves a draft fragment "…— to avoid the prime 2"; D3).
* Greedy 𝒫′ with μ ∈ [1/2 − o(1), 5/6] exists since 1/ℓ ≤ 1/3. Bonferroni 1[X=0] ≤ 1 − X + X(X−1)/2 holds for all
  integers X ≥ 0. ✔
* Counting in progressions: r | N_d ⇔ d ≡ c_r := −p·4̄ (mod r) (r odd, c_r ≢ 0). #{d ≤ p/4 : d ≡ c_r, (d/p)=1} =
  ½(p/(4r) + O(1)) + ½ Σ_t ((c_r + rt)/p), and ((c_r+rt)/p) = (r/p)((t + c_r r̄)/p) is a character sum over an
  *interval* of length L = p/(4r) ≥ p^{1/2−2ε}/4 (r ≤ z² = p^{1/2+2ε}). Burgess is uniform in the shift and gives
  O(L·p^{−δ(ε)}) once L ≥ p^{1/4+ε'}, i.e. for ε < 1/12 (the text's "p^{1/2−3ε} ≥ p^{1/4+ε}" needs ε ≤ 1/16 —
  state it). Relative error p^{−δ} uniform in r ✔. The O(1) rounding terms are not mentioned in the text, but there
  are ≤ π(z)² ≤ p^{1/2+2ε} = o(p) of them, so they are harmless (D3). Pólya–Vinogradov would *not* suffice for the
  pairs — Burgess is genuinely needed there and is correctly invoked.
* Final optimisation: 1 − μ + μ²/2 is decreasing on [0,1], value 5/8 at μ = 1/2. ✔ |𝓑| ~ p/8 by Pólya–Vinogradov. ✔
* Uniformity: the o(1) depends only on ε (fixed) via the Burgess exponent; no parameter-dependent constants. ✔
"PROVED relative to Burgess" is accurate (Burgess is an unconditional theorem, so this is simply PROVED).

From-scratch exhaustive check (`scripts/review_pf_prop21.py`, `logs/review_pf_prop21.txt`; ALL d ≤ p/4, a = 1):
obstructed fraction 0.589 (p = 1002121 ≡ 1 mod 840), 0.567 (p = 10001881 ≡ 1 mod 840), 0.284 (p = 1000037),
0.311 (p = 10000121). Consistent with ≤ 5/8; for p ≡ 1 (mod 840) (2,3,5,7 all QR) the bound is nearly attained at these
sizes, so 5/8 is not a loose bound in practice. Note the author's EVIDENCE line (pass rates 0.39–0.60) samples
**all a** with 4a²d ≤ p (box-weighted), not the a = 1 family of the proposition (D4).

### C6. R(p) recomputation at p ≈ 10⁸ — **SOUND** (matches)

`scripts/review_pf_R.py` (b-form, complete range b ≤ (4p+1)/3, which suffices since j ≤ (p+1)/3; cross-checked against
direct (A,C) enumeration for p = 101, 1009, 10007, 100003): **R(100004521) = 44, R(100000007) = 62**, identical to the
author's log. Dyadic profiles have 0–8 hits per block, as stated (`logs/review_pf_R.txt`).
