# Novelty audit 2026-10b (task O70): tools and results of the OMEGA9–17 / WINDOW / KARY3 round

**Auditor:** side agent O70 (branch `side-agent/novelty-audit-2`). This is a priority audit,
not a proof check. Correctness is taken from the cited internal reviews.

## Search limits (read first)

* **No internet in this pass.** Only `sources/`, `LITERATURE_2026.md`, the earlier audits
  (`reviews/novelty-audit-2026-10.md`, `reviews/novelty-audit-omega8.md`,
  `reviews/lit-audit-*.md`) and the auditor's own background knowledge were used.
* **Tags.**
  * **[checked in sources/…]**: the claim was read in the archived file named.
  * **[memory]**: the claim is from the auditor's recollection. Theorem numbers, constants,
    years and venues may be wrong. A [memory] claim of the form "X does not contain Y" is
    weak evidence.
* **TCS literature in the archive:** only BGP (arXiv:1201.3261), PYY (arXiv:0801.0059)
  and BEKK (arXiv:2407.18688). None of the following is archived: LMN, Håstad, Mansour,
  Tal, Lecomte–Tan, Bazzi, Razborov, Braverman, the LLL papers, Janson,
  Riordan–Warnke, Gallagher, Maynard, Opera de Cribro.
* **"Apparently new"** means that neither the archive nor the auditor's memory contains
  the result. It is **not** a priority certificate.
* **Confidence** is the auditor's probability that a competent specialist search would
  *not* turn up an essentially identical prior statement. Its levels:
  * low < 50%;
  * medium 50–80%;
  * high > 80%.

---

## 1. Energy bound C-1 / Conjecture Q and the DNF Fourier tail `W^{>t} ≤ 4·2^{−(t+1)/k}`

**Objects.** All are PROVED and reviewed: R38, R38b, R50 (all SOUND).
* `POINTWISE_OMEGA10.md` §3 and `paper/energy-dnf-note.tex`, Theorem 1.1. Let F be the
  avoidance indicator of a family of cylinder events on a finite product space with **any
  product measure**. If `λ^{supp E} ≤ 2` for every event, then
  `G_F(λ)=Σ_U λ^U‖F^{=U}‖² ≤ 1`. The constant 2 is sharp (Prop. "single").
* Thm 4.3 ("Conjecture Q"): for a hypergraph with all edge weights `≤2`,
  `Q_μ(H) ≤ Π_{J∈M}(w_J−1)`.
* Lemma 4.2: `|Θ_λ| ≤ Π_{J∈M}(w_J−1)` for `Θ_λ(C)=Σ_{J⊆C}(−1)^{|J|}λ^{∪J}`, by
  deletion–contraction.
* Corollaries 1.2–1.3:
  * `energy(F;t) ≤ 2^{−(t+1)/k}a(2−a)`;
  * width-k DNF tails `W^{>t} ≤ 4p(2−p)2^{−(t+1)/k}` under every product measure and alphabet;
  * the base `2^{−1/k}` is sharp over all product spaces;
  * on the uniform cube the rate lies between `3^{−t/k}` and `2^{−t/k}`.
* Thm 7.1: the filtration (digit-weighted) variant.

**Closest known results.**

| Prior work | What it gives | Relation |
|---|---|---|
| LMN (JACM 1993) + Håstad's switching lemma (STOC 1986) [memory] | Width-w DNF ε-concentrated up to degree `O(w log 1/ε)`. O'Donnell, *Analysis of Boolean Functions* §4.4, states `W^{≥t} ≤ 2·2^{−t/(20w)}` [memory; the constant 20 is uncertain, but R50 D9 re-derives ≈18.8 from the switching route] | Same *shape*. The campaign's exponent constant is 1 instead of ≈20, and the proof has no restriction. |
| Mansour (JCSS 1995) [memory] | DNF sparsity, and the degree bound via the switching lemma with an unspecified constant | Uses the LMN bound as input. Not an improvement of it. |
| Håstad, "A slight sharpening of LMN" (JCSS 2001) [memory] | Improves the log-size / depth dependence for AC⁰. As recalled, it is not a width-w explicit-constant DNF tail | Must be checked. It is the most likely place for a sharp DNF constant. |
| Tal, "Tight bounds on the Fourier spectrum of AC⁰" (CCC 2017) [memory; the note says it was checked online earlier, `reviews/energy-dnf-note-review.md` §6] | `W^{≥t} ≤ 2·2^{−t/O(log s)^{d−1}}` and level-k ℓ¹ bounds. No explicit-constant width-w DNF tail | Different norm (ℓ¹ growth) and unspecified constants. |
| Lecomte–Tan (FOCS 2021) [the bibliographic data and Facts 6 and 9 were checked online in an earlier pass, per R50 §6; the paper itself is not archived] | Fact 9: `|ĝ(S)| ≤ 2^{|S|}·Pr[S covered]` (unsigned, uniform cube). Fact 6: LMN with an unspecified C | The cover device is the ancestor of Lemma 3.1. The *signed* cover count, the polarization and Θ steps, and the all-levels weighted ℓ² form are not in it (per the note §1 and R50). |
| Lovett–Wu–Zhang, "Decision list compression by mild random restrictions" (STOC 2020) [memory, low confidence about content] | Width-w DNFs under *constant-rate* restrictions compress to small decision lists | **New lead not named in the note.** Mild restrictions avoid the p≈1/(5w) loss of the switching route, so they may give `W^{≥t} ≤ 2^{−t/(Cw)}` with a small C. Must be checked. |
| Furst–Jackson–Smith (COLT 1991); Blais–O'Donnell–Wimmer (COLT 2008 / ML 2010) [memory] | LMN-type concentration under product distributions. In FJS the degree bound degrades with the bias. BOW cover general finite product domains via a generalized noise operator | Corollary 1.3 has **no bias dependence**. That is the selling point most exposed to these papers. Under a p-biased switching lemma the dependence could plausibly be removed by known methods. |
| Boppana (IPL 1997), Amano (ToC 2011) [memory] | Width-w DNF/CNF total influence `≤2w`, resp. `≤w` | Not beaten: the note concedes its `(4k/ln2)p` is weaker. |
| Hypercontractivity on product spaces: Bonami–Beckner, Oleszkiewicz/Wolff for biased spaces, global hypercontractivity of Keevash–Lifshitz–Long–Minzer [memory] | Bounds on `‖T_ρ f‖_2` for **ρ<1** in terms of `‖f‖_q`. On small-bias spaces the constants blow up unless f is "global" | Theorem 1.1 is a `ρ>1` statement (`G_F(ρ²)=‖T_ρF‖²`). Hypercontractivity does not imply it. Like the global theory, the hypothesis is per-event and bias-free, but the auditor knows no ρ>1 bound for avoidance indicators there. |
| Fourier growth / PRGs (Chattopadhyay–Hatami–Hosseini–Lovett ITCS 2019; Chattopadhyay–Hatami–Lovett–Tal; Tal 2017) [memory] | Level-k **ℓ¹** bounds `L_{1,k}(f) ≤ (Cw)^k` for width-w DNF/AC⁰ | `G_F` is weighted **ℓ²** growth. ℓ¹ growth bounds do not imply the ℓ² weighted bound with constant base 2 (wrong norm and unspecified C). No ℓ² ρ>1 "growth ≤ 1" statement is recalled. |
| Kelley–Lovett–Meka (NOF separations 2023; the Kelley–Meka 3-AP "sifting"), and Lovett–Solomon–Zhang / Alweiss–Lovett–Wu–Zhang (spread families, DNF compression) [memory] | Spreadness / sunflower structure of DNFs | Different questions (structure, density increment). The auditor recalls no Fourier-tail constant from these. |
| Signed inclusion–exclusion `Θ_λ` | For `λ_v ≤ 1` (a probability), Θ is a probability of avoidance, so `0 ≤ Θ ≤ 1` is trivial. For `λ_v ≥ 1` it is the analytic continuation. Cf. Scott–Sokal [checked in sources/scott-sokal-0309352.pdf only as to its topic: the independence polynomial at negative fugacity and the LLL] | Lemma 4.2's bound `|Θ| ≤ Π(w_J−1)` under `w_J ≤ 2` is a zero-free/boundedness statement of the same *flavour* as the Shearer / Scott–Sokal region. The auditor knows no identical statement, and the deletion–contraction proof is elementary. |

**What is genuinely new (apparently).**
1. **Theorem 1.1 / Thm 4.3 as stated.** A per-event weight hypothesis gives `G_F ≤ 1`
   uniformly over product measures and alphabets, with the sharp constant 2. The
   polarization → signed-cover → deletion–contraction proof avoids random restrictions.
   *Confidence: medium.* The statement is clean and the auditor recalls nothing like it.
   But ρ>1 noise bounds for DNFs are a natural question, and the Fourier-growth and
   global-hypercontractivity communities are large.
2. **The constant 1 in the DNF tail exponent, `W^{>t} ≤ 4·2^{−(t+1)/k}`, and the
   bias-free product-measure version.** *Confidence: low–medium.* Constants in LMN-type
   tails are rarely optimised, so a small-C version may sit inside a mild-restriction or
   sharp-switching paper (Lovett–Wu–Zhang; Håstad 2001; Rossman) without being
   advertised. The sharpness facts are apparently new as stated (*medium*):
   * base 2 is optimal over all product spaces;
   * on the uniform cube the rate lies in `[3^{−t/k}, 2^{−t/k}]`.
3. **The modulus-weighted / filtration form (Thm 7.1) and its use as a sieve error
   bound.** It is new as an application (*high*, consistent with
   `novelty-audit-omega8.md` (ii)). This is the part that matters for ES.

**Not new.** The Efron–Stein machinery and the identity `G_F(ρ²)=‖T_ρF‖²` are standard,
and so is the influence corollary (weaker than Boppana/Amano, as conceded). The cover
device is in Lecomte–Tan (Fact 9).

**Must-check list before external submission:**
* Håstad 2001;
* Lovett–Wu–Zhang 2020;
* Furst–Jackson–Smith 1991 (bias dependence);
* Blais–O'Donnell–Wimmer;
* Rossman's entropy switching lemma;
* the Fourier-growth line: CHHL 2019 and Chattopadhyay–Hatami–Lovett–Tal;
* KLLM global hypercontractivity (whether any ρ>1 bound for "global" Boolean functions
  covers avoidance indicators).

The note's current hedge ("We believe Theorem 1.1 and the constant 1 … are new, but we
make no priority claim") is **appropriate**. It should add Lovett–Wu–Zhang to the
must-check list.

---

## 2. Janson-type inequality for one-hot product spaces under the lopsided LLL (`POINTWISE_HAAR.md` Thm 1.4)

**Object.** The setting is atomic events (partial assignments) `E` on a product of independent
finite variables. Hypothesis: the lopsided local lemma holds with `Γ(E)` = the events
*conflicting* with `E`. Write `K = max_E Π_{E'∈Γ(E)}(1−x_{E'})^{−1}`, let `μ = ΣP(E)`, and
let `Δ` be the sum over **compatible** (bit-sharing) pairs only. Then

* `−log P(Av) ≥ μ − KΔ`, and
* `−log P(Av) ≥ min(μ/2, μ²/(4KΔ))`.

It is PROVED and reviewed (`reviews/pointwise-haar-review.md`). Inside the same file:

* Lemma 1.1 (compatible events);
* Lemma 1.2 (NA of one-hot vectors ⇒ product bound);
* Lemma 1.3 (lopsided LLL + inflation bound).

**Closest known results.**

| Prior work | What it gives | Relation |
|---|---|---|
| Janson (1990); Janson–Łuczak–Ruciński; the Boppana–Spencer proof (Alon–Spencer, *The Probabilistic Method*, Ch. 8) [memory] | For up-sets `B_i ⊆ R` of a random subset R: `P(∧B̄_i) ≤ e^{−μ+Δ/2}` and `≤ e^{−μ²/(2Δ)}` in the extended form. Proof: `P(B_i | ∧_{j<i}B̄_j) ≥ P(B_i) − Σ_{j<i, j~i} P(B_i∧B_j)`, via Harris/FKG | **Thm 1.4 is exactly the Boppana–Spencer chain** with the one Harris step replaced by an LLL conditional bound (cost K). The extended-Janson step (random subfamily, `p = μ/(2KΔ)`) is the textbook trick verbatim. |
| Riordan–Warnke, "The Janson inequalities for general up-sets" (RSA 2015) [memory] | Janson for arbitrary up-sets in a product of independent Bernoullis (not just principal up-sets) | Still monotone/Harris-based. One-hot variables (`P(X=r | X≠r') > P(X=r)`) are *not* covered. This is precisely the gap Thm 1.4 fills, as Remark (ii) says. |
| Erdős–Spencer, "Lopsided LLL and Latin transversals" (1991) [memory] | Lopsided LLL. The conflict graph is a lopsidependency graph for atomic events in the variable setting (standard: SAT, Latin transversals) | Lemma 1.3, first half: **known** (correctly labelled "standard"). |
| Haeupler–Saha–Srinivasan, "New constructive aspects of the LLL" (FOCS 2010 / JACM 2011) [memory] | "LLL distribution": `P(A | ∧Ē) ≤ P(A)·Π_{E∈Γ(A)}(1−x_E)^{−1}` | Lemma 1.3's inflation bound: **known**; it should cite HSS. The campaign already cites HSS elsewhere (`novelty-audit-2026-10.md` 1e). |
| Lu–Székely, "Using the Lovász local lemma in the space of random injections" (EJC 2007) and "A new asymptotic enumeration technique: the LLL" (arXiv 0905.3983, ~2009) [memory, **medium–low confidence about content**] | Lopsided/negative-dependency LLL lower bounds `P(∧Ā) ≥ Π(1−x)`, matched with **upper bounds of Janson type** for enumeration (matchings, permutations, Latin rectangles). As recalled, the upper bound is proved by conditional probabilities along an ordering in a negative-dependency setting | **Closest suspected prior art.** If their upper-bound theorem is stated for a general lopsidependency graph, then Thm 1.4 is essentially a special case or a sibling, transferred from random injections to product spaces. Must-check. Mohr's thesis (USC 2013, Lu's student) [memory] is the second place to look. |
| Joag-Dev–Proschan (1983) [memory] | Negative association of multinomial/one-hot vectors | Lemma 1.2: **known** (correctly labelled). |
| Mousset–Noever–Panagiotou–Samotij (Ann. Probab. 2020) [memory] | Cumulant expansion of `−log P(no copy)` beyond Janson | Monotone binomial setting. Not a competitor. |

**What is genuinely new (apparently).**
* A clean Janson inequality for **atomic events on general product spaces**, with:
  * conflicts charged only through the LLL factor K;
  * only compatible pairs entering Δ.

  As a statement this is apparently new (*confidence: low–medium*, mainly because of
  Lu–Székely / Mohr). The proof technique is **not** new: Boppana–Spencer plus HSS. It
  should be presented as "a routine combination of the Boppana–Spencer proof with the
  HSS inflation bound; we found no statement in this form".
* The **application**: the lower bound `Φ(T) ≫ 𝓛³/log𝓛` for the Haar avoider exponent
  of the ES system (§2) and the packing barrier Prop 1.5. Both are new (*high*); see item 6.

**Not new.** Lemmas 1.2 and 1.3 (already labelled standard). Lemma 1.1 is an elementary
observation that underlies the lopsided-LLL treatment of SAT-type conflict graphs
[memory].

---

## 3. The β-weighted local lemma (`POINTWISE_OMEGA13.md` Lemma 1.1)

**Object.** On a product space, set `x_E = β^{s(E)}P(E)` and `η = (3/4)log β`. If the
per-coordinate sums `w̃_ℓ = Σ_{E∋ℓ} x_E ≤ η` for every coordinate, then:

* `P(∩Ē) ≥ exp(−(4/3)Σ x_E)`;
* `P(E | ∩_𝒮F̄) ≤ x_E`;
* `P(A | ∩_𝒮F̄) ≤ β^{|supp A|}P(A)`.

It is PROVED (R48–R48c).

**Closest known results.**
* **Asymmetric LLL** (Lovász; Spencer 1977; Alon–Spencer Ch. 5, Lemma 5.1.1) [memory].
  The proof *is* the asymmetric LLL with a specific choice of `x_E`. The only step beyond
  verifying the hypothesis is the standard estimate `−log(1−x) ≤ (4/3)x` for `x ≤ 1/4`.
* **Size-exponential weights in the variable setting** [memory].
  * The choice `x_E ∝ c^{|E|}P(E)` is the classical device for **non-uniform** hypergraph
    problems: the Erdős–Lovász (1975) non-uniform Property B criterion and Beck's
    non-uniform colouring arguments.
  * It is also the standard "per-variable" corollary: if every variable lies in events of
    total weight `Σ_{E∋v}(1+ε)^{|E|}P(E) ≤ c(ε)`, the events are avoidable. This appears
    in many textbook exercises and in algorithmic-LLL papers in the per-variable form.
  * The auditor cannot give an exact citation with these constants, but the pattern is
    folklore.
* **Conditional / "LLL-distribution" bound** `P(A|∩F̄) ≤ P(A)Π(1−x_F)^{−1}`:
  Haeupler–Saha–Srinivasan (JACM 2011) [memory]. The file already cites it.
* **Cluster-expansion and Shearer refinements** (Bissacot–Fernández–Procacci–Scoppola
  2011; Kolipaka–Szegedy; Scott–Sokal) [Scott–Sokal checked in
  `sources/scott-sokal-0309352.pdf` for topic only]. These sharpen the region. They are
  not needed here.

**What is genuinely new.** Nothing at the level of the lemma.
* Lemma 1.1 is a **routine instance of the asymmetric LLL**. The file's label "PROVED" is
  fine, but it should also say "standard" (as POINTWISE_HAAR Lemma 1.3 does).
* *Confidence that the lemma is not new: high.*
* The campaign-specific content is the **parameter choice** `β = 1+1/log𝓛`, which makes
  the per-coordinate threshold `η ≍ 1/log𝓛` independent of the prime ℓ and of the level.
  This replaces O11's `θ ≍ log ℓ/𝓛`.
* That choice drives the 1/5 → 1/4 step for the ES witness modulus (item 6). It is part
  of the *application's* novelty and should not be presented as a new local lemma.

**Recommended wording.** "Lemma 1.1 (a standard per-coordinate form of the asymmetric local
lemma with weights `x_E = β^{|supp E|}P(E)`; cf. Alon–Spencer Lemma 5.1.1 and HSS for the
conditional bound)."

---

## 4. The planting lemma (`POINTWISE_OMEGA14.md` Lemma 1.1) and the level barrier (Thm 1.3)

**Object.** Let the bits be independent with `P(b_i=1)=p_i`. Put `r_i=p_i/(1−p_i)`, `R=Σr_i`
and `r*=max r_i`. If `R ≥ (k+1)+(2k+1)r*`, then there is a law ν with the same
≤k-dimensional marginals as μ and `ν(b=0)=0`. The construction is explicit: it adds
signed Möbius charges σ_J on (k+1)-sets with weights `∝ Π_J r_i`. The lemma is PROVED
(R49, R49b) and verified exactly for k ≤ 3 (`verify.py` (dg)).

Thm 1.3 is the dual statement: no level-k big-junta minorant `B ≤ F` keeps the mass of the
fibres where `R ≥ (k+1)+(2k+1)r*`. The file itself already says "No novelty is claimed for
Lemma 1.1".

**Closest known results.**

| Prior work | What it gives | Relation |
|---|---|---|
| **BGP, arXiv:1201.3261, §4.9, Prop 26 and Thm 27** [checked in `sources/lit2026/audit-arxiv-1201.3261v1.txt`, ll. 604–635, 1125–1135] | `m(n,k,p) = min_{Q∈A(n,k,p)} Q(all ones)` and `n_c(k,p) = min{n : m(n,k,p) = 0}`. For p ≥ 1/2: lower bound `n_c ≥ k/(2(1−p))+1` (k even), `(k+1)/(2(1−p))` (k odd), via the truncated moment problem. **Upper bound only for `1−p = 1/q`, q a prime power:** `n_c ≤ C·k/(1−p)·log(1/(1−p))`, via a Gilbert–Varshamov orthogonal array and a greedy symbol map | **This is exactly the identical-marginal case of Lemma 1.1** after flipping bits (BGP's p ↔ campaign `1−p_i`). Lemma 1.1 gives `n_c(k,p) ≤ (k+1)p/(1−p)+2k+2`. That removes BGP's `log(1/(1−p))` factor and the prime-power restriction, and lands within a factor ≈2 of BGP's lower bound (14). It also handles **non-identical marginals**, which BGP do not treat. |
| PYY, arXiv:0801.0059 [checked in `sources/lit2026/audit-arxiv-0801.0059v3.txt`, ll. 149–260] | The *maximum* `M(n,k,p)` of the AND probability (the sieve-majorant side) | The other side of the same LP. Not a competitor for planting. |
| BEKK, arXiv:2407.18688 [checked in `sources/lit2026/audit-arxiv-2407.18688v1.txt`, abstract] | Exact formulas for the maximum `M(n,k,p)` only | Does not treat `m` or `n_c`. |
| Bazzi (FOCS 2007 / SICOMP 2009); Razborov (TOCT 2009); Braverman (JACM 2010) [memory] | LP duality: k-wise independence ε-fools f ⇔ degree-k sandwiching polynomials exist | Thm 1.3 ⇐ Lemma 1.1 is the **minorant half of Bazzi's duality**, specialised to the extreme `ν(F=1)=1`. The duality itself is known; the campaign's Remark (i) says so. |
| Even–Goldreich–Luby–Nisan–Velicković (1998) [memory, via BGP ref. [16]]; Alon–Goldreich–Mansour, "Almost k-wise independence versus k-wise independence" (IPL 2003) [memory] | EGLNV: k-wise independence fools OR/AND and combinatorial rectangles with error `2^{−Ω(k)}` (Bonferroni). AGM: statistical distance between almost-k-wise and k-wise laws | Lemma 1.1 is the **converse** of EGLNV-type fooling for OR. With mean count `R ≳ 2k`, a k-wise law can make OR identically true. So the Bonferroni level `k ≍ S` is necessary for a lower-bound sieve. The auditor knows of no statement of this converse with arbitrary marginals and a linear threshold. AGM is not related beyond topic. |
| Prékopa (1988/1990) discrete moment problem; Boros–Prékopa Bonferroni optimality [memory] | Sharp Bonferroni-type bounds for `P(S=0)` from the first k binomial moments | The **exchangeable** case of Lemma 1.1 is a statement about this moment problem (`P(S=0)` can be 0 given k binomial moments). It is in principle decidable by Prékopa's / BGP's moment criteria, but BGP's discrete-support upper bound shows it had not been worked out sharply. |
| Sieve-theoretic lower-bound limits: the β-sieve sifting limit, the Selberg parity example, Tao 254A Notes 4 duality [the duality is checked in `sources/lit2026/audit-tao-254a-notes4-sieve-theory.md`; the rest is memory] | A lower-bound sieve of level D is positive only above the sifting limit | Thm 1.3 is a *combinatorial-level* (number of big coordinates) analogue. Its level is "k coordinates", not "modulus D". Analogous, not identical. |

**Exploratory LP check (EVIDENCE, floating-point, this audit).**
* `scripts/o70_nc_lp.py` → `data/o70/nc_lp.txt`.
* For identical marginals `1/q`, q ∈ {2,3,5,8,16}, and k ∈ {1,2,3,4,6}, the exact
  exchangeable optimum `n_c` (symmetrisation makes exchangeable laws WLOG) lies within
  +3 of BGP's lower bound (14). Lemma 1.1's sufficient n is ≈ 2.2–2.9× larger.
* So the truth is ≈ `kq/2`. Lemma 1.1 is sharp up to a factor ≈2 in the dense regime,
  which is all the barrier needs.
* BGP's `k/(1−p)·log` upper bound is off by a log factor.

**What is genuinely new (apparently).**
1. **Lemma 1.1 as a theorem about k-wise independent laws.** It is an explicit planting
   construction with **arbitrary marginals** and a **linear** threshold `R ≳ 2k+1`. In
   the identical case it gives `n_c(k,p) = Θ(k/(1−p))` for all `p ∈ [1/2,1)`, which
   closes the `log(1/(1−p))` gap left by BGP Thm 27 and drops the prime-power
   restriction.
   * *Confidence: medium–low.* BGP's paper (2012) may have follow-ups that closed this
     gap, and the auditor has no citation index. Moment-problem experts would probably
     consider the exchangeable case routine.
   * The current hedge ("no novelty is claimed") is **too modest** with respect to BGP
     Thm 27 and should be replaced by an explicit comparison (see the agent report).
   * This is a side remark for the TCS literature. It does not bear on ES.
2. **Thm 1.3 (level barrier for dense big-junta minorants) and its ES consequence.**
   Ingredients are Bazzi-type duality plus planting. The result is new as an ES/sieve
   statement (*high*). Its *method* is the standard LP-duality route (BGP Prop 4; Tao
   254A Thm 5).

**Not new.** The LP/sandwich duality, the Bonferroni sufficiency side and the moment-problem
framing.
