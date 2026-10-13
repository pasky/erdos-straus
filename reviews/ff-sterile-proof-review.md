# Review R179 of FF_STERILE_PROOF.md (O179) — hostile, round 1

**Repairs applied:** D1–D10 applied directly to FF_STERILE_PROOF.md as "(R179 repair)" notes (author quiet since
commit 714d5b7c). The author's text is otherwise unchanged; the report AGENT_REPORT_O179.md is not edited (its SHARP 1–3
wordings are covered by D1–D3 and D8).

Reviewer: R179. Document reviewed: FF_STERILE_PROOF.md at merge of side-agent/ff-sterile-proof (report
reviews/agent-reports/AGENT_REPORT_O179.md). From-scratch scripts: `scripts/review_fsp_poly.py` (own F_q[T]
arithmetic incl. irreducibility test and Cantor–Zassenhaus factorisation), `scripts/review_fsp_enum.py`,
further `scripts/review_fsp_*.py` listed per claim. Nothing here concerns ES over Z.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (one-sided form), Lemma 1.2 (cylinder = rational approximation) | SOUND |
| Lemma 2.1 (genus parity) | SOUND (but not new: it is FF2 §3's R166-checked parity plus arithmetic; see D-list) |
| Lemma 3.1 (π-weights, π-free families) | SOUND |
| **Thm 3.2 (O(q, A) Haar-null)** | **SOUND** (true, short, essentially the classical almost-all mechanism of FUNCTIONFIELD_ES Thm 5.3 in profinite form; consequence (a) needs a scope sentence) |
| §0 "u ≡ 1 (T²) covered by E = −1; these are the only interesting slice points" | first half SOUND; second half GAP (D4) |
| §4 (i)–(iii) at x*_c | (i) SOUND (R166); (ii) CLAIMED from O173, not re-derived (D5); (iii) SOUND |
| §4 residual problem (exact reformulation) | SOUND (the "exactly B2" gloss is Assessment, D6) |
| §4 cyclotomic structure (r const ⇒ K even; splits ⇒ solutions) | SOUND |
| §4 cyclotomic EVIDENCE K ≤ 149 | SOUND-AFTER-REPAIRS (reproduced exactly for 15 ≤ K ≤ 80; SKIP accounting/pattern wording, D7) |
| §5 measure table and 1/3 + 2/27 + 4/81 decomposition | SOUND (reproduced exactly K ≤ 12 from own solution list) |
| §5 "no sign of an exact 1/2" | overstated Assessment (D8) |
| §5 "no quadratic-character mechanism (PROVED)" | SOUND-AFTER-REPAIRS: true only in the narrow group-character sense; wording/labels (D10) |
| §5 clopen remark | SOUND (trivial) |
| §5 "near-x* zero coverage is ultrametric triviality" | FALSE as stated for K ≥ 7 (D9) |
| §6 counting bounds / square-root barrier | SOUND (as a statement about these parametrisations) |

## Lemma 1.1 / 1.2 — SOUND
Re-derived. (⇒) E′r = TH′L′r − r = H′L″(H + H′) − r = HH′L″ + H′²L″ − r = T^K + H′²L″ using (I), (II) and
L′ = g′L″. (⇐) as written. Lemma 1.2: H′(1 − THL′) = H′ − T g′ HH′L″ ... = −H − T^{K+1}g′ (asserted on every
enumerated solution in `review_fsp_enum.py`); EE′ = D = 1 + T^{K+2}g′²L″ (asserted on every solution).
**Independent enumeration.** `review_fsp_enum.py` enumerates by the *one-sided* route of Lemma 1.1 (choose
H′, g′, L″, test E′ | T^K + H′²L″, recover H) — a different search from the author's (H, H′) route. Solutions
with a ≥ b are found directly (bound b + deg g′ + λ ≤ K − 1 from deg r = K − 1 − (b + deg g′ + λ)); a < b
solutions are their H ↔ H′ swaps. Result for K ≤ 12: 226 solutions, **set-identical** to `fsp_enum.py 12`
(sorted line-by-line `cmp`), per-K counts 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104 (K = 2..12). Note: the
document's "cyclotomic counts 2, 6, 8, 12, 4, 72, 4" are the r-constant subcounts, not these totals.
**K ≤ 14 run** (`review_fsp_enum.py 14`, log `data/review_fsp_enum14_log.txt`, list `data/review_fsp_enum14.txt`):
312 solutions, set-identical to `fsp_enum.py 14` (the document's 312), per-K 48, 38 at K = 13, 14.

## Lemma 2.1 (genus parity) — SOUND; attribution needs repair
Re-derived step by step: D = EE′ = 1 + T^{K+2}g′²L″ = 1 + MY² with (M, Y) as stated; for π | E, π ∤ MY (else
π | 1), so −M ≡ Y^{−2} is a nonzero square mod π and (−M/E) = 1 (E monic of degree 1 + a + l ≥ 1, E(0) = −1).
In F₃[T] ((q − 1)/2 = 1): (A/B)(B/A) = (−1)^{deg A deg B}; (−1/B) = (−1)^{deg B} since (3^d − 1)/2 ≡ d (mod 2);
(T/B) = (−1)^{deg B}(B(0)/3); (2/3) = −1. (E/L″) = (−1)^λ since L″ | L′ | E + 1. Hence
K even: (−1)^{deg E + λ + λ deg E} = 1 ⟺ (1 + deg E)(1 + λ) odd ⟺ deg E, λ even;
K odd: (−1)^{deg E + (deg E + 1) + λ + λ deg E} = 1 ⟺ λ(1 + deg E) odd ⟺ λ odd, deg E even. Same for E′.
Consequences a ≡ b, a + b ≡ 0, l ≡ a + 1, λ ≡ K (mod 2) follow from deg E = 1 + a + l, deg E′ = 1 + b + l,
K = a + b + λ. deg r ≡ K: re-derived (cases a > b, a = b (leading coefficient 1 + 1 = 2 ≠ 0), a < b).
Check (from scratch, independent solution list): K ≤ 14, 312 solutions, **0 violations** of deg E, deg E′ even,
λ ≡ K, deg r ≡ K; classes (a, b, λ, K mod 2): (0,0,0,0) 112, (1,1,0,0) 88, (0,0,1,1) 84, (1,1,1,1) 28 — exactly the
document's numbers.
Note that the hypothesis "on the slice (u(0) = 1)" is not used: E(0) = E′(0) = −1 holds for every solution of
(I), (II) by definition of E, E′. Only the identification of solutions with families needs the slice.

## Lemma 3.1 (π-weights) — SOUND
Re-derived. AL | P + E with x a unit gives gcd(E, AL) = 1, so mod E: P ≡ π, X ≡ π/A, X/L ≡ π/(AL), and the four
types are ≡ a₀, πa₀, π/(Aa₀), π²/(Aa₀) (weights 0, 1, 1, 2). Equal weights: E | s reduces to E | a₀ + b₀,
E | L/a₀ + L/b₀ (types 2,2 and 3,3, using X/L a unit mod E) or E | 1 + Aa₀b₀ (types 1,2), no π. Weight difference 1
(types (0,1), (0,2), (1,3), (2,3)): linear in π; (0,3): π² ≡ −Aa₀b₀. lc(s) = 1 for distinct types once n ≥ n_F
(Lemma 6.2). Correct.

## Theorem 3.2 (O(q, A) is Haar-null) — SOUND
*Setting.* R̂ = lim F_q[T]/W = ∏_ℓ O_ℓ (CRT), R̂^* = ∏_ℓ O_ℓ^*, Haar = product of the normalised Haar measures;
O(q, A) is closed (FF2 §0.1: complement = union of the clopen validity sets V_F), hence Borel. Fine.
*Family.* F_ℓ = (ℓ; 0, 1; 2, 1): a = 1, b = X, s = 1 + X, n_F = 1 + max(k, deg ℓ). Valid ⟺ A | P + ℓ and
ℓ | 1 + X ⟺ ℓ | A + P + ℓ (A invertible mod ℓ) ⟺ P ≡ −A (mod ℓ); lc(s) = lc(X) = 1 = lc(ℓ) since n > k; s ≠ 0.
ℓ ≡ −κ (mod A) with κ a unit forces ℓ ∤ A. Checked from scratch (`scripts/review_fsp_thm32.py`, log
`data/review_fsp_thm32_log.txt`): for (q, A) ∈ {(3, T²), (5, T), (3, T² + 1), (2, T³)}, all monic P of one degree
n and all irreducible ℓ ∤ A of degree ≤ 2 (≤ 3 for q = 2), 15 337 pairs: generic validity (FUNCTIONFIELD_ES §6.2
definition) ⟺ the two congruences, and in every valid case A·XYZ = P(XY + YZ + ZX) holds with monic X, Y, Z of
degree ≥ n − k. (Includes q = 2: the theorem's "every q" is fine, NC being checked.)
*Probability.* B_ℓ = {x_ℓ ≡ −A (mod ℓ)} depends only on the ℓ-component; −A is a unit mod ℓ, so μ(B_ℓ) =
1/(|ℓ| − 1). The κ-event lives on the components at primes of A, disjoint from all ℓ, so conditioning on κ is
harmless; the B_ℓ are mutually independent (product measure) — full independence, not just pairwise, so BC-II
applies verbatim. Divergence: #{ℓ monic irreducible, deg ℓ = e, ℓ ≡ −κ (A)} = q^e/(Φ(A)e) + O((k + 1)q^{e/2}/e)
(prime polynomial theorem in progressions, Rosen, *Number Theory in Function Fields*, Thm 4.8 — **not accessed
by me** (no copy in sources/); FUNCTIONFIELD_ES Fact 5.2 cites the same standard result). Even Dirichlet's
theorem in analytic form (L(1, χ) ≠ 0) suffices for divergence of Σ 1/|ℓ|. Numerically (q = 3, A = T²,
`review_fsp_thm32.py`): S(e) = Σ_{deg ℓ ≤ e} 1/(|ℓ| − 1) per class grows by ≈ 1/(6e) per degree (≈ (H_e)/Φ(A),
Φ(T²) = 6) for all six unit classes κ; e.g. e = 11: S ∈ [0.24, 0.86].
*Conclusion.* For each of the Φ(A) classes κ, a.s. infinitely many F_ℓ are valid; a finite union of null sets
is null. ∎ Correct as stated, including "for every q and every monic A of positive degree".
*Consistency with earlier statements* (all checked, no contradiction):
* O140 Prop 4.1 (1 ∈ O for char ≥ 5): a nonempty null set. Direct check: F_ℓ at x = 1 needs ℓ ≡ −1 (A) and
  ℓ | A + 1; deg ℓ ≤ k with ℓ monic ≡ −1 (A) forces ℓ = A − 1, and A − 1 ∤ A + 1 (difference 2). So no F_ℓ is valid
  at 1, as it must be.
* FF2 §0.1 tree plateau ≈ 1 % (R166 D11): O null ⇒ for every ε finitely many families cover mass ≥ 1 − ε (inner
  regularity), so the plateau must eventually fall with NTH → ∞. But see D2: the theorem gives **no rate**; the F_ℓ
  family alone leaves uncovered mass ∏(1 − 1/(|ℓ| − 1)) ≈ e^{−S(e)} ≍ e^{−1/6} at deg ℓ ≤ e (computed: 0.35–0.79
  per class at e = 11), so F_ℓ alone would need astronomically large ℓ to beat 1 %.
* FF2 §0.2 / (J)14 positive *slice* measure: the slice {x ≡ 1 off T} has Haar measure 0 in R̂^*, and the slice
  measure is a different measure; O ∩ slice may have positive slice measure while O is Haar-null. No conflict;
  DISCOVERIES (J)14 already states this. Thm 3.2 does **not** decide FF2 §0.2's slice alternative ("positive
  measure inside this slice" vs "empty or null") — see D2.
* FUNCTIONFIELD_ES Thm 5.3 (failure proportion ≤ (Φ(A) + o(1))/log n) is the same mechanism (one prime g in a
  progression dividing a shift of P, BC/second-moment); Thm 3.2 is its measure-theoretic profinite form. The
  "PROVED, ~5 lines" headline is accurate, but novelty is low (D3).
*Integer analogue (sanity).* Over Z the same argument (ℓ ≡ −x (mod 4) prime, x ≡ −4 (mod ℓ); a = 1, b = X =
(n + ℓ)/4, ℓ | 1 + X) shows the Mordell/linear-family obstructed set in Ẑ^* is Haar-null. That is weaker than the
known "almost all n" theorems (Vaughan 1970: exceptions ≤ N exp(−c(log N)^{2/3})) and says nothing about every
prime. The document makes no integer claim; the report's spark correctly guesses "probably just a restatement".
No overclaim.

## §0 remark on slice points
u ≡ 1 (mod T²): the family (−1; 0, 1; 0, 1) (a = b = 1, s = 2 = lc E, κ = 1, Y = Z = PX) gives
1/X + 2/(PX) = (P − 1)/(PX) = T²/P in char 3 — SOUND. But "so these [u = 1 + Tv, v(0) ≠ 0] are the only
interesting slice points" ignores u(0) = 2. The family (1; 0, 1; 2, 1) covers u ≡ 2 (mod T²) (A | P + 1, s = 1 + X),
leaving u = 2 + Tv, v(0) ≠ 0, which FF2 §0.1 listed among the uncovered candidates (2 + T + T², 2 + 2T + T², …).
Lemma 2.1 does not apply there (E(0) = +1 changes (T/E)). See D4.

## §4 at x*_c
(iii) re-derived: covering gives E ≡ −(1 + cT) (mod T^{N+1}); deg E ≤ N forces E = −(1 + cT), non-monic for c = 1
and of odd degree 1 for c = 2. deg E′ ≤ N: E′ ≡ −(1 + cT)^{−1}, so (1 + cT)E′ + 1 = μT^{N+1}; deg E′ < N is
impossible ((1 + cT)E′ = −1), so deg E′ = N, μ = c, and the root T = −c gives c(−c)^{N+1} = 1, i.e. c = 1, N odd,
deg E′ = N odd — excluded by Lemma 2.1. SOUND.
Residual problem: the covering condition at level N is v ≡ −HL′ (mod T^N) (Lemma 1.2), weakest at
N₀ = ⌈K/2⌉ + 1; Case A is excluded at x*_c (R166); at x*_c every family is Case A or B (FF2 (F2)). Nonzero constant
terms of H, H′, L″ are forced by H g′L″ ≡ −c (mod T). The counterexample K = 2, H = T + 2, H′ = T + 1 checked by
hand: H + (1 + T)H′ = T² ≡ 0 (mod T²), but HL′ + 1 = T, v_T = 1 < 2, and the family covers u ≡ 1 + T + 2T² (mod T³).
SOUND. K = 1 has no solutions (checked by hand and in the enumeration), so "K ≥ 2" loses nothing.
Covers of x*_c among the reviewer's own 312 solutions with K ≤ 14: **none** (consistent with R175/O175).

## §4 cyclotomic sub-family
Structure SOUND: deg r ≡ K (Lemma 2.1) ⇒ r constant only for even K; every split of T^K + r₀ with
H + H′ = r₀Tg′ (g′ monic, g′(0) ≠ 0) is a solution ((II) is the split, (I) by construction). Own counts
(`review_fsp_cyclo.py 2 14`, own Cantor–Zassenhaus factorisation, every factor re-tested irreducible and the
product re-multiplied): 2, 6, 8, 12, 4, 72, 4 for K = 2, 4, …, 14, matching the deg r = 0 rows of the reviewer's
independent full enumeration (K ≤ 12) and the document. Odd K: 0, as predicted.
**Independent re-run of a subrange** (`review_fsp_cyclo.py 15 80 300000`, log `data/review_fsp_cyclo_K15_80.txt`):
all 66 levels 15 ≤ K ≤ 80 agree with `data/fsp_cyclo_K15_150.txt` field-by-field (n and best z for c = 1, 2, and
the same SKIP pattern at cap 3·10⁵); no hit; best z = 12 vs N₀ = 14 at K = 26 (r₀ = 2), reproduced. Over the full
author log the maximum elsewhere is 13 at K = 142 (needed 72), then 9 (K = 148); see D7 for wording and SKIP
accounting.

## §5 measure
`review_fsp_measure.py` on the reviewer's own K ≤ 12 solution list (exact rationals, maximal cylinders,
normalised Haar on v with v(0) ≠ 0): 1/3 (K ≤ 4), 11/27 (K = 5..7), 37/81 (K = 8, 9), 113/243 (10), 343/729 (11),
349/729 = 0.4787 (12), 1051/2187 = 0.4806 (13), 1057/2187 = 0.4833 (14; log `data/review_fsp_measure14_log.txt`) —
identical to the table; 1/3 = two depth-2 cylinders (prefix (c, 2)), +2/27 = four depth-4
cylinders, +4/81 = eight depth-5 cylinders. Extrapolation: the two-level increments 0.0137, 0.0101, 0.0045,
0.0039, 0.0016 have successive ratios 0.74, 0.45, 0.85, 0.41; a geometric tail with ratio 0.5 / 0.6 / 0.7 / 0.85
gives 0.4922 / 0.4930 / 0.4943 / 0.4997. The data do not distinguish 0.493 from 1/2 (D8).
Near x*: on the reviewer's K ≤ 12 data, the neighbourhood v ≡ c (mod T⁴) (i.e. u ≡ 1 + cT mod T⁵) meets **no**
cylinder, although cylinders of depth 5 and 7 (K = 8, 12) meet v ≡ c (mod T³). Since depth-5..7 cylinders could
sit inside the T⁴-neighbourhood without containing x*, this emptiness is a genuine observation, not
ultrametric triviality (D9).

## §6 counting
Re-derived: with ρ = deg r, (a) r (≈ 3^ρ choices) and a divisor triple of T^K + r (3^{o(K)} by the divisor
bound) fix the solution; (b) for a ≥ b, b + deg g′ + λ = K − 1 − ρ, so (H′, g′, L″) ranges over ≤ 3^{K−1−ρ}·K²
triples (this is the bound the reviewer's enumerator uses); a < b by the H ↔ H′ swap. min(ρ, K − 1 − ρ) ≤ K/2,
against cylinder mass 1/(2·3^{N₀−1}) ≈ 3^{−K/2}: no decay. The tail formula and the union-bound sufficient condition
are correct, and the document correctly notes that Case A must also be excluded on the region used. SOUND as a
statement about these two parametrisations (it is not a lower bound on #sol).

## Defects (no FATAL, no MAJOR; 10 MINOR)

**D1 (MINOR, attribution/overclaim) — §2 Lemma 2.1, report SHARP 2, §5 "this closes R175 D7".** The core of
Lemma 2.1 (deg E, deg E′, deg D even, at every slice point with u(0) = 1) is FUNCTIONFIELD_ES2 §0.2
"Necessary condition from quadratic reciprocity (PROVED, q = 3)", re-derived and checked by R166; R175's D7 repair,
already applied in SIGNLAYER_DEEP Lemma 3.1, cites exactly that. So Lemma 2.1 does not "supply the missing step"
of R175 D7: that step was supplied when D7 was repaired. The new content is a corollary: a ≡ b, l ≡ a + 1,
λ ≡ K, deg r ≡ K (mod 2), hence cyclotomic solutions only at even K. *Repair:* state "Lemma 2.1 (FF2 §0.2's
reciprocity parity, R166-checked, re-derived here, plus the corollaries λ ≡ K, deg r ≡ K)"; drop "closes R175 D7"
(say "consistent with the R175 D7 repair"). Also note that the hypothesis u(0) = 1 is used only to identify
solutions with families: E(0) = E′(0) = −1 holds for every solution of (I), (II).

**D2 (MINOR, scope) — §3 Consequence (a), report SHARP 1 ("settles R166 D11").** What Thm 3.2 settles is the
R̂^*-mass question raised in R166 D11 (the ≈ 1 % ffl_tree plateau cannot be a positive-measure obstruction; by
inner regularity finitely many families cover mass ≥ 1 − ε for every ε). It does **not** settle FF2 §0.2's own
alternative, which is about *slice* measure ("O(3, T²) has positive Haar measure inside this slice" vs "empty or
null"): the slice is Haar-null. The theorem also gives no rate: F_ℓ alone leaves uncovered mass
∏(1 − 1/(|ℓ| − 1)) ≍ e^{−1/6} at deg ℓ ≤ e (computed 0.35–0.79 per class at e = 11), so it says nothing about
when the plateau must fall. *Repair:* "Settles R166 D11's R̂^* question: O(3, T²) is Haar-null, so the plateau
is not a positive-measure obstruction (no rate is given). FF2 §0.2's slice-measure alternative remains open."

**D3 (MINOR, novelty) — §3 Thm 3.2 framing, report SHARP 1.** The theorem is correct, but it is the
measure-theoretic profinite form of FUNCTIONFIELD_ES Thm 5.3's mechanism: one prime in a progression mod A dividing a
shift of P, plus a second-moment/Borel–Cantelli argument. Over Z the same 5-line argument shows that the
linear-family obstructed set in Ẑ^* is Haar-null, which is weaker than Vaughan's "almost all n" theorem. *Repair:*
add one sentence: "Profinite form of the classical almost-all mechanism (cf. FUNCTIONFIELD_ES Thm 5.3); new only
as a statement about O(q, A)." Cite the prime polynomial theorem in progressions (Rosen Thm 4.8 / FUNCTIONFIELD_ES
Fact 5.2) explicitly; Dirichlet's theorem in analytic form already suffices for divergence.

**D4 (MINOR, unsupported dismissal) — §0, "so these are the only interesting slice points".** Slice points with
u(0) = 2 are ignored. u ≡ 2 (mod T²) is covered by (1; 0, 1; 2, 1), but u = 2 + Tv with v(0) ≠ 0 is neither treated
nor shown covered, and FF2 §0.1 listed such lifts (2 + T + T², 2 + 2T + T², 2 + 2T + 2T²) as uncovered candidates.
Lemma 2.1 does not hold there as stated (E(0) = +1). *Repair:* "Here we treat the sub-slice u ≡ 1 (mod T); the
points with u(0) = 2, u ≢ 2 (mod T²), are not treated."

**D5 (MINOR, label) — §4 "What is proved at x*_c (all PROVED; the first two are O173/O175 results re-derived)".**
(ii)'s window (N + 1)/4 ≤ l ≤ 2N − k − 1 is O173 Lemma 2.3. O173 is under parallel review (R173), and the document
does not re-derive it. *Repair:* "(ii) … (O175 Lemma 3.2, R175-checked; O173 Lemma 2.3, CLAIMED pending R173)".

**D6 (MINOR, label) — §4 residual problem, "exactly the integer divisor-class problem B2".** The reformulation is
PROVED. The identification with B2 is an analogy (Assessment). *Repair:* add "(Assessment: analogue of B2)".

**D7 (MINOR, EVIDENCE accounting) — §4 cyclotomic search and report.** (a) 10 of the 47 SKIPped (K, r₀) pairs are at
odd K (91, 117, 121, 123, 143; both r₀). By Lemma 2.1 these have no cyclotomic solutions, so the genuinely
unexamined set is **37 pairs at 29 even levels**. (b) The pattern "T^K + 1 has cyclotomic solutions at K = 4, 12,
20, …, 136, 148 (mostly K ≡ 4 mod 8)" is read off an incomplete list: r₀ = 1 is SKIPped at the even levels
K = 60, 84, 120, 122, 130, 132, 140, 146 (60, 84, 132, 140 are ≡ 4 mod 8). (c) "elsewhere ≤ 13 against needed ≥ 72"
is garbled. The correct reading: apart from K = 26 (z = 12 vs 14), the best is z = 13 at K = 142 (needed 72), then
z ≤ 9. *Repair:* reword (a)–(c) accordingly; optionally prune odd K by Lemma 2.1.

**D8 (MINOR, overstated Assessment) — §5 "no sign of an exact 1/2", report SHARP 3.** The two-level increment
ratios are 0.74, 0.45, 0.85, 0.41, which is erratic. A geometric tail at the largest observed ratio (0.85) gives
0.4997, and 0.5–0.7 gives 0.492–0.494. The finite data cannot distinguish a limit ≈ 0.493 from 1/2. *Repair:*
"extrapolations give 0.492–0.500 depending on the assumed ratio; the data neither support nor exclude an exact
1/2". Keep the exact decomposition 1/3 + 2/27 + 4/81 + tail, which is correct.

**D9 (MINOR, false dismissal) — §5 last bullet, "Near x*_c coverage is zero up to the depth at which x*_c is known
uncovered … ultrametric triviality. This is all R175's 'far below 49 %' says."** Ultrametricity only forces this
for cylinders of depth ≤ the neighbourhood depth. R175's statement (zero coverage inside u ≡ 1 + cT (mod T⁵) for
K ≤ 13) includes all families with N₀ + 1 > 5 (K ≥ 7). Their cylinders could lie inside the neighbourhood without
containing x*, so the emptiness is a genuine observation. Reviewer check: among the K ≤ 12 cylinders, those of
depth 5 and 7 meet v ≡ c (mod T³) but none meets v ≡ c (mod T⁴). *Repair:* "for families of level N ≤ 4 (cylinder depth ≤ 5) this is
ultrametric triviality; for deeper families (K ≥ 7) R175's observation is a genuine (EVIDENCE) local deficit near x*."

**D10 (MINOR, wording/label) — §2 Remark and §5 "No quadratic group character produces it (PROVED)".** What is
proved is narrow: (i) the pro-3 group 1 + TF₃[[T]] has no nontrivial continuous ±1-valued character; (ii) local
quadratic (Hilbert) symbols at T see only u(0). Both are immediate. "The only such character of the slice is
v(0) = c" is wrong as phrased. u ↦ v(0) is an F₃-valued homomorphism on 1 + TF₃[[T]], and the sign of c is a
function on the sub-slice v(0) ≠ 0, which is not a group. "No quadratic character (Legendre/genus) can split the
slice into covered/uncovered halves" goes beyond (i)–(ii). Global Jacobi symbols of u-dependent data, such as FF2's
((1 + cT)/E), are not local characters at T. FF2 only *tried* some and found them consistent. *Repair:* keep (i)–(ii)
as PROVED and label the broader "no genus mechanism" as Assessment. Replace "the only such character … is v(0) = c"
with "the only ±1-valued invariant visible to quadratic symbols at T is the sign of v(0) = c".
