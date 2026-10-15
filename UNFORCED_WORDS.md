# UNFORCED_WORDS — forced vs unforced words, CONJECTURE U and the anti-Landau event (task O231, spark relay Z1)

**ES is not solved here, and no infinite case of it is claimed.** Labels as in DISCOVERIES.md. Memos `BRAINSTORM/z7_*.md`;
scripts `scripts/z7_*`. Notation (SYNTHESIS_SPARKS5): n ≡ 1 (4) odd, ψ = (·/n) (Jacobi; Legendre at primes); words
w = (t, u, v) ∈ ℤ³_{>0}, tuv − u − v = n; A = tu − 1, B = tv − 1; sides N_t = tn + 1 = AB, N_u = n + u = Av,
N_v = n + v = Bu; χ(w) = ψ(A) = ψ(B); certificate ⟺ χ = −1 (N₋ = #certificates). A positive integer x is *clean* if no
prime r | x has ψ(r) = −1. C_n := the multiplicative semigroup of clean integers. Forced = some side clean
(⟹ χ = +1, Lemma S); U = #words with no clean side. Words are counted ordered in (u, v), as in s5_U.c.

## 0. Iteration log (construction → kill → which hypothesis → modification)
(I1) Construction: look for "automatic" unforced words — words whose sides are polynomials in n with an NR factor
forced by a symbol. Found: n ≡ 5 (8) is trivial (ψ(2) = −1). For n ≡ 1 (8): the word (n + 2, 1, 1) has sides
(n + 1)², n + 1, n + 1, so it is unforced iff n + 1 is unclean. → §1.
(I2) Kill: the same n + 1 also carries a *certificate* (u = 1 family, A ranges over all divisors of n + 1). Every word
with min(t, u, v) ≤ 2 lives on one of the three "automatic" side numbers n + 1, n + 2, 2n + 1, and on each of these
families unforced ⟺ certificate (Prop F). So nothing is gained over ES-five unless min ≥ 3. → §1.

## 1. The automatic families: unforced ⟺ certificate when min(t, u, v) ≤ 2 (PROVED)
**Lemma 1.1 (n ≡ 5 (8)).** For odd non-square n ≡ 5 (8), the word (1, n + 2, 2) is unforced: N_t = n + 1 and
N_u = 2(n + 1) are even and ψ(2) = −1; N_v = n + 2 has ψ(n + 2) = ψ(2) = −1, so it has a prime factor with ψ = −1.
Hence U(n) ≥ 1. (Not a certificate: χ = ψ(n + 1) = +1.) So CONJECTURE U has content only at n ≡ 1 (8). ∎

**Families with a small parameter.** A word with t = 1 is (1, d + 1, (n+1)/d + 1) for a divisor d = A of n + 1 (every
divisor occurs); u = 1: (d + 1, 1, (n+1)/d), A = d, again every divisor of n + 1; t = 2: A any divisor of 2n + 1,
u = (A+1)/2, v = ((2n+1)/A + 1)/2; u = 2: A = 2t − 1 any divisor of n + 2 (odd), v = (n+2)/A. (v = 1, 2: symmetric.) The
fixed side of these families is n + 1 (t = 1, u = 1, v = 1), 2n + 1 (t = 2) or n + 2 (u = 2, v = 2).

**Prop F (PROVED).** Let n ≡ 1 (8) be odd, X ∈ {n + 1, n + 2, 2n + 1} and F_X the family(ies) with fixed side X. TFAE:
(i) F_X contains a certificate; (ii) F_X contains an unforced word; (iii) X is unclean.
*Proof.* (iii) fails ⟹ every word of F_X has the clean side X, so it is forced and (Lemma S) not a certificate. (iii) ⟹
(i): pick a prime r | X with ψ(r) = −1 and take A = r (every divisor of X is an admissible A in F_X); χ = ψ(r) = −1.
(i) ⟹ (ii): a certificate has no clean side (Lemma S). ∎
**Corollary 1.2.** If U(n) = 0 or N₋(n) = 0, then n + 1, n + 2 and 2n + 1 are all clean (a *Landau triple*), and
then every word with min(t, u, v) ≤ 2 is forced. Conversely, at a Landau triple U(n) ≥ 1 ⟺ some word with
min(t, u, v) ≥ 3 has three unclean sides. At primes p ≡ 1 (8), by Lemma S's formula ψ(r) = (−X/r): p + 1 clean ⟺ all odd
r | p + 1 are ≡ 1 (4); p + 2 and 2p + 1 clean ⟺ all their prime factors are ≡ 1, 3 (8). (Same for composite n with
Jacobi symbols.)
So the anti-Landau event is genuinely weaker than a certificate only on words with min ≥ 3. On the automatic families
the two coincide exactly, and both reduce to the Landau-type condition "one of three fixed linear forms has a prime
factor in a non-split class".

**Numerics (EVIDENCE; `scripts/z7_types.c`).** All 464 288 primes p ≡ 1 (8), p < 3·10⁷: U ≥ 1 everywhere. The least
min(t, u, v) of an unforced word is ≥ 3 exactly at the 10 508 Landau-triple primes (0 mismatches), as Prop F
predicts. Over n ≡ 1 (8) non-square ≤ 2·10⁵ including composites there are 0 mismatches, and the only U = 0 case is
105 = 3·5·7, a Landau triple (106 = 2·53, 107, 211 are all clean mod 105). The Landau-triple fraction among primes
≡ 1 (8) is 3.3 % / 2.7 % / 2.2 % on the decades (3·10⁴, 3·10⁵) / … / (3·10⁶, 3·10⁷). This slow decay matches the
(log p)^{−3/2} heuristic for three half-dimensional conditions. Largest least-min observed at a Landau triple: 18.

## 2. Where the anti-Landau content sits, and parity across a family
**Lemma 2.1 (symbol-visible and symbol-blind sides; PROVED).** ψ(N_u) = ψ(u), ψ(N_v) = ψ(v), ψ(N_t) = ψ(1) = +1, and
ψ(u)ψ(v) = χ. Hence:
(a) a word with ψ(u) ≠ ψ(v) is a certificate (χ = −1, all sides unclean);
(b) a word with ψ(u) = ψ(v) = −1 has N_u, N_v unclean for free. It is unforced iff N_t ∉ C_n, i.e. tn + 1 has
    ≥ 2 prime factors (with multiplicity) with ψ = −1;
(c) a word with ψ(u) = ψ(v) = +1 is unforced iff all three sides contain ≥ 2 ψ-odd prime factors.
So a non-certificate unforced word always needs the t-side event "tn + 1 ∉ C_n". No symbol can detect this event,
because ψ(tn + 1) = 1 identically. This is the precise "anti-Landau" kernel of CONJECTURE U beyond ES-five. In cases
(b)/(c) a congruence covering cannot supply it: any covering identity evaluates fixed symbols, and those are all +1 on
the class n ≡ 1 (mod M) (B1-type).

**Flip Lemma 2.2 (PROVED).** Fix X ∈ {t, u, v} and its value. The X-family of words is in bijection with the set of
divisors D of N_X in the class D ≡ −1 (mod X): D = A for X = t (then B = N_t/A), D = A for X = u (then t = (A+1)/u,
v = N_u/A), and D = B for X = v. On it, χ = ψ(D). Hence the family contains a certificate iff the image of
Div(N_X) → (ℤ/X)^× × {±1}, d ↦ (d mod X, ψ(d)), contains (−1, −1). In particular, if some word of the family has
D and N_X has
* a prime r ∥ N_X with ψ(r) = −1 and r ≡ 1 (mod X) (take D′ = Dr or D/r), or
* primes r ∥ D, s ∥ N_X/D with r ≡ s (mod X) and ψ(r) ≠ ψ(s) (take D′ = Ds/r),
then the family contains a certificate. *Proof.* D′ ≡ D ≡ −1 (mod X), D′ | N_X, and ψ(D′) = −ψ(D). Each D in the class
gives a positive word: for X = u, t = (D+1)/u ≥ 1 and v = N_u/D ≥ 1, and similarly for the others. ∎
For X ∈ {1, 2} every odd r is ≡ 1 (mod X), which recovers Prop F. For X ≥ 3 the flip needs a ψ-odd prime of N_X in
the class 1 (mod X) (or a matched swap). That is a divisor-in-class condition with the modulus X part of the word,
i.e. B2 verbatim.

**Numerics (EVIDENCE; `scripts/z7_flip.py 9 200000`, primes p ≡ 1 (8) < 2·10⁵).** There are 94 262 non-certificate
unforced words. 73 % are flippable by Lemma 2.2's two moves. 96 % have a certificate somewhere in one of their three
families. Flippable but no family certificate: 0, consistent with the lemma. So "parity across the family of a shared
side" is the typical mechanism by which an unforced word sits next to a certificate. But the flip needs a prime in a
moving residue class, so it is not a deterministic bridge U ≥ 1 ⟹ N₋ ≥ 1 (goal 2): Lemma 2.2 *is* the e-slice form
−1 ∈ Σ_e(N), with e = X.

## 3. Extending Prop F: s = 3, 4, 7; Landau depth; a Dickson-conditional obstruction
(I3) Construction attempt: push Prop F to larger fixed parameters s, using the *fixed* QR prime 2 as a flip tool.
**Prop F′ (PROVED; p ≡ 1 (8) prime).** For s ∈ {3, 4, 7} and X ∈ {p + s, sp + 1}: the X-family (u = s or v = s,
resp. t = s) contains a certificate ⟺ it contains an unforced word ⟺ X is unclean.
*Proof.* As in Prop F it suffices to show that X unclean ⟹ some admissible D (D | X, D ≡ −1 (mod s)) has ψ(D) = −1.
For odd primes r | X, Lemma S gives ψ(r) = (−s/r), and ψ(2) = +1.
* s = 3: 4 ∥ X (since p ≡ 1 (8)). Let r be an odd prime of X with ψ(r) = −1. Then D = r (if r ≡ 2 (3)) or D = 2r
  (if r ≡ 1 (3)) is admissible.
* s = 4: X is odd and ψ(r) = (−4/r) = (−1/r), so ψ(D) = (−1/D) = −1 for every D ≡ 3 (4). The family is nonempty ⟺
  X has a prime r ≡ 3 (4) ⟺ X is unclean, and then *every* word of the family is a certificate.
* s = 7: 8 | X, and 7 ∤ X since p ≠ 7. ψ(r) = (−7/r) = (r/7) (quadratic reciprocity), so a ψ-odd r is a
  non-residue mod 7. The powers 1, 2, 4 of 2 run through the residues mod 7, so one of r, 2r, 4r is ≡ 6 (mod 7), and it
  divides X. ∎
*2-adic remark.* For X = s ≡ 7 (8), or 4 | s, every word of the family is a certificate. For t ≡ 7 (8), 8 | AB forces
4 | A or 4 | B; for u ≡ 7 (8), 8 | Av forces 4 | A or 4 | v. This is the three-bit law on a family: χ is 2-adic
(SYNTHESIS_SPARKS4 §1). For s = 7 it combines with the 2-trick, so nonemptiness ⟺ uncleanness. For s = 8 the
equivalence fails (nonempty needs a divisor ≡ 7 (8)).
**Numerics (EVIDENCE; `scripts/z7_propF.py 100000`, primes p ≡ 1 (8) < 10⁵).** For s = 1, 2, 3, 4, 7 and both kinds
of family there are 0 mismatches in "unclean ⟺ certificate ⟺ unforced". At s = 5, 6, 8, "unclean ⟹ certificate" fails
at 183–328 primes per family. "Unforced ⟺ certificate in the family" fails only at s = 5 (24 resp. 39 primes). At
s = 6, 8 the family's unforced words all coincide with its certificates even when the side is unclean.

**Landau depth.** Let K(p) = max{K : p + s and sp + 1 are clean for all 1 ≤ s ≤ K}.
**Corollary 3.1 (PROVED).** U(p) = 0 or N₋(p) = 0 ⟹ K(p) ≥ 4 and also p + 7, 7p + 1 are clean. If K(p) ∈ {2, 3, 6},
then some word with min(t, u, v) = K(p) + 1 is a certificate (s = 3, 4, 7 respectively).
**Numerics (EVIDENCE; `scripts/z7_depth.c`, all 464 288 primes p ≡ 1 (8) < 3·10⁷).** The histogram of K is
0: 356 992, 1: 96 788, 2: 7 619, 3: 1 965, 4: 715, 5: 153, 6: 37, 7: 6, 8: 8, 9: 4, 10: 1 (p = 21 746 761).
The least min(t, u, v) of an unforced word equals K(p) + 1 at every prime with K ∈ {2, 3, 6, 7, 9, 10}. It exceeds
K(p) + 1 at 41/715 primes with K = 4, at 29/153 with K = 5 and at 3/8 with K = 8, always by ≤ 9.
**Theorem 3.2 (CONDITIONAL on Dickson's prime k-tuples conjecture).** For every K ≥ 1 there are infinitely many primes
p ≡ 1 (8) with K(p) ≥ K. At these primes every word with min(t, u, v) ≤ K is forced (neither a certificate nor
unforced).
*Proof.* Let M = 8·∏_{3 ≤ ℓ ≤ 2K+1} ℓ^{a_ℓ} with ℓ^{a_ℓ} > K + 1 (ℓ prime; also 2^{a_2} > K + 1). Put p = 1 + Mx. For
1 ≤ s ≤ K and ℓ ≤ 2K + 1, p + s ≡ sp + 1 ≡ s + 1 (mod ℓ^{a_ℓ}), so v_ℓ(p + s) = v_ℓ(sp + 1) = v_ℓ(s + 1). Hence
p + s = (s + 1)·L_s(x), sp + 1 = (s + 1)·L′_s(x) with L_s = 1 + (M/(s+1))x and L′_s = 1 + (sM/(s+1))x. The forms p,
L_s, L′_s (L′_1 = L_1) are pairwise non-proportional, ≡ 1 mod every ℓ ≤ 2K + 1, and number ≤ 2K + 1 < ℓ for every
other prime ℓ. So the system is admissible, and Dickson gives infinitely many x with all of them prime. Then every
prime factor of s + 1 is ≤ K + 1 and is a residue mod p (p ≡ 1 mod ℓ for odd ℓ, p ≡ 1 (8) for ℓ = 2). Also
ψ(L_s) = ψ(p + s)ψ(s + 1) = ψ(s) = +1, because s is a product of primes ≤ K. Likewise ψ(L′_s) = ψ(1)ψ(s + 1) = +1. So
p + s and sp + 1 are clean. A word with min = s ≤ K has the side sp + 1 (if t = s) or p + s (if u or v = s). ∎
So **no proof of CONJECTURE U (or of ES-five) can use only words of bounded minimum parameter**. This is the U-analogue
of B2's "fixed finite slice sets fail i.o. under H" and of SQ_±'s Dickson-conditional "no finite t-set". The
hypothesis a U-proof must violate is boundedness of the family; the escape is H-A (growing family). The observed depth
grows slowly: max K = 10 below 3·10⁷.

## 4. A sharper unforcedness: U2 (A and B both unclean)
Since A | N_t, N_u and B | N_t, N_v, a word whose A and B both contain a ψ-odd prime is unforced. Let U2 = #such
words. Then **N₋ ≤ U2 ≤ U (PROVED)**: a certificate has ψ(A) = ψ(B) = −1. A word in U ∖ U2 has one of A, B clean, and
the side containing the other factor is unclean only through v or u.
**Numerics (EVIDENCE; z7_types.c, all 464 288 primes p ≡ 1 (8) < 3·10⁷).**
* U2 ≥ 1 everywhere.
* Σ N₋/Σ U2 = 0.873 and Σ U2/Σ U = 0.882.
* min N₋/U2 = 0.620 (p = 23 125 409: 364/587). At the three primes where N₋ ≥ U/2 fails (5 270 849, 17 188 937,
  21 387 257), N₋/U2 = 192/275, 164/245, 126/191 ≈ 0.70.
* Over n ≡ 1 (8) ≤ 2·10⁵ (composites too), U2 = 0 only at n = 105.

**CONJECTURE U2 (EVIDENCE as above):** for odd non-square n ≡ 1 (4), U2(n) = 0 ⟺ n = 105. It is intermediate between
CONJECTURE U and SQ₅ (N₋ ≤ U2). Its bridge inequality "N₋ ≥ U2/2" is unrefuted to 3·10⁷ at primes ≡ 1 (8), with
margin (min 0.62). It is only EVIDENCE, and in view of §2 probably a distributional fact rather than an injection.
For n ≡ 5 (8), U2 ≥ 1 trivially: the word (1, 3, (n+1)/2 + 1) has A = 2 (ψ(2) = −1) and B = (n+1)/2, and
ψ(B) = ψ(n+1)ψ(2) = −1. It is Mordell's classical certificate.

**Remark 4.1 (the forcing hierarchy; R227 D18 in this language).** Forcing notions interpolate between U and N₋:
ψ-clean side (Lemma S) ⊂ congruence-pinned sides (R225/R227 D4–D5: (−1/·)-clean or defective N_u with A ≡ −1 (mod u)
pinning A mod 4 or mod 8) ⊂ *family-exact forcing*: "the X-family has no certificate" (Flip Lemma 2.2 criterion). With
family-exact forcing on all three sides, "unforced" means "each of its three families contains a certificate". The
corresponding U_fam satisfies U_fam ≥ 1 ⟺ N₋ ≥ 1, tautologically, since a certificate lies in its own families. So the
sharper the forcing notion, the closer "U ≥ 1" is to ES-five itself. CONJECTURE U is the *coarsest* member, and its
gap to ES-five is exactly the words whose three families are certificate-free for non-clean reasons: R227's
congruence-pinned sides, and more generally sides whose ψ-odd primes sit only in classes that Lemma 2.2 cannot move.
The same mechanism can also force χ = −1 on a whole family (R227 D4/D5; Prop F′'s s = 4, 7 families consist entirely
of certificates). In every case the forcing is a function of (N_X's factorization, X mod 8): the three-bit law on a
family.

## 5. Goal 3: where "N₋/U ≈ 3/4" comes from. It is a stratum mixture; the robust law is Haar 3/4 at large min
**Prop 5.1 (PROVED, finite computation; `scripts/z7_haar2.py 5`).** For every p ≡ 1 (4), the solutions of
tuv − u − v ≡ p (mod 2⁵) number 1280 for each class p mod 16. Exactly 3/4 of them are five-slice (4 | t, u, v, A or B).
The condition is a mod-4 condition and 2⁵ already resolves A, B mod 4, so the 2-adic Haar mass of the certificate set on
X_p(ℤ₂) is exactly 3/4, independently of p mod 16. This is the pointwise local version of (J)39 Lemma 2.1's 240/320.
**Stratified census (EVIDENCE; `scripts/z7_ratio.c`, all primes p ≡ 1 (4) in windows; table = Σ N₋/Σ N by
min(t, u, v) ≥ m, p ≡ 1 (8)):**

| window | m ≥ 1 | m ≥ 3 | m ≥ 10 | m ≥ 50 | N₋/U (m ≥ 1) | N₋/U (m ≥ 3) |
|---|---|---|---|---|---|---|
| (10⁴, 3·10⁴) | 0.572 | 0.761 | 0.719 | — | 0.765 | 0.902 |
| (10⁵, 2·10⁵) | 0.598 | 0.758 | 0.728 | — | 0.771 | 0.888 |
| (10⁶, 1.3·10⁶) | 0.618 | 0.756 | 0.733 | 0.740 | 0.771 | 0.872 |
| (10⁷, 1.03·10⁷) | 0.635 | 0.754 | 0.736 | 0.748 | 0.770 | 0.859 |
| (2.9·10⁷, 2.93·10⁷) | 0.640 | 0.753 | 0.736 | 0.746 | 0.769 | 0.854 |

(p ≡ 5 (8) is similar at m ≥ 10, 50: 0.76, 0.755. At m = 3, 4 the class is distorted by its all-certificate families
u, t ≡ 3 (mod 8) → N_X ≡ 0 (8), giving 0.81–0.85.)
**Reading (Assessment).**
* Words with large min(t, u, v) carry the Haar sign law N₋/N ≈ 3/4 already at p ≈ 10⁴, with no visible drift.
* The whole deficit of N₋/N, and its slow drift 0.57 → 0.64, lives in the strata min ≤ 2. These are the automatic
  families of Prop F, where (i) a clean p + 1, p + 2 or 2p + 1 makes the whole family χ = +1 (a Landau event of
  probability ≍ 1/√log p), and (ii) if the side is unclean, the certificate fraction on the family is ≤ 1/2 exactly
  as in Lemma 5.2 below. That is far below 3/4. Hence N₋/N drifts up as the logarithmic weight of the min ≤ 2
  strata, and the Landau probability, decay.
* **Lemma 5.2 (PROVED).** Let F be an automatic family with fixed side X = ∏ r^{e_r}. Every divisor of X is an
  admissible D, so Σ_{D|X} ψ(D) = ∏_{ψ(r)=1}(e_r+1)·∏_{ψ(r)=−1}[e_r even]. Hence the number of certificates in F is
  (τ(X)/2)·(1 − ∏_{ψ(r)=−1}[e_r even]/(e_r+1)). This is exactly τ/2 (flip involution) if some ψ-odd prime has an odd
  exponent, and τ/3 if the ψ-odd part of X is r². In the latter case, R227 D4's "defective side, rate 1/3" is this
  lemma. So N₋(F) ≥ U(F)/2 whenever a ψ-odd prime of X has odd exponent, but not for X = r²·(clean).
* **SHARP (EVIDENCE + Lemma 5.2): every N₋ ≥ U/2 failure at n ≡ 1 (8) sits on a defective n + 1.** All 8 failures with
  n ≡ 1 (8) in R227's complete list (n < 10⁷) and among the primes < 3·10⁷ (110 897, 1 512 089, 2 152 097,
  3 000 329, 5 270 849, 9 948 977, 17 188 937, 21 387 257) have **ψ-odd part of n + 1 equal to 3²** (`scripts/z7_defect_p1.py`;
  the ninth, 4 095 125 = 5³·181², is ≡ 5 (8)). The largest family (t = 1 and u = 1, indexed by Div(p + 1)) then has
  certificate rate exactly 1/3. At p = 5 270 849, for example, the min ≤ 2 strata have N₋/U = 148/333, while min ≥ 3
  has 44/56. Splitting all 464 288 primes p ≡ 1 (8) < 3·10⁷ by the ψ-odd profile of p + 1 gives min N₋/U:
  odd exponent present 0.564 (320 343 primes, 0 failures); clean 0.600 (107 296); even, ψ-odd part 3² 0.475
  (25 666, 3 failures); other even profiles 0.549 (10 983). Why 3: 3 | p + 1 forces p ≡ 2 (3), hence ψ(3) = −1
  automatically, so 3² is the most frequent pure-square defect. The failure needs, in addition, an unusually lopsided
  min ≥ 1 stratum (3 failures among 25 666 such primes).
* "N₋/U ≈ 3/4, scale-stable" is a weighted average of two strata moving in *opposite* directions. The min = 1 stratum
  has N₋/U ≈ 0.59 (> 1/2 because some non-certificates of a flip pair are forced through their u/v side). The min ≥ 3
  stratum has 0.90 → 0.85, slowly decreasing, since its forced share falls slower than its non-certificate share. So
  the stability is a coincidence of the window 10⁴–3·10⁷, not a law. It should not be explained by a 2-adic mass
  computation; the 2-adic mass explains N₋/N at large min instead (Prop 5.1).
* At large min, ≈ 12–15 % of all words are forced, i.e. roughly half of the Haar non-certificate quarter. Forcing does
  not deplete certificates there; it only sorts non-certificates.
