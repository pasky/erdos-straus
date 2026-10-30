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

Verification key. **V** = statement read by me in the source; the excerpt file is in `sources/z52/thin_pointwise/`,
accessed 2026-10-30. **V2** = read by me in a later paper that restates it; that paper is named. **Vs** = read by a
subagent and saved to the excerpt file, with spot checks by me. **R** = verified earlier in the repository (file named).
**NA** = NOT ACCESSED, classical statement given for orientation only. "Count" is the expected or exact number of
witnesses at one n. "Class" refers to §0.

| # | statement (source, theorem no.) | ver. | count at one n | class | does ES admit the mechanism? |
|---|---|---|---|---|---|
| 1 | Every prime p ≡ 1 (4) is x² + y². Zagier, AMM 97 (1990) 144: an involution on the finite set S = {(x,y,z) ∈ ℕ³ : x² + 4yz = p} has exactly one fixed point, (1,1,k), so \|S\| is odd and (x,y,z) ↦ (x,z,y) has a fixed point. "Only the last [assertion] requires that p be a prime of the form 4k+1." | V (`01-zagier.txt`) | 1 unordered rep.; \|S\| is thick | ζ (T) | Only via a thick superset with one prime-sensitive local step. On (★) sets the parity is uninformative (§2.1). INVOLUTION_ES Prop 2.3: \|X(q²)\| is odd for the O152 set |
| 2 | Thue's lemma ⇒ two squares (Brillhart, Math. Comp. 26 (1972) 1011) | NA (`02-thue-brillhart.txt`) | O(1) | ε | Needs a definite form; ES's quadratic pieces are split (DETERMINISTIC_EXISTENCE row 1) |
| 3 | Lagrange four squares; Cauchy–Davenport was "applied … to give a new proof to a lemma of Lagrange" (Alon, CN, after Thm 3.2) | V2 (`alon_cn.txt`) for the CD link; Jacobi's r₄ NA | 8σ(n) for odd n (NA) | α+β, ε′ | not thin |
| 4 | Gauss: n = x² + y² + z² ⟺ n ≠ 4^a(8k+7) (Choi–Kumchev–Osburn §1) | Vs (`04-three-squares.txt`) | ≍ n^{1/2±ε} (class-number formula NA) | β | not thin (B3) |
| 5 | Duke–Schulze-Pillot, Invent. Math. 99 (1990): large n represented by the spinor genus are represented by the form; ineffective (Siegel) | V2 (`dsp_via_6cores.txt`; the original theorem text was not opened) | ≍ n^{1/2} | β | not thin; spinor/genus steps are true at squares (T1, §4 line 1) |
| 6 | Ono–Soundararajan, Invent. Math. 130 (1997): x² + y² + 10z² under GRH | NA (`06-ono-soundararajan.txt`) | ≍ n^{1/2} | β | not thin |
| 7 | Bhargava–Hanke 290-theorem, Thm 1 (29 critical integers); §4.2–4.3: Eisenstein lower bounds vs cusp upper bounds, then a finite check | Vs (`07-fifteen-290.txt`) | power | β+θ | not thin |
| 8 | Pell existence; negative Pell for primes p ≡ 1 (4) (Legendre) | NA (`08-pell.txt`) | one fundamental solution | ε (+ genus for −1) | DETERMINISTIC_EXISTENCE §4: the Pell splitting factors the discriminant, not N_θ(p) |
| 9 | p = x² + ny² ⟺ p splits completely in the ring class field (Cox, Thm 9.4) | NA (`10-cox.txt`) | O(1) | κ (R) | ES is not a Frobenius condition (B1; CLASS_FORCING Thm 2.1) |
| 10 | Hasse–Minkowski; Meyer (rank ≥ 5 indefinite isotropic) | NA | rational points, infinite | κ | rational ES points are trivial; integrality is the whole content (GEOMETRY_ES §1) |
| 11 | GRH: the least prime outside a subgroup H of (ℤ/q)^×, index h, is < (α(h)+o(1)) log²q, α(2) = 0.8 (Lamzouri–Li–Soundararajan, arXiv:1309.3595v3, Thm 1.2); Ankeny O(log²q), Bach < 2 log²q (as stated in LLS §1.1) | V (`lls_least_qnr.txt`) | ≍ log²q window, polylog | κ | yields the QNR / subgroup layer only. Under GRH, "(q/p) = −1 for some prime q ≤ 2 log²p ⇒ ES(p)" is *equivalent* to ES for large p (CONTEXT) |
| 12 | Linnik: P(a,q) ≪ q^L, L = 5.5 (Heath-Brown), L = 5.2 (Xylouris, Acta Arith. 150 (2011) 65–91), as stated in LLS §1.2; GRH (Bach–Sorenson): P(a,q) ≤ (1+o(1))(φ(q) log q)² | V2 (`lls_least_qnr.txt`); the L = 5 thesis claim NA | power window | ξ / κ | F3: ES's modulus is tied (§4 line 4) |
| 13 | Least prime ideal in Chebotarev: N𝔭 ≪ d_L^{40}, effective (Zaman, arXiv:1508.00287v3 abstract); LMO79 NA | V (`zaman_chebotarev.txt`) | power | κ / ξ | as 12 |
| 14 | Least primitive root: Burgess g(p) = O(p^{1/4+ε}); GRH (Shoup): g(p) ≪ ω(p−1)⁴(log ω(p−1)+1)⁴ log²p; i.o. g(p) > c log p log₃p (Moree survey, arXiv:math/0412262v2 §27) | V2 (`moree_artin.txt`) | polylog under GRH | κ | as 11 |
| 15 | Heath-Brown 1986: at most two primes q for which P(q) (primes with primitive root q) is finite; g(p) ≤ 7 for infinitely many p (Moree, §§ on Heath-Brown) | V2 (`moree_artin.txt`) | n/a | infinitude, **not pointwise** | B6: a statement about infinitely many p. The "one of three" disjunction is a fixed finite menu (B2(iii)) |
| 16 | Heath-Brown–Puchta, Asian J. Math. 6 (2002), Thm 1: every large even n is a sum of two primes and exactly 13 powers of 2 (7 under GRH, Thm 2) | Vs (`hb_puchta_2002.txt`) | power (Goldbach part) | ξ | F2 (B3) |
| 17 | Ternary Goldbach, Helfgott arXiv:1501.05438 (book; supersedes 1312.7748) | V (`helfgott_ternary.txt`, abstract) | ≍ n²/log³n | ξ | not thin |
| 18 | Ramaré–Walker, arXiv:1610.05804, Thm 1.1: for q ≤ x^{1/16}, every invertible class mod q contains a product of three primes < x^{1/3}. Proof: Brun–Titchmarsh + additive combinatorics, no parity barrier | V (`ramare_walker.txt`) | power | ε′ / ξ | **closest inhomogeneous-target analogue of gate G4**: any target class, modulus arbitrary, but the generating set is *all* primes up to q^{16/3}. ES's generating set is the ≤ log₂N prime factors of one integer (§2.2) |
| 19 | Chevalley–Warning: Σd_i < n ⇒ #Z ≠ 1, p \| #Z, and Z ≠ ∅ ⇒ #Z ≥ q^{n−d} (Bishnoi–Clark arXiv:2201.11236v1 Thm 1.1; Alon CN Thm 3.1). Ax–Katz NA | V | count ≡ 0 mod p, so ≥ p once one zero is known | ζ | §2.1 |
| 20 | Restricted-variable Chevalley (Schauz 2008, Brink 2011): (q−1)Σdeg f_j < Σ(\|X_i\|−1) ⇒ #Z_X ≠ 1 (Bishnoi–Clark Thm 1.3b) | V | ≥ 2 | ζ | §2.1 |
| 21 | Combinatorial Nullstellensatz Thm 1.2; Cauchy–Davenport Thm 3.2; Alon–Friedland–Kalai: average degree > 2p−2 and max degree ≤ 2p−1 ⇒ p-regular subgraph (Alon, CPC 8 (1999), Thm 6.1) | V (`alon_cn.txt`) | ≥ 1 | ζ / ε′ | §2.1, §2.2 |
| 22 | Erdős–Ginzburg–Ziv; Olson D(G) for p-groups; ±-weighted Davenport ⌊log₂n⌋+1 (ACFKP) | NA (the repo copy `sources/lit2026g/acfkp.txt` also records non-verification) | ≥ 1 | ζ + ι | zero-sum gives the identity, not −1 (z33_target_davenport; EXSET_CHAR_FORCING Lemma 2.2) |
| 23 | Huang, Ann. of Math. 190 (2019), arXiv:1907.00847v2, Thm 1.1 (every induced subgraph of Qⁿ on 2^{n−1}+1 vertices has max degree ≥ √n) via Lemma 2.2 (A_n² = nI) + Cauchy interlacing | V (`huang_sensitivity.txt`) | ≥ 1 vertex | ν (T) | §2.4 |
| 24 | Spencer 1985: any n sets on n points have a colouring of discrepancy ≤ 6√n; original proof existential (Lovett–Meka arXiv:1203.5747v2, abstract and Thm 1) | V2 (`lovett_meka_spencer.txt`) | exponentially many colourings | ε (entropy pigeonhole) / λ | M4: the colouring is free; target symmetric |
| 25 | Cilleruelo–Luca–Baxter, arXiv:1602.06208v2, Thm 1.2: every positive integer is a sum of three base-g palindromes, g ≥ 5; "The proof of Theorem 1.2 is algorithmic" | V (`clb_palindromes.txt`) | ≍ n^{1/2} (≍ n^{1/2} palindromes ≤ n, triples ≍ n^{3/2}) | α | not thin; digit-carry algorithms are inside B1 Thm M |
| 26 | Croot 2003 (colouring version) and Bloom (positive upper density ⇒ finite S with Σ1/n = 1), Bloom arXiv:2112.03726v2, Thms 1–2 | V (`bloom_croot.txt`) | many | λ / M4 | M4 (z31_unit_fractions) |
| 27 | Bang–Zsigmondy; Bilu–Hanrot–Voutier (Lucas/Lehmer terms of index > 30 have primitive divisors) | R (`BRAINSTORM/z45_recent_pointwise_tools.md` §B, via Voutier/Stewart) | ≥ 1 | μ / κ (R) | wrong integer and wrong class (+1 or ±1 mod t); PRIMITIVE_INTERSECTION |
| 28 | Sylvester–Schur; Erdős–Selfridge | NA | ≥ 1 / non-existence | μ | §0 μ row |
| 29 | Four-colour theorem (RSST 1997: unavoidable set + discharging) | NA (Gonthier's Notices article could not be fetched) | ≥ 1 colouring | θ′ | §2.3 |
| 30 | Ore conjecture (LOST 2010): every element of a finite non-abelian simple group is a commutator | NA | ≈ \|G\| | β (Frobenius formula) | not thin |
| 31 | Lenstra–Schoof 1987, primitive normal bases exist for every E/F (Cohen–Huczynska arXiv:math/0610400v2, abstract) | V2 (`cohen_huczynska_lenstra_schoof.txt`) | power | ξ (+ computation) | not thin |
| 32 | Zaremba. Bourgain–Kontorovich Thm 1.2 (almost every q, arXiv:1107.3776); Shkredov Cor 1 (every prime / squarefree q), arXiv:2603.14116v2 (24 Jun 2026); X. Zhang Thm 1.2 (all q), arXiv:2605.02518v2 (8 May 2026), unrefereed | V (BK); R + version check (`zaremba_2026_versions.txt`, repo `sources/lit2026g/shkredov_zaremba2026.txt`) | q^{2w_M−1}, a power | γ | F2: ES₅ is critical, ≍ log²p ((J)94, ZAREMBA_TRANSFER) |
| 33 | Markoff mod p. Chen, Ann. of Math. 199 (2024), arXiv:2011.12940v2, Thm 1.2.5: every Γ-orbit on X*(p) has size divisible by p. Thm 1.2.6: the BGS exceptional set is finite, and strong approximation holds at all other p. BGS arXiv:1607.01530 Thm 1: a giant orbit, with \|X*(p) − C(p)\| ≤ p^ε | V (`chen_markoff.txt`, `bgs_markoff.txt`) | \|X*(p)\| ∼ p² | γ + ζ | wrong axis: this is the connectivity of one surface mod p, not existence over a family (B2_ACROSS row 2) |
| 34 | Ghosh–Sarnak, arXiv:1706.06712v3, (1.6): Σ_{\|k\|≤K} h_M(k) ∼ C± K (log K)². Thm 1.2(i): ≥ √K (log K)^{−1/2} Hasse failures. (1.7): numerically ≈ C₀K^{0.8875}. Remark 1.3(a): the failures of Prop 8.1(iii) use reciprocity + Markoff descent and are not explained by integral BM | V (`ghosh_sarnak.txt`) | (log k)² on average, the same scale as ES | failure side | ES's precedent at its own scale: polylog count, no BM explanation, power-many failures. ES has none to 10¹⁸ (z38_markoff_precedent) |
| 35 | Harpaz, arXiv:1511.04876v2, Thm 1.0.1: for the pencil (c₁t+d₁s)(c₂t+d₂s)x² + (c₃t+d₃s)(c₄t+d₄s)y² = 1 over ℤ_S (S ∋ 2, ∞), if seven explicit square classes are F₂-independent, then Y has an S-integral point | V (`harpaz_conic_logk3.txt`) | — | κ + descent–fibration | the only verified existence theorem for a log K3 family. It is S-integral with hypotheses on coefficient square classes; ES's U_n is log K3 (Bright–Loughran, `bright_loughran_logk3.txt`) but not of this shape (B2_ACROSS row 6) |
| 36 | Margulis/EMM: for Q of signature (p,q), p ≥ 3, q ≥ 1, not proportional to a rational form, N_Q(a,b,T) ∼ λ(b−a)T^{n−2} (EMM98 Thm 2.1, as restated in Margulis–Mohammadi arXiv:1001.2756v1 Thm 1.1) | V2 (`margulis_mohammadi_oppenheim.txt`) | T^{n−2} | δ | not thin; no group |
| 37 | Erdős 1950: an AP of odd n with no n = 2^k + p (covering congruences); Crocker 1971 (p + 2^a + 2^b, infinitely many odd exceptions); Pan 2011 (≫ x^{1−ε} exceptions) | R (s9 ✓-marks, R282; `sources/lit2026g/erdos_2kp.txt`, secondary) | ≍ 1 and ≍ log n | failure side | coverings act on the fixed orbit k ↦ 2^k; ES's sets move with n (B2) |
| 38 | Goldbach's other conjecture: the odd numbers not of the form p + 2k² (k > 0) are 1, 3, 17, 137, 227, 977, 1187, 1493, 5777, 5993; next > 10⁹ if it exists (OEIS A060003, citing Hodges 1993) | V (`oeis_A060003_goldbach_other.txt`); Hodges' paper NA | ≍ √n/log n, a **power** | failure side | calibration: even a power-size expected count without a covering obstruction does not guarantee every n. Only finitely many failures are known; nothing structured |
| 39 | Sierpiński numbers (k·2ⁿ + 1 composite for all n; 78557) | NA | — | failure side (covering) | B1-type |
| 40 | Erdős–Tetali 1990 (bases with r(n) ≍ log n) | R (s9) | log n | λ / M4 | designed set |

**Reading of the catalogue** (Assessment). Rows with a *thin* count *and* a proof are 1, 2, 8, 9, 11, 14, 19–24 and 27.
Every one of them is (T) or (R). The (T) rows (1, 2, 8, 19–24) all run on a thick object: S(p), a √p-box, F_q^n, 2^{n−1}+1
vertices, n sets. The (R) rows (9, 11, 14, 27) all have a fixed modulus or a cyclotomic integer. Rows 34, 37 and 38 show
the default outcome for thin counts without (T) or (R): exceptions, sometimes power-many (34) and sometimes with no
visible structure (38). Rows 18 and 33 are the nearest structural cousins of ES's two forms. Row 18 is the inhomogeneous
subset-product target of gate G4, solved only because the generating set is dense. Row 33 is "every orbit is large",
solved by a count congruence (orbit size ≡ 0 mod p) on a thick set. ES has neither a dense generating set nor an orbit
structure. Since (J)103 this adds one fact: the Markoff precedent (row 34) has *power-many* failures at ES's own
log²-scale, numerically ≈ K^{0.8875}, of which only O(√K) are explained algebraically (GS Remark 1.3(a)). The
problem class therefore does not guarantee existence; ES's empirical robustness (no failure to 10¹⁸, minimum 612
solutions on cheap slices at 10¹⁸–10²⁵) is a property of ES, not of the class.

## §2 Most promising untried mechanisms

**Bottom line first** (Assessment). Among the classes of §0 I found no untried mechanism with a credible route to ES.
The generator matrix (§2.0) shows that every cell is either screened by an earlier file or already one of the repo's
known open loopholes. §2.1–§2.4 work the four cells that had not been screened to a first lemma with a numerical check.
All four close, with precise reasons. Promise ratings are honest, and all are low.

### §2.0 Generator matrix: thick objects at a fixed prime p × extraction rules

A (T)-type proof needs a thick deterministic object built from p, an exact local extraction rule, and a step that is
false at odd squares (§4 line 1). Rows are the thick objects available at p; columns are the rules. Each cell names the
file that screened it, "§2.x" for cells worked here, or **open**.

| thick object at p (size) | collision | parity / count congruence | descent | spectral / interlacing | exact identity / charge | inhomogeneous covering | orbit / expansion | squeeze |
|---|---|---|---|---|---|---|---|---|
| O1 trial pairs 𝓡 = {(u,C)} (≍ p log p) | PARITY_AUDIT (tied modulus) | §2.1 | — | PARITY_AUDIT §2 (Weil error p^{1/2}) | SINGLE_P_COUNT genus split; BM_CORRECTED | — | — | — |
| O2 divisor sets of N_C = 4Cp+1, C ≤ p (each τ(N_C) small; union thick, but large primes are private) | LONGSHOT_PIGEONHOLE (signed only) | §2.1 | — | z45_interlacing_stable (stability lost) | **open** at growing level ((J)10) | z31_zero_sum, EXSET_CHAR_FORCING L2.2, §2.2 | — | PRIMITIVE_INTERSECTION, §0 μ |
| O3 hyperbola 𝓗: xy ≡ 1 (4p) (≍ p) | SYNTHESIS_SPARKS8 §1.7 (Thue wall) | — | — | PARITY_AUDIT (Kloosterman) | — | (J)85 (sub-power windows needed) | — | — |
| O4 HJ / CF data {p/a} with χ_p (p) | bsA_farey_lnr_pigeonhole | WINDMILL_REDUCTION (windmill = Conway-river symmetry) | LOWER_TAIL_ASTRA (forest; fixed roots fail under Dickson) | §2.4 | DEDEKIND_ES §2, §2.3 | — | ZAREMBA_TRANSFER (critical count) | — |
| O5 class groups / forms of disc −4p, p; p = ππ̄ in ℤ[i] (≍ √p) | DETERMINISTIC_EXISTENCE §4 (Pell) | — | noncounting_shapes (Fermat descent: shape constraint) | — | DETERMINISTIC_EXISTENCE row 7 (genus) | — | QUATERNION_ES, (J)33 | PROPAGATION_CLOSURE (Gaussian coordinates: visibility, not class) |
| O6 lattices L_ρ(g) (ASTRA_BRIDGE) | z31_geometry_topology | — | — | — | — | (J)85 | — | — |
| O7 Zagier-type sets with an ES-shaped windmill (X(p) of O152) | — | INVOLUTION_ES(2): finite affine menus barred; **open** for non-affine or infinite menus | — | — | — | — | — | — |
| O8 SL₂ words / theta multiplier (Question R) | — | — | — | — | METAPLECTIC_ES | — | thin_group_orbits, QUESTION_R | — |

Reading (Assessment): the only **open** cells are the two the repository already lists as loopholes. One is growing-level
exact identities ((J)10: the positivity is the spin event). The other is non-affine windmills (INVOLUTION_ES2). No new open
cell turned up. Two uses as a generator:
1. Any new thick object at p (a row) should be run against all eight columns before anything else.
2. Any new extraction rule (a column) should be run against O1–O8.

The matrix is the deliverable of goal (b) of this wave for lane D.

### §2.1 Count congruences: Chevalley–Warning, Ax–Katz, restricted variables, Zagier-type parity (class ζ)

*What it would say.* Some count attached to p is ≢ 0 modulo a prime q, and the count is over a set whose non-trivial
elements are certificates. That forces a certificate with no main term at all: count ≥ 1, as in Zagier, Chevalley's
"#Z ≠ 1", and Chen's "orbit size ≡ 0 mod p".

*The brief's question* is whether ES has a polynomial formulation with #vars > degree, and what would lift a mod-p
solution to a positive integer one. Two answers.

**Lemma 2.1 (PROVED, elementary).** Let n be odd, t ≡ 0 (mod 4), N = tn + 1 = ∏ ℓ_i^{a_i}, G = (ℤ/t)^× = G₂ × G_odd
(2-part and odd part), and let
E_t(n) = {e ∈ ∏[0, a_i] : ∏ ℓ_i^{e_i} ≡ −1 (mod t)} (the level-t (★) certificates).
* (a) *Complement pairing.* e ↦ a − e is a fixed-point-free involution of E_t(n). Hence #E_t(n) = D_t(n) is even, and so
  is R(n) = Σ_C D_{4C}(n).
* (b) *−1 lives in G₂.* The odd-part condition π_odd(∏ ℓ^e) = π_odd(−1) = 1 is homogeneous: e = 0 solves it. Hence a
  q-adic count congruence for odd q (Chevalley–Warning over F_q, Olson or Davenport in q-groups) can force non-trivial
  solutions of the *odd-part* condition only. Whether the class is −1 rather than +1 is decided entirely in the 2-group
  G₂.
* (c) *No lift is needed in the divisor encoding; the cubic encoding has #vars = degree.* A certificate e gives a positive
  integral (★) triple directly: d = ∏ ℓ^e, u = (d+1)/t, B = (N/d + 1)/t, C = t/4, as in FRONTIER §2.1. In the raw
  equation F = 4uBC − u − B − p (3 variables, degree 3) Chevalley–Warning needs d < n and fails. The
  restricted-variable theorem (Bishnoi–Clark Thm 1.3b) fails too: with X_i ⊆ F_q its hypothesis
  (q − 1)·3 < Σ(|X_i| − 1) ≤ 3(q − 1) can never hold. So every formulation with #vars > degree must add variables.
  The natural one is the exponent/divisor encoding above, where the target is already a congruence and (a)–(b) apply.

*Proof.* (a) A fixed point has 2e = a, so d² = N with d ≡ −1 (t). Then d = tu − 1 and t²u² − 2tu + 1 = tn + 1, so
n = tu² − 2u is even, a contradiction. (b) −1 has order 2, so π_odd(−1) = 1. (c) |X_i| ≤ q for subsets of F_q. ∎

*Consequence (Assessment).* By (a) and (b), a count congruence on the full exponent box is either odd-q, which is blind
to ±1, or mod 2, where (a) makes it vacuous. Restricted variables can break the complement symmetry: restrict to
d < √N, which gives D_t/2 at each level and R/2 in total. Then a mod-2 law would need R(p)/2, or some level-wise half
count, to have forced parity at primes p ≡ 1 (4); it is 0 at odd squares.

*Numerical check* (EVIDENCE; `scripts/z52_thin_parity.c`, outputs in `data/z52_thin/parity_*.txt`). Over n ≡ 1 (4):
* (a) holds with no exception: every D_C(n) is even, n ≤ 20001 and n ∈ [10⁶, 1.04·10⁶].
* R(p)/2 is odd for 561/1125 primes ≤ 20001 (0.499) and for 751/1473 primes in [10⁶, 1.04·10⁶] (0.510). For composite
  non-squares the rate is 0.48–0.50.
* v₂(R(p)) is spread over 1–6, roughly geometrically (window 10⁶: counts 751, 383, 158, 56, 122, 3 for v₂ = 1…6).
* So no parity or 2-adic law holds at the (★) layer, consistent with the exact failures (R = 0 at 409, 577, 5569, 9601,
  all reproduced).

*Why §3/§4/§6 do not kill the class outright.* Line 1 is passable, because Zagier's prime-sensitive step is a
uniqueness-of-fixed-point step, which is false at squares. The (J)2 / INVOLUTION_ES2 barrier covers finite affine
menus only.

*How it fails here.* By Lemma 2.1 and the data, the congruence cannot live on certificate sets or their natural halves.
It must live on a **thick superset** S(p) ⊋ certificates (Zagier's S has \|S\| ≫ √p) with a second involution whose
unique fixed point exists only at primes. That is exactly INVOLUTION_ES's open non-affine case. This section adds
nothing that makes that case more likely.

*First problem if someone insists:* exhibit any thick S(p), with an explicit involution σ, such that \|Fix σ\| is odd
for all primes p ≡ 1 (4) below 10⁴ and Fix(τ) ⊆ ES certificates for a second involution τ. A computer search over
piecewise-linear involutions with p-dependent breakpoints on the O152 set is the cheapest test.

**Promise: 1/10.**

### §2.2 Zero-sum with a chosen level: Davenport/Olson with AGP freedom, gate G4 (classes ε′, ζ)

*What it would say.* Alford–Granville–Pomerance get subset products ≡ 1 by choosing a modulus whose unit group has small
exponent, so that the Davenport constant is small. ES can choose its level t = 4C freely (p is forced; t is not). So:
choose t such that the prime factors of N_t = tp + 1 must contain a subset with product ≡ −1 (mod t).

**Lemma 2.2 (PROVED, elementary).**
* (a) For every L, the set of t with exp((ℤ/t)^×) \| L is finite: every prime power q^e \| t needs λ(q^e) \| L. So any
  zero-sum certificate at bounded exponent uses a **fixed finite menu** of levels. Such menus fail for infinitely many
  p ≡ 1 (24) under Hypothesis H (B2, Thm 2.2(iii); (I)8). Exponent 2 means exactly t \| 24, i.e. Mordell's levels.
* (b) At an exponent-2 level the divisor-residue set equals the subgroup ⟨ℓ_i⟩, which equals the F₂-span of the ℓ_i
  (DETERMINISTIC_EXISTENCE Prop 3.3(b)). So linear algebra over F₂ decides the event exactly. At every level,
  HIT ⇒ SUB ⇒ GEN, where:
  * HIT: some d \| N_t with d ≡ −1;
  * SUB: −1 ∈ ⟨ℓ_i⟩;
  * GEN: −1 ∈ F₂-span of the ℓ_i in G/G² (the genus layer).

*Proof.* (a) λ(q^e) is divisible by q − 1 and, for odd q, by q^{e−1}; λ(2^e) = 2^{e−2} for e ≥ 3. So λ(q^e) | L bounds
both q and e. (b) A divisor ≡ −1 is a product of the ℓ_i; reduce
modulo G². ∎

*Numerical check* (EVIDENCE; `scripts/z52_thin_levels.py`, `data/z52_thin/levels_1e5.txt`; all p ≡ 1 (4) in
[10⁵, 1.03·10⁵], C ≤ 60):

| levels | (p, C) pairs | SUB | GEN | HIT |
|---|---|---|---|---|
| exponent-2 levels | 536 | 0.433 | 0.433 | 0.433 (as (b) forces) |
| all other levels | 7504 | 0.320 | 0.347 | 0.062 |

So off the exponent-2 levels the genus layer, which is all that F₂ zero-sum arguments see, passes 5.6× more often than
the true event. 28.6 % of (p, C) pairs are genus-passing misses.

*Why §3/§4 do not kill it outright.* At *unbounded* exponent the menu grows with p, so this is hatch H-A or E1.

*How it fails* (Assessment). Growing the exponent grows the 2-rank of G, which is ω(t) + O(1). The certificate then needs
the ≈ log log p prime factors of one N_t to reach −1 inside an F₂-space of growing dimension, then the class inside the
genus coset (factor 5.6 above). Privacy (SYNTHESIS_SPARKS8 L2.3) forbids pooling across levels. The only zero-sum
theorem with an arbitrary target in the catalogue is Ramaré–Walker (row 18), and it needs the generating set to be *all*
primes up to q^{16/3}.

*Answer for gate G4.* Davenport, Olson and EGZ certify the identity. With the target −1 they see the F₂-span, and that is
exact only at t \| 24. This sharpens z33_target_davenport (η(G) = 0 only at exponent 2) with a measured gap.

**Promise: 1/30.**

### §2.3 Discharging: an exact charge identity inside one prime (class θ′, not screened before)

*What it would say.* In the four-colour theorem, an exact Euler identity holds at every planar graph, and local
redistribution forces a configuration from a finite list. For ES the analogue would be an exact identity over the thick
object O4 (all a mod p), Σ_a w(a) = W(p) with W(p) > 0 at primes and = 0 at squares, and with w(a) > 0 only when a is a
certificate (a QNR with HJ-length(p/a) ≤ 3; DEDEKIND_ES Cor 4.6).

**Lemma 2.3 (PROVED relative to the Hirzebruch–Zagier/Barkan–Hickerson–Knuth formula, stated in DEDEKIND_ES §2 and
re-checked numerically here).** Let p ≡ 1 (4) be prime, p/a = [[b₁, …, b_r]] the minus continued fraction, and
c(a) = Σ_i (b_i − 3) the HJ charge. Then
  Σ_{a QNR} c(a) = Σ_{a QR} c(a) = −(p − 1)/2.
More generally, for any function c on (ℤ/p)^×, Σ_a χ_p(a) c(a) = Σ_a χ_p(a) c⁺(a), where c⁺(a) = (c(a) + c(p − a))/2.

*Proof.*
* 12 s(a,p) = c(a) + (a + a*)/p, where a·a* ≡ 1 (mod p).
* s(p − a, p) = −s(a,p) and χ_p(−1) = 1 for p ≡ 1 (4), so Σ_{a QNR} s(a,p) = 0, and likewise over the QRs.
* The QNRs are closed under a ↦ p − a and a ↦ a*, so Σ_{a QNR} (a + a*)/p = 2 · (p(p−1)/4)/p = (p − 1)/2.
* The QR case is identical.
* The general statement is the pairing a ↔ p − a.
∎

*Numerical check* (EVIDENCE; `scripts/z52_thin_dedekind.py`, `data/z52_thin/dedekind_le700.txt`): the BHKZ identity
holds for every a and every prime p ≡ 1 (4) with p ≤ 700, with zero violations. Σ_{QNR} 12 s = 0 and both charge sums
equal −(p−1)/2, as proved. For orientation, the ES₅ certificate counts E5(p) are 2 to 26 in this range.

*How it fails* (Assessment).
* The natural charge is χ-blind: its odd part cancels.
* Even charges are character sums Σ χ(a) c⁺(a). Their exact evaluation is the BM / T(p) layer, already free pointwise
  ((J)103 Prop 2.2, Burgess).
* A positive χ-weighted total does not localise onto the length-≤ 3 set. Discharging also needs a *local* move: a rule
  sending charge from a non-certificate a to a neighbour, with "positive final charge ⇒ certificate". The HJ/Stern–Brocot
  neighbourhoods do not see χ (Lemma 2.3 is the simplest instance).
* Finite configuration lists would be a fixed menu (B2(iii)).

**Promise: 1/30.** Not new in ingredients (DEDEKIND_ES); new only as a closed mechanism class.

### §2.4 Exact-spectrum interlacing (Huang) and Hoffman–Delsarte forcing (class ν)

*What it would say.* Huang fixes the whole spectrum of a thick signed matrix by an exact identity (A_n² = nI), and Cauchy
interlacing forces every principal submatrix on more than half the vertices to have a large eigenvalue, hence a vertex
of high degree. The Paley analogue: the Hoffman bound says a set of residues all of whose differences are QRs has
size ≤ √p. An ES version would force a χ-sign change, i.e. a certificate (Theorem A: certificate ⟺ (uv/p) = −1), inside
any sufficiently large p-dependent set.

**Lemma 2.4 (PROVED, elementary).**
* (a) A ⊆ F_p^× satisfies χ_p(ab) = 1 for all a, b ∈ A iff A lies in one coset of the QR subgroup. Such A can have size
  (p − 1)/2, so no Hoffman/Delsarte or interlacing bound forces a *product-type* sign change.
* (b) Additive form of the words: p = tuv − u − v gives ū + v̄ ≡ t (mod p), and the certificate condition is
  χ_p(ū v̄) = −1. For fixed t the relation x ~ t − x is a perfect matching, with trivial spectrum. For the additive Paley
  structure, Hoffman needs sets of size > √p.

*Proof.* (a) Fix a₀ ∈ A. Then χ(a) = χ(a₀) for all a ∈ A. (b) From tuv = p + u + v ≡ u + v (mod p). ∎

*Numerical check* (EVIDENCE; `scripts/z52_thin_words.py`, `data/z52_thin/words.txt`). All words p = tuv − u − v
(t, u, v ≥ 1) were enumerated, and ū + v̄ ≡ t was asserted for each.

| p | words | words with (uv/p) = −1 | max words at one level t | √p |
|---|---|---|---|---|
| 409 | 39 | 8 | 12 | 20 |
| 2521 | 37 | 4 | 8 | 50 |
| 66529 | 69 | 18 | 8 | 258 |
| 1000033 | 175 | 116 | 16 | 1000 |

So the word sets are far below the √p scale at which Hoffman-type forcing starts. (The count includes t = 1, 2 words.
Theorem A's certificate criterion is quoted, not re-proved, and the column is illustrative.)

*How it fails.* The ES sign condition is multiplicative, so (a) applies. The forest signing is gauge-trivial
(z45_interlacing_stable). The additive reformulation has polylog-size fibres. A Huang-type proof would need a thick
matrix with an exact spectral identity *and* certificates as its large-degree witnesses. No candidate is known, and
§2.0 row O4 lists the thick χ-objects that exist.

**Promise: 1/50.**

### §2.5 What a successful mechanism would have to look like (Assessment, distilled from §0–§2.4)

Any proof must combine three things:
1. A *thick* deterministic object built from p, of size ≥ p^c.
2. An *exact* extraction rule that outputs a tied-modulus certificate (§4 line 4), not an identity-target collision and
   not a subgroup or genus statement.
3. A step that is false at odd squares and true at primes, as Zagier's "exactly one fixed point" is.

The catalogue contains no theorem that delivers item 2 for a target outside a small subgroup, except via a dense
generating set (Ramaré–Walker) or an orbit structure (Chen). ES has neither. Absent a new extraction rule, the honest
forecast is that a proof will not come from transplanting a known thin-regime mechanism.

## §3 Hostile review record

(skeleton)

## §4 Not accessed / leads that were wrong

(skeleton)
