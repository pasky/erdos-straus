# z52d avenue — batch Q16 (113 items) summary
ES is OPEN. Rows: `out_Q16.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch (logic/complexity, physics analogies, probabilistic models, count statistics): 65 rows are "calibration only", handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 59 | 59 |
| circular | 23 | 0 | 0 | 0 | 23 |
| known-false | 12 | 0 | 0 | 0 | 12 |
| open-plausible | 0 | 4 | 2 | 2 | 8 |
| unclear | 7 | 1 | 0 | 0 | 8 |
| harder-than-open (⇒ deterministic QNR) | 2 | 1 | 0 | 0 | 3 |
Novelty: 0 → 58, 1 → 55, 2 → 0. Plaus-3 rows are calibration lemmas, main-term statements or averaged results (yield none/partial).
**Plausibility ≥ 2 AND novelty ≥ 1 with any yield beyond calibration**: none with ES yield.
* **Z2551**: *the 3/4 exceptional-set bound is effective once the Landau–Page modulus is excised from Bombieri–Vinogradov* (the only ineffective input). Partial result, B6.
* **Z2989**: *for each p, some prime e ≡ 3 (4) has a QNR factor of (p+e)/4*. PROVED here and trivial: (N_e/e) = (e/p). Necessary condition only; the class −1 is B2.
  (Z1074 moment-LP density bound, Z0522 Kolountzakis precedent needing M4: no ES yield.)

**Recurring missing theorems**
1. *Polylog one-coordinate window* (open, plaus 1; FRONTIER §7.2): Z0847 (Vmin ≤ (log p)^A), Z1335 (Cmin ≤ (log p)^A), Z2048(a).
2. *Poly-time solver ⇒ deterministic QNR* (harder-than-open): Z2048, Z2545, Z3035; Z2747 (S¹₂ ⊢ ES ⇒ the same).
3. *Partition function / Lee–Yang / stability non-vanishing* (circular or z45-refuted): Z1127, Z1128, Z1325, Z1365, Z1594, Z1722, Z1726, Z2753.
4. *Janson / Poisson / moment lower tail at fixed p* (= H⁻_BM, or B6 if averaged): Z0473, Z1041, Z1044, Z3109, Z3137, Z0628, Z0629, Z0781, Z1040.
5. *Finite menus / SAT coverings / unavoidable configurations* (B1, B2(iii)): Z2323, Z3004, Z3190, Z1012, Z1132, Z2748, Z2640.
6. *Main term / local factor F* (known-true, B3): Z0823, Z0825, Z0830, Z0906, Z0970, Z1037, Z1733.
7. *Reformulations of ES / ES₅* (circular): Z0161, Z0185, Z0980, Z1367, Z1992, Z2656, Z2680, Z2724, Z1924, Z2296.

**New in this pass**
* **(★) certificates are QNRs** (PROVED, elementary; `scripts/z52d_avenue_Q16_qnr.py`): if M = 4uC − 1 divides p + u, then (M/p) = −1.
  Checked on 15 714 certificates at p < 2·10⁴. So any poly-time (★) solver is a deterministic QNR finder (extends z31_complexity from ES₅ to (★)).
* **Z1924 correction**: Pass 1's AP objection varied p instead of m. With r = qm − p, (★) ⟺ r | (m+1)/4, and on a fixed-q piece this is
  r | p + q with r ≡ −p (mod q): one shift p + q. That is a bounded window (fixed q) or the tied event (growing q).
* **Z3137**: d = 4kC − 1 | 4Cp+1 ⟺ d | p + k. So the C-periodic small-prime pattern and the class condition do not factor: the class condition is the whole event.
* **Z0473**: the item asks whether any log²-count problem without local obstruction fails i.o. Yes: Markoff surfaces (Ghosh–Sarnak; Loughran–Mitankin), already cited in FRONTIER §2.4.
* **Z1954**: Lucas/BHV primitive divisors are the only known family controlling a divisor's *class* (±1 mod n, sign = (D/ℓ)); for ES it restates rank of apparition.
* **Z2680**: Pass 1 measured edges (x, x+1) on F_p, not the forest F_p. Its 0.503 is the trivial value.

**Assessment.** Q16 contains no architecture that escapes B1/B2/B6. The concrete ES-strength open statements are the known
one-coordinate windows (§7.2). The complexity items collapse onto derandomised QNR finding, which is strictly harder than an existence proof.
