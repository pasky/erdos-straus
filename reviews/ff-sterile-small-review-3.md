# R226 — hostile review of FF_STERILE_SMALL.md §§6–8 (O220 checkpoints 3–4: A = T, k = 1)

Reviewer: R226 (side agent, branch side-agent/review-ff-small-3). Reviewed: side-agent/ff-sterile-small @ 343353a4.
Scope: Prop 6.1 / Cor 6.2, the k = 1 reduction "(Σ) on the q − 3 slices ⟹ no finite covering", Lemma 7.1, Lemma 7.2,
Theorem 7.3 (3 ≤ r ≤ 19), Lemma 7.4 / Theorem 8.1 (r ≥ 20), the q = 9 (k = 1) CERTIFIED statement, the odd-s observation.
§§1–5 are out of scope (R220, R221).
Own scripts (written from the text; none derived from `fz1_*`): `scripts/review_fz1_ff.py` (own F_q/F_q[T] arithmetic, field
axioms asserted), `review_fz1_prop61.py`, `review_fz1_tuples.py`, `review_fz1_enum27.py` (python-flint factoring),
`review_fz1_routecheck.c`, `review_fz1_sum.c`, `review_fz1_tail.c` (k = 1 port of R220's reviewer-written tail),
`review_fz1_caseA.py`, `review_fz1_largeq.py`; logs in `data/fz1_review/`.

## Summary verdicts

| claim | verdict |
|---|---|
| Prop 6.1 (k = 1 depth-1 families only in classes u₀ ∈ {−1, −2}) | **SOUND** (two small proof gaps, m-1) |
| Cor 6.2 + "what changes on these slices" ((B^{k=1}), mass q^{−⌈(s−1)/2⌉}) | **SOUND** |
| Reduction (Σ_{k=1}) on the q − 3 slices ⟹ O(q, T) ≠ ∅ ⟹ no finite linear covering of ES_q(T) | **SOUND** (excluding the slices u₀ ∈ F₃^* is harmless, §2) |
| Lemma 7.1 (k = 1 Case B structure, 19 routes) | **SOUND** (documentation: Lemma 1.4 hypothesis, m-2) |
| Lemma 7.2 (k = 1 Case A, T ∤ K, T ∤ z, route (ix), tail (b)) | **SOUND** |
| Theorem 7.3 (3 ≤ r ≤ 19; ≤ 9.47 at r = 3, ≤ 27.7 at r = 4) | see §5 (filled in below) |
| Lemma 7.4 / Theorem 8.1 (r ≥ 20, K(3^20) ≤ 4.19·10⁸) | see §6 |
| q = 9, k = 1 CERTIFIED negative statement about the method | see §7 |
| odd-s / odd-r absence (EVIDENCE) | see §7 |

## 1. Prop 6.1 and Cor 6.2

**Re-derivation.** For k = 1, N = k + j − 1 = j, so the cylinder u ≡ −E (mod T^{N+1}) has depth 1 iff j = v_T(L) = 0.
*Case B, j = 0* (so γ = 0, s = 1): E = L'w − 1, E' = L'C − 1, EE' = 1 + TL'g' gives m'wC = T + v, w + C = g'v (pure
algebra). If E = 1 or E' = 1 then u₀ = −1 directly (E' ≡ −u^{−1}). Otherwise E, E' are monic of positive degree, so w, C are
monic and w + C ≠ 0 (q odd). Degree count: deg(w + C) = max(a, b), so y + deg v = max(a, b); if z + a + b ≥ 2 and
z + min(a, b) ≥ 1 then deg v = z + a + b > max(a, b), contradiction. **The case z = 0, min(a, b) = 0, max(a, b) ≥ 2 is not
covered by the document's inequality** (there z + a + b = max(a, b)); it is impossible for a different reason: with C = 1,
m' = 1, w = T + v, deg v = a forces g' = 1 and then T + v + 1 = v (m-1). The remaining cases z + a + b ≤ 1 give exactly the three
listed tuples (re-derived; in characteristic 3, T² + 3T + 1 = T² + 1). All have E(0) = 1, u₀ = −1.
*Case A, j = 0:* E | a1 + b1, a1b1 | E + 1, T ∤ a1b1. Nonconstant E forces b1 = 1 (say), deg E = deg a1, E + 1 = lc(E)·a1, and
E | a1 + 1 ⟺ E | 1 + lc(E). The document's lc argument is right and necessary: lc(s) ∈ {1, lc(a0 + b0), lc(L/a0 + L/b0)} and
here deg a0 > deg b0 and L/a0 + L/b0 = 1 + a1, so lc(s) = 1, E monic, E | 2: impossible. (With lc(E) = −1 the family would
exist in every odd characteristic, not only in char 3 as the remark says — harmless.) Constant E = lc(s) ∈ {1, 2}.

**Brute force from the definition** (`review_fz1_prop61.py`): every (E; t_a, a0; t_b, b0) with T ∤ a0b0 (j = 0), all 16 type
pairs, E of every leading coefficient with deg E ≤ dE and L | E + 1 (necessary), validity tested on a concrete monic P of
large degree with P ≡ 1 mod E·L and P(0) = −E(0) (= x_u mod W_F, FUNCTIONFIELD_ES Lemma 6.2) by the definition
(A·a0, A·b0 | P + E, s ≠ 0, E | s, lc(s) = lc(E)). q = 3 (deg a0, b0 ≤ 2, deg E ≤ 4), q = 5 (2, 3), q = 7 (1, 4), q = 9 (1, 3):
**no valid j = 0 family outside u₀ ∈ {−1, −2}**; all valid families with nonconstant E lie on u₀ = −1, as stated
(`data/fz1_review/prop61.txt`). In particular no lc(E) = 2 family appears at q = 9 (the char-3 subtlety is handled correctly).

**Cor 6.2 / (B^{k=1}).** {−1, −2} = F₃^* for q = 3^r. On u₀ ∉ F₃^* (in particular u₀ ≠ 1): L'(0)w(0) = 1 − u₀ ≠ 0,
L'(0)C(0) = 1 − u₀^{−1} ≠ 0, v ≡ m'wC (mod T) (s ≥ 1), so T ∤ m'g'wCv. s = N + 1 + γ with 0 ≤ γ ≤ j = N and N ≥ 1 (no depth-1
families), so s ≥ 2 and the union over the admissible N of the nested cylinders u ≡ −E (mod T^{N+1}) has relative mass
q^{−⌈(s−1)/2⌉}. Also on these slices E ≠ 1 and E' ≠ 1 (they would give u₀ = −1), so w, C are monic. SOUND.

## 2. The reduction for k = 1 (the excluded slices)

The conclusion is still "no finite linear covering of ES_q(T)". FUNCTIONFIELD_ES2 §0.1 (stated for general A) says a finite
covering exists iff O(q, A) = ∅; one point of O anywhere suffices for non-existence (Dirichlet in F_q[T]: the unit class mod W
of that point contains irreducible P of every large degree, and no family of the finite covering is valid there). The slices
u₀ ∈ F₃^* are simply not used. The union bound is correctly set up: every Case B tuple and every Case A datum has its maximal
cylinder in exactly one slice (u₀ = −E(0)); the left side of (Σ_{k=1}) counts all tuples/data with T ∤ m'g'wCv (resp. T ∤ K),
which includes every family meeting a slice u₀ ∉ F₃^* (Prop 6.1 ⟹ none of depth 1 there), so the summed covered relative
measure of the q − 3 slices is ≤ the left side, and if that is < q − 3 some slice has positive uncovered measure, hence a point
of O(q, T). The counts include tuples on the slices u₀ ∈ F₃^* ∖ {1} as well (overcount; harmless). SOUND.

## 3. Lemma 7.1 (k = 1 Case B)

**Re-derivation.** (i) As in the document; the "z + a + b > s" branch: deg(g'v) = y + z + a + b ≤ max(a, b) forces z = y = 0,
min(a, b) = 0, then with C = 1: w = wC = T^s + v = T^s + w + 1, impossible; the "<" branch is the standard one. y + t = max(a, b)
since lc(w + C) ∈ {1, 2} ≠ 0. Identities: Ev = (w + C)m'w − v = m'w² + T^s; EC = g'(T^s + v) − C = g'T^s + w;
EE' = L'(L'wC − g'v) + 1 = 1 + T^s L'g'. (ii) all congruences re-derived; gcd(w, v) | T^s and T ∤ v, so w is a unit mod v.
(iii) Route by route (read against the code of `fz1_sum.c`): T0, R4', X1, X2 (loss-free reconstructions), R1 (ordered
factorisations of T^s + v, multinomial or two-step Lemma 4.1), R2 (n, d, ρ) = (s + 2y + z, a + y + z, y + z) cofactor allowed
(1 + T^s m'g'² ≡ 1 mod L'), R3 (s + y, a + y + z, a + y) E-only, R4 (s, a + y + z, z + a) cofactor (deg T^s + m'w² = s because
a ≤ b), R3C/R4C, R5a/b, R6a/b, R8a/b, R9a, R10a (classes: w² ≡ −wC mod v, ≤ 2^{ω(v)} square roots — correctly *without* the
factor 2 for T that the k ≥ 2 code has), R10b (Σ_v 2^{ω(v)} = q^t(2 + (t − 1)(1 − 1/q))), the τ-bound inside logSomClass
(re-derived: δ | v, deg δ ≤ t/2, δ coprime to m', v in one class mod m'δ). All 19 are correct k = 1 transcriptions. Every
class route applies Lemma 1.4 (T-adic refinement) with a T-free modulus: valid because every counted divisor divides a T-free F
(so is prime to T) and every F used with the cofactor version is prime to T and to Q (m-2: the statement of Lemma 1.4 in §1 is
written for T | Q; the k = 1 use relies on the R220-repaired hypothesis — say so in Lemma 7.1(iii)).

**Brute force.** `review_fz1_tuples.py` enumerates all monic T-free (m', g', w) with z + a + y ≤ D, sets E = m'g'w − 1 and
tests every s ≤ SMAX for C = (g'T^s + w)/E, accepting only tuples that satisfy the definition; it does not assume
deg(m'wC) = s, and asserts every claim of Lemma 7.1(i)–(ii) on every tuple found (727 tuples at q = 3, 400 at q = 5, 286 at
q = 7, 656 at q = 9: **0 failures**). Per-pattern counts (complete for patterns a ≤ b, s ≤ D: q = 3 s ≤ 11, q = 5 s ≤ 7,
q = 7 s ≤ 6, q = 9 s ≤ 6, total and slice-filtered) agree **exactly** with the author's `fz1_enum` (1028 + 249 + 159 + 159
patterns, plus the filtered q = 9 run: 0 mismatches). Every one of the 19 author routes separately vs these counts
(`review_fz1_routecheck.c`, linking the author's `pattern_bound1`): **0 violations**, most routes attain ratio 1.000.
SOUND.

## 4. Lemma 7.2 (k = 1 Case A)

**Re-derivation.** (a) If T ∤ a1b1 (any γ), Prop 6.1's Case A argument applies verbatim (it only uses E | a1 + b1,
a1b1 | E + 1, T ∤ a1b1 and lc(s)), so E is constant and u₀ ∈ F₃^*. T ∤ K: E(0) + 1 = 1 − u₀ ≠ 0. EF = T^α a1' + b1 gives
F(0)E(0) = b1(0) ≠ 0, so T ∤ F; (A3) gives z ≡ b1KF ≢ 0 (mod T). β > α + λ forces λ = κ = f = 0 and then (A4)
b1(KF − 1) = T^α + F, impossible by degrees. (A4) needs a1'KF ≠ 1, true since a1'KF = 1 would give T^α a1' + F = 0. Route (ix):
multiplying (A4) by a1'K gives (E + 1)(a1'KF − 1) = T^α a1'²K + a1'KF, i.e. **E(a1'KF − 1) = 1 + T^α a1'²K**. γ = 0 is the
maximal cylinder (mass q^{−α}), and only (E, α) determine the cylinder. lc(E) = lc(K) (E + 1 = a1'b1K) ∈ {1, 2}.
Routes of `fz1_caseA.py`: (i) 2N(λ)N(β)N(κ); (ii) 4N(λ)N(κ)N(f) (lc K, lc F); (iii) E | T^α + b1²K (= zE), ≡ −1 mod b1K, the
factor 4 contains a redundant 2 (lc(E) = lc(K) is fixed once K is) — conservative; (iv) E | T^α a1' + b1, ≡ −1 mod a1'b1, lc(E)
unknown: the factor 2 is needed (see below); (v) z ((q − 1)q^ζ choices), then an ordered factorisation of T^α + z
(≤ 2·multinomial; ordered monic factorisations with prescribed degrees ≤ multinomial by the labelled-roots argument);
(vi) quadratic for (b1, F). All valid. (b) min((i), (ii)) ≤ 4q^{α−ζ}, (v) ≤ 2q^{ζ+1}3^α, geometric mean √8·q^{(α+1)/2}3^{α/2};
patterns ≤ (α + 1)³; tail ratio ((α + 2)/(α + 1))³(3/q)^{1/2}. SOUND.

**Brute force** (`review_fz1_caseA.py enum`, own enumeration of (a1', b1, K) over a box larger than the claimed pattern range,
λ up to α + 1, β up to α + λ + 1): strict mode (lc(E) ∈ {1, lc(a1 + b1)}, u₀ ∉ {−1, −2}): q = 5 (α ≤ 3) 7 data, q = 7 (α ≤ 2)
0, q = 9 (α ≤ 2) 14, q = 3 0; loose mode (only T ∤ K, lc(E) ∈ {1, 2}): q = 5: 69, q = 7: 18, q = 9: 35, q = 3: 75 data.
Every claim of 7.2(a) (z ≠ 0, T ∤ z, f ≥ 0, λ ≤ max(f, β), deg z ≤ ζ, route (ix), (A2)–(A4), lc(E) = lc(K), no pattern with
β > α + λ) holds on every datum; the six author routes and R226's four routes: 0 violations; route (iv) is attained (ratio
1.000 in loose mode), confirming that the lc(E) factor 2 the author added there is necessary.

(work in progress: §5 Theorem 7.3, §6 Lemma 7.4, §7 q = 9 / odd s, defects list)
