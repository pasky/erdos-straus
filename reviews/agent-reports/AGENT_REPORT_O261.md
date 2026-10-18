# AGENT REPORT O261 — B2 across fields (wide net)

Branch `side-agent/b2-across-fields`. Main file `B2_ACROSS_FIELDS.md`; 13 field memos `BRAINSTORM/z31_*.md`; excerpts
`sources/lit2026g/` (≈ 35 tiny text files, ≈ 130 KB total); scripts `scripts/o261/` (2 small checks). **ES is not solved.**

## Answer
B2 is **not** equivalent to, or an instance of, any *solved* problem among the 13 fields surveyed. It is
* an INSTANCE of the integral Hasse principle (with positivity) on a log K3 family (BL's framing). Its closest open sister is
  x³ + y³ + z³ = k (CTW: no BM obstruction; Heath-Brown: ~ρ log B solutions; both verified in the sources).
* given exact reformulations on the named sub-lines, none of which is equivalent to ES itself:
  * E2 is a cyclic, non-increasing divisibility system, so Lipshitz's local-to-global principle does not apply. It fails
    at 193, 2521 and 66529 even though it is ℓ-adically solvable for every ℓ (Lemma 7.1, PROVED).
  * The cap-0 window event is a target problem {−1, −p} for a box product set.
  * A single E2 slice is a "divisors in residue classes" decision problem (Lenstra).
  * The shot family E4 asks for an ideal divisor of (1 + 2k√−p) with norm ≡ −1 (mod 4k) (Lemma 4.1, PROVED, numerically
    checked).

## The one genuinely new literature fact (SHARP as information, not as a route)
**Zaremba's conjecture is claimed to be proved pointwise in 2026 preprints.**
* Shkredov, arXiv:2603.14116, Cor 1: every prime or squarefree q.
* X. Zhang, arXiv:2605.02518, Thm 1.2: every q, with a large absolute M.
* Mechanism: growth in SL₂(ℤ/qℤ) applied to Cantor-type sets in ℤ/qℤ.
* I read the statements, but not the proofs, which are unrefereed.

This was the brief's top priority. It is the first pointwise result in the thin-orbit family, and the campaign memos
`BRAINSTORM/thin_group_orbits.md` §4 and `farey_ford_cf.md` say "every thin-orbit local–global theorem is density one". That
is outdated if the preprints stand; I did not edit those files and leave the update to the parent.

Transfer to ES: in CF coordinates, ES-five is also a fixed-modulus problem. It asks for a QNR A mod p with HJ-length(p/A) ≤ 3
(DEDEKIND_ES Cor 4.6). However, its certificate count is only ≍ log² p on average, and there is no alphabet knob that would
make it a power. A growth/equidistribution gluing needs a power-size expected count. This is an Assessment, not a proved
obstruction.

## Pattern (Assessment)
Every pointwise existence theorem I surveyed uses at least one of four inputs:
* M1: a power-size main term;
* M2: a fixed-modulus character or group event;
* M3: homogeneity or a group action on the solutions;
* M4: freedom to choose the objects.

B2 lacks all four (features F1–F3). Zaremba 2026 is the sharpest test: it uses M1 + M2, and the ES-five analogue keeps M2 but
has no M1.

## Verification
* Read in the sources by me: BK Thm 1.8 / (1.37); Shkredov Cor 1, Thms 8, 12, Lemma 13; Zhang Thm 1.2, Remark 1.4;
  Moshchevitin–Shkredov abstract; Chen Thms 1.2.3, 1.2.5, 1.2.6; CTW abstract; the Heath-Brown conjecture; Lipshitz's LGP (via
  DHMP); Bloom abstract; BL Thms 1.8, 1.9.
* Each remaining research-agent claim is graded in §6: verbatim-by-agent, abstract-only, or NOT verified (the long flagged
  list includes Duke–Schulze-Pillot, Ono–Soundararajan, the ACFKP value, Erdős–Rényi, AGP and the least-witness bounds).
* "Conway–Guy" from the brief: not identified, and no claim is made.

## Review
I ran one self-requested hostile review (reviewer subagent). It found no FATAL issues. It raised nine MAJOR points, all
repaired and marked "R-O261 repair". The most important were:
* the dictionaries had been over-scoped to "B2/ES" when they cover sub-lines;
* the Zaremba size argument overreached;
* the Harpaz theorem was misdescribed;
* the claim that ES solution heights are O(p²) was false (counterexample z ~ p⁴/96);
* the three-cubes status was misstated;
* the QNR hardness statement conflated a solver with mere existence.

## Suggested parent actions
1. Record the Shkredov/Zhang 2026 preprints in LITERATURE_2026 and correct thin_group_orbits §4 / farey_ford_cf.
2. Optionally pursue the spark in §5: an ES relaxation with a Zaremba-type certificate set. This is a methodological test case
   only.
