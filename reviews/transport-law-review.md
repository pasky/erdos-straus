# R211 — hostile review of O213 TRANSPORT_LAW.md (+ BRAINSTORM/y5_*.md)

Reviewer: R211 (side agent). Scope: TRANSPORT_LAW.md, the eight memos BRAINSTORM/y5_*.md, logs/y5_*, the
O213 report. All numerics below were redone with from-scratch code (`scripts/review_r211_*`); the author's
scripts were not run or reused.

## Summary verdicts (in progress)

| claim | verdict |
|---|---|
| SHARP 1 transport = Ptolemy mod 8 | (pending) |
| SHARP 2 general-r Jacobi law | (pending) |
| SHARP 3 narrow/wide dictionary | (pending) |
| SHARP 4 SQ_H | (pending) |
| SHARP 5 p = 21841, o* census | (pending) |
| (a) P_h, C(o), (J)26 | (pending) |
| (b) census | (pending) |
| (c) no mod-32 shadow | (pending) |
| (d) Siegel–Weil | (pending) |

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
(D_i, −1)(D_i, D_{i+1})·... = (D_i, −D_{i+1}), using (a, a) = (a, −1). (ii) At odd ℓ ∤ N the ℤ_ℓ-lattice is
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
"Jacobi symbol (K_{r−1}/K_r) = product of local symbols at 2 and ∞ along the continued fraction" is the classical
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

## Defects
(numbered list follows)
