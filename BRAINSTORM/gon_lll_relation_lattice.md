# Brainstorm O148(b): lattice reduction (LLL / Coppersmith / Lenstra) and the relation-lattice (matroid) view

ES is not solved; nothing here proves any case of it. Labels as in DISCOVERIES.md.

## 1. Idea

Two ways lattice reduction could enter a pointwise proof:
(b1) **Coppersmith/Lenstra as a proof device.** B2 says every encoding reduces to "N_θ(p) has a divisor in a
residue class r mod s". This is *exactly* the problem of Lenstra's "Divisors in residue classes" and its LLL
version (Coppersmith–Howgrave-Graham–Nagaraj, CHN). Could the lattice that finds such divisors also certify
that one exists?
(b2) **Relation lattice / matroid view of an e-slice.** By LONGSHOT_PIGEONHOLE Lemma 1.1, Type T(p) holds in the
slice e iff −1 ∈ Σ_e(N) = {∏ ℓ^{t_ℓ} mod e : |t_ℓ| ≤ v_ℓ(N)}, N = N_e^T(p). Let ℓ₁,…,ℓ_k be the primes of N,
H_e = ⟨ℓ_i mod e⟩ ≤ G_e = (ℤ/e)^*, and L_e = {t ∈ ℤᵏ : ∏ℓ_i^{t_i} ≡ 1 (e)} the **relation lattice**
(covolume |H_e|). Then (exact restatement, PROVED from Lemma 1.1):

> **ES slice ⟺ the coset t₀ + L_e meets the box B_N = ∏[−v_i, v_i]**, where t₀ is any exponent vector with
> ∏ℓ_i^{t₀,i} ≡ −1 (e); the coset exists iff −1 ∈ H_e.

So the slice splits into a *linear-algebra half* (−1 ∈ H_e: a subgroup-membership / binary-matroid rank question,
decided by characters) and a *geometry-of-numbers half* (an inhomogeneous box problem / CVP in ℓ^∞ for L_e).
The hope: the first half is "genus-like" and might be provable for every p; the second is a covering-radius
question where GoN (Minkowski's second theorem, Kannan–Lovász μ ≤ ½Σλ_i, transference) gives sufficient criteria.

## 2. Literature anchor

* H. W. Lenstra Jr., *Divisors in residue classes*, Math. Comp. 42 (1984) 331–340 (verified via the Leiden PDF
  abstract): if s > n^{1/3}, gcd(r,s) = 1, at most 11 divisors of n are ≡ r (mod s), found in polynomial time.
* D. Coppersmith, N. Howgrave-Graham, S. V. Nagaraj, *Divisors in residue classes, constructively*, Math. Comp. 77
  (2008) 531–545 (IACR ePrint 2004/339; existence of the paper verified, the formulae in the abstract did not
  render): explicit LLL construction; extends to s ≥ n^{α}, α > 1/4, with a bound depending on α − 1/4
  (exponent details from memory, unverified). A 2026 J. Number Theory follow-up "Divisors in residue classes
  revisited" exists (search hit only, not read).
* Kannan–Lovász (Ann. Math. 128 (1988)): covering radius μ(L,K) ≤ ½ Σ λ_i(L,K) for symmetric convex K; and the
  trivial volume bound μ(L,K)ᵏ·vol K ≥ covol L. Banaszczyk transference (from memory).

## 3. Barrier screen

**(b1) Coppersmith/Lenstra: an enumeration device only.** Coppersmith's method builds, from the shifts
x^j N^{m−i} f(x)^i, a lattice whose short vector is a polynomial h with h(x₀) = 0 *over ℤ for every small modular
root x₀*. The implication runs one way (root ⇒ root of h). A short vector exists in *every* such lattice
(Minkowski), including at n = m² and including for classes with no divisor, so its existence carries no
information on whether a root exists. Lenstra's 11 and CHN's bounds are **upper bounds** (multiplicity ≤ O(1)
per (c,d)-slice once the modulus 4cd exceeds N^{1/3}, e.g. Type II needs 16cd² ≳ p). This fits B3/Prop 2.3
(bounded multiplicity) and does not help existence. As an algorithm it is irrelevant here: ES(p) for a given p is
easy to find by direct search. **Collapses at the step "short vector ⇒ root" (false direction).**

**(b2) Relation lattice.** Screen of the two halves.
* *Linear-algebra half is solved for primes and fails at odd squares (PROVED, elementary).*
  (i) If n = m² (odd, gcd(m,e) = 1) then H_e ⊂ K_e = ker χ_{−e} ∌ −1 (LONGSHOT_PIGEONHOLE Lemma 1.2(iii): every
  ℓ | N lies in K_e). So **the membership step is the step that is FALSE at odd squares (B5)**.
  (ii) If e = q is prime (q ≡ 3 (4)), G_q is cyclic and −1 ∈ H_q ⟺ |H_q| even ⟺ some ℓ | N is a non-square
  mod q ⟺ (Lemma 1.2(i)) some ℓ | N has (ℓ/p) = −1. For Type II with (q/p) = −1 this holds automatically
  (χ_{−q}(N) = (q/p) = −1, Lemma 1.2(ii)). By Dirichlet (CRT on the two characters χ_{−4} and (·/p)) such primes q exist,
  so for every prime p ≡ 1 (4) *some* Type II slice passes the linear-algebra half. (For the slice to be
  non-vacuous one also wants q ≤ (p+4)/3; the least such q is a least-non-residue-type quantity, ≪ (log p)² under
  GRH; an unconditional q < p/3 for all large p needs a Linnik/Burgess bound for primes in a coset of an index-4
  subgroup mod 4p — from memory, not checked. Numerically the membership half holds for ≈ half of all e.) Checked numerically
  (assertion in the script for every prime e ≤ 3000 and 8 primes near 10⁸).
  So the genus/matroid half of ES is a theorem; all difficulty sits in the box.
* *GoN half = the lottery (B2/B4).* The box has 3^{ω(N)}…τ(N²) lattice points, the coset has density 1/|H_e|.
  Volume bound: covering needs τ(N²) ≳ |H_e|, and |H_e| is typically ≍ φ(e) (the primes of N generate most of
  G_e). Kannan–Lovász needs Σλ_i ≤ 2 in the box norm, impossible when N is squarefree and k ≥ 3 (every nonzero
  integer vector has sup-norm ≥ 1, so λ_i ≥ 1). A deterministic covering criterion therefore needs ω(N) ≳ log₃ e,
  which is LONGSHOT_PIGEONHOLE Lemma 2.1/Thm 2.2 (B4). A probabilistic hit has chance ≈ τ(N²)/|H_e| per slice,
  Σ_e over slices ≍ log³p: ET's mass, i.e. B2's polylog lottery. Which coset point is hit depends on the discrete
  logs of the large prime factors of N — the lottery H-A/H-B.
* *B1:* the membership half uses only characters (congruence data) and is uniform — fine, it is already proved.
  The box half is exactly what Theorems M/C forbid deciding from congruence data.
* *B3:* main term τ(N²)/|H_e| ≤ p^{o(1)} per slice — allowed, but only as an expectation.
* *B6:* none (pointwise).

## 4. Experiment (`scripts/bs_gon_relation.py`, < 10 s)

8 hard primes p ≈ 10⁸ (p ≡ 1 (24), square class mod 840), slices e ≤ 3000; counts [slices, −1 ∈ H_e, −1 ∈ Σ_e]:

| e ≤ | Type I | Type II |
|---|---|---|
| 30 | 56, 30, 25 | 56, 35, 29 |
| 100 | 144, 58, 33 | 144, 101, 59 |
| 300 | 400, 186, 61 | 400, 241, 74 |
| 1000 | 1400, 633, 120 | 1400, 850, 118 |
| 3000 | 4000, 1743, 107 | 4000, 2291, 91 |

The membership half holds in a stable ≈ 45–60 % of slices at every scale; the box half (given membership) decays
from ≈ 85 % (e ≤ 30) to ≈ 5 % (1000 < e ≤ 3000), as τ(N²)/|H_e| predicts. Odd squares m² ≈ 10⁶
(6 controls): 0 slices pass membership, as (i) says. EVIDENCE only.

## 5. Viability Assessment

(b1) **COLLAPSES** at "short vector ⇒ root": LLL/Coppersmith certify *non-existence beyond a list*, never
existence; Lenstra/CHN give multiplicity upper bounds only.
(b2) **PARTIAL (sharp reformulation, not ES).** ES(p) ⟺ for some e, an explicit coset of the relation lattice
L_e meets the exponent box B_N. The coset's existence (the matroid/genus half) is PROVED for every prime p and is
precisely the step that fails at odd squares; what remains is an ℓ^∞ inhomogeneous lattice problem whose only
available GoN criteria (volume, Kannan–Lovász) need ω(N) ≳ log e and so collapse to B4, while the probabilistic
version is B2's lottery. By-product (PROVED, elementary, modest novelty — a repackaging of PIGEONHOLE Lemmas
1.1/1.2): the two-half decomposition and statement (ii).
Next step if anyone pursues it: a covering-radius bound for L_e in ℓ^∞ that uses the *distribution* of the
relation lattice (Ajtai–type random-lattice / Rogers mean-value input) would have to hold for one e at every p —
that is H-A in lattice language, with no known technology.
