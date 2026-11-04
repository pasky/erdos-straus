# LIT_CHECK — literature verification (z56 / central)

Status labels: **VERIFIED-PRIMARY** = statement read in the paper itself (arXiv/publisher PDF);
**VERIFIED-SECONDARY** = read in a named secondary source that is quoted; **UNVERIFIED** = not found / not accessed.
Lines marked *(derived)* are my own substitution into a quoted statement, not a claim of any source.
PDFs fetched to /tmp/lit (arXiv, numdam, matwbn.icm.edu.pl, jtnb.centre-mersenne.org).

---------------------------------------------------------------------------------------------------
## 1. Nair–Tenenbaum (Acta Math. 180 (1998) 119–144) and Shiu (Crelle 313 (1980) 161–170)

Original NT PDF: not obtainable (Project Euclid / Springer bot walls). Shiu original: not found online.

**NT main theorem — VERIFIED-SECONDARY** (K. Henriot, "Nair–Tenenbaum bounds uniform with respect to the
discriminant", arXiv:1102.1643 = Math. Proc. Camb. Phil. Soc. 152 (2012) 405–424, p.1–2, "Theorem 1 (Nair and Tenenbaum)"):
> "For fixed constants k ⩾ 1, A ⩾ 1, B ⩾ 1, ε > 0, let M_k(A,B,ε) be the class of non-negative functions F of k
> variables such that F(a1b1,…,akbk) ⩽ min(A^{Ω(a1···ak)}, B(a1···ak)^ε) F(b1,…,bk) for all ai, bj such that
> (a1···ak, b1···bk) = 1."
> "Theorem 1 (Nair and Tenenbaum). Let k ⩾ 1. Let Q1,…,Qk ∈ Z[X] be k pairwise coprime and irreducible polynomials.
> Let Q = Q1···Qk and denote by g its degree and D its discriminant. Let ρ_{Qj}(n) (resp. ρ(n)) denote the number of
> zeroes of Qj (resp. Q) modulo n … Assume Q has no fixed prime divisor. Let 0 < α < 1, 0 < δ < 1, A ⩾ 1 and B ⩾ 1.
> Let ε ⩽ αδ/(12g²) and F ∈ M_k(A,B,ε). We have, uniformly in x ⩾ c0‖Q‖^δ and x^α < y ⩽ x,
> Σ_{x<n⩽x+y} F(|Q1(n)|,…,|Qk(n)|) ≪ y Π_{p⩽x}(1 − ρ(p)/p) Σ_{n1···nk⩽x} F(n1,…,nk) ρ_{Q1}(n1)···ρ_{Qk}(nk)/(n1···nk),
> where c0 depends at most on g, α, δ, A, B and the implicit constant depends at most on g, D, α, δ, A, B."

Henriot's caveats (p.1 & p.5): "Nair and Tenenbaum do not require the polynomials Qj to be irreducible and pairwise
coprime : this assumption is made here merely to simplify the statement"; and "Nair and Tenenbaum [10] actually
consider functions F satisfying the above property for all ai, bj such that (ai, bi) = 1, although the proof … requires
this property only for … (a1···ak, b1···bk) = 1." Henriot (p.7) also says NT "Theorem 3" is the analogue over primes
x<p⩽x+y. (So for k=1 the NT class is: F ⩾ 0, F(ab) ⩽ min(A^{Ω(a)}, B a^ε) F(b) whenever (a,b)=1.)

*(derived)* Q(n)=n, k=1: ρ(p)=1, g=1, so Σ_{x<n⩽x+y} F(n) ≪ y Π_{p⩽x}(1−1/p) Σ_{n⩽x} F(n)/n ≍ (y/log x) Σ_{n⩽x}F(n)/n
for x^α < y ⩽ x. (Bordellès' explicit version below states exactly this shape.)

Related explicit statement — VERIFIED-PRIMARY: O. Bordellès, arXiv:2402.12333, Theorem 1 (p.2):
> "Let ℓ ⩾ 1 and f be a positive arithmetic function such that there exists k ∈ Z⩾1 such that, for all (m,n), we
> have f(mn) ⩽ τ_k(m) f(n). (1.1) Then, uniformly for all x ⩾ exp(728 (12eℓ)^28 log(192eℓ)) and x^{1/ℓ} ⩽ y ⩽ x,
> Σ_{x−y<n⩽x} f(n) ⩽ Λ(k,ℓ) (y/log x) Σ_{n⩽x} f(n)/n" (Λ explicit).

**Shiu Theorem 1 — VERIFIED-SECONDARY** (two concordant secondary statements):
- Bordellès arXiv:2402.12333 p.1, "Theorem A": "Let (ε,η,θ) ∈ ]0,1/2[³, a < q ∈ Z⩾1 such that (a,q)=1, and f be a
  non-negative multiplicative function satisfying ∃A>0, f(p^α) ⩽ A^α, ∃B=B(η)>0, f(n) ⩽ Bn^η … Then, uniformly for
  q < y^{1−θ} and 1 ⩽ x^ε ⩽ y ⩽ x, Σ_{x−y<n⩽x, n≡a (q)} f(n) ≪ (y/φ(q)) (1/log x) exp(Σ_{p⩽x, p∤q} f(p)/p)."
- Henriot p.1: same bound "in the range q < y^{1−β}, x^α ⩽ y ⩽ x"; adds "Shiu's result in [12] is actually stated in
  a slightly different way, which is however easily seen to be equivalent to the above."
  (Exact original wording/numbering of Shiu's Theorem 1: UNVERIFIED.)

---------------------------------------------------------------------------------------------------
## 2. Erdős–Hooley Δ(n) = max_u #{d | n : e^u < d ⩽ e^{u+1}}

**(a) Δ(mn) ⩽ τ(m)Δ(n) — VERIFIED-SECONDARY** (attributed to Hall–Tenenbaum, *Divisors*, Lemma 61.1):
- de la Bretèche–Tenenbaum, "Two upper bounds for the Erdős–Hooley Delta-function", arXiv:2210.13897
  (Sci. China Math. 66 (2023) 2683–2692), p.2: "Considering the inequality (see [5; lemma 61.1])
  (2·1) Δ(mn) ⩽ τ(m)Δ(n) (m ⩾ 1, n ⩾ 1)", [5] = Hall & Tenenbaum, *Divisors*, CUP 1988. Note: no coprimality.
- Bordellès arXiv:2402.12333 p.3: "It is well-known by [9, Lemma 61.1] that the function Δ_k satisfies (1.1)"
  (i.e. Δ_k(mn) ⩽ τ_k(m)Δ_k(n)). Also trivially 1 ⩽ Δ ⩽ τ (Koukoulopoulos–Tao p.1).
  Hooley 1979 (PLMS 38, 115–151) itself: not accessed (UNVERIFIED there).

**(b) Mean value — VERIFIED-PRIMARY**
- Koukoulopoulos–Tao, arXiv:2306.08615 (PLMS (3) 127 (2023) 1865–1885), p.2: "Theorem 1 (Mean value bound). For
  x ⩾ 1, we have Σ_{n⩽x} Δ(n) ≪ x(Log₂ x)^{11/4}." ✔ exponent 11/4 confirmed.
- **Superseded**: de la Bretèche–Tenenbaum, "Note on the mean value of the Erdős–Hooley Delta-function",
  arXiv:2309.03958v14 (Acta Arith. 219.4 (2025) 379–394), p.2: "Theorem 1.1. For all large real x, we have
  (1·3) S(x) ≪ x(log₂ x)^{5/2}." Also (p.3, (1·7)): "if F ∈ Z[X] is an irreducible polynomial … Σ_{n⩽x} Δ(|F(n)|)
  ≪_F x(log₂ x)^{5/2}".  Current best per dlB–T arXiv:2512.05652 p.1: "x(log₂ x)^{1+η+o(1)} ≪ S(x) ≪ x(log₂ x)^{5/2},
  where η ≈ 0.353327".
- Lower bound: Ford–Koukoulopoulos–Tao, arXiv:2308.11987 (PLMS (3) 129 (2024) e12618), p.2: "Theorem 2. For any
  ε > 0 and all x ⩾ 1, we have Σ_{n⩽x} Δ(n) ≫_ε x(Log₂ x)^{1+η*−ε} ⩾ x(Log₂ x)^{1+η−ε}", η = 0.353327…
  (FKT p.3 and Bordellès p.3 also quote "x(log log x)^{3/2} ≪ ΣΔ(n)" from an earlier dlB–T preprint version; I could
  not find a 3/2 lower bound in v14 of 2309.03958 → treat that 3/2 lower bound as UNVERIFIED.)

**(c) Short-interval sums of Δ — VERIFIED-PRIMARY** (yes, stated explicitly):
- de la Bretèche–Tenenbaum, "On moments of the Erdős–Hooley Delta-function", arXiv:2512.05652 (Dec 2025), p.2:
  "Inserting (1·5) into the proof of [13; cor. 4] [=Nair–Tenenbaum] readily yields … Corollary 1.2. Let F ∈ Z[X] be
  irreducible with no fixed prime divisor. Then, for any t ⩾ 1 and ε > 0, we have
  Σ_{x<n⩽x+y} Δ(|F(n)|)^t ≪ y(log x)^{β(t,1)−1}(log₂ x)^{t+1+δ(t,1)/2} provided x^ε ⩽ y ⩽ x",
  with β(t,z)=2^t z − t, z_t = t/(2^t−1), δ = 1_{z=z_t}.
  *(derived)* F(X)=X, t=1: β(1,1)=1, z_1=1 ⇒ δ=1, giving Σ_{x<n⩽x+y} Δ(n) ≪ y(log₂ x)^{5/2} for x^ε ⩽ y ⩽ x.
- Bordellès arXiv:2402.12333 p.3, Corollary 2: "Uniformly for all x ⩾ exp(728(12eℓ)^28 log(192eℓ)) and
  x^{1/ℓ} ⩽ y ⩽ x, we have Σ_{x−y<n⩽x} Δ(n) ⩽ φ(ℓ) y(log x)^{−1+4/π}" (explicit, weaker exponent; φ(ℓ)=16748Λ(2,ℓ)).

---------------------------------------------------------------------------------------------------
## 3. Pointwise Δ(x+h) − Δ(x) (Dirichlet divisor error term) in short intervals

**Ivić, JTNB 21 (2009) 251–261** (publisher PDF jtnb.669; arXiv:0708.1601 lists "195-205", publisher header says
251-261) — **VERIFIED-PRIMARY**, p.254:
> "An omega-result analogous to (1.11) holds for Δ(x+h) − Δ(x) as well, namely
> (1.12) Δ(x+h) − Δ(x) = Ω(√h log^{3/2}(√x/h)) (x^ε ⩽ h ⩽ x^{1/2−ε}).
> Concerning the true order of Δ_k(x+h) − Δ_k(x), we remark that on the basis of (1.9) M. Jutila [4] conjectured that
> (1.13) Δ(x+h) − Δ(x) ≪_ε x^ε √h (x^ε ⩽ h ⩽ x^{1/2−ε}), which would be close to best possible, in view of (1.12)."
Also p.253 ((1.5)–(1.6)): trivial Δ_k(x+h)−Δ_k(x) ≪_ε x^ε h, and via Shiu "Δ_k(x+h) − Δ_k(x) ≪ h log^{k−1} x
(x^ε ⩽ h ⩽ x) as the 'trivial' bound". [4] = Jutila, Ann. Univ. Turku. Ser. AI 186 (1984) 23–30 (not accessed).

**Ivić–Zhai, "On the Dirichlet divisor problem in short intervals", arXiv:1209.0872** — **VERIFIED-PRIMARY**:
- p.3: "The formula (2.1) led Jutila [14] to propose Conjecture 3. For any 0 < ε < 1/4 and x^ε ⩽ U ⩽ x^{1/2−ε} we have
  (2.5) Δ(x+U) − Δ(x) ≪_ε x^ε √U. This conjecture is much stronger than the unconditional estimate
  (2.6) Δ(x+U) − Δ(x) ≪_ε x^ε U (1 ≪ U ⩽ x) … On the other hand, from (1.1) one obtains by trivial estimation
  (2.7) Δ(x+U) − Δ(x) ≪_ε x^{131/416+ε} (1 ≪ U ≪ x)." (So Jutila's conjecture is stated as open.)
- p.4, "Theorem 1. We have (3.1) Δ(x+U) − Δ(x) ≪_ε x^{1/4+ε}U^{1/4} (1 ≪ U ≪ x^{3/5}), and
  (3.2) Δ(x+U) − Δ(x) ≪_ε x^{2/9+ε}U^{1/3} (1 ≪ U ≪ x^{2/3})."
- p.6: "Note that x^{1/4}U^{1/4} ⩽ U for U ⩾ x^{1/3}, hence for x^{1/3} ⩽ U ⩽ x^{3/5} we obtain an improvement over (2.6)".
  *(derived)* At U = x^{1/4}: (3.1) gives x^{5/16+ε}, (3.2) gives x^{11/36+ε}; both exceed the trivial x^{1/4+ε}.
  So **no power-saving pointwise bound for h = x^{1/4} was found** in any source read.
- Larger-h log-saving (all intervals, not power saving): Matomäki–Radziwiłł–Shao–Tao–Teräväinen, arXiv:2204.03754
  (Forum Math. Pi 11 (2023) e29), abstract: Σ_{X<n⩽X+H}(f(n)−f^♯(n))F(g(n)Γ) ≪ H log^{−A} X "when θ = 5/8 and
  f ∈ {Λ, μ, d_k} or θ = 1/3 and f = d_2", range X^{θ+ε} ⩽ H ⩽ X^{1−ε}.

**Current Δ exponent — VERIFIED-PRIMARY**: Li–Yang arXiv:2308.14859, p.2: "Theorem 1.2. R(X) = O_ε(X^{θ*+ε}) and
Δ(X) = O_ε(X^{θ*+ε}) for all ε > 0, where θ* = 0.314483…" (θ* = 0.3144831759741…, Definition 1.1).

**Hardy Ω — VERIFIED-SECONDARY**:
- Li–Yang p.1–2: "a series of papers [9],[10] and [11] by G. H. Hardy, who proved that both R(X) and Δ(X) are
  (1.3) Ω((X log X)^{1/4}) … Since then, no one has been able to enlarge the exponent 1/4". (Note: they attach the
  (log X)^{1/4} factor to both; I did not check Hardy.)
- Ivić–Zhai p.1–2: Cramér's mean square ∫_1^T Δ²(x)dx = (ζ(3/2))⁴/(6π²ζ(3)) T^{3/2} + F(T) "also shows that
  Δ(x) = o(x^{1/4}) cannot hold as x → ∞."
Ivić's book (ch. 13) and Jutila 1984: not accessed (UNVERIFIED as primary).

---------------------------------------------------------------------------------------------------
## 4. Exponent pairs

**Definition — VERIFIED-SECONDARY** (both cite Graham–Kolesnik ch.3; GK itself not accessed):
- Saito–Suzuki–Takeda–Yoshida, arXiv:2312.15642 (Res. Number Theory 11 (2025) art. 50), p.14–15, Def. 16–18:
  model phase φ_{y,s}(x) = y x^{1−s}/(1−s) (s≠1), y log x (s=1); f ∈ F(N,P,y,s,ε) if [a,b] ⊆ [N,2N], f ∈ C^P and
  |f^{(p)} − φ^{(p)}_{y,s}| ⩽ ε|φ^{(p)}_{y,s}| (1⩽p⩽P). "Definition 18 (Exponent pair). A pair of real numbers (k,ℓ)
  with 0 ⩽ k ⩽ 1/2 ⩽ ℓ ⩽ 1 is said to be an exponent pair if for any positive real number s, there are … P = P(k,ℓ,s)
  and … ε = ε(k,ℓ,s) such that … Σ_{a<n⩽b} e(f(n)) ≪ L^k N^ℓ + L^{−1}, where L := yN^{−s}".
- Trudgian–Yang, "Toward optimal exponent pairs", arXiv:2306.05599, p.1–2, (1.1)–(1.2): f^{(p+1)} close to
  (d^p/dx^p)(yx^{−σ}); "(k,ℓ) is a (one-dimensional) exponent pair if for all σ > 0, there exists some P … and
  c … < 1/2 such that Σ_{n∈I} e(f(n)) ≪ (y/N^σ)^k N^ℓ (y ⩾ N^σ)", (k,ℓ) ∈ {0⩽k⩽1/2⩽ℓ⩽1, k+ℓ<1} ∪ {(1/2,1/2),(0,1)}.

**Exponent pair conjecture — VERIFIED-PRIMARY** (Trudgian–Yang p.2): "The exponent pair conjecture asserts that
(ε, 1/2 + ε) is an exponent pair for any ε > 0. … the conjecture implies at once the Lindelöf hypothesis and solves
(up to ε) the Dirichlet divisor problem."

**A and B processes — VERIFIED-PRIMARY** (Trudgian–Yang p.4, (1.10)–(1.11)): "A(k,ℓ) := (k/(2k+2), ℓ/(2k+2) + 1/2)"
[= (k/(2k+2), (k+ℓ+1)/(2k+2)) ✔]; "B(k,ℓ) := (ℓ − 1/2, k + 1/2)" ✔. Also convexity (Rankin) stated there.

**Σψ(x/m) lemma — VERIFIED-PRIMARY in Saito et al.** (proved there; GK attribution not checked), p.15:
> "Lemma 19. For the sum S_{δ,η}(N,N′) := Σ_{N<n⩽N′} ψ(x/(qn+δ) − η) with x ⩾ 1, q ∈ N, N ⩾ 1, N ⩽ N′ ⩽ 2N,
> 0 ⩽ δ ⩽ q+1 and η ∈ R and an exponent pair (k,ℓ), we have S_{δ,η}(N,N′) ≪ (x/q)^{k/(k+1)} N^{(ℓ−k)/(k+1)}
> + (x/q)^{−1} N², where the implicit constant depends only on k, ℓ."
With q=1, δ=η=0: Σ_{N<n⩽N′⩽2N} ψ(x/n) ≪ x^{k/(k+1)} N^{(ℓ−k)/(k+1)} + N²/x ✔.

**Vaaler — VERIFIED-SECONDARY** (Vaaler, BAMS 12 (1985) not accessible: AMS bot wall):
- Ma–Sun arXiv:2109.02924 p.3, "Lemma 2.1 … due to Vaaler ([4, Theorem A.6]) [=Graham–Kolesnik]. Let ψ(t) := {t} − 1/2.
  For x ⩾ 1 and H ⩾ 1, ψ(x) = −Σ_{1⩽|h|⩽H} Φ(h/(H+1)) e(hx)/(2πih) + R_H(x), where Φ(t) := πt(1−|t|)cos(πt) + |t|,
  and … |R_H(x)| ⩽ (1/(2H+2)) Σ_{|h|⩽H} (1 − |h|/(H+1)) e(hx)." (The page image does print "cos(πt)". I recall GK A.6
  having cot(πt) here, but I have not checked GK, so treat this function as a possible typo.)
- Saito et al. p.13, Lemma 14 (H > 0 real): ψ_H(x) = −Σ_{1⩽|h|<H} c_H(h)e(hx)/(2πih), |ψ − ψ_H| ⩽ (1/2H)Σ_{|h|<H}
  (1−|h|/H)e(hx), |c_H(h)| ⩽ 1; "This follows by the same construction as Theorem A.6 of [4]".

**Bourgain — VERIFIED-PRIMARY**: arXiv:1408.5794 "Decoupling, exponential sums and the Riemann zeta function", §5
(p.19): "Theorem 6. (ε + 13/84, ε + 55/84) is an exponent pair." Abstract: |ζ(1/2+it)| ≪ t^{13/84+ε}. Journal
(per Trudgian–Yang bibliography): J. Amer. Math. Soc. 30.1, pp. 205–224 (they print "(Mar. 2016)"; volume 30 is 2017).

---------------------------------------------------------------------------------------------------
## 5. Short sums of σ_{it}(n)n^{−it/2} / twisted divisor problem Δ(x; it)

**UNVERIFIED — nothing found.** arXiv API searches ("twisted divisor", divisor+imaginary+error term, Eisenstein +
short intervals) and web searches returned no pointwise short-interval result. Closest hit:
Mahatab–Mukhopadhyay, "Omega theorems for the twisted divisor function", arXiv:1807.10047 — concerns long sums
Σ*_{n⩽x}|τ(n,θ)|², τ(n,θ) := Σ_{d|n} d^{iθ}, proving an Ω(T^{3/8−c/(log T)^{1/8}}) result; not short intervals.

---------------------------------------------------------------------------------------------------
## 6. Lattice points near the hyperbola / divisors near √n

**Cilleruelo–Jiménez-Urroz, "The hyperbola xy = N", JTNB 12 (2000) 87–92 (numdam) — VERIFIED-PRIMARY**, p.88:
> "Question. Given α < 1/2, how many lattice points (x,y) of the hyperbola xy = N verify N^{1/2} ⩽ x ⩽ N^{1/2} + N^α?
> By a geometric argument we see that for two lattice points we already need α ⩾ 1/4. …
> Conjecture [apparently of I. Ruzsa]. For all ε > 0 there exists an integer k such that only for a finite number of
> values of N there can be more than k lattice points on xy = N verifying N^{1/2} ⩽ x ⩽ N^{1/2} + N^{1/2−ε}.
> We prove that the conjecture is true on average … d_α(n) = #{(a,b) | a,b ∈ I, ab = n}, for I = (N, N+N^α].
> Theorem 4. Let 0 < α < 1 fixed. Then Σ d_α²(n) = 2N^{2α} + O(N^{3α−1} log N) + O(N^α)."
**Cilleruelo–Jiménez-Urroz, "Divisors in a Dedekind domain", Acta Arith. 85 (1998) 229–233 — VERIFIED-PRIMARY**,
p.230: "Theorem 1.3. On the hyperbola xy = N there are at most k lattice points (x1,y1),…,(xk,yk) such that
N^γ ⩽ x1 < … < xk and xk − x1 ⩽ N^{E_k(γ)}", E_k(γ) = [kγ](2kγ − [kγ] − 1)/(k(k−1)) (Theorem 1.1, p.229).
(Both are per-N divisor-spacing results, not sums over x<km⩽x+y.)

**Huxley–Sargos, Acta Arith. 69 (1995) 359–366 — VERIFIED-PRIMARY**, p.359–360: Γ_δ = {a ⩽ x ⩽ a+N, |y−f(x)| ⩽ δ},
0 ⩽ δ ⩽ 1/4, hypothesis (1.2) |f^{(n)}(x)| ≍ λ; "Théorème 1. Sous la seule hypothèse (1.2), on a
(1.5) ν(Γ_δ) ≪ Nλ^{2/(n(n+1))} + Nδ^{2/(n(n−1))} + (δλ^{−1})^{1/n} + 1".
*(derived)* f(m)=x/m, m ∈ [M,2M], M ≍ √x, n=2: λ ≍ x^{−1/2}; the count #{(k,m): x<km⩽x+y} ⩽ ν(Γ_δ) with δ ≍ y/M;
for y = x^{1/4}, δ ≍ x^{−1/4}: bound ≪ x^{1/3} + x^{1/4} + x^{1/8}, i.e. weaker than the expected size ≍ y = x^{1/4}.
Trifonov arXiv:2609.17715 Theorem 2 (third-derivative refinement, needs δ ⩽ (CM)^{−1/2}) — *(derived)* same setting
gives ≪ M^{10/13+ε} = x^{5/13+ε}, also above x^{1/4}.

MRSTT (arXiv:2204.03754, abstract) use "an elementary decomposition of the neighbourhood of a hyperbola into
arithmetic progressions to control type I₂ sums" — averaged/nilsequence setting, H ⩾ X^{1/3+ε} for d_2.

**No source found giving pointwise asymptotics or power-saving bounds for #{(k,m): x<km⩽x+y, m∈(a√x,b√x]} with
y ≈ x^{1/4}** → UNVERIFIED (Chamizo, Filaseta–Trifonov 1996 not accessed).

---------------------------------------------------------------------------------------------------
## Summary

| # | Item | Status | Key verified content / source |
|---|------|--------|-------------------------------|
| 1 | NT main theorem, class M(A,B,ε) | VERIFIED-SECONDARY | Henriot 1102.1643 Thm 1: F(ab) ⩽ min(A^{Ω(a)},Ba^ε)F(b), (a,b)=1; Σ_{x<n⩽x+y}F(|Q(n)|) ≪ yΠ(1−ρ(p)/p)Σ F(n)ρ(n)/n, x^α<y⩽x, ε⩽αδ/(12g²) |
| 1 | NT for Q(n)=n | derived from above | ≪ (y/log x)Σ_{n⩽x}F(n)/n; Bordellès Thm 1 explicit analogue (PRIMARY) |
| 1 | Shiu Thm 1 | VERIFIED-SECONDARY | Bordellès Thm A, Henriot p.1 |
| 2a | Δ(mn) ⩽ τ(m)Δ(n) | VERIFIED-SECONDARY | dlB–T 2210.13897 (2·1) citing Hall–Tenenbaum *Divisors* Lemma 61.1 |
| 2b | KT mean value | VERIFIED-PRIMARY | KT Thm 1: ≪ x(Log₂x)^{11/4} |
| 2b | best upper bound | VERIFIED-PRIMARY | dlB–T 2309.03958 Thm 1.1: ≪ x(log₂x)^{5/2} |
| 2b | lower bound | VERIFIED-PRIMARY | FKT Thm 2: ≫ x(Log₂x)^{1+η−ε}, η=0.353327… |
| 2c | short-interval ΣΔ | VERIFIED-PRIMARY | dlB–T 2512.05652 Cor 1.2 (⇒ y(log₂x)^{5/2}, x^ε⩽y⩽x, derived); Bordellès Cor 2 |
| 3 | Jutila conj. (1.13), Ω (1.12) | VERIFIED-PRIMARY | Ivić JTNB 21 p.254; Ivić–Zhai Conj. 3 (open) |
| 3 | pointwise power saving at h=x^{1/4} | none found | Ivić–Zhai Thm 1 beats trivial only for U ⩾ x^{1/3} (their remark) |
| 3 | θ* = 0.314483… | VERIFIED-PRIMARY | Li–Yang Thm 1.2 |
| 3 | Hardy Ω(x^{1/4}) | VERIFIED-SECONDARY | Li–Yang (1.3); Ivić–Zhai (Cramér) |
| 4 | exponent pair def. | VERIFIED-SECONDARY | Saito et al. Def 18; Trudgian–Yang (1.2) (both cite GK ch.3) |
| 4 | exponent pair conjecture | VERIFIED-PRIMARY | Trudgian–Yang p.2 |
| 4 | Σψ(x/n) lemma | VERIFIED-PRIMARY (Saito et al. Lemma 19) | ≪ x^{k/(k+1)}N^{(ℓ−k)/(k+1)} + N²/x |
| 4 | Vaaler | VERIFIED-SECONDARY | Ma–Sun Lemma 2.1 & Saito et al. Lemma 14 (cite GK Thm A.6) |
| 4 | A, B processes | VERIFIED-PRIMARY | Trudgian–Yang (1.10), (1.11) |
| 4 | Bourgain (13/84+ε, 55/84+ε) | VERIFIED-PRIMARY | arXiv 1408.5794 Thm 6 |
| 5 | twisted divisor short intervals | UNVERIFIED | nothing found |
| 6 | hyperbola-neighbourhood count, y≈x^{1/4} | UNVERIFIED (no such result found) | related: C–JU JTNB 2000 Thm 4 & question (α ⩾ 1/4 for 2 points); C–JU 1998 Thm 1.3; Huxley–Sargos Thm 1 (derived bound x^{1/3} only) |
