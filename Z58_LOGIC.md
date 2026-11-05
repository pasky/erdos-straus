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
| **F3 composites** | Sharpened by new data (§4, CERTIFIED to 10⁹; 10¹⁰ pending). Among non-square composites in Mordell's classes (n mod 840 ∈ 𝔐) the zeros of R end at **17 401 609** (to 10⁹). The 285 composite zeros of F3 are overwhelmingly outside 𝔐, mostly divisible by 3, 5 or 7. In 𝔐 the composite mean of R/L² is 0.1189 against 0.1246 for primes on [10⁷, 10⁸]. So primality beyond non-squareness is *not* visibly used by (MS) above 2·10⁷: (MS⁺) is consistent with all data (EVIDENCE). Thm 3.1 says a feasible proof of (MS) must factor any composite zeros in 𝔐 above 10¹⁷; if (MS⁺) holds there are none. |
| **F4 known zeros** | Nothing here proves positivity. Prop 2.1: any counterexample to a Π₁ rung has a proof of falsity of length polylog(p). This is the logic reading of F4: the 14 (★)-zeros, 38 𝔊*-zeros and 12 R₈-zeros are *short refutations* of the corresponding rungs at thresholds below them. |

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

## 4. Census: composite zeros in Mordell's classes (CERTIFIED to 10⁹; EVIDENCE for the reading)

`scripts/z58_logic_zeros.c` is a bitset sieve over all triples. It marks every n ≡ 1 (4), n ≤ N, of the form
4uBC − u − B, and lists the unmarked ones. `scripts/z58_logic_classify.py` splits them into P / SQ / C and factors the
composites.

*Validation.* At N = 8·10⁶ the engine reproduces exactly the screen files. It finds 13 primes (the known ones
≤ 8·10⁶), 1 413 odd squares, and the 285 composites of `composite_zeros_le8e6.txt` (list equality checked).

**Census to N = 10⁹ (CERTIFIED, single engine; `data/z58/logic/zeros_1e9_summary.txt`).** Per decade ⌊log₁₀ n⌋:

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

* The composite zeros in 𝔐 classes number 18 in total. The two largest are 12 538 801 = 11·47·79·307 and
  **17 401 609 = 47·370 247**. There are none in (1.75·10⁷, 10⁹].
* The prime zeros in 𝔐 end at 8 813 281.
* The "balanced" composite zeros (least prime factor ≥ n^{1/3}) end at 2 956 321 = 211·14 011.
* Composite zeros above 3·10⁷ are dominated by small factors: 3 | n in most of them, otherwise 5 or 7.
  Mechanism (PROVED, elementary): a hit d is coprime to n, because g | d and g | r | (d+1)/4 force g | 1. So 3 | n
  removes every d ≡ 0 (mod 3). Every n in an 𝔐 class is coprime to 105.

**Mean R/L² by class on n ≡ 1 (4), n ∈ [10⁷, 10⁸] (CERTIFIED counts, `means_1e8.txt`).**
* Primes: 0.1636 (2 548 324 n, 0 zeros).
* Primes in 𝔐: 0.1246 (158 955 n, 0 zeros).
* Composites in 𝔐: **0.1189** (482 339 n, 2 zeros).
* Composites with 3 | n: 0.0966 (82 zeros).
* Other composites: 0.1470 (9 zeros).

**CONJECTURE (MS⁺).** R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐.
* *Evidence.* There is no counterexample in (1.75·10⁷, 10⁹]. In 𝔐 the composite mean R/L² is within 5 % of the prime
  mean. The composite zeros thin out by decade in the same way as the prime zeros.
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

*Consequence (PROVED modulo Graham–Ringrose, `lit_verify.md` item 9, PARTLY verified via a survey).* Infinitely many
primes p have n_p ≫ log p · log log log p. All but finitely many of them lie in 𝔐 by Lemma 5.2, and d_min(p) ≥ n_p
there. So (MS) has no witness rule of the form "some d ≤ c·log p fires". Trial search in increasing d is not
O(log p)-step on the target set.
* Under GRH, Bach's n_p ≤ 2 log² p is an *upper* bound on n_p only. It gives no upper bound on d_min: no implication
  GRH ⟹ (MS) is known (FRONTIER §2.4).

## 6. Barrier analogues (to be written)

## 7. Verdict (provisional)

Narrowed / clarifying. The logic picture:
1. (MS) is Π₁. Independence would imply truth. Eventual forms are Σ₂ and do not finish ES.
2. A feasible (S¹₂) proof must factor the composite zeros in 𝔐 (Thm 3.1).
3. The data say there are probably none above 1.75·10⁷ (MS⁺, EVIDENCE). Primality is then needed only as
   non-squareness.
