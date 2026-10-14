# LENGTH_THREE — one object behind every "length 3" (task O206, wave Y-c)

Status: in progress (O206). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on DEDEKIND_ES (DK, (J)9), HJ_DEEP ((J)15), MARKOFF_ES ((J)37), COMPOSITION_ES ((J)38), FIXED_MODULUS_SHOTS
((J)25), CHI_FLIP. Scripts `scripts/l3_*`.

Notation. A *word* is (c, m, s) ∈ ℤ³_{≥1} with N := K(c, m, s) = mcs − c − s > 0 (negative continuant); h := cm − 1,
h′ := ms − 1. (R-self repair: N > 0 is required — (1,1,1) gives N = −1 and a degenerate pentagon.) A word with all letters
≥ 2 is *interior*; words with a letter 1 are *formal* (boundary) words and are NOT HJ fractions of length 3 (e.g. (1, 4, 2) at
N = 5, while L₃(5) = ∅). For interior words, N/h′ = [[c, m, s]] is an HJ fraction of length 3 (DK Lemma 1.1, with DK's
(v, t, u) = (c, m, s), A = h′, A* = h). Type II cube point (c, d, j) (FMS Lemma 1.1): h = 4cdj − 1 | pj + c,
s := (pj + c)/h.

## 0. Iteration log

(Y1) Searched for a common geometric carrier. First guess: the closed geodesic (Zagier cycle) of the cyclic word
(c, m, s). Killed: its trace is N − m, unrelated to the discriminant 4(μ² − n) of (J)37. Second guess: act with the
word matrix γ = M(c)M(m)M(s) on the (J)37 form [n, −2μ, 1]: no simplification (sympy). Third: the word is a
**Farey pentagon**, and its five continuants are the λ-lengths of the pentagon, i.e. the five cluster variables of
an A₂ cluster algebra with one frozen value N (§1). The other "length 3" statements are readings of this pentagon
at a CM point (Machin, §2) and along the orthogonal pencil of one geodesic (CF depth, §3).

## 1. The object: a Ford-decorated Farey pentagon = an A₂ frieze with one frozen value N (PROVED, elementary)

**Proposition 1.1.** Let c, m, s ≥ 1 and N = K(c, m, s). The vectors
`V₁ = (0, −1), V₂ = (1, 0), V₃ = (c, 1), V₄ = (h, m), V₅ = (N, h′)`
(cusps 0, ∞, c, c − 1/m, N/h′) satisfy |det(V_i, V_k)| =: λ_{ik} with
* sides λ₁₂ = λ₂₃ = λ₃₄ = λ₄₅ = 1, closing side λ₅₁ = N;
* diagonals λ₁₃ = c, λ₂₄ = m, λ₃₅ = s (the three letters), λ₁₄ = h, λ₂₅ = h′.
For letters ≥ 2 the four unit sides form the HJ path ∞ → c → h/m → N/h′ (DK §5.1). With Ford horocycles,
λ_{ik} are Penner λ-lengths, and the five Ptolemy relations of the pentagon are
`  cm = h + 1,   ms = h′ + 1,   hh′ = mN + 1,   hs = N + c,   ch′ = N + s.`   (P)
Conversely every positive integer solution (c, m, s, h, h′) of (P) with N > 0 is a (possibly formal) word with N = K(c, m, s);
it is an HJ length-3 fraction iff c, m, s ≥ 2. So "positive integral A₂ frieze with frozen (1,1,1,1,N)" = formal word, and
"length-3 HJ word" = such a frieze with all three letters ≥ 2 (R-self repair).
*Proof.* V_{i+1} = b_i V_i − V_{i−1} with (b) = (c, m, s), so consecutive determinants are 1 and
det(V_{i−1}, V_{i+1}) = b_i; the rest is expansion (e.g. det(V₃, V₅) = ch′ − N = s). Ptolemy = Plücker. The
converse: the first two relations define h, h′, and the third is then hh′ − mN − 1 = m(mcs − c − s − N), so N = K. ∎

(P) is the exchange pattern of the cluster algebra of type A₂ with frozen variables on the five sides of a pentagon
(cluster cycle c → h → m → h′ → s → c, exchange x_{k−1}x_{k+1} = x_k·(side) + (side)). So:
**a length-3 HJ word at N = a positive integral point of the A₂ cluster variety with frozen values (1, 1, 1, 1, N)
= a positive integral frieze of the pentagon with one non-unit boundary entry N.** The dihedral reflection fixing the
N-side is reversal (c ↔ s, h ↔ h′, m fixed).

**Corollary 1.2 (the five ES slices are the five cluster variables; PROVED, = DK Thm 4.5 restated).** For interior words
(letters ≥ 2) and N ≡ 1 (4):
`  (h′/N) = −1  ⟺  one of the five cluster variables c, m, s, h, h′ is ≡ 0 (mod 4).`
DK Thm 4.5's five conditions 4 | tu−1, tv−1, t, u, v are exactly 4 | h′, h, m, s, c. Each gives an ES solution (DK
Cor 1.2, Thm 4.5). The symmetric formulation is new as a statement (content is DK's).
CERTIFIED (`scripts/l3_dict.py 100000 5000`, 72 s): all 4 411 125 words with N ≤ 10⁵: pentagon determinants, (P),
Cor 1.2 (1 016 788 "some variable ≡ 0 mod 4" words with N ≡ 1 mod 4), 0 failures. Controls: all 156 odd squares
25 ≤ N ≤ 10⁵ have words, none with a variable ≡ 0 (mod 4); N = 105 has no interior word (HJ_DEEP (W)).

**Corollary 1.3 (the certificate cube is the pentagon with m = 4dj, N = pj; PROVED).** A Type II cube point (c, d, j)
is the word (c, 4dj, s) at N = pj (HJ_DEEP Prop 2.1 / FMS Lemma 1.1 rewritten), and FMS's three equivalent
divisibilities are Ptolemy relations of its pentagon: h | pj + c is hs = N + c; h | 4dj²p + 1 is hh′ = mN + 1; and
h | p + 4c²d with cofactor e = (c + s)/j follows from 4cd·(hs) = p(h + 1) + 4c²d. So the cube is the pentagon with
the middle diagonal ≡ 0 (mod 4) and the moving divisibility j | gcd(N/p, m/4) attached.
CERTIFIED (`l3_dict.py 100000 5000`): all 34 303 cube points of primes 5 ≤ p ≤ 5000, 0 failures.

Reading. The "3" of HJ length is the three short diagonals (c, m, s) of the pentagon. The cube's coordinates (c, d, j)
are one short diagonal c, and the factorisations m = 4dj (middle short diagonal) and N = pj (closing side).

## 2. The five slices are the five vertices: Ford-horocycle (Penner h-length) identities (PROVED, elementary)

For a decorated ideal triangle with λ-lengths, the horocyclic arc at vertex V of triangle (V, X, Y) has length
λ_XY/(λ_VX λ_VY) (Penner). Arcs add over a fan. In the Ford decoration, moving V to ∞ makes this the Farey telescoping
x_{i+1} − x_i = 1/(b_i b_{i+1}) (classical; cf. Farey-based Egyptian algorithms, e.g. Bleicher 1972 — from memory).

**Theorem 2.1 (vertex identities).** For every word (c, m, s) at N, the arc of the Ford horocycle at V_i between the two
pentagon sides at V_i has length λ_{i−1,i+1}/(λ_{i−1,i}λ_{i,i+1}). Cutting it by the two diagonals from V_i gives
three arcs. After dividing by N where needed:
| vertex | opposite diagonal | identity | ES slice (DK Thm 4.5) |
|---|---|---|---|
| V₁ = 0 | h′ = A | h′/N = 1/c + 1/(ch) + 1/(hN) | 4 ∣ A: Type I, a = 1 |
| V₂ = ∞ | c | c/N = 1/h′ + 1/(mh′N) + 1/(mN) | 4 ∣ v: e-slice (reversal) |
| V₃ = c | m | m/N = 1/(cs) + 1/(cN) + 1/(sN) | 4 ∣ t: Type II (A)3 |
| V₄ = h/m | s | s/N = 1/h + 1/(mhN) + 1/(mN) | 4 ∣ u: e-slice |
| V₅ = N/h′ | h = A* | h/N = 1/s + 1/(sh′) + 1/(h′N) | 4 ∣ A*: Type I reversal |
If the opposite diagonal is 4w, dividing by w gives 4/N as three unit fractions. These are exactly the five ES triples of
DK Cor 1.2 / Thm 4.5 (e.g. at V₁, DK's b = (N + c)/s equals h by the Ptolemy relation hs = N + c).
*Proof.* Each identity is a fan decomposition. For example at V₁ the fan is (V₁V₂V₃), (V₁V₃V₄), (V₁V₄V₅) with arcs
1/(1·c), 1/(c·h), 1/(h·N), and the total is λ₂₅/(λ₁₂λ₁₅) = h′/N. Algebraically each identity is one relation of (P).
For the three vertices whose fan contains the N-side, that arc is N/(⋯), and dividing by N makes it a unit fraction. ∎
CERTIFIED (`l3_dict.py 100000`): all five identities in exact rationals on all 4 411 125 words N ≤ 10⁵, 0 failures.

**Corollary 2.2 (SHARP dictionary).** For N ≡ 1 (mod 4): *ES five-slice certificate at N ⟺ a Farey pentagon with four
unit sides and closing side N in which some vertex has opposite diagonal ≡ 0 (mod 4) ⟺ (DK Thm 4.5) the Jacobi symbol
(A/N) = −1.* The ES triple is the vertex's horocycle, cut into three arcs by the diagonals from that vertex. All of Type II
(cube point (c, d, j)) is the V₃ identity of the pentagon (c, 4dj, s) at pj, divided by d:
4/p = 1/(dcs) + 1/(dcpj) + 1/(dspj).

## 3. Machin is the same pentagon read at a CM point on the side V₁V₂ (PROVED, elementary)

**Theorem 3.1.** Let (c, m, s) be a word at N, r := √(N/m), z* := ir ∈ ℍ (a point of the pentagon side V₁V₂ = (0, ∞)),
so z*² = −N/m. For x ∈ ℚ let K_x be the Möbius map z ↦ (xz − r²)/(z + x). It fixes z*, sends ∞ ↦ x, and is the rotation
about z* through the angle 2·arg(x + ir), clockwise in the standard orientation (K′_x(z*) = e^{−2i·arg(x+ir)}; R-self repair of
the sign), since x + z* ↦ K_x is the regular representation of ℚ(z*)^×. Then:
`(c + z*)(s + z*) = (c + s)(1/m + z*)  ⟺  K_c ∘ K_s = K_{1/m}  ⟺  K_c(s) = 1/m  ⟺  K(c, m, s) = N,`
i.e. arccot(c/r) + arccot(s/r) = arccot(1/(mr)) (all angles in (0, π/2)).
*Proof.* (c + z)(s + z) = (cs + z²) + (c + s)z = (cs − N/m) + (c + s)z, and cs − N/m = (c + s)/m ⟺ mcs − c − s = N.
K_c(s) = (cs − r²)/(s + c) = 1/m is the same equation. ∎
**Type II.** For m = 4dj, N = pj: r² = p/(4d) **does not depend on j**. Multiplying by 2d resp. m gives COMPOSITION
Prop 5.1 verbatim: 2d(c + z*) = 2cd + √−pd and m(1/m + z*) = 1 + 2j√−pd. So the two-term Machin relations of Type II are
the pentagons (c, 4dj, s) at pj read at the single CM point z*_d = i√(p/4d), the top of the geodesic
C_d : |z|² = p/(4d) (geodesic of [4d, 0, −p]). The three arccot arguments are the three short diagonals c, s, m (as 1/m),
scaled by 1/r. So the Machin "3" is the HJ "3".
*Relation to §2.* Machin is the arctan (elliptic) form of the V₃ identity: tan-addition gives
(r/c + r/s)/(1 − r²/cs) = rm, which is m = 1/c + 1/s + N/(cs). The horocyclic (parabolic) form of §2 keeps the cross
term N/(cs) as a third arc.
CERTIFIED (`l3_dict.py`): cs − (c + s)/m = N/m on all words N ≤ 10⁵; = p/(4d) on all 34 303 cube points (p ≤ 5000).

## 4. CF depth 3 is the same pentagon on a geodesic of the orthogonal pencil of C (PROVED, elementary)

Let (c, m, s) be a word at N, r² = N/m, and consider the pencil of quadratic algebras / binary forms
`  R_μ := ℚ(r²)[z]/(z² + μz + r²) for μ ∈ ℚ,   Norm_μ(X + Yz) = X² − μXY + r²Y²,`
an algebra over ℚ (r² = N/m ∈ ℚ). Geometrically, i.e. letting μ range over ℝ ∪ {∞} and taking the roots of z² + μz + r²
(at μ = ∞ only the geometric object, no algebra; R-self repair), this is the **orthogonal pencil of the geodesic C : |z| = r**. For |μ| < 2r it gives
the points of C (μ = 0 is z*), for |μ| > 2r the geodesics orthogonal to C (the product of their endpoints is r²), and for
μ = ∞ the pentagon side V₁V₂ = (0, ∞). Put ℓ_x := z + x (so ℓ_c, ℓ_s, ℓ_{1/m} are the three Machin elements).

**Theorem 4.1.** For every μ: m²·Norm_μ(ℓ_{1/m}) = hh′ − mμ (an arithmetic progression in μ, by hh′ = mN + 1). At the two
pencil members
`  μ_c := N + c = hs,   μ_s := N + s = ch′   (Ptolemy relations λ₁₄λ₃₅ = λ₁₅ + λ₁₃,  λ₁₃λ₂₅ = λ₁₅ + λ₃₅)`
it equals −h resp. −h′, and that value divides μ.
*Proof.* m²(1/m² − μ/m + N/m) = 1 − mμ + mN; at μ = N + c this is 1 − mc = −h. ∎

**Corollary 4.2 ((J)37/(J)38 are Thm 4.1 for Type II words).** Let (c, d, j) be a cube point of a prime p, i.e. the
word (c, 4dj, s) at pj, and put ω := 2dz. Then ω² + 2dμ·ω + pd = 0, so ℤ[ω] ⊂ R_μ is an order (the integral lattice is a choice; R-self repair),
m·ℓ_{1/m} = 1 + 2jω, and:
* d = 1, μ = μ_c = pj + c: ℤ[ω] = COMPOSITION's O = ℤ[√(μ² − p)] with ω = −η̄, and 1 + 2jω ∈ O′ = ℤ[2√(μ² − p)] is ε_μ = 1 − 2jη̄ of (J)38 Thm 1.3
  (t = c). Its norm −h = −(4cj − 1) divides μ because of the Ptolemy relation hs = N + c. In the regular CF of
  √(4μ² − 4p) it is the convergent of index 2 (depth 3) when j ≥ 2 (μ > 2p), resp. index 0 (depth 1) when j = 1
  ((J)37 Thm 4.3 + R202 M1). The mirror point (s, d, j) gives μ_s.
* general d, μ = μ_s: V_{pd} at μ_V = dμ_s = cd·h′ with λ = cd, D = h′ (COMPOSITION Prop 4.1(b)).
So **"the B = 1 slot ε_μ has norm dividing μ" is a Ptolemy relation of the pentagon**, read on the geodesic g_{μ_c} of the
orthogonal pencil of C. "Depth 3" is a statement in MARKOFF's coordinates (x, z_M) = (B − μA, A/2), where ε is the
convergent (p₂, q₂) of √(4μ² − 4p) and Lagrange's criterion applies. *R-self repair:* an earlier sentence placed this in
the cutting sequence of g_{μ_c} in the z-frame, read through the Ford horocycle at −1/m. That is FALSE: the change of frame is
affine but not unimodular. Example: (p, c, d, j, s) = (7, 2, 1, 3, 1) has m = 12, μ_c = 23, Q₃ = h = 23. In the z-frame the
form is [4, 92, 7], and |f(−1, 12)| = 92 > √8352/2, so that Ford horocycle misses the geodesic. The arithmetic dictionary
is unaffected.
CERTIFIED (`l3_dict.py … 5000`): for all 10 646 d = 1 cube points with p ≤ 5000, Norm = −h, h | μ_c, and the CF of
√(4μ² − 4p) has Q₃ = h (μ > 2p) resp. Q₁ = h (μ ≤ 2p), 0 failures. (For p ≤ 1000 the count is 1 736, matching the
COMPOSITION census.)

## 5. The unified object and the dictionary (summary)

**The object 𝒫(c, m, s; N):** the Ford-decorated Farey pentagon (0, ∞, c, c − 1/m, N/h′) with four unit sides and closing
side N. Equivalently: a positive integral A₂ frieze with frozen values (1, 1, 1, 1, N) (a formal word; the HJ word [[c, m, s]] when all letters ≥ 2); the
tridiagonal path form with diagonal (c, m, s), whose leading/trailing principal minors are the five cluster variables
and N (CHI_FLIP's Q_w). It comes with the geodesic C : |z|² = N/m, orthogonal to the side V₁V₂, and with the
orthogonal pencil of C.

| "length 3" statement | what it says about 𝒫 | where in ℍ |
|---|---|---|
| (J)9/(J)15 HJ length 3, five slices, (A/N) = −1 | some vertex's opposite diagonal ≡ 0 (4); the ES triple is that vertex's Ford horocycle cut by the fan (Thm 2.1, Cor 2.2) | the five cusps |
| (J)25 certificate cube (c, d, j) | 𝒫(c, 4dj, s; pj); the three divisibilities are Ptolemy relations (Cor 1.3) | λ-lengths |
| COMPOSITION Prop 5.1 Machin | rotation about z* = top of C: K_c(s) = 1/m (Thm 3.1); r² = p/4d independent of j | μ = 0 member |
| (J)37 CF depth 3 / (J)38 ε_μ | m²Norm(ℓ_{1/m}) = −h on g_{μ_c}, divisibility = Ptolemy hs = N + c (Thm 4.1, Cor 4.2) | μ = μ_c member |
| HJ path itself | the side V₁V₂ and the Farey path V₂…V₅ | μ = ∞ member |

The four "3"s: the three short diagonals (HJ letters = Machin arguments), the three arcs of a vertex horocycle (ES triple),
the three CF steps before the cusp −1/m (a Farey path on g_{μ_c}), and the cube coordinates (c, d, j) = (λ₁₃, factor of λ₂₄,
factor of λ₁₅). All of them are the single relation K(c, m, s) = N, i.e. the pentagon's Ptolemy system (P).
*Scope/novelty (Assessment; "new" means new in this campaign — no literature search was done, R-self repair).* Every individual identity is elementary and most are classical in disguise: continuants =
λ-lengths = frieze entries (Conway–Coxeter, Penner), Farey telescoping = h-lengths, Machin = regular representation. New
here: the identification of DK's five ES slices with the five vertices (Cor 2.2, with the five ES triples as fan decompositions),
and of the (J)37/(J)38 divisibility N(ε_μ) | μ with a Ptolemy relation, on one geodesic pencil.

## 6. The ES / ES^{(S)} gap in pentagon language: one side stops being tangent (PROVED, elementary)

Penner's identities hold for any decoration, so pentagons with non-unit sides give Egyptian identities with non-unit
numerators. For the frozen values (λ₁₂, λ₂₃, λ₃₄, λ₄₅, λ₅₁) = (Q², 1, 1, 1, n) and middle diagonal λ₂₄ = 4, the V₃ fan
gives
`  4/n = 1/(sn) + 1/(sc) + Q²/(cn),`
the ES^{(S)} shape of UNIT_ORBIT_ES (third numerator Q²). The Ptolemy system is 4c = Q² + h, hs = n + c, 4s = h′ + 1,
hh′ = Q² + 4n, ch′ = Q²s + n. **For Q odd these pentagons are in bijection with the divisors h ≡ 3 (mod 4) of 4n + Q²**
(c = (h + Q²)/4, s = (n + c)/h, using 4(n + c) = 4n + Q² + h). This is the fixed-modulus-4 shot. Geometrically the
Ford horocycles at 0 and ∞ are pulled apart to λ-length Q² (distance 4 log Q). ES is the case where all four
sides are tangent (Q = 1, or the general cube pentagon (c, 4dj, s)), and there the modulus 4cd·… returns.
CERTIFIED (`scripts/l3_mute_side.py 3001 15`): 23 510 such pentagons (odd n ≤ 3001, odd Q ≤ 15), Ptolemy + identity
exact, 0 failures.
*What does not work.* The decoration torus (rescaling horocycles, λ_ik ↦ f_if_kλ_ik) cannot make the Q²-side tangent
while keeping the closing side a multiple of a prime n and the other sides unit. Solving f₁f₂Q² = f₂f₃ = f₃f₄ = f₄f₅ = 1
forces λ₁₄ ↦ h/Q² and N ↦ f₁²Q²n, and integrality then needs Q² | h and Q²·(…) | n. So the torus does not transport
ES^{(S)} certificates into the O(p²) box (consistent with the exponent cap of (J)34). DK 8.3 scaling is the torus element
f = (α, α⁻¹, α, α⁻¹, α) (PROVED: it sends (c, m, s, N) ↦ (α²c, m/α², α²s, α²N) and fixes the sides and h, h′), so it is
HJ_DEEP Lemma 2.3's reparametrisation.

## 7. Constructive use of the unified object (task part 2): candidates and screens

Each item names the barrier hypothesis it tries to violate, then gives the outcome.

**7.1 Conway–Coxeter positivity (frieze side; violates "no deterministic input").** For all-unit frozen values, every
positive integral frieze has a quiddity equal to 1 (an ear). This is the deterministic engine behind "friezes =
triangulations". Here the quiddity at V_i is exactly the opposite diagonal (the ES slice variable of Thm 2.1). With one
frozen value N > 1, interior words have all five quiddities ≥ 2, and an ear exists only for boundary words (a letter 1).
Those are the divisor-of-N + 1 certificates of DK §4.2, which at p ≡ 1 (4) need (p + 1)/2 to have a prime factor
≡ 3 (mod 4): a fixed shot, not a theorem. Positivity plus integrality forces nothing mod 4. **Dead** (no analogue of
the ear lemma with a non-unit boundary value: L₃(N) = ∅ for N ∈ E_W, HJ_DEEP (W)).

**7.2 Exact identities over the whole decorated family (H-E; candidate (a) of the brief).** Penner/Farey telescoping
is exact over full Farey sequences (Σ 1/(bb′) = 1 over adjacent pairs) and over full fans. The ES object is a fan of
exactly three pieces with a congruence on the opposite diagonal. Summing over all A ∈ (ℤ/N)^× gives the classical
exact sums: Heilbronn's sum of partial quotients, and Dedekind sums (DK (D3), which only see r − r′). The length-3
count itself is the (★) divisor convolution. A signed count Σ χ is a 2-adic cell sum (CHI_FLIP 4.2), and
Eichler–Selberg places ES in the split-hyperbolic term (GROWING_IDENTITIES Prop 2.1). The pentagon adds no new
summation: its Ptolemy system is homogeneous of degree 2 in the λ's, so every identity it generates is a relation
among the same five divisor-type quantities. **No positive identity found (Assessment).**

**7.3 The moving pencil (candidate (b); violates B2's fixed-level hypothesis).** For Type II with fixed d, r² = p/(4d)
does not depend on j (Thm 3.1). So *all* cube points (·, d, ·) live on the orthogonal pencil of the single geodesic
C_d, and μ is part of the object. This is a genuine "moving geodesic family" in which the level is not fixed. But the
ES condition on it is Thm 4.1: m²Norm_μ(ℓ_{1/m}) = −D with D | μ. Eliminating μ = λD gives back
D(4djλ − 1) = 4dj²p + 1, the (d, j)-line. The modulus D is still part of the solution. **Reduces to B2/H-A** (PROVED
reduction; the pencil makes the level move, but the divisibility is still a Ptolemy relation with an unknown divisor).

**7.4 T1 as geometry (candidate (c)).** On the Type II slices the reason is visible in the Machin/CM picture (PROVED,
classical in substance — ET Prop 1.6 / Yamamoto): at n = M² the Machin field is ℚ(√−dM²) = ℚ(√−d). The target
1 + 2jM√−d is a *primitive* element of ℤ[√−d] of norm 1 + d(2jM)². So every odd prime q | 1 + 4dj²M² has (−d/q) = 1,
while h ≡ −1 (mod 4dj) forces the Jacobi symbol (−d/h) = −1. Proof of the last step: (−1/h) = −1; for d = 2^a d′ one
has (d′/h) = (−1/d′)(−1)^{(d′−1)/2} = 1, and (2/h) = 1 when a ≥ 1 since h ≡ −1 (mod 8). So no cube point exists at any
odd square (check: 0 cube points at all odd squares 9 ≤ M² ≤ 9801, inline probe). For d = e² the geodesic C_d has rational endpoints ±M/2e and this is Fermat's "1 + x² has no divisor
≡ 3 (mod 4)" in ℤ[i]. At a prime p the same computation gives only (−pd/q) = 1 for q | 1 + pd(2j)², so the requirement
(−d/h) = −1 becomes (p/h) = −1, a reciprocity condition that is satisfiable. (R-self repair: an earlier "extra genus
character of ℚ(√−pd)" was wrong, e.g. p = 7, d = 1 has trivial genus group and cube points exist.) Geometrically: at
squares the Type II CM point z* = iM/(2√d) is the M-dilate (a Hecke translate) of i/(2√d), and the condition no longer
involves N. This is the (J)13 "geometry sees only genus" statement in Machin form. It is not new
and gives no existence at primes.

**7.5 Equidistribution (candidate (d); screen against B3).** (R-self repair: an earlier version said that the points
z*_d equidistribute. That is FALSE: they are purely imaginary and stay on the imaginary axis mod SL₂(ℤ). Duke's theorem
concerns full Heegner packets of one discriminant, not these distinguished representatives.) Any equidistribution input
would have to come from the packet of [4d, 0, p] or from the pencil geodesics, and the ES event is an exact coincidence of
rational cusps, K_c(s) = 1/m, attached to one specific representative. Equidistribution controls sets of fixed positive
measure. I see no way to make it say anything about a single exact coincidence at a single p. **No route (Assessment)**;
no scale or average claim is made.

**7.6 Farey-chain slice (EVIDENCE, negative).** The cleanest fully "geometric" certificates are those where 4/p itself
is the h-length of a three-edge Farey chain seen from one cusp: 4/p = Σ 1/(b_ib_{i+1}) with b_i | b_{i−1} + b_{i+1}.
Among all ES solutions of primes < 400, 358/1615 Type I and 242/641 Type II solutions are such chains. The primes
13, 37, 97, 181, 193, 277, 373 have none (`/tmp` probe recorded here). It is another restricted slice set with failures.
That it fails infinitely often is expected by analogy with (J)2/B2 but NOT shown (R-self repair). **Not pursued.**

**7.7 What the unified language does buy (Assessment).** (i) The five slices are cyclically arranged (vertex ↔
opposite diagonal), so DK Thm 4.5 reads "the pentagon's mod-4 frieze has a zero quiddity ⟺ (A/N) = −1". The sign is
a property of the ℤ/8-frieze. (ii) (J)37/(J)38's "norm divides μ" and the cube's divisibilities are *Ptolemy
relations*, and Machin is the same relation at a CM point. So the four "length 3" phenomena are algebraically equivalent
restatements of K(c, m, s) = N. That does not prove that every mechanism seeing one sees all (Assessment, R-self repair),
but B2 appears in each as an unknown λ-length (the divisor h) inside the Ptolemy system. (iii) ES^{(S)} versus ES is "one
side non-tangent" (§6). A proof would have to produce pentagons with tangent sides. The decoration torus cannot do that
while keeping N = p (§6); other moves are not excluded.

## 8. Verdict (O206 checkpoint 1)

* **PROVED (elementary; CERTIFIED to N ≤ 10⁵ / p ≤ 5000 with controls).** One object carries all four "length 3"
  statements: the Ford-decorated Farey pentagon 𝒫(c, m, s; N), i.e. the positive integral A₂ frieze with frozen values
  (1, 1, 1, 1, N), together with the geodesic C : |z|² = N/m and its orthogonal pencil.
  * HJ length 3 = the pentagon's three short diagonals.
  * The five ES slices = the five vertices: each ES triple is a Ford horocycle cut by the vertex fan, and the slice
    condition is "opposite diagonal ≡ 0 (4)" (Thm 2.1, Cor 2.2).
  * The cube = the Ptolemy system with m = 4dj, N = pj (Cor 1.3).
  * Machin = rotation about the CM point z* = top of C (Thm 3.1). For Type II, z* depends on (p, d) only.
  * CF depth 3 / ε_μ = the pencil member μ_c = N + c, where "N(ε_μ) | μ" is the Ptolemy relation hs = N + c
    (Thm 4.1, Cor 4.2).
  * ES^{(S)} = the same pentagon with one side of λ-length Q² (§6).
* **Constructive (Assessment, §7).** No deterministic existence mechanism appears in the unified language. Every
  candidate reduces to the Ptolemy system, which contains the unknown divisor h, i.e. B2/H-A. This covers ear lemmas,
  exact identities, the moving pencil, T1 geometry and equidistribution. The pencil does make the level move (7.3),
  but the divisibility survives elimination.
* **ES is not solved; no infinite case of ES is claimed.**
