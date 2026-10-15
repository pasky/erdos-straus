# R226 — hostile review of FF_STERILE_SMALL.md §§6–8 (O220 checkpoints 3–4: A = T, k = 1)

Reviewer: R226 (side agent, branch side-agent/review-ff-small-3). Reviewed: side-agent/ff-sterile-small @ 343353a4.
**Repairs applied** (author quiet): m-1..m-6 applied to FF_STERILE_SMALL.md §§6–8 in place, marked "(R226 repair)", plus a
status-line pointer to this review; scripts of the author untouched (m-5 documented only); m-7 concerns the report only.
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
| Theorem 7.3 (3 ≤ r ≤ 19; ≤ 9.47 at r = 3, ≤ 27.7 at r = 4) | **SOUND** (independently re-certified for every 3 ≤ r ≤ 19 with R226 code and R226's own exact q = 27 enumeration: r = 3 ≤ 18.03 < 24, r = 4 ≤ 31.89 < 78; stale scope text m-3) |
| Lemma 7.4 / Theorem 8.1 (r ≥ 20, K(3^20) ≤ 4.19·10⁸) | **SOUND** (monotonicity re-derived term by term; K(3^20) ≤ 4.19188·10⁸ re-evaluated in exact rationals; orientation unstated, m-4) |
| q = 9, k = 1 CERTIFIED negative statement about the method | **SOUND** (53.0 reproduced; exact inputs not archived, m-6; R226 exact s ≤ 14: 3.92790) |
| odd-s / odd-r absence (EVIDENCE) | **SOUND as EVIDENCE** (confirmed: q = 9 odd s ≤ 15, q = 27 s ≤ 12) |

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

**Definition-level check of the k = 1 cylinder** (`review_fz1_validity.py`, q = 9, s ≤ 6, every tuple with E(0) ∉ F₃ and every
split s = j + 1 + γ, 0 ≤ γ ≤ j): the family (E; 0, T^γ g'; 2, T^j L') is valid at a concrete P ≡ x_u (mod W_F) for
u ≡ −E (mod T^{j+1}) and invalid for all q − 1 perturbations u + cT^j (3924 tests, 436 valid, 0 mismatches). So Lemma 1.1 of
FUNCTIONFIELD_ES3 (written in a k ≥ 2 setting) does apply verbatim for k = 1, as §6 asserts.

## 5. Theorem 7.3 (3 ≤ r ≤ 19)

**Audit of `fz1_certify.sh`.** `set -euo pipefail`; each component is parsed and checked finite and ≥ 0, the final comparison
exits 1 on failure and runs inside a pipeline with pipefail: fails closed. `fz1_tail` exits 1 if any box fails. `fz1_sum`
refuses an exact-count file whose line count differs from the number of patterns, and a "SKIP" line falls back to the route
bound (conservative). The q = 27 exact files (`data/fz/enum1_27/e_2..12`) have 0 SKIP lines and all counts 0; `caseA.txt`
(α ≤ 4) is complete (`fz1_caseA.py` checks completeness per level) and all 0. Rounding: long-double logs with a final ×1.01;
Case A in exact rationals. The lc(E) = 2 factor: present in route (iii) (×4, of which ×2 is redundant since lc(E) = lc(K) is
fixed by K — conservative) and in route (iv) (×2, needed: attained by R226's loose-mode brute force, §4). The log
`data/fz/certify_k1.txt` matches the theorem's constants (9.4678, 27.634, 15.497, 11.103, ≤ 9.741 for 7 ≤ r ≤ 19).
**Trust point.** At r = 3 the theorem rests on the exact enumeration: the route bounds alone give Case B ≈ 71.7 > 24 (62.4 of
it from s ≤ 12; `fz1_sum 3 80 -`), so "no filtered tuple for s ≤ 12 at q = 27" is load-bearing.

**Independent re-certification (`review_fz1_certify.sh 3 19`, log `data/fz1_review/certify.txt`, R226 code only).**
* *Exact q = 27 counts* (`review_fz1_enum27.py`, FLINT factorisation; sweeps V (all v with t ≤ t₀, lc(v) ∈ {1, 2}: factor
  T^s + v, all ordered (w, C)), R2, R3, R4 (all data with the pair-degree ≤ D = ⌊2(s − t₀ − 1)/3⌋: factor the target polynomial,
  run over its divisors in the class −1); completeness by t = s − (a + y + z) for a ≤ b; every tuple verified against the
  definition). Validated against the naive enumerator (q = 3 s ≤ 9, q = 5 s ≤ 7, q = 7 s ≤ 6, q = 9 s ≤ 6, total and filtered;
  every s with three different t₀): 0 mismatches. **q = 27, 2 ≤ s ≤ 12: 0 tuples with E(0) ∉ F₃** (unfiltered a ≤ b counts
  2, 12, 2, 33, 16, 107, 38, 130, 73, 235, 116; s ≤ 7 total 172, as the document says); 1.9·10⁷ factorisations, ≈ 35 min.
  CONFIRMED.
* *Case B bounds* (`review_fz1_sum.c`, 20 routes re-derived in §3: T0, R4', X1, X2, X2C, W1 (C fixes v; w ≡ −C mod v), R1,
  R2, R3, R4, R3C, R4C, R5a/b, R6a/b, R8a, R9a, R10a/b; own Lenstra/Coppersmith class counts with the Lemma 1.4 lift; own
  divisor bounds: binomial, exact max-τ / max-τ₃ by a knapsack DP, own Rankin DP). Per-route check vs exact counts: 0
  violations. Finite part (s ≤ 80): r = 3: 71.748 bound-only (author 71.708), with R226 exact s ≤ 12 → **9.3463**; r = 4:
  **24.841** (author 24.812).
* *Tail s > 80* (`review_fz1_tail.c`, k = 1 port of R220's box code: zero integer shifts, weight q^{1/2 − s/2}): r = 3 ≤ 2.0·10⁻⁵,
  r = 4 ≤ 1.8·10⁻⁶.
* *Case A* (`review_fz1_caseA.py mass`, routes (i), (ii), (v), (vi) only, no exact data, + Lemma 7.2(b) tail): r = 3 ≤ 8.505,
  r = 4 ≤ 6.733 (weaker than the author's 3.85 / 2.55 without exact data; not needed).
* **Totals ×1.01: r = 3: 18.03 < 24; r = 4: 31.89 < 78; r = 5: 19.62 < 240; r = 6: 15.16 < 726; 7 ≤ r ≤ 19: ≤ 13.79.**
  Theorem 7.3 is independently re-certified for every 3 ≤ r ≤ 19 (with a different route set, different divisor bounds, a
  different exact enumerator and a different tail). **SOUND.**

## 6. Lemma 7.4 / Theorem 8.1 (r ≥ 20)

**Re-derivation.** Orientation a ≤ b (w ↔ C, E ↔ E' symmetry; for a > b the C-routes) — needed for t = s − σ (y + t = b) and
for deg(T^s + m'w²) = s (z + 2a ≤ s); the proof uses both without saying so (m-4). R1: v (≤ q^t: fixed lc), then ordered
triple factorisation of the monic degree-s polynomial T^s + v (≤ τ₃ ≤ 3^s). R2: (m', g') ≤ q^{y+z}, E | 1 + T^s m'g'², degree
s + z + 2y ≤ 3s (y ≤ b = s − a − z), ≤ 2^{3s}; then w = (E + 1)/L', C = (E' + 1)/L'. R3: (w, g'), E | g'T^s + w (degree s + y ≤ 2s),
then C = (g'T^s + w)/E, m' = (E + 1)/(g'w). R4: (m', w), E | T^s + m'w² (degree s), g' = (E + 1)/(m'w), v = (T^s + m'w²)/E.
All monic divisor counts ≤ 2^{deg}. min(t, y + z, a + y, a + z) ≤ min(s − σ, 2σ/3) ≤ 2s/5, integer ⇒ ≤ ⌊2s/5⌋; patterns
(a, z, y) ∈ [0, s]³ (the extra factor 2 is a harmless overcount). Weight q^{−⌈(s−1)/2⌉}. e(s) ≤ 1/2 − s/10 and e(s) ≤ 0 for
s ≥ 2 (checked to 10⁵; general by the inequality). Case A: Lemma 7.2(b) × q^{−α}, exponent (1 − α)/2 ≤ 0. So every term of K is
nonincreasing in q, and for q = 3^r ≥ 3^20, left side of (Σ_{k=1}) ≤ K(q) ≤ K(3^20) < 3^20 − 3 ≤ q − 3. (K(3^r) = ∞ for r ≤ 18,
since 8 ≥ q^{1/10}; r = 20 is the first r where K alone suffices.) **SOUND.**
**Evaluation** (`review_fz1_largeq.py`, exact rationals with q^{1/2} = 3^10, q^{1/10} = 9 exact; √8, √3 replaced by squared-checked
rational upper bounds; tails as exact rational geometric majorants): K(3^20) ≤ **4.19188·10⁸** (Case B s ≤ 400: 4.191879·10⁸,
tail ≤ 2.3·10⁻⁷; Case A 39.198) < 3^20 − 3 = 3.4868·10⁹; matches `data/fz/largeq_k1.txt`. Largest terms at s = 25, 35, 15.
Minor implementation remark (m-5): `fz1_largeq.py` replaces an underflowing tail by 1e-300, which is not an upper bound
when the true value lies in (1e-300, e^{−690} ≈ 2.2·10⁻³⁰⁰); immaterial here (×1.0001 slack, margin ×8), but not "fail-closed"
as advertised — use `math.inf` or exact rationals.
**Theorem 8.1** = Thm 7.3 (r ≤ 19) + Lemma 7.4 (r ≥ 20): SOUND. The r = 20..30 direct certificates are a consistent cross-check.

## 7. q = 9 (k = 1) and the odd-s / odd-r observations

*CERTIFIED negative statement about the method.* The author's routes give Σ_{19 ≤ s ≤ 80} = 53.03 (`fz1_sum 2 80 -`: 396.25 −
343.22), R226's routes 43.5; either way > 6 − 4.6, so the union-bound method with these routes cannot close q = 9. Reproduced.
The exact inputs (Case B 3.929 for s ≤ 18, Case A 0.671 for α ≤ 6) are **not archived** (no `data/fz/enum1_9`; m-6). R226's
own exact filtered q = 9 counts (s ≤ 15, `data/fz1_review/enum9`) give Case B mass **3.92790** for s ≤ 14 (s = 2: 1.5556,
4: 2.0000, 6: 0.1701, 8: 0.1704, 10: 0.0126, 12: 0.0190, 14: 0.0003), consistent with 3.929 for s ≤ 18.
*Odd s at q = 9* (EVIDENCE): R226's enumeration confirms 0 filtered tuples for every odd s ≤ 15 (and the q = 9 naive
enumeration for odd s ≤ 5), while even s carry mass. *Odd r* (q = 27, s ≤ 12: none) confirmed (§5). Correctly labelled EVIDENCE /
Spark; nothing in the proofs depends on it.

## Defects

No FATAL, no MAJOR.

* **m-1 (MINOR, Prop 6.1 proof, Case B).** "If z + a + b ≥ 2 then deg v = z + a + b > max(a, b)" fails when z = 0 and
  min(a, b) = 0 (then z + a + b = max(a, b)). Repair: add "if z = 0 and, say, C = 1, then w = T + v and w + 1 = g'v; for a ≥ 2
  deg v = a forces g' = 1 and T + 1 = 0" (or quote the argument of Lemma 7.1(i)). Also "w + C ≠ 0: monic" presupposes E, E'
  nonconstant; add "if E = 1 or E' = 1 then u₀ = −1 directly". (Optional: the remark on lc(E) = 2 holds in every odd
  characteristic with lc(E) = −1, not only in char 3.)
* **m-2 (MINOR, Lemma 7.1(iii)).** Lemma 1.4 is stated for moduli with T | Q; in k = 1 all moduli are T-free. The use is valid
  (every counted divisor divides a T-free F; the cofactor versions have F prime to QT^j), via the R220-repaired hypothesis
  note after Lemma 1.4. Say this explicitly in Lemma 7.1(iii).
* **m-3 (MINOR, Thm 7.3 "Scope", stale).** The paragraph still says r ≥ 20 is EVIDENCE and that `init_omstar`/`init_rankin`
  take q as a C int; both are superseded by §8 (Lemma 7.4 PROVED; helpers now take a floating q). Repair: "r ≥ 20: Lemma 7.4
  (§8); the r ≥ 20 certificates of `fz1_certify.sh 20 30` are a cross-check". Also "Lemma 7.4" sits in §8 (cosmetic).
* **m-4 (MINOR, Lemma 7.4 proof).** State the orientation a ≤ b (C-versions of R3, R4 for a > b): both t = s − σ and
  deg(T^s + m'w²) = s use it.
* **m-5 (MINOR, `fz1_largeq.py`).** Underflow replaced by 1e-300 is not a valid upper bound below e^{−690}; immaterial.
* **m-6 (MINOR, reproducibility).** The q = 9 (k = 1) exact data behind "3.929 / 0.671" are not archived; the CERTIFIED
  statement only needs the route-bound part (53 > 1.4), which is reproducible, but the 3.929 should be archived or labelled
  as computed-not-archived. (R226's independent s ≤ 14 value 3.92790 is consistent.)
* **m-7 (MINOR, wording, Thm 7.3 statement).** "≤ 27.7 (r = 4)" vs the brief/report's "27.6": the log gives 27.634; "≤ 27.7" is
  correct, the report's "27.6" is a rounding-down (report only).
