# Hostile review of POINTWISE_OMEGA6.md (task O23)

Subject: branch `side-agent/omega-hcpi` at 7003065 (`POINTWISE_OMEGA6.md`,
`reviews/agent-reports/AGENT_REPORT_O23.md`, `scripts/omega6_corner.py`,
`data/omega6/`). Context: O5 §§3,4,7 (Prop 7.1, HC_Π), O5 review, O4 §4.2,
`sources/shiu-1980.pdf` (OCR of pp. 162–163), `sources/henriot-1102.1643.pdf`
(Thm 4, Thm 5, (1.4), §2). Review tools: `scripts/review_omega6_check.py`,
`scripts/review_omega6_ft.py` (this branch).

## Verdict table

| # | Item | Verdict |
|---|---|---|
| 1 | Lemmas 1.1, 1.2, 1.4, Def 1.3, Thm 1.5 (three-fibre reduction) | **CONFIRMED**. Nits D2, D3 |

## Item 1 — §1, the three-fibre reduction. CONFIRMED

* **Lemma 1.1.** (2): mod m, `4sa²≡−1` gives `(4sa)^{−1}≡−a`, so
  `4sab≡1 ⇔ b≡−a`. Mod q, `4sa²≡κ` gives `(4sa)^{−1}≡κ^{−1}a`, so
  `4sab≡1 ⇔ b≡κ^{−1}a ⇔ a≡κb`. Both moduli are coprime (m prime to 2q),
  so CRT gives one class mod qm. (3) is (2) with `κ↔κ^{−1}` (an atom has
  `4κsb²≡1`, i.e. `4sb²≡κ^{−1}`). Checked.
* **Lemma 1.2.** The i-th element (i≥1) has `n′=n′_0+id≥id`. There are
  at most `T` elements, so `Σ≤(2/d)(1+𝓛)`. Checked.
* **Pseudo-atoms.** A fibre's elements include integers whose true Π-part
  is a proper multiple of m. The charging only bounds the weights of true
  atoms, and each true atom is a distinct element (distinct free variable,
  so distinct n′) of the fibres of its *own* m. The bound is an upper
  bound. Checked.
* **Lemma 1.4.** Case `b≤qm`: `n′<4sa`. Otherwise `b−qm≥1` is in the class
  with `n′−4sa<n′≤T/(qm)`, so it is not an element only if `n′−4sa<y`.
  Then `b<qm(1+y/(4sa))+1/(4sa)<2qm+1`. Checked. Numerically (T=10⁹,
  q=337·347, all 10452 corner atoms): 0 violations of `s,a,b≤2qm`, of
  `n′<y+4min(sa,sb,ab)`, and of `n′=ν(s,a,m)` (Thm 3.2's identity).
* **Thm 1.5.** Each atom is charged once: to a period sum (non-first in
  some fibre), to a first-element bound (`d≤y`), or it is a corner atom.
  A fibre's total charge is `≤(2/d)(1+𝓛)+2/d=(2+𝓛)·2/d`; with `d=4ab`
  this is `(1+𝓛/2)/(ab)`. The number of fibres over `(a,b)` is at most
  `τ(a+b)` (O5 Lemma 3.1(1)), over `(s,a)` at most `τ(4sa²+1)`. Checked.
  Remark (iii) (`D_sb=D_sa(κ^{−1})`, `h_1(κ^{−1})=h_2(κ)`) checked; also
  `gcd(κ^{−1}+1,q)=gcd(κ+1,q)`, so `g_0` is the same.

**D2 (minor; definitional).** `D_sa` and `D_sb` (Thm 1.5) and `FT`
(Thm 3.2) sum over **all** s. But Prop 2.1 Regime III uses the
injectivity of `(s,a)↦4sa²`, which needs s squarefree (O5 Lemma 1.1).
For non-squarefree s, the subcase `32SA²<q` does **not** hold "at most
one pair". The fix is free: Theorem 1.5 only charges fibres that contain
an atom, and atoms have squarefree s. So define `D_sa`, `D_sb`, `FT` with
`s` squarefree. Regimes I–II are unaffected (they over-count all s).

**D3 (minor; exponent).** Thm 1.5 Remark (ii) and Cor 2.2's proof quote
O5 Prop 7.1 as `P_1≪2^k𝓛²(q^{−1+o(1)}+H^{−1/4})`. Prop 7.1 gives
`P_1≤4𝓛²[2τ(q)(2+𝓛)/q+…]`, i.e. `2^k𝓛³/q` in the first term (O5's own
summary says `(𝓛/2)P_1≤2^{k+O(1)}𝓛⁴(…)`). Harmless: Cor 2.2's `𝓛⁵`
absorbs it.
