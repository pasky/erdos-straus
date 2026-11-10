# Z70_GEN — generative class maps (wave z70, lane GEN; final lane of the z68–z70 arc): narrowed — no generative map; eight classes of candidate maps excluded (five by scoped proof, three by blind tests); not a HOT LEAD

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
(D5) The checkpoint-1 falsifier table promised a family run on the composite (★)-zeros ≤ 10⁵; it was not done (the genus
target code is prime-specific) — the final table (§4) marks it untested. (D4) `data/z70/gen/` holds the raw per-prime records as one xz archive (`runs_W123.tar.xz`, 12 MB) to respect the 20 MB cap.

## 2. Theorems (PROVED unless labelled otherwise)
Setting for §2: p prime, p ≡ 1 (mod 4), d ≥ 1 with p ∤ d, D = −4dp, Cl = Cl(D) (primitive forms ↔ invertible ideals of
O = ℤ[√−dp], Cox §7). A good solution has a ≤ (p + e)/(4d) < p and e ≤ (p + 4d)/(4d − 1) < p (z69), hence p ∤ aA·e;
gcd(A, 2ad) = 1 (A ≡ −1 mod 4ad); e odd and gcd(e, d) | gcd(N_a, d) = 1. ψ := the genus character of D attached to p,
ψ([f]) = (m/p) for any m represented by f with p ∤ m (a class invariant — genus theory, Cox Thm 3.15); equivalently
ψ([𝔞]) = (N𝔞/p) for invertible 𝔞 with p ∤ N𝔞.

**Theorem GW (genus wall).** (a) ψ(g) = −1 for every g ∈ G_d(p). (b) For any Σ ⊂ ker ψ the subgroup ⟨Σ⟩ is disjoint from
G_d(p); the same holds for the image of ⟨Σ⟩ under any endomorphism x ↦ kx and under any automorphism preserving ψ.
In particular the classes of all prime ideals of norm q with (q/p) = +1 (split, or ramified over q | 2d) lie in ker ψ, and
so does every class of order ≤ 2 when d is squarefree, (q/p) = +1 for all q | 2d and p > 3d. On 𝔐 (where (2/p) = (3/p) = (5/p) = (7/p) = 1)
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
gcd(e, k) = 1 (e odd, gcd(e, d) = 1) and both factors are primitive with coprime norms. If y = 0, multiply 𝔈·conj 𝔟 = xO by
𝔟 (𝔟·conj 𝔟 = kO for invertible 𝔟, Cox Lemma 7.14): k𝔈 = x𝔟; comparing contents (𝔈, 𝔟 primitive) gives |x| = k and 𝔈 = 𝔟,
so e = k; as gcd(e, 2d) = 1 and k | 2d this forces e = 1, impossible (4abd = p + 1 ≡ 2 mod 4). So y ≠ 0 and
e·k = x² + dp y² ≥ dp. But
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

**Lemma REP (canonical representation fibres are barren).** Let p ≡ 1 (mod 8) be prime, d ≥ 1, and suppose
p = x² + 4d·a² with a ≥ 1 (the fibre "named" by a representation of p by x² + d·w², w = 2a). Then N_a = p + 4a²d has no
divisor A ≡ −1 (mod 4ad): the fibre a contributes nothing to G_d(p).
*Proof.* N_a = x² + 8d·a² = x² + 2d·(2a)². gcd(x, 2da) = 1 (a common prime would divide p). Every prime q | N_a is odd,
q ∤ d·a (else q | x), and −2d·(2a)² ≡ x² (mod q) gives (−2d/q) = 1, i.e. χ_{−8d}(q) = 1 for the Kronecker character
χ_{−8d}(m) = (−8d/m), a character modulo 8d with χ_{−8d}(−1) = −1. Hence χ_{−8d}(A) = 1 for every divisor A of N_a.
Since p ≡ 1 (mod 8) and x is odd, 4da² ≡ 0 (mod 8): da² is even. If a is even then 8d | 4ad and A ≡ −1 (mod 4ad) gives
χ_{−8d}(A) = χ_{−8d}(−1) = −1, impossible. If a is odd then d is even, d = 2d′, and N_a = x² + 16d′a²: every prime factor
has (−4d′/q) = 1 and the character χ_{−4d′}(m) = (−4d′/m) (modulo 4d′, which divides 4ad = 8ad′) is odd, so again A ≡ −1 (mod 4ad) is impossible.
∎ (The mechanism is T1's: the representation makes N_a a norm from ℤ[√−2d] (resp. ℤ[2√−d′]), whose norms are "squares" for
the character that separates the target residue −1.)

**Proposition SLICE (fixed-n word moves are re-factorisations; PROVED except the Remark).** Let T_n = {(x, y, z) ∈ ℕ³ : xyz − x − z = n}. Each word lies
in three slices: fixed y — (xy − 1)(zy − 1) = ny + 1; fixed x — (xy − 1)·z = n + x; fixed z — symmetric. A move preserving
one coordinate is a re-factorisation of the fixed integer ny + 1, n + x or n + z subject to a congruence (factors ≡ −1 mod y,
resp. the factor xy − 1 ≡ −1 mod x). *Remark (Assessment, sketch — not a proof):* on the fibre over y, (X, Z) := (xy − 1, zy − 1) satisfies XZ = ny + 1; the
fibrewise automorphisms of this hyperbola over ℚ(y) are (X, Z) ↦ (λX, Z/λ) and their compositions with the swap; a scaling λ
that is a *fixed* rational function (not chosen from the factorisation of ny + 1) and keeps both letters integral on every
fibre is plausibly only ±1, and λ = −1 gives x' = (2 − xy)/y ∉ ℤ for y ≥ 3 — so the only uniform fibrewise move would be the
swap; every other fibrewise move picks a divisor. (Non-fibred maps are tested in §3.4.) Also (PROVED, Lemma P5 of
LOOSE + direct check): s, τ_xy, τ_yz, μ, μ^s map Triv_n (words with a letter 1) into Triv_n and T_n ∖ Triv_n into itself
wherever defined. [τ_xy(x, y, 1) is defined only for x = y (then (xy − 1) | (n + y) with n + y − (xy − 1) = y − x), and τ_xy is
an involution on its domain; μ is defined on Triv only and lands in Triv.]

**Supplementary pre-registration (item 1b, added after W1–W3 and the screens, before any run of it): canonical
representation fibres.** Always-present *principal* seeds: the ideals (2a + √−p)·… attached to representations of p.
For d ∈ {1, 2, 3, 5, 7} let a_c(p) := w/2 where p = x² + d·w² with w even (exists and is unique up to sign for d = 1, 2, 3, 7
when p ≡ 1 (mod 24) and, for d = 7, (p/7) = 1; for d = 5 only when p is represented by the principal form of
discriminant −20); then N_{a_c} = p + 4a_c²d = x² + 2d·w². Prediction (Lemma REP, §2, proved before the run): the fibre
a_c is *barren* (no divisor A ≡ −1 mod 4a_c d) for every p ≡ 1 (mod 8) and every such d. Kill/check: any good divisor in a
canonical fibre refutes the lemma (bug); otherwise CERTIFIED on W1–W3. Comparison (descriptive): fraction of good
fibres among a ∈ [a_c/2, 2a_c] ∖ {a_c}.

## 3. Results (CERTIFIED computations; readings labelled; group structures CONDITIONAL on GRH via `quadclassunit`, every "∈ G" test unconditional)
Samples: primes p ≡ 1 (mod 24); W1 = [10⁵, 1.3·10⁵) 305 primes, W2 = [10⁶, 1.03·10⁶) 286, W3 = [10⁷, 1.02·10⁷) 1 561 (held out,
scored once); 𝔐 = 135 (W1 ∪ W2), 397 (W3). Pooled outputs `data/z70/gen/pool_W12.txt`, `pool_W3.txt` (registered statistics:
"U" = uniform null, "A" = per-prime half-octave α-null of A2; "X" = exact-α pooled null of D2).

### 3.1 Item 1 — genus / ambiguous / Rédei / small-prime seeding: every family BLIND relative to its minimal norms
| family (mean \|S\|/\|𝒯\|, W3) | W1 ∪ W2: hits vs E (z) — A-null; X-null | W3 (held out): A-null; X-null | coverage (G ≠ ∅), W3 | reading |
|---|---|---|---|---|
| S_AMB (0.000) | 0 hits everywhere (S_AMB ∩ 𝒯 empty for d = 1, 2, 3, 7; 0.2 % of 𝒯 for d = 5 in W1 ∪ W2) | 0 | 0 | **PROVED blind** (Lemma AMB) |
| S_RED (0.002–0.013) | d=1: 368 vs 388.4 (−0.9); X: 368 vs 402.6 (−1.5); d = 2–7: \|z\| ≤ 1.9 | d=1 −0.65; X −1.3; all d \|z\| ≤ 1.5 | d=1: 117/1560 (exp. 125.6) | blind (EVIDENCE) |
| S_CYC (≈0.006–0.013) | d=1: 1210 vs 1225.7 (−0.7); X: −1.7 | d=1 +0.8; d=2 −7.3, d=3 −6.2 (A); **X: all \|z\| ≤ 1.1** | d=1: 1261/1560 (exp. 1260.8) | blind vs exact minimal norm |
| S_GEN2 (≈0.004–0.011) | A: d=1 +4.2, d=3 +8.0, d=7 +10.1; **X: all \|z\| ≤ 0.6** | A: d=1 +5.1, d=3 +12.3, d=7 +15.7; **X: \|z\| ≤ 0.7** | d=2: 1218/1557 (X-exp. 1076, z +8.6) | BIAS vs the coarse null fully explained by exact minimal norm; coverage excess = same-norm exclusivity (below) |

* **Registered verdicts.** K-GEN1 fires (blind) for S_AMB, S_RED, S_CYC on the registered A-null except S_CYC at d = 2, 3 on W3
  (negative z — fewer hits than the coarse null; X-null: |z| ≤ 1.1). **BIAS fires for S_GEN2** (A-null z ≥ 4 on W1 ∪ W2 and
  ≥ 3 on W3 at d = 1, 3, 7) — decomposed: (i) against the exact-α null (pre-registered for W3, D2) the hit counts agree at
  every d (|z| ≤ 0.7 on W3; W1 ∪ W2 |z| ≤ 0.6): a GEN2 class is good exactly as often as any target class with the same
  minimal norm at another prime; (ii) **100 % of hit units have a reduced ideal that is itself a natural representative**
  (W3: 2031/2031, 1381/1381, 607/607, 937/937, 250/250 for d = 1, 2, 3, 5, 7), with least natural norm ≤ 100 in 90 % (d = 1),
  i.e. every hit is an *ideal identity at small norm* — a congruence condition on p modulo that norm (Prop. WORD); (iii) the
  remaining coverage excess (d = 2: X-z +5.8 / +8.6; d = 7 +4.8 / +3.8) is within-prime **exclusivity of same-norm seeds**: at
  d = 2, among 2 143 groups of GEN2 seed units with equal minimal norm, 0 had ≥ 2 good units vs 272.7 expected under
  independence (`gen2_coverage_decomp.txt`; d = 1: 180 vs 190.2) — two different ideals of one small norm are rarely both
  natural, which spreads a fixed number of hits over more primes (EVIDENCE; a partial proof: for prime norm N two natural
  A-ideals of the same norm in different units would need N | (a₁ − a₂)(a₁ + a₂) with a₁ + a₂ < N, impossible).
* **No GEN-CANDIDATE**: no family reaches coverage 1 at any d (best: S_CYC / S_GEN2 at d = 1, 81–86 %). **Union over
  d ∈ {1, 2, 3, 5, 7}** of S_GEN2 covers 584/591 (W1 ∪ W2) and 1 543/1 561 (W3) primes — exactly the exact-α expectation
  (581.3, z +0.9; 1 536.5, z +1.4); every uncovered prime is in 𝔐 (W3: 18 of 397 𝔐-primes uncovered, 0 of 1 164 others).
  So the union is a menu of small-norm divisor events (a B1-type congruence menu), whose failures concentrate on 𝔐, as GW(c)
  predicts (all seeds of 𝒯 have norm ≥ n_p, and n_p ≥ 11 on 𝔐).
* **First entry along S_CYC** (k = 1, 3, 5, …; d = 1, W3): k = 1 at 1228/1560 primes (the least admissible non-residue prime
  ideal 𝔮* is itself good — via its own natural identity in 1 398 of 1 399 CYC hit units, e.g. q* = 7 with p ≡ 3, 5 mod 7), else k ≥ 11 at 283 —
  the cyclic orbit is a search with a heavy first atom, not a map.
* **Item 1b — canonical representation fibres (Lemma REP):** the fibre a_c named by p = x² + d·(2a_c)² was barren at
  **every** prime of W1–W3 for d = 1, 2, 3, 5, 7 (0 good of 305 + 286 + 1 561 (d = 1, 2, 3), 70 + 86 + 409 (d = 5),
  150 + 140 + 777 (d = 7)); comparison fibres a ∈ [a_c/2, 2a_c] are good with probability 0.1–2 % each
  (`rep_fibres.txt`). CERTIFIED check of the PROVED lemma: the always-present principal seeds are *anti*-generative.

### 3.2 Item 2 — Rédei / 2-primary structure vs G: null
* r₄ for D = −4dp with d ∈ {1, 2, 3, 5, 7} is a function of p mod 840 on this sample (Rédei's 4-rank is governed by Legendre
  symbols among the prime discriminants of D, i.e. by (p/q), q | 2d, and fixed symbols among q | d): r₄ = 1 for d = 1, 2, 3;
  r₄ ∈ {0, 1} by residue class for d = 5, 7 — so the registered within-stratum test is degenerate for r₄ (D3); between strata
  it is confounded with the Mordell classes (local divisor effects) and not interpreted.
* r₈ (not a congruence invariant: for d = 1, 8 | h(−4p) iff p = x² + 32y², Barrucand–Cohn — quoted from memory, not used):
  within-stratum t for log(1 + |G_d|): W1 ∪ W2 d = 1 +0.54, 2 −1.00, 3 −0.15, 5 +0.21, 7 (𝔐 −2.32, all −0.6); W3 −1.42, +1.54,
  +0.65, +1.34, −0.64; for 1[G_d = ∅]: all |t| ≤ 2.14 (W1 ∪ W2), ≤ 1.03 (W3). Signal criterion (|z| ≥ 4 then ≥ 3) not met.
* 2-primary positions of good classes inside the target 2-coset: pooled χ² below its df everywhere (z −0.6 … −2.9 on
  W1 ∪ W2, −0.7 … −2.6 on W3): no preferred 2-primary position (slight under-dispersion, attributable to the pairing
  structure of G — not a signal).
* Emptiness: G₁ = ∅ at 1 of 591 (W1 ∪ W2) and 1 of 1 561 (W3) primes; G₇ = ∅ at 376/1561; no relation to r₈ (above).
**Verdict item 2: null.** The 2-primary class-group structure carries no detected information about |G_d| or its emptiness
beyond the residue class of p (EVIDENCE; CONDITIONAL on GRH for the invariant factors).

### 3.3 Item 3 — small-split-prime orbits (primes ≤ 50, norm budget 64√(dp)): a divisor search; class level only at or below chance
* **Free region (Prop. WORD):** 0 class-level hits below N = √(dp) for every d and window, and **0 violations** of
  N(𝔰)·m(g) ≥ dp among all (III) hits (W1–W3).
* (III) hits vs nulls at the registered thresholds X_j = √(dp)·2^j, j = 0…3 (W3, d = 1): 0, 0, 274, 1 702 hits vs α-null
  2 382, 2 846, 3 732, 5 020 (z −36.1, −39.3, −41.4, −34.1); same sign for every d and window (`pool_*.txt`). **No positive excess anywhere**;
  the deficit is the free-region exclusion (a seed of norm N cannot share a class with a good class of natural norm
  < dp/N unless it *is* that representative) which the α-null does not model; at j = 6 (X = 64√(dp)) the deficit has shrunk to
  z = −1.7 … −3.3 on W1 ∪ W2 but is still −6.4 … −14.2 on W3 (the excluded region grows relative to the budget).
* First entry (least seed norm whose class is good): type (I) — the seed is a natural representative — at 1 508/1 560 (d = 1),
  1 383/1 557 (d = 2), 836/1 525 (d = 3), 791/1 524 (d = 5), 200/1 185 (d = 7) primes of W3 (similar on W1 ∪ W2).
  **Registered K-GEN3** (no positive (III) excess AND type I ≥ 90 %): fires for d = 1 only; for d ≥ 2 the type-I share is
  below 90 % (89–90 % at d = 2; 17–55 % at d = 3, 5, 7) because 50-smooth natural norms are rare there and the orbit reaches
  most of 𝒯 by 8√(dp) — these first entries are class-level coincidences occurring *below* the chance rate. Registered
  outcome for d ≥ 2: **unresolved by the letter of K-GEN3, no BIAS-3** (Assessment: the 90 % clause was a poor choice; it
  measures smoothness of natural norms, not generation).

### 3.4 Item 4 — fixed-n solution graphs: no orbit starts without a known good solution (scoped to the listed moves)
`scripts/z70_gen_graph.py` → `graph.jsonl`; n = 73, 409, 577, 5569, 9601, 23929, 83449, 102001 (no trivial certificate),
37, 157, 1621, 4357, 12301 (with trivial certificates), controls 9, 25, 105, 4545.
* Explicit maps s, τ_xy, τ_yz, μ, μ^s, ρ_L, ρ_R (ρ_C for n ≤ 3·10⁴): **no component of T_n contains both a trivial word and a
  non-trivial certificate** at any tested n; at the five p ≡ 5 (8) inputs the only certificates in Triv-components are the
  trivial certificates themselves. PROVED for s, τ_xy, τ_yz, μ, μ^s (Prop. SLICE: they preserve Triv_n and its complement);
  CERTIFIED for ρ_L, ρ_R, ρ_C at the tested n. **K-GEN4 fires** (scoped to these maps).
* Slice moves (re-factorisations): every certificate reachable from Triv_n is 1–4 slice moves away (e.g. 409: 6 at distance 1,
  2 at distance 2; 102001: distances 1–4; at each of 23929, 83449, 102001 four certificates lie in slice components without
  trivial words). The entering moves are re-factorisations of ny + 1 (y-slice) or n + x, n + z with a factor in a fixed residue class
  (e.g. 409: (1, 2, 410) → (4, 2, 59) uses 7 | 2·409 + 1 = 819 with 7 ≡ −1 (mod 8)) — the tied divisor event itself.
* Type II threefold (PROVED, one line): every positive solution (a, b, c, e) at fixed (c, d) lies on the hyperbola
  (4acd − 1)(4bcd − 1) = 4c²dn + 1 together with the always-present integral point (a, b) = (0, −cn) (factorisation
  (−1)·(−(4c²dn + 1))); the move between them is the choice of a divisor ≡ −1 (mod 4cd). Orbits *can* start at
  always-present points, but the first step is the divisor event; no uniform (polynomial, fibre-preserving) move exists
  besides the swap is known (SLICE Remark, Assessment).

### 3.5 Screens (`screen_F2.txt`, `screen_F4.txt`, `screen_F13.txt`)
* **F1:** G_d(m²) = ∅ for all 648 pairs (m ≤ 301 odd, d ∈ {1, 2, 3, 5, 7}, gcd(m, d) = 1) — the computational face of GW(e).
* **F2 (12 R₈-zero primes near 10¹⁰), d = 1, 2:** G₂ ≠ ∅ at all 12 (|G₂| = 12–72: the C-even c = 1 line is empty, other c are
  not); seed hits: AMB/RED 0, CYC 30 + GEN2 36 hit classes in total, all via small natural norms; FR violations 0. Nothing in
  the families distinguishes C even from C odd.
* **F3 (285 composite (★)-zeros):** G_d ≠ ∅ for some d ≤ 7 at 281; none at 57, 345, 2305, 4545 (4545 = the known Type II
  exception). GW holds verbatim for non-square composites (ψ_n = (·/n)); the seed families are blind there for the same reasons.
* **F4 (42 hard primes: 14 (★)-zeros, 38 𝔊*-zeros incl. 85 664 329 and 564 661 441, + 2521, 3361, 21841, 76441),
  d = 1, 2, 3, 5, 7:** every hard prime has G_d ≠ ∅ for some d ≤ 7 (59 empty (p, d) fibres of 210); AMB 0 hits; RED 36,
  CYC 110, GEN2 210 hit classes; at 3 primes (3361, 2094481, 85664329) no family hits for any d; item-3 first entries mostly
  type I; 0 FR violations.

## 4. Mandatory falsifier table — final

| screen | outcome | label |
|---|---|---|
| **F1 odd squares** | GW(e): at n = m² the character computation forces (m²/A) = −1, so G_d(m²) = ∅ for every d — the target coset 𝒯 does not exist, every seed family is vacuous. The step where non-squareness (primality) enters a generative map is GW(a)/(c): the map must output a class with ψ = −1, which requires an ideal whose norm has a prime factor q with (q/n) = −1 (q ≥ n_p). Computation: 648 (m, d) pairs, all G = ∅. | PROVED + CERTIFIED |
| **F2 numerator 8 / C-even** | All lemmas are uniform in d (d = 2 = the numerator-8 Type II family, R₈ = its c = 1 line); nothing here distinguishes C even from C odd and nothing claims positivity. At the 12 R₈-zero primes near 10¹⁰: G₂ ≠ ∅ (c ≥ 2), seeds hit only through small natural norms; 0 FR violations. Lemma REP kills the canonical fibre for d = 2 at *every* p ≡ 1 (8). | PROVED / CERTIFIED |
| **F3 composites** | GW holds for every non-square n with gcd(n, 2d) = 1 and gcd(a, n) = 1 (ψ_n = Jacobi (·/n)); AMB/ORD/WORD need the class dictionary, i.e. the CLASS hypotheses (gcd(n, d) = 1, gcd(e, 2dn) = 1) — not claimed for all composites. 281 of the 285 composite (★)-zeros have G_d ≠ ∅ for some d ≤ 7 (none: 57, 345, 2305, 4545). No family run on composites (genus target code is prime-specific) — **untested numerically for the families**. Nothing here separates primes from composites beyond non-squareness. | PROVED (scoped) / CERTIFIED census |
| **F4 known zeros** | All 42 hard primes (incl. 85 664 329, 564 661 441) run at d = 1, 2, 3, 5, 7: G_d ≠ ∅ for some d at every one; no family is generative there (3 primes with no hit by any family at any d); AMB 0 hits; 0 FR violations. No positivity claimed. | CERTIFIED |

## 5. Verdict
**Narrowed (scoped theorems + blind tests); no generative map found; not a HOT LEAD. ES is OPEN.**
* *Which generative classes are excluded, and how* (the brief's fallback question):
  1. **Any word in ψ-trivial seeds** — principal class, ambiguous classes when (q/p) = 1 for q | 2d, prime ideals of norm q with
     (q/p) = 1 (all of norm < n_p; on 𝔐 all of norm ≤ 7), their powers, automorphic images preserving ψ: **PROVED blind**
     (GW(b)). The output of a generative map must contain a non-residue prime ≥ n_p (GW(c)).
  2. **Ambiguous classes themselves** (every class of order ≤ 2): **PROVED never good** for squarefree d, p > 3d (Lemma AMB).
  3. **Halving (2-descent / Rédei) — the unique group-theoretic escape from a ψ-trivial seed group** (GW(d)): reaches the
     2-power-torsion classes of the odd coset (S_RED) or, with odd seeds, a whole coset (a search). S_RED tested: blind
     (EVIDENCE, |z| ≤ 1.5 every d, W1–W3). Good classes of small order need large natural norms (Lemma ORD).
  4. **Words in small split primes of total norm < dp/m(g) (≈ √(dp/2))**: hit G only by *being* a natural representative —
     the divisor event (Prop. WORD, PROVED; 0 violations). Beyond that scale class-level coincidences occur, at or below the
     uniform/α rate (no positive excess in any window, d, or threshold).
  5. **Canonical principal seeds from representations p = x² + d(2a)²**: the named fibre is **PROVED barren** for p ≡ 1 (8)
     (Lemma REP; CERTIFIED on ≈ 5 400 (p, d) instances) — always-present constructions produce norms from ℤ[√−2d], which are
     "squares" for the character that separates the target residue: the T1 mechanism again.
  6. **Small-prime genus seeds and cyclic orbits** (S_CYC, S_GEN2): hit G exactly as often as classes of the same minimal norm
     (exact-α null, |z| ≤ 1.1 on W3), every hit an ideal identity at small norm (a congruence menu, B1); union over d ≤ 7
     covers 98.8 % of p ≡ 1 (24), failures all in 𝔐, as predicted by the null.
  7. **Fixed-n moves** (s, τ, μ, ρ_L, ρ_R, ρ_C): never connect always-present (trivial) words to non-trivial certificates
     (PROVED for s, τ, μ; CERTIFIED for ρ at 13 primes); fibre-preserving uniform moves are plausibly only the swap (SLICE Remark, Assessment);
     slice re-factorisations reach certificates in 1–4 steps but each entering step *is* the divisor event.
  8. **Rédei 4-/8-ranks**: r₄ is a congruence invariant here; r₈ and 2-primary positions show no relation to |G| or emptiness.
* *Escape hatches left open (Assessment).* (i) Non-group-theoretic, non-fibred maps producing ideals of norm ≫ √(dp) whose
  classes correlate with G (nothing tested here suggests one; every tested class-level coincidence sits at or below chance);
  (ii) maps using a *non-residue* input in an essential, non-menu way — GW forces this ingredient; the hits above use it only
  through small natural norms; (iii) the CLASS anti-coincidence (negative residual) and the d = 2 same-norm exclusivity are
  repulsions, not generation.
* **Hard screens (FRONTIER §4).** T1 squares: passes (GW(e); vacuous). 8/131: no positivity claim; uniform in d. Tied
  modulus: every hit decomposes into an ideal identity, i.e. a divisor ≡ −1 (mod 4ad) — the tie is not loosened. Fixed p: all
  statements are per p; none produces a solution without a divisor event.

## 6. Proposed FRONTIER §7 text (do not edit FRONTIER here)
"z70 GEN (`Z70_GEN.md`; narrowed — no generative class map). Question: can a good class of Cl(−4dp) be produced from data
present at every prime? PROVED: (GW) G_d(p) ⊂ ψ^{−1}(−1) (ψ = genus character at p), so words in ψ-trivial seeds (principal,
ambiguous for (q/p) = 1 at q | 2d, prime ideals of norm < n_p — on 𝔐 all of norm ≤ 7) are blind, every good class has
minimal and natural norms ≥ n_p, and 2-division (Rédei) is the only group-theoretic escape; (AMB) classes of order ≤ 2 are
never good (squarefree d, p > 3d); (ORD) A^{ord g} ≥ dp; (WORD) a seed ideal of norm < dp/m(g) hits G only by being a natural
representative (= the divisor event); (REP) the fibre named by p = x² + d(2a)² is barren for p ≡ 1 (8) (norms from ℤ[√−2d]);
(SLICE) fixed-n coordinate-preserving moves are re-factorisations; s, τ, μ preserve trivial words.
CERTIFIED/EVIDENCE (p ≡ 1 (24), 10⁵–1.02·10⁷, d = 1, 2, 3, 5, 7, held-out W3): ambiguous, Rédei (2-power-torsion), cyclic and
genus-seed families hit G exactly at the rate of classes with the same minimal norm (all hits = small-norm ideal identities);
union over d ≤ 7 of genus seeds covers 98.8 % (failures all in 𝔐, as the null predicts); smooth-prime orbits: no class-level
excess at any norm budget, 0 FR violations; Rédei r₈ / 2-primary positions unrelated to |G|; fixed-n explicit maps never join
trivial words to certificates (73, 409, hard zeros). Not a HOT LEAD."

## 7. Bottom line
A good class cannot be *generated* from the data every prime carries by any of the mechanisms the brief listed. The
reasons are now theorems rather than impressions: always-present seeds live in the kernel of the genus character ψ that
every good class violates (GW) — the class-group face of T1 — or, when canonical (ambiguous classes, representation
fibres), are provably never good (AMB, REP); the one group-theoretic exit, halving, lands in Rédei classes that are blind in
the data; and below the free-region scale any seed that hits a good class *is* a natural representative, i.e. the divisor
event (WORD). Every hit observed in 2 152 primes × 5 values of d is a small-norm ideal identity, at exactly the rate predicted by the
minimal norm of the class; fixed-n moves never start an orbit from trivial words. Primality enters only as the existence of
a non-residue prime ideal in the target genus — necessary, nowhere near sufficient. Not a HOT LEAD. ES is OPEN.

## 8. Reproduction (each command under `ulimit -v 6000000`, `timeout ≤ 1800`)
* validation: `uv run --with cypari2 --with sympy --with numpy python scripts/z70_gen_validate.py`
* registered runs: `scripts/z70_gen_runwin.sh W1 100000 130000`, `… W2 1000000 1030000`, `… W3 10000000 10200000`
  (writes `data/z70/gen/run_*.jsonl`; archived as `runs_W123.tar.xz`); pooling `python3 scripts/z70_gen_pool.py run_W1_d*.jsonl run_W2_d*.jsonl`
  and `… run_W3_d*.jsonl`; GEN2 coverage decomposition `python3 scripts/z70_gen_covdecomp.py DIR` (DIR = the unpacked archive).
* screens: `uv run --with cypari2 python scripts/z70_gen_run.py OUT d list <inputs>` (F2, F4; raw in `screens_raw.tar.xz`),
  `python3 scripts/z70_gen_screens.py OUT…`; F1/F3 `uv run --with cypari2 python scripts/z70_gen_f13.py data/z70/gen/screen_F13.txt`.
* item 1b: `uv run --with cypari2 python scripts/z70_gen_rep.py data/z70/gen/rep_fibres.txt`; item 4:
  `uv run --with cypari2 python scripts/z70_gen_graph.py data/z70/gen/graph.jsonl <n…>`.

## 9. Review log
(pending: hostile deep-mode internal review)
