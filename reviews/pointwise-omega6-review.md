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
| 2 | Prop 2.1 (`D_sa≪4^k𝓛⁴(H^{−1/2}+q^{−1/4})`), all three regimes; Cor 2.2 | **CONFIRMED** modulo Shiu Thm 1 and Henriot Thm 4, whose hypotheses I checked literally. Citation nit D1 |

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

## Item 2 — §2, Prop 2.1 and Cor 2.2. CONFIRMED (modulo Shiu, Henriot)

**The citations, read literally.**

* *Shiu* (Crelle 313, p. 163, Thm 1; OCR of the archived scan). The class
  M is: non-negative multiplicative, `f(p^l)≤A_1^l`, and for every ε>0,
  `f(n)≤A_2(ε)n^ε`. The hypotheses are `0<α<1/2`, `0<β<1/2`, `(a,k)=1`,
  `k<y^{1−β}`, `x^α<y≤x`, and the bound holds "as x→∞", uniformly in
  a, k, y. τ is in M with `A_1=2`. O6's paraphrase is correct, except
  for D1.
* *Henriot* (arXiv 1102.1643, Thm 4). Here f is in the class M of the
  Introduction (multiplicative, `f(p^ℓ)≤A^ℓ`, `f(n)≤B(ε)n^ε` for all ε).
  Q must be irreducible. Thm 4 is derived from Cor 2 "under the
  assumptions of Theorem 5", and Thm 5 assumes Q **primitive**
  (§2: "We assume that Q is primitive"). The range is `x≥c_0‖Q‖^δ`,
  `x^α<y≤x`, with `0<α,δ<1`. `Δ_D` is (1.4), a product over `p|D`. The
  constants depend on `α,δ,A,B` (and g). **No** "no fixed prime divisor"
  hypothesis is needed for the upper bound (that hypothesis is in Thm 1
  and Thm 6, not Thm 5). O6 quotes all of this correctly, including
  primitivity, which it secures by dividing by `g_0`.

**D1 (minor; citation range).** O6 says "We use … α=1/2, β=1/4" for both
theorems. Shiu requires `0<α<1/2` strictly, so α=1/2 is outside Shiu's
range (it is fine for Henriot, where `0<α<1`). The fix is free: in
Regime I, `y_1=4a²S/g_0=x_1/2`, so any α, e.g. α=1/4, works.

**Regime I (Shiu in s). Checked.**
* Fixed a: s is in one class mod q, so `n=4a²s+1` is in one class mod
  `4a²q`, inside `(4a²S,8a²S]`, and `g_0|n`. Then `n_1=n/g_0` is in one
  class mod `k_1=4a²q/g_0`. Its interval has length `y_1=4a²S/g_0` and
  right end `x_1≈2y_1`.
* `gcd(r_1,k_1)=1`. For `p|2a`, `n≡1 (p)` and `p∤g_0`. For `p|q` with
  `v_p(g_0)=f<e=v_p(q)`: `n≡κ+1 (p^e)`, so `v_p(n)=f` and `p∤n_1`. For
  `f=e`, `p∤k_1`, because `gcd(a,q)=1`. This also covers `q′`. Checked.
* `k_1<y_1^{3/4} ⇔ 4a²q⁴<g_0S³`, which is implied by
  `S≥(16A²)^{1/3}q^{4/3}`, and `16^{1/3}<3`. Checked.
* `Σ_sτ(n)≤τ(g_0)Σ τ(n_1)≪2^k(S/q)𝓛²`. Summing over the A values of a
  and dividing by SA gives `2^k𝓛²/q`. Checked.

**Regime II (Henriot in a). Checked**, including the points the report
asked about.
* *Content.* `P=4sq²X²+8sqrX+(4sr²+1)`. A common prime factor p does not
  divide `2sr`, so `p|q`. Its p-part is
  `min(v_p(q²),v_p(q),v_p(4sr²+1))=min(v_p(q),v_p(κ+1))=v_p(g_0)`. So the
  content is exactly `g_0`, and `P_1=P/g_0` is primitive. P has no real
  root, so P is irreducible over ℚ.
* *`Δ_D=1`.* `disc P_1=−16sq²/g_0²`. Its prime factors divide `2s` or
  `q/g_0`. For `p|2s`, `P_1≡g_0^{−1}≢0 (p)`. For `p|q/g_0`, the X- and
  X²-coefficients of `P_1` are divisible by p, and the constant
  `(4sr²+1)/g_0` is a p-unit (valuation argument). So `ρ(p^ν)=0` for all
  `p|D` and ν≥1, and each factor of (1.4) is 1. (For p with
  `v_p(g_0)=v_p(q)`, `P_1` is linear mod p, with `ρ(p)=1`; but then
  `p∤D`, so this is harmless.) Checked, including `q′`.
* *Main term.* `Π_{2<p≤x}(1−ρ/p)·exp(Σ2ρ/p)≤exp(Σρ/p+O(1))≪(log x)²`,
  since `ρ(p)≤2`. Checked.
* *Range.* `‖P_1‖≤‖P‖≤16sq²+1≤40Sq²`, and `x≥A/q−1≥C_1q^{1/2}S^{1/4}−1`.
  So `x≥c_0‖P_1‖^{1/4}` for `C_1≥3c_0`, say. The i-range has length `A/q`
  and starts near `A/q`. Halving it gives two intervals with
  `x′^{1/2}<y′≤x′`, as `A/q≥C_1q^{1/2}` is large. Checked. The "O(1)
  single points" are unnecessary. If kept, their bound is
  `2^kmaxτ(F)/A≤2^kA^{−1+o(1)}≤2^kq^{−3/2+o(1)}`, because `F≤A^{O(1)}` in
  Regime II. That is not "like Regime III", but it is fine (nit).
* Count: `≤2^k` classes r, times `τ(g_0)≤2^k`, gives `D(S,A)≪4^k𝓛²/q`.
  Checked.

**Regime III. Checked.** Not-I and not-II give `A≪q^{11/5}` and
`S≪q^{14/5}`, so `F≪q^{36/5}`. Nicolas–Robin gives `τ(F)≤q^{1/8}` for q
beyond an absolute constant. For bounded q, F is bounded, and the
constant absorbs it. The three counts are correct. The subcase
`32SA²<q` needs s squarefree (D2). Its bound `τ(F)≤(SA)^{1/2}` follows
from `τ(n)≪n^{1/4}` and `F≤32(SA)²`, with an absolute constant, so "for
SA beyond an absolute constant" is not even needed. Also `SA>h_1/4>H/4`.
The final sum over `≤4𝓛²` boxes is checked.

*Nit.* Prop 2.1's statement should list its hypotheses: `h_1(q,κ)>H`
(or replace H by `h_1`), and s squarefree (D2). It does not need `q>y²`,
as just noted.

**Cor 2.2. Checked.** `q^{−1/4}<H^{−1/2}` because `q>y²≥H²`. `D_sb`
uses `h_2>H`. `D_ab` uses Prop 7.1 (with D3's `𝓛³`). The total is
`≪4^k𝓛⁵H^{−1/4}`.

*Assessment.* Prop 2.1 is the main genuine gain of O6. It closes O5 §4
item 2's "period terms" without a separate `τ_Π` average in short boxes.
In the short regime, the `1/q` density of the plane pays for the
pointwise divisor bound. Short boxes are a problem only for first terms.

## Item 3 — Lemma 3.1, Thm 3.2, (FT_a). CONFIRMED (as sufficiency)

* **Lemma 3.1.** A corner atom with `4sa≤yZ` is the unique first element
  of its `(s,a,m)`-fibre, and `2/n′≤2/y≤Z/(2sa)`. Summing over `(s,a)` and
  `m|F` gives `(Z/2)D_sa`. Checked.
* **Thm 3.2.** `(1+𝓛/2+Z/2)(D_ab+D_sa+D_sb)≪Z·4^k𝓛⁴H^{−1/4}+…=4^k𝓛⁵H^{−a}`.
  For a remaining corner atom, `n′=ν(s,a,m)`: the n′-values of the
  `(s,a,m)`-fibre are exactly the `n′≥y` with `qmn′≡−1 (4sa)` (converse
  via Lemma 1.1(2); `gcd(qm,4sa)=1`). Checked, and numerically confirmed
  (Item 1). The threshold `H^{1/3−a}≤Ĥ^{1/3−a}` is in the right
  direction for HC_Π. The prime-power remark agrees with O5 Lemma 2.0′.
  So (FT_a) ⇒ HC_Π(a) for `a≤1/4`: **CONFIRMED**.

**D4 (minor-moderate; overclaim "equivalent").** §0 says "HC_Π is
**equivalent** (up to proved terms) to a bound for the corner sum 𝒦".
After Cor 2.2 it says "HC_Π(a′) … is equivalent … to
`𝒦^{>H^{1/3−a′}}≪…`". Only one direction is proved. `Σ^{>μ}` (atom
weights `2/n′`) is an *upper bound* for `Δ_O^{>μ}`. No lower bound
`𝒦≪Δ_O` (atom multiplicity per event, `2/n′` vs `1/φ(n′)`) is proved.
The 𝒦-statement also uses the threshold `H^{1/3−a′}`, and HC_Π uses
`Ĥ^{1/3−a′}≥H^{1/3−a′}`, so the 𝒦-statement is formally the stronger one.
Replace "equivalent to" by "implied by". The Status section and the
report already say "reduced to" and "follows from", which is correct.

**D7 (minor; FT is a needlessly loose target, and EVIDENCE measures 𝒦,
not FT).** `FT^{>μ}(Z)` sums `2/ν` over *every* `(s,a)` with `sa≤T` and
every `m|F`. This includes first "elements" with `ν>T/(qm)` (no atom
exists) and non-squarefree s. The proof of Thm 3.2 gives the restriction
`ν≤T/(qm)`, s squarefree, for free. Numerically
(`scripts/review_omega6_ft.py 1000000000 331 337 347 1 1 …`, Z=1, μ=1):

| κ (h) | FT | FT, s squarefree | … and `ν≤T/(qm)` | 𝒦 (whole class) |
|---|---|---|---|---|
| 1364 (341) | .0734 | .0645 | .0184 | .0149 |
| 440 (110) | .0914 | .0696 | .0259 | .0173 |
| 524 (131) | .1039 | .0838 | .0272 | .0156 |

So FT as defined is 4–6× the corner mass, and the existence restriction
removes most of the excess. The §4 table and the report ("of the average
size predicted by (FT)") measure 𝒦, not FT. That EVIDENCE says nothing
directly about (FT_a) in the form in which it is stated. Fix: state
(FT_a) with `ν≤T/(qm)` and s squarefree, and say that §4 measures 𝒦. (All
values are still below `h^{−1/4}`, so this is no evidence *against*
FT_a.)

*Assessment on Lemma 3.3 (CONFIRMED).* (1): `F≡1 (X)` gives
`m^{−1}≡m* (X)`. (2): `F<X²`. A divisor `<X` is the least residue of its
class. A divisor `≥X` is fixed by `m*<X`, and `m*` is the least residue
of `m^{−1}`. Hence ≤2 divisors per class. Numerically: 0 violations over
all `(s,a)` carrying m>1 atoms at T=10⁹. (3): `i<τ/2` is the correct
count also for odd τ (F can be a square, e.g. `κ=440`, `F=441`). Checked.
The comment "pointwise worst case `≍min(τ(F),y)/y`" is wrong for `τ>y`.
There the bound of (3) is `≍1+log(τ/y)`, not `≍1` (nit, Assessment
text).
