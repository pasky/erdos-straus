# z58 hostile cross-model review — TERNARY

**Verdict: ACCEPT-WITH-FIXES.** Theorem F survives independent re-derivation. The conclusion is **narrowed**, not dead: the genus main term is excluded on the local unit-square class, not the cusp route or all Type II encodings. ES remains OPEN.
Reviewed `side-agent/z58-ternary` at `fba42af75ce24d77a0c5dd1c9f2576fa3b179a81`, including AUTOMORPH Prop C and POINTWISE_TERNARY. All commands used `ulimit -v 4000000` and timeouts ≤ 1800 seconds.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| Lemma D(a)–(b), dictionary | CORRECT | Multiplication by the unit 4aC modulo f proves both directions; positivity and gcd(f,C)=1 are sufficient. |
| Lemma D(c)–(d) | CORRECT | The ray equation and distance are exact, representative-dependent; the two discriminants −4Cn and −16Cp are correctly distinguished. Jacobi reciprocity uses p≡1 (4). |
| Theorem F(i)–(iii) | CORRECT | The local-density factorization and prime-square asymptotic prove precisely the stated unit-class result. No squarefree-zero conjecture, Siegel lower bound, or Duke estimate is needed. |
| (H_δ) automatic for scalar ψ | CORRECT-WITH-FIX | The transformation character fixes the determinant square class. Specify det Q versus det(2Q): the displayed ε=(-det/ℓ) uses the quadratic-matrix convention. |
| Cor F1 | CORRECT | Unit squares modulo 840 are exactly {1,121,169,289,361,529}; arbitrary powers of 2,3,5,7 do not change the local unit-square condition. |
| §4.1 Shimura propagation | CORRECT | For fixed good p, E(pℓ²)=(ℓ+1−χ(-p det/ℓ))E(p), cusp O_p(√ℓ), no unary contribution. Validity on all n≡1 (4), not prime-only validity, yields the composite consequence. |
| “Unconditional where AUTOMORPH was conditional” | CORRECT, scoped | Replaces Prop C(b) on C₁ for genus-theta combinations with one ψ; does not prove Prop C(a) on arbitrary classes or for arbitrary Eisenstein series. |
| Pure-cusp / Waldspurger reduction | CORRECT-WITH-FIX | Pure cusp is unconditional in F's scope. A single Shimura eigensystem admits the local-class comparison below; a sum of different eigensystems is not one L-value. Preserve this distinction in summaries. |
| Waldspurger screen | CORRECT-WITH-FIX | Recomputed decisive data agree. It screens R-support proxies valid at the screened primes, not general Type II proxies; ranks remain numerical evidence. |
| §4.3 / POINTWISE comparison | CORRECT | One fixed bounded-complexity recipe plus a generic-size representation theorem is obstructed. Thin admissible sets, growing families and H5 remain outside that conclusion. |
| Remark F2 / “fixed-level forms cannot see it” | CORRECT-WITH-FIX | Polynomial square obstruction is relative to the identity's modulus. No theorem here forbids finer-modulus identities or all fixed-level encodings of tied conditions. |

## Independent derivation of F

1. Write Q(x)=xᵀAx and d=det A. Away from 2N all lattices are unimodular ternary; common determinant square class implies local isometry. Siegel's formula therefore gives E(n)=B(n)Σᵢcᵢκᵢ∏_{q|2N}α_q(Lᵢ,n).
2. For n∈C₁ every bad-prime density equals its value at 1, by x↦ux for n=u²∈Z_q×². Hence E(n)=B(n)A₀. The good-prime product B(1)>0 follows from L(1,χ_{−d})/ζ(2) with finitely many factors removed; χ_{−d} is nonprincipal. Thus E(1)=0 forces E(n)=0 throughout C₁, including nonsquare composites.
3. At a good odd ℓ, counting nonsingular solutions over F_ℓ gives α_ℓ(1)=1+ε₀/ℓ. For n=ℓ² the primitive contribution is 1−ℓ⁻²; x=ℓy contributes ℓ⁻¹α_ℓ(1). Consequently ℓα_ℓ(ℓ²)/α_ℓ(1)=ℓ+1−ε₀, proving the genus recurrence even when E(1)=0.
4. Genus subtraction is cuspidal. Split it into unary forms and U⊥. On each good-Hecke eigencomponent, h(ℓ²)=(λ(ℓ)−ψ(ℓ)(−1/ℓ))h(1); the cuspidal Shimura lift and Deligne give O_h(√ℓ). If h(1)=0 the term is exactly zero. The only admissible unary indices contributing at ℓ² are t=1, with coefficient 2χ(ℓ)ℓ.
5. Therefore 0=g(ℓ²)=ℓ[E(1)+2Σκ_χχ(ℓ)]+O_g(√ℓ). Dirichlet in every invertible class modulo 4N makes the bracket identically zero on that finite group. Averaging kills the odd characters, giving E(1)=0; character independence gives κ_χ=0. Old/imprimitive unary redundancies must first be removed, as the memo now does.
6. At a good prime p∈C₁, E(p)=0 and unary support is absent, so g(p)=h⊥(p). All-n R-support validity supplies g(ℓ²)=0 by T1; the theorem itself only assumes eventual prime-square vanishing. Prime-only validity supplies no such hypothesis.

This argument does not establish a converse: “exactly” should describe C₁=M at level 840, not assert that E cannot vanish elsewhere. Mixed nebentypus, non-genus Eisenstein parts, signed minorants and higher weights remain unclosed.

## Primary-source checks

The following are article text/scan checks, not metadata-only verification. Local copies/OCR are in `/tmp/xrev_TERNARY/`.

- **Duke–Schulze-Pillot (1990), pp. 54–56:** [primary scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0099/LOG_0011.pdf). Theorem 2(i) is the genus product of local densities; Theorem 2(ii) distinguishes spinor genus from genus outside finitely many square classes. Lemma 4(i) says theta minus genus theta is cuspidal; Lemma 4(ii) and its following paragraph identify U⊥ with cuspidal Shimura lifts. These directly support F's decisive inputs, also for general level.
- **Same source, Theorem 3 and Corollary, p. 56:** error n^{1/2−1/28+ε}; the main term is the *spinor-genus* average, with the stated square-part/congruence restrictions. The corollary requires primitive representation by the spinor genus. This is not “every sufficiently large locally represented integer” without qualifications. Large good primes avoid the finitely many exceptional square classes. Replace the stale contrary paraphrase in `lit_verify.md` §2, rather than merely appending a correction.
- **Iwaniec (1987), Theorem 1, p. 386:** [primary scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0087/LOG_0022.pdf). For actual weight κ≥5/2 and squarefree n, |a(n)|≪n^{κ/2−2/7}τ(n)(log 2n)². This equals κ/2−1/4−1/28, not the erroneous alternate exponent still present in `lit_verify.md` §3.
- **Duke (1988), pp. 73–76 and Theorem 5:** [primary PDF](https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf). Equation (1.2) recalls Iwaniec's bound; p. 76 explicitly says Theorem 5 includes holomorphic weight 3/2. Thus 13/28 is correct. Duke–Schulze-Pillot Lemma 2 supplies the general-character version and explains the Shimura/Deligne extension. Duke's Theorem 1 concerns fundamental discriminants and a fixed region, not exact hypercycle incidences.
- **Waldspurger (1981), I §§1–4, Corollary 2 p. 379, proof pp. 483–484:** [primary PDF](https://mate.dm.uba.ar/~nsirolli/files/waldspurger.pdf). His level N is the memo's 4N, and his weight numerator k is 3. Weight 3/2 is explicitly restricted to U⊥. With χ₀=ψχ_{−1}, the twist φ⊗χ₀⁻¹χ_t is φ⊗ψ̄χ_{−t}, agreeing with the memo and χ_{−4p} when ψ=1, p≡1 (4).
- **Important even-level repair:** Waldspurger Corollary 2 applies when n₁/n₂∈Q_q×² for every q dividing the level; it does not require odd N/4 or complete bad-prime eigenvectors. It gives a(n₁)²L₂ψ(n₂/n₁)n₂^{1/2}=a(n₂)²L₁n₁^{1/2}. On the screened ψ=1 class this is the desired constant-ratio relation whenever an anchor L-value is nonzero. The proof's last paragraph explicitly removes (H2) for same 2-adic square class. (H1) is automatic if the associated half-integral eigenspace exists, by Proposition 2. Hence even level alone is not an unresolved obstacle for this comparison; do not blindly cite Theorem 1 without its H2 or infer nonvanishing from a 0=0 ratio when every L-value vanishes.

The memo honestly labels its stronger general-level factorization (W-loc) a hypothesis. Keep that label unless its precise formulation is proved, but cite Corollary 2 for the comparison actually needed by the screen. For arbitrary nonquadratic ψ retain the character factor; do not claim a constant depending only on square classes without accounting for it. For nonempty scalar ternary-theta combinations ψ is quadratic. None of these source qualifications weakens F.

## Numerical reproduction

- `dict_check.py 150`, `thmF_check.py 40000`, `orbit.py`, and `coprime.py` reproduce their stored outputs byte-for-byte. The r(1)=0 row remains an ineligible diagnostic, not a failed genus identity. The theta checks are not computations of genus averages.
- Independent `scripts/z58_xrev_ternary_check.py arithmetic` recomputes the six residue classes, census summaries and six local densities (Q=⟨1,1,d⟩, d=1,2, q=3,5,7) by exact congruence counting modulo q³. All match.
- Census agreement: 486 nonsquare composite zeros; 17 prime-square orbits; multiplier set {3,5,7,9,11,21}; coprime-to-105 count/max 24/29210401; coprime-to-1155 count/max 16/17401609; in-M maximum 17401609. The source census's exhaustive zero certification, and LADDER's extension to 10¹¹, were not rerun.
- The original Waldspurger run hit its 900-second timeout after **12 complete rows**, all byte-identical (144 root/rank pairs). The independent script recomputed **all 192 root numbers** and the **16 zero-prime ranks** of the remaining four rows. Thus every decisive zero-prime rank was rerun, including the two conductor-32 models.
- Signs −1 occur exactly for conductors 21 and 45; every other row has numerical rank 0 at ≥2 of the four zeros. In particular conductor 32 at p=83449 gives L(E⊗χ_{−4p},1)≈0.0363071068404249, and at 102001 ≈1.18223142060929. Default-precision `ellanalyticrank` is not a certificate.
- Recounted stored rank-2 statistics: 11/56 versus 14/112; removing the duplicate conductor-32 row gives 9/52 versus 14/104. The last four rows' control ranks were not independently rerun; no statistical inference is justified.

## Mandatory falsifiers

| Screen | Hostile check |
|---|---|
| F1 odd squares | Pass in F's exact class; the genus kill, not a Hecke relation between squarefree parts 1 and p, is the new mechanism. |
| F2 numerator 8 / C-even | Negative theorem remains valid since R₈≤R. Checked 12 supplied zeros, 4 in M. No positive C-parity separation is claimed. |
| F3 285 composite zeros | Checked the supplied list has 285 entries, 15 in M. The larger census assertions reproduce. F does not require infinitely many nonsquare or squarefree zeros; finite disappearance beyond 3·10⁷ coprime to 105 says nothing asymptotic. |
| F4 14 (★) / 38 G* primes | Counts are 14/9 in M and 38/20 in M. The four-prime screen is sound evidence only for R-support validity at those indices. G*-support would impose its own additional zeros; no construction is supplied. General Type II support is NOT constrained by R-zeros. |

## Required fixes, in priority order

1. **Separate R-support from Type II support throughout Q-T, F4, §4.2 and the bottom line.** The screen cannot exclude a general Type II proxy. Explicit witnesses (a,b,c,d) at its four R-zeros are: 5569→(3,472,5,1), 9601→(3,835,2,1), 83449→(3,7072,5,1), 102001→(1,26609,6,1). Each satisfies 4abcd=a+b+nc and has c>1. These were independently generated and checked. Retain the screen conclusion only for R-support proxies valid at the screened primes; its existing threshold and multi-eigensystem caveats are essential.
2. **Scope the polynomial and “cannot see” language.** C₁ at a given level forbids a polynomial identity on that square residue class of the *same modulus*, not finer moduli. Counterexample: n≡8401 (9240) lies in 1 mod 840 yet has the fixed (★) recipe (u,B,C)=(3,(n+3)/11,1), because n≡8 (11). The class is primitive and contains infinitely many primes. Replace the blanket Remark F2 claim and §6 “fixed-level forms cannot see it” with the actual genus no-go / fixed-embedding statement.
3. **Repair literature notes in place and add exact primary references above.** In particular genus versus spinor genus, Iwaniec's exponent, and Waldspurger's character/H2 hypotheses. The same-local-class corollary resolves the even-level comparison concern, but does not certify the numerical L-values or prove universal nonvanishing. Do not silently promote the entire (W-loc) formulation.
4. **Carry theorem scope into headlines/FRONTIER text.** One scalar nebentypus, genus-theta Eisenstein part, support validity at prime squares, unit classes, and level restriction for all M-primes are indispensable. Say “on C₁, which is exactly M at level 840,” not a converse claiming the only vanishing classes. Specify the determinant convention. Keep “unconditional” relative to the standard proved inputs, not as a replacement of all AUTOMORPH Prop C.

After these fixes, record F as a genuine unconditional scoped strengthening and the lane as **narrowed**. No positivity theorem, all-proxy exclusion, or advance toward an ES proof follows.
