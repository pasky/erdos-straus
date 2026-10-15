# z16_frobenius — characteristic-3 Frobenius maps covering at x_u to covering at x_{u³} (O241)

## Idea
In characteristic 3, f ↦ f³ is a ring endomorphism. Cubing a valid Case B family (E, L', j, γ, g') gives a valid Case B family
(E³, L'³, 3(N + 1) − k, 3γ, g'³) at x_{u³}, of level 3N + 2 (STERILE_DIOPHANTINE Prop 5.1, PROVED). So covered ⇒ covered
under u ↦ u³; contrapositively a cube point in O gives a point in O. Hoped-for use: a renormalisation for games (z16_game_barrier)
or a self-similarity of U_c.

## Literature
Frobenius/Artin–Schreier self-similarity of power series: Christol's theorem (automatic sequences ⇔ algebraic over F_q(T));
Mahler 1949 (algebraic Liouville numbers in characteristic p). The char-2 Frobenius family (1 + Tg')² = 1 + T²g'² of
FF_STERILE_PUSH §4.

## Barrier screen
u³ ≡ 1 (mod T³): Frobenius leaves the c-slices (lands in the c = 0 slice), and shrinks balls (depth N + 1 ↦ 3N + 3), so it is
a renormalisation in the wrong direction for games. The tuple equations are not Frobenius-stable (w₁ + C₁ = T·g'v₁ needs
v_T = 1, cubing gives 3) — the same valuation bit that separates char 2 (covered) from odd char. Case A not checked.

## Cheap numerics
None (the proposition is an identity check).

## Assessment
PROVED (Case B), modest. Records a structural symmetry of the obstructed set; no route to O ≠ ∅.
