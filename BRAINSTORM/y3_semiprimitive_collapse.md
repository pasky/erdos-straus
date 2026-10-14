# y3_semiprimitive_collapse — Type II firing inside F_{h²}: pure Gauss sums and uniform cyclotomy (O211 (a))

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
Type II at prime h: h = 4cdj − 1, h | p + 4c²d. With m = 4cd, h ≡ −1 (mod m): h is semi-primitive mod m, so over
F_{h²} the order-m cyclotomy is *uniform* and all Gauss sums of order dividing m are *pure* (Stickelberger).
Question: is "semi-primitive + −p/4d ≡ c² (mod h)" a statement about pure Gauss/Jacobi sums or cyclotomic numbers
over F_{h²}, i.e. an algebraic but non-homomorphic bridge escaping TORSION_FIRING Thm 3.1?

## Findings
**(1) Stickelberger sign = the Type II parameter j (PROVED, classical).** Berndt–Evans–Williams, *Gauss and Jacobi
Sums* (1998), Thm 11.6.3: if h^t ≡ −1 (mod m), t minimal, q = h^{2tγ}, χ of order m > 2 on F_q, then
g(χ) = (−1)^{γ−1+γ(h^t+1)/m} √q. Here t = γ = 1, q = h², m = 4cd: **g(χ_{4cd}) = (−1)^j h**; for the order-c
character the sign is (−1)^{4dj} = +1. Checked for all m | h + 1, m ≥ 3, h ≤ 83 (scripts/y3_gauss.py, 0 failures).
The parity of j is the only information the pure Gauss sum carries; it does not involve p.

**(2) Scaling collapse (PROVED, elementary; Lemma 1.1/Prop 1.2 of BRIDGE_WORLDS.md).** F_h^* = ⟨g^{h+1}⟩ lies in the
class C_0 of every order m | h + 1. Hence every count "#{x ∈ F_{h²}^n : F(x) = p, x_i ∈ C_{a_i}}" with F weighted-
homogeneous of degree e depends on p only through p·F_h^{*e}, i.e. through characters of F_h^* of order | e (the
(h−1)-world). In particular all cyclotomic numbers with an F_h-shift, (a,b)_p := #{x ∈ C_a : x + p ∈ C_b}, equal
(a,b), independent of p. This is TORSION_FIRING Thm 3.1 in cyclotomic clothing.

**(3) The only bridge is the additive shift, and it transports the integer m (PROVED + EVIDENCE).** In F_{h²},
∏_{ζ ∈ μ_c, ζ ≠ 1}(1 − ζ) = c (derivative of X^c − 1 at 1), so
`Type II fires at (c, d, h) ⟺ −p ≡ ∏_{μ_{4cd}∖1}(1 − ζ) · ∏_{μ_c∖1}(1 − ζ)  (mod h).`
Uniform cyclotomic numbers are of the same nature: numerically m²(a,b)_m ≡ 1, 1 − m, 1 − 3m (mod h) for every
m | h + 1 tested (m ∈ {4, 6, 8, 10, 12, 16, 20, 24}, h ≤ 199; EVIDENCE, consistent with the Baumert–Mills–Ward closed forms
[Baumert, Mills, Ward, *Uniform cyclotomy*, J. Number Theory 14 (1982) 67–82]: m²(a,b) is an integer polynomial in
h, η, m). So the residue content of semi-primitive cyclotomy is "the integer m reduced mod h" — exactly the box
Box(k) = {c/j} (FIXED_MODULUS_SHOTS Thm 3.1), i.e. archimedean size data. For the objects listed (cardinalities, pure Gauss
sums, uniform cyclotomic numbers) the residue information is the box restatement; this is not a claim about all
conceivable algebraic constructions (R-O211 repair).

**(4) Counting identity?** The number of firing (c,d) at (p,h) is #{(c,j) : cj | k, c ≡ −pj (mod h)}. Box(k) has
≤ τ(k)² elements. It *can* be a subgroup for small k (R-O211 repair: h = 7, k = 2 gives Box = {1, 2, 4}, the
subgroup of order 3, whose indicator has a two-term character expansion). No general coset structure is known and
no cyclotomic-number identity counting firing pairs beyond the definition was found. (Assessment, not a theorem.)

## Barrier screen
B2: the firing modulus h is part of the solution; nothing here fixes it. B3/B6: (1)–(3) are per-h identities, any
p-count needs Σ_h (ET). T1: invisible at the level of (1)–(3) (p-independent); the genus layer is the class of
√(pd) in C_{(h+1)/2·odd} (gcd = 2 of Thm 3.1). Thm 9.1 not engaged (no fixed-level identity is produced).

## Cheap numerics
`scripts/y3_gauss.py`: (1),(2),(4) for all m | h + 1, h ∈ {7,…,83}: 0 failures; (3) table for m ∈ {4, 8, 12}.

## Assessment
COLLAPSES to the box (B2) for the objects examined: weighted-homogeneous cyclotomic counts are p-blind beyond
p mod F_h^{*e} (PROVED), and the additive shift ζ ↦ 1 − ζ / pure Gauss sums / uniform cyclotomic numbers carry
the integer m resp. the parity of j (PROVED resp. EVIDENCE). Iteration (violate "single h"): see
y3_lucas_rank (vary h with p through a recurrence) and y3_typeI_galois (in Type I, p acts as Frobenius on μ_m).
