# AGENT REPORT O223 — novelty audit of wave Y, DISCOVERIES (J)39–(J)55

Branch `side-agent/novelty-audit-d`. Main file: `reviews/novelty-audit-2026-10d.md`
(§§1–7 findings + verdict tables, §8 summary, §9 thirteen proposed ledger edits).
Archive: `sources/lit2026d/` (~2.5 MB: Morier-Genoud, Girstmair, Cohn–Heninger, Bernstein,
Hales, Kim–Oh, Schinzel 2013 PDFs + text extracts; Palamà 1959 and Huczynska text only).

## Main findings (all from sources opened in this pass unless marked)

1. **(J)42 Lemma 1.1 (mod-2 rigidity) is KNOWN**: Morier-Genoud, arXiv:1907.12790 §3.5
   p. 12 lists the five width-2 friezes over F₂ as the rotations of (1,1,1,0,0). I checked
   the dictionary to the campaign's even edge / opposite odd variable.
2. **(J)42 "χ is a function of (c, m, s) mod 4" is KNOWN in substance**: Girstmair
   (IJNT 7 (2011); stated explicitly in arXiv:1504.02618 §2) for regular CFs; (J)45 SHARP 2
   gets concrete citations (Girstmair; Eisenstein/Shallit/Bach–Shallit [snippets]); the
   signed Hilbert/Maslov form stays PARTIAL/apparently new.
3. **(J)51 Lemma 1.5 (FF Coppersmith threshold d(n − d)/n) is KNOWN**: Cohn–Heninger
   arXiv:1008.1284 Thm 1.2 (p. 3) gives exactly this threshold. Bernstein (2006) says the
   transfer to F_q(t) is easy. Lemma 1.4's per-degree constant 2 was not found
   (PARTIAL; Hales arXiv:2410.05030 has the 1/3 regime over ℤ[x]). (J)54 Cor 1.4 and
   FF_STERILE_SMALL Lemma 1.4 are KNOWN in substance.
4. **(J)55's citation check is done**: Schinzel 2000 (zbMATH review + abstract) and Schuh
   2024 (HAL abstract) cover **only linear denominators ax + b**. So (J)55 Thms 2.2/3.4 and
   Prop 4.1 look new; Thm 3.3 Rem (i) is their linear case. Bonus: Schinzel 2000's
   condition (1) covers every m ≡ 0 (mod 4). It should be cited at (J)49 SHARP 2.
5. **(J)49 Thm 3.1 (7/p for p ≢ 1 (105))**: folklore. PW §6 (p. 12) sieves m = 7 with the
   m-analogues of ET Prop 1.9, and MSE 3374919 has a level-14 identity. I found no
   printed statement. **(J)46's 7/p ≤ 10⁸ is superseded by PW Table 1** (no m = 7
   exception up to 10¹³).
6. **(J)48 Thm A/B**: KNOWN in substance (local–global + class number one of I₃). The ES
   specialisation is new. TWO_FIBRES already says so; the ledger line should too.
7. **(J)50 uniform-cyclotomy residue law (R216 "upgrade") is KNOWN**: it is the reduction
   mod h of Baumert–Mills–Ward 1982. I verified this from their formulas as restated in
   arXiv:2406.16805 Thm 1.2.
8. Nothing found for the square-numerator / exponent-cap variants ((J)41, (J)43, (J)47),
   ES_q sterility ((J)51, (J)54, FF_STERILE_SMALL), polygon-size uniqueness, or Mordell's
   840 as the "reach of one-slot χ-witnesses" ((J)46 Thm 4.2). These stay apparently new.

## Limits
- Not opened in full (bot walls): Schinzel 2000, Schuh 2024.
- Not opened at all: Girstmair 2011 full text, Bleicher 1972, Gauss DA, Mordell 1930,
  Ko 1937, Guy D11, Sierpiński 1956, Aigner 1964, Conway–Sloane 1992.
- Statements about these sources are secondary and tagged in the audit.
- (J)56 / FF_STERILE_SMALL was audited only for its Lemma 1.4 and for ES_q prior art.

## Requested from the parent
Review §9's ledger edits and apply them. No edits were made to DISCOVERIES.md or
LITERATURE_2026.md on this branch.
