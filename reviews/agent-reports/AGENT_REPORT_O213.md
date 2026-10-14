# AGENT REPORT O213 — spark relay Y5: the transport law (TRANSPORT_LAW.md, memos BRAINSTORM/y5_*)

Branch side-agent/transport-law. Merged: side-agent/frieze-es and main (incl. the R208 repairs of FRIEZE_ES).
**ES is not solved; no infinite case of ES is claimed.**

## SHARP
1. **The transport law is the Ptolemy relation mod 8 (PROVED; a sharp negative).** The relation through the even edge
   is ee′ ∈ {1 + o, N + o, 1 + No}. So for N ≡ 1 (8):
   * every word has o ≡ 3 (4);
   * certificate ⟺ o ≡ 7 (8);
   * "−(2/o)" is just "o mod 8", i.e. the slice condition itself.

   The sign does not move to a better-behaved small-modulus quantity. CERTIFIED on 784 732 words.
2. **General-r Jacobi law with an explicit archimedean factor (PROVED).** For every integer word with N = K_r > 0 odd
   and all K_i ≠ 0:

   (K_{r−1}/N) = ∏(K_i, −K_{i+1})₂ · (−1)^{#{i: K_i < 0 < K_{i+1}}}.

   * Proof: leading-minor Hasse invariant + product formula.
   * This closes O210 spark 1: one 2-adic factor per continuant step, not backtrack runs.
   * It makes "positivity = archimedean factor" (spark 5) an explicit Maslov count.
   * CERTIFIED on 131k positive and 66k signed random words.
   * Classical in substance (the Jacobi symbol along a continued fraction).
3. **Positivity = complex conjugation (PROVED dictionary).**
   * At fixed m, positive words are factorisations 1 + Nm = ab with a ≡ b ≡ −1 (mod m). Negative-pair words are the
     +1 class and have s_∞ = −1 (R211 repair: the trivial factorisation is c = 0, not a word).
   * In the e-slice form, −1 ∈ Σ_e(N) is the narrow-minus-wide ray class element c_∞. In the wide group the condition
     is trivial.
   * Steering: any object that sees only wide or unsigned data is ES-blind (Assessment).
4. **Mordell position alone (CONJECTURE SQ_H, EVIDENCE).** Certificates with an even middle letter m and 8 | m·e (e the
   even outer letter) exist at all 165 976 primes p ≡ 1 (8) ≤ 10⁷. They fail at exactly 22 composite non-squares
   N ≡ 1 (4) ≤ 10⁶ (105, 1465, 3865, …, 392505), a new fingerprint list. Honest caveat: the mean count is about 27, so
   this is a sub-lottery that is expected to survive.
5. **Fingerprint p = 21841 = 1 + 2⁴·3·5·7·13.** It has exactly one interior certificate pair, (9, 64, 38) and its
   mirror. Its least certificate vertex is o* = 2431 = 11·13·17, the unique outlier ≤ 10⁷ (next largest 335).

## Brief items
* (a) The o-progression family exists: P_h, o = h ≡ 7 (8), condition N mod o ∈ C(o) = −{c | o+1 : c, (o+1)/c even},
  and C(o) consists of Jacobi non-residues.
  * Density is τ(o+1)/o, not 1/2.
  * B2 re-enters per position as one relation sh = N + c (Type II for o = c, Type I for o = m), or as a thin
    congruence in P_h, where the factorisation moves to o + 1.
  * T1 is one Jacobi symbol in every position.
  * Relative to (J)26 Thm 3.1 (plus an Assessment-level identification of P_h classes with ET classes), there is no
    bound o_h* ≤ f(n_p).
* (b) Census:
  * o* = 7 for 94 % of p ≡ 1 (8) ≤ 10⁷; max 2431 interior and 239 formal;
  * the hard primes are quadratic residues mod 840 (R211 repair of "≡ 1 (120)") with least QNR 11–29;
  * o* is a divisor-event statistic, not a residue symbol (only P_h is QNR-shaped);
  * no Burgess-type gain.
* (c) Spark 4: no mod-16/32 shadow at squares (EVIDENCE to 10⁵), so T1 is one bit. Spark 1: SHARP 2. The
  r-uniqueness for r ≥ 5 was found independently with the same word as R208, credited to R208.
* (d) Siegel–Weil on full-rank data is the genus indicator (standard). The sign is the 2-adic genus label, and positivity
  is definiteness. SQ₅(p) ⟺ the χ = −1 genus (≍ p classes) contains a path-basis lattice (≪ p^{1/3+o(1)} of them):
  a thin-set lottery. Negative.

## Files
* TRANSPORT_LAW.md (deep file, §0 iteration log with the barrier hypotheses targeted).
* Memos, indexed in BRAINSTORM/README.md: y5_transport_is_ptolemy, y5_five_positions, y5_ocensus_hard_primes,
  y5_mod16_shadow, y5_general_r_jacobi, y5_narrow_wide, y5_siegel_weil_chamber, y5_even_middle.
* Scripts: y5_ptolemy_check.py, y5_ocensus.c, y5_positions.c, y5_general_r.py, y5_mod16.py, y5_words_at.py.
* Logs: y5_ocensus.txt, y5_positions.txt, y5_mod16.txt.

## Honesty notes
* SHARP 1 is negative: it deflates O210 SHARP 2.
* SHARP 2's formula is an elementary consequence of standard Hasse-invariant theory.
* The Kubota-cocycle identification is not verified (Assessment).
* SQ_H is weak evidence: the lottery heuristic predicts it.
* Literature is cited from memory (Cassels, Lam, Neukirch, Conway–Sloane, Kudla). No web check was done.
* No self-review subagent was run.

## Sparks (not pursued)
1. **Maslov positivisation.** Signed length-3 words at N are abundant and give QNRs cheaply. Can the change in HJ length
   under positive reduction be expressed by the Maslov/Rademacher count of Thm 3.1? A formula "λ(N/A) = 3 + (Maslov
   defect)" would turn SQ₅ into a statement about signed words.
2. **21841 and the C(o)-covering.** Characterise the primes whose only interior certificates have huge o. Are they
   exactly the primes ≡ 1 mod (8·3·5·7·13…) near sterile points of (J)26?
3. **SQ_H exceptions.** The 22 composite failures ≤ 10⁶ mostly have a small odd factor (R211: not 199 369 = 193·1033). Is there a genus/local explanation
   (as for 105), or is it the lottery?
4. **Narrow/wide over other fields.** In ℤ[ω] (the order-3 T1 of (J)19), the analogue of c_∞ is absent (complex
   place). Where does the TES obstruction sit in the narrow/wide picture?
5. **General-r with coefficients.** Thm 3.1 for friezes with general frozen boundary (CHJ) might give the Jacobi law for
   ES^□-type pentagons (Q², 1, 1, 1, n) of LENGTH_THREE §6.
