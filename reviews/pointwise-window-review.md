# Hostile review: POINTWISE_WINDOW.md (branch side-agent/window-omega @ fba65aa)

Reviewer: side-agent/review-window. Scope: POINTWISE_WINDOW.md, AGENT_REPORT_O10.md,
scripts/window_{w1,joint}.py, data/pointwise_window/, sources/sieve/.
Verdict per item; numbered defects at the end (D1, D2, …).

## Items

### 1. Window-3 reduction, Lemma 1.1, Lemma 1.2 — CORRECT

* q=3, p≡1 (3): both targets coincide, `−1≡−p≡2 (mod 3)`. `Rat_3(n)∋2` iff some
  prime factor of n is ≡2 (3) (if all factors ≡1, every u/v≡1; a factor r≡2 gives
  u=r, v=1). `x_3=(p+3)/4<p`, so `p∤x_3`; `gcd(x_3,3)=gcd(x_3,p)=1`. So window 3
  fails iff `n_3` has no factor ≡2 (3), and since 3 is the smallest q≡3 (4),
  `a_min≥7` follows. Both targets checked.
* Lemma 1.1 (F1 ⇒ fail): via Lemma 8.2 (needs p≡1 (8), q<3p; both hold) and
  Cor 8.3(a); Jacobi symbol is a character on `Rat_q`, `(−1/q)=−1`,
  `(−p/q)=−(x/q)=−1`. Correct.
* Lemma 1.2: `(n_q/q)=∏(r/q)^{v_r}`, `4n_q≡p (q)`, `(4/q)=1`. Correct (r=2
  counted as bad when `(2/q)=−1`; harmless since `n_3` is odd).
* "Hard": `1 mod 840` is one of Mordell's six classes {1,121,169,289,361,529};
  POINTWISE_SIZE §11 uses "hard" = Mordell-hard. Correct.

### 2. Theorem W1 proof (§2.2) — CORRECT (modulo S1–S3, as labelled)

Checked line by line:
* Sifting data: `n_p=210k+1`, so 2,3,5,7 ∤ n; `g(2)=g(5)=0` is legitimate;
  `d|n_p ⟺ p≡−3 (d)` is one reduced class mod `840d`; `φ(840d)=192φ(d)`.
* Dimension: `(1−1/ℓ)(1−(ℓ−1)^{−2})=(ℓ−2)/(ℓ−1)=1−g(ℓ)` — verified algebraically.
* Remainder: moduli `840d≤x^{1/2}(log x)^{−B}`, distinct per d; BV applies.
* `f(s)≥(e^γ/π)^{1/2}(s−1)^{1/2}` on `[1,2]`: verified (`t(t−1)≤2(t−1)`).
* Step 2: `k<1/(1/2−ε)≤2.22`, parity ⇒ k∈{0,2}. Correct.
* Step 4: `a/φ(a)·y=(x+3)/φ(4mr_1)=(x+3)/(2φ(m)(r_1−1))` (m odd, coprime to r_1,
  because all its primes are ≡1 (3)) ⇒ the stated `9C_0x/(log x)^2/(φ(m)(r_1−1))`.
  `Σ_{k≥1}1/φ(ℓ^k)=ℓ/(ℓ−1)^2` and `1+ℓ/(ℓ−1)^2 ≤ (1−1/ℓ)^{−1}(1+(ℓ−1)^{−2})`
  verified. The r_1-sum is over primes ≡2 (3) only, so the true size is ≈ε, and
  3ε is a safe overestimate. `C_3=27√2C_0C_2` checks.
* S2 is fine: the Selberg remainders are `≤ω(d)`, independent of a, so it is
  uniform for `a≫y`. (HR Thm 3.12 is the right family; the doc re-derives it anyway.)
* Step 5: c_1 is ε-independent (V(z) with `1/2−ε∈[0.45,0.5]`), so the
  `ε^{1/2}` vs `ε^{3/2}` choice of ε works.
* S1 citation: Teräväinen (archived, line 1446) cites exactly "[Opera de Cribro,
  Theorem 11.13], with β=1" for the semilinear sieve, with the same `f(s)`. The
  primary is not read, and the doc says so honestly. See D3 for the
  ch.14-vs-Thm-11.13 inconsistency with POINTWISE_SIZE Prop 11.4.

No mathematical gap found. Prop 11.4 → PROVED modulo S1–S3 is justified.
