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
