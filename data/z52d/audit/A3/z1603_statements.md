# Z1603 — draft ES-adjacent problem statements for an AI-math open-problem benchmark (audit A3; drafts only, NOT submitted)

Venue facts checked 2026-10-31: Epoch "FrontierMath: Open Problems" (https://epoch.ai/frontiermath/open-problems) takes
problems proposed by working mathematicians, reviewed by an editorial board (bar: "moderately interesting"), and needs a
bespoke *verifier program* — i.e. constructive/checkable answers. "FrontierMath Erdős" (68 Erdős problems, Lean-verified)
is a separate list. erdosproblems.com #242 forum: new comments suspended (repo record, BRAINSTORM/z52_lit_es_direct.md).
Submitting anything is an owner decision.

1. **(★)-failure beyond 10¹⁰ (constructive, expected YES).** Find a prime p ≡ 1 (mod 4), p > 10¹⁰, such that
   4uBC − u − B = p has no solution in positive integers. Known: exactly 14 such primes ≤ 10¹⁰ (409 … 8 813 281;
   FRONTIER §2.1, B1_LINE.md §3.6). Verifier: trial form R(p) = Σ_{4uC−1 ≤ p+u} 1[(4uC − 1) | p + u],
   ≈ (p/4) log p divisibility tests (≈ 6·10¹¹ at p = 10¹¹: hours in C, fine for a verifier, too slow for Python).
   Notability: low–moderate (calibrates the (★) zero law; not ES).
2. **PM-II counterexample (constructive, expected NO beyond 3361).** Find a prime p ≠ 3361 with no prime-modulus Type II
   certificate (BRAINSTORM/y3_primemod_census; exhaustive to 10⁸). Verifier: Type II divisor search restricted to prime
   moduli. Notability: low.
3. **Thin family 15·2^s + 1 (proof, Lean).** Prove 4/n = 1/x + 1/y + 1/z is solvable for every n = 15·2^s + 1
   (FRONTIER §7.8; 3·2^s + 1, 7·4^s + 9, 63·2^s + 1 are proved in the repo; no finite ET covering exists).
   Verifier: Lean statement (modelled on FormalConjectures ErdosProblems/242.lean). Notability: moderate at best.
