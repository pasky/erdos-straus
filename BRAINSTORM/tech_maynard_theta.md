# Maynard–Tao sieve with θ as the averaging variable, p fixed (O155)

Status: brainstorm memo, internal. **Verdict: COLLAPSES**, to B3 at the step "error ≤ main term" and to
H-A at the step "first-moment asymptotic over θ". The structural analogy is spurious for one precise reason
(Remark 1.2).

## 1. Idea

Maynard (2015) and Tao (Polymath 8b) prove that for an admissible k-tuple, infinitely many n have at least m
primes among n + h_1, …, n + h_k. The proof uses weights w(n) = (Σ_{d_i | n+h_i} λ_{d_1…d_k})² over n ~ N.
Bombieri–Vinogradov evaluates S₀ = Σ w(n) and S₁ = Σ w(n) Σ_i 1_P(n+h_i) asymptotically, and then
S₁ − (m−1)S₀ > 0 forces at least m primes.

For ES at a *fixed* prime p, the variable n is replaced by the slice parameter θ. The cleanest family is the (A)3
subsystem:

  R(p) = #{(A,B,C) ≥ 1 : 4ABC = p + A + B} ≥ 1  ⇒  ES(p).

**Lemma 1.1 (PROVED, elementary; dual forms).** The following three counts are equal for every prime p:

  R(p) = #{(A,C) : (4AC − 1) | p + A} = #{(A,C) : (4AC − 1) | 4Cp + 1}.

*Proof.* Given (A,C), put B = (p+A)/(4AC−1). Then p + A + B = 4ABC, and conversely. Since
gcd(4AC−1, 4C) = 1 and 4C(p+A) = (4Cp+1) + (4AC−1), the two divisibilities are equivalent. ∎

The second form is the brief's divisor form with t = 4C: we need m = 4AC − 1 ≡ −1 (mod 4C) to divide tp + 1.
The first form says p ≡ −A (mod q) for some q = 4AC − 1, i.e. p lies in a "forced class" (B2).

So θ = A, or θ = (A,C), is a free averaging variable at fixed p. This is *not* a T7 leak (redteam-2 H-B makes
the same point). The question is whether a Maynard-type weighted first or second moment over θ can be
evaluated at one p.

**Remark 1.2 (why the analogy is spurious).** ES needs *one* success, i.e. m = 1. For m = 1 the
Maynard–Tao criterion S₁ − 0·S₀ > 0 says only that w is positive somewhere on the success set. The
multidimensional optimisation of λ (the whole content of Maynard–Tao: the ratio log k/k) is irrelevant, since
it improves the ratio S₁/S₀, which only matters when m ≥ 2. The prime analogue of m = 1 is the prime
number theorem for n + h₁, which needs no Maynard. So the transfer reduces exactly to: **give an asymptotic,
or just a positive lower bound, for a (possibly weighted) first moment Σ_θ w(θ)·1[θ succeeds] at one p.**
That is redteam-2 hatch H-A, and it is where it fails (§3).

## 2. Literature anchor

* J. Maynard, *Small gaps between primes*, Ann. of Math. 181 (2015) 383–413. D.H.J. Polymath, *Variants of
  the Selberg sieve, and bounded intervals containing many primes*, Res. Math. Sci. 1 (2014) 12.
  (Standard; from memory.)
* J. Maynard, *Dense clusters of primes in subsets*, Compositio Math. 152 (2016) 1517–1554 (from memory,
  unverified page numbers). It proves the sieve for a general set 𝒜 of integers satisfying (i) a level of
  distribution in arithmetic progressions, (ii) Siegel–Walfisz-type uniformity, and (iii) a density
  hypothesis: 𝒜 ∩ [x,2x] has ≥ x/(log x)^{O(1)} elements. Hypothesis (iii) is what fails here.
* ET (Elsholtz–Tao 2013) evaluate Σ_{p≤N} f_II(p) ≍ N log³ N by averaging over p. This is the T7 version of
  the same first moment.

## 3. Barrier screen

**The 1/|θ| law (heuristic; EVIDENCE in §4).**
* For A ~ H, the event (4AC−1) | p + A has probability ≈ 1/(4AC−1) for each C ≤ (p+A)/(4A).
* So the expected number of successes in the block A ∈ [H,2H) is ≈ Σ_{A~H} log(p/A²)/(4A) ≈
  (log 2/4)·log(p/H²).
* That is O(log p) for **every** H, however large the block. The total over H ≤ √p is ≍ log²p.

Consequences for each Maynard input:

* **Density hypothesis (iii).** The success set in a θ-range of size X has ≍ log p·log X elements, so its
  density is X^{−1+o(1)}, not (log X)^{−O(1)}. Hypothesis (iii) fails for every X ≥ (log p)^{C}.
* **B3 (scale), the failing step.** Any level-of-distribution input in θ (Bombieri–Vinogradov,
  Zhang-type, or a Weyl/exponent-pair bound for Σ_A over p + A in progressions mod 4A) has error ≥ X^{1−δ}.
  The main term is ≤ log p·log X. So "error ≤ main term" forces X ≤ (log p)^{O(1/δ)}. In that range θ ranges
  over a polylog-sized set, which is exactly the regime of CONDITIONAL_ES Prop 2.3 (main term M ≤ p^{o(1)}
  with bounded multiplicity). No power-saving technology exists there.
* **Weights (B4).** Maynard's λ_d impose divisibility d | N_θ(p). At fixed p these are congruence conditions
  on θ (CRT). They concentrate w on a set of θ of relative measure 1/M while raising the per-θ success
  probability by at most the divisor-multiplicity factor (≤ 3^{ω(M)}).
  * Mass is conserved up to that factor, as measured in §4 (gain 1.5–2.6 against a cost of M).
  * Deterministic versions of the same idea are LONGSHOT_PIGEONHOLE Thm 2.2 (B4).
* **B1.** The weights and the main term are CRT data, so this is Thm M/Prop A territory unless the error
  term carries non-congruence information.
* **B2.** Each θ is one slice event, so the method is "aggregate over a growing family", i.e. H-A.
  Thm 2.2(iii) excludes finitely many θ. A growing family is not excluded, but it has no technology (above).
* **B5/T1.** R(m²) = 0 for odd m, because the (A)3 system is Type II and f_II(m²) = 0. The genus-blind main term
  (log 2/4)·Σ log(p/H²) is positive at n = m² too. So **the asymptotic "Σ_θ = main + o(main)" is the step
  that is false at odd squares**. A correct version must carry a genus/character term that cancels the
  main term exactly at squares (cf. the Eisenstein genus pairing, (I)4). Maynard's sieve has no such term,
  because primes have no genus.
* **B6/T7.** None at fixed p if θ is the variable. If one instead averages over p (the natural Maynard setup,
  n := p), one gets exceptional-set statements, where (D)18/(D)24 cap CRT-sieve savings at (log N)^{3/4}.
* **T2 (integrality).** Every block has main term O(log p), with no block > log p. The total mass log²p is
  spread across ≍ log p blocks of size O(log p), consistent with H-A's "≍ 𝓛³ blocks of O(1)" for the full
  Type II family.

## 4. Experiment (`scripts/bs_tech_maynard_theta.py`; ~1 min)

The first 6 primes p ≡ 1 (mod 24) above 10⁹ (p mod 840 ∈ {169, 193, 457, 481, 673, 73}; 169 is a square
class), A < 2¹⁵, winners per dyadic block k = 0..14:

| p mod 840 | R_X | per-block winners |
|---|---|---|
| 169 | 46 | 0 6 4 3 4 4 0 4 4 1 4 3 5 3 1 |
| 193 | 37 | 2 3 4 2 4 4 2 5 2 0 5 0 3 1 0 |
| 457 | 44 | 4 6 1 5 5 3 1 2 2 2 4 2 2 4 1 |
| 481 | 70 | 4 10 9 3 5 3 4 5 4 5 6 2 1 4 5 |
| 673 | 37 | 2 4 5 1 3 3 4 3 2 1 0 2 2 0 5 |
| 73  | 57 | 0 16 3 6 4 6 4 1 2 1 4 3 1 3 3 |

* The blocks are flat, at O(1)–O(log p). The predicted (log 2/4)·log(p/4^k) runs from 3.6 to 1.8, which
  is consistent within the noise.
* Zero blocks occur, so no single dyadic block is reliable.

*Maynard-weight test.* Restrict to A ≡ −p (mod M), A < 2¹⁸, so that M | p + A, summed over the 6 primes. The
total mass up to 2¹⁸ is extrapolated as ≈ 349 from flat blocks.

| M | weighted mass | fair share mass/M | gain |
|---|---|---|---|
| 5 | 105 | 69.8 | 1.50 |
| 15 | 60 | 23.3 | 2.58 |
| 105 | 5 | 3.3 | 1.5 |

The weights cost a factor M and give back only O(1)·(small factor)^{ω(M)}. The weighted family carries
*less* total mass, which is the expected B4 behaviour.

## 5. Viability Assessment

**COLLAPSES**: to B3 at "error ≤ main term" (the density hypothesis (iii) fails), and in reduced form
(Remark 1.2) to H-A, the open first-moment problem at fixed p. The genuinely Maynard part (multidimensional
weights) is irrelevant for m = 1.

*By-products:*
* Lemma 1.1, the three dual forms of the (A)3 system. PROVED, elementary, and essentially folklore: it is
  ET's Type II divisor form restated.
* The m = 1 remark, which is the precise reason the "some of many N_θ" analogy does not transfer.
* EVIDENCE for the flat per-block law with the predicted constant (log 2/4)·log(p/H²).

*What would revive it:* a second-moment or bilinear identity in θ at fixed p whose main term contains the
genus factor (vanishing at squares). That is H-A/H-B, with no technology known.
