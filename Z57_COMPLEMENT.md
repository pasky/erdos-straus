# Z57_COMPLEMENT — are the failure sets of different certificate families complementary at one prime?

Status: z57 lane COMPLEMENT (brief `z52bbriefs/z57_lanes.md` §COMPLEMENT, rules `z53_depth.md`). Internal, internally
reviewed only. **ES is OPEN; nothing here proves or disproves ES, (★), or any family's positivity at any infinite set of
primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts
`scripts/z57_complement_*`, data `data/z57/complement/`.

*(CHECKPOINT 1 — skeleton; sections marked TODO are filled in later.)*

## 1. Statements attacked

p ≡ 1 (mod 4) prime, L = log p. **The word set** W(n) := {(t, u, v) ∈ ℕ³_{≥1} : tuv − u − v = n} (ordered; (t,u,v) and
(t,v,u) are distinct unless u = v). For t, u, v ≥ 2 the word is the length-3 Hirzebruch–Jung fraction n/A = [[v,t,u]],
A = tu − 1 (`DEDEKIND_ES.md` Lemma 1.1). **The menu 𝓜** (every family is a set of words of W(p) or of W(cp)):

| family | words | meaning (source) |
|---|---|---|
| STAR | 4 \| t | (★) = ET Type II c = 1; (u, B, C) = (u, v, t/4); R_STAR = R(p) (FRONTIER §2.1) |
| G = 𝔊*, K | STAR with Q⁴ > P·p, resp. not (P, Q = min, max of u, v) | `Z56_FAMDESIGN` Thm V family and its Burgess corner |
| H3, HC | STAR with 64C³ ≤ p, resp. C ≤ ⌊L²⌋ | complete levels; HC words (Z56_FAMDESIGN §6) |
| B1 | 4 \| u or 4 \| v | López Type A / the b = 1 line, 4xy \| p + 4x + y (`B1_LINE.md`); R_B1 = 2·N₁ |
| I1 | 4 \| tu − 1 or 4 \| tv − 1 | ET Type I, slice a = 1 (`CONDITIONAL_ES` Lemma 1.1), incl. boundary words |
| QR | t, u, v ≥ 2, none of the above | Jacobi (A/p) = +1 words — **not certificates; placebo family** |
| c2, c3 | words of W(cp) with 4c \| t | ET Type II c-lines c = 2, 3 (4abcd − a − b = cp) |
| X_z | any of the above restricted to the level band z = log t / L ∈ [k/10, (k+1)/10) | sub-families with non-trivial zero rates |

For p ≡ 1 (4) and t, u, v ≥ 2, `DEDEKIND_ES.md` Thm 4.5 says (A/p) = −1 ⟺ the word lies in STAR ∪ B1 ∪ I1 (the five
slices); so STAR, B1, I1 are the Jacobi-(−1) cells of one set, and QR is the Jacobi-(+1) rest.

**(Q1) Complementarity measurement (EVIDENCE target).** For pairs (A, B) of families, at 10⁸, 10⁹, 10¹⁰ (windows) and
10¹¹, 10¹², 10¹³ (samples): (a) the residual correlation ρ_{AB|loc} of the counts after removing *local data* (p mod 840
strata; OLS on one-hot residues of p mod small prime powers), (b) joint zero / joint low-tail rates against the
within-stratum independence prediction (Mantel–Haenszel odds ratio OR_{AB|loc}). "Complementary beyond local data" :=
ρ_{AB|loc} < 0 robustly (nominal z < −4 at ≥ 2 scales, surviving the richer local control) or OR_{AB|loc} < 1 likewise.

**(Q2) Complementarity theorem (target if (Q1) finds a pair).** An inequality R_A(p) + R_B(p) ≥ c·(main term) or an
implication R_A(p) = 0 ⟹ R_B(p) ≥ 1 at a single large p.

**(Q3) Scoped negative (target if (Q1) finds none).** A theorem saying which structure all pairs of the menu share (same
integers p + u / tp + 1, same local data, same Jacobi cell function), and what a complementarity argument would therefore
have to supply.

## 2. Why this is not closed

* Closed/known: (★) vs b = 1 residuals positively correlated overall (+0.21…0.30; `BM_CORRECTED_COUNT.md` §4,
  `BRAINSTORM/z38_shared_brauer_character.md`); on the word set the two lines co-vary positively beyond |W| (partial
  0.35; `BRAINSTORM/s9_union_thinning.md`); Type I vs Type II residual log-counts +0.70 at p ≤ 2·10⁵
  (`BRAINSTORM/z52b_fingerprint.md` #246); windows *inside* (★) are net positively dependent with two congruence-level
  negative leads (`Z56_FAMATTACK.md` §3.2).
* Not done: (i) conditioning on local data beyond p mod 840 for *different families*; (ii) the joint *zero/low-tail*
  structure (the brief's question) rather than overall correlation; (iii) the Type I slice, the c-lines, 𝔊* vs its corner
  K, and the QR placebo; (iv) scales 10¹⁰–10¹³; (v) a theorem explaining the sign. None of the closed items (FRONTIER §6,
  z53 closed list) is a statement about the *joint* law of two families at one p.

## 3. First falsifier (pre-registered, checkpoint 1)

Engine `scripts/z57_complement_words.c` (all words of W(p) and W(cp) by factoring p + u, cp + u for u ≤ 2 + √(cp + 1);
validated below). **Registered rule:** a pair (A, B) of *disjoint-cell* families (STAR/B1/I1/c2/c3 and their level bands,
G/K) is a **lead** if its within-p-mod-840 residual correlation is < −4 nominal s.e. at two scales *and* stays < −2 s.e.
under the residue-OLS control; complementarity "beyond local data" is **killed for the menu** if no pair is a lead and
pooled joint-low-tail ratios (k = 2 families) are ≥ 1 within strata at every scale. Same-integer level bands of one slice
are reported but are not eligible as leads unless they survive the residue control (they are congruence-determined at
large t, cf. FAMATTACK's C(3,4)).

*Engine validation (CERTIFIED for the stated range).* `scripts/z57_complement_brute.py` (direct enumeration of all
(t, u, v), with every STAR, B1, I1 and c-line word turned into an explicit 4/n identity checked in exact rationals)
agrees with the engine column by column for all 349 odd n ≡ 1 (4), 5 ≤ n ≤ 1393 (primes, composites, squares). Against
the independent `scripts/z38_b1.c`: STAR = R and B1 = 2·N₁ at all 1045 primes p ≡ 1 (4) in [1000, 20000]. With JAC=1 the
engine recomputes (A/p) for every interior word and confirms Thm 4.5's cell law (0 failures, same range). Known values:
R(409) = R(577) = 0, R(1000009) = 20, B1(193) = B1(2521) = 0, all slices 0 at 9801 = 99² and at n = 105.

TODO: results (§4), theory (§5), screens, verdict, FRONTIER text, review.
