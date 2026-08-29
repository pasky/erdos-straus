# UNIT J16 report

- Blind construction: `blind43.md`; frozen pre-comparison at `a0bd2940c322cb69426cf83df7f903d563b49648`.
- Blindness is self-attested from the enforced read log, not cryptographic.
- S1, S2, S4, and S5 converged with §43; normalizations differ only by fixed Euler constants.
- S3 diverged mildly: §43's Layer-1 theorem is correct, but its all-denominator range is conservative.
- S6/S7 diverged substantively: a finite relative-mass inequality permits thinned `y,r` and an `O(θ_m t^4)` ledger.
- This yields the new provisional scale `[η₂(m)(log N)^3/φ(m)]^{1/4}` and its corresponding PW crossover.
- The wave-15 mixed local-factor correction is correct and does not obstruct the stronger upper bound.
- §43 is not wrong; Theorem 43.8 remains unchanged, with a clearly flagged stronger CLAIMED/PROVISIONAL route.
- `notes.md` adds §43.11 attestation and the affected-location Wave-16 flag.
- Full `uv run --with sympy,numpy,scipy python verify.py` passed; `notes.md` has zero control bytes.
