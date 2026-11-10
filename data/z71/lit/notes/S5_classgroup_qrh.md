# S5 — class groups, quasi-RH, AI-instrument survey

**Scope/labels.** Source claims below are not independently proof-audited; arXiv/preprints are not peer-reviewed. READ means inspected theorem statements/introduction/abstract, not proofs. “Assessment (unreviewed)” is relevance only. Line numbers are `pdftotext -layout` source `.txt` lines.

## Core results

### Frei–Sofos–Widmer, 2610.18491, *Some applications…* — READ §§1–3
The cited “breakthroughs” are identified at lines 24–30 and references at 553–560: OpenAI, *The quasi-Riemann hypothesis: A zero-free half-plane Re(s)>7/8* (Ope26c; 2610.18491 cites the 9/30 release); *The Quasi-Riemann Hypothesis* (Ope26b; Dirichlet QRH(1/8), finite-order Hecke over Q(√−3) QRH(1/12)); *Primitive roots for every admissible integer base* (Ope26a; cyclotomic fields containing 12th roots, QRH(10⁻⁶)); and Cureton–Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*, Hexagon hexagon:2610.00200v1, QRH(1/6000) for all Dedekind zetas, hence finite-order Hecke L-functions. Authors explicitly say they have not verified those arguments (24–31); their results are conditional on QRH(δ).

**Theorem 1.1 (lines 74–78):** for δ∈(0,1/2], if ζ_L has no zeros with Re(s)>1−δ, then
`|π_C(x,L/K) − (|C|/|G|)Li(x)| ≤ c₁ (|C|/|G|)^{1−δ} x^{1−δ} (log(Δ_L x^{n_L}))^{1/δ}` for x>2 (effective absolute c₁).
**Cor. 1.2 (80–91):** a prime ideal in any specified conjugacy class exists by `x ≥ c(δ)(log Δ_L)^{1/δ}(log log Δ_L)^{2/δ}`; count in (x/2,x] between `(1/4,3/4)(|C|/|G|)x/log x`. Thus least norm `≪δ (log Δ_L)^{1/δ}(loglog Δ_L)^{2/δ}`.
**Cor. 1.3 (92–101):** short-interval Chebotarev, `(x,x+x^{1−δ/2}]`, relative asymptotic `1+O(1/log x)`, provided `x≥c(δ)(logΔ_L)^{2/δ}(loglogΔ_L)^{6/δ}`.
**Cor. 1.4 (166–177):** `#Cl_L[ℓ] ≪_{δ,K,d,ℓ,ε} Δ_L^{1/2−1/(2ℓ(d−1))+ε}` if the normal closure over K satisfies QRH(δ).
**Theorem 1.5 (188–199):** averaged rth moments over any family S of degree-d extensions, under QRH for normal closures: `Σ_{L∈S(x)} #Cl_L[ℓ]^r ≪ x^{r/2+ε}(1+#S(x)^{1−r/(ℓ(d−1)+1)})` (constants as stated there).
**Cor. 1.7 (lines 237–241):** least generator height `η(L)≤C_{n,δ}Δ_L^{1/(2n)}` under QRH for normal closure. All pointwise except Theorem 1.5, which is family-average. Method ≤6 lines: modify Lagarias–Odlyzko explicit formula; bound low-lying zeros under zero-free half-plane; partial summation gives effective Chebotarev; feed small split primes into Ellenberg–Venkatesh torsion argument and generator theorem.

### Banks, 2610.31402, *Landau–Siegel zeros…* — READ §§1–3, theorem statements
**Thm 1.1 (lines 90–96):** for each ε>0, C≥C₀(ε), quadratic F/k, X=d_F^C, inert-prime sum `Σ_{Np≤X,χ(p)=−1} logNp/Np ≤ (1/2+ε)logX+O_{k,ε,C}(1)`; C₀ independent of k.
**Cor. 1.2 (98–105):** effective c(k)>0 with `(1−β)log d_F≥c(k)` for every real zero of L(s,χ_F/k).
**Thm 1.3 (109–121):** every Galois K/k (K≠Q): real zeros of ζ_K obey same effective gap and `h_KR_K ≥ c(k)d_K^{1/2}/((2π)^[K:Q] log d_K)`; consequently effective Brauer–Siegel uniformly over such extensions with degree/log discriminant→0.
**Thm 1.4 (155–163):** for Galois K/k degree n_K, S⊂G containing identity, all C≥C₀(ε,n_K), X=d_K^C, `Σ_{Np≤X} δ_p logNp/Np ≤ (|S|/|G|+ε)logX+O_{n_K,ε,C}(1)` uniformly in K. (δ_p is proportion of Frobenius primes in S.) **Thm 1.5 (169–178):** refined bound with `1+(|S|−1)/H` multiplier and field term `n_k log λ_K`; source displayed inequality (1.3). Pointwise, uniform-in-fields Chebotarev *upper bound*, not a prime-existence/lower bound. Method: simple vanishing on Galois-conjugate lattice points + Masser zero estimate; compute lattice invariant by averaging over normal-closure Galois group; compare polynomial counts. Unconditional; theorem does not claim unconditional pointwise Chebotarev asymptotic.

### Liu, 2610.26835 & 2610.12234 — ABSTRACT/statement-only, no long proof read
2610.12234 lines 120–150 summarizes the refined boundary `B_new=0.874957019420098946…`; Theorem 13.1 at 1923ff and statement 338ff gives finite-order Hecke L-functions over Q(√−3), while Cor. 14.1/1949ff transfers to Dirichlet L-functions. 2610.26835 Thm 2.1 lines 434–442 states the same optimized boundary for the relevant modified-average family; its §3 extends to cyclotomic base fields containing μ₁₂ (lines 958–980); Thm 17.1 lines 7401ff extends only boundary `B♭=0.874886647…` to all number fields and finite-order Hecke L-functions (scope, not the sharper number). These are zero-free half-plane claims for stated finite-order Hecke/Dirichlet families, not a universal 0.874957 result; manuscript analyzes/optimizes a proof system and relies on claimed underlying inputs. No proofs audited.

### Louboutin, 2610.29347 — READ §§1–4
Abstract/lines 9–18: determine odd primes p with at most two distinct prime factors in every odd `p−x²`, `x≤√p`, and `2p−x²` for every even `x≤√(2p)`. Exact pointwise (“every x”) implications: **Prop. 12 (lines 465–485):** for p≡1 mod8, `Modd′(p)≤2` iff p in the explicit 17-prime list; then `Cl_K` cyclic generated by either prime ideal above 2. **Props. 5,7,8 (lines 184–220):** other p mod8 force listed forms (`n²−2`, `m²+2`, `9m²±8m+2`, `4n²+1`, `n²+4`), inertness of all small primes below Minkowski (with explicitly excepted primes), and class number 1; Props 7/15 permit one stated Siegel–Tatuzawa-shaped exception. **Prop. 14 (lines 510–547):** for d=2p, p≡1 mod4, `Meven′(2p)≤2` iff `2p∈{10,26,122,362}`; class number 2 and `2p=m²+1`. **Prop. 15 (lines 548–581):** d=2p, p≡3 mod8, same condition forces d=m²+2 or `9m²±8m+2`, class number 1, one possible exception. These are implications/classifications, not a general equivalence “few factors iff small class number”; class number conclusions follow via small-prime inertness/principality and Brauer–Siegel. Fundamental units/regulators are explicitly exhibited and O(log d). Method: choose a non-inert small prime, force it to divide d−x², compare nearby x values; few prime factors constrain factorizations, then infer principal ideal classes and invoke Brauer–Siegel/class-number classifications.

### Diao 2610.28001; 2610.11353; Luo–Wang–Zhou 2611.12528, 2610.14613; 2610.36800
READ theorem statements only (not proofs). **Diao** Thms 1.1–1.2 (lines 117–128, 198–211) are average asymptotics for class numbers of indefinite binary quadratic forms; Thm 1.3 (245–253) gives a uniform bound for small fundamental Pell solutions; Cor. 1.4 (257–261) is an almost-all nonsquare D result. These are average/asymptotic over discriminants, except the stated uniform Pell bound; no individual prescribed-class divisor. **Ray class monoids** Thms 5.2, 6.1 (2610.11353 lines 776–825): structural finite-monoid results for ideals/orders and ray congruence data; algebraic classification, no analytic prime theorem. **Luo–Wang–Zhou** 2611.12528 Thms 1.1–1.3 (89–185) give formulas for ternary genera/class numbers/representation numbers; 2610.14613 Thm 1.1 and Cor. 1.2–1.6 (134–293) classify a correspondence between definite quaternion orders and ternary forms and related local/Brandt data. Statements are representation/genus and order-classification results, not pointwise ES. **2610.36800** Thms 1.1–1.3 (74–160): counts/limits for reduced ideals missed by the reduction procedure, averaged over positive fundamental discriminants; no forced ideal at a specified prime. Method (cluster): genus/representation formulas, ideal/order correspondences, reduction dynamics/counting; no tie-modulus positivity.

## Survey 2610.17090 (READ, caveat: survey’s own disclaimer lines 31–36, 247–251: no Lean compile/kernel check, papers unrefereed; extraction not verification)
**Instrument inventory (38 family entries; family/problem followed by the named device(s), one line each):**
- 003 zero-free region: sextic-family Möbius embedding; cube completion/transfer; common-signal continuation and saturated-witness zero detector.
- 004 Hilbert tenth/Q: finite rational tests + compactness; five-point height estimate; pole-parity existential formula.
- 017 irrationality exponent π: separated-weight interpolation; weighted transverse multiplicity/normal-basis rigidity; determinant-smallness constructions.
- 032 CM Hodge: four-factor switch/algebraic contraction; rank-two theta-tensor surface criterion; degree-one CM extraction.
- 074 Kakeya: deformed critical-exponent surface/BV selection; two-frame entropy transfer; chart/horizon narrowness framework.
- 087 Mahler: conformal lens; holomorphic mass pushed to boundary; feasible-simplex identity.
- 362 Vlasov–Maxwell: signed momentum-increment bootstrap; signed force identity; retarded-bin occupation/direction-change selection.
- 304 Hilbert–Smith: compact-source test categories; fixed-sphere lattice/bounded comparison; character classes/equal parts.
- 102 Unique Games: latent alphabet gadget; exact table keys/translation-orbit folding; row-fiber abundance by erasure.
- 107 matrix multiplication: finite separation of shared leg/shared-leg entropy inequality; spectral growth on polynomial multiplication; detecting characters.
- 157 Hadwiger: hole relation with tensor certification; entropy-minimizing container; scalar recipe/gradient realization/collision machine.
- 158 plane coloring: Haar rigidity transfer; angular palettes/binary centers/transition graph; common exclusion continua.
- 159 reciprocal-sum: triangular polynomial cells; shift comparison/positive counting; relative lifting with additive rank/exact marked projection.
- 196 zero divisors: odd cross-intersection parity; bounded-pattern random-matching estimate; planar-separator extraction/cone-picture band surgery.
- 197 direct finiteness: incidence criterion; polynomial pairing on punctured affine space; hole trades/random slabs/local lemma; character-twisted HNN packing.
- 248 Thompson F: small cocycle prescribed word value; trace-preserving polynomial flow; adaptive error budgets/L²-density→W*-generation.
- 287 free group factors: tame variables/finite models/residual concentration; integral character-division/codimension-two divisor removal; theta implication retaining nilpotent tame parameter.
- 002 BSD: terminal-scale divisor bins/padding anti-concentration; finite residue comparison via Braverman; degree-normalized two-band divisor graph.
- 007 Chowla: marked lines/transverse charts; finite-jet ultrapatching; ordinary character family/Thorne points/polynomial-orbit lemma.
- 010 Fontaine–Mazur: marked Chow relation via Quot-scheme localization; Chow universality with two output factors; auxiliary-surface/divisor-cosection comparison.
- 040 Bloch: supported rational descent; rank quotient/supported asymptotic complexes; ordinary/dual norm comparisons.
- 193 Serre positivity: packets on saturated logarithmic flags/separation; isolated-zero finiteness/projection count; finite passage templates/matching systems.
- 143 Hilbert 16: noisy-observation conditioning/dimension-free tilt; conditional density determines field; convexity-preserved subsolutions.
- 263 ionization: optimized nested positive filters/stationarity/Schmidt pinning; replica metric transport; positive replacement/randomized scanner/amplification.
- 265 area law: coupled purity bootstrap.
- 268 Haldane gap: self-adjoint spatial transfer operator on bond histories; moment-to-spectrum exact-integer certificates.
- 103 L=RL=BPL: exact correction/copy hierarchy; rank channels/conditional averaging; allowance/clock controller with catalytic key equality.
- 112 depth-three circuits: restriction bound independent of clause count; sparse partition; slice language.
- 156 Borsuk: odd spectral extension; equality-case degree analysis.
- 266 mutually unbiased bases: six-label triangle systems.
- 221 diluted spin glasses: seed ball/fixed-frame completion; root certificates/tangent-normal refinement; injective moments.
- 285 Baum–Connes: marked-depth Poisson perturbations; depth shift/charging fresh splits; recursive single-site law encoding.
- 293 hyperinvariant subspaces: parity-swindle Bott cancellation in norm-sequence quotient; sheet-cone complex/exact cone chains/prime-order obstruction/Shapiro extension.
- 297 Naimark: survey card’s instrument(s) at lines 2235–2260 (not class-group-relevant).
- 309 Kervaire: survey card at lines 2286–2310 (not relevant).
- 325 Crouzeix: card at lines 2330–2360 (not relevant).
- 340 nearby Lagrangian: card at lines 2367–2405 (not relevant).
- 376 forced Navier–Stokes: card at lines 2421–2445 (not relevant).

**Relevant flags from this list:** divisors/residue classes: 003, 002, 007, 287, 159; sieve/parity: 003, 196, 197, 007; pointwise every-n: 112 (but circuit lower bound, not arithmetic), 287 (divisor avoidance in a different setting); class groups: none of the survey instruments presents a class-group forcing tool; Kloosterman/dispersion: none identified; integral points: 004/finite rational tests and 159’s integer-affine lifting, but not ES integral-point production. Survey has two distinct dividend bins/graphs in family 002, not a divisor-in-a-prescribed-ideal-class mechanism. Note: inventory labels for final cards 297/309/325/340/376 are titles/short descriptions rather than audited extraction; lines cited above should be checked before reuse.

## Assessment (unreviewed): campaign implications
`Z70_CLASS.md` and `Z70_GEN.md` both say no class-map forcing mechanism; their 2-torsion/Rédei and small-split-prime seeds are either blind or only tested/null models. Frei–Sofos–Widmer changes a *conditional* least-splitting-prime bound if the relevant Dedekind zeta QRH is assumed: exponent is `1/δ` in `log Δ`, hence 8 under OAI-003 Dirichlet QRH(1/8) when applicable, 6000 under Cureton–Thorner QRH(1/6000), and 2 under GRH (δ=1/2), with the `(loglog Δ)^{2/δ}` factor. Crucial scope: OAI-003 is about Dirichlet L-functions, not arbitrary normal-closure Dedekind zetas, so cannot simply substitute it for their general Chebotarev/torsion statements; CT is the broad claimed input. No unconditional numerical exponent follows absent accepting those AI claims. Under QRH(δ), torsion exponent improves from 1/2 to `1/2−1/(2ℓ(d−1))+ε`; it does not show small split primes generate the whole class group. Cor. 1.2 supplies a small prime in each Frobenius conjugacy class, not an arbitrary ideal class; class group generation requires every class represented by a prime in a range (Hilbert class field application possible conditionally, but least prime bound then discriminant of the class field and different extension degree). Banks gives effective class-number lower bound but only `hR ≥ c(k)√d/((2π)^n log d)` for Galois fields; with an upper regulator this is not a sharp useful class-number lower bound for a fixed real quadratic field, and it forces no target class/divisor. His uniform Chebotarev estimate is an upper bound on weighted prime mass, not a least-prime theorem. Liu zero-free improvements do not change the campaign’s pointwise tied-divisor obstacle.

`git grep` finds no campaign Rabinowitsch criterion or Louboutin-type “all small arguments have ≤k prime factors iff class number small.” Z70 has quadratic-form/class-group discussion and genus constraints, but not this every-x factorization criterion. A Rabinowitsch-like converse could suggest a forcing route only if an ES condition implied a uniform factorization bound for *all* small x; converse/class-number criteria alone do not force a divisor in a prescribed ideal class, and the residue class here is tied to the unknown modulus. F1/F2 remain unresolved by these results: averaging/zero-free/ideal-class constraints do not cure odd-square vanishing or establish numerator-8 line positivity.
