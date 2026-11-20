<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="73c82b8e2">
A separate reviewer subagent was asked to review the changes in `git log 73c82b8e2..`. Its request and review follow.

Request: review changes since 73c82b8e2 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Fresh independent Claude Opus hostile review of round 2, commit range 73c82b8e2..HEAD, §§6–7 of notes/z78/WILD_ES.md. State provider/auth/quota errors. Attack every PROVED label/conditional, chart exhaustiveness & actual height incl Type I3 quadratic twists, exact same primes, both mean estimates (PV for imprimitive characters, interpolation under harmonic measure, moments/NT, O13 pair bound/energy/transfer, II2 O14 barrier), the GRH bulk cancellation, quantitative BH pair, and the uniform good-marked tame-cover proof (purity/local rings/twists). Re-run key computations plus independent checks of all 192 full minima and the C mean numerics if feasible. Use uv run --offline --no-project, ulimit -v ≤6000000, timeout≤1800, ≤2 compute processes; no repo edits. Check for disguised B2, overclaim about polylog, Haar versus prime means, labels. If any major gap say so, with precise fixes. Full response to be archived.

Commit log:
commit ffe650cd2ab5ebd1887d6d7025216cf9444aa629
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:47:13 2026 +0100

    z78 wild R2: get paired hard primes under explicit uniform Hardy–Littlewood

 notes/z78/WILD_ES.md | 12 +++++++++++-
 1 file changed, 11 insertions(+), 1 deletion(-)

commit aa97fca228d9750303454510b2cf5cf631790394
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:45:41 2026 +0100

    z78 wild R2: prove uniform tame-cusp blindness on a single adele

 notes/z78/WILD_ES.md | 14 ++++++++++++++
 1 file changed, 14 insertions(+)

commit eab6f025aab4a29e97c8368ac36fd28f8c168bdb
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:42:29 2026 +0100

    z78 wild R2: prove primorial thinning cancels in bulk first moments

 data/z78/wild_budget.txt  | 31 +++++++++++++++++++++++++++++++
 notes/z78/WILD_ES.md      | 20 ++++++++++++++++++++
 scripts/z78_wild_budget.c | 34 ++++++++++++++++++++++++++++++++++
 3 files changed, 85 insertions(+)

commit 145c70f88faf6ab2f0061eeb3f754d2cece0f0b1
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:39:02 2026 +0100

    z78 wild R2: attain full seven-chart 1/4 via moment interpolation and certify 192 exact minima

 data/z78/wild_full.csv     | 193 +++++++++++++++++++++++++++++++++++++++++++++
 data/z78/wild_full_log.txt |   6 ++
 notes/z78/WILD_ES.md       |  16 ++++
 scripts/z78_wild_full.py   | 104 ++++++++++++++++++++++++
 4 files changed, 319 insertions(+)

commit c0ebe6e6037090304de049409781e2874f035197
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:30:49 2026 +0100

    z78 wild R2: simultaneous seven-chart superpolylog gap via randomized graded square digits

 notes/z78/WILD_ES.md | 25 +++++++++++++++++++++++++
 1 file changed, 25 insertions(+)

commit 31956f8d0ad5adb6b8bad9d044ef3d4e35bd61bd
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 21:28:11 2026 +0100

    z78 wild R2: fix seven-chart exhaustive full-ES height and square-safe atoms

 notes/z78/WILD_ES.md | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)

Review:
**Verdict: no fatal or major mathematical gap found in §6.1–6.3 or §7 within their stated scopes, and all the computations replay.** The problems are mostly labels, credit and triage. There is one moderate gap in §6.4 G′ and one minor interface gap in G. Several framings should be fixed before export.

Reviewer: fresh Claude (Opus-class), same lab as the author, so this does not count as the cross-lab review the STATUS gate requires. No provider, auth or quota errors. No repo edits; all scratch work was in `/tmp/rv`, with `ulimit -v` ≤ 3 GB and at most 2 processes.

## Computations re-run
- **`z78_wild_full.py` replay:** EXIT 0. The six min/median/max lines match the note, and the CSV assert passed.
- **Independent checker (my own code, written separately from the repo scripts):** it enumerates the parameters of all seven rows directly (II2 over (a,c,d); II1/I4 using the unique e < 4ab; I1 over the divisors of 4a²d+1; I2/I3/II3 over triples). On all 192 primes it finds 0 mismatches. Every minimum is unique: II2 190, I1 1, I4 1, with no ties. All 192 p pass Miller–Rabin. 75/192 equal the round-1 star minimum, and the full minimum is never larger.
- **Chart exhaustiveness, brute force:** for all 193 primes 5 ≤ p < 1200 I enumerated every solution of 4/p = 1/x+1/y+1/z, recovered every (a,b,c,d,e) parametrisation in both orders, and took the minimum of the row periods (including I3's 4cdf). This equals the `hit()` scanner minimum in every case. Every solution was parametrised.
- **Square-safety:** for every period m ≤ 2500, none of the 32,737 `ref_atoms` classes (I3 square-root classes split, as in the note) contains a unit square.
- **Budget C:** recompiled; the output is byte-identical to `data/z78/wild_budget.txt`. An independent Python recomputation at T = 5·10⁴ for B = 7, 43, 313 matches all μ₀, μ_keep and μ_Q values to 6 decimals.

## Substance, section by section
**§6 table and height.** The table is exactly ET Prop 1.9 (checked against the PDF), including I2's −c/a mod f and I3's n² ≡ −4c²d mod f. The parameter reconstructions give b > 0 with no size condition. The coprimalities follow at p > m. Square-safety rests on EXPONENT_COVERING Thm 1.2 (Mordell/Schinzel via ET) and is numerically confirmed.

**§6.1 (Theorem F).** I checked:
- the Pólya–Vinogradov argument for imprimitive characters: tail D^{−1/6+o(1)}, mean square log Y/Y + D^{−1/4}, even jk give zero;
- the χ_d Euler-product comparison;
- ET Thm 7.1's uniformity (coefficients ≤ 8X, ρ(p^j) ≤ 3);
- the II2 Hölder exponents, where 1/r + 1/s = 1 and the ±5 powers balance;
- the overall L⁶ budget.

All sound. F is superseded by G.

**§6.2 (Theorem G).** The harmonic-measure interpolation is valid: Hölder with exponents 1/(1−t), 2/t, 2/t gives an exponent of 3(1−t) + C₁t/2 + t/2 + o(1), and Σ V^s/m ≤ L^{1+o(1)} holds. The fixed-moment bound (Landreau blocks with ρ ≤ 2) is fine. O13's Lemma 3.2 bookkeeping is generic in single-residue atoms, with first-step drift ≤ 2. The rough-family identity for the reverse Haar bound is correct. The Method ceiling is a valid implication, since B ≤ F₇ ≤ F_II2.

**§6.3 (Theorem H).** The local identities check out by hand. At each small prime the conditional and unconditional expectations share the value 1 + t_q/(q−1), uniformly in r. μ_keep loses a factor 1 − 1/q + O(1/q²) per prime. The GRH error is X^{σ+θ−1/2+o(1)}. It is correct but elementary, and its regime (B ≤ log X/24) is far from any computable range. At B = 1259 the data give μ_Q/μ₀ ≈ 0.41, as the note admits.

**§6.4 (G′).** The UHL₂ main term 𝔖/A(k) is correctly derived. The pair-square digit count is at least (ℓ−5)/4, and the drift is at most 6 ≤ 8.

**§7 (Theorem J).** I checked:
- Galois descent of the disc coordinate: σ̃(s) = ζs because μ_e lies in a domain, so w is invariant;
- normalisation preserving the smooth model;
- the residue → purity → Br(ℤ₅) = 0 chain, including the codimension-2 compatibility and H¹(𝔸¹_{𝔽₅}, ℤ/M) = H¹(𝔽₅, ℤ/M) for 5 ∤ M;
- that w′ is an M-th power because M | E/e.

All sound.

## Issues and fixes
1. **MODERATE, §6.4 G′.** The text asserts, without writing them out, that the H4 energy lemma, the junta (O11 Lemma 1.1/Cor 1.2) and the BRW minorant carry over to pair-unit first digits, i.e. digits from the set of residues where both n and n+840 are squares, not uniform units. These are exactly the kind of interface checks that O13 §5 needed review rounds R48a–d to get right. **Fix:** write out the I1/I2 analogues for the pair measure, or relabel G′ as "CONDITIONAL on UHL₂ and unwritten pair-measure interface checks".
2. **MINOR, G.** O13's atoms have odd M, so 2 was never a coordinate there. In the seven-row setting 2 is a live coordinate (m = 4h, deep powers of 2). It is fine as far as I can see: real 2-power conductors divide 8 | Q, and higher 2-digits are uniform. **Fix:** add the sentence saying so.
3. **Label (§0, round 2).** The κ<1/4 claim omits its dependencies: O13 §§3,5 (themselves resting on NT and OMEGA10 Thm 3.4), Gallagher (G) or GRH, and for the ceiling O14 Thm 4.5 (effective Page, fundamental lemma). **Fix:** list them, and state that the ordinary-PNT route gives κ<1/8.
4. **STATUS delta.** As drafted, "κ<1/4" without a qualifier would misstate the label. **Fix:** write "κ<1/8 (ordinary PNT), κ<1/4 with Gallagher or GRH, rel. the internal energy lemma and the O13 lemmas", mirroring the existing row. Better still, rewrite the "Witness sizes are not polylog" row as one row, because it currently omits O13's 1/4.
5. **Credit and triage.** For II2 alone, κ = 1/4 is already O13 Thm 5.1. G is new in three ways: the six other charts, the exact prescribed minimum, and the QR depth. It also loses an ε (L^{4+ε} versus O13's L⁴ log L). **Fix:** say this explicitly, and state that G supersedes round-1 D. "HEADLINE" overclaims: G is a B1-quantitative barrier, so RECORD/BARRIER-BROAD. H is NULL/BARRIER-SCOPED. G′ is CONDITIONAL and should not go in STATUS.
6. **Wording errors.**
   - In G's reverse Haar bound, "d the squarefree kernel of D" must be "squarefree part". The kernel (radical) fails at D = q².
   - In H, "in each chart" means the two charts (star and normalised II2), not seven.
   - "Prime-Haar units" should be "Haar units".
   - In J, "fixed rational u-line" should be "the t-line {u = u₀}".
7. **J scope (an improvement, not a gap).** By Grothendieck/Beckmann tame specialisation, every restricted cover with geometric monodromy order prime to 5 has potentially good marked reduction, because 0, −1, ∞ stay distinct mod 5. J therefore covers all torsors of that kind. Say so with the citation rather than keeping it as a hypothesis.
8. **Checks for disguised B2, polylog overclaim, Haar vs prime means.** No disguised B2 anywhere. No polylog overclaim: the disclaimers about single coordinates and "not all algorithms" are present. Haar and prime means are kept apart correctly: H's prime mean is under GRH, and G′'s 1/3 heuristic is labelled Assessment.
</code-review>
