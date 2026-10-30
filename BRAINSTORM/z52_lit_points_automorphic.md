# L4 — Integral and rational points; automorphic forms

## §0 Summary
- **New since 2026-09-28:** pending source verification.
- **Transferable structural features:** pending.
- **Campaign verdict changes:** pending.

## §1 Verified entries

### Bright–Loughran: the ES surfaces and their integral Brauer–Manin obstruction

Martin Bright and Daniel Loughran, “Brauer-Manin obstruction for Erdős–Straus surfaces,” arXiv:1908.02526v2 (last revised 12 May 2020); *Bulletin of the London Mathematical Society* 52 (2020), no. 4, 746–761, DOI 10.1112/blms.12374. Source: arXiv HTML v2, accessed 2026-10-30; excerpt: `sources/z52/points_automorphic/bright-loughran.txt`.

- **Verified statements.** Theorem 1.8: for every integer `n ≥ 2`, the Brauer–Manin set of the positive-real/integral-adic set is nonempty (hence no BM obstruction to the integral Hasse principle for this formulation). Theorem 1.9: the rational points do not have dense image in the BM set, so BM is not the only obstruction to strong approximation. Lemma 3.10 proves finiteness of integral points off the displayed exceptional lines, and in particular finiteness of positive integral points for each fixed `n`. These are results about individual fixed surfaces, not a uniform theorem solving ES for every `n`.
- **Status:** Published; the statements above were checked against the paper’s HTML. Note the explicit `n ≥ 2` range in the paper’s introduction; do not extend it to `n=1`.
- **Relation:** Already covered in `GEOMETRY_ES.md` §§1, 3, 6 and `LITERATURE_AUTOMORPHIC.md` §2; it does not change the campaign verdict.

### Linowitz–Thompson: signs of Eisenstein-newform Hecke eigenvalues

Benjamin Linowitz and Lola Thompson, “The sign changes of Fourier coefficients of Eisenstein series,” arXiv:1305.6356v1, submitted 28 May 2013. Source: arXiv abstract, accessed 2026-10-30; excerpt: `sources/z52/points_automorphic/linowitz-thompson.txt`.

- **Verified statement.** The abstract says they prove individual and statistical results on how signs of Hecke eigenvalues of an Eisenstein newform determine the newform; in particular, signs on any prime set of density greater than `1/2` determine it. This is a uniqueness/sign-pattern theorem, not positivity of each individual Fourier coefficient. No claim about an arbitrary growing-level Eisenstein combination is made here.
- **Status:** arXiv preprint; publication metadata not independently checked in this lane. Abstract accessed; theorem text not accessed.
- **Relation:** `LITERATURE_AUTOMORPHIC.md`, `METAPLECTIC_ES.md`; no new pointwise positivity input or campaign verdict change.

## §2 Structural-feature table

| Problem | Solvable structural feature | Does ES share it? | Transfer verdict |
|---|---|---|---|
| Bright–Loughran: Brauer groups/local obstructions on each `U_n` | Explicit surface geometry and a computable transcendental Brauer class; local invariants constrain solutions and identify BM behavior. | **Partial:** ES shares the exact surface and class, but Thm 1.8 only establishes BM-set nonemptiness; B2 still asks for an actual integral point. `GEOMETRY_ES.md` §1. | **Known-dead as a standalone proof route** (`GEOMETRY_ES.md` §§1,6; `BM_CORRECTED_COUNT.md`): BM alone does not give integral points; strong approximation fails by Thm 1.9. |
| Linowitz–Thompson: identify Eisenstein newform from signs | Multiplicativity/Hecke structure turns signs across a positive-density set of primes into a uniqueness fingerprint. | **No:** ES needs positivity/existence at one prescribed prime and only polylogarithmically many candidate events; it has no supplied positive-density prime set. B6 and B2. | **None:** theorem is sign-pattern uniqueness, not positivity of individual coefficients or a lower bound for an ES coefficient; `METAPLECTIC_ES.md` already treats ES’s Eisenstein-only normal form. |

## §3 New candidates

None. The source-verified results either restate audited ES geometry or concern sign patterns across a positive-density set of primes. Neither supplies the required single-object lower bound for a prescribed prime with expected count `≍ log² p`; proposing a transfer would evade B2/B6 rather than address them.

## §4 Not accessed / could not verify / incorrect leads

- No 2021–26 follow-up proving a new pointwise or density result on the Erdős–Straus surfaces was verified in this lane. The initial search surfaced no such result; this is not an exhaustive database search. The already-audited Bright–Loughran and geometry citations remain in `GEOMETRY_ES.md` and `LITERATURE_AUTOMORPHIC.md`.
- The named leads (Harpaz, Santens, Wilsch, Mitankin, Lyczak, Gvirtz-Chen, Cao–Xu/Wei, Colliot-Thélène–Wittenberg) were not individually re-opened here; rely on existing repo audits, not this note, for their exact statements.
- No 2024–26 theta-lift, Kudla–Millson, mock-modular, Borcherds, Bruinier–Funke, or half-integral-weight result certifying positivity of a single coefficient in a growing-level Eisenstein-type combination was source-verified. The leads in that clause remain **NOT VERIFIED**; no claim of nonexistence.
- Linowitz–Thompson: arXiv abstract accessed but full theorem text and publication metadata not checked; accordingly only the abstract-level statement is recorded.

