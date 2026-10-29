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

(placeholder)

## 3. Escape (a): partial / weighted confinement

(placeholder)

## 4. Escape (b): p-dependent sequences

(placeholder)

## 5. Escape (c): supersets E′ ⊇ E_ES

(placeholder)

## 6. Escape (d): reverse roles

(placeholder)

## 7. Hostile reviews

(placeholder)

## 8. Remaining gap

(placeholder)
