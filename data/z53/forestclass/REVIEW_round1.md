# Verdict: REJECT (as written)

Theorem 1's conditional construction survives review, and the main census/enrichment numbers reproduce. The rejection concerns false or unsupported mathematical conclusions attached to those results—not an ES counterexample or a defect in the Dickson construction. ES remains open.

## Findings

1. **FATAL to the headline classification — the claimed equivalence is false.** Locations: §4, “Reading” after Lemma G (lines 247–249); proposed FRONTIER text, lines 407–408; §8, lines 425–426. Lemma G proves **SM ⇒ no genus obstruction**, not the converse. At p = 17, a = 4 is not SM because −17 ≡ 3 mod 4, but N = 21 has divisors 3 and 7 in the target coset; indeed {4,3} and {4,7} are edges. Also p = 17, a = 5 is non-SM and isolated but not genus-obstructed: G² = {1,4}, the target coset is {2,3}, and divisors 2 and 22 of N = 22 occupy it. The memo's own data contain **360,342,119 non-SM vertices without a genus obstruction**. **Fix:** replace every “iff,” “precisely,” and “exactly” here by the one-way automatic-positivity statement. Retain Lemma G(1)–(4), which are correct.

2. **MAJOR — “only/exactly the genus layer” is not a theorem.** Locations: §0 lines 10–11, 18–22; §4 concluding readings; §6 lines 390–392; §7 lines 400–415; §8 lines 425–430. Neither Lemma G nor residual enrichment ratios exclude additional class-group information, another choice of roots, or a different argument. Proposition 3 gives a dictionary for edges incident to square vertices, not an impossibility theorem elsewhere. Calling the growing-root question “the HC question” also supplies no equivalence with the one-coordinate/polylogarithmic HC target in FRONTIER: components can extend beyond a root window, and HC also includes the level coordinate. Moreover §6's assertion that “at a root” the target is in the principal square coset is true for SM, **not SP**; p = 17, a = 4 is already an SP counterexample. **Fix:** consistently say “the measured enrichment is consistent with a genus explanation; no additional mechanism was detected”; label extrapolations Assessment/EVIDENCE. Limit the principal-coset assertion to SM. Describe T1/8 controls as consistency checks, not a successful existence-proof screen. Describe the decreasing failure rate as an observed two-bin comparison.

3. **MAJOR — distinguish the computed root sets from complete reduced-form/class-group data.** Locations: §1 lines 58–65; §0 labels “SM (reduced forms)”/“SP (all cycles)”; §2 line 93; §4 Proposition 2 and its reading. There are two boundary discrepancies:
   * SM includes a = floor(√p)+1, where the reduced-form identification need not hold. For p = 41, a = 7 belongs to SM, but its only reduced-range b are ±1, giving c = 6 < 7: no reduced form has leading coefficient 7. Conversely, reduced minima can exceed the root cutoff. At p = 19441 there are **56 reduced forms and 29 distinct minima**, but the computed SM has **27**; minima **146 and 151** lie outside its cutoff 140.
   * SP's definition extends beyond √p, whereas the cited theorem only identifies values below √p. For example p = 73, a = 9 belongs to the computed SP but is not below √73.
   There is also a primitive/imprimitive issue for positive discriminants: at p = 17, the Q = 2 reduced irrational gives (2,6,−4), an **imprimitive** form of discriminant 68, reducing after division by 2 to discriminant 17. In fact a primitive discriminant-68 form cannot have leading coefficient 2. PELLCYCLE explicitly distinguishes the combined cycles from a proved class-number interpretation. **Fix:** define SM/SP as the exact congruence-filtered root sets used by the engine; restrict the form identifications to their established ranges and specify whether imprimitive cycles are included. Do not silently replace them by Cl(±4p).

4. **MAJOR — Proposition 2(iii) is false for the globally truncated sets as defined.** Locations: lines 58, 206–214; corresponding assertion in §0 line 20. Take X = 10 and primes p = 17 and p′ = 20177. They are congruent modulo **8·lcm(1,…,10) = 20160**, but a = 8 is excluded from SP(17) by its root cutoff 5 and included in SP(20177), whose cutoff is 143. Both primes are 1 mod 8. **Fix:** assert congruence dependence for the untruncated local membership predicates, or require X ≤ √p+1 for every prime under comparison. The reciprocity argument then works; 8·lcm is a valid sufficient modulus.

5. **MAJOR — Proposition 2(i) is sound, but its advertised cardinality consequences exceed its proof.** Locations: §2 line 93; §4 lines 200–223; §7 line 406; §8 line 421. The multiplicity/Siegel argument counts **all reduced minima up to √(4p/3)**. It does not establish the same lower bound for the truncated SM set, still less for SMN or SP. The positive-discriminant paragraph is only an Assessment, and incorrectly describes the regulator as the sum over all cycles: the sum over classes involves a class-number factor. A real class number must not be confused with hR or with the number of cycle positions/distinct Q-values. **Fix:** keep the proved non-freezing statement for the full negative-discriminant reduced-minimum set; supply separate bounds for the actual truncated sets before applying that conclusion to them. Restrict “not quasi-polynomial” to the precise exclusion proved: a fixed finite list of polynomial-valued root recipes cannot enumerate a set of growing cardinality. State p ≡ 1 mod 4 explicitly for the primitive negative-discriminant discussion.

6. **MAJOR — no uniform density-(log X)^(−1/2) claim follows in the moving-p window.** Locations: §0 line 21; §4 lines 223–224. Fixed-discriminant Landau/Bernays-type asymptotics have discriminant-dependent constants and do not justify this assertion uniformly at X ≍ √p or for arbitrary growing windows. For any fixed X, CRT and Dirichlet permit arbitrarily large p ≡ 1 mod 8 with (−p/ℓ) = −1 for every odd prime ℓ ≤ X. Then SM ∩ [1,X] = {1,2}. Conversely, prescribing +1 at every such odd prime makes every a ≤ X with 4 ∤ a belong to SM. Choose p > X² to avoid the cutoff issue. **Fix:** qualify a fixed-p asymptotic with its constant/range, or label the moving-p claim explicitly as a sample-based heuristic. The measured share of hit roots is not itself the density of the entire filter.

7. **MAJOR — the bounded-menu conclusion is overbroad.** Locations: §0 lines 14–16; §3 lines 179–181; §7 lines 400–403, 416–417; §8 lines 423–424. Theorem 1 and Corollary 1.1 cover the listed **ordered initial distinct minima/root values**, the two genus minima, the two ambiguous classes, and prefixes of the specifically chosen prime-5 class. They do not cover every bounded-cardinality function of class-group data, an arbitrary p-dependent split ideal class, or initial positions in every individual real reduction cycle. “First elements of all cycles” must mean the smallest values in the ordered union, not a prefix of each cycle. **Fix:** replace “every bounded class-group menu” by the exact enumerated families and say “first K distinct SP values in the ordered union.” Novelty should remain the simultaneous H-fixed-root/K-least-nonresidue extension of the existing Dickson-shadow construction; it does not subsume FABLE Proposition 3.3's level-coordinate and many-word conclusions.

8. **MAJOR — Proposition 3(iv) asserts an actual parent where only a candidate parent exists.** Locations: lines 286–287 and 297–298. At p = 269 the reduced form (13,4,21) has b² = 4 < 13, but 4 ∤ 22, so vertex 13 has **no smaller neighbour**, rather than parent 4. The proposition's second sentence supplies exactly the missing condition. The principal form (1,0,p) also satisfies b² < a but gives the nonexistent vertex 0 and division by b² = 0. **Fix:** require a > 1 (hence b ≠ 0 here), say “the only possible parent is b²,” and then state that it exists iff b² | c+1. The proof of (i)–(iii), including the genus-character step, is otherwise correct for an actual square vertex b² ≤ p+2.

9. **MINOR — the p ≡ 5 mod 8 root-1 statement excludes SMN/NR.** Locations: §1 lines 75–76; §5 sentence preceding the census table. Root 1 has positive colour and is never in SMN or NR. Those sets hit at **root 2**, through the same edge {1,2}; 2 is SM and has negative colour in this congruence class. **Fix:** distinguish roots 1 and 2. The asserted success of all sets remains correct.

10. **MINOR — state the actual quantile comparison population.** Location: §5 lines 337–341. The numbers agree with `smn_fail_quantiles.txt`, but `z53_forestclass_smnquantile.py` ranks against **non-failing census primes only**, excludes all failures, uses strict “<”, and clips windows at the census boundary 10⁸. Thus these are not quite quantiles among all primes within ±10%. The top two failure windows are truncated; 193 has no eligible comparison prime. **Fix:** document those choices, or recompute the stated all-prime statistic. The retained file contains rounded individual quantiles, so its exact mean and threshold counts cannot be independently reconstructed from those rounded entries alone.

11. **MINOR — two numerical/reporting corrections.** Locations: §5 line 315 and sample table line 356. The intended union of odd 5…1999, odd squares 3²…99², and primes 1 mod 4 in [2000,12000] contains **1586 distinct inputs**, not 1607. The concatenated lists have 1607 entries, including 21 duplicate small squares. Say “1607 runs on 1586 distinct inputs” if that is the actual check. The stored 10¹² sample has SP hit mean **85.55**; conventional rounding to one decimal gives **85.6**, not 85.5. The other sample means/shares reproduce.

12. **MINOR — the advertised instances do not use the literal construction parameters.** Location: §3 lines 183–187 and `thm1_instances.txt`. For H = 3, K = 1, q = 11, construction step 1 would require 5 > 3+τ(12) = 9, which fails. The instance script also uses a smaller modulus than Q₀·rad(Q₀)·q. This does **not** invalidate their checked menu failures: c = 2 avoids the actual bad set, the smaller modulus supplies the needed local conditions, and the displayed L-values are prime. **Fix:** call them verified instances of the conclusion/sufficient local factorization pattern, or explicitly permit directly checking c ∉ B and using a reduced modulus. Do not call them literal instances of the displayed CRT construction without this explanation.

## What I verified independently

### Proof audit

**Theorem 1: passes, conditional on Dickson.** The τ bound supplies arbitrarily large q ≡ 3 mod 4 with the required strict inequality. Each divisor used in B is invertible mod q; |B| is bounded by the stated sum, leaving an available nonresidue c. The choices of Y and eℓ cover every prime power in 1+x, exclude q from its factors, and make all Lx integral. CRT applies because q is coprime to Q₀rad(Q₀).

Admissibility (α), (β), and (γ) all work: respectively constant 1 modulo ℓ, nonzero constants modulo q, and fewer linear roots than residues for ℓ > Y. Distinct x give distinct slopes and also distinct intercept/slope ratios (p₀+x)/Q, so the forms are nonproportional. Take the standard nonnegative representative p₀ and/or discard finitely many parameters to ensure all stated size conditions. In fact 2^e₂ > Y and 3^e₃ > Y already make Q₀ > Y².

Properties 1–5 pass. The factors 16 and 27 give p ≡ 1 mod 24. Reciprocity gives exactly the claimed character pattern, and **K < q is explicitly ensured and necessary** for the stated description through Kq. LTA Theorem 3.1 requires only the four primalities, p = 24k+1 and k ≥ 1; all hold, and its eight-vertex component is exactly the one quoted. For 4 ≤ i ≤ H, p ≡ 1 mod i and gcd(i,i+1)=1 give Li ≡ 1 mod i, ruling out all neighbour cofactors. For x = qj, the bad-set argument rules out eLx, while e itself cannot be −1 mod x. Also Lqj ≡ 1 mod j does follow from p ≡ 1 mod j and gcd(j,1+qj)=1, though this proof does not need it. The neighbour/isolation criterion is correctly applied at these coprime vertices.

**Corollary 1.1(a)–(e): passes for sufficiently large primes of the constructed family and the stated initial-value menus.** Odd-prime solvability lifts to prime powers; the 2-adic restriction is 4 ∤ a. Since K < q, the nonprincipal minima through Kq are exactly qs with s ∈ T, s ≤ K. There are two genera and the ambiguous reduced forms are the two displayed forms. Prime 2 ramifies, 3 is inert, and 5 splits, so 5 really is the least split prime. An ideal power above 5 is primitive of norm 5^k; choosing its corresponding b modulo 5^k in the reduced range gives the claimed reduced form when 5^k ≤ √p. This does not cover arbitrary split classes.

**Proposition 2(i): passes.** Here a ≤ √(4p/3) < p, so gcd(a,p)=1. There are at most two square roots at each odd prime power and at most four at a power of 2, yielding the safe bound 2^(ω(a)+1). The subpolynomial maximum and Siegel bound prove the displayed lower bound for full reduced minima. The ε losses can be absorbed by using ε/2 in the separate estimates.

**Lemma G(1)–(4) and “Colour on SM”: pass.** gcd(N,a)=1 follows from p ∤ a. Every Euler factor of σχ(N) is e+1, 0 or 1. Character orthogonality and the divisor-image span argument are exact; exponent choices 0 and 1 generate the whole elementary-2 span. The trivial-character term gives the stated fair-share lower bound on SM. The colour formula and 4 ∤ a are correct in the declared range. I additionally checked the divisor-coset/span/fair-share statements and colour formula by literal residue enumeration on **1474 (p,a) pairs**.

**Proposition 3(i)–(iii): pass.** The divisor/form correspondence is exact, and the forms are primitive for fundamental discriminant −4p. Modulo p a primitive such form is a nonzero rank-one quadratic form, so all its nonzero represented values have one Legendre symbol; this justifies the genus-theory step, including nonprimitive representations prime to p. The parity/Jacobi argument in (iii) is valid. Part (iv) needs finding 8's correction.

### Independent numerical work

My checker `/tmp/rev_fc_check.py` does **not** use repository enumeration helpers: it visits every vertex v ≤ p+2, tests its unique candidate parent u = −p mod v using the exact edge predicate, uses ordinary adjacency/BFS, and determines SM/SP by enumerating squares modulo every root. All six root-set sizes, full/depth-1/depth-2 hit counts, first hits/ranks, and edge counts agree with the compiled engine at:

**19441, 2521, 3361, 32441, 90697, 20233, 18089, 12433, 69257, 31513, 89209.**

Key results (full-component hit roots):

| p | edges / bichromatic edges | SM | SMN | SP |
|---|---:|---:|---:|---:|
| 19441 | 20 / 9 | 0/27 | 0/13 | 3/95 |
| 2521 | 18 / 2 | 4/17 | 0/8 | 6/36 |
| 3361 | 23 / 4 | 4/12 | 0/5 | 9/40 |

At 19441 the complete bichromatic components are exactly **{7,26,68,187,189,572,1496}, {20,39,499}, {38,129}**.

I independently explored all components meeting the specified menus at **21679561**, **13911395401**, and all five H = 8, K = 1 instances up to **87004184401**. Every component is monochromatic. In the first case the components are

`{1,2,3,7226521,10839781,10839782,21679562,21679563}` and `{11}`;

the prime L-values for x = 1,2,3,11 are **10839781, 7226521, 5419891, 1806631**. In the second case the nontrivial component is

`{1,2,3,4637131801,6955697701,6955697702,13911395402,13911395403}`,

with singleton components **{4}, {5}, {11}**. Its six L-values are **6955697701, 4637131801, 3477848851, 2782279081, 2318565901, 1159282951**, all prime. Both least nonresidues are 11. I also proved primality of **all 16 recorded instance primes**, including the three above 2^64, using recursive complete-factorization Lucas certificates rather than relying solely on probable-prime tests. For all 16, the recorded progression parameters, least-nonresidue lists, integrality of every L-value, and all-L-prime flags check correctly.

An independent C sieve gives **165976 + 1273994 = 1439970** primes 1 mod 8 in the two census ranges. Independently merging the stored summaries reproduces every failure/depth/max-rank entry:

| Set | full / depth≤2 / depth≤1 failures | maximum rank (a,p) |
|---|---:|---|
| ALL | 0 / 0 / 0 | 25 (25,78168721) |
| SP | 0 / 0 / 0 | 28 (32,19231801) |
| SM | 1 / 1 / 6 | 183 (911,4149601) |
| NR | 0 / 0 / 0 | 66 (339,41751889) |
| SMN | 48 / 48 / 54 | 375 (4679,23544721) |
| SQ | 668 / 4983 / 19583 | 94 (8836,81326281) |

The two SMN failure lists match the memo exactly: **34 + 14 = 48 distinct primes**, all prime and 1 mod 8. Re-running the supplied engine on all 48 confirms every SMN failure and SM failure only at 19441. The observed rates are approximately **2.0485·10^−4** and **1.0989·10^−5**. The quantile summary reports **47**, means **0.0561809099876 / 0.0526529391878**, and threshold counts **35 / 38**, matching the memo subject to finding 10.

I independently aggregated all raw genus rows and recomputed the Mantel–Haenszel ratios: **all 24 enrichment-table entries reproduce**. There are **669018402** total root records; among a ≥ 4 there are **94823144 SM** and **574180858 non-SM** vertices. Exactly **213838739** are genus-obstructed, all non-SM and all isolated. The census comparison range 1.20–1.62 also reproduces when using that script's extra stratum for the other membership flag; that is not exactly the same stratification as the genus table.

All five sample files have the claimed **3000/1000/500/300/100** rows, with zero failures for the reported sets. Their means (ALL, SM, SP, SMN, SQ) are:

- 10^9: **124.036, 31.7056667, 49.6173333, 19.608, 4.4973333**.
- 10^10: **155.711, 37.685, 60.647, 23.788, 4.692**.
- 10^11: **194.394, 44.794, 72.844, 28.706, 4.902**.
- 10^12: **235.99, 51.5066667, 85.55, 33.0266667, 5.31**.
- 10^13: **281.81, 60.32, 105.72, 39.64, 5.4**.

The five SM/ALL shares round to **0.256, 0.242, 0.230, 0.218, 0.214**. Stored hard-prime data have **134** rows and exactly the claimed SM/SP/SMN failure sets; all six H-instances have first SM/SP hits ≤ 11. The five H = 8 instances have first ALL/SP hits 9 or 10, SM hits 10 or 17, and SMN hits 19,23,22,19,43. The **5000** stored odd-square records all have zero bichromatic edges. An independent primality count finds exactly **1330** near-square primes; their stored records reproduce zero SM/SP/SMN failures, maximum SMN rank **94**, and the sole SQ failure **1299601**.

Scope of verification: I did not regenerate the entire 10^8 forest census or the original 129829-pair genus-check log. For those, I checked the retained summaries/raw aggregates plus the independent tests described above. Records above 10^11 were only read, not subjected to whole-forest reruns. All computation was timeout- and memory-bounded. No repository file was edited or committed.
