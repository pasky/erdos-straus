# Referee report v2: `paper/es-omega-note.tex` (side-agent/omega-hub @ 1cb8c2b)

Referee: side agent (review-omega2). Baseline: POINTWISE_OMEGA.md (PO) and
POINTWISE_OMEGA2.md (O2), as reviewed in `reviews/pointwise-omega-review.md`
and `reviews/pointwise-omega2-review.md` (Rounds 1–2). Sources checked:
ET arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`) and HSS
arXiv:1001.1231.

Defects are numbered P1, P2, … with severity MAJOR / MINOR / COSMETIC.

## 0. Build

`pdflatex` ×3 into a scratch directory: clean exit, **21 pages, no
warnings** (no undefined references or citations, no overfull boxes).

## 1. Statements vs the reviewed sources (faithfulness)

| Paper | Source | Faithful? |
|---|---|---|
| Thm 1.1 (`thm:main`), "Proved modulo Thm TZ; effective" | O2 Thm 5.1 (+ D2 repair) | yes; exponent, error term and `log p ≤ T^{1/3}e^{O(𝓛/log 𝓛)}` match |
| Thm `thm:two` (warm-up, exponent 2) | PO Thm 5.1 | yes (unchanged text, relabelled) |
| Lemmas `closed`, `pointwise`, `meanmass` | O2 Lemmas 1.1–1.3 | yes |
| Lemmas `pseudo`, `hub` | O2 Lemmas 2.1–2.2 (+ D1 repair) | yes; simple edge graph and the root overcount are stated |
| Lemma `lll`, Thm `crit` | O2 Thm 3.1 | yes; δ=e^{−50}, (G) 1/32, (W) δ/32, budgets O(Σ+1) |
| Lemma `qmass`, §`main` proof | O2 Lemma 4.1, Constr. 4.2, Lemma 4.3 | yes; y, 𝓑 threshold 1/64, exponents (2log2−6), (3log2−6), log Q≤5y |
| Hyp. `hyp:min`, Thm `Hmin`, Prop `bonf` | PO §6.2–6.3, O2 §5 | yes, with P3 below |
| Thm `haar-intro` | PO Thm 9.3 | yes |
| Lemma `dict` | O2 Lemma 8.1 (+ D3 repair: "by direct computation") | yes |
| `F_I≤n^{3/5+o(1)}` "modulo the proof of ET Prop 1.7 (its Lemma 2.8 and §3)" | O2 Prop 8.2.1 (+ D4 repair) | yes |
| Thm `eta` | O2 Thm 9.2 | yes |

I found **no strengthening** anywhere. The one place where the paper is
*weaker* than the sources is the joint W/`ck_min` statement (P8).

## 2. Citations

* **Thorner–Zaman:** text unchanged from v1 (Cor. 1.4, Rem. 1.5, McCurley
  as quoted there). Bibliography: Math. Z. 306 (2024), arXiv:2108.10878v2.
* **Haeupler–Saha–Srinivasan:**
  * cited as "cf. [HSS, Thm 2.1]" for the conditional LLL; checked, it is
    exactly arXiv:1001.1231 Thm 2.1;
  * the paper also gives a self-contained proof from the Alon–Spencer
    argument, so it does not depend on HSS;
  * the bibliography entry (J. ACM 58 (2011), no. 6, Art. 28) is correct.
* **Alon–Spencer Lemma 5.1.1** (4th ed.) is the asymmetric LLL. The proof
  of Lemma `lll` uses the intermediate claim
  `P(A|⋂_S Ā')≤x_A` from AS's proof, and says so.
* **Elsholtz–Tao:**
  * numbering is "as in arXiv:1107.1010v6", which is the archived version;
  * Prop 1.4 (`τ(kab²+1)` average), Prop 1.7, Lemma 2.8, §3 and
    identities (2.1)–(2.9) are all cited correctly.
* **Lau–Wu, Chang:** unchanged from v1.

## 3. New sections: do the proofs stand alone?

### §`sec:supp` (support-truncated inclusion–exclusion)
* Lemma `closed`: complete (Möbius, swap, partial alternating row sum,
  `I(V)=1⇔A=∅`). Lemma `pointwise`: complete; I re-checked the
  `L²+3L+4t+2` computation.
* **P1 (MINOR), Lemma `meanmass`.** The proof is too terse to stand alone.
  (a) The statement's second claim, `E|B*_L−1[A=∅]|≤2·4^{−L−1}e^{Λ_{16}}`,
  is never derived. It needs Lemma `pointwise`:
  `E|B*−1|≤E|B_L−1|+4^{L+1}EG≤2·4^{L+1}EG`, then `EG≤16^{−L−1}e^Λ`.
  (b) `M_1` is used in this section but defined only later, in Thm
  `transfer` (`Σ|c_i|/φ(d_i)`). It should be defined here as
  Σ|coefficient|·P(cell).
  (c) The coefficient identity
  `κ(U,c)=Σ_{F⊆A_U(c), supp F=U}(−1)^{|F|}=Σ_{W⊆U}(−1)^{|U∖W|}I_c(W)` is
  only gestured at ("as in Lemma closed").
  (d) The step `P(every ℓ∈U covered)≤E∏_{ℓ∈U}a_ℓ` is not stated.
  (e) Nothing says that non-unit cells get κ=0. Thm `transfer` needs
  `gcd(b_i,d_i)=1`, so this should be said.
  *Fix:* four lines, as in O2 Lemma 1.3.

### §`sec:pseudo`
* Lemma `pseudo`: complete at referee level.
  * Expansion and pseudoforest (the injection is given in one parenthesis,
    which suffices).
  * The singles factor and the component product.
  * The BFS tree count with the root overcount (D1 repaired).
  * The numerical series `<7.6`, which I re-checked: 7.583.
  * Two implicit steps a reader can fill: `(1+z)^{|π(F)|}≤e^{z|V(F)|}`,
    and that a component has ≥2 vertices.
* Lemma `hub`: complete.

### §`sec:crit`
* Lemma `lll`: complete and correct. Status "classical" is not one of the
  declared conventions (P7).
* **P2 (MINOR), Thm `crit` proof.** The logic is right but three steps are
  skipped.
  (a) *Local lemma:* `∏(1−x_E)≥e^{−λ}` needs `1−x≥e^{−1.1x}` for
  `x≤1/8` and `Σx_E=2(S_1^++S_2^+)`.
  (b) *Minorant:* `M_1≤2e^Λ` needs `M_1(B_L)≤E∏(1+2a)≤e^Λ` and
  `4^{L+1}EG≤4^{L+1}16^{−L−1}e^Λ≤e^Λ`.
  (c) *Twist:* the passage "Since (·/ℓ_0) has mean 0, |E[1[A=∅]ψ]| ≤
  P(Ā'∩{event at ℓ_0})" hides the actual argument:
  * factor `ψ=(X_{ℓ_0}/ℓ_0)·ψ'(X_{−ℓ_0})`;
  * condition on `X_{−ℓ_0}` and use independence;
  * replace `1[∉Forb]` by `−1[∈Forb]`, using mean zero;
  * bound by `P_{X_{ℓ_0}}(Forb)`.

  Also, "conductor coprime to Q ⇒ odd ⇒ squarefree" uses `2|Q`. That is
  in the setting, but it is worth one word.
  *Fix:* four or five lines, as in O2 Thm 3.1 Step 4.

### §`sec:main` (proof of Thm 1.1)
* Lemma `qmass`: correct.
  * It defers to Lemma `mass`, whose proof covers a general m and contains
    the `(3+log X)/m` k-sum.
  * The final divisor-bound step (`τ≤τ*(T+2)`,
    `Σ1/(sr')≤(1+𝓛)²`) is left implicit. That is acceptable because
    Lemma `mass` states it.
* Construction, (I), (W), (G), sizes, transfer and inversion: complete,
  and identical to the reviewed O2 §4–5.
  * The graph-type structure (vertices = unit classes mod ℓ, edges =
    distinct classes mod ℓℓ') is implicit in "contributes … the edge
    `−4D mod ℓℓ'`". Acceptable.
* The closing paragraph ("uses `y≥T^{1/3+o(1)}` twice") is accurate.
