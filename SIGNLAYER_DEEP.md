# SIGNLAYER_DEEP — deep dive of spark brainstorm B (task O175)

Status: in progress. **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Memos: `BRAINSTORM/bsB_*.md`; scripts `scripts/bsB_*`.

Chosen topic (from the memos): the function-field sterile point x*_c (FUNCTIONFIELD_ES2 §0.2, Conjecture 0.2),
read through the sign layer (`bsB_sterile_pretentious.md`: x* is a profinite square, maximally pretentious; its
only sign-layer constraint is a degree parity). Goal: decide whether x*_c (q = 3, A = T²) is covered by a Case B
family, construction-first; if not, find the structural reason.

## 1. Case B at the slice x ≡ 1 off T is a finite search for each level (PROVED, elementary)

Setting (FF2 §0.2, q = 3, k = 2; everything holds for odd q with the obvious changes noted). A point of the slice
is x_u (≡ 1 at every prime ≠ T, ≡ u mod T^∞), u = 1 + Tv, v(0) ≠ 0. FF2's Case B reduction: for monic L'
(T ∤ L'), j ≥ 1, g = T^γ g' (g' | L' monic, 0 ≤ γ ≤ j), N := j + 1, D := 1 + T^{N+1}L'g, a Case B family valid at
x_u exists iff D = E·E' with E, E' monic, E ≡ −u (mod T^{N+1}), E ≡ −1 (mod L').

**Lemma 1.1.** Put K := N + γ − 1 (so N − 1 ≤ K ≤ 2N − 2) and L' = g'L''. Case B families valid at x_u with
these (N, γ) correspond bijectively to tuples (h₁, h₁', g', L'', r) of polynomials, h₁, h₁', g', L'' monic with
nonzero constant term, such that
* (I) `h₁ + h₁' = T·g'·r`,
* (II) `h₁·h₁'·L'' = T^K + r`,
* (III) `h₁·L' ≡ −v (mod T^N)`, L' = g'L''
(E = −1 + T h₁ L', E' = −1 + T h₁' L'). Moreover deg r < deg(h₁h₁'), so **L'' = quo(T^K, h₁h₁') and
r = L''h₁h₁' − T^K are determined by (h₁, h₁', K)**, and deg h₁ + deg h₁' + deg L'' = K. In particular, for each
K the set of Case B families on the slice is finite (deg L' ≤ K + max deg h ≤ 2K), and each family covers the
cylinder `u ≡ 1 − T·h₁·L' (mod T^{N+1})`.

*Proof.* E ≡ −1 (mod L') ⟺ E = −1 + L'h; E monic and deg(L'h) ≥ 1 (else E = 1, impossible mod T²) give
lc h = 1; same for E' = −1 + L'h'. EE' = D ⟺ L'hh' − h − h' = T^{N+1}g (cancel L'). E ≡ −u (mod T^{N+1}) ⟺
L'h ≡ −Tv; so h = Th₁ with h₁L' ≡ −v (mod T^N) (III), h₁(0) ≠ 0. Then T h₁h₁'L' − h₁ − h₁' = T^{K+1}g' (*).
Mod T: h₁'(0) = −h₁(0) ≠ 0. Leading terms: the left side has degree 1 + a + b + deg L' (a, b = degrees of
h₁, h₁') because h₁ + h₁' has degree ≤ max(a, b); so a + b + deg L'' = K. Writing (*) as
g'(T h₁h₁'L'' − T^{K+1}) = h₁ + h₁' shows g' | h₁ + h₁' and T | h₁ + h₁'; define r by (I); dividing (*) by Tg' gives
(II). deg r = deg(h₁ + h₁') − 1 − deg g' ≤ max(a, b) − 1 < a + b (if min(a, b) = 0 then deg r ≤ a − 1 < a + b
still). Conversely (I)–(III) give (*) and hence E, E' with all properties; the congruence E' ≡ −u⁻¹ is then
automatic (EE' = D ≡ 1 mod T^{N+1}). ∎

*Check against FF2:* the known cylinder family E = T² − cT − 1 (a0 = b0 = T, j = 1, D = 1 + T⁴) is
h₁ = T − c, h₁' = T + c, g' = L'' = 1, r = −1, K = 2, N = 2, covering u ≡ 1 + cT + 2T² (mod T³), as FF2 states.

*Consequence for the heuristic (Assessment).* FF2 §0.2 argued that the expected number of covering Case B
families diverges (sum over deg L'). Lemma 1.1 shows deg L' ≤ 2K is forced, so at fixed level the count is
finite, and the naive expected number of solutions at a fixed point is Σ_K poly(K)·3^{−K}-type, **convergent**.
So the heuristic no longer predicts that x* (or a generic slice point) is covered: sterility of individual
slice points is the heuristically expected behaviour, and Conjecture 0.2 is a "convergent lottery" statement.
