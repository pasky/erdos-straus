# AGENT_REPORT_O224 — wave Z-a: a 4-specific input from the 2-adic χ-fibre

Branch side-agent/four-adic-input. Deep file `FOUR_ADIC_INPUT.md`; 8 memos `BRAINSTORM/z1_*.md` (indexed in
BRAINSTORM/README.md); scripts `scripts/z1_*`; data `data/z1/legendre_big.txt`. **ES is not solved, nor any infinite case.**

## SHARP:
1. **Fano pigeonhole (PROVED, elementary; FOUR_ADIC_INPUT Thm 1.3, memo z1_fano_pigeonhole).** This is a conceptual 6-line
   proof of MODEL_SPECIFIC Thm 3.1(a) (S_4 = {χ = −1}), which was previously proved by cell enumeration or Dedekind sums.
   * Q mod 4 is well defined on L/2L, and the even classes W ∖ 0 form a 3-point line of the Fano plane.
   * The five pentagon entries t, u, v, A, A* are, up to the odd factor n in the last two, the norms of e₁, e₂, e₃, n·e₁^#, n·e₃^#.
   * Frieze parity: exactly two entries are even, giving two distinct points of W ∖ 0.
   * An isotropic odd unimodular ℤ₂-lattice has exactly two nonzero points with Q ≡ 0 (mod 4), and they also lie in W ∖ 0.
   * Two 2-subsets of a 3-set meet.

   Reading: a certificate is a path-shaped 2-isogeny edge plus a pentagon vector pointing at one endpoint (the two isotropic
   classes are the two maximal overorders of CONSTRUCTIVE_ES Thm 1.2(b)), and the pointer always exists.
2. **The 2^k bit law (PROVED at cell level for every k; CERTIFIED by all cells mod 32 for k ≤ 5).** S_{2^k} covers f_k = (2/3)2^{−(k−2)} + (1/3)(1 − (1 − 2^{−(k−2)})²) of
   the χ = −1 cells: 7/12, 5/16, 31/192. These are exactly MODEL_SPECIFIC's unexplained 140/240 and 600/1920. So each extra
   power of 2 costs one fair bit per isotropic pentagon vector, and 4 costs none.
3. **The bits are correlated (EVIDENCE).** On actual words of primes p ≡ 1 (4) < 4000, independent bits would predict 0.82
   primes with S₈ = ∅. 12 are observed. At 131 and 241 every entry divisible by 4 has v₂ exactly 2. This is the quantitative
   form of "8/p fails where 4/p cannot".

## Main conclusions
* **Requirements (i)–(iv) (FOUR_ADIC_INPUT §2).** Let P = SQ₅ ("some path lattice of det p is 2-adically isotropic").
  * P ⟺ ES-five(p).
  * (iii) holds automatically (T1), and P also fails at 105.
  * (ii) holds in the strong sense: P(131) and P(241) are true while 8/131 and 8/241 are false, because 8 needs the extra
    bits. For 11/37 there is no character analogue. For TES and ES_q, P has no transcription: "not applicable", not checked.
    Over F_q[T] (q odd), 4 is a unit, so there is no 2-adic input at all.
  * (iv) fails: pigeonhole forcing exists only for M ∈ {2, 3, 4} (z1_small_prime_pigeonhole), so it does not explain 7.
  * So the 4-specific 2-adic input is used up by Thm 1.3, and (i) is the numerator-free CONJECTURE SQ₅.
* **Steering / negative results.**
  * Lattice side.
    * S_M is not even an isometry-class property for any M with φ(M) > 2 (PROVED via norm-one triples, z1_marking_isometry).
    * Siegel–Weil on lattices containing M_{v,t} sees only the square-root class of −p/v mod A*, while extending the fixed
      basis of M to a path basis needs glue ±1 (PROVED, marked statement, z1_glue_square_roots).
    * Path classes are "glued planes": a divisor form in the plane's class plus glue residue ±1 (Prop 3.1).
  * Walks and numerator arithmetic.
    * No lattice/Hecke/isogeny walk crosses χ (z1_isogeny_pointer).
    * "4 is a square" is refuted by 9/p and 16/p.
  * Legendre levels.
    * Levels with tp = 4^a(8b+7) are a character-free sub-lottery (every word there certifies by Thm A + Legendre).
    * It fails at 73, 1201, 1489, 9649, 21169, 23041, 44641 (all p ≡ 1 (4) < 10⁶ checked, full level range for the failures).
    * At odd squares it yields T1 in Legendre form (0 words at Legendre levels, all odd squares ≤ 10⁸, levels ≤ 3000).

## Self-review (deep reviewer, `review` tool, since 53204707): no FATAL; all findings accepted and repaired
* Gluing (MAJOR). "L_c is a path lattice iff c ≡ ±1" was false unmarked (p = 11, c = 4 gives the path (4, 1, 4) in another
  basis), and the root count 2^{ω−1} − 1 failed at 2-power moduli. Now stated as the marked extension criterion, with no count.
* Prop 3.1 (MAJOR). A pointwise "≍ log²p path classes" was an overclaim (it would imply SQ₅), and the minima relation was false.
  Both were removed and replaced by an on-average heuristic.
* S₆ norm-one proof. An invalid unit inference was replaced by a finite residue check (`z1_s6_residues.py`).
* Prop 1.4. The finite certification is upgraded to a proof for all k (independent uniform even entries per parity pattern).
* Isogeny memo. The false "expander resolution threshold" was replaced by the correct limitation (expansion cannot prove a
  thin target non-empty).
* Wording: "same t" coupling claim; M = 5 example memberships reversed; small-prime example contained 5; "exactly two
  nonzero classes"; 320 (not 4096) triples; 3 ≤ n < 1500; supersingular reading restricted to prime n; interior-marking
  uniqueness kept conditional; "not determined by χ" instead of "no character description"; TES/ES_q "not checked" carried to
  intro and outcome.
* The reviewer independently reproduced the 35 179-word check, the mod-32 fractions, the Fano enumeration, the
  4785 / 0.5014 / 12-vs-0.82 statistics, and all seven Legendre failures over their full level ranges.

## Verification done
* Thm 1.3 / Lemma 1.1:
  * word-level, all 35 179 words of odd n < 1500, 0 violations (`z1_thm13_check.py`, sympy Jacobi);
  * cell-level, `z1_fano.py`.
* Prop 1.4: exact fractions, `z1_depth_cells.py 5`.
* Marking: `z1_marking.py 3 400`, `z1_marking2.py 300`, `z1_interior_unique.py 600`.
* Legendre levels: `z1_legendre.c` (primes ≤ 10⁶, odd squares ≤ 10⁸, single-n full ranges).
* There are no positive ES-type claims, so no 10⁶ triple-check of an existence statement was needed.
* Items a reviewer should re-derive:
  * Lemma 1.1 case analysis;
  * that Lemma 1.2 (CONSTRUCTIVE_ES Lemma 1.1: "exactly two classes") applies to every word;
  * Prop 2's unit construction (gcd(n, M) = 1, n odd; confirmed by the self-review);
  * the marked gluing statement in z1_glue_square_roots (repaired).

## Labels
* PROVED: Thm 1.3, Lemma 1.1, z1 Props (marking Prop 2/3(a,b), small-prime classification, Legendre Prop 1/Cor 2, gluing,
  no-crossing).
* PROVED (cell level) / CERTIFIED (k ≤ 5): Prop 1.4.
* EVIDENCE: bit correlation, Legendre failures, S₆ class-invariance, uniqueness of interior markings.
* Assessment: tree-depth reading of 2^k slices, F_q[T] remark.

## Sparks (not pursued)
* **Global Fano.** Thm 1.3 is a pigeonhole inside one word. Is there a pigeonhole over the 2-isogeny graph? Each certificate
  edge carries a pointer to an endpoint. Do pointers along a walk in G_p satisfy a parity law that forces a path edge
  somewhere?
* **Depth bits on the tree.** Prove the Assessment that depth-k pentagon vectors point at vertices at distance k − 2 beyond
  the Eichler edge. Then 8/p becomes an X₀(4) problem with a marked step, and the correlation of §1.3 may be explained by
  Ptolemy (J)45 plus v₂(tp + 1).
* **The order-3 analogue.** The TES T1 over ℤ[ω] ((J)19) might have a "Q mod 3 on L/√−3 L" pigeonhole of the same type. Test
  whether TES's 16 failures are exactly where an order-3 Fano analogue has no target.
* **S₆ class-invariance.** Why is S₆ a union of isometry classes for gcd(n, 6) = 1 but not a genus function? If interior
  markings are provably unique (Greene's graph-lattice theorem), (ℤ/M)^* = {±1} gives a full proof.
* **Legendre failures.** The 7 Legendre-level failures are all ≡ 1 (mod 8) and include 73 and 1201, both hard for other
  sub-lotteries. Compare them with the hard primes of (J)45 and (J)53.
