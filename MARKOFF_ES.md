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
