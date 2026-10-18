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

### §2 — Prop 2.1, Prop 2.2, EVIDENCE 2.3 (scripts `review_r275_quartic.py`, `review_r275_bit_*.py`; logs `logs/review_r275_quartic.txt`, `logs/review_r275_bit.txt`)
**Prop 2.1: SOUND (and nearly tautological).** For a finite S with all w < p + 4d (automatic: w = p + 4d would need
p ≡ −1 (4)), the event is a function of p mod lcm(w). The density |C|/[Ω : I]: an abelian quotient sees a conjugacy class as
one element, so all of C restricts to the same element of Gal(I/ℚ); the fibre-product count then gives relative density
|C|/[Ω : I] in each compatible class r. Re-derived; correct. The R-O265 scope remark (fixed d, unbounded w not covered) is right.

**Prop 2.2 (proof): SOUND; its "Reading" and the verdict built on it: overclaim (MAJOR D3).** Proof re-derived: ψ = χχ̄′
is trivial on all primes ≡ 3 (4) not dividing pp′, these generate (ℤ/4pp′)^× (Dirichlet: every class ≡ 3 (4) contains one;
products of two cover the classes ≡ 1 (4)), equal characters have equal conductors, and an order-4 character differs from its
conjugate. Notational slip (MINOR D2): with i_p = a/b the character is that of λ = a − bi, not of π = a + bi (see §1 note);
harmless after renaming. The overclaim: "no independence barrier can be proved at unbounded level" (§0 v1, §2 Reading, §6
Goal (2), AGENT_REPORT sharp item 2) does not follow. Prop 2.2 excludes only *exact/pointwise* independence (a complete
invariant cannot be independent of anything); it says nothing against *statistical* independence statements with growing
parameters (joint equidistribution of (q/p)_4, q ≤ Q, with the level-d events), which are the kind of barrier one would
actually use — the Legendre symbols also determine p, yet are asymptotically independent of everything congruence-shaped.
The author's own EVIDENCE 2.3 is exactly such a statistical independence at unbounded witness size.
Repair: replace by "no *pointwise* independence statement holds at unbounded level; statistical independence is open
(EVIDENCE 2.3 supports it at fixed level)".

**EVIDENCE 2.3, part (A) (hit rates vs quartic data): SOUND (reproduced).** From-scratch Cochran–Mantel–Haenszel test
(hypergeometric variance) on all 39 175 primes p ≡ 1 (4) ≤ 10⁶, d ≤ 40, q ∈ {2, 3, 5, 7, 11, 13} on (q/p) = 1, strata
p mod lcm(4d, 16, q): 240 tests, max |z| = 2.60, 9 tests (3.8 %) with |z| > 2, none > 3; square levels max |z| = 1.82.
Consistent with the author (max 2.46, 2.5 %, none > 3, at 2·10⁶).

**EVIDENCE 2.3, part (B) (the "free, balanced quartic bit"): GAP — scope misreported, and the bit is NOT free (MAJOR D4).**
(i) The author's count (`z35_quartic_independence.py`, line 18: `W=b1_witnesses(p,D,…)`) is over witnesses with **d ≤ 40
only**; the document (§2, §6 Goal (1), AGENT_REPORT) says "b = 1 witnesses" without restriction. Over ALL witnesses of all
4 511 primes p ≡ 5 (8) ≤ 2·10⁵ (87 433 witnesses) I get +1: 51.79 %, −1: 48.21 % (naive z = 10.6); restricted to d ≤ 40,
50.11 % (reproduces the author).
(ii) Structural reason, missed by the author: from 4md = p + g and m + 1 = cg one gets the exact identity
  **w·m = c·p + 1**, hence w ≡ m⁻¹ (mod p) and (2w/p)_4 = ((2/m)/p)_4 = (2/p)_4·(m/p)_4⁻¹
(verified as an assertion on all 87 433 witnesses). So the "free bit" is the quartic symbol of the WINDOW m, and at windows
m = 2k² it collapses to the LEGENDRE symbol (k/p) — a congruence datum: m = 2 fires for every p ≡ 5 (8) (g = 3) and always
has bit +1 (4 511/4 511); m = 8 always −1 (1 144/1 144; (2/p) = −1); m = 18 always −1 (760/760; fires only for
p ≡ 53 (72), (3/p) = −1); m = 32 always +1 (575/575); m = 98 32.8 % (fires on three classes mod 392 with (7/p) = +1, −1, −1).
Generic windows (d ≤ 40, or 40 < d and m > 100) are balanced (50.1 %, 49.8 %).
Consequence: "the certificate carries a free, balanced quartic bit" and AGENT_REPORT spark 1 ("β is not forced") are false
as stated; the correct statement is "β(w) = ((2/m)/p)_4; it is forced (abelian) on the windows m = 2k², balanced on generic
windows". Nothing positive in the file rests on it, so not FATAL; but Prop 1.2(b) should also record w ≡ m⁻¹ (mod p) (it
makes the quartic parts of w and m mutually determined: (w/p)_4(m/p)_4 = 1).
