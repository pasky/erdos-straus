# Beyond 1/5: a β-weighted local lemma and the late-prime lightness hypothesis (task O48)

Status: checkpoint 2 (after R48a/R48b repairs; §5 added). Labels as in DISCOVERIES.md. Notation as in
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
family 𝒮 of events with `E∉𝒮`, `P(E | ∩_{F∈𝒮}F̄) ≤ x_E`. More generally (R48b D5), for
any event A determined by a coordinate set `supp A` (not necessarily in the family),
`P(A | ∩_{F∈𝒮}F̄) ≤ P(A)∏_{F∼A}(1−x_F)^{−1} ≤ β^{|supp A|}P(A)`.

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
`P(∩Ē)≥∏(1−x_E)≥exp(−(4/3)Σx_E)` and the conditional bound. For a general A, the
standard LLL bound `P(A|∩_{𝒮}F̄)≤P(A)∏_{F∈𝒮, F∼A}(1−x_F)^{−1}` is used (as in O8 Lemma 3.3;
Haeupler–Saha–Srinivasan, J. ACM 2011; theorem number not verified, source not archived). It
has a one-line proof (R48c m5): with `𝒮_1:={F∈𝒮: F∼A}`, `𝒮_2:=𝒮∖𝒮_1`, A is independent of
`∩_{𝒮_2}F̄` (disjoint supports), so
`P(A|∩_𝒮F̄)≤P(A∩_{𝒮_2}F̄)/P(∩_{𝒮_1}F̄|∩_{𝒮_2}F̄)≤P(A)/∏_{F∈𝒮_1}(1−x_F)`, the denominator by
the chain rule and the conditional bound `P(F|∩F̄')≤x_F` above. The displayed computation, applied with `supp A`, gives
`∏(1−x_F)^{−1}≤exp((4/3)|supp A|η)=β^{|supp A|}`. ∎

*Range (R48b D5).* The prime-side twist (§5, I1) needs `η≤0.19`. This fails at the
extreme `β=e^{1/3}` but holds for `β=1+1/log𝓛`, which is the only value used, as soon as
`(3/4)log(1+1/log𝓛)≤0.19`, i.e. `𝓛≥32.1` (`T≥e^{33}`) (R48c m3). The exact requirement is
`(0.01+η/(1−η))/0.99≤1/4`, i.e. `η≤0.1919`. All statements below are for such T ("T large").

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

## 2. LPL is not needed pointwise: heavy late primes are quarantined, second moment over ℓ

Put `s♯(E):=β^{ω(M)}C_1·g/M`. By O11 Lemma 2.1 and O12 Lemma 6.2, `P(E)≤s♯(E)` holds
for *every* graded class-of-one Q, uniformly. Put `V♯(ℓ):=Σ_{E: ℓ|M}s♯(E)`.

**Lemma 2.1 (reduction; PROVED).** Fix `Y≥𝓛` and let
`𝓗:={ℓ>Y prime: V♯(ℓ)>η/2}`. This set is deterministic and independent of Q.
Run Lemma 1.2 with only the primes `ℓ≤Y` and `ℓ∈𝓗` eligible. Then:

* (LLL) (1.1) holds at the end, at every coordinate.
* (cost) `log Q ≤ log Q_start + (1/η)Σ_Eβ^{ω}C_1(g_Y/M)log M_Y + (𝓛/η+𝓛)·R_2`.
* (mass) `Σ_Eβ^{s}P(E) ≤ S_Y + R_2`.

Here

```
R_2 := (4/η²)·Σ_{ℓ>Y} V♯(ℓ)².
```

*Proof.*
(LLL) For `ℓ>Y`, `ℓ∉𝓗`: `w̃_ℓ(Q)≤V♯(ℓ)≤η/2`, for every Q. Eligible coordinates
satisfy (1.1) when the procedure stops.

(weights) Let `Q=Q_Y·Q_𝓗`, where `Q_𝓗` is composed of primes in 𝓗. A surviving
atom has `gcd(M,Q)|g`. If no prime of 𝓗 divides `gcd(M,Q)`, then
`gcd(M,Q)|g_Y`, so `P(E)≤C_1g_Y/M` and `x_E=β^{s}P(E)≤β^{ω}C_1g_Y/M=:s_Y(E)`.
Otherwise `x_E≤s♯(E)` and some `ℓ∈𝓗` divides g, hence divides M. So

```
x_E ≤ s_Y(E) + Σ_{ℓ∈𝓗, ℓ|M} s♯(E),       Σ_E x_E ≤ S_Y + Σ_{ℓ∈𝓗}V♯(ℓ).
```

(Chebyshev) On 𝓗, `1<2V♯(ℓ)/η`. So
`|𝓗|≤(4/η²)ΣV♯²=R_2` and `Σ_{ℓ∈𝓗}V♯(ℓ)≤(2/η)ΣV♯²=(η/2)R_2≤R_2`.

(cost) Steps at `ℓ∈𝓗` cost at most `Σ_{a≤f_ℓ}logℓ≤𝓛` per prime, so `≤𝓛|𝓗|≤𝓛R_2`.
Steps at `ℓ≤Y` are charged as in Lemma 1.2, with the uniform weight
`s_Y(E)+Σ_{ℓ'∈𝓗,ℓ'|M}s♯(E)`. This weight is valid for every Q of the above
shape, because 𝓗 is fixed in advance. Their charge `Λ_st(M)≤log M_Y≤𝓛` gives
`(1/η)[Σs_Y log M_Y + 𝓛Σ_{ℓ∈𝓗}V♯(ℓ)] ≤ (1/η)Σs_Y log M_Y + (𝓛/η)R_2`. ∎

**Hypothesis V2(Y).** `Σ_{ℓ>Y prime}V♯(ℓ)² ≪ 𝓛²(log𝓛)^{O(1)}` for some `Y=𝓛^{O(1)}`.

**Corollary 2.2 (CONDITIONAL).** Proposition 1.3 holds with LPL(Y) replaced by V2(Y):
`R_2≪(log𝓛)²·𝓛²(log𝓛)^{O(1)}`, so `𝓛R_2/η≪𝓛³(log𝓛)^{O(1)}`.

*Why V2 is more accessible than LPL.*
* **Averaged over ℓ.** V2 is an average over the moduli ℓ (a
  Barban–Davenport–Halberstam-type second moment), not a pointwise bound for each ℓ.
* **Uses the full weights.** It uses `s♯=g/M` itself: the full ET mass
  `S♯≍𝓛^4log𝓛`, with no smooth truncation.
* **Heuristic size.** `V♯(ℓ)≈S♯/ℓ` gives `Σ_{ℓ>Y}V♯²≈S♯²/(Y logY)≈𝓛^8/Y`.
  So `A≥6` suffices.
* **First-term ℓ.** The special primes with `V♯(ℓ)≈ℓ^{−1/2}𝓛^{O(1)}`
  (`ℓ|4a²+1` with `a≈√ℓ`) have density `≈ℓ^{−1/2}`. They contribute `O(1)`.

*EVIDENCE for V2 versus LPL* (`scripts/omega13_v2.py`, `data/omega13/v2.txt`; β=1, `C_1=1`,
all atoms). Columns: `S♯`; `Σ_{ℓ>Y}V♯²` against the heuristic `S♯²/(Y logY)`; and
`max_{ℓ>Y}ℓV♯(ℓ)/S♯`.

| T | S♯ | Y=𝓛³ | Y=𝓛⁴ | Y=𝓛⁵ | max ℓV♯/S♯ |
|---|---|---|---|---|---|
| 10⁵ | 113.3 | 0.47 (1.15) | 0.019 (0.075) | 0 (0.005) | 6.4 |
| 10⁶ | 206.7 | 1.05 (2.06) | 0.029 (0.112) | 0.0010 (0.0065) | 9.8 |

* *The second moment.* For `Y≥𝓛³` it stays below the heuristic `S♯²/(Y logY)`. At `Y=𝓛²`,
  `T=10⁶` it is slightly above (42.86 vs 42.62; R48b D7).
* *The pointwise ratio.* `max ℓV♯(ℓ)/S♯` grows with T (6.4 → 9.8). This is the
  first-term effect, and it is why we prefer the averaged V2 to the pointwise LPL.
* *Scope.* This is finite-T evidence only.

## 3. Square-class quarantine: no inflation, and late-prime lightness from Haar masses

*Why.* The class of one is special. With class 1, the residual weights are
`gcd(M,Q)/M`, and the inflation `τ(P_Q)` comes from `ℓ|4D+1` (§1, M(Y)). So the
late-prime masses involve g, which is pointwise-hard (§2). With a *random* class
the expected masses are Haar masses `P_H(E)=1/φ(M)`, and those have pointwise
late-prime bounds (Shiu). A random class must still never *fire*: no atom may
have all its coordinates quarantined and matched. That is what the Jacobi lemma
guarantees.

**Lemma 3.1 (event classes are Jacobi non-residues; PROVED).** Let `(M,D)` be an
atom, i.e. `M≡3 (4)`, `A=(M+1)/4`, `D|A²`. Let d be the squarefree part of D. Then

* (a) every prime `ℓ|M` has `(−4D | ℓ) = (−d | ℓ)`;
* (b) the Jacobi symbol `(−4D | M) = −1`.

Consequently, if `gcd(r,Q)=1` and r is a quadratic residue modulo every prime
dividing Q, then `r≢−4D (mod M)` for every atom with `M|Q`. More generally, an
atom whose primes all divide Q is never consistent with r.

*Proof.*
(a) `gcd(M,4A)=1`. Every prime of D divides A, so `ℓ∤2D`. Also `−4D=−4d·□`.
(b) `(−4D|M)=(−d|M)=(−1|M)(d|M)=−(d|M)`, since `M≡3 (4)`. Every prime `p|d` divides A,
because `v_p(D)` is odd and `≤2v_p(A)`. So `M=4A−1≡−1 (mod p)`.
* For odd p, quadratic reciprocity with `(M−1)/2` odd gives
  `(p|M)=(M|p)(−1)^{(p−1)/2}=(−1|p)(−1)^{(p−1)/2}=1`.
* If `2|d`, then `2|A`, so `M≡7 (8)` and `(2|M)=1`.

Hence `(d|M)=1`. For the consequence: `(r|M)=∏(r|ℓ)^{v_ℓ}=1≠(−4D|M)`. ∎

Check: `scripts/omega13_jacobi.py 200000` verifies (a) and (b) on all 2 401 032 atoms with
`M≤2·10^5`, with 0 failures (`data/omega13/jacobi.txt`). These are classical:
ES identities cover the non-residue classes, and the Mordell-hard classes mod 840
are the squares.

**The square-class process (definition).** Start from `Q=8`, `r≡1 (8)`, Haar on the units at
the odd primes. Then take three *forced* `a=0` steps at `ℓ=3,5,7` (R48a m4, R48b D4): r mod 105
is a uniformly random square class, and mod 3 the only square is 1. So `840|Q` and `r≡1 (24)`
always hold, and r is a square mod 840, i.e. a Mordell-hard class. The forced steps are ordinary
`a=0` steps, so Lemma 3.2 covers them verbatim. They add only `log105` to the cost.
Coordinates and events are as in O11 Setting 2.0, but with fibre `n≡r (Q)` in place
of `n≡1 (Q)`. An atom `(M,D)` *survives* `(Q,r)` iff `−4D≡r (mod gcd(M,Q))` and `M∤Q`
(R48d D3; for `r=1` this is O11's `gcd(M,Q)|4D+1`). Equivalently `μ(E)>0`: by Lemma 3.1,
`M|Q` never occurs together with `−4D≡r (mod M)`. Only primes `ℓ≤Y` are eligible. A *step* at `(ℓ,a)` is taken while the
reweighted fibre mass `w̃_ℓ>η` (Lemma 1.1). It reveals `n mod ℓ^{a+1}` uniformly
among the classes of the current fibre that are squares mod ℓ:

* if `a=0`, this is uniform on the `(ℓ−1)/2` squares;
* if `a≥1`, the whole fibre already consists of squares.

By Lemma 3.1 no atom ever fires, so the final system has no deterministic event.
The prime side counts primes `p≡r (mod Q)`. For every real character χ mod Q,
`χ(r)=1`, exactly as for the class of one. So O11 Lemma 3.1's Case A/B analysis is
unchanged. This is checked in §5 (I3).

*Drift.* At an `a=0` step at ℓ, an atom with `ℓ|M` has
`E[p_new(E)]=(1+(−d_E|ℓ))p(E)` by Lemma 3.1(a). That is at most `2p(E)`, not
`p(E)`. All other steps are exact martingale steps.

**Notation.** State i means `(Q_i,r_i)`, with product measure `μ_i`. Put `p_i(E):=μ_i(E)`.
`u_i(E):=#{ℓ≤Y prime: ℓ|M, a_ℓ(i)=0}` counts the small primes of M not yet stepped.
`s_i(E)=|supp_i E|≤ω(M)`. `P_H` is Haar measure on `Ẑ^×`, so `P_H(E)=1/φ(M)`. For
`ℓ‖…`, `E^{(ℓ)}` is the event E with its ℓ-constraint removed.

**Lemma 3.2 (bookkeeping for the square-class process; PROVED).** Let the process stop
when every `ℓ≤Y` has `w̃_ℓ≤η`.

(a) *Supermartingale.* For any fixed weight `φ(E)≥0`, `G_i:=Σ_E p_i(E)2^{u_i(E)}φ(E)` is
a supermartingale.

(b) *Cost.* `E[log Q_end] ≤ log 840 + (1/η)Σ_E P_H(E)2^{ω_Y(M)}β^{ω(M)}log M_Y`.
Here `ω_Y` counts the primes `≤Y` and `M_Y` is the Y-smooth part.

(c) *Residual mass.* `E[Σ_E β^{s_end(E)}p_end(E)] ≤ S_H^β := Σ_E P_H(E)2^{ω_Y(M)}β^{ω(M)}`.

(d) *Late primes.* For every prime `ℓ>Y`, `E[w̃_ℓ(end)²] ≤ B_2(ℓ)`, where

```
B_2(ℓ) := Σ_{E,E': ℓ|M, ℓ|M'} β^{ω(M)+ω(M')} 2^{ω_Y(M)+ω_Y(M')} P_H(E)P_H(E')·φ(gcd(M,M')/ℓ^{min(v_ℓ(M),v_ℓ(M'))}).
```

Hence `P(∃ℓ>Y: w̃_ℓ(end)>η) ≤ η^{−2}Σ_{ℓ>Y}B_2(ℓ)`.

*Proof.*
(a) A step at `(ℓ,a)` with `a≥1` reveals a uniform class of the fibre, and all of
these are squares. So `E[p_new(E)|past]=p(E)`, and u is unchanged. A step with
`a=0` leaves the atoms with `ℓ∤M` unchanged. For `ℓ|M` it gives
`E[p_new]=(1+(−d_E|ℓ))p≤2p`, while `u` drops by 1.

(b) Let `τ_{ℓ,a}` be the time of the step at `(ℓ,a)` (∞ if never). Then
`logℓ·1[τ<∞] ≤ (logℓ/η)·w̃_{ℓ,a}(τ)1[τ<∞]`, where
`w̃_{ℓ,a}(i):=Σ_{v_ℓ(M)≥a+1}β^{s_i}p_i ≤ G^{(ℓ,a)}_i:=Σ_{v_ℓ(M)≥a+1}p_i2^{u_i}β^{ω(M)}`.
The process has at most `Σ_{ℓ≤Y}f_ℓ` steps, so the times are bounded. Optional
stopping for the nonnegative supermartingale `G^{(ℓ,a)}` gives
`E[G(τ)1[τ<∞]]≤G(0)`. Sum over `ℓ≤Y`, `a<v_ℓ(M)`, using
`Σ_{ℓ≤Y,a<v_ℓ}logℓ=log M_Y`. Also `p_0=P_H` (`M` odd, so the class mod 8 is irrelevant). The forced steps at 3, 5, 7 are not charged; they cost `log105`.

(c) Apply (a) with `φ=β^{ω(M)}`, and use `s_end≤ω`.

(d) ℓ is never stepped. So `p_i(E)=p_i(E^{(ℓ)})/φ(ℓ^{v})` and
`w̃_ℓ(end)²≤Σ_{E,E'∋ℓ}β^{ω+ω'}p(E)p(E')`. For a pair `(F,F')` define
`Π_i:=p_i(F)p_i(F')R_i`, with

* `R_i:=∏ρ` over the coordinates ℓ' shared by the supports;
* `ρ:=` the number of classes mod `ℓ'^{j}` in the current fibre, where `j≤min(v,v')` is the
  agreement depth (the largest j with `x_F≡x_{F'} mod ℓ'^j`); `ρ=1` if the current level is `≥j`.

Then `p p'≤Π`, and `Π_i2^{u_i(F)+u_i(F')}` is a supermartingale. Check, at a step
revealing a level of ℓ':

* *ℓ' constrains neither event:* nothing changes.
* *ℓ' constrains only one event at this level:* that event's factor behaves as in
  (a), and its ρ is already 1.
* *Both constrain ℓ' at this level and agree:* both are multiplied by the same
  `N·1[match]`, where N is the number of classes of the current fibre at this level
  (`ℓ'−1` if `a=0`, `ℓ'` if `a≥1`; R48a m1), and ρ is divided by N. So `Π→N·1[match]Π`. Its mean is Π for `a≥1`, and `(1+(−d|ℓ'))Π≤2Π` for `a=0`.
  In the latter case both u's drop.
* *Both constrain ℓ' and disagree at this level* (level `j+1`): both cannot match, so `Π→0`.

(Depth j is used for tightness only. With depth `min(v,v')`, Π is also a supermartingale, because
the disagreement step kills it (R48a m2).) At the start `R_0=∏φ(ℓ'^{j})≤φ(gcd)`.

So `E[Π_end]≤2^{u_0+u_0'}Π_0≤2^{ω_Y+ω_Y'}P_H(F)P_H(F')·φ(gcd(M_F,M_{F'}))`. Apply this
with `F=E^{(ℓ)}`, `F'=E'^{(ℓ)}` and multiply by `φ(ℓ^v)^{−1}φ(ℓ^{v'})^{−1}`. The final
claim is Chebyshev plus a union bound. ∎

*Remark.* (d) is the reason for the random class. The second moment of a *late*
mass is controlled by a Haar pair-correlation sum `B_2(ℓ)`, which is a deterministic
divisor sum with no g in it. For the class of one, the analogous quantity carries
the g-inflation.

**Notation.** `H(M):=β^{ω(M)}2^{ω_Y(M)}` and `w(M):=τ(A_M²)H(M)·M/φ(M)`. Summing over D,
`Σ_{D|A_M²}H(M)P_H(E_{M,D})=w(M)/M`. All sums run over `M≤T`, `M≡3 (4)`.

**Lemma 3.3 (the analytic inputs).**

(A) *PROVED modulo the Nair–Tenenbaum bound NT.* Take `β=1+1/log𝓛` and `Y≤T`. Then

* `S_H^β=Σ_M w(M)/M ≪ 𝓛³logY`;
* `Σ_E P_H(E)2^{ω_Y}β^{ω}log M_Y ≪ 𝓛³(logY)^4`.

NT is Nair–Tenenbaum's Theorem 1, as quoted in Henriot, arXiv:1102.1643, (1.1). We
use it with `k=2`, `Q_1(n)=n`, `Q_2(n)=4n−1` (fixed coefficients, no fixed prime
divisor, `ρ(p)=2` for odd p). The function is `F(n_1,n_2)=τ(n_1²)·f_2(n_2)`, where
f_2 is multiplicative with `f_2(p^k)≤8^k`.

(B) *PROVED, elementary.* For every `Y≥2`,

```
Σ_{ℓ>Y prime} B_2(ℓ) ≤ ((𝓛+1)/Y)·Ξ,      Ξ := Σ_M w(M)²τ(M)ω(M)/M ≪ 𝓛^{C_0},
```

with an absolute `C_0` (R48b D3). Explicitly, `C_0=81/2+8+o(1)`:
* `Στ(n²)^4/n≍𝓛^{81}`;
* `g²=H^4(m/φ)^4τ^4` has `f(p)≤16·16β^4` at `p≤Y`, which gives a factor `(logY)^{O(1)}`;
  at `p>Y` it has `f(p)=16β^4`.

The factor `(logY)^{O(1)}=(log𝓛)^{O(1)}` is absorbed. **Uniformity in Y (R48a m5):** Ξ's bound uses
only `2^{ω_Y}≤2^{ω}`, so it is uniform in `Y≤T`. The later choice `Y=𝓛^{C_0+4}` is therefore not circular.

*Proof of (A).*
* *First display.* Write `n=A`, `M=4n−1`, and `f_2(m)=H(m)m/φ(m)`. NT on
  `x<n≤2x` gives
  `≪x·∏_{p≤x}(1−ρ(p)/p)·Σ_{n_1≤x}τ(n_1²)/n_1·Σ_{n_2≤x}f_2(n_2)/n_2`. This is
  `≪x(log x)^{−2}(log x)³·(log x)^{β}(logY)^{β} ≪ x(log x)²logY`, since
  `(log x)^{β−1},(logY)^{β−1}≤e` (R48b D3). Divide by `M≍x` and sum over the `O(𝓛)` dyadic blocks.
* *Second display (R48b D1).* Use `log M_Y≤logY·Ω_Y(M)≤logY·τ(M_Y)`. This holds because
  `Σk_i≤∏(k_i+1)−1`. Then repeat with `f_2·τ_Y`. Here `τ(p^k)=k+1≤B_εp^{kε}` for every ε,
  so `F∈M_2(A,B_ε,ε)` uniformly in T (`β≤2`). (The earlier weight `(3/2)^{Ω_Y}` violated the NT
  class.) The Euler factor at `p≤Y` is `≈1+4β/p`, so `Σf_2τ_Y/n≪(logY)^{3}log x`. The
  bound `≪𝓛³(logY)^4` follows. ∎

*Proof of (B).*
* *Reduce to `V(q)`.* With `M=ℓm`, `M'=ℓm'`, we have
  `gcd(M,M')/ℓ^{min v}|gcd(m,m')`, so `φ(·)≤gcd(m,m')=Σ_{e|(m,m')}φ(e)`. Hence
  `B_2(ℓ)≤Σ_eφ(e)V(eℓ)²`, with `V(q):=Σ_{q|M}w(M)/M=Σ_{k≤T/q}w(qk)/(qk)`.
* *Cauchy–Schwarz in k* gives `V(q)²≤(𝓛+1)Σ_k w(qk)²/(q²k)`.
* *Regroup by `N=eℓk`.* The term `φ(e)w(N)²/(e²ℓ²k)` equals
  `(w(N)²/N)·φ(e)/(eℓ)≤(w(N)²/N)/ℓ`. The number of factorisations `N=eℓk` with
  ℓ fixed is `≤τ(N)`. So
  `Σ_{ℓ>Y}B_2(ℓ)≤(𝓛+1)Σ_N(w(N)²τ(N)/N)Σ_{ℓ|N,ℓ>Y}1/ℓ≤((𝓛+1)/Y)Ξ`.
* *Bound Ξ.* Cauchy–Schwarz separates the variables:
  `Ξ≤(Σ_{n≤T}τ(n²)^4/n)^{1/2}(Σ_{m≤4T}g(m)²/m)^{1/2}`, with
  `g=H²(m/φ)²τ²` (using `ω≤τ`). Both are mean values of multiplicative functions
  with `f(p^k)≪(k+1)^{O(1)}` and `f(p)=O(1)`, hence `≪𝓛^{O(1)}`, by the Euler
  product `∏_{p≤x}(1+f(p)/p+…)`. ∎

**Theorem 3.4 (Haar exponent 3; PROVED modulo NT).** Let `δ*(T)` be the Haar
probability that n avoids all events with `M≤T`. We use POINTWISE_HAAR §0's
normalisation (R48a m3, R48b D2): Haar measure on `{n∈Ẑ^×: n≡1 (24)}`. On all of `Ẑ^×`,
the value is exactly half of this, because the atom `M=3, D=1` kills `n≡2 (3)`.
Then

```
log(1/δ*(T)) ≪ 𝓛³(log𝓛)^5.
```

Only NT is used, and no Elsholtz–Tao input (R48b D6): all masses are Haar masses.

With POINTWISE_HAAR Thm 2.1 (`≫𝓛³/log𝓛`), this gives `log log(1/δ*) = (3+o(1))log𝓛`,
so the Haar exponent is `a=3`.

*Proof.* Take `β=1+1/log𝓛`, `η=(3/4)logβ≍1/log𝓛` and `Y=𝓛^{C_0+4}`. Run the
square-class process.

* *Bad events.* By Lemma 3.2(b,c) and Lemma 3.3(A),
  `E[log Q_end]≪(1/η)𝓛³(logY)^4` and `E[S_res]≪𝓛³logY`. By Lemma 3.2(d) and
  Lemma 3.3(B), `P(some ℓ>Y has w̃_ℓ>η)≤η^{−2}(𝓛+1)𝓛^{C_0}/Y≤1/4` for large T. By
  Markov, the events `{log Q_end>4E}` and `{S_res>4E}` each have probability `≤1/4`.
* *A good realisation.* So some realisation `(Q,r)` avoids all three bad events.
  In it:
  * every coordinate satisfies (1.1): coordinates `≤Y` because the process
    stopped, the others by the choice of realisation;
  * no event is deterministic (Lemma 3.1).
* *Conclusion.* Lemma 1.1 on the fibre `n≡r (Q)` gives
  `δ*≥(φ(24)/φ(Q))exp(−(4/3)S_res)`, since `r≡1 (24)`.
* *Explicit size.* `log φ(Q)≪(1/η)𝓛³(logY)^4≪𝓛³(log𝓛)^5` and `S_res≪𝓛³log𝓛`. ∎

This is the brief's item (iii), in sharper form than `𝓛^4`. It improves O12
Thm 6.3's `log(1/δ*)≪𝓛^5log𝓛`, and it settles POINTWISE_HAAR Conj 3.1 up to
logs.

**Corollary 3.5 (prime side; CONDITIONAL on the interface checks I1–I3).**

* *What changes.* In O11 Thm 3.2's assembly:
  * the quarantine `(Q,r)` comes from Theorem 3.4's realisation;
  * `log Q≪𝓛³(log𝓛)^{O(1)}`;
  * the residual system satisfies (1.1);
  * the residual mass is `S_res≪𝓛³(log𝓛)^{O(1)}`.
* *Junta.* O11 Cor 1.2 then gives `O(𝓛(S_res+𝓛))≪𝓛^4(log𝓛)^{O(1)}`.
* *Conclusion.* `log Z≪𝓛^4(log𝓛)^{O(1)}`. Hence
  `W(p)≥exp(c(log p)^{1/4}(log log p)^{−B})` for infinitely many Mordell-hard p,
  modulo (G), NT, and OMEGA10 Thm 3.4. Elsholtz–Tao is no longer needed (R48b D6).

The checks:

* **I1.** O8's BRW minorant (Lemma 3.1 / Thm 3.4) and O8 Lemma 3.3 (twist) run with
  Lemma 1.1's `x_E=β^sP(E)`, the conditional bound `≤x_E`, and coordinate sums `≤η`,
  instead of `2P(E)` and 1/32. Note that `η≍1/log𝓛` is *smaller* than 1/32.
* **I2.** O11 Cor 1.2's junta bound applies to this residual system. Its hypotheses
  are the edge weights `∏λ^{2v}` and `S`. They do not mention the class.
* **I3.** O11 Lemma 3.1 holds for the coset `rH` with r a square, `r≡1 (8)`:
  * every real character χ that is trivial on H has `χ(r)=1`;
  * cells are consistent with `r` mod `gcd(d_i,Q)` instead of with 1;
  * p is Mordell-hard because r is a square mod 840.

These are checks of interfaces written for the class of one, not new mathematics. They have not been done.
The junta `𝓛·S` is now the sole bottleneck. A junta `≪S·(log𝓛)^{O(1)}` (brief item (ii)) would push
the conditional prime exponent to `1/3`.

## 4. Status (checkpoint 1)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | β-weighted LLL: per-coordinate threshold `η=(3/4)logβ` | PROVED |
| Lemma 1.2 | threshold-η quarantine cost `(1/η)Σβ^ω s Λ_st` | PROVED |
| LPL(Y), M(Y), Prop 1.3 | class-of-one route | CONJECTURE / CONDITIONAL (superseded by §3) |
| Lemma 2.1, Cor 2.2 | heavy late primes quarantined ⇒ only the second moment V2 is needed | PROVED reduction / CONDITIONAL |
| §2 table | `Σ_{ℓ>Y}V♯²` below heuristic; pointwise `ℓV♯/S♯` grows | EVIDENCE |
| Lemma 3.1 | event classes `−4D mod M` have Jacobi symbol −1; Legendre `=(−d|ℓ)` | PROVED (+ check to 2·10⁵) |
| Lemma 3.2 | square-class process: supermartingales, cost, mass, late second moment `B_2` | PROVED |
| Lemma 3.3 | (A) Haar-weighted masses `≪𝓛³polylog`; (B) `Σ_{ℓ>Y}B_2≤(𝓛+1)Ξ/Y`, `Ξ≪𝓛^{O(1)}` | (A) PROVED mod NT; (B) PROVED |
| Thm 3.4 | `log(1/δ*(T))≪𝓛³(log𝓛)^5` (HAAR normalisation); Haar exponent a=3 | PROVED mod NT (Nair–Tenenbaum) |
| Cor 3.5 | (superseded by Thm 5.1) | — |
| §5 I1–I3 | BRW/EL, twist (`η≤0.19`), junta, coset transfer + (I) | PROVED (I3 mod (G)) |
| Thm 5.1 | `W(p)≥exp(c(log p)^{1/4}(loglog p)^{−1/4})` i.o.; `log L_h(T)≪𝓛^4log𝓛` | PROVED mod (G), NT, OMEGA10 Thm 3.4 (no ET) |

Not claimed: anything about ES itself; optimality of 1/4 (the junta `𝓛·S` is the bottleneck; heuristic truth 1/3).

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 900  uv run python scripts/omega13_inflation.py 100000)   # §1 EVIDENCE   -> data/omega13/inflation.txt
(ulimit -v 8000000; timeout 1800 uv run python scripts/omega13_v2.py 1000000)         # §2 EVIDENCE   -> data/omega13/v2.txt (~4 min)
(ulimit -v 8000000; timeout 900  uv run python scripts/omega13_jacobi.py 200000)      # Lemma 3.1     -> data/omega13/jacobi.txt
```

## 5. The interface checks I1–I3 (written out after R48a/R48b)

**Setting.** Fix the good realisation `(Q,r)` of Theorem 3.4. It has:
* `840|Q`, with r a square mod every prime of Q and `r≡1 (24)`;
* (1.1) at every coordinate, with `η≤0.19` (true for `T≥e^{33}`, §1 Range);
* `S_res=Σ_Eβ^{s(E)}P(E)≪𝓛³log𝓛` and `log Q≪𝓛³(log𝓛)^5`.

`F` is the indicator of avoiding all live events on the fibre `rH`, `H:={x≡1 (Q)}`, and
`δ:=E_{rH}F≥exp(−(4/3)S_res)` (Lemma 1.1). The events are single-valued congruences on fibre
coordinates, and there are `m≤T²` of them (atoms), as in O11 Thm 3.2.

**I1(a) (BRW minorant and EL; PROVED).** O8 Lemma 3.1 is pure algebra, valid for any events
`A_j` and functions `u_j`. Take `u_j` as in O11 Cor 1.2, with S replaced by `S_res` in τ:
`τ:=2𝓛⌈log₂(100m²(S_res+1)e^{3S_res})⌉`. Then EL_mod(τ) gives

```
E[F−B] ≤ m²Σ_jP(E_j)·e^{−3S_res}/(100m²(S_res+1)) ≤ e^{−3S_res}/100 ≤ δ/100,
```

using `ΣP(E_j)≤S_res` and `δ≥e^{−(4/3)S_res}`. So `μ:=E_{rH}B≥0.99δ`, and O9 Lemma 2.1 gives
`A≤1.03` verbatim. Only `E[F−B]≤δ/100` is used there.

**I1(b) (twist; PROVED).** Let ψ be real primitive of conductor `f>1`, with `gcd(f,Q)=1` and
`f|d_i` for some i. Fix a prime `ℓ_0|f`. Then `a_{ℓ_0}=0`, and `ℓ_0` is a coordinate
(`ℓ_0≤T`, `ℓ_0≠ℓ_aux`, as in O11 Thm 3.2). Follow O8 Lemma 3.3:
`|E[Fψ]|≤Σ_{E∋ℓ_0}p_{ℓ_0}(E)P(E∖ℓ_0∩F')`, where F' is the indicator of avoiding the
events not involving `ℓ_0`. That subfamily inherits (1.1). Lemma 1.1's general conditional bound
for `A=E∖ℓ_0` (`|supp A|=s(E)−1`) gives `P(E∖ℓ_0|F')≤β^{s(E)−1}P(E∖ℓ_0)`. Hence

```
|E[Fψ]| ≤ β^{−1}Σ_{E∋ℓ_0}β^{s(E)}P(E)·E F' = β^{−1}w̃_{ℓ_0}E F' ≤ η E F'.
```

The same bound gives `E F≥(1−η)E F'`. So
`|μ_ψ|≤E|B−F|+|E[Fψ]|≤(0.01+η/(1−η))E F≤(0.01+0.235)μ/0.99≤μ/4` for `η≤0.19`.

`E|B−F|=E[F−B]` holds because `B≤F` pointwise. The identity `μ_ψ=E[Bψ]` for any cell
representation needs only that ψ is primitive with f odd squarefree, as in O8.

**I2 (junta; PROVED).** Use O11 Lemma 1.1 and Cor 1.2 (digit filtration). These need only:
* independent coordinates whose digits above a first free digit `i_0(ℓ)` are uniform;
* events `∏ℓ^{v_ℓ}≤M≤T`, through the edge weights `∏λ_ℓ^{2v_ℓ}≤2`.

On the fibre `n≡r (ℓ^{a_ℓ})` the digits of index `≥a_ℓ` are uniform, exactly as for `r=1`.
The class r enters nowhere else, and conditioned systems are again initial segments. So the
cells of B have modulus `≤e^{2τ+3𝓛}`, i.e. `log max d_i≪𝓛(S_res+𝓛)`. Here `log m≤2𝓛` is
absorbed.

**I3 (linear transfer on the coset rH; PROVED modulo (G)).** O11 Lemma 3.1 holds with
`H={x≡1 (Q)}` replaced by `rH`, its hypotheses being:
* r is a square mod every odd prime of Q;
* `r≡1 (8)`;
* every cell is consistent with r, i.e. `b_i≡r (mod gcd(d_i,Q))`.

*Proof (changes only).* `c(χ)=E_{rH}[Bχ̄]/φ(Q)`.
* *Bounds and item 1.* `|c(χ)|≤Aμ/φ(Q)` as before. Consistency gives item 1
  (`cond χ≤Z`) verbatim.
* *Case A* (χ trivial on H). Then `c(χ)=χ̄(r)μ/φ(Q)`. For real χ this is a product of
  Legendre symbols at odd `p|Q` and a character mod 8. All of these are 1 at r, so
  `c(χ)=μ/φ(Q)`, identical to the class of one. Non-real χ enter O9 Thm 1.1 only through
  `|c(χ)|`.
* *Case B* (`f_2>1`). Unchanged: `c(χ)=ψ_1(r)E_{rH}[Bψ_2]/φ(Q)` with `|ψ_1(r)|=1`. The twist
  condition I1(b) applies to `ψ_2`.
* *Cell consistency.* Event cells have residue `−4D≡r (mod gcd(M,Q))` by survival. For the
  `u_j` (R48c m2): `E[F|X_W]` for a digit set W that is not an initial segment is still a
  function of `n mod m_W`, with `m_W` the *absolute* modulus (it includes the fixed fibre digits
  `<a_ℓ`). Its cells are fibre classes mod `m_W`, hence consistent with r. Since the weights are
  absolute, `log m_W≤τ` bounds the true modulus, so the `u_j`-moduli are `≤e^τ`. The rest of
  O11 Thm 3.2's argument applies.

*Property (I).* Let `n≡r (Q)` and `n≡−4D (M)` for an atom. Then the atom survives. If
`M|Q`, then `r≡−4D (M)`, which Lemma 3.1 excludes. Otherwise the event is live and occurs.
So `B≤F≤1[W(n)>T]` on `rH`. Mordell-hardness: r is a square mod 840. ∎

**Theorem 5.1 (exponent 1/4; PROVED modulo (G), NT, and OMEGA10 Thm 3.4).** For infinitely
many Mordell-hard primes p,

```
W(p) ≥ exp( c·(log p)^{1/4}·(log log p)^{−1/4} ),     uniformly  log L_h(T) ≪ 𝓛^4 log𝓛.
```

*Proof.* O11 Thm 3.2's assembly, with these substitutions:
* the realisation `(Q,r)` of Theorem 3.4 in place of Lemma 2.2's Q;
* I1(a) for the BRW minorant and EL;
* I1(b) for the twist;
* I2 for the junta;
* I3 with O9 Lemma 2.1 and the auxiliary prime `ℓ_aux∈(R,2R]` appended to Q, for the
  transfer.

*The class at `ℓ_aux` (R48c m1 = R48d D1).* The transfer runs on `Q':=Qℓ_aux` and the class
`r'` with `r'≡r (Q)` and `r'≡1 (ℓ_aux)` (CRT), on the coset `r'H'`, `H':={x≡1 (Q')}`. I3's
hypotheses hold for `(Q',r')`:
* `r'` is a square mod every odd prime of `Q'`; at `ℓ_aux` it is 1;
* `r'≡1 (8)`;
* cells are consistent: `ℓ_aux>R≥max d_i` is prime, so `gcd(d_i,Q')=gcd(d_i,Q)`.

The last point also shows that no atom or cell sees `ℓ_aux`. The transfer gives a prime
`p≡r' (Q')`, so `p≡1 (ℓ_aux)`. As `p≠1`, `p>ℓ_aux>R≥T`, exactly as in O9 Thm 2.2. This is
needed for infinitely many *distinct* p as `T→∞`: `W(p)>T` alone does not force `p>T`.

Then `log Z≤log Q+log ℓ_aux+log max d_i≪𝓛³(log𝓛)^5+𝓛(S_res+𝓛)≪𝓛^4log𝓛`. So some hard
`p>T` with `W(p)>T` has `log p≪𝓛^4log𝓛`. ∎

The bottleneck is the junta `𝓛·S_res`. The quarantine contributes only `𝓛³(log𝓛)^5`. Elsholtz–Tao
is not used. This supersedes Cor 3.5 (CONDITIONAL) and O12 Thm 6.3 (1/5).
