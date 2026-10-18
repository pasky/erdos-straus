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
