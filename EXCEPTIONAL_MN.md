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
