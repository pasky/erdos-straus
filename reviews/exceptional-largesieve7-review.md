# Review R73 of EXCEPTIONAL_LARGESIEVE7.md (hostile reviewer, branch side-agent/review-ls7)

Status: in progress. Reviewed text: `EXCEPTIONAL_LARGESIEVE7.md` as merged from
`side-agent/residue-dispersion` (commit 6bae2a4). From-scratch scripts: `scripts/review_ls7_*.py`.

## Verdict summary (per claim)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (proof re-derived; brute force M<20000) |
| Lemma 1.2 | SOUND (re-derived; brute force all p \| M, M<20000) |
| Lemmas 2.1–2.2 | SOUND-AFTER-REPAIRS (D1 citation: Shiu's class M not literally satisfied; Nair–Tenenbaum fixed-ε form needed; D2 constant) |
| Thm 3.1 | (pending) |
| Prop 4.1 | (pending) |
| Remark 4.2 | (pending) |
| Thm 4.3 | (pending) |
| Prop 5.1 | (pending) |
| (RD′) / §5 sketch | (pending) |
| Cor 6.1, §7 | (pending) |

## Defects

(numbered below as found)

**D1 (MAJOR, misapplied citation; repairable). §2 Lemma 2.1, last paragraph of proof.**
Shiu 1980 Thm 1 (checked against `sources/shiu-1980.pdf`, p. 162–163) requires `f ∈ M`:
(i) `f(p^l) ≤ A₁^l`, and (ii) **for every ε > 0** `f(n) ≤ A₂(ε)n^ε` for all n. The function
`f(n) = 1[P(n) ≤ 2Q]Γ(n)n^η` with fixed `η = 1/log 2Q > 0` **violates (ii) for every
ε < η** (take `n = 2^m`, m → ∞). The text's "η ≤ 1/log z ≤ ε/2 for N large" only gives (ii)
for each *fixed* ε once N ≥ N₀(ε) — not the "for every ε" hypothesis — so Thm 1 does not
apply as cited. The conclusion is nevertheless correct: Nair–Tenenbaum 1998
(`sources/nair-tenenbaum-1998.pdf`, Thm 1 with k = 1, class `M₁(A,B,ε)` with a **single
fixed** ε, `0 < ε < 1/8`, constant depending only on A, B, ε, δ; progressions via the
uniformity in the coefficients of Q, their remark after Thm 1) covers it with `A = 8e`,
`B = B(ε)`, ε = 1/16 say, uniform in Q because `η ≤ 1/log z ≤ ε/2`; alternatively "Shiu's
proof uses (ii) only for one ε = ε(α, β)". *Repair:* cite NT98 Thm 1 (or Shiu's proof, with
that remark) instead of Shiu Thm 1 as stated, and change "PROVED given Shiu 1980 Thm 1" to
"PROVED given Shiu's theorem in the fixed-ε form (Nair–Tenenbaum 1998, Thm 1)" in Lemma 2.1,
Thm 3.1, Thm 4.3 and the summary table. (Applied by reviewer.)

**D2 (MINOR, constant). §2 Lemma 2.1 proof.** "`f(ℓ^l) ≤ 3e^l`" and "`γ'(ℓ) ≤ 3`" are false
at small primes: K2 §2 sets `γ'(p) = γ(p)` for `p ≤ W`, with `γ(2) = 8` (whence K2's
`Γ(m) ≤ 8·3^{ω(m)}`); also `(1−2^{−1/2})^{−1} ≈ 3.41`. Correct: `f(ℓ^l) ≤ 8e^l`, `A₁ = 8e`.
Harmless. *Repair applied:* `3e` → `8e`.

## Per-claim notes

### Lemmas 1.1, 1.2 — SOUND
Re-derived: `g = gcd(D,A)`, `u = D/g`, `v = A/g` is coprime, `u | Av` ⇒ `u | A`, `uv | A`;
injectivity via `gcd((A/v)u, A) = A/v`; `4A ≡ 1 (M)` gives the three congruent labels, all of
the admissible form `−r/s`, `r ≥ 0`, `s ≥ 1`, `gcd(s,M) = 1` (LS6 §6.2 definition of H*), so
the H* bound is immediate. Lemma 1.2: `uvt = A ≡ 1/4 (p)` for odd `p | M`. Correct.
`scripts/review_ls7_triples.py` (from scratch; `uv run --with sympy --with numpy`): for all
`M ≡ 3 (4)`, `M < 20000`: set equality `{−4D : D | A²} = {−u/v}`, the bijection, `D = u²t`,
`A²/D = v²t`, all three label congruences, and Lemma 1.2's pinning at every prime `p | M`
(310815 (triple, prime) pairs) — 0 failures. Additionally (not checked by the author) the
H* upper bound `H* ≤ min(max(u,v), 4u²t, 4v²t)` against a brute-force least-label-height
for all `M < 4000` (22502 triples; equality in 20608) — 0 failures; Remark (a)'s example
`M = 167`, class 131, `H* = 13` via `−13/5` confirmed. (The author's "159390 triples" counts
triples, not (triple, prime) pairs — consistent.)

### Lemmas 2.1, 2.2 — SOUND-AFTER-REPAIRS (D1, D2)
Re-derived line by line: dyadic split `P(n) ∈ (Q,2Q]`, `Q ≥ y/2` covers `P(n) > y`;
`ℓ^η ≤ e` for `ℓ ≤ 2Q`; `e^x ≤ 1 + ex` on `[0,1]` gives `f(ℓ)/ℓ ≤ γ'(ℓ)/ℓ + eγ'(ℓ)η log ℓ/ℓ`;
Mertens gives `exp(Σ) ≪_W log 2Q·Π_{ℓ|k,ℓ≤2Q}(1−1/ℓ)` (using `e^{−x} ≤ (1−x)e^{x²}`, x ≤ 1/2);
`φ(k)^{−1}Π_{ℓ|k,ℓ≤2Q}(1−1/ℓ) = k^{−1}Π_{ℓ|k,ℓ>2Q}(1−1/ℓ)^{−1}`; the absorption
`2/(Q log 2) ≤ 1/(2 log 2Q)` holds for `Q ≥ z/2` large. Shiu's other hypotheses at the
parameters used: `x = 2Y`, interval length `Y = x/2 > x^β` (any β < 1/2), `k ≤ Y^{1−α}`,
`gcd(c,k) = 1` — fine; small x absorbed in the constant. Lemma 2.2: `Σ_i i^{r−1}e^{−i/(2L)}
≤ C_r L^r(1+log L)`, then `Σ_j j^s e^{−2γ j log 2/log z} ≤ C_s(log z/γ)^{s+1}`, `K^{2β} ≤ e^γ`
(needs `K ≤ z^{γ/2}`, as in K2) — correct. Only defects: D1 (citation), D2 (constant).
