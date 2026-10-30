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

(skeleton: 3–6 items, each: what it says for ES; first lemma; why §3/§4/§6 doesn't kill it; how it fails; numerics)

## §3 Hostile review record

(skeleton)

## §4 Not accessed / leads that were wrong

(skeleton)
