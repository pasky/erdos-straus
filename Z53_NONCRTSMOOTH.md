# Z53_NONCRTSMOOTH — fixed-modulus multiplicative representation vs the tied divisor event

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results, internally reviewed only.

Lane brief: `z52bbriefs/z53_depth.md` + `z53_lanes.md` §NONCRTSMOOTH. Scripts `scripts/z53_noncrtsmooth_*`, data
`data/z53/noncrtsmooth/`.

**Status: CHECKPOINT 1 (skeleton).** Sections marked *[to do]* are not yet written.

## 0. Summary *[to do at final]*

## 1. Statements attacked

Notation. p ≥ 5 prime. R(p) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = p} (FRONTIER §2.1). For a (★) triple put
x = 4Cu − 1, y = 4CB − 1, so xy = 4Cp + 1 and x ≡ y ≡ −1 (mod 4C). 𝓗 = {(x, y) : xy ≡ 1 (mod 4p)}.

* **(T) Target (FRONTIER §7 target-5 lane, §4 item 8 / hatch E1).** A non-CRT pointwise lower bound: for all
  sufficiently large primes p ≡ 1 (24), R(p) ≥ 1 (or Type II(p) ≥ 1), obtained from a *fixed-modulus multiplicative
  representation theorem* (every class mod a fixed modulus contains a product of small primes / smooth numbers /
  small integers: Erdős–Odlyzko–Sárközy, Garaev, Shparlinski, Walker, Ramaré–Walker, Szabó, Harman–Shparlinski, Weil on
  𝓗). Status: OPEN; (★) itself fails at 14 primes ≤ 10¹⁰ (largest 8 813 281), so (T) is "for p > p₀".
* **(T1) Where does the tie break each theorem?** Precise location of the height-dependent class condition in each
  fixed-modulus coordinate system. Status: §2 (PROVED dictionary) + §3.
* **(T2) Closest provable statement.** The strongest statement of the shape "fixed modulus(es) + multiplicatively
  structured objects + size" that is provable by the representation methods, and the exact gap to (★)/Type II.
  Status: §4 *[in progress]*.
* **(T3) Construction routes.** (a) "tie by construction" (x + 1, y + 1 ∈ 4Cℕ) and (b) "absorb the height into the
  modulus" (divisibility closure, Lemma 2 below), (c) x, y as products of small primes / smooth numbers.

## 2. Why this is not already closed

The closed list (brief + FRONTIER §6) contains: one-step dualization at fixed conductor, Erdős–Turán/Fejér with
max|S_h|, Cauchy–Schwarz in the function variable, low-conductor universality, Weil/Selberg–Hooley/bilinear fixed-modulus
savings "need p^{1−o(1)} saving" (PARITY_AUDIT §2), parity-breaking at fixed p (H-B). PARITY_AUDIT row D11 records
Ramaré–Walker/Szabó as "pointwise parity breaking, but over free primes, so it does not reach the B2 event" — one line,
no analysis of *which* fixed-modulus statement is closest or how the tie enters.

What is new here (escape claimed): none of the closed items analyses **multiplicative representation with free objects
at a fixed modulus** (the freedom M4 of B2_ACROSS_FIELDS), nor the *divisibility-closure* reformulation (Lemma 2), which
makes the class modulus fixed (4M) and the second modulus fixed (4p) **with no tie at all** — the tie is replaced by
"the height divides M". That is a genuinely tie-free fixed two-modulus product-representation problem; the question is
what it costs (§3) and what a representation theorem can prove about it (§4).

## 3. First lemmas (CHECKPOINT 1)

**Lemma 1 (fixed-modulus-p dictionary; PROVED).** For (u, B, C) ∈ ℕ³ the following are equivalent:
(a) 4uBC − u − B = p;
(b) x = 4Cu − 1, y = 4CB − 1 satisfy xy = 4Cp + 1;
(c) p ∤ uB, **4C ≡ ū + B̄ (mod p)**, and 4uBC − u − B < 2p.

*Proof.* (a)⇔(b): (4Cu − 1)(4CB − 1) = 4C(4uBC − u − B) + 1. (a)⇒(c): if p | u then B = 4uBC − u − p ≡ 0 (mod p), so
u, B ≥ p and 4uBC − u − B ≥ 4uB − u − B ≥ 2p² > p, impossible; symmetrically p ∤ B. Reducing (a) mod p and dividing by
uB gives the congruence. (c)⇒(a): Z := 4uBC − u − B = uB(4C − ū − B̄) ≡ 0 (mod p) in ℤ/p, and Z ≥ (4u − 1)B − u ≥
3u − 1 ≥ 2 > 0; a positive multiple of p below 2p equals p. ∎

So "tie by construction" (x + 1, y + 1 ∈ 4Cℕ) turns the fixed-modulus-p condition xy ≡ 1 into an **additive** condition
on Kloosterman fractions, 4C ≡ ū + B̄ (mod p) (a two-term modular Egyptian fraction with target in the short progression
4ℕ), and the whole content of ES-(★) beyond the congruence is the archimedean window 0 < Z < 2p — a window of *less than
two periods* of the modulus. Relaxing it to Z < 3p is trivial: (u, B, C) = (1, 1, (p+1)/2) gives Z = 2p for every odd p,
and the relaxed statement holds at every odd square (T1-blind). (PROVED, one line.)

**Lemma 2 (divisibility closure: a tie-free fixed two-modulus form; PROVED).** Let M ≥ 1. Define
P_M(p) := {x ≥ 1 : x ≡ −1 (mod 4M), ∃ y ≥ 1 with xy ≡ 1 (mod 4p), C := (xy − 1)/(4p) ∈ ℕ and C | M}.
Then every x ∈ P_M(p) gives the (★) triple ((x + 1)/(4C), (y + 1)/(4C), C), and every (★) triple arises from M = C.
Moreover Σ_{M≥1} |P_M(p)| = Σ_{(u,B,C)} τ(u) (sum over (★) triples, x-side).

*Proof.* C | M gives 4C | 4M | x + 1. Then xy = 4Cp + 1 ≡ 1 (mod 4C) and x ≡ −1 force y ≡ −1 (mod 4C), and
Lemma 1 (b)⇒(a) applies. Conversely M = C. For the identity: a (★) triple lies in P_M iff C | M and 4M | 4Cu, i.e.
C | M | Cu, and there are τ(u) such M. ∎

*Reading.* For fixed M, P_M(p) ≠ ∅ is a product-representation problem with **two fixed moduli** (4M for the class
of x, 4p for the product xy) and a hyperbolic size bound xy ≤ 4Mp + 1 — no height-dependent modulus. The tie has been
traded for the arithmetic condition "height | M". **Cost (to be quantified in §4):** the region xy ≤ 4Mp + 1 meets the
class 1 (mod 4p) in exactly M integers 4Cp + 1, of which only the τ(M) with C | M count; so P_M is the union of τ(M)
single-integer events "4Cp + 1 has a divisor ≡ −1 (mod 4M)" — a finite menu for fixed M (B1/B2(iii): fails i.o. under H),
and for growing M a family whose local expected count is ≍ τ(M)·log p/φ(4M)-ish (Assessment, to be made exact).

**First falsifier (planned, §5).** Multiplicatively structured sub-lotteries of (★) at the test primes and controls:
(i) x or y prime ("free-prime" representation, Ramaré–Walker/EOS shape); (ii) x and y both p^θ-smooth (Harman–Shparlinski
shape); (iii) the best fixed M (max |P_M(p)|) and the least M with P_M(p) ≠ ∅. A structured sub-lottery that is empty at
some prime p > 10⁶ where R(p) > 0 is a CERTIFIED counterexample to that sub-route.

## 4. Closest provable statement and the exact gap *[in progress]*

## 5. Computations *[to do]*

## 6. Screens (FRONTIER §4) *[to do]*

## 7. Verdict, proposed FRONTIER §7 text, bottom line *[to do]*
