<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="806c9cf79">
A separate reviewer subagent was asked to review the changes in `git log 806c9cf79..`. Its request and review follow.

Request: review changes since 806c9cf79 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus Round 2 review of Wave z83 Lane 2 (notes/z83/BCM_TS_LDIV.md §§6–8 and §0). Scrutinize every step of T_pf, especially one-place valued pair embeddings/old PA value group, Tarski–Vaught and formula fairness, reserve digits, Farey/host and dyadic composition: read git show 852dcb457:notes/z83/IE1_DECIDER.md §§6–8, currently on side-agent/z83-ie1-decider, for the imported lemma and compare z81/z82. Check all coarse M-fibre and CRT/order arguments, axis-unit no-go and scope. Challenge theorem, try to falsify signs, and give export verdict with concrete fixes. Cap any replay at ≤15 min; no heavy computation.

Commit log:
commit 89b89863e868ef396c151631fa46811704926200
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 04:02:21 2026 +0100

    Join elementary prime residues to Farey and dyadic lifts; separate squarefree product gluing

 notes/z83/BCM_TS_LDIV.md | 80 +++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 75 insertions(+), 5 deletions(-)

Review:
**Round 2 review: z83 Lane 2, `notes/z83/BCM_TS_LDIV.md` §0 and §§6–8 (commit 89b89863e)**

**Verdict: ACCEPT WITH FIXES. Not exportable yet.**

I found no fatal gap. The T_pf construction, the §7 squarefree-product no-minimum, the §7.1 criterion, scalar density and §8 all hold at the level of an interface audit against z81 §§3, 12–13, z82 and Lane 1 §§6–8. Lane 1 §§7–8 is the imported lemma; I compared it at 852dcb457 and at bb06ac1bc. Several fixes are needed before export: one dependency, one stale section, the headline wording, and the scope and triage. I ran one replay, under a minute: a check in the ordinary integers that §7.1's progression classification and least-hit criterion hold, for random squarefree products of primes up to 13. It passed.

## What I tried to break

| Target | Result |
|---|---|
| **§6.1 algebraic service (old PA value group).** Lift the monic minimal polynomial to `f`; Hensel root `α`; `x=α+qZ`. | Holds. `f` stays irreducible, its residue degree is at least `deg f`, and the fundamental inequality then forces ramification index 1. So E(α), E(α,Z) and E(x) keep the old value group. `x` is transcendental over E because Z is. Minor: the residue field of E(x) also picks up a transcendental (Abhyankar), so it is bigger than old-residue(b). This is harmless, because requests about new residues are enumerated later. Say so. |
| **Coefficient bounds** `q^n a_i` (q-edge) and `(hD)^n a_i` (dyadic edge) for all i | Holds. On the selected branch, Lane 1 §8 gives equality factor by factor. Undoing the substitution through an integral centre then bounds every coefficient, not just the leading one. This is a new claim beyond Lane 1, and I checked it. It relies on Lane 1's R2 fix 9 (each `(T−s_j)/D_j` is integral at every depth). That fix is in bb06ac1bc, not in the pinned 852dcb457. |
| **Order and hull** `x=qHη` | Holds: `|a_n|(qH)^n ≥ H^n/D^n`. |
| **Arithmetic quotient = valuation residue at q** | Holds. Surjectivity uses normalisation at q, then clearing other scalar poles with one scalar (invariant 1), then a Bézout inverse mod q. |
| **Tarski–Vaught and fairness** | Holds. Chain elementarity, then TV, gives `κ_final ≺ F*_ω`. Together with `k_q ≺ F*_ω` this gives `B/qB ≺ T/qT`, and P̄ transcendental makes it proper. Wording: TV needs `∃vφ` with φ *arbitrary*; the text says "existential pure-field formula". |
| **Signs** | Holds. Any later extension preserves the squareclass of P̄ fixed at the start. With all signs negative, §1 applies verbatim. QR fails at *every* odd scalar prime, the reserve primes included, because q is never a square mod P. The note says this correctly. |
| **§7 coarse fibres** | Holds. If `c∉C` it is a non-unit of B′, and a maximal M containing c contains h. Primes of 2 and large primes q become units at M. The new edges localise to polynomial rings. The fibres never vanish (gcd plus contraction). Regularity follows, `X²−p̄` has no root, so `c∈C`, and the prefix competitor finishes. I checked the inequalities `t'<h²/Q<h²/c≤t`. z82 short-pair dilutions at a modulus n∈M are still free in (Y,W), so they also localise to polynomials. |
| **§7 converse** (leastness ⇒ a root mod some `d>C` dividing every subproduct `e>C`) | Holds: `p|t ⇒ p²|t`, then `c=d²`, and `d²|X² ⇒ d|X` by integral closure. |
| **§7.1** | Correct, and checked numerically. But it is a reformulation: hits are a union of progressions, and a least hit exists iff their first points have a minimum. "Lower cut … attained" just means "has a least element". Title it a reduction, not an "exact criterion". |
| **Scalar density** | Correct, and elementary: base-m expansion, plus `x<m^k` for some ordinary k. |
| **§8 punctured units** | Holds, both for the z78 axis and for §4.1. I checked the latest-angle comparison `v(a(1+ε)^m−1)=v(ε)`. The increasing significance of `e_i` puts a later, smaller increment below any initial one. The monic-edge unit argument is right (torsion-free over A, units in `Frac(A)[x]`, constant contraction). Citations are missing for the "twisted monomial axis" (z82 BCM_LDIV §2, z78 IE1_UNITS §§1–3) and for "non-power-cofinal" (z81 §15). |
| **Composition with Farey, the z81 §13 PA order host and Lane 1's dyadic edges** | Holds as stated: the four §3 interfaces, content valuations, and a UFD upper algebra A[x] with units K*. |

## Required fixes

1. **Dependency pin.** 852dcb457 is not an ancestor of HEAD. Lane 1 has since had its R2 review (ACCEPT WITH FIXES, `REVIEW_IE1_DECIDER_R2_OPUS.md`, 31bb465d2) and fixes at bb06ac1bc. §6.1's all-coefficient freeze uses its fix 9. Re-pin to bb06ac1bc and cite that review. Merge both branches before export: Lane 1 also pins this note at e82519e23, off-branch. Harmonise "IE1_DECIDER §§1–3,6–8" in §0 with "§§1,3,6–8" in §6.
2. **§0 Result wording.** "even when P is a square at every one of those prime fields" is misleading. The primes of the §7 modulus h are *reserve* primes, where P is always a square, and the large-prime signs don't matter for that h. Suggested replacement: "…no least hit, although P has a root modulo every reserve modulus and (with positive signs) modulo every scalar prime of the cut."
3. **§7 scope is broader than "in the above model".** The argument uses only:
   - contraction and Bézout;
   - reserve roots;
   - polynomial, row and sphere sandwiches after inverting C, at coarse maximal ideals M.

   So it also holds in T_F and in every z81/z82 schedule. Say so; that is what justifies the BARRIER-BROAD triage. Also say it is **unproved for Lane 1's T_Π**: mixed-support DL edges at moduli sharing reserve primes destroy the polynomial presentation at M, as Lane 1 itself notes. So nobody should quote the §7 test for T_Π.
4. **Stale §5 Assessment.** It still says "outside the square-tested reserve-Gauss class the full scheme remains open" and "No master files changed". T_pf lies outside that class, yet the quintic still fails there. Add an "Assessment (export, superseding §5)" with:
   - the FRONTIER §4.18 replacement;
   - a §4 screening line: "making each prime residue field rich, even elementary, gives no root modulo a smooth squarefree h∉C; test gluing on coarse fibres".
5. **STATUS delta.** Add a label and pointer ("PROVED rel. …, BCM_TS_LDIV §§6–7, IE1_DECIDER §§7–8"). Merge it with Lane 1's delta into **one** PW/Farey row; AGENTS §3 forbids a second row for the same quantity. Neither model contains the other: T_Π has the full DL scheme on mixed supports, T_pf has pure dyadic lifting plus elementary residue fields.
6. **Triage.** "RECORD" for §6 is arguable, since T_pf does not dominate T_Π. Its real content is barrier-type: richness of individual prime fields is not the obstruction, CRT gluing is. I'd suggest BARRIER-BROAD for §7 and BARRIER-SCOPED or METHOD-CX for §6. Keep RECORD only if the merged STATUS row is about combinations of relaxations.
7. **z81 §12 interface.** z81 §12 says that at l∉C "every edge uses the baseline minimum", which is no longer true at served q. State the modified invariant: each ordinary edge born later is still Gauss over the *current* marked field, and the sphere-point lift needs only an infinite residue image. Also add one sentence on Farey temporary completions: their pair extensions at q continue the current chain, and the retained prefix keeps them, so the TV chain never forks.
8. **Minor.**
   - TV wording (arbitrary φ).
   - "log h∼L": the Chebyshev lower bound suffices.
   - The "constant-modulus least fragment" doesn't need pseudofiniteness and so holds in T_F too; say so, and check for overlap with z81 §13's constant-modulus case.

## Open questions (no fix needed)

- **Next repair attempt.** B′ localised at M is a valuation ring, so the obvious next try is TV-style service at coarse M. §7's converse shows what that must achieve: a single arithmetic lift on *every* PA subproduct e>C, which means coherence across infinitely many M, not one fibre at a time. That is a precise target; it is the note's "simultaneous squarefree-product repairs".
- **Combining with mixed DL.** Whether T_pf can also absorb Lane 1's mixed-support DL while keeping the §7 obstruction is open. The note's own scope restriction already leaves it open, and the export text should say so.

No ES, IE₁⁻ or ℕ claim follows from any of this, and the note's scope says so correctly.
</code-review>