# Hostile review R71 of EXCEPTIONAL_LARGESIEVE6.md (LS6, agent O71)

Reviewer: R71 (branch `side-agent/review-ls6`). Reviewed: LS6 as merged from
`side-agent/soft-pivotal` at 0f417ad. ES is not solved; (A\*) is not proved.
From-scratch scripts: `scripts/review_ls6_*.py`.

## Verdicts per claim (filled in as the review proceeds)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Cor 1.2 | SOUND (see notes) |

## Notes per claim

### Lemma 1.1 (prefactors are free)
Re-derived: LS4 defines `𝓡_{p'}(σ) = Σ_θ|σ̂(θ)|^{p'}`; with `P_S ≥ 0`,
`w_∅ = 1`, `Λ ≥ 1` the chain `1 + Λ^{2β}Σ_{S≠∅}w_SP_S ≤ Λ^{2β}Σ_Sw_SP_S`
is correct, and `Σ_S w_SP_S = E_T𝓡_2(σ_T)` is LS4 Lemma 1.1's identity.
Arithmetic of the remark: `2β·½log N = (log N)^{3/4}` ✓.
Script `scripts/review_ls6_lemma11.py` (exact enumeration on ℤ/210, 40
random laws/weights, Λ taken minimal): inequality holds, max LHS/RHS 0.59.

### Cor 1.2 (tilted law inherits LS4 Thm 4.2, Lemma 5.1, Thm 5.2, Cor 5.3)
Re-derived: LS5 Prop 2.1 with `Q'_c(𝒜_c) ≥ 3/4` gives `Z_c ≥ (3/4)e^{−8m_c/3}`
and `log E_T𝓡_2 ≤ 16m_c/3 + 2log(4/3) ≤ 6m_c + 1` ✓. Adding
`2β(log Λ' + 8m_c/3 + log(4/3))` gives `≤ 7m_c + 2 + 2β log Λ'` once
`16β/3 ≤ 1` ✓; with `m_c ≤ 32J`, `224J ≤ 512J` ✓.
Lemma 5.1 transfer: LS4's proof uses `1_G` only via (i) pinned
representation (valid for any `Φ ≥ 0`), (ii) `‖Φ‖_∞` bound, (iii)
non-pivotality when `v_ℓ, v'_ℓ ∉ R_ℓ`. For `Φ = 1_𝒜e^{−2Y}`, (iii) needs
every `p̃_q` (q ∈ 𝒫, including q = ℓ and q < ℓ) to agree on the two corner
paths: q < ℓ trivially; q ≥ ℓ because no class through ℓ is matched (its
ℓ-residue lies in R_ℓ) and `F̃_q` is a function of `F_q` (truncated
forbidding). ✓. The resulting `Z^{−1}` prefactor is exactly what Lemma 1.1
absorbs. This does not contradict R67 M3's example (that example compares
the tilted coefficient with the *untilted* prefactor `Q'(G)^{−1}`; the
present bound carries `Z^{−1}`).

### Lemma 2.1, Prop 2.2 (soft-pivotal bound)
Re-derived. (2.1): `E_v[χ_θΦ] = E_{v,v'}[χ_θ(v)Σ_A(−1)^{|A|}Φ(v^A)]` since for
A ≠ ∅ the coordinates `v_A` are independent of `v^A` and `E χ_ℓ = 0`; the
coin rule realises `U(·|Ω_q∖F̃_q)` exactly (`P(a) = (1/|Ω|)(1 + p̃/(1−p̃))`) ✓.
Leibniz (a) is the standard discrete product rule; (c): `D_ℓψ ≡ 0` off
pivots, `|D_ℓ(F∘u)| ≤ LΔ(u)`, `D_{T∖ℓ}` costs `2^{|T|−1}` ✓. Constants:
`g = (1−p̃)^{−1}` on `[0,1/2]` has Lipschitz 4 ⇒ `2^{|T|−1}·4Δ = 2^{|T|}·2Δ` ✓;
`φ_q` Lipschitz `2w_q` ⇒ `2^{|T|}w_qΔ_q` ✓; idle factors ≤ 1 except
`g_ℓ ≤ 2` ⇒ `2^{|S|}` ✓. Grouping maps by partitions and dropping
injectivity only increases ✓. `Δ_q ≤ Σ_C q^{−v_q(G_C)}` over varying
top-q classes: `F_q(A)ΔF_q(A')` is covered by residue sets of classes
matched off-top on exactly one side; truncation is 1-Lipschitz ✓.
(The pinned factor table uses `1_𝒜 = Π_{q∉S}λ_qΠ_{ℓ∈S}h_ℓ` on corners —
correct because off S the coin rule guarantees `x_q ∉ F̃_q`.)

### Lemma 3.1 (chains)
Re-derived. (i) same `F̃_r` on all corners ⇒ same `x_r`; the
`F^∪/F^∩` case split is exhaustive ✓. (iii) the recursion keeps the same
corner pair `(A, A∪ℓ)`; the differing off-top coordinate r of `C_j` is
≥ ℓ because the two paths agree below ℓ and on `S∖ℓ`, and `q > ℓ` since
`F_ℓ` depends only on coordinates < ℓ ✓. (iv) ✓ (`λ_q ≡ 1` where
`F_q = F̃_q`). (3.1) follows from Lemma 3.1(iv) and `Piv(F∘u) ⊆ Piv(u)` ✓.
Only wording defect: "(stop, `k = 1`… after relabelling)" (MINOR D-a).

### Lemma 4.1, Prop 4.2 (Walsh/XOR-cover form)
Re-derived. `D_Uf(∅) = (−1)^{|U|}2^{|U|}f̂(U)` ✓; `e^{−a_Rχ_R} =
cosh a_R − χ_R sinh a_R` ✓; `a_∅ = mean Y* ≥ 0` ✓. Minimal-subcover step:
`Σ_{covers} ≤ Π_R(1+|a_R|)Σ_{𝒯₀ min}` ✓; private elements exist in a
minimal cover ✓; `|a_R|^{1/n_R} ≤ β_R` in both cases `|a_R| ≤ 1`
(`n_R ≤ |R|`) and `|a_R| > 1` ✓; injectivity of 𝒯₀ ↦ map ✓. Coefficient
facts ✓ (centre Y* at its midrange).
Prop 4.2: Leibniz with two factors evaluates `e^{−Y*}` on the subcube over
the corner `A_T = U ⊆ T` ✓ (max over `A_T` covers it); shift by
`|S|log 2` (`L_ℓ ≤ log 2` since `p̃_ℓ ≤ 1/2`) costs `2^{|S|}` and leaves
`a_R` (R ≠ ∅) unchanged ✓; `2^{|T|}2^{|S∖T|}2^{|S|} = 4^{|S|}` ✓ (the
0/1 bound `2^{|T|−1}` is even used with slack). Coefficient bound:
`Δ(2w_qp̃_q)/2 = w_qΔ_q`, `Δ(L)/2 ≤ Δ_ℓ` ✓; restriction to subcubes only
decreases Δ and Piv ✓. Example: `1[A⊇B] = 2^{−|B|}Σ_{R⊆B}(−1)^{|R|}χ_R` ✓,
`‖a‖′ ≤ c`, `|D_B| ≤ 2^{|B|}e^{2c}` ✓.
Script `scripts/review_ls6_walsh.py` (seeds 1, 2; 800 random structured Y*
on cubes of dim ≤ 5 with the XOR-family sum computed exactly by group-algebra
DP; 300 random products of 0/1 and Lipschitz factors): Lemma 4.1 both
inequalities, the coefficient facts, Lemma 2.1(b),(c) all hold (Lemma
2.1(b) is attained with equality in some one-factor cases, as it must).

### Thm 5.1 (one rough prime, fixed fibre)
Re-derived line by line.
* `|Ψ(x)−Ψ(x′)| ≤ 2·1[H≠H′] + 2min(1, 2|Y−Y′|)` (`g_ℓ` is a function of the
  common past, `e^{−2Y} ≤ 1`) ✓. Leaks below ℓ are common to both paths,
  so only `q > ℓ` count ✓; `p_q > p̃_q ⟺ p_q > δ_q` because `p_q|Ω_q|` is an
  integer ✓; hard part `≤ 2(2Ep_ℓ + 4Λ_{>ℓ})` ✓.
* Soft part: for `q ≤ τ` only direct classes differ ✓; `min(1,a+b) ≤ a +
  min(1,b)` gives `4EV_dir + 2Σ_rE[1{τ=r}min(1, 2Y_{>r}(x)+2Y_{>r}(x′))]` ✓;
  `E V_dir ≤ 2μ̄(ℓ)` by the chain rule (ℓ-kernel uniform ≤ `(1−δ)^{−1}U`) ✓.
* `E[Y_{>r}(x)|𝓕_{≤r}] ≤ Θ_r(x_{≤r})`: coins at `q > r` are independent of
  `𝓕_{≤r}` (both paths), so x's future follows Q′ kernels from x's own past
  ✓; Θ_r keeps the r-coordinate congruence ✓.
* Truncation: `|F̃(F₁)ΔF̃(F₂)| ≤ 2|F₁ΔF₂|` (go through `F₁∩F₂`; adding k
  elements pushes out ≤ k) ✓. Coin step: the three cases are exhaustive
  ✓. **But the written intermediate does not give 10**: as written,
  `min(U,r^{−e}) + 2U·2r^{−e} + min(2U,2r^{−e}) = 3min(U,r^{−e}) + 4Ur^{−e}`,
  and with `U ≤ 2Σ_Cr^{−v_C}` this is `≤ (6+8)Σ_C r^{−max(v_C,e)} = 14Σ`.
  The second term is in fact `P(c_r∈D_r)·max_b P(repl ≡ b) ≤ U·2r^{−e}`
  (π_r ⊥ c_r), giving `6 + 4 = 10` ✓. Defect MINOR D-b (applied).
* Shared-prime bookkeeping re-derived: with `a = G_C/r^v`, `b = G′_{<r}`,
  `Γ(L)/L ≤ Γ(a)Γ(b)gcd(a,b)/(ab)`; multiplying by `a_{C′}r^{−max(v,e)}`
  leaves `(Γ(G_C)/G_C)·w_qΓ(G_{C′})Π_{p∈P₀∪{r: e>0}}p^{min(v_p(G_C),v_p(G_{C′}))}/G_{C′}`
  because `r^{v+e−max(v,e)} = r^{min(v,e)}` ✓ — this is exactly the
  exponent-capped `ν_{>r}(P;C)` ✓. The case "C by x′, C′ by x" at the
  shared prime ℓ: independent pinned values give `ℓ^{−v−v′} ≤ ℓ^{−max}` ✓.
  Constants `2·10 = 20`, `2·(20+20) = 80`, `2·80 = 160` ✓.
* The hypothesis "w non-increasing" is never used in the proof (harmless;
  MINOR D-c, noted only).
Verdict: SOUND (after the D-b repair of an intermediate expression).
The label "PROVED (fixed fibre)" is right for the inequality; everything
about *uniformity in X* is conditional on (FM2) — see §5 notes below.
