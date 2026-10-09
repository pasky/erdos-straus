# R108 — hostile review of EXCEPTIONAL_MN3.md (task O108, branch side-agent/et-typei-loglog)

Reviewer branch: `side-agent/review-emn3`. Source checked: ET = arXiv:1107.1010v6
(`sources/elsholtz-tao-1107.1010.pdf`, pp. 25–32 read via pdftotext). From-scratch scripts:
`scripts/review_emn3_*.py` (+ `.out.txt`).

## Verdict summary (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 2.1 (coprime harmonic sums) | SOUND |
| Lemma 2.2 (PV / Kronecker PV) | SOUND |
| Prop 2.3 (ET Prop 1.4 with φ(k)/k) | SOUND-AFTER-REPAIRS (m1, presentational); see §5 for all claims |

## 1. Lemma 2.1, Lemma 2.2, Prop 2.3 — re-derivation

**Lemma 2.1.** Re-derived: n ≤ y coprime to K has all prime factors ≤ y outside K, so
`W_K(y) ≤ Π_{p≤y,p∤K}(1−1/p)^{−1}`; the swap to `φ(K)/K` costs `Π_{p|K,p>y}(1−1/p)^{−1} ≤ e^{2ω(K)/y}`
(`−log(1−x) ≤ 2x` for x ≤ 1/2). Correct.

**Lemma 2.2.** (a) `(·/q)` for non-square odd q is non-principal; the imprimitive-PV reduction is
standard. (b) For `D = −4ka < 0`, `D ≡ 0 (4)`, the Kronecker symbol χ_D is a character mod |D|,
non-principal since D is not a square, `χ_D(q) = (4/q)(−ka/q) = (−ka/q)` for odd q, 0 for even q.
Correct. (Only a fixed real character is needed, so the classical PV constant is uniform.)

**Prop 2.3 hypotheses vs ET Thm 7.1 (p. 25).** Thm 7.1 needs: non-negative integer coefficients
`≤ N^l`, and `ρ(p^j) ≤ C` for all prime powers; conclusion `Σ_{n≤N} τ(P(n)) ≪_{D,l,C} N Σ_{m≤N} ρ(m)/m`.
No irreducibility. (a): `P(a) = kb²a+1`, coefficients `≤ kB² ≤ A^l`, ρ(p^j) ∈ {0,1}, and
`Σ_{m≤A} ρ(m)/m = W_{kb}(A) ≤ W_k(A)` — correct. (b): `P(b) = kab²+1`, coefficients `≤ kA ≤ B^l`,
ρ(p^j) ≤ 4 (I recomputed: ρ(2)=1, ρ(4)∈{0,2}, ρ(2^j)∈{0,4} for j≥3 when ka odd; odd p ∤ ka: Hensel,
≤ 2) — correct; ET p. 30 states the same.

**The (m₀,k)=1 indicator.** Re-derived case by case (odd m₀):
* `(m₀,k) > 1`: `P ≡ 1 (mod p)` for `p | k`, so ρ = 0; RHS 0 by definition.
* `(m₀,k)=1`, `(m₀,a) > 1`: ρ = 0; RHS `= Π_{p^j∥m₀} Σ_{i≤j} (−ka/p^i)`, factors with `p | a` are 1,
  others ≥ 0 — so RHS ≥ 0 = LHS.
* `(m₀,ka)=1`: ET p. 31. Correct.
Brute force (`review_emn3_prop23.py`, part 1): all k ≤ 40, a ≤ 12, odd m₀ ≤ 400 — **0 failures**;
ρ(2^j) ≤ 4 for K < 200, j ≤ 8 — 0 failures.
ET indeed drop the indicator: their final sum (p. 31, display before (7.11)) is
`Σ_{q:(q,2k)=1} Σ_a (−ka/q) Σ_{m≤B: q|m} 1/m`, i.e. `n = m/q` unrestricted, which is where the
`log B` instead of `(φ(k)/k) log B` enters. The author restricts `n` to `(n,2k)=1`: legitimate,
because the indicator `(m₀,k)=1` is a property of `m₀ = qn` and (q,k)=1 is forced anyway.

**q-ranges.** The four ranges {squares ≤ Q₂}, {non-squares ≤ Q₁}, {non-squares in (Q₁,Q₂]},
{all q > Q₂} *are* a partition once the square range is read as "squares ≤ Q₂" (the text bounds all
squares, which dominates since square terms are ≥ 0). So the "non-partition" remark in the text is
correct but unnecessary — see defect m1.
* Small q: `Σ_{a≤A} (−ka/q) = (−k/q) Σ_{a≤A} (a/q)`; PV for the non-principal `(·/q)`;
  `Σ_{q≤Q₁} W(B/q) q^{−1/2} log q ≤ W(B) · O(√Q₁ log Q₁)` — correct. (ET used the period bound O(q)
  and silently mishandled squares — "sums to zero" is false for square q; the author's separate
  square range repairs ET as well.)
* Middle: trivial, correct.
* Large q: weight `g(q) = W(B/q)/q` is positive non-increasing, partial sums of χ_D bounded by
  `C√(4ka) log(4ka)`; Abel gives `≤ 2·sup|S|·g(Q₂⁺) ≤ … W(B/Q₂)/Q₂`. Correct; the `(q,k)=1`
  restriction is automatic since χ_D(q) = 0 when (q,2ka) > 1.
* Choice 1: checked both sub-cases `Q₂ = kA ≥ Q₁` (middle log ≤ log k + O(1), tail
  `A^{1/2}k^{−1/2} log(2kA) ≪ A`) and `Q₂ = Q₁ > kA` (tail `≤ W(B) log(2kA) log(2A) ≪ A W(B)`).
  Choice 2: both PV and tail give `A^{1/2}k^{1/6} log(2kA)`. Correct.
* `Σ_j ρ(2^j)/2^j ≤ 1 + 4·1 = 5 ≤ 9` — the constant 9 is safe.

**Numerics (from scratch, part 2 of the script).** See §1.1 below.

### 1.1 Numerics (EVIDENCE; `scripts/review_emn3_prop23.out.txt`)
`S(k,A,B) = Σ_{a≤A,b≤B} τ(kab²+1)` for 34 values of k (1…6, all primorials up to 29#, primes
101…100003, 2·3·1009, 4·1009·1013, 2^10, 3^8) and boxes (A,B) ∈ {(2,3000),(6,1000),(40,150),(150,40)}.
* `S/((φ(k)/k)·AB log max(A,B)·Λ)` ∈ [0.18, 1.6] over all 136 cases, non-increasing in k: no sign of
  a hidden k-dependence in the constant (the small-A boxes are where `Λ = 1+log(1+k)` is active).
* The gain is real and visible: `S/(AB log B)` is 2.3–3.0 for prime `k ≈ 10⁵` but 0.85–1.28 for
  `k = 29# ≈ 6.5·10⁹` (larger n, yet fewer divisors), ratio ≈ `φ(k)/k`-driven.
* ET's `log(1+k)` normalisation decays to 0.04 — consistent with ET's bound being lossy in k.

## 2. Prop 2.5 and Theorem L'

Re-derived line by line.
* Substitution `ma²d+1 = k a'²d'+1`, `k = ms²t`, `φ(k)/k ≤ φ(m)/m`: correct; this is the only way the
  gain enters, and the BT factor `1/φ(m)` (from `φ(mad) ≥ φ(m)φ(ad)`) is then cancelled to `1/m`.
* Exponent bookkeeping with l = 30: `D' ≥ max(A',k^{1/28}) ⇒ kA'² ≤ D'^{28+2}`; `A' > max(D',k^{1/28})
  ⇒ kD' ≤ A'^{29}`. Correct. Size hypotheses of Prop 2.3 (`≥ ω(2k)+2`) hold once `k^{1/28} ≥ ω(2k)+2`,
  true for k ≥ m₀ (absolute, since `ω(n) ≪ log n/log log n`). Correct.
* Λ: `Λ ≤ 2` unless `D' < k^{1/3} log²(2kD')`; number of such dyadic D' ≪ `log(2k) + log L`. Per
  (s,t): `(st)^{−2}[L·log X + (log 2k + log L) log X log(1+k)] ≪ (st)^{−2}[L² + L log²(2ms²tL)]`, and
  `Σ_{s,t}(st)^{−2} log²(ms²tL) ≪ log² m` using `log L ≤ log m`. Correct.
* Block sum `Σ_{j≤2L} 1/j ≍ log L`: count `≪ (N/φ(m))·(φ(m)/m)(L²+L log² m) log L`. Correct.
* Tiny boxes: `n ≤ k(2A')²(2D') ≤ 8k^{1+3/28} ≤ 8k^{1.11}`; `τ(n) ≪ n^{0.0108} ≪ k^{0.012}` (absolute
  constant, effective). Occurrence: `X < st·a'd' ≤ 4st·k^{1/14} ≤ 4m^{1/14}(st)^{8/7}` (s²t ≤ (st)²).
  Mass: grouping by `u = st` (multiplicity τ(u) — this is where the `τ(st)` comes from; the text should
  say so, m2), `Σ_{u≥U} τ(u)u^{−2}(mu²)^{0.012}·#boxes ≪ m^{0.013} min(1, U^{−0.97})`,
  `U = (X/4m^{1/14})^{7/8}`, giving exponent `0.976·7/8 ≈ 0.85`. Summed over blocks: ≪ `log m` blocks
  with X ≤ m^{0.072}, geometric beyond: `≪ m^{0.014}`. Count `N m^{0.014}/φ(m) ≪ (N/L)m^{−0.35}` needs
  `L·m^{0.014}·log log m ≤ m^{0.65}`: fine for `L ≤ m^{1/2}`. **Exponents correct.**
* Theorem L': MN2 Prop 3.2 already has `/m`; `m^{0.02}/m ≤ m^{−0.35}`. The consequence: I checked
  `L² log² m ≤ L³ + log⁶ m` (case split `log² m ≤ L`), that `L³ log L/m → 0` forces m → ∞ (N ≥ 16),
  and that the `log m > L/10` range (MN2 Lemma 3.5, `e^{CL/log L}/m = m^{O(1/log L)−1}`) also → 0.
  Also `L > m^{1/2}` makes the hypothesis `L³ log L/m → 0` impossible, so the range restriction is harmless.
* Propagation through MN2: MN2 Prop 3.4's skeleton (PW (3.2), ET (A.12), BT weight) is reused
  unchanged; only MN2 Lemma 3.3 is replaced by Prop 2.3, and MN2 Prop 3.2 (Type II) already had `1/m`
  after the R102A/B repairs. MN2's lossy-box criterion `D' < k log⁴` is replaced by the sharper
  `D' < k^{1/3} log²`; both are only used through a box *count* ≪ `log(2k)+log L`, so nothing else changes.

| Claim | Verdict |
|---|---|
| Prop 2.5 | SOUND (exponents verified) |
| Theorem L' | SOUND; label should add PV and "rel. MN2 Prop 3.2" (m3) |

## 3. §1 and §3 — Type I log log

**§1 quotes.** Checked in ET: p. 5 quote verbatim (line "The double logarithmic factor …"); §9
p. 36 parenthesis literally reads "Type II case" (pdf line 1931) — the author flags the reading
"[means Type I]" explicitly; that reading is the natural one (the preceding sentence says the trick
*avoids* the Type I loss). ET (8.1)/(8.2) and the block cost `N log² N/j` (j = log c) re-derived; the
"only c ≤ N^ε matters, c > N^ε costs log(1/ε)" claim is correct.

**Lemma 3.1 (SL₂ form).** All four identities re-derived by hand (`σ_d([[p,q],[r,s]]) = [[p,r/d],[dq,s]]`,
fixed iff `r = dq`; anti-involution; Γ₀(d)-stability). Form `[f,4ad,de]`: disc `16a²d² − 4def = −4d`;
primitive since f is odd and coprime to ad. After `X↔Y`, `[de, 4ad, f]` has `d | A`, `B ≡ 0 (2d)`,
`B² ≡ D (4d)`, root `τ = (−2a + i/√d)/e` — matches the text. Parity counterexample `γMγᵀ = [[10,7],[7,5]]`
re-computed. Brute force (`review_emn3_sec3.py`): all `Σ^I_p` identities, det = 1, `M₂₁ = dM₁₂`,
`p = 2cM₂₁ − M₂₂`, disc −4d, primitivity and the twin identity hold on every Type I point for all
primes `3 ≤ p < 180` — 0 failures. **SOUND.** Caveat (m4): here `D = −4d ≡ 0 (mod 4N)` with N = d,
so these are Heegner/CM points in the Gross–Kohnen–Zagier sense *without* the Heegner hypothesis
`(D, N) = 1`; the classical equidistribution literature (Duke, Michel–Harcos, …) is mostly stated for
fixed level or coprime (D,N). The text should say so where it invokes "Heegner points".

**Lemma 3.2.** Spot-checked five moduli by hand ((a,c,f): `d ≡ d₀ (f)` ⇒ step 4acf; (c,d,f): roots
of `4da²+1 ≡ 0 (f)` ⇒ 4cdf; (a,d,·) ⇒ 4ad; (a,b,·) with e ⇒ 4ab; (b,d,e) ⇒ 4bd). Completeness
correctly labelled EVIDENCE. SOUND as labelled.

**Prop 3.3.** Exponents re-derived from `acd ≍ n`, `ce ≍ b`, `ef ≍ 4a²d`, `ff' = n²+4c²d`. Of the seven
inequalities, `4bd`, `4bcf'`, `4cdf'` are automatic (`β ≥ α`, `γ ≤ η`, `α ≤ 1`); the rest give R_bad.
Areas recomputed exactly (1/24 + 1/8 = 1/6; R**: `∫_{1/2}^{2/3}(α−1/3) + ∫_{2/3}^1(1−α) = 1/24 + 1/18 = 7/72`)
and by grid (`0.1668`, `0.0973`). Limiting-slice divisor claim and the finite-η counterexample
(α = β = 0.6, γ = η = 0.05: e-exponent 0.55 < 0.6) checked. **SOUND (PROVED geometry).** The
mass/"no trick" consequence is correctly labelled Assessment. I also checked the log-uniform heuristic
is the right one: in coordinates (α, φ = f-exponent) the divisor heuristic gives uniform density on
the unit square, and `β = 1+α−φ` is area-preserving onto the stated slice.

**§3.4–3.6.** Assessment-labelled sketches. (W_e)/(W_f) thresholds `(3/2)(β−γ) < 1−γ` reproduced from
"main `AD/e` vs Weil error `(eq)^{1/2+ε}`"; (N2) arithmetic `(RV)^{1/2} ≍ N^{3/2}(log N)^{1/2}/C` vs
main `N log N` re-derived. Labels adequate.

**Theorem 3.8.** Re-derived:
* `f_I(p) ≤ 2Σ_c w_c(p)`: ET Prop 2.2 (unique normalized sextuple per solution) + Lemma 2.8 for y ≤ z,
  and the point is determined by (a,c,d,f) via `e = (4a²d+1)/f`, `b = ce − a`. Brute-forced for all
  primes 3 ≤ p < 180 (ordered Type I solutions found from scratch by enumerating 4/p = 1/x+1/y+1/z):
  0 violations.
* Part (1): BT with `log(N/4ad) ≥ η₀ log N − O(1)`, and `Σ_{ad≤N} τ(4a²d+1)/φ(ad) ≪ log³ N` from ET (8.2)
  over ≤ log N dyadic blocks: `≪ η₀^{−1} N log² N`. Correct.
* Part (2): `c < N^{η₀}`; z = `N^{min(θ,1)/2}`, sieve level `z² ≤ N^θ` matches LD's q-range; primes in
  (N/2, N] are unsifted. (Ω₁) with `ℓ₀ = 2C₀+2`: `h(ℓ)/ℓ ≤ 1/ℓ + C₀/ℓ² < 1/2`. (Ω₂(1)) holds with
  `A₂ = O(C₀)`. `Π_{ℓ₀<ℓ<z}(1 − h(ℓ)/ℓ) ≪_{C₀} 1/log z` from `h ≥ 1 − C₀/ℓ`. The weights `w_c` are
  non-negative integers, so the sequence-with-multiplicity setting of Halberstam–Richert applies.
  `X_c ≪ (N/c) log² N` (ET Prop 1.4 with k = 4 over ≪ log N dyadic boxes per scale, ≪ log N scales).
  `Σ_{c≤N^{η₀}} X_c/log z ≪ (η₀/θ') N log² N` — the `log N^{η₀}` from Σ 1/c is exactly cancelled by
  `1/log z`. Correct.
* Sanity of LD (is it vacuous?): local densities computed heuristically: `h_c(2) = 0` (n odd — allowed,
  the lower bound is only imposed for ℓ > 2); for `ℓ | c`, `ℓ | n ⇔ ℓ | f`, and the τ-weighted density
  of `ℓ | f` is `≈ (1/ℓ)·(1 + 1/ℓ)^{−1}`, i.e. `h ≈ 1 − 1/ℓ` — inside the allowed window. So LD is not
  refuted by local obstructions. (Not a proof that LD is true; it is a hypothesis.)
* Source: Halberstam–Richert Thm 4.1 / Lemma 4.1 are **not in `sources/`; I could not check the exact
  statement**. From memory, Thm 4.1 is `S ≤ X/G(z) + Σ_{d<z², d|P(z)} 3^{ν(d)}|R_d|` under (Ω₁), and
  Lemma 4.1 gives `1/G(z) ≪ W(z)` under (Ω₁), (Ω₂(κ)) — consistent with the use made.
**Theorem 3.8: SOUND (PROVED implication).** Remark (b) is correctly labelled "proposed, not proved".

| Claim | Verdict |
|---|---|
| Lemma 3.1 (SL₂ / Heegner) | SOUND; terminology caveat m4 |
| Lemma 3.2 | SOUND as labelled (completeness EVIDENCE) |
| Prop 3.3 (R_bad area 1/6) | SOUND |
| §3.4 R** area 7/72 | SOUND (area); method claims Assessment, correctly labelled |
| Theorem 3.8 (LD ⟹ OPEN-I) | SOUND (HR not in sources — m5) |

## 4. Defects

No FATAL, no MAJOR found. I specifically looked for, and did not find: a k-dependent constant in
Prop 2.3 (ET Thm 7.1's constant depends only on degree, l and C = 4; PV constants are absolute);
a hidden `(q,k)=1` mismatch between the indicator and the Kronecker character (it is automatic);
circularity between Thm L' and MN2 (only MN2 Lemma 3.3 is replaced); an LD hypothesis that is
locally impossible (local densities fit the window).

* **m1 (MINOR, Prop 2.3 proof, "squares" bullet / "all q > Q₂" bullet).** The "not a partition"
  remark is confusing: with the square range read as `q = r² ≤ Q₂` the split *is* a partition; the
  bound for all squares merely dominates. *Repair (applied, marked):* state the range as `≤ Q₂`.
* **m2 (MINOR, Prop 2.5 tiny boxes).** `τ(st)` appears without explanation. *Repair (applied):*
  it counts pairs (s,t) with product u after grouping.
* **m3 (MINOR, labels of Prop 2.5 / Theorem L').** Dependencies omitted PV (through Prop 2.3) and
  MN2 Prop 3.2 / Lemma 3.5 / Prop 3.4's set-up. *Repair (applied):* labels extended.
* **m4 (MINOR, Lemma 3.1 and §3.5).** "Heegner points of discriminant −4d on X₀(d)": correct as
  forms (`[de,4ad,f]`, d | A, B ≡ 0 (2d), primitive), but `(D,N) ≠ 1` — no Heegner hypothesis; the
  standard equidistribution theorems do not apply as stated. The report's "(H**) … Heegner points"
  should carry the same caveat. *Repair (applied at Lemma 3.1).*
* **m5 (MINOR, Thm 3.8 proof).** Halberstam–Richert is not in `sources/`; Thm 4.1/Lemma 4.1 checked
  from memory only. *Repair (applied as a note):* flag it; the parent may want to add the HR pages.
* **m6 (MINOR, §1 quote).** ET's parenthesis literally says "Type II case"; the author's "[means
  Type I]" gloss is reasonable and flagged, but the report's ledger text ("our reading of ET's 'no
  similar trick' remark") should keep the [sic] visible. No repair needed in the document.

## 5. Final verdict

| Claim | Verdict |
|---|---|
| Lemma 2.1, 2.2 | SOUND |
| Prop 2.3 (coprimality-gain ET Prop 1.4) | SOUND-AFTER-REPAIRS (m1, presentational) |
| Prop 2.5 (tiny-box exponents) | SOUND-AFTER-REPAIRS (m2, m3) |
| Theorem L' | SOUND-AFTER-REPAIRS (m3, label only) |
| Lemma 3.1 (SL₂; Heegner identification) | SOUND-AFTER-REPAIRS (m4) |
| Lemma 3.2 (moduli list) | SOUND as labelled (completeness EVIDENCE) |
| Prop 3.3 (R_bad, area 1/6) | SOUND |
| §3.4 (R**, area 7/72) | area SOUND; method claims Assessment (correct label) |
| Theorem 3.8 (LD ⟹ OPEN-I) | SOUND (m5: HR unchecked against source) |
| Ledger text in AGENT_REPORT_O108 | acceptable; add PV + MN2 dependencies to Thm L' label |

The headline claim — MN2 open point (ii) (the m/φ(m) loss) is closed, Theorem L' holds with `/m`;
the Type I log log is NOT removed — is supported.
