# z52d avenue — batch P05 (100 items) summary
ES is OPEN. Rows: `out_P05.jsonl`; labels are Assessments unless a PROVED/CERTIFIED source is cited. The batch is mostly meta, infrastructure, formal-methods and dictionary items: 30 have role "calibration only" or "infrastructure" (no proof role).

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 36 | 0 | 0 | 0 | 36 |
| circular | 32 | 1 | 0 | 0 | 33 |
| known-false | 15 | 0 | 0 | 0 | 15 |
| open-plausible | 0 | 5 | 2 | 0 | 7 |
| unclear | 5 | 2 | 0 | 0 | 7 |
| harder-than-open | 2 | 0 | 0 | 0 | 2 |
Novelty: 0 → 55, 1 → 43, 2 → 2 (Z1936 categorification, Z1331 Bethe ansatz; neither has an object to work on).

**Plausibility ≥ 2 AND novelty ≥ 1:** one item, and its ES yield is nil.
* **Z2432**: *Σ_{n≤N} f(n)² ≪ N(log N)^A by incidence bounds.* Probably provable, but Cauchy–Schwarz then gives at most a positive proportion of n, which Vaughan already beats (B6).
* Novelty 0: **Z1797**, *ES for every 15·2^s + 1 with 60 | s*, and 4^s + 297 (FRONTIER §7.8; 60 ∤ s is PROVED, (J)110). A genuine open thin-family target, with no transfer to primes.
* Plausibility-1 open items: Z1386/Z1771 (an odd weighted count of solutions for every p, WINDMILL.md §1; must vanish mod 2 at squares); Z1153 (integral Y–Δ moves, PROPAGATION_CLOSURE §4: retired, not refuted); Z2926 (Gauss's one-class step = the cap-0 ratio-set event); Z3133 (I3 by a Cauchy-style universality argument).

**Recurring missing theorems** (items collapsing onto one statement)
1. *ES₅ restated: a positive word in the χ = −1 fibre exists at every p*: sign dictionaries Z2782, Z2871, Z2781, Z1487, Z2665, Z2898, Z2817; via lattices/QMC/Zaremba Z2718, Z2838, Z2994. Each re-expresses the quadratic bit (class, not parity); no target field has an existence theorem at length ≤ 3.
2. *Short vector ≠ certificate* (M1b; Minkowski points are signed; reduced-basis norms depend only on the determinant): Z1705, Z1766, Z1209, Z1015, Z2924, Z0357, Z2705.
3. *Equidistribution needs power counts* (B3/M1a): Z3147, Z2520, Z2504, Z2816, Z1921.
4. *One-sided lower tail H⁻_BM / R(p) ≥ 1*: Z3081, Z3001, Z0882, Z1430, Z1590, Z1611, Z0716, Z1774. This matches PILOT recurring statement 2.
5. *Cap 0: −1 must lie in the divisor-ratio set, not only in the subgroup that reciprocity forces*: Z2926, Z1370, Z3152 ((J)64, (J)34).
6. *Relaxation or propagation with no transport law*: Z1990, Z1332, Z1153, Z0348, Z2809. This matches PILOT recurring statement 3.
7. *Parity proof (PPA)*: Z1386, Z1771, Z1195, Z2766.
8. *Constructive ES gives deterministic QNR finding (A5)*: Z1769, Z1961, both harder-than-open (caveat: if the unrefereed OAI claim 003 holds, QNR finding is in P).
9. *Bounded procedures / finite menus (B1/B2(iii))*: Z1263, Z1636, Z1871, Z1509, Z1985, Z2548, Z3000, Z1309, Z1404, Z2911.

**Cheap falsification** (timeout 60, ulimit 4 GB; `scripts/z52d_avenue_P05_twopow.py`): Z2911 — (★) restricted to C = 2^j **fails at 503 of the 8977 primes p ≡ 1 (4) below 2·10⁵** (37, 157, 241, 409, 421, …). This is consistent with TWO_POWER_LADDER (2-group levels do not suffice; 1,298 failures ≤ 10⁶).

**Corrections to inputs**
* Z1188, Z1248, Z1546, Z2539: Pass 1's "no Lean project in repo" is outdated (LEAN_Z1546.md exists).
* Z1776, Z1797: Pass 1's "families already settled" is wrong (15·2^s + 1 with 60 | s and 4^s + 297 are open).
* Z2554: a model with positive-proportion failure contradicts Vaughan; any model must respect the 3/4 bound.
* Z2781: the relevant K-matrix is the 3×3 chain matrix, not 1×1 as Pass 1 used.
* Z0357: my quick no-go ("large lattice width ⇒ a unit lattice cube inside") was false (thin bodies along irrational directions), so the status is "unclear".

**Assessment.** No P05 item points at an architecture outside the repo's existing picture: B2/cap-0, H⁻_BM, relaxation-then-transport, parity/T1, or B1. The best-named gap is Gauss's one-class step: reciprocity forces the subgroup but not the ratio set (Z2926). There is no candidate for that step.
