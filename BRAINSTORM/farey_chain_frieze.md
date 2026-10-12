# BRAINSTORM — ES as 3-step Farey paths / frieze chains (O144, by-product of angles a, c)

Labels as in DISCOVERIES.md. ET Type I: `(x,y,z) = (abdp, acd, bcd)`, `4abd = pe + 1`, `a + b = ce`,
`bf = ap + c` with `f = 4acd − p` (POINTWISE_SPECTRAL Lemma 2.1). ET Type II: `(x,y,z) = (abd, acdp, bcdp)`,
`4abcd = a + b + cp`.

## 1. Idea (exact statement)

Take a monotone path `r₀ < r₁ < r₂ < r₃` in the Farey graph, with denominators q₀, …, q₃. Then
`r_{i+1} − r_i = 1/(q_i q_{i+1})`, and the denominators obey the Hirzebruch–Jung (Conway–Coxeter frieze)
recurrence `q_{i−1} + q_{i+1} = k_i q_i` with turning numbers k_i ≥ 1. Pure algebra (no coprimality needed):

**Lemma C.0 (PROVED).** If `q₁ | q₀ + q₂ = k₁q₁` and `q₂ | q₁ + q₃ = k₂q₂`, then
`1/(q₀q₁) + 1/(q₁q₂) + 1/(q₂q₃) = (k₁k₂ − 1)/(q₀q₃)`.
*Proof.* The first two terms sum to `k₁/(q₀q₂)`. Then `k₁q₃ + q₀ = k₁k₂q₂ − (k₁q₁ − q₀) = (k₁k₂ − 1)q₂`. ∎

**Prop C.1 (PROVED, elementary).** Let p ≥ 5 be prime. Then 4/p = 1/x + 1/y + 1/z has a positive solution iff
there are d ≥ 1 and a chain (q₀, q₁, q₂, q₃) of positive integers as in Lemma C.0 with span
`(k₁k₂ − 1)/(q₀q₃) = 4d/p`. In that case `(x, y, z) = (d q₀q₁, d q₁q₂, d q₂q₃)`. Explicitly:
* Type I: `(q₀, q₁, q₂, q₃) = (a, c, b, ap)`, with turning numbers `(k₁, k₂) = (e, f)`. The span is
  `(ef − 1)/(a²p) = 4a²d/(a²p)`. This is the SL₂ matrix `[[e, 2a],[2ad, f]]` of the brief.
* Type II: `(q₀, q₁, q₂, q₃) = (cp, a, b, cp)`, with turning numbers `((cp+b)/a, (cp+a)/b)` (integers by
  `4abcd = a + b + cp`). The span is `4d/p`.
* Converse: scale the chain by d (Lemma C.0). Every positive solution for prime p is of Type I or Type II (ET),
  so the Type I/II maps cover everything.
*Proof.*
* Type I: `x = d·a·bp`, `y = d·a·c`, `z = d·c·b` in the order (y, z, x). The divisibilities are `c | a + b = ce`
  and `b | c + ap = bf`.
* Type II: `y = d·cp·a`, `x = d·a·b`, `z = d·b·cp`. Here `a | b + cp` and `b | a + cp` hold because
  `cp + a + b = 4abcd`. ∎

**Corollary (sharp reformulation).** ES(p) ⟺ some monotone 3-step path in the Farey graph (a positive frieze
of width 2) spans an interval whose length is a positive integer multiple of 4/p. For a genuine Farey path, the
span condition is `4q₀q₃ | p(k₁k₂ − 1)`, and it forces p | q₀q₃ (a span ≥ 4 is impossible).

**Prop C.2 (PROVED "⇐"; EVIDENCE "⇒").** For a Type I/II solution, let g be the gcd of the three
coordinates after removing p (g = d when a, b, c are pairwise coprime). If ET's d is a perfect square s², the
solution is an *unscaled* chain for 4/p: multiply the chain of Prop C.1 by s. Conversely, data for all 11 800
solutions with p < 1500 show: chain-realisable (some ordering and factorisation) ⟺ g is a perfect square
(`scripts/bs_farey_frieze.py`, `scripts/bs_farey_frieze_classify.py`).

## 2. Literature anchor

* Farey graph, Ford circles and Hirzebruch–Jung continued fractions: standard (Hatcher, *Topology of numbers*).
* Conway–Coxeter friezes (1973): from memory, unverified page numbers.
* Bounded generation of SL₂(ℤ[1/p]) by elementary matrices (Vsemirnov 2014; Morgan–Rapinchuk–Sury 2018):
  from memory, unverified. It concerns elementary matrices with ℤ[1/p] entries. "Farey distance ≤ 3 over ℤ"
  is a different question, so I found no transferable statement.

## 3. Barrier screen

* **B2.** Fix (q₀, q₁), i.e. (a, c) for Type I. The remaining condition is a divisor event for one integer:
  q₂ ≡ −q₀ (mod q₁), q₃ ≡ −q₁ (mod q₂), plus the span divisibility. This is exactly the (a,c)-slice
  `f | p² + 4c²d`-type data. The path picture is the ET parametrisation in Farey clothing.
* **B3.** Unscaled chains (d a square) carry mass Σ_s 1/s² · L² ≍ L² instead of L³, because the d-sum loses its
  logarithm. This is consistent with the falling chain share (0.35 at p ≤ 400, 0.27 at p ≤ 6000). The full ES
  needs the scaled version, which is the L³ lottery again.
* **B5/T1.** At n = m² (odd), the scaled-chain statement is false. The failing step is the span divisibility, which
  is ET's genus condition. The Farey-path geometry itself is n-agnostic.
* **B6/T7.** No averaging input is used; nothing leaks.
* "Farey distance ≤ 3": the geodesic from r₀ to r₀ + 4d/p must cross at most two Farey edges. Bounding Farey
  distance between two *given* rationals is a CF-length statement. Here both endpoints are free, and the only
  constraint is arithmetic (the span). So geometry gives no leverage: any dynamical/Ford-circle count over
  (r₀, d) is the Type I/II count.

## 4. Experiment (`scripts/bs_farey_frieze.py`)

* p ≤ 400: 2256 solutions (x ≤ y ≤ z), 793 unscaled chains (0.352). Primes with no unscaled chain: 13, 37, 97,
  181, 193.
* p ≤ 6000: 63 085 solutions, 16 840 chains (0.267). There are 17 chain-free primes, all ≡ 1 (mod 12):
  13, 37, 97, 181, 193, 541, 673, 757, 1033, 1093, 1297, 1621, 1777, 2293, 2473, 3361, 3877.
* Classification for p < 1500, by the gcd g above:
  * Type I: chains = exactly the g-square solutions (2223/2223; 0 of 6274 non-squares).
  * Type II: likewise (1403/1403; 0 of 1900).

## 5. Viability Assessment

**PARTIAL (sharp reformulation), COLLAPSES to B2 as a route.**
* Prop C.1 (PROVED): ES(p) ⟺ a 3-step monotone Farey path / width-2 frieze spans a positive multiple of 4/p.
  It packages Type I and Type II uniformly, with the turning numbers (e, f), resp. ((cp+b)/a, (cp+a)/b).
* The unscaled version ("span exactly 4/p") is the square-d sub-family. Its mass is L², and it misses 17 primes
  ≤ 6000. CONJECTURE (weak, from data growth): it misses infinitely many primes.
* Novelty: unverified. The Type I identity is visible in ET's matrices. I found no literature hit for the frieze
  form, but did not search exhaustively.
