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

*Proof.* All functions used have modulus `≤x`, so B has level `≤x` on the fibre in the sense of
O14 Setting 2.0. O14 Thm 4.5: if `log x≤c𝓛^4/log𝓛` then `E_HB≤0`; and a certificate from
equidistribution needs `Σ_pB(p)≈N_xE_HB>0` up to the errors granted by 𝓘, which (since every
function of modulus `≤x` has a translation orbit within the family) are subject to O15 Cor 2.4
and Prop 2.5 (orbit-uniform, Hölder-averaged): the planted fake `N_xν` satisfies every such
statement with `E B` computed under ν equal to that under Haar (level `≤x<D`), so it is
consistent with 𝓘 at the true accuracy whenever `log x≤c𝓛^4/log𝓛`, and gives `∫F dm_ν=0`. ∎

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
