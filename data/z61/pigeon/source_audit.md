# Analytic-source audit for Z61 PIGEON

The files were downloaded from the precise URLs below with `curl -fL`, then read
using `pdftotext -layout`. Burgess's Theorem 2 exponent was additionally inspected
on a rendered image of printed page 107 (PDF page 2); OCR/text extraction is
unreliable there. No newer or purportedly sharper exponent is required.

## Primary inputs

1. D. A. Burgess, *The distribution of quadratic residues and non-residues*,
   Mathematika 4 (1957), 106–112.
   URL: https://www.cs.umd.edu/users/gasarch/TOPICS/res/burgess.pdf
   DOI: https://doi.org/10.1112/S0025579300001157
   SHA256: `843d0f4fe7242509953ad33685364c171b6de061fce0e9e2d1fbcd39b173ca61`
   Read: Theorem 1 p.106; Theorem 2 p.107; its deduction in §5 p.112.
   Used: least quadratic nonresidue modulo a prime p is O(p^a), for each fixed
   a > 1/(4√e). The implied constant/large-p qualification cannot be discarded.
   Theorem 1 controls character sums in intervals of length > p^(1/4+δ);
   the Vinogradov deduction uses the initial interval and the least nonresidue.
   This is NOT a prime-in-progression result or a claim that an arbitrary
   shifted level ρ is prime.

2. T. Xylouris, *Über die Nullstellen der Dirichletschen L-Funktionen und die
   kleinste Primzahl in einer arithmetischen Progression*, Bonn dissertation,
   2011.
   URL: https://bib.math.uni-bonn.de/downloads/bms/BMS-404.pdf
   Institutional record: https://bonndoc.ulb.uni-bonn.de/xmlui/handle/20.500.11811/5074
   SHA256: `1f6a27ed3a4a70d2a19b0d6767d64373c66369e8a9948afb9ddbc2ae83400b9f`
   Read: P(Q)'s definition p.9; Linnik form (2.6) p.10; Theorem 2.1 p.12
   and adjacent discussion contrasting the preceding 5.18 result; distinctions
   from Theorem 2.2. Used: uniformly over reduced classes modulo Q, the least
   prime is at most C Q^5, with an effective absolute C. In PIGEON Q=4n_p,
   gcd(−p,Q)=1. No Siegel-zero exclusion or GRH assumption is needed.
   The 2011 Acta Arithmetica paper is not the correct exponent-5 citation.
   This audit verifies the source theorem and application, not a fresh
   reproduction of the dissertation's zero-density numerical calculations.

## Cross-checks

- K. J. McGown and E. Treviño, *The least quadratic non-residue*, author survey:
  https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf
  SHA256: `77ead38384d9519f99ca48e116df2fe34fea1bd967dac304abd6d9a92f007ac5`
  Read §2, Theorems 2.4/2.6, Remark 2.7, and the least-nonresidue deduction
  ending on p.6. Prime modulus satisfies the unrestricted-r Burgess hypotheses.
- Repo `sources/lit2026/lau-wu-least-quadratic-nonresidue.txt`, introduction
  equations (1.4)–(1.5): prime-modulus Burgess/Vinogradov exponent agrees.
  SHA256: `48a2bc4314ebc3ae92ff64af4afd332701bb1e5565241f19f88fac91ebb4c7e3`.

## Input/application boundary

Burgess gives n_p ≤ C_δ p^(α+δ); Linnik gives ρ_L ≤ C_L(4n_p)^L.
Take δ=ε/(2L), then absorb the fixed constant into p^(ε/2) only for sufficiently
large p. Require ε<1−Lα for the sublinear complete-witness-range conclusion.
The nonresidue transport is elementary reciprocity, not part of either analytic
input; the p≡5 (8), ℓ=2 case must use ρ≡3 (8), not 7 (8).

The PDFs remain retrieval artifacts rather than duplicated repository sources;
URLs, printed page numbers, hashes, and the precise mathematical inputs are
retained here for reproducibility.
