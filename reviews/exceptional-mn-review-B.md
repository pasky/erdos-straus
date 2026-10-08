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
