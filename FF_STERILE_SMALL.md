# FF_STERILE_SMALL — the small-q sterility cases: q = 27 (r = 3), q = 9, and A = T (k = 1) (O220, wave Y-f)

Status: checkpoint 4 (O220): Thm 3.1 (q = 27, k ≥ 2; R220), Thm 5.2 (q = 9, k ≥ 2), Thm 8.1 (A = T, all q = 3^r, r ≥ 3) PROVED (computer-assisted); open: q = 3 (k ≥ 2), q = 9 (k = 1).
(Update, O226: q = 9, k = 1 is closed by FF_ODD_ABSENCE Thm 2.2 (reviewed R240, R241); with Thm 8.1, ES_q(T) has no finite linear
covering for every q = 3^r, r ≥ 2 (FF_ODD_ABSENCE Cor 2.3). Open: q = 3 (k ≥ 2).)
§§6–8 hostile review R226 (`reviews/ff-sterile-small-review-3.md`): no FATAL/MAJOR; Thm 7.3 independently re-certified for
3 ≤ r ≤ 19, Lemma 7.4 re-derived; minor repairs m-1..m-6 applied in place ("(R226 repair)").
Builds on FF_STERILE_PUSH.md ((J)51; notation (B), Lemmas 1.1–1.6, 2.1, 2.2, Thm 3.1), DEPTH_ASPECT.md §2, FUNCTIONFIELD_ES*.md.
Scripts `scripts/fz_*`.

Setting and notation exactly as FF_STERILE_PUSH (q odd, A = T^k, k ≥ 2, Case B tuple (m', g', w, C) of parameter s,
w = Tw₁, C = TC₁, v = T²v₁, degrees a = deg w, b = deg C, z = deg m', y = deg g', t = deg v, a + b + z = s, y + t = max(a, b)).
Key identity (FF_STERILE_PUSH Lemma 1.1(iii)):
  m'w₁C₁ = T^{s−2} + v₁,  deg v₁ = t − 2,  w₁ + C₁ = Tg'v₁.                                         (B₁)

## 0. Iteration log

* (I1) The binding point of the r = 3 barrier, (a, z, y, t)/s = (1/3, 1/3, 1/6, 1/6), is where every factor of
  T^{s−2} + v₁ has degree ≈ s/3 while v₁ has degree ≈ s/6. All Lemma 1.6 routes that pay for v₁ (factor q^{t−2}) and then
  for a factor of degree > t − 2 pay twice: **a monic factor of degree > deg v₁ determines v₁ by Euclidean division**
  (Lemma 1.1 below). This is the "short interval ↔ arithmetic progression" duality of F_q[T] in its simplest form.

## 1. Division routes (new; PROVED, elementary)

**Lemma 1.1 (Euclidean division determines v₁).** Let D be a monic divisor of m'w₁C₁ with deg D > t − 2 (e.g. D = m' if
z ≥ t − 1, D = w₁ if a ≥ t, D = C₁ always, since b − 1 ≥ t − 1). Then v₁ = −(T^{s−2} mod D) and
(T^{s−2} + v₁)/D = T^{s−2} div D (quotient of Euclidean division). In particular D determines v₁ and the cofactor
m'w₁C₁/D.
*Proof.* T^{s−2} = D·(m'w₁C₁/D) + (−v₁) with deg(−v₁) = t − 2 < deg D; Euclidean division by the monic D is unique. ∎

**Lemma 1.2 (division routes; PROVED from Lemma 1.1 and FF_STERILE_PUSH Lemmas 1.3–1.6).** With N*, cls as in
FF_STERILE_PUSH Lemma 1.6 and ω*(e) := max{ω(f) : f ∈ F_q[T], deg f ≤ e, T ∤ f}, the number of tuples with pattern
(s; a, z, y, t) is at most each of
| route | condition | data fixed | then | bound |
|---|---|---|---|---|
| D1 | z ≥ t − 1 | m' | v₁, G := w₁C₁ by Lemma 1.1; w₁ ∣ G of degree a − 1 | N*(z)·C(a+b−2, a−1) |
| D1c | z ≥ t − 1 | m' | as D1, w₁ in one of ≤ 2^{1+ω*(t−2)} square-root classes mod Tv₁ | N*(z)·2^{1+ω*(t−2)}·cls(a+b−2, a−1, t−1) |
| D2 | a ≥ t | w₁ | v₁, m'C₁; C₁ ∣ m'C₁, C₁ ≡ −w₁ (Tv₁) | N*(a−1)·cls(z+b−1, b−1, t−1) |
| D3 | — | C₁ | v₁, m'w₁; w₁ ∣ m'w₁, w₁ ≡ −C₁ (Tv₁) | N*(b−1)·cls(z+a−1, a−1, t−1) |
(cofactor versions of cls allowed in all three: G, m'C₁, m'w₁ are prime to Tv₁ by FF_STERILE_PUSH Lemma 1.1(iii).)
*Proof.* Lemma 1.1 gives v₁ and the cofactor; the rest is FF_STERILE_PUSH Lemma 1.6, rows R9a, R10a, R5a, R5b, with the
v₁-sum replaced by the single determined v₁ (so in D1c the average Σ2^ω is replaced by the maximum 2^{ω*}; Tv₁ has
ω(Tv₁) = 1 + ω(v₁) ≤ 1 + ω*(t − 2)). The tuple is then determined (FF_STERILE_PUSH Lemma 1.2: (m', w, v) or (g', v, w)
with g' = (w₁ + C₁)/(Tv₁)). ∎
These are the rows R9a, R10a, R5a, R5b without the factor N*(t − 2) — a gain of q^{t−2} whenever the condition holds.
At the r = 3 critical point (1/3, 1/3, 1/6, 1/6): D1 has exponent z + (a + b)·log 2/log q = 1/3 + (2/3)(log 2/log 27) = 0.4736 < 1/2.

**Lemma 1.3 (v₁ in a residue class; PROVED).** For every monic D ∣ m'w₁C₁: v₁ ≡ −T^{s−2} (mod D). Hence, for fixed D, the
number of admissible v₁ (deg t − 2, fixed leading coefficient lc(w + C)) is ≤ V(D) := q^{t−2−deg D} if deg D ≤ t − 2, and 1
otherwise (Lemma 1.1) (R220 repair m-1: formerly the weaker max(1, q^{t−1−deg D}); the certificate uses the sharp count). So in every route of FF_STERILE_PUSH Lemma 1.6 that fixes v₁ together with some of
m', w₁, C₁, the factor N*(t − 2) may be replaced by V(product of the fixed factors): (m', v₁) costs ≤ N*(z)·V(z),
(w₁, v₁) ≤ N*(a−1)·V(a−1), (C₁, v₁) ≤ N*(b−1)·V(b−1), (m', w₁, v₁) ≤ N*(z)N*(a−1)·V(z+a−1).
*Proof.* m'w₁C₁ = T^{s−2} + v₁ ≡ 0 (mod D). The v₁ ≡ given class mod D with deg v₁ = t − 2 and fixed leading coefficient:
if deg D ≤ t − 2 these are σ + D·h with deg h = t − 2 − deg D and fixed lc(h): exactly q^{t−2−deg D} choices. ∎
(R220 repair m-2) *τ-bound used by the certificate in R10a3.* For D = m' (deg z), e = t − 2:
Σ_{v₁ ≡ σ (m'), deg e, fixed lc} 2^{ω(v₁)} ≤ min(V(m')·2^{ω*(e)}, 2Σ_{j≤e/2} q^j·max(1, q^{e−z−j})), since 2^ω ≤ τ ≤ 2#{δ | v₁ : deg δ ≤ e/2},
and δ | v₁ forces gcd(δ, m') = 1 (v₁ ≡ −T^{s−2} is a unit mod m'), so by CRT each δ of degree j lies in ≤ max(1, q^{e−z−j}) such v₁.
Tail form (fz_tail): ≤ 2(s+1)q^{max(e/2, e−z)} for z ≤ e, and 2^{ω*(e)} ≤ 2^{(q−1)/2 + e/2} (at most q − 1 linear factors ≠ T,
the others of degree ≥ 2).
Routes affected (exponent per unit s, continuum): R5a → max(a, t) + class, R5b → max(b, t) + class, R9a → max(z, t) + C(a+b, a),
R10a → max(z, t) + class (with max 2^{ω*} instead of the average Σ2^ω), X1 → y + max(z, t), X2 → y + max(a, t),
R4' → max(z + a, t). Lemma 1.2's D-routes are the special case deg D ≥ t − 1.

**Lemma 1.4 (refined class bound below the Coppersmith threshold; PROVED).** In the setting of FF_STERILE_PUSH Lemmas 1.4/1.5
(F of degree n, Q of degree ρ, σ a unit mod Q, divisors E of degree d with E ≡ σ (mod Q)), assume moreover T ∣ Q and
T ∤ F. Then for every j ≥ 0 the number of such E is ≤ q^j·cls(n, d, ρ + j) (and ≤ q^j·cls with the cofactor version if F is
prime to Q).
*Proof.* Every such E is prime to T, so E mod QT^j is one of the ≤ q^j lifts of σ that are units mod QT^j (Q·T^j has the
same prime factors as Q since T ∣ Q). Apply the class bound with modulus QT^j (degree ρ + j) to each lift; cofactor version:
F prime to Q is prime to QT^j. ∎
All moduli used in the class routes (Tv₁, TL', Tw₁g', Tm'w₁, Tm'C₁, …) contain T and all F there are prime to T, so the
lemma applies to every class route. Continuum consequence: a class route with data (n, d, ρ) costs an extra exponent
max(0, d(n − d)/n − ρ) (Coppersmith threshold), instead of failing outright below the threshold.
(Repair of the hypothesis: Lemma 1.4 only needs every counted E to be prime to T, which holds when T ∣ Q (σ is a unit
mod Q) or T ∤ F; the cofactor version needs F prime to QT^j (equivalently to Q when T ∣ Q; R220 repair m-3).)

*Check (EVIDENCE):* `scripts/fz_check_bounds.c` compares the minimum of all routes as coded in `scripts/fz_sum.c` (Lemma 1.6 rows
with the refined class bound, plus Lemma 1.2/1.3 rows) with the exact pattern counts of `bsE_famcount`: q = 3, s ≤ 19
(146 patterns, 638 tuples); q = 5, s ≤ 13 (54 patterns); q = 7, s ≤ 11 (19 patterns): 0 violations, max count/bound 1.000.
(R220 repair m-5: this tests only the minimum over routes; R220's `scripts/review_fz_brute.py` tests every route separately,
q = 3 s ≤ 15, q = 5 s ≤ 11, q = 7 s ≤ 10: 0 violations.)

**Steering (EVIDENCE, `scripts/fz_rate.py`, grid + local refinement).** Continuum per-s exponent max_p min_route φ − 1/2
(units of log q):
| r | Lemma 1.6 only | + Lemmas 1.2/1.3 | + Lemma 1.4 | maximiser (last column) |
|---|---|---|---|---|
| 1 | +0.167 | +0.167 | **0.000** | thirds corner (1/3, 1/3, 1/3, 0) |
| 2 | +0.096 | +0.066 | **−0.044** | (1/3, 1/3, 1/3 − t, t), t ∈ [0, 0.02] (flat) |
| 3 | 0.000 | −0.010 | **−0.100** | (1/5, 1/5, 1/5, 2/5): the Elsholtz–Tao point, all routes = 2/5 |
| 4 | −0.021 | −0.058 | −0.100 | (1/5, 1/5, 1/5, 2/5) |
So at r ≥ 3 the exponent becomes the "ET exponent" 2/5 (DEPTH_ASPECT Lemma 2.2's 2(s − 3)/5 point), with a margin 1/10.

## 2. Case A tail for q ≥ 9

**Lemma 2.1 (PROVED).** For q ≥ 9 the number of Case A data of depth α valid somewhere on the slices is ≤ (α + 1)³·q^{(α−1)/2}·3^{α/2}.
*Proof.* Per pattern (λ, β, κ, f = α − β − κ, ζ = max(β, f) − λ ≥ 1) FF_STERILE_PUSH Lemma 2.2 gives route (i) ≤ q^{λ+β+κ−1},
route (ii) ≤ q^{λ+κ+f−1}, so min ≤ q^{λ+κ−1+min(β,f)} = q^{α−ζ−1} (as λ = max(β, f) − ζ); and route (v) ≤ q^ζ·α!/(β!κ!f!) ≤ q^ζ 3^α.
min(x, y) ≤ (xy)^{1/2} = q^{(α−1)/2} 3^{α/2}. Patterns: ≤ (α + 1)³. ∎
So the Case A mass beyond α > 40 is ≤ Σ_{α>40} (α+1)³ q^{−(α+1)/2} 3^{α/2}, ratio ≤ (43/42)³(3/q)^{1/2} < 1 (R220 repair m-9) (`scripts/fz_caseA.py`).
(This replaces the 6^α of DEPTH_ASPECT Lemma 2.4, which made the O216 Case A tail diverge for q = 27.)

## 3. Theorem: q = 27

**Theorem 3.1 (no finite linear covering of ES₂₇(T^k), k ≥ 2; PROVED, computer-assisted, same inputs and same certification
standard as FF_STERILE_PUSH Thm 3.1).** Let q = 27 and k ≥ 2. Then O(27, T^k) ≠ ∅, so ES₂₇(T^k, ·) has no finite linear
covering. More precisely the covered relative measure, summed over the 26 c-slices, is ≤ 3.06; hence at most 6 of the 26
c-slices have covered measure ≥ 1/2, and at least 20 have more than half of their measure in O(27, T^k).
*Proof.* As FF_STERILE_PUSH Thm 3.1 (take k = 2; Lemma 2.1 there), with the route minimum of Lemma 1.6 there extended by
Lemmas 1.2–1.4 and 4.1 here. `scripts/fz_certify.sh "3 80"` (log `data/fz/certify.txt`): finite Case B part 3 ≤ s ≤ 80
(`fz_sum.c`, long double) 3.0180430695; tail s > 80 (`fz_tail.c`, adaptive boxes, all 42 096 boxes certified; class
refinement j = ⌈θs⌉ with θ on a grid of step 1/256, cost q^{θs+1}) ≤ 2.922·10⁻⁴; Case A ≤ 0.0096590 (α ≤ 40 exact,
`fs_caseA.py`) + 6.1·10⁻¹⁶ (Lemma 2.1). Certified total (×1.01, the O216 error budget) 3.0583 < q − 1 = 26. ∎
(R220 repair m-4: Lemma 4.1 and the τ-bound of Lemma 1.3 are not needed: R220's independent certificate without them,
`scripts/review_fz_sum.c`, `review_fz_tail.c`, gives ≤ 3.056 (≤ 4.44 even with the weaker V of the original Lemma 1.3).)
*Cross-checks.* (i) `scripts/fz_sum_check.py 3 60` (exact integers/rationals, written from the text of the lemmas, own
(m, k) search, no Lemma 4.1) gives 3.017899 ≤ fz_sum's 3.018046 (same routes without Lemma 4.1; the difference is the
larger (m, k) search). (ii) Tail consistency: tail(60) ≤ 0.538 dominates fz_sum(61..80) + tail(80) = 3.6·10⁻⁸ + 2.9·10⁻⁴.
(iii) `fz_tail r S 8 1e-3 0` (new routes off) reproduces fs_tail exactly (r = 4, S = 60: 4.5833·10⁴ both).
(iv) Bound-vs-exact-count check of §1 (q = 3, 5, 7). Exact counts at q = 27 are out of reach; the routes are q-uniform.

## 4. Fixed-q divisor bounds: exponent 2/5 for every odd q, and the q = 9 status

**Lemma 4.1 (fixed-q divisor bound; PROVED).** Let F ∈ F_q[T] have exact degree n, T ∤ F, and let I'(j) be the number of
monic irreducibles of degree j other than T. For every ρ ∈ (0, 1], the number of monic divisors of F of degree d is
≤ ρ^{−d'}·exp(V_ρ(n)), d' = min(d, n − d), where V_ρ(n) is the value of the fractional knapsack with capacity n whose items
are the pairs (P, e) (P irreducible ≠ T of degree j, at most I'(j) of each degree, e ≥ 1), of weight j and gain
log(S_e(ρ^j)/S_{e−1}(ρ^j)), S_e(y) = 1 + y + … + y^e.
*Proof.* Divisors of degree d ↔ divisors of degree n − d (cofactor), so take d' ≤ n/2. With F = ΠP_i^{e_i},
#{D ∣ F monic, deg D = d'} = [x^{d'}] Π_i S_{e_i}(x^{deg P_i}) ≤ ρ^{−d'} Π_i S_{e_i}(ρ^{deg P_i}) (Rankin; nonnegative
coefficients). log Π S_{e_i} = Σ_i Σ_{e ≤ e_i} gain(P_i, e) with Σ e_i deg P_i = n. For fixed P the gains decrease in e
(S_e/S_{e−1} = 1 + y^e/S_{e−1}(y) decreases for 0 < y ≤ 1), so the integer solution uses each chain as a prefix and its value is ≤ the
fractional-knapsack optimum (all gains ≥ 0). ∎ Implemented in `fz_sum.c` (64 values of ρ; V_ρ by greedy fill, rounded
outward; brute-force check `scripts/fz_rankin_check.py`: q = 3, n ≤ 11 and q = 5, n ≤ 7, all d: 0 violations, max/bound 0.985); used in every C(n, d) of the routes and in R1 as N_z(F)·N_{a−1}(F/m′) (and permutations).
For fixed q **all divisor counts are q^{o(n)}** (R220 repair m-7, elementary: with F = ΠP_i^{e_i} of degree n, primes of degree
≥ J contribute Π(e_i + 1) ≤ 2^{Σe_i} ≤ 2^{n/J}; there are < q^J primes of degree < J, each with e_i + 1 ≤ n + 1; so
τ(F) ≤ 2^{n/J}(n+1)^{q^J}, and J = ⌊log_q(n/log²(n+2))⌋ gives log τ(F) = O(n log q/log n); δ₃ ≤ δ²), and every entropy term
of the continuum exponents disappears.

**Corollary 4.2 (EVIDENCE for the value 2/5 (grid); the bound itself PROVED).** For every odd q the Case B tuples of
parameter s number ≤ q^{(2/5)s + o(s)}. (Already from DEPTH_ASPECT Lemma 2.2 with δ, δ₃ = q^{o(n)} at fixed q, i.e. the
routes R1–R4 with sharp divisor bounds; `fz_rate.py r 40 3 0` confirms that the extended route set has the same maximum
2/5, attained only at (1/5, 1/5, 1/5, 2/5), for q = 3, 9, 27.) So at every odd q the tail of (Σ) converges geometrically
with rate q^{−s/10 + o(s)}; the obstruction at small q is entirely the finite part.

**q = 9 (CERTIFIED statement about the method; EVIDENCE for the shape).** With all routes (Lemmas 1.2–1.4, 4.1)
`fz_sum 2 80` gives finite sum 41.87 > q − 1 = 8 (terms 10⁻⁶ at s = 80, so the tail is negligible), but already
Σ_{s ≤ 8} = 9.22 > 8 and Σ_{s ≤ 20} = 37.6. (R220 repair m-6: "tail negligible" holds only with Lemma 4.1 in the
routes — without it the term at s = 80 is 0.118 — and is EVIDENCE: no q = 9 tail certificate at this point; see §5.) So (Σ) at q = 9 needs **exact counts of Case B tuples for s up to ≈ 20–24**
(or sharper small-s bounds); the bounds at s ≤ 12 are dominated by t ∈ {2, 3} (v₁ constant or linear: R1 counts
triples of a *single* polynomial T^{s−2} + v₁, computable exactly by factoring) and by z = 0 patterns. (R221 repair m-2: done in §5 — Theorem 5.2, exact counts s ≤ 22.)
At q = 3, (Σ) fails even with exact counts (FF_STERILE_PUSH §5: 94/27 > 2), so no union bound of this kind can work there.

## 5. q = 9: exact small-level counts close (Σ) (O220 checkpoint 2)

**5.1 Exact enumeration (`scripts/fz_enum.c`).** For each pattern (s; a, z, y, t), a ≤ b, all Case B tuples are listed by one
of eight loss-free reconstructions and every candidate is checked against the full definition (B) (m', w₁, C₁, g' monic with
nonzero constant terms and exact degrees, m'w₁C₁ = T^{s−2} + v₁, w₁ + C₁ = Tg'v₁, deg v₁ = t − 2, lc(v₁) = lc(w + C)); so the
output is exact provided the route lists every tuple. Routes (each complete by the cited identity):
* candidate search: M2 (C₁; v₁, m'w₁ by Lemma 1.1; then w₁ ≡ −C₁ mod Tv₁ or m' ∣ m'w₁), M3 (w₁; v₁ in its class mod w₁,
  Lemma 1.3; then C₁ ≡ −w₁ mod Tv₁ or m' ∣ m'C₁), M5 ((m', g', v₁ in its class mod m'); w₁, C₁ = roots of
  X² − Tg'v₁X + (T^{s−2} + v₁)/m', FF_STERILE_PUSH Lemma 1.2 X1);
* factoring (the class-divisor routes made exact: factor F completely over F_q — squarefree decomposition, distinct-degree
  factorisation, Cantor–Zassenhaus — and run over *all* its monic divisors of the required degree): M11 ((m', v₁) → w₁ ∣ w₁C₁),
  M12 ((m', g') → E ∣ 1 + T^s m'g'², R2), M13 ((w₁, g') → E ∣ g'T^{s−1} + w₁, R3), M14 ((m', w₁) → E ∣ T^{s−2} + m'w₁², R4),
  M16 ((w₁, v₁) → C₁ ∣ m'C₁, R5a).
Each factorisation is checked fail-closed (product of the factors = F; each factor monic, pairwise distinct, irreducible by
Rabin's test; exit on failure).
*Validation (EVIDENCE):* every one of the eight routes, forced on all patterns, reproduces the independent bsE_famcount census
exactly (q = 3, s ≤ 15; q = 5, s ≤ 12; q = 7, s ≤ 10; 0 mismatches; auto mode also q = 3 s ≤ 19, q = 5 s ≤ 13, q = 7 s ≤ 11).
At q = 9: F₉ table axioms checked; the factoring routes agree with the candidate-search routes on all patterns of s ≤ 13 and
on the 1053 patterns of 14 ≤ s ≤ 17 with search cost ≤ 9⁶; the self-checked binary reproduces the unchecked runs for all s ≤ 22 byte for byte.
R220 independently enumerated q = 9 through s = 9 (covered mass 0.553), matching.
(R221 repair m-6) R221 independently re-enumerated q = 9 for **all s ≤ 22** (own field model F₃[α]/(α² − α − 1), own polynomial
code; factoring-free routes for s ≤ 18 and for cheap patterns, FLINT-factoring routes otherwise; full (B) check): all 7 040
patterns agree count for count (`scripts/review_fz9_enum.c`, `review_fz9_flint.py`; `data/fz/review_r221_enum9_*.txt`). A certificate
built only from reviewer code (these counts, R220's route code + R221's own Lemma 4.1 for 23 ≤ s ≤ 80, own linearised tail, R218's Case A)
gives (Σ) ≤ 3.95 < 8 (`reviews/ff-sterile-small-review-2.md` §1b). Robustness: with the bounds of fz_sum, exact counts through s = 18
already suffice (4.735 < 8).

**5.2 Exact masses at q = 9 (CERTIFIED by exhaustive computation).** Σ_{s≤18} (tuples weighted by mult·9^{1−⌈s/2⌉}) = 0.592177;
per-level terms: 0.222 (s = 4), 0.049, 0.198, 0.027, 0.055, 0.0018, 0.029, 0.0020, 0.0045, 1.8·10⁻⁴, 2.6·10⁻³, 5.2·10⁻⁵,
8.3·10⁻⁵, 3.6·10⁻⁶, 1.5·10⁻⁴ (s = 18), against route bounds (s = 3, 4, 5, 6, …, 12; R221 repair m-3) 0.22, 0.89, 0.68, 2.47, …, 4.6 — the bounds overcount
by factors 10³–10⁴ at s ≈ 12–18.

**Lemma 5.1 (Lemma 4.1 linearised for the tail; PROVED).** V_ρ is concave and piecewise linear, so for any n₀,
V_ρ(n) ≤ V_ρ(n₀) + λ(n − n₀) for all n, λ the right derivative at n₀ (the ratio of the knapsack class that supplies the next
unit). Hence for s ≥ S every divisor count in a tail box is ≤ exp(s(−D log ρ + λN + c⁺/S)), c = V_ρ(n₀) − λn₀, with D, N the
box upper bounds of d'/s, n/s (the bound is increasing in d' and n). `fz_tail.c` (RANK = 1) uses 24 values of ρ and
n₀ ∈ {S/2, S, 2S, 4S}, outward rounded; brute-force check of the linearised bound (q = 3, 4 ≤ n ≤ 11): 0 violations.
(R221 repair m-4) The linearisation is used for all n at once, so V_ρ must be the knapsack over the FULL item set. The code keeps
the items with e·deg P ≤ NM = 8S + 8 (and gain ≥ 10⁻¹⁸); every omitted item has ratio ≤ min(1/NM, ρ^{NM}) (its gain
log(1 + y^e/S_{e−1}(y)), y = ρ^{deg P}, is ≤ min(1/e, y^e)), and `init_rankin` now checks fail-closed that this is < λ, so the
omitted items change neither V_ρ(n₀) nor the right derivative. (R221 also verified the constants externally against an untruncated
knapsack, `scripts/review_fz9_rankin.py`: 0 violations.)

**Theorem 5.2 (no finite linear covering of ES₉(T^k), k ≥ 2; PROVED, computer-assisted: O216 certification standard plus
exhaustive enumeration).** O(9, T^k) ≠ ∅ for every k ≥ 2, so ES₉(T^k, ·) has no finite linear covering. The covered relative
measure summed over the 8 c-slices is ≤ 3.58 < 8: the average uncovered fraction of a c-slice is ≥ 0.55, at least one c-slice
is more than half uncovered, and at most 3 c-slices have covered measure ≥ 0.95 (the number of c with covered measure ≥ θ is
≤ 3.58/θ).
*Proof.* (Σ) with k = 2 (FF_STERILE_PUSH Lemma 2.1). `scripts/fz_certify9.sh 80` (log `data/fz/certify9.txt`): finite part
3 ≤ s ≤ 80 by `fz_hybrid.c` — exact counts for s ≤ 22 (`data/fz/enum9/e_<s>.txt.gz`, produced by the self-checked fz_enum;
every pattern of each level listed, which fz_hybrid checks), exact mass 0.592201; route bounds (FF_STERILE_PUSH Lemma 1.6 +
Lemmas 1.2–1.4, 4.1) for 23 ≤ s ≤ 80; total 3.2872203; tail s > 80 by `fz_tail.c` with Lemma 5.1: ≤ 0.079749 (242 053 boxes,
none failed); Case A ≤ 0.17501 (α ≤ 40 exact, `fs_caseA.py`) + 1.1·10⁻⁵ (Lemma 2.1). Certified total (×1.01) 3.5774 < q − 1 = 8. ∎
(With exact counts only for s ≤ 18 the same certificate gives 4.735; `fz_certify9.sh 80 1 22` regenerates the enumeration (R221 repair m-1: formerly “80 1 21”, which bounds s = 22 instead).)
*Remark.* The exact per-level masses decay fast (1.8·10⁻⁵ at s = 22); the true left side of (Σ) is very likely ≈ 0.592 < 1,
which would give every c-slice — but levels 23 ≤ s ≤ 80 are covered only by route bounds (mass 2.70), so this is EVIDENCE.
With (J)51 and Theorem 3.1: **for every q = 3^r, r ≥ 2, and every k ≥ 2, ES_q(T^k) has no finite linear covering**; q = 3 stays
open (Conjecture 0.2; §5.3).

**5.3 q = 3 and Conjecture 0.2: an honest estimate of s₀ (Assessment, from CERTIFIED bound sums).** With all routes
(Lemmas 1.2–1.4, 4.1), `fz_sum 1 200` gives at q = 3 per-level bound terms 26.1 (s = 10), 68.1 (s = 20), 52.9 (s = 30),
26.3 (s = 40), 9.15 (s = 50), 2.43 (s = 60), 0.60 (s = 70), 0.15 (s = 80), 0.039 (s = 90), 0.011 (s = 100), 3·10⁻³ (s = 110);
bound-sum to s = 200: 1466.7. So the bound tail Σ_{s>s₀} drops below 0.5 (the scale of the uncovered measure left by the exact
union through s = 21, FF_STERILE_PROOF §5) only at **s₀ ≈ 80–85**. Since union bounds fail at q = 3 even with exact counts
(94/27 > 2), a proof along these lines needs the exact *union* of all cylinders of levels s ≤ s₀ ≈ 85. The true tuple counts are
≈ 3^{0.2s}–3^{0.4s} per level (FF_STERILE_PROOF §6, Cor. 4.2), i.e. up to ~10¹⁶ tuples at s ≈ 85, and the enumeration cost of
fz_enum grows like ≈ 3^s at q = 9 (≈ 9^{s/2}; R221 repair m-5); at q = 3 it would be ≈ 3^{s/2} ≈ 10²⁰ at s = 85. **Infeasible** (and it would
give only the conclusion of Conjecture 0.2 — no finite linear covering — not x*_c ∈ O). Conjecture 0.2 needs sharper bounds
at moderate s (where the routes overcount by factors 10³–10⁴, §5.2) or a structural argument.

## 6. A = T (k = 1), q = 3^r ≥ 9: where the depth hypothesis fails, and that the other slices restore it

Setting: k = 1, slice points x_u (x ≡ 1 off T, x ≡ u mod T^∞), u ∈ F_q[[T]]^*, u₀ := u(0). A linear family is valid at x_u iff
(FUNCTIONFIELD_ES3 Lemma 1.1, stated for general k) E ≡ −u (mod T^{N+1}), E ≡ −1 (mod L'), plus the Case A / Case B
divisibility, with N = k + j − 1 = j, j = v_T(L). So the validity set on the slice is the cylinder u ≡ −E (mod T^{N+1}); depth
N + 1 = 1 means a whole class u₀ = −E(0).

**Proposition 6.1 (depth-1 families; PROVED, elementary).** Let q be odd, k = 1. Every family with j = 0 (cylinder depth 1)
has u₀ = −E(0) ∈ {−1, −2}. Precisely: Case A with j = 0 forces E constant, E ∈ {1, 2} (the families of FUNCTIONFIELD_ES
Prop 1.4); Case B with j = 0 forces u₀ = −1, and there are exactly the tuples (m', g', w, C) = (T + 2, 1, 1, 1),
(1, T + 2, T + 1, 1), (1, T + 2, 1, T + 1) (E = T + 1, T² + 3T + 1, T + 1, all with E(0) = 1).
*Proof.* Case B (j = 0, so γ = 0, s = 1): writing E = L'w − 1, E' = L'C − 1 (E ≡ E' ≡ −1 mod L'), EE' = 1 + TL'g' gives
m'wC = T + v, w + C = g'v (FUNCTIONFIELD_ES3 Lemma 2.1(a), pure algebra). (R226 repair m-1: if E = 1 or E' = 1 then u₀ = −1
directly, as E' ≡ −u^{−1}; otherwise E, E' are monic of positive degree, so w, C are monic.) If z + a + b ≥ 2 and z + min(a, b) ≥ 1
then deg v = z + a + b > max(a, b) ≥ deg(w + C) = deg(g'v) ≥ deg v (w + C ≠ 0: monic, q odd): impossible. (R226 repair m-1: if
z = 0 and min(a, b) = 0, say C = 1, then w = T + v; for a ≥ 2, deg v = a forces g' = 1 and T + v + 1 = v: impossible.) So z + a + b ≤ 1. (z, a, b) = (1, 0, 0):
w = C = 1, g'v = 2, g' = 1, v = 2, m' = T + 2, E = T + 1. (0, 1, 0): w = T + v with v constant, w + 1 = g'v, comparing leading
coefficients v = 1, g' = T + 2, E = (T + 2)(T + 1) − 1 = T² + 3T + 1. (0, 0, 1) symmetric (E = L' − 1 = T + 1). (0, 0, 0):
m' = 1 = T + v and 2 = g'v force deg v = 1 and deg v = 0: impossible. In all cases E(0) = 1, u₀ = −1.
Case A (j = 0): a0 = ga1, b0 = gb1, gcd(a1, b1) = 1, E ∣ a1 + b1, E ≡ −1 mod a1b1 (T ∤ a1b1 as j = 0). If E is not
constant, E + 1 ≠ 0 is divisible by a1b1, so deg E ≥ deg a1 + deg b1, while deg E ≤ deg(a1 + b1) ≤ max(deg a1, deg b1);
so one of them, say b1, is 1, and deg E = deg a1 ≥ 1. Then deg a0 > deg b0, so lc(a0 + b0) = lc(L/a0 + L/b0) = 1 and E is
monic (lc(E) = lc(s) ∈ {1, lc(a0 + b0), lc(L/a0 + L/b0)}, DEPTH_ASPECT Lemma 2.4). Hence E + 1 = a1 and E ∣ a1 + 1 = E + 2 gives
E ∣ 2: contradiction. (Monicity matters in characteristic 3: with lc(E) = 2 one would get E + 1 = 2a1 and E ∣ a1 + 1 ⟺ E ∣ 3 = 0.)
So E is constant, E = lc(s) ∈ {1, lc(a0 + b0), lc(L/a0 + L/b0)} ⊂ {1, 2}. ∎
**Corollary 6.2.** For q = 3^r (so {−1, −2} = {2, 1} = F₃^*), on every slice with u₀ ∈ F_q^* ∖ F₃^* every valid family has
cylinder depth ≥ 2 (N ≥ 1): hypothesis (H1) of FF_STERILE_PUSH §4 is restored on these q − 3 slices. For q = 3 there are no such
slices (that is the (J)4 covering), for q = 9 there are 6.
**What changes on these slices (PROVED by the same algebra).** u₀ ≠ 1 gives L'(0)w(0) = 1 − u₀ ≠ 0 and L'(0)C(0) = 1 − u₀^{−1} ≠ 0,
so T ∤ w, C, v (v ≡ m'wC mod T): the Case B tuples are
  m'wC = T^s + v,  w + C = g'v,  T ∤ m'g'wCv,  s = N + 1 + γ, 0 ≤ γ ≤ N,                         (B^{k=1})
with relative cylinder mass q^{−N(s)}, N(s) = ⌈(s − 1)/2⌉, on the slice u₀ = −E(0). Compared with (B) (k ≥ 2, u₀ = 1), the
T-adic constraints T ∥ w, T ∥ C, T² ∣ v are gone (counts grow by ≈ q^{3}·(1 − 1/q)³ per pattern), the slice weight improves by
q^{1/2} on average (N(s) = ⌈(s−1)/2⌉ vs ⌈s/2⌉ − 1) and the averaging is over q − 3 slices. Case A changes too (T ∤ K now, since
E(0) + 1 = 1 − u₀ ≠ 0); its count has to be redone. Status: the reduction is PROVED; the counting certificate for k = 1 is not done.

## 7. A = T (k = 1): no finite linear covering for q = 3^r, 3 ≤ r ≤ 19 (O220 checkpoint 3)

Setting of §6: the q − 3 slices u₀ ∈ F_q^* ∖ F₃^*, all cylinders of depth ≥ 2 (Cor. 6.2), Case B tuples (B^{k=1}) with relative
mass q^{−⌈(s−1)/2⌉}. For k = 1 the analogue of FF_STERILE_PUSH Lemma 2.1 reads: if Σ_{Case B} q^{−N(s)} + Σ_{Case A} q^{−α} < q − 3,
some slice has positive uncovered measure, so O(q, T) ≠ ∅ and ES_q(T, ·) has no finite linear covering.

**Lemma 7.1 (k = 1 Case B structure and routes; PROVED).** (i) For every tuple (B^{k=1}): deg(m'wC) = s (if z + a + b > s then
deg(g'v) ≥ z + a + b ≥ max(a, b) forces z = 0, min(a, b) = 0, g' = 1, v = w + C, and then w + C = wC − T^s is impossible; if
z + a + b < s then deg v = s > max(a, b) ≥ deg(g'v)); y + t = max(a, b); E·v = T^s + m'w², EC = g'T^s + w, EE' = 1 + T^s L'g'
(same algebra as FF_STERILE_PUSH Lemma 1.1, DEPTH_ASPECT Lemma 2.1). (ii) Congruences: E ≡ −1 mod L'w (and mod g'w, m'w),
C ≡ −w mod v, w² ≡ −wC mod v, v ≡ −T^s mod every factor of m'wC (Lemma 1.3 analogue: V(D) = q^{t−deg D} or 1), and
w is a unit mod v. (iii) Hence the 19 routes of `scripts/fz1_sum.c` (the k = 1 rows of FF_STERILE_PUSH Lemma 1.6 with
w₁ → w, C₁ → C, v₁ → v, T^{s−2} → T^s, moduli without the factor T; class bounds with Lemma 1.4 refinement — every
counted E, w, C, m' is prime to T, every F is prime to T; Lemma 4.1 divisor bounds) are valid upper bounds. (R226 repair m-2:
here every modulus is T-free, so Lemma 1.4 is used in its repaired form — every counted divisor divides a T-free F, hence is prime
to T, and every F used with the cofactor version is prime to QT^j.)
*Check (EVIDENCE):* every route separately vs the exact counts of `fz1_enum` (q = 3, s ≤ 12; q = 5, s ≤ 9; q = 7, s ≤ 8;
q = 9, s ≤ 9): 0 violations (`scripts/fz1_check_bounds.c`).

**Lemma 7.2 (k = 1 Case A on the slices u₀ ∉ F₃^*; PROVED).** (a) In Case A exactly one of a1, b1 is divisible by T
(if neither, the argument of Prop 6.1 forces E constant, E ∈ {1, 2}, i.e. u₀ ∈ F₃^*); write T^α ∥ a1 (α ≥ 1), K = (E + 1)/(a1'b1)
(now T ∤ K since E(0) + 1 = 1 − u₀ ≠ 0), F = (a1 + b1)/E, z = (F + b1)/a1'. The identities (A0)–(A4) of DEPTH_ASPECT Lemma 2.3
hold verbatim, z ≠ 0 and T ∤ z, patterns with β > α + λ do not occur (they force KF = 1 and T^α + F = 0), so f = α − β − κ ≥ 0,
λ ≤ max(f, β), deg z ≤ ζ := max(f, β) − λ, and the maximal cylinder has relative mass q^{−α}. New route (ix): E ∣ 1 + T^α a1'²K,
E ≡ −1 mod a1'K. Routes (i)–(vi) of `scripts/fz1_caseA.py` are valid upper bounds (lc(E) = lc(K) ∈ {1, 2}: factor 2 wherever a
bound counts monic divisors only). (b) count(α) ≤ (α+1)³·√8·q^{(α+1)/2}·3^{α/2} (as Lemma 2.1), so the tail α > 40 is a convergent
geometric series for q ≥ 9.
*Check (EVIDENCE):* every route separately vs exact data from `fz1_caseA_enum` (route (ix) by factoring, cross-checked against
direct enumeration of (a1', b1, K)): q = 3 (α ≤ 7), 5, 7 (α ≤ 5), 9 (α ≤ 4): 0 violations (this check found and fixed the lc
factor 2 in routes (iii), (iv)).

**Exact enumeration (`fz1_enum.c`, `fz1_caseA_enum.c`).** k = 1 versions of the §5 routes (M2 needed one repair: for y = 0 the
factor C has degree t and does not determine v; then v = r₀ + lc·C by Lemma 1.3), validated by all 8 routes forced against an
independent Python brute force (`fz1_brute.py`: q = 3, s ≤ 8; q = 5, s ≤ 6; q = 7, s ≤ 5; 0 mismatches) and by cross-method
agreement at q = 3, 5, 27; F₂₇ = F₃[x]/(x³ − x − 1), field axioms checked; factorisations self-checked. With the slice filter
E(0) ∉ F₃ (the tuple's cylinder lies in a counted slice): **at q = 27 there are no tuples at all for s ≤ 12 and no Case A data
for α ≤ 4 on the 24 slices** (CERTIFIED by enumeration); unfiltered, all 172 tuples with s ≤ 7 have E(0) = 1 (slice u₀ = −1).

**Theorem 7.3 (no finite linear covering of ES_q(T) for q = 3^r, 3 ≤ r ≤ 19; PROVED, computer-assisted, O216 standard).**
For q = 3^r with 3 ≤ r ≤ 19, O(q, T) ≠ ∅: ES_q(T, ·) has no finite linear covering. The covered measure summed over the q − 3
slices u₀ ∉ F₃^* is ≤ 9.47 (r = 3; q − 3 = 24), ≤ 27.7 (r = 4; 78), ≤ 15.5 (r = 5), ≤ 11.1 (r = 6), ≤ 9.74 for 7 ≤ r ≤ 19 (decreasing to 9.0900 at r = 19).
*Proof.* `scripts/fz1_certify.sh 3 19` (log `data/fz/certify_k1.txt`): Case B finite part 2 ≤ s ≤ 80 (`fz1_sum.c`; for r = 3 with
the exact filtered counts s ≤ 12, `data/fz/enum1_27/`), tail s > 80 (`fz1_tail.c`, all boxes certified), Case A (`fz1_caseA.py`,
α ≤ 40 exact rationals, for r = 3 with exact filtered counts α ≤ 4; tail Lemma 7.2(b)); certified total ×1.01 < q − 3. ∎
*Scope.* (R226 repair m-3: superseded by §8 — r ≥ 20 is Lemma 7.4 (PROVED), and the helpers now take a floating q; the original
text was: "r ≥ 20 is not certified only for an implementation reason ... so r ≥ 20 is EVIDENCE".) The certified totals converge
to ≈ 9.09 (Case B → 7.00, from s = 2, 3 at large q; Case A → 2.00, from α = 1). *Independent re-certification (R226):* with
R226's own routes, tail, Case A bound and its own exact q = 27 enumeration (0 filtered tuples for s ≤ 12, confirmed), totals ≤ 18.03
(r = 3), 31.89 (r = 4), ≤ 19.62 (r ≥ 5) (`reviews/ff-sterile-small-review-3.md` §5). **q = 9 (k = 1) is not closed** (by this method; closed by FF_ODD_ABSENCE Thm 2.2, O226, which restricts the union bound to the
four primitive slices via the root-product law)**:** exact filtered counts
(R226 repair m-6: not archived; R226's independent s ≤ 14 value is 3.92790) give Case B mass 3.929 for s ≤ 18 (all from
even s; no tuples at odd s ≤ 17) and Case A ≤ 0.671 (exact α ≤ 6), but the route bounds for 19 ≤ s ≤ 80 add 53 > 6 − 4.6
(CERTIFIED statement about the method; the exact masses decay like 10⁻⁵ at s = 18, so the true sum is very likely ≈ 4.6 < 6, EVIDENCE).
Contrast: q = 3 has a finite covering ((J)4) — there are no slices u₀ ∉ F₃^*.

## 8. A = T for all r ≥ 3 (O220 checkpoint 4)

**Lemma 7.4 (q-uniform bound; PROVED).** For every q = 3^r ≥ 9 the left side of the k = 1 union bound over the q − 3 slices is
≤ K(q) := Σ_{s≥2} 2(s+1)³·8^s·q^{e(s)} + Σ_{α≥1} (α+1)³·√8·3^{α/2}·q^{(1−α)/2}, e(s) := ⌊2s/5⌋ − ⌈(s−1)/2⌉ ≤ 0, and K is
nonincreasing in q.
*Proof.* Case B, per pattern (s; a, z, y, t) of (B^{k=1}), oriented a ≤ b (R226 repair m-4: w ↔ C, E ↔ E' symmetry; for a > b use
the C-versions of R3, R4; the orientation gives t = s − σ below and deg(T^s + m'w²) = s): routes R1 (v, then an ordered triple factorisation of T^s + v:
≤ q^t·3^s), R2 ((m', g'), then a monic divisor E of 1 + T^s m'g'², degree ≤ 3s since y + z ≤ s: ≤ q^{y+z}·2^{3s}), R3 ((w, g'),
E ∣ g'T^s + w of degree ≤ 2s: ≤ q^{a+y}·4^s), R4 ((m', w), E ∣ T^s + m'w² of degree s: ≤ q^{z+a}·2^s) — each tuple is
reconstructed from the data and E (Lemma 7.1; E monic in Case B), N* ≤ q^d, and a degree-n polynomial has ≤ 2^n monic
divisors. With σ := a + y + z, t = s − σ and the least pairwise sum of (a, y, z) ≤ 2σ/3, min(t, y + z, a + y, a + z) ≤
min(s − σ, 2σ/3) ≤ 2s/5, hence (integers) ≤ ⌊2s/5⌋: count ≤ 8^s q^{⌊2s/5⌋} per pattern, ≤ 2(s+1)³ patterns with orientation,
mass q^{−⌈(s−1)/2⌉} each. e(s) ≤ 2s/5 − (s−1)/2 = 1/2 − s/10, and e(s) ≤ 0 for all s ≥ 2 (checked for s ≤ 600, and
1/2 − s/10 < 0 beyond). Case A: Lemma 7.2(b) with weight q^{−α}. All exponents of q are ≤ 0, so every term is nonincreasing in q. ∎
**Computation (`scripts/fz1_largeq.py 20`, log `data/fz/largeq_k1.txt`; exact rationals for s ≤ 600, α ≤ 200, geometric tails
via e(s) ≤ 1/2 − s/10, fail-closed against underflow (R226 repair m-5: an underflowing tail is replaced by 1e-300, which is not
an upper bound below e^{−690}; immaterial here; R226's exact-rational re-evaluation `scripts/review_fz1_largeq.py` gives K(3^20) ≤ 4.19188·10⁸)):** K(3^20) ≤ 4.192·10⁸ < 3^20 − 3 = 3.487·10⁹. Hence (Σ_{k=1}) holds for
every q = 3^r with r ≥ 20.

**Theorem 8.1 (A = T, all r ≥ 3; PROVED, computer-assisted).** For every q = 3^r with r ≥ 3, O(q, T) ≠ ∅: ES_q(T, ·) has no finite
linear covering. *Proof.* 3 ≤ r ≤ 19: Theorem 7.3. r ≥ 20: Lemma 7.4. (Cross-check: `fz1_certify.sh 20 30` with the overflow-safe
helpers also certifies r = 20..30 directly, totals ≤ 9.0904 < q − 3; `data/fz/certify_k1.txt`.) ∎
*Implementation note.* `init_omstar`/`init_rankin` (fz_sum.c) and `init_rankin` (fz_tail.c, fz1_tail.c) now take q as a floating
type (they took a C int, which overflowed for r ≥ 20 — the reason Thm 7.3 stopped at r = 19). The change is value-preserving for
the certified cases: fz_sum 3 80 (3.018043069489), fz_hybrid q = 9 (3.287220339594), fz1_sum 4 80 (24.81244341985) and
fz1_tail 4 80 (3.3028636616·10⁻⁵) are reproduced to all printed digits.
**Status of ES_q(T^k) for q = 3^r (with (J)51 and this file):** no finite linear covering for k ≥ 2 and every r ≥ 2 (Thms 3.1, 5.2 +
(J)51), and for k = 1 and every r ≥ 3 (Thm 8.1). Open here: q = 3 with k ≥ 2 (Conjecture 0.2), and q = 9 with k = 1 (§7: exact counts give
≈ 4.6 < 6, EVIDENCE; the bounds beyond s ≈ 19 are too weak) — the latter is now closed by FF_ODD_ABSENCE Thm 2.2 (O226;
reviews R240, R241), so k = 1 holds for every r ≥ 2 (FF_ODD_ABSENCE Cor 2.3) and only q = 3, k ≥ 2 remains open. q = 3 with k = 1 has a finite covering ((J)4).
