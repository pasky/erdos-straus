# Z56_K4LIT — literature sweep and judgement for unconditional K(4) = P(4,15)

**ES is OPEN.** Nothing here proves or disproves it. All results are internal and internally reviewed only.
Lane K4LIT (wave z56). Scripts `scripts/z56_k4lit_*`. Data and the three source-verified literature reports are in
`data/z56/k4lit/`:
* `lit_A_shifts.md`: one and two half-dimensional prime shifts;
* `lit_B_parity.md`: parity, Siegel zeros, levels;
* `lit_C_breakthroughs.md`: 2018–2026 parity and Type II breakthroughs.

Notation follows `Z55_P415.md`:
* 𝒬 = {primes ≡ 3 (mod 4)}; S = {n ≥ 1 : every prime factor ≡ 1 (mod 4)};
* N₁ = p + 4, N₂ = 4p + 1; SOTS = "sum of two squares" (weaker than S);
* Ω_𝒬 = the number of 𝒬-prime factors, counted with multiplicity;
* f, F = the semi-linear (κ = 1/2) lower and upper sieve functions;
* r(n) = #{(a, b) ∈ ℤ² : a² + b² = n}.

**P(4,15)**: there are infinitely many primes p ≡ 1 (mod 8) with p + 4 ∈ S and 4p + 1 ∈ S. By `Z54_HCKILL.md` Lemma 1.1
(PROVED) this is K(4), "HC(p) > 4 infinitely often".

**Reading guide.**
* "Verified" means the statement was read in the primary source: PDF text, or the page image of a scanned journal page.
  It was quoted either by a research subagent or by me. Every item in the hot-lead list was cross-checked by me against
  the source (§5).
* "Secondary" means the statement was read in a paper that quotes it.
* Sources dated 2026 are mostly arXiv v1 preprints: unrefereed.
* No exhaustiveness is claimed for any literature search.

---------------------------------------------------------------------------------------------------------------------
## 0. Hot leads and verdict (read this first)

### H1. P(4,15) is not in the literature, and neither is its det-1 analogue
P(4,15) is not known unconditionally, and no unconditional or conditional source states it. Its exact structural
analogue is also open unconditionally: primes p with p − 2, p + 2 both SOTS (equivalently prime norms of SL₂(ℤ)).
* **Friedlander–Iwaniec**, *Hyperbolic prime number theorem*, Acta Math. 202 (2009). Theorem 4,
  S(x) = Σ_{n≤x} r(n−2)r(n+2)Λ(n) ≍ x, holds "Under the same assumption as Theorem 2". That assumption is A(θ), "for
  some θ, less than 1 but sufficiently close to 1" (read from the PDF).
* **Sedunova**, arXiv:2609.28200 (Sept 2026), abstract (read): "the upper bound is unconditional, while the lower one
  rests on a strong hypothesis concerning the distribution of primes in arithmetic progressions".
* **Shparlinski–Xiao**, arXiv:2609.21460 (abstract): the result is "conditional on a very strong form of the
  Elliott–Halberstam conjecture".

So the det-1 problem has resisted for 17 years and was re-confirmed open twice in autumn 2026.

The best unconditional neighbours, all verified:
* **One shift exactly in S:** Iwaniec 1972, Acta Arith. 21, Thm 1. S₁ counts proper representations, so it covers
  p + A ∈ S, with order of magnitude N/(log N)^{3/2}.
* **One shift SOTS plus a second shift almost prime:** Nath–Xie, arXiv:2501.16723 **v3**, final version, Acta
  Arith. Theorem 1.1 reads #{p ≤ x : p = m² + n² + 1, Ω(p + 2) ≤ **9**} ≫ x/(log x)^{5/2}. v1 had 11; `Z55_P415.md`
  cites v1. Their Remark 1.1 gives Ω ≤ 3 under an EH variant.
* **Our Theorem U** (`Z55_P415.md`) has the same shape: N₁ ∈ S exactly, Ω_𝒬(N₂) bounded.
* **Two SOTS shifts with an almost-prime centre:** Sedunova Thm 2: squarefree n with ω(n) ≤ 7 and n ± 2 SOTS,
  ≫ x/log x.
* **Integer analogues are classical:** Indlekofer 1974 and Hooley 1974 give B₂(x) ≫ x/log x; Hooley 1973 gives
  n, n + h, n + k (from secondary sources).

### H2. The obstruction is level of distribution, but the forced parity buys nothing at BV level (Lemma P, new framing)
**What the literature says (verified).** For a sequence whose odd parts are ≡ 1 (mod 4), sifted by 𝒬, the parity of
Ω_𝒬 is fixed by the congruence. Iwaniec, *The half dimensional sieve*, Acta Arith. 29 (1976), Thm 2, read from the page
image, then makes the upper function F an *asymptotic*. The cost is remainders over d < A/Q, i.e. level ≈ (max
element)^{1−ε}. Cor. 2 (2.1) of the same paper: even the one-shift asymptotic for #{p < N : p − 1 SOTS} needs
E(N, N^{1−ε}), which is EH. So, as lit_B and lit_C say, there is no Selberg parity barrier for the *total* Ω_𝒬.

**What I add (§3, Lemma P, PROVED).** Forced total parity gives *no* improvement over the general semi-linear sieve at
Bombieri–Vinogradov level. There is a sequence supported on n ≡ 1 (mod 4) with:
* exactly the natural sieve data (|𝒜_d| = X/d + admissible remainder for all 𝒬-composed d ≤ D = x^{1/2−ε});
* sifted mass realising the lower function f;
* *no element in S*.

The mechanism is a hidden 𝒬-prime above the level. The parity that matters is the parity of the 𝒬-primes *below the
level*, and congruences do not fix it. In the variant whose data are restricted to d | P(z), the hidden prime only has
to exceed z. That variant blocks every level D ≤ x^{1−ε}/z, i.e. up to level ≈ 1/2 + η when z = x^{1/2−η}.

**Reading (Assessment).** An exact S-shift must be produced by non-sieve information. Iwaniec's switching does this, and
it uses the primality of the base variable p. Switching is cheap only for configurations near √x, which requires
sifting that shift to x^{1/2−η}, i.e. spending essentially the whole BV level on it. Hence the budget: **one exact
S-shift per level 1/2.** Two exact shifts cost level ≈ 1, which matches HCKILL Thm E, the P415 level ledger (≈ 0.996)
and FI 2009 (A(θ), θ → 1). This is an accounting of known methods, not a barrier theorem.

### H3. No 2018–2026 parity-breaking or Type II technology applies (lit_C; verified abstracts and theorems)
* **Prime as a number-field norm with a thin coordinate.** Friedlander–Iwaniec a² + b⁴, Heath-Brown–Li, Maynard,
  Pratt, Merikoski (X² + (Y² + 1)², sparse b), Green–Sawhney p² + nq² (arXiv:2410.04189). All are excluded by the P415
  Lemmas A1/A2 (full-family confinement). Green–Sawhney's Gowers-norm Type II also needs a coordinatewise product
  weight, whereas our weight is radial.
* **Average over the shift.**
  * Grimmelt–Merikoski–Pandey–Pascadi, arXiv:2610.41356 (Oct 2026): primes n² + h for almost all h. Abstract read; it
    is the first parity break in a non-factoring thin sequence.
  * Lichtman (shifted-prime Chowla on average); Lichtman–Teräväinen.
* **No prime variable.** The log-averaged and almost-all-scale correlations: Tao–Teräväinen, Helfgott–Radziwiłł,
  Pilatte, Klurman–Mangerel–Teräväinen.
* **Level beyond 1/2.** Every such result needs one fixed integer residue and well-factorable weights:
  * BFI Theorem 10 at 4/7;
  * Maynard at 3/5 (7/12 for linear-sieve weights);
  * Lichtman 66/107, arXiv:2309.08522 Cor. 1.5;
  * Pascadi 5/8, arXiv:2505.00653 Thm 1.3.

  Our moduli d₁d₂ carry the CRT residue (−4 mod d₁, −1/4 mod d₂). Semi-linear β-sieve weights are only *partially*
  well-factorable (Teräväinen arXiv:1611.08585 Lemma 9.2, Remarks 9.3–9.4: exponents 3/7 and 2/5, stated optimal).
* **Polynomial-root residues.** Zhang, Polymath8a Thm 1.1 (1/2 + 7/300) and Stadlmann (1/2 + 1/40) allow such residues
  but need smooth or densely divisible moduli, which does not fit sifting to ≈ √x.
* **The one fixed-shift parity claim.** Lü–Wang–Wu, arXiv:2610.20242 (14 Oct 2026, v1, abstract read), claim
  Σ_{p≤x} μ(p+2) = o(π(x)).
  * Unrefereed. Lit_C's reader judged the Type II step doubtful: it would seem also to give two-point Chowla at all
    scales (Assessment, not a verification).
  * Even if correct, it does not transfer as is. It gives o(π(x)) for a *signed, non-pretentious* function. P(4,15)
    needs a *lower bound* of size π(x)/log x for an indicator, plus level ≥ 3/4 for the companion sieve (§4.3).

### H4. The Siegel-zero route is closed on two counts
* **The inputs are too weak.** Under an exceptional character, the verified prime levels are:
  * Wright arXiv:2609.35950: Thm 3.1, x^{30/59} individually; Thm 3.2, x^{16/31} on average;
  * FI 2003 (via Wright's restatement): q = x^θ with θ < 233/462 ≈ 0.504.

  The Tao–Teräväinen route (arXiv:2109.06291 Thm 1.6, at most two Λ-factors) would need three-point divisor
  correlations, which they say are understood only for k ≤ 2. Merikoski's lower-bound sieve (arXiv:2108.01355 Thm 15)
  would need Type I level > 0.6163 for r(n+4)r(4n+1); only x^{1/12}-type levels are known (FI 2009 Lemma 4.2, det 1).
* **The route may be vacuous.** Banks, arXiv:2610.15483 (Oct 2026), "On the OpenAI proof that Landau–Siegel zeros do not
  exist", abstract read, gives an explicit-constant account of a claimed proof: (1 − β)log q ≥ 3·10⁻³ for all q ≥ 3.
  This is unrefereed, and we do not rely on it; if it is correct, every Siegel-zero-conditional route is vacuous.

### H5. The precise missing estimate (§4.2)
The cheapest formulation of what an FI-type proof of P(4,15) needs is (★K): a Bombieri–Vinogradov theorem at level
x^{1/2−η} for the Titchmarsh-type sequence {r(4p+1)}_p in the classes p ≡ −4 (mod d), with semi-linear sieve weights.
* It follows from EH.
* It was not located in the literature. The verified state of the art for the closest object, r(p − 1) in APs, is
  Dimitrov arXiv:2402.16425 Thm 1, with moduli only up to (log X)^A.
* Opened up, it is a level-≈1 statement for primes in moduli d·e. The CRT residue a_{de} ≡ −4 + 15d·\overline{4d}
  (mod de) carries a Kloosterman-type coupling between d and e.

### Verdict: **narrowed** (literature-calibrated)
The lane gives:
* a source-verified map;
* Lemma P (PROVED, scoped): the forced-parity escape hatch is closed at BV level;
* a precise missing estimate (★K), CONDITIONAL route, Assessment-level sketch.

K(4) unconditional is **known-hard in the practical sense**. It needs EH-strength input under every known method, and
its det-1 analogue has been open since 2009. This is not a theorem that it is hard. No 2018–2026 breakthrough
supplies the missing input.

**Recommendation (Assessment).**
1. Stop spending lanes on exact unconditional K(4).
2. Bank Theorem U, sharpened via Nath–Xie v3-style weights (K4CHEN), plus the EH and Bunyakovsky conditionals.
3. Record K(4) in FRONTIER as "EH-hard, FI-2009 class".
4. Re-open only if (★K), a fixed-shift Type II for the det-15 shell, or a verified Lü–Wang–Wu-type mechanism appears.

---------------------------------------------------------------------------------------------------------------------
## 1. Statements attacked (labels)

* **(T) P(4,15)**, OPEN. Lane question: is it, or a close analogue, known or known-hard?
* **(L) Lemma P**, PROVED, §3: hidden-prime extremality of the semi-linear sieve on parity-forced sequences.
* **(K) (★K) ⟹ P(4,15)**: CONDITIONAL on (★K) and on its switched companion (★K′). The proof is a sketch following FI
  2009 §§6–7 and P415 Theorem U, Step 3 (§4.2), so this is labelled Assessment, not PROVED.
* **(M)** The literature map (§2): verified statements with sources.

**Why not already closed.**
* P415 and HCKILL ran bounded literature checks (`data/z55/p415/lit_report.md`, `data/z54/hckill/lit_report.md`).
* This lane adds the following primary sources:
  * Iwaniec 1972 Thm 1 and Iwaniec 1976 Thms 1–4 / Cor. 2, from page images;
  * FI 2009 §§5–7 mechanism;
  * Sedunova 2026; Nath–Xie v3 (Ω ≤ 9); Dimitrov 2024;
  * the 2026 preprints GMPP, Lü–Wang–Wu and Banks;
  * the level-beyond-1/2 residue analysis;
  * the semi-linear well-factorability limitation.
* Lemma P answers a question the lit reports left open: does the "forced parity" observation by itself help? It
  escapes nothing in the closed list or FRONTIER §6.

---------------------------------------------------------------------------------------------------------------------
## 2. Literature map (verified statements; details and quotes in the three reports)

Each row gives the problem and the best result. "≻ EH" means needs at least EH-type input.

| Problem | Best result | Status | Source |
|---|---|---|---|
| p + A ∈ S (one shift), order of magnitude | ≍ N/(log N)^{3/2} | PROVED (BV + semi-linear sieve + switching) | Iwaniec 1972 Thm 1 (S₁ = proper reps) |
| p − 1 SOTS, asymptotic | conditional | needs E(N, N^{1−ε}) | Iwaniec 1976 Cor. 2 (2.1); Nath–Xie v3 p. 2 "still do not have an asymptotic" |
| p − 1 ∈ S in short intervals | θ ≥ 10/11 | PROVED | Matomäki 2007 Thm 1 |
| r(p − 1) in APs | moduli ≤ (log X)^A only | PROVED | Dimitrov arXiv:2402.16425 Thm 1 |
| Σ_p r(p − a) asymptotic | yes | PROVED | Linnik 1960 (secondary); FI 2009 Thm 5 via BFI Thm 9 |
| p − 1 SOTS & Ω(p + 2) ≤ 9 | ≫ x/(log x)^{5/2} | PROVED | Nath–Xie v3 Thm 1.1 (Ω ≤ 3 under EH-variant, Rem. 1.1) |
| p − 2, p + 2 both SOTS (det 1) | ≍ x/log x weighted | **CONDITIONAL on A(θ), θ → 1**; upper bound unconditional | FI 2009 Thms 2–4; Sedunova 2026; Kontorovich 2014 §3.6.2 ("(conditionally) resolving") |
| n ± 2 SOTS, n squarefree, ω(n) ≤ 7 | ≫ x/log x | PROVED (level x^{1/6} of r(n−2)r(n+2)) | Sedunova 2026 Thm 2; Thm 3: R(θ) ⟹ ≤ ⌊2/θ⌋ factors |
| integers n, n + 1 both SOTS | ≍ x/log x | PROVED | Indlekofer 1974; Hooley 1974 (secondary) |
| integers n, n + h, n + k SOTS | ∞ many | PROVED | Hooley 1973 (secondary) |
| p + 4 ∈ S & Ω_𝒬(4p + 1) bounded | ≫ x/(log x)² | PROVED rel. BV + cited sieve lemmas | Z55_P415 Thm U (internal) |
| **P(4,15)** | — | **CONDITIONAL**: EH(θ₀), θ₀ < 1 (HCKILL Thm E); Bunyakovsky for 720k² + 1 (Thm Q) | internal |
| P₂ values n = 720k² + 1 with both shifts in S | ∞ many | PROVED | Lemke Oliver 2012 Thm 1 + Thm Q (P415 Prop C) |

**Level and parity facts (verified).**
* Iwaniec 1976 Thm 1, sifting limit: f vanishes at s = 1, so β = 1.
* Iwaniec 1976 Thm 2: the asymptotic F when the parity is forced, at level A/Q.
* Iwaniec 1980 ("Rosser's sieve" §2.2): the κ = 1/2 bounds are best possible.
* FI 2009 §6, verbatim:
  > "Since the sieving limit for the semilinear sieve is β = 1 and our level of distribution is D = D(x) < √x, we
  > cannot successfully apply the lower bound sieve to S(A^{(δ)}, P, √x), but we can come close to this"
* FI 2009 §7: "Note that we actually require A(θ) for the sum weighted by a divisor function".

The fixed-residue levels (BFI 4/7, Maynard 3/5 and 7/12, Lichtman 66/107, Pascadi 5/8) and the polynomial-root
residue levels (Polymath8a 1/2 + 7/300, Stadlmann 1/2 + 1/40, smooth moduli) are as in H3.

---------------------------------------------------------------------------------------------------------------------
## 3. Lemma P: the hidden-prime barrier for parity-forced semi-linear sieving (PROVED)

**Setting.** A finite sequence 𝒜 = (a_n)_{n≤x} with a_n ≥ 0. For squarefree d composed of 𝒬-primes put
𝒜_d = Σ_{d|n} a_n and r_d = 𝒜_d − X/d for a parameter X > 0. Here g(d) = 1/d is the natural density of the
integers, and also that of the primes up to the factor φ, which is irrelevant here. Call 𝒜 **parity-forced** if
a_n > 0 ⟹ n ≡ 1 (mod 4); then Ω_𝒬(n) is even. The comparison sequence is 𝒩 = (1[n ≤ x, n ≡ 1 (4)]), with X = x/4,
|r_d| ≤ 1, and #(𝒩 ∩ S) ≍ x/√(log x) (Landau).

**Lemma P.**
* **(a) Full data.** Let 0 < ε < 1/4, x ≥ x₀(ε) and D = x^{1/2−ε}. Put
  a_n := #{q ∈ 𝒬 ∩ (D, 2D] : q | n, n/q ≡ 3 (mod 4)} for n ≤ x, and X := Σ_{q∈𝒬∩(D,2D]} x/(4q). Then:
  * (i) 𝒜 is parity-forced;
  * (ii) a_n > 0 ⟹ n ∉ S;
  * (iii) for every squarefree 𝒬-composed d ≤ D, |r_d| ≤ π(2D), hence Σ_{d≤D}|r_d| ≤ D·π(2D) ≪ X·x^{−2ε};
  * (iv) X ≍ x/log x.
* **(b) Data restricted to d | P(z).** Let x^ε ≤ z and let the hidden primes run over 𝒬 ∩ (z, 2z] instead (with
  X := Σ x/(4q) over them). Then (i), (ii) hold, and |r_d| ≤ π(2z) for all 𝒬-composed d | P(z). Hence
  Σ_{d|P(z), d≤D}|r_d| ≤ D·π(2z), which is ≪ X·x^{−ε}log x whenever zD ≤ x^{1−ε}.

**Consequence (PROVED).** Consider any lower bound Λ(X, D, z) ≤ Σ_{n∈S} a_n that is valid for every parity-forced
sequence with the given main term X·g and with Σ_{d≤D}|r_d| ≤ X x^{−ε/2} (or the restricted data of (b)). Every such
Λ satisfies Λ ≤ 0 in the ranges of (a) or (b). In other words, *sieve data at level ≤ x^{1/2−ε} plus forced total
parity can never certify a single element of S.* The same holds for data restricted to d | P(z) whenever
zD ≤ x^{1−ε}. For P(4,15) this means the following. No argument that uses, for the component N₂, only its
single-component sieve data at these levels plus N₂ ≡ 1 (mod 4) can certify N₂ ∈ S. A fortiori it cannot certify
"both components in S". (A vector example matching the exact joint density h(d₁, d₂) of (p + 4, 4p + 1), which has
h(q, q) = 0, is not constructed here.)

*Proof.*
* **(i)** n = qm with q ≡ 3 and m ≡ 3 (mod 4), so n ≡ 9 ≡ 1 (mod 4) and n is odd.
* **(ii)** q | n and q ∈ 𝒬.
* **(iii)** Let d be 𝒬-composed and squarefree, d ≤ D. Every prime factor of d is ≤ D < q, so (d, q) = 1 and d | qm ⟺ d | m.
  Then 𝒜_d = Σ_q #{m ≤ x/q : m ≡ 3 (4), d | m}. As d is odd, the conditions m ≡ 3 (4), m ≡ 0 (d) define one class
  modulo 4d. So each inner count is x/(4qd) + θ_q with |θ_q| ≤ 1. Summing gives 𝒜_d = X/d + r_d with
  |r_d| ≤ #{q} ≤ π(2D). The number of d is ≤ D, so Σ|r_d| ≤ Dπ(2D) ≤ 2D²/log D = O(x^{1−2ε}/log x) for large x.
* **(iv)** By Mertens in progressions, Σ_{q∈𝒬, D<q≤2D} 1/q = (log 2 + o(1))/(2 log D), so
  X = (x/4)(log 2 + o(1))/(2 log D) ≍ x/log x. Then Σ|r_d|/X ≪ x^{−2ε}.
* **(b)** The same computation applies: d | P(z) has all prime factors < z < q, and |r_d| ≤ #{q ∈ (z, 2z]} ≤ π(2z). Then
  Σ_{d≤D}|r_d| ≤ Dπ(2z) ≤ 2Dz ≤ 2x^{1−ε}, while X ≍ x/log x.

  "Admissible" in (a) means Σ|r_d| ≤ X x^{−ε/2}, which holds for x large since x^{−2ε} = o(x^{−ε/2}). In (b) it
  means Σ|r_d| ≪ X x^{−ε} log x. If z·D ≤ x^{1−2ε}, this is again ≤ X x^{−ε/2} for x large. That is the range stated in
  (b) with ε replaced by 2ε.
* **Consequence.** 𝒜 meets all the hypotheses and Σ_{n∈S} a_n = 0 by (ii). ∎

**Remarks.**
1. **Which function is realised.** The sifted mass of the example is S(𝒜, z) = Σ_q #{m ≤ x/q : m ≡ 3 (4), (m, P(z)) = 1}.
   This is the parity-*odd* model sequence {m ≡ 3 (4)} at parameter s′ = log(x/q)/log z, and it realises the lower
   function: S(𝒜, z) ~ X W(z) f(s′). In range (a), s′ = s(1 + O(ε)) with s = log D/log z, so the lower function f is
   asymptotically sharp *within the parity-forced class*. The natural 𝒩 realises F (Iwaniec 1976 Thm 2).
   * Numerics (EVIDENCE; `scripts/z56_k4lit_lemmaP.py`, `data/z56/k4lit/lemmaP_*.txt`):
     * at x = 10¹² and D = x^{0.45}, S(𝒜, z)/(X W(z)) = 0.5946, 0.7082, 0.8127, 0.9049, 0.9775 against
       f(s′) = 0.5837, 0.6981, 0.8038, 0.8998, 0.9758 for s = 1, 1.1, 1.25, 1.5, 2;
     * at x = 10¹³ and D = x^{0.49}: 0.1279, 0.4732, 0.6724, 0.8257, 0.9455 against f(s′) = 0.1713, 0.4739, 0.6633,
       0.8181, 0.9422, with s′ = 1.01–2.03;
     * the natural 𝒩 (x = 10⁸) gives 1.5052, 1.4351, 1.3463, 1.2290, 1.0643 against F(s) = 1.5059, 1.4358, 1.3469,
       1.2296, 1.0648;
     * sieve data for small d agree to ≤ 10⁻⁵ relative; 𝒜 ∩ S = ∅.

     The worst-case remainder bound D·π(2D)/X = 0.36 and 3.2 at these x is a crude bound. The lemma is asymptotic.
2. **Where the barrier ends.** (a) needs D² < x, since the m-variable (≤ x/D) must equidistribute modulo d ≤ D. It is
   *exactly* the BV level. Above level 1/2 with full data, Iwaniec 1976 Thm 2 shows that the parity-forced sieve becomes
   asymptotic at level A^{1−ε}. Lemma P makes no claim for 1/2 < θ < 1 with full data.
3. **Why switching escapes it.** Iwaniec 1972, Theorem U, Nath–Xie and FI all supplement the sieve data with an *upper
   bound for the switched configurations* N = q q′ m (two large 𝒬-primes). They obtain it by sieving the *prime*
   variable p = N − 4 inside the switched sequence, which uses information about the base sequence (primality) that is
   not in the data. In the example 𝒜 every z-rough element is such a configuration (for z = x^{1/2−η}, with
   m = q′m′, m′ ≤ x^{2η}). So switching is the only non-sieve input in these proofs, and it is cheap only near √x.
   This is the source of the "level 1/2 per exact shift" budget (H2; Assessment).
4. **Novelty.** This is a folklore-type construction: a "pigeonhole" example with a hidden prime. It was not located
   stated in this form for parity-forced κ = 1/2 sieving. It corrects the over-reading "no parity barrier, hence only
   level" in two directions. There is a barrier at BV level, namely the parity of the *small* 𝒬-primes. It disappears
   only at EH level.

---------------------------------------------------------------------------------------------------------------------
## 4. Judgement: methods ranked, and a concrete plan

### 4.1 Ranking (Assessment)

| # | Method | Reaches | Missing input | Probability (subjective) |
|---|---|---|---|---|
| 1 | Chen / Nath–Xie v3 vector sieve + switching + Richert weights (K4CHEN lane) | explicit Ω_𝒬(4p + 1) ≤ K with p + 4 ∈ S | constants audit only | high for a K ≈ 6–10; K = 0 impossible at BV level by H2 budget |
| 2 | FI-template with (★K) (r-weight on N₂, semi-linear on N₁, switching) | exact P(4,15) | (★K) + (★K′): BV at level 1/2 for {r(4p+1)} in p ≡ −4 (d) | very low: (★K) is level-≈1 for primes with Kloosterman-coupled residues |
| 3 | Shell-as-base Harman sieve (det-15 shell; GMPP-type Type II) | exact P(4,15) | Type I R(θ) for r(n+4)r(4n+1) with θ ≥ 1/2 (known: 1/12–1/6 for det 1) **and** a fixed-shift Type II for the shell (GMPP needs averaging over h) | very low; this is the FI hyperbolic-PNT gap itself |
| 4 | Fixed-shift multiplicative cancellation (Lü–Wang–Wu-type, g = i^{Ω_𝒬}) | at best "0 vs 2" discrimination | LWW verified; log-power saving on a sparse set; companion sieve at level ≥ 3/4 (§4.3) | very low |
| 5 | Siegel-zero dichotomy | — | levels ≤ 0.52 available vs ≈ 1 needed; three-point correlations; possibly vacuous (Banks 2026) | ≈ 0 |
| 6 | Algebraic families / prime-value theorems | — | excluded (P415 A1/A2) except Bunyakovsky slices | 0 (unconditionally) |

### 4.2 The best formulation: (★K) and its use (CONDITIONAL; sketch-level, Assessment)
**(★K).** For every A > 0 and fixed small η > 0, with λ_d the upper or lower semi-linear β-sieve weights of level
D = x^{1/2−η} supported on squarefree 𝒬-composed d:
  Σ_{d ≤ D} λ_d ( Σ_{p≤x, p≡1 (8), p≡−4 (d)} r*(4p+1) − g*(d)·𝒳 ) ≪ x (log x)^{−A}.
Here r* counts primitive representations, and g*, 𝒳 are the natural main-term density and mass. **(★K′)** is the
analogue for the switched sequences p = a q′ − 4 with prime q′ (P415 Step 3), needed only at small level x^{1/8}.

**Sketch of (★K) + (★K′) ⟹ P(4,15).** Follow P415 Theorem U with the vector sieve replaced as follows:
* N₂'s component is replaced by the weight r*(N₂). For N₂ ≡ 1 (mod 4) odd, r*(N₂) > 0 iff N₂ ∈ S.
* N₁ is sifted by the semi-linear lower sieve to z₁ = x^{θ₁} with level D, using (★K) as the remainder input.
* Iwaniec switching bounds the two-large-prime configurations in N₁, carrying the weight r*(N₂). An upper bound with a
  divisor-type weight via (★K′), or with r* ≤ r ≤ 4τ and a Landreau-type small-divisor majorant, loses only an
  absolute constant. So the O(η^{3/2}) versus η^{1/2} contest of Steps 4–5 is unchanged.
* The r*-weighted main mass (Σ_{p ≡ 1 (8)} r*(N₂) ≍ π(x)) replaces X·W(z₂). The conclusion is a positive *weighted*
  sum Σ_{p: N₁∈S} r*(N₂) ≫ x/(log x)^{3/2}. That already gives infinitude. By Cauchy–Schwarz with
  Σ_p r*(N₂)² ≪ x(log x)^{O(1)}, it also gives a count ≫ x/(log x)^{O(1)}.

This is FI 2009 §§6–7 with (p − 2, p + 2) replaced by (N₁, N₂). FI's "require A(θ) for the sum weighted by a divisor
function" is exactly (★K) once the divisor sum is opened. *Not checked line by line; Assessment.*

**Why (★K) is hard (Assessment).**
* Opening r*(4p+1) = Σ_{ef=4p+1} χ₋₄(e)·(primitivity) gives primes in classes modulo d·e, with d ≤ x^{1/2−η} and e up
  to √x (after e ↔ f switching): total modulus up to x. Trivially this is A(θ) with θ ≈ 1.
* Read as a statement about primes with factored moduli, the residue mod de is fixed on each factor: −4 mod d and
  −1/4 mod e. The combined class is a ≡ −4 + 15d·\overline{4d}^{(e)} (mod de). This couples d and e through d̄ mod e, so
  no single integer a serves all moduli (BFI, Maynard, Lichtman, Pascadi need one).
* A dispersion attack would meet Kloosterman fractions twisted by 15·\overline{4d}/e at total modulus ≈ x, far beyond
  the Deshouillers–Iwaniec range (≤ x^{5/8} even with a single fixed residue).
* Closest verified result: Dimitrov's BV for r(p − 1), with moduli ≤ (log X)^A.

### 4.3 Why the "0 vs 2" multiplicative route (Lead B of lit_C) needs level ≥ 3/4 anyway (PROVED identity + Assessment)
For odd N ≡ 1 (mod 4) with (N, 𝒬(z)) = 1 and z > N^{1/4}, Ω_𝒬(N) ∈ {0, 2}, and
1_S(N) = (1 + i^{Ω_𝒬(N)})/2 (PROVED: i⁰ = 1, i² = −1). So
  #{P(4,15)-primes ≤ x} ≥ ½ [ Σ_p 1_S(N₁)1[(N₂, 𝒬(z)) = 1] + Σ_p 1_S(N₁)1[(N₂, 𝒬(z)) = 1] i^{Ω_𝒬(N₂)} ],  z = x^{1/4+}.
The first sum needs an exact S-shift (level 1/2, Lemma P) jointly with 𝒬-sifting of N₂ to z > x^{1/4}. The semi-linear
lower bound needs s₂ > 1, i.e. extra level > x^{1/4}, for a total of ≈ 3/4 by the budget of H2 (Assessment). The
second sum needs cancellation of i^{Ω_𝒬} on a sparse set: relative o(1) on a set of density ≍ (log x)^{−1}. That is
stronger than the o(π(x)) a Lü–Wang–Wu-type theorem would give. Two independent hard inputs; ranked low.

### 4.4 Concrete plan (if the campaign wants to keep a K(4) thread alive)
1. **Bank (now).** Theorem U plus the K4CHEN explicit bound. Update the P415 citation: Nath–Xie v3 has Ω ≤ 9, not 11.
   Record in FRONTIER that K(4) is FI-2009-class and EH-hard (text in §6).
2. **Cheap, independent value (optional).** Port FI 2009 Lemma 4.2 / Sedunova Lemma 2 to the det-15 shell: the level
   of distribution of r(n+4)r(4n+1) in APs (Weil bound route, level ≈ x^{1/12}–x^{1/6}). It gives
   "∞ many squarefree n with ω(n) ≤ 7, n + 4 and 4n + 1 SOTS" (Sedunova Thm 2 analogue). **No ES content.** Prop C
   already gives a thin P₂ version with both shifts in S. Low priority.
3. **Watch list (trigger to re-open).**
   * (a) A refereed or independently verified Lü–Wang–Wu. If it holds, test their "C–S in the cofactor → determinant
     equation" Type II on Σ_{p≡−4 (d)} g(4p+1) with g = i^{Ω_𝒬}.
   * (b) A fixed-shift version of the GMPP Type II for binary-form sequences.
   * (c) Any beyond-1/2 prime level allowing residues of the coupled form −4 + 15d·\overline{4d} (mod de).
   * (d) Any unconditional lower bound in FI's det-1 problem: that would almost certainly port to P(4,15).
4. **Do not** spend lanes on: vector-sieve or linear-sieve level optimisation (done in the P415 ledger); Siegel zeros;
   algebraic families; "forced parity" improvements at BV level (Lemma P).

---------------------------------------------------------------------------------------------------------------------
## 5. Verification log (what I checked myself)

* **FI 2009 PDF** (text extraction; archive.ymsc.tsinghua.edu.cn): Assumption A(θ); Theorems 2, 3 and 4; §5 "level of
  distribution D = x^{1/12−2ε}"; §6 "√x suffices because, if n ≡ 1 (mod 4) has one prime factor from P, it must have a
  second one"; the "narrowly misses" paragraph; "we actually require A(θ) for the sum weighted by a divisor function".
* **Iwaniec, Acta Arith. 29 (1976)**, pp. 70–73, page images: Theorem 1 (S ≥ / ≤ with remainders over d < z^s, β = 1);
  Theorem 2 (hypotheses a′ ≡ 1 (4), 𝒫 ⊂ {p ≡ −1 (4)}; remainder over d < A/Q; F asymptotic); Theorems 3–4;
  Corollary 2 (2.1)–(2.3) with E(N, N^{1−ε}) and B(N, N^{1−ε}).
* **arXiv abstract pages** for 2609.28200 (Sedunova), 2610.41356 (GMPP), 2610.20242 (Lü–Wang–Wu), 2610.15483 (Banks):
  titles, authors, dates and abstracts as quoted.
* **Nath–Xie arXiv:2501.16723**: v3 listed, "Final version, published in Acta Arithmetica"; Theorem 1.1 with Ω(p+2) ≤ 9
  and Remark 1.1 (Ω ≤ 3 under EH-variant), from the v3 PDF text.
* **Not checked by me (subagent-verified only):** Iwaniec 1972 Thm 1 (OCR by subagent A); Matomäki 2007; Dimitrov;
  Teräväinen Lemma 9.2; the levels quoted for Lichtman, Pascadi, Maynard, Stadlmann and Polymath8a; Wright; Merikoski
  Thm 15; Tao–Teräväinen Thm 1.6. Per the brief these are pure-research items. The verdict depends on them only
  through "no known level ≥ 0.63 for our residues", which is robust: every listed level is ≤ 5/8.

---------------------------------------------------------------------------------------------------------------------
## 6. FRONTIER §4 hard screens (best items: Lemma P; plan item (★K))

1. **T1 squares.** Kill side, so the screen constrains upper-side proofs. Odd squares m² satisfy both confinements
   (m² + 4, 4m² + 1 are primitive SOTS, P415 §5). Lemma P is a statement about sieve data and is indifferent to squares.
   (★K) concerns primes only.
2. **8/131, 8/241.** K(4) is line-4 specific (HCKILL Lemma 1.1). Nothing here is claimed for other lines.
3. **Tied modulus.** Not applicable (fixed character χ₋₄).
4. **Fixed p.** Everything is a density or infinitude statement. Nothing touches a prescribed prime.

## 7. Proposed FRONTIER text (do not edit FRONTIER here)

> *(z56, `Z56_K4LIT.md`; kill side, K(4) = P(4,15).)* **Literature calibration (verified sources):**
>
> * **Neither P(4,15) nor its det-1 analogue is known unconditionally.** The det-1 analogue is FI 2009 Thm 4,
>   Σ Λ(n)r(n−2)r(n+2) ≍ x, proved only under A(θ) with θ → 1 and re-confirmed conditional by Sedunova
>   (arXiv:2609.28200, 2026).
> * **Closest unconditional results:** Iwaniec 1972 (one shift in S); Nath–Xie v3 (p − 1 SOTS, Ω(p + 2) ≤ 9);
>   Theorem U.
> * **No 2018–2026 parity or Type II breakthrough applies.** Norm-form families are excluded by P415 A1/A2. Other results
>   average over the shift (GMPP 2026). The beyond-1/2 levels need one fixed residue and well-factorable weights, and
>   semi-linear weights are only partially factorable. The Siegel-zero route is too weak (prime levels ≤ 0.52) and
>   possibly vacuous (Banks 2026, unrefereed).
> * **Lemma P (PROVED):** forced parity (odd parts ≡ 1 (4) sifted by 𝒬) gives nothing at BV level. A hidden 𝒬-prime above
>   the level yields a parity-forced sequence with natural level-x^{1/2−ε} sieve data, sifted mass f, and no element in
>   S. Exact S-shifts must come from switching, which costs ≈ level 1/2 per shift (Assessment). Hence two shifts cost
>   level ≈ 1, i.e. EH-hard for every known method.
> * **Precise missing estimate (★K):** BV at level 1/2 for {r*(4p+1)} in p ≡ −4 (mod d). It is level-≈1 for primes
>   with Kloosterman-coupled residues. (★K) + (★K′) ⟹ P(4,15) is an FI-template sketch (Assessment).
> * **Recommendation:** treat K(4) as FI-2009-class (EH-hard); bank Theorem U and the K4CHEN bound; re-open only on
>   (★K), a fixed-shift Type II for the det-15 shell, or a verified Lü–Wang–Wu-type mechanism.

## 8. Bottom line

Unconditional K(4) = P(4,15) is not in the literature. Its closest relative, Friedlander–Iwaniec's prime norms of
SL₂(ℤ) (p ± 2 both sums of two squares), has been proved only under an EH-strength hypothesis since 2009, and was
reaffirmed as such in 2026. The literature's diagnosis is a level-of-distribution obstruction. The half-dimensional
sieve with congruence-forced parity is asymptotic at level ≈ 1 (Iwaniec 1976 Thm 2).

Lemma P shows the forced parity is worthless at Bombieri–Vinogradov level: a hidden 𝒬-prime defeats it. An exact
S-shift therefore has to be paid for by switching, at about level 1/2 each, and two shifts need about level 1. No
recent breakthrough supplies this:
* the norm-form prime theorems are excluded by our confinement lemmas;
* GMPP-type parity breaking averages over the shift;
* the fixed-residue levels stop at 5/8 and do not allow our coupled residues;
* Siegel zeros give ≈ 0.5 and may not exist.

The precise missing input is (★K), a BV theorem for the Titchmarsh-type sequence r(4p+1). Verdict: **narrowed**. K(4)
is EH-hard for every known method, which is a judgement, not a theorem. Bank Theorem U and the explicit Ω bound, and
stop direct attacks. No step toward ES.

## 9. Review log
(pending: internal hostile review)
