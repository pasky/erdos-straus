# Z53_NONCRTSMOOTH — fixed-modulus multiplicative representation vs the tied divisor event

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on 4/p. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment, one per claim. Internal results, internally reviewed only (not refereed).

Lane brief: `z52bbriefs/z53_depth.md` + `z53_lanes.md` §NONCRTSMOOTH. Scripts `scripts/z53_noncrtsmooth_*`, data
`data/z53/noncrtsmooth/` (0.8 MB). Must-reads used: FRONTIER §§2–4, 6, 7; PARITY_AUDIT Remark 3.1 and rows B1, D11;
B2_ACROSS_FIELDS (M1/M2 table); Z52D_HYPERBOLA §§0–2; DISCOVERIES (J)28, (J)34, (J)43 (ES^□, exponent cap, phase diagram).

## 0. Summary

Fix a prime p ≡ 1 (mod 4) (the ES-relevant case; where a statement needs only p ≥ 5 odd prime, it says so). A (★) triple
(u, B, C) gives x = 4Cu − 1, y = 4CB − 1 with xy = 4Cp + 1 and x ≡ y ≡ −1 (mod 4C). Fixed-modulus multiplicative
representation theorems produce **free** objects (primes, products of primes, small or smooth integers) in a prescribed
class modulo a **fixed** modulus. This lane locates where the tie "class modulus = 4C = (xy − 1)/p" breaks each such
theorem, proves what is provable in that shape, and measures the structured sub-lotteries numerically. The organising
object is the two-modulus event

  **E(q, κ) : ∃ x, y ≡ −1 (mod q) with xy = κqp + 1** (q ∈ 4ℕ the *class modulus*, κ ≥ 1 the *cofactor*),

i.e. "4Cp + 1 has a divisor ≡ −1 (mod 4C/κ)" with 4C = κq. (★) at level C is E(4C, 1); Elsholtz–Tao Type II is the union
of the E(q, κ) with **κ | q/4** (Lemma 3.4); E(q, s²) is an ES^□-type relaxation.

1. **Dictionary (PROVED, §3).** (a) Tying x + 1, y + 1 to 4C turns xy ≡ 1 (mod p) into the additive condition
   4C ≡ ū + B̄ (mod p), plus the window 0 < 4uBC − u − B < 2p (Lemma 3.1). (b) Compact form:
   **R(p) = #{x ∈ (1, 4p) : gcd(x, 4p) = 1, (x x̄ − 1)/p divides x + 1}**, x̄ ∈ [1, 4p) the inverse of x mod 4p
   (Prop 3.2); for p ≡ 1 (4) every winner is a quadratic non-residue mod p. (c) Divisibility closure (Lemma 3.3):
   "height | M" removes the tie exactly and gives a problem with two fixed moduli (4M, 4p).
2. **Theorem B (one prescribed class modulus; PROVED).** (a) For every q ∈ 4ℕ and prime p ∤ q(q − 1), E(q, κ) holds
   for some κ ≤ q − 2 (CRT with x = q − 1). (b) #{p ≤ X : E(q, κ) for some κ ≤ J} ≤ (JX/q)(log(JX) + 6) +
   4J^{3/2}(X/(q − 2))^{1/2}. Consequently (Cor B1), for a class modulus q = q(X) ∈ 4ℕ with q ≤ X^{1/2},
   prescribed independently of p, all but o(π(X)) primes p ≤ X have no solution with κ ≤ q/(log X)^{2+η}: **a statement
   about one such class modulus that holds for almost all p ≤ X cannot guarantee a cofactor below q/(log X)^{2+η},
   against q − 2 from the trivial construction** (the bound q ≤ X^{1/2} is essential: §4.2) — while (★) needs κ = 1 and Type II needs κ | q/4. EVIDENCE: the least cofactor is 0.13–0.22·q at
   p ≈ 10⁶ (q = 8 … 1000).
3. **Theorem A (free-object rungs; PROVED constructions).** A0 (fixed class modulus, T1-blind), A1 (class modulus
   q = 4C/2, T1-blind), A2 (T1-admissible square cofactor, from one prime ℓ ≡ 3 (4) with (ℓ/p) = −1: 4·1·ℓ·C′ − 1 − ℓ =
   s²p, s < ℓ; ES^□-type, known in substance: (J)28, (J)43). **Exact criterion A2 → Type II:** s² | C′ ⟺ s² | ℓ + 1 and
   4ℓ | p + w (ℓ + 1 = s²w); this implies a (★) triple (w, (p + w)/ℓ, s²/4) — so making the free rung Type II is again a
   single tied divisor event.
4. **Theorem C (closure; PROVED part).** P_M(p) is a union of τ(M) single-integer events (C | M); Σ_M |P_M(p)| =
   Σ_{(★)} τ(u). **CONDITIONAL on H:** for every fixed finite set of M, P_M(p) = ∅ for all M in it, for infinitely many
   p ≡ 1 (24) (B2 Thm 2.2(iii)). **EVIDENCE:** even with M optimised per p, |P_M(p)| ≈ 0.44–0.52·log p on average.
5. **Literature (§4.4; statements read in the source).** Ramaré–Walker Thm 1.1; Szabó Thms 1–3; Harman–Shparlinski
   Thm 1; Shparlinski, *Modular hyperbolas*, Thm 13; Bourgain–Garaev Thm 2; the EOS conjecture (open, also under GRH —
   Szabó p. 1). Each supplies either free objects at a fixed modulus (rung A0) or products whose height and factorisation
   it does not control, or is an almost-all statement (B6). None reaches A3/A4 (Assessment).
6. **Falsifiers (§5; CERTIFIED where stated: two independent engines on all 9732 primes p ≡ 1 (24) < 10⁶).**
   * "x or y prime" (single free prime, rung-A0 shape): empty at **85** primes p ≡ 1 (24) < 10⁶ where R(p) > 0 (largest
     997 201) — CERTIFIED. Also at the test primes 2521, 3361, 66529.
   * "x and y both prime" (EOS shape): empty at **4614 of 9723** such primes (47 %) — CERTIFIED; still 39 % at p ≈ 10⁷
     (EVIDENCE). Unordered mean ≈ 0.056·log p.
   * "x and y both p^{1/4}-smooth": empty at 98.6–98.8 % of primes in every sample (EVIDENCE). (One smooth coordinate is a
     constant ≈ 0.3 share of R and is not refuted.)

**Verdict: narrowed.** At one class modulus q = q(X) ∈ 4ℕ with q ≤ X^{1/2}, prescribed independently of p (p averaged up
to X), no statement valid for almost all p can beat the trivial construction by more than (log X)^{2+η} in the cofactor
(Thm B, PROVED; the size hypothesis q ≤ X^{1/2} is essential, §4.2); tie removal by closure is a finite menu per M (Thm C);
free-object constructions reach the T1-admissible square-cofactor rung A2, and the step A2 → Type II is again a single
tied divisor event (Thm A, PROVED). What survives is the aggregation over the class modulus q — a *joint* statement over
many q at one p — which is B2 itself (§7). All of this concerns Type II (and its (★) line); ES(p) ⟺ Type I(p) or
Type II(p), and nothing here bears on Type I or on ES proofs that avoid Type II.

## 1. Statements attacked

Notation. p ≥ 5 prime (p ≡ 1 (4) where stated). R(p) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = p} (FRONTIER §2.1). For a (★)
triple put x = 4Cu − 1, y = 4CB − 1. E(q, κ) as in §0; κ(p, q) := least κ with E(q, κ) (∞ if none).

* **(T) Target (FRONTIER §4 item 8 / hatch E1; non-CRT lower bound).** For all sufficiently large primes p ≡ 1 (24),
  R(p) ≥ 1 (or Type II(p) ≥ 1), derived from a fixed-modulus multiplicative representation theorem. (★) itself fails at
  14 primes ≤ 10¹⁰ (largest 8 813 281), so (T) is "for p > p₀". **Status: OPEN; route narrowed (§§3–4).**
* **(T1) Where does the tie break each theorem?** Answered in §4.4 via the dictionary (§3).
* **(T2) Closest provable statement.** Thm B(a) for one prescribed class modulus (with the matching barrier B(b));
  Thm A2 for the T1-admissible square-cofactor rung. Exact gap: κ | q/4 (Lemma 3.4, Thm A).
* **(T3) Construction routes.** (a) tie by construction (Lemma 3.1); (b) absorb the height into the modulus (Lemma 3.3,
  Thm C); (c) x, y as primes / smooth numbers (Thm A, §5.1).

## 2. Why this is not already closed

The closed list (brief + FRONTIER §6) contains one-step dualization at fixed conductor, Erdős–Turán with max|S_h|,
Cauchy–Schwarz in the function variable, low-conductor universality, the statement that Weil/Selberg–Hooley/bilinear
fixed-modulus savings "need p^{1−o(1)}" (PARITY_AUDIT §2), and H-B. PARITY_AUDIT row D11 records Ramaré–Walker/Szabó as
"pointwise parity breaking, but over free primes, so it does not reach the B2 event", in one line. None of these analyses
(i) multiplicative representation with free objects at a fixed modulus (the freedom M4 of B2_ACROSS_FIELDS), (ii) the
divisibility-closure reformulation (Lemma 3.3), which is tie-free with two fixed moduli 4M, 4p, or (iii) what a statement
about one prescribed class modulus can possibly give (Thm B). The partial-tie ladder (Thm A) overlaps with known material
((J)28 ES^□, (J)34 exponent cap, (J)43 phase diagram); it is re-derived here only in the (q, κ) language needed to place
the representation theorems, and is attributed.

## 3. Dictionary

**Lemma 3.1 (fixed-modulus-p additive form; PROVED; p ≥ 5 prime).** For (u, B, C) ∈ ℕ³ the following are equivalent:
(a) 4uBC − u − B = p;  (b) x = 4Cu − 1, y = 4CB − 1 satisfy xy = 4Cp + 1;
(c) p ∤ uB, **4C ≡ ū + B̄ (mod p)**, and Z := 4uBC − u − B < 2p.

*Proof.* (a)⇔(b): (4Cu − 1)(4CB − 1) = 4C(4uBC − u − B) + 1. (a)⇒(c): if p | u then B = 4uBC − u − p ≡ 0 (mod p), so
u, B ≥ p and Z ≥ u(4B − 1) − B ≥ B(4p − 1) − p ≥ 4p² − 2p > p, a contradiction; symmetrically p ∤ B. Reduce (a) mod p
and divide by uB. (c)⇒(a): Z ≡ uB(4C − ū − B̄) ≡ 0 (mod p), and Z ≥ (4u − 1)B − u ≥ 3u − 1 ≥ 2 > 0 (as C, B ≥ 1). A
positive multiple of p below 2p is p. ∎

*Reading (Assessment).* "Tie by construction" converts xy ≡ 1 into an additive condition on Kloosterman fractions — a
two-term modular Egyptian fraction whose target 4C lies in the progression 4ℕ and is tied to the size by
4uBC = p + u + B. Beyond the congruence, (★) is the window 0 < Z < 2p, less than two periods of the modulus. Widening it
to Z < 3p is trivial (PROVED: (u, B, C) = (1, 1, (p + 1)/2) gives Z = 2p for every odd p, and at every odd square).

**Proposition 3.2 (compact fixed-modulus-4p form; PROVED).** Let p ≥ 5 be prime. For x coprime to 4p let x̄ ∈ [1, 4p) be
its inverse mod 4p and h(x) := (x x̄ − 1)/p. Then
  R(p) = #{x ∈ (1, 4p) : gcd(x, 4p) = 1, h(x) | x + 1},
the map (u, B, C) ↦ x = 4Cu − 1 is a bijection onto this set, with x̄ = 4CB − 1 and h(x) = 4C, and every winner has
3 ≤ x, x̄ ≤ (4p + 1)/3. If moreover p ≡ 1 (mod 4), every winner satisfies **(x/p) = −1** (in general (x/p) = −(−1/p)).

*Proof.* Given a triple, u = (p + B)/(4BC − 1) ≤ (p + B)/(4B − 1) ≤ (p + 1)/3 (the middle term decreases in B), so
x = (p + u)/B ≤ p + u ≤ (4p + 1)/3 < 4p; likewise y < 4p. Since xy = 4Cp + 1 ≡ 1 (mod 4p) and y ∈ [1, 4p), y = x̄ and
h(x) = 4C | x + 1. Conversely let h(x) | x + 1 with x ∈ (1, 4p). Then x x̄ ≡ 1 (mod 4p) gives 4 | h(x), and h(x) ≥ 1 since
x x̄ > 1; put C = h(x)/4. From x x̄ = 4Cp + 1 ≡ 1 (mod 4C) and x ≡ −1 (mod 4C) we get x̄ ≡ −1 (mod 4C), so
((x + 1)/4C, (x̄ + 1)/4C, C) is a triple by Lemma 3.1(b). The two maps are inverse. Residue claim: −4Cp ≡ 1 (mod x), so the
Jacobi symbol (−4Cp/x) = 1. The Kronecker symbol χ_{−4C} = (−4C/·) is an odd character mod 4C and x ≡ −1 (mod 4C), so
(−4C/x) = −1 (the T1 computation of PARITY_AUDIT Lemma 3.2). Hence (p/x) = −1, and Jacobi reciprocity gives
(x/p) = (p/x)·(−1)^{((p−1)/2)((x−1)/2)}; with x ≡ 3 (4) this is −(−1/p), i.e. −1 for p ≡ 1 (4). ∎
(Example for the general sign: p = 11, triple (1, 4, 1), x = 3, (3/11) = +1.) Checked against brute-force R(p) for the
first 60 primes p ≡ 1 (4) and for 409, 2521, 3361 (`scripts/z53_noncrtsmooth_checks.py`, which also checks the size bound and
4 | h(x)).

**Lemma 3.3 (divisibility closure; PROVED).** For M ≥ 1 let
  P_M(p) := {x ≥ 1 : x ≡ −1 (mod 4M), ∃ y ≥ 1 with xy ≡ 1 (mod 4p), C := (xy − 1)/(4p) ∈ ℕ, C | M}.
The height C of x ∈ P_M(p) is unique; x gives the (★) triple ((x + 1)/4C, (y + 1)/4C, C); every triple arises with
M = C; and Σ_{M≥1} |P_M(p)| = Σ_{(u,B,C)} τ(u).

*Proof.* Uniqueness: two admissible y differ by a multiple 4pk, so the heights differ by xk; both lie in [1, M] and
x ≥ 4M − 1 > M, so k = 0. C | M gives 4C | x + 1; xy = 4Cp + 1 ≡ 1 (mod 4C) then gives y ≡ −1 (mod 4C); apply Lemma
3.1(b). A triple lies in P_M iff C | M and 4M | 4Cu, i.e. C | M | Cu: τ(u) values of M. ∎

**Lemma 3.4 (the (q, κ) picture; PROVED).** Let q ∈ 4ℕ, κ ≥ 1. E(q, κ) holds iff ∃ (u, B) ∈ ℕ²: quB − u − B = κp.
Elsholtz–Tao Type II (ff′ − 4c²dp = 1, f ≡ f′ ≡ −1 (mod 4cd), FRONTIER §1) is exactly ⋃_{q∈4ℕ} ⋃_{κ | q/4} E(q, κ),
and (★) is ⋃_q E(q, 1).

*Proof.* x = qu − 1, y = qB − 1 ≥ q − 1 ≥ 3 (as x, y ≡ −1 (mod q) are positive): (qu − 1)(qB − 1) = q(quB − u − B) + 1.
Type II with (c, d) is E(4cd, c), since ff′ = 1 + c·(4cd)·p; conversely E(q, κ) with κ | q/4 is Type II with
(c, d) = (κ, q/(4κ)). ∎

So (★) is the cofactor-1 line, Type II the region κ | q/4.

**Lemma 3.5 (T1-admissibility; PROVED).** Call (q, κ) *T1-admissible* if the conductor of the Kronecker character
χ_{−κq} divides q, and let χ* be the primitive character inducing χ_{−κq}. For every integer m, E_{m²}(q, κ) (E with p
replaced by m²) fails for every T1-admissible (q, κ).
*Proof.* Let x | κqm² + 1 with x ≡ −1 (mod q); x is coprime to κqm. Every prime ℓ | x is odd and has −κqm² ≡ 1 (mod ℓ),
so χ_{−κq}(ℓ) = 1; hence χ_{−κq}(x) = 1, and χ*(x) = χ_{−κq}(x) = 1 since gcd(x, κq) = 1. But χ* is a character mod q
(its conductor divides q), and it is odd, so χ*(x) = χ*(−1) = −1. ∎
Type II pairs (κ | q/4) are T1-admissible: κq = 4κ²d with d = q/(4κ), and χ_{−4κ²d}, χ_{−4d} have the same primitive
character, of conductor dividing 4d = q/κ | q. Square cofactors κ = s² are T1-admissible (cond χ_{−s²q} = cond χ_{−q} | q).
A cofactor with a prime ℓ ∤ q to an odd power is never admissible (ℓ | cond χ_{−κq}).

## 4. Theorems

### 4.1 Theorem A — free-object rungs (PROVED constructions)

A representation theorem supplies a free prime (or product) ℓ in a prescribed class modulo a fixed modulus. In the
divisor form, the direct use of a free ℓ is: fix its class, then solve for the height C modulo ℓ. The rungs below are
what this mechanism reaches (the claim that no other use exists is not made).

* **A0 (fixed class modulus; T1-blind; p ≥ 5 prime).** For any q ≥ 1 and prime ℓ ≡ −1 (mod q), ℓ ∤ 2p (Linnik–Xylouris:
  ℓ ≪ q⁵, as used in (J)64), let C₀ ∈ [1, ℓ − 1] with 4C₀p ≡ −1 (mod ℓ). Then ℓ | 4C₀p + 1 and ℓ ≡ −1 (mod q); the same
  holds at every odd n coprime to ℓ (T1-blind). ℓ is the x of a (★) triple **iff 4C₀ | ℓ + 1**: a triple with x = ℓ at
  level C needs ℓ | 4Cp + 1, i.e. C ≡ C₀ (mod ℓ), and 4C | ℓ + 1, so C < ℓ and C = C₀; conversely, if 4C₀ | ℓ + 1 then
  ((ℓ + 1)/4C₀, ((4C₀p + 1)/ℓ + 1)/4C₀, C₀) is a triple by Lemma 3.1(b). Taking q = 4C₀ is sufficient, not necessary (e.g. p = 5, q = 8, ℓ = 7: C₀ = 1, 4 | 8, triple (2, 1, 1)). The
  residue C₀ is determined by (ℓ, p), not by the class of ℓ mod q.
* **A1 (class modulus 4C/2; T1-blind; p ≡ 1 (4)).** d = 2p + 1, C = p + 1, q = 2(p + 1) ∈ 4ℕ: 4Cp + 1 = (2p + 1)², q | 4C,
  d ≡ −1 (mod q), cofactor κ = 2. Since q = 4C/2, q ≥ (4C)^θ for every fixed θ < 1 and p large. Same at n = m² (m odd).
  So the size of the class modulus is not the obstruction; its exact relation to the height is (κ = 2 ∤ q/4 = (p + 1)/2,
  which is odd).
* **A2 (T1-admissible, square cofactor; one QNR prime; p ≡ 1 (4)).** Let ℓ ≡ 3 (4) be prime with (ℓ/p) = −1. Then there
  is an even s ∈ (0, ℓ) with ps² ≡ −1 (mod ℓ), C′ := (ps² + 1 + ℓ)/(4ℓ) ∈ ℕ, and 4·1·ℓ·C′ − 1 − ℓ = s²p; i.e. E(4C′, s²)
  holds with x = 4C′ − 1, y = 4C′ℓ − 1, and (multiplying the (★)(s²p) identity of FRONTIER §2.1 by s²)
  **4/p = s²/(ℓC′) + 1/(pℓC′) + 1/(pC′).**
  *Proof.* (−p/ℓ) = (−1/ℓ)(p/ℓ) = (−1)(ℓ/p) = 1 (quadratic reciprocity, p ≡ 1 (4)), so −p̄ is a square mod ℓ; of the two
  roots in (0, ℓ), whose sum is ℓ (odd), exactly one is even. ℓ | ps² + 1, 4 | ps² (s even) and 4 | 1 + ℓ, so
  4ℓ | ps² + 1 + ℓ, and 4ℓC′ − 1 − ℓ = ps². ∎
  (4C′, s²) is T1-admissible (Lemma 3.5), and A2 is impossible at n = m² ((−m²/ℓ) = −1). Sizes: the height is H = C′s²
  and q = 4C′ = 4H/s², so q = (4H)^{1−θ′} with θ′ = log s²/log 4H; for ℓ < p, θ′ ≤ 2 log ℓ/log(p/ℓ). So the class modulus
  is (4H)^{1−o(1)} whenever ℓ = p^{o(1)} (Assessment: the least such ℓ is polylogarithmic under GRH by effective
  Chebotarev in ℚ(i, √p), and p^{O(1)} unconditionally by Linnik-type bounds — not re-derived here). Known in substance:
  (J)28 Prop 2.2 (ES^□ from ONE prime r ≡ 3 (4) with (n/r) = −1) and the (J)43 phase diagram. Checked for every prime
  p ≡ 1 (4) below 2·10⁴ (`scripts/z53_noncrtsmooth_checks.py`).
* **A3 (Type II): κ | q/4. A4 ((★)): κ = 1.**

**Exact criterion A2 → A3 (PROVED).** In the A2 family the solution is Type II iff s² | C′ (Lemma 3.4). Since
4ℓC′ = ps² + 1 + ℓ and 4 | s², s² | C′ forces s² | ℓ + 1; write ℓ + 1 = s²w. Then 4ℓC′ = s²(p + w), and as gcd(s, ℓ) = 1,
**s² | C′ ⟺ s² | ℓ + 1 and 4ℓ | p + w.** In that case (u, B, C) = (w, (p + w)/ℓ, s²/4) is a (★) triple
(ℓ = 4(s²/4)w − 1 divides p + w because s²w ≡ 1 and ps² ≡ −1 (mod ℓ) give p ≡ −w; then 4wB(s²/4) − w − B = Bℓ − w = p).
The converse fails without the condition 4ℓ | p + w (p = 5, ℓ = 3, s = 2: the triple (1, 2, 1) exists but C′ = 2). So
asking the free rung to be Type II is at least as hard as a (★) triple with C = s²/4 — a single tied divisor event of
p + w. The free rung delivers the right class modulus up to a square cofactor; removing the cofactor is B2 (Assessment).

### 4.2 Theorem B — one prescribed class modulus (PROVED)

Recall κ(p, q) = least κ ≥ 1 with E(q, κ) (∞ if none); E(q, κ) ⟺ qκp + 1 has a divisor ≡ −1 (mod q) ⟺
quB − u − B = κp is solvable.

**(a)** If q ∈ 4ℕ and the prime p ∤ q(q − 1), then κ(p, q) ≤ q − 2.

*Proof.* x = q − 1 ≡ −1 (mod q). By CRT (gcd(q, p) = 1) take y ∈ [1, qp] with y ≡ −1 (mod q), y ≡ (q − 1)⁻¹ (mod p).
Then xy ≡ 1 (mod q) and (mod p), so xy = 1 + κqp with 1 ≤ κ ≤ ((q − 1)qp − 1)/(qp) < q − 1. ∎

(For integers q ≥ 4 not divisible by 4 the definition of κ(p, q) via quB − u − B = κp is used verbatim; (b) holds for
all q ≥ 4 in this sense, and is applied below only to q ∈ 4ℕ.)

**(b)** For every integer q ≥ 4, J ≥ 1 and X ≥ 3,
  #{p ≤ X prime : κ(p, q) ≤ J} ≤ (JX/q)(log(JX) + 6) + 4J^{3/2}(X/(q − 2))^{1/2}.

*Proof.* If κ(p, q) = j ≤ J, pick (u, B) with V := quB − u − B = jp; V determines p, so distinct p give distinct
(j, u, B). Fix j and count (u, B) with u ≤ B, V ≤ jX and j | V (pairs with u > B: same count by symmetry, factor 2).
u ≤ B gives V ≥ qu² − 2u ≥ (q − 2)u², so u ≤ U_j := (jX/(q − 2))^{1/2} (if U_j < 1 there is nothing to count). For fixed
u, B ≤ (jX + u)/(qu − 1), and (qu − 1)B ≡ u (mod j); a common divisor g of qu − 1 and j must divide u for solvability and
also divides qu − 1, so g = 1 and B lies in at most one class mod j: #B ≤ (jX + u)/(j(qu − 1)) + 1. With
Σ_{u≤U} 1/(qu − 1) ≤ 1/(q − 1) + (1 + log U)/q ≤ (log U + 7/3)/q (q ≥ 4, U ≥ 1) and Σ_{u≤U} u/(j(qu − 1)) ≤ U/(3j), the
count for j is ≤ (X/q)(log U_j + 3) + 2U_j ≤ (X/q)(½ log(jX) + 3) + 2U_j. Double and sum over j ≤ J, using
Σ_{j≤J} √j ≤ J^{3/2}. ∎

**Corollary B1 (PROVED).** Let q = q(X) ∈ 4ℕ ∩ [4, X^{1/2}] be a class modulus prescribed independently of p, and
J ≤ q/(log X)^{2+η} with η > 0 fixed. Then all but o(π(X)) primes p ≤ X have κ(p, q) > J. (Divide (b) by
π(X) ≥ X/log X: the first term gives ≤ (log(JX) + 6)/(log X)^{1+η} → 0; the second ≤ 4q log X/(√X (log X)^{3}) → 0.)
Hence no statement "for every (or almost every) p ∈ (X/2, X], E(q, κ) for some κ ≤ K", with q prescribed in advance,
holds with K ≤ q/(log X)^{2+η}. Statements in which q may depend on p are the aggregated problem and are not covered.

*The size hypothesis q ≤ X^{1/2} cannot be dropped* (cross-model review): with P = ∏_{3≤r≤X, r prime} r and q = 2 + 2P
(∈ 4ℕ, prescribed independently of p, and p ∤ q(q − 1) for odd p ≤ X), x = y = q − 1 gives xy = 1 + κqp with
κ = (q − 2)/p, so every p ∈ (X/2, X] has κ(p, q) < 2q/X ≪ q/(log X)^{2+η}. Also, for a *fixed* q the threshold
q/(log X)^{2+η} eventually drops below 1, so B1 says nothing about κ = 1 there; finite-q menus are handled only
conditionally (Thm C(b), under H).

**Corollary B2 (PROVED).** With J = 1, q = 4C: the share of primes p ≤ X having a (★) triple at the prescribed level C is
≤ (log X)(log X + 6)/(4C) + o(1). Summing (b)'s per-j bound over κ | q/4: the share of p ≤ X having a Type II solution
with prescribed class modulus q is ≤ τ(q/4)(log X)(log(qX) + 6)/q + (4 log X/√((q − 2)X))·Σ_{j | q/4} √j; for
4 ≤ q ≤ X^{1/2} the last term is ≤ 4τ(q)·X^{−1/2}·log X → 0. (Both shares need q ≤ X^{1/2}, or the explicit
remainders, for the o(1)/error terms. These are averages over p; they are used only as
barriers for pointwise statements at a prescribed modulus, not as inputs.)

*Reading (Assessment).* Heuristically E(q, κ) has probability ≍ log p/q for κ ≤ q (one log fewer than Cor B2 proves), so
the Type II region at class modulus q has probability ≍ τ(q/4) log p/q (the admissible cofactors are sparse — τ(q/4) of
them — though not all small: κ = q/4 is admissible). Type II(p) is the union over q of these events (Lemma 3.4); ES(p)
is Type I(p) or Type II(p), so a joint-in-q Type II theorem would suffice for ES but is not equivalent to it. Methods that work at
one prescribed class modulus — Weil, Burgess with smooth weights, sieves, representation theorems — therefore have at
most a (log X)^{2+η} factor to gain over the trivial construction there (in the scope of Cor B1: q ∈ 4ℕ, q ≤ X^{1/2},
prescribed independently of p), and the Type II content lies in the aggregation over q. EVIDENCE (§5.2): the least cofactor scales linearly in q (mean κ(p, q)/q = 0.13–0.22 at 19 primes near 10⁶), and the
number of ordered witnesses with κ ≤ q is ≈ log p for every q.

### 4.3 Theorem C — the closure is a finite menu

**(a) (PROVED).** P_M(p) is the union over the τ(M) integers N_C = 4Cp + 1 (C | M) of the events "N_C has a divisor
≡ −1 (mod 4M)"; |P_M(p)| ≤ Σ_{C|M} τ(N_C); Σ_M |P_M(p)| = Σ_{(★)} τ(u) (Lemma 3.3).

**(b) (CONDITIONAL on Hypothesis H).** For every fixed finite set 𝓜, P_M(p) = ∅ for all M ∈ 𝓜, for infinitely many
p ≡ 1 (24): P_M(p) ≠ ∅ certifies ES(p) through the fixed finite slice set {Type II (c, d) = (1, C) : C | M, M ∈ 𝓜}, and
`reviews/redteam-automorphic-2.md` Thm 2.2(iii) (FRONTIER B2) says such a set fails for infinitely many p ≡ 1 (24). So M
must grow with p (hatch E1).

**(c) (EVIDENCE).** With M chosen per p to maximise |P_M(p)|, the mean of |P_M(p)|/log p is 0.435 (p ≡ 1 (24) < 10⁶) and
0.52 (near-squares; p ≈ 10⁷), against R(p) ≈ 0.14–0.16·(log p)²; the maximising M lies in {1, …, 6} for 83 % (10⁶) to 89 %
(10⁷) of primes. For the fixed M = 2, P_2(p) = ∅ at 17 % (10⁶) / 7 % (10⁷) of primes.

*Heuristic (Assessment).* E|P_M(p)| ≈ c·τ(M) log p/M: every single closure problem has expectation O(log p), and → 0
once M ≫ (log p)^{1+δ}. So "absorb the height into the modulus" is algebraically exact but converts (★) into a menu of
τ(M) single integers per M; for fixed M this is B1/B2(iii).

### 4.4 Where the tie breaks each representation theorem

Statements were read in the primary source (arXiv abstract or PDF) unless marked; the right-hand columns are Assessment.

| theorem (verified statement) | what it gives in ES coordinates | where the tie breaks |
|---|---|---|
| **EOS conjecture** (Erdős–Odlyzko–Sárközy 1987): every reduced class mod q contains p₁p₂, p_i ≤ q. Open, "not known even under GRH" (Szabó arXiv:2208.05762, p. 1; Shparlinski arXiv:1705.06087 abstract). Banks–Shparlinski arXiv:2610.19597 (abstract): for q = powers of a **fixed** prime, all but a proportion exp(−c(log q)^{1/3}(log log q)^{−1/3}) of classes, constants depending on that prime | at q = 4p, class 1: a point (x, x̄) of the inverse graph with x and x̄ both prime (both < 4p) | (★) is the sub-count with h(x) | x + 1 (Prop 3.2). The "both prime" (★) sub-lottery is empty at 47 % of primes p ≡ 1 (24) < 10⁶ (CERTIFIED, §5.1). That the class-1-mod-4p case of EOS is provable is not known to us |
| **Ramaré–Walker** Thm 1.1 (arXiv:1610.05804; JTNB 30 (2018)): q ≤ x^{1/16} ⇒ every invertible class mod q contains p₁p₂p₃ with all p_i ≤ x^{1/3} | (i) q = 4C, class −1: a free product x ≡ −1 (mod 4C) — rung A0; (ii) q = 4p, class 1: some N = p₁p₂p₃ ≡ 1 (mod 4p) | (i) x must also divide 4Cp + 1 — a congruence on p modulo the free x, not supplied; (ii) the theorem controls neither the height (N − 1)/4p nor whether some divisor of N lies in −1 (mod (N − 1)/p) |
| **Szabó** (arXiv:2208.05762) Thm 1: q cube-free ⇒ \|E₂(q)\| ≥ (3/8 + o(1))φ(q) (products of two primes ≤ q); Thm 2: q large prime ⇒ E₆(q) = (ℤ/q)^×; Thm 3: q ≥ q₀(ε) ⇒ E₃(q^{6/5+ε}) = (ℤ/q)^× | as RW; Thm 1 is a density over classes | as RW; Thm 1 need not contain the class −1 |
| **Harman–Shparlinski** Thm 1 (arXiv:1408.4515): q cube-free large ⇒ every reduced a ≡ n₁⋯n₁₄ (mod q), n_i ≤ q^{1/(4√e)+ε} | x ≡ −1 (mod 4C) congruent to a product of 14 small integers — rung A0 | x must divide 4Cp + 1; the theorem is silent on that. Data: (★) solutions with x **and** y p^{1/4}-smooth are absent at ≈ 98.7 % of primes; with one smooth coordinate they are a constant share (≈ 0.3) of R, so the data do not refute a one-coordinate use (§5.1) |
| **Weil on 𝓗** (Shparlinski, *Modular hyperbolas*, Thm 13, arXiv:1103.2879): #{xy ≡ a (m), x ∈ I, y ∈ J} = φ(m)\|I\|\|J\|/m² + O(m^{1/2+o(1)}) | E(q, κ) in a box: after (u − q̄)(B − q̄) ≡ q̄² (mod p), a solution in a balanced box needs UV ≥ p^{3/2+ε}, i.e. cofactor ≍ q p^{1/2+ε} | worse than the trivial κ ≤ q − 2 (Thm B(a)); by Cor B1 no statement at a q ≤ X^{1/2} prescribed independently of p beats q/(log X)^{2+η} for almost all p ≤ X |
| **Garaev–Karatsuba** (via Shparlinski §3.2 and KSWX §3.3; PARITY_AUDIT row B1, verified by R265): almost all a ⇒ xy ≡ a (p), x, y ≤ p^{1/2}(log p)^{1+ε} | right size scale (xy ≈ p) | averaged over the residue a (B6); at a = 1 trivial; the tie is not a residue condition |
| **Bourgain–Garaev** Thm 2 (arXiv:1211.4184): \|I\| < p^{3/46} ⇒ #{x̄ + ȳ + z̄ = λ, x, y, z ∈ I} < \|I\|^{2/3+o(1)} (λ ∉ I⁻¹ ∪ {0}) | the additive form 4C ≡ ū + B̄ (Lemma 3.1) is a two-term reciprocal sum | an upper bound; the ES target λ = 4C is tied to the size by 4uBC = p + u + B |
| **Klurman–Shparlinski–Teräväinen** (arXiv:2609.25393, abstract): a small set of small primes generates (ℤ/q)^× for all but O(Q(log Q)^{−A}) moduli q ≤ Q | almost all class moduli q = 4C | ES needs a rare event (Cor B2: share ≤ (log X)²/(4C) at a prescribed level) at some q, not a typical property of almost all q |
| "Heath-Brown/Shparlinski xy ≡ 1 (mod p), x, y ≤ p^{1/2+ε}" (named in the brief) | — | not located in a primary source (§8); at a = 1 the box problem is trivial ((1, 1)) |
| smooth numbers in APs to one large modulus (Soundararajan; Harper) — statement **not verified** | N = 4Hp + 1 smooth | smoothness alone does not place a divisor in −1 (mod 4H); the class condition is again the missing input |

**Common pattern (Assessment).** Each theorem either (i) chooses a free object in a class modulo a fixed modulus (rung
A0; the object then has to divide a forced integer, i.e. p must lie in a prescribed class modulo the free object), or
(ii) produces objects whose height and factorisation it does not control, or (iii) averages over residues or moduli
(B6). By Thm B, (i) used at one class modulus q ≤ X^{1/2} prescribed independently of p is capped, for almost all p ≤ X, at
the trivial construction up to (log X)^{2+η}; by
Lemma 3.5 and Thm A the T1-admissible free rung is A2.

### 4.5 Closest provable statement and exact gap

* **Closest tie-free statement (PROVED):** for every q ∈ 4ℕ and p ∤ q(q − 1), E(q, κ) for some κ ≤ q − 2 (Thm B(a)); for a
  class modulus q = q(X) ∈ 4ℕ, q ≤ X^{1/2}, prescribed independently of p, nothing valid for almost all p ≤ X guarantees
  κ ≤ q/(log X)^{2+η} (Thm B(b), Cor B1; false without q ≤ X^{1/2}, §4.2).
* **Closest T1-carrying statement (PROVED, known in substance):** A2 — E(4C′, s²) with class modulus (4H)^{1−θ′},
  θ′ = log s²/log 4H, from one prime ℓ ≡ 3 (4) with (ℓ/p) = −1 (Dirichlet).
* **Exact gap (PROVED reduction + Assessment):** Type II ⟺ some E(q, κ) with κ | q/4 (Lemma 3.4); within A2 this is
  "s² | ℓ + 1 and 4ℓ | p + w", which implies a (★) triple with C = s²/4. At a prescribed q ≤ X^{1/2} the Type II event occurs for at
  most a τ(q/4)(log X)(log(qX) + 6)/q + o(1) share of p ≤ X (Cor B2), heuristically ≍ τ(q/4) log p/q; any proof of
  Type II(p) via this picture must aggregate over q (Assessment; ES proofs via Type I are not addressed). In the
  compact form (Prop 3.2): one needs a point x of the inverse graph of (ℤ/4p)^× whose height h(x) = (x x̄ − 1)/p divides
  x + 1; the information carried by the class of x modulo 4p or modulo any fixed Q is, at the winners, the χ-shadow
  (x/p) = −1 plus the class itself, and Thm B shows that a class modulus q ≤ X^{1/2} prescribed independently of p cannot, for almost all p, force a
  small height.

## 5. Computations

All commands with `ulimit -v 6000000` and `timeout ≤ 1800`. Data in `data/z53/noncrtsmooth/`; regenerate the summary with
`scripts/z53_noncrtsmooth_summary.py` (`summary.txt`).

### 5.1 Structured sub-lotteries of (★)

Engine 1 (`scripts/z53_noncrtsmooth_lottery.cpp`): all ordered (★) triples through u ≤ n/3 and the divisors
x ≡ −1 (mod 4u) of n + u (segmented factorisation of [n + 1, 4n/3]); y's factorisation is read off n + B. Columns: R; Rp
(x or y prime); Rbp (x and y prime); Rs50/Rs33/Rs25 (x and y both n^θ-smooth); Re33/Re25 (x or y n^θ-smooth); least C;
|P_M| for M = 1, 2, 6, 12, 60 and for the M maximising it. Engine 2 (`scripts/z53_noncrtsmooth_verify2.py`, independent
code): PARI divisors of 4Cp + 1 for all C ≤ (p + 2)/4, computing R, Rp, Rbp. **Engine 2 reproduces R, Rp and Rbp exactly
for all 9732 primes p ≡ 1 (24) < 10⁶, all 15 test primes, 538 of the 600 near-squares and 20 of the 400 primes near 10⁷**
(0 mismatches; `v2/*.csv`). Brute force in Python agrees for n ∈ {73, 97, 193, 409, 577, 1009, 3361}. Controls: the 10
(★)-failures of the test list give R = 0; odd squares give R = 0 identically (T1), so every sub-lottery vanishes there.

| sample | # | mean R/L² | either-prime /L | both-prime /L | R > 0, no prime x/y | R > 0, no both-prime pair | both p^{1/4}-smooth absent | one p^{1/4}-smooth absent |
|---|---|---|---|---|---|---|---|---|
| all p ≡ 1 (24) < 10⁶ | 9732 | 0.140 | 0.417 | 0.056 | **85** (56 > 10⁵, 32 > 5·10⁵; max 997 201) | **4614** (47 %) | 98.8 % | 13.7 % |
| near-squares m² + k (k ≤ 100), 1.0–2.9·10⁶ | 600 | 0.158 | 0.463 | 0.049 | 0 | 292 (49 %) | 98.7 % | 2.5 % |
| 400 consecutive p ≡ 1 (4) > 10⁷ | 400 | 0.163 | 0.514 | 0.056 | 0 | 156 (39 %) | 98.8 % | 1.0 % |
| test primes (FRONTIER §4 item 14) | 15 | — | — | — | 3 of 5 with R > 0 (2521, 3361, 66529) | 5 of 5 | 100 % | 60 % |

(L = log n; "/L" columns are unordered pair counts divided by L; the last four columns count primes with R > 0. The one
near-square with R = 0 is 1 134 241, a known (★) failure.)

* **CERTIFIED (two engines, complete range).** Among the 9732 primes p ≡ 1 (24) below 10⁶: exactly 9 have R(p) = 0 (the
  census values); exactly 85 have R(p) > 0 but no (★) triple with x or y prime (largest 997 201); exactly 4614 have
  R(p) > 0 but no triple with x and y both prime.
* **EVIDENCE.** Above 5·10⁵ the unordered either-prime count has mean 5.8 and variance/mean 1.05 (Poisson-like); the
  both-prime count has mean 0.74 and variance/mean 0.92. The either-prime mean grows like ≈ 0.42–0.51·log p over the
  samples; the both-prime mean like ≈ 0.05·log p.
* **CONJECTURE (conditional on (i) a Poisson zero law with mean c·log p, c ≈ 0.42–0.51, for the either-prime count, and
  (ii) unrestricted (★) failures being o(X^{1−c}) below X — e.g. R(p) > 0 eventually, or a joint zero law for the pair
  (R, Rp)).** Then the either-prime sub-lottery fails at ≍ X^{1−c+o(1)} primes below X with R(p) > 0 — infinitely many.
  The marginal law (i) alone does not place its zeros at primes with R(p) > 0. For the both-prime
  (EOS-shape) sub-lottery (c ≈ 0.05) the failures would have density p^{−0.05}, i.e. it fails at most primes in any
  practical range. Either way, no theorem that delivers a *prime* divisor (rung A0 with a prime, or EOS shape) can carry
  (★) at every large p unless these hypotheses fail.
* **EVIDENCE.** "x and y products of primes ≤ p^{1/4}" is empty at ≈ 98.7 % of primes in every sample (share of R:
  0.33–0.45 %); "≤ p^{1/3}": empty at 69–85 %. One coordinate p^{1/4}-smooth is a constant ≈ 0.26–0.33 share of R and empty
  at 1–14 %: not refuted.

### 5.2 One prescribed class modulus (`scripts/z53_noncrtsmooth_fixedq.py`, `fixedq.csv`)

For 19 primes p ≡ 1 (4) near 10⁶ (`nextprime(10⁶ + 1000k)`), the nine (★)-failures ≤ 10⁶ and 8 813 281, and
q ∈ {8, 12, 16, 24, 40, 60, 100, 200, 400, 1000}: κ(p, q) and N_q = # ordered witnesses (κ, x) with κ ≤ q,
x | qκp + 1, x ≡ −1 (mod q). Thm B(a) (CRT witness with κ ∈ [1, q − 2], and κ(p, q) ≤ q − 2) checked in all 290 rows.

| q | 8 | 12 | 16 | 24 | 40 | 60 | 100 | 200 | 400 | 1000 |
|---|---|---|---|---|---|---|---|---|---|---|
| mean κ(p, q)/q, 19 primes near 10⁶ | .22 | .20 | .13 | .18 | .15 | .17 | .15 | .16 | .17 | .16 |
| same, 10 (★)-failures | .35 | .41 | .29 | .26 | .14 | .32 | .31 | .28 | .21 | .16 |
| max κ(p, q) (all 29) | 5 | 8 | 11 | 14 | 16 | 41 | 67 | 143 | 294 | 392 |
| mean N_q / log p, 19 primes near 10⁶ | 1.23 | 1.19 | 1.16 | .96 | .98 | .95 | .93 | 1.00 | .97 | .99 |

EVIDENCE for the reading of Thm B: the least cofactor scales linearly in q; the number of ordered witnesses with κ ≤ q is
≈ log p independently of q. At the (★)-failure primes the least cofactor is larger for small q (they have no κ = 1 at any
level, by definition).

## 6. The four FRONTIER §4 hard screens (for the best idea of this lane)

The best idea is "use a fixed-modulus representation theorem to supply the divisor, after removing the tie by
divisibility closure (Lemma 3.3)".
1. **T1 (squares).** The representation theorems themselves hold for moduli built from odd squares (RW for all q, HS for
   cube-free q, Weil for all m), so they are T1-blind; the step that must fail at m² is the cofactor condition (Lemma
   3.5). A2 passes T1 (it uses a QNR prime) but stops at a square cofactor. **Pass only for A2; fail for the
   representation step.**
2. **8/131.** The (q, κ) analysis is numerator-specific only through 4 | q; the representation theorems are
   numerator-blind. **Fail (no 4-specific step).**
3. **Tied modulus.** Closure removes the tie exactly (Lemma 3.3) but turns it into a finite menu per M (Thm C), and one
   class modulus q ≤ X^{1/2} prescribed independently of p cannot force a small cofactor for almost all p (Thm B). **Fail — the lane's main negative result.**
4. **Fixed p.** All statements are at one p, except Thm B(b)/Cor B1–B2, which are averages used only as barriers.
   **Pass** (but no positive pointwise input survives).

## 7. Verdict, proposed FRONTIER §7 text, bottom line

**Verdict: narrowed.** Scoped results (all about Type II and its (★) line; ES = Type I or Type II): (i) for a class
modulus q = q(X) ∈ 4ℕ, q ≤ X^{1/2}, prescribed independently of p, no statement valid for almost all p ≤ X guarantees a
cofactor below q/(log X)^{2+η} (false without the size bound), while the trivial CRT construction gives q − 2 (Thm B,
Cor B1; PROVED); (ii) removing the tie by divisibility closure is a finite menu per M (Thm C(a) PROVED, (b) CONDITIONAL
on H) with expectation O(log p) per M (EVIDENCE/Assessment); (iii) the free-object rungs reach the T1-admissible
square-cofactor rung A2, and the exact condition for A2 to be Type II implies a (★) triple with C = s²/4 (Thm A; PROVED);
(iv) the prime and EOS-shape sub-lotteries are CERTIFIED to fail at many primes < 10⁶ where (★) holds, and are predicted
to fail infinitely often under a Poisson zero law plus negligible unrestricted failures (CONJECTURE). Surviving: a **joint** statement over many class moduli at
one p — e.g. a lower bound for #{q ≤ Q : E(q, κ) for some κ | q/4} at fixed p — which is B2 itself, and the compact
inverse-graph form (Prop 3.2) as a clean target for a non-fixed-modulus idea (Assessment).

**Proposed FRONTIER §7 text (do not edit FRONTIER here; for the non-CRT item / §4 item 8):**
> *(z53 NONCRTSMOOTH, `Z53_NONCRTSMOOTH.md`.)* Fixed-modulus multiplicative representation (Erdős–Odlyzko–Sárközy,
> Ramaré–Walker, Szabó, Harman–Shparlinski, Weil on 𝓗) does not supply the tied divisor. In the two-modulus form
> E(q, κ): x ≡ y ≡ −1 (mod q), xy = κqp + 1, (★) is κ = 1 and Type II is κ | q/4 (PROVED; ES = Type I or Type II).
> The trivial CRT solution has κ ≤ q − 2; for a class modulus q = q(X) ∈ 4ℕ with q ≤ X^{1/2}, prescribed independently
> of p, all but o(π(X)) primes p ≤ X have no solution with κ ≤ q/(log X)^{2+η} (PROVED, elementary; false without
> q ≤ X^{1/2}) — so a statement about one such class modulus has at most a (log X)^{2+η} factor to gain over the
> trivial construction, and the Type II content is the aggregation over q (Assessment).
> Removing the tie by "height | M" is a finite menu per M (fails i.o. under H). Free-object constructions reach the
> T1-admissible square-cofactor rung (4/p = s²/x + 1/y + 1/z from one prime ℓ ≡ 3 (4) with (ℓ/p) = −1; ES^□-type); making
> it Type II implies a (★) triple with C = s²/4. Compact form: R(p) = #{x ∈ (1, 4p) : (x x̄ − 1)/p | x + 1} on the inverse
> graph of (ℤ/4p)^×. CERTIFIED (two engines): among primes p ≡ 1 (24) < 10⁶, 85 have (★) solutions but none with x or y
> prime, and 4614 none with x and y both prime.

**Bottom line.** The fixed-modulus representation theorems are the right tools for the wrong quantifier: they speak
about every class modulo one modulus, while (★) asks for a rare event at *some* class modulus q among ≍ p of them.
Writing Type II (the part of ES studied here) as the two-modulus event E(q, κ) makes this exact. At one prescribed q the
trivial CRT solution already gives cofactor κ ≤ q − 2, and — for q ≤ X^{1/2} prescribed independently of p — for most
p ≤ X nothing smaller than q/(log X)^{2+η} exists there; (★) and Type II need κ = 1 and
κ | q/4. Tie removal by divisibility closure is algebraically exact but becomes a finite menu. Free primes are absent from
(★) at 85 primes below 10⁶ where (★) holds, and prime pairs (the EOS shape) at nearly half of them. The one T1-carrying
thing a free prime does buy is the square-cofactor relaxation A2, already known as ES^□. What would be new is a
joint-in-q lower bound at fixed p; this lane found no tool for it.

## 8. Literature verification record

* Read in the primary source for this lane: Ramaré–Walker arXiv:1610.05804 Thm 1.1 (abstract/statement); Szabó
  arXiv:2208.05762 Thms 1, 2, 3 and the remark that EOS is "not known … even if one assumes GRH" (PDF); Harman–Shparlinski
  arXiv:1408.4515 Thms 1, 2; Shparlinski arXiv:1103.2879 Thm 13 and the "out of reach" remark; Bourgain–Garaev
  arXiv:1211.4184 Thm 2; Klurman–Shparlinski–Teräväinen arXiv:2609.25393 (abstract only); Shparlinski arXiv:1705.06087
  (abstract: the EOS question is "still open"); Banks–Shparlinski arXiv:2610.19597 (abstract).
* Via the repository's verified record: Garaev–Karatsuba almost-all box (PARITY_AUDIT row B1, R265); Linnik–Xylouris
  exponent 5 ((J)64).
* NOT verified, and not relied on for any PROVED claim: the EOS 1987 paper itself; Garaev's two-variable results; Walker
  2016; Munsch–Shparlinski smooth representations; Soundararajan/Harper smooth numbers in APs; Corvaja–Zannier
  gcd(u − 1, v − 1) for S-units (a natural tool for "x + 1, y + 1 share a large factor while x, y are S-units"; only
  secondary sources found, so not used); "Heath-Brown/Shparlinski xy ≡ 1 with x, y ≤ p^{1/2+ε}"; the GRH/Linnik size
  remarks on ℓ in A2.

## 9. Reproduction

```
g++ -O2 -o /tmp/z53lot scripts/z53_noncrtsmooth_lottery.cpp
D=data/z53/noncrtsmooth
for f in p24 test nearsq s1e7; do uv run --with sympy python scripts/z53_noncrtsmooth_lists.py $D/in_$f.txt; done
for f in p24 test nearsq s1e7; do (ulimit -v 6000000; timeout 1800 /tmp/z53lot < $D/in_$f.txt > $D/lot_$f.csv); done
# engine 2, in chunks (START STOP index ranges into the input list; ~3.7 s/prime near 1e6, ~90 s/prime near 1e7):
uv run --with cypari2 python scripts/z53_noncrtsmooth_verify2.py $D/in_p24.txt START STOP $D/v2/p24_K.csv
uv run --with cypari2 python scripts/z53_noncrtsmooth_fixedq.py $D/fixedq.csv
uv run --with pandas python scripts/z53_noncrtsmooth_summary.py > $D/summary.txt
uv run --with sympy python scripts/z53_noncrtsmooth_checks.py   # Prop 3.2 vs brute force; A2 for p < 2·10⁴
```
Runtimes: engine 1 ≈ 20 min (p24), ≈ 10 min (10⁷ sample); engine 2 ≈ 25 min on 20 cores for p24.

## 10. Review log

* *Checkpoint 1* (commit e2c614f2): §§1–3 skeleton.
* *Hostile review (deep-mode subagent, on commit f9a1ae44).* No FATAL. MAJOR, all fixed: (1) Thm B's scope overstated
  ("every fixed-modulus method", "cannot add anything") → precise quantifiers (class modulus prescribed independently of
  p; almost all p), broader readings labelled Assessment; (2) the non-residue claim of Prop 3.2 needs p ≡ 1 (4) (p = 11
  counterexample) → hypothesis added, general sign −(−1/p) stated; A1 needs p ≡ 1 (4); (3) A0's "only if q = 4C₀" was
  false (p = 5, q = 8, ℓ = 7) → exact test 4C₀ | ℓ + 1; (4) the "exact gap" A2 → A3 was only one-way → exact criterion
  s² | ℓ + 1 and 4ℓ | p + w, converse counterexample p = 5, ℓ = 3, s = 2; (8) Cor B2's scale had one log too few → proved
  bound τ(q/4)(log X)²/q separated from the single-log heuristic; (9) EOS needs **both** coordinates prime, while the
  measured Rp is "either" → both-prime column added (4614 failures); (10) size/factorisation deductions in the
  RW/smooth rows removed; one-coordinate smoothness reported and not refuted; (12) CERTIFIED exceeded the independent
  record → engine 2 rerun on all 9732 primes (0 mismatches); (15) Poisson extrapolation and the "overdispersion" remark
  were wrong (ordered counts double the variance) → corrected (var/mean ≈ 1.05 unordered), limiting statement labelled
  CONJECTURE with its hypothesis. MINOR, fixed: ℓ < p in A2's size bound and "multiplying" not "dividing"; primitive vs
  imprimitive character in Lemma 3.5; uniqueness of the height in Lemma 3.3, U_j < 1 and κ = ∞ conventions in Thm B;
  Banks–Shparlinski's fixed base prime, Szabó Thm 3, the Bourgain–Garaev size relation 4uBC = p + u + B; stale numbers
  (400 primes at 10⁷; fixed-q table split into the 19 primes near 10⁶ and the 10 failures; "best M" is chosen per p;
  N_q counts ordered witnesses); the CRT checker now checks κ ∈ [1, q − 2]; one label per claim.
* *Cross-model review* (`data/z53/xreview/REVIEW_NONCRTSMOOTH.md`, on commit c3aee577; verdict ACCEPT-WITH-FIXES). It
  re-derived every lemma/theorem as CORRECT and replicated all data with an independent engine
  (`scripts/z53_xrev_noncrtsmooth_census.cpp`: 18/18 columns exact on 10 747 inputs; `scripts/z53_xrev_noncrtsmooth_audit.py`:
  290/290 fixed-q rows exact). Fixes applied: (1, MAJOR) the size hypothesis q ∈ 4ℕ, q ≤ X^{1/2}, prescribed
  independently of p, restored in every restatement of Cor B1 (§0, §4.2 reading, §4.5, §6, §7, FRONTIER text), with the
  reviewer's counterexample q = 2 + 2∏_{3≤r≤X} r showing it is essential, the remark that B1 is vacuous for fixed q, and
  the explicit Type II remainder in Cor B2; (2, MAJOR) "ES is the union / ES as E(q, κ)" replaced by Type II, with
  ES = Type I or Type II stated; (3) the Poisson CONJECTURE now states the extra hypothesis on unrestricted failures;
  (4) κ(p, q) defined for q ∉ 4ℕ in Thm B(b).
