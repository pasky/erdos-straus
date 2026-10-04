# Hostile review: POINTWISE_WINDOW.md (branch side-agent/window-omega @ fba65aa)

Reviewer: side-agent/review-window. Scope: POINTWISE_WINDOW.md, AGENT_REPORT_O10.md,
scripts/window_{w1,joint}.py, data/pointwise_window/, sources/sieve/.
Verdict per item; numbered defects at the end (D1, D2, …).

## Items

### 1. Window-3 reduction, Lemma 1.1, Lemma 1.2 — CORRECT

* q=3, p≡1 (3): both targets coincide, `−1≡−p≡2 (mod 3)`. `Rat_3(n)∋2` iff some
  prime factor of n is ≡2 (3) (if all factors ≡1, every u/v≡1; a factor r≡2 gives
  u=r, v=1). `x_3=(p+3)/4<p`, so `p∤x_3`; `gcd(x_3,3)=gcd(x_3,p)=1`. So window 3
  fails iff `n_3` has no factor ≡2 (3), and since 3 is the smallest q≡3 (4),
  `a_min≥7` follows. Both targets checked.
* Lemma 1.1 (F1 ⇒ fail): via Lemma 8.2 (needs p≡1 (8), q<3p; both hold) and
  Cor 8.3(a); Jacobi symbol is a character on `Rat_q`, `(−1/q)=−1`,
  `(−p/q)=−(x/q)=−1`. Correct.
* Lemma 1.2: `(n_q/q)=∏(r/q)^{v_r}`, `4n_q≡p (q)`, `(4/q)=1`. Correct (r=2
  counted as bad when `(2/q)=−1`; harmless since `n_3` is odd).
* "Hard": `1 mod 840` is one of Mordell's six classes {1,121,169,289,361,529};
  POINTWISE_SIZE §11 uses "hard" = Mordell-hard. Correct.

### 2. Theorem W1 proof (§2.2) — CORRECT (modulo S1–S3, as labelled)

Checked line by line:
* Sifting data: `n_p=210k+1`, so 2,3,5,7 ∤ n; `g(2)=g(5)=0` is legitimate;
  `d|n_p ⟺ p≡−3 (d)` is one reduced class mod `840d`; `φ(840d)=192φ(d)`.
* Dimension: `(1−1/ℓ)(1−(ℓ−1)^{−2})=(ℓ−2)/(ℓ−1)=1−g(ℓ)` — verified algebraically.
* Remainder: moduli `840d≤x^{1/2}(log x)^{−B}`, distinct per d; BV applies.
* `f(s)≥(e^γ/π)^{1/2}(s−1)^{1/2}` on `[1,2]`: verified (`t(t−1)≤2(t−1)`).
* Step 2: `k<1/(1/2−ε)≤2.22`, parity ⇒ k∈{0,2}. Correct.
* Step 4: `a/φ(a)·y=(x+3)/φ(4mr_1)=(x+3)/(2φ(m)(r_1−1))` (m odd, coprime to r_1,
  because all its primes are ≡1 (3)) ⇒ the stated `9C_0x/(log x)^2/(φ(m)(r_1−1))`.
  `Σ_{k≥1}1/φ(ℓ^k)=ℓ/(ℓ−1)^2` and `1+ℓ/(ℓ−1)^2 ≤ (1−1/ℓ)^{−1}(1+(ℓ−1)^{−2})`
  verified. The r_1-sum is over primes ≡2 (3) only, so the true size is ≈ε, and
  3ε is a safe overestimate. `C_3=27√2C_0C_2` checks.
* S2 is fine: the Selberg remainders are `≤ω(d)`, independent of a, so it is
  uniform for `a≫y`. (HR Thm 3.12 is the right family; the doc re-derives it anyway.)
* Step 5: c_1 is ε-independent (V(z) with `1/2−ε∈[0.45,0.5]`), so the
  `ε^{1/2}` vs `ε^{3/2}` choice of ε works.
* S1 citation: Teräväinen (archived, line 1446) cites exactly "[Opera de Cribro,
  Theorem 11.13], with β=1" for the semilinear sieve, with the same `f(s)`. The
  primary is not read, and the doc says so honestly. See D3 for the
  ch.14-vs-Thm-11.13 inconsistency with POINTWISE_SIZE Prop 11.4.

No mathematical gap found. Prop 11.4 → PROVED modulo S1–S3 is justified.

### 3. FHRSS cross-citation (§2.3) — CORRECT; hypotheses checked literally

Archived `2504.20289.txt` lines 34–49, Thm 1.1. With `f=x²+xy+y²`, `B=4`, `A=−3`,
`m=35`, `l=1`:
* f is primitive (gcd(1,1,1)=1); `D=−3` is not a square; f is positive definite;
  `(a,2D)=(1,6)=1`.
* `A≠0`; `gcd(A,B)=gcd(−3,4)=1`. `D=−3≡5 (8)`, so the alternative `2|AB` is
  needed, and `AB=−12` is even. ✓
* `gcd(l,m)=1`; `gcd(m,2DB)=gcd(35,24)=1`; `gcd(l−A,m)=gcd(4,35)=1`. ✓
* "Primitively represented by Bf+A" means `p=4f(x,y)−3` with `gcd(x,y)=1`. The
  doc's deduction is right: primes ≡2 (3), including 2, are inert in Z[ω], so a
  primitive value has none of them. `n≡(x−y)² (3)` and `3∤n` give `p≡1 (24)`.
  With `p≡1 (35)` this gives `p≡1 (840)`. FHRSS counts *primes*, so the lower
  bound transfers. (Since h(−3)=1 the two sets actually coincide.)
* Nit: "Their proof is Iwaniec's 1972 argument, i.e. the same S1–S3 route" is
  loose. FHRSS §1.4 says the sieve gives a genus-level count, and then [BF12]
  (Bourgain–Fuchs) is applied to pass to a single form. For D=−3 that step is
  vacuous (one class), so the nit is harmless (D5).
* FHRSS is an arXiv preprint (Apr 2025); the doc does not record its
  publication status (D5).

### 4. Theorem W2 (§4) — CORRECT as a CONDITIONAL result; literature claim is WRONG (D1)

* Data checked. `n_3=210k+1` and `n_7=210k+2`. 2 is 7-good, `(2/7)=1`. 3 and 5
  are 7-bad but never divide `n_7`. `(p/3)=(p/7)=1` gives even bad counts. The
  classes `−3,−7 mod ℓ` are distinct for ℓ∤4. `(Ω_1)` holds:
  `ω(ℓ)=1[ℓ∈P_3]+1[ℓ∈P_7]` has mean 1.
* Linear-sieve step. `s=(1−ε)/(1/2−ε)=2+2ε/(1−2ε)` and `f(s)=2e^γlog(s−1)/s≥(2/3)e^γε`
  are right. The `2^{ω(d)}`-weighted EH remainder via Cauchy–Schwarz plus
  Brun–Titchmarsh is standard and fine.
* `T^{(q)}` step. Fix `(m,r_1)` and sift `r_2` by `0`, `q/a`, and `(q−q')/a` (the
  last only for q'-bad ℓ). That is dimension 5/2, and the three classes are
  distinct for ℓ∤42. The sifting range `y^{1/10}<z` is compatible with the
  q'-condition the survivors satisfy. `Σ1/r_1·Σ_m(m/φ(m))^3/m ≍ ε·(ε log x)^{1/2}`
  gives `ε^{3/2}x/(log x)^2` against the main term `εx/(log x)^2`. Checked.
* **D1 (literature, substantive for Goal 2/3 framing).** The claims "We know of no
  such result in the literature (… nearest: FHRSS 2025, one form only)" (§0) and
  "The closest known results produce one condition (Iwaniec 1972; FHRSS 2025)"
  (§7.3) miss the direct precedent:
  **Friedlander–Iwaniec, *Hyperbolic prime number theorem*, Acta Math. 202
  (2009) 1–19.** It counts primes p with `p−2` and `p+2` both sums of two
  squares, i.e. two half-dimensional absence conditions on shifted primes. Its
  Thm 2 gives the lower bound `≫x/log x` (weighted) **assuming A(θ) for some
  θ<1 sufficiently close to 1**; the upper bound is unconditional. That is
  exactly W2's shape and exactly the "fixed level 1−ε_0 suffices" remark. Their
  §6–7 also use the semilinear sieve with β=1, then remove two-prime
  configurations. The unconditional lower bound is still open: arXiv:2609.28200
  (2026) restates it as resting on a strong hypothesis. Fix: cite FI09 as the
  model for W2 (W2 is "FI09-type"). Then use it as *evidence* for Assessment
  7.3: unconditional K=11 is the window analogue of a known open problem. This
  strengthens the doc's Goal-2 answer. The novelty wording must change.
  (Reviewer fetched FI09 from archive.ymsc.tsinghua.edu.cn; not archived in repo.)

### 5. Lemma 6.1 and §6 — lemma CORRECT; labels INCONSISTENT (D2)

* Proof checked. `ord(c)≤φ(q)<q`, so `e_c<q` distinct primes per big class are
  available. The chosen primes are distinct across classes, so u is squarefree,
  `u|n_q`, `u≡−1`, and `−1∈Rat_q`. The count `<q·φ(q)` outside K is right.
  Only target −1 is used, which is fine for a necessary condition.
  Reviewer brute force (own Rat_q enumeration, no project code): 2593 failing
  windows `q≤43`, `p≡1 (840)`, `p<10^6`, all satisfy the lemma. At this size
  `C_big=∅` always, so the check is weak.
* **D2 (labels).** §0's table row "Lemma 6.1 | every failing window costs sieve
  dimension ≥1/2; congruence classes cannot lower it | PROVED" contradicts §6.
  There the dimension consequence is explicitly an *Assessment* ("the
  bookkeeping step is not a proved estimate"). The same §6 paragraph then calls
  it "the rigorous form of the 'dimension ≥K/8' bookkeeping". AGENT_REPORT_O10
  repeats "Lemma 6.1 (PROVED) … So each window costs sieve density ≥1/2".
  Fix: the §0 row should read "Lemma 6.1: failing window ⇒ prime factors in a
  subgroup K∌−1 up to <qφ(q) exceptions — PROVED; dimension ≥1/2 —
  Assessment". Drop "rigorous form", and fix the report.
* Missing cross-reference. For a *single prime* window the dimension-1/2 upper
  bound is already a theorem: notes Thm 70.9 (`≪_a N/(log N)^{3/2}` for
  F1∪F3, effective), and DISCOVERIES #23. Only the joint J-window version is
  Assessment. Cite it (D6).
* "Congruence restrictions do not help (PROVED for fixed Q)". The proved content
  is only that the sifting density is unchanged. "Saves nothing in dimension"
  then inherits the Assessment status of the bookkeeping. Minor overlabel (D6).
* §7.3 uses Lemma 6.1 with J unbounded. The exception budget `Σ_q qφ(q)≍J^3`
  is then not O(1), so "(up to O_q(1) exceptions)" and "(log log x)^{O_q(1)}"
  need J-uniformity. That is fine inside an Assessment, but it should be said (D6).

### 6. Prop 7.2 and §7 Assessments — computation CORRECT; attribution of the gain WRONG (D3); labels mostly OK

* Prop 7.2 identity re-derived by hand and checked numerically (s=2,2.3,2.7,3:
  residual ≤2e−13). The ranges are fine: `s(1−α)∈[s/2,s−1]⊂[1,2]`, so
  `F(t)=2e^γ/t` applies. "PROVED (computation)" is acceptable for what it is,
  namely an identity between the sieve functions for this particular one-step
  scheme.
* **D3 (misattribution in §7.2 last paragraph, §7.3 bullet 2, §8 bullet 2, report
  Goal 3).** The text says W2 escapes route B "only because route A uses more
  than the sieve axioms: the parity of the bad count (Lemma 1.2)". But route B
  *as set up in §7.2 already uses Lemma 1.2*. Its Bonferroni step
  `1[clean_q] ≥ 1 − #{q-bad r|n_q: z≤r<√x}` is false for an `n_q` with exactly
  one bad prime `r≥√x`. It holds only because parity excludes that case. So
  parity is common to both routes. The real extra input of route A is the
  `T^{(q)}` bound. For each pair `(m,r_1)` it sifts `r_2` as a *prime*, with `ar_2−q`
  prime and the other window kept, in a dimension-5/2 upper sieve. This saves
  `ε^{1/2}` over the generic `F(s(1−α))` bound on `A_r`. That is a
  switching/structural input, not a parity input. The doc's own last sentence
  ("forces n_q/r to be m·r_2, which the generic bound F(1) does not see") is
  the correct explanation and contradicts the "only because … parity"
  sentence. Fix the wording, and the §7.3 sentence "Route A survives at level x
  only by feeding in the congruence-parity of Lemma 1.2".
* "and is negative at level `x^{1/2}`" (after Prop 7.2) is asserted, not
  computed. Prop 7.2 is only at D=x. Label it Assessment or give the computation
  (D4).
* §7.1 table and β facts. `β_{1/2}=1` and `β_1=2` are optimal (standard). The
  monotonicity argument for `β^{opt}_κ` is correct: `(Ω_{κ'})⇒(Ω_κ)` for κ'≤κ.
  "β_{3/2} near 3 (recalled from memory)" is flagged honestly. The J≥3 row is
  conditional ("impossible if β^{opt}_{3/2}>2"). Labels OK. Small nit: at J=3,
  `s=ϑ/(1/2−ε)` slightly exceeds 2ϑ, so the threshold is "β≤2ϑ/(1−2ε)", as in
  the J=2 row.
* §7.3 "single window: no parity barrier". As an Assessment this is fine, and
  it agrees with FI09 §6–7 (semilinear β=1, then two-prime removal). The §0
  slogan "a single window has **no** parity barrier" should keep the qualifier
  "given the congruence parity of Lemma 1.2". Otherwise it reads as a claim about
  the sieve alone (nit).
* §7.3 literature sentence: see D1 (FI09 is a two-condition result on shifted
  primes, conditional on level <1 close to 1).
