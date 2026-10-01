# Agent report C: task (c), Step 1 (formal-genericity meta-theorem)

Branch `side-agent/pointwise-size`. Deliverable: `POINTWISE_SIZE.md` §§0–5.
Machine checks are in `scripts/pointwise_size_*.py`, with outputs under
`data/pointwise_size/`. Step 2 has **not** started. I am stopping here for
parent review, as the brief asks.

## What was done

1. **Theorem M (transfer principle), PROVED.**
   * **Programs.** A small instruction set: ring operations, floor
     division, sign tests, FACTOR/DIVISORS, list loops; plus while-loops
     and extra primitives in the extended form.
   * **Formal run.** A program is run formally at a profinite point
     `q*∈Ẑ`. Every polynomial met factors into "formal primes" `h/C_h`,
     and floors are computed by Lemma D.
   * **Conclusion.** If the formal run is finite, then at every admissible
     q the actual run on `p=P(q)` follows it step by step.
   * **Existence of admissible q.** Under H for the polynomials met there
     are infinitely many. Bateman–Horn gives `≫N/(log N)^{|S|}`. Dickson
     suffices for linear families; Dirichlet/Linnik suffice if only p
     occurs.
   * **Static version.** Corollary M1 is the brief's form (`p mod M` plus
     factorisation shapes of fixed `f_i(p)`).
2. **Lemma CT (character trap), PROVED** from notes Thm 17.1 and
   Lemma 77.6. For `p≡1 (4)`, every p-free denominator of every positive
   solution has a prime factor that is a non-residue mod p. Checked on
   all 15555 solutions with `p≤5000`.
3. **Theorem C (formal odd-square principle).**
   * **PROVED part.** At a square-mimicking, universally nondegenerate
     point, every admissible q makes a correct witness-producing program
     with a finite formal run output FAIL.
   * **CONDITIONAL part.** Under H for one explicit finite family, every
     correct **bounded** witness-producing program fails for infinitely
     many `p≡1 (24)`.
4. **Instances, with an exact dictionary.**
   * Cor 17.3.1 and Thms 5.1/17.3/Prop 77.3 come from the rational point
     "1" with Dirichlet, unconditionally. Thm 54.1 is the Linnik
     quantitative form; Thm 54.3 is its genus analogue.
   * DEPTH3 Theorem 2 is Theorem C for `BFS_k`.
   * Theorem F is Theorem M for the while-program `BFS_∞`. The finite
     formal run is the 7883-vertex closure; FAIL is (C4). This gives the
     literal 13521-polynomial form; the 6402 refinement is the
     weak-genericity remark.
   * The EST remark: Theorem C is its precise H-conditional form for
     procedures.
5. **Scope.**
   * **Proposition A, PROVED.** Size comparisons of formal quantities,
     including against `c·p^θ` and short-interval tests on formal
     divisors, are *inside* the scope. So the archimedean feature (ii) of
     the brief does not escape by itself.
   * **Corollary E (under H).** A correct ES procedure must have an
     infinite or undefined formal run at every square-mimicking point:
     * (E1) unbounded p-dependent search; or
     * (E2) non-quasi-polynomial primitives (`⌊p^θ⌋`, least non-residue,
       orders), whose actual factorisations are then used.
   * **(E3)** Fixed non-abelian Frobenius information does *not* escape,
     modulo a Schinzel–Chebotarev hypothesis (stated, not developed).
   * **(E4)** Boolean/counting certificates and almost-all statements lie
     outside the meta-theorem. The meta-theorem is silent about them; it
     does not refute them.
   * **Quantitative thresholds.**
     * Congruence mechanisms need `≥(1/5.2−ε)log p` moduli. PROVED (notes
       §54).
     * Factoring mechanisms need `≳log p/log log p` factorised values.
       Assessment (uniform Bateman–Horn).
6. **Toy EVIDENCE.**
   * **Agreement.** Actual output equals formal output on 654 actual
     admissible primes. Program: Type I/II windows `a∈{3,7,11}`,
     `m∈{3,7}`, `p` up to `2.6·10^13`.
   * **Square-mimicking point.** The output is FAIL there.
   * **Non-square-mimicking point.** At a point that is not square
     mimicking at 7, the output is SUCCESS. This shows the formal engine
     is not trivially FAIL.
   * **Non-admissible primes.** 2955 of 3000 non-admissible primes in the
     same class succeed. Each success goes through a composite formal
     prime with a QNR factor.

## Points I would like the reviewer to check

* **Lemma D and the FACTOR step of Theorem M.** In particular, check the
  deduction that `K_A∈Z` at admissible q, and that the ordering of FACTOR
  output is eventually formal.
* **Theorem C's character computation** `(r_h/p)=(H_h/p)(u/p)^{−deg h}(C_h/p)`.
  Check also the choice of Λ'. Linear P is essential to both.
* **The claim that Theorem F is literally an instance.** The dictionary
  table is in §3.3. My lift of the certificate's class to a profinite
  point needs `q*_ℓ` off the roots of S for `ℓ∉Λ`. This is possible by
  their (C3) and because roots are finite mod ℓ.
* **Notes Thm 54.3.** I describe it as an analogue, not an instance. Its
  slices are not congruence classes: genus theory at an actual prime
  `p≡1 (mod R(T))` replaces the H-conditional character argument.

## Corrections and remarks for the parent

* **STATUS.md "e.g. by using the size of p".** Proposition A shows that
  size comparisons of formally given quantities are inside the
  obstruction. Size helps only through unbounded families (E1) or
  non-polynomial integers (E2). A STATUS wording update is suggested.
  I have not edited STATUS, since that is the parent's file.
* **DEPTH3.md cites EST "p. 5"** for the odd-square remark. In the
  archived PDF it is on printed p. 6, immediately after Prop 1.6.
  LITERATURE_2026 already says p. 6.
* **A heuristic flag for Step 2, not claimed.** In the independent model
  with the cubic intrinsic supply (notes Thm 18.2), `W(p)≤(log p)^A`
  fails infinitely often for **every** A. This is because
  `exp{−c(log T)^3}` with `T=(log p)^A` is not summably small. So the
  "frontier `A≥1`" of notes §54 is probably heuristically false. The
  real pointwise target needs witness moduli as large as
  `exp(c(log p)^{1/3})`. To be quantified in Step 2(b).

## Decision requested

May I proceed to Step 2? The planned direction (POINTWISE_SIZE §6) is:
E1 candidates with `p^θ`-length windows (short-interval / Hooley-Δ /
Erdős–Hall–type divisor statements in moving residue classes), and E2
candidates seeded by the actual least non-residue. Each gets a
random-model check before any numerics.

## Replay

```
(ulimit -v 4000000; PYTHONPATH=scripts uv run python scripts/pointwise_size_ct_check.py 5000 1000)   # ~20 s
(ulimit -v 8000000; PYTHONPATH=scripts uv run python scripts/pointwise_size_toy_formal.py 20000000)  # ~3 min
```
