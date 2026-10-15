# AGENT_REPORT O237 — pushing the pointwise cap down (spark relay Z7)

Branch side-agent/cap-down (merged side-agent/cap-pointwise and main incl. R238/R239). Main file CAP_DOWN.md; memos
BRAINSTORM/z13_{even_windows,pollack_quarter,gluing_negative,order3_anchor}.md; scripts scripts/z13_*; data
data/z13_*. **ES is not solved; no infinite case of ES is claimed.**

## SHARP:
1. **e*(n) ≪_ε n₀^{1/4+ε} for every non-square n ≡ 1 (mod 8)** (n₀ = squarefree part; e*(n) = 0 if some prime ≡ 3 (4)
   divides n). Also n₀^{1/2+ε} for n ≡ 5 (8), and p^{1/4+ε}/p^{1/2+ε} for odd squares via d = n/p. These are PROVED
   relative to Pollack, IJNT 10 (2014), Thm 1.4 (detector forms; Burgess + Vinogradov–Linnik; ineffective via Siegel),
   read from the author's PDF. O236 had rad(n)^5. Key input (Thm 1.2, PROVED, elementary): **even windows fire.** With
   K = (n+q)/4 = 2^t K′ and d = 2^t·Q′² (odd 2-exponent ≤ 2t is allowed), every prime q ≡ 3 (4) with (q/n) = −1 is a
   forced window, except (n ≡ 5, q ≡ 3 (8), v₂(n+q) odd). So the detector is (1−χ₋₄)(1−χ_{n₀}), with W = 4n₀.
2. **Discrete-log-free witness:** d = K·s^{ord_q(s)/2} (s | K a non-residue with odd exponent) gives cap ≤ (q−3)/4,
   sharp at a single window.
3. **Dictionary (order 3, Prop 6.1):** in ES the window constant (n + m = 4x) equals the shot constant (n + 4Q²), so
   only −1 must be self-generated, and reciprocity forces that. In TES the constants differ by 2ω, and the anchor
   numerator 2 must lie in ⟨primes of x⟩μ₆: a necessary condition that is a subgroup-membership lottery. The
   "degree-2 accident" of (J)19 is why the O236 theorem exists (Assessment).

## Results by goal
1. Goal 1 (spark 1): exponent 1/4 for n ≡ 1 (8), 1/2 otherwise (Cor 2.1).
   * The n ≡ 5 (8) half is a method barrier (Z7-2, Assessment). The bad windows' forced non-residue is 2 itself.
   * Any detector excluding the bad windows carries two conductor-n₀ characters in each of ξ±. Equivalently, it needs
     a 2-dim Burgess bound for χ(a² − 2b²) at side n₀^{1/8}.
   * In a variant allowing even 2-adic denominators, the exponent would be 1/4 for all n.
2. Goal 2 (spark 2):
   * General Type II window with cap: Lemma 1.1, and Lemma 3.1 for all D₁ at fixed x.
   * The cap is ≤ (q−3)/4 at every forced window, and exactly (q−3)/4 when K is a primitive prime. So for each fixed
     forced q, the explicit class {n : q is a forced window} has the absolute cap (q−3)/4, e.g. ≤ 2 for (11/n) = −1
     in the admissible 2-adic classes.
   * Nothing below the forced level is provable this way: cap 0 is −1 ∈ Σ_m(K), which is B2.
3. Goal 3 (spark 4), negative with narrow scope (Prop 4.1(b)):
   * At composite forced windows, the one-prime witness's odd orders combine by lcm.
   * One solution has one x, and K(m) is affine in m, so there is no multiplicative gluing.
   * T1 kills every Lemma-1.1 window at odd squares (Jacobi proof, §3).
4. Goal 4 numerics (EVIDENCE, every reported solution rebuilt exactly against Def 1.1):
   * Full Lemma-1.1 family: all 39 175 primes p ≡ 1 (4) ≤ 10⁶ have cap 0 at a window ≤ 63 (record p = 87 481).
     O236's "max 3" was the square-shot artefact.
   * All 87 759 relevant non-squares ≤ 10⁶ have cap 0 except n = 3985 (cap 1).
   * Odd squares: no windows.
   * Forced windows: least forced window mean 13.5 → 7.6 (p ≡ 1 (8)) and 21.3 → 14.6 (p ≡ 5 (8)); Prop 1.3 cap ≤ 47.
5. Goal 5 (spark 5): Prop 6.1 (necessary condition; negative within that window shape).

## Self-review (deep reviewer subagent): main results confirmed, repairs applied
* Confirmed: Lemmas 1.1/3.1, Thm 1.2, Prop 1.3, the Pollack application (hypotheses, W = 4n₀ and 256n₀²), the
  divisor routes, T1, and Prop 4.1(a).
* Repaired:
  * Prop 4.1(b) needed hypotheses and its formula was wrong (counterexamples n = 5, m = 567; n = 113, m = 1587;
    n = 12437, m = 63).
  * The 2-adic-variant witness is restricted to the excluded case.
  * δ_p = +1 means p | y, p ∤ z (not "p ∤ y").
  * Prop 6.1 is now stated as a necessary condition only, with the unit factor of x handled.
  * Minor fixes: the Siegel citation location, and wording.
* **For the parent:** the reviewer flags `scripts/review_r239_composite_squares.py` (called from main's verify.py)
  as building list(range(10⁸)), about 3.7 GiB, with no memory guard. That script is not mine; please check it.

## Sparks (not pursued)
1. Effective version of Cor 2.1: Pollack's residue is L(1, χ_{−4n₀}). Replacing Siegel with h ≥ 1 (or Goldfeld) should
   give an effective exponent between 1/4 and 5.
2. Many forced windows: Pollack (arXiv 1508.05035) gets ≫ n^κ character non-residues below n^{1/(4√e)+ε}. If this
   extends to the detector (1−χ₋₄)(1−χ_{n₀}), there are many forced windows ≤ n^{1/4+ε}. Could the minimum over them of
   (ord_q(s)/2 − b)/2 be shown ≪ n^{1/4−δ}? That would need an ord_q(s) that is small for one of them, a
   Fouvry–Iwaniec/Erdős–Murty-type statement about q | s^j − 1 in thin sets.
3. n ≡ 5 (8): is there a window shape where the forced non-residue is never 2 (e.g. via a divisor d ≡ 1 (8) with
   rad(n/d) | d), or a 2-dim Burgess bound for χ(a² − 2b²) beyond Chang's side p^{1/4}?
4. Growth of the least Type II window m₀(p): ≤ 23 for p ≤ 2·10⁴, ≤ 63 for p ≤ 10⁶. Is it ~ log p? Compare with the
   polylog lottery (B3).
5. Order 3: TES-like normalisations whose shot and window constants agree up to μ₃·cubes. Does the anchor calculus
   force such a normalisation to be Lagrangian (no T1₃)?
