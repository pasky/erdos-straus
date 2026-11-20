# Hostile cross-review, Round 2: `PROTH_ALLM.md` §§6–8 and `PROTH_RIGIDITY.md` §§5–6 (`git log 267ebe46c..`)

**Reviewer:** Claude (Anthropic), running in Claude Code as the requested fresh Opus reviewer. The harness does not show the
exact model ID, so I do not state one. There were no provider, auth or quota errors.
**Scope:** all 8 commits after 267ebe46c (29b16df4, dae1abb4, ab579758 merge, b7b718d4, 15fd472e, 60bb0e09, ea5a3cdf,
a87adc12). The diff touches only `notes/z78/PROTH_ALLM.md`, `notes/z78/PROTH_RIGIDITY.md`,
`data/z78/proth/primary-3-199.json`, `scripts/z78_proth_primary.py` and `scripts/z78_proth_primary_check.py`. No master file
was edited, so the lane rule holds. I re-proved every Round 2 statement by hand. I did **not** take the author's checker
or its data as assumptions: I wrote my own replay from the note text, `scripts/z78_r2opus_replay.py`, which does not import
or reuse the author's scripts.
**Nothing in Round 2 asserts ES at all s for any new m, and nothing here should be read that way.**

## 0. Verdict

| item | verdict |
|---|---|
| Thm 7: unit-only certificates for h=3..199 (m=2..100), cores and density one | **Correct.** All 99 rows were rechecked independently. A literal integer end-to-end construction passes at h=3,5,7,9. 31 rows beyond the table (h=201..261) are generated and verified. Form fixes F2 and F3 |
| §6 certificate-construction Assessment | Correct as an Assessment. Note that it still needs the full factorization of H (F7) |
| Thm 8: divisor-paid negative orbit; h=2^{12t+6}+13 | **Correct.** Re-proved, and the identity was replayed numerically at h=77 and h=262157 |
| Thm 9: arbitrary-shift word bound | **Correct** (elementary size bound). Exhaustive brute force agrees |
| Cor 9.1: modulus/cutoff lower bound | **Correct but overframed** (F4). The sparse family plays almost no role. The statement concerns the initial segment s≤m |
| PROTH_RIGIDITY Prop 5.1: tail limit set (corrected formula) | **Correct.** The correction was needed: the old "closure" version was false at the finite terms. The finite-level replay agrees |
| PROTH_RIGIDITY §5 exact finite-cover test | Correct relative to EXPONENT_COVERING Thm 1.4, through its family-agnostic proof (cite it, F10) |
| PROTH_RIGIDITY Prop 6.1: two mod-7 triples | **Correct**, but trivial. It refutes a self-posed analogue only (F8) |

I found no mathematical error. There are four required fixes, all of form, scope or labelling: F2, F3, F4 and F9.

## 1. Theorem 7: re-proof and attacks

**Word congruences.** h is odd, H=2^h−1, k=2H+1=4^m−1 and u=2H. A=c·F, where c|k and F is a product of distinct cyclotomic
factors of X^D+1 with X^D+1 | 2^s+1. Then A | k(2^s+1)=n+u. The requirements are A≡−1 (mod H) and A≡1 (mod 16). The second
holds because c≡1 (mod 16) and r'≥4 give X≡0 (mod 16). Together they give A≡7u−1 (mod 8u), since H≡−1 (mod 16) for h≥4.
At h=3, 14·7−1=97≡1 (mod 16), so this case also works. Hence t≡7 (mod 8). Since n+u≡7 (mod 8) for s≥3, also v≡7 (mod 8),
so t,v≥7. Then tuv−u−v=v(A+1)−u−v=n. The direct triple ADn, uD, AuD with D=(tv−1)/4 satisfies 4AuD=u+(A+1)n. All of this
is re-derived. ✓

**Realization at X≡2.** r'≡1 (mod h) and 2^h≡1 (mod H) give X=2^{r'}≡2. For an odd prime ℓ≡a (mod h) with ℓ∤h,
Φ_{2ℓ}(X)=(X^ℓ+1)/(X+1)≡(1+2^a)/3=B_a/B_1. Also Φ_2(X)≡Φ_6(X)≡3. Φ_2 always divides X^D+1 for odd D, and Φ_6 does so iff
3|D. All the selected factors are distinct cyclotomic factors of X^D+1, so their product divides it. I spot-checked the
evaluation with random ℓ<3000 and r'≡1 (mod h) at h∈{5,7,9,11,13,15,21,27}, computing Φ_{2ℓ}(2^{r'}) directly mod 16H. ✓
(Form nit: say *odd* primes ℓ. The class a can be even, and ℓ=2 would give Φ_4.)

**Steering.** Strip the h-primes from s/D to get r, with residue ρ (mod h). Divide by the reserved prime p_ρ | r, which
satisfies p_ρ≡ρ, p_ρ∉D and p_ρ∤h. The result r' is ≡1 (mod h). The quotient s/(r'D)=p_ρ·(h-part) is odd. The construction
is not circular, because ρ is computed after all the steering primes are already in r. ✓ The core period works as follows.
Take P = 4·(the ratio primes)·(one steering prime per unit class ≠1)·(3 if 3∈T0). For P|s we have 4|r', so no spare prime
is needed. ✓ **Square-unit closure:** take multiples of P that are also multiples of the orders of 2. At those s, n is 4^m
at the odd part and 1 at the 2-part. This is the same argument as §1, and it is valid. Theorem 7 does not state it, yet the
§0 STATUS delta claims it (F2).

**Density one.** We need s to have, in each unit class, at least e_a distinct prime factors, plus steering primes and a
spare prime. By the divergence of Σ1/p over a progression and a second moment (Turán–Kubilius), this holds on a set of
density 1. Inside any fixed progression it still holds after discarding finitely many primes. ✓

**The 9|h case.** Here T0={1,3}, which needs 3|D⊂s. When 3∤s, we have 7|H, k≡1 (mod 7) and 2^s∈{2,4}, so n≡3 or 5
(mod 7). These are nonresidues, so n is a non-square, n≡1 (mod 4) and outside every odd-square class mod 840. Thus
CONJS_GEN Thm 2 gives (S), i.e. a good word. ✓ **However,** CONJS_GEN Thm 2 is itself relative to the computer-assisted
Z64_SDEEPF Thm 3.6, and the §0 label omits this (F3). The 3∥h rows use only Φ_2, so they need no fallback. ✓

**Data claims replayed** (my code, not the author's checker):
* **The 99 rows.** All 99 rows satisfy c·3^{|T0|}·∏(B_a/B_1)^{e_a}≡−1 (mod H), with c|k, c≡1 (mod 16) and c∈{1,2^m+1}.
  Every index a is a unit with 1<a<h, and every multiplicity is a positive integer.
* **The pattern claims hold exactly.** The 66 rows with 3∤h all have c=1 and T0=∅. The 22 rows with 3∥h all have T0={1}
  and c=1. The 11 rows with 9|h all have T0={1,3} and c=2^m+1.
* **Literal end-to-end integer construction.** I used my own minimal-D certificates found by subset search, not the
  table's. I built s exactly as in the proof, including stripping and a non-trivial steering prime. I then computed the
  actual integers A and n=k·2^s+1 and checked: A/c | X^D+1, A | n+u and u | A+1; t,v≥2 with t≡v≡7 (mod 8); tuv−u−v=n and
  8|(n+t); and the ES identity 4AuD=u+(A+1)n. The runs were:

  | h | c | T0 | ratio primes | s (≈ bits of n) |
  |---|---|---|---|---|
  | 3 | 1 | {1} | 5, 11 | 78,540 |
  | 5 | 1 | {1} | 7, 17, 19 | 17,047,940 |
  | 7 | 17 | {1} | 5, 13, 19, 23 | 46,243,340 |
  | 9 | 33 | {1,3} | 7, 17, 53 | 16,272,060 (exercises Φ_6 and 3∣D) |

  At h=11 no certificate exists in the small pool. This end-to-end run is evidence that the steering recipe is literally
  right, not just abstractly right.
* **Beyond the table, author's generator.** I ran the author's generator through a wrapper with a bigger PARI stack
  (`scripts/z78_r2opus_beyond_pari.py`). At h=211 the default 8 MB stack overflows inside `factor`. It produced rows for
  h=201..261 (m=101..131), and **all 31 pass my independent checker** (`data/z78/xreview/r2opus_primary-2*.json`). The
  same c/T0 pattern persists: h=207, 225, 243 and 261 use c=2^m+1 with T0={1,3}.
* **Beyond the table, factorization-free.** Use 2^{−1}≡2^{h−1} (mod H). Then B_{h−1}/B_1≡1/2, so
  2=(B_{h−1}/B_1)^{h−1} with a nonnegative exponent and no group order needed. With B_1=3=B_3/B_1 this turns the
  §1 and §7 identities into explicit nonnegative certificates of weight ≤a(h−1)+2b. I generated and verified them for all
  143 odd h in [201,1001] with 3∤h satisfying the §1 or §7 hypothesis. 26 of these are outside §1. 124 of the 267 such h
  satisfy neither hypothesis. Output: `data/z78/xreview/r2opus_beyond.json`.

**Quantifier attack, and the size of the objects (F2).** Total multiplicity per row is the number of *distinct* primes
that s must contain. The 99 rows give:

| statistic | value |
|---|---|
| maximum | 5.4·10^56 (h=199) |
| median | 7.2·10^22 (h=83) |
| rows with weight <10^6 | only 13 |

So for most m the core period P is a product of more than 10^20 primes. The density-one set has no element below
roughly exp(10^20). "Density one" is true but purely asymptotic, and a STATUS reader must be told so. The factorization-free
§1/§7 certificates above have weight O(h²), which is dramatically smaller. I suggest the note mention this for the m it
covers.

## 2. §6 certificate-construction Assessment

Modulo R, every unit-index B_a has the image g of B_1. Telescoping gives
∏_{i<o}B_{2^i a}=(2^{2^o a}−1)/(2^a−1)≡1, using gcd(2^a−1,H)=1, so g^o=1. Since c=2^m+1=B_m and m=2^{−1} is a unit, the
target −1/(c·3^{|T0|}) has order dividing 2o in G/R. ✓ The generator still calls `factor(H)` (PARI, BPSW-level
primality) to obtain exponents and the p-primary projections. "No large dlogs" must not be read as "factorization-free"
(F7). This is irrelevant to correctness, since the checker multiplies integers mod H.

## 3. Theorem 8

* **The orbit identity.** Write 2^b≡−a (mod h) and d=2^a−1 | 2^{h+1}−1=k, using a|h+1. With a≥4 and h+1≥4 we get
  k≡d≡−1 (mod 16), so c=k/d≡1 (mod 16). Modulo H, k≡1, so −1/c≡−d=1−2^a. Next,
  2^a∏_{i<b}(1+2^{2^i})=2^a(2^{2^b}−1)≡2^a(2^{−a}−1)=1−2^a. ✓ Every factor lies in R: 2=B_1/B_{−1}, and
  B_j=(B_j/B_1)(B_3/B_1), which uses 3∤h and h≥5. ✓
* **The family.** 2^6≡−1 (mod 13) gives 13 | h+1, and h−13=2^{12t+6} gives −13∈⟨2⟩. We have h≡2 (mod 3), and 7|h because
  2^{12t+6}≡1 (mod 7). Since ⟨2 mod 7⟩={1,2,4}, −1∉⟨2 mod h⟩, so these h are genuinely outside §1. ✓
* **Replays.** The congruences hold for t=0..3. The full identity c·F≡−1 (mod H) holds at t=0 (h=77) and at t=1
  (h=262157, with a 262,157-bit H).
* **Search.** For h<400 exactly 10 values satisfy Thm 8 but not §1: 35, 49, 77, 203, 245, 299, 323, 329, 371, 395. The
  explicit unit-ratio product checks at h=35, 49, 77 and 203.
* **Optional generalization.** The example is one case of h=2^j+a with a | 2^j+1, a≥4, h odd and 3∤h. Then a | h+1 and
  −a≡2^j. For instance a=11 with j≡5 (mod 10).
* **Form.** "It suffices that …" is placed before the conclusion. Restate it as a standard hypothesis → conclusion.

## 4. Theorem 9 and Corollary 9.1

**Theorem 9.** Put L=2^{s−a}. Then n=L(u+1)+1, and the word equation gives v(tu−1)=(L+1)(u+1). Since tu−1≥u+1, v≤L+1. So
u(tv−1−L)=L+1+v∈(0,2(L+1)], which forces u≤2(L+1). ✓ This needs t≥2 ("interior"). The case s≤m, m≥2 gives
u≥4^m−2>2^{m+1}+2. ✓ A brute force over m≤4, s≤14 and all 0≤a≤s enumerated every word (t,v≥2). There is no word with
u>2(L+1) (0 violations), and 55 words exist where the bound allows them. Neither the bound nor the proof uses k=4^m−1. Any
k works.

**Corollary 9.1.** For odd q≤R, ord_q(2)≤φ(q)<R divides lcm(1..R) | m. This includes composite q, which is needed because
moduli may be composite. So q | k and n≡1 (mod q). Also 2^j≤R≤2^s, so n≡1 (mod 2^j). Hence n≡1 modulo every M≤R, and
every square-unit-avoiding class misses it. I replayed this for R≤12, B∈{1,3,5,7} and m∈{1,2,3}·lcm(1..R). ✓

**Critique (F4).** The square-unit part, n≡1 modulo every M≤R, holds for **every** s≥log₂R once lcm(1..R) | m. It has
nothing to do with sparsity. Theorem 9 is a trivial size bound, and it only bites at s≤m, which is the finite initial
segment. The sparse family is used only to pick one exponent in (m/2,m]. The corollary therefore says: "for these m,
certificates restricted to moduli ≤R must solve directly every exponent of the family up to about m/2." That is true, but
it is far from a "quantitative sparse obstruction", and it does not touch the sparse *tail* problem raised by Prop 5.
Concretely:
* the §8 title should change;
* §0's "lower bound for shifted-word plus square-avoiding congruence certificates on s=B·2^v" should be rescoped, for
  example to "uniform-in-m certificates need growing fixed moduli or an initial direct segment of length ≫m; initial
  segment only";
* triage should be BARRIER-SCOPED (FRONTIER §6 one-liner) at most.

**F5 (small).** The "at m_R=lcm(1..R)" sentence also needs m_R≥max(2B,2⌈log₂R⌉). For example B=100 and R=3 fail.

## 5. PROTH_RIGIDITY §§5–6

**Prop 5.1, corrected.** The correction from "closure of the sequence" to "⋂ of tail closures" was necessary. Every
finite term B2^v+a has 2-component B2^v+a, not a, so the old formula was false. The new proof works in both directions:
* *Forward:* take v_i→∞ and pass to a compact subsequence with limit ω∈Ẑ. v↦2^v (mod odd N) depends on v mod ord_N(2),
  which makes the map continuous.
* *Converse:* every ω∈Ẑ is a limit of integers v_i→∞, and then 2^{v_i}→0 in Z_2.

For 0∉E: a=0 is forced, and the component B·2^ω≠0 at ℓ∤B. ✓ The finite-level replay matches: for N up to 32·9·11 and
several B and a, the tail residue sets equal {x≡a (mod 2^e), x≡a+B·2^w (mod N_odd)} with the coupling through one w.

**Exact finite-cover test.** Ẑ is compact and the classes are clopen. EXPONENT_COVERING Thm 1.4 is stated for {n_m}, and
the note should cite its "family-agnostic" remark (line ~80), not the theorem alone (F10). The 2-adic component of n is 1,
since real s→∞, while the odd components of 2^s use μ_2=a. That is consistent with "2-component interpreted as 1".

**Prop 6.1.** The re-proof is short:
* m≡2 (mod 3) gives 4^m≡2, so k≡1 (mod 7).
* 3∤B gives s≢0 (mod 3), so n≡3 or 5 (mod 7).
* Both triples satisfy 4xyz=n(xy+yz+zx), checked for r<2000. They match `lean/ES/ES/Proth15.lean` `cls_7_3`/`cls_7_5`
  coefficient for coefficient. I did not rerun Lean, and the label correctly no longer says "Lean-verified".
* 5,720 sparse instances land in classes 3 and 5. For 3|B the classes are always QR mod 7.

**Critique (F8).** This is the s_cls_0/s_cls_1 argument of the existing k=15 proof (m=2), with only k≡1 (mod 7) used.
It gives ES at **every** s with 3∤s, not only on the sparse set, for all m≡2 (mod 3). Saying so makes clear why it
"refutes" sparse rigidity: the sparse set simply avoids the hard class 3|s. The refuted statement was never proposed in
any master file (I grepped STATUS and FRONTIER). Triage: METHOD-CX / NULL, not a barrier. The 3|B remark is correct.

## 6. Required and suggested fixes

**Required:**
* **F2 (Thm 7 statement and §0).**
  * State the square-unit closure inside Theorem 7, since the STATUS delta claims it.
  * State the sizes: total multiplicities up to 5.4·10^56 and median ≈7·10^22, with only 13 of 99 rows below 10^6. The
    period and density-one sets are purely asymptotic, and the first admissible s is astronomically large.
  * Optionally use the factorization-free O(h²) certificates for h satisfying §1 or §7.
* **F3 (labels).** §6/§0 must say "rel. CONJS_GEN Thm 2 (itself rel. computer-assisted Z64_SDEEPF Thm 3.6)" for the 9|h,
  3∤s exponents.
* **F4 (§8 framing and triage).** Rescope §8 and §0 as in §4 above. Classify Thm 9/Cor 9.1 as BARRIER-SCOPED. Split the
  single "Triage: HEADLINE" by item:
  * Thm 7 and Thm 8 are a RECORD-type extension of the §1C row (cross-review owed from the other lab, i.e. Astra).
  * §8 is BARRIER-SCOPED.
  * PROTH_RIGIDITY §6 is METHOD-CX.
* **F9 (Review line).** Replace "Round 2 review pending" with this file. Note that an Astra (other-lab) review of this Claude
  work is still owed under AGENTS §3 before any STATUS promotion.

**Suggested:**
* **F1.** Merge the two §0 "Result" lines into the one-sentence format.
* **F5.** Add the m_R≥2B condition.
* **F6.** Restate Thm 8 as hypothesis → conclusion, and optionally give the general h=2^j+a family.
* **F7.** In the Assessment, add that the generator needs factor(H).
* **F8.** Add the remark that Prop 6.1 covers all 3∤s, with the k=15 precedent.
* **F10.** Cite the family-agnostic remark of EXPONENT_COVERING.
* **Nit.** Say "odd primes ℓ".
* **Hygiene.** The untracked `data/z78/proth/primary.log` is not from this review, and it should not be swept into a commit.

## 7. Replay

```
ulimit -v 1500000
for w in rows e2e thm8 thm9 cor9 prop6 prop5 beyond; do timeout 1700 uv run --offline --no-project python -B scripts/z78_r2opus_replay.py $w; done
uv run --offline --no-project python -B scripts/z78_r2opus_replay.py checkfile data/z78/xreview/r2opus_primary-211-261.json
# generator beyond the table (author's solve, bigger PARI stack), then check with the line above:
timeout 1700 uv run --offline --no-project --with cypari2 python -B scripts/z78_r2opus_beyond_pari.py 211 261 OUT.json
```

Every mode ran in under 1 minute; the e2e mode took about 4 s and the generator run for h=211..261 about 44 s. The author's
checker also passes (`99/99`). Nothing was committed and no master file was touched.
