# R220 — hostile review of FF_STERILE_SMALL.md (O220 checkpoint 1: §§1–3, q = 27 certificate)

Reviewer: R220 (side agent, branch side-agent/review-ff-small). Reviewed commit: side-agent/ff-sterile-small @ 030af7a5.
Scope: Lemmas 1.1–1.4, Lemma 2.1, Theorem 3.1 (q = 27), Lemma 4.1 / Cor 4.2, the q = 9 statement, labels.
Own scripts (all from scratch, none derived from `fz_*`; the sum/tail extend R218's author-independent `review_fs2_*`):
`scripts/review_fz_bounds.py, review_fz_brute.py, review_fz_rankin.py, review_fz_lemma14.py, review_fz_sum.c,
review_fz_tail.c, review_fz_caseA.py, review_fz_certify.sh, review_fz_q9.py`; logs in `data/fz_review/`.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (Euclidean division determines v₁) | **SOUND** |
| Lemma 1.2 (division routes D1, D1c, D2, D3) | **SOUND** |
| Lemma 1.3 (v₁ ≡ −T^{s−2} mod every factor; V(D)) | **SOUND** (stated bound weaker than the one the scripts use, m-1) |
| Lemma 1.4 (T-adic refinement of class bounds) | **SOUND** (hypothesis wording, m-3) |
| Lemma 2.1 (Case A ≤ (α+1)³ q^{(α−1)/2} 3^{α/2}) | **SOUND** |
| Theorem 3.1 (q = 27, k ≥ 2: no finite linear covering; covered measure over the 26 slices ≤ 3.06) | **SOUND-AFTER-REPAIRS** (documentation repairs only: m-1, m-2; the inequality is independently re-certified with a strict subset of the stated routes: total ≤ 3.0556 < 26) |
| Lemma 4.1 (fixed-q Rankin/knapsack divisor bound) | **SOUND** |
| Cor 4.2 (Case B count q^{(2/5)s+o(s)} at every odd q) | **SOUND** as labelled (bound PROVED via DEPTH_ASPECT Lemma 2.2 + q^{o(n)} divisor bounds; the o(n) step is only sketched, m-7) |
| q = 9 CERTIFIED negative statement about the method | **SOUND** (Σ_{s≤8} = 9.2236 > 8 reproduced by independent code; the "tail negligible" remark depends on Lemma 4.1 and is EVIDENCE, m-6) |
| Labels (ES not solved; Conjecture 0.2 not claimed) | **SOUND** (document); report spark slightly overstated (m-8) |

No FATAL, no MAJOR defects.

## 1. Lemmas 1.1–1.4 (re-derived)

**Lemma 1.1.** From (B₁), T^{s−2} = D·(m'w₁C₁/D) − v₁ with deg v₁ = t − 2 < deg D; uniqueness of division by a monic D
gives remainder −v₁ and quotient m'w₁C₁/D. The three sufficient conditions are right: deg m' = z, deg w₁ = a − 1, and
deg C₁ = b − 1 = y + t − 1 ≥ t − 1 > t − 2 (Lemma 1.1(ii) of FF_STERILE_PUSH, y + t = max(a, b)). No hidden hypothesis
(T^{s−2} + v₁ is monic of degree s − 2 since t < s). *Check:* `review_fz_brute.py` asserts, for every v₁ enumerated
(q = 3, s ≤ 15; q = 5, s ≤ 12; q = 7, s ≤ 10) and EVERY monic divisor D of T^{s−2} + v₁ with deg D > deg v₁, that
−(T^{s−2} mod D) = v₁ and that the quotient times D is T^{s−2} + v₁ (2.2·10⁶ divisions at q = 7 alone), and for every
tuple that the larger of w₁, C₁ qualifies. 0 failures.

**Lemma 1.2.** Each row = an O216 row (R9a, R10a, R5a, R5b) with the N*(t − 2) choices of v₁ replaced by the single v₁
of Lemma 1.1. Re-derived: D1: m' ⇒ v₁, G = w₁C₁ ⇒ w₁ | G of degree a − 1 (≤ C(a+b−2, a−1)) ⇒ (m', w, v) ⇒ tuple
(R4'). D1c: w₁² ≡ −G (mod Tv₁) (from C₁ ≡ −w₁, a unit by Lemma 1.1(iii)) gives ≤ 2^{ω(Tv₁)} = 2^{1+ω(v₁)} classes
(q odd), each with ≤ cls(a+b−2, a−1, t−1) divisors (cofactor version: G prime to Tv₁). D2: w₁ ⇒ v₁, m'C₁ ⇒ C₁ in
class −w₁ mod Tv₁. D3: same with C₁ (always applicable). All four then reconstruct the tuple from (w, v, C) or
(m', w, v). SOUND. (The exponent claim 0.4736 at the r = 3 critical point: z + (a + b)·log 2/log 27 = 1/3 + (2/3)(0.2103)
= 0.4735; correct.)

**Lemma 1.3.** v₁ ≡ −T^{s−2} (mod D) for every D | m'w₁C₁ is immediate from (B₁). Count: v₁ of exact degree e = t − 2
with fixed leading coefficient lc(w + C) (1 if a < b, 2 if a = b — determined by the pattern) in a fixed class mod a
monic D of degree d: if d ≤ e, v₁ = σ + Dh with deg h = e − d and lc(h) fixed, i.e. **exactly q^{e−d} = q^{t−2−d}**
candidates; if d > e, at most 1. The document states the weaker max(1, q^{t−1−d}) (m-1). The listed route
consequences (R9a → max(z, t) + C(a+b, a) etc.) are correct continuum versions.

**Lemma 1.4.** Re-derived: if every counted E is prime to T, then E mod QT^j is a lift of σ that is a unit mod QT^j
(T | Q: units mod Q are prime to T; T ∤ Q: the admissible lifts are units mod T^j by assumption) — at most q^j lifts —
and the PUSH class bounds apply with modulus QT^j of degree ρ + j. The cofactor version needs F prime to QT^j: when
T | Q this is "F prime to Q"; when T ∤ Q it additionally needs T ∤ F (m-3; harmless, every application has T | Q).
Applicability audited route by route in `fz_sum.c`/`fz_tail.c`: the moduli TL', Tw₁g', Tm'w₁, Tg'C₁, Tm'C₁, Tv₁
all contain T, and the F's (1 + T^s m'g'², g'T^{s−1} + w₁, T^{s−2} + m'w₁², m'C₁, m'w₁, w₁C₁, …) are all prime to T.
*Check:* `review_fz_lemma14.py` (random highly factorable F, Q = T^i·Q₀): 34 997 (F, Q, d) groups over F₃ (deg F ≤ 16)
and 15 529 over F₅ (deg F ≤ 12), maximal class count vs min_j q^j·cls(n, d, ρ + j): 0 violations.

**Per-route brute force (stronger than the author's `fz_check_bounds`).** The author's check compares exact pattern
counts only with the *minimum* over routes, so an invalid route that never attains the minimum on small cases would go
unnoticed. `review_fz_brute.py` (own enumerator: v₁, then all ordered factorisations of T^{s−2} + v₁; agrees with R218's
independent `review_fs2_brute.py` tuple counts for q = 3, s ≤ 10) compares every pattern count with EVERY route of
`review_fz_bounds.py` separately (old rows, Lemma 1.4-refined rows R2r…R10ar, D1, D1c, D2, D3, X1', X2', R4'', and the
undocumented τ-bound route of m-2): q = 3 (s ≤ 15), q = 5 (s ≤ 12), q = 7 (s ≤ 10): **0 violations**; several new routes
are attained with equality (D1, D2, D3, R4'', X2': max count/route = 1.000 at q = 3).

## 2. Lemma 2.1 (Case A tail)

Re-derived. Patterns at depth α: β ∈ [0, α−1], κ ∈ [1, α−β], λ ∈ [0, max(β, f) − 1]: fewer than (α+1)³. Routes of PUSH
Lemma 2.2: (i) N*(λ)N*(β)q^{κ−1} ≤ q^{λ+β+κ−1}, (ii) N*(λ)q^{κ−1+f} ≤ q^{λ+κ+f−1}; min ≤ q^{λ+κ−1+min(β,f)} and
λ + min(β, f) = β + f − ζ, so min(i, ii) ≤ q^{α−ζ−1}; (v) q^ζ·α!/(β!κ!f!) ≤ q^ζ 3^α; geometric mean q^{(α−1)/2}3^{α/2}.
Correct, no hidden q-dependence; the ratio of consecutive mass terms ((α+2)/(α+1))³(3/q)^{1/2} is decreasing in α, so the
geometric majorant from α = 41 is valid (the text's (44/43)³ is a valid, slightly weaker constant than the script's
(43/42)³; both fine). *Checks (`review_fz_caseA.py`):* per pattern, min(i, ii, v)² ≤ q^{α−1}3^α in exact integers and
#patterns ≤ (α+1)³, for α ≤ 60 at q = 9 and q = 27: 0 violations. Exact Case A part α ≤ 40 (R218's author-independent
`review_fs2_caseA.mass`): 9.6590343463·10⁻³ at q = 27 (agrees with `fz_caseA.py` to all printed digits); Lemma 2.1 tail in
exact rationals (√q, √(3/q) replaced by rational lower/upper bounds): ≤ 6.087·10⁻¹⁶ (author: 6.086·10⁻¹⁶). SOUND.

## 3. Theorem 3.1 (q = 27)

**Logic.** Same skeleton as FF_STERILE_PUSH Thm 3.1 ((J)51; inputs: DEPTH_ASPECT Case B normal form, PUSH Lemma 2.1
averaging criterion (Σ), PUSH Lemma 2.2 Case A routes, compactness criterion) — those inputs were reviewed in R217/R218
and are not re-litigated here. New: the route minimum is extended by Lemmas 1.2–1.4 (and Lemma 4.1 in R1/divisor
counts), and the Case A tail by Lemma 2.1 (needed: the old 6^α majorant diverges at q = 27, 6/√27 > 1 — confirmed, R218's
`review_fs2_caseA.py 3` returns no tail). "At most 6 slices with covered measure ≥ 1/2": 3.0583/(1/2) = 6.12 ⇒ ≤ 6; ≥ 20
slices more than half uncovered. Correct.

**Audit of `fz_sum.c`.** Every row re-derived against the text: e[0]–e[18] are the O216 rows (unchanged except `divc` =
Lemma 1.4 min_j q^j cls and `lD` = min(C(n,d), Lemma 4.1)); e[4] alternatives (m' | F then w₁ | F/m', etc.; F = T^{s−2} + v₁
and F/m' prime to T, as Lemma 4.1 requires); e[19] D1/R9a with V; e[20] D1c/R10a with Σ_{v₁ in class} 2^{ω(v₁)} ≤
min(V·2^{ω*}, τ-bound); e[21], e[22] D2, D3; e[23]–e[25] X1', X2', R4''. `logV(e, d) = (e − d)·log q` for d ≤ e is the
sharp count of Lemma 1.3 (not the stated q^{t−1−d}, m-1). `omstar` (greedy by degree) is the correct maximum of ω
(exchange argument: replacing a factor of degree j by an unused one of smaller degree keeps the degree budget). The
τ-bound inside `logSomClass` — Σ_{v₁ ≡ σ (D)} 2^{ω(v₁)} ≤ Σ τ(v₁) ≤ 2Σ_{j ≤ e/2} Σ_{δ monic, deg j} #{v₁ ≡ σ (D), δ | v₁}
≤ 2Σ_{j≤e/2} q^j max(1, q^{e−d−j}) (δ is automatically prime to D since σ = −T^{s−2} is a unit mod D = m'; CRT modulus
deg d + j) — is **valid but not stated anywhere in the document** (m-2). Mass weight q^{1−⌈s/2⌉} ((s+1)/2 integer
division), multiplicity 2 for a < b, pattern loop (a ≥ 1, b ≥ a, y ≤ b − 2): correct. The Lemma 4.1 implementation
(`init_rankin`) drops items of gain < 10⁻¹⁸ (total effect < 2048·10⁻¹⁸) and rounds V outward by 10⁻¹² — adequate; verified
against exact maxima over all factorisation types (§4 below): 0 violations.

**Audit of `fz_tail.c`.** New routes R9a3, R10a3, R5a3, R5b3, X1_3, X2_3, R4p3: the linear forms for t − deg D
(t − z = 1 − a − 2z − y, etc.) are right and the integer offsets are dropped in the safe direction. R10a3's constant:
case d ≤ e: 2·(⌊e/2⌋ + 1)·q^{max(e/2, e−d)} ≤ 2(s+1)q^{...}, times 2 for Tv₁; case d > e: 2·2^{ω*(e)} with
ω*(e) ≤ (q−1)/2 + e/2 (at most q − 1 linear factors ≠ T, every other factor costs ≥ 2) — both covered by
logk = log 2 + ((q−1)/2) log 2 and polys = 1. Lemma 1.4 in boxes: j = ⌈θs⌉ ≤ θs + 1 digits, cost q^{θs+1}, class
conditions tested at ρ_eff = s(R + θ) + r0 ≤ ρ + j; all four conditions (d < ρ, n − d < ρ, 3ρ > n, Coppersmith
An + (B−M)d − Bρ < 0 with B > 0) are monotone in ρ, and the bisection result is re-checked, so validity does not depend
on the bisection. τ is treated as an independent interval [1 − Σhi, 1 − Σlo] (conservative). Box pruning keeps every
box that can contain a valid pattern; pattern count (sw+1)³, geometric tail with the ratio bound
((s+2)/(s+1))^{3+p}e^{φ−(log q)/2} — correct since w/(sw+1) ≤ 1/(s+1) for w ≤ 1. Fails closed (non-finite total or failed
box ⇒ exit 1; `fz_certify.sh` uses `set -euo pipefail` and checks finiteness). No defect found.

**Independent re-certification (`review_fz_certify.sh 3 80`, log `data/fz_review/certify.txt`).** Own finite sum
`review_fz_sum.c` (R218's author-independent harness + the Lemma 1.3 routes D1, D1c (ω* only), D2, D3, X1', X2', R4''
and Lemma 1.4 on all class rows; **without** Lemma 4.1 and **without** the undocumented τ-bound), own tail
`review_fz_tail.c` (R218's tail, exact substitution τ = 1 − α − ζ − η, + the same new routes, Lemma 1.4 by θ-bisection),
own Case A:
| component | R220 | author |
|---|---|---|
| finite 3 ≤ s ≤ 80 | 3.0457472488 (×(1+10⁻⁸)) | 3.0180430695 |
| tail s > 80 | 1.647·10⁻⁴ (×1.001; 58 880 boxes, all certified at depth ≤ 8) | 2.922·10⁻⁴ |
| Case A | 9.659034·10⁻³ (exact + rational tail) | 9.6590·10⁻³ + 6.1·10⁻¹⁶ |
| total | **3.0556 < 26** | 3.0583 (×1.01) |
Mine is larger in the finite part because it uses a strict subset of the routes (no Lemma 4.1, no τ-bound) — so the
theorem does not depend on either. With the document's weaker V(D) = max(1, q^{t−1−d}) (VMODE=1) the finite part is
4.4317 and the total 4.4416 < 26: **the theorem holds with the lemmas exactly as stated**, the sharp count only improves
the constant. Sanity: with the new routes switched off, my tail fails (infinite, as at O216), with them on it certifies
— the improvement is real and not an artefact of the harness. Rounding: long double logs with ≤ 10⁻¹¹ relative error per
term against a margin factor > 8.5; floating error is irrelevant.

**Bound ≥ exact counts.** Every route (old and new, separately) dominates the exact counts at q = 3, 5, 7 (§1). At
q = 27 exact counts are out of reach for nontrivial s; the routes are proved uniformly in q, so this is as intended.

## 4. Lemma 4.1, Cor 4.2, q = 9

**Lemma 4.1.** Re-derived: [x^{d'}]Π S_{e_i}(x^{deg P_i}) ≤ ρ^{−d'}Π S_{e_i}(ρ^{deg P_i}) for 0 < ρ ≤ 1 (nonnegative
coefficients); log Π S_{e_i} = Σ_i Σ_{e ≤ e_i} gain(P_i, e) with weights summing to n; the fractional knapsack over all
items (P, e) (at most I'(j) irreducibles per degree) dominates every integer selection, prefix-closed or not, since all
gains are ≥ 0. Degree-d ↔ degree-(n−d) symmetry is right. (Decreasing gains are not even needed for the upper bound.)
*Check (`review_fz_rankin.py`):* exhaustive over **factorisation types** (so exact maxima over ALL F of degree n with
T ∤ F, not samples): q = 3 (n ≤ 14), 5 (n ≤ 12), 7 (n ≤ 11), 27 (n ≤ 9), every d, 68 values of ρ: 0 violations of the
lemma; and the author's implementation `lRk` of `fz_sum.c` (64-point ρ grid, greedy fill) dominates the exact maxima
in all these cases (0 violations, max ratio 0.985). SOUND. Note: at q = 27 and the degrees that matter, Lemma 4.1 is
weaker than C(n, d) (e.g. n = 14, d = 7: 16384 vs 3432), and the q = 27 certificate does not need it (§3).

**Cor 4.2.** The bound q^{(2/5)s+o(s)} is PROVED: DEPTH_ASPECT Lemma 2.2 gives |𝓕(s)| ≤ (s+1)⁴·B·q^{⌊2(s−3)/5⌋} with
B = max(2δ₃(s), δ(s)δ(3s), δ(2s)), and δ, δ₃ ≤ δ² are q^{o(n)} at fixed q. The document's justification of the last
step ("the knapsack fills n with ≍ n/log_q n items") is a sketch (m-7). The value 2/5 being the maximum for the
*extended* route set is EVIDENCE (grid), correctly labelled. My own box-wise upper bound of the continuum exponent
(`RATE=1 review_fz_tail r 80 lev`, max over boxes of min-route φ⁺/log q − 1/2, φ⁺ an upper bound on the box, no
Lemma 4.1): r = 3: −0.078 (width 1/64), −0.094 (width 1/128), maximiser near (0.21, 0.21, 0.18) → the ET point
(1/5, 1/5, 1/5, 2/5) and −0.100 in the limit, consistent with the §1 table; r = 2: +0.019 (1/64), −0.006 (1/128),
consistent with the table's −0.044; old routes only, r = 3: +0.040 (1/64). At the ET point I re-derived by hand that
every route is ≥ 2/5 (R1 = t, R4'' = z + a, D1 = t, R2 = y + z, R3 = a + y, R4 = z + a with all Coppersmith thresholds
met: 6/25, 3/8, 3/10 < 2/5), so 2/5 cannot be improved by these routes there.

**q = 9 statement.** The CERTIFIED negative statement is about the bound-sum: Σ_{s≤8} = 9.2235939643 > 8 is reproduced
digit for digit by my independent `review_fz_sum 2` (Lemma 4.1 is inactive at s ≤ 8), so the failure of (Σ) *with these
bounds* is certified independently of any tail. The remark "terms 10⁻⁶ at s = 80, so the tail is negligible" depends on
Lemma 4.1: without it my per-s term at s = 80 is still 0.118 and the sum through s = 80 is 79.95 (m-6; label EVIDENCE).
**Additional data for the author's next step (`review_fz_q9.py`, exact enumeration over F₉ via python-flint):** the
exact Case B mass Σ_s #tuples(s)·q^{1−⌈s/2⌉} is 0.2222, 0.0494, 0.1975, 0.0274, 0.0549, 0.0018 for s = 4..9 (none at
s = 3), cumulative **0.5533 through s = 9**, against the bound-sum 10.675 through s = 9. So the exact small-s masses are
~19× below the bounds, and the q = 9 programme "exact counts up to s ≈ 20–24, then route bounds" looks plausible
(Assessment; the counts above are CERTIFIED by exhaustive enumeration, cross-validated at q = 3 against R218's enumerator).

## 5. Labels

Document status line, Theorem 3.1 (PROVED, computer-assisted, same standard as (J)51), Lemma labels, the steering table
(EVIDENCE) and the q = 9 statement are correctly labelled; ES, ES_q, and Conjecture 0.2 (q = 3) are not claimed. The
report's spark "this is a *finite* computation problem for Conjecture 0.2" (q = 3) overstates (m-8).

## 6. Defects

No FATAL. No MAJOR.

**m-1 (MINOR; Lemma 1.3, statement of V(D)).** The text gives V(D) = max(1, q^{t−1−deg D}); the proof already shows the
sharp count q^{t−2−deg D} (deg D ≤ t − 2), and `fz_sum.c` (`logV`) and `fz_tail.c` (`Vc` with the shift dropped) use the
sharp count — so the certificate uses a bound stronger than the one stated. It is true (re-derived, brute-forced in
`review_fz_brute.py`), and the theorem also holds with the stated weaker bound (my total 4.44 < 26), but the document
must state what the certificate uses. *Repair:* "V(D) := q^{t−2−deg D} if deg D ≤ t − 2, and 1 otherwise"; adjust the
proof's last sentence ("exactly q^{t−2−deg D} choices").

**m-2 (MINOR; undocumented route in the certificate).** `fz_sum.c` `logSomClass` and `fz_tail.c` R10a3 use, besides
V(D)·2^{ω*(t−2)}, the bound Σ_{v₁ ≡ σ (D), deg e, fixed lc} 2^{ω(v₁)} ≤ 2Σ_{j ≤ e/2} q^j max(1, q^{e−d−j}) (and in the
tail ≤ 2(s+1)q^{max(e/2, e−d)}, resp. 2^{(q−1)/2 + e/2} for d > e via ω*(e) ≤ (q−1)/2 + e/2). Lemma 1.2/1.3 mention only
the maximum 2^{ω*}. Valid (proof in §3 of this review; brute-forced as route R10a'tau) but absent from the text, and
Theorem 3.1's proof says "Lemmas 1.2–1.4 and 4.1". *Repair:* add to Lemma 1.3: "(R10a with v₁ in a class mod m')
Σ_{v₁} 2^{ω(v₁)} ≤ min(V(m')·2^{ω*(t−2)}, 2Σ_{j≤(t−2)/2} q^j·max(1, q^{t−2−z−j})), since 2^ω ≤ τ ≤ 2#{δ | v₁ : deg δ ≤ e/2}
and δ | v₁ forces gcd(δ, m') = 1 (v₁ ≡ −T^{s−2} is a unit mod m'); tail form: ≤ 2(s+1)q^{max(e/2, e−z)} for z ≤ e, and
ω*(e) ≤ (q−1)/2 + e/2." (Not needed for the theorem: my certificate omits it.)

**m-3 (MINOR; Lemma 1.4, hypothesis paragraph).** "(Repair of the hypothesis: … the cofactor version needs F prime to Q,
as before.)" — if T ∤ Q, the cofactor version applied with modulus QT^j needs F prime to QT^j, i.e. also T ∤ F. Harmless
(all applications have T | Q). *Repair:* "…the cofactor version needs F prime to QT^j (equivalently to Q when T | Q)."

**m-4 (MINOR; Thm 3.1 proof, dependency claim).** The proof cites Lemma 4.1 (§4, later in the document). My
re-certification shows neither Lemma 4.1 nor the τ-bound is needed (3.0556 < 26 without both; 4.44 with the stated
weaker V). *Repair (optional, strengthens the result):* add "(Lemma 4.1 and the τ-bound of Lemma 1.3 are not needed:
R220's independent certificate without them gives ≤ 3.056)".

**m-5 (MINOR; §1 Check paragraph).** `fz_check_bounds.c` compares exact counts with the minimum over routes only; an
invalid route that is never the argmin on small cases would pass. *Repair:* cite R220's per-route check
(`review_fz_brute.py`: every route separately, q = 3 s ≤ 15, q = 5 s ≤ 12, q = 7 s ≤ 10, 0 violations).

**m-6 (MINOR; §4 q = 9, tail remark).** "terms 10⁻⁶ at s = 80, so the tail is negligible" holds only with Lemma 4.1 in the
routes (without: term 0.118 at s = 80, sum to 80 = 79.95) and is not certified (no q = 9 tail run). *Repair:* "(with
Lemma 4.1; EVIDENCE, no tail certificate at q = 9)". The CERTIFIED part (Σ_{s≤8} of the bounds = 9.22 > 8) is fine.

**m-7 (MINOR; §4, "V_ρ(n) = o(n)").** Only sketched. *Repair:* give the elementary bound: with F = ΠP_i^{e_i} of degree
n, primes of degree ≥ J contribute Π(e_i + 1) ≤ 2^{Σ e_i} ≤ 2^{n/J}, and there are < q^J primes of degree < J, each with
e_i + 1 ≤ n + 1; so τ(F) ≤ 2^{n/J}(n+1)^{q^J}, and J = ⌊log_q(n/log²(n+2))⌋ gives log τ(F) = O(n log q/log n) = o(n)·log q.
This makes Cor 4.2's "PROVED" self-contained (δ₃ ≤ δ²).

**m-8 (MINOR; AGENT_REPORT_O220 spark on Conjecture 0.2).** "combined with the exact union to s = 21 … this is a finite
computation problem for Conjecture 0.2 — but s₀ is probably several hundred". With union bounds failing at q = 3 even for
exact counts (94/27 > 2, §4 end), one would need the exact *union* of cylinders up to s₀, i.e. enumerating ≈ 3^{2s/5}
tuples per level up to s₀ ~ hundreds — finite in principle, infeasible in practice, and it would give the conclusion of
Conjecture 0.2 (no finite linear covering) rather than x*_c ∈ O. *Repair:* rephrase as "finite in principle; s₀ ≈ ?;
infeasible unless s₀ is small", and say "conclusion of Conjecture 0.2".

**m-9 (MINOR, cosmetic; Lemma 2.1).** The text's ratio constant (44/43)³ differs from the script's (43/42)³ (both valid;
the script's is the tight one for α ≥ 41). *Repair:* use (43/42)³ in the text.

## 7. Recommendation

Theorem 3.1 (q = 27) is SOUND-AFTER-REPAIRS with documentation-only repairs (m-1, m-2 needed so that the text states
every bound the certificate uses; m-3…m-9 optional). Independently re-certified: covered relative measure summed over
the 26 c-slices ≤ 3.056 (stated routes, sharp V) / ≤ 4.442 (stated weaker V), both far below 26. Together with (J)51 this
gives no finite linear covering of ES_q(T^k), k ≥ 2, for all q = 3^r, r ≥ 3.
