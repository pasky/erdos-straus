# Review R53 of EXCEPTIONAL_SPW2.md (O53, branch side-agent/weak-spw)

Reviewer: hostile side agent (branch side-agent/review-spw2). Reviewed
version: side-agent/weak-spw at ef0bfbd (merged into this branch).
Checked against EXCEPTIONAL_SPW.md (SPW1; Lemma 1.4, Thm 3.2, Lemma 3.1),
EXCEPTIONAL_INTERFREQ2.md (IF2; Def 1.2, Flat, Thm 5.2 + proof, Prop 9.1),
EXCEPTIONAL_KARY3.md §4.3. From-scratch scripts: scripts/review_spw2_*.py.

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| Lemma 1.1 (requirement) | **SOUND-AFTER-REPAIRS** — bookkeeping exact; "exact requirement"/"σ = N^{−c} gives nothing" overclaims necessity (M1); unstated hypothesis-free use of Thm 5.2 (m1) |
| Lemma 2.2 (near zone) | **SOUND** (remark: IF2 not SPW1 Lemma 9.3; K ≥ 3/2 is C = 2-specific) |
| Lemma 2.3 (interval support) | **SOUND**, and sharp (exact rank); "D ≥ 12–13" wrong (true: D ≥ 19 / N ≥ 38) |
| Thm 3.1 (K-free edge bound) | **SOUND** (constant m₀² → m₀(m₀+1)); proof chain verified numerically |
| Lemma 4.1 (dual) | **SOUND-AFTER-REPAIRS** — duality verified by independent LPs; ℤ ↔ ℤ/Q′ transfer mis-cited (m10) |
| EVIDENCE / Assessment | numbers reproduce; two "L ≈ N²/2" entries not computed; decay-rate reading of lower bounds overreaches (m11–m13) |

No FATAL defects. One MAJOR (wording/label), thirteen MINOR.

## Defects

**M1 (MAJOR, label/overclaim) — Lemma 1.1 title, third bullet, closing
paragraph of §1; AGENT_REPORT_O53 "This answers … : no."** Lemma 1.1 is
a sufficient condition obtained along one chain (Lemma 1.4 → Prop 9.1 →
Thm 5.2); necessity of log(K/η) = O((log N)^{3/4}) is not proved, so
"exact requirement" and "polynomially small σ does *not* suffice for anything
ES-relevant" are unproved. *Repair:* rename "requirement of the Prop 9.1 /
Thm 5.2 route"; bullet 3: "this route then gives only B ≥ N^{1−c−o(1)}";
add one line saying a different minorant construction might lose less.

m1 — Lemma 1.1 proof: Thm 5.2 is stated with t, 1/Δ ≥ e^{−S_A}; Lemma 1.1
uses it without. Valid (t, Δ enter only via the trivial case and the last
line; mean side independent of both) — add this as an explicit remark/lemma.
m2 — Lemma 1.1: s₀ = η/(4K), so the hypothesis is η/K ≥ 4N^{−A₁} (or A₁ → A₁+1).
m3 — Lemma 1.1: the (log log N)^{3/4}-free exponent depends on the KARY3 §4.3
pointer, which does not list IF2 Thm 5.2 and is itself unreviewed; label
"conditional on KARY3 §4.3" or keep the log log factor.
m4 — §2 after Lemma 2.2: "SPW1 Lemma 9.3" → "IF2 Lemma 9.3".
m5 — same place: "K ≥ 3/2" is the C = 2 value of max_q c/(k − c); at C = 3/2 it
is 4 (`review_spw2_nearzone.py`). State C = 2.
m6 — §2: "σ = η/(2K) ≍ 1/log N" → "≲ m₀²/(η log N)"; also note the paragraph is
superseded by Thm 3.1.
m7 — Lemma 2.3 note: "Φ(D) > 3N already for D ≥ 12–13" false (Φ(12) = 46 < 72);
correct: D ≥ 19; Φ(D) ≥ 3N + 2 for all N ≥ 38. Title's N > 40 is right for
C = 2; state C = 2 (general: Φ(D) ≥ (2C−1)N + 2).
m8 — Lemma 2.3: "length ℓ" must mean ℓ integer points (with span the bound
is off by one; the lemma is sharp).
m9 — Thm 3.1 (a) and (3.1): Σ_{|k|<m₀}|k| = ⌈m₀⌉(⌈m₀⌉−1) can exceed m₀²;
replace 4πm₀² by 4πm₀(m₀+1). Asymptotics unchanged.
m10 — Lemma 4.1: specify Q′ and replace the SPW1 Lemma 1.1 citation by the
K = ∞ lift (ρ(class) ≤ N, T ≥ CN²/ε′; no 1/2-clipping needed).
m11 — §4 numerics: N = 50 (0.78) and N = 80 (≈ 0.75) are not runs at
L ≈ N²/2; finite-L values are lower bounds and cannot evidence a decay rate.
m12 — §2: RSPW(2, 0.82, K ≈ 1.6) mixes two runs.
m13 — report headline "numerics favour weak SPW": Assessment at most, given
SPW1 §2's warning about small-N LPs.

## Bottom line

All PROVED items survive (Lemma 1.1 as an implication, Lemmas 2.2, 2.3,
Thm 3.1, Lemma 4.1). The quantitative content that matters downstream —
the route needs log(K_N/η_N) = O((log N)^{3/4}) and RSPW margins are only
forced below (log N)^{−1/3} — is correct. What is *not* established is
that the route's requirement is necessary (M1).

Scripts: scripts/review_spw2_{nearzone,interval,thm31,dual,rspw_lp,sawtooth}.py.

## Claim 1: Lemma 1.1

Re-derivation (independent).
1. SPW1 Lemma 1.4 mix R = (1 − 1/(2K))λ_N + R′/(2K) (needs only K ≥ 1/2 for
   R ≥ 0). Full class s (modulus e > CN ≥ N, one point of [1,N]):
   λ_N(s) = 1, so R(s) ≤ 1 − η/(2K). Sparse: R(s) ≤ 1/2 ≤ 1 − η/(2K) since
   η ≤ 1/2 ≤ K. Medium: λ_N(s) = c(s) so |R(s) − c(s)| = |R′(s) − c(s)|/(2K)
   ≤ Δ′/(2K). (P1) is convex. So SPW(C, σ = η/(2K), Δ₀ = Δ′/(2K)), σ ≤ 1/2.  ✔
   (The index sets (D, CN] and (N/2, CN] coincide for D = ⌊N/2⌋.)
2. IF2 Prop 9.1: θ = σ/(2(σ + τ + 1/(2C))), t = θ/2, s₀ = σ/2, Δ = 6θ + Δ₀.
   Since σ ≤ 1/2 and τ = O(1): 1/t = 4(σ + τ + 1/(2C))/σ ≤ c_C/σ, so
   log(1/t) ≤ log(K/η) + O_C(1). Δ ≤ 3 + Δ′/(2K), so
   log(1 + Δ(1+c)) ≤ log(1+c) + log 4 + log(1 + Δ′/K).  ✔ (bookkeeping right)
3. IF2 Thm 5.2 as *stated* assumes t ≥ e^{−S_A} and Δ ≤ e^{S_A}. Lemma 1.1
   applies it with no such hypothesis (its third bullet is precisely the
   regime t = N^{−c}). I re-read the proof of Thm 5.2: t enters only through
   the trivial case "KB ≥ tN" and the final line (1+Δ+Δc)B ≥ tNe^{−S′};
   the high-mass bound T_{>CN} < tN/s₀ + N needs only t ≤ 1, and the mean
   side (level λ ≤ (A + A₁ + 2)log N + S + λ₀) does not see t or Δ. So the
   hypotheses t, 1/Δ ≥ e^{−S_A} are cosmetic (they only make the conclusion
   "3/4-shaped") and the strengthened use is VALID — but it is an unstated
   extension of a cited theorem (defect m1).
4. s₀ = σ/2 = η/(4K), so the needed hypothesis is η/K ≥ 4N^{−A₁}, not
   η/K ≥ N^{−A₁} (absorb by A₁ → A₁ + 1). Trivial (m2).
5. The exponent "C′(log N)^{3/4}" without (log log N)^{3/4} relies on
   KARY3 Thm 4.1 replacing K2 Thm 5.1 inside IF Thm 2.5's mean side. KARY3
   §4.3 lists INTERFREQ Cor 2.3 at *pointer level, not re-reviewed*, and does
   not list IF2 Thm 5.2 at all. With level containing +S the self-consistent
   bound S ≤ C(c log N + S)^{3/4} ⇒ S = O((log N)^{3/4}) is fine, so I believe
   it, but the label should say "conditional on KARY3 §4.3 pointer" (m3).
6. "Exact requirement" / "polynomially small σ does *not* suffice for
   anything ES-relevant": Lemma 1.1 is a *sufficient* condition (an upper
   bound on the saving obtainable via this particular chain
   Lemma 1.4 → Prop 9.1 → Thm 5.2). Nothing is proved about necessity:
   a different mixing than Prop 9.1, or a sharper use of (5.1) than the
   final step, could lose less than log(1/t). The statement "σ = N^{−c} gives
   nothing" is true only as "this chain then yields only B ≥ N^{1−c−o(1)}".
   Overclaimed wording (defect M1).

Verdict Lemma 1.1: **SOUND-AFTER-REPAIRS** (bookkeeping correct; title and
third bullet overclaim necessity; relies on unstated hypothesis-free form of
Thm 5.2 and on the KARY3 pointer).

## Claim 2: Lemma 2.2 (near zone invisible) and its remarks

Re-derivation: a class of modulus e > CN through n₀ ∈ [1,N] has e ≥ ⌊CN⌋ + 1,
so n₀ + e ≥ ⌊CN⌋ + 2 > CN + 1 and n₀ − e ≤ N − ⌊CN⌋ − 1 < N − CN; it meets
[1,N] only at n₀ (e > N). Correct for real C ≥ 1 as well.
From scratch: `scripts/review_spw2_nearzone.py` (exact) — all e ∈ (CN, CN+3N],
all n₀, |j| ≤ 3, C ∈ {3/2, 2, 5/2, 3}, N ≤ 57: no hit. ✔

Remark "SPW1 Lemma 9.3 (σ ≤ 2/5) disappears once K ≥ 3/2": the lemma is
**IF2** Lemma 9.3 (SPW1 has no §9) — m4. The script computes, for every
q ≤ D and b, the single-q local system (c full lifts ≤ 1 − η, k − c sparse
lifts ≤ K, sum = c): feasible at η = 1 iff K ≥ c/(k − c). Max over q, b:
exactly **3/2 at C = 2** (q ≈ 0.4N, c = 3, k = 5), N = 12…200 ✔; but
**4 at C = 3/2** and 3/4 at C = 3. So the "K ≥ 3/2" threshold is
C = 2-specific (m5; state C = 2 or "K ≥ max_q c/(k−c)").

Fejér remark in the same paragraph ("K ≳ η² log N/m₀² forced"): superseded by
Thm 3.1 (K-free); I checked only that ‖T‖_∞ ≤ 4m₀N/e is right. The phrase
"σ = η/(2K) ≍ 1/log N if η fixed" should be "≲ m₀²/(η log N)" (only an upper
bound is proved; also η fixed is itself excluded by Thm 3.1) — m6.

Verdict Lemma 2.2: **SOUND** (remarks need m4–m6).

## Claim 3: Lemma 2.3 (interval support ⇒ R = λ_N)

Re-derivation: f = R − λ_N has zero class sums mod every d ≤ D (d = 1
included, mass N) ⇔ the Laurent polynomial F vanishes at every root of unity
of order ≤ D ⇔ ∏_{d≤D}Φ_d | F, degree Φ(D). Correct.
From scratch (`scripts/review_spw2_interval.py`, exact rank over ℚ): for
D ≤ 8 and every interval of ℓ ≤ Φ(D)+3 integer points (two offsets) the
solution space has dimension exactly max(0, ℓ − Φ(D)). So the lemma is
**sharp**, with the convention that ℓ = *number of integer points*
(span = ℓ − 1). If "length" is read as span (max − min), the claimed
"ℓ > Φ(D)" is off by one (span = Φ(D) admits f = z^a∏Φ_d ≠ 0) — m8: say
"ℓ points".

Numerical side claims:
* "(Φ(D) > 3N already for D ≥ 12–13)" is **wrong**: Φ(12) = 46 < 72. The first
  D with Φ(D) > 3(2D+1) is **D = 19**; Φ(D) ≥ 3N + 2 (the number of points of
  W ∪ Z at C = 2) holds for all N ≥ 38 (checked to 200). The title's "N > 40"
  is therefore correct (slightly conservative) for **C = 2** only; C is
  implicit (m7: fix the parenthetical, state C = 2, general form
  (2C − 1)N + 2 ≤ Φ(D)).
* Consequence "far mass unavoidable": correct — R = λ_N violates RSPW
  (full classes get mass 1), so supp f is not contained in any interval of
  ≤ Φ(D) points, i.e. some mass at distance ≥ (Φ(D) − N)/2 ≈ 0.076N² from W.

Verdict Lemma 2.3: **SOUND** (m7, m8 wording).

## Claim 4: Theorem 3.1 (K-free edge bound η ≲_C (log N)^{−1/3})

Line-by-line re-derivation:
* Pinning: for m₀ ≤ |k| ≤ M, |k| | L_M | e so the character has order
  e/|k| ≤ D, divides e, and is fixed by (P1) ✔. T̂ = K̂(ρ̂ − 1̂_W) supported in
  |k| < m₀ ✔; |T̂| ≤ |ρ̂| + |1̂_W| ≤ 2N (mass N from d = 1) ✔.
* (b) every y ∉ W is at cyclic distance ≥ min(r+1, N−r) = r+1 from
  x_in = 1+r ✔; A = eN/(4(M+1)r²) ✔ (uses only Σρ = N, so no K) ✔;
  T(x_in) ≤ −ηφ(x_in) + A ≤ −η + ητ + A ✔ (η ≤ 1 automatically).
* (c) dist(x_out, W) ≥ min(r+1, e−N−r) = r+1 ✔ (needs r < ((C−1)N−1)/2).
* Final inequality and the r = ⌈NM^{−1/3}⌉ asymptotics (three terms
  O_C(M^{−1/3}), O_C(M^{−2/3}), ≈ 32πM^{−1/3}·(N/2D)²) ✔. Admissibility of r
  needs M^{1/3} ≳ 2/(C−1) — implicit "N large" ✔. Constants depend on C only
  (e ≤ CN + L_M ≤ (C+1)N) and not on K or any other class ✔.
* **Defect m9 (constant).** (a) uses Σ_{|k|<m₀}|k| ≤ m₀², but
  Σ_{|k|<m₀}|k| = m′(m′+1), m′ = ⌈m₀⌉ − 1, which exceeds m₀² when m₀ is just
  above an integer (m₀ = 3.05: 12 > 9.3). m₀ = e/D is generically non-integer.
  Replace m₀² by m₀(m₀+1) (or ⌈m₀⌉²) in (a) and (3.1); asymptotics unchanged.
  (The §2 remark's 8πm₀² is a valid bound since m₀ ≥ 2C > 1.)

From scratch (`scripts/review_spw2_thm31.py`): Fejér pointwise bound and
tail bound checked exactly-in-float for (e, M) ∈ {(120,6), (420,7), (840,8),
(2520,10)}; then an LP on ℤ/e with *exactly* the theorem's hypotheses
(profile mod d | e, d ≤ D; ρ ≤ 1 − η on W only) at (N, C, e, M) = (60, 1.5,
120, 6), (60, 2, 180, 6), (100, 1.5, 180, 6), (84, 2, 420, 7), and every
inequality of the proof chain (Fourier support, |T̂| ≤ 2N, φ tails, T(x_in),
T(x_out), Lipschitz with the true Σ|k|, (3.1)) verified at all admissible r
on the optimiser and on 5 random feasible points each. No violation.
(At these sizes (3.1) is ≫ 1, so this checks the chain, not the rate.)

Labels: "RSPW with fixed η is false for large N even with K = ∞" ✔ (follows).
Verdict Thm 3.1: **SOUND** (m9 constant).

## Claim 5: Lemma 4.1 (dual of RSPW, K = ∞)

Re-derivation. Primal on ℤ/Q′: max η, ρ ≥ 0, (P1), ρ(s) ≤ 1 − η on full
classes (e | Q′, e > CN). Feasible (ρ = 1_W, η = 0) and bounded (η ≤ 1), so
finite LP strong duality applies. Weak duality: for g ∈ V_D, z ≥ 0 with
g + Σz_s1_s ≥ 0: 0 ≤ ⟨ρ, g + P⟩ = Σ_W g + Σz_sρ(s) ≤ Σ_W g + (1−η)Z ✔ —
the formula is right. η* = 0 ⇔ optimum ratio 1 attained ⇔ ∃ ν = g + P ≥ 0
with Σ_W ν = Σ_W g + Z = 0 (each full class meets W exactly once since
e > N) ⇔ ν ≡ 0 on W ✔. The ℤ-version of weak duality ("elementary
direction") is correct as stated (g bounded, R summable). Certificate
consequences via Lemma 2.2 ✔ (for e | Q′, x ∈ Z lies in n₀ mod e in ℤ/Q′
iff it does in ℤ, so P ≡ 0 on Z). IF2 Example 3.2 (ν = 1[0 mod 21] at
N = 20) is indeed such a ν with P at modulus 21 = N + 1 ✔.

From scratch (`scripts/review_spw2_dual.py`): primal LP vs the dual formula
as an independent LP (Z normalised to 1) on ℤ/Q′ for 8 parameter sets
(N ≤ 20, Q′ up to 27720, C ∈ {1, 1.1, 1.2, 1.5, 2}); agreement to 1e−13,
including non-trivial optima η* = 0.5 (N = 20, C = 1.2, Q′ = 2520) and
η* = 0 (C ≤ 1.1). ✔

**Defect m10 (periodic model unspecified / wrong citation).** "On the
periodic model" does not say which Q′, and "plus SPW1 Lemma 1.1" does not
apply verbatim: SPW1 Lemma 1.1(b) needs (P3) with Δ₀ and T ≥ 4(2+Δ₀)CN,
whereas RSPW leaves medium classes unconstrained. The repair is easy: in
the lift, for e ∤ Q′ with g = gcd(e,Q′) ≤ CN use the trivial ρ(s mod g) ≤ N
(total mass), so for g ≤ CN the lifted class has mass ≤ CN²/T + ε, while
for g > CN it has mass ≤ (1/2 + ε)(1 − η) ≤ 1 − η (full) — sparse classes are
unconstrained when K = ∞, so **no clipping at 1/2 is needed** here. Hence
η*_ℤ ≤ η*_per(Q′) for every Q′ (projection) and η*_ℤ ≥ η*_per(Q′) − ε for
Q′ = lcm(1..T), T ≥ CN²/ε′ (if η*_per < 1); η*_per is non-increasing along
divisibility. State this; then the "η* = 0 iff" holds on ℤ as well.

Verdict Lemma 4.1: **SOUND-AFTER-REPAIRS** (m10).

## Claim 6: EVIDENCE sections and Assessment 4.2 (labels)

Independent re-solves (`scripts/review_spw2_rspw_lp.py`, own LP on
[−L, N+L], moduli > span treated pointwise, HiGHS): N = 12, L = 96: η = 1.000;
N = 20, L = 160: 0.9552 (K = ∞), 0.6667 (K = 1); N = 30, L = 480: 0.8613
(K = ∞), 0.8595 (K = 1.5); N = 50, L = 200: 0.4821. All match the §2 table. ✔
Sawtooth table §6 recomputed exactly (`scripts/review_spw2_sawtooth.py`):
all entries for N = 100, 1000, 10000 match. ✔

Label issues:
* m11. §4 "Numerics: at L ≈ N²/2 the LP gives 0.86, 0.83, 0.78, 0.80, ≈ 0.75
  for N = 30…80": data/spw2 contains runs only for N = 30 (L = 480 ≈ N²/2),
  40 (L = 800), 60 (L = 1800), 80 (L = 2560 = 0.8·N²/2). The N = 50 value 0.78
  is not at L = 1250 in any data file (closest: 0.755 at 800, 0.798 at 1600),
  and N = 80's "≈ 0.75" is an extrapolation from 0.732 at L = 2560. Mark these
  two as interpolated/extrapolated. More importantly, finite-L optima are
  *lower* bounds for η*_ℤ (genuine measures), and the §5 local values are
  upper bounds; a decay *rate* cannot be read off lower bounds that grow
  with L. "Consistent with logarithmic decay" should be weakened to "no
  N^{−1/2} decay of the lower bounds visible for N ≤ 80".
* m12. "RSPW(2, 0.82, K ≈ 1.6) at N = 50": η = 0.82 is the L = 64N run, while
  max sparse class 1.60 was reported for the L = 16N run (η = 0.755); the
  L = 64N run's sparse maximum is not recorded. Either report the pair from one
  run or say RSPW(2, 0.755, 1.60). (Also: SPW(2, ≈ 0.25) at N = 50 is weaker
  than IF2 §9's SPW(2, 2/5) LP evidence at N ≤ 60, so it is not new.)
* m13. Report headline "Small-N numerics favour weak SPW being true": SPW1 §2
  (BDW) and SPW1 Thm 3.2 vs IF2 §9 already show small-N LP behaviour
  misleading at N ≲ 60. Assessment-level at most; say so in the headline.
* Assessment 4.2: correctly labelled heuristic; the withdrawn N^{−1/2} claim is
  clearly marked as withdrawn ✔. The last sentence of bullet 3 ("points to η*
  decaying only like a power of log N, i.e. weak SPW true") rests on a
  heuristic the author himself says underestimates edge concentration; keep
  it, but as "Assessment, weak" — no defect beyond m13.
* §5 local LPs: labelled EVIDENCE, "upper bounds for η*" ✔ (projection argument
  is correct, cf. SPW1 Lemma 3.1).
