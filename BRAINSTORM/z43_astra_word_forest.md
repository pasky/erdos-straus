# z43 Astra — the word forest as a deterministic construction target

**Checkpoint O275. No ES existence theorem.** Full proofs and exact scopes: `LOWER_TAIL_ASTRA.md` §§2–5.

## SHARP dictionary

Positive words `tuv−u−v=n`, modulo u↔v and with loops removed, form a forest on endpoint integers: at v the only possible smaller neighbour is `−n mod v`. On unit vertices its edge sign is the product of the two vertex Jacobi symbols. A good word is therefore a bichromatic edge (n≡1 mod4). Increasing branches satisfy a continued-fraction recurrence `v_next=a v+v_prev`.

This is not the old signed-solution graph: vertices here are endpoint integers of positive words; no signed denominator is involved. Novelty beyond the repository was not investigated.

## Construction and repair

1. Explore the component of 1 until it reaches a non-residue. **Fails:** 285 primes p≡1 (4)≤10^6. Four simultaneous linear primes give an explicitly closed eight-vertex residue tree; Dickson makes infinitely many.
2. Allow finitely many starting roots and arbitrary exploration depth. **Fails conditionally:** the n=1 shadow isolates every root 4,…,H, while roots 1,2,3 remain in the closed eight-vertex tree.
3. Replace fixed roots by the least non-residue. **Fails:** at p=2521 it is 11 and isolated. The pair of prime forms `p=2521+9240a`, `(p+11)/12=211+770a` makes this an infinite counterfamily under Dickson.
4. Force a sign change by long paths. **Fails in that scope:** CRT and Dirichlet produce arbitrarily long all-residue paths. This does not assert their whole components are monochromatic.

## Remaining constructive questions

- Can an independently defined *growing* root set be proved to meet a mixed component? Minimum mixed root ≤17 in the census is only EVIDENCE, not a suggested bounded-root conjecture (the fixed-root obstruction contradicts that under Dickson).
- The numerical quantity to study is the least root of a mixed component, not the least good endpoint: root descent may drastically reduce the search. There is no bound yet.
- Adding another incidence relation (for example sharing the level t) creates a different graph. Any resulting cycle argument must use an actual arithmetic constraint absent from this forest, rather than reintroducing a count estimate.
- An inverse theorem for simultaneous monochromatic components would be genuinely new. Independent per-level factorisation assumptions do not supply one.

The stopped real-quadratic-cycle lane was not executed at this checkpoint. The continued-fraction recurrence here is elementary and does not by itself connect a branch to the reduction cycle of Q(√p).
