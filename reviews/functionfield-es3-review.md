# R173 — hostile review of FUNCTIONFIELD_ES3.md (O173)

Reviewer: R173 (side agent). Reviewed: FUNCTIONFIELD_ES3.md, reviews/agent-reports/AGENT_REPORT_O173.md, scripts/ff3_*,
data/ff3_* (merged from side-agent/ff-sterile-point). Background: FUNCTIONFIELD_ES.md §6.2, FUNCTIONFIELD_ES2.md §0,
R166 review, DISCOVERIES (J)4/(J)12.
From-scratch scripts: `scripts/review_ff3_*.py` (own F_p[T] arithmetic, pure Python, 1 core). Logs `data/review_ff3_*`.

(in progress)

## Re-derivations (paper)

* Lemma 1.1: re-derived. A·L | P + E gives (i); T ∤ E, P ≡ 1, T^k X ≡ 1 (mod E), a0, b0 units mod E; the four type
  residues; mixed types give E | 1 + T^k a0 b0 = 1 + T^{N+1+γ}L'g' and lc(s) = 1. Converse (types 0 and 2,
  a0 = T^γ g', b0 = T^j L') checked: gcd/lcm are right because g' | L', γ ≤ j; s·T^k b0 ≡ D (mod E).
* Lemma 1.2: re-derived. deg D ≤ (N+1+γ) + 2l ≤ 2(N+1+l) − 2 since γ ≤ N − 1 (k ≥ 2); the class of E' is
  {−u^{−1} mod T^{N+1}, −1 mod L'} because D ≡ 1 modulo both; ρ + 1 = L'h, h const ⇒ T | L' (uses ρ(0) = −1, i.e.
  u(0) = 1). g' has degree ≤ l < deg ρ, so it equals the least residue.
* Lemma 2.1 (a)–(c): re-derived (see defect list for the N + γ ≥ 3 step).
* Lemma 2.2: re-derived line by line, including the Z' = −Z sub-case (c = −1, v_T(Z) = γ − 1, gcd(g', Z1) = 1,
  Z1 ∈ {1, T − 1}).
* Lemma 2.3: re-derived (i)–(iv). Degree of (****): deg(T^{N+1}ZZ') = N+1+z+z' > max(z, z'+1) since N ≥ 1.
  z + z' = γ + l + deg g' − N ≤ 2l − 1 (γ ≤ N − 1); N ≤ max(z, z'+1) + |z − z'|; hence N ≤ 4l − 1 − 3 min(z, z').
* Lemma 3.1: re-derived (needs γ + 1 ≤ j − 1, i.e. γ ≤ j − 2; D unchanged; cylinder mod T^{k+j−1} ⊇ mod T^{k+j}).
