# R200 — hostile review of EXPONENT_CAP.md (O200)

Reviewer: R200 side agent. Document reviewed: EXPONENT_CAP.md as merged from side-agent/exponent-cap (checkpoint 1),
AGENT_REPORT_O200.md. From-scratch scripts: `scripts/review_xc_algebra.py`, `scripts/review_xc_leaste.py`
(none reuses `scripts/xc_*`).

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Prop 1.2 (ES^{(y,e)} ⇔ g ≡ −1 mod 4Q^{(e)}) | SOUND |
| Prop 1.3 (duality D·g = 4k²n + Q₁², both directions) | SOUND |
| Cor 1.4 (overflow = inflated box) | SOUND-AFTER-REPAIRS (m2, m3) |
| T1 in (Q₁, k) coordinates | SOUND |

## Claim-by-claim

### Prop 1.2 — SOUND
Re-derived: for ℓ | Q odd, c = v_ℓ(Q), σ = v_ℓ(g+1), 4gx = n(g+1) + 4Q² gives v_ℓ(x) = σ when σ < 2c, so
v_ℓ(z) = v_ℓ(x) + σ − 2c = 2σ − 2c; for σ ≥ 2c, v_ℓ(x) ≥ 2c and v_ℓ(z) ≥ 0. Hence the ℓ-part of den z is
ℓ^{2·max(0, c−σ)} = ℓ^{2 v_ℓ(Q₁)}, since v_ℓ(Q₀) = min(c, v_ℓ((g+1)/4)) = min(c, σ) for ℓ odd. The ES^{(y,e)}
conditions (ℓ | y ⇔ ℓ | (g+1)/4 for ℓ ∤ n; c − σ ≤ e) combine to σ ≥ max(1, c − e) for each ℓ | Q (primes with
σ ≥ c ≥ 1 satisfy this automatically; primes with σ = 0 lie in Q₁ and violate (i)). ✓.
*Numerics (`review_xc_algebra.py`):* every shot datum with odd n ≤ 301, 1 ≤ Q ≤ 301 (odd AND even Q, 91 827 shots)
and with n ≤ 61, Q ≤ 1501 (111 533 shots): den(z) = Q₁² in all cases (so the "Q odd" restriction of the den
statement is unnecessary; it is needed only because Def 1.1 excludes ℓ = 2), and for odd Q the predicate
"g ≡ −1 mod 4Q^{(e)}" agrees with a *direct* test of Def 1.1 (exact rationals, factorisation of den z) for
e = 0, 1, 2, 3, ∞ in every case.

### Prop 1.3 — SOUND
Forward: g ≡ −1 (Q₀) and g·m = n + 4Q² ≡ n (Q₀) give m ≡ −n (Q₀) ✓. Expanding (4Q₀k − 1)(jQ₀ − n) = n + 4Q₀²Q₁²
gives Q₀[4kjQ₀ − 4kn − j − 4Q₀Q₁²] = 0 ✓ ⇒ (a); (a) ⇒ j ≡ 0 (4) ✓ (no parity assumption on Q₀ needed);
D = kj − Q₁² > 0 since the RHS of (a) is > 0 ✓; k·(a) with kj = D + Q₁² gives 4Q₀kD = 4k²n + D + Q₁² = (g+1)D ✓.
Converse: D ≡ −Q₁² (4k) ⇒ gcd(D, k) = gcd(Q₁², k) = 1 ✓, D odd ✓ (needs Q₁ odd, as stated), 4D | 4kn + j ✓,
g = 4Q₀k − 1 ✓, g(jQ₀ − n) = n + 4Q₀²Q₁² ✓ (I re-expanded), Q₀ = gcd(Q, (g+1)/4) because gcd(Q₁, k) = 1 ✓.
*Numerics:* forward identities (a), (b), 4 | j, D ≥ 1, D ≡ −Q₁² (4k) on all 91 827 + 111 533 shots above (incl.
even Q); converse on all 3 965 triples (n ≤ 81 odd, Q₁ ≤ 41 odd, k ≤ 40, gcd(Q₁, k) = 1, every admissible D):
Q₀ ∈ ℤ_{>0}, g = 4Q₀k − 1, g | n + 4Q², gcd(Q, (g+1)/4) = Q₀ — 0 failures.
The "Reading" (Q₁ = 1 ↔ the Type II line 4k²n + 1 with a divisor ≡ −1 (4k); k = 1 ↔ 4n + Q₁² with a divisor
≡ 3 (4)) is correct. Note (minor, m1): for Q₁ = 1 *both* D and g are ≡ −1 (mod 4k), so the identification with
FIXED_MODULUS_SHOTS Lemma 1.1 (d = 1) is with h ↔ g (h = 4cj − 1, c ↔ Q₀, j ↔ k), the divisor of 4k²n + 1 that
is ≡ −1 (mod 4k) being D *or* g; worth one clause.

### Cor 1.4 — SOUND-AFTER-REPAIRS
The computation is right (4Q₀k ≡ 1 (h) and h | n + 4Q² ⇔ −n ≡ Q₀Q₁²/k (h); checked on every shot above as
−n·k ≡ Q₀Q₁² (mod g)). Two imprecisions:
* (m2) "a shot datum (Q, h) **with overflow Q₁** exists iff … Q₀ | K" — Q₀ | K only gives Q₀ | gcd(Q, K); the
  overflow is exactly Q₁ iff additionally gcd(Q₁, K/Q₀) = 1 (and gcd(Q₀Q₁, n) = 1 for a shot datum). Without it
  the "if" direction produces a shot whose overflow is a proper divisor of Q₁. Repair: add "gcd(Q₁, K/Q₀) = 1,
  gcd(Q, n) = 1".
* (m3) Notation clash: Cor 1.4's j (= K/Q₀) is Prop 1.3's k, while Prop 1.3's j is a different quantity
  ((m+n)/Q₀). Rename to avoid a reader plugging Prop 1.3's j into c·j = K·Q₁².
The "Reading" after Cor 1.4 (covering needs e ≥ (log h)^{1−o(1)}) is a covering heuristic; it should carry an
(Assessment) tag or point explicitly to Prop 3.1(c), which is about *covering*, not about hitting −n/4.

### T1 in (Q₁, k) coordinates — SOUND
At n = m²: gcd(Q₁, k) = 1 (from Q₀ = gcd(Q, Q₀k)) and gcd(Q₁, m) = 1, so (2km)² + Q₁² is a sum of coprime squares
(Q₁ odd), all divisors ≡ 1 (4), contradicting D ≡ −Q₁² ≡ 3 (4) ✓. (For Q₁ even the shot cannot be ES^{(y,e)}
anyway; and in fact n + 4Q² = m² + (2Q)² with gcd(m, 2Q) = 1 already has no divisor ≡ 3 (4), so there is no shot
datum at all at a square — the (Q₁, k) reading is a restatement, not new information.)
