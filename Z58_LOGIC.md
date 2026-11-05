# Z58_LOGIC — logic and complexity of (MS). Verdict: narrowed; new CONJECTURE (MS⁺) (no non-square zero in Mordell classes in (1.75·10⁷, 10¹⁰]); no HOT LEAD

Status: z58 lane LOGIC (brief `z52bbriefs/z58_lanes.md` §LOGIC, common rules `z52bbriefs/z53_depth.md`).
**Final (after one hostile internal review, `data/z58/logic/internal_review.md`, 4 MAJOR + 11 MINOR, all applied; §8).**
Internal only. **ES is OPEN; nothing here proves or disproves ES or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_logic_*`,
data `data/z58/logic/`. Literature checks: `data/z58/logic/lit_verify.md` (research subagent; verdicts quoted there).

## 0. Falsifier table (mandatory)

The "idea" of this lane is not a positivity mechanism but a set of logic/complexity theorems *about* (MS). The table
records how each theorem and the one new conjecture (MS⁺, §4) interact with the four screens.

| screen | behaviour |
|---|---|
| **F1 odd squares** | (MS⁺) excludes squares explicitly. Squareness is decidable in polynomial time and squares factor trivially, so they put no computational obligation on a feasible proof (Thm 3.1). T1 itself is a *universal* (Π₁) statement with a uniform proof (Jacobi reciprocity). The prime zeros have no known uniform reason (§2 Remark, Assessment). The step that uses non-squareness must go beyond IOpen plus residues: the pseudo-squares n₀ + 840t of Thm 6.2 defeat it. |
| **F2 C-even sub-line** | The logic theorems apply verbatim to R₈. In particular "R₈(p) ≥ 1 for 𝔐-primes p > P" is Π₁ and false at P = 10¹⁰ (CERTIFIED, Z57_SYNTH §2.1), so it is refutable in Robinson's Q (Prop 2.1(b)). No step of this memo distinguishes C odd from C even. The memo claims nothing that F2 would falsify, because it proves no positivity. |
| **F3 composites** | Sharpened by new data (§4, CERTIFIED to 10¹⁰). Among non-square composites in Mordell's classes (n mod 840 ∈ 𝔐) the last zero of R within the census is **17 401 609**: none in (1.75·10⁷, 10¹⁰]. The 285 composite zeros of F3 lie predominantly outside 𝔐 (270/285; 15 are small in-domain zeros), and most are divisible by 3, 5 or 7. In 𝔐 the non-square composite mean of R/L² is 0.1189 against 0.1246 for primes on [10⁷, 10⁸]. So, within the data, primality beyond non-squareness is *not* visibly needed by (MS) above 2·10⁷: (MS⁺) is consistent with all data (EVIDENCE). Thm 3.1 says a feasible proof of (MS) must factor any composite zeros in 𝔐 above 10¹⁷; if (MS⁺) holds there are none. It must still find hits in polynomial time. |
| **F4 known zeros** | Nothing here proves positivity. By Prop 2.1, a counterexample p to a Π₁ rung yields a refutation in Q of length p^{O(1)}. This is the logic reading of F4: the 14 (★)-zeros, 38 𝔊*-zeros and 12 R₈-zeros (9, 20 and 4 of them in 𝔐) are explicit refutations of the corresponding rungs at thresholds below them; for the 𝔐-restricted rungs only the in-𝔐 ones count. (MS⁺) has threshold 17 401 609, above every known non-square zero in 𝔐 (largest prime one 8 813 281). |

No HOT LEAD.

## 1. Precise statements

Language of bounded arithmetic (Buss): 0, S, +, ·, ≤, ⌊x/2⌋, |x|, #. Define

* Hit(n, d) :≡ 3 ≤ d ≤ 2n ∧ d ≡ 3 (mod 4) ∧ r ≥ 1 ∧ r | (d + 1)/4, where r := (−n mod d). This is a polynomial-time
  (PV) predicate; it is Δ^b_1 in S¹₂.
* Prime(n) :≡ n ≥ 2 ∧ ∀a ≤ n ∀b ≤ n (a·b = n → a = 1 ∨ b = 1). This is Π^b_1.
* MClass(n) :≡ (n mod 840) ∈ 𝔐, 𝔐 = {1, 121, 169, 289, 361, 529}, and Mord(n) :≡ n > 10¹⁷ ∧ MClass(n). Both are
  polynomial time. In weak theories "n mod 840" is read through the quotient/remainder formula.
* Sq(n) :≡ ∃s ≤ n (s·s = n). Polynomial time (integer square root).

**(MS)** :≡ ∀n [Prime(n) ∧ Mord(n) → ∃d ≤ 2n Hit(n, d)].
**(MS⁺(P))** :≡ ∀n [MClass(n) ∧ n > P ∧ ¬Sq(n) → ∃d ≤ 2n Hit(n, d)], for a numeral P. The CONJECTURE of §4 is
(MS⁺) := (MS⁺(17 401 609)). Note that (MS⁺(P)) ⟹ (MS) only for P ≤ 10¹⁷. (MS⁺(10¹⁷)) is the version used in §§3, 6.

Lemma A.1 of Z57_SYNTH gives R(n) = #{d : Hit(n, d)} for every n ≥ 1. Hence (MS) is the brief's statement: necessarily
d ≤ (4n + 1)/3 ≤ 2n. (MS⁺) implies (MS) directly, since 17 401 609 < 10¹⁷.

## 2. (MS) as a Π₁ sentence (classical facts, stated precisely)

**Prop 2.1 (PROVED; standard).**
(a) (MS) is logically equivalent to the Π⁰₁ sentence ∀n θ(n), with θ(n) :≡ ¬Prime(n) ∨ ¬Mord(n) ∨ ∃d ≤ 2n Hit(n, d)
    (a Δ₀ formula once remainder and divisibility are expanded into bounded formulas of the ordinary language
    0, S, +, ·, ≤ of Q; the equivalence is pure logic).
(b) If (MS) is false, its least counterexample p yields a proof of ¬(MS) in Robinson's Q. Its length is polynomial
    in p, and every theory T ⊇ Q proves ¬(MS).
(c) Hence, if T ⊇ Q and T ⊬ ¬(MS), then (MS) is true (consistency of T is not even needed). In particular, (MS) independent of PA, or of ZFC,
    would imply (MS) true.
(d) The same holds for every rung of the Z57 ladder that has an explicit threshold: L2–L4, L3′, L3″ with P fixed.

*Proof.* (b) is Σ₁-completeness of Q applied to the true Δ₀ sentence ¬θ(p): Q decides every closed Δ₀ formula. The
proof checks all a, b ≤ p and all d ≤ 2p, which is polynomial in p (not in log p). (c) is the contrapositive of (b).
(d) is the same argument. ∎

*Remark (lengths).* The brute-force refutation from a counterexample p has length p^{O(1)}: ¬θ(p) is a universal
claim over all d ≤ 2p. No general polylogarithmic construction is known; this is not a proved lower bound on refutation
length. The odd squares are different: the
uniform Jacobi argument (Z57_SYNTH Lemma A.1(b)) proves ∀m R(m²) = 0 at once.

**Prop 2.2 (arithmetical classification of the target family; PROVED, definitional).**
* (MS), L2–L4, L3′, L3″ at a fixed numeral threshold P: Π⁰₁. L5 likewise, for a specified rational ε (M_𝔊* is a finite
  sum of character values; the comparison is decidable).
* Eventual forms "∃P ∀p > P …": Σ⁰₂. They are *not* covered by Prop 2.1(c); independence of a Σ₂ sentence gives no
  truth value.
* L6(η) "∀p ≥ p_V(η): X(p) ≥ −(c_V − η)L²", for a specified rational η and an explicit numeral p_V(η): Π⁰₁. A
  non-strict inequality between computable reals is Π⁰₁: quantify universally over a certified approximation precision
  together with p. "Σ⁰₂ otherwise" refers to the *existential-threshold formulation* ∃P ∀p ≥ P; a fixed but unknown
  numeral does not change the syntactic class.
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
Indeed, for n ≥ 2 (guaranteed by Mord(n)), ¬Prime(n) ↔ ∃a, b ≤ n (ab = n ∧ 1 < a < n); this uses elementary
arithmetic available in S¹₂. Pairing is S¹₂-definable with ⟨a, b⟩ ≤ (a + b + 1)², so t(n) := (2n + 1)² suffices.
Use a tagged witness (tag 0: hit d; tag 1: pair ⟨a, b⟩) with bounded decoding. ψ is Σ^b_1; in fact it is
polynomial-time decidable. Buss's witnessing theorem: if S¹₂ ⊢ ∀x ∃y φ(x, y) with φ ∈ Σ^b_1, then some
polynomial-time f satisfies φ(x, f(x)) for all x. (Buss 1986. The standard statement is recorded in `lit_verify.md`
item 1 as PARTLY verified: consistent with the thesis, theorem number not re-read.) The output is a nontrivial factor
pair, not a complete factorisation. ∎

**Corollary 3.2 (PROVED, same reliance).** Let Z_C := {n : Mord(n), n composite, ¬Sq(n), R(n) = 0}. If S¹₂ ⊢ (MS),
then some polynomial-time algorithm outputs a nontrivial factor pair of every element of Z_C ∩ (10¹⁷, ∞).
Contrapositively: if no polynomial-time algorithm correctly splits every element of some subset of
Z_C ∩ (10¹⁷, ∞), then S¹₂ ⊬ (MS). (Samplability is not needed for this worst-case form.)

**How strong is this? (Assessment, made precise where possible.)**
* *Only low levels bite.* Put Q_MS := "given n, output a hit, a nontrivial factorisation, or ¬Mord(n)". Q_MS is in
  FP^NP whenever it is total. Binary search with the NP oracle "∃d ∈ [x, y] Hit(n, d)" finds a hit in O(log n)
  queries; the oracle "∃a ∈ [x, y], 1 < a < n, a | n" factors. Hence witnessing theorems that only give FP^{Σ^p_k},
  k ≥ 1 (S^{k+1}_2, Buss), carry no information beyond the truth of (MS). Sharper for S²₂: S₂^{i+1} is ∀Σ^b_{i+1}-conservative over T₂^i
  (Buss, *Axiomatizations and conservation results for fragments of bounded arithmetic*, Thm 5). T¹₂'s Σ^b_1 search
  problems are polynomial-time projections/reductions of PLS problems (Buss–Krajíček, *An application of Boolean
  complexity to separation problems in bounded arithmetic*, Thm 5.3). Both theorem numbers were verified by the
  internal reviewer from the author PDFs (§8). So S²₂ ⊢ (MS) puts hit-or-factor in PLS (via such a reduction). Factoring is not known to be in
  PLS, and is not known to be outside it.
* *The obligation is about Z_C, not about primality as such.* Since PRIMES ∈ P, the hypothesis Prime(n) could be
  replaced by the polynomial-time test AKS(n) = 1. AKS correctness is proved in T₂^count (= VTC⁰₂, the first-order
  consequences of VTC⁰ with smash) by Jalali–Ježil (arXiv:2504.17041v2, Forum Math. Sigma 14 (2026) e49; abstract
  checked). Their introduction notes that an S¹₂ proof of AKS correctness would yield polynomial-time factoring. Doing so
  would not remove the obligation, which concerns only the composites with R = 0.
* *By §4, Z_C may well be finite.* Then the factoring-on-Z_C obstruction disappears: a finite table handles the
  no-hit composite branch. The separate requirement remains: an S¹₂ proof still yields a polynomial-time *hit finder*
  on primes, and existence of hits does not supply one. On that requirement see §5.

## 4. Census: composite zeros in Mordell's classes (CERTIFIED to 10¹⁰; EVIDENCE for the reading)

`scripts/z58_logic_zeros.c` is a bitset sieve over all triples. It marks every n ≡ 1 (4), n ≤ N, of the form
4uBC − u − B, and lists the unmarked ones. `scripts/z58_logic_classify.py` splits them into P / SQ / C and factors the
composites.

*Validation.* At N = 8·10⁶ the engine reproduces exactly the screen files. It finds 13 primes (the known ones
≤ 8·10⁶), 1 413 odd squares, and the 285 composites of `composite_zeros_le8e6.txt` (list equality checked).

**Census to N = 10¹⁰ (CERTIFIED: one exhaustive engine plus validation; `data/z58/logic/zeros_1e10_summary.txt`; full
zero list `zeros_1e10.txt.gz`).** The run took ≈ 15 min with a 312 MB bitset. The engine lists the zeros with
5 ≤ n ≤ 10¹⁰, n ≡ 1 (4); n = 1 (a square zero) is omitted, which affects no non-square count.

*Validation.*
* The 14 prime zeros it finds are exactly the certified (★) census to 10¹⁰ (FRONTIER §2.1; independent engines).
* Its non-square zeros n ≡ 1 (4) ≤ 4·10⁹ (458 ≤ 10⁹, 27 in (10⁹, 4·10⁹]) coincide exactly with the z52d gap
  census `data/z52b/pass2/ZF2/Z1018_gaps_1e9{,_4e9}.txt` (`BRAINSTORM/z52d_pass2_ZF2.md` Z1018). That census computed the
  gap set but did not split it by Mordell class. Z1018 is a second *implementation* of the same triple/arithmetic-progression enumeration, not a different algorithm.
  So the claim is double-implementation to 4·10⁹ and single-engine on (4·10⁹, 10¹⁰].
* A genuinely different algorithm, the divisor-enumeration decider `scripts/z58_logic_check.py`, uses min(u, B, C) ≤ (n/4)^{1/3} + 1 and
  sympy divisors. It confirms R = 0 at all 42 composite zeros in [10⁹, 10¹⁰], at 17 401 609, 12 538 801 and 8 813 281,
  and R ≥ 1 at 150 random non-squares in 𝔐 classes in [10⁹, 10¹⁰]. The original 150 inputs were not archived; the
  reviewer reran an independent 150-sample control with all hits (§8). This checks only the inputs tested.
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

* The composite zeros in 𝔐 classes number 18 in total: 1969, 2641, 5161, 18001, 23881, 90889, 112849, 199369,
  345361, 349609, 510169, 539281, 897961, 2956321, 3210601, 8725201, 12538801, 17401609. The two largest are 12 538 801 = 11·47·79·307 and
  **17 401 609 = 47·370 247**. There are none in (1.75·10⁷, 10¹⁰].
* The prime zeros in 𝔐 end at 8 813 281 (within the census to 10¹⁰).
* The "balanced" composite zeros (least prime factor ≥ n^{1/3}) end at 2 956 321 = 211·14 011 (within the census).
* Composite zeros above 3·10⁷ are dominated by small factors.
  * Above 10⁸, every composite zero is divisible by 3, 5 or 7 (52 + 42 of them).
  * The composite zeros coprime to 105 above 10⁷ are just 12 538 801, 17 401 609 and 29 210 401 = 11·31·85 661 (to 10¹⁰); all 42 composite zeros in [10⁹, 10¹⁰] are divisible by 3, 5 or 7.
  Mechanism (PROVED, elementary): a hit d is coprime to n, because g | d and g | r | (d+1)/4 force g | 1. So 3 | n
  removes every d ≡ 0 (mod 3). Every n in an 𝔐 class is coprime to 105.

**Mean R/L² by class on n ≡ 1 (4), n ∈ [10⁷, 10⁸] (CERTIFIED counts, `means_1e8.txt`).**
* Primes: 0.1636 (2 548 324 n, 0 zeros).
* Primes in 𝔐: 0.1246 (158 955 n, 0 zeros).
* Non-square composites in 𝔐: **0.1189** (482 339 n, 2 zeros).
* Non-square composites with 3 | n (outside 𝔐): 0.0966 (82 zeros).
* Other non-square composites: 0.1470 (9 zeros).
* R never reached the uint16 cap here (max R = 292 at N = 10⁸, reviewer instrumentation).

**CONJECTURE (MS⁺) = (MS⁺(17 401 609)).** R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐.
* *Evidence.* There is no counterexample in (1.75·10⁷, 10¹⁰]. In 𝔐 the composite mean R/L² is within 5 % of the prime
  mean. Both the composite and the prime zeros in 𝔐 end below 2·10⁷.
* *Assessment.* Inside 𝔐, primality appears to enter (MS) only through non-squareness. This refines F3: the 285
  composites lie predominantly outside 𝔐 (270/285), with 15 small in-domain zeros. Within the census to 10¹⁰ the
  𝔐-composite zeros end at 17 401 609.
* *Consequences.*
  * An argument for (MS) at threshold 10¹⁰ is *not* falsified by working for all non-squares in 𝔐: no such
    composite zero is known above 1.75·10⁷.
  * The factoring-on-Z_C part of Thm 3.1 is then vacuous. The hit-finding part is not.
  * Within the census, F1 (squares) is the only observed obstruction in the 𝔐 domain above the conjectured cutoff.

## 5. Search complexity of witnesses

**Lemma 5.1 (PROVED).** For a prime p ≡ 1 (mod 4) let d_min(p) be the least d with Hit(p, d) (+∞ if there is none).
Then d_min(p) ≥ n_p, the least quadratic non-residue mod p.

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

*Consequences (PROVED modulo the cited Ω-results, with their dependencies). The internal reviewer checked that the
cited W and "hard" (= Mordell-class) definitions match. The cited constructions do not prove that hits exist at
their primes; with d_min = +∞ for no hit, the bounds hold either way.*
* `POINTWISE_OMEGA.md` Thm 5.1 (PROVED modulo one cited source): W(p) ≥ (log p)^{2−ε} for infinitely many primes in
  𝔐. Hence so is d_min(p).
* `POINTWISE_OMEGA13.md` Thm 5.1 (PROVED modulo Gallagher, Nair–Tenenbaum and OMEGA10 Thm 3.4): d_min(p) ≥
  exp(c(log p)^{1/4}(log log p)^{−1/4}) for infinitely many primes in 𝔐.
* Unconditional except for the cited proposition: d_min(p) ≫ log p · log log log p for infinitely many p in 𝔐. Use
  Lemma 5.1 with Lau–Wu, Int. J. Number Theory 4 (2008), Prop 5.1. This is Graham–Ringrose's method, *restricted to
  p ≡ 1 (4)*, as used in `POINTWISE_OMEGA.md` Thm 8.5; Lemma 5.2 places those primes in 𝔐.

**Reading: three search strategies (PROVED where labelled; EVIDENCE for the data).** A witness for (MS) at p can be
sought in three natural ways.
* (i) *Trial over d* (no factoring). The number of trial values is ≍ d_min(p)/4; the bit cost carries an extra
  poly(log p) factor. By Lemma 5.3 the number of trials is superpolylogarithmic i.o., modulo OMEGA13. There is no
  "d ≤ polylog" witness rule, modulo the same dependency.
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
| 10⁸ | 2 741 075 (564 661 441) | ≥ 65 535 (capped; exact value 76 141 at 564 661 441, reviewer enumeration) | 241 (413 490 001) |

At sampled (probable) primes in decades through [10²¹, 10²²) the shift search is tiny (`scripts/z58_logic_umin.py`, `umin_samples.txt`):
* 125 random 𝔐 primes in the decades starting at 10¹², 10¹⁵, 10¹⁸ have max u_min = 7, 4, 4 and mean ≈ 1.7;
* 70 square-mimicking primes p ≡ 1 (mod 8∏_{3≤ℓ≤y} ℓ), y = 29, 37, 43, at 10¹⁵, 10¹⁸, 10²¹ have max u_min = 4, 4, 6.
  These are quadratic residues mod every prime ≤ y, so n_p > y and d_min > y.

*Reading.*
* The cost of a witness is not its size. d_min and C_min reach p^{0.7}-ish and ≥ 6·10⁴ at the hardest primes ≤ 10⁹,
  and 564 661 441 is the last 𝔊*-zero.
* Yet u_min stays below 470: some p + u with tiny u almost always has a divisor in the right class. That divisor is
  typically a *large* prime factor of p + u, which is why d_min is large while u_min is small.

**CONJECTURE FQ_u(A).** u_min(p) ≤ (log p)^A for every prime p ∈ 𝔐 with R(p) ≥ 1. (Data: u_min ≤ 469 for every such
p ≤ 10⁹.)

**Prop 5.5 (PROVED).** (MS) + FQ_u(A) put the hit-or-factor search on Mord inputs in FP^{FACTOR}, hence in FBQP by
Shor.
*Proof.* On composite n the oracle returns a factor pair directly. On prime p, for u = 1, 2, … ≤ (log p)^A, obtain the
prime factorisation of p + u from the oracle. Run a dynamic programme over the 4u residue classes mod 4u: process the
prime powers one prime at a time (choice of exponent 0…e), keep for each reachable class one backpointer, and test
whether the class −1 is reachable. There are O(log p) prime-power choices in total, so each u costs poly(u, log p);
the divisor list is never enumerated. Backpointers reconstruct d ≡ −1 (mod 4u), d | p + u, and d ≥ 4u − 1 is automatic.
By FQ_u some u ≤ (log p)^A succeeds. ∎
(The sampling script uses `sympy.divisors` for convenience; that is not the polynomial algorithm.) This is conditional
oracle efficiency, not a proved classical efficient search.
This is the (★) analogue of the CONJECTURE FQ of `BRAINSTORM/logic_complexity.md`. The form "for every prime p ∈ 𝔐
with p > P₀, u_min(p) ≤ (log p)^A" (R(p) ≥ 1 included) is a Π₁ strengthening of (MS) when P₀ ≤ 10¹⁷. It has the same
B2 status (Assessment).

**Prop 5.4 (PROVED, elementary): the classical cheap searches are table searches.** Suppose a hit has two of its
three coordinates bounded: u, B ≤ X, or u, C ≤ X, or B, C ≤ X. Then the hit is decided by p modulo a modulus ≤ 16X²:
* (u, C): d = 4uC − 1 ≤ 4X² and the test for these specified coordinates is p ≡ −u (mod d). (Membership
  p mod d ∈ H_d only says that *some* hit with this d exists: p = 5, u = 1, C = 2 gives d = 7 and 5 mod 7 ∈ H₇, but
  the actual hit is u = 2, C = 1.)
* (B, C): symmetric, with d′ = 4BC − 1 and the test p ≡ −B (mod d′);
* (u, B): p ≡ −(u + B) (mod 4uB).

What this excludes (PROVED modulo OMEGA13 for the first item):
* Exhaustive searches with both u, C (or both B, C) bounded by polylog(p) fail infinitely often. Such a hit has
  d = 4uC − 1 ≤ polylog(p), against Lemma 5.3.
* Fixed finite (u, B) menus fail by B1 (FRONTIER §3).
* *Growing* polylogarithmic (u, B) menus are **not** excluded here: C and d can be large. Excluding them would need a
  new size-controlled theorem.

*Consequence for Thm 3.1 (Assessment).* An S¹₂ proof of (MS) would supply a classical polynomial-time hit finder.
* It could not be an exhaustive (u, C) or (B, C) search with polylog bounds.
* It could be a growing (u, B) menu only if such menus succeed, which is open.
* The only candidate efficient search we know, (iii), needs a factoring oracle, and it is polynomial only
  CONDITIONALLY on (MS) + FQ_u(A) (Prop 5.5). The finite bound u_min ≤ 469 is EVIDENCE, not that theorem.

So such a proof would contain a classical method for producing a divisor of some p + u, p + B or 4Cp + 1 in a
prescribed class, beyond the excluded table searches. This is B2 in algorithmic dress. It is not a non-provability
theorem.

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
n := n₀ + 840t ∈ M. Then M ⊨ Mord(n) ∧ ¬Sq(n) ∧ "n has no (★) solution". Consequently, for every numeral P,
writing (MS⁺★(P)) for the starred form of (MS⁺(P)):
* (a) IOpen ⊬ (MS⁺★(P)) (unconditionally).
* (b) CONDITIONAL on the truth of (MS): M ⊨ IOpen + (MS★) + ¬(MS⁺★(P)), so IOpen + (MS★) ⊬ (MS⁺★(P)). (The
  hypothesis is essential: if (MS) were false, IOpen + (MS★) would be inconsistent and prove everything.)
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
* (b): the primes of M are standard. For a standard prime p, every (★) solution in M has u, B, C ≤ p, hence is
  standard: p + B = u(4BC − 1) ≥ 3u and p + u ≥ 3B give u + B ≤ p, and p + B ≥ 4C − 1 bounds C. The standard
  nonnegative integers form an initial segment of M's nonnegative cone. So M ⊨ (MS★) ⟺ ℕ ⊨ (MS★).
* (c): R(121) = 0 by T1, and the other listed zeros are CERTIFIED (§4). ∎

**Remark 6.3 (PROVED; the starred and Hit forms agree in IOpen).** In any discretely ordered ring with division
with remainder (so in every model of IOpen), ∃u, B, C ≥ 1 (4uBC − u − B = n) ⟺ ∃d ≤ 2n Hit(n, d) for n ≥ 1.
* (⇒) Put d := 4uC − 1 and r := u. Then n + r = Bd and 1 ≤ u ≤ (d + 1)/4 < d, so r is the remainder of −n mod d, and
  r | (d + 1)/4 = uC. From n = Bd − u ≥ d − (d + 1)/4 we get 3d ≤ 4n + 1 ≤ 6n, so d ≤ 2n.
* (⇐) Given the remainder r and the divisibility witnesses, put u := r, C := (d + 1)/(4r), B := (n + r)/d.
So Theorem 6.2 transfers to the Hit forms (MS), (MS⁺(P)): IOpen ⊬ (MS⁺(P)), and, CONDITIONAL on the truth of (MS),
IOpen + (MS) ⊬ (MS⁺(P)). The stars are kept in summaries for transparency. (Calculation supplied by the cross-model
review, §8.)

*What this says (Assessment).*
* The counterexample n = 121 + 840t is a **pseudo-square**: it is congruent to the square 121 modulo every standard
  modulus, but it is not a square.
* These particular pseudo-squares are indistinguishable from their square constant term by every standard-modulus
  residue test, and they defeat IOpen. A proof of (MS⁺) therefore needs arithmetic strength or information beyond
  IOpen together with residues. This is the model-theoretic
  form of the T1/B1 pairing: Theorem M at the profinite point 11² (FRONTIER §3 B1).
* Through (b), it also explains why the *prime* hypothesis is logically convenient in weak theories. M has no
  nonstandard primes, so (MS★) cannot fail there at a nonstandard element. (MS⁺), which data (§4) suggest is true and
  which is stronger over ℕ, is refuted in M.
* So "use non-squareness, not primality" (§4) is not free. Many non-squares are detected by one residue, but the
  hard ones (in 𝔐, square modulo many small primes) are exactly those for which residues say nothing. This one model
  does not classify all proof methods.
* Open: does IOpen ⊬ (MS★)? This needs a model with nonstandard primes in which Lemma 6.1 still applies; it is the
  open question of `logic_weak_arithmetic.md` §5 transferred to (MS).

### 6.2 Natural proofs (Assessment)

* The square-versus-non-square and prime-versus-composite distinctions are polynomial-time decidable (integer square
  root; AKS). So these input classes alone do not supply an indistinguishability barrier of the natural-proofs kind.
* No natural-proofs theorem, positive or negative, is established here. Recognising the promise of an input is not
  constructing its witness; PRIMES ∈ P is itself the example.
* Thms 3.1 and 6.2 are separate, scoped results. They are not consequences of this remark.

### 6.3 Parity (EVIDENCE)

* Sieve arguments cannot tell primes from products of two primes of comparable size (Selberg's parity barrier;
  standard, not re-verified here).
* An argument for (MS) that only uses "n has no prime factor below n^θ" proves R(n) ≥ 1 for such rough n. If its
  threshold is low enough to include them, it is falsified by the balanced semiprime zeros (finite range, §4): 2 956 321 = 211·14 011 (θ ≈ 0.359) and 897 961 = 443·2 027 (θ ≈ 0.445).
* Both of these lie in 𝔐 classes (2 956 321 mod 840 = 361, 897 961 mod 840 = 1). Still, no composite zero of any shape
  occurs in 𝔐 above 1.75·10⁷ (to 10¹⁰).
* So the parity barrier, as a falsifier for (MS) at threshold 10¹⁰, has **no data support** above 1.75·10⁷. It remains
  a barrier for *methods* (sieve lower bounds cannot produce pointwise positivity at one n), not for the statement.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed / clarifying; one new conjecture with strong finite data (MS⁺); no HOT LEAD.**

What was proved:
* Prop 2.1–2.2: the Π₁/Σ₂ classification and its consequences. Independence of (MS) would imply its truth.
  Counterexamples give brute-force refutations in Q of length p^{O(1)}. Existential-threshold forms are Σ₂.
* Thm 3.1 / Cor 3.2 (relative to Buss witnessing): an S¹₂ proof of (MS) yields a polynomial-time hit-or-factor
  algorithm. So it must split every composite zero in 𝔐 above 10¹⁷ (none are known), and it must find hits at primes.
* Lemmas 5.1–5.3: d_min ≥ n_p, d_min ≥ W(p), and 𝔐 = {p ≡ 1 (4) : n_p ≥ 11}. Hence no polylog trial-d witness rule,
  modulo the cited Ω-results.
* Prop 5.4: every two-small-coordinate search is a bounded-modulus table search. The (u, C) and (B, C) shapes are
  excluded at polylog size modulo OMEGA13; growing (u, B) menus are not excluded.
* Prop 5.5: (MS) + FQ_u(A) put the search in FP^{FACTOR}.
* Lemma 6.1 / Thm 6.2: the sign lemma for (★) in Shepherdson's model.
  * IOpen ⊬ (MS⁺★(P)) for every P.
  * CONDITIONAL on (MS) being true: IOpen + (MS★) ⊬ (MS⁺★(P)).
  * The counterexamples are pseudo-squares n₀ + 840t over every standard zero n₀ in 𝔐 classes.

What was computed:
* Zero census of R over all n ≡ 1 (4) to 10¹⁰: two implementations to 4·10⁹, a single engine beyond, and a different
  algorithm on checked samples. Within it, no non-square zero in 𝔐 classes in (17 401 609, 10¹⁰].
* Mean R/L² of non-square 𝔐 composites ≈ that of 𝔐 primes (0.119 vs 0.125) on [10⁷, 10⁸].
* Least witnesses d_min, C_min, u_min over all primes ≤ 10⁹: u_min ≤ 469, while d_min and C_min are large.
* u_min ≤ 7 at sampled probable primes in decades through [10²¹, 10²²), square-mimicking ones included.

**Hard screens (FRONTIER §4).**
* *T1 squares.* (MS⁺) excludes them by hypothesis. The pseudo-square theorem shows that a proof needs more than IOpen
  plus residues to use non-squareness.
* *8/131, numerator 8.* The logic results transfer verbatim to R₈. The 𝔐-restricted R₈ analogue of (MS⁺) is false at
  10¹⁰: 4 in-𝔐 prime zeros, 10 301 993 881, 10 529 331 121, 10 532 106 649 and 10 868 474 401 (12 R₈ prime zeros in
  all). So (MS⁺) for R carries the full-family content. Nothing here separates C odd from C even.
* *Tied modulus (B2).* Untouched. FQ_u and Prop 5.4 restate it algorithmically.
* *Fixed p.* No pointwise positivity conclusion is deduced from the reported averages. (The memo does use averages,
  Σ₂ formulations and infinitely-often assertions, but only descriptively or as barriers.)

**Proposed FRONTIER text** (do not edit FRONTIER here).
* §2.4 / §4 item F3:
  > *(z58 LOGIC.)* Within the census to 10¹⁰ the last non-square zero of R in Mordell's classes is the composite
  > 17 401 609 = 47·370 247. There is no non-square n ≡ 1 (4) with n mod 840 ∈ 𝔐 and R(n) = 0 in (17 401 609, 10¹⁰]
  > (CERTIFIED: two implementations to 4·10⁹, one beyond). The 𝔐 non-square-composite mean R/L² is 0.119 against 0.125
  > for 𝔐 primes on [10⁷, 10⁸]. Of the 285 composite zeros ≤ 8·10⁶, 270 lie outside 𝔐.
  > CONJECTURE (MS⁺): R(n) ≥ 1 for all non-square n > 17 401 609 in 𝔐 classes. It implies (MS), and its hypothesis
  > is decidable in polynomial time without primality.
  > Caveat (PROVED): IOpen ⊬ (MS⁺★), via the pseudo-squares n₀ + 840t (e.g. 121 + 840t) of Shepherdson's model.
  > CONDITIONAL on (MS) being true: IOpen + (MS★) ⊬ (MS⁺★). Here ★ marks the (★)-solution form; it is IOpen-equivalent
  > to the Hit form (`Z58_LOGIC.md` §6.1, Remark 6.3).
* §3 B1:
  > *(z58.)* d_min(p) ≥ W(p) (H_d ⊆ 𝓡(d)), so the number of trial d is superpolylog i.o. (modulo OMEGA13).
  > An S¹₂ proof of (MS) would give a polynomial-time hit-or-factor algorithm (Buss witnessing). Polylog (u, C) and
  > (B, C) searches fail i.o.; growing (u, B) menus are open.
  > A candidate polynomial-time factoring-oracle search is the shift search, conditional on (MS) + FQ_u(A):
  > then the search is in FP^FACTOR. EVIDENCE: u_min ≤ 469 for all primes p ≡ 1 (4) ≤ 10⁹.

**Bottom line.** (MS) is a Π₁ sentence. If it is independent it is true; this is cold comfort, and we know of no
*natural number-theoretic* Π₁ statement proved independent of PA (Friedman's combinatorial Π₁ examples exist;
`lit_verify.md` item 12). Logic does not find a shortcut. It sharpens three things.
* *Primality looks dispensable in Mordell's classes.* Non-square composites there behave like primes in the data,
  and their last zero within the census is 17 401 609. So the target can be posed as the statement (MS⁺), whose
  hypothesis is polynomial-time.
* *Non-squareness must be used beyond IOpen plus residues.* Open induction cannot exclude pseudo-squares.
* *A feasible proof needs a new classical search.* It would have to contain a polynomial-time classical method
  producing a divisor of some p + u, p + B or 4Cp + 1 in a prescribed class. That method must lie beyond the excluded
  polylog (u, C)/(B, C) searches.
  * Empirically such divisors are abundant at tiny u.
  * So the obstacle is B2 itself, now stated as a search problem: in FP^{FACTOR} conditionally on (MS) + FQ_u(A),
    not known to be in FP.

## 8. Review log and replay

**Internal hostile review** (`data/z58/logic/internal_review.md`, GPT-family reviewer, deep mode). It found 4 MAJOR and
11 MINOR issues; all were applied:
* (1) the conditional non-implication;
* (2) growing (u, B) menus not excluded;
* (3) the natural-proofs inference withdrawn;
* (4) finiteness of Z_C removes only the factoring branch;
* (5) MS⁺(P) thresholds;
* (6) encoding qualifications in Prop 2.2;
* (7) the n ≥ 2 guard and primary citations for conservation/PLS;
* (8) Lau–Wu for p ≡ 1 (4);
* (9) in-𝔐 counts (9/20/4; 270/285);
* (10) stars and scope of the model theorem;
* (11) the DP algorithm for FP^FACTOR;
* (12) script caps and flags;
* (13) sample decades and probable primes;
* (14) the `lit_verify.md` corrections;
* (15) status and replay.

The reviewer reran the 10⁸ and 10⁹ zero sieves, means and minwit at 10⁹, the classifier, the Z1018 comparison and the
independent decider. All reproduced; tables are in the review file.

**Cross-model review** (`data/z58/xreview/REVIEW_LOGIC.md`, ACCEPT-WITH-FIXES). All five required fixes were applied:
* (1) the shift search is called a *candidate* polynomial-time factoring-oracle search, conditional on (MS) + FQ_u(A)
  (§5, §7);
* (2) Prop 5.4's exact tests are p ≡ −u (mod d) and p ≡ −B (mod d′), with the p = 5 example;
* (3) the starred forms are kept in the FRONTIER proposal, and Remark 6.3 proves the IOpen equivalence;
* (4) the slogans are scoped: "only observed obstruction … within the census", the parity falsification is limited to
  thresholds that include the examples, and "no averaging" became "no pointwise positivity from averages";
* (5) the census lower endpoint is stated (5 ≤ n; n = 1 omitted).

The review also independently re-sieved to 10⁹ with a different loop order: exact archive equality. It reclassified the
whole 10¹⁰ archive, confirmed C_min = 76 141 at 564 661 441, and confirmed R₈ = 0 at the four in-𝔐 R₈ zeros.
Archive SHA256: e41709bcd38768c38d71d39813f4475b1815cc1995671496044fed1d197cac71.

**Replay** (each command under `ulimit -v 4000000` and `timeout 1800`):
```
gcc -O2 -o /tmp/z58zeros scripts/z58_logic_zeros.c && /tmp/z58zeros 10000000000 > /tmp/z1e10.txt        # ~15 min, 312 MB
uv run --with sympy python scripts/z58_logic_classify.py /tmp/z1e10.txt 1e10   # = zeros_1e10_summary.txt
zcat data/z58/logic/zeros_1e10.txt.gz | cmp - /tmp/z1e10.txt                    # archived list
gcc -O2 -o /tmp/z58means scripts/z58_logic_means.c -lm && /tmp/z58means 100000000      # = means_1e8.txt
gcc -O2 -o /tmp/z58minwit scripts/z58_logic_minwit.c -lm && /tmp/z58minwit 1000000000  # = minwit_1e9.txt (~2.5 min, 2 GB)
uv run --with sympy python scripts/z58_logic_umin.py                             # = umin_samples.txt (seed 5858)
uv run --with sympy python scripts/z58_logic_check.py FILE_OF_N                  # independent decider
```
The classifier needs the uncompressed list (`zcat` the archive first).
