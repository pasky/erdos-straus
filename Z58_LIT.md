# Z58_LIT — 2024–2026 literature, verified, read against (MS) and the z58 falsifiers (wave z58, lane LIT)

**Verdict: narrowed — no HOT LEAD.** The lane found one **important external item**: Kandukoori–Ramesh–Kumar prove
E(N) ≪ N exp(−c(log N)^{3/4}). It is public since 2026-07-30 and has an axiom-free Lean proof (CI green 2026-10-30). It
**pre-dates the campaign's internal 3/4 note (2026-09-06)**, which says "We are not aware of an earlier improvement" (§2.1).
Two items are new to the repo: Ventas arXiv:2610.41027 and Akaka v0.8. Pomerance–Weingartner is now published. The lane also
proves a (★) analogue of Ventas's modular-inversion symmetry (Prop I, §2.3). No literature mechanism found passes all four
falsifiers.

ES is OPEN; nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Literature statements are quoted from the opened source, with theorem number, unless marked "abstract only".
Proofs of cited papers were **not** re-checked, and preprints are unrefereed unless a journal is named. All sources were
accessed 2026-11-05.

Files:
* source notes from the three research subagents: `data/z58/lit/q1_es_2024_2026.md` (ES 2024–26 audit),
  `q2_single_integer.md` (pointwise divisor/prime results), `q3_hasse_squares.md` (integral HP and square obstructions);
* archived PDFs with SHA-256: `data/z58/lit/sources/` (README there);
* repo arXiv-id snapshot: `data/z58/lit/repo_arxiv_ids.txt` (1685 ids);
* scripts: `scripts/z58_lit_inversion.py` (Prop I check), `scripts/z58_lit_negpell_f3.py` (F3 probe, output
  `data/z58/lit/negpell_f3.txt`).

Prior sweeps that this lane does **not** repeat (all git-grepped first): `LITERATURE_2026.md`, `LITERATURE_2026_UPDATE.md`,
`Z53_LIT.md` (to 2026-11-01), `Z56_K4LIT.md`, `LITERATURE_AUTOMORPHIC.md`, `BRAINSTORM/z52_lit_*.md`. Every item the subagents
returned under brief (b)/(c) was already cited in the repo, except those listed in §2.

---

## 0. MANDATORY FALSIFIER TABLE (literature mechanisms; Assessment unless labelled)

Screens (`data/z58/screens/`):
* **F1** R(m²) = 0 for every odd m.
* **F2** the C-even sub-line R₈ has 12 prime zeros in [10¹⁰, 1.1·10¹⁰], 4 of them in 𝔐.
* **F3** 285 non-square composite zeros n ≡ 1 (4), n ≤ 7 999 801.
* **F4** 14 (★)-zero primes (the last is 8 813 281; 9 are in 𝔐) and 38 𝔊*-zeros (the last is 564 661 441).

**F3 screen data (CERTIFIED counts from the screen file).**
* Per half-decade [10^k, 10^{k+1/2}) the composite-zero counts are 12, 12, 25, 35, 45, 50, 62 for k = 3, 3.5, …, 6, and 35
  in the partial bin [10^{6.5}, 8·10⁶].
* 71 of the 285 are ≡ 1 (mod 24).
* **15 lie in 𝔐**: 1969 = 11·179, 2641 = 19·139, 5161 = 13·397, 18001, 23881, 90889, 112849, 199369, 345361, 349609, 510169,
  539281, 897961, 2956321 = 211·14011, 3210601 = 19·37·4567.

*Readings of the F3 data (EVIDENCE):*
* The composite zeros show no sign of thinning in absolute numbers (the per-half-decade counts rise up to 10^{6.5}).
* Restricting to 𝔐 leaves composite zeros too.
* A mechanism of the form "every non-square n except a finite sporadic set" would therefore give a statement that the
  composite data contradict, unless it uses primality.
* Probe (`negpell_f3.txt`):
  * A prime factor ≡ 3 (mod 4) occurs in 91 % of the composite zeros, against 77 % of 20 000 random non-square
    composites ≡ 1 (4) in [10⁵, 8·10⁶].
  * Restricted to n whose prime factors are all ≡ 1 (mod 4), negative Pell is solvable at 20/26 = 0.77 of the zeros
    (12/17 = 0.71 above 10⁵), against 0.67 of the controls.
  * So composite zeros are mildly enriched in prime factors ≡ 3 (4).
  * They are **not** enriched in negative-Pell (2-class-group) failure.
  * The control is not size-matched, so this is a weak signal only.

| mechanism (literature) | what it proves | F1 odd squares | F2 C-even line | F3 composites | F4 known zeros |
|---|---|---|---|---|---|
| Divisors in classes or intervals (Erdős–Hall, Tenenbaum, Ford, Ford–Green–Koukoulopoulos (FGK), Koukoulopoulos–Tao) | almost-all n or mean values; pointwise only **upper** bounds (Lenstra 1984 Thm; Coppersmith–Howgrave-Graham–Nagaraj (CHN) via Hales 2410.05030 Thm 4.2) | invisible (squares have density 0) | invisible | invisible (exceptional sets allowed) | allowed |
| Exceptional-set sieves: Vaughan 1970; **Kandukoori–Ramesh–Kumar 2026 (3/4)**; Akaka v0.8 ((log X)³ at almost all primes) | all n except a set of density → 0; Janson/Spencer no-hit bound for one forced-class family | invisible | consistent: Akaka v0.8 concerns *all* Type II solutions of m/p (m = 8 included), allowing ≤ C·m·X/(log X)⁴ bad primes per block. R₈ is only the c = 1 line of 8/p, so an R₈-zero need not be a bad prime there | invisible | consistent; no pointwise content |
| Least prime in AP, explicit (Bennett–Martin–O'Bryant–Rechnitzer (BMOR) 1802.00085 Thms 1.1/1.5; Xylouris) | pointwise and explicit; produces a *free* prime in a class | not engaged | not engaged | not engaged | not engaged: supplies no divisor of p + u |
| Least (prime) quadratic non-residue: Burgess, GRH (Lamzouri–Li–Soundararajan (LLS) Cor 1.1), Pollack (JNT 187 (2018) abstract; 1508.05035 Thm 1.1) | pointwise | **native**: a non-residue exists iff n is not a square | blind | **fails**: every non-square composite also has one | gives only a *necessary* condition (every witness d has a prime ℓ \| d with (p/ℓ) = −1) |
| Brauer–Manin on ES surfaces (Bright–Loughran (BL) Thms 1.1–1.9; Yamamoto; EST Prop 1.6) | obstruction side; no BM obstruction to existence for n ≥ 2 | **explains** T1 (reciprocity) | not addressed by BL (open question for STRUCT: is there BM data on the C-even sub-family?) | at the 285 composites: open. If BM does not obstruct there, "BM is the only obstruction" fails for the (★) surface (STRUCT lane) | same as F3 |
| Integral HP failures on cubic / Markoff-type log K3 (Lyczak–Mitankin–Uppal (LMU) 2311.10008 Thm 1.4; Dao 2504.10992 Thm 5.2; Ghosh–Sarnak; Loughran–Mitankin) | failure families (Dao: square parameters k = ℓ²); "almost all" positivity results | Dao Thm 5.2 is an *analogue* of T1 (square parameter, BM obstruction) | none | none of these gives existence for prime parameters | none |
| Thin-orbit reciprocity local–global (Rickards–Stange Thm 2.8; HKRS; Alkauskas) | squares plus a finite sporadic set (RS fat case PROVED) | **native** | blind | **fails** (F3 data above) | wrong shape: 14 + 285 zeros, apparently unbounded |
| Legendre descent: x² − py² = −1 for every prime p ≡ 1 (4) (§2.6) | pointwise, rigid, every p | native (impossible at squares) | n/a | **uses primality** at the split (x−1)(x+1) = py²; fails for every n with a prime factor ≡ 3 (4) and for a positive proportion of the rest (Koymans–Pagano) | **fails**: no threshold, so a verbatim port would "prove" R(p) ≥ 1 at 8 813 281 |
| Modular inversion (Ventas 2610.41027 Thm 3.1; (★) analogue Prop I, §2.3) | symmetry of finite hit patterns, not existence | consistent (squares ↦ squares) | **swaps** C-even with u-even, so it does not preserve the R₈ line | symmetric over all units: no primality | the D-cutoff breaks it; nothing pointwise |

**Reading (Assessment).**
* F1 is passed by every T1-native mechanism: characters, reciprocity, Pell.
* F3 rules out all of them except mechanisms that use primality at a rigid step (Legendre type).
* F4 rules out rigid steps that have no size threshold.
* So a literature mechanism surviving all four would have to be **prime-specific AND threshold-bearing**: an analytic count
  with an error term at one prime, or a size squeeze in the style of Chebyshev or Zsigmondy.
* **None was found** (§2.5–2.6), in line with Z53_LIT (J)103.

## 1. Precise questions (brief, sharpened)
* **Q1 (ES 2024–2026).**
  * Every ES / Egyptian-fraction research item from 2024-01-01 to 2026-11-05: what it claims, current version, whether
    refereed.
  * Lean formalisations.
  * Function-field ES.
  * Anything after Cao–Xu 2610.32302 (2026-10-23).
* **Q2 (single-integer existence).** Pointwise results of these kinds:
  * n has a divisor in a class or interval;
  * a shifted prime p + a has a divisor or prime factor in a class;
  * least prime in an AP with explicit constants;
  * integral Hasse principle with an every-parameter conclusion.
* **Q3 (structures obstructed at squares).** Existence at each large n or prime of a structure obstructed at squares. Per
  §0, especially structures that fail at composites and have small exceptions.

## 2. Findings

### 2.1 Kandukoori–Ramesh–Kumar: E(N) ≪ N exp(−c(log N)^{3/4}) — external, Lean-formalised, prior to the campaign's note

**Source.** S. Kandukoori, S. Ramesh, P. Kumar, *An improved bound for the exceptional set of the Erdős–Straus equation*.
* The PDF is dated "July 29, 2026" and was taken from https://sushaan-k.github.io/erdos-straus/paper.pdf. It is archived
  as `data/z58/lit/sources/kandukoori-ramesh-kumar-2026-07-29.pdf` (sha256 20a3290b…).
* No arXiv record was found (`au:Kandukoori` returns only an unrelated paper).
* It is not refereed as far as we know.

**Statements (quoted, PDF p. 1–2).**
* "Theorem 1 (main theorem). There is an absolute constant c > 0 such that, for all N ≥ 3, E(N) ≪ N exp{−c(log N)^{3/4}}."
* "The same saving holds relative to the primes: the number of exceptional primes up to N is ≪ π(N) exp{−c(log N)^{3/4}}
  after decreasing c."
* "Theorem 2 … For each fixed integer m ≥ 4, there are constants c_m, C_m > 0 such that, for all N ≥ 3,
  E_m(N) ≤ C_m N exp{−c_m(log N)^{3/4}}."
* Remark 1.2: "For a family of congruences with total weight µ ≍ (log X)^k … choosing log X of order (log N)^{1/(k+1)} gives
  a saving exp{−c(log N)^{k/(k+1)}}. The family with prime moduli used in the Vaughan method has quadratic mass … Here the
  cubic mass gives 3/4."

**Method (paper §§2–5).**
* Type II congruences 4a − 1 | n + 4h with h | a², a family of cubic logarithmic mass (Prop 4.2).
* A Janson/Spencer conditioning no-hit bound (Thm 5.2: P(W_b = 0) ≤ exp{−(1 − o(1))µ_b}).
* A finite counting estimate (Thm 5.4) and a lifting lemma (Lemma 5.5).
* We checked Example 1.1, 4/2521 = 1/644 + 1/30252 + 1/1217643 (exact arithmetic).

**Formal status (verified via the GitHub API).**
* At repository HEAD `f6c99eaa` (2026-10-30), the README says: "Everything is proved from Mathlib, including the
  Bombieri–Vinogradov theorem. The only axioms used are Lean's propext, Classical.choice and Quot.sound."
* The CI workflow `ci` runs `lake build` and then asserts that 5 `#print axioms` outputs equal exactly
  [propext, Classical.choice, Quot.sound]. Its run on f6c99eaa concluded **success**.
* We read the definitions in the Lean files. `saving c N = exp(−c (log N)^{3/4})` (Basic.lean l. 249–251).
  `IsMainBound f := ∃ c > 0, ∃ C > 0, ∀ N ≥ 3, f N ≤ C·N·saving c N`. `esExceptional n := ¬∃ x y z > 0, 4/n = 1/x+1/y+1/z`
  (Congruences/Certificates.lean l. 17–25).
* So the statement is faithful as read. **We did not build the project.** The build needs a Mathlib cache that exceeds this
  lane's memory budget.
* The first public commit, `268ebdbf` (2026-07-30), already defines the same 3/4 saving (EscAnalytic/Counting.lean l. 44).
  At that time it rested on nine named analytic axioms, the version that `LITERATURE_2026_UPDATE.md` §1 recorded on
  2026-10-21.

**Consequences for the campaign (Assessment).**
1. **Priority.** The campaign's `paper/es-threequarter-note.tex` was first committed 2026-09-06; it is internal and not
   posted. Its abstract says "We are not aware of an earlier improvement of the exponent 2/3". FRONTIER §2 (l. 61) lists the
   bound as "INTERNALLY PROVED". The K-R-K claim was public on 2026-07-30 and is now formalised without extra axioms.
   * The note's abstract must be corrected.
   * FRONTIER/STATUS must cite K-R-K as the first public (and machine-checked) 3/4 result.
   * `LITERATURE_2026_UPDATE.md` §1 ("neither … nor a new bound shown to surpass Vaughan") is now outdated.
2. **Independent confirmation.** The campaign's note uses the same architecture: classical Type II classes, cubic mass
   ≍ (log X)³, conditioning, then counting on [1, N]. A Lean proof of the same exponent strongly corroborates the internal
   result. The campaign's sharpness theorem (3/4 is the limit of CRT/coefficient-sum sieves, `EXCEPTIONAL_KARY3.md`) agrees
   with K-R-K Remark 1.2.
3. **Possibly still campaign-new** (Assessment; needs a careful comparison by the paper owner):
   * interval and progression versions, E(I) ≪ H exp(−c(log H)^{3/4}) ((D)30);
   * uniformity in m, E_m ≪ H exp(−c(log H)^{3/4}m^{−1/4}) ((D)31).
   * K-R-K Theorem 2 is for fixed m, with constants depending on m. The paper's only uniform statement is the quoted
     Pomerance–Weingartner bound.
4. **(MS) relevance: none.** The result is a density statement (B6); F1–F4 are not engaged (§0 row 2).

### 2.2 Akaka Zenodo v0.8 (new version; the repo knows v0.7)
* Zenodo API record 22905042 (concept 22556476) is v0.8, published 2026-09-22, titled "Uniform cubic lower bounds for strict
  three-unit-fraction representations at primes".
* Description (quoted): "There exist absolute constants c,C,X0 > 0 such that, for every real X >= X0 and each integer
  4 <= m <= (log X)^3, at most C m X/(log X)^4 primes p in (X,2X] have R_II,m(p) < c(log X)^3/m."
* It claims a "completed additive Lean certificate" (Lean 4.32.0; "credited FormalPantheon for the pinned
  Bombieri-Vinogradov development").
* It states: "This does not prove the universal Erdos-Straus or Schinzel conjecture … Independent human specialist review …
  remain[s] outstanding."
* Assessment: an almost-all statement with no pointwise content. It does not conflict with F2. It counts all Type II
  solutions of 8/p; R₈ is only their c = 1 line, so an R₈-zero need not be an exceptional prime for it. Even if it were,
  12 primes are far below the allowed ≈ X/(log X)⁴.

### 2.3 Ventas arXiv:2610.41027v1 (2026-10-29), and its (★) analogue (PROVED, elementary)
**Source.** "Erdős–Straus Conjecture: Modular Inversion in Mordell Classes", 8 pp., no journal reference, archived.
* Grid indicator (eq. (1)): for n ≡ 1 (4) and m = 4t, with r := (−n mod m), G_t(n) = 1 iff 1 < r < m and r | m + 1.
  * This yields the certificate 4/n = 1/(ti) + 1/(tik) + 1/(ntk), with only one denominator divisible by n.
  * So it is a **Type I** family, whereas (★) is Type II.
* Thm 3.1: G_t(u) = G_t(ι_T(u)) for 1 ≤ t ≤ T, where ι_T is inversion mod M_T = lcm(840, 4, …, 4T).
* (6): on 𝔐, inversion gives 1 ↔ 1, 169 ↔ 169, 121 ↔ 361, 289 ↔ 529 (four orbits).
* Prop 4.1: the inverse b_p of a Mordell prime at cutoff T_p = (p−1)/2 is never a square. The proof uses a QNR ≤ (p−1)/2
  and reciprocity, so it is T1-native.
* Thm 6.1: for fixed cutoff, paired classes have equal limiting prime-pattern frequencies (PNT in APs).
* The paper says: "The identities do not establish universal Grid coverage."

**Prop I (PROVED here, elementary; checked by `scripts/z58_lit_inversion.py` for all d ≤ 20 000, 0 violations).**
* Setup. For d ≡ 3 (mod 4) let H_d = {−r mod d : 1 ≤ r < d, r | (d+1)/4} be the (★) hit set (Z57_SYNTH Lemma A.1).
* Claim: x ∈ H_d ⟺ (4x)^{−1} mod d ∈ H_d.
* Under this map the hit (u, C) = (r, (d+1)/(4r)) goes to (C, u).
* *Proof.*
  * gcd(r, d) = 1 because r | (d+1)/4.
  * If x ≡ −r, put r′ = (d+1)/(4r). Then r′ | (d+1)/4 and 1 ≤ r′ ≤ (d+1)/4 < d.
  * From 4rr′ = d + 1 ≡ 1 (mod d) we get (4x)^{−1} ≡ (−4r)^{−1} ≡ −r′.
  * The map x ↦ (4x)^{−1} is an involution, so the converse follows. ∎
* *Corollary (PROVED).* Fix D, let L_D = lcm{d ≤ D odd}, and let n be prime to L_D. Then n and any n* with
  n* ≡ (4n)^{−1} (mod L_D) have the same set of hit levels d ≤ D. At each level the hit's (u, C) is swapped.
* On 𝔐, the odd part 105 pairs the classes as {1, 289}, {121, 169}, {361, 529}. These are three 2-orbits. They differ from
  Ventas's Grid orbits (computed in the script).
* By Dirichlet's theorem in APs mod lcm(840, L_D), primes in paired classes have equal limiting frequencies of every
  hit-pattern on d ≤ D. This is the analogue of Ventas Thm 6.1 (PROVED relative to PNT in APs).
* *F-readings.*
  * F1: squares map to squares, (4m²)^{−1} = ((2m)^{−1})², which is consistent with T1.
  * F2: the map exchanges the C-even sub-line with the u-even sub-line, so R₈ is not invariant.
  * F3/F4: the symmetry holds on all units, so it uses no primality. The cutoff d ≤ (4p+1)/3 breaks it, since n* is huge.
  * Assessment: a fixed-D distributional symmetry (B1-level), with no existence content.
* *Data aside.* Zero counts in the paired classes:
  * (★)-zeros: {1: 3, 289: 1}, {121: 0, 169: 0}, {361: 3, 529: 2};
  * 𝔊*-zeros: {1: 6, 289: 2}, {121: 0, 169: 2}, {361: 7, 529: 3}.
  * These counts are too small to read anything from, but they are offered to the MORDELL lane.

### 2.4 Status changes (verified)
* **Pomerance–Weingartner** arXiv:2511.16817 is published: *The Ramanujan Journal* 69 (2026), no. 2, article 31,
  DOI 10.1007/s11139-025-01312-2, online 2026-01-14. This is from the Crossref API record (title "Exceptions to the
  Erdős–Straus–Schinzel conjecture"). The arXiv record carries no journal reference.
* Unchanged (arXiv API, 2026-11-05):
  * Mihnea–Dumitru 2509.00128 is still v1 with no journal reference;
  * Cao–Xu 2610.32302 v1; Xu 2605.23601 v2; Ventas 2605.04551 v3; Jiang 2609.09204 v2 (withdrawn);
  * Bradford, *Integers* 25 #A54; Chamberland, *Integers* 26 #A42.
* arXiv `all:Straus` sorted by date shows **no ES preprint after 2610.41027** (2026-10-29).
* erdosproblems.com/242 (opened 2026-11-05, via the visit-webpage skill, which strips formulas):
  * it still lists Vaughan [Va70] as the exceptional-set record and MiDu25 for the 10¹⁸ verification;
  * K-R-K is not mentioned.
* Lean repositories (GitHub API):
  * google-deepmind/formal-conjectures `ErdosProblems/242.lean`: last touched 2026-09-18 (a modularisation chore);
  * carlok/erdos-straus-offset-lean: last commit 2026-09-21 (toolchain bump plus an axiom-audit CI);
  * leochlon/erdstrau: **404**, the repository is gone or private;
  * sushaan-k: §2.1.
* Function-field ES: no 2015–2026 paper found (subagent Q1, bounded search). This agrees with `FUNCTIONFIELD_ES.md`.

### 2.5 Q2: pointwise single-integer existence — answer: none (Assessment, scoped)
Details are in `data/z58/lit/q2_single_integer.md`; every item was already in the repo.
* Lenstra 1984 Thm (p. 331): "at most 11 positive divisors of n that are congruent to r modulo s" when s > n^{1/3}.
* CHN 2008, via Hales arXiv:2410.05030 Thm 4.2: an upper bound for s > n^α, α > 1/4.
* Both are **upper** bounds. Explicit-AP and least-QNR results (BMOR Thm 1.1/1.5; Pollack; LLS Cor 1.1) give free primes or
  character witnesses.
* **No pointwise lower bound for the divisors of one integer in a residue class modulo a modulus growing with the integer
  was found**, whether proved, conditional or claimed. This matches Z53_LIT §5(a).

### 2.6 Q3: existence obstructed at squares — answer: no item of the target shape (Assessment, scoped)
Details are in `data/z58/lit/q3_hasse_squares.md`; every arXiv item was already in the repo.
* Closest square-parameter analogue: Dao, arXiv:2504.10992v2, Thm 5.2. For k = ℓ² in a congruence class, a Markoff-type K3
  integral model has local points but an algebraic BM obstruction. This is failure at squares; it says nothing about
  success at primes.
* **Correction to the subagent report.** The report lists negative Pell for primes as "NOT VERIFIED". It is classical:
  * Chiang–Ciou–Tsai, NNTDM 24(3) (2018) 10–26, Example 4: "It is known that x² − py² = −1 is solvable in integers for p a
    prime congruent to 1 modulo 4". This is a secondary statement.
  * Proof (Legendre's descent, standard): take the least solution of x² − py² = 1. Since p ≡ 1 (4), x is odd and y is even.
    Then (x−1)(x+1) = py² with gcd(x−1, x+1) = 2. *Primality* forces {x−1, x+1} = {2a², 2pb²}. Minimality excludes
    x + 1 = 2a², so a² − pb² = −1.
  * Our check: no failure among primes p ≡ 1 (4) below 2·10⁵ (CF-period parity, `negpell_f3.txt`).
  * It fails at every square and at every n with a prime factor ≡ 3 (4).
  * Among squarefree n with all prime factors ≡ 1 (4), the solvable proportion is 1 − ∏_{j odd}(1 − 2^{−j}) ≈ 58 %
    (Koymans–Pagano arXiv:2201.13424, as quoted in K. Conrad, "Pell's equation II", Remark 3.6).
  * So negative Pell is the cleanest literature instance of "all primes in the class succeed, squares fail, a positive
    proportion of composites fail". It is the exact shape of (MS) **minus F4**: it has no small prime exceptions.
  * Its proof is rigid (a unit plus a factor split), so it cannot model (★), which has 14 prime zeros. The F3 probe (§0)
    found no link between (★)-composite zeros and negative-Pell failure.
* Assessment: no theorem was found of the shape "every sufficiently large prime has a point, infinitely many composites fail,
  squares are obstructed, and finitely many small primes fail".

## 3. Verdict, screens, proposed additions, bottom line

**Verdict: narrowed** (Assessment).
* What the literature offers (§0, §2.5–2.6) splits three ways:
  * T1-native but primality-blind mechanisms (characters, reciprocity, thin orbits), which F3 kills;
  * rigid prime-specific mechanisms (Legendre type), which F4 kills;
  * averaged or exceptional-set mechanisms, to which F1–F4 are invisible.
* No item supplies a pointwise, prime-specific, threshold-bearing existence argument.
* The one substantive new external result (K-R-K) is an exceptional-set theorem. It matters for the campaign's
  **priority and citations**, not for (MS).

**Screens for the best items.**
* K-R-K: F1–F4 not engaged (density statement).
* Prop I: F1 consistent; F2 swaps the sub-lines; F3/F4 no content.

**Proposed `LITERATURE_2026.md` additions** (do not apply here; for the parent):
* *Wave z58 (2026-11-05).*
  * **Kandukoori–Ramesh–Kumar**, "An improved bound for the exceptional set of the Erdős–Straus equation" (dated 2026-07-29;
    sushaan-k.github.io/erdos-straus; Lean github.com/sushaan-k/erdos-straus-lean, axiom-free at f6c99eaa, 2026-10-30, CI
    green).
    * Thm 1: E(N) ≪ N exp(−c(log N)^{3/4}). The same holds for primes, and Thm 2 gives it for fixed m ≥ 4.
    * Method: cubic-mass Type II family plus a Janson/Spencer no-hit bound.
    * Public since 2026-07-30, so it **precedes `paper/es-threequarter-note.tex` (2026-09-06)**. Supersedes
      LITERATURE_2026_UPDATE §1's "no sharper exponent" remark. Unrefereed, no arXiv record.
  * **Akaka v0.8**, Zenodo 22905042 (2026-09-22): a block-uniform version for 4 ≤ m ≤ (log X)³, with a Lean certificate
    claimed. AI-assisted and unrefereed.
  * **Ventas**, arXiv:2610.41027v1 (2026-10-29): modular inversion of Type I Grid patterns in the Mordell classes. Thm 3.1,
    Prop 4.1, Thm 6.1. The (★) analogue is Prop I of Z58_LIT §2.3.
  * **Pomerance–Weingartner**: now *Ramanujan J.* 69 (2026) no. 2, art. 31, DOI 10.1007/s11139-025-01312-2.
  * leochlon/erdstrau: GitHub 404 as of 2026-11-05.
  * Negative Pell: Chiang–Ciou–Tsai NNTDM 24(3) (2018) Ex. 4 (secondary statement of Legendre's theorem). It is a reference
    for the "all primes / not squares / not all composites" shape.

**Proposed FRONTIER text** (do not apply here):
* §2, exceptional set: "E(N) ≪ N exp(−c(log N)^{3/4}) was first made public by Kandukoori–Ramesh–Kumar (2026-07-30,
  Lean-formalised from Mathlib, CI-checked axioms); the campaign's `es-threequarter-note` (2026-09-06) is an independent
  internal proof of the same exponent; its interval/progression and uniform-in-m extensions ((D)30/(D)31) are not in K-R-K
  (Assessment)."
* §4 screening: "Literature mechanisms split into T1-native/primality-blind (killed by F3), rigid prime-specific (killed by
  F4), and averaged (blind to F1–F4); a viable mechanism must be prime-specific and threshold-bearing (Z58_LIT §0)."

**Bottom line.** The 2024–2026 literature, read through the z58 falsifiers, contains no mechanism that could prove (MS):
* those that see squares (characters, reciprocity, thin orbits) cannot tell primes from the 285 composite zeros;
* the classical prime-specific one (Legendre's negative-Pell descent) has no room for the 14 small prime zeros;
* everything else is averaged.

The most important find is administrative but significant. The campaign's "internally proved" 3/4 exceptional-set
exponent was made public two months earlier by Kandukoori–Ramesh–Kumar, and it now has an axiom-free Lean proof. The
campaign's 3/4 note and FRONTIER must cite it.

## 4. Review log
(Hostile citation review: pending.)
