# R32: hostile review of O32 / POINTWISE_XWIN.md

Reviewer branch `side-agent/review-xwin` (merged `side-agent/xwin-average` at 8d89852).
From-scratch scripts: `scripts/review_xw_*.py`.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 (half-set) | SOUND |

## Lemma 1.1 — half-set lemma

Definition checked against POINTWISE_SIZE §8.1: `Rat_q(x)={u/v mod q: uv|x, gcd(u,v)=1}`.
There is no separate "exponent budget" in the definition; the budget `|f_r|≤v_r(x)`
of Cor 8.3(b)/notes §70 F3 is simply the constraint `uv|x`. Lemma 1.1 uses only
`u=r`, `u=rs`, `u=r,v=s` for distinct primes `r,s|x`, all of which satisfy `uv|x`
whatever the exponents; so "no budget exceptions" is correct (the lemma is a pure
necessary condition, the budget can only remove elements from Rat, never add).

Re-derivation: −1 is a non-square mod a (a has a prime factor ≡3 (4)), so the
Klein orbits are of size 4 (g²≠1) or 2 (g²=1, `{g,−g}`); checked all six
coincidences. Excluding `gh=−1` and `g/h=−1` for distinct classes, plus `−1∉C`,
is exactly "C meets one half of each orbit, and picks 1 from {1,−1}". Equal-class
pairs (two primes in one class g): `g²≠−1`, `g/g=1`, harmless. Count of orbits:
`2^{ω(a)}` involutions (a odd, CRT), so `β(a)=(φ−2^ω)/4+2^{ω−1}−1`. ✔.

**From-scratch check** (`scripts/review_xw_halfset.py 300 20000`): for every
a≡3 (4), 3≤a≤300 (incl. composites), every x≤20000 and 2000 random x∈[10^8,10^12]
coprime to a, full enumeration of Rat_a(x); whenever −1∉Rat_a(x), verified C(x)
lies in some S_σ. Also verified `|S_σ|=φ(a)/2`, number of 2-orbits `=2^{ω−1}`
and the β formula. 1,119,553 failing pairs, no counterexample (15 s). EVIDENCE
supporting a proof I find correct.

Minor remark (no defect): Remark (iii) is right that the lemma only concerns
the −1 target, so the theorems below bound a superset of window failure.
