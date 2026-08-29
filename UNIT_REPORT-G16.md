# UNIT G16 report

- Added fixed §47 and exact `verify.py (at)`.
- Proved the exact one-step ratio `w_B Γ_S(B)` and the coprime contribution `O(Λ)`; old conditioning factors cancel in the ratio.
- Refuted literal (40.28): a retained squarefree `D=2` divisor cube gives `ℒ({A}) ≥ exp(cL/log L)` entirely at equal prime-power levels.
- The same cube refutes (37.19) for §37's prime-only-reduced count `H` at every `m ≍ Λ` and fixed base.
- This also refutes the proposed pairwise-coprime/squarefree restricted-`S` hierarchy (a singleton suffices).
- Proved the hierarchy for selected sets consisting only of tail prime atoms.
- Recorded why §39.3 thinning has no intrinsic-system analogue before composite-implication reduction; a finest atom deterministically triggers its coarser divisor atoms.
- Checked genuine higher/equal prime-power corners; (40.29) and the small-endpoint-only hierarchy remain open.
- Defined the union-preserving implication antichain and the exact repaired residual estimate (47.16); (40.19), (33.16), and `H_PF′` remain open.
- Default exact toy checks all 6,217 compatible degree-4 sets; the 99,362-triple power toy is behind `ES_FULL_SCAN=1`.
- `uv run --with sympy,numpy,scipy python verify.py` passes; control-byte and AST checks pass.
