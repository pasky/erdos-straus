# bsA_minkowski_stern — HJ length = Hamming weight of Minkowski's ?(A/n); ES in Stern's diatomic sequence (O174)

## Idea
Use Minkowski's question-mark function ?, which conjugates the Farey map to the doubling map, to carry the Farey ball into
binary arithmetic.

**M1 (PROVED; exhaustive check n < 200).** For 0 < A < n coprime, ?(A/n) = m/2^k is dyadic and
**r(n/A) = popcount(m)**, the number of 1-bits.
*Proof.* For A/n = [0; a₁, a₂, …], ?(A/n) has binary expansion 0.0^{a₁−1}1^{a₂}0^{a₃}1^{a₄}… (Denjoy/Salem). The 1-bits come
from the even-indexed quotients of A/n, which are the odd-indexed quotients of n/A. Terminal block: write A/n = [0; a₁, …, a_k] with a_k ≥ 2. The finite dyadic
?(A/n) = 2Σ_{j≤k}(−1)^{j+1}2^{−(a₁+…+a_j)} has binary expansion with blocks 0^{a₁−1}1^{a₂}0^{a₃}… in which the last block is
shortened by one and followed by a single opposite bit. So popcount = a₂ + a₄ + … + a_k if k is even, and a₂ + … + a_{k−1} + 1 if k is odd.
With n/A = [a₁; a₂, …, a_k] (index shift by one), this is exactly the HJ-length formula of bsA_farey_lnr_pigeonhole, Lemma 2's proof
(1 + Σ_odd for even length, Σ_odd for odd length, in n/A's indexing). Checked exactly for all 12 150
coprime pairs with n < 200, and in `scripts/bsA_minkowski.py`. ∎
**M2 (classical; checked).** If ?(A/n) = m/2^k then (A, n) = (s(m), s(2^k + m)), where s is Stern's diatomic sequence
(s(2N) = s(N), s(2N+1) = s(N) + s(N+1)). This is the Stern–Brocot/Calkin–Wilf enumeration.
**M3 (ES in Stern language; PROVED from M1, M2, DK Cor 4.6).** For p ≡ 1 (8):
**five-slice ES(p) ⟺ there are k and m < 2^k with popcount(m) ≤ 3, s(2^k + m) = p and (s(m)/p) = −1.**
So ES on the five slices says that the prime p occurs in Stern's diatomic sequence at an index N = 2^k + m with at most four
1-bits, with a non-residue "left partner" s(m). The Farey ball of radius R is ?⁻¹ of the dyadics of Hamming weight ≤ R.
For weight 3, s(2^k + 2^a + 2^b + 2^c) is the continuant tuv − u − v in the gaps.

## Literature
Salem, *On some singular monotonic functions…* (TAMS 1943); Denjoy (1938) (from memory). Northshield, *Stern's diatomic
sequence* (Amer. Math. Monthly 117 (2010) 581; from memory). Calkin–Wilf, *Recounting the rationals* (Monthly 2000). Values of
s at indices of low Hamming weight are polynomials in the gaps (folklore; Stern polynomials, Klavžar–Milutinović–Petr 2007,
from memory).

## Barrier screen
* **Burgess in the Farey metric.** The natural analytic question is a character sum of χ_p over ?⁻¹(weight ≤ R dyadics) ∩ (1/p)ℤ.
  For R ≍ ln² p the set has density ≥ 1/2 (PROVED, bsA_farey_lnr_pigeonhole Thm 3). The same holds for R ≍ ln p ln ln p
  *conditionally* on the unverified fixed-denominator law of large numbers. For R ≍ C ln p the size p^{1−ε(C)} is a heuristic guess only, with
  with a bilinear continuant structure K(b₁…b_r) = K(b₁…b_j)K(b_{j+1}…b_r) − K(b₁…b_{j−1})K(b_{j+2}…b_r). Bourgain–Kontorovich-type
  bilinear methods might give λ(p) ≪ ln p (Assessment, not attempted). For R = 3 the set has polylog size. Any polylog set
  can lie in QR_p, so cardinality-only arguments cannot work (B3/B6). A character-sum argument would have to exploit the
  specific structure of the ball, and I know none that does.
* Moshchevitin–Shkredov (Pacific J. 309 (2020), arXiv:1911.07487, abstract verified) control bounded partial quotients only
  for a *multiple* of p, and Chang treats averages over subgroups. Neither gives a QNR with a short ? expansion at a fixed p.
* B1/B2: the conditions s(2^k+m) = p with popcount(m) = 3 are exactly the (★) divisor events (each choice of two
  gaps leaves a divisibility condition for the third).
* T1: M3 at n = m² needs a Jacobi −1 left partner, which does not exist.

## Cheap numerics
`scripts/bsA_minkowski.py 150 3000`: identities M1–M2 (6 816 pairs, 0 failures). M3 holds for all 101 primes p ≡ 1 (8),
17 ≤ p < 3000.

## Assessment
A clean, possibly new packaging: **HJ length = popcount ∘ ?**, so ES five-slices = "Stern's diatomic sequence hits p at
weight ≤ 4 with a QNR partner". It opens the binary/automatic-sequence toolbox (Stern's sequence is 2-regular), but a
2-regular-sequence statement about *which primes occur at low-weight indices* is again the divisor event. Promise 1/5.
SHARP as a dictionary (M1).
