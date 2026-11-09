# Z68_SIGN — transporting long-word sign information to length-3 words: an exact bridge exists (contraction), but it is a re-parametrisation of L₃; bounded-digit words lie outside it, and no congruence-local transport from length 4 or 5 exists. Verdict: NARROWED; HOT LEAD: no

**ES is OPEN; nothing here proves or disproves ES, (S), SQ₅ or (MS).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief: `z52bbriefs/z68_lanes.md` §SIGN
(+ `z53_depth.md`, `z58_lanes.md` common rules / falsifier table). Scripts `scripts/z68_sign_*`, data `data/z68/sign/`.
Checkpoint 1 (falsifier table, gate log, kill tests KT1–KT4 registered before any computation): commit 0e96b6f17.

Notation (DEDEKIND_ES = DK, Z64_SDEEP, Z64_SDEEPF, Z66_UCOVER = UCOVER, Z67_ELL0 = ELL0). HJ word
n/A = [[b₁,…,b_r]], b_i ≥ 2, r = r(n/A); continuant K(b₁..b_r) = n, A = K(b₂..b_r), K(∅) = 1, and K of "length −1" is
0; L_r(n) = {A : r(n/A) = r}; length-3 words n/A = [[v,t,u]] ⟺ tuv − u − v = n, A = tu − 1 (DK Lemma 1.1);
χ_n(A) = (A/n) (Jacobi). λ(n) = min{r(n/A) : χ_n(A) = −1} (DK Cor 4.6). (S)(n): some A ∈ L₃(n) has χ_n(A) = −1;
at primes p ≡ 1 (4), p > 5, (S)(p) ⟹ ES(p) (DK Thm 4.5). A word is *good* if χ_n(A) = −1.

## Bottom line (one paragraph)

The brief's gate asked for an exact map from a p-adaptive long-word object with controlled sign to a good length-3
word. **One exists, and it is canonical** (Theorem 3, PROVED): every word of n, cut at any interior letter b, is a
"length-3 word with fractional outer letters", n = b·X·Y − X·Y′ − X′·Y (Lemma 1); whenever X′Y′ ∣ b the triple
(b/X′Y′, X′Y, XY′) is a length-3 word of n, and χ_n(A₃) = χ_n(A)·χ_n(X′Y′). **But it transports nothing:** its domain
is exactly the set of *refinements* of length-3 words (factorisations of the outer letters u = X′Y, v = XY′;
Prop 4), so any sign it delivers is the sign of a length-3 word already present; the input's own sign is irrelevant
(it is multiplied by χ_n(X′Y′)); its hypothesis X′Y′ ∣ b is the W2 class n ≡ −(u+v) (mod uv), i.e. (S)'s own tied
divisor event; and **no word with bounded digits of length > M/2 + 3 is in its domain** (Prop 5), so Zaremba/ZQ_M-type
witnesses — fable-6's objects — can never be contracted. Beyond the refinement domain, transports that are
*congruence-local* (output's fixed letters determined by the input's fixed letters and n modulo a fixed modulus) are
impossible already from length 4 (and 5) at every prime 11 ≤ ℓ ≤ 101 (Theorem 6, PROVED computer-assisted relative to
UCOVER Thm S(a)): length-5 good families catch *every* non-residue profile class at ℓ (CERTIFIED for 11 ≤ ℓ ≤ 211;
length 4 does not for ℓ ≥ 41 within the searched range), while length-3 good families provably cannot cover some of them.
Empirically (KT3, EVIDENCE), the strong cross-length correlation of sign statistics (ρ = +0.65 between the −1
fractions of L₃ and L₄ over 4171 primes; +0.61 within classes mod 9240) is carried entirely by words linked to L₃ by
the exact rescaling moves of Lemma 2: length-4 words with no rescaling move have ρ = −0.09, and at the hardest primes
(incl. 21841) their −1 fraction is normal. Task 2 of the brief (reduce (S) through the bridge to a new fixed-denominator
twisted estimate not in ZQ_M) is therefore vacuous: through the contraction, (S) reduces only to a positively weighted
form of itself (Prop 8). **Verdict: NARROWED** — the sign-retaining Zaremba ladder (fable-6) has no exact rung down to
length 3; what is missing is an *archimedean* (non-congruence, non-refinement) transport, i.e. B2.

## 0. Mandatory falsifier table (final)

The lane's objects: the contraction bridge (Thm 3), the obstruction theorems (Props 5, 8, Thm 6) and the KT3 statistics.

| screen | behaviour | where non-squareness / primality enters |
|---|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1, so every word of every length, its refinements and contractions, have sign +1; the contraction produces nothing at squares (both factors of χ(A₃) = χ(A)χ(X′Y′) are +1). The profile theorems concern non-residue profiles (no squares in their classes). | Only through χ_n ≢ 1; the bridge itself is sign-blind (it is an identity of integers). |
| **F2 C-even / numerator 8** | The contraction is a bijection between refinements and length-3 words (Prop 4), so it inherits exactly the cell distribution of L₃(n); cell-restricted versions are false: KT2 recomputes that at the 12 certified R₈-zero primes in [10¹⁰, 1.1·10¹⁰] there are 110–191 word pairs, 63–131 good pairs, 6–28 pairs with 4 ∣ t, and **none** with 8 ∣ t; at the 14 (★)-zero primes none with 4 ∣ t (N₋ ≥ 4). Independently reproduces R(p) and R₈(p) of the screen file at all 12 primes (counting boundary words). | — |
| **F3 composites** | Lemmas 1–2, Thm 3, Props 4, 5, 8 hold for every n ≥ 3 (the sign formulas need the stated coprimality, automatic at primes). Nothing uses primality. | not needed |
| **F4 known zeros** | (S) holds at all 14 + 12 screen primes (KT2 lists good words; Z64_SDEEPF f4_witnesses for all 64). 21841: 10 pairs, 1 good pair (t,u,v) = (64, 9, 38); its length-4 words: 154, of which 100 good; refinements of L₃: 14 (4 good); unlinked words: 50 (36 good, 0.72 — normal). Nothing here "explains" 21841 or proves positivity there. | — |

## 1. Precise statements attacked

* **Gate (brief task 1).** Find an exact map from a p-adaptive long-word object with controlled sign (bounded-digit
  HJ/CF word, a ZQ_M witness, any word of length R ≥ 4 with χ_p = −1, …) to an element of L₃(p) with χ_p = −1, or prove
  a precise obstruction. **Outcome: a canonical exact map exists (§2), and three precise obstructions describe its
  scope (Props 4, 5, Thm 6).**
* **Caveat (brief).** Fable-6's upside is λ(p) ≤ C log p. (S) is the statement that some *length-3* word is good. λ(p) ≤
  C log p has no known ES consequence; the bridge is the whole question.
* **Task 2.** Reduce (S)(p) through the bridge to one explicit fixed-denominator estimate not in ZQ_M. **Outcome:
  vacuous (Prop 8).**

## 2. The bridge: splitting, rescaling, contraction (all PROVED, elementary)

**Lemma 1 (split identity).** Let n = K(b₁..b_r), A = K(b₂..b_r), 0 ≤ j ≤ r − 1, b := b_{j+1}, and
X = K(b₁..b_j), X′ = K(b₁..b_{j−1}), Y = K(b_{j+2}..b_r), Y′ = K(b_{j+3}..b_r) (so j = 0 gives X/X′ = 1/0 and j = r − 1
gives Y/Y′ = 1/0). Then
(i) n = b·X·Y − X·Y′ − X′·Y;
(ii) X·A = Y + Z·n with Z = K(b₂..b_j) (Z = 0 for j = 0); in particular X·A ≡ Y (mod n);
(iii) if gcd(X, n) = 1, then χ_n(A) = χ_n(X)·χ_n(Y);
(iv) for j ≥ 1, X/X′ = [[b_j, …, b₁]]; for j ≤ r − 2, Y/Y′ = [[b_{j+2}, …, b_r]]; conversely, for any reduced fractions
X/X′, Y/Y′ with X > X′ ≥ 1, Y > Y′ ≥ 1 (or 1/0) and any integer b ≥ 2, the concatenated word
(HJ(X/X′) reversed, b, HJ(Y/Y′)) has continuant bXY − XY′ − X′Y and all letters ≥ 2, hence is the HJ word of a
fraction with that numerator.
*Proof.* With H(c) = [[c, −1],[1, 0]], H(b₁)⋯H(b_r) = [[K(b₁..b_r), −K(b₁..b_{r−1})],[K(b₂..b_r), −K(b₂..b_{r−1})]]. Put
P = H(b₁)⋯H(b_j) = [[X, −X′],[Z, −Z′]] (Z′ = K(b₂..b_{j−1}); P = I for j = 0) and Q = H(b_{j+1})⋯H(b_r), whose first
column is (K(b_{j+1}..b_r), Y) = (bY − Y′, Y) (expansion of the continuant along its first letter). The first column of
PQ is (n, A): n = X(bY − Y′) − X′Y, which is (i); A = Z(bY − Y′) − Z′Y. det P = 1 gives XZ′ = X′Z − 1, so
XA = XZ(bY − Y′) − (X′Z − 1)Y = Z·n + Y, which is (ii). (iii): gcd(A, n) = 1 (A is a continuant adjacent to n), so
(X/n)(A/n) = (Y/n) by (ii) and multiplicativity of the Jacobi symbol in its numerator, and (X/n) = ±1. (iv): continuants
are symmetric under reversal, and K(c₁..c_m)/K(c₂..c_m) = [[c₁,…,c_m]] for letters ≥ 2 (DK §1); the converse is (i) read
backwards plus uniqueness of HJ expansions. ∎
*Credit.* (i)–(ii) are the classical splitting and convergent identities for continuants; the reading "every word is a
length-3 word (b; X/X′, Y/Y′) with fractional outer letters, and χ_n(A) = χ_n(XY)" generalises the length-3 sign
dictionary A ≡ u·v⁻¹ (Z64_SDEEP §1). For j = 0 it is the tail form χ_n(A) = χ_n(Y) = ((−A₂)/A)-type reciprocity.

**Lemma 2 (rescaling move).** In Lemma 1 with j ≥ 1, let k ≥ 2 divide both b and Y′, with b/k ≥ 2 and gcd(k, X′) = 1.
Then w′ := (HJ(kX/X′) reversed, b/k, HJ(Y/(Y′/k))) is a word of the same n, with denominator A′ satisfying
kX·A′ ≡ Y ≡ X·A (mod n); hence, when gcd(kX, n) = 1, χ_n(A′) = χ_n(A)·χ_n(k). (Symmetrically on the left: k ∣ b, k ∣ X′,
gcd(k, Y′) = 1, j ≤ r − 2.)
*Proof.* (b/k)(kX)Y − (kX)(Y′/k) − X′Y = bXY − XY′ − X′Y = n; kX/X′ and Y/(Y′/k) are reduced fractions with numerator >
denominator ≥ 1 (Y′/k ≥ 1 since k ∣ Y′ ≠ 0); apply Lemma 1(iv) and then 1(ii) to w′. ∎

**Theorem 3 (contraction to length 3).** In Lemma 1 let 1 ≤ j ≤ r − 2 (so X′, Y′ ≥ 1 and X, Y ≥ 2). If X′Y′ ∣ b and
b ≥ 2X′Y′, then
  (t, u, v) := (b/(X′Y′), X′Y, XY′)
satisfies tuv − u − v = n with t, u, v ≥ 2, i.e. A₃ := tu − 1 ∈ L₃(n), n/A₃ = [[v, t, u]]. If gcd(XX′YY′, n) = 1
(automatic for prime n: all these continuants lie in [1, n)), then
  **χ_n(A₃) = χ_n(A)·χ_n(X′)·χ_n(Y′).**
*Proof.* tuv − u − v = (b/X′Y′)·X′Y·XY′ − X′Y − XY′ = bXY − X′Y − XY′ = n by Lemma 1(i). Then n = vA₃ − u gives
v·A₃ ≡ u (mod n), so χ(A₃) = χ(u)χ(v) = χ(X′Y·XY′) = χ(XY)·χ(X′Y′) = χ(A)·χ(X′Y′) by Lemma 1(iii). ∎
*Check (CERTIFIED).* `scripts/z68_sign_contract.c 200000`: every length-4 word of every prime p ≡ 1 (8), p ≤ 2·10⁵,
at both interior positions — 447 996 contractions, numerator and sign identity verified, 0 failures.
For length 4, [[a,b,c,d]] contracts at b iff d ∣ b (giving (b/d, cd − 1, ad), sign × χ(d)) and at c iff a ∣ c (giving
(c/a, ad, ab − 1), sign × χ(a)). E.g. at p ≡ 1 (8), [[a, 2t, c, 2]] ↦ [[2a, t, 2c − 1]] preserves the sign.

**Proposition 4 (the domain of the contraction is the set of refinements of L₃; the bridge is a re-parametrisation).**
For a length-3 word (t,u,v) of n and any factorisations u = X′·Y, v = X·Y′ into positive integers with X > X′ ≥ 1,
Y > Y′ ≥ 1, gcd(X,X′) = gcd(Y,Y′) = 1, the *refinement* Ref := (HJ(X/X′) reversed, t·X′Y′, HJ(Y/Y′)) is a word of n;
Theorem 3 applies to it at the letter tX′Y′ and returns (t,u,v). Conversely, every (w, j) to which Theorem 3 applies
is the refinement of its output with the factorisation (X′·Y, X·Y′). Hence contraction is a bijection
  {(w, j) : 1 ≤ j ≤ r − 2, X′Y′ ∣ b_{j+1}, b_{j+1} ≥ 2X′Y′}  ⟷  {((t,u,v), admissible factorisations of u and v)},
the trivial factorisation (X, X′, Y, Y′) = (v, 1, u, 1) being the length-3 word itself.
*Proof.* Lemma 1(iv) with b = tX′Y′: the continuant is tX′Y′·XY − XY′ − X′Y = tuv − v − u = n; Lemma 1(iv) also shows that
the cut of Ref at the letter tX′Y′ has data (X, X′, Y, Y′); Theorem 3 returns (tX′Y′/X′Y′, X′Y, XY′) = (t,u,v). The
converse is Theorem 3 plus Lemma 1(iv) (the word is determined by its cut data). ∎
*Reading.* Every sign the contraction can deliver is χ_n of a length-3 word of n that exists independently of the input;
the input's sign enters only multiplied by χ_n(X′Y′), which is determined by the factorisation. The existence condition
X′Y′ ∣ b says, for fixed outer data, n ≡ −(XY′ + X′Y) (mod XY·X′Y′), i.e. n ≡ −(u + v) (mod uv): the W2 (fixed (u,v))
class of SDEEPF/UCOVER — (S)'s own tied divisor event. **So the bridge exists, but it is a change of coordinates on L₃(n)
(Assessment, from the PROVED bijection).**

**Proposition 5 (bounded-digit words are outside the domain).** If all letters of w are ≤ M′ and Theorem 3 applies to w
at some position, then r ≤ M′/2 + 2. In particular, a word whose regular continued fraction has all partial quotients
≤ M (HJ letters ≤ M + 2) and length r > M/2 + 3 — e.g. every ZQ_M / Zaremba(M) witness for p large, whose length is
≫ log p — is never contractible.
*Proof.* For letters ≥ 2, K(c₁..c_L) − K(c₁..c_{L−1}) ≥ 1 by induction (K_L − K_{L−1} = (c_L − 2)K_{L−1} + (K_{L−1} − K_{L−2})
≥ K_{L−1} − K_{L−2}, base K₀ − K₋₁ = 1), so K(c₁..c_L) ≥ L + 1. Hence X′ ≥ j, Y′ ≥ r − j − 1, and
M′ ≥ b ≥ 2X′Y′ ≥ 2j(r − j − 1) ≥ 2(r − 2) for 1 ≤ j ≤ r − 2 (as j(r − j − 1) − (r − 2) = (j − 1)(r − j − 2) ≥ 0). The
regular-to-HJ dictionary [a₀; a₁, a₂, …] ↦ [[a₀ + 1, 2^{a₁−1}, a₂ + 2, 2^{a₃−1}, …]] gives HJ letters ≤ M + 2. ∎
(With letters ≥ 3 the continuants grow exponentially and the bound is far smaller.) *Not covered:* compositions of
rescaling moves at several positions (Lemma 2) applied to bounded-digit words; each single move is possible, a
full contraction is not (Assessment: untested).

**Gate verdict.** An exact bridge exists and is the natural one (cut a word, absorb the second continuants into the
cut letter). It is tautological (Prop 4) and excludes fable-6's bounded-digit witnesses (Prop 5). Other candidates
examined at checkpoint 1 — Klein group (length-preserving), duality (L₃ ↔ words of digit excess 2, a relabelling),
the multiplicative reading ⟨L₃(n)⟩ ⊄ QR (a restatement), F₂-homology relations (Z63_EUCLID: generic length-3 loops
are free), multiples kp ((J)95 Lemma C/D), letters equal to a least non-residue q (B2 at level 4q) — give nothing more.

## 3. Beyond the refinement domain: no congruence-local transport (Theorem 6)

**Families and profiles.** By Lemma 1, fixing every letter but one (the *big* letter b) gives a *family*
F = (X/X′, Y/Y′) of length r(X/X′) + r(Y/Y′) + 1, applicable exactly to the n ≡ −(X′Y + XY′) (mod XY) with b ≥ 2; for odd
n ≡ 1 (8) and gcd(XY, n) = 1 its sign is χ_n(XY) = (n/(XY)_odd), a periodic function of n. For a prime ℓ and a
non-residue g, the profile e_{ℓ,g} ∈ Ẑ (g at ℓ, 1 at every other prime, UCOVER) lies in a good family class at *level 1*
iff ℓ ∥ XY, X′Y + XY′ ≡ −1 (mod M := XY/ℓ) and g ≡ −(X′Y + XY′) (mod ℓ); goodness is then automatic
(χ = (g/ℓ) = −1). For length 3 the shapes (0,2), (2,0), (1,1) are exactly UCOVER's W1 and W2.
Then every integer n ≡ 1 (mod 8M), n ≡ g (mod ℓ), large, has the good word of F (gcd(XY, n) = 1 and
(n/(XY)_odd) = (g/ℓ)·∏_{q | M}(1/q) = −1).

**Proposition 7 (level-1 catching by length; CERTIFIED, `scripts/z68_sign_profile.c`, verified independently by
`scripts/z68_sign_verify_witness.py`, data `data/z68/sign/profile_*.txt`, `witness_verify.txt`).**
* Length 3 reproduces UCOVER exactly (ℓ = 11: uncaught {2, 6}; 13: {2, 7}; 17: {3, 5, 6, 7}).
* Length 4 (all families with XY ≤ 2·10⁶): catches every non-residue class mod ℓ for ℓ ∈ {11, 13, 17, 19, 23, 29, 31,
  37, 43, 47, 59}; for the other primes 41 ≤ ℓ ≤ 199 it misses some (ℓ = 41: {11, 15}; ℓ = 97: 17 of 48; ℓ = 181: 54 of
  90). At ℓ = 41 the event count converges (256, 287, 298, 300 events for XY ≤ 2·10⁵, 2·10⁶, 2·10⁷, 10⁸) with the same
  caught set; at ℓ = 97 unchanged at 2·10⁷ (EVIDENCE that length-4 level-1 events are finite; no proof).
* Length 5: catches **every** non-residue class mod ℓ for **every prime 11 ≤ ℓ ≤ 211** (XY ≤ 2·10⁵ for ℓ ≤ 127,
  ≤ 2·10⁶ for 131 ≤ ℓ ≤ 211; 2 189 witnesses re-verified on integers). Length-5 event counts keep growing with the
  bound (ℓ = 41: 915, 1505, 1967; ℓ = 131: 1057, 2034, 3306 for XY ≤ 2·10⁵, 2·10⁶, 2·10⁷), the growth coming from the
  shapes (1,3) and (2,2) at a roughly constant rate per decade of XY (EVIDENCE for infinitely many level-1 events).
  With XY ≤ 2·10⁵ only, 13 of the 277 primes in [103, 2000] are fully caught (caught fraction 0.60), consistent with a
  search-bound effect.
* **CONJECTURE P5.** For every prime ℓ every non-residue class mod ℓ is caught at level 1 by a length-5 good family.

**Definition (local transport).** A *local transport from length R to length 3 on a family F* (length R) is a rule
assigning to F and to each residue c of n modulo a fixed modulus M_F a length-3 family T(F, c) such that for every
sufficiently large n in F's class at which F is good, T(F, n mod M_F) applies to n and is good at n. (The contraction
is a local transport on the sub-class of F where X′Y′ ∣ b, with M_F = X′Y′·XY.)

**Theorem 6 (no local transport from length 4 or 5 to length 3; PROVED, computer-assisted relative to UCOVER
Thm S(a)).** For every prime 11 ≤ ℓ ≤ 101 there are a non-residue g₀ mod ℓ and an explicit good length-4 family F_ℓ
(listed by `scripts/z68_sign_transport_check.py`) such that
(a) every n ≡ 1 (mod 8M_ℓ), n ≡ g₀ (mod ℓ), n ≥ n₀(F_ℓ), has a good length-4 word, so λ(n) ≤ 4 on that class;
(b) for every q prime to ℓ, the class {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)} is not contained in a finite union of good
length-3 family classes (UCOVER Thm S(a): the branch g₀ + ℓℤ_ℓ contains a profile in U_S);
(c) hence there is no local transport from length 4 to length 3 on F_ℓ. The same holds with length 5 in place of 4
(Prop 7 catches every UCOVER branch at length 5).
*Proof.* (a): the paragraph "Families and profiles". (b): UCOVER Thm S(a) (PROVED there, computer-assisted, for
ℓ ∈ {11, 13} ∪ [17, 101]); `z68_sign_transport_check.py` intersects its certified branch lists with the length-4
level-1 catches — non-empty at all 22 primes (e.g. ℓ = 11: both branches 2, 6; ℓ = 41: 12 of 14 branches) — and
re-verifies each witness on integers. (c): let T be a local transport on F_ℓ and put q := lcm(8M_ℓ, M_F′), M_F′ the
prime-to-ℓ part of M_{F_ℓ}. The class K = {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)} is contained in F_ℓ's good class (a), and on
K the residue n mod M_{F_ℓ} takes finitely many values c; so all large n ∈ K are covered by the finitely many good
length-3 families T(F_ℓ, c). Finitely many n are covered by single SDEEPF words up to … — more simply, enlarging q by a
factor coprime to ℓ removes any finite set of small n from K's closure-relevant part; since covering is decided on the
profinite closure (UCOVER §6 compactness), K would be finitely coverable, contradicting (b) as q ⊥ ℓ. ∎
*Remark (all ℓ ≥ 11, weaker length).* For every prime ℓ ≥ 11, ELL0 (S-all) gives a non-residue class g₀ mod ℓ that is not
finitely coverable at length 3 for any q ⊥ ℓ, while the single family with fixed tail ℓ/(ℓ − g₀) (A = ℓ) is good on
the whole class n ≡ g₀ (mod ℓ): no local transport from length R_ℓ = 1 + r(ℓ/(ℓ − g₀)) ≤ ℓ to length 3 exists.
*Reading (Assessment).* On non-square classes, long-word sign existence is a congruence phenomenon already at length 5
(at least for ℓ ≤ 211), while length 3 is provably not; so a transport down the ladder must change the *fixed* letters
as n grows inside a congruence class — it must use the size of n (archimedean data), exactly what congruence-local
rules (identities, coverings, finite-state lifts) cannot supply. This is the precise sense in which "long-word sign
information" (which is local) "cannot be transported to L₃" (which needs non-local choices: ELL0).

## 4. Kill tests (registered at checkpoint 1) — outcomes

* **KT1 (sharp form "R₀ = 4") — FIRED.** Length 4 misses non-residue classes at level 1 for ℓ = 41 and most primes in
  [41, 199] (Prop 7). Registered fallback: least length catching all at level 1 is R₀(ℓ) ≤ 5 for every prime
  11 ≤ ℓ ≤ 211, = 4 for ℓ ≤ 37 and ℓ ∈ {43, 47, 59} (data). Theorem 6 is stated for length 4 *on the UCOVER branches*
  (where length 4 suffices at all 22 primes) and for length 5.
* **KT2 (cell-uniformity / F2) — did not fire.** (`scripts/z68_sign_cells.c`, `data/z68/sign/kt2_cells.txt`, 2.4 s.)
  At the 14 (★)-zero primes: no word with 4 ∣ t, N₋ ∈ [4, 26] pairs. At the 12 R₈-zero primes: no word with 8 ∣ t,
  4 ∣ t-pairs 6–28 (every such word good, as DK Prop 3.1 forces), N₋ ∈ [63, 131] pairs; R(p) = 2·#(4∣t pairs) +
  2·#{d ∣ p+1 : d ≡ 3 (4)} and R₈(p) = 2·#(8∣t pairs) + 2·#{d ∣ p+1 : d ≡ 7 (8)} reproduce the screen file exactly.
  **Consequence (CERTIFIED + PROVED reading).** "Every admissible 2-adic cell class of L₃(p) is non-empty" (per-cell
  exact-denominator mixing at length 3) is false at certified primes p > 10¹⁰; any transport whose output is only
  required to lie in an admissible union of cells would prove R₈(p) ≥ 1 there. A transport must use the full Jacobi
  cell union, i.e. the character (Z64_SDEEP Lemma 2: χ_n on L₃ is that union's indicator).
* **KT3 (information) — the "examine" branch was triggered and resolved.** (`scripts/z68_sign_lengths.c`,
  `z68_sign_kt3.py`, `z68_sign_contract.c`, `z68_sign_kt3b.py`; data `kt3_*`.) Over the 4171 primes p ≡ 1 (8) in
  (10⁴, 2·10⁵] with |L₃|, |L₄|, |L₅| ≥ 10: Spearman ρ(f₃, f₄) = +0.646, ρ(f₃, f₅) = −0.279 (f_r = −1 fraction of L_r).
  Not congruence data: ρ(f₃, f₄) = +0.61 within the 480 classes mod 9240 and +0.56 within the 256 classes of
  ((q/p))_{q ≤ 23}; +0.52 after regressing out band sums of (q/p), q < 3000, and Σ_{m < √p}(m/p).
  **Decomposition:** refinements (contractible length-4 words, 31 % of L₄): ρ = +0.745; non-refinements: +0.405;
  **unlinked** words (no rescaling move at either interior position: gcd(b, d) = gcd(a, c) = 1; 16 % of L₄):
  **ρ = −0.093** (−0.120 within classes mod 9240). At the hardest 1 % of primes by f₃ (f₃ ≤ 0.384): mean f₄ = 0.563
  (all words, vs 0.704), 0.527 (refinements, vs 0.786), 0.670 (unlinked, vs 0.679). At 21841 the unlinked fraction is
  36/50 = 0.72. **Reading (EVIDENCE):** the length-4 sign statistics carry information about the length-3 deficit only
  through the exact rescaling links of Lemma 2 / Theorem 3; length-4 words not linked to L₃ carry none detectable.
  (Registration deviation: the registered window was p ≤ 2·10⁵ with |ρ| thresholds; the decomposition and controls
  were added after ρ ≥ 0.3 triggered "examine", as registered.)
* **KT4 (brief).** (a) Squares: nothing is produced (F1). (b) 21841: consistent (F4 row; the bridge does not predict
  its deficit, and unlinked long words do not see it). (c) Not a finite covering of a square class: the only finite
  coverings here (Thm 6(a), Prop 7) are of classes with a non-residue at ℓ, and concern λ ≤ 4 or 5, not (S).

## 5. Task 2: what the bridge reduces (S) to

**Proposition 8 (vacuity of the reduction; PROVED from Prop 4).** For every n and every positive weight μ on
contractible pairs (w, j),
  Σ_{(w,j) contractible} μ(w, j)·[χ_n(A_w)·χ_n(X′Y′) = −1] > 0  ⟺  (S)(n),
and the left side equals Σ_{(t,u,v) good} Σ_{factorisations} μ. Any fixed-denominator estimate implying positivity of
a sum over contractible long words is a weighted estimate on L₃(n) itself (the weights being functions of the divisors
of u and v); by Prop 5 no estimate about bounded-digit words (ZQ_M, Zaremba(M), the fable-6 skew product) is about
contractible words at all. ∎
*Answer to the brief's task 2.* There is no explicit fixed-denominator twisted estimate, outside ZQ_M, that the bridge
reduces (S) to, other than (S) with divisor weights. Weighting does not change the scale problem: at fixed length every
word set of a fixed numerator is polylogarithmic (|L_r(n)| ≍ (log n)^{r−1} on average), so the B3 error-term constraint
(FRONTIER §3; Z64_SDEEP Prop 4) applies to every fixed-length encoding; the power-size encodings (length ≍ log n,
bounded digits) are exactly the ones outside the contraction's domain (Prop 5) (Assessment for the scale statement).

## 6. Verdict, screens, proposed FRONTIER text

**NARROWED.** No HOT LEAD. ES, (S) remain open.
* **PROVED (new):** Lemma 1(ii)–(iii) in the "fractional outer letters" form; Lemma 2 (rescaling moves, sign × χ(k));
  Theorem 3 (contraction, sign rule χ(A₃) = χ(A)χ(X′Y′)); Prop 4 (domain = refinements; bijection); Prop 5
  (bounded-digit words of length > M/2 + 3 are not contractible); Prop 8 (vacuity). **PROVED, computer-assisted
  (relative to UCOVER Thm S(a)):** Theorem 6 (no local transport from length 4 or 5 to length 3 at the 22 primes
  11 ≤ ℓ ≤ 101). **CERTIFIED:** Prop 7 tables (length 5 catches every non-residue class at level 1 for 11 ≤ ℓ ≤ 211);
  KT2 cell census at the 26 screen primes; 447 996 contractions checked. **EVIDENCE:** KT3 decomposition.
  **CONJECTURE:** P5.
* **Four FRONTIER §4 screens** (for the contraction bridge): T1 squares — PASS (sign-blind identity; nothing at
  squares). 8/131 — inherits L₃'s cells exactly; cell-restricted versions fail at certified primes (KT2). Tied
  modulus — FAILS to escape: X′Y′ ∣ b is n ≡ −(u+v) (mod uv), the W2 tied event. Fixed p — no averaging; but the bridge
  only re-parametrises L₃(p).
* **Fable-6 (board item) after this lane (Assessment).** Its upside λ(p) ≤ C log p stays a separate statement: no exact
  contraction reaches length 3 from its witnesses (Prop 5), and any congruence-local descent fails already from
  length 4/5 (Thm 6). A fable-6 success would be a new theorem about λ(p) only.

**Proposed FRONTIER §7 / z68 text (do NOT edit FRONTIER here):** *SIGN (`Z68_SIGN.md`):* Every HJ word of n cut at an
interior letter b is a length-3 word with fractional outer letters, n = bXY − XY′ − X′Y, χ_n(A) = χ_n(XY). PROVED: if
X′Y′ ∣ b (b ≥ 2X′Y′) then (b/X′Y′, X′Y, XY′) ∈ L₃(n) with χ_n(A₃) = χ_n(A)χ_n(X′Y′) (contraction); its domain is exactly
the refinements of length-3 words (factorisations of the outer letters), so it transports no information, and words
with bounded digits of length > M/2 + 3 are never contractible (so ZQ_M / fable-6 witnesses cannot be contracted).
PROVED (computer-assisted, rel. UCOVER Thm S(a)): no congruence-local transport from length-4 or length-5 good words to
length-3 good words at any prime 11 ≤ ℓ ≤ 101; CERTIFIED: length-5 good families catch every non-residue profile class at
level 1 for 11 ≤ ℓ ≤ 211 (length 4 does not for most ℓ ≥ 41). EVIDENCE: the cross-length sign correlation
(ρ ≈ +0.65 between the −1 fractions of L₃ and L₄, 4171 primes) is carried by rescaling-linked words; unlinked
length-4 words show ρ ≈ −0.09. Open: an archimedean (non-congruence, non-refinement) transport — i.e. B2.

## 7. Reproduction (all commands under `ulimit -v 6000000`, `timeout ≤ 1800`)
```
gcc -O2 -o prof scripts/z68_sign_profile.c && ./prof 11 199 4 2000000 > data/z68/sign/profile_R4_B2e6.txt   # 20 s
./prof 11 101 5 200000 > data/z68/sign/profile_R5_B2e5.txt; ./prof 103 127 5 200000 > data/z68/sign/profile_R5_B2e5_103_127.txt
./prof 131 211 5 2000000 > data/z68/sign/profile_R5_B2e6_131_211.txt                                          # 46 s
./prof 103 2000 5 200000 | grep -v '^W' > data/z68/sign/profile_R5_B2e5_103_2000.txt                          # 48 s
uv run --with sympy python scripts/z68_sign_verify_witness.py <profile file> <R>
uv run --with sympy python scripts/z68_sign_transport_check.py                                                # Thm 6 input
gcc -O2 -o cells scripts/z68_sign_cells.c && ./cells < (14 star + 12 r8 primes) > data/z68/sign/kt2_cells.txt
gcc -O2 -o len scripts/z68_sign_lengths.c && ./len 200000 > data/z68/sign/kt3_lengths_2e5.txt
uv run --with numpy --with scipy --with sympy python scripts/z68_sign_kt3.py
gcc -O2 -o con scripts/z68_sign_contract.c && ./con 200000 > data/z68/sign/kt3_contract_2e5.txt
uv run --with numpy --with scipy python scripts/z68_sign_kt3b.py
```

## 8. Internal hostile review
(pending)
