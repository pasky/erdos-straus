# HC(a,B) and the inverse-square problem (task O13)

Labels follow the house rules. ES is not solved here or anywhere.
Notation as in `POINTWISE_OMEGA4.md` (O4) §4.2 and §7: a vertex set O
at free primes `ℓ_1,…,ℓ_{j+1}` (all `>y`), `q:=∏ℓ_i` (squarefree, odd,
`q>y²`), CRT class `c mod q`, `κ:=−c` (a unit mod q). Atoms are written
`(s,a,b)` with **s squarefree** (O3 Lemma 2.1: this is a bijection onto
atoms), `M=4sab−1`, `q|M`, `a≡κb (q)`, `M=q·m·n′` with m the Π-part and
n′ the rest of the rough part; `P(e∖O)=1/φ(n′)≤2/n′` (n′ has `≤k`
prime factors, all `>y`), `n′≥y`. Survival: `m|4sa²+1`.

## 0. Summary (filled in as the work proceeds)

* §1 (PROVED). The obstruction of O4 Prop 7.3/§7.5 — the count
  `#{t≤t_0 : w·t̄² mod q ≤ Y}` beyond the Weil range — is **not** what
  HC needs. HC sums over *atoms*, and atoms have squarefree s. Then
  `(s,t) ↦ st²` is injective, so the relevant count is
  `#{(s,t): s squarefree, s≤Y, t≤t_0, st²≡w (q)} ≤ Yt_0²/q+1`,
  pointwise in w, with no divisor loss and no Kloosterman input.
* §2 (PROVED). **Theorem 2.3:** the `m=1` part of every non-hub codegree
  is `≪𝓛⁴4^{k/3}H^{−1/3}` for `4^k≤H≤y`. This is HC* (the restricted
  form of HC, Cor 4.1) with `a=1/3` for events whose atom has trivial
  Π-part, with saturated hubs (Def 2.0). **HC as literally stated in O4 is
  false** for lifted vertices: a non-hub lift of a hub class has codegree
  `≫1` (Def 2.0). O4 Thm 4.2 holds under HC* (saturated hubs; Cor 4.1(ii)). The proof combines the lifting with square-root
  counts and a thin-box lattice lemma. It uses no exponential sums.
* §3 (PROVED). The Π-part m (O4 gap (iii)) satisfies `m|u+v` and
  `m|4sa²+1`. Events with `m≤H^{1/3−a}` give HC* with exponent a (any `a<1/3`), and ray sums
  are bounded for balanced rays.
* §4. **Open residual HC_Π (large m).** It is a divisor-function problem
  in short progressions, not a Weil-range inverse problem. HC_Π implies
  HC*, and hence O4 Thm 4.2's `log W ≥ c(log₂p)^{3/2}` (Cor 4.1). Literal HC
  is **false** (Def 2.0), so O4 Thm 4.2 as stated is vacuous; it holds
  with HC* (Cor 4.1(ii)). HC* (saturated hubs) is open, and the proved
  rate stays O4 Cor 3.1.
* §5. Literature: no known theorem gives O4's IS. HC never needed IS
  (squarefree s).

## 1. The squarefree lifting lemma (PROVED)

**Lemma 1.1.** Let `q≥1`, `w∈ℤ`, `X≥1`. Then

```
#{(s,t)∈ℕ² : s squarefree, st²≤X, st²≡w (mod q)} ≤ X/q + 1.
```

*Proof.* Every positive integer n has exactly one factorisation `n=st²`
with s squarefree. So the pairs inject into
`{n≤X : n≡w (q)}`, which has at most `X/q+1` elements. ∎

**Corollary 1.2 (O4's core count, corrected).** In O4 Prop 7.3 a ray
`(a,b)=t(u,v)` (`gcd(u,v)=1`, `h=uv`) carries the atoms `(s,tu,tv)` with
`4hst²≡1 (q)`. Only squarefree s give atoms (other s give the same
`(M,D)` as an atom with smaller s and larger t, Lemma O3 2.1), so the
count O4 needs is

```
N^sf(q,w;t_0,Y) := #{t≤t_0, s≤Y squarefree : st²≡w (q)} ≤ Yt_0²/q + 1 ≤ Y/(4h) + 1
```

for `t_0≤(q/(4h))^{1/2}`, `w=(4h)^{−1}`. O4's target was `≪𝓛^B·Y·h^{−a}`;
this gives it with `a=1` whenever `Y≥h`, and with the absolute bound 2
when `Y<h`.

*Remark (why O4 met a Weil-range problem).* O4 counted every t with the
least residue `s_t:=w t̄² mod q ≤ Y`, squarefree or not. For non-squarefree
`s_t` the triple `(s_t,tu,tv)` is the *same atom* as some `(s′,t′u,t′v)`
with `s_t t²=s′t′²`, so O4's count over-counts each atom by up to
`#{t: t²|n}`, which can be `T^{c/log𝓛}`. The over-counted problem lies
beyond the Weil range, but lifting alone brings it within a divisor factor
`min(T^{O(1/log𝓛)},√Y)` of the target (§5). It is not shown to be hard,
and the atom count is elementary.

## 2. HC for the m=1 part, with a=1/3 (PROVED)

For an odd modulus Q, a unit K mod Q and `y≥2`, put

```
Δ¹(Q,K) := Σ 1/n   over (s,a,b)∈ℕ³, s squarefree, a≡Kb (Q), Q | 4sab−1,
                   n := (4sab−1)/Q ∈ [y, T/Q],
h_3 := min{ab : a≡Kb (Q), gcd(ab,Q)=1},  h_1 := min{sa : 4sa²≡K (Q)},
h_2 := min{sb : 4Ksb²≡1 (Q)},            Ĥ := min(h_1,h_2,h_3,y).
```

(minima over positive integers; s may be taken squarefree, since
`s=s′f²` gives `4sa²=4s′(fa)²` with `s′·fa≤sa`). The events with Π-part
`m=1` contribute at most `2Δ¹(q,κ)` to `Δ_O` (`P(e∖O)≤2/n′`, `n′=n`).
If no vertex of O is a *saturated* H-hub (Definition 2.0), then
`h_1,h_2,h_3>H` for `(q,κ)`: `c≡−u/v ⇔ u≡κv`, `c≡−4sa² ⇔ 4sa²≡κ`,
`c≡−1/(4sb²) ⇔ 4κsb²≡1`, and a congruence mod q holds mod every `ℓ|q`.

**Definition 2.0 (saturated hubs; a required repair of O4's HC).** A vertex
`(ℓ,x mod ℓ^{e_ℓ})` is a *saturated H-hub* if `x mod ℓ^v ∈ 𝓗_H(ℓ^v)` for
some `1≤v≤e_ℓ`.

*Why it is needed (review O13-D1; PROVED counterexample to HC as literally
stated in O4).* Take O4's k=3. Choose primes `ℓ_1,ℓ_2` near y (so `e_{ℓ_i}≥2`)
and lifts `x_i` of `−1 mod ℓ_i` that are not hubs mod `ℓ_i^{e}`. This is
possible since there are `ℓ_i^{e−1}` lifts and only `O(H log H)` hub classes.
For every M ≡ 3 (4), `(s,a,b)=((M+1)/4,1,1)` is an atom of class −1 and
Π-part 1. So for every prime `r∈[T^{.28},T^{.32}]` with `ℓ_1ℓ_2r≡3 (4)`, the
event of class −1 mod `ℓ_1ℓ_2r` contains O, and most of its lifts at r
survive hub deletion. Hence `Δ_O ≥ c·Σ_r 1/r ≫ 1` while O has no H-hub in
O4's sense, so HC as stated fails, and O4 Thm 4.2 must be read with saturated hubs.
(Lifting convention: O2 §10.3 splits a class mod `ℓ^a` into its lifts as
disjoint events with the same union, and `Δ_O` is unchanged for O containing
a lifted vertex. So the lift `x_i` inherits the codegree of the class −1.)
*Cost.* The quarantined mass becomes
`h_ℓ ≤ Σ_{v≤e_ℓ}|𝓗_H(ℓ^v)|/φ(ℓ^v) ≤ 3H(1+log H)/(ℓ−1)·Σ_{v≥1}ℓ^{1−v}
= 3H(1+log H)/(ℓ−1)·ℓ/(ℓ−1)` (review O13r-D3). This is O4's bound up to a
factor `1+O(1/y)`. So O4 Thm 4.2 step 2 (`300H(1+log H)<y`, `h_ℓ≤1/100`) and
`S_hub` are unchanged up to `1+O(1/y)`. O3 Thm 1.1 and Lemma 1.3 accept
arbitrary forbidden sets, so nothing else changes. (`e_ℓ≤k`, since
`ℓ^{k+1}>y^{k+1}>T`.)
With saturated hubs, the reduction mod `q′:=∏ℓ^{v_ℓ(M)}` of a non-hub O
has all heights `>H` mod `q′`: a hub congruence mod `q′` reduces to one mod
each `ℓ^{v_ℓ}`. The proofs below use only that Q is odd, so they apply
with `Q=q′`. Here `v_ℓ(M)≤e_ℓ`, and a hub congruence mod `q′` reduces
to one mod every `ℓ^{v_ℓ}`, which saturation forbids (review O13r-D2).

**Lemma 2.0′ (prime-power events; PROVED, review O13r-D1).** Group the
events containing O by their exponent pattern `(v_ℓ)_{ℓ∈O}`,
`v_ℓ=v_ℓ(M)≥1`. Then:

* Since `ℓ>y=2T^{1/(k+1)}` and `∏ℓ^{v_ℓ}≤T`, we have `Σv_ℓ≤k`, so there
  are at most `binom(k,|O|)≤2^k` patterns.
* For a fixed pattern, an event contains the lifted vertex `(ℓ,x_ℓ)` iff
  its class mod `ℓ^{v_ℓ}` is `x_ℓ mod ℓ^{v_ℓ}` (O2 §10.3; exactly one lift
  qualifies, and `v_ℓ≤e_ℓ`). So these events lie in the system `(q′,κ′)`,
  `q′=∏ℓ^{v_ℓ}`, with κ′ fixed by O.
* Their weight beyond O is `1/φ(n′)≤2/n′`, with `n′=M/(q′m)≥y`, because e
  strictly contains O and so has a free prime outside O.
* Theorem 2.3 needs only Q odd and `Q>y²`, so it applies with `Q=q′`, and
  `q′` has heights `>H` by the previous paragraph.

So every bound below that is stated for squarefree q holds for `Δ_O` at a
cost of a factor `2^k`. That factor is absorbed by HC*'s `e^{Ck}`; in O4
Thm 4.2 it adds `O(k/a)` to `log H`.

**Lemma 2.1 (ray sum).** Let `(u,v)` be a primitive positive vector with
`u≡Kv (Q)`, `gcd(uv,Q)=1`, `h=uv`. The atoms on the ray,
`(s,tu,tv)` with s squarefree, contribute to `Δ¹(Q,K)` at most
`1/y + 𝓛/(4h)`.

*Proof.* `M+1=4hst²`, and `M` determines `st²`, hence `(s,t)` (Lemma 1.1).
`M≡−1 (4h)` and `Q|M` put `n=M/Q` in the single class `−Q^{−1} mod 4h`
(`gcd(Q,4h)=1`). Distinct atoms give distinct n, and
`Σ_{y≤n≤X, n≡n_0 (d)}1/n ≤ 1/y+d^{−1}log(X/y)`. ∎

**Lemma 2.2 (lattice points in a thin box).** Let
`Λ:={(a,b): a≡Kb (Q)}` (index Q), `A,B≥1`, `A,B<Q`, `F′≥1` with `AB<F′Q`,
and `R:=[A,2A)×[B,2B)`. Then the points of `Λ*:={(a,b)∈Λ: gcd(ab,Q)=1}`
in R lie on at most `2F′+1` rays through 0 (each with primitive direction
`(u,v)∈Λ`), plus a set E with `|E| ≤ (2F′+1)(4F′+1)`.

*Proof.* Cut R along the a-axis into `k:=⌊2AB/Q⌋+1 ≤ 2F′+1` boxes of
width `A′=A/k`, so `A′B<Q/2`. Three lattice points of one sub-box have
`det(P_1−P_0,P_2−P_0)∈Qℤ` and `|det|<2A′B<Q`, so they are collinear:
the sub-box's points lie on one line L. Let `δ` be the shortest vector of
Λ along L.
* L through 0: the points are `t(u,v)` with `(u,v)` primitive positive;
  `(u,v)∈Λ` because t is a unit mod Q. One ray per sub-box.
* `δ=(u′,v′)`, `u′,v′>0`, `0∉L`: every point of Λ has
  `v′a−u′b≡0 (Q)`, so on L, `v′a−u′b=J∈Qℤ∖{0}`. On R,
  `|v′a−u′b|<2max(v′A,u′B)`, so `max(v′A,u′B)>Q/2`, and L∩R has at most
  `min(A/u′,B/v′)+1 = AB/max(v′A,u′B)+1 < 2F′+1` points.
* `δ=(u′,−v′)`, `u′,v′>0`: every point has `v′a+u′b≡0 (Q)`, and
  `0<v′a+u′b<2(v′A+u′B)` on R, so `max(v′A,u′B)>Q/4`; at most `4F′+1` points.
* δ on an axis: `(0,v′)∈Λ` forces `Q|v′`, so `v′≥Q>B`; `(u′,0)∈Λ`
  forces `Q|u′`, so `u′≥Q>A′`. Either way at most one point. ∎

**Theorem 2.3 (PROVED).** For odd Q with `Q>y²` and `Ĥ≥4^{ω(Q)}`,

```
Δ¹(Q,K) ≤ C·𝓛⁴·4^{ω(Q)/3}·Ĥ^{−1/3}     (C absolute).
```

Hence, for every vertex set O with no saturated H-hub vertex and
`4^k≤H≤y`, the `m=1` part of `Δ_O` is `≤ 2^{k+1}C𝓛⁴4^{k/3}H^{−1/3}`
(Lemma 2.0′ for the prime-power patterns): **HC*(1/3,4)
holds for the m=1 part** (Cor 4.1 for HC*).

*Proof.* Dyadic boxes `[S,2S)×[A,2A)×[B,2B)` (powers of 2, `SAB≤T`):
at most `8𝓛³` of them. A point has `1/n ≤ Q/(2SAB)`, and a nonempty box
has `SAB>Qy/32`, `AB>h_3/4`, `SA>h_1/4`, `SB>h_2/4`. Let N be the number
of points in a box. Square roots: `x²≡r (Q)`, r a unit, has `≤2^{ω(Q)}`
solutions (Q odd).

* (a) `A,B≥Q`. For each s, b lies in `≤2^ω` classes and a in one class:
  `N ≤ 2S·2^{ω+1}(B/Q)·2A/Q`, contribution `≤2^{ω+2}/Q`.
* (b) `A<Q≤B`. (C1): `4sa²≡K (Q)` (as `a²≡K·ab`), and `(s,a)↦4sa²<32SA²`
  is injective (s squarefree), so Lemma 1.1 gives `≤32SA²/Q+1` pairs, each
  with `≤2B/Q` values of b: contribution `≤32A/Q+1/(SA) ≤ 32A/Q+4/h_1`.
  (C3): per s, `≤2^ω·2B/Q` values of b and `≤1` of a: contribution
  `≤2^{ω+1}/A`. Together `≤4/h_1+2^{ω/2+3}Q^{−1/2}`.
* (c) `B<Q≤A`: the same with a↔b, `h_2`, (C2): `4Ksb²≡1`.
* (d) `A,B<Q`. Each class mod Q meets `[A,2A)` and `[B,2B)` at most once.
  If `AB≥F′Q` with `F′:=2^ωF`: (C3) gives `N≤2^{ω+1}S`, contribution
  `≤2^ωQ/(AB)≤1/F`. If `AB<F′Q`: Lemma 2.2. The set E contributes
  `|E|(S/Q+1)Q/(2SAB) ≤ |E|(2/h_3+16/y)`. Each of the `≤2F′+1` rays
  contributes at most its whole ray sum, `≤1/y+𝓛/(4h_3)` (Lemma 2.1).

Summing (`Q^{−1/2}<1/y`, `Ĥ≤y`):
`Δ¹ ≤ 8𝓛³[1/F + 15F′²·18/Ĥ + 3F′(1+𝓛)/Ĥ + 50·2^{ω/2}/Ĥ]`.
Take `F:=(Ĥ/4^ω)^{1/3}≥1`; then `1/F = F′²/Ĥ = 4^{ω/3}Ĥ^{−1/3}`. ∎

*Remark.* The proof uses no exponential sums. The three ingredients are
the squarefree lifting (Lemma 1.1, applied to the planes (C1), (C2) and to
rays), the square-root count (C3), and the thin-box geometry (Lemma 2.2).
Literal HC is false (Def 2.0). What remains for HC* is the Π-part m
(O4 gap (iii)); see §3.

## 3. The Π-part m (O4 gap (iii))

**Lemma 3.1 (m-systems; PROVED).** Let P=(s,a,b) be an atom containing O,
with Π-part m and ray `(u,v)=(a,b)/t`, `t=gcd(a,b)`. Then

1. `m | u+v` (and `m | 4sa²+1`, `m | 4sb²+1`);
2. with `κ_m:=` the CRT class `≡κ (q)`, `≡−1 (m)`, P satisfies
   `a≡κ_m b (qm)` and `qm | M`; conversely these imply `m|4sa²+1`;
3. writing `4sa²+1=m·m*`, one has `b=jm−a` for an integer j and
   `M = m·(4saj−m*)`, so `qn′ = 4saj−m*`.

*Proof.* (1) O3 Lemma 2.1(2): `m|gcd(M,4D+1)|a+b=t(u+v)`, and
`gcd(m,t)=1` since `t|M+1`. Mod m, `b≡−a`, so `4sb²≡4sa²≡−1`.
(2) `a≡−b (m)` and `4sab≡1 (m)` give `4sa²≡−1`. (3)
`M=4sa(jm−a)−1=4saj·m−(4sa²+1)`. ∎

So the m-part of `Δ_O` is `≤2Σ_{m>1}Δ¹(qm,κ_m)` (sum over Π-numbers m
prime to 2q, `m≤T/(qy)`; each atom is counted in the system of its own
m with weight `2/n′`). In the system `(qm,κ_m)` every point has
`a+b≥m`, so `h_3(qm,κ_m)≥m−1` and `h_1,h_2≥((m−1)/4)^{1/2}`.

**Proposition 3.2 (small m; PROVED).** The atoms with `m≤μ` contribute at
most `2μ·Δ¹(q,κ) ≤ 2Cμ𝓛⁴4^{k/3}Ĥ^{−1/3}` to `Δ_O`. With `μ=Ĥ^{1/6}`: the
part of `Δ_O` from events with `m≤Ĥ^{1/6}` is `≪2^k𝓛⁴4^{k/3}Ĥ^{−1/6}`; in
general `μ=Ĥ^{1/3−a}` gives `≪2^k𝓛⁴4^{k/3}Ĥ^{−a}`
(the factor `2^k` comes from the prime-power patterns, Lemma 2.0′).

*Proof.* `2/n′=2m/n≤2μ/n`, and `n=mn′≥y`, so the atom is a term of
`Δ¹(q,κ)`. Theorem 2.3. ∎

**Lemma 3.3 (ray sums with m; PROVED).** For a ray `(u,v)` as in Lemma 2.1
(modulus q), the atoms on the ray, all m included, contribute to `Δ_O` at most

```
min{ 2𝓛(1/u+1/v) + 4/y ,  τ(u+v)·(2/y + 𝓛/(2h)) ,  (T/(4hq)+1)·2/y }.
```

*Proof.* Atoms on the ray ↔ M (Lemma 2.1), `M≡−1 (4h)`, `q|M`, and M
determines `(m,n′)`. (i) For `n′∈[Y,2Y)`, `M<2qY(u+v)` (Lemma 3.1(1)), so
there are `≤Y(u+v)/(2h)+1` such M, each of weight `≤2/Y`; sum over dyadic
`Y≥y`. (ii) For fixed `m|u+v`, `n′` lies in one class mod 4h
(`gcd(qm,4h)=1` since `gcd(u+v,uv)=1`); Lemma 2.1's sum. (iii) At most
`T/(4hq)+1` values of M, each of weight `≤2/y`. ∎

*Per-ray* bound (i) is HC-shaped for balanced rays (`min(u,v)≥H^{1/3}`).
Bound (ii) is HC-shaped when `τ(u+v)≤min(y,h)·H^{−1/3}`, which follows from
`τ(u+v)≤H^{2/3}` since `h>H` (review O13r-D5; the earlier threshold
`y^{2/3}` was wrong, since `τ/h` can then be `y^{1/6}`). These bound
single rays only. HC_Π sums over all rays and off-ray points of all
m-systems, and no count of rays across the m-systems is given. So no class
of rays is "done" for HC_Π.

**Hubs reappear at large m (Assessment, with a PROVED identity).** By
Lemma 3.1(3), the extreme case `m=4sa²+1` (all of `4sa²+1` in the Π-part)
gives `M=(4sa²+1)(4saj−1)`, `qn′=4saj−1`, and the j with `q|4saj−1` form
one class mod q, so for that `(s,a)` the atoms contribute
`≤2/y+𝓛/(2sa)`. These are exactly the (F1) hub family of O3 Prop 2.2
(`κ≡4sa²`), and non-hub means `sa>H`. So the *pointwise* worst cases at
large m are hub-type, and the m-refinement is a structured, not a
Weil-range, problem. A complete treatment is §4.

## 4. What remains: the large-m part (precise residual)

Split `Δ_O = Δ_O^{≤μ} + Δ_O^{>μ}` by the Π-part m of the event's atom
(an event is charged to one of its atoms). Prop 3.2 handles `Δ_O^{≤μ}`.

**Hypothesis HC_Π(a′,B′)** (open; `0<a′<1/3`). For all large T, all k,
`4^k≤H≤y`, and every vertex set O with no *saturated* H-hub (Def 2.0), the
atoms with `m>Ĥ^{1/3−a′}` give `Δ_O^{>Ĥ^{1/3−a′}} ≤ e^{Ck}𝓛^{B′}H^{−a′}`.
(Threshold changed from `Ĥ^{1/6}` after review R2-D1: Prop 3.2 holds for
every μ. By §7 (Prop 7.1), HC_Π reduces further to its first terms
`P_0` with `m>Ĥ^{1/3−a′}`; that reduction costs `a≤1/4`.)

**Hypothesis HC*(a,B)** (the form O4 Thm 4.2 actually uses). As HC, but
with saturated hubs (Def 2.0), only for `4^{k}≤H≤y`, and with the bound
`Δ_O ≤ e^{Ck}𝓛^BH^{−a}` (C absolute).

**Corollary 4.1 (PROVED implication).** (i) HC_Π(a′,B′) (saturated hubs,
`4^k≤H≤y`) implies HC*(a′, max(B′,4)+1). The first-term form (P_0 with
`m>Ĥ^{1/3−a′}` bounded by `e^{Ck}𝓛^{B′}H^{−a′}`) implies
HC*(min(a′,1/4), max(B′,5)+1), using Prop 7.1. (ii) O4 Thm 4.2 holds with
HC* in place of HC: its step 3 chooses one H with
`H^a ≥ 𝓛^Be^{0.011k}/η_k`. The factor `e^{Ck}` adds `O(k/a)` to `log H`,
which is negligible against `log(1/η_k)≍k²`. The resulting
`H=y^{1/2+o(1)}` satisfies `4^k≤H≤y` and the saturated-hub cost condition of
Def 2.0. Hence, modulo Thorner–Zaman and Elsholtz–Tao Prop 1.4, HC_Π implies
`log W(p) ≥ 0.2·a′^{1/2}(log₂p)^{3/2}` for infinitely many Mordell-hard p
(and the first-term form gives `0.2·min(a′,1/4)^{1/2}`). Literal HC is false (Def 2.0). It also
quantifies over all `H≥2` without the `e^{Ck}` factor. With O4's
(unsaturated) hubs, HC_Π is false as well: lifts of the class −4 (F1,
`s=a=1`) carry the atoms `(1,1,b)`, `5|4b−1`, with `m=5` and constant
codegree (review O13r-D4).

*Proof.* (i) Theorem 2.3, Prop 3.2 with `μ=Ĥ^{1/3−a′}`, and `Ĥ≥H` for
`H≤y`. (ii) As stated: re-run O4 Thm 4.2 steps 2–5 with the factor
`e^{Ck}` and the condition `300(k+1)H(1+log H)<y`. ∎

**Anatomy of HC_Π (Assessment).** By Lemma 3.1 an atom with Π-part m
satisfies `m | u+v` and `m | 4sa²+1`. So HC_Π is a statement about
*divisors* of `u+v` and of `4sa²+1`, not about residues of inverses:

1. *Rays.* Lemma 3.3 bounds single rays: balanced rays, and rays with
   `τ(u+v)≤H^{2/3}`. Neither is "done" for HC_Π, because rays across the
   m-systems are not counted. The per-ray residue is the unbalanced rays
   with `τ(u+v)>H^{2/3}`; these force `u+v ≥ H^{c·log log H}`.
   For them HC_Π asks for
   ```
   (DIV)  #{m | u+v Π-number : the least n′≥y with qmn′≡−1 (4h) is ≤ Y} ≪ 𝓛^B H^{−a}·Y   (Y≥y).
   ```
   For `u=1` this is: small values of `ρ·m′ mod v` over the divisors
   `m′=(v+1)/m` (since `m^{−1}≡m′ (mod v)`), with `n′` rough and m smooth.
2. *Other points.* For a pair `(s,a)` with `4sa²≡κ (q)`, each `m|4sa²+1`
   gives one class of b mod qm, and the atoms contribute
   `≤2/n′_0(s,a,m) + 𝓛/(2sa)` (Lemma 3.1(3); n′ runs over a progression
   of difference 4sa; the term `𝓛/(2sa)` only when `m≤T/(4qsa)`, while the
   first-term `2/n′_0` occurs for every `m≤T/(qy)`). Summing over m costs
   the restricted divisor counts `τ_Π(4sa²+1; ≤T/(4qsa))` (period terms)
   and `τ_Π(4sa²+1; ≤T/(qy))` (first terms). Pointwise, τ is `T^{O(1/log𝓛)}`. In O4
   Thm 4.2, `H^{−a}=exp(−c𝓛^{2/3})`, so a pointwise divisor bound is fatal.
   What is needed is an *average* of `τ_Π(4sa²+1)` over the
   `(s,a)` in a box with `4sa²≡κ (q)`. When one of the ranges of s or a
   exceeds `q^{1+ε}`, a Shiu / Nair–Tenenbaum / Henriot bound would give a
   polylog average, once the dependence of the constants on `α,β` has been
   checked; I have not done this. When the ranges are shorter than q,
   no averaging theorem applies. Then only the pointwise
   `τ≤(sa)^{O(1/log log sa)}` is available. It suffices when
   `sa≤q^{O(1)}` and the count carries a factor `1/q`, but not in the core boxes.

So the obstruction has moved. It is no longer "inverses of squares
beyond the Weil range" (dissolved, §1–2). It is now a divisor-function
problem in short progressions, (DIV) plus the `τ_Π(4sa²+1)` averages.
The worst cases are again hub-like (§3, last paragraph).

**EVIDENCE (`scripts/omega5_codeg.py`, exact, one pair per T, Π=Π_0).**
The table gives the maximum of Δ over classes with hub level `>X` (O3
Def 2.3, enumerated to level HCAP=1024 for T=10⁹ and 2048 otherwise), split into m=1 and m>1.
The two parts are maximised independently, not at the class that maximises the total.
These are joint classes mod q, not lifted vertices (cf. Def 2.0):

| T | q | X=16: m=1 / m>1 | X=128 | X=512 | `X^{−1/3}` at 512 |
|---|---|---|---|---|---|
| 10⁹ | 337·347 | .020 / .017 | .0049 / .0089 | .0036 / .0067 | .125 |
| 10¹¹ | 937·941 | .022 / .041 | .0051 / .0101 | .0025 / .0035 | .125 |
| 10¹⁰ | 337·30011 | .0073 / 0 | .0032 / 0 | .0032 / 0 | .125 |

The m>1 part is **not** negligible: for the near-y pairs it is comparable
to the m=1 part and exceeds it at most levels. Over `X=16…512` its endpoint
decay exponent is ≈0.27 (T=10⁹) and ≈0.71 (T=10¹¹). Both are inside
`X^{−1/3}`. For the wide pair the m>1 column is **vacuous** for a structural
reason: `T/q≈989`, `n′>y=331`, and m odd `>1` gives `mn′≥993>T/q`. This is consistent with HC_Π but proves nothing.

## 5. The literature (survey; details and archived PDFs in `sources/lit2026/O13_LITERATURE_NOTES.md`)

O4's problem IS counts all `t≤t_0≤q^{1/2}` with `w t̄² mod q ≤ Y≤q^{1/2}`,
for every w. Statements below were checked against the archived PDFs.

* **Cilleruelo–Garaev** (arXiv:1007.1526, Thm 1): for prime p,
  `#{xy≡λ (p) : x∈[K,K+M], y∈[L,L+M]} < M^{4/3+o(1)}p^{−1/3}+M^{o(1)}`,
  uniformly in the shifts. It needs a prime modulus and covers `xy` only.
  Their proof idea (Heath-Brown: lift to integers, divisor bound) is
  exactly the lifting used here, and at the origin it gives the stronger
  `(Yt_0²/q+1)·max_n#{t:t²|n}` for any q.
* **Bourgain–Garaev** (arXiv:1211.4184, prime p; arXiv:1309.1124, any
  modulus, Thm 1): additive energies of reciprocals,
  `J_{2k} < (2k)^{90k³}(log N)^{4k²}(N^{2k−1}/m+1)N^k`. These give incomplete
  Kloosterman bounds below `m^{1/2}` (via energies). Neither paper states a
  short-box occupancy bound, and no all-w bound for IS follows directly.
* **Shparlinski's survey** (arXiv:1103.2879, Thm 13): the modular-hyperbola
  asymptotic with error `m^{1/2+o(1)}`. The survey notes this is trivial for
  `XY<m^{3/2}`, which is exactly IS's range.
* **Shparlinski** (arXiv:1004.0715, Thm 1): a mean square over residues c
  for `m²−n²≡c` in short ranges. This is an averaged statement only.
* **Korolev / Karatsuba** (short Kloosterman sums of length `q^ε`). These
  need special moduli (smooth, or prime powers) or carry log-power savings.
  They give no pointwise IS bound for products of ≤k large primes.
  These papers are not archived, and their statements were not checked
  against PDFs.

**Verdict on IS as posed in O4.** No known theorem gives
`N(q,w)≪𝓛^BYh^{−a}` for every w in O4's range. The lifting bound gives
`N(q,w) ≤ (Y/(4h)+1)·min(max_{n≤Yt_0²}#{t: t²|n}, √Y)`. (All s with
`st²=n`, `s≤Y`, share one squarefree kernel f, so there are at most
`(Y/f)^{1/2}` of them.) This is a factor `≤min(T^{O(1/log𝓛)},√Y)` short of
the target, pointwise. But HC never needed IS: it needs the squarefree
count, and that is exact (Lemma 1.1). Averaging over w or q (route (α))
is therefore unnecessary for the core.

## 6. Status

* **PROVED:** Lemma 1.1, Cor 1.2, Lemma 2.0′, Lemmas 2.1–2.2, Theorem 2.3
  (HC* with a=1/3 for the m=1 part), Lemma 3.1, Prop 3.2 (HC* with exponent a
  for `m≤Ĥ^{1/3−a}`), Prop 7.1 (period part, a=1/4), Lemma 3.3, Cor 4.1 (HC_Π ⇒ HC* ⇒ O4 Thm 4.2 rate),
  and the counterexample to literal HC (Def 2.0).
* **Open:** HC_Π, i.e. the large-m part. HC*(a,B) is therefore still
  not proved unconditionally, and the proved rate remains O4 Cor 3.1.
* **Scope.** Prime-power events (`ℓ^2|M`) are covered by Lemma 2.0′, at a
  cost of a factor `2^k`. The height transfer to `q′` is immediate with
  saturated hubs (Def 2.0). O4 Prop 7.2's period/boundary
  terms are subsumed by Theorem 2.3's cases (a)–(c).

## Replay

```
export PYTHONPATH=scripts
uv run --with sympy python scripts/omega5_codeg.py 1000000000 331 337 347 1024        # ~2 s
uv run --with sympy python scripts/omega5_codeg.py 10000000000 331 337 30011 2048     # seconds
uv run --with sympy python scripts/omega5_codeg.py 100000000000 933 937 941 2048      # minutes
```
Outputs: `data/omega5/codeg_*.txt`.

## 7. HC_Π, round 2: the (a,b)-parametrisation; the period part is done

Round 1 (§4) parametrised large-m atoms by `(s,a)` and met
`τ_Π(4sa²+1)`, a divisor function of a *quadratic* polynomial in short
progressions (the Henriot / Nair–Tenenbaum territory). Fixing `(a,b)`
instead puts the divisor function on the **linear** form `a+b`, where
elementary divisor switching suffices.

**Lemma 7.0 (fibres over (a,b,m); PROVED).** Fix `(a,b)∈Λ*` (Lemma 2.2's
notation, modulus q) and a Π-number `m | a+b` with `gcd(m,2abq)=1`.
The atoms `(s,a,b)` of Π-part m have s in one class mod qm, and their
values `n′=M/(qm)` run through the progression `n′≡−(qm)^{−1} (mod 4ab)`,
`y≤n′≤T/(qm)`. Hence their total weight is at most

```
2/ν(a,b,m) + 𝓛/(2ab),     ν(a,b,m) := least n′≥y with qmn′≡−1 (mod 4ab).
```

*Proof.* `qm | 4sab−1` fixes s mod qm. `M=qmn′≡−1 (mod 4ab)`. Consecutive
admissible s change n′ by `4ab`, and `Σ_{i≥0}1/(ν+4ab·i) ≤ 1/ν+(4ab)^{−1}log(T/(qmy))`. ∎

By Lemma 3.1(1), every atom of Π-part m has `m | a+b`. Hence

```
Δ_O^{>μ} ≤ P_0 + (𝓛/2)·P_1,
P_1 := Σ_{(a,b)∈Λ*, ab≤T} τ(a+b)/(ab),
P_0 := Σ_{(a,b)∈Λ*} Σ_{m|a+b, m>μ} 2/ν(a,b,m)     (first terms).
```

**Proposition 7.1 (the period part; PROVED, explicit).** With
`τ*(x):=max_{n≤x}τ(n)`,

```
P_1 ≤ 4𝓛²·[ 2τ(q)(2+𝓛)/q + τ*(12q²)/q + 6·h_3^{−1/4} ].
```

In particular `(𝓛/2)P_1 ≤ 2^{k+O(1)}𝓛⁴(q^{−1+o(1)} + H^{−1/4})` for a
vertex set O without saturated H-hubs. By Nicolas–Robin,
`log τ*(x) ≤ 1.538·log2·log x/log log x`, so `τ*(12q²)/q=q^{−1+o(1)}`
explicitly. Since `q>y²≥H²`, `q^{−1+o(1)}≤H^{−2+o(1)}`, and the period part
satisfies HC* with `a=1/4`.

*Proof.* Use dyadic boxes `R=[A,2A)×[B,2B)`. Since `a,b≤T`, there are at
most `4𝓛²` of them. Put `X:=max(A,B)`. Each b fixes a mod q, so R holds
`≤B(A/q+1)` points; by symmetry, `N_R≤AB/q+min(A,B)`. Each point weighs
`≤τ(a+b)/(AB)`, and `a+b<4X`. A nonempty box has `AB>h_3/4`, so `X>h_3^{1/2}/2`.
* `X≤3q²`: the box weighs
  `≤τ*(4X)(AB/q+min(A,B))/(AB) ≤ τ*(12q²)/q + τ*(4X)/X`. Also
  `τ(n)≤2√n` gives `τ*(4X)/X≤4X^{−1/2}≤6h_3^{−1/4}`.
* `X>3q²`, say `X=B`: for each a, `n=a+b` runs over one class mod q, a
  stretch of length B. Using `τ(n)≤2#{d|n: d≤√n}` and `√n<2√B`, and
  splitting by `g=gcd(d,q)`:
  `Σ_bτ(a+b) ≤ 2Σ_{d≤2√B}(Bg/(qd)+1) ≤ 2(B/q)·τ(q)(1+𝓛)+4√B`.
  With `B>3q²`, `4√B<2.4B/q`, so the box weighs `≤2τ(q)(2+𝓛)/q`.
  Here `τ(q)=2^{ω(q)}` for squarefree q, and `τ(q′)≤2^{Σv_ℓ}≤2^k` for the
  prime-power moduli of Lemma 2.0′ (review R2-D3). The case
  `X=A` is symmetric. ∎

*Remark.* No Shiu / Nair–Tenenbaum / Henriot input is needed for the
period part. Those theorems require progressions longer than
`modulus^{1+ε}`, plus α-dependent constants. Here the long variable is
summed elementarily once it exceeds `3q²`, and below that the pointwise
`τ*(12q²)` is absorbed by the factor `1/q`. The τ-weights on rays,
`τ(t(u+v))/(t²h)`, are harmless because their weight decays in `h`.

**What is left: the first terms P_0 (open).** We have
`P_0 = Σ_{(a,b)∈Λ*} Σ_{m|a+b, m>μ} 2/ν(a,b,m)`. For fixed `(a,b)`, the
classes `−(qm)^{−1} mod 4ab` are distinct for distinct `m|a+b`
(`m≤a+b<4ab`), so

```
Σ_m 2/ν(a,b,m) ≤ min( 2τ(a+b)/y·(1+o(1)) ,  2𝓛(1/a+1/b) + 4/y ),
```

(the second by Lemma 3.3(i)'s lifting at the point). Neither is summable
over the whole lattice. One needs to use `ν≤T/(qm)` (existence) and
`s≥1`, i.e. a count of *first atoms*. Each such atom has
`s<qm(1+y/(4ab))`, so P_0 is a sum over the m-system cores
`{s<2qm}` (for `4ab≥y`), summed over m. Partial results:

* `m≤Ĥ^{1/3−a}`: PROVED for the whole mass, not only first terms, by
  Prop 3.2 with `μ=Ĥ^{1/3−a}`, giving `≪2^k4^{k/3}𝓛⁴H^{−a}` (review R2-D1).
  This supersedes the per-m thin-box sketch of the previous version.
* `m>Ĥ^{1/3−a}`: no argument. Per m, the cores contribute up to `O(1/y)`.
  The sum over the up to `T/(qy)` values of m needs the number of
  first atoms with `n′∈[Y,2Y)` and `m>H^{1/3}` to be `≪𝓛^BH^{−a}Y`,
  summed over all m. The unbalanced rays of (DIV) are the sub-case
  `(a,b)=t(u,v)`.

**Status of HC_Π after round 2.** The period part is PROVED (a=1/4),
all atoms with `m≤H^{1/3−a}` are PROVED (Prop 3.2), and the first terms
`P_0` with `m>H^{1/3−a}` are open. The open piece is a pure core-counting problem for the moduli
`qm`, `m` Π-smooth, averaged over m with weight 1. It is no longer a
divisor-sum problem.
