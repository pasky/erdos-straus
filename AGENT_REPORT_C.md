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

---

# Step 2 report (POINTWISE_SIZE §§7–10)

§§0–5 are unchanged except for the intro sentence. Step 2 is in new
sections §7–§10. All scripts live under `scripts/pointwise_size_*.py`;
data under `data/pointwise_size/{wtail,window}/`. The Replay section is
updated.

## Results

1. **§7. The multiplier frame: the W(p)≤(log p)^A flag, quantified (Assessment).**
   * **What is exact.** For fixed T, `#{p≤N hard: W(p)>T} ~ δ*(T)π_h(N)`
     (PROVED). Here δ*(T) is the profinite avoider density.
   * **Measuring δ\*(T).** Exact Monte Carlo on Ẑ with multilevel
     splitting, nine runs, out to T=65535: `δ*(16383)≈7·10^{−13}`,
     `δ*(65535)≈2·10^{−17}`. The last value is noisy.
   * **Check against primes.** A census of all 6.35M hard p<10^9 matches
     `δ*·π_h` within 4% for T≤127, and within 18% (a deficit) at T=511.
   * **Shape.** `−log δ*≈0.77·I(T)`, where I is the independence exponent,
     computed to 2^20. The local exponent of `−log δ*` in `log T` rises
     from 2.3 to 2.6.
   * **Prediction.** Under the random-avoider heuristic RA, the
     one-expected-exceedance level of W over p≤N is about `(log N)^A`,
     with A = 2.5 (10^8), 2.8 (10^18), 3.1 (10^30) and 3.4 (10^50). The
     census is consistent with this.
   * **Consequence.** `H_MOD(A)` (notes §54) is **heuristically false for
     every A**. All that is needed is `log(1/δ*)=T^{o(1)}`. With the
     two-sided `−log δ*≍I≍(log T)^3`, the natural multiplier statement
     is `W≤exp(C(log p)^{1/3})`.
   * **What would make it rigorous.** (i) A prime-compatible analogue of
     notes Thm 31.4 (a unit-avoider lower bound). (ii) RA itself.
2. **§8. The window frame: the main candidate.**
   * **The statistic.** `a_min(p)` is the least q≡3 (4) with
     `Rat_q((p+q)/4)∋−1` or `−p`.
   * **Theorem 8.1 (PROVED).** `ES(p)⟺a_min(p)<∞`. The fixed-cutoff
     **X_win(C)**, `a_min(p)≤C log p` for all hard `p>10^18`, implies ES
     for any C.
   * **Lemma 8.2 (window reciprocity, PROVED).** `(r/q)=(r/p)` for every
     prime `r|(p+q)/4`. Hence (Cor 8.3) F1 is exactly the character trap,
     and for prime q every other failure is a budget failure.
   * **Prop 8.4 (escape).**
     * (a) PROVED: if p is a residue mod all primes ≤K, and every window
       a≤K is (residue constant)×prime, then `a_min>K`.
     * (b) Dickson gives infinitely many such p.
     * (c) Every bounded truncation is formally refuted.
     * Evidence: the self-checking adversary generator found 730/161/50/4
       such p for K=15/19/23/27, with `a_min` only slightly above K.
   * **Random model (Assessment).** The per-window marginal is
     `≈1.8(log p)^{−1/2}`, calibrated on single-window marginals at
     10^12 and 10^18. The model gives an extremal scale
     `Θ(log p/log log p)`, so X_win^∞(C) is heuristically true for every
     C>0. The formal-genericity obstruction sits exactly at
     `log p/log log p`. Data: `a_min/log p<10` everywhere tested (maximum
     6.69, at `p=8803369`, n_p=41). The concrete conjecture is
     **X_win(10)**.
   * **Numerics.**
     * Census of all hard and all Mordell-hard primes <10^8.
     * Samples at 10^12, 10^18 and 10^24.
     * Class-of-one primes, `p≡1 mod lcm(1..41)`: harder windows, but
       `a_min≤67`.
     * The formal adversaries.
     * W-record primes: their windows are small, e.g. W=2495 with
       `a_min=11`, and W=3263 with `a_min=23`.
   * **Position.** X_win is the *pointwise* form of J-window stacking with
     `J≍log p` (notes H_STACK §71), i.e. Wall (i). One structural
     consequence: equidistribution of divisors in the Erdős–Hall range
     `q≤(log p)^{log 2}` uses too few windows. Ratio sets up to `q≍log p`
     are needed.
3. **§9. Seeding by the least non-residue (E2).**
   * **Lemma 9.1 (PROVED).** Windows `q≡−p (mod 4n_p)` contain `n_p`, with
     `(n_p/q)=−1`, so they are never F1. For prime q they fail only by
     budget. Composite seeded q can still fail at the subgroup level; the
     reviewer's example is `p=349801`, `q=75`.
   * **Data.** The first seeded window fails 7.1% → 2.2% of the time from
     3·10^6 to 10^24 (fit `(log p)^{−0.9}`). Unseeded windows fail 60% →
     29% (fit `(log p)^{−0.56}`). At 10^18, two seeded windows fail jointly
     50× less often than two unseeded ones.
   * **Status.** `ES⇐X_QNR` (PROVED). It escapes in the necessary sense,
     conditionally on H. Refutation of its fixed-J truncations is only
     plausible.
4. **§10. Summary table, and an honest statement of what was not
   obtained.** There is no unconditional partial result beyond trivial
   or congruence-forced ones. No route to X_win itself is known.

## Self-review (deep reviewer subagent) and repairs applied

The review confirmed the following:
* the profinite sampler and the unbiasedness of the splitting estimator;
* Lemma 8.2;
* Prop 8.4(a), as originally stated;
* the reduction;
* the cheap replays;
* rat_hits against independent enumeration (1216 windows).

The following repairs were applied.

* **Prop 8.4(b) as first stated was false.** With `C_a=2^i3^j` no prime
  exists for K≥31. Generalised to `C_a` supported on Λ-primes that are
  residues mod p.
* **The formal-adversary generator was buggy.** It dropped square
  conditions and stripped factors from p itself. It is rebuilt and
  re-checks every hypothesis per p (0 rejections), and the table is
  regenerated.
* **X_win(C) with a fixed 10^18 cutoff is false for C<0.072.** The fixed
  form is now separated from the eventual form X_win^∞; the conjecture is
  X_win(10). The same is done for X_QNR.
* **Composite seeded windows** are added as a caveat; the F3-only
  statement is restricted to prime q.
* **The type label** in rat_hits was order-dependent. It is now intrinsic:
  Type II is available at the minimal window for 718191/719781 primes.
* **Assessment 7.2** now states its two-sided assumption, the sub-power
  versus polylog distinction, and that the predictions are
  one-expected-exceedance levels.
* **Model calibration** now uses measured single-window marginals, not
  joint tails with 2–7 observations.
* **Wording and data fixes.** Escape is now "necessary sense" where
  appropriate; nine runs, not five; 18%, not 17%; three primes with
  W>2047, not two; the K=15 p-range; "frames independent" softened; the
  Replay variable bug; the stale intro.

## Open points / for the parent

* **Thm 70.5 / Thm 70.9.** The per-window marginal `(log p)^{−1/2}` is
  cited from notes Thm 70.5/70.9: integer scale and shifted-prime upper
  bound. I did not re-verify those theorems.
* **Unproved model steps.** The window model's uniformity in growing q,
  and its neglect of rare correlated families, are not proved. The
  constant 8 in `8 log p/log log p` is a model output.
* **Missing piece for a rigorous §7.** The unit-avoider lower bound needs
  a mean value of divisors of `((M+1)/4)^2` in the class
  `−(M+1)/4 mod m`. That could be a self-contained follow-up task.
* **The K=31 formal-adversary run** (`M≈8.4·10^13`, `3·10^7` sieve
  steps) found no p. Larger searches would be needed to reach that
  depth.

## Replay

See POINTWISE_SIZE.md, Replay. The heaviest steps are the `split 65535`
runs (~15 min each), `windows 1e8 127` (~25 min) and `formal 23/27`
(~10 min each).

---

# Step 1 hostile review (side-agent/review-pointwise-size): repairs D1–D8 applied

Verdict: SOUND-AFTER-REPAIRS. All repairs are in one separate commit,
"Step 1 review repairs", touching §§0–5 only.

* **D1.** The precision rule `E_ℓ≥v_ℓ(D)` is replaced by the intrinsic
  condition (Prec) in §1.2. Lemma D, (F3') and the Theorem M proof are
  adjusted. §3.3 now says the following:
  * the certificate's data satisfy (Prec), but not the old rule. The
    reviewer found a violation with `v_2(den)=20` against `E_2=14`, and
    one at ℓ=233;
  * the (Prec) argument is given, both for monomial quotients and for the
    `R=0` tests under FORMAL_CLOSURE's (C2);
  * the literal 13521 match of S holds *for this certificate* (reviewer
    verified), not a priori.
* **D2.** (C3) is a remark: automatic at a point, binding only when a
  class is lifted. Λ' in Theorem C no longer lists the primes `≤Σdeg`.
* **D3.** `DIVISORS(0)` is totalised.
* **D4.**
  * §0 Theorem C now says "correct" (with the `SUCCESS (1,1,1)`
    counterexample) and "universally nondegenerate".
  * Corollary E names `P=24X+1`, or any linear P.
  * 3 is added to Λ', so `p≡1 (24)` for every linear P.
* **D5.** The E1 example's formal FAIL is now labelled CONDITIONAL on H,
  with an unconditional route via Schinzel added.
* **D6.** The least-non-residue argument is unconditional (Dirichlet), and
  the primitive's domain is specified.
* **D7.** Proposition A covers eventual-sign (Hardy-field) comparisons
  only. Oscillating archimedean tests, such as `{√p}<1/2`, are listed
  under E2, in §0 and in §4.1.
* **D8.** Positive d with `d||K_A|`; `q_0` forward reference; `σ:=0` when
  `R=0`; E3 wording made consistent ("open").

---

# Step 3 report (POINTWISE_SIZE §§11–12): unconditional Ω-results

## Results

1. **Theorem 11.2: `limsup_{p hard} W(p)/log p ≥ 5/8`.** This is PROVED
   modulo one cited theorem. Notes Thm 54.1 has `1/5.2≈0.19`. Two
   ingredients:
   * **The modulus.** Only moduli `M≡3 (4)` matter, so the class-of-one
     modulus is `L*(T)=lcm(24, M≤T, M≡3 (4))`, with
     `log L*=(2/3+o(1))T`. This is notes Lemma 66.2; the notes used it
     only for twisted families, not with prime selection.
   * **The least prime.** `L*(T)` is `O(log q)`-smooth. Chang (J. Anal.
     Math. 123 (2014), Cor. 11) gives a prime `≡1 mod q` below
     `q^{12/5+o(1)}` when `log P⁺(q)=o(log q)`; the statement was read in
     the author's PDF, archived in `sources/lit2026/`.

   More strongly, `L_h(T)≤exp{(8/5+o(1))T}` for all large T, which
   improves notes (58.18) (`5.2`). Other inputs give:
   * Linnik with Xylouris's exponent 5: 0.30;
   * GRH (Bach–Sorenson): 3/4;
   * a least prime `≪q^{1+ε}`: 3/2.

   The certified coefficient of this construction is capped at 3/2.
2. **Prop 11.2'' (PROVED; argument due to the Step-3 reviewer).** Every
   complete reduced prime-congruence certificate for `W>T` has
   `log Q≥(2/3−o(1))T`. So the class of one is optimal to leading order,
   and notes Thm 56.1's 1/2 is not sharp.
3. **Theorem 11.2': `limsup ck_min(p)/log p≥5/12`** (Type-I slices,
   notes Thm 54.3 modulus plus Chang). W and `ck_min` are both
   `≥(5/12−ε)log p` simultaneously, infinitely often.
4. **Lemma 11.3 (PROVED).** Window failure is never congruence-forced:
   every class of primes contains primes at which any given finite set of
   windows succeeds (CRT and Dirichlet). The class of one has no window
   analogue.
5. **Prop 11.4 (SKETCH).** `a_min(p)≥7` for `≫x/(log x)^{3/2}` hard
   `p≤x`, via the semi-linear sieve (Iwaniec, cited) and the parity of
   `(p+3)/4≡1 (3)`. The sieve details are not written out.
6. **Lemma 11.7 (PROVED).** `log(1/δ*(T))≤T^{1/2+o(1)}`. This is the
   first sub-exponential prime-compatible avoider bound, from a quarantine
   at `y=T^{1/2+η}` with CRT independence. It is still far from
   polylogarithmic, which is what superlinear W would need.
7. **Assessments 11.5 and 11.6 (method-specific, not barrier theorems).**
   * Windows: the simultaneous-F1 sieve has dimension `≈K/8` and fails
     for `K≥7` at BV level, and for `K→∞` at any level.
   * Superlinear W: the quarantine-plus-sieve error budget reaches only a
     linear range with the proved bounds.
   * A possible route to superlinear W is listed, with its missing inputs:
     an LLL-type Haar bound with polylogarithmic quarantine (the prime
     analogue of Thm 31.4), exceptional-character control, and control of
     the Bonferroni truncation under correlations.

## Answers to the brief

* **`a_min(p)>C log p` unconditionally.** Not obtained. The best
  construction here is the sketch `a_min≥7`.
* **`W(p)>(log p)^{1+δ}` unconditionally.** Not obtained. The best is the
  linear `W≥(5/8−ε)log p`.
* **A Bombieri–Vinogradov-averaged route avoiding Linnik.** The Linnik
  constant is avoided by Chang's smooth-moduli exponent, not by BV. BV
  averaging fails here because the needed moduli are sparse and
  structured, with only log-power savings available.

## Cross-checks (§12)

* **PW 2511.16817.** Thm 3.1 is a union bound with mass
  `≈(log N)^3/φ(m)<1/2` for large numerator m; at `m=4` the mass is
  `≫1`. PW define no truncated statistic. None of Prop 8.4, Lemma 11.3
  or Theorem 11.2 is in PW.
* **Notes §56, §58, §66.** Lemma 11.1 is notes Lemma 66.2. (58.18) is
  improved. Lemma 58.5 frames the remaining superlinear question.

## Self-review of Step 3 (deep reviewer) and repairs applied

The reviewer confirmed the headline constants 5/8 and 5/12, Chang's
applicability, Lemma 11.3 and Lemma 11.7. The following repairs were
applied.

* The certificate "gap [1/2,2/3]" was not open; it is replaced by
  Prop 11.2''.
* Assessments 11.5 and 11.6 are rescoped as method-specific; "all",
  "needs" and "precise list" are removed.
* Siegel-zero control is now listed as a missing input.
* Thm 11.2(d) now speaks of the certified coefficient.
* "Equivalently" is now "more strongly".
* The `log L` numbers are relabelled as the odd part `L=L*/8`.
* `T≥15` is required for hardness.
* Lemma 11.7: `0<η<1/2`, and the sum runs over eligible m.
* Prop 11.4: citations fixed (Iwaniec 1972 and 1976), and `ε<1/6`.
* The PW mass statement and the m=4 scope are corrected.

## Commits

* "Step 1 review repairs" (D1–D8), a separate commit.
* §11–§12 (Step 3).
* The Step-3 self-review repairs.

## Replay (Step 3)

```
PYTHONPATH=scripts uv run python scripts/pointwise_size_omega.py   # log L(T)/T to 1e7; least primes = 1 mod L*(T); < 1 min
```

---

# Round 2 review repairs (commit "Round 2 review repairs")

Verdict: SOUND-AFTER-REPAIRS (minor). The following repairs were applied.

* **R1.** (Prec): the Taylor condition is now *sufficient*, not
  equivalent. The reviewer's counterexample is included.
* **R2.** Prop 7.1(b): `δ*≥1/φ_h(L(T))=e^{−(2/3+o(1))T}`, citing
  Lemma 11.1 / notes Lemma 66.2. The §7.1 text now has
  `L(T)=e^{(2/3+o(1))T}`, and points to Lemma 11.7's stronger bound.
* **R3.** Prop 8.4(c) is relabelled: PROVED modulo Schinzel (via the E1
  route), or CONDITIONAL on H via Theorem C.
* **R4.** Lemma 9.1 now covers n=2 (`p≡5 (8)` gives `(2/q)=−1`), and the
  prime-q subgroup step is argued directly.
* **R5.** Stale cross-references are updated to 5/8 and 5/12: §0 Scope 3,
  §4.3 (Q1), §7.3 and the §10 table. The X_QNR escape is now
  unconditional. "Hard" is defined per section.
* **R6.** Theorem 11.2' is labelled. Chang Cor. 11 is stated to be
  unconditional, with Siegel zeros handled via Heath-Brown. Effectivity is
  not claimed, in contrast with notes §54.
* **R7.** A note that `log P⁺(q)≍log log q` puts us far inside Chang's
  safe range.
* **R8.** `gcd(x,q)=gcd(x,p)` holds for every q.
* **D6 nit.** We pass to the subclass mod `lcm(M_g,8c)` compatible with
  q*, which also covers c=2 and the `c|M_g` case.
* **§7.2.** The splitting estimator is unbiased but heavy-tailed. A
  few-run mean typically underestimates δ*, so the deepest rows are
  biased toward faster decay. The reviewer's plain-MC agreement at
  T=127 and T=511 is recorded.
* **Reviewer's remark (Assessment, next to 7.2).** Lemma 11.7 plus RA
  predicts `W(p)>(log p)^{2−ε}` infinitely often, with RA the only
  unproved input.

The work is complete pending merge.
