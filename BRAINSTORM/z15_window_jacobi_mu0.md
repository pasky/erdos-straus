# z15_window_jacobi_mu0 — when do constant windows reach a glued rational point? (O240)

## Idea
At μ = 0 of c·2^s + 1 (c + 1 = 4^i) the window parameter X* is a rational number at every odd place (ρ = 2^{−(j+2)/4} or
2^{−j/e}) glued with 0 at 2. All atom residues mod m are then residues of fixed rationals whose odd primes divide
N₀ = 4^i + m, where −m is a square; Jacobi reciprocity gives (d/m) = (2/m)^{v₂(d(ρ))} against the needed (−1/m) = −1 — using d(ρ) > 0, which holds because K has
positive coefficients, so atoms are positive on (0, ∞) (R252 D4 = R251 D8, applied by R252; essential).
## Results (MENU_STERILITY Prop 4.1, 4.3; PROVED)
* windows m ≡ 7 (mod 8) never fire at μ = 0; cyclotomic windows (e | j ⟹ j ≥ 3) are all of this kind;
* j = 2 Sophie-Germain windows m = 4ct⁴ − 1 with d = Π_{q|c} q^{a_q} f₊^x f₋^y (restricted menu — R252 D7, applied by R252): firing ⟺ m(t) | N(t) (explicit, deg ≤ 8); m irreducible ⟹ finitely many t
  (m | N identically is impossible: real root τ of m, N(τ) > 0). So the restricted SG menu at μ = 0 is a FINITE menu: an arithmetic accident. (R252 D7: a constant λ may also carry primes of
  g±(t), since 4K(ρ) = c·g₊g₋; then N is not polynomial in t and finiteness is Assessment; EVIDENCE `review_r252_sg_general.py`:
  no firing for c = 15, 63, 255, t ≤ 301; c = 3 only t = 1.)
## Literature
Jacobi reciprocity; resultant/Bezout bound.
## Barrier screen
This is a B1-type theorem for a richer menu: the window menu at a glued point is finite and Jacobi-constrained.
## Cheap numerics
`z15_proth_mu0.py 3 12 36 81` (0 cyclotomic hits); `z15_mu0_sg.py c 1 T`: c = 3 fires only at t = 1 (t ≤ 41);
none found for c = 15, 63 (t ≤ 301) or c = 255 (t ≤ 15). `z15_sg_mu0_complete.py 3`: 27 vectors.
## Assessment
PROVED (Props 4.1, 4.3) + EVIDENCE (c = 15, 63, 255 negative). Steering: whether μ = 0 of 15·2^s + 1 is sterile for ALL
polynomial-in-X families is open (Theorem A does not decide it).
