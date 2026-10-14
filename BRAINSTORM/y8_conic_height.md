# y8_conic_height — where the χ = +1 words sit on the conic: small-height points, and the boundary slice = principal genus (O217)

## Idea (goal c)
For χ = +1, Thm A gives x, y ∈ ℤ³ with x·y = 1 and z = x × y, |z|² = tp; the conic point is ℓ(w) = z mod p
(z is isotropic mod p and is the radical of span(x, y) mod p). Define the **height** h(ℓ) = min L_ℓ =
min{|y|²/p : y ≡ λℓ (mod p), y ≢ 0}. Then (PROVED) h(ℓ(w)) ≤ min(t, u, v) (L_w ≅ L_ℓ contains vectors of norm
t, u, v), so every χ = +1 word sits on a point of height ≤ p^{1/3} (min(t,u,v)³ ≤ tuv ≈ p + u + v).
**Boundary slice (PROVED).** Height-1 points ↔ representations p = |y|² (r₃(p)/48 orbits); words with u = 1 (or t = 1)
live there: G_w with u = 1 reduces to ⟨1⟩ ⊥ [[v, −1], [−1, t − 1]], (t − 1)v = p + 1, so these words are the forms
(v, 2, t − 1) of discriminant −4p = ideals (v, 1 + √−p) dividing (1 + √−p), and χ = +1 ⟺ principal genus (which for
p ≡ 1 (4) is Gauss's three-squares genus: x² + py² ⊂ ℤ³ via (1,0,0), (0, a, b), a² + b² = p). They occupy at most
τ(p + 1) of the ≈ h(−4p)/2 classes of that genus.

## Literature
Gauss Disq. art. 291–292; Duke (1988) and Golubeva–Fomenko / Ellenberg–Michel–Venkatesh (equidistribution of
lattice points on spheres and of their orthogonal lattices); Lubotzky–Phillips–Sarnak (Hurwitz quaternions; the
conic P¹(𝔽_p) as boundary of the (p+1)-tree); TWO_FIBRES Prop A2.

## Barrier screen
B6: equidistribution of {z : |z|² = tp} as t → ∞ (Duke/EMV) is an average over the level t, and the words are a
divisor-in-class-selected subset (B2). B3: the number of path bases per class is ≍ log³p/(p/24) on average —
almost all conic points carry none; there is no main term at a single point. T1: at p = m² the conic is replaced by
the "off-conic" functional f of Thm B; height reading persists (f·f ≢ 0).

## Cheap numerics (`scripts/y8_conic_words.py`)
p = 1009, χ = +1 words with u ≤ v, t ≤ 400: 15 words on 9 of the ≈ 42 conic orbits; all u = 1 or t = 1 words on
height-1 orbits; h(ℓ(w)) = min(t, u, v) in all 15 cases (e.g. (5,6,35) → height 5, (6,6,29) → 6, (169,2,3) → 2);
the four height-1 orbits used carry 2–3 words each (word pairs related by boundary moves).

## Assessment
PROVED (dictionary, height bound) + EVIDENCE (one prime). Answers (c): path bases sit on small-height conic points,
height = min letter (observed); "which points" is again "which ideals (A, 1 + √−tp) have norm ≡ −1 (t)" (B2).
No equidistribution statement applies at fixed p.
