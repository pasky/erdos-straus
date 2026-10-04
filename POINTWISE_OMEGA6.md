# HC_Π: the large-m divisor part of the hub-codegree hypothesis (task O23)

Labels follow the house rules. ES is not solved here or anywhere.
Notation as in `POINTWISE_OMEGA5.md` (O5): vertex set O, modulus q
(odd; squarefree, or `q′=∏ℓ^{v_ℓ}` for prime-power patterns, O5 Lemma
2.0′), class κ (a unit mod q), atoms `(s,a,b)` with s squarefree,
`M=4sab−1`, `q|M`, `a≡κb (q)`, Π-part m of `M/q`, `n′=M/(qm)≥y`, weight
`P(e∖O)≤2/n′`. `𝓛:=log T`. Survival (O5 Lemma 3.1): `m | a+b`,
`m | 4sa²+1`, `m | 4sb²+1`, `gcd(m,2q)=1`. Heights: O has no saturated
H-hub, so (O5 §2) `h_1,h_2,h_3>H` for `(q,κ)`, where
`h_1=min{sa: 4sa²≡κ}`, `h_2=min{sb: 4κsb²≡1}`, `h_3=min{ab: a≡κb, (ab,q)=1}`.
`ω(q)≤k`, `τ(q)≤2^k`. We write

```
Σ^{>μ} := Σ_{atoms, m>μ} 2/n′     (an upper bound for Δ_O^{>μ}, O5 §4).
```

## 0. Summary (filled in as the work proceeds)

* §1 (PROVED). **Three-fibre reduction.** Every atom lies in three
  arithmetic progressions ("fibres"): over `(a,b,m)` (s varies mod qm),
  over `(s,a,m)` (b varies), over `(s,b,m)` (a varies). Atoms that are
  not the first element of some fibre are paid for by that fibre's
  *period* sum. So `Σ^{>1} ≤ (1+𝓛/2)(D_ab+D_sa+D_sb) + 𝒦`, where `𝒦`
  sums over *corner atoms* (first in all three fibres), all of which have
  `s,a,b ≤ 2qm`.
* §2 (PROVED, modulo Shiu 1980 Thm 1 and Henriot 2012 Thm 4). The
  `(s,a)`-plane divisor sum
  `D_sa = Σ_{4sa²≡κ (q)} τ(4sa²+1)/(sa) ≪ 4^k𝓛⁴(H^{−1/2}+q^{−1/4})`.
  This is the "τ_Π(4sa²+1) average over residue classes" asked for.
  Together with O5 Prop 7.1 (`D_ab`), all period parts are done for
  **all** m>1 at once, with exponent 1/4.
* So HC_Π is **equivalent** (up to proved terms) to a bound for the
  corner sum `𝒦`.
* §3 (PROVED). Corner atoms with `min(4sa,4sb,4ab)≤yH^{1/4−a}` are paid
  for by the period sums (Lemma 3.1). Hence HC_Π(a), `a≤1/4`, follows
  from the **first-term bound (FT_a)** (Thm 3.2): on average over
  `4sa²≡κ (q)`, `4sa>yH^{1/4−a}`, the divisors m of `4sa²+1` must not
  put the least `ν≥y` with `qmν≡−1 (4sa)` close to y. Boxes in which a
  plane is long (Shiu/Henriot range) are done (Prop 3.4). The exact
  residual (Cor 3.5): (a) `m≥(qy/32)^{1/2}W^{−3/2}` with `s,a,b<mW`,
  `W=C4^k𝓛²H^a`; (b) boxes with a short plane.
* **HC_Π, HC* and the `(log₂p)^{3/2}` rate remain open.** EVIDENCE (§4):
  at high hub height the m>1 mass is mostly corner mass, of the
  average size predicted by (FT).

## 1. The three-fibre reduction (PROVED)

**Lemma 1.1 (fibres).** Let `m` be a Π-number prime to 2q.

1. *(a,b)-fibre.* Fix `(a,b)` with `a≡κb (q)`, `m|a+b`, `gcd(ab,qm)=1`.
   The s with `qm | 4sab−1` form one class mod qm. Along it,
   `n′_m(s):=(4sab−1)/(qm)` increases in steps of `4ab`.
2. *(s,a)-fibre.* Fix `(s,a)` with `4sa²≡κ (q)` and `m | 4sa²+1`. The b
   with `qm | 4sab−1`, `a≡κb (q)`, `m|a+b` form one class mod qm,
   namely `b≡−a (m)`, `b≡κ^{−1}a (q)`. Along it `n′_m` steps by `4sa`.
3. *(s,b)-fibre.* Fix `(s,b)` with `4κsb²≡1 (q)`, `m|4sb²+1`. The a form
   one class mod qm (`a≡−b (m)`, `a≡κb (q)`), and `n′_m` steps by `4sb`.

Every atom with Π-part m lies in its three fibres (with this m).

*Proof.* (1) is O5 Lemma 7.0. (2) Mod m: `4sa²≡−1` makes `4sa` a unit
with inverse `−a`, so `4sab≡1 ⇔ b≡−a`, and then `m|a+b`. Mod q:
`(4sa)^{−1}≡κ^{−1}a` because `4sa²≡κ`; so `4sab≡1 ⇔ b≡κ^{−1}a ⇔ a≡κb`.
(3) is (2) with `(a,κ)↔(b,κ^{−1})`. The last sentence is O5 Lemma 3.1. ∎

For a fibre, its *elements* are the members of the class with
`y ≤ n′_m ≤ T/(qm)` (true atoms, and possibly integers whose actual
Π-part is a proper multiple of m; those only enlarge the sums below).
The *first element* is the least one.

**Lemma 1.2 (period sums).** In any fibre whose step is `d`
(`d=4ab`, `4sa` or `4sb`), the elements other than the first have total
weight `Σ 2/n′ ≤ (1+𝓛)·2/d`. If `d≤y`, then the first element also has
weight `≤2/y≤2/d`.

*Proof.* The i-th element (i≥1) has `n′ ≥ i·d`, and `i≤T`. So the sum is
`≤(2/d)Σ_{i≤T}1/i ≤ (2/d)(1+𝓛)`. For the first, `n′≥y`. ∎

**Definition 1.3 (corner atoms).** An atom with Π-part m is a *corner
atom* if it is the first element of each of its three fibres, and
`4ab>y`, `4sa>y`, `4sb>y`. Put `𝒦^{>μ}:=Σ_{corner atoms, m>μ} 2/n′`.

**Lemma 1.4 (corner geometry).** A corner atom satisfies
`s,a,b ≤ 2qm` and `n′ < y+4·min(sa,sb,ab)`.

*Proof.* Take the (s,a)-fibre. Either `b≤qm`, and then
`n′=(4sab−1)/(qm)<4sa`. Or `b′:=b−qm≥1` is not an element, so
`n′−4sa=n′_m(b′)<y`. Then `4sab−1=qmn′<qm(y+4sa)`, hence
`b<qm(1+y/(4sa))+1/(4sa)<2qm+1`, as `4sa>y`. So `b≤2qm` and
`n′<y+4sa`. The other two fibres give `a≤2qm`, `n′<y+4sb` and
`s≤2qm`, `n′<y+4ab`. ∎

**Theorem 1.5 (reduction; PROVED).** For every μ≥1,

```
Σ^{>μ} ≤ (1+𝓛/2)·( D_ab + D_sa + D_sb ) + 𝒦^{>μ},
D_ab := Σ_{(a,b): a≡κb (q), (ab,q)=1, ab≤T} τ(a+b)/(ab),
D_sa := Σ_{(s,a): 4sa²≡κ (q), sa≤T} τ(4sa²+1)/(sa),
D_sb := Σ_{(s,b): 4κsb²≡1 (q), sb≤T} τ(4sb²+1)/(sb).
```

*Proof.* Fix an atom with Π-part `m>μ`. If it is not the first element
of its (a,b)-fibre, charge it to that fibre's period sum (Lemma 1.2).
Likewise for the (s,a)- and (s,b)-fibres. If it is the first element of
a fibre with step `d≤y`, charge it to that fibre's first-element bound
`2/d`. Every atom not charged so far is a corner atom. Each fibre is
charged at most `(2/d)(1+𝓛)+2/d=(2+𝓛)·2/d`; with `d=4ab` this is
`(1+𝓛/2)/(ab)`. A fibre over `(a,b,m)` exists
only if `m | a+b`, so the (a,b)-fibres carry total charge
`≤ Σ_{(a,b)} τ(a+b)(1+𝓛/2)/(ab) = (1+𝓛/2)·D_ab`.
The (s,a)-fibres need `m | 4sa²+1` and give `(1+𝓛/2)D_sa`. The (s,b)
ones give `(1+𝓛/2)D_sb`. A fibre contains an atom only if `ab≤T`
(resp. `sa≤T`, `sb≤T`), since `4sab−1≤T`. ∎

*Remarks.* (i) Nothing here uses `m>μ`. The bound holds for the whole
`m>1` part, and also for `m=1` (where it is weaker than O5 Thm 2.3).
(ii) `D_ab` is O5 Prop 7.1's `P_1` (PROVED, `≪2^k𝓛²(q^{−1+o(1)}+H^{−1/4})`).
(iii) `D_sb` is `D_sa` for the class `κ^{−1}`, whose heights are the
same with `h_1↔h_2`. So everything except `𝒦` is reduced to `D_sa`
(§2).

## 2. The (s,a)-plane divisor sum (PROVED modulo Shiu and Henriot)

**Cited theorems.** (Read in `sources/shiu-1980.pdf`, OCR of p. 163, and
`sources/henriot-1102.1643.pdf`, Thm 4 and (1.4).)

* **Shiu** (Crelle 313 (1980), Thm 1). For `f∈M(A,B,ε)` (in particular
  `f=τ`), `0<α,β<1/2`: uniformly in coprime `r,k` and in
  `1≤k<y^{1−β}`, `x^α≤y≤x`,
  `Σ_{x−y<n≤x, n≡r (k)} f(n) ≪ (y/φ(k))(log x)^{−1}exp(Σ_{p≤x, p∤k} f(p)/p)`.
  The constant depends only on `A,B,ε,α,β`.
* **Henriot** (Thm 4, `k=1`). For `f∈M(A,B,ε)`, `Q∈ℤ[X]` irreducible of
  degree g, primitive, discriminant D, `0<α,δ<1`: uniformly in
  `x≥c_0‖Q‖^δ`, `x^α<y≤x`,
  `Σ_{x<n≤x+y} f(|Q(n)|) ≪ Δ_D·y·Π_{g<p≤x}(1−ρ(p)/p)·exp(Σ_{p≤x, p∤D} f(p)ρ(p)/p)`,
  with `Δ_D=Π_{p|D}(1+Σ_{1≤ν≤g} f(p^ν)(ρ(p^ν)p^{−ν}−ρ(p^{ν+1})p^{−ν−1}))`
  and `‖Q‖` the sum of the absolute values of the coefficients. `c_0` and
  the constant depend only on `g,α,δ,A,B`.

We use `f=τ` (`A=2`), `α=1/2`, `β=1/4`, `δ=1/4`, `g=2`. So all implied
constants below are **absolute**. Write `g_0:=gcd(κ+1,q)`.

**Proposition 2.1.** For `T` larger than an absolute constant,

```
D_sa ≤ C·4^k·𝓛⁴·( H^{−1/2} + q^{−1/4} )     (C absolute).
```

*Proof.* Cut into dyadic boxes `s∈[S,2S)`, `a∈[A,2A)`, `SA≤T`; there
are `≤4𝓛²` of them. Put `F:=4sa²+1` and
`D(S,A):=(SA)^{−1}Σ_{box, 4sa²≡κ (q)} τ(F)`. For a pair in the box,
`gcd(a,q)=1`, and `F≡κ+1 (q)`, so `gcd(F,q)=g_0`.

*Regime I: `S ≥ 3A^{2/3}q^{4/3}` (Shiu in s).* Fix a. Then s runs over
one class mod q, so `n:=F` runs over one class mod `4a²q` in
`(4a²S,8a²S]`, and `g_0|n`. Write `n=g_0n_1`, so `τ(n)≤τ(g_0)τ(n_1)≤2^kτ(n_1)`.
Then `n_1` runs over a class `r_1` mod `k_1:=4a²q/g_0`, in an interval of
length `y_1=4a²S/g_0`, and `gcd(r_1,k_1)=1`. (For each `ℓ|q` with
`e=v_ℓ(q)`, `f=v_ℓ(g_0)`: if `f<e` then `v_ℓ(F)=f` exactly, as `F≡κ+1 (ℓ^e)`;
if `f=e` then `ℓ∤k_1`. This also covers the prime-power moduli `q′`.)
Here `k_1<y_1^{3/4}`: this is `(4a²)^{1/3}q^{4/3}g_0^{−1/3}<S`, implied by
`S≥3A^{2/3}q^{4/3}`.
Shiu gives `Σ τ(n_1) ≪ (y_1/φ(k_1))(log x_1)^{−1}exp(2Σ_{p≤x_1}1/p)
≪ (y_1/k_1)(k_1/φ(k_1))log x_1 ≪ (S/q)𝓛²` (using `k/φ(k)≪log log k`
and `x_1≤8T³`). Summing over the `A` values of a:
`D(S,A) ≪ 2^k𝓛²/q`.

*Regime II: `A ≥ C_1 q^{3/2}S^{1/4}` (Henriot in a).* Fix s. The a with
`4sa²≡κ (q)` lie in `≤2^{ω(q)}≤2^k` classes `r mod q`. For each,
`a=r+qi` with i in an interval of length `≤A/q+1` starting at
`x≥A/q−1`; split it into at most two intervals `(x′,x′+y′]` with
`x′^{1/2}<y′≤x′` (plus O(1) single points, bounded pointwise like
Regime III). Put `P(X):=4s(r+qX)²+1`. It is irreducible over ℚ (no real
roots). Its content is exactly `g_0` (the coefficients are `4sq²`,
`8sqr`, `4sr²+1≡κ+1 (q)`; a common divisor is prime to `2sr`, so it
divides q, and then it divides `gcd(q,κ+1)`). Set
`P_1:=P/g_0`, so `τ(P(i))≤2^kτ(P_1(i))`. `disc P_1 = −16sq²/g_0²`.
For `p|2s`, `P≡1 (p)`, so `P_1` is a nonzero constant mod p and
`ρ(p^ν)=0`. For `p | q/g_0`, `P_1≡(4sr²+1)/g_0≢0 (p)` (valuation
argument of Regime I), so again `ρ=0`. Every other `p|disc` divides
`g_0` but not `q/g_0`, hence not `disc P_1`. So `Δ_D=1`.
Also `Π(1−ρ(p)/p)·exp(Σ2ρ(p)/p) ≤ exp(Σ_{p≤x}ρ(p)/p) ≤ exp(2Σ_{p≤x}1/p) ≪ (log x)²`.
Henriot's condition `x≥c_0‖P_1‖^{1/4}` holds because `‖P_1‖≤4s(q+r)²+1≤40Sq²`
and `A≥C_1q^{3/2}S^{1/4}` (C_1 absolute). And `y≥x^{1/2}`. So
`Σ_i τ(P_1(i)) ≪ (A/q)𝓛²`. Summing over r and the `S` values of s:
`D(S,A) ≪ 4^k𝓛²/q`.

*Regime III: neither.* Then `A<C_1q^{3/2}(3A^{2/3}q^{4/3})^{1/4}`, so
`A≪q^{11/5}`, and `S<3A^{2/3}q^{4/3}≪q^{14/5}`. So `F≤32SA²≪q^{36/5}`, and
by Nicolas–Robin (`log τ(n)≤1.0661·log n/log log n`) `τ(F)≤q^{1/8}`
once q exceeds an explicit absolute constant (`q>y²→∞`). The constant
is astronomically large (about `log log q≥62`), but only the asymptotics
matter here. The number of pairs
in the box is at most each of: `A(S/q+1)` (a fixes s mod q), and
`2^kS(A/q+1)` (s fixes a in `≤2^k` classes), and `32SA²/q+1` (the map
`(s,a)↦4sa²<32SA²` is injective for squarefree s, and its values are
`≡κ (q)`; O5 Lemma 1.1).
* If `A>q^{1/2}`: `D(S,A) ≤ q^{1/8}·2^k(1/q+1/A) ≤ 2^{k+1}q^{−3/8}`.
* If `A≤q^{1/2}` and `32SA²≥q`: the count is `≤64SA²/q`, so
  `D(S,A)≤64q^{1/8}A/q≤64q^{−3/8}`.
* If `32SA²<q`: the box holds at most one pair, and it has
  `sa≥h_1>H`, so `SA>H/4`. Since `F≤32SA²≤32(SA)²`,
  `D(S,A)≤τ(F)/(SA)≤(SA)^{−1/2}≤2H^{−1/2}` (for `SA` beyond an absolute
  constant, again by Nicolas–Robin).

Summing over the `≤4𝓛²` boxes, with `q^{−3/8}≤q^{−1/4}` and
`1/q≤q^{−1/4}`, gives the claim. ∎

**Corollary 2.2.** Under the hypotheses of HC* (no saturated H-hub,
`4^k≤H≤y`, so `q>y²≥H²`):

```
Σ^{>μ} ≤ C·4^k·𝓛⁵·H^{−1/4} + 𝒦^{>μ}     for every μ ≥ 1.
```

*Proof.* Theorem 1.5. `D_ab≤P_1` (O5 Prop 7.1) gives `≪2^k𝓛²H^{−1/4}`
(using `q^{−1+o(1)}≤H^{−1/4}`). Prop 2.1 for `D_sa`, and for `D_sb`
(class `κ^{−1}`, heights `h_2>H`), gives `≪4^k𝓛⁴H^{−1/2}` (as
`q^{−1/4}≤H^{−1/2}`). Multiply by `1+𝓛/2`. ∎

So **HC_Π(a′) for `a′≤1/4` is equivalent, up to the proved term
`C4^k𝓛⁵H^{−1/4}`, to `𝒦^{>H^{1/3−a′}} ≪ e^{Ck}𝓛^{B′}H^{−a′}`.** By
Prop 3.2 of O5 (all atoms with `m≤μ`), one may even take μ=1 here and
ask for `𝒦^{>1}`; the m≤μ part of `𝒦` is already covered.

## 3. The corner: what is proved and the exact residual

**Lemma 3.1 (shallow corner; PROVED).** For `Z≥1`, the corner atoms
with `min(4sa,4sb,4ab) ≤ yZ` contribute at most `(Z/2)(D_sa+D_sb+D_ab)`.

*Proof.* Say `4sa≤yZ`. The atom is the first element of its
`(s,a,m)`-fibre, and each fibre has one first element. Its weight is
`2/n′≤2/y≤Z/(2sa)`. Summing over `(s,a)` and `m|4sa²+1` gives
`(Z/2)D_sa`. The other two planes are the same. ∎

**Theorem 3.2 (PROVED).** Let `0<a≤1/4`, `Z:=H^{1/4−a}`, and assume the
hypotheses of HC* (no saturated H-hub, `4^k≤H≤y`). Then for every μ≥1

```
Σ^{>μ} ≤ C·4^k·𝓛⁵·H^{−a} + FT^{>μ}(Z),
FT^{>μ}(Z) := Σ_{(s,a): 4sa²≡κ (q), 4sa>yZ, sa≤T}  Σ_{m | 4sa²+1, m>μ}  2/ν(s,a,m),
ν(s,a,m) := least integer ν≥y with  q·m·ν ≡ −1 (mod 4sa),
```

where m runs over Π-numbers prime to q (C absolute).

*Proof.* Cor 2.2 and Lemma 3.1 with this Z
(`Z·4^k𝓛⁴H^{−1/4}=4^k𝓛⁴H^{−a}`). A remaining corner atom has
`4sa>yZ`, and it is the first element of its (s,a,m)-fibre. The n′-values
of that fibre are exactly the `n′≥y` with `qmn′≡−1 (mod 4sa)`:
`qmn′=4sab−1` gives the congruence; conversely such n′ gives an integer
`b=(qmn′+1)/(4sa)`, which lies in the fibre's class by Lemma 1.1(2).
(`gcd(qm,4sa)=1`, as `m|4sa²+1` and `4sa²≡κ` is a unit mod q.) So its
n′ is ν. ∎

So **HC_Π(a) for a≤1/4 follows from the first-term bound**

```
(FT_a)   FT^{>H^{1/3−a}}(H^{1/4−a}) ≤ e^{Ck}𝓛^{B}H^{−a}    (all O as in HC*).
```

O5's residual `P_0` was the first terms of the `(a,b)`-fibres, summed
over the whole lattice. (FT) is smaller: only the first elements of
(s,a)-fibres with `4sa>yH^{1/4−a}` remain, and the atoms are also corner
atoms (Lemma 1.4: `s,a,b≤2qm`).

**Lemma 3.3 (shape of FT; PROVED).** Put `X:=4sa` and `F:=4sa²+1=aX+1`.

1. `m^{−1}≡F/m (mod X)`. So `ν(s,a,m)` is the least `ν≥y` with
   `ν≡−q^{−1}m* (mod X)`, where `m*:=F/m`.
2. Each residue class mod X contains at most two divisors of F.
3. Hence, pointwise, `Σ_{m|F} 2/ν(s,a,m) ≤ Σ_{0≤i<τ(F)/2} 4/(y+i)`,
   and `ν` always lies in `[y,y+X)`.

*Proof.* (1) `F≡1 (X)`. (2) `F=4sa²+1<16s²a²=X²`. A divisor `m<X` is the
least residue of its class. A divisor `m≥X` has `m*=F/m<X` and
`m*≡m^{−1} (X)`, so m* (hence m) is fixed by the class. (3) By (1) and
(2), distinct ν carry at most two divisors each. ∎

So (FT) asks for the divisors of `aX+1` to avoid, *on average over the
pairs `(s,a)` with `4sa²≡κ (q)`*, the short progression
`{−qν mod X : y≤ν≤y·H^{a}}`. Lemma 3.3(2) is the trivial Lenstra-type
range (`X>F^{1/2}`). The pointwise worst case is
`Σ_{m|F}2/ν ≍ min(τ(F),y)/y`, against the average `≍τ(F)·log(X/y)/X`.

**Proposition 3.4 (long planes; PROVED).** Cut the corner atoms of FT
(i.e. all corner atoms with `4sa>yZ`) into boxes
`s∈[S,2S)`, `a∈[A,2A)`, `b∈[B,2B)`, `m∈[μ_0,2μ_0)` (`≤8𝓛⁴` boxes).

1. If `(S,A)` is in Regime I or II of Prop 2.1, the box contributes
   `≤ C4^k𝓛²μ_0/B`.
2. If `(S,B)` is in Regime I or II (for the class `κ^{−1}`), the box
   contributes `≤ C4^k𝓛²μ_0/A`.
3. If `max(A,B)>3q²`, the box contributes `≤ C2^k𝓛μ_0/S`.

*Proof.* (1) Each corner atom is the first element of its (s,a,m)-fibre,
so the box holds at most `Σ_{(s,a)∈box, 4sa²≡κ}τ(4sa²+1)=SA·D(S,A)` of
them. Each has `n′=(4sab−1)/(qm)≥3SAB/(2qμ_0)`, so weight
`≤(4/3)qμ_0/(SAB)`. Hence the box gives `≤(4/3)(qμ_0/B)D(S,A)`, and
`D(S,A)≪4^k𝓛²/q` in Regimes I–II (proof of Prop 2.1). (2) is the same.
(3) Use the (a,b,m)-fibres, at most `Σ_{(a,b)∈box}τ(a+b)` of them, and O5
Prop 7.1's box bound `2τ(q)(2+𝓛)AB/q` for this sum when `max(A,B)>3q²`. ∎

**Corollary 3.5 (the residual, precisely).** Let `0<a≤1/4` and
`W:=C4^k𝓛²H^{a}`. Under the hypotheses of HC*, HC_Π(a) holds with
`B′=6` **except** for the corner atoms with `4sa>yH^{1/4−a}` in boxes
where, for each of the three planes, either the plane is *short* or the
remaining variable is `<μ_0W`. Here short means Regime III for `(S,A)`
or `(S,B)` (so both sides are `≪q^{14/5}`), and `max(A,B)≤3q²` for
`(a,b)`. In particular:

* if all three planes are long, the residual box has `S,A,B<μ_0W`,
  and `n′≥y` (`32SAB>qμ_0y`) forces
  ```
  m ≥ μ_0 ≥ (qy/32)^{1/2}·W^{−3/2}.
  ```
  So in boxes with three long planes, HC_Π(a) holds for all
  `m < (qy/32)^{1/2}W^{−3/2}`. Since `q>y²`, this is
  `≥ (y^{3/2}/6)H^{−3a/2}(C4^k𝓛²)^{−3/2}`. In the regime of O4 Thm 4.2
  (`k≍𝓛^{1/3}`, `log H≍𝓛^{2/3}`) it is `y^{3/2}H^{−3a/2−o(1)}`, far
  beyond O5's `H^{1/3−a}`.
* The residual is therefore (a) large m, `m ≥ (qy/32)^{1/2}W^{−3/2}`,
  with `s,a,b<mW`; or (b) boxes with a short plane. *(Assessment:)* in
  (b) the numbers `4sa²+1` are `≤q^{O(1)}`, and the only divisor bound
  I have there is pointwise, `τ≤q^{O(1/log log q)}`. That is not
  `≤e^{Ck}𝓛^B` once `log q` is large against `k log k` (in the Thm 4.2
  regime q can be as large as `T^{1−o(1)}`). Regime III's `q^{−3/8}`
  saving does handle short `(s,a)`-boxes whose third side is
  `B≥2^{k+7}μ_0q^{5/8}H^a`; and all boxes with `32SA²<q` contain the
  same single pair, the least residue of κ written as `4sa²` (O5 Lemma
  1.1).

*Proof.* Theorem 3.2 and Prop 3.4 with `B≥μ_0W` (resp. `A≥μ_0W`,
`S≥μ_0W`), summed over the `≤8𝓛⁴` boxes. The displayed bound uses
`(μ_0W)³>SAB>qμ_0y/32`. ∎

## 4. EVIDENCE (`scripts/omega6_corner.py`)

Exact enumeration of all m>1 atoms for one pair q (Π=Π_0, the y-smooth
primes; weights 2/n′; classes are joint classes κ mod q with O3 hub
height h, not lifted vertices). `tot` is the m>1 sum `Σ^{>1}`, `K` its
corner part (Def 1.3). Maxima over classes with `h>X`, taken
independently.

| T | q | atoms m>1 / corner | X=16: tot / K | X=256 | X=512 | `X^{−1/4}` at 512 |
|---|---|---|---|---|---|---|
| 10⁹ | 337·347 | 14756 / 10452 | .038 / .017 | .015 / .015 | .015 / .015 | .21 |
| 10¹¹ | 937·941 | 271490 / 166698 | .092 / .011 | .013 / .0086 | .0083 / .0080 | .21 |

* At small X the non-corner (period) part dominates; it is what §§1–2
  bound. At large X almost all of the m>1 mass is corner mass, so the
  residual of §3 is the real one.
* The heaviest corner classes are hub-like: at T=10⁹, κ=1364 (h=341)
  gets its corner mass from `(s,a)=(341,1)`, with `F=1365=3·5·7·13` and
  one first element per divisor m (Lemma 3.3), plus its mirror `(s,b)`.
  These sums are of size `≈τ(F)·log(4sa/y)/(4sa)`, the "average" size
  of Lemma 3.3, not the worst case `τ(F)/y`.
* `K` is flat to slowly decreasing in X at these sizes and stays well
  below `X^{−1/4}`. This is consistent with (FT) and proves nothing.

## 5. Status

* **PROVED:** Lemmas 1.1, 1.2, 1.4, Theorem 1.5 (three-fibre
  reduction); Prop 2.1 (`D_sa≪4^k𝓛⁴(H^{−1/2}+q^{−1/4})`), **modulo Shiu
  1980 Thm 1 and Henriot 2012 Thm 4** (both cited with absolute
  constants for fixed parameters); Cor 2.2; Lemma 3.1, Theorem 3.2
  (`Σ^{>μ}≤C4^k𝓛⁵H^{−a}+FT`), Lemma 3.3, Prop 3.4, Cor 3.5 (all modulo
  the same two citations, and O5 Prop 7.1).
* **Consequence.** Every period term of the large-m problem is done,
  for all m>1 at once, with exponent 1/4. HC_Π(a), `a≤1/4`, is reduced
  to the first-term bound (FT_a): divisors of `4sa²+1` must avoid, on
  average over `4sa²≡κ (q)`, the classes `−qν mod 4sa` with ν just above
  y. Long-plane boxes are done (Prop 3.4).
* **Open (exact residual, Cor 3.5):** corner atoms with `4sa>yH^{1/4−a}`
  in boxes where every plane is short or has its third side `<mW`. In
  particular: (a) `m≥(qy/32)^{1/2}W^{−3/2}` with `s,a,b<mW`; (b) boxes
  with a short plane (all numbers `≤q^{O(1)}`, no averaging theorem; the
  pointwise divisor bound is too weak when `ω(q)` is large).
* **Not achieved:** HC_Π, hence HC* and the rate
  `log W(p)≥c(log₂p)^{3/2}`, remain **open**. The proved rate is still
  O4 Cor 3.1. Nothing here is claimed for ES.
* *Assessment.* (FT) is a "divisors of `aX+1` in a short progression
  mod X" problem, averaged over a thin quadratic family
  `X=4sa`, `4sa²≡κ (q)`. Lemma 3.3(2) is the trivial Lenstra range
  (`X>F^{1/2}`). What is missing is an equidistribution statement for
  `q^{−1}·(divisors of 4sa²+1) mod 4sa` on average over this family,
  with savings polynomial in H and losses at most `e^{O(k)}𝓛^{O(1)}`.
  I do not know a theorem that gives it. Shiu/Henriot control how many
  divisors there are on average, but not where they lie mod 4sa.

## Replay

```
export PYTHONPATH=scripts
uv run --with sympy python scripts/omega6_corner.py 1000000000 331 337 347 1024      # ~2 s
uv run --with sympy python scripts/omega6_corner.py 100000000000 933 937 941 2048    # ~1-2 min
```
Outputs: `data/omega6/corner_1e9.txt`, `data/omega6/corner_1e11.txt`.
