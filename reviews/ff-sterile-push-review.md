# R217 — hostile review #1 of O216 FF_STERILE_PUSH.md

Reviewer: R217 (side agent, branch side-agent/review-ff-push). Document reviewed at merge of side-agent/ff-sterile-push
(commit as merged at review start). From-scratch scripts: `scripts/review_fs_*`.

Status: IN PROGRESS (written claim by claim).

## Summary verdicts
(filled in at the end)

## Claim-by-claim

### Lemma 1.1 (E·v = T^s + m′w², y + t = max(a, b), T² ∥ v) — SOUND
Re-derived: (R3) of DEPTH_ASPECT Lemma 2.1 is C·E = g′T^s + w; times m′w and m′wC = T^s + v gives
(T^s + v)E = (E + 1)T^s + m′w², i.e. Ev = T^s + m′w². Degrees: z + 2a ≤ z + a + b = s, with equality iff a = b, and then
the sum of two monic degree-s polynomials has leading coefficient 2 ≠ 0 (q odd). deg E = deg(L′w) = a + y + z, so
t = s − a − y − z = b − y. (iii): v_T(m′wC) = 2 < s forces v_T(v) = 2 exactly; a common prime of w₁ and v₁ divides
T^{s−2}. All correct; note (ii) uses q odd (H2), which §4 correctly lists.
From scratch: `scripts/review_fs_tuples.py` enumerates all tuples (B) by (m′, g′, w) ↦ C = (g′T^s + w)/E, re-checks (B)
literally and asserts Ev = T^s + m′w², y + t = max(a, b), T² ∥ v on every tuple (q = 3, s ≤ 13; q = 5, s ≤ 9): 0 failures
(see log in the "Numerics" section below).

### Lemma 1.2 (loss-free reconstructions T0, R4′, X1, X2) — SOUND
Each reconstruction re-derived (X1: w, C are the two roots of X² − g′vX + (T^s + v)/m′, so ≤ 2 ordered pairs).
Counts: N*(d) = q^d − q^{d−1} is the number of monic f of degree d ≥ 1 with T ∤ f; for v = T²v₁ the leading coefficient
is fixed per pattern (1 if a < b, 2 if a = b) and v₁(0) ≠ 0, which gives the same count N*(t − 2). Correct.

### Lemma 1.3 (C(n, d), multinomial) — SOUND
Standard (sub-multisets of the root multiset in F̄_q).

### Lemma 1.4 (FF Lenstra: 3ρ > n ⇒ ≤ 2 divisors of degree d in a unit class mod Q) — SOUND
Re-derived line by line. Points I checked specifically: (1) τ₀ is well defined even if gcd(F, Q) ≠ 1, because
σ₀e ≡ F (mod Q) with σ₀ a unit determines e mod Q — the document's wording ("when such τ₀ exists … τ₀ := e mod Q") is
correct but would read better as "τ₀ ≡ Fσ₀^{−1}"; (2) Λ-determinant: σ₀(u_x u′_y − u_y u′_x) ≡ 0 and deg ≤ X + Y = n − 2ρ < ρ,
so all differences are F_q(T)-collinear, hence multiples of one primitive b ∈ F_q[T]² (F_q[T] is a PID); (3) φ(α) =
α·(αb_xb_yQ + b_xτ₀ + b_yσ₀ + Q(x₀b_y + y₀b_x)) — constant term 0, so if b_xb_y ≠ 0 the second root is unique (|S| ≤ 2), and if
b_y = 0 the linear coefficient is b_x e₀ ≠ 0 (|S| = 1); b_x = 0 is impossible as stated (m8 repair is correct).
Nothing hidden: no hypothesis gcd(F, Q) = 1 is needed, and "monic or not" is harmless (λE ≡ λσ ≢ σ for λ ≠ 1).
From scratch: `scripts/review_fs_lenstra_bf.py` (own polynomial arithmetic; divisors from a known factorisation, all scalar
multiples included; every monic Q with deg Q ≤ 5 (p = 3) / ≤ 3 (p = 5); random highly-factorable F with n ≤ 14 (p = 3),
n ≤ 12 (p = 5) plus F = ∏ of all monic irreducibles of degree ≤ 2 and variants with repeated linear factors):
p = 3: 848 429 + 565 594 (degree, Q) groups; p = 5: 246 073 + 127 398 groups; **0 violations** of "≤ 1 if d < ρ or n − d < ρ"
and "≤ 2 if 3ρ > n"; the bound 2 is attained thousands of times (so it is sharp).

### Lemma 1.5 (FF Coppersmith–Howgrave-Graham by pigeonhole) — SOUND
Re-derived: (a) |F_q[T]^N/Λ| = q^{deg det Λ} and q^{N(μ+1)} > q^Δ for μ = ⌊Δ/N⌋ — exact Siegel lemma, no loss. (b) E prime to
Q, hence E | F₁; Q·f(x₀) ≡ Qx₀ + σ₀ = E ≡ 0 (mod E) and gcd(E, Q) = 1 give E | f(x₀); the scaled coefficient lattice of
{f^iF₁^{m−i}} ∪ {x^jf^m} is triangular with diagonal degrees (m − i)deg F₁ + iX, (m + j)X, so deg det ≤ Δ(m, k);
⌊Δ/N⌋ < md ⇔ Δ < N·md, which is (C); then deg P(x₀) < md = deg E^m forces P(x₀) = 0, and P ≠ 0 has ≤ m + k roots.
Asymptotics: (C)/m² → n/(2u) + Xu/2 < d with u = 1 + τ, optimum u = √(n/X) ≥ 1, i.e. nX < d² ⇔ ρ > d(n − d)/n. Correct.
Note: the proof needs deg x₀ ≤ X, i.e. ρ ≤ d; for d < ρ the count is ≤ 1 anyway, so using m + k ≥ 1 there is harmless
(both scripts rely on this; fine).
From scratch (same script): in every group with 3ρ ≤ n (Lenstra not applicable), d ≥ ρ, n − d ≥ ρ, the least m + k over
m ≤ 12, k ≤ 40 satisfying (C) was compared with the true maximal class size: 0 violations; the Coppersmith bound is
attained with value 3 (p = 3: 6 groups; p = 5: 75 groups), so the test reaches the regime beyond Lenstra.

### Lemma 1.6 (19-route table) — SOUND
Every row re-derived (n, d, ρ, coprimality):
* R2: E | D = 1 + T^s m′g′² (= EE′), deg D = s + 2y + z, E + 1 = L′Tw₁ so E ≡ −1 (mod TL′), ρ = 1 + y + z; D ≡ 1 (mod TL′), so the
  cofactor version is legitimate. R3: E | T(g′T^{s−1} + w₁) and E(0) = −1 ⇒ E | g′T^{s−1} + w₁; ρ = deg(Tw₁g′) = a + y; E-version
  only (correct: gcd(g′, w₁) can be ≠ 1). R4: Ev₁ = T^{s−2} + m′w₁² (Lemma 1.1(i)/T²), degree exactly s − 2 (lc 2 if a = b),
  prime to Tm′w₁. R3C/R4C: n = z + 2b − 2 for R4C is right (z + 2b ≥ s since b ≥ a; lc 2 when a = b).
* R5a/b, R6a/b: C₁ | (T^{s−2} + v₁)/w₁ = m′C₁, C₁ ≡ −w₁ (mod Tv₁) a unit by Lemma 1.1(iii); cofactor m′ (or w₁) prime to Tv₁. R8, R9: fine.
* R10: w₁C₁ = G₂ and C₁ ≡ −w₁ give w₁² ≡ −G₂ (mod Tv₁), G₂ a unit; in odd characteristic x² ≡ y² (mod P^e) with x, y units
  forces P^e | x − y or P^e | x + y (P cannot divide both), so ≤ 2 roots per prime power and ≤ 2^{ω(Tv₁)} = 2·2^{ω(v₁)} classes.
  Σ_{deg v = e, monic} 2^{ω(v)} = Σ_{d sqfree, deg d ≤ e} q^{e−deg d} = q^e(2 + (e − 1)(1 − 1/q)) (e ≥ 1) re-derived; v₁ with the
  fixed leading coefficient 2 is a scalar multiple of a monic one, so the monic sum is the right majorant. e = 0 gives 1 (both
  codes handle it).
* All divisors counted by C(n, d) are monic (E = L′w − 1, E′, w₁, C₁, m′ monic), as Lemma 1.3 requires.
From scratch: (1) `scripts/review_fs_tuples.py` gives exact pattern counts for q = 3 (s ≤ 13) and q = 5 (s ≤ 9); every count
is ≤ the minimum of my own implementation of the table (`scripts/review_fs_exact.py`) — see Numerics. (2) My C implementation
(`scripts/review_fs_fin.c`) and the author's `fs_sum.c` agree on every pattern up to the Coppersmith search range: the author
caps m ≤ 60, k ≤ 200; I search j = m + k ≤ 3000 exactly (convex in m) with the necessary condition nX < d² (proved by AM–GM:
n m(m+1) + X j(j+1) ≥ 2√(nX)·m(j+1) for m ≤ j) as prefilter. On all patterns s ≤ 70 (r = 4) and s ≤ 50 (r = 5, 6) my
bound is ≤ the author's, never larger (harness `/tmp/r217_cmp.c`, reproducible from the two sources), so the author's
values are never *below* what the lemmas give. Remark: the rewriting Δ(m, k) = [n·m(m+1) + X·j(j+1)]/2 with j = m + k
(since m(m+1) + 2km + k(k+1) = j(j+1)) simplifies (C) and shows the bound depends on m and j only.

### Lemma 2.1 (averaging over c, factor q − 1) — SOUND
Each Case B tuple has the single largest cylinder u ≡ −E (mod T^{N(s)+1}) (from γ ≤ j: s = k + j + γ ≤ k + 2j gives
N = k + j − 1 ≥ ⌈(s + k − 2)/2⌉, so every (N, γ)-cylinder of the tuple lies in that one — O173 Lemma 3.1 is not needed, as
R178 noted), and each Case A datum the cylinder u ≡ −E (mod T^{k+α}); N(s) ≥ 1 and k + α ≥ 2 fix u mod T², i.e. c = the
T-coefficient of −E. Hence Σ_c covered(c) ≤ left side of (Σ), and #{c : covered(c) ≥ θ} ≤ (left side)/θ. Correct, and it is
genuinely a new (if simple) gain over Thm 2.5. The tuple sets do not depend on k and the masses decrease in k, so k = 2 is
the worst case (checked against DEPTH_ASPECT §2.1/§2.2).
Arithmetic of (a): 2.176/(1/2) = 4.35, so ≤ 4 slices have covered mass ≥ 1/2 and ≥ 76 (the document says 75 — conservative,
fine) have more than half of their measure in O.

### Lemma 2.2 (Case A routes; α ≤ 2 empty) — SOUND
Normalisation checked against FUNCTIONFIELD_ES2 §0.2 (a0, b0 monic, so a1′, b1 monic) and DEPTH_ASPECT Lemma 2.4 (α > β
⇒ E, F, K monic). Six routes re-derived from (A0)–(A4): (iii) E | T^α + b1²K of degree max(α, 2β + κ) (lc 2 if equal),
E ≡ −1 (mod b1K); (iv) E | T^α a1′ + b1, E ≡ −1 (mod Ta1′b1); (v) z (T | z, 1 ≤ deg z ≤ ζ: ≤ q^ζ) then ordered monic
(b1, K, F) of T^α + z, degrees summing to α; (vi) b1 + F = a1′z, b1F = (T^α + z)/K, ≤ 2. Dropping g′ is right: the
cylinder depends only on (E, α). The α = 1, 2 argument re-done by hand (both surviving shapes force μ = 1 and μ + 1 = 0).
The certification does not even use it (fs_caseA.py sums from α = 1). From scratch: `scripts/review_fs_caseA.py`
reproduces the author's exact Case A sums to all 11 printed digits (r = 4: 8.4882704620e−4; r = 5: 8.7646411455e−5;
r = 6: 9.5155829299e−6); its α > 40 majorant uses q^{⌊(α−1)/2⌋−α} ≤ q^{−(α+1)/2} with an exact-rational ratio bound.
The author's tail (6.28·10⁻² at r = 4) is valid but a factor √q = 9 looser than necessary (it uses q^{−α/2}); this tail is
in fact the *largest* part of the r = 4 Case A total (6.36·10⁻²) — harmless.

