# BRAINSTORM (O146 a): forced joint factorisation across slices (hatch H-A)

Status: brainstorm memo. **ES is not solved here.** Labels as in DISCOVERIES.md.

Notation. For any integer n ≥ 2 let `V_I(n) = {4abd = ne+1, a+b = ce}`, `V_II(n) = {4abd = n+e, a+b = ce}`
(all coordinates ≥ 1), `V(n) = V_I(n) ∪ V_II(n)`. Every element gives an ES solution of 4/n
(`(abdn, acd, bcd)`, resp. `(abd, acdn, bcdn)`; one-line check as in redteam-2 §2.0), and for odd prime p,
ES(p) ⟺ V(p) ≠ ∅. Slices θ and integers `N_θ(n)` as in redteam-automorphic-2 Lemma 2.1.

## 1. Idea

At fixed p the slice integers are values of binary quadratic forms in the slice parameters, and composition
relates them. Two exact identities (PROVED, verified symbolically with sympy):

* (C1) `(p + 4a²d)(p + 4b²d) = (p + 4abd)² + 4dp(a − b)²` — two II{a,d} integers (values of `pX² + 4dY²`,
  disc −16dp) multiply to a value of the principal form `X² + 4dp Y²`, whose value at `(1, c)` is the II{c,d}
  integer `4c²dp + 1`.
* (C2) `(p + 4a²d)(4c²dp + 1) = p(4acd − 1)² + 4d(cp + a)²` — ties the rows II{a,d}, II{c,d}, II{a,c}
  (`cp + a`) together, with the common divisor candidate `f = 4acd − 1` appearing explicitly.

The hope (brief, angle (a)): such relations might make "every slice of a family Θ(p) is empty" an
*inconsistent* set of factorisation constraints, i.e. emptiness of many slices would force some integer to
have an impossible factorisation.

What would have to be true: an implication "all slices θ ∈ Θ(p) empty ⇒ contradiction", proved from the
relations among the `N_θ(p)`.

## 2. Literature anchor

* ET Prop 1.6 (Elsholtz–Tao, `sources/elsholtz-tao-1107.1010.pdf`, p. 6, checked): f_I(n) = f_II(n) = 0 for
  every odd perfect square n; ET's remark right after it: any method proving f_I(p) or f_II(p) > 0 "must
  necessarily fail when p is replaced by an odd square". ET p. 5: for composite n most solutions are of
  neither type.
* Composition / Brahmagupta identities: classical (Gauss composition).
* I found no statement in the literature about which **non-square** n have V(n) = ∅ (one web search; ET
  re-read; novelty of §4 below not verified).

## 3. Barrier screen

**Prop 3.1 (T1 transfer; PROVED, elementary).** Let R be any family of relations among the integers
`(N_θ(n))_θ` that holds for **every** integer n ≥ 2 (polynomial identities in ℤ[n, θ] such as (C1)–(C2),
composition laws, the bijections of Lemma 2.1 wherever they are proved for general n, local data
`n mod q` computed from n). Then "R holds and every slice is empty" is consistent: it is realised by every
odd square n = m² (ET Prop 1.6). Hence no argument whose only inputs are R together with
"all slices of Θ(n) are empty" can reach a contradiction.

*Proof.* At n = m² every relation in R holds (it holds for all n) and V(m²) = ∅, so every slice is empty. ∎

So a forced-correlation argument must contain a step that is false at odd squares (B5), i.e. it must use
a property of p that squares lack. The minimal such property is the non-principality of the Jacobi
character `χ_n = (·/n)` (all the vanishing at squares comes from reciprocity, ET §4). This turns the
"forcing" question into an exact question, which the experiment of §4 answers empirically.

* B1: the relations in (C1)–(C2) are identities; any "forcing" through finitely many of them at fixed
  parameters is a fixed finite slice set ⇒ Thm 2.2(iii) (CONDITIONAL on H).
* B2: (C1)/(C2) only re-encode the obvious fact that one solution lies in several slices (the same
  `f = 4acd − 1` divides `p + 4a²d`, `cp + a` and `4c²dp + 1`; for the last, `a²(4c²dp + 1) ≡ a(cp + a) (mod f)`
  and `gcd(a, f) = 1`). Products of slice integers are values of forms at points **off** the slice lines
  (`X = p + 4abd ≠ 1`). So no new divisor events are created; the relations give correlations between
  events, never an implication from emptiness to non-emptiness.
* B3/B4/B6: not engaged (no counting).
* T1: answered by Prop 3.1. Squares are where the forcing must fail.

## 4. Experiment: which n have V(n) = ∅? (`scripts/bs_corr_vempty.c`, `scripts/bs_corr_vempty_check.py`, `logs/bs_corr_vempty_1e6.txt`)

Exhaustive decision of V(n) = ∅ (with a ≤ b; bounds `4a²d ≤ n + 2a` (II) and `4acd ≤ 2n + 2` (I), derived from
`e ≤ a + b ≤ 2b`, `c ≤ 2b`), every candidate verified on the defining equations. An independent naive
Python enumeration agrees on 2 ≤ n ≤ 400.

**EVIDENCE.** For 2 ≤ n ≤ 10⁶: V(n) = ∅ exactly for the perfect squares (odd **and** even) and for the two
even non-squares n = 288 = 2⁵·3², 336 = 2⁴·3·7. **Every odd non-square n ≤ 10⁶ has V(n) ≠ ∅.** Extension (odd n only): all 4 498 919 odd non-squares
in (10⁶, 10⁷] have V(n) ≠ ∅ (`logs/bs_corr_vempty_odd_1e7.txt`).

Exact counts f = #V(n) (a ≤ b) for all odd n in [10⁵, 3·10⁵] (`scripts/bs_corr_count.c`,
`scripts/bs_corr_nearsq.py`, `logs/bs_corr_nearsq.txt`):

| class | min f/log³n | mean f/log³n |
|---|---|---|
| primes | 0.032 (n = 115201, f = 51) | 0.20 |
| odd non-squares, all | 0.0089 (n = 111969 = 3³·11·13·29, f = 14) | 0.11–0.16 by squarefree-part bin |
| "near squares" n = s·m², 2 ≤ s ≤ 30 (385 n) | 0.032 | 0.11 |
| odd squares | 0 | 0 |

The smallest non-square counts are composites with small prime factors (3, 5, 7), not near-squares: the
count does not degrade as n approaches a square in the sense s(n) → small.

**CONJECTURE SQ.** For odd n > 1: V(n) = ∅ ⟺ n is a perfect square. (EVIDENCE: all odd n ≤ 10⁷.)
SQ implies ES for primes, and it is exactly the statement "genus (reciprocity at squares) is the only way all
slices can be jointly empty".

## 5. Viability Assessment

**COLLAPSES to B5 (T1) at the "forcing" step, leaving PARTIAL (a sharp reformulation).**
* Relations among the N_θ cannot force anything by themselves (Prop 3.1): the all-empty pattern is
  consistent with every identity in n, and is realised at squares.
* The data say the only realised all-empty patterns (odd n ≤ 10⁶) are the squares. So the minimal honest
  version of H-A is SQ: "non-principal χ_n forces a non-empty slice". It is stronger than ES and uniform in n.
  Primality plays no visible role: odd composites behave like primes, with somewhat smaller constants.
* SQ is not easier than ES. By Thm C-type arguments (square-mimicking n), any proof through fixed finite
  slice sets fails for SQ too, so a proof of SQ is still a growing-family (H-A) argument.
  Positive point: SQ removes the temptation to use primality, so it identifies what any proof must "see":
  only the character χ_n. Possible use: test proposed H-A mechanisms on composite non-squares and on
  near-squares s·m², where the genus character is a fixed small-conductor character; an argument that
  needs primality beyond non-squareness is suspicious (EVIDENCE says it is unnecessary).
* By-products: Prop 3.1 (PROVED, trivial); identities (C1), (C2) (PROVED); SQ (CONJECTURE, EVIDENCE for odd n ≤
  10⁷); the even exceptions 288, 336 (CERTIFIED by two independent enumerations at n ≤ 400 and the C
  enumeration to 10⁶).
