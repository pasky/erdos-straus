# Referee report R33: `paper/es-subexp-note.tex` (branch side-agent/omega-paper-v4)

Referee: hostile side agent `side-agent/referee-subexp`. Merged author branch at
`ae9204b` (normal merge, since ff-only was impossible: main had moved).

Status: IN PROGRESS (written incrementally).

## Per-claim verdicts

| Item | Verdict | Notes |
|---|---|---|
| Lemma 2.1 (atoms) | SOUND | re-derived: u_q=max(0,d−a), w_q=d−2u_q, v_q=a−u_q−w_q ≥ 0 checked; brute force below |
| Lemma 2.2 (class of one) | SOUND | re-derived |
| Lemma 2.3 (mass bound) | SOUND | re-derived every step; g-symmetry and inner-sum bound brute-forced (`scripts/review_r33_atoms.py`, ratio ≤ 0.65); ET Prop 1.4 checked in source (see minor point 1) |
| Lemma 2.4 (iterated quarantine) | SOUND | #prime factors > z of M ≤ T is ≤ ⌊Λ/log z⌋ = k; pairs → atoms injection |
| Def 2.5 / Lemma 2.6 (pairs + lifts) | SOUND | change #1 vs OMEGA8 checked: lifts of a pair partition its class, so w_ell = w_ell(Pi) exactly; duplicates counted on both sides; m <= T^{k+2} |
| Thm 3.1 (TZ Cor 1.4 + Rem 1.5) | SOUND (minor 2) | checked against arXiv txt lines 37, 121–131 |
| Lemma 3.2 (severe) / Thm 4.1 (transfer) | SOUND | verbatim from refereed v3; re-read, no change found |
| Rem 4.2 (Page-type alternative) | SOUND as Assessment | K and log Z are indeed both \asymp\Lambda^7 (via t\Lambda); Page error is absolute, so need log Z \le c'\sqrt{\log x} and K \le (c-c')\sqrt{\log x}: log x \gg \Lambda^{14}. Agree. |
| Lemma 5.1 (LLL+conditioning) | SOUND | |
| Cor 5.2 | SOUND | 1−x \ge e^{−1.1x} on [0,1/32]; e^{1.1/32}=1.035 |
| Lemma 5.3 (BRW) | SOUND | identity re-derived; uses only A_i\in\{0,1\}, hence valid at non-unit integers too |
| Lemma 5.4 (size, change #2) | SOUND | 1+m+2m^2+m^3 \le 5m^3, log 5<2 |
| Lemma 5.5 (twist, change #4) | SOUND | 0.01+0.02/0.98=0.0304; 0.0304/0.99<1/4 |
| Thm 6.1 (Håstad as in O'Donnell) | SOUND | matches O'Donnell's (5\delta w)^k form (from memory of the book; book not archived) |
| Lemma 6.2 (tail, change #3) | SOUND | density ratio \prod(1-q_\ell 2^{-b})^{-1}, q 2^{-b}\le 1/(4N); (1-1/(4n))^{-n} decreasing from 4/3 |
| Cor 6.3 / Thm 7.1 (assembly) | SOUND | all constants re-derived |
| Thm 1.1 / Thm 1.2 | SOUND-AFTER-REPAIRS (labels only) | exponent arithmetic re-derived: t \ll \Lambda^6, K, log Z \ll \Lambda^7 |

## Numbered defects

1. MINOR (Lemma 2.3(b) proof, and intro). ET Prop 1.4 as stated in the source
   (arXiv 1107.1010, p. 6) is `Σ_{a≤A}Σ_{b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)`
   for A,B>1 and k ≪ (AB)^{O(1)}. The paper's use (k=4, so log(1+k)=log 5
   is absorbed) is correct, but the paper never states the result. Repair:
   quote the statement, including the `log(1+k)` factor, in a cited-result
   box like Theorem 3.1, so that “proved modulo [ET, Prop 1.4]” refers to
   something visible. Also: the paper's own k (the event-support size) clashes
   with ET's k; rename one of them in the proof.

(further points below)
2. MINOR (Thm 3.1, last sentence "also 0<λ<2"). This is not in TZ; it is an
   easy consequence (β_1 ≥ 1−1/(13 log 3q) > 1/2 and log x ≥ 12 log 2 > 1/β_1
   give x^{β_1−1}/β_1 < 1). Repair: move it out of the cited box with that
   one-line proof (Case A of Thm 4.1 already contains the argument).

3. MINOR (status labels). Thm 1.1 is labelled "modulo TZ and [ET]" and
   Thm 1.2 "modulo TZ", but both go through Thm 7.1, which is labelled
   "modulo TZ and Thm 6.1 (Håstad)". Thm 6.1 is a textbook theorem, so
   this is harmless, but the labels should agree with §8: either add
   Håstad to the headers of Thms 1.1/1.2, or declare once (in the status
   conventions) that textbook results cited in full (LLL, Håstad,
   Efron–Stein, Kaas–Buhrman) are not listed in labels.

4. MINOR (Remark 7.2). "cf. [Paper1], where log(1/δ*(T)) ≪ Λ^7/logΛ is
   proved": in Paper1 (es-omega-note.tex l. 211) this bound is stated
   *modulo [ET, Prop 1.4]*. Repair: say "proved modulo [ET, Prop 1.4]".

5. MINOR (novelty paragraph, §1 "Relation to the literature"). Two
   relatives are missing.
   (i) Filaseta–Ford–Konyagin–Pomerance–Yu, *Sieving by large integers and
   covering systems of congruences*, J. Amer. Math. Soc. 20 (2007),
   495–517. To my recollection (not archived, could not check) they already
   use the Lovász local lemma to lower-bound the uncovered density of a
   congruence system. This is closer to the Haar side (Cor 5.2) than
   Hough/BBMST. Cite it next to them.
   (ii) Even–Goldreich–Luby–Nisan–Velicković ("k-wise independence fools
   combinatorial rectangles / AND", via Bonferroni). The novelty audit
   (l. 45) names it, but the paper does not. It is the bridge between
   [Paper1]'s truncated inclusion–exclusion and the present bounded-
   independence sandwich, so one sentence citing it makes the "sieve ↔
   bounded independence" dictionary honest. Neither changes the novelty
   claim, which is already suitably hedged ("no priority claim").

6. MINOR (bibliography; the four TODO(verify) items). From my own
   knowledge (no library access in this pass either) the details given for
   Green (CPC 21 (2012) 942–951), Bourgain (Israel J. Math. 197 (2013)
   215–235), Hough (Ann. of Math. 181 (2015) 361–382) and BBMST (Invent.
   Math. 228 (2022) 377–414) match what I remember. I would rate them
   *probably correct, unverified*. Keep the TODO until someone checks them
   against MathSciNet/DOI. I also could NOT verify the TZ journal data
   (Math. Z. 306 (2024), Paper 54). Only the arXiv version is archived,
   and the paper correctly says it used that. Confirmed against archived
   sources: TZ Cor 1.4 / Rem 1.5 and the McCurley citation (TZ ref. [10],
   JNT 19 (1984) 7–32); ET Prop 1.4. Consistent with my memory: Bazzi
   (SICOMP 38 (2009) 2220–2272), Razborov (ToCT 1 (2009) Art. 3), Braverman
   (J. ACM 57(5) (2010) Art. 28), LMN (J. ACM 40 (1993) 607–620), Håstad
   (STOC '86, 6–20), Kaas–Buhrman (Stat. Neerl. 34 (1980) 13–18),
   Efron–Stein, Hoeffding, HSS (J. ACM 58(6) Art. 28), O'Donnell §4.4
   (switching lemma, (5δw)^k form) and §8.3 (orthogonal decomposition),
   HW Thm 317, AS Lemma 5.1.1.

7. MINOR (typesetting). The author's report says "no warnings", but
   pdflatex (2 passes, my run) reports 8 over-full hboxes, the worst being
   86.6pt at l. 624 (the expanded B display in Lemma 5.4), 44pt at l. 544
   (Lemma 5.1 display), 28pt at l. 805 (Thm 7.1 display) and 20pt at
   l. 675 (Lemma 5.5 display). Break those displays (multline/split).
   There are no undefined references or citations, and the build gives
   16 pages.

8. MINOR (wording). (i) Abstract: "equivalently, the least hard prime with
   W(p)>T is at most exp(O((log T)^14))". This is a strengthening (it
   implies the Ω-statement), not an equivalence. Say "more precisely".
   (ii) Notation paragraph: "log_2 denotes the binary logarithm only where
   explicitly said" is confusing. log_2 is used only as the binary
   logarithm (l. 152, 772–796), so just say so. (iii) The paragraph after
   Thm 7.1 ("Distinctness of the events plays no role …") sits oddly next
   to Def 2.5, which was rewritten precisely to make w_ℓ = w_ℓ(Π) exact.
   Say once, in Def 2.5, that the pair-then-lift construction is what
   makes Lemma 2.6(iii) an equality, and that duplicate lifts are counted
   in w_ℓ on both sides.
   (iv) Lemma 6.2(b): p = 1/(10w) needs w ≥ 1. This is automatic here
   (every |G_ℓ| = φ(ℓ^e) ≥ 2), but the abstract Setting allows |G_ℓ| = 1;
   add "w ≥ 1" or "|G_ℓ| ≥ 2".
