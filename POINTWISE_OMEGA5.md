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
`#{t: t²|n}`, which can be `T^{c/log𝓛}`. The over-counted problem is
genuinely beyond Weil (and is what the literature in §5 addresses);
the atom count is elementary.

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
If no vertex of O is an H-hub (O3 Def 2.3), then `h_1,h_2,h_3>H` for
`(q,κ)`: `c≡−u/v ⇔ u≡κv`, `c≡−4sa² ⇔ 4sa²≡κ`,
`c≡−1/(4sb²) ⇔ 4κsb²≡1`, and a congruence mod q holds mod every `ℓ|q`.

**Lemma 2.1 (ray sum).** Let `(u,v)` be a primitive positive vector with
`u≡Kv (Q)`, `gcd(uv,Q)=1`, `h=uv`. The atoms on the ray,
`(s,tu,tv)` with s squarefree, contribute to `Δ¹(Q,K)` at most
`1/y + 𝓛/(4h)`.

*Proof.* `M+1=4hst²`, and `M` determines `st²`, hence `(s,t)` (Lemma 1.1).
`M≡−1 (4h)` and `Q|M` put `n=M/Q` in the single class `−Q^{−1} mod 4h`
(`gcd(Q,4h)=1`). Distinct atoms give distinct n, and
`Σ_{y≤n≤X, n≡n_0 (d)}1/n ≤ 1/y+d^{−1}log(X/y)`. ∎

**Lemma 2.2 (lattice points in a thin box).** Let
`Λ:={(a,b): a≡Kb (Q)}` (index Q), `A,B≥1`, `A<Q`, `F′≥1` with `AB<F′Q`,
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
* δ on an axis: `(0,v′)∈Λ` forces `Q|v′`, `(u′,0)∈Λ` forces `Q|u′`;
  since `A′<Q` and `B<Q`... (for `(0,v′)`: `v′≥Q>B`), at most one point. ∎

**Theorem 2.3 (PROVED).** For odd Q with `Q>y²` and `Ĥ≥4^{ω(Q)}`,

```
Δ¹(Q,K) ≤ C·𝓛⁴·4^{ω(Q)/3}·Ĥ^{−1/3}     (C absolute).
```

Hence, for every vertex set O with no H-hub vertex (and `H≤y`), the
`m=1` part of `Δ_O` is `≤ 2C𝓛⁴4^{k/3}H^{−1/3}`: **HC(1/3, 4) holds for the
m=1 part**, with the harmless factor `e^{O(k)}`.

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
What remains for full HC is the Π-part m (O4 gap (iii)); see §3.
