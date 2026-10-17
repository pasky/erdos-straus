# AGENT REPORT O253 — Direction 2: amplifying one exception (Claude side)

Main file: `AMPLIFY_EXCEPTION.md`. Memos: `BRAINSTORM/z25_{reduction_form,t1_adversary,numerator_models,square_law,thresholds}.md`.
Scripts: `scripts/z25_{common,square_patterns,mixed_check,models,gate,joint_run,sqadv}.py`; log `logs/z25_gate_mordell.txt`.
**ES is not solved. No propagation law sufficing for ES was found.** Outcome: sharp "would suffice" thresholds and
obstruction theorems with exact scope.

## SHARP:
1. **T1 adversary / invisible witnesses (Thm 3.2, Cor 3.3, PROVED).** If p ≡ □ (mod L) then p has no ET witness with
   modulus dividing L. So a source witness whose modulus sees only residues of p that are squares is useless to any
   congruence-mediated ("determined") lift, and since squareness mod L is local, the lcm of invisible moduli is
   invisible: **joint recombination over ANY finite set of sources (all shifts, all witnesses at once) is total
   only if one single source has no invisible witness.** For p ∈ 𝓜, every {2,3,5,7}-smooth input modulus is invisible.
   Dictionary: *the only usable information about p is its residues at non-residue primes of p* — matching the
   (J)64 mechanism, which starts from a prime window with (q/n) = −1. Certified at all fixtures ≤ 5209: every
   source has ≥ 2 invisible witnesses, and adversarial tuples exist.
2. **Numerator models give a real test-bed of exceptions (Thm 2.5, CERTIFIED).** k/n with 8 ≤ k ≤ 25 has genuine
   prime exceptions (k = 8: 11, 17, 131, 241); every k-uniform law shape tested (square law, (p²−1)/4 recombination,
   {(p∓1)/2} recombination, forced successor in (p, 8p]) is false there, and exceptions look isolated.
3. **No free lunch for route D (Thm 2.4).** The {(p−1)/2, (p+1)/2} recombination law *is* ES on p ≡ 9 (mod 16)
   (half of the Mordell-class primes), because there both inputs are already known to be soluble.

## What was done
* §1 Deliverable 1: Thm 1.1 (exact counting criterion for an unspecified Vaughan constant; strictly stronger than
  Σ1/p divergence), Rem 1.2 (landing), Thm 1.3 (branching: polylog ceiling for fixed b and super-linear scale;
  exact threshold b ≥ rA at linear scale; additive gap threshold f = exp(o((log p)^{2/3}))), Thm 1.4 (composites),
  Thm 1.5 (blocks/hitting sets; route D).
* §2 obstructions: Prop 2.1 (an (A)-law is a family of total reductions; with growth it must pass through
  Vaughan-covered small-modulus witnesses), Thm 2.2 (slice isolation: witness transports never amplify),
  Thm 2.3 (primality-blind ET-valued laws refuted by odd squares), Thm 2.4, Thm 2.5.
* §3 constructions: affine-source recombination with exact gate (Thm 3.1: determined lift exists iff p has an ET
  witness with H | αH′ — the B2 gate); fixtures; 49 Mordell primes < 10^5 with (p+1)/2 prime: total at 0 of 49;
  T1 adversary (Thm 3.2/Cor 3.3); square law (Prop 3.4: only mixed (2,1,0) solutions matter; they are divisor events
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
| R1. Deliverable 1 | Thm 1.1: F ⊆ E contradicts Vaughan iff ∀c > 0: limsup F(N)·exp(c(log N)^{2/3})/N = ∞ (sufficient: F(N) ≥ N e^{−o((log N)^{2/3})} along a sequence; 3/4 with internal bound); strictly stronger than Σ_F 1/n = ∞. Thm 1.3: fixed branching b with outputs ≥ p^{λ₁}, λ₁ > 1 ⟹ T(N) ≤ 2(log N/log p₀)^{log b/log λ₁}, never suffices (σ-closed prime model consistent with K1–K4′); b successors in (p, Ap] with in-degree ≤ r suffices iff b ≥ rA; one forced successor in (p, p + f(p)] suffices iff f = e^{o((log p)^{2/3})} along a sequence. Thm 1.4 composites (full weight; one seed ⟹ powers of p₀ or new exceptional primes; log loss converting). Thm 1.5 blocks (hitting-set ≥ #blocks/μ; route D = least element). Label PROVED. Location AMPLIFY_EXCEPTION.md §1. |
| R2. Best law | (i) Total, all p₀, both Types, but into a relaxation: Prop 3.5, p₀ ∈ E ⟹ {n ≡ p₀ or n p₀ ≡ 1 (mod M_X)} ⊆ E_X (no ET witness with H ≤ X). PROVED, folklore-level, total. (ii) E-valued: only divisor closure (trivial, downward). (iii) Affine-source recombination W(n′) ⟹ W(p) via determined lifts with exact gate (Thm 3.1): NOT total (0/49 Mordell primes < 10^5, 0 fixtures). No new total E-valued law. |
| R3. Growth vs R1 | (i) has ≥ N/M_X elements (far beyond (1.1)) but in E_X ⊋ E; upgrading to E on a positive proportion is equivalent to ES(p₀) (Vaughan). (ii) zero growth from a prime seed. (iii) not total, so no growth. Distance: infinite in the sense that no E-valued law with any growth beyond {p₀} is proved. |
| R4. Obstruction | Cor 3.3 (PROVED): every congruence-mediated (determined-lift) recombination over any finite source set Q(p), any number of shifts, all witnesses jointly, is total only if some single source has no witness whose modulus L satisfies p ≡ □ (mod L); for p ∈ 𝓜 every {2,3,5,7}-smooth modulus is such. Thm 2.3: every ET-valued law whose proof does not use primality is refuted by odd squares. Thm 2.2: fixed-(a,b,c) transports isolate exceptional primes (never amplify). Thm 1.3(a): bounded branching with super-linear growth never suffices. Thm 2.4: {(p∓1)/2} recombination equals ES on p ≡ 9 (16). |
| R5. Fixtures | Determined-lift recombination (sources (p+j)/g prime, abs(j) ≤ 12, g ∣ 24), passing/all source witnesses: **97** 89:5/10, 103:14/27, 43(×2):3/14, none total, joint adversary exists; **193** 199:31/42, 97(×2):5/8, 61(×3):1/11, not total; **313** 79(×4):20/37, 151(×2):9/31, not total; **3361** 281(×12): **0/17**, 3359:25/423, not total; **5209** 2609(×2):10/40, not total; **233689** 116849(×2):34/167, 77899(×3):85/225, not total. Invisible witnesses (Thm 3.2) at every source of every fixture ≤ 5209 (e.g. 3361←281: 11/17 invisible). Contrapositive tests "q ∈ S ⟹ p₀ ∈ S with explicit witness": produced only for the passing witnesses (script gives the slice); no source is total. Mordell primes < 10^5 with (p+1)/2 prime: 0/49 total. Odd squares: the lemma of Thm 3.2 is ET Prop 1.6; n = 25 refutes the (p²−1)/4 law in primality-blind form. |
| R6. Key ideas / abandoned | **T1 adversary**: information about p usable by any congruence-mediated lift lives only at prime powers where p is a non-square; locality makes joint recombination no better than its best single source. **Reduction form**: (A)-law = total reductions; with enough growth they must pass through Vaughan-covered small-modulus witnesses, which the T1 adversary then makes invisible when smooth. **Numerator models**: k/n gives real exceptions; all k-uniform laws tested fail; exceptions isolated. Abandoned: square law (mixed solutions are a new B2 lottery; false at k = 8); progression upgrade (equivalent to ES(p₀)); witness-dependent transports (tautological F = E); {(p∓1)/2} route D (ES on p ≡ 9 (16)); multi-shift disjunction (Cor 3.3). |
| R7. Distance / next step | ES is not closer. Every amplification/recombination attempt is a total reduction ES(q) ⟹ ES(p), and every congruence-mediated reduction is blocked by the T1 adversary; non-congruential reductions must manufacture a divisor event at p (B2). Numerator models suggest exceptions are isolated, so a sufficing (A)-law would be a 4-specific dichotomy theorem (E = ∅ or E dense at its own scale) with no analogue in any model. Most promising next step: look for *non-congruential* lifts that read sizes (d, x, y, z) of input witnesses at sources forced to share p's non-residue primes, and test them first in the k = 8, 12 models, where a true law must fail. |
| R8. Resources | One session, ≈ 0.6 h wall-clock (17:22–17:55); ≈ 0.7 CPU-hour (≤ 2 cores, ulimit 8 GB). Reviews: none yet (awaiting parent's hostile review). |
