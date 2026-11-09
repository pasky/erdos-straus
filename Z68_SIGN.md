# Z68_SIGN — long-word sign information vs length-3 words: one exact partial contraction to length 3 is characterised (its domain = refinements of L₃; it excludes long bounded-digit words), and finite-family congruence selectors from length 4/5 to length 3 are obstructed. Verdict: NARROWED; HOT LEAD: no

**ES is OPEN; nothing here proves or disproves ES, (S), SQ₅ or (MS).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief: `z52bbriefs/z68_lanes.md` §SIGN
(+ `z53_depth.md`, `z58_lanes.md` common rules / falsifier table). Scripts `scripts/z68_sign_*`, data `data/z68/sign/`.
Checkpoint 1 (falsifier table, gate log, kill tests KT1–KT4 registered before any computation): commit 0e96b6f17.
Internal hostile review (deep mode; reviewer model gpt-6-astra): §8, all findings applied.

Notation (DEDEKIND_ES = DK, Z64_SDEEP, Z64_SDEEPF, Z66_UCOVER = UCOVER, Z67_ELL0 = ELL0). Throughout n is **odd**.
HJ word n/A = [[b₁,…,b_r]], b_i ≥ 2, r = r(n/A); continuant K(b₁..b_r) = n, A = K(b₂..b_r), K(∅) = 1, and K of
"length −1" is 0; L_r(n) = {A : r(n/A) = r}; length-3 words n/A = [[v,t,u]] ⟺ tuv − u − v = n, A = tu − 1 (DK Lemma
1.1); χ_n(A) = (A/n) (Jacobi). λ(n) = min{r(n/A) : χ_n(A) = −1} (DK Cor 4.6). (S)(n): some A ∈ L₃(n) has
χ_n(A) = −1; at primes p ≡ 1 (4), p > 5, (S)(p) ⟹ ES(p) (DK Thm 4.5). A word is *good* if χ_n(A) = −1.

## Bottom line

The gate asked for an exact map from a p-adaptive long-word object with controlled sign to a good length-3 word.
**What was found (PROVED, elementary).** Every word of n, cut at a letter b, is a "length-3 word with fractional outer
letters": n = b·X·Y − X·Y′ − X′·Y with χ_n(A) = χ_n(XY) (Lemma 1; classical continuant identities, formulated here).
If the cut is interior, X′Y′ ∣ b and b ≥ 2X′Y′, then (b/X′Y′, X′Y, XY′) is a length-3 word of n with
χ_n(A₃) = χ_n(A)·χ_n(X′Y′) (Theorem 3, *contraction*). This is a **partial, sign-corrected, numerator-preserving map**,
not a good-to-good transport (a good input can give a bad output: p = 137, §2). Its domain is exactly the set of
*refinements* of length-3 words — factorisations of the outer letters u = X′Y, v = XY′ (Prop 4, a bijection) — and its
divisibility hypothesis is, for fixed outer data, the W2 class n ≡ −(u+v) (mod uv). **No word with HJ letters ≤ M′
and length > M′/2 + 2 is in its domain** (Prop 5), so long bounded-digit witnesses (ZQ_M / Zaremba(M), fable-6's
objects, whose length is ≫ log p) cannot be contracted directly. **Obstruction for one natural class of transports
(PROVED, computer-assisted, relative to UCOVER Thm S(a)):** a *finite-family congruence selector* — a rule choosing, for
a fixed input family, an output length-3 family from a finite menu indexed by n modulo a fixed modulus — cannot exist
from length 4, nor from length 5, at any prime 11 ≤ ℓ ≤ 101 (Theorem 6): explicit good length-4 (and length-5) families
cover non-residue profile classes that no finite set of good length-3 families covers. CERTIFIED: length-5 good
families catch every non-residue profile class at level 1 for every prime 11 ≤ ℓ ≤ 211 (Prop 7). **Not excluded:**
transports whose output letters vary with n inside a congruence class (unbounded menus), multi-step rescaling moves,
rules using the whole input word, and the bounded-alphabet skew-product programme as a whole. Task 2 (reduce (S)
through the bridge to a new fixed-denominator estimate outside ZQ_M): through the contraction, (S)(p) reduces at primes
only to a positively weighted re-indexing of itself (Prop 8); **no new estimate was obtained** (Assessment that none is
hidden there). KT3 (EVIDENCE): the −1 fractions of L₃ and L₄ are strongly correlated across primes (ρ = +0.65, 4171
primes; +0.61 within classes mod 9240); the correlation is absent on the 7.8 % of length-4 words admitting no outgoing
rescaling move at any cut (ρ = −0.16), but present (+0.27, review) on the 30 % with no outgoing move at the interior
cuts; since almost all words admit some move, this does **not** establish that the correlation is "carried by links to
L₃". **Verdict: NARROWED** — direct contraction characterised, one class of congruence-local transports obstructed;
the sign-retaining ladder has no *demonstrated* rung down to length 3.

## 0. Mandatory falsifier table (final)

Objects: the contraction (Thm 3), the obstruction results (Props 4, 5, 8, Thm 6) and the KT3 statistics.

| screen | behaviour | where non-squareness / primality enters |
|---|---|---|
| **F1 odd squares** | Every word denominator A of n = m² is a unit mod m², so χ_{m²}(A) = +1 for every word of every length; contraction outputs are genuine words, so they are never good at squares (T1). The product formula χ(A₃) = χ(A)χ(X′Y′) needs gcd(X′Y′, n) = 1 and can fail at squares (χ_{2025}(9) = 0, review example). Profile theorems concern classes containing no squares. | Only through χ_n ≢ 1 on units; the contraction itself is an identity of integers. |
| **F2 C-even / numerator 8** | The *support* of the contraction's output is L₃(n) (Prop 4); counts are not inherited (refinement multiplicities vary). KT2 recomputes the cell census at the 26 screen primes: at the 12 R₈-zero primes in [10¹⁰, 1.1·10¹⁰]: 110–191 word pairs, 63–131 good pairs, 6–28 pairs with 4 ∣ t, **none** with 8 ∣ t; at the 14 (★)-zero primes none with 4 ∣ t (N₋ ∈ [4, 26]). R(p), R₈(p) of the screen file are reproduced (boundary words included). So admissibility of a cell set does not imply its non-emptiness at a given prime. | — |
| **F3 composites** | Lemmas 1–2, Thm 3 (identity part), Props 4, 5 hold for every odd n; the sign formulas need the stated coprimality (automatic at primes). Prop 8 is stated for primes only (its composite form is false: n = 333, review). Nothing uses primality otherwise. | coprimality in the sign formulas |
| **F4 known zeros** | (S) holds at the 14 + 12 screen primes (KT2 lists good words; Z64_SDEEPF f4_witnesses for all 64). 21841: 10 pairs, 1 good pair (64, 9, 38); 154 length-4 words (100 good), of which 14 are refinements of L₃ (4 good) and 24 admit no outgoing move (12 good). Nothing here predicts or explains its deficit. | — |

## 1. Precise statements attacked

* **Gate (brief task 1).** An exact map from a p-adaptive long-word object with controlled sign (bounded-digit HJ/CF
  word, ZQ_M witness, word of length R ≥ 4 with χ_p = −1, …) to an element of L₃(p) with χ_p = −1; or a precise
  obstruction. **Outcome:** a partial sign-corrected map (Thm 3) with characterised domain (Props 4, 5); an obstruction
  for finite-family congruence selectors (Thm 6). No good-to-good transport from any p-adaptive long-word object.
* **Caveat (brief; cf. ZAREMBA_TRANSFER / DISCOVERIES (J)95).** Fable-6's upside is λ(p) ≤ C log p; (S) is that some
  *length-3* word is good. λ(p) ≤ C log p has no known ES consequence.
* **Task 2.** Reduce (S)(p) through the bridge to one explicit fixed-denominator estimate not in ZQ_M. **Outcome:**
  only a weighted re-indexing of (S) (Prop 8); no new estimate.

## 2. Splitting, rescaling, contraction (PROVED, elementary)

**Lemma 1 (split identity; classical, formulated here).** Let n = K(b₁..b_r), A = K(b₂..b_r), 0 ≤ j ≤ r − 1,
b := b_{j+1}, X = K(b₁..b_j), X′ = K(b₁..b_{j−1}), Y = K(b_{j+2}..b_r), Y′ = K(b_{j+3}..b_r) (so j = 0 gives
X/X′ = 1/0 and j = r − 1 gives Y/Y′ = 1/0). Then
(i) n = b·X·Y − X·Y′ − X′·Y;
(ii) X·A = Y + Z·n with Z = K(b₂..b_j) (Z = 0 for j = 0); in particular X·A ≡ Y (mod n);
(iii) if gcd(X, n) = 1 then χ_n(A) = χ_n(X)·χ_n(Y);
(iv) for j ≥ 1, X/X′ = [[b_j, …, b₁]]; for j ≤ r − 2, Y/Y′ = [[b_{j+2}, …, b_r]]; conversely, for reduced fractions
X/X′, Y/Y′ with X > X′ ≥ 1, Y > Y′ ≥ 1 (or 1/0) and an integer b ≥ 2, the word (HJ(X/X′) reversed, b, HJ(Y/Y′)) has all
letters ≥ 2 and continuant bXY − XY′ − X′Y, hence is the HJ word of a fraction with that numerator.
*Proof.* With H(c) = [[c, −1],[1, 0]], H(b₁)⋯H(b_r) = [[K(b₁..b_r), −K(b₁..b_{r−1})],[K(b₂..b_r), −K(b₂..b_{r−1})]]. Put
P = H(b₁)⋯H(b_j) = [[X, −X′],[Z, −Z′]] (Z′ = K(b₂..b_{j−1}); P = I for j = 0, i.e. Z = 0, −Z′ = 1) and
Q = H(b_{j+1})⋯H(b_r), whose first column is (bY − Y′, Y) (continuant expansion along the first letter). The first
column of PQ is (n, A): n = X(bY − Y′) − X′Y, which is (i), and A = Z(bY − Y′) − Z′Y. det P = 1 gives XZ′ = X′Z − 1, so
XA = XZ(bY − Y′) − (X′Z − 1)Y = Z·n + Y, which is (ii). (iii): gcd(A, n) = 1 (adjacent continuants), so
(X/n)(A/n) = (Y/n), and (X/n) = ±1. (iv): continuants are reversal-symmetric and K(c₁..c_m)/K(c₂..c_m) = [[c₁,…,c_m]]
(DK §1); the converse is (i) read backwards with uniqueness of HJ expansions. ∎
*Credit.* (i)–(ii) are classical continuant/convergent identities (matrix form as in Z63_EUCLID Lemma E1, DK §§1–4); the
length-3 case A ≡ u·v⁻¹ is the sign dictionary of Z64_SDEEP §1. New here only the reading "(b; X/X′, Y/Y′)" and its use.

**Lemma 2 (rescaling move).** In Lemma 1 with j ≥ 1 (X′ ≥ 1), let k ≥ 2 divide b and Y′ (Y′ = 0 allowed, i.e.
j = r − 1), with b/k ≥ 2 and gcd(k, X′) = 1. Then w′ := (HJ(kX/X′) reversed, b/k, HJ(Y/(Y′/k))) — with Y/(0/k) := 1/0,
the empty tail — is a word of the same n, its denominator satisfies kX·A′ ≡ Y ≡ X·A (mod n), and hence, when
gcd(kX, n) = 1, χ_n(A′) = χ_n(A)·χ_n(k). Symmetrically on the left (k ∣ b, k ∣ X′ (X′ = 0 allowed), gcd(k, Y′) = 1,
Y′ ≥ 1).
*Proof.* (b/k)(kX)Y − (kX)(Y′/k) − X′Y = n. kX/X′ is reduced (gcd(k, X′) = 1 = gcd(X, X′)) with kX > X′ ≥ 1; Y/(Y′/k) is
reduced with Y > Y′/k ≥ 1, or is 1/0 when Y′ = 0 (then Y = 1). Apply Lemma 1(iv), then 1(ii) to w′. ∎

**Theorem 3 (contraction to length 3).** In Lemma 1 let 1 ≤ j ≤ r − 2 (so X′, Y′ ≥ 1 and X, Y ≥ 2). If X′Y′ ∣ b and
b ≥ 2X′Y′, then (t, u, v) := (b/(X′Y′), X′Y, XY′) satisfies tuv − u − v = n with t, u, v ≥ 2, i.e.
A₃ := tu − 1 ∈ L₃(n), n/A₃ = [[v, t, u]]. If gcd(XX′YY′, n) = 1 (automatic for prime n, since all these continuants
lie in [1, n)), then **χ_n(A₃) = χ_n(A)·χ_n(X′)·χ_n(Y′).**
*Proof.* tuv − u − v = bXY − X′Y − XY′ = n by Lemma 1(i). n = vA₃ − u gives vA₃ ≡ u (mod n), so
χ(A₃) = χ(u)χ(v) = χ(XY)χ(X′Y′) = χ(A)χ(X′Y′) by Lemma 1(iii). ∎
*Not good-to-good.* 137/95 = [[2,2,5,6,2]] cut at 6: (X, X′, Y, Y′) = (13, 3, 2, 1), output (t,u,v) = (2, 6, 13),
A₃ = 11; χ₁₃₇(95) = −1, χ₁₃₇(3) = −1, χ₁₃₇(11) = +1 (review). Good-to-good needs in addition χ_n(X′Y′) = +1.
*Length 4.* [[a,b,c,d]] contracts at b iff d ∣ b and b ≥ 2d (output (b/d, cd − 1, ad), sign × χ(d)), and at c iff
a ∣ c and c ≥ 2a (output (c/a, ad, ab − 1), sign × χ(a)). E.g. at p ≡ 1 (8), [[a, 2t, c, 2]] ↦ [[2a, t, 2c − 1]]
(t ≥ 2) preserves the sign.
*Check (CERTIFIED).* `scripts/z68_sign_contract.c 200000`: every length-4 word of every prime p ≡ 1 (8), p ≤ 2·10⁵, at
both interior cuts — 447 996 contractions, numerator and sign identity verified, 0 failures. (The review independently
checked 30 948 split positions incl. endpoints and 1 980 rescaling moves incl. empty tails.)

**Proposition 4 (domain of the contraction = refinements of L₃; PROVED).** For a length-3 word (t,u,v) of n and
factorisations u = X′·Y, v = X·Y′ with X > X′ ≥ 1, Y > Y′ ≥ 1, gcd(X,X′) = gcd(Y,Y′) = 1, the *refinement*
Ref := (HJ(X/X′) reversed, t·X′Y′, HJ(Y/Y′)) is a word of n to which Theorem 3 applies at the letter tX′Y′, returning
(t,u,v). Conversely every (w, j) to which Theorem 3 applies is the refinement of its output with these data. Hence
contraction is a bijection
  {(w, j) : 1 ≤ j ≤ r − 2, X′Y′ ∣ b_{j+1}, b_{j+1} ≥ 2X′Y′}  ⟷  {((t,u,v), admissible factorisations of u and v)};
the trivial factorisation (X, X′, Y, Y′) = (v, 1, u, 1) is the length-3 word itself.
*Proof.* Lemma 1(iv) with b = tX′Y′ ≥ 2: continuant tX′Y′·XY − XY′ − X′Y = tuv − u − v = n; the cut at that letter has
data (X, X′, Y, Y′) and Theorem 3 returns (t,u,v). Conversely the cut data determine the word (unique HJ expansions). ∎
*Reading (Assessment).* The map adds no length-3 word that is not already in L₃(n), and the sign it reports is that
word's own sign; the input's sign enters only through the correction χ(X′Y′). For fixed outer data, X′Y′ ∣ b is
n ≡ −(XY′ + X′Y) (mod XY·X′Y′), i.e. the W2 class n ≡ −(u+v) (mod uv) (plus the threshold t ≥ 2). Whether this
encoding (divisor-weighted refinements) could help an *analytic* existence proof is not excluded by anything proved.

**Proposition 5 (long bounded-digit words are outside the domain; PROVED).** If all HJ letters of w are ≤ M′ and
Theorem 3 applies to w at some cut, then r ≤ M′/2 + 2. If the regular continued fraction of n/A has all partial
quotients ≤ M, its HJ letters are ≤ M + 2 (so r ≤ M/2 + 3 for a contractible word), and r ≥ log n / log(M + 2) (as
n = K(w) ≤ (M + 2)^r); hence for fixed M and n > (M + 2)^{M/2+3} no such word is contractible.
*Proof.* For letters ≥ 2, K(c₁..c_L) − K(c₁..c_{L−1}) = (c_L − 2)K_{L−1} + (K_{L−1} − K_{L−2}) ≥ 1 by induction (base
K₀ − K₋₁ = 1), so K(c₁..c_L) ≥ L + 1. Hence X′ ≥ j, Y′ ≥ r − j − 1, and M′ ≥ b ≥ 2X′Y′ ≥ 2j(r − j − 1) ≥ 2(r − 2) for
1 ≤ j ≤ r − 2 (as j(r − j − 1) − (r − 2) = (j − 1)(r − j − 2) ≥ 0). Regular → HJ: [a₀; a₁, …, a_s] ↦
[[a₀ + 1, 2^{a₁−1}, a₂ + 2, 2^{a₃−1}, …]] with the terminal convention of DK §2 (R276 repair): for s > 0 even the last
letter is a_s + 1, for s odd the final block is 2^{a_s − 1}, and s = 0 gives [[a₀]] (e.g. 5/3 = [1; 1, 2] = [[2, 3]]);
in all cases HJ letters ≤ M + 2. K(w) ≤ (M+2)^r since each continuant step multiplies by at most the letter. ∎
*Not covered.* Some bounded-digit words admit single rescaling moves (Lemma 2); compositions of moves at several cuts,
and any other descent operation, are not studied here.

**Gate verdict.** The natural exact map — cut a word and absorb the second continuants into the cut letter — exists,
is characterised (Prop 4), and does not apply to long bounded-digit witnesses (Prop 5). The other candidates examined at
checkpoint 1 — Klein group (length-preserving), duality (L₃ ↔ words of digit excess 2, a relabelling), the
multiplicative reading ⟨L₃(n)⟩ ⊄ QR (a restatement), F₂-homology relations (Z63_EUCLID: generic length-3 loops free for
its specified known sets — a finite experiment, not a theorem), multiples kp ((J)95 Lemma C/D), letters equal to a least
non-residue q (B2 at level 4q) — gave nothing more (Assessment).

## 3. Finite-family congruence selectors: Theorem 6

**Families and profiles (PROVED).** By Lemma 1, fixing every letter but one (the *big* letter b) gives a *family*
F = (X/X′, Y/Y′) of length r(X/X′) + r(Y/Y′) + 1, applicable exactly to the n ≡ −(X′Y + XY′) (mod XY) with b ≥ 2. For
n ≡ 1 (8) with gcd(XY, n) = 1 its sign is χ_n(XY) = (n/(XY)_odd) (reciprocity; the 2-part of XY contributes (2/n) = 1),
a periodic function of n. For an odd prime ℓ and a non-residue g, the profile e_{ℓ,g} ∈ Ẑ (g at ℓ, 1 at every other
prime incl. 2; UCOVER) lies in the good class of F at *level 1* iff ℓ ∥ XY, X′Y + XY′ ≡ −1 (mod M := XY/ℓ) and
g ≡ −(X′Y + XY′) (mod ℓ) (all of v₂(XY) lies in M, so the 2-adic condition is included; the sign is (g/ℓ) = −1). For
length 3 the shapes (0,2), (2,0), (1,1) are exactly UCOVER's W1 and W2. Every integer n ≡ 1 (mod 8M), n ≡ g (mod ℓ),
with b ≥ 2, has the good word of F (gcd(XY, n) = 1, and (n/(XY)_odd) = (g/ℓ) = −1).

**Proposition 7 (level-1 catching by length; CERTIFIED within the stated bounds).** `scripts/z68_sign_profile.c`
(complete enumeration of all families with XY ≤ B), witnesses re-verified on integers by
`scripts/z68_sign_verify_witness.py` (`data/z68/sign/witness_verify.txt`).
* Length 3 reproduces UCOVER's level-1 sets (ℓ = 11: uncaught {2, 6}; 13: {2, 7}; 17: {3, 5, 6, 7}).
* Length 4, B = 2·10⁶: every non-residue class mod ℓ is caught for ℓ ∈ {11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 59};
  for the other primes 41 ≤ ℓ ≤ 199 some classes are not caught *within the bound* (ℓ = 41: {11, 15}; ℓ = 97: 17 of
  48; ℓ = 181: 54 of 90). ℓ = 41: event counts 256, 287, 298, 300 for B = 2·10⁵, 2·10⁶, 2·10⁷, 10⁸, same caught set;
  ℓ = 97 unchanged at 2·10⁷ (EVIDENCE only; whether unrestricted length-4 families catch these classes is unresolved).
* Length 5 (exact length): **every** non-residue class mod ℓ is caught for **every prime 11 ≤ ℓ ≤ 211** (B = 2·10⁵
  for ℓ ≤ 127, 2·10⁶ for 131 ≤ ℓ ≤ 211; 2 189 witnesses re-verified, full coverage asserted by the verifier).
  Event counts grow with B (ℓ = 41: 915, 1505, 1967; ℓ = 131: 1057, 2034, 3306 for B = 2·10⁵, 2·10⁶, 2·10⁷; from the
  shapes (1,3) and (2,2)) — EVIDENCE, three data points each. With B = 2·10⁵ only, for the 277 primes in [103, 2000]:
  exact length 5 fully catches 12 primes (pooled caught fraction 0.540), length ≤ 5 fully catches 13 (0.603) —
  consistent with a search-bound effect.
* **CONJECTURE P5.** For every prime ℓ, every non-residue class mod ℓ is caught at level 1 by a good length-5 family.

**Definition (finite-family congruence selector).** For a family F of length R, a *selector from length R to length 3
on F* consists of a modulus M_T and, for each residue c mod M_T, a length-3 family T(F, c), such that for every
sufficiently large n in F's class at which F is good, T(F, n mod M_T) applies to n and is good at n. (Equivalently,
the eventual good domain of F is covered by finitely many good length-3 families. Example of a *partial* selector: the
contraction of Thm 3 on the sub-class of F where X′Y′ ∣ b, b ≥ 2X′Y′ and χ_n(X′Y′) = +1 — a congruence condition for
fixed X′, Y′.)

**Theorem 6 (no selector from length 4 or 5 to length 3; PROVED, computer-assisted, relative to UCOVER Thm S(a)).**
For every prime 11 ≤ ℓ ≤ 101 there are a non-residue g₀ mod ℓ and an explicit good length-4 family F_ℓ (witness lines
in `data/z68/sign/profile_R4_B2e6.txt`, branch intersection by `scripts/z68_sign_transport_check.py`) such that
(a) every n ≡ 1 (mod 8M_ℓ), n ≡ g₀ (mod ℓ), n ≥ n₀(F_ℓ), has a good length-4 word (so λ(n) ≤ 4 on that class);
(b) for every q prime to ℓ, the class {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)} is not contained in a finite union of good
length-3 family classes (UCOVER Thm S(a): the branch g₀ + ℓℤ_ℓ contains a profile in U_S);
(c) hence no selector from length 4 to length 3 exists on F_ℓ. The same holds with length 5 (Prop 7 catches every
UCOVER branch at length 5).
*Proof.* (a): "Families and profiles". (b): UCOVER Thm S(a) (PROVED there, computer-assisted, for ℓ ∈ {11, 13} ∪
[17, 101]); the check script intersects its certified branch lists with the length-4 level-1 catches — non-empty at all
22 primes (ℓ = 11: both branches 2, 6; ℓ = 41: 12 of 14) — asserts the full prime range, and re-verifies each witness
on integers. (c): let T be a selector on F_ℓ with modulus M_T, and put q := lcm(8M_ℓ, M_T′, Q), where M_T′ is the
prime-to-ℓ part of M_T and Q is a product of primes ≠ ℓ large enough that every positive n ≡ 1 (mod Q) other than 1
exceeds the thresholds of F_ℓ and of the finitely many T(F_ℓ, c) (n = 1 is not ≡ g₀ (mod ℓ)). On
K := {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)} every n has F_ℓ's good word (a), n mod M_T takes finitely many values c₁,…,c_m, and
so every n ∈ K lies in the union of the good congruence classes of T(F_ℓ, c₁), …, T(F_ℓ, c_m) (each a finite union of
congruence classes, SDEEPF/UCOVER). Thus K is finitely coverable by good length-3 families, contradicting (b) since
q is prime to ℓ. ∎
*Remark (all ℓ ≥ 11, weaker length).* For every prime ℓ ≥ 11, ELL0 (S-all) gives a non-residue class g₀ mod ℓ that is
not finitely coverable at length 3 for any q ⊥ ℓ, while the single family with tail ℓ/(ℓ − g₀) is good on all of
{n ≡ 1 (mod 8), n ≡ g₀ (mod ℓ)} ((ℓ/n) = (n/ℓ) = (g₀/ℓ) = −1). So no selector from length 1 + r(ℓ/(ℓ − g₀)) (≤ ℓ) to
length 3 exists on that family.
*Reading (Assessment).* On non-square classes, long-word sign existence is decided by finitely many families already at
length 5 (for ℓ ≤ 211), while at length 3 it provably is not; any transport down to length 3 on such a class must make
its output's fixed letters depend on more than a fixed residue of n. Not excluded: outputs with letters varying with n
inside a congruence class, unbounded sequences of congruence refinements, multi-step moves, rules reading the whole
input word, and finite-state algorithms with unbounded output menus.

## 4. Kill tests (registered at checkpoint 1) — outcomes

* **KT1 (sharp form "R₀ = 4") — the registered B-bounded version FIRED** (length 4 with XY ≤ 2·10⁶ misses classes at
  ℓ = 41 and most primes in [41, 199]); the unrestricted statement is unresolved. Registered fallback: R₀(ℓ) ≤ 5 for
  every prime 11 ≤ ℓ ≤ 211 (CERTIFIED); R₀(ℓ) = 4 for ℓ ≤ 37 and ℓ ∈ {43, 47, 59} (length-4 cover found, and length 3
  fails by UCOVER). Theorem 6 uses length 4 only on the UCOVER branches, where it suffices at all 22 primes.
* **KT2 (cell census) — did not fire.** (`scripts/z68_sign_cells.c`, `data/z68/sign/kt2_cells.txt`, 2.4 s.) Numbers in
  the F2 row. **Consequence (CERTIFIED + reading):** "every admissible 2-adic cell class of L₃(p) is non-empty" is false
  at certified primes > 10¹⁰; a transport whose image is confined to the slices {4 ∣ t} or {8 ∣ t} cannot be universal,
  and admissibility of a cell set alone does not ensure its non-emptiness. (This does not show that a successful
  transport must use the full Jacobi cell union.)
* **KT3 (information) — "examine" branch triggered; partially resolved; the first resolution was withdrawn after
  review.** Populations: (A) `z68_sign_kt3.py` — 4171 primes p ≡ 1 (8) in (10⁴, 2·10⁵] with |L₃|, |L₄|, |L₅| ≥ 10:
  ρ(f₃, f₄) = +0.646, ρ(f₃, f₅) = −0.279 (f_r = −1 fraction of L_r); within the 480 classes mod 9240: +0.613; within
  the 256 classes of ((q/p))_{q ≤ 23}: +0.561; after regressing out log q/q-weighted sums of (q/p) over the prime bands
  3–23, 29–179, 181–877, 881–2999 and Σ_{m < ⌊√p⌋}(m/p) (as coded): +0.522. These controls show the correlation is not
  explained by the listed finite congruence data. (B) `z68_sign_kt3b.py` (4167 primes, extra size cuts): refinements
  (31 % of L₄): ρ = +0.744; non-refinements: +0.405. (C) **Withdrawn:** the first draft's "unlinked" set (gcd(b,d) =
  gcd(a,c) = 1, 16 % of L₄, ρ = −0.093) is not the no-move set — Lemma 2 also needs b/k ≥ 2; the true no-outgoing-move
  set at the *interior* cuts (30 % of L₄) has ρ = +0.271 (+0.353 within mod 9240; review). (D) `z68_sign_moves.c` +
  `z68_sign_kt3c.py` (3895 primes with ≥ 10 such words): words with **no outgoing move at any cut incl. endpoints**
  (7.8 % of L₄): ρ = −0.158 (−0.075 within mod 9240); at the hardest 1 % of primes by f₃ their −1 fraction is 0.563 vs
  0.558 overall; words with no move in or out at any cut are only 0.37 % of L₄. **Reading (EVIDENCE):** the
  cross-length correlation is real and not explained by the listed congruence controls; it disappears on the small set
  of words with no outgoing move at any cut, but since almost every word admits a move, and reachability to L₃ through
  multi-step moves was not computed, this does **not** show that the correlation is carried by links to L₃. Open.
* **KT4 (brief).** (a) Squares: nothing is produced (F1). (b) 21841: consistent (F4 row). (c) No finite covering of a
  square class is claimed: the finite coverings here (Thm 6(a), Prop 7) are of classes with a non-residue at ℓ and
  concern λ ≤ 4 or 5, not (S).

## 5. Task 2: what the bridge reduces (S) to

**Proposition 8 (PROVED, primes only).** For a prime p ≡ 1 (4) and every positive weight μ on contractible pairs (w, j),
  Σ_{(w,j) contractible} μ(w, j)·[χ_p(A_w)·χ_p(X′Y′) = −1] = Σ_{(t,u,v) good} Σ_{admissible factorisations} μ,
so the left side is > 0 iff (S)(p). *Proof.* Prop 4's bijection and Theorem 3's sign rule (coprimality is automatic at
primes). ∎ (For composite n the identity is false: n = 333, μ ≡ 1 gives 32 vs 34, because χ_n(X′Y′) can vanish; review.)
*Answer to task 2 (Assessment).* No fixed-denominator estimate outside ZQ_M was obtained through the bridge: through the
contraction, (S)(p) re-indexes as a divisor-weighted count over L₃(p). By Prop 5, statements about long bounded-digit
words (ZQ_M, Zaremba(M), the fable-6 skew product) are not statements about contractible words. Weighting does not
change the fixed-length scale problem (|L_r(n)| ≍ (log n)^{r−1} on average, so the B3 error-term constraint of FRONTIER
§3 / Z64_SDEEP Prop 4 applies to each fixed-length encoding); whether some weighted or multi-length encoding escapes it
is not excluded.

## 6. Verdict, screens, proposed FRONTIER text

**NARROWED.** No HOT LEAD. ES and (S) remain open.
* **PROVED:** Lemma 2 (rescaling moves), Theorem 3 (contraction, sign rule), Prop 4 (domain = refinements, bijection),
  Prop 5 (long bounded-digit words not contractible), Prop 8 (primes); Lemma 1 is classical (formulation here).
  **PROVED, computer-assisted (relative to UCOVER Thm S(a)):** Theorem 6. **CERTIFIED:** Prop 7 (length-5 level-1
  catching for 11 ≤ ℓ ≤ 211; length-4 catching lists within XY ≤ 2·10⁶), KT2 census, 447 996 contractions.
  **EVIDENCE:** KT3. **CONJECTURE:** P5. Novelty: `git grep` finds no prior statement of the rescaling/contraction
  package or of length-4/5 profile catching; the machinery is classical, the finite-cover obstruction is UCOVER/ELL0's.
* **Four FRONTIER §4 screens** (for the contraction): T1 squares — PASS (outputs are words; never good at squares).
  8/131 — the output's support is L₃; cell-restricted statements fail at certified primes (KT2). Tied modulus — does not
  escape: X′Y′ ∣ b is the W2 class n ≡ −(u+v) (mod uv). Fixed p — no averaging; re-indexes L₃(p).
* **Fable-6 after this lane (Assessment).** No direct contraction reaches length 3 from its long bounded-digit
  witnesses (Prop 5), and finite-family congruence selectors fail already from length 4/5 (Thm 6). Other descent
  mechanisms (multi-step moves, n-dependent outputs, the skew product itself) are not excluded.

**Proposed FRONTIER §7 / z68 text (do NOT edit FRONTIER here):** *SIGN (`Z68_SIGN.md`):* Every HJ word of n cut at a
letter b reads n = bXY − XY′ − X′Y with χ_n(A) = χ_n(XY) (classical). PROVED: at an interior cut with X′Y′ ∣ b,
b ≥ 2X′Y′, (b/X′Y′, X′Y, XY′) ∈ L₃(n) and χ_n(A₃) = χ_n(A)χ_n(X′Y′) (partial, sign-corrected contraction; not
good-to-good); its domain is exactly the refinements of length-3 words (factorisations of the outer letters), and no
word with HJ letters ≤ M′ and length > M′/2 + 2 is in it (so long ZQ_M / Zaremba witnesses are not directly
contractible). PROVED (computer-assisted, rel. UCOVER Thm S(a)): at every prime 11 ≤ ℓ ≤ 101 there is no
finite-family congruence selector from good length-4 (or length-5) words to good length-3 words; CERTIFIED: good
length-5 families catch every non-residue profile class at level 1 for 11 ≤ ℓ ≤ 211. EVIDENCE: the −1 fractions of L₃
and L₄ correlate across primes (ρ ≈ +0.65; +0.61 within classes mod 9240), mechanism open. Open: a transport with
n-dependent outputs or multi-step moves.

## 7. Reproduction (all commands under `ulimit -v 6000000`, `timeout ≤ 1800`)
```
gcc -O2 -o prof scripts/z68_sign_profile.c
./prof 11 199 4 2000000 > data/z68/sign/profile_R4_B2e6.txt                                   # 20 s
./prof 11 101 5 200000 > data/z68/sign/profile_R5_B2e5.txt
./prof 103 127 5 200000 > data/z68/sign/profile_R5_B2e5_103_127.txt
./prof 131 211 5 2000000 > data/z68/sign/profile_R5_B2e6_131_211.txt                           # 46 s
./prof 103 2000 5 200000 | grep -v '^W' > data/z68/sign/profile_R5_B2e5_103_2000.txt           # 48 s
./prof 41 41 4 100000000 ; ./prof 131 131 5 20000000                                           # event-count growth runs
uv run --with sympy python scripts/z68_sign_verify_witness.py data/z68/sign/profile_R4_B2e6.txt 4
uv run --with sympy python scripts/z68_sign_verify_witness.py data/z68/sign/profile_R5_B2e5.txt 5 full 11 101   # etc.
uv run --with sympy python scripts/z68_sign_transport_check.py                                 # Theorem 6 input
gcc -O2 -o cells scripts/z68_sign_cells.c
(grep -v '^#' data/z58/screens/star_prime_zeros.txt; grep -v '^#' data/z58/screens/r8_zeros_1e10.txt) | awk '{print $1}' | ./cells > data/z68/sign/kt2_cells.txt
gcc -O2 -o len scripts/z68_sign_lengths.c && ./len 200000 > data/z68/sign/kt3_lengths_2e5.txt
uv run --with numpy --with scipy --with sympy python scripts/z68_sign_kt3.py > data/z68/sign/kt3_report.txt
gcc -O2 -o con scripts/z68_sign_contract.c && ./con 200000 > data/z68/sign/kt3_contract_2e5.txt
uv run --with numpy --with scipy python scripts/z68_sign_kt3b.py > data/z68/sign/kt3b_report.txt
gcc -O2 -o mov scripts/z68_sign_moves.c && ./mov 200000 > data/z68/sign/kt3_moves_2e5.txt
uv run --with numpy --with scipy python scripts/z68_sign_kt3c.py > data/z68/sign/kt3c_report.txt
```

## 8. Internal hostile review and fixes
Deep-mode review of commits 0e96b6f17..851763a13 (reviewer model gpt-6-astra via the review tool; report kept at
`/tmp/z68_sign_review.md`, not committed). Verdict "reject as written; core mathematics repairable". It reproduced every
data file (profiles, 447 996 contractions, 2 189 length-5 witnesses, KT2 at all 26 primes, KT3 reports, UCOVER
sanity sets, all 22 branch intersections) and checked 30 948 splits and 1 980 moves independently. Findings and fixes:
* **FATAL F1 (KT3 "unlinked")**: gcd-one ≠ no-move (Lemma 2 needs b/k ≥ 2); corrected interior no-move set gives
  ρ = +0.27. *Fix:* claim withdrawn; KT3 recomputed with exact move predicates at all cuts (`z68_sign_moves.c`); the
  reading is now "correlation real, mechanism open" (§4 KT3).
* **M1** contraction is not good-to-good (p = 137 example): stated as a partial sign-corrected map; thresholds
  b ≥ 2X′Y′ / b ≥ 2d / c ≥ 2a restored in every summary; the "local transport" example made partial with χ(X′Y′) = +1.
* **M2** Prop 8 false for composites (n = 333: 32 vs 34): restricted to primes; F1/F3 rows rewritten via coprimality of
  actual denominators (χ_{2025}(9) = 0 example).
* **M3** overclaims ("transports nothing", "vacuous", "must be archimedean", "no rung"): replaced by the proved scope
  plus Assessments, with the escape hatches listed (bottom line, §3 reading, §5, §6); title changed.
* **M4** KT2 "must use the full cell union" inference removed.
* **M5** Theorem 6(c) proof rewritten (finite output menu; enlarge q to clear thresholds; good congruence classes);
  all-ℓ remark restricted to n ≡ 1 (mod 8).
* **M6** KT1 and length-4 statements now say "within XY ≤ 2·10⁶"; unrestricted R₀ = 4 unresolved.
* **Minors:** finite CF→HJ terminal convention and the growth bound r ≥ log n/log(M+2) added (Prop 5); Lemma 2 endpoint
  (Y′ = 0) handled; cumulative vs exact length-5 statistics both reported (12 vs 13 primes; 0.540 vs 0.603); KT3
  populations (4171 vs 4167) and the actual prime bands stated; "each single move is possible" corrected; Lemma 1
  credited as classical; argc/range checks added to `z68_sign_profile.c`, `_contract.c`, `_lengths.c`, a domain check
  to `_cells.c`; the transport script now asserts the prime range and names Theorem 6; the witness verifier can assert
  full coverage (used for all length-5 files); reproduction commands made executable.
