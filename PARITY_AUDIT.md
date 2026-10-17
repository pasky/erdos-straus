# PARITY_AUDIT — hatch H-B: parity-breaking literature audit and single-prime feasibility (task O255)

Status: in progress (O255). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md
(PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Literature excerpts in
`sources/lit2026f/`. "Cited" = external theorem whose statement we read in the source (or an archived
abstract/excerpt); proof not re-checked.

Builds on: PARITY_FIXED_P ((J)6), SYNTHESIS_SPARKS5 ((J)58), CAP_POINTWISE ((J)64), POINTWISE_WINDOW (item 15),
POINTWISE_SIZE §8, LITERATURE_2026 (checked to 2026-09-28).

## 0. The two single-prime events (exact formulations used throughout)

Fix a prime p ≡ 1 (mod 4) (the hard case; in practice p ≡ 1 (mod 24)). ψ(r) := (r/p).

**Event (a) — side-number event ((J)58 = SYNTHESIS_SPARKS5 §1; (J)9).** Words are w = (t, u, v) ∈ ℕ³ with
tuv − u − v = p; A := tu − 1, B := tv − 1, so N_u := p + u = A·v, N_v := p + v = B·u, N_t := tp + 1 = A·B, and the
ES sign is χ(w) = (−A/p) = ψ(A). ES-five(p) ⟺ ∃ w with χ(w) = −1 ((J)9 Thm 4.5; (J)58). Read on the u-side:

  E_a(p; U) :  ∃ u ≤ U, ∃ A | p + u with A ≡ −1 (mod u) and ψ(A) = −1.

(Any such A gives the word t = (A + 1)/u, v = (p + u)/A.) Two layers: the **class/size layer** "A | p + u,
A ≡ −1 (mod u)" (B2: a divisor of a shifted prime in a class modulo a modulus tied to the shift) and the **sign
layer** ψ(A) = −1 ((J)6: needs only upper bounds; no parity barrier).

*Lemma 0.1 (range; PROVED, elementary).* Every word has min(u, v) ≤ √(p+1) + 1. Hence E_a(p; √p + 2) ⟺ ES-five(p);
for U = p^θ with θ < 1/2 (in particular U = (log p)^C) E_a is a genuine restriction.
*Proof.* (tu − 1)(tv − 1) = tp + 1, so t·min(u,v) − 1 ≤ √(tp + 1), i.e. min(u,v) ≤ (√(tp+1) + 1)/t ≤ √(p+1) + 1
for t ≥ 1. Since χ(w) = ψ(A) = ψ(B) (Lemma S of (J)58), u and v play symmetric roles. ∎

*Swap form.* A ≡ −1 (mod u), A | p + u ⟺ (t, u, v) with p = tuv − u − v ⟺ "tp + 1 has a divisor ≡ −1 (mod t)"
((J)6 (★): R(p) = #{(j,f) : f | p + j, f ≡ −1 (mod 4j)} is the same count in Type II normalisation). At fixed p
the heuristic number of words is ≈ (log p)²/8 for (★) (EVIDENCE: R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰; (J)6 §3.3), i.e. **polylog many events in a family
of ≍ p parameter values**.

**Event (b) — window event ((J)64 = CAP_POINTWISE §1; POINTWISE_SIZE §8, Thm 8.1).** For a prime q ≡ 3 (mod 4),
q ≡ 4 − p (mod 8), (q/p) = −1, put K_q := (p + q)/4 (odd, gcd(K_q, pq) = 1). ES holds at window q (cap 0) iff
Rat_q(K_q) ∩ {−1, −p} ≠ ∅, Rat_q(K) = {u/v mod q : uv | K, gcd(u,v) = 1}. Its simplest (v = 1, target −1)
sub-event, the "B2 class" of the brief:

  E_b(p; Q) :  ∃ prime q ≤ Q as above, ∃ d | K_q with d ≡ −1 (mod q).

At such windows the *group* condition −1 ∈ ⟨primes of K_q⟩ mod q is **forced** by reciprocity ((J)64 Thm 1.1):
the sign layer is free; only the exponent budget (= class/size layer) is missing, and relaxing it gives the
PROVED cap e*(n) < q.

**Event (a⁴) — the sign-free normalisation used in the table (PROVED, classical).** Put the factor 4 into the class:

  E_a⁴(p; U) :  ∃ u ≤ U, ∃ f | p + u with f ≡ −1 (mod 4u).

If f = 4uC − 1 and B = (p + u)/f, then p = 4uBC − u − B, i.e. a Type II ES solution (Rosati/ET (A)3 form; this is
(J)6's (★): R(p) = #{(j, f) : f | p + j, f ≡ −1 (mod 4j)}). No sign layer is left: every hit is an ES solution.
The range lemma holds verbatim ((4uC − 1)(4BC − 1) = 4Cp + 1 gives min(u, B) ≤ √p/2 + 1), so E_a⁴(p; √p) is the full
(A)3 event and θ < 1/2 is a restriction. Swapping (f + 1 = 4uC): E_a⁴ ⟺ ∃ C, ∃ divisor of 4Cp + 1 that is ≡ −1
(mod 4C) — the N_t-side form. In two variables: **R(p) = #{(u, B) : uB | p + u + B, (p+u+B)/(uB) ≡ 0 (mod 4)}**.
This is what "divisors in moving residue classes" means here: the modulus 4u is tied to the shift u.

**What "known theorem reaches it" would mean.** A statement, for every large p (or a thin infinite set of p, or
under GRH), giving E_a(p; p^θ) with θ < 1/2, or E_b(p; p^θ) with θ < 1, or any positive lower bound for the
counts behind them. Note E_b with Q ≈ 3p is ES itself restricted to windows (POINTWISE_SIZE Thm 8.1).

## 1. The audit table (deliverable 1)

Conventions. "Single p" means: a statement for every large prime p (or a named thin infinite set of p, or under
GRH/RH) about the integers attached to that one p (p + u, 4Cp + 1, (p + q)/4). Excerpts: `sources/lit2026f/`
(file named in each row). (★) := R(p) of §0. Rows marked *(sec.)* were read only through a secondary source
(statement quoted in a paper we did read); all other statements were read in the primary source (abstract or
theorem statement; proofs not re-checked).

### 1A. Divisors of one integer in residue classes / intervals

| # | result | exact statement | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| A1 | Lenstra, *Divisors in residue classes*, Math. Comp. 42 (1984) 331–340, Main Thm and Prop (3.1) (`lenstra-1984-…`) | 0 ≤ r < s < n, s ≥ n^{1/3}, (r,s) = 1 ⇒ ≤ 11 divisors of n are ≡ r (mod s); for s ≥ n^α, α > 1/4: ≤ c(α) = O((α − 1/4)^{−2}) | every single n; **upper bound** | (a⁴): for u ≥ p^{1/4+ε}, each p + u has O_ε(1) divisors ≡ −1 (mod 4u). With Lemma 0.1 (u ≤ √p): the band u ∈ (p^{1/4+ε}, √p) carries O(1) candidates per u | wrong direction: no existence. Existence for one prescribed n is impossible in general (n prime) |
| A2 | Coppersmith–Howgrave-Graham–Nagaraj, Math. Comp. 77 (2008) 531–545 (abstract only; `coppersmith-…`) | same for α > 1/4, count O((α − 1/4)^{−3/2}), all such divisors found in poly time (lattice reduction) | single n; upper bound / algorithm | finds every hit with u ≥ p^{1/4+ε} in poly(log p) time per u, i.e. a *decision* procedure, not an existence theorem | same as A1 |
| A3 | Erdős–Hall, Math. Proc. Camb. Phil. Soc. 79 (1976) 281–287, THEOREM (OCR of renyi.hu; `erdos-hall-1976-…`); Erdős' earlier result quoted there | F(x,k) := #{n < x : divisors of n meet every reduced class mod k}. F(x,k) ~ x if k ≤ (log x)^{(1−ε) log 2}; at k = 2^{log log x + (c+o(1))√(log log x)}, F(x,k) ~ x·Φ̄(c) (Gaussian tail) — threshold "2^{ω(n)} ≈ k" | **almost all n ≤ x** | right *modulus range* for (a⁴): 4u ≤ (log p)^{0.69}. But it is a density statement over n; our family is the U = (log p)^{O(1)} specific integers p + 1, …, p + U | needs a version for *every* interval of polylog length (or for the AP {4Cp + 1}); best every-interval factorisation results need length ≥ x^{1/2} (rows C2–C3). Exponent gap 1/2 in the interval length |
| A4 | Ford, *The distribution of integers with a divisor in a given interval*, Ann. Math. 168 (2008) 367–433, Thm 1, Cor 2, Thms 6–7 (`ford-math0401223-…`) | order of H(x,y,z); H(x,y,2y) ≍ x/((log y)^δ(log log y)^{3/2}), δ = 0.086…; shifted primes p + λ: same order /log x (upper Thm 6; lower Thm 7 for y = x^a, z = x^b) | over n ≤ x / primes p ≤ x, **fixed** shift λ | nothing at one p; interval, not class | averaging over p is intrinsic; no class condition |
| A5 | Koukoulopoulos, *Divisors of shifted primes*, IMRN 2010, Thms 1.5–1.8 (`koukoulopoulos-2010-…`) | H(x,y,z;P_s) ≍ H(x,y,z)/log x (z ≥ y + y/(log y)^B), also in x-intervals of length x(log x)^{−B} | over p ≤ x, fixed s | nothing at one p | as A4 |

### 1B. Fixed modulus: modular hyperbola, Kloosterman sums, divisor functions in progressions to one modulus

| # | result | exact statement | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| B1 | Weil/Estermann via Shparlinski, *Modular hyperbolas*, Japan. J. Math. 7 (2012) 235–294, Thm 13, §3.1, §4.4, §6.3 (`shparlinski-1103.2879-…`) | #{xy ≡ a (m), x ∈ X, y ∈ Y_x} = φ(m)XY/m² + O(m^{1/2+o(1)}); making it nontrivial for XY < m^α, α < 3/2, "is out of reach" (tied to Selberg–Hooley 2/3); every a: xy ≡ a (p) solvable with \|x\|,\|y\| ≤ Cp^{3/4} only (survey's ref. [92], *sec.*); below p^{3/4} "apparently very hard"; almost all a: x, y ≤ m^{1/2}(log m)^{1+ε} (Garaev) | **pointwise in the modulus**, every residue a | (J)6 §3.4: (★) is an arithmetic subset of 𝓗 = {xy ≡ 1 (4p)} with polylog points; Weil counts boxes with error p^{1/2+ε} | **shortfall p^{1/2}** (the (J)6 number). Not a weakness of the bound: p^{1/2} is square-root cancellation, so no improved exponential-sum bound for single boxes can close it (§2) |
| B2 | Kowalski–Michel–Sawin, Ann. Math. 186 (2017) 413–500, Thms 1.1, 1.3, 1.7 (`kowalski-michel-sawin-1511.01636-…`) | q prime: Σ α_mβ_n Kl_k(cmn) ≪ q^ε‖α‖‖β‖(MN)^{1/2}(M^{−1/2} + (MN)^{−3/16}q^{11/64}) for q^{1/4} < MN < q^{5/4}, n in an interval; nontrivial for M = N > q^{11/24}, saving q^{−1/64} at q^{1/2}; Type I nontrivial for M = N > q^{3/7}; Thm 1.7: λ_f ⋆ 1 has exponent 1/2 + 1/102 for **every** prime modulus | pointwise in prime q; bilinear (Type II) below Pólya–Vinogradov | the only genuine *Type II* tool at one fixed prime modulus. (★) has unit coefficients ((J)6 Assessment 2.2): no Type II structure is requested | saves q^{1/64} (resp. 1/24) of a *trivial* bound; (★) needs error O(1) against trivial ≍ p (§2): saving p^{1−o(1)}. Gap exponent ≈ 1 − 1/64 relative to the trivial bound |
| B3 | Kowalski–Michel–Sawin, Ann. Sc. Norm. Pisa (5) 21 (2020), Thms 1.2–1.3 (`kowalski-michel-sawin-1802.09849-…`) | generalised Kloosterman: ‖α‖‖β‖(MN)^{1/2−η} for M, N ≥ q^δ, MN ≥ q^{3/4+δ} (Burgess-type barrier); Type I for MN² ≥ q^{1+δ} | pointwise in q | as B2 | as B2 (η unspecified, tiny) |
| B4 | Kerr–Shparlinski–Wu–Xi, arXiv:2204.05038 (v5 2023; journal JLMS (2) 108 (2023) per the agent, unverified), Thms 2.1, 2.4, 2.5, Cor 2.9, §3.3 (`kerr-shparlinski-wu-xi-…`) | Thm 2.4: Σ_{m∈I}Σ_{k≤K} α_mγ_k e_q(a m k̄) ≪ ‖α‖₂‖γ‖_∞ M^{1/2}K q^{o(1)}(M^{−1/4} + K^{−1/2}) — nontrivial for all M, K ≥ q^ε; §3.3: Selberg–Hooley's q ≤ X^{2/3} beaten **only on average over a** | any fixed q | the strongest short-range Kloosterman-fraction bound mod one q: the right *shape* for counting 𝓗 in thin boxes | saving min(M^{1/4}, K^{1/2}) of the trivial bound; detecting one residue (a = 1) in a box of area < p^{3/2} still needs all ≍ p/Y frequencies, and the main term XY/p is then smaller than the error (generic X × Y box, Y < p, a-sum via Thm 2.4: main/error ≍ (Y/p)^{3/4} < 1; our computation) |
| B5 | Bourgain–Garaev, Izv. Math. 78 (2014), arXiv:1211.4184, Thm 7, Cor 2, Thm 9 (`bourgain-garaev-…`) | Σα(x₁)α(x₂)e_p(a x̄₁x̄₂) nontrivial for \|I₁\| > p^{1/18}, \|I₂\| > p^{5/12+ε}; arbitrarily short initial intervals (Cor 2) | pointwise in p | multilinear Kloosterman fractions at very short ranges | power saving of a trivial bound; same gap as B4 |
| B6 | Selberg–Hooley (τ in APs, q ≤ x^{2/3−ε}, *sec.*: Shparlinski §3.1, KSWX §3.3); Fouvry–Kowalski–Michel, Mathematika 61 (2015), arXiv:1304.3199, Thm 1.1 (`fkm-1304.3199-…`) | Σ_{n≤x, n≡a (q)} τ(n) asymptotic for every q ≤ x^{2/3−ε}; d₃: every prime q ≤ x^{1/2+1/46} | **one modulus**, every a | N_t-side: Σ_{C≤X} τ(4Cp+1) = Σ_{n ≤ 4Xp+1, n ≡ 1 (4p)} τ(n) has an asymptotic iff 4p ≤ (4Xp)^{2/3−ε}, i.e. **X ≥ p^{1/2+ε}** | no class information; and the length threshold X ≈ p^{1/2} is exactly the range where E_a⁴ is already the whole (A)3 problem (Lemma 0.1): **the tool switches on where the restriction stops being a restriction** |
| B7 | Duke–Friedlander–Iwaniec, Invent. Math. 128 (1997) 23–43, Thm 1 (local `sources/dfi-1997-kloosterman-fractions.pdf`, p. 24); Bettin–Chandee, Adv. Math. 328 (2018), arXiv:1502.00769, Thm 1, Cors 1–2 (`bettin-chandee-…`) | Σ_{m∼M,n∼N,(m,n)=1} α_mβ_n e(a m̄/n) ≪ ‖α‖‖β‖(a+MN)^{3/8}(M+N)^{11/48+ε} (exponents as quoted by Bettin–Chandee; OCR of our PDF garbled); trilinear saving N^{1/20} | **moduli n vary** with the summation; a fixed (may equal p) | (★) in (u, C) variables: the condition (4uC − 1) \| p + u has m̄ = \overline{4C} ≡ u (mod 4uC − 1) — the Kloosterman fraction degenerates; in (m, C) variables the modulus is coupled (m ≡ −1 (mod 4C)), destroying the bilinear independence DFI need | structural mismatch + only a N^{1/48} power saving of a trivial bound |

### 1C. Pointwise statements about short intervals (the only "every x" factorisation results)

| # | result | exact statement | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| C1 | Huxley, Proc. LMS 87 (2003) (Δ(x) ≪ x^{131/416+ε}, *sec.*); Li–Yang, arXiv:2308.14859, Thm 1.2 (`li-yang-2308.14859-…`) | Δ(x) ≪ x^{θ*+ε}, θ* = 0.31448…; 5/16 "unbeatable barrier of existing methods" | every x | Σ_{u≤U} τ(p+u) = U log p + O(U) pointwise for **U ≥ p^{0.3145}**: the shortest family {p + u} on which *any* divisor statistic is known at one p | no residue class; with the class −1 (mod 4u) the main term drops from U log p to ≍ log p · log U while no error term below a power of U is known (§2) |
| C2 | Matomäki, IJNT 12 (2016) 323–340, abstract; IJNT 6 (2010) 1113–1116 (`matomaki-ijnt2016-…`) | every [x, x + √x(log x)^{7/3+δ}] contains an x^ε-smooth integer; every [x, x + C√x] an x^{1/(5√e)+ε}-smooth one | every x | if some p + u, u ≤ U, were (log p)^{O(1)}-smooth with ω ≳ log₂(4u), subset products could hit −1 (mod 4u) ((J)6 I3) | needs U = (log p)^{O(1)}; known U ≈ p^{1/2}(log p)^{7/3+δ}: **exponent gap 1/2** (and smoothness x^ε, not polylog) |
| C3 | Younis, arXiv:2409.05761, abstract (`younis-2409.05761-…`) | smooth-number density in [x, x + x^θ] for θ > 17/30, y ≥ exp((log x)^{2/3+ε}); **under RH**: θ > 1/2, y ≥ (log x)^K | every x; RH | as C2 | even RH stops at θ = 1/2: gap p^{1/2} survives RH |
