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
  `φ(ab) ≤ φ(a)·b`. Harmonic mass after pruning is `≥ (1/8 − o(1))(log z)² h(𝒥)` exactly as in
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

**Scaling.** Fibre mass `≍ t³/m` (lower and upper, absolute constants): the `1/φ(m)` from
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
+ r (4/3+κ) t`, with `|𝒜^{(m)}_X| ≤ K X^{4/3}` unchanged, `y ≤ Bs + 2`, `r ≤ D_B s + 2`, `s ≤ t s`. ∎

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
(non-trivial for `m ≤ ε (log N)^3`).

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
`𝓗^{3/4} m^{−1/4} ≤ C_3` (absolute) — note `t ≥ m^{1/4}·(stuff)` and `m ≤ t³ ⟸ s ≥ 1` since
`s ≥ 1 ⟺ t³ ≥ m` — and then the claim is trivial (`E_m(I) ≤ H + 1 ≤ 2H ≤ C H e^{−c C_3}`).
Otherwise `E_m(I) ≤ C_1 H e^{−(a_v/4) s} + H^{1/2} ≤ C H exp(−c 𝓗^{3/4} m^{−1/4})`
(`H^{1/2} ≤ H e^{−s}` as `s ≤ 𝓗^{3/4} ≤ 𝓗/2` for 𝓗 large). ∎

**Theorem B (progressions; PROVED rel. note).** SHORT Theorem 2 holds verbatim for E_m with
saving `exp(−c (log(H/q))^{3/4} m^{−1/4})` and `X_q = exp((m log(H/q)/(2C_2))^{1/4})`:
`E_m(I; q, b) ≤ C q_1 (H/q) exp(−c (log(H/q))^{3/4} m^{−1/4})`, `q_1` the X_q-smooth part of q.
*Proof.* SHORT Lemma 2.1 uses only that all primes of 𝓜 are ≤ X (true: ℓ ≤ X, primes of
`L_K` ≤ K, of `P_y` ≤ y); the rest is the proof of Theorem A with SHORT §2's bookkeeping. ∎

**Corollary C (primes; PROVED rel. note).** For `x ≥ 3`, `H ≤ x` with
`(log H)^{3/4} m^{−1/4} ≥ (2/c) log log x`:
`#{p ∈ (x, x+H] : p m-exceptional} ≪ (H/log x) exp(−(c/2)(log H)^{3/4} m^{−1/4})`.
E.g. for fixed m: `H ≥ exp(C_m (log log x)^{4/3})`, `C_m ≍ m^{1/3}`.
*Proof.* As SHORT Cor. 3.1. ∎

**Comparison with Pomerance–Weingartner Thm 1.3** (`N/exp(C L^{2/3} φ(m)^{−1/3})`,
`4 ≤ m ≤ L²`). Ratio of exponents: `L^{3/4} m^{−1/4} / (L^{2/3} φ(m)^{−1/3}) =
L^{1/12} φ(m)^{1/3} m^{−1/4} ≫ (Lm)^{1/12}/(log log 3m)^{1/3} → ∞`. So Theorem A is stronger
for every m in PW's range, and non-trivial in the wider range `m ≤ εL³` (PW: `m ≤ εL²`).
Heuristic reason for the shape: both arguments balance a fibre mass μ against a ledger
`e^{O(tμ)}` with `tμ ≍ L`; Vaughan/PW have `μ ≍ t²/φ(m)` ⇒ `μ ≍ L^{2/3}φ(m)^{−1/3}`;
here `μ ≍ t³/m` ⇒ `μ ≍ L^{3/4}m^{−1/4}`.
