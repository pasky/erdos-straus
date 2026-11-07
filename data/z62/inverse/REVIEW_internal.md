# Hostile internal review of Z62_INVERSE.md (commit bb8ebbdc)

Reviewer: internal subagent. Scope: every proof step and number of Lemmas 1–6, Cor 3 and Prop 4, the falsifier table,
the kill test against the pre-registration in commit 6500828e, tests 2/3, labels and prior-art attributions.
ES is OPEN; the memo never claims otherwise (checked).

**Verdict of the review.** No fatal error: the main verdict ((INV-main) dead by its pre-registered rule) stands, and
every number I re-ran reproduces exactly. There is one false PROVED statement (Lemma 5, parity of the genus twist when
s ≡ 3 mod 4), one false attribution (the "p + 4 instance" in Cor 3), two missing prior-art credits that undercut the
"why not closed" claim (Z52D_FOURIER / rank_O already did the B/T/Q/S split at hard primes vs controls, and
Z54_HCKILL Lemma 1.2 *is* Lemma 2), a wrong population label (F3 numbers), a false statement about the checkpoint
(F3 *was* changed), and several unlabelled "randomness" overclaims that must become Assessment, plus explicit
low-power wording for the kill test.

---

## 1. Fatal errors

None. The memo's main verdict follows its pre-registered rule, the proved lemmas that the verdict uses (Lemma 1, Lemma 2,
Cor 3, Prop 4) are correct up to the fixes below, and no claim touches the status of ES.

---

## 2. Errors to fix

### E1 (MAJOR, false PROVED statement): Lemma 5, the parity of χ_{−4u}χ_{s*}
The memo says: "let s* = ±s ≡ 1 (mod 4) … Then ψ = χ_{−4u}χ_{s*} is an odd real character mod 4u". But
ψ(−1) = χ_{−4u}(−1)·χ_{s*}(−1) = (−1)·sign(s*). For s ≡ 3 (mod 4) we have s* = −s < 0, so ψ is **even** and can kill
nothing. Example: s = 3, u = 3. Then χ_{−12}χ_{−3} is principal on ℓ ∤ 6, and the memo's ψ(ℓ) = (−(n/3)/ℓ) = (3u/ℓ) =
(9/ℓ) = 1 holds vacuously. The real kill at n = 147 = 3·7², u = 3 (N = 150, P = {5}, type T, checked) is by
χ_{−4} = χ_{−12}·χ_{12}. This matters for F3, because 3 and 7 (both ≡ 3 mod 4) divide most of the 285 composite zeros.
The "identically forced (twisted T1)" sentence is false as written for s ≡ 3 (4). With n = s·k², the memo's ψ gives
(−k²/ℓ) = (−1/ℓ), which is not identically 1.
**Corrected text:** "Let s | n be odd and let χ^{(s)} be the *even* real character with χ^{(s)}(ℓ) = (s/ℓ) for odd ℓ, i.e.
χ_s if s ≡ 1 (4) and χ_{4s} if s ≡ 3 (4). Suppose its conductor divides 4u (⟺ the squarefree kernel of s divides u).
Then ψ = χ_{−4u}χ^{(s)} is an odd real character mod 4u, and ψ(ℓ) = (ns/ℓ) = ((n/s)/ℓ) for every prime ℓ | n+u, ℓ ∤ 2u.
So a ψ-kill says 'n/s is a QR modulo every such ℓ'. For n = s·k², ψ(ℓ) = 1 identically (twisted T1; this agrees with
Z60_MS105 Lemma 1: s ∤ uC)." Also fix F3's phrase "a genus twist χ_{−4u}·χ_{s*} transfers to the Jacobi symbol
(±m/ℓ)" to "… χ_{−4u}·χ^{(s)} transfers to ((n/s)/ℓ)". The letter m is already used for the modulus.
The rest of Lemma 5 (the prime case, ψ = χ_{−4u}χ_{D′} with D′ > 0, p ∤ D′, ψ(ℓ) = (pD′/ℓ)) is correct.
*Supporting EVIDENCE the memo could add:* in the census, the composites' T-excess sits at gcd(k, n) > 1, as the
corrected Lemma 5 predicts. For u ∈ [17, 256]: K with gcd > 1 has T|f 0.400 and st|f 0.806; K with gcd = 1 has 0.256
and 0.663; controls have 0.234 and 0.637. A smaller residual remains at gcd = 1 (+0.026 for u, +0.038 for C).

### E2 (MAJOR, false attribution / false implied implication): Cor 3 header, "the C = 1 and p + 4 instances are the 'S'-conditions of Z54_HCKILL Lemma 1.1"
Cor 3 contains no p + 4 condition, because u = 4 (m = 16) is not an exponent-2 slice. Z54 Lemma 1.1's p + 4 ∈ S
belongs to the HC line-4 family (p + x or xp + 1 has a divisor ≡ −1 mod x), and R(p) = 0 does **not** force it. At the
zero p = 409, 413 = 7·59 with 7 ≡ 3 (4). In total p + 4 ∉ S at 5 of the 14 zeros: 409, 577, 23929, 102001, 1134241.
**Corrected text:** "(… PROVED; the C = 1 instance, 4p + 1 ∈ S, is one of the two S-conditions of Z54_HCKILL
Lemma 1.1. The other, p + 4 ∈ S, belongs to the HC line-4 family and is not forced by R(p) = 0, e.g. p = 409. The
u = 1 instance (p+1)/2 ∈ S is its R-analogue.)"

### E3 (MAJOR, prior art): Lemma 2 is Z54_HCKILL Lemma 1.2(a),(c)
Z54_HCKILL Lemma 1.2(a) already proves that G has exponent 2 ⟺ x | 24 (x ∈ {4, 8, 12, 24}), and that divisor residues
= H_N. Its proof is the same as the memo's (F₂-span of the prime classes). Lemma 1.2(c) already gives the
non-exponent-2 starved examples with at most two primes, which is what the p = 409, u = 4 example illustrates.
The memo credits neither.
**Fix:** Lemma 2 header → "(PROVED; = Z54_HCKILL Lemma 1.2(a), restated for the u/C slicings; the converse is
Lemma 1.2(c))".
Also, "For every other u, starved failures occur. Example (CERTIFIED): p = 409 …" is supported by only one example, so
the memo has not justified "every other u". Replace with: "For every other m ∈ 4ℕ, S is possible (Z54_HCKILL
Lemma 1.2(c); directly: take g of order ≥ 3 in G_m and N = ℓ₁ℓ₂ with ℓ₁ ≡ g, ℓ₂ ≡ −g, so −1 = ℓ₂ℓ₁⁻¹ ∈ H but
Div = {1, g, −g, −g²} ∌ −1). EVIDENCE: in the census, S occurs at every u and every C ≤ 256 outside {1, 2, 3, 6}.
Example (CERTIFIED): p = 409, u = 4 …"

### E4 (MAJOR, prior art; undercuts §1 "Why not closed"): the B/T/Q/S split and its hard-vs-control comparison already exist
§1 says: "Neither asked whether a zero has an atypical distribution of obstruction types across scales". But
Z52D_FOURIER (preamble and §0(b)), via rank_O's `scripts/z52d_rank_O_charobs.py`, already split obstructed windows into
χ_{−e}-kill / other real (genus) / non-real / poverty-type. Those are this memo's B / T / Q / S. It compared hard
primes with controls and found a χ_p-kill excess "largely what the hard set's selection (small BM main term) implies",
which is the very residual this memo reports. It also has the decomposition "every other odd real character is
χ_{−e}·ψ with ψ even real" used in Lemma 5.
**Fix (§1):** "Z52D_FOURIER / rank_O already split window obstructions into χ_{−e} / genus / non-real / poverty kills
and compared hard primes with controls on the Type II e-windows. They found only a χ_p-kill excess attributable to
small-BM selection. New here: the same split on R's u- and C-slicings, *conditional on failure*, at the actual zeros
and fresh near-zeros, under a pre-registered rule; plus the joint-failure tests." Also credit Z52D_FOURIER for the
χ_{−4u}·χ_{D′} decomposition in Lemma 5. In §4.1, cite Z52D_FOURIER §0(b) for "the known small-M_BM selection".

### E5 (MAJOR, prior art): Lemma 6 is prior, not "in the spirit of"
The slice part ("every hit uses d with χ_{−4u}(d) = −1, hence a prime ℓ | d with χ_p(ℓ) = −1") is Z59_MSPF Lemma 1.5
(every hit modulus is a χ_n-non-residue), Z57_BFII Lemma 2.1, and the Z60_LOPEZ coupling lemma. The Type I part is the
standard BM/T1 sign computation.
**Fix:** "Lemma 6 (PROVED, elementary; prior: Z59_MSPF Lemma 1.5, Z57_BFII Lemma 2.1, Z60_LOPEZ coupling lemma;
recorded for Type I in fable-5's form)". Remove "STEP2 is anti-supported" from the PROVED header (see W3).

### E6 (MODERATE, false statement about the checkpoint): §0 heading "the checkpoint-1 version is unchanged in substance"
`git show 6500828e:Z62_INVERSE.md` F3 reads: composite zeros "have slice-type profiles **indistinguishable** from the
prime zeros in the first census". The final F3 says they "are the one population with *extra* structure (+0.05…+0.09)".
That is a reversal. The checkpoint's own numbers already contradicted it (K u-bands 0.68/0.72 vs c 0.63/0.63).
**Corrected text:** "(final; F1, F2, F4 unchanged in substance from checkpoint 1. **F3 corrected**: the checkpoint called
the composites 'indistinguishable', but the kill-test statistic shows a T-driven excess +0.05…+0.09.)"

### E7 (MODERATE, wrong population): F3 numbers
§4.1: "**F3:** the 237 composite zeros ≥ 2·10⁴ have Δ st|f = +0.053 … +0.086 (SE ≤ 0.006)". These numbers come from
`killtest.py … K c`, which uses **all 285** K (no 2·10⁴ cut; checked). Restricted to the 237 K ≥ 2·10⁴ (my rerun),
Δ st|f = +0.048, +0.077, +0.046, +0.065 (SE ≤ 0.006).
**Corrected text:** "the 285 composite zeros have Δ st|f = +0.053 … +0.086 (SE ≤ 0.006; +0.046 … +0.077 for the 237 ≥
2·10⁴), mostly T." F3's "+0.05…+0.09" is then correct for all 285.

### E8 (MODERATE, statistics / overclaim): low power of the kill test must be explicit, and the residual is not "only" u [65–256]
* The pre-registered test has 6 near-zeros. Bootstrap SEs are 0.013–0.049, so the 95 % intervals are up to ±0.1. At
  u [17–64], Δ B|f = +0.024 ± 0.049 cannot exclude a +0.10 structured excess. The point criterion was met as
  pre-registered (honoured: same sets, bands, families, threshold, controls; completeness of the 6 near-zeros and their
  R independently verified). The **evidential weight is low**, and the memo's "(that is all of them; low power)" is
  too quiet given the bold "DEAD".
* The exploratory comparisons (larger samples) do show **statistically significant** structured (B) excesses below the
  0.05 tolerance: n vs c B|f u [65–256] +0.034 (SE 0.008, 4σ) and u [17–64] +0.029 (0.014); Z vs c B|f u [65–256]
  +0.039 (0.016) and **C** [65–256] +0.033 (0.011, 3σ). So "The only consistent residual is a BM-share excess of about
  +0.03–0.05 at u ∈ [65, 256]" is wrong about the location (C [65–256] too). Its attribution "which is the known small-M_BM
  selection" is untested here, so label it Assessment and cite Z52D_FOURIER §0(b).
* **Corrected §2 bullet:** "Pre-registered kill test fired (EVIDENCE; low power: 6 near-zeros, SE up to 0.049, so
  structured excesses up to ≈ 0.1 are not excluded). Beyond u, C = 16, the failing slices of the fresh near-zeros
  have type shares within the pre-set tolerance |Δ| ≤ 0.05 of class-matched controls. Exploratory (larger samples):
  the 14 zeros and the 125 R ≤ 4 primes are also within 0.05, but show a significant B|f excess of +0.03–0.04 (2–4σ)
  at u and C [65–256]. Assessment: this is the small-M_BM selection already seen by Z52D_FOURIER §0(b)."
* Mirror this in §4.1 ("All |Δ| ≤ 0.05: KILL criterion met." → add "(point criterion as pre-registered; low power)"),
  in §5, and in the proposed FRONTIER text.

### E9 (MODERATE): "class-matched" is false for the n vs c exploratory comparison
The controls c are matched to the 14 zeros' classes: they are 15 primes on each side of each Z, in classes
{1, 241, 289, 337, 361, 409, 529, 577} mod 840. The 125 near-zeros n include classes 169 (23), 121 (9) and 457 (2),
which have no controls. The memo itself says class matching shifts st|f by ≈ 0.06, so this comparison is
**unmatched**. **Fix:** "The 125 primes with 1 ≤ R ≤ 4 … versus the same c set, which is *not* matched to their
classes: all |Δ| ≤ 0.034."

### E10 (MINOR, arithmetic): Cor 3 proof, "χ_{−4}(N′) depends on p mod 32"
N′ = (p+3)/4 mod 4 is determined by p mod 16. For p ≡ 1 (24): p ≡ 1 (16) gives N′ ≡ 1 (4), and p ≡ 9 (16) gives
N′ ≡ 3 (4), which excludes χ_{−4}. **Corrected text:** "… while χ_{−4}(N′) = +1 iff p ≡ 1 (mod 16). For p ≡ 9 (16)
the second alternative is excluded, and the u = 3 slice must be a B-kill." (Consistent with data: the four zeros
≡ 9 (16), namely 409, 23929, 83449 and 1726201, all satisfy (ii) via the QR branch.)

### E11 (MINOR): "four two-way alternatives" omits the four-way C = 6 alternative
This appears in §2, the Bottom line and the proposed FRONTIER text. Cor 3 has two-way alternatives at u = 3, u = 6,
C = 2 and C = 3, plus a **four-way** one at C = 6. **Fix:** "plus four two-way alternatives and one four-way
alternative (C = 6)".

### E12 (MINOR): F4 "They satisfy Cor 3 (exactly; CERTIFIED consistency)" applied to G
The 24 𝔊*-zeros have R > 0, so Cor 3 does not apply to them, and some are ≡ 13 (24). Also, the census consistency
check verifies classifier output (no S/Q at exponent-2 slices), not the Cor 3 conditions themselves.
**Fix:** "The 14 (★)-zeros satisfy Cor 3 (CERTIFIED: checked directly by factorisation, all five items, all 14). The
G-zeros (R > 0) are outside its hypothesis." Also, "indistinguishable from class-matched controls conditional on
failure" → "within the 0.05 tolerance (with a 2–3σ B|f excess, E8)". The G-zeros were not compared in §4.1 at all.

### E13 (MINOR): test 3 wording
* The C engine computes `om += e`, i.e. Ω(c_u) (with multiplicity), not ω(c_u). Fix the text, or the code.
* s_u is the 100-smooth part *coprime to 4u* (primes dividing m are dropped), not "the 100-smooth part".
* The signature includes k, which depends on χ_{−4u}(c_u) = χ_p(c_u) by Lemma 1. Test 3 therefore conditions away
  precisely the quadratic (χ_p) layer of the private factor. Its "independence" is independence *beyond* the χ_p value
  of each c_u. Say so.
* In `private_oe.py`, a signature seen only once (n = 0 after leave-one-out) contributes factor 1.0, i.e. a certain
  failure. This inflates E slightly. It affects 9 169 of 5.67 M slice instances at MOD = 840 in the first window, and
  none of the 13 all-fail primes. Negligible, but mention it or use the pooled marginal as a fallback.

### E14 (MINOR): the "classifier agrees with brute-force R on all n ≡ 1 (4), 5 ≤ n < 1200" check has no committed script or log
I reproduced it independently (106 245 slices, both slicings, 0 mismatches), but the memo says "all commands in the
data headers", and this one is in no header. Commit a script, or cite this review.

### E15 (NIT): admissible C range
The scripts and memo use C ≤ (n+3)/4. The exact range is (4C−1)² ≤ 4Cn+1 ⟺ C ≤ (n+2)/4, so for n ≡ 1 (4) one
inadmissible C = (n+3)/4 slice per integer is kept as a failing slice. This is harmless (it can never hit; my brute
force agrees), but the text "C ≤ (n+3)/4" is not the admissible range.

---

## 3. Wording / label fixes

* **W1 (title and §2 bold first line):** "The cancellation at a zero is achieved by randomness, not by structure, at
  every scale beyond the four 'exponent-2' slices." This is unlabelled, and "every scale" overclaims. Only
  u, C ∈ [17, 256] were pre-registered, [5, 16] is exploratory, and nothing above 256 or 10⁸ was tested. The
  "structure/randomness" split is a *naming convention* (B/T/Q vs S). By the memo's own Lemma 5, every B-kill at a
  prime is also "an accident of the factorisation". **Replace with:** "**Assessment (from EVIDENCE at u, C ≤ 256,
  n ≤ 10⁸):** beyond the four exponent-2 slices, the failing slices at zeros show no slice-visible excess of
  structured kill types beyond ±0.05 (B/T/Q vs S; the labels 'structured/random' are conventions)." Title: add
  "(EVIDENCE, u, C ≤ 256, n ≤ 10⁸)".
* **W2 (Bottom line):** "So maximal cancellation at a zero, if one exists beyond 10¹⁰, is a conjunction of independent
  private failures. An inverse theorem has no structure to output" → "Assessment (extrapolating EVIDENCE ≤ 10⁸): …
  is *consistent with* a conjunction of private failures that are independent beyond their visible signatures. In the
  statistics tested here, an inverse theorem has no slice-visible structure to output." Also "the data say no" →
  "the tested statistics say no (Assessment)".
* **W3 (Lemma 6 header, §2 verdict, §5):** "STEP2 is anti-supported", "anti-supported at every scale (Lemma 6)",
  "anti-complementary … (Lemma 6, PROVED)". The lemma (PROVED) says every family needs a χ_p-non-residue prime. That
  B-kills "remove" this ingredient is a *heuristic reading* (Assessment). Type I's d is a free parameter, and nothing
  forces it to be built from the slice primes. Fix the header to "Lemma 6 (each family needs a QNR prime; PROVED,
  prior …)" and add "*Reading (Assessment):* the structure R(p) = 0 forces supplies only QR primes, so it cannot be
  the QNR input; this anti-supports, but does not refute, STEP2."
* **W4 (§2, "(STEP2) dead at bounded scale (Prop 4)"):** Scope it: "no STEP2 whose input is the slice-type vector up to
  a fixed K and whose output is a certificate determined by p mod q, q | L_K, and which fails at n = 1, can work
  (CONDITIONAL on Dickson for the slice part; unconditional for the certificate part)." Also keep the qualifier "that
  fails at n = 1" in §2's "fail every congruence-determined certificate of modulus | L_K".
* **W5 (Prop 4 attribution):** Add "the unconditional clause is the 'fixed congruence menu' dead end (FRONTIER §6) and
  Z60_LOPEZ Prop D; the 'constant × prime' Dickson mechanism is Z53_HCSHIFTS Thm W's". The C-slice extension and the
  Type I clause are the only new parts.
* **W6 (§4.2 test 2):** "no coupling at U = 16, 32" contradicts "Small-scale O/E < 1 is diffuse repulsion". At U = 8,
  764 observed vs 1071 expected is ≈ −9σ, which is joint structure, of the anti-coupling kind. → "no *excess* joint
  failure beyond the pre-registered band [1/3, 3] (O/E 0.67–1.48). At U ≤ 16, joint failure is significantly *rarer*
  than independent (O/E ≈ 0.7)." Also report that the pretentiousness 4-bin variant (Y = 61) gives O/E 1.70 / 3.94 at
  U = 32 / 64, not "almost unchanged". Note that leave-one-out marginals were not pre-registered (they change E by
  < 10⁻³ here; checked).
* **W7 (§4.2 test 3 "Reading:"):** label it "Reading (Assessment, post-hoc)". "independent in the fresh window" → "no
  detectable dependence (O/E 0.79–1.45; 11–47 events at U ≥ 32, so O/E up to ≈ 2.5 is not excluded at U = 64)".
  "carried by its zeros and R ≤ 6 primes" is near-tautological, since all-fail primes have small R; drop it or say so.
* **W8 (§4.1 "Exploratory comparisons (same statistic; run before the test was written)"):** The band census
  (bands.py) was run before checkpoint 1. The Δ/SE numbers quoted were produced by killtest.py, committed later in
  d1c45055. → "(the band census was run before the test was written; the Δ/SE values were recomputed afterwards with
  the kill-test script)".
* **W9:** "unmatched primes ≡ 1 (24) have st|f lower by about 0.06" → "by 0.04–0.07 on u-slices and 0–0.05 on
  C-slices (t also has R > 4)".
* **W10:** Lemma 5's "So no slice of a prime is killed *identically*: every kill is an accident of the factorisation" is
  an interpretation of the PROVED character identity. Mark it "(reading)".

---

## 4. Verified items (with commands)

All commands ran under `ulimit -v 4000000` with timeouts. Scratch files are in /tmp/rv62/.

1. **Kill test reproduces exactly.** `python3 scripts/z62_inverse_killtest.py data/z62/inverse/fresh_slices_U256.txt n c`
   gives the memo's table: Δ st|f −0.011 / +0.026 / −0.031 / +0.007 and Δ B|f +0.024 / +0.048 / −0.000 / −0.006, with
   identical SEs, and "KILL criterion met: True". The Z/c, n/c and K/c blocks in killtest.txt match the memo (Z max
   |Δ| 0.039; n max |Δ| 0.034; K Δ st|f +0.053…+0.086 for all 285).
2. **Pre-registration honoured.** I compared fresh.py and killtest.py with `git show 6500828e:Z62_INVERSE.md`.
   Near-zero definition, controls (3 nearest same-class mod 840 with R ≥ the median of the ±50-prime window), bands,
   families and threshold all match. **Completeness:** re-ran `scripts/z62_inverse_rsieve.c` to 10⁸
   (/tmp/rv62/R1e8.bin). The primes ≡ 1 (4) in (1.2·10⁷, 10⁸] with R ≤ 2 are exactly the 6 listed (all R = 2, all
   ≡ 1 (24)). There are no prime zeros in (1.2·10⁷, 10⁸]. The prime zeros ≤ 10⁸ are exactly the 14 listed.
3. **Independent R(n)** (my own `/tmp/rv62/rone.c`, direct (u,C) enumeration): it reproduces R for all 24 kill-test
   integers (6 × R = 2; controls 34–70), the 14 zeros (R = 0, first 8 + 712321 and the 5 ≥ 10⁶), and the 13 / 11
   all-fail lists. First window: 1134241, 1724209, 1726201, 5212561, 8813281 have R = 0, and 1021441, 2369929, 2786809,
   3292969, 3812257, 4160641, 4620841, 6416329 have R ∈ {2, 4, 6}. Fresh: R ∈ [2, 10]. Claims "five zeros + eight with
   R ≤ 6" and "R ∈ [2, 10]" confirmed.
4. **Independent slice classifier** (`/tmp/rv62/indep.py`: sympy factorisation; hits from actual divisors; H via
   element orders; B via Kronecker (−4k/ℓ); T via explicit enumeration of all real characters mod m as products of
   χ_{−4}, χ_8, (·/ℓ)). Random spot checks: 4000 codes from slices_U256.txt, 2000 from fresh_slices_U256.txt and 2000
   at small k ∈ {1,…,8,12,16} gave **0 mismatches** (all five codes represented).
5. **Brute force R vs classifier hit/no-hit** (`/tmp/rv62/bf.py`, imports the memo's classify): all n ≡ 1 (4),
   5 ≤ n < 1200, both slicings, slices up to the admissible limit + 2: 106 245 slices, **0 mismatches**.
6. **Example p = 409, u = 4:** 413 = 7·59, 59 ≡ 11 (16), ⟨7, 11⟩ = G₁₆ ∋ 15, Div = {1, 7, 11, 13}. Code 'S' in data.
   Correct.
7. **Cor 3 at the 14 zeros, directly by factorisation** (`/tmp/rv62/cor3.py`): (i)–(v) hold at all 14, and all are
   ≡ 1 (24). The odd real characters mod 4, 8, 12, 24 are {χ_{−4}}, {χ_{−4}, χ_{−8}}, {χ_{−4}, χ_{−3}} and
   {χ_{−4}, χ_{−8}, χ_{−3}, χ_{−24}}. The residues p + 2 ≡ 3 (8), p + 6 ≡ 7 (24), (p+1)/2 ≡ 1 (4),
   (p+3)/4 ≡ 1 (6) (mod 4: see E10) and 4Cp + 1 ≡ 1 (4C) are all correct. The exclusions χ_{−4}(3) = χ_{−4}(7) =
   χ_{−8}(7) = −1 are correct.
8. **Lemma 1:** proof correct, including the (−C/ℓ) = (−4Cp/ℓ)(p/ℓ) step. (c) checked on data: 0 violations of
   χ_p(u) = +1 among 84 571 B-killed u-slices at primes ≡ 1 (8). "No condition on χ_p(C)" is consistent with the data:
   8 759 of 29 301 B-killed C-slices (C ≤ 64) have χ_p(C) = −1.
9. **Lemma 2:** λ-argument and Div = H argument correct (but prior, E3). EVIDENCE: S occurs at every u and C ≤ 256
   outside {1, 2, 3, 6} in the census. The consistency block of killtest.txt (1255 integers, 0 violations) reproduces
   via check_lemma2.py logic.
10. **Prop 4:** integrality ((1+u) | L; (4C+1) | L), distinctness (4C(1+u) ≠ 4C+1), admissibility (all forms = 1 at
    t = 0), q_u ≡ 1 (4u), r_C ≡ 1 (4C), Div equal to n = 1's, no divisor ≡ −1 (1 + u < 4u − 1; 4C − 1 ∤ 4C + 1),
    B-kill ((−u/ℓ) = 1 for ℓ | 1+u; (−C/ℓ) = 1 for ℓ | 4C+1), Type I clause (χ_{−4d}(f) = +1 vs χ_{−4d}(−1) = −1): all
    correct. p ≡ 1 (840) ⟹ p ∈ 𝔐 is correct. The Bateman–Horn scale estimate K ≈ log p/(2 log log p) is fine as
    Assessment.
11. **Lemma 6:** χ_{−4d}(−p) = −(−d/p) = −(d/p) for p ≡ 1 (4) is correct, and p ∤ d is automatic. The slice part is
    correct (prior, E5).
12. **Test 2:** regenerated `/tmp/z62_joint 1000000 12000000 64` (88 565 primes) and `12000000 100000000 64` (621 484
    primes). `z62_inverse_joint_oe2.py … 840 11,13` reproduces 0.90 / 0.71 / 0.73 / 1.48 / 3.19 (13 vs 4.08) and the
    fresh 0.91 / 0.75 / 0.67 / 0.72 / 1.65 (11 vs 6.65). The all-fail lists match the file. joint.c hit bits agree with
    the Python classifier on all 609 census primes in range (0 mismatches). Leave-one-out and plain marginals give the
    same E to 3 decimals (no bug: the difference is second order).
13. **Test 3** (first window): `/tmp/rv62/priv 1000000 12000000 64 100` + `z62_inverse_private_oe.py [840]` reproduce
    0.96 / 1.09 / 1.85 / 2.26 / 2.92 and 0.96 / 1.10 / 1.82 / 2.31 / 3.02. The Jacobi routine `jac` is a correct binary
    Jacobi for odd positive moduli, and all calls pass odd positive moduli coprime to u. The fresh window was not
    re-run (memory of the Python aggregator).
14. **F1:** all 8 squares in the census have only B codes. The argument (−u ≡ m² mod ℓ, ℓ ∤ m) is correct.
    **F2:** E's u-slices hit at u ≤ 4 at rate 0.35. All 74 C-hits are at odd C. R ≥ 12 is from Z60_LOPEZ F2 (not
    recomputed). **F3:** 285 K, 265 divisible by 3, 5 or 7, all R = 0, none a square (checked against my sieve).
    **F4:** see E12.
15. **Census sizes:** 1231 + 24 = 1255. There are 363 controls for Z. 14 Z are in the census (the memo's "14 zeros
    vs 363 controls" is correct; the checkpoint's "10 of the 14 (≥ 2·10⁴)" applied only to the band table with minN).

---

## 5. Required fixes (summary)

1. Lemma 5: χ_{s*} with s* < 0 gives an *even* ψ. Replace it with the even character χ^{(s)} (χ_s or χ_{4s}), so that
   ψ(ℓ) = ((n/s)/ℓ). Fix F3's "(±m/ℓ)" accordingly (E1).
2. Cor 3 header: drop "p + 4" (not forced; p = 409). Only 4p + 1 ∈ S is Z54's (E2).
3. Credit Z54_HCKILL Lemma 1.2(a),(c) for Lemma 2, and justify "every other u" (E3).
4. Rewrite §1 "Why not closed" to credit Z52D_FOURIER / rank_O's B/T/Q/S-type split and its small-BM-selection finding
   (E4). Credit Lemma 6 to Z59_MSPF 1.5 / Z57_BFII 2.1 / Z60_LOPEZ (E5), and Prop 4's unconditional clause to
   Z60_LOPEZ Prop D / FRONTIER §6 (W5).
5. §0: F3 *was* changed since checkpoint 1; say so (E6).
6. F3 numbers are for all 285 K, not "237 ≥ 2·10⁴" (E7).
7. Kill test: state low power explicitly (SE up to 0.049). Report the significant B|f excess at u **and** C [65–256].
   Mark the small-M_BM attribution as Assessment (E8).
8. The n vs c comparison is not class-matched (E9).
9. Cor 3 proof: "p mod 32" → p mod 16, and p ≡ 9 (16) forces B at u = 3 (E10). "four two-way alternatives" → "+ one
   four-way (C = 6)" (E11).
10. F4: Cor 3 does not apply to G (E12). Test 3: Ω not ω, s_u coprime to 4u, k conditions on χ_p(c_u) (E13).
    Commit the n < 1200 brute-force check (E14).
11. Labels: the "randomness, not structure, at every scale" headline, the Bottom-line extrapolation beyond 10¹⁰, and
    "STEP2 anti-supported" must be Assessment and scoped (W1–W3). Test 2's "no coupling" → "no excess coupling;
    significant repulsion at U ≤ 16" (W6). Test 3 reading → Assessment, post-hoc (W7).
