# IΔ0, IΔ0+Ω1 and IΔ0+exp (EFA) on true Π1 sentences: what the primary literature says

Working dir: `/tmp/z66_ie1_lit2`. No model/provider/auth/quota errors occurred. Elsevier (ScienceDirect) full texts were
blocked by a captcha, and the JSTOR and Cambridge full texts were paywalled. For those items I could only read the abstract or the first-page extract.

Verdict legend: **VERIFIED** means I read the primary text and quote it. **PARTLY** means I only saw an abstract, extract or snippet, or a
reliable secondary source (named). **NOT FOUND** means what it says.

## Key sources I read in full or in large part (archived here)

| Source | File | URL |
|---|---|---|
| Hájek–Pudlák, *Metamathematics of First-Order Arithmetic*, Ch. V "Bounded Arithmetic" (Perspectives in Logic 3, pp. 267–395, open access) | `hajek_pudlak_chV_jina.md` (text extraction via r.jina.ai, so the OCR is noisy; Σ0 is often rendered "ΣQ"/"Σo") | https://projecteuclid.org/ebooks/perspectives-in-logic/Metamathematics-of-First-Order-Arithmetic/chapter/Chapter-V-Bounded-Arithmetic/pl/1235421934.pdf |
| S. Buss, "First-order proof theory of arithmetic", Handbook of Proof Theory, Ch. II (1998) | `buss_handbook_ch2.pdf` | https://mathweb.ucsd.edu/~sbuss/ResearchWeb/handbookII/ChapterII.pdf |
| C. Dimitracopoulos, "Subsystems of Peano arithmetic and classical results of number theory", *Filomat* 9:3 (1995) 473–481 (invited survey) | `dimitracopoulos_filomat1995_survey.pdf` (scanned) and `..._OCR.txt` (my tesseract OCR; IΣ0 is OCR'd as "IX,"/"IS,", Ω1 as "9;") | http://elib.mi.sanu.ac.rs/files/journals/flmt/9c/flmn70p473-481.pdf |
| J. Avigad, "Number theory and elementary arithmetic", *Philosophia Mathematica* 11 (2003) 257–284 | `avigad_elementary.pdf` | https://www.andrew.cmu.edu/user/avigad/Papers/elementary.pdf |
| H. Friedman, FOM post "grand conjectures", 16 Apr 1999 | `fom_friedman.html` | https://web.archive.org/web/20191129023832/https://cs.nyu.edu/pipermail/fom/1999-April/003014.html (original link http://cs.nyu.edu/pipermail/fom/1999-April/003014.html is now 404) |
| P. D'Aquino, M. Bovenzi, "A theorem of Legendre in IΔ0+Ω1", arXiv:1405.4367 | `bovenzi_daquino_legendre_1405.4367.pdf` | https://arxiv.org/abs/1405.4367 |
| E. Jeřábek, "Abelian groups and quadratic residues in weak arithmetic", MLQ 56 (2010) 262–278 (author PDF) | `jerabek_abquad_mlq2010.pdf` | https://users.math.cas.cz/~jerabek/papers/flt.pdf |
| E. Jeřábek, "Integer factoring and modular square roots", JCSS 82 (2016) 380–394 | `jerabek_factoring_1207.5220.pdf` | https://arxiv.org/abs/1207.5220 |
| S. Salehi, "Separating bounded arithmetical theories by Herbrand consistency", J. Logic Comput. 22 (2012) 545–560 | `salehi_1008.0225.pdf` | https://arxiv.org/abs/1008.0225 |
| S. Buss, "Bounded arithmetic, proof complexity and two papers of Parikh", APAL 96 (1999) 43–55 (author PDF) | `buss_parikh_papers.pdf` | https://mathweb.ucsd.edu/~sbuss/ResearchWeb/parikh/paper.pdf |
| H. Lipmaa, "On Diophantine complexity and statistical zero-knowledge arguments", ASIACRYPT 2003, LNCS 2894 | `lipmaa2003.pdf` | https://link.springer.com/content/pdf/10.1007/978-3-540-40061-5_26.pdf |
| A. Atserias, M. Müller, "Partially definable forcing and bounded arithmetic", AML 54 (2015) | `atserias_forcing.pdf` | https://www.cs.upc.edu/~atserias/papers/forcing/forcing_revised.pdf |
| M. Narusevych (arXiv 2208.14713 and the Cambridge version) | `narusevych_*.pdf` | https://arxiv.org/abs/2208.14713 |

---

## 1. Is IΔ0+exp Π1-conservative over IΔ0? Con(Q), Con(IΔ0), Herbrand and cut-free consistency

**Short answer.** No. IΔ0+exp is **not** Π1-conservative over IΔ0, and in fact not even over IΔ0+{Ωn : n∈N}. Hájek–Pudlák
Cor. V.5.34 proves this. Wilkie–Paris 1987 had posed it as an open problem, according to Buss. The separating Π1 sentences
are metamathematical: restricted consistency of Q, RCon_Q(m), or Herbrand consistency. IΔ0+exp does **not** prove
Con(Q), and therefore not Con(IΔ0) either. It **does** prove Herbrand consistency and cut-free consistency of Q. It also proves bounded
consistency of IΔ0, and HCon(IΔ0+Ωm) for every m.

The open questions are lower down: whether IΔ0+Ω1 is Π1-conservative over IΔ0, and more generally whether IΔ0+Ωi is Π1-conservative over IΔ0+Ωj. These are open and are tied to complexity theory, e.g. PH vs LinH.

### Hájek–Pudlák, Ch. V — **VERIFIED** (open-access PDF read via text extraction)
- **Thm V.5.20**: "(i) IΣ0 + Superexp ⊢ Con_{IΣ0}. (ii) IΣ0 + Exp ⊢ HCon_Q and for every k, IΣ0 + Exp ⊢ RCon_Q(k)." Here
  RCon_Q(k) means consistency with respect to proofs of cut-rank ≤ k, and HCon means Herbrand consistency. The proof begins "Assume ¬HCon(Q′) … this is
  impossible, since in IΣ0 + Exp we can define the truth for open formulae."
- **Thm V.5.19**: "It is provable in IΣ0 + Exp that: a formula has a cut-free proof if and only if it has a Herbrand proof."
- **Thm V.5.26 (Wilkie)** says that for a bounded φ the following are equivalent: "(1) There exists a cut I(x) in Q such that [Q ⊢ ∀x(I(x)→φ(x))];
  (2) There exists an interpretation of Q + (∀x)φ(x) in Q; (3) IΣ0 + Exp ⊢ (∀x)φ(x)." The text introduces it as: "a theorem of A.
  Wilkie which characterizes Π1 sentences provable in IΣ0 + Exp as the Π1 sentences interpretable in Q".
- **Thm V.5.27**: IΣ0+Exp ⊢ ∀xφ(x) ⇔ for some k, S^1_2 ⊢ ∀x ¬RPr_Q(k, ¬φ(ẋ)) ⇔ (for Π^b_1 φ) S^1_2 + RCon_Q(k) ⊢ ∀xφ(x).
  The authors add: "the set of sentences RCon_Q(k), k = 0,1,... axiomatizes the ∀Π^b_1 consequences of IΣ0 + Exp."
- **Cor V.5.29**: "Con_Q is not provable in IΣ0 + Exp."
- **Cor V.5.30**: "Cut elimination (unrestricted), and Herbrand's Theorem are not provable in IΣ0 + Exp. Proof. By Theorem 5.20 (ii)
  IΣ0 + Exp proves cut-free and Herbrand consistency of Q. If we had cut-elimination or Herbrand's Theorem in IΣ0+Exp, we could reduce
  the ordinary consistency of Q to the restricted one."
- **Thm V.5.31**: IΣ0 + Exp + Con_{IΣ0}^* does not prove Con_{IΣ0+Exp}. **Cor V.5.32**: "IΣ0 + Exp is not interpretable in IΣ0".
- **Thm V.5.33**: "For every k there exists m such that RCon_Q(m) is not provable in IΣ0 + Ωn + RCon_Q(k) for any n."
- **Cor V.5.34**: "IΣ0 + Exp is not Π1 conservative over IΣ0 + {Ωn; n ∈ N}." Immediately after it comes the passage on what remains open:
  > "In fact this is all that we know about Π1 conservativity between systems of bounded arithmetic. In particular it seems
  > plausible that IΣ0 + Ω1 is not Π1 conservative over IΣ0, but we cannot even prove that IΣ0 + {Ωn; n ∈ N} is not Π1
  > conservative over IΣ0. A Π1 sentence which might separate IΣ0 + Ω1 from IΣ0 is the so-called Bertrand's postulate. It is the
  > theorem (due to Sylvester) which says that there is a prime between n and 2n, for every n. This sentence is provable in
  > IΣ0 + Ω1, but no proof of it has been found in IΣ0. Whether such a proof exists is an important open problem."
- Also in §1, after Cor V.1.6: "The sentences which separate the levels of this hierarchy are Π2. We shall see in Sect. 5 that we
  can separate IΣ0+Exp from IΣ0 + Ωn by a Π1 sentence and the same is true for IΣ0 + Superexp and IΣ0 + Exp. Such separations
  remain, however, an open problem for the theories below IΣ0 + Exp."
- On the complexity connection (end of §5(g)):
  > "The related problems of whether IΣ0+Ωi is Π1 conservative over IΣ0+Ωj, for j < i, are still open. They are typical in the
  > sense that they are related to open problems in complexity theory. For instance, the question whether IΣ0 + Ω1 is Π1
  > conservative over IΣ0 seems to be formally related to the open problem whether PH = LinH (though we are not able to prove any
  > relation)."
- §5(g) also says: "If we are interested only in Π1 sentences, then it seems that all such sentences which are also truly mathematical
  results are provable in IΣ0 + Exp (we consider sentences like Con(Q) to be uninteresting for an ordinary mathematician). In fact
  the proofs use exponentiation at most once." Thm V.5.36 builds a hierarchy by number of uses of exponentiation. The remark after it reads:
  "We are not able to derive PHP_{Σ0} in IΣ0 + Ω1".

### Buss, Handbook Ch. II §4.3 — **VERIFIED**
- "**Theorem. (Wilkie and Paris [1987])** IΔ0 + exp cannot prove Con(IΔ0). Therefore, IΔ0 + exp cannot prove Con(Q)."
- "IΔ0 + exp ⊢ BdCon(IΔ0)" (bounded-proof consistency), and "IΔ0 + superexp ⊢ Con(IΔ0)".
- §4.3.8 says S2 + exp is ∀Π^b_1-conservative over S2 ∪ {Con_{Σk}(S2) : k ≥ 0}. §4.3.9 says this theory does not prove Con(S2).
- **§4.3.11**: "A related result, which was stated as an open problem by Wilkie and Paris [1987] and was later proved by Hájek and
  Pudlák [1993, Coro. 5.34], is the fact that there is a ∀Π^b_1-sentence φ, such that S^1_2 + exp ⊢ φ but such that S^k_2 ⊬ φ for
  all k ≥ 0."
- §4.2: Buss [1986] showed that bounded theories S cannot prove their own free-cut-free consistency. These independence results are
  "motivated by a yet-unfulfilled hope that independence results of these kinds could lead to a proof that P ≠ NP."

### A.J. Wilkie, J.B. Paris, "On the scheme of induction for bounded arithmetic formulas", APAL 35 (1987) 261–302, doi:10.1016/0168-0072(87)90066-2 — **PARTLY**
- The full text is Elsevier open archive, but the PDF was captcha-blocked and no abstract exists. Its content is attested only via HP and Buss (above).
  A secondary snippet, from an academia.edu paper "Finitistic arithmetic and classical logic", cites "Corollary 8.14 of (Wilkie and Paris 1987,
  p. 297), stating that IΔ0 + Exp does not prove the consistency of Q". I have not verified this.
- Salehi (below) says: "For this Π1-separation, Paris and Wilkie [8] suggested the notion of cut-free consistency … one can show that
  IΔ0 + Exp ⊢ CFCon(IΔ0), and then it was presumed that IΔ0 ⊬ CFCon(IΔ0)."
- URL: https://www.sciencedirect.com/science/article/pii/0168007287900662

### P. Pudlák, "Cuts, consistency statements and interpretations", JSL 50 (1985) 423–441, doi:10.2307/2274231 — **PARTLY** (first-page extract only)
- The extract covers interpretability in nonreflexive, finitely axiomatized theories, and "the method of 'shortening of cuts'" (Solovay). I could
  not read the theorem statements. HP Thm V.5.28 (a cut version of Gödel II for Q-interpretations: "for every cut J in T there exists m such
  that T ⊬ RCon_T^J(m)") is in this line of work. The attribution is my inference and was not checked in the paper.
- URL: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/cuts-consistency-statements-and-interpretations/43AA282E6574B73C2C6BC99CD3EF2183

### Herbrand consistency and the later sharpening — **VERIFIED** (arXiv text, abstracts)
- S. Salehi, *J. Logic Comput.* 22 (2012) 545–560 (arXiv 1008.0225). The abstract says Herbrand consistency "cannot Π1-separate the theory
  IΔ0+⋀jΩj from IΔ0; though it can Π1-separate IΔ0+Exp from IΔ0." **Thm 13** (arXiv numbering): "For any m ⩾ 1 we have IΔ0 + Exp ⊢
  HCon(IΔ0 + Ωm)." The paper also says: "I∆0 + Exp ⊬ Con(I∆0) (see [4] Corollary 5.29)", and "I∆0 + Exp ⊢ HCon(Q) but I∆0 + Exp ⊬ Con(Q) ([4], Theorem 5.20 and Corollary 5.29)."
  Problem 7: "Is there a Π1-sentence ψ such that IΔ0+Ωm+1 ⊢ ψ and IΔ0+Ωm ⊬ ψ?", called "the (difficult) open problem".
- S. Salehi, "Herbrand consistency of some arithmetical theories", JSL 77 (2012) 807–827. The abstract (OpenAlex) says: "the Herbrand version of Gödel's second
  incompleteness theorem follows for the theories IΔ0+Ω1 and IΔ0" (with a tailored HCon for IΔ0).
- Z. Adamowicz, *Fund. Math.* 171 (2002) 279–292: Tm = IΔ0+Ωm, m ≥ 2, Tm ⊬ HCons(Tm).
- L.A. Kołodziejczyk, JSL 71 (2006) 624–638: "there exists a number n such that ⋃m S_m does not prove the Herbrand consistency of
  the finitely axiomatizable theory S^n_3".

**Bottom line for item 1:**
- **Known:**
  - IΔ0+exp ⊬ Con(Q), Con(IΔ0) (Wilkie–Paris; HP V.5.29).
  - IΔ0+exp ⊢ HCon(Q), CFCon(Q), RCon_Q(k) for each k (HP V.5.20).
  - IΔ0+exp ⊢ BdCon(IΔ0) (Buss).
  - IΔ0+exp ⊢ HCon(IΔ0+Ωm) (Salehi).
  - IΔ0+exp is not Π1-conservative over IΔ0+{Ωn} (HP V.5.34).
  - The Π1 consequences of IΔ0+exp are exactly the bounded ∀φ interpretable in Q, equivalently S^1_2+{RCon_Q(k)} (Wilkie; HP V.5.26–27).
- **Open:**
  - Π1-conservativity of IΔ0+Ω1 over IΔ0, and of the Ωi over the Ωj (HP; Salehi Problem 7).
  - In HP's 1993/98 statement, even "IΔ0+{Ωn} not Π1-conservative over IΔ0" is unknown. HP say this is "formally related" to PH = LinH,
    though they explicitly cannot prove any relation.

---

## 2. Is any natural true Π1 sentence known to be unprovable in IΔ0? PHP, primes, Ajtai

**Short answer.** In the primary sources I read, no natural unrelativized number-theoretic Π1 sentence is known to be unprovable in IΔ0.
- Δ0-PHP in IΔ0 is open.
- Infinitude of primes in IΔ0 is open. It is Π2 as usually stated; the Bertrand/Sylvester forms are Π1.
- What is known: unprovability for the *relativized* PHP(R) in IΔ0(R) (Ajtai 1988), and for metamathematical sentences such as HCon(IΔ0) (Salehi).

### Hájek–Pudlák Ch. V §1 — **VERIFIED**
> "If we consider this principle [PHP] for Σ0 formulae, then it is at least as strong as IΣ0. Whether it is derivable in IΣ0 is an
> important open problem. We have some evidence that Σ0-PHP might be stronger than IΣ0; we can prove some mathematical results using
> Σ0-PHP which we are not able to derive in IΣ0 itself. In particular we have Q + Σ0-PHP ⊢ (∀x)(∃p)(p > x & "p is a prime"), i.e.
> Σ0-PHP proves that there are infinitely many primes, while we are not currently able to derive it in IΣ0."

### Paris, Wilkie, Woods, "Provability of the pigeonhole principle and the existence of infinitely many primes", JSL 53(4) (1988) 1235–1244, doi:10.1017/S0022481200028061 — **PARTLY** (Cambridge first-page extract; theorem contents via two secondary sources)
- Extract: "Problem 1. Can IΔ0 ⊢ ∀x∃y > x (y is prime)? … Problem 2. Can IΔ0 ⊢ Δ0PHP? … By obtaining partial solutions to Problem 2
  we shall show that Problem 1 has a positive solution if IΔ0 is replaced by IΔ0 + ∀x x^{log(x)} exists." The extract also gives
  "Theorem 1. For k ∈ N and F ∈ Δ0, …" (a weak-PHP bound with log_k), but the formula was lost in the HTML.
- Dimitracopoulos 1995 survey (OCR'd; "IX,"/"IS," = IΣ0, "9;" = Ω1). This is author-level testimony from a co-worker; Dimitracopoulos is not a PWW author.
  - "Theorem 16. IΣ0 + Ω1 proves weak-PHPΣ0"; "Theorem 17. IΣ0 + Ω1 proves that the set of primes is unbounded."
  - "Theorem 18. IΣ0 + Ω1 proves Sylvester's theorem. This follows from Theorem 16 and the fact that Woods's proof of Theorem 8 really uses
    weak-PHPΣ0, not PHPΣ0."
- Bovenzi–D'Aquino 2014, read in full:
  - "Theorem 1.8 (Paris, Wilkie and Woods, [PWW]) IΔ0 + Δ0-WPHP ⊢ ∀x∃p (Pr(p) ∧ p > x)", where Δ0-WPHP is "there is no injective
    Δ0-function from (1+ε)z into z".
  - "In [PWW] it is also shown that the Δ0-WPHP is provable in the theory IΔ0 + Ω1".
  - "Theorem 1.10 (PWW) IΔ0 + Ω1 ⊢ ∀x∃p (Pr(p) ∧ p > x)."
- Jeřábek MLQ 2010 intro: "the proof of infinitude of prime numbers in IΔ0 + WPHP(Δ0) by Paris et al. [22]".

### A. Woods, *Some problems in logic and number theory, and their connections*, PhD thesis, Manchester 1981 — **PARTLY** (secondary only; thesis not online)
- Dimitracopoulos 1995: "Theorem 8. IΣ0 + PHPΣ0 proves Sylvester's theorem, i.e. that for any 1 < x ≤ y one of y+1, …, y+x has a
  prime divisor p > x." The survey describes the proof as a logarithmic version of Sylvester's inequality, "unravelled" to a comparison map
  contradicting PHPΣ0. Corollaries: "(a) the answer to Problem 2 is 'yes' if IΣ0 is replaced by IΣ0 + PHPΣ0; (b) if the answer to Problem 3 is
  'yes', then the answer to Problem 2 is 'yes'." Also: "Theorem 9 [Woods]. IE^*_2 proves PHP_{E^*_2}". Woods' conjecture is that IΣ0(π)+DEF(π) proves
  primes are unbounded.
- Bovenzi–D'Aquino: "Theorem 1.7 (Woods, [Wo]) IΔ0 + Δ0-PHP ⊢ ∀x∃p (Pr(p) ∧ p > x)."
- Bertrand's postulate in IΔ0+Ω1: HP p.392–393 (quoted in §1): "provable in IΣ0 + Ω1, but no proof of it has been found in IΣ0".
- Cornaros (survey Thm 15): "IΣ0(π, K) + DEF(π, K) proves Bertrand's postulate" (K(x) = Σ_{n≤x} log n).

### Standard statement of the open problems — **VERIFIED** (Dimitracopoulos 1995 survey, p.475)
> "Problem 1 (Paris). Does IΣ0 prove the MRDP theorem? … Problem 2 (Wilkie). Does IΣ0 prove that the set of primes is unbounded?
> Problem 3 (Macintyre). Does IΣ0 prove PHPΣ0? … It is widely believed that the answer to all these problems is 'no'."

Bovenzi–D'Aquino (2014): "For example, it is still unknown if IΔ0 proves the existence of arbitrarily large of primes."

### M. Ajtai, "The complexity of the pigeonhole principle", FOCS 1988, pp. 346–355 (doi:10.1109/SFCS.1988.21951); journal version *Combinatorica* 14 (1994) 417–433 (doi:10.1007/BF01302964) — **PARTLY**
- The abstract (Springer/IEEE) is purely propositional: "Our main result is that the Pigeonhole Principle cannot be proved this way, if the size of the
  proof … is polynomial in n and each formula is constant depth (unlimited fan-in), polynomial size and contains only the variables of PHP_n."
- The arithmetic form is attested by secondary sources:
  - Narusevych (Cambridge diamond-OA version): "a celebrated theorem of Ajtai [1] establishing unprovability of the pigeonhole principle in the
    bounded arithmetic theory IΔ0(R) was used by him to give a super-polynomial lower bound for constant-depth proof systems (later
    improved to exponential …)".
  - Atserias–Müller 2015: "Ajtai's result implies independence from the theory IΔ0(R), and the mentioned improvements imply independence
    from Buss' T2(R)."
  - Zambella (ILLC eprint): "a strengthening of a theorem of Ajtai's: the independence of the pigeonhole principle from IΔ0(R)".
- I found no theorem number in the abstract. Ajtai built the model by nonstandard model theory, as a forcing-style expansion.

---

## 3. Friedman's grand conjecture; Avigad on EFA

### H. Friedman, FOM, "FOM: grand conjectures", Fri Apr 16 1999 — **VERIFIED**
URL: http://cs.nyu.edu/pipermail/fom/1999-April/003014.html (now 404). Archived copy:
https://web.archive.org/web/20191129023832/https://cs.nyu.edu/pipermail/fom/1999-April/003014.html
> "Conjuecture 1. Every theorem published in the Annals of Mathematics whose statement involves only finitary mathematical objects
> (i.e., what logicians call an arithmetical statement) can be proved in EFA. EFA is the weak fragment of Peano Arithmetic based on
> the usual quantifier free axioms for 0,1,+,x,exp, together with the scheme of induction for all formulas in the language all os
> whose quantifiers are bounded. This has not even been carefully established for Peano Arithmetic. … However, there are some
> proofs which are very difficult to understand for all but a few people that have appeared in the Annals of Mathematics - e.g.,
> Wiles' proof of FLT."

The typos are Friedman's own. The post also states "Conjecture 2" (logically strong categorical methods in Annals proofs can be eliminated "by restriction").

### J. Avigad, "Number theory and elementary arithmetic", *Philosophia Mathematica* (3) 11 (2003) 257–284 — **VERIFIED**
- Avigad calls it the "Grand conjecture. Every theorem published in the Annals of Mathematics whose statement involves only finitary mathematical objects
  (i.e., what logicians call an arithmetical statement) can be proved in elementary arithmetic." Then: "Specific conjecture. Fermat's last
  theorem is derivable in elementary arithmetic."
- **Dirichlet**: "Despite the use of analytic methods in the original proof, it turns out that Dirichlet's theorem can be derived in
  weak fragments of arithmetic. Patrick Cegielski [1992] has shown that primitive recursive arithmetic, PRA, suffices; the proof
  amounts to formalizing the usual analytic methods in RCA0, and then invoking Π2 conservativity over PRA. There seems to be no bar to
  adapting the definitions to RCA*0, and, with some extra care, getting the argument to go through there; this would yield
  derivability in EA." Also: "there are alternative proofs of Dirichlet's theorem that seem to be amenable to direct formalization in
  EA" (Selberg 1949). Note that Avigad does **not** claim that an EA proof of Dirichlet has actually been carried out.
- **PNT**: "Gaisi Takeuti [1978] developed enough complex analysis to carry out the proof of the prime number theorem in a
  conservative extension of first-order arithmetic, and with additional care Oliver Sudac has shown [2001] that IΣ1 suffices. …
  Cornaros and Dimitracopoulos were able to formalize Selberg's proof in IΔ0 + (exp), a theory equivalent to elementary arithmetic."
  Footnote 14 corrects Sudac's claim that IΣ1 is conservative over PRA.
- **Quadratic reciprocity**: Avigad says nothing about it (grep of the full text finds no "reciprocity").
- On consistency: "a striking theorem due to Alex Wilkie that implies that elementary arithmetic cannot even prove the consistency of
  Robinson's Q." On weaker theories he points to "Paris et al. [1988] and D'Aquino and Macintyre [2000]".

---

## 4. Gaifman–Dimitracopoulos 1982 and MRDP

H. Gaifman, C. Dimitracopoulos, "Fragments of Peano's arithmetic and the MRDP theorem", in *Logic and Algorithmic* (Zürich 1980),
Monographie de L'Enseignement Mathématique 30, Univ. Genève 1982, pp. 187–206 — **PARTLY**. I could not find the paper online.
- Dimitracopoulos 1995 survey (co-author's own statement; scanned and OCR'd):
  - The survey defines the problem: "Since the MRDP theorem cannot be expressed as a set of sentences of LA, what is meant in problem 1 is: Can we replace N ⊨ by
    IΣ0 ⊢ in the MRDP theorem?" Here MRDP is "For every Σ1 formula φ(x̄) we can effectively find a polynomial p ∈ Z[x̄, ȳ] such that N ⊨ ∀x̄[φ(x̄) ↔ ∃ȳ(p = 0)]".
  - "**Theorem 4.** IΣ0 + exp proves the MRDP theorem. … The first of these results was proved by H. Gaifman and, independently, the
    author (see [6]) … the proofs … are based on the fact that inside any M ⊨ IΣ0 + exp one can code finite (in the sense of M), Σ0
    definable sequences of elements of M."
  - "Theorem 5. IΣ0 + exp proves PHPΣ0" (Dimitracopoulos–Paris 1986). "Theorem 6. IΣ0 + exp proves that the set of primes is
    unbounded."
  - "Concerning Problem 1, this feeling is especially strong, in view of the following observation of A. Wilkie (see [19]): If IΣ0
    proves the MRDP theorem, then NP = co-NP." The same holds for IΣ0+Ω1: "Wilkie's observation shows that if IΣ0 + Ω1 proves the MRDP
    theorem, then NP = co-NP."
- Bovenzi–D'Aquino 2014 (arXiv, read): "it is still an open problem if IΔ0 proves the MRDP-theorem … IΔ0 ⊢ ∀x̄ (θ(x̄) ↔ ∃ȳ
  p(x̄,ȳ) = 0)? Wilkie (see [W]) observed that a positive answer to this problem in IΔ0 would give a positive solution to the well
  known open problem in complexity theory if NP = coNP. It is also unknown if IΔ0 + Ω1 proves MRDP-theorem and, again, a positive
  answer would give NP = coNP." Here [W] is Wilkie, "Applications of complexity theory to Σ0-definability problems in arithmetic", LNM 834 (1980).
- Buss, Handbook II §1.2.7.3 cites Gaifman–Dimitracopoulos [1982, Prop 2.3] for adding Σ1-defined functions over BΣ1. He also says the
  Δ0-definability of exponentiation "was first (and independently) proved in the setting of IΔ0 by Gaifman and Dimitracopoulos [1982]".
- A ResearchGate snippet (unverified) says: "Gaifman and Dimitracopoulos showed that IΔ0 + ∀x∃y 2^x=y does prove MRDP. Kaye proved MRDP using only
  induction for bounded existential formulas" [+exp]. This refers to R. Kaye, "Diophantine induction", APAL 46 (1990) 1–40; I could not get its abstract.
- C. Pollett, "On the bounded version of Hilbert's tenth problem", AML 42 (2003) 469–488, doi:10.1007/s00153-002-0162-y. Abstract
  **VERIFIED**: "The theory I_5E_1 is shown to be unable to prove 𝒟=NP. This non-provability result is used to show that I_5E_1 cannot
  prove the MRDP theorem."
- **Status in IΔ0: open** (Paris' Problem 1). A positive answer would imply NP = coNP (Wilkie).

---

## 5. Pell equations, quadratic forms, Legendre, QR, PNT, Dirichlet

- **P. D'Aquino, "Pell equations and exponentiation in fragments of arithmetic"**, APAL 77 (1996) 1–34, doi:10.1016/0168-0072(95)00018-6 — **PARTLY** (abstract)
  > "We study the relative strength of the two axioms (P) Every Pell equation has a nontrivial solution (exp) Exponentiation is
  > total over weak fragments, and we show they are equivalent over IE1. We then define the graph of the exponential function using
  > only existentially bounded quantifiers in the language of arithmetic expanded with the symbol #…"

  Consequence (my inference from IE1 ⊆ IΔ0 together with IΔ0 ⊬ exp by Parikh): IΔ0 does not prove (P), and neither does IΔ0+Ω1, since (P) implies exp.
- **P. D'Aquino, A. Macintyre, "Non-standard finite fields over IΔ0+Ω1"**, Israel J. Math. 117 (2000) 311–333, doi:10.1007/BF02773575 — **PARTLY** (abstract)
  > "We consider residue fields of primes in … IΔ0+Ω1. We prove that each such residue field has exactly one extension of each
  > degree. The standard proofs use counting and the Frobenius map. … we looked for, and found, another proof using permutation groups
  > and the elements of Galois cohomology. This proof fits nicely into IΔ0 + Ω1 using, instead of exponentiation, exponentiation
  > modulo a prime."

  Jeřábek 2010 adds that the decomposition of a finite abelian group into p-groups "was formalized in IΔ0 + Ω1 by D'Aquino and Macintyre [9]".
- **P. D'Aquino, A. Macintyre, "Quadratic forms in models of IΔ0+Ω1. I"**, APAL 148 (2007) 31–48, doi:10.1016/j.apal.2007.05.004 — **PARTLY** (abstract). Note: two authors, not D'Aquino alone.
  > "Gauss used quadratic forms in his second proof of quadratic reciprocity. In this paper we begin to develop a theory of binary
  > quadratic forms over weak fragments of Peano Arithmetic, with a view to reproducing Gauss' proof in this setting."
- **Part II: Local equivalence**, APAL 162 (2011) 447–456, doi:10.1016/j.apal.2010.12.003 — **PARTLY** (abstract): "In this second
  paper of the series we do a local analysis of quadratic forms over completions of a non-standard model of IΔ0+Ω1."
  - Jeřábek 2010 describes the program: D'Aquino–Macintyre "aims towards proving quadratic reciprocity or at least some of its special cases in S2".
  - I found no genus-theory result in weak arithmetic.
- **Legendre's theorem on ax²+by²+cz²=0**: Bovenzi & D'Aquino, arXiv:1405.4367 (2014) — **VERIFIED**. Main result: "Theorem 2.1 (Legendre)
  Let a,b,c ∈ M∖{0} be non-zero, not all of the same sign, square-free and pairwise relatively prime. Then the equation ax²+by²+cz²=0
  has a non trivial solution in M iff (Leg.1) −ab R c, (Leg.2) −bc R a, (Leg.3) −ac R b", where "R" means "is a square modulo". It is proved for M ⊨ IΔ0+Ω1 via the normal form,
  Thm 2.3/2.11. The authors obtained "estimates on the growth rate of the solution … of polynomial size in x^{log2 y}".
- **Quadratic reciprocity** — **VERIFIED** for Jeřábek; the rest via the survey and Jeřábek's intro:
  - Jeřábek 2010, Thm 5.7: "T^0_2+Count2(PV) and IΔ0+Count2(Δ0) prove the law of quadratic reciprocity", the supplementary laws, and
    multiplicativity of the Legendre symbol.
  - Cornaros: QR in IE*_2 (survey Thm 14; "On Grzegorczyk induction", APAL 74 (1995)).
  - Berarducci–Intrigila, APAL 55 (1991) 35–50, according to the survey:
    - "Theorem 11. IΣ0 + weak-PHPΣ0 proves Lagrange's theorem";
    - "Theorem 12. IΣ0 + EQΣ0 proves the 'complementary conditions' of the quadratic reciprocity law";
    - "Theorem 13. IΣ0 + EQΣ0 proves that a prime number is the sum of two squares iff it is of the form 4n + 1."
- **Euler's criterion / Fermat's little theorem** (Jeřábek 2010, VERIFIED): proved in S^2_2 + iWPHP(PV) + PHP(PV). "It remains an open problem
  whether FLT is provable in the bounded arithmetic S2." By Krajíček–Pudlák, S^1_2 does not prove FLT if RSA is secure.
- **PNT**: C. Cornaros, C. Dimitracopoulos, "The prime number theorem and fragments of PA", AML 33 (1994) 265–281, doi:10.1007/BF01270626 — **PARTLY** (summary)
  > "We show that versions of the prime number theorem as well as equivalent statements hold in an arbitrary model of IΔ0+exp."

  The survey (Thm 7) says the proof is a modification of Selberg's, using Woods' approximate logarithm and replacing limits by induction.
- **Dirichlet's theorem in bounded arithmetic / EFA**: **NOT FOUND** as a published theorem. The only result found is in PRA, by Cegielski 1992
  (technical report, as cited by Avigad). Avigad only conjectures that it goes through in EA.
- **Negative Pell, continued fractions, genus theory in weak arithmetic**: **NOT FOUND**.
  - Bovenzi–D'Aquino cite Lagarias 1980 on the complexity of x²−Dy²=−1, but only as complexity background.
  - Manders–Adleman, JCSS 16 (1978) 168–184, is complexity background: binary quadratic problems that are NP-complete.

---

## 6. E. Jeřábek beyond the 2010 MLQ paper

- His publication list (https://users.math.cas.cz/~jerabek/papers/PAPERS.html) has no paper on sums of two squares, Thue's lemma, or the provable
  existence of quadratic non-residues in IΔ0-type theories. **NOT FOUND**.
- Related work (**VERIFIED**, abstract and text):
  - "Integer factoring and modular square roots", JCSS 82 (2016). It shows that factoring randomly reduces to PPA and to WEAKPIGEON (PPP). It also shows unconditionally that PPA contains
    "square root computation modulo n, and finding quadratic nonresidues modulo n". The methods come from bounded arithmetic; Thm 4.2 (citing
    Jeřábek 2010) is in S^1_2+Count2(PV). These are search-problem results, not provability in IΔ0.
  - "Iterated multiplication in VTC0" (AML 61, 2022), side result: "there is a well-behaved Δ0 definition of modular powering in
    IΔ0+WPHP(Δ0)".
- Fermat's two-squares theorem in IΔ0+EQΣ0: Berarducci–Intrigila 1991, according to Dimitracopoulos' survey Thm 13. Jeřábek 2010 notes that mod-2
  counting by involutions (Heath-Brown, Zagier) proves it, but states no theorem of his own about two squares.

---

## 7. A theorem saying "every true Π1 sentence with polynomially bounded witnesses is provable in IΔ0+exp"?

**NOT FOUND, and it cannot exist in that naive form.**
- Every Π1 sentence is IΔ0-equivalent to ∀x φ(x) with φ ∈ Δ0. A bounded "witness" ∃y ≤ p(x) inside is already Δ0.
- HP Cor V.5.29 gives a true ∀Δ0 sentence, Con_Q, that IΔ0+exp does not prove.
- What does exist is Wilkie's exact characterization of the Π1 theorems of IΔ0+exp (HP Thm V.5.26/5.27): they are exactly the bounded ∀φ interpretable in Q on a cut, equivalently those
  provable in S^1_2 + {RCon_Q(k)}.

On the Diophantine side, the relevant class is the Adleman–Manders class 𝒟 (L. Adleman, K. Manders, "Diophantine complexity", FOCS 1976, pp. 81–88,
doi:10.1109/SFCS.1976.13). I could not get its abstract. Lipmaa 2003 (VERIFIED) describes it:
> "It has been an open question since [AM76], whether D = NP, where D is the class of sets S that have representing polynomials R_S,
> such that µ ∈ S iff for some polynomially long witness ω ∈ Z^m, R_S(µ;ω) = 0." "Adleman and Manders showed that several
> NP-complete problems belong to the class D and, based on that, conjectured that D = NP. … Jones and Matiyasevich [JM84] … proved
> that D = NP iff the set {(µ1,µ2): µ1 ≤2 µ2} belongs to D … Pollet [Pol03] … showed that when co-NLOGTIME ⊆ D then D = NP."

Note that the witness *bit-length* is polynomial: values are up to 2^{poly(|µ|)}, not poly(µ). That is the IΔ0+Ω1/#-scale, not the
IΔ0 value scale. Pollett 2003 (VERIFIED abstract) shows that I_5E_1 cannot prove 𝒟=NP and cannot prove MRDP. The link between
"Δ0 = Diophantine with value-bounded witnesses" and complexity is Wilkie's observation (item 4): MRDP in IΔ0 implies NP=coNP.

My remark, not from any source: by MRDP with exponential witness bounds plus log-padding one can presumably put Con(Q) into the form ∀u∃ȳ ≤ u^k
P(u,ȳ)=0. Then even "polynomially bounded Diophantine witnesses" would not rescue such a theorem. I found no source that states this.

---

## 8. Parikh's theorem

R. Parikh, "Existence and feasibility in arithmetic", JSL 36 (1971) 494–508, doi:10.2307/2269958 — **PARTLY**. The original is
paywalled; the first-page extract contains only the opening Bernays quotation. Statements by later authors:
- **Buss 1999** ("two papers of Parikh", author PDF, VERIFIED):
  - "Theorem 3 (Parikh [30]) If A(x,y) is a bounded formula with no additional free variables, and if IΔ0 can prove ∀x∃yA(x,y), then for
    some k, ℓ > 0, IΔ0 ⊢ ∀x∃y(y < x^k + ℓ ∧ A(x,y))." Buss adds: "Parikh presented a proof-theoretic proof based on Herbrand's theorem".
    Dimitracopoulos later noted the model-theoretic proof.
  - Also "Theorem 2 (Parikh [30]) There is no formula A(x,y,z) such that IΔ0 proves (1) ∀x∀y∃!zA(x,y,z), (2) ∀x∀y∀z(A(x,0,1) ∧ (A(x,y,z) →
    A(x,S(y),z·x))), (3) ∀x∀y∀z(A(x,y,z) → z ≠ 0)". In words, IΔ0 cannot prove exponentiation total.
- **Buss Handbook II, 1.2.7.1** (VERIFIED): "Parikh's Theorem. Let A(x⃗,y) be a bounded formula and T be a bounded theory. Suppose T ⊢
  (∀x⃗)(∃y)A(x⃗,y). Then there is a term t such that T also proves (∀x⃗)(∃y ≤ t)A(x⃗,y)."
- **HP Thm V.1.4** (VERIFIED, OCR noisy): for φ ∈ Σ0(f), π ∈ Π1(f), if IΣ0(f) + π ⊢ (∀x)(∃y)φ(x,y) (f monotone), then for some term t
  of L(f), IΣ0(f) + π ⊢ (∀x)(∃y ≤ t(x))φ(x,y). Cor V.1.6: the hierarchy IΣ0 ⊂ IΣ0+Ω1 ⊂ … ⊂ IΣ0+Exp ⊂ IΣ0+Superexp is proper.
- **Dimitracopoulos 1995 survey, Thm 3**: "If IΣ0 ⊢ ∀x∃yφ(x,y), where φ is Σ0, then there exists k ∈ N such that IΣ0 ⊢ ∀x∃y < x^k + k φ(x,y)."
