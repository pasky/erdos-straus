# z52b pass 1 — batch H02 (25 items)

**Summary.** 25 items: covered 15, nothing 9, skipped 1, interesting 0, needs-compute 0.
No item turned up anything promising enough for a depth lane. ES remains OPEN.
New concrete checks: Z0409 (Schinzel N_m, m = 16..40), Z0501 (Δ for residue classes), Z0526 (Harpaz hypotheses), Z0530 ((★) covering vs M),
Z0547 (level-failure frequency), Z0663 (Ramsey-ES refuted), Z0799 (Gaussian angle, null).
Outcomes: `data/z52b/pass1/outcome_H02.jsonl`. Scripts: `scripts/z52b_p1_H02_*`. Data: `data/z52b/pass1/H02/`.

## By-products worth recording (none rises to `interesting`)

* **Z0663 — Ramsey-ES is false (PROVED, elementary).** For prime p > 256 every solution of 4/p = 1/x+1/y+1/z has
  min denominator ≤ 3p/4 and max denominator ≥ p^{3/2}/2.
  * Type I: x = px′ with p | 4x′−1, so x ≥ p(p+1)/4.
  * Type II: x = py′z′/(4y′z′−y′−z′) needs p | 4y′z′−y′−z′, so y′z′ ≥ p/4.
  * Also max ≤ 1.2p⁴.
  * Hence the 2-colouring c(n) = ⌊log₈ log₂ n⌋ mod 2 has no monochromatic solution for every prime with
    log₂ p ∈ [(2/3)·8^{j+1}+2, 8^{j+1}).
  * Data check (p ∈ [300, 3000]): min z/p = 11 at p = 419.
  * Residue-class colourings reduce to numerator problems: mono mod 3 ⟺ 12/p is 3-term representable; mono mod 4
    ⟺ 16/p is.
  * Reproduce: `python3 scripts/z52b_p1_H02_ramsey.py 3000`.
* **Z0409 — Schinzel N_m calibration (EVIDENCE).**
  * Largest exceptional prime of m/p, scanned to p ≤ 3·10⁶ for m = 16..40, plus PW Table 1 for m ≤ 15.
  * Fit for m ≥ 16 (uncensored): log N_m ≈ 2.09·m^{0.505±0.14}, which is PW's exp(m^{1/2}) heuristic.
  * Size of ln N_m/√m: ≈ 1.9–2.4 for odd m, ≈ 2.7–3.3 for 4 | m.
  * The 4 | m excess matches the known persistence of T1 for 4 | m. Brute force confirms that at n = 9..169 Type I/II
    are empty at odd squares exactly for m = 4, 8, 12, 16 (`data/z52b/pass1/H02/t1_general_m.txt`).
  * m = 20, 28, 32, 36, 39, 40 are censored at 3·10⁶. Reproduce:
    `scripts/z52b_p1_H02_schinzel_Nm.sh 3000000; python3 scripts/z52b_p1_H02_schinzel_analyze.py`.
* **Z0526 — Harpaz's conic log K3 theorem does not fit U_n structurally.**
  * Every conic fibration of the Cayley cubic (via an edge line, or via the extra line {y=−x, z=n/4}) has split
    fibres. For the extra-line pencil the residual-conic discriminant is λ², a square.
  * So fibres are G_m-torsors with trivial descent, not norm-1 tori.
  * Reproduce: `scripts/z52b_p1_H02_harpaz_conics.py`.
* **Z0530 — the (★) covering system on n ≡ 1 (4) ≤ 4·10⁶.**
  * Uncovered primes fall from 70 695 (M = 8) to 88 (M = 65 536) to the 12 census zeros (M ≥ 4·10⁶).
  * The decay is ≈ exp(−0.05 (log M)²).
* **Z0799 — null.** |corr(residual log R(p), cos 4kθ_p)| < 0.005 over 69 108 primes in [10⁶, 3·10⁶].
