# EXSET_LINNIK — Linnik confinement for ES₅ / ES exceptional primes: circularity, escapes, and a Heath-Brown upgrade

*Wave z51, lane 2a, slug `linnik`. Brief: `/home/pasky/projects/math/z51briefs/2a_opus_linnik.md`. ES is OPEN; nothing
here claims it proved or disproved. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z51_linnik_*`, data `data/z51_linnik/`.*

## 0. Summary table

| # | claim | label | review |
|---|---|---|---|
| 1.2 | Linnik transfer: the input of every (L1)–(L4) argument is the containment E ⊂ B(a, T) (exact: the pointwise implication P(a, T); approximate: up to a remainder); B is periodic for quadratic tests, Haar(B) ≤ 1/T; Linnik is a level-free transfer | PROVED (trivial) | R1: MINOR, repaired |
| 2.2 | fixed-order (k ≥ 3) character biases of squarefree-supported data have mean exactly φ(k) over the primes of any unit class: never CRT-certified (Chebotarev + Kummer) | PROVED | R1: MAJOR (coset), repaired; consequences for the larger sieve / full Montgomery withdrawn |
| 2.3–2.4 | **plane lemma**: the native ES₅/U word classes meeting the Π-plane (x = 1 off Π) are the words of the Π-part h (W1) and an explicit W2 family; **plane parity law**: their boxes c mod h have (c/h) = −1 | PROVED; CERTIFIED (brute force, two independent scripts) | R1: SOUND after D ≤ h + 2 and coprimality repairs |
| **2.5–2.6** | **sterile sparse planes**: for Σ_{q∈Π} q^{−1/2+ε} ≤ η₀, Haar-half of the Π-plane, and half of every sign cell, avoids every ES₅/U class; hence **no avoidance-of-word-classes argument, at any level, certifies quadratic Linnik confinement or bias (T > 2) on sparse Π** — though such data would give a power saving (Rem 2.7) | PROVED | R1: SOUND (exact, infinite-range scope); per-cell version added |
| 2.8 | hybrid "Linnik for biased + CRT majorant for the rest" with bounded whole-period level is capped at the U/ES₅ CRT exponent | PROVED (given EXSET_SIEVE_MASS Thm 3.2) | R1: MAJOR (level definition), rescoped to whole-period level |
| 2.9 | dense planes sterile with probability ≥ c₀e^{−C₀(Σ log q/q)²} (would extend 2.6 to all polylog-smooth data) | CONJECTURE; EVIDENCE: pair mass 0.77–1.02 flat for y = 200…1600, 28% sterile incl. triples at y = 200 | R1: evidence wording repaired |
| 2.10 | scoped conjunction of the four obstructions (A)–(D); the first-draft universal circularity theorem is **withdrawn** | PROVED (conjunction) | R1: FATAL as first stated → rescoped |
| **3.1** | **bias suffices**: #{p ≤ X : \|Σ_{q∈S}(q/p)\| ≥ (log X)^{−κ}s} ≪ X^{(1+2κ)/A+δ} for a block S at (log X)^A, A > 1, κ < (A−1)/2 | PROVED rel. Heath-Brown (1995) | R1: kernel/norm SOUND; threshold repaired |
| **3.2** | **T2-lite**: #{p ≤ X : e*(p) > (log X)^A/4} ≪ X^{1/A+δ} for every A > 1 (CAP_BOUNDED Thm 3.2(a): X^{2/A}, A > 2); the q₃-route cannot go below A = 1 (GRH) | PROVED rel. Heath-Brown; CONDITIONAL (GRH) for the limit | R1: proof repaired, exponent confirmed |
| 3.3 | with Heath-Brown the Linnik requirement (log X)^{1+δ} lies inside the heuristic forcing reach (z50: "just short") | Assessment | R1: wording repaired |
| 4.1–4.2 | p-dependent data cost their dimension; fibred and archimedean-twisted data reduce to §2; injective word-form data give nothing | PROVED | R2 |
| 5.1–5.2 | zoo relaxations have the wrong orientation (E_R ⊂ E_ES); ES₅-defined supersets are CRT avoiders (colour is not free) | PROVED | R2 |
| 5.3 | window strengthening: the window lottery is near-independent and its failures are residue-biased (0.34–0.38 vs 0.50, 33 663 primes near 10⁸); power saving for ES CONDITIONAL on the pointwise (WL_A) | EVIDENCE; CONDITIONAL | R2 |
| 6.1 | ES Type II ratio classes: forcing labels per q ≈ 0.034(log p)³ (cubic supply confirmed, p = 10⁵…10⁸); collapse to ≈ 40 at plane points | EVIDENCE | R2 |
| 6.2 | fibred reverse-role Montgomery sieve with CRT-certified depletion is capped | PROVED (given LS Cor 2.2 + EXSET_SIEVE_MASS Thm 3.2) | R2 |
| 8 | remaining gap; T2-full not reached | Assessment | — |

**Bottom line (Assessment).** T2-full is not reached. T2-lite is reached in the form the CONTEXT names (cap threshold
A > 2 → A > 1, exponent 2/A → 1/A). For T2-barrier the lane proves scoped obstructions, strictly beyond z50's G3
Assessment: fixed-order higher characters are never CRT-certified; quadratic confinement or bias on sparse prime sets
cannot be certified by native ES₅/U word classes at any level (multi-coordinate sterile planes with every sign pattern);
bounded-level hybrids and fibred reverse-role sieves inherit the CRT cap. Heath-Brown moves the Linnik requirement from
(log X)^{2+δ} to (log X)^{1+δ}, inside the heuristic forcing reach, so the route is heuristically consistent with room;
what is missing is a non-CRT input that handles the non-generic (plane-like) primes.

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
* (L5) Gallagher's larger sieve: not of this shape. If 𝒜 ⊂ [1, N] occupies ≤ ν_p classes mod p for p ∈ E, then
  |𝒜| ≤ (Σ_{p∈E} log p − log N)/(Σ_{p∈E} log p/ν_p − log N) when the denominator is positive. Used with E ⊂ (X/2, X] as
  the moduli to bound #E, it gives: if |𝒜| > 2ν and ν_p ≤ ν on E, then #E ≤ 2ν log N/log(X/2); a power saving needs
  ν ≤ X^{1−c}, i.e. 𝒜 confined to ≤ X^{1−c} classes mod every exceptional p (subgroups of index ≥ X^{c} when 𝒜 is
  multiplicatively generated). (In its primal use the larger sieve works with ν_p ≈ p/2, e.g. for the squares; R1.)

**Lemma 1.2 (Linnik transfer; PROVED, trivial; repaired after R1).** Let a ≠ 0. (i) #B(a, T) ≤ Δ/T. (ii) *Exact form:* a
Linnik-type argument for a set E of primes in (X/2, X] (data (L1)–(L4)) is a datum plus the input E ⊂ B(a, T), with
output #E ≤ Δ/T. The input is literally the pointwise implication

  **P(a, T):** every prime p ∈ (X/2, X] with β_p(a) < T satisfies ES₅(p) (resp. ES(p), U(p)).

*Approximate form:* the input #(E ∖ B(a, T)) ≤ R gives #E ≤ Δ/T + R; then P(a, T) is only required outside a remainder
set of size R. (iii) If the bound Δ/T ≤ X^{1−c} is used with Δ ≥ X, then T ≥ X^c; since |Σ a_n χ(n)|² ≤ #supp(a)·‖a‖²,
as soon as one prime has to satisfy β_p ≥ T this forces |Ψ_p|·#supp(a) ≥ X^c (for quadratic tests, #supp(a) ≥ X^c). ∎

So the ES-specific content of a Linnik argument sits in the containment E ⊂ B(a, T) (exact or up to a remainder). The
question of gate G3 is whether that containment can be *derived* without proving ES₅ pointwise.

### 1.2 Quadratic tests are periodic; Linnik is a level-free transfer

For p ≡ 1 (mod 4) and odd squarefree n, Jacobi reciprocity gives χ_p(n) = (n/p) = (p/n). So for quadratic tests β_p(a)
depends only on p mod lcm{4n : a_n ≠ 0}, and B(a, T) is a periodic set. Under Haar measure on the units x ≡ 1 (mod 8) of
Ẑ the symbols (x/n), n odd squarefree, are orthonormal, so

  E_Haar |Σ a_n (x/n)|² = ‖a‖²,   Haar(B(a, T)) ≤ 1/T.   (1.1)

The period lcm{4n} can be e^{(1+o(1))N}, and a single term (x/n) already has modulus n up to N. Lemma 1.2(i) is therefore
a **level-free transfer**: it counts the primes in a periodic set of arbitrary period and per-term level, but only for
sets of the special shape B(a, T). The z50 CRT caps charge the level log d of each summand modulus d and are evaluated at
level ≤ K log N (R1: per-term level, not total period). This is why z50 B §4.2 found that Linnik duality breaks the square
floor: for coherent non-negative data (e.g. a = 1_𝒜) the odd squares coprime to supp(a) have all symbols +1 and lie in B,
yet Linnik counts B correctly. (For signed data squares need not lie in B.) Tests of order ≥ 3 are not periodic at all
(§2.2).

### 1.3 What is known about the exceptional primes ("CRT information")

Let E_X be the ES₅-exceptional primes in (X/2, X], 𝔉₅ the refined W1/W2 certificate classes and 𝔘 the U classes
(EXSET_SIEVE_MASS Def 1.2). For every finite 𝔊 ⊂ 𝔉₅ with all moduli ≤ X/2, E_X ⊂ Ω(𝔊) := ℤ ∖ ∪𝔊 (the classes have
thresholds below their moduli). Same for U with 𝔘. We call the input of Lemma 1.2 **CRT-certified**
* *exactly*, if it is deduced as "p prime, p ∈ Ω(𝔊) ⟹ p ∈ B(a, T)" for some finite 𝔊, i.e. as a statement valid for
  all large primes of a periodic set;
* *approximately*, if #(E_X ∖ B) is bounded by a non-negative CRT majorant ν ≥ 1 on Ω(𝔊) ∖ B_J (B_J the periodic
  extension of B, §2.4) of level ≤ K log X, counted on [1, X] by equidistribution (the z50 framework).

### 1.4 Which barrier, which door

The Linnik door (z50 B §4.2; CONTEXT (2)) is the level-free transfer of §1.2. Gate G3 (an Assessment in z50) says the
input needs a pointwise implication. §2 proves four scoped obstructions (Theorem 2.10): fixed-order (k ≥ 3) tests are
never CRT-certified (Prop 2.2); exact certification of quadratic tests is *false* on sparse prime sets (Cor 2.6, via
sterile "planes", which extend the r-generic sterile points of (J)70 from one non-residue to every sign pattern, for
the native ES₅/U classes); hybrids with a CRT majorant of bounded whole-period level are capped (Prop 2.8); fibred
reverse-role sieves are capped (Prop 6.1). The first draft claimed a universal circularity theorem; R1 found it FATAL as
stated, and it is withdrawn. §3 shows that bias (not confinement) suffices and lowers the threshold of CAP_BOUNDED
Thm 3.2 from A > 2 to A > 1 with Heath-Brown's sieve (T2-lite).

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

## 2. Certification barriers (T2-barrier, scoped)

### 2.1 Strength of the input

In the exact form the input is P(a, T). It implies the conclusion, since #B(a, T) ≤ Δ/T, and it is formally stronger: it
puts ES₅ on an explicit set of primes whose complement has (periodic, Haar) density ≤ 1/T ≤ X^{−c} by (1.1), while the
conclusion only bounds the *size* of E_X. In the approximate form only #(E_X ∖ B) ≤ X^{1−c} is needed. For quadratic
tests with a supported on squarefree products of primes from a set Π, B(a, T) is a union of atoms
{p : (q/p) = ε_q, q ∈ Π}. The cheapest power-saving data (§3): Π a dyadic block (y/2, y], y = (log X)^A, A > 1
(Heath-Brown), and B ⊇ the profiles whose non-residue fraction θ satisfies |θ − 1/2| ≥ η/2, η = (log X)^{−κ}. So P(a, T)
must prove ES₅ at every prime whose Π-profile is unbiased up to η/2: relative density 1 − X^{−c}. The only pointwise
statements of this type known are finite coverings (ES when n₂(p) ≤ 13: Π = {q ≤ 13}, Haar(B) = 2^{−5}); (J)70 shows
that the one-non-residue version (r-generic lines) has no finite covering for r ≥ 2.84·10⁶.

The rest of §2 asks whether the input can be **derived from CRT information** (§1.3), and proves four scoped
obstructions.

### 2.2 Fixed-order tests of order k ≥ 3 are never CRT-certified

**Proposition 2.2 (PROVED: Chebotarev + Kummer theory; repaired after R1).** Let k ≥ 3, S a finite set of primes,
a ≠ 0 supported on squarefree S-numbers, and C a unit class modulo L′ with k | L′ and C ⊂ {p ≡ 1 (mod k)}. For primes
p ∈ C put β^{(k)}_p(a) := Σ_{χ mod p, ord χ = k} |Σ a_n χ(n)|²/‖a‖². The mean of β^{(k)}_p(a) over the primes p ∈ C (in
relative natural density) is exactly φ(k). Hence no statement "p ∈ C ⟹ β^{(k)}_p(a) ≥ T" with T > φ(k) holds for all
large primes, and the primes p ∈ C with β^{(k)}_p(a) ≤ 2φ(k) have relative density ≥ 1/2.

*Proof.* Put F := ℚ(ζ_{L′}), K := F(α_q : q ∈ S) with α_m the positive real k-th root of m, G := Gal(K/ℚ), H := Gal(K/F).
For σ ∈ G and a positive squarefree S-number (or ratio) m, σ(α_m) = ψ_m(σ)α_m with ψ_m(σ) ∈ μ_k, multiplicative in m.
The primes of C have Frobenius in the coset g₀H fixed by C; since Gal(F/ℚ) is abelian, g₀H is a union of conjugacy
classes. As g₀ ≡ p ≡ 1 (mod k) on μ_k, ψ_m(g₀h) = ψ_m(g₀)ψ_m(h). *Kummer step:* for squarefree n ≠ n′ and m := n/n′,
ψ_m is non-trivial on H. Otherwise α_m ∈ F, so ℚ(α_m) ⊂ F is abelian, hence Galois and real; its conjugates are real
roots of x^k − m, i.e. ±α_m, so α_m² ∈ ℚ and m² ∈ ℚ^{×k}, impossible for k ≥ 3 since every prime of m has exponent ±1
(this is the special case of Schinzel's theorem on abelian binomials that we need). *Identification:* for 𝔭 | p with
Frobenius σ, ψ_n(σ) ≡ n^{(p−1)/k} (mod 𝔭), and reduction maps μ_k isomorphically onto the k-th roots of unity of F_p; so
the order-k characters mod p are n ↦ ψ_n(σ)^t, t ∈ (ℤ/k)^×, and β^{(k)}_p(a) = Φ(σ) :=
Σ_t |Σ a_n ψ_n(σ)^t|²/‖a‖², a conjugacy-invariant function (conjugation permutes the t). Chebotarev gives the relative
density mean (1/|H|)Σ_{h∈H} Φ(g₀h) = Σ_t Σ_{n,n′} a_n ā_{n′} ψ_{n/n′}(g₀)^t mean_h ψ_{n/n′}(h)^t/‖a‖² = φ(k), the
off-diagonal means vanishing because ψ_{n/n′}^t is a non-trivial character of H. ∎

*Scope (R1).* (i) Squarefree support is essential: with a = 1 on {q₁², …, q_M²} every quartic character has
χ(q_i²) = (q_i/p) = 1 on p ≡ 1 (mod 8q₁⋯q_M), so β^{(4)}_p = 2M is CRT-certified. (ii) Only a fixed order k (or a fixed
finite set of orders) is covered; aggregates over all characters of order ≥ 3 have trivial baselines (a = δ₁ gives
p − 3) and are not treated. (iii) In particular Montgomery's additive tests, the full Elliott sieve and Gallagher's
larger sieve (L5) are **not** covered. Order 2 is different in kind: (q*/p) is a Dirichlet character in p
(ℚ(√q*) ⊂ ℚ(ζ_{4q})), which is why CAP_BOUNDED Thm 3.2 works; §§2.3–2.4 treat it.

### 2.3 Planes: the classes of 𝔉₅ ∪ 𝔘 through an "n = 1 twisted at Π" point

**Definition.** Let Π be a finite set of primes ≥ 11. The **Π-plane** is 𝒫_Π := {x ∈ Ẑ : x = 1 in ℤ_ℓ for every prime
ℓ ∉ Π (ℓ = 2 included), x_q ∈ ℤ_q^× for q ∈ Π}, with μ_Π := ∏_{q∈Π} Haar(ℤ_q^×). Its points are units, ≡ 1 (mod 8) and
≡ 1 (mod 840) (the Mordell-hard classes), and (x/q) = (x_q/q) can be any sign pattern ε ∈ {±1}^Π. For |Π| = 1 this is
the r-generic line of (J)54/(J)70.

**Lemma 2.3 (plane classes; PROVED, elementary; CERTIFIED by brute force; repaired after R1).** Let h range over
Π-numbers > 1 (all prime factors in Π), m over Π-free numbers (2 allowed).
(a) A W1 class n ≡ −u (mod M), u | M + 1, M = hm ≥ 2, meets 𝒫_Π iff m | u + 1. Then a := (u+1)/m and
    b := ((M+1)/u + 1)/m are integers with h = mab − a − b, i.e. (m, a, b) is a *word of h* (a, b ≥ 1, am, bm ≥ 2), and
    the class meets 𝒫_Π in the box {x ≡ −u (mod h)}. Conversely every word of h with m prime to Π gives such a class.
(b) A W2 class n ≡ −(u + v) (mod uv) with gcd(u, v) = 1 and uv = hm meets 𝒫_Π iff m | u + v + 1. Writing u = h₁m₁,
    v = h₂m₂ (h₁h₂ = h a unitary splitting, m₁m₂ = m) and D := (u + v + 1)/m, one has
    (Dm₁ − h₂)(Dm₂ − h₁) = D + h, both factors ≥ 1, and D ≤ h₁ + h₂ + 1 ≤ h + 2 (equality for u = 1, v = h); the box is
    x ≡ −(u + v) (mod h). W2 classes with gcd(u, v) > 1 contain no units.
(c) Refinements (v mod 8, or t mod 4) are 2-adic; the plane fixes the 2-adic coordinate, so each W1/W2 class has at most
    one compatible refined intersection, with the same box. Let L(h) be the number of W1 and W2 classes of (a), (b). Then
    L(h) ≤ 2 Σ_{a ≤ √(h+1)+1} τ(h + a) + Σ_{h₁h₂=h unitary} Σ_{f ≤ √(2h+2)} (τ(f + h₁) + τ(f + h₂)) ≤ C_ε 2^{ω(h)} h^{1/2+ε}.

*Proof.* On 𝒫_Π, x ≡ 1 (mod m) and x mod h is free, so a class mod hm (gcd(h, m) = 1) meets 𝒫_Π iff its residue is
≡ 1 (mod m); the box is its residue mod h. (a) −u ≡ 1 (mod m) gives u = am − 1. Put t := (M + 1)/u. From tu = hm + 1 ≡ 1
and u ≡ −1 (mod m) we get t ≡ −1, t = bm − 1, and (am − 1)(bm − 1) = hm + 1 is h = mab − a − b. The converse reverses
the steps. (b) Dm₁m₂ = h₁m₁ + h₂m₂ + 1; expanding, (Dm₁ − h₂)(Dm₂ − h₁) = D²m₁m₂ − D(h₁m₁ + h₂m₂) + h = D + h. Also
Dm₁ − h₂ = (h₁m₁ + 1)/m₂ > 0, symmetrically, and D ≤ (h₁m₁ + h₂m₂ + 1)/(m₁m₂) ≤ h₁ + h₂ + 1. (c) W1: ab | h + a + b gives
b | h + a, and for a ≤ b, a² − 2a ≤ h; (a, b) determines m. W2: for each unitary splitting, the smaller of the two
factors is f ≤ √(D + h) ≤ √(2h + 2), and D divides f + h₂ (if f = Dm₁ − h₂) or f + h₁; then everything is determined. ∎
*Checks.* `scripts/z51_linnik_plane.py`: for Π = {11, …, 31} and eight h (incl. 11·13·17, 13²·19) the classes from (a),
(b) coincide with a direct enumeration over all moduli hm, m ≤ 3000. R1 re-derived (a) and the parity law below with
an independent script from the definitions (`reviews/z51-linnik-review-1-check.py`, Π = {11, …, 23}, m ≤ 120, h incl.
1, 121, 143, 2431): all assertions pass.

**Lemma 2.4 (plane parity law; PROVED; repaired after R1).** If a class of 𝔉₅ ∪ 𝔘 meets 𝒫_Π in the box c (mod h), then
the Jacobi symbol (c/h) = −1. In particular h ≠ 1 and h is not a square, and a point x ∈ 𝒫_Π can lie in that class only
if (x/h) = −1.
*Proof.* Choose (CRT) a large integer n in the refined class with n ≡ 1 (mod 8m′), n ≡ c (mod h) (m′ the odd part of m),
and, for W1, gcd(n, u) = 1 (possible since gcd(u, M) = 1). For W1, Mv = n + u then forces gcd(n, v) = 1, and a common
divisor of u and v divides n, so gcd(u, v) = 1; for W2 the unit residue mod uv gives the same. W1: from
(tu − 1)(tv − 1) = tn + 1 and u(tv − 1) = n + v, the Jacobi symbols at n satisfy (M/n) = ((tv − 1)/n) = (u/n)(v/n) =
(uv/n), M = tu − 1. The class is a certificate class, so n's word has a slot ≡ 0 (mod 4), and Theorem A
(FOREST_DEEP_FABLE; stated for odd n ≡ 1 (4) with gcd(uv, n) = gcd(u, v) = 1, composite n allowed) gives (uv/n) = −1.
Writing M = 2^e M′: (2/n) = 1 and reciprocity give (M/n) = (n/M′) = (n/h)(n/m′) = (c/h). W2: (uv/n) = (c/h) likewise.
For 𝔘 we need the slot directly (Theorem B is stated for primes): an endpoint ≡ 0 (mod 4) is a slot; if u ≡ 7 (mod 8)
then v(tu − 1) = n + u ≡ 0 (mod 8), so v or tu − 1 is ≡ 0 (mod 4). ∎
*Check:* asserted for every certificate box at h = q and h = qq′ in all runs of `scripts/z51_linnik_planemass.py`
(blocks up to y = 1600; 0 failures), and by R1 (above). The all-residue plane points are squares at every prime, so
Lemma 2.4 recovers the square base; the content is that for a sign pattern ε only the h with ε(h) := ∏ ε_q^{v_q(h)} = −1
carry boxes.

### 2.4 Sterile planes and the exact-certification barrier

**Theorem 2.5 (sterile planes; PROVED, elementary given Lemmas 2.3–2.4).** For every ε ∈ (0, 1/8] there is
η₀(ε) > 0 such that for every finite set Π of primes ≥ 11 with σ_ε(Π) := Σ_{q∈Π} q^{−1/2+ε} ≤ η₀(ε):
(a) μ_Π{x ∈ 𝒫_Π : x lies in no class of 𝔉₅ ∪ 𝔘 (any modulus)} ≥ 1/2;
(b) for every sign pattern ε ∈ {±1}^Π, the same holds for the uniform measure on the cell {x ∈ 𝒫_Π : (x_q/q) = ε_q}.
*Proof.* h = 1 carries no box (Lemma 2.4). (a) A box mod h has μ_Π-measure 1/φ(h). By Lemma 2.3(c) the covered measure
is ≤ Σ_{h>1} C_ε 2^{ω(h)} h^{1/2+ε}/φ(h) ≤ C_ε(∏_{q∈Π}(1 + 2Σ_{k≥1} q^{k(1/2+ε)}/φ(q^k)) − 1). For q ≥ 11 and ε ≤ 1/8
the inner sum is ≤ 2q^{−1/2+ε}, so the bound is ≤ C_ε(e^{4σ_ε} − 1) ≤ 8C_εσ_ε for σ_ε ≤ 1/4. (b) In a cell a compatible
box mod h has relative measure 2^{ω(h)}/φ(h); the same computation with 4^{ω(h)} gives ≤ C_ε(e^{8σ_ε} − 1) ≤ 16C_εσ_ε
for σ_ε ≤ 1/8. Take η₀ := min(1/8, 1/(32C_ε)). ∎

**Corollary 2.6 (exact CRT certification of quadratic Linnik confinement is false on sparse prime sets; PROVED).** Let Π
be as in Theorem 2.5, a ≠ 0 supported on squarefree Π-numbers, T > 2, and B_J := {x : |Σ a_n (x/n)|² ≥ T‖a‖²} the
periodic (Jacobi) extension of B(a, T) (for primes p ≡ 1 (mod 4), (n/p) = (p/n)). Then:
(i) there is x ∈ 𝒫_Π in no class of 𝔉₅ ∪ 𝔘 with |Σ a_n (x/n)|² ≤ 2‖a‖² < T‖a‖²;
(ii) for every finite 𝔊 ⊂ 𝔉₅ ∪ 𝔘 there are infinitely many primes p ∈ Ω(𝔊) ∖ B_J; so no implication
     "p prime, p ∈ Ω(𝔊) ⟹ β_p(a) ≥ T" holds for all large primes, at any level of 𝔊.
*Proof.* (i) Under μ_Π the signs (x_q/q) are independent and uniform, so E|Σ a_n (x/n)|² = ‖a‖². The sterile set Z has
μ_Π(Z) ≥ 1/2, so E[|Σ|²·1_Z] ≤ ‖a‖² forces some z ∈ Z with |Σ|² ≤ 2‖a‖². (ii) Let L := 8·lcm(all refined moduli of
𝔊)·∏_{q|n, a_n≠0} q. Membership in the classes of 𝔊 and in B_J depends only on x mod L, and z mod L is a unit class;
Dirichlet's theorem gives infinitely many primes p ≡ z (mod L). ∎
(ii) is a statement about all large primes. It does not produce primes in (X/2, X] when the data grow with X (R1); see
§2.6.

**Remark 2.7 (the scope contains power-saving data).** Let A > 2, then 0 < ε < 1/2 − 1/A, y := (log X)^A,
Π := any ⌊η₀(ε)(y/2)^{1/2−ε}⌋ primes in (y/2, y], 𝒜 := the products of r := ⌊log X/log y⌋ distinct elements of Π,
a := 1_𝒜. Then |𝒜| ≥ (|Π|/r)^r = X^{1/2−ε−1/A−o(1)}, and if every exceptional p were a residue of every q ∈ Π, then
β_p = |𝒜| and Heath-Brown (L3) with N = X would give #E_X ≪ X^{1/2+1/A+ε+2ε′+o(1)}, a power saving once
2ε′ < 1/2 − 1/A − ε. Corollary 2.6 says this confinement, and any bias with T > 2, cannot be derived from avoidance of
ES₅/U word classes as a statement valid for all large primes, at any level; by Theorem 2.5(b), every sign pattern on
Π is realised by sterile points.

### 2.5 Approximate certification: a bounded whole-period hybrid lemma

**Proposition 2.8 (PROVED given EXSET_SIEVE_MASS Thm 3.2; rescoped after R1).** Let Π ⊂ (y/2, y] with y = (log X)^A,
a ≠ 0 supported on squarefree Π-numbers, T ≥ X^c, 𝔊 ⊂ 𝔉₅ ∪ 𝔘 finite. Let ν = Σ_i c_i 1[n ≡ b_i (mod d_i)] ≥ 0 on ℤ, put
L := lcm(d_i, moduli of 𝔊), and assume the **whole-period** radical level λ(L) := Σ_{ℓ | L, ℓ > W} log ℓ ≤ K log X. If
ν ≥ 1 on Ω(𝔊) ∖ B_J, then ν ≥ 1 on all of Ω(𝔊); hence log(1/Eν) ≤ Cλ^{2/3}(log λ)^{2/3}, λ ≤ K log X: the hybrid "Linnik
for the biased points + CRT majorant for the rest" saves no more than the U/ES₅ CRT cap.
*Proof.* Since every q ∈ Π eventually exceeds W, ω_Π(L) log(y/2) ≤ λ(L), so 2^{ω_Π(L)} = X^{o(1)} < T. Fix a residue r
mod L in Ω(𝔊) (unit or not). Write n = n₁n₂ with n₁ | rad L, (n₂, L) = 1. Under additive Haar measure on Ẑ conditioned on
x ≡ r (mod L), the symbols (x/n₂) are orthogonal with E(x/n₂)² = φ(n₂)/n₂, so
E[|Σ a_n (x/n)|² | r] = Σ_{n₂} (φ(n₂)/n₂)|Σ_{n₁} a_{n₁n₂}(r/n₁)|² ≤ 2^{ω_Π(L)}‖a‖² < T‖a‖² (Cauchy–Schwarz: at most
2^{ω_Π(L)} terms n₁). So the fibre contains points (and integers) outside B_J; ν, being L-periodic, is ≥ 1 on the whole
fibre. EXSET_SIEVE_MASS Thm 3.2 needs per-summand level ≤ λ, which holds after rewriting ν with residue indicators
mod L. ∎
*Scope (R1).* The standard cap charges each summand's modulus separately; here the whole period is charged. A hybrid
whose summands have small levels but whose periods jointly involve most of Π is **not** covered (open). The parenthetical
ES/ET extension of the first draft is withdrawn.

### 2.6 Dense and multi-scale prime sets (CONJECTURE, with EVIDENCE)

Theorem 2.5 needs σ_ε(Π) small because Lemma 2.3(c) is a pointwise bound. On average the boxes are far fewer.
`scripts/z51_linnik_planemass.py y es5 haar` takes Π = all primes in (y/2, y], removes the single-coordinate boxes
(h = q; 8–35 per q, all non-residues, against (q − 1)/2 non-residues), and charges the pair boxes (h = qq′) by the union
bound under the product measure on what is left (`data/z51_linnik/planemass.jsonl`). The random search checks only the
boxes it lists (h = q, qq′, and at y = 200 also qq′q″; the square boxes q² are empty by Lemma 2.4); larger products and
mixed powers q²q′ are not checked.

| y | #Π | certificate boxes per pair / (log h)² | pair mass | triple mass | search: points avoiding the checked boxes |
|---:|---:|---:|---:|---:|---|
| 200 | 21 | 1.10 | 1.02 | 0.21 | 842/3000 = 0.28 (h = q, qq′, qq′q″) |
| 400 | 32 | 1.11 | 0.77 | not computed | 472/1000 (h = q, qq′) |
| 800 | 61 | 1.11 | 0.92 | not computed | 409/1000 (h = q, qq′) |
| 1600 | 112 | 1.11 | 0.98 | not computed | 393/1000 (h = q, qq′) |

(U instead of ES₅ at y = 200: pair mass 0.88, 0.43 avoid h = q, qq′.) The pair mass is flat in y, as predicted by
"boxes ≈ 1.1(log h)²" and Mertens (≈ 2.2(log 2)² ≈ 1.05 per block); the survivors match e^{−mass} (Poisson).

**CONJECTURE 2.9 (dense planes).** There are c₀, C₀ > 0 such that for every finite set Π of primes ≥ 11 and every sign
pattern, the sterile part of the cell has relative measure ≥ c₀ exp(−C₀(Σ_{q∈Π} log q/q)²).
*Heuristic (not a proof).* An averaged form of Lemma 2.3(c), Σ_{q,q′∈Π} L(qq′)/(qq′) ≪ (Σ_{q∈Π} log q/q)², plus control of
all higher boxes and a local-lemma argument with suitable dependency bounds.
*Consequence (CONDITIONAL on 2.9).* Corollary 2.6 would extend to every datum supported on squarefree Π-numbers with
Σ_{q∈Π} log q/q = o(√log X), in particular to all dense dyadic blocks and all polylog-smooth squarefree data
(Σ_{q≤(log X)^A} log q/q ≍ log log X), with |Σ|² ≤ X^{o(1)}‖a‖² at a sterile point.

### 2.7 Summary of the obstructions, and what is left

**Theorem 2.10 (scoped conjunction; PROVED as Prop 2.2 + Cor 2.6 + Prop 2.8 + Prop 6.1; rescoped after R1, the
first-draft "universal circularity" is withdrawn).** For ES₅/U exceptional primes:
(A) a fixed-order (k ≥ 3) character bias of a squarefree-supported datum cannot follow from any statement valid for all
    large primes of a unit class (Prop 2.2);
(B) a quadratic confinement or bias (T > 2) of a datum on squarefree Π-numbers, Π sparse (σ_ε(Π) ≤ η₀), cannot follow
    from avoidance of any finite family of native ES₅/U word classes as a statement valid for all large primes (Cor 2.6),
    although such data would give a power saving (Remark 2.7);
(C) a hybrid with a CRT majorant of bounded whole-period level is capped at the U/ES₅ CRT exponent (Prop 2.8);
(D) the reverse-role (fibred Montgomery) sieve with CRT-certified depletion is capped likewise (Prop 6.1).
*Not covered:* dense or multi-scale Π (Conjecture 2.9); variable-order aggregates, full Montgomery/Elliott tests and the
larger sieve; hybrids with per-summand level only; the ET/Vaughan ratio families of ES on planes (one-coordinate
analogue: DEPTH_ASPECT Thm 3.1; numerics for ℛ(M) at plane points in §6.1); and finite-range arguments, i.e. statements
about the primes in (X/2, X] only, whose relevant moduli exceed X (for Remark 2.7's data the modulus encoding the Π-profile
is exp(y^{1/2−ε} log y), already superpolynomial in X).
*Reading (Assessment).* What remains for a Linnik proof is input outside these certification mechanisms: either
pointwise forcing at the individual primes ≤ X (B2-type), or an approximate statement that controls the non-generic
exceptional primes by some non-CRT means. *Comparison with z50:* G3 was an Assessment; z50 B Thm 5.2 bounded certified
marginal depletion of the integer avoider; (J)70/DEPTH_ASPECT Thm 3.1 gave one-coordinate sterile points for the ET
classes. New here: (A); the multi-coordinate sterile planes with every sign pattern for native ES₅/U classes and the
low-bias witness (B); the whole-period hybrid lemma (C); (D).

## 3. Escape (a): partial / weighted confinement, and a Heath-Brown upgrade

### 3.1 Bias suffices

For an odd prime p and a finite set S of primes with p ∉ S put σ_S(p) := Σ_{q∈S} (q/p).

**Theorem 3.1 (bias version of the Linnik bound; PROVED relative to Heath-Brown's quadratic large sieve; threshold
repaired after R1).** Let A > 1, 0 ≤ κ < (A − 1)/2, η := (log X)^{−κ}, y := (log X)^A, and S a set of s ≥ y/(5 log y)
primes in (y/2, y]. Then for every δ > 0,

  #{p ≤ X prime : |σ_S(p)| ≥ ηs} ≪_{A,κ,δ} X^{(1+2κ)/A + δ}.

*Proof.* Discard p = 2 and the ≤ s + 1 = X^{o(1)} primes in S. r := ⌊log X/log y⌋. For an r-tuple of elements of S let n₀
be the parity kernel of its product (the product of the q occurring an odd number of times), and b_{n₀} := #{ordered
r-tuples with kernel n₀}. Then b is supported on odd squarefree n₀ ≤ y^r ≤ X, and for odd p ∉ S,
Σ b_{n₀}(n₀/p) = σ_S(p)^r. By orthogonality of the sign characters on {±1}^S, ‖b‖² = E_ε(Σ_q ε_q)^{2r} ≤ (2r − 1)!! s^r
≤ (2rs)^r. Heath-Brown's Theorem 1 (Acta Arith. 72 (1995), p. 237: both variables odd squarefree, bound
≪_ε (MN)^ε(M + N)Σ|a_n|²) with M = N = X, restricted to odd primes, gives Σ_p |σ_S(p)|^{2r} ≪_ε X^{1+2ε}(2rs)^r. Primes
with |σ_S(p)| ≥ ηs number ≪_ε X^{1+2ε}(2r/(η²s))^r. Here log(s/r) = (A − 1 + o(1)) log log X and
r = (1 + o(1)) log X/(A log log X), so (2r/(η²s))^r = X^{−(A−1−2κ)/A + o(1)}; take ε = δ/3. ∎
*Check* (`scripts/z51_linnik_bias_check.py`, `data/z51_linnik/bias_check.txt`; reproduced by R1): the identity
Σ b(n₀/p) = σ^r, the formula ‖b‖² = Eσ^{2r} and the (2r−1)!!s^r bound hold exactly for S = primes in (30, 60), r ≤ 4; the
empirical large-sieve sums are ≤ 0.05·(Q + N)‖b‖² for Q ≤ 10⁵.

*Reading.* Full confinement (σ_S = s) is not needed: a non-residue fraction θ_p ≤ 1/2 − η/2 on one dyadic block
suffices, for any κ < (A − 1)/2. Under Haar measure σ_S/s has standard deviation s^{−1/2} = (log X)^{−A/2+o(1)}, so the
Linnik set is still superpolynomially rare among profiles (Hoeffding: exp(−cη²s) = exp(−(log X)^{A−2κ−o(1)}), and
A − 2κ > 1). *Scope (R1):* the dense block S here has σ_ε(S) → ∞, so it is **outside** Corollary 2.6; the sparse
sub-blocks of Remark 2.7 are inside it (they need A > 2), and Conjecture 2.9 would cover the dense block.

### 3.2 T2-lite: the cap threshold of CAP_BOUNDED Thm 3.2 drops from A > 2 to A > 1

**Corollary 3.2 (PROVED relative to Heath-Brown's Theorem 1, the PNT for primes ≡ 3 (mod 4), and CAP_DOWN Thm 1.2/Prop 1.3
via CAP_BOUNDED Lemma 3.1).** For every A > 1 and δ > 0,

  #{p ≤ X prime : e*(p) > (log X)^A/4} ≪_{A,δ} X^{1/A + δ}.

This improves CAP_BOUNDED Thm 3.2(a) (X^{2/A+o(1)}, non-trivial only for A > 2) in range and exponent. It counts
large-cap primes; it says nothing about ES-exceptional primes.
*Proof.* By CAP_BOUNDED Lemma 3.1, e*(p) > (log X)^A/4 implies p ≡ 1 (mod 8) and q₃(p) > (log X)^A =: y, i.e. (q/p) = +1
for every prime q ≡ 3 (mod 4), q ≤ y. Take S := the primes q ≡ 3 (mod 4) in (y/2, y] (s ∼ y/(4 log y) by the PNT in
progressions); p ∉ S since p ≡ 1 (mod 8). Then σ_S(p) = s, and Theorem 3.1 with κ = 0 (η = 1) gives the bound. ∎

*Remarks.* (1) The argument is Baier's least-non-residue argument (§1.5) transplanted to q₃(p); the novelty is only the
complete application to the exponent cap (CAP_BOUNDED Rem. (3) records an earlier reviewer sketch, CAP_INTERPOLATION
Rem. 3.2(b), of a power saving for e ≥ (log N)^{1+ε} by a different class large sieve). Pollack's bound is not needed.
(2) The route through q₃ cannot give a fixed power saving for A ≤ 1: with k := π(y; 4, 3), CONDITIONALLY on GRH,
#(𝒫(y) ∩ [1, X]) = 2^{−k}π(X; 8, 1) + O(√X log²X) (expand 1[p ≡ 1 (8)]·∏(1 + (q/p))/2 into characters of conductor
≤ 8∏q = e^{O(y)}; the coefficients have ℓ¹-norm 1), which is X^{1−o(1)} for y = (log X)^A, A ≤ 1. Lau–Wu Thm 1.2
(Graham–Ringrose) is the unconditional analogue for the least non-residue along a sequence. Going below A = 1 needs a
mechanism other than counting the confinement set 𝒫(y).
(3) Part (b) of CAP_BOUNDED Thm 3.2 (polylog exceptions above p^ε) is not improved: Heath-Brown's X^ε loss is too
large there.

### 3.3 Can a bias be forced without pointwise forcing?

* **Not by the certification mechanisms of §2, where they apply.** Corollary 2.6 needs T > 2, so it excludes exact
  certification of any bias for data on sparse prime sets; Proposition 2.8 excludes hybrids of bounded whole-period
  level. Dense blocks are not covered (Conjecture 2.9).
* **Heuristically yes, with room — a change from z50 (Assessment).** With Heath-Brown the Linnik route needs bias on
  primes q ≈ (log X)^{1+δ}, not (log X)^{2+δ}. Lane B's per-prime forcing heuristic (EXSET_SIEVE_MASS §4.2) covers all
  non-residues mod q at a *generic* profile once (log p)² ≳ q log q, i.e. up to q ≈ (log p)²/log log p; with the full
  ES Type II classes the label supply is cubic (§6.1). In a model where labels fall independently, an exceptional p must
  avoid ≍ (log p)²/q labels at each non-residue q, so its conditional profile is tilted towards residues by a factor
  e^{−c(log p)²/q} per such q: far more bias than Theorem 3.1 needs. z50 called the route "just short" (reach
  (log p)²/log log p against (log X)^{2+δ}); against (log X)^{1+δ} the heuristic reach has room (log X)^{1−δ}/log log X.
  No conditional distribution of actual exceptional primes is established.
* **Where the heuristic fails: at the sterile plane points.** On 𝒫_Π the h = q slice of labels at a non-residue q
  consists of the words of q (Lemma 2.3), ≈ 10–35 of them for q ≤ 1600 (and ≈ 40 for the ℛ(M) classes, §6.1), against
  (log M)² + log q·log M (U words) or ≈ 0.034(log p)³ (ℛ(M)) at a generic profile; boxes at h = qq′, … add a bounded
  mass. The sterile plane points of Theorem 2.5 are explicit non-generic profiles at which the forcing does not happen.
  A proof must therefore either force at the individual primes (using that their Π-free coordinates are generic, a
  property of the integer p rather than of a bounded-level class), or control the non-generic exceptional primes
  approximately by non-CRT means (Lemma 1.2, approximate form).

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
    one uses a^{(c)}. If the a^{(c)} are supported on squarefree Π-numbers with Π as in Theorem 2.5 and Π ∩ supp(L) = ∅,
    the sterile plane point z of Corollary 2.6 for a^{(c₀)}, c₀ := z mod L (≡ 1 at the Π-free part of L), gives
    infinitely many primes in that fibre avoiding 𝔊 and outside the Linnik set. (If L shares primes with Π, condition on
    them as in Prop 2.8's proof; this costs a factor 2^{ω_Π(L)} in T and needs a sterile point in the corresponding
    sub-cell, which Theorem 2.5(b) provides.) So fibring does not escape §2 within its scope.
(ii) *Archimedean twists a_n n^{it_p}, |t_p| ≤ T₀.* The Haar computation (1.1) is unchanged for each fixed t;
    E_Haar max_{|t|≤T₀}|Σ a_n (x/n) n^{it}|² ≪ (1 + T₀ log N)‖a‖² (Sobolev in t), so Corollary 2.6 holds with T > C T₀ log N,
    while the hybrid sieve's Δ grows by the same factor T₀.
(iii) *Dependence through the word data of p* (e.g. 𝒜_p := the divisors of p + 1, or the values of the word forms
    n + u that p "sees"). Such maps are injective (the divisor set of p + 1 determines p), and for generic data the
    vectors a^{(p)} are linearly independent, so K = dim V = #E and Lemma 4.1 reads #E ≤ #E·Δ/T. This is void, because
    T ≤ β_p(a) ≤ Δ for every single vector (Parseval: β_p(a) ≤ N + p for additive tests; |⟨a, χ_p⟩|²/‖a‖² ≤ #supp(a) ≤ N
    for quadratic tests; and Δ ≥ N + X resp. Δ ≥ N). ∎
*Exact blocking lemma for (b).* A p-dependent datum helps only if its dependence has ≤ X^{c} states (Lemma 4.1); such a
datum is a fibred datum, covered by §2 (Prop 4.2(i)). The word-form sequences have ≍ #E states and give nothing.

## 5. Escape (c): supersets E′ ⊇ E_ES defined by free character data

**Lemma 5.1 (orientation; PROVED, trivial).** Every relaxation in the zoo (capped ES^{(y,e)}, ES^{(S)}, ES^□, V_φ, odd
power rungs, window certificates with a cap) satisfies ES(p) ⟹ R(p), so its failure set E_R is a *subset* of E_ES. The
free character data these relaxations force (CAP_BOUNDED Lemma 3.1: E_{ES^{(y,e)}} ⊂ 𝒫(4e + 3); ES^□'s one Dirichlet
prime; V_φ's fixed-modulus shots) are properties of E_R. They pass to E_ES only if E_ES ⊂ E_R, i.e. only if R ⟺ ES at
primes. A superset E′ ⊇ E_ES is the failure set of a *strengthening* R′ ⟹ ES, and "E′ ⊂ B" is again a forcing statement
for ES itself: (q/p) = −1 (or an unbiased profile) ⟹ R′(p) ⟹ ES(p). ∎

**Lemma 5.2 (word colour is not free; PROVED by citation).** For a strengthening defined by a sub-menu 𝔊 of ES₅
certificate classes, E′ = E_X ∩ Ω(𝔊)-type avoider and every certificate condition is a congruence: the colour of a word
is a function of its shape (Theorem A; LOWERTAIL_DEEP_FABLE Lemma 1.2; FOREST_DEEP_FABLE Prop 3.1: the sets
G_A = {−d : d | A + 1, (−d/A_odd) = −1} are p-independent). So "Type II slices with undetermined colour" do not exist at
the level of classes: character data of p enter only through the *shadow* (whether p ≡ −d mod A for some d | A + 1).
Hence Corollary 2.6 (sparse Π) and Proposition 2.8 (bounded whole-period level) apply to every ES₅-defined E′, within
their scopes. ∎

**The window strengthening (EVIDENCE + Assessment).** The one natural strengthening with character content is
R′_y(p): *some prime window q ≡ 3 (mod 4) in (y/2, y] carries an ES solution with x = (p + q)/4* (CAP_DOWN Lemma 3.1 at
cap 0; equivalently q | d₁ + d₂ for two divisors d₁, d₂ of p(p + q)/4). E′_y ⊇ E_ES. Windows with (q/p) = −1 are
*forced* (CAP_DOWN Thm 1.2: they always carry some capped certificate), and they fire at cap 0 about twice as often as
unforced ones (CAP_BOUNDED §5). `scripts/z51_linnik_windows.py` tests the lottery on all 33 663 Mordell-hard primes in
[10⁸, 1.2·10⁸] (`data/z51_linnik/windows_1e8_y{200,400}.json`):

| block | windows | cap-0 rate forced / unforced (mean) | P(no forced window fires \| k) observed vs ∏(1 − ρ_q) | mean pair corr. | non-residue fraction: all / E′-type failures |
|---|---:|---|---|---:|---|
| (100, 200] | 11 | 0.47 / 0.23 | k = 2: 0.279/0.289; k = 4: 0.068/0.074; k = 6: 0.0165/0.0186; k = 8: 0.0054/0.0044 | −0.006 | 0.501 / 0.339 |
| (200, 400] | 16 | 0.34 / 0.17 | k = 4: 0.168/0.176; k = 7: 0.044/0.045; k = 10: 0.0082/0.0105; k = 12: 0.0046/0.0039 | −0.004 | 0.501 / 0.382 |

(Failures here = no forced window fires; the unforced ones are ignored.) The cap-0 events at different windows are
uncorrelated to within ±0.1 and multiply to within ~10–20%, and the failures are strongly residue-biased (non-residue
fraction 0.34–0.38 against 0.50). *Model consequence (Assessment).* If the lottery were independent with rates
ρ_forced ≈ 2ρ_unforced, the profile of E′_y would be tilted by a fixed factor (1 − ρ_f)/(1 − ρ_u) < 1 per non-residue
window: a *constant* bias, far more than Theorem 3.1 needs ((log X)^{−κ}). The pointwise statement that would make this
rigorous is

  **(WL_A)** every prime p ∈ (X/2, X] whose non-residue fraction θ_p on the primes ≡ 3 (4) in (y/2, y],
  y = (log X)^A, satisfies |θ_p − 1/2| < η/2, η = (log X)^{−κ}, has a window in that block carrying an ES solution.

**Corollary 5.3 (CONDITIONAL on (WL_A) for some A > 1, κ < (A − 1)/2).** #{p ≤ X : ES(p) fails} ≤ X^{(1+2κ)/A + o(1)}.
*Proof.* E_X ⊂ E′_y ⊂ {biased profiles} by (WL_A); Theorem 3.1. ∎
*Reading.* (WL_A) is the cleanest form of the escape: one window among ≈ (log X)^A/(2A log log X) must fire at every
*unbiased* prime; the biased primes are left to Heath-Brown. It is pointwise (gate G4: −1 in the divisor ratio set of
p(p + q)/4 mod q at one window), and under the model it fails with probability exp(−c(log X)^{A−o(1)}) per prime, so it
is heuristically true for every A > 1. It is not a CRT consequence: at a plane point (p ≡ 1 to high order at every prime
outside the block) x = (p + q)/4 has the fixed small-prime part of (1 + q)/4, and the window lottery loses its
randomness exactly as the word labels do (Lemma 2.3); a proof of the analogue of Corollary 2.6 for ES Type II window
classes was not attempted. *Exact blocking lemma for (c):* Lemmas 5.1–5.2: no zoo relaxation has the right orientation;
ES₅-defined supersets are covered by §2; the window strengthening needs (WL_A), a pointwise statement.

## 6. Escape (d): reverse roles (small primes q as moduli, exceptional primes as the sequence)

### 6.1 The forcing reach with the full ES Type II classes (EVIDENCE)

Classes: ℛ(M) = {n ≡ −4D (mod M) : M ≡ 3 (4), A = (M + 1)/4, D | A²} (CAP_INTERPOLATION Prop 5.1 at e = 0: every prime
p ≡ −4D (mod M), p ∤ DM, satisfies ES); these are the Type II ratio classes carrying the cubic supply of the 3/4 note.
Profinite forcing as in z50 B §4.2: fix p, a prime q ∤ p; a residue a mod q is *forced away* if the point that agrees
with p at every m prime to q and equals a at q lies in some ℛ(qm) with (m, q) = 1, qm ≤ p; i.e. m | p + 4D and
a ≡ −4D (mod q). `scripts/z51_linnik_forcing_es.c` + `z51_linnik_forcing_run.py` (Mordell-hard p near 10^k; mode 0 = at
p; mode 1 = at the plane point, x ≡ 1 at every m), `data/z51_linnik/forcing_es_*.json`. Means over the primes:

| p ≈ | labels per q (q ≥ 25) | labels/(log p)³ | non-residues reached: q ∈ [25,50) | [50,100) | [100,150) | [150,200) | [200,300) | first hole q* |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 10⁵ (6 p) | 55 | 0.036 | 0.77 | 0.53 | 0.36 | 0.32 | — | 17–29 |
| 10⁶ (6 p) | 96 | 0.036 | 0.89 | 0.66 | 0.50 | 0.42 | — | 17–37 |
| 10⁷ (4 p) | 141 | 0.034 | 0.95 | 0.80 | 0.64 | 0.55 | 0.41 | 29–41 |
| 10⁸ (4 p) | 208 | 0.033 | 1.00 | 0.90 | 0.77 | 0.67 | 0.52 | 37–53 |
| plane point, any p ≥ 10⁷ | 40 (saturated) | → 0 | 0.57 | 0.40 | 0.32 | 0.31 | 0.26 | 17 |

(Lane B's U-word numbers at the same p: [25,50) 0.47, 0.57, 0.70, 0.79; [100,125) 0.18, 0.25, 0.33, 0.40.)
* **The cubic supply is real at the label level:** labels per q ≈ 0.034 (log p)³ over four decades, against
  (log p)² + log q log p for U words. Coupon-collector coverage of the (q − 1)/2 non-residues then predicts a reach
  q log q ≈ 0.07(log p)³, i.e. q ≈ (log p)³/(15 log log p), which is (log p)^{3−o(1)} as the brief anticipated, and well
  beyond Heath-Brown's requirement (log X)^{1+δ} (§3). (EVIDENCE for the label count; Assessment for the extrapolation.)
* **At the plane point the reach collapses:** the labels saturate at ≈ 40 per q (they are the finitely many solutions of
  (km − 1)(k′m − 1) = (qm + 1)², the ℛ-analogue of the words of q in Lemma 2.3), and coverage is frozen at the same
  values for every p. Residue classes mod q are never hit there (plane parity), while at an actual p the ℛ classes also
  hit residues (the m-part carries the other sign).

### 6.2 CRT-certified reverse-role sieves are capped

**Proposition 6.1 (PROVED given EXCEPTIONAL_LARGESIEVE Thm 2.1/Cor 2.2 and EXSET_SIEVE_MASS Thm 3.2).** Let 𝔊 ⊂ 𝔉₅ ∪ 𝔘
be finite, L ≤ X^K, and for each unit class c mod L let ω_c(q) (q ≤ Q ≤ X, q ∤ L) be the number of classes mod q missed
by the whole avoider Ω(𝔊) ∩ {n ≡ c (mod L)} (fibrewise CRT-certified depletion). Then the fibrewise Montgomery bound
Σ_c (X/L + Q²)/L_c(Q) for #(E_X) is ≥ X·exp(−C(log X)^{2/3+o(1)}).
*Proof.* On each fibre the bound is CRT-admissible for the fibre avoider (reparametrise n = c + Lk; the moduli q are
prime to L), so by EXCEPTIONAL_LARGESIEVE Cor 2.2 it is ≥ (X/L)·E ν_c with ν_c = |g_c*|² ≥ 0, ≥ 1 on the fibre avoider,
periodic with moduli dividing L·lcm(q₁, q₂). Then ν := Σ_c 1[n ≡ c (L)]ν_c is a nonnegative congruence combination,
≥ 1 on all of Ω(𝔊), of level ≤ log L + 2 log Q ≤ (K + 2) log X, and Σ_c (X/L)E ν_c = X·E ν. EXSET_SIEVE_MASS Thm 3.2
gives E ν ≥ exp(−C λ^{2/3}(log λ)^{2/3}). ∎
*Why the cubic reach does not enter.* The reach of §6.1 uses the residues of p modulo **every** m ≤ p/q, i.e. the
integer p itself. A fibre fixes p only mod L ≤ X^K; the classes ℛ(qm) whose m | L are certified on the fibre, and they
number ≈ Σ_{m | L} τ(A_m²)/m ≈ (log log X)^{3} per q (the 1/m-weighted divisors m of L have log m ≈ log z, not log X),
so certified fibrewise depletion stops at q ≈ (log log X)³ (Assessment; consistent with Prop 6.1). At the plane fibres it
is the saturated plane count.

### 6.3 Decision

The brief asks whether the reverse-role reach is CRT-certified (then capped) or needs pointwise input. **Answer:** the
(log p)³ reach is a property of the individual integer p (its residues modulo all m ≤ p/q). Its CRT-certified part is
capped by Proposition 6.1, and at the sterile plane points it is zero. Used as a Linnik input (q as residues of the
exceptional primes) it is exactly the forcing of §3.3, which needs the pointwise statement P(a, T) or (WL_A). It needs
pointwise input.

## 7. Hostile reviews

**Model note.** The `subagent` tool failed (module error) in this session; reviews were run with the `pi` CLI,
`--model openai-codex/gpt-6-astra:high`, as non-interactive sessions in this worktree.

**R1 (Astra, high; §§1–3 of the first draft; `reviews/z51-linnik-review-1.md`, independent check script
`reviews/z51-linnik-review-1-check.py`).** Overall MAJOR revision; the first-draft Theorem 2.10 (universal circularity)
FATAL as stated. Per claim, and the repair made:
* Lemma 1.2: MINOR/MAJOR — the approximate form does not force the pointwise P(a, T). *Repaired:* exact and approximate
  forms separated; a ≠ 0; support statement conditioned on a required prime.
* (1.1): SOUND; interpretation MAJOR — CRT level is per summand, not total period; squares lie in B only for coherent
  non-negative data. *Repaired* (§1.2).
* Prop 2.2: MAJOR — Frobenius lies in a coset, not in Gal(K/F); compatibility of the class with p ≡ 1 (k) needed;
  consequences (larger sieve, full Montgomery/Elliott, "order ≥ 3 entirely") FATAL: wrong Parseval sign, variable-order
  aggregates have trivial baselines, squarefree support essential (counterexample with q_i²), the larger sieve does not
  need index ≥ p^δ in its primal use. *Repaired:* coset computation, elementary Kummer step replacing the Schinzel
  citation, fixed-order and squarefree scope; consequences withdrawn; (L5) described correctly.
* Lemma 2.3: (a) SOUND; (b) MINOR — D ≤ h + 1 false (u = 1, v = h gives D = h + 2). *Repaired* (D ≤ h + 2,
  f₁f₂ ≤ 2h + 2, sum over splittings, refinement remark).
* Lemma 2.4: SOUND after coprimality selection and a direct U-slot argument (Theorem B is for primes). *Repaired.*
* Theorem 2.5: SOUND (needs h = 1 excluded by Lemma 2.4; added). The "every sign pattern" sentence was unsupported:
  *repaired* by Theorem 2.5(b) (4^{ω(h)} union bound).
* Cor 2.6: SOUND in its exact, infinite-range scope. *Repaired:* B_J, refined moduli in L, no claim about (X/2, X].
* Remark 2.7: MAJOR qualification — ε must satisfy ε < 1/2 − 1/A. *Repaired.*
* Prop 2.8: MAJOR — the cited cap charges per-summand level, the proof needs whole-period level; nonunit residues need
  additive Haar. *Repaired and rescoped* (bounded whole-period hybrid lemma; per-summand hybrids open; ES/ET
  parenthetical withdrawn).
* §2.5/Conj 2.9: MAJOR evidentiary — "mass_trip = 0" meant "not computed"; local lemma not justified. *Repaired:* triple
  mass computed at y = 200 (0.21; 28% of points avoid all checked boxes), checked boxes listed, heuristic labelled.
* Theorem 2.10: FATAL as a universal theorem. *Withdrawn;* replaced by the scoped conjunction (A)–(D) with an explicit
  "not covered" list and the finite-range caveat (the Π-profile modulus is superpolynomial in X).
* Theorem 3.1: kernel collapse and norm SOUND; Heath-Brown's statement verified against the original (odd squarefree
  variables); threshold 2ηs made κ = 0 vacuous. *Repaired* (threshold ηs; p ∈ S and p = 2 discarded; δ-form).
* Cor 3.2: MAJOR proof error (vacuous κ = 0), exponent recoverable. *Repaired;* Pollack dependency removed; earlier
  reviewer sketch credited; "large-cap primes, not ES" stated.
* Remark (2): MINOR normalisation (𝒫(y) includes p ≡ 1 (mod 8)). *Repaired.*
* §3.3: MAJOR scope — "barrier applies unchanged" to dense S false; "forcing reach zero at plane points" false as a
  universal statement; approximate option omitted. *Repaired.*
R1 reproduced: the plane self-check (8/8), the planemass run at y = 200 (pair mass 1.0176; 100/300 pair-sterile), the
bias identities, and an independent W1/parity verification.

## 8. Remaining gap (precise)

1. **T2-full (Linnik confinement for ES₅/ES).** Needed: E_X ⊂ B(a, T) (or up to X^{1−c}) for some datum with T ≥ X^c.
   With Theorem 3.1 a bias of size (log X)^{−κ} on one dyadic block at (log X)^{1+δ} suffices. The lane shows this cannot
   come from (A) fixed higher-order characters, (B) native ES₅/U word-class avoidance on sparse prime sets (any level),
   (C) bounded-level hybrids, (D) fibred reverse-role sieves. Open routes: dense or multi-scale blocks (CRT-certified
   bias is excluded there only CONDITIONALLY on Conjecture 2.9); hybrids with per-summand level only; ES with the
   ET/Vaughan ratio classes on planes; and non-CRT inputs: pointwise forcing (e.g. (WL_A), §5) or an approximate
   argument controlling the non-generic exceptional primes.
2. **T2-lite** is reached for the cap relaxation (Corollary 3.2, A > 1). Below A = 1 the confinement set 𝒫(y) is too large
   (GRH); a different forcing mechanism would be needed.
3. **Heuristic status.** Heath-Brown puts the requirement (log X)^{1+δ} inside the forcing reach ((log p)² for U words,
   ≈ (log p)³/(15 log log p) for the ES ratio classes, §6.1); the window lottery is near-independent with residue-biased
   failures (§5). So the Linnik route is heuristically consistent with room. The obstruction is the non-generic profiles
   (sterile planes), where both the word labels and the ratio-class labels collapse to finitely many per q.
4. **Not done.** A proof of Conjecture 2.9 (needs an averaged form of Lemma 2.3(c) and a local-lemma argument); planes
   for the ET/Vaughan families; a per-summand-level version of Proposition 2.8.
