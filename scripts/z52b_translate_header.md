# z52b lane `translate` — reformulations of ES translated into their native fields

**ES is OPEN.** Nothing here proves or disproves it. This is a breadth-first list of candidate connections, not a
graded slate: the only filter applied was "obviously false / meaningless / literal duplicate". Items are not checked
against the campaign barrier map (B1–B9) on purpose.

{SUMMARY}

## Method

1. Listed the repo's equivalent / sufficient / near-equivalent forms of ES (FRONTIER §§1–2, DEDEKIND_ES, FOREST_*,
   QUESTION_R, METAPLECTIC_ES, GEOMETRY_ES, FRIEZE_ES, WINDMILL, MARKOFF_ES, COMPOSITION_ES, LATTICE_MEETING,
   BALANCED_LATTICE, THREE_SQUARES, KUDLA_ES, QUATERNION_ES, LORENZINI_W, ZAREMBA_TRANSFER, POWER_LADDER_ES, Z52 pencil,
   I3/U(n)) and invented further translations. New ones written down here include: a 4-vertex fan multigraph with p
   spanning trees and a sandpile-pairing condition; effective resistance A/p; lens spaces / linear plumbings / 2-bridge
   links and their homotopy type; tridiagonal ternary lattices with a non-square discriminant form; triangle orbifolds
   of area 2π(1 − 4/n); triangles with integer exradii and inradius n/4; the Frobenius-class form uv | n + u + v (numerical
   semigroups, Popoviciu); totally split cubics T²(T − s) + e(T − n/4); frieze patterns with coefficients; dP5 log K3
   (Harpaz); −Γ₁(c) matrices with fixed upper-right entry p; TFNP search classes; Legendre-PRF distinguishers.
2. For each form × field where it is native, recorded the nearest PROVED theorem (or the nearest known object), what the
   field's toolbox would try first, and the cheapest test.
3. `seen:<file>` tags were added automatically by a fixed-string `git grep -il` on 1–3 specific keywords per item
   (first hit, non-review files preferred). They mean "the keyword occurs there", not "this exact item was done there".
4. Literature: arXiv ids in `refs` were checked against the arXiv API (`scripts/z52b_translate_arxiv.py`). Non-arXiv
   classics are cited by author/title/year from memory, and are named as facts only where they are standard.
   Anything less certain is phrased in `first_step` as "check whether …".

Item count: {N}. Items carrying a `seen:` tag: {NSEEN}.
Data: `data/z52b/translate.jsonl`. Builder: `scripts/z52b_translate_build.py` (items are in `scripts/z52b_translate_items_*.py`).
