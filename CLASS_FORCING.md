# CLASS_FORCING — can higher reciprocity / governing fields force the CLASS of a divisor? (task O263, route (b))

Status labels as in DISCOVERIES.md. **ES is not solved.** Memos: BRAINSTORM/z33_*.md. Scripts: scripts/z33_*.

## 0. Iteration log
* v0 (construction attempt 1). "Reciprocity forces χ(N); upgrade to the class of N, then to a divisor." Screen: the class
  of N mod t is ALREADY known exactly (it is p mod t), so the "forced quotient" of the total product is all of G; the gap is
  entirely in the factorisation (§2, Thm 2.1). Modification: look for forcing of INDIVIDUAL factors (§3).
* v1 (attempt 2). "Forced-factor lemma + Davenport." The forced multiset of a single N is (small primes, one opaque
  element) — a prime N is always compatible; zero-sum needs ≥ exp(G)/2 escaping factors (§4). Modification: make the
  forced small primes do the work by choosing d (CRT) — this is exactly the ET Type II congruence family d | (w+1)/4 (B1, §3.3).
* v2 (attempt 3). "Non-abelian Frobenius data of p (cubic/quartic residue symbols, governing fields) is NOT congruence
  data — maybe it escapes B1." Result: it constrains the factors only through Kummer Frobenius classes whose shadow in the
  ray class group mod t is quadratic (§5), and under a Hypothesis-H-with-Chebotarev it adds nothing at all (§6).
* v3 numerics (§7).

## 1. Setting: the four lines and the event

For a prime p ≡ 1 (4) (p ≡ 3 (4) is trivial) the B2 divisor event has the form
  E(N, t):  some divisor w | N has w ≡ −1 (mod t),  equivalently  −1 ∈ Σ(N) := {subset products of the prime factors of N, with multiplicity} ⊂ G := (ℤ/t)^×,
or, in the signed e-slice form (LONGSHOT_PIGEONHOLE Lemma 1.1), −1 ∈ Σ^±_e(N) := {ab⁻¹ mod e : ab | N}. The lines used:
| line | integer N | modulus t | class of N in G |
|---|---|---|---|
| b = 1 (López Type A; B1_LINE) | p + 4d | 4d | p mod 4d |
| c-line (dual coordinate) | cp + 1 | 4c | cp + 1 mod 4c |
| Type II e-slice (signed) | (p + e)/4 | e | p/4 mod e |
| Type I e-slice (signed) | (pe + 1)/4 | e | 4⁻¹ mod e |
In every line the **class of N in G is a function of p mod t** (column 4). This trivial remark is the root of §2.

## 2. The forced quotient of the total product is all of G; reciprocity only re-expresses it

**Theorem 2.1 (what reciprocity can say about the total product; PROVED).** Fix a line of §1 and a modulus t, G = (ℤ/t)^×.
(a) *(Congruence.)* For every character ψ of G, ψ(N) is a function of p mod t. So the "forced quotient" of the total product
is G itself: H_forced = {1}, and no reciprocity law (quadratic, cubic, quartic, Eisenstein, Artin for ray class fields mod t)
can add information about [N] ∈ G; such laws can only re-express ψ(p) through other data of p.
(b) *(What the residue symbols of p see.)* Let Ω/ℚ be any finite Galois extension (e.g. Ω = ℚ(ζ_n, a₁^{1/n}, …, a_k^{1/n})
for the residue symbols (a_i/p)_n; a Rédei field for a Rédei symbol [a, b, p]; a Smith/Koymans–Pagano governing field).
For primes p unramified in Ωℚ(ζ_t), the pair (Frob_p|Ω, p mod t) is equidistributed in
Gal(Ωℚ(ζ_t)/ℚ) = Gal(Ω/ℚ) ×_{Gal(F/ℚ)} G, F := Ω ∩ ℚ(ζ_t) (Chebotarev in the compositum). Hence Frob_p|Ω determines exactly the
image of [p] in G/G_F, G_F := Gal(ℚ(ζ_t)/F), and is independent of [p] beyond it. Since F ⊂ Ω^{ab}, only the abelian part of Ω
matters.
(c) *(Computation of F for the standard data.)* (i) n = ℓ an odd prime, a₁, …, a_k multiplicatively independent mod ℓ-th powers:
Ω^{ab} = ℚ(ζ_ℓ), so the ℓ-th power residue symbols (a_i/p)_ℓ carry no information on [p] mod t beyond p mod ℓ (if ℓ | t).
(ii) n = 4 (quartic symbols), Ω = ℚ(i, a^{1/4}), a ≠ ±□ (this excludes a = −4b⁴ = −(2b²)², the Sophie-Germain case of the
Remark, where Ω = ℚ(i) is abelian; (R272 repair) hypothesis made explicit) : Ω^{ab} = ℚ(i, √a); information = (a/p)
and p mod 4. (iii) Rédei fields (dihedral of order 8 over ℚ, containing the biquadratic ℚ(√a, √b) — (R272 repair) biquadratic is a
hypothesis; degenerate cases are cyclic quartic): Ω^{ab} = ℚ(√a, √b); information = two
Legendre symbols.
(iv) *(R272 repair: the earlier claim that governing fields have multiquadratic Ω^{ab} is withdrawn.)* A governing field is not
canonical: any finite Galois Ω′ ⊇ Ω (e.g. Ωℚ(ζ₁₆), Ωℚ(ζ₅)) governs the same invariant, and then F sees [p] mod 16 resp. mod 5 in
full (cyclic quotients ⊄ G/G²); even minimal 2-power governing fields may have cyclic-quartic or ℚ(ζ₁₆)-type abelian parts.
For the specific fields of Smith / Koymans–Pagano the abelian part was NOT checked (no sources available).
So, **(R272 repair; replaces the earlier bold summary) any Frobenius datum of p sees [N] ∈ G only through a quotient of p mod t
(congruence data: the image of [p] in G/G_F), and is equidistributed independently of [p] beyond that quotient. For the data
(i)–(iii) the quotient is of G/G² × (p mod gcd(n, t)) type — the χ-shadow of Prop 10.3 (WINDMILL_REDUCTION) and Lemma 2.2(b)
(SYNTHESIS_SPARKS8) plus a cyclotomic piece.** In short: reciprocity data of p = congruence data of p plus an independent
non-abelian part. Since [N] is itself a function of p mod t ((a)), nothing downstream depends on how large F is.
*Proof.* (a) (R272 repair) N ≡ p (mod 4d) (b = 1 line), N = cp + 1 (c-line; for c odd N is even and only odd divisors can be
≡ −1 (mod 4c), so the event concerns the odd part of N), 4N ≡ p (mod e) and 4N ≡ 1 (mod e) for the e-slices (e ≡ 3 (4) odd). (b) Ω and ℚ(ζ_t) are Galois with intersection F, so
Gal(Ωℚ(ζ_t)/ℚ) is the fibre product; Chebotarev gives equidistribution of Frob in it; the fibre over σ ∈ Gal(Ω/ℚ) is a
coset of G_F, so σ fixes exactly [p]·G_F. F ⊂ ℚ(ζ_t) is abelian, hence F ⊂ Ω^{ab}. (c)(i) Gal(Ω/ℚ) ≅ (ℤ/ℓ)^k ⋊ (ℤ/ℓ)^× with
u acting by multiplication; for u ≢ 1 the commutators (u − 1)v exhaust (ℤ/ℓ)^k, so the abelianisation is (ℤ/ℓ)^× and
Ω^{ab} = ℚ(ζ_ℓ) (same argument as BALANCED_LATTICE Lemma 2.5). (ii) Gal(ℚ(i, a^{1/4})/ℚ) ≅ D₄ under the stated condition, with
commutator subgroup of order 2, so Ω^{ab} is the biquadratic ℚ(i, √a). (iii) D₄ again; its abelianisation is (ℤ/2)², the
biquadratic subfield. ∎
*Remark (an exception worth recording).* For a = −4b⁴, (−4b⁴)^{1/4} = (1 + i)b ∈ ℚ(i): x⁴ + 4b⁴ splits (Sophie Germain).
This is the single quartic Kummer datum that is abelian, and it is precisely the algebraic factorisation behind the thin
families (J)74/(J)75/(J)80 (4X⁴ + 1 = (2X² + 2X + 1)(2X² − 2X + 1)). It acts on the INTEGER (forcing a factorisation of
p + 4d when p itself is a 4th-power-type value), not on residue symbols of a generic prime p.

**Table 2.2 (b = 1 line, d ≤ 30; `scripts/z33_forced_quotient_table.py`, `logs/z33_forced_quotient_table.txt`).** G = (ℤ/4d)^×.
"quad" = |G/G²| = number of quadratic characters = what Legendre/Rédei data of p can see (Thm 2.1(c)); the rest of [p] is
seen only by p mod 4d itself. Last column: classes x ≡ 1 (4) (the possible [p]) with −1 ∈ ⟨x⟩: always 0, since ⟨x⟩ ⊂ ker χ₋₄.
| d | |G| | primary decomposition | exp | quad | possible [p] | −1 ∈ ⟨[p]⟩ |
|---|---|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 2 | 1 | 0 |
| 2 | 4 | 2·2 | 2 | 4 | 2 | 0 |
| 3 | 4 | 2·2 | 2 | 4 | 2 | 0 |
| 4 | 8 | 2·4 | 4 | 4 | 4 | 0 |
| 5 | 8 | 2·4 | 4 | 4 | 4 | 0 |
| 6 | 8 | 2·2·2 | 2 | 8 | 4 | 0 |
| 7 | 12 | 2·2·3 | 6 | 4 | 6 | 0 |
| 8 | 16 | 2·8 | 8 | 4 | 8 | 0 |
| 9 | 12 | 2·2·3 | 6 | 4 | 6 | 0 |
| 10 | 16 | 2·2·4 | 4 | 8 | 8 | 0 |
| 11 | 20 | 2·2·5 | 10 | 4 | 10 | 0 |
| 12 | 16 | 2·2·4 | 4 | 8 | 8 | 0 |
| 13 | 24 | 2·3·4 | 12 | 4 | 12 | 0 |
| 14 | 24 | 2·2·2·3 | 6 | 8 | 12 | 0 |
| 15 | 16 | 2·2·4 | 4 | 8 | 8 | 0 |
| 16 | 32 | 2·16 | 16 | 4 | 16 | 0 |
| 17 | 32 | 2·16 | 16 | 4 | 16 | 0 |
| 18 | 24 | 2·2·2·3 | 6 | 8 | 12 | 0 |
| 19 | 36 | 2·2·9 | 18 | 4 | 18 | 0 |
| 20 | 32 | 2·4·4 | 4 | 8 | 16 | 0 |
| 21 | 24 | 2·2·2·3 | 6 | 8 | 12 | 0 |
| 22 | 40 | 2·2·2·5 | 10 | 8 | 20 | 0 |
| 23 | 44 | 2·2·11 | 22 | 4 | 22 | 0 |
| 24 | 32 | 2·2·8 | 8 | 8 | 16 | 0 |
| 25 | 40 | 2·4·5 | 20 | 4 | 20 | 0 |
| 26 | 48 | 2·2·3·4 | 12 | 8 | 24 | 0 |
| 27 | 36 | 2·2·9 | 18 | 4 | 18 | 0 |
| 28 | 48 | 2·2·3·4 | 12 | 8 | 24 | 0 |
| 29 | 56 | 2·4·7 | 28 | 4 | 28 | 0 |
| 30 | 32 | 2·2·2·4 | 4 | 16 | 16 | 0 |
*Reading.* Exponent 2 (where subset products = generated subgroup, multiplicities irrelevant) only for d ∈ {1, 2, 3, 6}
(4d | 24, Prop 10.3's "t | 24"). For every other d, the quadratic shadow is a proper quotient (|G/G²| < |G|) and even the
generated subgroup is not the subset-product set. **Criterion from total-product data alone: E(p + 4d, 4d) is forced iff
[p] = −1 in G, which never happens for p ≡ 1 (4)** (it would need p ≡ 3 (4)); this is z29(b) in its strongest form: knowing
the FULL class (not just characters) changes nothing.

## 3. Individual factors: the strongest forced-factor lemma and the exact forced criterion

Write N = s·L with (R272 repair) s := ∏_{q ≤ B} q^{min(v_q(N), e_q)} — exactly what p mod M_B, M_B := ∏_{q ≤ B} q^{e_q}, reveals —
and L := N/s the opaque cofactor (class g_L := [N]·[s]⁻¹ ∈ G known, factorisation unknown; L absorbs any excess q^{v_q(N) − e_q},
and "L prime" stays an admissible abstract completion since the adversary may take v_q(N) = e_q).

**Lemma 3.1 (forced-factor lemma, strongest form; PROVED, trivial).** Let S be a multiset in an abelian group G with product g.
For every homomorphism φ : G → A, Σ_{x∈S} φ(x) = φ(g). Consequently for every subgroup H ∌ g some x ∈ S lies outside H
((R272 repair, garbled fragment fixed) "N ≡ a (mod t), a ∉ H ⟹ some prime factor ∉ H"; the case H = ker χ₋₄ is "N ≡ 3 (4) ⟹ a prime ≡ 3 (4)").
Nothing more is forced: **(realisability)** for every multiset S′ ⊂ G with product g there are integers N′ ≡ N (mod t) whose
prime factors have exactly the classes S′ — in particular N′ prime (S′ = {g}). (R272 note: this is abstract realisability; realising
"L prime" by actual primes p in a class needs two linear forms prime simultaneously — that is HC's job in §6, not Dirichlet's.)
*Proof.* Product formula; for realisability take primes in the prescribed classes (Dirichlet) and adjust nothing: their
product has class g. ∎
So the forced content of the total product on Σ is {1, g}, and with the smooth part known it is Σ(s) ∪ Σ(s)·g_L.

**Proposition 3.2 (exact forced criterion; PROVED).** Call E(N, t) *forced by (p mod M)* if it holds for every abstract
factorisation of L compatible with the known data (Lemma 3.1). Then
  E(N, t) is forced  ⟺  −1 ∈ Σ(s) ∪ Σ(s)·g_L   (signed version: −1 ∈ Σ^±(s)·{1, g_L, g_L⁻¹}),
and this is a condition on p mod lcm(t, M_B): a finite union of residue classes (B1). If in addition the images ā_i ∈ G/H of the
k prime factors of L were known (a hypothetical input; §5 shows reciprocity does not supply it), forcing ⟺ for every lift
(a_i) ∈ ∏ ā_i with ∏ a_i = g_L, −1 ∈ Σ(s)·Σ(a_1, …, a_k): a finite check. (R272 repair: an unproved sentence about failure "for every choice of images" deleted.)
*Proof.* ⟸: the subset product is realised by a divisor (a subset of the small primes, possibly times L). ⟹: L prime is
compatible (Lemma 3.1), and then Σ(N) = Σ(s) ∪ Σ(s)·g_L exactly. ∎

**3.3 Choosing d to force small factors is the ET Type II covering.** "Choose d from p's residue data so that N_d has forced
factors in chosen cosets": the only forced factors are small primes q | N_d ⟺ d ≡ −p·4⁻¹ (mod q). A certificate built
from them (Prop 3.2 with L unused) is a B-smooth w ≡ −1 (mod 4d) with w | p + 4d, i.e. **d | (w + 1)/4 and p ≡ −4d (mod w)**: a
classical ET Type II residue class (B1). Using L as well gives the classes of Prop 3.2. Either way a finite congruence covering.

**Theorem 3.4 (the forced rule never fires at the point n = 1; PROVED, unconditional).** Fix B, D. Let
M := lcm(4D!, ∏_{q ≤ B} q^{e_q}) with q^{e_q} > 16D(D + 1) (so that also the 2-part of cp + 1 leaves t = 4c invertible room). For every prime p ≡ 1 (mod M) and every line of §1 with level
d, c ≤ D (resp. e ≤ D), the forced criterion of Prop 3.2 fails. Hence (Dirichlet) every "forced-factor" rule with bounded
levels and bounded small primes misses infinitely many primes — namely a full residue class.
*Proof.* p ≡ 1 (M) makes the smooth part of N and the class of L coincide with those of the integer N₁ obtained at "p = 1":
p + 4d ↦ 1 + 4d, cp + 1 ↦ c + 1, (p + e)/4 ↦ (1 + e)/4, (pe + 1)/4 ↦ (e + 1)/4 (the exponents e_q exceed the valuations of
these numbers; t | M). So Σ(s) ∪ Σ(s)·g_L is contained in the set of classes of divisors of N₁ ((R272 repair) "contained in", not
"is": e.g. B = 5, d = 12, N₁ = 49 gives {1, 49} ⊊ {1, 7, 49}). (R272 repair: q^{e_q} > 4D + 1 already suffices here; the stronger
q^{e_q} > 16D(D + 1) ≥ t·N_i(1) is what Thm 6.1 needs — it gives t | M/s_i, so the cofactor's class mod t is constant along
p = 1 + Mk. For c odd, v₂(cp + 1) = v₂(c + 1) and only odd divisors matter, so the 2-part is harmless.) A divisor v of 1 + 4d with v ≡ −1 (mod 4d)
satisfies v ≤ 4d + 1, so v = 4d − 1, and 4d − 1 | 4d + 1 ⟹ 4d − 1 | 2: impossible. Likewise c + 1 has no divisor ≡ −1 (mod 4c)
(4c − 1 > c + 1), and ab | (1 + e)/4 with a ≡ −b (mod e) needs e | a + b ≤ (1 + e)/4 + 1 < e. ∎
*Reading.* This is JOINT_BUDGET Prop 4.3's "modulo divisors of p − 1, p looks like 1, and 4/1 has no solution" made into a
statement about forced factors. (R272 repair, attribution:) it is the classical "congruence coverings never contain p ≡ 1 (mod M)"
obstruction (JOINT_BUDGET Prop 4.3 + B1_LINE §4) in forced-factor language — an analogue of, not a specialisation of,
LONGSHOT_PIGEONHOLE Thm 2.2 (a density bound) and POINTWISE_SIZE Thm C (CONDITIONAL on H); low novelty.

## 4. Zero-sum (Davenport) quantification: how many forced escaping factors would be needed

Let G = (ℤ/t)^×. Call x *escaping* if x ∉ H for a given subgroup H ∌ −1. Define the **target constant**
  η(G) := sup { min_{H ≤ G, −1 ∉ H} #{x ∈ S : x ∉ H} : S a multiset over G with −1 ∉ Σ(S) },
so that "every subgroup avoiding −1 is escaped by more than η(G) factors" forces −1 ∈ Σ(S).

**Lemma 4.1 (lower bound; PROVED).** If G has an element x of order 2n, n odd, with x^n = −1, then η(G) ≥ n − 1.
In particular for t = 4q, q ≡ 3 (mod 4) prime: η ≥ (q − 3)/2; and for t = 4d with d ≡ 3 (4) prime the same.
*Proof.* S := ((n−1)/2 copies of x, (n−1)/2 copies of x⁻¹). Σ(S) = {x^j : |j| ≤ (n − 1)/2} ∌ x^n = −1 (as −n < −(n−1)/2 and
n > (n−1)/2, and x^j = −1 ⟺ j ≡ n (2n)). If H ∌ −1 contained x (or x⁻¹) it would contain x^n = −1; so every element of S escapes
every such H: the min is n − 1. For t = 4q take x = (−1 mod 4, a generator mod q) of order q − 1 = 2n with n odd: x^n =
(−1, −1) = −1. ∎
**Proposition 4.2 (the forced supply is at most one escaping factor per subgroup).** From total-product data the number of
forced escaping large factors is 1 if g_L ∉ H and 0 otherwise (Lemma 3.1, realisability); for the b = 1 line and H = ker χ₋₄
it is 0 from total-product data alone (z29(b); (R272 repair) once the smooth part is known the cofactor can escape ker χ₋₄,
e.g. p + 4d = 3·L forces L ≡ 3 (mod 4)); for H = G² it is 1 iff g_L is a non-square (the (J)64 bit). Lemma 2.3 of SYNTHESIS_SPARKS8 (large primes
are private to one N_d) forbids pooling escaping factors from different levels into one integer. Hence (R272 repair) a
criterion of the form "> k escaping factors per subgroup ⟹ −1 ∈ Σ" must have k ≥ η(G), and η(G) ≥ (q − 3)/2 at a prime level
q ≡ 3 (mod 4) (Lemma 4.1; for q ≡ 1 (4) the construction gives only odd(q − 1) − 1, = 0 at Fermat primes), while ONE integer N_d
supplies ≤ 1. Moreover η(G) ≥ 1 ⟺ exp(G) > 2 for t = 4d: η ≥ 1 ⟺ some S has −1 ∈ ⟨S⟩ ∖ Σ(S); if exp(G) = 2 then ⟨S⟩ = Σ(S);
the converse was checked for all d ≤ 150 by R272 (`scripts/review_r272_eta_pos.py`; a general proof is not supplied — Assessment). **The zero-sum
mechanism cannot convert parity forcing into class forcing at any level with η(G) ≥ 1**, i.e. at every level except
those where a single escaping element is already −1-generating (exponent-2 levels t | 24, where −1 ∈ Σ ⟺ −1 ∈ ⟨S⟩).
*Quantitative reading (Assessment).* Ω(N) ≤ log₂N, so even unforced (actual) escaping factors can feed Lemma 4.1-type
groups only for q ≲ 2 log₂ p; typical N has ≍ log log p factors, i.e. zero-sum certificates are a small-modulus (B1-scale)
phenomenon; at larger levels Σ(S) is a 2^{Ω}-point random subset of G — the lottery. This is LONGSHOT_PIGEONHOLE Prop 1.4
(Kneser) in the target-−1 form; Lemma 4.1 gives the explicit cyclic witness. (R272 note: Lemma 4.1 is weak — brute force gives
η((ℤ/28)^×) ≥ 4, η((ℤ/44)^×) ≥ 7, `logs/review_r272_eta.txt`; with DISTINCT classes the relevant notion is the critical number
(Diderrich–Mann, Gao–Hamidoune: ≳ 2√|G| distinct elements avoiding small-subgroup obstructions give Σ = G) — repetition is what
makes η large. Literature not checked against sources.)

## 5. Reciprocity at an individual prime factor: what it links, and why it never reaches the class mod t

**Proposition 5.1 (the individual reciprocity link; PROVED).** Let p ≡ 1 (4), N = p + 4d, ℓ | N a prime, ℓ ∤ 2dp.
(a) χ_{−4d}(ℓ) = (ℓ/p). (Product over ℓ: Lemma 2.2(b).)
(b) For n | ℓ − 1: (p/ℓ)_n = (−4d/ℓ)_n, i.e. the n-th power class of p mod ℓ is the Frobenius of ℓ in K_{n,d} :=
ℚ(ζ_n, (−4d)^{1/n}). By n-th power reciprocity this is equivalent to a statement about ℓ modulo a prime π | p in ℤ[ζ_n]
(the n-th power class of ℓ mod π); multiplied over ℓ | N it gives (N/π)_n = (4d/π)_n, i.e. N ≡ 4d (mod p) — again a
total-product statement, now modulo p instead of modulo t.
(c) ((R272 repair) assume −4d ∉ ℚ^{×n}; otherwise K_{n,d} = ℚ(ζ_n) and the datum is trivial.) The joint law of (ℓ mod t,
Frob_ℓ in K_{n,d}) over primes ℓ is Chebotarev in ℚ(ζ_t)K_{n,d}, with ℚ(ζ_t) ∩ K_{n,d} ⊂
K_{n,d}^{ab}, which is ℚ(ζ_n) for n an odd prime (Thm 2.1(c)(i)) and ℚ(i, √d) ⊂ ℚ(ζ_{4d}) for n = 4 (d not a square; for
d = b², −4d = ((1 + i)√b)⁴ and K_{4,d} = ℚ(i, √b) is itself abelian: (p/ℓ)_4 = (b/ℓ) for ℓ ≡ 1 (4) — the Sophie-Germain exception, still
only a quadratic character of ℓ);
so the only class-mod-t information about ℓ carried by its power-residue data is χ_{−4d}(ℓ) and ℓ mod n.
*Proof.* (a) ℓ | p + 4d ⟹ p ≡ −4d (mod ℓ), so (−4d/ℓ) = (p/ℓ) = (ℓ/p) (p ≡ 1 (4)), and (−4d/ℓ) = χ_{−4d}(ℓ) by QR.
(b) The first statement is p ≡ −4d (mod ℓ); Kummer theory identifies (a/ℓ)_n with Frob_ℓ on a^{1/n}. (c) as Thm 2.1(b),(c). ∎

**Theorem 5.2 (no forbidden class for a single factor; PROVED, unconditional).** Let Ω/ℚ be finite Galois, C ⊂ Gal(Ω/ℚ) a
conjugacy class compatible with p ≡ 1 (4), d ≥ 1, and a ∈ (ℤ/4d)^×. Then there are infinitely many primes p with
Frob_p|Ω ∈ C such that p + 4d has a prime factor ℓ ≡ a (mod 4d), ℓ > any given bound.
*Proof.* Pick a prime ℓ ≡ a (mod 4d), ℓ unramified in Ω, ℓ ∤ 2d. Ω ∩ ℚ(ζ_ℓ) = ℚ (only ℓ ramifies in ℚ(ζ_ℓ)), so Chebotarev
in Ωℚ(ζ_{4ℓ}) — with ℚ(ζ_4)-part chosen compatibly with C — gives infinitely many p ∈ C with p ≡ −4d (mod ℓ), p ≡ 1 (4). ∎
*Reading.* So no datum of p in any fixed Galois extension (residue symbols of any order, Rédei symbols, governing fields)
rules out any class for an individual large factor. Combined with Lemma 3.1 (only the product is constrained) and
Prop 5.1(c) (the only individual link, χ_{−4d}(ℓ) = (ℓ/p), involves the unknown ℓ): **(R272 repair of the slogan) reciprocity
data of p = congruence data of p plus an independent non-abelian part; the congruence part is B1, and the non-abelian part
assigns no class to any individual large factor.**
What it would take to rule out the *whole multiset* (all factors simultaneously in a bad configuration) is the realisation
question of §6.

## 6. Realisation: non-abelian data of p adds nothing to bounded-level forcing (CONDITIONAL)

*(R272 repair, D1 FATAL.)* The first version of HC and Thm 6.1 was false: its compatibility condition only controlled
Ω ∩ ℚ(ζ_M), so the abelian part of Ω could force a congruence at a prime q > B. Counterexample (R272,
`scripts/review_r272_thm61_cex.py`): D = 1, B = 6, Ω = ℚ(ζ₇), C = {p ≡ −4 (mod 7)}; then 7 | p + 4 and w = 7 ≡ −1 (mod 4) is a
certificate at d = 1 for every p ∈ C (and HC as stated fails for f₁ = (f₀ + 4)/s₁). Corrected statements:

**Hypothesis HC (Bateman–Horn–Chebotarev; R272 repair).** Let f₀, …, f_r ∈ ℤ[k] be linear, Ω/ℚ finite Galois, C ⊂ Gal(Ω/ℚ) a
conjugacy class, Ω₀ := Ω ∩ ℚ^{ab} of conductor m, and A ⊂ (ℤ/m)^× the residues whose Artin symbol on Ω₀ lies in C|_{Ω₀}. If
there is k₀ with f₀(k₀) mod m ∈ A such that the system j ↦ f_i(k₀ + mj) (0 ≤ i ≤ r) is admissible, then there are infinitely many
k ≡ k₀ (mod m) with all f_i(k) prime and Frob_{f₀(k)}|Ω ∈ C. (Ω = ℚ is Dickson's conjecture; the non-abelian part of C imposes no
local condition, since Ω ∩ ℚ(ζ_n) ⊂ Ω₀ for every n; this is the standard heuristic.)

**Theorem 6.1 (CONDITIONAL on HC as corrected; R272 repair).** Fix D, a finite Galois Ω/ℚ with Ω₀ = Ω ∩ ℚ^{ab} of conductor m,
and a class C with C|_{Ω₀} = {1}. Take B ≥ max(4D + 2, every prime dividing m) and M as in Thm 3.4 with additionally
e_q ≥ v_q(m) (so Ω₀ ⊂ ℚ(ζ_M)). Then there are infinitely many primes p ≡ 1 (mod M) with Frob_p|Ω ∈ C such that **no**
certificate exists on the b = 1 line at levels ≤ D (either coordinate) or on any Type I/II e-slice with e ≤ D.
*Proof.* Put p = f₀(k) := 1 + Mk and, for each integer N_i(p) of the lines at levels ≤ D (p + 4d, cp + 1, (p + e)/4,
(pe + 1)/4), s_i := the B-smooth part of N_i(1) and f_i(k) := N_i(1 + Mk)/s_i ∈ ℤ[k] (s_i | M; q^{e_q} | M exceeds v_q(N_i(1)), so
v_q(N_i(1 + Mk)) = v_q(N_i(1)) for q ≤ B). Since m | M and C|_{Ω₀} = 1, every k is allowed by A (f₀(k) ≡ 1 (mod m)), so HC needs
admissibility of the f_i only: for q ≤ B, f_i(k) ≡ f_i(0) = B-rough part of N_i(1) ≢ 0 (mod q); for q > B the leading coefficients
(M/s_i, M/(4s_i), eM/(4s_i)) are q-units and the number of forms 1 + 2D + 2#{e ≤ D, e ≡ 3 (4)} < 4D + 2 ≤ B < q, so some residue
survives. HC gives infinitely many k with all f_i(k) prime and Frob_p ∈ C. Since q^{e_q} > 16D(D + 1) ≥ t·N_i(1), t | M/s_i and
[f_i(k)] = [f_i(0)] mod t, so at such p, Σ(N_i) = Σ(s_i) ∪ Σ(s_i)·[L_i(1)] ⊂ Σ(N_i(1)) ∌ −1 (Thm 3.4). ∎
*Reading (R272 repair).* Frobenius data = its abelian (congruence) shadow + a non-abelian part. The congruence part is B1 and
may well cover whole classes (the ℚ(ζ₇) example above); only the non-abelian part is shown (conditionally) useless at bounded
levels: at the point C|_{Ω₀} = 1 of the abelian shadow, no non-abelian condition rescues a bounded-level rule. This is the
four-line + Chebotarev extension of B1_LINE Thm 4.2 (same p ≡ 1 (M_σ) mechanism). It says nothing about unbounded levels (the
full b = 1 line uses d up to ≈ p/8), where the B2 lottery lives and no finite system of forms applies.

## 7. Numerics (EVIDENCE): how much does the forced mechanism certify?

`scripts/z33_census.py 1000000 200 10,30,1000` (`logs/z33_census_1e6_D200.txt`; 7 s): all 39 175 primes p ≡ 1 (4),
5 ≤ p ≤ 10⁶, b = 1 line, levels d ≤ 200; each actual certificate converted to (x, y, z) = (ad, acdp, cdp) and checked exactly
(first 3000); assertion "forced ⟹ actual" checked at every prime.
| tier (levels d ≤ 200) | certified | failures ≤ 10⁶ | odd squares 9…998001 (499) |
|---|---|---|---|
| A: actual Σ(N) ∋ −1 | 39 171 | 4: 193, 2521, 66529, 252001 (last needs d > 200) | 0 certified |
| Gen: −1 ∈ ⟨prime factors⟩ (cap relaxation) | 39 175 | 0 (193, 2521, 66529 all pass) | 0 certified |
| F₁₀: forced, primes ≤ 10 + one opaque cofactor | 38 441 | 734 (1.87 %) | 0 |
| F₃₀ | 39 132 | 43 (0.11 %) | 0 |
| F₁₀₀₀ | 39 171 | 4 (same as A: at p ≤ 10⁶ the cofactor is ≤ 1 prime > 1000) | 0 |
| X2: exponent-2 levels only (d, c ∈ {1,2,3,6}, e = 3 Types I/II), actual factors | 39 102 | 73 (0.19 %): 1321, 1489, 2521, 14281, 28921, … , 981601 | 0 |
Hard primes: 193 / 2521 / 66529 fail A and every F_B (as they must), pass Gen; 3361 passes every tier on this line (its
difficulty is Type-II-prime-modulus, CONJECTURE PM-II). 193 and 66529 pass X2; 2521 fails X2.

*Limiting (Haar) failure density of the forced congruence rule* (`scripts/z33_haar_forced.py`, `logs/z33_haar_forced.txt`;
4000 Haar-random p ≡ 1 (4) of size ≈ 10¹⁶ coprime to all primes ≤ max(B, D) + 1):
F_{10,200}: 72/4000 = 1.80 % ± 0.21 %; F_{30,200}: 9/4000 = 0.22 % ± 0.07 %; F_{1000,200}: 0/4000 (max least level 17);
F_{10,1000}: 44/4000 = 1.10 % ± 0.17 % (binomial s.e.; (R272 repair) error bars added). R272's independent sampler
(`logs/review_r272_haar.txt`): 1.76 % (n = 20000), 0.13 % (26/20000), 0/4000, 0.82 % (33/4000) — consistent within ≈ 1.7σ.
*Reading.* The forced mechanism (small forced primes + one forced element, i.e. Lemma 3.1/Prop 3.2 at its strongest) is an
ET congruence covering. It certifies most primes — 98 % with only the primes 2, 3, 5, 7 — but provably never a full set:
Thm 3.4 excludes the class p ≡ 1 (mod M) (Haar measure 1/φ(M), far below the sampling resolution for B = 1000), and Thm 6.1
(HC) keeps infinitely many primes outside it in every Chebotarev class compatible with that point. This is B1 exactly, with
"forced" now meaning "forced by any residue-symbol / governing-field data" (§2, §5, §6). The certifications are not new
existence mechanisms: what is forced is a congruence class of p, and the class p ≡ 1 (M) is where they fail.
*T1 control.* All tiers fail at all 499 odd squares ≤ 10⁶, including Gen. Reason (Prop 5.1(a) at n = m²): every prime ℓ | m² + 4d
has χ_{−4d}(ℓ) = (−4d/ℓ) = (m²/ℓ) = 1, so all factors lie in ker χ_{−4d} ∌ −1 — the T1 obstruction in its "generated subgroup"
form. At a prime the same factors have χ_{−4d}(ℓ) = (ℓ/p): T1 vs prime is visible factor by factor exactly through this link.

**Corollary 5.3 (R272 repair, D8: restated; the first version contradicted the WINDMILL 10.2/10.3 injectivity caveat).**
Let K = ℚ(√−tp), N = tp + 1 (the c-line; only here is a principal ideal (1 + √−tp) of norm N exhibited — the earlier
"or of any line's N" is withdrawn), and let the prime factors ℓ of N correspond to ideals 𝔩 | (1 + √−tp).
(i) (PROVED, WINDMILL Prop 10.3.) In 1 → (O/t)^×/im O^× → Cl_{(t)}(K) → Cl(K) → 1 the norm homomorphism Cl_{(t)}(K) → G sends
the kernel, at every odd prime power ℓ^k ∥ t, onto the squares (norms x² + tpy² ≡ x² mod ℓ^k, ℓ | tp ramified, all squares
occurring). Hence N𝔞 mod t is a class invariant on Cl(K) only modulo squares (odd part of t; at most the characters mod 8 at 2):
no function F on Cl(K) satisfies F([𝔞]) = N𝔞 mod t for all ideals 𝔞 of a class beyond G/G².
(ii) (Assessment.) Data about the factor classes that are invariants of Cl(K) as an abstract group / its 2^∞-structure (what
Rédei / Smith / Koymans–Pagano methods produce: ranks, Artin pairings, Frobenius in governing fields) therefore yield only the
χ-shadow of ℓ mod t; making "abstract class data" precise is not attempted.
(iii) (PROVED, WINDMILL 10.2.) A concrete class on the divisor hypercube DOES determine the divisor: for m | N with m ≤ √N the
form [m, 2, N/m] of discriminant −4tp is reduced, so its class determines m itself (R272 checked 15 312 such divisors). That is
knowing the factorisation — B2. ∎

## 8. Construction attempts (iteration log, each with the barrier hypothesis it hit and the modification tried)
* C1 total class → divisor: dies on realisability (N prime). Modification: individual factors (C2).
* C2 forced small factors by choosing d (CRT): = ET Type II classes (§3.3), B1; dies at p ≡ 1 (M) (Thm 3.4). Modification:
  non-congruence data (C3).
* C3 cubic/quartic/Eisenstein/Rédei/governing-field data of p: seen by [N] only through a quotient of p mod t
  (congruence data; G/G²-type for (i)–(iii)), independent non-abelian part otherwise (Thm 2.1, Prop 5.1, Cor 5.3 as repaired);
  the non-abelian part is conditionally useless at bounded levels at the point C|_{Ω₀} = 1 (Thm 6.1, R272 repair); the abelian
  part is B1 and can cover whole classes. Modification: data that act on the integer, not on p (C4).
* C4 algebraic factorisation of N forced by p's Gaussian/representation data (p = a² + b², p = x² + ny², 4d = poly(a, b)):
  N becomes a binary-form value; its factors are pushed INTO the genus subgroup (anti-forcing; JOINT_BUDGET Prop 4.2, near
  squares (J)53/(J)55), and finitely many polynomial families in (a, b) are barred by (J)3 (POINTWISE_BINARYFORM).
  The one abelian quartic exception (−4b⁴, Sophie Germain) is the thin-family mechanism (J)74, which needs p itself special.
* C5 zero-sum pooling across levels: large primes private (Lemma 2.3 SS8); η(G) ≥ (q − 3)/2 at prime levels (Lemma 4.1).
* C6 one integer carrying several levels (Type II ff′ = kp + 1, levels k/c for c² | k/4): the conditions nest (the weakest is
  the largest c), so this is one level, not several; no gain.
* C7 the exponent-2 shadow X2 (levels t | 24, where Σ = ⟨S⟩ and the event is "a factor escapes a subgroup"): a finite union
  of Landau events; fails exactly when p imitates a square for finitely many binary-form representability tests (p + 4 a
  primitive sum of two squares, p + 8 = x² + 2y², …); 73 failures ≤ 10⁶. Sieve-accessible on average, not pointwise.

## 9. Verdict (O263 checkpoint 1; R272 repairs applied)
* **Answer to route (b): no.** (R272 repair) Any Frobenius datum of p — residue symbols of any order, Rédei symbols,
  governing fields, Artin reciprocity for ray class fields mod t — sees the class [N] ∈ G only through a quotient of p mod t,
  i.e. congruence data, and is independent of [p] beyond it (Thm 2.1(b); for residue/Rédei data the quotient is G/G²-type plus
  p mod n; for general governing fields its size was not determined). For each individual prime factor ℓ the only link to
  p is χ_{−4d}(ℓ) = (ℓ/p), which involves the unknown ℓ (Prop 5.1), and no class is forbidden for a single large factor
  (Thm 5.2). Abstract class-group data on the factors yield only the χ-shadow; concrete reduced forms on the divisor hypercube
  determine the divisor itself, i.e. the factorisation (Cor 5.3 as restated). In short: reciprocity data of p = congruence
  data of p plus an independent non-abelian part.
* The congruence part is B1: the forced rules miss the explicit class p ≡ 1 (mod M) unconditionally (Thm 3.4, PROVED; the
  classical p ≡ 1 (M) obstruction in forced-factor language), though they may cover other whole classes (e.g. p ≡ −4 (7)).
  The non-abelian part adds nothing at bounded levels at the point C|_{Ω₀} = 1 (Thm 6.1, CONDITIONAL on the corrected HC;
  the first version was FALSE, R272 D1).
* Davenport/zero-sum cannot bridge parity and class: η(G) ≥ (q − 3)/2 at prime levels q ≡ 3 (4) against ≤ 1 forced escaping
  factor per integer (Lemma 4.1, Prop 4.2).
* EVIDENCE (§7, independently reproduced by R272): forced (congruence) certificates cover 98–99.9 % of primes ≤ 10⁶ but never
  the class p ≡ 1 (M); the generated-subgroup relaxation never fails at primes (levels ≤ 200) and always fails at odd squares,
  factor by factor.
* ES is not advanced; everything ends at B1 (congruence) or B2 (a divisor of one integer in a moving class).

*Checks* (`scripts/z33_checks.py`, `logs/z33_checks.txt`): Prop 5.1(a) on 140 287 (p, d, ℓ) triples (p ≡ 1 (4) < 2·10⁴,
d ≤ 60): 0 violations. Thm 3.4 with D = 6, B = 26 at the first 20 primes p ≡ 1 (mod M), all four lines (signed e-slices
included): 0 forced firings.
