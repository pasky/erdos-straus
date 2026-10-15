# NEAR_SQUARE_EXIST — near-square primes: from the hardness explanation towards existence (task O225, wave Z-b)

Status: in progress (O225). **ES is not solved here, nor any infinite case of it unless explicitly stated with a complete
proof.** Labels as in DISCOVERIES.md. Builds on NEAR_SQUARE.md ((J)55, R225), THREE_SQUARES.md ((J)53), DEDEKIND_ES.md
Thm 4.5 (the sign table). Memos BRAINSTORM/z2_*.md, scripts `scripts/z2_*`.

Notation. p ≡ 1 (mod 4) prime (p ≡ 3 (4) is trivial). A *word* is (t, u, v) ∈ ℕ³ with tuv − u − v = p;
A = tu − 1, A* = tv − 1, AA* = tp + 1, p + u = vA, p + v = uA*; χ(w) = (A/p) (= (A*/p)). Words are the same objects
seen from two sides:
* *t-side (level t):* divisors A | tp + 1 with A ≡ −1 (mod t) (then A* ≡ −1 (mod t) automatically);
* *u-side (u-level u):* divisors A | p + u with A ≡ −1 (mod u) (t = (A + 1)/u, v = (p + u)/A).

**Sign table (DEDEKIND_ES Thm 4.5, PROVED + CERTIFIED there).** For n ≡ 1 (mod 4): χ(w) = −1 ⟺ 4 divides one of
t, u, v, A, A*. (Re-checked: `scripts/z2_words.c` mode 1, all 34 913 178 words with u ≤ v of all 332 180 primes
p ≡ 1 (4) below 10⁷: 0 mismatches between (A/p) and the table.)

## 1. The u-side mechanism for every u (goal 1; PROVED)

**Prop 1.1 (u-side T1, all u).** Let p ≡ 1 (mod 4) be prime and u ≥ 1 with p + u = x² + y², gcd(x, y) = 1. Then every
word with this u (or with v = u) has χ = +1. If u is even there is no word with this u at all.
*Proof.* N := p + u = vA. Since gcd(x, y) = 1, every odd prime factor of N is ≡ 1 (mod 4) and 4 ∤ N.
*u even.* N is odd, so N ≡ 1 (mod 4) and u ≡ 0 (mod 4). Then A = tu − 1 ≡ 3 (mod 4), but A | N forces A ≡ 1 (mod 4):
no word. (Equivalently: by the table every word with 4 | u has χ = −1, so the u-level is "clean" only vacuously.)
*u odd.* N even ⇒ x, y odd ⇒ N ≡ 2 (mod 8) ⇒ u ≡ 2 − p ≡ 1 (mod 4).
– A odd: A ≡ 1 (4) (product of primes ≡ 1 mod 4), v = N/A ≡ 2 (4); tu = A + 1 ≡ 2 (4) ⇒ t ≡ 2 (4); A* = tv − 1 is odd.
  So none of t, u, v, A, A* is ≡ 0 (4).
– A even: A = 2A′, A′ ≡ 1 (4), so A ≡ 2 (4); v = N/A is odd with v ≡ 1 (4); tu = A + 1 ≡ 3 (4) ⇒ t ≡ 3 (4) (u ≡ 1);
  A* = tv − 1 ≡ 2 (4). Again none of the five is ≡ 0 (4).
By the sign table χ = +1. The v-side statement is the same argument with (u, A) ↔ (v, A*). ∎
CERTIFIED-style check (`scripts/z2_words.c` mode 1): all primes p ≡ 1 (4) below 10⁷: 1 358 527 words have p + u or
p + v a sum of two coprime squares; 0 have χ = −1; none of them has the flagged u (or v) even. Control: all odd squares
below 10⁶: 6 434 flagged words, all χ = +1 (as every word at a square).
So R225's "even u" gap closes trivially: for even u the hypothesis forces u ≡ 0 (4), and 4 | u is exactly the u-level
on which *every* word has χ = −1 — the hypothesis then says there are no words. This is the cleanest form of the
u-side mechanism: **at 4 | u, χ = −1 is free and the whole content is "p + u has a divisor ≡ −1 (mod u)"; p + u a sum of
two coprime squares kills that divisor (T1: p = m², u = 4 gives m² + 4).**

