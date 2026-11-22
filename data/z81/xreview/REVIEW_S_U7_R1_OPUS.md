<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-s-u7 (notes/z81/S_U7_FORCE.md). The author is a GPT-6.2 Astra lane. Verify every theorem, move-graph/class-group/Rédei calculation, computational certificate (especially any Conj. B/C counterexample or census), falsifier screen (F1–F4 + 2521/3361/113035442521), and scope claim. Reject disguised B2 re-encoding. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit b9f4b3a9edd3986306f3cb7a0dc0457daa3a32d6
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 14:59:34 2026 +0100

    z81: refute the U7 three-exception clause and bound joint ring-class visibility

 data/z81/s_u7/c135-all.txt   |  27 +++++++++++
 data/z81/s_u7/c135-all2.txt  |  85 +++++++++++++++++++++++++++++++++++
 data/z81/s_u7/c135-ap.txt    |   5 +++
 data/z81/s_u7/c135-high.txt  |   1 +
 data/z81/s_u7/class.txt      |  40 +++++++++++++++++
 data/z81/s_u7/controls.txt   |  45 +++++++++++++++++++
 data/z81/s_u7/counter.txt    |  34 ++++++++++++++
 data/z81/s_u7/counter2.txt   |  37 +++++++++++++++
 data/z81/s_u7/walk.txt       |  20 +++++++++
 notes/z81/S_U7_FORCE.md      | 105 +++++++++++++++++++++++++++++++++++++++++++
 scripts/z81_su7_audit.c      |  19 ++++++++
 scripts/z81_su7_class.py     |  61 +++++++++++++++++++++++++
 scripts/z81_su7_classcheck.c |  25 +++++++++++
 scripts/z81_su7_controls.py  |  40 +++++++++++++++++
 scripts/z81_su7_csearch.c    |  63 ++++++++++++++++++++++++++
 scripts/z81_su7_walk.py      |  53 ++++++++++++++++++++++
 16 files changed, 660 insertions(+)

Review:
**Verdict: accept with fixes.** The main result holds up. The three-exception clause of Conjecture C is refuted by 2,238,327,841 and 4,367,159,449, and I confirmed this with my own engine. The rest of the mathematics is correct. The fixes are a process violation, triage gaps and readability.

## What I replayed (about 9 minutes in total)

| Item | Result |
|---|---|
| `audit` run on both counterexamples | 32 and 35 witnesses; 9 and 15 of them with ω≤2; no F₁∪F₃∪F₅ witness; six-cofactor hits 25·599, 9·13089647 and 7·17, 7·933953, 7·27125473 |
| **My own engine** (sympy; enumerates words p=rtz−r−z by least letter, both orientations; shares no code with the lane's scripts) | Same witness sets, f for f, at both primes. No witness is c·q^e with c∈{1,3,5}, so the refutation holds under both the F_c and the κ(f) conventions of `Z68_U7F` §9.1 |
| All 110 `csearch` blocks, (10⁹, 1.11·10¹¹] | **Byte-identical** to `c135-all{,2}.txt`. Sums: 1,552,708 unmarked inputs, 4,984 of them prime, exactly 2 with no three-cofactor witness (`NO135`) |
| `walk.py`, `controls.py`, `class.py` (cypari2) | Byte-identical to the data files |
| 2521 | My enumerator gives the same 7 interior words and a unique U₇ witness f=87. No endpoint product is divisible by 11, so the v₁₁ separation is correct |
| Certificates for 3153419441929, 6955940568721, 1590284203561; the factorisations 20p+1 and 68p+1; the s₁, s₂ congruences; n=305761; p≡131 (170) in the trap family | All check |

**Why the census is sound.** I read the code. The sieve marks an input only when f∈F₁₃₅ (f≤5·10⁵) and r|f+1, r≤f−1, n≡−r (mod f). That is exactly a witness, and I checked the modular-inverse indexing. So no prime that lacks a witness can be removed. Any spurious `NO135` from the word search would surface as an extra exception, and the only two are confirmed by direct audit. Miller–Rabin with 12 bases up to 37 is deterministic in this range, and the overflow assertions hold.

## Substance

1. **Refutation (§1): CERTIFIED, correct and new.** Neither number appears anywhere on main. The scope is right: the eventual three-cofactor form, Conjecture B and the six-cofactor clause are not refuted. One thing the note should say: the heuristic support in `Z68_U7F` §9.1 (exceptions flat at 3 from 10⁷ to 10⁹, fitted exponent ≈1.08>1) is now undercut, because two new exceptions appear just above 10⁹.
2. **Theorem A (§2): correct but trivial.** 2n+1=(2m−1)(2m+1), and any divisor of 2n+1 that is 7 mod 8 is a middle-2 witness. Reducing it to ω≤2 is just (ℤ/8)× = C₂×C₂. It is a thin quadratic family, which the note itself admits (screens 15–16). It should be triaged NULL/METHOD-CX, not "Theorem". The odd-square obstruction for 2s²+1 is correct.
3. **§3 walks: correct, DATA.** The trap-family escape is pure algebra and checks: χ(34)=χ(17)=−1, T=(p+39)/170, and the word (34,T,5). It is closely tied to z80's own word (5,7,(p+5)/34): 5T−1=(p+5)/34. The note admits "not previously unknown solubility". No disguised B2: no depth or termination claim is made.
4. **Theorem B (§4): correct.** The exponent-4 proof via c·g²·c⁻¹=g⁻² is fine. The Hilbert-only exponent-2 proof (inertia injects, inertia generates by Minkowski) is fine. The detector step via Chebotarev is fine, and C|60 and C|6 are computed correctly. Two challenges:
   - **It undersells itself.** The disclaimer "not a claim about restricting to primes splitting in a preassigned field" is unnecessary in the relevant case. If K⊂L (adjoin K, which is still a ring class field) and K∩ℚ(ζ_M)=ℚ, the same fibre-product argument works inside Gal(EL/K). That case covers every (★) field, since p ramifies in K_C. Prime divisors of 4Cp+1 always split in K_C, so this is the scope that matters, and it should be stated.
   - **Novelty is likely folklore-level.** The group theory is elementary, so priority should be phrased modestly.
5. **Internal quartic example: correct.** I verified the D₄ fibre-product structure, that η² cuts out ℚ(√5), and η=ρ·ψ with ψ quadratic. The logs fit (−1)^(a+b): η/ρ is trivial at 151 and 239 and −1 at 83 and 2447, consistent with an arbitrary twist. This is a genuine upgrade. It closes two caveats that FRONTIER (lines ~836 and ~1038) still records: "quartic identification sample-certified only; no (★)-internal configuration was constructed". The §0 block proposes no FRONTIER update for this. The genus-independence sentence ("prime discriminant supports … after adjusting the conductor") is muddled. The simple argument (χ₋₁₁ and χ₅ agree on both primes, χ_p by the product formula) is enough.
6. **Falsifier screens F1–F4 (2521, 3361, 113035442521 included): pass.** The numerator-8 controls, the U⁽⁸⁾ valuation case at 2521 (88=8·11, v₂(r)=1), and the checks that no Z₇ element is of the form 2m²−1 all hold.

## Form and process defects (must fix)

- **AGENTS §2 "Errors" violation.** A refutation must fix every master-file quote in the same commit. FRONTIER.md:2846 still says "C (… c ∈ {1,3,5} except 3361, 21841, 76441)". STATUS §2 item 3 lists Conjecture C unscoped, and STATUS §4 needs a refutation entry. `Z68_U7F.md` §9.1 (and lines 292, 314, 346, 409) needs a `> **Erratum (z81):**` pointer. The commit touches no master file.
- **Triage is incomplete.** §0 lists only REFUTATION. Theorem B should be BARRIER-SCOPED (a FRONTIER line next to the `Z60_RAYCLASS` Prop 3.1 entry). The internal example is an upgrade of Prop 4.1's caveat and needs a FRONTIER edit at export after review. Theorem A and §3 are NULL/DATA.
- **Label.** The header says CERTIFIED while the body mixes PROVED, CERTIFIED and Assessment. Per-section labels exist, but §0 should say "mixed; see sections".
- **Readability.** The prose is very dense and stacks defensive negations ("not …, not …"). There is orchestration residue ("the two requested monster primes"), and "None is evidence for a full numerator-8 failure" is opaque. `Review: none` should become this cross-lab review, noting that my independent sympy engine confirms both counterexamples.
- **Branch.** It is behind main because z81-lit was merged after it forked. It merges cleanly, and the 15k "deletions" in a two-dot diff are an artefact of that.

No claim here amounts to ES, (S) at all primes, U₇ or (MS⁺₁₀₅), and none is made.
</code-review>
