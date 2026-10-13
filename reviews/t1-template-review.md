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
Note χ((√5)) = (−φ mod √5 / 5) = (−3/5) = (2/5) = −1 (φ ≡ 3 mod √5): the ramified prime is always in the non-trivial class.

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

### C5. Theorem 2.1 (local invariants on integral points, any number field) — SOUND (one hypothesis to reword)
Re-derived line by line.
* Permutation invariance of α (used for every relabelling) holds identically in Br K[2], independent of the equation:
  with a = −u₁/u₃, b = −u₂/u₃ the cyclic shift is (−b/a, 1/a) = (−b, a) + (a, −1) = (b, a) = (a, b).
* (a) (a, b)_ℝ = ½ ⟺ a, b < 0 ⟺ u₁, u₂ have the sign of u₃. Correct.
* (b) Correct: the most negative of −v_i occurs twice, tame symbol (−1)^{(V−W)²}(a/b)^{V−W} = (−u₁/u₂)^{V−W}; if W < V
  then v(u₁ + u₂) > V forces u₂/u₁ ≡ −1. (This is BL Lemma 3.5's argument, generalised; correct over any K.)
* (c) **Correct, including wild ramification.** I re-derived the DRINFELD identity directly: with x = 4u₁/n − 1,
  y = −u₂/u₃ one has −x = (u₁/u₃)(1 − y)/y, so (−x, y) = (u₁/u₃, y) + (1 − y, y) + (y, y) = (−u₁/u₃, y) = α, and
  (y, −1) + (x, y) = (−x, y). x ≠ 0 since u₂ + u₃ = 0 would give u₁ = n/4 ∉ O_v. If v(u₁) ≥ 1 then
  −x = 1 − 4u₁/n ∈ U^{(2e+1)} ⊂ K_v^{*2} (e = v(2), v(n) = 0). If v(u₁) = 0 = max then all u_i are units,
  −x ∈ 1 + 4O_v, K_v(√−x)/K_v is unramified (root of t² − t − w), and the unit y is a norm: α = 0. Nothing depends
  on e or f. It is a genuinely different (shorter) proof of Bright–Loughran Lemma 3.8 (checked against
  sources/bright-loughran-1908.02526.pdf, Lemma 3.8: "n odd ⇒ inv₂ α(U_n(ℤ₂)) = 1", proved there by a case table).
  The all-units case cannot occur over ℚ₂ (residue field F₂) but does occur over ℚ₄ = ℚ(√5)₂ (residue field F₄),
  which is why the unramified-extension step is needed.
* (d) Correct: Type II forces v₂ = v₃ = V ≥ 2s and u₃/u₂ ≡ −1 if V > 2s; symbol (−u₂/u₃)^V trivial in both parity
  cases. Type I forces v₁ = 2s exactly; symbol (−u₃/u₂)^{2s}.
* All of (b)–(d) are statements about LOCAL integral points (u ∈ O_v³), as in BL; the proof uses nothing global.
**Numerical test (from scratch, `scripts/review_t1t_local.py 3 60`, log `logs/review_t1t_local.txt`).** Own
arithmetic in ℤ[t]/(f) for ℚ(√5) (2 inert), ℚ(√2) (2 = (√2)², e = 2, wild), ℚ(√3) (2 = (1+√3)², e = 2, wild), ℚ(∛2)
(2 = θ³, e = 3, wild). Tame symbols at every odd place (Hensel-lifted factors of f; ramified 3, 5 via explicit
uniformisers). **The 2-adic invariant is computed directly**, not by reciprocity: K_v^*/K_v^{*2} is computed
explicitly (|U/U²| = 2^{1+[K_v:ℚ₂]} asserted), N(K_v(√a)) generated by sampling x² − ay² and asserted to have index
exactly 2, pairing asserted symmetric; validated against the ℚ₂ formula on rational pairs (inv = [K_v:ℚ₂]·(a,b)₂) and
by full Hilbert reciprocity on 150 random pairs per field, where inv₂ ≠ 0 in 61/63/71/69 cases (so the test has
teeth). Results on 508 / 548 / 524 / 398 integral solutions of 4/n = Σ1/u_i (n ∈ {3, 7, 9, 11, 13, 15, 21, 25, 29, 45,
49, 81, 121, 169, 225}, no sign conditions imposed): inv₂ = 0 in **all** cases (ℚ(√5): 264 all-unit and 244 non-unit
cases), (a) matches the sign rule always, (b) no non-zero tame invariant at v ∤ 2n, (d) 0 on all 136/68/172/50
Type I/II-shaped places with v(n) even, reciprocity sum 0 on every solution. Control: for even n (where (c) does
not apply) inv₂ ≠ 0 on 57/120, 28/120, 36/120, 46/120 solutions.
Only issue: hypothesis "2 ∤ n" must read "n prime to 2" (defect m5).

### C6. Corollary 2.2 (T1 for sign-pattern ES) — SOUND for the stated direction; converse/"iff" overclaimed
With F = ∅: Σ_real inv = |P|/2, complex places 0, (b), (c) kill all other places outside n, so Σ_{v|n} inv_v α ≡ |P|/2
by Hilbert reciprocity; for n = m² (m prime to 2) every v | n has v(n) even and (d) gives 0 at Type I/II-shaped places,
so for |P| odd no solution is Type I/II-shaped at every prime of n. Correct. V_φ = ES_{{σ₁},{σ₂}} is T1-bearing:
PROVED. ES_{ℚ(∛2)} (r₁ = 1, r₂ = 1) is T1-bearing: PROVED (wild 2 covered by (c), checked numerically in C5).
Overclaims: (i) "If |P| is even … there is no such T1" — what is shown is only that α gives no obstruction (sum 0);
it does not show Type I/II-shaped solutions exist at squares. AGENT_REPORT SHARP-3 upgrades this to "T1-bearing
**iff** |P| odd (and no real place unpinned)", which is not proved (other obstructions are not excluded; for K ≠ ℚ
the generation of Br U_n/Br K by α is not established in the document) — defect m6. (ii) The example "totally
positive ES over a real quadratic field … a theorem for all n" misquotes BRAINSTORM/other_rings.md Prop 3.3, which
requires N(ε) = −1 and n ∈ ℤ (defect m7).

### C7. Theorem 3.1 (V_φ(p) for every odd prime p ≠ 5; CONDITIONAL on GRH via Lenstra 1977) — SOUND (CONDITIONAL); justification should be replaced by Lenstra's Cor. 4.8
*Source check.* sources/ has no copy; I obtained the scan (GDZ Göttingen, Invent. Math. 42, LOG_0012) and OCR'd it
(`/tmp/lenstra77_ocr.txt`, not committed). Lenstra §2: K global, F/K finite Galois, C ⊂ Gal(F/K) union of conjugacy
classes, W ⊂ K^* finitely generated of rank ≥ 1, k ≥ 1; M = {𝔭 : (𝔭, F/K) ⊂ C, ord_𝔭 W = 0, [k_𝔭^* : ψ(W)] | k}.
(3.1): for number fields, under GRH for the ζ-functions of L_n = K(ζ_n, W^{1/n}) for all squarefree n, d(M) exists
and equals a. **(4.8) Corollary:** if W ⊄ K^{*q} for every q > 1 and GRH holds, then M is infinite (indeed d(M) > 0
by (4.6)) iff C ⊄ ∪ Gal(F/L_l), the union over primes l with L_l ⊂ F.
*Application.* K = ℚ(√5), W = ⟨φ⟩ (not a q-th power, so (4.7) holds), k = 1, F = K(i, √p), C = {σ: σ(i) = i,
σ(√p) = −√p} (F/K biquadratic since −1, p, −p ∉ K^{*2} for p ≠ 5). L_2 = K(√φ) ⊄ F (φ ≢ −1, ±p mod K^{*2} by
signatures (+,−) vs (−,−), (±,±)); for odd l, L_l = K(ζ_l, φ^{1/l}) is non-abelian over K (φ ∉ K^{*l}), so L_l ⊄ F
(F abelian). Hence the union is empty and (4.8) gives d(M) > 0 under GRH. Degree-≥2 primes have density 0, so
infinitely many degree-one 𝔮 ∤ 10p satisfy (i)–(iii), and the proof's algebra (re-derived: (t/𝔮) =
(−1/ℓ)(p/ℓ)(φ/𝔮) = 1, squares = ⟨φ²⟩, so 𝔮 | a_k for some k ∈ [0, (ℓ−1)/2), χ(𝔮) = (p/ℓ) = −1) then gives the
solution by Thm 1.3(b)/Prop 1.2. **The positivity question raised by the author's own Assessment is settled
rigorously by (4.8)**; the author's ad-hoc entanglement discussion is unnecessary and contains a slip ("√p ∈ ℚ(ζ_p)"
is false for p ≡ 3 mod 4; it is √(−p), and with i ∈ F the conclusion survives) — defect m8. The GRH hypothesis should be
stated as GRH for ζ_{K(ζ_n, φ^{1/n})}, n squarefree (Lenstra 3.1), not only prime r.
*Formalisation of "infinitely many shots".* Correct and pointwise in p: for each fixed p one application of Lenstra
with a p-dependent F; no uniformity in p is needed or claimed. The k produced is ≤ (ℓ−1)/2 with ℓ the least prime in
M (no explicit bound on k without effective Chebotarev/Artin; the document claims none).
*Numerics* (`scripts/review_t1t_artin.py 300000 …`, log `logs/review_t1t_artin.txt`): for p ∈ {11, 19, 29, 31, 41, 59,
61, 71, 79, 89, 1009, 999959} the proportion of degree-one 𝔮 (N𝔮 < 3·10⁵) satisfying (i)–(iii) is 0.088–0.093
(≈ ¼ × an Artin-type constant), and for the first 300 such 𝔮 per p the k with 𝔮 | a_k was found explicitly.
*Strengthening (see C4):* for p ≡ ±2 (mod 5) the theorem is unconditional (𝔮 = (√5), k ∈ {0, −1}); GRH is needed only
for p ≡ ±1 (mod 5).

### C8. §4: ES over ℤ[∛2] (EVIDENCE) — SOUND (evidence reproduced); unconditional-route plan — GAP (hidden Galois hypothesis)
*Prop 1.2 transfer.* Correct verbatim with η = ε^k, ε = θ − 1 (N ε = 1, ε ≈ 0.26 > 0): only positivity at the one real
place is needed, and σ(x), σ(y), σ(z) > 0 follow as in C3; no mute-place argument is needed. T1 for ES_{ℚ(∛2)}:
PROVED by Cor 2.2 (2 = θ³ wildly ramified is covered by Thm 2.1(c); tested in C5).
*From-scratch reproduction* (`scripts/review_t1t_cbrt2.py 3000 8 200`, log `logs/review_t1t_cbrt2.txt`; own ℤ[θ]
arithmetic, Euclidean gcd with norm-decrease asserted, complete factorisation of (a_k), exact subset search in the ray
class group). |Cl_{4∞}| = 4 and it is **(ℤ/2)²** (|(O/4)^*| = 32, image of ±ε^j of order 16); the class of (−1, +)
has order 2, so the criterion is indeed "some sub-product of prime factors of a_k lies in (−1,+)" (single primes do
not suffice). The document's example (p = 13, k = 2) verifies exactly. All 429 odd primes p < 3000 are solved
(true min|k| = 0, 1, 2, 3, 4, 7 for 361, 48, 16, 2, 1, 1 primes; the author's 332/70/23/… come from a restricted search,
cf. m3). No odd square m², m < 200, is solved by the mechanism for |k| ≤ 8 (complete factorisation).
*Minor:* "Cl_{4∞}(K) (a 2-group …)" is true for ℚ(∛2) but not for r₁ = 1 fields in general ((O/4)^* has odd part
∏_{𝔭|2}(N𝔭 − 1) when some 𝔭 | 2 has residue degree > 1) — defect m9.
*Unconditional plan (labelled "Assessment / plan, not done" — label is correct).* Harper–Murty, Canad. J. Math. 56
(2004), Theorem 1, assumes **K/ℚ Galois** with unit rank ≥ 4 (confirmed from the abstract: "Let K be a finite Galois
extension of ℚ with unit rank greater than 3"). A Galois field has r₁ ∈ {0, [K:ℚ]}, so the proposed instance
"r₁ = 1, r₂ = 4, degree 9" (and every r₁ = 1 field other than ℚ) is outside the cited result. The plan can only use
totally real Galois fields with |P| odd and mute places M — which needs units of signature (+ at P, − at every
v ∈ M) and a per-place version of the (−,−) exclusion of C3 — or a non-Galois extension of the Gupta–Murty sieve,
which is not available off the shelf. Also "(p/ℓ) = −1 via Bombieri–Vinogradov for fixed p" is unexamined. The
promise "4/5 as a theorem" in bsJ is not supported (defect M2).

### C9. Barrier screen and Assessments of §3 — acceptable as Assessment
B5/T1: correct (Thm 1.3(a), Cor 2.2). B2: the claim "hypothesis violated for unit divisors" is accurate in the
stated sense — the class condition lives in the fixed group Cl_{4∞₁} because d₁ = η is a unit, whereas over ℤ the
analogous modulus 4c is part of the solution; this is an Assessment, not a theorem, and should be labelled so
(the screen carries no label). B3/B6: correct (infinite search at fixed p, pointwise Chebotarev/Artin input).
"No transfer to ℤ" is labelled Assessment — fair. Dictionary (K = ℚ, η = 1): correct (p + 4 has a prime factor
q ≡ 3 mod 4 ⟺ (p/q) = −1 for some q | p + 4, since p ≡ −4 mod q). §0 (J2, V_{3,4} over ℚ) was not re-checked
(EVIDENCE, no headline claim).

### C10. Labels
§1–§2 PROVED labels: justified (after M1 repair for Prop 1.2). Thm 3.1 CONDITIONAL: justified (and partly
unconditional, m4). §1 / §3 / §4 EVIDENCE: reproduced from scratch with stronger (complete) controls. AGENT_REPORT
SHARP-2 "⟺ unit-Type-II solutions" and SHARP-3 "iff |P| odd": overstated (m2, m6). bsJ "Promise as a theorem 4/5":
not supported (M2).

## Defects
