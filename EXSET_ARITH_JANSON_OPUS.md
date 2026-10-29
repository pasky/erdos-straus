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

## 2. Obstructions: squares, one-sidedness, and a Buchstab-type deficit

### 2.1 The square floor, located

Call 𝓕 a family *anti-square on I* if no event of 𝓕 contains a square of I.

**Lemma 2.1 (which families are anti-square; PROVED or cited).**

1. *U certificate classes on I = {n ≡ 1 (8)}.* The events are {n ≡ −v (mod A)}, with A ≡ −1 (mod v),
   v ∈ 4ℤ ∪ (8ℤ+7), and 1 < A < n+v. They are anti-square: this is Theorem E (z48). It is also CERTIFIED for the
   prime-modulus subfamily up to N = 10⁹ (§7: the chain program aborts on a square hit, and none occurred).
2. *The CONJECTURE_S_MODEL Thm 2.1 family on I = {n ≡ 1 (24)}.* The events are E_{u,v} = {n ≡ −u−v (mod uv)},
   with u, v odd and coprime and u ≡ 3 (mod 4). Squares m² with gcd(m, 6) = 1 avoid every E_{u,v}.
   *Proof.* Suppose m² ∈ E_{u,v}. If a prime p divides gcd(m, u), then p | m² + u + v − m², so p | u + v, hence p | v,
   contradicting gcd(u, v) = 1. The same argument applies to v. So gcd(m, uv) = 1, and (uv/m²) = +1. But Lemma 1.1 of
   CONJECTURE_S_MODEL gives (uv/n) = −1 for every n ≡ 1 (8) in E_{u,v} when u ≡ 3 (4). ∎
3. *Forced ES classes on I = [1,N].* These are ℛ(M), the (a,D) classes and the Case-A classes. None contains a
   square (EXCEPTIONAL_KARY2, "Key new inputs"; Mordell/Jacobi).

**Theorem 2.2 (square floor for the chain; PROVED).** Let 𝓕 be anti-square on I, and suppose (RLD) holds for some
ordering with parameters (η_i, K). Then

    Σ_i η_i P(E_i)  ≥  μ − KΔ − log(1/ν(□_I)),      □_I = squares in I.

For I = {n ≤ N : n ≡ 1 (8)} one has ν(□_I) = (4+o(1))/√N, so log(1/ν(□_I)) = ½ log N − log 4 + o(1). Thus
every unit of net model mass μ − KΔ beyond ½ log N must be paid for by RLD error.

*Proof.* □_I ⊆ Av(𝓕) ∩ I, so −log ν(Av 𝓕) ≤ log(1/ν(□_I)). Compare with Theorem 1.3. ∎

**Proposition 2.3 (where (R1) fails; PROVED).** Put σ_i = ν(□_I)/ν(B_i^d), the square share of B_i^d. Squares are
never in E_i, so

    ν(E_i | B_i^d) = (1 − σ_i) · ν(E_i | B_i^d ∖ □).

Hence (R1) at step i holds with η_i < σ_i only if the non-square part of B_i^d *over*-represents E_i by the factor
(1−η_i)/(1−σ_i). If the non-squares satisfy (R1) with η = 0 and no excess, then exactly η_i = σ_i. Summed, the
error is then Σ_i σ_i P(E_i). This is O(1) while ν(B_i^d) ≫ ν(□_I)e^{C}, and it becomes the whole mass once
ν(B_i^d) is within a constant factor of ν(□_I). So the failure is not spread over the chain. It sits in the
steps after the sifted set has come down to O(√N) elements, as the square floor requires. ∎

CERTIFIED illustration (§7, prime-modulus U family, N = 10⁹): σ ≤ 0.012 up to ℓ ≈ 1400, where the total deficit
is 0.0146. Of that, 0.0051 is the square part Σσ_ℓ w(ℓ)/ℓ; the rest is §2.3.

**Corollary 2.4 (maximal RLD depth for the three anti-square families; PROVED from Thm 2.2 and the cited model
lower bounds on μ − KΔ).** RLD with total error ≤ ημ (η < 1 fixed) is false:

* for the CONJECTURE_S_MODEL family truncated at H once c(log H)² > (½ log N)/(1−η), i.e. at
  H ≥ exp(C√log N), on I = {n ≡ 1 (24)};
* for the es-subexp-note rough Type II family (mass ≥ cL³/log L, Δ ≪ L²) once
  L³/log L ≫ log N, i.e. at T ≥ exp(C(log N log log N)^{1/3}), on I = [1,N].

These are exactly the depths at which a transferred model bound would give a power saving. *Assessment:* so the
square floor caps any RLD-based Janson transfer at a power saving, never more. This is consistent with Target 2
and gives no reason by itself to abandon the route below that depth.

### 2.2 One-sidedness (the Linnik control)

The chain uses (R1) only as a *lower* bound on hits of an independent class, and (R2) only as an upper bound up
to a constant K. No two-sided asymptotic is needed, so the method is consistent with FRONTIER §4 item 7.
Two-sided per-step statements are in fact false:

* Even in the model, ρ_i^model = P(E_i | B_i) is typically far below P(E_i) when Δ > 0. The events are positively
  correlated through shared bits. In the composite-modulus U family at A ≤ 3000 (§7), Σ P(E_i) = 9.07 while
  Σ ρ_i^model = 6.14.
* At integers, the square floor (Prop 2.3) and the deficit of §2.3 are one-sided failures of the *lower* bound.
  They are the failures that matter.

### 2.3 A third obstruction: a scale-invariant non-square deficit at moduli ≥ N^{1/2.5} (EVIDENCE + Assessment)

The numerics of §7 show something not predicted in the brief. For the prime-modulus U family, define the
*non-square deficit*

    D_ns(ℓ) = Σ_{ℓ' ≤ ℓ} [w(ℓ')/ℓ' − ρ_{ℓ'} · ν(B_{ℓ'})/ν(B_{ℓ'} ∖ □)].

This is the chain deficit after the square part has been removed exactly. D_ns is small for small ℓ but grows
steadily once ℓ ≥ N^{1/2.5}. As a function of s = log N/log ℓ it is **scale-invariant** across N = 10⁷, 10⁸,
10⁹:

| s | 2.9 | 2.3 | 2.2 | 1.95 | 1.75 |
|---|---|---|---|---|---|
| D_ns (N = 10⁸) | — | 0.024 (s=2.42) | 0.083 (s=2.21) | 0.217 (s=1.95) | 0.395 (s=1.74) |
| D_ns (N = 10⁹) | 0.009 (s=2.87) | 0.034 (s=2.48) | 0.088 (s=2.19) | 0.210 (s=1.96) | 0.364 (s=1.77) |

The random-class control has the same moduli and the same number of classes per prime, but uniformly random
residues. It has **no** deficit at any depth: |Σ(w/ℓ − ρ_ℓ)| ≤ 0.07 down to 221 survivors at N = 10⁹ and
ℓ ≤ N/2.

*Assessment (mechanism).* The U classes are **shift-aligned**. At every prime the classes are −v (mod ℓ) for the
shifts v | ℓ+1, so all events with a fixed shift v are divisibility conditions on the single integer n + v. At
integers, n + v ≤ 2N has at most s prime factors ≥ N^{1/s}. The Haar model treats divisibility by large primes
as independent, and this fails exactly as the Mertens product fails to predict sifted counts of high-dimensional
sieves near s ≈ 1. Compare the prime k-tuple count with its Mertens product, which differ by e^{γk} at
z = N. The data agree with the predicted features: the deficit depends on s only, it switches on near
s ≈ 2.5, and it is absent for unaligned classes. It is irrelevant for the targets, whose moduli are N^{o(1)}
(s → ∞). But it shows that (R1) relative to the Haar model is **false** at moduli ≥ N^{0.4}, for reasons that have
nothing to do with squares. Any proof of (R1) must therefore use that the moduli are ≤ N^{1/s_0}.

## 3. The collapse theorem: a chain of certified ratios is a majorant

The brief and z50 CONTEXT §4(e) list chain-rule / conditioning arguments as door (vii): "not of the form
N·Eν + error". This section shows that the door is open only for **per-step inputs that are not pointwise
certificates**. Every chain whose steps are certified pointwise by functions from a linear class 𝒞 is literally a
single 𝒞-majorant, and so inherits every cap proved for 𝒞.

### 3.1 The theorem

Keep the notation of §1: E_i ⊆ ℤ, B_1 = ℤ, B_{i+1} = B_i ∖ E_i, S = B_{m+1}. A **per-step certificate** for step i
is a pair (r_i, g_i), with r_i ∈ [0,1) and g_i : ℤ → ℝ, such that

    (1_{E_i} − r_i) 1_{B_i}  ≥  g_i      pointwise on ℤ,                                       (3.1)

with interval value G_i := Σ_{n∈I} g_i(n). Then Σ_I (1_{E_i} − r_i)1_{B_i} ≥ G_i. If G_i ≥ 0 this is the step bound
ρ_i ≥ r_i. More generally it gives ν(B_{i+1}) ≤ (1 − r_i)ν(B_i) − G_i/#I, which covers absolute-error inputs.

**Theorem 3.1 (collapse; PROVED).** Put c_i = ∏_{j>i}(1 − r_j) and

    ν* := ∏_{j=1}^m (1 − r_j) − Σ_i c_i g_i.

Then ν* ≥ 1_S pointwise on ℤ; in particular ν* ≥ 0 on ℤ. Moreover

    Σ_{n∈I} ν*(n) = #I·∏_j (1 − r_j) − Σ_i c_i G_i,

which is exactly the bound on #(S ∩ I) that the chain argument produces. If every g_i lies in a linear space 𝒞 of
functions containing the constants, then ν* ∈ 𝒞.

*Proof.* Pointwise, 1_{B_{i+1}} = 1_{B_i} − 1_{E_i}1_{B_i} = (1 − r_i)1_{B_i} − (1_{E_i} − r_i)1_{B_i}. By (3.1) this is
≤ (1 − r_i)1_{B_i} − g_i. Induction on i gives 1_{B_{k+1}} ≤ ∏_{j≤k}(1−r_j) − Σ_{i≤k} ∏_{i<j≤k}(1−r_j) g_i, using
1_{B_1} = 1 and 1 − r_j > 0. Take k = m. The interval identity is linearity. ∎

The chain looks multiplicative because the ratios multiply. The certificates, however, enter linearly, with the
fixed weights c_i. What the chain computes is the interval sum of one function ν* that dominates 1_S on all of ℤ.

### 3.2 Consequences: the caps apply to certified chains

**Corollary 3.2 (CRT-certified chains; PROVED given (D)20 and (D)24).** Let 𝓕 be a finite mixture of forced ES
classes (ℛ(M), (a,D), Case-A, selector), and let I = [1,N]. Suppose a chain or Janson argument certifies each step
by (3.1), with g_i a CRT function of level ≤ λ. That is, g_i is a finite real combination of indicators of residue
classes whose moduli divide one period of log-size ≤ λ. Then the bound it proves satisfies

    (a) if every modulus occurring in the g_i is ≤ D ≤ N/2:   #I·∏(1 − r_j) − Σ c_i G_i  ≥  (N − D)·e^{−Cλ^{3/4}};
    (b) if the moduli are ≤ N^A and each interval value G_i is evaluated as N·Eg_i plus at most the sum of the
        absolute coefficients of g_i (coefficient-sum evaluation): saving ≤ C_A (log N)^{3/4}.

In case (c), where moduli exceed N/2 and the G_i are evaluated exactly, the chain is a hybrid in the sense of
(D)26. There it is capped under weak SPW, which remains open.

*Proof.* By Theorem 3.1, ν* is a nonnegative CRT function of level ≤ λ, and ν* ≥ 1 on every integer that avoids
𝓕. By KARY3 (D)24, Eν* ≥ e^{−Cλ^{3/4}}. (a) By (D)20 (Selberg minorant + Poisson; nonzero frequencies with
denominator ≤ D), Σ_{n≤N} ν* ≥ (N − D)Eν*. (b) The chain's bound is then N·Eν* plus a coefficient sum. This is
the setting of (D)24 Cor 4.2 / (D)18. ∎

**Corollary 3.3 (prime-supported certificates; PROVED given (D)22).** Let I be the primes ≤ N, and suppose (3.1)
holds only at primes, with g_i CRT of level ≤ λ. Then ν* ≥ 1_S at primes and ν* ≥ 0 at primes, so ν* is an
admissible prime-law majorant. The cap of (D)22 applies: saving ≤ Cλ^{3/4}(log λ)^{3/4}, or C_Bλ^{3/4} under
bounded B. This includes per-step inputs at BV/BDH/EH/GRH level, provided they are used through pointwise
minorant/majorant certificates (Selberg weights, Bonferroni, β-sieve) at any polynomial level.

**Remark 3.4 (what the collapse covers).** Everything below is a special case of (3.1).

* *Ratio of two certified bounds.* If ν(E_i ∩ B_i) ≥ Σ_I m_i with m_i ≤ 1_{E_i}1_{B_i} and ν(B_i) ≤ Σ_I M_i with
  M_i ≥ 1_{B_i}, then r_i = Σm_i/ΣM_i is certified by g_i = m_i − r_iM_i, with G_i = 0.
* *Absolute-error level of distribution with a dichotomy* ("either B_i is small and we are done, or the error is
  relatively small"). The iteration ν(B_{i+1}) ≤ (1−r_i)ν(B_i) + err_i is linear, so it is covered with G_i = −err_i.
* *The Janson step itself.* Lemma 1.2 is pointwise. So if (R1) and (R2) are certified by 𝒞-functions, the
  composite certificate for ρ_i ≥ (1−η_i)P(E_i) − KΣP(E_i∩E_j) lies in 𝒞.
* *Density increment on progressions, and entropy chains (Shearer).* Both are dominated by the trivial CRT sieve
  with period ≤ N, i.e. level ≤ log N; the derivation is in §5.1.

### 3.3 What escapes the collapse, and LP duality

The collapse needs (3.1) on **all of ℤ** with g_i ∈ 𝒞. Two kinds of per-step input escape it.

* **(E-I) Certificates valid only on I.** If (3.1) holds only for n ∈ I, then ν* ≥ 1_S only on I. For this
  relaxation no cap can hold: already at level log 2N the LP value equals the true count (EXCEPTIONAL_LARGESIEVE2
  Prop 6.1). But a pointwise inequality on I involving the high-period set B_i is itself non-CRT interval
  information about B_i ∩ I. This is door (i).
* **(E-II) Non-pointwise inequalities about sums over I.** Examples: the large sieve applied to the set B_i,
  Cauchy–Schwarz/dispersion, Bombieri–Vinogradov proved for the specific sequence 1_{B_i}, or Halász-type bounds.
  These are not of the form (3.1). §4 shows that the *structure-blind* ones certify nothing.

*LP duality check (brief item 2).* The caps (D)17–(D)25 are proved through a comparison measure σ on the
model space. σ lives on the avoiders and is within e^{S(λ)} of uniform on every nonnegative level-λ test function
(EXCEPTIONAL_LARGESIEVE2 Lemma 1.1). So σ *violates* (R1) at every step: σ(E_i ∩ B_i) = 0. It therefore bounds a
chain argument exactly when the per-step inputs are statements that σ would also have to satisfy, namely
nonnegative level-λ tests. These are the certified chains of Theorem 3.1. For (E-I)/(E-II) inputs the comparison
measure gives no bound, and nothing in (D)17–(D)29 bounds them "secretly". **Assessment:** a chain-rule proof
beyond 3/4 must contain at least one per-step input of type (E-I) or (E-II) that carries information at level
> λ about the specific sifted set B_i ∩ I. Door (vii) is therefore not a separate door: certified chains are
capped like majorants, and every uncapped chain step is a door-(i) input.

## 4. Structure-blind inputs certify no ratio

Type (E-II) inputs include the large sieve, Barban/Davenport/Halberstam variance bounds, Cauchy–Schwarz and
dispersion with arbitrary coefficients. They are inequalities valid for every sequence on I. The brief asks for
RLD from "BV/BDH for sifted sets". This section shows that such inputs, even combined with an oracle for all
low-level statistics of B_i, cannot certify a single step of (R1).

**Proposition 4.1 (blindness; PROVED, elementary).** Fix a step i, a modulus D with gcd(q_i, D) = 1, and a set
W ⊇ B_i that is a union of classes mod D. For example, W can be the avoidance set of the events whose moduli
divide D. A *blind derivation* of (R1) at step i may use:

* (i) the exact values ν(B_i ∩ C) for every class C mod D (an oracle for all level-D statistics of B_i);
* (ii) the inclusion B_i ⊆ W;
* (iii) any inequality Φ(x) ≥ 0 that holds for every x ∈ [0,1]^I. Examples are the large sieve
  Σ_{q≤Q} Σ_{a prim} |x̂(a/q)|² ≤ (N+Q²) Σ x_n², BDH with its Siegel–Walfisz hypothesis read off from (i), and
  Cauchy–Schwarz.

Suppose the **room condition** holds: in every class C mod D, #(C ∩ I ∩ W ∖ E_i) ≥ #(C ∩ I ∩ B_i). Then no blind
derivation proves ν(E_i ∩ B_i) > 0. In particular it proves no instance of (R1) with η_i < 1.

*Proof.* In each class C mod D choose X ∩ C ⊆ (C ∩ I ∩ W) ∖ E_i with #(X ∩ C) = #(C ∩ I ∩ B_i). This is possible
by the room condition. Then x = 1_X has the same level-D statistics as B_i, since every class whose modulus
divides D is a union of such classes. Also X ⊆ W, and x satisfies every inequality of type (iii). Every premise
holds for X, yet ν(E_i ∩ X) = 0. \u220e

The room condition fails only if B_i fills W ∖ E_i in some class mod D. That cannot happen once a single event
at a modulus coprime to D has removed more than a 1/q_i share of some class. So it holds at every step after the
first few.

**Corollary 4.2.** A chain argument in which every step uses only blind inputs certifies no positive ratio at
any step past that point. Its output is then at most what the level-D information gives directly: the CRT count
of W ∩ I, i.e. the saving of the level-D sieve.

*Assessment (consequence for the brief's item 3).* "Relative BV/BDH for sifted sets" can enter the chain only
as a **sequence-specific** statement: an equidistribution theorem proved for the particular sequence 1_{B_i},
from its own structure (bilinear, multiplicative or spectral), and controlling the specific class a_i mod q_i.
The classical general-sequence theorems (BDH, the large sieve, Barban's theorem) are blind. Bombieri–Vinogradov in
max-over-a form needs a Type I/II decomposition of the sequence. For the shift-aligned U family such a
decomposition exists one shift at a time: {n : n + v has no prime factor ≡ −1 (v) below z} is multiplicative in
n + v. It does not exist for the intersection over many shifts. Equidistribution of that intersection is a
correlation statement for multiplicative indicator functions at many shifts. This is Elliott/Chowla territory
(lane D), at a depth (number of shifts ≍ log z) far beyond anything known.

## 5. Attempts at RLD in a nontrivial range

TBD.

## 6. Consequences and exponents (conditional)

TBD.

## 7. Numerics

TBD.

## 8. Reviews

TBD.
