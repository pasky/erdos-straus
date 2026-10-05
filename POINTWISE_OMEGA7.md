# HC_Π corner residuals: the (m,m*) hyperbola and Kloosterman input (task O26)

Labels follow the house rules. ES is not solved here or anywhere. Notation
as in `POINTWISE_OMEGA6.md` (O6): atoms `(s,a,b)`, s squarefree,
`M=4sab−1=q·m·n′`, `a≡κb (q)`, Π-part m, `m|a+b`, `m|F:=4sa²+1`, weight
`2/n′`, `𝓛=log T`, heights `h_i>H`. By the symmetry `(a,b,κ)↔(b,a,κ^{−1})`
we treat atoms with `a≤b`.

## 1. The (a,j,m,m*) parametrisation and a modular-hyperbola count

**Lemma 1.1 (PROVED).** For an atom put `j:=(a+b)/m∈ℕ` and `m*:=F/m`. Then
(i) `qn′=4saj−m*` and `m*·b=aqn′+j`; (ii) `a·m*≡κj` and `j·m≡(1+κ^{−1})a (mod q)`;
(iii) `m·m*≡1 (mod 4a²)` and `s=(mm*−1)/(4a²)`; (iv) the map
`atom↦(a,j,m,m*)` is injective; (v) if `a≤b`, `2/n′≤8aq/(j·m·m*)`.

*Proof.* `b=jm−a`, so `M=4sa(jm−a)−1=m(4saj)−F=m(4saj−m*)`, giving (i)
first part; multiply `M=qmn′` by a and use `4sa²=mm*−1`:
`mm*b−(a+b)=aqmn′`, i.e. `m*b−j=aqn′`. (ii): mod q, `4sa²≡κ` gives
`4sa≡κā`, and `m*≡4saj (q)` by (i). `jm=a+b≡a+κ^{−1}a`. (iii) is
`F=mm*`. (iv): `(a,m,m*)` fix s, and `(j,m,a)` fix b. (v):
`m*b−j=aqn′>0`, `b=jm−a≥jm/2`, so `aqn′≥jmm*/2−j≥jmm*/4` once `mm*≥4`. ∎

So for fixed `(a,j)` with `gcd(j,q)=1`, `m*` lies in the class
`β:=κjā (q)`, m in `α:=(κ+1)β^{−1} (q)` (as `mm*=F≡κ+1`), and
`mm*≡1 (mod c)`, `c:=4a²`, `gcd(c,q)=1`. Atoms with `s∈[S,2S)` have
`F∈[4a²S,8a²S+1]`. Counting them is a *modular hyperbola* problem.

**Lemma 1.2 (modular hyperbola; PROVED modulo the Weil–Estermann bound
`|K(h_1,h_2;c)|≤τ(c)gcd(h_1,h_2,c)^{1/2}c^{1/2}`).** Let `c≥2`,
`gcd(q,c)=1`, α,β integers, I,J intervals of integers with `|I|,|J|≤c`.
Then

```
N := #{(u,v)∈I×J : (α+qu)(β+qv)≡1 (mod c)} = |I||J|φ(c)/c² + O(τ(c)²c^{1/2}log²(2c)),
```

with an absolute implied constant.

*Proof.* `u↦α+qu` is injective mod c on I. Expand both indicators in
additive characters mod c:
`N=c^{−2}Σ_{h_1,h_2 mod c} Î(h_1)Ĵ(h_2)K(h_1,h_2;c)`, with
`|Î(h)|≤min(|I|,‖hq/c‖^{−1})` (geometric sum). `(0,0)` gives the main
term. If exactly one `h_i=0`, K is a Ramanujan sum, `|c_c(h)|≤gcd(h,c)`;
grouping `h=dh′` (`d|c`) and using that `h′q` runs over residues mod
`c/d`, these terms are `≤c^{−2}·|J|·Σ_{d|c}d·(c/d)log(2c)≤τ(c)log(2c)`.
If `h_1h_2≠0`, Weil–Estermann and the same grouping by
`d=gcd(h_1,h_2,c)` give `≤c^{−2}τ(c)c^{1/2}Σ_{d|c}d^{1/2}(c/d)²log²(2c)
≤τ(c)²c^{1/2}log²(2c)`. ∎

**Proposition 1.3 (box bound; PROVED modulo Weil–Estermann).** Fix
`(a,j)`, `gcd(aj,q)=1`, and dyadic `s∈[S,2S)`, `m∈[M_0,2M_0)`,
`m*∈[M_1,2M_1)`. The atoms with `a≤b` in this box have total weight

```
≤ 2/(ajq) + 2/(ajM_1) + 2/(ajM_0) + 2q/(a³jS) + C·τ(4a²)²log²(8a²)·q/(jS).
```

*Proof.* `F<4M_0M_1` and `F≥4a²S` give `M_0M_1>a²S`; each atom weighs
`≤8aq/(jM_0M_1)` (Lemma 1.1(v)). Put `m=α+qu`, `m*=β+qv`;
`|I|≤M_0/q+1`, `|J|≤M_1/q+1`.
*Case `M_0,M_1≤cq`* (so `|I|,|J|≤c` up to splitting into 2 pieces):
Lemma 1.2 gives `N≤|I||J|/c+Cτ(c)²c^{1/2}log²(2c)`. Multiply by the weight:
`(2q/(ajM_0M_1))(M_0/q+1)(M_1/q+1)` expands to the first four terms, and
`8aq·C τ²·2a log²/(jM_0M_1)≤16Cτ²log²·q/(jS)`.
*Case `M_0>cq`* (or `M_1>cq`): for each m* the m lie in one class mod
`cq`, `≤2M_0/(cq)` of them; so `N≤(M_1/q+1)M_0/(2a²q)` and the weight is
`≤4/(ajq)+4/(ajM_1)`. ∎

**Range covered (correction of a first estimate).** The Kloosterman
error is `≈a^{ε}q/(jS)` *per a*. Summed over `a∈[A,2A)` it is
`≈A^{1+ε}q/(jS)`, so Prop 1.3 is effective for boxes with

```
S ≥ A^{1+ε}·q·H^{a}·𝓛^{B}      (not merely S ≫ qH^a a^ε).
```

The terms `2/(ajM_1)` (`M_1≥` least residue of `κjā`, a hub height
`>H/(aj)` when `a·M_1<q`) and `2/(ajM_0)` (`M_0≥μ/2`, as m>μ) are the
first-term pieces; they are summed over `(a,j)` in §2. The elementary
linear-in-s count (divisors of `4a²s+1` in a class mod q, switching at
`√F`; §2) needs instead `S≥max(A²H^{2a},q)·H^{a}𝓛^B`. So Lemma 1.2 adds
exactly the a-dominant boxes `A≳q`, `AqH^a≤S<A²H^{2a}`. Left open after
both: `S<A·q·H^{a}` with `A≳qH^{−3a/2}` (quadratic-root regime; §3).

## 2. Boxes with a long s-variable (elementary)

Fix a dyadic `(s,a)`-box `[S,2S)×[A,2A)` and consider its atoms with
`a≤b`. Write `d:=m*`, so `m=F/d`. Put `g_0:=gcd(κ+1,q)`.

**Lemma 2.0 (PROVED).** For an atom, every prime `ℓ|g_0` divides j. In
particular, if `gcd(j,q)=1` then `g_0=1`; and `gcd(j,q)>1` forces `j>y`.

*Proof.* `mm*=F≡κ+1≡0 (ℓ)`, and `gcd(m,q)=1` (m is a Π-number prime
to q), so `ℓ|m*`. By Lemma 1.1(ii) `a·m*≡κj (q)` with `a,κ` units, so
`ℓ|j`. The primes of q exceed y. ∎

**Lemma 2.1 (linear count; PROVED).** Fix a and j with `gcd(j,q)=1`, and
let `c:=κjā (q)`, `d_0∈[1,q)` its least residue, `X:=3a√S`. Then

```
N(a,j) := #{(s,d): s∈[S,2S), 4sa²≡κ (q), d|F, d≡c (q), F/d>μ}
       ≤ (S/q)·(1/d_0 + 1/μ + 2(1+log X)/q) + 2(X/q+1).
```

*Proof.* By Lemma 2.0, `g_0=1`, so `e:=(κ+1)c^{−1}` is a unit and
`d′:=F/d≡e (q)`. Since `F≤8a²S+1≤X²`, `d≤X` or `d′≤X`. For a fixed
`d≤X` with `d≡c`: `d|4a²s+1` fixes s mod d (`gcd(d,2a)=1`), and
`4sa²≡κ` fixes s mod q; d is a unit mod q, so s lies in one class mod
qd: `≤S/(qd)+1` values. Summing over `d≡c (q)`, `d≤X`:
`Σ1/d≤1/d_0+Σ_{1≤i≤X/q}1/(iq)`, and there are `≤X/q+1` terms. The d′
side is identical with `d′>μ`, so its first term is `≤1/μ`. ∎

*Remark.* The error `2(X/q+1)` is the only place where "first terms"
enter. It is `≪(S/q)H^{−a}` iff `S≥max(9A²H^{2a}, qH^{a})·O(1)`.

**Lemma 2.2 (first terms; PROVED).** For `d_0(a,j)` as in Lemma 2.1 and
`h_3>H`,

```
E(A) := A^{−1} Σ_{a∈[A,2A), (a,q)=1} Σ_{j≤2T, (j,q)=1} 1/(j·d_0(a,j)) ≤ 12𝓛²(H^{−1/3}+q^{−1}).
```

*Proof.* (1) `d_0(a,j)` depends on `r:=j mod q` only, and
`Σ_{j≡r, j≤2T}1/j≤1/r+2𝓛/q`. As `r↦d_0(a,r)` is injective,
`Σ_r1/d_0≤𝓛`. So `Σ_j1/(jd_0)≤Σ_{1≤r<q}1/(r·d_0(a,r))+2𝓛²/q`.
(2) *Hub bound.* `a·d_0≡κr (q)` with `ad_0r` prime to q, so
`(u,v)=(ad_0,r)` has `u≡κv`, and `h_3>H` gives `rd_0>H/a`. Cover
`[1,q)²` by `≤4𝓛²` dyadic boxes `[R,2R)×[D,2D)`. A box holds
`≤min(R,D)` points `(r,d_0(a,r))` (injective in each coordinate), each
with `1/(rd_0)≤1/(RD)`; a nonempty box has `4RD>H/a`. So a box gives
`≤1/max(R,D)≤(RD)^{−1/2}<2(a/H)^{1/2}`, and
`Σ_r1/(rd_0)≤8𝓛²(2A/H)^{1/2}`.
(3) *Average over a.* For fixed r and each value d, `a≡κr d̄ (q)`, so
`≤A/q+1` values of a give `d_0(a,r)=d`. Hence
`Σ_a1/d_0(a,r)≤(A/q+1)𝓛` and `A^{−1}Σ_aΣ_r1/(rd_0)≤𝓛²(1/q+1/A)`.
Take the better of (2) and (3): `min(8√2(A/H)^{1/2},1/A)≤11.4H^{−1/3}`. ∎

**Proposition 2.3 (long-s boxes; PROVED).** Assume `h_3>H` and let
`μ≥1`. In an `(s,a)`-box, *all* atoms (corner or not) with `a≤b`,
`m>μ`, `gcd(j,q)=1` have total weight

```
≤ 3𝓛/μ + 30𝓛²(H^{−1/3}+q^{−1}) + 𝓛(32A/√S + 6q/S).
```

*Proof.* `2/n′=2qm/(4sab−1)` and `m=(a+b)/j≤2b/j` give
`2/n′≤4q/(j(4sa−1))≤(4/3)q/(jSA)`. By Lemma 1.1(iv) the atoms inject
into the tuples `(s,a,j,d)` counted by `N(a,j)`, `j≤a+b≤2T`. So the
weight is `≤(4q/(3SA))Σ_{a,j}N(a,j)/j`. Insert Lemma 2.1, use
`Σ_{j≤2T}1/j≤2𝓛`, `1+log X≤2𝓛`, `X/q+1≤6A√S/q+1`, and Lemma 2.2 for
the `1/d_0` terms. ∎

**Corollary 2.4.** With `μ=H^{1/3−a}`, `0<a≤1/6`, and `q>H²`: every
`(s,a)`-box with `S≥max(A²,q)·H^{2a}` contributes
`≪𝓛²H^{−a}` from the atoms with `a≤b`, `gcd(j,q)=1`. By the symmetry
`(a,b,κ)↔(b,a,κ^{−1})` (which preserves `h_3` and swaps `h_1,h_2`), the
same holds for `a≥b` in `(s,b)`-boxes with `S≥max(B²,q)H^{2a}`. This uses
no corner structure and no Shiu/Henriot input. ∎

**Lemma 2.5 (the case `gcd(j,q)>1`; PROVED).** Let `g:=gcd(j,q)>1` (q
squarefree, or a prime-power modulus `q′` of O5 Lemma 2.0′). Then
`g≥y`, and the conclusion of Prop 2.3 holds for the atoms with
`gcd(j,q)>1`, with `30𝓛²(H^{−1/3}+q^{−1})` replaced by
`3𝓛/y+11𝓛²/q`.

*Proof.* Fix `g` and a. (i) `jm≡(1+κ^{−1})a (q)` gives `g|κ+1`, and
`d≡κjā (q)` gives `gcd(d,q)=g`. (ii) For a fixed `d|F`, `d≡c:=κjā`:
s is fixed mod q and mod d, compatibly since `F≡κ+1≡0 (g)`; so s lies
in one class mod `qd/g`, `≤gS/(qd)+1` values. Write `d=gd_1`; then
`d≡c (q)` iff `d_1≡c/g (mod q/g)`, so
`Σ_{d≤X}g/d≤1+2𝓛g/q`, with `≤gX/q+1` terms. (iii) `d′=m` is prime to
q and lies in one class mod `q/g` (from `mm*≡κ+1` mod `q/g`, where
`m*` is a unit): `≤S/(qd′)+1` values of s each, and
`Σ_{d′>μ}1/d′≤1/μ+2𝓛g/q`, with `≤gX/q+1` terms. So
`N(a,j)≤(S/q)(1+1/μ+4𝓛g/q)+2(gX/q+1)`. (iv) Now j runs over multiples
of g: `Σ_{j≤2T, g|j}1/j≤2𝓛/g`. Inserting as in Prop 2.3, the factor g
cancels in every term except `S/q·1`, which gives `(4/3)(2𝓛/g)≤3𝓛/y`.
The sum over the `≤2^k` divisors `g|q` costs nothing more: distinct g
give disjoint sets of j. ∎

So the `gcd(j,q)>1` case flagged in §1 is closed, uniformly in the box.
Cor 2.4 holds for all atoms with `a≤b` (resp. `a≥b`) in the stated boxes.
