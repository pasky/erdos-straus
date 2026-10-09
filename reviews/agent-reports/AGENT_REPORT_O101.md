# AGENT_REPORT O101 — novelty audit 2026-10c

Deliverable: `reviews/novelty-audit-2026-10c.md` (web + zbMATH + arXiv API; sources archived
in `sources/o101/`).

Headline findings (all verified in primary or zbMATH text):
1. **Correction needed (m/n note, (D)31):** Elsholtz, Trans. AMS 353 (2001), Remark 7.3,
   already gives an explicit-in-m constant `c_{m,3} = 3e^{−2/3}(8m)^{−1/3} − ε` in Vaughan's
   bound (for N > N_m, non-uniform). PW 2026 Thm 1.3 is the first *uniform* one. Thm A's
   comparison is unaffected (ratio `(Lm)^{1/12}`). No exponent > 2/3 for three unit fractions
   anywhere (Viola/Shen/Elsholtz line). No short-interval/progression exceptional-set result
   found (only Sander 1991/94, a progression *lower* bound for one family). Cor D answers the
   density half of PW's/Pomerance's (Mar 2026 talk) open transition question.
   PW is now Ramanujan J. 69 (2026) Paper 31.
2. **Coverings:** Yamamoto 1965 Table 1 lists, for primes 11 ≤ q ≤ 97, the level-q covered
   classes; the uncovered non-residues are 2, 6 (mod 11), 2, 7 (mod 13), 3, 5, 6, 7 (mod 17) —
   exactly x*'s residues and the r = 17 cells C₅, C₇. Terzi 1971 already had a 198-residue
   exception list mod 120120 (predates Salez for the r = 13 theorem). Nothing in the
   literature on non-square sterile points; Yamamoto (1965, p. 47) and Ionascu–Wilson (2011)
   lean the other way at integer level (no contradiction with our profinite statements).
3. **Pell/Lucas Type-I form:** nothing ES-specific found; apparently new; tools classical
   (TYPEI5 Lemma 1.1 is a routine LTE argument).

Concrete text edits are listed at the end of §§1.2 and 2.2 of the audit (not applied here —
they touch `paper/` and DISCOVERIES, left to the parent).
