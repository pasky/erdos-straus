# R277 — hostile review of SINGLE_P_COUNT.md (O260, route (a): counting at one prime)

Reviewer: R277 side agent. Scope: SINGLE_P_COUNT.md as merged from `side-agent/single-p-count`, memos BRAINSTORM/z30_*,
scripts/z30_*, logs/z30_*. From-scratch checks: `scripts/review_r277_*.py` / `.c` (none of the author's code reused).

(work in progress — filled in claim by claim)

## Claim-by-claim verdicts

### Lemma 1.1 (three exact forms of (★); PROVED) — **SOUND**
Re-derived. (1) gcd(u,B) | p and gcd = p is size-excluded; (2) (4uC−1)(4BC−1) = 4C(4uBC−u−B)+1, cofactor ≡ −1 (mod 4C)
since d·d′ ≡ 1, d ≡ −1; swap is fixed-point-free (u = B ⟹ u | p ⟹ 4C − 2 = p, impossible); (3) direct matrix product.
From scratch (`scripts/review_r277_exact.py`, part A): triple count = pair form = divisor form (both halves) = SL₂ form
(enumerating a ≡ −1 (mod c) divisors of cp+1) = R* (coprime, u+B odd), and R(p) even, for every prime p < 300: 0 mismatches.

### Lemma 2.1 (genus split; PROVED) — **SOUND** (it is an identity; the content is the definition of M_gen)
Re-derived: for gcd(n,q) = 1, Σ_{χ²=1} χ(n)χ̄(a) = |G/G²|·1[na ∈ G²]; X is *defined* as the complement, so R* = M_gen + X
is tautological once the real-character sum is evaluated. No convergence/truncation issue: 𝒫(n) is finite and each pair
expansion is a finite orthogonality relation. From scratch (part B): for every odd n < 1600, M_gen computed three ways —
(i) definition with s(q) = |units|/|squares| and membership in a brute-force square set, (ii) Prop 2.2(a)'s explicit
Legendre/mod-8 form, (iii) Σ_{pairs} φ(q)^{−1} Σ_{χ real} χ(n)χ(a) with the real characters enumerated by brute force as
homomorphisms (ℤ/q)^× → {±1} — agree exactly in ℚ; also #real chars = |G/G²| = 4·2^{ω_odd(uB)} for every q met.
An independent C engine (`scripts/review_r277_count.c`) reproduces R* and M_gen of the Python code on all odd n < 1600.

### Prop 2.2 (PROVED) — **SOUND** (two MINOR wording points, D7–D8 below)
(a) re-derived (2-part: na ≡ 1 (8) ⟺ n ≡ a (8); odd ℓ | u: a ≡ −B). Exact check: see Lemma 2.1, (ii) = (i).
(b) re-derived: na ∈ G² ⟹ a ≡ x² (q) ⟹ x² + u = B(4uC′ − 1) with f = 4uC′ − 1 ≡ −1 (4u), f | x² + u, contradicting
PARITY_AUDIT Lemma 3.2 (I re-checked that lemma's proof: every prime ℓ ∤ 2u of x² + u has (−u/ℓ) = 1, while χ_{−4u}(f) = −1).
Exact: R* = M_gen = X = 0 at all odd squares 9 … 1521 (part B, in ℚ) and, by the C engine, at all 86 odd squares ≤ 30001.
(c) correct (any lift y of z). (d) re-derived and checked exactly for all 54 admissible pairs with u, B ≤ 11 (part D).
