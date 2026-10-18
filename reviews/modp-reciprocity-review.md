# R275 — hostile review of O265 (MODP_RECIPROCITY.md)

Reviewer: side-agent/review-modp-recip. Author branch merged: side-agent/modp-reciprocity (head 95dbec07).
From-scratch scripts: `scripts/review_r275_*.py`, logs `logs/review_r275_*.txt`. Author's scripts were NOT reused.
**ES is not solved, here or anywhere.**

## Summary verdict per claim
(filled in progressively)

## Defects
(filled in progressively)

## Per-claim notes

### §1 — Prop 1.1, Prop 1.2 (script `scripts/review_r275_sec1.py`, log `logs/review_r275_sec1.txt`)
**Prop 1.1: SOUND.** Re-derived: (4cd − 1)g = p + 4d ⟺ 4d(cg − 1) = p + g; w ≡ 3 (4), p + 4d ≡ 1 (4) ⇒ g ≡ 3 (4), so
g ≥ 3 and 0 < g ≤ m + 1 < 4m, i.e. g is the least residue; converse: g_m ≡ −p ≡ 3 (4) so g_m ≠ 1 and w < p + 4d; for (iii),
m ≡ −1 (g) gives 4m ≥ 4g − 4 > g, so the fixed g is the least residue. From scratch, all three sets {(m, g, d)} (from (i) by
enumerating all d ≤ (p+3)/8 and all divisors of p + 4d; from (ii) over all m ≤ (p+1)/3; from (iii) over all g ≡ 3 (4))
coincide for all 609 primes p ≡ 1 (4) ≤ 10⁴ (5 902 certificates).

**Prop 1.2(a), (b) identities: SOUND.** Re-derived: (w/p) = (p/w) = (−d/w) = −1 (w ≡ −1 mod 4d and mod 8 when d even);
p ≡ −4d (g), −g (d′), −g (m′). The R-O265 example (5,2,3,1) vs (709,2,3,89) checked by hand. (b): wg ≡ 4d (p) and
4^{(p−1)/4} = 2^{(p−1)/2}. All five symbol identities and the quartic identity: 0 failures on the 5 902 certificates above.

**Prop 1.2(b) "function of (a, b)" / Burde: SOUND (the statement); the q ≡ 3 (4) explanation is slightly wrong (MINOR D1).**
Sign bookkeeping written out (the author delegated it to numerics). The reduction i ↦ i_p = a/b is reduction modulo
λ := a − bi (not π = a + bi: a + bi ≡ 0 gives i ≡ −a/b). With a odd, b even, λ is primary up to ±1, and [−1/q]_4 = 1 for
q ≡ 3 (4), so no unit ambiguity enters [λ/q]_4. Biquadratic reciprocity with the primary −q ((q² − 1)/4 even) gives
  (q/p)_4 ↔ [q/λ]_4 = [−1/λ]_4 · [λ/q]_4 = (−1)^{(p−1)/4} · ((a + bi)/(a − bi))^{(q+1)/4}  (computed in F_q[i]),
a value in {±1, ±i}, read with i ↦ a/b. Verified from scratch: 0 failures for q ∈ {3, 7, 11, 19, 23, 31, 43} on all 12 980
primes p ≡ 1 (4) < 3·10⁵. Consequences: for q ≡ 3 (4) the symbol is a function of ((a : b) ∈ P¹(F_q), p mod 8) — only b mod 4
of 2-adic data, 0 conflicts; without p mod 8 ≈ 50 % conflicts (6 466/12 980 for q = 3), reproducing the author's observation.
For q ≡ 1 (4) the symbol is a function of (a mod q, b mod q) alone (both [λ/μ]-factors of q = μμ̄ carry the same sign
supplement, which squares away): 0 conflicts for q ∈ {5, 13, 17, 29, 37}. For q = 2: a function of (a, b) mod 8 (0 conflicts).
Burde's law (p/q)_4(q/p)_4 = ((ac − bd)/q), (p/q) = 1: 0 failures on 11 615 pairs (q < 200, p < 2·10⁴) — Burde's statement as
used matches the standard form (Lemmermeyer, *Reciprocity Laws*, Ch. 5); I could not access Burde's 1969 paper itself
(not in sources/), the citation J. reine angew. Math. 235 (1969) 175–184 matches the standard bibliographic record.

**Prop 1.2(c) and "Answer to goal (1)": SOUND as Assessment** (correctly labelled; it is a framing statement).
