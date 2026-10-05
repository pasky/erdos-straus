# Shrinking the quarantine modulus: graded (fibre) quarantine (task O44)

Status: IN PROGRESS. Labels as in DISCOVERIES.md.

Notation: `𝓛=log T`; atoms `(M,D)`, `M≤T`, `M≡3 (4)`, `A=A_M=(M+1)/4`,
`D|A²` (O2 §4). ET = Elsholtz–Tao arXiv:1107.1010 (archived,
`sources/elsholtz-tao-1107.1010.pdf`); ET Thm 7.1 is their Erdős-type bound
`Σ_{n≤N}τ(P(n)) ≪_{deg,l,C} N Σ_{m≤N}ρ(m)/m`, ET Cor 7.4 its linear case.

## 0. Where `log Q_Π ≍ 𝓛^7/log𝓛` comes from, and the idea

In O2 Lemma 11.2 / Thm 11.3 (used by O8 Thm 3.4 and O9 Thm 2.2) a
quarantined prime ℓ is fixed to `n≡1 (ℓ^{e_ℓ})` with the *full* exponent
`e_ℓ=max{e: ℓ^e≤T}`, so every quarantined prime costs `e_ℓ log ℓ > 𝓛/2`.
Two costs:

* `Π_0={ℓ≤z}`, `z=𝓛²`: `π(z)𝓛 ≍ 𝓛³/log𝓛` (needed to make the width
  `k=⌊𝓛/log z⌋` small);
* bad primes `|𝓑| ≤ kS*/c_0 = 64k²S* ≪ 𝓛^6/log𝓛` (ET), each `≤𝓛`.

Idea (graded quarantine). Quarantine ℓ only to `n≡1 (ℓ^{e})` with a
*partial* exponent e chosen so that the remaining "fibre coordinate"
`n mod ℓ^{f_ℓ}` inside `1+ℓ^eℤ` carries per-coordinate mass `≤c_0`.
Heuristically the fibre mass at ℓ is `≈ S*/ℓ^{e+1}`, so it suffices to take
`ℓ^{e+1} > Y` with `Y ≍ S*/c_0 ≍ kS*`, and primes `ℓ>Y` need no quarantine
at all. Cost: `log Q ≤ Σ_{ℓ≤Y} log ℓ^{e} ≤ π(Y)log Y ≈ Y ≍ 𝓛^5` (ET).
The width also improves: every coordinate of an event uses a factor
`ℓ^{v}>Y` of M, so width `≤ 𝓛/log Y`, and no separate `Π_0`/z is needed.

What must be proved:

1. (Survival/uniform mass) O2 Lemma 11.1 covers graded quarantines
   (the proof only uses `m|gcd(M,4D+1)`).
2. (Fibre mass, the main lemma) a uniform bound
   `w_ℓ(Q) ≪ 𝓛^{O(1)}/ℓ^{e+1}` for the mass at the fibre coordinate of ℓ
   (ET Thm 7.1 / Cor 7.4 in progressions mod `ℓ^e`).
3. (Interfaces) the Haar local lemma (O2 Thm 11.3), O8 Thm 3.4's system,
   and O9 Thm 1.1's character expansion accept fibre coordinates.

## 1. The hypothesis of OMEGA10 Remark 4.3 for ES events

**1.1 The literal hypothesis is not available for ES (Assessment; not proved).**
Remark 4.3 asks `∏_{ℓ∈supp E}ℓ^{a_ℓ} ≤ T^ρ`, `a_ℓ` the largest exponent of ℓ
used by *any* event. For a free prime `ℓ∈(z,√T]` the atoms `M=ℓ^{f}m'`
(`f=f_ℓ=⌊𝓛/logℓ⌋`, `m'≤T/ℓ^f`, `M≡3 (4)`) give events with `ℓ^f | r`
whenever one survives, so one expects `a_ℓ` near `f_ℓ`, i.e. `ℓ^{a_ℓ}>T/ℓ`,
for most such ℓ. If so, an event with j free primes `≤T^{1/j}` has
`∏ℓ^{a_ℓ} ≥ T^{j-1}`, and the hypothesis would hold only with
`ρ≍k≍𝓛/log𝓛`, giving back OMEGA10 Thm 4.2's `𝓛^6`. This is an implication only.
Neither the occurrence of top powers in surviving events (it can fail:
at `T=10^4`, the only multiple of `97²` below T is `≡1 (4)`) nor the
existence of events with many such primes is proved here. §1.2 makes the
question moot.

**1.2 What is true instead: a digit-filtration form of OMEGA10 Cor 3.5.**
Write each coordinate `X_ℓ` (units mod `ℓ^{f}`, or a fibre `1+ℓ^aℤ mod ℓ^f`,
§2) in base-ℓ digits `X_ℓ=(δ_{ℓ,0},δ_{ℓ,1},…)`; the Haar measure is the
product of uniform measures on the digits (digit 0 on units mod ℓ). An ES
event fixing `X_ℓ mod ℓ^v` fixes the *initial segment* of digits `0..v-1`.
For a digit set U let `m_U:=∏_ℓ ℓ^{1+max\{i:(ℓ,i)∈U\}}` (the modulus a function
of `X_U` needs). Fix `λ_ℓ≥1` and put `Λ_{ℓ,i}:=λ_ℓ^{i+1}`.

**Lemma 1.1 (filtration C-1; PROVED).** For each ℓ let `i_0(ℓ)≥0` be the
*first free digit*: the digits `≥i_0(ℓ)` are independent uniform coordinates, and
the digits `<i_0(ℓ)` are fixed (e.g. `i_0=a_ℓ` on a fibre, Setting 2.0, or
`i_0=max(a_ℓ,v_ℓ(E_j))` on the cylinder of `E_j`, Remark (ii)). Let F be the
good-indicator of a family of events, each fixing an initial segment
`i_0(ℓ)..v_ℓ(E)−1` of the free digits at every ℓ in its support (values
arbitrary). Keep the *absolute* weights `Λ_{ℓ,i}=λ_ℓ^{i+1}` (`i≥i_0(ℓ)`). If
every event satisfies `∏_ℓ λ_ℓ^{2v_ℓ(E)} ≤ 2`, then

```
G'_F := Σ_U (∏_ℓ Λ_{ℓ, max U_ℓ})·‖F^{=U}‖² ≤ 1     (empty U_ℓ: factor 1),
```

where `F^{=U}` is the Efron–Stein decomposition over digits. With
`λ_ℓ:=2^{logℓ/(2𝓛)}` the hypothesis is `r_E:=∏ℓ^{v_ℓ(E)} ≤ T`, true for
every ES event, and `∏_ℓΛ = 2^{log m_U/(2𝓛)}`, so
`Σ_{U: log m_U>τ}‖F^{=U}‖² ≤ 2^{−τ/(2𝓛)}`.

*Proof.* Write the proof for `i_0(ℓ)=0`. For general `i_0`, re-index the free
digits and replace `Λ_{ℓ,−1}:=1` below by the weight 1 of the constants, so the
first free level `i_0` gets `1+μ'=λ^{i_0+1}`; the edge-weight bound at the end
becomes `λ^{i_0+1}·λ^{2(v−i_0−1)} ≤ λ^{2v}`. For each ℓ let `W_{ℓ,i}` (`i=−1,0,1,…`) be the functions of `X_ℓ`
measurable w.r.t. digits `≤i` and orthogonal to those of digits `<i`, and
`P_{≥j}:=I−E[·|δ_{ℓ,<j}]=Σ_{i≥j}P_{W_{ℓ,i}}`. With `μ'_{ℓ,j}:=Λ_{ℓ,j}−Λ_{ℓ,j−1}`
(`Λ_{ℓ,−1}:=1`), `Σ_iΛ_{ℓ,i}P_{W_{ℓ,i}} = I+Σ_{j≥0}μ'_{ℓ,j}P_{≥j}`. Since
`Σ_{U: max U_ℓ=i}F^{=U}` is the `W_{ℓ,i}`-component, tensoring over ℓ gives

```
G'_F = Σ_{V} μ'^{V} ‖L_V F‖²,
```

the sum over *selections* `V={(ℓ,j_ℓ)}` (at most one level per ℓ), with
`L_V:=∏_{(ℓ,j)∈V}P_{≥j}`. Now `P_{≥j}=I−E_{B}` for the *tail block*
`B_{ℓ,j}=(δ_{ℓ,j},δ_{ℓ,j+1},…)`, which is an independent coordinate. So
`‖L_VF‖²` is the top Efron–Stein energy of F w.r.t. the block coordinates
of V, and OMEGA10 Lemma 3.1's proof applies verbatim after splitting each
event into single values on the blocks (F is unchanged; one split piece of
E holds at x iff E does). Its support in V is `{ℓ: v_ℓ(E)>j_ℓ}`. Hence
`‖L_VF‖² ≤ E_x N_{Ĥ(x)}(V)²`, where Ĥ(x) is the hypergraph on vertices
`(ℓ,j)` with one edge `Ê:={(ℓ,j): j<v_ℓ(E)}` per event E holding at x (the
trace of Ê on a selection V is exactly the block support). Adding the
nonnegative terms of non-selections,
`G'_F ≤ E_x Q_{μ'}(Ĥ(x))`. By OMEGA10 Thm 3.4 this is `≤1` once every edge
has `∏_{(ℓ,j)∈Ê}(1+μ'_{ℓ,j}) ≤ 2`. Here `1+μ'_{ℓ,0}=λ` and
`1+μ'_{ℓ,j}=1+λ^j(λ−1)` (`j≥1`), and `1+λ^j(λ−1) ≤ λ²` iff `λ^j ≤ λ+1`,
which holds for `j<v_ℓ(E)` because `λ^{v_ℓ} ≤ √2` by hypothesis. So the
edge weight is `≤∏_ℓλ_ℓ^{2v_ℓ(E)} ≤ 2`. ∎

*Remarks.* (i) `Σ_jλ^j(λ−1)` telescopes to `λ^v−1`, so the edge weight is
`≤exp(Σ_ℓ(λ_ℓ^{v_ℓ}−1))`; by convexity this allows `λ_ℓ=2^{logℓ/(ρ𝓛)}` for
any `ρ ≥ 1/log₂(1+ln2) ≈ 1.32`. We use ρ=2.
(ii) *Conditioned systems.* O8's `F^{(j)}` is `F_{<j}` (the good-indicator of
the events before `E_j`) restricted to the cylinder `E_j`. At ℓ the remaining
digits start at `i_0:=max(a_ℓ,v_ℓ(E_j))` (fibre digits below `a_ℓ` are fixed by
the quarantine), and every other event restricts to a cylinder on the digits
`i_0..v_ℓ(E)−1`, again an initial segment of the free digits. This is the
case `i_0(ℓ)=max(a_ℓ,v_ℓ(E_j))` of Lemma 1.1, so the lemma holds for every
`F^{(j)}`, with the cost `m_U` measured in absolute digit positions.
(iii) The proof never uses single values on full coordinates. O8 Setting
3.0's splitting is not needed (BRW Lemma 3.1 takes any events).

**Corollary 1.2 (junta term `≪𝓛(S+𝓛)` for ES; PROVED implication inside
O8 Thm 3.4 / O9 Thm 2.2).** In OMEGA10 Thm 4.2 take for `u_j` the truncation
of `F^{(j)}` to digit sets with `log m_U ≤ τ`,
`τ:=2𝓛⌈log₂(100m²(S+1)e^{3S})⌉`, with `m≤T²` unsplit events (atoms). O8's
EL(t) counts coordinates (`|U|>t`). What holds here is its modulus-weighted
analogue

```
EL_mod(τ):   E[(F^{(j)}−u_j)² | E_j] = Σ_{U: log m_U>τ}‖(F^{(j)})^{=U}‖² ≤ e^{−3S}/(100m²(S+1))   for every j,
```

which follows from Lemma 1.1 (the tail is `≤2^{−τ/(2𝓛)}`). O8 Thm 3.4's
proof uses EL only through BRW Lemma 3.1,
`E[F−B] ≤ m²Σ_jP(E_j)E[(F^{(j)}−u_j)²|E_j]`, so EL_mod(τ) suffices there. Each `u_j` is a combination of cells of modulus `≤e^τ`, and the
cells of B have modulus `≤e^{2τ+3𝓛}`. Hence

```
log Z ≤ log Q_Π + O(𝓛(S+𝓛)) ≪ log Q_Π + 𝓛^5 log𝓛     (ET: S≤S*≪𝓛^4log𝓛),
```

independently of z and k. This is Remark 4.3's conclusion with `ρ=2`,
obtained without its hypothesis. The remaining 𝓛-powers are now all in
`log Q_Π`.

*Check* (`scripts/omega11_filtration.py 2 600`, `data/omega11/filtration.txt`):
exact digit-level Efron–Stein on random systems (≤3 primes, ≤3 digits each,
digits on [2] or [3], ≤6 events, weights scaled so the hypothesis is tight):
max `G'=0.9972` (600 systems); conditioned systems (F of events 2.., restricted
to event 1's cylinder, as `F^{(j)}`): max `1` (attained by constant F);
with the weaker scaling `∏λ^{v}≤2` (ρ=1) also max `0.9971`, so ρ=1 may well
be true (not claimed).

## 2. Graded quarantine with log-weighted thresholds: `log Q ≪ 𝓛²S*/log𝓛`

**Setting 2.0 (graded quarantine).** Exponents `0≤a_ℓ≤f_ℓ:=⌊𝓛/logℓ⌋` for
odd primes ℓ, and `Q:=8∏ℓ^{a_ℓ}`. For every odd `ℓ≤T` with `a_ℓ<f_ℓ` there is
a coordinate `X_ℓ:=n mod ℓ^{f_ℓ}`, restricted to the fibre `n≡1 (ℓ^{a_ℓ})`
(units if `a_ℓ=0`), with its uniform (Haar) measure; the coordinates are
independent on the class `n≡1 (Q)`. An atom `(M,D)` **survives Q** if
`gcd(M,Q) | 4D+1` and `M∤Q`. Its event is
`E_{M,D}: X_ℓ ≡ −4D (mod ℓ^{v_ℓ(M)})` for all `ℓ∈supp:={ℓ: v_ℓ(M)>a_ℓ}`
(consistent with the fibre since `ℓ^{a_ℓ} | 4D+1`). The **fibre mass** at
ℓ is `w_ℓ(Q):=Σ_{surviving atoms, v_ℓ(M)>a_ℓ} P(E_{M,D})`. O2's class-of-one
quarantine is the special case `a_ℓ∈{0,f_ℓ}`.

**Lemma 2.1 (uniform weights; PROVED).** For every Q and surviving atom,
`P(E_{M,D}) ≤ s(M,D) := C log log T·gcd(M,4D+1)/M`, and
`S♯ := Σ_{(M,D)} s(M,D)` obeys O2 Lemma 11.1's bound
(`≤exp((log2+o(1))𝓛/log𝓛)`; `≪𝓛^4 log𝓛` modulo ET Prop 1.4). Moreover
(I) holds: if `n≡1 (Q)` and no surviving event occurs at n, then `W(n)>T`.

*Proof.* At `ℓ∈supp` the fibre probability is `1/φ(ℓ^{v})` if `a_ℓ=0` and
`ℓ^{−(v−a_ℓ)}` if `a_ℓ≥1`; in both cases `≤(ℓ/(ℓ−1))ℓ^{min(v,a_ℓ)}/ℓ^{v}`.
Off supp, `ℓ^{v}|Q`. So `P(E) ≤ (gcd(M,Q)/M)∏_{ℓ|M}ℓ/(ℓ−1) ≤ C loglogT·g/M`
with `g=gcd(M,4D+1)`, because survival gives `gcd(M,Q)|g`. O2 Lemma 11.1's
proof bounds `Σ C loglogT·g/M` directly (it only uses `m|g`). For (I): if
`n≡1 (Q)` and `n≡−4D (M)` with `D|A_M²`, reducing mod `gcd(M,Q)` gives
survival; if `M|Q` then `n≡1 (M)`, excluded by Fact 1.1; otherwise the event
occurs. ∎

**Lemma 2.2 (graded iterated quarantine; PROVED).** Fix `0<c≤1/8`. Start from
`a_3=a_5=a_7=1`, all other `a_ℓ=0`. While some odd ℓ has `a_ℓ<f_ℓ` and

```
w_ℓ(Q) > θ_ℓ(Q) := c·(a_ℓ+1)·logℓ / 𝓛,
```

raise `a_ℓ` by one. The procedure stops, and at the end:

* (LLL) every event E has `Σ_{ℓ∈supp E} w_ℓ ≤ c`;
* (cost) `log Q ≤ log 840 + (𝓛/c)·Σ_{(M,D)} s(M,D)·log₂τ(M)
  ≤ 9 + (1+o(1))·𝓛²S♯/(c·log𝓛)`.

*Proof.* Each step raises some `a_ℓ≤f_ℓ`, so it stops. (LLL): for
`ℓ∈supp E`, `v_ℓ(M)≥a_ℓ+1`, so
`Σ_{ℓ∈supp E}w_ℓ ≤ (c/𝓛)Σ_ℓ v_ℓ(M)logℓ = c·logM/𝓛 ≤ c`.
(cost): a step at ℓ from a to a+1, taken at stage `Q_i`, has
`log ℓ < 𝓛·w_ℓ(Q_i)/(c(a+1))`, and `w_ℓ(Q_i) ≤ Σ_{(M,D): v_ℓ(M)≥a+1} s(M,D)`
by Lemma 2.1. Each pair `(ℓ,a)` is stepped at most once. The steps may be
taken in any order, and several primes may be raised simultaneously at one
stage `Q_i`: each raise is justified at `Q_i`, the bound on `w_ℓ(Q_i)` is uniform
in Q, and the stopping test concerns only the final Q. Summing,
`log(Q/840) ≤ (𝓛/c)Σ_{(M,D)} s(M,D)·h(M)` with
`h(M):=Σ_{ℓ|M}H_{v_ℓ(M)}` (`H_v=Σ_{i≤v}1/i`). Now `H_v≤log₂(v+1)` (induction:
`1/(v+1)≤log₂(1+1/(v+1))` as `log₂(1+x)≥x` on `[0,1]`), so
`h(M)≤log₂τ(M)≤(1+o(1))𝓛/log𝓛` (Wigert, `M≤T`). ∎

*Why log-weighted thresholds.* The local lemma only needs every event's
*total* coordinate mass to be small (neighbourhood sum
`Σ_{E'∼E}2P(E') ≤ 2Σ_{ℓ∈supp E}w_ℓ`), not each `w_ℓ≤1/(64k)`. Charging the
threshold to the factor `ℓ^{a+1}` of M that the coordinate consumes makes the
budget `log M≤𝓛` do the work of the width k. In particular **no initial
`Π_0={ℓ≤z}` is needed, and z, k disappear**; this alone removes O2's
`π(z)𝓛≍𝓛³/log𝓛` floor and the factor `k²` of `|𝓑|≤64k²S*`.
The ratio (cost of a step)/(threshold) is `logℓ/θ = 𝓛/(c(a+1))`, uniform in
ℓ; with full quarantine it would be `≍𝓛²/logℓ`.

## 3. Assembly: exponent 1/6

**Lemma 3.1 (linear transfer with fibre cells; PROVED modulo (G), as O9
Thm 1.1).** Assume `8|Q`. Then O9 Thm 1.1 holds without `gcd(d_i,Q)=1`, provided every cell is
consistent with the class of one (`b_i≡1 mod gcd(d_i,Q)`), and with
`E_D` replaced by `E_H`, the Haar mean over `H:={x∈(ℤ/N)^*: x≡1 (Q)}`,
`N:=lcm(Q,D)`. That is: `μ:=E_H B>0`, `A:=E_H|B|/μ`, `Z:=Q·max d_i`; twist
condition `|E_H[Bψ]|≤μ/4` for every real primitive ψ of conductor `f>1`
with `gcd(f,Q)=1` and `f|d_i` for some i.

*Proof (changes only).* On `G=(ℤ/N)^*`, `f(n)=B(n)1[n≡1 (Q)]` has
`c(χ)=φ(N)^{−1}Σ_{n∈H}B(n)χ̄(n)=E_H[Bχ̄]/φ(Q)` (`G→(ℤ/Q)^*` is onto with
kernel H). So `|c(χ)|≤Aμ/φ(Q)`, `c(χ_0)=μ/φ(Q)`. Item 1: by consistency each
term of f is one cell mod `lcm(d_i,Q)≤Qd_i≤Z`, so `c(χ)≠0` forces
`cond χ≤Z`. Item 3: let χ be real with `c(χ)≠0`, induced by a primitive ψ of
conductor f. Split `ψ=ψ_1ψ_2`, with the primes of `f_1` dividing Q and
`gcd(f_2,Q)=1`. Real primitive conductors have squarefree odd part and
2-part `|8`, and `8|Q`, so `f_1|Q` and `ψ_1≡1` on H. If `f_2=1`, χ is trivial
on H, hence induced from a character mod Q: this is Case A (`q_1|Q≤Z`,
`c(χ)=μ/φ(Q)`), unchanged. If `f_2>1`, then `c(χ)=E_H[Bψ_2]/φ(Q)`, and a
cell with `f_2∤d_i` has zero `ψ_2`-mean (average over a free prime
`p|f_2`, `p∤d_i`, whose coordinate is uniform on units on H). So the twist
condition applies to `ψ_2`, and Case B is unchanged. The rest of O9 Thm
1.1's proof does not use coprimality (`log N≤log Q+1.04 max d_i`). ∎

**Theorem 3.2 (PROVED modulo (G), Elsholtz–Tao Prop 1.4 and OMEGA10 Thm 3.4 (internal; two SOUND reviews)).** For
infinitely many Mordell-hard primes p,

```
W(p) ≥ exp( c·(log p)^{1/6} );     uniformly  log L_h(T) ≪ (log T)^6.
```

*Proof.* Lemma 2.2 with `c=1/64` gives Q (`840|Q`) with
`log Q ≤ 9+(1+o(1))64𝓛²S♯/log𝓛 ≪ 𝓛^6` (ET: `S♯≪𝓛^4log𝓛`). Then follow O9
Thm 2.2, with these changes.
* Haar side: neighbourhood sums `≤2c=1/32`, so `δ=E_HF≥e^{−2.2S}`,
  `S=S_tot(Q)≤S♯`, as in O8 Thm 3.4.
* Minorant: O8 Lemma 3.1 (BRW) on the `m≤T²` unsplit events, with `u_j` from
  OMEGA10 Thm 4.2 (coordinate-count truncation; supports `≤ω(M)≤2𝓛/log𝓛`),
  which already gives a junta `≪k𝓛(S+k𝓛)≪𝓛^6`, so EL holds and
  `E[F−B]≤δ/100`. **Lemma 1.1/Cor 1.2 is not needed for Thm 3.2**; it is
  needed only for Cor 4.1 (the 1/5 implication), where the junta must be
  `≪𝓛^5log𝓛`.
* Twist: O8 Lemma 3.3 verbatim. It needs only the neighbourhood sums
  `≤1/32` and `w_{ℓ_0}≤c=1/64` at a prime `ℓ_0|f_2`, which is a coordinate with
  `a_{ℓ_0}=0`, since `gcd(f_2,Q)=1`.
* Transfer: Lemma 3.1 with O9 Lemma 2.1 (`A≤1.03`) and the auxiliary prime
  `ℓ_aux∈(R,2R]`, `R=max(T,max d_i)`, appended to Q (it exceeds T, so no
  event uses it).

So `log Z ≤ log Q + O(𝓛(S♯+𝓛)) ≪ 𝓛^6`, and some hard `p>T` with `W(p)>T` has
`log p≪𝓛^6`. ∎

*Unconditionally* (no ET) nothing changes: `log S♯≤(log2+o(1))𝓛/log𝓛`, so
O9 Thm 2.3 (`log W≥(1/log2−o(1))log₂p·log₃p`) stands.

*Ledger after Thm 3.2 (under ET).* `log Q ≤ 64(1+o(1))𝓛²S♯/log𝓛`, i.e.
`≍𝓛^6` if `S♯≍𝓛^4log𝓛`; junta `≪𝓛(S+𝓛)≪𝓛^5log𝓛` (Cor 1.2). **The quarantine is
again the bottleneck**, now by a factor `≍𝓛/log𝓛` (`64𝓛²S♯/log𝓛` against `𝓛S♯`). The lossy step is the
worst-case charge `h(M)≤log₂τ(M)≤𝓛/log𝓛` per atom in Lemma 2.2 (§4).

**Corollary 3.3 (Haar side; PROVED modulo ET).** Lemma 2.2 with `c=1/8` and
the local lemma (neighbourhood sums `≤1/4`) give
`log(1/δ*(T)) ≤ log φ(Q)+4S♯ ≪ 𝓛²S♯/log𝓛 ≪ 𝓛^6`. This improves O2 Thm 11.3's
`𝓛^7/log𝓛`.

## 4. Below `𝓛^6`: the charge moment, EVIDENCE, and the floor of the architecture

The only lossy step in Lemma 2.2 is the worst-case bound
`h(M)≤log₂τ(M)≤𝓛/log𝓛`. The proof actually gives

```
log Q ≤ 9 + (𝓛/c)·Ω♯,     Ω♯ := Σ_{(M,D)} s(M,D)·h(M),   h(M)=Σ_{ℓ|M}H_{v_ℓ(M)} ≤ ω(M)+Σ_{ℓ²|M}log₂(v_ℓ+1).
```

**Hypothesis H_ω(B).** `Ω♯ ≪ 𝓛^4(log𝓛)^B`, i.e. the s-weighted mean of
`h(M)` is `≪(log𝓛)^{B−1}` given `S♯≍𝓛^4log𝓛`. (Heuristically `B=2`: `ω(M)` has
mean `log log T` under any reasonable weighting.)

**Corollary 4.1 (PROVED implication).** Under H_ω(B), ET, (G) and OMEGA10 Thm
3.4: `log Q≪𝓛^5(log𝓛)^B`, `log Z≪𝓛^5(log𝓛)^{max(B,1)}`, hence
`W(p) ≥ exp(c(log p)^{1/5}(log log p)^{−max(B,1)/5})` for infinitely many
Mordell-hard p. (Proof: Theorem 3.2's proof with the displayed cost and
Cor 1.2's junta.) ∎

**EVIDENCE for H_ω** (`scripts/omega11_hmoment.py`, `data/omega11/hmoment.txt`;
the factor `C loglog T` of s replaced by the exact `∏_{ℓ|M}ℓ/(ℓ−1)`). The s-weighted mean of h at
`T=10^4,10^5,10^6` is `2.32, 2.57, 2.79` (with the pure weight `g/M`: `2.18, 2.42, 2.63`). This tracks `log log T`
(`2.22, 2.44, 2.63`; steps `0.25, 0.22` against `0.22, 0.19`), while the worst-case charge
`𝓛/log𝓛` is `4.15, 4.71, 5.26` (steps `0.56, 0.55`). So the mean charge is
consistent with `log𝓛+O(1)`, i.e. `B=2`. Most of `Ω♯` comes from primes
`ℓ≤𝓛²` (`141/172, 308/389, 593/770`). This is not a proof.

*What H_ω needs (Assessment).* Write `ω(M) ≤ ω_{≤y}(M)+𝓛/log y` with
`y=T^{1/log𝓛}`. Then H_ω(2) follows from the averaged per-prime bound

```
Σ_{ℓ≤y} V(ℓ) ≪ 𝓛^4(log𝓛)^2,      V(ℓ) := Σ_{(M,D): ℓ|M} s(M,D),
```

plus the analogous sum over `ℓ²|M`. That is ET Prop 1.4 in arithmetic
progressions to moduli `ℓ≤T^{o(1)}`, *on average over ℓ*. In the
parametrisation of O2 Lemma 4.1 (`D=sr'²`, `A=sr'k`, `m|r'+k`,
`m|n:=4sr'²+1`) one has the identity

```
M = m·N,     N = 4sr'u − n/m,   u := (k+r')/m,   and  s(M,D) ≍ 1/N  (up to loglog),
```

so `V(ℓ)` counts `ℓ|m` or `ℓ|N`. The main terms are `≪S♯/ℓ`. The obstruction
is the *first term* of each u-progression: for fixed `(s,r',m)` the least u
with `ℓ|N(u)` has weight `≤1/max(ℓ,N_min)`, and there are `≍T` triples. An
upper bound needs these first elements to be equidistributed over
`(s,r',m)` (or over ℓ). For a single ℓ this is a uniform Shiu/Henriot-type
bound for divisors of `4sr'²+1` in residue classes. We did not prove it,
even on average over `ℓ≤y`.

**The floor of this architecture (Assessment).** Any graded class-of-one
quarantine feeding *this* local-lemma criterion (`x_E=2P(E)`, neighbourhood
sums `≤1/4`) needs at least `w_ℓ ≤ 1/8` at every coordinate (a property of the
chosen sufficient criterion, not of every local-lemma argument). If the fibre masses behave like `w_ℓ(a)≈κS/ℓ^{a+1}` (as the
main terms suggest), this alone forces `ℓ^{a_ℓ+1}≳S` for all `ℓ≲S`, so
`log Q ≳ Σ_{ℓ≤S}log(S/ℓ) ≍ S/log S`, which is `≍𝓛^4` under ET with `S≍S♯`.
Lemma 2.2's per-event rule (thresholds `∝log ℓ^{a+1}/𝓛`) costs
`≍S𝓛/log(S𝓛)` under the same model. That is `𝓛^5` up to logs, and
`𝓛^5log𝓛·…` is what Cor 4.1 gets. Junta (`𝓛S`) and quarantine are then
balanced, so **1/5 is the natural limit of the present ES-modulus route**.
Going further would need both a smaller junta modulus than `𝓛·S` (O9 Lemma
4.1's floor in modulus form, OMEGA10 §1) and a quarantine cheaper than
`S𝓛`. No lower bound for `S` beyond O8 Prop 6.6 (`S≫𝓛²`, modulo a
standard BV lower bound) is known here, so these floors are not theorems.

**Finite-T EVIDENCE for Lemma 2.2** (`scripts/omega11_graded.py`;
`data/omega11/graded*.txt`). The local-lemma quantity
`max_E Σ_{ℓ∈E}w_ℓ` stays below c in every run. The script runs the
*distinct-event* variant of Lemma 2.2 (thresholds tested on distinct-event
masses, all violators raised per round). That variant is equally valid: the
local lemma works with distinct events, and their masses are at most the
atomic sums used in the charging. It can stop earlier than the atomic
iteration as written (at `T=10^4` the atomic mass at ℓ=1237 is 0.01456,
above its threshold 0.01208, review R44a).

| T | c | rounds | log Q (graded) | #primes in Q | largest | max exponent | `max_EΣw` | proven cost bound |
|---|---|---|---|---|---|---|---|---|
| 10⁴ | 1/64 | 2 | 1900 | 287 | 9239 | 2 | 0.0144 | 1.0·10⁵ |
| 10⁵ | 1/64 | 3 | 4054 | 557 | 21839 | 3 | 0.0136 | 2.9·10⁵ |
| 10⁶ | 1/64 | 4 | 7531 | 960 | 34319 | 4 | 0.0129 | 6.8·10⁵ |
| 10⁵ | 1/8 | 3 | 690 | 126 | 1439 | 3 | 0.0711 | 3.6·10⁴ |
| 10⁶ | 1/8 | 4 | 1247 | 206 | 1847 | 4 | 0.0764 | 8.5·10⁴ |

For comparison, O2 Lemma 11.2 at `T=10^5`, `z=20` with the matching per-prime
threshold `c_0=1/(64k)=0.0052` gives `log Q_Π=8942`
(`scripts/omega2_iterq.py 100000 20 0.0052`). With `c=1/8` the Haar
certificate is `log(1/δ*) ≤ 764` at `10^5` and `≤1390` at `10^6`, against O2's
1479 and 3565 (`c_0=1/(8k)`, z=20, O2 §11 table).
At these T the asymptotic gain (`≍𝓛/log𝓛`: `64𝓛²S♯/log𝓛` against O2's `64k²S*𝓛=16𝓛³S*/log²𝓛` at `z=𝓛²`) is small, and the ratios
(≈2) are illustrative only.

## 5. Status and scope

| item | statement | label |
|---|---|---|
| §1.1 | Remark 4.3's literal hypothesis holds for ES only with `ρ≍k` | Assessment (mechanism proved) |
| Lemma 1.1, Cor 1.2 | digit-filtration C-1; ES junta modulus `≪𝓛(S+𝓛)`, i.e. Remark 4.3's conclusion with ρ=2 | PROVED (from OMEGA10 Thm 3.4) |
| Lemma 2.1–2.2 | graded quarantine, log-weighted thresholds: `log Q ≤ 9+(𝓛/c)Ω♯ ≤ 9+(1+o(1))𝓛²S♯/(c log𝓛)` | PROVED |
| Lemma 3.1 | O9 Thm 1.1 with fibre cells | PROVED modulo (G) |
| Thm 3.2 | `W(p)≥exp(c(log p)^{1/6})` i.o. | PROVED modulo (G), ET Prop 1.4, OMEGA10 Thm 3.4 |
| Cor 3.3 | `log(1/δ*)≪𝓛^6` | PROVED modulo ET |
| Cor 4.1 | exponent `1/5` up to `(log log p)^{O(1)}` under H_ω | PROVED implication |
| H_ω | `Ω♯≪𝓛^4(log𝓛)^B` | OPEN; EVIDENCE (B=2) |
| §4 floor | `≈1/5` for this route | Assessment |

Not claimed: anything about ES itself; optimality of 1/6; H_ω.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 900 uv run python scripts/omega11_filtration.py 2 600)        # Lemma 1.1 check, ~3 min -> data/omega11/filtration.txt
(ulimit -v 8000000; timeout 1200 uv run python scripts/omega11_graded.py 10000)           # Lemma 2.2, seconds
(ulimit -v 8000000; timeout 1200 uv run python scripts/omega11_graded.py 100000)          # ~1 min -> data/omega11/graded.txt
(ulimit -v 8000000; timeout 5400 uv run python scripts/omega11_graded.py 1000000)         # ~10 min -> data/omega11/graded_1e6.txt
(ulimit -v 8000000; timeout 1200 uv run python scripts/omega11_graded.py 100000 0.125)    # -> data/omega11/graded_c8.txt
(ulimit -v 8000000; timeout 600 uv run python scripts/omega2_iterq.py 100000 20 0.0052)   # O2 comparison row
(ulimit -v 4000000; timeout 1800 uv run python scripts/omega11_hmoment.py 10000 100000 1000000)  # §4, ~5 min -> data/omega11/hmoment.txt
```
