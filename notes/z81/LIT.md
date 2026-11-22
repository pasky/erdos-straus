Result: Trybushnyi (arXiv:2611.14167; Lean deposit Zenodo 23188522, **public 2026-10-06**) proves a 3/4 exceptional-set bound that is explicit, Lean-formalised and uniform in the numerator K with K^{−1/4}. It was public before our first m^{−1/4} commit (2026-10-08). Kandukoori–Ramesh–Kumar's 2026-11-06 revision is editorial only: 3/4 for m = 4 and for each fixed m, with constants depending on m and no uniform-m statement. Trybushnyi also proves an independent-model 3/4 barrier for square-sieve weights. No new pointwise mechanism has appeared. For z81-gap, Jiang–Lau–Lü's level-free Type I/II method (arXiv:2611.12467) plausibly ports to the single windows k = 3, 7; its Type II core (Thm 4.1) is b-free. Round-2 deep hunts for z81-specific-class, cap-zero, s-u7 and farey-proof found no usable new input.            Label: Assessment (literature screen); quoted statements are as stated in opened sources; no external proof was audited; the porting statements are Assessment (unverified)
Scope: Round 1 covered arXiv math.NT (247) and math.LO (64), 2026-11-10…19, plus keyword, author, version and web sweeps. Round 2 added the K-R-K revision history (three PDF versions, GitHub `sushaan-k/erdos-straus`), the Zenodo deposit dates, and targeted 2024–2026 hunts (a)–(d), several of them cut short by arXiv HTTP 429 (§4). It also read the JLL §§2–8 structure. The 11-20…22 listings were not yet announced and remain unswept. No ES proof or disproof exists anywhere; ES is OPEN.
Review: cross-lab Astra deep review `data/z81/xreview/REVIEW_LIT_OPUS_ASTRA.md` (fixes applied in the following commit); research-subagent extractions `data/z81/lit/notes/S1–S3, R2a–R2d` were read and spot-checked; ✔ items were re-opened by the author
Triage: DATA, plus one priority correction (REFUTATION/correction class for the STATUS §1A and §4 wording, below)
STATUS delta: §1A first bullet: replace "Kandukoori–Ramesh–Kumar's claim predates ours (`Z58_LIT.md`); Dahan gets 5/7 (`Z71_LIT.md`)" by "Kandukoori–Ramesh–Kumar's m=4/fixed-m claim predates ours (`Z58_LIT.md`). Trybushnyi arXiv:2611.14167 (Lean deposit public 2026-10-06, before our m-uniform note) proves E_K(N) ≤ N exp(−c((log N)³/K)^{1/4}) uniformly for 4 ≤ K ≤ (log₂N)³/2⁸⁵, with explicit c. So the initial-segment m^{−1/4} form is external; our short-interval/AP, prime-transition and SEL-conditional variants are not in it. Dahan gets 5/7 (`Z71_LIT.md`, `notes/z81/LIT.md` §0.4)." §4 Priority bullet: replace the second sentence by "Kandukoori–Ramesh–Kumar's (m=4 and fixed m) and Trybushnyi's (uniform K, explicit, publicly deposited 2026-10-06) 3/4 bounds predate ours by public/commit date; do not claim either as first."

# z81 LIT — literature and external-inspiration scout, 2026-11-10 … 2026-11-22 (Rounds 1–2)

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

This is the initial-segment case of our `paper/es-mn-short-note.tex` Thm A (z = 0), now **public, external and with
explicit constants**. Our Thm A says E_m((z,z+H]) ≤ CH exp(−c(log H)^{3/4}m^{−1/4}) uniformly in m ≥ 4 and z. Round 2
adds that Trybushnyi's Lean deposit with the uniform-K Theorem A was **public on Zenodo on 2026-10-06** (record
23188522 v1.0, API `created` field). That is earlier than our first commit containing m^{−1/4} (6af987ca6,
2026-10-08), so **we have no priority even internally-by-date** (§0.4). The paper cites neither K-R-K nor us; it says Vaughan's 2/3 stood "for more than fifty years" (l. 44–47) and
cites Dahan's 5/7 as concurrent. Our short-interval and AP variants and Thm U/L′ are not in it. Its §1 remark (l. 88–94)
recovers the upper side of our m/p density transition up to (log log)^4: E_K(N) ≤ N/(log N)² for
K ≤ c′(log N)³/(log log N)⁴. The lower side is Pomerance–Weingartner Thm 3.1, which is already cited in our note.
**Proposed delta:** the §0 header above. FRONTIER §1 "Exceptional set" should carry the same sentence.

## 0.4 Priority table for the 3/4 exceptional-set bound (Round 2; all from opened texts and APIs, proofs not audited)

| source (date evidence) | m = 4 | numerator m / K | constants, effectivity | barrier | pointwise | formal proof (as claimed, not replayed) |
|---|---|---|---|---|---|---|
| K-R-K v1: 38 pp., PDF dated July 29, 2026; GitHub page repo first commit 7a6356b4 2026-09-01, PDF sha ef7e7565 (`data/z81/lit/krk/krk_465815b8.txt`) | Thm 1.1: E(N) ≪ N exp(−c(log N)^{3/4}) | Thm 13.4 (l. 2392–2394): each fixed m ≥ 2, constants c_m, C_m. Uniform m **only CONDITIONAL** on Hyp 13.5: Thm 13.6 (l. 2459–2466) gives exponent (log N)^{3/4}/(φ(m)(m/φ(m))^{B_A}) for m ≤ (log N)^A, i.e. a 1/φ(m) loss, much weaker than m^{−1/4} | unspecified; BV-based | heuristic Remark only | none | Lean deduction of Thm 1.1 from nine named inputs, BV among them (l. 97–101) |
| K-R-K v2: 23 pp., still dated July 29, 2026; commits 7cdc9712…d96c7e30, 2026-10-30; sha 20a3290b = the Z58 archive | Thm 1 | Thm 2: each fixed m ≥ 4, constants depending on m. The conditional uniform-m section is **dropped** | Remark 7.2: ineffective via BV | Remark 1.2 (μ ≍ (log X)^k ⇒ k/(k+1); heuristic) | none | "proves Theorems 1 and 2 … using only Mathlib and Lean's standard axioms"; BV adapted from an open-source formalisation |
| **K-R-K v3 (revised, fe24ced5, 2026-11-06; sha e785d172; `krk/krk_fe24ced5.txt`)** | Thm 1 (l. 36–37), unchanged | Thm 2 (l. 39–45), unchanged: fixed m ≥ 4, c_m, C_m | unchanged (Remark 7.2 l. 1412–1414) | unchanged Remark 1.2 | none | the Mathlib-only/BV-credit sentence was shortened to "proves Theorems 1 and 2, the bound for exceptional primes, Example 1.1, and every numbered result of Sections 2–6" (l. 80–81). AI line: MIT CSAIL Mantis for Lean autoformalisation (l. 1415) |
| Trybushnyi: Zenodo 23188522 v1.0 (**2026-10-06**, Thm A ≙ paper Thm 1.1(b)); Zenodo 24017156 v2 (2026-11-06); arXiv 2611.14167v1 (2026-11-10) | E₄(N) ≤ N exp(−(log N)^{3/4}/8689) for N ≥ 2^{2^{64}} (Cor 1.2 ✔ l. 74) | **uniform** 4 ≤ K ≤ h³/2⁸⁵, exponent (log N)^{3/4}/(24(2³²K)^{1/4}) (Thm 1.1 ✔ l. 63–72) | explicit and effective ("everything is effective", l. 1874) | **Prop 11.1, proved and formalised**: independent-model square-sieve weights cannot pass 3/4 | none | full: 3171 declarations, no sorry (App. C l. 2101–2128; Zenodo descriptions) |
| ours: `paper/es-threequarter-note.tex` (first commit 4ecb5cb1d, 2026-09-06); `paper/es-mn-short-note.tex` Thm A (m^{−1/4} first in 6af987ca6, 2026-10-08); unposted | 3/4 | Thm A: **uniform in all m ≥ 4 and in short intervals (z, z+H]**; AP version; prime-transition Thm U; SEL-conditional sharp transition | ineffective (BV) | `paper/sieve-limits-note.tex`, z80 BEYOND_34 | none | none |

**Reading.** K-R-K is first for m = 4 and for fixed m: their PDF is dated 07-29 and their public repo dates from 09-01,
while our 3/4 note was first committed 09-06. Trybushnyi is first for the uniform-K initial-segment form (public
10-06; ours 10-08 and internal), and his is the only version with explicit constants, an effective threshold, a
proved barrier and a complete formal proof. What remains distinctive in our note, as far as these three sources
go: short-interval and arithmetic-progression uniformity, the bound for exceptional primes in short intervals, the
m/p density-transition statements, and their SEL-conditional sharpening. Novelty in the wider literature is
unverified. Neither K-R-K (any version) nor Trybushnyi cites the other (grep; Trybushnyi's reference list l. 2256–2298 ✔).

| lane | dispatch |
|---|---|
| **z81-specific-class** (break 3/4) | **Read Trybushnyi §11 ✔ (l. 1795–1890) before investing.** (i) *Bookkeeping law* (heuristic, l. 1796–1810): a mass L^β of classes at a cost of L^γ bits per event gives the exponent β/(β+γ). For Type II, β = 3 and γ = 1. Elsholtz–Tao's (log p)³ log log p solution count caps β at 3+o(1). So **any gain must come from γ < 1**: intersections of 2k ≍ µ events must be evaluated at total modulus far beyond N. (ii) *Barrier* Prop 11.1 ✔ (l. 1821–1825, formalised): in the **independent** model, for every Ψ that is a linear combination of ∏_{t∈T}1_{E_t} with ∏u_t ≤ ξ and Ψ = 1 off the events, E[Ψ²] ≥ exp(−(4/3)(48/K)^{1/4}(log ξ)^{3/4}). Selberg Λ² and, heuristically, the large sieve are of this form. The author's own conclusion (l. 1870–1873) is that a larger exponent "needs information about the exceptional set beyond the distribution of n in residue classes of modulus at most N". This corroborates z80 `BEYOND_34.md` §§13,16 from outside. **Consequence for the lane (Assessment):** large-modulus dispersion or bilinear Kloosterman input at a *fixed* level N^{1+δ} changes only the constant (it buys a factor 1+δ of bits, not γ < 1). A route past 3/4 must change the weight class, i.e. it must not be polynomial in event indicators, or it must use non-CRT structure of E, for instance that E is divisor-closed (Trybushnyi l. 128–133 uses this only for the small primes). Bettin–Drappeau–Lee 2610.42008 contains **no** new Kloosterman-fraction bound (S1). Gou–Wang–Xu 2611.18825 assume 2/2 ratios conjectures and give **no** implication to BCR Conj. 1 (S1). The Kotecký–Preiss/Dobrushin real cluster bound (Trybushnyi §3, Cor 3.2) is a reusable *technique* that removes log log losses in correlated inclusion–exclusion. It could clean constants in our 3/4 note and in its ≍ log log variants. **Round 2 (§4.1): no 2024–2026 theorem exploits divisor-closure or sparse prime support to beat residue-class sieving.** The nearest results are Banks 2609.37434 (a random-model p₁p₂ hits every class), Banks–Shparlinski 2610.19597 (almost all classes mod p^γ) and Chan 2506.04087 (multiplicatively closed sets of *positive density*). |
| **z81-gap** (g ≥ 11 i.o.) | **(1) FHRSS arXiv:2504.20289 is still v1** (API, 2026-11-22). The proof of Thm 3.9 is still omitted and no follow-up was found (keyword and author sweeps). **(2) New input:** Jiang–Lau–Lü arXiv:2611.12467 ✔ (Thm 1.1, l. 103–108) prove *Motohashi's conjecture*: Σ_{p≤x} b(p−1) = κ𝔖 x/(log x)^{3/2} + O(x/((log x)^{3/2}√(log log x))). Here b is the indicator of sums of two squares. The method (l. 132–171) is Vaughan's identity. Type I comes from Fouvry–Tenenbaum BV for b·W, with W built from auxiliary split primes. Type II is a mean square of b(mn−1) after extracting a | mn−1 with all p_ν ≡ 1 (4), so that b(ah) = b(h). Then harmonic switching, high moments and Selberg-sieve removal of W. *Lead (Assessment, unchecked):* both of our windows k = 3, 7 live in class-number-one fields Q(√−3), Q(√−7). The EXTREME §10 Thm I event "(p+k)/(k+1) is primitively F_k-represented" is the multiplicative indicator b′_k(n) = 1 iff every prime of n splits or ramifies, which has the same two structural features JLL use (FT-type BV; b′(ah) = b′(h) for split a). So JLL's method plausibly gives an **asymptotic, independent proof of the single-window FHRSS input for k = 3, 7**, removing the dependence on the omitted Thm 3.9. **(3) Joint windows: already mapped in the repo.** g ≥ 11 needs p+3 ∈ 4·b′₃ and p+7 ∈ 8·b′₇ on the *same* prime. `POINTWISE_WINDOW.md` (W2, l. 35–45, 520–527) identifies this as the window analogue of Friedlander–Iwaniec, *Hyperbolic PNT* (Acta Math. 2009), whose lower bound for p with p±2 both sums of two squares needs a level θ < 1 near 1. Sedunova arXiv:2609.28200 (abstract re-read, `tgt_sumsq.tsv`) still assumes a level x^θ for r(n−2)r(n+2). The sieve-level ledger is `Z55_P415.md` §0.2: semi-linear⊗semi-linear with switching needs level ≈ 1.22. FRONTIER l. 2165–2171 and `Z56_K4LIT.md` record no unconditional result; Nath–Xie arXiv:2501.16723 (Ω(p+2) ≤ 9, one semi-linear and one linear condition) is already cited there. **What is new is JLL.** Iwaniec showed that the Motohashi asymptotic follows from EH-level input, E(x, x^{1−ε}) (✔ l. 116–130). JLL get it unconditionally by replacing level with a Vaughan-identity Type I/II argument, so the single semi-linear problem is no longer level-limited. **Sharp question for the lane (Assessment, unverified):** does JLL's architecture prove FI09's lower bound, and hence W2? There are two concrete obstacles. Type I needs BV-type distribution of the *shifted product* b(n−2)b(n+2), which is not multiplicative, so Fouvry–Tenenbaum Thm 1.8 no longer applies (this is exactly Sedunova's assumed level). Type II needs auxiliary split divisors extracted from *both* mn−2 and mn+2 before the Cauchy–Schwarz over h. Equivalent reformulation: an integer point on the (2,2) quaternary quadric F₃(U,V) − 2F₇(U′,V′) = −1 with 4F₃(U,V)−3 prime. Achenjang–Woo Thm A ✔ (l. 135–162) needs *linear* L_i and does not apply. **Round 2: the exact porting hypotheses (H1)–(H7) are in §4.5.** In short, the Type II core JLL Thm 4.1 depends only on the auxiliary prime sets, so it ports verbatim with split auxiliary primes. Type I needs a Fouvry–Tenenbaum class check for modulus 3 or 7. The major arcs use the recent, unrefereed exclusion of Landau–Siegel zeros. |
| **z81-cap-zero** | Nothing new in the window bears on the common-exponent barrier r−1 | L. Kerr–Punch–Trudgian 2611.08816 ✔-abstract (S1: Thm 1.1 l. 62–94) remove the log from Burgess at prime moduli, with explicit C(r). This matters only if an explicit cap computation uses Burgess; it does not change e*. Ford–Gabdullin–Pratt 2611.15534 (order of H_{≥r}(x,y,2y), counted over n ≤ x; S2) is calibration only. **Trap:** it is not pointwise and has no residue class. **Round 2 (§4.2):** no 2025–2026 pointwise supply of primes r with r−1 | L, nor any bounded-denominator 3-term relaxation. The nearest items are Yang 2609.24347 (a lower bound for the density of p with P⁺(p−1) ≥ p^c), the conditional OpenAI-reported x^{1−o(1)} primes with P⁺(p−1) ≤ x^δ as quoted in Li–Zhuang 2610.15674 (unverified, already in the repo), and Czenky et al. 2507.03727 (Egyptian fractions over powers of one prime: a solution in rank R forces p−1 | R−1, a common-exponent-type divisibility constraint that is INSPIRATION only). |
| **z81-b2-duality** | No Vieta theorem for positive integral points. Jiang 2611.24452 (Vieta transitivity on Markoff mod p for p > 10^{320}, every D ≠ 4; S3) and Berman–Kingsbury-Neuschotz 2611.23168 (λ₂ along congruence families; S3) concern mod-p orbits of a fixed surface. **Trap:** a mod-p statement true for all large p also holds at n = m², so it fails F1 (`B2_ACROSS_FIELDS.md` already files Chen as the wrong axis). "Erdős' last equation" n(x₁+…+x_n) = x₁⋯x_n (Luca–Pink–Sándor 2611.20783: liminf log f(n)/log n = 0; Sándor–Zakarczemny 2611.20799: x_{n−1} ≤ n + max{d | 2n²−2n, d ≤ √(2n²−2n)}; S2) is a cousin of the amicable cubic p+e+b = ebt. Its divisor bound comes from the same factorisation (P′x−n)(P′y−n) = const that produces B2 here: ALREADY-COVERED. Zhao 2611.14226 ✔ (l. 79–91) records ES ⊂ Cayley cubic, [−n : 4t₁ : 4t₂ : 4t₃] ∈ S(ℚ), citing ET Rem 2.10 and Bright–Loughran. This is known; its height asymptotic is not integral or positive. |
| **z81-farey-proof** | math.LO window (64 titles) has nothing on IOpen, IE₁, IΔ₀, Shepherdson or Bézout models. The week's logic news is Hilbert's 10th over ℚ: Bhargava–Burungale 2611.16130 "ℤ is Diophantine in ℚ" (S3 Thm A l. 83–96), Sun 2611.14605 (26 unknowns; 16 under abc), Mazur–Rubin–Shlapentokh 2611.19103, Pasten–Vidaux 2611.24748. These are definability over fields, using elliptic curves and heights. There is no route to bounded-existential induction in discretely ordered rings: NULL for IE₁⁻ vs ES. Visser 2611.18383 (self-interpretations of S¹₂, Krajíček theories) is NULL. **Round 2 (§4.4):** there is no 2024–2026 paper on IE₁, IE₁⁻, IΔ₀ or IOpen divisibility, Farey or Gauss reduction by the listed authors. The new technique items are Kato 2608.12891 (a model of PA⁻_smu without Euclidean division: eventual-polynomial behaviour of one-variable terms plus finite avoidance plus compactness), Ježil 2505.14516 (PV₁ model with a nonstandard number without prime factorisation, CONDITIONAL on the hardness of factoring) and Hetzl–Weiser 2509.05653 (strict hierarchy of open-induction fragments). |
| **z81-s-u7** | Banks–Shparlinski 2610.19597 (S1, Thms 1.1–1.4): every reduced class mod p^γ is ℓ₁ℓ₂ℓ₃ with ℓ₁,ℓ₂ ≤ q and ℓ₃ ≤ exp(C(log q)^{2/3}(log log q)^{4/3}); binary EOS fails for at most φ(q)exp(−c(log q)^{1/3}…) classes. These are free primes, not divisors of one integer, and the modulus is fixed: screens 4 and 9, INSPIRATION at most. No new Rédei 4-rank or class-group-orbit paper in the window. Tang 2611.23465 (symmetric matrices of fixed determinant; 2-torsion of class groups announced for later) is remote. **Round 2 (§4.3):** the only joint same-parameter 4-rank theorem is Xu–Zhu 2608.00387 (asymptotic independence of 4-ranks of ℚ(√−d), ℚ(√−d₀d), averaged over squarefree d). It is already in `Z53_LIT.md`. No pointwise cross-field 4/8/16-rank relation was found. |
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
  paper"), with no commit since 11-10. Round 2 re-read all three PDF versions (§0.4); the revision is editorial.
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
  of math.CO/AG outside the keywords; the Fouvry–Tenenbaum 2022 class definition (§4.5 H1).

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
*bookkeeping* item is the Trybushnyi priority correction, sharpened in Round 2 by the 2026-10-06 Zenodo date (§0.4).
Still open: sweep the 11-23 listing; open FT 2022 Def. 1.1 for (H1); if z81-gap builds on JLL, get an Astra
cross-read of JLL Thm 4.1 and §7.

## 4. Round 2 (2026-11-22): targeted 2024–2026 hunts and the JLL porting audit

Subagent notes are in `data/z81/lit/notes/R2a–R2d` (opened texts are in `data/z81/lit/src/`). The verdicts below are mine,
after reading the notes and spot-opening the cited lines. **Coverage caveat:** the arXiv API returned HTTP 429 during
part of (a)–(d). (d) was re-run by me afterwards, complete: `r2d_kw.tsv` has 91 rows and `r2d_au.tsv` 305. The failed
queries are listed in R2a–R2c, so the negatives there are **not exhaustive**.

**4.1 (a) Divisor-closed sets / sparse prime support; z81-specific-class.** No theorem was found that exploits
divisor-closure, or support on a sparse prime set P_E, to save beyond residue-class sieving. No bilinear bound for
p₁p₂ ∈ Ω_q over a sparse P was found either.
* Banks 2609.37434 (R2a, Thm 1.1 l. 119–133): in Granville's random model, a.s. every class mod every large q is g₁g₂
  with g_i ∈ (X_q, 2X_q] and Θ > 3/4. A random model, not primes. INSPIRATION as a benchmark only.
* Banks–Shparlinski 2610.19597 Thm 1.2: almost all classes mod p^γ are products of two primes. Fixed modulus family.
* Chan 2506.04087 Thm 2 (l. 68–79): close points on a modular hyperbola with offsets in a multiplicatively closed M.
  It needs **positive lower density** of M, which is the opposite regime to P_E.

Assessment: the gap is genuine. "E divisor-closed ⇒ every prime factor of an exception is exceptional" gives only the
trivial E(N) ≪ #{n ≤ N : p | n ⇒ p ∈ P_E}. To exploit it one would need a *lower* density of non-exceptional primes in
the classes that the sieve misses, which is circular.

**4.2 (b) Smooth shifted primes / generation / restricted Egyptian fractions; z81-cap-zero.** NULL for the barrier
r−1 | L (R2b).
* Yang 2609.24347 Thm 1.1 (R2b, l. 75–83): liminf T_c(x)/π(x) ≥ max(1−ρ(16/(5c)), 1−c+g(c)) for P⁺(p−1) ≥ p^c. This
  is a large-factor frequency, the wrong direction.
* The OpenAI smooth-shifted-prime claim quoted in Li–Zhuang 2610.15674 (l. 41–64) is reported as unverified and is
  already in the repo.
* Klurman–Shparlinski–Teräväinen 2609.25393 and Hughes 2610.04678 are ALREADY-COVERED (almost all q).
* Czenky–McGovern–Plavnik–Rowell–Watkins 2507.03727 Cor 2.9 (l. 198–202): "If there exists a solution in rank R, then
  p−1 divides R−1" (1 as a sum of unit fractions with p-power denominators). A clean instance of a common-exponent
  constraint, not a supply.

**4.3 (c) Joint class ranks; z81-s-u7.** The only joint same-parameter theorem is Xu–Zhu 2608.00387 (R2c).
* Thm 1.1 (l. 141–147): d_TV of the joint 4-rank law of ℚ(√−d), ℚ(√−d₀d) from π_CL⊗π_CL is ≪ (log log X)^{−c}. It is
  **averaged** over squarefree d, with no prime-subfamily statement.
* Thm 1.3 (l. 178–186): density-one transfer of 2-primary structure.
* It is ALREADY-COVERED (`Z53_LIT.md`). The deterministic relation it mentions is genus-theoretic 2-ranks only
  (l. 78–82). Governing-field items (2505.20117, function fields; 2407.03754, genus) are NULL.
* **No pointwise 4-, 8- or 16-rank cross-field relation at a fixed p was found in 2024–2026.** The classical pre-2024
  joint 16-rank results for ℚ(√−p), ℚ(√−2p) are cited in Xu–Zhu (l. 94–100) and were not re-screened here.
* Author query failed with 429, so this negative is non-exhaustive.

**4.4 (d) Weak arithmetic; z81-farey-proof** (re-run complete).
* No 2024–2026 paper by Jeřábek, Boughattas, Smith, Otero, Wilkie, Macintyre, D'Aquino, Berarducci, Kołodziejczyk or
  Thapen on IE₁, IE₁⁻, IΔ₀, IOpen + Bézout, Gauss reduction or Farey fractions.
  * Jeřábek 2404.06888 (exponential integer parts; IE₂ ⊢ TEIP) is NULL for divisibility.
  * The other listed hits (D'Aquino–Macintyre 2411.08808; Gruza–Kołodziejczyk–Łełyk 2512.09120;
    Kołodziejczyk–Sun 2604.01808) are off-target.
* Relevant technique items:
  * **Kato 2608.12891** (abstract read): PA⁻_smu ⊬ Euclidean division. The method is "every one-variable term eventually
    agrees with a polynomial over the dyadic rationals" plus a finite avoidance lemma plus compactness. INSPIRATION for
    building normal discretely ordered models in which a division or Farey step fails; new to the repo.
  * **Ježil 2505.14516**: CONDITIONAL on factoring hardness, a PV₁ model with a nonstandard m having no prime
    factorisation. A cautionary parallel to the campaign's "divisibility-minimal failure" screen, in a different
    theory; new to the repo.
  * Hetzl–Weiser 2509.05653 Thm 4.4 (R2d, l. 319–330): a strict hierarchy of open-induction fragments. NULL.
  * Enayat–Łełyk–Visser 2508.14758 (IE₁ + Coll ⊢ PA) is ALREADY-COVERED.
  * Thamrongthanyalak, "Quadratic forms in normal open induction", MLQ 70 (2024) is ALREADY-COVERED (`Z64_UNPROV.md`,
    `Z65_LOGIC2.md`).

**4.5 (e) Porting Jiang–Lau–Lü 2611.12467 to b′₃((p+3)/4), b′₇((p+7)/8); z81-gap.** Each item is a hypothesis the
port needs, or a pitfall; all ✔ re-read in `src/2611.12467.txt`. Here b′_k(n) = 1 iff every prime factor of n
splits in ℚ(√−k), with ramified k excluded automatically since k ∤ F for p prime. The k = 7 windows divide by 8, not 4.
* **(H1) Type I = Lemma 3.1 (l. 285–372).**
  * JLL deduce BV at level q ≤ x^{0.41}, 4 ∤ q, for f = b·W from Fouvry–Tenenbaum (Trans. AMS 375 (2022)) Thm 1.8,
    applied to the multiplicative b_t = b·∏t_ν^{ω_ν} in the class **F(4,2)**. Membership needs prime values depending
    only on p mod 4 within a spacing-2 band sequence (l. 330–352).
  * For b′_k the prime values depend on p mod 3 (k = 3) or on (p/7) (k = 7). **Must check** that FT Definition 1.1
    allows a general modulus D, presumably F(3,2), F(7,2) or F(12,2), F(28,2), with the matching analogue of the
    "4 ∤ q", q₄ = (q, 4^∞) main-term adjustment (l. 339–346). FT itself was not opened here.
  * Also b′_k(p^j) = 0 for every inert p and j ≥ 1, unlike b(p²) = 1. This is simpler, but the local factors change.
* **(H2) Type II = Prop 4.2 (l. 800–835).**
  * The only arithmetic use of b is "every auxiliary prime ≡ 1 (4) ⇒ b(ah) = b(h) without coprimality" (l. 815–816),
    then Cauchy over h.
  * **Thm 4.1, the mean square Q_Y (l. 787–797), "uses only (4.1)"** (l. 776–777): prime sets in the bands
    [exp(Lϑ_ν), exp(2Lϑ_ν)] with 1/4 ≤ V_ν ≤ 1/2.
  * Split primes in ℚ(√−3) or ℚ(√−7) have relative density 1/2, so V_ν = ½log 2 + o(1). **So §§5–7 port verbatim**
    for the auxiliary sets, and b′_k(ah) = b′_k(h) holds for split a.
  * Pitfall: Q_Y is defined through mn − 1 = ah. Our prime variable is p = 4n − 3 (or 8n − 7), so the relation becomes
    mn + 3 = 4ah (or mn + 7 = 8ah). The determinant relation cmn − ars = c − a (l. 158, (5.1) l. 892) and the §5.3 kernel
    (l. 1007–1012) must be redone with the shift and multiplier. Assessment: routine but **not checked**.
* **(H3) Major arcs, §7 (l. 2118–2135).** These use "the exclusion of Landau–Siegel zeros (see [1, 11])": Banks
  arXiv:2610.15483 on the OpenAI proof that Landau–Siegel zeros do not exist, and Green Hexagon:2610.00311. Both are
  **2026, unrefereed**, and needed for L(s,χ*)⁻¹ ≪ log q* + (log(|u|+3))^{3/4} for q* ≤ L^B.
  * A port is therefore PROVED only **rel. that exclusion**.
  * Assessment, unchecked: since q* ≤ L^B and σ₀ = 1 − ¼c₀L^{−3/4}, Siegel's ineffective theorem with ε < 3/(4B) may
    suffice, at the cost of effectivity.
* **(H4) Harmonic switching / high moments, §§5–6.** They "follow closely the method of [30, 22]" (l. 160–161):
  OpenAI, "Poisson–Dirichlet law for prime predecessors" (2026 preprint), and Lü–Wang–Wu arXiv:2610.20242 (2026).
  Both are unrefereed dependencies.
* **(H5) Weight removal, §8 (l. 2500–2531).** The Selberg sieve uses the local densities g_b(p) = 1/p or 2/p − 1/p².
  For b′_k, inert p must exclude every n with p | n, not only p ∥ n. Modulo p² that is p + p disjoint classes,
  so g(p) = 2/p − 1/p² becomes 2/p, and the prime condition reads p ∤ 4n − 3 (or p ∤ 8n − 7). Routine.
* **(H6) The main-term Euler product (§3.3, l. 632–700) changes** (Landau–Ramanujan κ → the ℚ(√−k) analogue, with
  L(1, χ_{−k})^{1/2}). The 2-adic step "b(2n) = b(n)" (l. 665) fails for k = 3, because 2 is inert in ℚ(√−3), so
  b′₃(2n) = 0. It holds for k = 7, because 2 splits. Redo the reduction (3.13).
* **(H7) Theorem I side conditions** (`notes/z80/EXTREME.md` §10: primitivity and p ≡ 1 mod m for ℓ ∈ {3,5,7}) add
  fixed congruences on p. They are compatible with BV and FT at bounded cost.
* **Net (Assessment).** A port would give an **asymptotic** single-window count for k = 3, 7, PROVED rel. (FT class
  check) + (Landau–Siegel exclusion or a Siegel substitute) + [30, 22], and would remove the omitted-FHRSS-Thm-3.9
  dependence for these k. **It does not give the joint k = 3, 7 count.** In Prop 4.2 the second indicator b′₇(ah + c)
  sits inside the Cauchy–Schwarz and cannot be removed. The joint Type I also needs the distribution in arithmetic
  progressions of the non-multiplicative b′₃(n)b′₇(n + c′) (FI09/Sedunova's open input). **Nothing here is PROVED for
  ES or for g ≥ 11.**
