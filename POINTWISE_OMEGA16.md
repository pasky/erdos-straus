# Which standard-type hypothesis gives the exponent 1/3? (task O61)

Status: CHECKPOINT 1 (for parent review). Labels as in DISCOVERIES.md. Notation as in POINTWISE_OMEGA13.md (O13),
POINTWISE_OMEGA14.md (O14), POINTWISE_OMEGA15.md (O15): `𝓛=log T`; atoms `(M,D)`, `M≡3 (4)`,
`M≤T`, `A=(M+1)/4`, `D|A²`, event `E_{M,D}={n≡−4D (mod M)}`;
`W(p)=min{M≡3 (4): p≡−4D (mod M), D|((M+1)/4)²}` (POINTWISE_SIZE §7). *Mordell-hard*: p is a
square modulo 840 (O13 §3).

## 0. Summary

**Answer.** The weakest natural hypothesis found is **LS ("Linnik's theorem for sifted
sets")**: every unit-class sieve system (events `n≡a_E (mod m_E)`, `m_E≤T`, any number, any
overlap, any dimension) whose avoider set has Haar density `δ>0` contains a prime `p>T` with
`log p≤C(log T+log(1/δ))` (§1). It is the log-scale (Linnik, not Cramér) form of the random-set
model, and for a single residue class it *is* Linnik's theorem.

* **Thm 1.2 (PROVED implication, modulo Nair–Tenenbaum via O13 Thm 3.4):** LS(C) ⇒
  `W(p)≥exp(c(log p)^{1/3}(log log p)^{−5/3})` for infinitely many Mordell-hard p; LS is needed
  for one system per T only. `LS(Φ)` with `Φ(λ)=λ^θ` gives exponent `1/(3θ)`.
* **Brief item (i)** (EH-type equidistribution): any hypothesis consisting of Haar-centred error
  bounds for primes in classes / characters of moduli `≤x` (BV, EH, GRH *truncated to moduli `≤x`*, the progression part of
  GEH), used through a linear certificate (O15 Def 2.1), yields at most exponent **1/4** — the
  planted fake satisfies it (Prop 3.1). "Primes in sifted sets
  *with main term*" is too strong as stated: its asymptotic and constant-factor forms are
  false in the integer analogue and heuristically false for primes by a compounding Buchstab
  deficit `(e^γω(u))^κ` (Prop 2.1; numerics §6 N1); its log-scale form implies LS.
* **Brief item (ii)** (Hardy–Littlewood/Bateman–Horn-type hypothesis for product sets — read as
  LS restricted to CRT-product sifted sets with growingly many local conditions, not a standard
  fixed-polynomial HL/BH statement): yields exactly
  **exponent 2 in the polynomial scale**, `W≥(log p)^{2−o(1)}` and no more, because every CRT-product
  subset of the avoider set has `log(1/δ)≍T^{1/2±o(1)}` (Prop 4.1, lower bound modulo
  Barban–Davenport–Halberstam). This extends POINTWISE_OMEGA Prop 6.1 to all product sets.
* **Brief item (iii)** (Cramér-type least prime): CR(A) `log p≤log(1/δ)+A log T` ⇒ LS ⇒ **1/3**.
  The literal "`p≪δ^{−1}(log Q)^{O(1)}` for any set of density δ mod Q" is false (§1 Rem (c)).
* **Consistency (§5):** LS is not refuted by the planted/parity-type fakes (they are reweightings
  of Haar onto the complement of the avoider set, not prime-like sequences), but it is provably
  *not* reachable by linear certificates (Prop 3.1): a beyond-the-barrier hypothesis like twin
  primes. Robust to Siegel zeros (Linnik + Deuring–Heilbronn) and Jacobsthal/Maier effects (all
  absorbed by the `log T`, `C` slack). Matches POINTWISE_SIZE's `log W≍(log p)^{1/3}`; RA ⇒ LS for the ES family `𝓔_T`.
  LS = "remove the sieve-limit factor `log z` from O13 Thm 5.1".
* **EVIDENCE (§6):** Buchstab compounding for primes to `10^9` (N1); on the ES family the LS
  ratio `log p_min/(𝓛+log(1/δ*))` is 0.64–1.29 for `T≤4095` (least hard p with `W>4095` is
  `133050918961`, `W=5935`) (N2); greedy adversarial sieve systems of dimension `κ≤8` stay at LS
  ratio `≤1.15` on the resolved configurations (3 of 69 unresolved), gaining `≈z^{0.85–0.9}` over
the random model with no visible growth in κ on this grid (N3).

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
`δ=1/φ(q)`), LS(C) asks for a prime `p>q`, `p≡a (q)`, `p≤q^{2C}` — Linnik's theorem, which
holds for some absolute C (Linnik's lower bound `π(x;q,a)≫x/(φ(q)√q log x)` for `x≥q^L` gives at
least two such primes, so one exceeds q; we do not track the best admissible C). LS is the statement that a sifted set behaves, for the purpose of
containing *one* prime, like a residue class of the same density: the *log-scale* (Linnik,
not Cramér) form of the random-set model. (b) Some `T^{O(1)}` slack beyond `1/δ` is needed
(R61 m2): the least avoiding prime `>T` can exceed `T^{1−o(1)}/δ`. Shifted Jacobsthal: a gap
`(a,a+y)` in the integers coprime to `P(z)`, `gcd(a,P(z))=1`, is a covering of `(0,y)` by the unit
classes `−a mod ℓ`, `ℓ≤z`, with `δ≍1/log z` and `y=z^{1+o(1)}` (Ford–Green–Konyagin–Maynard–Tao);
the greedy adversaries of §6 N3 and of R61 (moduli the primes in `(T/2,T]`) gain a factor `≈T`
over `log p/δ`. The `C·log T` term absorbs this. (c) The Cramér-type form "`p≪δ^{−1}(log Q)^{O(1)}`" for an arbitrary set of
density δ mod Q is false (take the units of `(Q(1−δ),Q)`); the restriction to events of
*small modulus* T (with `log lcm(m_E)` up to `≍T`) is what makes LS plausible. Its strong
form is in §2.

**Theorem 1.2 (LS ⇒ exponent 1/3; PROVED implication, modulo Nair–Tenenbaum via the *proof* of O13
Thm 3.4, i.e. its good realisation `(Q,r)`, O13 §5 Setting).** Assume LS(C). Then for every large T
(`T≥e^{33}`, O13 §5 range) there is a Mordell-hard prime `p>T` with
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
where `log x≍log(1/δ)≍κ·log log T` (up to log factors; exact under HAAR Conj 3.1, R61 m6) while the sieve needs `log x≫κ log T`. That `log T`
versus `log log T` per unit of dimension is exactly the gap 1/4 vs 1/3 (§3).

## 2. The ladder of hypothesis strengths; which forms are too strong

Write `π_𝓔(x):=#{T<p≤x: p avoids 𝓔}` and `λ:=log T+log(1/δ(𝓔))`.

| name | statement (for all unit-class systems, moduli ≤ T) | gives (via Thm 1.2) | status |
|---|---|---|---|
| CR(A) (Cramér form) | `π_𝓔(x)≥1` for `log x≥log(1/δ)+A log T` | 1/3 | Assessment: plausible |
| LS(C) (Linnik form) | `π_𝓔(x)≥1` for `log x≥Cλ` | 1/3 | Assessment: plausible; true for single classes for some absolute C (Linnik) |
| LS(Φ) | `π_𝓔(x)≥1` for `log x≥Φ(λ)` | `log W≫Φ^{−1}(log p)^{1/3}` up to logs | e.g. `Φ(λ)=λ^θ` gives exponent `1/(3θ)` |
| PS_log(C,c_0) | `π_𝓔(x)≥c_0δ^{C}π(x)` for `log x≥Cλ` (some `c_0∈(0,1/2]`) | 1/3 | implies LS(C+1) for large T |
| PS(C,c) (constant-factor lower bound) | `π_𝓔(x)≥c·δ·π(x)` for `log x≥Cλ` | 1/3 | **heuristically false** (Prop 2.1) |
| AS(C) (asymptotic, "main term") | `π_𝓔(x)~δπ(x)` for `log x≥Cλ` | 1/3 | **false in the integer analogue, heuristically false for primes** (Prop 2.1) |

CR ⇒ LS(max(1,A)) is immediate. PS_log(C,c_0) ⇒ LS(C+1): at `log x=(C+1)λ`,
`c_0δ^Cπ(x)≫c_0δ^C(T/δ)^{C+1}/λ≥c_0T^{C+1}/λ≥1`. PS(C,c) ⇒ PS_log(C,c) since `δ≤1`, `C≥1`
(take `c≤1/2`; the empty system shows `c` must be `<1` — `π_𝓔(x)=π(x)−π(T)`). So among these the
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

(b) (*Primes; Assessment.*) For the unit classes
`n≡−h (mod ℓ)`, `3≤ℓ≤z`, `h` even fixed, the prime count `#{p≤x: p+h z-rough}` is predicted to
be `(e^γω(u)+o(1))·δ·π(x)·(1+o(1))` with the same Buchstab factor (the roughness of `p+h≤x+h`
is an archimedean constraint invisible to Haar). For a κ-tuple version (distinct even shifts
`h_1,…,h_κ≤y`, classes `−h_i` mod every prime `ℓ∈(y,z]`, so all are distinct units and
`κ<ℓ−1`; small primes `ℓ≤y` carry no events) the factor is predicted to compound to
`(e^γω(u))^κ`. Choosing `κ≍log z/log log z`, `y=κ²` (so `λ≍log z`) and u fixed with
`e^γω(u)<1`, `u≥2C`, the ratio `π_𝓔(x)/(δπ(x))` would tend to 0: PS(C,c) fails for every fixed
C, c. *Assumptions beyond fixed-tuple HL:* this needs the Buchstab factor to compound *uniformly*
for κ growing with z (a uniform k-tuple heuristic with archimedean corrections), which is
stronger than any fixed-tuple Hardy–Littlewood statement; hence the label Assessment. Part (a)
shows the failure of the integer AS (not of an integer PS: `ω(u)>0`). CR, LS and PS_log are not
affected: the deficit `(e^γω(u))^κ=e^{−O(κ)}=δ^{O(1/log log z)}`.

So "primes in sifted sets of dimension κ *with main term*" (brief item (i)) is, as literally
stated, too strong; the deficit is the Buchstab/Maier phenomenon (periodic sets of period
`lcm≫x` sampled by an archimedean window). The correct strength is the log-scale existence
statement LS. EVIDENCE for (b) at toy scale: §6.

## 3. Brief item (i): equidistribution hypotheses (EH, GEH, …) give exactly the 1/4 ceiling

**Proposition 3.1 (EH-type input caps at 1/4; PROVED implication from O14 Thm 4.5 and O15
Cor 2.4/Prop 2.5, same inputs: (G), effective Page, fundamental lemma).** Let 𝓘 be any
hypothesis consisting of *Haar-centred error bounds* for the primes `p≤x`, `p∈H`, `p∤q`, in
residue classes, Dirichlet characters or additive characters of moduli `q≤x`: statements
`|Σ_{p≤x,p∈H,p∤q}h(p)−N_{x,q}E_Hh|≤𝔈_h` (`N_{x,q}`: number of such primes), individually or
averaged over h and q, with error bounds `𝔈_h≥2log x` (resp. averages of such) — e.g. BV,
EH(θ) for any `θ<1`, GRH truncated to moduli `≤x`, and the specialisation of GEH to primes in
progressions. (GEH's full content about general convolutions, and anything not Haar-centred, is not
covered. **Full GRH is not covered** (R61 M1): it also asserts `|Σ_{p≤x}χ(p)|≪√x log²(qx)` for
characters of modulus `q>x`, e.g. mod `lcm(M≤T)≈e^T`, which is non-trivial at `log x≍𝓛^4`; whether
the planted ν satisfies these — i.e. whether its Fourier coefficients at all characters of modulus
`≤e^{O(T)}` are `≪T²x^{−1/2}` — is open. O15 Cor 2.4 covers such characters only for
full-orbit-uniform use.) Every certificate of
"`∃p≤x` prime, Mordell-hard, `W(p)>T`" of the minorant type — `B≤F` on a fibre `n≡r (Q)` with `log Q≤T^{0.05}`, B a combination
of functions of those moduli, concluding `Σ_{p≤x}F(p)≥Σ_{p≤x}B(p)>0` from 𝓘 — needs

```
log x ≥ c𝓛^4/log𝓛 ,       i.e.  certified  log W(p) ≪ (log p·log log p)^{1/4}.
```

*Scope.* "Certificate" means a linear certificate in the sense of O15 Def 2.1: it may use
that the prime counting measure `m_x` is nonnegative of mass `N_x` and satisfies 𝓘, but not
its atomicity, integrality or support (O15 §6 (N2)).

*Proof.* Let `log x<0.6𝓛(k+1)` with `k+1=⌊μ*/2⌋`, `μ*≍𝓛³/log𝓛` as in O15 Thm 1.2, i.e.
`log x≤c𝓛^4/log𝓛`. A modulus `q≤x` has at most k big prime factors (`>T^{0.6}`), so every
function of modulus `≤x` restricted to the fibre H depends on the small coordinates and on at
most k big ones, i.e. lies in O14's `𝒱_k`, on which ν and Haar agree (O14 Thm 1.3; equivalently
the `|I|≤k` clause of O15 Lemma 1.1, whose proof uses no mean condition). The planting condition
holds on every fibre with `log Q≤T^{0.05}` (O14 Thm 4.5 / O15 Thm 1.2). Hence the
diffuse measure `m_ν:=N_xν` has, for every `q≤x` and every class / character / additive
character mod q, *exactly* the value `N_xE_H(·)`, which differs from the centring `N_{x,q}E_H(·)`
by at most `(N_x−N_{x,q})·1≤ω(q)≤2log x`: it satisfies every statement of 𝓘, whatever its error
terms, as long as they are `≥2log x` per statement (for averaged forms such as EH, the extra
`Σ_{q≤x^θ}2log x≤2x^θlog x` is below the `x(log x)^{−A}` allowed). But `∫F dm_ν=0` (O14 Lemma 4.1). So no deduction from 𝓘 (plus
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
`∏_ℓ|A_ℓ|/φ(ℓ^{e_ℓ})`. This is our reading of brief item (ii): it has the Hardy–Littlewood/
Bateman–Horn *shape* (density = product of local densities) but is a bespoke growing-system
least-prime hypothesis, not a standard fixed-polynomial HL/BH statement. The ES avoider set `F_T` (avoid all atoms `M≤T`) is not a product
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
(in its π-form for the interval `(x/2,x]`, moduli `m≤4Q`, reduced residues a only):
`Σ_{m≤4Q}Σ_{a∈(ℤ/m)^×}e_m(a)²≪xQ log x+x²(log x)^{−10}≪x²(log x)^{−5}`. Cauchy–Schwarz over the
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
Prop 3.1 (level-of-distribution statements, GRH for moduli `≤x`, BV/EH/progression-GEH) through linear certificates, nor
from any orbit-uniform linear certificate of any level (O15 Cor 2.4, Prop 2.5), nor in the
presence of a Siegel-model main term (O15 Thm 3.1). LS is in the same position as
the twin-prime conjecture relative to the sieve: a "beyond-the-barrier" hypothesis. (Assessment
for "not refuted"; PROVED for "not implied by linear certificates", by Prop 3.1.)

**5.2 Exceptional zeros.** If a real χ_1 mod `q_1≤T` has a Siegel zero, a system may keep
only `{χ_1=1}` (δ=1/2), where primes are depleted below `q_1^{O(1)}`. LS(C) still holds for
such systems once C is at least a Linnik exponent: Linnik's theorem (uniform in q, exceptional zero
included, via Deuring–Heilbronn) supplies primes `p>q_1`, `p≡1 (q_1)`, below `q_1^L≤T^L`, while
LS asks for `log p≤C(log T+log 2)`. So LS is consistent with exceptional zeros; it is the log scale that
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
(and exactly, `(log p·log log p)^{1/3}`, under POINTWISE_HAAR Conj 3.1). Consistent.
*No uniform upper companion.* One might hope to make 1/3 the exact exponent by an upper bound
of the same log-scale strength, e.g. "`π_𝓔(x)≤x·δ^{1/C}T^C` for all `x≥T`". For the ES family this
would give `W(p)≤exp(C′(log p·log log p)^{1/3})` for *every* large Mordell-hard p (take
`log(1/δ)≫𝓛³/log𝓛`, POINTWISE_HAAR Thm 2.1) — in particular ES for all large p. But as a
statement about *all* unit-class systems it is **false**: for a prime `p_0∈(T,2T]` remove every
class mod each `m≤T` except `p_0 mod m`; then `δ=1/φ(lcm(m≤T))=e^{−(1+o(1))T}` and `p_0` avoids
everything, while the bound demands `π_𝓔(2T)<1`. Upper companions must therefore be
family-specific (for `𝓔_T` they amount to a quantitative form of ES itself, like RA's upper half).
LS has no such problem: tailoring a system to a prime only helps existence.

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
| 4095 | 133050918961 | 25.61 | 18.77 | 23.98 | 0.95 |

(Counts of hard `p<10^{11}` with `W>T`: 40313, 2776, 107, 0 for `T=511,…,4095`, against
`δ*π_h(10^{11})≈42400, 3120, 141, 3.6`; the deficit at fixed T shrinks as x grows — at T=511
it is 18% at `10^9` and 5% at `10^{11}` — as Prop 7.1(a) of SIZE forces eventually.) The
LS ratio stays `≈1` (CR with `A≈1`); the outlier `p=2031121` (`W>2047`) is a lucky early
record. The T=4095 entry is from the scan of `[10^{11},2.27·10^{11})`
(`data/omega16/esleast_1e11_1e12.log`): `p=133050918961` (`≡121 (840)`, a square), with
`W(p)=5935` recomputed independently by direct divisor search; it lies a factor ≈5 beyond the
Cramér/RA estimate `x_C≈2.6·10^{10}`, consistent with the deficit noted above.

**(N3) Adversarial sieve systems** (`scripts/omega16_adversary.py`, `data/omega16/adversary_1e9.*`).
Remove `κ` unit classes mod each prime `3≤ℓ≤z` (`z≤1000`, `κ≤8`), chosen greedily to kill the
smallest surviving primes (ℓ in increasing, decreasing or random order — a "Jacobsthal for
primes" adversary). Over the 66 of 69 configurations with an answer below `10^9`, the LS ratio
`log p_min/(log z+log(1/δ))` lies in `[0.75,1.15]`; the best (increasing-order) adversary
reaches 1.12–1.15 and does not grow with κ (z=100: 1.00, 1.07, 1.12, 1.15, 1.15, 1.14 for
κ=1,2,3,4,6,8). Against the random-set prediction `p≈log p/δ` the adversary gains a factor
`≈z^{0.85–0.9}` (e.g. z=1000, κ=6: `p_min=5.6·10^8`, `δp_min/log p_min≈425`), with no visible
growth in κ on this grid — exactly the `T^{O(1)}` slack that the `log T` term of LS (or `A log T` of CR) absorbs, and
no factor growing with the dimension was observed (a finite, censored grid). No resolved toy system violates LS(1.2); the three
unresolved ones (`p_min>10^9`) have ratio `>0.98`, `>0.98`, `>1.12`.

## 7. Status

| item | statement | label |
|---|---|---|
| Hyp LS(C), LS(Φ) | Linnik for unit-class sifted sets | CONJECTURE (Assessment: plausible, §5) |
| Thm 1.2 | LS(C) ⇒ `W≥exp(c(log p)^{1/3}(loglog p)^{−5/3})` i.o., Mordell-hard | PROVED implication, modulo NT (via the realisation `(Q,r)` in the proof of O13 Thm 3.4) |
| Prop 2.1(a) | integer analogue of AS(C) false for every C | PROVED (Buchstab–de Bruijn, classical) |
| Prop 2.1(b) | PS(C,c), AS(C) fail for primes by `(e^γω(u))^κ` | Assessment (HL heuristic); EVIDENCE N1 |
| Prop 3.1 | Haar-centred BV/EH/progression-GEH/GRH input for moduli `≤x`, linear certificates: exponent ≤ 1/4 (full GRH not covered) | PROVED implication, inputs of O14 Thm 4.5 ((G), effective Page, fundamental lemma) |
| Prop 4.1(a) | product subset of `F_T^{MH}` with `log(1/δ)≤T^{1/2+o(1)}` | PROVED |
| Prop 4.1(b) | every product subset of `F_T` has `log(1/δ)≫T^{1/2}(log T)^{−8}` | PROVED modulo Barban–Davenport–Halberstam |
| Cor 4.2 | HL_prod ⇒ `W≥(log p)^{2−o(1)}` i.o.; route capped at `(log p)^{2+o(1)}` | PROVED implication |
| §5 | fakes, Siegel, Jacobsthal, SIZE consistency | Assessment (5.1 "not implied" part PROVED by Prop 3.1; 5.4 uniform upper companion false, PROVED) |
| §6 | N1–N3 | EVIDENCE |

Not done / open: (1) a *proof* that LS holds for some nontrivial class of high-dimensional
systems beyond the sieve limit (this is the whole difficulty); (2) whether LS restricted to
LLL-regular systems (O13 (1.1)) is equivalent to full LS; (3) a natural *family-specific*
upper companion making 1/3 the exact exponent (uniform ones are false, §5.4); (4) the growing small-x deficit of actual hard primes
against δ* at fixed x (N2) is not analysed.

## Replay

```
PYTHONPATH=scripts uv run python scripts/omega16_buchstab.py 1e9      # N1, ~1 min, ~3 GB
PYTHONPATH=scripts uv run python scripts/omega16_esleast.py 4095 1e9   # N2, ~10 s
PYTHONPATH=scripts uv run python scripts/omega16_esleast.py 8191 1e11  # N2, ~15 min
PYTHONPATH=scripts uv run python scripts/omega16_esleast.py 8191 1e12 1e8 1e11  # N2 extension, hours
PYTHONPATH=scripts uv run python scripts/omega16_adversary.py 1e9      # N3, ~15 min, ~5 GB
```
(all under `ulimit -v 8000000`, single core.)
