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
