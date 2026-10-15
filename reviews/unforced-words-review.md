# R233 — hostile review of O231 (UNFORCED_WORDS.md, BRAINSTORM/z7_*.md)

Reviewer branch side-agent/review-unforced-words (merged side-agent/unforced-words). From-scratch scripts:
`scripts/review_r233_*`. ES is not solved; nothing below changes that.

## Summary verdicts (filled in progressively)

| # | claim | verdict |
|---|---|---|
| 1 | Lemma 1.1 (n ≡ 5 (8) trivial) | SOUND |
| 2 | Prop F, Cor 1.2 | SOUND (MINOR notation D2) |
| 3 | Prop F′ (s = 3, 4, 7), Cor 3.1 | pending numerics |
| 4 | Lemma 2.1, Flip Lemma 2.2 | pending |
| 5 | Thm 3.2 (Dickson) | pending |
| 6 | U2 sandwich, CONJECTURE U2 | pending |
| 7 | Remark 4.1 | pending |
| 8 | Prop 5.1 (Haar 3/4) | pending |
| 9 | Lemma 5.2 | pending |
| 10 | SHARP 1 (failures ⟹ ψ-odd part of n+1 = 3²) | pending |
| 11 | Lemma 6.1 / 105 genus collapse | pending |
| 12 | SQ_± split | pending |
| 13 | labels | pending |

## Claim 1 — Lemma 1.1: SOUND
Re-derived. (1, n+2, 2): 2(n+2) − (n+2) − 2 = n. A = n+1, B = 1; sides N_t = n+1 (≡ 6 (8), so 2 ∥ N_t with
ψ(2) = (2/n) = −1), N_u = 2(n+1), N_v = n+2 with ψ(n+2) = (2/n) = −1 (an odd number of ψ-odd prime factors).
χ = ψ(n+1) = ψ(1) = +1. Non-squareness is automatic for n ≡ 5 (8). Nothing to repair.

## Claim 2 — Prop F, Cor 1.2: SOUND
Re-derived the four parametrisations: t = 1 ⟺ (u−1)(v−1) = n+1 (A = u−1); u = 1 ⟺ (t−1)v = n+1 (A = t−1, N_u = n+1);
t = 2 ⟺ (2u−1)(2v−1) = 2n+1; u = 2 ⟺ (2t−1)v = n+2. In each, every positive divisor of the fixed side X is an
admissible D and gives a positive word. (iii)⇒(i) with D = r; (i)⇒(ii) Lemma S; (ii)⇒(iii) definition. Note the
proof never uses n ≡ 1 (8) (for n ≡ 5 (8) r = 2 is allowed) — harmless. The proof is valid for composite n as well
(X is coprime to n, so no ψ = 0 primes occur). Cor 1.2 ✓. Cor 3.1's "min = K(p)+1" for the certificate is also right:
the certificate of the s-family cannot have another coordinate < s, because that coordinate's side is clean by K(p) ≥ s−1.
