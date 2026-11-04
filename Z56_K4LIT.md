# Z56_K4LIT — literature sweep and judgement for unconditional K(4) = P(4,15)

**ES is OPEN.** Nothing here proves or disproves it. All results are internal and have been internally reviewed only.
Lane K4LIT, wave z56. Scripts: `scripts/z56_k4lit_*`. Data: `data/z56/k4lit/`, containing three literature reports
(their errata are in §9):
* `lit_A_shifts.md`: one and two half-dimensional prime shifts;
* `lit_B_parity.md`: parity, Siegel zeros, levels;
* `lit_C_breakthroughs.md`: parity-breaking and Type II results, 2018–2026.

Notation follows `Z55_P415.md`:
* 𝒬 = {primes ≡ 3 (mod 4)}; S = {n ≥ 1 : every prime factor ≡ 1 (mod 4)};
* N₁ = p + 4, N₂ = 4p + 1; SOTS = "sum of two squares", which is weaker than S;
* Ω_𝒬 = number of 𝒬-prime factors counted with multiplicity;
* f, F = semi-linear (κ = 1/2) lower and upper sieve functions; for 1 ≤ s ≤ 2,
  f(s) = 2(e^γ/πs)^{1/2} arccosh √s and F(s) = 2(e^γ/πs)^{1/2};
* r(n) = #{(a, b) ∈ ℤ² : a² + b² = n}; r*(n) = number of primitive representations.

**P(4,15)**: infinitely many primes p ≡ 1 (mod 8) have p + 4 ∈ S and 4p + 1 ∈ S. By `Z54_HCKILL.md` Lemma 1.1 (PROVED)
this is K(4), "HC(p) > 4 infinitely often".

**Provenance tags for literature items.** Each tag says how a statement was read, not whether its proof was checked:
* [P-me]: primary text read by me (page image or PDF text);
* [P-sub]: primary text read by a research subagent, and re-read by the internal reviewer where noted in
  `internal_review.md`;
* [Sec]: read in a paper that quotes it;
* [Abs]: arXiv abstract only.

Sources dated 2026 are mostly unrefereed arXiv v1 preprints. "Not located" always means "not found in the bounded
searches documented in the reports". No search is claimed to be exhaustive.

---------------------------------------------------------------------------------------------------------------------
## 0. Hot leads and verdict (read this first)

### H1. P(4,15) and its det-1 analogue were not located as unconditional theorems (Assessment, from the map in §2)
* **No source located states P(4,15).** Our own conditional versions are the only ones known to us:
  * EH(θ₀) ⟹ P(4,15), HCKILL Theorem E;
  * Bunyakovsky for 720k² + 1 ⟹ P(4,15), Theorem Q.
* **The exact structural analogue is conditional in its source.** That analogue is primes p with p − 2 and p + 2 both
  SOTS, equivalently prime norms on SL₂(ℤ).
  * **Friedlander–Iwaniec, *Hyperbolic prime number theorem*, Acta Math. 202 (2009).** Theorem 4 [P-me] states
    S(x) = Σ_{n≤x} r(n−2)r(n+2)Λ(n) ≍ x "Under the same assumption as Theorem 2". That assumption is A(θ) "for some
    θ, less than 1 but sufficiently close to 1"; the upper bound is unconditional.
  * **Sedunova, arXiv:2609.28200 (Sept 2026)** [Abs]: "the upper bound is unconditional, while the lower one rests on
    a strong hypothesis concerning the distribution of primes in arithmetic progressions".
  * **Shparlinski–Xiao, arXiv:2609.21460** [Abs, via lit_C]: "conditional on a very strong form of the
    Elliott–Halberstam conjecture".
* **The best unconditional neighbours located:**
  * **Iwaniec 1972, Acta Arith. 21, Thm 1** [P-sub]. S₁ counts proper representations. With A = −4 this gives
    p + 4 ∈ S for ≍ N/(log N)^{3/2} primes p ≤ N.
  * **Nath–Xie, arXiv:2501.16723 v3** ("Final version, published in Acta Arithmetica") [P-me]. Theorem 1.1:
    #{p ≤ x : p = m² + n² + 1, Ω(p + 2) ≤ **9**} ≫ x/(log x)^{5/2}. Version v1 had 11, and `Z55_P415.md` cites v1.
    Remark 1.1 gives Ω ≤ 3 under an EH variant.
  * **Our Theorem U** (`Z55_P415.md`, internal) has the same shape: N₁ ∈ S exactly and Ω_𝒬(N₂) bounded.
  * **Sedunova Thm 2** [P-sub]: a *representation-weighted* count, ≫ x/log x, of squarefree n with ω(n) ≤ 7 and n ± 2
    SOTS. It gives infinitely many distinct such n; the same order for distinct n is not claimed.
  * **Integer analogues:**
    * Indlekofer 1974: B₂(x) ≫ x/log x [P-sub, page image];
    * Hooley 1973/74 [Sec].

### H2. Sieve data plus forced parity: counterexamples below level 1/2, a guarantee above it (Lemma P, Prop P′)
**Literature [P-me].** Iwaniec, *The half dimensional sieve*, Acta Arith. 29 (1976):
* **Theorem 2** treats sequences with odd parts ≡ 1 (mod 4) sifted by primes ≡ 3 (mod 4), where the parity of Ω_𝒬 is
  fixed by the congruence. The *upper* bound's main term becomes the main term of an asymptotic. Its relative error is
  O(e^{4K−s}((L + log Q)/log A)^γ), with remainders over d < A/Q, i.e. level ≈ (max element)·Q⁻¹.
* **Cor. 2 (2.1)** obtains the one-shift asymptotic for #{p < N : p − 1 SOTS} from the hypothesis E(N, N^{1−ε}) (EH
  type), with a main-term error O(ε^γ). It does not claim EH is necessary.

**What this lane adds (§3).**
* **Lemma P (PROVED).** Take the semi-linear sieve by 𝒬, any density g(q) = 1/q + O(1/q²) with g(q) ≥ 1/q (this
  includes 1/q and the shifted-prime density 1/(q − 1)), and level D = x^{1/2−ε}. Then there is a sequence on
  n ≡ 1 (mod 4) with the same local density (and remainders within the stated bound) and **no element in S**. The
  mechanism is a hidden 𝒬-prime above the level. A variant with data restricted to d | P(z) works whenever
  zD ≤ x^{1−ε}, with D ≥ 1.
* **Prop P′ (PROVED relative to Iwaniec 1976 Thm 1).** Conversely, full data at a fixed level D = x^θ with θ > 1/2
  force positive S-mass ≫ X(log x)^{−1/2} for every parity-forced sequence.
* **So, for these densities and remainder hypotheses, 1/2 is the infimum exponent for a uniform single-component
  guarantee.** There are counterexamples at every fixed exponent below 1/2, and positivity at every fixed exponent
  above it. The endpoint itself is not settled here. Bombieri–Vinogradov gives 1/2 − ε. Iwaniec 1972 obtains an exact
  shift at that level with switching, which uses the primality of p and is not part of the sieve data. This is not a
  claim that switching is necessary.

**Reading (Assessment, about known implementations, not a necessity theorem).** For two components no data-only
threshold is known. Lemma P establishes only the single-component obstruction and gives no lower bound for a
threshold with the actual joint data; constructing a compatible joint counterexample is a separate problem. The product
linear sieve with joint data works above level 1; the vector sieve needs level > cosh²(1/2) ≈ 1.27 (HCKILL). The
switched implementations found need ≈ 0.996 (P415 ledger, model, sufficient level found). FI 2009 needs A(θ) with θ near 1.

### H3. None of the 2018–2026 parity-breaking or Type II results located supplies the missing input (Assessment, per lit_C)
* **Prime = norm with a thin coordinate.** This covers Friedlander–Iwaniec a² + b⁴, Heath-Brown–Li, Maynard
  (incomplete norm forms), Pratt, Merikoski (X² + (Y² + 1)², sparse b), and Green–Sawhney p² + nq²
  (arXiv:2410.04189). The *full-family confinement constructions* built on these theorems are excluded by P415
  Lemmas A1/A2, under their hypotheses. Other uses of these technologies are not excluded by a theorem; none was
  found that fits (Assessment). Green–Sawhney's Type II uses coordinatewise product weights; ours is radial.
* **Results that average over the shift.**
  * Grimmelt–Merikoski–Pandey–Pascadi, arXiv:2610.41356 (Oct 2026) [Abs]: primes n² + h for almost all h.
  * Lichtman; Lichtman–Teräväinen.
* **Log-averaged and almost-all-scale correlations, with no prime variable:** Tao–Teräväinen, Helfgott–Radziwiłł,
  Pilatte, Klurman–Mangerel–Teräväinen.
* **Distribution of primes beyond 1/2.** Separate ledgers [P-sub unless marked]:
  * **Fixed integer residue with well-factorable weights:**
    * BFI Thm 10: 4/7 [Sec];
    * Maynard II: 3/5, and 7/12 for linear upper-bound weights;
    * Lichtman arXiv:2309.08522 Cor. 1.5: 66/107;
    * Pascadi arXiv:2505.00653 Thm 1.3: 5/8, and 3/5 for linear upper-bound weights.
  * **Structured factored moduli with absolute values:** Maynard I, fixed residue.
  * **Residues allowed to vary per prime, smooth or densely divisible moduli:** Polymath8a Thm 1.1, 1/2 + 7/300;
    Stadlmann, 1/2 + 1/40.

  None covers our CRT residues (−4 mod d₁, −1/4 mod d₂) together with semi-linear sieve supports up to ≈ √x.
  Teräväinen arXiv:1611.08585 Lemma 9.2 / Remarks 9.3–9.4 gives a partial factorization of semi-linear weights with
  exponent 3/7 (lower) and 2/5 (upper); Remark 9.3 shows 3/7 is optimal *for that lemma's factorization assertion*.
* **The one fixed-shift parity claim located.** Lü–Wang–Wu, arXiv:2610.20242 (14 Oct 2026, v1) [Abs], claims
  Σ_{p≤x} μ(p+2) = o(π(x)).
  * It is unrefereed. Lit_C's reader judged the Type II step doubtful (Assessment, not a verification).
  * Even if correct, it gives o(π(x)) for a signed non-pretentious function. P(4,15) needs a lower bound of order
    π(x)/log x for indicators (§4.3).

### H4. The Siegel-zero route is not viable (Assessment)
* **The available inputs are too weak for the coupled-residue problem.**
  * Uniform-in-residue prime levels under an exceptional character:
    * Wright arXiv:2609.35950 Thm 3.1: x^{30/59} individually [P-sub];
    * Wright Thm 3.2: x^{16/31} on average [P-sub];
    * FI 2003, via Wright's restatement: θ < 233/462 [Sec].
  * Wright also recalls a fixed-residue result up to x^{2/3−ε} under an exceptional character [Sec, per
    internal_review.md]. Fixed residue does not fit our coupled residues.
  * Tao–Teräväinen arXiv:2109.06291 Thm 1.6 allows at most two Λ-factors, and they say three-point divisor
    correlations are not understood.
  * Merikoski arXiv:2108.01355 Thm 15 needs Type I and Type-I-χ inputs at exponent > 0.61634, plus comparison-sequence
    hypotheses. For r(n+4)r(4n+1) only Weil-bound levels of type x^{1/12} are available, by analogy with FI 2009
    Lemma 4.2 (det 1).
* **The route may be vacuous.** Banks, arXiv:2610.15483 (Oct 2026) [Abs], gives an explicit-constant account of an
  "OpenAI manuscript" claiming (1 − β)log q ≥ 3·10⁻³ for all q ≥ 3. It is unrefereed and we do not rely on it.

### H5. The cheapest missing estimate identified is (★K) (incomplete specification, Assessment, §4.2)
* **Statement.** (★K) is a Bombieri–Vinogradov theorem at level x^{1/2−η} for the Titchmarsh-type sequence
  {r*(4p+1)}_p in the classes p ≡ −4 (mod d), with semi-linear sieve weights.
* **What it would give.** FI's template would give P(4,15) with (★K) plus a switched companion (★K′). This is a
  research specification, not a proved implication.
* **Status.** It was not located in the literature. Opened up, it concerns primes in classes modulo d·e with total
  modulus up to ≈ x. For (d, e) = 1 the residue is −4 + 15d·\overline{4d} (mod de), coupling d and e.
* **Closest object.** The quoted BV theorem for r(p − 1) (Dimitrov arXiv:2402.16425) has moduli ≤ (log X)^A, and its
  printed main term fails a local check (§9 erratum). It is not used as a benchmark.

### Verdict: **narrowed** (literature-calibrated)
**What this lane provides.**
* A provenance-tagged map (§2).
* Lemma P with its converse Prop P′. For one component, 1/2 is the infimum exponent for a uniform data-only
  guarantee of S-mass; the endpoint is open.
* An incomplete research specification (★K), with its to-do list.

**The judgement (Assessment).** Unconditional K(4) is *known-hard in the practical sense*. Every implementation
audited needs EH-strength input. Its det-1 analogue has been conditional since 2009, and that status was reaffirmed in
2026. No 2018–2026 result located supplies the input. This is not a theorem that K(4) is hard.

**Recommendation (Assessment).**
1. Stop spending lanes on exact unconditional K(4).
2. Bank Theorem U and the K4CHEN explicit bound.
3. Record K(4) as "FI-2009 class (EH-hard for known methods)".
4. Re-open only if one of the triggers in §4.4 appears.

---------------------------------------------------------------------------------------------------------------------
## 1. Statements attacked (one label each)

* **(T) P(4,15).** CONJECTURE. The lane question: is it, or a close analogue, known or known-hard?
* **(L) Lemma P.** PROVED (§3).
* **(L′) Prop P′.** PROVED relative to Iwaniec 1976 Theorem 1, cited [P-me] (§3).
* **(I) Identity 1_S(N) = (1 + i^{Ω_𝒬(N)})/2 on the stated range.** PROVED (§4.3).
* **(K) "(★K) + (★K′) ⟹ P(4,15)".** Assessment: a proposed route with a sketch (§4.2), not a proved implication.
* **(B) The level "budget" readings and the ranking (§4.1).** Assessment.
* **Literature items.** Each cited result is PROVED relative to its source (the source's own theorem; CONDITIONAL
  where the source is conditional, e.g. FI 2009 Thm 4 on A(θ)). Provenance is tagged separately. Search and
  applicability summaries (H1, H3, H4, §§7–8) are Assessment.

**Why this is not already closed.**
* P415 and HCKILL ran bounded literature checks (`data/z55/p415/lit_report.md`, `data/z54/hckill/lit_report.md`). This
  lane adds the following:
  * Iwaniec 1972 Thm 1;
  * Iwaniec 1976 Thms 1–4 and Cor. 2, from page images;
  * the FI 2009 §§5–7 mechanism;
  * Sedunova 2026;
  * Nath–Xie v3 (Ω ≤ 9);
  * the 2026 preprints GMPP, Lü–Wang–Wu and Banks;
  * the residue-structure analysis of the beyond-1/2 levels;
  * the semi-linear factorization limitation.
* Lemma P and Prop P′ answer a question the literature reports left open: does forced parity by itself help, and at
  which level? This escapes nothing in the closed list or in FRONTIER §6.

---------------------------------------------------------------------------------------------------------------------
## 2. Literature map (statements of cited results; provenance tags; details in the reports)

| Problem | Best result located | Status in source | Source [tag] |
|---|---|---|---|
| p + 4 ∈ S, order of magnitude | ≍ N/(log N)^{3/2} | proved (semi-linear sieve + switching, BV) | Iwaniec 1972 Thm 1, S₁ = proper reps, A = −4 [P-sub] |
| p − 1 SOTS, asymptotic | conditional | from E(N, N^{1−ε}) with O(ε^γ) error | Iwaniec 1976 Cor. 2 (2.1) [P-me]; Nath–Xie v3 p. 2 "still do not have an asymptotic" [P-me] |
| b*(p − 1) = 1, i.e. (p − 1)/2 ∈ S, in short intervals | (x, x + x^θ], θ ≥ 10/11 | proved | Matomäki 2007 Thm 1 [P-sub] |
| Σ_p r(p − a) asymptotic | yes | proved | Linnik 1960 [Sec]; FI 2009 Thm 5 via BFI Thm 9 [P-me] |
| p − 1 SOTS & Ω(p + 2) ≤ 9 | ≫ x/(log x)^{5/2} | proved | Nath–Xie v3 Thm 1.1 [P-me] |
| p − 2, p + 2 both SOTS (det 1) | Λ-weighted ≍ x | lower bound conditional on A(θ), θ → 1; upper bound unconditional | FI 2009 Thms 2–4 [P-me]; Sedunova 2026 [Abs]; Kontorovich 2014 §3.6.2 [P-sub] |
| n ± 2 SOTS, n squarefree, ω(n) ≤ 7 | representation-weighted ≫ x/log x | proved (level x^{1/6} for r(n−2)r(n+2)) | Sedunova 2026 Thm 2; Thm 3: R(θ) ⟹ ≤ ⌊2/θ⌋ factors [P-sub] |
| integers n, n + 1 both SOTS | ≫ x/log x | proved | Indlekofer 1974 [P-sub]; Hooley 1974 [Sec] |
| integers n, n + h, n + k SOTS | infinitely many | proved | Hooley 1973 [Sec] |
| p + 4 ∈ S & Ω_𝒬(4p + 1) bounded | ≫ x/(log x)² | internal (rel. BV + cited sieve lemmas) | Z55_P415 Thm U |
| **P(4,15)** | — | internal conditionals: EH(θ₀) (HCKILL Thm E); Bunyakovsky (Thm Q) | internal |
| P₂ values n = 720k² + 1 with both shifts in S | infinitely many | proved | Lemke Oliver 2012 Thm 1 + Thm Q (P415 Prop C) |

**Sieve facts [P-me].**
* **Iwaniec 1976 Thm 1:** κ = 1/2 bounds with remainders over d < z^s, with lower function 1 − f_I(s)/√s =
  (e^γ/πs)^{1/2}∫₁^s dt/√(t(t−1)) on [1, 2]. This equals f(s) above and vanishes at s = 1, so the sifting limit is β = 1.
* **Iwaniec 1976 Thm 2:** as in H2.
* **FI 2009 §6, verbatim:**
  > "Since the sieving limit for the semilinear sieve is β = 1 and our level of distribution is D = D(x) < √x, we
  > cannot successfully apply the lower bound sieve to S(A^{(δ)}, P, √x), but we can come close to this"
* **FI 2009 §7:** "Note that we actually require A(θ) for the sum weighted by a divisor function, but this extra factor
  can be handled by an application of Cauchy's inequality."

---------------------------------------------------------------------------------------------------------------------
## 3. Lemma P and Prop P′: below level 1/2 no data-only guarantee of S-membership, above it a guarantee

**Setting.** We work with a finite sequence 𝒜 = (a_n)_{n≤x} with a_n ≥ 0.
* **Data.** For squarefree 𝒬-composed d put 𝒜_d = Σ_{d|n} a_n and r_d = 𝒜_d − X·g(d), for a mass X > 0 and a
  multiplicative density g.
* **Admissible densities.** We take g(q) = (1 + c_q)/(q + c_q) on 𝒬 with constants 0 ≤ c_q ≤ C/q. This gives:
  * c_q = 0: g = 1/d, the density of the integers;
  * c_q = 1/(q − 2): g(q) = 1/(q − 1), the single-component local density of p + 4 and of 4p + 1 over primes
    p ≡ 1 (8). At q = 3 this is c₃ = 1, g = 1/2, so this case needs C ≥ 3.
* **Parity-forced.** 𝒜 is *parity-forced* if a_n > 0 ⟹ n ≡ 1 (mod 4). Then n is odd and Ω_𝒬(n) is even.
* **P(z).** P(z) = ∏_{q∈𝒬, q<z} q.

**Lemma P (PROVED).** Fix 0 < ε < 1/4 and C ≥ 1, and let x ≥ x₀(ε, C).
* **(a) Full data.** Put D = x^{1/2−ε}. There is an 𝒜 with:
  * **(i)** 𝒜 is parity-forced;
  * **(ii)** no element in S;
  * **(iii)** Σ_{d≤D, d 𝒬-composed sqfree} |r_d| ≪_{ε,C} X·x^{−ε/5};
  * **(iv)** X ≍_{ε,C} x/log x (in case (a) the constants depend on C only).
* **(b) Data restricted to d | P(z).** For D ≥ 1 (free), x^ε ≤ z and zD ≤ x^{1−ε}, the same holds with the sum in (iii) over
  d | P(z), d ≤ D.

**Construction.** Let H = D in case (a) and H = z in case (b), and let E = x^{ε/2}.
* **The density-adjusting weight.** For m ≥ 1 put w(m) = Σ_{e | m, e ≤ E, e sqfree 𝒬-composed} c_e, with
  c_e = ∏_{q|e} c_q. This weight is ≥ 0.
* **The sequence.** a_n := Σ_{q ∈ 𝒬 ∩ (H, 2H]} 1[q | n, m := n/q ≡ 3 (mod 4)]·w(m), for n ≤ x.

*Proof.*
1. **Parity and S.** Every n with a_n > 0 is n = qm with q ≡ m ≡ 3 (mod 4). So n ≡ 1 (mod 4), and q | n with
   q ∈ 𝒬, hence n ∉ S.
2. **Coprimality.** Every d in the data has all prime factors ≤ H in case (a) (they are ≤ D) and < H in case (b)
   (they are < z), while every hidden prime is > H. Hence (d, q) = 1 and d | qm ⟺ d | m. Also e ≤ E < H, so the hidden q never divides e.
3. **One hidden prime.** For Y = x/q,
   Σ_{m≤Y, m≡3 (4), d|m} w(m) = Σ_{e≤E} c_e·#{m ≤ Y : m ≡ 3 (4), [d, e] | m} = (Y/4)Σ_{e≤E} c_e/[d, e] + O(Σ_{e≤E} c_e).
   This holds because d, e are odd, so the conditions define one class mod 4[d, e]. Moreover
   Σ_{e≤E} c_e ≤ Σ_{e≤E} C^{ω(e)}/e ≪_C (log x)^C.
4. **The untruncated sum.** Σ_{all e} c_e/[d, e] = Σ_e c_e(d, e)/(de)
   = d⁻¹∏_{q′∤d}(1 + c_{q′}/q′)∏_{q′|d}(1 + c_{q′}) = G·g(d), where G := ∏_{q′∈𝒬}(1 + c_{q′}/q′) converges. The last
   step uses (1 + c)/(q′(1 + c/q′)) = (1 + c)/(q′ + c) = g(q′).
5. **The tail e > E.** Write f = (d, e) and e = fe′. Then
   Σ_{e>E} c_e(d, e)/(de) ≤ d⁻¹Σ_{f|d} c_f Σ_{e′>E/f} c_{e′}/e′,
   and Σ_{e′>T} c_{e′}/e′ ≤ Σ_{e′>T} C^{ω(e′)}/e′² ≪_C T^{−1/2}. So the tail is
   ≪ d⁻¹E^{−1/2}Σ_{f|d} c_f f^{1/2} ≤ d⁻¹E^{−1/2}∏_{q′|d}(1 + C q′^{−1/2}).
6. **Assembling 𝒜_d.** Summing over q gives 𝒜_d = X g(d) + r_d with X := (G/4)Σ_{q∈𝒬∩(H,2H]} x/q and
   |r_d| ≪ π(2H)(log x)^C + (X/d)E^{−1/2}∏_{q′|d}(1 + Cq′^{−1/2}).
7. **Size of X.** By the prime number theorem in progressions, Σ_{q∈𝒬∩(H,2H]} 1/q ~ log 2/(2 log H). As
   H ≥ x^{ε}, this gives X ≍_{ε,C} x/log x, which is (iv).
8. **Summing the remainders.**
   * The first part of |r_d| sums to ≪ D·π(2H)(log x)^C over d ≤ D. In case (a) this is ≪ D²(log x)^C ≤ x^{1−2ε}(log x)^C.
     In case (b) it is ≪ Dz(log x)^C ≤ x^{1−ε}(log x)^C.
   * The second part sums to ≪ X E^{−1/2}Σ_{d≤D} d⁻¹∏_{q′|d}(1 + Cq′^{−1/2}) ≪ X x^{−ε/4} log x. The last step uses
     Σ_{d≤D} h(d)/d ≤ ∏_{q′≤D}(1 + h(q′)/q′) ≪_C log(2D) for h(q′) = 1 + Cq′^{−1/2}.
   * Comparing with X ≍ x/log x gives (iii), with room to spare. ∎

**Prop P′ (PROVED relative to Iwaniec 1976 Theorem 1 [P-me]).** Suppose:
* 𝒜 is parity-forced and supported on n < x;
* g satisfies Iwaniec's κ = 1/2 hypotheses (Ω₁)–(Ω₂) with sifting set 𝒬. This holds for the g above, since
  q·g(q) = 1 + O(1/q) and Mertens in progressions applies;
* Σ_{d<D, d|P(√x)} |r_d| ≪ X(log x)^{−1} for D = x^θ with θ > 1/2 fixed.

Then Σ_{n∈S} a_n ≥ X·W(√x)·(f(2θ) − o(1)), where W(z) = ∏_{q∈𝒬, q<z}(1 − g(q)). In particular the sum is
≫_{θ,C} X(log x)^{−1/2} > 0, for the densities of Lemma P (in general ≫_{θ,g}, with fixed sieve-hypothesis
constants K, L).

*Proof.* Let n < x have a_n > 0 and (n, P(√x)) = 1. Then Ω_𝒬(n) is even. If it were ≥ 2, then n ≥ (√x)² = x, a
contradiction. So n ∈ S, and Σ_{n∈S} a_n ≥ S(𝒜, √x). Apply Iwaniec's Thm 1 lower bound with z = √x and s = 2θ, so
that z^s = D:
S ≥ Ω(z)X{1 − f_I(s)/√s + O(e^{2K−s}(log z)^{−γ})} − Σ_{d<D}|R(𝒜, d)|.
Here 1 − f_I(s)/√s = f(s) for s ∈ (1, 2]. For s > 2 it stays positive and tends to 1, by Iwaniec §4, equations
(4.3)–(4.4), and Lemma 7 (explicit up to s = 3). Also Ω(z) = W(z) ≍_g (log x)^{−1/2}. Theorem 1 is stated for finite
sets. Its proof rests on pointwise sieve inequalities, which may be multiplied by a_n ≥ 0 and summed, so it applies
verbatim to weighted sequences. ∎

**Reading (both PROVED statements).** The data in question are the sieve data for one parity-forced component with
density 1/q + O(1/q²) on 𝒬.
* At any fixed level x^{1/2−ε}, the stated hypotheses (density g with g(q) ≥ 1/q, remainders within the stated
  bound, forced parity) alone do not guarantee a single element of S. The obstruction is the parity of the 𝒬-primes
  *below the level*, which congruences do not fix.
* At any fixed level x^θ with θ > 1/2, the hypotheses of Prop P′ guarantee ≫ X(log x)^{−1/2} of S-mass.

So 1/2 is the infimum exponent for a uniform guarantee; the endpoint is not settled here. BV supplies 1/2 − ε. The
audited unconditional implementations (Iwaniec 1972, Theorem U, Nath–Xie, FI 2009) all add *switching*: an upper bound
for the configurations N = qq′m, obtained by sieving the prime variable p = N − 4 in the switched sequence. Switching
uses primality of the base variable, which the data do not contain. No claim is made that switching is necessary.
* **What this does not cover.** It does not cover the joint data of (p + 4, 4p + 1). Their joint density h(d₁, d₂)
  has h(q, q) = 0 for q ∈ 𝒬, q ≠ 3, and h(3, 3) = 1/2.
* **Joint-data threshold.** Lemma P gives only the single-component obstruction. It gives no lower bound for a
  threshold with the actual joint data, and constructing a compatible joint counterexample is a separate problem. The
  product linear sieve with joint data gives sufficiency above level 1 (Assessment from HCKILL's setup). Nothing is
  settled below that.

**Remarks.**
1. **Numerics (EVIDENCE).** The hidden-prime example with g = 1/d is in `scripts/z56_k4lit_lemmaP.py`, with output in
   `data/z56/k4lit/lemmaP_*.txt`. Its sifted mass realises the parity-*odd* model at the cofactor parameter
   s′_q = log(x/q)/log z. That parameter is ((1/2 + ε)/(1/2 − ε))·s + o(1), where s = log D/log z; it is *larger* than
   s for fixed ε, so the example is not claimed to make f sharp.
   * Run x = 10¹², D = x^{0.45}: S(𝒜, z)/(XW(z)) = 0.5946, 0.7082, 0.8127, 0.9049, 0.9775 for s = 1, 1.1, 1.25, 1.5, 2.
     The comparison is f(s′) at the representative s′ for q = 1.5D: 0.5837, 0.6981, 0.8038, 0.8998, 0.9758.
   * The natural sequence (n ≤ 10⁸, n ≡ 1 (4)) gives 1.5052, 1.4351, 1.3463, 1.2290, 1.0643 against
     F(s) = 1.5059, 1.4358, 1.3469, 1.2296, 1.0648. For s ≤ 2 its survivors are exactly S, so this is Landau's theorem
     in sieve form.
   * Relative sieve-data errors for the tested small d are ≤ 1.6·10⁻³, and ≤ 1.1·10⁻⁵ for d ≤ 23.
   * The crude total D·#{hidden q}/X is 0.36 at 10¹² and 3.2 at 10¹³. These values do not verify the asymptotic
     hypothesis at those sizes; the lemma is asymptotic.
   * The density-adjusting weight w with c_q = 1/(q − 2) gives ratio·φ(d) = 0.9997–1.0000 for d ∈ {3, 7, 11, 19, 21,
     33, 57, 231} (`scripts/z56_k4lit_phiweight.py`, Y = 2·10⁷, E = 2000; `data/z56/k4lit/phiweight.txt`).
2. **Novelty (Assessment).** Lemma P is a folklore-type construction with a hidden prime above the level. Prop P′ is
   an immediate corollary of Iwaniec's Theorem 1. The infimum-exponent statement for parity-forced κ = 1/2 data was not
   located in this form. It corrects the shorthand "no parity barrier, only level" in lit_B and lit_C. At BV level there
   is a barrier, namely the parity of the small 𝒬-primes. It disappears as soon as the level exceeds 1/2.

---------------------------------------------------------------------------------------------------------------------
## 4. Judgement: methods ranked, and a concrete plan (all Assessment unless labelled)

### 4.1 Ranking

**1. Chen / Nath–Xie v3 vector sieve with switching and Richert weights (the K4CHEN lane).**
* Reaches: an explicit bound Ω_𝒬(4p + 1) ≤ K with p + 4 ∈ S.
* Missing: a constants audit.
* Probability: high for some explicit K. K = 0 is not reached by the implementations in the P415 ledger.

**2. FI template with (★K): r*-weight on N₂, semi-linear sieve on N₁, switching.**
* Reaches: exact P(4,15).
* Missing: (★K) and (★K′) (§4.2).
* Probability: very low. Opened up, (★K) is a level-≈1 statement for primes with coupled residues.

**3. Shell-as-base Harman sieve (det-15 shell; GMPP-type Type II).**
* Reaches: exact P(4,15).
* Missing:
  * Type I level R(θ) for r(n+4)r(4n+1) with θ ≥ 1/2. The det-1 analogues known are 1/12 (FI Lemma 4.2) and 1/6
    (Sedunova).
  * A *fixed-shift* Type II estimate for the shell. GMPP's Type II averages over h.
* Probability: very low. This is the FI hyperbolic-PNT gap itself.

**4. Fixed-shift multiplicative cancellation (Lü–Wang–Wu type, g = i^{Ω_𝒬}).**
* Reaches: at best the "0 vs 2" discrimination.
* Missing:
  * Lü–Wang–Wu verified;
  * a log-power saving on a sparse set;
  * the companion sieve (§4.3).
* Probability: very low.

**5. Siegel-zero dichotomy.**
* Missing: the inputs are too weak (H4).
* Probability: ≈ 0.

**6. Algebraic families / prime-value theorems.**
* The full-family constructions are excluded (P415 A1/A2). What remains are Bunyakovsky slices.
* Probability: 0, unconditionally.

### 4.2 Proposed route via (★K) (Assessment: an incomplete research specification and sketch, not a proved implication)

**The primitive weight (PROVED identity).** For odd N, r*(N) = 4Σ_{e|N} μ²(e)χ₋₄(e) = 4·2^{ω(N)}·1_S(N).
* *Proof.* After division by 4, both sides are multiplicative. For r*/4 the local factors are: a split prime power
  ℓ^a contributes 2, since the Gaussian factor is π^a or π̄^a but not a mix (a mix would force a common divisor);
  an inert prime factor contributes 0, since it divides both coordinates. Units give the factor 4, including at N = 1.
  On the other side, Σ_{e|N} μ²(e)χ₋₄(e) = ∏_{ℓ|N}(1 + χ₋₄(ℓ)), which is 2^{ω(N)} if N ∈ S and 0 otherwise. ∎

**(★K), specification.** Let λ_d be the upper or lower semi-linear β-sieve weights of level D = x^{1/2−η}. They are
supported on squarefree d composed of 𝒬-primes q ≠ 3. Put 𝒫 = {p ≤ x prime : p ≡ 1 (8), p ≢ 2 (3)}. Discarding
p ≡ 2 (3) loses nothing: there 3 | N₁ and 3 | N₂, so r*(N₂) = 0.

The required estimate is that for every A,
  Σ_{d≤D} λ_d (Σ_{p∈𝒫, d | p+4} r*(4p+1) − g*(d)·𝒳) ≪ x(log x)^{−A},
where:
* 𝒳 = Σ_{p∈𝒫} r*(4p+1);
* g* is multiplicative with g*(q) = 𝔼[r*(N₂) | q | N₁] / 𝔼[r*(N₂)] · 1/(q − 1).

Since q | N₁ ⟹ N₂ ≡ −15 (mod q), a residue determined by q, the local factor at q is the conditional r*-mass. The
explicit local computation, including the primes 3 and 5 that divide the determinant 15, is part of the specification
and was **not carried out**.

**(★K′), specification.** (★K′) is a uniform upper bound of the expected order for the switched sums
  Σ_{a = mq} Σ_{q′ prime, q ≤ q′ ≤ (x+4)/a, aq′−4 ∈ 𝒫} r*(4aq′ − 15),
summed over m ∈ S, m ≤ x/z₁², and q ∈ 𝒬 with q ≥ z₁. The bound is needed with an absolute constant (P415 Step 3
ranges). A crude bound by r* ≤ 4τ loses a logarithm and is **not** an acceptable substitute (internal review
Finding 4). The bound must be proved with the r*-weight itself, for example via a divisor-sum evaluation as in FI §7
and Lemma 4.1.

**Sketch of (★K) + (★K′) ⟹ P(4,15)** (Assessment). Follow P415 Theorem U with these changes:
* Replace N₂'s sieve component by the weight r*(N₂).
* Sieve N₁ by the semi-linear lower sieve to z₁ = x^{θ₁}, with level D, using (★K).
* Bound the two-large-prime configurations in N₁ via (★K′).

The intended comparison is the contest O(η^{3/2}) against ≍ η^{1/2} of P415 Steps 4–5. That it survives the
r*-weighting is **not established**. Still to do:
* the mass asymptotic for 𝒳;
* the local densities g*;
* the switched bound (★K′) with its parameter dependence;
* the complementary-divisor analysis. The primitive coefficients μ²(e)χ₋₄(e) are not symmetric under e ↔ N/e, so
  FI's small-divisor evaluation does not transfer automatically.

If all this goes through, the output is a positive weighted sum
Σ_{p: N₁∈S} r*(N₂) ≫ x/(log x)^{3/2}, which gives infinitude. Cauchy–Schwarz with
Σ_{p≤x} r*(4p+1)² ≤ 16Σ_{n≤4x+1} τ(n)² ≪ x log³x gives a count ≫ x/(log x)^6. This is the FI 2009 §§6–7 structure
transplanted. FI's own hypothesis is A(θ) with a divisor-function weight. It motivates (★K) but is not identical to it:
FI use r on different forms with their own local factors.

**Why (★K) is hard (Assessment).**
* Opening r* by the identity gives primes in classes modulo d·e, with d ≤ x^{1/2−η} and squarefree e | 4p + 1.
  After switching e ↔ (4p + 1)/e, e is ≤ √x, so the total modulus is up to ≈ x.
* On the primitive support we have (d, e) = 1, with d composed of 𝒬-primes and e of split primes. The residue is
  then a ≡ −4 (mod d) and 4a + 1 ≡ 0 (mod e), i.e. a ≡ −4 + 15d·\overline{4d} (mod de). The inverse is taken modulo
  e; check: 4a + 1 ≡ −15 + 15·4d·\overline{4d} ≡ 0 (mod e). Before primitive cancellation, common factors require
  (d, e) | 15 and modulus lcm(d, e).
* The coupling through \overline{d} (mod e) means no single integer residue serves all moduli, which BFI, Maynard,
  Lichtman and Pascadi require. A dispersion attack would meet Kloosterman fractions twisted by
  15·\overline{4d}/e at total modulus ≈ x, far beyond the ranges those methods reach (≤ x^{5/8}, single residue).

### 4.3 The "0 vs 2" multiplicative route (lit_C Lead B)
**Identity (PROVED).** Let N be odd, N ≡ 1 (mod 4), (N, P(z)) = 1 and z > N^{1/4}. Then Ω_𝒬(N) ∈ {0, 2}, because
at most three 𝒬-factors fit and the number is even. Hence 1_S(N) = (1 + i^{Ω_𝒬(N)})/2. With all sums over primes
p ≤ x, p ≡ 1 (8), and z > (4x + 1)^{1/4}:
  Σ_p 1_S(N₁)1_S(N₂) = ½[Σ_p 1_S(N₁)1[(N₂, P(z)) = 1] + Σ_p 1_S(N₁)1[(N₂, P(z)) = 1]·i^{Ω_𝒬(N₂)}].

**Reading (Assessment).**
* The first sum combines an exact S-shift with 𝒬-sifting of N₂ to z > x^{1/4}. The implementations audited would
  need extra level beyond BV for it; the bookkeeping says ≈ 3/4 total. This is a sufficient-implementation count, not
  a lower bound.
* The second sum needs relative o(1) cancellation of i^{Ω_𝒬} on a set of density ≍ (log x)^{−1}. That is stronger
  than the o(π(x)) a Lü–Wang–Wu-type theorem would give.
* These are two independent hard inputs, so the route ranks low.

### 4.4 Concrete plan
1. **Bank now.**
   * Theorem U, plus the K4CHEN explicit bound.
   * Correct the P415 citation: Nath–Xie v3 has Ω ≤ 9, not 11.
   * Record K(4) in FRONTIER as FI-2009 class (text in §7).
2. **Optional and cheap, but with no ES content.** Port FI 2009 Lemma 4.2 / Sedunova Lemma 2 to the det-15 shell,
   giving the level of distribution of r(n+4)r(4n+1) in APs via Weil bounds.
   * Expected outcome (Assessment, an unproved plan): a representation-weighted infinitude of squarefree almost-prime
     n with n + 4 and 4n + 1 SOTS.
   * Prop C already gives a thin P₂ version with both shifts in S. Low priority.
3. **Triggers for re-opening.** Re-open K(4) if any of the following appears:
   * (a) An independently verified Lü–Wang–Wu. Then test their "C–S in the cofactor → determinant equation" Type II on
     Σ_{p≡−4 (d)} g(4p+1) with g = i^{Ω_𝒬}.
   * (b) A fixed-shift version of the GMPP Type II for binary-form sequences.
   * (c) A beyond-1/2 prime level allowing coupled residues −4 + 15d·\overline{4d} (mod de).
   * (d) Any unconditional lower bound in FI's det-1 problem, which would very likely port to P(4,15).
4. **Do not spend lanes on:**
   * level optimisation of vector or linear sieves (P415 ledger);
   * Siegel zeros;
   * algebraic families;
   * "forced parity" at BV level (Lemma P).

---------------------------------------------------------------------------------------------------------------------
## 5. Verification log

**Checked by me against primary text [P-me].**
* **FI 2009 PDF** (text extraction):
  * Assumption A(θ); Theorems 2, 3, 4 and 5;
  * §5: "level of distribution D = x^{1/12−2ε}";
  * §6: the β = 1 / D < √x passage; "√x suffices because, if n ≡ 1 (mod 4) has one prime factor from P, it must
    have a second one";
  * §7: the divisor-weight sentence; "narrowly misses".
* **Iwaniec, Acta Arith. 29 (1976), pp. 70–73**, page images:
  * Theorem 1;
  * Theorem 2: hypotheses a′ ≡ 1 (4), 𝒫 ⊂ {p ≡ −1 (4)}; Q⁶ < z² ≤ A; remainder over d < A/Q; error term with
    ((L + log Q)/log A)^γ;
  * Theorems 3–4;
  * Corollary 2 (2.1)–(2.3).
* **arXiv abstract pages** for 2609.28200, 2610.41356, 2610.20242 and 2610.15483.
* **Nath–Xie v3 PDF:** Theorem 1.1 (Ω ≤ 9) and Remark 1.1; the abstract page lists v3 as "Final version, published in
  Acta Arithmetica".

**Checked by the internal reviewer** (`data/z56/k4lit/internal_review.md`, "Checks that pass"):
* Iwaniec 1972 Thm 1;
* Maynard II; Lichtman; Pascadi; Teräväinen Lemma 9.2;
* Polymath8a; Stadlmann; Wright; Merikoski Thm 15; Tao–Teräväinen Thm 1.6;
* Sedunova; GMPP.

The original BFI, Linnik, Hooley, Opera de Cribro and FI 2003 texts were not read; they are [Sec].

---------------------------------------------------------------------------------------------------------------------
## 6. FRONTIER §4 hard screens (best items: Lemma P / Prop P′; the (★K) route)

1. **T1 squares.** The kill side, so this screen constrains upper-side proofs. Odd squares m² satisfy both confinements:
   m² + 4 and 4m² + 1 are primitive SOTS (P415 §5). Lemma P and Prop P′ are statements about sieve data and are
   indifferent to squares. (★K) concerns primes only.
2. **8/131, 8/241.** K(4) is specific to line 4 (HCKILL Lemma 1.1). Nothing here is claimed for other lines.
3. **Tied modulus.** Not applicable: the character χ₋₄ is fixed.
4. **Fixed p.** Every statement is a density or infinitude statement. Nothing touches a prescribed prime.

## 7. Proposed FRONTIER text (do not edit FRONTIER here)

> *(z56, `Z56_K4LIT.md`; kill side, K(4) = P(4,15).)*
>
> **Literature calibration** (Assessment from provenance-tagged sources; bounded searches).
> * Neither P(4,15) nor its det-1 analogue was located as an unconditional theorem.
>   * The det-1 analogue is FI 2009 Thm 4, Σ Λ(n)r(n−2)r(n+2) ≍ x. Its lower bound needs A(θ) with θ → 1, and it was
>     reaffirmed as conditional in 2026 (Sedunova arXiv:2609.28200).
>   * The closest unconditional results are Iwaniec 1972 (p + 4 ∈ S), Nath–Xie v3 (p − 1 SOTS, Ω(p + 2) ≤ 9) and
>     Theorem U.
> * No 2018–2026 parity-breaking or Type II result located supplies the missing input.
>   * Full-family constructions satisfying P415 A1/A2 are excluded.
>   * The 2026 GMPP result on n² + h averages over the shift.
>   * The audited unconditional beyond-1/2 prime levels need a single fixed residue (≤ 5/8, weighted) or smooth
>     moduli (≤ 1/2 + 1/40). Our residues are coupled.
>   * Siegel-zero inputs are too weak.
>
> **Lemma P + Prop P′ (PROVED).** Take one parity-forced semi-linear component, with density
> g(q) = 1/q + O(1/q²) ≥ 1/q on 𝒬 and the stated remainder bounds.
> * At every fixed level below 1/2, a hidden 𝒬-prime gives a sequence with the same local density, admissible
>   remainders and no element in S.
> * At every fixed level above 1/2, the S-mass is ≫ X(log x)^{−1/2} (from Iwaniec 1976 Thm 1).
> * The endpoint is open. Nothing is claimed for joint data.
>
> So BV misses by ε. The audited unconditional implementations obtain exact S-shifts at BV level by switching
> (Iwaniec 1972); for two shifts they need level ≈ 1 (Assessment).
>
> **Research specification (★K) (Assessment).** BV at level 1/2 for {r*(4p+1)} in classes p ≡ −4 (mod d), with
> semi-linear weights; together with a switched companion, this is an FI-template route to P(4,15). Opened up, it is
> level-≈1 for primes, with residues coupled through \overline{d} (mod e).
>
> **Recommendation.** Treat K(4) as FI-2009 class (EH-hard for known methods). Bank Theorem U and the K4CHEN bound.

## 8. Bottom line

Unconditional K(4) = P(4,15) was not located in the literature. Its closest relative is Friedlander–Iwaniec's
prime-norm problem on SL₂(ℤ), with p ± 2 both sums of two squares. That problem has been proved only under an
EH-strength hypothesis since 2009, and was described as conditional again in 2026.

This lane makes the "it's only a level problem" diagnosis precise for one component, with sieve data plus the
congruence-forced parity:
* at every fixed level below 1/2, the stated hypotheses do not guarantee any element of S, because a hidden 𝒬-prime
  defeats them (Lemma P);
* at every fixed level above 1/2, Iwaniec's sieve guarantees S-mass (Prop P′).

Bombieri–Vinogradov sits at 1/2 − ε, and the audited unconditional implementations obtain each exact S-shift with
switching. Two exact shifts need about level 1 in every implementation audited.

No recent breakthrough located supplies this:
* full-family constructions on the norm-form prime theorems fail the confinement lemmas (P415 A1/A2);
* GMPP-type parity breaking averages over the shift;
* the audited unconditional fixed-residue weighted levels stop at 5/8 and do not allow coupled residues;
* the residue-uniform Siegel-zero inputs give ≈ 1/2 (a fixed-residue 2/3 is recalled by Wright [Sec]).

The cheapest missing input is the research specification (★K), a BV theorem for the Titchmarsh-type sequence r*(4p+1).

Verdict: **narrowed**. K(4) is EH-hard for every method audited; that is a judgement, not a theorem. Bank Theorem U and
the explicit Ω bound, and stop direct attacks. No step toward ES.

## 9. Review log and errata to the literature reports

* **Internal hostile review** (deep-mode subagent; `data/z56/k4lit/internal_review.md`). Verdict MAJOR REVISION, no
  FATAL. Lemma P's elementary core was confirmed, and both numerical runs reproduced byte-for-byte. Fixes applied:
  * **F1.** "f sharp at s" withdrawn. The example realises f at the larger cofactor parameter s′. Only the zero-S-mass
    statement is claimed.
  * **F2.** The density was generalised: Lemma P now covers g(q) = 1/(q − 1), the shifted-prime single-component
    density, via the weight w. Scope is single-component. The joint exception h(3, 3) = 1/2 is restored.
  * **F3.** "Disappears only at EH" was false. It is replaced by Prop P′: positivity of S-mass from data above level
    1/2. (Round 2 weakened "sharp threshold" to "infimum exponent; endpoint open".) "Switching is the only input" and the per-shift budget are now Assessment statements about
    audited implementations. A1/A2 are scoped to full-family constructions.
  * **F4.** (★K) is now consistently r*, with the primitive identity proved and the q = 3 exclusion stated. (★K′) is
    specified as a switched upper bound with the r*-weight; the τ-majorant shortcut is withdrawn. The route is labelled
    Assessment. The count after Cauchy–Schwarz is x/(log x)^6, and FI's hypothesis is said to "motivate" (★K), not to
    be identical to it.
  * **F5.** The coprimality condition was added to the CRT formula.
  * **F6.** Matomäki's result is now stated as b*(p − 1), i.e. (p − 1)/2 ∈ S. The Iwaniec specialisation is restricted
    to p + 4.
  * **F7.** Sedunova's count is now "representation-weighted".
  * **F8.** Dimitrov is no longer used as a benchmark; see erratum below.
  * **F9.** Level ledgers are separated by residue structure. The Siegel-zero ceiling ≤ 0.52 is qualified as uniform
    in residue, and Wright's fixed-residue 2/3 is noted. Merikoski's threshold is stated with its hypotheses.
  * **F10.** Provenance tags were added; "not located" replaces exhaustive wording; the personal cross-check claim was
    corrected.
  * **F11.** Iwaniec's Theorem 2 error term and Cor. 2's "sufficient, not necessary" status are stated.
  * **F12.** The numerical error claim was corrected (≤ 1.6·10⁻³), the remainder total uses #{hidden q}, and s′ is
    stated as a representative value.
  * **F13.** Lemma P(b)'s admissibility proof was reworked; it no longer changes ε.
  * **F14.** One label per claim (§1); the identity in §4.3 is separated from the reading, with prime restrictions
    under the sums.
* **Errata to the subagent literature reports.** These override the reports' text.
  * (i) **lit_A A1.5 / lit_C.** Dimitrov arXiv:2402.16425 Thm 1's printed global main term φ(q)⁻¹Σ_p r(p − 1) fails
    the local check q = 8, a = 7, where r(p − 1) ≡ 0. A local-density issue in the source as printed is unresolved.
  * (ii) **lit_C table row 15 and §2.14.** Banks 2610.15483 is an unrefereed account of a claimed proof. "Removes the
    Siegel-zero route" holds *only if correct*.
  * (iii) **lit_A and lit_C.** Sedunova's counts are representation-weighted.
  * (iv) **lit_B verdict (c).** The "≤ 0.52" Siegel-zero levels are residue-uniform. Wright recalls a fixed-residue
    x^{2/3−ε} result [Sec].
  * (v) **lit_C §2.8.** The Lü–Wang–Wu assessment is a reader's Assessment, not a verification or a refutation.
  * (vi) **lit_B / lit_C.** "No parity barrier" is to be read as: no barrier for the *total* Ω_𝒬 parity. At BV level
    there is the hidden-prime barrier of Lemma P.
* **Round-2 internal re-review** (`internal_review.md`, "Re-review (round 2)"). Verdict MAJOR REVISION, no FATAL.
  Weighted Lemma P was audited step by step and passes; Prop P′ passes, including s > 2. Fixes applied:
  * R1: "iff" / "exactly" / "never" replaced by the infimum-exponent reading, with the endpoint open; "identical data"
    replaced by "same local density, stated remainders".
  * R2: the joint lower-bound inference was deleted.
  * R3: D ≥ 1 is stated in (b); X ≍_{ε,C}; log(2D); ≤ H vs < H; C ≥ 3 for the shifted-prime case.
  * R4: ≫_{θ,C}; the weighted extension of Iwaniec Thm 1 is stated; §4, (4.3)–(4.4) and Lemma 7 are cited for s > 2.
  * R5: the r*/4 multiplicativity proof is written out; (★K) is relabelled an incomplete specification, with a to-do
    list including the e ↔ N/e asymmetry.
  * R6: literature-status labels are added in §1; universal phrases in §§7–8 are scoped.
  * The script docstring now lists the supported runs.
* **Cross-model review:** pending.
