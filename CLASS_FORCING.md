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
(ii) n = 4 (quartic symbols), Ω = ℚ(i, a^{1/4}), a ≠ ±□, a ≠ −4□² ·(□ a 4th power) : Ω^{ab} = ℚ(i, √a); information = (a/p)
and p mod 4. (iii) Rédei fields (dihedral of order 8 over ℚ, containing ℚ(√a, √b)): Ω^{ab} = ℚ(√a, √b); information = two
Legendre symbols. (iv) Smith's governing fields for 2^k-ranks are 2-extensions built over multiquadratic fields by iterated
dihedral/Rédei steps; whenever Ω^{ab} is multiquadratic (which holds for the Rédei-type towers in (iii), and must be checked
for any other Ω by computing Ω^{ab}), the information is a set of Legendre symbols.
So **in all these cases the residue-symbol data of p touches the class [N] ∈ G only through quadratic characters (G/G²) and
p mod n — the χ-shadow of Prop 10.3 (WINDMILL_REDUCTION) and Lemma 2.2(b) (SYNTHESIS_SPARKS8).**
*Proof.* (a) Column 4 of §1: 4N ≡ p, cp + 1, p, 1 (mod t) resp. (b) Ω and ℚ(ζ_t) are Galois with intersection F, so
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

Write N = s·L with s the B-smooth part (prime factors ≤ B, known from p mod M_B, M_B := ∏_{q ≤ B} q^{e_q}, e_q large) and L the
B-rough cofactor (class g_L := [N]·[s]⁻¹ ∈ G known, factorisation unknown).

**Lemma 3.1 (forced-factor lemma, strongest form; PROVED, trivial).** Let S be a multiset in an abelian group G with product g.
For every homomorphism φ : G → A, Σ_{x∈S} φ(x) = φ(g). Consequently for every subgroup H ∌ g some x ∈ S lies outside H
(for t ∤ … : "N ≡ a (mod t), a ∉ H ⟹ some prime factor ∉ H"; the case H = ker χ₋₄ is "N ≡ 3 (4) ⟹ a prime ≡ 3 (4)").
Nothing more is forced: **(realisability)** for every multiset S′ ⊂ G with product g there are integers N′ ≡ N (mod t) whose
prime factors have exactly the classes S′ — in particular N′ prime (S′ = {g}).
*Proof.* Product formula; for realisability take primes in the prescribed classes (Dirichlet) and adjust nothing: their
product has class g. ∎
So the forced content of the total product on Σ is {1, g}, and with the smooth part known it is Σ(s) ∪ Σ(s)·g_L.

**Proposition 3.2 (exact forced criterion; PROVED).** Call E(N, t) *forced by (p mod M)* if it holds for every abstract
factorisation of L compatible with the known data (Lemma 3.1). Then
  E(N, t) is forced  ⟺  −1 ∈ Σ(s) ∪ Σ(s)·g_L   (signed version: −1 ∈ Σ^±(s)·{1, g_L, g_L⁻¹}),
and this is a condition on p mod lcm(t, M_B): a finite union of residue classes (B1). If in addition the images ā_i ∈ G/H of the
k prime factors of L were known (a hypothetical input; §5 shows reciprocity does not supply it), forcing ⟺ for every lift
(a_i) ∈ ∏ ā_i with ∏ a_i = g_L, −1 ∈ Σ(s)·Σ(a_1, …, a_k): a finite check, and for |H| ≥ 3 and k ≥ 2 it can still fail for every
choice of images (the adversary has k − 1 free coordinates).
*Proof.* ⟸: the subset product is realised by a divisor (a subset of the small primes, possibly times L). ⟹: L prime is
compatible (Lemma 3.1), and then Σ(N) = Σ(s) ∪ Σ(s)·g_L exactly. ∎

**3.3 Choosing d to force small factors is the ET Type II covering.** "Choose d from p's residue data so that N_d has forced
factors in chosen cosets": the only forced factors are small primes q | N_d ⟺ d ≡ −p·4⁻¹ (mod q). A certificate built
from them (Prop 3.2 with L unused) is a B-smooth w ≡ −1 (mod 4d) with w | p + 4d, i.e. **d | (w + 1)/4 and p ≡ −4d (mod w)**: a
classical ET Type II residue class (B1). Using L as well gives the classes of Prop 3.2. Either way a finite congruence covering.

**Theorem 3.4 (the forced rule never fires at the point n = 1; PROVED, unconditional).** Fix B, D. Let
M := lcm(4D!, ∏_{q ≤ B} q^{e_q}) with q^{e_q} > 4D(D + 1). For every prime p ≡ 1 (mod M) and every line of §1 with level
d, c ≤ D (resp. e ≤ D), the forced criterion of Prop 3.2 fails. Hence (Dirichlet) every "forced-factor" rule with bounded
levels and bounded small primes misses infinitely many primes — namely a full residue class.
*Proof.* p ≡ 1 (M) makes the smooth part of N and the class of L coincide with those of the integer N₁ obtained at "p = 1":
p + 4d ↦ 1 + 4d, cp + 1 ↦ c + 1, (p + e)/4 ↦ (1 + e)/4, (pe + 1)/4 ↦ (e + 1)/4 (the exponents e_q exceed the valuations of
these numbers; t | M). So Σ(s) ∪ Σ(s)·g_L is the set of classes of divisors of N₁. A divisor v of 1 + 4d with v ≡ −1 (mod 4d)
satisfies v ≤ 4d + 1, so v = 4d − 1, and 4d − 1 | 4d + 1 ⟹ 4d − 1 | 2: impossible. Likewise c + 1 has no divisor ≡ −1 (mod 4c)
(4c − 1 > c + 1), and ab | (1 + e)/4 with a ≡ −b (mod e) needs e | a + b ≤ (1 + e)/4 + 1 < e. ∎
*Reading.* This is JOINT_BUDGET Prop 4.3's "modulo divisors of p − 1, p looks like 1, and 4/1 has no solution" made into a
statement about forced factors; it is the b = 1 / c-line / e-slice specialisation of LONGSHOT_PIGEONHOLE Thm 2.2 and
POINTWISE_SIZE Thm C, here with an exact, elementary proof and an explicit residue class (no density statement needed).
