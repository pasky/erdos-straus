# R292 — independent hostile review, round 1

Reviewed author branch `side-agent/paper-expfam`, merged into this worktree; no access to reviewer #1's review or branch. Author files are not modified. This is a claim-by-claim working review; numerical results and final recommendation are added below as completed.

## Referee summary

The paper separates congruence identities polynomial in n from identities polynomial in an exponential root. It uses forced algebraic divisors to complete finite exponent coverings for three families having a genuine obstruction to finite ET/divisor coverings, supplies further coverings for ten offsets, and proves restrictions on constant-gap and constant-ratio root identities. It does not claim ES for arbitrary primes. The new claim for 15·2^s+1 removes all exponents outside 60Z, rather than removing the obstruction at exponent zero.

## Claim 1: Section 2, odd squares and Theorem 2.7 (`thm:sterile`) — SOUND

I re-derived both Jacobi-symbol arguments. In Type I, c coprime to n gives e=(a+b)/c and 4abd=ne+1; in Type II, e=4abd−n gives ce=a+b. In either case reciprocity gives (q/e)=1 for the odd part q of ab, whereas b≡−a mod e gives (ab/e)=−1. Hence ab is even, which forces e≡7 mod 8 and contradicts (2/e)=−1. All necessary coprimalities are present.

For the class corollary the fixed-parameter product really does suffice, including I1's moving c and II2/II3's moving b. The CRT construction in Theorem 2.7 chooses a square representative coprime to those parameters; primes outside the modulus are independently avoided. Divisor classes cannot contain the residue 4^J at their odd prime. Taking exponents divisible by L·ord(2) handles arbitrary L and arbitrary lower thresholds. Restriction to base 4 is legitimate. No uniformity or finite-versus-infinite-cover gap found.

The proposition classifying integer unit-square points is also sound under the positive c0,k convention of the paper. For negative exponents the numerator is odd and >1 (or has 2-adic valuation one in the even-c0 case), excluding a unit square at every odd prime.

Minor definitional issue to repair: Definition 2.4 (`def:rule`, lines 350–360) calls a finite list an exponent covering when every uncovered s is “treated separately”, without requiring that exceptional set to be finite. Taken literally this makes the non-covering claims false/vacuous. Say “all but finitely many exponents are covered, with explicit solutions for the finitely many exceptions.” This is defect D1 (MINOR); the proofs consistently use the intended finite-exception meaning.
