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

### §2 "Consequence" — does the genus split evade CONDITIONAL_ES's square obstruction, or relocate it? — **SOUND as bookkeeping; the headline overstates what is gained (D1, MAJOR)**
What is true (re-derived): for the *same* count R the principal-character split R = M₀′ + X₀ has M₀′(m²) > 0 = R(m²),
so CONDITIONAL_ES Prop 3.1(3)'s obstruction has an exact analogue for R, and the order-≤2 split removes it: X(m²) = 0, so an
upper bound |X(n)| ≤ g(n) with g square-insensitive is not refuted by T1. (Note CONDITIONAL_ES Prop 3.1 is about a
*different* count, the Type-I slice S(p) of (3.1)–(3.2); the transfer to R is by analogy, which the document should say.)
What it does NOT do:
1. **The obstruction is relocated into (L), not removed.** Any split R = M + X with M ≥ 0, M(m²) = 0 has X(m²) = 0;
   the non-trivial part is that M_gen is explicit. The conditional target is now "(L) M_gen(p) ≥ g(p) AND (U) |X(p)| < g(p)"
   with the same g. (L) at the strength needed — g ≥ sup|X(p)|, which the document's own data put at sd(X) ≈ √(1.4–1.5·2M_gen)
   ≈ log p (my run: var(R − M_gen)/(2·mean M_gen) = 1.375 on [10⁵, 4·10⁵)) — is not reached by anything in the document:
   Prop 4.1 gives log log p (see D2).
2. **(U) is false at the known failures.** X(p) = −M_gen(p) at 409, 577, …, 329617 (M_gen/M₀ ∈ [0.57, 0.92]); my scan of all
   odd n ≤ 30001 finds 446 non-square n with R*(n) = 0 and M_gen(n) up to 11.5 (n = 17767; M₀ = 14.2) — i.e. X = −M_gen at
   Poisson-lower-tail points of every residue class except n ≡ 5 (8) (where the pair (1,2) always hits). So (U) is only
   meaningful asymptotically ("for all p > p₀") and is then exactly a Poisson-scale lower-tail statement: genus removes ≈ 27 %
   of the excess variance (my run: 1.880 → 1.375), leaving CONDITIONAL_ES Prop 3.1(2)'s "pointwise concentration at Poisson
   scale" requirement fully in place. The memo z30_genus_split says this ("only the square obstruction is relocated"); the
   SHARP headline in AGENT_REPORT_O260 and §0 bullet 2 should say it too.
3. No further structured (non-square) family with R* = 0 was found in n ≤ 30001 (zeros look like lower-tail events; 111 of
   the 306 non-square zeros in (5000, 30001] have a square factor, but none of the families k·m² is identically zero —
   e.g. n ≡ 5 (8) never vanishes). So I see no second "free" obstruction for X. EVIDENCE only.
