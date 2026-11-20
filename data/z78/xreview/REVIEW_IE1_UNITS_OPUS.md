<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="b40458745855c19f35d865af56908f7616a85d38">
A separate reviewer subagent was asked to review the changes in `git log b40458745855c19f35d865af56908f7616a85d38..`. Its request and review follow.

Request: review changes since b40458745855c19f35d865af56908f7616a85d38 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Requested independent cross-lab Claude Opus hostile review for wave z78. Identify your model. Audit notes/z78/IE1_UNITS.md and its cited interfaces, every axiom verification, ¬ES(P) preservation, both proof tiers, labels and scopes. Especially (1) two-component residue and finite-dimensional Kummer bound, (2) recursive residual proxy controls integrality/scheduling, generic specialization, rotated covers and infinite-field good prefixes, Gaussian normalization/TS, (3) cubic induction barrier, the nonstandard cut model. Look for counterexamples or circular dependencies. Return full review with severity/edits and verdict. Please do not edit any files; I will store your output verbatim.

Commit log:
commit cd960485a69f7db363fbd3fe842184bd47f22eae
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:56:38 2026 +0100

    z78: normalize split primes recursively and close the arithmetic TS successor

 notes/z78/IE1_UNITS.md | 24 +++++++++++++++++++-----
 1 file changed, 19 insertions(+), 5 deletions(-)

commit d804db79765c5f63cd0c1a1bc03ffa882d4c9410
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:54:32 2026 +0100

    z78: prescribe finite rotation functionals through recursively serviced proxy circles

 notes/z78/IE1_UNITS.md | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

commit 4b210bf6f80ad5cb4e0825014bfdfa7af1741574
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:51:19 2026 +0100

    z78: cubic induction barrier beyond full multiquadratic height surjectivity

 notes/z78/IE1_UNITS.md | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)

commit 161b10d9b05be159528d46b19efb1bb5a0c10f78
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:48:25 2026 +0100

    z78: bound residual squareclass kernel by cyclotomic and single-radical ranks

 notes/z78/IE1_UNITS.md | 9 +++++++++
 1 file changed, 9 insertions(+)

commit e4f140aa794b605f9d67ef4f71dbb962cae2cf80
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:43:34 2026 +0100

    z78: identify the two-component restriction and first-axis circle controls

 notes/z78/IE1_UNITS.md | 24 ++++++++++++++++++++++++
 1 file changed, 24 insertions(+)

Review:
# Hostile cross-lab review: wave z78 `notes/z78/IE1_UNITS.md` (commits b4045874..cd960485)

**Reviewer:** Claude, an Anthropic Opus-family model, running as a Claude Code subagent. The exact version string is not visible to me. The note appears to be Astra-authored (every z77 lane was Astra/GPT), so this counts as the other-lab review that AGENTS.md §3 requires. I edited no files.

**What I read.** The full diff: five commits, all of them adding the one new 83-line note. I also read the interfaces it cites: `notes/z76/QR_TS_BCM.md`, `notes/z77/IE1_NONPID.md`, `notes/z75/BCM4_PUSH2.md`, `notes/z76/IE1_BREAK.md`, `notes/z75/IE1_PUSH2.md`, and STATUS/FRONTIER rows 118–131, 156–159 and FRONTIER §3 item 18.

**How deep the check goes.** I re-derived every lemma that is new in this note. I checked the reused z75–z76 machinery only at its interfaces: prefix/tail marks, uniform Lang–Weil, the order and DVR proofs, and z76's spectral-sequence control lemma. I did not re-prove those from scratch.

## Verdict

- **§§1–3 (universal TS added to the BCM + Lag + full-QR Bézout ES countermodel): ACCEPT WITH FIXES.** I found no counterexample and no circular dependency. Every new lemma I re-derived holds. The fixes are mostly about presentation and checkability, but for a HEADLINE they should be done before export (M1–M3).
- **§4 (cubic window C₃, the unit-descent barrier, and the PA-cut model): ACCEPT, minor fixes.** It is correct and fairly elementary. Its triage and scope wording should be tightened.
- **¬ES(P) is preserved** in both models.
- **The labels are acceptable** once the dependency list is completed (m1).

---

## (1) Two-component residue and the finite-dimensional Kummer bound

**§1 parameter embedding: correct.**
- Over K=E(i), the circle X_K is a split torus G_m with coordinate U. So Br(X_K)[2] = Br(K)[2] ⊕ (K*/2)∪(U) exactly (characteristic 0), and the lift γ+(a,U) is literally correct.
- At every punctured q≠s the Laurent fibre forces v_q(a) to be even. At s the same holds on the component where U is a unit. Gaussian base change is unramified, and A° is a UFD with units F*·t(G), where t(λ)/t(λ/2)² lies in F*. Together these give a ∈ F*·E*².
- s is inert and has odd valuation, so s is not a norm. Hence J=0 and the parameter is unambiguous.
- The sign case reduces to z76's order-four argument. That needs (−1,s)≠0, which holds because its residue [−1] is nonzero in k_s.

**§1 two-component comparison: correct, and I re-derived it.**
- Downstairs the divisor over s has residue field κ(D)=k_s(i′)(x), with i′=y/x.
- Over E(i) it splits into D₁={Ū=0}, where U is a unit, and D₂={U=0}, where v(U)=1. Each residue field is isomorphic to κ(D) by a map fixing k_s and sending i′↦∓i.
- With e=1, ∂_{D_j}(β) is the image of ∂_D β. That image is the same old class c∈k_s on both components. The residue of γ is the same base class in l=k_s(i) on both components.
- ∂_{D₁}(a,U)=0 and ∂_{D₂}(a,U)=[a]. Therefore [a]=0 in l(x), hence in l.
- Proxy consequence: for s=hV+b we have A°[V]/(s)≅A°, so k_s is the preceding field. That field is ordered, so s is inert, and it is regular over F, so E_prev(i)/F(i) is regular. Then a ∈ F*∩F(i)*² = ±F*², and the sign case gives W=im Br(E)[2]. **Correct.**

**§3 Kummer bound: correct.**
- A_j→A_n is finite free, so A_j/s embeds in A°/s and is a domain. K_n=K_j(x_n) with x_n^{2^{n−j}}=d·x_j.
- The constant-field kernel at level j is finite because the algebraic closure of F in K_j is a finite extension.
- Gal(K_j(μ_{2^∞})/K_j) sits inside {±1}×ℤ₂, so it has mod-2 rank ≤2.
- Over M=K_j(μ_{2^∞}) the fields M(x_n) are nested, cyclic and single-radical. So Hom(Gal(M_∞/M),ℤ/2) has rank ≤1.
- The extension bound gives Hom(Gal(M_∞/K_j),ℤ/2) ≤ 3, and k_s(i) ⊂ M_∞. The stated bound (constant kernel + 3) is right.
- This finiteness is genuinely necessary: one H-mark can only prescribe a functional on a finite list.

**§3 parity coordinates: correct.** F*/2 = {±1} ⊕ ⊕_layers ⊕_{primes born there} 𝔽₂.
- Top-layer punctured valuations separate the top primes.
- F_prev is relatively algebraically closed in F, so F_prev*/2 injects.
- Monomials are positive old scalars modulo squares.
- A finite-dimensional subspace of a direct sum has finite total support, so finite-support extension of functionals is immediate.

## (2) Recursive proxy controls, specialization, covers, infinite fields, Gaussian normalization/TS

**Non-circularity: verified.**
- Clauses 1 and 2 for S_n are renewed inside successor n. The proxies' H-marks there use only clauses 1 and 2 for the completed S_{n−1}.
- General circles in successor n also use only S_{n−1}.
- Gaussian normalization uses TS only at primes from completed earlier successors, and the bottom's classical and z76 TS.
- The recursion bottoms out at successor 1, which has no H. There all places are bottom primes, including 2 with its 5-rotation.

**Clause 2 bit computation: verified.**
- At a top place r, rotating by a nonsquare unit norm u gives χ_r∂_r(f,u) = v_r(f) mod 2.
- Primes born at a higher layer have unit images all the way down the H-chain. A unit paired with a unit gives 0 at odd places. At 2 it also gives 0, because ε(5)=0 makes (5,u)₂=1 for every 2-adic unit u.
- Primes born at a lower layer are scalars of value 0 at every axis above their birth, so sp leaves them unchanged until their birth place, where v=1.
- So the vector the recursion can reach is exactly "any finitely supported birth-coordinate functional". That is what the general circle needs on the finite list sp_H(a_j).

**Clause 1 renewal: verified.**
- For b∈S* with dyadic value ≡1 (4):
  - at odd top places the norm is surjective on units (inert by Lag isotropy or a finite field; split trivially), then Hensel lifts;
  - at 2, units ≡1 (4) are sums of two 2-adic integer squares;
  - at H, red_Hφ_H(b) lies in S_old* with the same dyadic value, so the old clause 1 applies, and Hensel lifts at a nonzero coordinate.
- The free-line counterexample (−1,u) of z77 §5 is now killed by the residual proxy circle. z77 only claimed survival under the unchanged edges, so there is no conflict.
- The forced-P example from that same section is consistent with §1: P is a square in k_s, and the bit at P is available because P is split.

**Specialization detail: correct.**
- The torus-action identity m*β−pr₁*β=(a,δ(t)) holds on the function field of X×T₁. This is z76's control lemma over E(X).
- Pic(T₁)=ℤ/2 could make the parameter ambiguous by [−1], but (−1,N v)=0.
- The Gauss-axis extension keeps G=2G, and the maps are dominant on reductions. So sp commutes with the pullbacks, and evaluating at generic pairs in local balls is legitimate. This really does close the "hidden Gaussian-kernel term" loophole.

**Rotated covers and infinite-field good prefixes: acceptable as an extension of z76 §3.**
- The square-root substitution over the algebraic closure is the same trick z76 already used.
- At infinite top residue fields, every nonzero element is a Gaussian norm. Two squareclasses plus −1 written as a quotient of norms (from Lag isotropy) give this. So fibrewise rational points exist and the fibration density argument works.

**Gaussian normalization/TS: verified.**
- q=c·gḡ with c∈F*, c>0.
- Inert coordinates of c are even at every layer, by descending q=cN(g) through sp modulo squares. Here q's images are units and the norms' images are norms.
- Split coordinates are norms by TS from earlier layers, and 2=N(1+i). So c is a norm without needing any number-field norm theorem.
- The split-place imbalances (m,−m) are corrected by (π/π̄)^{−m}. Each such factor is a unit at every other place, at every intervening axis and at younger layers. This is correct.

**Edge cases I tried that do not break the argument:**
- A proxy whose residual b is not an arithmetic unit. Its normalized associate is listed. If χ_q(−1)=0, the QR supplement makes that associate ≡1 (4), and the associate's own TS circle kills [−1].
- A residual unit b that is negative in some ordering of k. Clause 1 is still consistent, because the axis is not the order valuation and the residual circle simply removes those orderings.
- Rotations at P. Remainders u=r+Pv are unchanged, so R/P and χ_P are unchanged.

## (3) Cubic barrier and the nonstandard cut model

- **C₃ step: verified.** N(1+t+t²)=1+2+4−6=1. The product coordinates are (x+2y+2z, x+y+2z, x+y+z), with sum 3x+4y+5z ∈ [3n,5n]. The norm-1 condition excludes sum 0.
- **General k: verified.** For odd k, N(t−1)=(−1)^{k+1}=1, and the sum factor lies in [k,2k−1].
- **Barrier: verified.**
  - A witness gives a unit with an integral adjugate inverse.
  - Every listed edge has only scalar units after adjoining F₀(t). The reason: F₀(t) is a cubic extension, which has no quadratic subfield, so radicands stay nonsquare and the conjugation still negates the Laurent exponent. Spheres keep a domain top form, and the remaining edges have monic or coefficient contraction.
  - Regularity gives linear disjointness, so the coordinates lie in D∩F₀=C.
- **Seed check: verified.** X²+1−PY² keeps an irreducible top form over ℚ(t)(P), so the IE1_BREAK §2 / IE1_PUSH2 Theorem A seed satisfies the barrier hypotheses.
- **PA-cut model: correct.**
  - In the seed, C₃ defines exactly ℕ. The sentence C₃ ↔ Pred transfers with the pair.
  - PW, normality and the filtered schemes transfer. Units of cut nonsquares exist in C by PA. So the z77 §4 criterion gives H(A*)=Γ⁰[G] for all finite independent cut systems.
  - J∋t!≠0, and J²=J by Lag. IE₁⁻ fails because base and step are provable in discretely ordered rings while ∀n C₃(n) fails.
- **No circularity.** The cut model does not rely on the PA-cut barrier theorem; it transfers the seed's failure, as the note itself says.

---

## Findings and requested edits

| # | Sev. | Location | Issue → edit |
|---|---|---|---|
| M1 | **Major (form; blocks export)** | whole of §§1–3 | There is no single theorem statement and no consolidated inductive invariant. The HEADLINE is spread over about ten "PROVED" paragraphs. → Add a displayed **Theorem** and a numbered invariant package in the style of BCM4_PUSH2 §2. It should list: the z75 input package; characters at all punctured primes with realized kernels; (B); punctured real and Gaussian UFD with units F*t(G) and F(i)*t(G); clauses 1–2 for S; TS at all completed primes. Add an "edge × invariant" table that includes the two new edge types: proxy line+circle, and the twist with protected Gaussian lists. |
| M2 | **Major (rigor of statement)** | §3a clause 2 | The "extended clause", which is what the general circle actually uses, is introduced after the fact ("We will use also…"), and "attainable functional" is never defined. → State clause 2 directly in its extended form. Define recursively Att_n(f₁..f_k) = {Σ_{r∈R} par_r(φ_r f_i) + v : R finite, v∈Att_{n−1}(sp_Hφ_H f_i)}. Prove as a separate lemma that Att contains every finitely supported birth-coordinate functional on the iterated specializations of constants. |
| M3 | Major-minor (simplify a fragile part) | "Important prefix detail" | Prescribing squares at *infinitely many* good places is unnecessary. An integral norm-one T has δ(T) of even valuation at every odd place (split: v(v₁)=v(v₂); inert: always), so a list entry that is a unit at r pairs to 0 automatically. Trivial bits need an explicit square only at the finitely many places where some entry is not a unit. → Say this. Keep the square device at most as an optional uniformity convenience. This shrinks the Lang–Weil/prefix bookkeeping. |
| m1 | Minor | §0 Label | The listed dependencies are incomplete. → Add, following z76: degree-two norm residue (the sp well-definedness), Brauer purity, Hochschild–Serre/the conic kernel, Kummer theory, Hensel, Nagata, uniform Lang–Weil, Shepherdson. |
| m2 | Minor | §3a "At the real pivot the first paragraph of §1" | Wrong pointer: the proxy statement is in the *third* paragraph of §1 ("additional assertion"), and "real pivot" is undefined. → Fix the pointer; say "proxy pivot". |
| m3 | Minor | notation | `B` is overloaded: upper algebra, Gaussian element in clause 1, and proxy lift. `𝔐` is undefined in §3b. "F_prev" is ambiguous; it means the constant field of the successor whose residual ring is S. → Rename them. |
| m4 | Minor | §3a | State explicitly χ_q(−1)=0 at proxy pivots. (B) on (−1,q) gives real bit 0, sp_w(−1,q)=(−1,b̄)→0 when b̄=1, and no other residues. For general b̄ the kernel is handled through the normalized associate's circle. At present this is only implicit in "accounted-for skips". |
| m5 | Minor | §4 "do not imply" | Properties such as H(A*)=Γ⁰[G] and J²=J are external, not first-order. → Rephrase as "there is a model with all these properties in which IE₁⁻ fails". |
| m6 | Minor (triage) | §0 Triage for §4 | BARRIER-BROAD is defensible only with an exact scope. → Scope it as "towers whose units descend after an odd-degree constant extension". Add a FRONTIER §4 screen line: "does the construction supply relative units of cubic (more generally non-quadratic) constant fields?". Optionally add, as an Assessment, the general moral: IE₁⁻ forces norm-form windows in other number fields, and quadratic tori cannot supply these. |
| m7 | Minor (form, AGENTS §2) | file | Two unrelated results with two different models sit in one note. The name `IE1_UNITS` hides the TS HEADLINE. → Split the note (e.g. `BCM_TS.md` and `IE1_CUBIC.md`), or at least give each part its own §0-style result line. |
| m8 | Minor (export) | STATUS delta | The new §1E BCM row should keep "not an external PID; fails L(Div)" (re-proved in §3b) and point to both z78 and z77 §5. Retire the STATUS §2 target-4 TS clause (line 159). Qualify FRONTIER §3 item 18 and STATUS line 158: H(A*)=Γ⁰[G] is *necessary, not sufficient* for IE₁⁻ (C₃ counterexample, z78 §4). Mark the row "cross-review owed → this review" until the fixes land. |
| n1 | Nit | §2 | "l*/l*² has order two" holds because the bottom has two classes and ordinary primes are finite fields. Say so once. |

## Baseline review of the diff

- The commits are clean: one new note, no edits to master files (correct for a lane note), no scripts or data.
- The commit messages match the content.
- The `.pi/` directory is untracked and not part of the commits.
- The "Review: none (checkpoint)" line must be updated after this review.
- The prose is extremely compressed. Several sentences ("This extends the uniform spreading/complexity argument of z76 §3", "Fixed test lists can include functions of every marked copy") push real verification work onto z76 without saying what changes. M1 and M3 are the cure.

## Bottom line

I found no fatal error, counterexample or circularity. If M1–M2 are done, I support exporting §§1–3 as PROVED (rel. z75–z77 and the named theorems), scoped as "IOpen + Bézout + BCM + Lag + full prime QR + universal TS ⊬ ES at P ≡ 1 (840), countable non-PID union, fails L(Div)".

§4 can be exported now with m5–m6.

Because the HEADLINE retires a STATUS target and leans on four earlier waves, I recommend a short second pass on the rewritten §3a only, after M1–M2. This is not required by the §3 gate, since no published record is involved.

Nothing here bears on ES in ℕ.
</code-review>
<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="b40458745855c19f35d865af56908f7616a85d38">
A separate reviewer subagent was asked to review the changes in `git log b40458745855c19f35d865af56908f7616a85d38..`. Its request and review follow.

Request: review changes since b40458745855c19f35d865af56908f7616a85d38 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Independent cross-lab Opus second hostile pass on final bb6f8e72a, especially rewritten §3a and the invariant package of notes/z78/IE1_UNITS.md. First full review ACCEPT WITH FIXES archived data/z78/xreview/REVIEW_IE1_UNITS_OPUS.md; verify all fixes M1–M3, m1–m8, n1 and look for remaining substantive gaps in axioms/¬ES(P)/scope. Check whether Att induction and the proxy finite support tree really close. No file edits. Concise explicit export verdict and any necessary corrections.

Commit log:
commit bb6f8e72aaa04b54e71ed3b624347d0f11681535
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:24:53 2026 +0100

    z78: record hostile Opus review and specify recursive attainable control spaces

 data/z78/xreview/REVIEW_IE1_UNITS_OPUS.md | 194 ++++++++++++++++++++++++++++++
 notes/z78/IE1_UNITS.md                    |  47 ++++++--
 2 files changed, 228 insertions(+), 13 deletions(-)

commit cd960485a69f7db363fbd3fe842184bd47f22eae
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:56:38 2026 +0100

    z78: normalize split primes recursively and close the arithmetic TS successor

 notes/z78/IE1_UNITS.md | 24 +++++++++++++++++++-----
 1 file changed, 19 insertions(+), 5 deletions(-)

commit d804db79765c5f63cd0c1a1bc03ffa882d4c9410
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:54:32 2026 +0100

    z78: prescribe finite rotation functionals through recursively serviced proxy circles

 notes/z78/IE1_UNITS.md | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

commit 4b210bf6f80ad5cb4e0825014bfdfa7af1741574
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:51:19 2026 +0100

    z78: cubic induction barrier beyond full multiquadratic height surjectivity

 notes/z78/IE1_UNITS.md | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)

commit 161b10d9b05be159528d46b19efb1bb5a0c10f78
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:48:25 2026 +0100

    z78: bound residual squareclass kernel by cyclotomic and single-radical ranks

 notes/z78/IE1_UNITS.md | 9 +++++++++
 1 file changed, 9 insertions(+)

commit e4f140aa794b605f9d67ef4f71dbb962cae2cf80
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:43:34 2026 +0100

    z78: identify the two-component restriction and first-axis circle controls

 notes/z78/IE1_UNITS.md | 24 ++++++++++++++++++++++++
 1 file changed, 24 insertions(+)

Review:
# Second hostile pass: `notes/z78/IE1_UNITS.md` at bb6f8e72a

**Reviewer:** Claude (Anthropic, Opus family). I edited no files.

**Scope:** I read the full diff b4045874..bb6f8e72a, which is six commits touching one note plus the archived first review. I re-derived the rewritten §3a and the invariant package. I checked the rest of §§1–4 only for consistency with the first review.

## Verdict

**EXPORT: ACCEPT.** All the first-review fixes are in place (M3 sound, m7 only partly, which is acceptable).
- I found no remaining substantive gap in the axioms, in ¬ES(P), or in the scope.
- Both the Att induction and the proxy finite-support tree close.
- The six corrections below are minor wording clarifications. They can be applied at export and do not block it.

## Fix verification

| Fix | Status |
|---|---|
| **M1** | Done. Theorem A is displayed, and there is a four-item package and an edge table. The table includes the two new edge types: proxy line+circle, and the twist with both protected lists. |
| **M2** | Done. Clause 2 is now stated in extended form for every finite list in `k_n*/2`. `Att_n` is defined recursively with no reference to torus points. The constant-list lemma is a separate statement. |
| **M3** | Done and correct. The even-valuation argument for integral rotations holds at split places (`v(v₁)=v(v₂)`) and at inert places. The note rightly excludes 2, where Gaussian ramification gives `δ(i)=N(1+i)=2`, an odd valuation. At 2, restricting to boundaries {1, 5} is a valid sub-choice. |
| **m1** | Done: the dependency list is complete. |
| **m2** | Done: now "proxy pivot, end of §1". |
| **m3** | Done: `b₀`, `ζ`; 𝔐 defined; `F_prev` removed. `B` survives only in §4, which is separate. |
| **m4** | Done: `χ_q(−1)=0` stated, with unserviced proxies sent to the normalized-associate queue. |
| **m5** | Done: "a model with all these properties in which IE₁⁻ fails"; external invariants flagged as such. |
| **m6** | Done: triage scoped to ∛2 unit descent; a FRONTIER screen is proposed. |
| **m7** | Partly. The note is still not split, but the Theorem A/B headings separate the two results. Acceptable. |
| **m8** | Done: the STATUS delta carries non-PID, ¬L(Div), z77 §5, the target-4 TS clause, and "necessary, not sufficient". |
| **n1** | Done. |

## Does the Att induction close? Yes.

**Indexing.**
- In successor n, the proxies renew clauses 1–2 for `S_n` using only clauses 1–2 for `S_{n−1}`, at H.
- General circles in successor n also use only `S_{n−1}`.
- `k_{n−1}` is fixed once successor n−1 completes, and so are its completion's residue field and the marks. So the H-images of everything built later land in frozen data. Nothing circular.

**What a general circle can reach.**
- The only lever is the residual point at the new axis w, because constant parameters `a∈F` are units at every newly born punctured prime.
- Its marks are free at the top discrete places, and equal ζ·T_H at H.
- So the set of reachable vectors is exactly `A_top(a)+Att_{n−1}(sp_Hφ_H a) = Att_n(a)`.
- The constant-list lemma gives ψ(a) ∈ Att_n(a) for every finitely supported birth-prime functional ψ. Pick, at each layer, the primes of ψ born at that layer.
- Squareclass linearity holds because the value group ℤ[1/2] is 2-divisible, so square-normalized specialization is a homomorphism on squareclasses.
- The basis computation goes through:
  - primes born higher have S-unit residuals down to the dyadic place;
  - primes born lower are value-0 scalars until birth;
  - monomials equal a square times a scalar.
- Sign drops out because `(−1, N v)=0`.

**Clause 2 realizability.** For r∈U take δ(T) a nonsquare unit; this works at both split and inert r. Take squares on supp f \ U. Elsewhere the bits vanish automatically. At H, lift T_H by completeness and Hensel. The torus-square perturbation leaves δ unchanged mod squares.

**Clause 1 renewal.**
- Odd top places: the unit norm is surjective.
- Dyadic: u ≡ 1 (4) is a sum of two squares in ℤ₂.
- H: old clause 1 applies.

## Does the proxy finite-support tree close? Yes.

- A `b₀=1` proxy has all its prescriptions fixed by its scheduled data (the list, U, T_H). None depend on a defect, so only finitely many explicit places are needed and H is online.
- Defect-dependent choices occur only at general circles. Those use the two-option prefixes of z76, so branching stays finite.
- At infinite residue fields there are two classes and −1 is a quotient of norms. So the norms are everything, and the fibration-density argument stands.
- Dovetailing covers every list, since each list appears at a finite stage. The proxies' own new elements are covered too.
- Each clause-2 instance is created once, and its marks are then frozen.

## ¬ES(P) and scope

- Sorted bounds keep every entry in the bottom.
- `u=r+Pv` leaves `R/P` and `χ_P` unchanged.
- `P≡1 (840)` lies in 𝔐.
- I re-checked §4: C₃'s step coordinates, the `[3n,5n]` sum, the odd-k norm `(−1)^{k+1}=1`, and the descent `D∩F₀=C`. All correct.
- The scope wording is right: Theorem A is a countable non-PID Bézout union failing L(Div); Theorem B is a separate model with no Bézout, TS or QR claim; nothing is said about standard ES or about IE₁⁻ vs ES.

## Corrections (minor, apply at export)

1. **Constant-list lemma and §3.** State explicitly that `k_n* = F*·S_n*`. This follows recursively from finite support: clear the r-orders with old primes and the H-value with an old monomial, then recurse. So every punctured prime has a positive field associate with an S_n-unit residual, and the parity basis uses that associate (it need not be arithmetic). As written, §3's "arithmetic generators" and §3b's "When normalization exists…" read as if normalization might fail.
2. **§3a lead sentence.** Change `k`, `S` to `k_n`, `S_n`. Also say that the "top discrete marks" of `k_n` are the places of primes born in successor n−1, with 2 only at n=1; for n>1 the dyadic place is reached through the recursion.
3. **Package item 4 or the table.** Add one line: clauses 1–2 are statements about the final `k_n`, taken instance by instance. Each instance is created by one scheduled proxy and kept by frozen marks. Other edges only enlarge `k_n`.
4. **Theorem A.** Change "exactly two nonzero classes" to "exactly two nonzero squareclasses".
5. **Package item 2.** Change "old rational prime" to "old real-side prime", to avoid the number-theory reading.
6. **Proxy line and V.** Say once that `w(hV)>0`, so `q` reduces to `b`. This is implicit now.

None of these changes a result or a label. The note can be exported as Theorem A at HEADLINE (PROVED rel. §0) and Theorem B at BARRIER-BROAD (scoped). In the WAVES R line, list the cross-model reviews (Opus ACCEPT WITH FIXES, then this follow-up ACCEPT).
</code-review>
