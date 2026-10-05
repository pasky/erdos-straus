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
