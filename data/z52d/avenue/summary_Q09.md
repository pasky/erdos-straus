# z52d avenue — batch Q09 (113 items) summary
ES is OPEN. Rows: `out_Q09.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch, mostly geometry of the ES cubic (Cayley cubic, pencils, Markoff analogues, integral-Manin), heights and literature calibration.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 2 | 44 | 46 |
| known-false | 47 | 0 | 0 | 0 | 47 |
| circular | 10 | 0 | 0 | 0 | 10 |
| open-plausible | 0 | 1 | 2 | 0 | 3 |
| unclear | 1 | 0 | 6 | 0 | 7 |
Novelty: 0 → 68, 1 → 45, 2 → 0. 23 rows are calibration-only. Plaus-3 rows are calibration or main-term statements (yield none).
**Plausibility ≥ 2 AND novelty ≥ 1**: none with an ES yield. The rows with content beyond calibration:
* **Z2040/Z2481**: *#{P ∈ U_1(ℚ)_{>0} : den(P) ≤ B} ≍ B(log B)²* is equivalent to ET's N log³N via scaling (averaged; B6).
* **Z2687**: *the ES₅ frieze N-fibre is dP5 minus a pentagon* (Harpaz's log K3 class; non-BM obstruction precedent; disproof side only).
* Disproof-side computations, cheap and open: Z2626 (Br on S_{n,−4}), Z2834/Z2835 (pencil zeros), Z2629 (log³ vs log², see below). The others (Z0785, Z0786, Z0793, Z0871, Z0964, Z0993, Z0997, Z1013, Z1099, Z1289, Z1407, Z1677, Z2114/5/7, Z2141, Z2190, Z2465, Z2500, Z2894) are calibration.

**Recurring missing theorems**
1. *A group action / moves on ES points* (M3; Aut U_n finite, linear in each variable): Z0992, Z1120, Z1164, Z1293, Z1330, Z1369, Z1732, Z2297,
   Z2471, Z2492, Z2493, Z2608, Z2702, Z2813, Z2919. On S_{n,D}, both Vieta moves fix C: Z2735, Z2664, Z2815, Z2866.
2. *Scaling isomorphism U_n ≅ U_1 over ℤ[1/n]* (GEOMETRY_ES §1) kills every n-dependent geometric invariant: Z0787, Z1652, Z1672, Z1676,
   Z1712, Z2042, Z2470, Z2499, Z2686, Z2814. Any 'prime T1' must live in the integral model.
3. *Finer cohomological obstruction* (none: π₁(U_n) = 1, étale-Brauer = BM = ∅): Z1432, Z1671, Z1672.
4. *Restatements* (circular): Z1588, Z2697, Z2793, Z2878, Z1966, Z0998, Z2109, Z2913. 5. *Elliptic/Selmer imports* (no p-dependent curve): Z1712, Z1713, Z2089, Z2090, Z2574.

**New in this pass** (`scripts/z52d_avenue_Q09_primitive_height.py`, < 60 s)
* **Z0866 (PROVED)**: for p ≡ 1 (4) every Type II solution is (abk, pkma, pkmb), gcd(a,b) = 1, m | a+b, p = 4abk − (a+b)/m, gcd = k. Type I is never
  primitive. So primitive ES = the line k = 1, dual to (★) = the line m = 1. (a, m) = (1, 1) solves every p ≡ 2 (3), which explains 'all failures
  ≡ 1 (12)'. Checked on 798 primitive solutions (p < 2600). The failures contain those of the d = 1 shot family (COMPOSITION_ES) plus 277, 373, 853, ….
* **Z0865/Z0898/Z0964 (PROVED)**: every (★) solution has max denominator ≤ p(p+1)/3. So minz(p) > p(p+1)/3 forces R(p) = 0, which explains why
  the height-extremal prime 577 (0.5026 p²) is a (★)-failure (script check p < 2600).
* **Z2868 (PROVED)**: S_{n,D} (diagonal quadratic coefficients (n, 1, 0)) is not affinely equivalent over any field to a Markoff or four-holed-sphere
  cubic ((1, 1, 1)): the cubic part forces a monomial linear part, and translations add no square terms.
* **Z2686/Z2696/Z2617**: BL Lemma 3.10 (finite integral points off the 9 lines at fixed n) settles the A¹-curve and log-height-counting items.
* **Z2629**: the boundary-splitting explanation of log³ vs log² is excluded (the lines and nodes are already rational over ℚ).

**Assessment.** No Q09 architecture escapes M3 or the scaling isomorphism: the geometry of U_n is n-independent and has no moves, so all
p-dependence is in the integral model, i.e. the divisor lottery (B2). The one structurally new fact is the Type II (k, m) plane with
(★) and primitive ES as dual coordinate lines. Next: a primitive-failure census to 10⁷ (cheap) to see whether it thins like (★).
