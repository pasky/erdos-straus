# EXSET_LINNIK — Linnik confinement for ES₅ / ES exceptional primes: circularity, escapes, and a Heath-Brown upgrade

*Wave z51, lane 2a, slug `linnik`. Brief: `/home/pasky/projects/math/z51briefs/2a_opus_linnik.md`. ES is OPEN; nothing
here claims it proved or disproved. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z51_linnik_*`, data `data/z51_linnik/`.*

## 0. Summary table

| # | claim | label | review |
|---|---|---|---|
| 1 | audit: what a "Linnik-type argument" is; which inputs it consumes | — | TBD |
| 2 | circularity / CRT-certification barrier (T2-barrier) | TBD | TBD |
| 3 | escape (a): bias instead of confinement; Heath-Brown upgrade of CAP_BOUNDED Thm 3.2 (T2-lite) | TBD | TBD |
| 4 | escape (b): p-dependent sequences | TBD | TBD |
| 5 | escape (c): supersets E′ ⊇ E_ES from the relaxation zoo | TBD | TBD |
| 6 | escape (d): reverse roles, forcing reach with full Type II classes | TBD | TBD |
| 7 | hostile reviews | — | — |
| 8 | remaining gap | Assessment | — |

## 1. Audit

### 1.1 What a "Linnik-type argument" is

**Definition 1.1 (Linnik datum).** A *Linnik datum* at scale X is a quadruple (N, a, Ψ, Δ):
* a fixed coefficient vector a = (a_n)_{n≤N} (independent of the moduli), ‖a‖² := Σ|a_n|²;
* for every prime p ≤ X a set Ψ_p of non-trivial characters of ℤ/p (additive tests) or of (ℤ/p)^× (multiplicative
  tests);
* a dual large-sieve constant Δ: Σ_{p≤X} Σ_{χ∈Ψ_p} |Σ_n a_n χ(n)|² ≤ Δ‖a‖² for every a in the admissible class.

The *bias* of p is β_p(a) := Σ_{χ∈Ψ_p} |Σ_n a_n χ(n)|²/‖a‖², and the *Linnik set* is B(a, T) := {p ≤ X : β_p(a) ≥ T}.
The instances in the brief:
* (L1) Linnik / Montgomery: additive tests, Δ = N + X² (Montgomery–Vaughan). If 𝒜 ⊂ [1, N] misses ω(p) classes mod p
  and a = 1_𝒜, then β_p ≥ |𝒜|ω(p)/(p − ω(p)) (Montgomery's local inequality).
* (L2) Elliott/Gallagher multiplicative large sieve: Ψ_p = all non-principal χ mod p, Δ ≍ N + X².
* (L3) Heath-Brown's quadratic large sieve (Acta Arith. 72 (1995) 235–275, Thm 1): Ψ_p = {χ_p}, χ_p(n) = (n/p), a
  supported on odd squarefree n, Δ = C_ε (XN)^ε (X + N).
* (L4) the Montgomery–Vaughan moment large sieve for real characters (as used by Lau–Wu, below): a = j-fold products of
  primes from a dyadic block, Ψ_p = {χ_p}; a special case of (L2)/(L3) in its input.
* (L5) Gallagher's larger sieve: not of this shape. Input: 𝒜 ⊂ [1, N] occupies ≤ ν_p classes mod p for p ∈ E; output
  |𝒜| ≤ (Σ_{p∈E} log p − log N)/(Σ_{p∈E} log p/ν_p − log N). It needs ν_p ≤ p^{1−δ}; for multiplicatively generated 𝒜
  this means 𝒜 mod p lies in a subgroup of index ≥ p^δ (characters of order ≥ 3 are involved).

**Lemma 1.2 (Linnik transfer; PROVED, trivial).** (i) #B(a, T) ≤ Δ/T. (ii) A Linnik-type argument for a set E of primes
in (X/2, X] is a datum plus the *input* E ⊂ B(a, T) (or #(E ∖ B(a, T)) ≤ X^{1−c}); its output is #E ≤ Δ/T (+ X^{1−c}).
The input is literally the pointwise implication

  **P(a, T):** every prime p ∈ (X/2, X] with β_p(a) < T satisfies ES₅(p) (resp. ES(p), U(p)).

(iii) A power saving with Δ ≥ X needs T ≥ X^c. Since |Σ a_n χ(n)|² ≤ #supp(a)·‖a‖², this forces |Ψ_p|·#supp(a) ≥ X^c; for
quadratic tests, #supp(a) ≥ X^c. ∎

So all ES-specific content of a Linnik argument sits in the containment E ⊂ B(a, T). The question of gate G3 is whether
that containment can be *derived* (from what is known about exceptional primes) without proving ES₅ pointwise.

### 1.2 Quadratic tests are periodic; Linnik is a level-free transfer

For p ≡ 1 (mod 4) and odd squarefree n, Jacobi reciprocity gives χ_p(n) = (n/p) = (p/n). So for quadratic tests β_p(a)
depends only on p mod lcm{4n : a_n ≠ 0}, and B(a, T) is a periodic set. Under Haar measure on the units x ≡ 1 (mod 8) of
Ẑ the symbols (x/n), n odd squarefree, are orthonormal, so

  E_Haar |Σ a_n (x/n)|² = ‖a‖²,   Haar(B(a, T)) ≤ 1/T.   (1.1)

The period lcm{4n} can be e^{(1+o(1))N}. Lemma 1.2(i) is therefore a **level-free transfer**: it counts the primes in a
periodic set of arbitrary period, but only for sets of the special shape B(a, T). CRT methods (z50's caps) need period
≤ N^{O(1)}. This is why z50 B §4.2 found that Linnik duality breaks the square floor: odd squares lie in B (all their
Jacobi symbols are +1), and Linnik counts B correctly although it has no "square floor". Tests of order ≥ 3 are not
periodic at all (§2.2).

### 1.3 What is known about the exceptional primes ("CRT information")

Let E_X be the ES₅-exceptional primes in (X/2, X], 𝔉₅ the refined W1/W2 certificate classes and 𝔘 the U classes
(EXSET_SIEVE_MASS Def 1.2). For every finite 𝔊 ⊂ 𝔉₅ with all moduli ≤ X/2, E_X ⊂ Ω(𝔊) := ℤ ∖ ∪𝔊 (the classes have
thresholds below their moduli). Same for U with 𝔘. We call the input of Lemma 1.2 **CRT-certified**
* *exactly*, if it is deduced as "p prime, p ∈ Ω(𝔊) ⟹ p ∈ B(a, T)" for some finite 𝔊, i.e. as a statement valid for
  all large primes of a periodic set;
* *approximately*, if #(E_X ∖ B) is bounded by a CRT majorant ν ≥ 1 on Ω(𝔊) ∖ B of level λ ≤ K log X, counted on
  [1, X] by equidistribution (the z50 framework).

### 1.4 Which barrier, which door

The Linnik door (z50 B §4.2; CONTEXT (2)) is the level-free transfer of §1.2. Gate G3 (an Assessment in z50) says the
input needs a pointwise implication. §2 proves the barrier with explicit scope: non-quadratic tests are never
CRT-certifiable (Prop 2.2); exact certification of quadratic tests is *false* on sparse prime sets (Cor 2.6, via
sterile "planes", which extend the r-generic sterile points of (J)70 from one non-residue to every sign pattern);
approximate certification is capped at the CRT exponent (Prop 2.8). §3 shows that bias (not confinement) suffices and
lowers the threshold of CAP_BOUNDED Thm 3.2 from A > 2 to A > 1 with Heath-Brown's sieve (T2-lite).

### 1.5 Literature (checked 2026-10-29, web search)

* Linnik (1941); Montgomery (1968) for (L1); Elliott for (L2); Heath-Brown (1995) for (L3); Gallagher (1971) for (L5).
* Duke–Kowalski: #{primitive χ mod q ≤ Q : χ(n) = 1 for n ≤ (log Q)^α} ≪ Q^{2/α+ε} (α > 2), the Linnik exponent.
* S. Baier, "A remark on the least n with χ(n) ≠ 1" (quoted by Lau–Wu): with Heath-Brown's sieve, n_{χ_d} ≤ (log|d|)^{1+ε}
  for almost all fundamental discriminants d. This is the least-non-residue analogue of §3's T2-lite.
* Y.-K. Lau and J. Wu, "On the least quadratic non-residue", IJNT (2008), Thm 1.1: #{d ≤ Q : χ_d(p) = 1 for all
  P < p ≤ 2P} ≪ Q e^{−c log Q/log log Q} uniformly for C log Q ≤ P ≤ (log Q)², via the Montgomery–Vaughan moment large
  sieve (their Lemma 2.1); Thm 1.2 (Graham–Ringrose): this is sharp at P ≍ log Q. Read from the author's PDF
  (hkumath.hku.hk/~yklau/p/34.pdf).
* No application of Linnik-type sieves with exceptional ES/ES₅ primes as moduli was found beyond CAP_BOUNDED Thm 3.2.

## 2. The circularity theorem (T2-barrier)

### 2.1 Strength of the input

By Lemma 1.2 the input is P(a, T). It implies the conclusion, since #B(a, T) ≤ Δ/T. It is formally stronger: it puts
ES₅ on an explicit set of primes whose complement has Haar density ≤ 1/T ≤ X^{−c} by (1.1), while the conclusion only
bounds the *size* of E_X. For quadratic tests it concerns profiles: if a is supported on squarefree products of a
prime set Π, B(a, T) is a union of atoms {p : (q/p) = ε_q, q ∈ Π}. The cheapest power-saving data are (§3): Π a set of
primes in a block (y/2, y], y = (log X)^A, A > 1 (Heath-Brown), and B = the profiles with a non-residue fraction θ
outside [1/2 − η, 1/2 + η], η = (log X)^{−κ}. So P(a, T) must prove ES₅ at *every* prime whose Π-profile is unbiased up
to η, i.e. on a set of relative density 1 − X^{−c}. The only pointwise statements of this type known are finite
coverings: ES holds when n₂(p) ≤ 13 (Π = {q ≤ 13}, Haar(B) = 2^{−5}). (J)70 shows that the one-non-residue version
(r-generic lines) has no finite covering for r ≥ 2.84·10⁶.

The rest of §2 asks whether the input can be **derived from CRT information** (§1.3).

### 2.2 Tests of order ≥ 3 are never CRT-certified

**Proposition 2.2 (PROVED: Chebotarev + Kummer theory; Schinzel's theorem on abelian radical extensions).** Let k ≥ 3,
S a finite set of primes, a supported on squarefree S-numbers, and U ⊂ Ẑ^× a non-empty union of unit classes mod L.
For a prime p ≡ 1 (mod k) put β^{(k)}_p(a) := Σ_{χ mod p, ord χ = k} |Σ a_n χ(n)|²/‖a‖². Among the primes p ∈ U with
p ≡ 1 (mod k), the average of β^{(k)}_p(a) (in Dirichlet density) is exactly φ(k). Hence those with β^{(k)}_p(a) ≤ 2φ(k)
have density ≥ 1/2 of them, and no statement "p ∈ U ⟹ β^{(k)}_p(a) ≥ T" with T > 2φ(k) holds for all large primes.

*Proof.* Fix a class r mod kL inside U with r ≡ 1 (mod k), F := ℚ(ζ_{kL}), K := F(S^{1/k}). For p ≡ r unramified in K the
values (n^{(p−1)/k} mod p)_n, read through a primitive k-th root of unity mod p, are the Frobenius action on
(n^{1/k})_n, and the order-k characters mod p are exactly χ(n) = ι(n^{(p−1)/k}) for the φ(k) faithful ι. By Chebotarev
(applied to K/ℚ, primes with prescribed restriction to F), Frob_p is equidistributed on Gal(K/F) over these p. By
Kummer theory over F, the character "σ ↦ σ(m^{1/k})/m^{1/k}" of Gal(K/F) is trivial iff m ∈ F^{×k}. For distinct
squarefree n, n′ the ratio m = n/n′ is a positive rational not in ℚ^{×2}; if m ∈ F^{×k} ⊂ (abelian field)^{×k}, then the
splitting field of x^k − m is abelian, and Schinzel's theorem gives m² ∈ ℚ^{×k}, impossible for k ≥ 3 (each prime of m
has exponent ±1). So E_p[χ(n)χ̄(n′)] = δ_{nn′} and the average of |Σ a_n χ(n)|² is ‖a‖² for each of the φ(k) characters. ∎

*Consequences.* (a) The larger sieve (L5) needs index ≥ p^δ subgroups, i.e. biases of order ≥ 3: no CRT-certified input
exists. (b) For (L1)/(L2) with a = 1_𝒜, 𝒜 ⊂ squarefree S-numbers prime to p, Parseval on (ℤ/p)^× splits the additive
bias as β_p^{add} = (p/(p−1))Σ_{χ≠χ₀}|Σ_𝒜 χ|²/|𝒜| − |𝒜|/(p−1); every order-≥3 part has average φ(k) over the primes of any
unit class. The only certifiable part is the quadratic one (order 2: ℚ(√q*) ⊂ ℚ(ζ_{4q}) is abelian, which is why
CAP_BOUNDED Thm 3.2 works). So from now on Ψ_p = {χ_p}.

### 2.3 Planes: the classes of 𝔉₅ ∪ 𝔘 through an "n = 1 twisted at Π" point

**Definition.** Let Π be a finite set of primes ≥ 11. The **Π-plane** is 𝒫_Π := {x ∈ Ẑ : x = 1 in ℤ_ℓ for every prime
ℓ ∉ Π (ℓ = 2 included), x_q ∈ ℤ_q^× for q ∈ Π}, with μ_Π := ∏_{q∈Π} Haar(ℤ_q^×). Its points are units, ≡ 1 (mod 8) and
≡ 1 (mod 840) (the Mordell-hard classes), and (x/q) = (x_q/q) can be any sign pattern ε ∈ {±1}^Π. For |Π| = 1 this is
the r-generic line of (J)54/(J)70.

**Lemma 2.3 (plane classes; PROVED, elementary; CERTIFIED by brute force).** Let h range over Π-numbers (all prime
factors in Π), m over Π-free numbers (2 allowed).
(a) A W1 class n ≡ −u (mod M), u | M + 1, with M = hm, meets 𝒫_Π iff m | u + 1. Then a := (u+1)/m and
    b := ((M+1)/u + 1)/m are integers with h = mab − a − b, i.e. (m, a, b) is a *word of h* (a, b ≥ 1, am, bm ≥ 2), and
    the class meets 𝒫_Π in the box {x ≡ −u (mod h)}. Conversely every word of h with m prime to Π gives such a class.
(b) A W2 class n ≡ −(u + v) (mod uv) with gcd(u, v) = 1 and uv = hm meets 𝒫_Π iff m | u + v + 1. Writing u = h₁m₁,
    v = h₂m₂ (h₁h₂ = h a unitary splitting, m₁m₂ = m) and D := (u + v + 1)/m, one has
    (Dm₁ − h₂)(Dm₂ − h₁) = D + h and D ≤ h + 1; the box is x ≡ −(u + v) (mod h). (W2 classes with gcd(u, v) > 1 contain
    no units.) Refined classes (v or t fixed mod 8 or 4) are subsets of these.
(c) Let L(h) be the number of W1 and W2 classes of (a), (b). Then
    L(h) ≤ 2 Σ_{a ≤ √(h+1)+1} τ(h + a) + 2^{ω(h)+1} Σ_{f ≤ √(2h+1)} (τ(f + h₁) + τ(f + h₂)) ≤ C_ε 2^{ω(h)} h^{1/2+ε}.

*Proof.* On 𝒫_Π, x ≡ 1 (mod m) and x mod h is free, so a class mod hm (gcd(h, m) = 1) meets 𝒫_Π iff its residue is
≡ 1 (mod m); the box is its residue mod h. (a) −u ≡ 1 (mod m) gives u = am − 1. Put e := (M + 1)/u = t. From
eu = hm + 1 ≡ 1 and u ≡ −1 (mod m) we get e ≡ −1, e = bm − 1, and (am − 1)(bm − 1) = hm + 1 is h = mab − a − b. The
converse reverses the steps. (b) D·m₁m₂ = h₁m₁ + h₂m₂ + 1; expanding (Dm₁ − h₂)(Dm₂ − h₁) = D²m₁m₂ − D(h₁m₁ + h₂m₂) + h
= D + h. D ≤ (h₁m₁ + h₂m₂ + 1)/(m₁m₂) ≤ h₁ + h₂ + 1 ≤ h + 1. (c) W1: ab | h + a + b gives b | h + a, and for a ≤ b,
a² − 2a ≤ h; so the ordered pairs are at most 2Σ_{a≤√(h+1)+1} τ(h + a), and (a, b) determines m. W2: with
f₁ := Dm₁ − h₂, f₂ := Dm₂ − h₁ ≥ 1 and f₁f₂ = D + h ≤ 2h + 1, the smaller factor f is ≤ √(2h+1), and D | f + h₂ (if
f = f₁) or D | f + h₁ (if f = f₂); then everything is determined. ∎
*Check* (`scripts/z51_linnik_plane.py`): for Π = {11, …, 31} and eight h (incl. 11·13·17, 13²·19), the W1 and W2
classes found from (a), (b) coincide with a direct enumeration over all moduli hm, m ≤ 3000.

**Lemma 2.4 (plane parity law; PROVED).** If a class of 𝔉₅ ∪ 𝔘 meets 𝒫_Π in the box c (mod h), then the Jacobi symbol
(c/h) = −1. In particular h is not a square, and a point x ∈ 𝒫_Π can lie in that class only if (x/h) = −1.
*Proof.* Take an integer n in the class with n ≡ 1 (mod 8m) and n ≡ c (mod h), coprime to uv (possible: the plane
point is a unit). Its word (t, u, v) has gcd(uv, n) = 1, hence gcd(u, v) = 1. W1: from (tu − 1)(tv − 1) = tn + 1 and
u(tv − 1) = n + v we get (M/n) = ((tv − 1)/n) = (u/n)(v/n) = (uv/n) with M = tu − 1. Since the class is a certificate
class, Theorem A (FOREST_DEEP_FABLE) gives (uv/n) = −1. Write M = 2^e M′: (2/n) = 1 (n ≡ 1 mod 8), so
(M/n) = (n/M′) = (n/h)(n/m′) = (c/h), using n ≡ 1 (mod m′). W2: (uv/n) = (n/(uv)′) = (c/h) likewise. U-certificates are
ES₅-certificates at n ≡ 1 (mod 8) (Theorem B). ∎
*Check:* asserted for every certificate box at h = q and h = qq′ in all runs of `scripts/z51_linnik_planemass.py`
(blocks up to y = 1600; 0 failures). The all-residue plane points are units that are squares at every prime, so Lemma
2.4 recovers the square base; the content is that for a sign pattern ε only the h with ε(h) := ∏ ε_q^{v_q(h)} = −1 matter.

### 2.4 Sterile planes and the barrier

**Theorem 2.5 (sterile planes; PROVED, elementary given Lemma 2.3).** For every ε ∈ (0, 1/8] there is η₀(ε) > 0 such
that for every finite set Π of primes ≥ 11 with σ_ε(Π) := Σ_{q∈Π} q^{−1/2+ε} ≤ η₀(ε),

  μ_Π{x ∈ 𝒫_Π : x lies in no class of 𝔉₅ ∪ 𝔘 (any modulus)} ≥ 1/2.

*Proof.* A box mod h has μ_Π-measure 1/φ(h). By Lemma 2.3(c) the covered measure is at most
Σ_{h>1 Π-number} C_ε 2^{ω(h)} h^{1/2+ε}/φ(h) ≤ C_ε(∏_{q∈Π}(1 + 2Σ_{k≥1} q^{k(1/2+ε)}/φ(q^k)) − 1). For q ≥ 11 and
ε ≤ 1/8 the inner sum is ≤ 2q^{−1/2+ε}, so the bound is ≤ C_ε(e^{4σ_ε} − 1) ≤ 8C_εσ_ε for σ_ε ≤ 1/4. Take
η₀ := min(1/4, 1/(16C_ε)). ∎

**Corollary 2.6 (exact CRT certification of quadratic Linnik confinement is false; PROVED).** Let Π be as in Theorem
2.5, a supported on squarefree Π-numbers, and T > 2. Then:
(i) there is x ∈ 𝒫_Π in no class of 𝔉₅ ∪ 𝔘 with |Σ a_n (x/n)|² ≤ 2‖a‖² < T‖a‖²;
(ii) for every finite 𝔊 ⊂ 𝔉₅ ∪ 𝔘 there are infinitely many primes p ∈ Ω(𝔊) with p ∉ B(a, T); so the implication
     "p prime, p ∈ Ω(𝔊) ⟹ p ∈ B(a, T)" is false, at every level.
*Proof.* (i) Under μ_Π the signs (x_q/q) are independent and uniform, so E|Σ a_n (x/n)|² = ‖a‖² (as in (1.1)). The
sterile set Z has μ_Π(Z) ≥ 1/2, so E[|Σ|²·1_Z] ≤ ‖a‖² forces some z ∈ Z with |Σ|² ≤ 2‖a‖². (ii) Let L := 8·lcm(moduli
of 𝔊)·∏_{q|n, a_n≠0} q. Membership in the classes of 𝔊 and in B(a, T) (via (p/n) = (n/p), p ≡ 1 mod 4) depends only on
p mod L, and z mod L is a unit class; Dirichlet's theorem gives infinitely many primes p ≡ z (mod L). ∎

**Remark 2.7 (the scope contains power-saving data).** Let A > 2, y := (log X)^A, Π := any ⌊η₀(y/2)^{1/2−ε}⌋ primes
in (y/2, y], 𝒜 := the products of r := ⌊log X/log y⌋ distinct elements of Π, a := 1_𝒜. Then |𝒜| ≥ (|Π|/r)^r =
X^{1/2−ε−1/A−o(1)}, and if every exceptional p were a residue of every q ∈ Π, then β_p = |𝒜| and Heath-Brown (L3) with
N = X would give #E_X ≪ X^{1+2ε′}/|𝒜| = X^{1/2+1/A+ε+2ε′+o(1)}, a power saving. Corollary 2.6 says that this confinement
(and any bias with T > 2) cannot be read off from avoidance of ES₅/U word classes, at any level. The
same holds for any Linnik datum supported on squarefree Π-numbers, every sign pattern being realised by sterile points.

**Proposition 2.8 (approximate certification inherits the CRT cap; PROVED given EXSET_SIEVE_MASS Thm 3.2).** Let Π, a
be as in Remark 2.7 and T ≥ X^c. Let ν = Σ_i c_i 1[n ≡ b_i (mod d_i)] ≥ 0 have period L | lcm d_i, level
λ = Σ_{ℓ | L, ℓ > W} log ℓ ≤ K log X, and suppose ν ≥ 1 on Ω(𝔊) ∖ B(a, T) for a finite 𝔊 ⊂ 𝔉₅ ∪ 𝔘 whose moduli divide
L. Then ν ≥ 1 on all of Ω(𝔊), and therefore log(1/Eν) ≤ Cλ^{2/3}(log λ)^{2/3}: the hybrid "Linnik for the biased primes +
CRT majorant for the rest" saves no more than the U/ES₅ CRT cap.
*Proof.* Fix r mod L in Ω(𝔊) (a union of classes mod L). Write n = n₁n₂ with n₁ | L, (n₂, L) = 1. Conditional on
x ≡ r (mod L), the symbols (x/n₂) are still orthonormal, so
E[|Σ a_n (x/n)|² | r] = Σ_{n₂} |Σ_{n₁} a_{n₁n₂}(r/n₁)|² ≤ 2^{ω_Π(L)}‖a‖², where ω_Π(L) := #{q ∈ Π : q | L}
(Cauchy–Schwarz; a = 1_𝒜 has at most 2^{ω_Π(L)} terms n₁ per n₂). Since L ≤ X^{K+o(1)} and Π ⊂ (y/2, y],
ω_Π(L) ≤ (K + o(1)) log X/log(y/2), so 2^{ω_Π(L)} = X^{o(1)} < T. By Markov, B(a, T) has relative Haar measure < 1 in the
fibre, so the fibre contains points of Ω(𝔊) ∖ B, where ν ≥ 1; ν is constant on the fibre. Hence ν ≥ 1 on Ω(𝔊), and
EXSET_SIEVE_MASS Thm 3.2 applies. ∎
(For ES and the ET classes the same fibre argument reduces to the 3/4 caps of (D)17–(D)29.)

### 2.5 Dense and multi-scale prime sets (CONJECTURE, with EVIDENCE)

Theorem 2.5 needs σ_ε(Π) small because Lemma 2.3(c) is a pointwise bound. On average the boxes are far fewer.
`scripts/z51_linnik_planemass.py y es5 haar` takes Π = all primes in (y/2, y], removes the single-coordinate boxes
(h = q; there are 8–35 of them per q, all non-residues, against (q − 1)/2 non-residues), and charges the pair boxes
(h = qq′) by the union bound under the product measure on what is left (`data/z51_linnik/planemass.jsonl`):

| y | #Π | certificate boxes per pair / (log h)² | pair mass | pair-sterile fraction (random search) |
|---:|---:|---:|---:|---:|
| 200 | 21 | 1.10 | 1.02 | 0.354 (2000 trials) |
| 400 | 32 | 1.11 | 0.77 | 0.472 (1000) |
| 800 | 61 | 1.11 | 0.92 | 0.409 (1000) |
| 1600 | 112 | 1.11 | 0.98 | 0.393 (1000) |

(U instead of ES₅ at y = 200: pair mass 0.88, sterile fraction 0.43.) The pair mass is flat in y, as predicted by
"boxes ≈ 1.1(log h)²" and Mertens: per block it is ≈ 1.1·(2 log y)²·(Σ_{q∈block} 1/q)²/2 ≈ 2.2(log 2)² ≈ 1.05. Squares h = q² carry
no box (Lemma 2.4). Triple boxes have mass O(1/log y).

**CONJECTURE 2.9 (dense planes).** There are c₀, C₀ > 0 such that for every set Π of primes ≥ 11,
μ_Π(sterile) ≥ c₀ exp(−C₀ (Σ_{q∈Π} log q/q)²). (A Lovász-local-lemma argument would give this from an averaged form of
Lemma 2.3(c): Σ_{q,q′} L(qq′)/(qq′) ≪ (Σ log q/q)², plus the pointwise single-coordinate bound.)
Consequence: Corollary 2.6 would hold for every Linnik datum supported on Π-numbers with Σ_{q∈Π} log q/q = o(√log X),
in particular for every polylog-smooth datum (Σ_{q≤(log X)^A} log q/q ≍ log log X). The argument of Corollary 2.6(i)
then gives |Σ|² ≤ e^{O((log log X)²)}‖a‖² = X^{o(1)}‖a‖² at a sterile point.

### 2.6 What is left: the input must be finite-range information

**Theorem 2.10 (circularity, scoped; PROVED as the conjunction of Lemma 1.2, Prop 2.2, Cor 2.6, Prop 2.8).** Let a
Linnik-type argument (L1)–(L5) give #E_X ≤ X^{1−c} for ES₅ (or U) exceptional primes. Then:
1. its input is the pointwise implication P(a, T) with T ≥ X^c (Lemma 1.2);
2. the parts of P(a, T) carried by characters of order ≥ 3 cannot follow from any statement valid for all large primes
   of a periodic set (Prop 2.2);
3. for quadratic tests with a supported on squarefree Π-numbers, σ_ε(Π) ≤ η₀ (this includes power-saving data, Remark
   2.7), P(a, T) cannot follow from avoidance of any finite family of ES₅/U word classes, of any level (Cor 2.6);
4. a CRT majorant of level ≤ K log X cannot replace it on the unbiased part (Prop 2.8).
Hence the input must use information about the primes p ≤ X that is not periodic. Near each sterile, unbiased plane
point z, the primes p ≡ z (mod L) exist below X once L ≤ cX^{1/5} (Linnik's theorem, Xylouris' exponent), lie outside
B(a, T), and avoid every 𝔉₅ ∪ 𝔘 class whose modulus divides L; so a proof of P(a, T) must find their certificates among
pivots whose modulus does not divide L. This is a statement about individual primes ≤ X (B2-type).

*Comparison with z50.* G3 was an Assessment; z50 B Thm 5.2 bounded certified depletion of the *integer* avoider mod
ℓ (marginal, U/ES₅); (J)70 gave sterile points with one non-residue for the ET classes. Theorem 2.10 is new in scope:
it covers every Linnik-type inequality of the brief (order ≥ 3 entirely; quadratic tests on sparse prime sets; bias as
well as confinement; the hybrid with CRT majorants). It does not cover: dense or multi-scale Π (Conjecture 2.9), ES
with the ET/Vaughan ratio classes for |Π| ≥ 2 (planes not computed for those families), and finite-range derivations.

## 3. Escape (a): partial / weighted confinement, and a Heath-Brown upgrade

### 3.1 Bias suffices

For a prime p and a finite set S of primes not containing p put σ_S(p) := Σ_{q∈S} (q/p).

**Theorem 3.1 (bias version of the Linnik bound; PROVED relative to Heath-Brown's quadratic large sieve).** Let A > 1,
0 ≤ κ < (A − 1)/2, y := (log X)^A, and S a set of s ≥ y/(5 log y) primes in (y/2, y]. Then

  #{p ≤ X prime : |σ_S(p)| ≥ 2(log X)^{−κ} s} ≤ X^{(1+2κ)/A + o(1)}.

*Proof.* r := ⌊log X/log y⌋. For an r-tuple of elements of S let n₀ be the squarefree kernel of its product, and
b_{n₀} := #{ordered r-tuples with kernel n₀}. Then b is supported on odd squarefree n₀ ≤ y^r ≤ X, and for p ∉ S,
Σ b_{n₀}(n₀/p) = σ_S(p)^r (squares contribute 1). By orthogonality of the sign characters on {±1}^S,
‖b‖² = E_ε(Σ_q ε_q)^{2r} ≤ (2r − 1)!! s^r ≤ (2rs)^r. Heath-Brown's Theorem 1 with M = N = X gives
Σ_{p≤X} |σ_S(p)|^{2r} ≤ C_ε X^{1+2ε}(2rs)^r. Primes with |σ_S(p)| ≥ 2ηs, η := (log X)^{−κ}, number at most
C_ε X^{1+2ε}(2rs)^r/(2ηs)^{2r} = C_ε X^{1+2ε}(r/(2η²s))^r. Here log(s/r) = (A − 1 + o(1)) log log X and
r = (1 + o(1)) log X/(A log log X), so (r/(2η²s))^r = X^{−(A−1−2κ)/A + o(1)}. ∎
*Check* (`scripts/z51_linnik_bias_check.py`, `data/z51_linnik/bias_check.txt`): the identity Σ b(n₀/p) = σ^r, the formula
‖b‖² = Eσ^{2r} and the (2r−1)!!s^r bound hold exactly for S = primes in (30, 60), r ≤ 4; the empirical large-sieve sums
are ≤ 0.05·(Q + N)‖b‖² for Q ≤ 10⁵.

*Reading.* Full confinement (σ_S = s) is not needed. A non-residue fraction θ_p ≤ 1/2 − (log X)^{−κ} on one dyadic block
suffices, for any κ < (A − 1)/2. Under Haar measure σ_S/s has standard deviation s^{−1/2} = (log X)^{−A/2+o(1)}, so the
required bias is (log X)^{1/2+δ} standard deviations: the Linnik set is still a superpolynomially rare set of profiles
(Haar density ≤ exp(−(log X)^{1+2δ'})), and §2's barrier applies to it unchanged (Cor 2.6 needs only T > 2).

### 3.2 T2-lite: the cap threshold of CAP_BOUNDED Thm 3.2 drops from A > 2 to A > 1

**Corollary 3.2 (PROVED relative to Heath-Brown's Theorem 1, the PNT for primes ≡ 3 (mod 4), CAP_DOWN Thm 1.2/Prop 1.3
via CAP_BOUNDED Lemma 3.1).** For every A > 1,

  #{p ≤ X prime : e*(p) > (log X)^A/4} ≤ X^{1/A + o(1)}.

This improves CAP_BOUNDED Thm 3.2(a) (X^{2/A+o(1)}, non-trivial only for A > 2) in both range and exponent.
*Proof.* By CAP_BOUNDED Lemma 3.1, e*(p) > (log X)^A/4 implies p ≡ 1 (mod 8) and q₃(p) > (log X)^A =: y, i.e. (q/p) = +1
for every prime q ≡ 3 (mod 4), q ≤ y; and such p exceed y. Take S := the primes q ≡ 3 (mod 4) in (y/2, y]
(s ≥ y/(5 log y) for large X by the PNT in progressions). Then σ_S(p) = s, and Theorem 3.1 with κ = 0 gives the bound. ∎

*Remarks.* (1) The argument is Baier's least-non-residue argument (§1.5) transplanted to q₃(p); the novelty is only the
application to the exponent cap. (2) The route through q₃ cannot go below A = 1: 𝒫((log X)^A) (all q ≡ 3 (4) up to
(log X)^A residues) has relative Haar density 2^{−π(y;4,3)} = X^{−o(1)} for A < 1, and CONDITIONALLY on GRH it contains
2^{−π(y;4,3)}π(X) + O(√X log²X) = X^{1−o(1)} primes (expand ∏(1 + (q/p))/2 into characters). Lau–Wu Thm 1.2
(Graham–Ringrose) shows the analogous least-non-residue statement is sharp at y ≍ log X unconditionally along a
sequence. Going below A = 1 needs a forcing mechanism other than the least forced window.
(3) Part (b) of CAP_BOUNDED Thm 3.2 (polylog exceptions above p^ε) is not improved: Heath-Brown's X^ε loss is too
large there.

### 3.3 Can a bias be forced without pointwise forcing?

* **Not by CRT certification.** Corollary 2.6 needs only T > 2, so it rules out exact certification of any bias, and
  Proposition 2.8 any approximate certification at level O(log X), for data on sparse prime sets.
* **Heuristically yes, with room — a change from z50.** With Heath-Brown, the Linnik route needs (bias on) primes
  q ≈ (log X)^{1+δ}, not (log X)^{2+δ}. Lane B's per-prime forcing heuristic (EXSET_SIEVE_MASS §4.2) covers all
  non-residues mod q at a *generic* profile once (log p)² ≳ q log q, i.e. up to q ≈ (log p)²/log log p. So in the Haar
  model an exceptional p would have to avoid ≍ (log p)²/q labels at each non-residue q ≤ (log p)^{2−δ}, and its
  conditional profile is tilted towards residues by a factor e^{−c(log p)^{δ}} per such q: far more bias than Theorem 3.1
  needs. z50 called the Linnik route "just short" (reach (log p)²/log log p against (log X)^{2+δ}); with Theorem 3.1 the
  heuristic reach exceeds the requirement by (log X)^{1−δ}. (Assessment.)
* **Where the heuristic fails: exactly at the planes.** On 𝒫_Π the labels at a non-residue q are the words of q alone
  (Lemma 2.3: m = Π-free part), about 1.1(log q)² of them, against (log M)² + log q·log M at a generic profile. So the
  per-prime forcing reach is zero at plane points. This is why sterile planes exist (Thm 2.5) and why the forcing must be
  pointwise: it needs the Π-free coordinates of p to be generic, which is a property of the actual prime, not of a
  congruence class.

## 4. Escape (b): p-dependent sequences

A p-dependent Linnik argument uses a vector a^{(p)} for each p ∈ E. With no structure there is no large sieve at all:
a^{(p)} := conj χ_p restricted to [1, N] gives |⟨a^{(p)}, χ_p⟩|² = N‖a^{(p)}‖² for every p. The usable structure is
low dimension.

**Lemma 4.1 (dimension loss; PROVED).** Let V be a K-dimensional space of coefficient vectors and suppose
β_p(a^{(p)}) ≥ T with a^{(p)} ∈ V ∖ {0} for every p ∈ E. Then #E ≤ KΔ/T, where Δ is the large-sieve constant valid on V.
*Proof.* Take an orthonormal basis f₁, …, f_K of V. Cauchy–Schwarz gives |⟨a^{(p)}, χ⟩|² ≤ ‖a^{(p)}‖²Σ_k|⟨f_k, χ⟩|², so
T ≤ Σ_k β_p(f_k). Summing over p ∈ E and using Σ_p β_p(f_k) ≤ Δ for each k gives T·#E ≤ KΔ. ∎
The loss K is sharp in general (V spanned by K vectors each concentrated on one Linnik set). Hybrid large sieves are
the same mechanism with a continuous family: Gallagher's Σ_q Σ_χ ∫_{−T₀}^{T₀}|Σ a_n χ(n) n^{it}|² dt ≪ (N + Q²T₀)‖a‖²
charges archimedean twists n^{it}, |t| ≤ T₀, by a factor ≍ T₀ (Sobolev: max_{|t|≤T₀} is controlled by the integral of
the function and its derivative).

**Proposition 4.2 (the three kinds of p-dependence; PROVED).**
(i) *Dependence through p mod L, L ≤ X^K.* Then K ≤ φ(L) and the argument is a fibred datum: on the fibre p ≡ c (mod L)
    one uses a^{(c)}. If the a^{(c)} are supported on squarefree Π-numbers with Π as in Theorem 2.5, Corollary 2.6 applies
    to the fibre of the sterile plane point z (all Π-free coordinates of z are 1), with the threshold T replaced by
    2·2^{ω_Π(L)} (the conditional second moment of Prop 2.8's proof). So fibring does not escape §2.
(ii) *Archimedean twists a_n n^{it_p}, |t_p| ≤ T₀.* The Haar computation (1.1) is unchanged for each fixed t;
    E_Haar max_{|t|≤T₀}|Σ a_n (x/n) n^{it}|² ≪ (1 + T₀ log N)‖a‖² (Sobolev in t), so Corollary 2.6 holds with T > C T₀ log N,
    while the hybrid sieve's Δ grows by the same factor T₀.
(iii) *Dependence through the word data of p* (e.g. 𝒜_p := values or divisors of the word forms n + u that p "sees").
    Such maps are injective on primes up to bounded multiplicity (p + 1 ∈ 𝒜_p, or the divisor set of p + 1 and p + 2,
    determines p up to O(1) choices), so K ≥ c·#E and Lemma 4.1 gives #E ≤ CΔ#E/T: nothing unless T > CΔ ≥ X; but for
    quadratic tests T ≤ #supp(a) ≤ N, and Δ ≥ N. ∎
*Exact blocking lemma for (b).* A p-dependent datum helps only if its dependence has ≤ X^{c} states (Lemma 4.1); such a
datum is a fibred datum, covered by §2 (Prop 4.2(i)). The word-form sequences have ≍ #E states and give nothing.

## 5. Escape (c): supersets E′ ⊇ E_ES

(placeholder)

## 6. Escape (d): reverse roles

(placeholder)

## 7. Hostile reviews

(placeholder)

## 8. Remaining gap

(placeholder)
