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

Remark 1.3. The same holds verbatim for k·b^m + c (2 replaced by the primes of b) and for any sequence whose reduction modulo every M
is eventually periodic (Lucas sequences etc.), with Ẑ replaced by the appropriate profinite exponent space.
