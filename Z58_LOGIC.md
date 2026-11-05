# Z58_LOGIC — logic and complexity of (MS)

Status: z58 lane LOGIC (brief `z52bbriefs/z58_lanes.md` §LOGIC, common rules `z52bbriefs/z53_depth.md`).
**Checkpoint 1.** Internal, not yet reviewed. **ES is OPEN; nothing here proves or disproves ES or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_logic_*`,
data `data/z58/logic/`. Literature checks: `data/z58/logic/lit_verify.md` (research subagent; verdicts quoted there).

## 0. Falsifier table (mandatory)

The "idea" of this lane is not a positivity mechanism but a set of logic/complexity theorems *about* (MS). The table
records how each theorem and the one new conjecture (MS⁺, §4) interact with the four screens.

| screen | behaviour |
|---|---|
| **F1 odd squares** | (MS⁺) excludes squares explicitly. Squareness is decidable in polynomial time and squares factor trivially, so they put no computational obligation on a feasible proof (Thm 3.1). T1 itself is a *universal* (Π₁) statement with a uniform proof (Jacobi reciprocity). The prime zeros have no known uniform reason (§6, Assessment). |
| **F2 C-even sub-line** | The logic theorems apply verbatim to R₈. In particular "R₈(p) ≥ 1 for 𝔐-primes p > P" is Π₁ and false at P = 10¹⁰ (CERTIFIED, Z57_SYNTH §2.1), so it is refutable in Robinson's Q (Prop 2.1(b)). No step of this memo distinguishes C odd from C even. The memo claims nothing that F2 would falsify, because it proves no positivity. |
| **F3 composites** | Sharpened by new data (§4, CERTIFIED to 10¹⁰). Among non-square composites in Mordell's classes (n mod 840 ∈ 𝔐) the zeros of R end at **17 401 609**: none in (1.75·10⁷, 10¹⁰]. The 285 composite zeros of F3 are overwhelmingly outside 𝔐, mostly divisible by 3, 5 or 7. In 𝔐 the composite mean of R/L² is 0.1189 against 0.1246 for primes on [10⁷, 10⁸]. So primality beyond non-squareness is *not* visibly used by (MS) above 2·10⁷: (MS⁺) is consistent with all data (EVIDENCE). Thm 3.1 says a feasible proof of (MS) must factor any composite zeros in 𝔐 above 10¹⁷; if (MS⁺) holds there are none. |
| **F4 known zeros** | Nothing here proves positivity. By Prop 2.1, a counterexample p to a Π₁ rung yields a refutation in Q of length p^{O(1)}. This is the logic reading of F4: the 14 (★)-zeros, 38 𝔊*-zeros and 12 R₈-zeros are explicit refutations of the corresponding rungs at thresholds below them. (MS⁺) has threshold 17 401 609, above every known non-square zero in 𝔐 (largest prime one 8 813 281). |

No HOT LEAD.

## 1. Precise statements

Language of bounded arithmetic (Buss): 0, S, +, ·, ≤, ⌊x/2⌋, |x|, #. Define

* Hit(n, d) :≡ 3 ≤ d ≤ 2n ∧ d ≡ 3 (mod 4) ∧ r ≥ 1 ∧ r | (d + 1)/4, where r := (−n mod d). This is a polynomial-time
  (PV) predicate; it is Δ^b_1 in S¹₂.
* Prime(n) :≡ n ≥ 2 ∧ ∀a ≤ n ∀b ≤ n (a·b = n → a = 1 ∨ b = 1). This is Π^b_1.
* Mord(n) :≡ n > 10¹⁷ ∧ (n mod 840) ∈ 𝔐, 𝔐 = {1, 121, 169, 289, 361, 529}. Polynomial time.
* Sq(n) :≡ ∃s ≤ n (s·s = n). Polynomial time (integer square root).

**(MS)** :≡ ∀n [Prime(n) ∧ Mord(n) → ∃d ≤ 2n Hit(n, d)].
**(MS⁺)** :≡ ∀n [Mord(n) ∧ ¬Sq(n) → ∃d ≤ 2n Hit(n, d)] (CONJECTURE, §4).

Lemma A.1 of Z57_SYNTH gives R(n) = #{d : Hit(n, d)} for every n ≥ 1. Hence (MS) is the brief's statement: necessarily
d ≤ (4n + 1)/3 ≤ 2n. (MS⁺) implies (MS).

## 2. (MS) as a Π₁ sentence (classical facts, stated precisely)

**Prop 2.1 (PROVED; standard).**
(a) (MS) is logically equivalent to the Π⁰₁ sentence ∀n θ(n), with θ(n) :≡ ¬Prime(n) ∨ ¬Mord(n) ∨ ∃d ≤ 2n Hit(n, d)
    (a Δ₀ formula; the equivalence is pure logic).
(b) If (MS) is false, its least counterexample p yields a proof of ¬(MS) in Robinson's Q. Its length is polynomial
    in p, and every theory T ⊇ Q proves ¬(MS).
(c) Hence, if T ⊇ Q is consistent and T ⊬ ¬(MS), then (MS) is true. In particular, (MS) independent of PA, or of ZFC,
    would imply (MS) true.
(d) The same holds for every rung of the Z57 ladder that has an explicit threshold: L2–L4, L3′, L3″ with P fixed.

*Proof.* (b) is Σ₁-completeness of Q applied to the true Δ₀ sentence ¬θ(p): Q decides every closed Δ₀ formula. The
proof checks all a, b ≤ p and all d ≤ 2p, which is polynomial in p (not in log p). (c) is the contrapositive of (b).
(d) is the same argument. ∎

*Remark (lengths).* A refutation from a counterexample p has length p^{O(1)}, not polylog(p): ¬θ(p) is a universal
claim over all d ≤ 2p. No shorter certificate of R(p) = 0 is known for prime p. The odd squares are different: the
uniform Jacobi argument (Z57_SYNTH Lemma A.1(b)) proves ∀m R(m²) = 0 at once.

**Prop 2.2 (arithmetical classification of the target family; PROVED, definitional).**
* (MS), L2–L4, L3′, L3″, L5 at fixed threshold P: Π⁰₁.
* Eventual forms "∃P ∀p > P …": Σ⁰₂. They are *not* covered by Prop 2.1(c); independence of a Σ₂ sentence gives no
  truth value.
* L6(η) "∀p ≥ p_V(η) …": Π⁰₁ if p_V(η) is an explicit number, Σ⁰₂ otherwise.
* ES itself: Π⁰₁ (all bounds on x, y, z are polynomial in n).

*Consequence (Assessment).* For the (★) route, only Π₁ statements with explicit threshold ≤ 10¹⁷ finish ES
(Z57_SYNTH §1.4). An analytic proof of an eventual Σ₂ form with an ineffective threshold would leave the target open,
in the way Siegel's theorem leaves effective class-number bounds open.

## 3. Witnessing: what a feasible proof of (MS) must compute

**Theorem 3.1 (PROVED relative to Buss's witnessing theorem for S¹₂).** Suppose S¹₂ ⊢ (MS). Then there is a
polynomial-time function f with the following property. For every n with Mord(n), either Hit(n, f(n)) holds, or
f(n) = ⟨a, b⟩ with a·b = n and 1 < a, b < n. In particular f factors, in polynomial time, every n with Mord(n) and
R(n) = 0. Since R(m²) = 0, this includes all odd squares in 𝔐 classes.

*Proof.* Inside S¹₂, (MS) is equivalent to ∀n ∃w ≤ t(n) ψ(n, w) for a suitable term t. Here
ψ(n, w) :≡ ¬Mord(n) ∨ (w = ⟨a, b⟩ ∧ a·b = n ∧ 1 < a < n) ∨ Hit(n, w).
Indeed ¬Prime(n) ↔ ∃a, b ≤ n (ab = n ∧ 1 < a < n) by pure logic, and pairing is S¹₂-definable. ψ is Σ^b_1; in fact
it is polynomial-time decidable. Buss's witnessing theorem: if S¹₂ ⊢ ∀x ∃y φ(x, y) with φ ∈ Σ^b_1, then some
polynomial-time f satisfies φ(x, f(x)) for all x. (Buss 1986; the standard statement is recorded in
`lit_verify.md` item 1 as PARTLY verified: consistent with the thesis, theorem number not re-read.) ∎

**Corollary 3.2 (PROVED, same reliance).** Let Z_C := {n : Mord(n), n composite, ¬Sq(n), R(n) = 0}. If S¹₂ ⊢ (MS),
then Z_C admits a polynomial-time factoring algorithm. Contrapositively: if Z_C contains an infinite polynomial-time
samplable set of hard-to-factor integers, then S¹₂ ⊬ (MS).

**How strong is this? (Assessment, made precise where possible.)**
* *Only low levels bite.* Put Q_MS := "given n, output a hit, a nontrivial factorisation, or ¬Mord(n)". Q_MS is in
  FP^NP whenever it is total. Binary search with the NP oracle "∃d ∈ [x, y] Hit(n, d)" finds a hit in O(log n)
  queries; the oracle "∃a ∈ [x, y], 1 < a < n, a | n" factors. Hence witnessing theorems that only give FP^{Σ^p_k},
  k ≥ 1 (S^{k+1}_2, Buss), carry no information beyond the truth of (MS). The Σ^b_1-conservation of S²₂ over T¹₂ gives a
  PLS bound for S²₂-proofs (Buss–Krajíček; `lit_verify.md` item 2, PARTLY verified). Factoring is not known to be in
  PLS, and is not known to be outside it.
* *The obligation is about Z_C, not about primality as such.* Since PRIMES ∈ P, the hypothesis Prime(n) could be
  replaced by the polynomial-time test AKS(n) = 1. Proving AKS correct needs more than S¹₂ as far as is known:
  Jalali–Ježil (arXiv:2504.17041, Forum Math. Sigma 14 (2026) e49; abstract checked) prove it in T₂^count. Doing so
  would not remove the obligation, which concerns only the composites with R = 0.
* *By §4, Z_C may well be finite.* Then the obligation is vacuous: a finite table suffices, and Theorem 3.1 is no
  barrier at all. Theorem 3.1 has teeth only if (MS⁺) fails infinitely often.

## 4. Census: composite zeros in Mordell's classes (CERTIFIED to 10¹⁰; EVIDENCE for the reading)

`scripts/z58_logic_zeros.c` is a bitset sieve over all triples. It marks every n ≡ 1 (4), n ≤ N, of the form
4uBC − u − B, and lists the unmarked ones. `scripts/z58_logic_classify.py` splits them into P / SQ / C and factors the
composites.

*Validation.* At N = 8·10⁶ the engine reproduces exactly the screen files. It finds 13 primes (the known ones
≤ 8·10⁶), 1 413 odd squares, and the 285 composites of `composite_zeros_le8e6.txt` (list equality checked).

**Census to N = 10¹⁰ (CERTIFIED: one exhaustive engine plus validation; `data/z58/logic/zeros_1e10_summary.txt`; full
zero list `zeros_1e10.txt.gz`).** The run took ≈ 15 min with a 312 MB bitset.

*Validation.*
* The 14 prime zeros it finds are exactly the certified (★) census to 10¹⁰ (FRONTIER §2.1; independent engines).
* Its non-square zeros n ≡ 1 (4) ≤ 4·10⁹ (458 ≤ 10⁹, 27 in (10⁹, 4·10⁹]) coincide exactly with the independent z52d gap
  census `data/z52b/pass2/ZF2/Z1018_gaps_1e9{,_4e9}.txt` (`BRAINSTORM/z52d_pass2_ZF2.md` Z1018). That census computed the
  gap set but did not split it by Mordell class. So the claim is double-engine to 4·10⁹ and single-engine on (4·10⁹, 10¹⁰].
* An independent divisor-enumeration decider, `scripts/z58_logic_check.py`, uses min(u, B, C) ≤ (n/4)^{1/3} + 1 and
  sympy divisors. It confirms R = 0 at all 42 composite zeros in [10⁹, 10¹⁰], at 17 401 609, 12 538 801 and 8 813 281,
  and R ≥ 1 at 150 random non-squares in 𝔐 classes in [10⁹, 10¹⁰].
* A bug producing *false hits* would be the dangerous direction for the "none" claim below. It would also have to
  spare all 14 + 285 + 1 413 validated zeros.

Per decade ⌊log₁₀ n⌋:

| decade | prime zeros | odd squares | composite zeros | …in 𝔐 classes | …semiprime pq | …least prime ≥ n^{1/3} |
|---|---|---|---|---|---|---|
| 10¹ | 0 | 3 | 1 | 0 | 1 | 0 |
| 10² | 2 | 11 | 8 | 0 | 2 | 0 |
| 10³ | 2 | 34 | 24 | 3 | 12 | 2 |
| 10⁴ | 2 | 108 | 60 | 3 | 10 | 2 |
| 10⁵ | 3 | 342 | 95 | 7 | 18 | 3 |
| 10⁶ | 5 | 1 081 | 111 | 3 | 6 | 1 |
| 10⁷ | 0 | 3 419 | 93 | 2 | 3 | 0 |
| 10⁸ | 0 | 10 811 | 52 | **0** | 1 | 0 |
| 10⁹ | 0 | 34 189 | 42 | **0** | 0 | 0 |

* The composite zeros in 𝔐 classes number 18 in total. The two largest are 12 538 801 = 11·47·79·307 and
  **17 401 609 = 47·370 247**. There are none in (1.75·10⁷, 10¹⁰].
* The prime zeros in 𝔐 end at 8 813 281.
* The "balanced" composite zeros (least prime factor ≥ n^{1/3}) end at 2 956 321 = 211·14 011.
* Composite zeros above 3·10⁷ are dominated by small factors.
  * Above 10⁸, every composite zero is divisible by 3, 5 or 7 (52 + 42 of them).
  * The composite zeros coprime to 105 above 10⁷ are just 12 538 801, 17 401 609 and 29 210 401 = 11·31·85 661 (to 10¹⁰); all 42 composite zeros in [10⁹, 10¹⁰] are divisible by 3, 5 or 7.
  Mechanism (PROVED, elementary): a hit d is coprime to n, because g | d and g | r | (d+1)/4 force g | 1. So 3 | n
  removes every d ≡ 0 (mod 3). Every n in an 𝔐 class is coprime to 105.

**Mean R/L² by class on n ≡ 1 (4), n ∈ [10⁷, 10⁸] (CERTIFIED counts, `means_1e8.txt`).**
* Primes: 0.1636 (2 548 324 n, 0 zeros).
* Primes in 𝔐: 0.1246 (158 955 n, 0 zeros).
* Composites in 𝔐: **0.1189** (482 339 n, 2 zeros).
* Composites with 3 | n: 0.0966 (82 zeros).
* Other composites: 0.1470 (9 zeros).

**CONJECTURE (MS⁺).** R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐.
* *Evidence.* There is no counterexample in (1.75·10⁷, 10¹⁰]. In 𝔐 the composite mean R/L² is within 5 % of the prime
  mean. Both the composite and the prime zeros in 𝔐 end below 2·10⁷.
* *Assessment.* Inside 𝔐, primality appears to enter (MS) only through non-squareness. This refines F3: the 285
  composites are a non-𝔐 small-n phenomenon, and the 𝔐-composite zeros end near 1.7·10⁷.
* *Consequences.*
  * An argument for (MS) at threshold 10¹⁰ is *not* falsified by working for all non-squares in 𝔐: no such
    composite zero is known above 1.75·10⁷.
  * The witnessing obligation of Thm 3.1 is then vacuous.
  * F1 (squares) is the only structural obstruction left in the 𝔐 domain.

## 5. Search complexity of witnesses (in progress)

**Lemma 5.1 (PROVED).** Let d_min(p) be the least d with Hit(p, d). Then d_min(p) ≥ n_p, the least quadratic
non-residue mod p.

*Proof.* Z57_SYNTH Lemma A.1(b): every element of H_d is a unit with Jacobi symbol (·/d) = −1. So a hit forces
(p/d) = −1, hence some prime ℓ | d with (p/ℓ) = −1. Here ℓ is odd because d is. Since p ≡ 1 (4), reciprocity gives
(ℓ/p) = −1, so d ≥ ℓ ≥ n_p. ∎

**Lemma 5.2 (PROVED, elementary).** For a prime p ≡ 1 (mod 4): p mod 840 ∈ 𝔐 ⟺ n_p ≥ 11.
*Proof.* With p ≡ 1 (4), reciprocity gives (ℓ/p) = (p/ℓ) for odd ℓ, and (2/p) = 1 ⟺ p ≡ 1 (8). So n_p ≥ 11 ⟺
p ≡ 1 (8) and p is a square mod 3, 5 and 7. This is exactly p mod 840 ∈ 𝔐: 𝔐 is the set of unit squares mod 840,
the squares of 1, 11, 13, 17, 19, 23. ∎

**Lemma 5.3 (PROVED, elementary).** d_min(p) ≥ W(p), where W(n) := min{M ≡ 3 (4) : n mod M ∈ 𝓡(M)} and
𝓡(M) := {−4D mod M : D | A_M²}, A_M = (M + 1)/4. These are the "multiplier witness" sets of `POINTWISE_OMEGA.md` §0.
*Proof.* H_d ⊆ 𝓡(d). Indeed, let k | A := (d + 1)/4 and put D := kA. Then D | A², and 4A ≡ 1 (mod d) gives
4D ≡ k, so −k ≡ −4D (mod d). ∎

*Consequences (PROVED modulo the cited Ω-results; not re-checked here).*
* `POINTWISE_OMEGA.md` Thm 5.1 (PROVED modulo one cited source): W(p) ≥ (log p)^{2−ε} for infinitely many primes in
  𝔐. Hence so is d_min(p).
* `POINTWISE_OMEGA13.md` Thm 5.1 (PROVED modulo Gallagher, Nair–Tenenbaum and OMEGA10 Thm 3.4): d_min(p) ≥
  exp(c(log p)^{1/4}(log log p)^{−1/4}) for infinitely many primes in 𝔐.
* Unconditionally (Lemma 5.1 + Lemma 5.2 + Graham–Ringrose, `lit_verify.md` item 9 PARTLY verified): d_min(p) ≫
  log p · log log log p i.o. in 𝔐.

**Reading: three search strategies (PROVED where labelled; EVIDENCE for the data).** A witness for (MS) at p can be
sought in three natural ways.
* (i) *Trial over d* (no factoring). The cost is ≍ d_min(p). By Lemma 5.3 it is superpolylogarithmic i.o. (modulo
  OMEGA13). There is no "d ≤ polylog" witness rule.
* (ii) *Levels C* (factor 4Cp + 1 for C = 1, 2, …, then a subset-product search mod 4C). The cost is C_min(p)
  factorisations.
* (iii) *Shifts u* (factor p + u for u = 1, 2, …, then look for a divisor ≡ −1 mod 4u). The cost is u_min(p)
  factorisations, where u_min(p) is the least remainder r over all hits.

Exhaustive data over all primes p ≡ 1 (4) ≤ 10⁹ (`scripts/z58_logic_minwit.c`, `minwit_1e9.txt`; zeros skipped).
The table gives the per-decade maxima over 𝔐 primes:

| decade | max d_min (at p) | max C_min (at p) | max u_min (at p) |
|---|---|---|---|
| 10⁴ | 2 383 (26 209) | 149 (26 209) | 26 (19 441) |
| 10⁵ | 64 255 (706 801) | 4 016 (706 801) | 131 (427 249) |
| 10⁶ | 60 759 (4 617 649) | 974 (6 116 401) | 410 (4 160 641) |
| 10⁷ | 2 953 943 (85 664 329) | 41 027 (85 664 329) | 469 (53 325 721) |
| 10⁸ | 2 741 075 (564 661 441) | ≥ 65 535 (capped; 564 661 441) | 241 (413 490 001) |

At sampled primes up to 10²¹ the shift search is tiny (`scripts/z58_logic_umin.py`, `umin_samples.txt`):
* 125 random 𝔐 primes at 10¹², 10¹⁵, 10¹⁸ have max u_min = 7, 4, 4 and mean ≈ 1.7;
* 70 square-mimicking primes p ≡ 1 (mod 8∏_{3≤ℓ≤y} ℓ), y = 29, 37, 43, at 10¹⁵, 10¹⁸, 10²¹ have max u_min = 4, 4, 6.
  These are quadratic residues mod every prime ≤ y, so n_p > y and d_min > y.

*Reading.*
* The cost of a witness is not its size. d_min and C_min reach p^{0.7}-ish and ≥ 6·10⁴ at the hardest primes ≤ 10⁹,
  and 564 661 441 is the last 𝔊*-zero.
* Yet u_min stays below 470: some p + u with tiny u almost always has a divisor in the right class. That divisor is
  typically a *large* prime factor of p + u, which is why d_min is large while u_min is small.

**CONJECTURE FQ_u(A).** u_min(p) ≤ (log p)^A for every prime p ∈ 𝔐 with R(p) ≥ 1. (Data: u_min ≤ 469 for every such p ≤ 10⁹.) FQ_u(A) together with (MS) puts the search problem in FP^{FACTOR}, hence in FBQP by Shor. This is
the (★) analogue of the CONJECTURE FQ of `BRAINSTORM/logic_complexity.md`. FQ_u with "for every prime p > P₀"
(R(p) ≥ 1 included) is itself a Π₁ strengthening of (MS) and has the same B2 status (Assessment).

**Prop 5.4 (PROVED, elementary): the classical cheap searches are table searches.** Suppose a hit has two of its
three coordinates bounded: u, B ≤ X, or u, C ≤ X, or B, C ≤ X. Then the hit is decided by p modulo a modulus ≤ 16X²:
* (u, C): d = 4uC − 1 ≤ 4X² and the test is p mod d ∈ H_d;
* (B, C): symmetric, with d′ = 4BC − 1 and r = B;
* (u, B): p ≡ −(u + B) (mod 4uB).

So a deterministic polynomial-time search that enumerates such pairs up to polylog(p) is a bounded-modulus table search.
For the (u, C) and (B, C) shapes, Lemma 5.3 shows it fails infinitely often (modulo OMEGA13). For (u, B) we did not
prove a Jacobi lemma; it is covered by B1/Theorem M only in the qualitative form of FRONTIER §3.

*Consequence for Thm 3.1 (Assessment).* An S¹₂ proof of (MS) would supply a classical polynomial-time search. It
could not be any of the table searches above, and the only efficient search we know (iii) needs factoring. So such a
proof would contain an unknown classical method for producing a divisor of some p + u, p + B or 4Cp + 1 in a
prescribed class. This is B2 in algorithmic dress: a precise sense in which (MS) has no "obvious" feasible proof. It
is not a non-provability theorem.

## 6. Barrier analogues

### 6.1 Pseudo-squares: (MS⁺) fails in a model of open induction (PROVED)

Shepherdson's model M (Shepherdson 1964; description and the facts used here as in
`BRAINSTORM/logic_weak_arithmetic.md` §1):
* M consists of the elements n = n₀ + Σ_{q>0} a_q t^q, with finitely many rational q > 0, a_q real algebraic and
  n₀ ∈ ℤ. Here t is positive infinite, and n > 0 iff its leading coefficient is positive.
* M ⊨ IOpen.
* Each finite set of elements lies in ℝ_alg[σ] for σ = t^{1/k}, some k. Evaluation at σ = 0 is the ring homomorphism
  n ↦ n₀ ∈ ℤ.
* Every nonstandard element of M is a product of two nonstandard elements (Shepherdson; reproved in
  `logic_weak_arithmetic.md` C2). Hence the primes (irreducibles) of M are the standard primes.

In M write (MS★) and (MS⁺★) for (MS) and (MS⁺) with the hit stated as a solution of (★): ∃u, B, C ≥ 1,
4uBC − u − B = n. Over ℕ the two forms are equivalent by Z57_SYNTH Lemma A.1.

**Lemma 6.1 (sign lemma for (★); PROVED).** Let n ∈ M with n(σ) > 0 for all real σ ≥ 0. If u, B, C ∈ M are ≥ 1 and
satisfy 4uBC − u − B = n, then u₀, B₀, C₀ ≥ 1 and 4u₀B₀C₀ − u₀ − B₀ = n₀. Hence R(n₀) ≥ 1.

*Proof.*
* Work in ℝ_alg[σ]. u, B, C are positive in M, so they have positive leading coefficients and are positive for
  large σ.
* Suppose uBC has a real zero σ ≥ 0, and let σ₁ be the largest one. On (σ₁, ∞) none of u, B, C vanishes, so all are
  positive there (IVT), and hence u(σ₁), B(σ₁), C(σ₁) ≥ 0.
  * If C(σ₁) = 0, then −u(σ₁) − B(σ₁) = n(σ₁) > 0, which is impossible.
  * If C(σ₁) > 0 and u(σ₁) = 0, then −B(σ₁) = n(σ₁) > 0, which is impossible. B(σ₁) = 0 is symmetric.
* So u, B, C > 0 on [0, ∞). In particular u₀, B₀, C₀ are positive integers. Apply the evaluation homomorphism. ∎

**Theorem 6.2 (PROVED, given Shepherdson's model).** Let n₀ ∈ ℕ with n₀ mod 840 ∈ 𝔐 and R(n₀) = 0, and put
n := n₀ + 840t ∈ M. Then M ⊨ Mord(n) ∧ ¬Sq(n) ∧ "n has no (★) solution". Consequently:
* (a) IOpen ⊬ (MS⁺★).
* (b) If (MS) is true, then M ⊨ IOpen + (MS★) + ¬(MS⁺★). So IOpen + (MS★) ⊬ (MS⁺★).
* (c) Every standard zero lifts to such a counterexample in M:
  * every odd square in 𝔐 classes, e.g. n₀ = 121 = 11² (T1);
  * every composite zero, e.g. 17 401 609;
  * every prime zero in 𝔐, e.g. 8 813 281 (8 813 281 mod 840 = 1).
  The lifts are reducible in M, so they never violate (MS★).

*Proof.*
* n > 10¹⁷ because t is infinite. Also n = 840t + n₀, so n mod 840 = n₀ mod 840 ∈ 𝔐.
* ¬Sq(n): suppose y² = n in M. In some ℝ_alg[σ] this reads y(σ)² = n₀ + 840σ^k. The right side has the simple
  roots of 840σ^k = −n₀ (n₀ ≠ 0, k ≥ 1), so it is not a square of a polynomial.
* n(σ) > 0 for σ ≥ 0, so Lemma 6.1 applies: a (★) solution in M would give R(n₀) ≥ 1, contradicting R(n₀) = 0.
* (a) follows because M ⊨ IOpen.
* (b): the primes of M are standard. For a standard prime p, every (★) solution in M has u, B, C ≤ p, hence is standard
  (ℤ is an initial segment of M). So M ⊨ (MS★) ⟺ ℕ ⊨ (MS★).
* (c): R(121) = 0 by T1, and the other listed zeros are CERTIFIED (§4). ∎

*What this says (Assessment).*
* The counterexample n = 121 + 840t is a **pseudo-square**: it is congruent to the square 121 modulo every standard
  modulus, but it is not a square.
* So any proof of (MS⁺) must use non-squareness in a way that congruence data cannot see. This is the model-theoretic
  form of the T1/B1 pairing: Theorem M at the profinite point 11² (FRONTIER §3 B1).
* Through (b), it also explains why the *prime* hypothesis is logically convenient in weak theories. M has no
  nonstandard primes, so (MS★) cannot fail there at a nonstandard element. (MS⁺), which data (§4) suggest is true and
  which is stronger over ℕ, is refuted in M.
* So "use non-squareness, not primality" (§4) is not free. In weak arithmetic, non-squareness is visible only through
  the archimedean / real-closure structure, never through residues.
* Open: does IOpen ⊬ (MS★)? This needs a model with nonstandard primes in which Lemma 6.1 still applies; it is the
  open question of `logic_weak_arithmetic.md` §5 transferred to (MS).

### 6.2 Natural proofs: no computational teeth (Assessment, with one PROVED fact)

* The natural-proofs barrier needs a pseudo-random family that no efficient test separates from the targets. For
  (MS) the targets are primes or non-squares, and both are polynomial-time decidable (AKS; integer square root).
* Hence a *computational* "large, constructive property" barrier cannot exist here. The property
  "prime, or non-square, in 𝔐 and > 1.75·10⁷" is polynomial-time and, by §4, plausibly implies R ≥ 1.
* The barrier therefore moves from computability to provability. Thm 3.1 is its feasible-proof form (a hit-or-factor
  algorithm), and Thm 6.2 its model-theoretic form (pseudo-squares).
* PROVED fact used: the property is polynomial-time decidable. Squareness via Newton's integer square root; primality
  by AKS.

### 6.3 Parity (EVIDENCE)

* Sieve arguments cannot tell primes from products of two primes of comparable size (Selberg's parity barrier;
  standard, not re-verified here).
* An argument for (MS) that only uses "n has no prime factor below n^θ" proves R(n) ≥ 1 for such rough n. By §4 it
  is falsified by the balanced semiprime zeros: 2 956 321 = 211·14 011 (θ ≈ 0.36) and 897 961 = 443·2 027 (θ ≈ 0.45).
* Both of these lie in 𝔐 classes (2 956 321 mod 840 = 361, 897 961 mod 840 = 1). Still, no composite zero of any shape
  occurs in 𝔐 above 1.75·10⁷ (to 10¹⁰).
* So the parity barrier, as a falsifier for (MS) at threshold 10¹⁰, has **no data support** above 1.75·10⁷. It remains
  a barrier for *methods* (sieve lower bounds cannot produce pointwise positivity at one n), not for the statement.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed / clarifying; one new conjecture with strong data (MS⁺); no HOT LEAD.**

What was proved:
* Prop 2.1–2.2: the Π₁/Σ₂ classification and its consequences. Independence of (MS) would imply its truth;
  counterexamples give refutations in Q of length p^{O(1)}; eventual forms are Σ₂.
* Thm 3.1 / Cor 3.2 (relative to Buss witnessing): an S¹₂ proof of (MS) yields a polynomial-time hit-or-factor
  algorithm, so it must factor every composite zero in 𝔐.
* Lemmas 5.1–5.3: d_min ≥ n_p, d_min ≥ W(p), and 𝔐 = {p ≡ 1 (4) : n_p ≥ 11}. Hence no polylog trial-d witness rule
  (modulo the cited Ω-results). Prop 5.4: every two-small-coordinate search is a bounded-modulus table search.
* Lemma 6.1 / Thm 6.2: the sign lemma for (★) in Shepherdson's model. IOpen ⊬ (MS⁺), and IOpen + (MS) ⊬ (MS⁺) if (MS)
  is true. The counterexamples are pseudo-squares n₀ + 840t over every standard zero n₀.

What was computed:
* Zero census of R over all n ≡ 1 (4) to 10¹⁰: double-engine to 4·10⁹, single engine plus an independent decider on
  samples beyond. No non-square zero in 𝔐 classes in (17 401 609, 10¹⁰].
* Mean R/L² of 𝔐 composites ≈ that of 𝔐 primes (0.119 vs 0.125).
* Least witnesses d_min, C_min, u_min over all primes ≤ 10⁹: u_min ≤ 469, while d_min and C_min are large. u_min ≤ 7
  at sampled primes up to 10²¹, square-mimicking ones included.

**Hard screens (FRONTIER §4).**
* T1 squares: (MS⁺) excludes them by hypothesis. The pseudo-square theorem shows non-squareness must be used
  non-locally.
* 8/131 / numerator 8: the logic results transfer verbatim to R₈. The R₈ analogue of (MS⁺) is false at 10¹⁰ (12 prime
  zeros), so (MS⁺) for R carries the full-family content; nothing here separates C odd from C even.
* Tied modulus (B2): untouched. FQ_u and Prop 5.4 restate it algorithmically.
* Fixed p: every statement here is at fixed p or a Π₁ sentence over p. No averaging is used.

**Proposed FRONTIER text** (do not edit FRONTIER here).
* §2.4 / §4 item F3:
  > *(z58 LOGIC.)* Inside Mordell's classes the composite zeros of R end at 17 401 609 = 47·370 247: there is no non-square
  > n ≡ 1 (4) with n mod 840 ∈ 𝔐 and R(n) = 0 in (17 401 609, 10¹⁰]. This is CERTIFIED, double-engine to 4·10⁹. The
  > 𝔐-composite mean R/L² is 0.119 against 0.125 for 𝔐 primes on [10⁷, 10⁸].
  > CONJECTURE (MS⁺): R(n) ≥ 1 for all non-square n > 17 401 609 in 𝔐 classes. It implies (MS), and it makes the
  > hypothesis decidable in polynomial time, without primality.
  > Caveat (PROVED): IOpen + (MS) ⊬ (MS⁺). The pseudo-squares 121 + 840t of Shepherdson's model are counterexamples.
  > So non-squareness must be used non-locally (`Z58_LOGIC.md` §§4, 6.1).
* §3 B1:
  > *(z58.)* d_min(p) ≥ W(p) (H_d ⊆ 𝓡(d)), so the trial-d witness search is superpolylog i.o. (modulo OMEGA13). An
  > S¹₂ proof of (MS) would give a polynomial-time hit-or-factor algorithm (Buss witnessing).
  > The only efficient search known is factor-based: u_min ≤ 469 for all primes ≤ 10⁹. FQ_u ⟹ search ∈ FP^FACTOR.

**Bottom line.** (MS) is a Π₁ sentence. If it is independent it is true; this is cold comfort, and no natural
number-theoretic Π₁ independence is known to us. Logic does not find a shortcut. It sharpens three things.
* The primality hypothesis looks dispensable in Mordell's classes. Composites there behave like primes, and their last
  zero is 17 401 609, so the target can be posed as the polynomial-time-hypothesis statement (MS⁺).
* What is *not* dispensable is a non-local use of non-squareness. Open induction cannot exclude pseudo-squares.
* Any feasible proof would have to contain a classical algorithm producing a divisor of some p + u (or 4Cp + 1) in a
  prescribed class, beyond every bounded table search. Empirically such divisors are abundant at tiny u, so the
  obstacle is B2 itself, now stated as a search problem in FP^{FACTOR} (conditionally) but not known in FP.
