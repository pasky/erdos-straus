# y3_ordinary_bridge — ordinary reductions as bridges between the (h+1)- and (h−1)-worlds (O211; R206 D3)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea (orchestrator, from R206 D3)
TORSION_FIRING Thm 3.1 needs supersingular/torus input (exponent | h^s + 1). Points of a curve ORDINARY at h land in
E(F_h) of order N = h + 1 − a_h, and Hom(E(F_h), F_h^*) can be large (y² = x³ + x + 1 at h = 127: N = 126 = h − 1).
So ordinary reductions are a bridge candidate. How large, how often, and what can such a bridge carry?

## Findings
**(1) Hasse ceiling on ordinary bridges (PROVED, elementary).** |Hom(E(F_h), F_h^*)| ≤ gcd(N, h − 1) = gcd(a_h − 2, h − 1).
Hence **if a_h ≠ 2 every homomorphic image of E(F_h) in F_h^* has order ≤ |a_h − 2| ≤ 2√h + 2**; only at a_h = 2
(N = h − 1, "E(F_h) lives in the (h−1)-world") can it be large. Symmetrically the (h+1)-world is a_h = 0 (N = h + 1).
For fixed non-CM E/ℚ, a_h = 2 occurs for ≍ √X/log X primes h ≤ X (Lang–Trotter CONJECTURE); density zero is known
unconditionally (Serre, Publ. IHÉS 54, 1981), with X^{4/5}-type upper bounds under GRH (Serre; Murty–Murty–Saradha).
*Proof.* A homomorphism to the cyclic group F_h^* has image of order dividing exp E(F_h) and h − 1, hence dividing
gcd(N, h − 1) = gcd(h + 1 − a, h − 1) = gcd(2 − a, h − 1); Hasse gives |a| ≤ 2√h. ∎
**(2) The firing-relevant part is still orthogonal (PROVED).** For m | h + 1, m > 2, any homomorphism A → F_h^* (A any
finite abelian group) sends elements of order dividing m into μ_{gcd(m, h−1)} ⊆ {±1}. So the m-part of E(F_h) — the
part that could encode "4cd | h + 1" — never reaches p's world, ordinary or not; ordinary curves only add a prime-to-m
image of size ≤ 2√h + 2 (a ≠ 2).
**(3) Canonical maps have bounded image (PROVED relative to Mazur).** The reduced Tate pairing t_n(Q, ·) : E(F_h) → μ_n
is canonical when Q is a GLOBAL n-torsion point; then n | #E(ℚ)_tors ≤ 16 (Mazur), so the image μ_{ord Q} has ≤ 12 elements
(Mazur: points of order ≤ 12). Large images need h-dependent data (a non-canonical choice of subgroup of F_h^*), i.e. no information.
CM variant: E(F_h) ≅ O/(π − 1) (Lenstra) and O → O/𝔥 ≅ F_h is a ring map, but O^* (imaginary quadratic) has ≤ 6
elements; non-unit α ∈ O give tier-(c)-type conditions h | N(p + Xα) — for O = ℤ[√−d], α = 2c√−d this is the
Type I number p² + 4c²d: **Type I is the imaginary-quadratic, finite-unit analogue of the tier-(c) bridge of
BRIDGE_WORLDS §2**, whose real-cyclotomic version has infinite units (§6).
**(4) The box needs trace 0.** The ES integers c, d, j with 4cdj = h + 1 are divisor data of N iff a_h = 0. With trace a
the analogous condition 4cd | h + 1 − a, h = 4cdj − 1 + a, turns h | p + 4c²d into h | pj + (1 − a)c — a different
equation (a = 2: the signed variant h | pj − c). (PROVED, one line: 4cdj ≡ 1 − a mod h.)
**(5) Size ceiling** (R206 repair (ii) in TORSION_FIRING): any sufficient firing rule at h fires inside −Box(k),
|Box(k)| ≤ τ(k)²; an image of size up to 2√h + 2 can only enter as a lottery.

## Cheap numerics
scripts/y3_ordinary.py 20000 (E: y² = x³ + x + 1, 1134 primes h ≡ 3 mod 4): supersingular h: 10; gcd(#E, h − 1) ≥ √h: 10
(rare, as (1) predicts); (h+1)-part reaching F_h^* beyond ±1: 0.

## Barrier screen
B3 (images ≤ 2√h + 2 and box ≤ h^{o(1)}: lottery), B2 (a_h = 2 primes are a density-zero moving set), Mazur (canonical
maps), T1 not engaged (no sufficient rule produced).

## Assessment
COLLAPSES: ordinary reductions are genuine bridges (D3 is right), but their homomorphic images are Hasse-bounded
except at Lang–Trotter primes a_h = 2, the firing-relevant m-part stays orthogonal, canonical maps are Mazur-bounded,
and the ES box is a trace-0 object. By-product: the trichotomy a_h = 0 / a_h = 2 / other = (h+1)-world / (h−1)-world /
Hasse-bounded mixture, and "Type I = finite-unit (imaginary quadratic) tier (c)".
