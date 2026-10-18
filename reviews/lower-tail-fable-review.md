# R286 — hostile review of LOWER_TAIL_FABLE.md (O274, model FABLE)

Reviewer: R286 (side agent, branch side-agent/review-tail-fable). Author files merged from side-agent/lower-tail-fable.
From-scratch scripts: `scripts/review_r286_*.py` (no reuse of `z43_fable_*`).

**Repairs applied** (author quiet after checkpoint 1; marked "(R286 repair …)" in LOWER_TAIL_FABLE.md and the O274 report):
D1 ((2.5) restated), D2 (ES → ES₅ for §2.8/§2.9, ⟹ flagged open), D3 (table scope + even-A note), D4 (§1 remark), D5/D6
(census wording, Astra/SIGN_IDENTITY cross-ref), D7/D8 (calibration note), D9 (CM / (a+b)² claim), D10 (reducedness),
§4 labels. The author's original text is kept; repairs are inserted as marked notes.

**Bottom line:** no FATAL. Five MAJOR (D1, D2, D3, D7, D9), five MINOR. SHARP 2 SOUND; SHARP 3 GAP (it is ES₅, not ES);
SHARP 1 GAP as framing (SOUND-AFTER-REPAIRS as an Assessment).

## Claim A — SHARP 2: Thm 1.1 (canonical two-target form) and Lemma 2.7

**Verdict: Thm 1.1 SOUND. Lemma 2.7 SOUND (re-proved; a sharper Type I form noted). Companion forms (1.3), (1.4),
(2.1)–(2.3), (2.6) SOUND; (2.5) FALSE as stated (D1); §1 last remark contradicts Lemma 2.7 (D4).**

*Re-derivation.* Type II: if d = 4muw − 1 divides N = mp + u, put v = N/d; then mp = 4muvw − u − v, so
u + v = m(4uvw − p), i.e. e := 4uvw − p = (u+v)/m ∈ ℤ_{>0}, and 1/(uvw) + (u+v)/(mpuvw) = (p+e)/(puvw) = 4/p.
Type I: if d = 4muw − p > 0 divides N, h = N/d gives hp + mp + u = 4hmuw, so 1/(muw) + 1/(hpmw) + 1/(huw) = 4/p.
Converse: for p ∤ x the fraction (4x − p)/(px) is reduced; the classical two-unit-fraction criterion (coprime
U, V | px with (4x − p) | U + V) splits by whether p | U (Type I: U = pm, V = u, x = muw) or not (Type II), and
re-indexing gives the certificate. Every step checks.

*From-scratch test* (`scripts/review_r286_canon.py 3000 25`, own divisor/Jacobi/Kronecker code, exact Fractions):
all 8 334 unordered solutions of 4/p = 1/x + 1/y + 1/z for the 211 primes p ≡ 1 (4), p < 3000, enumerated
completely via (ay − b)(az − b) = b²; every one has exactly 1 or 2 p-divisible denominators; **every solution maps to
a certificate of its own type** (21 088 certificates; the stated reconstruction returns exactly that solution) and
**every certificate in the window m, u < 25 (6 105 Type I + 3 854 Type II = 9 959, matching the author's count)
reconstructs to one of the enumerated solutions, of the claimed type**. 0 failures. (Caveat on test power: every
p < 3000 has both a Type I and a Type II solution, so a per-prime *existence* comparison would be vacuous; the
solution↔certificate maps above are the non-vacuous test.)

*Lemma 2.7 re-proof.* (II) d ≡ −1 (mod 4mu) gives gcd(d, mu) = 1 and m⁻¹ ≡ 4uw (mod d), so p ≡ −4u²w and
(p/d) = (−1/d)(w/d) = −(w/d); d ≡ −1 (mod 4w) gives (w/d) = +1 (odd part by reciprocity, 2-part via d ≡ 7 (8) when
w is even). (I) From mp ≡ −u and p ≡ 4muw (mod d): m(p² + 4u²w) ≡ 0 and 4m²w ≡ −1 (mod d); gcd(m, d) | p, so for
p ∤ mu we get (−w/d) = 1, (w/d) = −1, and (w/d) = (p/w) (Kronecker; reciprocity with d ≡ −p (mod 4w), 2-part via
(2/·) being even under n ↦ −n mod 8). In particular **the Type I level is never w = 1**. Additionally (reviewer,
PROVED by the same computation, verified on all 14 712 Type I certificates from solutions, p < 3000):
**(p/d) = −(p/mu)** for Type I, so the non-residue of a Type I certificate is carried by d·m·u jointly as well as by w;
(p/d) = +1 in exactly half (7 356) of the cases. p = 13, (m, u, d) = (2, 1, 3), w = 2 confirmed.
Numerically 0 violations of either half of Lemma 2.7 on all certificates (from solutions and window).

*Companion forms.* (1.4) is a literal re-indexing (δ = u, (d+1)/4 = muw). (1.3) holds with the relabelling
(u, w) ↦ (m, w): d | 4m²w + 1 and d ≡ −p (mod 4mw); converse d = 4uwk − p gives the Type I certificate (u, k, w).
(2.2) II and (2.3) II: count-level bijection with Type II certificates verified for every p < 400
(`scripts/review_r286_forms.py`): #witnesses = #certificates at all 37 primes. (2.3) I follows from (1.3) by passing
to the complementary divisor (ff′ = 4u²w + 1 ≡ 1 mod 4uw turns −p into −p⁻¹). (2.6) correct for prime e ≠ p.

## Claim B — SHARP 3: Legendre form (§2.8) and mutual-shift graph (§2.9)

**Verdict: GAP (MAJOR D2). The direction "(r, A) ⟹ ES(p)" is SOUND (re-proved with five explicit constructions,
including all degenerate cases). The direction "ES(p) ⟹ ∃ (r, A)" is NOT proved — it is exactly the campaign's open
five-slice statement ES₅ / λ(p) ≤ 3. The §2.8 table is incomplete and one row is wrong for even A (D3). §2.9: dictionary
SOUND for ES₅ (not ES); census numbers reproduced; two descriptive errors (D5) and the graph is Astra's forest (D6).**

*Dictionary.* For a pair (r, A) put a = (p+r)/A, b = (A+1)/r, c = r. Then p = abc − a − c, A = bc − 1, A* := ab − 1, and
p/A = [[a, b, c]]; this is DEDEKIND_ES Lemma 1.1 with [[v, t, u]] = [[a, b, c]] (a, b, c ≥ 1 allowed). The five
conditions of DEDEKIND_ES Thm 4.5 are 4 | A, 4 | A*, 4 | b, 4 | c, 4 | a. Reviewer's explicit solutions (derived
independently, each an algebraic identity given p = abc − a − c):
S1 (4 | A, D = A/4) 4/p = 1/(A*Dp) + 1/(aD) + 1/(A*aD); S2 (4 | A*, D = A*/4) 4/p = 1/(ADp) + 1/(cD) + 1/(AcD);
S3 (b = 4w) 4/p = 1/(acw) + 1/(apw) + 1/(cpw); S4 (c = 4w) 4/p = 1/(wA*) + 1/(bpw) + 1/(bpwA*);
S5 (a = 4w) 4/p = 1/(wA) + 1/(bpw) + 1/(bpwA).

*From-scratch test* (`scripts/review_r286_legendre.py 3000 1200`). The set of pairs is finite and enumerated
completely (A ≥ r − 1, and A = p + r forces r | p + 1, otherwise r ≤ p + 2): 11 655 pairs at the 211 primes
p ≡ 1 (4) < 3000, 6 557 at the 188 non-square composites n ≡ 1 (4) < 1200, 369 at odd squares. On **every** pair,
(A/n) = −1 (Jacobi) ⟺ some S_i applies, and every applicable S_i is an exact ES identity (0 failures; this
re-verifies DK Thm 4.5 *including* the degenerate words a, b or c = 1, which Thm 4.5 itself does not cover — they are
covered by DK Cor 4.6's R169 remark only for p ≡ 1 (8); for p ≡ 5 (8) the pair (r, A) = (1, 2) always exists and S2
applies since a = (p+1)/2 ≡ 3 (4)). Every prime has a pair; no odd square does (T1 control). The 2-adic reading
"(A/p) = −1 ⟺ A ≡ 3 (4) or r ≡ 3 (4)" for odd A, r: re-proved by reciprocity ((A/p) = (−r/A) and
(r/A) = (−1/r)(−1)^{(r−1)(A−1)/4}) and 1 346/1 346 QNR odd pairs consistent. "r ≡ 0 (4): sign automatic" re-proved
((r/A) = 1 because A ≡ −1 (mod r), A ≡ 3 (4)); 0 counterexamples.

So "⇐" (each pair gives ES(p)) is SOUND, relative to nothing beyond the reviewer's identities S1–S5 plus Thm 4.5's
mod-8 cell check (re-verified here on all pairs).

*The "⟹" direction is open.* The images of S1–S5 are the five DK slices: proper sub-families of Thm 1.1's
certificates (S3 is Type II with m = 1, i.e. (u+v)/e = 1; S4/S5 are Type II with one of the two coprime divisors
equal to 1; S1/S2 are Type I with a = 1). Nothing in §2.8 maps an arbitrary ES solution into one of them, and
DEDEKIND_ES Cor 4.6 states only "the five X/e-slices of ES(p) together hold ⟺ λ(p) ≤ 3" — the ledger calls this
**ES-five / ES₅** ((J)-items at DISCOVERIES l. 596–598, 1630) and lists λ(p) ≤ 3 as EVIDENCE/CONJECTURE, not as a
consequence of ES. Measured from scratch: of the 8 334 solutions at the 211 primes < 3000, **4 671 (56 %) are not
produced by any (r, A)**; at p = 2521 only 2 of 9 solutions are five-slice. So "ES(p) ⟹ Legendre form" would be a new
theorem (ES ⟹ ES₅), not a re-indexing. Since ES(p) is known for all p in range, the brute-force "0 mismatches"
of `z43_fable_hj.py` cannot test this direction (the author's own report says so for the even branches; the issue is
the whole ⟹ direction, not the even branches).

*The §2.8 table (which slice fires; all QNR pairs at the 211 primes < 3000, 6 096 pairs).*

| r mod 4 | A | #QNR pairs | slices that fire (reviewer) | author's row |
|---|---|---|---|---|
| 0 | odd | 1 510 | S4 always (+S2 or S3 sometimes) | "López Type A", sign automatic — correct |
| 1 | odd | 770 | S3 (Type II, m = 1) | "(★), d = A" — correct |
| 1 | even | 724 | S2 (Type I) | **missing** |
| 2 | odd | 1 178 | S3 in 770, S2 in 408 | "Type I branch" — **wrong for 770/1 178 (Type II)** |
| 3 | odd | 576 | S5 (+S3 in 229) | explicit formula — correct (576/576) |
| 3 | even | 2 338 | S1 and/or S5 | **missing**; and "extra condition: none" fails: 886 even-A pairs with r ≡ 3 have (A/p) = +1; the row's explicit formula is valid on only 934/2 338 |

So half of all certificates (3 062 / 6 096, even A with odd r) are outside the table, the "four-branch
decomposition by r mod 4" is not a decomposition, and the r ≡ 2 label is wrong. (The odd-A rows themselves check.)

*§2.9 graph.* Dictionary (t, e) ↔ (a, c): with A = (p+e)/t one gets A | p + e, A ≡ −1 (mod e), (A/p) = (te/p),
so "bichromatic edge ⟺ Legendre pair" is SOUND — hence G_p characterises **ES₅**, not ES (same gap). Vertices with
p | e never lie on an edge (te | p + t + e with p | e forces p | t), so colour 0 is harmless. Census re-computed
from scratch with a complete edge enumeration (`scripts/review_r286_graph.py`; every edge is found from its smaller
endpoint s ≤ 1 + √(p+1), since (t−1)(e−1) ≤ p + 1 when both ends are ≥ 2): connected 28/211, QNR in comp(1) 209/211
(the two exceptions 409, 1201 reproduced), bichromatic edge 211/211, odd squares 0. **But**: (i) the other components
are not "2- or 3-cliques": there is no triangle at all — every component at every tested prime is a tree
(cycle rank 0 at all 211 primes < 3000 and at 48 sampled primes up to 3·10⁶); {4, 7, 11} at 73 is the path 7—4—11
(77 ∤ 73 + 7 + 11 = 91); off-root components have 2–8 vertices (344 edges, 131 two-edge paths, 39 larger trees).
(ii) "comp(1) has ≍ log² p vertices" is not supported: mean |comp(1)| over 12 primes near 3·10³, 3·10⁴, 3·10⁵,
3·10⁶ is 26.7, 44.6, 49.0, 57.3 against log² p = 64, 106, 159, 222 (ratio falling 0.42 → 0.26). (iii) G_p is
exactly the word forest F_p of LOWER_TAIL_ASTRA Lemma 2.1 ((J)106, O275, run in parallel), which *proves* the forest
structure (unique smaller neighbour r_v = −p mod v); the endpoint encoding itself is SIGN_IDENTITY Lemma 1.1.

## Claim C — SHARP 1: the index calibration (§3.2, Assessment)

**Verdict: GAP (framing; MAJOR D7 + arithmetic MINOR D8). The counting itself is right; the headline reading and the
ladder statement are not.** (`scripts/review_r286_index.py`.)

* Correct: the number of cells (m, u) with mu | U is Σ_{k|U} τ(k) = τ₃(U) (= 3^{ω(U)} for squarefree U), each cell
  contributes ≈ log p divisor tries, and d ≡ −1 (mod 4U) is sufficient for every such cell. For H = squares,
  [G : H] = 2^{ω(U)+O(1)} (the O(1) is the 2-part: 1 or 2 extra factors). So τ₃(U) ≫ [G : H] for squares — arithmetic SOUND.
* **"tries ≪ group for every U (equality region only U | 24)" is false as stated**: the tries carry the factor log p, so
  tries ≥ |G| = φ(4U) for all U up to ≈ log p·(log log)^{O(1)} — e.g. at p = 10⁹ every U in {1, 2, …, 120, 210, 2310}
  has τ₃(U) log p > φ(4U). The crossover is a function of p, not the fixed set U | 24 (a constant that secretly
  depends on the parameter).
* **The ladder arithmetic is wrong for composite k.** [G : G^k] = Π_{cyclic factors C_n} gcd(k, n), which is
  ≈ k^{π(y)/φ(k)} only for *prime* k. For U = Π_{q ≤ y} q, log₃[G : H_k] / π(y) → 0.50 (k = 3), 0.94 (k = 4), 1.13 (k = 6),
  1.10 (k = 8), 1.44 (k = 12) — so for k = 6, 8, 12, 24 the index **exceeds** τ₃(U) = 3^{π(y)} (checked at y = 100,
  10³, 10⁴), contradicting "[G : H] ≈ k^{π(y)/φ(k)} < 3^{π(y)}" for all k ≥ 3. The ladder is not monotone in k.
  On the brief's question: **cubes are not borderline** (index 3^{π/2}, a factor 3^{π/2} below τ₃); the borderline
  rung is **k = 4** (8^{π/2} = 2.83^π vs 3^π).
* **The "explains why ES^□ had to be provable" reading is not supported (MAJOR D7).** ES^□'s proof (SYNTHESIS_SPARKS2
  Prop 2.2) uses *no* pooling over cells mu | U and *no* square-coset target modulo 4U: it is the fixed-modulus-4 shot
  g | n + 4Q² with Q free (one Dirichlet prime r ≡ 3 (4), (n/r) = −1, then solve 4Q² ≡ −n mod r). In the campaign's
  (k, Q₁) phase diagram it is the slice k = 1 (DISCOVERIES l. 895), i.e. exactly the *other* provable category of §3.8
  ("shot family infinite at a fixed modulus"). The count τ₃(U) log p vs 2^{ω(U)} plays no role in it, and "tries ≥ index"
  is neither necessary nor sufficient for a hit (the author concedes the covering point for k ≥ 3, but the same
  objection applies at k = 2). Repair: present the calibration as a heuristic *consistency* check, state that ES^□ is
  proved by an infinite shot family at modulus 4 (not by the counted pooling), drop "had to be provable", and correct
  the ladder (prime k only; k = 4 borderline; composite k ≥ 6 above the line).

## Claim D — §2 "what the forms expose" and §3 mechanism audit (spot checks of PROVED items)

**Verdict: mostly SOUND; one false PROVED statement (MAJOR D9).**

* "Every certificate divisor is ≡ 3 (mod 4), so every certificate integer has a prime factor ≡ 3 (4); no primitive
  sum of two squares carries a certificate": SOUND.
* **"#E(𝔽_p) for curves with CM by ℤ[i] and all their quartic twists are sums of two coprime squares", and (§3.3)
  "(a+b)² = p + 2ab … has no prime factor ≡ 3 (mod 4), hence carries no certificate": FALSE.** Direct point counts of
  y² = x³ − Dx for all D mod p (`scripts/review_r286_cm.py`, 95 primes p ≡ 1 (4) < 1200): at 50 primes some ℤ[i]-CM order
  has a prime factor ≡ 3 (4) (p = 13: #E = 18 = 3² + 3²; p = 37: 36), and (a+b)² has one at 60 primes (p = 29:
  (5+2)² = 49; p = 37: (1+6)² = 49). The orders p + 1 ± 2a = (a ± 1)² + b² need not be primitive.
  **Worse, such orders do carry certificates**: p = 229 = 2² + 15², #E = 234 (t = −4) = 229 + 5 has the Type II
  certificate (m, u, d) = (1, 5, 39), 4/229 = 1/60 + 1/2290 + 1/2748; p = 349, #E = 360 = 349 + 11 has the Type I
  certificate (1, 11, 3), 4/349 = 1/88 + 1/10560 + 1/335040; p = 1153, #E = 1170 likewise (all verified exactly and the
  orders by point count). So "this kills at the root every 'p = a² + b² / CM group order' construction" is wrong; the
  correct statement is only about *primitive* norms. Repair: restrict to primitive representations, delete the (a+b)²
  example, and downgrade §3.3's CM bullet to "dead by B2 (lottery)", like the non-CM case.
* f_II even (§3.5): SOUND under the ET ordered convention (y, z) — the involution u ↔ v has a fixed point only if
  e | 2u, hence e | p (gcd(e, u) | p), forcing e ∈ {1, p}, both impossible for p ≡ 1 (4). Should state the
  convention: for *unordered* solutions u ↔ v gives the same solution, and the parity statement is about certificates.
* No Vieta (§3.6): SOUND — 4muwc = mp + u + c (II) and 4muwc = p(m + c) + u (I) are multilinear (each variable to
  degree 1), and (4mwu − 1)(4mwc − 1) = 4m²wp + 1 checks.
* §3.1 lattice remark, §3.4, §3.7: descriptive Assessments, nothing to falsify; the "u_i m_i < d for Klein-polygon
  vertices" is standard.

## Numbered defects

* **D1 (MAJOR) — §2 (2.5) is false.** "Type II ⟺ p = e²k² − y² − e for some e ≡ 3 (4), k ≥ 1, y ≥ 0" fails at
  p = 13, 37, 97, 181, 193 (and 3 more primes < 1000): e.g. 4/13 = 1/4 + 1/26 + 1/52 is Type II, but no (e, k, y) exists
  (complete search: e ≤ p + 1 is forced). The derivation gives 4uv = e²s² − (u − v)² and hence p + e = w(e²s² − y²), which
  is of the stated shape only when the level w is a square; indeed, for every p < 1000, (2.5) has a witness ⟺ some Type II
  certificate has square level w (0 mismatches), and at the failing primes every Type II certificate has non-square w. The "equivalently p ∈ W − □, W = {X² − e : e | X}" reading is worse: with e = 2, X = (p+3)/2, y = (p+1)/2 it holds for
  **every** n ≡ 1 (4), odd squares included (39/39 squares < 6400). *Repair:* "(2.5) Type II ⟺ p + e = w(e²k² − y²) for
  some e ≡ 3 (4), k, w ≥ 1, y ≥ 0 with ek ≡ y (2), ek > y (the w = □ case is the stated form)", and delete the W − □ clause
  (or keep e ≡ 3 (4) in W and add the factor w).
* **D2 (MAJOR) — §2.8 / §2.9 / §4 / SHARP 3: "ES(p) ⟺ Legendre form" and "ES(p) ⟺ G_p has a bichromatic edge" are
  proved only in the direction ⇐.** The ⟹ direction is ES ⟹ ES₅ (λ(p) ≤ 3), open in the ledger; 56 % of all solutions
  for p < 3000 are outside the five-slice image. DEDEKIND_ES Cor 4.6 is misapplied (it characterises the five slices, and
  only for p ≡ 1 (8)). *Repair:* replace ES(p) by ES₅(p) (five-slice ES) in §2.8, §2.9, §4 and SHARP 3; state
  "ES(p) ⇐ (r, A)" as PROVED; delete "the whole content of ES is 'the infinite system {(A, −c)} covers the primes'"
  (it is the content of ES₅).
* **D3 (MAJOR) — §2.8 table.** Even A with odd r (3 062 of 6 096 QNR pairs, all Type I slices S1/S2 or S5) is missing;
  row r ≡ 3 "extra condition: none" is false for even A (886 QR pairs) and its explicit formula fails on 1 404/2 338
  even-A QNR pairs; row r ≡ 2 labelled "Type I branch" is Type II ((A)3, 4 | b) in 770/1 178 cases. *Repair:* restrict the
  table to odd A and say so, add the even-A row ("(A/p) = −1 needed; S1 (4 | A) / S2 (4 | ab − 1) / S5 (4 | a)"), and
  relabel r ≡ 2 as "Type I (4 | ab − 1) or Type II (4 | (A+1)/r)".
* **D4 (MINOR) — §1, last Remark** "Every certificate (m, u, d) forces (p/d) = −1" contradicts Lemma 2.7(I) (p = 13,
  (2, 1, 3)). *Repair:* "Every Type II certificate forces (p/d) = −1; every Type I certificate forces (p/w) = −1 and
  (p/d) = −(p/mu)." (The latter identity is new here, PROVED in Claim A, 14 712/14 712 checks.)
* **D5 (MINOR) — §2.9 census.** "Sporadic 2- or 3-cliques ({4,7,11} at 73, …)": no triangles exist; off-root components are
  trees with 2–8 vertices; {4, 7, 11} is a path. "comp(1) has ≍ log² p vertices": not supported (ratio to log² p falls
  0.42 → 0.26 from 3·10³ to 3·10⁶). *Repair:* "small trees (2–8 vertices)"; "|comp(1)| grows slowly (mean 27 at 3·10³,
  57 at 3·10⁶ in samples); growth rate not determined".
* **D6 (MINOR, attribution) — §2.9.** G_p is the word forest F_p of LOWER_TAIL_ASTRA Lemma 2.1 ((J)106, O275 parallel run),
  which proves it is a forest; the encoding t | p + e, e | p + t is SIGN_IDENTITY Lemma 1.1. Spark 3 (edge-to-edge
  mediant move) should be read against Astra's unique-parent map. *Repair:* add the cross-reference.
* **D7 (MAJOR, framing) — §3.2 / §4 / SHARP 1.** The calibration does not "explain why ES^□ had to be provable": ES^□ is
  proved by an infinite fixed-modulus-4 shot family (§3.8's second category), not by pooled counting against a square
  coset. *Repair:* as in Claim C.
* **D8 (MINOR) — §3.2 arithmetic.** (a) "tries ≪ group for every U (equality only U | 24)" ignores the log p factor —
  the crossover U ≈ log p·(log log p)^{O(1)} depends on p; (b) "[G : H] ≈ k^{π(y)/φ(k)} < 3^{π(y)}" holds only for prime
  k; for k = 6, 8, 12, 24 the index exceeds τ₃(U); k = 4 is the borderline rung, cubes are not.
* **D9 (MAJOR) — §2 "What the forms expose" and §3.3, CM / (a+b)² claims are false** (Claim D): ℤ[i]-CM orders and
  (a+b)² are not primitive in general, have prime factors ≡ 3 (4) at about half the primes, and CM orders *do* carry
  certificates (p = 229, 349, 1153). *Repair:* restrict to primitive norms; CM orders are "dead by B2" only.
* **D10 (MINOR, presentation) — §1 "Proof sketch"** omits that (4x − p)/(px) is reduced (gcd = 1 because p ∤ x), which the
  two-unit-fraction criterion needs; one line.

## Labels (§4)

Thm 1.1, (1.3), (1.4), (2.1)–(2.3), (2.6), Lemma 2.7: PROVED — agreed. (2.5): currently false (D1); PROVED after repair.
§2.8: "⇐" PROVED (relative to Thm 4.5's mod-8 cell check, re-verified here on all pairs incl. degenerate words); "⟹"
must be removed or labelled as the open ES ⟹ ES₅ (D2). §2.9 dictionary: PROVED for ES₅. §2.9 census: EVIDENCE (numbers
reproduced; descriptions D5). §3.2 calibration: Assessment, with D7/D8 repairs. §3.3 CM bullet: not PROVED (D9).
No claim of ES (or of any case of it) is made; that is correct.

## Summary

| Claim | Verdict |
|---|---|
| SHARP 2: Thm 1.1 | SOUND |
| SHARP 2: Lemma 2.7 | SOUND (sharpened: Type I (p/d) = −(p/mu)) |
| §1–2 companion forms | SOUND except (2.5) and the W − □ clause: FALSE as stated (D1), SOUND-AFTER-REPAIRS |
| SHARP 3: Legendre form | GAP — ⇐ SOUND, ⟹ unproved (= ES ⟹ ES₅) (D2); table defects (D3) |
| SHARP 3: graph G_p | dictionary SOUND for ES₅; census reproduced; D5, D6 |
| SHARP 1: index calibration | GAP (framing, D7) + arithmetic errors (D8); SOUND-AFTER-REPAIRS as an Assessment |
| §3 PROVED spot-checks | f_II even, no-Vieta, "≡ 3 mod 4 divisor": SOUND; CM / (a+b)² kill: FALSE (D9) |

No FATAL defect: nothing claimed about ES itself is wrong, and the core canonical form is correct. Five MAJOR
(D1, D2, D3, D7, D9).
