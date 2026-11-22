Result: No new forcing mechanism at a fixed prime was found in the completed searches, and nothing passes 3/4. Trybushnyi's explicit, uniform-in-K 3/4 bound was publicly deposited on 2026-10-06, before our first m^{−1/4} statement (2026-10-08). The 2026-11-06 Kandukoori–Ramesh–Kumar revision is editorial. Jiang–Lau–Lü (arXiv:2611.12467) is a research lead for z81-gap, and its port is blocked by a named, unproved shifted mean-square estimate.            Label: Assessment (literature screen). External statements are quoted as stated by their authors, from opened texts; no external proof or Lean build was audited; no JLL port is proved
Scope: Round 1 covered arXiv math.NT (247 listings) and math.LO (64), submitted 2026-11-10…19, plus keyword, author, version and web sweeps. Round 2 covered the K-R-K PDF history (three versions), the Zenodo deposit dates, the repo commit dates, targeted 2024–2026 hunts (a)–(d) (partly cut short by arXiv HTTP 429, §4) and a JLL §§2–8 structure read. Not swept: the 11-20…22 listings (unannounced on 2026-11-22), and math.CO/AG title by title. Negative findings mean "not found in the completed searches". ES remains open.
Review: cross-lab hostile review by GPT-6.2 Astra (deep), ACCEPT-WITH-FIXES, `data/z81/xreview/REVIEW_LIT_OPUS_ASTRA.md`; all ten fixes applied in the commit that adds that file. Research-subagent extractions (`data/z81/lit/notes/S1–S3`, `R2a–R2d`) were read and spot-checked; ✔ items were re-opened by the author.
Triage: DATA, plus one priority correction (REFUTATION/correction class for the STATUS §1A and §4 wording)
STATUS delta (hold for orchestrator wording check; reviewer: keep claims dated and source-specific):
* §1A first bullet: replace "Kandukoori–Ramesh–Kumar's claim predates ours (`Z58_LIT.md`); Dahan gets 5/7 (`Z71_LIT.md`)" with: "External 3/4 claims: Kandukoori–Ramesh–Kumar (m = 4 and each fixed m; repo commit dates precede ours, `Z58_LIT.md`); Trybushnyi (arXiv:2611.14167; Lean deposit Zenodo 23188522 dated 2026-10-06, before our 2026-10-08 m-uniform statement): E_K(N) ≤ N exp(−c((log N)³/K)^{1/4}) for 4 ≤ K ≤ h³/2⁹⁰, h = ⌊log₂N⌋, explicit c, as stated by the author. Our short-interval, AP, exceptional-prime-in-short-interval and m/p-transition variants are not in either (`notes/z81/LIT.md` §0.4). Dahan claims 5/7 (`Z71_LIT.md`)."
* §4 Priority bullet: "Do not claim the 3/4 bound, or its initial-segment m^{−1/4} form, as first: K-R-K (m = 4, fixed m) and Trybushnyi (uniform K) are earlier by the dated evidence in `notes/z81/LIT.md` §0.4; public-visibility dates are unverified."

# z81 LIT — literature and external-inspiration scout, 2026-11-10 … 2026-11-22 (Rounds 1–2)

ES is OPEN. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. ✔ = statement re-read by the
author in the opened `.txt` (`data/z81/lit/src/<id>.txt` or `data/z81/lit/krk/*.txt`; line numbers given). Every item
is an unrefereed preprint unless a journal is named. Theorems and Lean checks are **as stated by their authors**. No
external proof was audited, and no Lean package was built.

## 0.3 Priority flag: Trybushnyi arXiv:2611.14167 (orchestrator: act at export)

**The statements** ✔ (`2611.14167.txt` l. 63–79). Write h = ⌊log₂N⌋ ≥ 4096 and K ≥ 4.
* **Thm 1.1(a)**: if Kh ≥ 2⁶⁶ and 2⁸⁵K ≤ h³, then E_K(N) ≤ N exp(−(log N)^{3/4}/(24(2³²K)^{1/4})).
* **Thm 1.1(b)**: if Kh ≥ 2⁶¹ and 2⁹⁰K ≤ h³, the same holds with 2³⁷K in place of 2³²K.
* **Cor 1.2**: E₄(N) ≤ N exp(−(log N)^{3/4}/8689) for N ≥ 2^{2^{64}}, from (a); and /20666 for N ≥ 2^{2^{59}}, from (b).
* **Deposits.** Zenodo 23188522 v1.0 (`created` and publication date 2026-10-06, API) states Theorem A = Thm 1.1(b),
  formalised. Zenodo 24017156 (2026-11-06) and arXiv v1 (2026-11-10) add 1.1(a).
* **Formalisation, as stated.** The paper (App. C, l. 2101–2128) and both Zenodo descriptions say: Lean 4.22 with
  Mathlib, no `sorry`/`admit`/`native_decide`/extra axioms, and 3171 declarations in v2. Not built or replayed here.

**Comparison with our note** (`paper/es-mn-short-note.tex` Thm A, l. 148–161). Our Thm A gives the same exponent and
the same m^{−1/4} dependence, uniformly in m ≥ 4 *and in short intervals* (z, z+H]; it is ineffective (BV). Trybushnyi
is initial-segment only, but explicit and effective. The statements and ranges are not identical.

**Dates** (repo commit dates, not publication attestations).
* Our first m^{−1/4} statement: `071daebe6` (`EXCEPTIONAL_MN.md`, 2026-10-08 16:36) and `9c1a3ce5b`
  (`es-mn-short-note` skeleton, 19:01). `6af987ca6` (19:07) only adds the proofs.
* Our m = 4 note: `paper/es-threequarter-note.tex`, first commit 2026-09-06.
* The repo TeX is readable in the campaign repository but has not been submitted or posted to arXiv.
* Ordering: Trybushnyi's dated deposit (10-06) precedes our m-uniform statement (10-08).

**Other points.**
* The paper cites neither K-R-K nor us. It says Vaughan's 2/3 stood "for more than fifty years" (l. 44–47) and cites
  Dahan's 5/7 as concurrent.
* Its remark at l. 88–94 gives E_K(N) ≤ N/(log N)² for K ≤ c′(log N)³/(log log N)⁴. That is an initial-segment
  consequence; our prime-transition Thms U/L′ and the SEL-conditional sharpening are separate statements.

## 0.4 Priority table for the 3/4 exceptional-set bound (from opened texts and APIs; proofs not audited)

* **K-R-K v1** (38 pp., PDF dated July 29, 2026; `krk/krk_465815b8.txt`).
  * Dates: in the K-R-K **paper-website** repo `sushaan-k/erdos-straus` from its first commit `7a6356b4`
    (2026-09-01). Their **separate Lean repository** has root commit `268ebdbf` dated 2026-07-30 (`Z58_LIT.md`
    l. 142–168). Git dates are not public-visibility attestations.
  * m = 4: Thm 1.1, E(N) ≪ N exp(−c(log N)^{3/4}).
  * Fixed m: Thm 13.4 (l. 2392–2394), each fixed m ≥ 2, constants c_m, C_m.
  * Uniform m: **only CONDITIONAL.**
    * Thm 13.6 (l. 2459–2468), on Hyp 13.5, for 2 ≤ m ≤ (log N)^A: E_m(N) ≤ C_A N min{1, (1 + log log 3N)
      exp(−c_A(log N)^{3/4}/(φ(m)(m/φ(m))^{B_A}))}.
    * Thm 13.9 (l. 2562–2576) extends to m ≤ exp(κ(log N)^{1/4}) on Hyps 13.5 **and** 13.8.
    * Either way the loss is 1/φ(m), not m^{−1/4}.
  * Also Prop 13.2 (l. 2111–2134), large-prime-factor propagation:
    #{n ≤ N exceptional, P⁺(n) > Y} ≪ N(1 + log N) exp(−c(log Y)^{3/4}).
  * Formal: a Lean deduction of Thm 1.1 from nine named analytic inputs (l. 97–101).
* **K-R-K v2** (23 pp., same dateline; commits 7cdc9712…d96c7e30, 2026-10-30; sha256 20a3290b…, the same file as the
  Z58 archive).
  * Thm 1 (m = 4) and Thm 2 (each fixed m ≥ 4, constants depending on m). The conditional uniform-m material is
    dropped.
  * Remark 7.2: ineffective via BV. Remark 1.2: the heuristic "total weight (log X)^k ⇒ exponent k/(k+1)".
  * Formal claim: "proves Theorems 1 and 2 … using only Mathlib and Lean's standard axioms"; BV is adapted from an
    open-source formalisation.
* **K-R-K v3** (the revision; commit fe24ced5, 2026-11-06; sha256 e785d172…; `krk/krk_fe24ced5.txt`).
  * **Editorial only**: about 206 changed sentence-lines, consisting of rewording, renamed theorem titles (Thm 5.2
    "a Janson-type inequality", Thm 5.4 "sieve upper bound", Lemma 5.3 "counting in a residue class") and layout.
  * Thm 1 (l. 36–37) and Thm 2 (l. 39–45) are unchanged in content. Remark 1.2 and Remark 7.2 (l. 1412–1414) are
    unchanged.
  * No barrier or pointwise section was added. No uniform-m statement.
  * Formal claim shortened to "proves Theorems 1 and 2, the bound for exceptional primes, Example 1.1, and every
    numbered result of Sections 2–6" (l. 80–81). AI statement: MIT CSAIL Mantis used for Lean autoformalisation
    (l. 1415).
* **Trybushnyi** (§0.3).
  * Explicit and effective ("everything is effective", l. 1874).
  * Uniform 4 ≤ K ≤ h³/2⁸⁵, from (a), or h³/2⁹⁰, from (b).
  * **Prop 11.1** (l. 1821–1828), a barrier *inside an independent model*, stated by the author and formalised per
    App. C. Take independent events E_t with P(E_t) = 1/u_t, u_t = Kacd − 1, K ≥ 4, K log ξ ≥ 48. For every linear
    combination Ψ of products ∏_{t∈T}1_{E_t} with ∏u_t ≤ ξ and Ψ = 1 off all events,
    E[Ψ²] ≥ exp(−(4/3)(48/K)^{1/4}(log ξ)^{3/4}).
  * It bounds a second moment in the model, not the true exceptional set. Its extension to Selberg weights and the
    large sieve (l. 1858–1873) is the author's heuristic.
* **Ours** (internal; dates above).
  * 3/4 for m = 4.
  * Thm A: uniform in all m ≥ 4 and in short intervals. Also an AP version, exceptional primes in short intervals, the
    m/p transition (Thm U PROVED rel. BV and Shiu; Thm L′) and a SEL-conditional sharpening.
  * Ineffective. Limits: `paper/sieve-limits-note.tex`, `notes/z80/BEYOND_34.md`.
* **Dahan II** (arXiv:2611.08717) claims 5/7. The repo's worked modification (`Z71_LIT.md` §2.1.1, l. 73–86) reaches
  (log N)^{3/4}/(log log N)^{1/4}, not a clean 3/4.

**Reading (Assessment).** By the dated evidence, K-R-K precede us for m = 4 and for fixed m, and Trybushnyi precedes
our m-uniform initial-segment statement. K-R-K v2/v3 and Trybushnyi both *claim* formalisations of their headline
bounds. Only Trybushnyi claims explicit constants and a formalised barrier. Our distinctive items, relative to these
three sources only (wider novelty unverified): short-interval and AP uniformity, exceptional primes in short intervals,
and the m/p transition statements. A grep finds no K-R-K citation in Trybushnyi (references, l. 2256–2298 ✔) and no
Trybushnyi or Dahan citation in K-R-K v3.

## 0.5 Hot-lead dispatches per z81 lane

### z81-specific-class (break 3/4)
* **Read Trybushnyi §11 (l. 1795–1890) first.**
  * *Bookkeeping heuristic* (l. 1796–1810): mass L^β of classes at a cost of L^γ bits per event gives the exponent
    β/(β+γ). For Type II, β = 3 and γ = 1. Elsholtz–Tao's average count (log p)³ log log p suggests β cannot grow much.
  * *Barrier*: Prop 11.1 holds within its independent model (§0.4). The author's view (l. 1870–1873) is that a larger
    exponent "needs information about the exceptional set beyond the distribution of n in residue classes of modulus
    at most N". This corroborates z80 `BEYOND_34.md` §§13,16 from outside.
* **Assessment.** Within this bookkeeping, dispersion or bilinear Kloosterman input at a fixed level N^{1+δ} improves
  constants rather than the exponent. Nothing here excludes routes through genuine correlations of the real events,
  other event families, or a different transfer estimate.
* Technique: the real Kotecký–Preiss/Dobrushin bound (Cor 3.2, l. 364) controls correlated inclusion–exclusion
  without log log losses. Relevant to the constants and log log variants of our 3/4 note.
* Bettin–Drappeau–Lee 2610.42008 contains no new Kloosterman-fraction bound. Gou–Wang–Xu 2611.18825 assume ratios
  conjectures (2/2 Dirichlet and zeta; 1/1 angular Hecke for n²+1) and give no implication to or from BCR Conj. 1.
* **Round 2 (§4.1).** No 2024–2026 theorem found that exploits divisor-closure or sparse prime support to save beyond
  residue-class sieving. The nearest items:
  * K-R-K v1 Prop 13.2 (large-prime-factor propagation; not an exponent gain);
  * Banks 2609.37434 (random model);
  * Banks–Shparlinski 2610.19597 (almost all classes mod p^γ);
  * Chan 2506.04087 (multiplicatively closed sets of positive density).

### z81-gap (g ≥ 11 infinitely often)
* **FHRSS arXiv:2504.20289 is still v1** (API, 2026-11-22). The proof of Thm 3.9 is still omitted; no follow-up was
  found in the completed searches.
* **Repo state** (`POINTWISE_WINDOW.md` l. 15–18):
  * W1 (a_min ≥ 7, i.e. window 3 failing) is already PROVED there by a semi-linear sieve route, modulo cited sieve
    theorems. So for k = 3 the single-window input does not need FHRSS.
  * W2 (a_min ≥ 11) is **CONDITIONAL** on EH. It is the window analogue of Friedlander–Iwaniec 2009 (p ± 2 both sums
    of two squares; lower bound conditional on a level near 1). That is an analogue, not an implication.
  * Sedunova arXiv:2609.28200 still assumes a level for the representation-*weighted* r(n−2)r(n+2).
  * `Z55_P415.md` §0.2's 1.22 is a modelled *sufficient* level for one P(4,15) implementation, not a necessary level
    for W2.
* **JLL arXiv:2611.12467** ✔ (Thm 1.1, l. 103–108): Σ_{p≤x} b(p−1) = κ𝔖 x/(log x)^{3/2} +
  O(x/((log x)^{3/2}√(log log x))), unconditionally. Iwaniec had shown that it follows from EH-strength input (l. 116–130).
  * Method: Vaughan's identity; Type I via Fouvry–Tenenbaum BV for b·W; Type II via a mean square after extracting
    auxiliary split primes; harmonic switching; Selberg removal of the weights.
  * **Research question (Assessment): can this method give the single-window counts for b′₃((p+3)/4) and
    b′₇((p+7)/8), and is the joint count reachable?** Here b′_k(n) = 1 iff n is primitively represented, i.e. no inert
    prime divides n.
  * The port needs a **new shifted mean-square estimate**, replacing JLL Thm 4.1's equation mn − 1 = ah by
    mn + k = (k+1)ah. This is not supplied by JLL or by any cited preprint. Full hypotheses: §4.5.
* **Joint target, corrected.** With t = (p+7)/8 we have (p+3)/4 = 2t − 1, so the joint indicator is b′₇(t)b′₃(2t−1).
  * Quadric form: points on F₃(U,V) − 2F₇(U′,V′) = −1 with **both** pairs primitive, 4F₃(U,V) − 3 prime, and the
    Theorem-I progression conditions.
  * Two single-window asymptotics do not give a joint lower bound.
  * Achenjang–Woo 2611.16062 Thm A ✔ (l. 135–162) needs *linear* L_i in the same variables, so it does not apply.
  * Nath–Xie 2501.16723 (Thm 1.1 ✔ l. 112–115) has one sum-of-squares condition plus Ω(p+2) ≤ 9. It is already in
    the repo.

### z81-cap-zero
* Nothing found bears on the common-exponent barrier r−1 ∣ L.
* Kerr–Punch–Trudgian 2611.08816 give a log-free Burgess bound at prime moduli with explicit C(r). It matters only for
  explicit cap computations.
* Ford–Gabdullin–Pratt 2611.15534 (Thm 1.1: H_{≥r}(x,y,2y) ≍ x log(2r)/((log Y)^{1−E(θ)}(log log Y)^{3/2}), counted
  over n ≤ x) is calibration only: not pointwise, and no residue class.
* **Round 2 (§4.2):** no 2025–2026 pointwise supply of primes r with r−1 ∣ L, and no bounded-denominator 3-term
  relaxation. The nearest items:
  * Yang 2609.24347 (density of primes with P⁺(p−1) ≥ p^c);
  * the unverified OpenAI smooth-shifted-prime claim as quoted in Li–Zhuang 2610.15674 (already in the repo);
  * Czenky et al. 2507.03727 Cor 2.9 (with p-power denominators, a solution in rank R forces p−1 ∣ R−1). This is a
    divisibility constraint of common-exponent type: INSPIRATION only.

### z81-b2-duality
* No Vieta theorem for positive integral points.
* Jiang 2611.24452 (Vieta transitivity on generalised Markoff surfaces over 𝔽_p, p > 10^{320}) and
  Berman–Kingsbury-Neuschotz 2611.23168 (λ₂ along congruence families of p) are statements over 𝔽_p about fixed
  surfaces: **wrong domain** for positive integral ES points. `B2_ACROSS_FIELDS.md` already files Chen there.
* "Erdős' last equation" n(x₁+…+x_n) = x₁⋯x_n:
  * Luca–Pink–Sándor 2611.20783: liminf log f(n)/log n = 0.
  * Sándor–Zakarczemny 2611.20799: x_{n−1} ≤ n + max{d ∣ 2n²−2n, d ≤ √(2n²−2n)}.
  * The divisor bound comes from the same factorisation trick that produces B2 here: ALREADY-COVERED.
* Zhao 2611.14226 ✔ (l. 79–91) records the known embedding of ES into the Cayley cubic.

### z81-farey-proof
* The math.LO window (64 titles) has no IOpen, IE₁, IΔ₀ or Bézout-model paper.
* The Hilbert-10-over-ℚ cluster is definability over fields: NULL here. It comprises Bhargava–Burungale 2611.16130,
  Sun 2611.14605 and 2611.25002, Mazur–Rubin–Shlapentokh 2611.19103, and Pasten–Vidaux 2611.24748.
* **Round 2 (§4.4, complete re-run):** no 2024–2026 paper on IE₁, IE₁⁻ or IΔ₀ divisibility, Farey or Gauss reduction
  by the listed authors. Technique items:
  * **Kato 2608.12891** (a PA⁻_smu model without Euclidean division, via eventual-polynomial terms plus avoidance plus
    compactness);
  * **Ježil 2505.14516** (a PV₁ model with a nonstandard number without prime factorisation, CONDITIONAL on the
    hardness of factoring);
  * Hetzl–Weiser 2509.05653 (a strict hierarchy of open-induction fragments).

### z81-s-u7
* Banks–Shparlinski 2610.19597: products of three primes in every class mod p^γ, and binary EOS for almost all
  classes. These are free primes, not divisors of one integer, with a fixed modulus: screens 4 and 9.
* **Round 2 (§4.3):** the only joint same-parameter 4-rank theorem found is Xu–Zhu 2608.00387.
  * Thm 1.1: asymptotic independence of the 4-ranks of ℚ(√−d), ℚ(√−d₀d), averaged over squarefree d.
  * Thm 1.3 needs h(ℚ(√d₀)) odd.
  * Already in `Z53_LIT.md`.
* No pointwise cross-field 4/8/16-rank relation was found in the completed searches (one author query failed with
  429).

### z81-geom-comb
* **TRAP:** Gao–Geroldinger–Wang–Zeng 2611.24775 (Thm 1.1): D(C_n^r) ≥ r(n−1)+1+⌊r/(8n−7)⌋ for n = 2k with k ≥ 3 odd.
  So the van Emde Boas–Kruyswijk formula fails for r ≥ 8n−7; the first instance from the theorem is (n, r) = (6, 41).
  * It remains valid for p-groups (Olson) and for rank ≤ 2.
  * Do not use the conjectured equality for general unit groups (ℤ/4uℤ)^*. Use Olson on p-parts, or general upper
    bounds.
* Jain 2611.21136: every large N = a + b with P⁺(a) ≤ N^β (β > √(103/(256e))) and P⁺(b) ≤ (log N)^C. This is
  pointwise in N, but for sums: it gives no 4x = p + g with prescribed g, and needs an added quadratic-character step.
* Zhi 2611.24034 (|AA+A| ≫ N^{129/85}L^{−72/85}, N ≤ p^{1/2}), Farnamfar 2611.19594 and Matijasevick 2611.17205:
  NULL.

## 1. Falsifier table for candidate external mechanisms (Assessment)

The screens are those of FRONTIER §4 items 1, 2 and 14.
* **F1 (odd squares)** screens *strict/line* witnesses (e.g. (★)), not unrestricted ES at squares.
* **F2** separates full 8/n failures (8/11, 8/17, 8/131, 8/241) from R₈ = 0, the C-even (★) line of 8/p. Full 8/p
  *passes* at the R₈ zeros, e.g. 1,590,284,203,561 and 6,955,940,568,721.
* **F3** distinguishes the strict Type II zero 4545, the U₇ zeros Z₇, and the R = 0 composite controls.
* **F4** is the (★)-zero primes 409 … 8,813,281 and the composite 17,401,609.

| mechanism (source) | F1 | F2 | F3 / F4 | reading |
|---|---|---|---|---|
| polymer-gas sieve over Type II classes u = Kacd−1 (Trybushnyi) | not engaged: bounds an exceptional set | numerator-uniform for K ≥ 4; consistent, since 8/131 and 8/241 are permitted exceptions | not engaged | same architecture class as K-R-K and our 3/4 note |
| Prop 11.1 model barrier (Trybushnyi) | — | — | — | a barrier within its model, not a mechanism |
| JLL-type prime asymptotics (2611.12467) | not applicable: counts hard primes (window failures), not witnesses | not applicable | **inapplicable** to prime-count asymptotics | supply side for z81-gap only |
| vector sieve, semi-linear + linear (Nath–Xie) | not applicable | not applicable | inapplicable | almost-prime conditions, not window failures |
| linear forms + one norm form (Achenjang–Woo) | counting theorem; not a pointwise witness statement | numerator-blind | inapplicable | needs linear L_i in the same variables |
| three primes in every class mod p^γ (Banks–Shparlinski) | free primes, not divisors of one integer | numerator-blind | inapplicable | screens 4 and 9 |
| pointwise smooth decomposition N = a+b (Jain) | the decomposition exists for every large N, squares included, so no square-sensitive step | blind | would have to survive F3/F4 if built into a witness argument | needs an added quadratic-character step |
| Vieta transitivity over 𝔽_p (Jiang; Chen) | **wrong domain** (finite-field orbits) | — | — | not a positive-integral statement |
| Davenport / zero-sum constants (Gao et al.) | group-theoretic; blind unless the group depends on (·/p) | blind | — | tool; trap for general n, rank ≥ 3 |

## 2. Sweep methodology and coverage

* Scripts:
  * `scripts/z81_lit_arxiv.py`, a deterministic pager (copy of z71). Since the fix commit it exits non-zero on
    failure, with no unbound `total`.
  * `scripts/z81_lit_sweep.sh` now drives **every** query family used (NT, LO, keywords, authors, targets, Round-2
    weak arithmetic), records per-query status in `OUTDIR/SWEEP_LOG.tsv` (default `data/z81/lit/replay/`; the committed TSVs are the original runs and are never overwritten), and propagates failures.
  * `scripts/z81_lit_versions.py` checks versions via `id_list`.
  * The Round-2 (a)–(c) subagent queries are recorded in `notes/R2a–R2c` together with their outcomes; their TSVs
    are `r2a_*`, `r2b_*` and `r2c_*`.
* **math.NT** `nt.tsv`: 247 listings (primary or cross-list) dated 2026-11-10…19, all titles read, abstracts for about
  45. The 11-20…22 listings were unannounced on 2026-11-22 and are unswept. **math.LO** `lo.tsv`: 64, all titles read.
* Keyword sweeps 2026-11-01…22 over math.NT/AG/CO/DS/GR/LO and cs.CC/LO, rows per file: egypt 7, divisors 2, sieve 1,
  geom 15, comb 8, logic 1, erdos 2, kloost 7.
  * The small counts reflect exact-phrase `abs:` matching. The NT title read covers those terms within NT, but not
    in other categories.
* Authors `authors.tsv` (2026-09-15…11-22; 280 rows, mostly namesakes). Targeted: `tgt_sumsq` 13, `tgt_halfdim` 3,
  `tgt_fhrss` 20. Round-2 weak arithmetic: `r2d_kw` 91 and `r2d_au` 305, both complete.
* Versions `versions.tsv`, 2026-11-22, unchanged:
  * FHRSS v1; Dahan II v1; Dahan I v2;
  * Bettin–Chandee v1 (Adv. Math. 2018); BCR v1;
  * Maynard I–III; Maynard 1507.05080 v2 and 2407.14368;
  * Elsholtz–Tao v6.
* K-R-K: not on arXiv. Its versions are in `data/z81/lit/krk/`, with full hashes in `krk/SHA256SUMS`.
* Full texts: 24 Round-1 PDFs plus the Round-2 PDFs, extracted with `pdftotext`. `src/MANIFEST.txt` gives full
  sha256 hashes and sizes. The PDFs themselves are not committed.
* **Non-arXiv** (S3, 2026-11-22):
  * erdosproblems.com/242: last edited 7 May 2026; no comments since 11-10.
  * plasma-ai/erdos: PR #65 merged 11-10; nothing on E0242 since.
  * formal-conjectures 242.lean: unchanged since 09-18.
  * Dahan's GitHub: Papers I v2 and II v1 only.
  * MathOverflow: none found. Math.SE: unresolved.
  * Tao blog: nothing since 11-10.
* **Not done:** a Lean replay; any proof audit; the 11-20…22 listings; math.CO/AG title by title; opening
  Fouvry–Tenenbaum myself. Their D-generality is per the reviewer's reading of arXiv:2004.04766v4.

## 3. Per-paper verdicts (Rounds 1–2)

The verdict vocabulary is NEW-MECHANISM / USABLE-INPUT / INSPIRATION / ALREADY-COVERED / FLAWED / NULL. No item
earned NEW-MECHANISM.

* **Trybushnyi 2611.14167**: USABLE-INPUT (priority) and INSPIRATION (barrier, technique). See §0.3–0.4.
  * Lemma 2.1 ✔ (l. 217–224): if u = Kacd − 1 divides nc + a, then K/n = 1/(abd) + 1/(acdn) + 1/(bcdn).
  * AI declaration ✔ (l. 205–214): Claude Opus 5.x assisted.
* **Jiang–Lau–Lü 2611.12467**: INSPIRATION / research lead for z81-gap (§4.5).
* **Nath–Xie 2501.16723**: ALREADY-COVERED (`Z54_HCKILL.md`, `Z55_P415.md`).
* **Achenjang–Woo 2611.16062**: INSPIRATION (gap) ✔ Thm A l. 135–162. The extension to general binary forms is a
  remark only (l. 163–165).
* **Gou–Wang–Xu 2611.18825**: NULL. Conditional on ratios conjectures (2/2 Dirichlet and zeta; 1/1 angular Hecke for
  n²+1).
* **Grimmelt–Merikoski–Pandey–Pascadi 2610.41356**: NULL (averaged over h).
* **Bettin–Drappeau–Lee 2610.42008**: NULL.
* **Kerr–Punch–Trudgian 2611.08816**: minor USABLE-INPUT (explicit Burgess bound).
* **Banks–Shparlinski 2610.19597**: INSPIRATION.
* **Ford–Gabdullin–Pratt 2611.15534**: NULL (calibration; log(2r) form).
* **Jain 2611.21136**: INSPIRATION.
* **Gao–Geroldinger–Wang–Zeng 2611.24775**: TRAP.
* **Zhi 2611.24034, Farnamfar 2611.19594, Matijasevick 2611.17205, and the zero-sum papers 2611.14140, 2611.20197,
  2611.25050, 2611.15210, 2611.19508**: NULL.
* **Dai–Li–Li–Yi 2611.15110**: INSPIRATION for the coverings target (STATUS §2 item 5), untested.
* **Luca–Pink–Sándor 2611.20783, Sándor–Zakarczemny 2611.20799**: ALREADY-COVERED.
* **Jiang 2611.24452, Berman–Kingsbury-Neuschotz 2611.23168**: NULL (wrong domain).
* **Zhao 2611.14226**: ALREADY-COVERED.
* **Hilbert-10 cluster, Visser 2611.18383, Ford (RGA) 2611.13697**: NULL.
* **Agrawal 2611.06798, Trey Li 2611.01793, Ji 2611.16665**: NULL.
* **Shao 2611.23488, Bazin–Klurman 2611.24117, Yang 2611.25495, Wang 2611.14161, Kiss–Sándor 2611.26555,
  Burrin–Gröbner 2502.17678**: NULL.
* Round 2:
  * **K-R-K v3**: editorial revision (§0.4).
  * **Banks 2609.37434, Chan 2506.04087**: INSPIRATION.
  * **Yang 2609.24347**: NULL.
  * **Czenky et al. 2507.03727**: INSPIRATION.
  * **Xu–Zhu 2608.00387**: ALREADY-COVERED.
  * **Kato 2608.12891, Ježil 2505.14516**: INSPIRATION (new to the repo).
  * **Hetzl–Weiser 2509.05653, Jeřábek 2404.06888**: NULL.
  * **Enayat–Łełyk–Visser 2508.14758, Thamrongthanyalak (MLQ 2024)**: ALREADY-COVERED.

**Bottom line (Assessment).** No external mechanism found forces one tied divisor class at a fixed prime, and nothing
passes 3/4. The actionable items:
* The **dated priority correction** (§0.3–0.4).
* The **Davenport trap**.
* One **research question** for z81-gap: a shifted JLL mean-square estimate, then the joint indicator b′₇(t)b′₃(2t−1).

Still open: sweep the 11-23 listing. If z81-gap builds on JLL, obtain an independent cross-read of JLL Thm 4.1 and §7.

## 4. Round 2 details (2026-11-22)

The subagent notes are `data/z81/lit/notes/R2a–R2d`. The verdicts are the author's. During (a)–(c) the arXiv API
returned HTTP 429 on some queries (listed in those notes). (d) was re-run completely by the author. **The negatives in
(a)–(c) are therefore not exhaustive.**

**4.1 (a) Divisor-closed / sparse-support sets.** None of the items found exploits divisor-closure or support on a
sparse prime set P_E beyond residue-class sieving.
* K-R-K v1 Prop 13.2 bounds exceptional n with a large prime factor.
* Banks 2609.37434 Thm 1.1 (R2a, l. 119–133) is a random model with Θ > 3/4.
* Banks–Shparlinski Thm 1.2 gives almost all classes mod p^γ.
* Chan 2506.04087 Thm 2 (l. 68–79) needs M of positive lower density.
* Assessment: divisor-closure alone gives only E(N) ≤ #{n ≤ N : every p ∣ n lies in P_E}.

**4.2 (b) Smooth shifted primes / generation / restricted Egyptian fractions.**
* Yang 2609.24347 Thm 1.1 (R2b, l. 75–83) is a large-factor frequency, the wrong direction.
* Li–Zhuang 2610.15674 (l. 41–64) quotes the unverified OpenAI claim.
* Klurman–Shparlinski–Teräväinen and Hughes are ALREADY-COVERED (almost all q).
* Czenky et al. Cor 2.9 (l. 198–202) is INSPIRATION only.

**4.3 (c) Joint class ranks.**
* Xu–Zhu 2608.00387 Thm 1.1 (l. 141–147) and Thm 1.3 (l. 178–186, assuming h(ℚ(√d₀)) odd). Both are averaged over
  squarefree d, with no prime-subfamily statement.
* The only deterministic relation mentioned there is genus-theoretic 2-ranks (l. 78–82).
* Governing-field items 2505.20117 (function fields) and 2407.03754 (genus theory): NULL.
* Pre-2024 joint 16-rank results for ℚ(√−p), ℚ(√−2p), cited in Xu–Zhu l. 94–100, were not re-screened.

**4.4 (d) Weak arithmetic** (`r2d_kw.tsv`, `r2d_au.tsv`, both complete).
* No 2024–2026 paper by Jeřábek, Boughattas, Smith, Otero, Wilkie, Macintyre, D'Aquino, Berarducci, Kołodziejczyk or
  Thapen on IE₁, IE₁⁻, IΔ₀, IOpen + Bézout, Gauss reduction or Farey fractions.
* Kato 2608.12891 (abstract read) and Ježil 2505.14516 (abstract read): technique INSPIRATION, new to the repo.
* Hetzl–Weiser Thm 4.4 (R2d, l. 319–330): NULL.
* Enayat–Łełyk–Visser 2508.14758 and Thamrongthanyalak (MLQ 70, 2024): ALREADY-COVERED (`Z64_UNPROV.md`,
  `Z65_LOGIC2.md`).

**4.5 (e) What a JLL port to b′₃((p+3)/4) and b′₇((p+7)/8) would need.** Research obligations only; **nothing here
is proved**. Every line reference is to `src/2611.12467.txt`.
* **(H1) Type I, Lemma 3.1 (l. 285–372).**
  * JLL apply Fouvry–Tenenbaum (Trans. AMS 375 (2022)) Thm 1.8 to b_t = b·∏t_ν^{ω_ν} in F(4,2). Per the reviewer's
    reading of arXiv:2004.04766v4, Def. 1.1 and Thm 1.8 allow any modulus D, so D = 3 and D = 7 are admissible in
    principle.
  * The real obligation is the **progression main term**, including q_D = (q, D^∞), the analogue of JLL's q₄ step
    (l. 339–346).
  * Prime values are constant on bands and classes mod D. b′_k(ℓ^j) = 0 for inert ℓ, and the ramified prime k never
    divides n on prime inputs p > k.
* **(H2) Type II.**
  * Prop 4.2 (l. 800–835) uses only "auxiliary primes ≡ 1 (4) ⇒ b(ah) = b(h)" (l. 815–816) before Cauchy–Schwarz.
    With *split* auxiliary primes (relative density 1/2, so V_ν = ½log 2 + o(1)), b′_k(ah) = b′_k(h) holds.
  * But the mean square Q_Y of Thm 4.1 (l. 769–805) is defined with rough Möbius-type coefficients and the equation
    **mn − 1 = ah**. Only the prime sets may vary ("uses only (4.1)", l. 776–777).
  * The port needs **mn + k = (k+1)ah**, which changes the determinant relation to cmn − ars = k(a − c) with an extra
    divisibility condition. It also changes the phase and kernel (l. 891–895, 1007–1015).
  * **This shifted estimate is the missing input.** It is not supplied by JLL or any cited preprint.
* **(H3) Major arcs, Lemma 7.2 (l. 2118–2135).** These use the exclusion of Landau–Siegel zeros: Banks
  arXiv:2610.15483 on the OpenAI proof, and Green Hexagon:2610.00311, both 2026 and unrefereed.
  * Assessment, unchecked: Siegel's theorem may substitute, ineffectively, since q* ≤ L^B.
* **(H4) Harmonic switching** follows the 2026 preprints [30] (OpenAI, Poisson–Dirichlet law) and [22] (Lü–Wang–Wu
  2610.20242) (l. 160–161). Both are unrefereed dependencies.
* **(H5) Weight removal, §8 (l. 2500–2531).** The local densities must be recomputed.
  * Generic inert ℓ: modulo ℓ², exclude ℓ ∣ (prime argument) and ℓ ∣ n, i.e. 2ℓ classes, so density 2/ℓ.
  * ℓ = 2: for k = 3, 4n − 3 is odd and 2 is inert, so only even n are excluded (density 1/2). For k = 7, 2 splits and
    8n − 7 is odd.
  * The ramified prime and the Theorem-I progression primes must be isolated.
  * Positivity must be established with the required congruences, not asserted.
* **(H6) Main term** (§3.3, l. 632–700). The Euler product changes. The step "b(2n) = b(n)" (l. 665) fails for k = 3
  (b′₃(2n) = 0) and holds for k = 7. Redo (3.13).
* **(H7) Theorem I side conditions** (`notes/z80/EXTREME.md` §10): primitivity, and p ≡ 1 mod m for ℓ ∈ {3,5,7}.
* **Net (Assessment).** Even granting (H1)–(H7) and every cited preprint, a single-window port still needs the shifted
  estimate (H2). k = 3 already has W1's sieve proof, so the port matters for k = 7 and for general k (FHRSS
  independence).
  * The joint count needs more. In Prop 4.2 a second indicator b′₃(2t−1) would sit inside the Cauchy–Schwarz.
  * The joint Type I needs the progression distribution of the non-multiplicative b′₇(t)b′₃(2t−1).
  * **Nothing here is PROVED for ES, for W2 or for g ≥ 11.**
