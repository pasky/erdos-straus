# AGENT REPORT O117 — the m/p density transition under Selberg's eigenvalue conjecture

Branch `side-agent/mn-sel-transition`. Deliverable `EXCEPTIONAL_MN4.md`, script `scripts/emn4_checks.py`
(+ `.out.txt`), self-review `reviews/emn4-selfreview.md` (deep reviewer: no FATAL/MAJOR; minors R1–R6 applied).

## Results (labels as in the file)

1. **Thm 4.1 (= Thm I_m; CONDITIONAL on (SEL_m)).** For `4 ≤ m ≤ L^5`, N ≥ N₀:
   `Σ_{N/2<p≤N} f_{I,m}(p) ≪ N(L² + L log² m)/m + N m^{−0.35}/L`. It is the m-uniform version of TTL Thm 8.1 ((D)32).
   (SEL_m) means no exceptional eigenvalues for `Γ₀(mdq²)` with even nebentypus mod q. It is implied by
   Selberg's conjecture for all `Γ₁(M)` and belongs to the same hypothesis family as TTL's.
2. **Thm 5.1 (= Thm L''; CONDITIONAL).** For all m ≥ 4 and N ≥ 16: `ρ_rep ≪ (L³ + L² log² m)/m + m^{−0.35}`, i.e. MN3 Thm L' without `log L`.
   The range `m > L^5` is unconditional (Lemma 0.1, from MN3 L' and MN2 Lemma 3.5).
3. **Thm 5.2 (sharp order; lower half CONDITIONAL, upper half = MN2 Thm U, unconditional).** For each ε there are
   `c_ε, A_ε, m_ε` such that for `m ≥ m_ε`: `log N ≤ c_ε m^{1/3}` ⇒ `ρ_rep ≤ ε`, and `log N ≥ A_ε m^{1/3}` ⇒ `ρ_rep ≥ 1−ε`.
   So under SEL the transition is at `log N ≍ m^{1/3}`, with matching orders on both sides. Profile: `ρ_rep ≪ A³` for
   `m^{−0.11} ≪ A ≪ 1`. Conj C2 (no sharp threshold constant) is untouched.
4. **Unconditional (§6).** The lower side stays MN3 Thm L'. The Kim–Sarnak strip of TTL §9 transfers unchanged, so this
   argument gives no unconditional gain. The new unconditional ingredients are:
   * Lemma 1.1, the reduction for general m;
   * a parity-free level-md normalisation `[f, 2mad, mde]` (separation `cosh ≥ 3/2`, sharp);
   * local densities, class counts `≪ √(md) log` without the `r(md)` factor, and the (K_a) count with modulus `ma²`;
   * §3, Brun–Titchmarsh and mass bounds with the exact `φ(m)/m` coprimality gain.

## How uniformity in m was handled (the point the parent asked about)

* **Remainders.** m enters polynomially (`(md/A)^{1/2}` spectral, `m^{1/2}A/D` Weil). Since `m ≤ L^5` costs nothing
  (Lemma 0.1), these are `L^{O(1)}` and are absorbed by TTL's `L^C` (the layers `k ≤ C₁ log L` go to BT).
* **Main terms.** The sieve cannot use `ℓ | 2md`, which loses `g(m) = m/φ(m)`. This loss is paid exactly by the gain
  `h = φ(m)/m` of the masses. The gain comes from the divisors f, e of `ma²d+1`, which are coprime to m: MN3 Prop 2.3
  with `k = m·…`, the root sums `ρ_{md}(f)`, and Prop 7.1_m's `X_a ≍ Dφ(ma²)/(ma²)`. Note that `Σ 1/φ(mx)` has
  **no** gain, so every BT sum takes its gain from f/e/τ_m.
* **Characters mod m.** They appear only as `χ_{−4md}` in the mean square of `L(1,χ)` over d. That bound is uniform
  only for `D ≥ L^{100}`, and the all-ranges extension is **false** (CRT counterexample in §3). So the whole region
  `D ≤ L^{100}` is removed from the spectral part and handled by aggregated BT in c. This costs
  `(N/m)L(log L)³ ≪ NL²/m`, because the region is thin.
* **Levels.** The levels are `mdq²` and the discriminants `−4md`. For odd m, content-2 forms appear when `md ≡ 3 (4)`;
  they add `h(−md)` to the class count. There is no parity subgroup.

## Caveats for the parent's review

* §§2–3 were drafted by two deep subagents and then checked by me and by the deep self-reviewer. Their own "Issues"
  lists are kept at the ends of §2 and §3. They include a correction to TTL: (b3) only justifies `N^{−δ/4}`, not
  `N^{−δ/2}`, which is still enough for TTL's κ = 1/4. They also note that TTL's intermediate `λ^{−ε} ≤ F^ε` needs `q ≲ A`,
  while the final bound does not.
* The proof is "TTL with changes written out". It inherits everything TTL Thm 8.1 cites: the DI/Drappeau large sieve,
  Prop 5.1, and the reduction. It is not machine-checked; the script checks only finite identities and gives a
  small-range diagnostic of the h-scaling.
* No independent hostile review has been done yet. Suggested focus for one: §3.2(c) (mean square uniform in m, the
  (3.2.1)/(3.2.2) split), §3.5 (low-D aggregated BT, sieve denominator `G(z) ≥ c h(2mcs) log z`), and §4 (2b-0)/(b5).
