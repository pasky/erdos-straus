# Review R28 of EXCEPTIONAL_KARY3.md (O28) — hostile reviewer

Reviewer branch `side-agent/review-kary3`; author files merged ff from
`side-agent/kary2-loglog`. Work in progress; verdict table at the end of
the pass.

## Checks done so far

### ElT (7.10), Thm 7.1, Cor 7.4 (sources/elsholtz-tao-1107.1010.pdf, pp. 25–32)

Verbatim statements match the author's §3 quotes:
* Thm 7.1: `N > 1`, P of degree D with non-negative integer coefficients
  `≤ N^l`, `ρ(p^j) ≤ C` for all p, j ⇒ `Σ_{n≤N}τ(P(n)) ≪_{D,l,C} N Σ_{m≤N}ρ(m)/m`.
  No irreducibility hypothesis. ✓
* Cor 7.4: `a, b ≪ N^{O(1)}` ⇒ `Σ_{n≤N}τ(an+b) ≪ τ((a,b)) N log N`. ✓
* (7.10): `Σ_{a≤A}Σ_{m≤B}ρ_{ka}(m)/m ≪ A log B log(1+k)`,
  `ρ_{ka}(m) = #{b mod m : kab²+1 ≡ 0}`. In the paper it sits inside the
  proof of Prop 1.4 (case A ≤ B), whose header has `k ≪ (AB)^{O(1)}`.

**Uniformity in k (hard check (i)).** I re-derived every step of the proof
(pp. 30–32) and tracked the k-dependence:
1. reduction to odd m: ρ_{ka}(2^j) ≤ 4, absolute. ✓
2. a = 2^l a₀, 2^l absorbed into k: `log(1+2^l k) ≤ log(1+k) + l`,
   weighted by `A/2^l`; summable in l, absolute. ✓
3. `q < A`: character `a ↦ (−ka/q)` on odd a, period 2q. It is principal
   iff q is a perfect square (Jacobi symbol `(·/q)` principal ⇔ q = □).
   ElT's "sums to zero" is false for square q (author's slip is real);
   square q give `≤ A Σ_{q=□} log(B/q)/q = O(A log B)`. Absolute. ✓
4. `A ≤ q ≤ kA`: trivial, `A log B·(log k + 1)`. ✓
5. `q > kA`: second slip (not flagged by the author): ElT's
   `c(q) = (−1)^{(q−1)/2 + m(q²−1)/8}` omits the reciprocity sign
   `(−1)^{((q−1)/2)((k′a−1)/2)}`; harmless, since for fixed a it is still
   8-periodic in q. Mean zero: the function `q ↦ (−ka/q)` (fixed a) is the
   Kronecker character of `−ka < 0`, never principal, so mean zero
   over period `8k′a` holds even when `k′a` is a square. Partial summation:
   `≤ 8k′a · log B/(kA) ≤ 8 log B`, absolute. ✓
6. `Σ_{m≤B, q|m}1/m = (log(B/q) + O(1))/q`, absolute. ✓

Verdict: (7.10) holds for all `A, B ≥ 2`, all `k ≥ 1`, with an absolute
implied constant. The `k ≪ (AB)^{O(1)}` hypothesis is needed only for the
Thm 7.1 / Cor 7.4 step converting τ-sums into ρ-sums. **Author's claim
SOUND.** (Suggest recording the second slip, item 5, for completeness.)

### Lemma 2.1 — SOUND
Re-derived: `log M = Σ_{p^v‖M, p^v≤y} v log p + log S_y(M) ≤ Z_y(M)log y + log S_y(M)`
(Z counts all `p^ν ≤ y` dividing M, including those with `p | S_y`, which
only increases Z). Squarefullness of S_y uses `P(M) ≤ y`. Constants: none.

### Lemma 2.2 — SOUND
`#{ν ∈ ℕ^m : max ν = t} ≤ m t^{m−1}`; `p^{−t} ≤ p^{−1}2^{1−t}`; c_m depends
on m only; Mertens + `γ'(p) ≤ 1 + 2p^{−1/2}`: `C_k(W)` depends on k, W
only, not on y. ✓
