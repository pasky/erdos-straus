# z63 hostile cross-model review — EUCLID

Reviewed `side-agent/z63-euclid` at `7d3d9c49d`; registration checked at `4e853613a`.
**Verdict: ACCEPT-WITH-FIXES.** The core lemmas and sampled certifications pass. **NARROWED**, not DEAD, is defensible only as a finite, known-set-specific assessment. ES and (S) remain open.

## Per-claim audit

| Claim | Classification | Independent reasoning / limitation |
|---|---|---|
| E1: matrices and index | **CORRECT** | Multiplying the continuant matrices gives `M=[[n,-A′],[A,-A″]]`; determinant one gives `AA′=1 mod n`. Thus `SM=[[-A,A″],[n,-A′]]` and `(d/n)=(A/n)` when `n=1 mod 4`. |
| E1: character nontrivial iff nonsquare | **CORRECT** | Products multiply lower-right entries mod n. Surjectivity onto units is implicit but elementary: choose `ad=1 mod n`, then `[[a,(ad-1)/n],[n,d]]` lifts d. CRT isolates a nonsquare unit at a prime occurring to odd exponent; at squares every unit has Jacobi +1. Descent through ±I requires `n=1 mod 4`. |
| E1: presentation complex / H₁ | **CORRECT** | The finite cover of the PSL₂ presentation complex has the asserted subgroup as fundamental group. Its first homology is the abelianization, including order-two elliptic classes. The signature presentation gives `e₂+2g+c−1`. Each displayed HJ word closes; this is NOT a bijection between HJ paths and arbitrary loops, nor ordinary homology of the underlying compact modular curve. |
| Integer total; (S) reformulation | **CORRECT** | A nontrivial character pairs the units into equal sign classes, giving φ(n)/2. At primes `p=1 mod 4` this count is even. For nonempty L₃, nonvanishing on its span is exactly existence of a negative-symbol word; at 105 the implication (S) is vacuous. |
| E2: Hecke eigenrelation | **CORRECT** | In the transfer sum, `d_i=d z_i x_{σ(i)}/ℓ mod n`. The product of the correction factors is one because σ permutes the representatives and `x_i z_i=ℓ`. Their additive Jacobi characters therefore sum to zero, leaving `(ℓ+1)χ`. This includes ℓ=2 and composites, provided ℓ∤n and `n=1 mod 4`. |
| E3: fake-cocycle criterion | **CORRECT** | A common-span vector of χ-value one obstructs every fake. Conversely `ψ(k+c)=χ(k)` is well-defined exactly when χ vanishes on the intersection; extend a basis to H. Empty candidate sets and zero χ cause no exception. |
| E3′: scoped consequence | **CORRECT** | Under ONLY the two stated information restrictions, fakes are indistinguishable. Independence of the high vectors modulo K+low makes all their values freely assignable. The intersection reduction follows by moving the high component to K+low. This says nothing universal about enlarged K, Hecke constraints, or integer balance. |
| §4.1 CERTIFIED ranks | **CORRECT (sampled; aggregates agree)** | Independent full-chain computation, with no imported lane code or Schreier tree, agrees at five primes for both parameter settings. Lane reruns also agree at a larger prime, a square and composites; details below. |
| KE2 numbers / interpretation | **CORRECT numbers; CORRECT-WITH-FIX interpretation** | Four Hecke reruns agree. Affine dimension zero means K plus Hecke equations determine **every** χ-value by finite linear algebra, including on generic loops. “Without supplying its values” / “gives no new way to evaluate it” is false literally; no **uniform nonvanishing theorem** is supplied. |
| KE1 registration and handling | **CORRECT-WITH-FIX** | The checkpoint precedes the computation commits. Final disclosure that the forced list was never fixed and the height split is post-hoc is honest. But 46/46 index-positive inputs does not count non-forced relations: the statistic includes the explicitly forced overlap identities. It cannot alone establish the stated non-forced >10% explanation. |
| (S), five slices, prior source | **CORRECT attribution / conditional implication** | The exact conjecture is already HJ_DEEP §3, not new here; the sign-to-five-slice implication is DEDEKIND_ES Thm 4.5. Its explicit ES identities and length-three dictionary match the usage. The prime word families prove (W) for p>5; L₃(5) is empty. The R174 extension to 10⁹ is actually recorded in HJ_DEEP, but was not rerun here. |
| E5 proved pieces / missing lemma | **CORRECT, with scope clarification** | Character factorization through the triangular reduction and the subgroup-containment reformulation are immediate. A χ-odd intersection vector is exactly what the restricted linear approach needs, not evidence that one exists uniformly. Reaching a *generic* loop is a proposed escape, not a proved necessary condition for every uniform proof of (S). |
| §§8–9 broad summary | **CORRECT-WITH-FIX** | “No relations with the rest beyond a bounded-height menu” must mean the tested K and levels. The memo's own p=1009 enlarged-known-set computation contradicts the unrestricted reading. No infinite failure theorem for the low menu was proved. |

E1/E2/E3 were re-derived above rather than accepted on the remembered Manin/Mazur references. Those references are background, not a verified attribution of the precise mod-two E2 statement.

## Recomputations

All execution used `ulimit -v 4000000`; every run had timeout ≤1800 seconds. No dense Cartesian-product arrays were used.
Independent audit: `timeout 1800 uv run --with sympy scripts/z63_xrev_euclid_check.py /tmp/xrev_EUCLID`.
The temporary tree was extracted with `git archive side-agent/z63-euclid` (lane scripts/data plus z58 screens).

| p | dim H₁ | short loops | high count = rank increment, B10/H20 | high count = rank increment, B30/H60 | all-short fake, B10 / B30 |
|---|---:|---:|---:|---:|---|
| 193 | 33 | 18 | 0 | 0 | no / no |
| 1009 | 169 | 20 | 10 | 0 | yes / no |
| 2953 | 493 | 38 | 16 | 0 | no / no |
| 5569 | 929 | 32 | 16 | 2 | yes / yes |
| 9601 | 1601 | 42 | 24 | 10 | yes / yes |

The independent code uses all directed graph edges, explicit relator chains, and a separate affine-consistency calculation; it also matches rank(K). The low/high tests use the stated height, not the outer HJ letters.
Lane H₁ rerun: `BMAX=30 HIGH=60 uv run scripts/z63_euclid_h1.py 193 2953 9601 18481 105 1465 2401` (timeout 300); all output fields match saved rows. At 18481, high count/increment=22/22; at 1465, 1/1; at 2401, χ is zero.

| Hecke rerun p | dim E | affine dim | χ∈E | all-short fake | high-zero fake with low values fixed |
|---|---:|---:|---|---|---|
| 193 | 3 | 0 | yes | no | yes |
| 1009 | 3 | 1 | yes | yes | no |
| 2953 | 7 | 1 | yes | no | no |
| 5569 | 5 | 1 | yes | yes | no |

Command: `BMAX=10 HIGH=20 LS=2,3,5,7,11,13 uv run scripts/z63_euclid_hecke.py 193 1009 2953 5569` (timeout 600). All fields match.
Allheight rerun reproduces p=1009: 510 low-height loops, rank 125, ten high short loops with increment seven; the three printed dependencies match exactly.
R₈ witness script rerun matches all twelve recorded words exactly (timeout 60).

Saved-data aggregates independently summed, **not full population reruns**:
- KE1 primes: 267 inputs, 12,764 short loops; high increments 2,584 / 7,244, zero deficits; index-positive 262 / 214 (B30 / B10).
- Controls: 108 rows, **102 distinct levels**, 1,966 short loops; high increments 366 / 1,022; index-positive 31 / 18. Totals include the six duplicated levels, as disclosed in §4.1.
- KE2: 89 inputs; dim E counts `(3:78, 5:3, 7:4, 9:3, 11:1)`; affine counts `(0:68, 1:16, 2:4, 3:1)`; fake counts 14 / 15. All rows have χ∈E.

## Mandatory falsifier audit

| Screen | Independent result | Consequence |
|---|---|---|
| F1 odd squares | Jacobi triviality proves zero index everywhere; square rerun at 2401 agrees. | Correct T1 behavior, but H₁-independence alone does not distinguish squares from primes. |
| F2 twelve R₈ zeros | Direct divisor search finds an interior negative-symbol word at all 12; max first successful u=8. HJ length and membership in the five-slice union are checked. | Correct: numerator-8/C-even failure does not refute the broader (S) target. |
| F3 285 composite zeros | **284 explicit negative-symbol length-three witnesses; 105 has no L₃ word**, independently checked over every unit. Max first successful u=52. | All 285 satisfy the conditional statement (S); do not describe 105 as possessing a certificate. |
| F4 14 (★) / 38 𝔊* prime zeros | Independent witnesses at all 14 and all 38; max first successful u=22 in each list. | Correct; this does not establish a homological forcing mechanism or a HOT LEAD. |

These checks verify (S) on the supplied screens; they do not rerun the separate computations establishing that the inputs are zeros of their respective narrower families.

## Required fixes, priority order

1. **Hecke conclusion:** replace “pins χ down without supplying its values” by “determines and permits computation of all its values at 68/89 tested levels, but supplies no uniform proof that some short-loop value is nonzero.” The literal stronger negative claim is not justified by KE2.
2. **Scope in export / bottom line:** consistently say “for these finite levels and these known sets.” Retain the p=1009 counterexample to enlargement and the absence of any proved infinite failure of the low menu. Do not turn the missing generic-loop relation into a necessary condition for all approaches.
3. **KE1:** retain “not evaluated as registered.” Separate the verified raw 46/46 index-positive count from the unreported classification/count of non-forced relations; do not present the former as proof of the latter.
4. **Notation:** use `H₁(Γ₀(p)/±1; F₂)` consistently in the missing lemma, or explain the switch to SL₂. Say “HJ paths give distinguished loops,” not a literal equivalence with all loops. State the `n=1 mod 4` descent hypothesis wherever the PSL₂ character is exported.

**Bottom line:** accept the elementary lemmas, the finite certifications with their stated parameters, and a carefully scoped NARROWED assessment. Do not record a general Euclidean-index impossibility theorem, a successful registered kill, or a Hecke no-go result.
