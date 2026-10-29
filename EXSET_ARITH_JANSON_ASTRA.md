# Arithmetic Janson–large-sieve hybrid (z50 C2, ajastra)

## 0. Summary and status

**Scope.** Long, adversarial exceptional-set attempt. ES remains open. No new exceptional-set estimate is claimed at initialization.

| Round | Target | Status | Review |
|---|---|---|---|
| 1 | Audit and universal arithmetic Janson | Pending | Pending |
| 2 | One-big-prime families and corrected bounds | Pending | Pending |
| 3 | ES-specific rescue or enlarged barrier | Pending | Pending |
| Final | Exponents, controls, exact surviving gap | Pending | Pending |

Labels used: PROVED, CONDITIONAL (named hypothesis), CERTIFIED (finite computation), EVIDENCE, CONJECTURE, Assessment. All advances require hostile cross-model review before acceptance.

## 1. Audit and references

**Assessment / scope audit.** Read the z48 and z49 contexts and the binding z50 context twice; FRONTIER §§2–4,6–7, BREADTH_Z45, the PR-B map and arithmetic/covers supplements, OAI_DUMP_IMPACT's audit, and the z48 forest/lower-tail summaries (FOREST_H4 §§3.5,5). The relevant model input is CONJECTURE_S_MODEL §2, not an independence assertion for actual integers. Its atomic Janson proof is in `paper/es-subexp-note.tex` §Janson: conditioning on an atom deletes coordinates in a PRODUCT probability space. Arithmetic first/second moments do not justify that deletion.

**Existing results, not new.** DISCOVERIES (D)17–(D)31 were read in full. EXCEPTIONAL_LARGESIEVE §§1–3 gives the exact CRT-admissible large-sieve/positive-square duality; (D)25 covers periodic Bessel rows, twists and hybrids; (D)27 covers one-big-prime forced families even at arbitrary frequency level; (D)28 handles residue-sparse multi-rough families. Thus simply renaming a periodic Bessel inequality “Janson” cannot help. A positive result here would need actual interval information, door (i), or a nonlinear conditioning theorem with new arithmetic input, door (vii). The counterexamples below are about the proposed estimates themselves, not about Bessel implementations.

**Precise target (CONJECTURE to be tested).** For distinct congruence atoms B_i={n≡a_i (q_i)}, q_i≤Q, let ν be uniform CRT measure, μ=Σ_i ν(B_i), and Δ=Σ_{i<j,(q_i,q_j)>1}ν(B_i∩B_j). Conflicting pairs contribute zero. On [1,N] let S_N be the avoider count. Test

    S_N ≤ C(N+Q²) exp(−μ+KΔ) + R(N,Q).                    (AJ)

Here C,K are absolute and a useful proposed error is R=N^{1/2+o(1)}; first test R=0 and R=C₀√N. Atomic probabilities ≤1/8 and conflicting probability load ≤1/8 will be imposed in counterexamples, so the model theorem's smallness hypotheses are not silently discarded. For prime inputs the model is uniform units and atom density is 1/φ(q), not 1/q. No prime-input counterexample is inferred from composite squares.

**Certificate-class audit.** In covering coordinates n=(tu−1)v−u, put A=tu−1. If 4|t, then A≡3 (4), u|(A+1)/4, and −u is an ℛ(A) label (take reduced ratio u/1 in LS7 Lemma 1.1). If 4|u, write u=4d: A=4td−1 and −u=−4d is an ℛ(A) class because d|((A+1)/4)². If 4|A, write A=4m: −u mod4m, u|4m+1, is the Type-I Case-A class with fixed a=1,d=m. Swap u,v for the other two slots. Thus every certificate has a forced-class encoding of one of the capped types. This is an encoding of witnesses, NOT a claim that every endpoint event is literally the same atom at the same modulus: refinements/unions and positivity ranges must be retained. In particular, a cap for a re-encoded family must be applied at its actual level. The one-big-prime Type-II family is directly in the ledger; no unverified transfer of its exponent to U will be made.

**Literature check (Assessment, 2026-10-29).** A live search for “Erdos Straus exceptional set 2026 Vaughan Pomerance Weingartner” located Pomerance–Weingartner, *Exceptions to the Erdős–Straus–Schinzel conjecture*, Ramanujan J. 69, 31 (2026), https://arxiv.org/abs/2511.16817, and the March 2026 Pomerance talk slides https://math.dartmouth.edu/~carlp/esconjfl.pdf (search hit only). Visited https://arxiv.org/html/2511.16817v2: §4 proves the 2/3 bound by the truncated large-sieve Euler product, with mass ≍log²X for the full Vaughan prime classes. No newer stronger published exceptional-set estimate was located. This limited search is not an exhaustive literature certification. Note the distinction from the *prime-coordinate forest subfamily*, whose mass is only ≍log X; the full Vaughan ℛ(ℓ) family has log²X mass. No OAI-003 hypothesis is used here.

## 2. Round 1: universal hybrid

### 2.1 Translated-square obstruction

**Theorem 2.1 (PROVED relative to the standard Weil bound for quadratic character sums; hostile review pending).** There are prime-modulus families with Q=(log N)^4, Δ=0, all atomic probabilities and all conflict loads ≤1/8, and μ≫(log N)^3/log log N, whose actual integer avoider count satisfies

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

**Corollary 2.2 (PROVED, elementary).** Even nearly perfect first/second CRT statistics on the actual interval do not repair this estimate with an O(√N) error. If m is the number of atoms, then m≤Q². Every individual atom and compatible pair intersection differs from its CRT expected COUNT by <1, and an incompatible intersection is identically zero. The sum of absolute normalized errors over all singletons and pairs is at most (m+m²)/N≤2Q⁴/N. Here N times this error is O((log N)^16)=o(√N), whereas the necessary remainder is ≫√N log log N. This does not rule out an error functional that magnifies low-order errors without bound; it rules out treating their raw aggregate as an admissible remainder in (AJ).

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

Pending Opus review of Theorem 2.1, Corollary 2.2 and the audit's encoding claims.

## 3. Round 2: one-big-prime structure

Pending: corrected theorem and comparison with CRT truncation, numerical verification, hostile review.

## 4. Round 3: ES-specific structure and transfer

Pending: rational labels/coordinate pinning, nonlinear obstruction or surviving route, hostile review.

## 5. Exceptional-set consequences and controls

Pending: E(N), ES₅, U and prime variants; squares, numerator 8, hard primes, R-zeros.

## 6. Final review and remaining gap

Pending. Do not merge without parent instruction.
