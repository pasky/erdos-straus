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

## Claim 3 — Prop F′ (s = 3, 4, 7) and Cor 3.1: SOUND
Re-derived. Odd r | p+s or sp+1 has ψ(r) = (p/r) = (−s/r); ψ(2) = +1 at p ≡ 1 (8). s = 3: 4 ∥ X, D ∈ {r, 2r}
reaches the class 2 (3) (3 ∤ X). s = 4: ψ(D) = (−1/D) = −1 for every admissible D. s = 7: 8 | X, 7 ∤ X, ψ(r) = (r/7),
r·⟨2⟩ = the NR coset ∋ 6. The 2-adic remark ("every word is a certificate when 4 | s or s ≡ 7 (8)") is also right:
−s is then a fundamental-type discriminant whose Kronecker character is a character mod s with value −1 at −1, and
(−s/2) = +1 = ψ(2) when s ≡ 7 (8).
From-scratch brute force `scripts/review_r233_propF.py 100000` (all 2 384 primes p ≡ 1 (8) < 10⁵; every word of each
family enumerated, cleanliness by full factorisation, Lemma S asserted): 0 mismatches of
"unclean ⟺ certificate ⟺ unforced" for s ∈ {1, 2, 3, 4, 7}, both family kinds. Controls reproduce the author's
numbers exactly: unclean ≠ certificate at s = 5: 310 (t) / 280 (u); s = 6: 328 / 183; s = 8: 297 / 290;
unforced ≠ certificate only at s = 5: 24 (t) / 39 (u).
Cor 3.1 follows (U = 0 or N₋ = 0 ⟹ all nine sides clean ⟹ K(p) ≥ 4 and p+7, 7p+1 clean). The "min = K(p)+1"
clause is right (see Claim 2).

## Claim 5 — Thm 3.2 (CONDITIONAL on Dickson): SOUND-AFTER-REPAIRS (D3, MINOR)
Re-derived. With p = 1 + Mx and every prime power ℓ^{a_ℓ} ∥ M exceeding K+1, (s+1) | M and p+s = (s+1)L_s,
sp+1 = (s+1)L′_s; the 2K distinct forms all have constant term 1 (≢ 0 mod ℓ | M) and, for ℓ > 2K+1, cover ≤ 2K < ℓ
residues: admissible, no local obstruction, all leading coefficients positive. Prime factors of s+1 are ≤ K+1 and
divide p−1, so ψ = +1; ψ(L_s) = ψ(s) = +1, ψ(L′_s) = ψ(1)ψ(s+1) = +1; a prime with ψ = +1 is clean. Label
CONDITIONAL is correct. Illustration `scripts/review_r233_dickson.py K` finds the predicted primes:
K = 2: p = 25 561, 53 281, 156 241; K = 3: 15 555 961, …; K = 4: 36 070 209 001, … — all with K(p) ≥ K verified by
direct factorisation.
**D3 (MINOR).** UNFORCED_WORDS.md §3, Thm 3.2 proof: "M = 8·∏_{3 ≤ ℓ ≤ 2K+1} ℓ^{a_ℓ} … (also 2^{a_2} > K + 1)" —
as written the 2-part of M is 8, so for K ≥ 15 (s+1 = 16) (s+1) ∤ M and L_s is not integral. Repair: M =
2^{a_2}·∏_{3≤ℓ≤2K+1} ℓ^{a_ℓ} with a_2 ≥ 3 and 2^{a_2} > K+1.
