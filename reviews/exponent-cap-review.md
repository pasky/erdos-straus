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
| Thm 2.1 (g ≤ 2nQ₁²(n + Q₁²), sharp in Q₁⁴) | SOUND (sharpness family needs m4) |
| Cor 2.2 / "archimedean wall" consequences | SOUND as stated; SCOPE OVERCLAIMED elsewhere (M1) |
| Prop 3.1 (box size; KEY OBSERVATION buys a divisor factor) | SOUND (covering-only scope, m5) |
| Thm 3.2 (ES^{(y)} with cap y^δ) | SOUND (relative to Lemma 2.2 sieve; ineffective) |
| Dictionary 3.3 (a), (b) | SOUND; citation verified (form n/2 is Banaszczyk's) |
| Dictionary 3.3 (c) + "beyond GRH" | Assessment, fair but overstated wording (m6) |
| Prop 4.1 | SOUND-AFTER-REPAIRS (m7: "> " should be "="; citations verified) |
| §5.1 EVIDENCE (S = {3}) | SOUND — reproduced exactly to 10⁶ |
| §5.2 EVIDENCE (k = 2 coverage) | SOUND (truncated statistic, m8) |
| Labels / Verdict (Assessment) | FAIR AFTER REPAIRS — M1 (scope of the "wall"), m5, m6 |

**Bottom line.** No FATAL defect. Every PROVED item re-derives; all identities, bounds and the §5.1 histogram
reproduce exactly with from-scratch code. One MAJOR defect (M1): the "archimedean wall" is proved only for
bounded *overflow* Q₁ (fixed S and bounded e), but the summary language ("every bounded cap is a finite search",
"no sieve can push the cap to any bounded e") drops that qualifier; with S allowed to grow with r the wall
demands only rad(Q₁)^e ≥ (r/4n)^{1/4}, which a sieve at level r^{1/4} could meet. The real obstruction to
bounded e with growing S is Prop 3.1, and it only rules out *covering* arguments.

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

### Thm 2.1 — SOUND
Re-derived both cases (notation of Prop 1.3, j ≥ 4).
*Case kj < 2Q₁²:* then k < Q₁²/2 and, by (b) with D ≥ 1, g ≤ 4k²n + Q₁² < Q₁⁴n + Q₁² ✓.
*Case kj ≥ 2Q₁²:* D ≥ kj/2; (a) gives Q₀ = (4kn + j)/(4D) ≤ 2n/j + 1/(2k) ≤ (n+1)/2 ✓; (b) gives
g ≤ (4k²n + kj/2)/(kj/2) = 8kn/j + 1 ≤ 2kn + 1 ✓; g = 4Q₀k − 1 ≤ n + 4Q₀²Q₁² (g divides a positive number) gives
k ≤ (n+1)/(4Q₀) + Q₀Q₁² ≤ (n+1)/4 + (n+1)Q₁²/2 ✓, so g ≤ n(n+1)(Q₁² + ½) + 1 ✓.
Final inequality: 2n²Q₁² + 2nQ₁⁴ − n(n+1)(Q₁² + ½) − 1 is increasing in Q₁² and equals n²/2 + n/2 − 1 at Q₁ = 1 ✓.
"In particular": g ≤ 4n·max(nQ₁², Q₁⁴) ✓. No hidden parameter dependence: all constants absolute.
*Numerics (`review_xc_algebra.py`, 203 360 shots incl. even Q):* both case bounds hold separately (case split
counts 42 008 / 49 819 on the n, Q ≤ 301 range), Q₀ ≤ (n+1)/2 in case 2, and max g/(nQ₁²(n + Q₁²)) = 0.5833 at
(n, Q, g) = (3, 1, 7), as the author reports.
*Sharpness family:* D = 3, j = 4, k = (Q₁² + 3)/4: D ≡ −Q₁² (mod 4k) ✓, Q₀ = (kn + 1)/3, g = (4k²n + Q₁²)/3 ✓
(I checked g | n + 4Q², gcd(Q, (g+1)/4) = Q₀ for all Q₁ ≤ 61, n < 200), g/(nQ₁⁴) → 1/12 ✓. The worked example
(n, Q, g) = (17, 200, 1119) is correct: x = 40, y = 4760, z = 119/25, ES^{(y,1)} but not ES (direct Def 1.1 test). Note
Q = 200 is even — fine for a shot datum, but outside Prop 1.2's "Q odd" (harmless: den z = Q₁² holds for even Q too,
see above).
* (m4) The family's congruence is stated as "n ≡ −1/k (mod 3)"; since 3 ∤ Q₁ forces Q₁² ≡ 1, k ≡ 1 (mod 3), so this
  is simply **n ≡ 2 (mod 3)**; sharpness is thus exhibited only for n ≡ 2 (mod 3) (fine for "the exponent 4 cannot
  be lowered" as a uniform statement, but say so). Also the family must require **gcd(Q₁, n) = 1** to be a shot
  datum: e.g. Q₁ = 5, n = 5, 35, 65 satisfy the stated conditions but gcd(Q, n) > 1 (59 such (Q₁, n) pairs in my
  range). Repair: "Q₁ odd, 3 ∤ Q₁, n ≡ 2 (mod 3), gcd(n, Q₁) = 1".

### Cor 2.2 and the "archimedean wall" — SOUND as stated, but its SCOPE is overclaimed (M1)
Cor 2.2's displayed inequalities are immediate from Thm 2.1 ✓; for r ≥ 4n³ the min is the Q₁⁴ branch
(√r/(2n) ≥ (r/4n)^{1/4} ⇔ r ≥ 4n³ ✓), so log Q₁ ≥ ¼ log(r/4n) and with Q₁ ≤ rad(Q₁)^e, e·log rad(Q₁) ≥ ¼ log(r/4n) ✓.
**But finiteness needs Q₁ bounded, i.e. fixed S (bounded rad Q₁) *and* bounded e.** ES^{(y,e)} as defined in
Def 1.1 restricts only the *exponents* of den z, not its radical, and the second clause of Cor 2.2 ("the same
bound holds for every S … with P := rad(Q₁) ≤ g") gives no finiteness at all (P ≤ g is circular). See M1 below:
several summary statements drop the "fixed S" qualifier.

### Prop 3.1 — SOUND (scope: covering arguments only)
(a) trivial ✓. (b) κ + e + 1 ≤ κ(e + 2) ⇔ (κ − 1)(e + 1) ≥ 0 ✓; ∏κ_i ≤ ∏(κ_i + 1) = τ(∏ s_i^{κ_i}) ≤ τ((r+1)/4)
since ∏ s_i^{κ_i} ∥ (r+1)/4 ✓; k ≤ ω((r+1)/4) ✓; the r-power form uses ω(N) ≤ (1 + o(1)) log N/log log N and
τ(N) = N^{o(1)}, with o(1) depending on r only (uniform in e) ✓. (c) ✓: (r−1)/2 ≤ |B_r(e)| forces
log(e + 2) ≥ (1 − o(1)) log log r; for fixed k, κ_i ≤ log₃ r gives (log₃ r + e + 1)^k ≥ (r−1)/2, so
e ≥ ((r−1)/2)^{1/k} − log₃ r − 1 ≥ r^{1/k}/2 for large r ✓.
*Numerics (`review_xc_lattice.py`):* for S = {3, 5} and all 1 127 primes r ≡ −1 (mod 60), r < 2·10⁵, |B_r(e)|
(computed from discrete logs) ≤ ∏(κ_i + e + 1) ≤ ∏κ_i·(e+2)² for e ≤ 3 ✓.
* (m5) Prop 3.1 bounds the *box*; it obstructs only arguments that cover all of (F_r^*)². A proof of ES^{(y,e)}
  needs only −n/4 ∈ B_r(e) for one r, which is not excluded by counting (the §5.1 data are exactly that). The text
  says this implicitly ("Coverage is…"), but Verdict item 3 / report "(a)+(b) of the brief are incompatible at
  e = 0 by the divisor bound, independently of the level of distribution" should read "incompatible *for a
  covering argument*". Also the "sieve window" display (log den z ≈ 2e log P ≳ (log r)^{2−o(1)} [coverage]) is
  heuristic: den z = Q₁² ≤ P^{2e} is an *upper* bound on the den of the solution actually found, coverage says
  nothing about the den of the hit; label it (Assessment).

### Thm 3.2 — SOUND (PROVED relative to UNIT_ORBIT Lemma 2.2; ineffective)
Re-derived step by step.
1. Sieve (FROBENIUS_FIRING Thm 4.2 with k ≥ 4 primes, M = 4 rad(n)P): ≫_M x/log²x primes, Lemma 2.3 removes
   ≪ x^{(3/4+ε)(1+1/k)} = o(x/log²x) with small Γ_r ✓ (k ≥ 4 only helps).
2. Exceptional count: λ₁^{∞}(Λ_r) ≤ B ⇒ r | N_c = ∏_{c_i>0} s_i^{2c_i} − ∏_{c_i<0} s_i^{−2c_i}, c ≠ 0, |c_i| ≤ B; N_c ≠ 0;
   ω(N_c) ≤ 2B log P/log 2; (2B+1)^k vectors ⇒ ≪_S B^{k+1} = x^{1−(k+1)η} = o(x/log²x) ✓. Constants depend on S only.
3. Minkowski II for K = [−1,1]^k: λ₁⋯λ_k·vol K ≤ 2^k det Λ, vol K = 2^k ⇒ ∏λ_i ≤ det Λ_r = [ℤ^k : Λ_r] = |Γ_r²| =
   (r−1)/2 ✓. λ_i ≥ λ₁ > B ⇒ λ_k ≤ x/B^{k−1} = x^{2/(k+1)+(k−1)η} ✓.
4. Representatives: any a ∈ ℤ^k, a = Σα_i v_i; a − Σ⌊α_i⌋v_i ∈ a + Λ_r has sup-norm ≤ Σλ_i ✓ (sublattice ⟨v_i⟩ may
   have finite index in Λ_r — harmless). Shifting by (L, …, L) gives exponents in [0, 2L] with Q² ≡ −n/4 ✓
   (−n/4 ∈ (F_r^*)² = Γ_r² by the choice (n/r) = −1, r ≡ 3 (4)).
5. Exponent: 2L ≤ 2k·x^{2/(k+1)+(k−1)η} ≤ 2k·r^{(2/(k+1)+(k−1)η)/(1−ε)}; k ≥ 2/δ + 1 gives 2/(k+1) ≤ δ/(1+δ) < δ, so
   small ε, η and large x give 2L ≤ r^δ ✓. (k > 2/δ − 1 would already suffice; the stated k is safe.)
6. ES^{(y)}: s_i | (r+1)/4 by r ≡ −1 (s_i) ✓, y = n(r+1)/4 > r ⇒ cap y^δ ✓. n ≡ 3 (4) is covered by Q = 1 ✓.
*Numerics (`review_xc_lattice.py`, k = 2, S = {3, 5}, exhaustive ℓ^∞ minima):* on the 262 primes r < 4·10⁴ with
⟨9, 25⟩ = (F_r^*)², λ₁λ₂ ≤ (r−1)/2 (max ratio 1.000 — Minkowski is tight here) and least box side L ≤ 2(λ₁ + λ₂)
(in fact max L/(λ₁+λ₂) = 0.987, so the bound used in step 4 is within a factor ≈ 2 of the truth) ✓.
Remark (1) is fair *for covering arguments with fixed S* (lower bound r^{1/k}/2 from Prop 3.1(c) vs proved
r^{2/(k+1)+ε}); Remark (2) is correctly labelled Assessment. No defect.

### Dictionary 3.3 — (a), (b) SOUND; (c) Assessment, wording overstated (m6)
(a) sufficient condition: for any centre c, the coset meets c + [−Σλ_i, Σλ_i]^k (as in Thm 3.2 step 4), and
[0, E]^k ⊆ box with E = min κ_i + e, so kλ_k ≤ E/2 suffices ✓; necessary condition = Prop 3.1(a) ✓.
(b) Λ_r is the kernel of ℤ^k → Γ_r², a ↦ ∏ s_i^{2a_i}; characters of ℤ^k/Λ_r ≅ Γ_r² are a ↦ e(θ·a) with θ ∈ Λ_r^*,
θ ≡ (φ(s_i²))_i mod ℤ^k ✓ (when Γ_r² = (F_r^*)², else characters of Γ_r²). Transference: Banaszczyk, Math. Ann. 296
(1993) 625–635, gives μ(L)·λ₁(L^*) ≤ n/2 in ℓ² (verified: this is Banaszczyk's stated form; Aggarwal–Regev-type
improvements, arXiv:1907.09020, sharpen the constant to (0.1275 + o(1))n, so n/2 is a valid, weaker form). The
logic: coverage fails ⇒ μ₂ > E/2 ⇒ λ₁(Λ^*) < k/E ⇒ a nonzero dual θ with all |θ_i| < k/E; if k/E ≤ 1 this θ ∉ ℤ^k,
so its character is nontrivial; if k/E > 1/2 the stated criterion is vacuous. ✓ (The author should add the
one-line "θ ∉ ℤ^k since |θ_i| < k/E ≤ 1" — otherwise "nontrivial" is unjustified; minor, folded into m6.)
(c) and the Assessment: the Bach bound (GRH: (ℤ/r)^* generated by primes < 2 log² r) and the log⁴ r threshold for
nontrivial GRH prime character sums are quoted correctly in substance. But "a range where **even GRH gives
nothing**" (§3.3 Assessment, Verdict 5, report SHARP 3 "beyond GRH") is stronger than what is shown: the
requirement is non-concentration for *some* sieved r, not for all r, and averaged (large-sieve type) statements
over r are not addressed (the author's own spark list mentions this). Repair (m6): "where no pointwise
character-sum input, even under GRH, is known to suffice; averaged inputs over r not examined (Assessment)".

### Prop 4.1 — SOUND-AFTER-REPAIRS (m7)
q_e = 4Q^{(e)} ≥ 4Q/rad(Q)^e ✓ (max(1, c−e) ≥ c − e). But "4Q/rad(Q)^e **>** 2√(N − n)/rad(Q)^e" is false as
written: N − n = 4Q², so 2√(N − n) = 4Q exactly — it is an equality. Harmless (the next step only needs
q_e ≥ N^{1/4+α}, which follows with C_n = √(n + 4)/4, since √N ≤ √(n + 4)·Q); repair: "= 2√(N−n)/rad(Q)^e" and
state C_n explicitly. Citations verified against abstracts/first pages: Coppersmith–Howgrave-Graham–Nagaraj,
*Divisors in residue classes, constructively*, Math. Comp. 77 (2008) 531–545: for s > N^α, α > 1/4,
gcd(r, s) = 1, #{d | N : d ≡ r (s)} = O((α − 1/4)^{−3/2}) ✓ (so with s ≥ N^{1/4+α} the count is O(α^{−3/2}) ✓);
Lenstra, *Divisors in residue classes*, Math. Comp. 42 (1984) 331–340: s > N^{1/3} ⇒ at most 11 divisors ✓.
gcd(−1, q_e) = 1 ✓. The "citation form not re-checked" caveat can be dropped. The *Reading* is Assessment and
fair; the title "below overflow N^{1/4}" is slightly off — the hypothesis is on rad(Q)^e (the *allowed* overflow),
not on the overflow of a given solution.

### §5.1 EVIDENCE — SOUND, reproduced exactly
`review_xc_leaste.py 1000000 24` (own divisor enumeration, own admissibility/overflow logic, GNU `factor` for
factorisation, every best solution re-verified with exact rationals and den z = 3^{2e}): all 78 496 primes
5 ≤ p < 10⁶ solved with j ≤ 24; least-e histogram 0: 73 910 (68 655 with j = 0), 1: 1 539, 2: 1 118, 3: 708,
4: 365, 5: 263, 6: 210, 7: 118, 8: 91, 9: 76, 10: 33, 11: 29, 12: 15, 13: 11, 14: 4, 15: 3, 16: 2, 19: 1 —
**identical** to §5.1; per-prime (least e, least e over prime g) agree with `data/xc/leaste_s3_primes.txt.gz` on
all 78 496 rows (max prime-g e = 19 ✓). The 2·10⁵ run (17 982 primes) also agrees row by row.
Completeness: I re-derived Q₀ < Q₁²(n+1)/2 from both cases of Thm 2.1's proof (case 1: Q₀ ≤ kn + j/4 with
k < Q₁²/2, j < 2Q₁²/k; case 2: Q₀ ≤ (n+1)/2), slightly sharper than the author's Q₁²n/2 + Q₁²/2 + 1; so "least e ≤ 4
exact for every p < 10⁶" ✓ (3^{20} > 9⁴·(10⁶+1)/2).
T1 control: 332 odd squares m² < 10⁶, 3 ∤ m, j ≤ 30: zero divisors ≡ 3 (mod 4) of m² + 4·9^j ✓ (trivially, as in §1).
Not re-checked: the per-residue-class tail ratios (0.149, …) and the "≈ 0.4 hits per unit of cap" gloss — the
latter is an interpretation (Assessment), not a measured quantity, and should be labelled so.

### §5.2 EVIDENCE — SOUND (m8)
`review_xc_lattice.py 200000 cap`: 1 127 primes r ≡ −1 (60) below 2·10⁵, 1 122 with ⟨9, 25⟩ = (F_r^*)², 20 with
L > 4√r + 10, the rest L/√r ∈ [0.647, 3.986], median 0.955 — matches the author up to r = 59, which `xc_cover.py`
skips (primerange starts at 60; off-by-one in all three counts, harmless). (m8) The reported min/median/max are of
a *truncated* sample (the 20 exceptional r are dropped); uncapped, r < 4·10⁴ already has L/√r = 4.96. Say
"among the 1 101 with L ≤ 4√r + 10".

## Numbered defects

**M1 (MAJOR) — scope of the archimedean wall overstated.** Locations: §0 (U2) "every bounded cap is a finite
search like ES"; §2 heading "every bounded cap is a finite search"; §2 Reading "The exponent cap is not a parameter
that a sieve can push down to 0"; §6 item 2 "The interpolation parameter does not reach ES continuously: the sieve
regime ends at e ≍ log r/log P, and below it there is nothing to sieve"; §6 closing "at bounded cap the
archimedean wall makes it a finite search"; AGENT_REPORT SHARP 2 "Every bounded cap is a finite search … no sieve
can push the cap to any bounded e".
Problem: Thm 2.1 bounds g by Q₁; Q₁ ≤ P^e is bounded only when P = rad(Q₁) is bounded, i.e. for *fixed S*.
ES^{(y,e)} (Def 1.1) does not bound rad(den z), and Cor 2.2's own "every S" clause (P := rad(Q₁) ≤ g) gives no
finiteness. Concretely, for e = 1 the wall only requires a squarefree Q₁ | (r+1)/4 with Q₁ ≥ (r/4n)^{1/4} — e.g.
r ≡ −1 (mod 4P) with P ≈ r^{1/4}, a modulus inside the Bombieri–Vinogradov range. So "no sieve can reach bounded
e" is not proved; what is proved is (i) fixed S + bounded e ⇒ finite search (Cor 2.2), and (ii) no *covering*
argument works at e = (log r)^{o(1)}·… (Prop 3.1(c): needs e ≥ (log r)^{1−o(1)}). The ES^{(y,e)}-for-bounded-e,
growing-S question (hit −n/4, not cover) is left open by the document.
Repair: in all listed places say "every bounded overflow (fixed S and bounded e) is a finite search"; replace "no
sieve can push the cap to any bounded e" by "with S fixed no sieve can …; with S growing, the wall only asks
rad(Q₁)^e ≥ (r/4n)^{1/4} − O(1), and the obstruction is Prop 3.1, which excludes covering arguments only"; add the
growing-S, bounded-e, non-covering case to the open questions (Assessment).

**m1 (MINOR)** §1 Prop 1.3 Reading: for Q₁ = 1 both D and g are ≡ −1 (mod 4k); say which one plays FIXED_MODULUS_SHOTS
Lemma 1.1's h (g ↔ h with c ↔ Q₀, j ↔ k).
**m2 (MINOR)** Cor 1.4: "with overflow Q₁ … iff … Q₀ | K" — add gcd(Q₁, K/Q₀) = 1 (else the overflow is a proper divisor
of Q₁) and gcd(Q, n) = 1.
**m3 (MINOR)** Cor 1.4 reuses j for K/Q₀ (= Prop 1.3's k); rename.
**m4 (MINOR)** Thm 2.1 sharpness family: the condition n ≡ −1/k (mod 3) is just n ≡ 2 (mod 3) (k ≡ 1 forced); add
gcd(n, Q₁) = 1 (e.g. Q₁ = 5, n = 35 meets the stated conditions but is not a shot datum).
**m5 (MINOR)** Prop 3.1 / Verdict 3 / report: "(a)+(b) of the brief are incompatible at e = 0 by the divisor bound,
independently of the level of distribution" — true for *covering* arguments only; add the qualifier. Label the
"sieve window" display (§3, after Prop 3.1) as Assessment (den z ≤ P^{2e} is an upper bound for the hit, not a
consequence of coverage).
**m6 (MINOR)** Dictionary 3.3(b): add "θ ∉ ℤ^k since |θ_i| < k/E ≤ 1, so χ is nontrivial (for k/E > 1/2 the criterion is
vacuous)". 3.3(c)/Verdict 5/report SHARP 3 "even GRH gives nothing", "beyond GRH": soften to "no known pointwise
character-sum input (even under GRH) suffices; averaged-over-r inputs not examined (Assessment)". Citation of
Banaszczyk is correct; the "citation form not re-checked" caveat can be dropped.
**m7 (MINOR)** Prop 4.1: "4Q/rad(Q)^e > 2√(N − n)/rad(Q)^e" is an equality (N − n = 4Q²); state C_n = √(n+4)/4.
Citations (CHN 2008, Lenstra 1984) verified; drop the caveat. Title "below overflow N^{1/4}" → "below allowed
overflow rad(Q)^e ≤ N^{1/4−α}/C_n".
**m8 (MINOR)** §5.2: min/median/max of L/√r are over the 1 101 non-exceptional r only — say so; `xc_cover.py` skips
r = 59 (primerange starts at 4·s₁s₂ = 60), so all three counts are one short. §5.1 "≈ 0.4 per unit of cap" is
an interpretation, label (Assessment).

## Labels and Verdict — fair after M1, m5, m6
PROVED labels on Prop 1.2, 1.3, Cor 1.4, Thm 2.1, Cor 2.2, Prop 3.1, Thm 3.2 (relative to Lemma 2.2, ineffective),
Dictionary 3.3(a)(b), Prop 4.1 (relative to CHN) are all justified. EVIDENCE labels on §5 are justified and the
data reproduce exactly. The closing Verdict "Not an opening for ES (Assessment)" is fair and correctly labelled;
it should, however, rest on "fixed-S bounded caps are finite searches (Cor 2.2) + covering needs inflated boxes
(Prop 3.1)", not on a claim that *no* sieve can reach bounded e (M1). ES is not solved, and no infinite case of ES
is claimed — ✓.
