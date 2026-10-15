# z1_isogeny_pointer — walks on the 2-isogeny graph (brief angle 2): no crossing, automatic pointer, path shape is the lottery (O224)

## Idea
Brief angle 2: walks from the spine word (χ = +1) must cross into χ = −1 within O(log p) steps (expander plus the 2-adic sign).
Translate into CONSTRUCTIVE_ES's dictionary: χ = −1 path classes are Eichler orders of level 2 in B_{p,∞}, i.e. edges of the
supersingular 2-isogeny graph G_p; χ = +1 path classes are Eichler orders of level p in B_{2,∞}.

## Literature
CONSTRUCTIVE_ES Thm 2.1, §5.1 (lattice operations preserve χ), Prop 3.1 (the middle letter is a Frobenius distance); Pizer
(1990), Ramanujan property of G_p; Kneser neighbours.

## Results
(a) **No crossing (PROVED; CONSTRUCTIVE_ES 5.1).** The spine word (p + 2, 1, 1) has L ≅ ⟨1, 1, p⟩ ∈ 𝔊⁺_p for
p ≡ 1 (mod 4), the only case of interest (R229 repair, D9: χ = (−1/p), which is −1 for p ≡ 3 mod 4). Every walk built from
Kneser ℓ-neighbours, Hecke correspondences, duals or rescalings preserves the rational similarity class of L ⊗ ℚ, hence C₀ ⊗ ℚ and χ. So no walk of any length
goes from χ = +1 to χ = −1. The two Brandt modules even share no cusp eigensystem (EVIDENCE, CONSTRUCTIVE_ES 5.2). Angle 2
as stated is ill-posed. The χ-change must change the rational similarity class (a different algebra).
(b) **Automatic pointer (PROVED, FOUR_ADIC_INPUT Thm 1.3, Remark (c)).** Once an edge of G_p is path-shaped, a pentagon vector
points at one of its endpoints. So inside G_p the 2-adic sign is no obstacle at all.
(c) **What remains is the path shape (EVIDENCE).** 𝔊⁻_p has ≈ p/16 classes, and deterministic members always exist. For
p ≡ 1 (mod 4) these include the norm-one classes ⟨1⟩ ⊥ M (M of det p with (−a/p) = −1, any genus representative). But a class is
a path class only on a thin set. `scripts/z1_normone.py 5 260` (p ≡ 1 mod 8): of the 1–4 norm-one classes in 𝔊⁻_p, the path
ones found are those coming from factorisations of p + 1 (spine/boundary words, z1_marking_isometry Lemma 1); not proved in general. At p = 73 and 193 none is a path class, while
other path classes exist (min 2, 3). Path classes have minimum ≤ 5 throughout (p ≤ 257).
If a path edge exists, a walk from a deterministic vertex (spine-adjacent or a Pizer/Ibukiyama special order) reaches it in
O(log p) steps by the Ramanujan property. But expansion presupposes the target: it cannot show that a separately defined thin
set is non-empty, and "hitting a path edge" is the divisor event, for which no walk rule is known.

## Barrier screen
B2: the target is a thin, divisor-defined subset of the edges. Expanders mix down to single vertices after O(log p) steps, so there is no density threshold. The real limitations are that
mixing cannot prove a thin target non-empty and that sampling a set of density ≍ log²p / p (on average; B3 scale) is costly.
So mixing does not help here (self-review repair of a false "resolution threshold" claim) (s3_isogeny_mixing,
bsC_isogeny_ramanujan already found the same). T1: at squares there is no B_{p,∞} at all.

## Cheap numerics
`scripts/z1_normone.py 5 260` (uses `ce_classes.classes`).

## Assessment
Negative, precise: (a) crossing is impossible by any lattice/Hecke walk; (b) the 2-adic sign costs nothing inside G_p;
(c) the whole difficulty is the existence of a point of the thin path-shape set, which expansion cannot supply. Promise 0/5.
