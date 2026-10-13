# DEDEKIND_ES — exact lattice-point formulas, Dedekind sums and reciprocity for ES certificates (O169)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.**
Labels as in DISCOVERIES.md. Scripts `scripts/dk_*`.

Notation. For 0 < A < n, gcd(A,n) = 1: `n/A = [[b₁,…,b_r]] = b₁ − 1/(b₂ − 1/(⋯ − 1/b_r))`, b_i ≥ 2, the
Hirzebruch–Jung (negative, "HJ") continued fraction; `r(n/A) := r` its length; `A* ∈ (0,n)` with `AA* ≡ 1 (n)`;
`s(a,c)` the Dedekind sum. `K(b₁,…,b_r)` = negative continuant (numerator of `[[b₁,…,b_r]]`):
`K(b) = b`, `K(b₁,b₂) = b₁b₂ − 1`, `K(b₁,b₂,b₃) = b₁b₂b₃ − b₁ − b₃`.

## 1. Dictionary: X-slice certificates are HJ fractions of length 3 (PROVED, elementary)

**Lemma 1.1.** Let n ≥ 2. The map `(t,u,v) ↦ A = tu − 1` is a bijection
`{(t,u,v) ∈ ℤ³_{≥2} : tuv − u − v = n}  →  L₃(n) := {A ∈ (0,n) : gcd(A,n) = 1, r(n/A) = 3}`,
with `n/A = [[v,t,u]]`, `A* = tv − 1`, `AA* = tn + 1`.
*Proof.* `[[v,t,u]] = v − u/(tu−1) = (v(tu−1) − u)/(tu−1) = (tuv−u−v)/(tu−1)`, and numerator/denominator are
coprime (consecutive convergents of an HJ CF are coprime: the convergent matrices have determinant 1). HJ
expansions with all b_i ≥ 2 are unique (the first entry is `⌈n/A⌉`, A ↦ ⌈n/A⌉A − n is the HJ step), so every
A with r(n/A) = 3 arises exactly once. Finally `(tu−1)(tv−1) = t(tuv − u − v) + 1 = tn + 1`, and `tv−1 < n`. ∎

So `E(n) := {(t,u,v) : tuv − u − v = n}` (WINDMILL_REDUCTION §6, PARITY_FIXED_P (★)) is, up to the boundary
cases u = 1 or v = 1 (which are HJ length 2: `n/(t−1) = [[v,t−1]]`-type data, i.e. divisors of n+1), the set
of **length-3 HJ fractions with numerator n**, and `(t,u,v)` are their partial quotients (middle one = t).

**Corollary 1.2 (ES slices in HJ language).**
* (Type I, slice a = 1; CONDITIONAL_ES Lemma 1.1) If some `A ∈ L₃(p)` has `A ≡ 0 (mod 4)`, then ES(p):
  with `n/A = [[v,t,u]]`, `m = A = tu − 1`, `m'' = A* = tv − 1`, `4/p = 1/(bdp) + 1/(cd) + 1/(bcd)` with
  `(c,f,g) = (v,u,t)`, `d = A/4`, `b = (p+v)/u`.
* (Type II, (A)3: `4abc − a − b = p`) If some `A ∈ L₃(p)` has middle entry `t ≡ 0 (mod 4)`, then ES(p)
  (`4/p = 1/(abc) + 1/(acp) + 1/(bcp)` with `(a,b,c) = (u,v,t/4)`).
So, in the cleanest form: **ES(p) ⇐ some reduced fraction A/p with A ≡ 0 (4) has HJ length exactly 3.**
In toric language: the cyclic quotient singularity `1/p(1,A)` has a minimal resolution
with exactly three exceptional curves.

EVIDENCE/CERTIFIED (`scripts/dk_dict.py 3000`, exact rationals): Lemma 1.1 as a set identity, and (D2), (D3)
of §2, for all primes and odd squares ≤ 3000 (0 failures); at every odd square n ≤ 3000, no `A ∈ L₃(n)` has
`A ≡ 0 (4)` (T1 control, as it must by ET Prop 1.6).

## 2. Dedekind sums see exactly the alternating half of the CF (PROVED, classical + one-line consequence)

**(D2) Hirzebruch–Zagier / Myerson formula** (classical; Hirzebruch–Zagier, *The Atiyah–Singer theorem and
elementary number theory*, 1974 — cited from memory, verified numerically, `dk_dict.py`):
`12 s(A,n) = Σ_{i=1}^r (b_i − 3) + (A + A*)/n`.

**(D3) Corollary (PROVED).** Let `r = r(n/A)`, `r' = r(n/(n−A))`. Then
`r − r' = −12 s(A,n) − 1 + (A + A*)/n`.
*Proof.* Riemenschneider duality: `Σ_i (b_i − 2) = r' − 1`. Apply (D2) to A and to n − A (whose inverse is
n − A*, and s(n−A,n) = −s(A,n)), eliminate Σb'_j = (r − 1) + 2r'. ∎

On a certificate `n/A = [[v,t,u]]`: `12 s(A,n) = t + u + v − 9 + (A+A*)/n` and `r' = t + u + v − 5`.
So **the Dedekind sum s(A,n) determines r − r' (the alternating sum of regular partial quotients) but not r
itself**; "r = 3" is the condition that the *odd-indexed* regular partial quotients of n/A are all 1 except in
the pattern `[v−1; 1, t−2, 1, u−1]` (entries 2 in [[·]] merge into the 1-strings).
