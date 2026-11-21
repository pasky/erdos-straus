# Hostile cross-lab review, round 3: `notes/z80/JUGULAR_COVER.md` (Thms H–J) and `notes/z80/ES_JUGULAR.md` §§10–11 and §0

Reviewer: Claude Opus (Anthropic). The author is the GPT Astra lane. Reviewed commit `2762a2832` (branch head; `git log main..`).
The earlier Opus reports cover §§1–9: `REVIEW_ES_JUGULAR_OPUS.md`, `REVIEW_ES_JUGULAR_D_OPUS.md` and
`REVIEW_ES_JUGULAR_R2_OPUS.md`. I re-read §§1–9 only for context. I spot-checked that the R2 fixes in `7da7663e1` were
applied (§0 Result/Review/Label, E restricted to the square-block model, the one-block control, "every Type I solution", the G
label, and the REPLAY split). They were.

## 0. Verdict

**ACCEPT WITH FIXES.** I checked every new proof step of H, I and J. The mathematics holds. I found no gap that changes a
label. The fixes needed are about attribution, labels, wording and scope:
* a FRONTIER-mandated citation is missing (K-R-K, wherever the 3/4 bound is quoted);
* both §0 blocks are incomplete (Review status of §§10–11, label inputs);
* the "exponent" wording is ambiguous in both §0 Result lines;
* there are several notation collisions and undefined symbols.

No master file is touched on the branch (checked with `git diff main.. -- STATUS.md WAVES.md FRONTIER.md …`: empty). The
STATUS delta "none" and the triage BARRIER-SCOPED are appropriate. Nothing here is, or is presented as, an ES proof.

## 1. Replays and independent checks (bounded: `ulimit -v ≤ 6000000`, `timeout ≤ 1800`)

| check | result |
|---|---|
| Author replay `scripts/z80_packet_density.py 7 11 16 24 32 48 64 80`, run from the repo root | byte-identical to `data/z80/jugular/packet-density.txt` (≈1 s) |
| **Independent** packet enumerator (my own code, sympy `n_order`/`legendre_symbol`; packets defined directly as "4G\|p+q and, for neutral, (p/q)=−1"), then a brute count over the full period of reduced residues ≡a (840) | **T=16** (P=960960): 1/12 and 13/24. **T=24** (P=22102080): 7/40 and 13/24, for all six classes. These match the script exactly. The author's own cross-check reaches only T=16 and shares `atoms()`; T=24 is new independent coverage. T=32 has P≈4·10⁸ and was skipped as over budget. |
| Independent empirical check at T=80: all primes 10⁴<p<10⁸ in each class (≈3·10⁴ per class) | 0.4550/0.4538/0.6931/0.6980/0.4550/0.6927 against exact 0.4523 (a≡1,121,361) and 0.6915 (a≡169,289,529). All within 2.4σ. The small uniform upward offset fits a Chebyshev bias: the hit classes are Jacobi non-residues, see §2.3. |
| Event counts | 37 neutral packets at T=80, in both engines; 7 and 14 CRT atoms at T=7 and 11, matching by hand |
| Square avoidance of single-block classes (used in J step 1) | brute force over all 738 classes −q mod 4G with q<120, G<1500, G≡−1 (q): 0 contain a unit square. A two-line proof is in §4.1. |
| Calibration, singles only versus full union (author's CRT engine, atoms filtered) | T=16: 0.083/0.083 against 0.083/0.542. T=80: 0.389/0.445 against 0.452/0.691 (a=1/169). At small heights the neutral packets matter a lot: at a=169 the 60\|p+11 packet holds on the whole class. This does not contradict J, which concerns log-power only. |

My scripts are kept outside the repo as requested; the sketches are in the Appendix.

## 2. Theorem H (exact density) — sound

* **Reduced classes.** q∤G because G≡−1 (q) or G is a product of units mod q. So −q is a unit mod 4G, and the neutral CRT
  classes are units mod 4Gq. The intersection of compatible reduced classes is one reduced class. Inclusion–exclusion over a
  finite set of fixed moduli plus PNT in APs gives exactly `1−dₐ=Σ_S(−1)^{|S|}c(S)φ(840)/φ(m(S))`. The script implements
  this signed-class recursion correctly: d = 1 − (avoid mass). All 840-consistency is handled by `crt`.
* **Height convention.** The script uses q≤T and G≤T, i.e. max(q,G)≤T, as stated. Generators are of exact order Q. k is the
  least integer with 3^k≥Q. Representatives g≡h^{3^i} run from the least positive residue upwards.
* **Normalization paragraph.** "δ(T)=d₁(T)/6" and "δ_all(T)" are **undefined in the note** (they are presumably from the
  brief). Define them or delete the sentence. The same applies to the §10 sentence "their limiting density inside all six
  prime classes is 1/6", which is trivially true and out of context.
* **Symbol clash.** The note uses `E` for the event set, for Theorem E and for generic events in J. Rename it, e.g. 𝓔.

### 2.3 Remark on the empirical offset (no action needed)
Every single-block class is a Jacobi non-residue mod the odd part of 4G (see §4.1). Primes up to 10⁸ are known to be biased
toward non-residue classes, so a slight empirical excess over the exact Haar density is expected. This is consistent with H
and is not evidence against it.

## 3. Theorem I (upper bound and finite-range transfer) — sound; attribution missing

I checked the following in detail.
* **Distinct targets and independence.** At a pivot r, the labels (k,q) give classes −q mod r. Since q<r these are
  distinct, and k≡−r⁻¹ (q) with k≤K<q fixes k. Distinct r are independent coordinates, and r∤M. Conditional on c, hits are
  therefore a sum of independent Bernoullis with at most one event per r. This is exactly what makes
  `E[C(hits,j+1)|c]=e_{j+1}(p)≤μ^{j+1}/(j+1)!` legitimate. It also sidesteps the divisor-cluster failure of raw Bonferroni
  recorded in `I3_DEEP_ASTRA.md` Caution 8.5. This is worth one explicit sentence in the note, because a reader who knows 8.5
  will look for it.
* **q-block BV.** The moduli are 4k≤4T^{1/200}≤4V^{1/10}. BV with max over the class is uniform in c. The main term is
  `(1/log V)Σ_{k∈J}1/φ(4k)`, which is ≥H/(2log V) trivially. It is ≪H by the divisor-closure bound
  `Σ_d μ²(d)/(dφ(d))·H`. The main term ≥1/(C log V) dominates `log^{−A}V`.
* **Pivot BV + BT, "double BV weighted errors".** The pivot moduli are q≤T^{1/10}≤x^{1/6}. The Cauchy split is
  `Σb(q)E(q) ≤ (Σb²/q)^{1/2}(Σ qE(q)²)^{1/2}`, and `qE(q)²≤E(q)·x/log x` by BT. With `Σb²/q≪L·Σ1/[k,k′]≪L⁴` (the
  integer majorant is valid because V>K²), the error is ≪xL^{2−(A+1)/2}, against a main term ≍xH/L. This is correct. The
  bound is uniform in c because BV and BT both take the max over residue classes.
* **Conditional selector transfer.** The selector is ℓ∤n for ℓ≤y=L outside 840. Primes ℓ>y are CRT-independent of the
  selector.
  * `E e^{yZ}≤exp(Σ_{ℓ>y}(e^{y/ℓ}−1)/ℓ)=O(1)`: the terms with ℓ∈(y,2y] give O(1/log y) and the tail gives O(1/log y). So
    P(Z>1/2)≪e^{−L/2}.
  * On Z≤1/2, `H≥(1−Z)H_full≫L`, since `Σ_{ℓ|k}1/k≤H_full/ℓ` for ℓ∤210.
  * The even-degree Bonferroni majorant satisfies S_j≤1[void]+C(hits,j+1): `S_j=C(h−1,j)` for h≥1 and `C(h−1,j)≤C(h,j+1)`.
  * The integer remainder is ≤(j+1)T^{j}2^{π(L)}=e^{O(L²)}, with O(1) error per AP.
  * With log T=c₀√log N the total is `N e^{−cL}+N^{Cc₀²}`. Correct.
* **One-sidedness.** The argument only ever bounds *misses* from above. No prime is produced at a specified input. Correct.

**Attribution (required).** The architecture is the one in K-R-K, in the internal 3/4 note and in Dahan II §7: a prime pivot
times a rough cofactor, conditional CRT independence, an even Bonferroni majorant and BV. FRONTIER §1 (lines 89–106) records
this and *requires* citing K-R-K wherever the 3/4 bound is mentioned. COVER "Exponent comparison", ES_JUGULAR §10 ("the
unrestricted 3/4 bound") and §11 ("the stronger ambient 3/4 theorem") all quote 3/4 without K-R-K or a pointer to
`paper/es-threequarter-note.tex`. Add a pointer in all three places. Also state that I is that architecture restricted to a
linear-mass one-block family. The current "one-block version of … I3_DEEP_ASTRA Lemma 8.7, not a new BV theorem" is accurate
but insufficient.

**Wording.** "Use odd multipliers k≤K coprime to 210" is redundant, since 210 is even. "Here are the details of the
prime-shift restriction, which prevents importing the unrestricted-word exponent" is opaque; say what is restricted and why.

## 4. Theorem J (lower bound exp(−L^{1+ε})) — sound, with interface citations to add

### 4.1 Step 1: single-block quarantine
* **Square avoidance.** The note derives this via Z57_BFII Cor 2.3 at a large odd square in the class. That is valid, but the
  direct proof is shorter and also covers the 2-adic coordinate. Write G=2^vG′ with G′ odd and G≡−1 (q), q≡3 (4).
  Reciprocity with (q−1)/2 odd gives `(−q/G′)=(G′/q)=(−2^{−v}/q)=−(2/q)^v`. This is −1 whenever v=0 or q≡7 (8). If q≡3 (8)
  and v≥1, then 8|4G and −q≡5 (8) is not a unit square mod 8. Hence no single-block class meets a unit square. (G′>1
  automatically.) Suggest inserting this.
* **Preload.** Random squares at all odd ℓ≤B=L^{1+e}<Y, outside 840, are ordinary a=0 steps. O13 Lemma 3.2(a)'s potential
  `p·2^u` absorbs their drift of at most 2 (the drift is `1+(b|ℓ)` for any class b, not only O13's atoms). Their cost
  θ(B)=O(B) is paid separately. Neutral packets with q≤B die by sign, and q=7 dies because a is a square mod 7. Correct.
* **Moment inputs.**
  * `ΣN_m/m≪L log L`, from `1/(q−1)+O(L/q)` summed over q≤T.
  * `N_{4G}≤ω(G+1)`.
  * The second input dominates O13's Ξ, because `W²τω≤(2β)^{2ω}τ²`. It is uniform in Y, since 2^{ω_Y}≤2^ω.
  * The Hölder exponents 1/(1−t),2/t,2/t sum correctly. `Σ_{m≤4T}V_m^s/m≤(log Y)^{O_s(1)}(log L)^s L^{β^s}=L^{1+o(1)}`
    holds; I re-derived the Euler product.
  * The first input then gives `L^{1+t(C₄−1)/2+o(1)}`. That is ≤L^{1+η} once t≤2η/(C₄−1). Correct.
* **2-adic digits.** Single-block moduli 4G can have free 2-digits above level 3. Their load at ℓ=2 is ≍ the total mass, so
  ℓ=2 *will* be stepped. O13 itself has odd moduli only. The note handles this with "(see z78 §6.2 for moduli divisible by
  4)". That reference does contain the needed sentence: free 2-digits are uniform binary digits, fibre classes ≡1 (8) are
  squares mod every 2^k, and Lemma 3.2(d) applies "to 2 after its 840 digits". It was Opus-reviewed
  (`data/z78/xreview/REVIEW_WILD_ES_OPUS_R2.md`). **Fix:** make the 2-adic step explicit in one sentence and put z78 §6.2 in
  the J label. Today J's label lists only O13 Lemmas 1.1, 3.2, 3.3(B), and the 2-adic extension is not in O13.
* **Late-prime bound.** `η^{−2}(1+L′)L^{C₄}/Y` with Y=L^A and η≍1/log L is o(1) for A>C₄+1. The choice A>C₄+5 is ample.
* **Markov budget.** Expected cost ≤O(B)+(1/η)L^{1+η′}. Expected mass ≤L^{1+η′}. The good-fibre bounds L^{1+2e} hold with
  room. Lemma 1.1 gives void ≥exp(−(4/3)L^{1+2e}). The fibre's unit-Haar mass is φ(840)/φ(Q). The total is
  ≥exp(−L^{1+ε}) because 2e<ε/2. Correct.

### 4.2 Step 2: Shiu and the conditional neutral-block bound — sound
* **Expected cylinder mass.** `E[β^{s_D}P_fibre(D)]≤C·W_{4G}/φ(4G)`. This is the one-event supermartingale, which needs no
  square avoidance for D and covers fully determined D, which then contribute 1. The stopping time is bounded. Correct.
* **Union bound over neutral cylinders.** O13 Lemma 1.1's *general-A* clause gives `P(D|∩F̄)≤β^{|supp D|}P(D)` under (1.1)
  for the single-block family. Then a union bound applies over all neutral cylinders with q>B. This is correct. Dropping the
  sign is an upper bound. Keeping the neutral events *out* of the LLL family avoids load at late coordinates q>Y, which is a
  real reason and not decoration.
* **Submultiplicativity.** w(ab)≤w(a)w(b) for non-coprime a,b holds for each of β^ω, 2^{ω_Y} and v/φ(v). It is also
  multiplicative, which Shiu needs: w(ℓ^j)≤8 and w(n)≪_σ n^σ uniformly in T because β≤2.
* **S_q(r) bound.**
  * First term r^{σ−1}≤r^{−1/2}.
  * Range (r,q²]: ≪q^{2σ−1}.
  * Beyond q²: Shiu with q≤√x gives `(x/(q log x))·(log x)^β(log Y)^{β}`. The 1/log x cancels, so each dyadic block is
    ≪(log Y)/q. Summed over O(L) blocks this is ≪L^{1+o(1)}/q, which is o(1) uniformly for q>B=L^{1+e}.
  * The note's "≪L^{1+o(1)}/q" is right.
* **Product bound.** The r_i are distinct because 3^i<Q for i<k. At most R₀=(486C)² of them are small, each factor is
  ≤C+1, and the rest are <1/243. This gives O(243^{−k})=O(q^{−5}), with fewer than q generators. Hence Σ_{q>B}O(q^{−4})=o(1).
  Correct.
* **Conclusion.** Markov plus step 1 gives a fibre that is good on both counts. The neutral packets then cost a factor ≥1/2.

### 4.3 Scope and wording of J
* **Strength of the bounds.** "exp(−(log T)^{1+o(1)})" is correct, but the bounds are **only** `e^{−cL}` and `e^{−L^{1+ε}}`.
  The heuristic mass is L log L. Whether log(1/(1−d)) is ≍L or ≍L log L is **open**. COVER §0 says "gives its logarithmic
  power, not its leading constant". That understates the gap: not even the order of magnitude ≍ is determined. Rephrase as
  "the power of log T up to L^{o(1)} factors; log(1/(1−d)) ≍ L versus L log L is not decided".
* **Label.** J's label should also name Theorem I (its upper half), z78 §6.2 (the 2-adic and interpolation interface) and
  PNT in APs (Haar ↔ prime density). Z57_BFII Cor 2.3 is needed only if the direct Jacobi lemma above is not inserted.
* **Notation collisions.**
  * η is used for the "o(1)" convention and also for the LLL threshold (3/4)logβ, two sentences apart.
  * e is the small exponent, the ET parameter e in §11 and the factor e in §10's "a=e".
  * L is log T and also Theorem E's cofactor L.
  * B is the preload bound and also §11's B=px.
  * T is the height and also the "upper unipotent" in §10.

  Rename.

## 5. Finite-range versus Haar exponent wording (challenge)

* **What "exponent 1/2" means.** Both §0 Result lines say "finite-range exponent 1/2" without saying of what. Write it out:
  #primes in (N,2N] missing all packets of height ≤exp(c₀√log N) is ≪N exp(−c₁(log N)^{1/2}). As written, a reader can
  take "1/2" as a density exponent in height, which is 1.
* **The structural reason for 1/2.** The note says "no optimality claim" and "unjustified to declare 1/2 an absolute
  ceiling". That is correct. But the campaign has the tool to say much more. The packet universe satisfies
  `EXSET_BEYOND_CRT.md` Thm 2.1 hypothesis (i):
  * single-block classes avoid all squares (§4.1);
  * a neutral CRT class is a non-residue mod q, so it contains no perfect square.

  Its supply exponent is β=1, with a γ=1 log-log, since the mass is ≍L log L. If (iii) is verified, that theorem caps every
  level-λ CRT majorant at log(1/Eν)≪λ^{1/2}(log λ)^{1/2}. The finite-range 1/2 would then be **sharp for the audited CRT
  class** up to a (log log)^{1/2}, exactly the d/(d+1) pattern quoted in `BEYOND_34.md` §16. I recommend one of two things:
  * (a) verify (iii) and upgrade the Assessment to a scoped method ceiling;
  * (b) state explicitly that 1/2=β/(β+1) for supply exponent β=1, as an expectation, not a claim.

  Either way, replace "worse than 3/4" with that explanation (and the K-R-K pointer). Note that the explanation is
  *linear mass*, not the prime-pivot restriction.
* **Haar versus input exponent.** The "density exponent 1 in height … not an exceptional exponent 1 in the input p" sentence
  is good and should stay.

## 6. ES_JUGULAR §10

* **H–J summary.** This is consistent with COVER. Add the K-R-K pointer. The sentence "Choosing after seeing the window is
  not non-CRT when the height is bounded" is correct: a bounded-height adaptive choice is a finite union of CRT events.
* **Expansion check.** The note says "the indicated word" but **no word is indicated**. The entry aNb−a−b is the upper-right
  entry of `T^{−a}L_N T^{−b}`; I computed it. With `T^aL_NT^b` it would be aNb+a+b. Write the word. The congruence remark is
  correct and elementary: `a↦a+jM` preserves the word mod M and shifts the entry by jM(Nb−1).
* **Amicable pair sentence.** The phrase "divisibility by 2^{v₂(b)+2} gives 4|(p+e+b)/(eb)" reads as a consequence, but it
  is an **extra hypothesis**. The arrows alone give only eb|p+e+b. Say "if moreover 2^{v₂(b)+2}|p+e+b, then N:=(p+e+b)/(eb)
  is ≡0 (4) and p=Neb−e−b is a (★) word". The converse (parity forced, gcd|p, coprime on this slice) is correct.
  Rename e and b; they collide with ET's e,b in §11.

## 7. ES_JUGULAR §11 (export block): every bullet checked; quantifiers mostly right

* **Residues.** The Mordell classes are 11², 13², …, 23² mod 840. (2/p)=(−1/p)=1 since p≡1 (8), and (3/p),(5/p),(7/p)=+1 by
  reciprocity. So the least nonresidue is ≥11. Correct.
* **Range.** Salez 10¹⁷; Mihnea–Bogdan 10¹⁸ is flagged as unrefereed per FRONTIER l.49. Fine.
* **Smallest-denominator windows.**
  * gcd(4x−p,px)=1 for x<p.
  * `(my−B)(mz−B)=B²`; D≡−B forces D′≡−B; the exponent box is D/B with |j_l|≤v_l(B).
  * The character/box disjunction is correct, since finite abelian duality separates −1 from a subgroup.
  * The box over B is box(x)·{p^{−1},1,p}, hence the three targets −1,−p,−p^{−1}.
  * All correct, and the stated equivalence ("conversely the smallest denominator lies in this range") is right.
* **ET windows.**
  * Positive A,B,d with 4ABd=p+e (resp. pe+1) and e|A+B give a solution without coprimality. I verified both identities.
  * The bound e≤(p+4)/3 follows from e≤a+b≤ab+1≤(p+e)/4+1. It gives (e,K)=1.
  * **S∩−S=∅ needs one line.** If A≡−B mod e with A|K and B|K separately, that is not literally AB|K. Pass to g=gcd(A,B):
    A/g·B/g divides K and e|(A+B)/g, since (g,e)=1. Add this line; it is what makes |S|≤φ(e)/2 correct.
  * **Z61 Thm 3.** This is stated "for sufficiently large p". In an anatomy of a hypothetical counterexample this threshold is
    unspecified (Burgess plus Linnik–Xylouris with L=5 for large moduli). It does not apply to a hypothetical failure in
    (10¹⁷, p₀). Add "(only beyond an unspecified threshold)".
* **Slices.**
  * U₇⊂U_II⇒ES (`Z68_U7F.md` l.10–11).
  * The list of forced factorizations matches Z68 Lemma 2 line by line, including "for p≡1 (3)", which holds in the Mordell
    classes, and the {1,3}∪{1,5} choice.
  * L₃(p)≠∅ comes from Z63 §1, via bsG_primes_trivial.
  * Equal endpoint characters follow from χ(tu−1)=χ(uv).
  * Correct.
* **Quantifier guard.**
  * The CT summary matches `POINTWISE_SIZE.md` Lemma CT(a–c) exactly, including that only the *product* is controlled in
    Type II.
  * "Vacuous on an empty solution set" is the right caution.
  * "Any exceptional primes lie in the avoider sets of H/I for every height" is correct. Through I it gives #counterexamples
    in (N,2N] ≪N e^{−c√log N}, which is weaker than the ambient 3/4 bound (cite K-R-K).
* **Logical guard.**
  * I verified `5c7cfdc09:notes/z80/IE1_SPLIT.md` §§9–10: P≡1 modulo all of D (hence 1 mod 840), least QNR exactly 2, both
    supplements failing, and cross-lab reviewed (R2/QNR reports).
  * The deduction "2 cannot be the least nonresidue of a standard counterexample" is correct.
  * The model hypotheses listed match §9's.
  * Fine.
* **Export-block hygiene.**
  * The block has no stated destination or triage (FRONTIER §3? §6? none?). As written, about 2 kB of bullets cannot go
    into FRONTIER §6, which allows one line per dead end.
  * Add a "Proposed export:" line with the target section and a compressed one-sentence form.
  * Pin the EXTREME citation in §11 to `62fefacf8`, as §9 already does, and pin the BEYOND_34 citation in COVER.

## 8. §0 blocks

**ES_JUGULAR §0.**
1. **Review line.** It lists A–C, D and §§6–9, but says nothing about §§10–11 or COVER. Until this report is cited, those
   parts are **cross-review owed**. Say so explicitly, then cite this file.
2. **Result line.** It now speaks only of H–J. The R2-mandated D/F and G result has been dropped, although the Label still
   lists D–G. Restore a two-clause Result: D/F/G as before, plus H–J. State the finite-range exponent as in §5.
3. **Label.** The §11 inputs are missing: Mordell, Salez (CERTIFIED, external), CAP_DOWN Lemma 3.1/Thm 1.2, Z61 Thm 3
   (Burgess, Linnik–Xylouris), Z68 Lemma 2, Z63 §1, POINTWISE_SIZE Lemma CT and IE1_SPLIT §§9–10 (internal, pinned). Add
   them, or say "§11: implications rel. the cited internal notes".

**COVER §0.**
1. "Review: none" is correct for now. Update it to cite this report.
2. Label: add z78 §6.2, PNT in APs and Theorem I for J's upper half.
3. Scope: the sentence "The finite-range bound is not a sharp lower tail at a prescribed p" is garbled. Suggested
   replacement: "I is an upper bound on the number of misses, not a statement about any prescribed p, and is not shown
   sharp".
4. Result: specify the counted quantity for "exponent 1/2".

## 9. Falsifier rows (H–J table; §11 F-line)

* **F1.** Correct, and strengthened by §4.1: neutral CRT classes are also square-free classes (a nonsquare mod q). J uses
  square digits only to build avoider fibres.
* **F2.** "131 is not in the prime classes" is correct, but **241 is not in them either** (241≡3 mod 7, a non-residue). The
  sentence suggests 241 is a live test. The large R₈ zero 1590284203561 is ≡361 (840), so it is in the classes; H–J assert
  nothing there. Correct as stated. The 8G remark is correct.
* **F3.** The N_II at composite n remark is correct and matches the earlier reviewed §9 row.
* **F4.** No coverage is claimed at the 14 zeros or at 17401609 (≡169 mod 840). Correct.
* **§11 F-line.** Correct.

## 10. Data and replay hygiene

* `packet-density.txt` has no header. The columns are T, a, d, the neutral-packet count and |𝓔|. Add a header line, or
  describe the columns in the note.
* **CERTIFIED coverage.** The note should record the independent coverage. Today it is the self brute check to T=16 (same
  enumerator). This review adds an independent enumerator with exact period counts at T=16,24 and an empirical check at T=80.
* **Scale calibration.** Optionally add the singles-only versus full comparison (§1), so that readers do not over-read the
  neutral-packet negligibility in J as a finite-T statement.

## 11. Required fixes (for this round to count as cross-reviewed)

1. Cite K-R-K and `paper/es-threequarter-note.tex` at every 3/4 mention: COVER Exponent comparison, ES_JUGULAR §§10, 11.
   Credit I's architecture to K-R-K / 3/4 note / Dahan II §7 (FRONTIER required wording).
2. ES_JUGULAR §0:
   * Review line: §§10–11 and COVER cross-review owed, then this report.
   * Result: restore D/F/G alongside H–J.
   * Label: add the §11 inputs.
3. Both §0 lines: define "finite-range exponent 1/2" as a count of misses in (N,2N]. In COVER, replace "not its leading
   constant" with the L versus L log L openness.
4. J label: add z78 §6.2 (2-adic free digits and interpolation) and Theorem I. Add the one-sentence 2-adic step, or, better,
   the explicit Jacobi square-avoidance lemma (§4.1).
5. §10: write the word `T^{−a}L_NT^{−b}`. Make the 2^{v₂(b)+2} condition an explicit hypothesis.
6. §11: add the gcd line for S∩−S=∅. Qualify Z61's "sufficiently large p" as an unspecified threshold. Add a proposed-export
   line (destination and compressed text). Pin EXTREME/BEYOND_34.
7. Define or remove δ(T), δ_all(T). Fix the notation collisions (E, η, e, L, B, T).
8. F2: note that 241 is also outside the classes.

**Optional.**
* Verify EXSET Thm 2.1(iii) for the packet universe to make 1/2 a scoped CRT-method ceiling, or state 1/2=β/(β+1) as an
  explanation (§5).
* Add a sentence that, conditional on c, hits have ≤1 event per pivot, which is why Caution 8.5 does not bite.
* Add a packet-density header and the coverage note.

## Appendix — independent checks (scripts kept outside the repo)
```
# indep.py: packets from scratch (sympy)
#   singles: q prime 7..T, q≡3 (4), G≤T, q|G+1 -> event 4G|p+q
#   neutral: Q=(q-1)/2, k=min{k:3^k>=Q}, h with n_order(h,q)=Q, g_i≡h^{3^i} (q), Π g_i≤T -> 4G|p+q and legendre(p,q)=-1
#   period mode: P=lcm(840, consistent moduli); count reduced r≡a (840) mod P hit by any packet
#   T=16: P=960960 -> 1/12, 13/24 ;  T=24: P=22102080 -> 7/40, 13/24  (all six classes, matching the script)
#   empirical mode: primes 1e4<p<1e8 per class at T=80 -> within 2.4σ of exact
# sq.py: for q<120, G<1500, G≡-1 (q): (-q mod 4G) ∉ {s² mod 4G : s odd}  -> 738 classes, 0 failures
# singles.py: repo z80_packet_density.density with atoms() restricted to single blocks, T=16,32,48,80
```
