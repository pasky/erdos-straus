# Hostile review A of EXCEPTIONAL_MN.md (R94, reviewer A)

Reviewed: `EXCEPTIONAL_MN.md` at merge of `side-agent/mn-threequarter` (0bc7efc), against
`paper/es-threequarter-note.tex` ("the note"), `EXCEPTIONAL_SHORT.md` ("SHORT"),
`sources/pw.txt` / `sources/pomerance-weingartner-2511.16817/…v2.pdf` ("PW").
From-scratch scripts: `scripts/review_emnA_*.py`.

Status: COMPLETE (round 1).

## Verdict summary (filled in as claims are checked)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (identity for m) | SOUND (re-derived; machine-checked from scratch) |
| Def 1.2 / Lemma 1.3 (atom family, dedup, CRT) | SOUND (re-derived) |
| §1.4 (where 4 is used; Jacobi obstruction irrelevant) | SOUND (grep of the note re-done) |
| Lemma 2.1 (h_m, S_m) | SOUND (re-derived; checked from scratch to K = 2·10⁵, incl. primorial m) |
| Prop 3.1 / Cor 3.2 (fibre mass ≍ t³/m, BV with q = muv) | SOUND (re-derived; toy EVIDENCE reproduced with a better toy) |
| Lemma 4.1 (void, η = 1/4, y = max(2,Bs)) | SOUND |
| Lemma 4.2, Thm 4.3 (moments, Bonferroni, ledger e^{O(t⁴/m)}) | SOUND |
| Theorem A (incl. m^{−1/4} bookkeeping, trivial-range logic) | SOUND rel. note (MINOR wording repairs D1, D2) |
| Theorem B, Cor C | SOUND rel. note + SHORT (the prime-q caveat is correct and necessary) |
| PW comparison (§5) | SOUND-AFTER-REPAIRS (D1: asymptotic, not "for every m") |
| Corollary D (density transition) | SOUND (algebra re-checked); framing MINOR (D3) |
| §6 "matches the heuristic exactly", §7.3 | Assessment — overclaimed wording (D4) |
| §7.1 toy masses | EVIDENCE; toy design flaw, conclusion survives (D5) |

## Claim-by-claim notes

### Lemma 1.1
Re-derived: over the common denominator `n s u v w`, numerators of `1/(suw), 1/(nsvw), 1/(nuvw)`
are `nv, u, s`; `nv+u = s kℓ` so the sum is `s(kℓ+1) = m·suvw`, i.e. the total is `m/n`.
`s ≥ 1` is an integer by hypothesis `kℓ | nv+u`; `w = (kℓ+1)/(muv) ≥ 1`. Holds for every
`n ≥ 1` in the class, so every m-exceptional n (incl. n = 1) avoids every atom. The class is a
unit class: `(v, kℓ) = 1` because `(v,k)=1` (atom definition) and `v < ℓ`. The PW definition
of "m/n not the sum of 3 unit fractions" is `(x,y,z) ∈ N³`, not necessarily distinct
(PW (2.1)), matching MN's. No issue.

### Lemma 1.3
Re-derived each of (i)–(iv). (iii): `kℓ ≡ k'ℓ ≡ −1 (mod muv)`, `ℓ ∤ muv` (ℓ prime,
`ℓ > X^{1/2} > m z_j^2 ≥ muv`; indeed `ℓ | kℓ+1` is impossible anyway), so `k ≡ k' (mod muv)`,
and `muv ≥ 4H^2 > K` forces `k = k'`. (ii) `|uv'−u'v| < z_j^2 ≤ x_j^{1/3} < ℓ`. `m ≤ K < ℓ`
gives `(ℓ, m L_K) = 1`. Conditional independence: the only coordinates of n used by an atom
are `n mod k` (k | L_K) and `n mod ℓ`; CRT over `L_K·Π ℓ` is exact. No m-dependence.

### §1.4 (uses of "4" in the note)
Independent grep of the note (`pmod4`, `4uv`, `equiv1/3`, `24L`, `8/\pi`): occurrences are
eq:parameters (𝒦(K)), lem:identity, eq:atomdef, lem:CRT proof, lem:h, eq:HkBV (an explicitly
*unused* hypothesis, the `24L_J` there is irrelevant), thm:harvest (q = 4uv, φ(4uv) ≥ 2φ(u)φ(v)),
§6 unpruned route (`φ(4uv)`, `2^{ω(q/4)}`), lem:profile/lem:euler ("enlarge to all odd k"; only
in the ordered-atom *alternative* moment proof, which MN does not use — it uses the
conditional-independence proof), §10/§11 (heuristic). MN's list (a)–(f) is complete for the route
it transfers. The density argument never evaluates a quadratic character: the void bound is
`Π_ℓ(1 − f_c(ℓ)/ℓ)` over *independent uniform* coordinates, so even if all atom classes mod ℓ
were non-residues (the pointwise obstruction), only a density-0 set (e.g. squares) could exploit it.
Agree the m ≡ 0 (4) dichotomy of POINTWISE_MN does not enter.

### Lemma 2.1
(a) Re-derived: `S_m(x) = Σ_{e|m} μ(e)/e·(log(x/e)+γ+θ_e e/x)`; the term `−Σ μ(e)log e/e`
equals `F'(1)` for `F(s) = Π_{p|m}(1−p^{−s})`, i.e. `(φ(m)/m)Σ_{p|m} log p/(p−1) ≥ 0`; error
`≤ 2^{ω(m)}/x ≤ 2^{ω(m)}/m² ≤ γφ(m)/m`. ✓ (b) `φ(k)/k ≥ 1 − Σ_{p|k}1/p` and
`Σ_{k∈𝒦_m, p|k} 1/(pk) ≤ S_m(K)/p²`; `Σ_p p^{−2} = 0.45225`. ✓ (c), (d) ✓ (d needs every
prime of m to be ≤ K, true for K ≥ m).
From scratch (`scripts/review_emnA_lemmas.py 200000`, m = 4..40, 60, 210, 2310, 30030;
checkpoints x = m², 10³, 10⁴, 10⁵, K): 0 failures; `S_m(K)/((φ(m)/m) log K) ∈ [1.056, 1.209]`,
`min h_m/S_m = 0.635` — agrees with the author's ranges. (a) even holds for all `x ≤ m²` for the
primorials tested, so the hypothesis `x ≥ m²` is not tight (harmless).
Hidden-m-dependence hunt: the only m-dependence is `φ(m)/m`, and it cancels exactly against
`1/φ(muv) ≥ 1/(φ(m)uv)` (lower) / `1/φ(muv) ≤ 1/(φ(m)φ(u)φ(v))` (upper). m with many small
primes (primorials) are covered: (a),(b),(c) have no `ω(m)` loss once `K ≥ m²`.

### Prop 3.1 / Cor 3.2 (the BV step written out)
Fix a full block `(x,2x]`, `z = x^{1/6}`. Retained triples `(k,u,v)` (pruned, low-ω, `k ∈ 𝒥`)
contribute `Σ_triples [π(2x; muv, −k̄) − π(x; muv, −k̄)]`, `k̄ = k^{−1} mod muv` (reduced: `(k,m)=1`,
`(k,uv)=1`). Write each bracket as `(li 2x − li x)/φ(muv) + E(x; muv, −k̄)`.
*Main:* `≥ (x/log 2x)·(1/φ(m))·Σ 1/(uv) ≥ (x/log 2x)(1/φ(m))(1/32 − o(1))(log z)² h(𝒥)
≫ x log x · h(𝒥)/φ(m)` (`φ(muv) ≤ φ(m)·uv` — true since `φ(muv)/(muv) = Π_{p|muv}(1−1/p) ≤
Π_{p|m}(1−1/p)`).
*Error:* group by `q = muv`; `uv = q/m` is fixed, `≤ 2^{ω(uv)} ≤ t^{D log 2}` coprime splittings,
`≤ T_X = t⁴` multipliers each (pruning), so `Σ|E| ≤ t^{4+D log 2} Σ_{q ≤ t³x^{1/3}} E*_x(q)
≤ t^{4+D log 2} C_R x (log x)^{−R}` by BV (`t³ x^{1/3} ≤ x^{1/2}(log x)^{−A_R}` for x ≥ X^{1/2},
X large, since `m ≤ t³`). Main/err `≫ (log x)^{R+1} t^{−7−D log 2} ≫ 1` for fixed R, using
`h(𝒥) ≥ 1`, `φ(m) ≤ t³`. No m-dependence in R or thresholds once `m ≤ t^{A}` for a fixed A. ✓
*Pruning loss:* harmonic loss `≪ (log z)²(1+log K)³/t⁴ ≪ t` vs main `≥ t² h(𝒥)/32`; weighted
loss multiplies by `muv/φ(muv) ≪ log log(muv) ≪ log t` and by `1/m ≤ 1/φ(m)`, main by
`1/φ(m)`: relative `O(log t/t)`, uniformly in m. ✓ (note lem:congestion is stated for
𝒥 ⊆ 𝒦(K) but its proof only uses k ≤ K; MN's remark is correct.)
*Upper:* BT with `log(2x/(muv)) ≥ (2/3 − o(1)) log x`, `φ(muv) ≥ φ(m)φ(u)φ(v)` (`φ(ab) =
φ(a)φ(b)·g/φ(g)`, g = (a,b)), then lem:latupper and `h(𝒥) ≤ S_m(K) ≤ C(φ(m)/m)κt`. ✓
Distinct classes mod ℓ: Lemma 1.3. ✓ Cor 3.2 for c = 0 etc.: active atoms have `(k,c) = 1`. ✓
Note: Def 1.2's remark that the simplified (no-ω) family of note §6 may also be used is fine
without re-deriving note §6 for m: that family is a superset, so the lower bound follows from the
ω-restricted subfamily, and the upper bound (BT, no ω) and the inventory `≤ K X^{4/3}` are
unchanged.

**From-scratch toy (EVIDENCE, `scripts/review_emnA_mass.py`, output `…mass.out.txt`).**
Deduplicated-by-construction family (`z_j = x_j^{0.33}` so `z_j² < ℓ`, `muv > K`, a floor
`u,v > F` *common to all m* playing the role of H; dedup verified: 0 duplicate classes), actual
primes, `X = 10⁷`, `K = 170 ≥ m²` for m ≤ 13, 3 random reduced c each:
`m·μ_c ∈ [11.1, 12.8]` for m = 4..13 while `φ(m)·μ_c` ranges over [3.7, 11.8].
With `K = 1000`: m ∈ {4,13,30,31,32}: `m·μ_c ∈ [10.6, 16.1]`, `φ(m)μ_c ∈ [3.7, 15.4]`.
So the `1/m` (not `1/φ(m)`) scaling is visible; the residual spread is the bounded Euler factor
`Π_{p|(m,uv)}(1−1/p)` and the small-K edge (`muv > K` bites harder at small m). Unique fibre
c = 0: `φ(m)μ_0 ∈ [1.6, 3.6]` (≍ t²/φ(m)), as stated in MN §3.

### Lemma 4.1 (void) — re-derived
`Z(c) = Σ_{y<p≤K, p|L_K, p|c} 1/p`; for `p > y`, `p | L_K`, the events `p | c` are independent
with probability `1/p` also under `S_y = 1` (CRT; `S_y` only touches primes ≤ y).
`E e^{yZ} ≤ exp((e−1) y Σ_{p>y} p^{−2}) ≤ e^{C_Z}` absolute for every `y ≥ 2`. With
`y = Bs = 8a_v s`: `P(Z > 1/4) ≤ e^{C_Z − 2a_v s}`. On `Z ≤ 1/4`, primes `p ≤ y` with `p | c`,
`p | L_K` are excluded by `S_y` (`c ≡ n mod p`), so `h(𝒥_c) ≥ h_m − Z·S_m ≥ 0.29 S_m ≥
0.29(φ(m)/m)κt/2` (Lemma 2.1(a) needs `K ≥ m²`: `κt ≥ 6 log t + 1`, absolute threshold).
`μ_c ≥ a_h t² h(𝒥_c)/φ(m) ≥ 0.145 κ a_h t³/m = 2a_v s`. Total `(1+e^{C_Z})e^{−2a_v s} ≤ e^{−a_v s}`
for `s ≥ s_0`. All constants absolute. ✓ Using `η = 1/4` against `h_m ≥ 0.548 S_m` with the loss
measured in `S_m` units is exactly right: no `φ(m)/m` mismatch between gain and loss.

### Lemma 4.2, Theorem 4.3 — re-derived
In a fibre, distinct atoms at one ℓ have distinct classes mod ℓ (Lemma 1.3) ⇒ at most one hit per
ℓ ⇒ `H_X | c` is a sum of independent Bernoullis ⇒ `E(H)_j ≤ μ_c^j ≤ (C_u s)^j` (upper bound
holds on every fibre). Bonferroni: `(e C_u s/(r+1))^{r+1} ≤ e^{−(r+1)} ≤ e^{−D_B s} ≤ e^{−a_v s}`
for `r+1 ≥ D_B s`, `D_B = max(e²C_u, a_v)`. ✓ Ledger: `log T_abs ≤ π(y)log 2 + log(r+1) +
r(4/3+κ)t ≤ C_L t s` using `s ≥ 1`, `t ≥ 1`. ✓ (i): `H_X(n) = 0` for every m-exceptional n ≥ 1
(Lemma 1.1 holds for *every* positive n in the class), `Q_r(0) = 1`. ✓

### Theorem A — bookkeeping re-done
(i) `d > D_0 = e^{a_v s}`: `≤ H e^{−a_v s/2 + 4√(Bs+2)} + (Bs+2)e^{a_v s}`;
(ii) `d ≤ D_0`: `≤ 2H(1+a_v s)e^{−a_v s} + e^{a_v s + C_L t s}`. With `t⁴ = m𝓗/(2C_2)`:
`t s = t⁴/m = 𝓗/(2C_2)` (so the ledger is `H^{1/2}`), `s = (𝓗/(2C_2))^{3/4} m^{−1/4}`. ✓
Side conditions: `m ≤ t³ ⟺ s ≥ 1`; `t = (ms)^{1/3} ≥ (4s)^{1/3}`, so `s ≥ s_*` (absolute) forces
t above every absolute threshold (incl. `K ≥ m²`, `m ≤ K`, `t³ ≤ K^{1/2}`, BV thresholds). Below
`s_*` the claim is trivial. The final constant c is `(a_v/4)(2C_2)^{−3/4}`-type, absolute. ✓
The m-uniform exponent `c m^{−1/4}` has no `φ(m)` or `log m` loss: confirmed.
Also checked: no step needs `H ≤ z` or `X ≤ H` (X ≤ H^{1/(2C_2)} anyway since `t ≤ 𝓗/(2C_2)`).

### Theorem B / Corollary C
SHORT Lemma 2.1 needs only that every prime of 𝓜 is ≤ X: true for the m-family (ℓ ≤ X, primes
of `L_K` ≤ K, of `P_y` ≤ y). The proof of SHORT Thm 2 (smooth part d is coprime to q₂ as y < X)
transfers. MN's caveat that SHORT's "every prime q" remark does *not* transfer is correct:
`log X_q / saving ≍ (m/log(H/q))^{1/2}` and `m` may be as large as `(log(H/q))³`. Cor C:
`(c/2)S ≥ log log x` absorbs `1/log x`. ✓

### PW comparison (§5) — checked against `sources/pw.txt` (text of arXiv:2511.16817v2)
PW Thm 1.3 (pw.txt l.69–71): absolute C, for `4 ≤ m ≤ (log N)²`, `#{n ≤ N : m/n not a sum of 3
unit fractions} ≤ N/exp(C(log² N/φ(m))^{1/3})` — counts **integers** n, (x,y,z) ∈ N³ not
necessarily distinct (PW (2.1)), same notion as MN. Exponent ratio
`L^{1/12} φ(m)^{1/3} m^{−1/4} ≫ (Lm)^{1/12}/(log log 3m)^{1/3}` ✓. Since c is unspecified and
ineffective, "beats" is an asymptotic statement (D1). Vaughan's per-m `exp(−c(log N)^{2/3})` is as
quoted by PW (l.48–49); Vaughan 1970 itself not accessed (same as the author).

### Corollary D — re-derived
`f(L) = cL^{3/4}m^{−1/4} − 2 log L` is increasing for `L > (8/(3c))^{4/3}m^{1/3}`; at
`L_0 = A m^{1/3}(log m)^{4/3}`: `f(L_0) = cA^{3/4} log m − 2log A − (2/3)log m − (8/3)log log m
≥ (cA^{3/4} − 10/3 − 2 log A/log 4) log m ≥ log(2C)` for A large. Count `≤ N/(2L²) ≤ N/(log N)²`
(`√2 log(N/2) ≥ log N` iff `N ≥ 2^{3.41}`). ✓ PW Thm 3.1 proof (pw.txt l.276–450): most primes
in `(N/2, N]` are m-exceptional at `N = exp((φ(m)/(C log² m))^{1/3})` ✓; PW p.2 quote on the
`exp(m^{1/3})`–`exp(m^{1/2})` window ✓. Gap factor `(log m)²(m/φ(m))^{1/3}` ✓. Consistency check:
at PW's N, Theorem A's saving is `≍ (φ(m)/log² m)^{1/4} m^{−1/4} ≪ (log m)^{−1/2}` — trivial, no
contradiction.

### Brute force: actual m-exceptional n (EVIDENCE; `scripts/review_emnA_exceptions.py`)
Independent solver (x = smallest denominator in `(n/m, 3n/m]`, two-unit-fraction criterion
"∃ d₁,d₂ | b with a | d₁+d₂" — necessity proof: write y = g y', z = g z', (y',z') = 1; then
`y'z' | b`, `ag = e(y'+z')` with `b = y'z'e`, and `d_i = (a,e)·y', (a,e)·z'` work — cross-checked
against naive search, 0 mismatches; composites enumerated from exceptional primes via divisor
closure). Output `scripts/review_emnA_exceptions.out.txt`.
* m = 4..15, n ≤ 10⁶: exactly PW Table 1 (pw.txt l.837–896) restricted to n ≤ 10⁶ (e.g. m = 8:
  {1,2,3,11,17,131,241}; m = 12: 24 values up to 12241; m = 15: 32 values up to 20521).
* m = 16..24, n ≤ 10⁶: counts 48, 21, 54, 24, 80, 35, 68, 65, 194 — all exceptions small;
  highly composite m (12, 16, 18, 20, 24) have visibly more exceptions (local factors), consistent
  with bounded Euler factors, not with any m-uniformity failure.
* N = 10⁵: `E_m(N)/N` = 1.6 %, 6.1 %, 11.9 %, 25.8 %, 43.5 % for m = 60, 120, 210, 420, 840
  (`log N / m^{1/3}` = 2.9, 2.3, 1.9, 1.5, 1.2): the qualitative density transition at
  `log N ≍ m^{1/3}` is visible. None of this can test Theorem A (c, C unspecified).

## Defects

No FATAL and no MAJOR defect found. The transfer 4 → m is lemma-by-lemma correct and every
constant I traced is absolute; the claimed `m^{−1/4}` uniformity holds.

**D1 (MINOR) — §0 bullet 1, §5 "Comparison", AGENT_REPORT item 2.** "Beats PW … for every m in
their range" is asymptotic only (c ineffective, unrelated to PW's C). *Repair:* "for
`N ≥ N_0` (absolute, ineffective), uniformly in `4 ≤ m ≤ (log N)²`, the exponent of Theorem A
exceeds PW's; the ratio is `≫ (Lm)^{1/12}/(log log 3m)^{1/3}`."

**D2 (MINOR) — §0, Theorem A "(non-trivial for m ≤ ε(log N)³)", §5 "extends it to m ≤ εL³".**
At `m ≍ εL³` the saving is a bounded constant `≍ c ε^{−1/4}`, so the bound beats the trivial one
only if ε is small in terms of the ineffective C. *Repair:* "the saving tends to ∞ iff
`m = o((log N)³)`; for `m ≤ ε(log N)³` with ε = ε(C) small it is a non-trivial constant factor".

**D3 (MINOR) — §6 Cor. D framing.** "Density transition at `log n = m^{1/3+o(1)}`" is correct
only as: (PW) most primes exceptional at (a range of) N with `log N ≤ (φ(m)/(C log² m))^{1/3}`,
(MN) most primes representable for *all* `log N ≥ C_D m^{1/3}(log m)^{4/3}`; monotonicity in
between is not known. MN states "at their specific log N"; PW's proof actually gives a range
(PDF p. 7, read from the rendered page since pw.txt drops superscripts: the Type I count
`≪ (N/φ(m)) log² N log² m` is proved under `e^{m^{1/4}} ≪ N < e^m`, and the Type II count is
`≪ (N/φ(m)) log² N log log N`; so the argument gives "most primes in (N/2,N] are m-exceptional"
for every N with `m^{1/4} ≲ log N ≤ (φ(m)/(C log² m))^{1/3}`) — citing the range would strengthen
the statement. *Repair:* one sentence, as above.

**D4 (MINOR, Assessment wording) — §0 "Mechanism", §6 "Why it matches the heuristic exactly".**
PW's heuristic intensity is `(log³ p/m)(log log p)^{O(1)}` (pw.txt l.80–84) and their rigorous Type II
first-moment count is `≪ (N/φ(m)) log² N log log N` (l.~430), i.e. intensity `≲ (log N)³ loglog N/φ(m)`.
MN's `μ_c ≍ t³/m` agrees up to bounded/loglog factors, at scale `t ≍ (m log N)^{1/4} ≪ log N`. *Repair:*
replace "exactly" by "up to bounded and log log factors".

**D5 (MINOR) — §7.1 toy masses.** The author's toy has no common floor for u,v, so the
`muv > K`-type truncation and u = v = 1 collisions depend on m (author's own caveat). *Repair:*
use a deduplicated toy with an m-independent floor and `K ≥ m²`; mine
(`review_emnA_mass.py 1e7 170 0.33 0 7`) gives `m·μ_c ∈ [11.1, 12.8]` for m = 4..13 vs
`φ(m)μ_c ∈ [3.7, 11.8]` — a cleaner confirmation of the `1/m` scaling.

**D6 (MINOR, cosmetic) — Thm 4.3(iii) proof "`s ≤ t s`".** Spell out: `π(y)log 2 ≤ y ≤ Bs+2
≤ (B+2)ts`, `log(r+1) ≤ r ≤ (D_B+2)s`, `r(4/3+κ)t ≤ 2(D_B+2)ts` (uses `s, t ≥ 1`).

**D7 (MINOR, scope) — Def 1.2 parenthesis on the simplified route.** Only the original (ω-cutoff,
pruned) route of the note is re-derived for m. Using the no-ω family is still fine (superset:
lower bound via the ω-subfamily; BT upper bound and inventory unchanged), but say so rather than
implying note §6 was transferred.

## Overall
Theorem A, Theorem B, Cor. C, Cor. D: **SOUND relative to the note (and SHORT)**, with MINOR
wording repairs D1–D7. The label "PROVED rel. note" is appropriate; the note itself remains
internally reviewed only, so nothing here is externally verified.
