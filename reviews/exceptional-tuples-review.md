# Hostile review — EXCEPTIONAL_TUPLES.md (task O21, branch `side-agent/tuple-door` @ 331e863)

Reviewer branch `side-agent/review-tuples`. Subject files imported verbatim
from 331e863. Context read: EXCEPTIONAL_THETA.md (§1, Prop 2.4, Thm 2.5,
Lemmas 3.1/3.2, Cor 3.4), EXCEPTIONAL_KARY2.md Thm 5.1, DISCOVERIES (A)6.

**Overall verdict: SOUND-AFTER-MINOR-REPAIRS.** Every PROVED item checks out
at referee level. No mathematical error was found. The defects are about
scope, wording, and one missing explanation in the numerics (D2). D2 also
adds a heuristic point about TC_θ near θ = 1.

## Verdicts

| item | verdict | notes |
|---|---|---|
| Lemma 1.2 | SOUND | trivial |
| Lemma 1.3 (shift form) | SOUND | (1.4)/(1.5) correct; distinct residues per ℓ make different D for the same ℓ mutually exclusive. Wording nit D9 |
| Thm 2.1 | SOUND | identity `Σ_{j≤K}(−1)^j C(f,j) = (−1)^K C(f−1,K)` (f ≥ 1); j = 0 exact; error `≤ KηN`; CRT side `≤ Π(1−p)+e_K` since `C(f−1,K) ≤ C(f,K)` |
| Cor 2.2 | SOUND | `μ_{y_K} > K/e² − 1` holds because one step of y adds one `p_ℓ < 1`; `e_K ≤ (eμ/K)^K ≤ e^{−K}`; `Kη_K = e^{−K/e²}`; total `≤ (e + e^{−K(1−e^{−2})} + 1)` ≤ e+2. y_K depends only on K (no y-vs-N constraint is needed; `log y_K ≍ K^{1/2}` so `y_K = N^{o(1)}` under TC_θ). Values y₁₂…y₆₀ recomputed: 30, 126, 358, 1150, 3162 ✓ |
| Cor 2.3 | SOUND (as an implication) | in fact `E(N) ≤ (e+2)N exp(−(2/e²)(log N)^θ)` without o(1). Constant not optimal (D10) |
| Prop 2.4 | SOUND | `e_j(F) ≤ (ΣF)^K` needs ΣF ≥ 1 ✓; `ΣF ≤ yμ_y`; `(log y_K)² ≤ K/(ce²)`; condition `K^{3/2} ≲ log N` ✓. "Recovers 2/3 without the (log log)^{1/3}": correct, it is weaker than (A)6 |
| Thm 3.1 (truncated weights) | SOUND | see "Thm 3.1 check" below |
| Cor 3.2 | SOUND | parameter arithmetic re-done, see below |
| Cor 3.3 | SOUND within stated scope | the "both directions" summary overstates (D4) |
| Cor 3.4 | SOUND | level `≤ kA log N` is correct for K2's level (distinct primes > W, lcm ≤ N^{kA}); the "bounded k useless" reading needs Cor 3.3's scope (D5) |
| Prop 4.1 | SOUND | Chebyshev + `|S| ≤ N` + `P(x) ≤ e^{−Z(x)}` are all correct. Entropy ≍ (log y)³ is asserted in §0 but only implicitly proved (D6) |
| Prop 4.2 | SOUND (mathematics), proof cites the wrong statement (D1) | Jacobi argument re-derived: for prime q \| A, `ℓ ≡ −1 (q)`; odd q: `(q/ℓ) = (−1)^{(q−1)/2}(−1/q) = 1`; q = 2: `ℓ ≡ 7 (8)`; so `(−4D/ℓ) = −1`. `0 ∉ 𝓡(ℓ)` as `(A,ℓ) = 1`. Squares avoid ✓ (checks.txt (2): 42 546 classes all QNR). Count: `#{f=0} ≥ ⌊√N⌋` against `(e+2)N e^{−K/e²} ≤ (e+2)N^{1/2−ε/e²}`; the `Ne_K` term is `≤ N·N^{−e²/2}`, negligible ✓ |
| Prop 4.3 | SOUND as stated | its use in §4.2/Assessment 4.4 is wider than the statement (D3) |
| §5 numerics | REPRODUCED | `tuples_checks.py` output identical; `tuples_moments.py 1e6 … es` output bit-identical to `moments_N1e6_es.txt`; §5 tables match the data files. Interpretation of (c) is incomplete (D2) |

### Thm 3.1 check (the truncated-weight extension of ET Prop 2.4)

* ET Prop 2.4 is stated for arbitrary weights `s_i ≥ s_* > 0`. Its proof
  uses the weights only through the bands `B_g` (Step 1), the lower set
  `Λ = {Σ j_g s_g ≤ λ}` (Step 3, which needs `s_i ≥ s_g` on `B_g`), and
  `e^{−2αs_g} ≤ e^{−αs_i}` (Step 5). None of these uses `s_i = log ℓ`.
* With `s_ℓ = min(log ℓ, L₀) ≤ L₀ ≤ λ`, no coordinate is discarded in
  Step 0. The hypothesis `p_i ≤ 1/4` is then needed for **every** slice
  prime, not only for `ℓ ≤ e^λ` as in ET Thm 2.5. Thm 3.1 assumes it. For
  Cor 3.2 it comes from ET Cor 3.4's first check,
  `|F_ℓ(c)| ≤ ℓ^{C+o(1)} ≤ ℓ/4` for all `ℓ ≥ ℓ₀(C)`. That check holds for
  all slice primes, not only small ones ✓.
* Mixed condition ⇒ weighted level ≤ λ:
  `Σ_{T_i} s_ℓ ≤ min(Σ log ℓ, |T_i|L₀)` ✓. Conditioning on `(c, x)`:
  `E[1[n≡b_i (d_i)] | c, x]` depends only on `x_{T_i}` (non-slice digits
  are independent and uniform; prime powers of ℓ ∈ T_i are fine) ✓.
* Jensen over c: the weights, and hence `G` and `s_*`, do not depend on c.
  The fibre bound is affine in `p_ℓ(c)` apart from `log(16μ(c)+16)`, which
  is concave ✓. `ν_c(0) ≥ 1` because `|F_ℓ(c)| < ℓ` ✓.
* Cor 3.2: `λ = λ₀` because `kL₀ = λ₀`. Then
  `19αλ₀ ≤ 19λ₀^{3/4} + 57k log(A log N)`. First mass sum
  `≤ C min(α,1)^{−3} ≤ Cλ₀^{3/4}`. Second: `αL₀ ≥ 3 log(A log N)` and
  `μ̄ ≤ e·Cβ^{−3}|_{β=1/(A log N)}`, so it is `O(1)`. G-terms:
  `λ/s_* ≤ max(λ₀/log ℓ₀, k)`, so they are `O(log²(k+log N))` ✓.

## Defects

**D1 (minor, proof wording; Prop 4.2).** The proof says squares contradict
"Corollary 2.2's `(e+2)N e^{−K/e²}`". Corollary 2.2 *states* a bound for
E(N), and squares are not ES exceptions, so that statement alone gives no
contradiction. The contradiction is with the bound
`#{n ≤ N : f_y(n) = 0} ≤ N(Π(1−p)+e_K+Kη_K) ≤ (e+2)N e^{−K/e²}`, i.e.
Theorem 2.1 with the estimates in the proof of Cor 2.2. *Repair:* cite
Thm 2.1 plus the Cor 2.2 estimates. Better, record that bound as
(2.2′) in Cor 2.2's statement.

**D3 (moderate, scope; Prop 4.3 vs §0/§4.2/Assessment 4.4).** Prop 4.3
covers only majorants built from **prime-family classes `−4D mod ℓ`,
ℓ ∈ 𝒫_y**, along r shifts. The table row ("one fixed shift pair:
Prop 4.3 caps any such input at O(log log N), however precise"), the
§0 row ("any modulus") and Assessment 4.4 ("Used for one fixed shift tuple
they are capped by Prop 4.3") apply it to divisor correlations
`Σ τ(n)τ(n+h)`. Those carry information about *all* divisors of `n+h`:
composite M, primes > y, and non-witness divisors such as `q ≡ 1 (4)`.
* The extension to all shift-form ES classes `M | n+4D`
  (`M ≡ 3 (4)`, `D | A_M²`, `M ≤ N^A`) is immediate and should be
  added: 0 is never hit, since `(D,M) = 1`; ν depends only on these
  indicators; and the CRT density of their avoiders is at least that of
  `{n : n+4D` has no prime factor `q ≡ 3 (4), q ≤ N^A` for every
  `D ∈ 𝒮}`, which is `≥ exp(−2r(log log N^A + 3))` by the same product.
* A ν that also uses **non-witness** indicators along the shifts (e.g.
  `q | n+4D`, q ≡ 1 (4), or exact divisor counts) is **not** covered.
  The `G(0) ≥ 1` argument needs every pattern of those indicators to
  occur on the full avoider set, and this is not proved.

*Repair:* add the extension, and restate the table, §0 and Assessment 4.4
as "majorants built from ES witness classes along the r shifts". Divisor
correlations used through other indicators should be listed under "not
covered".

**D4 (minor, label leak; Cor 3.3 closing sentence, §0 verdict, §4
verdict).** "The correlation order needed for saving `(log N)^θ` is
`(log N)^θ` up to `log log N`, **in both directions**" sits inside a
PROVED corollary (∎). The upper direction (order `2⌈(log N)^θ⌉`
suffices) holds only under TC_θ, a CONJECTURE. *Repair:* "necessary:
order `≥ c(log N)^θ/log log N` (PROVED); sufficient under TC_θ
(CONDITIONAL)."

**D5 (minor, scope; Cor 3.4).** Cor 3.4 bounds Eν. Its readings
("bounded k gives no θ > 3/4", "needs k ≥ (log N)^{4θ/3−1−o(1)}") are
about methods, and they need Cor 3.3's hypothesis `B ≥ ½N·Eν`
(CRT-main-term evaluation). As written the scope is missing. *Repair:*
add "for methods as in Cor 3.3".

**D6 (nit; Prop 4.1).**
* §0 states "entropy ≍ (log y)³". The proof shows `EZ ≥ c₂(log y)³`, and
  EZ is the entropy up to `Σ h₂` corrections. The upper bound
  `H ≤ Σ p_ℓ(log(1/p_ℓ)+1) ≤ (log y+1)μ_y` is never written. Add one line.
* Prop 4.1 is a pure entropy count: any law of entropy ≫ log N is
  TV-far from every N-point sample. It does not separate "many shifts"
  from "one shift", so the text should not present it as evidence for
  that distinction. Its correct use is "TC must be a low-complexity
  statement", which the text also says.

**D7 (minor, unlabeled claim; §2 Remark 3, used in §6.1).** "With
composite moduli M ≤ y the trivial range becomes `K ≲ (log N)^{3/4}`" is
not proved. Composite classes are not CRT-independent, so Theorem 2.1 is
not exact for them. §6.1 uses this remark to say that prime-family TC_θ
with θ ∈ (2/3, 3/4] gives nothing new for E(N). That conclusion is true
anyway, by the known 3/4 theorem. *Repair:* label the remark Assessment,
and base §6.1 on the 3/4 note.

**D8 (nit; §4.2 table).**
* Granville–Soundararajan is listed with "shifts: growing". Their sieve
  Erdős–Kac concerns a **single** n (one shift); what grows is the moment
  order. Fix the column.
* Ford arXiv:2408.03803 ("Poisson approximation of prime divisors of
  shifted primes") was first posted 2024-08-07, but the table says
  "(2025)". Content verified: Kubilius-model analogue for `p+a`, TV
  estimate, single shift ✓.

**D9 (nit; Lemma 1.3 wording).** `S_k` is the distinct-prime
("falling-factorial") part of the k-point correlations
`Σ_n Π ω_{y,D_i}(n+4D_i)`. The plain products also contain diagonal terms
with a repeated `(ℓ,D)`. (1.5) is stated correctly; only the gloss "is
the k-point correlation" is loose.

**D10 (observation, not an error; Cor 2.2/2.3 constant).** The choice
`μ ≈ K/e²` is not optimal. With `μ = βK`, the budget only needs
`(eβ)^K ≤ e^{−βK}`, i.e. `1 + log β + β ≤ 0`, which gives β ≈ 0.278
(vs e^{−2} ≈ 0.135). That doubles the constant in Cor 2.3,
`2/e² → ≈0.557`. It also changes the K-threshold in Prop 4.2 for that
recalibrated TC family. Not needed for any θ claim.
