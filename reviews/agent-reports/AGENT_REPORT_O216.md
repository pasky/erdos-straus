# AGENT_REPORT_O216 — function-field sterility pushed down to q = 3^4 (FF_STERILE_PUSH.md)

**SHARP:**
1. **Theorem 3.1 (PROVED, computer-assisted, same inputs as (J)26 Thm 2.5): for q = 3^r with r ≥ 4 (q ≥ 81) and every k ≥ 2,
   O(q, T^k) ≠ ∅ — ES_q(T^k) has no finite linear covering.** Previously r ≥ 27 ((J)26); R187 E5 guessed r ≥ 10. For r ≥ 5 the
   statement holds in every c-slice, with uncovered relative measure ≥ 0.74 (r = 5), ≥ 0.62 (r = 6), ≥ 0.98 (r ≥ 7).
2. **Function-field divisors in residue classes with absolute bounds** (Lemmas 1.4, 1.5, elementary): if 3 deg Q > deg F,
   F has ≤ 2 divisors of a given degree in a unit class mod Q (Lenstra over ℤ gives 11); and a Coppersmith–Howgrave-Graham
   bound with threshold deg Q > d(n − d)/n (≤ n/4), proved by pigeonhole (no LLL loss over F_q[T]). These replace the divisor
   function on every binding route.
3. **Char 2 is non-sterile by Frobenius (PROVED):** (1 + Tg')² = 1 + T²g'², so for q even the single family
   (T² + cT + 1; 0, T + c; 2, T + c) covers the whole c-slice. The odd-characteristic input is exactly v ≠ 0 (E ≠ E'), i.e. −2 ≠ 0.
4. New exact identities for Case B tuples: E·v = T^s + m'w² and y + t = max(a, b) (Lemma 1.1) — one degree of freedom less in
   every pattern, and four reconstruction routes with no divisor loss.

## What was done
* Goal (1): `FF_STERILE_PUSH.md` §§1–3. Lemma 1.1 (degree identity), 1.2 (loss-free routes), 1.3 (divisors by degree: C(n,d)),
  1.4 (FF Lenstra), 1.5 (FF Coppersmith), 1.6 (19-route table incl. the square-root-class route R10 with Σ2^{ω(v)} averaging),
  2.1 (averaging over c: factor q − 1), 2.2 (Case A routes; depth α ≤ 2 empty). Theorem 3.1 certified for 4 ≤ r ≤ 30 by
  `scripts/fs_certify.sh` (fails closed; log `data/fs/certify.txt`): exact-pattern finite sums (`fs_sum.c`, cross-checked to
  10 digits by the independent exact-rational `fs_sum_check.py`), rigorous adaptive-box tail (`fs_tail.c`), Case A
  (`fs_caseA.py`). Left side of (Σ) ≤ 2.18 at r = 4 (needs < 80), 0.25 at r = 5, 0.37 at r = 6, < 0.012 for r ≥ 7.
  Sanity: route bounds ≥ exact famcount counts on all patterns (q = 3, 5, 7; 0 violations); Lemmas 1.4/1.5 brute-forced on
  32 591 (degree, class) groups over F₃, F₅ (0 violations).
* Goal (3): §4 — k = 1 (q = 3, A = T): hypothesis "cylinder depth ≥ 2" fails (constant families of FUNCTIONFIELD_ES Prop 1.4
  carry full mass); char 2: "v ≠ 0" fails (Frobenius-square families). ℤ: Assessment of which tools transfer.
* Goal (2): §5 — exact reformulation of "a Case B family covers x*_c" as the system (S1) T^n | m'g'²v₁(1+cT) + 1,
  (S2) a second T-adic congruence, (S3) v₁ | 1 + m'(Tω)² (an equivalence, PROVED). No structural exclusion found: it is the
  lottery shape again. Precise limits: at q = 3 even exact counts give (Σ)-sum 94/27 > 2 through s = 15 (exact census), so the
  union bound is dead there; the route exponents are +0.167 (q = 3), +0.096 (q = 9), 0.000 (q = 27), −0.027 (q = 81) (grid,
  EVIDENCE). At q = 27 the binding point is where the R10 Coppersmith threshold τ = αβ/(α+β) meets the R1 multinomial bound.

## Honest negatives / labels
* Conjecture 0.2 (q = 3) is **not** proved, nor any sterile point at q = 3, 9, 27. Theorem 3.1 is about q ≥ 81.
* The r = 3 "barrier" is EVIDENCE/Assessment (failure to certify ≠ negative result). (R217/R218 repair: but the Lemma 1.6 bound-sum itself exceeds q − 1 = 26 already at s = 36, so the failure of *this* union bound at r = 3 is CERTIFIED; only "every union bound fails" is Assessment.)
* Theorem 3.1 inherits the inputs of (J)26 Thm 2.5 (O173 Lemmas 1.1/2.1 as re-derived by R187, R166 Case A, compactness).
* Self-review: codex deep reviewer (no FATAL; MAJOR: rounding/fail-open certification, false "polynomial count" claim at the
  thirds corner — actually exp(Ω(s/log s)) genuine tuples exist there, reviewer's cyclotomic construction —, overstated barrier
  labels; all repaired). A fresh hostile review by the parent is still needed, especially of fs_tail.c's box bounds.

## Sparks (not pursued)
* Transplant Lemmas 1.4–1.6 (class-divisor bounds, loss-free routes, averaging over cells) to the ℤ Mordell boxes of
  DEPTH_ASPECT §3 / MORDELL17: could make r₀ of (J)26 Thm 3.1 explicit and much smaller (r = 13, 17 still out: level-1 term).
* r = 3 (q = 27): a bivariate Coppersmith for the R10 problem (unknown w₁, C₁ with known product and sum ≡ 0 mod Tv₁), or an
  average bound for d₃ over {T^{s−2} + v₁} in F₂₇[T]; either closes q = 27.
* k = 1, q = 3^r ≥ 9: slice analysis at u(0) ∉ {1, 2} (classes not hit by constant families) — a no-covering theorem for A = T?
* The reviewer's cyclotomic family (T^{3^h−1} − 1, exp(Ω(s/log s)) tuples at the thirds corner): test whether any covers x*_c —
  it is the richest explicit source of high-level Case B families at q = 3.
* Char 2, large q, A = T²: are there sterile points off the slice u(0) = 1?

* Hostile reviews: R217 (`reviews/ff-sterile-push-review.md`) and R218 (`reviews/ff-sterile-push-review-2.md`, independent recertification r = 4..30 with own code): no FATAL/MAJOR; minors repaired in FF_STERILE_PUSH.md, marked (R217 repair) / (R218 repair).
