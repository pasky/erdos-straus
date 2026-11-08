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
