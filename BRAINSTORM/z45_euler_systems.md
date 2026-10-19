# z45 — Euler systems, tied moduli, and a finite-support obstruction

## 0. Summary

**Assessment.** Euler systems really can act at one fixed arithmetic object, so the average leak B6 is not their fundamental problem here. Their norm relations, however, do not respect the certificate condition. There is an elementary reason an exact, nonvanishing-detecting system cannot satisfy ordinary norm compatibility: at fixed p the certificate levels have finite support, whereas a norm-compatible class cannot die permanently upstairs and remain nonzero downstairs. Cyclotomic units and Stickelberger distributions have explicit compatible families but do not detect the divisor event; the obvious p-twist is actually trivial at the sole (★) level of p = 3361. Heegner systems have a further mismatch between modular level, quadratic field, and ring-class conductor. Complete small-prime censuses verify both creation and destruction of certificates under C ↦ Cℓ. A larger auxiliary system with a non-functorial, height-sensitive extraction map is not ruled out, but constructing that map with an existence theorem is precisely the unbroken B2 step.

**Verdict: PARTIAL — exact missing implication: nonvanishing of an independently constructed auxiliary Euler/Iwasawa class ⇒ a positive, bounded-height divisor in the single class −1 at some tied level. Direct faithful norm-compatible detectors COLLAPSE. Promise: 1/5. ES remains open.**

**Assessment / prior coverage.** Searches of tracked markdown for `Euler system`, `Kolyvagin`, `Iwasawa`, and `norm.compatib` found no previous Euler/Kolyvagin-system construction. This is not a claim that towers, Heegner points, or Gauss sums are new here: `TORSION_FIRING.md` §3.4 already screens cyclotomic/anticyclotomic towers as Frobenius firing devices; `BRAINSTORM/bsE_qpower_moduli_Z.md` and `bsE_padic_interpolation.md` screen prime-power depth; `TWO_POWER_LADDER.md`, `CLASS_FORCING.md`, `KUDLA_ES.md`, `BRAINSTORM/bsC_valence_borcherds.md`, and `B2_ACROSS_FIELDS.md` supply the existing dictionaries. The new contribution below is the narrowly scoped finite-support/norm-compatibility screen and its exact toy tests, not a new arithmetic existence theorem.

## 1. Precise dictionary

### 1.1 Three different meanings of “level”

**PROVED (elementary; the existing (★) dictionary).** Put

- t = 4C, N_C(p) = 4Cp + 1;
- S_C(p) = {d > 0 : d | N_C(p), d ≡ −1 (mod 4C)};
- r_C(p) = |S_C(p)|.

Writing d = 4Cu − 1 and N_C/d = 4CB − 1 gives

    4CuB − u − B = p,
    4/p = 1/(uBC) + 1/(pBC) + 1/(puC).

Here u,B ≥ 1; boundary values 1 are INCLUDED. Thus Σ_C r_C(p) = R(p), the (★) subfamily, not the full Type II count and certainly not an equivalent reformulation of ES. In the four primes below there are no equal-divisor pairs, so r_C is twice our tabulated unordered count.

**PROVED (full Type II dictionary).** For a full Type II tuple,

    4abd = p + e,  a + b = ce,
    C = cd,  f = 4Ca − 1,  f′ = 4Cb − 1,
    ff′ = 1 + 4cCp = 1 + 4c²dp.

Its denominators are (abd, pacd, pbcd). Thus the modulus is 4C but the side integer also depends on c | C. The star line is c = 1. The Heegner form [f,2,f′] has discriminant D = −16c²dp. The basis change in `bsC_valence_borcherds.md` puts it on X₀(4cd) with the additional representative condition C_form + 1 = B_form/2. Merely belonging to the ambient Heegner divisor does not impose this extra condition.

**PROVED (consequence of that discriminant formula).** On the star line the CM field is Q(√−Cp): replacing C by Cℓ generally changes the field, not just its conductor. Along C ↦ Cℓ² its square class stays fixed, but the modular level changes too. In the full family, fixing d and varying c keeps Q(√−dp) fixed and multiplies the order discriminant by ℓ² when c ↦ cℓ; simultaneously X₀(4cd) changes. These are not the usual Heegner systems on one fixed elliptic curve / one fixed X₀(N), with only ring-class conductor varying.

**PROVED (existing ideal dictionary, restricted family).** For p ≡ 1 (4), O_K = Z[√−p]. With β_k = 1 + 2k√−p,

    N_K/Q(β_k) = 1 + 4k²p.

The shot family in `B2_ACROSS_FIELDS.md` Lemma 4.1 / `BRAINSTORM/z31_duke_equidistribution.md` consists exactly of ideal divisors a | (β_k) with Na ≡ −1 (mod 4k). This is the d = 1 slice of the full Type II dictionary, with c = k; it is NOT the whole star line and NOT all ES solutions. This fixed-field version is the best candidate for a ring-class tower, but β_k itself is changing.

### 1.2 A fully class-aware object exists, without norm compatibility

**PROVED (group-ring encoding).** For G_C = (Z/4C)× define

    D_C(p) = Σ_{d | N_C(p)} [d mod 4C] ∈ Z[G_C].

Its coefficient at [−1] is exactly r_C(p). Its Fourier transform is

    χ(D_C(p)) = Σ_{d | N_C(p)} χ(d)
               = ∏_{q^a || N_C(p)} (1 + χ(q) + … + χ(q)^a),
    r_C(p) = (1/φ(4C)) Σ_χ χ(−1) χ(D_C(p)).

Character orthogonality proves the last formula; factoring a divisor into prime powers proves the middle one. This uses ALL characters, not just the quadratic layer. The product is an Euler product over prime factors of ONE N_C; it is not an Euler-system norm relation between levels C and Cℓ.

**Assessment.** One must not assert “Euler systems only see parity.” Cyclotomic and Heegner systems have genuinely higher-character information. The missing theorem connects that information to this particular D_C(p), or to a coefficient of its analogue for the full family. The campaign's reciprocity ceiling is a scoped statement about the forcing input, not a universal limitation on arithmetic cohomology.

## 2. What the actual existence machinery does

### 2.1 Cyclotomic units: explicit relations and an exact failed detector

**PROVED (classical identities, proved here).** Let m ≥ 4 be divisible by 4, F_m = Q(ζ_m), and u_m = 1 − ζ_m. Choose compatible roots ζ_{mℓ}^ℓ = ζ_m and write σ_a(ζ_m) = ζ_m^a. Then

    N_{F_{mℓ}/F_m}(u_{mℓ}) = u_m                    if ℓ | m,
    N_{F_{mℓ}/F_m}(u_{mℓ}) = u_m / σ_ℓ⁻¹(u_m)    if ℓ ∤ m.

For ℓ | m the ℓ conjugates give ∏_{j=0}^{ℓ−1}(1 − ζ_{mℓ}ζ_ℓ^j) = 1 − ζ_m. For ℓ ∤ m the same product has one forbidden exponent divisible by ℓ; its factor is 1 − ζ_m^{ℓ⁻¹ mod m}, giving the quotient. These are S-units when m is a prime power, and units otherwise. Kummer classes inherit the corresponding additive corestriction relations, since Kummer commutes with norms.

For a fixed a prime to mℓ, the unit v_{m,a} = u_m^{1−σ_a} satisfies the same relations. This gives the obvious p-dependent family v_{m,p} on levels prime to p.

**PROVED + CERTIFIED (counterexample to that detector).** At p = 3361, m = 20,

    3361 ≡ 1 (mod 20),  hence v_{20,3361} = 1,
    20·3361 + 1 = 67221 = 99·679,
    99 ≡ 679 ≡ −1 (mod 20).

So the Kummer class of the obvious p-twisted unit is zero at the unique star level C = 5, despite an actual certificate. Conversely the untwisted cyclotomic family exists independently of p, including at squares. Neither family has the desired nonvanishing dictionary. Other twists/regulators are not excluded by this example.

### 2.2 Stickelberger and Gauss sums

**PROVED (centered Stickelberger distribution, elementary).** Put

    Θ_m = Σ_{1≤a<m, (a,m)=1} (1/2 − a/m) σ_a⁻¹ ∈ Q[Gal(F_m/Q)].

For group-ring projection π from level mℓ to m,

    πΘ_{mℓ} = Θ_m                         if ℓ | m,
    πΘ_{mℓ} = (1 − σ_ℓ⁻¹)Θ_m             if ℓ ∤ m.

Indeed, over the ℓ lifts a+jm, the coefficients sum to 1/2−a/m. When ℓ ∤ m, subtract the unique lift divisible by ℓ; its projected contribution is σ_ℓ⁻¹Θ_m. This establishes the distribution relation without invoking an annihilator theorem. It is independent of p. Multiplication by 1−σ_p again kills the component at m = 20, p = 3361.

**PROVED relative to the classical Hasse–Davenport lifting theorem (memory; not source-verified here).** For a nontrivial multiplicative character χ of F_q× and nontrivial additive ψ, writing χ_r = χ∘N_{F_{q^r}/F_q}, ψ_r = ψ∘Tr,

    G_{q^r}(χ_r,ψ_r) = (−1)^{r−1} G_q(χ,ψ)^r.

This is extension-of-finite-fields compatibility, NOT conductor compatibility C ↦ Cℓ and NOT a divisibility relation among 4Cp+1. Gauss sums' nonvanishing therefore does not certify an ES divisor. No claim that this formula by itself constitutes the requisite global Euler system is made.

**PROVED (prior result, scope retained).** `TWO_POWER_LADDER.md` Thm 3.2, for residue orders 3 and 4, distinguishes the forced Stickelberger component S = ∏x_a^{a⁻¹} from the divisor's norm component D = ∏x_a. They agree only in the quadratic quotient. The above distribution relation does not identify those two components. In particular, an annihilation statement for an ideal-class group is not existence of an ideal divisor of the prescribed β_k in a prescribed norm residue class.

### 2.3 Heegner/Kolyvagin systems: a fixed-p tool, but not an existence seed

**PROVED relative to standard Heegner theory; verified source below.** Fix an elliptic curve E/Q of conductor N, an imaginary quadratic K satisfying the split Heegner hypothesis, and ring-class fields H_f. For an auxiliary prime ℓ inert in K with ℓ ∤ fND_K, compatible Heegner points satisfy

    Tr_{H_{fℓ}/H_f}(y_{fℓ}) = a_ℓ(E) y_f,
    a_ℓ(E) = ℓ + 1 − #E(F_ℓ).

The underlying divisor relation is Tr(x_{fℓ}) = T_ℓ x_f. We state ONLY the inert, prime-to-conductor relation; split-prime formulas need the horizontal CM terms and are not being suppressed. If G_ℓ is cyclic of order ℓ+1 with generator σ, Kolyvagin's derivative is

    D_ℓ = Σ_{i=1}^{ℓ} iσ^i,
    (σ−1)D_ℓ = (ℓ+1) − Σ_{i=0}^{ℓ}σ^i.

This last identity is a direct telescoping computation. For a separate coefficient prime r with r | ℓ+1 and r | a_ℓ, it gives the invariance modulo r needed to descend derivative classes; local congruence relations and duality then constrain Selmer groups.

**PROVED relative to Kolyvagin's theorem (verified statement).** In Tom Weston, *The Euler System of Heegner Points*, Theorem 4.1, good reduction at an odd coefficient prime r, surjectivity Gal(Q(E[r])/Q) ≅ GL₂(F_r), and y_K ∉ rE(K) imply that Sel(K,E[r]) has order r and is generated by the Kummer image of y_K. Proposition 5.2 and §6.1 provide the displayed inert trace and derivative relations. Source: https://swc-math.github.io/notes/files/01Weston2.pdf ; retrieved PDF and text are in `data/z45_euler_systems/weston.*`. Notation r here avoids confusing the coefficient prime with the fixed ES denominator p. The broader Gross–Zagier implication “nonzero L′ ⇒ a non-torsion Heegner point” is reviewed in that source's introduction; no derivative nonvanishing for an ES-attached E is established here.

**Assessment.** This theorem works at a single E,K. Auxiliary primes are selected, not averaged ES denominators, so B6 is not the problem. But its hypothesis already supplies a nonzero arithmetic seed. Norm relations also admit the identically zero system and alone cannot generate nonvanishing. Moreover nonzero rational points on E, or nonzero special-cycle classes, are not positive integral certificates on U_p.

**Assessment (application mismatch).** For ES, no fixed E and local Selmer condition encoding the representative equation C_form+1 = B_form/2 has been supplied. On the d = 1 fixed-field slice K = Q(√−p), the level 4c already involves the ramified prime 2; primes of c also divide the CM conductor. Thus the simplest split, coprime Heegner hypotheses cannot just be assumed. General CM/ramified-level constructions are conceivable, but they still require a proof that the certificate subset is respected by trace. `KUDLA_ES.md` §2 explains why the existing cycle-degree identities supply only a genus majorant unless the divisor-class restriction is inserted explicitly.

## 3. Attempts and exact tests

### 3.1 Finite support obstructs a faithful norm system

**Lemma 3.1 (PROVED).** If S_C(n) is nonempty for positive n, then C ≤ (n+2)/4.

*Proof.* With d = 4Cu−1, d′ = 4CB−1, u,B ≥ 1, we have n = 4CuB−u−B. This expression increases in either variable and is at least 4C−2. ∎

**Lemma 3.2 (PROVED; precise scope).** Let A_k be abelian groups, T_k : A_{k+1} → A_k homomorphisms, and a_k ∈ A_k. Suppose a_k = 0 whenever S_{C₀ℓ^k}(p) is empty, and

    T_k(a_{k+1}) = a_k.

Then every a_k = 0. The same conclusion holds for T_k(a_{k+1}) = E_k(a_k) if each E_k is injective on A_k.

*Proof.* Lemma 3.1 makes a_k = 0 for all sufficiently large k. Descend from such a k, using T_k(0)=0, and in the second version injectivity of E_k. ∎

**Assessment / limitations.** Consequently a class which is nonzero exactly when the level has a certificate cannot be a genuine norm-compatible family on an infinite tower that contains a successful level. This is stronger than failure of simple monotonicity, but ONLY under the stated faithfulness and compatibility hypotheses. Euler factors can annihilate classes, and a detector can be a non-functorial functional of nonzero auxiliary classes; the lemma excludes neither loophole. (R-z45 repair: non-injective traces are *not* a loophole — the lemma already allows arbitrary homomorphisms T_k; only annihilating Euler operators or non-faithful extraction escape.) After restricting to an eigenspace over a field on which the Euler factor is a nonzero scalar, however, its injective version applies again.

**Lemma 3.3 (PROVED; the issue persists for full Type II).** At p ≡ 1 (4), every Type II solution has a presentation

    4/p = 1/x + 1/(pY) + 1/(pZ),  Y ≤ Z,
    p/4 < x ≤ p/2,
    C = gcd(Y,Z) ≤ (p+3)/6.

*Proof.* Let e = 4x−p. Then 1/Y+1/Z = e/x; positivity gives x>p/4, while 1/Y+1/Z≤2 gives x≤p/2. Also Y≤2x/e. The function 2x/(4x−p) decreases, and the smallest integer x is (p+3)/4, giving Y≤(p+3)/6. To identify the canonical level, write Y=aC, Z=bC with gcd(a,b)=1. The equation x(a+b)=eabC shows ab | x; put d=x/(ab). Since gcd(x,e)=gcd(x,p)=1, d | C; put c=C/d. Then a+b=ce and C=cd, as required. ∎

Thus the same terminal-support obstruction holds for faithful full-Type-II level detectors, not merely for the deficient star subfamily. It is not a theorem forbidding all Iwasawa descriptions of finite data.

### 3.2 Why the arithmetic divisors do not norm down

**Lemma 3.4 (PROVED; multiplicative-level privacy).** For any integer h>1,

    gcd(N_C(p), N_{Ch}(p)) = gcd(N_C(p), h−1).

No positive divisor can be a certificate at BOTH C and Ch.

*Proof.* N_{Ch}−hN_C=1−h proves the gcd identity. A common certifying divisor d would divide h−1, while its upper-level congruence forces d≥4Ch−1>h−1, a contradiction. ∎

**Assessment.** This rules out literally carrying the same rational divisor upstairs and back down. It does not rule out a correspondence replacing it by a different divisor. That replacement is exactly the class-changing arithmetic input missing from the norm analogy.

**PROVED (fixed-field shot analogue).** For β_k above,

    N(β_{kℓ}) − ℓ²N(β_k) = 1 − ℓ².

Their rational norm supports therefore overlap only at primes dividing ℓ²−1. Both β_k and β_{kℓ} already lie in K; regarding β_{kℓ} as an element of a ring-class extension and norming to K gives a power of β_{kℓ}, not β_k. Ring-class norm relations for CM points do not give norm relations for this moving list of prescribed elements.

### 3.3 Complete census at the four requested primes

**CERTIFIED (exact arithmetic; independent engines for both (★) and full Type II).** Script `scripts/z45_euler_systems_scan.py` exhausts C≤floor((p+2)/4) by divisor search. Independently it enumerates every full Type II solution via

    (eY−x)(eZ−x)=x²,  e=4x−p,
    p/4 < x ≤ p/2,  1≤eY−x≤x.

It checks each Egyptian-fraction identity using exact rational arithmetic, recovers c,d,C, and matches the c=1 output against the first engine. A further independent full-Type-II engine enumerates C≤floor((p+3)/6), c|C, and factors ff′=1+4cCp in the required class, retaining gcd(a,b)=1 for canonical tuples; its complete tuple list agrees. Thus these are complete tables for the stated primes, not searches up to an arbitrary level cutoff. Counts are unordered Y≤Z.

| p | star bound | all successful star C (pair count) | all successful full Type II C (pair count) |
|---|---:|---|---|
| 3361 | 840 | 5 (1) | 5 (1), 290 (1) |
| 409 | 102 | none | 2 (2), 3 (1), 10 (1), 15 (1), 16 (1) |
| 577 | 144 | none | 2, 4, 10, 14, 21, 50, 58 (one each) |
| 5569 | 1392 | none | 2, 5, 8, 10, 12, 20, 30, 36, 204, 205 (one each) |

**CERTIFIED.** At 3361 the two full solutions are exactly

    (x,Y,Z;c,d,C) = (850,25,170;1,5,5),
                     (841,290,8410;10,29,290).

The star event at C=5 has factors 99,679. Along ℓ=5 its truth values at C=1,5,25,125,625 are 0,1,0,0,0; every later level is impossible by height. Thus both implications S_C≠∅ ⇒ S_{Cℓ}≠∅ and S_{Cℓ}≠∅ ⇒ S_C≠∅ fail, with the same p and ℓ. Full Type II similarly has a birth 1→2 and death 2→4 at p=409, while p=577 has birth 1→2, survival 2→4, and death 4→8. This is not evidence for any unobserved norm law.

**CERTIFIED (all star transitions within the feasible box at 3361).** Among C≤840/ℓ:

| ℓ | 0→0 | 0→1 | 1→0 | 1→1 |
|---:|---:|---:|---:|---:|
| 2 | 419 | 0 | 1 | 0 |
| 3 | 279 | 0 | 1 | 0 |
| 5 | 166 | 1 | 1 | 0 |
| 7 | 119 | 0 | 1 | 0 |

For 409,577,5569 every star transition is 0→0; this reflects failure of the entire subfamily, NOT failure of ES. JSON records all factors, solution tuples, transitions, and ℓ-power towers for ℓ=2,3,5,7, including full Type II towers.

**CERTIFIED (controls).** The star detector is empty at n=9,25,49,121,3481. At numerator 8, the analogous slice N=8Cn+1, d≡−1 (8C), is empty at 131 and 241. These numerator checks certify only the corresponding subfamily; the full numerator-8 exceptions are the established campaign controls, not independently recomputed here. Near-square test primes include 577=24²+1 (no star level but seven full Type II pairs) and 3361=58²−3 (one star level).

### 3.4 Iwasawa: there is a field tower, not a certificate tower

**PROVED (elementary tower structure).** For fixed ℓ, F_k=Q(ζ_{4ℓ^k}) contains a cyclotomic Z_ℓ-extension after removing its finite torsion Galois factor. Its completed group ring is Λ=Z_ℓ[[Γ]]≅Z_ℓ[[T]]. Cyclotomic units provide compatible elements in a unit/cohomology inverse limit. In contrast, the groups freely generated by S_{ℓ^k}(p) are zero for all sufficiently large k, so their inverse limit under ANY homomorphisms is zero. The same conclusion holds for the full Type II certificate groups by Lemma 3.3.

**Assessment.** No nonzero characteristic ideal of this literal inverse limit can control certificate existence: the module is zero. A Selmer/Iwasawa module of some different auxiliary object may be nonzero, but a control theorem connecting its specializations to the finite certificate sets is absent. Characteristic ideals do not automatically detect every finite-level event, even in standard Iwasawa theory. Allowing a separate auxiliary tower while retaining one fixed certificate level avoids Lemma 3.2; it simply abandons the proposed identification of the tower coordinate with the tied ES modulus.

**PROVED (numerical counterexample made exact by factor enumeration).** At p=3361,

    D_5 = 4[1]+3[3]+3[7]+2[9]+4[11]+3[13]+3[17]+2[19]
          in Z[(Z/20)×],
    D_25 = 2[1] in Z[(Z/100)×].

Here 4·25·3361+1 = 336101 is prime, certified by the divisor loop. Projection of D_25 to level 20 is 2[1], not D_5, and loses the entire [−1] coefficient 2. This is exactly a ramified cyclotomic step ℓ|m, where the unit norm law has Euler factor 1. Hence the most direct fully class-aware divisor distribution does not satisfy that norm law.

## 4. FRONTIER §4 checklist

**Assessment.** The audited proposal is “apply existing norm-compatible units / CM classes, then transport their nonvanishing into ES certificates.” PASS below means only that the specific objection is avoided, not that an ES proof exists. An exact divisor detector can repair several FAILs by definition, but then loses norm compatibility.

| # | result | reason |
|---:|:---:|---|
| 1 | FAIL | Units and ambient CM classes exist at odd squares. An exact S_C projection respects T1, but no norm-compatible extraction is provided. |
| 2 | FAIL | Cyclotomic norm laws also hold at m=8C and at p=131,241; nothing forces the required numerator-4 distinction. The numerical detector correctly rejects the 8-slices. |
| 3 | FAIL | The proposed transport law is numerator-independent. No 4-specific nonvanishing/extraction input is known. |
| 4 | FAIL | Modulus 4C remains tied to N_C=4Cp+1 (or to 4cCp+1). No theorem supplies its target divisor; Lemmas 3.2–3.4 block the most literal transfers. |
| 5 | PASS | p stays fixed in norm identities, Selmer arguments, and all computations. Choosing Kolyvagin auxiliary primes is not averaging p; recovering bounded ES height from that choice is instead missing. |
| 6 | N.A. | No main-term/error estimate is proposed. Merely counting all CM points would re-enter B3; no power-sized certificate count is asserted. |
| 7 | PASS | Only existence/nonvanishing is sought; no false two-sided asymptotic for R(p). |
| 8 | PASS | The proposed all-level family grows with p, so a fixed-menu B1 theorem does not alone refute it. Fixed-level p-twists see only p mod m; their explicit failure is recorded rather than promoted into a global impossibility claim. |
| 9 | FAIL | Higher-character Euler data are real, but no connection to the [−1] coefficient of D_C is proved. Substituting the known reciprocity forcing recovers only its quadratic shadow. |
| 10 | PASS | No pooling assumed. The stronger multiplicative-level gcd identity explicitly exhibits the privacy problem. |
| 11 | N.A. | No reflection of signed solutions is used; subtraction in cohomology is not claimed to preserve positive certificates. |
| 12 | FAIL | Nonzero units / rational Heegner points / ambient cycles are relaxed objects. Their extraction into the positive finite ES box is exactly the missing transport theorem. |
| 13 | PASS | No BM-only or local-global sufficiency is asserted. Kudla/BM positivity is recognized as insufficient. |
| 14 | FAIL | A universal star-system seed is impossible at 409,577,5569. Full Type II succeeds there but still has births/deaths; the obvious p-twisted unit vanishes at 3361's sole star level. |
| 15 | FAIL | Norm laws have no demonstrated response to the near-square class deficit. Exact tests at 577=24²+1 and 3361=58²−3 show that no naive persistence is available. |
| 16 | PASS | No transfer from a specially factored thin family to generic primes is claimed. |
| 17 | N.A. | No coset-covering/pigeonhole criterion is used. Supplying the missing large-factor residue information would still be B2, not a consequence of norm compatibility. |

## 5. “Euler systems for divisor events”: first axioms and toy test

**Definition / proposed framework (Assessment).** An exact event system would consist of:

1. A level object A_C(p), a positive cone, and a canonical class a_C whose nonzero positive part is equivalent to S_C(p)≠∅ (or the explicitly specified full Type II event).
2. Transitive transition maps T_{D,C} for C|D, and Euler operators E_{ℓ,C}, constructed from arithmetic independently of already knowing the successful divisors.
3. Relations T_{Cℓ,C}a_{Cℓ}=E_{ℓ,C}a_C, with sufficient nonannihilation on the detected component to transport nonvanishing.
4. An independently proved nonzero seed, and a positive, cap-zero, bounded-height extraction map. The seed must have a T1-sensitive, numerator-4-specific justification rather than being assumed equivalent to ES.

**PROVED (first theorem for these axioms).** If “nonannihilation” in axiom 3 is injectivity, these axioms admit no nonzero exact detector on a cofinal multiplicative tower at fixed p. This is Lemma 3.2, including the full Type II variant. Thus the first naive axioms are inconsistent with successful examples, not an untested conjecture.

**CERTIFIED toy case.** With the faithful scalar detector b_C=r_C/2 at p=3361, the 5-tower is

    b_1,b_5,b_25,b_125,… = 0,1,0,0,… .

Axiom 3 with the identity Euler operator would demand b_25=b_5, which fails. For the richer class-aware toy, πD_25=2[1]≠D_5 as in §3.4. Neither failure is merely loss of quadratic information.

**Assessment (minimal viable revision).** Retain a nonzero auxiliary system z_C even when the certificate set is empty, and introduce an extraction ε_C(z_C). Its compatibility must have a defect:

    T_{Cℓ,C} ε_{Cℓ}(z_{Cℓ}) = E_{ℓ,C} ε_C(z_C) + δ_{ℓ,C}(p).

The first genuinely new theorem needed would compute or bound δ without inserting the unknown divisor event, and use an independent seed to force a positive extracted class before the height cutoff. One cannot set δ=0, or merely assert it is harmless: the finite-support argument proves that it must absorb every surviving class eventually.

**PROVED toy defect calculation.** For the scalar identity-operator toy, take δ_k=b_{5^{k+1}}−b_{5^k}. Then δ_0=+1, δ_1=−1 and all later defects are zero; their total telescopes to zero. Thus a signed telescoping identity alone gives no positive existence theorem. At the group-ring level the defect at 5→25 is 2[1]−D_5 and its [−1] coefficient is −2. Defects necessarily contain the precise class information one hoped the norm law would supply.

**Assessment.** This is a specification of a missing theory, not a conjecture with evidence for its existence. A useful experiment must first find a genuinely arithmetic, certificate-independent defect formula on a fixed-field full Type II slice. Simply naming a Selmer group or defining a module whose generators are the desired solutions would be circular. No candidate here meets that requirement.

## 6. Verdict and next steps

**Assessment — PARTIAL, promise 1/5.** Off-the-shelf cyclotomic/Stickelberger/Heegner systems do not transfer to ES. A faithful norm-compatible event system collapses at finite support (B-fin), and a nonfaithful auxiliary system stops at the class-sensitive extraction step (B2), not at B6. This does not rule out every future Euler-system construction; it states the exact axiom that must be abandoned and the replacement theorem that must be supplied.

**Self-review (Assessment).** I checked the decision against the actual inert trace formula and its nonzero-seed hypothesis, separated star/shot/full-Type-II levels, and checked the potential counterarguments to Lemma 3.2: annihilating Euler factors and non-functorial extraction escape its hypotheses. The verdict therefore remains PARTIAL rather than a claim that all Euler-system approaches are impossible.

**Concrete next steps (Assessment).** The only economical follow-up is to choose a fixed d, a precise CM/Heegner correspondence on the c-tower, and compute its action on the extra condition C_form+1=B_form/2. Reject it unless a certificate-independent defect law appears. A second possible test is to keep C fixed and add a separate auxiliary conductor: then the finite-support lemma no longer applies, but a full-class, positive-height extraction map must be exhibited before any Selmer computation. More prime census alone is unlikely to change the conclusion.

**CERTIFIED reproducibility.** Run `ulimit -v 2000000; timeout 90 uv run scripts/z45_euler_systems_scan.py`. The script uses only the standard library, O(p²) elementary iterations for these small p, and no dense arrays. All assertions pass; the independent star and full-Type-II enumerations agree. Outputs: `data/z45_euler_systems/census.json` and `census.txt`; literature source: `weston.pdf` and `weston.txt`. No existing project file is modified.
