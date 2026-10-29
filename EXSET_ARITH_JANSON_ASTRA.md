# Arithmetic Janson–large-sieve hybrid (z50 C2, ajastra)

## 0. Summary and status

**Scope.** Long, adversarial exceptional-set attempt. ES remains open. No new exceptional-set estimate is claimed at initialization.

| Round | Target | Status | Review |
|---|---|---|---|
| 1 | Universal AJ with O(√N) remainder | Refuted; √N log log N required in a generic family | Opus SOUND, minors repaired |
| 2 | One-big-prime truncated hybrid | Classical exact formula; no exponent gain | Opus SOUND, minors repaired |
| 3 | ES-specific rescue or enlarged barrier | Pending | Pending |
| Final | Exponents, controls, exact surviving gap | Pending | Pending |

Labels used: PROVED, CONDITIONAL (named hypothesis), CERTIFIED (finite computation), EVIDENCE, CONJECTURE, Assessment. All advances require hostile cross-model review before acceptance.

## 1. Audit and references

**Assessment / scope audit.** Read the z48 and z49 contexts and the binding z50 context twice; FRONTIER §§2–4,6–7, BREADTH_Z45, the PR-B map and arithmetic/covers supplements, OAI_DUMP_IMPACT's audit, and the z48 forest/lower-tail summaries (FOREST_H4 §§3.5,5). The relevant model input is CONJECTURE_S_MODEL §2, not an independence assertion for actual integers. Its atomic Janson proof is in `paper/es-subexp-note.tex` §Janson: conditioning on an atom deletes coordinates in a PRODUCT probability space. Arithmetic first/second moments do not justify that deletion.

**Existing results, not new.** DISCOVERIES (D)17–(D)31 were read in full. EXCEPTIONAL_LARGESIEVE §§1–3 gives the exact CRT-admissible large-sieve/positive-square duality; (D)25 covers periodic Bessel rows, twists and hybrids; (D)27 covers one-big-prime forced families even at arbitrary frequency level; (D)28 handles residue-sparse multi-rough families. Thus simply renaming a periodic Bessel inequality “Janson” cannot help. A positive result here would need actual interval information, door (i), or a nonlinear conditioning theorem with new arithmetic input, door (vii). The counterexamples below are about the proposed estimates themselves, not about Bessel implementations.

**Precise target (CONJECTURE to be tested).** For distinct congruence atoms B_i={n≡a_i (q_i)}, q_i≤Q, let ν be uniform CRT measure, μ=Σ_i ν(B_i), and Δ=Σ_{i<j,(q_i,q_j)>1}ν(B_i∩B_j). Conflicting pairs contribute zero. On [1,N] let S_N be the avoider count. Test

    S_N ≤ C(N+Q²) exp(−μ+KΔ) + R(N,Q).                    (AJ)

Here C,K are absolute and a useful proposed error is R=N^{1/2+o(1)}; first test R=0 and R=C₀√N. Atomic probabilities ≤1/8 and conflicting probability load ≤1/8 will be imposed in counterexamples, so the model theorem's smallness hypotheses are not silently discarded. For prime inputs the model is uniform units and atom density is 1/φ(q), not 1/q. No prime-input counterexample is inferred from composite squares.

**Certificate-class audit.** In covering coordinates n=(tu−1)v−u, put A=tu−1. If 4|t, then A≡3 (4), u|(A+1)/4, and −u is an ℛ(A) label (take reduced ratio u/1 in LS7 Lemma 1.1). If 4|u, write u=4d: A=4td−1 and −u=−4d is an ℛ(A) class because d|((A+1)/4)². If 4|A, write A=4m: −u mod4m, u|4m+1, refines a Type-I Case-A class with d=m at its actual modulus 4g(m), g(m)=∏p^{⌈v_p(m)/2⌉}; use the complementary divisor (4m+1)/u to write the Case-A inverse label. Swap u,v for the other two slots. Thus every five-slot (ES₅) certificate has a forced-class encoding of one of the capped types. This is an encoding of witnesses, NOT a claim that every endpoint event is literally the same atom at the same modulus: refinements/unions and positivity ranges must be retained. In particular, a cap for a re-encoded family must be applied at its actual level. The one-big-prime Type-II family is directly in the ledger; no unverified transfer of its exponent to U will be made.

**Literature check (Assessment, 2026-10-29).** A live search for “Erdos Straus exceptional set 2026 Vaughan Pomerance Weingartner” located Pomerance–Weingartner, *Exceptions to the Erdős–Straus–Schinzel conjecture*, Ramanujan J. 69, 31 (2026), https://arxiv.org/abs/2511.16817, and the March 2026 Pomerance talk slides https://math.dartmouth.edu/~carlp/esconjfl.pdf (search hit only). Visited https://arxiv.org/html/2511.16817v2: §4 proves the 2/3 bound by the truncated large-sieve Euler product, with mass ≍log²X for the full Vaughan prime classes. No newer stronger published exceptional-set estimate was located. This limited search is not an exhaustive literature certification. Note the distinction from the *prime-coordinate forest subfamily*, whose mass is only ≍log X; the full Vaughan ℛ(ℓ) family has log²X mass. No OAI-003 hypothesis is used here.

## 2. Round 1: universal hybrid

### 2.1 Translated-square obstruction

**Theorem 2.1 (PROVED relative to the standard Weil bound for quadratic character sums; Opus review: SOUND with minor repairs).** There are prime-modulus families with Q=(log N)^4, Δ=0, all atomic probabilities and all conflict loads ≤1/8, and μ≫(log N)^3/log log N, whose actual integer avoider count satisfies

    S_N ≫ √N log log N.

Consequently (AJ) is false for R=0 and for R=C₀√N for any fixed constants C,C₀,K. More generally, this example forces R(N,(log N)^4)≫√N log log N whenever the exponential term is negligible. This is a statement about the proposed numerical inequality, including nonlinear proofs; it is not merely a cap on Bessel/majorant proofs. It does NOT refute an error N^{1/2+o(1)}, and its forbidden classes are not claimed to be ES classes.

*Proof.* Put k=⌊log Q/(4 log 2)⌋. For each odd prime Q/2<p≤Q, forbid every residue a satisfying

    ( (a−j)/p ) = −1  for all 0≤j<k.                     (2.1)

Write Ω_p for this residue set and use the singleton classes a mod p as the atomic events. Since p>k, the k roots j are distinct. Expand 2^{−k}∏_{j<k}(1−χ_p(a−j)) and sum over a. Away from these roots it is the indicator of Ω_p; at the roots its total correction is O(k). For every nonempty subset J, ∏_{j∈J}(X−j) is squarefree, and Weil gives absolute character sum ≤(|J|−1)√p (the singleton sum is zero). Therefore

    |Ω_p| = 2^{−k}p + O(k√p+k), uniformly in p,k.        (2.2)

Since 2^k≤Q^{1/4}, the relative error is O(kQ^{−1/4})=o(1). The prime number theorem on (Q/2,Q] now gives μ=Σ_p|Ω_p|/p≍Q^{3/4}/log Q. At one modulus distinct atoms conflict; at distinct moduli they share no coordinate, so Δ=0. The conflict load of a fixed atom is (|Ω_p|−1)/p=o(1), and atom probabilities are 1/p=o(1).

Every n=x²+j, 0≤j<k, avoids all classes: at the jth shift the symbol is 0 or +1. For k≤x<y the gap y²−x²>k, so the intervals [x²,x²+k−1] are pairwise disjoint. Hence

    S_N ≥ k(⌊√(N−k)⌋−k+1) ≍ k√N.

The asserted scale follows; (N+Q²)e^{−μ}=o(1). ∎

**Corollary 2.2 (PROVED, elementary).** Even nearly perfect first/second CRT statistics on the actual interval do not repair this estimate with an O(√N) error. If m is the number of atoms, then m≤Q². Every individual atom and compatible pair intersection differs from its CRT expected COUNT by <1, and an incompatible intersection is identically zero. The sum of absolute normalized errors over all singletons and pairs is at most (m+m²)/N≤2Q⁴/N. Here N times this error is O((log N)^16)=o(√N), whereas the necessary remainder is ≫√N log log N. This does not rule out an error functional that magnifies low-order errors without bound; it rules out treating their raw aggregate as an admissible remainder in (AJ). The per-intersection <1 statement holds at every order, not merely two; what grows uncontrollably is the number of intersections and their aggregate error. The floor-function toy is only a sanity check, not evidence for a transfer theorem.

**Assessment / next attack.** The generic square floor is not a universal constant-times-√N floor: even a slowly growing union of translated squares survives. This sharpens the brief's elementary square control, but is not an ES-specific obstruction and gives no new exceptional-set exponent. Next retain the exact truncation term rather than replace the large-sieve denominator by its complete Euler product.

### 2.2 Finite verification

**CERTIFIED.** `scripts/z50_ajastra_toys.py`, `data/z50_ajastra/round1.json`; memory bounded, timeout 180 s. At N=10^6, k=4:

| Q | μ | Δ | maximum conflict load | actual avoiders | (N+Q²)e^{−μ} |
|---:|---:|---:|---:|---:|---:|
| 1000 | 4.45816 | 0 | 0.07333 | 13469 | 23167.31 |
| 2000 | 8.42779 | 0 | 0.07546 | 4164 | 1093.52 |
| 4000 | 15.38999 | 0 | 0.07257 | 3998 | 3.521 |

Each system contains all 3996 distinct positive translated squares x²+j≤10^6. Thus the last two rows refute the finite C=C₀=1 version too. These toys are not in the asymptotic Q=(log N)^4 regime; the theorem, not the finite rows, supplies that quantification. An independent exhaustive CRT/intersection check covers 225 pairs at moduli 3,5,7 and N=137.

### 2.3 Hostile review

**Opus hostile review: no FATAL/MAJOR; SOUND after minor repairs.** The requested identifier `anthropic/claude-opus-5-5:high` was rejected by the tool as unavailable; the same model resolved as `anthropic/claude-opus-5-5` in deep mode and performed the review. Session: `/home/pasky/.pi/agent/sessions/--home-pasky-projects-math-erdos-straus-claude-agent-worktree-0046--/2026-10-29T14-35-14-871Z_01a18816-2437-76dd-89bf-63569c482718.jsonl`. It reproduced all toy outputs, independently checked a smaller Legendre-symbol sieve, tested (2.2), and checked 77,246 five-slot certificates. Repairs: scope certificates to ES₅; give the actual Case-A modulus; clarify the higher-order floor-function observation.

**Assessment / attribution repair.** This has low novelty: squares/quadratic images are the classical sharpness examples for the large and inverse large sieve. See Green–Harper, *Inverse questions for the large sieve* (2014), https://arxiv.org/abs/1311.6176 (abstract visited), and the internal `EXCEPTIONAL_WEIGHTS2.md` Prop. 5.3 on quadratic alignment. The modest additional point is the growing translated-square family with vanishing conflict load, disproving a universal *constant-times* square-root remainder. No new ES theorem or priority claim follows.

## 3. Round 2: one-big-prime structure

### 3.1 Exact corrected hybrid for a common smooth modulus

**Theorem 3.1 (PROVED, classical large sieve with exact probability bookkeeping; no novelty claimed; Opus SOUND).** Let every event modulus divide sp for some p in a finite set of primes coprime to s. In the fibre n=c mod s, combine the active atoms into a forbidden set Ω_p(c) of residues mod p, with β_p(c)=|Ω_p(c)|/p<1. Let N_c be the number of n∈[1,N] in the fibre; omit empty fibres and fibres where an active event depends only on s (these are entirely forbidden). For each remaining nonempty fibre choose a frequency cutoff R_c≥1. With independent Bernoulli variables Y_p of parameters β_p(c), put

    D_c=∏_p p^{Y_p},    ν_c=Σ_p −log(1−β_p(c)).

Then

    S_N ≤ Σ_c (N_c+R_c²) e^{−ν_c} / Pr(D_c≤R_c).         (3.1)

If Λ_c:=Σ_p β_p(c)log p≤(log R_c)/2, then Pr(D_c≤R_c)≥1/2 and

    S_N ≤ 2 Σ_c (N_c+R_c²)e^{−μ_c},   μ_c=Σ_pβ_p(c).    (3.2)

In particular if Λ_c≤¼log N_c and μ_c≥m in every nonempty fibre, choose R_c=√N_c to obtain S_N≤4Ne^{−m}. Fibres with β_p=1 have no survivors and may also be omitted.

*Proof.* Write n=c+st. Since p∤s, this is an invertible affine change mod p, and the t range is an interval of N_c consecutive integers. The arithmetic large sieve gives its avoider count at most (N_c+R_c²)/S_c(R_c), where

    S_c(R)=Σ_{d≤R,d|∏p} ∏_{p|d} β_p/(1−β_p).

The complete sum is Z_c=∏(1−β_p)^{−1}=e^{ν_c}. Dividing every summand by Z_c gives exactly Pr(D_c=d), proving (3.1). Markov applied to log D_c, whose expectation is Λ_c, gives Pr(D_c>R_c)≤Λ_c/log R_c for R_c>1. At the endpoint R_c=1 the sufficient condition forces Λ_c=0, so there are no forbidden residues and the bound is trivial; empty prime sets are interpreted by empty products. Finally ν_c≥μ_c. ∎

**Scope.** This handles a bounded smooth part when its common period s is affordable, not merely when each separate smooth multiplier is small. For moduli kℓ with k≤K, s=lcm(1,…,K) may have log s≍K. In the internal 3/4 family K=X^κ and s is much larger than N at the useful scale. Once s≥N, every actual fibre has N_c≤1, so this enumeration cannot exploit a positive mass in (3.2). The 3/4 note avoids this loss by keeping the fibres inside a CRT model and transferring a truncated majorant. Formula (3.1) is a genuine interval theorem but remains a classical periodic Bessel argument and does not escape (D)19/25/27.

### 3.2 Why the missing denominator is exponentially expensive

**Lemma 3.2 (PROVED, elementary Chernoff bound; no novelty claimed).** In one fibre suppose every p≥P>1. Set μ=Σβ_p, ν=Σ−log(1−β_p), and k=⌊log R/log P⌋. If 0<k<μ, then

    log S(R) ≤ ν−μ + k + k log(μ/k).                    (3.3)

If k=0, S(R)=1. Moreover, for b=maxβ_p<1,

    0≤ν−μ≤Σβ_p²/[2(1−b)].                              (3.4)

*Proof.* D≤R implies K:=ΣY_p≤k. For t>0,

    Pr(K≤k) ≤ exp(tk)∏(1−β_p+β_pe^{−t})
             ≤ exp(tk+μ(e^{−t}−1)).

Choose t=log(μ/k), multiply by e^ν, and use the identity in Theorem 3.1. Equation (3.4) follows by summing −log(1−x)−x=Σ_{j≥2}x^j/j≤x²/(2(1−b)). ∎

**Assessment / critical scale.** The cubic mass in this paragraph is the CRT-model mass of `paper/es-threequarter-note.tex`, Theorem supply, not a mass obtained with an affordable actual fibre period. If the useful top primes have log p≍L, their mass is μ≍L³, and Σβ_p²=o(μ), then the cheap sufficient condition in (3.2) requires L⁴≲log N_c. If L=(log N)^α with α>1/4, (3.3) shows that the complete Euler product's saving μ is largely cancelled by the small probability Pr(D≤R). At α=1/3 and R≤√N, k=O((log N)^{2/3}), so log S(R)≤O((log N)^{2/3}log log N)+o(μ), rather than μ≍log N. For an actual negligible Σβ², this explicitly loses the desired power saving. For a whole prime range, splitting off the lower primes gives S(R)≤Z_low·S_top(R); one must optimize that split, not apply the single-band estimate blindly to all primes. These are calculations within the established large-sieve cap, not a new impossibility theorem for arbitrary interval methods. The affordable-period version with K≲log N instead has supply ≍L²log K and recovers the existing 2/3 bound with a log-log gain. See `paper/vaughan-loglog-note.tex` for the fibrewise argument (using a stronger Rankin tail), and KARY3 Theorem 5.1 for the stronger general truncated-majorant cap.

### 3.3 Round-2 review and numerical check

**CERTIFIED.** The same script checks 30 (fibre,cutoff) instances with N=10000, s=6, primes 5,7,11,13 and cutoffs 1,5,10,30,100. It enumerates the 16 subsets one at a time, verifies S(R)=e^ν Pr(D≤R) with exact rational arithmetic, compares the actual fibre avoider count with (3.1), and checks (3.3) whenever 0<k<μ. All pass; `data/z50_ajastra/round2.json`. These are small sanity checks: the Chernoff test exercises only k=1 in eight instances, and the interval bounds are loose.

**Opus hostile review: SOUND, no FATAL/MAJOR.** Session `/home/pasky/.pi/agent/sessions/--home-pasky-projects-math-erdos-straus-claude-agent-worktree-0046--/2026-10-29T14-51-46-415Z_01a18825-456f-76dd-89bf-635a879c4b75.jsonl`. It reproduced the files byte-for-byte and independently tested 596 random fibre systems and 2000 Chernoff instances. Minor repairs incorporated: R=1 and smooth-only events; common-period wording; explicit distinction between affordable and cubic-mass regimes; citations to existing stronger results; full-range/top-band distinction. The review confirms no new exceptional-set exponent.

## 4. Round 3: ES-specific structure and transfer

### 4.1 Exact pair distribution does not supply product independence

**Theorem 4.1 (PROVED, finite-field construction; hostile review pending).** For arbitrarily large prime q, put b=⌊q/9⌋ and β=b/q<1/8. There is a squarefree modulus M and a probability law ρ on its reduced residues with all of the following properties:

1. Every one- and two-prime-coordinate marginal of ρ is EXACTLY uniform product measure on units.
2. There are congruence atoms at q distinct prime moduli, with μ=b, Δ=0, atom probability ≤1/8 and conflict load <1/8.
3. Their avoidance probability under ρ is exactly (q−b)/q², whereas the unit-CRT avoidance probability is (1−β)^q≤e^{−b}.

Moreover, for any prescribed P₀, the selected primes can be taken in [P,2P] with P>P₀. With an enlarged period L, ρ extends to a law whose marginal mod EVERY d<P³ is exactly uniform on (ℤ/d)×. The normalized lower-tail error needed for a conclusion ρ(avoid)≤Ce^{−μ}+ε is therefore at least

    ε ≥ (q−b)/q² − Ce^{−b}.                             (4.1)

This obstruction applies to any inference, linear or nonlinear, asserted for all laws from only these exact marginals. It is NOT a counterexample to the uniform law on [1,N] or to the ordinary primes ≤N.

*Proof.* Choose q distinct primes p_i≡1 (mod q), indexed by i∈F_q. For fixed q, the prime number theorem in this progression permits choosing all of them in [P,2P] for sufficiently large P. Partition (ℤ/p_i)× into q equal buckets, labelled by F_q. Draw A,B uniformly in F_q and, independently conditional on these, choose n mod p_i uniformly from bucket Ai+B. CRT gives ρ.

For i≠j, the linear map (A,B)↦(Ai+B,Aj+B) is invertible. Thus any two bucket labels are independent uniform, and conditional uniform sampling within the buckets makes the entire two-coordinate residue distribution uniform, not just the hit indicators. Forbid all residues whose bucket label lies in a fixed set T⊂F_q of size b. Singleton atom probabilities are 1/(p_i−1), μ=qβ=b, and at a given prime the conflict load is β−1/(p_i−1)<1/8. Distinct atoms at the same prime are incompatible, and distinct primes are coprime, so Δ=0.

If A≠0, the q labels run over all of F_q and hit T. If A=0, avoidance holds exactly for B∉T. This proves the probability formula. Distinct affine polynomials give distinct label vectors, and every vector has the same number of unit-residue realizations, so ρ is also uniform on an explicit SUBSET of (ℤ/M)×, M=∏p_i.

For the extra level assertion put D=⌈P³⌉−1 (P may be integral) and L=lcm(M,1,…,D). Lift each selected residue independently and uniformly to its higher prime-power digits in L; choose every other prime-power coordinate uniformly on units. Each d≤D involves at most two distinct selected primes because each is ≥P. Its entire reduced residue marginal is therefore uniform by the proved two-coordinate property and independence of the additional digits. ∎

**Scope / novelty (Assessment).** Pairwise-independent affine codes are standard. This is an explicit arithmetic realization of their lower-tail obstruction with *all* AP marginals through a level, not a claim to invent pairwise independence. The inference-class exclusion is wider than Bessel proofs: it rules out an arbitrary nonlinear “first/second moments plus level D” theorem for arbitrary distributed sequences. But L is enormous relative to D, and no claim of polynomial level D≥L^θ is made. Consequently this is NOT a new 3/4 barrier for the actual interval sequence, and it must not be advertised as satisfying z50's strongest fallback. The missing ingredient is exactly interval/prime information not encoded in the stated marginals.

### 4.2 Can ES labels supply the missing ingredient?

**Existing PROVED structure.** LS7 Lemmas 1.1–1.2 give ℛ(M) labels −u/v with 4uvt=M+1 and, at p|M, a fixed residue a pins

    u=−av,   t=−1/(4av²)  (mod p).

Thus a residue pins two coordinates once the third is chosen. This controls collision sums and removes many arbitrary residue families, including the full freedom used in Theorems 2.1 and 4.1. Neither counterexample is claimed to have this ES triple structure.

**Attempt and exact failed step (Assessment).** Conditional on a smooth fibre, one-big-prime ES events become forbidden subsets Ω_p(c) at independent model coordinates. Their exact pair collision information is already as good as Δ=0 after merging each prime's residues. Yet Theorem 3.1 still has Pr(D≤R) in its denominator. Coordinate pinning is a statement about WHICH residues are in Ω_p, not about how [1,N] meets a long intersection of their complements. To use it nonlinearly one needs a signed count of interval representatives of simultaneous rational-label constraints when their modulus product exceeds N. The unconditional LS7 residue-dispersion estimates do not give that count: their conclusion concerns one-prime load distribution; the multi-prime height-cut version is explicitly false (LS7 Prop. 4.1), and RD′ remains open. No implication from GRH, EH, or OAI-003 to the missing count is proved here.

**No hidden escape by optimization (PROVED consequence of existing caps, not a new advance).** Let V_λ be the real span of all residue indicators of level≤λ dividing a common family period M, including constants. Finite linear-programming duality says

    max{ρ(avoid): ρ≥0, Eρ f=E_CRT f for every f∈V_λ}
      = min{E_CRT ν: ν∈V_λ, ν≥1_avoid everywhere}.       (4.2)

The right side is exactly the CRT-majorant problem, since ν≥1_avoid includes global nonnegativity. KARY3 Theorem 4.1 therefore supplies an EXACT-marginal law on the left with avoidance ≥exp(−Cλ^{3/4}) for its forced families. This explains why arbitrary nonlinear manipulation of ONLY these residue moments cannot escape. It is dual packaging of an existing result (compare INTERFREQ §3.1's moment LP), not a new independent barrier theorem. Interval support is absent on the left; imposing it is precisely the unproved extra input, not a technicality.

### 4.3 Fresh literature check and a possible but insufficient nonlinear tool

**CLAIMED external result, not used as an input.** A second live search located Croot–Mao–Pohoata–Yip, *A sharp inverse theorem for the quadratic large sieve*, arXiv:2607.15311v2 (September 2026), https://arxiv.org/html/2607.15311v2, whose full displayed argument was inspected. It uses positive quadratic-character mixtures and Jensen without assuming independence of the set's residues. Theorem 1.7 states that |A mod p|<(p+1)/2 for odd p≤(log N)^3 forces a quadratic intersection of size at least

    C |A|/√N · exp(c√(log N/log log N)).

This is a useful non-product tool, but not a bound |A|≤N^{1/2+o(1)}. Its transfer still truncates a Selberg-type weight to polynomial period. In ES, the currently available prime-local depletion is sparse, not half the residues; no hypothesis of that theorem is supplied by ES₅ or U failure. Its quantitative intersection can also be far smaller than |A|. No exceptional-set consequence follows. The Green–Harper inverse-sieve conjectures remain explicitly conjectures in that paper; I do NOT claim that (AJ) implies their quadratic-structure conclusions.

The original source https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf was also visited (§6, Problems 43–48). A search aggregator labelled a different entry “GREEN-086”; its page did not expose a precise problem statement, so it is not used as a source or as a claimed known-open reduction.

### 4.4 Round-3 numerical check and review

**CERTIFIED.** `data/z50_ajastra/round3.json` enumerates every affine polynomial for q=17,31,101. Three distinct-coordinate pairs per q have exactly uniform joint bucket distributions; the first and factorial-second moments match the independent model exactly. At q=101, μ=11, Δ=0 and the actual zero probability is 90/10201≈0.00882266, versus the CRT value 0.00000875054 and e^{−μ}≈0.0000167017. This verifies the finite-code ingredient, not the huge arithmetic lift or an actual interval claim. The script uses only O(q²) counters.

The required arithmetic controls are replayed from existing `z43_astra_check` helpers (not a duplicate census): 18 distinct hard/R-zero primes, 251 rational certificates, 50 odd squares, and numerator-8 slot checks at 17 and 241. Details and scope in §5 and `data/z50_ajastra/controls.json`. Hostile review pending.

## 5. Exceptional-set consequences and controls

Pending: E(N), ES₅, U and prime variants; squares, numerator 8, hard primes, R-zeros.

## 6. Final review and remaining gap

Pending. Do not merge without parent instruction.
