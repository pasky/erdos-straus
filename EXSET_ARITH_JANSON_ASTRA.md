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

Pending: statement, adversarial families, proof or counterexample, enumerable toy tests, hostile review.

## 3. Round 2: one-big-prime structure

Pending: corrected theorem and comparison with CRT truncation, numerical verification, hostile review.

## 4. Round 3: ES-specific structure and transfer

Pending: rational labels/coordinate pinning, nonlinear obstruction or surviving route, hostile review.

## 5. Exceptional-set consequences and controls

Pending: E(N), ES₅, U and prime variants; squares, numerator 8, hard primes, R-zeros.

## 6. Final review and remaining gap

Pending. Do not merge without parent instruction.
