# AGENT REPORT O162 — windmills on a general surface Z (branch side-agent/windmill-surface)

Deliverable: `INVOLUTION_ES2.md` (new file, §0–§7), scripts `scripts/inv2_cylinder_check.py`,
`scripts/inv2_formal_check.py`, `scripts/inv2_bt_mass.py`, log `logs/inv2_formal_check_30000.txt`.
ES is not solved.

## Outcome
The O158 status "narrowed, not barred" becomes:
* **barred CONDITIONAL on Bateman–Horn (lower bound)** for every finite-menu affine windmill on X in the class
  of INVOLUTION_ES Thm 5.1 (Cor 6.2.3): for every fixed proper closed Z, `≫ N/(log N)^k` primes
  `p ≡ 1 (24)` have `E(p) ∩ Z = ∅` (Thm 6.1(d));
* **barred CONDITIONAL on H** when every 2-dimensional component of Z is an axis cylinder `C × A¹` (incl. all
  coordinate planes; Thm 5.3). INVOLUTION_ES Cor 5.3 (Dickson, "sketch") becomes a complete conditional proof
  with a simpler prime family;
* **barred UNCONDITIONALLY (100% of primes `p ≡ 1 mod α₀` fail)** when Z has no *Siegel cylinder* component,
  i.e. no `C × A¹` with C carrying infinitely many positive integer points (Thm 6.1(b), Cor 6.2.1; ineffective
  through Siegel's theorem);
* unconditional positive proportion (lower density > 72.28%, certified bound) for the non-plane Siegel cylinder `{t = u}` (Prop 7.1, makes
  INVOLUTION_ES Remark 5.4 rigorous).

## Key new ingredients (all PROVED, elementary)
1. Lemma 2.1: axis lines carry APs with no odd squares (T1 at `n = m²`).
2. Prop 3.2: off axis lines, a non-cylindrical component has `O(N^{2/3})` points with `P ≤ N` (`P+1 ≥ tuv/2`).
3. Lemma 4.1: on axis cylinders the slice divisor divides a fixed polynomial: `A | p^{deg} f(−1/p,−p)`, etc.
4. Lemma 5.1: for `p ≡ 1 (8)`, `x ∈ E(p)`: odd parts of A, B and **uv** all have Jacobi symbol −1 mod p
   (the uv statement is new and is what makes the t-cylinders (e.g. `{v=c}`) work without A-dependent forms).
5. Lemma 5.2: Theorem C's character computation for an arbitrary fixed polynomial R(p).

## Honest residue (§7)
* Unconditional: Siegel cylinders, in particular coordinate planes; each is a half-dimensional sieve problem
  with a prime variable (one plane `{t=3}` ⇔ `(3p+1)/4` has only primes ≡ 1 mod 3; Iwaniec 1974 is the natural
  tool — not checked, not claimed).
* Under H alone: non-cylindrical surfaces (need an admissible prime outside an `O(N^{2/3})` set).
* Outside Thm 5.1's class: unchanged (infinite menus, non-affine maps, n-dependent SL₂, other auxiliary sets).

## Points for the reviewer
* Lemma 5.1 (uv part) and the B part: short reciprocity computations; numerically checked on 647 E-points.
* Thm 6.1(d) needs the *quantitative* BH lower bound (to beat the `N^{2/3}` set), not just H.
* Prop 7.1's constant: floating-point sum to a = 2·10⁵ plus a crude tail bound (script), margin is large.
* Labels: Lemma 5.2/Thm 5.3 "admissible ⇒ empty" PROVED, infinitude CONDITIONAL.

Evidence: `inv2_cylinder_check.py 2000` (Lemma 4.1 on 26031 incidences; bounded search = brute force on 4320
(p,W) pairs); `inv2_formal_check.py 30000 3000` (11 cylinders; QR(p) ⇒ empty, admissible ⇒ QR, no exception);
`inv2_bt_mass.py 200000 2000000`.

## Self-review (reviewer subagent, deep) and repairs applied
No FATAL. Repaired: (MAJOR) the displayed raw Dickson family for the 33 planes had a fixed prime divisor 5 —
now stated as the Theorem M normalised family `h(My+q̃)/C_h` with `E_ℓ > max v_ℓ(C_h)`; (MAJOR) Prop 7.1 tail
bound now certified (Decimal rounded-up partial sum + `φ(n) ≥ 0.375 n^{0.9}` tail), μ < 0.13860; (MINOR) BH
exponent `|S|`, F ⊆ {p ≡ 1 (4)} in Cor 6.2, α₀ divisible by 24, "other than p" restored, Siegel-cylinder
definition (condition on C), "truth ≈ 0.87" wording. Reviewer independently re-derived Lemma 5.1's symbols.
