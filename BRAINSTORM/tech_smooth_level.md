# Smooth-moduli level of distribution (Zhang / Polymath 8a, BFI) for ES witness moduli (O155)

Status: brainstorm memo, internal. **Verdict: COLLAPSES.** Pointwise it is a T7/B6 leak. For exceptional sets
it changes only the constant, not the exponent 3/4, by the campaign's CRT-majorant cap.

## 1. Idea

By Lemma 1.1 of `tech_maynard_theta.md`, the (A)3 system at p reads: p ≡ −A (mod q) for some q = 4AC − 1,
with p ≥ q − A. Type II and Type I have the same shape: p lies in a "forced class" a_q mod q whose modulus can
be chosen freely among many q. Zhang's theorem, and Polymath 8a's, extends Bombieri–Vinogradov beyond
x^{1/2} for x^{δ}-smooth (densely divisible) moduli. Bombieri–Friedlander–Iwaniec go beyond 1/2 for a
*fixed* residue with well-factorable weights.

*Hope.*
* (a) Pointwise: no route is visible.
* (b) Exceptional set: restrict the witness family to smooth q, which loses little, and use the larger
  level to beat E(N) ≪ N exp(−c(log N)^{3/4}) ((B)11).
* (c) Bilinear structure: the factorisation of q into smooth pieces could give a Type I/II
  (bilinear) decomposition at fixed p.

## 2. Literature anchor (from memory, standard)

* Y. Zhang, *Bounded gaps between primes*, Ann. of Math. 179 (2014) 1121–1174.
* D.H.J. Polymath, *New equidistribution estimates of Zhang type*, Algebra & Number Theory 8 (2014)
  2067–2199.
* Bombieri–Friedlander–Iwaniec, *Primes in arithmetic progressions to large moduli I–III*, Acta Math. 156
  (1986) etc.

All three are statements Σ_{q} |π(x;q,a_q) − π(x)/φ(q)|. The **primes up to x are the averaged variable**, and
q is averaged as well. In Zhang/Polymath the residues a_q must come from a fixed integer a, or a coherent
CRT family, for the dispersion method. The ES forced classes −A mod 4AC − 1 are coherent only within a
fixed (A,C) structure (from memory; not re-verified for ES-shaped residue systems).

## 3. Barrier screen

* **(a) B6/T7, the failing step.** At fixed p the quantity π(x;q,a_q) becomes 1[p ≡ a_q (mod q)], a single
  lottery event per q. A level-of-distribution statement over p carries no information at one p. "Average
  over q at fixed p" is H-A: the 1/|θ| law gives mass ≍ log²p over all q, against the error of any
  equidistribution statement in q.
* **(b) B1 and the (D) caps.** Counting the avoider primes p ≤ N via a majorant built from forced classes
  is a CRT-majorant argument.
  * (D)24 (EXCEPTIONAL_KARY3 Thm 4.1, Cor 4.2) gives log(1/Eν) ≤ Cλ^{3/4} for a majorant of level λ. Here
    λ is a log scale: classes of modulus ≤ N^A give λ ≤ A·log N.
  * (D)22 gives the same cap for prime-only majorants, and (D)19 caps large sieves.
  * Level beyond 1/2 raises the admissible A from 1/2 to 1/2 + ϖ. That changes only the constant c in
    exp(−c(log N)^{3/4}). The exponent 3/4 is structural (mass/dimension: the cubic mass B = 3 gives
    B/(B+1), (D)2), not a level-of-distribution artefact.
  * Smoothness of q is irrelevant to the caps, which hold "with arbitrary moduli and no B-hypothesis"
    ((D)24).
  * Beating 3/4 needs correlation input of growing order, TC_θ ((D)21), which is not a
    level-of-distribution statement.
* **(c) Bilinear structure at fixed p.** A factorisation q = q₁q₂ with both factors smooth gives
  p ≡ a_q (mod q₁) and (mod q₂). These are two lottery events, still at fixed p. There is no sum over p to
  apply dispersion to. Collapses to H-B (no long sums; O(1) mass per dyadic block).
* **B5/T1.** At n = m², every forced class misses n (Mordell/Jacobi: the classes contain no squares,
  (D)13). A level-of-distribution statement over primes is true but silent at squares, which are not
  prime. The step that would be false at squares is again "main term ⇒ some q hits", made pointwise.
* **B2.** Each q is one slice event (Thm 2.2). **B3** applies to any pointwise use. **B4**: restricting to
  smooth q is a congruence-type restriction, with no gain.

## 4. Experiment (`scripts/bs_tech_smooth_level.py`, N = 10⁶, 18 s)

This measures how many primes p ≡ 1 (mod 24), p ≤ 10⁶, are covered by the (A)3 system when the witness modulus
q = 4AC − 1 is restricted to be N^β-smooth (9732 primes in total).

| moduli allowed | uncovered | fraction |
|---|---|---|
| all | 9 | 0.0009 |
| P⁺(q) ≤ N^{1/2} | 10 | 0.0010 |
| P⁺(q) ≤ N^{0.4} | 25 | 0.0026 |
| P⁺(q) ≤ N^{0.3} | 250 | 0.026 |
| P⁺(q) ≤ N^{1/4} | 713 | 0.073 |
| P⁺(q) ≤ N^{0.2} | 2324 | 0.239 |

* Smooth witness moduli carry most of the mass for moderate β (EVIDENCE: the restriction (b) is cheap).
* At Zhang-type smoothness (β ≈ 1/100 or less, Polymath's δ) almost nothing is covered at this height.
* Neither fact matters, by the cap in §3(b).
* (The 9 uncovered primes reflect the (A)3 subsystem's own failures, not ES failures: ES holds for all
  these p.)

## 5. Viability Assessment

**COLLAPSES**: to B6/T7 pointwise, at the step "level of distribution over primes ⇒ one prime". For the
exceptional set it collapses to the (D)24 cap: the level enters only through λ ≤ A log N, so it changes the
constant and not the 3/4 exponent. No new partial theorem results.

*By-product (EVIDENCE):* the (A)3 subsystem with N^{0.4}-smooth moduli covers all but 25 of the 9732 primes
p ≡ 1 (24) up to 10⁶.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (§0.2, §0.3 and the
per-memo paragraph). Counterexamples, where computational, re-verified by `scripts/errata_check.py` (tag in brackets).

* **§2 conflates two estimates:** BFI's well-factorable *weighted* estimate is not the same absolute-discrepancy sum
  as Zhang's smooth-moduli estimate.
* §3(c) "no sum over p": this does not exclude bilinear summation over witness parameters at fixed p; small expected
  success mass does not eliminate long ambient sums (H-B). Smoothness is not B4's transparent-coset-covering
  hypothesis. EXCEPTIONAL_KARY3 Thm 4.1 / Cor 4.2 and EXCEPTIONAL_PRIMELAW Cor 4.2 have specific majorant
  hypotheses; they are not universal prohibitions on signed dispersion. **Corrected verdict:** PARTIAL → H-B.
