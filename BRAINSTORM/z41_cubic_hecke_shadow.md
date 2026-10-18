# z41_cubic_hecke_shadow — spark 3: no family of n biases the cubic layer; cubes bias an ES-invisible Hecke character (O272; §6)

**Idea.** O271 spark 3: cubic characters as the remaining algebraic disproof shape — can a structured family (n = r³, …) bias
all cubic characters mod t at the forced primes?
**Literature.** Cubic reciprocity; Hecke characters of ℚ(ω); TWISTED_T1.md (cubic obstructions for twisted targets).
**Result (Cor 6.1, PROVED).** For ANY set of n, conditional on ℓ | tn + 1 the cubic Dirichlet character of ℓ mod the level
prime is equidistributed (Thm 3.1, m = 3). A cube forces the Stickelberger component S = x₁x₂² (a cubic Hecke character of
conductor dividing 9t — ramification above 3 can occur), never the Dirichlet component D = x₁x₂. Squares are the only powers whose forced bias is Dirichlet-visible.
**Barrier screen.** T1 explained (m = 2 is the only coincidence S = D). A disproof family would have to act on the varying
prime factors of tn + 1 jointly — not excluded by this memo.
**Cheap numerics.** `scripts/z41_stickelberger.py` part (b): cubes 27, 125, 343, 729 — ℓ a cube mod q at 491/1492, 257/759,
255/741, 174/508.
**Assessment.** PROVED negative in narrow scope: no family of n biases the cubic Dirichlet layer THROUGH THE FORCING CONGRUENCE
(fixed n, ℓ; varying level prime). Joint restrictions on varying factors of tn + 1 and other algebraic constructions not excluded.
