# The Haar avoider exponent (task O46)

Branch `side-agent/haar-exponent`. Labels follow the house rules. ES is not
solved here or anywhere; everything below is about the profinite (Haar)
avoider density `δ*(T)` of the multiplier frame, i.e. a pure probability
problem on `∏_ℓ ℤ_ℓ`. Nothing here is a statement about primes unless
explicitly said (§5).

Notation. `𝓛 := log T`, `Φ(T) := log(1/δ*(T))`. The target exponent `a` is
defined by `Φ(T) = 𝓛^{a+o(1)}` (if it exists). Before this note:
`𝓛² ≪ Φ ≪ 𝓛^6` (lower: OMEGA8 Prop 6.6, single-prime events, modulo the
standard shifted-prime divisor bound (D'); upper: OMEGA11 Cor 3.3 modulo ET
Prop 1.4; OMEGA12 claims `𝓛^5 log𝓛`). Numerics: local exponent 2.26→2.58
(POINTWISE_SIZE §7.2).

## 0. The event system

Haar measure on `Ẑ`, restricted to the class `n ≡ 1 (24)`. For each
`M ≤ T`, `M ≡ 3 (4)`, `A_M := (M+1)/4`, and each `D | A_M²`, the **event**
`E_{M,D} := {n ≡ −4D (mod M)}`. `δ*(T)` = Haar measure (normalised in
`1 (24)`) of the set where no event occurs. Distinct pairs `(M, −4D mod M)`
are distinct events; repeated ones are counted once.

For an odd prime ℓ the **coordinate** is `X_ℓ := n mod ℓ^{f}` (f large);
the coordinates are independent and uniform on units (and on the fibre
`X_3 ≡ 1 (3)` at ℓ=3). Since `ℓ | M ⇒ ℓ ∤ A_M ⇒ ℓ ∤ D`, every event is an
**atomic event** (a partial assignment): `E_{M,D} = ⋂_{ℓ|M} {X_ℓ ≡ −4D (mod ℓ^{v_ℓ(M)})}`.
For squarefree M only `X_ℓ mod ℓ` matters, and `P(E_{M,D}) = 1/φ(M)`.

Two atomic events **share a bit** if they share a coordinate on which they
prescribe compatible residues and they are compatible on all shared
coordinates (then `P(E∩E') = P(E)P(E')/P(shared part) > 0`); they
**conflict** if on some shared coordinate the prescribed residues are
incompatible (then `E∩E' = ∅`).

## 1. General tools for atomic events on product spaces (PROVED)

Throughout §1: `(X_v)` independent random variables with arbitrary finite
(or countable) ranges; atomic events `E = {X_v ∈ a_{E,v} for v ∈ S_E}` where
each `a_{E,v}` is a single value (or, for prime powers, a residue class —
the arguments below only use that the restriction of E to `S_E∖S` is again
atomic and that `E` factorises over coordinates). For a family `𝓕` write
`Av(𝓕) := ⋂_{E∈𝓕} Ē`.

**Lemma 1.1 (compatible events; PROVED).** Let A be atomic and let 𝓒 be a
family of atomic events none of which conflicts with A. Then
`P(A ∩ Av(𝓒)) ≤ P(A)·P(Av(𝓒))`.

*Proof.* Condition on A, i.e. fix `X_v = a_{A,v}` for `v∈S_A`. For `C∈𝓒`,
`C∩A = A∩C'` where `C'` is the atomic event C with the coordinates in
`S_A` deleted (they agree with A, as C does not conflict with A); `C'` is
independent of `(X_v)_{v∈S_A}` and `C' ⊇ C`. Hence
`P(Av(𝓒) | A) = P(⋂ C̄') ≤ P(⋂ C̄) = P(Av(𝓒))`. ∎

**Lemma 1.2 (negative association; PROVED, classical input).** Let `𝓕_1, …, 𝓕_r`
be families of atomic events such that no event of `𝓕_i` shares a bit with
an event of `𝓕_j` (`i≠j`). Then `P(⋂_i Av(𝓕_i)) ≤ ∏_i P(Av(𝓕_i))`.

*Proof.* Encode each `X_v` by its one-hot indicator vector `(1[X_v=a])_a`.
A one-hot vector of a single random variable is negatively associated
(Joag-Dev–Proschan 1983, multinomial with one trial), and independent unions
of NA families are NA. An atomic event is a nondecreasing function of the
indicators `1[X_v=a_{E,v}]`, `v∈S_E` (its *bits*); `Av(𝓕_i)` is a
nonincreasing function of the bits of `𝓕_i`, and by hypothesis the bit sets
of different `𝓕_i` are disjoint. NA gives `E∏f_i ≤ ∏Ef_i` for nonnegative
nonincreasing `f_i` on disjoint index sets. ∎

(For residue classes mod `ℓ^v` with different v the "bits" are the
indicators of residues mod `ℓ^{f}`; an event uses the bits of its class.
Two events share a bit iff their classes intersect, i.e. iff they are
compatible at ℓ.)

**Lemma 1.3 (lopsided local lemma and its inflation bound; PROVED, standard).**
Let 𝓕 be a family of atomic events, `Γ(E) := {E'∈𝓕: E' conflicts with E}`,
and suppose there are `x_E∈(0,1)` with `P(E) ≤ x_E∏_{E'∈Γ(E)}(1−x_{E'})`.
Then for every atomic event A (in 𝓕 or not) and every `𝓢 ⊂ 𝓕`,

```
P(A | Av(𝓢)) ≤ P(A) · ∏_{E'∈𝓢, E' conflicts with A} (1−x_{E'})^{−1}.
```

*Proof.* The lopsided local lemma (Erdős–Spencer 1991) holds with the
lopsidependency graph Γ, because `P(E | Av(𝓢')) ≤ P(E)` whenever no event
of `𝓢'` conflicts with E (Lemma 1.1). Its proof gives, by induction on
`|𝓢|`, `P(E | Av(𝓢)) ≤ x_E` for `E∈𝓕∖𝓢`. For A, split `𝓢 = 𝓢_1 ∪ 𝓢_2`
with `𝓢_1` the events conflicting with A. Then
`P(A | Av(𝓢)) ≤ P(A | Av(𝓢_2)) / P(Av(𝓢_1) | Av(𝓢_2))`; the numerator is
`≤ P(A)` by Lemma 1.1, and the denominator is
`∏_{E∈𝓢_1}(1 − P(E | Av(earlier ∪ 𝓢_2))) ≥ ∏_{E∈𝓢_1}(1−x_E)`. ∎

**Theorem 1.4 (Janson-type lower bound for atomic events; PROVED).** Under
the hypothesis of Lemma 1.3, put `K := max_{E∈𝓕} ∏_{E'∈Γ(E)}(1−x_{E'})^{−1}`,
`μ := Σ_{E∈𝓕} P(E)` and `Δ := Σ_{{E,E'}: E≠E' share a bit} P(E∩E')`. Then

```
−log P(Av(𝓕)) ≥ μ − KΔ,      and      −log P(Av(𝓕)) ≥ min(μ/2, μ²/(4KΔ)).
```

*Proof.* Order `𝓕 = {E_1,…,E_N}`, `B_i := Av({E_j: j<i})`, so
`P(Av(𝓕)) = ∏_i(1−P(E_i|B_i))` and `−log P(Av) ≥ Σ_i P(E_i | B_i)`. Let
`B_i^d := Av({E_j: j<i, S_j∩S_i=∅})`; then `B_i ⊂ B_i^d`, so
`P(E_i|B_i) ≥ P(E_i)P(B_i|E_i)/P(B_i^d)`. Conditioning on `E_i`, events
`E_j` (`j<i`) conflicting with `E_i` are impossible, those sharing a bit
become `E_j'` (coordinates of `S_i` deleted; `P(E_i)P(E_j')=P(E_i∩E_j)`),
and `B_i^d` is independent of `E_i`. Hence

```
P(B_i | E_i) ≥ P(B_i^d) − Σ_{j<i, j shares a bit with i} P(E_j' ∩ B_i^d).
```

`B_i^d` is the avoidance of a subfamily of 𝓕, and every event conflicting
with `E_j'` conflicts with `E_j`; so Lemma 1.3 gives
`P(E_j' | B_i^d) ≤ K P(E_j')`. Therefore
`P(E_i|B_i) ≥ P(E_i) − K Σ_{j<i, j~i} P(E_i∩E_j)`, and summing over i gives
the first bound (if the right side is negative the inequality
`P(E_i|B_i) ≥ ` it is trivial). For the second: a subfamily
`𝓕' ⊂ 𝓕` satisfies the hypothesis with the same `x_E` (Γ shrinks) and
`P(Av(𝓕)) ≤ P(Av(𝓕'))`. Taking `𝓕'` random with inclusion probability
p, `E μ' = pμ`, `E Δ' = p²Δ`, so some `𝓕'` has `μ'−KΔ' ≥ pμ − p²KΔ`; take
`p = min(1, μ/(2KΔ))`. ∎

*Remarks.* (i) Δ only counts bit-sharing (compatible) pairs; conflicting
pairs, which carry all the "one coordinate, many residues" structure, cost
nothing except through K. (ii) Without some local-lemma control the
statement is false in spirit: Harris' inequality fails for one-hot
variables (`P(X=r | X≠r') > P(X=r)`), which is why Lemma 1.3 is needed for
`P(E_j'|B_i^d)`. (iii) With `x_E = 2P(E)`, `P(E) ≤ 1/8` and
`Σ_{E'∈Γ(E)} P(E') ≤ 1/8` the hypothesis holds and `K ≤ e^{1/3}`.

**Proposition 1.5 (the packing barrier: NA alone stops at `𝓛²`; PROVED).**
Lemma 1.2 bounds `δ* ≤ ∏_{E∈𝓕}(1−P(E))` for every family 𝓕 of pairwise
bit-disjoint events. For every such family of squarefree-modulus ES events,
`Σ_{E∈𝓕, ω(M_E)≥2} P(E) ≤ Σ_{3≤q≤T} 2/(q−1) ≪ log 𝓛`.

*Proof.* Charge each multi-prime event to its least prime q. Bit-disjoint
events through q prescribe pairwise distinct residues mod q, so at most
`q−1` of them, and each has `P(E) = 1/φ(M) ≤ 1/((q−1)·q')` with `q'>q`
another prime of M, so `≤ 2/(q−1)²` for q≥3. Summing: `≤ Σ_q 2/(q−1)`. ∎

So the single-prime bound `Φ ≫ 𝓛²` of OMEGA8 Prop 6.6 is the limit of
"independent/negatively correlated subfamily" arguments; going beyond it
needs the positive-correlation bookkeeping of Theorem 1.4.
