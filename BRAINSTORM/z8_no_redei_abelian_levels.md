# z8_no_redei_abelian_levels — a single sign-field level only sees genus data (O232, spark S1)

**Idea.** Explain the residual near-square depletion (O225 §3) by a Rédei/4-rank layer: c ∈ ⟨σ_r⟩G² \ ⟨σ_r⟩.

**Literature.** Rédei (J. reine angew. Math. 171 (1934)) 4-rank; Stevenhagen, "Rédei reciprocity, governing fields and
negative Pell" (Math. Proc. Camb. Phil. Soc. 2022, arXiv:1806.06250) — Rédei symbols are Frobenii in dihedral fields.

**Barrier screen.** H-D (non-abelian data) is the open hatch this would need; with abelian level fields it is closed:
SIGN_FIELDS Prop 3.1 — word existence at level u is a function of the residues r mod 4u of the prime factors of p + u.

**Cheap numerics.** Not run (spark: add a group-clean flag to `scripts/z2_hardness.c` and redo O225 §3 residuals).

**Assessment.** PROVED (Prop 3.1, trivial) + Assessment: no forcing beyond genus at a single abelian level; a
non-genus mechanism needs either non-abelian level fields (none arise from the five-slice words) or correlations across
levels. Negative steering result.
