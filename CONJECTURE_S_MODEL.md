# CONJECTURE_S_MODEL — bracketing certificate survival in the prime-Haar model

**Status: IN PROGRESS (z49 round 3, slug `sexp`).** ES is open; nothing here bears on ES existence directly.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment.

## 0. Summary (to be updated)

* §2 (target): **PROVED modulo the fundamental lemma of sieve theory**, δ(H) ≤ exp(−c L²). This is the sharp order
  and improves the L²/(log L)² of the rough-pair route. The method conditions on all small-prime coordinates and
  keeps endpoints with bounded smooth part.
* §3 (target): the reverse direction δ(H) ≥ exp(−L^{2+o(1)}) via non-adaptive class-of-one conditioning plus a
  β-weighted local lemma, reduced to a pointwise load hypothesis.

## 1. Model, events, and the colour

Logs are natural. H → ∞, L = log H. The **prime-Haar model**: n ranges over the profinite units with the product of
Haar measures, conditioned on n ≡ 1 (mod 24). Coordinates X_ℓ = n mod ℓ^∞ are independent: uniform units for ℓ ≥ 5,
uniform on 1 + 8ℤ₂ for ℓ = 2, and uniform on 1 + 3ℤ₃ for ℓ = 3.

For coprime 1 ≤ a < v ≤ H, the edge event is E_{a,v} = {n ≡ −a−v (mod av)}. The edge is a **certificate** when
(av/n) = −1 (Theorem A). δ(H) = P(no certificate edge with v ≤ H), as in FOREST_H4 Prop 5.1 (prime-Haar,
n ≡ 1 (24)).

**Lemma 1.1 (PROVED; colour is p-independent for odd pairs).** Let a, v be odd and coprime, and let n ≡ 1 (mod 8)
lie in E_{a,v}. Then (av/n) = −1 iff a and v are not both ≡ 1 (mod 4).

*Proof.* (2/n) = 1, and reciprocity for n ≡ 1 (4) gives (av/n) = (n/av) = ((−a−v)/a)((−a−v)/v) = ((−v)/a)((−a)/v).
That equals (−1/a)(−1/v)(v/a)(a/v) = (−1)^{(a−1)/2+(v−1)/2+(a−1)(v−1)/4}. The value is +1 for (1,1) mod 4 and −1 in
the other three cases. ∎

So on n ≡ 1 (24) the certificate events restricted to odd pairs are **a fixed subfamily** of the edge events: no
extra condition on n is imposed, and the 2-adic coordinate drops out entirely.

## 2. Upper bound on survival (Janson) — see below

## 3. Lower bound on survival — see below

## 4. Reality check against the simulation — see below
