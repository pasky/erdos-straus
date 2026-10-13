# R183 — hostile review of O183 `T1_TEMPLATE.md` (T1-bearing ES variants provable at primes)

Reviewer: R183 side agent. Documents: T1_TEMPLATE.md (merged from side-agent/t1-template), BRAINSTORM/bsJ_mute_place_unit_orbit.md,
reviews/agent-reports/AGENT_REPORT_O183.md. From-scratch scripts: `scripts/review_t1t_*.py` (own ℤ[φ] / ℤ[∛2] / ℤ[√d]
arithmetic, own tame and 2-adic Hilbert symbols; none of the author's `t1t_*` code is used).

Status: in progress.

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### C1. Definition of V_φ (§1) — SOUND
`4/n = 1/x + 1/y + 1/z`, x, y, z ∈ ℤ[φ], σ₁(x), σ₁(y), σ₁(z) > 0, σ₂-signs not all equal, n odd positive integer.
Normalisation is unambiguous (σ₁(φ) = 1.618…, σ₂(φ) = −0.618…, N(φ) = −1). Under α(u) = (−u₁/u₃, −u₂/u₃) the
conditions pin inv_{σ₁} = ½ and inv_{σ₂} = 0 (Thm 2.1(a), re-derived in C5). The "Anchor/partner bookkeeping"
paragraph is labelled Assessment and is in fact proved later (Cor 2.2). Only remark: the definition is for n ∈ ℤ;
Thm 1.3(a) and Cor 2.2 also speak of n = m² with m ∈ O — see defect m1.

### C2. Lemma 1.1 (Cl_{4∞₁} ≅ ℤ/2, χ = χ_{−φ}) — SOUND
Re-derived. h(ℚ(√5)) = 1, so Cl_{4∞₁} = ((O/4)^* × {±1}_{σ₁}) / image(O^*). From scratch
(`scripts/review_t1t_zphi.py`, check L11): |(O/4)^*| = 12, φ has order 6 mod 4, φ³ ≡ 1 + 2φ, the image of
±φ^j has order 12, (−1, +) ∉ image; so |Cl_{4∞₁}| = 2 with non-trivial class (−1, +). Character: for a unit u in
an unramified 2-adic field, (u, w)_2 = 0 for all w ∈ U^{(2)} = 1 + 4O_2 (K_2(√w)/K_2 unramified, u a norm), so the
conductor of K(√−φ)/K divides 4·∞₁ (σ₁(−φ) < 0, σ₂(−φ) > 0, −φ a unit) and the character is non-trivial, hence
equals the unique non-trivial character of Cl_{4∞₁}. Numerically: on every degree-one prime 𝔮 met in the Prop 1.2
run (split ℓ and 𝔮 = (√5)), "𝔮 has a generator ≡ −1 (mod 4) with σ₁ > 0" (computed by explicit normalisation over
±φ^j, j < 6) ⟺ (−φ/𝔮) = −1 (computed through the residue map φ ↦ r) — all instances agree (counts in C3).
Note χ((√5)) = (−3/5)... = (2/5) = −1 (φ ≡ 3 mod √5): the ramified prime is always in the non-trivial class.

### C3. Proposition 1.2 (explicit unit Type II solutions) — SOUND-AFTER-REPAIRS (proof gap at σ₂, claim true)
Algebra re-derived: e ≡ −n (mod 4), x + η = e(g+1)/4, 4/n − 1/x = e/(nx) = 1/y + 1/z; σ₁-positivity; x prime to
n (a prime 𝔭 | (x, n) divides 4x − n = e | a_k ≡ 4η (mod n)); n | y, n | z. All correct.
**Gap (defect M1):** the σ₂ step says "sgn z = −sgn x · sgn y, so the three signs are not all equal". This is a
non-sequitur: sgn x = sgn y = −1 gives sgn z = −1, i.e. all three negative — which V_φ forbids. The claim is
nevertheless true: σ₂(x) < 0 means σ₂(e) < −n and σ₂(y) < 0 means σ₂(g) < −1, whence σ₂(a_k) = σ₂(e)σ₂(g) > n;
but σ₂(a_k) = n + 4σ₂(η) < n since σ₂(η) = σ₂(φ)^{2k+1} < 0. So (−, −) is impossible and the conclusion holds.
*C3-numerics* (`scripts/review_t1t_zphi.py 1000000 12 2000`, log `logs/review_t1t_zphi_1e6.txt`; exact ℤ[φ]
arithmetic, exact sign tests of P + Q√5, own Euclidean gcd, full factorisation of N(a_k) when no prime < 4000
qualifies). **All 78 496 odd primes p < 10⁶, p ≠ 5, are solved by Prop 1.2**; every solution verified exactly
(4xyz = n(xy+yz+zx), σ₁ > 0, σ₂ mixed, N(x) prime to p, p | y, p | z). True min|k| histogram (k = 0, 1, …, 7, 10):
57082, 19143, 1859, 313, 78, 12, 6, 2, 1 — this differs from the document's (42589, 29024, …, 8: 1 prime) because
the author's scan (`t1t_phi_scan.py`, via `solve_unit_typeII`) ignores 𝔮 = (√5), prime factors > 10⁵, and the
case where both primes above ℓ divide a_k (defect m3). σ₂-patterns (sgn x, sgn y) observed: (+,+) 49418,
(+,−) 19503, (−,+) 9575, (−,−) never (as proved above). 131 902 prime-by-prime cross-checks
"normalisable ⟺ (−φ/𝔮) = −1 ⟺ (p/ℓ) = −1" all agree. **T1 control (complete, stronger than the author's):** for
every odd m < 2000 (including 5 | m) and |k| ≤ 12, every prime factor of a_k = m² + 4φ^{2k+1} (full factorisation;
split, ramified and inert) lies in the trivial class of Cl_{4∞₁}: no square is solved by Prop 1.2. (The author's
control skips 5 | m and prime factors > 10⁵.)

### C4. Theorem 1.3 (criterion; T1 for the mechanism) — SOUND (statement in the report is broader than proved)
Re-derived. (⇒) g ≡ −1 (4), σ₁ g > 0 is in the non-trivial class, χ is multiplicative on ideals prime to 2, so a
prime factor of g (hence of a_k) has χ = −1. (⇐) a_k is odd (a_k ≡ n mod 2), so any 𝔮 | a_k is prime to 2; h = 1
and Lemma 1.1 normalise its generator to g; σ₁(e) = σ₁(a_k)/σ₁(g) > 0 as σ₁(a_k) = n + 4σ₁(η) > 0. For 𝔮 | a_k:
𝔮 ∤ n (else 𝔮 | 4η), and n ≡ −φ(2φ^k)² (mod 𝔮) gives (n/𝔮) = (−φ/𝔮) = χ(𝔮) — including the ramified
𝔮 = (√5) (−φ is a 𝔮-unit and K(√−φ)/K is unramified at 𝔮; the "scope fix" is correct). (a) and (b) follow;
inert ℓ: n ∈ F_ℓ is a square in F_{ℓ²} (and in fact inert ℓ | a_k forces ℓ ≡ 1 mod 4, since η mod ℓ ∈ F_ℓ gives
η² = N(η) = −1). All confirmed numerically (C3).
*Remark (strengthening, not a defect of correctness):* (√5) | a_k ⟺ n ≡ −4·3^{2k+1} ≡ 3·(−1)^k (mod 5). Hence for
**every odd n ≡ ±2 (mod 5)** Prop 1.2 applies with 𝔮 = (√5) and k = 0 (n ≡ 3) or k = −1 (n ≡ 2) — checked for all
such primes < 2·10⁵ and odd n < 2·10⁴. So V_φ(p) is **unconditional for p ≡ ±2 (mod 5)** by Prop 1.2 alone; GRH is
needed in Thm 3.1 only for p ≡ ±1 (mod 5). The document misses this (defect m4).
*Scope:* the document states Thm 1.3 for "the hypothesis of Prop 1.2" (correct). AGENT_REPORT SHARP-2 and the
brief paraphrase it as "unit-Type-II solutions of V_φ(n) ⟺ …". That is broader than proved: Type II solutions with
d₁ := e·y/n − x a unit of signature (+,+) (η = φ^{2k}) or with other signs are not covered (for η = φ^{2k} the
relation sgn z = sgn x · sgn y at σ₂ does not exclude mixed patterns). Either define "unit-Type-II" as the Prop 1.2
family or drop "⟺" (defect m2).

## Defects
