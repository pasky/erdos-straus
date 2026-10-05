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
