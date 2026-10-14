# R211 — hostile review of O213 TRANSPORT_LAW.md (+ BRAINSTORM/y5_*.md)

Reviewer: R211 (side agent). Scope: TRANSPORT_LAW.md, the eight memos BRAINSTORM/y5_*.md, logs/y5_*, the
O213 report. All numerics below were redone with from-scratch code (`scripts/review_r211_*`); the author's
scripts were not run or reused.

## Summary verdicts

No FATAL. All PROVED statements re-derived and correct; all census numbers reproduced exactly from scratch to 10⁷.
Defects are in the *descriptions* of the evidence (hard primes, word counts, SQ_H scope) and in framing.

| claim | verdict |
|---|---|
| SHARP 1 transport = Ptolemy mod 8 | **SOUND** (and (J)42 needs correcting, D1) |
| SHARP 2 general-r Jacobi law | **SOUND**; novelty classical in substance (D3, D11) |
| SHARP 3 narrow/wide dictionary | **SOUND-AFTER-REPAIRS** (D4; a relabelling) |
| SHARP 4 SQ_H | **SOUND** as CONJECTURE/EVIDENCE; scope wording (D6) |
| SHARP 5 p = 21841, o* census | **SOUND** (exhaustive); hard-prime description wrong (D5) |
| (a) P_h, C(o), (J)26 | **SOUND-AFTER-REPAIRS** (D8, D10); (J)26 link upgradable (D9) |
| (b) census | **SOUND-AFTER-REPAIRS** (D5) |
| (c) no mod-32 shadow | **SOUND** (EVIDENCE) |
| (d) Siegel–Weil | **SOUND**; memo numerics wrong (D7) |
| labels | appropriate except D2, D9 |

## Claim-by-claim

### SHARP 1 — transport law = Ptolemy mod 8 (§1, memo y5_transport_is_ptolemy). Verdict: **SOUND** (minor wording).

Re-derivation. From h = cm − 1, h′ = ms − 1, N = cms − c − s: h′c = N + s, cm = 1 + h, ms = 1 + h′, sh = N + c,
hh′ = m(cms − c − s) + 1 = 1 + Nm. The even pair is adjacent (FRIEZE Lemma 1.1), so ee′ is the left side of one of
these five relations, with o the opposite vertex q_{i+3}. 4 | ee′. For the relation 1 + o: 8 | ee′ ⟺ o ≡ −1 (8);
for N + o and 1 + No (N odd, N² ≡ 1 (8)): 8 | ee′ ⟺ o ≡ −N (8). Hence o ≡ −N^ε (4) always, and
8 | ee′ ⟺ oN^ε ≡ 7 (8). Since oN^ε ≡ 3 (4), (−1)^{[oN^ε ≡ 7 (8)]} = −(2/oN^ε), and Thm 1.2 gives
(h′/N) = −(−1/N)(2/o)(2/N)^ε. For N ≡ 1 (8): o ≡ 3 (4) for every word, certificate ⟺ o ≡ 7 (8). Correct.

From-scratch check (`scripts/review_r211_identities.py`, SHARP1): all formal words with odd N ≤ 3000 (81 784 words, all
four classes of N mod 8): the five Ptolemy relations hold exactly, the even pair is adjacent, 4 | ee′,
o ≡ −N^ε (4), [8 | ee′] = [o ≡ −N^ε (8)], (h′/N) = −(−1/N)(2/o)(2/N)^ε = Thm 1.2, and for N ≡ 1 (8)
[some q_i ≡ 0 (4)] = [o ≡ 7 (8)] = [(h′/N) = −1]. 0 failures. (The author's larger run, 784 732 words to 2·10⁴, was not
rerun; the statement is a two-line identity.)

**How (J)42 should be corrected.** DISCOVERIES (J)42, bullet "Transport law", currently reads "a five-slice
certificate at N ≡ 1 (8) ⟺ some word has o ≡ ±1 (mod 8). At an odd square every word has o ≡ ±3 (mod 8) (T1). It is
Hilbert reciprocity localised: a cherry-depth reading in the 2-adic Bruhat–Tits tree." Two corrections:
1. The "±" are vacuous and misleading: at N ≡ 1 (8) **every** word has o ≡ 3 (mod 4), so the dichotomy is
   o ≡ 7 (8) (certificate) vs o ≡ 3 (8) (non-certificate; all words at odd squares). Replace "±1" by "7" and "±3" by "3".
2. Add the deflation: (R211/O213) the transport law has no content beyond Thm 1.2 plus the one Ptolemy relation
   through the even edge, ee′ ∈ {1 + o, N + o, 1 + No}; "−(2/o)" is the residue of o mod 8, i.e. the 2-adic depth of
   the even edge read through that relation (8 | ee′ ⟺ o ≡ −N^ε (8)). It is not a character of 2 carrying arithmetic
   of N at a small modulus, and o need not be small. The phrase "Hilbert reciprocity localised" should be replaced by
   "Thm 1.2 rewritten through one exchange relation" (the reciprocity is entirely inside Thm 1.2).
   FRIEZE_ES's summary line "one 2-adic bit at a unique even edge, transportable to a small modulus o" should get the same
   qualifier.

### SHARP 2 — general-r Jacobi law (§3, memo y5_general_r_jacobi Thm 1). Verdict: **SOUND** (novelty: classical in substance).

Re-derivation. (i) The path matrix (a_i on the diagonal, −1 off) has leading minors K_i (negative-continuant
recursion K_i = a_iK_{i−1} − K_{i−2}); with all K_i ≠ 0, LDLᵀ gives Q ≅ ⟨d_i⟩, d_i = K_i/K_{i−1}. With D_i = K_i
(K_0 = 1), ∏_{i<j}(d_i, d_j) = ∏_{i=1}^{r−1}(D_i, d_{i+1}) and (D_i, D_{i+1}/D_i) = (D_i, D_iD_{i+1}) =
(D_i, D_i)(D_i, D_{i+1}) = (D_i, −1)(D_i, D_{i+1}) = (D_i, −D_{i+1}), using (a, a) = (a, −1). (ii) At odd ℓ ∤ N the ℤ_ℓ-lattice is
unimodular, hence diagonal with unit entries, s_ℓ = 1 (intermediate ℓ | K_i are irrelevant — s_ℓ is a ℚ_ℓ-invariant).
(iii) At ℓ | N: gcd(K_{r−1}, K_r) = 1, so the span M of e_1..e_{r−1} is ℓ-unimodular and splits off;
L ≅ M ⊥ ⟨N/K_{r−1}⟩ over ℤ_ℓ, M ≅ ⟨u_1..u_{r−1}⟩ units with ∏u_i ≡ K_{r−1} mod squares, so
s_ℓ = ∏_i(u_i, N/K_{r−1})_ℓ = (K_{r−1}/ℓ)^{v_ℓ(N)}. (iv) ∏_v s_v = 1 and N > 0 odd give
(K_{r−1}/N) = s_2 s_∞, with (K_i, −K_{i+1})_∞ = −1 ⟺ K_i < 0 < K_{i+1}. All steps check; no hidden
hypothesis beyond the stated ones (N > 0 odd, K_1..K_{r−1} ≠ 0; r = 1 is the empty product).

From-scratch check (own 2-adic Hilbert symbol after Serre III.1.2, sanity-checked on (2,3), (−1,−1), (3,7), (3,5), …):
200 000 random words, r ≤ 10, letters positive, signed, and drawn from {−2, −1, 0, 1, 2, 3, 4, 8, 16, random}; coverage:
19 381 with some intermediate K_i = ±1, 167 778 with some even K_i, 59 599 with some negative K_i, 45 950 with a letter
0 or 1. 0 failures. Both factors are non-trivial in the sample (on 50 000 signed words: s_∞ = −1 in 29 035, s_2 = −1 in
25 223), so the test is not vacuous.

Novelty. The leading-minor formula for the Hasse invariant and "product formula ⇒ reciprocity" are textbook
(Cassels, *Rational Quadratic Forms*, Ch. 4/6 — not re-accessed here; the derivation above is self-contained). The shape
"Jacobi symbol (K_{r−1}/K_r) = product of local symbols at 2 and ∞ along the continued fraction" is, in R211's Assessment (not verified line by line against Kubota), the classical
Kubota splitting of the metaplectic cocycle on Γ(4)-type groups (Kubota 1969: for γ ∈ Γ₁(4) the Jacobi symbol (c/d) is
the coboundary of ∏_v σ_v, σ_v the local Kubota cocycles, whose real component is a sign-change count) evaluated on the
word's factorisation into T^{a_i}S; Jacobi symbols of continued-fraction convergents also have an explicit literature
(Bach–Shallit, *Algorithmic Number Theory* I (1996), Jacobi symbol via the simple continued fraction; Girstmair,
"Continued fractions and Jacobi symbols", IJNT 2011; Rademacher's Dedekind-sum formula for (a/c)). R211 did not find
this exact closed form stated in these sources (Girstmair/Bach–Shallit were seen only as abstracts via web search; not
read in full). The author's own Assessment ("classical in substance … what it adds is the explicit ∞-factor") is fair;
but the explicit ∞-factor is precisely the real Kubota cocycle, so "adds" should be "makes explicit in frieze notation"
(defect D3).

### SHARP 3 — positivity = narrow-minus-wide (§3.2, memo y5_narrow_wide). Verdict: **SOUND-AFTER-REPAIRS** (relabelling; one false justification).

Prop 1 re-derived: for fixed m ≥ 1, (c, s) ↦ (a, b) = (h, h′) = (cm − 1, ms − 1) is a bijection between positive
words and factorisations ab = 1 + Nm with a, b > 0, a ≡ b ≡ −1 (m) (converse: c = (a+1)/m ≥ 1 since a > 0 and
a ≡ −1 (m)); N = cms − c − s follows from hh′ = 1 + Nm when m ≠ 0. Negative pairs (c, s ≤ −1) ↔ a = −h, b = −h′ ≥ m + 1,
a ≡ b ≡ +1 (m); then K = (c, h, N) has signs (−, −, +), one change, s_∞ = −1, (h′/N) = −s_2. Checked from scratch for
all odd N ≤ 301 and m < 40 (bijection both ways and the sign) — 0 failures.
Defect: the memo's "A trivial factorisation (a, b) = (1, 1 + Nm) is always in the +1 class. So negative-pair-type data
exist for every N, apart from the degenerate c = 0" is wrong as an argument — a = 1 **is** c = 0 (h = −1), which is
excluded by K_1 ≠ 0, so the trivial factorisation provides no negative-pair word. The conclusion is nonetheless true:
m = 1, a = 2, b = (N + 1)/2 gives the negative-pair word (−1, 1, (1 − N)/2) for every odd N ≥ 3 (but for m ≤ 2 the classes
+1 and −1 mod m coincide, so the "+1 vs −1 class" dichotomy is only meaningful for m ≥ 3) (D4).
Prop 2 (e-slice): Σ_e(N) = {ab⁻¹ mod e : ab | N} ∋ 1, −1 ↦ complex conjugation under (ℤ/e)* ≅ Gal(ℚ(ζ_e)/ℚ), and the ray
class group mod e (no infinite place) of ℚ is (ℤ/e)*/±1. So in the wide group "−1 ∈ Σ_e" becomes "1 ∈ Σ_e", trivially true.
Correct, but a tautology: the boldface "**the whole ES slice condition is the kernel of narrow → wide**" is imprecise —
the kernel is {±1}, and the condition is that Σ_e(N) meets the non-trivial kernel element. Also the "N" of the e-slice
form is (p + e)/4 or (pe + 1)/4, not the frieze N; §3.2 juxtaposes them without saying so (D4).

### SHARP 4 — CONJECTURE SQ_H (§6, memo y5_even_middle). Verdict: **SOUND** as EVIDENCE/CONJECTURE (scope wording to fix).

Equivalence re-derived: by mod-2 rigidity o ∈ {h, h′} ⟺ the even edge is {c, m} or {m, s} ⟺ m even (then c + s odd, so
exactly one outer letter e is even); the even pair is {m, e}, and the word is a certificate ⟺ 8 | ee′ = m·e
(FRIEZE Cor 1.3, N ≡ 1 (4)). Correct.

From-scratch census (`scripts/review_r211_census.c`: plain enumeration of all (c, m, s) ≥ 1 with
N = cms − c − s ≤ X, N ≡ 1 (4), no divisor shortcuts; log `logs/review_r211_census_1e7.txt`, X = 10⁷, 4.3·10⁸ words,
17 s):
* primes p ≡ 1 (8) ≤ 10⁷: 165 976; SQ_H fails at **0** (formal and interior). ✔
* primes p ≡ 1 (4) ≤ 10⁷ (332 180): formal SQ_H fails at 0 (so the memo's "to 10⁶ at primes ≡ 1 (4)" can be raised to
  10⁷); **interior SQ_H fails at 5 primes**, all ≡ 5 (8) (5, 13, 29, 53, 7589). The CONJECTURE must therefore say "positive
  (formal) letters" explicitly (D6).
* class C fails at 10 (formal) / 21 (interior) primes ≡ 1 (8), class M at 147 / 394, the 4 | m slice at 9 primes
  ≤ 10⁶ (409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321) and 14 ≤ 10⁷. ✔ (all as claimed)
* non-square N ≡ 1 (4) ≤ 10⁶ (249 500): **formal** SQ_H fails at exactly the 22 listed N (105, 1465, …, 392505), none
  prime ✔. Interior SQ_H fails at 114 such N — §6 does not say that the 22 refer to formal words (D6).
* SQ₅ fails formally only at 105 and in the interior only at {5, 105} ✔. Odd squares 9 ≤ n² ≤ 10⁶ (499): no certificate
  at all ✔ (T1 control; this is a theorem, so it is a code check, not evidence).
* Mean certificate counts (formal, c ≤ s) at p ≡ 1 (8) ≤ 10⁷: H 26.83, C 23.68, M 13.51; at p ≡ 1 (840): 19.41 / 15.90 /
  7.92; min formal H count 1 at 2521 and 53 881 ✔ (exact agreement). The interior H mean is 22.27.
The label CONJECTURE (EVIDENCE) and the Assessment "with mean count ~27 no failure is the lottery's prediction" are
appropriate.

### SHARP 5 + (b) — p = 21841 and the o* census (§2, memo y5_ocensus_hard_primes). Verdict: **SOUND-AFTER-REPAIRS**.

* p = 21841, exhaustive (`scripts/review_r211_p21841.py`, brute force over all c, m ≤ N + 2): 42 formal words,
  14 with χ = −1 (all certificates), 20 interior words; the interior certificates are exactly (9, 64, 38) and
  (38, 64, 9), o = h′ = 64·38 − 1 = 2431 = 11·13·17 ✔. Formal o* = 135 via (1, 135, 163) ✔.
  Factorisation 21841 = 1 + 2⁴·3·5·7·13 ✔.
* Census reproduced **exactly** at 10⁷ (both modes): o* = 7 for 156 416 (94.24 %, interior) / 157 186 (94.70 %,
  formal); 15: 6240/5513; 23: 2262/2290; first-success positions H 56 696, C 91 590, M 17 690 (interior), and
  the o* = 7 firing counts 55 432 / 141 236 / 109 333 ✔. Max interior o* = 2431 at 21841, unique; next 335 at 691 681;
  max formal o* = 239 at 6 154 009 ✔. "o* = 7 for 94 %" ✔.
* **Defect (D5).** The memo's hard-prime list "(interior, o* ≥ 119)" has 10 entries; there are **17** (missing
  372 121 (199), 501 841 (119), 944 329 (167), 1 749 001 (199), 3 975 721 (199), 7 183 201 (127), 8 586 481 (135)).
  The claim "Every one of them is ≡ 1 (mod 120)" (memo) / "the other hard primes are all ≡ 1 (120)" (§2) is **false**:
  6 154 009 (in the author's own list) and 944 329 are ≡ 49 (mod 120). The correct (and stronger) statement: all 17 are
  quadratic residues mod 840, p mod 840 ∈ {1, 121, 169, 361} = {1, 11², 13², 19²}. Also "least QNR prime ≡ 7 (8) between
  23 and 127" fails for the full list (8 586 481: 191). n_p ∈ {11, 13, 17, 19, 23, 29} holds for all 17.
* **Defect (D7).** memo y5_siegel_weil_chamber "Cheap numerics": "N = 21 841 has 34 formal words (12 with χ = −1, 2
  interior). N = 1 000 033 has 133 words (91 with χ = −1)". True counts: 42 / 14 (and 2 interior certificates; 20
  interior words) and 174 / 116. Cause: `y5_words_at.py` stops at c² > 4N + 10 although c can be as large as N + 1
  (e.g. (327, 1, 68), (326, 68, 1) at 21841). The conclusion (words are a vanishing fraction of ≍ p classes) is unaffected.

### (a) Five positions, P_h, C(o), and (J)26 (§2, memo y5_five_positions). Verdict: **SOUND-AFTER-REPAIRS** (one upgrade, wording).

* Parity table re-derived: (c, m) even ⇒ s odd, edge {c, m}, o = h; c odd, m even ⇒ s even, edge {m, s}, o = h′;
  c, m odd, s even ⇒ {s, h}, o = c; c even, m odd ⇒ s odd, {h′, c}, o = s; all odd ⇒ {h, h′}, o = m. The "N enters
  via" column (o | N + c, o | N + s, h ≡ −1 (o), h′c = N + o, hh′ = 1 + oN with h ≡ h′ ≡ −1 (o)) is correct.
  (Strictly the parity of (c, m) fixes the position only up to s when c, m are both odd.)
* Prop 1 (P_h): for fixed odd o the candidates c ∈ [2, (o+1)/2] are distinct mod o, so there is **at most one** P_h
  word with h = o at a given N, and it exists iff N mod o ∈ C(o) **and** s = (N + c)/o ≥ 1 (≥ 2 for interior), i.e.
  o ≤ N + c — a size condition the memo omits (D8). For 4 | o + 1, |C(o)| = τ((o+1)/4) exactly (c = 2d with
  d | (o+1)/4); the bound τ(o+1)/o in §2 can be replaced by this exact value.
* C(o) ⊂ Jacobi non-residues for o ≡ 7 (8): (−c/o) = −(2/o)^{v₂(c)}(c′/o) = −(c′/o), and (c′/o) = (o/c′)(−1/c′) = 1
  since o ≡ −1 (c′) and o ≡ 3 (4). ✔ Also via (N/o) = (o/N) = (h/N) = (h′/N) for N ≡ 1 (4). ✔
* From-scratch check (`review_r211_identities.py`, item(a)): for all o ≤ 4000, o ≡ 7 (8): every element of C(o) is a
  unit with (x/o) = −1 and |C(o)| = τ((o+1)/4); for all N ≡ 1 (8) < 2000 and all o ≡ 7 (8) ≤ N + 200 the P_h words
  match Prop 1 (with the size condition). 0 failures.
* "For o = q prime … Equality holds only for q = 7 (C(7) = {3, 5}; with formal c = 1 or c = q + 1 one also gets 6)":
  |C(7)| = 2 < 3 = #non-residues mod 7, so there is no equality; the class 6 (mod 7) comes from the words (1, 8, s)
  (o = h′ = 8s − 1, not 7) and (8, 1, s) (o = s), which are not P_h words with o = 7 (D8).
* T1 per position ✔ (a prime ℓ | (o, n) would divide c | o + 1; gcd(h′, N) = 1).
* **(J)26 relation — can be upgraded.** §2 labels "the P_h classes are ET Prop 1.9 classes" an Assessment. It is in fact
  provable from ET's own Prop 1.9 (read in sources/elsholtz-tao-1107.1010.pdf, p. 7–8): for fixed even (c, m) the class
  N ≡ −c (mod o), o = cm − 1, is primitive (o ≡ −1 (mod c)), and the vertex-fan identity of the certificate vertex gives
  4/N as three unit fractions whose denominators are polynomials in the letters and N, hence in N on the class (s =
  (N + c)/o), positive for large N. So the class is *solvable by polynomials* in ET's sense, hence (ET: "every solvable
  primitive residue class is either Type I or Type II solvable") all large primes in it lie in finitely many classes of
  the ET Prop 1.9 families. Therefore a bound o_h*(p) ≤ F(r) for all large primes p ≡ 1 (24) with n_p = r (prime r ≥ r₀)
  would give a finite ET covering, contradicting DEPTH_ASPECT Thm 3.1 ((J)26). The conclusion "no bound o_h*(p) ≤ f(n_p)"
  is thus **PROVED relative to (J)26 Thm 3.1** (and to the routine vertex-fan identities), for P_h; it says nothing for
  o* over all positions (P_c, P_m with bounded o are not finite congruence families). Recommend relabelling (D9).
* The heuristic Σ_{o ≤ Y, o ≡ 7 (8)} |C(o)|/o ≍ log² Y is right (= Σ_{d ≤ Y/4, d even} τ(d)/(4d) up to O(1)).
* memo y5_ocensus_hard_primes "A bound o* ≤ (log p)^C … would yield QNRs": only a P_h certificate yields a small QNR
  ((p/o) = −1, so o has a prime factor that is a QNR); a small o* attained in P_c/P_m forces no small non-residue.
  Restrict the sentence to o_h* (D10).

### (c) No mod-16/32 shadow (§4, memo y5_mod16_shadow). Verdict: **SOUND** (as EVIDENCE).

From-scratch (`scripts/review_r211_mod32.py`, log `logs/review_r211_mod32.txt`): all formal words with N ≡ 1 (8),
χ = +1, compared at odd squares vs non-squares, per class N mod 32. At (position, o mod 32): all 20 cells are populated at
squares in every class, at X = 10⁵ and 4·10⁵ (word counts match the author's 2002/2004/2057/2005 up to the 5 words at
N = 1, which I include). At my finer resolution (position, o, e, e′ all mod 32; 320 cells per class) the
empty-at-squares cells drop from 61–74 per class (X = 10⁵) to 8–20 (X = 4·10⁵), max expected square count ≈ 3.3, and no cell
is populated only at squares — consistent with sampling (square words come in clusters of ~30 per N and mirror pairs,
so the Poisson model is optimistic). EVIDENCE label is right. The heuristic "the only global link is the one
product-formula bit" is an Assessment (the spinor-genus remark is unproved, as the memo says).

### (d) Siegel–Weil (§5, memo y5_siegel_weil_chamber). Verdict: **SOUND** (numerics in the memo wrong, see D7).

* r(L, G) = |Aut L|·[L ≅ G] for rank L = rank G (an isometric embedding of equal-determinant lattices is an
  isometry), so the genus average is 1/mass on gen(G) and 0 elsewhere. ✔ (Siegel's local-density form for m = n carries the
  extra factor 2, ε_{m,n} = 1/2; irrelevant to the conclusion.)
* |𝔊⁻_p| ≍ p: CONSTRUCTIVE_ES Thm 2.1 + the R199 count ≈ p/16 (Eichler mass for level 2, orbits of size ≤ 4). ✔
  ("genus G₋(p)": CONSTRUCTIVE_ES defines 𝔊⁻_p as a set of classes with ε = −1; whether it is a single 2-adic genus was not
  checked — immaterial for ≍ p.)
* Number of words at N ≪ N^{1/3+o(1)}: re-derived — the least letter is ≤ N^{1/3}+O(1); if it is m, the word is fixed by
  a divisor of 1 + mN; if it is c (or s), by a divisor h of N + c (h ≡ −1 (c)); so ≤ Σ_{t ≲ N^{1/3}} (τ(1 + tN) + 2τ(N + t))
  = N^{1/3+o(1)}. ✔ ((J)26 by-product.) Hence path-basis classes are a p^{−2/3+o(1)} fraction. ✔ (Assessment reading OK.)
* Numerical illustration wrong (D7, above).

### Other checks
* r-uniqueness (§3 bullet; memo Thm 2): K(2^i, x, 2^j) = xIJ − (I−1)J − I(J−1), A − B = I(x − 2) + 1 = 9; N = (2A + 3)²
  ≡ 9 (A), k = (N + B)/A ≥ 2. ✔ Duplicate of R208/FRIEZE §4, correctly flagged.
* "The product depends only on Q_a ⊗ ℤ₂, hence on the word mod 8" (memo): true (unimodular ℤ₂-lattices congruent mod 8
  are isometric); checked from scratch on 100 000 pairs w, w + 8t (N odd): s₂ unchanged in all.
* "r = 3 recovers FRIEZE Thm 1.2": Thm 3.1 at r = 3 gives (h/N) = (c, −h)₂(h, −N)₂ = CHI_FLIP Thm 1.1; turning this into
  the closed form (−1/N)(−1)^{[8 | ee′]} still needs the mod-8 cell evaluation (or FRIEZE's 3-case proof). "Recovers" →
  "implies, after a finite mod-8 evaluation" (D11, minor).

## Defects

No FATAL. Two MAJOR (one is a ledger correction outside the reviewed document), nine MINOR.

* **D1 (MAJOR — ledger, DISCOVERIES (J)42 "Transport law" bullet; FRIEZE_ES §2/§7 wording).** "o ≡ ±1 (mod 8)" /
  "o ≡ ±3 (mod 8)" are misleading (o ≡ 3 (4) for every word at N ≡ 1 (8)), and "Hilbert reciprocity localised" /
  "transportable to a small modulus o" overstate the content. *Repair:* the replacement text under SHARP 1 above; add a
  pointer "(deflated by O213 §1 / R211: Thm 1.2 + one Ptolemy relation; −(2/o) = o mod 8)". To be applied by the
  maintainer on main (not in this branch).
* **D5 (MAJOR — misread evidence; TRANSPORT_LAW §2 census bullet "the other hard primes are all ≡ 1 (120)", memo
  y5_ocensus_hard_primes "Hard primes" paragraph, O213 report (b)).** The hard-prime list "(interior, o* ≥ 119)" omits
  7 of 17 primes, and "≡ 1 (mod 120)" is false for 6 154 009 (in the list) and 944 329 (both ≡ 49 = 7² (mod 120)); "least
  QNR prime ≡ 7 (8) between 23 and 127" fails for 8 586 481 (191). *Repair:* list all 17 (interior: 21841, 238681,
  372121, 501841, 691681, 944329, 981481, 1249921, 1749001, 3191281, 3975721, 4362121, 6154009, 7183201, 7940521,
  8586481, 8984641; formal o* ≥ 119: the same minus 372121, 501841) and replace the congruence statement by "all are
  quadratic residues mod 840 (p mod 840 ∈ {1, 121, 169, 361}), n_p ∈ {11, 13, 17, 19, 23, 29}" (R211-verified).
* **D2 (MINOR; §7 "CERTIFIED / EVIDENCE: … T1 controls (499 odd squares) clean").** The absence of certificates at odd
  squares is FRIEZE Cor 1.4 (a theorem); the run is a code sanity check, not evidence. *Repair:* say so.
* **D3 (MINOR, novelty; §3 Assessment "What it adds is the explicit ∞-factor", memo y5_general_r_jacobi).** The
  ∞-factor (−1)^{#{K_i < 0 < K_{i+1}}} = ∏(K_i, −K_{i+1})_∞ is the real local Hilbert/Kubota factor of the same
  leading-minor formula; it is as classical as the 2-adic part. *Repair:* "Thm 3.1 is the leading-minor Hasse invariant
  + product formula (classical); new is only its frieze-notation reading (one 2-adic factor per continuant step; s_∞ as
  a sign-change count). Not located verbatim in the literature by O213/R211 (Kubota 1969; Bach–Shallit 1996;
  Girstmair 2011 not read in full)."
* **D4 (MINOR; §3.2, memo y5_narrow_wide Prop 1 last bullet, report SHARP 3).** "A trivial factorisation (1, 1 + Nm)
  is always in the +1 class. So negative-pair-type data exist for every N, apart from the degenerate c = 0": the trivial
  factorisation *is* c = 0, so it gives no word. *Repair:* "negative-pair words exist for every odd N ≥ 3, e.g.
  (−1, 1, (1 − N)/2); the ±1 dichotomy is meaningful only for m ≥ 3". Also: "the whole ES slice condition is the kernel
  of narrow → wide" → "the slice condition asks Σ_e(N) to meet the non-trivial element (complex conjugation) of
  ker((ℤ/e)* → (ℤ/e)*/±1)"; and note that the e-slice "N" is (p + e)/4 resp. (pe + 1)/4, not the frieze N.
* **D6 (MINOR; §6 and memo y5_even_middle).** (i) SQ_H must state "positive (formal) letters": interior SQ_H fails at 5
  primes ≡ 5 (8) (5, 13, 29, 53, 7589). (ii) The "22 composite exceptions" are formal-word exceptions (interior: 114).
  (iii) Memo "Each … has a small factor (3, 5, 7, 13, …)" and report spark 3 "all have a small odd factor" are false:
  199 369 = 193·1033. (iv) Worth recording: all 22 are ≡ 1 (mod 8) (formal SQ_H never fails at N ≡ 5 (8) ≤ 10⁶).
  (v) The formal SQ_H range at p ≡ 1 (4) can be raised to 10⁷ (R211: 0 failures among 332 180 primes).
* **D7 (MINOR; memo y5_siegel_weil_chamber "Cheap numerics").** Word counts wrong because `y5_words_at.py` truncates at
  c² > 4N + 10: N = 21 841 has 42 formal words (14 with χ = −1; 20 interior words, 2 interior certificates), not 34/12;
  N = 1 000 033 has 174 (116), not 133 (91). *Repair:* fix the loop bound (c ≤ N + 1) and the numbers.
* **D8 (MINOR; memo y5_five_positions Prop 1 and "o = q prime" bullet; §2).** Prop 1 omits the size condition
  s = (N + c)/o ≥ 1 (≥ 2 interior), and should say there is at most one P_h word per o; |C(o)| = τ((o+1)/4) exactly.
  "Equality holds only for q = 7" is false (|C(7)| = 2 < 3); the class 6 mod 7 comes from words with o ≠ 7.
* **D9 (MINOR, upgrade; §2 bullet on (J)26).** The identification of P_h classes with ET Prop 1.9 classes follows from ET
  Prop 1.9 itself (polynomial solvability + "every solvable primitive class is Type I or II solvable"); relabel the
  conclusion "no bound o_h*(p) ≤ f(n_p)" as PROVED relative to (J)26 Thm 3.1, and state it per fixed prime r ≥ r₀.
* **D10 (MINOR; memo y5_ocensus_hard_primes "Burgess-free?").** "o* ≤ (log p)^C … would yield QNRs" holds only for o_h*
  (P_h forces (p/o) = −1); restrict.
* **D11 (MINOR; §3 "r = 3 recovers FRIEZE Thm 1.2", memo).** Thm 3.1 at r = 3 is CHI_FLIP Thm 1.1; the ee′ closed form
  needs a further mod-8 evaluation. *Repair:* "implies, after the mod-8 evaluation".

## Ledger recommendation
(J)42 as in D1. A possible (J)43 entry for O213: SHARP 1 (deflation, PROVED), Thm 3.1 (PROVED, classical in substance),
P_h + the (J)26 consequence (PROVED relative to (J)26 after D9), SQ_H (CONJECTURE, EVIDENCE to 10⁷, formal letters),
p = 21841 fingerprint (CERTIFIED, exhaustive), hard primes square mod 840 (EVIDENCE, D5).
