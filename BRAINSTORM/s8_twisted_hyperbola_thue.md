# s8_twisted_hyperbola_thue — Thue/Minkowski on Xε ≡ u (mod p): height is free, class is tied (O258; §1.5)

**Idea.** ES-II ⟺ ∃ u and a point of H_u = {Xε ≡ u (mod p)} of height c = (Xε − u)/p with X ≡ −1 (mod 4cu) (Prop 1.5). Is there
a Thue-lemma or Minkowski argument (as for p = a² + b²) that produces such a point?
**Literature.** Thue's lemma; Minkowski's convex body theorem; Shparlinski's survey on modular hyperbolas (small solutions of
xy ≡ a need |x|, |y| ≤ p^{3/4} unconditionally).
**Barrier screen.** Thue/Minkowski need a lattice (a linear congruence). H_u is a hyperbola. At a fixed height its points are the
factorisations of the one integer cp + u. The class modulus 4cu depends on the height, while pigeonhole controls only an upper
bound on the height. The hypothesis violated is "target fixed in advance" (B2, (J)87 Remark 3.1).
**Cheap numerics.** Equivalence checked through `s8_mp_check.py` (same algebra).
**Assessment.** PROVED equivalence + Assessment (no route).
