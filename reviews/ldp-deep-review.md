# R177 — hostile review of O177 (LDP_DEEP.md + BRAINSTORM/bsD_*.md)

Reviewer branch `side-agent/review-ldp-deep` (merged `side-agent/spark-higher-reciprocity`). From-scratch scripts:
`scripts/review_ld_*.py`. Labels as in DISCOVERIES.md. **ES is not solved anywhere; nothing below changes that.**

## Summary verdicts (filled in claim by claim)

| # | Claim | Verdict |
|---|---|---|
| 1 | bsD_eichler_degree_k Prop 1 / LDP_DEEP Prop A.3.1 | (pending) |
| 2 | bsD_eichler_degree_k Prop 2 / LDP_DEEP Prop A.3.2 + "degree-2 accident" slogan | (pending) |
| 3 | bsD_brauer_cores Thm 1 / LDP_DEEP Thm A.1 | (pending) |
| 4 | LDP_DEEP Prop A.4.1, A.4.2, F-Gram construction | (pending) |
| 5 | EVIDENCE: split-supported Type II certificates, cd ≤ 30 | (pending) |
| 6 | bsD_frobenius_closure Thm 2 (+ cubic dictionary) | (pending) |
| 7 | bsD_missed_primes numbers (71; layers 2/12/0) | (pending) |
| 8 | bsD_genus_vacuity_LDp Prop 1, Remark 2 / LDP_DEEP B.1–B.2 | (pending) |
| 9 | LDP_DEEP B.0 Gram form | (pending) |
| 10 | spot checks: bsD_metaplectic_cubic, bsD_drinfeld_rank_k, bsD_artin_conjugation | (pending) |

## Detailed findings

## Defects

### Claim 5 — EVIDENCE "all but 5 of 9732 primes p ≡ 1 (24) < 10⁶ have a cd ≤ 30 Type II certificate whose f or f′ is an F-norm" — SOUND (numbers reproduced exactly; interpretation needs a caveat)
From scratch (`scripts/review_ld_split.py X 30`; own divisor enumeration from the factorisation; **every certificate is
converted into an explicit ES solution 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp), a = (f+1)/M, b = (f′+1)/M, and checked in
exact rationals**). Two definitions of "F-norm" (F = ℚ(ζ_M)⁺, M = 4cd):
S1 = author's "split-supported" (every ℓ | f has ℓ ≡ ±1 mod M; sufficient), S2 = exact criterion (f = N_{F/ℚ}𝔞 for an
O_F-ideal ⟺ for every ℓ^v ‖ f the residue degree g_ℓ = ord of ℓ in (ℤ/M)^×/{±1} divides v).

| X | #p ≡ 1 (24) | no cert | no S1 cert | no S2 cert | no cert with both sides S1 / S2 | frac certs S1 / S2 | frac with f or f′ prime |
|---|---|---|---|---|---|---|---|
| 2·10⁵ | 2212 | 0 | 3 (3361, 53089, 76441) | same 3 | 338 / 293 | 0.603 / 0.621 | 0.565 |
| 10⁶ | 9732 | 0 | 5 (3361, 53089, 76441, 549553, 967129) | same 5 | **1345** / 1178 | **0.582** / 0.601 | 0.536 |

Odd squares < 4·10⁴: 0 Type II divisor hits (T1 control) — reproduced. All author numbers (9732; 0; the 5 exceptions;
1345; 58%) reproduce exactly with S1; the exact notion S2 changes neither the exception list nor the conclusion.
**Caveat (defect D5):** 0.536 of all certificates have f or f′ *prime*, and a prime f ≡ −1 (mod M) is automatically
≡ ±1, i.e. automatically an F-norm. So "F-norm certificates exist" is ≈ "a certificate with a prime side exists";
the statistic carries essentially no information about the F-structure, which is consistent with (and actually
strengthens) the author's own "tautology" reading in A.4.2.
