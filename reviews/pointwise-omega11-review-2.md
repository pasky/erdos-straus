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
