# FF_THIRDS_CORNER — Conjecture 0.2 at q = 3: the thirds corner versus the sterile point x*_c (O227, wave Z-d1)

Status: checkpoint 1 (O227), reviewed by R247 (reviews/ff-thirds-corner-review.md; repairs marked "(R247 repair)", incl. new Lemma 3.3); report reviews/agent-reports/AGENT_REPORT_O227.md. ES is not solved here, nor any infinite case of ES or ES_q. Labels as in DISCOVERIES.md.
Builds on FUNCTIONFIELD_ES2.md §0.2 (Case A, Conjecture 0.2), FUNCTIONFIELD_ES3.md (Lemmas 1.1, 1.2, 2.1, 2.3; searches),
FF_STERILE_PUSH.md (notation (B), Lemma 1.1, §5; reviews R217/R218), FF_STERILE_SMALL.md ((J)56). Scripts `scripts/zt_*`.

Setting: q = 3 unless stated (most algebra holds for every odd q), A = T^k, k ≥ 2 (mostly k = 2), c ∈ F_q^*,
x*_c ≡ 1 at every prime ≠ T, x*_c ≡ u := 1 + cT (mod T^∞). Case B tuple (m', g', w, C) of parameter s, as in FF_STERILE_PUSH (B):
  m'w₁C₁ = T^{s−2} + v₁,  w₁ + C₁ = Tg'v₁,  w = Tw₁, C = TC₁, v = T²v₁,  E = L'w − 1, E' = L'C − 1, L' = g'm',
degrees a = deg w, b = deg C, z = deg m', y = deg g', t = deg v; a + b + z = s, y + t = max(a, b).
A tuple covers the slice point x_u iff E ≡ −u (mod T^{N(s)+1}), N(s) = ⌈(s + k − 2)/2⌉ (largest cylinder among the
families sharing the tuple, FUNCTIONFIELD_ES3 Lemma 1.1 with Lemma 3.1).

## 0. Iteration log

* (I1) Goal 1 is answered by a one-line degree argument, not by a Frobenius/cyclotomic computation: the identity
  E·C₁ = g'T^{s−1} + w₁ turns "E ≡ −u (mod T^m)" into the T-adic approximation w₁/C₁ ≡ −u (mod T^m). For a polynomial u
  of low degree this is a Liouville-type statement: the approximation has quality m but "height" max(a − 1, b), so
  covering forces max(a − 1, b) ≥ m unless w₁ = −uC₁ exactly. At x*_c (m = N + 1 ≈ s/2) this kills the whole thirds corner
  (a ≈ b ≈ s/3), in particular every cyclotomic tuple (§1).
* (I2) Barrier as steering wheel: the union-bound barrier at q = 3 assumes all patterns can reach the target. At a
  polynomial point they cannot; the remaining (lopsided) patterns admit a complete search costing ≈ 3^N per level (§2).
* (I3) A random-remainder lottery model over-predicted hits at control points by ≈ 10×; two more exact constraints
  (second Liouville constraint Cor 3.2; parity laws, incl. O226's z ≡ t ≡ s) brought it to the right order (§3).
* (I4) A proof attempt via the Bezout form (§5) found no further structure: the residual condition is a lottery.

## 1. The Liouville lemma

**Lemma 1.1 (R3 identity; PROVED).** E·C₁ = g'T^{s−1} + w₁ and E'·w₁ = g'T^{s−1} + C₁.
*Proof.* E·C₁ = (Tg'm'w₁ − 1)C₁ = Tg'(T^{s−2} + v₁) − C₁ = g'T^{s−1} + (Tg'v₁ − C₁) = g'T^{s−1} + w₁. Swap w ↔ C. ∎

**Lemma 1.2 (Liouville lemma at polynomial slice points; PROVED, q odd).** Let u ∈ F_q[T] with u(0) = 1, h := deg u ≥ 1,
and let a tuple of parameter s satisfy E ≡ −u (mod T^m) for some m ≤ s − 1. Then either
  (i) max(a − 1, b − 1 + h) ≥ m, or
  (ii) w₁ = −uC₁ exactly.
For u = 1 + cT (h = 1), (ii) is impossible, so **E ≡ −(1 + cT) (mod T^m) with m ≤ s − 1 forces max(a − 1, b) ≥ m.**
*Proof.* Mod T^m, Lemma 1.1 gives EC₁ ≡ w₁ (m ≤ s − 1), so w₁ + uC₁ ≡ 0 (mod T^m). This polynomial has degree
≤ max(a − 1, b − 1 + h); if it is nonzero its degree is ≥ m. For u = 1 + cT suppose w₁ = −(1 + cT)C₁. Leading
coefficients: 1 = −c, so c = −1 and w₁ = (T − 1)C₁. Then w₁ + C₁ = TC₁ = Tg'v₁, so C₁ = g'v₁; as gcd(C₁, v₁) = 1
(FF_STERILE_PUSH Lemma 1.1(iii)) v₁ is a constant, = 1 since C₁, g' are monic. Now m'w₁C₁ = (T − 1)m'g'² = T^{s−2} + 1;
at T = 1 this reads 0 = 2, false for q odd. ∎

**Corollary 1.3 (the thirds corner misses x*_c; PROVED).** If a tuple covers x*_c (k ≥ 2, s ≥ k + 2 so that
N(s) + 1 ≤ s − 1; (R247 repair) formerly "s ≥ 4", which is right only for k = 2), then max(a − 1, b) ≥ N(s) + 1 ≥ s/2 + 1. Equivalently its pattern lies in the *lopsided region*
  b ≥ N(s) + 1   (then a + z ≤ s − N(s) − 1 ≤ s/2 − 1)   or   a ≥ N(s) + 2   (then b + z ≤ s/2 − 2).
In particular no tuple with max(a, b) ≤ s/2 covers x*_c: the thirds corner (a, z, y, t)/s → (1/3, 1/3, 1/3, 0), where the
Lemma 1.6 route bounds of FF_STERILE_PUSH have exponent +0.167 above the critical 1/2 at q = 3, and every cyclotomic tuple
(below) is excluded.
*Proof.* Lemma 1.2 with m = N(s) + 1; N(s) + 1 ≤ s − 1 iff ⌈(s + k − 2)/2⌉ ≤ s − 2, true for s ≥ k + 2 (and for k = 2,
s ≥ 4; s = 3 has no tuple, FUNCTIONFIELD_ES3 Lemma 2.1 (R173 repair D1)). Then use a + b + z = s. ∎

*The cyclotomic tuples (R217/R218 M2 family).* Over F₃ with s = 3^h + 1 and v₁ = −1: lc(v) = −1 = lc(w + C)/lc(g') forces
lc(w + C) = 2, i.e. a = b; so 2(a − 1) ≤ s − 2, max(a − 1, b) = a ≤ s/2 < N(s) + 1. By Cor 1.3 **no cyclotomic tuple
covers x*_c**, for any h, any c. The same holds for every tuple with a = b (equal-degree w, C).

*Check (EVIDENCE, `scripts/zt_liouville.py` on the exact census `bsE_famcount 3 2 17 print`, 348 tuples, s ≤ 17).*
Every tuple re-verified ((B), Lemma 1.1); Lemma 1.2 tested at all 80 polynomial points u of degree 1..4 with u(0) = 1:
0 violations. Lopsided tuples (max(a − 1, b) ≥ N(s) + 1) are not rare at small s (e.g. 26/38 at s = 16); the exclusion is an
asymptotic statement about the thirds corner, not a small-s thinning. 24 tuples satisfy the exact alternative (ii), all at
u = 1 + cT − T² (and two degree-4 points); see Prop 1.4.

**Proposition 1.4 (exact tuples at polynomial points; PROVED, q odd).** Let u be a polynomial, u(0) = 1, h = deg u ≥ 1.
A tuple with w₁ = −uC₁ exists iff lc(u) = −1 and there are s ≥ 3 and a monic g₂ | (u − 1)/T (up to the unit) with
v₁ := −(u − 1)/(Tg₂) satisfying u | T^{s−2} + v₁ (then m'C₁² := −(T^{s−2} + v₁)/u, any split with C₁ monic, T ∤ C₁,
and g' = C₁g₂, w₁ = −uC₁; (R247 repair) for the converse also require T ∤ g₂, deg v₁ < s − 2 and v₁(0) ≠ 0). For such a tuple E = g₂T^{s−1} − u, so it covers x_u at every level N ≤ s − 2 it lives on, in particular at N(s) ((R247 repair) formerly "every level it lives on": at the top level N = s − 1 it fails, as T ∤ g₂).
*Proof.* As in Lemma 1.2: w₁ + C₁ = (1 − u)C₁ = Tg'v₁ and gcd(C₁, Tv₁) = 1 give C₁ | g'; put g' = C₁g₂, then
g₂v₁ = −(u − 1)/T and m'w₁C₁ = −um'C₁² = T^{s−2} + v₁. Leading coefficients: w₁ monic forces lc(u) = −1. Conversely the
displayed data satisfy (B₁), and E = Tg'm'w₁ − 1 = Tg₂(T^{s−2} + v₁) − 1 = g₂T^{s−1} − u. ∎
*Reading.* For h = 1 (u = 1 − T, the only lc = −1 case) T ≡ 1 (mod u), so T^{s−2} + v₁ ≡ 1 + 1 = 2 ≢ 0: **x*_c escapes the
exact tuples because T is trivial modulo u — the same "2 ≠ 0" as the char-2 Frobenius family of FF_STERILE_PUSH §4.**
For h ≥ 2 with lc(u) = −1 the condition T^{s−2} ≡ −v₁ (mod u) is a discrete-logarithm condition in (F_q[T]/u)^*; it holds
for s in an arithmetic progression as soon as −v₁ ∈ ⟨T⟩. E.g. u = 1 + cT − T² is covered this way (s = 5, 6, 13, 14 in the census).

## 2. A complete level-by-level search at polynomial points (Liouville makes it cheap)

**Proposition 2.1 (complete search; PROVED).** Let u be a polynomial with u(0) = 1, c := u'(0) ≠ 0, h = deg u, k ≥ 2,
N ≥ k + 1 ((R247 repair) formerly "N ≥ 3"; Lemma 1.2 needs N + 1 ≤ s − 1 with s ≥ 2N − k + 1), s ∈ {2N − k + 1, 2N − k + 2} (the parameters of level N). Every tuple of parameter s covering x_u is either exact
(Lemma 1.2(ii), classified by Prop 1.4) or is found by the following finite procedure (`scripts/zt_lop.c`).
Orientation A (X₁ = w₁, X₂ = C₁, Ê = E, τ = −u, α = (1 − u)/T) and orientation B (X₁ = C₁, X₂ = w₁, Ê = E',
τ = −u^{−1}, α = (1 − u^{−1})/T), with M := m'X₁:
* Case 1 (y ≤ N − 1). For every monic M, T ∤ M, deg M ≤ D (D_A = s − N − 3 + h, D_B = s − N − 3): g' is the
  truncation of αM^{−1} to degree < N; Ê = TMg' − 1; X₁ = (−g'T^{s−1}) mod Ê; m' = M/X₁.
* Case 2 (y ≥ N). For every monic M (T ∤ M) and v₁ (T ∤ v₁) with v₁ ≡ −T^{s−2} (mod M) and
  deg M + deg v₁ ≤ s − N − 3 + max(0, 2h − 4) (orientation A; s − N − 3 for B): X₂ = (T^{s−2} + v₁)/M, and X₁ ranges
  over the monic divisors of M with X₁ ≡ −X₂ (mod Tv₁); g' = (X₁ + X₂)/(Tv₁).
*Proof.* Non-exact covering tuples satisfy max(a − 1, b − 1 + h) ≥ N + 1 (Lemma 1.2; N + 1 ≤ s − 1 as N ≥ k + 1). If
b − 1 + h ≥ N + 1 use A: deg M = a + z − 1 = s − b − 1 ≤ D_A. Otherwise a ≥ N + 2, use B: deg M = b + z − 1 ≤ D_B.
In both orientations Ê = TMg' − 1 (E = L'w − 1 = Tg'm'w₁ − 1; same for E'), Ê·X₂ = g'T^{s−1} + X₁ (Lemma 1.1), and
covering is Ê ≡ τ (mod T^{N+1}) (E ≡ −u ⟺ E' ≡ −u^{−1}, as EE' = 1 + T^sL'g' and s ≥ N + 1), i.e. Mg' ≡ α (mod T^N).
Case 1: deg g' < N gives g' = trunc_N(αM^{−1}); deg X₁ < deg Ê gives X₁ as the stated remainder.
Case 2: y + t = max(a, b) (FF_STERILE_PUSH Lemma 1.1(ii)) gives, in A, deg M + deg v₁ = (s − b − 1) + (max(a, b) − y − 2)
= s − 3 − y + max(0, a − b), and symmetrically s − 3 − y + max(0, b − a) in B. In B, a ≥ N + 2 > b; in A with h = 1, b ≥ N + 1 > a;
in A with h ≥ 2, a − b ≤ s − 2b ≤ 2h − 4 (s ≤ 2N). With y ≥ N the bound follows. M | m'w₁C₁ = T^{s−2} + v₁ gives the
congruence for v₁ and X₂ = (T^{s−2} + v₁)/M; X₁ + X₂ = Tg'v₁ gives X₁ ≡ −X₂ (mod Tv₁). ∎
Every candidate is then re-verified from scratch ((B₁), monicity, T-coprimality, E ≡ −u mod T^{N+1}); only verified tuples are
reported. Cost per level ≈ 3^{N}·poly(N), against the ≈ 3^{2N} of the deg L' search of FUNCTIONFIELD_ES3 (which needs
deg L' ≤ 2N − 3 for completeness at level N).

**Cross-check (EVIDENCE).** `scripts/zt_lop_xcheck.py`: at all 80 polynomial points of degree 1..4 (u(0) = 1, u'(0) ≠ 0),
levels 3..8, the covering tuples of the exact census (`bsE_famcount 3 2 17`, an independent enumerator by (w, C)) are
exactly zt_lop's hits plus exact tuples (98 census tuples, 76 hits, 0 mismatching points).

**Result at x*_c (EVIDENCE: complete computer search, one code beyond level 8).** `zt_lop 3 2 3 NMAX 1,c`
(logs `data/zt_lop_xstar_c*.txt`, `data/zt_lop_xstar_k3_c*.txt`): **no Case B tuple covers x*_c at any level
3 ≤ N ≤ 20 (k = 2, c = 1 and c = 2)** and none at any level 4 ≤ N ≤ 18 for k = 3 (A = T³; levels ≤ 7 were already excluded
by FUNCTIONFIELD_ES3 §4). (R247: independently reproduced with a different enumeration, `scripts/review_r247_search.c`, for N ≤ 18 (k = 2) and N ≤ 16 (k = 3), both c; the c = 2 log is now committed.) Level 21 (k = 2) was not completed within the 8-hour budget (≈ 10¹¹ candidates). Levels ≤ 2 have no Case B tuple at x*_c (FUNCTIONFIELD_ES3 Lemma 2.1: N + γ ≥ 3 and the s = 4 tuples cover
u ≡ 1 + cT + 2T² only). With the Case A theorem (FUNCTIONFIELD_ES2 §0.2): no linear family of level ≤ 20 (k = 2) is valid at
x*_c. Previously: level ≤ 8 (FUNCTIONFIELD_ES3).

## 3. The second Liouville constraint, and a calibrated lottery model

**Lemma 3.1 (covering criterion without E; PROVED).** For a tuple of parameter s and N ≥ 1 with N + 1 ≤ s − 2, and a
polynomial u with u(0) = 1:  E ≡ −u (mod T^{N+1})  ⟺  **m'w₁² + u·v₁ ≡ 0 (mod T^{N+1})**  ⟺  u·m'C₁² + v₁ ≡ 0 (mod T^{N+1}).
*Proof.* E·C₁ ≡ w₁ (mod T^{s−1}) (Lemma 1.1) and C₁(0) ≠ 0 give E ≡ w₁/C₁ (mod T^{s−1}), so covering ⟺ w₁ + uC₁ ≡ 0
(mod T^{N+1}). From m'w₁C₁ = T^{s−2} + v₁, C₁ ≡ v₁/(m'w₁) (mod T^{s−2}); multiply by m'w₁ (a T-unit). The third form is the
same computation with w₁ ≡ v₁/(m'C₁) (mod T^{s−2}), multiplied by the T-unit m'C₁. ∎

**Corollary 3.2 (second Liouville constraint at x*_c; PROVED, q = 3; the exact case for general odd q is left open).**
A tuple covering x*_c (k = 2, N = N(s) ≥ 4) satisfies, besides max(a − 1, b) ≥ N + 1 (Cor 1.3),
  max(z + 2a − 2, t − 1) ≥ N + 1   and   max(z + 2b − 1, t − 2) ≥ N + 1.
In orientation A, case 1 of Prop 2.1 (b ≥ N + 1, y ≤ N − 1) this forces **deg w₁ = a − 1 ≥ N + 1 − deg M**: the small
side w₁ is a divisor of M = m'w₁ of degree at least N + 1 − deg M (so deg M ≥ (N + 1)/2).
*Proof.* Lemma 3.1 with u = 1 + cT: the polynomials m'w₁² + (1 + cT)v₁ and (1 + cT)m'C₁² + v₁ are ≡ 0 mod T^{N+1}, so each
is 0 or has degree ≥ N + 1. If m'w₁² = −(1 + cT)v₁: gcd(m'w₁, v₁) = 1 (a common prime divides T^{s−2}, and T ∤ v₁) forces
v₁ = λ ∈ F₃^*, w₁ = 1, m' = −λ(1 + cT), so λ = −c, m' = T + c, and T + c | T^{s−2} − c forces (−c)^{s−2} = c, i.e. c = 1 and
s even (q = 3: c² = 1). Then C₁ = (T^{s−2} − 1)/(T + 1), 1 + C₁ = T(T^{s−3} + 1)/(T + 1) = Tg'v₁ = −Tg' gives
lc(g') = −1: not monic. If (1 + cT)m'C₁² = −v₁: gcd(C₁, v₁) = 1 forces C₁ = 1, v₁ = −(1 + cT)m', and
m'w₁ = T^{s−2} + v₁ gives m'(w₁ + 1 + cT) = T^{s−2}, so m' = 1, w₁ = T^{s−2} − 1 − cT; then w₁ + C₁ = T(T^{s−3} − c) =
Tg'v₁ = −Tg'(1 + cT) gives lc(g') = −c, so c = −1 and (1 − T) | T^{s−3} + 1, false at T = 1. Degrees:
deg m'w₁² = z + 2a − 2, deg (1 + cT)v₁ = t − 1, deg (1 + cT)m'C₁² = z + 2b − 1, deg v₁ = t − 2.
Case 1 of orientation A: Mg' ≡ −c (mod T^N) with deg(Mg') = deg M + y; if deg M + y ≤ N − 1 then Mg' = −c, so
M = g' = 1, c = −1 and E = T − 1, which is not a tuple (FUNCTIONFIELD_ES3 Lemma 2.2, Z = 0). So y ≥ N − deg M and
t = b − y = s − deg M − 1 − y ≤ s − N − 1 ≤ N − 1 < N + 2; hence z + 2a − 2 = deg M + (a − 1) ≥ N + 1. ∎
*Remark.* The proof of Cor 3.2 uses c² = 1; for general odd q the exact case m'w₁² = −(1 + cT)v₁ needs (−c)^{s−2} = c and
lc(g') = 1 to be rechecked; not needed here.
*Check (EVIDENCE).* `scripts/zt_lemma31.py`: on all 348 census tuples (s ≤ 17) and all polynomial u of degree 1..4 with
u(0) = 1 (27 840 pairs), the T-adic agreement depths of E + u, m'w₁² + uv₁ and um'C₁² + v₁ (capped at s − 2) coincide.
Parity (FUNCTIONFIELD_ES2 §3, q = 3): all 348 census tuples have deg E, deg E', deg D even.

**The lottery at a polynomial point (Assessment, with a calibration that is EVIDENCE).** In case 1 of Prop 2.1 the whole
tuple is determined by M; it exists iff the remainder X₁ = (−g'T^{s−1}) mod Ê is a monic divisor of M (all other
conditions then hold automatically: C₁ = (g'T^{s−1} + X₁)/Ê is monic with C₁(0) = −X₁(0), and w₁ + C₁ = Tg'(MC₁ − T^{s−2})).
*Random-remainder model:* treat X₁ as uniform among the 3^{deg Ê} residues; by Cor 3.2 only divisors of degree in
[N + 1 − deg M, deg M] can occur (orientation A; analogous bound in B and at other polynomial points), parity forces
deg Ê even (FUNCTIONFIELD_ES2 §3), and the pattern parity law z ≡ t ≡ s (mod 2) of O226 (FF_ODD_ABSENCE Cor 1.7, branch
side-agent/ff-odd-absence, under review; checked here on all 348 census tuples) halves the admissible divisor degrees. So level N contributes Σ_M #{admissible divisors of M}·3^{−deg Ê}, summed over the M of Prop 2.1 (case 1),
plus (case 2) the number of region tuples satisfying both Liouville constraints times (1/2)·3^{−(N−1)}. Candidates with
Ê ≡ −u (mod T^{s−2}) ("structured": E = −u, Prop 1.4, and their relatives) are excluded from the model and from the
comparison. `zt_lop` prints this model per level ("refined").
*Calibration (`scripts/zt_ctl.sh` + `scripts/zt_calib.py`, log `data/zt_ctl_h4_N12.txt`; Case B only — Case A at polynomial points other than x*_c is not excluded by FUNCTIONFIELD_ES2 §0.2 and was not examined).* At all 52 polynomial points of
degree 2..4 with u(0) = 1, u'(0) ≠ 0, levels 3..12, complete search: unstructured hits vs. model
| levels | points with an unstructured hit | unstructured hits | model |
|---|---|---|---|
| 3..12 | 4 | 10 | 3.9 (degenerate split: at N ≤ 4, s − 2 ≤ N + 1, so "dep ≥ s − 2" is not a structure test) |
| 5..12 | 2 | 2 | 2.9 |
| 6..12 | 0 | 0 | 1.5 |
| 7..12 | 0 | 0 | 0.9 |
The model is consistent with the data within the (large) Poisson error of 2 events ((R247 repair) formerly "of the right
order and, at higher levels, slightly conservative"; P(0 | 1.5) = 0.22) (without the O226 parity law it predicted
5.2 / 2.8 / 1.6 for the last three rows). The structured hits
(E = −u and Prop 1.4 types, all at points with lc(u) = −1, plus their "dep = s − 2" companions) recur periodically in N
(e.g. u = 1 ± T − T² at N = 3, 6, 7, 10, 11, …) — the discrete-log mechanism of Prop 1.4.
**Lemma 3.3 ((R247 repair) no structured tuples at x*_c; PROVED, q = 3, s ≥ 5).** No tuple satisfies
E ≡ −(1 + cT) (mod T^{s−2}). So excluding "structured" candidates from the model is not a choice at x*_c (in particular at
x*_{−1}, which has lc u = −1). *Proof (R247).* T^{s−2} | w₁ + uC₁; non-exact forces max(a − 1, b) ≥ s − 2, so (i) a = 1, z = 0,
(ii) b = s − 2, (a, z) ∈ {(1, 1), (2, 0)}, or (iii) a = s − 1, b = 1, z = 0. In (i), (ii) v₁ (deg ≤ s − 3, resp. ≤ s − 4) is
the truncation of −m'w₁²u^{−1} below degree s − 2. (i): v₁u = −1 + (−c)^{s−2}T^{s−2} and Tv₁ | 1 + T^{s−2} + v₁; if
(−c)^{s−2} = −1 this gives g' = −c, monic only for c = −1, contradiction; if +1 then v₁ | 2, impossible. (ii): the
T^{s−3} coefficient vanishes (s ≥ 5) only for m' = T + c resp. w₁ = T + c, where m'w₁² = −uv₁ exactly: Cor 3.2's first exact
case resp. gcd(w₁, v₁) ≠ 1. (iii): w₁ = T^{s−2} − u, v₁ = −u: Cor 3.2's second exact case. ∎ Census check (R247,
`scripts/review_r247_structured_xstar.py`): max v_T(E + 1 + cT) − (s − 2) = 0 over all tuples s ≤ 16, only at s = 4.
*At x*_c* (both c give identical model values): refined model per level 7.6·10⁻⁴ (N = 5), 6.9·10⁻⁴, 4.4·10⁻⁴, 3.7·10⁻⁴,
3.1·10⁻⁴, 1.3·10⁻⁴, 2.0·10⁻⁴ (N = 11), 3.5·10⁻⁵, 2.3·10⁻⁵, 7.8·10⁻⁶, 9.9·10⁻⁶, 1.8·10⁻⁶, 6.8·10⁻⁷ (N = 17); total over
levels 3..17: 3.0·10⁻³ per c. The decay ratio tends to ≈ 1/3 (the model is poly(N)·3^{−N}: ≈ 3^{N−2} candidates M, each
needing a residue of size 3^{−(N + deg M)} to hit one of poly(N) admissible divisors). Extrapolated mass beyond the searched
levels (N > 20): ≈ 10⁻⁷.
*Contrast with generic points.* For a random slice point the expected number of covering tuples per level is
λ_N ≈ 0.22, 0.59, 0.37, 0.22, 0.096, 0.092 (N = 2..7, FUNCTIONFIELD_ES3 §2), and the union over levels is dominated by
balanced patterns (thirds corner) — which cannot reach a polynomial point at all (Cor 1.3). **So x*_c is not a typical
point of its cylinder: it is a "Liouville point", where the lottery is exponentially thinner (poly(N)·3^{−N} per level
instead of λ_N).** This corrects the Assessment of FUNCTIONFIELD_ES3 §3 ("x*_c is not visibly special"): its controls
(random lifts sharing six T-adic digits) are generic points, not low-height ones.

## 4. The cyclotomic families explicitly (goal 1)

`scripts/zt_cyclo.py` (python-flint): all tuples with s = 3^h + 1, v₁ = −1 (m'w₁C₁ = T^{3^h−1} − 1), exhaustive over the
3^{#factors} assignments for h = 2, 3 and 2·10⁵ random assignments for h = 4; each tuple re-verified ((B)); for c = 1, 2 the
depth dep_c = v_T(E + 1 + cT) is recorded (covering x*_c needs dep_c ≥ N(s) + 1):
| h | s | N(s) + 1 | tuples | max dep_c | dep histogram (c = 1; c = 2 identical up to ±1 counts) |
|---|---|---|---|---|---|
| 2 | 10 | 6 | 12 | 4 | 6, 4, 1, 1 at dep 1..4 |
| 3 | 28 | 15 | 1116 | 13 | 558, 374, 123, 39, 16, 2, 3 at dep 1..7, one tuple at dep 13 |
| 4 | 82 | 42 | 2013 (sample) | 10 | geometric, ratio ≈ 1/3 |
The depths are geometric with ratio ≈ 1/3 (the "random digits" behaviour of a generic family), always ≤ a = max(a − 1, b)
as Lemma 1.2 requires (asserted in the script), far below N(s) + 1 ≈ s/2. The single h = 3 outlier (dep 13 ≤ a ≤ 14) shows
that the Liouville bound, not the randomness, is what separates the thirds corner from x*_c at large depth.

## 5. The residual problem at x*_c in closed form (Bezout form)

**Proposition 5.1 (case 1 at x*_c is a Bezout/Euclid object; PROVED, q = 3).** Let u = 1 + cT, k = 2, N ≥ 4, orientation A,
case 1 (y ≤ N − 1). For a monic M (T ∤ M, d := deg M ≤ s − N − 2) let Z be the least residue of T^{−N} modulo M. Then
the forced data of Prop 2.1 are
  g' = c(T^N Z − 1)/M  (monic iff lc Z = c),   E = cT^{N+1}Z − (1 + cT),
i.e. (Z, cg') is the Bezout pair of (T^N, M): T^N Z − cMg' = 1. A covering tuple exists for this M iff lc Z = c and some factorisation
M = m'w₁ with deg w₁ ≥ N + 1 − d (Cor 3.2) satisfies E | T^{s−2} + m'w₁² ((R247 repair) "lc Z = c" added; converse: put
v₁ := (T^{s−2} + m'w₁²)/E, C₁ := Tg'v₁ − w₁), and then (one direction only; the converse needs gcd(Z, 1 + cT) = 1) for s = 2N (resp. 2N − 1)
  E | u² + m'·(T²Zw₁)²   (resp. E | u² + T·m'·(T²Zw₁)²).
*Proof.* cMg' = T^NZ − 1 gives Mg' ≡ −c (mod T^N) (c² = 1) with deg g' = N + deg Z − d < N, so g' = trunc_N(−cM^{−1}) (unique
such polynomial); lc g' = c·lc Z. E = TMg' − 1 = cT(T^NZ − 1) − 1. The divisibility is R4 (FF_STERILE_PUSH Lemma 1.6:
Ev₁ = T^{s−2} + m'w₁²). Modulo E, T^{N+1}Z ≡ cu, so T^{2N+2}Z² ≡ u²; multiply T^{s−2} + m'w₁² by T^{2N+4−s}Z². ∎
So the whole of Conjecture 0.2 beyond the searched levels is the statement that, for the ≈ 3^{N−2} polynomials M per level,
the Euclid-determined E_M = cT^{N+1}(T^{−N} mod M) − (1 + cT) never divides T^{s−2} + m'w₁² for a split of M with a
large w₁ (plus the much smaller case 2 and orientation B, which have the same shape). This is a deterministic but
structureless (lottery-type) condition: the remainder −T^{s−2}M^{−1} mod E_M must be a small divisor of M. The calibration
of §3 says such coincidences occur at rate poly(N)·3^{−N} per level.

## 6. Interpretation (goal 3; Assessment unless labelled)

**Dictionary: covering = rational T-adic approximation (PROVED content: Lemmas 1.1, 1.2, 3.1).** A tuple covers x_u at
level N iff the rational function −w₁/C₁ approximates u T-adically to order N + 1 (N + 1 ≤ s − 1), where the "height"
max(deg w₁, deg C₁) and the multiplicative side condition m'w₁C₁ = T^{s−2} + v₁ come from the tuple. Generic u are
approximated by balanced tuples (height ≈ s/3, order ≈ s/2: exponent 3/2, comfortably below Dirichlet's 2), so for them
coverage is a counting question dominated by the thirds corner — where the union bound fails at q = 3. A polynomial u of
degree h has Liouville exponent 1: a rational of height H ≠ −u approximates it to order ≤ H + h. Hence only lopsided
tuples (one of w, C of degree ≥ s/2) or exact identities can reach it. The obstructed set O(3, T²) ∩ slice is the complement
of a union of T-adic balls around the "tuple rationals" −w₁/C₁; low-height points sit far from all balls of large radius.

**Why q = 3 is covered at A = T but (conjecturally) not at A = T².** For k = 1 a cylinder can have depth 1, and the depth-1
families E = −1, −2 are exactly the "exact" families E = −u(0) of Prop 1.4 at precision 1: the Liouville constraint is
vacuous at depth 1, and F₃^* = {1, 2} is exhausted by the two constants ((J)4; for q = 3^r, r ≥ 2, the classes u(0) ∉ F₃
are not reached, (J)56). For k ≥ 2 every cylinder has depth N + 1 ≥ 3 > deg(1 + cT) + 1, so at x*_c the Liouville
constraint bites at every level, and the only escape — an exact family — is killed by one bit:
* c = +1: lc(u) = +1, and both exact types (E = −u, w₁ = −uC₁) need lc(u) = −1 (Prop 1.4, Lemma 1.2(ii)).
* c = −1: the would-be exact tuple w₁ = −uC₁ = (T − 1)C₁ needs (T − 1)m'g'² = T^{s−2} + 1 (Lemma 1.2), and T ≡ 1
  (mod T − 1) turns this into 0 = 2 ((R247 repair) garbled formula replaced): **the same "2 ≠ 0" that makes odd characteristic sterile and characteristic 2 covered
  by the Frobenius family (1 + Tg')² = 1 + T²g'² (FF_STERILE_PUSH §4)**.

**The leading coefficient as the archimedean sign (Assessment; a sharp analogy with (J)55).** In F_q[T] the place ∞ is the
archimedean place and lc is its sign. Exact families at a polynomial point need lc(u) = −1 (Prop 1.4); in the calibration data of
§3 (52 points of degree 2..4, levels 5..12) all 42 structured hits found by the lopsided search (dep ≥ s − 2; (R247 repair) the lop search omits non-lopsided exact tuples, so the true structured count is ≥ 58 — all at lc(u) = −1 anyway by Prop 1.4; e.g. u = 1 ± T − T² at N = 6, 7, 10, 11, …)
are at points with lc(u) = −1, while the lc(u) = +1 points carry only 2 hits (both unstructured, N = 5) (EVIDENCE). Over ℤ, (J)55 found the same split on p = m² + k: for k > 0 every polynomial family meets a fixed
character (sterile), for k < 0 escaping families exist. In both worlds a *low-height* point is sterile for polynomial/
exact families exactly on one side of the archimedean sign, and on the other side exact identities (here E = −u, there
the k < 0 families) can cover it ((R247 repair) "can": lc(u) = −1 is necessary, not sufficient — Prop 1.4's
discrete-log condition must also hold). x*_c with c = −1 sits on the "wrong" side and is saved only by 2 ≠ 0.

**ℤ face of the Liouville lemma (Assessment).** On the r-generic line of (J)26/(J)54 (x_q = 1 off r, x_r = u) take u a
small integer. A covering datum needs an ET divisor f ≡ −u (mod r^{N+1}) (shape of the Type II congruences); a positive
f < r^{N+1} − |u| is impossible unless f = −u, so the data must be "lopsided" (f ≥ r^{N+1} − |u|) or exact (f = |u|,
possible only for u < 0 — the sign again). The sterile Mordell points proved for r ≥ 2³² are measure-theoretic; small-integer
points of the line would be the ℤ-analogues of x*_c. Not pursued.

## 7. Route bounds restricted to the patterns that can reach x*_c (goal 2; EVIDENCE/Assessment, grid)

`scripts/zt_rate_lop.py` reruns the continuum optimiser of FF_STERILE_PUSH (`fs_rate.py`, Lemma 1.6 routes, grid G = 60)
on the patterns allowed at x*_c by Cor 1.3 and Cor 3.2 (normalised a ≤ b: b ≥ 1/2 and max(z + 2a, t) ≥ 1/2):
| q | all patterns: max min_route − 1/2 | restricted | restricted maximiser (a, z, y, t)/s |
|---|---|---|---|
| 3 | +0.167 (thirds corner) | **0.000** | (0, 0, 1/2, 1/2) |
| 9 | +0.096 | 0.000 | (0, 0.2, 0.3, 0.5) |
| 27 | 0.000 | −0.007 | (0.38, 0.12, 0.12, 0.38) |
So the whole super-critical excess of the q = 3 union bound lives in patterns that provably cannot reach x*_c. On the
admissible patterns the route bounds are exactly critical. (R247 repair: the former claim "the maximiser is a degenerate
corner where the true count is only polynomial" was false.) The zero set is large: at G = 60, 314 of the 961 grid points of
the boundary face b = y + t = 1/2 of the Liouville region (a 2-dimensional region, e.g. (1/6, 1/3, 1/3, 1/6), (0.1, 0.4,
0.4, 0.1)) and 12 points on segments of t = 1/2 (e.g. (1/6, 0, 1/3, 1/2)); the printed maximiser is just the first grid
point found. These patterns have w, m', g' of linear degree; no sub-critical count is known for them (R247,
`scripts/review_r247_rate_face.py`; the q = 27 value −0.007 is a grid artefact, local refinement gives −0.0024). Union bounds therefore
cannot settle x*_c either way (a single point has measure 0), but they no longer contradict it.
