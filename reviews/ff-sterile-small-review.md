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

(sections below)
