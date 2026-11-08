# Z66_UCOVER — is the uncovered set U bigger than the squares? Verdict: strengthened (U ⊋ squares PROVED); HOT LEAD: no

Lane UCOVER, wave z66 (brief `z52bbriefs/z66_lanes.md` §UCOVER; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES or any case of it.** Internal, unrefereed; internal hostile review:
see §9. Scripts `scripts/z66_ucover_*`, data `data/z66/ucover/`. Builds on `Z65_LOGIC2.md` (Thm D, Prop 5.5, §5.6,
cited LOGIC2) and Elsholtz–Tao (`sources/elsholtz-tao-1107.1010.pdf`, cited ET: Props 1.6, 1.7, 1.9, 2.2, 2.6,
Lemma 2.8, §§3, 10), and on `Z64_SDEEPF.md` (cited SDEEPF: Thm 2.1, Prop 3.5, Thm 3.6) for §6.

**Results in one paragraph.**
* (i) **Lemma 1 (PROVED).** The family classes containing a profile e_{ℓ,g} (g at the prime ℓ, 1 at every other
  prime) are described by three explicit Diophantine "event" equations, one per level k (ℓ-valuation of the modulus).
  Four of ET's seven families are redundant here. Every level has finitely many events, and they embed into ℕ-points of
  ET's varieties ΣI_{ℓ^k}, ΣII_{ℓ^k}, ΣII_{ℓ^{K′}} (K′ ≤ 2k − 1).
* (ii) **Theorem T (PROVED relative to ET §3's counting).** The set of g ∈ ℤ_ℓ^× with e_{ℓ,g} ∉ U has Haar measure
  ≤ ℓ^{−2/5+o(1)}. So for all large primes ℓ, e_{ℓ,g} ∈ U for most non-squares g. **U ⊋ (Ẑ^×)²: Q_U (LOGIC2 O7′) is
  answered negatively.** By LOGIC2 Thm D, for large ℓ all but O(ℓ^{3/5+o(1)}) of the non-square classes
  {n ≡ 1 (mod 840), n ≡ g₀ (mod ℓ)} are not finite unions of family classes, and NOI does not prove ES at their large
  primes (Cor T.1: Mordell–Schinzel beyond squares). The threshold ℓ₀ is effective but not computed.
* (iii) **Small ℓ (CERTIFIED to the stated levels; EVIDENCE beyond).**
  * ℓ = 11, 13: every e_{ℓ,g} is caught at level 1.
  * Every prime 17 ≤ ℓ ≤ 101 keeps surviving non-square branches through level 2 (ℓ ≤ 101), level 3 (ℓ ≤ 53) and
    level 4 (ℓ ≤ 23). The surviving mass stabilises, e.g. 0.0848 for ℓ = 17 at level 4.
* (iv) **The brief's K = {1 mod 840, (n/11) = −1}.** Profiles that are 1 away from 11 die at level 1. Two-prime
  profiles (g at 11, h at 13) survive in exactly two branches, (g, h) ≡ (2, 2), (6, 7) mod (11, 13), through levels
  (11², 13³) and (11³, 13²) (EVIDENCE: two A-splits skipped per run, so these counts are upper bounds).
  K ∩ U ≠ ∅ stays a CONJECTURE.
* (v) **(S)-families (PROVED, computer-assisted).** For SDEEPF's good-word coverings the analogue is decided
  rigorously, because words are 3-variable objects with explicit √N·log N counts.
  * For ℓ = 11, 13 and every prime 17 ≤ ℓ ≤ 101, every non-residue branch g₀ mod ℓ that survives level 1 contains
    profiles in no good-word class (for ℓ = 11: g₀ ∈ {2, 6}).
  * Every prime ℓ ≥ 10⁵ has such profiles (explicit bound).
  * Hence, e.g., {n ≡ 1 (840), n ≡ 2 or 6 (mod 11)} is not finitely coverable by good words. This is the (S)-version
    of K, and here it is proved.
  * SDEEPF's four classes n ≡ 6 (7) are not settled: their profiles need two small primes, where the explicit tail is
    too weak.

## 0. Falsifier table (mandatory)

This lane is about coverings by polynomial identities; it proposes no positivity mechanism for ES.

| screen | behaviour |
|---|---|
| **F1 odd squares** | The square profiles are in U (ET Prop 1.6). Every caught residue found is a quadratic non-residue mod ℓ (checked; PROVED via the Jacobi characters in Lemma 1), as F1 requires. |
| **F2 C-even / numerator 8** | Not applicable: no positivity claim. The covering question is posed for ET's Prop 1.9 families of the numerator-4 equation only. |
| **F3 composites** | Profiles are units of Ẑ (prime-like); nothing about composites. |
| **F4 known zeros** | Not applicable (no positivity claim). Integer profiles are impossible (Ẑ^× ∩ ℚ = {±1}). |

**Pre-registered kill test (K1, checkpoint 1).** The route "e_{ℓ,g} ∈ U for non-residues g" dies if, for every tested
prime ℓ ≥ 17, all non-residue branches of the ℓ-adic survivor tree are caught by level 3, or if the caught mass per
level does not decrease. **Result: passed.**
* ℓ = 11, 13 die at level 1.
* All 20 primes 17 ≤ ℓ ≤ 101 survive level 2 with mass 0.06–0.37 (out of 0.5).
* The 10 primes 17 ≤ ℓ ≤ 53 survive level 3, and ℓ = 17, 19, 23 survive level 4.
* The caught mass per level drops roughly tenfold per odd level (§3).
* Theorem T then made the route a proof for large ℓ.

## 1. Precise statements

* U := {π ∈ Ẑ^× : π lies in no ET Prop 1.9 family class} (closed; Z65_LOGIC2 §5.5). (Ẑ^×)² ⊆ U (ET Prop 1.6).
* For an odd prime ℓ and g ∈ ℤ_ℓ^×, let **e_{ℓ,g}** ∈ Ẑ^× be the profile with component g at ℓ and 1 at every
  other prime. A family class r mod m, m = ℓ^k m′ with ℓ ∤ m′, contains e_{ℓ,g} iff r ≡ 1 (mod m′) and r ≡ g (mod ℓ^k).
* **Q_U (brief).** Is U = (Ẑ^×)²? Equivalently (Thm D) is every non-square primitive class eventually covered by
  identities?
* **Theorem T (proved in §4).** For all sufficiently large primes ℓ, the Haar measure μ_ℓ of
  {g ∈ ℤ_ℓ^× : e_{ℓ,g} ∉ U} tends to 0. In particular e_{ℓ,g} ∈ U for non-squares g, so U ⊋ (Ẑ^×)².
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

### 2.1 Proof of Lemma 1 (PROVED)

Conventions. ET Prop 1.9 lists seven families (I-1 … I-4, II-1 … II-3). For a class "r mod m" write m = ℓ^k m′ with
ℓ ∤ m′; then e_{ℓ,g} lies in it iff r ≡ 1 (mod m′) and r ≡ g (mod ℓ^k). If k = 0 the class would contain the unit
square 1; family classes are solvable by polynomials (ET Prop 1.9, converse part) and classes containing a unit square are
not (ET p. 7, Schinzel / Prop 1.6), so k ≥ 1. For an integer X write X = ℓ^{v(X)}X′ with ℓ ∤ X′.

*Jacobi fact (J).* If f > 0 and f ≡ −1 (mod 4d) with d ≥ 1, then (d/f) = 1 and (−d/f) = −1. (Write d = 2^s d″:
(d″/f) = (f/d″)(−1)^{((d″−1)/2)((f−1)/2)} = (−1/d″)(−1/d″) = 1 since (f−1)/2 is odd; if s ≥ 1 then 8 | f + 1 and
(2/f) = 1. Finally (−1/f) = −1.) Also, for f ≡ 3 (mod 4) prime to ℓ, (ℓ/f) = (f/ℓ)(−1/ℓ) = (−f/ℓ).

**I-1** (n ≡ −f mod 4ad, f | 4a²d + 1). Put k₁ = v(a), k₂ = v(d); m′ = 4a′d′. The catch condition is
f ≡ −1 (mod 4a′d′), i.e. f = 4a′d′C − 1 with C ≥ 1, and ρ = −f (mod ℓ^k). Since f | 4a²d + 1 = 4ℓ^{2k₁+k₂}a′²d′ + 1 this
is (A). *Parity:* −4a²d ≡ 1 (mod f) gives (−d/f) = 1, so χ_{−4d}(f) = 1, where χ_{−4d}(x) = (−4d/x) is a character
mod 4d; f ≡ −n (mod 4d) gives χ_{−4d}(n) = χ_{−4d}(−1) = −1 on the class. At n = e_{ℓ,g} (≡ 1 mod 4d′, ≡ g mod
ℓ^{k₂}): χ_{−4d}(e_{ℓ,g}) = (−4d′/1)·(ℓ/·)^{k₂} = (g/ℓ)^{k₂} (as e_{ℓ,g} ≡ 1 mod 4). Hence k₂ is odd and g is a
non-residue. *ρ is a non-residue:* f ≡ −1 (mod 4a′d′) and (J) give (−d′/f) = −1; (−4ℓ^{2k₁+k₂}a′²d′/f) = 1 gives
(ℓ/f)^{k₂}(−d′/f) = 1, so (ℓ/f) = −1 (k₂ odd), i.e. (−f/ℓ) = −1.

**I-4, II-1** (e | a + b, (e, 4ab) = 1; n ≡ −1/e resp. −e mod 4ab). Put k₁ = v(a), k₂ = v(b), c := (a + b)/e. The catch
condition is e ≡ −1 (mod 4a′b′), i.e. e = 4a′b′D − 1, and then c(4a′b′D − 1) = ℓ^{k₁}a′ + ℓ^{k₂}b′; ρ = −1/e resp.
−e, and ℓ ∤ e because (e, 4ab) = 1 and k ≥ 1. *Reduction to k₁ = 0 or k₂ = 0 (sub-cylinders):* if k₁, k₂ ≥ 1, let
λ := ℓ^{min(k₁,k₂)}. Then v(c) = v(a + b) ≥ v(λ) (ℓ ∤ e), and (a/λ, b/λ, e) is again a family parameter triple
(e | (a + b)/λ = (c/λ)e, (e, 4ab/λ²) = 1) whose class n ≡ −e (resp. −1/e) mod 4ab/λ² contains the original class, with
the same catch condition e ≡ −1 (mod 4a′b′). So the caught cylinder ρ mod ℓ^k lies inside the cylinder ρ mod ℓ^{k−2v(λ)}
of a parent event. Iterating, every I-4/II-1 cylinder lies in one with k₁ = 0 (or k₂ = 0, symmetric), i.e. in the
cylinder of a solution of (E/D): c(4a′b′D − 1) = a′ + ℓ^k b′. *ρ is a non-residue:* ℓ^k b′ ≡ −a′ (mod e) and (J)
give (ℓ/e)^k = (−a′b′/e) = −1, so k is odd and (ℓ/e) = −1, i.e. (−e/ℓ) = −1; −1/e is in the same square class.

**II-2** (n ≡ −4a²d mod f, 4ad | f + 1). Put c := (f + 1)/(4ad), so f = 4acd − 1 and k = v(f) ≥ 1 forces ℓ ∤ acd. The
catch condition is f′ | 4a²d + 1; since c(4a²d + 1) − a·f = a + c and (c, f′) = 1, it is equivalent to f′ | a + c. As
4acd ≡ 1 (mod f), ρ = −4a²d ≡ −a/c. This is (F). *ρ is a non-residue:* (−4a²d/f) = (−d/f) = −1 by (J), and
(−4a²d/f′) = (1/f′) = 1, so (ρ/ℓ)^k = −1: k odd and ρ a non-residue.

**I-2** (n ≡ −f mod 4ac, n ≡ −c/a mod f, (4ac, f) = 1). If ℓ ∤ f: catch ⟺ f ≡ −1 (mod (4ac)′) and f | a + c, caught
ρ = −f mod ℓ^{v(ac)}: this is the II-1 event (a, b, e) := (a, c, f). If ℓ | f (so ℓ ∤ ac): catch ⟺ 4ac | 1 + f and
f′ | a + c, ρ = −c/a mod ℓ^{v(f)}: with D := (1 + f)/(4ac), (c, a, D) is an (F) event with ρ = −c/a.

**I-3** (n ≡ −f mod 4cd, n² ≡ −4c²d mod f with a chosen root, (4cd, f) = 1). If ℓ ∤ f: catch ⟺ f ≡ −1
(mod (4cd)′) and f | 1 + 4c²d, ρ = −f mod ℓ^{v(cd)}: the I-1 event (a, d, f) := (c, d, f). If ℓ | f: catch needs
g² ≡ −4c²d (mod ℓ^{v(f)}) and 4cd | 1 + f, f′ | 1 + 4c²d. Then f ≡ −1 (mod 4cd) and (J) give (−4c²d/f) = −1, while
(−4c²d/f′) = 1, so −4c²d is a non-residue mod ℓ and no g qualifies.

**II-3** (n ≡ −e mod 4ad, n ≡ −4a²d mod e, (4ad, e) = 1). If ℓ ∤ e: catch ⟺ e ≡ −1 (mod (4ad)′) and e | 1 + 4a²d,
ρ = −e: the I-1 event (a, d, f) := (a, d, e). If ℓ | e: catch ⟺ 4ad | 1 + e and e′ | 1 + 4a²d, ρ = −4a²d mod ℓ^{v(e)}:
with C := (1 + e)/(4ad), (a, C, d) is an (F) event with the same ρ.

Conversely every solution of (A), (E/D), (F) is a family event of type I-1, I-4/II-1, II-2 (the computations above
are reversible). ∎

### 2.2 Completeness bounds and the ΣI/ΣII embedding (PROVED)

* **(F)** Put w := (a + c)/f′. Then w(4acd − 1) = N(a + c), i.e. **4acdw = N(a + c) + w**: (a, c, w, d) satisfies ET's
  (2.3) with n = N, so (a, c, w, d, f′, 4adw − N) ∈ ℕ⁶ ∩ ΣI_N (ET's e := (a + c)/w = f′ and f := 4adw − N =
  (Na + w)/c > 0). For a ≤ c: w(4ad − 1) ≤ 2N, so N/4 < adw ≤ 2N/3 and c = (Na + w)/(4adw − N).
* **(E/D)** (pure case) 4a′b′cD = a′ + c + N b′: (a′, c, b′, D) satisfies ET's (2.15) with n = N, giving a point of
  ℕ⁶ ∩ ΣII_N (e_ET = (a′ + c)/b′ = 4a′cD − N, f_ET = 4a′b′D − 1 = e). For the enumeration (general split, a ≤ b):
  3a′b′cD ≤ ce ≤ 2ℓ^{k₂}b′, so a′cD ≤ (2/3)ℓ^{k₂} and b′ = (ℓ^{k₁}a′ + c)/(4a′cD − ℓ^{k₂}).
* **(A)** f | 4ℓ^{K′}a′²d′ + 1 (K′ := 2k₁ + k₂ = k + k₁ ≤ 2k − 1) ⟺ f | C + ℓ^{K′}a′ (the two differ by
  C·(…) − ℓ^{K′}a′·f and (f, C) = 1). With w := (C + ℓ^{K′}a′)/f: **a′(4d′Cw − ℓ^{K′}) = C + w**, i.e.
  4Cwa′d′ = C + w + ℓ^{K′}a′: (C, w, a′, d′) satisfies (2.15) with n = ℓ^{K′}, a point of ℕ⁶ ∩ ΣII_{ℓ^{K′}}.
  Enumeration: d′Cw ≤ ℓ^{K′}/2 and w ∈ (ℓ^{K′}/(4d′C), (ℓ^{K′} + C)/(4d′C − 1)].
* Each of these maps is injective, and ρ is a function of the point (−a/c; −e, −1/e; −f).

## 3. Computations for single primes (CERTIFIED for the stated levels)

* `scripts/z66_ucover_brute.py ELL MMAX`: literal enumeration of all seven ET families, modulus ≤ MMAX, ℓ | m;
  independent of Lemma 1.
* `scripts/z66_ucover_levels.c ELL K`: the exact level-K event list via (A), (E/D), (F) with the completeness bounds of
  §2.2. (E/D are enumerated for all splits, the redundant mixed ones included.)
* **Cross-check** (`crosscheck_brute_vs_exact.txt`; ℓ ∈ {11, 13, 17, 47}, k ≤ 3, MMAX = 10⁵):
  * every brute-force event, including the I-2, I-3, II-3 families, lies in the exact set;
  * every exact event with modulus ≤ 10⁵ is found by the brute force;
  * no caught residue is a quadratic residue;
  * F- and E-events occur only at odd k.
* `scripts/z66_ucover_tree.py ELL K`: survivor tree S_k (non-residues mod ℓ^k none of whose truncations is caught).

| ℓ | level-1 caught / non-residues | surviving mass after level 1, 2, 3, 4 (non-residues: 0.5) |
|---|---|---|
| 11 | 5/5 | 0 |
| 13 | 6/6 | 0 |
| 17 | 6/8 | 0.125, 0.0956, 0.0856, 0.0848 |
| 19 | 5/9 | 0.222, 0.152, 0.1388, 0.1379 |
| 23 | 9/11 | 0.0909, 0.0593, 0.0529, 0.0527 |
| 29 | 8/14 | 0.214, 0.187, 0.182 |
| 41 | 6/20 | 0.350, 0.337, 0.332 |
| 53 | 18/26 | 0.154, 0.145, 0.144 |
| 101 | 20/50 | 0.300, 0.290 |

(All 20 primes 17 ≤ ℓ ≤ 101 at level 2: `tree_k2_17_101.txt`; level 3: `tree_k3_17_31.txt`, `tree_k3_37_53.txt`;
level 4: `tree_k4_17_23.txt`.) The mass caught at level k falls quickly: for ℓ = 17 it is 0.375, 0.169, 0.065, 0.0072
at k = 1, 2, 3, 4. The events found at level k are a few hundred, against ℓ^k residues.

EVIDENCE (not proof) that e_{17,g} ∈ U for a set of g of mass about 0.08. The tail beyond the computed level is not
bounded explicitly, for the reason given after Theorem T.

## 4. Theorem T: U contains non-square profiles (PROVED, relative to ET §3)

Let P_I(n) := #(ℕ⁶ ∩ ΣI_n) and P_II(n) := #(ℕ⁶ ∩ ΣII_n).

**Input (ET §3, proof of Prop 1.7; read in the source).** P_I(n) ≤ n^{3/5 + η(n)} and P_II(n) ≤ n^{2/5 + η(n)} with
η(n) = O(1/log log n), absolute constants. ET state Prop 1.7 for Type I/II *solutions*, but the proof counts sextuples:
"these solutions arise from sextuples (a, b, c, d, e, f) ∈ ℕ⁶ ∩ ΣI_n obeying the Type I bounds in Lemma 2.8. In particular
… e·f·(cd)²·ac ≪ n³, and hence at least one of e, f, cd, ac is O(n^{3/5})", then each case is closed by the divisor bound
(A.6) applied to (2.1), (2.6), (2.9), (2.8) (Type II: e²·(ad)(ac)(cd) ≤ n², cases closed by (2.13), (2.19), (2.20),
(2.21)). Lemma 2.8's proof uses only the defining equations and a ≤ b, and the reflection symmetries (Remark 2.4 and the
ΣII analogue) map ℕ-points to ℕ-points and swap a, b. So the bounds hold for all ℕ-points, coprimality not used.

**Theorem T.** For an odd prime ℓ let C_ℓ := {g ∈ ℤ_ℓ^× : e_{ℓ,g} ∉ U} (an open set) and μ_ℓ its Haar measure
(normalised on ℤ_ℓ^×). Then
  μ_ℓ ≤ Σ_{k≥1} [P_I(ℓ^k) + 2P_II(ℓ^k) + Σ_{K′=k}^{2k−1} P_II(ℓ^{K′})] / φ(ℓ^k) ≤ ℓ^{−2/5 + o(1)}  (ℓ → ∞).
In particular, for every sufficiently large prime ℓ (effectively computable, not computed), μ_ℓ < 1/2, so **e_{ℓ,g} ∈ U
for a set of non-squares g of positive measure, and U ⊋ (Ẑ^×)²**: Q_U has a negative answer.

*Proof.* By Lemma 1 and §2.1, C_ℓ is the union over k of the cylinders {g ≡ ρ mod ℓ^k}, ρ ∈ E_k, each of measure
1/φ(ℓ^k), and the I-4/II-1 cylinders with both k₁, k₂ ≥ 1 lie inside pure ones. By §2.2 the residues of level k number
at most P_I(ℓ^k) (F), 2P_II(ℓ^k) (E/D pure; two residues per point) and Σ_{K′} P_II(ℓ^{K′}) (A). Let η_ℓ := sup_{n≥ℓ} η(n) → 0.
For η_ℓ ≤ 1/20: the F-term is ≤ ℓ^{(3/5+η_ℓ)k}/φ(ℓ^k) ≤ 2ℓ^{−0.35k}; the E-term ≤ 4ℓ^{−0.55k}; the A-term
≤ 2k·ℓ^{0.45(2k−1)−k} = 2k·ℓ^{−0.1k−0.45}. Summing over k ≥ 1 gives μ_ℓ ≪ ℓ^{−0.35}, and the k = 1 terms dominate,
giving ℓ^{−2/5+O(η_ℓ)}. ∎

**Corollary T.1 (Mordell–Schinzel beyond squares; PROVED, same reliance plus Z65_LOGIC2 Thm D).** For every sufficiently
large prime ℓ, all but O(ℓ^{3/5+o(1)}) of the (ℓ − 1)/2 non-residues g₀ mod ℓ have the following property. For every q
prime to ℓ, the primitive non-square class
  K(q, ℓ, g₀) := {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)}
(e.g. q = 840: a sub-class of Mordell's class 1 mod 840) meets U. Hence:
* K(q, ℓ, g₀) is not a finite union of ET family classes, so no finite set of polynomial ES identities covers its large
  primes;
* NOI ⊬ "ES at all large primes of K(q, ℓ, g₀)" (Thm D (iv) ⇒ (i), contrapositive).

*Proof.* The cylinders g₀ + ℓℤ_ℓ have measure 1/(ℓ − 1) each, so at most (ℓ − 1)μ_ℓ = O(ℓ^{3/5+o(1)}) of them lie
inside C_ℓ. For any other non-residue g₀ pick g ∈ (g₀ + ℓℤ_ℓ) \ C_ℓ. Then e_{ℓ,g} ∈ U ∩ closure(K(q, ℓ, g₀)), and
Thm D applies. ∎

*Remarks.*
* "Sufficiently large" is effective in principle (ET's divisor-bound constants), but the explicit ℓ₀ is astronomically
  large. The computations of §3 indicate that already every ℓ ≥ 17 tested works (EVIDENCE only, since the tail beyond the
  computed levels is not bounded explicitly).
* For ℓ = 11 and 13 every e_{ℓ,g} is caught at level 1 (CERTIFIED), so Theorem T is not about small ℓ. The brief's K
  needs two-prime profiles (§5).
* The A-family needs the Type II exponent 2/5: its level-k events live on ΣII_{ℓ^{K′}} with K′ up to 2k − 1, and
  2·(2/5) < 1. A bound of strength n^{1/2} (divisor-in-progression counting) would not suffice for the A-tail; this is
  why the theorem is not made explicit here.
## 5. The brief's K = {n ≡ 1 (840), (n/11) = −1}

* **Single prime (CERTIFIED).** The level-1 events for ℓ = 11 catch all five non-residues. 7, 8, 10 are caught by
  events whose moduli have no factor 13 (moduli 11, 44, 55, 176; `data/z66/ucover` level-1 list). 2 and 6 are caught **only** by the
  II-2 classes n ≡ −64 and n ≡ −324 mod 143 = 11·13 (F-events (a, c, d) = (4, 9, 1), (9, 4, 1)), which require π ≡ 1 mod 13.
* **Two-prime profiles** (`scripts/z66_ucover_levels2.c`, `scripts/z66_ucover_ktree.py`): π = (g at 11, h at 13, 1
  elsewhere) lies in K iff g is a non-residue mod 11. Events at all levels (11^{k′}, 13^{j′}) ≤ (11^K, 13^J) were
  enumerated by the two-prime form of Lemma 1, with every prime of S = {11, 13} split between the parameters.
  * (K, J) = (2, 2): 74/8580 of the K-box survives.
  * (2, 3): 802/111540. (3, 2): 594/94380.
  * In all three, survivors lie only over (g, h) ≡ (2, 2) or (6, 7) mod (11, 13); h must be a non-residue mod 13 too.
  * Two A-splits with N₁²N₂ > 10⁹ were skipped in each of the (2, 3), (3, 2) runs, so these survivor counts are upper
    bounds for those levels.
  * Data: `ktree_3_2.txt`, `ktree_2_3.txt`.
* **Status.** CONJECTURE (K ∩ U ≠ ∅), with this EVIDENCE plus Theorem T's mechanism. A proof needs an explicit tail
  bound at the fixed primes 11 and 13. The A-family's events at level k live on ΣII at n up to N², so this needs an
  explicit Type II count of strength n^{θ}, θ < 1/2 (ET's 2/5 with explicit divisor-bound constants). Not done here.
  Covering K by finitely many family classes is likewise not excluded.

## 6. (S)-families (SDEEPF): the same question, decided

**Setting.**
* SDEEPF's covering words are W1 = fixed (t, u) (A = tu − 1; class n ≡ −u mod A, n ≡ 1 mod 4, good iff (A/n) = −1)
  and W2 = fixed (u, v) (class n ≡ −(u + v) mod uv, good iff 8 | (n + t)(n + u + v), t = (n + u + v)/uv).
* Fixed (t, v) is W1 after u ↔ v. These are all the polynomial word families: tuv − u − v = n forces exactly one of
  t, u, v to have degree 1 in n.
* U_S := profiles π ∈ Ẑ, π ≡ 1 (mod 4), in no good-word class. By compactness, a class is a finite union of
  good-word classes (SDEEPF-type covering) iff its closure misses U_S. Square profiles lie in U_S (SDEEPF Prop 3.5).

**Lemma S1 (event equations; PROVED).** e_{ℓ,g} lies in a good class:
* W1(t, u) iff A = ℓ^k A′ (ℓ ∤ A′), A′ | u + 1, g ≡ −u (mod ℓ^k) and (g/ℓ)^k = −1. For n ≡ e_{ℓ,g} mod 8A,
  n ≡ 1 (mod 8) and (A/n) = (n/A_odd) = (g/ℓ)^k.
* W2(u, v) iff uv = ℓ^k m′ (ℓ ∤ m′), m′ | u + v + 1, g ≡ −(u + v) (mod ℓ^k), and the goodness bit holds. The bit
  depends only on the 2-adic component 1. If uv = 2^a w with w odd, then t ≡ w^{−1}(1 + u + v)/2^a (mod 8), and good
  ⟺ v₂(1 + t) + v₂(1 + u + v) ≥ 3.
* The event equations, with N := ℓ^k:
  * W1: A′(ts − N) = t + 1, where u + 1 = A′s.
  * W2: (u′s − M₂)(v′s − M₁) = N + s, where u = M₁u′, v = M₂v′, M₁M₂ = N, and u′v′s = u + v + 1.

**Lemma S2 (complete enumeration with an explicit count; PROVED).** `scripts/z66_ucover_swords.c` finds every
event at level k by scanning divisors in residue classes. Its number of scanned candidates is at most
  B(N, k) = [2R(1 + ln X₀) + 2X₀ + S(1 + ln S) + S] + (k + 1)[2R(1 + ln X₀) + 2X₀ + 2R_r(1 + ln Z′) + 2Z′],
with X₀ = √(2N) + 2, R = √(N + X₀) + 2, S = √(N/2) + 3, R_r = √(2N) + 4, Z′ = √(N/2) + 4, so B = O(k√N log N).
* *Completeness* (W1). Put X = ts − N. If X ≤ X₀, then min(t, s) ≤ √(N + X): this is the small scan. If X > X₀, then
  t ≥ X − 1 forces s ≤ √(N/2) + 2 and X | N + s with cofactor z ≤ √(N/2) + 1: this is the (z, s) scan.
* *Completeness* (W2). If s ≤ X₀, then min(X, Y) ≤ √(N + s). If s > X₀, the smaller factor r < s equals its least
  residue, s | M + r, r ≤ √(2N) + 1, and the cofactor (u′ or v′) is ≤ √(N/2) + 1.
* Each candidate yields at most one event.
* The script asserts cand ≤ B at every computed level.
* *Cross-check* (`scripts/z66_ucover_sbrute.py`, files `sbrute_17_3e4.txt`, `sbrute_11_1e5.txt`, `sbrute_13_1e5.txt`).
  Direct Jacobi on large integer representatives:
  * ℓ = 17, A, uv ≤ 3·10⁴, k ≤ 3: brute ⊆ exact, and all 79 exact events in range are found;
  * ℓ = 11, 13, A, uv ≤ 10⁵, k ≤ 4: brute ⊆ exact, and all 95 resp. 77 exact events in range are found.
  * Good W2 events at non-unit ρ (ℓ | ρ) occur. They are irrelevant for unit g and are discarded.
  * No good event at a quadratic residue occurs.

**Theorem S (PROVED, computer-assisted; `scripts/z66_ucover_stree.py`, data `stree_certified.txt`,
`stree_certified_small.txt`).**
* (a) Let ℓ ∈ {11, 13} or 17 ≤ ℓ ≤ 101 prime, and let g₀ be a non-residue mod ℓ not caught at level 1 (for ℓ = 11:
  g₀ ∈ {2, 6}; ℓ = 13: {2, 7}; ℓ = 17: {3, 5, 6, 7}; full lists in the data). Then g₀ + ℓℤ_ℓ contains g with
  e_{ℓ,g} ∈ U_S. Hence for every q prime to ℓ the non-square class {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)} is **not finitely
  coverable by good words**. No SDEEPF-type covering can prove (S) on it.
* (b) The same holds for every prime ℓ ≥ 10⁵ and a set of non-residues g of positive measure: Σ_k B(ℓ^k, k)/φ(ℓ^k)
  ≤ 0.31 < 1/2, and the bound decreases in ℓ.
* (c) For ℓ = 3, 5, 7 every e_{ℓ,g} is caught at level 1.

*Proof of (a).*
* The good caught residues are computed exactly for k ≤ K₂ (ℓ^{K₂} ≤ 2·10¹²).
* The survivor tree is computed exactly to level K₁ (ℓ^{K₁} ≤ 2·10⁶).
* Levels K₁ < k ≤ K₂: in each branch subtract 1/φ(ℓ^k) per caught cylinder over S_{K₁} (sub-additivity).
* Levels k > K₂: subtract Σ_{k>K₂} B(ℓ^k, k)/φ(ℓ^k). This is summed to k = 400, and the rest is bounded by twice the
  last term (ratio < 1/2).
* Every listed branch keeps a lower bound ≥ 0.0099 (worst case over all ℓ and branches; tail ≤ 9.4·10⁻⁴). For example
  ℓ = 11: 0.0956 per branch.
* An open union of cylinders of total mass below the branch mass cannot cover the branch. ∎

*Reading.*
* For (S), Mordell-type coverings fail beyond squares, provably and explicitly. The (S)-analogue of the brief's K is
  {1 mod 840, n ≡ 2, 6 mod 11}, and it is non-coverable.
* For the ET families the same mechanism works (Theorem T) but is explicit only for large ℓ. The obstruction is the
  I-1 family, whose events at level k sit on the 4-variable ΣII at n ≈ ℓ^{2k}.
* SDEEPF's four classes 265, 321, 769, 825 mod 840 (n ≡ 6 mod 7) are **not** settled here.
  * e_{7,g} is caught at level 1, since it lies in the covered class 601.
  * Those classes need profiles non-trivial at two small primes (e.g. 769 needs π₅ ≡ 4, π₇ ≡ 6). There the explicit
    tail Σ_{j,k}(j + 1)(k + 1)√(5^j 7^k) log/(φ(5^j)φ(7^k)) is too large unless events are computed to about 10¹⁵.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: strengthened.** Q_U is answered: U ⊋ (Ẑ^×)² (Theorem T). For (S) the analogous statement is proved
explicitly, including the (S)-version of the brief's K (Theorem S). No bearing on the truth of ES; no HOT LEAD.

What it buys:
* The brief's consequence (a) holds: "Mordell–Schinzel beyond squares" (Cor T.1). For large ℓ, most non-square
  classes {1 mod 840, g₀ mod ℓ} cannot be reached by any finite set of polynomial identities, and ES on their large
  primes is not provable in normal open induction.
* So Mordell's program (finite identity coverings) is blocked not only at the 6 square classes mod 840 but at
  non-square classes too. The obstruction is not just "the class contains squares".
* The uncovered profiles found are 1 at all but one prime: they look like the square 1 everywhere except at one
  prime ℓ, where they are a non-residue.

**Hard screens (FRONTIER §4).**
* *T1 squares.* Square profiles are in U (input). The new elements are non-squares whose deviation from the square 1
  sits at one prime. Every caught residue is a non-residue (Lemma 1 parity), which is T1's footprint.
* *8/131, numerator 8.* Not applicable (no positivity claim). The method transfers to any numerator with a Prop 1.9
  analogue (ET Remark 1.10). Not done.
* *Tied modulus (B2).* Not moved. Theorem T says B2 cannot be bypassed by identities even on non-square classes.
* *Fixed p.* Not applicable.

**Proposed FRONTIER text** (do not edit FRONTIER here).
> *(z66 UCOVER.)* Q_U answered: the set U of unit profiles in no ET Prop 1.9 family class is strictly larger than
> (Ẑ^×)² (`Z66_UCOVER.md` Thm T, PROVED relative to ET §3's ΣI/ΣII point counts). The profiles e_{ℓ,g} (g at ℓ, 1
> elsewhere) are caught by family classes only through three event equations (Lemma 1), with ≤ ℓ^{3k/5+o(k)} events at
> level k. Hence for large ℓ almost every g works. By Thm D, most non-square classes {1 mod 840, g₀ mod ℓ} are
> NOI-unprovable and beyond every finite identity covering ("Mordell–Schinzel beyond squares"; ℓ₀ effective, not
> computed). Explicitly: ℓ = 11, 13 fail at level 1; 17 ≤ ℓ ≤ 101 survive to the computed levels (EVIDENCE). The brief's
> K = {1 mod 840, (n/11) = −1} remains CONJECTURE: two-prime survivors at (11, 13) ≡ (2, 2), (6, 7) to level ≈ 11³·13².
> For SDEEPF's (S)-word coverings the analogue is PROVED explicitly (Thm S): e.g. {1 mod 840, n ≡ 2, 6 mod 11} is not
> finitely coverable by good words. SDEEPF's four classes n ≡ 6 (7) are still open.

**Bottom line.**
* Identity coverings fail beyond the squares. For every large prime ℓ, profiles that are the square 1 at every prime
  but ℓ, and a non-residue at ℓ, avoid all of Elsholtz–Tao's polynomial families. So ES on such non-square classes is
  out of reach of Mordell's method and of normal open induction.
* The proof is a measure count: each family meets these profiles only through ES-type equations at n = ℓ^k, which have
  ≪ n^{3/5} solutions.
* For the analogous (S)-coverings the same is proved explicitly by computer for every prime 17 ≤ ℓ ≤ 101 (and ℓ = 11,
  13).
* The specific K at 11 and SDEEPF's four classes stay open. They need explicit tails at fixed small primes.
* Nothing here touches ES itself; B2 is unchanged.

## 8. Open problems
* **O1.** Explicit ℓ₀ in Theorem T. This needs an explicit Type II count P_II(n) ≤ C n^{θ}, θ < 1/2, for the I-1 events
  (ΣII at n = ℓ^{2k−1}). With it, the single-ℓ computations of §3 would become proofs (e.g. ℓ = 17).
* **O2.** The brief's K at 11 (two-prime tail at 11, 13), and SDEEPF's four classes n ≡ 6 (7) (two-prime tail at 5, 7).
* **O3.** The exact shape of U ∩ {e_{ℓ,g}}: is it a Cantor set of positive measure for every ℓ ≥ 17? Is the surviving
  mass m_ℓ → 1/2 as ℓ → ∞ (Theorem T says yes)?
* **O4.** Does U contain profiles that are non-squares at infinitely many primes? (Not examined.)


## 9. Review log and replay

Internal hostile review: see below (filled after the review).

**Replay** (each under `ulimit -v 4000000`, `timeout 1800`; all runs take seconds to minutes):
```
gcc -O2 -o /tmp/zlev  scripts/z66_ucover_levels.c
gcc -O2 -o /tmp/zlev2 scripts/z66_ucover_levels2.c
gcc -O2 -o /tmp/zsw   scripts/z66_ucover_swords.c -lm
uv run --with sympy python scripts/z66_ucover_brute.py 17 100000      # = brute_17_1e5.txt (also 11, 13, 47)
uv run python scripts/z66_ucover_tree.py 17 4                         # = tree_k4_17_23.txt (ET, single prime)
uv run python scripts/z66_ucover_ktree.py 3 2 1000000000              # = ktree_3_2.txt (ET, K-question)
uv run --with sympy python scripts/z66_ucover_sbrute.py 17 30000 30000 # = sbrute_17_3e4.txt
uv run python scripts/z66_ucover_stree.py 11 6 11                     # = stree_certified_small.txt block ell=11
uv run python scripts/z66_ucover_stree.py 17 4 9                      # = stree_certified.txt block ell=17
```
