# R124 — hostile review of POINTWISE_TERNARY.md (O124)

Reviewer branch `side-agent/review-ternary`, merged `side-agent/ternary-embed` at review time.
From-scratch scripts: `scripts/review_tern_sweep.py`, `scripts/review_tern_qd.py`, `scripts/review_tern_ratio.py`;
logs `logs/review_tern_*.txt`. Sources checked: ET arXiv:1107.1010v6 (local PDF; Thm 1.1 p.4, remark p.5, Prop 1.6
p.6, definition p.7–8, Prop 1.9 p.8, (2.1)–(2.22) pp.11–14); Pila, Astérisque 228 (1995) 183–187 (downloaded from
numdam, Theorem A read verbatim). NOT accessed: Mordell's book pp. 287–290, Schinzel [68], Duke–Schulze-Pillot,
Blomer, Golubeva–Fomenko, HKK (these enter only through (M), which ET restate, and through hypothesis (R)).

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.3 (level sets) | SOUND |
| Lemma 2.1 (fibre count, definite, incl. k ≥ 4 slicing) | SOUND (MINOR m3) |
| Pila input (P) | SOUND — matches Pila Thm A (uniform in the variety; `H^{n−1+1/d}·exp(12√(d log H log log H))`) |
| Prop 2.2 | SOUND |
| (M), Lemma 3.1, Cor 3.2 | SOUND (MINOR m2 on the "consequence of Prop 1.6" parenthetical) |
| Thm 4.1 (a), (b) | SOUND; constants uniform in `p`; exponent `(k−2)/2 − 1/4 + ε` re-derived |
| Cor 4.2 (`𝒫_R ⊆ U`), ε₀ < 1/4 | SOUND relative to (R) (MINOR m1 wording "exactly") |
| Cor 7.1 (sterile points) | SOUND (square part is immediate from Cor 4.2; x** part imported from MORDELL13E, not rechecked) |
| Lemma 5.1, Prop 5.2, Cor 5.3, Pell example | SOUND (MINOR m3, m4) |
| Comp 6.1 (57 substructures, all isotropic, unique rank-3 `Q_d`) | SOUND — reproduced exactly with an independent ideal/saturation setup |
| Prop 6.2 | SOUND-AFTER-REPAIRS (MINOR m5: "not mild" proof sketch is not a proof as written) |
| §8 Step 4 EVIDENCE | SOUND — reproduced exactly (10⁶ failures, 10⁷ table, 10⁸ extremal prime, 10⁸ 1/20 sample, ratio) |
| Scope / novelty Assessments | Essentially right, but understated in two places (MAJOR M1, MINOR m6) |

No FATAL defects. One MAJOR (scope presentation), six MINOR.

## Re-derivations (what I checked and how)

(filled in below, claim by claim)
