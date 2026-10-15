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
