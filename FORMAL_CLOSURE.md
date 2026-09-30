# Formal closure of the seed component (running status)

Status file for the "does the Theorem-2 closure stabilize?" task. Labels:
PROVED / CONDITIONAL / EVIDENCE.

## 0. Running log

* (start) Analysis of the accidental-prime gap (§1 below); new engine
  `scripts/formal2.py` being written.
* formal2.py (python-flint) reproduces the old engine exactly (B=200 seed 1:
  734/4162/4460 vertices after rounds 2-4; it1 model point, B=1500: 7807
  vertices, 13359 polys, 1775 r-primes) in 35 s instead of ~30 min.
* Iteration (model point of it1, LAM = primes<=1500): iter0: 816 r-primes fail
  the counting certificate; explicit fragile analysis leaves 50 obstacles
  (25 primes 1511..2053 where the roots of S (incl. aux) cover all residues,
  11 fragile-dense r-primes 2089..26729, 14 C3 primes). Obstacles added to LAM
  with a QR residue minimising damage. iter1: 7883 vertices, 13521 polys,
  2 obstacles (1831, 1759). iter2 running.
* Plan for the final certificate: make every r-prime a model prime (residue
  = generic rho for explicit ones, random S-root-avoiding for the others) and
  recompute the closure *exactly* at the model point; then every decision is
  a numeric test at one integer qv with post hoc precision, no genericity.

## 1. Analysis (what exactly must be certified)

Notation of DEPTH3 §3. Fix a finite set `S` of primitive irreducible
`g∈Z[X]` (lc>0, `X,P∈S`), a finite set of primes `Λ`, exponents `E_ℓ`, and a
class `q0 mod M=∏ℓ^{E_ℓ}`. Put `C_g=∏_{ℓ∈Λ}ℓ^{v_ℓ(g(q0))}` (need
`v_ℓ(g(q0))<E_ℓ`). **Admissible** q: `q≡q0 (M)`, `r_g=g(q)/C_g` prime,
pairwise distinct, `∉Λ`, q large.

Key observation. At admissible q, for a prime `ℓ∉Λ`, `ℓ∤g(q)` for every
`g∈S` (since `g(q)=C_g r_g`). Hence the ℓ-adic valuation of every formal
number is that of its rational constant, for **every** prime, in Λ or not.
Consequently:

1. Primes of constants need **not** be in Λ for the fibre computation to be
   exact, *provided every polynomial whose value enters an integrality
   decision is in S*. The prior agent's parallel driver did not put the
   factors of `D+s` of *rejected* candidates into S; for a rejected
   candidate whose only failure is at a prime `ℓ∉Λ` of `const(r)`, the
   decision depends on `q mod ℓ` ("fragile" candidate). This is the real
   gap. Fix: either put the factors into S, or put ℓ into Λ with a residue
   `ρ_ℓ` avoiding the roots mod ℓ of every `g∈S` (so no `C_g` changes) and of
   the primitive part of every fragile `D+s`. For large ℓ this is a counting
   argument; for small ℓ an explicit check.
2. Characters are not needed for the final conclusion: at large admissible q
   the sign of a formal number is the sign of its constant, so
   nonpositivity of every formal vertex can be checked directly. (2a) then
   gives consistency checks only.
3. Hypothesis H needs no fixed prime divisor: for `ℓ∈Λ` automatic from
   `E_ℓ>v_ℓ(g(q0))`; for `ℓ∉Λ` it is "some residue mod ℓ avoids the roots of
   all g∈S", automatic for `ℓ>Σdeg`.
4. Robust rejection of a candidate D at every admissible q: failure of
   `g^β | D+s` in `Q[X]` for some g in r (resultant argument, q large), or a
   failure at a prime of Λ decided exactly at precision `E_ℓ`. Non-robust
   (fragile) rejections are recorded with their witness prime and polynomial.
