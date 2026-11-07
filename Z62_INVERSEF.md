# Z62_INVERSEF — inverse theorem for R(n) = 0 (tryhard lane, wave z62)

Lane: INVERSEF. Fresh attack; only external data used: `data/z58/screens/`. Scripts: `scripts/z62_inversef_*`, data `data/z62/inversef/`.

R(n) := #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}. Goal: "R(n)=0 ⟹ square-like structure", then "structure + p prime ⟹ another explicit ES solution (or impossible)".

**Verdict in one line.** The inverse half is PROVED in its exact form (§1–§2: R(p)=0 is equivalent to a precise "quadratic-non-residue arrangement" condition on the prime factors of 4Cp+1 for every C, with rigid consequences p ≡ 1 (8), 4p+1 ∈ ⟨primes ≡ 1 (4)⟩, p mod ℓ ∉ −Div((ℓ+1)/4) for ℓ ≡ 3 (4)); the "structure ⟹ other explicit solution" half FAILS as a theorem: the only explicit-solution machinery for a prime p is the identity families classified in §4, and (§5, CERTIFIED) these do not cover the non-square classes p ≡ 2041, 2521, 3361, 5161 (mod 9240) — primes ≡ 1 (840)-square classes that are QNR mod 11 — at any refinement tried (residual sub-classes GROW: 4 → 36 → 1089 → 3727). Zero primes are statistically square-like (§2.5) and the other solution families are mildly *suppressed*, not enhanced, at them (§6). NOT a hot lead. What survives: a clean complete classification of ES solutions and polynomial identities for prime p, reproduction of Mordell's 𝔐 as a corollary, and a sharp statement of why the identity/inverse route cannot close.

Status tags: PROVED / CONDITIONAL / CERTIFIED (computation, script named) / EVIDENCE.

## §0 Mandatory falsifiers (stated up front; re-checked in §9)

* (F1) odd squares n = m²: R(m²) = 0. Any structure claimed forced by R(n)=0 must HOLD at odd squares; any "second step" must FAIL at odd squares (must use p prime / non-square).
* (F2) R₈ (C-even half of R) vanishes at 12 primes in [10¹⁰, 1.1·10¹⁰] with R ≥ 12 (`r8_zeros_1e10.txt`). The inverse statement must distinguish R = 0 from R₈ = 0.
* (F3) 285 non-square composites n ≡ 1 (4), n ≤ 8·10⁶ have R(n) = 0 (`composite_zeros_le8e6.txt`). The inverse statement must hold for them.
* (F4) the 14 prime zeros (`star_prime_zeros.txt`) DO have other ES solutions; the second step must find them.

## §1 Three faces of R (PROVED; CERTIFIED n < 400 by `z62_inversef_basic.py`)

**Theorem 1.1.** For every n ≥ 1,
 R(n) = #{(u,B) ∈ ℕ² : 4uB | n+u+B}                                  (face Y)
   = #{(C,d) : C ≥ 1, d | 4Cn+1, d ≡ −1 (mod 4C)}                       (face C)
   = #{(d,r) : d ≡ 3 (mod 4), 4r | d+1, d | n+r}.                        (face d)

*Proof.* (Y): C = (n+u+B)/(4uB) is determined. (C): given (u,B,C) put d = 4uC−1; then d(4BC−1) = 16uBC² − 4C(u+B) + 1 = 4C(4uBC−u−B) + 1 = 4Cn+1, so d | 4Cn+1 and d ≡ −1 (4C). Conversely, if d | 4Cn+1 with d ≡ −1 (4C), put d' = (4Cn+1)/d; from dd' ≡ 1 and d ≡ −1 (mod 4C) we get d' ≡ −1 (4C); u = (d+1)/4C, B = (d'+1)/4C are integers and 4uBC − u − B = ((d+1)(d'+1) − (d+1) − (d'+1))/4C = (dd'−1)/4C = n. The maps are mutually inverse. (d): r := u, d := 4uC−1; from B(4uC−1) = n+u we get d | n+r and 4r | d+1; conversely C = (d+1)/4r, B = (n+r)/d, u = r. ∎

Consequences used below: R(n) = 0 ⟺ ∀r ≥ 1: n+r has no divisor ≡ −1 (mod 4r) ⟺ ∀C ≥ 1: 4Cn+1 has no divisor ≡ −1 (mod 4C) ⟺ ∀d ≡ 3 (4): (−n mod d) ∤ (d+1)/4. Only C ≤ (n+2)/4 can contribute (both cofactors are ≥ 4C−1, so (4C−1)² ≤ 4Cn+1).

## §2 Quadratic-residue structure (PROVED), and what R(p)=0 really forces

**Lemma 2.1 (odd squares; the model case).** If d ≡ 3 (4) and d ≡ −1 (mod 4r) then the Jacobi symbol (−r/d) = −1. Hence R(m²) = 0 for every odd m.
*Proof.* r odd: (r/d)(d/r) = (−1)^{(r−1)/2·(d−1)/2} = (−1)^{(r−1)/2} since (d−1)/2 is odd; and (d/r) = (−1/r) = (−1)^{(r−1)/2}; so (r/d) = 1 and (−r/d) = (−1/d) = −1. r = 2^a r', a ≥ 1: d ≡ −1 (mod 8) so (2/d) = 1, and (r'/d) = 1 as before (d ≡ −1 mod 4r'); again (−r/d) = −1. If d | m²+r with 4r | d+1 then gcd(d,m) = 1 (a common prime would divide r and d+1), so −r ≡ m² (mod d) gives (−r/d) = +1, contradiction. ∎

**Lemma 2.2 (character identity).** Let p ≡ 1 (4) be prime, C ≥ 1, q an odd prime with q | 4Cp+1. Then
 (q/p) = (p/q) = (−C/q) =: χ_C(q),
and q ↦ χ_C(q) depends only on q mod 4C; it defines a character χ_C of (ℤ/4C)^× with χ_C(−1) = −1.
*Proof.* 4Cp ≡ −1 (q) gives −Cp ≡ (2^{-1})² so (−C/q)(p/q) = 1; (p/q) = (q/p) by reciprocity (p ≡ 1 mod 4). Writing C = 2^a C', (−C/q) = (−1/q)(2/q)^a(C'/q) and (C'/q) = (q/C')(−1)^{(C'−1)(q−1)/4}: each factor depends on q mod 8 (if a ≥ 1, 8 | 4C) or mod 4C'. Value at q ≡ −1 (mod 4C): (−1/q) = −1, (2/q) = 1 if a ≥ 1, (C'/q) = 1 by the computation in Lemma 2.1. ∎

**Theorem 2.3 (arrangement characterization).** Let p ≡ 1 (4) prime, C ≥ 1, 4Cp+1 = ∏ q_i^{e_i}, H := ker χ_C (index 2 in (ℤ/4C)^×, −1 ∉ H). Then q_i mod 4C ∈ H ⟺ (q_i/p) = +1, and
 R has a hit at C (some (u,B) with this C) ⟺ some sub-multiset of the prime factors (with multiplicity) has product ≡ −1 (mod 4C).
In particular: (a) if every prime factor of 4Cp+1 is a QR mod p, there is no hit at C; (b) the number of QNR-mod-p prime factors (with multiplicity) is even; (c) a hit needs a sub-multiset with an ODD number of QNR factors whose H-components multiply to 1; e.g. if 4Cp+1 = q₁q₂ with q₁ QNR mod p, a hit occurs iff q₁ ≡ −1 (mod 4C).
*Proof.* Face C of Thm 1.1 plus Lemma 2.2; (b): ∏χ_C(q_i)^{e_i} = χ_C(4Cp+1) = χ_C(1) = 1. ∎

So **R(p) = 0 ⟺ for every C ≤ (p+2)/4, the QNR-mod-p prime factors of 4Cp+1 are "arranged" so that no sub-product (together with QR factors) is ≡ −1 (mod 4C)**. Odd squares satisfy this vacuously (no QNR factors at all: (m²/q) = 1). This is the exact inverse statement; everything "square-like" about R-zeros is a shadow of it.

**Corollary 2.4 (rigid consequences of R(p) = 0; PROVED).** (i) p ≡ 1 (mod 8) [face Y with (u,B) = (1,2): 8 | p+3 ⟺ p ≡ 5 (8)]. (ii) every prime factor of 4p+1 is ≡ 1 (mod 4) [C = 1, H = {1}]. (iii) for every prime ℓ ≡ 3 (4): p mod ℓ ∉ {−r : r | (ℓ+1)/4} [face d, d = ℓ]; e.g. p ≢ 2 (3); p ≢ 5,6 (7); p ≢ 8,10 (11); p ≢ 15,16,18 (19); p ≢ 17,20,21,22 (23). (iv) p ≢ 3 (mod 5) [d = 3 handles p ≡ 2 (3), d = 15 with r = 2 handles p ≡ 13 (15)]. (v) the odd part of p+2 has all prime factors ≡ 1 or 3 (mod 8) [C = 2: a factor ≡ 5 (8) would need a factor ≡ 3 (8) absent, but p+2 ≡ 3 (4) forces an odd number of factors ≡ 3 (4), i.e. some factor ≡ 3 (8) once 7 (8) is excluded].

**What is NOT forced (PROVED by example, from the 14 zeros).** "p is a square mod ℓ" is NOT forced for any ℓ ∉ {2,3} (nor mod 8·3 beyond p ≡ 1 (24)): 577 ≡ 2 (5), 409 ≡ 3 (7), 5212561 ≡ 2 (11) [least QNR prime of 5212561 is 11], 9601 ≡ 10 (23). For primes ℓ ≡ 1 (4) no single modulus-ℓ class is excluded by any (d,r) (face d needs ℓ | d ≡ 3 (4), so the excluded class lives mod ℓd'', not mod ℓ). "All prime factors of p+k split in Q(√−k)" is NOT forced: it fails at 8/24 values k ≤ 24 for the zero primes on average (random primes ≡ 1 (8): ~18/24) — `z62_inversef_struct.py`. [Parity remark, PROVED: for even k, the number ν_k of prime factors q of p+k with (−k/q) = −1 satisfies (−1)^{ν_k} = (−4k/(p+k)), a function of p mod 4k only; so ν_k is odd on half the classes whatever R(p) is.]

**§2.5 Statistical square-likeness (EVIDENCE, `z62_inversef_qnr.py`, `data/z62/inversef/qnr_stats.txt`).** Over C ≤ 40, the number of QNR-mod-p prime factors of 4Cp+1 (with multiplicity) is 20–46 for the 14 zero primes vs 32–90 for random primes ≡ 1 (8) of the same size; the number of C ≤ 40 with "all-QR" is 18–31 vs 4–24. Zero primes are clearly biased toward Theorem 2.3(a) but are far from satisfying it for all C — the arrangement condition (c) does the rest.

## §3 All ES solutions of a prime p (PROVED; CERTIFIED exhaustive for p < 80, `z62_inversef_identities.py`)

Let p ≥ 5 be prime, 4/p = 1/x+1/y+1/z. Then p divides exactly one or exactly two of x,y,z (all three is impossible: 4 = 1/x'+1/y'+1/z' has no solution).

**Theorem 3.1 (case (ii): p | y, p | z, p ∤ x).** The solutions are exactly
 x = g'YZ, y = p·m·g'·Y, z = p·m·g'·Z   where g',Y,Z,s ≥ 1, s | Y+Z, m := (Y+Z)/s, and **p + s = 4g'YZ**.
R(p) is the sub-family s = Y+Z (m = 1). Equivalent class form: p ≡ −4g'Y² (mod 4g'Ym − 1).
*Proof.* Write y = py', z = pz'. Clearing denominators: x(4y'z' − y' − z') = p·y'z'. Let g = gcd(y',z'), y' = gY, z' = gZ, gcd(Y,Z) = 1, κ' := 4gYZ − Y − Z, so xκ' = pgYZ. Since gcd(κ', YZ) = gcd(Y+Z, YZ) = 1, κ' | pg. If p ∤ κ' then κ' | g and x = p(g/κ')YZ, contradicting p ∤ x. So κ' = pκ'' with κ'' | g; put g = κ''g'; then x = g'YZ, and Y+Z = 4gYZ − pκ'' = κ''(4g'YZ − p), so s := (Y+Z)/κ'' is a positive integer with p + s = 4g'YZ and m = κ''. Conversely 1/(g'YZ) + 1/(pmg'Y) + 1/(pmg'Z) = (pm + Y + Z)/(pmg'YZ) = m(p+s)/(pmg'YZ) = 4/p. ∎

**Theorem 3.2 (case (i): p | z only).** The solutions are exactly
 x = bh(a+b)/t, y = ah(a+b)/t, z = p·a·b·h   where t ≡ 3 (4), gcd(a,b) = 1, t | a+b, and **pt + 1 = 4abh**.
*Proof.* z = pw; 4/p − 1/(pw) = (4w−1)/(pw) = 1/x + 1/y, so pw(x+y) = (4w−1)xy; p ∤ xy forces 4w − 1 = pt, and t ≡ 3 (4) as p ≡ 1 (4). Then 1/x+1/y = t/w ⟺ (tx−w)(ty−w) = w²; the divisor δ = tx − w of w² satisfies δ ≡ −w (mod t), and conversely any such δ gives integer x = (w+δ)/t, y = (w+w²/δ)/t (δ is coprime to t because gcd(w,t) = 1; w²/δ ≡ δ ≡ −w mod t). Writing δ = wb/a with a = w/gcd(w,δ), b = δ/gcd(w,δ) (both divide w since δ | w²), the condition is b ≡ −a (mod t). Finally with g = gcd(a,b), a = ga₁, b = gb₁: lcm(a,b) = ga₁b₁ | w, t | g(a₁+b₁) and gcd(t,g) = 1 (g | w, 4w ≡ 1 mod t), so t | a₁+b₁; rename (a₁, b₁, w/(a₁b₁)) → (a, b, h). The displayed x,y,z are integers and sum to (pt+1)/(pabh) = 4/p. ∎

The two theorems with their converses are exactly the two "master identities"; `z62_inversef_identities.py` enumerates both and compares with a brute-force list of ALL solutions for every prime p ≡ 1 (4), p < 80: no solution is missed and none is spurious (CERTIFIED). Note (for F1 below): both theorems are valid with p replaced by any odd n in the converse direction (they are identities), and Lemma 2.1-type arguments show **both families are empty for n = m²** (case (ii): with d = 4mg'Y−1 one gets (−g'/d)(n/d) = 1 while (−g'/d) = χ(−1) = −1 at d ≡ −1 mod 4g'; case (i): every prime q | w has (q/t) = (−t/q) = 1, so every divisor a of w has (a/t) = 1, and a ≡ −b (mod t) would give (a/t) = −(b/t)). This is Schinzel's obstruction in our normal form.

## §4 Polynomial identities for prime p: complete list (PROVED, degree count)

Call an *identity family* a residue class 𝒦 = {p ≡ c (mod D)} together with parameters (g',Y,Z,s) resp. (a,b,h,t) given by integer-valued polynomials in p on 𝒦 satisfying Thm 3.1/3.2 for all large p ∈ 𝒦. (Mordell's identities are of this kind.)

**Proposition 4.1.** Every identity family is one of:
 case (ii): (A) (Y,Z,s) constant, g' linear: class p ≡ −s (mod 4YZ), s | Y+Z.
     (B) (g',Y,m) constant, s linear: class p ≡ −4g'Y² ≡ −Y·m⁻¹ (mod 4g'Ym − 1).
     (C) (g',Y,s) constant, m linear: class p ≡ −(s+4g'Y²) (mod 4g'Ys).
 case (i): (A') (a,b,t) constant, h linear: class p ≡ −t⁻¹ (mod 4ab), t | a+b, gcd(t,2ab) = 1.
     (B') (a,h,t) constant, b linear: class p ≡ −(4a²h+1)/t (mod 4ah), t | 4a²h+1.
     (F1) (b,e,λ) constant: h = (p+λ)/4be, a = (pb+e)/λ, t = (a+b)/e (t linear in p!): class = {p ≡ −λ (4be), λe | pb+e+λb}.
     (F3) (e,h,λ) constant: a = (p+λ)/4eh, t = (4a²h+1)/λ, b = te − a (t quadratic): class = {p ≡ −λ (4eh), λ | 4a²h+1}.
*Proof sketch (full degree bookkeeping in the lane log; the key steps).* Case (ii): deg(p+s) = max(1, deg s) = deg g' + deg Y + deg Z and ms = Y+Z. If deg s ≤ 1 exactly one of g',Y,Z is linear: g' ⟹ (A); Y (say) ⟹ either m constant, s linear ⟹ (B) or s constant, m linear ⟹ (C). If deg s ≥ 2 then g', m, Z are constant and Y = (mp+Z)/(4g'Zm − 1) is linear, contradiction. Case (i): with e := (a+b)/t, 1 + deg t = deg a + deg b + deg h and deg t + deg e ≤ max(deg a, deg b). deg t = 0 gives (A') or (B'). deg t ≥ 1 and (wlog) deg a ≥ deg b force deg b + deg h ≤ 1: (0,0) is impossible (t | 1+4b²h constant); (deg b, deg h) = (0,1) gives, after substituting a = (pb+e)/(4beh−p) and comparing coefficients, that λ := 4beh − p is constant — this is (F1); (1,0) gives, from t(4aeh − p) = 4a²h+1, that u := 4aeh − p is constant (if deg u ≥ 1 then u | p²+4e²h in ℚ[p], impossible) — this is (F3) with the linear parameter renamed a. ∎
CERTIFIED: `z62_inversef_f1f3.py` builds 1661 F1- and 948 F3-instances for p < 3000 and checks each is an ES solution; `z62_inversef_covercheck.py` checks 878 classes of types (A)–(B') with gcd(c,D) = 1 and D | 9240 on three primes each (0 failures). (A)/(B) with s = Y+Z resp. m = 1 are exactly the R-classes; e.g. Mordell's p ≡ 3 (7) identity is (B) with D = 7, (Y,m) = (1,2): 4/p = 1/Z + 1/(2p) + 1/(2pZ), Z = (2p+1)/7 — a case-(ii) solution with m = 2, hence invisible to R (409 ≡ 3 (7) has R = 0).

**Lemma 4.2 (Schinzel).** No identity class contains an odd square; hence a class a (mod M) with a a square mod M is never a finite union of identity classes. (By §3's last paragraph: every identity instance at n = m² would be a case-(i)/(ii) solution for n = m², which do not exist.) ∎

## §5 Identity coverage computations (CERTIFIED, `z62_inversef_cover.py`, `data/z62/inversef/cover_M.txt`)

For a modulus M, enumerate all identity classes (c, D) of all seven families with D | M and mark residues; report classes a ≡ 1 (4), gcd(a,M) = 1 not covered.
* M = 840: uncovered = {1, 121, 169, 289, 361, 529} = Mordell's 𝔐 exactly (all squares). ✔ reproduces Mordell.
* M = 840·11: 34 uncovered = 30 square classes + **4 non-square**: 2041, 2521, 3361, 5161 (≡ 6, 2, 6, 2 mod 11; all in 𝔐 mod 840).
* M = 840·13: 4 non-square uncovered (2641, 3361, 4201, 9601); M = 840·17: 4 (2521, 5209, 10921, 11089).
* Refinement of the class 2041 (mod 9240) (`z62_inversef_refine3.py`, `data/z62/inversef/refine_2041.txt`): uncovered sub-classes / coprime sub-classes = 1/1 (M=9240), 36/2520 (M = 9240·2730, all seven families), 1089/725760 (M = 9240·2730·17·19, five families), 3727/8 709 120 (M = 9240·2730·17·19·12, five families). The *fraction* decays (10⁻² → 10⁻³ → 4·10⁻⁴) but the *count* grows; no exact finite cover appears.

**F4 (CERTIFIED, `z62_inversef_f4.py`, `data/z62/inversef/f4_zero_primes_cover.txt`).** Every one of the 14 zero primes lies in an identity class of modulus ≤ 239: 409, 23929, 1134241 ∈ (B)-class 3 (mod 7); 577, 329617 ∈ (B)-class 7 (mod 15) [p ≡ 2 (5)]; 5569 ∈ 31 (mod 39); 9601 ∈ 10 (mod 23); 83449 ∈ 23 (mod 59); 102001 ∈ 19 (mod 23); 712321 ∈ 11 (mod 23); 1724209 ∈ 19 (mod 39); 1726201 ∈ 143 (mod 239); 5212561 ∈ 43 (mod 87); 8813281 ∈ 103 (mod 111) — all of family (B), i.e. case-(ii) solutions with m ≥ 2. Three of them (9601, 1726201, 8813281) are NOT covered at modulus 840·ℓ(p), ℓ(p) their least QNR prime: the covering class involves a different prime than the least QNR.

## §6 Why the "structure ⟹ other solution" half cannot be a theorem via identities (EVIDENCE + heuristic)

1. **The complete inverse statement is the sieve.** R(p) = 0 ⟺ p avoids every R-class (A: −(Y+Z) mod 4YZ; B: −Y mod 4g'Y−1). This is all; any "square-like" statement forced by R = 0 is a reformulation of avoiding these classes (Cor 2.4 lists the rigid ones). The R-classes are a sub-family of the identity classes, so "R(p) = 0 ⟹ p in an identity class" is a statement about *finite exact covers* of residue classes by identity classes.
2. **The identity-cover program and its only possible closure.** If for each prime ℓ all classes a (mod M_ℓ) with (a/ℓ) = −1 were finite unions of identity classes, then every large prime would have an ES solution (take ℓ = least QNR prime of p, ℓ ≤ p^{1/4√e+ε} by Burgess; p ≡ 1 (4) makes (p/ℓ) = (ℓ/p)). Lemma 4.2 is no obstruction to this (such a is not a square mod M_ℓ). This is exactly the "structure (p QNR mod ℓ) ⟹ explicit solution" shape the brief asks for, and it uses primality only through "p is not a QR mod everything".
3. **It does not close, already at ℓ = 11** (§5): four non-square classes mod 9240 are uncovered and refinement by 2,3,5,7,13,17,19 leaves a growing number of uncovered sub-classes. Heuristic reason: identity classes with modulus D carry ≍ τ((D+1)/4)²-many residues, so classes that are QNR only at ℓ (QR at every other prime ≤ X) are hit only by D with ℓ ∥ D, whose total sieve weight up to X is ≈ (log X)²·(log log X)/ℓ; the uncovered density within such classes at level X is ≈ exp(−c(log X)²/ℓ) > 0 for every finite X. An exact finite cover is a coincidence of the Mordell-840 type, and the computations say it does not recur at 11 (nor 13, 17).
4. **The 14 zeros do not point to a hidden second family.** `z62_inversef_other.py` (`data/z62/inversef/other_families.txt`): counts R^{(m)}(p) of case-(ii) solutions with (Y+Z)/s = m, and of case-(i) solutions per t ≤ 63. At the zero primes R^{(2)} ∈ {0,…,16} (102001 and 8813281 have R^{(2)} = 0 too) vs 4–34 for random primes ≡ 1 (8) of the same size; case-(i) totals 10–248 vs 24–298. The other families are mildly *suppressed* at R-zeros (consistent with §2.5 square-likeness), not forced; they are nonempty at the 14 because their expectations ≫ 1, not because R = 0.
5. Consequently "R(p) = 0 ⟹ [square-like] ⟹ [other solution]" has the wrong sign: square-likeness pushes every family toward zero simultaneously; the only thing that can save a prime is that it is not a square mod everything (least-QNR), and converting that into an explicit solution requires the finite covers that do not exist (EVIDENCE level, §5).

## §7 What is actually established

* PROVED: Thm 1.1 (three faces), Lemma 2.1–2.2, Thm 2.3 (exact inverse characterization: the QNR-arrangement condition), Cor 2.4 (rigid consequences), Thm 3.1–3.2 (complete solution set of a prime, two master identities), Prop 4.1 (all polynomial identity families: seven), Lemma 4.2 (no identity class contains an odd square).
* CERTIFIED: faces agree (n < 400); master identities exhaustive (p < 80); 878 identity classes validated; F1/F3 instances validated; Mordell's 𝔐 recovered at M = 840; non-square uncovered classes at 840·{11,13,17}; refinement residuals; F4 coverings for the 14 zeros.
* EVIDENCE: §2.5 (square-likeness statistics), §6.4 (other families not enhanced), §6.3 (no finite cover at ℓ = 11).
* No CONDITIONAL theorem is claimed. NOT a hot lead.

## §8 Residual questions worth a lane
* Is there a *provable* obstruction (à la Schinzel) showing the class 2041 (mod 9240) is never a finite union of identity classes? One would need infinitely many non-square n ≡ 2041 (9240) outside all identity classes; the heuristic count of such n up to X is X·exp(−c log²X) → 0, so this is probably false as stated and the non-coverability is "soft" (no exact cover, though the uncovered set has density 0). A proof would need a different invariant.
* The arrangement condition of Thm 2.3 is a clean target for a *bilinear* count: R(p) ≥ #{C : 4Cp+1 = q₁q₂, q₁ ≡ −1 (4C)} — counting primes q₁ ≡ −1 (4C) with (4Cp+1)/q₁ prime. That is the standard analytic route, not an inverse one.

## §9 Falsifiers re-checked
* (F1) odd squares: Lemma 2.1 (R(m²) = 0), Thm 2.3(a) (all-QR for every C), §3 last paragraph (no case-(i)/(ii) solution at all), Lemma 4.2 (never in an identity class). Every structure claimed holds at squares; the identity second step fails at squares exactly as it must. ✔
* (F2) The inverse statement is per-C (Thm 2.3); R₈ = 0 is the sub-condition "even C only". The 12 primes in `r8_zeros_1e10.txt` have R ≥ 12 from odd C, so odd-C arrangement hits exist there; the statements distinguish. ✔
* (F3) Thm 1.1 / Cor 2.4(i)–(v) are proved for every n ≡ 1 (4) (nothing uses primality except Lemma 2.2's (p/q) = (q/p) rewriting, which is cosmetic); the 285 composites satisfy them by Thm 1.1. The identity second step is not claimed for them. ✔
* (F4) Each of the 14 zero primes has an explicit identity solution (family (B), modulus ≤ 239, §5), i.e. the "second step" succeeds at all 14 — but only by an identity found per prime, not by a theorem, and three of them need a prime other than their least QNR. ✔ (and the reason it is not a theorem is §5–§6.)
