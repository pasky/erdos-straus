# y1_heegner_level_t — words are x = 4 terms of a Gross–Kohnen–Zagier pairing of two Heegner points on X₀(t) (O209)

## Idea (brief item (d))
O205 spark: certificates are the x = 4 terms of the Gross–Zagier factorisation of J(−4A, −4A*) with AA* = tp + 1, and
"collisions without the level-t condition are plentiful". Make the level-t condition geometric.

**Lemma K1 (PROVED, elementary).** For a word w = (t, u, v) of odd n, the discriminants D = −4A = 4 − 4tu and
D* = −4A* = 4 − 4tv are both ≡ 2² (mod 4t), i.e. both satisfy the **Heegner condition for X₀(t) with the same root
r = 2 (mod 2t)**, with Heegner forms Q_u = [t, 2, u], Q_v = [t, 2, v] (more generally [ta, 2, c], ac = u resp. v), Heegner
points τ_u = (−1 + i√A)/t, τ_v = (−1 + i√A*)/t. For x := r·r = 4 one has (D D* − x²)/(4t) = 4(AA* − 1)/t = **4n**.
Conversely, any t ≥ 1 and two Heegner forms [t, 2, u], [t, 2, v] with (16AA* − 16)/(4t) = 4n give the word (t, u, v).
*Proof.* 4 − 4tu ≡ 4 (mod 4t); the forms have discriminant 4 − 4t·u; AA* = tn + 1. ∎
So X_n = {pairs of level-t Heegner points of root 2 and "Gross–Kohnen–Zagier index" m = 4n at x = 4}, t ≥ 1 varying.
**Reading (Assessment, standard GZ/GKZ local intersection theory).** For n = p, the x = 4 term contributes to the local
height ⟨P_D, P_{D*}⟩_ℓ only at primes ℓ | m = 4p that are non-split in K = ℚ(√−A) (equivalently in ℚ(√−A*), as AA* ≡ 1
mod p): ℓ = p contributes ⟺ (−A/p) = −1 ⟺ **χ(w) = −1**; otherwise the term lives at ℓ = 2. This is O205's
two-fibre split (Diff = {p} vs {2}) seen on the X₀(t) side: **the sign records at which prime two level-t CM points
with root 2 meet when their x = 4 pairing index is 4p.**

## Literature
Gross–Zagier, *On singular moduli*, J. reine angew. Math. 355 (1985); Gross–Kohnen–Zagier, *Heegner points and derivatives
of L-series II*, Math. Ann. 278 (1987) (level-N Heegner divisors, index (DD′ − x²)/4N, x ≡ rr′ mod 2N); Lauter–Viray
(singular moduli with non-fundamental discriminants, 2015) for the general local formula.

## Barrier screen
* **B2:** the level t is the moving modulus; the set of t with two root-2 Heegner discriminants whose product is
  16(tn + 1) is the divisor-in-class family. Without the level condition the "collision" is trivial: for every prime
  p ≡ 1 (24) below 2·10⁵, some t ≤ 11 has a divisor A | tp + 1 with (−A/p) = −1 (`scripts/y1_collisions.py`).
* **Thm 2.2 / B3:** GKZ generating series are modular in m for *fixed* (D, D*, N); here (D, D*, N) vary with the word, and
  m = 4n is fixed — a "diagonal" extraction across infinitely many levels (H-A).
* T1: at n = m², every x = 4 term lives at 2 (Diff = {2}); consistent.

## Cheap numerics
`scripts/y1_collisions.py 200000`: 2 212 primes p ≡ 1 (24), max least-t = 11 without the level condition.

## Assessment
PROVED dictionary (K1) + Assessment reading; it moves the level-t condition into the Heegner condition, which is the
natural geometric home of a moving modulus — but that is B2 restated. Promise 1/5.
