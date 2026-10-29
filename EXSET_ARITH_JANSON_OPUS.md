# EXSET_ARITH_JANSON_OPUS — an arithmetic Janson inequality via conditional ratios (wave z50, lane C1, slug `ajopus`)

ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z50_ajopus_*`. Data: `data/z50_ajopus/`.

## 0. Summary table

**Status: ROUND 1 COMPLETE (round-1 cross-model review pending; §8).**

| # | statement | label | § |
|---|---|---|---|
| A | Integer Janson: −log ν(Av 𝓕) ≥ μ − Σ η_i P(E_i) − KΔ under one relative-level hypothesis (RLD) = (R1) lower bound for independent classes in avoidance sets + (R2) K-upper bound for compatible pair classes. Harris enters only through (R2); independence through (R1). | PROVED (elementary) | §1 |
| A′ | Block-averaged RLD ⇔ the relative exceptional-set bound itself (no leverage without step-wise proofs) | PROVED (trivial) | §1.4 |
| B | Square floor located: for anti-square families (U at n≡1 (8), ES₅/S-model edges at n≡1 (24), forced ES classes) RLD error ≥ μ − KΔ − ½log N + O(1); the failure sits in the steps where B_i^d is within O(1) of the squares (η_i = σ_i, the square share) | PROVED | §2.1 |
| B′ | (R1) relative to the Haar model also fails, off the squares, for the U prime family at moduli ≥ N^{0.4}: a non-square deficit D_ns(s), s = log N/log ℓ, scale-invariant and bounded in N for fixed s; absent for random and for random-QNR classes; mechanism not identified | EVIDENCE (N = 10⁷–10⁹) | §2.3, §7 |
| C | **Collapse theorem:** any chain/Janson/conditioning argument whose steps are certified pointwise on ℤ by functions of a linear class 𝒞 is literally one 𝒞-majorant; hence CRT-certified chains save ≤ C(log N)^{3/4} (moduli ≤ N/2, or coefficient-sum evaluation, (D)20/(D)24) and prime-certified chains obey (D)22. Density-increment and entropy chains are CRT of level ≤ log N. | PROVED | §3, §5.3 |
| C′ | LP-duality check: the comparison measure of (D)17–(D)25 violates (R1) at every step, so it bounds exactly the certified chains; door (vii) reduces to door (i) | PROVED (C) + Assessment | §3.3 |
| D | Blindness: (R1) at a step is not derivable from an oracle for all level-D statistics of B_i^d + inclusion in a level-D set + any inequality valid for all [0,1]-sequences (large sieve, BDH, Cauchy–Schwarz), whenever a room condition holds (a hypothesis); with lane C2's r-wise-marginal laws, (RLD) needs genuinely archimedean information about B_i^d ∩ I | PROVED (elementary), per step | §4 |
| E | Positive ranges: exact CRT range (η_i ≤ 2P_iq_i/(Nβ_i)); fundamental-lemma range log ℓ ≤ c√log N (nothing new); blocking step beyond = a fundamental lemma in dimension κ ≍ log z at level s ≪ κ (FL∞) | PROVED / standard / Assessment | §5 |
| E′ | Conjecture RLD-U: off the squares, the prime-modulus U sieve at z = N^{1/s} is within e^{C(s)} of its Mertens product, C(s) < ∞ for every s > 1 | CONJECTURE (EVIDENCE: three decades, flat in N) | §5.5 |
| F | RLD-U at one s < 2C_V ≈ 1.48 ⇒ #{n ≤ N : U(n) fails} = #odd squares + O(N^{1−C_V/s+o(1)}) = #□ + o(√N) (Target 2 for U); exponent table for RLD to depth exp((log N)^α): θ = α (prime U), 2α (ES₅ edges), 3α (ES Type II); square floor sits exactly at the power-saving depth | CONDITIONAL | §6 |
| G | U holds trivially at every n ≡ 5 (8) (v = 3, A = 2) | PROVED (trivial) | §6 |
| H | Cross-model hostile review | see §8 | §8 |

**Exact remaining gap.** Beyond log ℓ ≍ √log N every proof of a single chain step (R1) must be a
sequence-specific, non-pointwise statement about the high-period sifted set B_i ∩ I (door (i)); certified
inputs collapse (C) and blind inputs certify nothing (D). For the prime U family this is the open problem FL∞
(a fundamental lemma beyond the sieve dimension), which numerically holds up to a bounded factor (E′) and would
give Target 2 for U (F). No instance of (R1) beyond the fundamental-lemma range was proved.

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

So, if ρ_max := max_{block} ρ_i ≤ 1/2, the *block-averaged* lower bound Σ_{block} ρ_i ≥ (1−η)μ_block implies the
relative survival bound ν(B_b) ≤ ν(B_a) e^{−(1−η)μ_block}. Conversely, the relative bound
ν(B_b) ≤ ν(B_a)e^{−X} implies Σ_{block} ρ_i ≥ (1−ρ_max)X. (Review repair: the remainder is Σρ_i²/(1−ρ_i), which
needs ρ_max bounded away from 1. The *ratio* bound is what is equivalent; an absolute survival bound alone does
not give it.) Both sides are relative exceptional-set statements of the same kind as the target.

*Consequence (Assessment, but forced by Lemma 1.4).* The chain rule gains leverage over a direct count only if
(R1) can be proved **step by step** by an argument that does not, in effect, count B_i ∩ I. The rest of this
document classifies such per-step arguments.

## 2. Obstructions: squares, one-sidedness, and a Buchstab-type deficit

### 2.1 The square floor, located

Call 𝓕 a family *anti-square on I* if no event of 𝓕 contains a square of I.

**Lemma 2.1 (which families are anti-square; PROVED or cited).**

1. *U certificate classes on I = {n ≡ 1 (8)}.* The events are {n ≡ −v (mod A)}, with A ≡ −1 (mod v),
   v ∈ 4ℤ ∪ (8ℤ+7), and 1 < A < n+v. They are anti-square: this is Theorem E (z48). It is also CERTIFIED for the
   prime-modulus subfamily up to N = 10⁹. The chain program of §7 checks every killed element and warns on a square
hit; no warning occurred. (Theorem E in fact excludes every divisor A > 1, proper or not.)
2. *The CONJECTURE_S_MODEL Thm 2.1 family on I = {n ≡ 1 (24)}.* The events are E_{u,v} = {n ≡ −u−v (mod uv)},
   with u, v odd and coprime and u ≡ 3 (mod 4). Squares m² with gcd(m, 6) = 1 avoid every E_{u,v}.
   *Proof.* Suppose m² ∈ E_{u,v}. If a prime p divides gcd(m, u), then p | m² + u + v − m², so p | u + v, hence p | v,
   contradicting gcd(u, v) = 1. The same argument applies to v. So gcd(m, uv) = 1, and (uv/m²) = +1. But Lemma 1.1 of
   CONJECTURE_S_MODEL gives (uv/n) = −1 for every n ≡ 1 (8) in E_{u,v} when u ≡ 3 (4). ∎
3. *Forced ES classes on I = [1,N].* These are ℛ(M), the (a,D) classes and the Case-A classes. None contains a
   square (EXCEPTIONAL_KARY2, "Key new inputs"; Mordell/Jacobi). Selector classes 0 mod p are excluded from this
   statement.

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
(1−η_i)/(1−σ_i). If the non-squares satisfy (R1) with η = 0 and no excess, then exactly η_i = σ_i, and the summed
error is Σ_i σ_i P(E_i). ∎

*Localization (CONDITIONAL on model-like decay; review repair).* The identity alone does not localize the
failure. Suppose additionally that ν(B_i^d) ≥ c·e^{−μ_i}, where μ_i = Σ_{j<i}P(E_j) is the mass already sifted.
Write T = log(1/ν(□_I)). Then σ_i ≤ c^{−1}e^{−(T−μ_i)}, and with P(E_i) ≤ 1/8,

    Σ_{i: μ_i ≤ T−t} σ_i P(E_i) ≤ c^{−1}∫_0^{T−t+1/8} e^{−(T−m)} dm ≤ 2c^{−1}e^{−t}.

So the square error accumulated before the last t units of mass ahead of the floor is O(e^{−t}). Under that
decay, the square-forced failure sits in the final O(1) units of mass before the sifted set reaches O(√N)
elements. Without the decay hypothesis only the identity is proved.

CERTIFIED illustration (§7, prime-modulus U family, N = 10⁹): σ ≤ 0.0055 up to ℓ = 1361, where the total
deficit is 0.0146. Of that, 0.0052 is the square part; the rest (0.0095) is §2.3.

**Corollary 2.4 (maximal RLD depth for the three anti-square families; PROVED from Thm 2.2 and the cited model
lower bounds on μ − KΔ).** RLD with total error ≤ ημ (η < 1 fixed) is false:

* for the rough-endpoint certificate edge family (the I3_DEEP_ASTRA §8.4 route transferred to certificates by
  Lemma 1.1 of CONJECTURE_S_MODEL; model −log survival ≥ cL²/(log L)², Δ = o(1)) truncated at H once
  cL²/(log L)² > (½ log N)/(1−η) + KΔ, i.e. at log H ≍ √log N·log log N, on I = {n ≡ 1 (24)};
* for the es-subexp-note rough Type II family (mass ≥ cL³/log L, Δ ≪ L²) once
  L³/log L ≫ log N, i.e. at T ≥ exp(C(log N log log N)^{1/3}), on I = [1,N].

K = O(1) is assumed throughout; a growing K defeats the deduction. *Review repair:* an earlier draft used the
CONJECTURE_S_MODEL Thm 2.1 family itself. That is not legitimate, because Thm 2.1 bounds μ and Δ only *after
conditioning on all small-prime coordinates*. Unconditioned, the family contains, e.g., the subfamily with
s₁ = 7, s₂ = 1, whose events all share the prime 7, and there Δ ≫ L⁴/(log L)⁴. A fibrewise integer transfer,
on progressions mod Q_Y with Q_Y = e^{O(L⁹)}, would need L ≤ (log N)^{1/9}.

These are exactly the depths at which a transferred model bound would give a power saving (up to logarithms). *Assessment:* so the
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

| s ≈ | 3.0 | 2.75 | 2.5 | 2.25 | 2.0 | 1.75 | 1.5 | 1.25 |
|---|---|---|---|---|---|---|---|---|
| D_ns, N = 10⁷ | −0.004 | 0.002 | 0.020 | 0.060 | 0.178 | 0.380 | 0.666 | 1.205 |
| D_ns, N = 10⁸ | 0.002 | 0.013 | 0.033 | 0.065 | 0.184 | 0.395 | 0.687 | 1.279 |
| D_ns, N = 10⁹ | 0.007 | 0.013 | 0.034 | 0.074 | 0.178 | 0.396 | 0.678 | 1.211 |
| model mass at N = 10⁹ | 3.42 | 3.74 | 4.36 | 4.98 | 5.77 | 6.92 | 8.40 | 10.41 |

(Nearest checkpoint to each s; the actual s differs by ≤ 0.04. Source: `data/z50_ajopus/chain_U_N*.txt`, column 9.)

The random-class control has the same moduli and the same number of classes per prime, but uniformly random
residues. It has **no** deficit at any depth: |Σ(w/ℓ − ρ_ℓ)| ≤ 0.07 down to 221 survivors at N = 10⁹ and
ℓ ≤ N/2.

Two features matter (EVIDENCE, three scales only). First, at fixed s the deficit does not grow with N over
N = 10⁷, 10⁸, 10⁹: the rows agree to ±0.02 for s ≥ 1.5 and to ±0.04 at s ≈ 1.25 (1.205, 1.279, 1.211; the
checkpoints are matched to nearest s, not interpolated). Meanwhile the model mass at fixed s grows like 0.74·log N/s.
Three scales cannot establish boundedness in N. They are consistent with it, in which case the relative error
D_ns/mass → 0 at every fixed s > 1. Second, the deficit switches on near s ≈ 2.5 and grows as s → 1. It is
irrelevant for the targets, whose moduli are N^{o(1)}. Note also that an O(1) integrated deficit is compatible
with vanishing average per-step relative error, so these data do not show that pointwise-in-step (R1) fails. They
show that the Haar model is off by a factor e^{D_ns(s)} at moduli ≥ N^{0.4}, for a reason unrelated to squares.

*Controls (EVIDENCE, N = 10⁹; §7).*

* (a) Random classes (distinct nonzero residues), same w(ℓ): total deviation within ±0.07 to the end (221
  survivors).
* (b) Random **quadratic non-residue** classes, same w(ℓ): the deviation is the square part; the non-square
  deficit stays within [−0.017, 0.050] down to ℓ = N/2.
* (c) Shift-aligned classes −v (mod ℓ), v | ℓ+1, v ≡ 1 (4) or 3 (8) (not anti-square; includes the full shift
  v = 1): the total deviation from the model is large and of both signs. It reaches +0.49 near s ≈ 1.6 and −1.54
  at the end (597 survivors).
* (d) Small-core near-squares km² (1 < k ≤ 10⁴) are **not** enriched among the U survivors at s = 2: 0.76%,
  against a baseline of 0.79%.

*Assessment (mechanism).* Deviations from the Haar model at small s occur for both shift-aligned families, (c) and
U, with family-dependent sign. They do not occur for either unaligned family, (a) and (b). This points to the shift
alignment: all events at shift v are divisibility conditions on the single integer n + v ≤ 2N, which has at most s
prime factors ≥ N^{1/s}. That is the familiar failure of Mertens products for high-dimensional sieves near s ≈ 1
(prime k-tuples: a factor (e^γ ω(s))^k). The sign and size for U are not explained, and the mechanism is not
established.

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

**Corollary 3.2 (CRT-certified chains; PROVED given (D)20, (D)24 and EXSET_I3 Cor 7.1).** Let 𝓕 be a finite
mixture of forced ES classes (ℛ(M), (a,D), Case-A, selector), and let I = [1,N]. Suppose a chain or Janson argument
certifies each step by (3.1), with g_i a CRT function of level ≤ λ. Level is meant in the ledger's sense: g_i is a
finite real combination of residue-class indicators, *each* of rough logarithmic level ≤ λ. No common small period
is required; a sum of terms with separate small moduli need not have one. Then:

* (a) If every modulus occurring in the g_i is ≤ D ≤ N/2, the bound proved satisfies
  #I·∏(1 − r_j) − Σ c_i G_i ≥ (N − D)·e^{−Cλ^{3/4}}.
* (b) Suppose instead the moduli are ≤ N^A and each interval value is evaluated with worst-case positive error
  accounting, G_i ≥ N·Eg_i − T_i with T_i the sum of absolute coefficients of g_i. If the chain's bound charges
  +Σc_iT_i, then that bound is ≥ N·Eν* ≥ N e^{−C_A(log N)^{3/4}}.
* For the native U/ES₅ class universe on n ≡ 1 (4) (EXSET_I3 Cor 7.1, lane E), the same two statements hold with
  the stronger cap Cλ^{2/3}/(log λ)^{1/3} in place of Cλ^{3/4}. This is the case for the U families of §§2, 5–7.

If the moduli exceed N/2 and the G_i are evaluated exactly, nothing is claimed. (Review repair: this case is not the
position-blind hybrid of (D)26, so the conditional weak-SPW cap does not cover it.)

*Proof.* By Theorem 3.1, ν* is a nonnegative CRT function of level ≤ λ, and ν* ≥ 1 on every integer that avoids 𝓕.
By KARY3 (D)24, Eν* ≥ e^{−Cλ^{3/4}}; for native U/ES₅ classes, EXSET_I3 Cor 7.1 gives the stronger bound. (a) By
(D)20 (Selberg minorant + Poisson; nonzero frequencies with denominator ≤ D), Σ_{n≤N} ν* ≥ (N − D)Eν*. (b) The
chain's bound is #I·∏(1−r) − Σc_i(N·Eg_i − T_i) = N·Eν* + Σc_iT_i, using #I = N. ∎

**Corollary 3.3 (prime-supported certificates; PROVED given (D)22, scoped).** Let I be the primes ≤ N and 𝓕 a
forced-class mixture. Suppose (3.1) holds at **all** primes (not only those ≤ N), with g_i CRT of level ≤ λ. Then
ν* ≥ 1_S ≥ 0 at all primes, so ν* is an admissible prime-law majorant, and its unit-Haar mean obeys the cap of
(D)22: log(1/E*ν*) ≤ Cλ^{3/4}(log λ)^{3/4}, or C_Bλ^{3/4} under bounded B. The chain's interval bound inherits this
only under the prime-law evaluation hypotheses of (D)22 (bound = π(N)E*ν* + Err). (D)22 does not bound arbitrary
exact prime sums.

**Remark 3.4 (what the collapse covers).** The following are special cases of (3.1).

* *Ratio of two certified bounds.* If ν(E_i ∩ B_i) ≥ Σ_I m_i with m_i ≤ 1_{E_i}1_{B_i} and ν(B_i) ≤ Σ_I M_i with
  M_i ≥ 1_{B_i}, then r_i = Σm_i/ΣM_i is certified by g_i = m_i − r_iM_i, with G_i = 0.
* *Absolute-error inputs*, ν(B_{i+1}) ≤ (1−r_i)ν(B_i) + err_i. These are covered **only if** the input itself
  comes with a pointwise certificate g_i ≤ (1_{E_i} − r_i)1_{B_i} and Σ_I g_i ≥ −err_i. A bare analytic error term
  need not have one.
* *The Janson step itself.* Lemma 1.2 is pointwise. So if (R1) and (R2) are certified by 𝒞-functions, the
  composite certificate lies in 𝒞.

### 3.3 What escapes the collapse, and LP duality

The collapse needs (3.1) on **all of ℤ** with g_i ∈ 𝒞. Two kinds of per-step input escape it.

* **(E-I) Certificates valid only on I.** If (3.1) holds only for n ∈ I, then ν* ≥ 1_S only on I. For this
  relaxation no cap can hold: already at level log 2N the LP value equals the true count (EXCEPTIONAL_LARGESIEVE2
  Prop 6.1). But a pointwise inequality on I involving the high-period set B_i is itself non-CRT interval
  information about B_i ∩ I. This is door (i).
* **(E-II) Non-pointwise inequalities about sums over I.** Examples: the large sieve applied to the set B_i,
  Cauchy–Schwarz/dispersion, Bombieri–Vinogradov proved for the specific sequence 1_{B_i}, or Halász-type bounds.
  These are not of the form (3.1). §4 shows that the *structure-blind* ones certify nothing.

*LP duality check (brief item 2).* The caps (D)17–(D)25 are proved through a comparison measure σ on the model
space. σ lives on the avoiders and is within e^{S(λ)} of uniform on every nonnegative level-λ test function
(EXCEPTIONAL_LARGESIEVE2 Lemma 1.1). Lane C2 (EXSET_ARITH_JANSON_ASTRA §4.1, (4.2)) states the same duality in
moment form: the maximal avoidance over all laws with *exactly* the CRT moments on level-λ tests equals the
CRT-majorant value. σ violates (R1) at every step, since σ(E_i ∩ B_i) = 0. So it bounds a chain exactly when the
chain's per-step inputs are statements that σ would also have to satisfy. Theorem 3.1 shows that pointwise level-λ
certificates are such statements. For (E-I)/(E-II) inputs neither the comparison measure nor the moment LP gives
a bound. Nothing in (D)17–(D)29 bounds them "secretly".

*Scope (review repair).* Theorem 3.1 covers chains with fixed scalars r_i and pointwise linear certificates. It is
not a classification of all nonlinear, adaptive or entropy arguments. **Assessment:** a chain-rule proof beyond the
caps must contain some per-step input that is not a pointwise level-λ certificate, and that carries information
about the specific set B_i^d ∩ I beyond its low-level statistics (§4). That is the content of door (i). Whether
every such input "is" a door-(i) input is a matter of definition, not a theorem.

## 4. Structure-blind inputs certify no ratio

Type (E-II) inputs include the large sieve, Barban/Davenport/Halberstam variance bounds, Cauchy–Schwarz and
dispersion with arbitrary coefficients. They are inequalities valid for every sequence on I. The brief asks for
RLD from "BV/BDH for sifted sets". This section shows that such inputs cannot certify a step of (R1) once the
step has any room. That holds even when they are combined with an oracle for all level-D statistics of the set
in (R1).

**Proposition 4.1 (blindness; PROVED, elementary; repaired after review).** Fix a step i and write B = B_i^d, the
set occurring in (R1). Fix a modulus D with gcd(q_i, D) = 1, and a set W ⊇ B that is a union of classes mod D. A
*blind derivation* of a lower bound for ν(E_i ∩ B) may use:

* (i) the exact values ν(B ∩ C) for every class C mod D (an oracle for all level-D statistics of B);
* (ii) the inclusion B ⊆ W;
* (iii) any inequality Φ(x) ≥ 0 that holds for every x ∈ [0,1]^I. Examples are the large sieve
  Σ_{q≤Q} Σ_{a prim} |x̂(a/q)|² ≤ (N+Q²) Σ x_n² and Cauchy–Schwarz. General-sequence BDH counts too, provided its
  hypotheses are verified only through (i).

Suppose the **room condition** holds: in every class C mod D, #(C ∩ I ∩ W ∖ E_i) ≥ #(C ∩ I ∩ B). Then no blind
derivation proves ν(E_i ∩ B) > 0, and in particular none proves (R1) at step i with η_i < 1.

*Proof.* In each class C mod D choose X ∩ C ⊆ (C ∩ I ∩ W) ∖ E_i with #(X ∩ C) = #(C ∩ I ∩ B). This is possible by
the room condition. Then 1_X has the same level-D statistics as B, since every class of modulus dividing D is a
union of such classes. Also X ⊆ W, and 1_X satisfies every inequality of type (iii). Every premise holds for X,
yet ν(E_i ∩ X) = 0. ∎

*Remarks.*

1. **Room is a hypothesis, not automatic.** It fails, for instance, when B fills I. Take I = [1,30], E_1 = 0 mod 3,
   E_2 = 1 mod 3, D = 1: then B_2^d = I and (R1) holds exactly (review counterexample to the pre-repair version,
   which used B_i instead of B_i^d). Room holds when, in every class C mod D, B occupies at most a
   (1 − 1/q_i)-fraction of C ∩ I ∩ W. This needs B to be genuinely sifted inside W *in every cell*, and cells of
   length ≥ q_i, so D ≤ N/q_i.
2. **Per-step only.** The oracle reveals |B ∩ I|. So Proposition 4.1 says nothing about what a sequence of
   oracles at different steps could deliver; no chain-level corollary is claimed.
3. **Relation to lane C2.** EXSET_ARITH_JANSON_ASTRA Prop 4.3 / Thm 4.1 construct laws on the residue space, *not*
   supported on an interval, that have exactly independent uniform r-coordinate marginals for any prescribed
   sparse forbidden sets (including ES labels), yet avoid far more often than e^{−μ}. Proposition 4.1 is the
   interval-supported counterpart: the fake X is an honest subset of I, but it matches only level-D statistics.
   Together they show the following. (RLD) cannot follow from (r-wise residue marginals) ∪ (level-D statistics of
   the set on I) ∪ (inequalities valid for all sequences). It needs information about the specific set
   B_i^d ∩ I that is *archimedean*: it uses that I is an interval of integers and that B_i^d is the actual sifted
   set.

*Assessment (consequence for the brief's item 3; downgraded after review).* "Relative BV/BDH for sifted sets" can
enter the chain usefully only as a **sequence-specific** statement: an equidistribution theorem for the particular
sequence 1_{B_i^d}, proved from its own structure and controlling the specific class a_i mod q_i. BV in
max-over-a form is not a general-sequence theorem; it needs a Type I/II decomposition. For the shift-aligned U
family such structure exists one shift at a time: {n : n + v has no prime factor ≡ −1 (v) below z} is
multiplicative in n + v. I know of no usable decomposition of the intersection over many shifts, but its
nonexistence is not proved. Equidistribution of that intersection is a correlation statement for multiplicative
indicator functions at ≍ log z shifts. This is Elliott/Chowla territory (lane D).

## 5. Attempts at RLD in a nontrivial range

### 5.1 The exact CRT range (PROVED)

**Proposition 5.1 (repaired after review).** Let I = [1,N]. Let B_i^d be periodic with period P_i, let
gcd(q_i, P_i) = 1, and let N ≥ 2P_i. Then

    | ν(E_i ∩ B_i^d)/ν(B_i^d) − 1/q_i |  ≤  4P_i/N,

so (R1) holds with η_i ≤ 4P_iq_i/N. For I a progression mod 8 (or 24) with gcd(P_i, 8) = 1, the same bound holds
with N replaced by #I.

*Proof.* Let r = #(B_i^d mod P_i) and A = #(E_i ∩ B_i^d ∩ I), B = #(B_i^d ∩ I). Each residue class b mod P_i in
B_i^d meets E_i in a single class mod P_iq_i, which contains N/(P_iq_i) + θ elements of [1,N] with |θ| ≤ 1. Hence
|A − rN/(P_iq_i)| ≤ r, and in the same way |B − rN/P_i| ≤ r. So B ≥ rN/(2P_i) once N ≥ 2P_i, and
|A/B − 1/q_i| ≤ (|A − rN/(P_iq_i)| + |B − rN/P_i|/q_i)/B ≤ 2r/B ≤ 4P_i/N. ∎

The chain stays in this range while the lcm of all moduli used is ≤ N^{1−ε}. For the prime U family that means
ℓ ≤ (1−ε)log N, so mass ≈ 0.74 log log N. This is the trivial range.

### 5.2 The fundamental-lemma range (standard; z50 CONTEXT §4(a))

For the prime U family the local density is w(ℓ)/ℓ, with w(ℓ) = #{v | ℓ+1 : v ≡ 0 (4) or v ≡ 7 (8)}. The
mass is Σ_{ℓ≤z} w(ℓ)/ℓ = (C_V + o(1)) log z, a Titchmarsh-divisor-type asymptotic. The empirical slope from §7
is C_V ≈ 0.74 (EVIDENCE; the constant was not derived in closed form). The sieve dimension on [w, z) is ≍ log z,
so a fundamental lemma needs s = log N/log z ≫ log z. In that range both counts in (R1) should be asymptotic to
their model values with relative error e^{−s/C}. *Label: Assessment / standard.* FI Lemma 6.3 and Cor 6.10 are
stated for fixed dimension. The uniform version in dimension κ ≍ log z needs the quantitative Bonferroni/β-sieve
bookkeeping, which is not re-done here. So the whole chain, and with it the
exceptional-set bound N exp(−c√log N), holds for log z ≤ c√log N. No chain is needed for this: the
fundamental lemma bounds the count directly. Note (a) of z50 CONTEXT is confirmed. Selberg's Λ² and the large
sieve stop at the same point. The reason is a Rankin truncation: the Euler product ∏(1 + g(p)) is carried by
d of size exp(c(log z)²).

### 5.3 Density increment and entropy chains (PROVED, short)

* *Density increment on progressions.* Suppose S ∩ I avoids the classes Ω_q mod q. Then some class mod q outside
  Ω_q carries S-density ≥ δq/(q − |Ω_q|). Iterating along coprime moduli q_1, …, q_k with product Q gives
  δ ≤ ∏_j(1 − |Ω_{q_j}|/q_j) + O(Q/N). The certificate is the indicator of a union of classes mod Q, a CRT
  majorant of level log Q ≤ log N. It is weaker than the caps.
* *Entropy chain rule (repaired after review).* Write X_j = n mod q_j for n uniform on S ∩ I, with coprime q_j and
  Q = ∏q_j. Then log #S = H(X_1, …, X_k) + H(n | X) ≤ Σ_j log(q_j − |Ω_{q_j}|) + log⌈N/Q⌉. Exponentiated, this is
  #(allowed classes mod Q)·⌈N/Q⌉ ≥ N·Eν, where ν is the indicator of the allowed classes mod Q. That is a CRT
  majorant of level log Q, so this entropy bound is never better than N·Eν. It is capped by (D)24, or by the 2/3
  cap for native U classes, whenever Q ≤ N^A. (The earlier claim that the bound is useless for Q > N was false.
  Example: N = 5, moduli 2 and 3, one allowed residue each, gives log#S ≤ 0.) Shearer-type inequalities with
  overlapping blocks were not analysed.

So these two particular versions of door (vii), the progression density increment and the plain entropy chain rule, are dominated by CRT majorants. No claim is made about general adaptive density-increment or entropy methods.

### 5.4 The blocking step, precisely

Beyond §5.2 the chain needs (R1) for the prime U family at ℓ with log ℓ ∈ [c√log N, (log N)/s_0]. There
B_ℓ has *model* density ℓ^{−C_V+o(1)} and period e^{(1+o(1))ℓ} ≫ N. Its actual density on I is what is to be
controlled, so it may not be assumed. By §§3–4, the input has to be
**(E-I)/(E-II) and sequence-specific**. Concretely it is the statement

> **(FL∞)** a fundamental lemma in sieve dimension κ ≍ log z at sifting level s = log N/log z ≪ κ, for the
> specific shift-aligned family. That is, the **non-square** sifted count is at most e^{O_s(1)} times its
> Mertens product. Squares must be removed: below s = 2C_V they alone exceed the Mertens product.

This is a known kind of open problem. No sieve method gives the order of magnitude when the dimension exceeds the
sifting level by a growing factor. Note that a terminal upper bound of this kind is neither a two-sided asymptotic
nor equivalent to step-wise (R1); it is what the chain would deliver. Selberg's upper bound for prime k-tuples loses 2^k k!, i.e. e^{O(k log k)},
and here k ≍ log z. That loss alone is z^{O(log log z)}, which swamps the saving z^{C_V}. *Assessment:* not provable
with present technology. No route in this lane produced a proof of any instance of (R1) beyond §5.2.

### 5.5 What is true numerically: Conjecture RLD-U

**Conjecture RLD-U (CONJECTURE; EVIDENCE in §2.3 and §7).** Let 𝓕_z be the prime-modulus U family on
I = {n ≤ N : n ≡ 1 (8)} with ℓ ≤ z. For every fixed s > 1 there is C(s) < ∞ such that for all N, with z = N^{1/s},

    #{n ∈ I : n ∉ □, n avoids 𝓕_z}  ≤  e^{C(s)} · #I · ∏_{ℓ≤z} (1 − w(ℓ)/ℓ).

Moreover C(s) → 0 as s → ∞.

Evidence: e^{C(s)} = e^{D_ns(s)} up to second-order terms. D_ns(s) does not grow over N = 10⁷, 10⁸, 10⁹ at any
tabulated s ∈ [1.25, 3] (§2.3; spread ≤ 0.08). Three scales are evidence, not proof. The values at s = 3, 2, 1.5, 1.25 are ≈ 0.005, 0.18, 0.68, 1.2. Falsifier: growth
of D_ns in N at fixed s, for instance at N = 10¹⁰, 10¹¹.

*Assessment of its status.* RLD-U is a clean, falsifiable, numerically tested statement. It is a sieve asymptotic
up to bounded factors, at a level beyond the sieve dimension. It is **not** a standard hypothesis, and it is not
visibly weaker than its consequence (§6). By z50 CONTEXT §1 it therefore counts as a conjecture, not as
progress. Its value is calibration. Off the squares, the integer chain tracks the Haar model up to a bounded factor
at every power level z = N^{1/s}, s > 1, as far as N = 10⁹, which is far beyond what any sieve proves. The only failure that grows with N is
the square floor of §2.1.

## 6. Consequences and exponents (conditional)

**Observation 6.0 (PROVED, trivial).** U holds at every n ≡ 5 (mod 8), n ≥ 5. Indeed c = 3 there, and the pair
v = 3 ∈ 8ℤ+3, A = 2 ≡ −1 (mod 3) satisfies A | n+3 and 1 < A < n+3. So all of U's content sits in the class
n ≡ 1 (mod 8), which is where every exception in the z49 census lies. That is why §§2, 7 work on
I = {n ≡ 1 (8)}. (The 4/n identity attached to this degenerate word was not examined; U is used here as defined
in z49 CONTEXT.)

**Corollary 6.1 (CONDITIONAL on Conjecture RLD-U at one s with 1 < s < 2C_V, and on the Titchmarsh-type
asymptotic Σ_{ℓ≤z} w(ℓ)/ℓ = (C_V + o(1)) log z).** Over U's domain n ≡ 1 (mod 4),

    #{n ≤ N : n ≡ 1 (4), U(n) fails}  =  #{odd squares ≤ N} + O(N^{1 − C_V/s + o(1)}).

The strict inequality s < 2C_V is exactly what makes the error term o(√N). This is Target 2 for U, conditionally.
With the empirical C_V ≈ 0.74 the admissible range is 1 < s < 1.48.

*Proof.* By Observation 6.0, an exception is either an odd square, or a non-square n ≡ 1 (8) that avoids every U
class, and in particular 𝓕_{N^{1/s}}. Since Σ w(ℓ)²/ℓ² < ∞ (w(ℓ) ≤ τ(ℓ+1)), the asymptotic gives
∏_{ℓ≤z}(1 − w(ℓ)/ℓ) = z^{−C_V+o(1)}. Apply RLD-U with z = N^{1/s}. ∎

The asymptotic for Σ w(ℓ)/ℓ is a Titchmarsh-divisor problem with divisors restricted to V. The standard
BV + Brun–Titchmarsh argument should give it (Assessment). The value C_V ≈ 0.74 is empirical, not a proved
constant. The conditional statement uses only the prime-modulus subfamily. The composite U classes, which carry
much more mass, are not needed. For comparison, the unconditional state of the art for U is
E_U(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}), proved in lane E (EXSET_I3 §7.3). That is optimal for CRT
majorants over the native class universe (EXSET_I3 Cor 7.1).

**Corollary 6.2 (CONDITIONAL on (RLD) with Σ η_i P(E_i) ≤ μ/2 and K ≤ 2, up to H = exp((log N)^α), α < 1).** Use
Theorem 1.3 and the cited model bounds. Δ is small in both cited families: the rough-edge family has Δ = o(1), and
the es-subexp Type II family has Δ ≪ L² = o(μ). Its moduli are rough, so its unit-Haar bound transfers to
ordinary Haar on [1,N].

| family (on I) | model −log P(Av) | exceptional set from RLD to α | beats current record iff | square floor forces RLD failure at (Cor 2.4) |
|---|---|---|---|---|
| prime U family, n ≡ 1 (8) | (C_V+o(1)) log z | N exp(−(C_V/2 + o(1))(log N)^α) | α > 2/3 (U record, lane E) | mass ½ log N, i.e. α → 1 |
| ES₅/U edge family, rough endpoints (I3 §8.4 route), n ≡ 1 (24) | ≥ cL²/(log L)² | N exp(−c(log N)^{2α}/(log log N)²) | α > 1/3 (U/ES₅ record 2/3) | log H ≍ √log N·log log N |
| ES Type II rough family (es-subexp `thm:haarlower`), [1,N] | ≥ cL³/log L | N exp(−c(log N)^{3α}/log log N) | α > 1/4 (ES record 3/4) | L ≍ (log N log log N)^{1/3} |

At the floor depths the logarithmic losses mean that the transferred bound is N^{1−c/(log log N)^{O(1)}}, not a
fixed power saving. Stepwise (RLD) for the prime U family with half-mass error at α = 1 is *not* the same
statement as the terminal Conjecture RLD-U, nor implied by it (review repair).

*Assessment.* For U/ES₅ the square floor sits where the transferred bound would reach N^{1/2+o(1)}; for ES it sits
where the forced-class family would reach the forced-class square floor. So (RLD) for these families can only be
asked up to the power-saving depth. Whether it holds there is open; nothing here shows it is "exactly as strong
as needed".

*Controls.*

* Odd squares: (RLD) fails there by Theorem 2.2. That is the T1 control, and the method passes it.
* Numerator 8: Theorem 1.3 is family-agnostic and only bounds survivors from above. For 8/n the exceptions
  11, 17, 131, 241 are finitely many, so no density statement is contradicted. The method proves nothing false
  for numerator 8. It also gives no pointwise statement, so FRONTIER §4 items 2–5 do not bind it.
* Hard primes (§7): 193, 2521, 3361, 66529 survive the whole prime-modulus U family at N = 10⁷ (ℓ ≤ 5·10⁶). The
  primes 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 8813281 are hit. So the prime-modulus
  family alone does not cover the known hard cases. That is consistent with an exceptional-set statement, which
  must allow survivors.

## 7. Numerics

All runs used `ulimit -v 8000000` and timeouts. The C sources are in `scripts/`; the outputs are in
`data/z50_ajopus/`.

### 7.1 Prime-modulus chain, exact (`scripts/z50_ajopus_chain.c`)

Usage: `chain N mode seed Lmax`. The program runs over I = {n ≤ N : n ≡ 1 (8)} with a byte array of size N/8.

* Primes ℓ ≤ Lmax are processed in increasing order, all classes at one prime forming one step; this is a Δ = 0
  chain.
* Classes are −v (mod ℓ) for v | ℓ+1 with v ≡ 0 (4) or v ≡ 7 (8). The proper-divisor condition is enforced: the
  element n = ℓ − v is skipped.
* Modes: 0 = U classes; 1 = random distinct nonzero classes; 2 = random quadratic non-residues; 3 = shift-aligned classes with
  v ≡ 1 (4) or 3 (8). Modes 1 and 2 use the same w(ℓ).
* Output per checkpoint: alive count, squares alive, model mass Σw/ℓ, Σρ_ℓ, the deficit, log model density
  Σlog(1−w/ℓ), log actual density, and D_ns (column 9). Column 9 subtracts the initial square count, so it is the
  non-square deficit only in modes 0 and 2, where squares are never killed. In modes 1 and 3 it is meaningless.

Runs at N = 10⁷, 10⁸, 10⁹ with Lmax = N/2 (mode 0 at N = 10⁷ used Lmax = 5·10⁶), each in seconds. The files
are `chain_U_N*.txt`, `chain_R_N*.txt`, `chain_M2_N1000000000.txt` and `chain_M3_N1000000000.txt`.

CERTIFIED facts:

* No square is ever hit by a U class (mode 0, all N). The program prints a warning on stderr for any such hit;
  none occurred.
* End states at N = 10⁹, ℓ ≤ 4.5·10⁸:
  - U: 20 742 survivors, of which 15 810 are squares. Model mass 12.95, Σρ = 8.48.
  - Random control: 221 survivors, mass 12.95, Σρ = 13.02.
  - QNR-random: 16 050 survivors (15 810 squares); final D_ns = 0.011, and max |D_ns| over checkpoints is 0.050.
  - Aligned non-U control (mode 3): total deviation from the model ranges over [−1.54, +0.49]; 597 survivors at
    the end.

EVIDENCE (the s-scaling table of §2.3):

* the non-square deficit is a function of s = log N/log ℓ alone, to ±0.02;
* it is ≤ 0.01 for s ≥ 2.8;
* it is bounded in N at each fixed s.

The model mass grows with slope C_V ≈ 0.74 in log ℓ: mass(1361) = 3.56, mass(1.17·10⁵) = 6.75,
mass(1.02·10⁷) = 10.07, mass(4.5·10⁸) = 12.95.

### 7.2 Composite moduli, model Monte Carlo, Janson bound (`scripts/z50_ajopus_janson.c`)

Usage: `janson N Amin Amax pmin samples seed`. Events are all U classes with modulus A ∈ [Amin, Amax] whose prime
factors are all ≥ pmin, ordered by A; for fixed A the divisors v come in enumeration order, not sorted. The integer chain runs on n ≡ 1 (8), n ≤ 10⁹. The model chain uses
Monte Carlo over independent prime-power coordinates, recording the first-hit index of each sample. μ, Δ (pairs
that share a bit and are compatible), max P and the maximal conflict sum are computed exactly. Files:
`janson_A*_p*.txt`.

| (Amin, Amax, pmin) | μ | Δ | max conflict | integer survival | model (MC) | exp(−μ) | exp(−μ+Δ) |
|---|---|---|---|---|---|---|---|
| (3, 3000, 3) | 9.07 | 12.10 | 4.09 | 2.15e−3 | 1.9e−3 (375 alive of 2e5) | 1.1e−4 | 20.5 |
| (11, 20000, 11) | 7.26 | 1.84 | 1.47 | 1.80e−3 | 1.6e−3 (635 of 4e5) | 7.0e−4 | 4.5e−3 |
| (29, 200000, 29) | 8.12 | 1.01 | 0.77 | 8.2e−4 | 5.3e−4 (105 of 2e5) | 3.0e−4 | 8.2e−4 |
| (3, 30000, 3) | 15.33 | 32.38 | 7.17 | 2.10e−4 | 6e−5 (25 of 4e5) | 2.2e−7 | 2.5e7 |

Monte Carlo relative standard error is ≈ 1/√(alive samples): about 5%, 4%, 10% and 20% in the four rows. The
(3, 3000, 3) row is `janson_A3_3000_p3.txt`.

Reading (EVIDENCE):

* With composite moduli, Janson's Δ is large unless the moduli are rough, as the S-model and es-subexp families
  arrange. exp(−μ+Δ) is then trivial.
* The local-lemma hypothesis (conflict sum ≤ 1/8) fails in all these unrestricted U families, because of the
  residue hubs (class −4 mod every A ≡ 3 (4); cf. (D)27).
* Integer and model chains agree to within 2.5% in −log survival while max A ≤ N^{0.4}, i.e. s ≥ 2.5.
  Integer survival exceeds the model by a factor 1.5–3.5 once A reaches N^{0.5}–N^{0.6}, matching §2.3.

### 7.3 Survivor structure (`scripts/z50_ajopus_cores.py`)

The U survivors at N = 10⁸, ℓ ≤ 10⁴ (s = 2) were dumped with `DUMP=file chain 100000000 0 1 10000` (mode 1 for the
control) and factored on a sample of 20 000.

| fraction with squarefree kernel ≤ K | K = 1 | 10² | 10⁴ | 10⁶ |
|---|---|---|---|---|
| U survivors | 5.69% | 5.73% | 6.45% | 15.35% |
| random control | 0.02% | 0.07% | 0.92% | 9.79% |
| uniform baseline | 0.03% | 0.10% | 0.82% | 8.07% |

Beyond the squares themselves, small-kernel near-squares km² are not enriched. The non-square deficit is not a
"soft square floor" of this kind.

## 8. Reviews

TBD.
