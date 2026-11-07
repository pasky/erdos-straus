# Literature verification: independence, arithmetic hierarchy, and proof barriers

**Scope.** This is a source audit, not a claim that every desired primary-source detail was located. “VERIFIED” means the cited primary source directly supports the quoted claim; “PARTLY” means the source supports only part of the requested formulation or a bibliographic detail remains unresolved; “NOT FOUND” means no qualifying primary-source quotation/theorem locator was verified here. Quotes are verbatim and kept short. Where a theorem number could not be verified, it is explicitly omitted.

## 1. Paris–Harrington and Goodstein

### Paris–Harrington
- **Reference:** Jeff Paris and Leo Harrington, “A Mathematical Incompleteness in Peano Arithmetic,” in *Handbook of Mathematical Logic*, ed. J. Barwise, North-Holland, 1977, pp. 1133–1142 (chapter D.8, §2 in some citations). Primary author-hosted scan: https://www.karlin.mff.cuni.cz/~krajicek/ph.pdf
- **Quote:** “We define a certain theory T in 2.1 and then show Con(T) →→ Con(PA) is provable in PA.” (scan text; the displayed arrow is a relative-consistency relation.)
- **Claim/verdict:** **PARTLY.** The paper establishes the Paris–Harrington finite Ramsey strengthening unprovable in PA and relates its consistency strength to PA. Its natural formal statement is Π⁰₂. I did not verify a numbered theorem in the scan establishing the exact requested phrasing “PA + PH proves Con(PA)” or “1-Con(PA)”; do not cite that wording as a theorem without checking the chapter’s notation and proof. The ordinary metamathematical point is that PA proves the implication from the PH principle to the relevant consistency assertion; it does not make PA inconsistent.
- **Π⁰₂ locator:** None verified in the primary scan during this audit; classification as Π⁰₂ is standard but should be labeled an external/formalization description, not a quote attributed to a theorem number here.

### Goodstein
- **Reference:** Laurie Kirby and Jeff Paris, “Accessible independence results for Peano arithmetic,” *Bulletin of the London Mathematical Society* 14 (1982), 285–293. DOI: https://doi.org/10.1112/blms/14.4.285
- **Quote/locator:** The article’s theorem text and theorem number were not verified from an accessible primary copy in this audit.
- **Verdict:** **PARTLY.** This is the correct foundational citation for the independence of the Goodstein theorem and related accessible statements. The Goodstein termination assertion is commonly classified Π⁰₂ (∀n∃m, with a primitive-recursive descent predicate), not Π⁰₁. Do not conflate the statement “every Goodstein sequence terminates” with a fixed finite computation or with a Π⁰₁ consistency sentence.

## 2. Friedman: Π⁰₁ statements and set-theoretic strength

### Boolean Relation Theory / SMAH
- **References:** Harvey M. Friedman, *Boolean Relation Theory and Incompleteness*, ASL Lecture Notes in Logic 55, Cambridge University Press, 2021 (earlier manuscript/book versions circulate under 2011); bibliographic record: https://doi.org/10.1017/9781108586070
- **Requested assertion:** A Π⁰₁ sentence provably equivalent over ACA′ or RCA₀ to Con(SMAH).
- **Quote/theorem number:** No qualifying primary-source quotation and theorem number verified in this audit.
- **Verdict:** **NOT FOUND** for the exact formulation. The wording is highly formalization-sensitive (base theory, coding, and which SMAH axiom); cite a page/theorem from the book before using it. It is not safe to infer a PA-independent concrete sentence merely from the title or from a consistency-strength comparison.

### Finite forms / PA independence / other Friedman claims
- **References to check:** Friedman’s writings on finite forms of Kruskal’s theorem and “Pi01 incompleteness”; author archive: https://u.osu.edu/friedman.8/ (research papers). A useful primary-related manuscript is *Aspects of Gödel Incompleteness*: https://u.osu.edu/friedman.8/files/2021/09/IncompChinese090821.pdf
- **Quote:** The manuscript says: “T is essentially incomplete in the sense that no consistent extension of T by finitely many sentences is complete.”
- **Verdict:** **PARTLY.** This quotation concerns essential incompleteness generally; it does not verify a named Friedman finite-Kruskal Π⁰₁ statement independent of PA. The requested examples, exact formulas, and refereed status were not verified. Treat “Adjacent Ramsey” and “order invariant graphs” as unverified leads here, not established PA-independence results.

## 3. MRDP and Diophantine encodings

### MRDP and fragments
- **References:** Yuri Matiyasevich, *Hilbert’s Tenth Problem*, MIT Press, 1993; Martin Davis, Hilary Putnam, Julia Robinson, and Yuri Matiyasevich, MRDP foundational papers. Andrey Gaifman and Costas Dimitracopoulos, “Fragments of Peano’s Arithmetic and the MRDP Theorem,” in *Logic and Algorithmic*, Monographie de l’Enseignement Mathématique 30 (1982), 187–206.
- **Quote:** A later source describing the fragment result states: “Gaifman and Dimitracopoulos [20] showed that I∆₀ + ∀x∃y 2ˣ=y does prove MRDP.” Source: https://elib.mi.sanu.ac.rs/files/journals/flmt/9c/flmn70p473-481.pdf
- **Theorem number/verdict:** **PARTLY.** The fragment result is supported by the quotation, but the original Gaifman–Dimitracopoulos theorem number was not verified. The standard MRDP result says recursively enumerable sets are Diophantine; hence a Π⁰₁ sentence’s negation (a Σ⁰₁ assertion) can be represented as existence of a solution, and its truth is equivalent to non-solvability. Exact equivalence in a weak formal theory requires specifying the chosen coding and formalization.

### Con(ZFC) and an explicit equation
- **Reference:** The MRDP theorem plus a chosen Gödel coding of ZFC proofs.
- **Claim/verdict:** **PARTLY.** In principle, “there is no ZFC proof of contradiction” is Π⁰₁ and can be transformed effectively into non-solvability of a Diophantine equation. The exact explicit polynomial depends on the proof predicate, universal Diophantine representation, and coding choices. No particular polynomial or primary-source theorem number was verified here; do not describe one as *the* canonical equation.

### Jones universal equation
- **Reference:** James P. Jones, “Universal Diophantine equation,” *Journal of Symbolic Logic* 47(3) (1982), 549–571. DOI: https://doi.org/10.2307/2273586
- **Quote/theorem number:** Not verified from a primary-source page in this audit.
- **Verdict:** **PARTLY.** Correct bibliographic lead for a universal Diophantine equation. Exact equation, parameter count, and theorem locator require checking the article itself.

## 4. Busy Beaver independence machines

### Yedidia–Aaronson
- **Reference:** Adam Yedidia and Scott Aaronson, “A Relatively Small Turing Machine Whose Behavior Is Independent of Set Theory,” arXiv:1605.04343 (2016). https://arxiv.org/abs/1605.04343
- **Quote/locator:** Exact abstract quotation and machine-state count were not extracted from the arXiv primary source in this audit.
- **Verdict:** **PARTLY.** The paper’s construction is commonly reported as a 7,910-state, 2-symbol machine whose halting behavior is independent of ZFC, conditional on consistency/appropriate soundness assumptions. The 748-state construction is a later result, not the Yedidia–Aaronson number.

### O’Rear / 748; subsequent claims
- **Reference:** Scott Aaronson, “The Busy Beaver Frontier,” primary author PDF: https://www.scottaaronson.com/papers/bb.pdf
- **Quote:** “Theorem 7 (O’Rear) There’s an explicit 748-state Turing machine that halts iff ZF is inconsistent. Thus, assuming ZF is consistent, ZF cannot prove the value of BB(748).”
- **Verdict:** **VERIFIED** for the exact theorem text as stated by Aaronson, with the crucial qualification “Assuming O’Rear’s construction is sound” in the preceding sentence.
- **Riebel / “BB(748)” and lower counts:** A thesis/report titled *The Undecidability of BB(748)* is a lead, but this audit did not verify its institutional repository record or theorem. Search results report a 745-state construction (Riebel, 2023), which conflicts with a simple claim that 748 remains the best count. **PARTLY:** do not assert “BB(643)” or “BB(432)” as independently established without an exact primary construction and machine model. State counts depend on the formal machine convention.

## 5. Gödel II, Π⁰₁ consequences, and non-implication

### Standard elementary implications
- **References:** Hajek and Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993; Per Lindström, *Aspects of Incompleteness*, Lecture Notes in Logic 10, ASL/Cambridge University Press, 1997 (reissued 2017). A stable book record: https://doi.org/10.1017/CBO9780511623764
- **Theorem numbers/quotes:** Not verified in the primary books in this audit.
- **Verdict:** **PARTLY.** With the standard arithmetization, if φ is Π⁰₁ and PA ⊬ φ, then PA is consistent: if PA were inconsistent, it proves every sentence. This implication is elementary and does **not** use Π⁰₁-ness. More substantively, if PA ⊢ ¬φ for a true Π⁰₁ φ, Σ⁰₁-completeness gives a contradiction to truth; hence a true Π⁰₁ sentence unprovable in PA is independent when PA is sound. Gödel II says a consistent, suitably axiomatized extension of elementary arithmetic cannot prove its own standard consistency.

### Does every true independent Π⁰₁ sentence imply Con(PA)?
- **Verdict:** **NOT FOUND / do not claim yes.** “PA ⊬ φ implies Con(PA)” is a metatheoretic implication, not a PA-provable implication φ → Con(PA). The latter is a distinct and generally unjustified strengthening. A supposed Π⁰₁-conservative extension PA+φ for a Π⁰₁ φ cannot be conservative for all Π⁰₁ sentences, since it proves φ itself; terminology may instead mean conservativity for a restricted class or relative to a different base.
- **Guaspari lead:** David Guaspari, “Partially conservative extensions of arithmetic,” *Transactions of the American Mathematical Society* 254 (1979), 47–68. Exact theorem number and a counterexample matching the requested “does not imply consistency” formulation were not verified. **PARTLY.** Avoid attributing that conclusion to Guaspari absent theorem-level checking.

## 6. RH and arithmetic hierarchy

### Lagarias criterion
- **Reference:** Jeffrey C. Lagarias, “An Elementary Problem Equivalent to the Riemann Hypothesis,” *American Mathematical Monthly* 109(6) (2002), 534–543. Author-hosted/arXiv record: https://arxiv.org/abs/math/0008177
- **Quote:** The paper’s Theorem 1.1 is the elementary divisor-sum criterion: RH is equivalent to the inequality σ(n) ≤ Hₙ + exp(Hₙ) log(Hₙ) for every integer n ≥ 1 (with the paper’s stated exceptional convention).
- **Verdict:** **PARTLY.** The equivalence is standard and Theorem 1.1 is the relevant locator. The all-n inequality has a universal number-quantifier formulation and can be represented as Π⁰₁ after effective arithmetic coding. The theorem is not itself presented as a formal-arithmetic Π⁰₁ classification; distinguish the elementary criterion from a proof-theoretic formalization.

### Davis–Matiyasevich–Robinson / RH and Π₁
- **Reference:** Martin Davis, Yuri Matiyasevich, and Julia Robinson, “Hilbert’s Tenth Problem: Diophantine Equations: Positive Aspects of a Negative Solution,” *Proceedings of Symposia in Pure Mathematics* 28 (1976), 323–378. DOI: https://doi.org/10.1090/pspum/028/0439737
- **Requested section/quote:** No exact section or verbatim primary-source passage verified.
- **Verdict:** **NOT FOUND** for the asserted exact RH equivalence in this source. Lagarias supplies a Π⁰₁-style criterion; the Davis–Matiyasevich–Robinson article is a general Diophantine/MRDP source, not verified here as presenting an RH equivalence.
- **Classification caution:** Goldbach and twin-prime conjectures in their usual forms are Π⁰₂ (∀n∃witness), not Π⁰₁. A positive universal counterexample-free condition can sometimes be rearranged only if the property has a bounded witness test; do not label arbitrary open conjectures Π⁰₁.

## 7. Proof lengths and finite consistency

### Pudlák
- **Reference:** Pavel Pudlák, “On the length of proofs of finitistic consistency statements in first-order theories,” in *Logic Colloquium ’84*, Studies in Logic and the Foundations of Mathematics 122 (1986), 197–233.
- **Quote/theorem number:** No exact primary-source theorem text or locator verified.
- **Verdict:** **PARTLY.** This is the correct foundational reference on lengths of proofs of finite-consistency statements. Claims of a lower bound such as n^ε must specify theory, proof system, encoding, and whether “length” is number of symbols or proof lines; no blanket bound was verified here.

### Parikh
- **Reference:** Rohit J. Parikh, “Existence and Feasibility in Arithmetic,” *Journal of Symbolic Logic* 36(3) (1971), 494–508. DOI: https://doi.org/10.2307/2270563
- **Quote/theorem number:** Not verified from the primary article.
- **Verdict:** **PARTLY.** Parikh’s theorem concerns bounds on provably total functions of weak arithmetic theories; it is not by itself a generic lower bound on proof lengths of arbitrary true Π⁰₁ instances. Avoid claiming it establishes Pudlák’s n^ε result.

## 8. Bounded arithmetic and number theory

### Buss and cryptographic consequences
- **References:** Samuel R. Buss, *Bounded Arithmetic*, Bibliopolis, 1986 (doctoral thesis/monograph); Jan Krajíček and Pavel Pudlák, “Some consequences of cryptographical conjectures for S¹₂ and EF,” *Information and Computation* 140 (1998), 82–94.
- **Quote/theorem numbers:** Not verified from the primary texts. In particular, the requested Buss Chapter 5 theorem number is not safely supplied here.
- **Verdict:** **PARTLY.** Buss’s witnessing theorem is a core result linking proofs in S¹₂ to polynomial-time functions, but theorem numbering varies between thesis and published versions. Krajíček–Pudlák is a relevant cryptographic independence/feasible interpolation paper; no precise “main theorem” statement verified in this audit.

### Jeřábek and weak arithmetic number theory
- **Reference:** Emil Jeřábek, “Abelian groups and quadratic residues in weak arithmetic,” *Journal of Symbolic Logic*  sketched bibliographic lead; author publication page/search needed for exact volume/pages.
- **Quote/theorem number:** Not verified.
- **Verdict:** **NOT FOUND** for the requested theorem numbers and the exact theory “T⁰₂ + Count₂.” Do not cite a specific formal strength until the paper and notation are checked.

### Primes, Bertrand, AKS
- **References/leads:** Paris, Wilkie, and Woods, “ provability of the pigeonhole principle and the existence of infinitely many primes,” *Journal of Symbolic Logic* 53 (1988) (exact title/locator requires checking); Jalali–Ježil 2025/26 AKS claim not verified.
- **Quote/theorem number:** None verified.
- **Verdict:** **NOT FOUND** for “S¹₂ or IΔ₀ proves infinitude of primes / Bertrand” in the exact requested formulations, and **NOT FOUND** for the 2025/26 AKS result. These are theory- and coding-sensitive; do not infer that all elementary number theory is provable in weak theories.

### Aaronson survey
- **Reference:** Scott Aaronson, “Is P versus NP formally independent?” (2003), author-hosted essay/paper; locate via https://www.scottaaronson.com/papers/ for definitive version.
- **Quote/theorem number:** Not checked in a primary copy.
- **Verdict:** **PARTLY.** Relevant for meta-level discussion of independence and barriers, but not a theorem proving independence of particular Π⁰₁ number-theory statements.

## 9. Barriers and unprovability analogies

### Sieve parity barrier
- **References:** John Friedlander and Henryk Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57 (2010); Selberg sieve literature.
- **Quote/theorem number:** No theorem in the book verified here that states the parity barrier as a formal impossibility theorem.
- **Verdict:** **PARTLY.** The parity problem is a limitation of broad classes of sieve methods, not an unconditional theorem that a specific number-theoretic conjecture is unprovable in arithmetic. Exact theorem/section and hypotheses are necessary.

### Relativization and natural proofs
- **References:** Theodore Baker, John Gill, and Robert Solovay, “Relativizations of the P=?NP Question,” *SIAM Journal on Computing* 4(4) (1975), 431–442, DOI https://doi.org/10.1137/0204037; Alexander Razborov and Steven Rudich, “Natural proofs,” *Journal of Computer and System Sciences* 55(1) (1997), 24–35, DOI https://doi.org/10.1006/jcss.1997.1494.
- **Quote/theorem number:** Not verified from primary article text here.
- **Verdict:** **PARTLY.** These are complexity-theoretic barriers, not direct formal barriers to number-theoretic proof. Relativization establishes that oracle techniques cannot resolve P vs NP in general; natural-proofs limitations are conditional on pseudorandom-function assumptions.

### Razborov bounded arithmetic
- **Reference:** Alexander A. Razborov, “Unprovability of Lower Bounds on Circuit Size in Certain Fragments of Bounded Arithmetic,” *Izvestiya: Mathematics* 59(1) (1995), 205–227. Primary PDF: https://www.karlin.mff.cuni.cz/~krajicek/razborov95.pdf
- **Quote:** “We show that if strong pseudorandom generators exist then the statement ‘α encodes a circuit of size n(log n) for SATISFIABILITY’ is not refutable in S²₂(α). For refutation in S¹₂(α), this is proven under the weaker assumption of the existence of generators secure against the attack by small depth circuits…”
- **Theorem number/verdict:** **VERIFIED** for the abstract’s conditional unprovability claim. The abstract does not give a theorem number; none is invented here. This is about formalized circuit lower bounds, not a direct theorem about number-theoretic conjectures.

### Krajíček forcing
- **Reference:** Jan Krajíček, *Forcing with Random Variables and Proof Complexity*, Cambridge University Press, 2011.
- **Quote/theorem number:** No theorem-level primary quotation verified.
- **Verdict:** **PARTLY.** Relevant background for constructing models and proof-complexity independence phenomena; not verified here as a result about number theory.

---

## 15-line summary
1. Paris–Harrington is a natural PA-independent finite Ramsey principle; exact requested Con(PA) wording needs notation-level checking.
2. Its usual arithmetic-hierarchy classification is Π⁰₂; the primary theorem locator was not verified here.
3. Kirby–Paris (1982) is the Goodstein independence reference; termination is Π⁰₂, not Π⁰₁.
4. Friedman’s exact ACA′/RCA₀ equivalence to Con(SMAH) remains unverified at theorem level.
5. MRDP converts recursively enumerable/Σ⁰₁ predicates to Diophantine solvability; weak-theory details need exact formalization.
6. A Con(ZFC) Diophantine equation exists effectively, but no unique canonical polynomial is verified here.
7. Yedidia–Aaronson’s 7,910-state machine and later smaller machines must not be conflated.
8. Aaronson quotes O’Rear’s explicit 748-state machine halting iff ZF is inconsistent, conditionally on construction soundness.
9. PA ⊬ φ implies Con(PA) only as a metatheoretic implication from consistency; φ need not prove Con(PA).
10. No verified theorem here says every true independent Π⁰₁ sentence proves a consistency statement.
11. Lagarias Theorem 1.1 gives an RH-equivalent all-n divisor inequality, which admits Π⁰₁-style coding.
12. Goldbach and twin primes in ordinary formulations are Π⁰₂, not Π⁰₁.
13. Pudlák and Parikh are relevant to proof lengths/feasibility, but no numeric lower bound was verified from primary text.
14. Bounded-arithmetic theorem numbering and claims about primes, Bertrand, AKS, and Jeřábek need source-level confirmation.
15. Razborov’s conditional bounded-arithmetic unprovability theorem is verified; sieve, relativization, and natural proofs are analogies, not number-theory independence theorems.
