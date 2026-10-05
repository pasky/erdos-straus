# The junta bottleneck: a level barrier at `𝓛·S` (task O49)

Status: IN PROGRESS. Labels as in DISCOVERIES.md. Notation as in POINTWISE_OMEGA13.md (O13),
O11, O12: `𝓛=log T`; coordinates `X_ℓ∈ℤ_ℓ^×` (Haar); atoms `(M,D)`, `M≡3 (4)`, `M≤T`,
`A=(M+1)/4`, `D|A²`, event `E_{M,D}={n≡−4D (mod M)}`; F = indicator that no event holds.

## 0. Summary and the question

O13 Cor 3.5 pays `log Z ≍ log Q + 𝓛·S` (S = residual mass `≍𝓛³` up to logs), and the
`𝓛·S` is the cell modulus of the BRW minorant (O11 Cor 1.2). The brief asks for a minorant
of cell modulus `≪S·polylog`, or a proof that `𝓛·S` is forced.

Answer pursued here: **it is forced, for every minorant of bounded level, not only BRW.**
§1 proves an abstract *planting* barrier: if every event has one "big" coordinate of cost
`≥L`, and B is any combination of functions that each see at most k big coordinates, then
`B≤F` forces `E B ≤ E[F·1{R<(k+1)(1+o(1))}]`, where R is the conditional odds-mass of the
big events given the small coordinates. §2 applies it to ES (in progress).

## 1. The planting lemma and the abstract level barrier

**Lemma 1.1 (planting; PROVED).** Let `b_1,…,b_n` be independent bits with
`P(b_i=1)=p_i∈[0,1)`, law μ. Put `r_i:=p_i/(1−p_i)`, `R:=Σr_i`, `r*:=max r_i`. Let `k≥0` with

```
R ≥ (k+1) + (2k+1)·r* .                                                (1.1)
```

Then there is a probability law ν on `{0,1}^n` with the same marginals as μ on every set of
`≤k` coordinates, and `ν(b=0)=0`.

*Proof.* Write `1_y` for the configuration with ones exactly on `y⊆[n]`, `P_0:=μ(1_∅)=∏(1−p_i)`,
so `μ(1_y)=P_0∏_{i∈y}r_i`. Let `e_a(·)` be elementary symmetric functions. If
`e_{k+1}(r)=0` then fewer than k+1 of the r_i are positive and (1.1) fails (`R≤k·r*`); so
`e_{k+1}(r)>0`. For `|J|=k+1` put `w_J:=∏_{i∈J}r_i/e_{k+1}(r)` (so `Σ_Jw_J=1`) and

```
ν := μ + P_0 Σ_{|J|=k+1} w_J σ_J,      σ_J := Σ_{y⊆J} (−1)^{|y|+1} δ_{1_y}.
```

* *Marginals.* Fix K with `|K|≤k` and a pattern `z⊆K`. The σ_J-mass of `{x: x_K=1_z}` is
  `[z⊆J]·Σ_{y'⊆J∖K}(−1)^{|z|+|y'|+1}=0`, since `J∖K≠∅`. So ν and μ agree on K; in
  particular (K=∅) ν has total mass 1.
* *Zero.* `ν(1_∅)=P_0−P_0Σ_Jw_J=0`.
* *Positivity.* Only `|y|` even, `|y|=j≥2`, `y⊆J` gets negative charge, of total
  `P_0Σ_{J⊇y}w_J=P_0∏_{y}r_i·e_{k+1−j}(s)/e_{k+1}(r)`, `s:=r_{[n]∖y}`. Since
  `μ(1_y)=P_0∏_yr_i`, it suffices that `e_{k+1−j}(s)≤e_{k+1}(r)`. Now `e_{k+1}(r)≥e_{k+1}(s)`,
  and `e_n(s)≥e_{n−1}(s)` for `1≤n≤k+1`: each n-set arises n times as `I∪{i}`, `|I|=n−1`,
  `i∉I`, so `n·e_n(s)≥e_{n−1}(s)(Σs−(n−1)r*)`, and `Σs≥R−jr*≥R−(k+1)r*`, so
  `Σs−(n−1)r*≥R−(2k+1)r*≥k+1≥n` by (1.1). Chain `n=k+2−j,…,k+1`. ∎

*Remarks.* (i) This is the dual (LP) side of lower-bound sieves: Bonferroni/BRW-type
minorants of degree k exist only if no such ν exists. Close in spirit to
Benjamini–Gurel-Gurevich–Peled (arXiv:1201.3261) and Peled–Yadin–Yehudayoff (RSA 2011)
(k-wise independent laws and extremal all-ones probabilities; cited in
`reviews/novelty-audit-2026-10.md`). No novelty is claimed for Lemma 1.1; the proof is
self-contained. (ii) Sharpness up to constants: for Poisson-like counts with mean S,
Bonferroni of order `k+1≈e²S` already gives a positive minorant (truncation error `≤(eS/(k+1))^{k+1}≤e^{−7S}`), so in that model the threshold is `k≍S`.

**Setting 1.2.** A product probability space with independent coordinates split into
*small* ones `X_s` and *big* ones `(X_b)_{b∈𝔅}`. Each big b carries a cost `c_b≥L`. Let 𝓕 be a
family of events, each of the form `E={X_s∈Σ_E}∩{X_{b(E)}∈Γ_E}` with exactly one big
coordinate `b(E)`. For fixed `x_s`, put `Ω_b(x_s):=⋃_{E: b(E)=b, x_s∈Σ_E}Γ_E`,
`p_b(x_s):=P(X_b∈Ω_b(x_s))`, `r_b:=p_b/(1−p_b)`, `R(x_s):=Σ_b r_b(x_s)`. Let F be the
indicator that no event of a (larger) family 𝓔⊇𝓕 holds. The *k-big-junta space* `𝒱_k`
is the linear span of functions each depending on `X_s` and on at most k big coordinates.
If every function of cost `≤log D` (sum of `c_b` of the big coordinates it reads) is
allowed, then `𝒱_k` with `k=⌊log D/L⌋` contains them all.

**Theorem 1.3 (level barrier; PROVED).** In Setting 1.2 assume `p_b(x_s)≤p*<1` for all
b, x_s; put `r*=p*/(1−p*)`. Then every `B∈𝒱_k` with `B≤F` pointwise satisfies

```
E B ≤ E[ F · 1{R(X_s) < (k+1)+(2k+1)r*} ].
```

*Proof.* Build a law ν: draw `x_s` from the true law. If `R(x_s)≥(k+1)+(2k+1)r*`, take the
law ν_{x_s} of Lemma 1.1 for the bits `b_b:=1[X_b∈Ω_b(x_s)]` (marginals `p_b(x_s)`), and
given the bits draw each `X_b` independently from its true law conditioned on
`X_b∈Ω_b` (bit 1) or `X_b∉Ω_b` (bit 0). Otherwise draw the big coordinates from their true
(product) law. For a function φ of `x_s` and of big coordinates in K, `|K|≤k`: given `x_s`,
the bits on K are independent with the true marginals, so `(X_b)_{b∈K}` has its true
product law. Hence `E_νφ=Eφ` for all φ∈𝒱_k, so `E B=E_νB≤E_νF`. In the planted case some
bit is 1, so some `E∈𝓕` holds and `F=0`. In the other case ν coincides with the true
law conditionally on `x_s`. ∎

*Reading.* Under the true law, `E[F|x_s]≤∏_b(1−p_b(x_s))≤e^{−R(x_s)(1−p*)}`. So the
minorant can only "see" the part of the avoider mass where the big events have total
odds `<k+1+o(k)`. If the avoiders are (conditionally on F=1) still typical for R, with
`R≈m` (the big mass), then any `B∈𝒱_k` with `E B≥εE F` needs `k≳m`, i.e.
`log D≳L·m`. For ES, `L≍𝓛` and m≍S up to logs: this is the `𝓛·S` barrier. §2 makes the
"still typical" step rigorous for ES.

## 2. The ES instance: any bounded-level minorant needs `log D ≫ 𝓛^4/log𝓛`

**Setting 2.0.** Haar measure on `Ẑ^×`, restricted to a fibre `n≡r (Q)` (first, Q has
no prime factor in `(y,T]`; this covers O13 Thm 5.1's `Q'=Q·ℓ_aux`, whose primes are
`≤Y=𝓛^{C_0+4}` or equal to `ℓ_aux>T`, once `y≥Y`; general Q in Theorem 2.6). F = indicator that no ES event
with `M≤T` holds. *Level:* a function on the fibre has level `≤D` if it is a linear
combination of functions `n↦φ(n mod qQ)` with `q≤D`; this contains every character of
conductor `≤D` and every cell of modulus `≤D` (times the fibre). *Big* coordinates: the
`X_ℓ` with ℓ prime, `ℓ>T^{0.6}`. A modulus `q≤D` has fewer than `log D/(0.6𝓛)` such prime
factors, so level `≤D` functions lie in `𝒱_k`, `k:=⌊log D/(0.6𝓛)⌋` (Setting 1.2).

Fix `y∈[𝓛^5, 𝓛^A]` (A fixed) and `N_0:=𝓛²`. Write `D*:=∏p^{⌈v_p(D)/2⌉}` (POINTWISE_HAAR
§2: `D|A²⟺D*|A`, and each n is `D*` for exactly `2^{ω(n)}` integers D). The *big family*:

```
𝓕 := { E_{M,D} : M = vℓ ≤ T, ℓ prime > T^{0.6}, M squarefree with all prime factors > y,
                 M ≡ 3 (4), n := D* ∈ [N_0, T^{1/10}], n | A_M }.
```

𝓕 is a subfamily of POINTWISE_HAAR's family (there `√T≤M≤T`, same roughness and D-range,
with `𝓛^5` replaced by `y≥𝓛^5`; its Lemmas 2.3–2.4 only improve when y grows). So:
(F1) distinct `(M,D)` give distinct events, `P(E)=1/φ(M)`; HAAR Lemma 2.3 (local-lemma
loads `w_q:=Σ_{E∋q}P(E) ≤ 𝓛³/(2q)+4𝓛T^{−2/5}` for `q>y`) and HAAR Lemma 2.4
(`Δ(𝓕)≤C𝓛²`) hold for 𝓕. No prime of any M divides Q (they lie in `(y,T]`), so on the
fibre the coordinates used by 𝓕 are still independent and Haar.

**Lemma 2.1 (big family: one big coordinate, small big-odds; PROVED).** Each `E∈𝓕` has
exactly one big coordinate `ℓ=ℓ(E)`, and its other coordinates (primes of v) are small.
For every ℓ and every value of the small coordinates,
`p_ℓ(x_s) ≤ p*:=T^{−0.1}(1+𝓛)·2 ≤ T^{−0.09}` for large T.

*Proof.* `v=M/ℓ<T^{0.4}`, so v has no prime `>T^{0.6}`; M has at most one. For fixed ℓ the
events with `ℓ(E)=ℓ` number at most `#{v<T/ℓ}·#{D: D*≤T^{1/10}} ≤ T^{0.4}·T^{0.1}(1+𝓛)`
(HAAR (F3)), each contributing one class mod ℓ, so `p_ℓ≤T^{0.5}(1+𝓛)/(ℓ−1)`. ∎

**Lemma 2.2 (mass of the big family; PROVED modulo Bombieri–Vinogradov and the
fundamental lemma — both theorems).** `μ:=Σ_{E∈𝓕}P(E) ≥ c_1𝓛³/log y` for `T≥T_0`.

*Proof.* Keep only `v≤T^{0.3}`, `ℓ∈(T^{0.6},T^{0.7}]`. The conditions `vℓ≡−1 (mod 4n)`,
`gcd(v,2n)=1` imply `M≡3 (4)` and `n|A_M`; `ℓ∤v` since `ℓ>v`. So

```
μ ≥ Σ_{N_0≤n≤T^{1/10}} 2^{ω(n)} Σ_{v≤T^{0.3}, y-rough sqfree, (v,2n)=1} (1/v)·S_{4n}(−v^{−1}),
S_q(c) := Σ_{ℓ∈(T^{0.6},T^{0.7}], ℓ≡c (q)} 1/ℓ.
```

*ℓ-sum.* Split `(T^{0.6},T^{0.7}]` into `≤𝓛` dyadic blocks `(X,2X]`. BV (with `max_{t≤2X}`,
moduli `q≤4T^{1/10}≤X^{1/5}`) gives `Σ_q E_q(X)≪_A X/𝓛^{A'}`, `E_q(X):=max_{t≤2X}max_{(c,q)=1}
|π(t;q,c)−π(t)/φ(q)|`. Call q *bad* if `E_q(X)>X/(φ(q)𝓛²)` for some block; then
`Σ_{q bad}1/φ(q)≤𝓛^{3−A'}`. For good q every block contributes
`≥(1/2X)(π(2X)−π(X)−2X/𝓛²)/φ(q)`, so `S_q(c)≥c_2/φ(q)` (`c_2=(1/2)log(7/6)`, T large).
Bad n: by Cauchy–Schwarz `Σ_{4n bad}2^{ω(n)}/φ(4n) ≤ (Σ_{bad}1/φ(q))^{1/2}(Σ_{n≤T}4^{ω(n)}/φ(n))^{1/2}
≪𝓛^{(3−A')/2+2}`, negligible for `A'=10`.
*v-sum.* The fundamental lemma (as in HAAR Lemma 2.2, sifting `[1,T^{0.3}]` by the primes `<y`
and the primes of n, `ω(n)≤𝓛`) gives `Σ_{v≤T^{0.3}, y-rough, (v,2n)=1}1/v ≥ c_3𝓛/log y`;
non-squarefree v (divisible by `p²`, `p>y`) cost `≤𝓛Σ_{p>y}p^{−2}=O(𝓛/y)`.
*n-sum.* `Σ_{N_0≤n≤T^{1/10}}2^{ω(n)}/φ(4n) ≥ (1/2)Σ 2^{ω(n)}/n ≥ c_4𝓛²` (HAAR Lemma 2.2's
last step). Multiply. ∎

**Lemma 2.3 (lower tail of the big odds via m copies; PROVED, from HAAR Thm 1.4).** Let
`1≤m≤y/𝓛^4`. Then, on the fibre,

```
E[ ∏_ℓ (1−p_ℓ(X_s))^m ] ≤ exp( −mμ + C_5 m² 𝓛² ).
```

*Proof.* *Copy system.* Take m independent copies `X_ℓ^{(1)},…,X_ℓ^{(m)}` of every big
coordinate (small coordinates shared), and the atomic events
`E^{(i)}:={X_q≡−4D (q) ∀q|v}∩{X^{(i)}_ℓ≡−4D (ℓ)}`, `E∈𝓕`, `i≤m`; call this 𝓕^{(m)}.
Given `x_s` the copies are independent, so `P(Av(𝓕^{(m)})|x_s)=∏_ℓ(1−p_ℓ(x_s))^m`, and the
left side is `P(Av(𝓕^{(m)}))`. Its mass is `mμ`.
*Local lemma.* `E^{(i)}` conflicts only with events sharing a prime `q|v` (any copy) or with
copy-i events at ℓ. So `Σ_{Γ(E^{(i)})}P ≤ mΣ_{q|v}w_q + w_ℓ ≤ m(𝓛/log y)(𝓛³/(2y)+4𝓛T^{−2/5}) + T^{−0.09}
≤ 1/8` (HAAR Lemma 2.3's `w_q`; `w_ℓ` as in Lemma 2.1), and `P(E)≤1/8`. HAAR Remark 1.4(iii):
the hypothesis of HAAR Lemma 1.3 holds with `x=2P`, `K≤e^{1/3}`.
*Pair sum.* Bit-sharing pairs of 𝓕^{(m)}: (α) same copy, `E≠E'`: exactly the bit-sharing
pairs of 𝓕, total `≤mΔ(𝓕)≤mC𝓛²`; (β) copies `i≠j`: they share only primes of
`g:=gcd(v,v')`, so `g>1` and agreement means `g|D−D'`; with `v=gw`, `v'=gw'` and (F2),
`P(E^{(i)}∩E'^{(j)})=1/(φ(g)φ(w)φ(w')φ(ℓ)φ(ℓ'))≤32/(gww'ℓℓ')`. For fixed `(g,n)` put
`Σ(g,n):=Σ_{w y-rough, ℓ>T^{0.6}: gwℓ≡−1 (4n)}1/(wℓ) ≤ C𝓛/(φ(4n)log y)`
(Brun–Titchmarsh `π(t;q,c)≤2t/(φ(q)log(t/q))`, `q=4n≤t^{1/6}`, gives `Σ_{ℓ≡c (q), ℓ>T^{0.6}}1/ℓ≤C/φ(q)`;
and `Σ_{w y-rough}1/w≤C𝓛/log y`).
  * `D=D'` (so `n=n'`): `≤Σ_n2^{ω(n)}Σ_{g>y}(32/g)Σ(g,n)² ≪ (𝓛³/log³y)Σ_{n≥N_0}2^{ω(n)}/φ(n)²
    ≪ 𝓛³log N_0/(N_0log³y) ≪ 𝓛`.
  * `D≠D'`: `g|D−D'≠0`; by HAAR (F5) `Σ_{g|D−D', g>1}1/g≤2𝓛/y`, so the sum is
    `≤(64𝓛/y)(C𝓛/log y)²(Σ_n2^{ω(n)}/φ(4n))² ≪ 𝓛^7/(y log²y) ≪ 𝓛²`.
  Each unordered cross pair is counted for at most `m²` copy pairs, so (β) `≤C'm²𝓛²`.
HAAR Thm 1.4: `−log P(Av(𝓕^{(m)})) ≥ mμ − e^{1/3}(mC+C'm²)𝓛²`. ∎

**Theorem 2.4 (level barrier for ES minorants; PROVED modulo BV and the fundamental lemma,
via HAAR Thm 1.4).** In Setting 2.0 let `μ≥c_1𝓛³/log y` be the big-family mass (Lemma 2.2)
and `1≤m≤min(y/𝓛^4, μ/(8C_5𝓛²))`. If B has level `≤D`, `B≤F` on the fibre, and

```
log D ≤ 0.6·𝓛·(μ/3 − 1),                                               (2.1)
```

then `E_fibre B ≤ exp(−mμ/4)`. With `y=max(𝓛^5,Y)`, `Y=𝓛^{O(1)}`, and `m≍𝓛/log𝓛`:
**every minorant of level `log D ≤ c𝓛^4/log𝓛` has `E B ≤ exp(−c'𝓛^4/(log𝓛)²)`.**

*Proof.* `k=⌊log D/(0.6𝓛)⌋≤μ/3−1`. By Lemma 2.1 and Theorem 1.3 (`r*≤2p*`),
`E B ≤ E[F·1{R<K'}]` with `K':=(k+1)+(2k+1)r*≤(k+1)(1+4p*)`. Given `x_s` the big coordinates
are independent Haar, so `E[F|x_s]≤∏_ℓ(1−p_ℓ)≤e^{−P}`, `P:=Σ_ℓp_ℓ≤R`. Hence, for `θ≥0`,
`E B ≤ E[e^{−P}1{P<K'}] ≤ e^{θK'}E[e^{−(1+θ)P}]`. Take `1+θ:=m(1+p*)`. Since
`log(1−p)≥−p(1+p)` for `p≤1/2`, `e^{−(1+θ)P}≤∏_ℓ(1−p_ℓ)^m`, and Lemma 2.3 gives
`E B ≤ exp(m(1+p*)K' − mμ + C_5m²𝓛²) ≤ exp(m(μ/2 − μ + μ/8))`, using
`(1+p*)K'≤(k+1)(1+6p*)≤μ/2` and `C_5m𝓛²≤μ/8`. ∎

**Corollary 2.5 (the transfer ceiling; PROVED implication).** On the fibre of O13 Thm 5.1
(`Q'=Qℓ_aux`, Q Y-smooth, `ℓ_aux>T`, `log(1/δ_fibre)≪𝓛³(log𝓛)^{O(1)}` modulo NT), every minorant B of F of level
`log D≤c𝓛^4/log𝓛` has `E B ≤ δ_fibre·exp(−𝓛^{4−o(1)})`. In particular BRW (O8 Lemma 3.1,
needing `E B≥0.99δ`), Selberg-type quadratic minorants, β-sieve/Bonferroni truncations
and any choice of `u_j` or weights in C-1 (brief items (i)–(iii)) all need cell/conductor
level `log Z ≥ log D ≫ 𝓛^4/log𝓛`. So O13 Thm 5.1's `log Z≪𝓛^4log𝓛` is optimal
up to logs **for every transfer that certifies primes through a level-D minorant of F** (a
function of n in the span of characters of conductor `≤D`), and such transfers cannot give
exponent better than `1/4` (up to logs) for `W(p)`, on these fibres.

*Proof.* Theorem 2.4 with `δ_fibre≥exp(−C𝓛³(log𝓛)^C)`. ∎

**Theorem 2.6 (any quarantine; PROVED, same inputs).** Let Q be any modulus with
`log Q≤𝓛^5`, r any unit class, and take `y:=𝓛^6`. Every B of level `≤D` with `B≤F` on `rH`
and `log D≤c𝓛^4/log𝓛` has `E_{rH}B≤exp(−c'𝓛^4/(log𝓛)²)`.

*Proof.* Replace 𝓕 by `𝓕_Q:={E∈𝓕: gcd(M,Q)=1}`; its coordinates are free and Haar on the
fibre, F is still `≤` its avoidance indicator, and all upper bounds (Lemma 2.1, local lemma,
Δ, Δ_×) are inherited by the subfamily. The lost mass is `≤Σ_{q|Q, q>y}w_q ≤
(log Q/log y)(𝓛³/(2y)+4𝓛T^{−2/5})+ω(Q)T^{−0.09} ≪ 𝓛²/log𝓛`, so `μ(𝓕_Q)≥μ/2≫𝓛³/log𝓛`.
Run Theorem 2.4 with `m≍𝓛/log𝓛 ≤ y/𝓛^4`. ∎

*Reading (Assessment for the last step).* A quarantine+minorant certificate (O9 Thm 1.1 shape)
counts primes `p≡r (Q)` with main term `E_{rH}B·π(x)/φ(Q)`. By Theorem 2.6, either
`log Q>𝓛^5`, or the level satisfies `log Z≥log D≫𝓛^4/log𝓛`, or the main term is
`≤exp(−c'𝓛^4/(log𝓛)²)π(x)`. Gallagher/BV-type transfers need `log x≫log Z` in the second
case and `log x≫log(1/E B)` in the third (main term ≥ error ≥ 1 in any counting argument).
Either way `log p≫𝓛^4/(log𝓛)²`. So **exponent `1/4` is the ceiling, up to logs, of every
argument that certifies a hard prime through a bounded-level Haar minorant of F**; the
heuristic truth `1/3` (Haar exponent 3) lies beyond it, as twin primes lie beyond sieve level.

**Numerics (`scripts/omega14_planting.py`, `data/omega14/planting.txt`).** (1) Lemma 1.1's
explicit ν verified in exact rationals on 300 random instances satisfying (1.1) (`n≤9`,
`k≤3`): `ν≥0`, `ν(0)=0`, all `≤k`-marginals equal μ; 0 failures. (2) Toy LP (n iid bits,
`F=1[all zero]`, B any sum of `≤k`-bit functions with `B≤F`): the optimum `E B/E F` vanishes
already at `R≈1.1 (k=1)`, `1.8 (k=2)`, `3.0 (k=3)` (n=10,10,12), below the sufficient
threshold `(k+1)+(2k+1)r*` (2.3, 3.9, 5.8). So (1.1) is conservative by a constant factor only;
the order `k≍R` is right (Remark (ii)).

## 3. What this says about the brief's routes (i)–(iii)

**Corollary 3.1 (no sharper energy tail; PROVED from Thm 2.4 and O8 Lemma 3.1/O11 Cor 1.2).**
On the fibre of O13 Thm 5.1, EL_mod(τ) (O11 Cor 1.2: every `F^{(j)}` has digit-energy beyond
log-modulus τ at most `e^{−3S}/(100m²(S+1))`) is **false** for `τ≤c𝓛^4/log𝓛`. In particular no
modulus weighting λ_v in C-1 (brief item (i)), however adapted to prime sizes or to
single-prime events, can give a tail `≤2^{−τ/ρ}` with `ρ≤c𝓛/(log𝓛)²` (such a tail would give EL_mod at
`τ≍ρ(S_res+𝓛)≪ρ𝓛³log𝓛≤c'𝓛^4/log𝓛`). The present `ρ=2𝓛` is optimal up to `(log𝓛)²`.

*Proof.* EL_mod(τ) makes the BRW minorant B have `E B≥0.99δ` (O13 I1(a)) and cells of modulus
`≤e^{2τ+3𝓛}` (O11 Cor 1.2), i.e. level `log D≤2τ+3𝓛`. Theorem 2.4 forbids this when
`2τ+3𝓛≤c𝓛^4/log𝓛`. ∎

*Item (ii)* (single-prime events exactly, BRW only for multi-prime ones). The product formula
`∏_ℓ(1−1[X_ℓ∈Ω_ℓ])` over single-prime events is itself a function of level `∏ℓ` (huge); any
truncation to level D is a level-D minorant, covered by Thm 2.4. Here the obstruction comes
from 2-or-more-prime events `M=vℓ` (one big prime, rough small part), whose mass `≍𝓛³/log𝓛` is
the bulk; single-prime events (`M=ℓ`) have mass only `≍𝓛²` (HAAR Prop 1.5's `S1`), so they
are not the issue. *Item (iii)* (Selberg-type quadratic minorants `1−(Σλ_dχ_d)²`-shaped, or
any other sieve): these have level `≤D²` for weights of level D, so they are covered too.

*Where the barrier comes from, concretely.* Condition on all coordinates below `T^{0.6}`. What
remains is a *one-dimensional sieve* on the big primes `ℓ>T^{0.6}`, with removed classes
`Ω_ℓ(x_s)` of total density `≈μ≍𝓛³/log𝓛`, i.e. a sieve of dimension `κ≍μ` with every
modulus `>T^{0.6}`. Lower-bound sieves of dimension κ need level `z^{≍κ}` (sieving limit
`β_κ≍κ`); here `z^{κ}=e^{≍𝓛μ}`. Lemma 1.1 is the elementary proof of `β_κ≳κ` that this
needs, and Lemma 2.3 shows that conditioning on avoidance (F=1) does not shrink κ.

## 4. Status (checkpoint 1)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | planting: odds-sum `R≥(k+1)+(2k+1)r*` ⇒ k-wise-equivalent law with no all-zero | PROVED (exact check, 300 instances) |
| Thm 1.3 | abstract level barrier `E B≤E[F·1{R<…}]` for `B∈𝒱_k`, `B≤F` | PROVED |
| Lemma 2.1 | big family: one big prime `>T^{0.6}`, `p*≤T^{−0.09}` | PROVED |
| Lemma 2.2 | big-family mass `≫𝓛³/log y` | PROVED mod BV + fundamental lemma (theorems) |
| Lemma 2.3 | m-copy Janson: `E∏(1−p_ℓ)^m≤exp(−mμ+Cm²𝓛²)` | PROVED (via HAAR Thm 1.4, Lemmas 2.3–2.4) |
| Thm 2.4 | level `log D≤0.6𝓛(μ/3−1)` ⇒ `E B≤exp(−mμ/4)` | PROVED (same inputs) |
| Cor 2.5 | on O13 Thm 5.1's fibre: level `≫𝓛^4/log𝓛` is necessary; Thm 5.1 optimal up to logs among level-D minorant transfers | PROVED implication (+NT for δ) |
| Thm 2.6 | any Q with `log Q≤𝓛^5`: same barrier | PROVED |
| "1/4 ceiling" reading | for all bounded-level-minorant certificates | Assessment (last step: main term vs x) |
| Cor 3.1 | EL_mod(τ) false for `τ≤c𝓛^4/log𝓛`: no better C-1 weights | PROVED |

Not claimed: anything about ES; anything about arguments that do not pass through a
bounded-level minorant of F (e.g. bilinear/Type II input on primes, parity-sensitive inputs).

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; OMP_NUM_THREADS=2 timeout 900 uv run --with scipy python scripts/omega14_planting.py 1)  # §1 checks -> data/omega14/planting.txt (~1 min)
```
