# Hostile cross-lab review, Round 3 (final): `notes/z80/PROTH_CORE.md` §0 and §§8–10, commit 3e395d6af

Reviewer: Claude Opus (cross-lab hostile reviewer), subagent session. Scope: every change in `git log b577c9e7f..`
(one commit, 3e395d6af). I did not edit anything outside `data/z80/xreview/` and committed nothing.

**Verdict: ACCEPT WITH MINOR REVISIONS.** Theorem 13 (ES at (4^m−1)2^s+1 for every 22≤m≤30 and every s≥0) replays
independently: my rule logic, coverage algorithm, X-row arithmetic and brute-force box all differ from the repository's.
The §8 sign certificates and the 7/23 rational targets replay. The §8 Proposition and the §10 Proposition,
noncontainment and strengthening are correct as scoped. One novelty claim is false: the "new m=265 core" is already an
instance of z78 Theorem 8. Several wording problems are listed below. Nothing claims ES in general, and no CLAIMED proof
is involved.

## 1. Independent replays (all exit 0; files in this directory)

| file | what it checks | result |
|---|---|---|
| `opus_r3_cover.py` → `opus_r3_cover.out` | Theorem 13: all 9 covers, 2,653 rows | all pass |
| `opus_r3_controls.py` → `opus_r3_controls.out` | negative controls for my coverage routine | gaps detected where expected |
| `opus_r3_groups.py` → `opus_r3_groups.out` | §§8, 10 | all pass (≈47 s) |

All runs used `ulimit -v 6000000`, `timeout ≤1800` and `uv run --offline --no-project python -B`, with pure stdlib and
no imports from the repository scripts. Peak memory was small: the largest object is a bytearray of at most 4096
children. I never built a period-sized array, and I never built a huge integer for any mask exponent.

### Method of `opus_r3_cover.py`

* **Fixed rows (M/D/W/II/K).** For each row I reduce n modulo the row's own test modulus M.
  * Periodicity is checked in the *exact* form needed: the dyadic part of M is at most 2^64, and 2^P≡1 modulo
    Mo/gcd(Mo,k), where Mo is the odd part of M. My first draft demanded 2^P≡1 mod Mo, which is too strong because k
    shares factors with 840, and it failed correctly. The repository's k·2^{s₀}(2^P−1)≡0 test is the correct one.
  * Each rule is then checked from first principles. M uses Mordell's six square classes mod 840, typed by hand. D uses
    my own direct triple for q. II and K use the divisibility conditions behind their explicit triples.
  * W uses the **actual Jacobi symbol** (A/n) on a positive representative in the class mod 8A, n≡1 mod 8, plus a
    check that v mod 4 is fixed on the class.
* **X rows.** I used different arithmetic from the repository.
  * A mod H is computed as c·∏_i B_i^{E_i}, where B_i=1+2^i and E_i aggregates the Möbius exponents over
    i≡a·b mod h. The repository instead takes Möbius products at 2^{a+4h} mod 16H.
  * A≡c mod 16 is checked separately, since every Φ_{2d}(0)=1 and 16|X. Together these give A≡7u−1 mod 16H.
  * I also check that c|k, that the masks consist of distinct divisors of an odd e, that 4e|P and j=0, and that the
    sources are exactly the units mod h.
* **Coverage.** I used a chunked recursive bytearray sieve. Each node a mod b sieves at most 4096 children b·c at once,
  where c is built from primes of L/b. It recurses only on uncovered children, keeping only compatible rows, and fails
  on any uncovered leaf. This differs from the repository's one-prime-at-a-time tree with a 55440 base sieve.
  * Negative controls: r2/cover-11 gives exactly the gap 0 mod P₉. Deleting the X rows gives a gap at 0 for every m.
    Random single-row deletions give detected gaps in 7–22 of 25 cases per m.
* **Brute box 513≤s≤1600** (the repository uses 64≤s≤512). For every s and **every** fixed row whose class contains s,
  I applied the rule to the actual integer n: 31,037 firings.
  * 25,055 of these firings produced explicit ES triples verified by 4xyz=n(xy+yz+zx).
  * For W rows I used all five explicit Dedekind slices: the D-triple, its u↔v reversal, the 4|t triple, and the
    DEDEKIND_ES 4|u and 4|v triples. Every W firing had (A/n)=−1 and at least one slice.
  * The remaining 5,982 firings were M rows, which rely on Mordell and scaling and produce no explicit triple.
  * Every s in the box was hit by some fixed row.
* **Other X-row checks.**
  * The s<64 triples of `z78/proth/small.json` for m=22..30 were re-verified (576 triples).
  * The X core lemma was checked on **actual integers** at small analogues: m=3..8, e|45, s=4e·(h-part and other
    multipliers), with exact Φ_{2d}(2^r) by division and h-part stripping. All 30 hits had A|n+u, t≡v≡7 mod 8 and a
    valid triple. X rows of the real covers cannot be brute-forced: s≥4e≈1.4·10^8 bits.

**Result.**

|m|period|rows|X rows (P, e)|
|---|---:|---:|---|
|22|8014397185594800|245|(137837700, 34459425), (872972100, 218243025)|
|23|351050016517200|316|(446185740, 111546435)|
|24|3859455600|170|(137837700, 34459425)|
|25|10475665200|219|(137837700, 34459425)|
|26|11480082455041200|476|(137837700, 34459425)|
|27|551350800|91|(137837700, 34459425)|
|28|551350800|111|(137837700, 34459425)|
|29|618064246800|362|(137837700, 34459425)|
|30|20044007361172594800|663|(137837700, 34459425)|

Periods and row counts agree with `r3/cover-replay.txt`. The m=30 period exceeds 2^64. The repository replay
`scripts/z80_proth_check.py` also runs green, in 3.9 s and 35 MB, and so does `scripts/z80_proth_final.py`.

**Finding (form, m=22).** The first X row (e=34459425) is **redundant**: the fixed rows plus the second X row alone
cover everything. I confirmed this with both my routine and the repository's `coverage`. Without the second row the
gap is 5342931457063200 mod L, which is 0 mod 872972100 and 91891800 mod 137837700. The note says "a second mask of
different degree covers the last gap of the first". That is true but misleading. Say instead that the e=218243025 mask
alone suffices with the fixed rows, and the e=34459425 row is superfluous. Also record the mask degree e (and the two
X rows at m=22) in §9, as the Theorem 3 table does. At present §9 points only to a file of periods and row counts.

### `opus_r3_groups.py`
1. **Sign certificates.**
   * `r3/sign-343.json` and `r3/sign-529.json` have 5 and 6 unit-index ratios (B_a/3) with positive exponents. Their
     product is −1 on the **whole** 2^h−1. c=1 with T0=∅ is dyadically legal, since 14H−1≡1 mod 16.
   * ord_h(2) is 147 and 253 respectively: odd, and of index 2. So −1∉⟨2 mod h⟩, and the doubling criterion of
     Theorem 12 cannot replace these certificates.
   * Using D_{2^i}=∏_{l<i}B_{2^l} as explicit B-products, −2^{−Σa}∏_{a∈Q}D_a² equals 7 and 23 on Φ_h(2). Multiplying
     by the certified sign gives **+7 and +23** in proj R₁. Both statements replay.
2. **Theorem 12 criterion.**
   * −1∈⟨2 mod h⟩ holds iff the v₂(ord_p 2) are equal and nonzero over p|h. Checked for all odd h≤5000 with 3∤h.
   * v₂ is constant along prime-power lifts.
   * The explicit word 2∏_{i<b}B_{2^i}≡−1 mod 2^h−1 holds at all 97 qualifying h≤601, as do B₃/B₁=3=B₁ and
     B₁/B₋₁=2.
   * All 9,005 primes ≡3,5 mod 8 below 2·10^5 have even order, with v₂=2 on the 5 mod 8 class.
3. **Characteristic-zero Proposition.** I took 17 cases h=p, p² with p≥5, even ord_p(2)<p−1 and h≤2000, using
   complex-log norms over G=⟨σ₂⟩. In every case N(1+ζ^a)=1 for all units a. For a∉⟨2 mod p⟩, N((1−ζ^a)/(1−ζ)) is
   positive real and ≠1, and a^o≢1 mod p.
4. **§10 divisor classes,** on a new box: 1≤m≤40, 0≤s≤400, all primes q≤1500. The classes are exact (the predicted
   class holds iff q|n), with at most one class per q. I verified 10,551 scaled triples for q≡3 mod 4.
5. **Noncontainment key lemma (z78 Prop 5), exhaustive on a small analogue.** For 2≤m≤15 and every odd B<h−1, no c|k
   and **no divisor** F|2^B+1 has cF≡−1 mod 2^h−1. That is 105 (m,B) pairs, and the set of divisors is a superset of
   all mask values.
6. **Strengthening count.** For every odd d≤30000 and five values of B (including the odd part of P₉), a b=2i+1 with
   i≤2·4^{ω(d)} and gcd(Bb−1,d)=1 exists. The largest i needed was 4.

## 2. Substance, claim by claim

**§0 / Theorem 13.** The proof logic is sound.
* At s≡0 mod 4e, stripping the h-part of s/e leaves r≡0 mod 4 and r coprime to h, and s/(re) is odd. So
  X^e+1 | 2^s+1, c·∏Φ | k(2^s+1)=n+u, and the congruence A≡7u−1 mod 16H gives t≡v≡7 mod 8 and the triple
  (ADn, uD, AuD).
* F1: s=2m+2≤62<64, so the square exponent falls in the direct-triple range.
* No ES(q) verification threshold is used.

PROVED (computer-assisted, relative to Mordell, DEDEKIND Thm 4.5 / Cor 1.2, THIN_CYCLO §1 and z77 §2). This is
confirmed.

**Theorem 12.** The mathematics is correct.
* Simultaneous half-orders are compatible iff the 2-valuations are equal and ≥1.
* The supplementary law gives even order at p≡3,5 mod 8.
* The prime-density quantifier ("at least half the primes", in relative prime density, with no integer density) is
  correct. It is conservative: the density of primes with even ord_p(2) is 17/24.

*Challenge (novelty and form).* This is z78 Theorem 1 (hypothesis 2^b≡−1 mod h, 3∤h) combined with the classical
characterization of −1∈⟨2 mod h⟩. The core part is already Lean-formalized as `ESProthCore.core_of_doubling`. Calling
it "Theorem 12" overstates it. Relabel it as a Corollary or Remark of z78 Thm 1, and mention `core_of_doubling`.
"…consists of all h for which…" reads as an iff for the core property. Write "the following set works: all h with…".

**Proposition (characteristic-zero obstruction).** Correct.
* The telescoping G-norm of 1+ζ^a is 1.
* u≡a mod (1−ζ), and a^o≢1 since o/ord_p(2) is a p-power and a∉⟨2⟩.
* −1∈⟨2 mod p^j⟩ (even order in a cyclic group), so the norm is ∏|σu|²>0. A positive real ≠1 has infinite order, so no
  power of u lies in ⟨doubling ratios⟩·torsion.

The non-descent remark is right: σ₂ does not preserve the kernel of ζ↦2. The parenthesis "(ζ−2 maps to 2 modulo that
kernel)" is garbled; write "σ₂(ζ−2)=ζ²−2↦2≠0 in ℤ/Φ_h(2)". Triage BARRIER-SCOPED (method-level) is appropriate.

**§8 core corollary.** The certificates replay (§1 above). **False novelty claim: "For h=529 this gives a new m=265
core."**
* h+1=530 has the divisors a=5, 10, 53, 106 ≥4, and −a∈⟨2 mod 529⟩ for all of them. (⟨2⟩ is the index-2 subgroup,
  i.e. the squares, and (−5/23)=(−1/23)(5/23)=(−1)(−1)=1.)
* So z78 Theorem 8 (§7, "a divisor of the multiplier pays for a negative doubling orbit") already gives the m=265
  core and density-one exponents.
* The 529 certificate is a valid *alternative*, with c=1 instead of c=k/31, and it is the first explicit witness of
  −1∈R₁ there. That gives the +23 target at the top layer, which is genuine DATA, but it is not a new core.
* For 343, z78 Thm 8 does not apply (no admissible a), but m=172 is already inside 2≤m≤200. So the 343 certificate
  adds only the +7 datum.

Delete "new". In §0 Scope and in the STATUS delta, either drop "m=265" or annotate it "(also z78 Thm 8, a=5)". This is
a priority error, not a validity error.

**§10 Proposition (prime-divisor classes).**
* The test is exact; my box confirms it. The q≡3 mod 4 triple is right.
* Salez 10^17 is correctly attributed, and Mihnea–Bogdan 10^18 is correctly flagged as a reported, unrefereed
  preprint. I could not check the arXiv record offline.
* "Membership in the doubling orbit is not an ES(q) proof" is correctly stated.

**Noncontainment.** Correct. It is z78 Proposition 5 verbatim with B the odd part of P₉, attributed as "PROVED rel.
z78 §5".
* F<H because B<h−1 (2^B+1<H).
* cF≡−1 forces F+k/c≡0 mod 2H, hence k/c>H and c=1, hence F≡2H−1, which is impossible.
* Scope: it is about the *unshifted* stripped domain, and other word types are not excluded. Stated correctly.

**Strengthening (bounded vs unbounded divisors).** Correct.
* With s=Bb·2^v and v≡0 mod lcm(ord_d 2, ord_h 2) (and v large):
  * P₉|s, so the fixed off-zero rows miss;
  * s≡Bb mod d, so the gcd test fails;
  * ord_q(2)|s, so n≡4^m≢0 mod every tested q;
  * Bb<h−1, so the Prop 5 argument applies.
* The inclusion–exclusion bound Y·2^{−ω}−2^{ω} with Y=2·4^{ω} gives at least one b, and b=d^{o(1)}.
* The scope is correctly limited to a **fixed bounded** set of tested q, with a threshold depending on the cutoff. It is
  explicitly *not* a no-go for the unbounded q≡3 mod 4 union, nor an ES failure. I find no quantifier slip.

**"Exact remaining problem" (Assessment).** This is fine. One precision point: the density-zero complement on P₉|s
holds for the **z79-selected** m (§6 density construction), whereas the ES-off-P₉ statement holds for **all** m≡11
mod τ. The proposed STATUS delta, "On the §6 infinite subfamily ES holds off 0 mod 497943285840 with relative
density-zero possible exceptions there", blurs the two. Write instead: "for all m≡11 mod τ, ES off P₉|s; for the
z79/§6-selected infinite subset of these, good words on relative density one of P₉|s".

## 3. Form, process and Lean
* **Lean.** `final-build.log` shows a successful cgroup build: `ProthQuadratic.quadratic_transfer` and
  `ProthFiveTower.core_five_tower`, axioms propext/Classical.choice/Quot.sound, with no `sorry` and no `native_decide`
  visible. Everything was replayed from cache. The §0 Lean scope statement is accurate. Nothing in §§8–10, and no
  all-s cover for m≥4, is formalized. The "Lean all s only for m=1,2,3" statement matches STATUS (Proth3, Proth15,
  proth63).
* **Checker change.** `z80_proth_check.py` now defines its own √n `divs` and recursive `mob`, replacing the O(n) z78
  `divs`, which is needed for e≈2·10^8. The new definitions are correct. The docstring still says "reuse the z78
  arithmetic helpers", which is now only partly true.
* **Reproducibility of discovery.**
  * `scripts/z80_proth_birthday.py` writes `data/z80/proth/mask-*.json`. Those files, `r3/mask-22.json` and the
    `r3-*.log`/`m2?.log` logs are **untracked**.
  * The README states that scratch files are not committed and that the proof checkers do not read them. True:
    `cover-*.json` embed all masks. Acceptable, but the untracked files should be cleaned or ignored.
  * The birthday script's `print('too few'…)` and `print('miss'…)` paths return silently, without a nonzero exit.
    This is discovery-only, so harmless.
* **Replay commands.** The §3 commands with `timeout 300` still suffice. §10's `z80_proth_final.py` command was
  verified (0.9 s).
* **Triage.** "RECORD (all-s and core ranges…)": the all-s range m≤30 is a genuine internal record. The core-range
  part is not, because 265 is a predecessor-class instance (above). The §0 Review line ("§§8–10 cross-review owed") is
  honest. This document discharges that debt for §§8–10 and §0, subject to the revisions below.
* **Cap/pipeline.** The lane edited only its note and data. STATUS, WAVES and FRONTIER were not touched, as
  required. The proposed STATUS delta is 6 lines.

## 4. Required / suggested revisions
1. **(Required, priority)** §8: delete "new" for the m=265 core and cite z78 Thm 8 (a=5). Adjust §0 Scope and the
   STATUS delta accordingly.
2. **(Required, precision)** STATUS delta: separate "all m≡11 mod τ: ES off P₉|s" from "selected subset: density-one
   good words on P₉|s".
3. (Suggested) §9: give the mask degrees, including e=218243025 at m=22 and e=111546435 at m=23. State that the
   e=34459425 row at m=22 is redundant, or drop it.
4. (Suggested) Theorem 12 → Corollary of z78 Thm 1; mention `core_of_doubling`; replace "consists of".
5. (Suggested) Fix the "ζ−2 maps to 2" parenthesis, and the outdated checker docstring.

With items 1–2 applied, §§8–10 and the m≤30 all-s extension meet the cross-lab review bar for promotion. A second
independent review is still owed if the m≤30 all-s range is to be treated as an improvement of a *published* record.
No published record is known to me.

— Signed: Claude Opus, cross-lab hostile reviewer (Round 3, final), reviewing commit 3e395d6af against b577c9e7f.
