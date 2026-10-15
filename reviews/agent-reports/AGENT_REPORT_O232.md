# AGENT_REPORT_O232 — sign fields: exponential near-squares, numerator sign fields, the non-genus layer

Branch side-agent/sign-fields (merged side-agent/near-square-exist first, as instructed). Main file SIGN_FIELDS.md; memos
BRAINSTORM/z8_*.md (6, indexed in BRAINSTORM/README.md); scripts scripts/z8_*; certificates data/z8/.
**ES is not solved; the only infinite ES statements are the certified families of Thm 1.3.**

## SHARP
1. **Numerator sign fields (PROVED, SIGN_FIELDS Prop 2.1 / Thm 2.2).** For numerator ν and u-level u (coprime case),
   the five ν-slots are a Frobenius set C_ν(n, u) ⊂ Gal(ℚ(ζ_{νu})/ℚ) (slot ν | t = "σ_A = complex conjugation on
   ℚ(ζ_{νu})"). At odd squares every odd A has σ_A fixing √−u, so the t-slot is T1-clean iff √−u ∈ ℚ(ζ_{νu}), and this
   holds for every u **iff ℚ(i) ⊂ ℚ(ζ_ν) iff 4 | ν** — a one-line Galois reason for (J)46's "full T1 ⟺ 4 | ν" (t-slots).
   Moreover **ν = 4 is the unique numerator whose coprime slot set is exactly the T1-forbidden half** of the c-fibre
   (relative size 1/φ(ν) = 1/2): for 4 the word condition *is* the sign/genus condition; for 8, 12, … it is a proper
   Chebotarev subset (an extra ζ₈-type bit). Check: 8/131, 8/241 — every χ = −1 word has its 4-slot ≡ 4 (mod 8).
   (R236 repair: "proper subset" only at levels u ≡ 1 (4) with ν ∤ n + u — at ν | n + u the v-slot gives the whole
   c-fibre; and the 8/131, 8/241 data are only *consistent with* this: ν-slot ⟹ ν/n solvable, not conversely, 8/113.)
2. **Mixed exponent points (EVIDENCE + description, SIGN_FIELDS §1.4).** n_s = 4^s + 105 is an infinite family with
   **every member in Mordell's hard classes mod 840** and a square mod 3, 5, 7. Certified: Λ ∩ Sq^× = ∅ (unit-square
   screen at L = 360), so the square half of (J)22's criterion holds and only the ET class supply can block a covering.
   The residual exponents are *mixed points* — CRT gluings in Ẑ of the integer square points 4⁴ + 105 = 19² and
   4⁻² + 105 = (41/4)² (μ* = 4 off the 3-adic component, −2 on it). An adaptive lifting covering drives the uncovered
   Haar measure 8·10⁻³ → 8.5·10⁻⁸ (75 refinements, period 4·10¹², 342 114 uncovered residues), then the greedy stalled. Either it terminates
   (certificate for a fully Mordell-hard near-square family) or some mixed point is sterile (a first *non-square*
   sterile point in an exponential limit set). Worth a dedicated run.

## Goals
* (1) Exponential near-squares: **PROVED (computer-assisted)** ES for all 4^s + k, k ∈ {9, 57, 81, 129, 153, 177, 201,
  225, 249} (ec_cert re-run standalone on every certificate: identity, integrality, positivity, periodicity, exact check to
  s = 400/600, T1 control; plus independent brute force for s ≤ 8). Lemma 1.1 (non-trivial k ≡ 9 mod 24 for c₀ = 1),
  Lemma 1.2 (no integer unit-square points for c₀ = 1 — the (J)22 Cor 1.5 obstruction never fires, PROVED).
  The answer to "does the closure of {2^s} meet Z_k^□": yes, but only at *non-unit* square points (and their mixed
  gluings), which divisor/ET classes can cover; no uncoverability proof exists for any k in this shape (none of the
  OPEN k has a unit-square point). OPEN: k = 33, 105, 273, 297 (all have integer non-unit square points). c₀ ≠ 1 not surveyed.
* (2) Sign fields for numerators: SHARP 1. Even-A words excluded (as in O225 Remark 2.4); the A*-slot class
  −(n + u)/n is analysed only in the coprime case.
* (3) Non-genus layer: **negative (PROVED trivial + Assessment)**: at a single level the existence of a χ = −1 word depends
  only on the residues mod 4u of the prime factors of p + u — no Rédei/non-abelian data can enter; a forced non-genus
  layer would need non-abelian level fields. The numerical enrichment test was NOT run.
* (4) Chebotarev-in-a-family: **negative (Assessment)**; prime words reduce to "p mod r ∈ {r − d : d | r + 1,
  (−d/r) = −1}"; bounded → B1/B2, growing → B3, summed → B6. Linear disjointness is free; hitting a divisor is the problem.

## Caveats for the reviewer
* Thm 2.2(d) is stated for u ≡ 1 (mod 4); for u ≡ 3 (mod 4) the whole c-fibre is forbidden (statement adjusted). (R236 repair: for ν = 4 at
  u ≡ 3 (4) the v-slot makes the whole c-fibre a 4-word set, so the coincidence holds there too; see SIGN_FIELDS Thm 2.2(d).)
* z8_adaptive.py's certificate path and z8_cert_tree.py (replay checker) are written but never produced a terminating certificate (the k = 105 run stalled), so the
  replay checker is untested beyond syntax.
* Memo z8_mixed_points cites Filaseta–Finch–Kozek from memory (flagged in the memo).
* I briefly ran 5 search processes in parallel once (house rule: ≤ 2 cores); afterwards ≤ 2.

## Sparks (not pursued)
* S1. Finish k = 105 (larger Mmax for the class supply, smarter class choice minimising period growth); if it stalls, test
  candidate mixed points for sterility directly (z8_point.py over all M ≤ 10⁶ for a fixed profinite μ).
* S2. c₀·4^s + k for c₀ ∈ {2, 3, 5} and two-parameter S-unit near-squares 4^a·9^b + k (Ẑ² exponent space, more coupling).
* S3. Group-clean flag in z2_hardness.c: is near-square depletion enriched at group-clean-not-genus levels (would be a
  multi-level or statistical effect, by Prop 3.1)?
* S4. Numerator sign fields on the t-side and the even-A words: complete the C_ν table for all slots and check whether
  the 8-failures follow a computable "ζ₈-bit" law (e.g. p mod 16 bias).
