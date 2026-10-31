# z52d avenue — batch PILOT (40 items) summary
ES is OPEN. Rows: `out_PILOT.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| circular | 13 | 0 | 0 | 0 | 13 |
| known-false | 9 | 0 | 0 | 0 | 9 |
| known-true (gap named) | 5 | 0 | 1 | 2 | 8 |
| open-plausible | 0 | 4 | 0 | 0 | 4 |
| unclear | 3 | 0 | 1 | 0 | 4 |
| harder-than-open | 2 | 0 | 0 | 0 | 2 |
Novelty: 0 → 21, 1 → 17, 2 → 2 (Z1333, Z2877; both dead on arrival).

**Plausibility ≥ 2 AND novelty ≥ 1:** one item, and it is calibration only.
* **Z0735** (9/n): *finitely many identities give 9/n = 1/x+1/y+1/z for every n ≥ 20 (exceptions exactly {2,5,11,19}).*
  A cheap check here found that numerator 9 has **no T1**: Type I/II-shaped solutions exist at odd squares 25…529 (e.g. 9/25 = 1/3 + 1/38 + 1/2850), and 4/n has none. Exceptions below 600 are confirmed.
  A covering or a sterile point for m = 9 would test whether B1 is purely a T1 phenomenon. Caveat: 5/n also lacks T1 and is still open.
  Yield for ES: none (numerator blindness).
* Also plausibility ≥ 2 but novelty 0: Z1253 (word↔fraction bridge, already PROVED; Pass 1's "nothing" came from a continuant
  convention error — the negative continuant needs t in the middle), Z1929 (subexponential (★) exceptional set; Vaughan/CRT,
  essentially in the repo; B6), and Z0026 (FF squares: a diagnostic for which step T1 forces a ℤ-proof to replace).

**Recurring missing theorems** (items collapsing onto one statement)
1. *One tied divisor event / two-coordinate slice at each p* (redteam-automorphic-2 Thm 2.2): Z0978, Z1454, Z1967, Z1987, Z2327,
   Z2099, Z2228, Z0210, Z3183. Each architecture's last step is "N(p) has a divisor in a class mod a modulus tied to the solution".
   New explicit instance: the coordinate conic fibration ((4x−p)y − px)((4x−p)z − px) = p²x² (Z1454).
2. *One-sided lower tail H⁻_BM / single-coefficient lower bound*: Z1580, Z1681, Z2068, Z2929 (one-sided form), Z2778 (I3 analogue),
   Z1425 (contains it at a = 4). The two-sided versions are false i.o. (Linnik, BM_CORRECTED Prop 3.1).
3. *Relaxation then transport with no transport theorem*: Z1644 (k ≥ 4 terms is trivial for numerator 4), Z2899 (length-L
   telescoping words give L-term sums), Z1813 (4k/(kp) = 4/p), Z0089 (units < 1 at one place; ℕ has none).
4. *Average-only (B6) exceptional-set statements*: Z0003, Z1929, Z2002.
5. *Calibration only, no proof role*: Z0618, Z0831, Z1333, Z1858, Z2138, Z2176, Z2240.

**Cheap falsifications run in this pass** (timeout 60, ulimit 4 GB)
* Z1464 (adaptive level choice): levels C = q | 4p+1 (q ≤ 500, p ≡ 1 (24) in [10⁵, 4·10⁵]) hit at 0.108, against 0.106 for the same q
  at random p. There is no information gain, matching privacy (SS8 Lemma 2.3): adaptivity passes only congruence data.
* Z0735: T1 absent for m = 9 (above).

**Corrections to inputs**
* Z0003: the status note "FF rate q^{−n/10}" is wrong. The rate in FUNCTIONFIELD_ES Thm 5.3 is (Φ(A)+o(1))/log n ≍ 1/log log|P|, which is weaker than
  Vaughan; q^{−n/10} is only a second-moment error term. FF gives no power-saving template.
* Z2099: MARKOFF_ES.md already reconciles Loughran–Mitankin with ES, so the status note "not reconciled" is outdated.
* Z2228: the Borwein–Choi (ab+bc+ca) calibration is cited from memory; verify it before using it.

**Assessment.** None of the 40 PILOT items points at a proof architecture outside the repo's B2 / H⁻_BM / relaxation-transport
picture. The single new handle is a calibration question (Z0735: is B1 exactly T1?) with no ES yield.
