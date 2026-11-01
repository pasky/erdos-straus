# Cross-model hostile review — NONCRTLOGIC

Reviewed `side-agent/z53-noncrtlogic` at `9ca51044209b9881bf7770943f2d4b356e8cd682`.
**Verdict: ACCEPT-WITH-FIXES.** Theorems A and T survive independent derivation; the local variant needs explicit closure hypotheses, and the class-number escape statement needs a quantifier/label repair. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| A(a), finite-information transfer | CORRECT | At each non-oracle node use M(a); at an oracle node its actual answer selects an existing child. Finite branching plus halting on every branch gives a finite computation tree, hence one maximum threshold. No distribution or Chebotarev assumption enters. |
| A(b)–(d), existence/counts | CORRECT | Union all branch families and local precisions. M(b)'s integrality, irreducibility and no-fixed-prime-divisor proof works for that union, including nonlinear P; H/BH/Dickson qualifications are retained. |
| A(e), finite-tree obstruction | CORRECT | Universal nondegeneracy makes appended denominator FACTORs legitimate, including unrealised leaves. Only correctness of the realised leaf is used. The T′ alternative needs fix 1. |
| A1, fixed nonabelian/bounded data | CORRECT | These are genuinely finite alphabets (undefined arithmetic cases can be totalised). Arbitrary predicates cannot evade the union argument; the finite-defined-tree restriction is essential. |
| A2, divisor-valued oracles/orders | CORRECT | Under admissibility DIVISORS(F) has its formal fixed length, so a capped index oracle suffices. For composite m, factor m first and use φ(K)∏r_h^(e−1)(r_h−1); require the stated coprimality/domain guards. |
| A3, constant advice | CORRECT | B bits give 2^B branches. The O(log log p) upper discussion is explicitly conditional on X_win(C), not a proved upper bound. |
| T1, principal prime and reversal | CORRECT | Norm(1−qβ)=P(q)=p implies an ideal of norm p and residue field F_p. Reducing β^d h(q) gives h^∨(β); inversion does not change a quadratic symbol. |
| T2, Hilbert reciprocity | CORRECT | At the odd prime ideal 𝔭, x is a unit and π a uniformiser; its Hilbert symbol is the residue symbol. Outside T(x)∪{𝔭} both are odd-place units. Product reciprocity gives the claimed identity. Sources checked below. |
| T3, real places | CORRECT | Every real conjugate β is negative, since 1/β is a nonzero real root of P. Thus 1−qβ>0 for q>0. |
| T4, QR transparency | CORRECT | At each relevant finite place π is a square; at real places it is positive; all factors of T2 are 1. Apply separately to β and h^∨(β). This concerns values, NOT all their prime factors. |
| T5, universal nondegenerate traps | CORRECT | Hensel solves y²+y=2z for 1+8z even in ramified 2-adic fields. At good ℓ the distinct reversed factors give squarefree products; the character expansion yields the stated weaker Weil lower bound. Avoiding the first k(ℓ) polynomials, then countably many local roots, gives nondegeneracy for every fixed h. |
| T, nonlinear witness obstruction | CORRECT | Append all output factorisations. For h≠P, h^∨(β)≠0. T4 makes h(q), C_h and constant prime factors residues after finite refinement; hence every prime factor of a p-free denominator is a residue, contradicting CT(a). H supplies admissible primes, not the character argument. |
| T′, merely local traps | CORRECT-WITH-FIX | Local trap conditions suffice, but a defined original tree does not itself guarantee that newly appended output FACTORs are defined at a non-universal point. Require nondegeneracy for the entire augmented family and C_P=1; see fix 1. |
| Trap examples / non-examples | CORRECT-WITH-FIX | Families, sign exclusions, and Gaussian conditions at 2,3,5 check out. “Every admissible p≡1 (24)” requires including 2,3 at trap precision; see fix 3. |
| Cor T1, Pell/CF and one √(kp) | CORRECT | Recomputed the √(q²+1) period 1 and half-integral period 3 from the complete-quotient recurrence. Unit coordinates are (2q,2); no smaller unit exists since b=1 would require q²±4+1 square. For √((kq)²+k), the repeating block is (2q,2kq). No maximal-order assertion for general k is smuggled in. |
| Cor T2(i), rational powers | CORRECT | Choose prime N≡1 modulo the exponent denominators. The expansion at infinity has rational coefficients and integral leading exponent; truncate its polynomial part, then fix coefficient-denominator congruences and the eventual remainder sign. |
| Cor T2(ii), irrational/log/joint-root obstruction | CORRECT | An infinite agreement subsequence forces polynomial degree nθ and leading coefficient cL^θ. Both roots would require L and 2L square; log P grows unboundedly but slower than every nonconstant polynomial. These are all-integer growth obstructions. |
| Cor T3(a),(b), QNR menus | CORRECT | Clear rational denominators and refine by their primes and the norm supports. Every candidate is zero or a residue. The memo correctly separates this pointwise fact from prime-input no-semantics, which needs infinitely many primes (H, or Dirichlet in the linear case). |
| Cor T3(c), necessary condition | CORRECT within the stated trap/admissibility scope | A finite augmented polynomial menu cannot supply the required non-residue prime factors. “Non-formal” must mean failure of a fixed finite menu, not that every intermediate of an unbounded search individually lacks a polynomial description. No sufficiency claim survives. |
| Cor T4, Cornacchia uniqueness/transfer | CORRECT | For k≥2, Cauchy–Schwarz bounds x₁y₂+x₂y₁≤p/√k<p. Divisibility of the product of sum and difference by p therefore forces equal ratios, hence equal primitive pairs. For k=1 allow the coordinate swap. |
| CF-norm QNR-blindness | CORRECT | An odd prime dividing a convergent norm cannot divide its denominator; therefore (p/ℓ)=1 and reciprocity applies. The even part is harmless only at p≡1 (8), as now stated. |
| §5, h(p) on X²+1 | CORRECT-WITH-FIX | The growth argument is sound: Siegel gives h→∞; GRH gives h=o(q), excluding every positive-degree polynomial. But prime-input “no semantics” also needs infinitely many primes in the class. The taxonomy must not present this as unconditional; see fix 2. |
| Proposition S and r-generic character rule | CORRECT | Reciprocity fixes n_p=r from the finite prefix. With u=24, primes other than r in H_h and C_h contribute +1, leaving (−1)^(v_r(H_h)+v_r(C_h)). This is a transfer/reduction, not a sterility proof with FACTOR. |
| S's inherited ET-class obstruction | CORRECT citation | STERILE_LOWER Thm 6.3 states the 2^21.4375 threshold and inherits Thm 2.1's finite-menu conclusion; Comp. 4.1 supports the small-r qualification. I checked the source statement, not its old numerical certificate anew. |
| Forest larger-edge criterion | CORRECT | Write p+ℓ=ww′. The edge congruence is w′≡−1 mod ℓ, w>ℓ is w′<(p+ℓ)/ℓ, and χ(w)=χ(ℓ)χ(w′). Thus bichromatic means χ(w′)=−1. |
| §6 associations and §7 verdict | CORRECT as Assessment | The reproduced conditional rates support an association, not a causal “parity only” theorem. “Narrowed, strengthened barrier” follows with the finite-tree, witness-producing and H restrictions; no ES conclusion follows. |

## Decisive computations

All executions used `ulimit -v 6000000`, finite CPU limits, and explicit `timeout`; Python ran through `uv`. Files were extracted into `/tmp/xrev_NONCRTLOGIC`, not applied to the worktree. Arrays in the census are O(5·10⁶), not Cartesian-product allocations.

Every saved stdout below reproduced **byte-for-byte**; qnrseed and forestroot JSON also reproduced byte-for-byte.

| Script suffix and arguments (`scripts/z53_noncrtlogic_*`) | Result |
|---|---|
| `trapcheck.py 4000 13 12` | All eight trap rows: zero violations; all twelve rows, counts and controls agree. In particular 240624 X²+1 tests and 86184 real-place-control violations. |
| `gausstoy.py 20000000 5000` | 322 admissible tuples; FAIL at 322/322; 3064/5000 control successes, all 3064 with a QNR prime and a composite formal value. |
| `primecert.py 20000000 4000` | All 322 tuples and all reported sub-2^64 trapcheck inputs pass the deterministic recheck. Degree-3/4 large-input rows remain probable-prime EVIDENCE, not certified primes. |
| `qnrseed.py 300 1000000 47 OUT` and `1000000 5000000 47 OUT` | Full 43442-prime census and all twelve zeros agree; both n_p-use rates, the ℓ=11 category statistics, and 33212/23630 CF-seed counts agree. |
| `rootparity_deep.py 1000000 3000000000 5 113 3000` and `... 29 113 3000` | Generic/deep instance counts agree; conditional larger-edge rates are respectively 0.324 vs 0.214 and 0.301 vs 0.160. |
| `rootparity.py 1000000 3000000 61` | Mordell-hard comparison agrees. |
| `forestroot.py 4 5000 OUT` | Special roots: 10/19 vs 11/19; Mordell sample: 279/400 vs 370/400; near-square sample: 124/131 vs 128/131; all square controls agree. |

The enumeration was also inspected: u≤B gives (4u−1)u≤p+u; enumerating divisors of p+u with m≡−1 (4u) is exhaustive. The CF seed strips the 2-part and rejects incomplete periods. Rerun agreement is reproducibility, not a second independent implementation of every count.

## Sources actually checked

- [Milne, Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf), III Thm 4.4 and Remark 4.5; V Example 5.4 (p. 179): Hilbert-symbol properties, local Artin interpretation, and the product formula over a number field. At an odd place, adjoining a nonsquare unit is unramified quadratic, so the uniformiser acts nontrivially and units trivially. This supplies the precise T2 input without relying on the unverified Neukirch locator.
- [Kopparty, The Weil bounds](https://sites.math.rutgers.edu/~sk1233/courses/finitefields-F13/weil.pdf), §4.1.3, p. 11: absolute character sum ≤(k−1)√q, with k the number of distinct roots. Every nonempty product in T5 is squarefree and nonsquare, so the bound applies.
- [Lamzouri, arXiv:1501.01003v2](https://arxiv.org/html/1501.01003v2), equation (1.3): Littlewood's GRH bound L(1,χ_d)≤(2e^γ+o(1))log log|d| for both signs of fundamental discriminant. This is the analytic input needed for the degree-positive class-number exclusion.
- Repository dependencies checked directly: POINTWISE_SIZE §§1.2–2 (especially M(b), whose proof permits nonlinear P); notes Lemma 77.6 (the Type-I/II Jacobi computations giving CT); Z52D_PELLCYCLE Lemma 1.4; STERILE_LOWER Thms 2.1/6.3 and Comp. 4.1.

## Required fixes, in priority order

1. **T′ closure hypotheses.** Define Π⁺ to append FACTOR of all nonzero SUCCESS denominators on every leaf, and require its whole formal tree to be defined and finite. Equivalently require nondegeneracy of P and every irreducible factor in its augmented S′, with C_P=1. Build Λ′, the original transfer precisions, and the trap precisions from Π⁺, not merely Π. A polynomial can be output using ring operations without previously being FACTORed; original-tree definedness does not check that polynomial's nondegeneracy. This repairs the proof and the A(e) reference without restoring universal nondegeneracy. State the F2 instance with its finite local valuation classes (t prime >5), not as a globally nondegenerate trap point.
2. **Class-number quantifiers/labels.** The proved analytic statement is: under GRH, every fixed finite rational-polynomial menu agrees with h(q²+1) at only finitely many prime inputs. Constant menus have this property unconditionally by Siegel. To conclude “no eventual prime-input formal semantics” on a congruence/trap class, additionally assume infinitely many prime q²+1 there (e.g. H). GRH alone does not supply quadratic prime values. If only finitely many such primes exist, eventual prime-input semantics is vacuous—the same issue already repaired for T3(b). Alternatively, specify an all-integer extension and supply a separate argument using infinitely many squarefree discriminants; the present prime-only proof does not do that. Put the actual qualifications in the taxonomy row as well as the paragraph; do not record a blanket PROVED escape for h(p).
3. **Local residue wording.** In the trap-point definition, replace “every admissible p is ≡1 (8) and ≡1 (3)” by “after including 2,3 in Λ at trap precision”. M's general admissibility definition does not automatically include these primes. Theorem T itself correctly does so; its conclusion is unaffected.
4. **Citations and export scope.** Replace the unchecked Neukirch pointer with a verified locator such as Milne V.5.4. Carry “defined finite formal tree”, witness production, the fixed finite menu quantifier, and conditional prime existence into any FRONTIER export. Keep the seed's supposed parity-only causal interpretation explicitly Assessment.

**Decision:** accept the main barrier strengthening after these repairs; no numerical discrepancy or counterexample to A/T was found. The h(p) addendum does not justify an unconditional new escape, and T′ must not be exported without the augmented-family hypotheses.
