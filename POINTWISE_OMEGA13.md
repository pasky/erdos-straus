# Beyond 1/5: a β-weighted local lemma and the late-prime lightness hypothesis (task O48)

Status: IN PROGRESS (checkpoint §1). Labels as in DISCOVERIES.md. Notation as in
POINTWISE_OMEGA11.md (O11) and POINTWISE_OMEGA12.md (O12): `𝓛=log T`, atoms `(M,D)`,
`g=gcd(M,4D+1)`, graded class-of-one quarantine `Q=8∏ℓ^{a_ℓ}` (O11 Setting 2.0),
fibre coordinates `X_ℓ` (independent, product measure), `supp E={ℓ: v_ℓ(M)>a_ℓ}`,
`s(E):=|supp E|≤ω(M)`.

## 1. A β-weighted local lemma: constant per-coordinate thresholds

*Why.* O11 Lemma 2.2 needs `Σ_{ℓ∈supp E}w_ℓ≤c` for every event. It gets this from
log-weighted thresholds `θ_ℓ=c(a+1)logℓ/𝓛`, which cost `𝓛/(c(a+1))` per unit of mass.
This factor 𝓛 is one of the two `𝓛`-factors in `log Q≍𝓛·S`.

**Lemma 1.1 (β-weighted LLL; PROVED).** Take a product probability space and
events E. Each E is determined by the coordinates in a finite set `supp E≠∅`,
with `s(E)=|supp E|`. Fix `1<β≤e^{1/3}` and `η:=(3/4)logβ`. Put
`x_E:=β^{s(E)}P(E)` and `w̃_ℓ:=Σ_{E∋ℓ}x_E`. Suppose

```
w̃_ℓ ≤ η   for every coordinate ℓ.                                  (1.1)
```

Then `P(∩Ē) ≥ exp(−(4/3)Σ_E β^{s(E)}P(E))`. Moreover, for every E and every
family 𝒮 of events with `E∉𝒮`, `P(E | ∩_{F∈𝒮}F̄) ≤ x_E`.

*Proof.* Let `E∼E'` mean that their supports meet. E is mutually independent
of the events whose supports are disjoint from its own (product measure), so
this is a dependency graph. Every E lies in some `supp`-coordinate ℓ, so
`x_E≤w̃_ℓ≤η≤1/4`. For `0≤x≤1/4`, `−log(1−x)≤x/(1−x)≤(4/3)x`. Hence

```
∏_{E'∼E}(1−x_{E'}) ≥ exp(−(4/3)Σ_{ℓ∈supp E}w̃_ℓ) ≥ exp(−(4/3)s(E)η) = β^{−s(E)}.
```

The middle step holds because each `E'∼E` shares at least one coordinate with E,
so it is counted in at least one `w̃_ℓ`. So `P(E)=x_Eβ^{−s(E)}≤x_E∏_{E'∼E}(1−x_{E'})`.
This is the asymmetric LLL hypothesis. Its standard conclusions are
`P(∩Ē)≥∏(1−x_E)≥exp(−(4/3)Σx_E)` and the conditional bound. ∎

*Effect.* The criterion is now per coordinate, with a threshold η independent of
ℓ and of the level. The price is the reweighting `β^{s(E)}≤β^{ω(M)}`. With
`β=1+1/K` the weight is `(1+1/K)^{ω(M)}`; heuristically its mean is
`≈(log T)^{1/K}`, which is `O(1)` for `K≍log𝓛`, giving `η≍1/log𝓛`. For comparison,
O11 uses `θ≍logℓ/𝓛`.

**Lemma 1.2 (graded quarantine with threshold η; PROVED, same charging as O11
Lemma 2.2).** Use any weights `s(M,D)≥P(E_{M,D})` that hold uniformly over the Q's
reached. Raise `a_ℓ` while `w̃_ℓ(Q)>η`. At the end, (1.1) holds and

```
log Q ≤ log Q_start + (1/η)·Σ_{(M,D)} β^{ω(M)} s(M,D)·Λ_st(M),
Λ_st(M) := Σ_{(ℓ,a) stepped, ℓ^{a+1}|M} logℓ ≤ log M.
```

*Proof.* A step at `(ℓ,a)` taken at `Q_i` has
`logℓ<(logℓ/η)w̃_ℓ(Q_i)`. Also `w̃_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}β^{ω(M)}s(M,D)`. Each
`(ℓ,a)` is stepped at most once; sum over the steps. ∎

*No gain in the worst case.* If large primes ℓ (`logℓ≍𝓛`) are stepped, then
`Λ_st(M)` can be `≍𝓛`, and the bound is `𝓛S/η`, no better than O11. There is a
gain only if every stepped prime is small. Then `Λ_st(M)≤log M_Y` (M_Y is the
Y-smooth part), whose mean is `≈log Y`.

**Hypothesis LPL(Y) (late-prime lightness).** Let `Y=𝓛^A` with A fixed, and
`g_Y:=` the Y-smooth part of g. Then for every prime `ℓ>Y`

```
V_Y(ℓ) := Σ_{(M,D): ℓ|M} β^{ω(M)}·C_1·g_Y(M,D)/M ≤ η .                   (LPL)
```

For a Y-smooth graded class-of-one Q, survival gives `gcd(M,Q)|g_Y`. So
`P(E)≤C_1g_Y/M` (O12 Lemma 6.2, `C_1=e³`), and (LPL) gives `w̃_ℓ(Q)≤η` at
every `ℓ>Y`. The procedure of Lemma 1.2 therefore never steps a prime `>Y`.
Status: **CONJECTURE**. It is a pointwise statement in ℓ, i.e. ET-type sums in
progressions to a large prime modulus. The O11 §4 "first-term" obstruction
reappears here. Heuristically `V_Y(ℓ)≈S_Y/ℓ+ℓ^{−1/2+o(1)}𝓛^{O(1)}`, which is
`≤η` for `A>4`.

**Hypothesis M(Y) (smooth inflation).**

```
S_Y := Σ_{(M,D)} β^{ω(M)} g_Y/M ≪ 𝓛³(log Y)^{O(1)},
Σ_{(M,D)} β^{ω(M)}(g_Y/M)·log M_Y ≪ 𝓛³(log Y)^{O(1)}.
```

*Heuristic.* In O12's Type I coordinates, class-of-one inflation over the Haar
mass `S_H=Σ1/φ(M)≍𝓛³` is `Σ_{e|P}1=τ(P)`, with `P=4a²d+1`. Restricted to Y-smooth
e it is `τ(P_Y)`, with mean `≈log Y`. So the full `S♯≍𝓛^4` comes from divisors e
of P with a prime factor `>Y`. Under ET-type inputs this should follow from a
Nair–Tenenbaum/Henriot bound for `τ(n_Y)` on `4a²d+1`. Status: **CONJECTURE (expected
standard)**, not proved here.

*EVIDENCE (finite T only).* `scripts/omega13_inflation.py`
(`data/omega13/inflation.txt`, β=1) gives:
* the total inflation `S_g/S_H=1.58, 1.78` at `T=10^4,10^5`;
* `S_Y=S_g` already for `Y≥𝓛³`.

At these T the asymptotic split cannot be seen, so this does not support M(Y).

**Proposition 1.3 (CONDITIONAL on LPL(Y), M(Y), and the interface check below).**
Take `β=1+1/log𝓛` and `Y=𝓛^A`, with the start of O12 Lemma 6.2. Then

```
log Q ≪ 𝓛 + log𝓛·log Y·𝓛³(log Y)^{O(1)} = 𝓛³(log𝓛)^{O(1)},
S_res := Σ β^{s}P(E) ≪ 𝓛³(log𝓛)^{O(1)}.
```

(a) *Haar side.* `log(1/δ*(T)) ≤ log φ(Q) + (4/3)S_res ≪ 𝓛³(log𝓛)^{O(1)}`.
Against POINTWISE_HAAR Thm 2.1 (`≫𝓛³/log𝓛`), this would give the Haar exponent
`a=3` exactly, up to logs.
(b) *Prime side.* O11 Cor 1.2 gives the junta term `O(𝓛(S_res+𝓛))≪𝓛^4(log𝓛)^{O(1)}`,
which is now **the bottleneck**. So `log Z≪𝓛^4(log𝓛)^{O(1)}`, and
`W(p)≥exp(c(log p)^{1/4}(log log p)^{−B})` for infinitely many Mordell-hard p,
modulo (G), ET, and OMEGA10 Thm 3.4.
(c) *Interface check (OPEN).* O8's BRW minorant and O8 Lemma 3.3 (twist) were
written for `x_E=2P(E)` with neighbourhood sums `≤1/32`. They must be re-run with
Lemma 1.1's `x_E=β^sP(E)`, conditional bound `≤x_E`, and coordinate sums `≤η`.
That has not been done. Cell consistency and O11 Lemma 3.1 are unaffected: Q is
still class-of-one.

*Proof sketch of the displays.* By LPL, only primes `≤Y` are stepped, so
`Λ_st≤log M_Y`. Lemma 1.2 with `1/η≍log𝓛` and M(Y) gives `log Q`. Lemma 1.1 gives
(a). For (b): O11 Thm 3.2's assembly, with O11 Cor 1.2's junta applied to the
residual mass. ∎

*What is left.* (i) LPL(Y): attempted in §2 by a hybrid split between small and
late primes, with a second moment over ℓ. Averaging over ℓ is allowed if the
heavy late primes are themselves quarantined and charged, so only
`Σ_{ℓ>Y}V(ℓ)²logℓ` is needed. (ii) M(Y). (iii) A junta below `𝓛·S`. This is the
brief's (ii), and with (i)–(ii) it would push the conditional exponent towards
1/3. (iv) The interface check (c).
