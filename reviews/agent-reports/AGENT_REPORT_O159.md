# AGENT_REPORT_O159 — two-variable binary-form identity certificates (branch side-agent/binaryform-identities)

Target: `POINTWISE_BINARYFORM.md`. Scripts: `scripts/bf_lemma11_check.py`, `scripts/bf_reach_check.py`,
`scripts/bf_search_typeI.py`. Data: `data/bf/`.

**Outcome: obstruction theorem, unconditional, any degree (POINTWISE_BINARYFORM Thm 3.2, Cor 3.4).**
Let F be ET Type I/II coordinates (a,…,f) that are polynomials (or rational functions) in (u,v), with
n = Q(u,v) and Q positive definite. Take any coset C mod M (8, 2D, the denominators | M) with Q(C)
a square unit mod M. Then F is valid there only near finitely many directions. So every finite set of
"Fermat + identity" certificates misses almost all primes of every square class, in particular
infinitely many Mordell-hard primes. Ingredients:
1. Lemma 1.1: ET Prop 1.6 reproved for bare N-points, with no gcd(c, n) condition (needed because
   specialised polynomial families need not keep coprimality). Checked on 36k small N-points.
2. Lemma 2.1: `Q(u,v) = w²` is a conic with a rational point (Hasse–Minkowski), so weak
   approximation puts odd squares in every square-class coset and every open sector. For u² + v²,
   "square class" equals the trivial class of `(Z[i]/M)*/((Z/M)*·⟨i⟩·squares)` (Lemma 2.2, brute
   force checked for 11 moduli; note M = 4 is NOT enough, 8 | M is needed). This is the
   two-variable class of one; no Hypothesis H is needed because the square points are genuine.
3. Lemma 3.1 (top forms fix signs away from finitely many directions) plus Lemma 3.3 (non-polynomial
   rational coordinates are integral on ≪ X^{1+ε} points).
4. Cor 3.4 uses Hecke's equidistribution of prime ideals in sectors and ray classes, cited not
   reproved.

Structure (question (1)): Prop 5.1 shows constant-level families are one-variable for every form
(n² + 4c²d is irreducible over Q). Prop 5.2 shows Type II families valid on a cone are one-variable
(O145 Prop 3.2 on lines + reflection invariance ⇒ O_Q-invariant). Search (§6): 0 genuinely
two-variable Type I families for u² + v² with c const or affine-linear and deg d ≤ 2 (small
coefficients); the positive control rediscovers O145's k = 21 family. Families on non-square classes
exist trivially (one-variable identities composed with Q), so "positive proportion of a Mordell-hard
class mod 840" is the wrong target. The correct statement is per square class mod the joint modulus.

Honest scope / please check:
* Novelty: folklore-level two-variable analogue of Mordell–Schinzel; no literature search done.
* Not covered: indefinite forms in cusp regions (§4.3, open); families given only as (x,y,z) ∈ Q[u,v]³
  (§4.4(iv)); procedures with floor/factorisation (needs a two-variable Theorem C); unbounded
  families of forms.
* Prop 5.2 relies on O145 Prop 3.2 (brainstorm-level, unreviewed).
* Engineering: the first search version had a sympy `solve` bug (dropped κ-only equations); it was
  caught by the built-in ET-equation assertion and fixed by an explicit check. The square-class
  audit is skipped for M > 1500 (never triggered for u² + v²).
