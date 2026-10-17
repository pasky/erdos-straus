# PARITY_AUDIT — hatch H-B: parity-breaking literature audit and single-prime feasibility (task O255)

Status: checkpoint 1 (O255; all four deliverables + numerics written; awaiting parent review). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md
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
for U = p^θ with θ < 1/2 (in particular U = (log p)^C) E_a is not known to be equivalent to ES-five (and the census of §5
shows small u suffice in practice).
*Proof.* (tu − 1)(tv − 1) = tp + 1, so t·min(u,v) − 1 ≤ √(tp + 1), i.e. min(u,v) ≤ (√(tp+1) + 1)/t ≤ √(p+1) + 1
for t ≥ 1. Since χ(w) = ψ(A) = ψ(B) (Lemma S of (J)58), u and v play symmetric roles. ∎

*Swap form.* A ≡ −1 (mod u), A | p + u ⟺ (t, u, v) with p = tuv − u − v ⟺ "tp + 1 has a divisor ≡ −1 (mod t)"
(its 4-normalised Type II analogue is (J)6's (★), below). At fixed p
the heuristic number of solutions is ≈ (log p)²/8 for (★) (EVIDENCE: R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰; (J)6 §3.3), i.e. **polylog many events in a family
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
(A)3 event (which itself fails at sparse primes, §5) and θ < 1/2 is a restriction. Swapping (f + 1 = 4uC): E_a⁴ ⟺ ∃ C, ∃ divisor of 4Cp + 1 that is ≡ −1
(mod 4C) — the N_t-side form. In two variables: **R(p) = #{(u, B) : uB | p + u + B, (p+u+B)/(uB) ≡ 0 (mod 4)}**.
This is what "divisors in moving residue classes" means here: the modulus 4u is tied to the shift u.

**What "known theorem reaches it" would mean.** A statement, for every large p (or a thin infinite set of p, or
under GRH), giving E_a(p; p^θ) with θ < 1/2, or E_b(p; p^θ) with θ < 1, or any positive lower bound for the
counts behind them. Note: the *full* window event (Rat_q(K_q) ∩ {−1, −p} ≠ ∅ over all q ≡ 3 (4) with p ∤ K_q) is equivalent to ES
(POINTWISE_SIZE Thm 8.1); E_b is a strict sub-event (QNR windows, v = 1, target −1) and fails at many primes (§5).

## 1. The audit table (deliverable 1)

Conventions. "Single p" means: a statement for every large prime p (or a named thin infinite set of p, or under
GRH/RH) about the integers attached to that one p (p + u, 4Cp + 1, (p + q)/4). Excerpts: `sources/lit2026f/`
(file named in each row). (★) := R(p) of §0. Rows marked *(sec.)* were read only through a secondary source
(statement quoted in a paper we did read); all other statements were read in the primary source (abstract or
theorem statement; proofs not re-checked).

### 1A. Divisors of one integer in residue classes / intervals

| # | result | statement (summary — full hypotheses in the excerpt) | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| A1 | Lenstra, *Divisors in residue classes*, Math. Comp. 42 (1984) 331–340, Main Thm and Prop (3.1) (`lenstra-1984-…`) | 0 ≤ r < s < n, s ≥ n^{1/3}, (r,s) = 1 ⇒ ≤ 11 divisors of n are ≡ r (mod s); for s ≥ n^α, α > 1/4: ≤ c(α) = O((α − 1/4)^{−2}) | every single n; **upper bound** | (a⁴): for u ≥ p^{1/4+ε}, each p + u has O_ε(1) divisors ≡ −1 (mod 4u). With Lemma 0.1 (u ≤ √p): the band u ∈ (p^{1/4+ε}, √p) carries O(1) candidates per u | wrong direction: no existence. Existence for one prescribed n is impossible in general (n prime) |
| A2 | Coppersmith–Howgrave-Graham–Nagaraj, Math. Comp. 77 (2008) 531–545 (abstract only; `coppersmith-…`) | same for α > 1/4, count O((α − 1/4)^{−3/2}), all such divisors found in poly time (lattice reduction) | single n; upper bound / algorithm | finds every hit with u ≥ p^{1/4+ε} in poly(log p) time per u, i.e. a *decision* procedure, not an existence theorem | same as A1 |
| A3 | Erdős–Hall, Math. Proc. Camb. Phil. Soc. 79 (1976) 281–287, THEOREM (OCR of renyi.hu; `erdos-hall-1976-…`); Erdős' earlier result quoted there | F(x,k) := #{n < x : divisors of n meet every reduced class mod k}. F(x,k) ~ x if k ≤ (log x)^{(1−ε) log 2}; at k = 2^{log log x + (c+o(1))√(log log x)}, F(x,k) ~ x·Φ̄(c) (Gaussian tail) — threshold "2^{ω(n)} ≈ k" | **almost all n ≤ x** | right *modulus range* for (a⁴): 4u ≤ (log p)^{0.69}. But it is a density statement over n; our family is the U = (log p)^{O(1)} specific integers p + 1, …, p + U | needs a version for *every* interval of polylog length (or for the AP {4Cp + 1}); best every-interval factorisation results need length ≥ x^{1/2} (rows C2–C3). Exponent gap 1/2 in the interval length |
| A4 | Ford, *The distribution of integers with a divisor in a given interval*, Ann. Math. 168 (2008) 367–433, Thm 1, Cor 2, Thms 6–7 (`ford-math0401223-…`) | order of H(x,y,z); H(x,y,2y) ≍ x/((log y)^δ(log log y)^{3/2}), δ = 0.086…; shifted primes p + λ: same order /log x (upper Thm 6; lower Thm 7 for y = x^a, z = x^b) | over n ≤ x / primes p ≤ x, **fixed** shift λ | nothing at one p; interval, not class | averaging over p is intrinsic; no class condition |
| A5 | Koukoulopoulos, *Divisors of shifted primes*, IMRN 2010, Thms 1.5–1.8 (`koukoulopoulos-2010-…`) | H(x,y,z;P_s) ≍ H(x,y,z)/log x (z ≥ y + y/(log y)^B), also in x-intervals of length x(log x)^{−B} | over p ≤ x, fixed s | nothing at one p | as A4 |

### 1B. Fixed modulus: modular hyperbola, Kloosterman sums, divisor functions in progressions to one modulus

| # | result | statement (summary — full hypotheses in the excerpt) | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| B1 | Weil/Estermann via Shparlinski, *Modular hyperbolas*, Japan. J. Math. 7 (2012) 235–294, Thm 13, §3.1, §4.4, §6.3 (`shparlinski-1103.2879-…`) | #{xy ≡ a (m), x ∈ X, y ∈ Y_x} = φ(m)XY/m² + O(m^{1/2+o(1)}); making it nontrivial for XY < m^α, α < 3/2, "is out of reach" (tied to Selberg–Hooley 2/3); every a: xy ≡ a (p) solvable with \|x\|,\|y\| ≤ Cp^{3/4} only (survey's ref. [92], *sec.*); below p^{3/4} "apparently very hard"; almost all a: x, y ≤ m^{1/2}(log m)^{1+ε} (Garaev) | **pointwise in the modulus**, every residue a | (J)6 §3.4: (★) is an arithmetic subset of 𝓗 = {xy ≡ 1 (4p)} with polylog points; Weil counts boxes with error p^{1/2+ε} | **shortfall p^{1/2}** (the (J)6 number). Not a weakness of the bound: p^{1/2} is square-root cancellation, so no improved exponential-sum bound for single boxes can close it (§2) |
| B2 | Kowalski–Michel–Sawin, Ann. Math. 186 (2017) 413–500, Thms 1.1, 1.3, 1.7 (`kowalski-michel-sawin-1511.01636-…`) | q prime: Σ α_mβ_n Kl_k(cmn) ≪ q^ε‖α‖‖β‖(MN)^{1/2}(M^{−1/2} + (MN)^{−3/16}q^{11/64}) for 1 ≤ M ≤ Nq^{1/4}, q^{1/4} < MN < q^{5/4}, n in an interval; nontrivial for M = N > q^{11/24}, saving q^{−1/64} at q^{1/2}; Type I nontrivial for M = N > q^{3/7}; Thm 1.7: λ_f ⋆ 1 has exponent 1/2 + 1/102 for **every** prime modulus | pointwise in prime q; bilinear (Type II) below Pólya–Vinogradov | a genuine *Type II* tool at one fixed prime modulus (see also B2′). (★) has unit coefficients ((J)6 Assessment 2.2): no Type II structure is requested | saves q^{1/64} (resp. 1/24) of a *trivial* bound; (★) needs error O(1) against trivial ≍ p (§2): saving p^{1−o(1)}. Gap exponent ≈ 1 − 1/64 relative to the trivial bound |
| B2′ | Blomer–Pascadi, arXiv:2607.24311 (Jul 2026, preprint), Thm 1.1, Rem. 1.2 (`blomer-pascadi-2607.24311-…`) | any modulus c, \|I\|,\|J\| ≤ N: Σ α_mβ_n S(am,n;c) ≪ ‖α‖‖β‖Nc^{1/2+o(1)}(c^{13/32}N^{−7/8} + c^{5/16}N^{−11/16} + c^{1/9}N^{−1/3}); saving c^{−1/32} at N = √c (doubles KMS); nontrivial for N ∈ (c^{13/28+ε}, c^{7/12−ε}); for prime c the lower range record stays KMS's p^{3/8} | pointwise in the modulus | the current record saving at the square-root range | as B2 with 1/32 in place of 1/64 |
| B3 | Kowalski–Michel–Sawin, Ann. Sc. Norm. Pisa (5) 21 (2020), Thms 1.2–1.3 (`kowalski-michel-sawin-1802.09849-…`) | generalised Kloosterman: ‖α‖‖β‖(MN)^{1/2−η} for M, N ≥ q^δ, MN ≥ q^{3/4+δ} (Burgess-type barrier); Type I for MN² ≥ q^{1+δ} | pointwise in q | as B2 | as B2 (η unspecified, tiny) |
| B4 | Kerr–Shparlinski–Wu–Xi, arXiv:2204.05038 (v5 2023; journal JLMS (2) 108 (2023) per the agent, unverified), Thms 2.1, 2.4, 2.5, Cor 2.9, §3.3 (`kerr-shparlinski-wu-xi-…`) | Thm 2.4: Σ_{m∈I}Σ_{k≤K} α_mγ_k e_q(a m k̄) ≪ ‖α‖₂‖γ‖_∞ M^{1/2}K q^{o(1)}(M^{−1/4} + K^{−1/2}) — nontrivial for all M, K ≥ q^ε; §3.3: Selberg–Hooley's q ≤ X^{2/3} beaten **only on average over a** | any fixed q | the strongest short-range Kloosterman-fraction bound mod one q: the right *shape* for counting 𝓗 in thin boxes | saving min(M^{1/4}, K^{1/2}) of the trivial bound; detecting one residue (a = 1) in a box of area < p^{3/2} still needs all ≍ p/Y frequencies, and the main term XY/p is then smaller than the error (generic X × Y box, Y < p, a-sum via Thm 2.4: main/error ≍ (Y/p)^{3/4} < 1; our computation) |
| B5 | Bourgain–Garaev, Izv. Math. 78 (2014), arXiv:1211.4184, Thm 7, Cor 2, Thm 9 (`bourgain-garaev-…`) | Σα(x₁)α(x₂)e_p(a x̄₁x̄₂) nontrivial for \|I₁\| > p^{1/18}, \|I₂\| > p^{5/12+ε}; arbitrarily short initial intervals (Cor 2) | pointwise in p | multilinear Kloosterman fractions at very short ranges | power saving of a trivial bound; same gap as B4 |
| B6 | Selberg–Hooley (τ in APs, q ≤ x^{2/3−ε}, *sec.*: Shparlinski §3.1, KSWX §3.3); Fouvry–Kowalski–Michel, Mathematika 61 (2015), arXiv:1304.3199, Thm 1.1 (`fkm-1304.3199-…`) | Σ_{n≤x, n≡a (q)} τ(n) asymptotic for every q ≤ x^{2/3−ε}; d₃: every prime q ≤ x^{1/2+1/46} | **one modulus**, every a | N_t-side: Σ_{C≤X} τ(4Cp+1) = Σ_{n ≤ 4Xp+1, n ≡ 1 (4p)} τ(n) (minus the term n = 1) has an asymptotic by the cited theorem when 4p ≤ (4Xp)^{2/3−ε}, i.e. **X ≥ p^{1/2+ε}** (a sufficient range, not an "iff") | no class information, and the shortest N_t-family {4Cp + 1 : C ≤ X} with a pointwise divisor statistic has X ≈ p^{1/2} (the hyperbola area p^{3/2} of B1 again); compare C1 on the u-side (U ≈ p^{0.3145}) |
| B7 | Duke–Friedlander–Iwaniec, Invent. Math. 128 (1997) 23–43, Thm 1 (local `sources/dfi-1997-kloosterman-fractions.pdf`, p. 24); Bettin–Chandee, Adv. Math. 328 (2018), arXiv:1502.00769, Thm 1, Cors 1–2 (`bettin-chandee-…`) | Σ_{m∼M,n∼N,(m,n)=1} α_mβ_n e(a m̄/n) ≪ ‖α‖‖β‖(a+MN)^{3/8}(M+N)^{11/48+ε} (exponents as quoted by Bettin–Chandee; OCR of our PDF garbled); trilinear saving N^{1/20} | **moduli n vary** with the summation; a fixed (may equal p) | (★) in (u, C) variables: the condition (4uC − 1) \| p + u has m̄ = \overline{4C} ≡ u (mod 4uC − 1) — the Kloosterman fraction degenerates; in (m, C) variables the modulus is coupled (m ≡ −1 (mod 4C)), destroying the bilinear independence DFI need | structural mismatch + only a N^{1/48} power saving of a trivial bound |

### 1C. Pointwise statements about short intervals (the only "every x" factorisation results)

| # | result | statement (summary — full hypotheses in the excerpt) | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| C1 | Huxley, Proc. LMS 87 (2003) (Δ(x) ≪ x^{131/416+ε}, *sec.*); Li–Yang, arXiv:2308.14859, Thm 1.2 (`li-yang-2308.14859-…`) | Δ(x) ≪ x^{θ*+ε}, θ* = 0.31448…; 5/16 "unbeatable barrier of existing methods" | every x | Σ_{u≤U} τ(p+u) = U log p + O(U) pointwise for **U ≥ p^{0.3145}**: the shortest family {p + u} on which *any* divisor statistic is known at one p | no residue class; with the class −1 (mod 4u) the main term drops from U log p to ≍ log p · log U while no error term below a power of U is known (§2) |
| C2 | Matomäki, IJNT 12 (2016) 323–340, abstract; IJNT 6 (2010) 1113–1116 (`matomaki-ijnt2016-…`) | every [x, x + √x(log x)^{7/3+δ}] contains an x^ε-smooth integer; every [x, x + C√x] an x^{1/(5√e)+ε}-smooth one | every x | if some p + u, u ≤ U, were (log p)^{O(1)}-smooth with ω ≳ log₂(4u), subset products could hit −1 (mod 4u) ((J)6 I3) | needs U = (log p)^{O(1)}; known U ≈ p^{1/2}(log p)^{7/3+δ}: **exponent gap 1/2** (and smoothness x^ε, not polylog) |
| C3 | Younis, arXiv:2409.05761, abstract (`younis-2409.05761-…`) | smooth-number density in [x, x + x^θ] for θ > 17/30, y ≥ exp((log x)^{2/3+ε}); **under RH**: θ > 1/2, y ≥ (log x)^K | every x; RH | as C2 | even RH stops at θ = 1/2: gap p^{1/2} survives RH |

### 1D. Parity breaking and level of distribution beyond 1/2 (all averaged)

| # | result | statement (summary — full hypotheses in the excerpt) | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| D1 | Friedlander–Iwaniec, *Asymptotic sieve for primes*, Ann. Math. 148 (1998) 1041–1065, Thm 1; *X² + Y⁴*, ibid. 945–1040; *Opera de Cribro* (AMS Coll. 57, 2010) ch. 16 (§16.4 parity), 17–18 (asymptotic sieve), 19–20 (bilinear forms for quadratic roots / Gaussian primes) — ToC only (`friedlander-iwaniec-math9811186-…`) | Type I (R) at level x^{2/3} < D < x plus Type II (B) with γ(n,C)μ(mn) twists in Δ^{−1}√D < N < δ^{−1}√x ⇒ Σ_{p≤x} a_p log p ~ H·A(x); Σ Λ(a² + b⁴) ~ (4/π)κ x^{3/4} | primes in a (thin) sequence **up to x** | at one p there is no sequence up to x. (b)/W2 is the only place an FI-type theorem enters, and it counts *how many p ≤ x* have failing windows (POINTWISE_WINDOW W2, FI09 shape) | object mismatch: FI detect primes (Möbius-twisted Type II); the single-p events are divisor events with unit coefficients ((J)6 Assessment 2.2). Averaging over p is intrinsic |
| D2 | Bombieri–Friedlander–Iwaniec, Acta Math. 156 (1986), Thm 10, *sec.* (quoted in Maynard I; `maynard-2006.06572-…`) | well-factorable λ, Q < x^{4/7−ε}: Σ_q λ_q(π(x;q,a) − π(x)/φ(q)) ≪ x(log x)^{−A}, fixed a | average over q, fixed a | — | averaged over moduli and over n ≤ x |
| D3 | Maynard, *Primes in APs to large moduli* I–III, Mem. AMS 306 (2025) 1542–1544, arXiv:2006.06572 Thm 1.1, 2006.07088 Thms 1.1–1.2, 2006.08250 Thm 1.1, Cor 1.4 (`maynard-2006.0*-…`) | levels x^{11/21}, x^{3/5} (triply well-factorable), x^{7/12} (λ⁺); III: sup over a for q₁ ≤ x^{1/10−3δ}, q₂ ≤ x^{4/10+4δ}; all but O(x^{1/2+δ}(log x)^{−A}) of the q ≤ x^{1/2+δ} with a divisor in [x^{2/5+δ}, x^{3/7}] have ≍ π(x)/φ(q) primes in every class | average / almost all q; counts primes ≤ x | — | as D2. Closest *shape* (III: every class, almost all q): still a statement about primes up to x for varying q, i.e. the dual of a single-p statement |
| D4 | Lichtman, arXiv:2211.09641 Thms 1.1, 1.4; arXiv:2309.08522 Thm 1.2, Cor 1.5/Thm 1.7 (`lichtman-*`) | P⁺(p − a) ≤ x^β for ≫ x/(log x)^C primes, β > 0.2843; level 17/32; level (5 − 4θ)/(8 − 6θ) = 66/107 uniformly for \|a\| < x^ε; Goldbach upper bound G(a) ≲ 3.39 Π_a(a) **at a single even a** | average over q; Thm 1.2 is single-a but an upper bound averaged over p < a | the single-a upper bound is the only "single integer" item here; it is an upper bound | upper bound / averaged over p < a; no lower bound at one integer |
| D5 | Pascadi, arXiv:2304.11696 Thm 1.1; arXiv:2505.00653 Thms 1.3, 1.5; arXiv:2404.04239 Thm 1 (`pascadi-*`) | smooth numbers to level 66/107 (absolute values, all q); primes 5/8 (triply well-factorable), 3/5 (linear sieve), smooth 5/8 ("limit of current methods"); P⁺(n² + 1) > n^{1.3} i.o. | average over q; n averaged | — | as D2 |
| D6 | Merikoski, JEMS 25 (2023), arXiv:1908.08816, Thms 1–2; Grimmelt–Merikoski, arXiv:2505.00493, Thms 1.1, 1.4–1.5 (`merikoski-*`, `grimmelt-*`) | P⁺(n² + 1) > n^{1.279} (1.312 under Selberg; G–M 1.312 unconditionally); Type II for Σ a_m b_n #{ℓ ∼ x : ℓ² + 1 ≡ 0 (mn)} via Deshouillers–Iwaniec | n averaged over [X, 2X] | the nearest analogue of "prime factors of the polynomial values p + 4a²d at one p" — but the polynomial variable, not a fixed prime, is averaged | single-p version would need the sum over n to collapse to one value |
| D7 | Drappeau, Compositio 151 (2015), arXiv:1307.7554 Thms 1–2; Fouvry–Radziwiłł, Ann. ENS 55 (2022), arXiv:1811.08672 Cors 1.1–1.2 (`drappeau-1307.7554-…`, `fouvry-radziwill-…`) | smooth numbers to level 3/5 (\|a\| ≤ x^δ); α ⋆ β with β Siegel–Walfisz on N ≥ exp((log x)^ε) to level 1/2 + 1/66 for \|a\| ≤ x/12; τ_k to 17/33 | average over q | — | as D2 |
| D8 | Maynard, *Primes with restricted digits*, Invent. 217 (2019), arXiv:1604.01041, Thm 1.1 (`maynard-1604.01041-…`) | #{p ∈ 𝒜} ≍ #𝒜/log X; Harman sieve, Type I level X^{50/77}, Type II via circle method | primes in a thin set up to X | — | as D1 |
| D9 | Assing–Blomer–Li, arXiv:2005.13915 (Adv. Math. 393 (2021) per the agent, unverified), Thm 1.1 (`assing-blomer-li-…`) | Σ_{Y<n≤X} Λ(n)τ(σn + f) = main + O((log X)^{−A}X) (GRH: X^{1−δ}), **uniform in the shift f** (σ = +1: X + f ≍ X; σ = −1: dual problem Σ_{n<f} Λ(n)τ(f − n), f > X) | one integer f, averaged over primes n | with σ = +1, f = p, X ≍ p: Σ_{q≤X} Λ(q)τ(p + q) — the **class-free** window sum of event (b), pointwise in p, but only over all windows q ≍ p | no class condition; the class-restricted version (d ≡ −1 (mod q)) has polylog main term, below any power-saving error (§2); length ≍ p, not p^θ |
| D10 | Drappeau, PLMS 2017, arXiv:1504.05549 (abstract; `drappeau-1504.05549-…`) | power saving in Σ_{p≤x} τ(p − 1) under GRH | over p ≤ x | — | averaged over p |

### 1E. Pointwise precedents for ternary representation problems, ES-specific literature, and the pointwise inputs we already use

| # | result | statement (summary — full hypotheses in the excerpt) | regime | gives at a single p | exact gap |
|---|---|---|---|---|---|
| E1 | Borwein–Choi, Exp. Math. 9 (2000) 153–158, Thms 1.1, 2.6, 3.1 (`borwein-choi-…`) | **unconditionally** at most 19 integers are not xy + yz + zx (x,y,z ≥ 1); 18 are known, a possible 19th is > 10¹¹ and is excluded under GRH (no Siegel zero suffices). For N = 2p₁⋯p_r: not representable ⟺ h(−4N) = 2^r (one form per genus), via (−1)^N r₃(N) = −6Σ_{xy=N}(−1)^{x+y} − 4Σ_{xy+yz+zx=N}(−1)^{x+y+z} and r₃ = 12h | **every single N** (unconditional up to one possible exception) | the only pointwise theorem found for a ternary "product-type" representation: (x+z)(y+z) = N + z², i.e. *a divisor of N + z² in an interval*. Analogue of (a⁴) with "interval" in place of "class mod 4u" | mechanism = an exact class-number identity. For ES only part of this is excluded by a theorem: Type I/II counts vanish at odd squares (T1), and no finite fixed-level combination of divisor sums σ_k(n;χ,ψ) can do that ((J)7 Thm 9.1); and class-group invariants see the class mod 4u only modulo squares ((J)5 Prop 10.3; ray class needed, Remark 10.4). Other identities (growing level, half-integral weight beyond these) are *not* excluded. **Not SHARP**; qualitative gap |
| E2 | Elsholtz–Tao, J. Aust. Math. Soc. 94 (2013) 50–105, arXiv:1107.1010, Thm 1.1, Props 1.4, 1.6, 1.7, Thm 1.8 (`elsholtz-tao-1107.1010-…`) | Σ_{p≤N} f_II(p) ≍ N log² N; f(p) ≪ p^{3/5+O(1/log log p)} ("the limit of the divisor bound"); f = 0-type vanishing at odd squares (Prop 1.6); f(p) ≫ (log p)^{0.549} for a relative-density-1 set of p | average / almost all p | full Type II has mean ≍ log³ p per prime (Σ_{p≤N} f_II(p)/π(N)); nothing pointwise. (★) is the h = 1 subfamily; its heuristic size (log p)²/8 is Lemma 2.1's M(p), not an ET theorem | averaged |
| E3 | Pollack, IJNT 10 (2014) Thm 1.4 (used in (J)66, `sources/pollack_ijnt2014_generalsplit6.pdf`); Burgess; Ankeny/Bach under GRH | a prime q in a prescribed Frobenius class of ℚ(i, √2, √p) with q ≪_ε p^{1/4+ε} for p ≡ 1 (8), p^{1/2+ε} for p ≡ 5 (8) (ineffective; (J)66 Cor 2.1), resp. q ≤ (16 log p + 70)² under GRH ((J)64) | **every single p** | (b): the window primes q themselves exist pointwise, small; at them the sign/group layer is forced ((J)64 Thm 1.1) | the class event d \| (p+q)/4, d ≡ −1 (mod q) is not touched: only the exponent cap e* < q is PROVED |
| E4 | Dyachenko, arXiv:2511.07465v1 (local PDF; re-read for this audit) | abstract: "central result (Theorem 10.21)": every prime P ≡ 1 (4) has 4/P = 1/A + 1/(bP) + 1/(cP). There is no Thm 10.21 in the text; the claim is Thm 9.21 | claimed every p | **no theorem**. Thm 9.21(III) finds a point of the lattice L = {(u,v) : ub′ + vc′ ≡ 0 (mod g)} in a box (Prop 9.25, elementary) — but L is built from (b′, c′, g), i.e. from a solution (b, c) with (4b−1)(4c−1) = 4Pδ + 1 that is presupposed; the step from a lattice point to a solution is the factorisation u² − v² = 4A/α (Lemmas D.33/D.16), i.e. the B2 divisor event itself, not proved | the author's own §11: "The general case … is certainly not proven … conditional in nature" (also `reviews/external-auro-zera-lean-wave20.md`) |
| E5 | Ventas, arXiv:2605.04551v3 (revised 2026-10-15; `ventas-2605.04551v3-…`) | Thm 2.4: sufficient condition (p + i has a divisor d ≡ 3 (4) with 4i \| p + d); finiteness of counterexamples only under Heuristic 3.2 (assumed) | heuristic | the sufficient condition is (a⁴)-type (a divisor of p + i in a class tied to i) | heuristic; no pointwise theorem; the author says the uniform control "remains a theoretical problem" |
| E6 | arXiv/erdosproblems #242 sweep 2026-09-20 → 2026-10-17 (`search-log-2026-10-17-erdosstraus-excerpt.txt`) | no ES preprint submitted after 2026-09-24 (the latest, Xu 2609.29250, is already in LITERATURE_2026); one revision (Ventas v3, E5); #242 page last edited 2026-05-07, newest forum post 2026-02-13 | — | nothing new | — |

Coverage gaps (stated honestly): Hall–Tenenbaum *Divisors* (Cambridge Tract 90) and Hall's Acta Arith. 29 (1976)
paper were not accessible; BFI 1986, DFI 1997's exact exponents, Heath-Brown's d₃ papers, Garaev's p^{3/4}
every-a result and Shkredov's bilinear bounds were read only through secondary sources (marked *sec.*); no
"Heath-Brown, divisors in residue classes" or Granville–Shiu paper on single-n divisors in classes was found (the
Shiu 1980 Brun–Titchmarsh for multiplicative functions, `sources/shiu-1980.pdf`, is an *upper* bound for sums over
n ≤ x in an AP, so it belongs with A4/A5).

## 2. The gap, quantitatively, against (J)6's p^{1/2} (deliverable 2)

**Lemma 2.1 (trial count; PROVED, elementary).** R(p) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = p} satisfies
R(p) = Σ_{(u,C)∈𝓡} 1[(4uC − 1) | p + u], 𝓡 := {(u,C) ∈ ℕ² : 4uC − 1 ≤ p + u}, and |𝓡| = (p/4) log p + O(p).
Writing 1[m | n] = m^{−1}Σ_{h mod m} e(hn/m):
  R(p) = M(p) + E(p),  M(p) := Σ_𝓡 1/(4uC − 1),  E(p) := Σ_𝓡 m^{−1}Σ_{0<h<m} e(h(p+u)/m)  (m = 4uC − 1),
and M(p) = (log p)²/8 + O(log p). For 1 ≤ U ≤ p the restriction u ≤ U keeps |𝓡_U| = (p/4) log U + O(p) and M_U(p) =
(log U)(log p)/4 − (log U)²/8 + O(log p).
*Proof.* (u, C) determines B = (p + u)/(4uC − 1), and B ≥ 1 ⟺ (u,C) ∈ 𝓡. For fixed u, C ranges up to
(p + u + 1)/(4u), so |𝓡| = Σ_{u ≤ p} (p/(4u) + O(1)) and M = Σ_u Σ_{C ≤ p/(4u)} 1/(4uC) + O(log p)
= Σ_u (1/(4u)) log(p/(4u)) + O(log p) = (log p)²/8 + O(log p). The U-version is the same sum cut at u ≤ U. ∎
(M(p) reproduces the (J)6 heuristic Σ_B M(B) ≈ (log p)²/8 and the observed R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹,
10¹⁰, where (log p)²/8 = 42.4, 53.7, 66.3.)
Check (`scripts/pa_lemma21_check.py`): the (u,C)-identity equals brute force for all primes < 400; at
p = 10⁴+7, 10⁵+3, 10⁶+3, 10⁷+19: M = 10.34, 16.17, 23.33, 31.81 vs (log p)²/8 = 10.61, 16.57, 23.86, 32.47 and
|𝓡| = 0.92–0.96 × (p/4) log p (R = 22, 20, 16, 42).

**Assessment 2.2 (what the p^{1/2} is, and what it is not).** Positivity R(p) ≥ 1 needs only E(p) > −M(p), with
M(p) ≍ (log p)². The known pointwise tools bound E(p) through complete exponential sums (Weil on 𝓗 = {xy ≡ 1
(4p)}, (J)6 §3.4) and give error p^{1/2+o(1)}: square-root cancellation in each complete sum, the (J)6 number. This
is the error scale of the *cited methods*, not a proved limit of every analytic approach. Under an independent-
incidence model the summands 1[m | p+u] − 1/m have total variance ≈ M(p), so nothing intrinsic forces fluctuations
of size p^{1/2}. (That R(p) ≍ (log p)² pointwise is itself only EVIDENCE.) Two structural remarks (Assessment):
restricting to u ≤ (log p)^A does **not** shrink the trial region (|𝓡_U| ≍ p log U, since C still runs to
p/(4u)), so (a⁴) at polylog U is no easier for complete-sum methods than (★) itself. Pre-factoring (summing over the
actual divisors of p + u) shrinks the trials to Σ_{u≤U} τ(p+u) ≈ U log p, but each u-term is then a character sum
over the divisors of one integer, Σ_{f | p+u} χ(f) with χ mod 4u, for which no analytic tool exists.

**The ledger (best known *pointwise-in-p* inputs, by category).**

| category | best known at a single p | needed | gap |
|---|---|---|---|
| class-aware counts on 𝓗 (Weil, Shparlinski Thm 13; B1) | box counts with error p^{1/2+ε} (asymptotics only for boxes of area ≫ p^{3/2+ε}) | E(p) > −M(p), M(p) ≍ (log p)², on a height-dependent arithmetic subset of 𝓗 | **factor ≍ p^{1/2}/(log p)²** between the cited error scale and the main term (the (J)6 number); no pointwise improvement of the area-p^{3/2} threshold is known |
| box benchmark, averaged over the residue a (Garaev via Shparlinski §3.2; KSWX §3.3) | almost all a: xy ≡ a (p) solvable with x, y ≤ p^{1/2}(log p)^{1+ε}, area p(log p)^{2+2ε}; every a: only \|x\|,\|y\| ≤ Cp^{3/4} (area p^{3/2}) | — (benchmark only: (★) is not a box-solvability question; at a = 1 the point (1,1) exists trivially; the obstruction is the height-dependent class condition) | shows that the p^{3/2} → p^{1+o(1)} box-area improvement is known only on average over residues (§3, "tied averaging") |
| divisor statistics of the u-side family {p + u} (Huxley; Li–Yang Thm 1.2; C1) | Σ_{u≤U} τ(p+u) ~ U log p for U ≥ p^{0.3145} | the class −1 (mod 4u) at U ≤ (log p)^A | no class information; exponent 0.3145 in the length, plus the class layer |
| divisor statistics of the t-side family {4Cp + 1} (Selberg–Hooley, FKM; B6) | asymptotic for C ≤ X once X ≥ p^{1/2+ε} (sufficient range of the cited theorem) | class −1 (mod 4C) | exponent 1/2 in the length, plus the class layer |
| structured (smooth) members of a short family (Matomäki 2016; Younis; C2–C3) | an x^ε-smooth integer in every [x, x + √x(log x)^{7/3+δ}]; under RH smooth-number asymptotics for length x^{1/2+ε}, y ≥ (log x)^K | a (log p)^{O(1)}-smooth p + u with u ≤ (log p)^{O(1)} (route (J)6 I3) | **p^{1/2}** in the length, unconditionally and under RH |
| Type II / bilinear at a fixed modulus (KMS 2017/2020, Blomer–Pascadi 2026, KSWX, Bourgain–Garaev; B2–B5) | power savings q^{1/64}, c^{1/32} (Blomer–Pascadi, at the √c range) … M^{1/4} of trivial bounds of bilinear forms | (★) has unit coefficients; error O(1) against trivial ≍ p | saving needed p^{1−o(1)}; Type II is not the missing input ((J)6 Assessment 2.2) |

**Answer to "which estimate gets closest, and by how much".** Pointwise in p, the closest class-aware estimate is
Weil's bound in its modular-hyperbola form (Shparlinski Thm 13). Its error scale p^{1/2+o(1)} exceeds the main term
(log p)² by a factor ≍ p^{1/2} (exponent 1/2), with no log-power refinement known. The literature calls going below
box area p^{3/2} "out of reach" for a single residue and ties it to the Selberg–Hooley 2/3 barrier (Shparlinski
§3.1). The only box results at area p^{1+o(1)} average over the residue class (Garaev; KSWX §3.3), and they are a
benchmark, not a reduction of (★). Class-blind statistics reach shorter families (u-side p^{0.3145}, Li–Yang) but
carry no class information. Under RH the short-interval length barrier for smooth numbers stays at p^{1/2}
(Younis). GRH helps only the sign/window layer (least non-residue, (J)64). These are statements about the cited
methods. No lower bound for the difficulty of (★) is proved here.

## 3. Feasibility verdict on hatch H-B (deliverable 3)

**Remark 3.1 (tied averaging; Assessment, the structural reason behind §2).** Every result in §1 that beats
Weil/Selberg–Hooley averages over a variable *independent* of the modulus: the residue a with the modulus fixed
(Garaev, KSWX §3.3), the moduli q ≤ x^θ with the integers n ≤ x free (D2–D7), or the sequence variable (D1, D6, D8,
A3–A5, E2). At a single p the only free variables are u (event (a⁴)), C (t-side) and q (event (b)), and each of them is
*also* the modulus of the class condition (4u, 4C, q). This is B2 seen from the literature side: no known
averaging theorem lets the modulus and the averaged variable move together with a fixed algebraic tie a = a(q).

**Lemma 3.2 (T1 for the events; PROVED, the χ-shadow of (J)6 Lemma 1.3).** Let n = m² be an odd square and u ≥ 1.
Then n + u has no divisor f ≡ −1 (mod 4u). Hence (a⁴) fails at every u for odd squares, and any proof of (a⁴) at a
prime p must use (ℓ/p) on prime factors ℓ of p + u.
*Proof.* f ≡ −1 (mod 4u) forces gcd(f, 4u) = 1 and χ_{−4u}(f) = χ_{−4u}(−1) = −1 (χ_{−4u} is an odd character mod 4u).
Every prime ℓ | m² + u with ℓ ∤ 2u has −u ≡ m² a non-zero square mod ℓ, so χ_{−4u}(ℓ) = (−u/ℓ) = +1, and so does every
divisor f coprime to 2u. ∎
At a prime p the same computation gives χ_{−4u}(ℓ) = (ℓ/p) (spin lemma), and since p + u ≡ u (mod p), (u/p) = −1
forces a QNR-mod-p prime factor: the χ-shadow is free whenever (u/p) = −1 (e.g. u = least QNR ≤ p^{1/(4√e)+ε},
Burgess–Vinogradov). Only the full class −1 (mod 4u) beyond its χ-shadow is left. That is (J)5 Prop 10.3 again
(genus versus ray class).

**Candidate combinations of known inputs (most plausible first), each with the missing piece named.**

1. *Erdős–Hall covering (A3) on the short family {p + u : u ≤ U}, U = (log p)^A, with the free χ-shadow (Lemma 3.2).*
   Erdős–Hall: an integer whose 2^{ω} exceeds k covers every class mod k, almost surely. **Missing:** a pointwise
   statement that among p + 1, …, p + U some p + u has ω(p + u) ≥ (1 + ε) log₂(4u) prime factors that are
   "random" mod 4u, i.e. Turán–Kubilius plus equidistribution of prime factors mod 4u for *every* interval of length
   (log p)^A. Known pointwise only for length ≥ p^{1/2}(log p)^{7/3+δ} (Matomäki; smoothness only, no
   equidistribution mod 4u), or for almost all intervals (Matomäki–Radziwiłł, Ann. Math. 183 (2016), not re-read
   here). Gap: p^{1/2} in length (unconditional and under RH, Younis), *plus* an equidistribution-mod-4u statement for
   the prime factors of one integer, which no theorem provides at any length.
2. *Windows (b): pointwise small window primes (E3: Pollack p^{1/4+ε} for p ≡ 1 (8); GRH (16 log p + 70)²) + the
   forced group layer ((J)64 Thm 1.1) + a zero-sum/Davenport forcing of the exponent budget.* Group-level success is
   forced; ES needs a sub-product of the prime factors of K_q, with exponents ≤ v_s(K_q), equal to −1 mod q.
   No combinatorial forcing of such a sub-product is possible below multiset length (q − 1)/2: L copies of a
   generator g give only the sub-products g, …, g^L, and −1 = g^{(q−1)/2} (PROVED, trivial; Davenport/Olson-type
   zero-sum bounds are of order q − 1). The multiset has length Ω(K_q) ≤ log₂ p. **Missing:** a window with
   q ≤ 2 log₂ p + 1. That fails infinitely often: every window prime is a quadratic non-residue mod p, the least
   non-residue is ≫ log p · log log log p infinitely often (Graham–Ringrose 1990; ≫ log p · log log p under GRH,
   Montgomery; both cited from memory, not re-read), and GRH gives only q ≤ (16 log p + 70)². One would also need a
   nearly maximally composite K_q. Both fail; this is (J)6 I3 with literature numbers.
3. *Fixed-modulus Kloosterman counting (B1, B4) applied to (★).* **Missing:** beyond-square-root cancellation for
   one residue on 𝓗 (area p^{1+o(1)} instead of p^{3/2}), which the literature calls out of reach (Shparlinski §3.1,
   §6.3), *and* arithmetic (not box) target sets (Lemma 2.1 shows restricting u does not shrink 𝓡). Even the
   class-free relaxation is the open every-residue modular-hyperbola conjecture.
4. *An almost-all-residues theorem (Garaev; KSWX §3.3) made pointwise by an averaging variable that is free at one
   p.* **Missing:** the free variable (Remark 3.1). The candidates u, C, q are all tied to the modulus.
5. *Exact-identity route à la Borwein–Choi (E1).* **Missing:** an identity expressing the Type II count through
   class numbers. At fixed level this is excluded ((J)7 Thm 9.1: counts vanishing at odd squares); class groups see
   only the χ-shadow ((J)5 Prop 10.3). The growing-level identity of (J)10 Prop 4.1 is the only T1-compatible
   candidate known, and its positivity is again the spin event.
6. *Parity-breaking sieves (D1–D8).* **Missing:** a sequence variable. These theorems count primes/prime factors
   along a sequence up to x; at one p they reduce to statements about how many p ≤ x are bad (POINTWISE_WINDOW
   W1/W2, FI09 shape), never to one p.

**Verdict (Assessment).** Hatch H-B is **not feasible with known inputs**. The audit confirms (J)6 from the
literature side, and sharpens it in three ways.
(i) Parity is not the binding constraint. Every parity-breaking theorem found is averaged over a sequence or over
moduli, and the single-p events are unit-coefficient divisor events.
(ii) The binding constraint is a square-root barrier at fixed modulus. The best class-aware pointwise estimate,
Weil in modular-hyperbola form, is short by exactly p^{1/2}, and the literature regards beating it for a single
residue as out of reach. Only residue-averaged results reach the log-power scale, and at a single p no averaging
variable is free of the modulus (Remark 3.1).
(iii) The restricted events (u ≤ (log p)^A, q ≤ p^θ) are no easier analytically than the full (★) (Lemma 2.1). They
are easier only combinatorially, through subset products, and that route needs factorisation statistics in every
short interval of polylog length, where the best pointwise results stop at length p^{1/2} (gap exponent 1/2, also
under RH).
H-B therefore collapses into H-A, as (J)6 said: a level-of-distribution statement for divisor incidences with the
modulus tied to the variable.

## 4. SHARP flags (deliverable 4)

**None.** No result found reaches a single-p statement of type (a) or (b): not for all large p, not for a thin
infinite set of p that are not already covered by congruences (B1), not under GRH/RH. Specifically:
* Every existence statement found is averaged (over n ≤ x, p ≤ x, moduli q ≤ x^θ, or residues a) — §1A, 1D, E2.
* Every pointwise-in-p statement is an upper bound (A1, A2, D4's G(a)), class-blind (C1, B6), or concerns
  intervals of length ≥ p^{1/2} (C2, C3), or stops at the sign/window layer (E3).
* The one pointwise ternary representation theorem (Borwein–Choi, E1) is GRH/Siegel-conditional and works through
  a class-number identity of a kind excluded for ES by T1 ((J)7 Thm 9.1). It is the closest *precedent*, not a
  reach.
* No ES proof claim in the window 2026-09-20 → 2026-10-17. Dyachenko's "Theorem 10.21" does not exist in the
  paper; its Thm 9.21 presupposes the divisor event (E4). ES is not solved.
Thin sets that *are* reached are B1 (congruence classes, polynomial identities) or campaign-internal algebraic
families ((J)62, (J)69, (J)74, (J)75, (J)80), none of which is known to contain infinitely many primes.

## 5. Numerics (EVIDENCE; `scripts/pa_events_census.py`, `scripts/pa_esfive_census.py`, logs in `logs/pa_*`)

All primes up to 10⁶; full divisor enumeration via a smallest-prime-factor sieve.

* **(a⁴) is not an all-p target.** E_a⁴(p; √p + 2) (= the full (A)3 event, R(p) ≥ 1) fails at 9 primes p ≡ 1 (4)
  ≤ 10⁶: 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321 (R(p) = 0 re-checked by the (u,C) count of
  Lemma 2.1 for the first six). Where it holds: least u has median 1, 99th percentile 5, maximum 131 (p = 427249).
  So any all-p theorem must aim at ES-five (event (a) with the sign layer) or full Type II, not at (★) alone.
* **(a) = ES-five on the u-side, primes p ≡ 1 (8) ≤ 10⁶ (19 552 primes):** no failure (consistent with (J)9's
  λ(p) ≤ 3). Least u has median 1, 99th percentile 5, 99.9th percentile 11, maximum 17 (p = 196561).
  **17 573 of 19 552 (89.9 %) are hit at u ≤ 2, where the class condition "A ≡ −1 (mod u)" is vacuous.** There the
  event is the pure spin event "p + 1 or p + 2 has a prime factor that is a non-residue mod p". Only 3 primes need
  u ≥ n_p (the least QNR, where Lemma 3.2 makes the χ-shadow free).
* **T1 control:** none of the 499 odd squares 9 ≤ m² ≤ 10⁶ has an (a⁴) hit or an (a) hit at any u ≤ m + 2
  (Lemma 3.2; (J)9).
* **(b) windows** (q prime, q ≡ 3 (4), q ≡ 4 − p (8), (q/p) = −1, q < 3p), primes p ≡ 1 (4) ≤ 10⁶ (39 175 primes).
  The B2 sub-event d | (p+q)/4, d ≡ −1 (mod q) fails at every such window for 8272 primes. Where it holds, least q
  has median 7, 99th percentile 19 759, maximum 141 971. The full target-−1 event (coprime u, v with uv | K_q and
  q | u + v) fails at every such window for 2458 primes; where it holds, least q has median 11 and 99th percentile
  4111. These failures are expected: the cap-theorem windows are only part of ES, and target −p (Type I) is
  excluded. So the restricted window event (b) is not an all-p target either.

**Remark 5.1 (where the single-p difficulty sits; Assessment from the census).** At a hard prime (p ≡ 1 (mod 840),
say) and each small u, the two layers are complementary. For u < n_p we have (u/p) = +1, so the sign layer is not
forced. For u ≤ 2 the class layer is vacuous, and the event is then a spin event at one integer. At u = n_p the sign
is forced but the class mod u is genuine. Neither half is a single-p theorem. The spin event at one integer is a
factorisation fact about that integer, just as the class event is. (J)6's "the sign layer is easy" holds for
*upper* bounds over many slices, not for one integer. Data: about 90 % of hard primes are decided by the spin event
at p + 1 or p + 2 alone. By the window analogue (POINTWISE_WINDOW W1: a_min(p) ≥ 7 for ≫ x/(log x)^{3/2} hard
primes, PROVED), one expects every fixed-U version of (a) to fail infinitely often. So a single-p theorem needs
U → ∞ with p, and that puts it back in the short-interval regime of §2, where the pointwise barrier is p^{1/2}.
