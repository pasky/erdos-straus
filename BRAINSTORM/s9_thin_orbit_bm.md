# s9_thin_orbit_bm — thin-orbit growth (Zaremba 2026) at the BM level (O271, mandatory (v) example)

## Idea
(J)94/(J)95: Zaremba is claimed pointwise by growth in SL₂(ℤ/q) (Shkredov arXiv:2603.14116; X. Zhang arXiv:2605.02518), but the
method needs density (|A|N^κ ≫ q), and ES-five has only ≍ log²p certificates; (J)99: T1 is Rickards–Stange's reciprocity
obstruction (theta multiplier) on the ES slices. Cross-combine with O268/§2: run the growth argument only at the BM level
(the reciprocity layer), where the target is a coset of index 2 instead of a single class.

## Literature
As above; Rickards–Stange (Duke 2025) reciprocity obstructions; ZAREMBA_TRANSFER Theorem A (λ(p) ≪ log p log log p, Chang-type).

## Barrier screen
At the BM level the problem is already solved pointwise by the least non-residue (SYNTHESIS_SPARKS9 Prop 2.2; in CF coordinates:
a quadratic non-residue A with p/A of bounded length, Theorem A's relaxation). So growth adds nothing there; at the class layer
(the single class −1 inside the coset) the target density is 2/φ(t) and the count ≍ log²p — the density hypothesis of the growth
method fails by a power. Hypothesis TG with a Legendre twist ((J)99) is the class-layer statement, open. T1: the reciprocity layer
is exactly where squares die, consistent. B3: power count needed vs polylog available.

## Cheap numerics
None new (see `scripts/s9_level_bm.py`; ZAREMBA_TRANSFER's ZQ tables).

## Assessment
Assessment: the BM/reciprocity layer is free (pointwise, elementary), and the growth method cannot see below it. The thin-orbit
door is closed at the class layer by density, as in (J)95. No route.
