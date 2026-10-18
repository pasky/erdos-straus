# QUESTION_R — thin-orbit local–global with a reciprocity obstruction (Rickards–Stange) as a model for ES (O267)

Status: working file (spark relay on O266 SHARP 1). **ES is not solved here or anywhere; no infinite case of ES is claimed.**
Labels as in DISCOVERIES.md. Preprints (Shkredov arXiv:2603.14116, Zhang arXiv:2605.02518) are unrefereed: every use is
CONDITIONAL. Scripts `scripts/z37_*`; memos `BRAINSTORM/z37_*.md`.

Notation (DEDEKIND_ES, ZAREMBA_TRANSFER). n odd, n ≡ 1 (4). A length-3 word w = (t, u, v) ∈ ℤ³_{≥2} with
tuv − u − v = n; A = tu − 1, A* = tv − 1, AA* = tn + 1 =: N_t, n/A = [[v, t, u]]; χ(w) := (A/n) (Jacobi).
N₋(n) := #{w : χ(w) = −1} (= the five-slice count, DEDEKIND Thm 4.5); a₀, a_T as in DEDEKIND §4.4.
RS = Rickards–Stange arXiv:2401.01860v3 (Duke 2025); Ψ = {γ ∈ Γ₁(4)_{≥0} : (a/b) = 1}, Ψ₁ = ⟨R, L⁴⟩,
R = [[1,1],[0,1]], L = [[1,0],[1,1]].

## 0. Iteration log
* cp0: merged O266 (side-agent/zaremba-transfer); read ZAREMBA_TRANSFER, RS (full PDF, §§2–5), DEDEKIND_ES §§1–4,
  THREE_SQUARES / NEAR_SQUARE (clean levels, coin model, open spark S2 = residual near-square gradient on unclean levels).
  Literature search (2024–26 citers of RS): §6.
* cp1 (parent note R276 merged): ZAREMBA §5.2 rows 1, 3, 4 are analogies; row 2 is exact (R276: the slice numerator
  sets satisfy RS Def 2.4). The regular-CF formula r = 1 + Σ_{i odd} a_i is false (only ≤; R276 D2) — not used here.
  Shkredov's M is 2^{2000} (R276 D1).
* Construction log (barrier as steering wheel):
  - I1 "keep the middle window inside Γ" (brief ingredient (i)) → Prop 2.1/§2 item 1: it is *equivalent* to a sign
    condition on the glued residue, so it adds no structure beyond the χ-twist.
  - I2 twisted count via Weil/Salié on gluing boxes → works only for N ≥ n^{3/4} (window 3/8 vs 1/18); via Burgess →
    unavailable (isolated points below N = n^{1/2}).
  - I3 σ-twisted BK circle method: σ is a semigroup character (Thm 1.5) and not cohomologous to a constant on the IFS,
    so the σ-twisted transfer operator has spectral radius < 1 at s = δ (Ruelle–Perron–Frobenius) — this controls
    twisted *averages* (density-one level), but the pointwise reciprocity term lives at denominators q | n (Prop 2.2(iii)).
  - I4 analytic reciprocity series via L(1, χ_{tK+1}) on near-square families → refuted numerically (§3.3).
  - I5 numerator 8 vs 4 → same invariant (§4.1), so reciprocity cannot separate them.

## 1. The exact dictionary (goal 1)

**Prop 1.1 (matrix form; PROVED, elementary).** For n ≥ 2 the map w = (t, u, v) ↦ γ_w = [[A, n], [t, A*]] is a bijection
from length-3 words of n onto {γ = [[a, b], [c, d]] ∈ SL₂(ℤ) : b = n, c ≥ 2, a ≡ d ≡ −1 (mod c), a, d ≥ 2c − 1}.
*Proof.* det γ_w = AA* − tn = 1 (DEDEKIND Lemma 1.1). Conversely a = cu − 1, d = cv − 1 with u, v ≥ 2 and ad − bc = 1 give
b = cuv − u − v. ∎
So ES-five(n) asks for an SL₂(ℤ)_{>0} matrix with upper-right entry n that is **self-levelled**, γ ≡ −[[1, ∗], [0, 1]]
(mod c(γ)) — the congruence modulus is the matrix's own entry c. RS's Ψ ⊆ Γ₁(4) has the *fixed* level 4. This is the
B2 hallmark ("the modulus is part of the solution") in RS's coordinates.

**Prop 1.2 (the per-level sign is a character of conductor | 4t; PROVED).** Let n ≡ 1 (4), w a word of n, A = 2^e·A_o
with A_o odd. Then `χ(w) = (A/n) = (2/n)^e · J(−t, A_o)` (Jacobi symbol with bottom A_o).
*Proof.* (A/n) = (2/n)^e (A_o/n) = (2/n)^e (n/A_o) (reciprocity, n ≡ 1 (4)). For a prime r | A_o, r | tn + 1, so
n ≡ −t̄ (mod r) and (n/r) = (−t̄/r) = (−t/r). Multiply over r^{v} ‖ A_o. ∎
So the RS invariant of the column (A, n) — a Jacobi symbol modulo the *target* n — equals, by reciprocity, a character
modulo 4t of the *divisor* A of N_t = tn + 1, evaluated on the class A ≡ −1 (mod t). RS's proof (Prop 3.2 + Lemma 4.3)
runs reciprocity the other way: their symbol (u/v) on the line ux + vy = n becomes a character modulo the target n of
the line parameter k, summed over ≍ n/(8xy) consecutive k (Pólya–Vinogradov). **Same identity, opposite long side:** in
RS the long side is the target modulus; in ES the long side would be the set of divisors of N_t, which is not an interval.
*Corollary 1.3 (PROVED for A odd by Prop 1.2; all cells checked).* If t ≡ 3 (mod 4), every word of level t is a slice
word: J(−t, A) = (A/t) = (−1/t) = −1 for odd A ≡ −1 (mod t). If 4 | t, likewise (DEDEKIND Thm 4.5). Generally χ(w)
depends only on (t, A, n) mod 8 (`scripts/z37_dictionary.py 20000`: 192 283 words, 0 formula failures, 76 cells, 0
ambiguous; this is DEDEKIND Thm 4.5 re-derived per level).

**Prop 1.4 (T1 for the (A)3 slice as an RS-type sign flip; PROVED).** Let γ = [[a, b], [c, d]] ∈ SL₂(ℤ)_{≥0} with
4 | c, a ≡ d ≡ 3 (mod 4), b ≡ 1 (mod 4). Then (a/b) = −(c/d). If moreover d ≡ −1 (mod c) (self-level), then (c/d) = 1,
so (a/b) = −1 and b is not a square.
*Proof.* (a/b)(d/b) = (ad/b) = ((1 + bc)/b) = 1, so (a/b) = (d/b) = (b/d) (b ≡ 1 (4)); (b/d)(c/d) = ((ad − 1)/d) =
(−1/d) = −1. For d ≡ −1 (mod c), c = 2^s c_o: (c/d) = (2/d)^s (d/c_o)(−1)^{(c_o−1)(d−1)/4} = (2/d)^s (−1/c_o)(−1/c_o) and
d ≡ −1 (mod 8) when s ≥ 3, d ≡ 3 (mod 4) with s = 2 even exponent, so (2/d)^s = 1. ∎ (Numerically: all 480 200 (A)3
words with t, u, v < 200 have (t/A*) = +1, (A/n) = −1.)
Compare RS Lemma 3.1: on Γ₁(4)_{≥0} one has (a/b) = (c/d). The ES (A)3 matrices live in the *other* coset of Γ₁(4) in
Γ₀(4) (a ≡ d ≡ 3), where the same computation gives the opposite sign, and self-levelling pins (c/d) = +1.

**Exactness at RS Def 2.4 (R276, PROVED).** The (A)3 numerator set X_T and the 4 | A numerator set satisfy both clauses
of RS Def 2.4 (every residue class mod m containing a square, here 1 mod m, is hit; no square is hit). The only gap to
RS's setting is that these sets are not semigroup orbits.

**Theorem 1.5 (RS's Kronecker character is the theta multiplier, a homomorphism of the positive semigroup only;
PROVED from the classical theta transformation law).** For γ ∈ Γ₁(4) with c ≥ 0, d > 0 put σ(γ) = (c/d) (Kronecker,
(0/1) = 1). Then σ(γ₁γ₂) = σ(γ₁)σ(γ₂) for γ₁, γ₂ ∈ Γ₁(4)_{≥0}; by RS Lemma 3.1 σ(γ) = (a/b), so Ψ = ker σ. σ is **not**
the restriction of any homomorphism Γ₁(4) → {±1}.
*Proof.* θ(z) = Σ e(m²z) satisfies θ(γz) = (c/d)(cz + d)^{1/2}θ(z) for γ ∈ Γ₁(4) (Shimura 1973, Koblitz IV §4 Prop 4;
ε_d = 1 for d ≡ 1 (4)), principal branch. Applying it to γ₁γ₂ and to γ₁, γ₂ successively gives
(c₃/d₃) = (c₁/d₁)(c₂/d₂)·w, w = (c₁γ₂z + d₁)^{1/2}(c₂z + d₂)^{1/2}/(c₃z + d₃)^{1/2} ∈ {±1}, constant in z. For
non-negative matrices (d_i ≥ 1) let z = iy, y → 0⁺: all three arguments tend to 0, so w = 1. For the second claim:
Γ₁(4) = ⟨T, L⁴⟩ (Γ₀(4) = ±⟨T, L⁴⟩, standard), σ(T) = σ(L⁴) = 1, but [[5, 2], [12, 5]] ∈ Γ₁(4)_{≥0} has σ = (12/5) = −1. ∎
Numerics: 20 000 random products of positive Γ₁(4) words, 0 failures of multiplicativity and of (c/d) = (a/b).
*Reading (Assessment).* RS §10 attribute the failure of their method for groups to "the place at infinity" (Question
10.1). Theorem 1.5 makes this exact: the obstruction to extending σ is the archimedean cocycle w of the metaplectic
(theta) cover, which vanishes on the positive cone. This is the same archimedean role of positivity that the campaign
met for ES ((J)52, (J)55: positivity of d / sign of k is what kills escapes). And the obstructed set — squares — is the
support of θ's Fourier coefficients. I did not find this formulation in RS or its citers (Assessment; folklore-level
classical input).

## 2. Question R: what a proof needs, exactly (goal 2)

Setting: Γ̃ ⊆ Γ₁(4)_{≥0} finitely generated, Zariski dense, Γ̃ ⊄ Ψ; Γ⁺ := Γ̃ ∩ Ψ (a subsemigroup by Thm 1.5, = ker σ|Γ̃);
seed (x, y), y odd, (x/y) = −1. (RS Thm 2.10's Γ'_n = ⟨S_n⟩ ⊆ Ψ is of the form Γ⁺ for Γ̃ = ⟨S_n, g'⟩, g' ∈ Ψ'.)
R(n) = #{γ ∈ Γ̃_X : den γ(x, y) = n}, R⁺(n) likewise for Γ⁺, R_σ(n) = Σ σ(γ) over the same set (X a height cutoff).

**Prop 2.1 (exact reduction; PROVED).** For γ ∈ Γ̃ with γ(x, y) = (a, n): (a/n) = σ(γ)(x/y) = −σ(γ). Hence
`R⁺(n) = (R(n) + R_σ(n))/2`, `R_σ(n) = −Σ_{γ : den = n} (a_γ/n)`, and **n is a Γ⁺-denominator ⟺ some Γ̃-orbit point
with denominator n has a numerator that is a Jacobi non-residue mod n.** At n = m², (a/n) = 1 for all a, so R_σ = −R
and R⁺ = 0 (RS Thm 2.5 for Γ⁺).
*Proof.* RS Prop 2.2 / (3.0.1): γ ∈ Ψ preserves the Kronecker symbol of (x, y), γ ∈ Ψ' flips it (Lemma 3.4); with
σ = ±1 on Ψ/Ψ' this is (a/n) = σ(γ)(x/y). ∎
So Question R, ZQ_M (ZAREMBA §4) and ES-five (DEDEKIND Cor 4.6) are **one problem type: "the structured numerator set
G(n) ⊆ (ℤ/n)^* is not contained in the Jacobi residues"**, with G(n) =

| problem | G(n) | |G(n)| | status |
|---|---|---|---|
| RS Thm 2.6 (Ψ, fat) | numerators on the line ux + vy = n (RS Lemma 4.1) | ≍ n/(8xy), an arithmetic progression | PROVED (PV) |
| ES at L ≍ log p log log p (Thm A) | {A : Σ c_i(A/p) small} | > p/2 | PROVED (pigeonhole) |
| Question R (Γ̃, δ near 1) | numerators of Γ̃(x, y) over n | ≍ n^{2δ−1} (expected), Cantor-type | open |
| ZQ_M (Zaremba, digits ≤ M) | Z_M ∩ Z_M^{−1}-type | ≍ n^{2w_M−1} | EVIDENCE only |
| ES-five | L₃(n) (HJ length 3) | ≍ log² n | EVIDENCE only |

**Prop 2.2 (major arcs and expansion are blind to Question R; PROVED in the stated form).** (i) For every modulus Q
and every non-square class, the congruence data of Γ⁺-denominators do not distinguish n = m² from admissible
non-squares: by RS Def 2.4(1) / Prop 2.12–2.13 (orbits with reciprocity obstruction admit squares mod every Q), any
product of local densities 𝔖(n) = ∏_p σ_p(n) that is positive on admissible classes is positive at admissible m².
(ii) Hence no asymptotic R⁺(n) ~ c·𝔖(n)·n^{2δ−1} can hold at all large admissible n; the true main term must carry a
factor vanishing at squares, which is **not an Euler product** — it is `1 − ∏_p 1[n ∈ ℚ_p^{×2}]` (Hasse principle for
squares), the product of local square indicators subtracted from 1.
(iii) In the twisted count R_σ(n) = −Σ_{a∈G(n)} (a/n), the character has conductor = the squarefree kernel of n
(up to 2): for n = m²k it is (·/k) on units mod m. So in a circle-method/expansion treatment the reciprocity term
lives at denominators q | n of size up to n — the far "minor arcs" — and not on major arcs.
*Proof.* (i) is RS's Def 2.4(1) as verified for Ψ₁-orbits in RS Prop 2.13 (and for ES slice sets by R276). (ii) follows
from (i) and Prop 2.1 (R⁺(m²) = 0). (iii) Jacobi symbol (a/m²k) = (a/k) for gcd(a, m) = 1. ∎

**Heuristic reciprocity singular series for thin orbits (CONJECTURE R-main, Assessment).** For Γ⁺ as above,
`R⁺(n) = (1/2)·c_Γ 𝔖(n) n^{2δ−1}·(1 + ε_n·1[n ∈ □·D] + o(1))`, ε_n = −1 at the obstructed square classes (RS Table 1:
n = m², with the 2-adic variants), where D is the finite set of 2-adic square classes. Reason: for n = m²k with k > 1,
R_σ(n)/R(n) = −(1/R)Σ (a/k) → 0 because Γ̃-numerators over n equidistribute mod k (strong approximation for Γ̃ mod k
plus primitivity), so the twisted count only survives when the character is principal. This is the RS analogue of the
factor (1 − 1_□) that their fat case gets from Pólya–Vinogradov: Σ_{k ≤ K} (ℓ(k)/n_o) = o(K) unless n_o = □.

**What a growth/gluing proof would need (Assessment, precise).** Write G(n) ⊇ A ∩ B^{−1} (Shkredov Cor 16 with Γ̃-prefix
and Γ̃-suffix sets, gluing scale N = n^{2ε}). By Prop 2.1 the full word P·M·S of a glued residue c has
(c/n)·(x/y) = σ(P)σ(M)σ(S) when the cut points are Γ₁(4)-return times, so with P, S ∈ Ψ the middle window decides:
σ(M) = −(c/n). Therefore:
1. *Middle inside Γ (brief's ingredient (i))* is not an extra structural condition but **equivalent to a sign
   condition on the glued residue**: σ(M) = +1 ⟺ (c/n) = −1 (plus the mod-4 return-time condition, a congruence
   condition, and a bounded-gap condition for finite generation).
2. *A main term vanishing at squares (ingredient (ii))* must come from a **twisted gluing count**
   `Σ_{c ∈ A∩B^{−1}} (c/n) = o(|A||B|/n)` for non-square n. Expansion in SL₂(ℤ/n) (Shk Lemma 14/15, Zhang Thm 3.6) holds
   at n = m² as well (strong approximation for Γ̃ at odd n), so it cannot give this (ZAREMBA §4 item 2; R276).
3. *Errors.* With A = ∪ intervals of length N, a box I × J contains N²/n solutions of ab ≡ 1: for N < n^{1/2}
   (Shkredov's regime, N < n^{1/9}) the solutions are isolated points and (c/n) on them is not a character sum over
   any interval — Burgess does not apply at any N. For N ≥ n^{1/2} the twisted box count is a Salié-type
   incomplete sum, O(n^{1/2+o(1)}) per box (Weil), nontrivial only for N ≥ n^{3/4+o(1)}, i.e. ε ≥ 3/8, while the
   middle-window step needs ε < 1/18. **The window conflict is therefore 3/8 vs 1/18** (not 1/8 vs 1/18 as in
   ZAREMBA §4, which assumed the character could be summed over gluing intervals).
4. *What would suffice (a precise open input).* "Hypothesis TG(ε₀, κ): for sets A = Λ₁ ∔ [N], B = Λ₂ ∔ [N] ⊆ ℤ/n with
   N = n^{2ε}, ε ≤ ε₀, and non-square n, Σ_{c∈A∩B^{−1}} (c/n) ≪ |A||B|N^{−κ}/n + n^{1−κ}." Under TG(1/18, κ) plus the
   Shkredov/Zhang machinery transported to Γ̃-digit sets (CONDITIONAL on the preprints and on that transport), the
   proof of Question R would go through for δ_Γ̃ > 1 − O(κ) by the same parameter count as ZAREMBA §1.3. TG is false
   for squares (as it must be) and is a χ-twisted Kloosterman-type problem on Cantor sets; I know no result of this
   kind below N = n^{1/2}.

**Distance from a Γ-theorem to ES-five (Assessment).** Even a full proof of Question R (all δ > 1 − κ/8) would be a
theorem about numerator sets of size n^{2δ−1} = n^{1−O(κ)}. ES-five's numerator set has size ≍ log² n (R276 D3: in
BK normalisation it is the critical exponent δ = 1/2 with a log² excess, not "dimension 0"). In the ladder of the table,
Question R sits between RS's fat case (n¹) and ZQ (n^{0.67} at M = 5), all at power size; ES-five is
at the B2/B3 floor. The gap n^{1−O(κ)} → log² n is the entire B3 scale gap; the only transferable piece is the shape of
the main term (factor vanishing at squares), which is heuristic for ES (§3).

## 3. A reciprocity singular series for the five-slice count (goal 3)

**3.1 Definition.** By Prop 1.2 the slice words of level t are the divisors d of N_t = tn + 1 in the range
[2t − 1, N_t/(2t − 1)] with d ≡ −1 (mod t) and (d/n) = −1, and (d/n) = (2/n)^e J(−t, d_o) is a character mod 4t of d
(d = 2^e d_o). Two main terms:
* *naive (congruence) model* M₀(n) = Σ_t Σ_{d | N_t, range} ρ₀(t, e(d)): every range divisor falls in each odd class
  mod 4t (with its 2-part) with equal probability; ρ₀ = (#bad classes)/(#classes). This is what any product of local
  densities predicts; M₀(m²) > 0.
* *reciprocity model* M_R(n) = Σ_t Σ_{d | N_t, range, (d/n) = −1} ρ_R(t, e(d)), ρ_R = (#bad classes)/(#classes with
  character value −1): divisors are equidistributed **within their character class**. Equivalently, by orthogonality,
  M_R keeps the principal character *and the real character J(−t, ·)* in the expansion of 1[d ≡ −1 (t)], i.e. the
  level-t term is (τ − S_t)/(…) with S_t(N) = Σ_{d | N} χ_t(d) = Π_{r^e‖N}(1 + χ_t(r) + … + χ_t(r)^e) ≥ 0 — for N prime to
  the conductor, the number of ideals of norm N in ℚ(√−t) (Dirichlet; Assessment-level identification). **The reciprocity factor at level t is
  "divisors minus binary-quadratic-form representations"**, and it vanishes exactly at clean levels (S_t = τ).
  M_R(m²) = 0 identically (every level of a square is clean), for the trivial reason (d/m²) = 1.

**3.2 Numerics (EVIDENCE; `scripts/z37_rss.c` (cross-checked against brute force at 1009, 9409, 10009),
`scripts/z37_rss_sets.py`, `scripts/z37_rss_analyse.py`; levels t ≤ 3000; primes in [10⁶, 1.06·10⁶] and near-square
primes m² + K ∈ [4·10⁵, 4·10⁶]).** Ratios of pooled sums:

| set | #n | words/n | N₋/W | N₋/M₀ | N₋/M_R | gap₀ | gap_R |
|---|---|---|---|---|---|---|---|
| generic primes | 2183 | 103.6 | 0.737 | 1.057 | 1.046 | — | — |
| m² + 24 | 76 | 103.5 | 0.568 | 0.790 | 0.891 | 0.25 | 0.15 |
| m² + 16 | 134 | 100.7 | 0.643 | 0.868 | 0.920 | 0.18 | 0.12 |
| m² + 8 | 70 | 90.2 | 0.656 | 0.819 | 0.897 | 0.23 | 0.14 |
| m² + 4 | 131 | 99.1 | 0.700 | 0.889 | 0.956 | 0.16 | 0.09 |
| m² + 1 | 132 | 92.6 | 0.722 | 0.885 | 0.968 | 0.16 | 0.07 |
| m² + 25 | 163 | 98.2 | 0.749 | 1.018 | 0.999 | 0.04 | 0.05 |
| m² − 3 | 133 | 116.3 | 0.673 | 1.120 | 1.070 | −0.06 | −0.02 |
| odd squares (T1) | 684 | 48.7 | 0 | 0 | M_R = 0 | 1 | 0 |

gap = 1 − (N₋/M)/(generic N₋/M). Per-n standard errors of the share ≈ 0.012, so gaps carry ≈ ±0.02–0.03. Readings:
(i) M_R is exact at squares by construction (M₀/W ≈ 1.10 at squares); (ii) at near-squares
m² + K with T1-type levels (K = 1, 4, 8, 16, 24), M_R removes **≈ 35–55 %** of the deficit that the congruence model
leaves; the remaining 7–15 % deficit relative to M_R is significant (≈ 3–7σ per family); (iii) K = 25, −3 show no
deficit beyond noise; (iv) generic primes have N₋/M_R ≈ 1.05: divisors with χ = −1 land in the class −1 (mod t)
slightly more often than equidistribution says.
Same picture at t ≤ 300 (`/tmp` run, all 15 families): N₋/M_R = 1.035 generic, 0.93 (K = 24), 0.95 (16), 0.92 (8),
0.97 (4, 12).

**3.3 An analytic version that failed (EVIDENCE, negative).** Averaging S_t over the family p = m² + K
(N_t = tm² + j, j = tK + 1) heuristically gives E[S_t] ∝ L(1, χ_{−t})L(1, χ_j)/L(1, χ_{−tj}), so the level-t bias
should grow with L(1, χ_j). Test (`scripts/z37_level_L.py K 120`, 80 primes per family): square-j levels have mean
per-divisor bias 0.78–1.00 (clean, as proved); on non-square j the mean bias is −0.04 to −0.08 and its Spearman
correlation with a truncated L_R(1, χ_j) is −0.14 (K = 1), +0.13 (K = 24), +0.04 (K = 16): **no detectable L(1, χ_j)
effect.** So the residual near-square deficit (open spark S2 of NEAR_SQUARE §5) is **not** a t-side divisor-character
effect: given the χ-signature of the divisors of tn + 1, the χ = −1 divisors avoid the admissible class −1 (mod t) more
than equidistribution predicts. This is the admissibility half (B2) again. A natural candidate is the u/v-side
cleanliness of NEAR_SQUARE §5 (K + u = s²), which a one-side model cannot see. (Assessment.)

**3.4 Comparison with RS.** In RS the reciprocity factor is a sharp indicator 1 − 1_□(n) (Prop 2.2, CONJECTURE R-main):
twisted counts with a non-principal character of small conductor equidistribute away. For ES the counts are only
≍ log² n, and the factor is **per level and continuous**: τ(N_t) − S_t(N_t), which is exactly 0 at clean levels and
positive otherwise, so near-squares (where many levels are clean: T1-type tK + 1 = c²) get a partial deficit and
squares a total one. The model explains the deficit only partly; it proves nothing at a single n (the factor is computed
from the factorisations of the N_t themselves).

## 4. Honest assessment (goal 4)

**4.1 Numerator models (PROVED + EVIDENCE, `scripts/z37_numerators.py 20000`).** For k/n the (A)3-type slice is
k·abc − a − b = n, i.e. length-3 words with k | t (k/n = 1/(abc) + 1/(acp) + 1/(bcp)). By Cor 1.3 the sign (A/n) is
constant −1 on {4 | t}, hence on {k | t} whenever 4 | k; for k ≤ 16 and n ≡ 1 (4), n ≤ 2·10⁴, the sign is constant
**exactly for k ∈ {4, 8, 12, 16}** and takes both values for every other k. So **the RS-type invariant does not
distinguish numerator 4 from 8**: the 8-slice is a sub-slice of the 4-slice (t ≡ 0 mod 8 ⊂ t ≡ 0 mod 4) with the same
character and the same square obstruction; what differs is only the size of the slice (a congruence factor 1/2 in the
main term). At p = 241 (an 8-exception, AMPLIFY_EXCEPTION Thm 2.5) neither the 4|t nor the 8|t slice has a word (241 is
in the DEDEKIND §4.4 vanishing list); 215 primes p ≡ 1 (4) below 2·10⁴ have no 8|t word (first: 5, 13, 17, 29, …).
(131 ≡ 3 (4) lies outside the n ≡ 1 (4) setting.) The 4-vs-8 distinction is a B3 (main-term size) question, invisible
to reciprocity — consistent with numerator blindness ((J)41).

**4.2 Barrier screen.**
* B1: everything in §1 is congruence data mod 8 per level (Cor 1.3) or mod 4 for Ψ — no covering content.
* B2: Prop 1.1 is B2 in RS coordinates (self-levelled matrices: modulus = entry c). Prop 2.1 shows that Question R is
  *also* a "structured numerator set vs Jacobi residues" problem, so RS-type thin orbits have their own B2: the sign of
  the glued residue is the sign of the middle window (§2 item 1).
* B3: Question R lives at numerator-set size n^{1−O(κ)}; ES at log² n. No transfer of scale.
* B4/B6: the reciprocity series M_R is computed from the factorisations of the N_t (single n), so B6 does not apply,
  but it is not a lower bound for anything — it is a model of N₋ given the divisor data.
* B5/T1: built in everywhere (M_R(m²) = 0; R⁺(m²) = 0; TG false at squares by design).
* Thm 9.1 / Prop 10.3 (campaign meta-theorems on menu/fixed-structure certificates): not engaged — no certificate menu
  is proposed.

**4.3 Verdict (Assessment).** The connection gives **no lever on B2 at a single p**. What it gives:
1. an exact dictionary: ES words = self-levelled SL₂(ℤ) matrices (Prop 1.1); per-level sign = character mod 4t
   (Prop 1.2); the (A)3 slice is the Γ₀(4)-coset of RS's Ψ with the opposite Kronecker law (Prop 1.4); RS's Kronecker
   character is the theta multiplier, a homomorphism only on the positive semigroup (Thm 1.5), which makes RS §10's
   "place at infinity" precise and matches the campaign's archimedean-positivity theme;
2. an exact reduction of Question R to "some Γ̃-numerator over n is a non-residue" (Prop 2.1), with the precise missing
   input (twisted gluing count, Hypothesis TG) and the precise reason expansion cannot supply it (Prop 2.2: main terms
   that are Euler products cannot vanish at squares; the reciprocity term lives at denominators q | n);
3. a reciprocity singular series for ES (§3) which is exact at squares and explains ≈ 35–55 % of the near-square
   deficit; the rest is an admissibility (B2) correlation, and the natural analytic L(1, χ_{tK+1}) refinement is
   refuted numerically.
No pointwise theorem for any ES relaxation and no theorem in thin orbits (Question R remains open) was obtained.

## 5. Literature checked (2026-10-18; web search + arXiv PDFs in /tmp only)
* Rickards–Stange arXiv:2401.01860v3 (Duke 2025), read in full: §3 (Lemma 3.1, Prop 3.2), §4 (Lemmas 4.1, 4.3), §5,
  §7.3 (Γ'_n = ⟨S_n⟩, δ → 1; Lemma 7.7), §10 (groups; Question 10.1; "the place at infinity").
* Shi–Shi–Whitehead–Williams-Tracy–Zhang, arXiv:2510.21702v2 (2026): reciprocity obstructions for octahedral, cubic,
  square, triangular packings; their §1 suggests "lifting to metaplectic covers … would help to explain reciprocity
  phenomena generally" — Thm 1.5 is an instance of exactly this for RS's Ψ.
* Kadyrov–Kazin–Orynbassar–Shynarbek arXiv:2610.16530 (2026): cites RS; bounded CF in ℚ(√127); not relevant.
* HKRS (Annals 2024); Kontorovich, Bull. AMS 63 (2026) survey "the rise and fall of the local-to-global conjecture";
  K. Stange's research page (reciprocity obstructions as a current programme).
* **No paper found that proves a local–global statement (even density one beyond what BK-type theorems give, or any
  pointwise statement) for a thin orbit carrying a reciprocity obstruction**; Question R appears open and unaddressed.
* Classical: theta transformation law (Shimura, Ann. Math. 97 (1973); Koblitz, GTM 97, Ch. IV §4); Kubota,
  "On automorphic functions and the reciprocity law in a number field" (1969).
