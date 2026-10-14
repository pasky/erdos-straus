# TWO_FIBRES — the two bad fibres of X₀(2p), words as hyperbolic matrices, and the cubic-lattice model of the χ = +1 side (task O209, spark relay Y1)

Status: checkpoint 1 (O209). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on SIGN_IDENTITY.md (O205: Prop 4.1, Thm 2.2, Prop 2.3), CHI_FLIP.md (Thm 1.1, Cor 1.3), CONSTRUCTIVE_ES.md
(Thm 1.2, Thm 2.1, Cor 2.2), KUDLA_ES/DIFF_DEEP ((J)13), bsA_fricke_vieta. Memos BRAINSTORM/y1_*; scripts `scripts/y1_*`.
Notation (CHI_FLIP): word w = (t, u, v), n = tuv − u − v odd, A = tu − 1, A* = tv − 1, AA* = tn + 1, χ(w) = (−A/n),
G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]] (det n), L_w its lattice, T_w = [[A*, 1], [1, A]] (det tn), M_w = S_vS_tS_u.

## Summary (checkpoint 1)
* **Theorem A (PROVED; classical inputs).** The χ = +1 fibre is the cubic lattice: for every odd n and word w,
  Diff(T_w) = {2} ⟺ n·G_w is the Gram matrix of three vectors of ℤ³ ⟺ ∃ x, y ∈ ℤ³, |x|² = A*, |y|² = A, x·y = 1.
  For p prime the χ = +1 lattices of det p are exactly L_ℓ = {x ≡ λℓ (mod p)} (Q = |x|²/p), ℓ on the conic
  x² + y² + z² ≡ 0 (mod p); 𝔊⁺_p is the image of P¹(𝔽_p)/S₄ (onto, not always injective) — the Hurwitz/Cerednik–Drinfeld side made explicit.
  **ES-five(p) ⟺ some p·G_w (w ∈ X_p) is not a Gram matrix of integer vectors** (non-embeddability).
* **Theorem B (T1, integral form; PROVED).** Every path lattice of odd square determinant m² is an index-m sublattice of
  ℤ³; for m = q prime it is ker(f mod q) for a functional f **off** the conic f·f ≡ 0 (forced by cyclicity of the
  discriminant group).
* **Proposition G″ (PROVED relative to the PNT for cuspidal GL(m) L-functions; memo y1_gl3_cuspidal; R214 repair D6).**
  No finite combination of exponent-zero twisted divisor convolutions d_k(n; ψ…) and coefficients λ_π(n)ψ(n) of unitary
  cuspidal π on GL(m) (any m ≥ 2, any characters) equals N₋ — **unconditionally**, including all self-dual orthogonal
  (Sym²/Ad) π that O205 left open. The mechanism is **size at primes, not T1**: on primes ℓ ≡ 1 (L) every d_k(ℓ; ψ…) = k, so
  E is constant there, the cusp part has mean o(1), and N₋ ≥ ω₃(p + 1) has divergent mean. (The earlier Prop G′ used T1
  plus a one-prime genericity hypothesis, which fails e.g. for Ad of a tetrahedral weight-one form — R214 D7; that analysis
  survives only as Remark G in the memo.)
* **Hyperbolic reading (memo y1_gamma8_trace; G1, G2 PROVED):** χ is a function of M_w mod 8 (Γ(8)-conjugation invariant)
  and not an SL₂(ℤ)-class function; the ES content of a trace-formula count is the extraction of three-letter presentations,
  at most a T^{−2/3+ε} fraction (B3; R209 repair of an unproved T^{−1+o(1)}).
* **Constructions that failed (§3):** three-squares certificates give only a sufficient local condition (nothing beyond Hasse at p); a sign-dominance
  injection N₊(p) ≤ N₋(p) is **false** (2 402 primes p ≡ 1 (4) below 10⁶ violate it; the worst are p ≡ 1 (24) with (p/5) = +1 — R214 repair D9: *not* archimedeanly near squares); parity
  gives only (p + 2, 1, 1); Cerednik–Drinfeld/Ribet/JL transfers act on edge sets, not on path data (B2).
* Assessment: one new exact dictionary with a usable asymmetry (class number one on the χ = +1 side) and one steering
  theorem (G″). No route to ES; the content stays the level-t divisor-in-class lottery (B2).

## 0. Iteration log (construction first; barrier as steering wheel)
(I1) O205's two fibres are asymmetric: the char-2 side is B_{2,∞}, class number one. Construct the explicit model →
Theorem A (§1). Barrier hit: H3 is a genus statement on a divisor-in-class family (B2).
(I2) Violate "genus data only": use the *integral* class-number-one structure to produce more than genus information —
at squares this gives Theorem B (T1 as a positive embedding), at primes only local certificates (§3.1).
(I3) Violate "bounded multiplicity / main-term certificates" (B3): look for a structural injection χ = +1 → χ = −1 at
fixed p (it would prove ES-five, since (p + 2, 1, 1) has χ = +1 for p ≡ 1 (4)). Refuted numerically (§3.2).
(I4) Violate "finite fixed-level Eisenstein" (Thm 9.1/Prop 2.3) by cuspidal GL(3) terms (O205 spark (c)) → Prop G″ (R214 repair: killed by size at primes, T1 not needed):
dead, including the orthogonal class (memo y1_gl3_cuspidal).
(I5) Violate "class function" (trace formulas): χ is a Γ(8)-class function (G1) but the words are a non-spectral
extraction (memo y1_gamma8_trace).
(I6) Two-fibre swaps (Cerednik–Drinfeld, Ribet bimodule, GKZ at level t): dictionaries, no forcing (memos y1_cerednik_swap,
y1_heegner_level_t); involutions: y1_reciprocal_parity.

## 1. Theorem A — the cubic-lattice model of the χ = +1 fibre (PROVED)

**Theorem A.** Let n be odd and w ∈ X_n. TFAE:
(i) Diff(T_w) = {2}, i.e. (−A/ℓ)^{v_ℓ(n)} = +1 for every odd prime ℓ (for n = p prime: χ(w) = +1);
(ii) C₀(L_w) ⊗ ℚ ≅ B_{2,∞};
(iii) ∃ x, y ∈ ℤ³ with |x|² = A*, |y|² = A, x·y = 1; moreover x, y can be chosen with x × y ≡ x + y (mod t) (after composing with a reflection if necessary: an improper
signed permutation turns it into x × y ≡ −(x + y); R214 repair D1);
(iv) L_w(n) embeds isometrically in I₃ = ℤ³, i.e. n·G_w is a Gram matrix of three integer vectors.
*Proof.* (i)⟺(ii) is CHI_FLIP Thm 1.1 with SIGN_IDENTITY Prop 4.1(b). (ii)⇒(iii): C₀(L_w) = ℤ⟨1, α, β, αβ/t⟩
(CONSTRUCTIVE) is an order of B_{2,∞}, contained in a maximal order; B_{2,∞} has one conjugacy class of maximal orders,
the Hurwitz order H, whose trace-zero part is ℤi + ℤj + ℤk = ℤ³ with nrd = |·|² (the half-integral Hurwitz elements have
half-integral real part). So i = 1 + α, j = 1 + β (trace zero, nrd A*, A, ij + ji = −2) become x, y ∈ ℤ³ with x·y = 1. With
z = x × y, ij = −x·y + x × y = −1 + z, so (1 − i)(1 − j) = z − x − y = αβ = tγ (γ = e₁e₃ ∈ C₀) lies in tH and has real part
0, hence lies in tℤ³. (iii)⇒(ii): x, y do not commute (det T_w = tn ≠ 0), so ℚ⟨x, y⟩ = H ⊗ ℚ = B_{2,∞}; its structure
constants depend only on T_w, so it is ≅ C₀(L_w) ⊗ ℚ. (iii, with congruence) ⇒ (iv): γ := (z − x − y)/t ∈ ℤ³ satisfies
γ·x = −(A* + 1)/t = −v, γ·y = −u, |γ|² = (A + 1)(A* + 1)/t² = uv, so M := ℤx + ℤy + ℤγ ⊂ ℤ³ has Gram
[[A*, 1, −v], [1, A, −u], [−v, −u, uv]] ≅ adj(G_w) = nG_w⁻¹ (det n²). Then ℤ³ ⊂ M^#, [M^# : ℤ³] = n, so nM^# ⊂ ℤ³ and the
n-multiples of the dual basis have Gram n²·(nG_w⁻¹)⁻¹ = n·G_w. (iv)⇒(ii): L_w ⊗ ℚ is similar to I₃ ⊗ ℚ, and the even
Clifford algebra is a similarity invariant. ∎
CHECKED. (iii) ⟺ (i): all 81 857 words of odd n ≤ 3001 (`scripts/y1_three_squares.c`, 0 mismatches; 7 824 words with
χ = +1 but Diff ⊋ {2} correctly do not lift, e.g. (1, 2, 23) ∈ X₂₁: 21 = x² + y² is impossible); primes ≤ 12 000 and all primes in (99 000, 10⁵]: see §5.
(iv): `scripts/y1_z3_gram.py 451`: 3 435 words of primes (⟺ χ = +1), 4 290 of composites (⟺ Diff = {2}), 0 failures.
The congruence in (iii) is attained for every lifting word with n ≤ 151.

**Corollary A1 (ES-five as non-embeddability).** For p prime, ES-five(p) ⟺ ∃ w ∈ X_p with p·G_w ∉ Gram(ℤ³) ⟺ ∃ w whose
binary T_w is not represented by x² + y² + z² (Gauss's three-squares genus of det tp, Disq. art. 278–292). Here ES-five(p)
⟺ N₋(p) ≥ 1 is MODEL_SPECIFIC Thm 3.1(a) with CHI_FLIP Cor 1.3 / CONSTRUCTIVE Cor 2.2 (R214 repair D4).
*Classical content (R214 repair D2).* (i) ⟺ (iii) is the classical local–global principle for binary forms represented by the
one-class genus of x² + y² + z² (Gauss, *Disq.* art. 288–292; Mordell 1930; Ko 1937; Siegel), specialised to T_w; Thm B and
Prop A2 are standard maximal-lattice/one-class-genus arguments (A2 ≈ Eichler orders of level p in the Hurwitz order ↔ P¹(𝔽_p)
mod units, as in the LPS/Brandt-matrix literature). Only the word-level packaging is new to the campaign.

**Proposition A2 (the χ = +1 genus is the conic).** For p prime, the positive ternary lattices L of det p isotropic at p
are exactly the L_ℓ := ({x ∈ ℤ³ : x ≡ λℓ (mod p), λ ∈ ℤ}, |x|²/p) with ℓ ∈ C(𝔽_p), C: x² + y² + z² = 0.
*Proof.* Such L is unimodular at odd ℓ ≠ p and isotropic at p, so C₀(L) ⊗ ℚ is ramified exactly at {2, ∞}: C₀ ≅ B_{2,∞},
and L ⊗ ℚ ≅ I₃(p) ⊗ ℚ (a ternary space is determined up to similarity by C₀; the scale is fixed by det). Hence
L(p) ⊗ ℚ ≅ I₃ ⊗ ℚ; L(p) lies in a norm-maximal lattice on this space; these form one genus (O'Meara 91:2), and ℤ³ is
norm-maximal (an index-2 overlattice would need x/2 with x ∈ ℤ³ ∖ 2ℤ³, |x|² ≡ 0 (4), impossible), so that genus is gen(I₃),
which has one class (R214 repair D3); so
L(p) ↪ ℤ³ with index p² (determinants p⁴ vs 1). The image M has all inner products ≡ 0 (p), so M mod p is totally
isotropic in 𝔽_p³, of dimension ≤ 1, and [ℤ³ : M] = p² forces M = pℤ³ + ℤℓ̃ with ℓ̃·ℓ̃ ≡ 0 (p). Conversely each L_ℓ is
integral, positive, of det p⁴/p³ = p, and L_ℓ ⊗ ℚ ≅ I₃(1/p) ⊗ ℚ has C₀ ≅ B_{2,∞}, so it is isotropic at p. ∎
So 𝔊⁺_p = image of C(𝔽_p)/O(ℤ³) ≅ P¹(𝔽_p)/S₄, hence at most #orbits ≈ (p + 1)/24 classes. CERTIFIED (`scripts/y1_conic_orbits.py`, against
`scripts/ce_classes.py`): equal counts for p = 13, 17, 29, 37, 41, 61, 73, 97, 101; p = 109: 6 orbits, 5 classes. R214 repair
D5 (independent enumeration, `scripts/review_r214_conic.py`): for **all** primes 5 ≤ p ≤ 127 the map is onto; it is injective
except at **p = 71 (3 → 2), 79 (4 → 3), 107, 109, 113, 127** (each time two size-24 orbits merge — two orbits can give
isometric lattices since ℤ³ need not be the unique unimodular overlattice; Assessment: the w_p swap of an edge's ends).
*Reading.* This is Deligne–Rapoport + Cerednik–Drinfeld made concrete: the singular points of X₀(2p)_{𝔽₂} are
X₀(p)^{ss}_{𝔽̄₂} = P¹(𝔽_p)/Aut(E_{j=0}) (A₄ = Hurwitz units mod ±1), and the cube group S₄ adds w₂. A χ = +1 word is a
point ℓ of the conic **together with a path basis of L_ℓ**; a χ = −1 word is an edge of the supersingular 2-isogeny graph
together with a path basis (CONSTRUCTIVE (J)35), and that side has no class-number-one model (class number of B_{p,∞}
≈ p/12).

## 2. Theorem B — T1 as an embedding (PROVED)

**Theorem B.** Let n = m² be an odd square. Every path lattice L_w (w ∈ X_n) is isometric to an index-m sublattice of ℤ³:
there are a, b, c ∈ ℤ³ with |a|² = v, |b|² = t, |c|² = u, a·b = b·c = −1, a·c = 0. If m = q is prime, L_w = ker(f mod q)
for a primitive f ∈ ℤ³ with f·f ≢ 0 (mod q).
*Proof.* L_w ⊗ ℚ has square determinant and C₀ ≅ B_{2,∞} (SIGN_IDENTITY Prop 4.1(d)), so L_w ⊗ ℚ ≅ I₃ ⊗ ℚ. L_w lies in
a norm-maximal lattice on this space; these form one genus (Eichler; O'Meara 91:2), and ℤ³ is norm-maximal (R214 repair
D3: an index-2 overlattice would need x/2, x ∈ ℤ³ ∖ 2ℤ³, |x|² ≡ 0 (4)), so it contains I₃, and the
genus of I₃ has one class. Index: √(det L_w) = m. For m = q prime an index-q sublattice is ker(f mod q) for a primitive f;
if f·f ≡ 0 (mod q), then f ∈ M := ker f and f/q ∈ M^#, giving an element of order q in M^#/M outside the subgroup ℤ³/M ≅
ℤ/q, so M^#/M ≅ (ℤ/q)²; but the discriminant group of a path lattice is cyclic (the 2×2 minor of G_w equal to 1;
CHI_FLIP Cor 1.3), ℤ/q². ∎
CHECKED: all 736 words of odd squares ≤ 2601 lift in the sense of (iii) and all 209 in the sense of B (`y1_z3_gram.py 451`);
f off the conic for every word of q² with q ∈ {3, 5, 7, 11, 13, 17, 19} (`scripts/y1_square_sublattice.py`, 155 words).
*Reading.* T1 is the statement that **at square determinant the path lattices live inside the cubic lattice itself**,
not only after scaling: a positive, geometric form of "every ε_ℓ = +1". Any proof of ES-five(p) must use a property of
p·G_w ⊂ ℤ³ that fails for G_w ⊂ ℤ³ at squares; Theorem A identifies p·G_w-embeddability with the Hasse invariant at p
(local, so B5-safe but bound by B2); we do not claim every use of the integral model reduces to it.

## 3. Constructions on the asymmetric model (attempts)

**3.1 Certificates from the three-squares theorem (PROVED sufficient condition; nothing new).** If A or A* is of the form
4^a(8b + 7), then T_w is not represented by I₃, so Diff(T_w) ≠ {2}; for n = p this gives χ(w) = −1; e.g. (8, 1, v),
n = 7v − 1: χ = (−7/n) = (n/7) = −1. (R209 repair: this is **not** a characterisation and not a cell condition: (29, 1, 3),
p = 83, has A = 28 obstructed, while (5, 1, 3), p = 11, in the same cell mod 8, has A = 4, A* = 14 representable; and
(1, 4, 7), p = 17, has χ = −1 with A = 3, A* = 6 both sums of three squares — the obstruction is to the *binary* T_w.) Gauss's genus
conditions at odd ℓ | t are automatically satisfied (T_w ≡ −(x − y)² mod t), and at ℓ | n they *are* χ. So for a single word the
χ = +1 side's integral structure certifies nothing beyond the local sign (Theorem A: embeddability ⟺ Hasse invariant):
steering consequence — **the class-number-one asymmetry is invisible at the level of single words.**

**3.2 Sign dominance (REFUTED; CERTIFIED finite computation, reproduced from scratch by R214).** An injection χ = +1 → χ = −1 inside X_p would prove ES-five(p) for p ≡ 1 (4)
(the reversal-fixed word (p + 2, 1, 1) has χ = +1; y1_reciprocal_parity R1). The numbers forbid it: among the 39 174 primes
p ≡ 1 (4), 5 < p < 10⁶, **N₋(p) < N₊(p) for 2 402** (census `si_census.c`). (R214 repair D9 — the earlier
"primes just above a square" description was wrong.) The 13 primes < 10⁶ with N₊ ≥ 4N₋ are 1249, 2521, 3049, 3361, 9601,
13 249, 29 401, 70 249, 225 289, 297 049, 361 321, 871 249, 925 369 (e.g. 2521: N₋ = 4, N₊ = 33; 871 249: N₋ = 46, N₊ = 185).
Several are **not** archimedeanly near a square (29 401 = 171² + 160, 225 289 = 474² + 613, 871 249 = 933² + 760, gaps to the
next square 183, 336, 1 107). What all 13 share is arithmetic: **p ≡ 1 (24) and (p/5) = +1** (11 of 13 also (p/7) = +1) —
p is a quadratic residue modulo the small moduli that short words see, which is the (J)27 reading ("p looks like a square
to the small moduli"), not "p is close to m²". Some are also m² + 24 or m² − 3, or values of other small forms
(29 401 = 6·70² + 1, 871 249 = 2·660² + 7²). So no fibre-swapping injection exists.

**3.3 Counting on both sides is genus-level (Assessment).** On the χ = +1 side the representation numbers r(T_w, I₃) are
given exactly by Siegel's formula (one class), and on the χ = −1 side Σ_O r(T_w, O⁰)/|O^×| over maximal orders of B_{p,∞}
is given by Siegel–Weil for the Gross-lattice genus. Both evaluate a *fixed* T_w (and note N₊(p) = #{w : r(T_w, I₃) > 0}, not Σ_w r(T_w, I₃)/48 — e.g. p = 5: 5 vs 6); neither says which T in the level-t family
F_t(p) = {t·diag(v, u) − R} lies in which genus — the divisor-in-class event (B2). The family sum is a family extraction
from the genus-2 theta series of I₃ (Thm 2.2 of O205 forbids a modular generating function in n).

**3.4 Fibre split versus masses (EVIDENCE/Assessment).** Eichler masses give ratio (p − 1)/4 : (p + 1)/12 → 3, matching
the cell ratio 240 : 80; per class mod 8 the census ratio Σ N₋/Σ N₊ (primes ≤ 10⁶) is 1.55, 2.25, 2.12, 5.42 for
p ≡ 1, 3, 5, 7 (8): the split is governed by 2-adic cells, not by fibre masses.

## 4. Barrier summary
* B2: every statement here (A1, 3.1–3.3) is "the level-t family meets the χ = −1 genus" — the moving modulus is t.
* B3/B6: trace formulas see the words only as at most a T^{−2/3+ε} fraction (R214 repair D11) (y1_gamma8_trace); JL/Ribet/level raising act on
  edge sets uniformly in families (y1_cerednik_swap).
* B5/T1: Theorem B is T1, now as an embedding into ℤ³; Theorem A at primes uses only the Hasse invariant at p.
* Thm 2.2 / Prop 2.3 (O205) extended: Prop G″ excludes all finite combinations of twisted d_k's and unitary GL(m) cusp
  coefficients, unconditionally, by size at primes (not T1); an exact identity for N₋, if any, must have a non-constant
  main term on primes ≡ 1 (L), i.e. lie outside that class.

## 5. Numerics (all tiny outputs)
| check | script | range | result |
|---|---|---|---|
| (iii) ⟺ Diff = {2} | y1_three_squares.c | all odd n ≤ 3001 (81 857 words) | 0 mismatches |
| (iii) ⟺ χ = +1, primes | y1_three_squares.c `p` | primes ≤ 12 000 (27 413 + 94 402 = 121 815 words); all primes in (99 000, 10⁵] (12 053 words) | 0 mismatches |
| T1: all words lift | y1_three_squares.c `sq` | odd squares ≤ 10⁵ (8 073 words) | all lift |
| (iv), Thm B | y1_z3_gram.py | n ≤ 451 (7 934 words) | 0 failures |
| f off conic | y1_square_sublattice.py | q ≤ 19 | all off conic |
| 𝔊⁺_p = image of conic/S₄ | y1_conic_orbits.py; R214 review_r214_conic.py | 10 primes ≤ 109; R214: all 5 ≤ p ≤ 127 | onto; non-injective at 71, 79, 107, 109, 113, 127 |
| sign dominance | si_census.c | primes ≤ 10⁶ | false at 2 402 primes |
