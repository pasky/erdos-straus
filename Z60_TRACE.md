# Z60_TRACE — trace formulas with R on the geometric side (wave z60, lane TRACE)

**ES is OPEN; (MS) is open. Nothing here proves or disproves either.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Brief: `z52bbriefs/z60_lanes.md` § TRACE with
`z58_lanes.md` (common rules, falsifier table) and `z53_depth.md`. Scripts `scripts/z60_trace_*`, data `data/z60/trace/`.

STATUS: checkpoint 1 (skeleton). Sections marked TODO are filled later.

Notation. R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; R_C(n) its C-slice; N = N_C(n) := 4Cn + 1. For C fixed,
(★)-solutions at C ↔ ordered divisor pairs dd' = N with d ≡ d' ≡ −1 (mod 4C), d = 4Cu − 1, d' = 4CB − 1 ("ES pairs",
class −1). "TRIV pairs" (class +1): dd' = N, d ≡ d' ≡ 1 (mod 4C), always including (1, N), (N, 1).
Weighted counts: ES_k(C, n) := Σ_{ES pairs} min(d, d')^{k−1}, TRIV_k(C, n) := Σ_{TRIV pairs} min(d, d')^{k−1}.

## 0. Prior art in the repository (git grep "Eichler", "Kuznetsov", "Hurwitz", "class number relation")

* GROWING_IDENTITIES (O170) §2, DISCOVERIES (J)10: via Cohen's Eichler–Selberg formula on Γ₀(q), χ, with q = 4C (or 4cd),
  N ≡ 1 (q): the ES class −1 enters the split-hyperbolic term A₃ only together with class +1, relative sign (−1)^k
  (Prop 2.1, PROVED rel. Cohen); Deligne needs ≍ kq-fold cancellation (Prop 2.2, Assessment); KH re-summation fails for
  the sum over C (§3, Assessment). **Elliptic side there = the generic Σ_t over all traces t with twisted root counts.**
* y1_gamma8_trace (O209): the Type I sign is a Γ(8)-class function, not an SL₂(ℤ)-class function; three-letter extraction
  is non-spectral. bsC_eichler_orientation, z9_brandt_screen, QUATERNION_ES: Brandt / Eichler-order dictionaries collapse
  to B2. Z53_HYPKLOOST: Kuznetsov / Kloosterman-fraction implementations give no saving (scoped theorems).
* What is **not** in the repo (git grep): a trace formula whose *elliptic* side is organised by the (★) geometry itself,
  i.e. in which the (★)-solutions and the class-number terms are two kinds of points of the **same** object. That is the
  angle taken here.

## 1. Precise statements attacked

**(TR-id)** For fixed C ≥ 1 and weight k ≥ 2, find an exact identity
`(elliptic class-number term)(C, n) + (hyperbolic term built from ES_k, TRIV_k)(C, n) + (scalar term) = Tr(T | S_k(Γ_C))`
for an explicit congruence group Γ_C and Hecke operator T, valid for every n ≥ 1 (PROVED, or PROVED relative to a quoted
trace formula + CERTIFIED numerically).
**(TR-pos)** Decide whether any spectral input (Deligne, positivity of T T*, averaging) applied to (TR-id) can force
ES_k(C, p) > 0 for some C at every large prime p (or p ∈ 𝔐), and if not, prove the obstruction as a scoped theorem.

Why not already closed: GROWING_IDENTITIES Prop 2.1–2.2 treat Γ₀(4C) with characters and a generic elliptic side; Prop
2.2's "kq-fold cancellation" is an Assessment, not a theorem; nothing there identifies the elliptic side with the
(★)-geometry or the T1 structure. The closed items of z53_depth.md are not used.

## 2. First lemma — the line dictionary (PROVED, elementary)

**Lemma 1 (line dictionary).** Fix C ≥ 1, n ≥ 1, N = 4Cn + 1. Put
`M_C(n) := {γ ∈ M₂(ℤ) : 4C·det γ − tr γ = n}`, `Δ_C(N) := {Γ ∈ M₂(ℤ) : det Γ = N, Γ ≡ −I (mod 4C)}`.
(i) γ ↦ Γ = 4Cγ − I is a bijection M_C(n) → Δ_C(N), equivariant for SL₂(ℤ)-conjugation (indeed GL₂(ℤ)).
(ii) With s := det γ, w := tr γ the point (s, w) lies on the **line** L_{C,n} : 4Cs − w = n; tr Γ = 4Cw − 2, and
    disc Γ := (tr Γ)² − 4 det Γ = 16C²·(w² − 4s).
(iii) Γ is elliptic ⟺ w² < 4s; parabolic-type (repeated eigenvalue) ⟺ w² = 4s, impossible for odd n; split
    (rational distinct eigenvalues) ⟺ w² − 4s is a positive square.
(iv) Split points of L_{C,n} ↔ ordered integer root pairs (u, B), u ≠ B... more precisely the roots u, B of x² − wx + s
    (s = uB, w = u + B) satisfy 4CuB − u − B = n, and exactly one of: u, B ≥ 1 (an (★)-solution at C ⟺ an ES pair
    (4Cu − 1, 4CB − 1)), or u, B ≤ 0 (writing u = −u′, B = −B′: (4Cu′ + 1)(4CB′ + 1) = N, a TRIV pair; u′ = 0 gives
    the trivial pair (1, N)). Mixed signs are impossible.
(v) (T1 on the line.) If n = m² is an odd square, L_{C,m²} has no split point with u, B ≥ 1, for every C.
(vi) Elliptic SL₂(ℤ)-conjugacy classes in Δ_C(N) with given (s, w) correspond to SL₂(ℤ)-classes of integral binary
    forms of discriminant w² − 4s (all orders), whose weighted number is the Hurwitz class number H(4s − w²).

*Proof.* (i) 4Cγ − I ≡ −I (mod 4C); conversely Γ ≡ −I gives γ := (Γ + I)/(4C) ∈ M₂(ℤ); det(4Cγ − I) = 16C² det γ −
4C tr γ + 1 = 4C(4C det γ − tr γ) + 1. Conjugation commutes with γ ↦ 4Cγ − I. (ii) tr Γ = 4Cw − 2 and
(4Cw − 2)² − 4(4Cn + 1) = 16C²w² − 16Cw − 16Cn = 16C²w² − 16C(w + n) = 16C²w² − 64C²s. (iii) from (ii); w² = 4s with
w = 2r gives n = 4Cr² − 2r even. (iv) Eigenvalues of γ are the roots u, B (integers when w² − 4s is a square, since
w² − 4s ≡ w² (mod 4)); 4CuB − (u + B) = n. If u ≥ 1 > B then (4Cu − 1) > 0 > (4CB − 1) and their product N > 0 is
impossible; similarly u ≤ 0 < B. If u, B ≤ 0 the identity (4Cu − 1)(4CB − 1) = N becomes (4Cu′ + 1)(4CB′ + 1) = N.
(v) T1 (FRONTIER §2; R(m²) = 0 for odd m) applied to (iv). (vi) classical (conjugacy classes of integer matrices with
irreducible characteristic polynomial x² − wx + s ↔ ideal classes of orders containing ℤ[γ] ↔ classes of forms of
discriminant (w² − 4s)/f², f² | w² − 4s; Hurwitz's weighting 1/|Aut⁺/±1|). The equivariant bijection (i) transports
classes. ∎

*Reading.* For fixed C the (★)-solutions are exactly the **positive split points** of the line L_{C,n} in the
(det, tr)-plane of M₂(ℤ); the elliptic points of the same line carry class numbers H(4s − w²); the negative split points
are the TRIV pairs. In Γ-coordinates this is the Hecke set Δ_C(N) for the principal congruence group Γ(4C) (Δ is
Γ(4C)-bi-invariant since Γ(4C) ≡ I). So the natural trace formula is that of the Hecke operator T_Δ on S_k(Γ(4C)), and its
elliptic side is the **line class-number sum**
`E_{C,k}(n) := Σ_{s ≥ 1, w := 4Cs − n, w² < 4s} P_k(4Cw − 2, N)·H(4s − w²)`, P_k(t, N) := (ρ^{k−1} − ρ̄^{k−1})/(ρ − ρ̄),
ρρ̄ = N, ρ + ρ̄ = t.
Size remark (elementary): the elliptic window is |w| < 2√s, s ≈ n/(4C), so it has ≈ √n/(2C^{3/2}) points and is
**empty for most n once C ≫ n^{1/3}** (TODO: exact statement).

## 3. MANDATORY FALSIFIER TABLE (checkpoint-1 version; re-stated at the end)

The object of this lane is an *identity*, valid for every n (prime, composite, square). An identity cannot be falsified by
the screens; what the screens test is any *positivity argument* drawn from it.

| Screen | How the trace identity behaves | What a positivity argument would have to use |
|---|---|---|
| F1 odd squares | Identity holds verbatim with ES_k(C, m²) = 0 for all C (Lemma 1(v)); then Tr = elliptic + scalar(if N square) + TRIV term exactly. | Some input that distinguishes the spectral/elliptic data at n = p from n = m². The elliptic line sum and Hecke traces are not visibly square-sensitive (TODO: test numerically). |
| F2 C-even sub-line | Identity is per C; R₈ = Σ_{C even} R_C. Any argument "some C works" that does not use C odd works verbatim for C even and proves a false statement at threshold 10¹⁰ (12 R₈-zeros). | Must use the odd-C levels Γ(4C), C odd, in an essential way. |
| F3 composites | Identity holds for all n; primality is not used. | Must use primality beyond non-squareness at an identifiable step (none in the trace formula itself). |
| F4 known zeros | At the 14 (★)-zero primes, ES_k(C, p) = 0 for every C, so the identity holds with no ES term at any level. | Any spectral lower bound must fail there (or have a threshold above 8 813 281). |

## 4. Plan / TODO
1. Theorem 2: exact trace identity for T_Δ on S_k(Γ(4C)) (all k ≥ 2), with constants; CERTIFY with pari
   (S_k(Γ(4C)) ≅ ⊕_{χ mod 4C} S_k(Γ₀(16C²), χ)).
2. Positivity analysis: even weight (sign-blind), odd weight, Deligne certificate, empty-window regime C ≫ n^{1/3}.
3. Literature verification (Shimura/Cohen trace formula, Eichler–Zagier Jacobi Eisenstein E_{2,1}, class-number sums in
   progressions).
