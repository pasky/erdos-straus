# Z71_LIT — literature refresh 2026-10-10 … 2026-11-10: new ideas for the campaign? (z71, lane LIT; campaign otherwise paused)

**Verdict: no HOT LEAD, no new forcing mechanism.** One major ES-specific paper appeared (Dahan, arXiv:2611.08717, 109 pp.,
2026-11-05). Read against the campaign it contains (i) an exceptional-set bound with exponent 5/7 — *weaker* than the
3/4 of Kandukoori–Ramesh–Kumar (K-R-K) and of the campaign's note, and obtained by the same architecture with a shorter
cofactor range; (ii) an "exponent 1 − o(1)" that holds only on a structurally defined subset; (iii) a pointwise programme
that ends, by the author's own statement, at an open hypothesis which is B2 with a logarithmic cap. Everything else found
(shifted divisor correlations, higher-order Titchmarsh, quasi-RH for Dedekind zeta functions, integral-point and
class-group papers) is averaged, wrong-axis, or already in the repository. Useful by-products: two citation facts
(§4) and a renumbering warning for Dahan I v2.

ES is OPEN; nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Literature statements are quoted from the opened source with theorem number; proofs of cited papers were
**not** audited; every item is an unrefereed preprint unless a journal is named. All sources accessed 2026-11-10.
Review status: research-subagent notes (`data/z71/lit/notes/S1–S6`) were reviewed by the orchestrator, who re-opened the
sources for every statement marked ✔ below; **no cross-model (Astra) review has been run.**

Files: sweep script `scripts/z71_lit_arxiv.py`; listings `data/z71/lit/{nt,nt_early,kw_*}.tsv`; archived PDFs + text
`data/z71/lit/sources/` (36 papers); subagent brief `data/z71/lit/BRIEF.md`; notes `data/z71/lit/notes/S1…S6_*.md`;
repo arXiv-id snapshot `data/z71/lit/repo_arxiv_ids.txt` (1879 ids).

---

## 0. Falsifier table for the literature mechanisms (Assessment unless labelled)

| mechanism (source) | F1 odd squares | F2 numerator 8 | F3/F4 | reading |
|---|---|---|---|---|
| Semi-composite CRT sieve s = pq (Dahan II §7) | not engaged: bounds a set, proves nothing at a given n | not engaged | not engaged | exceptional-set tool only; same class as the 3/4 note (§2.1.1) |
| Kneser/2-Sylow containers, generating-polynomial large sieve (Dahan II §§3–6) | not engaged | not engaged | not engaged | bounds *structured* exceptions; generic ("diffuse") ones untouched |
| Hypothesis T (Dahan II Thm 9.7(b)) | quantifies over prime shifts p ≡ 3 (4) with (n/p) = −1 (the set PNR(n)), which is empty at squares | no numerator-8 statement is made; an eventual statement, so the finite screens do not refute it | threshold N_T unspecified (Remark 9.8) | = B2 with cap (log n)^A; an assumption, not a mechanism |
| Phase/"Bohr–Siegel" certificate (Dahan II Thm 9.6(b)) | — | — | — | certifies *failure* of a window; already `BRAINSTORM/z45_siegel_dichotomy.md` §5.1, and its converse is false at 31121/43 (§5.2 there, CERTIFIED) |
| Weighted-dilation graphs (OpenAI; Walsh; Hu–Lü–Wang–Wu) | true on average regardless of squares | numerator-blind | — | fixed-shift averages over n; B6 |
| Stable reduction ⇒ orbit size ≥ p (Chen) | — | — | — | every-large-p theorem about mod-p orbits of a fixed surface; wrong axis (already `B2_ACROSS_FIELDS.md`) |
| Effective Chebotarev under QRH(δ) (Frei–Sofos–Widmer) | local/character input, true at squares | numerator-blind | — | sharpens CONDITIONAL relaxations only |

## 1. Method and coverage

* **Deterministic arXiv sweep** (arXiv API, paged, `scripts/z71_lit_arxiv.py`): every math.NT listing (primary or
  cross-list) submitted 2026-09-28 … 2026-11-10 — **1174 titles, all read by the orchestrator** (825 from 10-10, 349
  earlier); abstracts read for 40 flagged items. Keyword sweeps across all categories: Erdős–Straus / Egyptian / unit
  fractions (7 hits since 09-01), "Erdős problem(s)" (6), integral points / Brauer–Manin / Markoff / strong
  approximation / Zaremba / modular hyperbola (180, mostly noise), AI + open problems (68), and subset products /
  Davenport / covering systems / residue classes in math.CO, AG, GR, DS, PR, cs.CC (155).
* **Six research subagents** read 35 PDFs (text extracted with `pdftotext`) and did the non-arXiv sweep
  (erdosproblems.com #242, erdosproblems.ai, Zenodo, GitHub, openai/math, Crossref, MathOverflow/MSE).
* **Not done:** proof audits; a full semantic diff of the openai/math manifest (file-list inspection only); the
  erdosproblems.com forum thread could not be extracted in full; ResearchGate/viXra/HAL/SSRN were searched but not
  exhaustively; math.CO/AG were swept by keyword only, not title by title.

## 2. Findings

### 2.1 Dahan II: arXiv:2611.08717v1, "Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture" (2026-11-05)

Single author, no acknowledgement of K-R-K: the text contains no occurrence of "Kandukoori"/"Ramesh" and no 3/4
exceptional-set exponent ✔ (grep); the abstract says the record "has remained since Vaughan (1970)" at 2/3 ✔. Its
companion "Paper I" is arXiv:2608.24035, now at **v2 (2026-11-05, 47 pp.)** ✔ (arXiv API; title matches ref. [1]).

**2.1.1 The 5/7 bound (§7).** *Thm 7.12* ✔ (`.txt` l. 5021–5030): with Q = exp((c₃/2)t^{1/2}), t = log Z =
η(log N log log N)^{2/7}, for all N ≥ 3, |E(N)| ≪ N exp(−c′(log N)^{5/7}/(log log N)^{2/7}). *Thm 7.11*: 7/10 with
Q = exp(t^{1/3}).
* Architecture ✔ (l. 3831–3881, 5033–5064): prescribed witnesses s = pq ≡ −1 (mod 12ua), p ∈ (Z^{9/10}, Z] prime,
  q ≤ Q a (log Z)⁶-rough cofactor, Z^{1/10} ≤ u, a ≤ Z^{1/8}; conditionally on n mod M_small the indicators over
  distinct p are independent in the CRT model; even Bonferroni polynomial majorant; Siegel-zero-free
  Bombieri–Vinogradov. Sifting mean L ≍ t²·log Q/log t; Bonferroni/CRT cost exp(O(k·t)), k ≍ L.
* **Comparison (Assessment, orchestrator).** This is the architecture of `paper/es-threequarter-note.tex` (prime ℓ ↔ p,
  multiplier k ≤ X^κ ↔ cofactor q, conditioning modulus L_K ↔ M_small, even Bonferroni truncation) and of K-R-K. The
  only quantitative difference is the cofactor range: Dahan needs Q·exp(−c₃t^{1/2}) = o(1) because his BV error is
  summed over q (l. 5034–5036), so log Q ≍ t^{1/2}, L ≍ t^{5/2}/log t, cost exp(O(t^{7/2}/log t)) ≤ N^{1/2} ⇒ 5/7.
  The note reaches power-size multipliers (K-R-K: a Type II family of cubic logarithmic mass), L ≍ t³, cost
  exp(O(t⁴)) ⇒ 3/4. So Dahan II §7 is a third,
  independent arrival at the same design; it supplies no input beyond it, and it sits below the cap of
  `EXCEPTIONAL_KARY3.md` ((D)24), as it must.
* **Worked through (2026-11-11, orchestrator; relative to Dahan's §7 as stated, his proofs not audited).** Every use of
  the upper bound on Q in §7 was located (grep over l. 3888–5070). All but one need only Q ≤ Z^κ with κ < 1/40:
  Q < Z^{9/10} (CRT), Q < 12U² = 12Z^{1/5} (disjointness, Prop 7.3), qτ(q) and q² small against Z^{1/20} (lattice sums,
  Prop 7.8), and Lemma 7.9 (M_Q ≍ log Q/log y; its proof only improves for larger Q). The one genuine use is
  **Thm 7.10, Step 2 (l. 4844–4851)**: "we trivially bound 1_{ab+u≡0 (mod q)} by 1 and the cardinality of 𝒬 by Q",
  giving Q·exp(−c₃t^{1/2}). Replacement: with r_b(u, a) = #{q ∈ 𝒬 : (q, 12ua) = 1, q | ab + u} and R₀ = t⁶,
  Σ_{(u,a)} r_b E(u, a) ≤ R₀ Σ E(u, a) + (C₀/R₀) Σ r_b²/φ(12ua). The first term is ≪ t⁶ exp(−c₃t^{1/2}) by his Prop 7.7.
  For the second, expand r_b² over pairs q, q′: the condition is u ≡ −ab (mod [q, q′]), a reduced class (an active q
  forces (b, q) = 1), [q, q′] ≤ Q² ≤ U^{1/2}, so Σ_u 1/φ(u) ≪ t/[q, q′] (as in the proof of (latupper) in the 3/4 note),
  Σ_a 1/φ(a) ≪ t, and Σ_{q,q′≤Q} 1/[q, q′] ≪ (log Q)³; total ≪ t⁵, uniformly in b. Hence the error is o(1) for every
  b and every Q ≤ Z^κ. Then L ≍ H ≍ t² log Q/log t ≍ t³/log t, cost (K+1)^k = exp(O(t⁴/log t)) ≤ N^{1/2} at
  t ≍ (log N log log N)^{1/4}, and Prop 7.5 gives **E(N) ≪ N exp(−c(log N)^{3/4}/(log log N)^{1/4})** in his set-up.
  The (log log N)^{1/4} loss is the price of y-rough cofactors (density 1/log y); the 3/4 note avoids it with
  unrestricted multipliers and a small-prime selector. This is the same device as Theorem (supply) of the 3/4 note
  (multiplicity paid in mean square, Lemma wsecond), simplified because his BV saving is exp(−c√t).
* Scope: Thm 7.12 is stated for all exceptional integers n ≤ N, like the note.

**2.1.2 The "1 − o(1)" bound (§§3–6) is for a structured subset.** *Cor 6.12* ✔ (l. 3619–3686): for the *small-sheet
component* E₂^small(N; J(N)) — primes n in E₂(N; J) for which at least P/4 of the P ≈ (6/π²)J² coprime pairs (u, a)
have |Σ_{I₁}(an + u)| ≤ φ(4ua)^{ε₁(N)}, ε₁ → 0, I₁ = (J⁵, z₁] — the bound is
N exp(−(1/40960 + o(1)) log N/((log log N)(log log log N)^κ)). *Thm 6.10(a)*: the "certified hierarchy" E₂^cert
(kernel branch + four structured regimes) is ≪ N exp(−c(λ)(log N)^{2λ} log log N), J = (log N)^λ, λ ∈ (1/3, 1/2).
The complement is named and left open by the author ✔ (l. 3443–3457, 3813–3829): E₂^diffuse = primes with, for more
than 3P/4 pairs, sheets of intermediate size "without a low-index Kneser stabilizer" and "angularly diffuse" phases;
"Extending … to the full global exceptional set E(N) requires eliminating the residual unlocalized diffuse component".
The full set E₂(N; J) is claimed closed only for J ≤ exp(c₀√(log log N)) and λ ≤ 1/78 (abstract ✔), where the saving
is ≤ (log N)^{1/39+o(1)}.
* *Thm 4.3* ("generating-polynomial large sieve") ✔ (l. 1534–1600): the large sieve with squarefree moduli having at
  most h prime factors from I, weights t^{ω(q)}, z^h ≤ Q, applied to integers with ≤ R collisions; the product
  ∏(1 + t z_p(k)) = (1 − t)^r ∏(1 + t y_p) is positive. This is an all-level large sieve with a multiplicative weight —
  inside the class covered by the campaign's caps ((D)24, (D)27, (D)28) when applied to the whole exceptional set.
* **Reading (Assessment, orchestrator).** There is no conflict with "3/4 is sharp for CRT architectures": that theorem
  caps what a majorant can prove for *all* avoiders, while Cor 6.12 bounds avoiders with an extra rare property. A
  "small sheet" at ≥ P/4 pairs is a joint lower-tail event for the number of prime factors of P linear forms in a short
  window, so it is rare whether or not n is exceptional. The generic case is the diffuse one. In campaign terms the
  open diffuse component is the same wall as TC^alt_θ / the lower-tail (RLD-like) problem of `EXSET_CHAR_FORCING.md`
  §4.2 and the "multiplicity-poverty" failures (61 % of rich failures; Kneser stabiliser trivial in 84 %,
  `BRAINSTORM/z52b_pass1_H04.md`). A route to θ > 3/4 through Dahan II would need a new bound on E₂^diffuse at depth
  λ > 3/8; the paper gives none.
* Red flags (concrete, from S1; not audited): the small-sheet threshold is P/4 in Cor 6.12 but P/2 in one overview
  sentence; the constant 1/40960 appears without a displayed derivation chain; "container" has no single definition.

**2.1.3 The pointwise part (§§8–9, App. A).** *Hypothesis T* ✔ (Thm 9.7(b), l. 6200–6219): there is a fixed A > 5
such that for every large prime n ≡ 1 (24) some shift p ∈ PNR(n) ∩ [1, (log n)^A] has
Σ_{χ odd, ≠ψ₀}|μ̂_p(χ)|² < 1 + Σ_{ψ even, ≠χ₀}|μ̂_p(ψ)|², equivalently −1 ∈ D(K_p) = Σ(K_p)Σ(K_p)⁻¹ mod p,
K_p = (n + p)/4. T ⟹ ES for all large primes n ≡ 1 (24), threshold unspecified; Remark 9.8 ✔ says so and adds that
disjointness of large prime factors across shifts "does not by itself imply statistical independence". The abstract ✔
lists T and two signed error targets (C17), (C76) as open.
* **Reading (Assessment).** D(K_c) ∋ −1 is the campaign's Type II e-slice criterion (`LONGSHOT_PIGEONHOLE.md` l. 52–70),
  the displayed inequality is its Fourier form (odd-character energy below even-character energy), and T asserts that
  one e-slice with e ≤ (log n)^A succeeds: **B2 with a polylogarithmic cap**, i.e. the cap statements of
  `CAP_*.md`. It is postulated, not derived from any standard conjecture.
* Thm 9.6(b) (phase sum < π for one odd character ⟹ the window fails): this is the phase-separation lemma of
  `BRAINSTORM/z45_siegel_dichotomy.md` §5.1 (PROVED there); its converse is false (31121/43, §5.2 there; also
  `Z52D_FOURIER.md` Thm B/C). The subagent's label "NEW to the campaign" for this item was wrong and is corrected here.
* Thm 9.7(a) (witness depth min(uv, s) ≥ (1/5 − o(1)) log n along n_Y ≡ 1 mod 4·lcm(1..Y)): same type as B1
  (`POINTWISE_OMEGA13.md`), weaker. Thm 9.3 (Farey-diagonal L² dispersion, S ≤ N^{1/2−ε}): averaged over n ∼ N (B6).
  Thms 9.9–9.10 (factor reciprocity (q/p) = (q/n); 1/k! cross-polytope volume of the certificate region): Jacobi
  transfer is (J)83; the volume bound is a count of certificates, not a forcing statement.
* Not found in the campaign by `git grep` (S2; not independently checked): the exact "small-LCM divisor cancellation"
  of Thm 9.5 and the threefold V_n: 4uavw − 4u²v − w = n bilinear set-up. Neither is pointwise.

**2.1.4 Dahan I v2 (arXiv:2608.24035v2, 2026-11-05)** ✔ (API abstract + text): "substantially revised"; explicit
constants at exponent 2/3 (0.0942, 0.1093 − ε), a dual Type I criterion (Thm 3.14), a 2-Sylow container reduction
(Prop 4.6), a sub-quadratic batch procedure. **Numbering changed:** v1 Thm 4.6 → v2 Thm 4.7; v1 Prop 4.8 → v2 Prop 4.9;
v1 Thm 4.14 → v2 Thm 4.15; v1 Thm 4.17 → v2 Thm 4.18; Lemma 4.2, Thm 4.3, Prop 3.8 unchanged. Every Dahan theorem
number in the repo refers to **v1** (`paper/*.tex` already pin v1 in the bibliography).

### 2.2 Analytic cluster (note `S3_analytic.md`; statements from the subagent unless ✔)

| paper | statement | pointwise? | for the campaign |
|---|---|---|---|
| Walsh 2610.40439 ✔ Thm 1.1 | Σ Φ(n/x) d_k(n) d_l(n+h) = main·x(log x)^{k+l−2}(1 + O((log x)^{−η})) for all fixed k, l ≥ 1, h ≠ 0 | no: average over n, fixed h, constants depend on h | new *method* (OpenAI "weighted dilation graphs", removing logarithmic averaging); the repo screened that manuscript only for smooth shifted primes (`BRAINSTORM/z52b_tools.md` #261). Fixed shift, no tied modulus: B6 |
| Hu–Lü–Wang–Wu 2611.12756 | Σ_{x<n≤2x} Λ(n)τ_k(n+h) ∼ C_{k,h} x(log x)^{k−1}, fixed k ≥ 2, h ≠ 0 | no | same lineage; could matter only for mean-value side results (asymptotics for Σ_p f(p)), not for B2 |
| Baier 2610.15706 | #{x₁² + x₂² − x₃² = n², x₃ ∼ M}: asymptotic for **every** n when M ≥ n^{71/96+ε} (Kim–Sarnak) | yes, but main term of power size | Hecke-orbit mechanism with error n^{θ}; the (★) count has polylog size and a tie a ≡ d ≡ −1 (mod c) that is not a congruence condition. Known barrier (FRONTIER §3, row M1a: power-size counts) |
| Elsholtz–Stadlmann 2610.20554 | large-sieve bound for sets with ≤ Θ lifts mod p² above ω(p) ≍ p classes mod p, p ∼ M, M^k ≤ √N: \|A\| ≪ N(log M)^k/M^k | n/a | beats Johnsen–Selberg, matches Montgomery's large sieve; prime-square moduli only. Not the residue-dense input (A*) needs |
| Hughes 2610.04678 ✔ abstract | (1/log 2 + o(1)) log Q primes of polylog size cover (ℤ/q)^× by subset products for almost all q ≤ Q (sharpens Klurman–Shparlinski–Teräväinen, already in the repo) | almost all q | external primes, not the divisors of (p + e)/4 |
| Yang 2611.01522; Xi 2610.11083; Jiang–Lau 2610.10372; Chatterjee 2610.31832; Johnston–Naik 2610.08569; Richter–Teräväinen 2610.03417 | level-of-distribution, Kloosterman moments, spacing, larger-sieve variants, patterns in shifted primes | all averaged / almost-all | none |

### 2.3 Integral points and geometry (note `S4_geometry.md`)

* **de Saint Germain–Zhang 2611.03036**, Thm A: for G ∈ ℤ_{≥0}[x, y] of bidegree (m, n), the positive integral points of
  xyz = G(x, y) are finite if mn < 4, infinite if mn = 4, Zariski dense if mn > 4; Thm 4.5: they biject with adapted
  friezes of a rank-two generalised cluster algebra. The (★) surface is xyz = x + y + n (bidegree (1, 1), z = 4C): the
  finite type. The five cluster variables are x, y, (y+n)/x, (x+y+n)/(xy) = z, (x+n)/y — the pentagon/frieze structure
  of `FRIEZE_ES.md`. The paper has no existence statement beyond (1, 1, n+2) and nothing about 4 | z. **Not new for us.**
* **Chen 2610.16407**, Thm 1.1 ✔: every component X of the moduli of SL₂(𝔽_p)-covers has deg j_X ≥ p (stable
  reduction); with Kingsbury-Neuschotz this gives, for all p > N (ineffective), transitivity on the mod-p points of
  x² + y² + z² − xyz = τ + 2. A non-counting "every large p" theorem, but about mod-p orbits of a fixed surface
  (`B2_ACROSS_FIELDS.md` already files Chen 2024 as the wrong axis). Template "rigidity lower bound + counting upper
  bound ⟹ no exceptions" needs exceptional primes to come in large families; see `PROPAGATION_CLOSURE.md`.
* Tian–Wei 2611.07454, Alessandrì–He 2610.40815, Wei 2610.13528, Wang 2610.21762: Brauer groups and BM obstructions
  for Markoff-type and Fermat-near-miss surfaces; no "no BM obstruction ⟹ integral point" theorem (Alessandrì–He
  Remark 5.3 records an unexplained failure). Wu 2610.36497: congruence-Hasse failure for commutators in surface
  groups (not integral points on surfaces). Chiu 2610.06166: polylog-size *coverings* of rational points by
  subvarieties (not polylog point counts).

### 2.4 Class groups and quasi-RH consequences (note `S5_classgroup_qrh.md`)

* **Frei–Sofos–Widmer 2610.18491** ✔ (intro): effective Chebotarev under QRH(δ) for ζ_L (Thm 1.1); least prime in a
  Frobenius class ≪_δ (log Δ_L)^{1/δ}(log log Δ_L)^{2/δ} (Cor 1.2); Ellenberg–Venkatesh ℓ-torsion bounds (Cor 1.4).
  Inputs they cite as *claimed*: OpenAI QRH(1/8) for Dirichlet L, QRH(1/12) for Hecke over ℚ(√−3), and
  **Cureton–Thorner, hexagon:2610.00200v1: QRH(1/6000) for all Dedekind zeta functions** (new to the repo). Effect here:
  the repo's "CONDITIONAL on OAI-003" statements that only need Dirichlet L-functions are unchanged; statements that
  needed Hecke/Dedekind input (class-field Chebotarev in the z70 class lanes) get exponent 1/δ = 6000 under
  Cureton–Thorner instead of 2 under GRH. None of this forces a class or a tied divisor.
* Banks 2610.31402: effective (1 − β) log d_F ≥ c(k) over a base field, effective Brauer–Siegel for Galois K/k.
  Liu 2610.12234, 2610.26835: half-plane constant 7/8 → 0.87496, 0.87489 for the same families.
* **Louboutin 2610.29347**: primes p for which every p − x² (x ≤ √p odd) has ≤ 2 prime factors are classified via
  class number and fundamental unit (Rabinowitsch type). The repo has no Rabinowitsch item. Reading (Assessment): the
  forcing direction "class group non-trivial ⟹ a small split prime divides f(x) at small x" has power-many witnesses
  (h ≍ √D); it fails the (J)103 test. The polylog-size forced subgroup is the 2-part (genus theory, Rédei), which is
  already on the z70 open list.
* Diao 2610.28001, ray class monoids 2610.11353, Luo–Wang–Zhou 2611.12528/2610.14613, 2610.36800: averages or
  structure theory; nothing pointwise.
* Survey 2610.17090 ("What the Machine Invented"): 38 instrument cards from the OpenAI release; none concerns divisors
  in a tied residue class; the number-theoretic ones (003, 007) are the ones `OAI_DUMP_IMPACT.md` already covers.

### 2.5 Non-arXiv (note `S6_web.md`)

* **plasma-ai/erdos PR #65 ("E0242: reject the three claimed full proofs of Erdős–Straus") was merged 2026-11-10
  20:12 UTC** ✔ (GitHub API). erdosproblems.ai #242 still shows the claim-derived status line.
* erdosproblems.com #242: no change, K-R-K still not listed. K-R-K Lean repo: HEAD still `f6c99eaa` (2026-10-30).
  DeepMind formal-conjectures 242.lean: unchanged since 2026-09-18. openai/math: content update 2026-10-26 (CM Hodge,
  local smoothing, subexponential SAT); no family on our topics by file list.
* Zenodo 23770866 (Bhattacharjee–Bhattacharya, 2026-10-29): explicit constant at exponent 2/3, adapting Dahan I; not
  read; no improvement on 3/4. No new journal item (Crossref), no new MathOverflow question.

## 3. The most promising ideas, and what a first look gives

1. **Dahan's structured/diffuse split as a route to θ > 3/4.** Looked at (§2.1.2): the structured part is the cheap
   part; the diffuse part is our TC^alt wall. *No gain.* What would change this: any bound for E₂^diffuse at λ > 3/8.
2. **Dahan's Hypothesis T / phase certificates as a new coordinate for B2.** Looked at (§2.1.3): T is B2 with a cap;
   the certificate is our z45 §5.1 lemma and is not exact (31121/43). *No gain.* It is independent corroboration that
   an outside programme ends at the same atom.
3. **Weighted-dilation graphs** (the one genuinely new analytic method of the month, now with two external
   applications). Looked at: all statements are averages over n at fixed shift. A side use — asymptotics for the
   Elsholtz–Tao sums Σ_{p≤N} f_I(p), f_II(p) via higher-order Titchmarsh — is plausible but is a mean-value paper,
   not ES. *Not pursued (spending rule).*
4. **Chen's rigidity-plus-counting template.** Looked at: needs a structure in which ES-exceptional primes come in
   families larger than the exceptional-set bound; none known (`PROPAGATION_CLOSURE.md`). *No gain.*
5. **Unconditional/effective Chebotarev (QRH for Dedekind zeta).** Relabelling of conditionals only.
6. **Rabinowitsch-type forcing.** Power-size witness count; the polylog part is the Rédei item already open.

**Bottom line.** Nothing published in these weeks supplies a mechanism for forcing one tied divisor event at a fixed
prime, and nothing moves the exceptional-set exponent past 3/4. The resume condition in `OPERATIONS.md` is unchanged.

## 4. Actions taken / proposed

* Applied: FRONTIER header and §1 "Exceptional set" get a z71 entry for Dahan II; `paper/es-threequarter-note.tex`
  cites Dahan II (one sentence, no priority claim); `OPERATIONS.md` records that PR #65 is merged.
* Proposed, not done: an Astra cross-review of this memo if it is to be relied on; an audit of Dahan II Cor 6.12 only
  if the exceptional-set line is reopened.
