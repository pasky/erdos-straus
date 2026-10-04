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
part of `Δ_O` from events with `m≤Ĥ^{1/6}` is `≪𝓛⁴4^{k/3}Ĥ^{−1/6}`.

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

Bound (i) is HC-shaped for *balanced* rays (`min(u,v)≥H^{1/3}`), and (ii)
for rays with `τ(u+v)≤y^{2/3}`. Neither covers an unbalanced ray
`(u,v)`, `u<H^{1/3}`, with `τ(u+v)>y^{2/3}` and `h<T/(qy^{1/3})`.

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

**Hypothesis HC_Π(a′,B′)** (open). For all large T, all k, H as in HC
and every vertex set O with no H-hub, the atoms with `m>Ĥ^{1/6}` give
`Δ_O^{>Ĥ^{1/6}} ≤ 𝓛^{B′}H^{−a′}`.

**Corollary 4.1 (PROVED implication).** HC_Π(a′,B′) implies
HC(min(a′,1/6), max(B′,4)+1) (with the `e^{O(k)}` factor `4^{k/3}`, harmless
in O4 Thm 4.2). Hence, modulo Thorner–Zaman and Elsholtz–Tao Prop 1.4,
HC_Π implies `log W(p) ≥ 0.2·min(a′,1/6)^{1/2}(log₂p)^{3/2}` for
infinitely many Mordell-hard p (O4 Thm 4.2; `0.2/√6 > 0.08`).

*Proof.* Theorem 2.3, Prop 3.2 with `μ=Ĥ^{1/6}`, and `Ĥ≥H` when
`H≤y` (true in O4 Thm 4.2, where `H=y^{1/2+o(1)}`). ∎

**Anatomy of HC_Π (Assessment).** By Lemma 3.1 an atom with Π-part m
satisfies `m | u+v` and `m | 4sa²+1`. So HC_Π is a statement about
*divisors* of `u+v` and of `4sa²+1`, not about residues of inverses:

1. *Rays.* Balanced rays (`min(u,v)≥H^{1/3}`) and rays with
   `τ(u+v)≤y^{2/3}` are done (Lemma 3.3). The rest are unbalanced rays
   with `τ(u+v)>y^{2/3}`; these force `u+v ≥ y^{c·log log y}`.
   For them HC_Π asks for
   ```
   (DIV)  #{m | u+v Π-number : the least n′≥y with qmn′≡−1 (4h) is ≤ Y} ≪ 𝓛^B H^{−a}·Y   (Y≥y).
   ```
   For `u=1` this is: small values of `ρ·m′ mod v` over the divisors
   `m′=(v+1)/m` (since `m^{−1}≡m′ (mod v)`), with `n′` rough and m smooth.
2. *Other points.* For a pair `(s,a)` with `4sa²≡κ (q)`, each `m|4sa²+1`
   gives one class of b mod qm, and the atoms contribute
   `≤2/n′_0(s,a,m) + 𝓛/(2sa)` (Lemma 3.1(3); n′ runs over a progression
   of difference 4sa). Summing over m costs the restricted divisor count
   `τ_Π(4sa²+1; ≤T/(4qsa))`. Pointwise, τ is `T^{O(1/log𝓛)}`. In O4
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
Def 2.3, enumerated to level 2048), split into m=1 and m>1:

| T | q | X=16: m=1 / m>1 | X=128 | X=512 | `X^{−1/3}` at 512 |
|---|---|---|---|---|---|
| 10⁹ | 337·347 | .020 / .017 | .0049 / .0089 | .0036 / .0067 | .125 |
| 10¹¹ | 937·941 | .022 / .041 | .0051 / .0101 | .0025 / .0035 | .125 |
| 10¹⁰ | 337·30011 | .0073 / 0 | .0032 / 0 | .0032 / 0 | .125 |

The m>1 part is **not** negligible: for the near-y pairs it exceeds the
m=1 part at every level shown. It decays roughly like `X^{−0.8}`, well inside
`X^{−1/3}`. For the wide pair (`T/q≈10³`), `m n′≤T/q` leaves essentially
no room for `m>1`. This is consistent with HC_Π but proves nothing.

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
  `J_{2k} < (2k)^{90k}(log N)^{4k}(N^{2k−1}/m+1)N^k`. These give incomplete
  Kloosterman bounds below `m^{1/2}`, but only with savings that are small
  powers of log or tiny powers of N. They yield no all-w bound for IS.
* **Shparlinski's survey** (arXiv:1103.2879, Thm 13): the modular-hyperbola
  asymptotic with error `m^{1/2+o(1)}`. The survey notes this is trivial for
  `XY<m^{3/2}`, which is exactly IS's range.
* **Heath-Brown** (arXiv:1004.0715, Thm 1): a mean square over residues c
  for `m²−n²≡c` in short ranges. This is an averaged statement only.
* **Korolev / Karatsuba** (short Kloosterman sums of length `q^ε`). These
  need special moduli (smooth, or prime powers) or carry log-power savings.
  They give no pointwise IS bound for products of ≤k large primes (not
  archived: no arXiv versions found by the survey).

**Verdict on IS as posed in O4.** No known theorem gives
`N(q,w)≪𝓛^BYh^{−a}` for every w in O4's range. The lifting bound gives
`N(q,w) ≤ (Y/(4h)+1)·min(max_{n≤Yt_0²}#{t: t²|n}, √Y)`. (All s with
`st²=n`, `s≤Y`, share one squarefree kernel f, so there are at most
`(Y/f)^{1/2}` of them.) This is a factor `≤min(T^{O(1/log𝓛)},√Y)` short of
the target, pointwise. But HC never needed IS: it needs the squarefree
count, and that is exact (Lemma 1.1). Averaging over w or q (route (α))
is therefore unnecessary for the core.

## 6. Status

* **PROVED:** Lemma 1.1, Cor 1.2, Lemmas 2.1–2.2, Theorem 2.3
  (HC with a=1/3 for the m=1 part), Lemma 3.1, Prop 3.2 (HC with a=1/6
  for `m≤Ĥ^{1/6}`), Lemma 3.3, Cor 4.1 (HC_Π ⇒ HC ⇒ O4 Thm 4.2 rate).
* **Open:** HC_Π, i.e. the large-m part. HC(a,B) is therefore still
  not proved unconditionally, and the proved rate remains O4 Cor 3.1.
* **Scope caveats.** q is taken squarefree, as in O4 §7. Free primes
  `ℓ≤√T` have vertex classes mod `ℓ^{e_ℓ}`, and events with `ℓ^2|M` see
  `q′=∏ℓ^{v_ℓ}`. The proofs use only Q odd (§2) and the
  heights mod `q′`. The non-hub hypothesis is stated mod `ℓ^{e_ℓ}`, and
  the transfer to `q′` was not checked. O4 Prop 7.2's period/boundary
  terms are subsumed by Theorem 2.3's cases (a)–(c).

## Replay

```
export PYTHONPATH=scripts
uv run --with sympy python scripts/omega5_codeg.py 1000000000 331 337 347 1024        # ~1 min
uv run --with sympy python scripts/omega5_codeg.py 10000000000 331 337 30011 2048     # ~1 min
uv run --with sympy python scripts/omega5_codeg.py 100000000000 933 937 941 2048      # ~15 min
```
Outputs: `data/omega5/codeg_*.txt`.
