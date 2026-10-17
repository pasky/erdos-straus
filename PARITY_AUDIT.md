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
| B6 | Selberg–Hooley (τ in APs, q ≤ x^{2/3−ε}, *sec.*: Shparlinski §3.1, KSWX §3.3); Fouvry–Kowalski–Michel, Mathematika 61 (2015), arXiv:1304.3199, Thm 1.1 (`fkm-1304.3199-…`) | Σ_{n≤x, n≡a (q)} τ(n) asymptotic for every q ≤ x^{2/3−ε}; d₃: every prime q ≤ x^{1/2+1/46} | **one modulus**, every a | N_t-side: Σ_{C≤X} τ(4Cp+1) = Σ_{n ≤ 4Xp+1, n ≡ 1 (4p)} τ(n) has an asymptotic iff 4p ≤ (4Xp)^{2/3−ε}, i.e. **X ≥ p^{1/2+ε}** | no class information, and the shortest N_t-family {4Cp + 1 : C ≤ X} with a pointwise divisor statistic has X ≈ p^{1/2} (the hyperbola area p^{3/2} of B1 again); compare C1 on the u-side (U ≈ p^{0.3145}) |
| B7 | Duke–Friedlander–Iwaniec, Invent. Math. 128 (1997) 23–43, Thm 1 (local `sources/dfi-1997-kloosterman-fractions.pdf`, p. 24); Bettin–Chandee, Adv. Math. 328 (2018), arXiv:1502.00769, Thm 1, Cors 1–2 (`bettin-chandee-…`) | Σ_{m∼M,n∼N,(m,n)=1} α_mβ_n e(a m̄/n) ≪ ‖α‖‖β‖(a+MN)^{3/8}(M+N)^{11/48+ε} (exponents as quoted by Bettin–Chandee; OCR of our PDF garbled); trilinear saving N^{1/20} | **moduli n vary** with the summation; a fixed (may equal p) | (★) in (u, C) variables: the condition (4uC − 1) \| p + u has m̄ = \overline{4C} ≡ u (mod 4uC − 1) — the Kloosterman fraction degenerates; in (m, C) variables the modulus is coupled (m ≡ −1 (mod 4C)), destroying the bilinear independence DFI need | structural mismatch + only a N^{1/48} power saving of a trivial bound |

### 1C. Pointwise statements about short intervals (the only "every x" factorisation results)

| # | result | exact statement | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| C1 | Huxley, Proc. LMS 87 (2003) (Δ(x) ≪ x^{131/416+ε}, *sec.*); Li–Yang, arXiv:2308.14859, Thm 1.2 (`li-yang-2308.14859-…`) | Δ(x) ≪ x^{θ*+ε}, θ* = 0.31448…; 5/16 "unbeatable barrier of existing methods" | every x | Σ_{u≤U} τ(p+u) = U log p + O(U) pointwise for **U ≥ p^{0.3145}**: the shortest family {p + u} on which *any* divisor statistic is known at one p | no residue class; with the class −1 (mod 4u) the main term drops from U log p to ≍ log p · log U while no error term below a power of U is known (§2) |
| C2 | Matomäki, IJNT 12 (2016) 323–340, abstract; IJNT 6 (2010) 1113–1116 (`matomaki-ijnt2016-…`) | every [x, x + √x(log x)^{7/3+δ}] contains an x^ε-smooth integer; every [x, x + C√x] an x^{1/(5√e)+ε}-smooth one | every x | if some p + u, u ≤ U, were (log p)^{O(1)}-smooth with ω ≳ log₂(4u), subset products could hit −1 (mod 4u) ((J)6 I3) | needs U = (log p)^{O(1)}; known U ≈ p^{1/2}(log p)^{7/3+δ}: **exponent gap 1/2** (and smoothness x^ε, not polylog) |
| C3 | Younis, arXiv:2409.05761, abstract (`younis-2409.05761-…`) | smooth-number density in [x, x + x^θ] for θ > 17/30, y ≥ exp((log x)^{2/3+ε}); **under RH**: θ > 1/2, y ≥ (log x)^K | every x; RH | as C2 | even RH stops at θ = 1/2: gap p^{1/2} survives RH |

### 1D. Parity breaking and level of distribution beyond 1/2 (all averaged)

| # | result | exact statement | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| D1 | Friedlander–Iwaniec, *Asymptotic sieve for primes*, Ann. Math. 148 (1998) 1041–1065, Thm 1; *X² + Y⁴*, ibid. 945–1040; *Opera de Cribro* (AMS Coll. 57, 2010) ch. 16 (§16.4 parity), 17–18 (asymptotic sieve), 19–20 (bilinear forms for quadratic roots / Gaussian primes) — ToC only (`friedlander-iwaniec-math9811186-…`) | Type I (R) at level x^{2/3} < D < x plus Type II (B) with γ(n,C)μ(mn) twists in Δ^{−1}√D < N < δ^{−1}√x ⇒ Σ_{p≤x} a_p log p ~ H·A(x); Σ Λ(a² + b⁴) ~ (4/π)κ x^{3/4} | primes in a (thin) sequence **up to x** | at one p there is no sequence up to x. (b)/W2 is the only place an FI-type theorem enters, and it counts *how many p ≤ x* have failing windows (POINTWISE_WINDOW W2, FI09 shape) | object mismatch: FI detect primes (Möbius-twisted Type II); the single-p events are divisor events with unit coefficients ((J)6 Assessment 2.2). Averaging over p is intrinsic |
| D2 | Bombieri–Friedlander–Iwaniec, Acta Math. 156 (1986), Thm 10, *sec.* (quoted in Maynard I; `maynard-2006.06572-…`) | well-factorable λ, Q < x^{4/7−ε}: Σ_q λ_q(π(x;q,a) − π(x)/φ(q)) ≪ x(log x)^{−A}, fixed a | average over q, fixed a | — | averaged over moduli and over n ≤ x |
| D3 | Maynard, *Primes in APs to large moduli* I–III, Mem. AMS 306 (2025) 1542–1544, arXiv:2006.06572 Thm 1.1, 2006.07088 Thms 1.1–1.2, 2006.08250 Thm 1.1, Cor 1.4 (`maynard-2006.0*-…`) | levels x^{11/21}, x^{3/5} (triply well-factorable), x^{7/12} (λ⁺); III: sup over a for q₁ ≤ x^{1/10−3δ}, q₂ ≤ x^{4/10+4δ}; all but O(x^{1/2+δ}(log x)^{−A}) of the q ≤ x^{1/2+δ} with a divisor in [x^{2/5+δ}, x^{3/7}] have ≍ π(x)/φ(q) primes in every class | average / almost all q; counts primes ≤ x | — | as D2. Closest *shape* (III: every class, almost all q): still a statement about primes up to x for varying q, i.e. the dual of a single-p statement |
| D4 | Lichtman, arXiv:2211.09641 Thms 1.1, 1.4; arXiv:2309.08522 Thm 1.2, Cor 1.5/Thm 1.7 (`lichtman-*`) | P⁺(p − a) ≤ x^β for ≫ x/(log x)^C primes, β > 0.2843; level 17/32; level (5 − 4θ)/(8 − 6θ) = 66/107 uniformly for \|a\| < x^ε; Goldbach upper bound G(a) ≲ 3.39 Π_a(a) **at a single even a** | average over q; Thm 1.2 is single-a but an upper bound averaged over p < a | the single-a upper bound is the only "single integer" item here; it is an upper bound | upper bound / averaged over p < a; no lower bound at one integer |
| D5 | Pascadi, arXiv:2304.11696 Thm 1.1; arXiv:2505.00653 Thms 1.3, 1.5; arXiv:2404.04239 Thm 1 (`pascadi-*`) | smooth numbers to level 66/107 (absolute values, all q); primes 5/8 (triply well-factorable), 3/5 (linear sieve), smooth 5/8 ("limit of current methods"); P⁺(n² + 1) > n^{1.3} i.o. | average over q; n averaged | — | as D2 |
| D6 | Merikoski, JEMS 25 (2023), arXiv:1908.08816, Thms 1–2; Grimmelt–Merikoski, arXiv:2505.00493, Thms 1.1, 1.4–1.5 (`merikoski-*`, `grimmelt-*`) | P⁺(n² + 1) > n^{1.279} (1.312 under Selberg; G–M 1.312 unconditionally); Type II for Σ a_m b_n #{ℓ ∼ x : ℓ² + 1 ≡ 0 (mn)} via Deshouillers–Iwaniec | n averaged over [X, 2X] | the nearest analogue of "prime factors of the polynomial values p + 4a²d at one p" — but the polynomial variable, not a fixed prime, is averaged | single-p version would need the sum over n to collapse to one value |
| D7 | Drappeau, Compositio 151 (2015), arXiv:1307.7554 Thms 1–2; Fouvry–Radziwiłł, Ann. ENS 55 (2022), arXiv:1811.08672 Cors 1.1–1.2 (`drappeau-1307.7554-…`, `fouvry-radziwill-…`) | smooth numbers to level 3/5 (\|a\| ≤ x^δ); α ⋆ β with β Siegel–Walfisz on N ≥ exp((log x)^ε) to level 1/2 + 1/66 for \|a\| ≤ x/12; τ_k to 17/33 | average over q | — | as D2 |
| D8 | Maynard, *Primes with restricted digits*, Invent. 217 (2019), arXiv:1604.01041, Thm 1.1 (`maynard-1604.01041-…`) | #{p ∈ 𝒜} ≍ #𝒜/log X; Harman sieve, Type I level X^{50/77}, Type II via circle method | primes in a thin set up to X | — | as D1 |
| D9 | Assing–Blomer–Li, arXiv:2005.13915 (Adv. Math. 393 (2021) per the agent, unverified), Thm 1.1 with σ = −1 (`assing-blomer-li-…`) | Σ_{Y<n≤X} Λ(n)τ(f − n) asymptotic, error (log X)^{−A} (GRH: X^{1−δ}), **uniform in the single integer f** | one integer f, averaged over primes n < f | the closest "dual Titchmarsh at one integer" — the shape of event (b) summed over *all* windows q < f with no class condition | no class condition; and a class-restricted version has polylog main term, below any power-saving error (§2) |
| D10 | Drappeau, PLMS 2017, arXiv:1504.05549 (abstract; `drappeau-1504.05549-…`) | power saving in Σ_{p≤x} τ(p − 1) under GRH | over p ≤ x | — | averaged over p |

### 1E. Pointwise precedents for ternary representation problems, ES-specific literature, and the pointwise inputs we already use

| # | result | exact statement | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| E1 | Borwein–Choi, Exp. Math. 9 (2000) 153–158, Thms 1.1, 2.6, 3.1 (`borwein-choi-…`) | at most 19 integers are not xy + yz + zx (x,y,z ≥ 1); 18 known, a 19th > 10¹¹ is excluded under GRH (no Siegel zero suffices). For N = 2p₁⋯p_r: not representable ⟺ h(−4N) = 2^r (one form per genus), via (−1)^N r₃(N) = −6Σ_{xy=N}(−1)^{x+y} − 4Σ_{xy+yz+zx=N}(−1)^{x+y+z} and r₃ = 12h | **every single N** (one Siegel-type exception unconditionally) | the only pointwise theorem found for a ternary "product-type" representation: (x+z)(y+z) = N + z², i.e. *a divisor of N + z² in an interval*. Analogue of (a⁴) with "interval" in place of "class mod 4u" | mechanism = an exact class-number identity; for ES such identities are excluded: Type I/II counts vanish at odd squares (T1), and no fixed-level Eisenstein/σ-combination can do that ((J)7 Thm 9.1); class groups see the class mod 4u only through genus ((J)5 Prop 10.3; ray class needed, Remark 10.4). **Not SHARP**; qualitative gap |
| E2 | Elsholtz–Tao, J. Aust. Math. Soc. 94 (2013) 50–105, arXiv:1107.1010, Thm 1.1, Props 1.4, 1.6, 1.7, Thm 1.8 (`elsholtz-tao-1107.1010-…`) | Σ_{p≤N} f_II(p) ≍ N log² N; f(p) ≪ p^{3/5+O(1/log log p)} ("the limit of the divisor bound"); f = 0-type vanishing at odd squares (Prop 1.6); f(p) ≫ (log p)^{0.549} for a relative-density-1 set of p | average / almost all p | (★) has mean ≍ log² p over p, consistent with R(p) ≈ log² p/8 | averaged |
| E3 | Pollack, IJNT 10 (2014) Thm 1.4 (used in (J)66, `sources/pollack_ijnt2014_generalsplit6.pdf`); Burgess; Ankeny/Bach under GRH | a prime q in a prescribed Frobenius class of ℚ(i, √2, √p) with q ≪_ε p^{1/4+ε} for p ≡ 1 (8), p^{1/2+ε} for p ≡ 5 (8) (ineffective; (J)66 Cor 2.1), resp. q ≤ (16 log p + 70)² under GRH ((J)64) | **every single p** | (b): the window primes q themselves exist pointwise, small; at them the sign/group layer is forced ((J)64 Thm 1.1) | the class event d \| (p+q)/4, d ≡ −1 (mod q) is not touched: only the exponent cap e* < q is PROVED |
| E4 | Dyachenko, arXiv:2511.07465v1 (local PDF; re-read for this audit) | abstract: "central result (Theorem 10.21)": every prime P ≡ 1 (4) has 4/P = 1/A + 1/(bP) + 1/(cP). There is no Thm 10.21 in the text; the claim is Thm 9.21 | claimed every p | **no theorem**. Thm 9.21(III) finds a point of the lattice L = {(u,v) : ub′ + vc′ ≡ 0 (mod g)} in a box (Prop 9.25, elementary) — but L is built from (b′, c′, g), i.e. from a solution (b, c) with (4b−1)(4c−1) = 4Pδ + 1 that is presupposed; the step from a lattice point to a solution is the factorisation u² − v² = 4A/α (Lemmas D.33/D.16), i.e. the B2 divisor event itself, not proved | the author's own §11: "The general case … is certainly not proven … conditional in nature" (also `reviews/external-auro-zera-lean-wave20.md`) |
| E5 | Ventas, arXiv:2605.04551v3 (revised 2026-10-15; `ventas-2605.04551v3-…`) | Thm 2.4: sufficient condition (p + i has a divisor d ≡ 3 (4) with 4i \| p + d); finiteness of counterexamples only under Heuristic 3.2 (assumed) | heuristic | the sufficient condition is (a⁴)-type (a divisor of p + i in a class tied to i) | heuristic; no pointwise theorem; the author says the uniform control "remains a theoretical problem" |
| E6 | arXiv/erdosproblems #242 sweep 2026-09-20 → 2026-10-17 (`search-log-2026-10-17-erdosstraus-excerpt.txt`) | no new ES preprint; #242 page last edited 2026-05-07, newest forum post 2026-02-13 | — | nothing new | — |

Coverage gaps (stated honestly): Hall–Tenenbaum *Divisors* (Cambridge Tract 90) and Hall's Acta Arith. 29 (1976)
paper were not accessible; BFI 1986, DFI 1997's exact exponents, Heath-Brown's d₃ papers, Garaev's p^{3/4}
every-a result and Shkredov's bilinear bounds were read only through secondary sources (marked *sec.*); no
"Heath-Brown, divisors in residue classes" or Granville–Shiu paper on single-n divisors in classes was found (the
Shiu 1980 Brun–Titchmarsh for multiplicative functions, `sources/shiu-1980.pdf`, is an *upper* bound for sums over
n ≤ x in an AP, so it belongs with A4/A5).
