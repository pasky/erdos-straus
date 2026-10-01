# Referee report: "Large Erdős–Straus witnesses: Ω-results for the multiplier and slice parameters" (`paper/es-omega-note.tex`)

## Scope

* **Submission.** `paper/es-omega-note.tex` and its PDF (11 pp.), at branch
  `side-agent/pointwise-omega` commit `0e06282`, merged into this worktree.
* **Comparison base.** The reviewed `POINTWISE_OMEGA.md` (rounds 1–2 of
  `reviews/pointwise-omega-review.md`) and POINTWISE_SIZE §11 (Prop 11.2'').
* **Standard.** Hostile journal referee. Statements must be faithful, with no strengthening.
  Labels go in the theorem headers. Cited and proved material must be explicitly separated.
  Proofs must stand alone. Citations must be correct.
* **Compilation.**
  * `pdflatex` ×3 runs clean: 0 errors, 0 warnings, 0 over- or underfull boxes, no unresolved
    references.
  * The committed PDF matches the source (identical `pdftotext`).
  * The only leftover is `% TODO(submission): author metadata` / "Anonymous".

## Recommendation: **MINOR REVISION**

The mathematics is sound and faithful to the reviewed results.

* **Theorem 1.1** is the paper's main result: `W(p) ≥ (log p)^2 exp(−C log log p/log log log p)`
  i.o. It is correctly labelled "Proved modulo Theorem 4.1" (Thorner–Zaman, with the McCurley
  statement), and its proof in §§3–6 is a faithful condensation of the reviewed one.
* **Lemma 3.3 (mass)** is complete as written.
* **Lemma 4.2 (severe character) and Theorem 5.1 (transfer)** are correct as written, but too
  compressed in two or three places for a standalone paper (R7).
* **The parameter count** (§6) is right, apart from one constant slip (R8).
* **§8 (Lemmas 8.1–8.3, Prop 8.4, Cor 8.5, Thm 8.6) and §9 (Lemmas 9.1–9.2, Thm 1.3)** match
  the round-2-verified statements.

The defects are of four kinds:

* two places where the prose strengthens what is proved (R1, R2);
* two unlabelled claims (R3, R4), one of which hides a cited dependency;
* two citation/credit errors (R5, R6);
* proof-detail nits.

None affects a theorem.

## Checks performed

### Statements against the reviewed sources

| Paper | Source | Faithful? |
|---|---|---|
| Thm 1.1 (and its "more precisely") | POINTWISE_OMEGA Thm 5.1 | yes; label correct |
| Lemma 2.1 (atoms) | notes (58.3); my round-1 code check (51.2)⟺(58.3) | yes. The explicit `u_q,v_q,w_q` recipe was checked by hand: for `d≤a` one gets `(0,a−d,d)`, for `d>a` one gets `(d−a,0,2a−d)`. |
| Lemma 2.2, 3.1, 3.2, 3.3 | Fact 1.1, Lemmas 2.1–2.3 | yes |
| Thm 4.1 (TZ) | TZ Cor. 1.4, Rem. 1.5, (1.7), McCurley sentence p. 1 | yes. "Absolute effectively computable" ✓, `x≥q^{12}` ✓, `0<λ<2` ✓, arXiv-version caveat ✓ |
| Lemma 4.2, Thm 5.1 | Lemma 3.2, Thm 4.1 | yes (see R7, R10) |
| §6 | §5 | yes, apart from the constant slip R8 |
| Prop 7.1 | POINTWISE_SIZE Prop 11.2'', with notes Thm 56.1 inlined as step (i) | yes. Re-derived: (i) atom `−4∈𝓡(ℓ)`; (ii) `𝓡(3)={2}`; (iii) `M=3ℓ≡3 (4)`, `−4r≡1 (3)`, `r∤ℓ`; (iv) the sieve over `r≡2 (3)`. Total `T/2+T/6`. |
| Prop 7.2, Hyp 7.3, Thm 7.4 | Prop 6.1, H_MIN, Thm 6.2 | yes. The polylog clause is dropped, which is fine. |
| Lemmas 8.1–8.3, Prop 8.4, Cor 8.5, Thm 8.6 | §8 (round 2) | yes. Lemma 8.1's proof does not even need `p≡1 (24)`. |
| §9: Lemma 9.1, Lemma 9.2, Thm 1.3 | Lemma 9.1, Lemma 9.2 (divisor form), Thm 9.3 | yes. ET is correctly marked "not needed below". |
| Joint W / ck_min statement (end of §8) | Cor 8.2 | yes; label correct |
| Summary of status | — | consistent with the headers |

### Algebra I re-checked independently in this round

* **Identity (1).** With `Ms=nv+u` and `M+1=4uvw`, the common denominator `nsuvw` gives
  `(nv+u+s)/(nsuvw) = s(M+1)/(nsuvw) = 4/n`.
* **Type-I recovery from a divisor (§8).** With `ef=N=p²+4ck²` and `h=4ck`:
  `4abc−1 = p(2p+e+f)/(4ck²)`, so `k(4abc−1) = p(a+b)`.

### Citations

| Reference | Verdict |
|---|---|
| **TZ** | Math. Z. 306 (2024), no. 3, Paper No. 54, per the arXiv listing. Statement checked in the archived v2. ✓ |
| **LW** | Int. J. Number Theory 4 (2008), 423–435, web-verified at worldscientific.com and HAL. Prop 5.1 was read in the archived author preprint, so the published numbering is not checked (R11). ✓ |
| **Chang** | J. Anal. Math. 123 (2014), 1–33, web-verified at Springer. Cor. 11 is present in the archived text. ✓ |
| **ET** | J. Aust. Math. Soc. 94 (2013), 50–105; the archived copy is arXiv:1107.1010v6. Prop 1.4 ("for any A,B>1, k≪(AB)^{O(1)}") ✓. Theorem 1.1, `N log²N ≪ Σ_{p≤N}f(p) ≪ N log²N log log N`, supports "average `(log N)^3` up to `log log N`". ✓ |
| **PW** | arXiv:2511.16817, title ✓. Its Vaughan quote `N/exp(c(log N)^{2/3})` ✓. But the 10¹⁸ verification is credited wrongly (R5). |
| **Vaughan** | Mathematika 17 (1970), 193–198 (as in PW's references). ✓ |
| **McCurley** | J. Number Theory 19 (1984), 7–32 (TZ ref. [10]). ✓ |
| **GR** | Progr. Math. 85, Birkhäuser 1990, 269–309 (as in LW ref. [13]). ✓ |
| **Salez** | arXiv:1406.6307. ✓ |
| **Davenport ch. 14, AS Lemma 5.1.1, HW Thm 317** | standard; not re-checked against the books. |
| **Mordell** | see R6. |

## Numbered defects

**R1 — MEDIUM-LOW (strengthening: necessity claimed, only sufficiency proved).**

* **Location.** Abstract and §1 (paragraph after Thm 1.1).
* **Quotes.**
  * Abstract: "and isolate the exact combinatorial input needed to go further".
  * §1: "beyond it one needs a pointwise 'hypergraph' minorant, and Theorem 7.4 shows that such
    a minorant would suffice".
* **Problem.** Thm 7.4 proves only H_min(θ) ⇒ exponent `1/θ`. Neither necessity nor exactness
  is shown. The source says "What would suffice" (§6.2).
* **Fix.** Use "and isolate a purely combinatorial hypothesis that suffices to go further", and
  "beyond it a pointwise ('hypergraph') minorant is needed for this route; Theorem 7.4 shows such a
  minorant suffices".

**R2 — MEDIUM-LOW (strengthening: "by this route" dropped).**

* **Location.** §7.1, after Prop 7.1.
* **Quote.** "With Chang's theorem this gives the previous record `W≥(5/8−ε)log p`, and no
  complete certificate can do better than linear."
* **Problems.**
  * (a) Prop 7.1 bounds `log Q`, not `p`. A class `c≠1 mod Q` may contain primes far below Q.
    POINTWISE_SIZE §11.1 says so explicitly ("A certificate class other than c=1 could, however,
    contain a prime below Q") and concludes only "no complete certificate does better than 5/8
    *by this route*".
  * (b) The record does not come from Prop 7.1. It comes from the class of one modulo `L*(T)`,
    from `log L*=(2/3+o(1))T`, and from Chang.
* **Fix.** "The class of one modulo `L*(T)` together with Chang's least-prime bound gives
  `W≥(5/8−ε)log p` i.o. By Proposition 7.1, no complete certificate does better than linear when
  its prime is supplied by a least-prime theorem (which bounds `log p` by `O(log Q)`)." If the
  5/8 record is kept as background, either give its 3-line proof (which needs `log L*(T)`) or
  label it as known from companion work.

**R3 — LOW (unlabelled claim).**

* **Location.** §7.3, last paragraph.
* **Quote.** "plain event-level Bonferroni truncation over the raw atom list fails: … so the
  truncated mean is negative for `4.2θ²(log T)²≲J≤T^θ`."
* **Problem.** This is POINTWISE_OMEGA Prop 6.3 (PROVED there). Here it is an unlabelled
  assertion with a one-clause sketch. That violates the paper's own convention ("Every theorem
  header carries a label").
* **Fix (either).**
  * Promote it to "Proposition (Proved)" with the 6-line proof: r primes `≡1 (4)` and r primes
    `≡3 (4)` in `(y,2y]`, `n≡−4`, `N≥r²≥2J−1`, probability `≥(2y)^{−2r}`,
    `C(2J−2,J−1)≥4^{J−1}/(2J−1)`, threshold `(2√2θ/log 4)²`.
  * Or mark it as a remark "(proof sketch)".

**R4 — LOW (unlabelled claim with a hidden cited dependency).**

* **Location.** §9, last paragraph.
* **Quote.** "A congruence saving *uniform in a fixed prime* (the per-prime analogue of
  Lemma 3.3) would, by the local lemma, give `log(1/δ*(T))≤(log T)^{O(1)}`."
* **Problem.** This is POINTWISE_OMEGA Thm 9.4. Its polylogarithmic conclusion needs the global
  polylog mass from Elsholtz–Tao Prop 1.4. Without it, `exp(−4S_tot)` is only `exp(−T^{o(1)})`
  (round 2, R2-1). The required hypothesis is also the precise relative one,
  `w_ℓ ≤ log z/(8 log T)`, not the vague "congruence saving". The paper even says ET "is not
  needed below", which is true for Thm 1.3 but not for this sentence.
* **Fix.** State it as a Remark: "If `w_ℓ(T,z)≤log z/(8 log T)` for all primes `z<ℓ≤T`, with
  `z=(log T)^C`, then by the local lemma and [ET, Prop. 1.4]
  `log(1/δ*(T))≪(log T)^{max(C+1,4)+o(1)}`."

**R5 — LOW (credit).**

* **Location.** §1, first paragraph.
* **Quote.** "it has been verified for `n≤10^{18}` (\cite{PW}, §6; \cite{Salez} for `10^{17}`)".
* **Problem.** PW §6 reads: "verified up to 10^17 by Salez [11], and this was recently improved
  to 10^18 by Mihnea–Dumitru [7]".
* **Fix.** Cite S. Mihnea and B. C. Dumitru, *Further verification and empirical evidence for
  the Erdős–Straus conjecture*, arXiv:2509.00128. It is archived as
  `sources/lit2026/arxiv-2509.00128.pdf`.

**R6 — LOW (citation detail).**

* **Location.** The bibliography entry `\bibitem{Mordell}`.
* **Quote.** "L. J. Mordell, Diophantine Equations, Academic Press, 1969, Chapter 30."
* **Problem.** Elsholtz–Tao (ref. [44]) cite this book as "volume 30 of Pure and Applied
  Mathematics". "Chapter 30" looks like a conflation with the series volume number.
* **Fix.** Use "Pure and Applied Mathematics 30, Academic Press, 1969", with the page range of
  the Erdős–Straus discussion checked against the book. ET also credit the mod-840 classification
  jointly to Obláth (Mathesis 59 (1950), 308–316), so consider adding that.

**R7 — LOW (proof completeness of Theorem 5.1, the paper's main engine).** The following steps
are asserted without their one-line reasons.

* **(a) Case A.** "`λ_*>0`". The reason is `log x>2` and `β*>1/2`, which give
  `x^{β*−1}/β*<1`. The proof should also note that λ is common to all i by Lemma 4.2's second
  claim.
* **(b) Case B.**
  * The formula `λ_i=1−ψ(b_i)x^{β*−1}/β*` needs
    `χ*(a_i)=χ*_Q(a_i)χ*'(a_i)=χ*_Q(1)ψ(b_i)`.
  * The equivalence "`q*|q_i ⟺ q*'|d_i`" needs `q*_Q|Q`. That is automatic, because a severe q*
    divides some `Qd_j` and `gcd(d_j,Q)=1`.
  * `|μ_ψ|` is controlled by the twist condition precisely because ψ is real primitive, with
    conductor `q*'>1` coprime to Q and dividing some `d_i`. Say so.
* **(c) The prefactor.** `Σc_iθ(x;q_i,a_i)=(x/φ(Q))Σc_iλ_i(1+ε_i)/φ(d_i)` uses
  `φ(Qd_i)=φ(Q)φ(d_i)`, i.e. `gcd(Q,d_i)=1`.
* **(d) The range.** `x≥Z^{12}` requires `C_1≥12`.

Four or five added lines suffice. The mathematics is right (round 1, §2).

**R8 — LOW (constant slip).**

* **Location.** §6, "Twist".
* **Quote.** "`|μ_ψ|≤V/15+e^{−15S}≤μ/4`".
* **Problem.** With `μ≥0.99V≥0.99e^{−2S}`, the second inequality needs `e^{−13S}≤0.18`, i.e.
  `S≥0.14`. The source has `e^{−15S−6}`, which works for all `S≥0`.
* **Fix.** Restore the `−6`. Alternatively, note that `S≥(½log 2+o(1))`, from the class `−4` at
  the primes `ℓ≡3 (4)` in `U`.

**R9 — LOW (scope of the numerics; round-1 D8 carry-over).**

* **Location.** Remark 3.4: "Numerically `S≈6.5, …, 38.5` … (with `y=√T`)".
* **Problem.** The paper does not say that this parameter does not instantiate the theorem:
  * at `y=√T`, `max g = 0.08–0.33 > 1/16`, and the twist condition actually fails (ratio 0.267
    at T=10⁴);
  * the theorem's `y=√T·exp(3𝓛/log𝓛)` exceeds T unless `log T>e^6≈403`.
* **Fix.** Add one sentence: "These values illustrate S only; Lemma 3.2's `g≤1/16`, and hence
  Theorem 1.1, is asymptotic (U is empty unless `log T>e^6`)." POINTWISE_OMEGA already carries
  this caveat.

**R10 — NIT.** Lemma 4.2, third claim: "If no severe pair has `q*|q`" should read "If
`q∈𝒬` and no severe pair has `q*|q`". The proof uses that severity is relative to `𝒬`.

**R11 — NIT (Thm 8.6 citation).**

* LW phrase `P_y` via `χ_p(q)=1`, where `χ_p=(p/·)_K`. Add the translation: for
  `p≡1 (4)`, `χ_p(q)=(q/p)` (reciprocity; LW note `χ_p(2)=(2/p)`).
* State that "Prop. 5.1" refers to the numbering of the author preprint (archived), since the
  IJNT numbering was not compared.

**R12 — NIT.**

* Cor 8.5: "B is periodic modulo some L". Take L divisible by the modulus of the given class
  (hence by 24), so that Prop 8.4 applies.
* Thm 1.2(a): "supported on primes with `n_p>T`" should read "on large primes".

**R13 — NIT (wording, unlabelled numerics).**

* §1 says a congruence proof "would contradict the usual random model for `n_p`". A heuristic
  cannot be contradicted; use "would exceed the random-model prediction
  `max_{p≤x}n_p≍log x log log x`".
* §1: "Numerically `log(1/δ*(T))` grows like a small power of `log T`" is unsourced EVIDENCE
  (heavy-tailed Monte Carlo). Either cite the computation or drop it.

**R14 — NIT.**

* §1/§8 say "the slice is positive iff `M_{c,k}(p)>0`", but only "if" is shown (the `a,b`
  formula in §8).
* The converse is two lines: put `e=ha−p`, `f=hb−p`; then
  `ef=16c²k²ab−4ck·k(4abc−1)+p²=N` and `e≡−p (h)`. Add it, or write "if".
* Also give the one-line check `k(4abc−1)=p(a+b)` for the displayed `a,b`, which I verified.

**R15 — NIT.**

* Proof of Thm 1.3, "Good pairs": add the LLL check.
  `Σ_{E'∼E}x_{E'} ≤ 2(w'_{ℓ_1}+w'_{ℓ_2}) = T^{−3ε+o(1)}`, so `∏_{E'∼E}(1−x_{E'})≥1/2` for
  large T. Also justify that μ′ is a product measure: it is Haar conditioned on a product set.
* "Every rough part is `ℓ, ℓ², ℓ_1ℓ_2`": add "(as `y³>T`)".

**R16 — NIT (intro background).**

* **Quote.** "the class of one (every prime `p≡1 (mod lcm{M≤T})` has `W(p)>T`) together with
  Linnik's theorem shows `W(p)≫log p` … with Chang's least-prime bound … the constant becomes
  5/8".
* **Problem.** 5/8 needs the smaller modulus `L*(T)=lcm(24, M≤T, M≡3 (4))`, with log
  `(2/3+o(1))T`. With `lcm{M≤T}` (log ≈ T), Chang gives only 5/12.
* **Fix.** Say "modulo `lcm{M≤T, M≡3 (4)}`".

**R17 — HOUSEKEEPING.** Remove `% TODO(submission): author metadata` and fill in the authors and
date before submission.

## Summary for the editor

The note proves what it claims, under the stated citations. The central novelty is correct, and I
verified it twice at full detail (rounds 1–2 of `reviews/pointwise-omega-review.md`):

* the congruence saving `m|r+k` (Lemma 3.3);
* the Siegel-zero-proof Linnik-range transfer via Thorner–Zaman's λ-scaled error (Lemma 4.2,
  Thm 5.1).

Required before acceptance:

* remove the two strengthenings, R1 and R2;
* label or prove the two unlabelled claims, R3 and R4 (R4 must mention Elsholtz–Tao);
* fix the credit R5 and the reference R6;
* add the short proof details R7 and fix the constant R8;
* add the scope sentence R9.

The remaining items are optional polish.
