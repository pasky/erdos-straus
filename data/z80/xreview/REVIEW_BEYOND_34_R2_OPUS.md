# Hostile cross-lab review — `notes/z80/BEYOND_34.md` §§12–14 (Round 2, commit 25eb836d2)

Reviewer: Claude Opus (Anthropic). The author is GPT-6.2 Astra. Internal review only, not refereed.
Scope: only the diff `6c9d497e1..25eb836d2`: §0 edits, §12 (QR, the Montgomery estimate, the synchronised-alphabet barrier and an Assessment), §13 (UB), §14 (PP) and the falsifier supplement. I checked §§1–11 only at the interfaces that Round 2 uses. They were reviewed separately and I did not re-audit them.

Sources checked:
* the Maynard Thm 1.1 excerpt in `sources/lit2026f/maynard-2006.06572-excerpt.txt`;
* `paper/sieve-limits-note.tex`: Def. `def:majorant`, Thm `noBcap`, Thm `main`, Lemma `budget`, Lemma `compmeas`, Thm `PLcap`;
* `EXSET_CHAR_FORCING.md` Prop 5.1′, `CAP_DOWN.md` Lemma 3.1, `EXCEPTIONAL_SHORT.md` Cor 3.2 and `notes/z75/ANALYTIC_BREAK.md` §0;
* the side branches `side-agent/z80-es-jugular` (`notes/z80/ES_JUGULAR.md`) and `side-agent/z80-r-below` (`notes/z80/R_BELOW_619.md`).

Arithmetic replay: a small exact script was run under `ulimit -v 6000000; timeout 600 uv run --offline --no-project python`. Its output is quoted in §6. Nothing was committed, and no master file was edited.

## 0. Verdict

**ACCEPT in substance.** I found no incorrect bound.
* QR (14) is correct, ineffective, and holds on the stated hypotheses.
* The Montgomery estimate is correct for every fixed C>2.
* The synchronised-alphabet barrier is correct and has the scope stated.
* UB (16) is correct. The Heath-Brown Cor 2 application is legitimate on all integers, and the bias of the squares is accounted for.
* The compmeas conditioning is legitimate: B is a pointwise-nonnegative element of V_𝒟 of level ≤ log N.
* PP is a correct, essentially trivial corollary.

There is **one mathematical statement fix (M1)**. The Montgomery-type hypothesis already implies Dirichlet GRH. So "the same convention about U and GRH" is vacuous, and the conclusion should be stated at the GRH scale. There is also one label fix (M2) and several form fixes (F1–F9).

## 1. §12 Theorem QR, bound (14)

**Changing the smoothness box via products of m primes.**
* With y=U^{10000}, m=⌊B′log₂y/log₃y⌋ and w_i=Y_i^{1/m}, every product of m distinct primes from [w_i,w_i^{1+δ}] lies in [Y_i,Y_i^{1+δ}].
* All primes are ≤ w₂^{1+δ}=y^{.475·1.0005/m}<z=2y^{1/m}, so they are >3 and divide L₀.
* The windows for i=1 and i=2 are disjoint, so d=d₁d₂ is squarefree and divides L₀. (The note's L=t₀L₀² is therefore more than needed; t₀L₀ suffices. This is harmless.)
* Distinct pairs (d₁,d₂) give distinct d by unique factorisation, and for a fixed t₀ distinct d give distinct r. So the τ-multiplicity step is no longer even needed. The note's use of it is harmless.
* Mertens gives Σ_{w<p≤w^{1+δ}}1/p=log(1+δ)+o(1), with w_i→∞ because log w_i ≍ log y·log₃y/log₂y.
* The ordered-choice deletion costs ≤m/w_i=o(1).
* Dividing by m! gives Σ1/d_i ≥ c₁^m/m! = (log y)^{−B′(1+o(1))}, since m log m ~ B′log₂y. ✓

**Maynard interface.** Maynard's Thm 1.1 requires Q₁Q₂²<x^{1−100ε}, Q₁¹²Q₂⁷<x^{4−100ε} and Q₁²⁰Q₂¹⁹<x^{10−100ε}, and gives ≪_{a,ε,A} x/(log x)^A for every A.
* With Q₁=48Y₁^{1+δ} and Q₂=2Y₂^{1+δ} the exponents are .98049, 3.68684 and 9.62981 (exact rational replay). The smallest slack is .0195, so ε≈1.9·10⁻⁴ works. ✓
* The main term is ≫(y/log y)(log y)^{−2B′(1+o(1))}. Taking Maynard's A>2B′+2 makes the absolute error smaller. This is legitimate because A is arbitrary at fixed (a,ε). ✓
* As before, the family (jd₁,d₂) sits inside Maynard's full double sum. ✓
* The number of values of t₀ is ≤2y/(Y₁Y₂), so one t₀ carries y^{.505−o(1)} distinct r, which is ≥y^{.504}. ✓

**Rate.** We have log(1+e*) ≤ log L+O(1) ≤ 2ψ(z)+log y+O(1). Also log z=(10000/B′)(1+o(1))·log U·log₃U/log₂U, using log₂y=log₂U+O(1) and log₃y=log₃U+o(1). So c=10000/B′, with B′ arbitrary. ✓ The constant factor 2 and the log y term are o of the exponent.

**Interfaces with §§10–11.** These are unchanged.
* log D₀ ≪ log y+θ(z)=U^{o(1)}=o(U), so D₀<R, and the Linnik/GRH q-height is as before.
* (L,Q)=1 still holds, because q≡−1 at every odd prime ≤z.
* P ≥ y^{.503} and l ≤ U³ still give the large-sieve exponent <.997.
* The small-nonresidue alternative costs O(log y)=o(z).

Effectivity is correctly stated: the result is ineffective through Maynard/Siegel–Walfisz, and Z75 retains the effective bound. The Z75 quote 4e*(p)+3≤√(4p/3) at p≡1 (8) matches `notes/z75/ANALYTIC_BREAK.md` §0. ✓

**Debate point (no fix needed).** "The fixed-ratio Dickman argument does not apply" is true. Hildebrand's uniform Ψ(x,y)~xρ(u) would apply in this range (log z ≫ (log₂y)^{5/3+ε}). The elementary m-prime construction is preferable anyway, since it gives squarefree d | L₀ directly. The rate (14) is optimal *for this route*: a log-power Maynard saving forces harmonic mass ≥(log y)^{−O(1)}, hence u log u ≪ log₂y with u=log Y/log z. That is exactly (15).

## 2. §12 Montgomery estimate (C>2)

**Hypothesis.** The hypothesis is a weakening of Montgomery's ψ-conjecture: it restricts to 24|m and m≤x^θ with θ<1, and uses an x^κ√(x/m) error. Passing from ψ to π costs only prime-power terms of size x^{o(1)}(√x/m+1). These are ≤x^κ√(x/m). The restriction θ<1 keeps the hypothesis away from the near-x range in which Friedlander–Granville limitations live. ✓

**Arithmetic.**
* With z=(log y)^C and m=⌈a log y/log z⌉, we get w=y^{a/m}≤z and log w=log z−o(1).
* Every product of m distinct primes from [w/2,w] lies in [y^a2^{−m},y^a]=y^{a−o(1)}.
* The harmonic mass is (c₀/log w)^m/m!=y^{−a/C−o(1)}, because m(log m+log log w)=m(log₂y+O(1)) and m·log₂y→(a/C)log y. ✓
* Deletion costs m/(w/log w)→0, since C>1. ✓
* The modulus satisfies 24d≤24y^a<x^{(1+a)/2}. At κ=(1−a)/8 the relative error is x^{κ+(a−1)/2+o(1)}→0, uniformly in d. ✓
* There are ≤y^{1−a+o(1)} values of t₀, and no multiplicity arises. So one t₀ carries y^{a(1−1/C)−o(1)} primes. After colour halving this is ≥y^{1/2+4γ}, because a(1−1/C)>1/2+5γ. Such a,γ exist iff C>2: for example C=5/2, a=.95, γ=.009 gives .57>.545, checked exactly. ✓
* Large sieve: l≤U³ and A₀>20/γ give log(4l)/log y<γ/6. Hence log(P/4l)/log 2y>1/2+3γ and the bad-conductor count is ≤M^{1−6γ+o(1)}·y^{O(1)}≤M^{1−5γ}. ✓
* Slots: V=exp(C₀U) with C₀>2C₁/γ (where C₁ is the q-height constant) supplies V^{1−γ} candidates per slot even in the harmful-Siegel case. The union bound Σ(kV^{−4γ})^j=o(1) then holds. Fourier inversion needs P≫U², which holds. ✓
* The cap is O(z+log y)≪_C(log U)^C. ✓

"Ordinary EH does not suffice" is correct: the total error x/(log x)^A swamps the main sum y^{1−a/C}. "GRH alone does not suffice" is also correct: GRH gives a √x error per modulus, so a<1/2 and therefore a(1−1/C)<1/2.

**M1 (mathematical, statement).** The hypothesis implies Dirichlet GRH.
* Take a primitive χ mod q and the fixed modulus m=24q. For each reduced class mod m the error is O(x^{1/2+κ}).
* Twisting by χ (which is nonprincipal mod m) gives Σ_{p≤x}χ(p) ≪_m x^{1/2+κ}. Partial summation then gives L(s,χ)≠0 for Re s>1/2+κ, for every κ>0.
* So under this hypothesis U=log₂R is always available, and the unconditional-U reading is redundant.

**Exact fix.** Replace "with the same convention about U and GRH" by: "The hypothesis implies Dirichlet GRH (fix m=24q), so U=log₂R and log(1+e*)≪_C(log₃R)^C." In the §0 STATUS delta, replace "(log U)^{2+ε}" by "(log₃R)^{2+ε} under the stated Montgomery-type hypothesis (which implies Dirichlet GRH)".

**Form (F2).** Cite Montgomery (*Topics in Multiplicative Number Theory*, LNM 227, 1971, or the 1976 problem list). Then resolve three notation clashes:
* m is used both for the hypothesis modulus and for the number of prime factors;
* a is used both for the residue class and for the exponent 0<a<1;
* C₀ means the V-exponent here but is the q-height constant in §11, where V=exp(CU).

## 3. §12 barrier for the synchronised squarefree alphabet

**Counting argument.** There are ≤τ(L) primes r with r−1|L, hence ≤2^{τ(L)} subset products. So covering a positive fraction of a group of size G needs τ(L)≥log₂G−O(1). ✓ The packet actually needs (r−1)/4 | L_o, that is r−1|4L; this changes τ by O(1) only. (Toy replay: L=2⁴3²·5·7·11 has τ=120 and 45 such primes.)

**Consequence.** Wigert's bound then gives log L ≫ log U·log₂U. ✓ This is consistent with QR, since z ≫ log U log₂U, and with the Montgomery estimate (C>2>1). The gap between "log U·log₂U" and "(log U)^{2+}" is honestly left open.

**Precision (F9).** log φ(D′) ≫ kU ≍ U² (k slots, each v_i>√V), not merely ≫U. This is harmless.

**Scope.** The barrier covers the full-support certificate with e*≪L only. The disclaimer about single-target and unbounded-power schemes is correct and must stay.

The Assessment on paying only on binary digits matches §6: the overflow is (L_o v_p(g)−c_p)⁺, and the cap is half of it. It is nonzero at c_p=1 because v_p(g) is odd there. It also matches `CAP_DOWN.md` Lemma 3.1, reading δ_p=0 with x=K_m. No bounded-cap claim is made, which is correct.

## 4. §13 Theorem UB

**(17).** The pairing count gives E S^{2k}≤(2k−1)!!m^k. An exact replay with four primes and k=1,2,3 (Legendre symbols, zeros included, full CRT period) gives 3.67≤4, 33.96≤48 and 432.7≤960. The exponent −(A−1)/(2A) follows from k≈log N/(2A log₂N) and m≍(log N)^A/log₂N. ✓

**Heath-Brown Cor 2 on all integers.**
* Write n=tab² with ta the squarefree kernel. Deleting or reinstating the s|b changes S by at most ω_{>Y}(b)=o(m).
* For s≡3 (4) and odd a, (a/s)=(−1)^{(a−1)/2}(s/a). The sign depends on a only. ✓ The twist by (t/s) has modulus 1.
* Cor 2 holds for arbitrary coefficients on n≤(2Y)^j≤X, with the outer variable a odd squarefree. Its energy Σ_{n₁n₂=□}|c_{n₁}c_{n₂}| is at most the number of 2j-tuples with even multiplicities, ≤(2j)^jm^j.
* Markov with threshold ηm/2 gives N^{2ε}·2X·(8j/η²m)^j. ✓ This matches `EXSET_CHAR_FORCING.md` Prop 5.1′, whose inner variable was primes; there the outer variable was the prime p and here it is the kernel a.
* We have (C_η(log N)^{1−A})^j=X^{−(A−1)/A+o(1)} uniformly. The floor of j costs (log N)^{A−1}, and the case X<2Y is trivial. ✓
* The sum Σ_{b≤√N}(N/b²)^{1/A}≍_A N^{1/2} needs A>2, which is stated. ✓
* Sharpness: squares give S≥m−o(m), so the biased population is ≍N^{1/2+o(1)}. ✓

So (16) is correct, and E_unb is honestly called a containment. Priority of this standard Heath-Brown application to all integers has not been checked. Say so.

**Natural bias and conditioning of the compmeas law.**
* Lemma `compmeas` (LP duality) gives ρ∈𝓜(𝒜) with E_ρf≤e^{Cλ^{3/4}}E_Uf for every f∈V_𝒟 with f≥0 pointwise. Signed class coefficients are allowed.
* B=(S/ηm)^{2k} is pointwise ≥0. Each tuple term is (n/Q_τ)·1[(n,Q′_τ)=1], a signed combination of classes mod squarefree products of ≤2k bias primes. Its charged level (primes >W only, each counted once) is ≤2k log 2Y≤log N.
* So B∈V_𝒟 once 𝒟 contains those products and the coarsened majorant moduli, and λ≍log N.
* Hence ρ(|S|≥ηm)≤e^{C(log N)^{3/4}}N^{−(A−1)/(2A)+o(1)}=o(1). Conditioning costs a factor 1+o(1) on every nonnegative f∈V_𝒟, where ρ depends on 𝒟. ✓ One may take 𝒟 to be all divisors of M′ of level ≤λ, so "all nonnegative tests of that level" is accurate for period M′.
* The balanced-avoider barrier follows. ✓

The level and nonnegativity therefore do permit adding the sign statistic. The question in the brief is answered in the affirmative.

**Simpler route (form).** The "Equivalently" sentence is actually the cleaner proof. ν+B majorises all of 𝒜, so noBcap alone gives E ν ≥ e^{−Cλ^{3/4}}−E B, with no compmeas and no conditioning. As the note says, this holds for Haar means. Under Thm `main`'s (A2), the class-coefficient sum of B is about η^{−2k}(2Y)^{2k}=N^{1+o(1)}, which may exceed N unless k is shortened by a constant factor. The compmeas route avoids that, because only ν is coarsened.

**Asymptotic caveat (Assessment).** noBcap's C absorbs 2W with log W≈10¹⁰. The o(1) needs Y=(log N)^A≫W, that is, astronomically large N. Below that, the T-primes are uncharged and the inequality is vacuous. This matches noBcap's own nature and needs no fix. A one-clause mention would forestall misreading.

**Unit-law qualifications.** Under E* the signs are ±1, independent and symmetric, so (17) holds verbatim. The factor exp(S*(λ)) with S*=Cλ^{3/4}(log λ)^{3/4} is the reviewed one. Cλ^{3/4} for all mixtures is pointer-level in `sieve-limits-note`, and the note correctly does not rely on it.

**F5.** "Bounded cofactors as in PLcap" should read "moduli with G≤P(G)^{1+B}, B fixed (PLcap)".

**M2 (label).** The closing sentence about the fibre word-square model is asserted with only a one-line sketch:

> "fixing n mod ∏s leaves fresh pivots independent … same 2/3 floor"

It sits inside the PROVED UB block.

**Exact fix.** Prefix it with "Assessment:" or move it to the §13 Assessment paragraph, keeping "only for that model and hypotheses".

## 5. §14 Corollary PP and the falsifier supplement

**PP.** The proof is correct and trivial: the absolute numerator from P divided by P_I, with the loss bounded by (log H)^C. The dyadic case is fine. For short intervals, Huxley with H≥x^{7/12+ε} gives log x≤(12/7)log H, so P_I≫H/log H. ✓

The scope disclaimers (no sparse prime population, no prime values, possibly no primes in a shifted interval) are correct.

**F4.** `EXCEPTIONAL_SHORT.md` Cor 3.2 states BHP H≥2x^{0.525} as its primary input, with Huxley only in parentheses. Either cite Cor 3.2(a) for the wider range or say "Huxley (as recalled parenthetically in Cor 3.2)". Both are checked only from secondary sources there; carry that caveat.

**Falsifier supplement (F6).** The note says:

> "The sieve-limits square-base law … need not stay biased on a growing set of primes"

This is inaccurate. The ρ of §13 is the LP-dual law of `compmeas`, not the square-base sequential law. Also, §13 does not merely say ρ "need not stay biased": it proves ρ(biased)=o(1). The square base fixes residues only at primes ≤W, whereas T⊂(Y,2Y] with Y≫W.

**Exact fix.** "The compmeas comparison law of §13, although supported on periodic avoiders, gives mass o(1) to residues biased on 𝒯 (𝒯 lies above the square-base primes ≤W). This is what lets the balanced restriction be added."

## 6. Replay output (exact rationals)

```
Maynard 1 2 0.98049 < 1 slack 0.01951
Maynard 12 7 3.6868425 < 4 slack 0.3131575
Maynard 20 19 9.6298125 < 10 slack 0.3701875
a(1-1/C)= 0.57 > 0.545 True
k 1 E S^2k 3.67 bound 4 ;  k 2 33.96 bound 48 ;  k 3 432.68 bound 960
tau(L) 120 #primes r, r-1|L 45
```

These are arithmetic checks only; none of them is a check of an asymptotic input.

## 7. Form (baseline review of the diff)

* **F1 (§0, required by AGENTS.md §2).** The Result, Label and Triage lines were not updated. The Result line still names only P and QB. The Label line lacks Mertens/PNT for QR, the CONDITIONAL Montgomery hypothesis, Heath-Brown Cor 2, reciprocity, `compmeas` for UB, and Huxley/BHP for PP.
  * Triage should read "RECORD (QR); BARRIER-SCOPED (§12 synchronised-alphabet barrier, §13 UB floor); DATA (PP)".
  * The STATUS delta's UB sentence belongs in a FRONTIER §6 line, not STATUS. It is a scoped barrier, as the delta itself says.
  * Also give (14) explicitly in the delta: "log(1+e*)≤U^{(c+o(1))log₃U/log₂U} for every fixed c>0".
* **F2.** The notation clashes listed in §2. Also, k and j in §13 reuse §11 symbols with new meanings; add a one-line reset as §10 does.
* **F3.** `ES_JUGULAR.md` and `R_BELOW_619.md` are cited without a path, and neither exists in this tree. Give them as `notes/z80/ES_JUGULAR.md` (branch `side-agent/z80-es-jugular`) and `notes/z80/R_BELOW_619.md` (branch `side-agent/z80-r-below`), or wait for the merge. The cited content (Thm A: arrows to the least nonresidue; §§3–4: nonnegative centred moments at a greater level) matches.
* **F7.** "Use these families in the **signed** Maynard count": this means the inclusion–exclusion indicator, while the errors are absolute. Say "the inclusion–exclusion count of §10 with absolute Maynard errors".
* **F8.** §12 "this regime m log m=O_{B′}(log₂y)": it is in fact ~B′log₂y. Stating that asymptotic makes the rate derivation one line.
* **F9.** See §3: log φ(D′) ≫ U², not just ≫ U.
* The 2-line §0 Review edit ("Round 2 §§12–14: cross-review owed") is correct. After this review it can read "cross-model (Anthropic Opus, `data/z80/xreview/REVIEW_BEYOND_34_R2_OPUS.md`, ACCEPT in substance; M1–M2 and F1–F9 requested)".
* No master file was touched, which is correct for a lane commit. No new certificate is needed, because §§12–14 make no finite claims.

## 8. Summary of exact fixes

| id | kind | location | fix |
|---|---|---|---|
| M1 | math (statement) | §12 Montgomery para; §0 STATUS delta | The hypothesis implies Dirichlet GRH (m=24q fixed), so the conclusion is log(1+e*)≪_C(log₃R)^C. Delete "same convention about U". Delta: "(log₃R)^{2+ε}". |
| M2 | label | end of §13 "Balanced comparison" | Mark the word-square fibre 2/3 sentence as Assessment, or supply a proof. |
| F1 | form | §0 | Update Result, Label and Triage. Move UB to a FRONTIER §6 line. State (14) explicitly. |
| F2 | form | §12 Montgomery, §13 | Rename m, a and C₀. Cite Montgomery. Add a symbol reset. |
| F3 | form | §13 Assessment | Give paths and branches for ES_JUGULAR and R_BELOW_619. |
| F4 | form | §14 | Fix the Cor 3.2 attribution (BHP primary, Huxley parenthetical, both from secondary sources). |
| F5 | form | §13 units | "G≤P(G)^{1+B}" instead of "bounded cofactors". |
| F6 | form (accuracy) | falsifier supplement | Replace the square-base sentence as in §5. |
| F7–F9 | form | §12 | "Signed", m log m~B′log₂y, and log φ(D′)≫U². |

No other mathematical fix is required. QR, the Montgomery estimate (C>2), the barrier, UB (16), the compmeas conditioning and PP all stand on their stated hypotheses.
