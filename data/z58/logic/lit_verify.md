# Literature verification: bounded arithmetic and number theory

Research note: quotations below are from the cited primary source or its abstract where indicated. “NOT FOUND” means I did not establish the precise requested attribution/theorem from accessible primary text in this pass, not that the claim is false. Search URLs are not substituted for theorem text where no primary quote could be checked.

## 1. Buss (1986), bounded arithmetic and witnessing — PARTLY

The core characterization is standard and consistent with Buss’s thesis: the polynomial-time functions are precisely the [1mΣᵇ₁-definable functions of S¹₂[0m; the corresponding higher-level characterization is generally stated as Σᵇᵢ-definable functions of Sᵢ₂ being FP^{Σᵖᵢ₋₁}. The requested existential witnessing claim also matches the S¹₂ witnessing theorem. I did not retrieve a legible theorem number and exact theorem wording from the OCR thesis in this pass, so these exact formulations are not marked fully verified here.

Source: Samuel R. Buss, *Bounded Arithmetic* (1986 thesis), https://mathweb.ucsd.edu/~sbuss/ResearchWeb/BAthesis/Buss_Thesis_OCR.pdf (full thesis; search indexed as “Bounded Arithmetic”). Relevant survey search result: https://www.karlin.mff.cuni.cz/~krajicek/ml-14-4-23.pdf .

## 2. Buss–Krajíček (1994) PLS and Buss (1990) conservation — PARTLY

The PLS characterization is attributed in the literature to Buss–Krajíček, but I did not verify the exact PLMS article’s theorem text in this pass. The proposed inference that S²₂ Σᵇ₁ consequences are witnessed in PLS is consistent with the stated witnessing/conservation results; it is not independently quoted here. The conservation claim is usually given as Sᵢ₊₁₂ being Σᵇᵢ₊₁-conservative over Tᵢ₂, not with the index shifted to Tᵢ₂ as in some informal phrasings; check the source’s precise indexing and formula class before relying on that restatement.

Buss–Krajíček paper record/search: https://mathweb.ucsd.edu/~sbuss/ResearchWeb/Si2Ti2sep/index.html . A later source describes their characterization as “PLS ≡ Σ̂ᵇ₁” (notation-dependent): https://www.karlin.mff.cuni.cz/~krajicek/low.pdf . No exact theorem-number quotation located for the requested 1990 conservation claim.

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

## 10. Formalizing AKS / PRIMES∈P — VERIFIED (new work, not Jeřábek); partly as framed

There is now a direct bounded-arithmetic formalization result: Jalali, *Feasibility of Primality in Bounded Arithmetic* (2025 preprint / 2026 journal version), whose abstract says: “We prove the correctness of the AKS algorithm … within the bounded arithmetic theory T₂^count or, equivalently, the first-order theory APC₁.” Therefore a positive published/preprint result exists, but it should not be attributed to Jeřábek’s “Iterated multiplication in VTC⁰.” A separate paper abstract says Jeřábek proved correctness of Rabin–Miller in S²₂ + iWPHP(PV) + PHP(PV), distinct from AKS.

AKS result: https://arxiv.org/abs/2504.17041 ; journal publication: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/feasibility-of-primality-in-bounded-arithmetic/18A1BD004161C115D21E117A20B0B172 . Secondary abstract reporting Rabin–Miller: https://arxiv.org/pdf/2504.17041 .

## 11. Paris–Wilkie–Woods (1988) and infinitude of primes — VERIFIED (attribution/result), theorem wording not independently quoted

The paper title itself is “Provability of the Pigeonhole Principle and the Existence of Infinitely Many Primes”; Jeřábek’s introduction explicitly reports “the proof of infinitude of prime numbers in IΔ₀ + WPHP(Δ₀) by Paris et al. [22].” This confirms the claim with the WPHP schema over Δ₀-definable functions. The exact statement should not silently replace that with a differently formalized “weak PHP” without defining the class.

Quote from Jeřábek, Introduction: https://users.math.cas.cz/~jerabek/papers/flt.pdf . Original article citation record: https://www.jstor.org/stable/2274618 .

## 12. Natural Π⁰₁ independence in number theory — NOT FOUND as a settled “none known” survey claim

There are natural/combinatorial Π₁ independence examples, notably Harvey Friedman’s finite graph/Boolean-relation examples, so a broad assertion that no natural Π⁰₁ independence examples exist is false. However, whether these count as “number-theoretic” is a matter of classification. Busy Beaver / consistency statements are arithmetic Π₁ but are often excluded as not natural in the intended sense. I found no authoritative survey quote establishing the blanket statement “no natural number-theoretic Π₁ independence from PA or ZFC is known.” Best cautious conclusion: no specific natural elementary number-theory example was verified here; the unrestricted no-natural-example claim is too broad.

Relevant discussion: MathOverflow, “Natural Π₁ sentence independent of PA,” including Friedman’s order-invariant graph example: https://mathoverflow.net/questions/359260/natural-pi-1-sentence-independent-of-pa . Scott Aaronson’s discussion emphasizes the role of Π₁ consequences in known independence methods: https://www.scottaaronson.com/papers/indep.pdf .
