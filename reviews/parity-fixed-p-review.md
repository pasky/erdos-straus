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
