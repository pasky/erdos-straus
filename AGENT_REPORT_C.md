# Agent report C: task (c), Step 1 (formal-genericity meta-theorem)

Branch `side-agent/pointwise-size`. Deliverable: `POINTWISE_SIZE.md` §§0–5.
Machine checks are in `scripts/pointwise_size_*.py`, with outputs under
`data/pointwise_size/`. Step 2 has **not** started. I am stopping here for
parent review, as the brief asks.

## What was done

1. **Theorem M (transfer principle), PROVED.**
   * **Programs.** A small instruction set: ring operations, floor
     division, a divisibility test, sign tests, FACTOR/DIVISORS, list
     loops. The extended form adds while-loops and extra primitives.
     Errors are totalised to FAIL.
   * **Formal run.** A program is run formally at a profinite point
     `q*∈Ẑ`. Every polynomial met factors into "formal primes" `h/C_h`.
     Floors use Lemma D, divisibility tests use (F3'), and integrality is
     Lemma I.
   * **Conclusion.** If the formal run is finite, then at every admissible
     q the actual run on `p=P(q)` follows it step by step, outputs and
     witnesses included.
   * **Existence of admissible q.** Under H for the polynomials met there
     are infinitely many. Bateman–Horn gives `≫N/(log N)^{|S|}`. Dickson
     suffices for linear families. Dirichlet suffices if only p occurs;
     Linnik also applies when there is no threshold.
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
4. **Instances.**
   * Cor 17.3.1 and Thms 5.1/17.3/Prop 77.3 come from the rational point
     "1" with Dirichlet, unconditionally. Thm 54.1 is the Linnik
     quantitative form. Thm 54.3 is a genus analogue, not an instance.
   * DEPTH3 Theorem 2 is Theorem C for `BFS_k`.
   * **Theorem F is Theorem M for the while-program `BFS_∞`.**
     * The finite formal run is the 7883-vertex closure, and FAIL is (C4).
     * The certificate's own Λ, `E_ℓ` and `q0` serve as the data, so the
       H-family is exactly theirs.
     * This gives the literal 13521-polynomial form. The 6402 refinement
       is the weak-genericity remark.
   * The EST remark: Theorem C is its precise H-conditional form for
     procedures.
5. **Scope.**
   * **Proposition A, PROVED.** Size comparisons of formal quantities,
     including against `c·p^θ` and short-interval tests on formal
     divisors, are *inside* the scope. So the archimedean feature (ii) of
     the brief does not escape by itself.
   * **Corollary E (under H).** A correct ES procedure must have an
     undefined or infinite formal run at every square-mimicking point:
     * (E1) unbounded p-dependent search; or
     * (E2) non-quasi-polynomial primitives (`⌊p^θ⌋`, least non-residue,
       orders), whose actual factorisations are then used.
   * **(E3)** Fixed non-abelian Frobenius information is **open**.
     Theorem M does not cover it, since a congruence point does not
     determine Frobenius. A decorated extension under a
     Schinzel–Chebotarev hypothesis is proposed, not proved.
   * **(E4)** Boolean/counting certificates and almost-all statements lie
     outside the meta-theorem. The meta-theorem is silent about them; it
     does not refute them.
   * **Quantitative thresholds.**
     * The multiplier and slice mechanisms `W(p)≤T(p)` and
       `ck_min(p)≤T(p)` fail infinitely often when
       `T≤(1/5.2−ε)log p`. PROVED (notes §54). This bounds the size of
       the witness parameters, not the number of objects consulted.
     * For the explicit window family, a restricted Bateman–Horn model
       refutes the first `K=o(log p/log log p)` windows. This is an
       Assessment, not a general bound.
6. **Toy EVIDENCE.**
   * **Agreement.** The complete actual output, witness included, equals
     the formal output on 331 + 323 actual admissible primes. Program:
     Type I/II windows `a∈{3,7,11}`, `m∈{3,7}`, `p` up to `2.6·10^13`.
   * **Square-mimicking point.** The output is FAIL there.
   * **Non-square-mimicking point.** At a point that is not square
     mimicking at 7, the output is SUCCESS with `d=4`.
   * **Non-admissible primes.** 2955 of 3000 non-admissible primes in the
     same class succeed. Each success goes through a composite formal
     prime with a QNR factor.

## Self-review (reviewer subagent, deep mode) and repairs made

The review confirmed the following as correct: Lemma D, Theorem M(a)(b)
under the defined-run hypothesis, Lemma CT, Theorem C's character
computation, the existence of `q*_univ`, Proposition A, and §§3.1–3.2.

The following repairs were made.

1. **Corollary M1.** It lacked the precision `E_ℓ≥v_ℓ(M_0)` for
   `p mod M_0`. Added.
2. **The first toy verifier was wrong.** It enumerated formal divisors in
   a non-eventual order and compared only success flag and window. At the
   `nsq` point it said `d=2r²`; the actual run used `d=4`. Fixed: eventual
   order, and the complete output is now compared. The rerun gives 0
   mismatches.
3. **The Linnik clause of M(d) ignored the threshold `q_0`.** It is now
   qualified; Thm 54.1 has no threshold.
4. **Definedness.**
   * Added Lemma I (Ẑ-integrality, so `K_A∈Z` always).
   * Totalised errors.
   * Handled non-eventually-positive output denominators in Theorem C.
   * At `q*_univ`, bounded programs always have defined, finite formal
     runs.
5. **Theorem F.** Two changes make the dictionary exact without
   refining the certificate's congruence data:
   * §1.2 no longer requires leading-coefficient primes (35 such primes
     lie outside the certificate's Λ) or all primes `≤Σdeg` in Λ. It uses
     (C3) instead, and primitivity of `f_h` is proved without lc primes.
   * A `DIVIDES` instruction was added. It needs precision only when
     `R=0`, which is their (A)/(B) split.

   We checked the test correspondence on paper, not by re-verification.
6. **Q2.** Restricted to an explicit window model. The general claim is
   withdrawn.
7. **E3.** Downgraded to open / proposed. "Only p-dependent families of
   fields escape" is withdrawn.
8. **Q1 summaries.** Now say "size of witness parameters".
9. **§6.** Separates necessary escape (Corollary E) from global escape.
10. **Minor wording.** p is excluded from "every prime seen is a residue";
    `n_p∉Λ`; "quadratic characters `χ_s`" for Thm 54.3; digits of p are
    no longer listed as automatically E2.

## Points I would like the parent's reviewer to check

* **The formal machinery.** Lemma D, (F3'), Lemma I, and the FACTOR step
  of Theorem M. In particular, check that the ordering of FACTOR output is
  eventually formal.
* **Theorem C's character computation**
  `(r_h/p)=(H_h/p)(u/p)^{−deg h}(C_h/p)`, and the choice of Λ'. Linear P is
  essential to both.
* **The Theorem F dictionary (§3.3).** Is (F3') with `R≠0`/`R=0` really
  their (A)/(B)? Do their `E_ℓ` cover every `D'` with `R=0`?
* **Notes Thm 54.3** is presented as an analogue, not an instance.

## Corrections and remarks for the parent

* **STATUS.md "e.g. by using the size of p".** Proposition A shows that
  size comparisons of formally given quantities are inside the
  obstruction. Size helps only through unbounded families (E1) or
  non-polynomial integers (E2). A STATUS wording update is suggested.
  I have not edited STATUS.
* **DEPTH3.md cites EST "p. 5"** for the odd-square remark. In the
  archived PDF it is on printed p. 6, immediately after Prop 1.6.
* **A heuristic flag for Step 2, not claimed.** In the independent model
  with the cubic intrinsic supply (notes Thm 18.2), `W(p)≤(log p)^A`
  fails infinitely often for every A, since `exp{−c(log T)^3}` with
  `T=(log p)^A` is not summably small. So the "frontier `A≥1`" of notes
  §54 is probably heuristically false. The real pointwise target needs
  witness moduli as large as `exp(c(log p)^{1/3})`. To be quantified in
  Step 2(b).

## Decision requested

May I proceed to Step 2? The planned direction (POINTWISE_SIZE §6) is:
E1 candidates with `p^θ`-length windows (short-interval / Hooley-Δ /
Erdős–Hall–type divisor statements in moving residue classes), and E2
candidates seeded by the actual least non-residue. Each gets a
random-model check before numerics.

## Replay

```
(ulimit -v 4000000; PYTHONPATH=scripts uv run python scripts/pointwise_size_ct_check.py 5000 1000)   # ~20 s
(ulimit -v 8000000; PYTHONPATH=scripts uv run python scripts/pointwise_size_toy_formal.py 20000000)  # ~3 min
```
