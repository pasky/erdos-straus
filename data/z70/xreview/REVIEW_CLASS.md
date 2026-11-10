# Z70 CLASS hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN.** Accept the scoped lemmas and descriptive computations, not an exhaustive identification of I17 or a no-go theorem.
Reviewed `side-agent/z70-class` at `29abb44c2d7ff7fa587eedce46b3b2a8a121eceb`.
No provider/auth/quota error occurred. All review computations used ≤2 processes, `ulimit -v 6000000`, command timeouts ≤1200 s.
Independent audit: `scripts/z70_xrev_class_check.py` (run from an archived lane tree with `uv run --with sympy --with numpy --with cypari2 python PATH mode`).

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| §1.1 ideal identity and G = T + X, unrestricted n,d | **WRONG as stated; repairable scope** | At n=105,d=3,(a,b,c,e)=(3,3,2,3), A=71: the ideal identity fails; E=[3,36,213] and T=[3,0,105] are nonprimitive. Require gcd(n,d)=1 before using these classes. |
| §1.1 every e-ideal factors into split prime ideals | **WRONG for composites** | n=33,d=1,(3,3,2,3) has E=(3,√−33), a ramified invertible ideal. At n=315,d=1,(9,9,2,9), E is primitive/invertible but its norm meets the conductor. Require gcd(e,2dn)=1 for the stated split-factor dictionary. |
| §1.1 equivalent e-ideal membership test | **CORRECT** | With its explicit gcd(e,2dn)=1, ab=(n+e)/(4d), a≡ρ/(2d) and ρ²≡−dn imply b≡−a mod e; converse immediate. 1,019 independently enumerated root tests pass. |
| Lemma Φ; DL, CS, FIB | **CORRECT with stated §1.6 hypotheses** | gcd(n,d)=gcd(a,n)=1 makes N_a prime to 2dn; the one-sided ideal factorisation proves multiplicativity even for noncoprime factors. The displayed reading of G for composites must specify the coprime-fibre subset or treat omitted fibres separately. |
| Lemma DL′ | **CORRECT** | Expansion gives AB=4c²dn+1; conversely a+b=c(4abd−n)>0 gives integral e. The coprime-factor move proved in the text has compatible roots a′≡a mod A. No existence theorem follows. |
| SR and RF | **CORRECT, scoped** | min(A,B,de)²≤d(2n+e); reduced-form detection needs an A-side representative and the shear of the third coefficient. SR is not a genericity theorem; the corrected RF coverage is not 97%. |
| FR, FR′, Corollary J | **CORRECT** | Integral invertible ideals and the strict norm-product bound are essential. Primitivity repairs injectivity; this is a proved result, not an empirical assumption. J follows from the impossible norm 2×odd×odd=x². |
| Remark V; Proposition NG | **CORRECT only as scoped** | Multi-affinity excludes coordinate-wise quadratic root swaps, not simultaneous/nonlinear fixed-n moves. NG restates the tied divisor condition; it does not rule out a constructive forcing argument. |
| Corrected FIX-CS/FIX-ALL implementation | **CORRECT in audited sample** | Both d=1 F1 files reproduce byte-for-byte. Independent PARI arithmetic checks 450 replicates, 5,100 imposed fibre equations, 1,710 CS relations including 90 self-loops, genus preservation and every reported statistic. |
| “Calibrated” disappearance of positive residual | **CORRECT-WITH-FIX** | These are reproducible model contrasts, not a validated exchangeable randomisation law. FIX-ALL d=1 pooled control fails; absence of positive excess cannot certify an exhaustive arithmetic explanation. |
| Negative departures unresolved | **CORRECT / honestly reported** | Re-pooling gives FIX-ALL d=1 L1=−4.605, L3=−6.216, C0=−6.206; ALLS L1=−3.069, L3=−3.887. Partial protection and the confounded diagnostics are explicitly acknowledged. |
| 216/218 L1 overlaps are identities | **CERTIFIED reproduction agrees** | d=1 [4,000,000,4,003,000): 132 EID + 84 REP-ID + 2 OTHER; 1,486/1,510 classes have a small natural representative. This count is not attribution of the null excess. |
| Item 2a least-split-prime signal | **CONDITIONAL (GRH) / EVIDENCE agrees** | Recomputed saved-table z=−14.499/−13.044; reran the genus-stratified order calculations, reproducing the displayed means. Cyclic 2-Sylow reasoning is valid for the stated prime discriminants, not arbitrary −4dp or −4yp. |
| Item 2b/2c orders versus decoys | **CONDITIONAL (GRH) / EVIDENCE agrees** | All 66,474 witness rows and 132,948 decoys satisfy identities, roots, ±5% window, mod 8, coprimality and character matching; 288 sampled orders independently recomputed. Re-clustered maximum |z|=1.79455. |
| “Generic” witness classes / orders “match” decoys | **CORRECT-WITH-FIX** | Matching design is sound for the registered conditional comparison, but non-rejection is not equivalence. SR/FR do not imply probabilistic genericity; selective decoy failures and norm/discriminant/witness caps limit coverage. |

## Algebra re-derivation and scope counterexample

Put s=√−dn, β=2ad+s, Ae=N_a. When gcd(n,d)=1, gcd(d,Ae)=1 and 𝔡²=(d).
Then 𝔄𝔈=(Ae,β) (one-sided split factors under the Φ hypotheses), and 𝔡(𝔄𝔈)=(β): both containment and norm dAe=N(β) hold.
Thus [𝔄]=T_d−[𝔈]; swapping a,b conjugates E, so G=T_d+X with X inversion-closed.
For composite coprime-d solutions outside Φ, the class identity can still hold, but the split-prime factorisation argument does not automatically extend.
Independent integer-lattice HNF multiplication and PARI composition verify 94 admissible solutions, including n=409,21841 at d=1,2,3,5,7 and composite n=33,69,315.
At n=4545 all five tested d have no solutions: its dictionary test is **vacuous**, not a nontrivial composite validation.
For the counterexample n=105,d=3, in basis (1,s), HNF(𝔄𝔡𝔈)=[[639,54],[0,3]], whereas HNF((β))=[[639,18],[0,1]].
This is also an actual F3 screen member, not an irrelevant artificial parameter choice.
Φ multiplicativity passes 228 independently multiplied divisor pairs, including repeated primes and the nonmaximal order ℤ[√−39].
FR: an integral principal product has generator x+ys and norm x²+dny²<dn, hence y=0; comparing integer contents proves FR′.
Therefore injectivity holds on primitive integral invertible ideals with **pairwise norm product <dn** (in particular each norm <√dn).
Translation rigidity instead needs N(R)N(R′)N(L)<dn; two small representatives alone do not suffice. Independent small-ideal censuses pass for (409,1),(4545,1),(21841,3),(13,3).

## Nulls and calibration

The original PSC overwrite and PSF dropped-row failures are explicitly withdrawn; I do not reuse their inferential conclusions.
The corrected solver uses unimodular ±1 elimination, freezes unresolved rows at real values, and asserts original equations; the audit found no surviving constraint bug.
Independent seed 70042, R=200, d=1 F1 with smoke primes excluded: FIX-CS (Mx,Ex,L1,L3)=(3.40,2.51,3.40,2.29), C0=−2.73;
FIX-ALL=(−0.53,0.52,−2.79,−1.29), C0=−2.25. This confirms the direction without sharing the production random stream.
Independent pooling of saved per-n records, excluding smoke primes: FIX-CS d=1 L1=18.665; d=3 Mx=4.924, Ex=5.155; d=2 A2=4.805 (invalid control).
Preserving equations is necessary, not sufficient for calibration: pivot choice, freezing, widened prime pools, uniform large-prime classes and loss of small-norm geometry alter the comparison law.
Counts of nonzero-variance primes are degeneracy diagnostics, not power estimates against a specified arithmetic alternative.
The memo mostly reports these limitations honestly; its title and “calibrated, corrected account / structure = divisor lattices” summary remain stronger than the evidence.

## Mandatory falsifier audit

| Screen | Assessment |
|---|---|
| F1 odd squares | Correct obstruction: good A is prime to 2dm; each prime divisor of A splits for −d, whereas A≡−1 mod 4d requires χ_{−4d}(A)=−1. Existing-solution symmetries are vacuous. Availability of a nonsplit divisor at nonsquares is necessary, **not sufficient** for the tied residue. |
| F2 12 numerator-8 zeros | No positivity claim, so no contradiction. Even d gives the numerator-8 Type-II family; R₈ counts its c=1 subline, not all even-d solutions. The memo does not numerically screen these 12 inputs; d=2 small-window runs are not a substitute. |
| F3 285 composite zeros | Numerical scope is only 93 below 10⁵: 61 skipped, 8 small, 24 analysed. The missing ideal hypotheses fail at the screen member 105. Replace “a symmetry ... cannot separate” by “no tested identity establishes a prime/composite separation.” |
| F4 14 ★-zeros, 38 G*-zeros | The 35-input run contains all 14 ★-zeros but only 31/38 G*-zeros, not merely the 26 below 10⁶ (five larger ones overlap the ★ list). Missing: 1105441,2094481,4617649,11814001,20445289,85664329,564661441. No full-screen numerical claim is justified. |

## Untested or inadequately tested symmetry candidates — concrete next tests

- **Genus/ambiguous seeding:** for every ambiguous class and genus coset, enumerate principal/ambiguous seeds independently of G, then apply explicit candidate maps. Measure first entry into G, not just overlaps inside G; require failure at squares and report all four screens.
- **Rédei structure beyond h:** compute Rédei matrices and 4-rank/character pairings for −4dp (d=3,5,7) and −4yp/−4Cp witness orders; condition on norm, genus and invariant factors. v₂h of the two cyclic prime-field groups does not test these multi-factor discriminants.
- **Small-split-prime composition:** exhaust a fixed norm budget of translations, including nonprincipal-genus and ambiguous translations, and stratify by the exact FR product threshold. Test constructive orbits from a principal/ambiguous seed and untangle ideal identities from genuinely class-level relations.
- **Negative residual:** use an exact compatible lattice-point test N(R)N(R′)ℓ=x²+dny², retaining all natural representatives; validate against independently chosen nongood primitive ideals. ALLS and two-window MATCH2 do not settle the observed avoidance.
- **Fixed-n nonlinear/descent moves:** enumerate complete solution graphs for n=73,409 and hard zeros; search simultaneous changes or Type-I/II correspondences with fixed n. Multi-affinity only kills a coordinate-wise Vieta swap, not these maps; test whether an orbit can start without a known good solution.
- **Witness-decoy blind spots:** exhaust decoys for dropped small moduli; report their witness fraction and class orders separately; stratify retained pairs by factorisation type and 2-primary structure. Present effect bounds, not “genericity”; use a fresh held-out band for any new statistic.

## Required fixes, in priority order

1. Put gcd(n,d)=1 in the §1.1 class dictionary; separately require gcd(e,2dn)=1 for split-factor vectors. Scope Φ's composite G-description to admissible fibres; retain the counterexamples above as regression fixtures.
2. Retitle/conclude “substantial divisor-lattice contribution; no positive excess against the tested full-fibre null” rather than “the residual is divisor-lattice structure.” Keep unresolved deficits and failed pooled control adjacent to every calibration claim.
3. Replace “generic by SR/FR”, “fully explained” and unqualified “match” by the actual conditional non-rejection/within-stratum findings. Do not promote these into absence of a generative symmetry.
4. State the F2 untested numerical screen, F3 93/285 coverage and F4 31/38 coverage explicitly; either run the omissions or mark them untested. Scope the F1 necessity and F3 separation wording as above.

**Bottom line:** substantial, reproducible narrowing; the corrected prime-case algebra survives. The unqualified composite dictionary is false, calibration remains model-dependent, and the untested generative mechanisms remain open. ACCEPT-WITH-FIXES, not an ES advance or an exhaustive negative verdict.
