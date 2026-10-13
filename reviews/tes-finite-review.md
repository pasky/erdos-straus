# R194 — hostile review of TES_FINITE.md (O194)

**Repairs applied** (author quiet, no commits on side-agent/tes-finite after e126ef48): D1–D7 applied directly to
TES_FINITE.md and D2/D3 to reviews/agent-reports/AGENT_REPORT_O194.md, each marked "(R194 repair, Dk)". D8 is a ledger
item for the parent (DISCOVERIES).

Reviewer: side agent R194 (branch side-agent/review-tes-finite; author branch side-agent/tes-finite merged).
From-scratch scripts: `scripts/review_tf_*.py` (own ℤ[ω] arithmetic, own solvers, own Hilbert / cubic symbols;
no import of `tf_*`, `tw_*`). Source checked: Bright–Loughran arXiv 1908.02526 (sources/bright-loughran-1908.02526.pdf,
read in full for §2–§3).

## Summary verdicts
| Claim | Verdict |
|---|---|
| Prop 1.1 / Cor 1.2 (finiteness, explicit bound, "infinite iff vanishing two-term subsum") | SOUND (D1: over ℤ = BL Lemma 3.10) |
| Thm 2.1 (TES fails at exactly the 16 primes, N ≤ 30000) | SOUND — fully reproduced by an independent solver (D7 minor) |
| Thm 3.1 (no BM obstruction from Br U ≅ Br K ⊕ ℤ/6 at the 16 failures) | SOUND — BL inputs valid over ℚ(ω); all 16 certificates re-verified (D5 wording) |
| §4 cubes / characters | characters re-verified; cubes not re-run |
| Prop 5.1 (order-2 T1 for 8/n at odd squares) | SOUND (2-adic step re-derived; BL Lemmas 3.2/3.4/3.5/3.9 transfer checked) (D6) |
| Thm 5.2 (8/n insoluble at 131, 241; list ≤ 299; primes ≤ 2·10⁵) | SOUND computation, but KNOWN: PW Table 1 (D2, MAJOR) |
| Thm 5.3 (no BM obstruction at 3, 11, 17, 131, 241) | SOUND (certificates re-verified; 3, 11, 17 supplied by reviewer); = BL Rem 1.10 (D4) |
| Cor 5.4 / B7 | logic SOUND; novelty/significance overclaimed — SOUND-AFTER-REPAIRS (D3, MAJOR) |

No FATAL defects. Two MAJOR (D2, D3: literature/attribution for §5, affecting SHARP #1 and #3), six MINOR. The TES
half (§1–§3) is new, correct, and fully reproduced.

## 1. Prop 1.1 / Cor 1.2 (finiteness) — SOUND (minor attribution / wording defects)

Re-derived. (a) |t/n| ≤ Σ|c_i|/|x_i| ≤ 3 max_i |c_i|/|x_i| ⇒ some |x_i| ≤ 3|c_i||n|/|t|, i.e. N(x_i) ≤ 9N(c_i)N(n)/N(t).
For TES (t = 9, N(c) = (1, 1, 4)): N(x) ≤ N(n)/9, N(y) ≤ N(n)/9, N(z) ≤ 4N(n)/9. ✓
(b) r = t/n − c_i/x_i = (t x_i − c_i n)/(n x_i) = A/B; c_j/x_j + c_k/x_k = A/B ⇔ A x_j x_k − B c_k x_j − B c_j x_k = 0;
multiplying by A: (A x_j − B c_j)(A x_k − B c_k) = A²x_jx_k − AB(c_k x_j + c_j x_k) + B²c_jc_k = B²c_jc_k. ✓ Both factors
are non-zero (product ≠ 0), each divisor d determines x_j = (d + Bc_j)/A, x_k = (B²c_jc_k/d + Bc_k)/A. ✓
Two-term triangle bound: min(|x_j|/|c_j|, |x_k|/|c_k|) ≤ 2/|r|, i.e. N(x_j) ≤ 4N(c_j)N(B)/N(A) for the smaller one ✓
(this is what method B uses). r = 0 ⇔ x_i = c_i n/t; for TES, c_i n/9 ∈ O would need λ⁴ | c_i n, impossible as
gcd(n, 6) = 1 and c_i ∈ {ω, ω², 2}. ✓ Remark (3): if c_i n/t ∈ O then (c_i n/t, c_j m, −c_k m) is a solution for every
m ∈ O∖0 ✓, and the proof shows all but finitely many solutions then have a vanishing two-term subsum ✓.
No quantifier issue: the bound in (a) is uniform in the solution; the finite union over i covers every solution.
Count bound "Σ_i Σ_{x_i} 6·τ_O(...)" ✓ (6 units per ideal divisor).

Defects: see D1 (attribution: over ℤ this is BL Lemma 3.10 verbatim, incl. the "u_i = −u_j" exception).

## 2. Thm 2.1 (16 TES failures, N ≤ 30000) — SOUND (N ≤ 3000 and N = 26893 independently reproduced; full range: see below)

Completeness logic re-derived. (i) Every solution has some coordinate in the Prop 1.1(a) disk; it is 2-primary,
so enumerating only 2-primary x_i in the three disks is complete. (ii) Given x_i, (x_j, x_k) ↔ divisors d of
M = (n x_i)² c_j c_k, all 6 unit multiples of every ideal divisor; the 2-primary and integrality conditions are then
tested. (iii) Reduction to one 2-primary π per conjugate pair: Lemma 3.1 of TWISTED_T1 forces n ≡ 1 (mod 2), so
only ±π matter; x_i ↦ −x_i maps TES(π) to TES(−π) (−1 ≡ 1 mod 2) and (x, y, z) ↦ (ȳ, x̄, z̄) maps TES(π) to
TES(π̄) (ω̄ = ω²). ✓ Both symmetries also confirmed by brute force (all split π, N ≤ 400:
`review_tf_zomega.py conjcheck 400`).

From-scratch solver `scripts/review_tf_zomega.py` (own a + bω arithmetic, own Eisenstein factorisation via
norms, own divisor enumeration — same mathematics as the author's method A, independent code; every solution is
checked in the cleared equation 9xyz = n(ωyz + ω²xz + 2xy)):
* `census 3000` (21 s): zeros exactly at N ∈ {7, 13, 19, 61, 79, 97, 103, 151, 193, 211, 367, 409, 769, 2029, 2239};
  N ≤ 1000: 85 primes, 507 solutions, mean 5.96, 13 zeros; (1000, 3000]: 130 primes, 1244 solutions, mean 9.57,
  2 zeros — identical to the author's numbers. All 1751 solutions have π dividing exactly 1 (1301) or 2 (450)
  coordinates (Type I / II shapes) ✓.
* `one 179 36` (N = 26893, 3 s): 0 solutions ✓. `one 11 2` (N = 103): 0 ✓. Disk count for N = 103, z-disk N ≤ 45.8:
  162 non-zero lattice points, 42 of them 2-primary ✓.
* **Full range `census 30000`** (39 min, one core, `logs/review_tf_census30000.txt`): 1630 primes (one per conjugate
  pair; split N ≤ 30000 and inert p ≤ 173); zeros **exactly** the 16 listed; solutions by shape 21042 (π divides one
  coordinate) / 7038 (two) — identical to the author's; band (3000, 30000]: 1415 primes, 26329 solutions, 1 zero
  (26893), consistent with the author's 14.40·408 + 20.31·1007 ≈ 26327. **Thm 2.1 independently reproduced in full.**

## 3. Thm 3.1 (no BM obstruction from Br U at the 16 failures) — SOUND (all 16 certificates re-verified)

BL inputs over k = ℚ(ω), checked against the paper. BL §2 is explicitly "over a field k of characteristic 0", n ∈ k^*.
(i) The K-linear change u_i = x_i/c_i turns TES into 9/n = Σ 1/u_i, i.e. BL's U_{n'} after u_i = (9/4)u'_i, n' = 16n/81 ✓
(ratios, hence α_ζ, are scaling-invariant). (ii) Prop 2.5/2.6: Br Ũ/Br k ≅ (ℚ/ℤ(−1))^{G_k} ≅ μ(k), representatives
α_ζ = (−u₁/u₃, −u₂/u₃)_ζ, ζ ∈ μ(k); for k = ℚ(ω), μ(k) = μ₆ ✓. α_ω ≠ 0 has order 3, α_{−1} ≠ 0 order 2, so they generate
ℤ/6 ✓ (the bijection ζ ↦ α_ζ is not claimed to be a homomorphism, and isn't needed). Lemma 2.4 (Br₁Ũ = Br k) uses only
Pic Ũ_k̄ = ℤ·L₁₂ with trivial action ✓ over any k. (iii) Cor 2.9 (Br U → Br Ũ iso): surjectivity Thm 1.7; injectivity
from (2.8) with Pic Ũ → Pic E onto — E is the exceptional conic of the A₁ point, its tangent cone u₁u₂+u₁u₃+u₂u₃ = 0
has the k-point (1:0:0), so E ≅ ℙ¹_k and L₁₂ (defined over k) meets it with intersection 1 ✓ — valid over K. So
Br U/Br K ≅ ℤ/6 = ⟨α_ω, α_{−1}⟩ ✓, and orthogonality to Br U ⟺ Σ inv α_ω = Σ inv α_{−1} = 0 ✓ (Br K pairs to 0;
Br ℂ = 0 at the complex place).

Certificate logic ✓: Q_v = P₀ (v ≠ 𝔮), Q_𝔮 = P₁ is in W (P₀ ∈ W_v for v ∉ T(P₀) = {𝔮}; P₁ ∈ 𝒰(O_𝔮) ∩ U°), and
Σ_v inv_v β(Q) = Σ_v inv_v β(P₀) + [inv_𝔮 β(P₁) − inv_𝔮 β(P₀)] = 0. Only the TAME place 𝔮 (∤ 6n) enters, so the
wild invariants (computed by the author via reciprocity) are not needed for the certificate; and only equality of
symbol values at 𝔮 is needed, so sign/inverse conventions are irrelevant.

From-scratch check `scripts/review_tf_bm.py` (own valuations, residue fields, tame symbol, cubic and quadratic
residue symbols; u = (x/ω, y/ω², z/2)): for each certificate it recomputes z₀ from (x₀, y₀), checks both points on U,
recomputes T(P₀) by factoring the denominator of z₀ and testing x₀, y₀, z₀ ≡ 1 at (2) — T(P₀) = {𝔮} exactly — checks
P₁ 𝔮-integral, and compares the symbols. Hand-entered: N = 7, 103, 151, 211, 26893 (data from the document /
author's run); the other 11 parsed (data only) from the author's `tf_bm.py` output (`logs/review_tf_author_certs.txt`).
**All 16 pass**; in every case (inv_𝔮 α_ω, inv_𝔮 α_{−1}) = (0, 0) for both P₀ and P₁. N = 103: P₀ = (−7−14ω, 5+4ω,
(630−672ω)/(326−428ω)), T = {(49−33ω)}, N𝔮 = 5107; P₁'s only bad norm 7687 ✓ (as stated).
Symbol code is not trivially-zero: `scripts/review_tf_symcheck.py` on complete TES sets at π (N = 307, 439, 601, 1009)
gives the cubic exponent of α_ω at π constant = 2 ≠ 0 (order-3 T1 law of TWISTED_T1 Thm 3.2(a)), and the quadratic
symbol at N = 439 split 27/27 ✓ (matches the author's convention check).

Remaining caveats are correctly stated by the author (Br U° classes ramified along L_ij not considered; étale-BM /
descent not excluded). See D3 for the wording of the theorem statement.

## 4. §4 cubes — not independently re-run (low priority; EVIDENCE-level framing is fine). Statement that
TES(π³) is solvable at N(π) ∈ {7, 13, 19} although TES(π) is not is consistent with TWISTED_T1 (inheritance only π ⇒ π³).

## 5. Schinzel 8/n

### Prop 5.1 (order-2 T1 at odd squares) — SOUND
Re-derived. (a) 2-adic: for u ∈ 𝒰(ℤ₂), put a := −u₂/u₃, x := (8/n)u₁ − 1. From 1/u₂ + 1/u₃ = x/u₁ one gets
−u₁/u₃ = x·a/(1 − a), so α = (xa/(1−a), a) = (x, a) + (a, a) − (1−a, a) = (x, a) + (−1, a) = (−x, a); −x = 1 − 8u₁/n ∈ 1 + 8ℤ₂
is a square ⇒ inv₂ α ≡ 0 on all of 𝒰(ℤ₂) (u₂ + u₃ = 0 is impossible 2-adically: it forces u₁ = n/8 ∉ ℤ₂). This is the
author's DRINFELD_ES Lemma 2.1 route, ✓. (b) Odd p: BL Lemmas 3.2, 3.4, 3.5, 3.9 re-read in the PDF. They are p-local
and use "4" only through (1.2)/(2.5) as a p-adic unit; with 8/n = 4/(n/2), n/2 ∈ ℤ_p^* resp. v_p(n/2) = v_p(n), each
proof goes through verbatim (Lemma 3.5's "p cannot divide only one u_i since p ∤ 2n" ✓; Lemma 3.9 Type 1 uses
v_p(u₁) = v_p(n) via p ∤ m, ✓ as p is odd). (c) ∞: BL Lemma 3.1 (U(ℝ)₊ connected, inv = −1) is a statement about the
real surface, ✓ after rescaling. Hence ∏_{p | n} inv_p α = −1, and at n = q^{2j} no Type I/II solution. ✓
From scratch (`scripts/review_tf_schinzel.py` + `_run.py`, own Hilbert symbols incl. the 2-adic formula):
`hilb 127 137 239 251 1009 1053 105`: all 679 positive solutions (23+6+58+7+7+482+96, = author's 679) satisfy
∏_{p|n} = −1, inv₂ = +1, inv_∞ = −1, inv_p = +1 for p ∤ 2n, AND the full product over all places = +1 (symbol self-test).
`t1 8 100`: 592 solutions at n = q², 0 Type I, 0 Type II ✓; m = 16: 211, 0/0 ✓.

### Thm 5.2 (8/n insoluble at 131, 241) — SOUND as a computation; MAJOR literature defect (D2)
Bounds re-proved: x ≤ y ≤ z ⇒ 8/n ≤ 3/x and 1/x < 8/n, so n/8 < x ≤ 3n/8; given x, A = 8x − n > 0, B = nx,
(Ay − B)(Az − B) = B² with 0 < d = Ay − B ≤ B (y ≤ z), and for the brute force B/A < y ≤ 2B/A. Two from-scratch solvers
(divisor / brute force) agree on every n ∈ [2, 299]; failures exactly {2, 3, 11, 17, 131, 241} ✓; counts 8/127: 23,
8/239: 58, 4/131: 32, 4/241: 8 ✓. `primes 200000`: failing odd primes exactly {3, 11, 17, 131, 241} ✓ (a failing prime
is certified by the complete divisor search; passing primes by an exhibited, exactly checked solution).
`squares 20000`: every odd k² ≤ 20000, k ≥ 3, solvable ✓.
**But this is known:** Pomerance–Weingartner, arXiv 2511.16817 (Ramanujan J. 2026), Table 1, row m = 8:
"all exceptions n ≤ 10¹³: 1, 2, 3, 11, 17, 131, 241" — the PDF is in this repo (sources/pomerance-weingartner-2511.16817/),
and the campaign cites PW heavily (DISCOVERIES (D)31, EXCEPTIONAL_MN*). PW Thm 3.1 moreover proves that for every m ≥ 8
there are > exp(c φ(m)^{1/3}/(log m)^{2/3}) primes p with m/p insoluble. See D2.

### Thm 5.3 (no BM obstruction at 3, 11, 17, 131, 241) — SOUND
Certificates re-verified with own Hilbert symbols (`cert` mode): n = 131: P₀ = (23, 57, 171741/8) > 0, T(P₀) = {2},
P₁ = (30, 36, −23580), inv₂ = +1 for both ✓; n = 241: P₀ = (36, 185, 1605060/19), T = {19}, P₁ = (36, 180, −7230),
inv₁₉ = +1 for both ✓. The document gives certificates only for 131, 241; my own search found certificates for
3, 11, 17 too (e.g. n = 17: P₀ = (3, 8, 408/5), T = {5}, P₁ = (−60, −60, 510/257); n = 11: P₀ = (2, 6, 33/2), T = {2}).
Note (D4): this is BL Remark 1.10 ("versions of Theorems 1.5, 1.8, and 1.9 also hold in this case") — the Thm 1.8
version gives W^{Br} ≠ ∅ for every n; the certificates are an explicit confirmation, not new content.
Count table (EVIDENCE) re-computed from scratch: m = 4: 32.8/6, 62.2/11; m = 8: 13.5/0 (2 zeros), 27.4/3;
m = 12: 7.2/0 (1 zero), 15.2/0 (1 zero) — identical. (The m = 12 zeros, 193 and 1129, are in PW Table 1.)

### Cor 5.4 / B7 — logic SOUND; novelty/significance OVERCLAIMED (MAJOR, D2/D3)
Logic: Thm 5.3 (W^{Br} ≠ ∅) + Thm 5.2 (W ∩ 𝒰(ℤ) = ∅) at n = 131 refute the universally quantified principle
"for every model of BL's family, W^{Br} ≠ ∅ ⇒ positive integral point". ✓ Scope of B7's PROVED part is correctly
restricted (no claim about "p > p₀" arguments). However:
(a) Both inputs are in the literature: insolubility = PW Table 1 (m = 8, to 10¹³); W^{Br} ≠ ∅ for all n = BL Remark 1.10
(Thm 1.8 version). Cor 5.4 is therefore a two-citation consequence of known results, not a new theorem.
(b) The principle is already refuted at n = 3, where Thm 5.3 holds (own certificate above) and insolubility is a
two-line hand argument (x ≤ 3n/8 forces x = 1, then 1/y + 1/z = 5/3 forces y = 1, 1/z = 2/3). So the PROVED content of
B7 does not need 131, 241 at all; what 131/241 add is that the failures are not just "m/n close to 3" size effects —
an Assessment, not a theorem.
(c) More substantively, PW Thm 3.1 already proves, for every m ≥ 8, more than exp(c φ(m)^{1/3}/(log m)^{2/3}) failing
primes (by an Elsholtz–Tao-type sieve: primes avoiding all Type I/II classes of small modulus), i.e. *the "lottery"
mechanism the author postulates is a theorem for large m*, and together with BL Rem 1.10 gives Cor 5.4-type
statements for every m ≥ 8 with failures as large as exp(m^{1/3+o(1)}). This is the right context for B7 and for §4's
"lottery" Assessment.
(d) BL Thm 1.9 already shows (for all n) that U_n(ℚ) is not dense in U_n(𝔸)^{Br}_•: BM is known not to be the only
obstruction to strong approximation on these surfaces. Cor 5.4's increment over BL 1.9 is that the failing open set is
the *specific* W of the 8/n problem (not some smaller open); worth saying explicitly.

## 6. Other checks
* §4 cubic characters at the 16 failures re-computed (own residue symbols): N = 19: (0, 1, 2), N = 13: (1, 2, 0),
  N = 26893: (0, 0, 0) (26893 ≡ 1 mod 9, 2 and λ cubes mod π); the other 13 have χ_π(ω), χ_π(2) both ≠ 0 ✓.
* Labels: Prop 1.1/Cor 1.2 PROVED ✓; Thm 2.1 CERTIFIED ✓; Thm 3.1 "PROVED by certificate modulo BL" ✓; Thm 5.2
  CERTIFIED ✓ (but known, D2); Cor 5.4 PROVED ✓ (but known, D3); counts EVIDENCE ✓; lottery Assessment ✓.

## Numbered defects

**D1 (MINOR) — §0 (I1), Prop 1.1: missing attribution.** Over ℤ, Prop 1.1 including Remark (3) is BL Lemma 3.10
(finiteness of {u ∈ U_n(ℤ): u₁u₂u₃ ≠ 0, u_i ≠ −u_j}, proved by the same "min |u_i| ≤ 3n/4, then two-term" argument,
with the vanishing-subsum family u_i = −u_j as the only exception). "Positivity is not what makes ES(p) finite" is
therefore already in BL. *Repair:* add "(over ℤ this is BL Lemma 3.10; the new content is the extension to imaginary
quadratic O with coefficients c_i)".

**D2 (MAJOR) — §5 Thm 5.2, AGENT_REPORT "Novelty" and SHARP #1: the 8/n failures are in the literature, in a source
already in this repo.** Pomerance–Weingartner, arXiv 2511.16817 (Ramanujan J. 69 (2026) Paper 31;
`sources/pomerance-weingartner-2511.16817/`), Table 1 row m = 8: all exceptions n ≤ 10¹³ are 1, 2, 3, 11, 17, 131, 241.
PW Thm 3.1: for every m ≥ 8 more than exp(c φ(m)^{1/3}/(log m)^{2/3}) primes p have m/p not a sum of 3 unit fractions.
The report's "may be in the literature … not searched further" is not acceptable for a SHARP claim when the campaign's
own ledger cites PW ((D)31, EXCEPTIONAL_MN*). (OEIS indeed has no sequence 3, 11, 17, 131, 241 — re-checked.) *Repair:* Thm 5.2 → "(CERTIFIED; reproduces PW Table 1, m = 8, which
covers n ≤ 10¹³)"; drop "≤ 2·10⁵" as the headline range; in the counts paragraph and §4 Assessment cite PW Thm 3.1
(the "lottery" failures for m ≥ 8 are a theorem, by an Elsholtz–Tao-type sieve) and the campaign's own density-transition
results (EXCEPTIONAL_MN/MN2: transition at log n ≍ m^{1/3}).

**D3 (MAJOR) — Cor 5.4 / B7 and SHARP #1/#3: overclaimed novelty and significance.** (a) Cor 5.4 is an immediate
consequence of BL Remark 1.10 (Thm 1.8 version for m/n: W^{Br} ≠ ∅ for every n) and PW Table 1. (b) The universally
quantified principle B7 refutes is already refuted at n = 3 (8/3: x = 1 forced, then y = 1, 1/z = 2/3; W^{Br} ≠ ∅ by
the reviewer's own certificate P₀ = (1, 1, 3/2), T = {2}, P₁ = (−60, −60, 10/27)), so 131/241 are not needed for the
PROVED part; their added value (failures not explained by m/n being close to 3) is an Assessment. (c) Nobody would
posit the principle for all n: Schinzel's conjecture already carries n > n₀(m). The meaningful family statement —
"BM is the only obstruction for n ≥ n₀ with n₀ uniform in m" — is refuted by PW Thm 3.1 + BL Rem 1.10 (failures up
to exp(m^{1/3+o(1)})). (d) BL Thm 1.9 already shows that U_n(ℚ) is not dense in U_n(𝔸)^{Br}_• for every n.
*Repair:* relabel Cor 5.4 "PROVED (immediate from BL Rem 1.10 + PW Table 1; already witnessed at n = 3)"; restate B7 as
"(known) by BL Rem 1.10 + PW Thm 3.1, no 'BM is the only obstruction for n ≥ n₀' principle uniform in m holds for the
Schinzel family; for fixed m = 8 the last failure is 241 ≤ 10¹³ (PW)"; put the BL Thm 1.9 contrast in one sentence;
in SHARP #1 replace "is FALSE … already over ℚ" by a re-attributed statement. The TES half (§2–3) is unaffected and is
the genuinely new part (no literature for TES).

**D4 (MINOR) — Thm 5.3: missing citation and missing certificates.** BL Remark 1.10 states the Thm 1.8 version for
m/n; cite it. The document claims certificates for n ∈ {3, 11, 17, 131, 241} but prints only 131, 241. *Repair:* cite
BL Rem 1.10 and either print the three missing certificates (e.g. the reviewer's: n = 3 above; n = 11: P₀ = (2, 6, 33/2),
T = {2}, P₁ = (−60, −60, 330/251); n = 17: P₀ = (3, 8, 408/5), T = {5}, P₁ = (−60, −60, 510/257); all invariants equal) or
restrict the list.

**D5 (MINOR) — Thm 3.1 statement and SHARP #2 wording.** "failures of the integral Hasse principle not explained by
the Brauer–Manin obstruction" should carry the qualifier already in Scope (i): "…by the BM obstruction from
Br U = Br K + ⟨α_ω, α_{−1}⟩ (BL's group of the affine surface; Br U° and étale-BM not considered)".

**D6 (MINOR) — §5 Prop 5.1 EVIDENCE line: control ranges.** The control counts (m = 12: 124; m = 5: 351/135;
m = 6: 147/63) are for q ≤ 60, not q ≤ 100 as the sentence suggests (reviewer: q ≤ 60 reproduces them exactly;
q ≤ 100 gives m = 12: 271, 0/0; m = 5: 2374, 696/269; m = 6: 1214, 306/120). *Repair:* state "q ≤ 60" for the controls.

**D7 (MINOR) — Thm 2.1 "every solution found at a prime has Type I or Type II shape" is a theorem, not an observation.**
π | 9xyz forces π to divide some coordinate; π dividing all three gives 9 = ω/x′ + ω²/y′ + 2/z′, impossible as
|9| > 1 + 1 + 2. So the 21042/7038 split is EVIDENCE only in its proportions. *Repair:* one-line proof.

**D8 (MINOR, ledger) — DISCOVERIES line ~819 still says "the finiteness of TES is open (O194)".** Prop 1.1 settles it;
update when the ledger entry is written.
