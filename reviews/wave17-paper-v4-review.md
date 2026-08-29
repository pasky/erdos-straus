# Wave-17 paper v4 fidelity review

**Verdict: FAITHFUL-AFTER-REPAIRS.**  The v4 additions accurately transcribe the source notes and preserve the provisional register.  One post-v4 status defect was repaired minimally: source §49 has since refuted the implication-antichain hierarchy (47.16) and the corresponding reduced-count moment route.

## Scope

Read `paper/espaper.tex` in full, the full v4 status/fidelity list in `paper/README.md`, source §§39.7, 41, 43, 46–49, and the M17 paper diff.  The review covered the two headlines, the PW comparison, §§46–48, internal-review pedigree, bibliography, build, and hygiene.

## Defects

| ID | Class | Finding | Disposition |
|---|---|---|---|
| D1 | STRUCTURAL | Four live-frontier sentences still called (47.16) the repaired **OPEN** wall, which became false when source §49 refuted both that hierarchy and the reduced factorial moments. The README queue also still treated (47.16) as future work. | **REPAIRED** at `paper/espaper.tex:79`, `:137`, `:997`, and `:2709`, each flagged `% (wave-17 fidelity repair)`; added the required README erratum and corrected the v5 queue. No §49 proof material was imported. |
| — | TRANSCRIPTION | No defect found in the audited statements or formulas. | — |
| — | OVERCLAIM | No defect found. Refutations remain confined to internal sufficient mechanisms; the conjecture, `H_PF'`, (33.16), (37.27), and (40.19) are not claimed refuted. | — |

## Fidelity findings

- **Theorem 43.12:** exact `≪_ε`, `c_ε`, fourth root, `η₂(m)L³/φ(m)`, and `3 ≤ m ≤ L^(3−ε)` range; both prime and all-denominator forms are present. Theorem 34.8/43.7 and all three §39.7 qualifications remain visibly inherited and **CLAIMED/PROVISIONAL**.
- **Finite relative mass:** paper (43.36) matches source symbol-for-symbol: finite cutoff `K`, coefficient `(1−p⁻¹)/p^e`, inner condition `(a,pm)=1`, and upper bound `H_m(K)/p`. The quarantine, `M=η₂(m)t³/φ(m)`, even degree, `O(Mt)` ledger, fixed-gap audit, and semigroup `γ` also agree.
- **PW comparison:** (43.32)–(43.34) use the adjudicated scales. `R/P={η₂(m)³φ(m)L}^{1/12}` and `L≥1/(η₂(m)³φ(m))` are exact; constants are explicitly excluded from a literal finite crossover. The common `m≤L²` regime and the separate provisional `m≤L^(3−ε)` regime are honestly distinguished.
- **§47 scope:** the nested cube refutes literal (40.28) and raw-`H` (37.19), not `H_PF'`, the pair route, or the conjecture. The antichain deletion direction, unchanged union/void, `Q_S`, `w_B`, prime-power factors in `Γ_S`, and quantifiers in (47.16) match source §47. Source §49’s later grid refutation is now stated only as a status erratum.
- **§46:** `W₁=floor(zL²/log L)≈L⁵loglog L/(log L)²`, `W₂=floor(zW₁)`, the full prefix, the `c≥z, m≤zW₁` wedge, and the exact ordered distinct-cell remainder (46.13) all agree. Pair target (40.19) remains open.
- **§48:** `χ_s(p)=1 ⇒ M_{c,k}(p)=0`; the identically-one set is exactly `{1,2,3,6}`. Theorem 48.4 retains the fixed-`d`, reduced hard-class, admissibility, necessity-within-shape, and refinement scopes. Theorem 48.5 retains bounded full modulus and residue-one escape. Census values `385/77/(12289,76)` and `1181/103/(92401,102)` are exact and explicitly computational only.
- **Pedigree:** the §43.11 allowed-read scope, freeze hash, convergence/divergence summary, post-freeze adjudication, and self-attestation limitation are accurate. The paper consistently calls all such checks internal rather than external validation.

## Formula and README checks

Displayed formulas checked symbol-by-symbol: (43.35), (43.36), (43.34), (47.16) with its `Γ_S` definition, (46.8), (46.13), (48.2)–(48.3), and (48.16)–(48.17). No range, local factor, prime-power exponent, or constant-dependence discrepancy was found.

README fidelity entries spot-checked: Theorem 43.12; (43.36)–(43.42); (47.16); Corollary 46.3/(46.13); and Theorem 48.1. Their transcription claims are accurate; the new one-line §49 erratum supersedes only the stale status of (47.16).

## Global and mechanical checks

- Abstract and introduction retain the honest two-headline framing: `m=4` with exponent `3/4`, and general `m` with the fourth-root local-factor scale.
- “Unconditional” is narrowed to “assumes no unproved hypothesis”; external verification, blocked Vaughan access, and “first improvement found since 1970 **if** review succeeds” are explicit.
- Every `\cite` key resolves to a bibliography item; M17 added no unresolved citation key.
- Two `pdflatex -interaction=nonstopmode espaper.tex` runs exited zero. The final log had zero TeX errors and no undefined references or citations; output remained 45 pages. Only pre-existing nonfatal `hyperref`/`amsmath` warnings remained.
- `paper/espaper.tex` control-byte count: **0**. `notes.md` and `verify.py` were untouched.
