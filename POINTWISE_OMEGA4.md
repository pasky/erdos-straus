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
