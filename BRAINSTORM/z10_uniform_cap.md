# z10_uniform_cap — the cap knob uniformly in e, and its saturation (O234; deep file CAP_INTERPOLATION.md §§1–3)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
O229's c_e for ES^{(y,e)} (free mute set) came from BV with divisor weights κ^{ω(q)}, which is not uniform in κ = e+2.
Barrier hypothesis: "BV at fixed A". Violation: the moduli 4c₀d₀ only need size X^{1/(10κ)}, so log x/log q ≥ 4κ and
Gallagher's PNT gives relative error e^{−cκ} per modulus — no weights at all. Then let e = e(N) grow.

## Result
* Thm 2.1 (PROVED rel. Gallagher's PNT, BV, large sieve): #{p ≤ N : ES^{(y,e)}(p) fails} ≤
  N exp(−c(log N)^{(e+2)/(e+3)}/((e+2)log(e+3))) uniformly for e ≤ log log N — c_e ≍ 1/(e log e), not ((e+1)(e+2))^{−e}.
* Saturation at e ≍ log log N: ≤ N exp(−c log N/(log₂N log₃N)) for every e ≥ log log N.
* Thm 3.1 (ceiling, PROVED, Rankin): the prime-modulus large sieve with cube classes TRUNCATED to V < ℓ/4 cannot do
  better at any cap. (R237 repair D1: the truncation is not forced — Prop 5.1 has no size condition — and the full
  family gives a power saving at e = ∞ and e ≥ (log N)^{1+ε}, CAP_INTERPOLATION Remark 3.2; log log N ≤ e ≤ (log N)^{1+ε}
  OPEN.)

## Barrier screen
B6 exactly (averages); Thm 3.1 is a theorem about the method's bound, not the true exceptional set (heuristically
exp(−exp(c√(log N/log₂N))) density). T1: all classes are non-residues; squares never hit.

## Assessment
Clean, modest: closes O229's spark 3 (uniformity) with a matching ceiling for the truncated family (R237 D1). Not a route to ES.
