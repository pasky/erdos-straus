# EXSET_ARITH_JANSON_OPUS — an arithmetic Janson inequality via conditional ratios (wave z50, lane C1, slug `ajopus`)

**Status: IN PROGRESS (skeleton).** ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z50_ajopus_*`. Data: `data/z50_ajopus/`.

## 0. Summary table

| # | statement | label | section |
|---|---|---|---|
| A | integer Janson from one relative-level hypothesis (RLD) | TBD | §1 |
| B | square floor: where RLD must fail | TBD | §2 |
| C | collapse: chains of certified ratios are majorants | TBD | §3 |
| D | structure-blind inputs certify no ratio | TBD | §4 |
| E | positive range for RLD | TBD | §5 |
| F | exponents if RLD held to depth L | TBD | §6 |
| G | numerics | TBD | §7 |
| H | hostile reviews | TBD | §8 |

**Exact remaining gap:** TBD.

## 1. Janson's proof as a product of ratios; the one hypothesis (RLD)

### 1.1 Setting

* **Integers.** I ⊂ ℤ is a finite set of integers. Typical choices: I = [1,N]; I = {n ≤ N : n ≡ 1 (mod 8)} (the
  U / ES₅ setting); or the primes ≤ N. ν is the uniform probability on I. For X ⊆ ℤ write ν(X) = #(X ∩ I)/#I.
* **Model.** P is the profinite Haar probability, conditioned on the same 2-adic (and, if wanted, 3-adic) class as
  I. The coordinates X_p = n mod p^∞ are independent.
* **Events.** 𝓕 = (E_1, …, E_m) is an ordered family of residue classes E_i = {n ≡ a_i (mod q_i)}. Each E_i is read both
  as a subset of ℤ and as an event in the model. supp(E_i) is the set of primes p | q_i. For p = 2, count p only if
  the class fixes n beyond the conditioned 2-adic class.
* **Relations.**
  - E_i, E_j **conflict** if a_i ≢ a_j (mod gcd(q_i, q_j)). Then E_i ∩ E_j = ∅ in ℤ *and* in the model.
  - They **share a bit** (j ∼ i) if supp(E_i) ∩ supp(E_j) ≠ ∅ and they do not conflict.
  - They are **independent** if their supports are disjoint.
* **Sifted sets.** B_i = Av(E_1, …, E_{i−1}) = ℤ ∖ ∪_{j<i} E_j and S = Av(𝓕) = B_{m+1}. Also
  B_i^d = Av({E_j : j < i, supp E_j ∩ supp E_i = ∅}) ⊇ B_i.
* **Model quantities.** μ = Σ_i P(E_i) and Δ = Σ_{j<i, j∼i} P(E_i ∩ E_j).

The model inequality to be transferred is the atomic Janson inequality of `paper/es-subexp-note.tex` (Theorem
"Janson-type inequality for atomic events"; restated in CONJECTURE_S_MODEL §2.1):
−log P(Av 𝓕) ≥ μ − KΔ, with K = e^{1/3} under the local-lemma hypotheses.

### 1.2 The chain identity and the Harris-free reduction

**Lemma 1.1 (chain identity; PROVED, trivial).** Put ρ_i = ν(E_i ∩ B_i)/ν(B_i) (and stop if ν(B_i) = 0). Then

    ν(S) = ∏_i (1 − ρ_i),   hence   −log ν(S) ≥ Σ_i ρ_i.

*Proof.* B_{i+1} = B_i ∖ (E_i ∩ B_i). ∎

**Lemma 1.2 (pointwise reduction; PROVED).** For every i, pointwise on ℤ,

    1_{E_i} 1_{B_i} ≥ 1_{E_i} 1_{B_i^d} − Σ_{j<i, j∼i} 1_{E_i ∩ E_j} 1_{B_i^d}     and     1_{B_i} ≤ 1_{B_i^d}.

*Proof.* B_i = B_i^d ∖ ∪{E_j : j < i, supp E_j ∩ supp E_i ≠ ∅}. The E_j in this union that conflict with E_i are
disjoint from E_i as subsets of ℤ. So E_i ∩ B_i = (E_i ∩ B_i^d) ∖ ∪_{j∼i} E_j. Apply the union bound. ∎

Lemma 1.2 is the integer form of the first two lines of the model proof. It needs neither Harris nor
independence: at integers it is literally the same inclusion–exclusion. All arithmetic sits in the two remaining
steps.

### 1.3 Where Harris (and independence) enter, and what replaces them

The model proof bounds ρ_i^model = P(E_i | B_i) from below in three moves:

* (M1) P(E_i | B_i) ≥ [P(E_i ∩ B_i^d) − Σ_{j∼i} P(E_i ∩ E_j ∩ B_i^d)] / P(B_i^d). This is Lemma 1.2 and holds verbatim
  for ν.
* (M2) **Independence.** P(E_i ∩ B_i^d) = P(E_i) P(B_i^d), because B_i^d involves no coordinate of E_i. This is not
  Harris; it is the product structure. At integers it becomes a *relative* level-of-distribution statement: the
  class a_i mod q_i must be represented in the sifted set B_i^d ∩ I with its model share.
* (M3) **Harris substitute.** P(E_i ∩ E_j ∩ B_i^d) = P(E_i) P(E_j' ∩ B_i^d) ≤ K P(E_i ∩ E_j) P(B_i^d). The first equality
  is again independence. The inequality is the lopsided local lemma, whose only correlation input is Lemma
  "Compatible events": P(A ∩ Av(𝒞)) ≤ P(A) P(Av(𝒞)) when no member of 𝒞 conflicts with A. This lemma is the
  replacement for Harris in the one-hot setting. Its proof conditions on A, which turns each C ∈ 𝒞 into a
  *larger* event C′ ⊇ C. At integers, conditioning on A = {n ≡ a (mod q)} maps I to the progression
  {a + qm} of length #I/q. Sifting by the larger events C′ is then a *different* sieve problem on a *shorter*
  interval. The model comparison becomes a relative *upper* bound for a class inside an avoidance set.

So the integer proof needs exactly one kind of input: relative equidistribution of a residue class inside an
avoidance set of the same family. A lower bound is needed for independent classes (M2), and an upper bound with
constant K for compatible pair classes (M3).

**Hypothesis (RLD) [parameters η_i ∈ [0,1], K ≥ 1].** For every i:

* (R1) ν(E_i ∩ B_i^d) ≥ (1 − η_i) P(E_i) ν(B_i^d);
* (R2) ν(E_i ∩ E_j ∩ B_i^d) ≤ K P(E_i ∩ E_j) ν(B_i^d) for every j < i with j ∼ i.

(R1) is a lower bound for a class independent of the sifting family. (R2) is an upper bound for an atomic class
inside an avoidance set (lopsided). In the model, (R1) holds with η_i = 0 and (R2) with K = ∏(1−x)^{−1} by the
lopsided LLL. For families with Δ = 0, (R2) is vacuous. An example is prime moduli with all classes at one prime
merged into one step; there only (R1) is needed.

**Theorem 1.3 (integer Janson from RLD; PROVED, elementary).** Under (RLD),

    −log ν(Av 𝓕) ≥ μ − Σ_i η_i P(E_i) − K Δ.

If (RLD) holds for every subfamily (same K, and errors Σ η_i P(E_i) ≤ η μ(subfamily)), then also
−log ν(Av 𝓕) ≥ min((1−η)μ/2, (1−η)²μ²/(4KΔ)).

*Proof.* By Lemma 1.2, ρ_i ≥ ν(E_i ∩ B_i)/ν(B_i^d) ≥ [ν(E_i ∩ B_i^d) − Σ_{j∼i} ν(E_i ∩ E_j ∩ B_i^d)]/ν(B_i^d).
By (R1), (R2) this is ≥ (1−η_i)P(E_i) − K Σ_{j∼i} P(E_i ∩ E_j). Sum and apply Lemma 1.1. For the second form, note
ν(Av 𝓕) ≤ ν(Av 𝓕′) and repeat the random-subfamily averaging of the model proof, with μ replaced by (1−η)μ. ∎

*Assessment.* Theorem 1.3 is a bookkeeping statement. Its value is that it isolates the arithmetic input as one
family of relative inequalities. Everything below is about (RLD): where it is false (§2), and which kinds of proof
of it are automatically capped (§§3–4). Then comes what is true numerically (§7), and what it would give (§6).

### 1.4 Averaged RLD is the conclusion

**Lemma 1.4 (PROVED, trivial).** For any block i ∈ [a, b),

    Σ_{a≤i<b} ρ_i ≤ log(ν(B_a)/ν(B_b)) ≤ Σ_{a≤i<b} ρ_i/(1 − ρ_i).

So the *block-averaged* lower bound Σ_{block} ρ_i ≥ (1−η)μ_block is equivalent, up to second-order terms
Σρ_i², to the relative survival bound ν(B_b) ≤ ν(B_a) e^{−(1−η)μ_block}. That is a relative exceptional-set
statement of the same kind as the target.

*Consequence (Assessment, but forced by Lemma 1.4).* The chain rule gains leverage over a direct count only if
(R1) can be proved **step by step** by an argument that does not, in effect, count B_i ∩ I. The rest of this
document classifies such per-step arguments.

## 2. Obstructions: squares, Linnik, small sets

TBD.

## 3. The collapse theorem: why a chain of ratios is not automatically non-linear

TBD.

## 4. Structure-blind inputs

TBD.

## 5. Attempts at RLD in a nontrivial range

TBD.

## 6. Consequences and exponents (conditional)

TBD.

## 7. Numerics

TBD.

## 8. Reviews

TBD.
