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

**Setting 2.0.** Haar measure on `Ẑ^×`, restricted to a fibre `n≡r (Q)` (Q arbitrary but
*y-smooth*: all its prime factors are `≤y`; this covers O13 Thm 3.4's square-class
quarantine, whose primes are `≤Y=𝓛^{C_0+4}`, once `y≥Y`). F = indicator that no ES event
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
(`Δ(𝓕)≤C𝓛²`) hold for 𝓕. Every prime of every M exceeds `y≥` every prime of Q, so on the
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
