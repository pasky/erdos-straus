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

## 1.6 Smoke tests done before registration
None (engine written after this registration).

## 2. Theorems (statements; proofs in §3 when written)
**Theorem GW (genus wall; to be proved in §3).** (a) G_d(n) ⊂ 𝒯_d(n), a single genus coset with χ_n = −1 (n prime; for
general non-square n coprime to 2d the corresponding product of genus characters); 𝒯_d(m²) = ∅. (b) If Σ ⊂ Cl has all
genus-character values of the principal genus restricted to χ_n (χ_n(Σ) = 1), then ⟨Σ⟩ ∩ G_d(n) = ∅; in particular the
classes of all prime ideals of norm q with (q/n) = +1 (split or ramified) and the ambiguous classes whose χ_n-value is
+1 generate a subgroup blind to G. On 𝔐 this contains every prime ideal of norm ≤ 7 and, for d | 210, all ambiguous
classes over 2, 3, 5, 7 and over p. (c) Every class of 𝒯 has all its ideal norms N (gcd(N, n) = 1) with (N/n) = −1, hence a
prime factor q ≥ n_p (least quadratic non-residue). (d) The only escape from a χ_n-trivial seed subgroup by group
operations is division by 2 (𝒯 ⊂ Cl ∖ Cl², ker χ_n ⊇ Cl²): the halving closure of ⟨Σ⟩ is ⟨Σ⟩_odd + Cl[2^∞]-shifts — either
the whole of Cl (a search) or, canonically, S_RED.
