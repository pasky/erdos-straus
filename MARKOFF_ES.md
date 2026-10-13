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

## 3. Integral model, local conditions, T1 and Brauer–Manin

Integral model: 𝒮_{n,D} := Spec ℤ[A, B, λ]/(nA² + B² + D − 2DλAB) (S_{n,D} with C = 2Dλ, isomorphic over ℚ).
Admissible local sets: W_ℓ ⊂ 𝒮(ℤ_ℓ) cut out by: not(ℓ | A and ℓ | B); ℓ | n ⇒ ℓ ∤ B; for ℓ = 2 also A even, B odd;
W_∞ = {A, B, λ > 0}. Admissible integral points = 𝒮(ℤ) ∩ ∏_v W_v = the V_n-points with this D.

**Lemma 3.1 (local solubility; PROVED).** ∏_v W_v ≠ ∅ ⟺ (i) D ≡ 3 (mod 4), (ii) gcd(D, n) = 1, and (iii) every
prime ℓ | D has (−n/ℓ) = 1. Call such D *admissible*.
*Proof.* ℓ = 2: A even, B odd forces nA² + B² + D ≡ 1 + D ≡ 0 (mod 4); conversely for D ≡ 3 (4), A = 2, B = 1,
λ = (4n + 1 + D)/(4D) ∈ ℤ₂. ℓ | D odd: λ ∈ ℤ_ℓ needs v_ℓ(nA² + B² + D) ≥ v_ℓ(D) + v_ℓ(AB); if ℓ | A then ℓ ∤ B and
the left side is a unit, if ℓ | B then ℓ ∤ A and ℓ | n (excluded by W_ℓ) or the left side is a unit; so ℓ ∤ AB,
ℓ ∤ n and −n ≡ (B/A)² (mod ℓ); conversely Hensel. ℓ ∤ 2D: A = B = 1 (or any units) gives λ ∈ ℤ_ℓ. ∞: any A, B > 0. ∎

**Corollary 3.2 (T1 is a fibrewise LOCAL obstruction; PROVED).** For n = m² no D is admissible: (−m²/ℓ) = (−1/ℓ),
so (iii) forces D ≡ 1 (mod 4), contradicting (i). Hence for every D ≥ 1 the admissible adelic set of 𝒮_{m²,D} is
empty — at ℓ = 2 if D ≢ 3 (4), otherwise at some prime ℓ ≡ 3 (4) dividing D to an odd power. The only global input
is "an integer ≡ 3 (mod 4) has a prime factor ≡ 3 (mod 4) to an odd power", i.e. reciprocity for (−1/·) applied to
the PARAMETER D. On the 3-fold V_n (D a coordinate) this is a Brauer–Manin obstruction:

**Proposition 3.3 (family BM; PROVED).** On V_n (coordinates A, B, λ, D), β := (−1, D) is unramified along the
divisor {D = 0} = {nA² + B² = 0} iff n is a square (that divisor is ℚ-irreducible with function field
ℚ(√−n)(A, λ), D is a uniformiser there since ∂/∂B = 2B − 2λDA = 2B ≠ 0, and −1 is a square in ℚ(√−n) iff n ∈ ℚ^{*2}).
For n = m² and every admissible adelic point (W_v as above, now with D ∈ ℤ_v free), Σ_v inv_v β = 1/2: inv₂ = 1/2
(D ≡ 3 mod 4 at 2), inv_ℓ = 0 for odd ℓ (ℓ | D forces (−1/ℓ) = 1 by Lemma 3.1(iii)), inv_∞ = 0 (D > 0). So T1 for
the whole ES^{[2]} family is the BM obstruction of the single quaternion algebra (−1, D) — the same algebra as
CHI_FLIP Prop 1.6 in different coordinates. For non-square n the class is ramified and gives nothing.

**Proposition 3.4 (no Brauer–Manin obstruction on any admissible fibre; PROVED).** Let D be admissible. Then
(∏_v W_v)^{Br S_{n,D}} = ∏_v W_v ≠ ∅.
*Proof.* By Prop 2.2 it suffices to show that some place realises all four values of (α₁, α₂) while the other
places stay fixed. D ≡ 3 (4) has a prime ℓ ≡ 3 (4) with v := v_ℓ(D) odd; ℓ is admissible, so r² ≡ −n (mod ℓ) for
some r. At P_ℓ = (A, B, λ) ∈ W_ℓ (A, B units, B ≡ ±rA mod ℓ^v): α₁(P_ℓ) = (A, −D)_ℓ = (A/ℓ)^v = (A/ℓ) and
α₂(P_ℓ) = (B, −nD)_ℓ = (B/ℓ) = (±r/ℓ)(A/ℓ). Choosing (A/ℓ) and the sign ± freely ((−1/ℓ) = −1) realises all four
pairs; Hensel lifts any such residue choice to a point of W_ℓ (λ is then determined and ℓ-integral). ∎
*Reading.* The prime ℓ ≡ 3 (4), ℓ ∥_odd D, that T1 forbids at squares (Cor 3.2) is exactly the prime that kills
every Brauer–Manin obstruction at non-squares. So for non-square n, nothing local or Brauer-theoretic stands in
the way on any admissible fibre; existence is a pure "integral Hasse principle in the λ-direction" question.
Note this is a statement about the FIBRE surfaces, whose integral points (if any) lie on infinitely many
λ-conics; unlike GS Thm 1.1 there is no compact fundamental set, so emptiness of S_{n,D}^{adm}(ℤ) is not even
known to be decidable for a single D.

(Notation note after R201: GROWING_MUTE's (A, B) form now allows Q of any parity (R201 M1); V_n and everything
below are unchanged — they never use the parity of Q. R201 m2: "only one integral Vieta involution" holds for
every odd n > 1; consistent with §4 below, where no hit with n | λ ever occurs.)

## 4. The continued-fraction dictionary: ES is depth 3

**Theorem 4.1 (norm-form dictionary; PROVED).** Fix n odd, μ ≥ 1, N := 4(μ² − n), and D ≥ 1 odd with
gcd(D, n) = 1, D | μ, λ := μ/D. The admissible points of V_n with this (λ, D) are in bijection with pairs
{±x}, z ≥ 1, gcd(x, z) = 1 and x² − N z² = −D, via A = 2z, B = μA ∓ x (the two signs are the ι_B-pair).
D ≡ 3 (mod 4) and x odd are then automatic.
*Proof.* (μA − B)² − (μ² − n)A² = B² − 2μAB + nA², so the V_n equation is x² − (μ² − n)(2z)² = −D. D odd ⇒ x odd,
x² ≡ 1 (8) ⇒ D ≡ 3 (4). A even, B ≡ x odd, gcd(A, B) = gcd(2z, x) = 1. B·B' = (μA)² − x² = nA² + D, so for q | n,
BB' ≡ D ≢ 0 (mod q): gcd(B, n) = 1. B > 0 since x² < μ²A². ∎

**Theorem 4.2 (CF dictionary; PROVED).** Let Q_k (k ≥ 1) be the complete-quotient denominators of the regular CF of
√N (p_{k−1}² − N q_{k−1}² = (−1)^k Q_k). If μ² > 4n/3, then: admissible points of V_n with λD = μ ⟷ odd k with
Q_k odd, gcd(Q_k, n) = 1 and **Q_k | μ** (point: D = Q_k, A = 2q_{k−1}, B = μA ∓ p_{k−1}). Hence
`  ES^{[2]}(n) ⟺ ∃ μ (> √(4n/3)) ∃ odd k : Q_k(√(4μ² − 4n)) is odd, prime to n, and divides μ`
(up to the finitely many μ ≤ √(4n/3), whose Pell equations must be checked separately; ⇐ holds for all μ).
*Proof.* ⇐: Thm 4.1 with (x, z) = (p_{k−1}, q_{k−1}) (convergents are coprime). ⇒: D ≤ μ < 2√(μ² − n) = √N
when μ² > 4n/3, so by Lagrange's criterion (|x² − Nz²| < √N, gcd = 1 ⇒ x/z is a convergent) |x|/z = p_{k−1}/q_{k−1},
and the sign of −D forces k odd. ∎

**Theorem 4.3 (ES's shot family is exactly depth 3; PROVED).** Let μ > 2n, and write μ = t + nj with
t ∈ {1, …, n}, j ≥ 2. Then a₀ = 2μ − 1, a₁ = 1, a₂ = j − 1 and
`  Q₁ = 4μ − 1 − 4n,   Q₂ = 4n,   Q₃ = 4tj − 1,   (p₂, q₂) = (2μj − 1, j).`
Q₁ > μ never divides μ. The depth-3 point is (A, B) = (2j, 1) (and its ι_B-partner B = 4μj − 1), so for μ > 2n:
**B = 1 ⟺ k = 3**, and the depth-3 condition Q₃ | μ reads (4tj − 1) | (t + nj) ⟺ (4tj − 1) | n + 4t² (as
gcd(4tj − 1, 4t) = 1 and 4t(t + nj) ≡ 4t² + n) — the classical shot family "n + 4t² has a divisor ≡ −1 (mod 4t)".
All hits at k ≥ 5 are overflow solutions (B > 1).
*Proof.* √N ∈ (2μ − 1, 2μ) iff μ > n + 1/4. Then m₁ = 2μ − 1, Q₁ = N − (2μ − 1)², a₁ = ⌊(√N + 2μ − 1)/Q₁⌋ = 1 as
4μ − 1 < 2Q₁ for μ > 2n. m₂ = Q₁ − m₁ = 2μ − 4n, Q₂ = (N − m₂²)/Q₁ = 4n(4μ − 1 − 4n)/Q₁ = 4n. a₂ =
⌊(√N + m₂)/4n⌋ = ⌊(4μ − 1 − 4n)/4n⌋ (the numerator lies in (4μ − 1 − 4n, 4μ − 4n), and 4n ∤ 4μ − 1 − 4n + θ for
θ ∈ (0, 1)) = j − 1, remainder 4t − 1. m₃ = 4n a₂ − m₂ = 2μ − 4t, Q₃ = (N − m₃²)/4n = (4t(μ − t) − n)/n = 4tj − 1.
Convergents: (p₀, q₀) = (2μ − 1, 1), (p₁, q₁) = (2μ, 1), (p₂, q₂) = (a₂·2μ + 2μ − 1, a₂ + 1) = (2μj − 1, j), so
B = 2μq₂ ∓ p₂ ∈ {1, 4μj − 1}. Conversely B = 1 means x = 2μz − 1, i.e. x/z = [2μ − 1; 1, z − 1], a convergent of
index 2 (k = 3); the alternative expansion has index 3 and the wrong sign. ∎
*Check (`scripts/mk_depth3.py 3000 13 17 29 37 41 73 97 101 105 21`):* the Q₁..Q₃ formulas for all 2n < μ ≤ 3000;
every B = 1 hit is at k = 3 (B = 1 counts: 0, 2, 4, 0, 2, 4, 0, 8, 2, 0 branches); no hit has n | λ. And
`scripts/mk_depth.py n 400 400` (n = 13, 17, 29, 73, 97): every V_n point found by brute force (A, B ≤ 400,
μ ≤ 400) is a CF hit, and every CF hit satisfies V_n and all side conditions; n = 9, 25: 0 hits (T1 control).

*Reading.* In the CF of √(4μ² − 4n) the first three steps are polynomial in (t, j) and produce ES's finite shot
family (a finite search: Q₃ | μ forces t ≲ n/4, λ ≈ n/(4t) bounded). Overflow solutions are the same divisibility
"Q_k | μ" at greater depth. For large j at fixed t the CF keeps following a polynomial pattern whose partial
quotients run through the Euclidean algorithm of (n, t) (computed: a₃ = ⌊n/t⌋, Q₄ = 4a₃(n mod t)·j + O(1)), with
odd-position Q_k ≈ c_k·j; a hit Q_k | t + nj then forces λ ≲ n/c_k and finitely many j. When the Euclidean pattern
ends, some even-position Q becomes constant and the expansion branches by j modulo that constant — the moving
modulus of B2 appearing as CF branching. (This last paragraph is an Assessment from the computed first steps,
not a proved structure theorem.) The parallel with DEDEKIND_ES (J)9 — ES certificates are HJ length-3 words — is
striking: in both continued-fraction languages ES is "length/depth 3".

## 5. No parametric families in the λ-direction

**Theorem 5.1 (PROVED).** Let n > 0 be a non-square and D ≥ 1. There is no triple of polynomials
(A(s), B(s), λ(s)) ∈ ℚ[s]³ with λ non-constant and nA² + B² + D = 2Dλ·AB identically.
*Proof.* Put μ = Dλ, f = μ² − n ∈ ℚ[s], R = ℚ[s][√f]. f = (μ − √n)(μ + √n) with coprime non-constant factors, so f
is not a constant times a square and R is the coordinate ring of the affine curve y² = f(s), with exactly two
places at infinity (leading coefficient D²·lc(λ)² is a square). Hence R^* = ℚ^* × ⟨ε⟩ (rank ≤ 1 = #places at ∞ − 1).
η = μ + √f has norm n (a unit, non-constant), and α = B − μA + A√f has norm −D (a unit). Write η = c ε^b (b ≠ 0)
and α = c' ε^a. Norms: n = c²N(ε)^b and −D = c'²N(ε)^a. If b is odd, N(ε) > 0 (as n > 0), so N(α) > 0,
contradiction. If b is even, n = (c N(ε)^{b/2})² is a square, contradiction. ∎
*Reading.* Fixed-D solutions are sporadic in λ: each λ is a separate arithmetic event in the real quadratic
order O_λ = ℤ[2√(λ²D² − n)] (Thm 4.1: "the prime ideal(s) above D are principal"; the sign of the generator is
automatic because x² − 4dz² ≢ 3 mod 4). Contrast GS (1.5): Markoff V_k has polynomial curves iff k = 4 + ν². So B1
(identities) is closed in the λ-direction too, and existence is a class-group question.

## 6. The fibrewise integral Hasse principle in λ: a large main term, blocked by class groups

Fix n non-square and an admissible D (Lemma 3.1). For each λ, Thm 4.1 asks whether x² − N_λ z² = −D
(N_λ = 4(λ²D² − n)) has a primitive solution. Split the event in two layers:
* **local (genus) layer**: primitive solubility at every p. For odd p | λ²D² − n it says (−D/p) = 1; at 2 it says
  D ≡ 7 (8) or λ even (x odd, so −D + N z² must be ≡ 1 mod 8, and only z mod 2 matters). So λ must avoid the two
  roots of λ²D² ≡ n mod p for every p with (n/p) = 1, (−D/p) = −1: a half-dimensional sieve condition, expected
  density ≍ (log Λ)^{−1/2} (Assessment; a lower bound of this order is what Iwaniec's half-dimensional sieve gives
  for such quadratic-polynomial conditions — not re-derived here);
* **global (class) layer**: the genus-admissible ideal above D is actually principal in O_λ.

**EVIDENCE (`scripts/mk_fibreHP.py 300 1,3000,30000 <n…>`, every reported hit re-checked by the convergent
identity; assertion "global ⇒ local" never failed).** Entries hit/locally-ok for λ in [L₀, L₀ + 300), L₀ = 1, 3000,
30000, three smallest admissible primes D:
`  n=13:  D=7: 49/63 30/48 37/49 | D=11: 49/83 34/66 41/72 | D=19: 21/32 16/22 10/19`
`  n=17:  D=3: 79/104 58/87 51/74 | D=7: 104/163 95/142 68/116 | D=11: 60/80 47/63 40/60`
`  n=21:  D=11: 57/76 41/65 37/59 | D=19: 42/64 45/64 29/54 | D=23: 76/99 47/73 51/73`
`  n=29:  D=3: 42/62 39/52 28/44 | D=11: 45/65 34/57 28/41 | D=19: 56/85 42/66 40/64`
`  n=33:  D=7: 88/131 72/104 59/95 | D=19: 44/60 39/56 36/52 | D=23: 96/165 81/147 66/130`
`  n=37:  D=19: 22/31 19/31 12/26 | D=23: 81/125 68/110 63/100 | D=31: 40/60 30/44 29/41`
`  n=41:  D=3: 52/70 41/56 35/54 | D=7: 73/127 76/114 55/86 | D=11: 72/108 47/89 62/86`
`  n=53:  D=3: 50/80 46/68 41/68 | D=19: 41/85 38/71 42/64 | D=23: 75/106 66/97 53/80`
`  n=57:  D=11: 53/70 43/60 27/47 | D=23: 96/144 89/123 66/118 | D=31: 74/127 53/105 54/92`
`  n=61:  D=7: 23/34 20/25 22/28 | D=11: 45/86 46/72 26/61 | D=23: 80/125 58/100 54/94`
`  n=73:  D=7: 46/69 25/52 30/50 | D=11: 59/105 53/84 39/70 | D=31: 37/60 29/50 19/40`
`  n=89:  D=3: 39/47 28/42 18/31 | D=7: 85/123 51/102 56/86 | D=19: 64/104 55/86 39/77`
`  n=97:  D=7: 50/72 27/52 28/53 | D=19: 25/37 20/27 20/26 | D=23: 89/168 72/141 61/127`
`  n=101: D=3: 42/63 31/50 25/41 | D=7: 71/97 63/77 54/76 | D=11: 56/79 39/67 37/59`
`  n=105: D=11: 46/80 40/60 27/58 | D=19: 35/51 28/45 34/45 | D=31: 81/117 53/90 56/95`
`  n=113: D=3: 75/98 57/84 58/78 | D=19: 55/87 45/70 40/64 | D=23: 83/132 67/106 50/97`
So P(global | local) ≈ 0.45–0.8 and drifts down only slowly with λ (to 10⁵: n = 13, D = 7: 11/15; n = 17, D = 3:
11/25 in [10⁵, 10⁵ + 100)). T1 controls: n = 9, 25 have no admissible D; with the non-admissible D = 7, 11 (n = 9)
and 3, 7 (n = 25), 0/300 locally ok and 0 global (`scripts/mk_genus.py 300 9 7 9 11 25 3 25 7`).
Interpretation (Assessment): the regulators are large (e.g. n = 13, D = 7, λ = 10005: period 21 012 for
√N ≈ 1.4·10⁵), so class numbers are small, as Cohen–Lenstra predicts for real quadratic orders; given the genus,
the class is principal with probability bounded below. Hit depths k are deep inside the period (k = 2329 of 21 012
in that example), i.e. these are not bounded-depth (ES-like) solutions.

**Proposition 6.1 (what the λ-direction does to the barrier map; Assessment built on PROVED Thms 4.1–5.1).**
(a) B6 does not apply (n fixed) and **B3 does not apply**: the heuristic number of λ ≤ Λ with a point on a single
admissible fibre is ≍ Λ/(log Λ)^{1/2} — a polynomially large main term, against log³ p for ES (the price: the
solutions have size exp(Λ^{1−o(1)})). The local layer of this main term is a provable half-dimensional sieve
statement.
(b) B1 is closed in this direction (Thm 5.1: no parametric families at fixed D), and every bounded-depth piece of
the CF is a finite search (depth 3 = ES, Thm 4.3).
(c) The residual step is: **for some genus-admissible λ, the ideal above D is principal in ℤ[2√(λ²D² − n)].** This is
a Gauss/Cohen–Lenstra-type class-group statement in a one-parameter quadratic family of real quadratic orders. No
unconditional technique proves even that some real quadratic family contains infinitely many orders with a given
split prime principal outside Richaud–Degert-type families — and the RD subfamily here (n | λ) is exactly the one
killed by reciprocity (GROWING_MUTE Prop 1.2(c); observed: no hit with n | λ). So the λ-direction trades ES's
divisor-in-a-moving-class lottery for a class-group lottery: a different, famous open problem, not a proof.
(d) A pigeonhole variant (fix λ, let D run over divisors of a highly composite μ, Davenport constant of Cl(O_μ))
needs h(O_μ) ≲ ω(μ) and a target (not zero-sum) element of the narrow class group, so it reduces to the same
class-number input.

## 7. Can the B = 1 locus (ES) be reached? (task 4)

**Proposition 7.1 (PROVED).** (a) On a fixed fibre, the curve {B = 1} ∩ 𝒮_{n,D} : nA² + 1 + D = 2DλA has only
the integral points with A | D + 1 (finitely many). (b) A Pell orbit (fixed λ, D) meets B = 1 in at most one
ι_B-pair: along the orbit the convergent index grows and B ≈ nA/(2μ) grows geometrically, and B = 1 is the
depth-3 convergent (Thm 4.3), so an orbit reaches ES iff its reduced point already is the ES point.
(c) Composition inside one order O_μ: if α_i = B_i − A_iη have norms −D_i (D_i | μ), then α₁α₂ has norm +D₁D₂
(≡ 1 mod 4: wrong sign, not a V_n point) and α₁α₂α₃ has norm −D₁D₂D₃ (a V_n point if D₁D₂D₃ | μ), but it is a
product of three depth-≥3 elements and lands at depth 3 only by coincidence; across different μ there is no
composition (different quadratic orders).
*Proof.* (a) A | 1 + D from the equation mod A. (b) Thm 4.2–4.3 and the cone description of GROWING_MUTE
Prop 1.2(b). (c) multiplicativity of the norm; the mod-4 sign rule of §5. ∎
*Reading.* The ES locus is a thin curve on each fibre, so integral-point theory gives no help (Siegel-finite, and
hitting it is the depth-3 divisibility (4tj − 1) | n + 4t², the classical lottery). Vieta/automorph moves and
composition move AWAY from depth 3. O201 spark 3 (composition) does not give ES.

## 8. Verdict (O202 checkpoint 1)

1. **Literature (§1, checked against full texts).** GS prove the integral HP for almost all k and infinitely many
   failures for x² + y² + z² − xyz = k; LM/CTWX compute the BM obstruction for those surfaces; Dao treats the
   four-holed-sphere family. None applies directly: S_{n,D} is not Markoff-type (no C², A₂ singularity at infinity,
   no Markoff mixing), and the ES content is the condition "level divides a coordinate" (2D | C), which GS-type
   counting cannot see (B2). Erratum: the author of arXiv:2202.07142 is Quang-Duc Dao.
2. **Brauer group and T1 (§2–3; PROVED).** Br S_{n,D}/Br ℚ = (ℤ/2)², ⟨(A, −D), (B, −nD)⟩, no transcendental part.
   T1 is a *fibrewise local* obstruction (every D fails at 2 or at a prime ℓ ≡ 3 (4) ∥_odd D), and on the 3-fold
   V_n it is the BM obstruction of (−1, D), unramified iff n is a square. For non-square n, every admissible fibre
   has empty BM obstruction — killed by the very prime that T1 uses at squares.
3. **CF dictionary (§4; PROVED).** ES^{[2]}(n) ⟺ some odd-index CF denominator Q_k of √(4μ² − 4n) divides μ;
   **ES's shot family is exactly depth k = 3** (Q₃ = 4tj − 1, μ = t + nj), all overflow solutions are deeper.
4. **λ-direction (§5–6).** No parametric families (Thm 5.1, PROVED). On a single admissible fibre, a locally
   admissible λ is globally solvable with frequency ≈ 0.45–0.8 (EVIDENCE, 16 n × 3 D, λ to 3·10⁴, spot checks
   at 10⁵): a polynomially large main term (≍ Λ/√log Λ), so B3 and B6 do not bite. The missing step is a
   Cohen–Lenstra/Gauss-type principal-ideal statement in the family ℤ[2√(λ²D² − n)], a famous open problem; the
   Richaud–Degert subfamily where class groups are controllable (n | λ) is exactly the one killed by reciprocity.
5. **Status: ES^{[2]} / ES^{(y,1)} for all non-squares OPEN; ES untouched.** Positive outcome: an exact
   translation of ES^{[2]} into a class-group question for real quadratic orders with a large heuristic main
   term; ES itself is its depth-3 truncation.
