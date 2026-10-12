# Brainstorm O141(d): ES as a Π₂ sentence of (N, +, |) and Lipshitz's local-to-global principle

Verdict: **COLLAPSES to B5/B2**, with an exact failing step. Two PROVED propositions record why.

## 1. Idea

Multiplication is not needed to state (a strengthening of) ES. By CRT, `∃x (a | x ∧ b | x+1)` ⟺
gcd(a,b) = 1. For coprime a, b, `4ab | N` ⟺ `4a | N ∧ b | N`. Put

  `Φ_d(a,b,e) :≡ e | a+b ∧ 4a | d+e ∧ b | d+e ∧ ∃x (a | x ∧ b | x+1)`,  a, b, e ≥ 1.

By ET Prop 2.3 (CONDITIONAL_ES Lemma 1.2), Φ_d gives the Type II solution (abk, acdk, bcdk) of 4/d, where
4abk = d+e and ce = a+b. Hence

  `ES'' :≡ ∀n ≥ 2 ∃d ∃a,b,e (d | n ∧ d ≥ 2 ∧ Φ_d(a,b,e))`

is a Π₂ sentence of the language {+, |, 1} (with ≥ definable from +). ES'' implies ES, by descent from d.
ES'' holds for even n (d = 2, a = b = 1, e = 2) and for n with a prime factor ≡ 3 (4) (a = b = e = 1). So
ES'' ⟸ "every prime p ≡ 1 (4) has a coprime Type II point" (CONJECTURE).
* EVIDENCE (`scripts/bs_logic_divsys.py`): every Mordell-hard prime < 3·10⁵ has a coprime Type II point.
  Among n ≡ 1 (4), n ≤ 2·10⁴, the (not necessarily coprime) Type II system is empty exactly at the odd
  squares and at n = 4545; for 4545 the divisor d = 5 works. Coprimality changes emptiness only at
  n = 105 and 5985, both composite.

The existential theory of (Z, +, |, ≤) is decidable (Bel'tyukov 1976; Lipshitz 1978). Lipshitz's method,
as refined by Lechner–Ouaknine–Worrell (LICS 2015) and later work, rests on a **local-to-global
principle**:
* a divisibility system in *increasing form* has an integer solution iff it has a solution modulo every
  prime in a finite set P(Φ);
* moreover it then has infinitely many solutions.

Here "increasing form" means that, for some total order of the variables, the leading variable of every
implied divisor f | g lies only in g.

The hope was: show Φ_p is "locally solvable" and invoke the LGP to get ES(p).

## 2. Literature anchor

* L. Lipshitz, "The Diophantine problem for addition and divisibility", Trans. AMS 235 (1978).
* A. Bel'tyukov (1976). From memory.
* Lechner–Ouaknine–Worrell, "On the complexity of linear arithmetic with divisibility", LICS 2015. Title
  and abstract verified.
* The statements of increasing form and the LGP, quoted here, were read in a 2022 ENS internship report
  (R. Defossez) that surveys these results. Its Theorem 4 says: an r-increasing system with solutions
  modulo every p ∈ P(Φ) has infinitely many solutions, with explicit bit bounds. That is a secondary
  source; the primary papers were not read.
* Undecidability of the full theory of (N, +, |) (J. Robinson) is standard. Whether its ∀∃ fragment is
  decidable is from memory, unverified, and not used.

## 3. Results

**Prop D1 (no increasing form; PROVED).** For every constant d ≥ 1, the system
{e | a+b, 4a | d+e, b | d+e} is not in increasing form for any order of a, b, e. Nor is any system
equivalent to Φ_d over N.

*Proof.*
* In the divisibility module of 4a, the polynomial d+e appears. So increasing form needs LV(4a) = a ≻ e,
  or else e ≻ a with e only on the right. The latter holds only if e ≻ a. Likewise b | d+e forces e ≻ b.
* But e | a+b puts a+b in the module of e. So increasing form needs max(a,b) ≻ e, which is a
  contradiction.
* Independently of syntax: a satisfiable increasing system has infinitely many solutions (LGP, Thm 4
  above). But Φ_d has finitely many, because e ≤ a+b and 4ab ≤ d+e give (4a−1)(4b−1) ≤ 4d+1. ∎

The obstruction is the **size cycle** e ≤ a+b, ab ≲ d+e. It is the same cycle that bounds every ES
search, now visible as a syntactic invariant. Lipshitz's procedure must therefore case-split and
instantiate bounded variables. For each fixed d this is a finite search (a fixed finite set of slices:
B2/B1).

**Prop D2 (local solvability is vacuous; PROVED).** For every d ≥ 1, including odd squares, and every
prime ℓ, Φ_d has a solution modulo ℓ in Lipshitz's sense (with gcd(a,b) = 1).

*Proof.*
* ℓ odd: take a = b = e = 1. The conditions read v_ℓ(1) ≤ v_ℓ(2) and v_ℓ(4) = 0 ≤ v_ℓ(d+1).
* ℓ = 2, d odd: take a = b = 1 and e ≡ −d (mod 4), e odd. Then v₂(e) = 0 ≤ v₂(2).
* ℓ = 2, d ≡ 2 (4): take a = b = 1 and e = 2.
* ℓ = 2, d ≡ 0 (4): take a = 1, b = 3 and e = 4. Then v₂(4) = 2 = v₂(a+b), and v₂(12) = 2 ≤ v₂(d+4).
  ∎

At odd squares d = m², however, Φ_d is globally empty: ET Prop 1.6, re-checked for d ≤ 2·10⁴ by the
script. So the LGP is false for Φ at every odd square.

## 4. Barrier screen

* **B5.** The failing step is named exactly: "local (Lipshitz) solvability ⇒ global solvability". It is
  false at every odd square, and it is licensed in Lipshitz's theorem only by increasing form, which Φ
  never has (D1). This is a divisibility-logic twin of the campaign's Prop 8.3 ("local + spinor ⇒
  global is false at odd squares").
* **B1.** p-adic solvability of Φ_d is congruence data. It holds for all d (D2), so it decides nothing.
  This matches Theorem M.
* **B2.** Lipshitz's case split instantiates variables down to finitely many slices. As a proof strategy
  it is the "fixed finite set of slices" route, which fails infinitely often under H.
* **B3, B4, B6.** Not applicable: no counting.

## 5. Viability Assessment: **COLLAPSES to B5** (step: Lipshitz LGP) and to B2 (case split)

* By-products, all PROVED and elementary:
  * the Π₂ (N, +, |) form ES'';
  * D1: no increasing form, because of the size cycle;
  * D2: local solvability is vacuous.
* Novelty is minimal, but the D1 cycle is a clean one-line explanation of why "decision procedures for
  linear arithmetic with divisibility" cannot be leveraged.
* A non-collapsing variant would need an LGP for divisibility systems *with* a size cycle under an
  extra archimedean hypothesis. At d = m² that hypothesis would have to fail, so it would amount to
  ES itself.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (§0.3 and the per-memo
paragraph). Counterexamples re-verified by `scripts/errata_check.py` (tag in brackets).

* **§1 CRT substitution is false:** gcd(a,b) = 1 does not imply gcd(4a,b) = 1, so "4a | d+e ∧ b | d+e" does not give
  4ab | d+e. Counterexample [lgp]: d = 9, (a,b,e) = (1,2,3) satisfies Φ₉ (3 | 3, 4 | 12, 2 | 12, x = 1), but
  4ab = 8 ∤ 12, so no Type II solution results. At d = 1 the same tuple satisfies Φ₁ while (4a−1)(4b−1) = 21 > 5,
  contradicting D1's bound. (The memo's script tests 4ab | d+e, a different, stronger formula.)
* **Repair:** replace b | d+e by 4b | d+e; with gcd(a,b) = 1 the lcm is then 4ab. The syntactic cycle and D2's local
  constructions survive, so the naive LGP remains unusable.
* §4's second collapse is invalid: finitely many branches per input d need not be a fixed finite family
  independent of d (redteam-automorphic-2 Thm 2.2(iii)). **Corrected verdict:** PARTIAL → H-A.
