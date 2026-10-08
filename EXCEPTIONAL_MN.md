# EXCEPTIONAL_MN — the 3/4 exceptional-set bound for m/n (task O94)

Status labels as in DISCOVERIES.md. "The note" = `paper/es-threequarter-note.tex`
(INTERNALLY PROVED, not externally refereed). "SHORT" = `EXCEPTIONAL_SHORT.md` ((D)30).
Everything labelled PROVED here is proved *relative to the note* (its lemmas are
re-run with `4` replaced by `m`; the re-run is spelled out lemma by lemma below).

Notation. Fix an integer `m ≥ 4`. `n ≥ 1` is *m-exceptional* if `m/n = 1/x_1+1/x_2+1/x_3`
has no solution in positive integers. `E_m(N) = #{n ≤ N : n m-exceptional}`;
`E_m(I)` the same over an interval `I`. `L = log N`. `ρ(m) = m/φ(m)`.

## 0. Summary

* **Theorem A (PROVED rel. note).** Absolute `c, C`: for every `m ≥ 4`, every interval I of
  length `H ≥ 2`: `E_m(I) ≤ C H exp(−c (log H)^{3/4} m^{−1/4})`; in particular
  `E_m(N) ≤ C N exp(−c (log N)^{3/4}/m^{1/4})`. Asymptotically beats Pomerance–Weingartner's
  `exp(−C (log N)^{2/3}/φ(m)^{1/3})`: the exponents' ratio is `≫ (Lm)^{1/12}/(log log 3m)^{1/3}`, so
  Theorem A's bound is smaller once this exceeds an absolute (ineffective) Λ_0. The saving tends
  to ∞ iff `m = o((log N)³)`. (R94A repair D1, D2; R94B repair D2)
* **Theorem B / Cor. C:** progressions and primes in short intervals, as in SHORT (§5).
* **Corollary D:** most primes in `(N/2,N]` are m-representable once
  `log N ≥ C m^{1/3}(log m)^{4/3}`; with the proof of PW Thm 3.1 (most primes exceptional for
  `m^{1/4} ≪ log N ≤ (φ(m)/(C log² m))^{1/3}`), the *density* transition ("most primes exceptional" →
  "most primes representable") is at `log n = m^{1/3+o(1)}`. Monotonicity in between is unknown.
  PW's rigorous bounds left it between `m^{1/3}` and `m^{1/2}` (R94A D3, R94B D3). Nothing is said about the largest exception.
* **Mechanism:** nothing in the note's density argument is m-specific. Take multipliers
  `k ≤ X^κ` coprime to m; fibre mass becomes `≍ t³/m` on reduced/good fibres (upper bound
  `≪ t³/m` on every fibre; absolute constants); the ledger
  stays `e^{O(t·mass)}`; the whole m-dependence is `t³ → t³/m`. The Jacobi-symbol obstruction of
  POINTWISE_MN Lemma 1.1 is about the pointwise witness-modulus process and does not enter (§1.4).

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
and `ω(uv) ≤ D log log X`. Only the note's *retained original* (ω-cutoff, pruned) route is
re-derived here. Using the larger no-ω family `𝒜′` is still fine: the lower bound comes from the ω-subfamily,
and the BT upper bound and the inventory are unchanged. The note's §6 Cauchy–Schwarz route itself also transfers
via `φ(muv) ≥ φ(m)φ(u)φ(v)`:
`Σ_q W_c(q)² E*_x(q) ≪ x t⁶/φ(m)`, so the error is
`≪ x t³ φ(m)^{−1/2}(log x)^{−R/2}` against a main term `≫ x t h(𝒥)/φ(m)`. Their ratio is `≪ t^{7/2}(log x)^{−R/2} → 0`
for R = 26 (R94B's sketch, not written out further). (R94A repair D7; R94B repair D1) Atom event `E_A = {n ≡ −u v^{−1} (mod kℓ)}`, `H_X = Σ_A 1_{E_A}`.
`(k,m) = 1` is forced: `kℓ ≡ −1 (mod m)`. Unlike the note (`k ≡ 1 (4)`) we allow every
k coprime to m and let `ℓ ≡ −k^{−1} (mod m)` vary with k; this is what makes the
fibre mass `≍ t^3/m` rather than `t^3/(mφ(m))` (§2).

**Lemma 1.3 (deduplication and conditional independence; PROVED).** For `X ≥ X_0`
(absolute) and every `m ≤ t³` (R94B repair D5: only `ℓ ∤ m` uses the size of m), note lem:CRT holds verbatim for `𝒜^{(m)}_X`: every
m-exceptional integer avoids every atom; at fixed ℓ the atoms have distinct projections
mod ℓ; the exact CRT intersection formula (eq:intersection) holds; conditional on
`c (mod L_K)` the coordinates `n mod ℓ` are independent uniform; an atom is active in
fibre c iff `k | u + cv`.

*Proof.* The note's proof uses only: (i) the identity (Lemma 1.1); (ii) `|uv'−u'v| < z_j^2 < ℓ`
(unchanged); (iii) from `kℓ ≡ k'ℓ ≡ −1 (mod m uv)` and `(ℓ, muv) = 1`: `k ≡ k' (mod muv)`,
and `muv > H^2 > K` gives `k = k'`; (iv) `ℓ > X^{1/2} > K` so all ℓ are coprime to `L_K`
(and to m, as `ℓ > X^{1/2} > t³ ≥ m`). ∎

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

## 3. Fibre masses for general m (replaces note thm:harvest, cor:fibremass)

Standing range: **`4 ≤ m ≤ t³`** (t = log X). Then for X ≥ X_0 (absolute) `m ≤ t³ ≤ K^{1/2}`,
so Lemma 2.1 applies with `K ≥ m²`, and every modulus below is `muv ≤ t³ x^{1/3} ≤ x^{0.34}`.

Unchanged inputs (they involve only `k ≤ K`, `(c,k) = 1`, never m or `k mod 4`):
note lem:lattice (stated for every `1 ≤ k ≤ K`), lem:omega, lem:congestion (stated for every
`𝒥 ⊆ 𝒦(K)`; its proof uses only `𝒥 ⊆ [1,K]`, so it holds for `𝒥 ⊆ 𝒦_m(K)`), Shiu, BT, BV.
For `(c, L_𝒥) = 1` put `r_𝒥(u,v;c) = #{k ∈ 𝒥 : k | u + cv}` as in the note.

**Proposition 3.1 (pruned prime slice for m; PROVED rel. note).** Fix κ, D as in the note.
There are absolute `a_h, A_h > 0`, `X_h` such that for `X ≥ X_h`, `4 ≤ m ≤ t³`,
every `1 ∈ 𝒥 ⊆ 𝒦_m(K)` and every `(c, L_𝒥) = 1`, with the note's pruning (eq:pruning) except
`4uv | kℓ+1` → `muv | kℓ+1`,
`a_h t² h(𝒥)/φ(m) ≤ Σ_{X^{1/2}<ℓ≤X} f^{good}_{c;𝒥}(ℓ)/ℓ ≤ A_h t² h(𝒥)/φ(m)`.

*Proof (only the changed lines of the note's proof).*
* Prime condition: `ℓ ≡ −k^{−1} (mod q)`, `q = muv`; reduced since `(k, muv) = 1`.
* Main-term weight of a triple: `(li 2x − li x)/φ(muv) ≥ x/(φ(m) uv log 2x)` because
  `φ(ab) ≤ φ(a)·b`. Harmonic mass after pruning is `≥ (1/8 − o(1))Λ² h(𝒥) ≥ (1/32 − o(1))(log z)² h(𝒥)` exactly as in
  the note (lem:omega, lem:congestion, `h(𝒥) ≥ 1`). Removed *weighted* mass: `1/φ(muv) ≤
  (muv/φ(muv))/(muv) ≪ log t/(φ(m)uv)` since `muv/φ(muv) ≪ log log(3muv) ≪ log t` and `m ≥ φ(m)`;
  so relative loss is `O(log t / t)` as in the note. Block main term `≥ a x log x · h(𝒥)/φ(m)`.
* BV: for fixed q, `uv = q/m` is determined, ≤ `2^{ω(uv)}` allocations, ≤ `T_X = t⁴` multipliers
  each: `W_good(q) ≤ t^{4+D log 2}` (unchanged). Choose `R > 4 + D log 2 + 13` in (eq:BV);
  `q ≤ x^{0.34}` is below the BV level. Total error `O(x (log x)^{−13})`, while the main term is
  `≥ a x log x /φ(m) ≥ a x log x · t^{−3} ≫ x (log x)^{−2}` (`h(𝒥) ≥ 1`, `φ(m) ≤ m ≤ t³`,
  `log x ≍ t`). **This is the only place the range `m ≤ t³` is used for the lower bound**; any
  fixed power `m ≤ t^{A}` works with R depending on A.
* Distinctness of the counted classes: Lemma 1.3.
* Upper bound: BT (eq:BT) with `q = muv ≤ x^{0.34}` and `φ(muv) ≥ φ(m)φ(u)φ(v)`, then
  lem:lattice (eq:latupper). ∎

**Corollary 3.2 (uniform fibre masses for m; PROVED rel. note).** For `X ≥ X_h`,
`4 ≤ m ≤ t³` and **every** residue `c (mod L_K)`, with `𝒥_c = {k ∈ 𝒦_m(K) : (k,c) = 1}`,
`μ_c = Σ_ℓ f_c(ℓ)/ℓ` (f_c counts active atoms of `𝒜^{(m)}_X` at ℓ):
`a_h t² h(𝒥_c)/φ(m) ≤ μ_c ≤ A_h t² h(𝒥_c)/φ(m) ≤ C_u t³/m`,
with `C_u` absolute (Lemma 2.1(d), `log K ≤ κt`). For `(c, L_K) = 1`: `μ_c ≥ a_u t³/m`,
`a_u = 0.54 κ a_h/2` (Lemma 2.1(a),(b), `log K ≥ κt/2`).

*Proof.* Note cor:fibremass verbatim (active atoms have `(k,c) = 1`; `1 ∈ 𝒥_c`), with
Proposition 3.1 and `h(𝒥) ≤ h_m(K) ≤ C(φ(m)/m) κ t`. ∎

**Scaling.** Fibre mass `≍ t³/m` on reduced fibres (lower and upper, absolute constants;
on a general fibre only `μ_c ≪ t³/m` — e.g. c = 0 has `𝒥_c = {1}`, `μ_c ≍ t²/φ(m)`): the `1/φ(m)` from
the prime progression mod `muv` is partly cancelled by `h_m ≍ (φ(m)/m) log K`. Compare the
note's m = 4 family (`k ≡ 1 (4)` only): `t³ · (1/4)·(1/φ(4))`-type constant; our wider
multiplier set gains a constant factor at m = 4 but this is irrelevant there.

## 4. Void, moments and Bonferroni assembly with the m-scaling

Write `s = t³/m` (the fibre-mass scale; `s ≥ 1` in the range `m ≤ t³`). Selector
`y = max(2, B s)`, `S_y = 1_{(n,P_y)=1}`, B absolute (fixed in Lemma 4.1).

**Lemma 4.1 (conditioned void for m; PROVED rel. note).** There are absolute `a_v, B, s_0 > 0`
and `X_v` such that for `X ≥ X_v`, `4 ≤ m ≤ t³` with `s = t³/m ≥ s_0`:
`P(H_X = 0 | S_y = 1) ≤ e^{−a_v s}`.

*Proof.* Note lem:void with these changes. Reveal `c (mod L_K)`; `Z(c) = Σ_{y<p≤K, p|L_K, p|c} 1/p`.
The moment bound (eq:Zmoment) `E(e^{yZ} | S_y=1) ≤ e^{C_Z}` holds for every `y ≥ 2` (C_Z absolute),
so `P(Z > 1/4 | S_y = 1) ≤ e^{−y/4 + C_Z}`. The selector removes every `p ≤ y`, `p | c`
(`p | L_K` ⇒ `p | c ⟺ p | n`). On `Z ≤ 1/4`, by Lemma 2.1(b),(c),(a) and `log K ≥ κt/2`:
`h(𝒥_c) ≥ h_m(K) − Σ_{p|c, y<p≤K, p|L_K} S_m(K)/p ≥ (0.54 − Z) S_m(K) ≥ 0.29 (φ(m)/m)·κt/2`.
Then (Cor. 3.2, lower bound with 𝒥 = 𝒥_c; `1 ∈ 𝒥_c`, `(c, L_{𝒥_c}) = 1`) and Lemma 1.3:
`P(H_X = 0 | c, S_y = 1) = Π_ℓ (1 − f_c(ℓ)/ℓ) ≤ e^{−μ_c} ≤ exp(−a_h t²·0.145 κ t/m) = e^{−2a_v s}`,
`a_v := 0.0725 κ a_h`. Take `B = 8a_v`: for `s ≥ 2/B` the bad-fibre probability is
`≤ e^{C_Z − 2a_v s}`. Total `≤ (1 + e^{C_Z}) e^{−2a_v s} ≤ e^{−a_v s}` for `s ≥ s_0 := (1+C_Z+log 2)/a_v + 2/B`. ∎

(Note: the threshold η of the note is now the absolute 1/4 — the union-bound loss
`Z·S_m(K)` is measured against `h_m ≥ 0.54 S_m` in the same units, so no m-dependence enters.)

**Lemma 4.2 (factorial moments; PROVED rel. note).** For `X ≥ X_h`, `4 ≤ m ≤ t³`, every
`2 ≤ y < X^{1/2}` and every integer `j ≥ 1`: `E((H_X)_j | S_y = 1) ≤ (C_u s)^j`.

*Proof.* Note thm:moments, conditional-independence proof, verbatim: in a fibre c, H_X is a
sum of independent Bernoulli(`f_c(ℓ)/ℓ`) over ℓ (Lemma 1.3), so `E((H_X)_j | c) ≤ μ_c^j`, and
`μ_c ≤ C_u t³/m` for **every** c (Cor. 3.2). ∎

**Theorem 4.3 (assembly for m; PROVED rel. note).** There are absolute `a_v, D_B, C_L, X_a, s_0`
such that for `X ≥ X_a`, `4 ≤ m ≤ t³`, `s = t³/m ≥ s_0`, and r the least even integer
`≥ D_B s`, `ν_X = S_y·Q_r(H_X) ≥ 0` satisfies
(i) `ν_X(n) ≥ 1` for every m-exceptional n with `(n, P_y) = 1` (incl. n = 1);
(ii) `E_CRT ν_X ≤ 2 e^{−a_v s}`;
(iii) its expansion into congruence classes has total absolute coefficient sum
`T_abs ≤ e^{C_L t s}` (= `e^{C_L t⁴/m}`), every modulus dividing 𝓜 (eq:space, all primes ≤ X).

*Proof.* (i) Lemma 1.1 ⇒ `H_X(n) = 0`; `Q_r(0) = 1`. (ii) note lem:Bonferroni, Lemmas 4.1, 4.2:
`E(Q_r(H_X) | S_y=1) ≤ e^{−a_v s} + (e C_u s/(r+1))^{r+1} ≤ e^{−a_v s} + e^{−(r+1)}`
with `D_B = max(e² C_u, a_v)`. (iii) note (eq:termcount): `log T_abs ≤ π(y) log 2 + log(r+1)
+ r (4/3+κ) t`, with `|𝒜^{(m)}_X| ≤ K X^{4/3}` unchanged, `y ≤ Bs + 2`, `r ≤ D_B s + 2`. Explicitly, using `s, t ≥ 1` (R94A repair D6):
`π(y) log 2 ≤ y ≤ Bs + 2 ≤ (B+2)ts`, `log(r+1) ≤ r ≤ (D_B+2)s`, and `r(4/3+κ)t ≤ 2(D_B+2)ts`.
So `C_L = B + 3(D_B+2) + 2` works. ∎

So the **whole m-dependence is the substitution `t³ → s = t³/m`** in the saving and in the
Bonferroni depth, while the per-atom modulus cost `(1+κ)t` stays — hence the ledger `e^{O(t s)}`.

## 5. Main theorem: E_m in arbitrary intervals, uniformly in m

**Lemma 5.1 (divisor closure for m; PROVED, trivial).** If `n = d n'` and `n'` is
m-representable, so is n (`m/n = Σ 1/(d x_i)`). Hence the `y`-rough part `n'` of an
m-exceptional n is m-exceptional (n' = 1 is m-exceptional for m ≥ 4).

**Theorem A (PROVED rel. note).** There are absolute `c, C > 0` (ineffective, as in the note)
such that for **every** integer `m ≥ 4`, every real z and every `H ≥ 2`,
`E_m((z, z+H]) ≤ C · H · exp(−c (log H)^{3/4} m^{−1/4})`.
In particular `E_m(N) ≤ C N exp(−c (log N)^{3/4}/m^{1/4})` for all `N ≥ 2`, `m ≥ 4`
(the saving `→ ∞` iff `m = o((log N)³)`; for `m ≤ ε(log N)³` with ε = ε(C) small it is a
non-trivial constant factor — R94A repair D2).

*Proof.* SHORT Theorem 1's proof with t³ → s. Fix m, put `𝓗 = log H`. Let X be chosen below
(with `X ≥ X_a`, `m ≤ t³`, `s ≥ s_0`), `D_0 = e^{a_v s}`. Split m-exceptional `n ∈ I` by
their y-smooth part d (SHORT Lemma 1.2; it is m-free).
(i) `d > D_0`: SHORT Lemma 1.2(b),(c): `≤ H D_0^{−1/2} e^{4√y} + y D_0`.
(ii) `d ≤ D_0`: `n' ∈ I/d` is m-exceptional and `(n',P_y) = 1` (Lemma 5.1), so `ν_X(n') ≥ 1`;
SHORT Lemma 1.1 (it uses only that ν_X is a finite combination of congruence classes —
Theorem 4.3(iii)) gives `≤ Σ_{d≤D_0}(2(H/d) e^{−a_v s} + T_abs) ≤ 2H(1 + a_v s) e^{−a_v s} + D_0 e^{C_L t s}`.
Since `y ≤ Bs + 2`, `4√y ≤ a_v s/4` once `s ≥ s_1` (absolute). Altogether
`E_m(I) ≤ C_1 H e^{−a_v s/4} + e^{C_2 t s}`, `C_2 = C_L + a_v + 1`.
Choose `t = (m 𝓗/(2C_2))^{1/4}`, so `e^{C_2 t s} = e^{C_2 t⁴/m} = H^{1/2}` and
`s = t³/m = (𝓗/(2C_2))^{3/4} m^{−1/4}`. The side conditions read
`t ≥ log X_a`, `m ≤ t³ ⟺ m ≤ (𝓗/(2C_2))³`, `s ≥ max(s_0,s_1)`; each fails only if
`𝓗^{3/4} m^{−1/4} ≤ C_3` (absolute). Indeed `s ≥ 1 ⟺ t³ ≥ m`, and `t³ = ms ≥ 4s`, so
`t ≥ log X_a` follows from `s ≥ (log X_a)³/4` (R94B repair D5). In that case the claim is trivial (`E_m(I) ≤ H + 1 ≤ 2H ≤ C H e^{−c C_3}`).
Otherwise `E_m(I) ≤ C_1 H e^{−(a_v/4) s} + H^{1/2} ≤ C H exp(−c 𝓗^{3/4} m^{−1/4})`
(`H^{1/2} ≤ H e^{−s}` as `s ≤ 𝓗^{3/4} ≤ 𝓗/2` for 𝓗 large). ∎

**Theorem B (progressions; PROVED rel. note).** For `q ≥ 1`, `b ∈ Z`, `H/q ≥ 2`, with
`X_q = exp((m log(H/q)/(2C_2))^{1/4})` and `q_1` the X_q-smooth part of q:
`E_m(I; q, b) ≤ C q_1 (H/q) exp(−c (log(H/q))^{3/4} m^{−1/4})`.
Hence the bound without `q_1` (halved c) for `q ≤ exp((c/2)(log(H/q))^{3/4} m^{−1/4})`, and
without loss for q whose prime factors all exceed X_q.
*Proof.* SHORT Lemma 2.1 uses only that all primes of 𝓜 are ≤ X (true: ℓ ≤ X, primes of
`L_K` ≤ K, of `P_y` ≤ y); the rest is the proof of Theorem A with SHORT §2's bookkeeping. ∎
(SHORT's extra remark that *every prime* q is covered does **not** transfer automatically:
it absorbs `log X_q` into the saving, and here `log X_q / ((log(H/q))^{3/4}m^{−1/4}) ≍
(m/log(H/q))^{1/2}` need not be bounded. Primes `q ∈ (exp((c/2)𝓢), X_q]`, `𝓢` the saving, are not covered.)

**Corollary C (primes; PROVED rel. note).** For `x ≥ 3`, `H ≤ x` with
`(log H)^{3/4} m^{−1/4} ≥ (2/c) log log x`:
`#{p ∈ (x, x+H] : p m-exceptional} ≪ (H/log x) exp(−(c/2)(log H)^{3/4} m^{−1/4})`.
E.g. for fixed m: `H ≥ exp(C_m (log log x)^{4/3})`, `C_m ≍ m^{1/3}`.
*Proof.* As SHORT Cor. 3.1. ∎

**Comparison with Pomerance–Weingartner Thm 1.3** (`N/exp(C L^{2/3} φ(m)^{−1/3})`,
`4 ≤ m ≤ L²`). Ratio of exponents: `L^{3/4} m^{−1/4} / (L^{2/3} φ(m)^{−1/3}) =
L^{1/12} φ(m)^{1/3} m^{−1/4} ≫ (Lm)^{1/12}/(log log 3m)^{1/3} → ∞`. Both bounds have
unrelated, ineffective constants, so the comparison is asymptotic only. There is an absolute
(ineffective) Λ_0 such that Theorem A's bound is below PW's whenever `(Lm)^{1/12} ≥ Λ_0 (log log 3m)^{1/3}`.
In particular this holds for each fixed m once N is large, uniformly in `4 ≤ m ≤ L²` for `N ≥ N_0`.
Theorem A's saving tends to ∞ iff `m = o(L³)` (PW's is non-trivial for `m = o(L²)`).
PW's proof also uses Bombieri–Vinogradov, so there is no effectivity trade-off.
(R94A repair D1, D2; R94B repair D2)
Heuristic reason for the shape: both arguments balance a fibre mass μ against a ledger
`e^{O(tμ)}` with `tμ ≍ L`; Vaughan (m = 4) / PW have `μ ≍ t²/φ(m)` ⇒ `μ ≍ L^{2/3}φ(m)^{−1/3}`;
here `μ ≍ t³/m` ⇒ `μ ≍ L^{3/4}m^{−1/4}`.

## 6. Consequence: the density transition for m/n is at log n = m^{1/3+o(1)}

Pomerance–Weingartner (arXiv:2511.16817v2, Thm 3.1 and its proof, PDF pp. 6–8; `sources/pw.txt` lines ~270–450)
show *in the proof* of Thm 3.1 (the statement itself only counts exceptional primes) that *most
primes* `p ∈ (N/2, N]` are m-exceptional (m large) for every N in the range
`e^{m^{1/4}} ≪ N < e^m` (needed for their Type I count `≪ (N/φ(m)) log²N log²m`) with
`log³N · log²m ≤ φ(m)/C` (Type II count `≪ (N/φ(m)) log²N log log N`). That is, for
`m^{1/4} ≪ log N ≤ (φ(m)/(C log² m))^{1/3}`. The exponents were read from the rendered PDF p. 7 by both
reviewers, since `pw.txt` drops superscripts. (R94A repair D3; R94B repair D3) Their Thm 1.3 gives the converse only for `log N ≫ m^{1/2}(log m)^{3/2}`, and they
write (p. 2): "between exp(m^{1/3}) and exp(m^{1/2}) there is a transition from 'usually false'
to 'usually true'"; their Poisson heuristic (p. 3) predicts the transition at `exp(m^{1/3+ε})`.

**Corollary D (PROVED rel. note).** There is an absolute `C_D` such that for all `m ≥ 4`
and all N ≥ 16 with `log N ≥ C_D m^{1/3} (log m)^{4/3}`:
`#{p ∈ (N/2, N] : p prime, m-exceptional} ≤ N/(log N)² = o(π(N) − π(N/2))`;
and for integers, `E_m(N) = o(N)` as soon as `log N / m^{1/3} → ∞`.

*Proof.* Theorem A with I = (N/2, N] gives `≤ C N exp(−c L^{3/4} m^{−1/4})`, `L = log(N/2)`.
Let `f(L) = c L^{3/4} m^{−1/4} − 2 log L`; `f′(L) > 0` iff `L > (8/(3c))^{4/3} m^{1/3}`. At
`L_0 = A m^{1/3}(log m)^{4/3}` with `A ≥ (8/(3c))^{4/3}` (take `C_D = 2A`, so that
`log(N/2) ≥ L_0` under the hypothesis):
`f(L_0) = c A^{3/4} log m − 2 log A − (2/3) log m − (8/3) log log m
≥ (c A^{3/4} − 10/3 − 2 log A/log 4) log m ≥ log(2C)` for A large absolute (`log m ≥ log 4`).
So for `L ≥ L_0`: count `≤ C N e^{−f(L) − 2 log L} ≤ N/(2L²) ≤ N/(log N)²` (`√2·log(N/2) ≥ log N` for N ≥ 2^{2+√2}; N ≥ 16 suffices).
Integers: the saving `(log N)^{3/4} m^{−1/4} = (log N/m^{1/3})^{3/4} → ∞`. ∎

So the *density* transition is at `log N = m^{1/3+o(1)}` in the following sense.
* PW's proof: most primes in `(N/2, N]` are m-exceptional for `m^{1/4} ≪ log N ≤ (φ(m)/(C log² m))^{1/3}`.
* Corollary D: most primes there are m-representable for **all** `log N ≥ C m^{1/3}(log m)^{4/3}`.

Monotonicity in between is not known (R94A repair D3). The remaining
gap is a factor `≍ (log m)² (m/φ(m))^{1/3}` in log N. This confirms the *density* part of PW's
heuristic. It says nothing about the **largest** m-exceptional n (Schinzel's threshold), which
PW's heuristic places near `exp(m^{1/2})` (PW p. 3); Corollary D bounds proportions only.

**Why it matches the heuristic up to bounded and log log factors (Assessment; R94A repair D4).**
Our reduced-fibre mass `μ_c ≍ (log X)³/m` (Cor. 3.2) agrees, up to bounded and `log log` factors, with:
* PW's heuristic intensity `(log³ p/m)(log log p)^{O(1)}` (PW p. 3);
* their rigorous Type II first-moment count `≪ (N/φ(m)) log²N log log N`.

Our count is at scale `X = e^t`, `t ≍ (m log N)^{1/4} ≪ log N`, restricted to `k ≤ X^κ`, `ℓ ∈ (X^{1/2}, X]`; the 3/4 mechanism converts mass μ at
ledger cost `e^{O(tμ)}` into saving `e^{−cμ}`. With `t⁴/m ≍ L` the mass at the chosen scale is
`L^{3/4}m^{−1/4} = (L/m^{1/3})^{3/4}`, which is ≥ 1 when `L ≥ m^{1/3}`, i.e. (up to the factors
above) where the Poisson intensity at scale `X = e^t` with `t ≤ L` can exceed 1.

## 7. Checks, uniformity, and where things could fail

**7.1 Machine checks.**
* `scripts/emn_identity.py`: Lemma 1.1 identity on 4 821 random (m ≤ 60, k ≤ 50, prime ℓ, u,v,w)
  instances, exact rational arithmetic, 0 failures; Lemma 1.3 distinct projections at fixed ℓ
  (m ∈ {4,5,6,7,11,12}, ℓ ∈ (1000,3000), K = 6, `u,v ≤ √ℓ`, `muv > K`): 19 446 atoms, 0 collisions.
* `scripts/emn_hm.py 100000`: Lemma 2.1, 0 failures.
* `scripts/emn_mass2.py 1e6 170 7 60 2` is the primary toy (EVIDENCE, R94A repair D5; output
  `scripts/emn_mass2.out.txt`, 25 s). It is deduplicated, with an m-independent floor `u, v ∈ (7, 60]`, K = 170 ≥ m²,
  `muv > K`, `z² < ℓ`, actual primes ℓ ∈ (10⁶, 2·10⁶], and 2 reduced c.
  * Collisions at fixed ℓ: 0 (Lemma 1.3).
  * For m = 4..13: `m·μ_c ∈ [0.976, 1.129]` while `φ(m)·μ_c ∈ [0.325, 1.042]`. The scaling is `1/m`, not `1/φ(m)`.
  * Independent reviewer toys agree: R94A `m·μ ∈ [11.1, 12.8]`; R94B (dedup, m up to 210) `m·μ ∈ [2.68, 3.10]`.
* The older `scripts/emn_mass.py 1e6 30 40` (output `scripts/emn_mass.out.txt`) counts *incidences*: there is no floor,
  no `muv > K` filter and no deduplication, and its truncation depends on m. It gave `m·μ ∈ [3.85, 4.58]` for
  m = 4..30, 60, 105, 210, and the BV-main-term prediction agreed to ≤ 1.2%. It is superseded by `emn_mass2.py`.
* The residual parity pattern in `m·μ` (≈ 1.0 for even m, ≈ 1.1 for odd m in the v2 run) is a
  configuration-specific observation. No Euler-factor explanation is claimed (R94B repair D6), and Cor. 3.2 does not
  need one.

**7.2 Uniformity in m (goal 3).** All constants in Theorems A, B, Cor. C, D are absolute;
the m-dependence is *exactly* `c_m = c·m^{−1/4}` in the exponent (no φ(m), no log m loss).
Where m enters: (a) `μ ≍ t³/m` (Cor. 3.2, two-sided on reduced fibres); (b) the BV range `m ≤ t³`
(Prop. 3.1), automatically satisfied whenever the saving `s = t³/m ≥ 1`; (c) `K ≥ m²` for
Lemma 2.1 (automatic, K = e^{κt}). Lower-order point: on reduced fibres `m·μ_c/t³` is bounded
above and below by absolute constants; nothing is lost from m/φ(m) because the `1/φ(muv)` gain and the
`h_m ≍ (φ(m)/m) log K` loss cancel to `1/m` with absolute constants (Lemma 2.1, Cor. 3.2; 7.1 data).

**7.3 Is `m^{−1/4}` the right m-dependence for this method? (Assessment.)** Given a mass
`μ ≍ t³/m` at ledger `e^{O(tμ)}`, `μ = (L/m^{1/3})^{3/4}` is forced by `tμ ≍ L`. A larger
mass would need more multipliers: the k-range `K = X^κ` is already a power of X; the
u,v-range `≤ X^{1/6}` per block is what keeps `z² < ℓ` (distinctness). So within the note's
architecture `m^{−1/4}` is the mass-driven ceiling, mirroring note §10's 3/4 ceiling. The
PW lower construction (Thm 3.1: `≫ N/log N` exceptional primes at their
`log N ≍ (φ(m)/log² m)^{1/3}`) only forces any saving there to be `≤ log log N + O(1)`;
it does not decide θ = 3/4.

**7.4 Where the argument fails / what is m-specific (goal 1).**
* Nothing fails for any m ≥ 4. (m ≤ 3: every n is trivially representable.)
* The POINTWISE_MN dichotomy `m ≡ 0 (4)` vs not is **irrelevant** here (§1.4): it concerns
  whether a revealed quadratic class can dodge all events (pointwise witness modulus); the
  density argument only needs *first-moment mass per fibre* and *conditional independence*,
  both character-blind.
* Type I solutions (PW Cor. 2.2) are not used, exactly as
  in the note for m = 4: Type II atoms alone carry the mass `t³/m`.
* The only genuinely m-sensitive inputs are BV (range of moduli `muv`) and Lemma 2.1; both
  are uniform in the range where the theorem is non-trivial.
* Effectivity: as in the note, ineffective (standard BV). Only lower bounds use BV; the
  constants `c, C` are absolute but not computable from the proof.

## 8. Literature (goal 4; web search 2026-10-07 + campaign files)

* **Vaughan 1970** (Mathematika 17; full text not accessible, `sources/vaughan-1970-access-log.md`):
  `E(N) ≪ N exp(−c (log N)^{2/3})`. PW p. 2 and Elsholtz–Tao quote it for **4/n only**. PW's
  abstract says they "generalize a result of Vaughan to show that for each m, most n's have m/n"
  representable. Whether Vaughan's paper itself treats general m is **unverified**: its title names
  Schinzel, but the full text is inaccessible (R94B repair D4). PW Thm 1.3 is the first m-explicit bound we can cite.
* **Pomerance–Weingartner** arXiv:2511.16817v2 (= Dartmouth "ESS-ExceptionsV8", checked
  identical statement of Thm 1.3, 2026-10-07): `E_m(N) ≤ N/exp(C (log² N/φ(m))^{1/3})`,
  `4 ≤ m ≤ log² N`; Thm 1.1/3.1 lower constructions; Poisson heuristic `exp(−(log p)³/m)`.
* No 3/4-type, short-interval or progression result for m/n found (searches: "exceptional set
  m/n three unit fractions", "Erdős–Straus–Schinzel almost all n", "Sierpiński 5/n exceptional set",
  "(log N)^{3/4}"; LITERATURE_2026.md: PW is the only substantial recent work on Sierpiński/Schinzel).
  The 3/4 bound itself is campaign-internal even at m = 4 (novelty audit: "apparently new").
* Hence (Assessment): Theorem A is, as far as we can tell, new for every m ≠ 4 (and its m = 4
  case is SHORT Theorem 1); its m-uniform form and Corollary D (sharp m^{1/3} transition) are new
  relative to PW. Novelty of the *method* is nil beyond the note: it is the note with 4 → m.

## 9. Status

* Theorem A, B, Cor. C, D: **PROVED relative to the note** (and SHORT for the local transfer),
  same internal-only status; the m-transfer is lemma-by-lemma (§§1–5), every change listed.
* §7.1 toy masses: EVIDENCE. §7.3, §6 last paragraph, §8 novelty: Assessment.
* Open: (i) close the `(log m)²` gap in Corollary D (lower side is PW's first-moment count, upper
  side ours); (ii) for `m ≥ ε(log N)³` Theorem A is trivial; PW Thm 3.1 shows no
  saving beyond `log log N + O(1)` is possible at `log N ≍ (φ(m)/log² m)^{1/3}`; (iii) SHORT's open smooth-q progression step carries over unchanged.

## Replay

```
uv run --with sympy python scripts/emn_hm.py 100000            # Lemma 2.1, ~1 min
uv run --with sympy python scripts/emn_identity.py             # Lemmas 1.1, 1.3, ~1 min
ulimit -v 8000000; timeout 1800 uv run --with sympy --with numpy \
    python scripts/emn_mass2.py 1e6 170 7 60 2                 # §7.1 dedup toy masses, ~30 s
ulimit -v 8000000; timeout 1800 uv run --with sympy --with numpy \
    python scripts/emn_mass.py 1e6 30 40                       # §7.1 old incidence toy, ~10 min
```
