# FF_THIRDS_CORNER — Conjecture 0.2 at q = 3: the thirds corner versus the sterile point x*_c (O227, wave Z-d1)

Status: in progress (O227). ES is not solved here, nor any infinite case of ES or ES_q. Labels as in DISCOVERIES.md.
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

**Corollary 1.3 (the thirds corner misses x*_c; PROVED).** If a tuple covers x*_c (k ≥ 2, s ≥ 4 so that
N(s) + 1 ≤ s − 1), then max(a − 1, b) ≥ N(s) + 1 ≥ s/2 + 1. Equivalently its pattern lies in the *lopsided region*
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
and g' = C₁g₂, w₁ = −uC₁). For such a tuple E = g₂T^{s−1} − u, so it covers x_u at every level it lives on.
*Proof.* As in Lemma 1.2: w₁ + C₁ = (1 − u)C₁ = Tg'v₁ and gcd(C₁, Tv₁) = 1 give C₁ | g'; put g' = C₁g₂, then
g₂v₁ = −(u − 1)/T and m'w₁C₁ = −um'C₁² = T^{s−2} + v₁. Leading coefficients: w₁ monic forces lc(u) = −1. Conversely the
displayed data satisfy (B₁), and E = Tg'm'w₁ − 1 = Tg₂(T^{s−2} + v₁) − 1 = g₂T^{s−1} − u. ∎
*Reading.* For h = 1 (u = 1 − T, the only lc = −1 case) T ≡ 1 (mod u), so T^{s−2} + v₁ ≡ 1 + 1 = 2 ≢ 0: **x*_c escapes the
exact tuples because T is trivial modulo u — the same "2 ≠ 0" as the char-2 Frobenius family of FF_STERILE_PUSH §4.**
For h ≥ 2 with lc(u) = −1 the condition T^{s−2} ≡ −v₁ (mod u) is a discrete-logarithm condition in (F_q[T]/u)^*; it holds
for s in an arithmetic progression as soon as −v₁ ∈ ⟨T⟩. E.g. u = 1 + cT − T² is covered this way (s = 5, 6, 13, 14 in the census).

## 2. A complete level-by-level search at polynomial points (Liouville makes it cheap)

**Proposition 2.1 (complete search; PROVED).** Let u be a polynomial with u(0) = 1, c := u'(0) ≠ 0, h = deg u, k ≥ 2,
N ≥ 3, s ∈ {2N − k + 1, 2N − k + 2} (the parameters of level N). Every tuple of parameter s covering x_u is either exact
(Lemma 1.2(ii), classified by Prop 1.4) or is found by the following finite procedure (`scripts/zt_lop.c`).
Orientation A (X₁ = w₁, X₂ = C₁, Ê = E, τ = −u, α = (1 − u)/T) and orientation B (X₁ = C₁, X₂ = w₁, Ê = E',
τ = −u^{−1}, α = (1 − u^{−1})/T), with M := m'X₁:
* Case 1 (y ≤ N − 1). For every monic M, T ∤ M, deg M ≤ D (D_A = s − N − 3 + h, D_B = s − N − 3): g' is the
  truncation of αM^{−1} to degree < N; Ê = TMg' − 1; X₁ = (−g'T^{s−1}) mod Ê; m' = M/X₁.
* Case 2 (y ≥ N). For every monic M (T ∤ M) and v₁ (T ∤ v₁) with v₁ ≡ −T^{s−2} (mod M) and
  deg M + deg v₁ ≤ s − N − 3 + max(0, 2h − 4) (orientation A; s − N − 3 for B): X₂ = (T^{s−2} + v₁)/M, and X₁ ranges
  over the monic divisors of M with X₁ ≡ −X₂ (mod Tv₁); g' = (X₁ + X₂)/(Tv₁).
*Proof.* Non-exact covering tuples satisfy max(a − 1, b − 1 + h) ≥ N + 1 (Lemma 1.2; N + 1 ≤ s − 1 as N ≥ 3). If
b − 1 + h ≥ N + 1 use A: deg M = a + z − 1 = s − b − 1 ≤ D_A. Otherwise a ≥ N + 2, use B: deg M = b + z − 1 ≤ D_B.
In both orientations Ê = TMg' − 1 (E = L'w − 1 = Tg'm'w₁ − 1; same for E'), Ê·X₂ = g'T^{s−1} + X₁ (Lemma 1.1), and
covering is Ê ≡ τ (mod T^{N+1}) (E ≡ −u ⟺ E' ≡ −u^{−1}, as EE' = 1 + T^sL'g' and s ≥ N + 1), i.e. Mg' ≡ α (mod T^N).
Case 1: deg g' < N gives g' = trunc_N(αM^{−1}); deg X₁ < deg Ê gives X₁ as the stated remainder.
Case 2: y + t = max(a, b) (FF_STERILE_PUSH Lemma 1.1(ii)) gives deg M + deg v₁ = (s − max(a,b) − 1) + (max(a,b) − y − 2) +
(max(a, b) − b or − a) = s − 3 − y + max(0, a − b) (A; symmetric for B). In B, a ≥ N + 2 > b; in A with h = 1, b ≥ N + 1 > a;
in A with h ≥ 2, a − b ≤ s − 2b ≤ 2h − 4 (s ≤ 2N). With y ≥ N the bound follows. M | m'w₁C₁ = T^{s−2} + v₁ gives the
congruence for v₁ and X₂ = (T^{s−2} + v₁)/M; X₁ + X₂ = Tg'v₁ gives X₁ ≡ −X₂ (mod Tv₁). ∎
Every candidate is then re-verified from scratch ((B₁), monicity, T-coprimality, E ≡ −u mod T^{N+1}); only verified tuples are
reported. Cost per level ≈ 3^{N}·poly(N), against the ≈ 3^{2N} of the deg L' search of FUNCTIONFIELD_ES3 (which needs
deg L' ≤ 2N − 3 for completeness at level N).

**Cross-check (EVIDENCE).** `scripts/zt_lop_xcheck.py`: at all 80 polynomial points of degree 1..4 (u(0) = 1, u'(0) ≠ 0),
levels 3..8, the covering tuples of the exact census (`bsE_famcount 3 2 17`, an independent enumerator by (w, C)) are
exactly zt_lop's hits plus exact tuples (98 census tuples, 76 hits, 0 mismatching points).

**Result at x*_c (EVIDENCE: complete computer search, one code beyond level 8).** `zt_lop 3 2 3 NMAX 1,c`
(logs `data/zt_lop_xstar_c*.txt`): **no Case B tuple covers x*_c at any level 3 ≤ N ≤ NMAX** — see the table in §3 for the
reached NMAX. Levels ≤ 2 have no Case B tuple at x*_c (FUNCTIONFIELD_ES3 Lemma 2.1: N + γ ≥ 3 and the s = 4 tuples cover
u ≡ 1 + cT + 2T² only). With the Case A theorem (FUNCTIONFIELD_ES2 §0.2): no linear family of level ≤ NMAX is valid at
x*_c. Previously: level ≤ 8 (FUNCTIONFIELD_ES3).
