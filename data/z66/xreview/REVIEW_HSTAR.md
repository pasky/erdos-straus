# z66 HSTAR — hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** The centraliser obstruction, stated polynomial lemma and scoped prime-to-p transparency survive independent derivation. “NARROWED; no engine; no HOT LEAD” is justified. Do not promote the broader exclusions or the erroneous Wewers sentence.
Reviewed `side-agent/z66-hstar` at `c84e6fa684930ec85f29e53dbbba0ea1704a03c8`, `Z66_HSTAR.md`, its scripts/data, and the cited repository lemmas. No provider errors encountered. ES remains OPEN.

## Claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| §1 realisation scheme; Remark 1.1; Nec(v) | CORRECT | A map into an empty certificate set forces an empty domain. This applies to (★), Type II and S∃, **not ES**. The engine must be inapplicable at squares, possibly because its characteristic/degree hypothesis is only defined for primes. |
| Definition as progress toward H★ | CORRECT-WITH-FIX | It is a semantic framework, not a non-circularity criterion: `D(n)=n, Real(n)=Cert(n), ε=id` qualifies. No effective extraction or complexity bound is required. Distinguish this tautological scheme from an independently proved engine; the memo generally does. |
| Ord and Ord_k | CORRECT | If maximal p-valuation B≥2 occurs once, valuations contradict the sum; if three times, the sum is too small; if twice, `p/k<a≤p²/(kp−2)<(p+1)/k`, impossible. Then exactly one or two denominators contain p. The one-denominator case forces `p | kx′−1`, hence x′>1; two quotients both 1 would require `z=p/(k−2)`. The hypotheses p>k≥4 suffice. |
| Corollary Ord, centraliser list | CORRECT | Z64_EQUIV Lemma A gives three inertia orders at p≡1 (4). An inertia element of order pk has a commuting nontrivial prime-to-p part. A p-cycle has centraliser C_p in S_p; subgroups inherit the restriction. Unipotents in PSL₂(F_p), and p-elements in the listed Frobenius groups, also have p-group centralisers. This excludes ES pairs **on those groups**, not arbitrary extraction from their covers. |
| Theorem T | CORRECT | Checked Obus 1703.01191, Thm 1.5 and Rem 1.9 directly: fixed disjoint branch sections give unique tame lifting; the prime-to-p fundamental-group quotients are isomorphic. Surjections onto G, p∤|G|, correspond. Ramification orders, subgroup/block structure and intermediate genera are preserved. This is not a ban on new proofs of existence in characteristic p. |
| DD | CORRECT-WITH-FIX | A constant extraction is a witness rule; computability/totality are explicit for the Π⁰₁ assertion; also assume decidable class membership and certificate checking. It need not be an input-supplied certificate or a trivial rule. Carry the square-obstructed target and polynomial-identity hypotheses into the final bullet; T1 alone says nothing about ES certificates at squares. |
| Aff | CORRECT-WITH-FIX | Transitivity forces the translation subgroup C_p; an S_p-conjugator therefore normalises it. Two nontranslations with different fixed points, a translation plus a nontranslation, and all translations give the stated normal forms, the last with p−2 classes. Specify labelled nonidentity branch cycles, reordering where needed, and all a_i≠1 in the “no translation” case. Normalising the second fixed point to 1 initially gives b₂=1−a₂; a further scaling gives the displayed b₂=1. |
| N; CPZ-T1; general-C norm proof | CORRECT | Petronio Thms 3.13/3.14 explicitly allow integer coordinates, hence (m,0); the Eisenstein degree condition excludes 3|m. For C=1, a divisor 3 mod 4 is equivalent to a 3 mod 4 prime factor, not to failure of unrestricted two-square representability. The n=11 counterexample correctly prevents the false converse. For general C, every prime factor of 4Cm²+1 has χ_{−4C}=1, whereas −1 mod 4C has character −1. |
| 2V, as formally stated | CORRECT | Positivity on the full lattice coset makes leading forms nonnegative and nonconstant degrees even. Degree equality is α+β+γ+δ=max(α,β,γ+2). An α/β maximum leaves three constants; otherwise α+β+δ=2. The d-quadratic case makes c constant; the a-quadratic case gives `4bd·a₁c=p/(4bd)+a₁+b`, forcing a₁ constant (irreducible quadratic leading form). All outputs are affine in p. |
| 2V as exclusion of every polynomial/arithmetic extraction; D2 | CORRECT-WITH-FIX | Carry the **identity and full-coset positivity/integrality** assumptions into summaries. Non-polynomial functions of (x,y) are still extraction maps under §1; calling them “not a realisation step” does not eliminate them. D2 with general ε is unresolved, just as D7 with general ε is. |
| Pos | CORRECT | (1,−n−1,0) solves the unrestricted equation; the positivity restriction is essential. No implication against geometrically positive extraction follows. |
| K-block; one-element lemma | CORRECT | At prime degree every transitive realisation is primitive and N=4Cn+1 has no required divisor. The general existence assertion is explicitly conditional on SWZ. Wang et al. verify all compatible triples through degree 31; N=29 is a valid domain example. The dihedral N=37 square example is unconditional. The fixed point's block is a union of full L-cycles plus that point, hence size 1 mod L. Block-equipped schemes are not excluded. |
| Split and proper (★) sub-family | CORRECT-WITH-FIX | For a triangle C_p×K-cover, the C_p projections must have exactly two nonzero entries; after scaling these are ±1. Coprime orders give the displayed K-signature and converse generation. State p≥5 and the triangle hypothesis explicitly, or supply the short Riemann–Hurwitz exclusion of other signatures. The p=409 C₂₃₄ example checks: orders (117,234,2), reciprocal equation 4. |
| Nec(i)–(iv); homology cover | CORRECT | These follow in their stated settings. The characteristic subgroup of the surface group is normal in the orbifold group; the unramified cover multiplies both |G| and 2g−2 by p^(2g). At p=5, degree 625 gives genus 626 and group order 6250. |
| §6 “Wewers lifting reaches the cyclic Lemma-F covers” | WRONG | Z65_LIFT Prop E states the opposite: their marked reduction is exceptional, with σ=1 at the unique tame point, and they are **not** lifts of special G-maps. Delete this sentence; retain Prop O only within its actual hypotheses. |
| “No lifting theory … covers” noncyclic p-Sylows | GAP | Being outside the particular Raynaud–Wewers–Obus results invoked here does not prove absence of every lifting theorem. Replace by “the cited special-map/cyclic-Sylow results do not apply.” |
| D3 genus-zero invariant; catalogue; KT2 | CORRECT-WITH-FIX | Fried Cor 2.3 directly gives the data-determined spin sign; Thm 1.3 concerns 3-cycle Nielsen classes with r≥n≥5, not arbitrary odd inertia. DD makes this a witness rule, not automatically type I. Unresolved higher-genus/general-extraction rows are honest. Neither KT2 nor the catalogue proves all possible engines dead. |

## Reproduction and certification

All commands used `ulimit -v 4000000` and `timeout` ≤1800 seconds. No lane files were modified.
- `z66_hstar_ord_check.py 3000`: **211 primes, 8,334 representations, zero missing pk entries, zero p² entries**, exact agreement. The imported Z65 enumerator was also inspected.
- Compiled the census with `gcc -O2 -Wall -Wextra`; N=4,5,6,7,8 outputs are **byte-identical** to the committed data. Counts (R,I,E): (7,3,1), (17,0,0), (57,15,6), (141,0,0), (428,41,14).
- Independent `scripts/z66_xrev_hstar_checks.py` enumerates permutations and **all candidate block subsets**, not the lane's pair-closure algorithm: every row, genus, primitive flag and block-size set agrees at N=4,5,6 (8,17,63 compatible data). The elementary census logic is sound for realisability/primitivity; N=9,10 were not rerun in this review.
- Source checks: https://arxiv.org/pdf/1703.01191 (Thm 1.5, Rem 1.9); https://www.numdam.org/item/10.5802/wbln.34.pdf (Thms 3.13/3.14); https://arxiv.org/pdf/2512.06545 (abstract/introduction, degree≤31); https://arxiv.org/pdf/math/0611591 (Thm 1.3, Cor 2.3). The norm-family criterion is checked directly in Petronio rather than inferred from a literature-note flag.

## Mandatory falsifiers

| Screen | Audit |
|---|---|
| F1 odd squares | Correct for the three square-obstructed targets. Semantic soundness is not an engine; prime-only applicability is not a new extraction. The admissible-square qualification in N is necessary and present. |
| F2 12 R₈-zeros | Correctly **not passed as a new route**: Ord_k applies to 8/p for p>8, and the other stated barriers are numerator-blind. No false claim that an R₈-zero is a full Type II or ES zero. |
| F3 285 composite (★)-zeros | The degree's imprimitivity is a different condition from a certificate divisor in the required residue class. Treat “no special Hurwitz meaning” as an assessment, not a proved universal negative. The dihedral counterexamples support only the scoped naked-block exclusion. |
| F4 14 (★)-zeros, 38 𝔊*-zeros | The centraliser/bad-reduction conclusions are correctly scoped; no engine is claimed at these primes. A (★)-zero certainly fails its C=1 line, so the one-way CPZ statement applies. Do not infer the same for every 𝔊*-zero. |

## Required fixes, priority order

1. Remove the false cyclic-Wewers reachability claim; limit all “no lifting theory” language to the results actually invoked.
2. Keep D2/general non-polynomial extraction unresolved; propagate the exact 2V hypotheses and the “sets, not proofs” scope of T to the bottom line/FRONTIER proposal.
3. Keep DD's target restrictions; do not equate data-determined output with a supplied certificate. Clarify Aff's cases and Split's triangle/p≥5 hypotheses.
4. Describe the scheme definition as semantic and the broad catalogue judgments as assessments; the justified verdict remains **NARROWED**, not closure.
