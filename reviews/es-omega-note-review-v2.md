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

### §`sec:limits`, §`sec:haar` (changed parts)
* **P3 (MINOR), status of `H_min(θ)` for θ≥1/3.**
  * The Hypothesis header reads "true for θ≥1/3, open for θ<1/3" with no
    status label or reference.
  * The Summary lists "`H_min(θ)` for θ≥1/3" under *Proved modulo
    Thorner–Zaman*. But `H_min` is pure congruence combinatorics, and its
    proof (Thm `crit` plus the construction in §`main`) uses no analytic
    input. This is an understatement, not an overclaim, but the labels
    are inconsistent.
  * The construction proving it is buried inside the proof of Thm 1.1.
  * *Fix:* state "Proposition (Proved): `H_min(1/3)` holds, with
    `T^{o(1)}=exp(O(log T/log log T))`", proved by the first half of
    §`main`. Cite it in the Hypothesis header and move it to *Proved* in
    the Summary.
* **P4 (MINOR), Thm `eta` depends on a Remark.**
  * The proof of Thm `eta` ("Proved implication") ends with "the argument
    there [Remark `rem:pp`] … gives `log(1/δ*)≤π(z)log T+T^{o(1)}`".
  * Remark `rem:pp` is headed "Conditional; the implication is proved
    modulo [ET, Prop 1.4]". The ET dependence concerns only the
    polylogarithmic size of `S_tot`, not the LLL step Thm `eta` uses.
  * A reader could therefore think Thm `eta` is modulo ET.
  * *Fix:* split the LLL step (PO Thm 9.4, first bullet:
    `δ*≥(8/φ(Q_z))exp(−4S_tot)` under the per-prime condition) into a
    lemma labelled *Proved*, and cite it from both places.
* **P5 (MINOR), unlabelled, unproved aside.** "A direct elementary
  argument gives ≪√ℓ log ℓ points with a=1 at a prime ℓ" (after Lemma
  `dict`) carries no status and no proof. The paper's own convention is
  that every statement is labelled. *Fix:* either add the six-line proof
  (O2 Prop 8.2.2: `ℓ∤c`, `gcd(c,f)=1`, `(c−a)(f−1)≤a(ℓ+1)`, two divisor
  sums), or mark it "(not used; proof omitted)".
* **P6 (MINOR), "Type I solutions" vs "points".**
  * The abstract says the paper will "identify the single-prime atoms with
    Elsholtz–Tao Type I solutions". After Lemma `dict` the text says
    "governed by Type I representations of 4/r".
  * Lemma `dict` is a bijection with **points** of `ℕ⁶∩Σ_I^r` with `a≤b`
    and d squarefree.
  * ET's *Type I solutions* are triples `(x,y,z)` with c coprime to n.
    They correspond to points only up to the dilation (2.10), under
    ET's normalisation (`abcd` coprime to n, `gcd(a,b,c)=1`), not under
    "d squarefree".
  * For prime r the atoms do inject into Type I solutions:
    * `ℓ∤c` holds (O2 Prop 8.2 proof);
    * d squarefree pins the dilation to λ=1.
  * Surjectivity is not claimed or proved.
  * *Fix:* "identify the single-prime atoms with points of Elsholtz–Tao's
    Type I variety" (abstract), and "governed by the Type I variety
    `Σ_I^r`" (text).
* Thm `eta`: faithful to O2 Thm 9.2.
  * The split at `R=T^{1/(1+η)}` is right.
  * The case ℓ>R is trivial and is not mentioned. Acceptable.
* The closing Assessment (κ=3/8 from η=3/5, η=1/2 ↦ 1/3, progression
  average) is correctly labelled Assessment.

### Conventions and cosmetics
* **P7 (COSMETIC).** The headers "classical" (Lemma `lll`) and "Proved
  implication" (Thm `eta`) are not among the declared conventions
  (Proved / Proved modulo X / Cited). Thm `slice-intro` has no header
  label: its status sits inside the items. Either add "classical" and
  "proved implication" to the conventions paragraph, or relabel.
* **P8 (COSMETIC, optional strengthening the paper is entitled to).**
  * The joint statement "`W≥(log p)^{2−o(1)}` and
    `ck_min≥(log p)^{1−o(1)}` jointly" is still derived from Thm `two`.
  * The primes of Thm 1.1 are also `≡1 (mod ℓ)` for every `ℓ≤y`, with
    `y=T^{1/3+o(1)}` and `log p≤T^{1/3+o(1)}`.
  * So `n_p>y≥(log p)^{1−o(1)}`, and the joint statement holds with
    exponent 3 for W.
  * Not a defect; mention or leave.

## 4. Summary and verdict

| # | Severity | Location | Issue |
|---|---|---|---|
| P1 | MINOR | Lemma `meanmass` proof | second claim not derived; `M_1` undefined in §; κ identity, coverage bound, unit-cells remark implicit |
| P2 | MINOR | Thm `crit` proof | LLL numeric step, `M_1≤2e^Λ`, and the twist factorisation argument skipped |
| P3 | MINOR | Hyp. `hyp:min` header; Summary | `H_min(1/3)` unlabelled; listed as modulo TZ though purely combinatorial |
| P4 | MINOR | Thm `eta` proof ↔ Remark `rem:pp` | proved theorem leans on a remark labelled modulo ET |
| P5 | MINOR | after Lemma `dict` | `√ℓ log ℓ` claim unlabelled and unproved |
| P6 | MINOR | abstract; after Lemma `dict` | "Type I solutions/representations" should be "points of the Type I variety" |
| P7 | COSMETIC | headers | labels outside the declared conventions |
| P8 | COSMETIC | §`typeI` end | joint W/`ck_min` statement could use Thm 1.1 |

No MAJOR defects, and no statement stronger than the reviewed sources. The
mathematics of the new sections is complete and correct. The minor issues
are proofs written more tersely than "stand alone" requires (P1, P2) and
status-label hygiene (P3–P7).

**Verdict: MINOR REVISION.**

---

# Round 4 (side-agent/omega-hub @ 6beaa92)

Imported `paper/es-omega-note.tex` and `POINTWISE_OMEGA2.md` from 6beaa92.
Build: `pdflatex` ×3, clean, **23 pages, 0 warnings** (no undefined
references or citations, no overfull boxes).

| # | Status | Evidence |
|---|---|---|
| P1 | **FIXED** | `M_1(Φ)` is defined before Lemma `meanmass`. The statement now gives `E|B*−1|≤2·4^{L+1}z^{−L−1}e^{Λ_z}`, derived via Lemma `pointwise`. The proof now spells out the κ identity, the pairwise cancellation, the coverage bound `1_c≤∏_{ℓ∈U}a_ℓ`, unit cells only, and the G-expansion. |
| P2 | **FIXED** | Thm `crit` proof: `x_E≤1/8`, `1−x≥e^{−1.1x}`, `Σx_E=2(S_1^++S_2^+)`; `M_1≤M_1(B_L)+4^{L+1}M_1(G)≤2e^Λ`; `log(M_1/μ)≤Λ+λ+1`. The twist step now factors `ψ=χ_0ψ'`, conditions on `X_{−ℓ_0}`, swaps `∉Forb` for `∈Forb`, and states the sub-family LLL with `(7/8)(15/16)>0.82`. |
| P3 | **FIXED** | New Prop `prop:hmin` (Proved) is the construction half of the old proof. The Hypothesis header cites it. The Summary moves `H_min(θ≥1/3)` to *Proved* and keeps only Thm `main`, Thm `Hmin` and Cor `joint` under TZ. |
| P4 | **FIXED** | New Lemma `ppl` (Proved) isolates the LLL step. Thm `eta` and Remark `rem:pp` cite it. The ET dependence now sits only in the Remark (polylogarithmic `S_tot`). |
| P5 | **FIXED** | New Prop `prop:a1` (Proved) with a full proof, marked "not used below". |
| P6 | **FIXED** | The abstract says "points of Elsholtz–Tao's Type I variety". The subsection title and text say "Type I variety `Σ_I^r`". |
| P7 | **FIXED** | The conventions now define "Proved modulo the proof of X", "Classical", "Proved implication" and "Assessment". Lemma `lll` is "classical, proof included", and Thm `slice-intro` now has a header label. |
| P8 | **FIXED** | New Cor `cor:joint`, which replaces the exponent-2 joint remark. |

### New items

* **Prop `prop:hmin` (paper): SOUND.**
  * It is exactly the construction, (I), (W), (G) and the sizes from the
    reviewed O2 §4, followed by Thm `crit`.
  * The conclusion (840|Q, `log Q≤5y`, `log max d_i` and `log(M_1/μ)` at
    most `e^{O(𝓛/log 𝓛)}=T^{o(1)}`, μ>0, twist) matches every clause of
    Hypothesis `hyp:min` for θ≥1/3. That includes θ=1/3, since
    `5y=T^{1/3+o(1)}≤T^{1/3+ε}`.
  * The proof of Thm `main` now starts from it and is otherwise unchanged.
* **Lemma `ppl` (paper): SOUND.**
  * It is PO Thm 9.4's first bullet. Re-checked:
    * `x_E=2/φ(r_E)≤1/2`, since `r_E` has a prime `>z≥3`, so `φ≥4`;
    * the LLL condition `1/φ≤x_E·e^{−1/2}·…` holds;
    * `Σ_{E'∼E}x_{E'}≤2Σ_{ℓ|r_E}w_ℓ`;
    * `1−x≥e^{−2x}` on `[0,1/2]`;
    * `ω(r_E)≤log T/log z` gives `Σ_{ℓ|r_E}w_ℓ≤1/8`;
    * `∏(1−x_E)≥exp(−4S_tot)` (distinct events ≤ atoms);
    * the relative measure of the class of one is `φ(24)/φ(Q_z)=8/φ(Q_z)`.
  * No ET input is used.
* **Prop `prop:a1` (paper): SOUND.**
  * Same argument as O2 Prop 8.2.2 (reviewed Round 2), specialised to a=1.
  * Re-checked: `ℓ∤c`, `gcd(c,f)|ℓ`, `cf|a(ℓ+f)+c`, `(c−1)(f−1)≤ℓ+1`.
  * Both branches are `Σ_{j≤2+√ℓ}τ(ℓ+j)`. The final sum carries an
    `O(√ℓ)` for the `+1` terms.
  * **COSMETIC:** the proof writes `y=acd, z=bcd` for the denominators,
    which clashes with the paper's parameter `y`. Use `(X,Y,Z)` or "the
    denominators".
* **O2 Cor 5.2 and paper Cor `cor:joint`: SOUND** (Proved modulo TZ).
  * The primes of Thm `main` are `≡1` mod Q with `24|Q` and every `ℓ≤y`
    dividing Q. So `p≡1 (24)` and `(p/ℓ)=1`, hence `(ℓ/p)=1`
    (reciprocity, `p≡1 (4)`).
  * Lemma `lem:np` (stated for `5≤ℓ≤B`) gives `ck_min(p)>y`.
  * With `log p≤T^{1/3}e^{O(𝓛/log 𝓛)}` and `y=T^{1/3}e^{2𝓛/log 𝓛}`,
    `y≥(log p)^{1−o(1)}`. The W-part is Thm 1.1.
  * The O2 text cites "PO Lemma 8.1" for the same statement; consistent.

**Round 4 verdict:** P1–P8 are all FIXED, and the new items are sound.
One cosmetic notation clash remains (Prop `a1`). **Recommendation: ACCEPT**
(the notation fix can go in at proof stage).
