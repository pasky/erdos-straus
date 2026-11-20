# An arbitrary finite tuple of integral negative-Pell witnesses compresses to one

(§0 block: z74 Opus xreview fix)
```
Result: any fixed number of INTEGRAL negative-Pell witnesses compresses to the fundamental one (bounded-value gap
        lemma), so polynomial menus over ℚ(P) in them inherit both conclusions of PELL_ES_MENU_NOGO.md.
Label: PROVED (rel. PELL_ES_MENU_NOGO.md and its cited theorems). Unconditional.
Scope: integral witnesses only (independent rational witnesses are NOT covered, example in §Boundary); fixed finite
       menu and arity; not a statement about ES.
Review: cross-model (Claude Opus), data/z74/xreview/REVIEW_PELLNOGO_OPUS.md — ACCEPT-WITH-FIXES (§0 only).
Triage: BARRIER-BROAD
STATUS delta: none (see PELL_ES_MENU_NOGO.md).
```

**Theorem (ordinary primes, unconditional).** Fix any finite menu of triples of polynomials in `x₁,y₁,…,xᵣ,yᵣ` over `ℚ(P)` (so the arity may vary over the menu). At an ordinary prime p, a selector may use **any integral tuple** with `xⱼ²−pyⱼ²=−1`, including arbitrary signs, repetitions and unbounded powers. There is a computable primitive unit-square progression inside `1 mod 840` on which **no prime** yields a positive integral ES triple by these rules. On a computable progression `1 mod M`, `840|M`, at most `O_menu(√B)` primes up to B succeed. The progressions need not be the same. These are no-go results for the rules, not for ES or negative Pell.

**Reduction to one generator.** At a prime admitting an integral witness put `s=√p`. Use the units of **the order `ℤ[s]`**, not necessarily those of the maximal order. The positive units form a cyclic group: in any fixed interval `[1,B]` the conjugate of a unit has magnitude ≤1, so its two integer coefficients are bounded. Since a negative-norm solution exists, changing sign and inverting if needed gives a unit >1; the least such unit ε generates by division by its powers. Its norm must be −1. Write `ε=x₀+s y₀`; its conjugate is `−ε⁻¹`, so both integer coordinates are positive and `ε>√p`. Every input unit has the form `δⱼ ε^{nⱼ}`, `δⱼ=±1`, `nⱼ` an **odd, possibly negative** integer. Absorb the δ's by a finite choice of simultaneous sign changes of each coordinate pair.

**Bounded-value lemma.** For each fixed polynomial f and fixed height exponent, all values `m=f(p,x₁,y₁,…,xᵣ,yᵣ)` of absolute value at most `2p⁴` (or any fixed polynomial bound) are values of an effectively finite list of polynomials in `(x₀,y₀)` over `ℚ(P)`. Finitely many coefficient poles are excluded. No bound on ε or the n's is required.

To prove it, use the formal variable `s²=P` in the coefficients and `Zⱼ=ε^{nⱼ}` at evaluation. After sign choices substitute

```
xⱼ=(Zⱼ−Zⱼ⁻¹)/2,        yⱼ=(Zⱼ+Zⱼ⁻¹)/(2s).
```

Thus `f=Σ_{α∈I} c_α(s) Z^α`, a fixed Laurent polynomial with `N=|I|`; the zero polynomial is immediate. The involution on the formal expansion is `s↦−s, Zⱼ↦−Zⱼ⁻¹`, so `I=−I` and `c_{−α}=(-1)^(Σαⱼ) σ(c_α)`. At p put `k_α=α·n`; this has the parity of `Σαⱼ`. Quadratic conjugation therefore sends the **whole term** `c_α ε^{k_α}` exactly to the `−α` term, also for signed n's and exponent zero.

Choose an integer `A≥1` so that, uniformly in p off the poles, `N, |m|, |c_α|, |σ(c_α)|, D ≤ p^A`, where `D=D(p)≥1` is a common rational **integer** denominator with `D c_α∈ℤ[s]` for all α. Such A is computable: write each coefficient `(a(P)+s b(P))/d(P)` with integer polynomials, take the product of the absolute nonzero denominator values, and bound both numerators and denominators polynomially in p (`|d(p)|≥1`). This cost does not involve a Pell witness.

Insert 0 below the sorted **distinct positive** exponents. If a consecutive gap from h to e has `e−h>14A`, take the *lowest* such gap. Factor the entire tail with exponents at least e as `ε^e L`, where `L=Σ_{k_α≥e} c_α ε^{k_α−e}`. Here e is the **least** exponent in the tail. Since the offsets are nonnegative and `|σ(ε)|<1`, `|σ(L)|≤N p^A≤p^{2A}` regardless of the spread above e. If L is nonzero, `DL` is a nonzero algebraic integer, and `1≤|Norm(DL)|=D²|L σ(L)|` forces `|L|≥p^(−4A)`. But all terms below e have exponent ≤h, including every negative exponent. Hence

```
p^(−4A) ε^e ≤ |ε^e L| ≤ |m| + N p^A ε^h ≤ p^(3A) ε^h,
```

contradicting `ε>√p` and the chosen gap. The top tail thus sums **exactly** to zero; its conjugate, the full tail of exponents ≤−e, also vanishes. Delete both. Ties never need to be separated, and no individual term need vanish. All surviving positive exponents are ≤`14AN` because all intervening gaps from zero were small; the same holds in absolute value on the negative side. If there was no large gap, the bound already holds without deletion. Opposite indices are kept or deleted together; no division by a tied coefficient or specialized coefficient is used.

**Symbolic descent, not interpolation at the chosen p.** Enumerate symmetric retained subsets of I, assigning integers `|k_α|≤14AN` with `k_{−α}=−k_α` and `k_α≡Σαⱼ mod 2` (exponent zero included when allowed). This is finite and contains every surviving pattern, without testing realizability by actual n. In the algebra `ℚ(s)[U,V]/(U²−PV²+1)` put `T=U+sV`, `T⁻¹=−U+sV`. Each candidate `Σ c_α T^{k_α}` is regular in U,V, even for negative exponents. Conjugation fixing U,V sends `T↦−T⁻¹`; by the subset symmetry and parity this sum is invariant. Explicitly replace powers by the two displayed linear polynomials and average the resulting polynomial with its coefficient conjugate: this gives a representative in `ℚ(P)[U,V]` of the same class. It evaluates to m at `(x₀,y₀)` for the retained pattern. Different coordinates can use different patterns; their finite Cartesian product still uses **the same generator**. No square root of P is adjoined to the final formula coefficients.

**Application.** For sorted ES denominators `u≤v≤w`, positivity and discreteness give `u≤3p/4`, `v≤2pu/(4u−p)≤2pu`, `w=puv/(4uv−p(u+v))≤puv≤2p⁴`. Apply the lemma to all three output coordinates, regardless of slot order. Now apply the `ℚ(P)` version of `PELL_ES_MENU_NOGO.md` to the resulting one-witness menu: its rational-witness prohibition includes the integral generator at every successful prime. This gives both stated conclusions, handling finitely many exceptional primes by refinement in the all-miss progression. In the compression itself there is **no thin exceptional set** depending on powers or cancellation. In fact if `ε>p^{7A}`, even the first positive exponent starts a tail forced to vanish by the same inequality, so only exponent-zero terms are needed for that coordinate.

**Boundary.** The lemma only used the polynomial bound on m and its being an evaluated rational polynomial value, not output integrality for the gap estimate. But integer **inputs** provide the cyclic group, large generator and integral powers. For example for `p>5` the norm-one element `(s+1)/(s−1)` has nonintegral trace `2(p+1)/(p−1)`; no positive power can be an algebraic integer (integrality would descend by the monic power equation). Multiplying ε by it gives a rational negative-Pell witness outside the integral power group, even multiplicatively independent of ε. The finite-menu compression proved here is not a result about independent rational witnesses, a number of inputs growing with p, or formulas involving division by witness-dependent expressions.
