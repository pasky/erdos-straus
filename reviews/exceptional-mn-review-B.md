# R94 — hostile review B of EXCEPTIONAL_MN.md (task O94)

Reviewer B, branch `side-agent/review-emn-b` (author files merged from `side-agent/mn-threequarter`).
Scope: EXCEPTIONAL_MN.md — Lemma 1.1–1.3, Lemma 2.1, Prop. 3.1, Cor. 3.2, Lemma 4.1–4.2, Thm 4.3,
Theorem A, Theorem B, Cor. C, Cor. D, the Pomerance–Weingartner (PW) comparison, §§7–8.
The note `paper/es-threequarter-note.tex` and EXCEPTIONAL_SHORT.md are taken as given (reviewed
elsewhere); I check only the 4 → m transfer and the new claims. PW = arXiv:2511.16817v2,
read in `sources/pw.txt` (full text available locally). Vaughan 1970: **not accessible** (see
`sources/vaughan-1970-access-log.md`); only secondary quotations checked.

## Verdict summary

| claim | verdict |
|---|---|
| Lemma 1.1 (identity `kℓ+1 = m·uvw` ⇒ class m-representable) | SOUND (re-derived; exhaustive check) |
| Def. 1.2 / Lemma 1.3 (atom family, dedup, CRT independence) | SOUND |
| §1.4 (only uses of `4` in the note; Jacobi obstruction irrelevant) | SOUND, one MINOR omission (simplified route, D1) |
| Lemma 2.1 (h_m) | SOUND (re-derived; numerics 0 failures incl. primorial m) |
| Prop. 3.1 (pruned prime slice, BV uniform in m ≤ t³, modulus muv) | SOUND (BV step written out below) |
| Cor. 3.2 (fibre mass `≍ t³/m` on reduced fibres, `≪ t³/m` on all) | SOUND; independently confirmed numerically (EVIDENCE) |
| Lemma 4.1 (void with absolute η = 1/4, y = max(2,Bs)) | SOUND |
| Lemma 4.2, Thm 4.3 (moments, Bonferroni, ledger `e^{O(ts)}`) | SOUND |
| Theorem A (`E_m(I) ≤ CH exp(−c (log H)^{3/4} m^{−1/4})`, absolute c, C) | SOUND (rel. note + SHORT) |
| m^{−1/4} bookkeeping / "no φ(m), log m loss" | SOUND |
| Theorem B, Cor. C | SOUND (rel. SHORT); caveat on prime q is correct |
| PW Thm 1.3 comparison ("beats for every m in their range") | SOUND-AFTER-REPAIRS (D2: asymptotic, not literal) |
| Cor. D (density transition `log n = m^{1/3+o(1)}`) | SOUND-AFTER-REPAIRS (D3: cite PW's *proof* range, not Thm 3.1's statement) |
| §8 literature (Vaughan "for each m") | GAP in citation only (D4) |

No FATAL or MAJOR defect found. The transfer really is `t³ → t³/m`: the two m-sensitive
factors (`1/φ(muv)` from the prime progression and `h_m ≍ (φ(m)/m) log K` from the multiplier
set) cancel to `1/m` with absolute constants, and every other step is m-blind.

## 1. Re-derivations (claim by claim)

**1.1 Lemma 1.1.** Over the denominator `nsuvw` the numerators are `nv + u + s = s·kℓ + s =
s(kℓ+1) = m·suvw`. `(v,kℓ) = 1` because `v | kℓ+1`, so the class `nv ≡ −u (kℓ)` exists and
`s ≥ 1` for n ≥ 1. All three denominators are positive integers; no distinctness is claimed or
needed (PW's definition, eq. (2.1), allows repetition). **Check** (`scripts/review_emnB_lemmas.py`):
*exhaustive* over m ∈ [4,40), k < 30, ℓ < 60 (ℓ not required prime), **all** factorisations
`(kℓ+1)/m = uvw`, and every n ≤ 3kℓ in the class: 73 497 instances, exact rationals, 0 failures.
The multiplier condition `k ≡ 1 (4)` of the note is replaced by `(k,m)=1`, which is exactly what
`m | kℓ+1` forces; ES-solvability (here: m-solvability) of every positive n in the class is
implied for every m, with no further condition on k, ℓ, u, v. SOUND.

**1.2 Lemma 1.3.** (ii) `|uv'−u'v| < z_j² = x_j^{1/3} < ℓ` is m-free. (iii) `kℓ ≡ k'ℓ ≡ −1 (muv)`
with `(ℓ,muv)=1` (ℓ prime `> X^{1/2} > max(m, z_j²)`) gives `k ≡ k' (muv)` and `muv ≥ 4H² > K`,
so `k = k'`. (iv) all ℓ coprime to `L_K` and to 𝓜/ℓ. Activation `k | u+cv` ⟺ `c ≡ −uv^{−1} (k)`.
The hypothesis "m ≤ K" in the statement is never used by the proof except for `ℓ ∤ m`, which
already follows from `ℓ > X^{1/2} > t³ ≥ m`. SOUND.

**1.3 Lemma 2.1.** Re-derived: (a) Möbius/harmonic expansion with `|Σ_{i≤y}1/i − log y − γ| < 1/y`
(true for real y ≥ 1), error `≤ 2^{ω(m)}/x`, and `−Σ_{e|m}μ(e)log e/e = (φ(m)/m)Σ_{p|m}log p/(p−1) ≥ 0`;
(b) `φ(k)/k ≥ 1 − Σ_{p|k}1/p` and `Σ_{k∈𝒦_m, p|k} 1/k = S_m(K/p)/p` for `p ∤ m`, `Σ_p p^{−2} = 0.4522…`;
(c) `k = pj`; (d) Mertens with absolute constant, all `p | m` are `≤ K` once `K ≥ m`. **Check**
(from scratch, `review_emnB_lemmas.py 100000`): m = 4..300 plus 210, 2310, 30030, 510510/17,
4·9·25·49 — (a) on a grid of x ∈ [m², 10⁵], (b) at 1 000+ values of K, (c) for p ∈ {2,3,5,7,11,13,101}
∤ m: 0 failures; `S_m(K)/((φ(m)/m)log K) ∈ [1.05,1.26]`, `h_m/S_m ∈ [0.64,0.99]`. SOUND.

**1.4 Prop. 3.1 — the BV step written out (uniform in 4 ≤ m ≤ t³).** Fix a full block (x,2x],
`z = x^{1/6}`, `t/2 ≤ log x ≤ t`. Retained triples `(k,u,v)`: `k ∈ 𝒥 ⊆ 𝒦_m(K)`,
`(u,v) ∈ 𝒮(k,c;H,z)`, `ω(uv) ≤ D log log X`, `r_𝒥(u,v;c) ≤ t⁴`. Each needs
`ℓ ≡ −k^{−1} (mod q)`, `q = muv`, a reduced class since `(k,m) = (k,uv) = 1`.
Then
`Σ_{x<ℓ≤2x} f^{good}(ℓ) = Σ_triples (li 2x − li x)/φ(muv) + Σ_triples E(x; muv, −k^{−1})`.
*Main term:* `φ(muv) ≤ φ(m)·uv` (`φ(ab) = ab Π_{p|ab}(1−1/p) ≤ φ(a)b`), so main
`≥ (x/(φ(m) log 2x)) Σ 1/(uv)`; lem:omega (per k, needs only `(c,k)=1`) gives `≥ (1/8)(φ(k)/k²)Λ²`
per k, so `≥ (1/32)(log z)² h(𝒥)` before pruning; the pruned harmonic mass is
`≤ t^{−4}·C(log z)²(1+log K)³ ≪ t` (lem:congestion holds for every `𝒥 ⊆ [1,K]`), negligible against
`(log z)² h(𝒥) ≫ t²` since `h(𝒥) ≥ 1`. In *weighted* units the pruned loss uses
`1/φ(muv) ≤ (muv/φ(muv))/(muv) ≪ log t /(m uv) ≤ log t/(φ(m)uv)` — the same factor `1/φ(m)` as the
main term, so the relative loss is `O(log t/t)` uniformly in m. Main `≥ a x log x · h(𝒥)/φ(m)`.
*Error term:* group by q. For fixed q (with `m | q`) the pair `(u,v)` is one of `≤ 2^{ω(q/m)} ≤ (log X)^{D log 2}`
coprime splittings of `q/m`, each with `≤ t⁴` retained k (and distinct k give distinct classes mod q,
irrelevant since `E^*` is a max). So `|Σ E| ≤ t^{4+D log 2}·Σ_{q ≤ m x^{1/3}} E^*_x(q)`.
`m x^{1/3} ≤ t³x^{1/3} ≤ 8(log x)³x^{1/3} ≤ x^{1/2}(log x)^{−A_R}` for x ≥ x_R. By (eq:BV) with
R ≥ 4 + D log 2 + 13 + 1: `|Σ E| ≤ C x (log x)^{−13}`.
*Comparison:* main `≥ a x (log x) /φ(m) ≥ a x (log x)/t³ ≥ (a/8) x (log x)^{−2}` (`φ(m) ≤ m ≤ t³`,
`t ≤ 2 log x`). So the error is `o(main)` with a threshold depending only on (κ, D, R) — absolute.
*Upper bound:* BT with `q = muv ≤ x^{0.34}`, `log(2x/q) ≥ 0.6 log x`, and `φ(muv) ≥ φ(m)φ(u)φ(v)`
(`φ(ab) = φ(a)φ(b)·g/φ(g)`, g = (a,b)), then (eq:latupper). Dividing by x and summing over `≍ t`
blocks gives `a_h t² h(𝒥)/φ(m) ≤ Σ f/ℓ ≤ A_h t² h(𝒥)/φ(m)` with absolute constants. SOUND.
The range `m ≤ t³` enters only in the comparison above (any `m ≤ t^A` works with R = R(A)), as claimed.

**1.5 Cor. 3.2.** Upper on every c: `h(𝒥_c) ≤ h_m(K) ≤ S_m(K) ≤ C(φ(m)/m)κt` ⇒ `μ_c ≤ C_u t³/m`.
Lower on reduced c: `h_m(K) ≥ 0.54·S_m(K) ≥ 0.54(φ(m)/m)·κt/2` (needs `K ≥ m²`: true as
`m ≤ t³ ≤ e^{κt/2}` for t large) ⇒ `μ_c ≥ a_u t³/m`. The `φ(m)` cancels exactly. SOUND.
**Independent numerics (EVIDENCE, `scripts/review_emnB_mass.py`, output `review_emnB_mass.out.txt`).**
Written from scratch and *deduplicated* (counts distinct classes mod ℓ, which is what enters
`Π(1 − f_c(ℓ)/ℓ)`), actual primes ℓ ∈ (10⁶, 2·10⁶], K = 20, `u,v ≤ x^{1/3}`, 3 random reduced c,
13 values of m including 30, 60, 105, 210. Measured μ agrees with the BV main term
`Σ 1/φ(muv)·∫dt/(t log t)` to ≤ 1.3 %, and `m·μ ∈ [2.68, 3.10]` while `φ(m)·μ ∈ [0.67, 2.76]`:
the `1/m` (not `1/φ(m)`) scaling is clearly visible (m = 210 has m/φ(m) = 4.4). This confirms the
author's §7.1 with a different configuration and with deduplication (dedup loss was 0 here).

**1.6 Lemma 4.1.** Z only runs over `p | L_K`, i.e. primes ≤ K not dividing m; for `p ≤ y` the
selector kills `p | c` (`p | L_K` ⇒ (`p | c` ⟺ `p | n`)); (eq:Zmoment) is m-free.
On `Z ≤ 1/4`: `h(𝒥_c) ≥ h_m − Σ_{p|c, y<p≤K, p∤m} S_m(K)/p ≥ (0.5477 − 0.25) S_m(K) ≥ 0.29 S_m(K)`,
both sides in units of `S_m(K)`, so η = 1/4 is genuinely absolute (the note's η ≤ a_0/4 is replaced
by `η < 1 − Σp^{−2} − 0.29`). Then `μ_c ≥ 0.145 κ a_h t³/m = 2a_v s`; with `y = Bs`, `B = 8a_v`,
`P(Z > 1/4) ≤ e^{C_Z − 2a_v s}`; total `(1+e^{C_Z})e^{−2a_v s} ≤ e^{−a_v s}` for `s ≥ s_0`. SOUND.
(Small point: the bad-fibre bound needs `y = Bs`, i.e. `s ≥ 2/B`; this is included in s_0.)

**1.7 Lemma 4.2 / Thm 4.3.** In a fibre, `H_X = Σ_ℓ B_ℓ` with independent `B_ℓ ~ Bernoulli(f_c(ℓ)/ℓ)`
(distinct classes mod ℓ), so `E(H)_j = j!·e_j(p_ℓ) ≤ μ_c^j ≤ (C_u s)^j`. Bonferroni (r even):
`1_{H=0} ≤ Q_r(H) ≤ 1_{H=0} + C(H,r+1)`, giving `e^{−a_v s} + (eC_u s/(r+1))^{r+1} ≤ e^{−a_v s} + e^{−(r+1)}`
for `r ≥ e²C_u s`. Ledger: `|𝒜^{(m)}_X| ≤ K·X·X^{1/3}`, `2^{π(y)}` selector terms, so
`log T_abs ≤ (B+2)s log 2 + log(r+1) + r(4/3+κ)t ≤ C_L t s` (t ≥ 1, s ≥ s_0 ≥ 1). SOUND.

**1.8 Theorem A.** With `t⁴ = m𝓗/(2C_2)`: `e^{C_2 ts} = e^{C_2 t⁴/m} = H^{1/2}`,
`s = t³/m = (𝓗/(2C_2))^{3/4} m^{−1/4}` — the m-exponent −1/4 checks. Smooth-part split (SHORT 1.2
is m-free; `1` is m-exceptional for m ≥ 4 since m/1 > 3): (i) `H e^{−a_v s/2 + 4√(Bs+2)} + yD_0`;
(ii) `2H(1+a_v s)e^{−a_v s} + D_0 e^{C_L ts}`. All side conditions (`X ≥ X_a`, `m ≤ t³`, `s ≥ s_0,s_1`)
reduce to `s ≥ C_3` because `t³ = ms ≥ 4s`; otherwise the bound is trivial. Final constant
`c = (a_v/4)(2C_2)^{−3/4}`, absolute. SOUND (relative to the note's thm:assembly machinery and SHORT
Lemmas 1.1–1.2, which I did not re-audit).

**1.9 Theorem B / Cor. C.** SHORT Lemma 2.1 needs only that every prime of 𝓜 is ≤ X (ℓ ≤ X,
primes of `L_K` ≤ K, of `P_y` ≤ y) — m-free. Cor. C is Theorem A plus `e^{−cS/2} ≤ 1/log x` when
`S ≥ (2/c) log log x`; `C_m ≍ m^{1/3}` checks. The author's caveat that SHORT's "every prime q"
remark does not transfer is correct: `log X_q = (m log(H/q)/(2C_2))^{1/4}` vs saving
`≍ (log(H/q))^{3/4}m^{−1/4}`, ratio `≍ (m/log(H/q))^{1/2}`. SOUND (rel. SHORT).
(The hypothesis `H ≤ x` in Cor. C is unused; harmless.)

## 2. Pomerance–Weingartner comparison and Corollary D (checked against `sources/pw.txt`)

* **Definition.** PW (2.1): `m/n = 1/x+1/y+1/z`, `x,y,z ∈ ℕ`, repetitions allowed — same as
  EXCEPTIONAL_MN. Confirmed operationally: my from-scratch brute force (below) reproduces PW Table 1.
* **PW Thm 1.3 (pw.txt l.69–71):** "for each pair m, N with `4 ≤ m ≤ (log N)²` the number of n ≤ N
  with m/n not the sum of 3 unit fractions is at most `N/exp(C(log²N/φ(m))^{1/3})`". Counts
  **integers**, has **φ(m)**, range `m ≤ (log N)²` — all as quoted by the author (after the
  self-review repair). PW's proof also uses Bombieri–Vinogradov (pw.txt l.600), so it is no more
  effective than Theorem A — there is no effectivity trade-off to mention.
* **Exponent ratio** `L^{3/4}m^{−1/4}/(L^{2/3}φ(m)^{−1/3}) = L^{1/12}φ(m)^{1/3}m^{−1/4} ≫
  (Lm)^{1/12}/(log log 3m)^{1/3}` — correct (φ(m) ≫ m/log log 3m). See D2 for the quantifier.
* **PW Thm 3.1 (l.270–273)** as *stated* only gives "more than `exp{cφ(m)^{1/3}/(log m)^{2/3}}`
  exceptional primes". The "most primes in (N/2,N] are m-exceptional" statement is in the
  **proof** (l.437–448: "most primes p ∈ (N/2,N] are covered neither by Type I nor Type II
  congruences if `φ(m)/log²m = C log³N`") and in the intro (l.74–79). The author cites "Thm 3.1
  and its proof" — acceptable; see D3.
* **Cor. D arithmetic** re-checked: `f′(L) > 0 ⟺ L > (8/(3c))^{4/3}m^{1/3}`; at
  `L_0 = A m^{1/3}(log m)^{4/3}`, `cL_0^{3/4}m^{−1/4} = cA^{3/4} log m`; `−(2/3)log m − (8/3)log log m
  ≥ −(10/3) log m`; `(log N)² ≤ 2 log²(N/2)` for `N ≥ 11`. Gap factor `(log m)²(m/φ(m))^{1/3}` = ratio
  of `m^{1/3}(log m)^{4/3}` to `(φ(m)/log²m)^{1/3}` — correct. Consistency: at PW's N the saving
  `(L³/m)^{1/4} = (φ(m)/(Cm log²m))^{1/4} < 1`, so Theorem A is trivial there (no contradiction).

## 3. Brute force (from scratch; EVIDENCE)

`scripts/review_emnB_exc.py` decides m-representability of m/n for *every* n ≤ N0 directly
(x ∈ (n/m, 3n/m]; then `a/b = 1/y+1/z` iff ∃ coprime y′,z′ with `y′z′ | b`, `a | y′+z′`).
* m = 4..15, **all n ≤ 25 000**: the exceptional sets coincide **exactly** with PW Table 1
  (pw.txt l.882–896), including composites (m=12: 25; m=13: 14; m=14: 841; m=15: 16, 34, 122, 226)
  — `scripts/review_emnB_exc.out.txt`, 2 s.
* Larger m, n ≤ 10⁵ (`review_emnB_exc_bigm.out.txt`), `E_m(10^j)`, j = 1..5:
  m=16 [8,18,32,44,48], 30 [9,36,93,147,184], 60 [10,65,262,740,1570], 210 [10,95,636,3055,11908].
  Densities fall with n for fixed m and rise with m, as the theory predicts; with ineffective c, C
  these data cannot test Theorem A quantitatively (they are not offered as such).

## 4. Defects

**D1 (MINOR) — simplified (unpruned) route asserted but not re-run.** Def. 1.2 says the
`ω(uv) ≤ D log log X` cutoff is kept "on the retained original route; the simplified route of note §6
drops it", and §1.4 lists only the pruned route's uses of 4. The note's §6 (thm:unpruned, lem:wsecond)
uses `φ(4uv) ≥ 2φ(u)φ(v)` and a Cauchy–Schwarz with weight `1/φ(4uv)`; its m-version is not written.
*Repair:* add one paragraph: `φ(muv) ≥ φ(m)φ(u)φ(v)`, so `Σ_q W_c(q)²E^*_x(q) ≪ (x/log x)φ(m)^{−1}C_3(log z)⁴(1+log K)³
≪ x t⁶/φ(m)`; with `Σ_{q≤m x^{1/3}}E^* ≤ C x(log x)^{−R}` the error is `≪ x t³φ(m)^{−1/2}(log x)^{−R/2}`,
against main `≫ x t h(𝒥)/φ(m)`: ratio `≪ t²φ(m)^{1/2}(log x)^{−R/2} ≤ t^{7/2}(log x)^{−R/2}` → 0 for
R = 26. (So the route does transfer; alternatively delete the parenthetical.)

**D2 (MINOR) — "beats PW Thm 1.3 for every m in their range" is an asymptotic, not literal, statement.**
Location: §0 bullet 1, §5 "Comparison", O94 report item 2. Both bounds have unrelated, ineffective
constants (c, C here; C in PW). What is proved is: there is an absolute (ineffective) Λ_0 such that
Theorem A's bound is below PW's whenever `(Lm)^{1/12} ≥ Λ_0 (log log 3m)^{1/3}` (in particular for each
fixed m once N is large, and for all m ≥ Λ_0^{12+ε} in PW's range). *Repair:* say exactly that.

**D3 (MINOR) — Cor. D / §6: cite the range PW's proof gives, not a single N.** "Density transition at
`log n = m^{1/3+o(1)}`" is a statement about a range of N. PW's proof (l.360–448) shows "most primes in
(N/2,N] are m-exceptional" for every N with `e^{m^{1/6}} ≪ N < e^{m^{1/4}}` and `log³N·log²m ≤ φ(m)/C`
(Type I bound needs the first, Type II the second), i.e. on `log N ∈ [m^{1/6}, (φ(m)/(C log²m))^{1/3}]`.
*Repair:* state that range explicitly (and that it is PW's proof, not the statement of Thm 3.1), so the
transition claim is "most primes exceptional for log N ≤ m^{1/3−o(1)} (down to m^{1/6}), most
representable for log N ≥ m^{1/3+o(1)}".

**D4 (MINOR) — §8 Vaughan attribution unsupported by the cited source.** §8 states Vaughan gave
"for each m, `E_m(N) ≪_m N exp(−c_m(log N)^{2/3})` (as quoted by PW p. 2 and the campaign)". PW p. 2
(pw.txt l.46–50) quotes Vaughan's bound only for 4/n; Elsholtz–Tao (1107.1010, l.103–105) likewise; PW's
abstract says they "generalize a result of Vaughan to show that for each m, most n's have m/n
representable". Vaughan's paper is inaccessible. *Repair:* "Vaughan 1970 (quoted for m = 4 by PW and
E–T; whether the paper treats general m — its title mentions Schinzel — is unverified)". This does not
affect any PROVED claim, only the novelty Assessment.

**D5 (MINOR, cosmetic) — Theorem A side-condition sentence.** "note `t ≥ m^{1/4}·(stuff)`" is vague;
the clean statement is `t³ = m s ≥ 4s`, so `t ≥ log X_a` follows from `s ≥ (log X_a)³/4`.
Likewise Lemma 1.3's hypothesis "every m ≤ K" should read "m ≤ t³" (only `ℓ ∤ m` is used).

**D6 (MINOR) — §7.1 Euler-factor explanation is unverified.** The sentence attributing the residual
m-dependence to "`Π_{p|m} p/(p+1)·(m/φ(m))`-type" factors and the parity pattern (3.9 vs 4.4) is a
configuration-specific observation (my K = 20, z = x^{1/3} run gives `m·μ` ≈ 2.7 for even m, 2.9–3.1 for
odd m). Label as EVIDENCE/observation or drop; Cor. 3.2 does not need it.

## 5. Bottom line

Theorem A (with the exact `m^{−1/4}` uniformity and absolute c, C), Theorem B, Cor. C and Cor. D are
SOUND relative to the note and SHORT; the m-transfer was re-derived line by line and the decisive
`1/φ(m) × φ(m)/m = 1/m` cancellation was confirmed numerically from scratch. Only MINOR repairs
(D1–D6), all wording/citation level. Novelty (§8) remains an Assessment; ES is not solved.

Scripts: `scripts/review_emnB_lemmas.py`, `review_emnB_exc.py`, `review_emnB_mass.py` (+ `.out.txt`).
