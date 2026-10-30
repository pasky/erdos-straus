# z52 deep lane D (opus) — how is a POINTWISE existence theorem in a THIN regime ever proved?

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results are internally reviewed only.

## Summary (to be written last)

(skeleton)

## Predecessors read (do not repeat)

This question has been asked in the repository three times already, and their verdicts stand:
* `DETERMINISTIC_EXISTENCE.md` (O168): 29 deterministic existence mechanisms, each with its failing step.
* `B2_ACROSS_FIELDS.md` ((J)94; 13 field memos `BRAINSTORM/z31_*`): the M1a/M1b/M2/M3/M4/M5 input pattern.
* `BRAINSTORM/s9_lower_tail_literature.md` ((J)103): "no every-n theorem for a natural problem with a polylog main term";
  natural polylog problems (p + 2^k, p + 2^a + 2^b, Markoff) have structured exceptions.

Also read, and cited below where relevant: `polynomial_method.md` (+ errata), `z31_zero_sum.md`, `z33_target_davenport.md`,
`EXSET_CHAR_FORCING.md` §2 (gate G4, Kneser covering lemma), `z45_recent_pointwise_tools.md` and `PRIMITIVE_INTERSECTION.md`
(Zsigmondy/BHV), `INVOLUTION_ES.md`/`INVOLUTION_ES2.md`, `invol_topological.md`, `z45_interlacing_stable.md`,
`noncounting_shapes.md`, `DEDEKIND_ES.md`, `z38_markoff_precedent.md`/`MARKOFF_ES.md`, `PROPAGATION_CLOSURE.md`, and FRONTIER §§2–7.

**What this file adds** (all Assessment unless labelled):
1. A taxonomy organised by *how the witness is extracted*, not by field. It separates thin-regime theorems from those
   whose count is secretly a power (§0).
2. A catalogue in which every entry carries a source-verification status (§1). Several items the earlier surveys marked
   "(memory)" are now checked: Chen's Markoff Thms 1.2.5–1.2.6, Ghosh–Sarnak (1.6)/(1.7)/Thm 1.2, Harpaz Thm 1.0.1, the
   Chevalley–Warning / restricted-variable / CN statements, Lamzouri–Li–Soundararajan, Ramaré–Walker, Huang, and
   Cilleruelo–Luca–Baxter.
3. A generator matrix (thick objects at p × extraction rules), plus four cells worked to a first lemma with numerics (§2).
   One cell answers the brief's Chevalley–Warning question; another answers the zero-sum/G4 question.

## §0 Taxonomy

**The organising distinction** (Assessment, checked against every verified entry of §1). "Thin regime" means that the
*final* witness count at one n is O(1) or polylog. Every verified pointwise theorem in that regime gets existence from
one of two sources:

* **(T) thick object + exact extraction rule.** A deterministic auxiliary object of size ≥ n^c (or the whole ambient
  group) is built from n. A local, exact rule extracts the witness: a collision/difference, a parity of fixed points, a
  count congruence, interlacing, or descent. The witness count can be 1 (Zagier: one representation; Dirichlet: one q;
  Huang: one vertex). The proof never estimates the witness count.
* **(R) algebraic rigidity.** The event is a Frobenius/character event at a *fixed* modulus (least witnesses under GRH;
  p = x² + ny²), or the integer has cyclotomic/binomial origin, so all its prime factors are confined to a small
  subgroup and a size/valuation squeeze applies (Bang–Zsigmondy, BHV, Sylvester–Schur). Or the count is an exact
  multiplicative function of n whose value at a prime is a Legendre-symbol expression (r₂(p) = 8, one-class genera).

All other pointwise theorems in the catalogue are **not thin**. Their witness count at one n is a power of n, and existence
comes from main-term dominance after enlarging the search box (circle method, sieve, Burgess, Linnik, Eisenstein vs cusp,
expansion on a power-size Cantor set). For ES, B-fin and B3 say the whole O(p²) box carries only a polylog count, so no
enlargement is available. In thin regimes *without* (T) or (R), the natural every-n statements are false or open:
p + 2^k, p + 2^a + 2^b, p + 2k² (5777, 5993), Markoff k with ≍ (log K)² average orbit count, x³ + y³ + z³ = k. ES belongs
to this last group. The relation to (J)94: (T) merges M1b and M5 and adds spectral and descent extraction; (R) merges M2
with the exact multiplicative counts and the squeeze. The new point is that the thick object and the extraction rule are
independent design choices. §2.0 uses this as a generator.

| class | precedent (verified entries in §1) | decisive structural feature | ES verdict (barrier / §4 line) | screened in repo? (scope check) |
|---|---|---|---|---|
| α exact identity / algorithm | Mordell identities; CLB palindromes (Thm 1.2, "proof is algorithmic") | witness is a piecewise polynomial / digit-local function of n on a finite partition | dead at primes: B1 Thm M covers ring ops, floor division (hence base-g digit carries), factorisations, loops; Mordell–Schinzel. Lives only on thin families ((J)74–(J)80) | yes: POINTWISE_SIZE, FORMAL_CLOSURE. Scope correct; palindrome-type carry algorithms are inside Thm M's primitive list |
| β count secretly large (mass / class number / character formula) | Gauss 3 squares, Duke–Schulze-Pillot, Bhargava–Hanke 290, Ono–Soundararajan (GRH), Ore via Frobenius formula | exact or asymptotic count ≍ n^c with a main term separated from cusp/error | dead: count ≍ log²p (B3); the exact theta-quotient normal form is Eisenstein-only ((J)101) | yes: z31_quadratic_forms, B2_ACROSS row 3, (J)101 |
| β′ exact O(1) count, positive by a congruence | r₂(p) = 8 (two squares); one-class genera; negative Pell at primes p ≡ 1 (4) | count is multiplicative in n (Eisenstein, one class per genus), so positivity at p is a Legendre-symbol identity | dead as stated: R(p) is a shifted divisor sum Σ_C D(4Cp+1), not multiplicative in p; finite fixed-level Eisenstein identities cannot certify ((J)7 Thm 9.1 via T1); growing level is open ((J)10: positivity is the spin event) | yes: (I)5, (J)7, (J)10, METAPLECTIC_ES |
| γ generation / expansion / strong approximation | Chen Markoff mod p (Thms 1.2.5–1.2.6), BGS Thm 1, BK / Shkredov / Zhang Zaremba | a group acts transitively or expands on a power-size set; Chen adds "every orbit size ≡ 0 mod p" (a ζ step) | dead: no infinite group acts on U_n(ℤ) (M3); ES₅ certificates have critical count ≍ log²p (F2) | yes: B2_ACROSS rows 1–2, ZAREMBA_TRANSFER, markoff_* (thin_group_orbits §4 outdated if Shkredov/Zhang stand, already flagged in (J)94) |
| δ rigidity / orbit classification | Margulis–Oppenheim, EMM98 Thm 2.1 | unipotent orbit closures are homogeneous; existence via a closed-or-dense dichotomy | dead: no unipotent action; ES targets exact integers, not small values; counts infinite / power | yes: technique_transfer_list (Lindenstrauss), z31_dynamics_ergodic |
| ε pigeonhole / collision (T) | Dirichlet; Thue → p = x² + y²; Pell; Spencer (partial colouring); Siegel's lemma | thick auxiliary set and fewer boxes; the witness is a *difference/quotient* of two colliding elements, so the **target is the identity** or a symmetric neighbourhood | dead: ES targets −1, and collisions give signed solutions (B4, §4 line 17); the class is tied to the exact height (F3, (J)85) | yes: LONGSHOT_PIGEONHOLE, DETERMINISTIC_EXISTENCE rows 1–2, s8_twisted_hyperbola_thue, z31_geometry_topology |
| ε′ inhomogeneous covering | Cauchy–Davenport (Alon Thm 3.2); Ramaré–Walker Thm 1.1 (product of 3 primes in *every* class mod q); covering radius | arbitrary targets are reached because the generating set is **dense** (all primes ≤ q^{16/3}; \|A\| + \|B\| > p) | dead: the generating set is the prime factors of ONE integer, Ω ≤ log₂N (F2); length ladder log q / √q / q; privacy forbids pooling across shifts | yes: z31_zero_sum, s6_divisor_pigeonhole, EXSET_CHAR_FORCING Lemma 2.2, SYNTHESIS_SPARKS8 Lemma 2.3 |
| ζ count congruence / parity (T) | Zagier windmill; Chevalley–Warning; restricted-variable Chevalley; Alon–Friedland–Kalai; Chen's orbit sizes ≡ 0 mod p | \|S\| ≢ \|Fix\| (mod q) on a **thick** set S. Zagier: "Only the last [assertion] requires that p be a prime of the form 4k+1", i.e. one local, prime-sensitive step | §2.1: on the (★) certificate sets themselves every level count is even and R(p)/2 mod 2 is a fair coin, so the congruence must live on a thick superset. Finite affine menus are barred ((J)2, INVOLUTION_ES2 Thm 5.1); non-affine thick windmills remain open | yes for involutions on X(p) (INVOLUTION_ES, WINDMILL_REDUCTION). CW only in polynomial_method (b3), whose "modulus ceiling" was retracted by errata; §2.1 closes that gap |
| η topological degree / fixed point | Brouwer, Borsuk–Ulam, Sperner; Zagier's own remark (Euler-characteristic parity) | continuous analogue of ζ | as ζ | yes: invol_topological (COLLAPSES to ζ) |
| θ compactness / covering with growing data | König, profinite compactness | finite obstructions ⇒ global obstruction | dead: profinite sterile set K ⊇ (Ẑ^×)² (B1/B5) | yes: noncounting_shapes |
| θ′ discharging (exact charge identity inside one object) | four-colour theorem (unavoidable set + discharging; NOT ACCESSED) | an exact Euler-type identity at each object forces a local configuration from a list | the within-p exact identities are the BM / genus layer (free pointwise, (J)103 Prop 2.2) and the Dedekind–HJ charge, which is χ-blind (§2.3). Finite configuration lists are fixed menus (B2(iii)) | **not screened as a mechanism**; ingredients in DEDEKIND_ES §2, SYNTHESIS_SPARKS9. §2.3 |
| ι induction with transport | EGZ (prime case + multiplicativity); Graham 1963 recursion; Ramsey recursions | the base case is easy and a transport law climbs | dead direction: ES(n) ⇒ ES(mn) descends to primes, which are the base case; no upward law found | yes: PROPAGATION_CLOSURE, TRANSPORT_LAW, AMPLIFY_EXCEPTION, z31_unit_fractions |
| κ Galois / fixed-modulus character event (R) | least prime outside a subgroup < (α(h)+o(1))log²q (GRH, LLS Thm 1.2); least primitive root (Shoup, via Moree); Linnik; Chebotarev least prime (Zaman); p = x² + ny² (Cox Thm 9.4, NOT ACCESSED) | the event is a Frobenius class at a FIXED modulus, so L-functions control every short window | gives exactly the parity / subgroup layer: CLASS_FORCING Thm 2.1, the cap relaxation (J)64 (−1 ∈ ⟨primes of K⟩). Class needs the box (§4 line 9) | yes: CLASS_FORCING, TWO_POWER_LADDER, CAP_POINTWISE, z31_small_count_pointwise |
| μ size / valuation squeeze (R) | Bang–Zsigmondy, BHV; Sylvester–Schur; Chebyshev/Bertrand; Erdős–Selfridge (non-existence) | a known integer of exactly known size whose "bad" primes are bounded by a valuation formula, so a good prime must exist | dead: bad primes for ES are unbounded; *prime* certificates already fail (the (★) prime-divisor subfamily fails at 94 primes < 10⁶, PRIMITIVE_INTERSECTION), and composite certificates are invisible to valuations | partly: z45_recent_pointwise_tools, PRIMITIVE_INTERSECTION (Zsigmondy/BHV); Sylvester–Schur not screened, adds nothing (privacy) |
| ν spectral / interlacing (T) | Huang Thm 1.1 (A_n² = nI, Cauchy interlacing); Hoffman/Delsarte clique bounds | an exact identity fixes the whole spectrum of a thick matrix; interlacing passes it to every large principal submatrix | §2.4: the ES sign condition is multiplicative, and multiplicative χ-cliques are cosets (no Hoffman bound); forest signings are gauge-trivial | partly: z45_interlacing_stable (MSS families); Hoffman / Huang-type: §2.4 |
| λ probabilistic + derandomisation | LLL; Erdős–Tetali designed bases; Spencer; conditional expectations | freedom to choose the object (M4) | dead: p is forced; conditional expectations need the fixed-p average ≥ 1, which is R(p) ≥ 1 | yes: prob_lll_fixed_p, z31_graphs_probabilistic, s9 |
| ξ main-term dominance after box enlargement | Vinogradov–Helfgott; Heath-Brown–Puchta Thm 1; Burgess; Linnik (L = 5.2); Lenstra–Schoof; Ramaré–Walker | expected count in the enlarged box is a power of n | dead: B-fin (the whole box is O(p²) and polylog), B3 | yes: CONDITIONAL_ES, z31_small_count_pointwise |
| failure side | Erdős p + 2^k (covering); Crocker/Pan p + 2^a + 2^b; Goldbach's other conjecture (5777, 5993); Ghosh–Sarnak Markoff (≥ √K/(log K)^{1/2} failures, numerics ≈ K^{0.8875}) | thin count + a covering or reciprocity mechanism ⇒ structured exceptions | ES has no BM obstruction at n ≥ 2, and its only structured exceptions are squares (T1). A "prime T1" is the only disproof shape ((J)97) | yes: s9, z31_small_count_pointwise, z38_markoff_precedent |

**Classes not yet screened as mechanisms before this file:** θ′ (discharging), the Hoffman/Huang part of ν, the
Sylvester–Schur part of μ, and Chevalley–Warning/restricted-variable CW as a *count congruence* within ζ. They are
treated in §2.1–§2.4, and the μ part above. None changes an earlier verdict. One scope remark: polynomial_method.md
(b3) claimed that "CN-type witnesses have moduli ≤ (log p)²", and its errata withdrew this. §2.1 replaces the claim by a
correct and narrower statement: count congruences on certificate sets are blind for a different reason, complement
pairing.

## §1 Catalogue (verified from sources)

(skeleton: per theorem — statement + theorem number, expected count at one n, mechanism class, ES admits it?)

## §2 Most promising untried mechanisms

(skeleton: 3–6 items, each: what it says for ES; first lemma; why §3/§4/§6 doesn't kill it; how it fails; numerics)

## §3 Hostile review record

(skeleton)

## §4 Not accessed / leads that were wrong

(skeleton)
