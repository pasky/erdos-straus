# R224 — hostile review of O217 THREE_SQUARES.md (+ memos BRAINSTORM/y8_*.md, AGENT_REPORT_O217)

Reviewer: R224 (side-agent/review-three-squares). Merged side-agent/three-squares at its tip (README conflict: kept both).
All numerics re-done with from-scratch code `scripts/review_r224_*.py` (author scripts not reused).

## Summary verdicts
| claim | verdict |
|---|---|
| Lemma 1.1, Lemma 1.2 (a)–(c), rank-one sterility | **SOUND** (MINOR D1 wording, D2 two inconsistent "clean" conventions) |
| Prop 1.3 (square test) | **SOUND** (MINOR D2) |
| Prop 3.1 | **SOUND** (MINOR D3 citation/hypothesis) |
| Lemma 3.2 (Mordell 840 = lnr level) | **SOUND** (MINOR D4 "exactly Mordell") |
| (further rows added below as checked) | |

## Claim-by-claim

### Lemma 1.1 / 1.2 — SOUND
Re-derived. AA* = (tu−1)(tv−1) = t(tuv − u − v) + 1 = tp + 1, so A | tp + 1, gcd(A, p) = 1, AA* ≡ 1 (p) gives
(A/p) = (A*/p); p ≡ 1 (4) gives (−A/p) = (A/p); multiplicativity gives the product. For odd r | tp + 1 (so r ∤ t,
r ≠ p): (r/p) = (p/r) and p ≡ −t⁻¹ (r) gives (p/r) = (−t/r). (a) every prime of A divides tp + 1. (c) ((tp+1)/p) =
(1/p) = 1; if tp + 1 = s·ℓ^e with s (lnr−1)-smooth then (s/p) = 1, so (ℓ/p)^e = 1, e odd ⇒ (ℓ/p) = 1. Correct, and the
"only this exact form" caveat is right (two rough odd-exponent primes can both be −1; even exponent unconstrained).
Checks (`scripts/review_r224_lemmas.py`): every word of every prime p ≡ 1 (4) < 1500 (words enumerated two
independent ways, (t, A)-divisor form and direct (u, v) search — identical sets): χ = (A/p) = (A*/p) = ∏(r/p)^e,
0 failures; reciprocity constraint for t < 60 at all those p, 0 failures; clean ⇒ no χ = −1 word, 0 failures;
(r/p) = (−t/r) for all odd r | tp + 1, 0 failures. Rank-one form (one rough prime ≥ lnr with odd exponent, or none):
667 levels (p ≡ 1 (4) in (2·10⁵, 2.03·10⁵), t < 40), all 667 clean. Counterexample p = 200 881 (prime, lnr 11),
14p + 1 = 3·5·433², (3/p) = (5/p) = 1, (433/p) = −1: confirmed.

### Prop 1.3 — SOUND
⇒ trivial. ⇐: for odd non-square n write n = m²n′, n′ > 1 squarefree odd; r ↦ (n′/r) is a non-principal character
(Jacobi/Kronecker, modulus | 4n′), so some odd prime r ∤ n has (n/r) = −1; t ≡ −n⁻¹ (r) gives r | tn + 1.
Check: all odd n < 3000: non-squares have an unclean level (found by search), odd squares have no unclean level
t ≤ 300; 0 failures.

### Prop 3.1 — SOUND
Words ↔ pairs (t, A) with A | tp + 1, A ≡ −1 (t) is a bijection (u = (A+1)/t; AA* ≡ 1 (t) ⇒ A* ≡ −1 (t), v = (A*+1)/t;
tuv − u − v = (AA* − 1)/t = p). Verified against direct enumeration above. ES-five ⟺ N₋ ≥ 1 is imported.

### Lemma 3.2 — SOUND
Re-derived the residues: q = 3 ⇒ p ≡ 2 (3) ⇒ t₀ = 1; q = 5 ⇒ p ≡ 2, 3 (5) ⇒ t₀ = 2, 3; q = 7 ⇒ p ≡ 3, 5, 6 (7) ⇒
t₀ = 2, 4, 1; all divide q + 1; A* = (t₀p+1)/q ≡ −1 (t₀) from AA* ≡ 1. The six classes mod 840 are exactly the odd
squares coprime to 105 mod 840 (computed). Check over all 36 805 primes p ≡ 1 (4) < 10⁶ with lnr ≤ 7: the stated word is
a valid χ = −1 word in every case; lnr ≥ 11 ⟺ p mod 840 ∈ {1, 121, 169, 289, 361, 529}: 0 mismatches over all
p ≡ 1 (4) < 10⁶.

## Defects
D1 (MINOR) — Lemma 1.2(b) and Summary item 2: "Every prime r < lnr(p) is clean" mixes the level notion with primes.
Repair: "(b) every prime r < lnr(p) has (r/p) = +1, so a level t with tp + 1 (lnr − 1)-smooth is clean."

D2 (MINOR) — two different definitions of "clean": §1 Definition (all primes r | tp + 1, INCLUDING 2, symbol (r/p)) and
Prop 1.3 (ODD primes only, symbol (n/r)). For p ≡ 5 (8) and odd t these differ (2 | tp + 1, (2/p) = −1: unclean in
§1, possibly clean in Prop 1.3); the §2 statistics use the §1 notion. Summary item 2 and the AGENT_REPORT juxtapose them
as one notion. Repair: call the Prop 1.3 notion "odd-clean" (or state that for n = p ≡ 1 (4) the two notions agree
except at r = 2), and say Prop 1.3 is stated for the odd-clean notion.

D3 (MINOR) — Prop 3.1 cites "CHI_FLIP + TWO_FIBRES Thm A"; the needed input is ES-five(p) ⟺ N₋(p) ≥ 1, which is
MODEL_SPECIFIC Thm 3.1(a) (with CHI_FLIP Cor 1.3), as TWO_FIBRES Cor A1 itself says after R214 D4; the (t, A)
bijection is elementary. Also state the hypothesis p ≡ 1 (4) prime in the Prop (χ = (A/p) uses it).

D4 (MINOR) — Lemma 3.2 "this is exactly Mordell's congruence theorem on ES-five": it recovers the prime case of Mordell's
covering set (same exceptional classes), via different (one-word) certificates; Mordell's theorem is a statement about
polynomial identities for all n. Repair: "recovers, at primes, the covering set of Mordell's theorem".
