# bsC_typeII_commutative — Type II is a commutative factorisation in ℤ[√−dn] (the Type II twin of QUATERNION_ES Lemma 1.1) (O176)

**ES is not solved here.** Labels as in DISCOVERIES.md. Script `scripts/bsC_typeII_commutative.py`.

## Idea
QUATERNION_ES §3 presents Type II as "genuinely non-commutative": `(2ai + j)(2bi − j) = −e(1 + 2ck)` in (−d, −p). Left-
and right-multiplying by i (i(2ai + j) = −2ad + k, (2bi − j)·i... ) moves it into the commutative subfield ℚ(k), k² = −dp.
Commutative factorisations are where Kudla/Heegner (and Diff-parity) have the cleanest grip, so record the exact form.

## Statement (PROVED, two-line algebra; checked)
**Lemma 1.** Let n ≥ 3 be odd, d ≥ 1, k = √(−dn). Then (a, b, c, d, e) is a Type II tuple of n
(`4abd = n + e, a + b = ce`) iff
`(2ad + k)(2bd + k) = de·(1 + 2ck)` in ℤ[k],
and then `N(2ad + k) = d·e·f`, `N(2bd + k) = d·e·f'`, `N(1 + 2ck) = ff'` (f = 4acd − 1, f' = 4bcd − 1).
*Proof.* LHS = 4abd² + k² + 2(a+b)dk = d(4abd − n) + 2(a+b)dk; compare with de + 2cde·k. Norms: 4a²d² + dn =
d(4a²d + n) and ef = 4a²d + n (ET). ∎ *Check:* all 336357 Type II tuples of all odd n ≤ 2·10⁴, 0 failures.
**Reading.** Type II ⟺ the element `1 + 2ck` (norm 1 + 4c²dn) times de is a product of two elements of the *line*
`{x + k : x ∈ 2dℤ_{>0}}`. Ideal-theoretically: (1 + 2ck) = 𝔣𝔣' with N𝔣 = f, and 𝔣 = (2ad + k)/(𝔡𝔢) — the Heegner
form [f, 4ad, de] of disc −4dn (POINTWISE_TYPEII_SPECTRAL) is the class of 𝔣. Compare Type I (QUATERNION Lemma 1.1):
`(1 + 2a w)(1 + 2b w) = e(2c w − p)` in ℤ[√−d]. **Dilation 1 ↔ k:** Type I lives on the line {1 + xw} in ℤ[√−d], Type II on
the line {x + k} in ℤ[√−dn] — the role of the constant term and the irrational part swap, and n moves into the field.

## Barrier screen
* **B2**: the line condition (k-coefficient exactly 1, constant term ≡ 0 mod 2d) is a representative condition on
  elements of a fixed ideal class; the class of 𝔣 is a genus/Galois object (bsC_valence_borcherds Prop 1).
* **T1**: at n = m², K = ℚ(√−dm²) = ℚ(√−d) and Diff-parity for [f, 2, f'] kills it (KUDLA_ES Thm 1.4; R172-repaired).
  In Lemma 1 itself T1 enters via (−f/m)-type genus characters of 𝔣.
* **B1/B4/B6**: not engaged.
* **Use**: it removes the "non-commutative" label from Type II (QUATERNION §3 headline is presentational, not
  structural) and makes the Type I/II dilation an explicit swap of coordinates on two lines.

## Assessment
**PROVED identity, modest novelty (an equivalent of the Heegner-form picture (I)4); no mechanism.** It is the input for
the level-vs-determinant form of Type II in DIFF_DEEP §2. Promise 1.
