# z55 HCF — independent hostile review

Reviewed `side-agent/z55-hcf` at `a350c6718de85e335e9bbd0b5ec1609d9dfebd65`.
**Verdict: ACCEPT-WITH-FIXES.** The new obstruction theorem and its quantitative corollary survive.
This strengthens the obstruction to fixed finite certificate coverings, not an upper bound for HC.
The pointwise target remains unproved; Erdős–Straus remains OPEN.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Used Z53 L1.1, L1.2, L3.1 | CORRECT | Rechecked the word identities, coordinate bound, and both reciprocity cases; details below. |
| P1.1 | CORRECT | Primality and c<p supply gcd(c,v)=1; complementary divisors exchange −p and −1. |
| P1.2, both lines | CORRECT | Divisors are a or aq, a divides s; complementing aq in sq leaves s/a, with residues −p (U), −1 (T). |
| L2.1 | CORRECT | The Jacobi kernel is exactly the powers of 2 at 7 and 15; the available 2³ supplies every required exponent. |
| §2 consequences/counterexamples | CORRECT | Multiplicativity gives both coverings; all four larger-c counterexamples independently checked. |
| T3.1 | CORRECT | All six steps and the CRT/Dirichlet quantifiers check; no quadratic hypothesis on R is needed. |
| C3.2 | CORRECT | The least-nonresidue estimate and reduction to finite support are valid; ℓ=11,R=2 really forces least nonresidue prime 11. |
| C3.3 | CORRECT | Choose Y at least min S and all prime factors of d; only a finite truncation is needed. |
| P3.4 | CORRECT | Correct unit CRT class, Linnik application, logarithmic estimate, cutoff conversion, and infinitude. |
| §5 lemma/admissibility numbers | CORRECT | Exact rerun agreement; additional independent algebra and odd-c/T-line checks pass. |
| §5 large-CRT “CERTIFIED” samples | CORRECT-WITH-FIX | Counts reproduce, but primality/factor primality above 2⁶⁴ is only probable in these scripts. |
| §5 census to 2·10⁹ | Not fully re-certified here | Inspected code/data; reran to 10⁶, confirming HC=64 at 21841. Full 2·10⁹ output was not rerun. |
| §0/§3 covering verdict | CORRECT | Excludes a scheme with a finite family per least-nonresidue value, already at 11; does not refute HC≤F(ℓ_p) itself. |
| §4 methodological necessity claims | CORRECT-WITH-FIX | Assessment is the right label, but several absolute assertions exceed the fixed-cover theorem. |

## Proof reconstruction

1. L1.1: U is v(tc−1)=p+c; T is (cu−1)(cv−1)=cp+1. The proposed positive
   divisors reconstruct positive integral words. For L1.2 order u≤v; v(tu−2)≤p gives
   v≤p unless tu=2, when v=p+1 or p+2. Also t≤p+2; none of p,p+1,p+2 is admissible.
2. L3.1: writing d=2^a d′ gives (d/p)=(2/p)^a(−c/d′) on either line.
   For c=4k, d≡3 (4), and reciprocity with d≡−1 (k) gives (k/d)=1, hence −1.
   For odd c≡−p (8), reciprocity gives (−c/d′)=(d′/c)=−(2/c)^a;
   (2/p)=(2/c), so again −1. Coprimality follows from c<p and d≡−1 (c).
3. P1.1: cv divides p+c+v implies the two separate divisibilities. Conversely their gcd
   divides gcd(c,p)=1, so their product divides. For vd=p+c, reducing modulo c gives vd≡p;
   invertibility exchanges v≡−p with d≡−1. P1.2 follows by the complementary-divisor split above.
4. L2.1: gcd(c,N)=1 for N=p+c or cp+1. Thus every odd factor is a unit mod c.
   The kernels are {1,2,4} and {1,2,4,8}, with (−1/c)=−1. A nonresidue q can be
   multiplied by 2^a, 0≤a≤3, to reach −1; conversely a divisor of character −1 contains such q.
5. T3.1 Steps 1–2: each outside-S valuation of d is bounded by the pinned precision;
   consequently s divides M and c+1. All its primes are residues modulo p, so L3.1 forces L>1.
   Thus L≥ℓ₀>3R+1. With m=(c+1)/s, d≡−1 implies L≡−m (c).
6. Step 4: an S-valuation beyond J would force c+R or Rc+1 to be a positive multiple
   of ℓ^J>R(C+1), contradicting c≤C. Hence U has c+R=hL, and T has Rc+1=nL.
7. Step 5: U gives hm+R=kc. Multiplying by s yields c(sk−h)=h+sR.
   Put e=sk−h≥1; s≤e+h gives (c−R)e≤(R+1)h. Here c=hL−R>R,
   so c≤R+(R+1)h and L≤R+1+2R/h≤3R+1, a contradiction.
8. Step 6: T gives nm+1=kc, hence c(sk−n)=s+n. With e=sk−n≥1 and s≤e+n,
   obtain c≤2n+1 and L≤2R+(R+1)/n≤3R+1, again impossible.
   CRT is coprime because 1≤R<min S; Dirichlet supplies infinitely many primes beyond C.
9. C3.2: for least nonresidue r and m=ceil(ℓ/r), the nonzero remainder mr−ℓ<r is a residue;
   m is therefore a nonresidue, m≥r, and r(r−1)<ℓ. The stated small cases finish the bound.
   Choose Y to contain every prime of every d in the finite family. Pinning 2,3,5,7 gives 840.
10. C3.3: a certificate class only reads primes dividing d. A sufficiently precise CRT
    neighbourhood of x retains that class and T3.1 excludes its arbitrarily large primes.
    For the second assertion M>C ensures that every prime in the constructed neighbourhood exceeds C.
11. P3.4: with C=floor(Y^A) (C=3 for A=0), M≤210(C+1)^4 and ℓ^J≤2ℓ(C+1).
    Thus log N≤(1.02+1.26A)Y(1+o(1)). Linnik gives log p≤L₀ log N+O(1).
    The extra 1.26 in the stated denominator absorbs the error, so κ′_A log p≤Y and
    κ_A(log p)^A≤C. Excluding Y-smooth certificates is stronger than the required smaller-cutoff exclusion.
    p≡1 (M), p≠1 implies p>M>C; every prime≤Y divides N while p is coprime to N, so p>Y.
    This proves infinitude. At A=0 the displayed κ₀=1/2 is vacuous but valid; the proof's κ₀=3 also works.

## Computations and source checks

All computation runs used `ulimit -v 6000000`, CPU limits, and individual `timeout` bounds.
Extracted the pinned revision into `/tmp/xrev_HCF`; used `uv run --with sympy` (SymPy 1.14.0).
All three original Python outputs are byte-identical to the recorded data:
- L2.1: 8,932 cases; P1.2: 39,695; zero mismatches.
- Single-prime T3.1: 2,071 / 2,399 / 2,291 certificate divisors, zero violations;
  admissibility scan to c=2000 also reproduces every listed count.
- Multi-prime T3.1: 1,168 / 1,653 / 1,170 certificate divisors, zero violations.
- New `scripts/z55_xrev_hcf_check.py`: U/T core algebra checks 2,863,580 / 2,855,400,
  all c=3..5000, R=1..12, all divisors L>3R+1 (including composite L/even exponents): no solutions.
  Odd-c P1.2: 3,375 U and 4,295 T cases below p=10,000, zero mismatches; four §2 counterexamples confirmed.
- C census rerun to 10⁶: 39,175 primes≡1 (4), HC≤64, record 21841, zero small-lemma violations.
  The 49,109,660-prime census and its full tail remain un-reproduced here, not evidence for the proof.

Decisive external citations checked against source statements:
- [Xylouris, BMS 404](https://bib.math.uni-bonn.de/downloads/bms/BMS-404.pdf), §2.3,
  Theorem 2.1: P(q)≪q⁵ with an effective absolute constant. This supports exactly the needed uniform exponent.
- [Rosser–Schoenfeld (1962)](http://denise.vella.chemla.free.fr/Rosser-Schoenfeld-1962.pdf),
  read via Jina: (3.6) π(x)<1.25506x/log x for x>1; Theorem 9/(3.32) θ(x)<1.01624x for x>0.
  Both justify the memo's weakened 1.26 and 1.02 constants.

## Required fixes, in priority order

1. Relabel the large-CRT prime/factorisation experiments **EVIDENCE (probable-prime based)**,
   or supply deterministic primality certificates for the sampled p and all factor leaves.
   `sympy.isprime` explicitly documents BPSW, not a proof, above 2⁶⁴; these samples exceed that range.
   Exact output agreement is not a primality certificate. Small-range lemma and algebra checks are unaffected.
2. Keep §4's necessity claims scoped to the techniques analysed. Replace “p is not a square (⟺ p is prime,
   for the purposes …)” with the precise Jacobi/coprimality hypotheses; nonsquareness is not primality.
   Replace “a pointwise argument would need … not a congruence” by “a fixed finite certificate covering cannot
   suffice; a possible alternative is factorisation information.” Growing-modulus reasoning is not excluded.
   Likewise a large prime factor is a necessary component, not literally “the entire content” of a certificate.

No missing hypothesis invalidates T3.1 or P3.4. No counterexample to their statements was found.
Accept the narrowed covering obstruction after these label/scope fixes; do not record the HC target as proved or dead.
