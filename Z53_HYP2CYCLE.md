# Z53_HYP2CYCLE — depth lane HYP2CYCLE: 2-cycles of the remainder map in the balanced block (FRONTIER §7.1, R2)

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only.

Brief: `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z53_lanes.md` §HYP2CYCLE. Scripts `scripts/z53_hyp2cycle_*`, data
`data/z53/hyp2cycle/`.

**Status: CHECKPOINT 1** (skeleton; sections marked TODO are being filled).

## 1. Statements attacked

Notation (as in `Z52D_HYPERBOLA.md` §§2–3). n odd ≥ 5, U ≥ 1 an integer with 2U < n. For x ∈ (U, 2U] let f(x) be the
unique y ∈ (U, 2U] with y ≡ −n (mod x), or ⊥. A *2-cycle* is an unordered pair {u, B} ⊂ (U, 2U] with f(u) = B, f(B) = u
and uB | n + u + B (the last is automatic at primes, Z52D Prop 2(b)); its *level* is k := (n + u + B)/(uB).

* N₂(n, U) := #2-cycles (the "no 4-condition" count).
* N₄(n, U) := #2-cycles with 4 | k. By Z52D Prop 2, the balanced-block (★) count is N(U, U) = 2N₄(p, U).
* N₅(n, U) := #2-cycles in some five-slice (4 | k, u, B, ku − 1 or kB − 1).

**(R2) [target, FRONTIER §7.1 / Z52D (R2)].** There is η > 0 such that N₄(p, U) ≪ U^{1−η} for all primes p and
U ≍ p^{1/4}. **(R2′)** The same for N₂. (R2′) ⟹ (R2). Trivial bound: N₄ ≤ N₂ ≤ U/2 (Z52D Thm 1(a)).

Also attacked (kickoff): an exact identity turning 2-cycle counts into a boundable sum; a CERTIFIED falsifier; whether N₂
is bounded better than N₄; where the 4-condition enters.

## 2. Why this is not already closed

Z52D closed, as scoped theorems, (i) one-step dualization at fixed conductor, (ii) Erdős–Turán/Fejér with max |S_h|,
(iii) Cauchy–Schwarz in the function variable, (iv) low-conductor/class-conditioned main terms. All four are
*cancellation* implementations on the additive-character side. R2 is an *upper-bound counting* statement. It can be
attacked by (a) algebraic counting (determinant method on the cubic surface kuB − u − B = p; Z52D's (R3), "not
attempted"), (b) the dynamics of f (functional-graph / continued-fraction structure), (c) structural identities (level,
strip, fixed-difference forms). None of these is covered by the closed list or by FRONTIER §6.

## 3. First results (checkpoint 1)

**Lemma A (level form; PROVED).** Let 4U < k for every level in range (true in the balanced block once n ≥ 2^16 with
U = ⌊n^{1/4}⌋, since k ≥ n/(4U²) − 1). Then {u, B} ↦ k is injective, and
N₂(n, U) = #{k : s_k := (−n mod k) ∈ (2U, 4U], D_k := s_k² − 4(n + s_k)/k = w² for an integer w ≥ 1 with
(s_k ± w)/2 ∈ (U, 2U]}, and N₄ is the sub-count with 4 | k.
*Proof.* kuB = n + s with s = u + B ∈ (2U, 4U], so s ≡ −n (mod k), and s < k forces s = s_k. Then uB = (n + s_k)/k and
u, B are the roots of X² − s_kX + uB, whose discriminant is D_k = (B − u)². Conversely such k, w give the pair. u ≠ B
since u = B would give u | n with 1 < u < n... (n prime; for composite n the diagonal is excluded by w ≥ 1). ∎

**Lemma B (where the 4-condition enters; PROVED).** For a 2-cycle at a prime p: if u, B are both odd then k is odd; if
u = 2^a u′ (a ≥ 1, u′ and B odd) then 4 | k ⟺ B ≡ −(p + u) (mod 2^{a+2}), while the 2-cycle condition alone gives only
B ≡ −p (mod 2^a). So the 4-condition is exactly *two extra 2-adic bits on the even vertex*, and (★)-pairs are the
"mixed 2-cycles" u ↦ g(u) := (−(p + u) mod 4u, lifted into (U, 2U]) ↦ f(g(u)) = u.
*Proof.* gcd(u, B) = 1 (Z52D Prop 2(b)). If both odd, uB and p + u + B are odd. If u is even: 4uB | p + u + B ⟺
4u | p + u + B and B | p + u + B (coprime moduli) ⟺ B ≡ −(p + u) (mod 4u) and f(B) = u; and mod u the first is
B ≡ −p, i.e. B = f(u). The 2-part of the extra condition is the class of B mod 2^{a+2}. ∎

**First falsifier (EVIDENCE / CERTIFIED counts; `scripts/z53_hyp2cycle_scan.c`, `…_maxsearch.c`, validated against an
independent O(U²) brute force `…_brute.py` on all odd n ≤ 30 000 × 4 choices of U: 59 959 cases, 0 mismatches).**

* *Exhaustive scan of all primes 5 ≤ p < 4·10⁹ (U = ⌊p^{1/4}⌋ ≤ 251; 189 961 813 primes):* max N₂ = 7, max N₄ = 5.
  Histograms (p ∈ [10⁹, 4·10⁹), 1.39·10⁸ primes): N₂ = 0…7: 96 507 873 / 35 491 903 / 6 319 531 / 729 037 / 61 590 /
  4 132 / 199 / 13. All odd composites ≤ 10⁸: max N₂ = 6. No route to a power-size count is visible; the tail is
  Poisson-like (TODO: fit).
* *Layer means (U = ⌊p^{1/4}⌋):*

| sample | E N₂ | E N₅ | E N₄ | E[k ≡ 2 (4)] | E[u+B odd] | P(N₂>0) | P(N₄>0) |
|---|---|---|---|---|---|---|---|
| 2·10⁵ primes from 10⁸ | 0.3647 | 0.2737 | 0.0732 | 0.0730 | 0.2918 | 0.309 | 0.070 |
| 10⁵ primes from 10¹² | 0.3664 | 0.2755 | 0.0749 | 0.0722 | 0.2928 | 0.308 | 0.072 |
| 2·10⁴ primes from 10¹⁶ | 0.3636 | 0.2706 | 0.0722 | 0.0751 | 0.2923 | 0.305 | 0.070 |
| 10⁴ primes from 10¹⁸ | 0.3545 | 0.2635 | 0.0690 | 0.0739 | 0.2885 | 0.296 | 0.066 |
| 10⁵ odd squares m², m ≈ 10⁶ | 0.1507 | 0 | 0 | 0.0612 | 0.1203 | 0.140 | 0 |
| 10⁵ random odd n ≈ 10¹² | 0.2981 | 0.2236 | 0.0594 | 0.0605 | 0.2378 | 0.257 | 0.057 |

  * N₄/N₂ ≈ 1/5 and N₅/N₂ ≈ 3/4 at primes, flat from 10⁸ to 10¹⁸ (TODO: exact CRT-model constants).
  * At p ≡ 1 (4): N₅ = #bichromatic 2-cycles exactly (0 exceptions in 1.5·10⁵ primes; LOWER_TAIL_ASTRA Lemma 2.2 + the
    five-slice sign theorem). At p ≡ 3 (4): N₅ = #monochromatic (TODO: check status in repo).
  * **T1 sits in the five-slice layer, not in the 2-cycle count:** at odd squares N₂ > 0 for 14.0 % of n, while
    N₄ = N₅ = 0 identically. So any *lower* bound for N₂ (no 4-condition) is T1-blind and useless for ES; for *upper*
    bounds the 4-condition is a bounded thinning (N₄ ≤ N₂).

**First no-go (PROVED modulo the cited statement; details §5 TODO).** Heath-Brown's affine determinant method (CIME
notes Thm 15, as restated in Reuss's thesis Thm 2 and Browning–Heath-Brown Math. Z. 2005 eq. (3)) applied to
F = kuB − u − B − p in any box u ≤ B₁, B ≤ B₂, k ≤ B₃ produces ≫ exp(2√(Π log B_i / log T)) ≥ min(B_i)^{2/√3}
auxiliary polynomials (T = B₁B₂B₃), more than the trivial bound min(B_i)·p^{o(1)}. So route (R3) in its standard form is
vacuous in every block.

## 4. TODO (rest of the lane)
* CRT/random-map model constants for E N₂, E N₄, E N₃ (3-cycles of f); Poisson fits; joint independence.
* Controls: FRONTIER §4 item-14 test primes; near-squares p = m² ± r.
* Dynamics/CF section: what fixed-p Gauss-map/transfer analysis can see (cylinders = intervals; termination = divisor
  event; prefix × suffix = modular hyperbola).
* Full proof of the determinant-method no-go; other models.
* Verdict, screens, §7 text, review.
