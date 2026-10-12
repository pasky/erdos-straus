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
  WINDMILL Lemma 3). E.g. the transposition `(y z)` acting on ordered solutions has sign `(−1)^{3f(p)}
  = (−1)^{f(p)}`: **the parity of f(p) is the sign of a coordinate swap.** Zolotarev computes the sign of
  a permutation that is an element of a *group acting simply transitively*; the ES solution set carries
  no such group structure (the only natural symmetries are S₃ and divisor complementation), so there is
  no Zolotarev-type evaluation of this sign.
* *Eisenstein/hyperbola lattice counts* give exact parity identities only for sums over regions
  (e.g. `Σ_{n≤x}τ(n)=2Σ_{d≤√x}⌊x/d⌋−⌊√x⌋²`): an average over n — barrier B6/T7.

## 2. Literature anchor

Gauss's lemma, Zolotarev (1872), Eisenstein's lattice-point proof: standard (from memory). Quartic and
octic symbols of 2 and their `x²+32y²` / `x²+64y²` criteria: standard (Barrucand–Cohn; from memory,
unverified). Campaign: WINDMILL.md §3.2 tested parities of f, f_I, f_II on 732 primes against 93 invariants
(Legendre symbols ℓ≤43, quartic symbols of 2,3,5,7, octic of 2, bits of h(D)) — best agreement 55%.

## 3. Barrier screen, and Proposition S

**Proposition S (PROVED, elementary).** Let `W(n)` be any weighted count of Type I and Type II solutions
of 4/n (weights in ℤ). Suppose (S) holds for all n in a set containing the odd squares `m²` with
`gcd(m,M)=1`, where ψ is ±1-valued with `ψ(m²)=1` (e.g. ψ completely multiplicative, or any real
Dirichlet character mod M). Then:
1. `ε=+1`, so (S) says: `W(n)` is odd ⟺ `ψ(n)=−1`.
2. If ψ is a real Dirichlet character mod M (or any product of such), `W(p)` is **even** for every prime p
   in a square class mod M. Hence (S) cannot prove ES for those classes — and the hard core of ES is
   exactly p ≡ 1 (24) in square classes mod 840.
3. If ψ is completely multiplicative and (S) proves ES(p) for all p in a set H of primes, then ψ(p)=−1 on
   H: ψ must be **Liouville-type** on H, `ψ(n)=(−1)^{Ω_H(n)}·(…)`, not a character.

*Proof.* `f_I(m²)=f_II(m²)=0` for odd m (ET Prop 1.6), so `W(m²)=0` and `1=ε ψ(m²)=ε`. (2): `ψ(p)=ψ(m²)=1`
when `p≡m² (mod M)`. (3): immediate from (1). ∎

So character-valued sign identities fail exactly at T1 (the step that fails at m² is "ψ(n)ε=−1", which
for a character is a *local* condition shared by p and m²) — they are congruence data, i.e. B1. The only
T1-compatible sign identities have a Liouville-type right side, which uses the global factorisation of n
(the same escape as the windmill route, memo `invol_windmill_signature.md` §1.2).

Screen: B1 — characters: collapses (Prop S(2)); Liouville-type: escapes. B2 — (S) would sum all slices,
no finite slice set. B3/B6 — no main term, pointwise; Eisenstein-type region counts collapse to B6. B5 —
Prop S.

## 4. Experiment

Liouville-type right sides are in the F₂-span of the completely additive functions
`Ω_r(n) mod 2` (number of prime factors ≡ r (mod M), with multiplicity); I added these (and `ω_r`) to the
all-n signature test (`scripts/bs_invol_signature2.py … forms additive`, rows: all 3333 n ≤ 2·10⁴,
n≡1 (4), gcd(n,6)=1; 345 weight columns, rank 174). M=24: combined right-side rank 1131; M=120: 1919.
**Result: dim(W ∩ RHS) = 1 in both cases, spanned by the trivial repeated-denominator count (even on all
hard primes).** No natural ES weight satisfies a Liouville-type, character-type, divisor-type or
binary-form-type parity law on all n ≤ 2·10⁴ (EVIDENCE).

## 5. Viability

**COLLAPSES.** Character-valued sign identities collapse to B1/T1 by Prop S (they force W(p) even on all
square classes). Liouville-type identities survive the screens in principle but none exists among the
tested weights (E2, EVIDENCE), and there is no structural source for one: the sign of `f(p)` is the sign of
a coordinate swap on a set without group structure, so no Zolotarev-type evaluation exists.
By-product: Prop S (PROVED, elementary) — a clean T1 statement for sign/parity identities.
