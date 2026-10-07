# Hostile review R90 of EXCEPTIONAL_WEIGHTS2.md (task O90)

Reviewer branch `side-agent/review-weights2`; author branch `side-agent/crt-alignment-w`
(merged at review start). Author's document not edited. From-scratch scripts:
`scripts/review_weights2_*.py`. ES is not solved; no θ > 3/4 is claimed by anyone here.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (min over 𝔉_A = M_{𝔊_max}) | SOUND (trivial) |
| Lemma 1.1 "Consequence for refutations" (refuting (W) with 𝔊 ⊇ 𝔊_X ⇒ θ > 3/4 for E_pr) | GAP — literally wrong as stated (D1, D2) |
| Lemma 2.1 (period forcing) | SOUND |
| Lemma 2.2 (prime case) | SOUND |
| Lemma 2.2 "same holds for composite moduli" | GAP (D3) |
| Prop 3.1 (prime-slice mass ≫ (log Y)², BV with 2^{ω(q)} weights) | SOUND (lower bound; ineffective) — written out in §A |
| "≍ (log Y)²" (upper bound, used in Cor 4.2/§5/§7) | GAP, harmless (D5) |
| Cor 3.2 | SOUND; composite remark can be upgraded on units via CEILINGS Prop 1.1 (D6) |
| Prop 4.1 | SOUND (trivial first moment) |
| Cor 4.2 | SOUND-AFTER-REPAIRS ("essentially all" is in mass, not in number; D7) |
| Prop 4.3 formula (4.1) and Fejér identity | SOUND (re-derived; D8 minor) |
| Prop 4.3 size Assessment | correctly labelled; heuristic mis-stated (congruence, not equation; D9); my EVIDENCE supports it uniformly in h ≤ 2·10⁴ |
| Lemma 5.1 | SOUND (prime slices only, as the author says) |
| Prop 5.2 | SOUND |
| "(W) is precisely … attainment of the growing-dimension large sieve"; 2/3 prime exponent | overclaimed prose (D10) |
| Prop 5.3 premise ℛ(ℓ) ⊆ QNR | SOUND (re-proved; brute force ℓ ≤ 10⁴: 0 failures; also Jacobi(·|M) = −1 for all composite M ≤ 10³) |
| Prop 5.3 √(N log N) cap | SOUND-AFTER-REPAIRS (one false inequality in the proof, D11; scope D12) |
| §6 EVIDENCE | REPRODUCED (independent code, Y ≤ 10⁶); off-by-one-prime cutoff in the author's S(Y) (D13) |
| §7 verdict "(W) open; CRT plan as specified fails" | SOUND, after D1–D3 (item 1 must be weakened) |

**Overall.** No FATAL defect. The mathematical core (Props 3.1, 4.1, 5.3, Lemmas 2.1, 5.1)
is correct. Two MAJOR defects are in the one sentence that sells a refutation of (W) as "a
θ > 3/4 theorem for E_pr" (D1 direction of inclusion + selector classes; D2 quantifier). D3
is an unproved extension used in prose.

## Defects

**D1 (MAJOR) — §1 "Consequence for refutations": inclusion runs the wrong way.**
Location: EW2 §1, paragraph "*Consequence for refutations (PROVED, from W1 Prop 5.1(a′))*";
repeated in §7 item 1 and in the O90 report table row "Lemma 1.1".
W1 Prop 5.1(a′) gives `E_pr(N) ≤ K + y + M_{𝔊_X}(N)`. For 𝔊 ⊇ 𝔊_X, Lemma 1.1 gives
`M_𝔊 ≤ M_{𝔊_X}` — an upper bound for M_𝔊 says nothing about M_{𝔊_X}. The claimed
`E_pr(N) ≤ K + y + M_𝔊(N)` needs a *different* input: every exceptional prime p > (some
bound) lies in 𝒜(𝔊), i.e. **every class of 𝔊 ∖ 𝔊_X is prime-forced** (contains no
exceptional prime above the bound). This is false for the selector classes that 𝔉_A
allows: W1/KARY2 selector classes are `0 mod p`, and 𝔉_A admits them for all p ≤ N^A. The
class `0 mod p` contains the prime p, so every exceptional prime p ∈ (y, N] is removed by
a member of 𝔊_max. Hence for 𝔊_max (the very family Lemma 1.1 reduces to) the bound
`E_pr ≤ K + y + M_𝔊` is **not** available; the true statement is
`E_pr(N) ≤ K + y + #{exceptional p ≤ N : p ∈ some class of 𝔊∖𝔊_X} + M_𝔊(N)`, and the middle
term is uncontrolled (≤ π(N)) once selector moduli p ∈ (y, N] are present.
*Repair.* State: "If 𝔊_X ⊆ 𝔊 and every class in 𝔊 ∖ 𝔊_X is an ℛ(M)- or Case-A class (which
are forced for every n > K′ in the class, by the polynomial identities — cite LS7 Lemma 1.1 /
ElT Prop 1.4 and state K′), then `E_pr(N) ≤ max(K,K′) + y + M_𝔊(N)`." Note explicitly that
𝔊_max is *not* such a family (its selector classes 0 mod p, y < p ≤ N^A, delete all primes
in (y, N^A]; e.g. 𝒜(𝔊_max) ∩ [1, N^A] contains no prime > y), so a refutation of (W) via
𝔊_max does **not** yield any E_pr bound. The sentence "a refutation therefore needs an
argument at least as strong as a new exceptional-set theorem" must be restricted to
refutations using prime-forced families ⊇ 𝔊_X. (Equivalently: redefine 𝔉_A so that selector
classes have moduli ≤ y only, as in 𝔊_X; then 𝔊_max changes and Lemma 1.1 still holds.)

**D2 (MAJOR) — quantifier: "refuting (W)" ≠ "θ > 3/4".**
Location: EW2 §1 same paragraph ("Refuting (W) … i.e. proving `M_𝔊(N) ≤ Ne^{−(log N)^θ}`
with θ > 3/4"), §7 item 1, report row "Lemma 1.1".
(W) is `∃C, N₀ ∀N ≥ N₀: min_𝔊 M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}`. Its negation is: for every C
there are infinitely many N with `min_𝔊 M_𝔊(N) < N e^{−C(log N)^{3/4}}`, i.e.
`M ≤ N e^{−ω(N)(log N)^{3/4}}` along a **subsequence** with ω → ∞ arbitrarily slowly. This is
neither "θ > 3/4" (a power improvement in the exponent) nor valid for all N. Even with D1
repaired, ¬(W) gives only `E_pr(N_k) ≤ N_k e^{−ω(N_k)(log N_k)^{3/4}}` on a sequence N_k
(and monotonicity of E_pr does not fill the gaps). *Repair.* Replace "refuting (W) … would
prove θ > 3/4" by "a bound `M_𝔊(N) ≤ N e^{−(log N)^θ}` (θ > 3/4, all large N) for a
prime-forced 𝔊 ⊇ 𝔊_X would prove θ > 3/4 for E_pr; a mere refutation of (W) gives an
o-improvement of the constant along a subsequence." (W1 Prop 5.1(c) already phrases the
negation correctly with ω(N) → ∞; EW2 should match it.)

**D3 (MAJOR, unproved extension) — Lemma 2.2 for composite moduli.**
Location: EW2 §2, sentence after the proof of Lemma 2.2 ("The same holds for any subfamily
with lcm ≤ N (composite moduli, |ℛ(M)| = M^{o(1)}). So period forcing never costs more than
`(log N)^{o(1)}`"), and §7 item 2 ("forcing reaches only subfamilies of period ≤ N, mass
`(log N)^{o(1)}`"). Two problems. (i) For prime slices "cost" `log(1/δ′) = −Σ log(1−p_ℓ)`
is ≤ 2·mass, but for composite moduli the union of classes is not a product, so a mass bound
does not bound the cost; one needs a lower bound for the avoider density δ′ of the union,
and the union bound `δ′ ≥ 1 − Σ_{M|L}|ℛ(M)|/M` is useless as soon as the mass exceeds 1.
(ii) Even the mass is not `(log N)^{o(1)}` by the stated argument: for L ≤ N the divisor
sum `Σ_{M|L} M^{−1+ε} = Π_{ℓ^a‖L}(1 + …)` over the primorial L ≈ N is `exp(≍(log N)^ε/ε)`,
not `(log N)^{ε}` (the true mass may well be polylogarithmic, but that needs an argument
about τ((M+1)/4)² on divisors M of L, not given). What is easy for ℛ-classes: for
`4uv | M+1` the Jacobi symbol `(−u/v | M) = −1` (reciprocity, as in Prop 5.3's premise), so
unit squares mod L avoid every ℛ(M), M | L, and δ′ ≥ (density of unit squares mod L)
`≫ 2^{−ω(L)}/log log N`, i.e. cost `≤ (log 2)·log N/log log N + O(log log log N)` — far below the 3/4 scale, which is all §§2–3 actually need, but
not `(log N)^{o(1)}`. (Selector classes 0 mod p, p | L add only `Π(1−1/p)`, cost
`≪ log log log N`, harmless.) *Repair.* Either restrict the `(log N)^{o(1)}` claim to prime
slices, or replace it by the proved bound `cost ≤ ω(L) log 2 + O(log log log N) ≪ log N/log log N`
(via quadratic residues; note this uses the D-independent fact that ℛ(M) ⊆ non-squares
mod every prime ℓ | M, which needs its own one-line proof for composite M), or give a real
argument (Haar exponent: if all moduli ≤ e^𝓛 are included the cost is ≍ 𝓛³ with
𝓛 ≍ log log N by CEILINGS_UNIFIED, consistent with `(log N)^{o(1)}`, but lcm ≤ N does not
mean "all moduli ≤ e^𝓛" and the general case needs proof).

**D4 (MINOR) — Lemma 2.1 follow-up sentence.** "a subfamily costs its density in every
window **only if** its period is ≤ N/k": Lemma 2.1 gives "if", not "only if". Repair: "if".
