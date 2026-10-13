# EXPONENT_COVERING — exponent coverings of ES on sparse exponential families (O185, spark relay K)

Status: internal research note, SPARK phase. **ES is not solved; no claim beyond the stated families.** Labels as in DISCOVERIES.md.
Scripts `scripts/ec_*`. Builds on LORENZINI_W.md §9 (Sierpiński-type exponent covering for Lorenzini's (W)), POINTWISE_SIZE (B1),
`scripts/mordell_lib.py` (the seven Elsholtz–Tao Prop 1.9 fixed-parameter class families, "ET classes" below).

## 0. Summary (updated as the work proceeds)
* (§1) Exact criterion (PROVED): an exponential family n_m = k·2^m + c (c = ±1) is covered, for all large m, by finitely many ET classes
  iff its *limit set* Λ_k ⊂ Ẑ avoids the sterile set S (the complement of the union of all ET classes). S contains all profinite squares.
* (§2) Why B1 disappears (PROVED, structural): for polynomial families the parameter space Ẑ = Π_q Z_q is a product over the target
  primes, so "a square at every q separately" glues to a profinite square point. For exponential families the exponent μ ∈ Ẑ couples the
  primes q through the orders ord_q(2), and local squares need not glue: this is a Sierpiński covering, but with quadratic characters.
* (§3) First instance (search result; certification in progress): n = 27·2^m + 1, which lies in Mordell's hard class 529 (mod 840) for all
  m ≡ 2 (mod 12) and contains the primes 109, 1811939329 (m = 26), 30399297484750849 (m = 50).

## 1. Setup and the compactness criterion
Notation. k ≥ 1 odd, c ∈ {+1, −1}, n_m = k·2^m + c. An *ET class* is a residue class r (mod M) from one of the seven families of
Elsholtz–Tao Prop 1.9 (`mordell_lib.iter_classes`): every sufficiently large n ≡ r (mod M) has an explicit solution of 4/n = 1/x+1/y+1/z
whose coordinates are polynomials in n. U ⊂ Ẑ is the union of all ET classes (open); S := Ẑ \ U (closed) is the *sterile set*.

**Lemma 1.1 (periodicity; PROVED).** Let M = 2^s M′ with M′ odd and M′ | 2^L − 1. For m ≥ s, n_m mod M depends only on m mod L.
*Proof.* n_{m+L} − n_m = k2^m(2^L − 1) ≡ 0 (mod M′), and n_m ≡ c (mod 2^s) for m ≥ s. ∎ (Every odd M′ divides 2^L − 1 for L = ord_{M′}(2).)

**Definition (limit set).** For μ ∈ Ẑ let ν(μ) ∈ Ẑ = Z_2 × Π_{q odd} Z_q have 2-component c and q-component k·2^μ + c, where
2^μ ∈ Z_q^× is the continuous extension of m ↦ 2^m (Z_q^× is a profinite group). Λ_k := ν(Ẑ), a compact set.

**Theorem 1.2 (PROVED).** The following are equivalent: (a) there are finitely many ET classes and m₀ such that every n_m, m ≥ m₀,
lies in one of them; (b) Λ_k ∩ S = ∅. Moreover Λ_k ∩ Sq ≠ ∅ ⟹ (b) fails, where Sq := {x ∈ Ẑ : x_q ∈ Z_q² for all q} is the set of
profinite squares (Sq ⊂ S).
*Proof.* ET classes are clopen. (b)⇒(a): Λ_k is compact, so finitely many classes C_1..C_r cover it; their union C is a union of residue
classes mod some M = 2^s M′. For m ≥ s, n_m ≡ ν(m) (mod M) (odd components agree; both 2-components ≡ c mod 2^s), and ν(m) ∈ C.
(a)⇒(b): given μ, pick m_j ≥ m₀, m_j → ∞, m_j → μ in Ẑ. Then n_{m_j} → ν(μ) in Ẑ (the 2-components k2^{m_j} + c → c). All n_{m_j} lie in the
closed set C, hence ν(μ) ∈ C ⊂ U. Squares: if an ET class r (mod M) contained x ∈ Sq then r is a square mod every prime power of M, so
r ≡ s² (mod M); r is odd when M is even (all ET residues are ≡ −f, −e or −e⁻¹ with f, e odd), so there are odd integers s′ ≡ s (mod M)
with s′² in the class, s′ large. But odd squares have no Type I/II solutions (ET Prop 1.6, campaign T1), while the class gives one. ∎

**Divisor classes.** D_q := {n ≡ 0 (mod q)} for an odd prime q: ES(n) follows from an explicit ES(q) scaled by n/q, and the
coordinates are again polynomials in n, integer-valued on the class. Put U′ := U ∪ ⋃_q D_q, S′ := Ẑ \ U′ (closed).

**Theorem 1.4 (PROVED; same proof as 1.2).** A finite covering of {n_m : m ≥ m₀} by ET and divisor classes exists iff Λ_k ∩ S′ = ∅.
S′ ⊇ Sq^× := {x : x_2 ≡ 1 (8), x_q ∈ (Z_q^×)² for all odd q} (profinite *unit* squares): D_q contains no point that is a unit at q, and the
ET part is Theorem 1.2. So non-unit square points (e.g. ν(ℓ) = s² with an odd prime q | s) are NOT obstructions: they lie in D_q.

**Corollary 1.5 (integer obstruction points; PROVED).** Let b = 2, c = +1, k odd. For ℓ ∈ Z, ν(ℓ) ∈ Sq^× iff ℓ = 0 and k = 4^j − 1 (j ≥ 1).
*Proof.* ℓ ≥ 0: ν(ℓ) has odd components the integer N = k2^ℓ + 1 > 1; N is a square in every Z_q (q odd) iff N = s² (an integer that is a
square modulo almost all primes is a square), and a unit at every odd q iff s is a power of 2. Then k2^ℓ = (s−1)(s+1) with s = 2^j forces
ℓ = 0 (k2^ℓ is odd·2^ℓ, s ± 1 odd), k = 4^j − 1. ℓ < 0: components (k + 2^{|ℓ|})/2^{|ℓ|}; a square everywhere iff 2^{|ℓ|}(k + 2^{|ℓ|}) = □,
so |ℓ| even and k + 2^{|ℓ|} = s² with s a power of 2: k = 4^j − 4^i odd forces i = 0, i.e. ℓ = 0. ∎
So **3·2^m + 1, 15·2^m + 1, 63·2^m + 1, … (k = 4^j − 1) admit no finite exponent covering by ET/divisor classes**: along m ≡ 0 (mod L),
n_m ≡ 4^j (mod 2^L − 1) mimics the even square 4^j (the "2²-mimicking" form of B5/T1; note T1 itself is about odd squares).

Remark 1.3. The same holds verbatim for k·b^m + c (2 replaced by the primes of b) and for any sequence whose reduction modulo every M
is eventually periodic (Lucas sequences etc.), with Ẑ replaced by the appropriate profinite exponent space.

## 2. Why B1 does not apply: product vs. coupled parameter spaces (PROVED)
**Proposition 2.1 (polynomial families).** Let f ∈ Z[t] be non-constant and F = {f(t) : t ∈ Z, t ≡ t₀ (mod T)}. The closure of F in Ẑ is
f(t₀ + TẐ), computed componentwise: f(t)_q = f(t_q). Hence F̄ ∩ Sq^× ≠ ∅ iff for every prime q (q = 2 included, with "≡ 1 mod 8") there is
t_q ∈ t₀ + TZ_q with f(t_q) a unit square in Z_q. Consequently a finite ET/divisor covering of F exists only if (i) some *single* prime power
q^e makes f(t) a non-(unit square) mod q^e for all t ≡ t₀ (T) — a one-prime local obstruction — or (ii) F̄ avoids Sq^× because of (i) after all.
Only finitely many q can do (i) (for q ∤ 2T·lc(f)·disc(f) large, y² = f(t) has a smooth F_q-point with y ≠ 0 by Weil, which lifts by Hensel).
*Proof.* Ẑ = Π_q Z_q and f commutes with the projections, so independent local choices t_q glue to t̂ ∈ Ẑ; then f(t̂) ∈ Sq^× and
Theorem 1.4 (whose proof is family-agnostic: any compact closure + clopen classes) excludes a covering. ∎
This is the mechanism behind B1 (Mordell/Schinzel; POINTWISE_SIZE Thm C at the rational point q*_univ): the prime/integer family is
"locally a unit square at each prime separately", and the product structure glues the local points into a profinite square-mimicking point.

**Proposition 2.2 (exponential families: the coupling).** For n_m = k·2^m + c the q-component of ν(μ) depends on μ through
μ mod ord_q(2)·q^∞ only, and these quotients of Ẑ are *not independent* as q varies (they share the prime factors of the orders).
Let A_q := {μ ∈ Ẑ : ν(μ)_q ∈ (Z_q^×)²}, a clopen set (for q ∤ k: A_q ≠ ∅ iff ... it is a union of classes mod ord_q(2)·q^{e}).
Then Λ_k ∩ Sq^× = ⋂_q A_q (the 2-component c = 1 is a square), and by compactness it is empty iff ⋂_{q ∈ Q} A_q = ∅ for a finite set Q.
That finite emptiness statement is a **Sierpiński covering of the exponents by quadratic characters (and divisibilities)**: for every
m mod L = lcm_{q∈Q} ord_q(2), some q ∈ Q has q | n_m or (n_m/q) = −1. Unlike the polynomial case, each A_q can be non-empty
(every single prime is locally harmless) while the intersection is empty. So the hypothesis of B1 that fails is *product structure of
the parameter space over the target primes*. (PROVED: this is a restatement of Theorem 1.4 plus compactness.)

Example (k = 27, Q = {5, 7, 13}, L = 12): writing (χ₅, χ₇, χ₁₃) for the Legendre symbols of n_m (0 = divisible):
m ≡ 0,3,6,9 → 7 | n_m; m ≡ 1,5,9 → 5 | n_m; m ≡ 4,7,10 → (n_m/7) = −1 (n_m ≡ 6 mod 7); m ≡ 8, 11 → (n/5) = −1;
m ≡ 2 → n_m ≡ 5 (mod 13), (5/13) = −1, while (n_m/3) = (n_m/5) = (n_m/7) = +1 — this is the class where n_m ≡ 529 (mod 840),
Mordell's hard class. Each A_q alone is non-empty; A₅ ∩ A₇ ∩ A₁₃ = ∅.

## 3. The Skolem / Bertók–Hajdu dictionary (SHARP; dictionary PROVED, the principle CONJECTURE)
By Theorem 1.4 and Prop 2.2, the square half of the covering problem for n_m = k·2^m + 1 is exactly:
> (EH_k) *If the equation k·2^x + 1 = y² has no solution with x ∈ Z and y ∈ Z a unit at every odd prime (i.e. y = ±2^j), then it has
> no solution modulo some M: there is M such that k·2^x + 1 ≢ (unit)² (mod M) for every x ≥ v₂(M).*
Equivalently Λ_k ∩ Sq^× = ∅ for every k ≠ 4^j − 1 (Cor 1.5 identifies the global solutions). (EH_k) is an *exponential local–global
principle* of exactly the type of Skolem's conjecture and of the Hasse-type principle of Bertók–Hajdu (arXiv:1407.6499, Math. Comp. 2016;
extension Monatsh. Math. 2018, doi 10.1007/s00605-018-1169-8), with one twist: the unknown y ranges over a non-finitely-generated
group of units, so it is a *mixed* (exponential + square) principle. Bertók–Hajdu prove their principle for "almost all" equations and
find moduli via numbers m with small Carmichael λ(m) (Erdős–Pomerance–Schmutz); our moduli M | 2^L − 1 with L highly composite are the
same device. **So: ES on k·2^m + 1 by fixed slices ⟸ (EH_k) + "no sterile non-square point in Λ_k"; and ⟹ (EH_k).**
The second condition is the campaign's sterile-set question (POINTWISE_TYPEI2, LORENZINI_W §4) restricted to a compact
one-parameter set.
