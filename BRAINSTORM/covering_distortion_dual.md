# BRAINSTORM — covering-system duals of ES: distortion method, minimum-modulus analogues, determinacy (O150, angle c)

Labels as in DISCOVERIES.md. No new script; the relevant numerics are the campaign's (POINTWISE_SIZE §7, OMEGA13,
POINTWISE_TAIL).

## 1. Idea

"ES by identities" means a finite family of ET congruence classes `r_i (mod m_i)` (each solved by a polynomial
identity) covering every large prime. By Dirichlet, that is the same as covering `(ℤ/L)^×` with L = lcm m_i. Recent
covering-system technology proves *non-existence* of coverings and lower-bounds the uncovered density:
* Hough's minimum-modulus theorem;
* the distortion method of Balister–Bollobás–Morris–Sahasrabudhe–Tiba (BBMST).

Questions:
1. Does this technology give a cleaner or stronger form of the campaign's Theorems M/C?
2. Does it quantify the covering complexity needed for ES (minimum modulus, uncovered density)?
3. Does it give a new obstruction theorem?

## 2. Literature anchor

* **BBMST**, "On the Erdős covering problem: the density of the uncovered set", Invent. Math. 228 (2022) 377–414,
  arXiv:1811.03547 (abstract and §§1, 3 read for this memo).
  * Thm 1.1: let `μ(p^i) = 1 + (log p)^{3+ε}/p`, and take distinct moduli `d_i ≥ M` with `C = Σ μ(d_i)/d_i`. Then the
    uncovered density is `≥ e^{−4C}/2`.
  * General Thm 3.1 (verbatim shape): sieve prime by prime with measures `P_i`, distortion caps `δ_i ∈ [0,1/2]`, and
    `ν(d) = ∏_{p_j|d}(1−δ_j)^{−1}`. If `η := Σ_i min{M_i^{(1)}, M_i^{(2)}/(4δ_i(1−δ_i))} < 1`, where `M_i^{(k)}` is
    the k-th `P_{i−1}`-moment of the conditional removed mass `α_i(x)` at step i, then
    `P_0(R) ≥ (1−η) exp(−(2/(1−η)) Σ_d ν(d)/d)`.
  * They note that their proof avoids the Lovász Local Lemma used by Hough.
* **Hough**, "Solution of the minimum modulus problem for covering systems", Ann. of Math. 181 (2015). From memory:
  every covering system with distinct moduli has minimum modulus ≤ 10¹⁶; BBMST improve this to < 10⁶.
* **Campaign duals**:
  * the profinite avoider density δ*(T) of ET classes of modulus ≤ T:
    `𝓛³ ≪ log(1/δ*(T)) ≪ 𝓛³(log𝓛)^5` (CEILINGS_UNIFIED Prop 1.1, OMEGA13 Thm 3.4; LLL-based);
  * the witness modulus `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o. (OMEGA13 Thm 5.1);
  * tail exponent 3 (POINTWISE_TAIL);
  * the compactness theorem TYPEI2 Thm A ("finite covering ⟺ no sterile point").

## 3. Analysis

**(c1) No finite covering: already unconditional and classical.** An ET identity family on a class r (mod m)
produces a Type I/II solution for *every* n ≡ r (m), composite n included. Since `f_I(k²) = f_II(k²) = 0` for odd k
(ET Prop 1.6), no such class contains an odd square. Hence the classes of odd squares in `(ℤ/L)^×` are never
covered, and no finite covering of the large primes exists. This is the Mordell/Schinzel square-class obstruction
(ET p. 8).
* This is unconditional. BBMST-type density bounds add nothing here: an uncovered *subgroup of positive density*
  (the odd-square classes) already exists.
* Theorem C is conditional on H for a different reason. It handles *adaptive procedures that factor polynomial
  values f_i(p)*, i.e. conditions on factorisation shapes, which are not congruence conditions on p. The
  distortion method only handles congruence classes, so it cannot see these steps.

**(c2) Making Theorem C / redteam-2 Thm 2.2(iii) unconditional is a parity problem, not a covering problem.**
Replacing H by a lower-bound sieve ("each f_i(p) has only large prime factors, in prescribed residue classes")
is exactly the semi-linear sieve problem of POINTWISE_WINDOW. It is solved for one slice (Thm W1, ≫ x/(log x)^{3/2})
and blocked by parity at two slices (WINDOW2 Thm P1: parity input is *necessary*; WINDOW3 numerical gap).
Covering-system methods are parity-blind (they are statements about Haar measure), so they cannot help with this
step. (Assessment, with the PROVED necessity statement of WINDOW2 Thm P1.)

**(c3) Covering complexity is already quantified, and the dictionary is exact.**

| covering systems | ES (campaign) |
|---|---|
| uncovered density of a system with moduli ≤ T | δ*(T); `log 1/δ* ≍ 𝓛³` up to (log𝓛)^5 |
| minimum modulus (Hough) / largest needed modulus | W(p) (largest witness modulus needed at p); Ω-results above |
| distinct moduli, Σμ(d)/d = C | ET classes have multiplicity (≈ 𝓛³ total mass), not distinct |
| LLL (Hough) → distortion (BBMST) | β-LLL / square-class quarantine (OMEGA13 Lemma 1.1, 3.2) |
| Schinzel's divisibility conjecture | no analogue (no covering exists) |

"Any covering of the primes in [x, 2x] by ET classes needs a modulus ≥ exp(c(log x)^{1/4−o(1)})" is the
Hough-type statement. It holds because a positive proportion `exp(−C(log T)³(log log T)³)` of primes p ≤ x have
W(p) > T (POINTWISE_TAIL Thm 2.1, valid for log T ≤ c(log x/log log x)^{1/4}). It is PROVED modulo Gallagher and
Nair–Tenenbaum in that file; it is not new here.

**(c4) Could distortion sharpen the Haar exponent?** OMEGA13's `(log𝓛)^5` comes from the quarantine cost
`(1/η)𝓛³(log Y)^4` with η ≍ 1/log 𝓛 (β-LLL threshold), not from the masses.
* BBMST's Thm 3.1 replaces the LLL threshold by distortion caps δ_i ≤ 1/2, at cost factor ν(d) on masses.
* Raw ES system: at the primes 2, 3 (and the Mordell primes 5, 7) the conditional removed mass α_i(x) equals 1
  on most fibres, because Mordell's classes cover every non-hard class. So `Σ_i M_i^{(1)} ≥ 1` already, η < 1
  fails, and BBMST cannot be applied without a quarantine.
* After the square-class quarantine to primes ≤ Y, the remaining system is what OMEGA13 handles. Whether
  distortion with `δ_ℓ ≍ 1/log 𝓛` gives η < 1 with ν(d) = 1 + o(1) on average, and so `log(1/δ*) ≪ 𝓛³` exactly,
  depends on second moments M^{(2)} of ET-class masses over moving fibres. It was not decided here (**UNCLEAR**).
* Even if true, it improves a Haar-side constant only. It does not transfer to a single prime (B6).

**(c5) Game / determinacy view.** Consider the game where Adversary reveals p mod ℓ for ℓ = 2, 3, 5, … and
Prover wins at the first stage where the revealed residues lie in an ET class.
* The Prover's winning set is open in the compact space Ẑ^×, so the game is determined (Gale–Stewart; elementary
  here).
* Prover has a winning strategy ⟺ a finite covering exists (König).
* Adversary has one ⟺ a sterile profinite point exists.
* This is exactly TYPEI2 Thm A / POINTWISE_SIZE's compactness, and square classes show the Adversary wins (the
  point "1 everywhere" is sterile for Type I/II congruence data; Theorem C). The game view adds no information.
  Under H, the Adversary's win transfers to infinitely many primes, which is the B1 conclusion.

## 4. Barrier screen

* **B1.** (c1)–(c3) are B1 itself, viewed dually. Covering technology lower-bounds uncovered Haar mass, which is
  exactly what B1 says exists.
* **B2.** Not reached. Covering methods never see the divisor events of N_θ(p) at a fixed p.
* **B3/B6.** Covering densities are averages over p (Haar measure). At a single p they are silent.
* **B5.** The odd-square point is the canonical uncovered point; every covering bound is consistent with it.
* **T7.** Pure average leak.

## 5. Viability Assessment

**COLLAPSES** to B1/B6. The dual covering problem is *already exactly quantified* by the campaign's Haar/Ω line,
and the classical square-class obstruction proves non-coverability unconditionally. The only conditional
ingredient, H in Theorem C, concerns factorisation-shape steps. Replacing it is a parity-blocked sieve problem
(WINDOW2), which covering methods cannot address.

By-products:
* the dictionary table (c3) (Assessment);
* the observation (PROVED, trivial) that BBMST Thm 3.1 is inapplicable to the raw ES system because of the
  Mordell classes at 2, 3, 5, 7;
* an UNCLEAR program, (c4): use distortion inside the quarantined fibre to remove `(log𝓛)^5` and get
  `log(1/δ*(T)) ≍ 𝓛³` (Haar side only). Its value to ES is nil, but it would settle POINTWISE_HAAR Conj 3.1 up to
  constants.
