# bsM_borel_cantelli_patterns — sterile points and non-square patterns (O188)

**Dictionary (PROVED, STERILE_STEER Prop 3.1).** S := Ẑ minus the union of all ET classes is closed. ES(p) ⟺ p ∉ S,
and SQ ⟺ S ∩ ℕ_odd = odd squares.
**Dichotomy.** Let G_T be the set of points that are 1 off T and non-squares on T, with product measure ν_T.
* Divergent: Σ_{q∈T, q≡3(4)} 1/q = ∞ ⇒ ν_T-a.e. point is covered, already by the classes II2(1,1,q) = {n ≡ −4 (q)}
  (Prop 3.2, PROVED, second Borel–Cantelli). Every non-square integer's pattern is divergent.
* Convergent: T = {r}, r ≥ r₀ ⇒ positive ν-measure of sterile points (O178). Expected for sparse T
  (Σ q^{−1/10+δ} small), but needs a multi-prime box dictionary that has not been written.
**Reading.** ES lives at ν-null points (integers) on the divergent side, so pattern/genus/measure arguments cannot
reach it (profinite B6). CONJECTURE-level spark: sterile points exist in G_T for *every* T ⊂ [q₀, ∞), divergent
or not (greedy heuristic: per-prime forbidden mass ≈ polylog(q)/q). If true, no finite ET covering exists for the
square class p·Sq^× of any prime p with least QNR ≥ q₀.
**Promise** 1–2 (clean language; no route).
