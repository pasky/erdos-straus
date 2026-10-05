# Review R45b of POINTWISE_OMEGA12.md (reviewer 2 of 2: §6–6B, the exponent assembly)

Reviewer: hostile side agent (branch side-agent/review-omega12b). Reviewed: POINTWISE_OMEGA12.md at
`side-agent/homega` 1eeefea (merged non-ff into this branch, since main had moved on).
Scope: Thm 6.1, Lemma 6.2, Thm 6.3, Haar corollary, §6A last para, §6B table; their use of O11
Lemma 1.1/Cor 1.2/Lemma 2.1/Lemma 2.2/Lemma 3.1/Thm 3.2/Cor 3.3/Cor 4.1 and O9 Thm 1.1.
Thm 5.1 (H_ω(2)) and §§1–4 are taken as given (other reviewer), except where noted.

STATUS: in progress.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 6.1 (`(log p)^{1/5}(loglog p)^{−2/5}`) | pending |
| Lemma 6.2 (pre-quarantine `ℓ≤𝓛`, `s_1=e³g/M`, cost `1.02𝓛+7`) | pending |
| Thm 6.3 (`(log p)^{1/5}(loglog p)^{−1/5}`) | pending |
| Haar corollary `log(1/δ*)≪𝓛^5log𝓛` | pending |
| §6A last para (CONJECTURE label) | pending |

## Defects

(none yet)

## Derivations

### D1. Lemma 6.2 (re-derived)

* Fibre probability (O11 Setting 2.0): coordinate `X_ℓ` uniform on the fibre `1+ℓ^{a}ℤ mod ℓ^{f}` (units if
  `a=0`). Fixing `X_ℓ mod ℓ^v` (`v>a`) has probability `ℓ^{−(v−a)}` if `a≥1` (the fibre mod `ℓ^v` has `ℓ^{v−a}`
  elements, uniform), `1/φ(ℓ^v)` if `a=0`. Off supp (`v≤a`) the factor is 1 and `ℓ^v | gcd(M,Q)`. So
  `P(E)=∏_{ℓ∈supp,a≥1}ℓ^{a}/ℓ^{v}·∏_{ℓ∈supp,a=0}(ℓ/(ℓ−1))ℓ^{−v}·1 = (gcd(M,Q)/M)·∏_{ℓ∈supp,a_ℓ=0}ℓ/(ℓ−1)` — an
  *equality*, matching the author's display. ✓
* Monotonicity: the procedure only raises exponents, so `a_ℓ≥1` for every odd `ℓ≤𝓛` at every stage; hence
  `a_ℓ=0 ⇒ ℓ>𝓛`. Need `a_ℓ=1≤f_ℓ=⌊𝓛/logℓ⌋`, i.e. `ℓ≤T`: true since `𝓛≤T`. ✓
* Euler factor: `ℓ>𝓛 ⇒ ℓ−1>𝓛−1≥1`, number of such `ℓ|M` is `≤log M/log𝓛 ≤ 𝓛/log 𝓛` (author uses the cruder
  `ω(M)≤1.45𝓛`). `∏(1+1/(ℓ−1))≤exp(#/(𝓛−1))≤exp(1.45𝓛/(𝓛−1))≤e^{2.9}` at `𝓛=2`, decreasing in 𝓛. ✓
  (Sharper: `≤exp(𝓛/((𝓛−1)log𝓛))→1`; irrelevant to the exponent.)
* `gcd(M,Q)|g` by survival (`gcd(M,Q)|4D+1`). So `P(E)≤e³g/M=s_1`. ✓ (from-scratch check: D3.)
* Start cost: `Q_start=8·∏_{odd ℓ≤max(𝓛,7)}ℓ`, `log Q_start≤log 840+θ(𝓛)≤6.73+1.01624𝓛` (Rosser–Schoenfeld
  1962 Thm 9: `θ(x)<1.01624x` for `x>0` — correct citation). ✓
* Cost of the iteration: O11 Lemma 2.2's charging sums, over the *steps actually taken* `(ℓ,a→a+1)`,
  `logℓ<𝓛w_ℓ(Q_i)/(c(a+1))≤(𝓛/c)Σ_{v_ℓ(M)≥a+1}s_1/(a+1)`. The pre-set steps `(ℓ≤𝓛, 0→1)` are not charged
  (paid by `θ(𝓛)`), so the sum over taken steps is `≤(𝓛/c)Σ_{(M,D)}s_1·h(M)`. The only Lemma 2.1 input is
  `w_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}s_1`, valid at every stage `Q_i` because `P(E)≤s_1` holds for every Q reached (not
  for every Q — the author correctly says "every Q reached"). ✓
* (LLL): unchanged — at termination every `ℓ` with `a_ℓ<f_ℓ` (in particular every pre-set ℓ that remains a
  coordinate) has `w_ℓ≤c(a_ℓ+1)logℓ/𝓛`; `ℓ∈supp E ⇒ a_ℓ+1≤v_ℓ(M)`; sum `≤c·logM/𝓛≤c`. The stopping test is
  applied to the pre-set primes too (the loop ranges over all odd ℓ with `a_ℓ<f_ℓ`). ✓
* (I): O11 Lemma 2.1's (I) proof uses only `n≡1 (Q)` and Fact 1.1, no structure of Q. ✓

**Verdict Lemma 6.2: SOUND** (pending numerical check D3).
