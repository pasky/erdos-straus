# bsD_artin_conjugation — the ES ray class −1 is complex conjugation: Type II asks for a divisor whose Artin symbol in ℚ(ζ_M) is the Frobenius at ∞ (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. No script (dictionary; the parity part is bsC Prop 1).

## Idea
Translate the ray condition into Galois language and ask which part of it any reciprocity can see. Under
Gal(ℚ(ζ_M)/ℚ) ≅ (ℤ/M)^×, the class −1 is **complex conjugation c = Frob_∞**. So Type II(p) reads: *for some
M = 4cd, the integer N = 1 + cMp has a divisor f whose Artin symbol σ_f in ℚ(ζ_M)/ℚ equals the archimedean Frobenius*
("a finite avatar of the infinite place"). Since N ≡ 1 (M), σ_N = 1 and the co-divisor f′ has σ_{f′} = c too.

## Literature
Neukirch, ANT VI §5–6 (Artin map, ray class fields of ℚ); Gross–Zagier, *Heegner points and derivatives of
L-series*, Invent. 84 (1986), II §1 (complex conjugation and Atkin–Lehner action on Heegner points:
c(𝒪, 𝔫, [𝔞]) = (𝒪, 𝔫̄, [𝔞]⁻¹), w_N(𝒪, 𝔫, [𝔞]) = (𝒪, 𝔫̄, [𝔞𝔫⁻¹])); bsC_valence_borcherds (Type II certificate =
Heegner point of discriminant −4Mcp on X₀(M)); bsC_parity_quadratic_only Prop 1.

## Statement / analysis
**Dictionary (PROVED, tautological).** With K = ℚ(ζ_M), K⁺ its maximal real subfield: f ≡ −1 (M) ⟺ σ_f|_{K⁺} = 1
and σ_f|_K ≠ 1 (for M > 2). The ray condition splits into
(i) a **quadratic sign part** (σ_f nontrivial on the CM extension K/K⁺) — exactly what Diff-parity over K⁺ can see
(bsC Prop 1 with F = K⁺, η = η_{K/K⁺}); and
(ii) the **K⁺-part** σ_f|_{K⁺} = 1, i.e. f ≡ ±1 (M): a condition in the group (ℤ/M)^×/{±1} of order φ(M)/2, with
**no archimedean anchor** (K⁺ is totally real; c acts trivially on it).
So the order-≥3 content R of KUDLA_ES §2 lies in "σ_f trivial on the totally real field K⁺" (R177 repair: the K⁺-part
also contains the even quadratic characters — for M | 24 it is entirely quadratic — so it is not *precisely* R). Reciprocity laws
anchor at ∞ through c; on K⁺, c is invisible — a second way of seeing bsD_frobenius_closure Thm 2(b).
**Heegner/real-structure attempt (Assessment).** On X₀(M), the anti-holomorphic involutions c∘w_d act on Heegner points
by [𝔞] ↦ [𝔞⁻¹𝔡]; their fixed points are governed by [𝔞]² = [𝔡] — genus theory (2-torsion of the class group).
Fixed-point theorems for anti-holomorphic involutions (Harnack/Lefschetz: real ovals) give real points, not CM points of
a given discriminant, and the CM points among them are a 2-torsion (genus) condition again. No order-≥3 handle.

## Barrier screen
* **Hypotheses → escapes.** The decomposition (i)+(ii) is forced by c having order 2. An escape would need a
  mechanism anchored at a *non-archimedean* place whose Frobenius has order ≥ 3 — e.g. "f ≡ ℓ₀ (M)" for a fixed small
  prime ℓ₀ (a divisor that imitates a finite place). ES's target is −1, not a finite Frobenius (H-A: moving modulus).
* B2 (the K⁺-part is the class-layer divisor event); T1 passes; B1 for any fixed finite set of M.

## Assessment
Dictionary (PROVED, elementary), negative as a route: the ES target class is the archimedean Frobenius, so every
reciprocity anchored at ∞ sees only its quadratic shadow; the remaining order-φ(M)/2 part lives on a totally real
field where nothing anchors it. Promise 1 (clarifying; explains *why* the R-part has no Siegel–Weil incarnation).

## Correction / extension (written after a second pass; supersedes the "no archimedean anchor" sentence above)
Over F = K⁺ = ℚ(ζ_M)⁺ itself the ray condition **does** have an archimedean anchor: η = η_{K/F} is a *quadratic* ray
class character of F of conductor 𝔪·∞₁⋯∞_r (every real place of F ramifies in the CM field K), and for an ideal 𝔞
of F prime to M, `Art_{K/F}(𝔞) = N_{F/ℚ}𝔞 mod M ∈ {±1}`. Hence **for divisors f that are norms of F-ideals
(f = N_{F/ℚ}𝔞, e.g. all prime factors ≡ ±1 mod M), f ≡ −1 (M) ⟺ η(𝔞) = −1 — a quadratic, parity-visible
condition over F.** bsC_parity_quadratic_only Prop 1 does not apply, because its data t are ℚ-rational; here the
data are F-ideals. The cost moves to F-rationality: only the "split part" of N (prime factors ≡ ±1 mod M, density
2/φ(M) among primes) can carry such 𝔞 with N𝔞 | N. Numerics and assessment: LDP_DEEP.md §A.4.
