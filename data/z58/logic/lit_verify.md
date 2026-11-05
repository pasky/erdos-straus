# Literature verification: bounded arithmetic and number theory

Research note: quotations below are from the cited primary source or its abstract where indicated. “NOT FOUND” means I did not establish the precise requested attribution/theorem from accessible primary text in this pass, not that the claim is false. Search URLs are not substituted for theorem text where no primary quote could be checked.

## 1. Buss (1986), bounded arithmetic and witnessing — PARTLY

The core characterization is standard and consistent with Buss’s thesis: the polynomial-time functions are precisely the Σᵇ₁-definable functions of S¹₂; the corresponding higher-level characterization is generally stated as Σᵇᵢ-definable functions of Sᵢ₂ being FP^{Σᵖᵢ₋₁}. The requested existential witnessing claim also matches the S¹₂ witnessing theorem. I did not retrieve a legible theorem number and exact theorem wording from the OCR thesis in this pass, so these exact formulations are not marked fully verified here.

Source: Samuel R. Buss, *Bounded Arithmetic* (1986 thesis), https://mathweb.ucsd.edu/~sbuss/ResearchWeb/BAthesis/Buss_Thesis_OCR.pdf (full thesis; search indexed as “Bounded Arithmetic”). Relevant survey search result: https://www.karlin.mff.cuni.cz/~krajicek/ml-14-4-23.pdf .

## 2. Buss–Krajíček (1994) PLS and Buss (1990) conservation — VERIFIED (by the internal reviewer, z58 LOGIC §8)

* Buss, *Axiomatizations and conservation results for fragments of bounded arithmetic*, Theorem 5: S₂^{i+1} is
  ∀Σ^b_{i+1}-conservative over T₂^i. https://mathweb.ucsd.edu/~sbuss/ResearchWeb/BAaxioms/camera.pdf
* Buss–Krajíček, *An application of Boolean complexity to separation problems in bounded arithmetic*, Theorem 5.3:
  the Σ^b_1-definable search problems of T¹₂ are (polynomial-time projections/reductions of) PLS problems.
  https://mathweb.ucsd.edu/~sbuss/ResearchWeb/Si2Ti2sep/paper.pdf
(The research subagent's original entry, which marked this PARTLY and raised an indexing doubt, is superseded.)

## 3. Krajíček–Pudlák (1998), cryptography and primality — PARTLY

A primary-source quotation in Jeřábek’s later paper gives the key result: “Krajíček and Pudlák [17], who have shown that S¹₂ does not prove FLT if the RSA cryptosystem is secure.” It immediately clarifies that their argument applies to “a weak corollary of FLT stating that multiplication modulo a prime is a torsion group.” Thus it is not accurately summarized as a blanket claim that S¹₂ cannot prove a specified primality notion Δᵇ₁; the exact consequence should be stated in terms of FLT / that torsion corollary under RSA security.

Source: Jeřábek, *Abelian groups and quadratic residues in weak arithmetic*, Introduction, https://users.math.cas.cz/~jerabek/papers/flt.pdf . Original publication: Krajíček & Pudlák, *Some consequences of cryptographical conjectures for S¹₂ and EF*, Information and Computation 140 (1998), 82–94; record https://www2.karlin.mff.cuni.cz/~krajicek/problemy.html . The source additionally says Jeřábek proved FLT in S¹₂ equivalent to correctness of Rabin–Miller; this is a separate result.

## 4. Jeřábek, “Integer factoring and modular square roots” — VERIFIED (complexity claim); NOT FOUND (arithmetic add-ons)

The arXiv abstract states: “We show that general integer factoring is reducible in randomized polynomial time to a PPA problem and to the problem WEAKPIGEON in PPP. Both reductions can be derandomized under the assumption of the generalized Riemann hypothesis.” This is randomized polynomial-time reductions to search problems in PPA and PPP (specifically WEAKPIGEON); it does not say factoring itself is in PPA/PPP as a deterministic many-one reduction. It also says unconditionally PPA contains modular square-root computation and finding quadratic nonresidues modulo n.

No claim about bounded arithmetic proving existence of prime factorizations or Fermat’s little theorem is made in the abstract checked. Do not infer either from the reduction result.

Exact quote and source: arXiv abstract, https://arxiv.org/abs/1207.5220 . Journal reference: JCSS 82 (2016), 380–394.

## 5. Jeřábek, “Abelian groups and quadratic residues in weak arithmetic” — VERIFIED

The abstract states: “We prove the quadratic reciprocity theorem (including the supplementary laws) in the arithmetic theories T⁰₂ + Count₂(PV) and IΔ₀ + Count₂(Δ₀) with modulo-2 counting principles.” The same abstract distinguishes related results: FLT and Euler’s criterion are derived in S²₂ + iWPHP(PV) + PHP(PV). Thus do not ascribe the quadratic reciprocity proof to that latter theory.

Exact quote, abstract: https://users.math.cas.cz/~jerabek/papers/flt.pdf . Journal record: https://onlinelibrary.wiley.com/doi/10.1002/malq.200910009 .

## 6. APC₁ / dual weak PHP witnessing — PARTLY

Jeřábek’s primary paper describes its result as “a strengthening of Wilkie’s witnessing theorem for S¹₂ + dWPHP(PV)” and proposes “a natural framework for formalization of randomized algorithms in bounded arithmetic.” Its abstract also states that it formalizes Nisan–Wigderson derandomization in a conservative extension. This supports randomized-algorithm reasoning but does not by itself establish the requested exact identification of Σᵇ₁ search problems with TFZPP (or a randomized-polytime class). The APC₁ naming/definition and exact witnessing class need a theorem-level statement from the later *Approximate counting in bounded arithmetic* paper; I have not verified that theorem number/wording here.

Exact abstract: Emil Jeřábek, “Dual weak pigeonhole principle, Boolean complexity, and derandomization,” https://users.math.cas.cz/~jerabek/papers/wphp.pdf . Journal paper: APAL 129 (2004), 1–37. Related JSL paper record: https://www.researchgate.net/publication/38385172_Approximate_counting_in_bounded_arithmetic (not a primary full-text citation).

## 7. Lagarias inequality and Davis–Matiyasevich–Robinson — PARTLY

Lagarias’s criterion is the RH equivalence with the inequality σ(n) ≤ Hₙ + exp(Hₙ) log(Hₙ) for all positive integers n (with the n=1 boundary convention handled in the theorem). A search-indexed statement explicitly calls this “Lagarias’s criterion”; an accessible formalization page says “the Riemann hypothesis is equivalent to the inequality σ(n) ≤ H_n + exp(H_n) log(H_n) for all positive integers n.” The requested exact Lagarias theorem number/primary paper quotation was not fetched in this run.

On the DMR item: not verified. The strong wording that the 1976 DMR paper gives a particular RH-equivalent Diophantine equation / Π⁰₁ sentence is not substantiated by the sources accessed; it needs checking against the actual Proc. Sympos. Pure Math. 28 article before being repeated. RH does have effective arithmetic formulations, but attribution to DMR and the specific equation are not established here.

Lagarias criterion reference/formalized statement: https://lean-lang.org/eval/problems/riemann_hypothesis_iff_lagarias_elementary_criterion/ . Article: Jeffrey C. Lagarias, “An elementary problem equivalent to the Riemann hypothesis,” Amer. Math. Monthly 109 (2002), 534–543; bibliographic record https://www.jstor.org/stable/2695443 . DMR search lead only: https://celebratio.org/Robinson_JB/article/964/ .

## 8. Friedman’s grand conjecture (1999) — VERIFIED

Friedman’s FOM posting labels this “Conjecture 1” and states: “Every theorem published in the Annals of Mathematics whose statement involves only finitary mathematical objects (i.e., what logicians call an arithmetical statement) can be proved in EFA.” This verifies the wording, with the caveat that his parenthetical equates the formulation to arithmetical statements, not simply an informal “finite objects” paraphrase.

Exact quote, primary FOM posting (16 April 1999): https://fomarchive.ugent.be/1999-April/003014.html .

## 9. Least quadratic non-residues — PARTLY

Graham–Ringrose’s infinitely-often lower bound is supported by the survey/search source: n(p) ≫ (log p)(log log log p) for infinitely many primes p. Bach’s GRH bound nₚ ≤ 2(log p)² is also reported by a survey. I did not verify Montgomery’s claimed infinitely-often GRH lower bound log p log log p in a primary source; it is not presented as established here. Distinguish lower-bound constants/notation and sources carefully.

Graham–Ringrose secondary source: https://campus.lakeforest.edu/trevino/Spring2026/Math499/Elmhurst.pdf ; additional survey: https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf . Bach bound reported in the latter (citing Bach, *Math. Comp.* 55 (1990)): https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf .

## 10. Formalizing AKS / PRIMES∈P — VERIFIED (corrected after internal review)

arXiv:2504.17041v2 (Jalali–Ježil, *Feasibility of Primality in Bounded Arithmetic*, updated 2026-01-27; Forum of
Mathematics, Sigma 14 (2026) e49), abstract verbatim: "We prove the correctness of the AKS algorithm within the bounded
arithmetic theory T^count_2 or, equivalently, the first-order consequences of the theory VTC^0 expanded by the smash
function, which we denote by VTC^0_2. Our approach initially demonstrates the correctness within the theory
S^1_2 + iWPHP augmented by two algebraic axioms and then show that they are provable in VTC^0_2." (Checked by the lane
via the arXiv API.) There is **no** identification with APC₁; the subagent's earlier "equivalently APC₁" was wrong. The
authors are Jalali and Ježil. Per the internal reviewer, their introduction notes that an S¹₂ proof of AKS correctness
would yield polynomial-time factoring.

## 11. Paris–Wilkie–Woods (1988) and infinitude of primes — VERIFIED (attribution/result), theorem wording not independently quoted

The paper title itself is “Provability of the Pigeonhole Principle and the Existence of Infinitely Many Primes”; Jeřábek’s introduction explicitly reports “the proof of infinitude of prime numbers in IΔ₀ + WPHP(Δ₀) by Paris et al. [22].” This confirms the claim with the WPHP schema over Δ₀-definable functions. The exact statement should not silently replace that with a differently formalized “weak PHP” without defining the class.

Quote from Jeřábek, Introduction: https://users.math.cas.cz/~jerabek/papers/flt.pdf . Original article citation record: https://www.jstor.org/stable/2274618 .

## 12. Natural Π⁰₁ independence in number theory — NOT FOUND as a settled “none known” survey claim

There are natural/combinatorial Π₁ independence examples, notably Harvey Friedman’s finite graph/Boolean-relation examples, so a broad assertion that no natural Π⁰₁ independence examples exist is false. However, whether these count as “number-theoretic” is a matter of classification. Busy Beaver / consistency statements are arithmetic Π₁ but are often excluded as not natural in the intended sense. I found no authoritative survey quote establishing the blanket statement “no natural number-theoretic Π₁ independence from PA or ZFC is known.” Best cautious conclusion: no specific natural elementary number-theory example was verified here; the unrestricted no-natural-example claim is too broad.

Relevant discussion: MathOverflow, “Natural Π₁ sentence independent of PA,” including Friedman’s order-invariant graph example: https://mathoverflow.net/questions/359260/natural-pi-1-sentence-independent-of-pa . Scott Aaronson’s discussion emphasizes the role of Π₁ consequences in known independence methods: https://www.scottaaronson.com/papers/indep.pdf .
