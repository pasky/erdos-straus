# Z70_GEN — generative class maps (wave z70, lane GEN; final lane of the z68–z70 arc): narrowed — no generative map found; five scoped no-go theorems (GW, AMB, ORD, WORD, REP); the tested seed families hit G only at the rate fixed by their minimal norms; not a HOT LEAD

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
**bias**, not a generative map; a rule at the null is **blind**. [Cross-model review: this is a *candidate screen*, not a
formal definition of generation; coverage conditional on G_d ≠ ∅ does not prove fibre positivity (a universal construction
must also choose d or prove its fibre non-empty); and a rule that, by an independently specified identity, *constructs* a
natural ideal is legitimate — realising the divisor event constructively is the goal, not a disqualification. "Blind" means
only "no detected excess against a particular null".]

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
reduced forms → exponent vectors); **CONDITIONAL on GRH** for the group structure [the promised independent
count of reduced forms was NOT implemented — review item 12; completeness-dependent statistics stay GRH-conditional]; every membership test "class ∈ G" is an equality of reduced
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
sets equal the exhaustive `z70_class_core.solutions` sets (22 listed n incl. 73, 409, 37, 1621, 3361, 21841, composites
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
(D6) Item 4 as implemented is narrower than registered: the graph contains the words T_n only (no Type II vertices, no
trivial integral points, no CS/DL/DL′ edges — the Type II part is the one-line PROVED remark of §3.4), all registered inputs
(73, the 14 (★)-zeros, the 26 𝔊*-zeros ≤ 10⁶, controls) were run after the review (the first pass had omitted 19 of them).
(D7) First-entry orderings were implemented only for S_CYC (not S_RED, S_GEN2); the registered list of every empty (p, d)
with r₄, r₈ is given as counts plus `empty_fibres.txt`. (D8) D2's chronology (analyses added after W1 ∪ W2, before W3) is
author-reported: the code and the W3 data entered git in the same commit. (D9) After the internal review (§9) the pipeline
was corrected and **all of W1–W3 was rerun** (conditional within-bin α-null with finite-population correction `famAC`,
threshold-local item-3 censoring, seed-level identity check, matched conditioning of the coverage null, cross-fitted
exact-α null); §3 reports the rerun.
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
In particular the classes of all *invertible* prime ideals of norm q with (q/p) = +1 (split, or ramified over q | 2d — for
non-squarefree d or at the conductor prime 2 of ℤ[√−dp] a prime ideal need not be invertible and then defines no class) lie
in ker ψ, and
so does every class of order ≤ 2 when d is squarefree, (q/p) = +1 for all q | 2d and p > 3d. On 𝔐 (where (2/p) = (3/p) = (5/p) = (7/p) = 1)
this covers every prime ideal of norm ≤ 7 and, for squarefree d | 210, all of Cl[2]. (c) Every invertible ideal 𝔞 with
p ∤ N𝔞 in a class with ψ = −1 has (N𝔞/p) = −1, so N𝔞 has a prime factor q with (q/p) = −1, q ≥ n_p (least quadratic
non-residue of p); in particular every good class has minimal norm α(g) ≥ n_p and every natural norm ≥ n_p. (d) For
H ≤ Cl let H^sat := {x : 2^j x ∈ H for some j ≥ 0}. Then H^sat = Cl₂ ⊕ (H ∩ Cl_odd) (Cl₂ = 2-Sylow subgroup). If H ⊂ ker ψ
then H^sat ∩ ψ^{−1}(−1) = (Cl₂ ∩ ψ^{−1}(−1)) ⊕ (H ∩ Cl_odd) ≠ ∅. Consequently, **within the operation set
{+, −, x ↦ kx, ψ-preserving automorphisms, "all x with 2x = h"}** the only operation that leaves a ψ-trivial seed group is
the halving step, and the closure reaches exactly (H′)^sat, H′ ⊂ ker ψ the closure of H under the first four operations:
the fixed set Cl₂ ∩ ψ^{−1}(−1) (the 2-power-torsion classes of the odd ψ-coset; S_RED is its intersection with the target
genus) shifted by H′ ∩ Cl_odd — the whole odd ψ-coset as soon as H′ ⊇ Cl_odd (a search, not a map). (Automorphisms *not*
preserving ψ can leave ker ψ without halving — e.g. Cl(−260) ≅ C₄ × C₂ at p = 13, d = 5, (x, y) ↦ (x, y + x mod 2), review
item 7 — they are outside this statement; they are not canonical, since ψ is.) (e) For n = m² (odd, gcd(m, d) = 1) the computation of (a) gives (m²/A) = 1 = −1, so
G_d(m²) = ∅ (= T1); for non-square **n ≡ 1 (mod 4)** with gcd(n, 2d) = 1 and solutions with gcd(a, n) = 1 the same proof
works with ψ_n := (·/n) (Jacobi), a nontrivial product of genus characters (n ≡ 1 mod 4 is needed for Jacobi reciprocity:
at n = 15, d = 1 the solution (1, 4, 5, 1) has A = 19 and (19/15) = +1).
*Proof.* (a) g = [A, 4ad, de] represents A, p ∤ A. By Jacobi reciprocity (p ≡ 1 mod 4, A odd positive) (A/p) = (p/A) =
∏_{q^k ∥ A} (p/q)^k. For q | A: q | N_a = p + 4a²d and q ∤ 2ad, so p ≡ −4a²d (mod q) and (p/q) = (−d/q); hence
(p/A) = (−d/A) (Jacobi). For odd positive A coprime to d, (−d/A) = (−4d/A) (Kronecker), and m ↦ (−4d/m) is a character
modulo 4d with value −1 at m ≡ −1 (it is odd: (D/−1) = sign D for D ≡ 0 mod 4; Cohen, *A Course in Computational Algebraic
Number Theory*, §1.4.2 — standard). As A ≡ −1 (mod 4d), ψ(g) = (A/p) = −1. (b) ψ is a homomorphism Cl → {±1}; kΣ and
automorphic images preserving ψ stay in ker ψ; ker ψ ∩ G = ∅ by (a). Prime ideals: ψ([𝔮]) = (q/p). Classes of order ≤ 2:
by Lemma AMB below every such class contains an invertible ideal of norm k | 2d, so ψ = (k/p) = 1 under the hypothesis.
(c) immediate from ψ([𝔞]) = (N𝔞/p) = −1 and multiplicativity of the Legendre symbol; α(g) < p as α(g) ≤ √(4dp/3) < p for
p > 4d/3, which holds whenever G_d(p) ≠ ∅: p = 4abd − e ≥ 4abd − a − b ≥ 4d − 2 (as e ≤ a + b and
4abd − a − b ≥ 4d − 2 for a, b ≥ 1), so 4d/3 ≤ (p + 2)/3 < p (cross-model review). (d) Write x = x₂ + x_o. For j ≥ the exponent of Cl₂, 2^j x = 2^j x_o, and multiplication by 2^j is an
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
Lemma SR, m(g) ≤ √(d(2p + e)), so every 𝔰 with N(𝔰) < dp/√(d(2p + e_max)) — a *uniform sufficient* cutoff of order √(dp/2), distinct from the
class-dependent bound dp/m(g), which can be much larger — hits G only by an ideal identity —
i.e. N(𝔰) is itself a good norm A ≡ −1 (mod 4ad) dividing N_a (or a B- or de-norm) with the matching root: **the divisor
event**. *Proof.* Corollary FR′ of `Z70_CLASS.md` §1.6 (two distinct primitive invertible ideals with norm product < dp lie
in distinct classes) + Lemma SR. ∎ WORD is a *constraint*, not an exclusion: identity hits remain possible and can be
constructive. CERTIFIED: 0 violations of N(𝔰)·m(g) ≥ dp among all class-level (III) hits of item 3
(W1–W3, 5 values of d, 16 078 910 seed ideals in the target genus — review count).

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
wherever defined. [τ_xy keeps the letters x, y (swapped), so a word with x = 1 or y = 1 stays trivial. For (x, y, 1) with
x, y ≥ 2: n = xy − x − 1, n + y − (xy − 1) = y − x and |y − x| < xy − 1, so τ_xy is defined only for x = y, where it fixes the
word. τ_xy is an involution on its domain, so no non-trivial word maps to a trivial one. μ is defined on Triv only and lands
in Triv. (Boundary case found by the review: τ_xy(1, 75, 1) = (75, 1, 2) — trivial, as claimed.)]

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
scored once — the post-review rerun (D9) is deterministic and reproduces every registered W1–W3 statistic exactly); 𝔐 = 135
(W1 ∪ W2), 397 (W3). Pooled outputs `data/z70/gen/pool_W12.txt`, `pool_W3.txt`. Nulls: "U" uniform in 𝒯 (registered);
"A" per-prime half-octave α-null with independent-Bernoulli variance (registered A2); "AC" the same bins with the
finite-population (hypergeometric) variance — the correct conditional randomisation (review fix); "X" exact-α null: rate of
goodness among target units with the *same* minimal norm α at the *other* primes (LOO) and, as a check, 2-fold cross-fitted
rates ("XF", disjoint training primes); coverage nulls are trained and evaluated on primes with G ≠ ∅ only (review fix).
**All z-scores are model contrasts, not calibrated p-values** (dependence within primes and shared fitted rates are not
modelled; XF agrees with LOO to |Δz| ≤ 0.1, which addresses rate leakage only).

### 3.1 Item 1 — genus / ambiguous / Rédei / small-prime seeding
**Registered outcomes (K-GEN1 on W1 ∪ W2, A-null; BIAS needs z ≥ 4 there and same sign ≥ 3 on W3):**

| family | d = 1 | d = 2 | d = 3 | d = 5 | d = 7 |
|---|---|---|---|---|---|
| S_AMB (∩ 𝒯 ≠ ∅ at 0/0/0/290/301 of 591 primes; W3 0/0/0/767/784 of 1 561) | no statistic | no statistic | no statistic | 0 hits | 0 hits |
| S_RED: hits z / coverage z | −0.9 / −0.1 blind | +1.9 / +1.1 blind | +0.2 / +0.3 blind | +0.9 / −0.1 blind | +1.1 / +1.2 blind |
| S_CYC | −0.7 / +0.8 blind | **−3.8 / −4.4: K-GEN1 fails (negative)**; W3 −7.3 / −7.5 | −1.4 / −2.0 blind (W3 −6.2 / −6.6) | +0.4 / +0.3 blind | +0.4 / +0.4 blind |
| S_GEN2 | **+4.2** / +2.0 → W3 +5.1: **BIAS** | +3.6 / **+12.4** → W3 +20.8: **BIAS (coverage)** | **+8.0 / +8.7** → W3 +12.3 / +13.0: **BIAS** | −0.7 / +2.3 blind | **+10.1 / +11.1** → W3 +15.7 / +17.3: **BIAS** |

S_AMB: where S_AMB ∩ 𝒯 ≠ ∅ (d = 5, 7, about half the primes) it has 0 hits, as Lemma AMB proves; for d = 1, 2, 3 the set is
empty on this sample (no statistic). **No GEN-CANDIDATE**: no family reaches coverage 1 at any d (best S_CYC / S_GEN2 at
d = 1: 81–86 % of primes with G ≠ ∅).

**Decomposition of the BIAS and of the negative CYC departures (descriptive; the claimed pre-W3 timing of these analyses is author-reported only, D2/D8 — not verifiable from git):**
* *Exact minimal norm accounts for the hit counts (descriptive fitted contrast, units with α ≤ 5000 only — at W3 the X
  null drops 507 CYC units at d = 3 and 2 059 at d = 5, so it scores 230 of 232 resp. 138 of 142 CYC hit classes; it is not an
  equivalence test that "the rate is fixed by the norm").* Against X, every family and d has |z| ≤ 1.8 on W1 ∪ W2 and |z| ≤ 1.3 on W3
  (GEN2: +0.25, −0.45, −0.23, −0.55, −0.35 and −0.46, −0.67, +0.57, −0.41, +0.20 for d = 1, 2, 3, 5, 7; CYC W3 d = 2: +0.27,
  d = 3: −0.92 — the negative A-null departures of CYC disappear too). Read: a seed class is good as often as a target class
  with the *same minimal norm* at another prime; the coarse half-octave null misjudges the very small norms.
* *Which ideal carries the hit (seed-level identity, review fix).* S_GEN2: for **every** hit class one of its generating seed
  ideals (a product of two base ideals) *is itself a natural representative* — W3 4 062/4 062, 2 762/2 762, 1 214/1 214,
  1 874/1 874, 500/500 (d = 1, 2, 3, 5, 7), W1 ∪ W2 likewise 100 % — i.e. each GEN2 hit is the divisor event at a small norm
  (least natural norm ≤ 100 for 90 % of d = 1 hit units). S_CYC: the generating ideal 𝔮*^{±k} is natural for 2 582/2 798
  (d = 1), 342/434, 198/232, 92/142, 0/12 hit classes (W3); in the remaining cases the seed power is *not* natural but the
  class's reduced ideal is (2 796/2 798 …) — a class-level coincidence between 𝔮*^k (k ≥ 3) and a small natural
  representative (example found by the review: p = 106 537, d = 1, 𝔮*³ of norm 11³ = 1 331 lies in the class of the natural
  ideal of norm 127). These coincidences occur at the X-null rate (above). S_RED has no generating ideal; its hit classes'
  reduced ideals are natural in 175/177 units (W3, d = 1).
* *Coverage.* With matched conditioning the X-null coverage agrees for every family and d except S_GEN2 at d = 2
  (W1 ∪ W2 470/586 vs 411.6, z +5.8; W3 1 218/1 557 vs 1 076.6, z +8.6; d = 7 is now +0.2 / +1.0 — the earlier d = 7 excess was
  the conditioning artefact found by the review). The d = 2 excess is within-prime **exclusivity of same-norm seeds**: among
  2 143 groups of d = 2 GEN2 seed units with equal minimal norm, 0 had ≥ 2 good units vs 272.7 expected under independence
  (`gen2_coverage_decomp.txt`; d = 1: 180 vs 190.2): a fixed number of hits spread over more primes (EVIDENCE; for prime
  norms two natural A-ideals in different units would need N | (a₁ − a₂)(a₁ + a₂) with a₁ + a₂ < N — the composite-norm
  case is not proved). A repulsion, not generation.
* **Union over d ∈ {1, 2, 3, 5, 7}** of S_GEN2 covers 584/591 (W1 ∪ W2) and 1 543/1 561 (W3) primes, vs 581.3 and 1 536.5
  under X with independence across seeds and d (an approximation — the d = 2 exclusivity shows it is not exact); every
  uncovered prime is in 𝔐 (W3: 18 of 397 𝔐-primes, 0 of 1 164 others). The union is a menu of small-norm divisor events
  (B1-type); its failures concentrate on 𝔐, where all ψ = −1 seeds have norm ≥ n_p ≥ 11 (GW(c)).
* **First entry along S_CYC** (k = 1, 3, 5, …; W3): d = 1 — k = 1 at 1 228/1 560 primes, k = 3…9 at 33, k ≥ 11 at 283, never
  (G meets no odd multiple of [𝔮*]) at 16; for d ≥ 2, k = 1 is rare (166, 99, 46, 0 of 1 557, 1 525, 1 524, 1 185) and
  "never" occurs at 53, 221, 116, 185 primes. The cyclic orbit is a search with a heavy first atom at d = 1 (𝔮* natural when
  e.g. q* = 7, p ≡ 3, 5 mod 7), not a map. (RED / GEN2 first-entry orders were not implemented — D7.)
* **Item 1b — canonical representation fibres (Lemma REP):** the fibre a_c named by p = x² + d·(2a_c)² was barren in all
  **8 088** instances (d = 1, 2, 3: 2 152 each; d = 5: 565; d = 7: 1 067; W1–W3); comparison fibres a ∈ [a_c/2, 2a_c] ∖ {a_c}
  are good with mean probability 0.12–2.59 % each (`rep_fibres.txt`). CERTIFIED check of the PROVED lemma.

### 3.2 Item 2 — Rédei / 2-primary structure vs G: null (EVIDENCE; GRH-conditional invariant factors)
* r₄ is constant within p mod 840 strata on this sample (= 1 for d = 1, 2, 3; ∈ {0, 1} by residue class for d = 5, 7 —
  Rédei: the 4-rank is governed by quadratic symbols among the prime discriminants dividing D, here functions of p mod 840),
  so the registered within-stratum r₄ test is degenerate (D3); between strata r₄ is confounded with Mordell classes — not
  interpreted.
* r₈ within strata (registered; signal needs |t| ≥ 4 then ≥ 3): log(1 + |G_d|): W1 ∪ W2 t = +0.54, −1.00, −0.15, +0.21, −1.61
  (d = 1, 2, 3, 5, 7; 𝔐 only d = 7: −2.32); W3 −1.42, +1.54, +0.65, +1.34, −0.64; 1[G_d = ∅]: |t| ≤ 2.14 (W1 ∪ W2),
  ≤ 1.03 (W3). Not met.
* 2-primary positions of good classes in the target 2-coset: the registered χ² was referred to a with-replacement
  reference; against the finite-population expectation (B − 1)(N − K)/(N − 1) the observed values are close (W3:
  5 609 vs 5 599, 6 509 vs 6 663, 5 193 vs 5 436, 1 649 vs 1 679, 652 vs 725 for d = 1, 2, 3, 5, 7) — no excess of preferred
  positions; no calibrated statistic (sparse tables, the orbit count is approximated by npos/2), so this is descriptive.
  (The earlier "under-dispersion due to pairing" reading is withdrawn.)
* Emptiness: every (p, d) with G_d(p) = ∅ is listed with r₄, r₈ in `empty_fibres.txt` (868 pairs: d = 1: 2, d = 2: 9,
  d = 3: 106, d = 5: 95, d = 7: 656 — W1–W3); no within-stratum relation to r₈ (above).

### 3.3 Item 3 — small-split-prime orbits (primes ≤ 50, norm budget 64√(dp)): a divisor search; class level only below chance
* **Free region (Prop. WORD):** **0 violations** of N(𝔰)·m(g) ≥ dp among all class-level (III) hits (W1–W3, d = 1–7). Below
  N = √(dp) (j ≤ 0) there are no (III) hits except at d = 2: 6 (W1 ∪ W2) and 2 (W3) hit classes at j = 0, all with
  N·m(g) ≥ dp (e.g. p = 1 009 993: seed norm 1 421 < √(2p) ≈ 1 421.3, least natural norm 1 422; p = 10 023 553: 4 477 and
  4 478 — review). The earlier sentence "0 class-level hits below √(dp) for every d" was wrong and is withdrawn.
* (III) hits with threshold-local censoring (review fix: an identity is removed only once reached) vs the conditional α-null
  (AC) at the registered thresholds X_j = √(dp)·2^j, j = 0…3 — W3, d = 1: 0, 0, 280, 1 712 vs 2 562, 3 004, 3 850, 5 103;
  every d and window is negative (z −7.5 … −83). **No positive excess anywhere** (BIAS-3 does not fire). The deficit is the
  free-region exclusion — a seed of norm N cannot share a class with a good class of natural norm < dp/N unless it *is*
  that representative — which none of the nulls models; it is not evidence of an additional anti-coincidence.
* First entry (least seed norm with a good class): type (I) at 1 508/1 560 (d = 1), 1 383/1 557, 836/1 525, 791/1 524,
  200/1 185 primes of W3 (W1 ∪ W2: 567/590, 526/586, 287/521, 282/533, 55/311). **Registered K-GEN3** (no positive (III)
  excess AND type I ≥ 90 %): **fires for d = 1 only**; for d ≥ 2 it is **unresolved by its letter** (type I 89–90 % at d = 2,
  17–55 % at d = 3, 5, 7: 50-smooth natural norms are rare there, and the orbit reaches most of 𝒯 by 8√(dp)); no BIAS-3.

### 3.4 Item 4 — fixed-n word graphs: no orbit from trivial words to non-trivial certificates under the explicit maps
`scripts/z70_gen_graph.py` → `graph.jsonl` (34 inputs). Run: all 14 (★)-zero primes (409 … 8 813 281), all 26 𝔊*-zero primes
≤ 10⁶, 73, controls 9, 25, 105, 4545. The registered combined graph (Type II vertices, trivial integral points, CS/DL/DL′
edges) was **not** built — D6; the Type II part is the one-line remark below.
* Explicit maps s, τ_xy, τ_yz, μ, μ^s, ρ_L, ρ_R (and ρ_C for n ≤ 3·10⁴): **no component contains a trivial word and a
  non-trivial certificate** at any of the 34 inputs; where trivial certificates exist (p ≡ 5 mod 8 cases such as 37, 157,
  1621, 4357, 12301, 184837, 434437, 571741) the certificates in Triv-components are exactly those trivial ones. PROVED for
  s, τ_xy, τ_yz, μ, μ^s (Prop. SLICE: Triv_n and its complement are preserved); CERTIFIED for ρ_L, ρ_R, ρ_C at the tested n.
  **K-GEN4 fires only in a modified form: for the implemented word subgraph.** The registered combined test (Type II
  vertices, trivial integral points, CS/DL/DL′ edges) is **incomplete**; a word-subgraph disconnection does not exclude
  paths through additional Type II vertices.
* Slice moves (re-factorisations): certificates reachable from Triv_n lie 1–4 slice moves away; at several inputs some
  certificates lie in slice components without trivial words (e.g. 4 at 23929, 18 at 5 212 561, 28 at 8 813 281). Each
  entering move re-factorises ny + 1, n + x or n + z with a factor in a fixed residue class (e.g. 409: (1, 2, 410) → (4, 2, 59)
  uses 7 | 819 = 2·409 + 1 with 7 ≡ −1 mod 8) — the tied divisor event.
* Type II threefold (PROVED, one line): every positive solution at fixed (c, d) lies on (4acd − 1)(4bcd − 1) = 4c²dn + 1
  with the always-present integral point (a, b) = (0, −cn); the move between them is the choice of a divisor ≡ −1 (mod 4cd).
  Orbits can start at always-present points, but the first step is the divisor event.

### 3.5 Screens (`screen_F2.txt`, `screen_F4.txt`, `screen_F13.txt`)
* **F1:** G_d(m²) = ∅ for all 648 pairs (odd m ≤ 301, d ∈ {1, 2, 3, 5, 7}, gcd(m, d) = 1) — the computational face of GW(e).
* **F2 (12 R₈-zero primes near 10¹⁰), d = 1, 2:** G₂ ≠ ∅ at all 12 (|G₂| = 12–72: the C-even c = 1 line is empty, other c are
  not); hit classes: AMB/RED 0, CYC 30, GEN2 36; 0 FR violations. Nothing distinguishes C even from C odd.
* **F3 (285 composite (★)-zeros), census only:** G_d ≠ ∅ for some *tested coprime* d ≤ 7 at 281; at 57, 345, 2305 no
  solution among the tested coprime d (they have Type II solutions at excluded d: (1, 5, 2, 3) with d = 3; (1, 29, 10, 3),
  d = 3; (2, 58, 4, 15), d = 5 — review), and 4545 (the known Type II exception). The seed families were not run on
  composites (D5); GW(e) applies to non-square n ≡ 1 (mod 4) under its gcd hypotheses.
* **F4 (42 hard primes: 14 (★)-zeros, 38 𝔊*-zeros incl. 85 664 329 and 564 661 441, + 2521, 3361, 21841, 76441),
  d = 1, 2, 3, 5, 7:** every hard prime has G_d ≠ ∅ for some d ≤ 7 (59 empty (p, d) of 210); AMB 0 hits; RED 36, CYC 110,
  GEN2 210 hit classes; at 3 primes (3361, 2094481, 85664329) no family hits for any d; 0 FR violations.

## 4. Mandatory falsifier table — final

| screen | outcome | label |
|---|---|---|
| **F1 odd squares** | GW(e): at n = m² the character computation forces (m²/A) = −1, so G_d(m²) = ∅ for every d — the target coset does not exist and every seed family is vacuous. Where non-squareness (primality) enters a generative map: GW(a)/(c) — its output must be a class with ψ = −1, i.e. contain an ideal whose norm has a prime factor q with (q/n) = −1 (q ≥ n_p). 648 (m, d) pairs computed, all G = ∅. | PROVED + CERTIFIED |
| **F2 numerator 8 / C-even** | All lemmas are uniform in d (d = 2 = the numerator-8 Type II family; R₈ = its c = 1 line); nothing distinguishes C even from C odd, nothing claims positivity. At the 12 R₈-zero primes G₂ ≠ ∅ (c ≥ 2); hits only through small natural norms; 0 FR violations. Lemma REP kills the canonical d = 2 fibre at every p ≡ 1 (8). | PROVED / CERTIFIED |
| **F3 composites** | GW(e) holds for non-square n ≡ 1 (mod 4) with gcd(n, 2d) = 1 and gcd(a, n) = 1 (ψ_n = Jacobi (·/n)); AMB/ORD/WORD rely on the CLASS dictionary hypotheses — not claimed for all composites. Census: 281 of 285 composite (★)-zeros have G_d ≠ ∅ for a tested coprime d ≤ 7. Families **not run** on composites. Nothing here separates primes from composites beyond non-squareness. | PROVED (scoped) / CERTIFIED census / untested |
| **F4 known zeros** | All 42 hard primes run at d = 1, 2, 3, 5, 7: G_d ≠ ∅ for some d at each; no family is generative there (3 primes with no hit by any family at any d); AMB 0 hits; 0 FR violations. Item 4 run on all 14 (★)-zeros and all 26 𝔊*-zeros ≤ 10⁶. No positivity claimed. | CERTIFIED |

## 5. Verdict
**Narrowed: no tested rule found; not a HOT LEAD. ES is OPEN.** Scoped **exclusions** (PROVED): GW kernel seeds, AMB
(classes of order ≤ 2), REP (the named representation fibre). Scoped **constraints** (PROVED, not exclusions): ORD
(order/norm bound), WORD (below the free-region scale a hit is an identity — which may be constructive). Everything else
below is non-rejection of particular nulls for particular tested rules, not impossibility; no theorem excludes all
generative maps.
* *Which generative classes are excluded, and how* (the brief's fallback question):
  1. **Words in ψ-trivial seeds** — principal class, prime ideals of norm q with (q/p) = 1 (all of norm < n_p; on 𝔐 all of
     norm ≤ 7), classes of order ≤ 2 when d is squarefree, p > 3d and (q/p) = 1 for q | 2d; with x ↦ kx and ψ-preserving
     automorphisms: **PROVED blind** (GW(b)). Any generative output must involve a non-residue prime ≥ n_p (GW(c)).
  2. **Classes of order ≤ 2**: **PROVED never good** for squarefree d with p > 3d and p(4d − 3) > 8d (Lemma AMB; the second
     condition is needed: p = 5, d = 1 has the good class [2, 2, 3] of order 2); non-vacuous test: S_AMB ∩ 𝒯 ≠ ∅ at about half
     of the primes for d = 5, 7, 0 hits.
  3. **Halving (2-descent / Rédei)** — within {+, −, kx, ψ-preserving automorphisms, halving} the only step that leaves ker ψ
     (GW(d)); its canonical target S_RED is **blind as tested** (A- and X-null |z| ≤ 1.9; uniform null d = 1 W1 ∪ W2: −2.8). Good classes of small
     order need large natural norms (Lemma ORD).
  4. **Seed ideals of norm < dp/m(g)** (class-dependent; uniform sufficient cutoff ≈ √(dp/2)): hit G only by *being* a natural
     representative — the divisor event (Prop. WORD, PROVED *constraint*; identity hits may be constructive; 0 violations in
     ≈ 1.6·10⁷ seed ideals). Beyond that scale class-level coincidences occur, below
     every null tried.
  5. **Canonical principal seeds from representations p = x² + d(2a)²**: the named fibre is **PROVED barren** for
     p ≡ 1 (8) (Lemma REP; 8 088 instances CERTIFIED) — the representation makes N_a a norm from ℤ[√−2d], a "square" for
     the character separating the target residue: the T1 mechanism again.
  6. **Small-prime genus seeds and cyclic orbits** (S_CYC, S_GEN2): **as tested**, they hit G as often as classes of the same
     minimal norm (descriptive X contrast on α ≤ 5000, |z| ≤ 1.1 on W3 for these two families; **coverage exception: GEN2 at
     d = 2 exceeds its coverage null, z +8.6 on W3** — same-norm exclusivity); every GEN2 hit is a seed-ideal identity at small norm; CYC hits are seed
     identities or class-level coincidences of 𝔮*^k with a small natural representative at the null rate. A congruence menu
     (B1): union over d ≤ 7 covers 98.8 %, failures all in 𝔐.
  7. **Fixed-n explicit maps** (s, τ, μ, ρ_L, ρ_R, ρ_C): never connect trivial words to non-trivial certificates *in the word
     subgraph* (PROVED for s, τ, μ; CERTIFIED for ρ at 34 inputs; the registered combined Type II graph is incomplete, D6); slice re-factorisations reach certificates, but each entering step is the
     divisor event; a uniform fibrewise move other than the swap is not known (Assessment).
  8. **Rédei 4-/8-ranks**: r₄ is a congruence invariant on this sample; r₈ and 2-primary positions show no detected relation
     to |G| or emptiness.
* *Escape hatches left open (Assessment).* (i) Non-group-theoretic, non-fibred maps producing ideals of norm ≫ √(dp) whose
  classes correlate with G — nothing tested here points to one (every class-level coincidence observed is at or below the
  nulls); (ii) maps using a non-residue input in an essential, non-menu way — GW forces this ingredient, the observed hits use
  it only through small natural norms; (iii) automorphisms not preserving ψ (not canonical); (iv) the d = 2 same-norm
  exclusivity and the CLASS anti-coincidence are repulsions, not generation.
* **Hard screens (FRONTIER §4).** T1 squares: passes (GW(e); vacuous). 8/131: no positivity claim; uniform in d. Tied
  modulus: every GEN2 hit and most CYC hits are seed-ideal identities, i.e. divisors ≡ −1 (mod 4ad); the rest are
  coincidences with small natural representatives — the tie is not loosened. Fixed p: no statement produces a solution
  without a divisor event.

## 6. Proposed FRONTIER §7 text (do not edit FRONTIER here)
"z70 GEN (`Z70_GEN.md`; narrowed — no generative class map found). Question: can a good class of Cl(−4dp) be produced from
data present at every prime? PROVED: (GW) G_d(p) ⊂ ψ^{−1}(−1) (ψ = genus character at p): words in ψ-trivial seeds (principal,
prime ideals of norm < n_p — on 𝔐 all of norm ≤ 7 — and, under AMB's hypotheses, the ambiguous classes) are blind; every good
class has minimal and natural norms ≥ n_p; within {+, −, kx, ψ-preserving automorphisms, halving} only halving (Rédei)
leaves ker ψ; (AMB) classes of order ≤ 2 are never good (squarefree d, p > 3d, p(4d − 3) > 8d); (ORD) A^{ord g} ≥ dp; (WORD, a constraint) a
seed ideal of norm < dp/m(g) hits G only by being a natural representative (= the divisor event, possibly constructive); (REP) the fibre named by
p = x² + d(2a)² is barren for p ≡ 1 (8) (norms from ℤ[√−2d]); (SLICE) fixed-n coordinate-preserving moves are
re-factorisations; s, τ, μ preserve trivial words. EVIDENCE (p ≡ 1 (24) in 10⁵–1.02·10⁷, d = 1, 2, 3, 5, 7, held-out W3; z's
are model contrasts; descriptive, α ≤ 5000): Rédei (2-power-torsion), cyclic and genus-seed families hit G at the rate of
classes with the same minimal norm (coverage exception: genus seeds at d = 2, same-norm exclusivity); every genus-seed hit is a small-norm seed-ideal identity; union over d ≤ 7 covers 98.8 % (failures all in 𝔐);
smooth-prime orbits show no class-level excess, 0 FR violations; r₈ / 2-primary positions unrelated to |G|; fixed-n
explicit maps never join trivial words to certificates in the word subgraph (all 14 (★)-zeros, 𝔊*-zeros ≤ 10⁶; the
registered combined Type II graph and the composite seed-family screen were not done). OPEN (untested candidates from the
cross-model review): mixed non-residue words with root-sensitive selection; halving with an odd-part anchor;
representation-neighbour seeds a_c ± 1. Not a HOT LEAD."

## 7. Bottom line
No tested rule generates a good class from the data every prime carries. Five scoped theorems survive hostile checking:
three **exclusions** — seeds in the kernel of the genus character ψ that every good class violates are blind (GW, the
class-group face of T1), classes of order ≤ 2 are never good (AMB), the fibre named by p = x² + d(2a)² is barren (REP) — and
two **constraints**: good classes have large order relative to their natural norms (ORD), and below the free-region scale a
seed that hits a good class *is* a natural representative (WORD — such identity hits are the divisor event and may be
constructive; WORD does not disqualify them). Within {+, −, kx, ψ-preserving automorphisms, halving} only halving leaves
ker ψ; the tested Rédei target (zero odd part) was blind in the data. Seeds supplied with ψ = −1 (non-residue primes, some
ambiguous classes) are *not* covered by GW. In 2 152 primes × 5 values of d the tested families hit G at the rate of classes
with the same minimal norm (descriptive, α ≤ 5000; coverage exception GEN2 at d = 2); fixed-n explicit moves never start an
orbit from trivial words in the word subgraph (the combined Type II graph is untested). The genus obstruction uses
non-squareness; primality also supplies the coprimality the ideal dictionary needs. No theorem here excludes all generative
maps.

**OPEN — uncovered generative candidates (from the cross-model review; concrete tests, not endorsed leads):**
1. **Mixed non-residue words with root-sensitive selection.** At each (p, d) take the first three split primes in each genus;
   form exponent words in {−2, −1, 0, 1, 2} of support ≤ 3, keep the target genus, output four distinct classes ranked by
   |b|/a of their reduced forms (tie-breaking frozen before a fresh window). Test union coverage, output fraction and
   exact-α contrasts on fresh primes and F1–F4. (Neither S_CYC nor S_GEN2; aggregate smooth-orbit deficits do not exclude a
   selected subset, especially beyond WORD's free region.)
2. **Halving with an odd-part anchor.** Choose the least split prime in the principal genus whose class has non-zero odd
   component; enumerate solutions of 2x = h and 4x = h, keep target-genus classes, rank by a fixed small root-based rule.
   Test coverage on all inputs, counting absence of an anchor as failure. (GW(d) permits these shifted 2-primary cosets;
   S_RED tested only the zero-odd-part coset.)
3. **Representation-neighbour seeds.** For d = 1, p ≡ 1 (mod 8), p = x² + 4a_c²: at a = a_c ± 1 (positive) take the least prime
   factor q of p + 4a² with (q/p) = −1 and output [(q, 2a + √−p)] (no tied-residue test in choosing q). Test the frozen
   two-class rule and fixed alternate-d extensions on fresh primes and hard zeros, scoring absent q as failure. (REP excludes
   a_c only; WORD permits constructive identity hits; at squares the Jacobi −1 filter gives no seed.)

Not a HOT LEAD. ES is OPEN.

## 8. Reproduction (each command under `ulimit -v 6000000`, `timeout ≤ 1800`)
* validation: `uv run --with cypari2 --with sympy --with numpy python scripts/z70_gen_validate.py` (→ `validate.txt`).
* registered runs (post-review pipeline; refuses to overwrite, stops on error): `scripts/z70_gen_runwin.sh W1 100000 130000 DIR`,
  `… W2 1000000 1030000 DIR`, `… W3 10000000 10200000 DIR` (raw records archived in `runs_W123.tar.xz`); pooling
  `python3 scripts/z70_gen_pool.py DIR/run_W1_d*.jsonl DIR/run_W2_d*.jsonl` → `pool_W12.txt` and `… DIR/run_W3_d*.jsonl` →
  `pool_W3.txt` (asserts unique (p, d)); `python3 scripts/z70_gen_covdecomp.py DIR` → `gen2_coverage_decomp.txt`;
  `python3 scripts/z70_gen_empty.py DIR/run_W*.jsonl` → `empty_fibres.txt`.
* screens: `uv run --with cypari2 python scripts/z70_gen_run.py OUT d list <inputs>` (F2, F4; raw in `screens_raw.tar.xz`,
  first-pass pipeline — the registered statistics are unchanged by D9), `python3 scripts/z70_gen_screens.py OUT…`;
  F1/F3 `uv run --with cypari2 python scripts/z70_gen_f13.py data/z70/gen/screen_F13.txt`.
* item 1b: `uv run --with cypari2 python scripts/z70_gen_rep.py data/z70/gen/rep_fibres.txt`; item 4:
  `uv run --with cypari2 python scripts/z70_gen_graph.py data/z70/gen/graph.jsonl <n…>` (appends).

## 9. Review log
**Internal hostile review** (requested in deep mode through the review tool, which ran it on `openai/gpt-6-astra`; no
provider / auth / quota error) at `14bc8dc47`: *request changes* — 12 major, 3 minor items; it reproduced both pooled files,
both screen summaries, the coverage decomposition, all 249 validation checks and the 73/409 graphs byte-for-byte, and found
the small-fibre enumeration, genus targets, seed construction independent of G, ORD, REP and WORD sound in their domains.
Fixes applied (all in this memo / the scripts; full W1–W3 rerun, D9):
1. "every hit is an ideal identity" conflated *reduced ideal natural* with *seed ideal natural* → seed-level identity check
   added (`seedid`); GEN2: every hit is a seed identity; CYC: 2 582/2 798 … (d = 1, W3), the rest class-level coincidences of
   𝔮*^k with small natural representatives (§3.1); headline/bottom line reworded to "tested rules".
2. "no class-level hit below √(dp)" false at d = 2 (6 + 2 hits, all respecting FR′) → corrected (§3.3).
3. coverage null trained on all primes but evaluated on G ≠ ∅ → matched; the d = 7 coverage excess disappears, d = 2 remains
   and is attributed to same-norm exclusivity (§3.1).
4. α-null variances not the conditional randomisation → "AC" null with finite-population hypergeometric variance added; X
   null cross-fitted; all z declared model contrasts.
5. item-3 profile censored early hits by later identities → threshold-local censoring (§3.3).
6. K-GEN1 misreported (CYC d = 2 fails already on W1 ∪ W2; AMB has no statistic) → family × d outcome table (§3.1).
7. GW(d) "only group-theoretic operation" overclaimed → restricted to {+, −, kx, ψ-preserving automorphisms, halving};
   counterexample with a non-ψ-preserving automorphism recorded.
8. AMB summaries dropped p(4d − 3) > 8d (p = 5, d = 1 counterexample) → restored everywhere.
9. composite scope: GW(e) needs n ≡ 1 (mod 4) (n = 15 counterexample); F3 census wording "tested coprime d"; composite-family
   claim removed.
10. 2b χ² referred to the wrong reference → finite-population expectation reported, reading withdrawn (§3.2).
11. ledger incomplete → D6–D8 added; the 19 omitted item-4 inputs were run (K-GEN4 unchanged).
12. unconditional class-number cross-check claimed but not implemented → claim withdrawn (§1).
13. numbers: 22 validation inputs; 16 078 910 seed ideals; S_AMB ∩ 𝒯 ≠ ∅ for d = 5, 7 at ≈ half the primes; r₈ d = 7 t −1.61;
    RED A-null d = 2 +1.90; 8 088 canonical fibres, comparison up to 2.59 %; CYC first-entry "never" counts → corrected.
14. τ_xy boundary case (x = 1 or y = 1) → proof text fixed.
15. append-mode reruns could double count → run script refuses existing output, runwin stops on error, pooling asserts
    unique (p, d).
Owed: cross-model (Astra) review per the wave flow — note that this internal review was already produced by Astra; the
orchestrator may prefer a different reviewer.

## 10. Cross-model review (`data/z70/xreview/REVIEW_GEN.md`, Astra, at `49de2aa1c`): ACCEPT-WITH-FIXES
The reviewer reproduced the pooled files, validation (249/249), seed identities, union coverage, 8 088 barren canonical
fibres, F2/F4 counts and the 73/409 graphs, and found GW, AMB, ORD, WORD, REP, SLICE correct in their stated scopes. Fixes
applied: (1) exclusions (GW kernel, AMB, REP fibre) separated from constraints (ORD, WORD); constructive identity hits
explicitly allowed (§0, WORD, §5, §7); the §7 blanket claim "always-present seeds lie in the kernel" removed (false for
non-residue seeds and some ambiguous classes). (2) Exact-norm (X) claims qualified as descriptive, α ≤ 5000 (dropped-unit
counts given), and the GEN2 d = 2 coverage exception added to the compact summaries; the pre-W3 chronology of the D2
analyses labelled author-reported, not verified. (3) Item 4: combined Type II graph labelled incomplete, K-GEN4 stated as a
modified word-subgraph result, also in the FRONTIER text; composite seed-family screen remains untested. (4) GW(c)'s missing
non-empty-fibre size argument added; GW(b) restricted to invertible prime ideals (conductor primes); WORD's uniform
sufficient cutoff distinguished from the class-dependent dp/m(g); "primality enters only as …" replaced by "the genus
obstruction uses non-squareness; primality also supplies dictionary coprimality". The reviewer's three uncovered candidates
are recorded as OPEN with their tests in §7.
