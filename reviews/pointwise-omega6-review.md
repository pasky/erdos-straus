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
| 3 | Lemma 3.1, Thm 3.2, (FT_a) ⇒ HC_Π(a) | **CONFIRMED** as a sufficient condition. Claims of "equivalence" are wrong (D4). FT is looser than needed (D7) |
| 4 | Prop 3.4, Cor 3.5 (long planes; exact residual) | **CONFIRMED** as stated. Scope is overstated (D5). The description of residual (b) is wrong for (a,b)-short boxes (D6). The Regime III side remark is wrong in one subcase (D8) |
| 5 | EVIDENCE table and replay | **CONFIRMED**: both replays are byte-identical. Wording nits (D9) |
| 6 | Honesty of status: HC_Π, HC*, rate NOT proved; exact residual | **CONFIRMED** honest. The residual statement is correct, but its "in particular" gloss needs D5/D6 |

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

## Item 4 — Prop 3.4, Cor 3.5. CONFIRMED as stated, with scope defects

* **Prop 3.4(1),(2).** Corner atoms in the box are first elements of
  `(s,a,m)`-fibres, so there are at most `Σ_{(s,a)∈box}τ(F)=SA·D(S,A)` of
  them. Each weighs `≤(4/3)qμ_0/(SAB)` (`4SAB−1≥3SAB`). So the box gives
  `≤(4/3)qμ_0D(S,A)/B≪4^k𝓛²μ_0/B` in Regimes I–II. Checked.
* **Prop 3.4(3).** O5 Prop 7.1's long-box bound gives
  `Σ_{box}τ(a+b)≤2τ(q)(2+𝓛)AB/q` (it needs `max(A,B)>3q²`, so that
  `4√B<2.4B/q`). The box then gives `≤(8/3)τ(q)(2+𝓛)μ_0/S`. Checked.
* **Cor 3.5.** If a plane is long and its third side is `≥μ_0W`, the
  box gives `≤H^{−a}`, and there are `≤8𝓛⁴` boxes. Together with Thm 3.2
  this gives `B′=5` (6 is safe). With three long planes, `S,A,B<μ_0W`
  and `32SAB>4sab>qmy≥qμ_0y`. So `μ_0>(qy/32)^{1/2}W^{−3/2}`, and
  `(qy/32)^{1/2}>y^{3/2}/6` because `q>y²`. Checked.

**D5 (moderate; scope of the "three long planes" gain).** "Long" for
`(a,b)` means `max(A,B)>3q²`. Since `a,b≤T`, **the (a,b)-plane is never
long when `q≥T^{1/2}`**. With three long planes, say `B>3q²`, the
`(s,a)`-plane is long only if `S≥3q^{4/3}` or `A≥C_1q^{3/2}`. Then
`T≥4SAB≫q^{10/3}`. So boxes with three long planes exist only for
`q≲T^{3/10}`, i.e. for vertex sets with `|O|≲0.3(k+1)` free primes (as
`q≥y^{|O|}`, `y=2T^{1/(k+1)}`). Cor 3.5 says "In the regime of O4
Thm 4.2 … it is `y^{3/2}H^{−3a/2−o(1)}`, far beyond O5's `H^{1/3−a}`".
The report repeats this ("With three long planes, HC_Π holds for
`m<…`. In O4's Thm 4.2 regime this is about `y^{3/2}H^{−3a/2}`"). Both
invite the reading that the m-range of HC_Π has been pushed from
`H^{1/3−a}` to `y^{3/2−o(1)}` in the main regime. It has not. For
`|O|≥(k+1)/2` (`q≥T^{1/2}`), part (a) of the residual is empty, part (b)
is everything outside Prop 3.4(1),(2), and the m-threshold proved there
is still O5's `H^{1/3−a}`. Fix: state the q-range (`q≲T^{3/10}`) next to
the threshold, in Cor 3.5, §0 and the report.

**D6 (moderate; Assessment of residual (b) is wrong for one sub-case).**
Cor 3.5's text and the report describe (b), "boxes with a short plane",
as follows: "the numbers `4sa²+1` are `≤q^{O(1)}`, and the only divisor
bound I have there is pointwise". That holds when the short plane is
`(s,a)` or `(s,b)` (Regime III: `S,A≪q^{14/5}`). It is **false** when the
only short plane is `(a,b)` (`max(A,B)≤3q²`). There both s-planes may be
long, so Shiu/Henriot *do* apply. The box survives only because its third
sides are small (`A,B<μ_0W`), while `S` can be as large as `2qμ_0`. So the
obstruction is not "no averaging theorem". (The numbers are `≤q^{O(1)}`
only with an exponent that grows like `𝓛/log q`. That is harmless when
`q≥T^{1/2}`, but not for small q.) Unlike (a), this
sub-case has **no** lower bound on m: `S<μ_0W` fails, so the derivation
of (a) does not apply. This sub-residual (`a,b<2mW`, any m>μ, large s) is
the hub-like / unbalanced-ray family of O5 §4 (DIV). It is plausibly the
heart of the problem (§4: κ=1364's mass sits at `(s,a)=(341,1)` and its
mirror `(27713,·,1)`). For `q≥T^{1/2}` (D5) it is present in every box
with long s-planes. Fix: split (b) into (b1) "an s-plane is short
(numbers `≤q^{O(1)}`)" and (b2) "only (a,b) is short, `a,b<2μ_0W`, m
unrestricted". State (b2) explicitly in §0, §5 and the report.

**D8 (minor; false side remark).** Cor 3.5 claims: "Regime III's
`q^{−3/8}` saving does handle short (s,a)-boxes whose third side is
`B≥2^{k+7}μ_0q^{5/8}H^a`". Regime III has three subcases. The third
(`32SA²<q`) has `D(S,A)≤2H^{−1/2}`, with **no** `q^{−3/8}`. There the box
bound `(4/3)qμ_0D/B` needs `B≫qμ_0H^{a−1/2}`, not `μ_0q^{5/8}H^a`. The
next clause ("all boxes with `32SA²<q` contain the same single pair")
reads as an aside, not as the needed exception. The claim holds for the
first two subcases (`2^{k+1}q^{−3/8}`, `64q^{−3/8}`; `2^{k+7}≥128`
covers both). Fix: "for boxes with `32SA²≥q`". (The single-pair
statement itself is right: `4sa²<q` with `4sa²≡κ` forces `4sa²=`
the least residue of κ, and squarefree injectivity gives uniqueness,
given D2.)

## Item 5 — EVIDENCE (§4). CONFIRMED

Both replays (`omega6_corner.py` at T=10⁹ and T=10¹¹) reproduce
`data/omega6/corner_1e9.txt` and `corner_1e11.txt` byte for byte.
T=10⁹ took 0.6 s and T=10¹¹ about 2 min. The §4 table matches the data:
14756/10452 and 271490/166698 atoms; `.038/.017`, `.015/.015`,
`.015/.015`; `.092/.011`, `.013/.0086`, `.0083/.0080`. The script's
corner test matches Def 1.3. A fibre's predecessor counts as an element
iff it is positive with `n′≥y`, and pseudo-atoms count, as in the text.

**D9 (minor; wording).** (i) "The heaviest corner classes are hub-like:
at T=10⁹, κ=1364 (h=341)". κ=1364 is only third. The heaviest are
κ=440 (h=110; `F=441=21²`) and κ=524 (h=131). All are F1 hubs, so the
point stands, but say "the heaviest class with h>256". (ii) "one first
element per divisor m (Lemma 3.3)" for `F=1365`. Only m=15 and m=3 give
corner atoms (`(341,1,461669)`, `(341,1,110852)`). The mirror is
`(27713,1364,1)`, m=3. The other 13 divisors give no corner atom. Their first
element lies beyond `T/(qm)`, or is not an atom, or fails another
corner condition. (iii) "of the
average size predicted by (FT)": FT itself is 5× larger (D7).

## Item 6 — honesty of status. CONFIRMED

§0, §5 and the report all say that HC_Π, HC* and the `(log₂p)^{3/2}`
rate are **open**. They say the proved rate is O4 Cor 3.1 and that
nothing is claimed for ES. The Cor 3.5 residual ("every plane short or
third side `<μ_0W`") is an exact complement of what Prop 3.4 proves, and
I confirm it as stated. Only its gloss is defective: (a) is empty for
`q≥T^{1/2}` (D5), and (b) is mis-described for (a,b)-short boxes (D6).
The labels PROVED / modulo Shiu, Henriot, O5 Prop 7.1 / Assessment /
EVIDENCE are used correctly, apart from D4's "equivalent".

## Defect list

| # | Severity | Where | Defect | Fix |
|---|---|---|---|---|
| D1 | minor | §2 cited theorems | α=1/2 is outside Shiu's range `0<α<1/2` | Use α=1/4 for Shiu (`y_1=x_1/2`) |
| D2 | minor | Thm 1.5, Prop 2.1 III, Thm 3.2 | `D_sa`, `D_sb`, FT sum over all s, but Regime III's injectivity/single-pair needs s squarefree | Restrict to squarefree s (free: only atom fibres are charged) |
| D3 | minor | Thm 1.5 Rem (ii), Cor 2.2 | O5 Prop 7.1 gives `P_1≪2^k𝓛³…`, not `𝓛²` | Correct the exponent (absorbed by `𝓛⁵`) |
| D4 | minor-moderate | §0, after Cor 2.2 | "HC_Π equivalent to a 𝒦-bound": only ⇐ is proved (Σ is an upper bound for Δ_O; thresholds H vs Ĥ) | "implied by" |
| D5 | moderate | Cor 3.5, §0, report | Three long planes need `q≲T^{3/10}`; for `q≥T^{1/2}` the (a,b)-plane is never long. The `y^{3/2}H^{−3a/2}` m-threshold "in the Thm 4.2 regime" is vacuous for large O | State the q-range wherever the threshold is quoted |
| D6 | moderate (Assessment) | Cor 3.5 (b), §5, report | (b) "no averaging theorem, numbers `≤q^{O(1)}`" is wrong for boxes whose only short plane is (a,b). There Shiu/Henriot apply, `a,b<2mW`, s is large, and **m is unrestricted**: the hub/unbalanced-ray family | Split (b) into (b1) short s-plane, (b2) (a,b)-short with small a,b, any m; name (b2) as a main residual |
| D7 | minor | Thm 3.2, (FT_a), §4 | FT ignores `ν≤T/(qm)` and squarefree s, and is 4–6× 𝒦 numerically. EVIDENCE measures 𝒦, not FT | Add both restrictions to FT; say §4 measures 𝒦 |
| D8 | minor | Cor 3.5 (b) aside | The `q^{−3/8}` saving does not hold in the subcase `32SA²<q` (bound `2H^{−1/2}`) | "for boxes with `32SA²≥q`" |
| D9 | minor | §4 bullets | "heaviest" κ=1364 is third; "one first element per divisor" is false (2 of 15); "size predicted by FT" | Reword |
| nits | — | Prop 2.1 | Statement omits `h_1>H` / squarefree s; Regime II "single points" are unnecessary, and the bound is not "like Regime III"; "worst case `≍min(τ,y)/y`" should be `≍min(τ/y,1+log(τ/y))` | Reword |

## Overall verdict

All PROVED items (Lemmas 1.1–1.4, Thm 1.5, Prop 2.1, Cor 2.2, Lemma 3.1,
Thm 3.2, Lemma 3.3, Prop 3.4, Cor 3.5) are **CONFIRMED**, modulo Shiu
Thm 1, Henriot Thm 4 and O5 Prop 7.1. I checked the hypotheses of both
cited theorems against the archived PDFs: Henriot's primitivity is met
via `P/g_0`, `Δ_D=1`, and the range is `x≥c_0‖P_1‖^{1/4}`. The one range
slip (D1, Shiu's α) is fixed for free. No defect breaks a proof.
D2 is a definitional repair, and D4/D8 are wording.

The genuine gains are:
* `D_sa≪4^k𝓛⁴(H^{−1/2}+q^{−1/4})`, which gives all period terms of the
  large-m problem for all m>1, with exponent 1/4;
* the reduction of HC_Π(a), `a≤1/4`, to the first-term sum FT_a.

The headline extension of the m-range (`y^{3/2−o(1)}`) applies only to
`q≲T^{3/10}` (D5). The residual is larger than the gloss suggests: it
includes the (a,b)-short family with small a,b and **unrestricted m**
(D6), which is where the numerical corner mass sits. HC_Π, HC* and the
`(log₂p)^{3/2}` rate remain **open**, and O6 labels them honestly as
such.

Recommended before merge: apply D1–D9. D5 and D6 change the narrative
in §0, Cor 3.5, §5 and the report. The rest are one-line fixes.
