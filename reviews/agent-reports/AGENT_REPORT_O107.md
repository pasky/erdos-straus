# AGENT REPORT O107 — is x** = x(2,15) sterile? (r = 13, complete enumeration by ES level)

Branch `side-agent/xss-sterility`. Deliverable: `POINTWISE_MORDELL13E.md`, `scripts/m13e_*`, `logs/o107_run{1,2}.log`.

## Outcome
No class found. **x\*\* survives.** Conjecture 5.2 of 13B stays OPEN.

1. **Comp. 3.1 (CERTIFIED).** x\*\* lies in no ET class (seven families, any T-free modulus) of ES level
   `N < 2.59·10¹⁰`. That is all 54 T-units up to `13⁹`; no T-unit lies in `(13⁹, 11¹⁰)`. The runs produced
   2 865 550 ES solutions and 445 655 distinct boxes. Hence x\*\* is in no class of T-level `M_T ≤ 161050`.
   This is complementary to the e-capped targeted searches (`e ≤ 2·10⁹` P/Q, `≤ 2·10⁸` U): here `e` is unbounded.
   The x\* control re-finds exactly the two 13B data.
2. **Engine** `m13e_es.c`: 13B's divisor method with a segmented sieve, 128-bit arithmetic and meet-in-the-middle on the
   congruence `D ≡ −s (mod r)` (bitmap-prefiltered hash). It runs at ≈1–1.9 µs per x, about 9–12× faster than `m13b_es`.
   Validation:
   * identical solution sets to `m13b_es` on 9 levels;
   * identical box sets on all 32 levels `≤ 4·10⁷` (209 295 boxes);
   * independent Python divisor check on 10 x-ranges at `N = 13⁹` (128-bit regime): 6417 solutions, identical;
   * `m13e_inv.py` recomputes `z` exactly and aborts unless the chunk files tile `(N/4, 3N/4]`.
3. **Lemma 2.1 (PROVED).** In the (2,2) cell, every family except I3 has odd `v_T(N)`; for I3, `v_T(N) ≡ v_T(f)+1`.
   This was checked on 6062 boxes. *Scope (PROVED):* x\*\* ≡ x\* (mod 143), and x\* is covered. So no argument that
   depends only on `x mod 143` (quadratic or higher reciprocity at 11 and 13) can prove x\*\* sterile; a proof must use
   the 13-adic digit `15 ≢ 2 (mod 169)`.
4. **Comp. 3.2–3.3 (CERTIFIED, local picture).**
   * `C_3(x**) = {x_11≡2 (11³), x_13≡15 (13³)}` meets only 7 boxes of these levels (total mass `7.7·10⁻⁵`). None of
     them comes from the five levels above 4.6·10⁹.
   * `C_2(x**)` is 56.6% covered, and the mass per level decays from 0.1–0.3 to ≤ 4·10⁻² at `N ~ 10¹⁰`.
   * The nearest boxes miss x\*\* by a single digit (factor 11). Example: II3 `(183703,3,65219)` agrees mod `11²13²`.
     So the survival looks generic, not structural.
5. **Prop. 4.1 (PROVED reduction).** If the boxes of level `> 13⁹` meeting `C_3` have total mass `< 1−7.7·10⁻⁵`, then
   `C_3` contains a sterile point, and no finite ET covering exists for `(p/11)=(p/13)=−1`. Verifying this needs the open
   explicit ES-count bound of MORDELL17 §4/§6, now at two primes. For x\*\* itself no measure argument works.

## Not done / suggestions
* The next level is `11¹⁰`, then 7 more up to `4.3·10¹⁰`. That is ≈ +4 h per 10¹⁰ of x-range on 2 cores with this
  engine. The enumeration is linear in N; we see no sublinear complete method.
* STATUS/DISCOVERIES were not edited. Suggested ledger line: "x\*\* in no ET class of ES level < 2.59·10¹⁰ (CERTIFIED,
  13E Comp. 3.1); Lemma 2.1 parity (PROVED); sterility of x\*\* OPEN".
* The run dirs are in `/tmp/o107/run`, `/tmp/o107/run2` (inv pkls + raw ES chunks, if the parent wants to re-check).
