# The junta bottleneck: a level barrier at `𝓛·S` (task O49)

Status: IN PROGRESS. Labels as in DISCOVERIES.md. Notation as in POINTWISE_OMEGA13.md (O13),
O11, O12: `𝓛=log T`; coordinates `X_ℓ∈ℤ_ℓ^×` (Haar); atoms `(M,D)`, `M≡3 (4)`, `M≤T`,
`A=(M+1)/4`, `D|A²`, event `E_{M,D}={n≡−4D (mod M)}`; F = indicator that no event holds.

## 0. Summary and the question

O13 Cor 3.5 pays `log Z ≍ log Q + 𝓛·S` (S = residual mass `≍𝓛³` up to logs), and the
`𝓛·S` is the cell modulus of the BRW minorant (O11 Cor 1.2). The brief asks for a minorant
of cell modulus `≪S·polylog`, or a proof that `𝓛·S` is forced.

Answer: **it is forced (up to logs) for every *dense* minorant of bounded level — any B
with `B≤F` keeping a share `≥exp(−𝓛^{3.9})` of the avoider mass — not only for BRW**
(Thm 2.4, Cor 2.5, Cor 3.1). Sparse minorants with small `A=E|B|/E B` remain open (Prop 2.7).
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

*Technical remarks (R49 m1).* (a) Only finitely many b have `p_b(x_s)>0` (in the ES instance:
primes ≤T), so Lemma 1.1 is applied to a finite bit vector; bits with `p_b=0` get `w_J=0` and are
never planted. (b) `ν≪P` with `dν/dP≤2` (the positive extra charge on `1_y` is `≤μ(1_y)`, since
`e_{k+1−j}(s)≤e_{k+1}(r)`), so `B≤F` P-a.e. suffices and every P-integrable φ stays ν-integrable.
(c) `x_s↦ν_{x_s}` is measurable (Ω_b depends on x_s through a finite modulus in the ES instance).

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
copy-i events at ℓ. So `Σ_{Γ(E^{(i)})}P ≤ mΣ_{q|v}w_q + w_ℓ ≤ m(𝓛/log y)(𝓛³/(2y)+4𝓛T^{−2/5}) + T^{−0.49}
≤ 1/8` (HAAR Lemma 2.3's `w_q`; here `w_ℓ:=Σ_{ℓ(E)=ℓ}P(E)` is the *unconditional* load, not
Lemma 2.1's conditional `p_ℓ(x_s)`: by the count in Lemma 2.1's proof and `P(E)=1/φ(vℓ)`,
`w_ℓ≤T^{0.1}(1+𝓛)·(Σ_{v y-rough}1/φ(v))/(ℓ−1)≤T^{0.1}(1+𝓛)(C𝓛/log y)/(ℓ−1)≤T^{−0.49}` for `ℓ>T^{0.6}`), and `P(E)≤1/8`. HAAR Remark 1.4(iii):
the hypothesis of HAAR Lemma 1.3 holds with `x=2P`, `K≤e^{1/3}`.
*Pair sum.* Bit-sharing pairs of 𝓕^{(m)}: (α) same copy, `E≠E'`: exactly the bit-sharing
pairs of 𝓕, total `≤mΔ(𝓕)≤mC𝓛²`; (β) copies `i≠j`: they share only primes of
`g:=gcd(v,v')`, so `g>1` and agreement means `g|D−D'`; with `v=gw`, `v'=gw'` and (F2),
`P(E^{(i)}∩E'^{(j)})=1/(φ(g)φ(w)φ(w')φ(ℓ)φ(ℓ'))≤32/(gww'ℓℓ')`. For fixed `(g,n)` put
`Σ(g,n):=Σ_{w y-rough, ℓ>T^{0.6}: gwℓ≡−1 (4n)}1/(wℓ) ≤ C𝓛/(φ(4n)log y)`
(Brun–Titchmarsh `π(t;q,c)≤2t/(φ(q)log(t/q))`, `q=4n≤t^{1/5}`, gives `Σ_{ℓ≡c (q), ℓ>T^{0.6}}1/ℓ≤C/φ(q)`;
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

then `E_fibre B ≤ exp(−mμ/4)` (the computation gives `exp(−3mμ/8)`). With `y=max(𝓛^5,Y)`, `Y=𝓛^{O(1)}`, and `m≍𝓛/log𝓛`:
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
up to logs **among transfers that need a level-D minorant of F keeping a share
`≥exp(−𝓛^{3.9})` of the avoider mass** (level = span of characters of conductor `≤D`); see the
scope note after Prop 2.7 for sparse minorants.

*Proof.* Theorem 2.4 with `δ_fibre≥exp(−C𝓛³(log𝓛)^C)`. ∎

**Theorem 2.6 (any quarantine; PROVED, same inputs).** Let Q be any modulus with
`log Q≤𝓛^5`, r any unit class, and take `y:=𝓛^6`. Every B of level `≤D` with `B≤F` on `rH`
and `log D≤c𝓛^4/log𝓛` has `E_{rH}B≤exp(−c'𝓛^4/(log𝓛)²)`.

*Proof.* Replace 𝓕 by `𝓕_Q:={E∈𝓕: gcd(M,Q)=1}`; its coordinates are free and Haar on the
fibre, F is still `≤` its avoidance indicator, and all upper bounds (Lemma 2.1, local lemma,
Δ, Δ_×) are inherited by the subfamily. The lost mass is `≤Σ_{q|Q, q>y}w_q ≤
(log Q/log y)(𝓛³/(2y)+4𝓛T^{−2/5})+ω(Q)T^{−0.09} ≪ 𝓛²/log𝓛`, so `μ(𝓕_Q)≥μ/2≫𝓛³/log𝓛`.
Run Theorem 2.4 with `m≍𝓛/log𝓛 ≤ y/𝓛^4`. ∎

**Proposition 2.7 (where a low-level minorant's mean lives; PROVED).** In Theorem 2.4's
setting (or 2.6's), let `G:={R(X_s)<K'}`. Then `E B ≤ E[B^+·1_G]` and `P(G)≤exp(−3mμ/8)`.

*Proof.* In Theorem 1.3's law ν, `B≤F=0` on planted configurations, and on unplanted ones
(the x_s-measurable event G) ν equals the true law. So `E B=E_νB≤E[B·1_G]≤E[B^+1_G]`. For
`P(G)`: `R≥P`, so `P(G)≤e^{θK'}E e^{−θP}` with `θ:=m(1+p*)`, and `e^{−θP}≤∏(1−p_ℓ)^m`;
Lemma 2.3 and the arithmetic of Theorem 2.4 give `≤exp(−3mμ/8)`. ∎

*Scope (after self-review; corrects an earlier overclaim).* Theorems 2.4/2.6 bound the
*absolute* mean of every level-D minorant. They block every transfer that needs the
minorant to keep a non-negligible share of the avoider mass — in particular O13 Thm 5.1's
BRW route (`E B≥0.99δ`), and every route through EL-type energy bounds (Cor 3.1). They do
**not** by themselves block O9 Thm 1.1 in general: its cost `C(1+log A)log Z` depends only on
`log Z` and `A=E|B|/E B`, which are invariant under `B↦εB`. The loophole is a *sparse*
minorant: level `≪𝓛^4/log𝓛`, mean `≤e^{−3mμ/8}`-small (Prop 2.7: its positive mean is carried
by the exponentially rare, non-low-level set G), yet `A=O(1)` or `log A≪𝓛^{1−ε}`. No such
minorant is known, and the natural candidate (Bonferroni on big primes, restricted to G)
lives outside the level-D space and has `log A≍μ`. Whether `log A·log Z≫𝓛^4/polylog` holds for
all level-D minorants is **open** (target O49b). So "1/4 is the ceiling of minorant-based
transfers" is an **Assessment**, proved only for dense minorants (mean `≥e^{−c𝓛^4/(log𝓛)²}`
relative to the fibre).

**Numerics (`scripts/omega14_planting.py`, `data/omega14/planting.txt`).** (1) Lemma 1.1's
explicit ν verified in exact rationals on 100 random instances satisfying (1.1), 25 for each
`k=0,1,2,3` (`n≤22`, `p_i∈[0.2,0.5]` plus one zero coordinate; ρ=ν−μ is supported on `|y|≤k+1`,
so the check is exact without enumerating `2^n`): `ν≥0`, `ν(0)=0`, all `≤k`-marginals of ρ
vanish; 0 failures (the script asserts this, and LP success/feasibility). (2) Toy LP (n iid bits,
`F=1[all zero]`, B any sum of `≤k`-bit functions with `B≤F`): on our grid (p step 0.05) the
first grid values with optimum `E B/E F=0` are `R≈1.1 (k=1)`, `1.8 (k=2)`, `3.0 (k=3)`
(n=10,10,12); these are grid values, not thresholds. R49's bisection on the exactly
symmetrised LP (`scripts/review_o14_toy_lp.py`) gives the actual thresholds `R≈1.11, 1.25, 2.51`
(same n), all below the sufficient threshold `(k+1)+(2k+1)r*` (2.3, 3.9, 5.8). So (1.1) is conservative by a constant factor only;
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
level-D replacement that remains a minorant is covered by Thm 2.4. Here the obstruction comes
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

## 5. Status (checkpoints 1–2)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | planting: odds-sum `R≥(k+1)+(2k+1)r*` ⇒ k-wise-equivalent law with no all-zero | PROVED (exact check, 100 instances, k≤3) |
| Thm 1.3 | abstract level barrier `E B≤E[F·1{R<…}]` for `B∈𝒱_k`, `B≤F` | PROVED |
| Lemma 2.1 | big family: one big prime `>T^{0.6}`, `p*≤T^{−0.09}` | PROVED |
| Lemma 2.2 | big-family mass `≫𝓛³/log y` | PROVED mod BV + fundamental lemma (theorems) |
| Lemma 2.3 | m-copy Janson: `E∏(1−p_ℓ)^m≤exp(−mμ+Cm²𝓛²)` | PROVED (via HAAR Thm 1.4, Lemmas 2.3–2.4) |
| Thm 2.4 | level `log D≤0.6𝓛(μ/3−1)` ⇒ `E B≤exp(−mμ/4)` | PROVED (same inputs) |
| Cor 2.5 | on O13 Thm 5.1's fibre: level `≫𝓛^4/log𝓛` is necessary; Thm 5.1 optimal up to logs among level-D minorant transfers | PROVED implication (+NT for δ) |
| Thm 2.6 | any Q with `log Q≤𝓛^5`: same barrier | PROVED |
| Prop 2.7 | a level-D minorant's mean lives on a set of measure `≤e^{−3mμ/8}` | PROVED |
| "1/4 ceiling" (§2 version) | dense minorants only | superseded by Cor 4.6 |
| Cor 3.1 | EL_mod(τ) false for `τ≤c𝓛^4/log𝓛`: no better C-1 weights | PROVED |
| Lemma 4.1 | deterministic planting: `R(x_s)≥…` for all `x_s` ⇒ `E B≤0` | PROVED |
| Lemmas 4.2–4.4 | uniqueness family; class-uniform primes mod 4n; class-uniform D's mod v | PROVED (4.3 mod (G) + effective Page) |
| Thm 4.5 | every fibre with `log Q≤T^{0.05}`: no minorant `B≤F` of level `log D≤c𝓛^4/log𝓛` has `E B>0` | PROVED mod (G), Page, fundamental lemma |
| Cor 4.6 | 1/4 is the ceiling (up to `(loglog)^{1/2}`) of certified bounds via minorant transfers needing `log x≫log Z` (O8/O9/O13); closes Prop 2.7's loophole there | PROVED implication |

Not claimed: anything about ES; anything about arguments that do not pass through a
bounded-level minorant of F (e.g. bilinear/Type II input on primes, parity-sensitive inputs).

## 4. Closing the sparse loophole: no positive minorant at all below level `𝓛^4/log𝓛` (O49b)

*Idea.* Prop 2.7 leaves room only on `G={R(X_s)<K'}`. If the big odds are bounded below for
**every** small configuration, then `G=∅` and Theorem 1.3 gives `E B≤0` outright: no
minorant of that level has positive mean, sparse or not, and A plays no role. Typical-case
bounds (Lemma 2.3) cannot give this, because `R(x_s)` is a divisor-type sum over the shifts
`x+4D`. So we pass to a subfamily in which every (ℓ,D) has a *unique* small part v, and
prove class-uniform equidistribution.

**Lemma 4.1 (deterministic planting; PROVED, from Thm 1.3).** In Setting 1.2, suppose
`R(x_s)≥(k+1)+(2k+1)r*` for *every* `x_s`. Then every `B∈𝒱_k` with `B≤F` has `E B≤0`.

*Proof.* Theorem 1.3 with `1{R<…}≡0`. ∎

**The uniqueness family.** Fix a small absolute `ε∈(0,1/10]` (chosen in Lemma 4.3), put
`X:=T^ε`, `V:=X^{1/3}`, `y:=𝓛^6`, and

```
𝓕* := { E_{vℓ,D} : n:=D*∈[V,X], v≤V y-rough squarefree, ℓ prime ∈(T^{0.6},T^{0.7}],
                   vℓ≡−1 (mod 4n) }.
```

As in Lemma 2.2, `vℓ≡−1 (4n)` gives `M=vℓ≡3 (4)` and `n|A_M`, i.e. `D|A_M²`. Also `M` is squarefree
and y-rough, `√T≤M≤T`, and `D≤n²≤T^{2ε}<M/4`, so 𝓕* is a subfamily of §2's 𝓕 (with v
restricted further). Lemma 2.1 holds for it.

**Lemma 4.2 (unique small part; PROVED).** For each pair (ℓ,D) there is at most one v with
`E_{vℓ,D}∈𝓕*`. Hence, for every small configuration x (the coordinates at primes `≤T^{0.6}`),

```
Σ_ℓ p_ℓ(x) = Σ_{v} Σ_{D: n_D∈[V,X], 4D≡−x (mod v)} c(v,n_D),     c(v,n):=Σ_{ℓ∈(T^{0.6},T^{0.7}], ℓ≡−v^{−1} (4n)} 1/(ℓ−1),
```

with v over y-rough squarefree `v≤V`, and `c(v,n):=0` if `gcd(v,2n)>1`.

*Proof.* v satisfies `v≡−ℓ^{−1} (mod 4n)` and `1≤v≤V≤n<4n`, so v is determined by (ℓ,n).
Given x, the events at ℓ whose small part holds are the `E_{vℓ,D}` with
`x≡−4D (mod v)`. Distinct D give distinct classes `−4D mod ℓ`, since `0<|D−D'|<T^{2ε}<ℓ`. So
`p_ℓ(x)=(ℓ−1)^{−1}#{D: the v of (ℓ,D) exists and x≡−4D (v)}`. Sum over ℓ, then group by v. ∎

**Lemma 4.3 (class-uniform primes mod 4n; PROVED modulo (G) and the effective Page bound,
as quoted in POINTWISE_OMEGA9 §1).** There is an absolute `ε_0>0` such that, for `ε≤ε_0`, T
large, and `q_1` the modulus of the exceptional character of (G) with `Q_G:=4X` (if any), put

```
𝒩_exc := {n : q_1 | 4n} if q_1 exists and q_1>𝓛^{1.9};   𝒩_exc := ∅ otherwise.
```

Then `c(v,n) ≥ 0.13/φ(4n)` for every `n∈[V,X]∖𝒩_exc` and every `v≤V` with `gcd(v,2n)=1`.

*Proof.* Put `q:=4n≤Q_G` and `b:≡−v^{−1} (q)`, a unit. Every χ mod q is induced by a primitive
`χ*` of conductor `q*|q`, and `|ϑ(x;χ)−ϑ(x;χ*)|≤log q`. Orthogonality and (G) give, for
`x∈[T^{0.6},T^{0.7}]`,

```
|ϑ(x;q,b) − x/φ(q) + [q_1|q]χ_1(b)x^{β_1}/(β_1φ(q))| ≤ (C'/φ(q))·x·(e^{−log x/(κlog Q_G)} + (log x/log Q_G)²/Q_G) + log q.
```

In the exceptional case the Gallagher term (not the induced-character term `log q`) carries a
prefactor `(1−β_1)log x≤0.7/(κε)`. Since `log x/log Q_G≥0.6/(ε+o(1))`, the right side is
`≤x/(8φ(q))` once ε is small. The range condition `Q_G^{6c}=4^{6c}T^{6cε}≤x` holds for
`ε≤0.05/c`.
*Exceptional term.* If `q_1∤q`, it is absent. If `q_1|q` and `q_1≤𝓛^{1.9}`, the effective Page bound
`1−β_1≫q_1^{−1/2}(log q_1)^{−2}` gives `x^{β_1−1}≤exp(−c𝓛^{0.05}/(log𝓛)²)=o(1)`, and `1/β_1≤2`.
If `q_1|q` and `q_1>𝓛^{1.9}`, then `n∈𝒩_exc`, which is excluded.
So `ϑ(t;q,b)∈[(7/8−o(1)),(9/8+o(1))]·t/φ(q)` (the `+o(1)` covers `χ_1(b)=−1`) on `[T^{0.6},T^{0.7}]`. Partial summation then gives
`Σ_{ℓ≡b (q), ℓ∈(T^{0.6},T^{0.7}]}1/ℓ ≥ (7/8)log(7/6)/φ(q) − O(1/(𝓛φ(q))) ≥ 0.13/φ(q)`: the
integral `∫ϑ(t)(1+log t)(t log t)^{−2}dt` gives `log(7/6)`, and the boundary terms are
`O(1/𝓛)`. ∎

*Exceptional set is harmless.* If `q_1>𝓛^{1.9}`, write `q'':=q_1/gcd(q_1,4)≥q_1/4`; then
`n∈𝒩_exc ⟺ q''|n`. It is used only through Lemma 4.4's class-uniform upper bound for multiples
of `q''`, with `τ(q'')/q''≤𝓛^{−1.8}`.

**Lemma 4.4 (the D's are class-uniform mod v; PROVED, elementary).** Put `L:=log X=ε𝓛`.
For T large, every odd squarefree y-rough `v≤V`, and every unit class a mod v,

```
W(v,a) := Σ_{D: n_D∈[V,X]∖𝒩_exc, D≡a (v)} 1/φ(4n_D) ≥ L²/(200v).
```

*Proof.* Write `D=κt²` with κ squarefree, so `n_D=κt`; this is a bijection between D and such
pairs. Keep only `t≤X^{1/6}` with `(t,v)=1` and `κ∈(K_1,K_2]`, where `K_1:=X^{2/3}` and `K_2:=X/t`.
Then `n_D∈[V,X]`, and `D≡a (v)` means `κ≡b:=at^{−2} (v)`. Since `φ(4n)≤2n`,
`W(v,a)≥H_all−H_exc`, where `H_all`/`H_exc` are the surrogate sums of `1/(2κt)` over the kept
pairs with all n / with `n∈𝒩_exc`; we bound `H_all` below and `H_exc` above.
*Squarefree count.* For a unit `b mod v`,
`N_b(K):=#{κ≤K squarefree, κ≡b (v)} = σ_vK/v + O(√K)` uniformly, with
`σ_v=Σ_{(d,v)=1}μ(d)/d²≥6/π²`. To see this, write `μ²(κ)=Σ_{d²|κ}μ(d)`; if `p|(d,v)` the count
is empty, otherwise `#{m≤K/d²: md²≡b (v)}=K/(d²v)+O(1)`; the tail `d>√K` costs `≤√K/v`.
Partial summation gives
`Σ_{κ∈(K_1,K_2], κ≡b}1/κ ≥ (σ_v/v)log(X^{1/3}/t) − O(K_1^{−1/2})`.
*Sum over t.* For y-rough v,
`Σ_{t≤X^{1/6},(t,v)=1}(1/t)log(X^{1/3}/t) ≥ L²/24 − (ω(v)/y)·O(L²) − O(L) ≥ L²/48`.
So `H_all≥(1/2)(6/π²)L²/(48v) − O(LX^{−1/3})`.
*Removing 𝒩_exc* (only if `q_1>𝓛^{1.9}`). Here `q''|κt`, so `q''/(q'',t)` divides κ. Together
with `κ≡b (v)` this is one class mod `v·q''/(q'',t)` (or empty), and HAAR (F4) bounds the
`1/κ`-sum by `1/K_1+(q'',t)log(X^{1/3})/(vq'')`. Since `Σ_{t≤X}(q'',t)/t≤τ(q'')(1+L)`,
`H_exc≤L²τ(q'')/(vq'')+O(LX^{−2/3}) ≤ 4L²𝓛^{−1.8}/v`.
Collecting, `W(v,a)≥L²/v·(6/(96π²)−o(1)) ≥ L²/(200v)`, using `X^{−1/3}≤1/v`. ∎

**Theorem 4.5 (no positive low-level minorant; PROVED modulo (G), the effective Page bound and
the fundamental lemma).** There are absolute `c,ε>0` such that, for T large, the following holds
for every modulus Q with `log Q≤T^{0.05}` and every unit class r.
Let B be any function on the fibre `n≡r (Q)` of level `≤D` (Setting 2.0), with `B≤F` pointwise and
`log D≤c𝓛^4/log𝓛`. Then

```
E_{fibre} B ≤ 0 .
```

*Proof.* *Setting.* Small coordinates: everything except the `X_ℓ` with ℓ prime,
`ℓ>T^{0.6}`, `ℓ∤Q`; the coordinates fixed by the fibre are constants among the small ones.
The family is `𝓕*` minus the events whose ℓ divides Q. Each event has exactly one big
coordinate, and `p*≤T^{−0.09}` (Lemma 2.1; the family is smaller).
*Uniform lower bound for R.* Fix any small configuration x, with x a unit. By Lemma 4.2,
`R(x)≥Σ_ℓp_ℓ(x)≥Σ_vΣ_{D≡−x/4 (v), n_D∉𝒩_exc}c(v,n_D) − Σ_{ℓ|Q, ℓ>T^{0.6}}p*`.
For `D≡−x/4 (v)`, D is a unit mod v, so `gcd(v,2n_D)=1`. Lemmas 4.3–4.4 then give
`R(x) ≥ 0.13·(L²/200)·Σ_{v≤V y-rough sqfree}1/v − (log Q)T^{−0.09} ≥ μ* := c_9ε³𝓛³/log𝓛`.
For the v-sum, the fundamental lemma gives `≥c_3log V/log y` (as in Lemma 2.2).
*Conclusion.* `k:=⌊log D/(0.6𝓛)⌋`, so `(k+1)+(2k+1)r*≤(k+1)(1+4p*)≤μ*` if `c≤0.3c_9ε³`.
Lemma 4.1 gives `E B≤0`. ∎

**Corollary 4.6 (the 1/4 ceiling of the minorant-transfer architecture; PROVED implication).**
* *Scope.* Certificates that produce a Mordell-hard prime with `W(p)>T` from a Haar minorant
  `B≤F` with `E B>0`, on a fibre with `log Q≤T^{0.05}`, through a transfer whose hypothesis
  requires `log x≫log Z`. Here Z is the minorant's level and x the certified search bound.
  O8/O9 Thm 1.1, and hence O13 Thm 5.1, are of this type (O9 needs
  `log x≥C(1+log A)log Z`); this covers BRW, Selberg, Bonferroni, sparse or dense, any A.
* *Statement.* For every such certificate, `log Z≥c𝓛^4/log𝓛` (Thm 4.5), hence the certified
  bound has `log x≫𝓛^4/log𝓛`. So such certificates cannot give
  `W(p)≥exp((log p)^{1/4+δ})` (δ>0), nor `exp(C(log p log log p)^{1/4})` with C large, *as
  certified bounds*. O13 Thm 5.1 (`(log p)^{1/4}(log log p)^{−1/4}`) is optimal within this
  architecture, up to a factor `(log log p)^{1/2}` in `𝓛`.
* *Not claimed.*
  * Nothing about the true size of the least such prime.
  * Nothing about transfers that do not require `log x≳log Z`.
  * Nothing about prime input other than low-conductor minorants, e.g. bilinear/Type II or
    parity-sensitive input.

Within this scope, this supersedes Prop 2.7's open loophole.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; OMP_NUM_THREADS=2 timeout 900 uv run --with scipy python scripts/omega14_planting.py 1)  # §1 checks -> data/omega14/planting.txt (~1 min)
```
