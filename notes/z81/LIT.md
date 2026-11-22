Result: The 2026-11-10…22 literature contains one important ES item: Trybushnyi arXiv:2611.14167, a third independent, explicit and Lean-formalised 3/4 exceptional-set bound that is uniform in the numerator K with the K^{−1/4} dependence. It also proves an independent-model 3/4 barrier for square-sieve weights. There is no new pointwise mechanism. The best lead is for z81-gap: Jiang–Lau–Lü's unconditional asymptotic for primes u²+v²+1 (arXiv:2611.12467, a level-free Type I/II method). It is set against the repo's FI09/W2 joint-window ledger.            Label: Assessment (literature screen); quoted statements are as stated in opened sources, proofs NOT audited
Scope: arXiv math.NT (complete, 247 listings) and math.LO (complete, 64) submitted 2026-11-10…2026-11-19. Nothing dated 11-20…22 had been announced by 2026-11-22, a Sunday. Keyword sweeps over 8 categories, 2026-11-01…22; author sweeps 2026-09-15…11-22; version checks of 16 load-bearing preprints; non-arXiv web check. No ES proof or disproof exists anywhere; ES is OPEN.
Review: none (Round 1; the orchestrator re-opened the sources for every ✔ item; research-subagent extractions in data/z81/lit/notes/S1–S3 were read and spot-checked; no Astra cross-review yet)
Triage: DATA, plus one priority correction (REFUTATION/correction class for the STATUS §1A wording, below)
STATUS delta: §1A first bullet: replace "Kandukoori–Ramesh–Kumar's claim predates ours (`Z58_LIT.md`); Dahan gets 5/7 (`Z71_LIT.md`)" by "Kandukoori–Ramesh–Kumar's claim predates ours (`Z58_LIT.md`); Trybushnyi arXiv:2611.14167 (2026-11-10; explicit constants, Lean-formalised per Zenodo 24017156) independently proves E_K(N) ≤ N exp(−c((log N)³/K)^{1/4}) uniformly for 4 ≤ K ≤ (log N)³/B, so the m^{−1/4} numerator variant is also external; the short-interval and progression variants are not in it; Dahan gets 5/7 (`Z71_LIT.md`, `notes/z81/LIT.md`)". §4 Priority bullet: add "and Trybushnyi's (arXiv:2611.14167) for the uniform-K form".

# z81 LIT — literature and external-inspiration scout, 2026-11-10 … 2026-11-22 (Round 1)

ES is OPEN. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. ✔ = statement re-read by me
in the opened `.txt` (file `data/z81/lit/src/<id>.txt`, line numbers given). Every item is an unrefereed preprint
unless a journal is named. **No external proof was audited.**

## 0.5 Hot-lead dispatches per z81 lane

**Orchestrator: priority flag (act now).** Trybushnyi, arXiv:2611.14167v1 (2026-11-10, 36 pp.), proves this ✔
(Thm 1.1, l. 63–72). For K ≥ 4, h = ⌊log₂N⌋ ≥ 4096, Kh ≥ 2⁶⁶ and 2⁸⁵K ≤ h³,
**E_K(N) ≤ N exp(−(log N)^{3/4}/(24(2³²K)^{1/4}))**.
* It follows that E_K(N) ≤ N exp(−c((log N)³/K)^{1/4}) with c = 1/6144 for 4 ≤ K ≤ h³/2⁸⁵.
* Cor 1.2 ✔ (l. 74): **E₄(N) ≤ N exp(−(log N)^{3/4}/8689) for N ≥ 2^{2^{64}}**.
* The Lean 4.22/Mathlib formalisation has 114 modules and 3171 declarations. By the paper's statement (App. C ✔,
  l. 2101–2128) it has no `sorry`, `native_decide` or extra axioms. The Zenodo record 24017156 says the same (S3);
  nothing was built or replayed here.

This is the initial-segment content of our `paper/es-mn-short-note.tex` (E_m(N) ≤ CN exp(−c(log N)^{3/4}m^{−1/4}),
m ≤ t³), now **public, external and with explicit constants**. Our note is dated 2026-10-08 by commit but is
unposted. The paper cites neither K-R-K nor us; it says Vaughan's 2/3 stood "for more than fifty years" (l. 44–47) and
cites Dahan's 5/7 as concurrent. Our short-interval and AP variants and Thm U/L′ are not in it. Its §1 remark (l. 88–94)
recovers the upper side of our m/p density transition up to (log log)^4: E_K(N) ≤ N/(log N)² for
K ≤ c′(log N)³/(log log N)⁴. The lower side is Pomerance–Weingartner Thm 3.1, which is already cited in our note.
**Proposed delta:** the §0 header above. FRONTIER §1 "Exceptional set" should carry the same sentence.

| lane | dispatch |
|---|---|
| **z81-specific-class** (break 3/4) | **Read Trybushnyi §11 ✔ (l. 1795–1890) before investing.** (i) *Bookkeeping law* (heuristic, l. 1796–1810): a mass L^β of classes at a cost of L^γ bits per event gives the exponent β/(β+γ). For Type II, β = 3 and γ = 1. Elsholtz–Tao's (log p)³ log log p solution count caps β at 3+o(1). So **any gain must come from γ < 1**: intersections of 2k ≍ µ events must be evaluated at total modulus far beyond N. (ii) *Barrier* Prop 11.1 ✔ (l. 1821–1825, formalised): in the **independent** model, for every Ψ that is a linear combination of ∏_{t∈T}1_{E_t} with ∏u_t ≤ ξ and Ψ = 1 off the events, E[Ψ²] ≥ exp(−(4/3)(48/K)^{1/4}(log ξ)^{3/4}). Selberg Λ² and, heuristically, the large sieve are of this form. The author's own conclusion (l. 1870–1873) is that a larger exponent "needs information about the exceptional set beyond the distribution of n in residue classes of modulus at most N". This corroborates z80 `BEYOND_34.md` §§13,16 from outside. **Consequence for the lane (Assessment):** large-modulus dispersion or bilinear Kloosterman input at a *fixed* level N^{1+δ} changes only the constant (it buys a factor 1+δ of bits, not γ < 1). A route past 3/4 must change the weight class, i.e. it must not be polynomial in event indicators, or it must use non-CRT structure of E, for instance that E is divisor-closed (Trybushnyi l. 128–133 uses this only for the small primes). Bettin–Drappeau–Lee 2610.42008 contains **no** new Kloosterman-fraction bound (S1). Gou–Wang–Xu 2611.18825 assume 2/2 ratios conjectures and give **no** implication to BCR Conj. 1 (S1). The Kotecký–Preiss/Dobrushin real cluster bound (Trybushnyi §3, Cor 3.2) is a reusable *technique* that removes log log losses in correlated inclusion–exclusion. It could clean constants in our 3/4 note and in its ≍ log log variants. |
| **z81-gap** (g ≥ 11 i.o.) | **(1) FHRSS arXiv:2504.20289 is still v1** (API, 2026-11-22). The proof of Thm 3.9 is still omitted and no follow-up was found (keyword and author sweeps). **(2) New input:** Jiang–Lau–Lü arXiv:2611.12467 ✔ (Thm 1.1, l. 103–108) prove *Motohashi's conjecture*: Σ_{p≤x} b(p−1) = κ𝔖 x/(log x)^{3/2} + O(x/((log x)^{3/2}√(log log x))). Here b is the indicator of sums of two squares. The method (l. 132–171) is Vaughan's identity. Type I comes from Fouvry–Tenenbaum BV for b·W, with W built from auxiliary split primes. Type II is a mean square of b(mn−1) after extracting a | mn−1 with all p_ν ≡ 1 (4), so that b(ah) = b(h). Then harmonic switching, high moments and Selberg-sieve removal of W. *Lead (Assessment, unchecked):* both of our windows k = 3, 7 live in class-number-one fields Q(√−3), Q(√−7). The EXTREME §10 Thm I event "(p+k)/(k+1) is primitively F_k-represented" is the multiplicative indicator b′_k(n) = 1 iff every prime of n splits or ramifies, which has the same two structural features JLL use (FT-type BV; b′(ah) = b′(h) for split a). So JLL's method plausibly gives an **asymptotic, independent proof of the single-window FHRSS input for k = 3, 7**, removing the dependence on the omitted Thm 3.9. **(3) Joint windows: already mapped in the repo.** g ≥ 11 needs p+3 ∈ 4·b′₃ and p+7 ∈ 8·b′₇ on the *same* prime. `POINTWISE_WINDOW.md` (W2, l. 35–45, 520–527) identifies this as the window analogue of Friedlander–Iwaniec, *Hyperbolic PNT* (Acta Math. 2009), whose lower bound for p with p±2 both sums of two squares needs a level θ < 1 near 1. Sedunova arXiv:2609.28200 (abstract re-read, `tgt_sumsq.tsv`) still assumes a level x^θ for r(n−2)r(n+2). The sieve-level ledger is `Z55_P415.md` §0.2: semi-linear⊗semi-linear with switching needs level ≈ 1.22. FRONTIER l. 2165–2171 and `Z56_K4LIT.md` record no unconditional result; Nath–Xie arXiv:2501.16723 (Ω(p+2) ≤ 9, one semi-linear and one linear condition) is already cited there. **What is new is JLL.** Iwaniec showed that the Motohashi asymptotic follows from EH-level input, E(x, x^{1−ε}) (✔ l. 116–130). JLL get it unconditionally by replacing level with a Vaughan-identity Type I/II argument, so the single semi-linear problem is no longer level-limited. **Sharp question for the lane (Assessment, unverified):** does JLL's architecture prove FI09's lower bound, and hence W2? There are two concrete obstacles. Type I needs BV-type distribution of the *shifted product* b(n−2)b(n+2), which is not multiplicative, so Fouvry–Tenenbaum Thm 1.8 no longer applies (this is exactly Sedunova's assumed level). Type II needs auxiliary split divisors extracted from *both* mn−2 and mn+2 before the Cauchy–Schwarz over h. Equivalent reformulation: an integer point on the (2,2) quaternary quadric F₃(U,V) − 2F₇(U′,V′) = −1 with 4F₃(U,V)−3 prime. Achenjang–Woo Thm A ✔ (l. 135–162) needs *linear* L_i and does not apply. |
| **z81-cap-zero** | Nothing new in the window bears on the common-exponent barrier r−1 | L. Kerr–Punch–Trudgian 2611.08816 ✔-abstract (S1: Thm 1.1 l. 62–94) remove the log from Burgess at prime moduli, with explicit C(r). This matters only if an explicit cap computation uses Burgess; it does not change e*. Ford–Gabdullin–Pratt 2611.15534 (order of H_{≥r}(x,y,2y), counted over n ≤ x; S2) is calibration only. **Trap:** it is not pointwise and has no residue class. |
| **z81-b2-duality** | No Vieta theorem for positive integral points. Jiang 2611.24452 (Vieta transitivity on Markoff mod p for p > 10^{320}, every D ≠ 4; S3) and Berman–Kingsbury-Neuschotz 2611.23168 (λ₂ along congruence families; S3) concern mod-p orbits of a fixed surface. **Trap:** a mod-p statement true for all large p also holds at n = m², so it fails F1 (`B2_ACROSS_FIELDS.md` already files Chen as the wrong axis). "Erdős' last equation" n(x₁+…+x_n) = x₁⋯x_n (Luca–Pink–Sándor 2611.20783: liminf log f(n)/log n = 0; Sándor–Zakarczemny 2611.20799: x_{n−1} ≤ n + max{d | 2n²−2n, d ≤ √(2n²−2n)}; S2) is a cousin of the amicable cubic p+e+b = ebt. Its divisor bound comes from the same factorisation (P′x−n)(P′y−n) = const that produces B2 here: ALREADY-COVERED. Zhao 2611.14226 ✔ (l. 79–91) records ES ⊂ Cayley cubic, [−n : 4t₁ : 4t₂ : 4t₃] ∈ S(ℚ), citing ET Rem 2.10 and Bright–Loughran. This is known; its height asymptotic is not integral or positive. |
| **z81-farey-proof** | math.LO window (64 titles) has nothing on IOpen, IE₁, IΔ₀, Shepherdson or Bézout models. The week's logic news is Hilbert's 10th over ℚ: Bhargava–Burungale 2611.16130 "ℤ is Diophantine in ℚ" (S3 Thm A l. 83–96), Sun 2611.14605 (26 unknowns; 16 under abc), Mazur–Rubin–Shlapentokh 2611.19103, Pasten–Vidaux 2611.24748. These are definability over fields, using elliptic curves and heights. There is no route to bounded-existential induction in discretely ordered rings: NULL for IE₁⁻ vs ES. Visser 2611.18383 (self-interpretations of S¹₂, Krajíček theories) is NULL. |
| **z81-s-u7** | Banks–Shparlinski 2610.19597 (S1, Thms 1.1–1.4): every reduced class mod p^γ is ℓ₁ℓ₂ℓ₃ with ℓ₁,ℓ₂ ≤ q and ℓ₃ ≤ exp(C(log q)^{2/3}(log log q)^{4/3}); binary EOS fails for at most φ(q)exp(−c(log q)^{1/3}…) classes. These are free primes, not divisors of one integer, and the modulus is fixed: screens 4 and 9, INSPIRATION at most. No new Rédei 4-rank or class-group-orbit paper in the window. Tang 2611.23465 (symmetric matrices of fixed determinant; 2-torsion of class groups announced for later) is remote. |
| **z81-geom-comb** | **TRAP (important):** Gao–Geroldinger–Wang–Zeng 2611.24775 ✔-abstract, S2 Thm 1.1 l. 51–58: **D(C_n^r) ≥ r(n−1)+1+⌊r/(8n−7)⌋ for n = 2k, k ≥ 3 odd**, so the van Emde Boas–Kruyswijk formula is false. The first instance from the theorem is (n, r) = (6, 41). The formula remains valid for p-groups (Olson) and rank ≤ 2. Any lane computation that uses D(G) = Σ(n_i−1)+1 for a general (non-p-group, rank ≥ 3) unit group (ℤ/4uℤ)^* must use Olson only on the 2-part, or the general vEB–K/Meshulam upper bound, never the conjectured equality. Jain 2611.21136 (S2 Thm 1): every large N = a+b with P⁺(a) ≤ N^β, β > √(103/(256e)) ≈ 0.3893, and P⁺(b) ≤ (log N)^C. This is **pointwise**, so it applies at a fixed prime p. **Trap:** it is for sums, not 4x = p+g (a difference, with 4 | a). Like every pointwise smoothness statement it holds at n = m², so on its own it fails F1; it is INSPIRATION for "smooth x with polylog-smooth 4x−p". Zhi 2611.24034 (|AA+A| ≫ N^{129/85}) and Farnamfar 2611.19594 (Katz–Tao 1.8263…) are finite-set expansion results with no divisor-set content: NULL. Matijasevick 2611.17205 (subset-sum inverse theorem) is NULL. |

## 1. Mandatory falsifier table for candidate external mechanisms (Assessment)

F1 is odd squares, F2 is numerator 8 (8/11, 8/17, 8/131, 8/241; R₈ zeros incl. 1,590,284,203,561 and
6,955,940,568,721), F3 is 4545 and Z₇, and F4 is the (★)-zeros 409 … 17,401,609.

| mechanism (source) | F1 | F2 | F3 / F4 | reading |
|---|---|---|---|---|
| Two-copy polymer-gas sieve over Type II classes u = Kacd−1 (Trybushnyi §§2–10) | not engaged: it bounds a set and proves nothing at any n | numerator-uniform for K ≥ 4 *by design*; consistent, since it is an exceptional-set bound (8/131 and 8/241 are allowed exceptions) | not engaged | same class as our 3/4 note, K-R-K and Dahan §7; capped by Prop 11.1 / BEYOND_34 |
| Independent-model square-sieve barrier (Trybushnyi Prop 11.1) | — | — | — | a barrier, not a mechanism; matches FRONTIER "3/4 sharp for CRT architectures" |
| JLL / Iwaniec half-dimensional prime asymptotics (2611.12467) | n/a: they produce *hard* primes (window failures), not ES solutions | n/a | must be consistent with the CERTIFIED max g = 127 up to 5·10¹² and with "g = 3 on relative density one"; a lower bound of order x/(log x)^{3/2} (single) or x/(log x)² (joint) contradicts neither | supply side for z81-gap only |
| Vector sieve, semi-linear + linear (Nath–Xie) | n/a | n/a | same as above | gives almost-prime, not window-failure, conditions |
| Linear forms + one norm form prime (Achenjang–Woo Thm A) | true at squares; a counting theorem | numerator-blind | — | needs linear L_i in the same variables; does not reach joint shifted-form conditions |
| Products of three primes in every class mod p^γ (Banks–Shparlinski) | true at squares | numerator-blind | — | screen 9 (class of free primes, not of a divisor of one integer), screen 4 (fixed modulus) |
| Pointwise smooth decomposition N = a+b (Jain) | **holds at m²**, so an ES argument resting only on it fails F1 | blind | — | needs an added quadratic-character step |
| Vieta transitivity mod p (Jiang; Chen) | **true at every large p and at squares** | — | — | wrong axis (mod-p orbits, not positive integral points) |
| Davenport / zero-sum constants (Gao et al.) | group-theoretic, blind unless the group depends on (·/p) | blind | — | tool; **trap** for general n, rank ≥ 3 |

## 2. Sweep methodology and coverage

* Scripts: `scripts/z81_lit_arxiv.py` (copy of the deterministic z71 pager), `scripts/z81_lit_sweep.sh` (all API queries),
  `scripts/z81_lit_versions.py` (id_list version check). TSVs are in `data/z81/lit/` (id, date, primary, cats, authors,
  title, abstract).
* **math.NT** `nt.tsv`: **247** listings (primary or cross-list) dated 2026-11-10…11-19, **all titles read**, abstracts
  read for about 45. By day: 38/19/37/19/8/12/31/20/43/20. The API returned nothing for 11-20…22: they were not yet
  announced on Sunday 2026-11-22, and the Monday 11-23 listing must be swept in Round 2. There is one day of overlap with
  z71 (11-10).
* **math.LO** `lo.tsv`: **64**, all titles read. Weak-arithmetic hits: none.
* Keyword sweeps 2026-11-01…22 over math.NT/AG/CO/DS/GR/LO and cs.CC/LO: `kw_egypt` 7 (ES/Egyptian/unit
  fraction/Sierpiński/Schinzel), `kw_divisors` 2, `kw_sieve` 1, `kw_geom` 15 (BM/integral points/cubic surface/Markoff/
  Vieta/strong approximation), `kw_comb` 8 (sum-product/subset products/Davenport/covering radius), `kw_logic` 1,
  `kw_erdos` 2, `kw_kloost` 7. The small counts of `kw_sieve` and `kw_divisors` reflect phrase-exact `abs:` matching. The
  complete NT title read covers what they would miss within NT, but **not** in other categories.
* Authors `authors.tsv` (2026-09-15…11-22; 280 rows, mostly namesake noise): Dahan, Bettin, Chandee, Radziwiłł, Maynard,
  Drappeau, Pascadi, Lichtman, Sawhney, Elsholtz, Stange, Rickards, Trudgian, Paredes, Sasyk, Kandukoori, Trybushnyi,
  Weingartner, Pomerance, Jeřábek, Boughattas, Thorner, Zaman, Shparlinski, Ford, Koukoulopoulos, Granville,
  Soundararajan, Heath-Brown, Browning, Wilsch, Kingsbury-Neuschotz, Bourgain, Fouvry, Kowalski, Michel.
* Targeted, all years: `tgt_sumsq.tsv` 13, `tgt_halfdim.tsv` 3, `tgt_fhrss.tsv` 20 (noise apart from FHRSS itself and
  Damm-Johnsen 2510.26655).
* Versions `versions.tsv` (API 2026-11-22). **Unchanged:** FHRSS 2504.20289 **v1**, Dahan II 2611.08717 **v1**, Dahan I
  2608.24035 **v2** (z71 renumbering warning stands), Bettin–Chandee 1502.00769 v1 (Adv. Math. 2018), BCR 1411.7764 v1,
  Maynard large moduli I v2, II v1, III v1, Maynard 1507.05080 v2, 2407.14368 v1, Elsholtz–Tao 1107.1010 v6.
  K-R-K: not on arXiv. GitHub `sushaan-k/erdos-straus` HEAD is `fe24ced5` (2026-11-06, "Update the page to the revised
  paper"), with no commit since 11-10. **The revised K-R-K paper was not re-read: Round-2 item.**
* Full texts read: 24 PDFs via `pdftotext` (`data/z81/lit/src/MANIFEST.txt` gives sha256; only three `.txt` files are
  committed: 2611.14167, 2611.12467, 2501.16723). Research-subagent extraction notes: `data/z81/lit/notes/S1_analytic.md`,
  `S2_comb.md`, `S3_web_geom.md`; brief `data/z81/lit/BRIEF.md`.
* **Non-arXiv** (S3, 2026-11-22):
  * erdosproblems.com/242 was last edited 7 May 2026, has no new comments after 11-10, and lists neither K-R-K nor
    Trybushnyi.
  * plasma-ai/erdos: PR #65 was merged 11-10, and the only later issue (#67) is on E0036. erdosproblems.ai #242 is
    open, with claim "none".
  * formal-conjectures 242.lean is unchanged since 09-18.
  * Dahan's GitHub repo was rebuilt on 11-15. It contains Papers I v2 and II v1 only (no Paper III); Paper I is "under
    review at The Ramanujan Journal" (README).
  * New ES GitHub repos (pottertech "NOT a proof", Tiny-ht certificate lab, derekblair) were found by repo search but
    not audited. GitHub code search was unavailable (401).
  * MathOverflow: none. Math.SE: unresolved (a snippet suggested a recent question but the API returned nothing).
  * Tao blog: nothing since 11-10.
* **Not done:** a Lean replay of Trybushnyi's package; an audit of any proof; the 11-20…22 listings; title-by-title reading
  of math.CO/AG outside the keywords; a re-read of the revised K-R-K paper.

## 3. Per-paper verdicts

| paper | verdict | exact content (✔ = re-read) and reason |
|---|---|---|
| **Trybushnyi 2611.14167** "The exponent 3/4 for the exceptional sets of K/n = 1/x+1/y+1/z" | **USABLE-INPUT (priority) + INSPIRATION (barrier, technique)** | ✔ Thm 1.1(a,b) l. 63–72; Cor 1.2 l. 74; Lemma 2.1 (Type II identity u = Kacd−1, u \| nc+a ⇒ K/n = 1/(abd)+1/(acdn)+1/(bcdn)) l. 217–224; Lemma 2.2 transfer cost (#E+1)^{2k} l. 243; real Kotecký–Preiss Cor 3.2 l. 364; Prop 11.1 barrier l. 1821; Lean App. C l. 2101ff. Averaged over n ≤ N, so nothing pointwise. Third independent arrival at 3/4 (after K-R-K and our note; Dahan II repaired to 3/4 in Z71 §2.1.1), first with explicit constants and uniform K. AI declaration: written with Claude Opus 5.x (l. 205–214). |
| **Jiang–Lau–Lü 2611.12467** (listed 11-09, not discussed in z71) "primes of the form u²+v²+1" | **USABLE-INPUT / NEW-METHOD for z81-gap** | ✔ Thm 1.1 l. 103–108 (Motohashi asymptotic, error saving √(log log x)); ✔ Iwaniec's EH-conditional route l. 116–130; ✔ method outline l. 132–171. Averaged over p ≤ x, which is what the gap lane needs (a supply of hard primes). Adapting it to b′₃ and b′₇ is an Assessment. |
| Nath–Xie 2501.16723 (2025) | ALREADY-COVERED (`Z54_HCKILL.md`, `Z55_P415.md`, FRONTIER l. 2074, 2171) | ✔ Thm 1.1 l. 112–115 (≫ x/(log x)^{5/2}, p = m²+n²+1, Ω(p+2) ≤ 9); ✔ Rem 1.2–1.3 l. 122–137 (vector sieve of mixed dimensions; ∏(p+a_i)). There is no double semi-linear version. |
| **Achenjang–Woo 2611.16062** | INSPIRATION (gap), NULL elsewhere | ✔ Thm A l. 135–162: Σ ∏Λ(L_i(x,y))1_P(N_{K/ℚ}(T₁(x)+T₂(y)α)) asymptotic for an imaginary quadratic K; the authors anticipate all nondegenerate binary forms (l. 163–165, a remark only). Linear L_i in the same variables, so it does not give joint shifted-form conditions. Applications: BM is the only obstruction to weak approximation for a conic-bundle family (rational points, not integral); rank-2 twists. |
| Gou–Wang–Xu 2611.18825 | NULL (conditional, wrong family) | S1: Landau's four problems with power saving under 2/2 ratios + GRH; no implication to or from BCR Conj. 1. |
| Grimmelt–Merikoski–Pandey–Pascadi 2610.41356 | ALREADY-SCREENED (z71 TSV), NULL | S1: primes n²+h for almost all h ≤ X^{1/2−o(1)}: averaged over h (B6). Harman sieve with a Type II beating parity is a technique note only. |
| Bettin–Drappeau–Lee 2610.42008 | NULL | S1: CLT for additive-twist central values; no new trilinear Kloosterman bound. |
| Kerr–Punch–Trudgian 2611.08816 | USABLE-INPUT (minor, explicit Burgess) | S1 Thm 1.1: log-free Burgess at prime moduli, explicit C(r); Cor: 37N^{1/2}p^{3/16} for N ≤ p^{5/8}, p ≥ 3·10¹². |
| Banks–Shparlinski 2610.19597 | INSPIRATION (s-u7), screen 9 | S1, see §0.5. |
| Ford–Gabdullin–Pratt 2611.15534 | NULL (calibration) | S2 Thm 1.1: H_{≥r}(x,y,2y) ≍ x log(2^r)/((log Y)^{1−E(θ)}(log log Y)^{3/2}), counted over n ≤ x. |
| Jain 2611.21136 | INSPIRATION (geom-comb), F1 trap | S2 Thm 1–2, see §0.5. Thm 2 is a BV-type average over q ≤ x^{153/256−ε}, uniform in the class. |
| **Gao–Geroldinger–Wang–Zeng 2611.24775** | **TRAP** for geom-comb | ✔ abstract; S2 Thm 1.1. vEB–K is false for n = 2k, k ≥ 3 odd, r ≥ 8n−7. |
| Zhi 2611.24034; Farnamfar 2611.19594; Matijasevick 2611.17205; Kuhlmann–Oertel–Wengiel 2611.14140; Pop–Rad–Ţurcaş 2611.20197; EGZ 2611.25050, 2611.15210; Harborth 2611.19508 | NULL | finite-set expansion and zero-sum constants; no divisor-set or class-of-one-integer content. |
| Dai–Li–Li–Yi 2611.15110 (covering systems: odd distinct ⇒ 45 \| lcm; min modulus < 14000, squarefree ≤ 7) | INSPIRATION (coverings target, STATUS §2 item 5, not a z81 lane) | S2: the distortion method plus joint convex comparison of residue-class indicator sums may sharpen positive-measure sterility certificates of the r = 17…79 kind. Untested. |
| Luca–Pink–Sándor 2611.20783; Sándor–Zakarczemny 2611.20799 | ALREADY-COVERED | S2, see §0.5 b2-duality. |
| Jiang 2611.24452; Berman–Kingsbury-Neuschotz 2611.23168 | NULL (wrong axis) | S3. |
| Zhao 2611.14226 (Cayley cubic N_U(B) ∼ c_Peyre B(log B)⁶) | ALREADY-COVERED | ✔ l. 79–91: ES embedding into the Cayley cubic and BM (Bright–Loughran) are known. Rational height counts. |
| Bhargava–Burungale 2611.16130; Sun 2611.14605, 2611.25002; Mazur–Rubin–Shlapentokh 2611.19103; Pasten–Vidaux 2611.24748; Visser 2611.18383; Ford (RGA) 2611.13697 | NULL | definability and undecidability over fields and rings of integers; no weak-arithmetic or ES content. |
| Agrawal 2611.06798 (z71 TSV) | NULL | S2: distinct unit-fraction representations with shifted Golomb-prime denominators; not 3-term. |
| Trey Li 2611.01793 (z71 TSV) | NULL | groups of prime units mod n. |
| Ji 2611.16665 ("QRH via ℚ[i]", 599/600 zero-free half-plane) | NULL (relabels conditionals at most) | abstract only; adds to the Z71 §2.4 QRH cluster; not audited. |
| Shao 2611.23488; Bazin–Klurman 2611.24117; Yang 2611.25495; Wang 2611.14161 (Sun ternary via Waldspurger: FRONTIER M1a power-size); Kiss–Sándor 2611.26555; Burrin–Gröbner 2502.17678 | NULL | averaged, or a power-size main term, or off-topic. |

**Bottom line (Assessment).** There is still no external mechanism that forces one tied divisor class at a fixed prime,
and nothing that passes 3/4. The one actionable *mathematical* lead is for z81-gap: JLL's unconditional Motohashi method. Applied to the
class-number-one windows k = 3, 7, it plausibly gives the single-window input (removing the omitted FHRSS Thm 3.9);
the two obstacles above block its extension to the FI09/W2 joint problem. The one actionable
*bookkeeping* item is the Trybushnyi priority correction. Round 2: sweep the 11-23 listing, re-read the revised K-R-K
paper (HEAD fe24ced5), and answer the lanes' literature queries. If z81-gap leans on JLL, the load-bearing theorem should
get an Astra cross-read.
