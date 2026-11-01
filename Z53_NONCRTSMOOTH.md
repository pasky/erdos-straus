# Z53_NONCRTSMOOTH — fixed-modulus multiplicative representation vs the tied divisor event

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on 4/p. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results, internally reviewed only (not refereed).

Lane brief: `z52bbriefs/z53_depth.md` + `z53_lanes.md` §NONCRTSMOOTH. Scripts `scripts/z53_noncrtsmooth_*`, data
`data/z53/noncrtsmooth/` (0.5 MB). Must-reads used: FRONTIER §§2–4, 6, 7; PARITY_AUDIT Remark 3.1 and rows B1, D11;
B2_ACROSS_FIELDS (M1/M2 table); Z52D_HYPERBOLA §§0–2; DISCOVERIES (J)28, (J)34, (J)43 (ES^□ and the phase diagram).

## 0. Summary

Fix a prime p. A (★) triple (u, B, C) gives x = 4Cu − 1, y = 4CB − 1 with xy = 4Cp + 1 and x ≡ y ≡ −1 (mod 4C).
Fixed-modulus multiplicative representation theorems produce **free** objects (primes, products of primes, small or
smooth integers) in a prescribed class modulo a **fixed** modulus. This lane locates exactly where the tie
"class modulus = 4C = (xy − 1)/p" breaks each such theorem, proves what is provable in that shape, and measures the
structured sub-lotteries numerically. The organising object is the two-modulus event

  **E(q, κ) : ∃ x, y ≡ −1 (mod q) with xy = κqp + 1** (q ∈ 4ℕ the *class modulus*, κ ≥ 1 the *cofactor*).

With q = 4C/κ this is "4Cp + 1 has a divisor ≡ −1 (mod 4C/κ)". (★) at level C is E(4C, 1); Elsholtz–Tao Type II is
E(q, κ) with **κ | q/4** (Lemma 3.4); E(q, κ) for a square κ is an ES^□-type relaxation.

1. **Dictionary (PROVED, §3).** (a) Tying x + 1, y + 1 to 4C by construction turns xy ≡ 1 (mod p) into the *additive*
   condition 4C ≡ ū + B̄ (mod p), and the whole remaining content of (★) is the archimedean window
   0 < 4uBC − u − B < 2p (Lemma 3.1; widening it to 3p makes it trivial and T1-blind). (b) Compact fixed-modulus form:
   **R(p) = #{x ∈ (1, 4p) : gcd(x, 4p) = 1, (x·x̄ − 1)/p divides x + 1}**, x̄ ∈ [1, 4p) the inverse of x mod 4p
   (Prop 3.2). So R(p) is a property of the inverse permutation of (ℤ/4p)^× on its fundamental domain; winners are
   quadratic non-residues mod p (Lemma CT in this form). (c) Divisibility closure (Lemma 3.3): the tie can be removed
   exactly by requiring "height | M" for a fixed M, which gives a tie-free problem with two fixed moduli (4M, 4p).
2. **Theorem B (fixed class modulus is decided by the trivial construction, up to log²; PROVED).** (a) For every p and
   every q ∈ 4ℕ with p ∤ q(q − 1), E(q, κ) holds for some κ ≤ q − 2 (CRT with x = q − 1). (b) For every q ≥ 4, J ≥ 1,
   X ≥ 3: #{p ≤ X prime : E(q, κ) for some κ ≤ J} ≤ (JX/q)(log(JX) + 6) + 4J^{3/2}(X/(q − 2))^{1/2}. Hence no statement
   "for every large p, E(q, κ) with κ ≤ K" holds when K ≤ q/(log p)^{2+η} (and q ≤ p^{1/2}); in particular (★) at a
   prescribed level C (J = 1) holds for at most a (log X)²/(4C)·(1 + o(1)) share of primes. Numerically the least
   cofactor is ≈ 0.16–0.27·q at p ≈ 10⁶ for q = 8 … 1000 (EVIDENCE, §5.2). **Every fixed-class-modulus method (Weil,
   Burgess, sieve or representation theorem) can therefore improve on the trivial CRT solution by at most a factor
   (log p)^{2+o(1)} in the cofactor; ES needs cofactor 1 (or κ | q/4). The ES content is entirely the aggregation over
   the class modulus q.**
3. **Theorem A (free-object rungs; PROVED constructions, with T1 status).** A0: fixed class modulus — one prime
   ℓ ≡ −1 (mod q) and C ≡ −(4p)⁻¹ (mod ℓ) (T1-blind). A1: class modulus q = 2C = (4C)/2, i.e. q ≥ (4C)^θ for every
   θ < 1 — d = 2p + 1, C = p + 1 (T1-blind). A2: T1-admissible with square cofactor κ = s², s < ℓ — one prime ℓ ≡ 3 (4)
   with (ℓ/p) = −1 gives 4·1·ℓ·C′ − 1 − ℓ = s²p, i.e. 4/p = s²/(ℓC′) + 1/(pℓC′) + 1/(pC′) (an ES^□-type relaxation,
   known in substance: (J)28, (J)43); its class modulus is (4H)^{1 − O(log ℓ/log p)} (H the height). A3 (Type II):
   κ | q/4. A4 ((★)): κ = 1. **Exact gap (A2 → A3): the free rung reaches the right class modulus up to a square
   cofactor s²; ES needs s² | q/4, which forces s² | ℓ + 1 and is again a single tied divisor event.**
4. **Theorem C (closure is a finite menu; PROVED + CONDITIONAL).** P_M(p) (Lemma 3.3) is the union of τ(M) events
   "4Cp + 1 has a divisor ≡ −1 (mod 4M)", C | M; Σ_M |P_M(p)| = Σ_{(★)} τ(u); for fixed M it fails for infinitely many
   p ≡ 1 (24) (CONDITIONAL on H, by B2 Thm 2.2(iii)); the best single M carries ≈ 0.44–0.52·log p ordered solutions on
   average (EVIDENCE), against ≈ 0.14–0.16·(log p)² for R(p).
5. **Literature (§4.4, verified statements).** Ramaré–Walker Thm 1.1, Szabó Thms 1–2, Harman–Shparlinski Thm 1,
   Shparlinski's *Modular hyperbolas* Thm 13, Bourgain–Garaev Thm 2, the EOS conjecture (open; Shparlinski 2017,
   Banks–Shparlinski 2026). Each produces free objects at a fixed modulus (rung A0), or power-size products whose heights
   are ≫ p^{1+δ} (no factorisation control), or almost-all statements (B6). None reaches A3/A4. The EOS-type statement at
   the class 1 (mod 4p) — "some x and x̄ are both prime" — is itself open, and the (★) prime sub-lottery sits inside it.
6. **Falsifiers (CERTIFIED / EVIDENCE, §5).** "x or y prime": 85 primes p ≡ 1 (24) ≤ 10⁶ have R(p) > 0 but no (★)
   triple with x or y prime (largest 997 201; two engines agree on the 32 above 5·10⁵). The prime sub-lottery has mean
   ≈ 0.42–0.51·log p unordered pairs, so a Poisson model predicts ≍ X^{1/2+o(1)} failures below X (EVIDENCE/CONJECTURE: the
   free-prime route fails infinitely often). "x and y both p^{1/4}-smooth": empty at 98.6–98.8 % of primes in every
   sample (dead). "x, y both p^{1/3}-smooth": empty at 69–85 %.

**Verdict: narrowed.** The fixed-modulus representation route is reduced to scoped theorems: at one class modulus the
trivial construction is optimal up to (log p)^{2+o(1)} (Thm B), the tie can be removed only by a finite menu (Thm C), and
free-object constructions reach the T1-admissible square-cofactor rung (A2) and no further. The four §4 hard screens are
in §6. What survives is precisely the aggregation over the class modulus q of events of probability ≍ log p/q — B2 itself;
the escape hatch left by Thm B is a *joint* statement over many q at one p (§7).

## 1. Statements attacked

Notation. p ≥ 5 prime. R(p) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = p} (FRONTIER §2.1). For a (★) triple put
x = 4Cu − 1, y = 4CB − 1. 𝓗 = {(x, y) : xy ≡ 1 (mod 4p)}. E(q, κ) as in §0.

* **(T) Target (FRONTIER §4 item 8 / hatch E1; §7 non-CRT lower bound).** For all sufficiently large primes
  p ≡ 1 (24), R(p) ≥ 1 (or Type II(p) ≥ 1), derived from a fixed-modulus multiplicative representation theorem. (★)
  itself fails at 14 primes ≤ 10¹⁰ (largest 8 813 281), so (T) is "for p > p₀". **Status: OPEN; the route is narrowed
  (§§3–4).**
* **(T1) Where does the tie break each theorem?** Status: answered (§4.4 table), via the dictionary (§3) and the
  (q, κ) picture.
* **(T2) Closest provable statement.** Status: Thm B(a) (trivial CRT, optimal up to (log p)^{2+o(1)} by Thm B(b)) for
  a fixed class modulus; Thm A2 (one QNR prime) for the T1-admissible square-cofactor rung. The exact gap to Type II is
  "κ | q/4" (Lemma 3.4, Thm A).
* **(T3) Construction routes.** (a) tie by construction (Lemma 3.1); (b) absorb the height into the modulus (Lemma 3.3,
  Thm C); (c) x, y as primes / smooth numbers (Thm A, §5.1). All narrowed.

## 2. Why this is not already closed

The closed list (brief + FRONTIER §6) contains one-step dualization at fixed conductor, Erdős–Turán with max|S_h|,
Cauchy–Schwarz in the function variable, low-conductor universality, the statement that Weil/Selberg–Hooley/bilinear
fixed-modulus savings "need p^{1−o(1)}" (PARITY_AUDIT §2), and H-B. PARITY_AUDIT row D11 records Ramaré–Walker/Szabó as
"pointwise parity breaking, but over free primes, so it does not reach the B2 event", in one line. None of these
analyses (i) multiplicative representation with free objects at a fixed modulus (the freedom M4 of B2_ACROSS_FIELDS),
(ii) the divisibility-closure reformulation (Lemma 3.3), which is genuinely tie-free (two fixed moduli 4M, 4p), or
(iii) what a fixed-class-modulus statement can possibly give (Thm B). The partial-tie ladder (Thm A) overlaps with known
material ((J)28 ES^□, (J)34 exponent cap, (J)43 phase diagram); it is re-derived here only in the (q, κ) language needed
to place the representation theorems, and attributed.

## 3. Dictionary (all PROVED)

**Lemma 3.1 (fixed-modulus-p additive form).** For (u, B, C) ∈ ℕ³ the following are equivalent:
(a) 4uBC − u − B = p;  (b) x = 4Cu − 1, y = 4CB − 1 satisfy xy = 4Cp + 1;
(c) p ∤ uB, **4C ≡ ū + B̄ (mod p)**, and Z := 4uBC − u − B < 2p.

*Proof.* (a)⇔(b): (4Cu − 1)(4CB − 1) = 4C(4uBC − u − B) + 1. (a)⇒(c): if p | u then B = 4uBC − u − p ≡ 0 (mod p), so
u, B ≥ p and Z ≥ u(4B − 1) − B ≥ B(4p − 1) − p ≥ 4p² − 2p > p, a contradiction; symmetrically p ∤ B. Reduce (a) mod p
and divide by uB. (c)⇒(a): Z ≡ uB(4C − ū − B̄) ≡ 0 (mod p), and Z ≥ (4u − 1)B − u ≥ 3u − 1 ≥ 2 > 0 (as C, B ≥ 1). A
positive multiple of p below 2p is p. ∎

*Reading.* "Tie by construction" (x + 1, y + 1 ∈ 4Cℕ) converts the multiplicative fixed-modulus condition xy ≡ 1
into an additive one on Kloosterman fractions — a two-term modular Egyptian fraction whose target 4C lies in the short
progression 4ℕ and is tied to the size: C ≤ (p + u + B)/(4uB). Beyond the congruence, (★) is the archimedean window
0 < Z < 2p, i.e. *less than two periods* of the modulus. Widening to Z < 3p is trivial: (u, B, C) = (1, 1, (p + 1)/2)
gives Z = 2p for every odd p, and also at every odd square (T1-blind).

**Proposition 3.2 (compact fixed-modulus-4p form).** For x coprime to 4p let x̄ ∈ [1, 4p) be its inverse mod 4p and
h(x) := (x x̄ − 1)/p. Then
  R(p) = #{x ∈ (1, 4p) : gcd(x, 4p) = 1, h(x) | x + 1},
the map (u, B, C) ↦ x = 4Cu − 1 is a bijection onto this set, with x̄ = 4CB − 1 and h(x) = 4C. Every winner satisfies
3 ≤ x, x̄ ≤ (4p + 1)/3, and **(x/p) = −1**.

*Proof.* Given a triple, u = (p + B)/(4BC − 1) ≤ (p + B)/(4B − 1) ≤ (p + 1)/3 (the middle term decreases in B), and
x = (p + u)/B ≤ p + u ≤ (4p + 1)/3 < 4p; likewise y < 4p. Since xy = 4Cp + 1 ≡ 1 (mod 4p) and y ∈ [1, 4p), y = x̄ and
h(x) = 4C | x + 1. Conversely let h(x) | x + 1 with x ∈ (1, 4p). Then x x̄ ≡ 1 (mod 4p) gives 4 | h(x), and h(x) ≥ 1
since x x̄ > 1; put C = h(x)/4. From x x̄ = 4Cp + 1 ≡ 1 (mod 4C) and x ≡ −1 (mod 4C) we get x̄ ≡ −1 (mod 4C), so
(u, B, C) = ((x + 1)/4C, (x̄ + 1)/4C, C) is a triple by Lemma 3.1(b). The two maps are inverse. For the residue claim:
−4Cp ≡ 1 (mod x), so −4Cp is a non-zero square mod x and the Jacobi symbol (−4Cp/x) = 1. The Kronecker symbol
χ_{−4C} = (−4C/·) is an odd character mod 4C and x ≡ −1 (mod 4C), so (−4C/x) = χ_{−4C}(−1) = −1 (the T1 computation of
PARITY_AUDIT Lemma 3.2). Hence (p/x) = −1, and by Jacobi reciprocity (p ≡ 1 (4)) (x/p) = −1. ∎

Checked against brute-force R(p) for the first 60 primes p ≡ 1 (4) and for 409, 2521, 3361
(`scripts/z53_noncrtsmooth_checks.py`; also x, x̄ ≤ (4p + 1)/3 and 4 | h(x) at every winner).

**Lemma 3.3 (divisibility closure: a tie-free two-fixed-moduli form).** For M ≥ 1 let
  P_M(p) := {x ≥ 1 : x ≡ −1 (mod 4M), ∃ y ≥ 1 with xy ≡ 1 (mod 4p), C := (xy − 1)/(4p) ∈ ℕ, C | M}.
Every x ∈ P_M(p) gives the (★) triple ((x + 1)/4C, (y + 1)/4C, C); every triple arises with M = C; and
Σ_{M≥1} |P_M(p)| = Σ_{(u,B,C)} τ(u).

*Proof.* C | M gives 4C | x + 1; xy = 4Cp + 1 ≡ 1 (mod 4C) then gives y ≡ −1 (mod 4C); apply Lemma 3.1(b). A triple lies
in P_M iff C | M and 4M | 4Cu, i.e. C | M | Cu: τ(u) values of M. ∎

**Lemma 3.4 (the (q, κ) picture; Type II = "κ | q/4").** Let q ∈ 4ℕ, κ ≥ 1. E(q, κ) holds iff
∃ (u, B): quB − u − B = κp. Elsholtz–Tao Type II (ff′ − 4c²dp = 1, f ≡ f′ ≡ −1 (mod 4cd), FRONTIER §1) is exactly
⋃_{q ∈ 4ℕ} ⋃_{κ | q/4} E(q, κ), and (★) is ⋃_q E(q, 1).

*Proof.* x = qu − 1, y = qB − 1: (qu − 1)(qB − 1) = q(quB − u − B) + 1. Type II with (c, d) is E(4cd, c) (ff′ = 1 + c·(4cd)·p);
conversely E(q, κ) with κ | q/4 is Type II with c = κ, d = q/(4κ). ∎

So (★) is the cofactor-1 line, Type II the region κ | q/4, and the class modulus q is "4C/κ" in the divisor form
"4Cp + 1 has a divisor ≡ −1 (mod 4C/κ)" with 4C = κq.

**Lemma 3.5 (T1-admissibility).** Call (q, κ) *T1-admissible* if the conductor of χ_{−κq} divides q. If n = m² is an
odd square (any m), then E_n(q, κ) (E with p replaced by n) fails for every T1-admissible (q, κ).
*Proof.* Let x | κqm² + 1 with x ≡ −1 (mod q). Every prime ℓ | x has −κqm² ≡ 1 (mod ℓ), so χ_{−κq}(ℓ) = 1; hence
χ_{−κq}(x) = 1. But χ_{−κq} is an odd character mod q, so χ_{−κq}(x) = χ_{−κq}(−1) = −1. ∎
Type II pairs (κ | q/4) are T1-admissible: κq = 4κ²d with d = q/(4κ), and χ_{−4κ²d}, χ_{−4d} have the same primitive
character, of conductor dividing 4d = q/κ | q. Square cofactors κ = s² are T1-admissible (cond χ_{−s²q} = cond χ_{−q} | q).
A cofactor κ with a prime ℓ ∤ q to an odd power is never admissible (ℓ | cond χ_{−κq}).

## 4. Theorems

### 4.1 Theorem A — free-object rungs (PROVED constructions)

Representation theorems supply a free prime (or product) ℓ in a prescribed class modulo a fixed modulus. In the divisor
form the only way to use a free ℓ is: fix its class, then solve for the height C modulo ℓ. The rungs below are what this
mechanism reaches.

* **A0 (fixed class modulus; T1-blind).** For any q ≥ 1 and any prime ℓ ≡ −1 (mod q), ℓ ∤ 2p (Linnik–Xylouris:
  ℓ ≪ q⁵, as used in (J)64), let C₀ ∈ [1, ℓ − 1] with 4C₀p ≡ −1 (mod ℓ). Then ℓ | 4C₀p + 1, ℓ ≡ −1 (mod q). Identical at
  every odd n coprime to ℓ, so T1-blind. It is (★) only if q = 4C₀ — the residue C₀ is forced by (ℓ, p) and is "random"
  in [1, ℓ).
* **A1 (class modulus (4C)^{1−o(1)}; T1-blind).** d = 2p + 1, C = p + 1, q = 2(p + 1): 4Cp + 1 = (2p + 1)², q | 4C,
  d ≡ −1 (mod q), and q = 4C/2 ≥ (4C)^θ for every fixed θ < 1 and p large. Same at n = m². So *the size* of the class
  modulus is not the obstruction; its exact relation to the height is (here κ = 2 ∤ q/4 since q/4 = (p+1)/2 is odd).
* **A2 (T1-admissible, square cofactor; one QNR prime).** Let p ≡ 1 (4) and ℓ ≡ 3 (4) prime with (ℓ/p) = −1. Then there
  is an even s ∈ (0, ℓ) with ps² ≡ −1 (mod ℓ), C′ := (ps² + 1 + ℓ)/(4ℓ) ∈ ℕ, and
  4·1·ℓ·C′ − 1 − ℓ = s²p, i.e. E(4C′, s²) holds with x = 4C′ − 1, y = 4C′ℓ − 1, and
  **4/p = s²/(ℓC′) + 1/(pℓC′) + 1/(pC′).**
  *Proof.* (−p/ℓ) = (−1/ℓ)(p/ℓ) = (−1)(ℓ/p) = 1 (quadratic reciprocity, p ≡ 1 (4)), so −p̄ is a square mod ℓ; of the two
  roots in (0, ℓ), whose sum is ℓ (odd), exactly one is even. ℓ | ps² + 1, 4 | ps² (s even) and 4 | 1 + ℓ, so
  4ℓ | ps² + 1 + ℓ. Then 4ℓC′ − 1 − ℓ = ps². The Egyptian form is (★)(s²p) divided by s² (FRONTIER §2.1 formula). ∎
  (q, κ) = (4C′, s²) is T1-admissible (Lemma 3.5), and indeed A2 is impossible at n = m² ((−m²/ℓ) = −1 for ℓ ≡ 3 (4)). Sizes: the height is H = C′s² and q = 4C′ = (4H)/s², so q = (4H)^{1−θ′} with
  θ′ = log s²/log 4H ≤ 2 log ℓ/log(p/ℓ): **the class modulus is (4H)^{1−o(1)} as soon as ℓ = p^{o(1)}** (e.g. under GRH
  via effective Chebotarev in ℚ(i, √p); unconditionally only ℓ ≪ p^{O(1)} — both Assessment, not re-derived). This is an
  ES^□-type relaxation, known in substance ((J)28 Prop 2.2: ONE prime r ≡ 3 (4) with (n/r) = −1; (J)43 phase diagram);
  checked for every prime p ≡ 1 (4) below 2·10⁴ (§9).
* **A3 (Type II): κ | q/4. A4 ((★)): κ = 1.**

**Exact gap A2 → A3 (PROVED).** In the A2 family the solution is Type II iff κ = s² divides q/4 = C′ (Lemma 3.4).
Since 4ℓC′ = ps² + 1 + ℓ and 4 | s², s² | C′ implies s² | 1 + ℓ. Write ℓ + 1 = s²w. Then s²w ≡ 1 (mod ℓ), so
ps² ≡ −1 gives p ≡ −w (mod ℓ), i.e. ℓ | p + w, and ℓ = 4(s²/4)w − 1: (u, B, C) = (w, (p + w)/ℓ, s²/4) is a (★) triple
(4wB(s²/4) − w − B = Bℓ − w = p). So asking the free rung to be Type II is asking for a (★) triple with C = s²/4 — a
single tied divisor event of p + w again (the trial form, FRONTIER §2.1). The free rung delivers the right class modulus
up to a square cofactor; removing the cofactor is B2.

### 4.2 Theorem B — one class modulus is decided by the trivial construction (PROVED)

For q ≥ 4 and a prime p ∤ q(q − 1) let κ(p, q) be the least κ ≥ 1 with E(q, κ) (equivalently: qκp + 1 has a divisor
≡ −1 (mod q); equivalently quB − u − B = κp is solvable).

**(a)** κ(p, q) ≤ q − 2.

*Proof.* x = q − 1 ≡ −1 (mod q). By CRT (gcd(q, p) = 1) take y ∈ [1, qp] with y ≡ −1 (mod q), y ≡ (q − 1)⁻¹ (mod p).
Then xy ≡ 1 (mod q) and (mod p), so xy = 1 + κqp with 1 ≤ κ ≤ ((q − 1)qp − 1)/(qp) < q − 1. ∎

**(b)** For every q ≥ 4, J ≥ 1 and X ≥ 3,
  #{p ≤ X prime : κ(p, q) ≤ J} ≤ (JX/q)(log(JX) + 6) + 4J^{3/2}(X/(q − 2))^{1/2}.

*Proof.* If κ(p, q) = j ≤ J, pick (u, B) with V := quB − u − B = jp; V determines p, so distinct p give distinct
(j, u, B). Fix j and count (u, B) with u ≤ B, V ≤ jX and j | V (pairs with u > B are counted by symmetry, factor 2).
u ≤ B gives V ≥ qu² − 2u ≥ (q − 2)u², so u ≤ U_j := (jX/(q − 2))^{1/2}. For fixed u, B ≤ (jX + u)/(qu − 1), and
(qu − 1)B ≡ u (mod j); a common divisor of qu − 1 and j would have to divide u (for solvability) and qu − 1, hence is 1,
so B lies in at most one class mod j: #B ≤ (jX + u)/(j(qu − 1)) + 1. Summing over u ≤ U_j with
Σ_{u≤U} 1/(qu − 1) ≤ 1/(q − 1) + (1 + log U)/q ≤ (log U + 7/3)/q (q ≥ 4) and Σ_{u≤U} u/(j(qu − 1)) ≤ U/(3j):
the count for j is ≤ (X/q)(log U_j + 3) + 2U_j ≤ (X/q)(½ log(jX) + 3) + 2U_j. Double and sum over j ≤ J, using
Σ_{j≤J} √j ≤ J^{3/2}. ∎

**Corollary B1.** Let q = q(X) ≤ X^{1/2} be a single class modulus chosen independently of p, and J ≤ q/(log X)^{2+η}
(η > 0). Then all but o(π(X)) primes p ≤ X have κ(p, q) > J (divide (b) by π(X) ≥ X/log X; after division the second
term of (b) is ≤ 4q log X/(√X (log X)^{3}) → 0). So no pointwise statement "for every p ∈ (X/2, X], E(q, κ) for some
κ ≤ K" with q fixed in advance can hold with K ≤ q/(log X)^{2+η} (statements where q may depend on p are the
aggregated problem and are not covered): **at a single class modulus, the trivial CRT solution (κ ≤ q − 2) is optimal up to a factor
(log p)^{2+o(1)}**, whatever method (Weil, Burgess with smooth weights, sieve, representation theorem) is used.
(A Brun–Titchmarsh count in place of "primes ⊂ integers" would save one log; not needed.)

**Corollary B2 (no single level decides (★)).** With J = 1, q = 4C: the share of primes p ≤ X having a (★) triple at
level C is ≤ (log X)(log X + 6)/(4C) + o(1). Likewise, with κ ranging over the τ(q/4) divisors of q/4, the share of p
having a Type II solution with class modulus q is ≤ τ(q/4)(log X)(log(qX) + 6)/q + o(1). (Averaged statements — B6
applies to them as *inputs*; they are used here only as no-go's for pointwise fixed-modulus statements.)

*Reading (Assessment).* At class modulus q the Type II region {κ | q/4} lies a factor ≍ q/log p below the threshold of
any fixed-modulus statement; its probability is ≍ τ(q/4) log p/q. ES is the union over q ≤ p of these sub-unit events.
The tie is therefore not a defect of particular theorems but the *aggregation over the class modulus*: a fixed-modulus
theorem can only ever speak about one q at a time (or about a fixed finite set, Thm C), and at one q it has nothing to
add to the trivial construction. EVIDENCE (§5.2): the measured least cofactor is 0.16–0.27·q (q = 8 … 1000, p ≈ 10⁶), and
the number of solutions with κ ≤ q is ≈ 1.0·log p for every q, matching the heuristic "≈ κ log p/q solutions with
cofactor ≤ κ".

### 4.3 Theorem C — the closure is a finite menu

**(a) (PROVED).** P_M(p) is the union over the τ(M) integers N_C = 4Cp + 1 (C | M) of the events "N_C has a divisor
≡ −1 (mod 4M)"; |P_M(p)| ≤ Σ_{C|M} τ(N_C); Σ_M |P_M(p)| = Σ_{(★)} τ(u) (Lemma 3.3).
**(b) (CONDITIONAL on Hypothesis H).** For every fixed finite set 𝓜 of M's, ⋃_{M∈𝓜} P_M(p) = ∅ for infinitely many
p ≡ 1 (24): P_M(p) ≠ ∅ certifies ES(p) through the fixed finite slice set {Type II (c, d) = (1, C) : C | M}, which
fails i.o. by `reviews/redteam-automorphic-2.md` Thm 2.2(iii) (FRONTIER B2). So M must grow with p (hatch E1).
**(c) (EVIDENCE).** The best single M carries on average 0.435·log p (p ≡ 1 (24) ≤ 10⁶), 0.52·log p (near-squares and
p ≈ 10⁷) ordered solutions, against R(p) ≈ 0.14–0.16·(log p)²; the maximising M is 1, 2, 3, 4, 5 or 6 in 83 % (p ≡ 1 (24) < 10⁶)
to 89 % (p ≈ 10⁷) of cases, and P_2(p) = ∅ for 17 % (10⁶) / 7 % (10⁷) of primes. Heuristic (Assessment): E|P_M(p)| ≈ c·τ(M) log p/M, so every
single closure problem has expectation O(log p), and → 0 once M ≫ (log p)^{1+δ}.

So "absorb the height into the modulus" works algebraically but converts (★) into a menu of τ(M) single integers per M:
for fixed M it is B1/B2(iii); for growing M the expectation per M collapses. Either way the content is again the union
over moving data.

### 4.4 Where the tie breaks each representation theorem

Statements below were read in the primary source (arXiv abstract or PDF) unless marked. "Rung" refers to Thm A.

| theorem (verified statement) | what it gives in ES coordinates | where the tie breaks |
|---|---|---|
| **EOS conjecture** (Erdős–Odlyzko–Sárközy 1987): every reduced class mod q contains p₁p₂, p_i ≤ q. OPEN (stated as open in Shparlinski arXiv:1705.06087 abstract; Banks–Shparlinski arXiv:2610.19597 abstract, 2026: true for q = prime powers up to a proportion exp(−c(log q)^{1/3}…) of classes, and with a third subpolynomial prime) | at q = 4p, class 1: a point (x, x̄) of the inverse graph with **x and x̄ both prime** (both < 4p, so x̄ is the least inverse) — power-size expected count ≈ 8p/log²p | (★) = the sub-count with h(x) | x + 1 (Prop 3.2), a filter of probability ≍ 1/C at height C; the prime (★) sub-lottery has ≈ 0.45 log p pairs and fails at 85 primes ≤ 10⁶ (§5.1). Even the unfiltered EOS-type existence is open |
| **Ramaré–Walker** Thm 1.1 (arXiv:1610.05804, JTNB 30 (2018)): q ≤ x^{1/16} ⇒ every invertible class mod q contains p₁p₂p₃ with all p_i ≤ x^{1/3} | (i) q = 4C, class −1: free x ≡ −1 (mod 4C), size ≤ (4C)^{16} — rung A0; (ii) q = 4p, class 1: N = p₁p₂p₃ = 4Hp + 1, H ≤ p^{15+o(1)} | (i) x must divide 4Cp + 1 (a congruence on p mod the free x); (ii) a divisor ≡ −1 (mod 4H) needs cofactor ≤ p while 4H ≈ N/p: probability ≍ 1/H among ≤ 8 divisors |
| **Szabó** (arXiv:2208.05762) Thm 1: q cube-free ⇒ |E₂(q)| ≥ (3/8 + o(1))φ(q) (two primes ≤ q); Thm 2: q large prime ⇒ E₆(q) = all (six primes ≤ q) | as RW; Thm 1 is a density (B6-type, over classes) | as RW; Thm 1 does not even give the class −1 |
| **Harman–Shparlinski** Thm 1 (arXiv:1408.4515): q cube-free large ⇒ every reduced a is n₁⋯n₁₄ (mod q), n_i ≤ q^{1/(4√e)+ε} | x ≡ −1 (mod 4C) as a product of 14 integers ≤ (4C)^{0.152}: x ≤ (4C)^{2.13}, x is (4C)^{0.16}-smooth — rung A0 | x must divide 4Cp + 1; in the balanced block x ≈ (4C)^{1.5} ≈ p^{3/4} would have to be p^{0.08}-smooth (ρ(10) ≈ 10⁻¹⁰); data: "x, y both p^{1/4}-smooth" is empty at 98.8 % of primes (§5.1) |
| **Weil on 𝓗** (Shparlinski, *Modular hyperbolas*, Thm 13, arXiv:1103.2879): #{xy ≡ a (m), x ∈ I, y ∈ J} = φ(m)|I||J|/m² + O(m^{1/2+o(1)}) | E(q, κ) in a box: after (u − q̄)(B − q̄) ≡ q̄² (mod p) one needs UV ≥ p^{3/2+ε}, i.e. cofactor κ ≍ q p^{1/2+ε} | worse than the trivial κ ≤ q − 2 (Thm B(a)); by Thm B nothing at fixed q can beat q/(log p)^{2+o(1)} |
| **Garaev–Karatsuba** (via Shparlinski §3.2 and KSWX §3.3; PARITY_AUDIT row B1, verified by R265): almost all a ⇒ xy ≡ a (p), x, y ≤ p^{1/2}(log p)^{1+ε} | right size scale (xy ≈ p) | averaged over the residue a (B6); at a = 1 trivial; the tie is not a residue condition |
| **Bourgain–Garaev** Thm 2 (arXiv:1211.4184): |I| < p^{3/46} ⇒ #{x̄ + ȳ + z̄ = λ, x, y, z ∈ I} < |I|^{2/3+o(1)} (λ ∉ I⁻¹ ∪ {0}) | the additive form 4C ≡ ū + B̄ (Lemma 3.1) is a two-term reciprocal sum | an *upper* bound; the ES target λ = 4C is tied to the size (uBC ≤ p/4) and the count is at critical density |
| **Klurman–Shparlinski–Teräväinen** (arXiv:2609.25393, abstract): a small set of small primes generates (ℤ/q)^× for all but O(Q(log Q)^{−A}) moduli q ≤ Q | almost all class moduli q = 4C | ES needs a *rare* event (probability ≍ log p/q) at *some* q, not a typical property of almost all q |
| Heath-Brown/Shparlinski "xy ≡ 1 (mod p), x, y ≤ p^{1/2+ε}" (named in the brief) | — | not located in a primary source (research agent, §8); at a = 1 the box problem is trivial ((1, 1)) and the non-trivial-box versions are covered by Thm 13 |
| **smooth numbers in APs** (Soundararajan; Harper) — statement *not verified* here | N = 4Hp + 1 y-smooth with y = p^{0.152+ε} (if the cited range holds) | only O(1) prime factors ⇒ τ(N) = O(1) ≪ 4H: a divisor ≡ −1 (mod 4H) has probability ≍ 1/H |

**Common pattern (Assessment).** Each theorem either (i) chooses a free object in a class modulo a fixed modulus
(rung A0 — the object then has to divide a forced integer, i.e. p must lie in a class modulo the free object), or
(ii) produces objects of size Q^{1+δ} or more (heights H ≥ p^δ), whose divisors cannot be steered into the class
−1 (mod 4H), or (iii) averages over residues or moduli (B6). By Thm B, (i) is capped at the trivial construction; by
Lemma 3.5 and Thm A, the T1-admissible free rung is A2; nothing reaches κ | q/4.

### 4.5 Closest provable statement and exact gap

* **Closest tie-free statement (fixed two moduli):** E(q, κ) for some κ ≤ q − 2, for every p ∤ q(q − 1) — trivial
  (Thm B(a)) and optimal up to (log p)^{2+o(1)} (Thm B(b)). Provable by the brief's methods (character sums mod p with
  smooth weights, Burgess) — but they cannot add anything (Cor B1).
* **Closest T1-carrying statement:** A2 — E(q, s²) with q = (4H)^{1−O(log ℓ/log p)}, from one prime ℓ ≡ 3 (4) with
  (ℓ/p) = −1 (Dirichlet; Burgess-type size bounds for ℓ are not needed for existence).
* **Exact gap:** Type II ⟺ some E(q, κ) with κ | q/4 (Lemma 3.4). At each q this has probability ≍ τ(q/4) log p/q
  (Cor B2 for the upper bound; heuristic for the matching size), so any proof must aggregate over q ≤ p — the moving
  modulus (B2). In the compact form (Prop 3.2): one needs a point x of the inverse graph of (ℤ/4p)^× whose height
  h(x) = (x x̄ − 1)/p divides x + 1; fixed-modulus information (the class of x mod 4p, or modulo any fixed Q) sees only
  the χ-shadow (x/p) = −1.

## 5. Computations

All commands with `ulimit -v 6000000` and `timeout`. Data in `data/z53/noncrtsmooth/` (summary: `summary.txt`).

### 5.1 Structured sub-lotteries of (★) (`scripts/z53_noncrtsmooth_lottery.cpp`)

For each n, all ordered (★) triples are enumerated through u ≤ n/3 and the divisors x ≡ −1 (mod 4u) of n + u (segmented
factorisation of [n + 1, 4n/3]); y's factorisation is read off n + B. Columns: R; Rp (x or y prime); Rs50/Rs33/Rs25 (x and
y both n^θ-smooth); least C; the M maximising |P_M| and |P_M| for M = 1, 2, 6, 12, 60. Cross-checks: brute-force Python
R(n) for n ∈ {73, 97, 193, 409, 577, 1009, 3361} (equal); a second engine (`scripts/z53_noncrtsmooth_verify2.py`, PARI
divisors of 4Cp + 1 over all C ≤ (p + 2)/4) re-derived R and Rp for the 32 primes > 5·10⁵ with R > 0, Rp = 0 and 5
controls: 0 mismatches (`verify2_p24.txt`). Controls: the 10 (★)-failures of the test list give R = 0 (consistent with
the census); odd squares give R = 0 identically (T1), so every sub-lottery is 0 there.

| sample | # | mean R/L² | mean Rp/L | Rp share | R > 0, Rp = 0 | Rs25 = 0 | Rs33 = 0 | Rs50 = 0 |
|---|---|---|---|---|---|---|---|---|
| all p ≡ 1 (24) < 10⁶ | 9732 | 0.140 | 0.835 | 0.47 | **85** (56 > 10⁵, 32 > 5·10⁵; max 997 201) | 98.8 % | 85.3 % | 14.3 % |
| near-squares m² + k, k ≤ 100, 10⁶–2.9·10⁶ | 600 | 0.158 | 0.926 | 0.41 | 0 (one R = 0: 1 134 241, a known (★) failure) | 98.7 % | 78.6 % | 9.0 % |
| 392 consecutive p ≡ 1 (4) > 10⁷ | 392 | 0.163 | 1.028 | 0.39 | 0 | 98.7 % | 69.1 % | 2.6 % |
| test primes (FRONTIER §4 item 14) | 15 | — | — | — | 3 of 5 with R > 0 (2521, 3361, 66529) | 100 % | 100 % | 60 % |

(L = log n; Rs-columns are fractions of primes with R > 0.)

* **CERTIFIED (two engines for p > 5·10⁵).** The "free prime" sub-route ((★) with x or y prime — the EOS/Ramaré–Walker
  shape) fails at 85 primes p ≡ 1 (24) below 10⁶ where (★) itself holds; among the test primes, at 2521, 3361 and 66529.
* **EVIDENCE.** Rp counts ordered triples; unordered prime pairs have mean ≈ 0.42–0.51·log p. Under a Poisson model the
  zero probability is p^{−0.42…−0.51}, and Σ_p p^{−1/2}/log p diverges: one expects ≍ X^{1/2+o(1)} primes below X where the
  prime sub-lottery fails (overdispersion ≈ 2× observed at 10⁶ makes this more likely, not less). **CONJECTURE:** there are
  infinitely many primes p with R(p) > 0 and no (★) triple with x or y prime. So no fixed-modulus theorem about *prime*
  divisors can carry (★).
* **EVIDENCE (dead route).** "x and y products of primes ≤ p^{1/4}" is empty at ≈ 98.7 % of primes in every sample (share
  of R: 0.2–0.45 %). "≤ p^{1/3}": empty at 69–85 %. Only "≤ p^{1/2}" survives as a constant share (≈ 28 %) — which is no
  longer "small primes".

### 5.2 Fixed class modulus (`scripts/z53_noncrtsmooth_fixedq.py`, `fixedq.csv`)

For 19 primes p ≡ 1 (4) near 10⁶ (from `nextprime(10⁶ + 1000k)`), the nine (★)-failures ≤ 10⁶ and 8 813 281, and
q ∈ {8, 12, 16, 24, 40, 60, 100, 200, 400, 1000}: κ(p, q) and N_q = #{(κ, x) : κ ≤ q, x | qκp + 1, x ≡ −1 (mod q)}.
Thm B(a) checked in all 290 rows.

| q | 8 | 12 | 16 | 24 | 40 | 60 | 100 | 200 | 400 | 1000 |
|---|---|---|---|---|---|---|---|---|---|---|
| mean κ(p, q)/q | .26 | .27 | .19 | .21 | .15 | .22 | .20 | .20 | .18 | .16 |
| max κ(p, q) | 5 | 8 | 11 | 14 | 16 | 41 | 67 | 143 | 294 | 392 |
| mean N_q / log p | 1.10 | 1.11 | 1.11 | 1.00 | .99 | .91 | .94 | 1.05 | .93 | 1.02 |

EVIDENCE for the reading of Thm B: the least cofactor scales linearly in q, and the number of cofactors ≤ q is ≈ log p
independently of q.

## 6. The four FRONTIER §4 hard screens (for the best idea of this lane)

The best idea is "use a fixed-modulus representation theorem to supply the divisor, after removing the tie by
divisibility closure (Lemma 3.3)".
1. **T1 (squares).** The representation theorems themselves hold for moduli built from odd squares (RW for all q, HS for
   cube-free q, Weil for all m), so they are T1-blind; the step that must fail at m² is the cofactor condition
   (Lemma 3.5). A2 passes T1 (uses a QNR prime) but stops at a square cofactor. **Pass only for A2; fail for the
   representation step.**
2. **8/131.** The (q, κ) analysis is numerator-specific only through 4 | q; the representation theorems are
   numerator-blind. Nothing here distinguishes 4/p from 8/p. **Fail (no 4-specific step).**
3. **Tied modulus.** Closure removes the tie exactly (Lemma 3.3) but turns it into a finite menu per M (Thm C) and a
   sub-unit expectation per class modulus (Thm B). **Fail — this is the lane's main negative result.**
4. **Fixed p.** All statements here are at one p, except Thm B(b)/Cor B1–B2, which are averages used only as no-go's.
   **Pass** (but no positive pointwise input survives).

## 7. Verdict, proposed FRONTIER §7 text, bottom line

**Verdict: narrowed.** Killed as scoped theorems: (i) at a fixed class modulus no method can beat the trivial CRT
solution by more than (log p)^{2+o(1)} in the cofactor (Thm B; PROVED); (ii) removing the tie by divisibility closure is
a finite menu per M (Thm C; PROVED + CONDITIONAL on H) with expectation O(log p) per M (EVIDENCE); (iii) free-object
constructions stop at the T1-admissible square-cofactor rung A2 (Thm A; PROVED constructions, A2 known in substance);
(iv) prime and small-smooth sub-lotteries are CERTIFIED to fail at many primes where (★) holds, and predicted to fail
infinitely often (EVIDENCE/CONJECTURE). Surviving: a **joint** statement over many class moduli at one p — e.g. a lower
bound for #{q ≤ Q : E(q, κ) for some κ | q/4} at fixed p — which is B2 itself, and the compact inverse-graph form
(Prop 3.2) as a clean target for anyone with a non-fixed-modulus idea.

**Proposed FRONTIER §7 text (do not edit FRONTIER here; for item 5 / §4 item 8):**
> *(z53 NONCRTSMOOTH, `Z53_NONCRTSMOOTH.md`.)* Fixed-modulus multiplicative representation (Erdős–Odlyzko–Sárközy,
> Ramaré–Walker, Szabó, Harman–Shparlinski, Weil on 𝓗) cannot supply the tied divisor. In the two-modulus form
> E(q, κ): x ≡ y ≡ −1 (mod q), xy = κqp + 1, (★) is κ = 1 and Type II is κ | q/4 (PROVED). At one class modulus q the
> trivial CRT solution has κ ≤ q − 2, and for all but o(π(X)) primes p ≤ X no solution has κ ≤ q/(log X)^{2+η} (PROVED,
> elementary): every fixed-modulus method is capped at the trivial construction up to (log p)^{2+o(1)}, and the ES
> content is the aggregation over q. Removing the tie by "height | M" is a finite menu per M (fails i.o. under H).
> Free-object constructions reach only the T1-admissible square-cofactor rung (4/p = s²/x + 1/y + 1/z, one QNR prime
> ℓ ≡ 3 (4), s < ℓ; ES^□-type). Compact form: R(p) = #{x ∈ (1, 4p) : (x x̄ − 1)/p | x + 1} on the inverse graph of
> (ℤ/4p)^×. CERTIFIED: 85 primes p ≡ 1 (24) < 10⁶ have (★) solutions but none with x or y prime.

**Bottom line.** The fixed-modulus representation theorems are the right tools for the wrong quantifier: they say
something about every class modulo one modulus, while (★) asks for a rare event (probability ≍ log p/q) at *some* class
modulus q among ≍ p of them. Writing ES as the two-modulus event E(q, κ) makes this exact: at a single q the trivial
CRT solution already achieves cofactor κ ≤ q − 2, nothing can do better than q/(log p)^{2+o(1)} for most p, and (★)/Type II
need κ = 1 / κ | q/4. Tie removal by divisibility closure is algebraically exact but turns into a finite menu; free
primes or small smooth numbers do not even exist inside (★) at many primes (85 certified below 10⁶). The one T1-carrying
thing a free prime does buy is the square-cofactor relaxation A2, already known as ES^□. What would be new is a
*joint-in-q* lower bound at fixed p; this lane found no tool for it.

## 8. Literature verification record

* Read in the primary source (arXiv abstract or PDF, fetched for this lane by a research subagent or by me): Ramaré–Walker
  arXiv:1610.05804 Thm 1.1; Szabó arXiv:2208.05762 Thms 1, 2; Harman–Shparlinski arXiv:1408.4515 Thms 1, 2; Shparlinski
  arXiv:1103.2879 Thm 13 and the "out of reach" remark; Bourgain–Garaev arXiv:1211.4184 Thm 2; Klurman–Shparlinski–
  Teräväinen arXiv:2609.25393 (abstract only); Shparlinski arXiv:1705.06087 (abstract: EOS question "still open");
  Banks–Shparlinski arXiv:2610.19597 (abstract).
* Via the repository's verified record: Garaev–Karatsuba almost-all box (PARITY_AUDIT row B1, R265); Linnik–Xylouris
  exponent 5 ((J)64).
* NOT verified (not relied on for any PROVED claim): the EOS 1987 paper itself; Garaev's two-variable results; Walker
  2016; Munsch–Shparlinski smooth representations; Soundararajan/Harper smooth numbers in APs (range q ≤ y^{4√e−δ});
  Corvaja–Zannier gcd(u − 1, v − 1) for S-units (a natural tool for "x + 1, y + 1 share a large factor while x, y are
  S-units"; only secondary sources were found, so it is not used); "Heath-Brown/Shparlinski xy ≡ 1 with x, y ≤ p^{1/2+ε}".

## 9. Reproduction

```
g++ -O2 -o /tmp/z53lot scripts/z53_noncrtsmooth_lottery.cpp
D=data/z53/noncrtsmooth
for f in p24 test nearsq s1e7; do uv run --with sympy python scripts/z53_noncrtsmooth_lists.py $D/in_$f.txt; done
for f in p24 test nearsq s1e7; do (ulimit -v 6000000; timeout 1800 /tmp/z53lot < $D/in_$f.txt > $D/lot_$f.csv); done
uv run --with cypari2 python scripts/z53_noncrtsmooth_verify2.py $D/lot_p24.csv 500000 > $D/verify2_p24.txt
uv run --with cypari2 python scripts/z53_noncrtsmooth_fixedq.py $D/fixedq.csv
uv run --with pandas python scripts/z53_noncrtsmooth_summary.py > $D/summary.txt
uv run --with sympy python scripts/z53_noncrtsmooth_checks.py   # Prop 3.2 vs brute force; A2 for p < 2·10⁴
```
Runtimes: p24 ≈ 20 min, s1e7 ≈ 10 min (1.4 s per prime at 10⁷), others < 2 min.

## 10. Review log

*Checkpoint 1* (commit e2c614f2): §§1–3 skeleton.

*[pending hostile review]*
