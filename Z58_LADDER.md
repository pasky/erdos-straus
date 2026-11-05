# Z58_LADDER — mechanism III (size-controlled covering) and the ladder: checkpoint 1

Status: z58 lane LADDER (brief `z52bbriefs/z58_lanes.md` §LADDER, rules `z52bbriefs/z53_depth.md` with z53 → z58).
Internal, not yet reviewed. **ES is OPEN; nothing here proves or disproves ES or (MS).** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_ladder_*`, data `data/z58/ladder/`.

## 0. Falsifier table (mandatory; checkpoint version — restated at the end)

Object of this lane: mechanism III of `Z57_SYNTH.md` in its *size-controlled, symmetric* form (§1), and the new
primality-free rung L2^𝔐 (§2).

| screen | behaviour of the idea | identifiable step |
|---|---|---|
| F1 odd squares | μ(m²) = ∞ for every odd m (no hit class contains a square, Lemma A.1(b)); L2^𝔐 excludes squares by hypothesis | the only use of "n is not a square" is that χ_n = (·/n) is a non-principal real character, so a hit modulus can contain a prime ℓ with χ_n(ℓ) = −1 (Lemma 1.1(c)) |
| F2 C-even sub-line | SC(D) and L2^𝔐 are *statements*, not proofs; restricted to C even they become R₈-statements, which are false at 10¹⁰ (4 Mordell zeros). A proof must use moduli d ≡ 3 (mod 8) (C odd); nothing in §§1–2 does this yet | not yet identified (open) |
| F3 composites | **new data (§2):** inside Mordell's classes, non-square composites have the same μ-statistics as primes to 2–3 digits, and R(n) = 0 at 18 composites ≤ 10⁸ in 𝔐 (last 17 401 609) against 9 primes (last 8 813 281). Of the 285 F3 composites, 270 lie outside 𝔐 (factor 3, 5 or 7, or non-square class mod 840) | primality is used only through n mod 840 ∈ 𝔐 (equivalently: coprime to 210 and a square class) and non-squareness — EVIDENCE that nothing else about primality matters statistically |
| F4 known zeros | SC(1.93 p^{2/3}) is *equivalent* to (MS) (Lemma 1.1); it holds at no zero; any proof needs threshold > 8 813 281 (primes) and, for L2^𝔐, > 17 401 609 | threshold |

**Not a HOT LEAD** (checkpoint assessment): no step yet fails on the C-even sub-line.

## 1. Mechanism III, size-controlled and symmetric

**Definition.** For n ≥ 1 let μ(n) := min over (★)-solutions (u, B, C) of min(4uC − 1, 4BC − 1, 4uB) (μ = ∞ if R(n) = 0).

**Lemma 1.1 (PROVED).** Let (u, B, C) solve 4uBC − u − B = n.
* (a) n ≡ −u (mod 4uC − 1), n ≡ −B (mod 4BC − 1), n ≡ −(u + B) (mod 4uB); conversely each of these congruence events
  (with the stated divisibility shape: k | (d+1)/4 for the first two; n ≥ 4uB − u − B for the third) yields a solution.
* (b) min(4uC − 1, 4BC − 1, 4uB) ≤ (64/9)^{1/3}(n + 1)^{2/3} < 1.9231 (n + 1)^{2/3}. Hence R(n) ≥ 1 ⟺ μ(n) < 1.9231(n+1)^{2/3}.
* (c) For a prime p ≡ 1 (mod 4): μ(p) ≥ n_p (least quadratic non-residue).

*Proof.* (a) n + u = B(4uC − 1), n + B = u(4BC − 1), n + u + B = 4uBC; converses: Lemma A.1(a) of Z57_SYNTH for the
d-forms; for the pair form put C := (n + u + B)/(4uB) ≥ 1. (b) (4uC)(4BC)(4uB) = 4(4uBC)² = 4(n + u + B)², and
uB ≥ u + B − 1 gives u + B ≤ (n + 4)/3 when C ≥ 1 [4uBC ≥ 4(u + B − 1) ⇒ n ≥ 3(u + B) − 4], so n + u + B ≤ (4n + 4)/3; the
least of the three integers 4uC, 4BC, 4uB is at most the cube root of their product (FAMTRY §4.5 records the same bound).
(c) Every d-form hit class has Jacobi symbol −1 (Lemma A.1(b)), so the hit modulus d has a prime factor ℓ with
(p/ℓ) = −1, i.e. (ℓ/p) = −1, so d ≥ n_p. For the pair form, χ_{−4uB}(−(u+B)) = −1 (FRONTIER §2.2) and p ≡ −(u+B), so
(−uB/p) = −1, (uB/p) = −1, and uB has a prime factor ℓ ≥ n_p. ∎

**Size-controlled covering statement SC(D).** *For every prime p > P in 𝔐 there is a solution with μ ≤ D(p).*
SC(1.923(p+1)^{2/3}) ⟺ (MS) (Lemma 1.1(b)); SC(D) for smaller D is a rung *above* (MS). Prop A.3 of Z57_SYNTH kills
every bounded D; `POINTWISE_OMEGA13.md` Thm 5.1 (PROVED modulo cited inputs) kills D ≤ exp((log p)^{1/4−ε}) for Type II
witness moduli.

**Data (CERTIFIED counts, one engine; `scripts/z58_ladder_mu.c`, `data/z58/ladder/mu_1e8*.txt`).** All n ≡ 1 (4) ≤ 10⁸,
moduli up to CAP = 420 000 ≥ 1.923(10⁸+1)^{2/3}, so "μ > CAP" ⟺ R(n) = 0 there. Reproduces the 14 known prime zeros and
(lpf ≥ 11 part of) the F3 list ≤ 8·10⁶ exactly.
* Records of μ over primes p ≡ 1 (4): 12 847 at 963 481 (= p^{0.685}), 14 559 at 9 477 889 (p^{0.598}), 44 771 at
  98 943 049 (p^{0.581}); all three in 𝔐. The record exponent is decreasing; at accessible sizes the symmetric least hit
  modulus of the hardest primes is a sizeable power of p — no compression below the trivial p^{2/3} scale is visible.
* In 𝔐 the fraction of primes with μ > 100 is 0.20–0.21 in every decade 10⁵…10⁸ (outside 𝔐: 0.011).

## 2. A primality-free rung: L2^𝔐

**L2^𝔐(P).** *R(n) ≥ 1 for every non-square n > P with n mod 840 ∈ 𝔐.* Trivially L2^𝔐(P) ⟹ L2(P) = (MS) at threshold P.
(𝔐 is the subgroup of squares of (ℤ/840)^×, so n ∈ 𝔐 ⇒ gcd(n, 210) = 1.)

**Data (CERTIFIED by the same scan, cross-checked against the F3 list).** Non-square n ≤ 10⁸ in 𝔐 with R(n) = 0:
9 primes and 18 composites: 1969, 2641, 5161, 18001, 23881, 90889, 112849, 199369, 345361, 349609, 510169, 539281,
897961, 2 956 321, 3 210 601, **8 725 201 = 29·300869, 12 538 801 = 11·47·79·307, 17 401 609 = 47·370247** (last three
new: above the F3 range). μ-statistics of composites in 𝔐 vs primes in 𝔐, decade [10⁷, 10⁸]: P(μ > 100) 0.232 vs 0.209,
P(μ > 10³) 0.0156 vs 0.0125, P(μ > 10⁴) 3.0·10⁻⁴ vs 2.1·10⁻⁴, mean log μ / log log n 1.336 vs 1.305. For 100-rough
composites in 𝔐 the match is closer still: 0.2091 / 0.0129 / 2.13·10⁻⁴ / 1.305 (EVIDENCE).

*Reading (Assessment).* F3 says (MS) over all n ≡ 1 (4) is false; it does **not** say primality is needed on 𝔐. On 𝔐
the composite analogue has a few more zeros at these sizes (small factors 11, 13, … exclude moduli), but is consistent
with all data above 1.75·10⁷. If L2^𝔐 is true, a proof of (MS) may be blind to primality on 𝔐: the F3 screen then
reduces to "uses n mod 840 ∈ 𝔐 and a threshold".

## 3. Next steps (in progress)
* Extend the 𝔐-composite zero census to [10⁸, 10⁹] (per-n decider with the μ-bound as exact cut-off).
* F2 inside III: which share of minimal hits uses C odd / d ≡ 3 (mod 8); is there a structural reason that d ≡ 3 (8)
  moduli are needed in 𝔐?
* Ladder arrows: a provable rung strictly between L2 and L3 would prove (MS) (L3 ⟹ S ⟹ L2 and S proved ⟹ L2); the
  meaningful question is rungs *above* L2 that are structurally easier (SC(D), L2^𝔐) and provable rungs *below* L2.
