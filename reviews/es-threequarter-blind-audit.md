# Blind soundness audit of `paper/es-threequarter-note.tex` (task a1)

Target: Theorem 1.1, `E(N) ≤ C N exp{-c (log N)^{3/4}}` (all denominators).
Auditor: side agent a1, worktree `erdos-straus-claude-agent-worktree-0004`.
Version audited: the note as of commit `e130c0e` (1431 lines).

Protocol followed. The verdict below was written and committed **before**
I opened `reviews/es-threequarter-note-review.md`,
`reviews/wave32-sec76-review.md`, `reviews/es-threequarter-note-check.py`,
or any review of §§16/34/39/76. Before the verdict I read only the note,
Shiu's Theorem 1 (sources/shiu-1980.pdf, pp. 162–163, from page images),
and my own scripts. I did not need notes.md: the note is self-contained
for the load-bearing route.

## Blind verdict

**SOUND.** I found no load-bearing defect. Every step of the load-bearing
route re-derives with the stated uniformities. That route is §5
(unpruned supply) → Cor 3.x fibre masses → the conditional-independence
proof of Thm 6.3 → Lemma 7.1 (void) → Lemma 8.1/Thm 8.2 (Bonferroni
assembly) → §9 (primes and Rankin transfer). The defects I found are
cosmetic or expository, listed below. None changes a statement.

Label recommendation: keep "INTERNALLY PROVED; not externally refereed".
This audit adds one independent internal check. It does not replace an
external expert reading. My confidence is high for the logic and
bookkeeping. The analytic inputs (Shiu Thm 1, Montgomery–Vaughan BT,
Bombieri–Vinogradov) are used within their standard published ranges.
Shiu's hypotheses were checked against the scanned paper.

### Re-derivation, step by step (load-bearing route)

Notation: `t = log X`, `K = ⌊X^κ⌋`, `κ < 1/240`, `H = K^10`,
`z = x^{1/6}` on the block `(x, 2x]`, `L = log N`.

1. **Atoms and the identity (Lemma 2.1).** `4uv | kℓ+1` and
   `nv ≡ -u (kℓ)` give `4/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)`. Checked
   algebraically and on toy atoms (script §3). Exceptional integers avoid
   every atom. ✓
2. **Distinctness / CRT (Lemma 2.2).** Suppose two atoms at the same ℓ
   have the same projection. Then `ℓ | uv'−u'v` and `|uv'−u'v| < z² =
   x^{1/3} < ℓ`, so `(u,v) = (u',v')`. Then `k ≡ k' (4uv)` with `4uv >
   4H² > K`, so `k = k'`. Every ℓ satisfies `ℓ > X^{1/2} > K`, so ℓ is
   coprime to `L_K` and to `P_y`. Conditional on `c = n mod L_K` (and on
   `n mod P_y`), the coordinates `n mod ℓ` are independent and uniform.
   An atom is active iff `k | u+cv`. Then
   `H_X = Σ_ℓ I_ℓ` with independent `I_ℓ ~ Bernoulli(f_c(ℓ)/ℓ)`. ✓
   Toy check: the exact CRT values of `E H` and `E (H)_2` (pair sum with
   lcm probabilities) equal the fibre averages exactly. Monte Carlo
   `P(H=0)` matches the averaged product formula (script §3).
3. **Moment order uniformity (Thm 6.3, conditional-independence proof).**
   `E[(H)_m | c] = m!·e_m(p_ℓ) ≤ μ_c^m` holds exactly. Its only input is
   `μ_c ≤ C_u t³` for **every** c, so the only constant raised to the
   power m is `C_u`. That is absorbed in step 6 by `D_B > e·C_u`. There
   is no hidden `C^r`. ✓
4. **Upper fibre mass (Cor 4.3).** An active atom has `(k,c) = 1`, so
   `k ∈ J_c`. BT (MV form) at `q = 4uv ≤ 4x^{1/3}` gives `≪ x/(φ(q) log x)`.
   With `φ(4uv) ≥ 2φ(u)φ(v)` (checked) and the lattice upper bound
   `Σ_S 1/(φ(u)φ(v)) ≪ φ(k)k⁻²Λ²` (re-derived via the `1/φ` divisor
   expansion; the secondary terms are absorbed since `H = K^10`), we get
   `Σ_ℓ f_c/ℓ ≪ t²h(J_c) ≤ C t³`, uniformly in c. ✓
5. **Lower fibre mass (Thm 5.2 + Lemma 5.1).**
   * The main term uses `li(2x)−li(x) ≥ x/log 2x`, `1/φ(4uv) ≥ 1/(4uv)` and
     the lattice lower bound `≥ (1/4)φ(k)k⁻²Λ²`. I re-derived the latter
     by Möbius inversion of `(u,v)=1`. The relative error is
     `O(τ(k)k²/(φ(k)H)) = O(K^{-8})`, and the coefficient is
     `≥ 6/π² > 1/4`. The main term is therefore `≫ x·t·h(J)`.
   * Error term: group by `q = 4uv`. At most `2^{ω(q/4)}` ordered coprime
     factorisations give `W_c(q)² ≤ 2^{ω(uv)} Σ r²`. Cauchy–Schwarz
     against `Σ_{q≤4x^{1/3}} E*(q) ≤ C_R x (log x)^{-R}` (BV, fixed R,
     unconditional; Siegel zeros affect effectivity only) and the BT
     bound `E*(q) ≪ x/(φ(q) log x)` give
     `(x t⁶)^{1/2}(x t^{-26})^{1/2} = x t^{-10}`.
   * Lemma 5.1: expanding `r²` gives the single congruence
     `[k,k'] | u+cv`, with `d ≤ K² ≤ U^{1/5}` and a reduced residue.
     Shiu applies to `F = 2^ω n/φ(n)` (hypotheses (i), (ii) and
     `k < y^{1−α}`, `x^β < y ≤ x` verified against Shiu p. 162–163). The
     local factor `exp(−Σ_{p|d} 2/(p−1)) ≍ (φ(d)/d)²` gives a box sum
     `≪ log U·φ(d)/d²`. The outer v-sum is `≪ (log z)²`. The pair sum is
     `Σ φ([k,k'])/[k,k']² ≤ Σ (k,k')/(kk') ≪ (log K)³`, checked
     numerically on toys.
   * The modulus-one case is handled elementarily. Uniform in c, J, K. ✓
   * The weights over composite moduli 4uv are handled correctly: BV is
     used only through `Σ_q E*(q)` with `E* ≥ 0` a max over reduced
     residues, at level `4x^{1/3} ≪ x^{1/2}(log x)^{-A}`.
6. **Void (Lemma 7.1).**
   * `S_y = 1` forces `(c,p) = 1` for every `p ≤ y` with `p | L_K`.
   * `h(J_c) ≥ h(𝒦) − Σ_{p|c, y<p≤K, p|L_K}(1+log K)/p ≥ (a₀−2Z) log K`.
   * The events `p | n` for `p > y` are CRT-independent of the selector.
     `E e^{yZ} ≤ exp((e−1) y Σ_{p>y} p^{-2}) = O(1)`, so
     `P(Z > η) ≤ e^{−ηBt³+O(1)}`.
   * On `Z ≤ η`: `P(H=0 | c) = Π(1−f_c/ℓ) ≤ e^{−μ_c} ≤ e^{−a t³}`.
   * `B` is chosen after `a_v`, as stated. ✓
7. **Bonferroni and depth (Lemma 8.1, Thm 8.2).**
   * Bonferroni identities: `Q_r(h) = C(h−1,r)` for `h ≥ 1` and
     `1_{h=0} ≤ Q_r ≤ 1_{h=0} + C(h,r+1)`. Checked exhaustively for
     `r ≤ 30`, `h < 120`.
   * `E[C(H,r+1)|S] ≤ (C_u t³)^{r+1}/(r+1)! ≤ (eC_u t³/(r+1))^{r+1}
     ≤ exp(−D_B log(D_B/(eC_u)) t³)` once `r+1 ≥ D_B t³`. ✓
8. **Level and ledger.**
   * Every term of `S_y·Q_r(H_X)` is a single class (or empty) of modulus
     `≤ P_y(KX)^r = e^{O(t⁴)}`. Each is counted on `[1,N]` exactly as
     `N/q + O(1)`. That holds for every q, including `q > N`. No
     prime-distribution input is used at level N, so no BV/BT level
     budget arises for these moduli.
   * Ledger: `T_abs ≤ 2^{π(y)}(r+1)|𝒜|^r`, `|𝒜| ≤ K X^{4/3}`,
     `log T_abs ≤ C_L t⁴`. The ledger is honestly `e^{O(rt)}` with
     `r ≍ t³`.
   * So `Σ_{n≤N} ν ≤ N e^{−c t³} + e^{C_L t⁴}`. ✓
9. **Optimisation.** Take `t = α L^{1/4}` with `C_L α⁴ ≤ 1/2`. Then
   `T_abs ≤ N^{1/2}` and the saving is `c α³ L^{3/4}`. The exponent is
   exactly 3/4, with no ε loss. Every parameter is fixed before α, in the
   order the note states. The omitted range `max(K,y) = e^{O(L^{1/4})}`
   is negligible. ✓
10. **All denominators (Rankin).**
    * Every prime factor of an exceptional n is exceptional. Take
      `δ = η₀ L^{-1/4}`. Since `u^{1/4} ≤ L^{1/4}` on `[log x₀, L]`, the
      bound `δu ≤ η₀u^{3/4}` holds there.
    * The partial-summation integral `∫ e^{−(c₀−η₀)u^{3/4}} du`
      converges. The higher prime powers contribute `O(Σ p^{-3/2})`.
    * Hence `E(x) ≪ x^{1−δ}`. ✓

I also replayed the non-load-bearing ordered-atom proof of Thm 6.3. The
prime-power table (34) was checked by brute force on `Z/p^E`, with and
without the unit selector. Also checked: the `φ(q₀)²/φ(g)` unit-pair
count, the Euler-factor ratio `1 + O(p^{-2})` of Lemma 6.2, the
cancellation (35), and Lemma 6.1's Shiu application. All correct.

The retained original route (§4: low-ω Lemma 3.3, congestion Lemma 4.1,
Thm 4.2) also checks. Its tail needs only `D log(3/2) > 1`. Its
multiplicity is `W_good(q) ≤ t^{4+D log 2}` with `R > 4 + D log 2 + 10`.
Its removed `1/φ` mass costs only `O(log t)`.

### Defect list (blind)

All defects are cosmetic or expository. None is load-bearing.

| # | Severity | Line | Quote | Fix |
|---|---|---|---|---|
| B1 | cosmetic | 423–424 | "Fix any integer $D$ with $D\log(3/2)>1+2$" | The tail exponent is `(log z)^{1−D log a₀}`, so `D log(3/2) > 1` suffices. "1+2" is an unexplained overkill. Write `>1` (or explain the slack). |
| B2 | cosmetic | 22 | "for the\ Erd\H{o}s" | Stray forced space in the title. |
| B3 | expository | 324 (Lemma 3.1 proof) | "$+O\left(\frac{\Lambda\tau(k)\log z}{H}+\frac{\Lambda^2}{H}\right)$" | The `d ≤ H` error is really `O(Λτ(k) log H / H)`, and the tail is `≤ (1+log z)²/H`. The displayed form is correct but loose. No change needed. |
| B4 | expository | 1103 (Thm 8.2) | "at least one on every exceptional prime $n>\max(K,y)$" | Only `n > y` is needed (`S_y(n) = 1`). The extra `K` is harmless. |
| B5 | expository | 942–981 | The ordered-atom replay is presented as a full second proof. | The replay is correct as written (table and cancellation verified), but its iteration step ("Iteration over ordered compatible distinct atoms") leaves implicit that compatible distinct atoms have distinct ℓ. Lemma 2.2 gives this, and that is what makes `P(∩) = Π` relative probabilities with fresh `1/ℓ`. A one-clause cross-reference would help. |

No repaired `.tex` is needed for soundness. I did not edit the note in
this blind phase.

### Numerical sanity checks

`scripts/es34_blind_audit_checks.py` (run:
`PYTHONPATH=scripts uv run python scripts/es34_blind_audit_checks.py`).
All 16 checks pass. They cover:

* Bonferroni identities.
* Exact `E(H)_m = m! e_m ≤ μ^m` for Bernoulli sums.
* Toy-family distinctness and CRT `E H`, `E(H)_2`, `P(H=0)` against the
  fibre formulas.
* `h(𝒦(K)) − (2/π²) log K → 0.7548` (bounded), and the removal bound
  (16).
* `φ(4uv) ≥ 2φ(u)φ(v)`.
* The prime-power table (34), the Euler ratio, and the unit-pair count.
* The §10 classes `−4D`, `D | A²`, and the `τ(A²)` bounds.
* The pair sum `/(log K)³`.
* Symbolic `3/4` bookkeeping.

These are algebra and probability checks on toy parameters. They are
**not** evidence in the asymptotic regime (`H = K^10`, `z = x^{1/6}`),
which is computationally unreachable.

The note compiles cleanly (`pdflatex` ×3, 21 pages, no undefined
references).
