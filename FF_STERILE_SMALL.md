# FF_STERILE_SMALL — the small-q sterility cases: q = 27 (r = 3), q = 9, and A = T (k = 1) (O220, wave Y-f)

Status: work in progress (O220). **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in DISCOVERIES.md.
Builds on FF_STERILE_PUSH.md ((J)51; notation (B), Lemmas 1.1–1.6, 2.1, 2.2, Thm 3.1), DEPTH_ASPECT.md §2, FUNCTIONFIELD_ES*.md.
Scripts `scripts/fz_*`.

Setting and notation exactly as FF_STERILE_PUSH (q odd, A = T^k, k ≥ 2, Case B tuple (m', g', w, C) of parameter s,
w = Tw₁, C = TC₁, v = T²v₁, degrees a = deg w, b = deg C, z = deg m', y = deg g', t = deg v, a + b + z = s, y + t = max(a, b)).
Key identity (FF_STERILE_PUSH Lemma 1.1(iii)):
  m'w₁C₁ = T^{s−2} + v₁,  deg v₁ = t − 2,  w₁ + C₁ = Tg'v₁.                                         (B₁)

## 0. Iteration log

* (I1) The binding point of the r = 3 barrier, (a, z, y, t)/s = (1/3, 1/3, 1/6, 1/6), is where every factor of
  T^{s−2} + v₁ has degree ≈ s/3 while v₁ has degree ≈ s/6. All Lemma 1.6 routes that pay for v₁ (factor q^{t−2}) and then
  for a factor of degree > t − 2 pay twice: **a monic factor of degree > deg v₁ determines v₁ by Euclidean division**
  (Lemma 1.1 below). This is the "short interval ↔ arithmetic progression" duality of F_q[T] in its simplest form.

## 1. Division routes (new; PROVED, elementary)

**Lemma 1.1 (Euclidean division determines v₁).** Let D be a monic divisor of m'w₁C₁ with deg D > t − 2 (e.g. D = m' if
z ≥ t − 1, D = w₁ if a ≥ t, D = C₁ always, since b − 1 ≥ t − 1). Then v₁ = −(T^{s−2} mod D) and
(T^{s−2} + v₁)/D = T^{s−2} div D (quotient of Euclidean division). In particular D determines v₁ and the cofactor
m'w₁C₁/D.
*Proof.* T^{s−2} = D·(m'w₁C₁/D) + (−v₁) with deg(−v₁) = t − 2 < deg D; Euclidean division by the monic D is unique. ∎

**Lemma 1.2 (division routes; PROVED from Lemma 1.1 and FF_STERILE_PUSH Lemmas 1.3–1.6).** With N*, cls as in
FF_STERILE_PUSH Lemma 1.6 and ω*(e) := max{ω(f) : f ∈ F_q[T], deg f ≤ e, T ∤ f}, the number of tuples with pattern
(s; a, z, y, t) is at most each of
| route | condition | data fixed | then | bound |
|---|---|---|---|---|
| D1 | z ≥ t − 1 | m' | v₁, G := w₁C₁ by Lemma 1.1; w₁ ∣ G of degree a − 1 | N*(z)·C(a+b−2, a−1) |
| D1c | z ≥ t − 1 | m' | as D1, w₁ in one of ≤ 2^{1+ω*(t−2)} square-root classes mod Tv₁ | N*(z)·2^{1+ω*(t−2)}·cls(a+b−2, a−1, t−1) |
| D2 | a ≥ t | w₁ | v₁, m'C₁; C₁ ∣ m'C₁, C₁ ≡ −w₁ (Tv₁) | N*(a−1)·cls(z+b−1, b−1, t−1) |
| D3 | — | C₁ | v₁, m'w₁; w₁ ∣ m'w₁, w₁ ≡ −C₁ (Tv₁) | N*(b−1)·cls(z+a−1, a−1, t−1) |
(cofactor versions of cls allowed in all three: G, m'C₁, m'w₁ are prime to Tv₁ by FF_STERILE_PUSH Lemma 1.1(iii).)
*Proof.* Lemma 1.1 gives v₁ and the cofactor; the rest is FF_STERILE_PUSH Lemma 1.6, rows R9a, R10a, R5a, R5b, with the
v₁-sum replaced by the single determined v₁ (so in D1c the average Σ2^ω is replaced by the maximum 2^{ω*}; Tv₁ has
ω(Tv₁) = 1 + ω(v₁) ≤ 1 + ω*(t − 2)). The tuple is then determined (FF_STERILE_PUSH Lemma 1.2: (m', w, v) or (g', v, w)
with g' = (w₁ + C₁)/(Tv₁)). ∎
These are the rows R9a, R10a, R5a, R5b without the factor N*(t − 2) — a gain of q^{t−2} whenever the condition holds.
At the r = 3 critical point (1/3, 1/3, 1/6, 1/6): D1 has exponent z + (a + b)·log 2/log q = 1/3 + (2/3)(log 2/log 27) = 0.4736 < 1/2.
