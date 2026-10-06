# Which standard-type hypothesis gives the exponent 1/3? (task O61)

Status: IN PROGRESS. Labels as in DISCOVERIES.md. Notation as in POINTWISE_OMEGA13.md (O13),
POINTWISE_OMEGA14.md (O14), POINTWISE_OMEGA15.md (O15): `𝓛=log T`; atoms `(M,D)`, `M≡3 (4)`,
`M≤T`, `A=(M+1)/4`, `D|A²`, event `E_{M,D}={n≡−4D (mod M)}`;
`W(p)=min{M≡3 (4): p≡−4D (mod M), D|((M+1)/4)²}` (POINTWISE_SIZE §7). *Mordell-hard*: p is a
square modulo 840 (O13 §3).

## 0. Summary (to be completed)

## 1. The hypothesis and the conditional theorem

**Definition 1.1 (unit-class sieve system).** A finite family 𝓔 of *events*
`E={n≡a_E (mod m_E)}` with `2≤m_E≤T` and `gcd(a_E,m_E)=1`. Its *avoider set* is
`S(𝓔)={n∈Ẑ^×: n≢a_E (mod m_E) for all E∈𝓔}`, and `δ(𝓔)` is its Haar measure in `Ẑ^×`
(equivalently: the proportion of unit classes mod `lcm(m_E)` lying in no event). A prime p
*avoids* 𝓔 if `p≢a_E (mod m_E)` for every E. No condition on the number of events, their
overlaps, or the "dimension" is imposed. Fibre conditions `n≡r (mod Q)` are included by
adding the events `n≡c (mod Q)`, `c≢r`.

**Hypothesis LS(C) (Linnik's theorem for sifted sets).** For every unit-class sieve system
with `δ(𝓔)>0` there is a prime `p>T` avoiding 𝓔 with

```
log p ≤ C·( log T + log(1/δ(𝓔)) ).                                          (1.1)
```

More generally, **LS(Φ)** replaces the right side of (1.1) by `Φ(log T+log(1/δ))` for an
increasing function Φ.

*Remarks.* (a) For a single class (all classes mod q but one removed; `T=q`,
`δ=1/φ(q)`), LS(C) is Linnik's theorem with exponent `≤2C` — a theorem (any `C≥5/2`
suffices, Xylouris). LS is the statement that a sifted set behaves, for the purpose of
containing *one* prime, like a residue class of the same density: the *log-scale* (Linnik,
not Cramér) form of the random-set model. (b) The term `log T` is needed: events
`n≡ℓ (mod m_ℓ)` with distinct primes `m_ℓ∈(T/2,T]` kill every prime `ℓ≤T/4` at total cost
`≪1/log T`. (c) The Cramér-type form "`p≪δ^{−1}(log Q)^{O(1)}`" for an arbitrary set of
density δ mod Q is false (take the units of `(Q(1−δ),Q)`); the restriction to events of
*small modulus* T (with `log lcm(m_E)` up to `≍T`) is what makes LS plausible. Its strong
form is in §2.

**Theorem 1.2 (LS ⇒ exponent 1/3; PROVED implication, modulo Nair–Tenenbaum via O13
Thm 3.4).** Assume LS(C). Then for every large T there is a Mordell-hard prime `p>T` with
`W(p)>T` and `log p ≪_C 𝓛³(log𝓛)^5`. Consequently, for infinitely many Mordell-hard primes,

```
W(p) ≥ exp( c_C·(log p)^{1/3}·(log log p)^{−5/3} ).
```

Under LS(Φ), the same holds with `log p≤Φ(C_0𝓛³(log𝓛)^5)`.

*Proof.* Let 𝓔_T consist of (i) all atoms `E_{M,D}` with `M≤T`, and (ii) the events
`n≡c (mod 840)` for the unit classes c that are not squares mod 840. Each atom is a unit
class: `gcd(M,4A)=1` and `D|A²`, so `gcd(4D,M)=1`. Moduli are `≤max(T,840)=T`.

*Density.* Let `(Q,r)` be the good realisation of O13 Thm 3.4 (O13 §5 Setting): `840|Q`, r a
square mod every prime of Q, `log Q≪𝓛³(log𝓛)^5`, and on the coset `rH={n≡r (Q)}` the
indicator F of avoiding all atoms with `M≤T` (O13 §5: *live* atoms; atoms with `M|Q` never
meet rH by O13 Lemma 3.1, and atoms with `−4D≢r (mod gcd(M,Q))` are empty on rH) has
`E_{rH}F≥exp(−(4/3)S_res)`, `S_res≪𝓛³log𝓛`. Every `n∈rH` with `F(n)=1` lies in `S(𝓔_T)`
(r is a square mod 840). Since rH has Haar measure `1/φ(Q)` in `Ẑ^×`,

```
log(1/δ(𝓔_T)) ≤ log φ(Q) + (4/3)S_res ≪ 𝓛³(log𝓛)^5 .
```

*Prime.* LS(C) gives a prime `p>T` avoiding 𝓔_T with `log p≤C(𝓛+log(1/δ(𝓔_T)))≪𝓛³(log𝓛)^5`.
By (ii), p is a square mod 840 (p>T>7 so p is a unit mod 840): Mordell-hard. By (i), no atom
with `M≤T` has `p≡−4D (mod M)`, so `W(p)>T` directly from the definition of W.

*Infinitely many.* As `T→∞` the primes are distinct infinitely often, since `p>T`. Inverting,
`𝓛≫(log p)^{1/3}(log𝓛)^{−5/3}` and `log𝓛≍log log p`. ∎

*Remarks.* (a) The log factors come only from O13 Thm 3.4. Under POINTWISE_HAAR Conj 3.1
in the Mordell-hard normalisation (`log(1/δ)≍𝓛³/log𝓛`), the conclusion improves to
`log W(p)≫(log p·log log p)^{1/3}` i.o. (b) LS is used for *one* system per T, of
"dimension" `κ≍𝓛³/log𝓛` (O14 §2) with sifting range T; it is used far below the sieve limit,
where `log x≍log(1/δ)≍κ·log log T` while the sieve needs `log x≫κ log T`. That `log T`
versus `log log T` per unit of dimension is exactly the gap 1/4 vs 1/3 (§3).

## 2. The ladder of hypothesis strengths; which forms are too strong

Write `π_𝓔(x):=#{T<p≤x: p avoids 𝓔}` and `λ:=log T+log(1/δ(𝓔))`.

| name | statement (for all unit-class systems, moduli ≤ T) | gives (via Thm 1.2) | status |
|---|---|---|---|
| CR(A) (Cramér form) | `π_𝓔(x)≥1` for `log x≥log(1/δ)+A log T` | 1/3 | Assessment: plausible |
| LS(C) (Linnik form) | `π_𝓔(x)≥1` for `log x≥Cλ` | 1/3 | Assessment: plausible; C≥5/2 needed (Linnik) |
| LS(Φ) | `π_𝓔(x)≥1` for `log x≥Φ(λ)` | `log W≫Φ^{−1}(log p)^{1/3}` up to logs | e.g. `Φ(λ)=λ^θ` gives exponent `1/(3θ)` |
| PS_log(C) | `π_𝓔(x)≥δ^{C}π(x)` for `log x≥Cλ` (at `log x=Cλ` the right side is `≥T^C/(Cλ)≥1`) | 1/3 | implies LS(C) |
| PS(C,c) (constant-factor lower bound) | `π_𝓔(x)≥c·δ·π(x)` for `log x≥Cλ` | 1/3 | **heuristically false** (Prop 2.1) |
| AS(C) (asymptotic, "main term") | `π_𝓔(x)~δπ(x)` for `log x≥Cλ` | 1/3 | **false in the integer analogue, heuristically false for primes** (Prop 2.1) |

CR ⇒ LS(max(1,A)) and PS_log(C) ⇒ LS(C) are immediate; PS ⇒ PS_log. So among these the
weakest natural form is LS: *existence of one prime* at *Linnik scale* in the log of the
inverse density. Theorem 1.2 needs LS only for the single family `𝓔_T` (for infinitely many T).

**Proposition 2.1 (main-term forms are too strong).**
(a) (*Integer analogue; PROVED, classical.*) Replace primes by integers and Haar on `Ẑ^×` by
Haar on `Ẑ`, and take the events `n≡0 (mod ℓ)`, ℓ prime `≤z=T`. Then `δ=∏_{ℓ≤z}(1−1/ℓ)`,
`λ=log z+log log z+O(1)`, and for `x=z^u` with u fixed,
`#{n≤x avoiding}=Φ(x,z)~x ω(u)/log z=(e^γω(u)+o(1))·δx` (Buchstab–de Bruijn). Since
`e^γω(u)≠1` for all u outside a discrete set (e.g. `e^γω(2)=e^γ/2=0.8905…`), for every C there
are `u≥2C` with `Φ(x,z)/(δx)↛1`, while `log x=u log z≥Cλ` for large z. So the integer AS(C)
is false for every C.

(b) (*Primes; Assessment, conditional on the Hardy–Littlewood heuristic.*) For the unit classes
`n≡−h (mod ℓ)`, `3≤ℓ≤z`, `h` even fixed, the prime count `#{p≤x: p+h z-rough}` is predicted to
be `(e^γω(u)+o(1))·δ·π(x)·(1+o(1))` with the same Buchstab factor (the roughness of `p+h≤x+h`
is an archimedean constraint invisible to Haar). For a κ-tuple version (classes `−h_1,…,−h_κ`
mod every `ℓ≤z`, `κ<ℓ`) the factor compounds to `(e^γω(u))^κ`. Choosing
`κ≍log z/log log z` (so `λ≍log z`) and u fixed with `e^γω(u)<1`, `u≥2C`, the ratio
`π_𝓔(x)/(δπ(x))` tends to 0: PS(C,c) fails for every fixed C, c. CR, LS and PS_log are not
affected: the deficit `(e^γω(u))^κ=e^{−O(κ)}=δ^{O(1/log log z)}`.

So "primes in sifted sets of dimension κ *with main term*" (brief item (i)) is, as literally
stated, too strong; the deficit is the Buchstab/Maier phenomenon (periodic sets of period
`lcm≫x` sampled by an archimedean window). The correct strength is the log-scale existence
statement LS. EVIDENCE for (b) at toy scale: §6.

## 3. Brief item (i): equidistribution hypotheses (EH, GEH, …) give exactly the 1/4 ceiling

**Proposition 3.1 (EH-type input caps at 1/4; PROVED implication from O14 Thm 4.5 and O15
Cor 2.4/Prop 2.5, same inputs: (G), effective Page, fundamental lemma).** Let 𝓘 be any
hypothesis about the primes `p≤x` that only concerns their distribution in residue classes,
Dirichlet characters or additive characters of moduli `≤x` (with any error terms and any
averaging over moduli): e.g. EH(θ) or GEH(θ) for any `θ<1`, GRH, BV. Every certificate of
"`∃p≤x` prime, Mordell-hard, `W(p)>T`" of the minorant type — `B≤F` on a fibre, B a combination
of functions of those moduli, concluding `Σ_{p≤x}F(p)≥Σ_{p≤x}B(p)>0` from 𝓘 — needs

```
log x ≥ c𝓛^4/log𝓛 ,       i.e.  certified  log W(p) ≪ (log p·log log p)^{1/4}.
```

*Scope.* "Certificate" means a linear certificate in the sense of O15 Def 2.1: it may use
that the prime counting measure `m_x` is nonnegative of mass `N_x` and satisfies 𝓘, but not
its atomicity, integrality or support (O15 §6 (N2)).

*Proof.* Let `log x<0.6𝓛(k+1)` with `k+1=⌊μ*/2⌋`, `μ*≍𝓛³/log𝓛` as in O15 Thm 1.2, i.e.
`log x≤c𝓛^4/log𝓛`. A modulus `q≤x` has at most k big prime factors (`>T^{0.6}`), so every
function of modulus `≤x` restricted to the fibre H is a combination of reduced products with
`|I|≤k`, on which the planted perturbation vanishes (O15 Lemma 1.1, second clause). Hence the
diffuse measure `m_ν:=N_xν` has, for every `q≤x` and every class / character / additive
character mod q, *exactly* the Haar-predicted value `N_xE_H(·)`: it satisfies 𝓘 with zero error,
whatever 𝓘's error terms are. But `∫F dm_ν=0` (O14 Lemma 4.1). So no deduction from 𝓘 (plus
nonnegativity and mass) can conclude `∫F dm_x>0`. ∎

*Comments.* (a) Raising θ (BV `1/2` → EH `1−ε`) changes only the constant c; even a
hypothetical level `x^A`, A fixed, changes only c. The level a sieve needs is `log D≍𝓛^4/log𝓛`,
i.e. `D=x^{(𝓛/log𝓛)^{1+o(1)}}` when `log x≍𝓛³`; beyond level x the primes are *not*
equidistributed (O15 Lemma 2.3). So no level-of-distribution hypothesis reaches 1/3. (b) What
1/4 means here: 1/4 is already PROVED unconditionally up to `(log log p)^{1/2}` (O13 Thm 5.1);
EH adds nothing to the exponent. (c) "Primes in sifted sets of dimension κ *with main term*"
(Bombieri/Friedlander–Iwaniec asymptotic-sieve style) is *not* of type 𝓘: it asserts the
count in the sifted set directly. Its constant-factor and asymptotic forms are too strong
(Prop 2.1); its log-scale form PS_log is a strengthening of LS. Thus item (i), correctly
formulated, collapses to LS. (d) Maynard–Tao weights detect *some* primes among κ forms; they do
not produce elements of a κ-dimensional sifted set below the sieve limit, which is what ES needs
(every event must fail). Assessment.

*The dimension count behind 1/3 vs 1/4.* On the fibre, the big-prime events form a sieve of
dimension `κ≍𝓛³/log𝓛` (conditional odds-mass `R≍κ`, O14 §2) with sifting range `z=T`. The
avoider density is `δ=e^{−Θ(κ)}` up to logs, while a sieve needs `s=log D/log z≫κ`
(sieve limit `β_κ≍κ`), i.e. `log D≫κ𝓛`. LS asks for `log x≍log(1/δ)≍κ`: a factor `𝓛=log z`
below the sieve limit. The Jacobsthal-type example `κ=1` (one class mod each `ℓ≤z`) shows the
`log T` term in LS cannot be dropped, but there `κ log z` and `log T` coincide; no example is
known where a κ-dimensional unit-class sieve with moduli `≤T` has no prime (or integer) avoider
below `exp(C(log T+log(1/δ)))` (Assessment; toy search §6).

## 4. Brief item (ii): Hardy–Littlewood for product sets gives only `W≥(log p)^{2−o(1)}`

A *product system* is a unit-class sieve system in which every event has prime-power modulus;
equivalently its avoider set is a CRT product `S=∏_ℓA_ℓ`, `A_ℓ⊆(ℤ/ℓ^{e_ℓ})^×`, `ℓ^{e_ℓ}≤T`, with
`δ(S)=∏_ℓ|A_ℓ|/φ(ℓ^{e_ℓ})`. **HL_prod(C)** is LS(C) restricted to product systems: primes with
independently prescribed local behaviour at all `ℓ≤T`, the density being the "singular series"
`∏_ℓ|A_ℓ|/φ(ℓ^{e_ℓ})` (the Hardy–Littlewood/Bateman–Horn shape; conjectural because the number
of local conditions grows). The ES avoider set `F_T` (avoid all atoms `M≤T`) is not a product
set; HL_prod can only be applied to product subsets of it. Let `δ_prod(T)` be the largest
density of a product set `S⊆F_T` (resp. `S⊆F_T^{MH}`, the Mordell-hard part).

**Proposition 4.1 (product subsets of the avoider set are thin).**
(a) (*PROVED.*) `log(1/δ_prod(T))≤T^{1/2+o(1)}`, already for `F_T^{MH}`.
(b) (*PROVED modulo the Barban–Davenport–Halberstam theorem.*) Every product set `S⊆F_T` has
`log(1/δ(S))≫T^{1/2}(log T)^{−8}`. Only the atoms `(ℓ_1ℓ_2, q)` with primes
`ℓ_1≡1, ℓ_2≡3 (4)` in `(√T/2,√T]` and a prime `q|(ℓ_1ℓ_2+1)/4` are used.

*Proof of (a).* Fix `ε>0`, `y:=T^{1/2+ε}`. Let `A_2:={1 mod 8}`, and for odd `ℓ≤y` let `A_ℓ` be
the quadratic residues (mod ℓ, lifted to `ℓ^{e_ℓ}`); this contains the Mordell-hard classes at
3, 5, 7. An atom `(M,D)` all of whose primes are `≤y`: for `n∈S`, `(n|M)=1`, while
`(−4D|M)=−1` (O13 Lemma 3.1(b)); so `n≢−4D (M)`. Every other atom has exactly one prime
`ℓ>y≥√T`, to the first power (`ℓ²>T`); put `B_ℓ:={−4D mod ℓ: (M,D) atom, ℓ|M≤T}` and
`A_ℓ:=(ℤ/ℓ)^×∖B_ℓ` for `y<ℓ≤T`. Then S avoids all atoms. `|B_ℓ|≤Σ_{v≤T/ℓ}τ(A_{vℓ}²)≤(T/ℓ)T^{o(1)}
≤T^{1/2−ε+o(1)}≤ℓ/2`, so
`log(1/δ(S))≤log 4+π(y)log2+Σ_{ℓ>y}2|B_ℓ|/(ℓ−1)≤T^{1/2+ε+o(1)}+T^{1+o(1)}Σ_{ℓ>y}ℓ^{−2}≤T^{1/2+ε+o(1)}`. ∎

*Proof of (b).* Let `x:=√T`, block `𝒫:=` primes in `(x/2,x]`, `𝒫_j:={ℓ∈𝒫: ℓ≡j (4)}`. For
`ℓ∈𝒫` let `Ā_ℓ` be the projection of `A_ℓ` mod ℓ and `b_ℓ:=#{q<x/2 prime, q odd: −4q mod ℓ∉Ā_ℓ}`.
For distinct primes `q,q′<ℓ` the classes `−4q,−4q′` mod ℓ are distinct, so
`|Ā_ℓ|≤ℓ−1−b_ℓ` and `δ(S)≤∏_{ℓ∈𝒫}(1−b_ℓ/(ℓ−1))`, hence `log(1/δ(S))≥x^{−1}Σ_{ℓ∈𝒫}b_ℓ`.

*Constraint.* Fix an odd prime `q<x/2` and `c∈(ℤ/q)^×`; let `𝒫_1(c)`, `𝒫_3(c)` be the members
of `𝒫_1`, `𝒫_3` that are `≡c (q)`. For `ℓ_1∈𝒫_1(c)`, `ℓ_2∈𝒫_3(−c^{−1})`: `M:=ℓ_1ℓ_2≤T`,
`M≡3 (4)`, `M≡−1 (q)`, so `4q|M+1`, `q|A_M`, and `(M,q)` is an atom. Since S is a CRT product,
`S∩E_{M,q}=∅` iff `−4q∉Ā_{ℓ_1}` or `−4q∉Ā_{ℓ_2}`. If some `ℓ_1∈𝒫_1(c)` and some
`ℓ_2∈𝒫_3(−c^{−1})` both had `−4q` in Ā, the atom would meet S. So all of `𝒫_1(c)` or all of
`𝒫_3(−c^{−1})` "block q". As `c↦−c^{−1}` is a bijection and the `𝒫_j(c)` partition `𝒫_j`,

```
Σ_{ℓ∈𝒫}[q blocked at ℓ] ≥ Σ_c min(|𝒫_1(c)|,|𝒫_3(−c^{−1})|) ≥ |𝒫|/2 − (1/2)Σ_{a mod 4q}|e(q,a)| ,
```

with `e(q,a):=#{ℓ∈𝒫: ℓ≡a (4q)}−|𝒫|/φ(4q)` (use `min(u,v)≥(u+v)/2−|u−v|/2` and the triangle
inequality through the common mean `|𝒫|/φ(4q)`).

*Summation.* Sum over odd primes `q≤Q:=x(log x)^{−6}`. By Barban–Davenport–Halberstam
(in its π-form for the interval `(x/2,x]`, moduli `m≤4Q`):
`Σ_{m≤4Q}Σ_a e_m(a)²≪xQ log x+x²(log x)^{−10}≪x²(log x)^{−5}`. Cauchy–Schwarz over the
`≤Σ_{q≤Q}φ(4q)≤2Q²` pairs `(q,a)`: `Σ_qΣ_a|e(q,a)|≪Q·x(log x)^{−5/2}`. The main term is
`(π(Q)−1)|𝒫|/2≫Q x(log x)^{−2}`, which dominates. Hence
`Σ_ℓb_ℓ≫Qx(log x)^{−2}` and `log(1/δ(S))≫Q(log x)^{−2}≫T^{1/2}(log T)^{−8}`. ∎

**Corollary 4.2.** (a) HL_prod(C) ⇒ `W(p)≥(log p)^{2−o(1)}` for infinitely many Mordell-hard p
(Thm 1.2's proof with the product set of 4.1(a)). (b) Applying HL_prod to any product subset of
`F_T` certifies only `log p≤C(𝓛+log(1/δ(S)))`, and `log(1/δ(S))≫T^{1/2−o(1)}`: so the route
cannot certify more than `W(p)≥(log p)^{2+o(1)}`. Exponent 2 in the polynomial scale is its
exact value. This is far below the unconditional `exp(c(log p)^{1/4}(log log p)^{−1/4})`
(O13 Thm 5.1), and it extends POINTWISE_OMEGA Prop 6.1 (ceiling 2 for prime-local *designs*
with the class of one) to *all* product sets.

*Reading.* Hardy–Littlewood/Bateman–Horn-type hypotheses are statements about product
(singular-series) sets. The ES avoider set is far from a product: its density `e^{−𝓛^{3+o(1)}}`
exceeds that of its best product subset `e^{−T^{1/2+o(1)}}` by an exponential in T. So any
hypothesis that sees only local, prime-by-prime structure is useless here; the hypothesis must
apply to *non-product* sifted sets (events coupling several primes), as LS does. (Other readings
of item (ii) — e.g. prime values of a polynomial chosen to avoid events — fall under POINTWISE_SIZE
Thm C/Theorem M: a fixed polynomial family has bounded W under Schinzel H; uniformity in the
degree turns it back into LS. Assessment.)

## 5. Is LS plausible? Consistency checks

**5.1 The planted fakes (O14/O15) do not refute LS; they show it is beyond linear methods.**
The planted law ν (O14 Thm 1.3/Lemma 4.1) is a probability measure on the profinite fibre,
`ν≪P` with `dν/dP≤2`, agreeing with Haar on every function reading `≤k≍𝓛³/log𝓛` big
coordinates, and carried by `{F=0}`. LS is a statement about the *primes*; ν would refute it
only if the primes `≤x` were known to be distributed like ν, and nothing of the kind is
known or expected: ν is Haar *re-weighted onto the complement of the avoider set*, i.e. ν is
the hypothetical counterexample itself, not an independent prime-like object. (Contrast
Selberg's parity example, where the fake — integers with `λ(n)=−1` — is a natural sequence
sharing the primes' sieve axioms and *does* miss the target set.) What the fakes do prove is
the converse direction: LS (for `𝓔_T`) does not follow from any input of the type in
Prop 3.1 (level-of-distribution statements, GRH, BV/EH/GEH) through linear certificates, nor
from any orbit-uniform linear certificate of any level (O15 Cor 2.4, Prop 2.5), nor in the
presence of a Siegel-model main term (O15 Thm 3.1). LS is in the same position as
the twin-prime conjecture relative to the sieve: a "beyond-the-barrier" hypothesis. (Assessment
for "not refuted"; PROVED for "not implied by linear certificates", by Prop 3.1.)

**5.2 Exceptional zeros.** If a real χ_1 mod `q_1≤T` has a Siegel zero, a system may keep
only `{χ_1=1}` (δ=1/2), where primes are depleted below `q_1^{O(1)}`. LS(C) still holds for
such systems with `C≥5/2`: Linnik's theorem (uniform, with Deuring–Heilbronn) supplies primes
`≡1 (q_1)` up to `q_1^5`. So LS is consistent with exceptional zeros; it is the log scale that
makes it robust (the Cramér form CR(A) needs A at least Linnik's constant for the same reason).

**5.3 Jacobsthal / Maier.** The known mechanisms that push the first element of a sifted set
far beyond `1/δ` — Jacobsthal-type coverings (one class per prime `≤z` covers intervals of
length `z^{1+o(1)}`, Ford–Green–Konyagin–Maynard–Tao), Maier/Buchstab deficits (Prop 2.1) —
cost at most a factor `T^{O(1)}` or `δ^{o(1)}`, which LS absorbs through `C·log T` and
`C·log(1/δ)`. (Assessment; no unit-class system violating LS is known to us.)

**5.4 POINTWISE_SIZE's heuristic.** Heuristic RA (SIZE §7.3:
`#{p≤N hard: W(p)>T}≈δ*(T)π_h(N)` whenever the right side is `≥1`) implies LS for the family
`𝓔_T` with `C=1+o(1)` (up to the Mordell-hard normalisation), and SIZE's heuristic
`log W≍(log p)^{1/3}` is what Thm 1.2 yields under LS, up to the log factors of O13 Thm 3.4
(and exactly, `(log p·log log p)^{1/3}`, under POINTWISE_HAAR Conj 3.1). Conversely the Haar
*lower* bound `log(1/δ*)≫𝓛³/log𝓛` (POINTWISE_HAAR Thm 2.1) together with an *upper* count of the
same log-scale strength (e.g. `π_{𝓔_T}(x)≤x·δ(𝓔_T)^{1/C}` for `log x≥Cλ`, a hypothetical upper
companion of LS) would make 1/3 the true i.o. exponent up to log factors. Consistent.

**5.5 What is proved unconditionally in the LS shape (restatement of O13 Thm 5.1 and O14 §4, up to `(log𝓛)^{O(1)}`).** O13 Thm 5.1 is, for the family `𝓔_T`,
an unconditional statement `π_{𝓔_T}(x)≥1` for `log x≥C·𝓛·log(1/δ_{rH})·(log𝓛)^{O(1)}`: LS with
an extra factor `log T=𝓛` (the junta/sieve-limit factor). By O14/O15 that factor is forced for
every linear certificate. So LS is exactly "remove the sieve-limit factor `log z` from the
unconditional theorem", the analogue for this sieve of going from Linnik-by-sieve to the
Cramér-type prediction.

## 6. Numerics (EVIDENCE only)

**(N1) Buchstab deficit for primes, compounding in κ** (`scripts/omega16_buchstab.py`,
`data/omega16/buchstab_1e{8,9}.txt`). Events `n≡−h_i (mod ℓ)`, `3≤ℓ≤z=x^{1/u}`, shifts
`H=(2), (2,6), (2,6,8)` (κ=1,2,3); ratio of `#{z<p≤x: p+h_i z-rough ∀i}` to `δ·(π(x)−π(z))`,
δ the exact Haar density in `Ẑ^×`. At `x=10^9`:

| u | κ=1 | κ=2 | κ=3 | `(e^γω(u))^κ` (κ=1,2,3) |
|---|---|---|---|---|
| 1.5 | 1.254 | 1.578 | 1.995 | 1.187, 1.410, 1.674 |
| 2.0 | 0.942 | 0.890 | 0.846 | 0.891, 0.793, 0.706 |
| 3.0 | 1.007 | 1.014 | 1.023 | 1.005, 1.010, 1.016 |
| 4.0, 5.0 | 1.000 | 1.000 | 1.000 | 1.000 |

The ratio is visibly multiplicative in κ (at u=2: `0.942^κ≈0.942, 0.887, 0.836`), and at u=2
it drifts toward the prediction as x grows (κ=3: 0.958, 0.881, 0.846 at `x=10^7,10^8,10^9`;
the gap is the usual `1/log x` secondary terms). This supports Prop 2.1(b): main-term forms
fail by a factor `c^κ`, while log-scale forms (LS, PS_log) are untouched.

**(N2) LS on the ES family itself** (`scripts/omega16_esleast.py`, `data/omega16/esleast_*.json`).
Least prime `p≡1 (24)` with `W(p)>T` (SIZE §7 normalisation), exhaustive to `10^{11}`; δ* from
POINTWISE_SIZE §7.2; `x_C` solves `δ*·li(x_C)/8=1` (Cramér/RA prediction for the first one).

| T | `p_min` | `log p_min` | `log(1/δ*)` | `log x_C` | `log p_min/(𝓛+log(1/δ*))` |
|---|---|---|---|---|---|
| 31 | 2521 | 7.83 | 2.64 | 6.33 | 1.29 |
| 127 | 33289 | 10.41 | 5.47 | 9.69 | 1.01 |
| 511 | 2031121 | 14.52 | 9.40 | 14.04 | 0.93 |
| 1023 | 2031121 | 14.52 | 12.02 | 16.85 | 0.77 |
| 2047 | 2031121 | 14.52 | 15.11 | 20.14 | 0.64 |
| 4095 | `>10^{11}` | `>25.33` | 18.77 | 23.98 | `>0.94` |

(Counts of hard `p<10^{11}` with `W>T`: 40313, 2776, 107, 0 for `T=511,…,4095`, against
`δ*π_h(10^{11})≈42400, 3120, 141, 3.6`; the deficit at fixed T shrinks as x grows — at T=511
it is 18% at `10^9` and 5% at `10^{11}` — as Prop 7.1(a) of SIZE forces eventually.) The
LS ratio stays `≈1` (CR with `A≈1`); the outlier `p=2031121` (`W>2047`) is a lucky early
record. A scan of `[10^{11},10^{12})` for T=4095 is running (`data/omega16/esleast_1e11_1e12.*`).

**(N3) Adversarial sieve systems** (`scripts/omega16_adversary.py`, `data/omega16/adversary_1e9.*`).
Remove `κ` unit classes mod each prime `3≤ℓ≤z` (`z≤1000`, `κ≤8`), chosen greedily to kill the
smallest surviving primes (ℓ in increasing, decreasing or random order — a "Jacobsthal for
primes" adversary). Over all 69 configurations with an answer below `10^9`, the LS ratio
`log p_min/(log z+log(1/δ))` lies in `[0.75,1.15]`; the best (increasing-order) adversary
reaches 1.12–1.15 and does not grow with κ (z=100: 1.00, 1.07, 1.12, 1.15, 1.15, 1.14 for
κ=1,2,3,4,6,8). Against the random-set prediction `p≈log p/δ` the adversary gains a factor
`≈z^{0.85–0.9}` (e.g. z=1000, κ=6: `p_min=5.6·10^8`, `δp_min/log p_min≈425`), *independent of
κ* — exactly the `T^{O(1)}` slack that the `log T` term of LS (or `A log T` of CR) absorbs, and
never a factor growing with the dimension. No toy system violates LS(1.2).
