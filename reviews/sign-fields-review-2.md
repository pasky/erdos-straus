# R236 — hostile review #2 of O232 (SIGN_FIELDS.md, BRAINSTORM/z8_*.md, data/z8/)

Reviewer: R236 (round 1, no edits to author files). Merged `side-agent/sign-fields` at 25fa4b4a (README conflict resolved
as a union of both tables). From-scratch scripts: `scripts/review_r236_cert.py` (certificate checker, sympy only, no
ec_cert/z8 import), `scripts/review_r236_misc.py` (Lemma 1.1 offsets, mod-840 table, integer square points, T1 control,
independent ES search s ≤ 10), further `scripts/review_r236_*.py` below.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 1.3 (ES for all 4^s + k, nine k) | SOUND (independently re-certified); MINOR wording/novelty issues |
| Lemma 1.1 | SOUND (MINOR: s ∈ {0,1} handled only by the certificates) |
| Lemma 1.2 | SOUND statement, proof has a slip at ℓ = 0 (MINOR) |
| §1.4 OPEN list / square points / k = 105 | (pending) |
| Prop 2.1 | (pending) |
| Thm 2.2 (a)–(d) | (pending) |
| 8/131, 8/241 | (pending) |
| §3 Prop 3.1 + Assessment | (pending) |
| §4 Assessment | (pending) |
| novelty | (pending) |

## 1. Theorem 1.3 — SOUND

**Independent certificate check** (`review_r236_cert.py data/z8/*.json 300`). The JSON field semantics (n = k·b^s + c with
json-k = 1 = c₀, json-c = the offset; x, y, z coefficient lists in n, low→high) were re-derived from the data (e.g.
k = 9, D₅: x, y, z = 2n/5, 4n/5, 4n; 5/2n + 5/4n + 1/4n = 4/n). For every class of all nine files I checked:
1. 4xyz − n(xy + yz + zx) ≡ 0 in ℚ[n] (sympy, exact).
2. Integrality by a *different* method from ec_cert's forward differences: with D = lcm of coefficient denominators,
   D·p ∈ ℤ[n], so p(n) ∈ ℤ is a condition on n mod lcm(M, D); all residues ≡ r (mod M) enumerated.
3. Positivity: leading coefficient > 0 and largest real root < 1 for every polynomial (n_pos = 1 everywhere — all
   coefficients turn out non-negative; positivity is automatic).
4. Periodicity, re-derived: write M = 2^a M′, M′ odd. For 2s ≥ a, 4^s ≡ 0 (mod 2^a), and 4^s mod M′ has exact period
   ord_{M′}(4); so n_s mod M is purely periodic in s ≥ ⌈a/2⌉ with period ord_{M′}(4). Checked ord_{M′}(4) | L for every
   class (the only even modulus is 2716 = 4·679 in k = 225, needing s ≥ 1; ord_{97}(4) = 24 = L).
5. Coverage of every s ∈ [s₀, s₀ + L) (s₀ = 0, or 1 for k = 225).
6. For s ≤ 300 the class formula evaluated at the actual integer n_s, checked as positive integers satisfying the identity
   (in particular s = 0, n = 1 + k even, is covered by a class in every file — no brute-force exceptions needed).
Result: all nine COVERED. The author's own `ec_cert.py` also passes on all nine (to m = 600; it uses a more conservative
m₀ = 2 for k = 225, harmless).

**Independent brute force** (`review_r236_misc.py` (e)): an independent ES search (x near n/4, then (ay − b)(az − b) = b²
over divisors) finds a solution for every s ≤ 10 for all 13 offsets k ≡ 9 (24), k ≤ 300 (including the four OPEN ones).

**T1 control.** All integer square points 4^ℓ + k = □ (finite: (t − 2^ℓ)(t + 2^ℓ) = k) for the nine k:
k = 9: 25 (ℓ = 2); 57: 121 (3); 129: 4225 = 65² (6); 153: 169 (2); 201: 1225 = 35² (5); 225: 289 (3); 81, 177, 249: none.
Each lies in a **D** (divisor) class of its certificate (D₅, D₁₁, D₅, D₁₃, D₅, D₁₇ respectively), and my check 6 evaluated
the actual solution there. Moreover every non-D class r (mod M) of every certificate is a *non-square* residue class mod M
(exhaustive over s mod M; `misc` (d)), consistent with T1 / Yamamoto — no family "proves" anything impossible.

**Mordell-hard members** re-derived from n_s mod 840 (period 6 for s ≥ 2): 57 (s ≡ 3 (6), 121), 153 (s ≡ 2, 169), 177 (s ≡ 5,
361), 225 (s ≡ 0, 3, i.e. 0 mod 3: 289, 121); 9, 81, 129, 201, 249 never hard. Matches the text.

Defects:
- **D1 (MINOR, novelty/wording, Thm 1.3 + abstract use).** Five of the nine k (9, 81, 129, 201, 249) are immediate from
  Mordell's mod-840 theorem (every n_s with s ≥ 2 avoids the six classes; certificate = D₅ ∪ II2 mod 15), and k = 153 is
  Mordell + the divisor class 13 | n_s (s ≡ 2 mod 6). Only k = 57, 177, 225 use a genuinely non-Mordell ET class
  (moduli 11/31/2015; 39; 39/2019/2716). Repair: say so explicitly in Thm 1.3 ("k = 9, 81, 129, 201, 249: Mordell;
  153: Mordell + D₁₃; 57, 177, 225: genuine coverings"), so the headline is not read as nine new results.
- **D2 (MINOR).** "These are near-square infinite families … on which polynomial families in m provably cannot cover"
  is true of the full family m² + k, not of the subfamily m = 2^s, and the exponential subfamily has only O(log X)
  members below X; the sentence should not suggest the certificate defeats the Z_k^□ obstruction — it sidesteps it
  (as (J)22 does). Repair: one clause "(the exponential subfamily is thin; the covering is of Sierpiński type, (J)22)".
- **D3 (MINOR, Lemma 1.2 proof, ℓ = 0).** "the odd components are the odd integer N = 4^ℓ + k": for ℓ = 0, N = 1 + k is
  even. The statement is still true for all odd k ≥ 3, but for k = 4^j − 1 (k = 3, 15, 63, …) ν(0) *is* a unit square at
  every odd q and is excluded only by the 2-adic condition x₂ = k ≡ 1 (mod 8) in Sq^× (EXPONENT_COVERING §1). Repair:
  "ℓ = 0: 1 + k a unit at all odd q forces 1 + k = 2^j; square at all odd q forces j even; then k ≡ 3, 7 (mod 8),
  violating x₂ ≡ 1 (8)" (or restrict the lemma to k ≡ 1 mod 8, where 1 + k ≡ 2 mod 8 is never a power of 4).
- **D4 (MINOR, Lemma 1.1).** The lemma is stated for s ≥ 2; members s = 0, 1 are covered only by the certificates (they
  are, check 6). One clause suffices.
