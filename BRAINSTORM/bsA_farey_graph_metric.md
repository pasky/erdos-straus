# bsA_farey_graph_metric — the honest Farey-graph metric (signed CF) vs the HJ length (O174)

## Idea
DK Cor 4.6 calls λ(p) a "least non-residue in the Farey metric", but the HJ length r(p/A) is not the Farey-graph
distance. The graph distance d_F(∞, p/A) is the length of the shortest integer continued fraction with entries of
**any sign** (Beardon–Hockman–Short, *Geodesic continued fractions*, Michigan Math. J. 61 (2012) 133; abstract
verified). Signed words K(b₁,b₂,b₃) = p with b_i ∈ ℤ∖0 are "signed ES" data, and signed ES is trivial
(4/p = 1/((p−1)/4) − 1/(p(p−1)/4) for p ≡ 1 (4)). So I expected the signed metric to make the QNR question easy, which
would isolate positivity (b_i ≥ 2) as the true content.
Define λ_F(p) = min{d_F(∞, p/A) : (A/p) = −1}. Trivially λ_F ≤ λ, since the HJ expansion is a Farey path.

## Literature
Beardon–Hockman–Short 2012. Short–Walker, *Geodesic Rosen continued fractions* (2016; from memory). Geodesics between two
vertices of the Farey graph stay in the *ladder*, the triangles crossed by the hyperbolic geodesic (classical; used in
the script).

## Barrier screen / what happened
* Distance 2: p/A is a Farey neighbour of an integer k ⟺ A | p ± 1. Divisors of p − 1 are QRs for p ≡ 1 (8), since
  (q/p) = (p/q) = 1. So only p + 1 contributes, exactly as for HJ length 2 (DK 4.2).
* Distance 3, signed: for each t the signed factorisations of tp + 1 into factors ≡ −1 (t) add new words. For example
  u = −1 needs t + 1 | p − 1, and then A = −(t+1) is again a divisor of p − 1, hence a QR.
* **EVIDENCE (`scripts/bsA_fareydist.py 6000`):** for all 186 primes p ≡ 1 (8), 17 ≤ p < 6000, λ_F(p) = λ(p) exactly
  (132 with value 2, 54 with value 3). **Signed words never reach a non-residue earlier than positive HJ words.** My
  expectation was wrong: the sign freedom of the Farey metric produces only QRs or Klein-equivalent copies of positive
  words.
* So, empirically, the QNR question is the same in the signed and positive metrics, even though *signed ES is trivial*.
  Reading (Assessment): the trivial signed ES solutions are 2-term identities, and they sit at the QR words (divisors of
  p − 1). The ES difficulty is therefore not positivity of the CF entries. It is the requirement of a QNR at distance 3,
  which both metrics share. (I did not prove λ_F = λ in general. A proof would go through the BHS normal form of
  geodesic CFs: entries |b_i| ≥ 2, with the sign patterns that produce p > 0 reducing to HJ words of A or p − A.)
* (R174 repair.) The distance-2 bullet already *proves* λ_F(p) = 2 ⟺ λ(p) = 2 (d_F = 1 only at A = 1, a QR; distance 2 ⟺
  A | p ± 1; divisors of p − 1 are QRs). With λ_F ≤ λ this gives **λ_F(p) = λ(p) whenever λ(p) ≤ 3 (PROVED)**, i.e. at every
  p ≡ 1 (8) where five-slice ES holds (all p < 10⁶ by DK). So the BFS evidence is implied, the conjecture λ_F = λ is open
  only when λ ≥ 4, and the reading below should be taken as weak: distance-3 signed words never enter.
* B1–B6 unchanged. T1: at squares both metrics see only Jacobi +1.

## Cheap numerics
`scripts/bsA_fareydist.py` (BFS on the ladder of Stern–Brocot ancestors, which contains every geodesic).

## Assessment
Negative but clarifying. The "Farey metric" of DK is effectively the true Farey-graph metric on the QNR question
(CONJECTURE λ_F = λ, EVIDENCE p < 6000). Sign freedom does not trivialise anything. Promise 0/5. It removes one
tempting escape ("work in the signed metric, where ES is trivial").
