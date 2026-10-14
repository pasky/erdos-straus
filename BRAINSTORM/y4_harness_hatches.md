# y4_harness_hatches — the numerator harness on the open hatches (O212, goal (d); O208 spark 3)

## Idea
Run O208's harness (8/131, 8/241; new 11/37 from y4_t1_numerators; TES failures; ES_q failures; odd squares) on the
partial hatches H-A, H-B, H-D, H-E, H-F, WINDMILL_REDUCTION Remark 10.4, and SQ₅/χ-flip. A hatch dies if its
*stated* mechanism is numerator-uniform, since its 8-version would then wrongly prove 8/131.
(Calibration after R207 D1: a uniform mechanism with an explicit threshold n > n₀(M) is not refuted by finitely many
failures. Threshold-robust form: Pomerance–Weingartner Thm 1.2 gives, for every M ≡ 0 (4), M ≥ 6.52·10⁹, a prime
p ∈ (M², 2M²) with M^□(p) ∧ ¬(M/p). The test below therefore applies to mechanisms uniform in M with no threshold or with n₀(M) ≤ M²; a larger
(e.g. polynomial M³) threshold is NOT excluded by this argument (R-O212 repair).)

## Literature / sources inspected
STATUS.md §Escape hatches; PARITY_FIXED_P §2 (Assessment 2.2); GROWING_IDENTITIES Summary; GROWING_MUTE;
BRAINSTORM/nonab_frobenius_redei; QUATERNION_ES §§1–2; KUDLA_ES §§1–2; STRONG_APPROX_ES §9; GEOMETRY_ES §0;
WINDMILL_REDUCTION Rem 10.4; HJ_DEEP §3; CHI_FLIP §1.6. Survey by a research subagent; verdicts below re-checked by me
against the quoted statements (Rem 10.4 and the H-E Assessment read directly).

## Barrier screen = the harness (verdicts)
| hatch | stated mechanism | 4 enters | verdict |
|---|---|---|---|
| H-A | aggregate joint factorisation of a growing family Θ(p), moving modulus | only through the class (−1 mod 4cd) | **skeleton uniform; content = the lottery.** No theorem is stated, so nothing is killed, but the 8-version of every H-A step leads to the same divisor-in-class event, which is empty at 131 for d even. Any successful H-A must therefore feed a numerator-sensitive input (e.g. the χ-fibre), not the factorisation framework alone. |
| H-B | parity-breaking count of divisors in a moving class at fixed p | sign sieve uses 4ad, 4cd; reduces to H-A (PARITY_FIXED_P Ass. 2.2) | same as H-A. The sign layer it controls is the □/sign layer, which is blind (s3_box_bit). |
| H-D | non-abelian object with nonzero coefficient | dictionaries are 4-shaped (4dm − 1, 4abd); no object specified | not testable as stated; the quaternion dictionary (J)33 is 4-specific only through χ = −ε₂ — that piece is the χ-fibre. |
| H-E | exact positive identity | GROWING_IDENTITIES: none found; STRONG_APPROX §9: finite Eisenstein combinations killed by T1 | open. Harness requirement: the positivity input must fail for 8 at 131 — T1 alone does not (8 has T1). |
| H-F | integral geometry beyond BM | GEOMETRY_ES §0: "BM-only for the ES model" ≡ ES | the uniform principle "BM-only for all m/n surfaces" is FALSE (8/131, BL Rem 1.10). Only an ES-model-specific geometric input survives. |
| Rem 10.4 | ray class group mod t of ℚ(√−tp) sees "N𝔪 ≡ −1 (mod t)" | the class −1 mod t; uniform in t | **uniform encoding; dead as an existence mechanism.** It restates the target coset; the 8-analogue target is non-empty at 131 for every t ≡ 0 (8) with the right sign, while the divisor hypercube misses it. |
| SQ₅ / χ-flip | some word has χ = −1 (numerator-free) | through Thm 3.1(a) S₄ = {χ = −1} | **4-specific; passes the harness**: at 131 there are 29 χ = −1 words and S₈ = ∅, so SQ₅ does not imply 8/131. Also passes 11/37 vacuously (no 11-slice statement). |

## Cheap numerics
None new beyond `scripts/y4_t1_numerators.py` (the 11/37 certificate) and O208's 131/241 data; the verdicts are
logical classifications of stated mechanisms.

## Assessment
All the partial hatches are **uniform skeletons whose missing content is a lottery input**. The harness does not kill
them, because none of them states an existence theorem. For a mechanism uniform in M without threshold (or with n₀(M) ≤ M²),
it shows what the missing input must be: an event that is false for some (M, p) with M^□(p) ∧ ¬(M/p) (8/131, 8/241 if
there is no threshold), so not T1, not BM, not the sign/□ layer and not ray-class encodings. Among known objects only the χ-fibre
(SQ₅, (J)32/(J)33) passes. This sharpens O208's reading and adds no new route.
