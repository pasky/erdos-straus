# R219 — hostile review of O218 (SYNTHESIS_SPARKS4.md + BRAINSTORM/s4_*.md)

Reviewer branch `side-agent/review-synthesis-four` (merged `side-agent/synthesis-four`). From-scratch scripts:
`scripts/review_r219_*`. ES is not solved; nothing below changes that.

## Summary verdicts
(in progress)

## Defects

### D1 (MAJOR) — "signed" means two different things; the SQ_± record |t| ≤ 18 is false for the stated definition
*Location:* SYNTHESIS_SPARKS4 header ("'signed' = t u v ≠ 0, not positive"), §2.1 (R_n) (no "not positive"),
§2.5 bullets + CONJECTURE SQ_± ("some *signed* point"), s4_three_bits_meta P3(c), AGENT_REPORT SHARP 1;
`scripts/s4_sqpm.c` line 1 ("SIGNED word (t,u,v nonzero …)" — positive words included).
*Finding (from-scratch `scripts/review_r219_sqpm.c`, cross-checked by the factoring-free brute force
`scripts/review_r219_bruteword.py`):* every number in §2.5/§2.4 is reproduced **exactly** when the search admits
*all* words with t u v ≠ 0 (positive ones included): records 15 @ 97 185 (≤ 10⁶), 18 @ 4 884 441 (≤ 10⁷); |t| ≤ 6
failures 15 / 62 / 403 (≤ 10⁵/10⁶/10⁷); |t| ≤ 12 failures 8 (≤ 10⁷: 34 489, 97 185, 895 609, 3 567 369, 3 781 761,
4 884 441, 5 737 449, 8 351 385). Positive ES-five ≤ 10⁶: fails only at 105, record 231 @ 702 585 (reproduced).
But with the header's definition (signed = not positive) the least |t| is **not** ≤ 18:

| range | strictly-signed failures | record least \|t\| (strictly signed) | |t|>6 | |t|>12 |
|---|---|---|---|---|
| ≤ 10⁵ | 0 | 19 @ 60 369 | 34 | 7 |
| ≤ 10⁶ | 0 | 30 @ 297 465 | 203 | 34 |
| ≤ 10⁷ | 0 | 54 @ 9 817 305 | 1 277 | 156 |

Example (brute force, no factoring): n = 60 369 has positive χ = −1 words at t = 4, 5, 7, but the first strictly
signed χ = −1 word is (−19, 6, −525) (A = −115). So the *existence* half of SQ_± survives with either reading (0
failures ≤ 10⁷ for strictly signed words — the 105 statement is fine), but "least |t| ≤ 18", "403 vs 10 550" and
"8 vs 996" compare (signed ∪ positive) against positive, i.e. they measure ES-five *plus* signed tickets, not "signed
instead of positive". The quantitative "positivity is not the bottleneck" reading of §2.6 must be re-stated: dropping
positivity *and keeping* the positive words is easier (trivially ⊇ ES-five), while the strictly-signed problem alone
has a least-|t| record (54) far below ES-five's (231) but well above 18.
*Repair:* define (R_n) and SQ_± with "t u v ≠ 0" (positive allowed) — this is what was computed and is the natural
T1-keeping relaxation — and say so in the header; add the strictly-signed numbers above as a separate line
("even without positive words: 0 failures ≤ 10⁷, record 54 @ 9 817 305"); fix the comment in s4_sqpm.c.

### D2 (MINOR) — §2.3 "positivity costing nothing at these t" is false at t = 6
*Location:* SYNTHESIS_SPARKS4 §2.3, sentence after the table.
*Check:* re-derived the table (for n ≡ 1 (8): (−A/n) = (|A|/n); for an odd prime q | tn + 1, (q/n) = (n/q) = (−t/q);
since (ℤ/t)* = {±1} and gcd(d, t) = 1, a divisor d ∉ {1, |tn+1|} can be signed into A ≡ −1 (mod t), A, B ≠ −1; total
symbol of |tn+1| is +1, so a χ = −1 divisor exists iff some prime factor has (−t/q) = −1). All ten rows are correct:
`scripts/review_r219_slots.py 40000` — 4 900 non-squares n ≡ 1 (8), 0 mismatches between brute force and the table.
For **positive** words, A > 0 forces d ≡ −1 (mod t), and (d/n) = (−t/d) (Kronecker). For t = 1, 2, 3, 4 this is
automatic ((−3/d) = (d/3), (−4/d) = (−1/d)). For t = 6 it is not: (−6/d) = −(2/d) when d ≡ 5 (6), so the positive
t = 6 slot holds iff **6n + 1 has a divisor ≡ 17 or 23 (mod 24)** (0 mismatches on the same 4 900 n), and it differs
from the signed t = 6 slot at **694 of the 4 900 n** (first: n = 41, 6n + 1 = 13·19, both ≡ 1 (6); A = −13 gives a
signed word (6, −2, −41) with χ = −1, but no positive t = 6 word).
*Repair:* "positivity costs nothing at t = 1, 2, 3, 4; at t = 6 the positive slot needs a divisor ≡ 17, 23 (mod 24)".

### D3 (MAJOR → repairable) — §2.4 "no finite t-set" sketch: the argument is fixable, cleaner than stated, and needs only Dickson's conjecture
*Location:* SYNTHESIS_SPARKS4 §2.4; s4_three_bits_meta P3(d).
*Problems as written:* (i) "(bounded power of 2 and 3) × prime" — without fixing n ≡ 0 (mod p) for each odd prime
p ≤ 2T + 1 the tuple is never admissible (e.g. p = 5: the residues −1/t, t ∈ {±1, ±2}, cover (ℤ/5)*, so 5 divides one of
n ± 1, 2n ± 1 unless 5 | n); the "suitable modulus" is left unspecified. (ii) "signs fixed by congruences … +1 or
excluded (to be checked per T)" is an unproved per-T case analysis. (iii) Only *linear* polynomials occur, so the
right hypothesis is Dickson's conjecture, not full Schinzel H.
*Repaired argument (CONDITIONAL on Dickson's prime k-tuples conjecture; I regard it as a complete proof modulo
Dickson).* Fix T. Let P = ∏ odd primes p ≤ 2T + 1 and take n ≡ 0 (mod P), n ≡ r (mod 2^K) with r ≡ 1 (8) and K large
(so v₂(tn + 1) = a_t is fixed). For p | P, tn + 1 ≡ 1 (mod p); for p > 2T + 1 the 2T linear forms
f_t(k) = (t n(k) + 1)/2^{a_t} cannot cover ℤ/p; so the tuple {f_t : 1 ≤ |t| ≤ T} has no fixed prime divisor and Dickson
gives infinitely many n with every |tn + 1| = 2^{a_t}·q_t, q_t prime. For such n ≡ 1 (8): (2/n) = (−1/n) = 1 and
(q_t/n) = (|tn+1|/n) = 1, so **every** divisor A of tn + 1 has (−A/n) = +1 — no sign analysis needed. Finally n−1 =
2^{a}q with a fixed excludes all but finitely many squares. Hence for every T there are infinitely many odd non-square
n with no χ = −1 word (signed or positive) of |t| ≤ T. Numerical illustration `scripts/review_r219_dickson.py 3`:
n = 7 665, 29 505, 202 545 have all |tn + 1| (|t| ≤ 3) of the form 2^a·prime and indeed no χ = −1 word at |t| ≤ 3.
*Repair:* replace §2.4 by the above; label CONDITIONAL (Dickson).

### D4 (MINOR) — §2.2: the prime 2
"the sign is a genus character ψ_t(q) = (−t/q) of the prime factors" omits q = 2: for odd t, 2 | tn + 1 and
χ(2) = (2/n), which is −1 for n ≡ 5 (8). Harmless (n ≡ 5 (8) is settled by Prop 2.1(c)) but state "for n ≡ 1 (8)" or
add the factor (2/n)^{v₂(tn+1)}.

### D5 (MAJOR, upgrade) — the three-bit law for signed words is PROVABLE now; label CERTIFIED undersells it, and the ε_∞ sign convention is garbled
*Location:* SYNTHESIS_SPARKS4 §1 "Three-bit law (… CERTIFIED for all signed …)", s4_three_bits_meta "Three bits",
s4_kudla_green_infinity K2 (relies on it), AGENT_REPORT "Points for the reviewer".
*Proof (reviewer; all steps positivity-free).* Let w ∈ X_n(ℤ), n odd > 0, t u v ≠ 0; ε_v = +1 iff Q_w is ℚ_v-isotropic.
1. For odd ℓ, CHI_FLIP Thm 1.1's local computation ε_ℓ = (−A/ℓ)^{v_ℓ(n)} uses only that B = tv − 1 (the 2×2 leading
   minor) is an ℓ-unit when ℓ | n (B | tn + 1) and unimodularity when ℓ ∤ 2n — no positivity. So ∏_{ℓ odd} ε_ℓ = χ(w).
2. Hilbert reciprocity for C₀(Q_w): χ = ε₂·ε_∞.  3. L1: ε_∞ = −1 ⟺ w positive.
4. ε₂ is a function of (t, u, v) mod 8 (CHI_FLIP Cor 1.2, R198 Hensel lemma, positivity-free); the certificate is a
   function of w mod 4.
5. On positive words certificate ⟺ χ = −1 ⟺ ε₂ = +1 (MODEL_SPECIFIC 3.1(a) = the 240 χ = −1 cells). Every one of the
   320 odd-n cells mod 8 contains positive words (letters in [9, 16]), so certificate ⟺ ε₂ = +1 is a **cell identity**,
   valid for all words.
6. Signed w: ε_∞ = +1, so χ = ε₂, i.e. certificate ⟺ χ = +1 ⟺ χ·s_∞ = −1. ∎
(The route via TRANSPORT Thm 3.1 is the same: its 2-adic factor is ε₂ up to (−1, −n)₂, a function of n mod 4.)
*From-scratch check* `scripts/review_r219_threebit.py 1001` (own Hilbert symbols at 2, ∞ and odd ℓ on ⟨v, vB, nB⟩, all
words with |t| ≤ n + 3): 77 658 words (56 260 signed), 320 cells; 0 violations of each of (a) χ = ε₂ε_∞, (b) certificate
⟺ ε₂ = +1, (c) certificate ⟺ χ·s_∞ = −1, (d) ε_∞ = −1 ⟺ positive, (e) ε₂ constant on cells mod 8, (l) ε_ℓ =
(−A/ℓ)^{v_ℓ(n)} for all ℓ | n.
*Convention defect:* §1 writes "ε_∞ε₂ε_n = 1 … the ∞-factor is (−1)^{ind_−(Q_w)/2}". With ε = isotropy signs, ε_∞ = −1
iff ind_− = 0, whereas (−1)^{ind_−/2} = +1 iff ind_− = 0: the two differ by a global sign (−(−1)^{ind_−/2} = ε_∞;
TRANSPORT's s_∞-factor is the Hilbert-symbol-product normalisation, not the isotropy one).
*Repair:* label the three-bit law PROVED (all words), cite the 6-step proof; write ε_∞ = −(−1)^{ind_−/2} = −s_∞;
K2 of s4_kudla_green_infinity then becomes PROVED unconditionally.

### D6 (MINOR) — §1 meta-statement (a) is not "PROVED as stated"; (R₂) at odd squares is provable in one line
*Location:* SYNTHESIS_SPARKS4 §1 "Meta-statement (PROVED as stated …)" item (a); §5 first bullet; s4_three_bits_meta P3 (R₂).
(i) "R ⊄ D ⇒ the conclusion is true at every odd square" is false for arbitrary R (take R = D ∪ a small disc in the
other part of X_n(ℝ) avoiding all integral points). What is true: X_n(ℝ) ∖ D is where signed words live, and *if* the
argument's conclusion is insensitive to replacing D by X_n(ℝ) ∖ D (or R ⊇ X_n(ℝ) ∖ D) it proves a statement true at odd
squares. Reviewer's side remark: X_n(ℝ) has exactly two components (D and the rest — the graph u = (n + v)/(tv − 1) over
{tv < 1} and over {t, v < 0, tv > 1} are glued along the smooth line {t = −1/n, v = −n}), so "R meets a component other
than D" and "R ⊇ X_n(ℝ) ∖ D" differ only by this quantifier. Repair: state (a) with "R ⊇ X_n(ℝ) ∖ D" and label (a) an
Assessment/heuristic, keeping only "ES-five(n) ⟺ X_n(ℤ) ∩ (D × Ω₂) ≠ ∅" as PROVED.
(ii) "signed certificates exist at odd squares: CERTIFIED at all 24 odd squares ≤ 2501" can be PROVED for all odd
n ≡ 1 (8): w = (−1, 1, −(n + 1)/2) has A = −2, B = (n − 1)/2 ≡ 0 (mod 4) — a certificate (and χ = (2/n) = +1, consistent
with D5). Repair: replace CERTIFIED by this one-liner.

### D7 (MINOR) — s4_selling_voronoi_wall: algebra SOUND, citation unverified, a heuristic count mislabelled
*Checks.* Lemma S identity and its converse re-derived by hand (Gram of (e₁, e₂, e₃) with conorms p₁₂ = p₂₃ = 1,
p₁₃ = 0 has off-diagonals (−1, 0, −1) and diagonals (p₀₁ + 1, p₀₂ + 2, p₀₃ + 1)) — SOUND. Lattice invariance: I could
not access Conway–Sloane, *Low-dimensional lattices VI* (Proc. R. Soc. A 436 (1992) 55–68; not in sources/). Instead
I checked its key lemma independently (`scripts/review_r219_vonorm.py`): for 400 random positive words the 7 coset
minima of L/2L (brute force over a box, no superbase used) equal the 7 superbase vonorms predicted from the conorms
{1, 1, 0, v − 1, t − 2, u − 1}; 0 mismatches. Since conorms are a GL₃(𝔽₂)-equivariant linear function of the vonorm
function, the conorm *multiset* is a lattice invariant, as claimed (the labelling — which face carries (1, 1, 0) — is
not, when a conorm vanishes: then the obtuse superbase is non-unique; the memo's construction 2 acknowledges this).
The Voronoi-cell name (one of the six conorms zero ⇒ hexa-rhombic dodecahedron) matches my memory of CS VI / Fedorov
but is likewise unverified. *Defect:* "the wall-with-unit-conorms lattices of det p are the ≍ log²p positive words"
is a heuristic average (Σ_t d(tp + 1)/φ(t)), not a pointwise bound; label it so. Also say explicitly that ES-five
here means interior (t ≥ 2) and that "two zero conorms" counts CS's always-zero seventh conorm.

### D8 (MINOR) — s4_kudla_green_infinity: K1 SOUND; K2 SOUND and now unconditional, but its stated dependencies are off
*Checks.* K1 re-derived: T_w = [[B, 1], [1, A]], det tn; t < 0 ⇒ indefinite; t > 0, w signed ⇒ v < 0 (tv = 1 forces
n = −1) ⇒ B < 0, det > 0 ⇒ negative definite. SOUND. For K2 the clean route is: the algebra of T_w is B_T = (−B, −tn),
and **B_T ≅ C₀(Q_w) place by place** — checked from scratch (`scripts/review_r219_kudla.py 1001`: inv_v(−B, −tn) =
ε_v(Q_w) at v = 2, ∞, every ℓ | n and every odd ℓ | t, on all 77 658 words of odd n ≤ 1001; 0 failures; T_w pos. def.
⟺ w positive, 0 failures; at odd squares |Diff| odd and Diff = {∞} ⟺ certificate on all 2 281 square-n words, 0
failures). Then K2 follows from D5 (three-bit law, now PROVED) plus the (J)13 identification Diff(T) = Ram_fin(B_T)
∪ ({∞} if T is not positive definite), which is local at each finite place and hence sign-blind.
*Defects.* (i) The K2 label "given the three-bit law … CERTIFIED" — upgrade to PROVED (D5). (ii) "no ℓ ∤ 2n lies in
Diff" needs one line for ℓ | t (T_w is not ℓ-unimodular there): −B ≡ 1 (mod t) is an ℓ-adic square, so (−B, −tn)_ℓ = 1.
(iii) The memo cites "(J)13" for 2 ∉ Diff ⟺ certificate; (J)13 concerns the modular-curve collection where ES
tuples clear 2 by their congruences; the Eichler-level-2 dictionary at n = p is TWO_FIBRES/(J)39 Prop 4.1. Cite both
and state which incoherent collection is meant (C_∞ definite, C_ℓ split for ℓ < ∞). Novelty: a re-reading (agreed).

### D9 (none) — s4_maslov_inertia: SOUND
Lemma I is Jacobi's signature rule (inertia = number of sign changes in 1, K₁, …, K_r when no K_i = 0); with K₀ = 1 > 0
and K_r > 0 the up-changes are exactly half, so μ = ind_−/2. The r = 3 corollary (ind_− ∈ {0, 2}, μ even ⟺ definite ⟺
positive, by L1) is correct; my three-bit script confirms ε_∞ = −1 ⟺ positive on 77 658 words. Not re-running the
75 097-word certificate is acceptable: it is a direct corollary of Sylvester/Jacobi. Only defect: the convention
clash noted in D5 (the "∞-factor" (−1)^{ind_−/2} is s_∞, not the isotropy sign ε_∞ = −s_∞). Label "PROVED, classical"
is right; promise 0/5 is honest.

### D10 (MINOR) — remaining memos
(a) **s4_three_bits_meta P3(c)** "≈ 75.5 signed χ = −1 words on average versus ≈ 33.7 positive ones (primes ≤ 1001)":
same confusion as D1. `scripts/review_r219_counts.py 1001` (primes 5…997): strictly signed 42.1, positive 33.8,
all 75.9 per prime. So "signed" there = all words. Repair: "≈ 42 strictly signed + ≈ 34 positive".
(b) **s4_mute_infinity** row (R₂) "trivial": it is in fact PROVED for every odd n ≥ 5 at t = −1 (AB = 1 − n): n ≡ 1 (4):
A = 1, w = (−1, −2, n − 2); n ≡ 7 (8): A = −2; n ≡ 3 (8): A = 2 (χ = +1 in each case, so a certificate by the three-bit
law; brute-force confirmation that a t = −1 signed certificate exists for all odd n ∈ [5, 1001], same script). Say so.
The (R_n) row's "no finite t-set under H" → "under Dickson" (D3); "slots doubled" fine.
(c) **s4_two_and_infinity**: "B_{2,∞} … is precisely the C₀ of every non-certificate positive word" holds at n = p
prime only; for composite n a non-certificate positive word has C₀ ramified at {2, ∞} ∪ {ℓ | n : ε_ℓ = −1}, an even
number of extra ℓ's (e.g. TWO_FIBRES' (1, 2, 23) ∈ X₂₁). Also "(C₀ ≅ B_{2,∞} ⟺ embeds as a Gram of integer vectors)"
must read "n·G_w is a Gram of integer vectors" (TWO_FIBRES Thm A(iv)) or "T_w is" (A(iii)). The "ES-five(p) ⟺ not every
positive path lattice is Hamiltonian" is TWO_FIBRES Cor A1 verbatim — mark as a restatement, not a new consequence.
(T1-place lemma (a) re-derived: trivial and correct.)
(d) **s4_minkowski_sail**: Lemma M re-derived ((cm − 1)s = p + c ≡ c; χ = (−cs/p)) — SOUND. Tool 1's "50.0 %" is not
an empirical finding: for p ≡ 1 (4), A ↦ −A preserves the QNR class and Λ_{−A} is the reflection of Λ_A, which swaps
the open quadrant pairs, so the split is exactly ½ by symmetry (PROVED). Tool 2 (sail ↔ HJ of p/A, other quadrant ↔
p/(p − A)) matches the classical toric picture (Oda §1.6, not re-read). Tool 3 example correct (x + y ≡ 0 (p), x, y ≥ 1
⇒ xy ≥ p − 1).
(e) **s4_real_analytic_tools** §1: "path basis is a thin extraction, ≪ p^{1/3+o(1)} of ≍ p classes" — the exponent 1/3
is unsupported (no proof or citation; the selling memo says ≍ log²p on average; the known pointwise bound for ES
solution counts is Elsholtz–Tao's n^{3/5+o(1)}). Repair: cite or replace by "p^{o(1)} on average (≍ log²p heuristically)".
"θ(−1/τ) *is* the product formula" is an Assessment, not an identity; label it. Verdicts (COLLAPSES) agree.
