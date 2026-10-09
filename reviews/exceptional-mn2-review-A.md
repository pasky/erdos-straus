# R102A — hostile review of EXCEPTIONAL_MN2.md (task O102), reviewer A

Reviewed: `EXCEPTIONAL_MN2.md` at `side-agent/mn-transition` (merged into this worktree),
`reviews/agent-reports/AGENT_REPORT_O102.md`. Dependencies consulted: `EXCEPTIONAL_MN.md`
(Def 1.2, Lemmas 1.1/1.3, Prop 3.1, Cor 3.2, Lemma 4.1, Cor D), `paper/es-threequarter-note.tex`
(lem:Bonferroni, eq:parameters), Shiu 1980 (`sources/shiu-1980.pdf`, scanned; pp. 161–162 read as
images, Theorem 1 from memory of the standard statement — conditions `(a,k)=1`, `k < y^{1−β}`,
`x^α ≤ y ≤ x`, F ∈ M), PW `sources/pw.txt` / PDF.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (reduced CRT model) | SOUND (rel. MN Cor 3.2) |
| Lemma 1.2 (multiplicity S_2) | SOUND (minor presentational defects) |
| Theorem 1.3 | SOUND (rel. MN Cor 3.2, BV, BT, Shiu) |
| Theorem U | SOUND; label "PROVED rel. MN Cor 3.2, BV, Shiu" justified. Wording of "removes the (log m)^{4/3}" needs a qualifier (D-U1) |
| Theorem L / §3 | see below |
| §2 numerics | see below |

## 1. Theorem U — line-by-line re-derivation

**Lemma 1.1.** Re-derived.
* CRT: `ℓ > X^{1/2} > K` (note eq:parameters: `ℓ ∈ I_j ⊂ (X^{1/2}, X]`), so `ℓ ∤ L_K` and
  `(Z/𝓜)^× ≅ (Z/L_K)^× × Π (Z/ℓ)^×`; coordinates independent and uniform. ✓
* Activity: atom event `n v ≡ −u (mod kℓ)`; mod k with `k | L_K` this reads `k | u + cv`. ✓
* At fixed ℓ, distinct atoms have distinct classes mod ℓ: same (u,v) ⇒ same k (MN 1.3(iii):
  `k ≡ k' (mod muv)`, `|k−k'| < K < H² < muv`); different coprime pairs ⇒ `0 < |uv'−u'v| < z_j² < ℓ`. ✓
  The classes `−u v^{−1}` are nonzero mod ℓ (`0 < u < ℓ`). So given c, the number of hits at ℓ
  is Bernoulli(`f_c(ℓ)/(ℓ−1)`) under the uniform-unit law, independent over ℓ. ✓
* `P(H=0|c) = Π(1−p_ℓ) ≤ e^{−Σp_ℓ} ≤ e^{−μ_c}`; `E[C(H,r+1)|c] = e_{r+1}(p) ≤ (Σp)^{r+1}/(r+1)!`. ✓
* Bonferroni: `Q_r(h) = C(h−1,r) ≤ C(h,r+1)` for h ≥ 1, r even (note lem:Bonferroni). ✓
  (Numerically re-checked, `scripts/review_emn2A_identities.py`.)
* Key input: MN Cor 3.2 lower bound on **every** `(c, L_K) = 1`. For such c, `𝒥_c = 𝒦_m(K)`
  (all k coprime to m), and Cor 3.2's lower bound `a_u t³/m` comes from Prop 3.1 with 𝒥 = 𝒦_m(K) and
  Lemma 2.1(a),(b) (needs `K ≥ m²`, guaranteed by `m ≤ t³ ≤ K^{1/2}` for X ≥ X_0). This is a
  statement about the distribution of the *primes ℓ*, not about n, so it applies to every
  reduced fibre with absolute constants. I see no hidden m-dependence: Prop 3.1's only use of
  m-size is `φ(m) ≤ t³` against a BV error `(log x)^{−13}`, absolute once X ≥ X_h. ✓
* `(2eC_u s/(r+1))^{r+1} ≤ e^{−(r+1)}` for `r+1 ≥ 2e²C_u s`. ✓
* Primes as the model: for p prime in (N/2, N] with `N/2 > X`, `p mod 𝓜` is a unit, so every
  fibre is reduced; this is the correct reason no selector is needed. ✓

**Lemma 1.2.** Re-derived.
* `Q_r(H(n)) = Σ_{|B|≤r} (−1)^{|B|} 1[n ∈ ∩_B E_A]` (B over sets of distinct atoms;
  `C(H,j) = #{j-subsets of hit atoms}`). ✓
* B with a repeated ℓ: distinct classes mod ℓ ⇒ empty intersection (shown above). ✓ (This answers
  the author's "point for review" — true, via MN 1.3(iii) for equal (u,v) and the lattice
  inequality for unequal.)
* ℓ's of B = prime factors of q_B above X^{1/2}: k ≤ K < X^{1/2} so all prime factors of k are
  below X^{1/2}. ✓ Given q and ℓ, the atom is fixed by k | q' (k ≤ K) and u, v | kℓ+1: at most
  `Σ_{k|q', k≤K} τ(kℓ+1)²` choices. ✓ (Over-count is harmless: M(q) is only bounded above.)
* Cauchy–Schwarz `g² ≤ τ(q') Σ τ(kℓ+1)⁴`. ✓
* Shiu: summing τ⁴ over *all* n ≡ 1 (mod k) in (kx, 2kx] (primality of ℓ dropped — an upper
  bound). Interval length y = kx, endpoint 2kx: `y ≥ (2kx)^α` ✓; `k < y^{1−β}` ⇔ `k^β < x^{1−β}`,
  true for `k ≤ X^κ`, `x ≥ X^{1/2}`, κ < 1/240 ✓; `τ(p^l)⁴ = (l+1)⁴ ≤ 16^l` ✓; `Σ_{p≤y} 16/p`
  gives `(log)^{16}`, times `1/log` from Shiu: `(log X)^{15}` ✓; the `1/φ(k)` in Shiu times the
  length kx gives `(k/φ(k)) x` ✓. Dyadic sum with weight `1/(ℓ−1) ≍ 1/x`, `≍ t` blocks:
  `≪ t^{16} log t ≤ t^{17}` ✓.
* `φ(q) = φ(q') Π(ℓ_i − 1)` (q' coprime to the ℓ's) ✓; `Σ_{ℓ_1<…<ℓ_j} Π ≤ (Σ_ℓ)^j/j!` ✓;
  `q' ≤ K^r` ✓; Euler product `Π_{p≤x}(1 + Σ_ν (ν+1)^{2r}/φ(p^ν)) ≪_r (log x)^{4^r}` ✓
  (the p-local factor is `1 + 4^r/(p−1) + O_r(p^{−2})`).
* Constants: `C(r)` depends on r, κ and Shiu's implied constant only — not on m. ✓

**Theorem 1.3.** Re-derived.
* `q_B ≤ (KX)^r = e^{(1+κ)rt}`, `rt ≍ s·(sm)^{1/3}`, so `q_B ≤ N^{0.45}` under
  `L ≥ C_1 s^{4/3} m^{1/3}` (C_1 absolute; r ≤ 2e²C_u s + 2 ≤ C s for s ≥ s_0 ≥ 1). ✓
* Main-term identity: B with empty intersection contribute 0 to both sides; for the others
  `P(ñ ∈ ∩E_A) = 1/φ(q_B)` since `a_B` is a unit. So `Σ_B (−1)^{|B|}/φ(q_B) = E Q_r(H(ñ))`
  exactly. ✓
* Every prime p ∈ (N/2, N] satisfies `(p, q_B) = 1` (N/2 > X). ✓
* BT `π(N; q, a) ≤ 2N/(φ(q) log(N/q))` with `q ≤ N^{0.45}` ⇒ `|Δ| ≤ CN/(φ(q)L)` ✓.
  BV for `π*` with main term `π*(N)/φ(q)` instead of `li`: the difference is
  `|π*(N) − (li N − li N/2)|/φ(q)`, summed over q ≤ N^{0.45} gives `≪ L · N e^{−c√L}` ✓ (minor gap in
  the text: not said; see D-U3).
* Cauchy–Schwarz with weights `Δ_q^{1/2}·Δ_q^{1/2}` ✓; exponent bookkeeping with t ≤ L:
  `(C N² t^{17r+4^r} L^{−1−A'})^{1/2} ≤ C' N L^{−3}` for `A' = 17r + 4^r + 5` ✓.
* `N/L² ≤ e^{−a_u s} N/(3L)` iff `L ≥ 3e^{a_u s}` — absorbed into N_0(s) ✓.
* `e^{−(r+1)} ≤ e^{−a_u s}` needs `r ≥ a_u s`: true since `a_u ≤ C_u` ✓.
* N_0(s) depends on s only (C(r), BV constant `C_{A'(r)}`, the condition `L ≥ 3e^{a_u s}`) —
  **not on m**. This is the crux of uniformity and it holds. ✓
* m-range: `m ≤ t³` ⇔ `s ≥ 1` ✓; `t = (sm)^{1/3} ≥ (4s)^{1/3}`, so `X ≥ X_1` for s ≥ s_0 ✓.

**Theorem U.** Follows: `log N ≥ A_ε m^{1/3} ≥ A_ε ≥ log N_0(s)` ✓.
Ineffectivity: BV at level `L^{−A'(r)}` with A' growing in s (Siegel), plus MN's X_h (BV in
Prop 3.1). Correctly stated. ✓

### Defects (Theorem U)

**D-U1 (MINOR, §0 bullet 1, §1 opening, report item 1).** "This removes the `(log m)^{4/3}` of
MN Cor D" is true for the *qualitative* statement `ρ_exc → 0`, but Cor D proves the stronger
`ρ_exc ≤ 1/L` (count `≤ N/L²`). Theorem 1.3 at `ρ_exc ≤ 1/L` would need `s ≍ log L`, i.e.
`log N ≫ m^{1/3}(log L)^{4/3}`, and N_0(s) then becomes uncontrolled (BV at level `L^{−A'}` with
`A' ≥ 4^r`, r ≍ log L — BV is not available with A' growing like `L^{c}`). *Repair:* say
"removes the `(log m)^{4/3}` for the statement `ρ_exc = o(1)` (resp. ρ_exc ≤ ε)", and note that
Cor D's rate `ρ_exc ≤ 1/L` is not improved.

**D-U2 (MINOR, Lemma 1.2 statement).** It says both "for fixed r and `X ≥ X_2(r)`" and "(for
`X ≥ X_1`; C(r) depends on r, κ only)". Pick one. Since Shiu's bound is valid for all
`x ≥ 2` with an implied constant depending only on (A_1, A_2(·), α, β), `X ≥ X_1` suffices; drop X_2(r).

**D-U3 (MINOR, Thm 1.3 proof).** "BV (with π* = difference of two BV sums)" — BV is stated with
`li(y)/φ(q)` (or `π(y)/φ(q)`); the text's Δ uses `π*(N)/φ(q)`. One line is needed: the switch costs
`Σ_{q≤N^{0.45}} |π*(N) − ∫_{N/2}^N dt/log t|/φ(q) ≪ L·N e^{−c√L}` (PNT). Harmless.

**D-U4 (MINOR, Remark (i)).** "MN Cor D covers `A ≥ C (log m)^{4/3}` effectively-in-form" —
MN Cor D is itself ineffective (Theorem A's c, C are ineffective via BV in Prop 3.1). Replace by
"with the explicit rate `ρ_exc ≤ 1/L`".

**D-U5 (MINOR, Lemma 1.1 statement).** The hypothesis is `r ≥ e²·2C_u s`, but the proof needs
`r + 1 ≥ 2e²C_u s` — fine — and Thm 1.3 later needs `r ≥ a_u s`; worth stating `a_u ≤ C_u`
explicitly (it follows from `a_u s ≤ μ_c ≤ C_u s` on a nonempty set of fibres).

No FATAL or MAJOR defect found in Theorem U. Its correctness rests entirely on MN Cor 3.2's
*lower* bound on every reduced fibre (itself PROVED rel. the note and reviewed in R94A/B);
the new argument adds nothing that could fail beyond the standard BV/BT/Shiu inputs.
