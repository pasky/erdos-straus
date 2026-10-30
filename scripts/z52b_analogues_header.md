# z52b lane `analogues` — analogue-world mining for Erdős–Straus (ES is OPEN)

Data: `data/z52b/analogues.jsonl`. This file is generated from the jsonl by `scripts/z52b_analogues_build.py`, which reads the
batch files `scripts/z52b_analogues_b01.py … b09.py`. Nothing here proves ES or any infinite case of it. Per the brief this is a
breadth-first list. The only filter is an obvious-nonsense filter, and items were not graded against the barrier checklist.

## Summary

* **362 items** in 9 worlds (sections A–I below). Confidence-not-nonsense: high 131, med 160, low 71. Effort: cheap 294,
  medium 67, big 1. 717 distinct free-form tags; 51 items carry a `seen:<file>` tag.
* **Tag histogram (top 30):** function-field 53, constraint-world 29, literature 25, data 22, new-world 21, sibling-problem 19,
  computation 18, real-quadratic 15, T1 14, Gaussian 14, reformulation 14, polynomial-ring 13, boundary-marker 12, S-integers 12,
  calibration 8, topology 8, context 8, closed 8, numerator-spectrum 7, units 7, 2-adic 7, logic 7, finite-field 6,
  classification 6, quaternion 6, matrices 6, k-terms 6, signed-ES 5, dictionary 5, squares 5. The full histogram is in the
  auto-generated statistics below.
* **New small computations (all cheap, scripts committed):**
  - The *constraint-world census*. For every prime p ≡ 1 (mod 4) below 2·10⁴ (1125 primes), all solutions were enumerated
    (`scripts/z52b_analogues_constraints*.py`; failure lists in `data/z52b/analogues_constraints_fails_20000.json`,
    `…constraints4_fails_8000.json`).
  - The Z[1/ℓ] unit-mechanism check (`scripts/z52b_analogues_zl.py`).
  - A weighted-ES check (`scripts/z52b_analogues_weighted.py`).
* **Corrections made during generation.** These are the obvious-nonsense filter at work. They are recorded as items so that
  nobody repeats the mistakes:
  - S-integer relaxations collapse. Denominators in (1/ℓ)ℕ make ES trivial whenever ES(ℓ) holds. One non-integral denominator
    always suffices: 4/p = 1/(p/3) + 1/(2p) + 1/(2p). So the "ℓ-depth" and "smooth-numerator" hierarchies I first wrote down are
    empty (items 0053, 0074, 0055, 0096). The only S-integer content that does not depend on ES itself is the unit-sum
    *mechanism*.
  - Two guesses about the failure sets of constrained worlds were checked against the data. The guess for the norm world was
    refuted (0217). The guess for the chain world was confirmed, with a sharper statement (0218).

### The 10 items I find most exciting

1. **0109 / 0110 / 0214 — a 2-adic coincidence.** Restrict to solutions with all denominators even (⇔ 8/p is a 3-term sum), or
   to solutions with some denominator ≡ 0 (mod 4). Each constrained world fails at **exactly {17, 241}** among the 1125 primes
   p ≡ 1 (mod 4) below 2·10⁴. Possible structural content: a 2-adic bijection, and a Schinzel m = 8 strengthening of ES that
   appears to have only finitely many exceptions.
2. **0113 — near-complete sub-world.** Solutions with z = lcm(x, y, z) exist for every such prime below 2·10⁴ except
   **2521 = lcm(1..10) + 1**. This is a rich sub-family and a candidate proof target.
3. **0218 — miniature Mordell/T1 model.** Restrict to chain solutions x | y | z. Every one of the 161 failures is ≡ 1 (mod 24),
   the square class mod 24. Inside that class, 161 of the 267 primes fail. Proving that chain identities cover
   p ≢ 1 (mod 24) is a finite-covering exercise. The residual class is a lottery world with real, observable failures.
4. **0107 — numerator-spectrum reformulation.** M(p) = {m : m/p is a 3-term sum} is closed under divisors. So ES ⇔ M(p) contains
   *some* multiple of 4. The literature gives |M(p)| ≍ polylog on average (Luca–Pappalardi; Mond–Portier). A forced large
   numerator ≡ 0 (mod 4) would prove ES.
5. **0201 / 0358 — hard primes look like squares.** The constrained-world failures cluster at p with very smooth p − 1
   (241, 601, 1801, 2521). Such p are square-like modulo many M, which is exactly where T1 empties the certificate lines. The
   proposal is a T1-depth invariant D(p), to be correlated with #ES(p).
6. **0258 — a proved world attached to p.** For p ≡ 1 (mod 4), Q(√p) has a unit of norm −1. So positive ES for 4/p holds over
   O_{Q(√p)} by the N(ε) = −1 mechanism, with a unit built from Pell solutions. Trace descent of this solution is an explicit
   integer experiment.
7. **0052 / 0074 — the S-integer picture, finished.** Positive ES over Z[1/ℓ] holds for every odd prime ℓ checked (ℓ < 3000),
   via e | 1 + ℓ^k with k ≤ 7. The relaxations themselves collapse, which isolates the integer target: a p-tied surrogate η(p)
   for the unit (0338).
8. **0219 — Borwein–Choi.** N = xy + yz + zx, the same symmetric form as ES's pretzel determinant 4xyz/n, is a sibling solved
   with class numbers (complete up to one possible GRH exception). Their form correspondence might be extended to track xyz.
9. **0155 / 0156 — singularity theory as a host world.** ES ⇔ 4/n is the log canonical threshold of a Brieskorn–Pham polynomial
   x^a + y^b + z^c. The other quasi-homogeneous (Arnold / Orlik–Wagreich) types give a family of geometrically natural
   "generalized Egyptian" relaxations to test.
10. **0337 / 0017 / 0191 — transfer and negative transfer.**
    - From the FF density-zero theorem: under GRH, the ES exceptional set should have a power saving. A conditional result of
      this shape was not found in the literature.
    - From Mordell–Schinzel: ES is false over Z[T] with eventual positivity. Hence ES may be unprovable in open induction, and
      every proof must be non-uniform in n.

### Per-world map: step that works → integer-side replacement → nearest literature

| World | Status there | Step that works | Integer statement that would replace it | Nearest literature / repo |
|---|---|---|---|---|
| F₂[T] (A = T²), F₄[T] (A = T) | PROVED (finite covering) | char-2 cancellation, no square-class obstruction | finite *signed* covering plus a positivity-repair lemma (0002, 0339) | FUNCTIONFIELD_ES §6 |
| F₉, F₂₇ … | no finite linear covering (PROVED) | — (behaves like Z) | Mordell (known) | FF_ODD_ABSENCE |
| fixed q, deg P → ∞ | density-zero failures (PROVED) | one-prime identity + RH in F_q[T] | GRH ⇒ power-saving exceptional set (0003, 0337) | FUNCTIONFIELD_ES §5; Vaughan |
| q → ∞, fixed degree | FALSE for most P | — | large numerators fail (A₃(p) polylog) (0004) | Luca–Pappalardi; Mond–Portier |
| F_q[T] with free leading coefficients | exceptions = squares exactly (q large) | Weil sum over q − 1 unit shifts | cancellation over a p-tied family of shifts (0300) | EXSET_FUNCTION_FIELD §1.3 |
| one mute place (FF) | PROVED for all P | Bilharz (FF Artin) | Z[1/ℓ] unit mechanism (elementary) (0299, 0052) | FF_MUTE Thm 3.5 |
| Z[1/ℓ], Z[1/p] | PROVED (trivially, and also via units) | e \| 1 + ℓ^k; or depth-1 identity | p-tied surrogate η(p) with e \| 1 + η(p) (0338); relaxations collapse (0053, 0074, 0096) | other_rings Prop 3.2 |
| O_K, N(ε) = −1; Q(√p) | PROVED | η ≡ −1 mod an inert ℓ ≡ 3 (4) | same surrogate; trace descent to numerator 8 (0056, 0057, 0258) | other_rings Prop 3.3 |
| Gaussian / imaginary-quadratic cones | OPEN | — | twin of ES; ladder (1+i)^k (0059, 0332) | Bradford–Ionascu |
| Z[T] (lc > 0) | FALSE at square classes | — | non-uniformity filter (0017, 0340) | Mordell–Schinzel |
| constrained ℕ-worlds | some FALSE, some apparently complete | — | strengthenings: 8/p, lcm = z, pure Type II (0109, 0113, 0204) | this lane's data |
| k ≥ 4 terms, signed, weighted | easy / trivial | extra term, sign, or numerator | merging lemma (0312); signed + repair (0310, 0339) | Elsholtz–Planitzer |
| matrices, quaternions | relaxations / reformulations | non-diagonal freedom | projection gives weighted ES (easy) (0069, 0315) | QUATERNION_ES |
| triangle orbifolds, Seifert, LCT, Dynkin T_{x,y,z}, resistors, AP packings | reformulations | — | invariants of solutions (H₁, det, Dedekind sums) | this lane, items D |

## Method and coverage

* **Generation.** I took the worlds named in the brief one at a time (F_q[T], other rings, numerators, k terms, signed,
  p-adic/adelic, matrices, Z[T], Gaussian/Eisenstein, quaternions, finite fields, ultraproducts, tropical, S-integers,
  constrained ES, other numerators). For each world I wrote down three things: what is proved there, the step that does the
  work, and the integer statement that would replace that step. I then invented further host worlds where 1/x + 1/y + 1/z
  appears natively:
  - geometry and topology: triangle orbifolds, Seifert spaces, pretzel links, Brieskorn singularities and lcts, Dynkin stars,
    dessins;
  - combinatorics and physics: resistor networks, tilings, perfectly periodic schedules and AP packings, codes;
  - logic and probability: weak arithmetic, Beurling integers, random thinning;
  - deformations: q-deformations, dual numbers, categorified N[T], cone families inside Z[√2].

  Two further sources of items:
  - Sibling Diophantine problems with known status, mined for "the step that works there".
  - The repo's FF memos (FF_MUTE, EXSET_FUNCTION_FIELD, FF_ODD_ABSENCE), mined as transfer seeds.
* **Literature.** Every cited arXiv id was checked against the arXiv API: 1405.4025, 1107.1010, 1908.02526, 1905.06151,
  2201.11805, 1111.2574, 2303.15685, 2305.16518, 2112.03726, math/0311421, 2404.07113, 2404.16016, math/0411305, 1606.02117,
  1108.6118, 2507.03727, 2012.05984, 1805.02945, 2305.02689, 2606.15159, 2412.09728, 2410.24165, 1412.3263, 1012.0814,
  2605.23011, 2606.27104, and others in refs. The following were checked by web search: Guerrieri–Loper–Oman; Borwein–Choi
  (Exp. Math. 2000); Haag–Kertzer–Rickards–Stange (Annals 2024); Graham 1964 (PJM); Erdős problem #242; Pomerance's notes
  stating Sierpiński 5/n was verified to 10¹⁸. Unverified leads appear only as "check whether …" in `first_step`. Examples are
  Niederreiter's FF Zaremba, Bourgain–Garaev, Keating–Rudnick, Bank–Bary-Soroker–Rosenzweig, Sawin–Shusterman, W. Chen, and
  Breusch/Stewart.
* **Not done.**
  - No item was graded against the barrier checklist (as the brief instructs).
  - The `seen:` tags are incomplete: only memos I knew of or grepped quickly are tagged.
  - The constraint census stops at 2·10⁴ (8·10³ for the second batch of constraints).
  - The FF experiments proposed in sections A and H (sign-subgroup cones, A irreducible vs reducible, 4-term FF coverings) were
    not run.
  - The Z[√2] four-cone experiment, the Gaussian (1+i)^k ladder and the trace descent in Q(√p) were not run.
  - The Borwein–Choi correspondence and the quasi-homogeneous lct relaxations were not worked out.
