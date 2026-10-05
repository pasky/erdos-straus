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

## Theorem 1.2 / Corollary 1.3 — fixed-set stacking

Re-derived line by line; **SOUND**.

* Sieve input = notes Lemma 12.1. I re-checked its proof: Parseval
  `(1/ℓ)[(ℓ−ν)g²+ν]=g` with `g=ν/(ℓ−ν)`, Cauchy–Schwarz gives (12.2), large
  sieve with `Q=X^{1/2}`, Markov `H(Q)≥V^{-1}/2` when `log Q≥2Λ`. Gives `|S|≤4XV`. ✔
* Sifted classes: for odd `ℓ>y`, `ℓ|p+a ⇒ ℓ|x_a ⇒ ℓ mod a∈C(x_a)⊆S_{σ_a}`; so
  removing `{t: ℓ|24t+1+a}` when `ℓ mod a∉S_{σ_a}` is legitimate. Roots distinct
  for `ℓ>2max A` (also `ℓ∤a`, `ℓ∤24`). `ν(ℓ)≤J+1<ℓ` since `max A≥4J−1`. ✔
* `Λ≤(J+1)(log z+O(1))=(log X)/5+O_A(1)≤(log X)/4`. ✔
* Density: `G∖S_σ` is exactly `φ(a)/2` reduced classes, so Mertens in APs mod
  the fixed a gives `½ log log z+O_a(1)` per window, regardless of which
  selection; the sum over windows is additive, **no independence between
  windows is needed** (the large sieve takes arbitrary root sets). Windows
  sharing prime factors (e.g. a=15 and a=3) are harmless: the per-ℓ root
  `−(1+a)/24 mod ℓ` depends on a only as an integer. ✔
* Uniformity in the class sets: only finitely many (`2^{Σβ}`) selection
  vectors, each with the same `V` up to `O_A(1)`. ✔
* Cor 1.3: `p>3Z` makes every `a≤Z` admissible (`x_a<p`), and
  `gcd(x_a,a)=gcd(x_a,p)=1`, so Lemma 1.1 applies; `J(Z)=⌊(Z+1)/4⌋` ✔;
  `T(N,7)≪N/(log N)^2`, `T(N,11)≪N/(log N)^{5/2}`, `T(N,23)≪N/(log N)^4` ✔.
* The claim that it upgrades POINTWISE_WINDOW §6's joint "dimension ≥J/2"
  Assessment to a theorem is correct: Lemma 1.1 removes the `<qφ(q)`
  exceptional primes of Lemma 6.1 that blocked a clean sieve.

## Corollary 1.4 — two-sided orders: SOUND-AFTER-REPAIRS (labels only)

Equivalences `a_min≥7 ⟺ a_min>3` (Z=3, J=1, exponent 3/2) and
`a_min≥11 ⟺ a_min>7` (Z=7, J=2, exponent 2) ✔. Lower bounds: W1 counts
`p≡1 (840)` (⊂ `p≡1 (24)`) with window 3 failing ⇒ `a_min≥7` ✔; W2 analogous on EH.

* **MINOR-1** (Table row 1.4 / Cor 1.4 first bullet): status written "PROVED"
  but W1 is "PROVED modulo cited sieve theorems S1–S3" (S1, the semi-linear
  β-sieve, not read in a primary source per POINTWISE_WINDOW §2.1). Repair:
  label the lower half "PROVED modulo the sieve theorems cited for W1".
* **MINOR-2** (Cor 1.4): the counts `#{p≤x: a_min(p)≥7}` do not say `p≡1 (24)`;
  the upper bound (Thm 1.2) is proved only for that class. Either add
  `p≡1 (24)` or note that the same sieve with `p=4t+1` covers all `p≡1 (4)`.
