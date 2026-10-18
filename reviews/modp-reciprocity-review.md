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

### §3 — 3.1 (citations), Lemma 3.2, Prop 3.3, EVIDENCE 3.4 (script `review_r275_windows.py`, log `logs/review_r275_windows.txt`)
**3.1 "polynomial (a, b)-menus are already closed": SOUND for full ET families; one sentence overstates the scope (MAJOR D5).**
Checked against the files: POINTWISE_BINARYFORM Thm 3.2 ((J)3) — polynomial Type I/II family for Q, M ⊇ 8, 2D, K_F: (a) never
valid where Q(P) is an odd square, (b)/(c) valid points of a square class lie near finitely many directions; Lemma 3.3 +
Cor 3.4 handle rational families up to density zero. SYNTHESIS_SPARKS7 Thm 1.1 / NORMFORM_CUBIC Thm 1.1′ ((J)78): polynomial
Type II family valid at ONE point ⇒ A, B, C, D ∈ ℚ[P]. NORMFORM_CUBIC Cor 3.2 ((J)79): every polynomial ET family (I or II)
valid at one point is an identity in n = N(x), for every irreducible binary form; u² + v² is ℚ-irreducible, so all three
apply verbatim in the variables (a, b). Hence "every polynomial ET family in (a, b) is an identity in p or nowhere valid" is
correct, and the brief's premise was indeed wrong for full families.
Overstatement: the list "(levels d, windows m, side numbers p + 4b², p + 4ab, … chosen polynomially)" suggests that choosing
only the LEVEL (or only a side number) polynomially is covered. It is not: these theorems need ALL ET coordinates
polynomial (or rational). A menu "d = F(a, b), then any divisor w ≡ −1 (mod 4d) of p + 4d" has a non-polynomial witness and
is a B2 divisor event — which is exactly why the author then tests such levels numerically in EVIDENCE 3.4. (On the b = 1
line: m and d both polynomial ⇒ g = 4md − p polynomial and c = (m + 1)/g rational, so that case IS covered via Lemma 3.3.)
Repair: "every family in which the full certificate (d, w) — equivalently (m, d) — is polynomial/rational in (a, b) is an
identity in p or invalid (density zero for rational); a polynomial level or window with a free divisor is not covered and
is the non-polynomial residue studied below".

**Lemma 3.2: SOUND; hypotheses stronger than needed (MINOR D6).** Re-derived line by line (the reciprocity step
(g/m′)(m′/g) = (−1/m′) uses g ≡ 3 (4); m′ = 1 is fine with (·/1) = 1). The proof uses only the JACOBI value (p/m′) = +1, not
that p is a square mod m′, and for s ≥ 1 only p ≡ 1 (8) (an odd number is a square mod 2^{s+2}, s ≥ 1, iff it is ≡ 1 mod 8);
for s even ≥ 2 no 2-adic condition is needed at all ((2/g)^s = 1 already contradicts). Strengthened form: *if (p/m′) = +1
and (v₂(m) even or p ≡ 1 (8)), the window m is sterile.* From scratch: 199 208 pairs (p ≤ 2·10⁴, m ≤ 400) satisfying it,
0 firings; on the complement (s odd, p ≡ 5 (8), (p/m′) = 1) 2 294/41 874 fire, so the 2-adic clause is needed. This is just
the T1 obstruction read on one window; the label "local form of T1" is accurate. Gaussian supply re-derived (CRT is not
needed for a single u — the two conditions enter the proof separately) and checked on all p ≡ 1 (4) < 10⁶: all odd m | ab
(472 770 trials), all even m | ab with 2^{s+2} | b² (596 174), m = ab/2 (39 175): 0 firings.

**Prop 3.3: SOUND as stated (whole class only).** ET Prop 1.6 is pointwise (odd squares have no Type I/II point at all;
confirmed in BRAINSTORM/corr_joint_factorisation.md's check of the ET PDF, p. 6), so one square point in V(C) suffices.
Construction re-derived: s ≡ 1 (4M) prime, X² ≡ −1 (s²), X ≡ X₀ (M); N = (X² + 1)/s² ≡ N₀ s⁻² ≡ N₀ (M). MINOR D7: the gloss
"(the class n ≡ 1 (mod M))" needs gcd(N₀, M) = 1 (from X² + 1 = nN one gets N₀(n − 1) ≡ 0 (M) only); the proof does not use
it. The scope caveat (sectors / least lifts not covered) is correctly stated; the result is weak but honestly labelled.

**EVIDENCE 3.4: plausible; partially re-checked.** Re-checked the two sterile windows (m = a, m = ab/2: 0 firings, 10⁶); the
neighbour-control z-values were not recomputed (author already flags them as indicative). The explanation of the enhanced
windows m = b, |a − b| (square-class confinement of −p mod m′) is consistent with Prop 5.1(ii).

### §5 — Prop 5.1, Cor 5.2 (same script/log)
**Prop 5.1 (i), (ii)-first-half: SOUND.** Re-proved: (i) εp ≡ x² (m), x a unit (gcd(x, y) = 1), ε ∈ {1, 4} a square ⇒ Lemma 3.2
(odd m). (ii) εp ≡ Dy² (m), D and y units mod m (gcd(x, Dy) = 1), −g ≡ p (m) ⇒ (−g/m) = (D/m); a firing odd window forces
(−g/m) = −1. Exhaustive from-scratch check over ALL odd divisors (the author tested only m = odd part of y and m = x) for all
78 350 primes p ≡ 1 (4) < 10⁶ (Cornacchia representations, asserted x² + Dy² = p, gcd(x, Dy) = 1):
  odd m | y: 0 firings in 128 358 / 68 888 / 60 912 / 53 453 trials (D = 1, 2, 3, 7); 47 040 (4p = L² + 27M², L, M odd) and
  16 759 (p = L′² + 27M′², the L, M even case);
  odd m | x, m > 1, (D/m) = +1: 0 firings in 114 685 / 29 504 / 17 938 / 24 043 / 13 503 / 5 948 trials;
  odd m | x, (D/m) = −1: 7.5 % / 9.6 % / 11.3 % / 8.8 % / 9.8 % fire (D = 2, 3, 7, 27-in-4p, 27) — over all divisors,
  small windows dominate, hence higher rates than the author's m = x figures.
The 4·109 = 2² + 27·4² (m = 2 fires) and 5 | x, y ≡ ±2 (5), D = 3 (−p ≡ 3 mod 20) examples re-checked by hand.
MINOR D8: (a) the clause "which roughly doubles the firing probability" is a heuristic inside a PROVED statement — move it
to the Check paragraph as EVIDENCE; (b) AGENT_REPORT sharp item 1 and the brief say "sterile **iff** (D/m) = +1" — only "if"
is proved (and true): (D/m) = −1 windows fire only sometimes (the Prop text itself is correct); (c) §6 Goal (3) "checked
exhaustively to 10⁶" — the author's check covers only m = odd part of y and m = x; my all-divisor check above now supports
the exhaustive wording. (d) for the D = 27 case with L, M both even, gcd(L, 27M) = 1 fails for (L, M) itself — the Prop's
hypothesis applies to (L/2, M/2) with ε = 1 (Cor 5.2 says this; Prop 5.1's "e.g. … 27" should too).

**Cor 5.2: PROVED part SOUND; the first sentence is not provable and should be Assessment (MINOR D9).** "The representations
p = x² + Dy² … are the only canonical integers of size ≍ √p attached to p" has no precise meaning and is labelled under
"PROVED + Assessment" without separation; the ticket count p^{−1/2+o(1)} for balanced tickets is a heuristic (≈ τ(m + 1)/m
per window is a residue-lottery model, not proved). Repair: label those two sentences Assessment.

### §4 — Prop 4.1, EVIDENCE 4.2 (script `review_r275_sq.py`, log `logs/review_r275_sq.txt`)
**Prop 4.1: SOUND.** Re-derived: (a) p ≡ −4k² (ℓ) ⇒ (p/ℓ) = (−1/ℓ), and (ℓ/p) = (p/ℓ). (b) −4 = (1 + i)⁴ is a fourth power
mod ℓ ≡ 1 (4), so (p/ℓ)_4 = (k²/ℓ)_4 = (k/ℓ); then Burde (checked in §1, 0 failures). From scratch: 26 397 triples
(p ≤ 2·10⁴, k ≤ 11, ℓ | p + 4k², ℓ ∤ 2k), 0 violations of (a) or (b). The "What it forces" paragraph is Assessment-level
reasoning (in particular "the target class −1 mod k² beyond its quadratic shadow lies in G²" is imprecise: −1 ∉ G² for
G = (ℤ/4k²)^×; what is meant is that the fibre of the class over its image in G/G² is invisible) — MINOR D10: label it
Assessment and fix the G² sentence. Note also (my §2 identity) (w/p)_4 = (m/p)_4⁻¹, another expression that does not give a
p-only constraint either (m is unknown), consistent with the author's conclusion.

**EVIDENCE 4.2: SOUND (reproduced, mechanism supported).** From scratch on the 3 591 primes p ≡ 1 (4) in [9·10⁵, 10⁶],
levels 100 ≤ d ≤ 400: hit rate 1.215 % at squares, 1.052 % at non-squares with (d/p) = −1, 0.985 % with (d/p) = +1 (same
ordering as the author's 1.07 / 0.91 / 0.85 % over p < 10⁶; rates grow slowly with p, as Σ_c 1/φ(4cd − 1) ∝ log(p/4d)/d).
Observed ratio squares / non-squares 1.19 (author 1.22); naive prediction Σ_{w ≤ p} 1/φ(w) ratio 1.17 (author 1.19). The
c = 1 witness w = 4k² − 1 = (2k − 1)(2k + 1) alone: 1/φ ratio 1.46, and the event "4d − 1 | p + 4d" occurs 0.235 % (squares)
vs 0.145 % (non-squares) — the witness factorisation is indeed the driver. The author's admitted spurious factor 2 in
z35_sg_predict.py does not affect ratios (my script has none). Labels (EVIDENCE, "B1-level") appropriate.
