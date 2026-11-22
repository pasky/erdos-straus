<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-farey-proof (notes/z81/FAREY_PROOF.md). The author is a GPT-6.2 Astra lane. Verify every theorem, model construction, order/valuation/Bézout/IOpen check, ES-exclusion proof (no leakage of positive witnesses!), Farey/short-vector/Gauss-reduction verification, falsifier screen (F1–F4), and scope claim. Never allow pooling of separate models. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit 2a54bd0dfc5e07cab47a2975fb70a911b64c6777
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 14:32:09 2026 +0100

    Combine Bézout and supplied Pell windows at an ES-failing prime via a fixed subpower cut

 notes/z81/FAREY_PROOF.md | 90 ++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 90 insertions(+)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no mathematical error. The fixes needed are about scope, wording and triage. This is the cross-lab review the note says it still owes, so after the fixes the "Review:" line can cite it.

**Scope reviewed:** commit `2a54bd0`, which adds one file, `notes/z81/FAREY_PROOF.md`. No master files are touched, which follows the lane rules, and the §0 block has the required format.

## What I checked and believe correct

**§1: Pell solution at p gives negative Pell, in IE₁⁻.**
- The mod-4 parity step, the split of `(u−1)/2 · (u+1)/2 = p(v/2)²`, and the lemma that coprime factors of a square are squares in a Bézout domain all check out.
- The strict decrease `w² = (u+1)/2 < u²` checks out.
- The packing into a unary induction block (index bound `w ≤ u−j`, with a "factorization of p" escape) is sound. Primality comes from Bézout, and the witness bounds are polynomial.
- This is Legendre's classical argument, and the note says so; it claims no priority.

**§2: the cut lemma for the subring T.**
- **The cut C** (elements b with every ordinary power `b^j < H`) is a convex subring. It is not a model of PA: `⌊log H⌋` lies in C but `2^{⌊log H⌋}` does not.
- **IOpen.** T is the convex subring of R bounded by ordinary powers of H. It is an integer part of the real closure of its fraction field: fractions are bounded by discreteness and roots by the root bound. So T satisfies IOpen.
- **Dichotomy.** Any a in T above C has ordinary powers cofinal in T. The proof routes through a B-point in `(a, 3a/2)`.
- **Pell windows, a above C:** the first ordinary power `e^j ≥ 2n` gives `e^j < 2en`, and the window bounds `n ≤ u ≤ (2a+1)(n+1)` follow.
- **Pell windows, a in C:** then d and b are in C. Powers are bracketed inside B, with one extra comparison using `e ≥ 2+√3`.
- **PA subrings.** Every PA subring D of T lies inside C, because `a^a` would have to lie in D.
- **Factorial strings.** The counterstep argument holds. Divisibility facts agree between B and T because every quotient is bounded by `h ∈ C`.
- **Nonvacuity.** An elementary non-end extension `D₀ ≺ D₁` followed by a MacDowell–Specker end extension `D₁ ≺ B` works. It also gives T a nonstandard initial PA cut D₁.

**§3: the moving-modulus construction.** I checked:
- freezing at old primes via the Vandermonde bound (M contains `|V_e|²` and `D_m`);
- root-avoidance at newly entered primes (it needs the prime to exceed the total degree, which the factorial look-ahead guarantees);
- invariant 2 at precision d, obtained by Taylor expansion at a later depth with `d | D_j/D_m`;
- that the integrality loss is `D_m^{deg}`, which lies in C, so the reserve really does not shrink.

The point is sound: in z80 the reserve shrank only to secure invariant 2.

**§4: ES exclusion, with no leakage of positive witnesses.**
- **Seed.** `P = (1+LZ)²` is restricted to K(P), and `(P−1)/840` is arithmetic.
- **Hull test.** It works by peeling off the leading coefficient `L^{2n}`.
- **Descent and positivity.** Any ES triple descends to polynomials `G_i(P)`. Their positivity propagates to the whole positive ray by the clopen argument.
- **Specialisation.** At the late depth, `1+Ls` is a unit at every prime of D, so `gcd(1+Ls, LD) = 1`. Choosing q by CRT gives positive B-integers `G_i(q²)`.
- **Contradiction.** The pattern is strict: divisible by q² when the constant term is 0, coprime to q otherwise. This is exactly the strict Type I/II triple at an odd square that PA excludes (z79 §11).

**§5: passing from R to T.** Bézout and the (Sep) factors compress into T with polynomially bounded entries. ¬ES(P), primality of P and the `840` quotient all restrict. BCM fails.

**Numerical replay (well under the 15-minute cap):**
- 8/11, 8/17, 8/131 and 8/241 have no positive unit-fraction triple.
- (★) is zero at 409, 577, 5569, 9601, 23929, 83449 and 102001, and holds at 241 (with d=3).
- 409 = 20²+3², 241 = 15²+4², and 241 ≡ 1 (mod 24).
- The two R₈ zeros are ≡ 361 (mod 840), so both lie in 𝔐.
- The last prime (★) zero in `data/z58/screens` is 8,813,281.
- All cited files exist.

## Issues to fix

1. **The main consequence is never stated.**
   - The z80 §17 obstruction (G), which kills Farey, short vectors and Gauss reduction, needs a scalar S above every ordinary power of P. T contains no such S.
   - z80 §6's L(Div) and factorial witness needs `b!` with `b > 2P`, which T also lacks.
   - So in T, full Farey, prime short vectors, full reduction, L(Div) and IE₁⁻ are genuinely UNKNOWN. None of the note's screens rules T out as an IE₁⁻ model.
   - The only hint is the obscure "does not force a genuinely super-polynomial error…" sentence in §5.
   - Fix: add a z80-§19-style HOLDS / FAILS / UNKNOWN ladder for T. Flag T to the orchestrator as an *open candidate*, not a claim. Rename the note or state its outcome, since "FAREY_PROOF" proves no Farey result.

2. **The Scope line contradicts §5 and leaves out Lag.**
   - It says "No claim of … BCM", but §5 proves BCM fails.
   - Lag also fails, by z80 §6's argument: the residue at P is formally real, since `K[P]/(P) = K` and the edges preserve this. −1 has no root mod P.
   - State both failures.

3. **§1's new IE₁⁻ consequence is never tested on T.**
   - At P it holds vacuously, but only once there are no Pell units in `K[√P]`, which needs proof.
   - At B-primes it holds by PA.
   - At other horizontal primes it is open.
   - Since this screen is generated in the same note, the note should run it on T.

4. **The STATUS delta is ambiguous.** "No full Farey or IE₁⁻ separation" should become: "full Farey/short vectors/reduction/L(Div)/IE₁⁻ undetermined; Lag and BCM fail; only P≡1 (840)". It should also note that T loses things z80 Model 2 has: congruences at every nonstandard modulus, Lag, internal Dirichlet, and a cofinal PA ring. "Separately" is right; this is a trade-off, not a strengthening.

5. **Triage and FRONTIER.**
   - HEADLINE is debatable. The result adds a rung to the z80 ladder, and the new combination (IOpen+Bézout+(Sep)+PW ⊬ ES) is real.
   - It does narrow the scope of the z80 §§1,16 factorial and diagonal-limit barrier: that barrier needs a PA scalar above P, and power cuts escape it.
   - Propose a FRONTIER §3/§4 edit; the note currently proposes no FRONTIER delta.

6. **Cross-references and label.**
   - §2 says "rel. §§3–6" but should say §§3–5; §6 is the falsifier table.
   - The Label omits compactness, MacDowell–Specker and Nagata, all of which are used.

7. **Readability.**
   - Define T formally.
   - In the cut lemma, state the 3/2 density factor directly instead of "2, replaceable by 3/2".
   - In the BCM proof, say "comaximal in the K-algebra A". In T itself, P+1 and P+3 share the factor 2.
   - §3's final sentence on chart pull-back and the patching for rows are very compressed. I accept them by analogy with z80 §3, but they deserve a few explicit lines.

8. **Minor.**
   - The word "failing" in "any failing prime p≡1 (4)" in §1 does no work.
   - The falsifier table (F1–F4) is sound and pools no models. §1 is kept separate as an IE₁⁻ theorem, and §§2–5 are one model T, including the nonvacuity choice of B.
</code-review>
