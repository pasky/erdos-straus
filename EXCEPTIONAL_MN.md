# EXCEPTIONAL_MN — the 3/4 exceptional-set bound for m/n (task O94)

Status labels as in DISCOVERIES.md. "The note" = `paper/es-threequarter-note.tex`
(INTERNALLY PROVED, not externally refereed). "SHORT" = `EXCEPTIONAL_SHORT.md` ((D)30).
Everything labelled PROVED here is proved *relative to the note* (its lemmas are
re-run with `4` replaced by `m`; the re-run is spelled out lemma by lemma below).

Notation. Fix an integer `m ≥ 4`. `n ≥ 1` is *m-exceptional* if `m/n = 1/x_1+1/x_2+1/x_3`
has no solution in positive integers. `E_m(N) = #{n ≤ N : n m-exceptional}`;
`E_m(I)` the same over an interval `I`. `L = log N`. `ρ(m) = m/φ(m)`.

## 0. Summary (filled in as the work proceeds)

Target: `E_m(N) ≪ N exp(−c L^{3/4} m^{−1/4})`, `c` absolute, uniformly in a range of m;
plus SHORT's interval/progression transfer. Main structural finding so far: **nothing in
the note's density argument is m-specific**; the Jacobi-symbol obstruction of
POINTWISE_MN Lemma 1.1 concerns the *pointwise* witness-modulus process (square-class
revelation), which the density argument never uses (§1.3).

## 1. The atom family for general m

**Lemma 1.1 (multiplier identity for m; PROVED, elementary).** Let `k, ℓ ≥ 1`, `u, v, w ≥ 1`
with `kℓ + 1 = m·uvw`. If `n ≥ 1` and `nv ≡ −u (mod kℓ)`, then `s = (nv+u)/(kℓ)` is a
positive integer and
`m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)`.

*Proof.* Over `nsuvw` the numerators sum to `nv + u + s = s·kℓ + s = s(kℓ+1) = m·suvw`. ∎

(For m = 4 this is note lem:identity. `(uv, kℓ) = 1` since `uv | kℓ+1`, so the class
`−u v^{−1} (mod kℓ)` is a well-defined unit class; every positive integer in it is
m-representable.)

**Definition 1.2 (atom family).** Keep the note's parameters (eq:parameters) verbatim
(`t = log X`, `K = ⌊X^κ⌋`, `H = K^{10}`, blocks `I_j`, `z_j = x_j^{1/6}`) except
`𝒦_m(K) = {1 ≤ k ≤ K : (k, m) = 1}`, `L_K = lcm 𝒦_m(K)`.
`𝒜^{(m)}_X` = quadruples `(k, ℓ, u, v)` with
`k ∈ 𝒦_m(K)`, `ℓ ∈ I_j` prime, `H < u, v ≤ z_j`, `(u,v) = (uv,k) = 1`,
`m·uv | kℓ + 1`
(and `ω(uv) ≤ D log log X` on the retained original route; the simplified route of note
§6 drops it). Atom event `E_A = {n ≡ −u v^{−1} (mod kℓ)}`, `H_X = Σ_A 1_{E_A}`.
`(k,m) = 1` is forced: `kℓ ≡ −1 (mod m)`. Unlike the note (`k ≡ 1 (4)`) we allow every
k coprime to m and let `ℓ ≡ −k^{−1} (mod m)` vary with k; this is what makes the
fibre mass `≍ t^3/m` rather than `t^3/(mφ(m))` (§2).

**Lemma 1.3 (deduplication and conditional independence; PROVED).** For `X ≥ X_0`
(absolute) and every `m ≤ K`, note lem:CRT holds verbatim for `𝒜^{(m)}_X`: every
m-exceptional integer avoids every atom; at fixed ℓ the atoms have distinct projections
mod ℓ; the exact CRT intersection formula (eq:intersection) holds; conditional on
`c (mod L_K)` the coordinates `n mod ℓ` are independent uniform; an atom is active in
fibre c iff `k | u + cv`.

*Proof.* The note's proof uses only: (i) the identity (Lemma 1.1); (ii) `|uv'−u'v| < z_j^2 < ℓ`
(unchanged); (iii) from `kℓ ≡ k'ℓ ≡ −1 (mod m uv)` and `(ℓ, muv) = 1`: `k ≡ k' (mod muv)`,
and `muv > H^2 > K` gives `k = k'`; (iv) `ℓ > X^{1/2} > K` so all ℓ are coprime to `L_K`
(and to m, as `m ≤ K`). ∎

**1.4 Where m = 4 was used in the note, and why the Jacobi obstruction is irrelevant here.**
Grep of the note for every occurrence of `4`/`mod 4`: (a) lem:identity (→ Lemma 1.1);
(b) `k ≡ 1 (4)` in 𝒦(K) and lem:h (→ §2, h_m); (c) the BV/BT modulus `q = 4uv`
(→ `q = muv`, §2); (d) `φ(4uv) ≥ 2φ(u)φ(v)` (→ `φ(muv) ≥ φ(m)φ(u)φ(v)`, valid as
`φ(ab) ≥ φ(a)φ(b)` always); (e) `|𝒜_X| ≤ K X^{4/3}` (unchanged); (f) §§10–11 of the note
(heuristic ceiling, checkpoints; not load-bearing). No step of the density proof
(lattice lemma, Shiu, congestion, harvest, moments, void, Bonferroni) looks at the
quadratic character of the atom classes. POINTWISE_MN Lemma 1.1(d) / Prop. 2.1 are
statements about which *square classes* a revealed residue can avoid — needed for the
pointwise witness-modulus exponent 1/4, not for E_m(N). So the m ≡ 0 (4) dichotomy of
POINTWISE_MN does **not** reappear in the density problem.

## 2. The multiplier harmonic sum h_m (replaces note lem:h)

Put `S_m(x) = Σ_{j ≤ x, (j,m)=1} 1/j`, `h(𝒥) = Σ_{k∈𝒥} φ(k)/k²`, `h_m(K) = h(𝒦_m(K))`.

**Lemma 2.1 (PROVED).** Let `m ≥ 4`.
(a) For `x ≥ m²`: `S_m(x) ≥ (φ(m)/m) log x`.
(b) For every K ≥ 1: `h_m(K) ≥ (1 − Σ_p p^{−2}) S_m(K) ≥ 0.54 S_m(K)`.
(c) For every prime `p ∤ m`: `Σ_{k ∈ 𝒦_m(K), p | k} φ(k)/k² ≤ S_m(K)/p`.
(d) `h_m(K) ≤ S_m(K) ≤ C (φ(m)/m) log K` for `K ≥ m`, C absolute.

*Proof.* (a) Möbius over `e | m`: `S_m(x) = Σ_{e|m} μ(e)/e · Σ_{i ≤ x/e} 1/i`, and
`Σ_{i≤y} 1/i = log y + γ + θ/y`, `|θ| ≤ 1` (y ≥ 1; here `x/e ≥ m ≥ 1`). Hence
`S_m(x) = (φ(m)/m)(log x + γ) − Σ_{e|m} μ(e) log e / e + θ' 2^{ω(m)}/x`, and
`−Σ_{e|m} μ(e) log e/e = (φ(m)/m) Σ_{p|m} log p/(p−1) ≥ 0` (logarithmic derivative of
`Π_{p|m}(1−p^{−s})` at s = 1). So `S_m(x) ≥ (φ(m)/m) log x + γφ(m)/m − 2^{ω(m)}/m²`, and
`2^{ω(m)} ≤ m ≤ γ m φ(m)` for m ≥ 4 (φ(m) ≥ 2).
(b) `φ(k)/k ≥ 1 − Σ_{p|k} 1/p`, so `h_m ≥ S_m(K) − Σ_{p ∤ m} p^{−2} S_m(K/p)` and
`S_m(K/p) ≤ S_m(K)`; `Σ_p p^{−2} < 0.4523`.
(c) Write `k = pj`, `(j,m) = 1`, `j ≤ K/p`; `φ(k)/k² ≤ 1/(pj)`.
(d) `S_m(K) ≤ Π_{p ≤ K, p∤m}(1−1/p)^{−1} ≤ (e^γ+o(1)) log K · Π_{p|m, p≤K}(1−1/p)`, and for
`K ≥ m` every prime of m is ≤ K. ∎

*Check.* `scripts/emn_hm.py 100000`: (a) at x = m² and x = K, (b), (c) for p ∈ {3,5,7,11,101},
for m = 4..60 and 210: 0 failures; observed `S_m(K)/((φ(m)/m) log K) ∈ [1.05, 1.23]`,
`h_m/S_m ∈ [0.63, 0.98]`.

So `h_m(K) ≍ (φ(m)/m) log K` uniformly for `K ≥ m²` (the note's lem:h is the special
case of the sub-progression `k ≡ 1 (4)`, `h = (2/π²) log K`).
