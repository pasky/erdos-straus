# An explicit rate beyond fixed powers: `W(p) ≥ (log p)^{k(p)}` with `k(p)→∞`

Task O6. Labels follow the house rules. ES is not solved here or anywhere;
nothing below bears on whether `W(p)<∞`. Notation as in `POINTWISE_OMEGA.md`
(PO), `POINTWISE_OMEGA2.md` (O2) and `POINTWISE_OMEGA3.md` (O3). `𝓛=log T`;
`log_j` is the j-fold iterated logarithm.

**Results at a glance.** *(filled in at the end)*

## 0. What is made explicit

O3 Thm 5.1 (k-level minorant) asserts constants `C_k, A_k` with
`log(M_1/μ) ≤ C_kŜ^{A_k}`, without values; O3 Thm 5.2 feeds this into
PO Thm 4.1 for each fixed k. Here every constant of O3 Thm 5.1 is
tracked (§1), the ES instantiation is made explicit in k (§2), k is let
grow with T (§3), the bottleneck is isolated (§4), and the Haar side is
compared (§5). No step of O3's proof is changed; §1 is pure bookkeeping
on the proof as written (and reviewed twice) in O3 §5.

Fixed constants throughout (as in O3): `w=16`, `1+w'=17e^{1/2}`,
`δ=e^{−50}`, `δ_r=[4er(1+w')^r]^{−1}`. For `k≥3` put

```
δ_* := δ_k = min_{r≤k} δ_r,     β_k := 8k·2^k/δ_* = 32e·k²·(34e^{1/2})^k,
b_k := 2 log β_k + log(3k)  ≤  8.06k + 5 log k + 10.1,
A_k(Ŝ) := (k−1)!·( log(3Ŝ+k+1) + b_k ).
```

(`log β_k = log(32e)+2log k+k log(34e^{1/2}) ≤ 4.47+2log k+4.027k`.)

## 1. The k-level minorant with explicit constants (PROVED)

**Theorem 1.1 (O3 Thm 5.1, explicit).** Let `k≥3` and `Ŝ≥1`. Take a system
as in O3 Setting 5.0 (events of support `≤k`, all vertices classes mod
`ℓ^{e_ℓ}`), with (I) of O2 Thm 3.1, total mass `≤Ŝ`, and per-prime total
mass `≤c_k(Ŝ) := k^{−2}e^{−56−2A_k(Ŝ)}`. Then the minorant B of O3 Thm 5.1
(twist condition of PO Thm 4.1 included) satisfies

```
K := 1+log(M_1/μ) ≤ e^{102+A_k(Ŝ)},     #free prime powers per modulus ≤ e^{102+A_k(Ŝ)}.
```

So `log K ≤ (k−1)!·(log(3Ŝ+k+1) + 8.06k + 5log k + 10.1) + 102`.

*Proof.* We run O3's proof verbatim and only bound its parameters. Recall
(O3 §5): levels `r=k,…,3` are processed top-down; at level r with frozen
mass `Σ_r` (original level-r events plus everything pushed in from
above),

```
H_r = k·Σ_{s>r}(L_s+1),   Λ_r = (Σ_r+H_r+1)/(2δ_r),   𝔐_{r+1} = ∏_{s>r}4e^{Λ_s},
L_r = least with 4^{L_r+1} ≥ 200k·𝔐_{r+1}·e^{H_r/2+Λ_r+3Ŝ_{≥r}},   N_r = r(L_r+1)+H_r,
```

`Ŝ_{≥r}=Σ_{s≥r}(Σ_s+1)`. Vertices of level-r degree `>δ_r/2` are pushed
to singles, and j-sets (`2≤j≤r−1`) with level-r codegree
`>δ_r(4N_r)^{−(j−1)}/(2r)` are pushed to level j (level 2 holds singles
and edges). Finally level-2 vertices of degree `>δ` become singles.

**Step 1 (one potential).** Put

```
Ẑ_r := Σ_r + H_r + Σ_{t>r}Λ_t + Ŝ_{≥r} + Ŝ + k.
```

* *Ẑ is monotone:* `Ẑ_{r−1}−Ẑ_r ≥ Λ_r−Σ_r ≥ 0`, since `Λ_r≥Σ_r/(2δ_r)`.
  So `Ẑ_s≤Ẑ_r` for `s≥r`.
* *Level-r parameters:* `Λ_r≤Ẑ_r/(2δ_r)`, and from the definition of
  `L_r`, with `log𝔐_{r+1}≤k log4+Σ_{t>r}Λ_t`,
  `(L_r+1)log 4 ≤ log(800k)+2k+3Ẑ_r+Ẑ_r/(2δ_r) ≤ Ẑ_r/δ_r` (as `Ẑ_r≥k≥3`
  and `1/δ_r>10^5`). Hence `L_r+1 ≤ Ẑ_r/δ_*` and
  `4N_r ≤ 4kẐ_r/δ_*+4Ẑ_r ≤ 8kẐ_r/δ_*`.
* *Markov push (O3 §5 Step A).* `Σ_{|O|=j}P(O)Δ^{(r)}_O=binom(r,j)Σ_r`, and
  at a prime ℓ, `Σ_{O∋v@ℓ,|O|=j}P(O)Δ^{(r)}_O=binom(r−1,j−1)w^{(r)}_ℓ`.
  Dividing by the thresholds, the mass pushed from level r into size j is
  at most
  `2^k·(2k/δ_*)·(8kẐ_r/δ_*)^{j−1}·Σ_r ≤ (β_kẐ_r)^j`, and the per-prime mass
  at ℓ is at most `β_k^jẐ_r^{j−1}w^{(r)}_ℓ` (`1≤j≤r−1`; `j=1` = singles).

**Step 2 (the recursion).** Level `r−1` is frozen after all levels `s≥r`
have pushed into it, so `Σ_{r−1} ≤ Ŝ + Σ_{s≥r}(β_kẐ_s)^{r−1} ≤ Ŝ+k(β_kẐ_r)^{r−1}`.
With `H_{r−1}=H_r+k(L_r+1)`, `Σ_{t≥r}Λ_t=Σ_{t>r}Λ_t+Λ_r` and
`Ŝ_{≥r−1}=Ŝ_{≥r}+Σ_{r−1}+1`:

```
Ẑ_{r−1} ≤ Ẑ_r(1+(k+1)/δ_*) + 2Σ_{r−1} + 1 ≤ (2k+3)(β_kẐ_r)^{r−1} ≤ 3k(β_kẐ_r)^{r−1},
```

using `β_k ≥ 1+(k+1)/δ_*` and `β_kẐ_r ≥ 2Ŝ+1`. Put `z_r:=log Ẑ_r+b_k`. Then
`z_{r−1} ≤ (r−1)z_r` for `3≤r≤k`: this is
`(r−2)b_k ≥ (r−1)log β_k+log 3k`, which holds for `b_k=2logβ_k+log 3k`
and `r≥3`. Since `Ẑ_k ≤ 3Ŝ+k+1` (`H_k=0`, `Σ_k≤Ŝ`),

```
z_r ≤ z_k·(k−1)!/(r−1)!,    in particular   log Ẑ_2 ≤ (k−1)!z_k − b_k = A_k(Ŝ) − b_k.
```

**Step 3 (level 2 and the outputs).** `Ẑ_2` bounds the frozen level-2
mass `S_1+S_2`, `H_2`, `Σ_{t>2}Λ_t` and `Ŝ_{≥2}`. The final degree push
gives `S_1^{new}≤S_1+2S_2/δ≤3e^{50}Ẑ_2`, so (O3 Step B, level 2)
`Λ_2 = 16(S_1^{new}+δH_2)+16e^{98}S_2 ≤ 17e^{98}Ẑ_2`, the final total mass
is `Ŝ_tot ≤ 4e^{50}Ẑ_2`, and `L_2+1 ≤ [log(800k)+2k+Σ_{t>2}Λ_t+Λ_2+3Ŝ_tot]/log 4 ≤ e^{101}Ẑ_2`.
Therefore

```
K ≤ 1 + log𝔐_2 + log(1/μ) ≤ 1 + 2k + Σ_{t>2}Λ_t + Λ_2 + 3Ŝ_tot + 1 ≤ 18e^{98}Ẑ_2 ≤ e^{101}Ẑ_2,
#primes per cell ≤ Σ_{s≥3}s(L_s+1) + 2(L_2+1) ≤ H_2 + 2e^{101}Ẑ_2 ≤ e^{102}Ẑ_2,
```

using `log(1/μ) ≤ 3Ŝ_tot+1` (O3 Thm 5.1). With Step 2 this is the claim.

**Step 4 (per-prime condition (P_k)).** Let `m^{(r)}` be the maximum over
ℓ and over levels `j<r` of the level-j mass at ℓ after levels `≥r` are
processed (`m^{(k+1)}≤c:=c_k(Ŝ)`); the frozen level-r mass at ℓ is
`≤m^{(r+1)}`. By Step 1, `m^{(r)} ≤ m^{(r+1)}(1+β_k^{r−1}Ẑ_r^{r−2}) ≤ 2β_k^{r−1}Ẑ_r^{r−2}m^{(r+1)}`.
Writing `log Ẑ_r=z_r−b_k`, using `(r−1)logβ_k−(r−2)b_k≤0` and Step 2,

```
log(m^{(3)}/c) ≤ Σ_{r=3}^k [log 2 + (r−2)z_r] ≤ k + (k−1)!z_k·Σ_{r=3}^k (r−2)/(r−1)! ≤ k + A_k(Ŝ),
```

since `Σ_{r≥3}(r−2)/(r−1)! = Σ_{r≥3}(1/(r−2)!−1/(r−1)!) = 1`. At the end,
levels `≥3` have per-prime mass `≤m^{(3)}` each, and level 2 has
`≤m^{(3)}(1+e^{50})` (degree push, Markov per prime). The total is
`≤e^{51}k·m^{(3)} ≤ e^{51+k+A_k}k·c ≤ 1/(64k)`, because `k≤A_k`. This
is (P_k), which is all O3 Step B and the twist step use. ∎

*Remarks.*

* The factorial is exactly O3's "downward polynomial amplification": a
  push from level r into size j costs `Ẑ_r^j`, and the worst chain is
  `k→k−1→…→2`. §4 discusses whether it is intrinsic.
* `b_k=O(k)` carries the `e^{O(r)}` constants `δ_r`, `2^r`; they enter
  only additively inside the factorial.

## 2. The ES instantiation, explicit in k (PROVED modulo Thorner–Zaman)

**Construction 2.0.** Fix `k≥3` and T. Put `y:=2T^{1/(k+1)}` (so `y^{k+1}>T`),
`Π_0:={ℓ≤y}`, `Ŝ:=S*+1` with `S*` the uniform mass of O2 Lemma 11.1, and
`c:=c_k(Ŝ)` (Thm 1.1). Run O2 Lemma 11.2 from `Π_0` with `z=y` and
threshold c: it stops at `Π=Π_0∪𝓑` with `|𝓑| ≤ ⌊𝓛/log y⌋S*/c ≤ kŜ/c`.
Put `Q:=lcm(24,ℓ^{e_ℓ}:ℓ∈Π)`, `𝒫:={y<ℓ≤T}∖𝓑`, and form the events as in
O3 Construction 4.1. Every rough part `r≤T` has all prime factors `>y`,
so `Ω(r)≤k`: the system has supports `≤k`.

The only change from O3 Thm 5.2's construction is `y`: O3 used
`T^{1/k}exp(2𝓛/log𝓛)`, a factor inherited from O2 where it secured the
per-prime conditions (O2 Lemma 4.3 (W),(G)). With the iterated quarantine
those conditions come from Lemma 11.2, and the factor is not used:
O3 Lemma 4.2 needs only (I) (O2 Lemma 4.3 (I), which uses only that
`Π∋` every prime `≤y` and `ℓ^{e_ℓ}≤T`), the per-prime bound `≤c` (Lemma
11.2), the total mass `≤S*` (O2 Lemma 11.1), and the size of `log Q`.
For k growing with T the factor would be fatal (`2𝓛/log𝓛 ≫ 𝓛/k`).

**Theorem 2.1 (PROVED modulo Thorner–Zaman, via PO Thm 4.1; effective).**
There is an absolute effective constant `C_2` such that the following
holds. If `k≥3` and T satisfy

```
(C_{k,T})     A_k(S*+1) + log(C_2𝓛) ≤ 𝓛/(6k²),
```

then there is a Mordell-hard prime `p≡1 (mod 840)`, `p>T`, with
`W(p)>T` and `log p ≤ T^{1/k}`; in particular `W(p) > (log p)^k`.

*Proof.* Write `A:=A_k(Ŝ)`. O3 Lemma 4.2 holds verbatim for
Construction 2.0 (previous paragraph), so Theorem 1.1 applies:
`K ≤ e^{102+A}`, and every modulus `d_i` is a product of at most
`e^{102+A}` prime powers `≤T`, so `log max d_i ≤ e^{102+A}𝓛`. As in O3
Thm 4.3, take a prime `ℓ_0∈(R,2R]`, `R=max(T,max d_i)`, and replace Q by
`Qℓ_0`. Sizes:

* `π(y)𝓛 ≤ 1.26(y/log y)(k+1)log y = 1.26(k+1)y` (Rosser–Schoenfeld;
  `𝓛<(k+1)log y`);
* `|𝓑|𝓛 ≤ kŜ𝓛/c = k³Ŝe^{56+2A}𝓛 ≤ e^{56+4A}𝓛` (`k³, Ŝ ≤ e^A`);
* `log Z ≤ log Q + log 2R + log max d_i ≤ 2.52(k+1)T^{1/(k+1)} + e^{104+4A}𝓛`.

PO Thm 4.1 gives `p≡1 (Qℓ_0)` with `W(p)>T` and

```
log p ≤ C_1K·max(log Z,K) ≤ C_1e^{102+A}·[2.52(k+1)T^{1/(k+1)} + e^{104+4A}𝓛].
```

The first term is `≤T^{1/k}/2` iff `A+log(5.04C_1e^{102}(k+1)) ≤ 𝓛/(k(k+1))`;
the second is `≤T^{1/k}/2` iff `5A+log(2C_1e^{206}𝓛) ≤ 𝓛/k`. Both
follow from `(C_{k,T})` with `C_2:=6C_1e^{206}` (note `k+1≤𝓛`, and
`(C_{k,T})` forces `y≥7`). `840|Q`, so p is Mordell-hard, and
`p>ℓ_0>T`. ∎

## 3. Letting k grow: explicit rates (PROVED modulo the cited theorems)

Two bounds for `S*` are available (O2 Lemma 11.1):

* (U) unconditionally, `S* ≤ C log𝓛·𝓛³·τ*(T+2) = exp((log 2+o(1))𝓛/log𝓛)` (Wigert);
* (ET) modulo Elsholtz–Tao Prop. 1.4 (a published theorem, used as in
  PO Lemma 9.2), `S* ≪ 𝓛^4 log𝓛`.

`(C_{k,T})` reads `6k²(k−1)!(log(3S*+k+1)+b_k) + 6k²log(C_2𝓛) ≤ 𝓛`.

**Corollary 3.1 (PROVED modulo Thorner–Zaman and Elsholtz–Tao Prop. 1.4;
effective).** Put `κ(X):=max{k≥3 : 6k·k!·(6log X+9k) ≤ X}`, so
`κ(X)=(1+o(1))log X/log log X`. For infinitely many Mordell-hard p,

```
W(p) > (log p)^{κ(log log p)},   i.e.   log W(p) ≥ (1+o(1))·log₂p·log₃p/log₄p.
```

*Proof.* Under (ET), `log(3S*+k+1) ≤ 5log𝓛+O(1)` for `k≤𝓛`, and
`b_k ≤ 9k+C`. So for `k=κ(𝓛)` and T large, `(C_{k,T})` holds (the
`6log X` absorbs the constants and the `log(C_2𝓛)` term). Theorem 2.1
gives p with `W(p)>T≥(log p)^{κ(𝓛)}` and `log log p ≤ 𝓛/κ(𝓛) ≤ 𝓛`. Since κ is
nondecreasing, `κ(𝓛)≥κ(log log p)`. Distinct T give infinitely many p
(`p>T`). ∎

**Corollary 3.2 (PROVED modulo Thorner–Zaman; effective).** Put
`κ_0(X):=max{k≥3 : 5k·k! ≤ log X}`, so `κ_0(X)=(1+o(1))log₂X/log₃X`.
For infinitely many Mordell-hard p,

```
W(p) > (log p)^{κ_0(log log p)},   i.e.   log W(p) ≥ (1+o(1))·log₂p·log₄p/log₅p.
```

*Proof.* Under (U), `log(3S*+k+1) ≤ 0.7𝓛/log𝓛` for T large. For
`k=κ_0(𝓛)`, `6k²(k−1)!·0.7𝓛/log𝓛 = 4.2k·k!·𝓛/log𝓛 ≤ 0.84𝓛`, and the
remaining terms `6k²(k−1)!b_k+6k²log(C_2𝓛) = (log𝓛)^{O(1)}` are `≤0.16𝓛`.
Conclude as in Cor 3.1. ∎

*So the first target of the brief holds:* `W(p)/(log p)^k → ∞` along
infinitely many p with an explicit `k=k(p)→∞`. In uniform form,
`log L_h(T) ≤ T^{1/κ(𝓛)}` with `1/κ(𝓛) ~ log₃T/log₂T`:

**Corollary 3.3 (uniform form).** For all large T there is a hard prime p
with `W(p)>T` and `log log p ≤ 𝓛/κ(𝓛)` (under ET), resp. `≤𝓛/κ_0(𝓛)`
(unconditionally in the sense of Cor 3.2). So
`log log L_h(T) ≤ (1+o(1))𝓛·log₂𝓛/log𝓛`, resp. `≤ (1+o(1))𝓛·log₃𝓛/log₂𝓛`.

Comparison: O3 Thm 5.2 gives `log log L_h(T) ≤ 𝓛/k+O_k(𝓛/log𝓛)` for each
fixed k, i.e. `o(𝓛)` with no rate.

## 4. The bottleneck

### 4.1 Anatomy of the factorial (PROVED, about the scheme)

In Theorem 1.1 the factorial comes from one inequality only, the Markov
push (Step 1): the mass pushed from level r into size j is bounded by
`binom(r,j)Σ_r/t_j` with threshold `t_j=δ_r(4N_r)^{−(j−1)}/(2r)`, and
`N_r ≥ r(L_r+1) ≥ rΛ_r/log4 ≥ Σ_r/(2δ_r log 4)`. So the bound for the
new level-j mass is `≥ Σ_r^j`, and level j then needs its own
truncation `L_j ≥ Λ_j/log 4 ≥ Σ_j`, hence thresholds `(L_j)^{−(i−1)}` for
its i-subsets. Along the chain `k→k−1→…→2` the exponents multiply:
`log Σ_2 ≳ (k−1)!·log Ŝ`. Every other parameter (`H_r`, `Λ_r`, `𝔐`, the
twist, the per-prime masses) enters only through `Ẑ_r` and costs a
factor `3kβ_k^{r−1}`, i.e. the additive `b_k` in `z_r`.

Two facts locate the problem precisely.

* **Markov is sharp at the first push** (O2 Prop 11.4, O3 Prop 2.2): at
  level 3 the pairs of codegree `>t` have mass `≫(1/t)log(1/t)`, the
  Markov bound up to the log. So the first push cannot be made cheaper
  by better counting.
* **The cascade is an artefact.** The heavy sets are κ-monochromatic
  (all vertices `(ℓ_i, κ mod ℓ_i)` for one rational κ of small height;
  O3 §2 EVIDENCE for pairs; Prop 2.2 for the three families). A pushed
  κ-monochromatic j-set has level-j sub-codegrees `≍1`, so the scheme
  pushes it down step by step until its vertices `(ℓ,κ)` become singles
  — at a final cost `≈Σ_ℓ1/ℓ ≈ log(k+1)` per κ, not the product of the
  intermediate Markov bounds. Quarantining the hub classes directly
  (O3 §1) avoids the cascade. What is missing is an arithmetic statement
  that *nothing else* is heavy.

### 4.2 The precise sufficient input, and what it buys (PROVED implication)

For `H≥2` let `𝓗_H` be the hub set of O3 Def 2.3 (`−u/v`, `uv≤H`;
`−4sa²`, `sa≤H`; `−1/(4sb²)`, `sb≤H`). A vertex `(ℓ,x)` is an *H-hub* if
`x∈𝓗_H(ℓ^{e_ℓ})`.

**Hypothesis HC(a,B)** (hub codegree; open). For all large T, all
`3≤k≤𝓛^{1/2}`, every `Π⊇{ℓ≤2T^{1/(k+1)}}` and every `H≥2`: in the system of
Construction 2.0 for Π (supports `≤k`), with every event containing an
H-hub deleted, every vertex set O with `2≤|O|≤k−1` and no H-hub has
codegree `Δ_O ≤ 𝓛^B H^{−a}`.

Vertex *degrees* are not part of HC: they are enforced by Markov at cost
`kS_H/δ_k` (O2 Thm 10.3 step 1). EVIDENCE for `|O|=2`, `k=3` is O3 §2:
the maximum outside `𝓗_X` decays like `X^{−0.7}` at fixed T, with no
growth in T over `10^9…10^13`. Nothing is known for `|O|≥3`.

**Lemma 4.1 (transfer bookkeeping; PROVED modulo Thorner–Zaman).**
Suppose, for Construction 2.0 with some Π, `|Π∖Π_0|≤e^X`, and a minorant
for `1[W>T]` on `n≡1 (Q)` exists as in PO Thm 4.1 with `K≤e^X` and moduli
on `≤e^X` free prime powers. Then some hard `p>T` has `W(p)>T` and
`log p ≤ C_1e^X[2.52(k+1)T^{1/(k+1)} + e^{X+2}𝓛]`.

*Proof.* The size bullets of Theorem 2.1's proof with `e^X` in place of
`|𝓑|` and of the prime counts. ∎

**Theorem 4.2 (PROVED implication, modulo Thorner–Zaman and Elsholtz–Tao
Prop. 1.4).** If HC(a,B) holds, then for infinitely many Mordell-hard p

```
log W(p) ≥ c_a·(log log p)^{3/2},    c_a := 0.2·a^{1/2}.
```

*Proof.* Fix T and k, and let `δ_k:=[4ek·17^k]^{−1}` (O2 Thm 10.3).

1. *Base system.* Construction 2.0 with Lemma 11.2 threshold
   `c:=δ_k e^{−0.011k}/(64k)`, so `|𝓑| ≤ kŜ/c = e^{O(k)}Ŝ`.
2. *Hub quarantine.* Impose `X_ℓ∉𝓗_H(ℓ^{e_ℓ})` at every free ℓ by O3
   Thm 1.1/Cor 1.2 (decoupling) with the conditioned measure P′.
   `h_ℓ ≤ 3H(1+log H)/(ℓ−1) ≤ 1/100` since `ℓ>y≫H`, and
   `S_hub ≤ 3H(1+log H)(log(k+1)+1)` (Mertens over `y<ℓ≤T`). Under P′,
   events with an H-hub have measure 0, and `p′≤p·(100/99)`, so all
   masses and codegrees grow by at most `e^{0.011k}`.
3. *Main minorant.* O2 Thm 10.3 under P′ (O3 Lemma 1.3, which needs
   `h_ℓ≤1/100`). With `Ŝ′:=e^{0.011k}Ŝ`, its proof gives
   `Λ′+λ ≤ 22kŜ′/δ_k`, `L+1 ≤ 17kŜ′/δ_k`, so with `N:=17k²Ŝ′/δ_k ≥ k(L+1)`
   condition (CD_k) holds as soon as all `Δ^{(j+1)}≤η_k:=δ_k/(2N^{k−2})`.
   By HC this holds for `H:=⌈(𝓛^Be^{0.011k}/η_k)^{1/a}⌉`, and
   ```
   log(1/η_k) ≤ (k−1)(log Ŝ + 2.86k + 3log k + 6).
   ```
4. *Output.* Cor 1.2 of O3: `log(M_1/μ) ≤ 22kŜ′/δ_k + 3S_hub + 2`, primes
   per modulus `≤ k(L+1)+J+1 = O(K)`. So with ET (`log Ŝ ≤ 5log𝓛`),
   ```
   X := log K + O(1) ≤ (k/a)(2.86k + 5log𝓛 + 3log k + 6) + (B/a)log𝓛 + 2log log H + O(1).
   ```
5. *Optimise.* Take `k:=⌊(a𝓛/5.72)^{1/3}⌋`. Then `X ≤ 2.86k²/a + O(k log𝓛/a)`,
   and Lemma 4.1 gives
   `log log p ≤ max(X+𝓛/(k+1), 2X+log𝓛) + O(log k)`. Here
   `X = (0.5+o(1))(5.72/a)^{1/3}𝓛^{2/3}` and `𝓛/k = (1+o(1))(5.72/a)^{1/3}𝓛^{2/3}`,
   so `log log p ≤ (1.5+o(1))(5.72/a)^{1/3}𝓛^{2/3}`.
   Since `W(p)>T`, `log W(p) ≥ 𝓛 ≥ (1−o(1))(a/5.72)^{1/2}1.5^{−3/2}(log log p)^{3/2}`,
   and `(5.72)^{−1/2}1.5^{−3/2} = 0.227 > 0.2`. ∎

So the factorial of Theorem 1.1 is *entirely* the cascade: an arithmetic
codegree bound of polynomial strength in the hub height would replace
`(k−1)!` by `k²` in `log K`.

### 4.3 Ceilings of the method (Assessment)

Even with HC, three losses remain. Each is stated as the inequality
that causes it.

1. **Lemma 10.2 thresholds.** A j-set at a level with truncation L must
   have codegree `≲(k(L+1))^{−(j−1)}`. This is real for truncated
   expansions (O2 Lemma 10.2 remark: a cluster reusing j old vertices
   out of `≍kL` can be placed in `binom(kL,j−1)` ways, and the O2 D12
   example shows the true moment, not just the bound, is too large).
2. **Monochromatic hubs force `H ≳ (kL)^{k−2}`.** O3 Prop 2.2 extends
   verbatim to j-sets: for κ of height h, j primes `ℓ_i>y` with
   `∏ℓ_i ≤ T/y²` and one more prime `ℓ'≡` a fixed class mod `≍h` give
   `Δ ≳ c/φ(4h)`. (Uniformity in h needs primes in progressions to
   moduli up to `(kL)^k`, so this is an Assessment, not a theorem.)
   So the hub height must reach `(kL)^{k−2}`, and
   `log K ≥ log S_hub ≳ (k−2)·log(kL)`.
3. **`L ≥ e^{ck}Ŝ` from support truncation.** In O2 Lemma 1.2,
   `|B_L−1| ≤ binom(2N,L) ≤ 4^{L+1}binom(N,L+1)` counts *primes*. With
   per-prime weight `w≥4` this makes `Λ ≥ 2ek(1+w)^kS_H`, hence
   `L ≥ e^{ck}Ŝ` and item 2 costs `≳k²`. This loss is *not* intrinsic to
   truncation: for n disjoint events of support k, the true value is
   `B_L = (−1)^{⌊L/k⌋}binom(n−1,⌊L/k⌋)`, of size `≈2^{n}`, not `4^{L}`.
   An event-sensitive form of Lemma 1.2 (error `≤C^{#events}` for
   high-support events, keeping the prime count for hubs) would plausibly
   give `L ≤ k^{O(1)}Ŝ`.

Consequences (same bookkeeping as Thm 4.2):

* HC alone: `log K ≈ 2.86k²/a`, giving `log W ≍ (log₂p)^{3/2}` (Thm 4.2).
* HC plus `L≤k^{O(1)}Ŝ`: `log K ≈ (k/a)(log Ŝ+O(log k))`. With ET,
  `k≍(a𝓛/log𝓛)^{1/2}` gives `log log p ≲ (𝓛 log𝓛/a)^{1/2}`, i.e.
  `log W(p) ≳ a(log₂p)²/log₃p`. This is the brief's second target up to
  `log₃p`. The `log₃p` is the factor `log Ŝ≍log𝓛` in item 2; the exact
  form `exp(c(log₂p)²)` would need `log K=O(k)`, which item 2 rules out
  whenever `Ŝ→∞` (and `S_tot(Π)≍𝓛^{2.5}` numerically, PO §2).
* Unconditionally (no HC) the cascade gives Theorem 1.1's `(k−1)!`.

### 4.4 The third target is outside the method (Assessment, with a PROVED part)

`W(p) ≥ exp((log p)^c)` i.o. means `log p ≤ 𝓛^{1/c}` for some p with
`W(p)>T`.

* *PROVED part.* In any construction of this family, p ≡ 1 mod Q with
  `Q ⊇ ∏_{ℓ≤y}ℓ`, and PO Thm 4.1 gives `log p ≥ log Q ≥ θ(y)`. So
  `y ≤ 𝓛^{O(1)}`, and the events then have up to `k ≍ 𝓛/log𝓛` free
  primes.
* *Assessment.* With `k≍𝓛/log𝓛`, items 1–2 of §4.3 give
  `log K ≳ k log k ≍ 𝓛`. Then `log p ≥ K ≥ T^{c'}`, which is no better
  than the trivial range. So `exp((log p)^c)` needs a minorant whose
  ℓ¹-cost does not grow with the number of free primes per event, i.e.
  one that tracks the local lemma as the Haar side does (§5).

## 5. The Haar side, explicit in k (PROVED)

**Proposition 5.1.** For every `z≥2`, with `k_z:=⌊𝓛/log z⌋`,

```
log(1/δ*(T)) ≤ π(z)𝓛 + 8k_z²S*𝓛 + 4S*.
```

*Proof.* O2 Thm 11.3's proof with z free: Lemma 11.2 at threshold
`c_0=1/(8k_z)` gives `|𝓑|≤8k_z²S*`, and the local lemma gives
`P(no event) ≥ e^{−4S*}` under the class of one mod `Q_Π`. ∎

* The dependence on the number of free primes per event is
  **polynomial** (`k_z²`), against `(k−1)!` in the exponent on the prime
  side. The local lemma needs only per-prime smallness (`c_0=1/(8k)`),
  with no codegree condition and no truncation, so neither the cascade
  nor items 1–3 of §4.3 arise.
* With `z=𝓛²`: `log(1/δ*) ≪ 𝓛³(S*+1)`, i.e. `≪𝓛^7log𝓛` under ET (O2
  Thm 11.3). Under the density heuristic `log L_h(T) ≈ log(1/δ*(T))`
  (POINTWISE_SIZE RA; Assessment) this is the Haar form of the third
  target: `W(p) ≥ exp((log p)^{1/7−o(1)})`. The heuristic truth is
  `log W ≍ (log p)^{1/3}` (POINTWISE_SIZE §7).
* **The gap, quantitatively.** In the uniform form, the prime side now
  proves `log log L_h(T) ≤ (1+o(1))𝓛 log₂𝓛/log𝓛` (Cor 3.3, ET). The Haar
  side gives `log log(1/δ*) ≤ (7+o(1))log𝓛`. The prime side is weaker
  by a factor `≍𝓛/log₂𝓛` in the doubly logarithmic scale.
