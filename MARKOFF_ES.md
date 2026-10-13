# MARKOFF_ES — ES variants as integral points on Markoff-type cubic surfaces (task O202, spark relay W)

Status: in progress (O202). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on GROWING_MUTE.md (O201, CLAIMED, under review R201): Prop 1.1 (A, B) form, Prop 1.2 (Markov-type equation),
Prop 2.2 (surfaces S_{n,D}). Scripts `scripts/mk_*`.

Notation (from O201). n > 1 odd. ES^{[2]}(n) shot data ⟺ (A, B, λ, D) ∈ ℤ_{>0}⁴ with
`  V_n :  nA² + B² + D = 2λD·AB,   A even, B odd, gcd(A, B) = gcd(B, n) = 1`
(ES^{(y,1)}: B squarefree; ES's shot family: B = 1). μ := λD, g := 2λAB − 1, D·g = nA² + B².
S_{n,D} : nA² + B² + D = ABC (an integral point of V_n is a point of S_{n,D} with 2D | C).

## 0. Iteration log

(W1) Literature (§1): GS's "Markoff type" class requires all three squares with coefficient ±1; S_{n,D} has no C²
and coefficient n on A². It is in GS's other class (reducible leading term, h = 1), where GS's "fullness" is trivial
here (A = B = 1 is a line on which F is linear). The ES content is the extra condition 2D | C: the LEVEL divides a
coordinate (B2).
(W2) Geometry (§2): S_{n,D} is a conic bundle over the C-line; both Vieta involutions preserve C, so the "Markoff
group" is fibrewise Pell, no mixing. Br S_{n,D}/Br ℚ = (ℤ/2)², no transcendental part.

## 1. Literature (checked 2026-10-13 against the arXiv full texts)

* **Ghosh–Sarnak**, *Integral points on Markoff type cubic surfaces*, Invent. Math. (2022), arXiv:1706.06712v3.
  Surfaces V_k : M(x) = x₁² + x₂² + x₃² − x₁x₂x₃ = k.
  * Thm 1.1: explicit compact fundamental sets F_k^± for the action of Γ (Vieta involutions, permutations, sign
    changes) on V_k(ℤ) for generic k; h_M(k) := number of Γ-orbits, finite; h_M(k) ≪ |k|^{1/3+ε}.
  * (1.6): Σ_{|k|≤K} h_M^±(k) ∼ C_± K (log K)² (average class number grows like log², "critical dimension").
  * Thm 1.2: (i) at least √K (log K)^{−1/2} Hasse failures with 0 < k ≤ K (quadratic reciprocity, k = 4 + βν²);
    (ii) M is *almost perfect*: #{|k| ≤ K admissible, h_M(k) = 0} = o(K). Method (Rem 1.3(d)): points with x₁ small
    (≈ power of log K) in a "tentacled" region; for fixed x₁ a binary quadratic form in (x₂, x₃); a variance bound
    via divisor sums for varying quadratic forms (Blomer–Granville) and Kloosterman's method for ternary forms.
  * (1.8): the Markoff group method applies to F = c x₁x₂x₃ + Σ a_ij x_i x_j + Σ a_i x_i + a **with a_jj = ±1 for
    j = 1, 2, 3**. Intro + App. A: if the cubic part F₀ is reducible (h(F) = 1), F is "full" (proof announced for a
    forthcoming paper, not in this one). Numerics: Hasse failures ≈ C K^{0.8875} for 0 < k ≤ 6·10⁸.
* **Loughran–Mitankin**, *Integral Hasse principle and strong approximation for Markoff surfaces*, IMRN 2021 no. 18,
  14086–14122, arXiv:1807.10223. U_m : x² + y² + z² − xyz = m. Thm 1.1/1.2: weak/strong approximation fails for all
  but ≪ B^{1/2} of |m| ≤ B. Thm 1.3: a BM obstruction to the integral HP forces m − 4 ∈ ⟨±1, 2, 3, 5⟩ mod squares.
  Thm 1.4: #{BM-explained Hasse failures, |m| ≤ B} ≍ B^{1/2}(log B)^{−1/2} (they note GS's claimed (log)^{−1/4} is
  really (log)^{−1/2}). Thm 1.5: #{failures NOT explained by BM} ≫ B^{1/2}/log B. For general m,
  Br U_m/Br ℚ ≅ (ℤ/2)³ (quaternion algebras). Prop 2.4: smooth cubic S minus a triangle of lines H:
  Br Ū ≅ ℚ/ℤ(−1) unless the lines meet in an Eckardt point.
* **Colliot-Thélène–Wei–Xu**, *Brauer–Manin obstruction for Markoff surfaces*, Ann. SNS Pisa (5) 21 (2020),
  arXiv:1808.01584. Same surfaces. Thm 1.1: if U_m(A_ℤ) ≠ ∅ then for every finite S, U_m(ℤ) is not dense in
  ∏_{p∉S} U_m(ℤ_p) (strong approximation fails, by reduction theory only); Cor 1.2: for m ≠ 0, 4 the Brauer group
  does not control strong approximation. Full computation of Br U_m (algebraic and transcendental parts).
* **Q.-D. Dao** (*not* "Qian Dong Dao" as in LITERATURE_AUTOMORPHIC.md — erratum), *Brauer–Manin obstruction for
  integral points on Markoff-type cubic surfaces*, arXiv:2202.07142 (JNT 2024). Surfaces
  x² + y² + z² + xyz = ax + by + cz + d with (a, b, c, d) the four-holed-sphere boundary-trace parametrisation
  (the Fricke cubic of BRAINSTORM/bsA_fricke_vieta F1). Thm 1.3: ≍ M⁴ of the |k_i| ≤ M have algebraic-BM-explained
  failures of strong approximation; also integral HP failures not explained by algebraic BM.
* Bourgain–Gamburd–Sarnak (2016): strong approximation mod p for Markoff triples (k = 0) — cited from GS's
  introduction, not re-read.

**What transfers (Assessment).** All four works study a FIXED cubic form with the level k varying, and their
positive results (GS Thm 1.2(ii)) count represented levels by putting one variable small and using that the rest
is a binary quadratic form of the other two. Our family is the level set F_n(A, B, C) := ABC − nA² − B² = D. Its
cubic part ABC is reducible, so it falls under GS's "h = 1" remark, where fullness is *trivial*: on the line
A = B = 1, F_n = C − n − 1 is linear, so every D is represented. The ES content sits entirely in the side condition
**2D | C (level divides a coordinate)**, which is not a congruence condition on (A, B, C) independent of the level:
substituting C = 2λD turns the level set into the 3-fold V_n, and "D is represented" into
D = (nA² + B²)/(2λAB − 1) ∈ ℤ, a divisor condition (B2). GS's counting does not see this condition, and LM/CTWX
compute obstructions for fixed surfaces (§2–3 below does that for S_{n,D}).

## 2. Geometry of S_{n,D} (fixed n odd, D ≥ 1)

**Proposition 2.1 (shape; PROVED, direct computation).** Let U = S_{n,D} : nA² + B² + D = ABC over ℚ.
(a) U is smooth (∇ = (2nA − BC, 2B − AC, −AB) vanishes only at A = B = 0, which is not on U since D ≠ 0). Its
closure X ⊂ ℙ³: W(nA² + B²) + DW³ = ABC has boundary X ∩ {W = 0} = the triangle ABC = 0 (as for Markoff) and
exactly one singular point, [0:0:1:0], of type A₂ (local equation AB = W(nA² + B²) + DW³). Markoff closures are
smooth; so S_{n,D} is NOT a "Markoff-type surface" in the sense of LM Prop 2.4 / CTWX / GS (1.8).
(b) U is a conic bundle over the C-line: the fibre over C = c is the Pell conic nA² − cAB + B² = −D (discriminant
c² − 4n). The two Vieta involutions ι_A : A ↦ BC/n − A and ι_B : B ↦ AC − B both FIX C (there is no involution in
C, which occurs linearly). So the "Markoff group" ⟨ι_A, ι_B⟩ acts fibrewise; ι_A ι_B is the Pell automorph of the
fibre. There is no mixing between fibres and no descent to a compact fundamental set as in GS Thm 1.1: the
integral points form a union of fibrewise Pell orbits, one family per value of C, and there are infinitely many
values of C to search. (For ES: C = 2λD, so the fibres are indexed by λ.)
(c) U ∩ {AB ≠ 0} ≅ G_m² (C = (nA² + B² + D)/(AB)), and U ∖ G_m² = L₊ ∪ L₋ ∪ M₊ ∪ M₋ with
L_± = {A = 0, B = ±√−D} and M_± = {B = 0, A = ±√(−D/n)}, each ≅ A¹_C. So U is an affine modification of the torus
(like the Bright–Loughran ES surface), not a Markoff surface.

**Proposition 2.2 (Picard and Brauer groups; PROVED modulo the standard Hochschild–Serre/purity facts quoted).**
(a) ℚ̄[U]^* = ℚ̄^* and Pic Ū ≅ ℤ(χ₁) ⊕ ℤ(χ₂), generated by [L₊], [M₊], where χ₁, χ₂ are the quadratic characters of
ℚ(√−D) and ℚ(√−nD).
(b) Br₁U / Br ℚ ≅ H¹(ℚ, Pic Ū) ≅ (ℤ/2)², generated by α₁ = (A, −D) and α₂ = (B, −nD).
(c) Br U = Br₁ U (no transcendental classes), although Br Ū ≅ ℚ/ℤ(−1) ≠ 0.
*Proof.* (a) A unit restricted to G_m² is cA^iB^j; A vanishes to order 1 along L_± (∂F/∂B = 2B − AC ≠ 0 there, so
(A, C) are local coordinates), B along M_± likewise, so i = j = 0. The localisation sequence
0 → ℚ̄[U]^*/ℚ̄^* → ℚ̄[G_m²]^*/ℚ̄^* = ⟨A, B⟩ → ⊕ℤ[L_±] ⊕ ℤ[M_±] → Pic Ū → Pic G_m² = 0 with div A = L₊ + L₋,
div B = M₊ + M₋ gives Pic Ū ≅ ℤ⁴/⟨(1,1,0,0), (0,0,1,1)⟩, and Galois swaps L₊ ↔ L₋ via χ₁, M₊ ↔ M₋ via χ₂.
(b) H³(ℚ, G_m) = 0 and (a) give Br₁U/Br ℚ ≅ H¹(ℚ, Pic Ū) = H¹(ℚ, ℤ(χ₁)) ⊕ H¹(ℚ, ℤ(χ₂)) = (ℤ/2)² (χ_i ≠ 1 since
D, nD > 0). α₁ is unramified on U: along L_± its residue is −D ∈ ℚ(√−D)(C)^{*2}, along M_± A is a unit; similarly
α₂ (residue −nD = n²·(−D/n) along M_±). Both are non-constant and independent in Br U/Br ℚ by the local
evaluation in Prop 3.3 below (all four sign patterns occur at one prime).
(c) Br Ū ⊂ Br(G_m²)_ℚ̄ = ℚ/ℤ(−1) (generated by symbols (A, B)_m); the residue of (A, B)_m along L_± is the
constant ±√−D, an m-th power in ℚ̄, so Br Ū = ℚ/ℤ(−1), with (Br Ū)^{G_ℚ} = ℤ/2 (generated by (A, B)₂). A class
of Br U lifting it would restrict on G_m² to (A, B) + (χ, A) + (χ', B) + const, χ, χ' ∈ H¹(ℚ, ℚ/ℤ); its residue
along the ℚ-irreducible divisor A = 0 (function field ℚ(√−D)(C)) is [√−D]·χ|_{ℚ(√−D)}. Vanishing needs a
character of G_ℚ whose restriction to ℚ(√−D) cuts out ℚ((−D)^{1/4}); that field is not the compositum of
ℚ(√−D) with an abelian extension of ℚ, because ℚ((−D)^{1/4}) is not Galois over ℚ (it would have to contain i, i.e.
ℚ(√−D) = ℚ(i), impossible for D ≡ 3 mod 4, and −D ≠ −4c⁴). So the lift does not exist. ∎
*Contrast.* LM Prop 2.4 / CTWX: for Markoff surfaces (smooth cubic minus a triangle without Eckardt point)
Br U_m/Br ℚ is generically (ℤ/2)³, and transcendental elements matter for special m.
