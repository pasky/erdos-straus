# Hostile review R44b (reviewer 2 of 2): POINTWISE_OMEGA11.md — §1 filtration lemma and exponent assembly

Reviewer branch: side-agent/review-omega11b (merged side-agent/quarantine-bound @ 105a522).
Scope: Lemma 1.1, Remarks (i)–(iii), Cor 1.2; exponent chain of Thm 3.2, Cor 3.3, Cor 4.1, H_ω(B) EVIDENCE;
consistency with OMEGA8 Thm 3.4, OMEGA9 Thm 1.1/Lemma 2.1, OMEGA10 Thm 3.4/4.2/Remark 4.3.

STATUS: in progress.

## Summary verdicts
(filled in below as checks complete)

## Detailed checks

### A. Lemma 1.1 — line-by-line re-derivation
Re-derived independently, step by step:

1. *Per-prime level decomposition.* With `W_{ℓ,i}` = functions of digits `≤i` orthogonal to all functions of
   digits `<i` (`W_{ℓ,−1}` = constants), `Σ_{U: max U_ℓ=i}F^{=U}` is exactly the `W_{ℓ,i}`-component
   (digit-ES pieces with top digit `i` are measurable w.r.t. digits `≤i` and orthogonal to every function of
   digits `<i`; the pieces with top `<i` span the latter). ✓
2. *Telescoping.* Coefficient of `P_{W_i}` in `I+Σ_{j≥0}μ'_jP_{≥j}` is `1+Σ_{j≤i}(Λ_j−Λ_{j−1}) = Λ_i`. Needs
   `μ'≥0`, i.e. Λ nondecreasing: true for `λ≥1`. ✓
3. *Tensoring.* The per-ℓ operators act on disjoint coordinates and commute; `L_V` is a product of commuting
   orthogonal projections, hence an orthogonal projection, so `⟨F,L_VF⟩=‖L_VF‖²`. ✓
4. *Block reduction.* `P_{≥j}=I−E[·|δ_{<j}]=I−E_{B_{ℓ,j}}` (integrate out the tail block). Regard the space as
   the product of the blocks `B_{ℓ,j_ℓ}` (ℓ∈V) and one lumped "rest" coordinate. Then
   `‖L_VF‖² = E_{rest}‖(F_{rest})^{=V}‖²`, which is precisely the quantity bounded in O10 Lemma 3.1's proof. That
   proof needs single values **only on the V-coordinates** (off V the event condition is merely evaluated at
   `x_{V^c}`). Splitting each event into the disjoint completions of its block values leaves `F` unchanged
   (`∏_pieces(1−1_p)=1−Σ1_p=1−1_E`), and exactly one piece per event holds at each x. ✓
5. *Hypergraph identification.* `N_𝓗(V)` depends only on the traces of the edges on V
   (`N(V)=Σ_{R⊆V}(−1)^{|R|}τ(R)` with τ on traces). Trace of the piece-support on the blocks of V is
   `{(ℓ,j_ℓ): v_ℓ(E)>j_ℓ} = Ê∩V`. Multisets of edges are harmless (O10 Lemma 3.3 is stated for multisets; a
   doubled edge contributes `Σ_{k≥1}C(m,k)(−1)^k=−1` like a single one). ✓
6. *Non-selections.* Adding `μ'^V N(V)²≥0` for non-selection V gives `G'≤E_xQ_{μ'}(Ĥ(x))`. ✓
7. *Edge weight.* `1+μ'_{ℓ,0}=λ`, `1+μ'_{ℓ,j}=1+λ^j(λ−1)≤λ²` ⟺ `λ^j≤λ+1`; the hypothesis forces each factor
   `λ_ℓ^{2v_ℓ}≤2`, so `λ^j≤λ^{v−1}<√2<2≤λ+1`. Edge weight `≤λ^{2v−1}` per prime `≤∏λ^{2v}≤2`. ✓
8. *ES specialisation.* `∏λ_ℓ^{2v_ℓ}=2^{log r_E/𝓛}` with `r_E=∏ℓ^{v_ℓ(M)}≤M≤T`; and
   `∏_ℓΛ_{ℓ,maxU_ℓ}=2^{log m_U/(2𝓛)}`; Markov on the weights gives the tail `2^{−τ/(2𝓛)}`. ✓
9. *Digit structure of fibres.* On `1+ℓ^aℤ` (a≥1), `X=1+ℓ^a y` has digit 0 = 1, digits `1..a−1` = 0, and digits
   `≥a` equal those of y (no carry), so they are i.i.d. uniform on `[ℓ]`; for a=0 (units) digit 0 is uniform on
   `ℓ−1` values, the rest uniform and independent. Fixing `X mod ℓ^v` = fixing digits `0..v−1`. ✓
10. *Remark (i).* `λ·∏_{j=1}^{v−1}(1+λ^j(λ−1)) ≤ exp(λ^v−1)`; `Σ_ℓ(2^{x_ℓ/ρ}−1)` over `Σx_ℓ≤1` is maximised at a
    vertex (convexity), giving `2^{1/ρ}−1≤ln2` ⟺ `ρ≥1/log₂(1+ln2)=1.316`. ✓ (unused)
11. *Remark (ii).* With absolute weights and first remaining level `i_0`, `1+μ'_{i_0}=Λ_{i_0}=λ^{i_0+1}`, edge factor
    `≤λ^{i_0+1}λ^{2(v−i_0−1)}=λ^{2v−i_0−1}≤λ^{2v}`. Events inconsistent with `E_j` disappear (factor 1 in F);
    consistent ones fix digits `i_0..v−1`, an initial segment of the remaining digits. The conditional measure
    on the cylinder is the product of uniform measures on the remaining digits. ✓
12. *Remark (iii).* O8 Lemma 3.1 (BRW) is stated for arbitrary events `A_i` and arbitrary real `u_j`, and
    `E[A_je_j²]=P(E_j)·E[(F^{(j)}−u_j)²|E_j]`; nothing requires single values. ✓

**Verdict on Lemma 1.1 + Remarks: SOUND** (pending the numerical check in §B).

### B. From-scratch numerics for Lemma 1.1 (`scripts/review_o11b_filtration.py`)

Independent code (not the author's): exact digit-level Efron–Stein energies by Möbius inversion of
`‖E[F|X_W]‖²`; 1–3 "primes", up to 3 digits, digit 0 on units (`ℓ−1` values) or full; random **first free
digit `i_0`** (models both fibres `a_ℓ>0` and Remark (ii)'s conditioned systems, with absolute weights
`Λ_{ℓ,i}=λ^{i+1}`, `Λ_{ℓ,i_0−1}:=1`); 1–8 events fixing initial segments of the remaining digits; random
per-prime log-sizes rescaled so the hypothesis is **tight** (`max_E∏λ^{ρv}=2`). Besides `G'≤1` it checks the two
intermediate steps of the proof: (b) the identity `G'=Σ_{selections}μ'^V‖L_VF‖²`, and (c) the per-selection bound
`‖L_VF‖²≤E_xN_{Ĥ(x)}(V)²` with `Ĥ` built from `Ê={(ℓ,j): j<v_ℓ(E)}`.

| run | ρ | systems | max G' | max\|G'−Σ_sel\| | max(‖L_VF‖²−E N²) |
|---|---|---|---|---|---|
| random, seed 2 | 2 | 1500 | 0.99933 | 9e−16 | 7e−16 |
| random, seed 3 | 1 | 600 | 0.99961 | 1e−15 | 6e−16 |
| random, seed 5 | 1.32 | 600 | 0.99871 | 1e−15 | 9e−16 |
| hill-climb (150 steps each), seed 11 | 2 | 60 | 0.99869 | — | — |
| hill-climb, seed 12 | 1 | 60 | 0.99981 | — | — |
| **power check**, seed 4 | 0.5 | 600 | **1.537** | 8e−16 | 6e−16 |

So (b) and (c) hold to rounding, `G'≤1` at ρ=2 (and, unclaimed, at ρ=1), and the test has power: at ρ=0.5 it
detects `G'>1`. This agrees with the author's `data/omega11/filtration.txt` (max 0.9972 at ρ=2, 0.9971 at ρ=1).
**EVIDENCE consistent with Lemma 1.1; no counterexample.**

### C. Corollary 1.2 (junta modulus `≪𝓛(S+𝓛)`)

Checked against O8 Lemma 3.1 (BRW, arbitrary events/`u_j`), O8 Thm 3.4 (EL constant `e^{−3S}/(100m²(S+1))`,
`E[F−B]≤m²Σ_jP(E_j)·tail_j≤δ/100` with `δ≥e^{−2.2S}`) and O9 Thm 2.2 (`log Z≤log Q+log ℓ_aux+log max d_i`).

* `2^{−τ/(2𝓛)}≤1/(100m²(S+1)e^{3S})` by the choice of τ, and Remark (ii) gives `G'_{F^{(j)}}≤1` for every j, so
  the modulus-truncation error obeys the EL bound. ✓ (Strictly, "EL" in O8 is phrased with `|U|>t`; what BRW
  needs is only `E[(F^{(j)}−u_j)²|E_j]≤…`, which is what is proved. Wording only — m1.)
* A function of digit set U (absolute positions) depends on `X_ℓ mod ℓ^{maxU_ℓ+1}`, so `u_j` is a combination of
  cells of modulus `m_U≤e^τ`; these cells lie in the fibre, hence are consistent with the class of one. ✓
* Terms of B are `A_iA_ju_j`, `A_iA_jA_{j'}u_ju_{j'}` (and lower), modulus `≤T³e^{2τ}`. ✓
* `m≤#atoms≤Σ_{M≤T}τ(A_M²)≤T^{1+o(1)}≤T²` for large T, so `log₂(m²)≪𝓛` and `τ≍𝓛(S+𝓛)`; with S the atom
  mass `S_tot(Q)≤S♯≪𝓛^4log𝓛` (ET), `log Z≤log Q+O(𝓛(S+𝓛))≪log Q+𝓛^5log𝓛`. ✓ Duplicated atoms (same event)
  are harmless: BRW and the local lemma allow multisets; using atom mass in both `τ` and `δ≥e^{−2.2S}` is
  consistent.
* With O2's full quarantine (`i_0=0`, units) the same argument applies verbatim, giving in O9 Thm 2.2
  `log Z ≪ 𝓛^7/log𝓛 + 𝓛^5log𝓛`, consistent with O10 Thm 4.2 (`≪𝓛^6` junta there). ✓

**Verdict on Cor 1.2: SOUND.**

### D. Exponent chain: Thm 3.2, Cor 3.3, Cor 4.1

**Thm 3.2.** Re-derived:
* Lemma 2.2 with `c=1/64`: `log Q ≤ 9+64(1+o(1))𝓛²S♯/log𝓛`; `S♯≪𝓛^4log𝓛` under ET (O2 Lemma 11.1 already
  contains the `C log log T` factor, so no hidden extra `log𝓛`). Hence `log Q≪𝓛^6`. ✓
* Haar side: `x_E=2P(E)`, neighbourhood sum `≤2Σ_{ℓ∈supp E}w_ℓ≤2c=1/32`; `−ln(1−2p)≤2.07p` for `2p≤1/32` gives
  `δ≥e^{−2.2S}`. ✓
* Twist (O8 Lemma 3.3): needs `1.07·w_{ℓ_0}≤0.02`; `w_{ℓ_0}≤θ_{ℓ_0}=c·logℓ_0/𝓛≤1/64` gives `0.0167`. ✓ (`a_{ℓ_0}=0`
  since `ℓ_0∤Q`; `ψ` depends on digit 0 only.)
* Transfer: O9 Thm 1.1 needs `A≤Z^{1/4}` (`A≤1.03` by O9 Lemma 2.1 with η=1/99) and gives
  `log p≪(1+log A)log Z≪log Z`. ✓
* Junta: Cor 1.2 gives `𝓛^5log𝓛`; the "coarser" O10 Thm 4.2 route (`k≤ω(M)≤(1+o(1))𝓛/log𝓛`,
  `t≍k(S+k𝓛)`, cells on `≤3k+2t` coordinates of modulus `≤T`) gives `k𝓛(S+k𝓛)≍𝓛^6`, also enough. So
  **Thm 3.2 does not need Lemma 1.1 at all**; only Cor 4.1 does. (Observation, not a defect; the label's
  dependency "OMEGA10 Thm 3.4" is correct either way.)
* `log p≪𝓛^6`, `p>T` (auxiliary prime), `W(p)>T=e^𝓛≥exp(c(log p)^{1/6})`; T→∞ gives infinitely many p. ✓

Bottleneck: `log Q≍64𝓛²S♯/log𝓛` vs junta `≍𝓛S♯`: ratio `≍𝓛/log𝓛`, **not** `𝓛/log²𝓛` as written (defect m2).
The same slip occurs at line 357 ("asymptotic gain ≈𝓛/log²𝓛" over O2): O2's
`64k²S*𝓛=16𝓛³S*/log²𝓛` (z=𝓛², `log z=2log𝓛`) against `64𝓛²S♯/log𝓛` is a gain `≍𝓛/(4log𝓛)`; likewise for the
`c=1/8` Haar comparison (`8k²S*𝓛` vs `8𝓛²S♯/log𝓛`). Harmless for every stated exponent.

**Cor 3.3.** `c=1/8`, neighbourhood sums `≤1/4`, `x∏(1−x')≥2P(1−1/4)≥P`; `1−x≥e^{−2x}` for `x≤1/2` gives
`δ≥e^{−4S♯}`; `log(1/δ*)≤log φ(Q)+4S♯≪𝓛²S♯/log𝓛≪𝓛^6`. Depends only on Lemmas 2.1–2.2 + ET. Comparison
with O2 Thm 11.3 (`𝓛³S*/log²𝓛≍𝓛^7/log𝓛`) ✓. **SOUND.**

**Cor 4.1.** `log Q≤9+(𝓛/c)Ω♯` is exactly what Lemma 2.2's charging gives
(`Σ_{a<v}1/(a+1)=H_v`); under H_ω(B) `log Q≪𝓛^5(log𝓛)^B`; junta `𝓛^5log𝓛` (needs Cor 1.2, i.e. Lemma 1.1);
`log p≪𝓛^5(log𝓛)^{max(B,1)}` inverts to `𝓛≫(log p)^{1/5}(log log p)^{−max(B,1)/5}`. ✓ Label "PROVED
implication" under H_ω, ET, (G), O10 Thm 3.4 is accurate. **SOUND.**

**Thm 3.2 verdict: SOUND** (modulo (G), ET Prop 1.4, O10 Thm 3.4, and the other §2–3 lemmas, which are reviewer
1's scope).

### E. H_ω(B) and its EVIDENCE (`scripts/review_o11b_hmoment.py`, `data/review_o11b/hmoment.txt`)

From-scratch recomputation over all atoms (`M≤T`, `M≡3 (4)`, `D|A²`, weight `g/M`, `g=gcd(M,4D+1)`), extended
one decade beyond the author:

| T | Σ g/M | mean h (g/M) | mean h (exact s) | log log T | 𝓛/log𝓛 |
|---|---|---|---|---|---|
| 10⁴ | 55.28 | 2.1840 | 2.3240 | 2.2203 | 4.148 |
| 10⁵ | 113.27 | 2.4178 | 2.5718 | 2.4435 | 4.712 |
| 10⁶ | 206.68 | 2.6282 | 2.7935 | 2.6258 | 5.262 |
| 10⁷ | 347.65 | 2.8195 | 2.9936 | 2.7799 | 5.798 |

The author's numbers (2.18/2.42/2.63; 2.32/2.57/2.79) are reproduced exactly. At 10⁷ the step is 0.19 vs
`Δlog log T=0.15` vs `Δ(𝓛/log𝓛)=0.54`: still tracking `log log T+O(1)`. Caveats (Assessment): the range is far
from the asymptotic regime (`Σg/M` grows like `≈𝓛^{3.3}` here, not yet `𝓛^4log𝓛`), and `log𝓛` vs
`(log𝓛)^{1+ε}` cannot be separated numerically. The label "OPEN; EVIDENCE (B=2)" is appropriate, and Cor 4.1 is
correctly stated as an implication. The reduction in "What H_ω needs" (`ω(M)≤ω_{≤y}(M)+𝓛/log y`,
`y=T^{1/log𝓛}`; the identity `M=4sr'mu−n=m(4sr'u−n/m)` from `D=sr'²`, `A=sr'k`, `k=mu−r'`) checks out; it is
correctly labelled Assessment. `h(M)≤ω(M)+Σ_{ℓ²|M}log₂(v_ℓ+1)` is valid (`H_v≤log₂(v+1)`, `H_1=1`).

**Verdict on H_ω labels: SOUND.**
