# Z60_RAYCLASS — norm forms in varying imaginary quadratic fields. Verdict: **narrowed** (no lead)

**ES is OPEN; (MS), U_II, CONV-II are open. Nothing here proves or disproves them.** Internal, unrefereed. Labels:
PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z60_rayclass_*`, data
`data/z60/rayclass/` (README-style headers in the files; exact commands in §6).

Notation: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} ((★)); R₈ its C-even half; U_II = (★) ∪ (a = 1 line); N_II the full
Type II count (4abcd = a + b + nc); 𝔐 = {1, 121, 169, 289, 361, 529} mod 840. Throughout, for odd n, squarefree t₀ ≥ 1 and
r ≥ 1: ω = √(−t₀n), O = ℤ[ω], K_{t₀} = ℚ(√(−t₀n)), **β_r := 1 + rω**, N(β_r) = 1 + t₀nr². K_C := ℚ(√(−Cn)).
S₁(n) := #{(a,b,c) ∈ ℕ³ : 4abc = a + b + nc} (Type II with d = 1, the "shot family"; all of it lives in the single field
ℚ(√−n), Lemma 1(iv) with t₀ = 1).

## 0. Bottom line and falsifier table

**Bottom line.** The ray-class picture is a faithful re-encoding of the tied divisor event and does not move B2. What it
does settle (scoped): (1) one dictionary for (★), the a = 1 line and the full family — divisor events along the ray
r ↦ 1 + r√(−t₀n) of one field, with moduli t₀r², 4t₀r², 2t₀r (Lemma 1); T1 is "the field ℚ(√(−t₀s)) of the square class s
of n lies in ℚ(ζ_M)" (Lemma 2), giving all dead levels of n = s·m² (Cor 2.1). (2) *Per field*, every ring class group of
every order of K_C sees N𝔞 mod 4C only through real characters (Prop 3.1, generalising WINDMILL_REDUCTION Prop 10.3 to all
orders, all moduli, the prime 2); at the 14 (★)-zero primes this visible layer is satisfied at 64–90 of the levels C ≤ 300
while the event holds at none (CERTIFIED). (3) *Across fields* the information barrier is genuinely weaker: class data of
two orders in two different fields can determine a quartic residue character (Prop 4.1 + an instance with ℚ(√−17), ℤ[17i]),
so Z53_WILDCARD row 6's "joint constraints" escape is real *as information*; but the only relations that class field
theory imposes on the prime divisors of β are total-product relations (Prop 4.2), so it is not real *as forcing*.
(4) **Class number.** Class-number size is T1-blind (squares have ring class numbers ≫ √n/log log n, Prop 5.1). In a
*fixed* field the expected count of a ray family is proportional to L(1, χ) (Prop 5.2 + EVIDENCE: Spearman 0.875 for S₁),
and single-field families have many zeros (S₁: **160 prime zeros ≤ 10⁷**, count per decade still increasing; 42 % of
the zeros ≤ 3·10⁶ have L(1, χ_{−4p}) < 0.5 vs 3.8 % of controls). The varying-field family (★) assigns each divisor
exactly one level and is L-free at leading order. So the Siegel-type pointwise information the brief hoped for
appears only in single-field routes, and there it is a liability. Varying the field averages over quadratic twists. That
averaging is what makes (★) better than any single field, and it is also why no single class group can carry a proof.

| Screen | Ray layer N𝔞 ≡ −1 (mod 4C) | Class layer (any ring class group of K_C; genus; h; small-prime splitting) | Single-field family S₁ ⊂ N_II (ℚ(√−n) only) | Cross-field class data (§4) |
|---|---|---|---|---|
| **F1 odd squares** | = the event; fails by Lemma 2(c) (K = ℚ(√−t₀) ⊂ ℚ(ζ_M)) | **binds exactly** (Lemma 2: real character χ_{−4C} kills it); CERTIFIED: GV_C(m²) = 0 for all 99 odd squares 9 … 199², all C ≤ 100. Class *number* is T1-blind (Prop 5.1). | S₁(m²) = 0 (Lemma 2, t₀ = 1) | squares: every prime factor of 4Cm² + 1 already satisfies χ_{−4C} = 1, so no joint datum can produce a hit (Lemma 2 is a statement about the integers) |
| **F2 R₈ (C even)** | restatement | blind to C-parity: at the 12 R₈-zero primes GV_C holds at 16–38 even levels C ≤ 200, hits at none (CERTIFIED) | not applicable | no C-parity mechanism identified |
| **F3 composites** | restatement | genus condition satisfiable at every non-square n (Lemma 2(b), Cor 2.1); CERTIFIED: all 285 screen composites have GV_C at 9–38 levels C ≤ 100 | — | primality enters nowhere (Prop 4.2 is integer-blind) |
| **F4 known zeros** | restatement | CERTIFIED: at each of the 14 (★)-zero primes GV_C holds at 64–90 levels C ≤ 300 (least such C: 4, 7, 8, 12 or 13), hits at none | **fails massively**: 160 own prime zeros ≤ 10⁷ (25 in 𝔐, largest 8 841 673; in 𝔐 6 193 441) | n/a |

Verdict per column: ray layer = restatement; class layer passes F1 only; single-field families fail F4 outright;
cross-field data are information without a p-linked relation. **Not a HOT LEAD.**

## 1. Precise statements attacked

**(RC)** For every sufficiently large prime p ≡ 1 (mod 24) [(MS): p > 10¹⁷, p mod 840 ∈ 𝔐] there are C ≥ 1 and an ideal 𝔞
of ℤ[√(−Cp)] with 𝔞 | (1 + 2√(−Cp)) and N𝔞 ≡ −1 (mod 4C). By Lemma 1(ii), (RC) ⟺ R(p) ≥ 1. Open (Assessment: it is (MS)).

Questions of the brief: (Q1) exact correspondence (orders, non-split primes, units), analogues for the a = 1 line and for
4mn + 1 → Lemma 1. (Q2) Is N𝔞 ≡ −1 (4C) a ray-class / genus condition? → §3 (ray: yes, tautologically; genus: exactly its
real-character shadow; equal to it iff C ∈ {1, 2, 3, 6}). (Q3) Can the class group of discriminant −16Cp (size ≍ √(Cp),
Siegel), or small-prime splitting in K_C, force an 𝔞? → §§3–5 (no, in the scopes stated). (Q4) Where do T1 and primality
enter? → Lemma 2, Cor 2.1, §7.

## 2. What is prior (not redone) and what was open

Prior: WINDMILL_REDUCTION Prop 10.3 (for odd ℓ | t, ideal classes of ℤ[√−tp] see N𝔞 mod ℓ only mod squares; t | 24),
Remark 10.4 (ray classes mod t see the event, as a restatement; ring class groups do not), Computation 10.2 (the class map
is injective on the divisor hypercube); `BRAINSTORM/bsB_rayclass_norm_pullback.md` (linear character detectors of the
event are χ∘N); B2_ACROSS_FIELDS Lemma 4.1 = `BRAINSTORM/z31_duke_equidistribution.md` (shot family ⟺ ideal divisor of
1 + 2k√−p of norm ≡ −1 (4k); Heegner points; polylog vs √p); Z58_TERNARY Lemma D(d); Z58_TRYO Lemmas 8.1–8.2;
CLASS_FORCING Thm 2.1 and §4; Z59_CONV2 Lemma 1 and Prop 2.2; Z59_MSPLUS Thm 1 (L-free leading mean, dead moduli).
Z53_WILDCARD row 6 left open: joint constraints across the *varying* fields K_C, and class-group structure/size as a
*proof input*. This lane addresses exactly these two; §§3, 5.2 contain modest generalisations of prior per-field facts,
flagged as such.

## 3. Dictionary, T1 in field language, and the per-field class shadow

**Lemma 1 (one ray, three moduli; PROVED, elementary).** Let n ≥ 1 be odd, t₀ ≥ 1 squarefree, r ≥ 1.
(i) Every odd prime q | N(β_r) has q ∤ 2t₀nr and (−t₀n/q) = 1, so q splits in K_{t₀}, and q does not divide the conductor
of O. β_r is primitive in O (its 1-coordinate is 1), so exactly one of the two primes of O above q divides β_r, to
multiplicity v_q(N(β_r)). Hence 𝔞 ↦ N𝔞 is a bijection from the odd-norm ideal divisors of β_r (all invertible) onto the odd
positive divisors of N(β_r). Units play no role (the statement is about ideals).
(ii) (★) has a solution at level C ⟺ with C = t₀s² (t₀ squarefree) and r = 2s, some 𝔞 | β_r has N𝔞 ≡ −1 (mod t₀r²).
(iii) The a = 1 line at T (Z59_CONV2 Lemma 1(ii): Tn + 1 has a divisor ≡ −1 mod 4T) ⟺ with T = t₀r², some odd 𝔞 | β_r has
N𝔞 ≡ −1 (mod 4t₀r²). For r even this is implied by (ii) at C = T/4. So U_II adds exactly the odd r.
(iv) The full family at m (Z59_CONV2 Lemma 1(v): 4mn + 1 has a divisor ≡ −1 mod 4m/r(m), r(m) the largest c with c² | m)
⟺ with m = t₀s², r = 2s, some 𝔞 | β_r has N𝔞 ≡ −1 (mod 2t₀r). With t₀ = 1 and c = s this is the d = 1 slice
(Z59_CONV2 Lemma 1(v) with d = m/r(m)² = 1), i.e. S₁; all of it lives in ℚ(√−n).
*Proof.* (i) N(β_r) = 1 + t₀nr² ≡ 1 modulo every prime of t₀nr. For odd q | N(β_r), −t₀n ≡ (r⁻¹)² mod q is a non-zero
square, so q is unramified (q ∤ 2t₀n ⊇ disc) and split. The conductor of ℤ[√(−t₀n)] in O_K divides 2t₀n, so O is maximal at
q. If both primes above q divided β_r, then qO | β_r, impossible since β_r ∉ qO. Hence v_𝔮(β_r) = v_q(N β_r) for the unique
𝔮 | β_r above q. (ii) Z59_CONV2 Lemma 1(i) with T = 4C: (★) at level C ⟺ 4Cn + 1 has a divisor ≡ −1 (mod 4C). Write C = t₀s²
uniquely; then 4Cn + 1 = 1 + t₀n(2s)² = N(β_{2s}) and 4C = t₀(2s)². Apply (i) (N(β_{2s}) is odd). (iii) Tn + 1 = N(β_r), 4T =
4t₀r². If r is even, 4 | T and a divisor ≡ −1 (mod 4T) is ≡ −1 (mod T) = mod 4(T/4). (iv) m = t₀s² with t₀ squarefree gives
r(m) = s and 4m/r(m) = 4t₀s = 2t₀r, 4mn + 1 = N(β_{2s}). ∎
*Check.* `scripts/z60_rayclass_fam.c` computes R, its square-level slices and S₁ by independent enumerations. They agree with
brute force for all n ≡ 1 (4), 5 ≤ n ≤ 401 (0 mismatches; §6).

**Lemma 2 (T1 = the square-class field lies in the cyclotomic field of the modulus; PROVED).** In Lemma 1 write
n = s·m² with s squarefree. Let M be the modulus of the line (t₀r², 4t₀r² or 2t₀r). Let K' = ℚ(√(−t₀s)) and let χ be the
Kronecker character of disc(K') (real, primitive, χ(−1) = −1).
(a) If |disc K'| divides M, then no odd divisor of N(β_r) is ≡ −1 (mod M).
(b) If n = p is prime and p ∤ t₀r, then p | disc K' and p ∤ M, so (a) does not apply. All levels in the (MS) range
(C ≤ (p+1)/3) satisfy p ∤ t₀r.
(c) If n = m² (s = 1), the hypothesis of (a) holds at every level of all three lines, since |disc ℚ(√−t₀)| divides 4t₀ and
4t₀ | M in each case (r even in (ii), (iv); M = 4t₀r² in (iii)). This is T1 for (★), U_II and N_II at once.
*Proof.* (a) For an odd prime q | N(β_r): q ∤ t₀s, and −t₀s(mr)² ≡ 1 (mod q), so χ(q) = (−t₀s/q) = 1. Hence χ(d) = 1 for every
odd divisor d. If |disc K'| | M, χ is a character mod M, and χ(M − 1) = χ(−1) = −1. (b) t₀p is squarefree when p ∤ t₀, so
p | disc K'. Moreover p ∤ M iff p ∤ t₀r (M ∈ {t₀r², 4t₀r², 2t₀r}). In the (MS) d-form, d = 4uC − 1 ≤ (4p+1)/3 forces
C ≤ (p+1)/3 < p, so p ∤ C = t₀(r/2)². (c) disc ℚ(√−t₀) ∈ {−t₀, −4t₀}. ∎
Lemma 2(a) is the field form of Z58_TERNARY Lemma D(d) and of the L_T-profile remark of Z59_CONV2 (F1 row). The general-s
version gives:

**Corollary 2.1 (dead levels at n = s·m²; PROVED).** For odd non-square n = s·m² (s squarefree), (★) has no solution at any
level C with s | C. Conversely, if s ∤ C then |disc K'| ∤ 4C, so Lemma 2(a) does not obstruct that level.
*Proof.* With C = t₀σ², s | C means every prime of s divides t₀ or σ. Put g = gcd(t₀, s). Then sqf(t₀s) = (t₀/g)(s/g), and
s/g consists of primes dividing σ and not t₀. So (t₀/g)(s/g) | t₀σ² = C, hence |disc K'| | 4·sqf(t₀s) | 4C = M. Apply Lemma 2(a).
Conversely, a prime ℓ | s with ℓ ∤ C has ℓ ∤ t₀, so ℓ | sqf(t₀s) | disc K', while ℓ ∤ 4C. ∎ CERTIFIED check: among the 2 728
non-squarefree non-square n ≡ 1 (4) ≤ 60 000, no hit lies at a level C ≡ 0 (mod s) (`checks.txt`). *Scope:* for primes and for
squarefree composites, Cor 2.1 kills only levels C ≥ n, which lie outside the (MS) range. So it does **not** explain F3 in
general. (Prior analogues: Z58_WILDCARD Lemma 4.3, "twisted T1" for the numerator ladder; Z59_MSPLUS dead moduli concern
d, not C. Cor 2.1 is not claimed new in substance.)

**Proposition 3.1 (per-field class shadow, all orders and moduli; PROVED, standard CFT; generalises WINDMILL_REDUCTION
Prop 10.3 / Remark 10.4).** Let K be imaginary quadratic, O ⊂ O_K an order with ring class field L_O, and M ≥ 1. Let
G_M ⊂ (ℤ/M)^× be the group of residues N𝔞 mod M of ideals 𝔞 of O_K prime to M·f(O) (G_M ≅ Gal(K(ζ_M)/K)). There is a
subgroup S ⊂ G_M such that:
(a) for every ring class κ ∈ Cl(O), the residues N𝔞 mod M of the ideals 𝔞 ∈ κ (prime to Mf) form exactly one coset of S, and
every element of that coset is N𝔭 mod M for infinitely many degree-1 primes 𝔭 ∈ κ (positive Dirichlet density);
(b) G_M/S is an elementary abelian 2-group; in particular S ⊇ G_M².
Hence the indicator [N𝔞 ≡ −1 (mod M)] is a class function on Cl(O) only if S = 1, which forces G_M to have exponent ≤ 2. For
K = K_C with p ∤ 4C (p prime, the level C of (★)), G_{4C} = (ℤ/4C)^×, and the event is class-determined iff 4C | 24, i.e.
C ∈ {1, 2, 3, 6}. For every other C, every ring class of every order of K_C that contains an ideal with norm ≡ −1 (mod 4C)
also contains infinitely many prime ideals with norm ≢ −1 (mod 4C).
*Proof.* L_O/ℚ is Galois with Gal(L_O/ℚ) ≅ Cl(O) ⋊ ⟨τ⟩, τ (complex conjugation) acting by inversion (Cox, *Primes of the
form x² + ny²*, Lemma 9.3; source-verified via three citing texts, §8). Since τxτ⁻¹x⁻¹ = x⁻², the commutator subgroup contains
Cl(O)², so the maximal abelian subextension of L_O/ℚ has elementary 2-abelian Galois group. F := L_O ∩ K(ζ_M) is Galois over ℚ
(an intersection of Galois extensions) and abelian over ℚ (a subfield of K(ζ_M), which is abelian over ℚ), so Gal(F/K) is
elementary 2-abelian. Gal(L_O(ζ_M)/K) is the fibre product Gal(L_O/K) ×_{Gal(F/K)} Gal(K(ζ_M)/K). The Artin symbol of 𝔞
in Gal(L_O/K) ≅ Cl(O) is κ(𝔞), and in Gal(K(ζ_M)/K) ↪ (ℤ/M)^× it is N𝔞 mod M. Both maps are homomorphisms on ideals prime
to Mf. So (κ(𝔞), N𝔞 mod M) lies in the fibre product: given κ, N𝔞 mod M lies in the coset of S := Gal(K(ζ_M)/F) over the image
of κ in Gal(F/K). Chebotarev in L_O(ζ_M)/K gives (a), and (b) is G_M/S ≅ Gal(F/K). For K_C: p ramifies in K_C and not in
ℚ(ζ_{4C}), so K_C ∩ ℚ(ζ_{4C}) = ℚ and G_{4C} = (ℤ/4C)^×. Finally, (ℤ/M)^× has exponent ≤ 2 iff M | 24. ∎
*Reading.* The *visible layer* of the level-C event for any single ring class group is therefore at most
GV_C(n) := "some divisor d | 4Cn + 1 has χ(d) = χ(−1) for every real character χ mod 4C". It is a necessary condition for a
hit, and it equals the event iff C ∈ {1, 2, 3, 6}. (Splitting of small primes in K_C is Legendre data of p, a
special case.) **Computation (CERTIFIED, `scripts/z60_rayclass_genus.py`):** GV_C(m²) = 0 for all 99 odd squares m² with
3 ≤ m ≤ 199 and all C ≤ 100 (T1, as Lemma 2 predicts). At the 14 (★)-zero primes, GV_C holds at 82, 72, 70, 67, 73, 64, 70,
81, 74, 90, 85, 80, 82, 77 of the levels C ≤ 300 (least: 4, 4, 4, 4, 4, 8, 13, 8, 4, 4, 12, 7, 13, 8), and the event at none.
At the 285 screen composites GV_C holds at 9–38 levels C ≤ 100, at the 12 R₈-zero primes at 16–38 even levels C ≤ 200; the
event holds at none of these levels (consistent with the screens). So no argument that only certifies the class-visible
layer, at any level and in any order, can reach the event: it would "prove" (★) at all 14 zeros.

## 4. Across fields: more information, no more relations

**Proposition 4.1 (joint class data can see beyond the quadratic shadow; PROVED group-theoretically, arithmetic instance
CERTIFIED).** Let D = D₄ = ⟨r, s⟩, π: D → D^{ab} ≅ (ℤ/2)², and let ψ be the automorphism of D^{ab} swapping r̄ and s̄. Then
G := {(x, y) ∈ D × D : π(x) = ψ(π(y))} has order 16, [G, G] = ⟨(r², r²)⟩, and (r, s) ∈ G has order 4 in G^{ab}
(`scripts/z60_rayclass_checks.py`: |G| = 16, |[G,G]| = 2, (r,s)² ∉ [G,G]). Arithmetic meaning: let K₁ ≠ K₂ be imaginary
quadratic and L₁ ⊃ K₁, L₂ ⊃ K₂ dihedral-of-order-8 fields that are ring-class-type (Gal(L_i/K_i) cyclic of order 4,
complex conjugation acting by inversion) with L₁ ∩ L₂ = B := K₁K₂ the common maximal abelian subfield. Restricting
to B, K₁ is cut out in L₁ by "rotation" and in L₂ by a "reflection class", and vice versa. So Gal(L₁L₂/ℚ) is exactly
this twisted G, and L₁L₂ contains a **cyclic quartic** field over ℚ. That field is invisible to each L_i separately
(Prop 3.1).
*Instance.* K₁ = ℚ(√−17), Cl(−68) ≅ ℤ/4, L₁ its Hilbert class field (genus field ℚ(i, √17)); K₂ = ℚ(i), O = ℤ[17i],
Cl(−1156) ≅ ℤ/8, L₂ the D₄-subfield of its ring class field (genus field ℚ(i, √17)). L₁ ≠ L₂ (their split sets differ),
so L₁ ∩ L₂ = B. Data (`scripts/z60_rayclass_burde.py`, CERTIFIED for q ≤ 2·10⁶): the 9 259 primes q that split
completely in L₁ and L₂ (q = x² + 17y² and q represented by [1,0,289] or [2,2,145]) all have q mod 17 ∈ {1, 4, 13, 16} =
the quartic residues. The 9 303 primes that split completely in L₁ but not L₂ all have q mod 17 ∈ {2, 8, 9, 15}. So
the pair of ring classes determines the quartic residue character of q mod 17. This is classical in spirit (rational
quartic reciprocity: Burde 1969; Lemmermeyer, Acta Arith. 67 (1994) eq. (7), "(p/q)₄(q/p)₄ = ((ac − bd)/q)"; source
check §8). It is quoted here only for its consequence: **WINDMILL_REDUCTION Prop 10.3 and B2_ACROSS_FIELDS "F6"
("class-group / genus data see only the quadratic shadow") are per-field statements.** For joint data across fields
they fail, so the Z53_WILDCARD row-6 escape is real at the level of information. (In (★) the relevant pairs would be
K_C = ℚ(√(−ℓp)) and an order of conductor ℓ in ℚ(√−p). The genus fields ℚ(√ℓ, √−p, …) are shared, which is the
configuration of Prop 4.1. That such pairs give quartic characters mod ℓ is the Prop 4.1 mechanism; it was not computed
for specific p.)

**Proposition 4.2 (total-product principle; PROVED part + Assessment).** Let K = K_{t₀}, β = β_r, and (β) = ∏ 𝔮_i^{e_i}. For
every finite abelian extension E/K with conductor 𝔣 prime to (β), Artin reciprocity gives the single relation
∏_i Art_{E/K}(𝔮_i)^{e_i} = Art_{E/K}((β)), which depends only on β mod 𝔣. For E = K(ζ_M) it reads ∏ N𝔮_i^{e_i} ≡ N(β) = 1 + t₀nr²
(mod M), a function of n mod M. For non-abelian Galois E/K, Frobenius classes do not compose, and no relation among the
Frob_E(𝔮_i) follows from 𝔮_i | β beyond those of the abelian subextensions. (PROVED: the displayed relation. Assessment:
"no other relation". This is not a theorem about every proof; it is the observation that CFT supplies only
multiplicative, i.e. total-product, constraints.) The event asks for a **sub**-product with norm ≡ −1 (mod M). A relation
among total products constrains sub-products only through zero-sum/Davenport combinatorics (CLASS_FORCING §4). Those need
more prime factors than 4Cp + 1 has in the hard cases. So Prop 4.1's extra information is about *individual* prime factors,
whose Frobenius data are not linked to p by any relation, while Prop 4.2's p-linked relations are total products. The
cross-field route therefore lands on B2 again: one needs the residues of the actual prime factors of the specific integer.

## 5. Where the class number enters

**Proposition 5.1 (class-number size is T1-blind; PROVED).** For odd m ≥ 3 and C ≥ 1 let O_m = ℤ[2m√−C], the order of
discriminant −16Cm² containing 1 + 2m√−C (the square analogue of ℤ[2√(−Cp)], discriminant −16Cp). Then
h(O_m) ≥ f·φ(f)/(3f) ≥ c·m/log log m with f ≥ 2m its conductor. Hence any criterion "h(−16Cn) ≥ g(n) ⟹ (★) at level C" with
g(n) ≤ c√n/log log n is false at every odd square. Siegel's bound h(−16Cp) ≫_ε (Cp)^{1/2−ε} is weaker than what squares
satisfy unconditionally.
*Proof.* Cox Thm 7.24: h(O) = h(O_K)·f/[O_K^×: O^×]·∏_{ℓ|f}(1 − (d_K/ℓ)/ℓ) ≥ f·∏_{ℓ|f}(1 − 1/ℓ)/3 = φ(f)/3, and
φ(f) ≫ f/log log f. −16Cm² = f²d_K with |d_K| ≤ 4C gives f ≥ 2m. ∎ (Thm 7.24 source-checked via citing texts, and
numerically against PARI `qfbclassno` for 64 pairs (C, m), C ≤ 11, m ≤ 1001: 0 mismatches.)

**Proposition 5.2 (parameter density: one field vs varying fields; PROVED, elementary).** Let p be prime and f odd with
gcd(f, t₀p) = 1.
(a) Varying fields: #{C mod f : f | 4Cp + 1} = 1.
(b) One field (fixed t₀): #{s mod f : f | 1 + 4t₀ps²} = ρ_f := #{x mod f : x² ≡ −t₀p}, and
Σ_{f odd, (f, t₀p)=1} ρ_f f^{−σ} = ∏_{ℓ ∤ 2t₀p} (1 + χ(ℓ)ℓ^{−σ})/(1 − ℓ^{−σ}) = ζ(σ)L(σ, χ)/ζ(2σ) × (Euler factors at ℓ | 2t₀p),
χ = χ_{−4t₀p}.
So along a single-field ray the density of divisor-candidates is governed by L(1, χ_{−4t₀p}) = π·h/√(t₀p) (up to the
2-adic normalisation). Along the varying-field family each f meets exactly one level class. Since C ↦ (t₀, s), C = t₀s²,
is a bijection, (a) is the sum over t₀ of the single-field counts (b): the varying-field count averages the twisted
densities ρ_f(−t₀p) over the twists t₀.
*Proof.* (a) 4p is invertible mod f. (b) 1 + 4t₀ps² ≡ 0 ⟺ (2t₀ps)² ≡ −t₀p (multiply by t₀p, a unit), a bijection s ↔ x. The
Euler factor is 1 + (1 + χ(ℓ))Σ_{k≥1} ℓ^{−kσ} (Hensel, ℓ odd, ℓ ∤ t₀p) = (1 + χ(ℓ)ℓ^{−σ})/(1 − ℓ^{−σ}) =
(1 − ℓ^{−2σ})/((1 − ℓ^{−σ})(1 − χ(ℓ)ℓ^{−σ})). ∎
*Assessment (heuristic, not a theorem).* The expected number of hits of a fixed-t₀ ray family at p is ≍ L(1, χ_{−4t₀p})·(log p)^k
(k = 1 for the (★)-square slices, k = 2 for S₁). For (★) it is L-free at leading order (consistent with Z59_MSPLUS Thm 1).
Siegel gives L ≫_ε p^{−ε} only; a hypothetical exceptional character χ_{−4p} would make single-field families at p very
poor, and (★) would not care to first order.

**EVIDENCE (`counts_1e6_1.2e6.txt`, `lcorr_1e6_1.2e6.txt`; 7 254 primes p ≡ 1 (4) in [10⁶, 1.2·10⁶]).**
Spearman correlation with L(1, χ_{−4p}) and log-elasticity (slope of log X on log L, over X > 0):

| count X | mean | Spearman(X, L) | elasticity |
|---|---|---|---|
| S₁ | 42.97 | +0.875 | 1.23 |
| (★)-hits with u a square (ideal divisors of s + √−p) | 6.65 | +0.729 | 1.10 |
| (★)-hits with C a square (ideal divisors of 1 + 2s√−p) | 7.12 | +0.723 | 1.07 |
| all of R | 32.26 | +0.426 | 0.32 |
| R minus the two square-level slices | 18.49 | **−0.354** | — |

The single-field slices scale like L¹, as Prop 5.2 predicts. The rest of (★) (fields K_{t₀}, t₀ > 1) is *anti*-correlated
with L(1, χ_{−4p}). That is consistent with the twist-averaging reading, though not derived. Control mean L = 1.237.
At the 133 S₁-zeros ≤ 3·10⁶, 42.1 % have L < 0.5 (controls 3.8 %). At the 14 (★)-zeros L ∈ [0.52, 1.24], mean 0.84; at
the 38 𝔊*-zeros mean 0.82; at the 12 R₈-zeros mean 1.05; none of these is below 0.5. (★)-zeros are mildly low-L. This is
consistent with 9 of the 14 lying in 𝔐, where (ℓ/p) = 1 for ℓ ≤ 7 and the Euler factors at 3, 5, 7 are those of
ℚ(i) (product ≈ 0.82). This is a reading, not a fit.

## 6. Data and exact commands (all `ulimit -v 4000000`, `timeout ≤ 1800`)

* `gcc -O2 -o fam scripts/z60_rayclass_fam.c -lm`
  * `./fam range 1000000 1200000 > data/z60/rayclass/counts_1e6_1.2e6.txt` (columns p R Sq_u Sq_C S₁).
  * `./fam s1zeros 5 10000000` gives `s1_prime_zeros_le1e7.txt`: **160 primes p ≡ 1 (4) ≤ 10⁷ with S₁(p) = 0**, 25 of them in
    𝔐 and 105 with p ≡ 1 (24). By range: <10³: 8; 10³–10⁴: 14; 10⁴–10⁵: 23; 10⁵–10⁶: 54; 10⁶–10⁷: 61. The count per decade
    is still increasing. The first ones are 13, 37, 97 (agreeing with the known shot-family failures, DISCOVERIES (J)36).
    CERTIFIED by one engine, validated by brute force for n ≤ 401. The [8 841 674, 10⁷] tail was rerun separately (no zeros).
* `uv run --with cypari2 --with numpy --with scipy python scripts/z60_rayclass_lcorr.py <counts> <zeros>` produces the §5 table.
* `uv run --with cypari2 python scripts/z60_rayclass_genus.py <file> CMAX [even]` produces `genus_star_zeros_C300.txt`,
  `genus_composite_zeros_C100.txt`, `genus_r8_zeros_Ceven200.txt`, `genus_odd_squares_C100.txt` (columns: n, #levels with
  GV, #levels with hit, least GV-but-no-hit level).
* `python3 scripts/z60_rayclass_checks.py` checks Cor 2.1 and the group lemma (`checks.txt`).
* `python3 scripts/z60_rayclass_burde.py` gives the Prop 4.1 instance (output reproduced in §4).

## 7. Answers to the brief, screens, what survives

* **(Q1)** Lemma 1: exact for all orders (odd-norm divisors are prime to the conductor, so they are invertible), with no
  non-split primes (every odd q | N(β) splits) and no unit issue. The a = 1 line is the odd-r part of the same ray. The full
  family is the same ray with the modulus relaxed from t₀r² to 2t₀r (Z59_CONV2's "tie relaxes to ≥ 2√(4m)").
* **(Q2)** Ray-class: yes, tautologically (N is a homomorphism on Cl_{(4C)}(K_C); WINDMILL_REDUCTION Remark 10.4). Genus
  (any ring class group, any order): exactly the real-character shadow GV_C (Prop 3.1), which equals the event iff
  C ∈ {1, 2, 3, 6}.
* **(Q3)** No, in the following scopes. Per field, class data are blind beyond GV_C, and GV_C holds at the known zeros
  (Prop 3.1 + CERTIFIED). Class-number size is T1-blind (Prop 5.1). The pointwise class number enters only single-field
  ray families, multiplicatively, and those fail F4 (S₁: 160 prime zeros ≤ 10⁷). Small-prime splitting is Legendre data
  (CLASS_FORCING Thm 2.1). Across fields, more residue information is available (Prop 4.1), but no p-linked relation
  beyond total products exists (Prop 4.2, Assessment beyond the displayed relation).
* **(Q4)** T1: Lemma 2(c), the field ℚ(√−t₀) ⊂ ℚ(ζ_M). It is a genus (real-character) phenomenon. Class numbers,
  L-values and Heegner-point counts do not degenerate at squares. Primality: in this picture it enters only as "the
  square class s = n is large, so no level in range is dead" (Lemma 2(b), Cor 2.1). Every squarefree composite shares
  this. So the field picture does not see F3, and no step here uses primality beyond non-squareness at small levels.
* **FRONTIER §4 hard screens** (for the best idea of the lane, the cross-field information of §4): T1 squares, passes
  (vacuously: Lemma 2 kills the integers); 8/131 (C-parity), no mechanism; tied modulus, not resolved (Prop 4.2 lands
  on it); fixed p, fails (no pointwise input beyond total products).
* **Survives (escape hatches, none a lead).** (E1) A *non-CFT* relation tying individual prime factors of 4Cp + 1
  across levels C (shared primes q | C − C′ are the only arithmetic link; Prop 4.2's scope excludes only CFT relations).
  (E2) Twist-averaged statements: the varying-field family is Σ_{t₀} of single-field families (Prop 5.2). A pointwise
  lower bound for a *twist average* of L-weighted counts is conceivable (twist averages of L(1, χ·χ_{t₀}) are
  well-behaved). But the obstacle is the divisor-in-class condition, not the L-weight. (E3) Prop 4.1-type cross-field
  characters as a sieve input (they are Frobenius data of q, i.e. congruence data; Assessment: this is B1/B2 again).

**Proposed FRONTIER §7 text (do not edit FRONTIER).** "*RAYCLASS (z60).* The ray-class picture is a restatement:
(★), the a = 1 line and the full Type II family are divisor events along one ray 1 + r√(−t₀n) of ℚ(√(−t₀n)), with
moduli t₀r², 4t₀r², 2t₀r. T1 ⟺ ℚ(√(−t₀s)) ⊂ ℚ(ζ_M) for the square class s of n (dead levels s | C). Per field, ring
class groups of any order see only the real-character shadow GV_C, which holds at the 14 (★)-zeros at 64–90 levels
C ≤ 300 (CERTIFIED). Across fields, joint class data can see quartic characters (ℚ(√−17) & ℤ[17i] example), but CFT
imposes only total-product relations on the divisors. Class-number size is T1-blind. In single-field families the
expected count ∝ L(1, χ_{−4t₀p}) (Spearman 0.875 for S₁), and S₁ (Type II d = 1) has 160 prime zeros ≤ 10⁷,
still increasing per decade. Varying the field is what removes the L-dependence. Open: a non-CFT relation among the
individual prime factors of 4Cp + 1 across levels."

## 8. Literature verification (research subagent; secondary sources, books not directly accessible)

* Cox, *Primes of the form x² + ny²*, **Thm 7.24** (class number of orders): statement quoted verbatim in Daniels &
  Lozano-Robledo (Thm 2.2, citing "[Cox89] Theorem 7.24"); same number in the 2nd and 3rd editions per citing texts.
  Numerically re-verified (§5). Matches.
* Cox **Lemma 9.3** (ring class field generalized dihedral over ℚ, τ acts by inversion): paraphrased identically in Daniels &
  Lozano-Robledo, arXiv:1403.2264, and Gil-Muñoz's thesis. Matches. (Lemma 5.28 only gives "Galois over ℚ" for the Hilbert class
  field.)
* Burde's rational quartic reciprocity: Lemmermeyer, "Rational quartic reciprocity", Acta Arith. 67 (1994) 387–390, eq. (7):
  for p, q ≡ 1 (4), p = a² + b², q = c² + d², 2 | b, 2 | d, (p/q) = 1: (p/q)₄(q/p)₄ = ((ac − bd)/q), citing Burde, J. Reine
  Angew. Math. 235 (1969). Used only as context for Prop 4.1, whose instance is checked directly.

## 9. Review log

(To be filled after the hostile internal review.)
