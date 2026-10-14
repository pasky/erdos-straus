# FF_STERILE_SMALL — the small-q sterility cases: q = 27 (r = 3), q = 9, and A = T (k = 1) (O220, wave Y-f)

Status: checkpoint 1 (O220): Theorem 3.1 (q = 27) PROVED (computer-assisted, certified as O216); q = 9 and A = T open. **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in DISCOVERIES.md.
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
triples of a *single* polynomial T^{s−2} + v₁, computable exactly by factoring) and by z = 0 patterns. Not attempted yet.
At q = 3, (Σ) fails even with exact counts (FF_STERILE_PUSH §5: 94/27 > 2), so no union bound of this kind can work there.
