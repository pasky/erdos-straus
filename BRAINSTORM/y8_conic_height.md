# y8_conic_height — where the χ = +1 words sit on the conic: small-height points, and the boundary slice = principal genus (O217)

> **R224:** "observed h = min letter" is PROVED (THREE_SQUARES Lemma 4.2): h = min Q_w = min(t, u, v).

## Idea (goal c)
For χ = +1, Thm A(iii) gives a *compatible* pair x, y ∈ ℤ³ (x·y = 1, |x|² = A*, |y|² = A, x × y ≡ x + y mod t);
z = x × y has |z|² = tp and is the image of the middle basis vector e₂ under the embedding p·G_w ⊂ ℤ³ (z·x = z·y = 0,
z·γ = p), so the image is pℤ³ + ℤℓ with ℓ(w) = z mod p
(z is isotropic mod p and is the radical of span(x, y) mod p). Define the **height** h(ℓ) = min L_ℓ =
min{|y|²/p : y ≡ λℓ (mod p), y ≢ 0}. Then (PROVED, for compatible embeddings) h(ℓ(w)) ≤ min(t, u, v). R-O217: an arbitrary primitive z with
z^⊥ ≅ T_w is NOT enough — p = 61, w = (63,1,1), x = (−3,2,7), y = (−7,−3,−2) gives z = (17,−55,23) with
z − x − y ≢ 0 (mod 63) and a conic point of height 2 > min letter 1. ℓ(w) also depends on the chosen compatible pair
(the map to conic orbits is only defined up to the non-injectivity of TWO_FIBRES Prop A2) (L_w ≅ L_ℓ contains vectors of norm
t, u, v), so every χ = +1 word sits on a point of height ≤ p^{1/3} (min(t,u,v)³ ≤ tuv ≈ p + u + v).
**Boundary slice (PROVED).** Height-1 points ↔ representations p = |y|² (orbits under the 48 signed permutations; not r₃(p)/48 in general
because of stabilisers, e.g. r₃(5) = 24, one orbit); words with u = 1 (or t = 1)
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
(script repaired to use compatible pairs) p = 1009, χ = +1 words with u ≤ v, t ≤ 400: 15 words on 9 of the ≈ 42
conic orbits; all u = 1 or t = 1 words on height-1 orbits; h(ℓ(w)) = min(t, u, v) in all 15 cases (e.g. (5,6,35) → 5,
(6,6,29) → 6, (169,2,3) → 2); p = 61: 5 words, 3 orbits, h = min letter, incl. (63,1,1) → 1;
the four height-1 orbits used carry 2–3 words each (word pairs related by boundary moves).

## Assessment
PROVED (dictionary, height bound) + EVIDENCE (one prime). Answers (c): path bases sit on small-height conic points,
height = min letter (observed); "which points" is again "which ideals (A, 1 + √−tp) have norm ≡ −1 (t)" (B2).
No equidistribution statement applies at fixed p.
