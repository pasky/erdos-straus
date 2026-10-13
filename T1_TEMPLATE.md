# T1_TEMPLATE — T1-bearing Erdős–Straus variants that can be proved at primes (task O183, spark relay J)

Status: in progress (O183). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on TWISTED_T1.md (O182, CLAIMED, under review R182), DRINFELD_ES.md, KUDLA_ES.md §1. Scripts `scripts/t1t_*`,
memos `BRAINSTORM/bsJ_*.md`.

## 0. Plan and iteration log

Goal: a variant V(n) (Egyptian-fraction type, over some ring, with a normalisation) such that
(i) V has an anchor+partner obstruction: no Type I/II-shaped solution at k-th powers (a T1), yet
(ii) V(p) is PROVABLY solvable at every prime p.
Its proof is then a mechanism that provably evades B5 — a template for ES.

(J1) Heuristic steer. ES's anchor is the real place (positivity), which (a) pins inv_∞ = ½ and (b) makes every
attached quadratic object *definite* (KUDLA §1: B_T definite), hence class sets finite, hence the search bounded
and the lottery (B1–B3). Moving the anchor to a FINITE place (congruence normalisation) frees the real place:
attached objects become indefinite, strong approximation becomes available, and the search is unbounded. The
hope: in such a variant, existence of Type I/II solutions is governed by local conditions + the T1 Brauer class
ONLY (strong approximation with Brauer–Manin, Colliot-Thélène–Xu style), so primes are provably solvable while
squares are provably obstructed.

(J2) Over ℚ, swap the roles (anchor 2 by congruence normalisation, partner ∞ by a sign pattern):
`V_{t,M}(n): t/n = 1/x + 1/y − 1/z, x, y, z > 0, x ≡ y ≡ 1, z ≡ −1 (mod M)` (`scripts/t1t_swap.py`, complete
enumeration). EVIDENCE: for t = 3, M = 4 the invariants are inv₂ = ½, inv_∞ = 0, inv_q = ½ (q | n) on every solution,
and odd squares 9, 25, 49, 121 have only "other"-shape solutions — a T1 with anchor and partner swapped. But the
search is still finite (x < 2n/t: one real place, and it is pinned), and V_{3,4} already fails at the primes 13, 17,
37, 41, 89, 97 (complete search). Hypothesis of B1–B3 still satisfied: *finite search at fixed n*. Over ℚ a
2-torsion T1 needs ∞ pinned (inv_∞ is free otherwise), so the search is always finite. Modification: go to a field
with TWO real places, pin one (anchor) and put a sign pattern on the other (partner); the unit group of infinite
order then makes the search infinite while keeping the T1 (§1).
