# bsN — ES as "−p lies in a divisor box" (O191 memo)

Source: FIXED_MODULUS_SHOTS.md §3–§4 (PROVED there). Box(k) := {c/j : c, j ≥ 1, cj | k} ⊂ (ℤ/h)^*.
* Type II: ES(p) has a solution with divisor h ⟺ h ≡ 3 (4) and −p ∈ Box((h+1)/4) mod h.
* Type I: ⟺ −p ∈ Box((h+p)/4) mod h (h ≡ −p mod 4).
* ES^{(S)} (O186): the box is replaced by the coset ∏q^{κ_q}·⟨S⟩²; for S-smooth (h+1)/4 the ES box is the bounded
  exponent box |e_q| ≤ κ_q (all parities) vs the unbounded parity coset e ≡ κ (2) — as residue sets the box is INSIDE the coset (Box(k) ⊆ 4⟨S⟩², R191 repair of "incomparable"; Cor 3.2), with size τ₃(k) vs |⟨S⟩²|.

Why it matters: an Artin/Gupta–Murty route needs, at a prime r of a fixed Chebotarev set, a certified residue set of
density ≫ 1 with group structure. Boxes have ≤ τ₃ elements (mean 77 for r < 10⁶; occasionally a small subgroup coset, e.g. ⟨2⟩ mod 31); and ES(p)
has certifying moduli only up to O(p²) (finiteness), whereas ES^{(S)} has infinitely many.

Open sparks (not pursued):
1. Covering view: ℤ_{prime} ⊂ ⋃_h (−Box((h+1)/4) mod h) ∪ (Type I). The masses Σ τ₃(k)/h diverge like log³; squares are
   outside all boxes (Jacobi −1, Remark 2.5). A covering theorem with *boxes* (structured, multiplicatively closed up to
   bounds) rather than arbitrary classes might evade the CRT-admissible large-sieve cap ((A)19) — unclear.
2. Type I's box depends on p ((h+p)/4): a self-referential condition; any fixed-point/involution structure?
3. Joint failure of the three modulus-4 shots p+1, p+4, 4p+1: 942 primes < 10⁶; predicted density ≍ (log p)^{−3/2}?
