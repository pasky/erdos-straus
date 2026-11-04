# Literature report B: parity, Siegel zeros, and levels of distribution for P(4,15)

> **Errata (z56 K4LIT internal review):** see `Z56_K4LIT.md` §9 — errata there override this report (Dimitrov local-density issue; Banks/Lü–Wang–Wu unrefereed, conditional readings; Sedunova counts are representation-weighted; Siegel-zero ≤0.52 levels are residue-uniform; "no parity barrier" means total-Ω_𝒬 parity only — at BV level there is the hidden-prime barrier, Lemma P).


Target: P(4,15). There are infinitely many primes p ≡ 1 (mod 8) with p+4 ∈ S and 4p+1 ∈ S, where S = {n : every prime factor of n is ≡ 1 (mod 4)} and Q = {primes ≡ 3 (mod 4)}.
Note that p ≡ 1 (mod 8) gives p+4 ≡ 5 (mod 8) and 4p+1 ≡ 5 (mod 8). So **both sifted components are ≡ 1 (mod 4)**. This matters below.

Status legend:
- **VERIFIED** means I read the primary text myself (PDF or scan; OCR checked against page images where flagged).
- **SECONDARY** means the statement is quoted from another paper's verbatim restatement.
- **UNVERIFIED** means I only have a title or snippet, or I could not read the source.

Access notes:
- ams.org, books.google and worldscientific all sit behind Cloudflare/CAPTCHA. *Opera de Cribro* itself, the AMS TOC PDF, and the FI "illusory sieve" text could not be read.
- matwbn.icm.edu.pl (Acta Arith. scans) was reached after its Anubis proof-of-work check. The scans have no text layer, so I OCR'd them with tesseract and read the key pages as images.

---

## B1. Parity barrier for the half-dimensional (κ=1/2) sieve

### B1.1 Iwaniec, "The half dimensional sieve", Acta Arith. 29 (1976) 69–95. VERIFIED (page images pp. 69–74)
URL: https://matwbn.icm.edu.pl/ksiazki/aa/aa29/aa2914.pdf

- p. 69 (§1):
  > "Estimations of the 'sifting function' which are given in Theorem 1 cannot be essentially improved. Theorem 2 shows that in a special case the main term of the upper estimation coincides with the main term of the asymptotic formula for the sifting function. The fundamental result of the paper is included in Theorem 4."
- p. 71, **Theorem 1**: this is the κ=1/2 upper and lower bound, S(A,z) ≷ Ω(z)X{1 ∓ f(s)/√s or + F(s)/√s + O(e^{2K−s} log^{−γ} z)} ± Σ_{d<z^s, d|P(z)} |R(A,d)|, with γ = 1/2 − 1/((2−log 2)e). For 1 ≤ s ≤ 2:
  - 1 − f(s)/√s = √(e^C/(πs)) ∫_1^s dt/√(t(t−1))
  - 1 + F(s)/√s = 2√(e^C/(πs))
  - In particular f(1)=1, so the lower bound vanishes at s=1. This is sifting limit β = 1.
- pp. 71–72, **Theorem 2** (verbatim hypothesis):
  > "Let a′ denote the greatest odd divisor of a. … Theorem 2. Let us assume that a ∈ 𝒜 ⇒ a′ ≡ 1 (mod 4), 𝒫 ⊂ {p ≡ −1 (mod 4)}. Then, for Q⁶ < z² ≤ A := max_{a∈𝒜} a we have S(𝒜,z) = Ω(z)X{1 + F(s)/√s + O(e^{4K−s}((L+log Q)/log A)^γ)} + θ Σ_{d<A/Q, d|P(z)} |R(𝒜,d)|, where s = log A/log z and |θ| ≤ 1."

  So **when the parity of Ω_𝒫(a) is forced by a congruence (a′ ≡ 1 mod 4, sifting primes ≡ 3 mod 4), the upper-bound function F is an asymptotic equality.** The price is that the remainder runs over d < A/Q. That is level ≈ (max element)^{1−ε}, not X^{1/2}.
- p. 72, **Theorem 3**: this is the asymptotic for Σ b*(a), where b* = primitive representations a = u²+v², (u,v)=1. Hypothesis: a ≡ 1, 2 or 5 (mod 8), 𝒫 ⊂ {p ≡ −1 (mod 4)}. The remainder is again over d < A/Q.
- p. 72, **Theorem 4**: this is the asymptotic for Σ b(a), b = sums of two squares. Hypothesis: a′ ≡ 1 (mod 4), 𝒫 = {p ≡ −1 (mod 4)}, ω(p^α) = ω(p). The remainder is over d < A/Q, plus O(A/Q).
- p. 73, **Corollary 2**:
  - (2.1) Σ_{p<N} b(p−1) ~ (1/√2)Π(…)N/log^{3/2}N + θ₁E(N, N^{1−ε}).
  - (2.3) Σ_{n<N} b(n)b(n+1) = (3/8)N/log N{1+O(ε^γ)} + θ₃{B(N,N^{1−ε}) + B(N/2,N^{1−ε})}.
- pp. 73–74, remark (verbatim):
  > "(2.1) implies that Motohashi's conjecture [6] about the number of primes of the form x²+y²+1 ≤ N follows in its corrected form … from Halberstam's well-known conjecture [5] that E(N, N^{1−ε}) = O(N/log^A N). Similarly, (2.3) implies that Hooley's conjecture about Σ_{n<N} b(n)b(n+1) would follow from the estimate B(N, N^{1−ε}) = o(N/log N)."

**Relevance.** This is the primary answer to B1's key question.
- The κ=1/2 extremal configuration is exactly "Ω_𝒫(a) has fixed parity". For 𝒫 = Q that parity is χ₋₄(a′), so it is congruence-detectable.
- Iwaniec shows that for sequences inside a′ ≡ 1 (mod 4) the sieve becomes asymptotic. The only cost is level of distribution ~ A^{1−ε}.
- For one shifted-prime component this is Elliott–Halberstam strength, as Iwaniec says explicitly.
- Both components of P(4,15) satisfy the hypothesis a′ ≡ 1 (mod 4).

### B1.2 Iwaniec, "Rosser's sieve", Acta Arith. 36 (1980) 171–202. VERIFIED (OCR, §2.2, p. 175)
URL: https://matwbn.icm.edu.pl/ksiazki/aa/aa36/aa36210.pdf

> "2.2. The sieve of dimension 1/2 < κ < 1. The cases κ = 1/2 and κ = 1 have been considered in [9] and [12] respectively and the results obtained are best possible. The examples showing optimality of (1.4) for κ = 1/2 (see [9], [16]) and for κ = 1 (see [15], [16]) are quite different and none of them can be adapted for 1/2 < κ < 1."

References in that quote:
- [9] Iwaniec, *The half dimensional sieve*
- [12] Jurkat–Richert
- [15] Richert, unpublished
- [16] Selberg, *Sieve methods*, Proc. Sympos. Pure Math. 20 (1971) 311–351 (not read: UNVERIFIED)

**Relevance.** The κ=1/2 bounds are proved optimal, and the optimality examples come from [9] and Selberg [16]. In [9] the sharpness of F is exhibited by Theorem 2, i.e. by the congruence-parity sequences above. I did not see the κ=1/2 lower-bound (f) extremal example written out in the pages I read. My inference is that it is the complementary class a′ ≡ 3 (mod 4), with an odd number of 𝒫-factors.

### B1.3 Friedlander–Iwaniec, *Opera de Cribro* (AMS Coll. Publ. 57, 2010). TOC: SECONDARY (search snippets); contents UNVERIFIED
TOC fragments, from search-engine snippets of https://www.ams.org/bookstore/pspdf/coll-57-toc.pdf and coll057-endmatter.pdf:
- **Ch. 14, The Semi-Linear Sieve**: 14.1 Introduction (p. 275), 14.2 A Summary of Previous Results (275), 14.3 First Application (277), **14.4 Asymptotic Semi-Linear Sieve (278)**, 14.5 Applications of the Asymptotic Semi-Linear Sieve (281), **14.6 Shifted Primes as a Sum of Two Squares (282)**, 14.7 … (title not retrieved).
- Ch. 15, Applications—Choice but not Prime.
- **Ch. 16, Asymptotic Sieve and the Parity Principle** (pp. 331–343): 16.1 Distribution Functions (331), 16.2 The Basic Theorem (332), 16.3 Proof of the Basic … (title truncated in snippet).
- Ch. 11, The Beta-Sieve (Thms 11.12–11.13 give the β-sieve; Nath 2108.09212 cites them with β=1 for κ=1/2).
- Ch. 12 contains "The Remainder in a Well-Factorable Form" (p. 252); Maynard cites it as §12.7. Lemma 12.16 is cited by Teräväinen and Nath as "linear sieve weights are well-factorable".

Endmatter snippet: "The beta-sieve with κ = 1/2 is called the semi-linear sieve and several of its applications are featured in Chapter 14."

**Secondary description of §14.4 (VERIFIED as a quote of the blog).** K. Soundararajan, comment 78.4 on F. Calegari's *Persiflage* post "Prime divisors of polynomials" (29 May 2016). URLs: https://galoisrepresentations.org/2016/05/29/prime-divisors-of-polynomials/ ; compiled PDF http://www.math.uchicago.edu/~fcale/papers/blog.pdf p. 162.
> "this is a semi-linear sieve problem, and the best reference for that is probably the book of Friedlander and Iwaniec (chapter 14). They explain that the semi-linear sieve is capable of producing asymptotic formulas (as in the "sums of two squares" problem), under two basic conditions: (1) A parity restriction: one must sieve integers in a sequence A by primes in a set P, with the property that elements of A have an even number of divisors from P — this holds for sums of two squares if A is taken to be integers = 1 mod 4 and P the primes which are 3 mod 4 … (See [FI10, 14.4]). (2) a level of distribution condition: the sum of error terms in the sieve, up to the bound on p that you impose, must be under control. Condition (1) seems very intrinsic to the method (e.g., I don't see how to get a lower bound with the sieve for the integers where all prime factors are 3 mod 4)."

**Relevance.** This confirms that FI §14.4 ("asymptotic semi-linear sieve") is Iwaniec's Theorem 2 mechanism. The parity obstruction is removed precisely by the "a ≡ 1 (mod 4), sifting primes 3 (mod 4)" congruence. P(4,15) satisfies condition (1) for each component, so only condition (2), level, remains.

### B1.4 Friedlander–Iwaniec, "Hyperbolic prime number theorem", Acta Math. 202 (2009) 1–19. VERIFIED (full text)
URL: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6709-11511_2009_Article_33.pdf

- **Assumption A(θ)** (p. 3): E(x,Q) = Σ_{q≤Q} max_{(a,q)=1} max_{y≤x} |ψ(y;q,a) − y/φ(q)| ≪ x(log x)^{−A} for Q = x^{θ−ε}.
- **Theorem 2**: "If A(θ) holds for some θ, less than 1 but sufficiently close to 1, then … c₁x/log x < π_Γ(x) < c₂x/log x". The text continues: "the upper bound is unconditional".
- **Theorem 4** (p. 5): under the same assumption, S(x) = Σ_{n≤x} r(n−2) r(n+2) Λ(n) ≍ x.
- **Theorem 5** (unconditional, via [BFI, Theorem 9]): T(x) = Σ_{n≤x} r(n−2)r(n+2)Λ(n+2), which reduces to Σ_p r(p−4) log p, has an asymptotic formula. This is a single-component result.
- §6 (pp. 10–11), the parity mechanism and the level obstruction, verbatim:
  > "We detect the factor b(n−2) by the semilinear sieve with respect to the set P = {p ≡ 3 (mod 4)} … Here √x suffices because, if n ≡ 1 (mod 4) has one prime factor from P, it must have a second one."

  > "Since the sieving limit for the semilinear sieve is β = 1 and our level of distribution is D = D(x) < √x, we cannot successfully apply the lower bound sieve to S(A(δ),P,√x), but we can come close to this."

  Here D = x^{θ−1/2−ϑ−ε} (6.10). The other factor r(n+2) is opened as Σ_{k≤√x} χ(k), so the moduli are 4δdk ≤ x^θ. This is why θ must be near 1.
- §7: the residual integers with exactly two P-primes ≥ z are bounded by switching plus upper-bound sieves. The proof takes ϑ = (1−θ)/2 and s = 2−θ.
- p. 14:
  > "The latter counts survivors of two linear sieves, while the former counts survivors of one linear and two semi-linear sieves. The assumption of the full conjecture A(1) narrowly misses resolving the twin prime conjecture … whereas the extra flexibility in the sum S(x) allows us to succeed, even with the weaker assumption."

**Relevance.** This is the exact structural analogue of P(4,15): one prime and two half-dimensional components, with no parity barrier because both components are ≡ 1 (mod 4). The proof needs A(θ), θ near 1. That confirms our internal "EH-strength" finding.

The port to (p+4, 4p+1) needs three things:
- the shifted-convolution input Lemma 4.2 for r(n+4)r(4n+1), proved by the Lemma 4.1 Weil-bound route;
- the forms n+4 and 4n+1 in place of n±2;
- b (all prime factors 1 mod 4) rather than r for the second component. Large Q-squares are negligible; small ones are handled at small primes.

### B1.5 Unconditional one-exact-component results (BV level). VERIFIED (secondary statements, read in full intros)
- **Iwaniec**, "Primes of the type φ(x,y)+A where φ is a quadratic form", Acta Arith. 21 (1972) 203–234 (title from refs). Nath–Xie report:
  > "in his celebrated work [10], Iwaniec used the semi-linear sieve to establish the matching lower bound #{p ≤ x : p = m²+n²+1} ≫ x/(log x)^{3/2}."

  Opera §14.6 "Shifted Primes as a Sum of Two Squares" presumably reproduces this (UNVERIFIED).
- **Nath–Xie**, arXiv:2501.16723 (v3 2026). URL https://arxiv.org/abs/2501.16723
  - **Theorem 1.1**: #{p ≤ x : p = m²+n²+1, Ω(p+2) ≤ 9} ≫ x/(log x)^{5/2}.
  - The method is a vector sieve, semi-linear × linear (Prop. 3.10), plus Iwaniec's "switching principle" (Prop. 4.2), with BV (Pan's version).
  - Remark 1.1: under a version of EH (their (3.3) for q ≤ x^{1−ε}) one gets Ω(p+2) ≤ 3.
  - Footnote on FI 2009: "The upper bound is established without any assumption."

  **Relevance.** This is the state of the art for "one exact half-dim shift + bounded anatomy of the other" at level 1/2. It matches our internal BV result. No paper found gets two exact half-dimensional shifts of primes unconditionally.

### B1.6 "Sieve with character information / pretentious parity"
Iwaniec's Theorem 2 and FI §14.4 are the literature's version of "sieve aware of χ₋₄-parity". Apart from those, I found no source treating any of the following:
- Selberg Λ² weights twisted by χ;
- "pretentious parity" for κ=1/2;
- sieving sequences inside n ≡ 1 (mod 4) by Q beyond the asymptotic semi-linear sieve.

Granville (B2.6) is the linear-sieve analogue: extremal examples become realised when the Liouville parity is "character-like" because of a Siegel zero. **Nothing further found.**

---

## B2. Exceptional (Siegel) zeros

### B2.1 Heath-Brown, "Prime twins and Siegel zeros", Proc. LMS (3) 47 (1983) 193–224. SECONDARY (as restated in Tao–Teräväinen Thm 1.5(i))
> "[11, Theorem 1] For any distinct fixed natural numbers h₁,h₂, one has E_{n≤x}Λ(n+h₁)Λ(n+h₂) = 𝔖 + O(1/log log η) uniformly for all q_χ^{250} ≤ x ≤ q_χ^{300}"

### B2.2 Tao–Teräväinen, arXiv:2109.06291, "The Hardy–Littlewood–Chowla conjecture in the presence of a Siegel zero". VERIFIED
- **Theorem 1.6** (verbatim):
  > "Let 0 ≤ k ≤ 2 and ℓ ≥ 0, and let h₁,…,h_k, h′₁,…,h′_ℓ be fixed distinct natural numbers. Suppose that one has a Siegel zero β with associated conductor q_χ and quality η. Let 0 < ε₀ < 1 be fixed, and let x lie in the range q_χ^{10k+1/2+ε₀} ≤ x ≤ q_χ^{η^{1/2}}. Then we have E_{n≤x}Λ(n+h₁)···Λ(n+h_k)λ(n+h′₁)···λ(n+h′_ℓ) = 𝔖 + O(1/log^{1/(10 max(1,k))} η)".
- Limitation stated just after Remark 1.7:
  > "This latter restriction [k ≤ 2] is an inherent limitation of our current state of knowledge of correlations for functions like the divisor function τ := 1∗1; in particular, k-point correlations E_{n≤x}τ(n+h₁)···τ(n+h_k) are currently only well understood when k ≤ 2."
- §1.2: "the von Mangoldt function Λ = μ∗log similarly 'pretends' to be like χ∗log … τ has level of distribution at least 2/3, the key point being that this is larger than 1/2."

### B2.3 Matomäki–Merikoski, arXiv:2112.11412 (IMRN 2023). VERIFIED (intro)
- Abstract: an asymptotic for Σ_{n≤X} Λ(n)Λ(±n+h) uniformly for h = O(X), assuming Siegel zeros.
- Intro, describing the illusory sieve:
  > "Friedlander and Iwaniec [4: The illusory sieve, IJNT 1 (2005) 459–494] have shown that the error in (8) [Λ ≈ χ∗log] can be controlled if we can solve the corresponding ternary divisor problem."

### B2.4 Merikoski, arXiv:2108.01355, "Exceptional characters and prime numbers in sparse sets". VERIFIED
- Intro:
  > "For their [FI illusory sieve] method it is required to solve the corresponding ternary divisor problem … This essentially comes down to showing that the sequence has an exponent of distribution 2/3 − ε."
- **Theorem 1** (conditional): infinitely many primes a²+b⁸.
- **Theorem 15** (general lower-bound sieve under an exceptional character χ_D, D = x^{o(1)}), verbatim:
  > "Suppose that the exponent of distribution is at least α = 2/3 − γ for some γ < 1/6 (in the sense of Propositions 7 and 8). Then Σ_{n∼x}Λ(n)a_n ≥ (1 − 2 log((1+3γ)/(1−6γ)) − O(L(1,χ_D) log⁵x) − o(1)) Σ_{n∼x}Λ(n)b_n … the lower bound is non-trivial as soon as the exponent of distribution satisfies α > (1+√e)/(1+2√e) = 0.61634..."
- Props 7–8 are the Type I and "Type I χ" information: Σ_{d∼D} α(d) Σ a_{dm} with arbitrary divisor-bounded α, D ≤ x^{α}.

### B2.5 Levels for primes in APs under an exceptional character
- **FI 2003**, "Exceptional characters and prime numbers in arithmetic progressions", IMRN 2003 no. 37, 2033–2050. SECONDARY (Wright's restatement, Thm 2.1 of arXiv:2609.35950):
  > "Let χ be a real character mod D. Let x > D^r with r = 554,401, let q = x^θ with θ < 233/462, and let (a,q) = 1. Then ψ(x,q,a) = (ψ(x)/φ(q))(1 − χ(aD/(q,D))) + O(L(1,χ)(log x)^{r^r})."

  Sachpazis (arXiv:2511.16452) abstract: FI's asymptotic is non-trivial "for moduli q ≤ x^{1/2+1/231}".
- **Wright**, arXiv:2609.35950. VERIFIED.
  - **Thm 3.1**: individual q ≤ x^{30/59−ν}.
  - **Thm 3.2**: averaged q ∼ Q < x^{16/31−ν}, "Elliott–Halberstam-type".
- **Wright**, arXiv:2311.12470: same exponents in its abstract.

**Relevance.** A Siegel zero lifts the prime level only to ≈ 0.508 (individual) and ≈ 0.516 (averaged). FI 2009 needs θ ≈ 1, so this is nowhere near enough.

### B2.6 Granville, arXiv:2010.01211, "Sieving intervals and Siegel zeros". VERIFIED (abstract only)
> "Assuming that there exist (infinitely many) Siegel zeros, we show that the (Rosser-)Jurkat-Richert bounds in the linear sieve cannot be improved …"

**Relevance.** Siegel zeros *realise* the linear-sieve extremal examples. I found no half-dimensional analogue.

### B2.7 Sums of two squares at shifted primes under Siegel zeros
I found no paper proving any half-dimensional or sums-of-two-squares statement at one or two shifts of primes conditional on Siegel zeros. I searched arXiv and the web for "Siegel zero / exceptional character" together with "sums of two squares / semi-linear / half-dimensional". **Nothing found.**

The closest verified statements are TT Thm 1.6 (≤ 2 Λ-factors plus Liouville factors) and Merikoski Thm 15 (primes in a sequence with Type I level > 0.6163).

---

## B3. Levels of distribution beyond 1/2

### B3(i) Fixed integer residue a, weighted moduli
- **BFI**, Acta Math. 156 (1986), **Theorem 10**. SECONDARY (Maynard II "Theorem A"; Lichtman (1.3)):
  > "Let a ∈ Z and A,ε > 0. Let λ_q be a sequence which is well-factorable of level Q ≤ x^{4/7−ε}. Then Σ_{q≤Q,(q,a)=1} λ_q(π(x;q,a) − π(x)/φ(q)) ≪_{a,A,ε} x/(log x)^A."
- **Maynard I**, arXiv:2006.06572, **Thm 1.1**. VERIFIED. Absolute values; fixed a; q₁ ≤ Q₁, q₂ ≤ Q₂ with Q₁Q₂² < x^{1−100ε}, Q₁¹²Q₂⁷ < x^{4−100ε}, Q₁²⁰Q₂¹⁹ < x^{10−100ε}.
  - **Cor 1.4**: q₁ ≤ x^{1/21}, q₂ ≤ x^{10/21−ε}.
  - **Cor 1.3**: all but O(δQ) moduli q ∼ x^{1/2+δ}, δ < 1/55.
- **Maynard II**, arXiv:2006.07088. VERIFIED.
  - **Thm 1.1**: triply well-factorable, Q ≤ x^{3/5−ε}.
  - **Thm 1.2**: well-factorable *linear* upper-bound sieve weights, D ≤ x^{7/12−ε}.
- **Lichtman**, arXiv:2309.08522. VERIFIED.
  - **Cor 1.5**: triply well-factorable, ϑ < 66/107.
  - **Thm 1.7**: ϑ = (5−4θ)/(8−6θ) − ε, uniformly for 0 < |a| < x^ε; and ϑ₁ = (5−θ)/8 − ε for |a| < x^{1+ε}.
- **Pascadi**, arXiv:2505.00653, **Thm 1.3**. VERIFIED. For a ∈ Z∖{0}:
  - (i) Q ≤ x^{5/8−ε} with triply-well-factorable weights;
  - (ii) Q ≤ x^{3/5−ε} with upper-bound well-factorable linear sieve weights;
  - **Thm 5.4** (not read) covers upper and lower linear weights with a factorization-dependent exponent.
- **Stadlmann**, arXiv:2309.00425, **Thm 1**. VERIFIED. x^δ-smooth moduli, exponent 1/2 + 1/40 − ε. Also **Cor 2**: MPZ[ω,δ] whenever 80ω + (80/3)δ < 1.

### B3(ii) Residue depending on the factorization of the modulus
All B3(i) results require **one integer a** (|a| < x^{1+ε} at most) for all q. In the product sieve on (p+4)(4p+1) the residue mod d₁d₂ is CRT(−4 mod d₁, −4̄ mod d₂). Those are the roots of P(n) = (n+4)(4n+1) prime by prime. **B3(i) does not apply as stated.**

Results that do allow this:
- **Polymath8a**, arXiv:1402.0811, **Theorem 1.1**. VERIFIED.
  > "Let θ = 1/2 + 7/300 … For all primes p, let a_p be a fixed invertible residue class modulo p, and for q ≥ 1 squarefree, denote by a_q the unique invertible residue class modulo q such that a_q ≡ a_p modulo all primes p dividing q. There exists δ > 0 … Σ_{q≤x^{θ−ε}, q x^δ-smooth, squarefree} |ψ(x;q,a_q) − x/φ(q)| ≪ x log^{−A} x … independent of the residue classes (a_p)."

  Further statements in the same paper:
  > "Zhang establishes a weaker form of Theorem 1.1, with θ = 1/2 + 1/584, and with the a_q required to be roots of a polynomial P of the form ∏_{j≠i}(n + h_j − h_i)"

  > "[BFI, Fouvry–Iwaniec] … with θ as large as 1/2 + 1/14, but with the restriction that the residue classes a_p are obtained by reduction modulo p of a fixed integer a ≥ 1."

  **Claim 2.3, MPZ^{(i)}[ϖ,δ]**: the same estimate for densely divisible moduli D_I^{(i)}(x^δ), with one integer a coprime to P_I. That is equivalent to arbitrary a_p.
  - **Thm 2.4(i)**: MPZ^{(4)}[ϖ,δ] for 600ϖ + 180δ < 7.
- **Stadlmann Cor 2** improves this to 1/2 + 1/40 for x^δ-smooth moduli.
- Two roots per prime (−4 and −4̄): uniformity in (a_p) handles them by averaging over random root choices, up to divisor-weight bookkeeping. This step is my inference; it is the standard GPY/Zhang usage.

**Caveat.** These need x^δ-smooth or densely divisible moduli. Classical β-sieve weights with sifting range z ≫ x^δ are not supported on such moduli.

### B3(iii) Well-factorability of semi-linear (κ=1/2, β=1) weights
- Maynard II §9, VERIFIED, quotes the property for the **linear** sieve:
  > "if d ∈ D⁺(D) and D = D₁D₂ then d = d₁d₂ with d₁ ≤ D₁ and d₂ ≤ D₂"

  Here D⁺(D) = {p₁⋯p_r : p₁⋯p_{2j}p_{2j+1}³ ≤ D}.

  Iwaniec, "A new form of the error term in the linear sieve", Acta Arith. 37 (1980) 307–320, is titled and cited as a *linear*-sieve result. I found no statement that Iwaniec's bilinear-remainder theorem covers κ=1/2.
- **Teräväinen**, arXiv:1611.08585, **Lemma 9.2 / Remarks 9.3–9.4**. VERIFIED. Only *partial* factorability of semilinear weights holds:
  - Lower-bound support D^{−,SEM} = {p₁⋯p_{2k−1}p_{2k}² ≤ x^ρ}, with ρ = (3/7)(1−4θ) − ε.
  - Upper bound: ρ = (2/5)(1−4θ) − ε.
  - Factorization d = d₁d₂ with d₁ ≤ D and d₁d₂² ≤ x^{1−4θ−2ε²}/D.
  - "The exponent ρ = 3/7(1−4θ) − ε is optimal in Lemma 9.2."
  - Reused as **Nath, arXiv:2108.09212, Lemma 3.4** ("Partial well-factorability of semi-linear sieve").
- My own check, consistent with the above: the β=1 upper set contains d = p₁p₂ with p₁ ≈ D^{1/2}, p₂ < p₁. Such d cannot be split as D^{0.3}·D^{0.7}. **So κ=1/2 β-sieve weights are not well-factorable in the BFI sense.** BFI/Maynard/Lichtman/Pascadi therefore do not directly raise the level of a semi-linear sieve. None of those papers states a κ=1/2 result; I searched for one.

---

## VERDICT

**(a) Precise parity barrier for P(4,15).** In the classical (Selberg/Bombieri) sense there is **none**.
- For each component, the half-dimensional extremal configuration is the fixed parity of Ω_Q (Rosser's sieve §2.2; Iwaniec 1976 Thm 2). With sifting set Q that parity is χ₋₄.
- p+4 ≡ 4p+1 ≡ 5 (mod 8), so both components lie in the congruence class where the parity is forced even. This is exactly Iwaniec's Theorem 2/4 hypothesis, which FI §14.4 call the "asymptotic semi-linear sieve" (Soundararajan's summary).
- The literature's obstruction is **level of distribution**:
  - The semi-linear sieving limit is β = 1, so each component needs level D > z with z ≈ x^{1/2}.
  - Equivalently, Iwaniec's asymptotic remainder Σ_{d<A/Q}|R| needs level ≈ x^{1−ε}.
  - For one shifted-prime component, Iwaniec says (1976, pp. 73–74) that the asymptotic follows from Halberstam's E(N,N^{1−ε}).
  - With BV you get one exact component (Iwaniec 1972) plus almost-prime or bounded anatomy in the other (Nath–Xie Thm 1.1).
  - Two exact components are proved only conditionally: FI 2009 Thm 4 (n∓2 analogue, Λ(n)r(n−2)r(n+2) ≍ x) needs A(θ), θ near 1, with max over residues.
- No source claims the level-~1 requirement is a *proven* barrier. It is the requirement of every known method.

**(b) A Siegel-zero-conditional proof is not obtainable from existing theorems.** Each candidate route has a missing input:
1. *Prime level under a Siegel zero.*
   - Best available: x^{30/59} individually and x^{16/31} on average (Wright Thms 3.1/3.2), or x^{1/2+1/231} (FI 2003).
   - FI 2009 needs A(θ), θ → 1.
2. *Tao–Teräväinen / illusory-sieve route.*
   - Λ ≈ χ_D∗log turns Σ Λ(n) r(n+4) r(4n+1) into a three-point correlation of divisor-type functions.
   - TT explicitly say that k-point τ-correlations are understood only for k ≤ 2; FI's illusory sieve needs the ternary divisor problem (Matomäki–Merikoski; Merikoski).
3. *Merikoski Thm 15 lower-bound sieve* with a_n = r(n+4)r(4n+1), plus small-Q cleanup. It would need:
   - Type I and Type-I-χ distribution of a_n to exponent α > 0.61634, with arbitrary divisor-bounded α(d) over n ≡ 0 (mod d);
   - a comparison sequence b_n with known Σ Λ b_n;
   - x in the conductor window exp(log^{10}D) < x < exp(log^{16}D).

   Only x^{1/12} is verified (FI 2009 Lemma 4.2, Weil bound). I found no result giving the shifted convolution Σ_{n≡0(d)} r(n+4)r(4n+1) to level > 0.616. **That input is the precise missing theorem.**

   Plausibility is therefore "maybe, with a new spectral shifted-convolution-in-APs theorem". There is no Siegel-zero proof of P(4,15) to cite.

**(c) Best level that could feed the product (total dimension 1) sieve on (p+4)(4p+1).**
- With sharp β-sieve weights the usable level is **1/2 (BV)**. BV is uniform in residues, so the CRT-mixed residue classes are fine.
- Every level-beyond-1/2 result for a fixed residue (BFI 4/7, Maynard 3/5 and 7/12, Lichtman 66/107, Pascadi 5/8 triply and 3/5 linear) requires one integer residue a. They therefore do not cover CRT(−4 mod d₁, −4̄ mod d₂).
- Those fixed-residue results also need well-factorable weights, and κ=1/2 weights are only partially factorable (Teräväinen Lemma 9.2, Rem. 9.3–9.4).
- Results that do allow residues to be roots of P mod each prime are Zhang (1/2+1/584), Polymath8a Thm 1.1 (1/2+7/300) and Stadlmann (1/2+1/40). They hold only for x^δ-smooth or densely divisible moduli, which fits fundamental-lemma/GPY-type weights rather than z ≈ √x semi-linear sifting.
- Net: at most **1/2 + 1/40 − ε** (smooth moduli), and effectively **1/2** for the sieve actually needed. Nothing approaches the ~1 that FI-type arguments use.
