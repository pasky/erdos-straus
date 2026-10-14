# s3_box_bit — (J)28 ES^□ × (J)25 box criterion × (J)38 Prop 4.1 slicing: a □-shot carries exactly one bit

**Combines:** (J)28 (ES^□ shot g | p + 4Q², g ≡ 3 mod 4), (J)25 Thm 3.1 (ES at modulus h ⟺ −p ∈ Box((h+1)/4) mod h,
Box(k) = {4c²d : cd | k}), (J)38 Prop 4.1(b) (Type II = d-sliced B = 1 points of V_{pd}), (J)34 (overflow).
Brief item: "across n (n ↔ nd slicing)".

## Idea
Transport a □-shot (g, Q) with overflow Q₁ > 1 into an ES certificate by changing n (slicing n ↔ nd, or n ↔ nQ₁²)
or by re-reading the same modulus g.

## Results (PROVED, elementary)
1. *Slicing re-parametrises the box at fixed g.* An ES point of V_{pd} at modulus g is a cube point (c, d, j) of p
   with 4cdj = g + 1 (Prop 4.1(b)); so "some slice d at modulus g" ⟺ −p ∈ Box((g+1)/4) mod g, independent of Q.
   Multiplying n by Q₁² turns (g, Q₀Q₁) into the shot (g, Q₀Q₁²) of pQ₁² (as pQ₁² + 4Q₀²Q₁⁴ = Q₁²(p + 4Q²)): the
   overflow grows. Neither move uses the □ data beyond g.
2. *The one bit.* For a prime g ≡ 3 (mod 4), g ∤ p: [a □-shot at g exists] ⟺ (p/g) = −1. And [ES certificate at
   modulus g] ⇒ (p/g) = −1: if −p ≡ 4c²d with cd | (g+1)/4 then g ≡ −1 (mod 4d), so (d/g) = 1 by the (∗)-computation
   of SYNTHESIS_SPARKS3 Thm 1.1, whence (−p/g) = 1. So **the □ relaxation at a prime modulus is exactly the sign layer
   of the Type II certificate at that modulus**; ES additionally needs the class (box) layer.

## Literature
Internal: SYNTHESIS_SPARKS (O171) "sign layer / class layer" skeleton; FIXED_MODULUS_SHOTS Thm 3.1.

## Barrier screen
B2 exactly: the box is the class layer; the bit is the genus/sign layer (Prop 10.3 of (J)5).

## Cheap numerics (`scripts/s3_bit_vs_box.py 20000 2000`, 2 s)
Pairs (p, g), p ≡ 1 (4) prime < 20000, g ≡ 3 (4) prime < 2000: box hits 8423/88436 = 9.5% when (p/g) = −1, and
**0/85939** when (p/g) = +1 (as proved). Identity check for s3_eps_mu_sieve: 0 mismatches.

## Assessment
PROVED dictionary, negative for transport: the relaxed certificate contributes the necessary sign bit and nothing
toward the box condition; slicing across n is a relabelling of the same box. Promise 0.
