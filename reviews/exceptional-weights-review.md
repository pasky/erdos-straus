# Hostile review R81 of EXCEPTIONAL_WEIGHTS.md (O81, branch side-agent/weights-below-one)

Reviewer: R81 side agent (branch side-agent/review-weights). Round 1.
Scripts (from scratch, none of the author's code reused): `scripts/review_weights_*.py`.

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Lemma 1.2 | SOUND (checked numerically, primal/dual brackets overlap) |
| Thm 2.1 / Lemma 2.0 | SOUND (constants re-derived; brute-force LP chain holds with ≥ 8× slack) |
| Cor 2.2 (incl. "iff (W)") | SOUND-AFTER-REPAIRS (iff is literally right per family and up to C ↔ C′; (W) must name its family class — D1) |
| Lemma 3.1, 3.2 | SOUND (brute force: Lemma 3.2 holds with slack ≥ 21×, all F for ℓ ≤ 31) |
| Thm 3.3 | SOUND as stated; SOUND-AFTER-REPAIRS for the "ℛ(ℓ)-slices" gloss (D2) |
| Lemma 4.1, 4.2 | SOUND (one regularity hypothesis on Φ̂ to make explicit — D5) |
| Prop 5.1 | SOUND-AFTER-REPAIRS ((a): `E(N) ≤ M(N)` not literally proved — D3; upper bound shift-uniform: yes, for the 3/4-note family only — D1) |
| Rem 6.1 | SOUND |
| §5.1 EVIDENCE | SOUND (independently reproduced at N = 300) |
| §0 table / labels | SOUND-AFTER-REPAIRS (D1–D4 wording) |

**Overall: no FATAL defect. One MAJOR (D1: the open question (W) and the "iff" are
family-dependent and the document never fixes the family; one sentence asserts an upper
bound for a family the 3/4 note does not treat). The rest MINOR.**

## Detailed checks

### Lemma 1.1, Lemma 1.2 (SOUND)
* 1.1: `Σ_n Ψ(n)ν(n+t) = Σ_θ ν̂(θ)e(tθ)Ψ̌(θ)` and `Ψ ≥ 1_{[1,N]}`, `ν ≥ 0` on ℤ: correct.
  The θ = 0 term needs `w(0) ≥ Ψ̌(0) = ΣΨ ≥ N`, which `w ≥ |Ψ̌|` gives.
* 1.2: Parseval normalisation `Σ_{n mod Q} gν = QΣ_θ ĝ·conj(ν̂)` is right; the equality
  case gives a real g because w is even and ν real; Sion applies with G compact convex
  and `{ν ≥ 1_𝒜}` convex; attainment of the min uses `w(0) > 0`. Verified numerically
  (`scripts/review_weights_thm21.py`): primal `min Σ|W_N||ν̂|` and dual `max⟨g,1_𝒜⟩`
  computed by independent polygon-LP brackets overlap on 10 toy systems (Q = 60, 90).

### Lemma 2.0, Theorem 2.1 (SOUND)
Re-derived line by line:
* Selberg/Beurling majorant `Φ_K(x) = ½[B(Kx) + B(K(1−x))]` (B = Beurling's function):
  numerically Φ ≥ 0, Φ ≥ 1 on [0,1], ∫Φ = 1 + 1/K to 5 digits (K = 1,2,3).
* Poisson: `W_N(θ) = Σ_k NΦ̂(N(k−θ))`; supp ⊂ `‖θ‖ ≤ K/N`, `W_N(0) = N(1+1/K)`. Numerically
  off-band |W_N| ≤ 3·10⁻⁹ (truncation), W(0) exact, and `max|W_N| = W_N(0)`.
* `k̂_δ = (1 − |ξ|/δ)_+`; `v̂ = 1` on |ξ| ≤ δ, 0 for |ξ| ≥ 2δ; periodisation equals 1 on
  `‖θ‖ ≤ δ` needs only δ ≤ 1/3 (author has δ ≤ 1/4). `|v| ≤ 2k_{2δ} + k_δ ≤ 5δ` and
  `≤ 2δ(πδx)⁻²` (so the stated envelope holds with room: numerically max ratio 0.60).
* Block sum: `5δM(L)(2 + 2·(1/6)) = (35/3)δM(L) ≤ 12δM(L)`; blocks j ≤ −2 use
  `|x| ≥ (|j|−1)L` — correct. Numerically the worst block-sum ratio is 0.52.
* `Σ_r g(r) = Qĝ(0) ≤ W_N(0)`; `12δN(1+1/K) = 12(K+1)`. Correct.
* Brute force (`scripts/review_weights_thm21.py`, 30 toy sets: random densities 0.3/0.05,
  one block, AP step 7, single point; (Q,N,K) ∈ {(60,12,1), …, (240,40,4)}): with the
  true |W_N| weights, `M(N) ≤ D ≤ RELAX ≤ 12(K+1)M(⌈N/K⌉)` in every case, where RELAX is
  the LP keeping only what the proof uses (g ≥ 0, band, mass). Observed `D/M(N) ∈ [1.09,
  1.58]`, `RELAX/(12(K+1)M(L)) ≤ 0.114`. The constant 12(K+1) is generous but correct;
  the (K+1) growth is real (single-point set: RELAX ≈ 1.05(K+1)).

### Corollary 2.2, Prop 5.1(c): is "iff (W)" literally right? (yes, per family)
For a **fixed** finite family 𝔊 (avoider set 𝒜) and fixed K: write V(N) for the Φ_K optimum.
Thm 2.1 gives `M(N) ≤ V(N) ≤ 12(K+1)M(N)`. Hence
* cap with constant C (`V(N) ≥ Ne^{−C(log N)^{3/4}}`, N ≥ N₀) ⇒ `M(N) ≥ Ne^{−C(log N)^{3/4} − log 12(K+1)}`
  ⇒ (W) with any C′ > C for N ≥ N₀′;
* (W) with C′ ⇒ `V(N) ≥ M(N)` ⇒ cap with C = C′ (and, by Lemma 1.1, the cap for every
  window/weight ≥ |Ψ̌|).
Both directions are right; the equivalence is "∃C" ↔ "∃C′". Prop 5.1(c)'s
"every translation-invariant per-frequency method is capped ⇔ (W)" is also right (⇒ via
the Φ_K member of "every"). The "escape" direction is vacuous as a *method*: if M(N) is
small then the exceptional count is already ≤ M(N) (up to D3), so the band-limited bound
only certifies M(N); the author says this ("not a door about Fourier analysis"). Fine.
The real problem is that 𝔊 = 𝔊_N is never fixed — see D1.

### Lemmas 3.1, 3.2 (SOUND)
* 3.1: `Σ_{θ∈Θ_S} m_S(θ)e(Nθ) = Π_ℓ g_ℓ(N)` by the CRT product structure (all h_ℓ ≢ 0, so
  θ ≠ 0); `|sin x| ≥ sin²x`. Correct. Numerically `M_S/[(1/2)A_S(1−|Πφ|)] ≥ 2.00` on 400
  random 1–3-prime systems (w = |S_N|) — the inequality holds with factor 2 to spare.
* 3.2: μ(B) ≤ #B·p/a_ℓ with `#B ≤ 2ηℓ` (h ↦ 2Nh bijective), `a_ℓ ≥ Σ|1̂|²/max|1̂| = 1−p`,
  `1−|cos πx| = 1 − cos(π‖x‖)` and `1−cos y ≥ 2y²/π²`. All correct.
  Brute force (`scripts/review_weights_lemma32.py`): **all** F ∋ 0 (translation invariance of
  |1̂_F|) with p ≤ 1/4, all N ≢ 0, for ℓ ≤ 31 and up to C(ℓ−1,k−1) ≤ 7·10⁵ beyond, plus 2·10⁴
  random F per (ℓ,k) up to ℓ = 61: min `(1−|φ|)/(9/(256k²))` = 21.3 (attained at small k).
  Observed `1 − |φ| ≥ 0.50` in every case; the k² loss is a proof artefact (heuristically
  the truth is ≫ 1/log k, e.g. F an interval), harmless for Thm 3.3.

### Theorem 3.3 (SOUND as stated)
Re-derived the weight change through NC Prop 2.1 / Thm 2.3 / Cor 2.5:
* Expansion `R_w(ν) = Σ_S |d_S| M_S^w` with `d_∅ = Eν`, `M_∅ = w(0) = N`: correct for Q₀ = 1
  (ŷ_ℓ = 1̂_{F_ℓ} off 0; CRT product; Θ_S disjoint).
* Existence of good ℓ₀ ∈ S, ℓ₀ ∤ N: `s_ℓ < log ℓ` for every ℓ (good: log(ℓ/2k³); bad:
  log(ℓ/2k)), bad primes contribute ≤ B₁, so `Π_{good∈S} ℓ > e^{λ−B₁} ≥ N`, and distinct
  primes all dividing N would have product ≤ N. ℓ₀ ≥ 5 since 4k ≤ ℓ. Correct.
* `e^{−s_ℓ} = 2p_ℓk_ℓ²` (good), `= 2p_ℓ` (bad) ⇒ `e^{−s(S)} ≥ k_{ℓ₀}² Π_S 2p_ℓ` **because ℓ₀
  is good** (this is why ℓ₀ must be chosen good — the proof does so). Then
  `Π_S 2p(1−p) ≤ A_S Π_S 2p ≤ (512/9c₀) M_S^w k₀²Π2p ≤ (512/9c₀)M_S^w e^{−s(S)}`; r₀ via
  `p ≤ (4/3)p(1−p)` (p ≤ 1/4). Numerically the per-S inequality holds with ≥ 56× slack.
* ET Prop 2.4 (checked in EXCEPTIONAL_THETA §2.3) needs only `s_i ≥ s_*`, `p_i ≤ 1/4` for
  `s_i ≤ λ`; no link between s_i and p_i — so the new weights are legitimate.
  `G = ⌊log₂(λ/s_*)⌋+1 = O(log λ)`.
* Φ̄: `e^{−αs_ℓ} ≤ 2^α ℓ^{−α(1−3γ)}` (uses |F_ℓ| ≤ ℓ^γ); `s_ℓ ≤ λ` ⇒ `ℓ ≤ (2e^λ)^{1/(1−3γ)}`
  (author's `e^{λ+s_*}` is a harmless overestimate); truncated mass via `ℓ^{−1/log X} ≥ e^{−1}`
  ≪ λ³; bad primes `≤ B₁/log 5` terms. With α = λ^{−1/4}: Φ̄ ≤ Cλ^{3/4} + O(log²λ).
* Final step: λ = 2log(4N) + log(512/9c₀) + B₁ gives `ε^w ≤ e^{−B₁}/(16N) ≤ e^{−Φ̄}/4` for N ≥ N₀.
* Constants: C₉ depends on γ, C_M, B₁, c₀ and the fixed s_* — none on N. (M) is a mass
  hypothesis of the usual ET type, not the conclusion in disguise (no circularity).
* Every hypothesis is used: p ≤ 1/4 (Prop 2.1, r₀, ℓ₀ ≥ 5), w(0) = N (main term),
  c₀ (Lemma 3.1), γ < 1/3 (Φ̄ and boundedness of bad primes), B₁ (good-prime product),
  Q₀ = 1 (product structure of ν̂ on Θ_S), hit-pattern (shape of ν̂ on Θ_S).
Scope issue: see D2.

### Lemmas 4.1, 4.2 (SOUND)
* 4.1: Selberg minorant T of the arc, degree H = ⌈N/c⌉−1; `|T̂(k) − 1̂_arc(k)| ≤ 1/(H+1) ≤ c/N`
  (Montgomery, Ten Lectures Ch. 1 — from memory, standard); `T ≤ 1_arc` gives
  `P(‖X_S‖ ≤ c/N) ≥ E T(X_S) = Σ T̂(k)Πφ_ℓ(k) ≥ c/(2N)`. Correct.
* 4.2: Fejér at x₀ ∈ F, H′ = ⌈cℓ/N⌉ ≥ 2|F| ⇔ ℓ ≥ 2|F|N/c; `(H′−|F|)/ℓ ≥ c/(2N)`;
  `a_ℓ ≤ (ℓ·p(1−p))^{1/2} ≤ √|F|`. Correct.

### Prop 5.1 (upper bound and uniformity in t)
The only result giving `M(N) ≤ Ne^{−c(log N)^{3/4}}` is the campaign's own 3/4 note
(`paper/es-threequarter-note.tex`, Thm "critical-window assembly", eq. (transfer)); no
external result is involved. I checked that it is shift-uniform: ν_X = S_y·Q_r(H_X) is
≥ 0 on all of ℤ (the identity for binom(H_X(n), j) holds for all integers n; Bonferroni
Q_r(h) ≥ 1_{h=0} for integer h ≥ 0), ≥ 1 on 𝒜_X := {S_y = 1, H_X = 0}, and the transfer step
uses only "#{n in a window of length N, n ≡ a (q)} = N/q + O(1)", valid for every window.
So `M_{𝒜_X}(N) ≤ Ne^{−c_a t³} + e^{C_L t⁴}` uniformly in the shift, with t = α(log N)^{1/4},
X = e^t. **But only for this family 𝒜_X** (selector + multiplier classes mod kℓ, k ≤ K);
see D1, D3. (b), (d) re-derived: correct (gap of ≥ N on the cycle since
`(ℓ−k)/k ≥ N`; greedy averaging; final step `|X′||F_ℓ| < ℓ`).

### §5.1 EVIDENCE (reproduced)
`scripts/review_weights_translate.py 300` (own code): family size 1633, 664 dense primes,
random translates 1.11·10⁻³ (saving 12.50), t = 0 count 19 (2.76), Montgomery–Vaughan large
sieve 154.7 (0.66) — all identical to the table. My own coordinate-ascent (exact
survivors first, smoothed 0.3^{#kills} tiebreak, 3 restarts) found **31** survivors (saving
2.27), slightly better than the author's 28. Prop 5.1(d) greedy gives only 8 here.
Conclusion of §5.1 ("near the sieve scale, says nothing about exponents") is fair.

### Remark 6.1 (SOUND)
`Qĝ = Qĝ₁·conj(S_N)/N`, admissible for |S_N|; dual identification and the feasible
constant `ν ≡ M(N)/N` are correct; the same holds with `|Qĝ₁| ≤ N` off 0.

## Defects

**D1 (MAJOR) — (W), Cor 2.2(b,c), Prop 5.1(a,c), §0 rows "Thm 2.1, Cor 2.2" and "(W)": the
family is never fixed.** M(N) = M_𝔊(N) depends on the finite family 𝔊 = 𝔊_N, and is
*decreasing* under enlarging 𝔊. The "iff" of Cor 2.2 is a per-family statement; "the door
is capped" for a *method class* needs (W) **uniformly over the families that methods may
use**, i.e. for the largest admissible family. The document alternates between
(i) "the forced-class families" (undefined), (ii) "the families of the 3/4 note" (Prop
5.1(a): 𝒜_X with X = exp(α(log N)^{1/4}), a specific, deliberately small family), and
(iii) Q₀ = 1 ℛ(ℓ) prime slices (§2 "What M(N) is", §5.1). Concretely:
* §2, end of "What M(N) is": "The upper bound M(N) ≤ N exp(−c(log N)^{3/4}) holds (the 3/4
  note's bound is shift-uniform)" sits in the ℛ(ℓ) prime-slice (Q₀ = 1) paragraph. The 3/4
  note does not treat that family (its classes are mod kℓ with multipliers and a selector);
  for the k = 1, primes-only family the mass is a smaller power of log (the author says
  so in §5), so its natural sieve-limit exponent is B/(B+1) < 3/4 and neither the upper
  bound nor the 3/4 scale in (W) is the right benchmark there. Unsupported as placed.
* Cor 2.2(c): "would cap every per-frequency bound … for every family" — a lower bound for
  M_𝔊(N) caps only methods using 𝔊 (or subfamilies of it).
*Repair:* define (W_𝔉) for an explicit class 𝔉 of families (e.g. all finite families of
ℛ(M)/Case-A/selector classes with moduli ≤ N^A, A fixed), as
`min_{𝔊∈𝔉_N} M_𝔊(N) ≥ Ne^{−C_A(log N)^{3/4}}`; restate Cor 2.2(b)/(c) and Prop 5.1(c) per
family and the "door" statement with (W_𝔉); restrict the §2 upper-bound sentence to 𝒜_X;
for the Q₀ = 1 ℛ(ℓ) toy say explicitly which exponent is the benchmark.

**D2 (MINOR) — Thm 3.3, gloss "(M) true for ℛ(ℓ)-slices" and §0 row.** The theorem assumes
`p_ℓ ≤ 1/4` for **all** ℓ (Prop 2.1/ET Prop 2.4 and the r₀ step need it, bad primes
included). Q₀ = 1 ℛ(ℓ)-slices violate it: |ℛ(ℓ)|/ℓ = 1/3, 3/7, 3/11, 9/23, 13/47 for
ℓ = 3, 7, 11, 23, 47 (computed). Dropping those primes is not WLOG (a majorant for the
full family need not majorise the smaller family's larger avoider set). *Repair:* either
state the ℛ(ℓ) application for ℓ ≥ ℓ₀ only (toy family without small primes), or extend
Thm 3.3 to Q₀ > 1 with c-independent F_ℓ: then `ν̂(a/Q₀ + Σh_ℓ/ℓ) = D_S(a)Π1̂(h_ℓ)` with
`D_S(a) = Q₀⁻¹Σ_c d_S(c)e(−ac/Q₀)`, Lemma 3.1 becomes `1 − Re e(Na/Q₀)Πφ_ℓ(N)` (same
anti-concentration from ℓ₀), and `|d_S(c)| ≤ Σ_a|D_S(a)|`; this looks routine but must be
written out (the ES families have c-dependent F_ℓ(c), which this does not cover).

**D3 (MINOR) — Prop 5.1(a) "E(N) ≤ M(N)" (also §0 row, §5 bullet).** The proof gives only
`#(𝒜∩[1,N]) ≤ M(N)`. The 3/4 note's ν_X is ≥ 1 on exceptional **primes > max(K,y)**; E(N)
counts all exceptional n ≤ N (composites, n = 1, primes ≤ max(K,y) with K growing with N),
and membership of these in 𝒜_X is not shown. *Repair:* write
`E_pr(N) ≤ K + y + M_{𝒜_X}(N)` (and E(N) via the note's Rankin step), or prove
exceptional ⇒ ∈ 𝒜_X for the integers in question. Nothing downstream changes.

**D4 (MINOR) — wording/labels.** (a) §2 and §0 Verdict: "No arithmetic-free argument can
cap it" is an Assessment, not a theorem: what is PROVED is that the cap is *equivalent* to
the arithmetic statement (W). Label it Assessment. (b) §0 row Thm 2.1: "best per-frequency
bound lies in [M(N), 12(K+1)M(N)]" — add "for the window Φ_K, per family". (c) The
constant could be stated as (35/3)(K+1); 12 is fine.

**D5 (MINOR) — §4 preamble, "|W_N(θ)| ≥ N/3 for ‖θ‖ ≤ c_Φ/N, N ≥ N_Φ".** Continuity of Φ̂ at
0 and integrability do not control the aliases `Σ_{k≠0}NΦ̂(N(k−θ))`; one needs e.g.
`|Φ̂(ξ)| ≪ |ξ|^{−1−η}` (then the aliases are O(N^{−η})). *Repair:* add that hypothesis (all
windows of interest, Schwartz or Φ_K, satisfy it).

**D6 (MINOR) — Lemma 3.2 is very lossy.** Not a defect of correctness; noting that the
observed `1−|φ| ≥ 1/2` on all tested F suggests a k-free (or ≫ 1/log k) bound (unproved; heuristic only), which would let
Thm 3.3 use weights `log(1/(2p_ℓ)) − O(log log ℓ)` and weaken γ < 1/3. Optional.

## Repairs applied (by the reviewer, at the parent's request)

The author's context was exhausted, so I applied the repairs on this branch. I first merged
`side-agent/weights-below-one`, which was already up to date. Every change in
`EXCEPTIONAL_WEIGHTS.md` and `AGENT_REPORT_O81.md` is marked "(R81 repair, applied by
reviewer)". There is one commit per defect.
* **D1** — new "Families" paragraph after the Notation. It defines 𝔊_X (the 3/4-note
  family), 𝔊_ℛ (the Q₀ = 1 ℛ(ℓ) toy family) and 𝔉_A (all forced-class families with moduli
  ≤ N^A), together with (W_𝔊) and (W_{𝔉_A}). The following are now stated per family:
  the §0 rows for Thm 2.1, Prop 5.1 and (W); Cor 2.2(b),(c); Prop 5.1(a),(c); and Open
  problem (W). The §2 sentence about the upper bound is restricted to 𝔊_X. The report is
  updated to match.
* **D2** — the application to ℛ(ℓ) is restricted to primes ℓ ≥ ℓ₀. Here ℓ₀ is chosen so
  that p_ℓ ≤ 1/4 and |ℛ(ℓ)| ≤ ℓ^γ, and ℓ₀ ≥ (2e^{s_*})^{1/(1−3γ)}. A new scope paragraph
  after Thm 3.3 lists the violating primes 3, 7, 11, 23, 47. The Q₀ > 1 extension is
  explicitly **not claimed**, since it was not written out. Updated in the §0 row, in
  "What this closes" and in the report.
* **D3** — new Prop 5.1(a′): `E_pr(N) ≤ K + y + M_{𝔊_X}(N)`, with a proof (S_y(p) = 1
  since p > y, and H_X(p) = 0 by the note's identity lemma). "E(N) ≤ M(N)" is withdrawn
  in the doc, the (W) bullet and the report.
* **D4** — "no arithmetic-free argument can cap it" is relabelled Assessment, in the §0
  Verdict, after Cor 2.2 and in the report. What is PROVED (the equivalence with (W_𝔊))
  is said explicitly. The emptiness of the "escape" as a method is noted.
* **D5** — §4 now has the hypothesis `|Φ̂(ξ)| ≤ C_Φ|ξ|^{−1−η}`, with the alias estimate
  O(N^{−η}) written out.
* **D6** — not applied (optional; heuristic only).

After these repairs the verdicts in the summary table that read SOUND-AFTER-REPAIRS
become SOUND. Labels are unchanged except for the D4 relabelling to Assessment.

## Replay
```
ulimit -v 8000000
timeout 1200 uv run --with scipy --with numpy python scripts/review_weights_thm21.py   # ~5 min
timeout 900  uv run --with numpy python scripts/review_weights_kernel.py               # ~1 min
timeout 1800 uv run --with numpy python scripts/review_weights_lemma32.py             # ~10 min
timeout 3000 uv run --with numpy python scripts/review_weights_translate.py 300 1     # ~10 min
```
