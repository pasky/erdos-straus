# AGENT REPORT O206 — one object behind every "length 3" (LENGTH_THREE.md)

Branch side-agent/length-three. Main file `LENGTH_THREE.md`. Scripts `scripts/l3_dict.py`, `scripts/l3_mute_side.py`.
**ES is not solved; no infinite case of ES is claimed.**

## SHARP
1. **The five ES slices are the five vertices of a Farey pentagon (Thm 2.1 / Cor 2.2).** A length-3 HJ word
   [[c, m, s]] = N/h′ is the Ford-decorated Farey pentagon (0, ∞, c, c − 1/m, N/h′): four unit sides, closing side N,
   diagonals c, m, s, h = cm − 1, h′ = ms − 1. Equivalently it is a positive integral A₂ frieze with frozen values
   (1,1,1,1,N), and the five continuants are the five cluster variables. DK Thm 4.5's five slices
   (4 | A, A*, t, u, v) are "the diagonal opposite vertex V_i is ≡ 0 (mod 4)". The ES triple is Penner's horocycle at
   V_i cut by the fan from V_i (Farey telescoping), divided by N where needed.
   So (J)9 reads: **(A/N) = −1 ⟺ some quiddity of the pentagon frieze is ≡ 0 (mod 4).**
2. **Machin, CF depth 3 and the cube are Ptolemy relations of the same pentagon on one geodesic pencil.**
   * Machin (COMPOSITION Prop 5.1) is the rotation about the CM point z* = i√(N/m), which lies on the side (0, ∞):
     K_c(s) = 1/m ⟺ K(c, m, s) = N. For Type II, r² = p/(4d) is independent of j (Thm 3.1).
   * (J)37/(J)38's "N(ε_μ) divides μ" is the Ptolemy relation hs = N + c, read on the member μ_c = N + c of the
     orthogonal pencil of the geodesic |z|² = N/m (Thm 4.1, Cor 4.2).
   * The cube's three divisibilities are Ptolemy relations (Cor 1.3).
3. **ES^{(S)} vs ES = one non-tangent side (§6).** Pentagons with frozen values (Q², 1, 1, 1, n) and middle diagonal 4
   correspond bijectively (Q odd) to the divisors h ≡ 3 (mod 4) of 4n + Q². They give 4/n = 1/(sn) + 1/(sc) + Q²/(cn),
   which is the fixed-modulus-4 shot. ES needs all four sides tangent. The decoration torus cannot transport one into
   the other at prime n. DK 8.3 scaling is a torus element.

## What was done
* §1 pentagon / A₂-frieze dictionary (Prop 1.1); Cor 1.2 (five slices = five cluster variables); Cor 1.3 (cube).
* §2 vertex identities (Thm 2.1): all five ES triples of DK Thm 4.5 are fan decompositions of Ford horocycles.
* §3 Machin = CM rotation on the pentagon side (Thm 3.1). It is the arctan form of the V₃ identity.
* §4 orthogonal pencil of C; Thm 4.1: m²Norm_μ(z + 1/m) = hh′ − mμ, equal to −h at μ_c = hs and −h′ at μ_s = ch′.
  Cor 4.2 recovers (J)38's ε_μ and (J)37's depth 3/1 split (j ≥ 2 vs j = 1), and V_{pd} for general d.
* §5 unification table. §6 ES^{(S)} gap. §7 constructive screens. §8 verdict.
* Numerics (exact rationals):
  * `l3_dict.py 100000 5000` (72 s) checked all 4 411 125 words with N ≤ 10⁵ (pentagon determinants, Ptolemy, five
    vertex identities, Machin, Cor 1.2) and all 34 303 cube points with p ≤ 5000 (10 646 with d = 1: norm, h | μ_c,
    and CF Q₃/Q₁ = h). 0 failures.
  * Controls: the 156 odd squares ≤ 10⁵ have no slice word; 105 has no interior word; there are 0 cube points at odd
    squares ≤ 9801.
  * `l3_mute_side.py 3001 15`: 23 510 Q²-side pentagons, 0 failures.

## Constructive verdict (Assessment)
No deterministic existence mechanism. Every candidate reduces to the Ptolemy system, whose unknown λ-length h is B2's
"modulus part of the solution":
* (7.1) Conway–Coxeter ear lemma: fails with a non-unit boundary value; E_W words do not exist.
* (7.2) Exact identities: the pentagon adds no new summation.
* (7.3) Moving pencil: the level moves, but μ eliminates back to the (d, j)-line.
* (7.4) T1: Machin field ℚ(√−dM²) = ℚ(√−d), so genus theory kills every cube point at squares (classical; PROVED
  three-line version). It gives nothing at primes.
* (7.5) Duke equidistribution: the target has measure zero (B3/B6).
* (7.6) Farey-chain slice: fails at 13, 37, 97, 181, 193, 277, 373.
The value of the result is the dictionary: the four "length 3" phenomena carry no independent information.

## Novelty / honesty
Each identity is elementary and most are classical in disguise:
* continuants = λ-lengths = frieze entries (Conway–Coxeter, Penner);
* Farey telescoping = h-lengths;
* Machin = the regular representation.

New as statements:
* the slices ↔ vertices identification, with the five ES triples as fan decompositions;
* "N(ε_μ) | μ = Ptolemy";
* the j-independence of the Type II CM point;
* the ES^{(S)} non-tangent-side reading.

Literature not searched (frieze-with-coefficients papers, e.g. Cuntz–Holm–Jørgensen, are cited from memory only in
the sparks below).

## Sparks (not pursued)
1. **Friezes over ℤ/4, ℤ/8.** Find a direct frieze-theoretic proof of Cor 1.2 (zero quiddity mod 4 ⟺ Jacobi −1),
   replacing DK's 512-cell check, e.g. via counts of SL₂(ℤ/8)-friezes (Morier-Genoud et al.). Link it to CHI_FLIP's
   2-adic isotropy.
2. **Friezes with coefficients** (Cuntz–Holm–Jørgensen, from memory). Is there a combinatorial model for positive
   integral friezes with boundary (1,1,1,1,N)? Lorenzini's (W) = HJ_DEEP's E_W would then become a statement about
   those objects.
3. **All of Type II on one geodesic.** The CM points z*_d = i√(p/4d) all lie on the side (0, ∞) at discrete heights.
   Type II(p) ⟺ some Machin rotation at one of these points. Could the diagonal flow along the imaginary axis, or Hecke
   correspondences between heights d and d′, relate certificates at different d?
4. **Longer polygons.** Vertex fans in (r + 2)-gons give r-term Egyptian identities with the same Ptolemy structure.
   Check whether k-term ES variants (k ≥ 4, known easy) have a pentagon-to-hexagon "ear-adding" proof that degenerates
   exactly at k = 3.
5. **Pencil at general μ.** ℓ_cℓ_s = (c + s − μ)z + (c + s)/m: a one-parameter family of Machin-type relations
   interpolating Machin (μ = 0) and the HJ side (μ = ∞). Is there a μ with an independent arithmetic meaning, e.g. the
   intersection with the closed geodesic of the cyclic word (trace N − m)?
