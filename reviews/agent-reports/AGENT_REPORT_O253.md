# AGENT REPORT O253 — Direction 2: amplifying one exception (Claude side)

Main file: `AMPLIFY_EXCEPTION.md`. Memos: `BRAINSTORM/z25_{reduction_form,t1_adversary,numerator_models,square_law,thresholds}.md`.
Scripts: `scripts/z25_{common,square_patterns,mixed_check,models,gate,joint_run,sqadv}.py`; log `logs/z25_gate_mordell.txt`.
**ES is not solved. No propagation law sufficing for ES was found.** Outcome: sharp "would suffice" thresholds and
obstruction theorems with exact scope.

## SHARP:
1. **T1 adversary / invisible witnesses (Thm 3.2, Cor 3.3, PROVED).** If p ≡ □ (mod L) then p has no ET witness with
   modulus dividing L (proof repaired after self-review: ET normalisation at the square via a CRT choice of m).
   (R266 repair: Thm 3.2 is classical in substance — the Mordell–Schinzel square-class obstruction, ET Prop 1.6 and
   ET p. 8, campaign T1 / DISCOVERIES (C)2, (C)7; what is new here is its application to recombination laws and
   the locality remark of Cor 3.3, folklore-level.)
   So a source witness whose modulus sees only residues of p that are squares is useless to any
   congruence-mediated ("determined") lift, and since squareness mod L is local, the lcm of invisible moduli is
   invisible: **joint recombination over ANY finite set of sources that must accept every supplied witness tuple
   is total only if one single source has no invisible witness** (necessary, not sufficient; joint lifts do beat
   single ones on visible inputs, e.g. p = 17: moduli 8, 12 fail, lcm 24 passes). Favourable-witness existence
   proofs are not covered. For p ∈ 𝓜, every {2,3,5,7}-smooth input modulus is invisible.
   Dictionary: *the only usable information about p is its residues at non-residue primes of p* — matching the
   (J)64 mechanism, which starts from a prime window with (q/n) = −1. Certified at all fixtures ≤ 5209: every
   source has ≥ 2 invisible witnesses, and adversarial tuples exist.
2. **Numerator models give a real test-bed of exceptions (Thm 2.5, CERTIFIED).** k/n with 8 ≤ k ≤ 25 has genuine
   prime exceptions (k = 8: 2, 3, 11, 17, 131, 241 below 2000); every k-uniform law shape tested (square law,
   *truncated* (p²−1)/4 recombination (factors q > k only; the untruncated analogue is vacuous since 2 ∈ E_k),
   {(p∓1)/2} recombination, forced successor in (p, 8p]) is false there.
3. **No free lunch for route D (Thm 2.4).** The {(p−1)/2, (p+1)/2} recombination law *is* ES on p ≡ 9 (mod 16)
   (half of the Mordell-class primes), because there both inputs are already known to be soluble.

## What was done
* §1 Deliverable 1: Thm 1.1 (exact counting criterion for an unspecified Vaughan constant; strictly stronger than
  Σ1/p divergence), Rem 1.2 (landing), Thm 1.3 (branching: polylog ceiling for fixed b and super-linear scale;
  exact threshold b ≥ rA at linear scale; additive gap threshold f = exp(o((log p)^{2/3}))), Thm 1.4 (composites),
  Thm 1.5 (blocks/hitting sets; route D).
* §2 obstructions: Prop 2.1 (an (A)-law is a family of total reductions; with growth it must pass through
  Vaughan-covered small-modulus witnesses), Thm 2.2 (slice isolation: witness transports never amplify),
  Thm 2.3 (primality-blind ET-valued proofs refuted at a verified odd square, e.g. n = 121 ∈ 𝓜), Thm 2.4, Thm 2.5.
* §3 constructions: affine-source recombination with exact gate (Thm 3.1: determined lift exists iff p has an ET
  witness with H | αH′ — the B2 gate); fixtures; 49 Mordell primes < 10^5 with (p+1)/2 prime: total at 0 of 49;
  T1 adversary (Thm 3.2/Cor 3.3); square law (Prop 3.4: only mixed (≥2,1,0) solutions matter; they are divisor events
  of (p² + m)/4; m = 3 killed by reciprocity; false for k = 8); progression law into the relaxation E_X (Prop 3.5)
  and why it cannot be upgraded.

## Sparks (not pursued)
* Sources q forced to share p's non-residue primes (e.g. (q/ℓ) = (p/ℓ) for all ℓ ≤ B) make q's own T1 constraint
  visible to p — visibility is necessary for any lift; is there a family where it is also sufficient?
* "Mordell theorem for p²": which m ≡ 3 (4) are dead for mixed solutions of 4/p² when p ∈ 𝓜 (m = 3 is).
* Compute E_k for k = 8, 12 to 10^5: are numerator-model exceptions finite (CONJECTURE)? A proof for one k would be
  an ES-type theorem in a model with exceptions, i.e. a model of "least exception" behaviour.
* Non-congruential lifts (using sizes x, y, z, d of the input witness, not only residues) are the only escape from
  Cor 3.3; none was found.

## R1–R8

| Row | Content |
|---|---|
| R1. Deliverable 1 | Thm 1.1: F ⊆ E contradicts Vaughan iff ∀c > 0: limsup F(N)·exp(c(log N)^{2/3})/N = ∞ (R266: the "only if" is relative to Vaughan's unspecified c₀ and to counting alone) (sufficient: F(N) ≥ N e^{−o((log N)^{2/3})} along a sequence; 3/4 with the internal bound); strictly stronger than Σ_F 1/n = ∞. Thm 1.3 (prime successors; core v1.1 (ii)): fixed b with successors ≥ p^{μ}, μ > 1 ⟹ T(N) ≤ (K+1)b^K + 1, K = log(log N/log p₀)/log μ (polylog; log log N for b = 1), never suffices when all outputs stay among primes of 𝓜 (σ-closed prime model consistent with K1–K4′; = Astra RESET §4 test 3); growing branching ≤ p^{δ} with successors ≥ p^{μ} ⟹ T(N) ≤ (K+2)N^{δ/(μ−1)}, so δ ≥ μ − 1 is necessary; slowly growing successors: b > r successors in (p, Ap], in-degree ≤ r, suffices iff b ≥ rA; one forced successor in (p, p + f(p)] suffices if f = e^{o((log p)^{2/3})} along a sequence; for f ≥ e^{c(log p)^{2/3}} no counting contradiction (no model constructed) (R266 repair). Thm 1.4 composites (full weight; one seed ⟹ powers of p₀ or new exceptional primes; log loss converting; composite outputs must be rewritten as prime laws before Thm 1.3 applies). Thm 1.5 blocks (hitting-set ≥ #blocks/μ_N; route D = least element). Label PROVED. Location AMPLIFY_EXCEPTION.md §1. |
| R2. Best law | (i) Total, all p₀, both Types, but into a relaxation: Prop 3.5, p₀ ∈ E ⟹ {n ≡ p₀ or n p₀ ≡ 1 (mod M_X)} ⊆ E_X (no ET witness with H ≤ X). PROVED, folklore-level, total — but by core §5 a classical congruence progression, i.e. NOT SUCCESS (R266 repair). (ii) E-valued: only divisor closure (trivial, downward). (iii) Affine-source recombination W(n′) ⟹ W(p) via determined lifts with exact gate (Thm 3.1): NOT total (0/49 Mordell primes < 10^5, 0 fixtures). No new total E-valued law. |
| R3. Growth vs R1 | (i) has ≥ N/M_X elements (far beyond (1.1)) but in E_X ⊋ E; upgrading to E on a positive proportion is equivalent to ES(p₀) (Vaughan). (ii) zero growth from a prime seed. (iii) not total, so no growth. Distance: infinite in the sense that no E-valued law with any growth beyond {p₀} is proved. |
| R4. Obstruction | Cor 3.3 (PROVED): a congruence-mediated (determined-lift) recombination over any finite source set Q(p), any shifts, that must accept every supplied tuple of source witnesses, is total only if some single source has no witness whose modulus L satisfies p ≡ □ (mod L); for p ∈ 𝓜 (and α ∣ 2^a3^b5^c7^d) every {2,3,5,7}-smooth modulus is such. Not covered: proofs that a favourable witness exists, non-congruential lifts. Thm 3.2 (PROVED; classical in substance: Mordell–Schinzel / ET Prop 1.6, campaign T1): p ≡ □ (mod L) ⟹ no ET witness of p with H ∣ L. Thm 2.3: a primality-blind ET-valued proof is refuted at a verified odd square (n = 121 for the (n²−1)/4 scheme). Thm 2.2: fixed-(a,b,c) transports isolate exceptional primes. Thm 1.3(a),(d): bounded branching with successors ≥ p^{μ}, μ > 1, never suffices; branching ≤ p^{δ}, δ < μ − 1, never suffices by counting. Thm 2.4: {(p∓1)/2} recombination equals ES on p ≡ 9 (16). |
| R5. Fixtures | Determined-lift recombination (sources (p+j)/g prime, abs(j) ≤ 12, g ∣ 24), passing/all source witnesses: **97** 89:5/10, 103:14/27, 43(×2):3/14, none total, joint adversary exists (lcm 2^6·3^2); **193** 199:31/42, 97(×2):5/8, 61(×3):1/11, none total; **313** 79(×4):20/37, 151(×2):9/31, 13(×24):1/4, none of 11 total; **3361** 281(×12): **0/17**, 3359:25/423, none total; **5209** 2609(×2):10/40, none total; **233689** 116849(×2):34/167, 77899(×3):85/225, none total (joint search not run at 233689). Invisible witnesses (Thm 3.2) at every source of every fixture ≤ 5209 (e.g. 3361←281: 11/17 invisible). Contrapositive tests "q ∈ S ⟹ p₀ ∈ S with explicit witness": the passing source witnesses give explicit p₀-witnesses (same slice, d = quotient); no source is total. Mordell primes < 10^5 with (p+1)/2 prime: 0/49 total (other Mordell-class primes ≤ 10^5 not tested — R266). Odd-square control: Thm 3.2's lemma checked on all fixture ET moduli; n = 121 refutes the primality-blind (n²−1)/4 scheme. |
| R6. Key ideas / abandoned | **T1 adversary**: information about p usable by any congruence-mediated lift lives only at prime powers where p is a non-square; locality means invisible inputs cannot be rescued by combining sources (joint lifts still help on visible inputs). **Reduction form**: (A)-law = total reductions; with enough growth they must pass through Vaughan-covered small-modulus witnesses, which the T1 adversary then makes invisible when smooth. **Numerator models**: k/n gives real exceptions; all k-uniform laws tested fail; exceptions isolated. Abandoned: square law (mixed solutions are a new B2 lottery; false at k = 8); progression upgrade (equivalent to ES(p₀)); witness-dependent transports (tautological F = E); {(p∓1)/2} route D (ES on p ≡ 9 (16)); multi-shift disjunction (Cor 3.3). |
| R7. Distance / next step | ES is not closer. Every amplification/recombination attempt is a total reduction ES(q) ⟹ ES(p), and every congruence-mediated reduction that must accept every supplied source witness is blocked by the T1 adversary (favourable-witness proofs not covered); non-congruential reductions must manufacture a divisor event at p (B2). Numerator models suggest exceptions are isolated, so a sufficing (A)-law would be a 4-specific dichotomy theorem (E = ∅ or E dense at its own scale) with no analogue in any model. Most promising next step: look for *non-congruential* lifts that read sizes (d, x, y, z) of input witnesses at sources forced to share p's non-residue primes, and test them first in the k = 8, 12 models, where a true law must fail. |
| R8. Resources | One session, ≈ 0.9 h wall-clock (17:22–18:15 incl. repairs); ≈ 1 CPU-hour (≤ 2 cores, ulimit 8 GB). Reviews: one self-requested hostile review (deep mode, GPT reviewer): no FATAL; 10 MAJOR + 3 MINOR, all repaired in commits after 187b3a2 (prime-successor scope and boundary cases of Thm 1.3, Prop 2.1(b) downgraded to Assessment, Thm 2.3 scope and n = 121, Thm 2.5 populations and truncated-law distinction, Thm 3.1 prime-member transfer, Thm 3.2 proof with ET normalisation and α caveat, Cor 3.3 scope, Prop 3.4(b) p ∤ m, g = 24 rerun, 97 lcm). Independent hostile review R266 (`reviews/amplify-exception-review.md`): no FATAL; all numerics reproduced from scratch; MAJOR: Thm 3.2 attribution (classical Mordell–Schinzel/T1), missing Astra prior-art credit, R-table oversell; minors; all repaired by the reviewer, marked (R266 repair). |
