# y5_even_middle — the Mordell position alone: even-middle-letter certificates (O213, items (a)/(b))

## Idea
Among the three position classes of y5_five_positions, H = {o = h or h′} is the only one where the factorisation
event sits on the small number o + 1 and N enters through a congruence mod o. Does H alone carry SQ₅?

By mod-2 rigidity, o ∈ {h, h′} ⟺ the even edge is {c, m} or {m, s} ⟺ **m is even**. Then exactly one outer letter e
is even, since c + s is odd. The word is a certificate ⟺ 8 | m·e (FRIEZE Cor 1.3). So:

**SQ_H(N):** N = cms − c − s with positive c, m, s, m even, and 8 | m·e, where e ∈ {c, s} is the even outer letter.
Equivalently, 4 | m (the classical slice 4/p = 1/(kcs) + 1/(kcp) + 1/(ksp) for p = 4kcs − c − s), **or** 2 ∥ m and
4 | e.

In divisor form: ∃ even c, and a divisor o | N + c with o ≡ −1 (mod lcm(2c, 8)) (PROVED equivalent for the P_h half;
the P_h′ half is the mirror image).

## Literature
* The 4 | m slice is the classical identity behind Type II with "a = 1" (Mordell; Elsholtz–Tao §2). Its failure at
  some primes is classical: here 9 primes ≡ 1 (8) ≤ 10⁶ (409, 577, 5569, …).
* DK five slices: (J)9; FRIEZE Cor 1.3.

## Barrier screen
* B2: SQ_H is a divisor event on N + c.
* For bounded (c, s) it is a congruence family p ≡ −(c + s) (mod s·lcm(2c, 8)), and for bounded (c, m) it is
  p ≡ −c (mod cm − 1). Both are B1.
* B5/T1: every certificate dies at squares.
* B6: pointwise.
So SQ_H is a sub-lottery, like "Type I alone" and "Type II alone" (MODEL_SPECIFIC table; f_I, f_II ≥ 1 to 10⁸).

## Cheap numerics (`scripts/y5_positions.c`, log `logs/y5_positions.txt`; EVIDENCE)
* **Primes p ≡ 1 (8) ≤ 10⁷ (165 976): SQ_H holds at every one, for formal and for interior words.**
  * Position class C (o = c or s) fails at 10 primes (formal; 21 interior), all ≤ 10⁶.
  * Position class M (o = m) fails at 147 (formal; 394 interior).
  * The pure 4 | m slice fails at 9 primes ≤ 10⁶.
  * Mean numbers of certificate words per prime (counting only words with c ≤ s): H 26.8, C 23.7, M 13.5.
  * At locally square primes p ≡ 1 (840) the means are 19.4 / 15.9 / 7.9: H is the least suppressed.
  * The minimum H-count is 1, at p = 2521 and 53 881.
* All non-square N ≡ 1 (4) ≤ 10⁶ (249 500):
  * SQ₅ (formal) fails only at 105, and interior only at 2 values, as known.
  * **SQ_H fails at exactly 22 composite N:** 105, 1465, 3865, 4545, 5481, 10305, 12145, 34489, 36841, 39361, 40425,
    51129, 67425, 95505, 115465, 147609, 179361, 196065, 199369, 210105, 341145, 392505. No prime is among them.
* T1 control: no certificate at the 499 odd squares ≤ 10⁶ (y5_ocensus; holds for every position class by T1).

## Assessment
CONJECTURE SQ_H (EVIDENCE to 10⁷ at primes ≡ 1 (8), to 10⁶ at primes ≡ 1 (4)): every prime p ≡ 1 (4) is
cms − c − s with m even and 8 | m·e.
* This is a 2-of-5-slice sub-conjecture of SQ₅, structurally singled out as the position where o is N-free.
* With mean count ~27 at 10⁷, never failing is what the lottery heuristics predict, so this is not deep evidence.
* The 22 composite exceptions are a new fingerprint list. Each is ≡ 1 (mod 4) and has a small factor
  (3, 5, 7, 13, …): 105 = 3·5·7, 1465 = 5·293, 3865 = 5·773, 34489 = 7·13·379, …
* Promise 1/5: it shrinks the target but does not change its nature.
