# Hostile review: POINTWISE_OMEGA.md §§0–7 (branch `side-agent/pointwise-omega`, Theorem 5.1)

## What was reviewed

* **Subject.** `POINTWISE_OMEGA.md` §§0–7 and `AGENT_REPORT_C2.md` (checkpoint 1), at commit
  `094999e`. I also checked the branch head `1dd87a3`. Its §§1–7 are byte-identical to `094999e`
  except that §0 gains item 5 and §7 gains the last bullet. So everything below applies to
  `1dd87a3` too.
* **Not reviewed.** The checkpoint-2 material (§8 Type-I frame, §9 Haar side, §0 item 5). It falls
  outside this brief and needs its own review; see §5.
* **Sources and context read.**
  * Thorner–Zaman, arXiv:2108.10878v2: the archived pdf/txt, with its sha256 checked against
    `sources/lit2026/README.md`. Read: §1 (Thm 1.1, Rem. 1.2–1.3, (1.3)–(1.8), Cor. 1.4,
    Rem. 1.5) and §2 (Thm 2.1, Thm 2.3, derivation of Thm 1.1).
  * notes (51.1)/(51.2), (51.19), §54 (Thm 54.1, Cor. 54.2), (58.2)/(58.3), Lemma 58.5, Thm 17.3(c),
    Lemma 33.3, Prop. 33.2, Thm 51.2.
  * POINTWISE_SIZE §§7, 11 and §12.
* **Method.** Every proof in §§1–6 was re-derived by hand.
* **Code.** All code is independent: `scripts/review_omega_*.py` imports nothing from
  `pointwise_omega_*`. Outputs are in `data/review_omega/`.

## Verdict: **SOUND-AFTER-REPAIRS** (no mathematical defect in any load-bearing statement)

Theorem 5.1 survives. For infinitely many Mordell-hard primes,
`W(p) ≥ (log p)^2 exp(−C log log p/log log log p)`. This is **PROVED modulo Thorner–Zaman
Cor. 1.4** (which carries the McCurley-region uniqueness statement TZ use to define λ; see D1).

* I checked the citation literally against the source. Its use in Theorem 4.1 is legitimate:
  * the error is relative to `λx/φ(q)`;
  * the constants are absolute and effective;
  * the range is `x ≥ q^{12}`;
  * the ℓ¹ summation over the Bonferroni terms is fine.
* Lemma 3.2 and the Case A/B split are correct. The "unique severe character" claim holds
  across the family, and the Case-B twisted mean is controlled with the correct sign handling.
* Lemmas 2.1 and 2.3, the Brun minorant, and the parameter count giving exponent 2 are correct.
* Consequence: H_MOD(A) (notes (51.19)) is false for every `A<2`, with the same citation label.

The defects are labelling, scope and wording problems (D1–D12). None changes a theorem.

| Item of the brief | Verdict |
|---|---|
| (1) Thorner–Zaman statement and its literal application (Thm 3.1, Thm 4.1) | **SOUND** (citation label: D1, D2) |
| (2) Lemma 3.2, Case A / Case B of Thm 4.1 | **SOUND** |
| (3) Lemma 2.1, Lemma 2.3, Brun minorant (mean, mass, twist), parameter optimisation | **SOUND** (cosmetic D7; parameter remark D8) |
| (4) `W(p)>T` is literally what is certified; hardness; distinct primes | **SOUND** |
| (5) Labels of Prop 6.1, Prop 6.3, Thm 6.2; H_MOD refutation vs notes (51.19)/§54 | **SOUND-AFTER-REPAIRS** (D3, D5, D10, D12) |

## 1. The citation (item 1)

### 1.1 What Thorner–Zaman actually state

The source is `arxiv-2108.10878-thorner-zaman-pntap.txt`, ll. 37–39, 121–131 and 46–96.

* **Corollary 1.4.** There is a constant `c_4>0` with the following property. If `q≥2` and a are
  coprime integers, `x≥q^{12}`, and `λ=λ(x,q,a,x)` is as in Thm 1.1, then

  ```
  Σ_{p≤x, p≡a (q)} log p = (λx/φ(q)) [1 + O(exp(−c_4 log x/log q) + exp(−c_4 (log x)^{3/5}/(log log x)^{1/5}))].
  ```

  "The implied constant and c_4 are absolute and effectively computable."
* **Remark 1.5.** `λ(x,q,a,x)=1−χ_1(a)x^{β_1−1}/β_1` if `β_1` exists. I checked this against
  the integral definition in Thm 1.1 with `h=x`: `(1/x)∫_0^x(1−χ_1(a)t^{β_1−1})dt` gives the same
  value.
* **Definition of `β_1`.** The McCurley sentence (ll. 37–39) defines `β_1` and `χ_1` for
  modulus q. There is at most one real zero in `Re s ≥ 1−1/(13 log(q(|Im s|+3)))`. It is simple,
  and its character is unique.
* **No other conditions.** The statement imposes nothing further on q or a. It has no "x ≥ c_3"
  clause (that is absorbed), and no smoothness condition or Siegel hypothesis.

**The derivation of Cor. 1.4 from Thm 1.1 (sanity check).**

* Thm 1.1 needs `λx/φ(q) ≥ x^{θ+ε}`, with `θ=32/37` and `ε=1/555`, so `1−θ−ε=74/555=2/15`.
* (1.7) and the effective Siegel bound `1−β_1 ≫ q^{−1/2}` give `λ ≫ q^{−1/2}log q`.
* `x ≥ q^{12}` makes `φ(q)x^{θ+ε−1} ≤ q^{1−12·2/15} = q^{−0.6}`. This is consistent with (1.8):
  `δ_2=1/12 ≤ 2/15`.
* In Thm 2.3 the prefactor `√(x log x/(h log q))` is absorbed in (2.5) by shrinking the
  constant. So the O-term really is relative, with absolute constants. The source states this
  explicitly (ll. 76–80): "(1.3) and (1.4) are each scaled by λ".

### 1.2 The application in Theorem 4.1, checked literally

* **Moduli and range.**
  * The moduli are `q_i=Qd_i ≤ Z`, with classes `a_i` that are units (`gcd(b_i,d_i)=1`,
    `a_i≡1 (Q)`).
  * `log x ≥ C_1 K log Z ≥ 12 log Z`, so `x ≥ q_i^{12}` for every i.
  * Each relative error is `≤ C_0E_1`, because `log q_i ≤ log Z`.
* **Uniformity and the ℓ¹ sum.**
  * Each term is a separate application of Cor. 1.4 with absolute constants. The total error is
    `|Σ c_iλ_iε_i/φ(d_i)| ≤ 2C_0E_1·Σ|c_i|/φ(d_i) = 2C_0E_1M_1`.
  * The number of terms (about `T^J`) never enters. Only the ℓ¹ mass `M_1 ≤ e^S` does. This is
    legitimate.
  * The positivity requirement `E_1 ≤ μ/(8(C_0+1)M_1) ≈ e^{−3S}` costs
    `log x ≫ S·log Z + S²`.
* **The identity `Σ_{p≡1(Q)} log p·B(p) = Σ_i c_iθ(x;q_i,a_i)`.** Primes dividing some `d_i`
  cannot lie in a unit class mod `d_i`. Every prime counted satisfies `p>Q>T`.
* **Remark (ii) of Thm 4.1 is right.** PNT uniform only for `q ≤ exp(c√log x)` would force
  `log x ≳ (log Z)^2 ≥ y^2 ≥ T`. The Linnik-range relative form is what makes exponent 2
  possible.
* **The published version was not checked.** Only arXiv v2 (2021) was read; the Math. Z. 2024
  text may differ in numbering or constants (D2). The source's own description of Deuring–Heilbronn
  entering through Thm 2.1/(2.2) via Jutila is accurately reported (ll. 212–251).

## 2. Lemma 3.2 and the Case A/B split (item 2)

### 2.1 Lemma 3.2

**At most one severe pair.**

* Suppose `(χ_a,β_a)` and `(χ_b,β_b)` are severe. Put `q'=lcm(q_a,q_b) ≤ Z²`.
* The induced characters mod q′ have the zeros of the primitive ones in `Re s>0`. The extra Euler
  factors vanish only on `Re s=0`.
* Both β lie in `[1−1/(13 log 3Z²),1) ⊆ [1−1/(13 log 3q'),1)`, which is the McCurley region for
  q′ at `t=0`.
* "At most one real zero, unique χ_1" for q′ then forces `β_a=β_b` and `χ_a=χ_b`, as primitive
  characters.

**Identification with TZ's `β_1`.**

* If `q*|q≤Z`, then `β* ≥ 1−1/(13 log 3Z²) ≥ 1−1/(13 log 3q)`, so `β*` is TZ's `β_1` for q.
* If no severe pair has `q*|q`, then any `β_1` of q is `<1−1/(13 log 3Z²)`.
* Since `1−1/(13 log 6)=0.957>1/2`, we get `x^{β_1−1}/β_1 ≤ 2E_2`.

All of this is correct. The proof uses only the McCurley sentence as quoted by TZ (D1).

### 2.2 Case A (`q*|Q`)

* For every i, `χ_1 mod q_i` is induced by χ*, and `χ*(a_i)=χ*(1)=1` because `a_i≡1 (Q)`. So
  every `λ_i=λ_*=1−x^{β*−1}/β*`.
* `λ_*>0` for `log x>2`, `β*≥1/2`. Indeed `−log β ≤ 2(1−β)` gives `(β−1)log x − log β < 0`.
  This is also checked on a grid in `review_omega_constants.py`.
* `λ_*` is common to all terms, so it factors out. Positivity is then `μ > C_0E_1M_1`.
* No lower bound on `1−β*` is needed. That is exactly the point of TZ's λ-scaled error.

### 2.3 Case B (otherwise)

* For a severe χ* with `q*'>1`:
  * `q*|q_i` holds iff `q*'|d_i`. This uses `gcd(d_i,Q)=1`; also `q*_Q|Q` is automatic, since
    severity puts q* inside some `q_i`.
  * For such i, `χ_1(a_i)=χ*_Q(1)·χ*'(b_i)=ψ(b_i)`.
  * `ψ=χ*'` is real primitive with conductor `f=q*'>1`, coprime to Q, and dividing some `d_i`.
    So the twist hypothesis covers it.
* **The main term.**
  * Put `η=x^{β*−1}/β*∈(0,1)` for `log x>2`. Then
    `Σc_iλ_i/φ(d_i) = μ − ημ_ψ + Σ_{other i}c_i(λ_i−1)/φ(d_i) ≥ μ − 2|μ_ψ| − 2E_2M_1`.
  * **Sign issues.** This lower bound does not depend on the sign of `ψ(b_i)` or of `c_i`.
    `|μ_ψ| ≤ μ/4` leaves `μ/2`, so no cancellation against the main term is possible.
  * The error term uses only `λ_i<2`. In fact `|λ_i−1|<1` for `log x>2`.
* **The constants.** The conclusion's threshold `E ≤ μ/(8(C_0+1)M_1)` makes both brackets
  positive (checked). The bound `u^{3/5}/(log u)^{1/5} ≥ u^{1/2}` holds for all `u>1`, since
  `√u ≥ log u`.

**Verdict for item 2: SOUND.**

## 3. Lemmas 2.1, 2.3, the Brun minorant, the parameters (item 3)

### 3.1 Lemma 2.1

The proof is correct.

* `ℓ>y≥√T` gives `ℓ‖M` and `m=M/ℓ<T/y≤√T≤y`.
* m is y-smooth with prime powers `≤T`, so `m|Q`.
* `n≡−4D (M)` with `n≡1 (m)` forces `m|4D+1`.

The stated converse also holds by CRT.

**Independent check** (`review_omega_local.py`). It builds `F_ℓ` by *projecting the full
atom sets* 𝓡(M) onto `c≡1 (mod m)`. That is the definition, not the author's `(m,D)` recipe.
Then it computes W(n) from scratch over all `M≤T`:

| T | `log Q` | random `n≡1 (Q)` | with `W>T` | mismatches | forced survivors with `W≤T` | forced single hits with `W>T` |
|---|---|---|---|---|---|---|
| 1000 | 66.5 | 20000 | 17 | 0 | 0 / 1000 | 0 / 1000 |
| 4095 | 131.7 | 20000 | 0 | 0 | 0 / 500 | 0 / 500 |

The last column tests the converse. The same script verifies, for all `M<1200`, that
`{−uv^{−1}: uvw=A_M}` equals `{−4D: D|A_M²}`. This is notes (51.2) ⟺ (58.3), with 0
mismatches, so the doc's 𝓡(M) is the notes' W.

### 3.2 Lemma 2.3

Re-derived step by step.

* **The involution.** `D↦A²/D` preserves `m|4D+1`: `4A≡1`, `D^{−1}≡−4`, so
  `4A²D^{−1}≡−1 (m)`.
* **The parametrisation.** `D|A² ⟺ sr|A` for `D=sr²`, s squarefree. Prime by prime this reads
  `2v(r)+v(s) ≤ 2v(A) ⟺ v(r)+v(s) ≤ v(A)`.
* **Injectivity and the weight.** `(m,ℓ,D)↦(m,s,r,k)` is injective. Also
  `1/(ℓ−1) ≤ 2/ℓ = 2m/(4A−1) ≤ 2m/(3A)`.
* **The key congruence.** `m | (4sr²+1)+(4srk−1) = 4sr(r+k)` and `gcd(m,4sr)=1` give `m|r+k`.
  Then `k≥max(r,m−r)≥m/2`, and the progression sum is `≤ (3+log X)/m`.
* **The first display** follows. The second uses `4sr²+1 ≤ T+2` and Wigert.

All steps are correct.

**Numerical chain** (`review_omega_S.py`, `y=√T`). It computes the triple sum, the parametrised
`(m,s,r,k)` sum *before* the k-bound, and the closed majorant. Each must dominate the previous one.

| T | S (mine) | S (doc) | `g_max` | triple sum | param. sum | display (c) | doc's "majorant" |
|---|---|---|---|---|---|---|---|
| 10³ | 6.4836 | 6.48 | 0.326 | 7.80 | 70.8 | 377.7 | 440 |
| 10⁴ | 13.5572 | 13.56 | 0.211 | 16.26 | 170.8 | 944.8 | 1066 |
| 10⁵ | 23.9360 | 23.94 | 0.159 | 28.15 | 348.5 | 1985.0 | 2195 |
| 10⁶ | 38.4911 | 38.49 | 0.083 | 44.51 | 635.2 | 3710.7 | 4044 |

* All inequalities hold. Fact 1.1 had 0 failures on the quarantined moduli.
* S lies between `(log T)^2` and `(log T)^3`: `S/(log T)^2` rises 0.136→0.202, while
  `S/(log T)^3` falls. Only `T^{o(1)}` is used.
* The doc's "majorant" column is a slightly weaker variant of the display (D7).

### 3.3 The Brun minorant

* **Sign.** `Σ_{j<J}(−1)^jC(N,j) = (−1)^{J−1}C(N−1,J−1) ≤ 0` for `N≥1` and J even, so
  `B ≤ 1[N=0]`.
* **Mean.** `μ−V = −E[C(N−1,J−1)1_{N≥1}]`. Also `C(N−1,J−1) ≤ C(N,J)`, which is trivial for
  `N<J` and equals `(J/N)C(N,J)` for `N≥J`. Hence `|μ−V| ≤ e_J ≤ (eS/J)^J ≤ e^{−2J}`, because
  `e/22 < e^{−2}`.
* **Mass and density.** `V ≥ e^{−2S}` when `g≤1/16`, and `M_1 ≤ e^S`.
* **The twist formula.** `μ_ψ = (−1)^r∏h·(inner truncated sum)` is right. ψ is forced to be
  `(·/f)` for odd squarefree f. Both tail cases (`r≤J/2`, `r>J/2`) are right, and the total is
  `|μ_ψ| ≤ V/15 + e^{−6}e^{−13S}V ≤ 0.07V < 0.2475V ≤ μ/4`.

**Independent checks** (`review_omega_bonf.py`).

* **Part 1: exhaustive, tiny system.** Five primes 11–23 with random `F_ℓ`, J=2,4. It expands B
  into explicit `(c_i,b_i,d_i)`. Checked: `B(n)≤1[N=0]` for every n mod ∏ℓ; μ equals the unit
  average of B; and `μ_ψ`, computed *from the definition with the Jacobi symbol*, equals the
  product formula for every `P_f`. All OK.
* **Part 2: random and extremal `g≤1/16`, S up to 20, precision adaptive to `e^{−2J}`.**
  * Checked: `|μ−V| ≤ e_J ≤ (eS/J)^J ≤ e^{−2J}`, `μ≥0.99V`, `M_1≤e^S`, and
    `log(M_1/μ)=2S+o(1) ≤ 3S+1`.
  * The worst twist over all r, with `h=g` on the largest g's, is `|μ_ψ|/μ ≤ 0.067`.
  * All OK.
  * (A first run at 400 digits produced a precision artefact at S=20. It was fixed by adaptive
    precision, not by loosening the test.)
* **Part 3: actual `F_ℓ`, T=10⁴, y=√T.** This is outside the hypotheses, since 48 primes have
  `g>1/16`. Here `μ/V=1.000000` and `−log V=14.0`. The worst r=1 twist is
  `|μ_ψ|/μ = 0.267 > 1/4`. So **at the EVIDENCE parameter `y=√T` the twist condition fails**. The
  hypothesis `g_max≤1/16`, and with it the factor `exp(3𝓛/log𝓛)` in y, is load-bearing, not
  cosmetic (D8).

### 3.4 Parameters (exponent 2)

* **Size of Q.** `log Q ≤ θ(y)+π(√T)𝓛+log 24 ≤ 2y` holds for large T.
* **Size of Z.** `log Z ≤ log Q+(J−1)𝓛 ≤ 3y`.
* **Size of K.** `K = 1+log(M_1/μ) ≤ 3S+2 ≤ log Z`.
* **Size of p.** `log p ≤ C_1(3S+2)·3y = √T·exp((3+log 2+o(1))𝓛/log𝓛)`.
* **Inversion.** This gives `T ≥ (log p)^2 exp(−O(log log p/log log log p))`.
* **Distinct primes.** Infinitely many distinct p arise because `p>Q>T`. This is needed, since
  `W(p)<∞` is unknown.
* **Effectivity.** Wigert can be made explicit (Nicolas–Robin), so `g≤1/16` holds as soon as
  `y<T`.

The statement is correct.

## 4. What is certified (item 4)

* `W(n)>T` is literally (58.3), and that is the notes' (51.1)/(51.2) (§3.1).
* **Smooth moduli.** Every `M≤T`, `M≡3 (4)`, with all prime factors `≤y` divides Q. This includes
  prime powers `ℓ^e≤T` and M sharing several quarantined primes. Each such M is killed by
  Fact 1.1 (proof checked: `0<D+A≤2A<M`).
* **Other moduli.** Every other M has exactly one prime `ℓ>y`, with `ℓ‖M`. Its smooth cofactor m
  is quarantined, so all `D|A_M²` are accounted for in `F_ℓ`.
* **Hardness.** `840|Q`, so `p≡1 (840)`, which is a Mordell class. This is also `≡1 (24)`, as
  required by `L_h` in notes (58.2).
* **The §5 EVIDENCE primes** were reproduced exactly by `review_omega_primes.py`. They are
  `k=9089, 11715, 13712, 53015, 54335`, with `W(p)=1007, 1151, 1199, 1759, 1475` and
  `log p=75.6–77.4`.

**Verdict for item 4: SOUND.**

## 5. Labels: §6 and the H_MOD statement (item 5)

* **H_MOD.** The notes' (51.19) is `H_MOD(A): W(p)≤(log p)^A` for every sufficiently large prime.
  Theorem 5.1 gives infinitely many p with `W(p) > (log p)^{2−o(1)} > (log p)^A` for each `A<2`.
  So H_MOD(A) is false for `A<2`. This extends Cor. 54.2, which covered `A<1`. A=2 is not
  touched, because of the `exp(−C…)` loss.
* **Lemma 58.5(1).** It uses `L_p`, and `L_p≤L_h`, so the corollary is correctly drawn.
* **Prop 6.1** is correct as stated: class-of-one quarantine, at most one unquarantined prime per
  modulus.
  * One of `ℓ_1ℓ_2` and `3ℓ_1ℓ_2` is `≡3 (4)` and `≤T`.
  * The case `ℓ_1=3` is fine, since then the M is `9ℓ_2` and still has the two free primes.
  * Brute force (`review_omega_pairs.py`): 0 uncovered pairs at T=10⁴ and 10⁵.
  * The unlabelled `c≠1` remark after it is an Assessment (D12).
* **Prop 6.3** is correct for the raw atom list.
  * The `K_{r,r}` configuration at the class `−4`, `D=1`, has CRT probability `≥(2y)^{−2r}`.
  * `C(N−1,J−1) ≥ C(2J−2,J−1) ≥ 4^{J−1}/(2J−1)`.
  * The threshold is `(2√2θ/log 4)^2 = 4.163θ²`.
  * The upper limit `J≤y` is needed and is stated.
  * EVIDENCE was reproduced independently:

    | T, θ | irredundant multi-prime atoms | hubs |
    |---|---|---|
    | 10⁴, 0.3 | 52.1% | |
    | 10⁴, 0.4 | 52.0% | |
    | 10⁴, 0.45 | 50.8% (D9) | |
    | 10⁵, 0.4 | 65.4% | `−16, −36, −12` with 331/320/299 edges on 72/73/72 primes, as stated |

* **Theorem 6.2** is correct.
  * Adjoining `ℓ_0∈(R,2R]` keeps every hypothesis, and the twist family only shrinks.
  * The bound is `log p ≤ T^{θ+2ε+o(1)}`.
  * The polylogarithmic clause needs `A≥1` as written. This is automatic (D10).
  * The label "PROVED modulo Theorem 3.1" is right in the doc but wrong in AGENT_REPORT (D5).

## 6. Numbered defect list

**D1 — LOW (citation bookkeeping).**

* **Location.** §0 item 1 and AGENT_REPORT l.15: "PROVED modulo one cited theorem"; Lemma 3.2:
  "PROVED from the McCurley statement".
* **Problem.** Lemma 3.2 uses a second cited input. That input is McCurley's zero-free region
  with Landau–Page uniqueness for *every* modulus `q'≤Z²`, known only through TZ's paraphrase
  (l. 37: "It follows from work of McCurley [10]"). It is not a hypothesis of Cor. 1.4 for the
  moduli `q_i`.
* **Fix (either suffices).**
  * (a) Say "modulo TZ Cor. 1.4 together with the McCurley-region statement quoted on TZ p. 1".
  * (b) Replace it by the textbook Landau–Page theorem (Davenport ch. 14; absolute effective c).
    The severe threshold becomes `1−c/log(3Z²)` with any `c≤1/13`, and `E_2` becomes
    `exp(−c log x/log 3Z²)`. I checked that Lemma 3.2 and Case B go through verbatim. The
    identification with TZ's `β_1` needs `13c·log 3q ≤ log 3Z²`, which holds for `c≤1/13`.

**D2 — LOW (citation version).**

* **Location.** Thm 3.1 heading: "Thorner–Zaman, Math. Z. 306 (2024), arXiv:2108.10878v2,
  Corollary 1.4".
* **Problem.** Only arXiv v2 (21 Sep 2021) was read. The published Math. Z. 306 (2024) no. 3,
  Paper 54 was not checked for numbering or constant changes.
* **Fix.** Add "statement and numbering as in arXiv v2; published version not compared".

**D3 — LOW-MEDIUM (unlabelled overclaim).**

* **Location.** §6.2, l. 555 (at `1dd87a3`).
* **Quote.** "On the Haar side the corresponding statement is easy: the local lemma, as in notes
  Thm 31.4 and POINTWISE_SIZE Lemma 11.7, gives void probabilities."
* **Problem.** For `θ<1/2` the Haar analogue was not proved anywhere at checkpoint 1.
  * Notes Thm 31.4 is for integer residues: its quarantine `n≡0` is unavailable for units, as
    POINTWISE_SIZE §7.3(i) explains.
  * Lemma 11.7 is the case `θ≥1/2` only.
  * AGENT_REPORT's own next step (a) calls it "feasible but technical".
  * The branch's later §9 proves only `T^{1/3+o(1)}` unconditionally, and polylog only under the
    open H_PP. This contradicts "easy".
* **Fix.** Replace the sentence with: "On the Haar side the corresponding void-probability bound
  is known for `θ≥1/2` (Lemma 11.7) [and `θ>1/3`, §9]; for smaller θ it is open (§9, H_PP). What
  is missing on the prime side in addition is a pointwise minorant…"

**D4 — LOW (scope).**

* **Location.** §0 item 2.
* **Quote.** "This is exactly the 'mean value for divisors of `((M+1)/4)²` in the class
  `−(M+1)/4 mod m`' that POINTWISE_SIZE §7.3(i) lists as missing."
* **Problem.** §7.3(i) asks for it in the polylog-quarantine, multi-prime (LLL) setting.
  Lemma 2.3 is the global prime-local (`y≥√T`) instance. §7 of the doc states this correctly
  ("in the prime-local setting"); §0 does not.
* **Fix.** Add "in the prime-local setting (global mass; the per-prime version needed for polylog
  quarantines remains open)".

**D5 — LOW (labels).**

* **Location.** The labels at three places:
  * §7, l. 646: "is now refuted unconditionally for every `A<2`";
  * AGENT_REPORT l. 68: "**Theorem 6.2 (PROVED):**";
  * AGENT_REPORT ledger "(F). `H_MOD(A)` is refuted for `A<2`".
* **Problem.** All of these are PROVED modulo the TZ citation (plus D1). "Unconditionally" is
  defensible only in the sense "no GRH/Siegel hypothesis", and should say so.
* **Fix.** Use "refuted for every `A<2` (PROVED modulo TZ Cor. 1.4; no GRH, no Siegel caveat)" and
  "Theorem 6.2 (PROVED modulo Thm 3.1)".

**D6 — LOW (inherited qualification dropped).**

* **Location.** §7, l. 655, "Upper side (notes §51, Thm 51.2(1)) …".
* **Problem.** Notes Thm 51.2(1) "inherit[s] the campaign's provisional-review qualification on
  the Section 39 moment and Bonferroni machinery". The bracketing sentence states it without that
  qualification.
* **Fix.** Append "(with notes Thm 51.2's provisional-review qualification)".

**D7 — COSMETIC.**

* **Location.** The §2 EVIDENCE table, column "Lemma 2.3 majorant" (440, 1066, 2195, 4044).
* **Problem.** `pointwise_omega_S.py` evaluates `(4/3)(3+log T)Σ…` with `X=⌊T/4⌋+1`. The
  displayed majorant has `(3+log X)`, `X=(T+1)/4`, which gives 377.7, 944.8, 1985.0, 3710.7.
  Both dominate S.
* **Fix.** Relabel the column as "(slightly weakened) Lemma 2.3 majorant" or recompute it.

**D8 — LOW (EVIDENCE does not instantiate the theorem; add a sentence).**

* **Location.** §2 EVIDENCE ("with `y=√T`") and §5.
* **Problem.** The EVIDENCE regime differs from the theorem's regime in two ways.
  * The theorem's `y=√T·exp(3𝓛/log𝓛)` is `≥T` unless `log T>e^6≈403`. Below that, U is empty and
    the construction is just the class of one. It gives `y<T^{0.9}` only for `log T>1808`.
  * At the EVIDENCE parameter `y=√T` we have `g_max=0.08–0.33>1/16`, and the twist condition
    actually fails (r=1 ratio 0.267 at T=10⁴, §3.3 above).
* **Status of the theorem.** Nothing is wrong with the asymptotic theorem, and "effective" stays
  true. But the numerics illustrate S only. They do not illustrate the hypotheses of Thm 5.1.
* **Fix.** Say so explicitly. Optionally note that any constant `>log 2` in place of 3 suffices
  asymptotically (`>1.07` with Nicolas–Robin, effectively).

**D9 — COSMETIC.**

* **Location.** §6.3, l. 597: "between 51% and 65%".
* **Problem.** T=10⁴, θ=0.45 gives 50.8%.
* **Fix.** Write "≈51%–65%".

**D10 — NIT.**

* **Location.** Thm 6.2: "Suppose the polylogarithmic version holds … Then
  `W(p) > exp(c(log p)^{1/(2A)})`".
* **Problem.** After adjoining `ℓ_0`, `log Z` includes `log 2T`. So for `A<1` the bound would be
  `(log T)^{A+1}`, not `(log T)^{2A}`. However, `A≥1` is forced: if a prime `ℓ≡3 (4)` near T
  divided neither Q nor any `d_i`, then B would be periodic mod a modulus coprime to ℓ. It would
  then be `≤0` everywhere, since it must be ≤0 on `n≡−4 (ℓ)`, so `μ≤0`.
* **Fix.** Add "(necessarily `A≥1`)".

**D11 — NIT.**

* **Location.** §0 l. 32.
* **Quote.** "the least hard prime with `W>T` satisfies `log L_h(T)…` (notes (58.2))".
* **Problem.** In (58.2) `L_h` means `p≡1 (24)`, not Mordell-hard. The bound holds for both,
  since `p≡1 (840)`.
* **Fix.** Adjust the wording.

**D12 — LOW (label).**

* **Location.** §6.1, l. 510.
* **Quote.** "If the quarantine class is some `c≠1` … the bound `p>∏_Πℓ` is then replaced by the
  requirement `log x≥12 log Z` of every transfer through Theorem 3.1 or Linnik-range PNT."
* **Problem.** This is a statement about a method, not a proved ceiling.
* **Fix.** Label it **Assessment**. In §0 4(a), keep "class-of-one" explicit, as it already is.

## 7. Notes for the parent (not defects of the branch)

* **Ledger text that becomes stale on merge.**
  * notes §51 wave-20 pointer ("exactly the exponents `A≥1` remain open");
  * notes Cor. 54.2 ("remaining open pointwise exponent range is exactly `A≥1`");
  * DISCOVERIES (F)10 ("exact remaining frontier is `A≥1`") and (H)6;
  * STATUS l. 78;
  * POINTWISE_SIZE §7.3 ("Nothing superlinear is proved"), §11.3's title and Assessment 11.6, and
    §12's §58 bullet.
* **Not reviewed.** §8 (Type-I frame) and §9 (Haar side) of `1dd87a3` are not reviewed. That
  includes Thm 8.5 (modulo Lau–Wu) and Thm 9.3 (`T^{1/3+o(1)}`, unconditional). They need a
  separate hostile pass before entering the ledger.

## Replay

```
export PYTHONPATH=scripts
R="uv run python"
(ulimit -v 8000000
 for T in 1000 10000 100000; do $R scripts/review_omega_S.py $T; done   # ~1 min; 1e5 ~4 min
 $R scripts/review_omega_S.py 1000000                                 # ~40 min -> data/review_omega/S_1e6.txt
 $R scripts/review_omega_local.py 1000 20000 1000 7                   # 3 s
 $R scripts/review_omega_local.py 4095 20000 500 11                   # 20 s
 $R scripts/review_omega_bonf.py --no-part3                           # ~9 min (parts 1-2)
 $R scripts/review_omega_bonf.py 10000                                # +13 min (part 3)
 for th in 0.3 0.4 0.45; do $R scripts/review_omega_pairs.py 10000 $th; done
 $R scripts/review_omega_pairs.py 100000 0.4                          # ~5 min
 $R scripts/review_omega_primes.py 1000 5                             # <1 s
 $R scripts/review_omega_constants.py)                                # <5 s
```

---

# Round 2: checkpoint 2 (§8 Type-I frame, §9 Haar side) and the status of D1–D12

## What was reviewed

* **Subject.** `POINTWISE_OMEGA.md` §§8–9 and §0 item 5, plus the checkpoint-2 part of
  `AGENT_REPORT_C2.md`.
  * Head `1dd87a3` holds the checkpoint-2 material.
  * The repair commit `c13e7a0` ("review repairs D1–D12") leaves §§8–9 untouched.
  * My worktree is synced to `c13e7a0`, including its `POINTWISE_SIZE.md` edits.
* **Sources read.**
  * notes (36.1), (44.2), Thm 48.1, (48.7)–(48.12), Thm 50.1, Thm 54.3, Thm 56.2.
  * Lau–Wu, archived author PDF/txt: §1, §4 (Lemmas 4.1–4.3), and §5 (the definition of `P_y`,
    Prop 5.1 and its proof through (5.10)).
  * Elsholtz–Tao arXiv:1107.1010 (`sources/elsholtz-tao-1107.1010.pdf`), Prop 1.4 and Remark 1.5.
* **Code.** Independent code in `scripts/review_omega_typeI.py` and
  `scripts/review_omega_haar.py`, with output in `data/review_omega/{typeI_30000,haar_*}.txt`.
  Nothing is imported from `pointwise_omega_*` or `verify.py`.

## Verdict (round 2): **SOUND-AFTER-REPAIRS** (all items mathematically sound; minor label repairs)

| Item | Verdict |
|---|---|
| Lemma 8.1 (`ck_min ≥ n_p`) | **SOUND** |
| Cor 8.2 (joint `W≥(log p)^{2−o(1)}`, `ck_min≥(log p)^{1−o(1)}`) | **SOUND** (modulo Thm 3.1) |
| Prop 8.3 (complete Type-I certificate forces `ℓ\|L` and `(a/ℓ)=1`) | **SOUND** |
| Cor 8.4 (congruence route certifies exactly `n_p`) | **SOUND** (scope nit R2-3) |
| Thm 8.5 (`ck_min ≫ log p·log₃p` i.o.) | **SOUND modulo Lau–Wu Prop 5.1**. The statement was read and the application is correct; the primes are Mordell-hard. |
| Lemma 9.1 (`m≤r²+1`, parametrisation) | **SOUND** |
| Lemma 9.2 (global mass) | **SOUND**. The divisor-bound form is PROVED; the polylog form holds modulo ET Prop 1.4, with k=4 inside ET's range. |
| Thm 9.3 (`log(1/δ*)≤T^{1/3+o(1)}`, unconditional) | **SOUND** (asymptotic; no numerical instance, see R2-7) |
| Thm 9.4 (H_PP ⇒ polylog) | **SOUND-AFTER-REPAIRS** (label must mention ET: R2-1) |
| D1–D12 | 11 FIXED, 1 PARTIAL (D5; see the table at the end) |

## R2.1 §8: the Type-I frame

### Lemma 8.1

Re-derived.

* Take `(c,k)∈𝓑_p` with `ck≤B`. Then `s=sf(c)≤B`.
* `Δ_s∈{−s,−4s}`, so `χ_s(p)=(−s/p)=(−1/p)∏_{q|s}(q/p)`.
* Each factor is 1:
  * `(−1/p)=(2/p)=1` from `p≡1 (8)`;
  * `(3/p)=(p/3)=1` from `p≡1 (12)`;
  * the primes `5≤q≤B` by hypothesis.
* Notes Thm 48.1 (whose hypotheses are exactly `p≡1 (24)` and `(c,k)∈𝓑_p`) then gives `M_{c,k}=0`.
* For `ck_min≥n_p`, take `B=n_p−1`. This is fine even when `n_p−1<5`, since unforced slices
  have `c≥5`.

**EVIDENCE.** My own `ck_min`, written directly from (36.1)/(44.2)/(48.9) with divisor
enumeration, matches the doc.

* Across the 385 primes `p≡1 (24)` below 30000: 0 violations of `ck_min≥n_p`, and 238 equalities.
* The strict records come out exactly as notes (48.12): `(73,7)…(12289,77)`.
* The example `p=193`, `(c,k)=(26,2)`: `N=3⁵·5·31`, `h=208`, `−p≡15`. The hitting divisors are
  {15, 2511} and no prime power hits, as stated.

### Cor 8.2

* The primes of Thm 5.1 are `≡1 (mod ℓ)` for every `ℓ≤y`. So `(p/ℓ)=1`, hence `(ℓ/p)=1` by
  reciprocity (`p≡1 (4)`).
* Lemma 8.1 then gives `ck_min>y`.
* `y/log p ≥ e^{−(log 2+o(1))𝓛/log𝓛}`, with the constant `C_2` absorbed. Also
  `𝓛 = (2+o(1))log log p`: the upper bound is `log p ≥ log Q ≫ √T`, the lower bound is
  `log p ≤ T^{1/2+o(1)}`.
* Correct; the label is PROVED modulo Thm 3.1.

### Prop 8.3

Re-derived step by step.

* **Step 1.** `gcd(L,4ℓ)` is 4 if `ℓ∤L`, and `4ℓ` otherwise (`24|L`). So `c_0` exists in both
  branches of the contrapositive.
* **Step 2.** `χ_ℓ(n)=(n/ℓ)` for `n≡1 (4)`. This holds in both cases `Δ_ℓ=−ℓ` and `Δ_ℓ=−4ℓ`.
* **Step 3.** `χ_ℓ(−1)=−1` because `Δ_ℓ<0`. So `χ_ℓ(q)=1`, i.e. `−ℓ` is a square mod q. Also
  `q≠ℓ` and `q∤L`, which is possible by choosing q large.
* **Step 4.** CRT compatibility holds on `gcd(L,4ℓ)`. Moreover `ρ≢0`, so the class is reduced.
* **Step 5.** `q | p²+4ℓ = N_{ℓ,1}` and `q≡−c_0≡−p (mod 4ℓ=h)`. So the coefficient of grade `−p`
  in (44.2) is `≥1`.
* **Admissibility.** `(ℓ,1)∈𝓑_p` holds for `p>2ℓ`, and `sf(ℓ)=ℓ≥5`.

**Machine check.** I ran the construction on four instances, covering both branches (`ℓ∤L`, and
`ℓ|L` with `(a/ℓ)=−1`):

| ℓ | L | a | `c_0` | q | ρ |
|---|---|---|---|---|---|
| 5 | 168 | 1 | 13 | 47 | 11 |
| 7 | 120 | 1 | 5 | 23 | 8 |
| 13 | 312 | 73 | 21 | 31 | 14 |
| 11 | 1320 | 241 | 21 | 23 | 5 |

In every instance, the first 20 primes of the constructed class all have `M_{ℓ,1}(p)>0` (0
failures).

### Cor 8.4

* B is periodic mod `L=lcm(Q,d_i)`. A large prime p has `p∤L`, so `a=p mod L` is reduced.
* `24|Q|L` and `a≡1 (Q)`, so `a≡1 (24)`.
* Prop 8.3 then gives `(a/ℓ)=(p/ℓ)=(ℓ/p)=1` for `5≤ℓ≤T`, so `n_p>T`. Correct.
* The proof never uses `a≡1 (Q)` beyond `a≡1 (24)`, so it holds for every class with `a≡1 (24)`.
  The §8 rhetoric ("every congruence method") is therefore justified once that is said (R2-3).
* Conversely, Lemma 8.1 *is* a fixed-period certificate: the QR conditions mod `∏_{ℓ≤T}ℓ`. So
  "exactly `n_p`" is right.

### Thm 8.5 and Lau–Wu Prop 5.1

* **The statement**, read in `lau-wu-least-quadratic-nonresidue.txt` ll. 378–405:
  * **Definitions.** "In this section, we denote by p and q prime numbers.
    `P_y:={p : p≡1 (mod 4) and χ_p(q)=1 for all q≤y}`."
  * **Hypotheses.** Let δ>0 be a fixed small constant, and let y(x) be strictly increasing on
    `[120,∞)` with `(log x)e^{−δ(log₂x)^{1/2}} ≤ y(x) ≤ δ(log x)log₃x`.
  * **Conclusion.** There are `c=c(δ)>0` and `x_n→∞` such that
    `Σ_{x_n^{1/2}<p≤x_n log x_n, p∈P_{y(x_n)}} 1 ≫ x_n e^{−c y(x_n)/log y(x_n)}`.

  The doc's quotation is accurate.
* **Meaning of `χ_p`.** Here `χ_p=(p/·)_K`, the Kronecker symbol of the fundamental discriminant
  `p` (`p≡1 (4)`).
  * For odd q, `χ_p(q)=(p/q)=(q/p)`.
  * For `q=2`, LW themselves note `χ_p(2)=(2/p)` (l. 435ff.).

  So the doc's gloss "`χ_p(q)=(q/p)`" is correct.
* **The application.**
  * `y(x)=δ log x log₃ x` is the allowed upper end. It is strictly increasing on `[120,∞)`, since
    `log₃120=0.449>0`.
  * The count `x_n^{1−O(δ log₃x_n/log₂x_n)}` is eventually ≥1, so `P_{y(x_n)}` meets the interval.
* **Hardness.**
  * `(2/p)=1` and `p≡1 (4)` give `p≡1 (8)`.
  * `(3/p)=1` gives `p≡1 (3)`.
  * `(5/p)=(7/p)=1` give `(p/5)=(p/7)=1`.
  * So `p mod 840` is a unit square: one of the 6 Mordell classes `{1,121,169,289,361,529}`, all
    `≡1 (24)`. Lemma 8.1 applies with `B=y(x_n)`.
* **Size.** `log p ≤ log x_n + log log x_n` gives `y(x_n) ≥ (δ/2)log p·log₃p` for large n.
* **Effectivity.** Not claimed, which is correct: the sequence `x_n` comes from LW Lemma 4.2,
  which uses Maier's argument to avoid exceptional zeros.
* **Label.** "PROVED modulo Lau–Wu Prop 5.1", with the proof following Graham–Ringrose and not
  checked, is right. Bibliographic data are missing (R2-5).

## R2.2 §9: the Haar side

### Lemma 9.1

* **The bound `m≤r²+1`.** The involution argument needs only `m | M=4A−1`, so `4A≡1 (m)`. Then
  `m|r'+k≤2k`, so `r≥2sr'−1/(2k)`, hence `r≥2sr'`. So
  `m ≤ 4sr'²+1 ≤ 4(sr')²+1 ≤ r²+1`.
* **The parametrisation.** Algebra re-derived:
  * `m(vk−ℓr')=r'+k`, `e(mv−1)=r'(ℓ+v)`, `e=(ℓ+v)/(4sr')`;
  * conversely `srk = (mℓ+mv−4nr')/4 = (mℓ+1)/4`. So `mℓ≡3 (4)` is automatic, but harmless.
* **The partner class.** `−4A²/D = −(4A)²/(4D) ≡ −(4D)^{−1} (mod ℓ)`.

**Checks.**

* **Parametrisation.** It agrees with direct enumeration of all `(m,D)` with `m≤ℓ²+1`,
  `D≤A`, `m|4D+1`, for every prime `5≤ℓ<200` (0 mismatches).
* **`m≤r²+1`.** No surviving atom violates it, over all z tested:
  * T=10⁴: z = 20, 100;
  * T=2·10⁴: z = 150;
  * T=10⁵: z = 5, 20, 100, 300, 1000 (0.31–0.81·10⁶ atoms);
  * T=10⁶: z = 1000, 3000 (3.8·10⁶ atoms).
* **Examples.**
  * `F^{full}_{19}={8,12,14,15,18}`.
  * The `19³` example is reproduced: `A=1715=5·7³`, `D=7`, class 10 mod 19.
  * `87359` is prime, `(ℓ+1)/4=2⁴·3·5·7·13` and `τ(A²)=729`. Also `ℓw_ℓ=681.0` at
    `(T,z)=(10⁵,100)`.

### Lemma 9.2

* **The weight.** `1/φ(r) ≤ C log log T/r` holds for every `r≤T`; the "prime factors >z" remark
  is not needed (R2-4).
* **Halving.** The involution preserves `m|4D+1`.
* **Injectivity.** The injection into `(m,s,r',k)` overcounts by summing over all
  `m|4sr'²+1`, which is harmless for an upper bound.
* **The k-sum.** `m|r'+k` and `k_0≥m/2` give `(3+log X)/m`.
* **Elsholtz–Tao Prop 1.4** (pdf p. 3): "For any `A,B>1`, and any positive integer
  `k≪(AB)^{O(1)}`, one has `ΣΣ_{a≤A,b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)`."
  * Here `k=4` is fixed, and the dyadic blocks have `A=2S`, `B=2R≥2>1`, so the hypotheses hold.
    Restricting to squarefree a only drops nonnegative terms.
  * Each block gives `O(log T)`. There are `O((log T)²)` blocks, so the total is
    `≪(log T)^4 log log T`.

**EVIDENCE matches.**

* `(T,z)=(2·10⁴,150)`: `S_tot=19.39`, `S_ev=16.16`.
* T=10⁵: `S_ev=49.65, 39.20, 29.81, 24.22, 17.87` for `z=5…1000`.
* T=10⁶: `S_ev=38.49, 30.55`.
* The proof's chain bound `(2/3)max(r/φ(r))(3+log X)Στ/(sr')` dominates `S_tot` in every case.

### Theorem 9.3

This is the delicate part. Every step was re-derived.

1. **Structure.** `y³>T`, so z-rough parts are `ℓ`, `ℓ²` or `ℓ_1ℓ_2`.
   * Single atoms are events on one coordinate `X_ℓ=n mod ℓ^{e_ℓ}`.
   * `g_ℓ ≤ Σ1/φ(r)` holds, since an `r=ℓ` atom removes `ℓ^{e−1}` of the `φ(ℓ^e)` units.
   * `1∉G_ℓ`: `−4D≡1 (mod ℓ or ℓ²)` together with `m|4D+1` gives `M|4D+1`, contradicting Fact 1.1.
2. **Bad primes.** `|B| ≤ 4Σg_ℓ ≤ 4S_tot = T^{o(1)}`. This uses only the divisor-bound form of
   Lemma 9.2, *not* ET, so Thm 9.3 is unconditional as labelled.
   * Quarantining b at `n≡1 (b^{e_b})` costs `≤ log φ(b^{e_b}) ≤ log T` each.
   * Since `1∉G_b`, all single atoms at b die.
   * A pair with both primes bad dies by Fact 1.1.
   * A pair `(ℓb,a)` with ℓ good becomes `X_ℓ≡a (ℓ)` exactly when `a≡1 (b)`, and is impossible
     otherwise.
   * **The count.** At most `|B|·(T/(ℓy))·τ²_max` such atoms involve a given ℓ, each of weight
     `1/(ℓ−1)`. So `g'_ℓ−g_ℓ ≤ T^{−3ε+o(1)}`, and the total added mass is
     `≤|B|τ²T/y² = T^{1/3−2ε+o(1)}`. Correct.
3. **The local lemma.**
   * **The measure.** μ′ is the product of uniform measures on the allowed units at each good
     prime. This is exactly Haar conditioned on avoiding the single sets: a product set in a
     product space.
   * **The dependency graph.** A pair event depends only on `(X_{ℓ_1} mod ℓ_1, X_{ℓ_2} mod ℓ_2)`.
     It is therefore mutually independent of all events that share no prime with it, so "join if
     they share a prime" is a valid dependency graph.
   * **Event sizes.** `μ'(E) ≤ ∏ 1/((ℓ_i−1)(1−g'_{ℓ_i})) ≤ 4/((ℓ_1−1)(ℓ_2−1))`.
   * **Per-prime weight.**
     `w'_ℓ ≤ (8T/ℓ²)τ²Σ_{ℓ'>y}1/(ℓ'(ℓ'−1)) ≤ 16τ²T/(ℓ²y) ≤ T^{−3ε+o(1)}`.
   * **The LLL condition.** It needs `∏_{E'∼E}(1−2μ'(E')) ≥ 1/2`. Since
     `Σ_{E'∼E}x_{E'} ≤ 2(w'_{ℓ_1}+w'_{ℓ_2}) → 0`, this holds for large T.
   * **The conclusion.** `∏(1−x_E) ≥ exp(−4Σμ'(E)) ≥ exp(−16S_tot)`.
4. **Collecting.**
   * The conditioning costs `8/φ(Q')`, with `log φ(Q') ≤ (π(y)+|B|)log T`.
   * The single sets cost `∏(1−g'_ℓ) ≥ exp(−2Σg'_ℓ)`, valid since `g'≤1/2`.
   * Total: `exp(−T^{1/3+ε+o(1)})`. Correct.

**Numerics** (`review_omega_haar.py --theta 0.05`, with `y=T^{0.383}`).

* The structural claims hold literally:
  * 0 rough parts with more than 2 prime factors;
  * `1∈G_ℓ` at 0 primes;
  * pairs that are impossible or converted after the bad-prime quarantine behave as described.
    At T=10⁴ there are 3 bad primes, 2146 impossible pairs and 34 converted pairs.
* `max g'_ℓ = 0.23`.
* The LLL product is ≈0.34<1/2 at T=10⁴ and T=10⁵, so the asymptotic condition is not met at
  accessible T. That is expected, since the margin is `T^{−3ε}`. So Theorem 9.3 has no numerical
  instance (R2-7, remark only).

### Theorem 9.4

* **The setup.** `x_E=2/φ(r_E)≤1/2` holds since every rough prime is `≥5` (`z≥3`).
* **The LLL condition.** `Σ_{E'∼E}x_{E'} ≤ 2Σ_{ℓ|r_E}w_ℓ`, and `ω(r_E) ≤ log T/log z`. Under
  H_PP this gives `∏ ≥ e^{−1/2} ≥ 1/2`.
* **The conclusion.** `P ≥ exp(−4S_ev)`. Correct.
* **The label.** The polylogarithmic conclusions use ET's `(log T)^4 log log T`. Without ET,
  `S_tot` is only `exp(O(log T/log log T))` and nothing polylogarithmic follows (R2-1).
* **A finite certificate.** H_PP holds literally at `(T,z)=(10⁵,1000)` (ratio 0.961) and
  `(10⁶,3000)` (ratio 0.810), as in the doc. My literal check of the LLL hypothesis on the event
  graph gives `min_E ∏_{E'∼E}(1−x_{E'}) ≥ 0.75` and `0.79` respectively. So Thm 9.4 yields a
  rigorous finite-T certificate there; a pleasant side remark the author could add.
* **The Linnik remark** ("`ℓw_ℓ` is not polylogarithmic for all ℓ") is correct.
  * `P|A` gives `|𝓡(ℓ)| ≥ #{D≤A : D|A²} = (τ(A²)+1)/2 ≥ 3^K/2`, because the classes `−4D`,
    `D≤A<ℓ`, are distinct mod ℓ.
  * Linnik gives `log ℓ ≪ K log K`.

## R2.3 Defect list (round 2)

**R2-1 — LOW (label).**

* **Location.** Thm 9.4 heading "(PROVED implication; Haar only)", and §0 item 5 ("follows from
  the per-prime Hypothesis H_PP (Theorem 9.4, PROVED implication)").
* **Problem.** The explicit bound `−O((log T)^4 log log T)`, and with it the whole polylogarithmic
  conclusion, needs Elsholtz–Tao Prop 1.4. Without ET it fails, since `S_tot` is only `T^{o(1)}`.
* **Fix.** Use "PROVED implication, modulo Elsholtz–Tao Prop. 1.4 for the polylogarithmic mass
  (Lemma 9.2)" in both places, and in the AGENT_REPORT table.

**R2-2 — LOW (overstatement).**

* **Location.** AGENT_REPORT checkpoint 2, l. 189.
* **Quote.** "On the prime side, the same construction is exactly H_MIN(1/3); it would give
  exponent 3, but it is blocked by the hub obstruction of §6.3."
* **Problem.** Prop 6.3 proves only that *event-level Bonferroni on the raw atom list* fails.
  §6.3 itself says that deduplicated or other minorants are not ruled out. H_MIN(1/3) is open, not
  blocked. The doc's own sentence (§9 end) is accurate.
* **Fix.** Write "…blocked for event-level Bonferroni (Prop 6.3); H_MIN(1/3) itself is open".

**R2-3 — NIT (scope).**

* **Location.** Cor 8.4 is stated for minorants on the class `1 mod Q`. The §8 text claims "Every
  congruence method for `ck_min` is exactly the least-quadratic-non-residue Ω-problem".
* **Fix.** Add "(the proof uses only `a≡1 (24)`; it holds verbatim for minorants on any reduced
  class `a mod Q` with `a≡1 (24)`, which contains all hard primes)".

**R2-4 — COSMETIC.**

* **Location.** Lemma 9.2 proof: "Since r has all prime factors `>z≥2`,
  `1/φ(r) ≤ C log log T/r`".
* **Problem.** The bound holds for every `r≤T`; the premise is irrelevant.
* **Fix.** Drop the premise or replace it with "for every `r≤T`".

**R2-5 — NIT (citation data).**

* **Location.** Thm 8.5's citation gives only "author PDF". Please add the journal data if
  published. I believe it is Int. J. Number Theory 4 (2008), but did not verify this.
* The archived PDF's sha256 matches `sources/lit2026/README.md`; I checked only the pointer there.

**R2-6 — NIT (D5 residue).**

* **Location.** AGENT_REPORT_C2.md title: "unconditional superlinear Ω-result for W(p)".
* **Fix.** Use "superlinear Ω-result … (PROVED modulo TZ Cor. 1.4)".

**R2-7 — REMARK (no defect).**

* Theorem 9.3 is purely asymptotic: its LLL margin `T^{−3ε}` is not reached at `T≤10⁵`.
* Conversely, Theorem 9.4's hypothesis H_PP holds literally at `(10⁵,1000)` and `(10⁶,3000)`.
  This gives rigorous finite-T Haar lower bounds there. Optionally state it as EVIDENCE.

## R2.4 Status of round-1 defects at `c13e7a0`

| # | Status | Where / how |
|---|---|---|
| D1 | **FIXED** | §0 "one cited source (TZ Cor. 1.4 together with the McCurley-region statement…)". There is a Convention paragraph after Thm 3.1, Lemma 3.2 is relabelled "PROVED modulo the McCurley-region statement quoted by TZ", and a Landau–Page alternative remark is added. AGENT_REPORT l.15 is updated. |
| D2 | **FIXED** | Thm 3.1 heading: "statement and numbering as in arXiv v2, published version not compared". |
| D3 | **FIXED** | The §6.2 sentence now reads "known for `θ≥1/2` (Lemma 11.7) and for `θ>1/3` (Theorem 9.3) … open (§9, H_PP)". The `θ>1/3` claim is verified in R2.2 above. |
| D4 | **FIXED** | §0 item 2: "in the prime-local setting (global mass). The per-prime version … remains open (§9, H_PP)". |
| D5 | **PARTIAL** | Fixed in §7 ("PROVED modulo Theorem 3.1: no GRH, no Siegel caveat"), at AGENT_REPORT l.68 (Thm 6.2) and in ledger (F). The AGENT_REPORT title still says "unconditional" (R2-6). |
| D6 | **FIXED** | §7 upper-side bullet now carries Thm 51.2's provisional-review qualification. |
| D7 | **FIXED** | The column is relabelled "slightly weakened Lemma 2.3 majorant¹", with a footnote giving the exact values. |
| D8 | **FIXED** | New paragraph "Scope of this EVIDENCE (reviewer D8)", with all points included. |
| D9 | **FIXED** | "≈51%–65%". |
| D10 | **FIXED** | "(necessarily `A≥1`)". |
| D11 | **FIXED** | "the least prime `p≡1 (24)` with `W>T` (notes (58.2)'s `L_h`; the primes produced are also Mordell-hard)". |
| D12 | **FIXED** | It is now "*Assessment (a statement about methods, not a proved ceiling).*" |

**The `POINTWISE_SIZE.md` edits in `c13e7a0`** are accurate and correctly labelled. They are the
dated update notes in §7.3 Assessment 7.2, "What would make 7.2 rigorous", the §11.3 title,
Assessment 11.6, and §12's Lemma 58.5 bullet. One of them checks out explicitly: "`log(1/V) ≤ 2S ≤
T^{o(1)}`" is true under the theorem's parameter (`g≤1/16`).

**Still for the parent at merge (round-1 §7):** notes §51 pointer, Cor. 54.2, DISCOVERIES (F)10 and
(H)6, STATUS l.78. Also any new ledger entries for §§8–9: they should carry the labels above, with
the ET qualification for Lemma 9.2's polylog form and Thm 9.4 (R2-1).

## Replay (round 2)

```
export PYTHONPATH=scripts
(ulimit -v 8000000
 uv run python scripts/review_omega_typeI.py 30000                          # <5 s
 uv run python scripts/review_omega_haar.py 10000 --extras 20 100 --theta 0.05   # ~3 s
 uv run python scripts/review_omega_haar.py 20000 150                       # ~2 s
 uv run python scripts/review_omega_haar.py 100000 5 20 100 300 1000 --theta 0.05  # ~10 s
 uv run python scripts/review_omega_haar.py 1000000 1000 3000)             # ~4 min, ~3 GB
```
