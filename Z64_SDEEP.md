# Z64_SDEEP — conjecture (S) as a character-value problem (wave z64, lane SDEEP)

**ES is OPEN; nothing here proves or disproves ES, (MS), SQ₅ or (S).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Scripts `scripts/z64_sdeep_*`, data
`data/z64/sdeep/`. Brief: `z52bbriefs/z64_lanes.md` §SDEEP (+ z58 common rules, z53 depth brief).

*Status: final draft (checkpoint 1 with kill tests KS0–KS2 committed before any lane computation, commit 7bd1196af).
Verdict: **NARROWED** — no HOT LEAD. Internal hostile review: §9.*

Notation (HJ_DEEP, DEDEKIND_ES = DK, FOREST_*). n ≡ 1 (mod 4); a *word* of n is (t,u,v) ∈ ℤ³_{≥2} with
tuv − u − v = n; A = tu − 1, A* = tv − 1, AA* = tn + 1, n/A = [[v,t,u]]; L₃(n) = {A}; χ_n(x) = (x/n) (Jacobi).
N₋(n), N₊(n) = numbers of words with χ_n(A) = −1, +1. Counts "per pair" are per reversal pair {(t,u,v),(t,v,u)}
(at primes u ≠ v always, DK §6 C3).

## 0. Mandatory falsifier table (final; for (S) and for the three mechanisms tested)

| screen | behaviour | where non-squareness / primality enters |
|---|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1 ⟹ N₋(m²) = 0 (T1, DK Prop 3.1). Lemma 2 below: the sign is the n-free cell function σ, so T1 says "integral points of tuv − u − v = m² lie in the five cells C₊". Every sub-count used in KS1 vanishes at squares; KS0 is about non-squares only. | only in χ_n ≢ 1, i.e. in "the integral points escape C₊" — nowhere else. |
| **F2 C-even / numerator 8** | (S) uses all 15 Jacobi −1 cells (five slices 4 ∣ t,u,v,A,A*), not the (★) line or its C-even half; (S) holds at the 12 R₈-zero primes near 10¹⁰ (Z63_EUCLID §7, CERTIFIED there). KS1 tested every slice and every cell separately (no law). | — |
| **F3 composites** | (S) is conjectured for all non-square n ≡ 1 (4); no counterexample < 10⁹ (HJ_DEEP + R174). KS0 adds 18 957 adversarial n up to 9·10¹³, many composite (d·m², n ≡ 1 mod lcm(1..23), near-squares): 0 failures, min N₋ (pairs) = 65 among the fully enumerated ones. | not needed (Assessment). |
| **F4 known zeros** | (S) holds at the 14 (★)-zero and 38 𝔊*-zero primes (≤ 10⁹ census). The hardest prime ≤ 2·10⁶ for (S) is 21841 (one −1 pair out of 10; also DK's t_min record), p ≡ 1 (mod 840) ∈ 𝔐. | — |

## 1. Precise statements

* **(S) (CONJECTURE; HJ_DEEP §3).** For every non-square n ≡ 1 (mod 4) with L₃(n) ≠ ∅ there is a word with
  χ_n(A) = −1. At primes p ≡ 1 (4), p > 5: (S)(p) ⟹ ES(p) (DK Thm 4.5); L₃(p) ≠ ∅ is automatic (bsG_primes_trivial).
* **Sign dictionary (PROVED, prior work).** χ_n(A) = χ_n(uv) (A ≡ u·v⁻¹ mod n); = (−u/A) = (−t/A) for odd A
  (n ≡ −u mod A and reciprocity); = −1 iff 4 divides one of t,u,v,A,A* (DK Thm 4.5 / §8.1; elementary proofs in
  FOREST_CONNECTIVITY Thm 2.1 and FOREST_DEEP_FABLE Thm A; endpoint form mod 8: FOREST_DEEP_FABLE Thm B).
* **Target of this lane** (brief): Σ_{A∈L₃(n)} (1 − χ_n(A)) > 0 — find structure on L₃(n) that a character can see;
  push to (a) a theorem on an explicit infinite non-congruence family of primes, (b) a threshold under a named
  hypothesis, (c) a counterexample, or (d) a precise missing lemma.
* **What was not closed before this lane** (and is now tested): (i) *non-constant* parity laws whose parity is a
  non-abelian Chebotarev invariant (only constant parities, DK C5 / Z62_PARITY, and statistical Rédei correlations,
  BRAINSTORM/nonab_frobenius_redei, had been tested) — KS1; (ii) (S) beyond 10⁹ in adversarial families — KS0;
  (iii) the trace / Salié form of the sign as a completion device — KS2.

## 2. Theory: what a character can see on L₃(n)

**Lemma 1 (the sign is a function of the trace; PROVED, elementary).** Let n be odd, γ = [[a,b],[c,d]] ∈ Γ₀(n).
If gcd(tr γ + 2, n) = 1 then (d/n) = ((tr γ + 2)/n); if gcd(tr γ − 2, n) = 1 then (d/n) = ((tr γ − 2)/n).
*Proof.* ad ≡ 1 (mod n), so tr γ ± 2 ≡ d + d⁻¹ ± 2 = (d ± 1)²·d⁻¹ (mod n); take Jacobi symbols. ∎
*For words.* γ_w = [[A, t],[n, A*]] ∈ SL₂(ℤ) ∩ Γ₀(n) and tr γ_w + 2 = A + A* + 2 = t(u+v). Hence
**χ_n(A) = (t(u+v)/n) = ((t(u+v) − 4)/n)** whenever these are coprime to n. CERTIFIED on every word (u < v) of every
prime p ≡ 1 (8), p ≤ 2·10⁶ (37 116 primes; `scripts/z64_sdeep_words.c`, 0 failures). *Reading (Assessment):* the
sign of a reversal pair is the quadratic character of n at s + 2 = t(u+v), s = tr γ_w, i.e. the value at n of the
genus-type character attached to the factorisation (s−2)(s+2) of the discriminant s² − 4 of the form
[n, A* − A, −t] (this makes the BRAINSTORM item Z2825 precise; it is a reformulation, not a mechanism).

**Lemma 2 (character blindness; PROVED, from DK §8.1).** For n ≡ 1 (mod 4) the map L₃(n) → {±1}, A ↦ χ_n(A),
factors through the cell map w = (t,u,v) ↦ (t,u,v) mod 4 ∈ (ℤ/4)³, followed by the *n-independent* function
σ: σ(c) = +1 iff c ∈ C₊ := {(1,2,3), (1,3,2), (2,1,2), (2,2,1), (3,1,1)}. Consequently, for every F: L₃(n) → ℂ,
Σ_{A∈L₃(n)} χ_n(A)F(A) = Σ_c σ(c) Σ_{cell(w)=c} F(A_w), and
**(S)(n) ⟺ the integral points of S_n : tuv − u − v = n (letters ≥ 2) are not all contained in the five residue
classes C₊ mod 4.** At n = m² they are (T1). *Proof.* DK Thm 4.5/§8.1 (σ is the stated table), applied termwise. ∎
*Meaning for the brief.* On the structured set L₃(n) the character χ_n carries no information beyond selecting 15 of
the 20 admissible 2-adic cells. The analytic content of χ_n (Burgess on intervals of length n^{1/4+ε}, Pólya–Vinogradov,
GRH for small non-residues, large sieve in the modulus n) concerns χ_n on *additively* structured sets of power size;
on L₃(n) only the cell structure survives. So "a character seeing L₃(n)" is equivalent to "the integral points of S_n
being 2-adically non-degenerate", i.e. to cell-restricted representation counts R_c(n), each a union over levels of
divisor-in-a-moving-class events (HJ_DEEP Prop 4.1; B2).

**Prop 3 (aggregate character data is congruence data; PROVED, a restatement of CLASS_FORCING Thm 2.1 at levels u).**
For a fixed level u and N = n + u, Π_{q^e ‖ N, q odd} χ_n(q)^e = χ_n(u)·(2/n)^{v₂(N)} and, for odd prime q | N, q ∤ n,
χ_n(q) = (−u/q). Both are functions of n mod 8u (and of q mod 4u). So every identity obtained from χ_n on the
*whole* fibre is a congruence condition on n (B1). It forces an admissible −1 divisor (A ≡ −1 mod u) by itself only
when (ℤ/u)^× has exponent ≤ 2, i.e. u ∣ 24 (the quadratic layer of FOREST_CONNECTIVITY Prop 3.1, Landau-type and
conditionally refuted as a complete proof under Schinzel's H). For u ∤ 24 the passage from "odd number of χ_n-odd
prime factors" to "a sub-product ≡ −1 (mod u)" is exactly the B2 class event. *Proof.* χ_n(N) = χ_n(u) since
N ≡ u (mod n); multiplicativity; reciprocity q ∣ n + u ⟹ (q/n) = (n/q) = (−u/q). The exponent-2 statement is
CLASS_FORCING Thm 2.1 / FOREST_CONNECTIVITY Prop 3.1. ∎

**Prop 4 (KS2: Salié / Kloosterman completion is a B3 instance; PROVED as a counting statement + Assessment).**
By Lemma 1 the words are the points (A, A*) of the modular hyperbola AA* ≡ 1 (mod n), 0 < A, A* < n, with
t := (AA* − 1)/n ≥ 2 and t ∣ A + 1 (then t ∣ A* + 1 automatically, since AA* ≡ 1 mod t), plus A, A* ≥ 2t − 1.
(i) For fixed t the strip tn ≤ AA* < (t+1)n contains exactly the points with AA* = tn + 1 (PROVED: AA* ≡ 1 mod n),
so every region in the (A, A*)-plane meets the word set in a union of single hyperbolas, one integer tn + 1 per t.
(ii) Under the extra congruence t ∣ A + 1 the expected number of points over all t is Σ_t τ(tn+1)/t ≍ log² n
(heuristic for the average; the pointwise count is N(n) = |L₃(n)|, which is ≍ log² n on average, DK 10.2).
(iii) The available pointwise error term for counting modular-hyperbola points in a region of area 𝒜 is
O(n^{1/2+ε}) (Weil/Salié), independent of 𝒜. Since the word set has total size ≍ log² n, a completion argument
needs an error ≪ log² n: B3's scale constraint (FRONTIER §3) applies verbatim. **KS2 fired (registered kill):** the
word region is a union of one-point-thick hyperbolas (i), and the completion only re-expresses each per-t divisor
problem. The Salié identity (twisted Kloosterman sums are sums over square roots mod n) converts a χ_n-weighted count
over a *thick* region into an unweighted count on a conic, but no thick region whose points are all words (or a
positive majorant supported on words) exists. *Scope:* this rules out completion over regions of the (A, A*)-plane;
it does not rule out high-multiplicity encodings (B3, Remark 2.4).

## 3. Kill tests (registered at checkpoint 1) — outcomes

### KS1 — non-abelian parity laws: DEAD on the registered dictionary
`scripts/z64_sdeep_words.c` (all words, all primes p ≡ 1 (8), p ≤ 2·10⁶; 37 116 primes, 1.8 s) +
`scripts/z64_sdeep_ks1.py` (cypari2 class numbers) → `data/z64/sdeep/ks1_report.txt`.
* Features: 368 per-pair sub-count parities (N₋, N₊, |L₃|, slices 4∣t / 4∣A,A* / 4∣u,v, all 40 cells (t mod 4,
  {u,v} mod 4)), each unrestricted and restricted to t ≤ 2, 3, 4, 8 and to min(u,v) ≤ 4, 8, 16.
* Invariants: (2/p)₄, (ℓ/p)₄ (ℓ = 3,5,7,11,13, where defined), h(−4p)/4 and h(−8p)/4 mod 2, h(−4p)/8, h(−8p)/8,
  h(−3p)/4 mod 2 (where defined), all 55 pairwise products (66 non-abelian invariants), plus the abelian bits.
* Method: for every feature f and non-abelian ρ, the best predictor of f ⊕ ρ that depends only on p mod 1680 (in-sample
  class majority) is compared with the same predictor for f alone; a law "f ≡ ρ + (congruence function)" shows up as
  accuracy ≥ 0.99 with a gain over the abelian fit.
* **Result (CERTIFIED for this range and dictionary):** 258/368 features are already congruence laws mod 1680
  (mostly cells that never occur); among the remaining 110, the maximal accuracy of f ⊕ ρ is 0.9981, reached only on
  the domain (3/p) = 1 where (3/p)₄ ⊕ h(−3p)/4 is constant and the feature is already abelian (gain 0); the largest
  gain of any pair is 2.5σ (of 7 260 pairs; noise). One non-trivial abelian parity law appears: the number of −1 pairs
  with min(u,v) ≤ 4 is odd iff (3/p) = −1 (p ≡ 17 mod 24, already a Mordell class).
* **Verdict: KS1 fired — NAP dead on this dictionary.** Scope: parities of the listed sub-counts versus the listed
  invariants and their pairwise products, p ≤ 2·10⁶. Not tested: mod-4 or mod-8 laws, weighted sub-counts, other
  governing fields.

### KS0 — the conjecture in adversarial families: did not fire (no counterexample)
`scripts/z64_sdeep_decide.c` (exact decision: u ≤ √(n/2) segmented factor sieve, or Pollard-rho early exit at the
first −1 word followed by full enumeration if none is found; validated against brute force for all n ≡ 1 (4), n < 4000,
0 mismatches). Outputs `data/z64/sdeep/ks0_*.txt` (columns: n, family, mode, has_word, pairs, −1 pairs, least u of a
−1 pair (full mode) / exit u (early mode), first u with a word).
| family | n | range | mode | (S)-failures | min N₋ (pairs) | mean N₋/|L₃| |
|---|---|---|---|---|---|---|
| (a) near-squares m² + k, −48 ≤ k ≤ 48 | 1 248 | 10¹²–8·10¹³ | full | 0 | 69 | 0.736 (lowest group k = 24: 0.62) |
| (b) d·m², d ∈ {5,…,105} (21 values) | 2 088 (timeout at 2 310) | 10¹¹–8·10¹³ | full | 0 | 65 | 0.738 (lowest d = 5: 0.68) |
| (c) n ≡ 1 (mod lcm(1..23)) | 14 999 | 5·10⁹–8·10¹³ | early | 0 | — | first −1 word at u ≤ 24 |
| (d) m² + k, m ≡ 0 (mod lcm(1..13)) | 622 | ≤ 9·10¹³ | early | 0 | — | — |
**Reading (EVIDENCE).** No failure; in the fully enumerated families N₋ ≥ 65 pairs and N₋/|L₃| ≥ 0.47 at every n.
Near-squares and fixed-character composites show only mild deficits (T1 deformation: at n = m² + k the sign of a word
with outer letter u is the character (u(u+k)/A), so slices with u(u+k) = □ are dead — finitely many u per k).
Square-mimicking n (c, d) are *not* hard for (S): words with one small letter and one large letter remain (only words
with both outer letters small are excluded, B1). The independent-pair coin model (DK 10.2, q ≈ 0.70) predicts
failure probabilities ≤ 0.3^{65} here.

### Census of N₋ at primes (EVIDENCE, `/tmp` dump of `z64_sdeep_words.c`, reproducible in 2 s)
Primes p ≡ 1 (8), p ≤ 2·10⁶: pooled fraction of −1 pairs 0.702; min N₋ (pairs) = 1 at 17, 41, 21841; = 5 in
(2·10⁵, 10⁶]; = 11 in (10⁶, 2·10⁶]; independent-pair model predicts 0.65 total failures, 0 observed (consistent with
DK 10.2). Hardest: 21841 (1 −1 pair of 10; least QNR 11; p ≡ 1 mod 840).

### Prime-A sub-statement (new census; EVIDENCE + Assessment)
"(S) with a prime certificate": some −1 pair has A or A* prime (equivalently: some n + u has a *prime* factor
q ≡ −1 (mod u), 2u − 1 ≤ q ≤ (n+u)/2, with the right cell). `scripts/z64_sdeep_primeA.c` →
`data/z64/sdeep/primeA_2e7.txt`: among the 317 477 primes p ≡ 1 (8), p ≤ 2·10⁷, it fails only at **20521, 21841,
589681**. The mean number of prime-certificate −1 pairs is ≈ c(p)·log p with c = 0.81, 0.89, 0.94, 0.97 in the decades
10⁴, 10⁵, 10⁶, 10⁷; a fit c(p) ≈ c∞ − b/log p gives c∞ ≈ 1.2. *Assessment:* in a Poisson model the failure
probability is ≈ p^{−c}, so prime-only (S) is expected to have finitely many exceptions only because c∞ > 1, and only
barely (for c ≤ 1 the expected number of failures diverges like log log x). Any argument that can only produce *prime*
witnesses (sieve / Chebotarev style) therefore works at the very edge of the random model; arguments using composite
divisors have expected count ≍ log² p.

## 4. Attempts at the other deliverables (honest log)

* **(a) Explicit infinite non-congruence family of primes.** The only mechanism tried that would give one (a parity law
  with a non-abelian invariant, KS1) is dead on its dictionary. Families defined by the factorisation of n + u (e.g.
  "p + 4 has a prime factor ≡ 3 (4)", FOREST_CONNECTIVITY Prop 3.1) are certificate-defined and give nothing new.
  Polynomial families: with letters linear in m and t constant, tuv − u − v = d·m² + k forces
  k = −d(x − β/d)² − αβ/d < 0 (u = α(m+x), v = β(m+y), tαβ = d; elementary coefficient comparison), so no polynomial
  family represents d·m² + k with k ≥ 0 (PROVED for this shape; cf. (J)84 for the general positivity obstruction).
* **(b) Threshold under a named hypothesis.** GRH, Elliott–Halberstam and Chebotarev-type hypotheses control Frobenius
  data; every (S)-witness condition is "q ∣ N" for a specific integer N ∈ {n + u, tn + 1}, which is not a Frobenius
  condition (Prop 3: the Frobenius-visible part is n mod 8u). We found no standard hypothesis implying (S) at every
  large n; the hypotheses that do imply it (pointwise divisor-in-class statements) are reformulations of B2
  (Assessment).
* **(c) Counterexample.** None (KS0; plus the ≤ 10⁹ census of HJ_DEEP/R174).
* **(d) Precise missing lemma** — §5.

## 5. Precise missing lemma

By Lemma 2, (S) is equivalent to:
**ML (2-adic escape).** For every non-square n ≡ 1 (mod 4) [large], the set S_n(ℤ_{≥2}) of integral points of
tuv − u − v = n is not contained in the five classes C₊ mod 4.
Equivalent sign-free form (PROVED equivalent, DK Thm 4.5): there are u ≥ 2 and a divisor A of n + u with
A ≡ −1 (mod u), 2u − 1 ≤ A ≤ (n+u)/2, such that 4 divides one of t = (A+1)/u, u, v = (n+u)/A, A, tv − 1.
**What any proof of ML must contain (Assessment, with the proved pieces cited):**
1. a step producing a divisor of a specific integer N (n + u or tn + 1) in a residue class whose modulus grows with the
   level — no fixed finite menu of levels suffices (B2 Thm 2.2(iii), CONDITIONAL on H; HJ_DEEP Lemma 3.2 for
   fixed-pair families, PROVED);
2. at that step, χ_n-information can enter only as n mod 8·(level) (Prop 3, PROVED), and the sign itself only as the
   cell selection (Lemma 2, PROVED) — so character-sum, GRH or Rédei input cannot be the step;
3. the count of candidate events is ≍ log² n (≍ log n if only prime divisors are produced), so a counting step needs
   error o(log² n) pointwise — not available from completion (Prop 4) or averages (B6).
**Escape hatches left open** (not excluded by anything above): high-multiplicity encodings (B3 Remark 2.4); a
non-counting structural argument acting on the factorisations of the n + u for many u *jointly* beyond aggregate
products (CLASS_FORCING §6 "full factor multiset"); mod-4/8 (not mod-2) laws of weighted counts.

## 6. Verdict

**NARROWED.** No HOT LEAD; ES and (S) remain open.
* **PROVED:** Lemma 1 (trace form of the sign; certified on 37 116 primes); Lemma 2 (character blindness: (S) ⟺ ML,
  2-adic escape of integral points); Prop 3 (aggregate χ_n data = congruence data; restatement of CLASS_FORCING
  Thm 2.1 at levels u); Prop 4 (i)–(iii) (completion over the (A, A*)-plane meets words in one-point-thick
  hyperbolas; KS2 fired); no polynomial word family for d·m² + k, k ≥ 0, in the shape of §4(a).
* **CERTIFIED / EVIDENCE:** KS1 dead (no non-abelian parity law, 7 260 feature–invariant pairs, 37 116 primes);
  KS0 no counterexample among 18 957 adversarial n ≤ 9·10¹³ (min N₋ = 65 among 3 336 fully enumerated);
  prime-certificate (S) fails only at 20521, 21841, 589681 among primes p ≡ 1 (8) ≤ 2·10⁷.
* **Answer to the brief's question** ("what extra structure lets a character see L₃(n)?"): on L₃(n) the character is
  a fixed 2-adic cell function (Lemma 2); there is nothing else for a character to see. The structure that would have
  to be exploited is the *divisor* structure of the integers n + u / tn + 1 (B2), not character values.

## 7. Four FRONTIER §4 hard screens (for ML / the lane's best idea, the trace–cell reformulation)
* T1 squares: built in (cells C₊ exactly at squares) — PASS (non-squareness enters only as "escape from C₊").
* 8/131 (numerator 8 / C-even sub-line): (S) uses all five slices; per-slice laws were tested and none exists —
  not applicable to a mechanism (none found).
* Tied modulus: FAILS to escape — every certificate is a divisor of n + u in the class −1 (mod u) (Prop 3, Lemma 2).
* Fixed p: no averaging used; but no pointwise mechanism found.

## 8. Proposed FRONTIER text (do NOT edit FRONTIER here)
*§6 / z64 block (SDEEP):* Conjecture (S) as a character-value problem. PROVED: for γ ∈ Γ₀(n), (d/n) = ((tr γ ± 2)/n), so
the sign of a word is (t(u+v)/n) (trace form); and the sign on L₃(n) factors through the n-free mod-4 cell map, so (S)
⟺ the integral points of tuv − u − v = n escape the five cells C₊ (T1: they never do at squares). Aggregate χ_n data on
a fibre is congruence data (CLASS_FORCING Thm 2.1); Salié/Kloosterman completion meets the words in one-point-thick
hyperbolas (B3). CERTIFIED/EVIDENCE: no non-abelian parity law for 368 sub-count parities vs 66 Rédei/quartic/class-
number invariants (p ≡ 1 (8) ≤ 2·10⁶); no (S) failure among 18 957 adversarial n ≤ 9·10¹³; prime-certificate (S)
fails only at 20521, 21841, 589681 (p ≡ 1 (8) ≤ 2·10⁷), with expected count ≈ 1.2 log p (barely Poisson-safe).
Narrowed: character tools have nothing to act on beyond cells; the missing step is a divisor of one integer in a
moving class (B2).

## 9. Bottom line
(S) looked like a pure character problem: show that χ_n is not identically 1 on the log²-size set L₃(n). It is not a
character problem. On L₃(n) the Jacobi symbol is a fixed function of the letters mod 4 (and equals (t(u+v)/n), the
character at the trace + 2), so every character-sum, GRH, large-sieve or Rédei argument sees only which 2-adic cells
the integral points of tuv − u − v = n occupy. T1 is the statement that at squares they occupy only five cells. The
three mechanisms registered here all failed their kill tests or found nothing: no non-abelian parity law, no
completion with a positive-thickness region, no counterexample in adversarial families up to 9·10¹³ (N₋ ≥ 65 there).
What remains is the familiar tied-divisor event, now stated as a 2-adic escape lemma for integral points (§5).
