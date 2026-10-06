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
