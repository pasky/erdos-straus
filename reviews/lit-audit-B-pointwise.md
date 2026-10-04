# Literature-priority audit: pointwise Ω and formal genericity

**Scope/status (2026-10-04).** Pure literature audit; this is not a verification of the campaign proofs. Local archived items were read via `pdftotext -layout`; the Jina web-search endpoint returned HTTP 402 for three searches, and no browser/search replacement was available in this pass. Thus claims below are based on the stated primary-source PDFs/texts and the campaign ledger; I cannot certify a comprehensive Google Scholar/MO/forum/Tao-blog search. In particular, I did not obtain Schinzel's 2000 paper, Yamamoto 1965, Graham–Ringrose, Montgomery, Pomerance 1980, or the requested Tao comments. Citations to them below are secondary or campaign-provided unless stated otherwise.

## Primary-source findings

### Elsholtz–Tao and the odd-square obstruction

Elsholtz–Tao, *Counting the number of solutions to the Erdős–Straus equation*, arXiv:1107.1010v6 (published J. Number Theory 148 (2015), 523–532), Proposition 1.6, p. 6 of the arXiv PDF: for every odd perfect square `n`, `f_I(n)=f_II(n)=0`. Their text says this “essentially dates back to Schinzel … and Yamamoto”; it explains that when proving `f_I(p)` or `f_II(p)` nonzero one needs methods which fail after replacing p by an odd square, “which already rules out many strategies (e.g. a finite set of covering congruence strategies, or the circle method).” This is a method-specific warning, not a theorem about all algorithms or every bounded witness-producing procedure. Theorem 1.8 on p. 7 gives lower bounds for *numbers of representations* for infinitely many n; it is not a lower bound on the least denominator/least parameter.

The stronger campaign Theorem C is not literally in ET: ET's proposition concerns the two specified Type I/II counting functions, whereas POINTWISE_SIZE formalizes finite computation traces, incorporates factorizations/divisor lists and eventual-sign/floor behavior, and states an H-conditional infinite-prime conclusion for correct witness-outputting procedures. Priority should be phrased as a formal generalization/axiomatization of ET's stated warning, contingent on the new transfer argument—not as an established literature theorem.

### Bright–Loughran

Bright–Loughran, *A Brauer–Manin obstruction for the Erdős–Straus surface*, arXiv:1908.02526, Corollary 1.3, p. 3: for odd prime n=p and a natural solution, some pair has `u_i/u_j ∈ Z_p^*` and `(-u_i/u_j / p)=-1`; they describe this as unifying Yamamoto's quadratic reciprocity conditions. Corollary 1.4 on the same page recovers ET Prop. 1.6's stated odd-square restrictions on particular valuation patterns. This is geometric/solution-structure obstruction, not a least-search-depth Ω bound and not a procedure meta-theorem. Nothing in the inspected opening theorem statements yields campaign (2a)/(2b)'s bounds on `W(p)`.

### Salez modular filters

Salez, *The Erdős–Straus conjecture: modular filters*, arXiv:1406.6307 (2014), §3.1 (PDF pp. 7–8): defines `Ω_a`, the induced sets `S_m`, and says `S_m` acts as a filter modulo m; §3.2 defines shortened filters. The later sections use filters in finite computational verification. The PDF does **not**, in the inspected statements, prove a lower bound/Ω-result for the least filter modulus, least depth, or least solution parameter. Thus it is a construction/algorithmic precedent, not a pointwise least-witness lower-bound precedent. The generalized “Schinzel theorem” quoted in Salez, Proposition 2, says if `4/(at+b)` is 3-Egyptian and `(a,b)=1`, then b is a quadratic nonresidue modulo a. This is a QR obstruction, not a bound on the least k.

### Dahan, search-depth paper

Dahan, arXiv:2608.24035v1, *Sieve dimension and search depth for the Erdős–Straus conjecture* (version archived here):

* Proposition 3.8, PDF pp. 10–11 (printed pages 10–11): an explicitly described residual family `H` of primes `n≡1 mod 24` lies outside the algorithm's hyperbolic witness family at **every** depth; it gives 14 such primes up to `5·10^9`, not an asymptotic lower bound on required depth. Increasing the depth cannot resolve those primes because this algorithm searches the wrong subfamily (text immediately following Prop. 3.8).
* Theorem 4.3, printed p. 17: for a fixed finite set P of coprime pairs, the exceptional set has `≪_P N(log N)^{-1-|P|/2}`. This is a fixed-depth sieve-density estimate, not a least-depth Ω bound.
* Theorem 4.14, printed p. 22 (PDF page follows theorem heading): produces `≍ N(log N)^{-3/2}` primes blind to both branches at shift c=7, via a quadratic-form representation. Again, a fixed shift/branch blind set, not growth of the least solution parameter.
* The abstract/introduction (PDF pp. 1–2) reports Schinzel-generalization threshold `n_m ≥ exp(m^{1/3+o(1)})` if it exists; the cited source is Pomerance–Weingartner, not a new Dahan bound. Dahan's search-depth tradeoff results (Theorems 4.17 onward) are upper bounds on exceptional-set size at a specified depth, not lower bounds on the first successful depth. Its explicit residual H gives a finite-depth-independent blind spot for one algorithm, rather than a pointwise Ω theorem for a canonical least solution parameter.

### Pomerance–Weingartner

Pomerance–Weingartner, *Exceptions to the Erdős–Straus–Schinzel conjecture*, arXiv:2511.16817v2 (2025), Theorem 1.1, p. 2: for every ε>0 and sufficiently large m, some n>`exp(m^{1/3−ε})` has `m/n` not representable as three unit fractions. The proof additionally establishes many prime n near that scale are exceptions (stated immediately after Theorem 1.1; detailed theorem in §4). This concerns a **varying numerator m** in the Schinzel generalization and existence/nonexistence of representations—not the least solution denominator for `4/p`, and not `W(p)`. It is a close methodological analogue in the sense that a parameter is varied and exceptional inputs are constructed, but it is not an antecedent Ω-bound for campaign (2a)/(2b). Do not identify it with `n_m`, the least threshold after which every n works: it gives a lower obstruction on any such threshold, if it exists.

### Schinzel 2000 / Yamamoto

ET's bibliography (arXiv p. 32, reference [68]) identifies A. Schinzel, “On sums of three unit fractions with polynomial denominators,” *Functiones et Approximatio* 28 (2000), 187–194. ET p. 6 says its odd-square observation “essentially dates back” to Schinzel and Yamamoto; ET's own Prop. 1.6 provides an exact, checkable statement. The paper itself and Yamamoto 1965 were not accessible in this search, so I cannot responsibly give Schinzel's exact theorem or Yamamoto lemma/page beyond the secondary descriptions. Salez Prop. 2 gives the polynomial-linear QR theorem above, but it should not be represented as a verified quotation of Schinzel 2000.

## Campaign claims: nearest prior work and priority assessment

### (2a) Fixed powers Ω for W(p)

**Prior closest statements:** ET Prop. 1.6 (odd-square vanishing for two representation counts; method limitation), plus the campaign's cited Chang smooth-modulus least-prime theorem for the earlier `limsup W(p)/log p ≥ 5/8` bound (DISCOVERIES (H)6). None of the primary PDFs inspected gives a lower bound for the campaign's least multiplier witness modulus W. PW's Theorem 1.1 has different numerator/exception quantifiers. Dahan gives depth-specific exceptional counts, not this pointwise Ω bound.

**New relative to these sources:** the CRT avoidance of all forced classes through T and Linnik-range PNT/AP transfer for primes, with the stated fixed-k (then every A in O3) growth, is a genuinely different pointwise parameter bound as far as these inspected sources establish. It is not a lower bound on the least denominator in a particular ES solution; W is specifically the campaign's forced-class witness modulus. The distinction must remain explicit.

**Attribution accuracy:** DISCOVERIES (H)13 attributes fixed k to O3 and (H)14 to O4, modulo Thorner–Zaman (and ET Prop. 1.4 for the sharper rate). That is internally consistent with the primary literature inspected. Its attribution of earlier 5/8 to Chang (H)6 is not independently audited here. Avoid suggesting Schinzel/ET/PW already proved Ω(W).

### (2b) Iterated-log rate

**Prior closest statements:** O3 fixed-k bound (campaign's own earlier result), Chang's smooth-modulus 5/8 bound and the classic least-prime/least-nonresidue CRT-transfer architecture. PW/Dahan do not supply this W bound. No independent external source found for the exact rate.

**New:** explicit dependence of the multilevel sieve bookkeeping on k, choosing k to grow, yields `log W(p) ≥ (1+o(1)) log₂p·log₃p/log₄p` i.o. with ET Prop. 1.4 and Thorner–Zaman, and a weaker iterated-log rate without ET Prop. 1.4. This is an explicit strengthening of O3's fixed-k statement, not a direct extension of any bound in the audited prior PDFs.

**Attribution accuracy:** DISCOVERIES (H)14 correctly identifies the immediate antecedent as O3 Thm 5.1/5.2 and calls O4's work explicit-constant bookkeeping plus growing k. The bibliography's use of ET Prop. 1.4 is for the total-mass estimate, not a prior least-witness result. Conditional dependencies should accompany the headline every time.

### (2c) Type-I slice and least QNR

**Prior closest statement:** least quadratic nonresidue Ω-results (campaign cites Graham–Ringrose and Lau–Wu; `ck_min` is a campaign Type-I parameter). The mathematical mechanism is the closest analogue: construct a modulus/progression whose small prime factors are quadratic residues, then transfer to primes. The inspected Salez/Bright–Loughran/ET papers establish QR obstructions but no least-QNR Ω bound for the Type-I parameter. Chang's smooth-modulus least-prime result is another CRT-transfer analogue, not the same statistic.

**New:** `ck_min(p) ≫ log p·log₃p` i.o. via Lau–Wu's least-QNR Ω input and the campaign's exact reduction of congruence certification to the least QNR `n_p`. It is not a new least-QNR theorem. The exact “congruence methods certify exactly n_p” is a campaign equivalence, not an attribution to prior QR literature.

**Attribution accuracy:** DISCOVERIES (H)9 and H6 distinguish the new reduction from the cited least-QNR input, appropriately. It should explicitly state that the lower bound inherits Lau–Wu's ineffectivity/status and is not itself a better least-QNR result. The checked Lau–Wu archive is listed below.

### (3) Theorem M and Theorem C

**Prior closest statements:** ET Prop. 1.6 and its remark (precise odd-square failure of Type I/II counting methods; examples finite congruence coverings and circle method); Schinzel/Yamamoto as historical antecedents per ET; Bright–Loughran Cor. 1.4 (valuation-pattern restrictions on odd squares); Dahan Prop. 3.8 (an algorithm-specific blind subfamily at all search depths); Pomerance–Weingartner concerns exceptional `m/n`, not algorithms. None of these inspected works states a universal transfer theorem for arbitrary bounded deterministic factorization/divisor-list procedures, nor the H-conditional conclusion for every correct bounded witness producer.

**New:** Theorem M formalizes stabilization of a finite execution trace at a profinite polynomial point (including floors, signs, factorization/divisor lists), while Theorem C combines this with a correctness/odd-square obstruction and Hypothesis H to obtain infinitely many prime inputs on which the program cannot output a correct witness. That is materially broader than ET's specific `f_I,f_II` vanishing proposition. It is also conditional: the universal conclusion over actual primes depends on Hypothesis H for the explicit finite family; finite formal transfer alone is not an unconditional theorem that infinitely many primes exist.

**Attribution accuracy:** DISCOVERIES (G)7 and (H)1–4 mostly represent this distinction accurately: G7 calls the earlier antecedent informal and says novelty unchecked; H3 labels Theorem C conditional, and H1 separates proved transfer from conditional existence. The statement “instances … Elsholtz–Tao remark” is defensible only in the qualified, precise-form sense claimed in POINTWISE_SIZE, not as equivalence or priority. Do not conflate Theorem F (a specific certificate) with generic Theorem C. Bright–Loughran/Dahan are structural or algorithm-specific analogues, not the same meta-theorem.

## Requested nearby literature / analogues

* **Salez filters:** no least-depth Ω theorem located in the archived paper; fixed finite filters and computation only (see above).
* **Least prime in AP / CRT:** classic analogue is construction of a modulus with prescribed small-prime behavior followed by a least-prime-in-progression theorem. Campaign cites Pomerance (1980), Granville–Pomerance, and Chang 2014. These are methodological analogues, not ES-specific least-solution claims. I could not verify exact statements/pages for Pomerance (1980) or Granville–Pomerance in this pass.
* **Least QNR:** Graham–Ringrose (1990) and Lau–Wu are the relevant cited Ω inputs for (2c). Montgomery's GRH estimate is not an unconditional lower-bound analogue; GRH gives upper control for least nonresidues. Exact citations were not independently checked beyond the locally archived Lau–Wu PDF.
* **Jacobsthal function:** Rankin, Maier–Pomerance, and Ford–Green–Konyagin–Maynard–Tao are relevant CRT-gap/least-avoider analogues, but not bounds on ES denominators or W. Exact theorem comparisons need separate review.
* **Post-2020 Brauer–Manin / Hypothesis H searches:** Bright–Loughran's arXiv:1908.02526 is pre-2020 and was examined. Search endpoint unavailable; no claim that this is an exhaustive post-2020 literature census. No verified Colliot-Thélène–Sansuc–Swinnerton-Dyer / Harpaz / Poonen theorem matching this finite-program transfer was found in the supplied local archive. Any broad “first meta-theorem” claim therefore needs a dedicated database search and, likely, expert review.

## Archived materials relied on

Date for copies/verification: **2026-10-04**. SHA-256 values are for the exact files under `sources/lit2026/`. URL is source location (files were copied from the worktree's existing archive, not newly downloaded in this audit).

| Archived file | URL | Fetch/archive date | SHA-256 |
|---|---|---:|---|
| `audit-elsholtz-tao-1107.1010.pdf` / `.txt` | https://arxiv.org/pdf/1107.1010 | 2026-10-04 | PDF `b2f22be400ed6443569f4f79f40f9d9424f8aafee8548646cb11a6ed488ae604`; TXT `f02364084bda16e9743609d8b21d08cb8635873edfac22aa65969b090c57eba` |
| `audit-bright-loughran-1908.02526.pdf` / `.txt` | https://arxiv.org/pdf/1908.02526 | 2026-10-04 | PDF `09683c9a381a88730f906630b671e654c6ccc8622e1f2b3d1b19997ce7741d8e`; TXT `425eb3403ebf3c333addaa3f95379d953bd0d330f9262f151ed8fac4106d3508` |
| `audit-dahan-2608.24035v1.pdf` / `.txt` | https://arxiv.org/pdf/2608.24035v1 | 2026-10-04 | PDF `5a5c4bc89ee9949888ee869b7e1bfbec40d1578d9ea89bb884d549867d55a493`; TXT `8ae7f9ea09774953cfeba8b5a7583470bd506148cbdf5e35314ddd59feecc1af` |
| `audit-pomerance-weingartner-2511.16817v2.pdf` / `.txt` | https://arxiv.org/pdf/2511.16817v2 | 2026-10-04 | PDF `87b34b8d24ca4f26f5c80ba8d1d7a335570f76a449df741d5995ee664273128f`; TXT `abb051c766bea02d47fa8bbc32a6d8bb03ea103e3e0b4c5e2d51bb5ba311ea5a` |
| `audit-salez-arxiv-1406.6307.pdf` / `.txt` | https://arxiv.org/pdf/1406.6307 | 2026-10-04 | PDF `3e9481453eab710435642568652826e6c73f39e3bad4776f0cef7f0db90e0cb3`; TXT `b8a69fc8d976373c5b7b9499e571a655f773c24720341a3bee504284013b1142` |
| `audit-lau-wu-least-quadratic-nonresidue.pdf` / `.txt` | https://hkumath.hku.hk/~yklau/p/34.pdf (Y.-K. Lau, J. Wu, author PDF; source provenance in existing archive) | 2026-10-04 | PDF `4b17e69d2f1a2773b66b1645b8b59cb5a628333b17d1b2c751b8ba1e75accab4`; TXT `48a2bc4314ebc3ae92ff64af4afd332701bb1e5565241f19f88fac91ebb4c7e3` |
| `audit-chang-short-character-sums-composite-moduli.txt` | https://math.ucr.edu/~mcc/paper/Char060113.pdf (Mei-Chu Chang, author-hosted text) | 2026-10-04 | `5637e227edd9607fcc519e612758ee3a5b9a32716015aacce0a7e3889842438f` |

**Caveat:** Campaign-discussed Dahan/PW versions in the pre-existing source archive are `sources/dahan-2608.24035v1.pdf` and `sources/pomerance-weingartner-2511.16817v2.pdf`; this note archives audit-prefixed copies. No edit was made to `sources/lit2026/README.md`.

**Archive note (parent, 2026-10-04).** The `audit-*` PDF copies that were byte-identical to files already archived (ET, PW, Dahan, Bright–Loughran, Salez, Elsholtz–Planitzer, Lau–Wu; plus the Lau–Wu/Chang `.txt` and the Vaughan access log) were removed. The originals are at `sources/elsholtz-tao-1107.1010.pdf`, `sources/pomerance-weingartner-2511.16817/…v2.pdf`, `sources/dahan-2608.24035v1.pdf`, `sources/bright-loughran-1908.02526.pdf`, `sources/lit2026/arxiv-1406.6307.pdf`, `sources/lit2026/arxiv-1805.02945-elsholtz-planitzer.pdf`, `sources/lit2026/lau-wu-least-quadratic-nonresidue.{pdf,txt}`, `sources/lit2026/chang-short-character-sums-composite-moduli.txt` and `sources/vaughan-1970-access-log.md` (same SHA-256). The `audit-*.txt` extractions are kept.
