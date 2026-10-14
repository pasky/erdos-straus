# s3_order3_numerator — (J)19/(J)28 order-3 world × (J)31 TES failures × (J)32 m = 4 uniqueness

**Combines:** (J)19 (TES: 9/n = ω/x + ω²/y + 2/z over ℤ[ω], order-3 T1), (J)28 Thm 3.5 (TES^{□₃} at every 2-primary
non-cube prime to 6, rel. Chebotarev), (J)31 Thm 2.1 (TES fails at 16 2-primary split primes, N(π) ≤ 30000; none BM),
(J)32 (over ℤ, only m = 4 has a χ-fibre slice set). Brief item: "(J)19 order-3 T1 × (J)32 m = 4 uniqueness".

## Idea
(a) Is the order-3 relaxation blind to TES's genuine failures (the order-3 instance of SYNTHESIS_SPARKS3 Cor 2.1)?
(b) Does the order-3 world admit an analogue of the m = 4 phenomenon — a numerator-free character target whose
non-vanishing implies the exact problem?

## Results
(a) PROVED by combination: the 16 TES failures are 2-primary split (N ≡ 1 mod 3) primes prime to 6, hence non-cubes,
so (J)28 Thm 3.5 gives TES^{□₃} there. EVIDENCE (`scripts/syn2_tes_shots.py 27000 50`, 15 s): all 5856 2-primary split
primes with N(π) ≤ 27000 are solved in TES^{□₃} by the explicit recipe (equation exact), including all 16 failures and
both associates; T1₃ control: 0 shots at cubes. So the order-3 relaxation is blind exactly as M^□ is over ℤ.
(b) Logical constraint (PROVED, trivial): any statement T₃(π) "some word of π has a non-trivial cubic character value"
that is (i) numerator-free and (ii) implies TES(π) must be FALSE at the 16 failures — although they are non-cubes, where
an order-3 analogue of SQ₅ would predict truth. So in the TES normalisation, an "SQ₅₃" (non-cube ⇒ character
non-constant on words) and a "χ₃-fibre slice theorem" cannot both hold. Over ℤ the pair (SQ₅, S₄ = {χ = −1}) is
consistent with all data to 10⁸ ((J)15, (J)32). (R207 repair m8: the logic does not use numerator-freeness, and "SQ₅₃" / "χ₃-fibre" are unformalised; the following is an
Assessment.) This is a sense in which **the numerator 4 over ℤ is special
while 9 over ℤ[ω] is not**: the order-3 world has genuine non-T1, non-BM failures, so any T1-plus-character mechanism
transplanted from ℤ must break there.

## Literature
TWISTED_T1, TES_FINITE, SYNTHESIS_SPARKS2 §3; Bright–Loughran over ℚ(ω) (Br U/Br K ≅ ℤ/6) as used in (J)31.

## Barrier screen
(a) is the numerator-blindness barrier; (b) is a consistency screen for any future "order-3 template" (O182's anchor
calculus) — it predicts failure, so the order-3 world is a *testing ground for refuting* candidate mechanisms: a
mechanism that proves ES and transplants to TES is wrong.

## Cheap numerics
As in (a). The word/character structure of TES slices was not built (needs a ℤ[ω] word enumerator; `scripts/tf_core.py`
has the arithmetic) — left as a spark.

## Assessment
(a) PROVED + EVIDENCE; (b) PROVED (logic) with an Assessment reading. Useful as a falsification harness: every (E1)/(E2)
candidate should be run against TES at N(π) = 7, 13, 19, … and against 8/n at 131, 241. Promise as route 0; as tool:
medium.
