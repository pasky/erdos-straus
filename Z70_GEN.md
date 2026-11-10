# Z70_GEN — generative class maps (wave z70, lane GEN; final lane of the z68–z70 arc) — CHECKPOINT 1 (skeleton)

**ES is OPEN. Nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z70_gen_*`, data `data/z70/gen/`. Sources: `Z70_CLASS.md` (Lemmas Φ, DL′, SR, FR, FR′,
Cor. J, Prop. NG), its review `data/z70/xreview/REVIEW_CLASS.md` §"Untested … symmetry candidates", `Z70_LOOSE.md` §3
(T_n, Lemma P5), `BRAINSTORM/bsB_redei_oddpart.md` (2-power theory sees only the sign layer of a residue condition).

## 0. Precise question and objects
Notation of `Z70_CLASS.md` §1.1/§1.6: p prime ≡ 1 (mod 4) (n for general inputs), d ≥ 1, gcd(d, p) = 1, D = −4dp,
O = ℤ[√−dp], Cl = Cl(D) the form class group. Type II solution (a, b, c, e): 4abd = p + e, ce = a + b; A = 4acd − 1,
N_a = p + 4a²d = A·e. **Good set** G_d(p) = {[A, 4ad, de]} = {φ_a(A) : a ≥ 1, A | N_a, A ≡ −1 (mod 4ad)} (PROVED,
§1.1/RF of CLASS: the second description needs no further condition — e := N_a/A ≡ −p (mod 4ad), b := (p + e)/(4ad),
c := (A + 1)/(4ad) give ce = a + b automatically).
**Question (brief).** Is there a map producing some g ∈ G_d(p) from data that exist at *every* prime — the principal
class, ambiguous classes, genus cosets, classes of small split primes — rather than moving an existing good class?
"Generative" (operational definition, fixed now): a rule R computable from p without consulting G (nor any divisor of
any N_a / 4c²dp + 1 chosen *because* it is ≡ −1 mod the tied modulus) that outputs a finite candidate set S_R(p) ⊂ Cl with
S_R(p) ∩ G_d(p) ≠ ∅ for every prime p in the tested range with G_d(p) ≠ ∅ (coverage = 1) — and with |S_R(p)| small
compared with the target genus (else it is a search). A rule with coverage < 1 but hit rate above the uniform null is a
**bias**, not a generative map; a rule at the null is **blind**.

## 0.1 Mandatory falsifier table (checkpoint-1 version; restated at the end)

| screen | how a generative class map must behave | status at checkpoint 1 |
|---|---|---|
| **F1 odd squares** | at n = m² the good genus coset does not exist (Thm GW(a) below: G_d ⊂ 𝒯_d := {χ_p = −1 ∩ …}, and for n = m² every assigned character value forced on a good form is inconsistent — T1). A generative map must output nothing good at squares; any map built from seeds in ker χ is PROVED blind at every n (GW(b)). The step where non-squareness enters: existence of a class with χ_n = −1, i.e. of an ideal norm q with (q/n) = −1. | PROVED (GW) |
| **F2 numerator 8 / C-even** | d even (d = 2 here) is the numerator-8 Type II family; R₈ is its c = 1 line. Every statement here is uniform in d, so nothing distinguishes C even; the 12 R₈-zero primes near 10¹⁰ are run for d = 2 as a screen of the seed families (they have G₂ ≠ ∅ or not — reported). | registered (§1) |
| **F3 composites** | GW holds for every non-square n with gcd(n, 2d) = 1 (χ_n replaced by the product of the genus characters at primes of odd exponent); the seeds are blind there too. Composite (★)-zeros: seed families run on the coprime-admissible ones ≤ 10⁵ (d = 1) — coverage reported, with the CLASS gcd caveats (n = 105, 33, 315 skipped/flagged). | registered |
| **F4 known zeros** | 14 (★)-zeros, 38 𝔊*-zeros (all, including 85 664 329 and 564 661 441 — the √p engine of §2 makes them cheap), 2521, 3361, 21841, 76441: run with d = 1, 2, 3, 5, 7. At p with G_d(p) = ∅ (d = 1: 37, 1621, 3361) every map is vacuous; a generative map would have to be defined for the d where G_d ≠ ∅ only. | registered |

## 1. Pre-registration (committed before any registered run; smoke tests listed in §1.6)
**Samples.** Primes p ≡ 1 (mod 24) in W1 = [10⁵, 1.3·10⁵), W2 = [10⁶, 1.03·10⁶), W3 = [10⁷, 10⁷ + 2·10⁵) (W3 = held-out:
scored once after W1, W2), d ∈ {1, 2, 3, 5, 7}; the 𝔐 subset (p mod 840 ∈ {1, 121, 169, 289, 361, 529}) reported
separately; screens F1–F4 as in §0.1. Class groups by PARI `quadclassunit` + full enumeration of the group (dict of
reduced forms → exponent vectors); **CONDITIONAL on GRH** for the group structure (h is cross-checked by counting
reduced forms for |D| ≤ 4·10⁸ — unconditional there); every membership test "class ∈ G" is an equality of reduced
forms (unconditional). G_d(p) is enumerated exactly by the small-fibre engine (a ≤ a_max := ⌊√((p + e_max)/(4d))⌋,
e_max = ⌊(p + 4d)/(4d − 1)⌋; every solution has min(a, b) ≤ a_max and G = −G), validated against
`scripts/z70_class_core.py:solutions` on ≥ 50 inputs (primes and composites) before any registered run.
**Target coset** 𝒯_d(p) := the genus of the good forms (all assigned genus characters fixed by A ≡ −1 (mod 4d),
(A/p) = −1); computed from characters, asserted to contain G_d(p) and to be one coset of Cl².

**Item 1 — genus/ambiguous seeding (seed families computed without looking at G):**
* S_AMB = Cl[2] ∩ 𝒯 (ambiguous classes in the target genus);
* S_RED = Cl[2^∞] ∩ 𝒯 (2-power-torsion classes of the target genus = the classes reachable from the ambiguous ones by
  repeated halving — the Rédei / 2-descent candidates; the escape hatch of GW(c));
* S_CYC = {k[𝔮*] : k odd, |k| ≤ 9}, 𝔮* = the prime ideal (q*, r + √−dp), r the least root, of the least split prime q* whose
  class lies in 𝒯 (the cyclic orbit of the least admissible non-residue prime);
* S_GEN2 = {σ + τ : σ, τ ∈ Base} ∩ 𝒯 with Base = Cl[2] ∪ {±[𝔮_γ] : γ ∈ Cl/Cl²}, 𝔮_γ the least split prime ideal in
  genus γ (one-step compositions of ambiguous classes and genus-minimal primes — every genus coset seeded).
For each family F and prime: hits H_F = |S_F ∩ G|, expectation E_F = |S_F|·|G|/|𝒯| (uniform null inside the target coset;
pairs {x, −x} treated as units, hypergeometric variance), coverage = 1[S_F ∩ G ≠ ∅], expected coverage from the same
null; first entry = position of the first hit in the canonical order of S_F (S_CYC: k = 1, 3, 5, …; S_RED: by order then
reduced form; S_GEN2: by norm product).
**Kill K-GEN1:** for every family and every d, pooled |z| < 3 for H vs E on W1 ∪ W2 and coverage within 3σ of its null
⟹ the family is **blind** (no generative signal at this resolution). **GEN-CANDIDATE:** coverage = 1 on all primes with
G ≠ ∅ in W1 ∪ W2 for some (F, d) with mean |S_F| ≤ |𝒯|/10 ⟹ stage 2 (W3 + F1–F4) ⟹ HOT LEAD if it survives.
**BIAS:** z ≥ 4 pooled and same sign z ≥ 3 on W3 ⟹ decompose the hits (ideal identity vs class level, §item 3 rule).

**Item 2 — Rédei / 2-primary structure vs G (d = 1, 2, 3, 5, 7):** per prime: 2-rank r₂, 4-rank r₄, 8-rank r₈ of Cl(D)
(from the invariant factors), |G_d(p)|, 1[G_d(p) = ∅], and the distribution of the 2-primary components of good classes
over Cl₂ ∩ (2-component of 𝒯) (uniform under the null; χ² per prime, pooled). Tests: (2a) within strata of p mod 840,
regression of log(1 + |G_d|) on 1[r₈ > r₈,min] (d = 1: 8 | h(−4p)) and on r₄; (2b) the χ² of 2-primary positions.
Signal ⟺ |z| ≥ 4 on W1 ∪ W2 and same-sign |z| ≥ 3 on W3. Emptiness: list every (p, d) with G_d(p) = ∅ and its r₄, r₈.

**Item 3 — small-split-prime composition orbits from the principal seed (norm budget):** seeds = all primitive ideals
𝔰 of norm N ≤ X composed of split primes ≤ P = 50 (all root choices), X = dp (so that the free region N·m < dp of
Lemma FR′ is covered and exceeded). Classify each 𝔰 with [𝔰] ∈ G: (I) 𝔰 is a natural representative (𝔄, conj 𝔅,
𝔡·conj 𝔈 of some solution or their conjugates for −g) — an ideal identity, i.e. 𝔰 *is* a divisor event; (III) otherwise —
a class-level coincidence, which by FR′ requires N(𝔰)·m(g) ≥ dp (asserted; m(g) = least natural norm). First entry
X*(p) = least N(𝔰) with [𝔰] ∈ G and its type. Null for (III): uniform in 𝒯 over the classes reached and not (I)-hit.
**Kill K-GEN3:** (III) hits pooled z < 3 against that null and the first entry of type (I) at ≥ 90 % of primes ⟹ the orbit
is a divisor search (no class-level generation). **BIAS-3:** (III) z ≥ 4 ⟹ decompose.

**Item 4 — fixed-n solution graphs (n = 73, 409, the 14 (★)-zeros, hard 𝔊*-zeros ≤ 10⁶; controls 9, 105, 25):**
vertices = the full word set T_n of `Z70_LOOSE.md` §3 plus the Type II solutions of d ≤ 7 with c ≥ 1, and the always-present
seed set Triv_n (words with a letter 1: divisor words of n + 1, Lemma P5) together with the trivial integral points
(0, −cn, c, d) of the Type II threefold; edges = every explicit move used anywhere in z69–z70 (s, τ_xy, μ, ρ_L, ρ_R, ρ_C,
a ↔ b, CS, DL, DL′, and the "slice re-factorisation" moves). Question: is a certificate reachable from Triv_n / trivial
points by moves whose *definition* does not require a divisor ≡ −1 (mod the tied modulus)? Registered outcome: report
components; **K-GEN4:** no certificate reachable from seeds by such moves at 73 and 409 ⟹ "no orbit starts without a
known good solution" (scoped to the listed moves); any reachable certificate ⟹ extract the move word and test it as a
uniform rule on all primes p ≡ 1 (4) < 10⁴ (stage 2; must fail at 9, 25, 105).

## 1.6 Smoke tests and amendments (all before any registered run)
*Validation* (`scripts/z70_gen_validate.py` → `data/z70/gen/validate.txt`): 249 (n, d) checks — the small-fibre solution
sets equal the exhaustive `z70_class_core.solutions` sets (23 listed n incl. 73, 409, 37, 1621, 3361, 21841, composites
33, 105, 4545, 1105, squares 9, 25, 225; 30 random primes in [10⁴, 6·10⁴); d = 1, 2, 3, 5, 7); for primes: g_b = −g_a, every
good class in the computed target genus, the three natural ideals lie in the class, #genera = |Cl/Cl²|. (Bug found and fixed
during validation: 2-adic genus characters must be taken from Cox Thm 3.15, not guessed — δ is *not* a character for
D = −4N, N ≡ 3 (4).)
*Smoke tests* (excluded from all registered samples): d = 1, 3 on primes ≡ 1 (24) in [50000, 52000) (20 primes each);
d = 1 on [500000, 503000) (29 primes; item 3 only, and the α-null below). Observations that changed the design:
(i) with X = dp the smooth orbit reaches **every** class of 𝒯 (d = 1 at 5·10⁴), so the item-3 (III) null is degenerate;
(ii) class-level (III) hits are absent below N ≈ 4–8·√(dp) and then track the uniform rate — the free region (FR′; 0
violations of N·m(g) ≥ dp); (iii) seeds with small minimal norm α (e.g. k = 1 in S_CYC) are good far above the uniform
rate when q* = 7 and p ≡ 3, 5 (mod 7) — a Mordell-class congruence identity (A = 7), absent on 𝔐; (iv) G₁(p) = ∅ also at
51361, 51913 (confirmed with the exhaustive engine).
**Amendments (before the registered runs):** (A1) item 3: X := min(dp, 64√(dp)); statistics reported cumulatively at
thresholds X_j = √(dp)·2^j, j = −4 … 6; registered thresholds for K-GEN3: j = 0, 1, 2, 3. (A2) **α-matched null (primary
for items 1 and 3):** a negation-unit u of 𝒯 is good with probability ρ(β(u)) := (# good units)/(# target units) in the
half-octave bin β = ⌊2 log₂ α(u)⌋ of its minimal norm α(u) (first coefficient of the reduced form), estimated over the
whole target coset of the same prime (item 3: with the (I)-classes removed). This asks the right question — does a seed
family hit G more often than classes *of the same minimal norm*? — because good classes have small natural
representatives (SR) and small-norm seeds would otherwise show a trivial size bias. The uniform null is still reported.
Kill/signal thresholds unchanged, applied to the α-matched z; strata 𝔐 / non-𝔐 reported separately.

**Deviation ledger (complete).** (D1) The memo text of the amendments A1/A2 above was written before the registered runs
but, through a tool race, committed only together with the W1–W3 results (`git log`); the *code* implementing A1/A2
(`scripts/z70_gen_run.py`, item-3 thresholds, `score_alpha`) was committed in `c7a1a785c`, before any registered run.
(D2) After W1 ∪ W2 had been pooled and **before W3 was run**, three analyses were added (code committed with the W3
data): the **exact-α pooled null** (leave-one-prime-out rate of goodness among target units with the *same* minimal norm α
at the other primes of the same window and d; units with α > 5000 dropped and counted), the **hit decomposition** (is
the reduced ideal of a hit class a natural representative? its least natural norm), and the **union over d** coverage
with its null. They are post hoc relative to W1 ∪ W2 and pre-registered relative to W3. (D3) Item 2a's r₄ test is
degenerate within p mod 840 strata (r₄ is a function of p mod 840 for these d — §3.2); only r₈ is testable within strata.
(D4) `data/z70/gen/` holds the raw per-prime records as one xz archive (`runs_W123.tar.xz`, 12 MB) to respect the 20 MB cap.

## 2. Theorems (PROVED unless labelled otherwise)
Setting for §2: p prime, p ≡ 1 (mod 4), d ≥ 1 with p ∤ d, D = −4dp, Cl = Cl(D) (primitive forms ↔ invertible ideals of
O = ℤ[√−dp], Cox §7). A good solution has a ≤ (p + e)/(4d) < p and e ≤ (p + 4d)/(4d − 1) < p (z69), hence p ∤ aA·e;
gcd(A, 2ad) = 1 (A ≡ −1 mod 4ad); e odd and gcd(e, d) | gcd(N_a, d) = 1. ψ := the genus character of D attached to p,
ψ([f]) = (m/p) for any m represented by f with p ∤ m (a class invariant — genus theory, Cox Thm 3.15); equivalently
ψ([𝔞]) = (N𝔞/p) for invertible 𝔞 with p ∤ N𝔞.

**Theorem GW (genus wall).** (a) ψ(g) = −1 for every g ∈ G_d(p). (b) For any Σ ⊂ ker ψ the subgroup ⟨Σ⟩ is disjoint from
G_d(p); the same holds for the image of ⟨Σ⟩ under any endomorphism x ↦ kx and under any automorphism preserving ψ.
In particular the classes of all prime ideals of norm q with (q/p) = +1 (split, or ramified over q | 2d) lie in ker ψ, and
so does every class of order ≤ 2 when (q/p) = +1 for all q | 2d and p > 3d. On 𝔐 (where (2/p) = (3/p) = (5/p) = (7/p) = 1)
this covers every prime ideal of norm ≤ 7 and, for squarefree d | 210, all of Cl[2]. (c) Every invertible ideal 𝔞 with
p ∤ N𝔞 in a class with ψ = −1 has (N𝔞/p) = −1, so N𝔞 has a prime factor q with (q/p) = −1, q ≥ n_p (least quadratic
non-residue of p); in particular every good class has minimal norm α(g) ≥ n_p and every natural norm ≥ n_p. (d) For
H ≤ Cl let H^sat := {x : 2^j x ∈ H for some j ≥ 0}. Then H^sat = Cl₂ ⊕ (H ∩ Cl_odd) (Cl₂ = 2-Sylow subgroup). If H ⊂ ker ψ
then H^sat ∩ ψ^{−1}(−1) = (Cl₂ ∩ ψ^{−1}(−1)) ⊕ (H ∩ Cl_odd) ≠ ∅: **division by 2 is the only group-theoretic operation that
leaves a ψ-trivial seed group**, and what it reaches is the fixed set Cl₂ ∩ ψ^{−1}(−1) (the 2-power-torsion classes of the
odd ψ-coset; S_RED is its intersection with the target genus) shifted by the odd part of H — the whole odd ψ-coset as soon as
H ⊇ Cl_odd (a search, not a map). (e) For n = m² (odd, gcd(m, d) = 1) the computation of (a) gives (m²/A) = 1 = −1, so
G_d(m²) = ∅ (= T1); for non-square n with gcd(n, 2d) = 1 the same proof works with ψ_n := (·/n) (Jacobi), a nontrivial
product of genus characters.
*Proof.* (a) g = [A, 4ad, de] represents A, p ∤ A. By Jacobi reciprocity (p ≡ 1 mod 4, A odd positive) (A/p) = (p/A) =
∏_{q^k ∥ A} (p/q)^k. For q | A: q | N_a = p + 4a²d and q ∤ 2ad, so p ≡ −4a²d (mod q) and (p/q) = (−d/q); hence
(p/A) = (−d/A) (Jacobi). For odd positive A coprime to d, (−d/A) = (−4d/A) (Kronecker), and m ↦ (−4d/m) is a character
modulo 4d with value −1 at m ≡ −1 (it is odd: (D/−1) = sign D for D ≡ 0 mod 4; Cohen, *A Course in Computational Algebraic
Number Theory*, §1.4.2 — standard). As A ≡ −1 (mod 4d), ψ(g) = (A/p) = −1. (b) ψ is a homomorphism Cl → {±1}; kΣ and
automorphic images preserving ψ stay in ker ψ; ker ψ ∩ G = ∅ by (a). Prime ideals: ψ([𝔮]) = (q/p). Classes of order ≤ 2:
by Lemma AMB below every such class contains an invertible ideal of norm k | 2d, so ψ = (k/p) = 1 under the hypothesis.
(c) immediate from ψ([𝔞]) = (N𝔞/p) = −1 and multiplicativity of the Legendre symbol; α(g) < p as α(g) ≤ √(4dp/3) < p for
p > 4d/3. (d) Write x = x₂ + x_o. For j ≥ the exponent of Cl₂, 2^j x = 2^j x_o, and multiplication by 2^j is an
automorphism of Cl_odd; H = H₂ ⊕ H_o (H finite abelian), so 2^j x_o ∈ H ⟺ 2^j x_o ∈ H_o ⟺ x_o ∈ H_o. Hence
H^sat = Cl₂ ⊕ H_o. ψ is trivial on Cl_odd = 2·Cl_odd ⊂ 2Cl, ψ ≠ 1 (by (a) when G ≠ ∅, and in general because the genus
characters are surjective — Cox Thm 3.15), so ψ|Cl₂ ≠ 1 and Cl₂ ∩ ψ^{−1}(−1) ≠ ∅. (e) as (a) with (m²/A) = 1, resp. with
(A/n) = (n/A) (Jacobi reciprocity, n ≡ 1 mod 4) = (−d/A) = −1 (each q | A has n ≡ −4a²d mod q; needs gcd(a, n) = 1). ∎

**Lemma AMB (ambiguous classes are never good).** Let d be squarefree, p > 3d and p(4d − 3) > 8d. Then
Cl[2] ∩ G_d(p) = ∅, and every class of order ≤ 2 contains an invertible ideal of norm k ∈ {k₀, 2k₀ : k₀ | d}.
*Proof.* The reduced form [a, b, c] of a class x with 2x = 0 is equivalent to its inverse [a, −b, c]; by uniqueness of reduced
forms either b = 0, or b = a, or a = c. b = 0: ac = dp, a ≤ c, so a ≤ √(dp) < p and a | dp ⟹ a | d. b = a: a(4c − a) = 4dp,
a must be even, a = 2k, k(2c − k) = dp with 2k ≤ c, i.e. k² ≤ dp/3 < p², so k | d. a = c: b² − 4a² = −4dp, b = 2β,
(a − β)(a + β) = dp with 0 ≤ β ≤ a/2, so the cofactor ratio (a + β)/(a − β) ≤ 3: a divisor k = a − β of dp with
dp/3 ≤ k² ≤ dp; k | d forces p ≤ 3d, and p | k forces k ≥ p > √(dp) — both excluded. So x contains the ideal of norm a with
a = k₀ or 2k₀, k₀ | d (primitive: gcd(a, b, c) = 1 as the form is primitive). Now let g ∈ G ∩ Cl[2]. By z69/CLASS §1.1,
𝔄·𝔡·𝔈 = (2ad + √−dp), so [𝔈] = −g − T_d = g + T_d ∈ Cl[2] (T_d = [𝔡] has order ≤ 2). Let 𝔟 be the ideal of norm k ≤ 2d in the
class [𝔈] = −[𝔈] (above); then 𝔈·conj 𝔟 is integral, invertible, principal = (x + y√−dp), and primitive because
gcd(e, k) = 1 (e odd, gcd(e, d) = 1) and both factors are primitive with coprime norms. If y = 0 then (x) primitive forces
|x| = 1 and e·k = 1, impossible (e = 1 would give 4abd = p + 1 ≡ 2 mod 4). So e·k = x² + dp y² ≥ dp. But
e·k ≤ 2d(p + 4d)/(4d − 1) < dp ⟺ p(4d − 3) > 8d. Contradiction. ∎ (CERTIFIED consistency: S_AMB has 0 hits in all
registered windows and screens, §3.1.)

**Lemma ORD (good classes have large order).** For g ∈ G_d(p) with natural representative 𝔄 of norm A (or conj 𝔅 of
norm B): A^{ord g} ≥ dp, i.e. ord(g) ≥ log(dp)/log min(A, B). *Proof.* 𝔄 = (A, 2ad + √−dp) is a product of split prime
ideals "on one side" (Lemma Φ of CLASS), so 𝔄^m is primitive; if m·g = 0 then 𝔄^m = (x + y√−dp) with y ≠ 0 (else 𝔄^m = (1),
A = 1), so A^m ≥ dp. ∎ (So a good class of order 4 — e.g. in S_RED — has min(A, B) ≥ (dp)^{1/4}.)

**Proposition WORD (seed words hit G below the free-region scale only by being a natural representative).** Let 𝔰 be a
primitive invertible ideal (e.g. any product of split prime ideals with no conjugate pair: every word in classes of small
split primes is the class of such an ideal) with [𝔰] = g ∈ G_d(p), and let m(g) be the least norm of a natural representative
(𝔄, conj 𝔅, or 𝔡·conj 𝔈; all primitive for squarefree d). If N(𝔰)·m(g) < dp then 𝔰 *is* that natural representative; by
Lemma SR, m(g) ≤ √(d(2p + e)), so every 𝔰 with N(𝔰) < dp/√(d(2p + e_max)) (≈ √(dp/2)) hits G only by an ideal identity —
i.e. N(𝔰) is itself a good norm A ≡ −1 (mod 4ad) dividing N_a (or a B- or de-norm) with the matching root: **the divisor
event**. *Proof.* Corollary FR′ of `Z70_CLASS.md` §1.6 (two distinct primitive invertible ideals with norm product < dp lie
in distinct classes) + Lemma SR. ∎ CERTIFIED: 0 violations of N(𝔰)·m(g) ≥ dp among all class-level (III) hits of item 3
(W1–W3, 5 values of d, ≈ 4·10⁶ seed ideals in the target genus).

**Proposition SLICE (fixed-n word moves are re-factorisations).** Let T_n = {(x, y, z) ∈ ℕ³ : xyz − x − z = n}. Each word lies
in three slices: fixed y — (xy − 1)(zy − 1) = ny + 1; fixed x — (xy − 1)·z = n + x; fixed z — symmetric. A move preserving
one coordinate is a re-factorisation of the fixed integer ny + 1, n + x or n + z subject to a congruence (factors ≡ −1 mod y,
resp. the factor xy − 1 ≡ −1 mod x). The only fibrewise maps given by polynomials with integer coefficients in the slice
parameter that preserve integrality on all fibres are the identity and the swap: on the fibre over y, (X, Z) := (xy − 1,
zy − 1) satisfies XZ = ny + 1, a fibrewise automorphism of the hyperbola is (X, Z) ↦ (λX, Z/λ) or its composition with the
swap, and integrality of x' = (λX + 1)/y for all words forces λ ∈ ℤ[y]^× = {±1}; λ = −1 gives x' = (2 − xy)/y ∉ ℤ for y ≥ 3.
(PROVED for this fibration-preserving class of maps only; non-fibred maps are tested in §3.4.) Also (PROVED, Lemma P5 of
LOOSE + direct check): s, τ_xy, τ_yz, μ, μ^s map Triv_n (words with a letter 1) into Triv_n and T_n ∖ Triv_n into itself
wherever defined. [τ_xy(x, y, 1) is defined only for x = y (then (xy − 1) | (n + y) with n + y − (xy − 1) = y − x), and τ_xy is
an involution on its domain; μ is defined on Triv only and lands in Triv.]
