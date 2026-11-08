# Z66_UCOVER — is the uncovered set U bigger than the squares? (checkpoint 1)

Lane UCOVER, wave z66 (brief `z52bbriefs/z66_lanes.md` §UCOVER; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES or any case of it.** Internal, unrefereed.
Scripts `scripts/z66_ucover_*`, data `data/z66/ucover/`. Builds on `Z65_LOGIC2.md` (Thm D, Prop 5.5, §5.6) and on
Elsholtz–Tao (`sources/elsholtz-tao-1107.1010.pdf`, cited ET: Props 1.6, 1.7, 1.9, 2.2, 2.6, Lemma 2.8, §§3, 10).

**Status at checkpoint 1.** A clean reduction (Lemma 1, PROVED) and a proof plan for "U ⊋ (Ẑ^×)²" via the profiles
e_{ℓ,g} that equal 1 at every prime except one. Computations agree with an independent brute force.

## 0. Falsifier table (mandatory)

This lane is about coverings by polynomial identities; it proposes no positivity mechanism for ES.

| screen | behaviour |
|---|---|
| **F1 odd squares** | The square profiles are in U (ET Prop 1.6). Every caught residue found is a quadratic non-residue mod ℓ (checked; PROVED via the Jacobi characters in Lemma 1), as F1 requires. |
| **F2 C-even / numerator 8** | Not applicable: no positivity claim. The covering question is posed for ET's Prop 1.9 families of the numerator-4 equation only. |
| **F3 composites** | Profiles are units of Ẑ (prime-like); nothing about composites. |
| **F4 known zeros** | Not applicable (no positivity claim). Integer profiles are impossible (Ẑ^× ∩ ℚ = {±1}). |

**Pre-registered kill test (K1).** The route "e_{ℓ,g} ∈ U for non-residues g" dies if, for every tested prime
ℓ ≥ 17, all non-residue branches of the ℓ-adic survivor tree are caught by level 3, or if the caught mass per level
does not decrease. Partial result at checkpoint: ℓ = 11, 13 die at level 1; for all 18 primes 17 ≤ ℓ ≤ 101 the
surviving mass after level 2 is 0.06–0.37 (out of 0.5), and the level-2 caught mass is 0.01–0.20. The test is passed
so far.

## 1. Precise statements

* U := {π ∈ Ẑ^× : π lies in no ET Prop 1.9 family class} (closed; Z65_LOGIC2 §5.5). (Ẑ^×)² ⊆ U (ET Prop 1.6).
* For an odd prime ℓ and g ∈ ℤ_ℓ^×, let **e_{ℓ,g}** ∈ Ẑ^× be the profile with component g at ℓ and 1 at every
  other prime. A family class r mod m, m = ℓ^k m′ with ℓ ∤ m′, contains e_{ℓ,g} iff r ≡ 1 (mod m′) and r ≡ g (mod ℓ^k).
* **Q_U (brief).** Is U = (Ẑ^×)²? Equivalently (Thm D) is every non-square primitive class eventually covered by
  identities?
* **Target theorem (T).** For all sufficiently large primes ℓ, the Haar measure μ_ℓ of {g ∈ ℤ_ℓ^× : e_{ℓ,g} ∉ U}
  tends to 0; in particular e_{ℓ,g} ∈ U for non-squares g, so U ⊋ (Ẑ^×)².
* **K-question (brief).** Does K := {n ≡ 1 (840), (n/11) = −1} meet U?

## 2. Lemma 1 (reduction to three event equations; PROVED)

Let ℓ be an odd prime, k ≥ 1, N := ℓ^k. e_{ℓ,g} lies in a family class whose modulus has ℓ-valuation k iff
g ≡ ρ (mod ℓ^k) for a residue ρ ∈ E_k(ℓ) produced by one of:
* **(F)** a, c, d ≥ 1, ℓ ∤ acd, 4acd − 1 = N f′, ℓ ∤ f′, f′ | a + c:  ρ = −a/c (mod N).
* **(E/D)** a′, b′, c, D ≥ 1, ℓ ∤ a′b′, c(4a′b′D − 1) = a′ + N b′, ℓ ∤ e := 4a′b′D − 1:  ρ = −e and ρ = −1/e.
* **(A)** k₁ + k₂ = k, k₂ ≥ 1 odd, a′, d′, C ≥ 1, ℓ ∤ a′d′, f := 4a′d′C − 1 dividing 4ℓ^{2k₁+k₂}a′²d′ + 1:  ρ = −f.

(The E-equation with the ℓ-power split between a and b gives sub-cylinders of the pure case; see §2.2.)
Every caught ρ is a quadratic non-residue mod ℓ, and F- and E-events occur only for odd k.

*Proof sketch (full proof in §2.1).* Family by family (ET Prop 1.9 notation):
* I-1 (n ≡ −f mod 4ad, f | 4a²d + 1) gives (A); the class lies in {χ_{−4d}(n) = −1}, and χ_{−4d}(e_{ℓ,g}) =
  (g/ℓ)^{v_ℓ(d)}, so v_ℓ(d) is odd.
* I-4 and II-1 (n ≡ −1/e, −e mod 4ab, e | a + b) give (E/D).
* II-2 (n ≡ −4a²d mod f, 4ad | f + 1) gives (F); −4a²d ≡ −a/c mod f with c = (f + 1)/(4ad).
* I-2 gives (E) if ℓ ∤ f and (F) (twin) if ℓ | f. I-3 gives (A) if ℓ ∤ f; if ℓ | f it needs g² ≡ −4c²d, a non-residue,
  so it catches nothing. II-3 gives (A) if ℓ ∤ e and (F) if ℓ | e.

## 3. First computations (CERTIFIED for the stated ranges)

* `scripts/z66_ucover_brute.py ELL MMAX`: literal enumeration of all seven families, modulus ≤ MMAX, ℓ | m.
* `scripts/z66_ucover_levels.c ELL K`: exact level-K enumeration via (A), (E/D), (F) with the completeness bounds of
  §2.2.
* Cross-check (`data/z66/ucover/crosscheck_brute_vs_exact.txt`; ℓ ∈ {11, 13, 17, 47}, k ≤ 3, MMAX = 10⁵): every
  brute-force event (including the I-2, I-3, II-3 families) lies in the exact set, and every exact event with modulus
  ≤ 10⁵ is found by the brute force. No caught residue is a quadratic residue.
* ℓ = 11: level 1 catches all five non-residues (2, 6 only through the II-2 class −64 mod 143 = 11·13). ℓ = 13: all six
  are caught at level 1. So e_{11,g}, e_{13,g} ∉ U for every g.
* ℓ = 17 … 101 (`tree_k2_17_101.txt`): survivors persist through level 2, with mass 0.06–0.37.

(To be continued: §2.1 full proof, §4 Theorem T, §5 K-question, §6 (S)-families.)
