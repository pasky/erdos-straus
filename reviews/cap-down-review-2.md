# Hostile review #2 of CAP_DOWN.md (O237) — R243, round 1

Reviewer: R243 (side-agent/review-cap-down-2). Round 1: no edits to the author's files. Reviewed: CAP_DOWN.md as merged
from side-agent/cap-down (iteration Z7-1/Z7-2 + self-review repairs), BRAINSTORM/z13_*.md. From-scratch scripts:
`scripts/review_r243_lemmas.py` (lemmas, exact Fractions), `scripts/review_r243_caps.py` (numerics). Pollack's paper
(author's PDF, pollack-math.net/generalsplit6.pdf) archived as `sources/r243/pollack-ijnt2014-generalsplit6.{pdf,txt}`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (general Type II window with cap) | SOUND |
| Thm 1.2 (even windows fire, (E)) incl. Def 1.1 compatibility of the 2^t in d | SOUND |
| Prop 1.3 (one-prime witness d = K·s^{o/2}, cap ≤ (q−3)/4) | SOUND |
(continued below as checks complete)

## Detailed checks

### Lemma 1.1 — SOUND
Re-derived. 4/n − 1/K = m/(nK); 1/(nA) + d/(nKA) = m/(nK) ✓. All primes of d divide K, none divides m (s | K, s | m ⇒ s | n,
excluded by (i)); so v_s(A) = v_s(K + d) and v_s(z) = b + v_s(A) − c equals b (c < b), ≥ b (c = b), 2b − c (c > b) ✓.
2-part of den z trivial by (ii), odd parts even by (iii), coprime to n by (i), s | A | y when c_s > 2b_s ≥ 2 ✓. No prime
outside K can occur in den z (den z | d up to cancellation) ✓.
*From scratch:* exhaustive over all odd n ≤ 600, windows m ≤ 60, every K-smooth d ≡ −K (mod m) with c_s ≤ 2b_s + 6
(51 725 triples): Lemma 1.1's predicted cap (None when (ii)/(iii) fail) equals the least e with the triple in
EXPONENT_CAP Def 1.1, computed directly from den z, y, n with exact Fractions — no mismatch. Note this also confirms the
converse direction (a triple violating (ii)/(iii) is in no ES^{(y,e)}), which Lemma 3.1 later uses.

### Thm 1.2 — SOUND
Re-derived line by line: gcd(K, qn) = 1 ✓; (K/q) = (n/q) = (q/n) = −1 (Legendre/Jacobi reciprocity with n ≡ 1 (4),
q prime) ✓; (K′/q) = (2/q)^t (K/q) = −1 under (E) (so K′ > 1 automatically) ✓; H contains a non-residue ⇒ |H| even ⇒
−1 ∈ H (cyclic F_q^*) ✓; −K′ a residue of odd order o, h = (−K′)^{(o+1)/2} ∈ H with h² = −K′ ✓; d = 2^t ∏ s^{2a_s} ≡ −K ✓;
e ≤ max(a_s − b_s) ≤ (q − 2) − 1 ✓ (q = 3: e = 0). Mod-8 case split ✓ (n ≡ 1: q ≡ 3 (8) ⇒ v₂(n+q) = 2, t = 0;
n ≡ 5, q ≡ 3 (8) ⇒ t = v₂(n+q) − 2 ≥ 1).
*Def 1.1 compatibility of 2^t (the point the brief flags):* Def 1.1 constrains only primes of **den z**, not of the
Type II divisor d. With c₂ = t = b₂, Lemma 1.1 gives v₂(z) = b₂ + v₂(A) − c₂ ≥ b₂ ≥ 0, so 2 ∤ den z; the 2^t factor
is admissible. (It would not be if c₂ > 2t, which is exactly why the excluded case cannot use the non-residue 2.) ✓
*From scratch:* every non-square n ≡ 1 (4), 5 ≤ n ≤ 3000 (all prime factors allowed, incl. ≡ 3 (4)), every prime
q ≡ 3 (4), q < 300, q ∤ n, (q/n) = −1: 9 605 (n, q) pairs satisfy (E); for each, ALL square roots h of −K′ in ⟨S⟩
(own BFS) give d with (x, y, z) passing Def 1.1 with e ≤ q − 3; (K′/q) = −1 asserted. The 2 041 pairs failing (E) are
all n ≡ 5, q ≡ 3 (8), v₂(n+q) odd ✓.
Minor remarks: see defects D1 (the "excluded ⟹ not forced" wording).

### Prop 1.3 — SOUND
Existence of s: (K′/q) = ∏(s/q)^{b_s} = −1 ⇒ some odd s with b_s odd, (s/q) = −1 ✓. Non-residue in cyclic group of
order 2u (u odd) has v₂(o) = 1, s^{o/2} = −1 ✓. c_s = b + o/2 even (both odd) ✓; c₂ = t, other c = b ✓; cap
max(0, (o/2 − b)/2) ≤ ((q−1)/2 − 1)/2 = (q − 3)/4 ✓.
*From scratch:* for all 9 605 pairs above and EVERY eligible s, the triple from d = K·s^{o/2} has Def 1.1 cap exactly
max(0, (o/2 − b)/2) and 4e ≤ q − 3 (exact). The "e.g. s ≡ −1 (mod q)" special case (o = 2) ✓.
