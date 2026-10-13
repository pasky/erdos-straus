# AGENT_REPORT_O174 — spark brainstorm A on the Hirzebruch–Jung / Farey reformulation

Branch `side-agent/spark-hj-brainstorm`. Deliverables: 9 memos `BRAINSTORM/bsA_*.md` (indexed in BRAINSTORM/README.md), deep file
`HJ_DEEP.md`, scripts `scripts/bsA_*`. **ES is not solved, nor any infinite case of it.**

## SHARP:
1. **SQ₅ = (W) ∧ (S), and (W) is a published open question.** (HJ_DEEP §3.) For n ≡ 1 (4), the interior five-slice condition splits
   into two parts.
   * **(W)** says n = xyz − x − z for some x,y,z ≥ 2 (sign-free; n ≥ 2). This is *exactly* Lorenzini's question on the critical polynomial
     of the path graph A₃ (*The critical polynomial of a graph*, preprint 4 Dec 2022, Example 6.2(a); text checked by me): is the
     complement of the value set {0,1,2,3,5,6,9,11,14,15,35,105,510}? He says "we have not been able to answer this question" and
     gives partial results (Prop 6.3).
   * **(S)** says: if n is not a square and L₃(n) ≠ ∅, then some length-3 word has Jacobi −1. This is "T1 is the only
     obstruction".
   * **EVIDENCE to 10⁸** (`scripts/bsA_ws.c`, 54 s): (W)'s exceptions are exactly Lorenzini's list, and (S) has 0 violations. So
     interior SQ₅ holds for all non-square n ≡ 1 (4) < 10⁸ except 5 and 105 (DK had 10⁶). **DK's lone SQ₅ exception 105 is a
     (W)-exception**: it has no length-3 word at all, so the sign plays no role there.
   * Lemma 3.2 (PROVED): no finite covering by fixed-pair congruence families proves (W), because the class n ≡ −1 (mod M) always escapes.
2. **Master identity** (HJ_DEEP Lemma 1.1, PROVED): tuv − u − v = n ⟺ t/n = 1/(uv) + 1/(un) + 1/(vn). **All of Type II** = *formal* three-letter
   words K(a, 4cd, b) = cp, with outer letters ≥ 1 and middle ≡ 0 (mod 4c) (Prop 2.1). Outer letter 1 is not a genuine HJ word., and the sign is automatic, (A/p) = −(−1/p) (Prop 2.2). This is the HJ form of (I)7.
3. **ES sign = Wu-square** (bsA_wu_rokhlin_sign, Thm W; PROVED for HJ length r ≤ 5 by a finite mod-8 check relative to DK Cor 4.1;
   EVIDENCE for random lattices): (A/n) = +1 ⟺ w·w ≡ n + r − 1 (mod 8), with w the characteristic vector of the plumbing lattice.
   DK's five cells become the single congruence w·w ≡ p + 6 (mod 8). Rokhlin reading (conventions from memory): μ(L(n,A)) ≡ 1 − n (mod 8) iff +1.
4. **HJ length = popcount ∘ Minkowski ?** (bsA_minkowski_stern M1; PROVED, exhaustive check n < 200). So five-slice ES(p) ⟺
   p = s(2^k + m) (Stern's diatomic sequence), with popcount(m) ≤ 3 and (s(m)/p) = −1.
5. **Farey least non-residue** (bsA_farey_lnr_pigeonhole): r(n/A) + r(n/(n−A)) = Σ a_i (exact), and λ(p) ≤ (6/π² + o(1)) ln²p
   unconditionally (rel. Yao–Knuth). That beats the GRH conversion λ ≤ n_p ≤ 2 ln²p, but it has no ES content (B3 gap).

## What was done (one line each; labels in the files)
* bsA_farey_lnr_pigeonhole: unconditional λ bounds; pigeonhole is T1-safe but needs radius ≍ ln p ln ln p. Promise 1.
* bsA_selling_sandpile: a word is the 4-vertex multigraph "hub + path" with p spanning trees. ES ⟺ the non-square genus G⁻(p)
  contains a linear lattice, which is a class-layer condition reducing to Type II Heegner data (B2). Promise 1.
* bsA_lens_homotopy_surgery: (A/p) = −1 ⟺ L(p,A) is not homotopy equivalent to L(p,1), and such L(p,A) are never knot surgery in any
  ℤHS³ (Greene's world is the QR side). At squares ES is blind to homotopy (explicit L(m², A) examples). Promise 0–1.
* bsA_farey_graph_metric: signed CFs (true Farey-graph metric) give λ_F = λ (EVIDENCE p < 6000). Signed ES is trivial, yet sign
  freedom adds no QNR. Promise 0.
* bsA_fricke_vieta: the word is a point on the 4-holed-sphere Fricke cubic with boundary traces (v,t,u,T), T = tuv − t − u − v. The
  Vieta/BGS dynamics acts on the fibre, and ES lives on the base, so the brief's Markoff question has a precise negative answer. Promise 0.
* bsA_hecke_cusp_excursions: QR/QNR = split-torus orbits of Hecke points, and λ ≤ 3 = a three-excursion large deviation of measure
  p^{−1+o(1)}. Promise 0.
* bsA_wu_rokhlin_sign: SHARP 3. Promise 1.
* bsA_toric_ksb_wahl: at prime index the only T-singularities are A_{p−1} (QR), so certificates are never ℚ-Gorenstein smoothable.
  Promise 0.
* bsA_minkowski_stern: SHARP 4. Promise 1.
* HJ_DEEP: §1–§3 as in SHARP 1–2. §4 has six construction attempts (radius growth, multiplier growth, sign-flip transfers incl.
  scaling = reparametrisation (Lemma 2.3), genus/Kneser moves, injections/parity, direct attack on (W)), each steered by a named barrier
  hypothesis. Prop 4.1 is the exact reduction of (S): (S) fails at n ⟺ for all t, every admissible divisor X ≡ −1 (t) of tn+1 lies in
  the kernel of q ↦ (q/n). That is the sign-layer/class-layer skeleton in its sharpest form (H-A).

## Verdict (Assessment)
No route to ES. The HJ picture reduces to **one shape** (Lorenzini's A₃ critical polynomial, equivalently t/n of Type-II shape) and
**one sign** (the Wu/Jacobi class). Each half alone is tame: (W) is T1-free with a finite exceptional list, and (S) is
T1-sharp. Every mechanism I tried handles only one half. The best handle for the campaign: (W) is a published, T1-free, sign-free
sub-problem with a clean exceptional set, on which H-A ideas can be tested without B5 interference.

## Self-review (deep reviewer subagent, all findings repaired)
Repairs made:
* Prop 2.1 now concerns formal words (outer letters may be 1; counterexample 4/5 = 1/2 + 1/5 + 1/10), and "divided by d" was corrected.
* Prop 4.1 now carries its hypotheses (n ≡ 1 (4) non-square, L₃(n) ≠ ∅; it was vacuous at 105).
* The Lorenzini summary was corrected: Prop 6.3(a) also excludes m = 2, 4, and Remark 6.4 lists 0, 6, 510.
* Pointwise "|L₃(p)| ≍ log²p" claims were downgraded to averages.
* Fricke F3 now requires T ≥ 3 and reads "three-letter presentation", not primitive cycle.
* The error term in Thm 3 was restored in the summaries.
* The Greene/KSB scope was narrowed: they classify subsets of the QR side.
* The Wu checker now tests residue 0/4 explicitly, and the M1 terminal block is spelled out and re-checked.

The reviewer independently reproduced `bsA_ws.c` to 10⁸, `bsA_wu2.py`, `bsA_typeII_words.py`, M1 and Lemma 2, and it confirmed the
proofs of Lemma 1.1, Prop 2.2, Lemma 2.3, Lemma 3.2, Thm 3 and M1.

## Checks run
`bsA_hjlen.py check` (HJ via regular CF = direct, n < 400). Lemma 2 for n < 300. `bsA_selling.py 4`. `bsA_wu2.py` (24 692 words + 3 000
random lattices). `bsA_minkowski.py 150 3000`. `bsA_typeII_words.py 3000` (9 431 solutions, exact rationals, T1: 0 at squares).
`bsA_ws.c 10⁸` plus an independent HJ-algorithm cross-check of (W) for n < 3000. `bsA_cover2.py` (M up to 12 252 240).
`bsA_fareydist.py 6000`. `bsA_fricke.py`.

## Sparks (not pursued)
* Lorenzini also lists conjectural exceptional sets for A₄, A₅, A₆ (HJ length 4–6). Is there an ES-like sign reading at length 4
  (Thm W gives the sign) that makes a sister conjecture "(W₄) ∧ (S₄)"? (S_r) for all r would be "T1 is the only obstruction for words of length r".
* Prove (W) for n ≡ 1 (4) in a positive-density or "all but O(N^ε)" form. Lorenzini's Prop 6.3 plus a sieve over the u = 2, 3, 4, …
  shapes should give almost-all easily. A *pointwise* proof is H-A, but without T1 in the way.
* (S) small-|L₃| census: 18 of 30 small cases are all −1, where independent coins would give ≈ 2–3 all-(+1) cases among the 30. Probe sign correlations
  inside L₃(n), e.g. between words sharing a letter. A positive correlation mechanism would be H-B-flavoured.
* Other degenerate Voronoi/Selling types (other conorm 0/1 patterns) as encodings of other ES slices (bsA_selling_sandpile).
* Stern's sequence is 2-regular. Is there an automata-theoretic statement about primes occurring at low-weight indices with a QNR partner?
* A Bourgain–Kontorovich bilinear argument for λ(p) ≪ ln p (Burgess in the Farey metric). It has no ES meaning, but it would be a nice theorem.
