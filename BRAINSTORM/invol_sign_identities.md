# Brainstorm O152(c): sign identities (Gauss lemma, Zolotarev, Eisenstein) for ES counts

Status: **ES is not solved here.** One small PROVED proposition (Prop S) and EVIDENCE.

## 1. Idea

Classical sign proofs compute a Legendre symbol as `(−1)^{count}`: Gauss's lemma (count of residues
`ka mod p` above p/2), Zolotarev (`(a/p)` = sign of the permutation `x↦ax` of ℤ/p), Eisenstein's
lattice-point proof of reciprocity (`Σ⌊qk/p⌋`). An ES analogue would be an identity

  `(−1)^{W(n)} = ε·ψ(n)`,  `W(n)=Σ_{sol of 4/n} w(sol)` a weighted count of (Type I/II) solutions, (S)

with ψ an explicitly computable ±1-valued function (a character, a quartic/octic symbol, a class-number
bit, …). If ψ(p)·ε = −1 on the hard primes, (S) gives `W(p)` odd, hence ES(p).

Two remarks fix what (S) can mean:
* *Sign of a permutation = parity of a fixed-point count.* For an involution ι on a set Y,
  `sgn ι = (−1)^{(|Y|−|Fix ι|)/2}`, so sign identities give **mod-4** information about fixed-point counts.
  This matters because all natural ordered ES counts are even (S₃ acts freely on ordered solutions,
  WINDMILL Lemma 4; Jiang's ordered f_I,f_II even; per-slice Type II counts `N⁺` even by complementation,
  WINDMILL Lemma 3). E.g. for p≡1 (4) (coordinates distinct) the transposition `(y z)` acting on ordered solutions has sign `(−1)^{3f(p)}
  = (−1)^{f(p)}`: **the parity of f(p) is the sign of a coordinate swap.** Zolotarev computes the sign of
  a permutation that is an element of a *group acting simply transitively*; no such group structure on the ES
  solution set is known (the only natural symmetries found are S₃ and divisor complementation), so no
  Zolotarev-type evaluation of this sign is available. (Not a proof that none exists.)
* *Eisenstein/hyperbola lattice counts* give exact parity identities only for sums over regions
  (e.g. `Σ_{n≤x}τ(n)=2Σ_{d≤√x}⌊x/d⌋−⌊√x⌋²`): an average over n — barrier B6/T7.

## 2. Literature anchor

Gauss's lemma, Zolotarev (1872), Eisenstein's lattice-point proof: standard (from memory). Quartic and
octic symbols of 2 and their `x²+32y²` / `x²+64y²` criteria: standard (Barrucand–Cohn; from memory,
unverified). Campaign: WINDMILL.md §3.2 tested parities of f, f_I, f_II on 732 primes against 93 invariants
(Legendre symbols ℓ≤43, quartic symbols of 2,3,5,7, octic of 2, bits of h(D)) — best agreement 55%.

## 3. Barrier screen, and Proposition S

**Proposition S (PROVED, elementary).** Let `W(n)` be any weighted count of Type I and Type II solutions
of 4/n in Elsholtz–Tao's sense (n divides one, resp. two, denominators and is coprime to the rest;
weights in ℤ). Suppose (S) holds for all n in a set containing the odd squares `m²` with
`gcd(m,M)=1`, where ψ is ±1-valued with `ψ(m²)=1` (e.g. ψ completely multiplicative, or any real
Dirichlet character mod M). Then:
1. `ε=+1`, so (S) says: `W(n)` is odd ⟺ `ψ(n)=−1`.
2. If ψ is a real Dirichlet character mod M (or any product of such), `W(p)` is **even** for every prime p
   in a square class mod M. Hence (S) cannot prove ES for those classes — and the hard core of ES is
   exactly p ≡ 1 (24) in square classes mod 840.
3. (S) proves ES(p) for the primes p in a set H iff ψ(p)=−1 on H. If H contains a prime in a square
   class mod M, ψ is not a real character mod M (by (2)). Examples of admissible ψ: Liouville-type
   completely multiplicative functions `(−1)^{Ω_H(n)}`, or characters when H avoids square classes
   (e.g. χ₄ on p≡3 (4) — the easy classes).

*Proof.* `f_I(m²)=f_II(m²)=0` for odd m (ET Prop 1.6), so `W(m²)=0` and `1=ε ψ(m²)=ε`. (2): `ψ(p)=ψ(m²)=1`
when `p≡m² (mod M)`. (3): immediate from (1) and (2). ∎

So character-valued sign identities fail exactly at T1 (the step that fails at m² is "ψ(n)ε=−1", which
for a character is a *local* condition shared by p and m²) — they are congruence data, i.e. B1. For the hard
core (square classes) a T1-compatible sign identity needs a non-character ψ with ψ(p)=−1 there — e.g. a
Liouville-type right side, which uses the global factorisation of n (the same escape as the windmill route,
memo `invol_windmill_signature.md` §1.2), or a non-abelian Frobenius symbol extended multiplicatively.

Screen: B1 — characters: collapses (Prop S(2)); Liouville-type: escapes. B2 — (S) would sum all slices,
no finite slice set. B3/B6 — no main term, pointwise; Eisenstein-type region counts collapse to B6. B5 —
Prop S.

## 4. Experiment

Liouville-type right sides whose prime signs depend only on p mod M are in the F₂-span of the completely
additive functions `Ω_r(n) mod 2` (number of prime factors ≡ r (mod M), with multiplicity). This covers
only those ψ (M = 24, 120), not arbitrary completely multiplicative ±1 functions (e.g. quartic symbols
extended multiplicatively are not tested here; on primes they were tested in WINDMILL §3.2). I added these
(and `ω_r`) to the
all-n signature test (`scripts/bs_invol_signature2.py … forms additive`, rows: all 3333 n ≤ 2·10⁴,
n≡1 (4), gcd(n,6)=1; 385 weight columns incl. ET Type I/II × features, rank 200). Right-side rank (divisor + forms + Ω_r/ω_r): M=24: 1053; M=120: 1795.
**Result: dim(W ∩ RHS) = 1 in both cases, spanned by the `TI&x=y` count (x=y and n dividing exactly one
denominator; 0 on all hard primes).** No tested ES weight satisfies a parity law of the tested
Liouville/character/divisor/binary-form types on all n ≤ 2·10⁴ (EVIDENCE).

## 5. Viability

**COLLAPSES.** Character-valued sign identities collapse to B1/T1 by Prop S (they force W(p) even on all
square classes). Liouville-type identities survive the screens in principle but none exists among the
tested weights and tested right sides (EVIDENCE), and no structural source for one is known: the sign of
`f(p)` is the sign of a coordinate swap on a set with no known group structure, so no Zolotarev-type
evaluation is available.
By-product: Prop S (PROVED, elementary) — a clean T1 statement for sign/parity identities.
