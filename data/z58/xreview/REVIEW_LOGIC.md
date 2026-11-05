# z58 cross-model hostile review — LOGIC

**Verdict: ACCEPT-WITH-FIXES.** The principal logic results and refined census survive; the remaining fixes concern exact predicates and scope, not a failed main theorem. ES and (MS) remain OPEN. The unbounded (MS⁺) statement remains CONJECTURE, not a consequence of the census.
Reviewed `side-agent/z58-logic` at `027e5ec1cb8c0cfb3a863e47e1ee828a040b2cda`, including scripts, archive, screens and cited dependencies. No lane files changed.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| §1 Hit ↔ (★), witness bound | CORRECT | Set d=4uC−1; n+u=Bd, 1≤u≤(d+1)/4<d. Conversely r determines u=r, C=(d+1)/(4r), B=(n+r)/d. Since n≥d−(d+1)/4, 3d≤4n+1. |
| Prop 2.1(a–d), independence ⇒ truth | CORRECT | Expand divisibility/remainder with bounded quantifiers: θ is Δ₀. A false instance is a true closed Δ₀ counterexample, hence provable in Q. Therefore T⊬¬MS implies truth for T⊇Q, even without a consistency assumption. Fixed-depth bounded case expansion and unary arithmetic give p^{O(1)} length, not poly(log p). |
| Prop 2.2, hierarchy and ES | CORRECT | These are hierarchy upper bounds, not completeness/separation claims. Fixed rational parameters and thresholds suffice. A computable-real non-strict inequality is Π₁ via all approximation precisions; prefix ∃P gives Σ₂. For sorted ES denominators, x≤3n/4, y≤2nx, z≤nxy, giving polynomial bounds. |
| Thm 3.1 / Cor 3.2 | CORRECT | For n≥2, negated primality supplies a proper factor pair; Mord supplies that guard. Tagged hit-or-factor is polynomially balanced and Σᵇ₁, so Buss witnessing supplies FP. Only zero composites force the factor branch; this is not general factoring hardness. |
| §3 FP^NP and S²₂→PLS | CORRECT | NP queries locate a hit or factor by binary search whenever total. Buss conservation at i=1 transfers the relevant universal Σᵇ₁ sentence to T¹₂; Buss–Krajíček supplies a PLS projection. No converse or unconditional factoring-in-PLS conclusion follows. |
| §3 AKS / finite Z_C discussion | CORRECT | Checked current primary abstract/introduction. Finite Z_C removes only that restricted splitting obligation, not the prime hit-finding obligation. |
| §4 hit coprime to n | CORRECT | If g divides n and d, it divides r; r divides (d+1)/4, hence g divides both d and d+1, so g=1. |
| Lemmas 5.1–5.3 | CORRECT | Hit gives Jacobi (p/d)=−1; an odd prime factor ℓ of d has (p/ℓ)=−1. Reciprocity at p≡1 mod4 gives ℓ≥n_p. Residues at 2,3,5,7 yield exactly the six classes. For k∣A, D=kA∣A² gives −4D≡−k mod d. |
| §5 Ω consequences / trial-d exclusion | CORRECT, with stated dependencies | W≤d_min transfers the quoted lower bounds, including +∞ for no-hit primes. OMEGA13 Thm 5.1 has the displayed exponent and Mordell domain. Its analytic dependencies are retained, not independently discharged here. Lau–Wu Prop 5.1 explicitly supplies p≡1 mod4. |
| Prop 5.4, two-coordinate tables | CORRECT-WITH-FIX | For specified (u,C), the exact test is p≡−u mod(4uC−1), not all of H_d; similarly −B for (B,C). The modulus bounds and the exclusion of polylog (u,C)/(B,C) searches remain valid. Growing (u,B) menus are correctly left open. |
| Prop 5.5, conditional FP^FACTOR / FBQP | CORRECT | Factor n first; composites supply a pair. For primes, fixed-A FQ_u permits polynomially many u. Layered DP on 4u residues over prime-power choices reconstructs a divisor without listing all divisors. The residue −1 forces d≥4u−1>u, giving a valid hit. Shor, with amplification, yields bounded-error quantum search. |
| Lemma 6.1 | CORRECT | Beyond the largest nonnegative root of uBC all factors are positive. At that root they are nonnegative and a vanishing factor forces n≤0, contradiction. Thus positive integer constant terms give a standard (★) solution. |
| Thm 6.2(a–c) | CORRECT for stated starred forms | n₀+840σ^k is positive on σ≥0 and has simple complex roots, hence is not a polynomial square. The sign lemma excludes hits; every standard modulus sees n₀. Nonstandard elements factor after refining the Puiseux variable and splitting into real-algebraic factors, so primes are standard. Thus the relative non-implication genuinely needs truth of MS. |
| §6.2 natural proofs / §6.3 parity | CORRECT-WITH-FIX in scope | No natural-proofs theorem is claimed. Small balanced zeros falsify threshold-free roughness positivity, not MS above 10¹⁷; the later finite-range qualification is correct but should also accompany the initial falsification sentence. |
| §7 narrowed / no HOT LEAD | CORRECT | Clarifies obligations and proposes a stronger conjecture; proves neither positivity nor a general complexity/non-provability barrier for MS. |

## Required fixes, in priority order

1. **Do not call the shift method a known efficient search without its hypothesis.** §5's “only efficient search we know” and §7's proposed FRONTIER wording outrun Prop 5.5: polynomial oracle efficiency requires both MS and FQ_u(A); factoring alone does not bound the number of shifts. Replace with “a candidate polynomial-time factoring-oracle search, conditional on MS + FQ_u(A).” The finite u_min≤469 observation is evidence, not that complexity theorem.
2. **Repair Prop 5.4's exact residue tests.** Example: p=5, u=1, C=2 gives d=7 and p mod7∈H₇, but no integral B satisfies those specified coordinates; the actual hit is u=2,C=1. Use p≡−u mod d and p≡−B mod d′. No downstream exclusion needs changing.
3. **Keep the weak-theory formalization explicit in the FRONTIER proposal.** Its unconditional “IOpen⊬MS⁺” still drops the star. Either retain ★ or supply the ordered-ring equivalence: d=4uC−1, r=u, n+r=Bd and 3d≤4n+1; conversely the remainder/divisibility witnesses give u=r, B=(n+r)/d, C=(d+1)/(4r). These calculations justify the transfer; equivalence merely over ℕ would not suffice.
4. **Scope the interpretive slogans.** Change “F1 … only structural obstruction left” to “only observed obstruction above the conjectured cutoff within the census.” The balanced examples only refute roughness claims whose threshold includes them. Replace “Every statement … Π₁ … No averaging is used” with “No pointwise positivity conclusion is deduced from the reported averages”: the memo itself uses averages, Σ₂ formulations and infinitely-often assertions.
5. **State the census lower endpoint.** The engine lists 5≤n≡1 mod4, not literally all positive n≡1 mod4; n=1 is an omitted square zero. This does not affect MS⁺ or any reported non-square count.

## Exhaustiveness and numerical replay

The original engine is exhaustive in its documented range: for fixed u,B, C=1 minimizes n, and n increases in each positive coordinate. Every solution has u≤(N+1)/3, is reached by the B cutoff, and has u+B≡3 mod4. The bit-index stride uB corresponds exactly to n↦n+4uB; the inclusive index is floor((N−1)/4). Conversely every marked index reconstructs positive u,B,C, so no false hits are introduced. Signed 64-bit arithmetic and allocation/index bounds are safe through N=10¹⁰. This directly addresses the dangerous false-positive direction of the “none” claim.

I wrote `scripts/z58_xrev_logic_sieve.c` independently: exploit u↔B symmetry to impose u≤B, then enumerate u,C with 4u²C−2u≤N and B≡3−u mod4; progress in n by 4(4uC−1). Every solution has a symmetric representative, and each progression is checked against raw Hit. Raw d-search also checks every n≤4096. This is a differently ordered, independently bounded implementation of the same mathematics, not a fundamentally different census algorithm.

`scripts/z58_xrev_logic_verify.py` independently trial-factors the archive and uses a genuinely different divisor algorithm at selected inputs: m=min(u,B,C) satisfies 4m³−2m≤n; C=m is covered by (4mu−1)(4mB−1)=4mn+1, and u=m/B=m by divisors of n+m. Deduplication reconstructs all triples, not just one hit.

| Replay / independent check | Result |
|---|---|
| New sieve at 10⁸ and 10⁹ | **5,405 / 16,268 zeros; exact complete archive-prefix equality**. Original engine also rerun at 10⁸, exact equality. |
| Entire 10¹⁰ archive reclassified | 50,499 strictly increasing entries; every decade column agrees, including the omitted decade-0 square 9. This is archive checking, not a fresh full 10¹⁰ census. |
| MS⁺ cutoff / composite refinement | Exactly 18 in-class nonsquare composite zeros; maximum **17,401,609=47·370247**. Last in-class prime zero **8,813,281**. No archived in-class nonsquare zero in **(17,401,609,10¹⁰]**. |
| F3 ≤8·10⁶ | Exact screen equality: 285 composites, 15 in-class / 270 outside; also 13 primes and 1,413 squares. |
| Large composite structure | All 94 composite zeros ≥10⁸ divisible by 3,5 or7; coprime-to-105 composite zeros above 10⁷ are precisely 12,538,801; 17,401,609; 29,210,401. Last balanced zero 2,956,321. |
| Independent divisor rejection | All 18 in-class composite zeros and 8,813,281 have no triples. |
| Means engine at 10⁸ | Byte-for-byte saved-output match: PM 158,955 / 0.1246; CM 482,339 / 0.1189 / 2 zeros. Relative difference ≈4.6%, agreeing with “within 5%.” |
| Min-witness engine at 10⁹ | Byte-for-byte saved-output match, including u_min≤469 and explicit C saturation. |
| Independent minima at record inputs | 85,664,329: (d,C,u)=(2,953,943,41,027,18); 564,661,441: (2,741,075,**76,141**,9); 53,325,721: (11,255,5,469); 413,490,001: (193,763,201,241). |
| F2 independent complete triple counts | At 10,301,993,881; 10,529,331,121; 10,532,106,649; 10,868,474,401: R=30,42,12,18 respectively, and **R₈=0 in every case**. |

Archive SHA256: `e41709bcd38768c38d71d39813f4475b1815cc1995671496044fed1d197cac71`.
Independent 10⁸ output SHA256: `4ef0ddd3a7c547b3fabc039372ed469bf988fee5de738c41e3249041a0a69053`.
All computations used `ulimit -v 4000000`, timeouts ≤1800 seconds and one compute job at a time. The largest allocation was the original minwit replay (about 2.5 GB); the independent 10⁹ sieve uses about 31.25 MB. No new exhaustive run above 10⁹ or new replay of the large probable-prime sampler is claimed.

Replay: extract the reviewed commit's `data/z58/logic/` and `data/z58/screens/` into `/tmp/xrev_LOGIC`, then run each command with the shown resource wrapper:
```sh
ulimit -v 4000000; timeout 1800 gcc -O2 -Wall -Wextra -Werror scripts/z58_xrev_logic_sieve.c -o /tmp/xrev_LOGIC/independent_sieve
ulimit -v 4000000; timeout 1800 /tmp/xrev_LOGIC/independent_sieve 100000000 > /tmp/xrev_LOGIC/independent_1e8.txt
ulimit -v 4000000; timeout 1800 /tmp/xrev_LOGIC/independent_sieve 1000000000 > /tmp/xrev_LOGIC/independent_1e9.txt
ulimit -v 4000000; timeout 1800 uv run --with sympy python scripts/z58_xrev_logic_verify.py /tmp/xrev_LOGIC
```

## Falsifier table

| Screen | Checked verdict |
|---|---|
| F1 odd squares | Correct exclusion from MS⁺; the Jacobi obstruction proves their zero status. The pseudo-square model defeats the starred extension in IOpen, not MS in stronger theories. |
| F2 numerator-8 / C-even | Correct: 12 listed zeros, **4 in 𝔐**, independently checked above. Refutes the in-class R₈ analogue at threshold 10¹⁰, not full R or the logic theorems. |
| F3 285 composite zeros | Correct refinement: 15 in-domain, all below MS⁺'s cutoff. New full-prefix replay supports the finite absence, not an unbounded last-zero theorem. |
| F4 14 (★) / 38 𝔊* prime zeros | Counts and membership checked: **9 / 20 in 𝔐**. Only those refute class-restricted rungs, and only below their thresholds. No purported positivity mechanism survives by ignoring these inputs. |

## Source checks and limits

Buss's primary thesis, Chapter 5 Theorems 1 and 6 / Corollary 8, explicitly supplies the required witnessing result: https://mathweb.ucsd.edu/~sbuss/ResearchWeb/BAthesis/Buss_Thesis_OCR.pdf . Checked full PDF/OCR; the first reader extraction was truncated, so it was not treated as a complete source check.
Buss conservation Thm 5 (i≥1) and Buss–Krajíček §5.3 were read in the author texts: https://mathweb.ucsd.edu/~sbuss/ResearchWeb/BAaxioms/camera.pdf and https://mathweb.ucsd.edu/~sbuss/ResearchWeb/Si2Ti2sep/paper.pdf . Both match the memo's use.
AKS's corrected theory and factoring consequence match https://arxiv.org/html/2504.17041v2 (abstract/introduction). Raffer's introduction explicitly constructs the required Puiseux-polynomial model from Shepherdson's integer-part criterion: https://ar5iv.labs.arxiv.org/html/1010.3798 . Shepherdson's 1964 original was not retrieved; the construction was also checked directly via finite polynomial parts of descending Puiseux series.
Lau–Wu Prop 5.1 and its definition of P_y were read in the archived primary-source text `sources/lit2026/lau-wu-least-quadratic-nonresidue.txt`, lines 378–405. OMEGA/OMEGA13 statements and domain were checked, but their upstream analytic proofs were not re-proved in this review.

**Bottom line:** accept the scoped theorems and finite census after the listed fixes. No counterexample to MS⁺ was found; no evidence here turns it into a theorem or supplies a general barrier to proving MS.
