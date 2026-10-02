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
