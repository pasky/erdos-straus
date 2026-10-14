# y2 — Friezes over ℤ/4, ℤ/8 and the lifting problem: the Farey complex F₄ is blind, T1 is the only local obstruction (O210)

Labels as in DISCOVERIES.md. **ES is not solved.** Notation as in FRIEZE_ES.md.

## Idea
Short–Van Son–Zabolotskii (SVZ) model friezes over ℤ/n by closed paths in the Farey complex F_n, i.e. unimodular pairs
mod n up to ±1, with edges where det ≡ ±1. Their Thm 1.6: a tame semiregular frieze over ℤ/n lifts to a tame frieze
over ℤ of the same width iff its path is *strongly contractible* (spur removals and triangle shortcuts only).
Hope: the ES sign of a pentagon frieze at N ≡ ±1 (4) is the strong-contractibility class of its mod-4 walk. Then
"(A/N) = −1 ⟺ the mod-4 frieze lifts to a classical Conway–Coxeter pentagon" would be a topological theorem, and
the lifting theory might force existence.

**Dictionary (PROVED, elementary).** F₄ is the octahedron: 6 vertices, antipodal pairs {(1,0),(1,2)}, {(0,1),(2,1)},
{(1,1),(1,3)}, and its 8 faces are the Farey triangles mod Γ(4). For N ≡ ±1 (4) the pentagon's path
V₁…V₅ closes mod 4 to a 5-walk, because the N-side becomes an edge. At vertex i:
* q_i ≡ 0 (4) ⟺ the walk has a **spur** (V_{i−1} ≡ ±V_{i+1});
* q_i ≡ 2 (4) ⟺ the two neighbours are **antipodal**;
* q_i odd ⟺ the two neighbours are adjacent (a triangle corner).

So (J)9 / FRIEZE_ES Cor 1.3 reads: **(h′/N) = −1 ⟺ the mod-4 walk of the pentagon has a spur.** If it has no spur,
the walk is a 5-cycle of the octahedron with two consecutive antipodal corners (the even edge, both ≡ 2 mod 4).

## Iteration (barrier as steering wheel)
1. **Killed: the topological class is not the sign.** Every closed walk of odd length ≤ 7 on F₄ is strongly
   contractible: 960/960 closed 5-walks and 16 128/16 128 closed 7-walks. Even lengths have exceptions (264/288 for
   4-walks: the equator). So every pentagon frieze mod 4 lifts to a tame integral frieze of width 2, and SVZ's
   obstruction is blind to the ES sign. On actual words (`y2_f4_walks.py 120 6`), HJ lengths 2, 4, 6 show
   non-contractible walks, but these are uncorrelated with (A/N).
   Hypothesis violated by the hope: SVZ lift to **unit** boundary. The ES sign lives in lifts with a **fixed
   non-unit** boundary entry N, and it is a reciprocity invariant, not a homotopy invariant.
2. **Modification: lifting with prescribed coefficient.** Let A₈(N) be the mod-8 frieze classes with boundary
   (1,1,1,1,N mod 8), i.e. triples (c, m, s) mod 8 with K ≡ N (8); there are 80 for each odd N mod 8. Let R₈(N) be the
   set of classes realized by positive integral friezes at N.
   * The only *local* obstruction is T1: at N = M², the classes with 8 | ee′ are never realized (FRIEZE_ES Cor 1.4).
     These are exactly the walks with a spur.
   * EVIDENCE (`y2_lift8.py`): for odd non-square N ∈ (10⁴, 2·10⁴], every one of the 4 × 80 (N mod 8, class) pairs is
     realized with positive frequency. The minimum is 0.136, for (7,7,7) at N ≡ 1 (8), formal words. For interior words
     the minimum is 0.083, for (1,1,1) at N ≡ 7 (8).
     No hidden obstruction mod 8 appears beyond T1. But at most N with N ≤ 2·10⁴ some class is missing: about 100 words
     have to land in 80 classes, a coupon-collector lottery.
3. **Conclusion.** "Lift a spur-walk mod 4 to a positive frieze at N" is exactly SQ₅/(S) ((J)15). The finite-ring
   theory supplies the classes and their local admissibility, and nothing forces a lift. Counts of tame friezes
   over ℤ/p^r (Böhmler–Cuntz) count classes, i.e. A₈. Every such count is N-independent apart from N mod 8, so it
   cannot see T1 (B5).

## Literature
* I. Short, M. Van Son, A. Zabolotskii, *Frieze patterns and Farey complexes*, arXiv:2312.12953 (Adv. Math. 2025).
  Thm 1.6 (lifting ⟺ strongly contractible) and the definitions were read in the PDF (§1, lines on F₄'s
  non-contractible 4-path 0/1 → 1/1 → 2/1 → 3/1 → 0/1).
* B. Böhmler, M. Cuntz, *Frieze patterns over finite commutative local rings*, arXiv:2407.12596 (counts over ℤ/p^r;
  abstract verified).
* S. Morier-Genoud, *Counting Coxeter's friezes over a finite field via moduli spaces*, Alg. Comb. 4 (2021) (abstract seen).

## Barrier screen
* B5/T1: the pentagon has exactly one local (mod-8) obstruction, the square case. A finite-ring frieze theory is
  N-blind beyond N mod 8, so it can never prove existence at primes while failing at squares.
* B1: realizing a fixed mod-8 class at all N would be a congruence covering. It fails at squares by T1.
* B2: a lift means choosing an unknown λ-length; the class fixes only its residue.

## Cheap numerics
`scripts/y2_f4_walks.py` (walk census, word census to N ≤ 400 for r = 3 and N ≤ 120 for r ≤ 6) and
`scripts/y2_lift8.py` (R₈ census and class rates). Outputs are quoted above.

## Assessment
NEGATIVE (PROVED for the F₄ blindness; EVIDENCE for "no hidden mod-8 obstruction"). The SVZ lifting theory concerns
unit boundary and is blind to the ES sign. With coefficient N the lifting problem is (S)/SQ₅, a lottery per class.
Promise 0/5 as a route; the spur/antipode dictionary is a useful picture.
