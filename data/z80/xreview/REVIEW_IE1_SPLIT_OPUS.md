<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review. The author is a GPT-6.2 Astra lane. Check every model construction (ring axioms, discretely ordered, normality, each claimed induction/least-number instance and its exact formula class and parameters), every provability argument's formula complexity, and scope of notes/z80/IE1_SPLIT.md especially the simultaneous dilution, two-chart Gauss order, reserve-shrinking, PA strict-square progression, primary isolation, factorial and coupled PW failures. Require hostile fully independent checking, not plausibility. Give commit hash and export verdict. Do not edit files.

Commit log:
commit 94a31e87a05028057d6a3fc7f7f70ef5bd689fb9
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:23:26 2026 +0100

    z80: split all translates with scalar content and cofinal PA windows; isolate divisor lock

 notes/z80/IE1_SPLIT.md | 133 +++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 133 insertions(+)

Review:
**Verdict: ACCEPT WITH MINOR FIXES. Export is OK** for commit `94a31e87a05028057d6a3fc7f7f70ef5bd689fb9`, which only adds `notes/z80/IE1_SPLIT.md`. This review counts as the owed cross-lab hostile review. I edited no files.

## Headline claim
The headline is that `T = IOpen + Bézout + (Sep) + ∀n W(n;2,3) ⊬ ES` and `IE₁⁻ ⊢ T`. `W(n;2,3)` is exactly z75's `W₂` with K=7, so the note really does settle STATUS §2 item 4's "Bézout+IW₂" target. It is new: z75 and z79 had windows but no Bézout, and the z76 PID had Bézout but no window.

## What I re-derived myself, step by step
* **§1 induction block:**
  * Formula (1) is a single parameter-free `E₁` formula, and every bound is polynomial in `1+y`. The base holds by excluded middle at 0. The step carries the exception, or the newly false test supplies `k=i`. At a square it starts over.
  * Two-sidedness is needed only for the `¬V` disjuncts, and division with remainder supplies them.
  * **Factorial test:** one can choose `b` with `y+ℓ<b` for every standard `ℓ`. That `i∈B` contradicts `¬V(i+1)` is correct. Transcendence over `K` follows because a PA model is an integer part of its real closure (Shepherdson) and `R` is discrete. This gives the infinite rank.
* **Reserve:** compactness over predicates for `D` and the `Cₙ` works, together with relativized-PA and elementary end-inclusion schemes. Finite fragments come from iterating MacDowell–Specker.
* **§3 dilution:**
  * Gauss values are nondecreasing with depth and unchanged at `ℓ∤J`.
  * `v_ℓV_e < v_ℓJ`, and the adjugate argument gives some `j≤e` with value `≤v_ℓV_e`. A 20k-case random check found no violation.
  * The PA-CRT digit freezes the value at every `ℓ|J` at once, and later digits do not disturb it.
  * Invariant 1 holds with `c(f)=γ·gcd(N,J)`, a PA scalar. The two charts patch along the partition given by `c(b)`.
  * Invariant 2 at `C'` holds because `dV_e | J` for `d∈C'`, and the normalised fraction argument goes through.
* **§4:**
  * Depth-zero row ring is exactly `R_A[u,v]`: `aᵉ` clears the poles, and the identity `(au+bv)^{N+M}=1` lets you intersect the two localizations.
  * The sandwich `R_A[u,v] ⊆ R_{A'} ⊆ R_A[u,v,1/J]` holds.
  * Gauss's lemma holds over the gcd domain `S`. The leading form `H^k f_k(b,−a)` is not relatively infinitesimal, so the localized row meets the hull only in `Frac C`.
  * Old primes persist, since modulo a prime the row is an integral cover by two charts. Nagata applies, and the units stay `K*` because `A[1/a]∩A[1/b]=A`.
  * Floors work, and shrinking the reserve from `C` to `C'` preserves both the hull test and the residue embedding.
* **§5 bad prime:**
  * `P` is primitive and prime, and `(P−1)/d∈R` for every `d∈D⁺`.
  * Descent works through pole valuations, and positivity holds on the whole positive ray (it is clopen there).
  * `G_i(a+lZ)∈B[Z]` at a common depth. The cleared identity is `p·e₂=4·e₃`, so at least one constant term is zero. Three zeros would give 4≤3.
  * `s²≡a (mod l)` is solvable: `a≡1` modulo every odd prime of `J`, and `a≡1 (mod 8)`. The gcd conditions give a strict Type I or II triple. Excluding that rests on z79 §11's Jacobi proof, which I did not re-derive.
* **§6:**
  * Global (Sep) and Bézout hold via the factor calculus, and the least primary hit exists and is a coded power.
  * `L(Div)` fails: in `t|b! ∧ t>P` every hit is old, and `t−1≠P`.
  * BCM fails because the factors `X+j` are independent.
  * Lag fails because `Frac(A/P)` is purely transcendental over `K`, hence formally real.
  * Supplied-unit PW is forced by `IE₁⁻` (bound `u'<2au`), yet fails in the model at `d=P²−1`. The only norm-one units there are `±z^j` with `j` standard, via `K[z,z⁻¹]`, so abscissae stay below `(2P)^j`.
  * The `W(n;2,3)` successor bound checked numerically.
* **§7:** unary least descent and the reduction of ES to primes are correct, including the bounds `x≤3n/4`, `y≤2nx`, `z≤nxy`.

## Not independently replayed
* z79 §§1, 3 and 11 are imported; they were Opus-reviewed earlier.
* For §7's one-direction Smith 3.11 claim, I only confirmed against the archived text that Lemmas 3.2–3.10 minimise unary sets with a standard numeral `p`. Keep it labelled "rel. Smith".

## Required minor fixes
1. **`IE₁⁻ ⊢ IOpen`:** the note cites z79 §4, but that section proves base and step *in* IOpen, not that `IE₁⁻` proves IOpen. Cite §1 instead: open tests are two-sided.
2. **§1 factorial test:** state the shift `V'(i)=V(i+1)`, `H=y−1` explicitly. Read literally, (1) is vacuous because `0∤h` makes `¬V(0)` true.
3. **§1 two-sidedness:** say which theory proves it, and that the step uses provable totality `V∨V'`.
4. **Label:** add z79 §§4 and 8 (Bézout, (Sep), the isolation equivalence) and Smith (for §7) to the "rel." list.
5. **BARRIER-BROAD scope:** the barrier needs a *non-initial* PA subring; FRONTIER must carry that hypothesis. The "pole tower" Assessment is in fact a PROVED corollary: if the units of `(B∖0)⁻¹R` are `K*`, then `IE₁⁻` fails.
6. **STATUS delta:** add "fails supplied-unit PW at `d=P²−1`", for parity with the z75–z76 PW row.
7. **Wording:**
   * Fix the typo "geometic".
   * "advancing 2 to C′" should say the reserve shrinks.
   * Write out `c(f)=γ·gcd(N,J)` in §3 so invariant 1 can be checked directly.

## Points for debate
* **Triage:** I'd present this as a RECORD-type separation of a listed relaxation, not a structural step toward ES. The model is deliberately far from `IE₁⁻`: it fails factorial divisor induction, PW, `L(Div)`, Lag and BCM.
* **The factorial-divisor barrier** is short and genuine. It is the cleanest new item here: it shows that every construction with a cofinal PA coefficient ring needs non-scalar units in `(B∖0)⁻¹R`.
</code-review>
