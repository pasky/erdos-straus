# KUDLA_ES — the Kudla program (special cycles, incoherent Eisenstein series) against Erdős–Straus (task O172)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.** Labels as in
DISCOVERIES.md. Scripts `scripts/kud_*`. Inputs: QUATERNION_ES.md (O130: Λ_{d,m}, Prop 1.3), GROWING_IDENTITIES.md
(O170: Prop 4.1, the sign-blind set D*(n)), STRONG_APPROX_ES.md Thm 9.1, WINDMILL_REDUCTION.md Prop 10.3 / Rem 10.4,
reviews/redteam-automorphic.md §4 (T1–T8).

Kudla notation used throughout. For a collection 𝒞 = (𝒞_v)_v of local quadratic spaces of dimension r over ℚ_v
with the same discriminant, 𝒞 is *coherent* if ∏_v ε(𝒞_v) = 1 (then it comes from a global space), *incoherent*
otherwise. For a symmetric matrix T, `Diff(T, 𝒞) := {v : 𝒞_v does not represent T}`. If 𝒞 is incoherent and T is
nondegenerate of size r − 1, then |Diff(T, 𝒞)| is **odd** (Kudla, Ann. Math. 146 (1997), Lemma/Prop. on Diff; this
is just the product formula for the Hasse invariant of the unique local completion of T to 𝒞_v).
The central value of the incoherent Siegel Eisenstein series E(τ, s, Φ_𝒞) vanishes, and the T-th coefficient of
E'(τ, 0, Φ_𝒞) is supported on T with |Diff(T)| = 1 = {ℓ}; for ℓ < ∞ it equals (up to normalisation) log ℓ times a
Gross–Keating local multiplicity times a count of supersingular points (Kudla 1997 for Shimura curves; Gross–Keating
1993; Kudla–Rapoport–Yang, *Modular forms and special cycles on Shimura curves*, 2006). These deep identities are
**cited, not used**: every PROVED statement below is elementary (Hilbert symbols); the cited identities only give
the geometric reading.

## 1. Type I certificates are points of genus-2 Kudla special cycles; T1 is the parity of Diff(T)

Setting (QUATERNION_ES Lemma 1.2). For d, m ≥ 1 let `T(d,m) := [[d, −1/2],[−1/2, m]]` (half-integral, positive
definite, `det(2T) = 4dm − 1`). It is the Gram matrix (for the norm form `nrd`) of a pair of trace-zero elements
`u, v` with `u² = −d`, `v² = −m`, `uv + vu = 1`, generating the order Λ_{d,m} of reduced discriminant `4dm − 1` in the
definite algebra `B_T := B_{d,m} ≅ (−d, −d(4dm−1))_ℚ`. Let 𝒞 be Kudla's incoherent ternary collection for the
modular curve: 𝒞_ℓ = (M₂(ℚ_ℓ)⁰, det) for ℓ < ∞, 𝒞_∞ = positive definite ternary. Then T is represented by 𝒞_ℓ iff B_T
splits at ℓ (a binary space U ⊂ B⁰ determines its completion U ⊕ ⟨disc⟩ and hence B), so
`Diff(T(d,m), 𝒞) = Ram_fin(B_{d,m})`, and |Ram_fin| is odd because B_T is definite. Geometrically, a point of the
special cycle Z(T) is a supersingular E/𝔽̄_ℓ (ℓ ∈ Diff(T)) with two special (trace-zero) endomorphisms of Gram T.

**Lemma 1.1 (2 is never in Diff; PROVED).** `det(2T) = 4dm − 1` is odd, so Λ_{d,m} ⊗ ℤ₂ has reduced discriminant a
2-adic unit, hence is a maximal order of B_T ⊗ ℚ₂ of discriminant 1; so B_T splits at 2. ∎

**Theorem 1.2 (Type I ⇒ Kudla cycle; Diff(T) is computed by n; PROVED, elementary).** Let n ≥ 3 be odd (prime or
not) and let (a, b, c, d) be a Type I tuple for n in ET's parametrisation, `4abd = ne + 1`, `a + b = ce`. Put
`T = T(d, ab)` (so `det(2T) = ne`). Then
`Diff(T, 𝒞) = Ram_fin(B_T) = { ℓ | n : ℓ ∤ e, v_ℓ(n) odd, (−d/ℓ) = −1 }`,
and this set has odd cardinality. In particular:
(a) **(T1 for Type I.)** If n is a square, the right side is empty, contradicting oddness: odd squares have no
Type I tuples. More generally a Type I tuple at level d forces `∏_{ℓ | n, ℓ ∤ e} (−d/ℓ)^{v_ℓ(n)} = −1`.
(b) If n = p is prime, `Diff(T) = {p}`: the certificate is a point of Z(T) in characteristic p (QUATERNION_ES Prop 1.3),
i.e. of the support of the T-th coefficient of E'(τ, 0, Φ_𝒞).
*Proof.* By bilinearity and `(x, x) = (x, −1)`: `B_T ≅ (−d, −d·ne)`, and `(−d, −d·ne)_v = (−d, −1)_v·(−d, ne)_v`.
Odd ℓ ∤ d: `(−d, −1)_ℓ = 1` and `(−d, ne)_ℓ = (−d/ℓ)^{v_ℓ(ne)}`. If ℓ | e, then `e | 4a²d + 1` (QUATERNION_ES Lemma 1.1,
which uses `e | a + b`), so `−d ≡ (2a)^{−2}` is a square mod ℓ and the symbol is 1. If ℓ ∤ e, ℓ | n, the symbol is
`(−d/ℓ)^{v_ℓ(n)}`. If ℓ ∤ ne, it is 1. Odd ℓ | d: `ne = 4abd − 1 ≡ −1 (mod ℓ)`, so `ne ∈ −1·ℚ_ℓ^{×2}` and
`(−d, ne)_ℓ = (−d, −1)_ℓ`; the product is `(−d, −1)_ℓ² = 1`. At 2: Lemma 1.1. At ∞: `(−d, −dne)_∞ = −1`. Oddness of
the finite set: product formula. (a), (b) are immediate. ∎

*Check* (`scripts/kud_typeI_diff.py 20000`, ~60 s): all 882749 Type I tuples (a ≤ b) of all odd n ≤ 20000: Ram_fin(B_T)
computed from Hilbert symbols equals the predicted set in every case, 2 ∉ Ram, |Ram_fin| odd; 0 tuples at odd squares;
3 odd non-squares n ≤ 20000 have no tuple at all (EVIDENCE only; composite n is outside ES's prime reduction).

**Reading (Assessment).** This is the precise form of the brief's thesis for Type I: the certificate's Gram matrix
T lives in Kudla's *incoherent* ternary collection, whose Diff(T) must be odd; the ES congruence `e | a + b` makes
every place ℓ | e represent T, so Diff(T) is carried by the primes of n alone, with odd exponent and `(−d/ℓ) = −1`.
At n = m² no such prime exists — **T1 is the oddness of Diff(T) for the incoherent collection** (equivalently: at
squares the ES local conditions would make the collection {𝒞_ℓ} represent T everywhere, i.e. behave coherently,
which a definite B_T cannot). Mathematically this is Hilbert reciprocity, i.e. the same content as ET Prop 1.6 /
the Jacobi-symbol proofs (GROWING_IDENTITIES Lemma 1.3): a new *dictionary*, not new arithmetic.

**Theorem 1.4 (Type II: the Heegner Gram matrix; PROVED, elementary).** Let n ≥ 3 be odd and (a, b, c, d) a Type II
tuple, `4abd = n + e`, `a + b = ce`, `f = 4acd − 1`, `f' = 4bcd − 1`, so `ff' − 4c²dn = 1`, `f ≡ f' ≡ −1 (mod 4cd)`
(O131 / (I)4). Put `T' := [[f, 1],[1, f']]` (positive definite, the Gram matrix of the Heegner form `[f, 2, f']` of
discriminant −16c²dn). Its definite algebra is `B_{T'} ≅ (−f, −f(ff' − 1)) ≅ (−f, −f·dn)`, and
`Diff(T', 𝒞) = Ram_fin(B_{T'}) = { ℓ | n : v_ℓ(n) odd, (−f/ℓ) = −1 }`, of odd cardinality.
Hence (a) odd squares have no Type II tuples (T1 for Type II); (b) for n = p prime, `(−f/p) = −1` is **forced** (this is
the Bright–Loughran/Yamamoto condition `(f/p) = −(−1/p)`, (I)7) and Diff(T') = {p}.
*Proof.* `(−f, −f·X)_v = (−f, −1)_v(−f, X)_v`, `X = 4c²dn ≡ dn` mod squares. Odd ℓ ∤ f·dn: 1. Odd ℓ | f: `4c²dn = ff' − 1
≡ −1 (mod ℓ)`, so `X ∈ −ℚ_ℓ^{×2}` and the product is `(−f, −1)_ℓ² = 1`. Odd ℓ | d, ℓ ∤ f: `−f ≡ 1 (mod ℓ)` is a square
(f ≡ −1 mod d), so 1. Odd ℓ | n, ℓ ∤ d: `(−f/ℓ)^{v_ℓ(n)}` (if also ℓ | d the previous case gives 1 and then `(−f/ℓ) = 1`
anyway). At 2: `−f ≡ 1 (mod 4)` gives `(−f, −1)_2 = 1` and `(−f, u)_2 = 1` for odd u; if 2 | dn then 2 | d (n odd), so
`8 | 4cd` and `−f ≡ 1 (mod 8)`, giving `(−f, 2)_2 = 1`. At ∞: −1. Product formula. ∎
*Check* (`scripts/kud_typeII_diff.py 20000`, 26 s): all 336357 Type II tuples (a ≤ b) of all odd n ≤ 20000: Ram_fin(B_{T'})
= predicted set, 2 ∉ Ram, odd cardinality, 0 tuples at odd squares (1 odd non-square n ≤ 20000 has none).
*Remark.* The ambient algebra `(−d, −n)` of QUATERNION_ES's Type II identity `(2ai + j)(2bi − j) = −e(1 + 2ck)` is the
algebra of the pair (x, y) = (2ai + j, 2bi − j), whose Gram matrix is `e·T'`; it differs from B_{T'} (it agrees for only
1460 of the first 3000 tuples in the check) — scaling a binary space changes its Hasse invariant. The T1-relevant Kudla
index is T', not eT'.

**Summary of §1 (the dictionary; answers brief item (1)).** Both certificate types are *Fourier indices of Kudla's
incoherent genus-2 weight-3/2 Siegel Eisenstein series for the modular curve* (Type I: `T(d, ab)`, det(2T) = ne; Type
II: `T' = [[f,1],[1,f']]`, det(2T') = 16c²dn), and the ES congruence conditions (`e | a + b`, resp. `f ≡ −1 (mod 4cd)`)
are exactly what clears every place except the primes of n from Diff(T). Oddness of Diff (= incoherence) then forces a
prime of n to odd exponent: **T1 ⟺ incoherence parity**. At n = p, Diff = {p}: certificates are supersingular points mod
p of the special cycle Z(T), i.e. lie in the support of the T-th coefficient of E'(τ, 0, Φ_𝒞) (geometric reading via the
cited Kudla/Gross–Keating/KRY identities).
