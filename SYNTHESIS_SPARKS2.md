# SYNTHESIS_SPARKS2 — cross-pollinating (J)13–(J)25 (task O192, spark synthesis II)

Status: in progress (O192). ES is not solved, here or anywhere; nothing below proves a case of it.
Scripts `scripts/syn2_*`. Inputs: DISCOVERIES (J)11–(J)25 and the documents behind them; O178 DEPTH_ASPECT and O188
STERILE_STEER read from their branches (under review); SYNTHESIS_SPARKS.md (O171).

## 0. Iteration log

* (S1) Read the (J)13–(J)25 headlines and UNIT_ORBIT_ES §§1–2, 6, FIXED_MODULUS_SHOTS §§1–6, TWISTED_T1 §3.
  Common thread of the three newest provable variants (V_φ, ES^{(S)}, and the order-3 TES): anchor + wild partner +
  an *orbit* of shots with fixed modulus. The thread of (J)25: ES has no orbit (finite search, moduli O(p²)).
* (S2) Barrier question for (J)23: which hypothesis of its proof is load-bearing? The sieve (Bombieri–Vinogradov +
  Rosser–Iwaniec + Gupta–Murty) is needed only because S is FIXED. Letting S grow with n (seed (ii)) the variant becomes
  elementary (§2). This recalibrates what a "provable T1-bearing variant" is worth.
* (S3) Seed (iii) built concretely: an explicit fixed-modulus Type II shot family for the order-3 TES over ℤ[ω]
  (shot n + 18Q³, class condition mod 18), and a cubic mute normalisation (§3).

## 1. Cross-combinations (≥ 8), each with a sketch and a barrier pre-screen

Screens: B1–B6, T1 (= B5), F = (J)25's finiteness (every certificate of ES(p) has modulus O(p²)), D2 = (J)17's
degree-2 accident (over ℚ every Diff-parity / class invariant is quadratic). Verdicts are Assessments unless a
section below proves them.

**X1 (seed (i)) ES^{(S)} certificates [(J)23] × HJ/Lorenzini words [(J)15, (J)20]: "average" ES^{(S)} solutions at many
r into one ES word.** A length-3 word is tuv − u − v = n, i.e. t/n = 1/(uv) + 1/(un) + 1/(vn); an ES^{(S)} solution
with Q ≠ 1 is a *twisted* word (third numerator Q²). Two twisted words at r₁, r₂ combine only additively (six terms)
or by CRT on Q (Q leaves ⟨S⟩). Screen: F (any ES word has t, u, v ≤ O(p²)) and B2 via FIXED_MODULUS_SHOTS Cor 3.2
(same-D overlap is the bounded box |e_q| ≤ κ_q). Dead within the orbit family (the constructed triple is ES iff
Q | (r + 1)/4); other transformations are not excluded.

**X2 (seed (ii)) ES^{(S)} with growing S [(J)23] × least-non-residue scale [(J)9 Cor 4.6].** S = primes < 2r(p):
**elementary** (§2, Prop 2.2), Q ≪ log²p under GRH. Conversion to ES = box condition (B2). Not an ES route, but it
recalibrates (J)21/(J)23 (§2 Reading). ATTACKED (§2).

**X3 (seed (iii)) order-3 T1 [(J)19] × mute places [(J)23].** Explicit TES shot n + 18Q³ with fixed modulus 18; cubic
mute lemma; TES^{□₃} at every non-cube by one Hecke prime (§3). Uniform principle confirmed at orders 2 and 3; its
lesson is negative for ES (T1 is never the difficulty; orbit size is). ATTACKED (§3).

**X4 (seed (iv)) exponent coverings [(J)22] × sterile points [O178 Thm 3.1, O188].** O188 Lemma 4.1 already shows the
limit sets Λ_k never meet an r-generic line, so exponential families cannot approach O178's sterile points; the
pushed-forward class measure is 1/ord_{M'}(2) (O188 Lemma 4.2), so O178's convergent-measure mechanism does not
transfer. Primes p ≡ 1 (24) "near sterile points" are therefore not visible inside any k·2^m + 1. Remaining live
question (O188 spark 5): sterile points of Λ_k on ℓ-adic exponent lines. Screen: B1 hypothesis absent, but B5 (the
k = 4^j − 1 obstruction is the square 4^j) — Not pursued.

**X5 (seed (v)) Kudla Diff-parity [(J)13] × shots [(J)23, (J)25].** A shot (Q, r), r | n + 4Q², r ≡ 3 (mod 4), is the
binary form [r, 4Q, (n + 4Q²)/r] of discriminant −4n, i.e. r satisfies the Heegner hypothesis for ℚ(√−n) and the
"(n/r) = −1" condition is (−n/r) = +1 together with χ₋₄(r) = −1. An ES cube point (c, d, j) is the form
[h, 4cd, de] of discriminant −4dp with h ≡ −1 (mod 4cd), i.e. "first coefficient ≡ −1 modulo the middle one". The
T1 reads: ℚ(√−m²) = ℚ(i), where no prime ≡ 3 (mod 4) splits. Screen: (J)5 Prop 10.3 / (J)13 Prop 2.4′ — form classes
see "A ≡ −1 (mod B)" only through its genus shadow; Kudla is genus-invariant. A geometric reason for shots to fire
is just Chebotarev for ℚ(√−n, i). Dead as an ES mechanism; the dictionary is the (J)1 CM dictionary with a level.

**X6 (seed (vi)) SQ₅ sign half (S) [(J)15, (J)20] × longer HJ words / Lorenzini A_r.** The certificates of the
five SQ₅ slices are length-3 words (DEDEKIND_ES Lemma 1.1), and HJ_DEEP Prop 2.1 encodes Type II as formal
3-letter words at multiples cp (boundary letters 1 allowed); general Type I has no fixed-numerator word encoding
(HJ_DEEP, remark after Prop 2.1). Longer words are not ES certificates of these slices as such; whether some
longer-word encoding certifies other slices was NOT checked (self-review repair: an earlier "length 3 is forced for
all of ES" overstated the sources). At p ≡ 1 (12), (S)(p) unwinds to "tp + 1 = m·m″, m ≡ m″ ≡ −1 (mod t), with the
sign condition", the divisor form of the five slices (not of full ES). Screen: B2. Not pursued.

**X7 (new) totally positive ES over K = ℚ(√p) [(J)1 Prop 3.3] × anchor calculus [(J)19, (J)21 Thm 2.1] × involutions
[(J)2].** In K, p = (√p)² is a square, yet the two real places both carry ½, so Σ_{π|p} inv_π = 0: no T1 at p over K
(an even number of anchors cancels). ES(p) solutions are the σ-fixed (Galois-fixed) points of the totally positive
O_K-solutions of 4/p; the other σ-stable points have the shape 4/p = 1/z + Tr_{K/ℚ}(1/x) (a "quadratic Egyptian"
certificate: 4/p − 1/z = T/N with T² − 4N ∈ p·ℚ^{*2}). A parity/fixed-point argument needs a finite σ-stable set of
odd size whose non-rational σ-fixed points are excluded; the O_K-solution set is infinite (units), and no finite
σ-stable quotient with an odd count is in sight. Screen: (J)2 Thm 5.1 (finite-menu involutions), B6. Not pursued
beyond the sketch; the cancellation of the two anchors is the only new observation (Assessment).

**X8 (new) Drinfeld order-m classes [(J)18 Thm 2.2] × mute places [(J)23] in F_q[T].** Over F_q(T) the Artin problem
for a single mute prime is a theorem (Bilharz, RH for curves), so a function-field ES^{(S)} with |S| = 1 should be
provable unconditionally, whereas O178 Thm 2.5 gives sterile points for ES_q itself (large q, char 3). That would be a
clean model where "one mute place" provably separates a theorem from a problem with sterile points. Screen: model
only (no ℤ content); the anchor at ∞ needs a degree/sign normalisation compatible with NC. Not pursued (spark).

**X9 ES^{(S)} [(J)23] × exponent coverings [(J)22]: Q in an exponential orbit (Q = 3^m).** The shots n + 4·9^m: an
Artin problem of rank 1 (Hooley/GRH); the ES version needs r ≡ −1 (mod 4·3^m) (Prop 6.1), a growing modulus;
DEPTH_ASPECT Lemma 1.3 (exponential witnesses serve only bounded depth). Dead (B2).

**X10 DIFF_DEEP Prop 2.3 (ray condition free on one endomorphism) [(J)16] × divisor box [(J)25 Thm 3.1].** The box
−Box((h+1)/4) is exactly the constraint on the *second* endomorphism; per modulus it has size ≤ τ₃ = h^{o(1)}, which is
(J)16's "B3 in geometry-of-numbers form" made exact. Consistent; nothing new (screen B2/B3).

**X11 T1_TEMPLATE Thm 2.1 [(J)21] × TWISTED_T1 Lemma 2.1 [(J)19]: which normalisations of the free slot keep T1.**
Lemma 3.2 (§3) shows the mute condition is needed only when q ∤ x (case V > 0 is automatically trivial, at orders 2
and 3). So the natural mute normalisation is "v_q(z) < 0 and q ∤ x ⇒ m | v_q(z)", slightly weaker than O186's. PROVED (§3), minor.

**X12 internal-consistency audit of (J)13–(J)25.** §4.

## 2. Attack A (seed (ii) pushed to the end): with a growing mute set the T1-bearing variant is elementary

Notation of UNIT_ORBIT_ES §1. Let **ES^□(n)** be ES^{(S)}(n) with S = all odd primes not dividing n, i.e.
`4/n = 1/x + 1/y + 1/z,  x, y ∈ ℤ_{>0},  z ∈ ℚ_{>0} whose denominator is an odd square coprime to n.`
ES ⊂ ES^{(S)} ⊂ ES^□ for every finite S.

**Lemma 2.1 (T1 for ES^□; PROVED).** UNIT_ORBIT_ES Lemma 1.1 and Cor 1.2 hold verbatim for ES^□: every solution has
Σ_{ℓ|n} inv_ℓ α = ½, so at n = m² (m odd) no solution has Type I/II shape at every prime of m.
*Proof.* Lemma 1.1 is a statement at one place q; a given solution involves finitely many q, each muted (v_q(z) even
when negative); inv_2 = 0 because the denominator of z is odd; inv_∞ = ½. Cor 1.2's proof is then unchanged. ∎

**Proposition 2.2 (ES^□ at every non-square, elementary; PROVED, relative to Dirichlet's theorem only).** Let n > 1 be
odd and not a square.
(a) If n ≡ 3 (mod 4), Q = 1 and g = n + 4 give an ES solution (O186 Prop 3.1).
(b) If n ≡ 1 (mod 4), there is a prime r ≡ 3 (mod 4), r ∤ n, with Jacobi symbol (n/r) = −1. For the least such r
(call it r(n)) there is an odd Q with gcd(Q, n) = 1 and 4Q² ≡ −n (mod r), and UNIT_ORBIT_ES Prop 2.1 with g = r gives an explicit ES^□ solution of Type II shape at every
prime of n, with denominator of z dividing Q². If n = p is prime and p > 2r(p), one can take 0 < Q < 2r(p).
*(Self-review repair: the bound Q < 2r is false for composite n — n = 825, r = 7: the odd roots 3, 11 below 14
share factors with 825 and the least admissible Q is 17. For composite n only existence is claimed.)*
*Proof of (b).* n = n₀m², n₀ > 1 squarefree, n₀ ≡ 1 (mod 4) (as n ≡ 1 (mod 4) and m odd). The Jacobi character
(·/n₀) is non-trivial, so CRT gives a class a mod 4n₀ with a ≡ 3 (mod 4), (a/n₀) = −1; Dirichlet gives a prime
r ≡ a, r ∤ m. Then (n/r) = (n₀/r) = (r/n₀) = −1 (reciprocity, n₀ ≡ 1 (mod 4)). As (−1/r) = −1, −n/4 is a square mod r;
the two roots ±s give one odd representative in (0, 2r); the class s + 2rℤ contains elements prime to n (CRT, no prime
of n divides 2r). Prop 2.1 of UNIT_ORBIT_ES needs only g ≡ 3 (mod 4), g | n + 4Q², Q odd and prime to n. ∎
*Quantitative remark (Assessment; standard inputs, not re-derived).* r(n) is the least prime in a union of classes of
density ¼ for the pair of characters (χ₋₄, (·/n₀)); under GRH r(n) ≪ (log n)² (Bach-type bound), unconditionally
r(n) ≪ n^{O(1)} (Linnik). So for a prime p under GRH one may take S = {odd primes < 2r(p)} ∖ {p},
|S| ≪ (log p)²/log log p, and Q < 2r(p) ≪ (log p)².

**EVIDENCE (`scripts/syn2_sqden.py 1000000`, < 1 s).** All 78 496 primes 5 ≤ p ≤ 10⁶ solved by Prop 2.2, every solution
checked exactly (equation, positivity, odd square denominator coprime to p, Type II shape). For p ≡ 1 (mod 4):
max r(p) = 131 (p = 880 993); r(p) = 3, 7, 11, 19, 23, 31, … for 19 611, 9 825, 4 948, 2 444, 1 191, 624, … primes (each
next value roughly halves, as for a least non-residue). T1 control: for all odd squares m² ≤ 10⁶ and all odd Q ≤ 99
prime to m, m² + 4Q² has no prime factor ≡ 3 (mod 4) (0 found, as forced: a sum of two coprime squares).

**Reading (Assessment, the point of Attack A).**
1. The T1-bearing variant ES^□ is *trivially* true at every non-square: one Dirichlet prime, no sieve. The whole
   analytic content of (J)23 Thm 2.4 (Bombieri–Vinogradov + Rosser–Iwaniec + Gupta–Murty, ineffective) is the
   restriction to a FIXED finite S. Hence "a T1-bearing ES variant is provable" is, by itself, weak evidence for
   anything about ES: T1 is respected automatically by every shot mechanism whose firing condition is the quadratic
   character (n/r) = −1, and existence of such r is Dirichlet. What made (J)21/(J)23 non-trivial is the *size* of the
   orbit (rank 1 or fixed |S|), i.e. an Artin-type problem — not the T1.
2. The hierarchy ES = ES^{(∅)} ⊂ ES^{(S)} (fixed S, ineffective theorem) ⊂ ES^{(S_p)} (p prime, S_p = odd primes < 2r(p), elementary)
   ⊂ ES^□ (for S ⊆ S_p) is a scale of "how many mute places", and ES sits at the bottom, where the orbit is one
   point. Seed (ii)'s question "S = primes ≤ log p with Q ≤ p^{O(1)}" is answered only in a weaker form (under GRH,
   S = primes ≪ log²p, Q ≪ log²p; primes ≤ log p would need r(p) ≤ log p/2, which is false for a positive proportion
   of p by the usual least-non-residue statistics — Assessment). Within the orbit family of Prop 2.1, the conversion
   of the constructed triple to an ES triple is exactly "g ≡ −1 (mod 4Q)" (O186 Prop 6.1): for g = r(p) prime this
   needs Q | (r+1)/4, i.e. Q ≤ (r+1)/4 — a box condition (FIXED_MODULUS_SHOTS Cor 3.2) on the specific root
   Q ≡ √(−p/4) (mod r), the least-non-residue lottery in another dress. This is a statement about the constructed
   triple, not about every conceivable transformation of variant solutions into ES solutions.

## 3. Attack B (seed (iii)): an explicit fixed-modulus shot family for the order-3 TES, and TES with cubic mute places

Setting of TWISTED_T1 §3: O = ℤ[ω], λ = 1 − ω, TES(n): 9/n = ω/x + ω²/y + 2/z, x, y, z 2-primary (≡ 1 mod 2O);
n 2-primary, gcd(n, 6) = 1; α(u) = (−u₁/u₃, −u₂/u₃)_ω, u = (x/ω, y/ω², z/2). Put **g₀ := 10 + ω** (the class mod 18 with
g₀ ≡ −ω² (mod 9), g₀ ≡ ω (mod 2)).

**Proposition 3.1 (TES shot identity; PROVED, elementary).** Let D ∈ O with D ≡ 1 (mod 2) and gcd(D, 6n) = 1, and let
g ∈ O with g | n + 18D and g ≡ g₀ (mod 18). Put E := (n + 18D)/g, a := (g + ω²)/9, x := (ωn + E)/9, y := na, z := nxa/D.
Then x, a ∈ O, 9/n = ω/x + ω²/y + 2/z, x and y are 2-primary, z = Z/D with Z = nxa ≡ 1 (mod 2), and for every prime
π | n the solution has Type II shape at π (π ∤ x, v_π(y), v_π(z) ≥ v_π(n)).
*Proof.* x ∈ O: −ω²E ≡ gE = n + 18D ≡ n (mod 9), so E ≡ −ωn and 9 | ωn + E. a ∈ O by g ≡ −ω² (mod 9). Since
ωg + 1 = ω(g + ω²) = 9ωa: 9gx = ωng + n + 18D = 9ωna + 18D, i.e. **gx = ωna + 2D**. Then ω²x + 2D = x(g + ω²) − ωna
= a(9x − ωn) = aE, so ω²/y + 2/z = (ω²x + 2D)/(nxa) = E/(nx) = (9x − ωn)/(nx) = 9/n − ω/x. Mod 2: g ≡ ω, so
a ≡ ω + ω² ≡ 1, y ≡ 1, E ≡ g⁻¹ ≡ ω², x ≡ ω + ω² ≡ 1, Z ≡ 1. Shape: π ∤ 18D, so π ∤ n + 18D, π ∤ E, π ∤ x. ∎
For D = 1 this is a single shot n + 18 (TES's analogue of Mordell's p + 4); for D = Q³ it is an orbit with FIXED
modulus 18 (Q³ ≡ 1 (mod 2) automatically, as F₄^* has exponent 3 — the cube is invisible to the anchor).

**Definition (cubic mute variant).** For a set S of primes of O not dividing 6, **TES^{(S)}(n)**: 9/n = ω/x + ω²/y + 2/z
with x, y ∈ O 2-primary, z ∈ O[1/S] with z ∈ 1 + 2O₂, and for each q ∈ S the normalisation
`(N_q)  if v_q(z) < 0 and q ∤ x, then 3 | v_q(z).`
TES^{□₃} := TES^{(S)} with S = all primes not dividing 6n. (Shot solutions satisfy (N_q): q | Q, c = v_q(Q),
s = v_q(a); q ∤ g, so gx = ωna + 2Q³ gives v_q(x) = s if s < 3c and v_q(x) ≥ 3c otherwise; then v_q(z) = 2s − 3c
(s < 3c) and the case q ∤ x is s = 0, v_q(z) = −3c.)

**Lemma 3.2 (cubic mute lemma; PROVED).** For q ∈ S, q ∤ n, every TES^{(S)} solution has inv_q α = 0 in ⅓ℤ/ℤ.
*Proof.* If v_q(z) ≥ 0 all u_i are q-integral and TWISTED_T1 Thm 3.2's tame case applies. Let v_q(z) = −w < 0. Then
2/z ≡ 0 (mod q^w) and 9/n is a unit, so ω/x + ω²/y is q-integral; with x, y ∈ O this forces v_q(x) = v_q(y) =: V
(one of them positive and the other zero is impossible). A := −u₁/u₃, B := −u₂/u₃ have v(A) = v(B) = V + w =: v and
A/B = ωx/y; the tame symbol is (−1)^{v²}(A/B)^v = (−1)^v(ωx/y)^v, and −1 is a cube. (i) V = 0: (N_q) gives 3 | w = v,
so the symbol is a cube. (ii) V > 0: integrality of (ωy + ω²x)/(xy) gives v(ωy + ω²x) ≥ 2V, so y/x ≡ −ω (mod q^V) and
ωx/y ≡ −1: the symbol is (−1)^{2v} = 1. ∎ (The same computation with ω ↦ 1 and cubes ↦ squares shows that
UNIT_ORBIT_ES Lemma 1.1 needs its parity condition only when q ∤ x.)

**Theorem 3.3 (T1₃ for TES^{(S)}; PROVED from TWISTED_T1 Thm 3.2's proof + Lemma 3.2).** For every solution of
TES^{(S)}(n), Σ_{π|n} inv_π α = −⟨ω, 2⟩₂ ≠ 0. Hence at n = π^{3k} (π ∤ 6 prime, π ∉ S) no solution has Type I/II
shape at π. *Proof.* The place-by-place computation of TWISTED_T1 Thm 3.2 needs: x, y, z ∈ 1 + 2O₂ (anchor; ✓), u_i
λ-integral (partner; S ∌ λ ✓), integrality at tame v ∉ S, v ∤ n (✓); places in S contribute 0 (Lemma 3.2). ∎

**Corollary 3.4 (a cubic-character identity forced by T1₃; PROVED relative to Hecke's theorem on prime ideals in ray
classes).** For every prime element r ≡ 10 + ω (mod 18), 18 is not a cube modulo r.
*Proof.* If −18 ≡ t³ (mod r) (−1 is a cube), pick (Hecke) a prime π ≡ t (mod r), π ≡ 1 (mod 2), π ∤ 6. Then
r | π³ + 18, and Prop 3.1 (D = 1, g = r) gives a Type II-shaped solution of TES(π³), contradicting Thm 3.3. ∎
(By the cubic supplementary laws (18/r)₃ depends only on r mod 18, so it is a constant ≠ 1 on the class; numerically
(18/r)₃ = ω² for all 27 such r with N(r) ≤ 6000. A direct derivation from the supplements was not done.)

**Theorem 3.5 (TES^{□₃} at every non-cube; PROVED relative to Chebotarev for the abelian extension L·K(∛n)/K, L the
ray class field of K mod 18).** Let n ∈ O be 2-primary, gcd(n, 6) = 1, n not a cube. Then TES^{□₃}(n) has a solution
of Type II shape at every prime of n; if n is a cube, none of Type I/II shape at every prime (Thm 3.3).
*Proof.* As h_K = 1 and μ₆ → (O/18)^* is injective, "(𝔯) has a generator ≡ g₀ (mod 18)" is one class c₀ of the ray
class group mod 18. If all v_π(n) were ≡ 0 (mod 3), n = u·m³ with a unit u ≡ 1 (mod 2), i.e. u = ±1, and n would be a
cube; so some π | n (π ∤ 6) has 3 ∤ v_π(n), and M = K(∛n) is ramified at π while L' := L(∛18) is unramified outside 6.
Hence L' ∩ M = K ([M:K] = 3 prime) and Gal(L'M/K) = Gal(L'/K) × Gal(M/K). Pick σ ∈ Gal(L'/K) restricting to c₀ on L;
σ fixes a value ζ = σ(∛18)/∛18 ∈ μ₃; pick τ ∈ Gal(M/K) with τ(∛n)/∛n = ζ. Chebotarev for (σ, τ) gives a degree-1 prime
𝔯 = (r), r ≡ g₀ (mod 18), r ∤ 6n, with (n/r)₃ = ζ = (18/r)₃. *(Self-review repair: this avoids using that (18/·)₃ is
constant on the class, i.e. K(∛18) ⊂ L, which is plausible from the supplementary laws but was not checked.)* Then −n/18 ≡ Q³ (mod r) for some Q ∈ O, which may be taken ≡ 1 (mod 2) and prime to 6n (CRT),
and Prop 3.1 with D = Q³, g = r gives the solution; it satisfies (N_q) (remark after the Definition). ∎

**EVIDENCE (`scripts/syn2_tes_shots.py 6000 200`, 1.4 s; ℤ[ω] arithmetic from `scripts/tw_eis.py`, factorisation via sympy).**
(1) All 27 prime elements r ≡ 10 + ω (mod 18) with N(r) ≤ 6000 have cubic class of 18 equal to ω² (Cor 3.4).
(2) All 1536 2-primary split primes π (both 2-primary associates of each of the 768 split primes 7 ≤ N(π) ≤ 6000) are solved by
Thm 3.5's recipe with the least admissible r (max N(r) = 3187, max Q = 3671 ∈ ℤ): equation verified exactly in O,
2-primarity checked, Type II shape at π in all 1536, inv_π α = ω²-class "2" in all 1536 (matches TWISTED_T1's census
value (1, 2, 0)), and the cubic tame invariant at every mute prime above every q | Q is 0 (2908 places; Lemma 3.2).
(3) T1₃ control: for one 2-primary π above each split prime ≤ 200 (one associate, one of the two conjugates), and Q ≤ 39 prime to 6N(π) (267 shots), no divisor of
π³ + 18Q³ (any associate) lies in the class g₀.
(4) The plain single shot π + 18 (D = 1, TES itself) fires for only 52 of the 768 2-primary split primes with N(π) ≤ 6000.
(TES itself is not claimed at any prime here.)

**Reading (Assessment): the uniform principle and what it says about ES.**
* Order 2 and order 3 now behave identically: anchor (positivity / 2-primary) + wild partner (4 = 2², 9 = λ⁴·unit) +
  mute places normalised by m-th powers in the free slot. With infinitely many mute places, one Dirichlet/Hecke prime
  proves the variant at every non-m-th-power (ES^□: Prop 2.2; TES^{□₃}: Thm 3.5); with a fixed finite S, it is an
  Artin problem (m = 2: (J)23 for |S| ≥ 4, unconditional; m = 3: not attempted — a Gupta–Murty sieve over ℚ(ω) with
  the condition −n/18 ∈ ⟨S⟩³ mod 𝔯 is the natural route, CONJECTURE); with S = ∅, ES is a finite search ((J)25),
  while for TES (no positivity) finiteness is OPEN.
* In every mechanism of this shape the T1 is not the difficulty: the T1-sensitive step is a single character value ((n/r) = −1, resp.
  (n/r)₃ = (18/r)₃ ≠ 1), and Chebotarev supplies it whenever n is not an m-th power. My reading (Assessment, not a
  consequence of the results): for ES the difficulty sits in the size of the shot orbit, which over ℤ with S = ∅ is
  one point plus the growing-modulus lines of the certificate cube.
* So the "exact obstruction for ES" in seed (iii) is not a missing mute place per se but the absence of any
  equivalence ES ⟺ (variant with a mute place) + (cheap condition): the extra condition is O186 Prop 6.1's
  g ≡ −1 (mod 4Q) within the orbit family, which is B2. Assessment: provability of a T1-bearing variant is, by
  itself, weak evidence about ES.

## 4. Internal consistency audit (X12)

* **Citation error in DISCOVERIES (J)23** ("CRT large sieves for ES are capped at a (log N)^{3/4} saving ((A)19)"):
  section (A) has no item 19; the large-sieve cap is (D)19 (with (D)22 for prime laws; the form without the
  (log log N)^{3/4} factor is (D)24), PROVED conditional on KARY2 Thm 5.1. UNIT_ORBIT_ES §5 already carries R186 repair
  m8 to this effect; the ledger did not inherit it. Fix: "(D)19, (D)22, (D)24".
* **Notation clash "W"**: (J)10/(J)14 use W(n) for the *signed* single-slice certificate count
  (W(n) = Σ_{D(n)}(1 − (m″/n))/2, positivity = the sign event), while (J)15/(J)20 use (W) for the *sign-free*
  Lorenzini property n = xyz − x − z. So "(W) is trivial at primes" ((J)20 Prop 8.1) and "W(p) ≥ 1 for all primes
  ≤ 2·10⁶ is EVIDENCE" ((J)14) are about different objects and do not conflict; (H)19/(H)22 use W(p) for a third
  quantity. Suggest renaming (J)10/(J)14's count W_sl(n).
* Consistent on overlaps (checked by reading, and numerically where marked): (J)19's TES invariant (1, 2, 0) =
  the inv_π = 2 found on all 1536 shot solutions of §3 (numerical); (J)25 Remark 2.5 (A_h in the Jacobi −1 class)
  and (J)9 Thm 4.5 ((A/n) = −1) state the same sign; (J)25 Cor 2.3 (three modulus-4 shots) supersedes O188 §5's
  "p + 4 unique" (marked in both); (J)23 Cor 2.5 (ES^{(S)} at every n) and §2 here (ES^□ elementary) are consistent
  (ES^{(S)} ⊂ ES^□); (J)22 Cor 1.5 (k = 4^j − 1 obstruction at μ = 0) and O188 Lemma 4.1 (Λ_k avoids r-generic
  lines) do not conflict; (J)20 Prop 8.1 needs p ≥ 13 and 5 is on Lorenzini's list.
