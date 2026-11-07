# Z61_TRANSPORTO — one explicit factor-or-hit transport for U₇ (astra-1, board F2): pre-registration

**ES is OPEN. CONJECTURE U₇ is open.** Lane TRANSPORTO, wave z61 (Opus twin; the other twin's branch was not read).

## 0. Pre-registration (frozen before any test was run; commit `z61 transporto: pre-register rule R1`)

Target (Z60_LOPEZ §4.2): U₇(n) ⟺ some f ≡ 7 (mod 8), 7 ≤ f ≤ 2n+1, has r_f := (−n mod f) > 0 dividing f+1.
Columns F(n) = {f ≡ 7 (8): 7 ≤ f ≤ 2n+1, f ∤ n}; k_f = ⌈n/f⌉, r_f = k_f f − n, d_f = gcd(r_f, f+1),
a_f = r_f/d_f, Q(n) = ∏_{f∈F(n)} (a_f − 1)/a_f. Q(n) = 0 ⟺ U₇(n).

Column types: HIT (a_f = 1); EXIT (g_f := gcd(n, f)·… ≠ 1, precisely gcd(n, f) > 1 or gcd(n, k_f) > 1 —
a proper factor of n, since f ≠ n and k_f < n); ORDINARY (all others). At a prime n every column is HIT or ORDINARY.

**Rule R1 ("unit-shift Kummer transport").**
* *Tokens (denominator units):* (f, ℓ, j) for f ORDINARY or EXIT, ℓ prime, 1 ≤ j ≤ v_ℓ(a_f).
* *Capacity (numerator units):* (f, ℓ, j) for f ORDINARY, 1 ≤ j ≤ v_ℓ(a_f − 1); each unit absorbs one token.
* *Fibre:* S_{ℓ,j} = {f ∈ F(n): r_f ≡ 1 (mod ℓ^j)} — the Kummer "unit shift" of the token fibre
  r ≡ 0 (mod ℓ^j): inside a block (k fixed) r_{f+8t} = r_f + 8kt, so a token at r ≡ 0 is paired with the
  columns at r ≡ 1, which are exactly where (r−1)/r carries the numerator ℓ^j when d = 1.
* *Moves:* a token at an EXIT column exits at once (certificate gcd(n, f k_f)). Otherwise it walks S_{ℓ,j}
  cyclically starting at the first column after f; at each landing f′: EXIT → exit (proper factor);
  HIT → exit (hit); ORDINARY with a free unit (f′, ℓ, j) → deposit. Tokens are processed in increasing (ℓ, j, f).
* *Termination potential:* number of not-yet-visited columns of S_{ℓ,j} (strictly decreasing, ≥ 0).
* *Conservation (ℓ-flux ledger):* every token ends deposited, exited, or **stranded** (potential 0, no sink).
  R1 is *valid at n* iff nothing is stranded. Valid at a hit-free n would give Σ_f v_ℓ(a_f) ≤ Σ_f v_ℓ(a_f−1) + exits
  for every ℓ; at a prime (no exits) this would make Q(n) a positive integer < 1, impossible — so "R1 valid at every
  prime" would force U₇ at primes.

**Pre-registered kills.** (K1) conservation fails: a stranded token at a prime, or at a test composite/square
(where the surplus must end at proper-factor exits); (K2) termination fails; (K3) the endpoint condition at primes
is merely the existence of a hit (in some set); (K4) no rule writable. No broadening of moves after a
counterexample.

Tests: n = 169, 289, 361, 529; Z₇ = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425}; more odd squares;
the 14 (★)-zero primes, the 12 A-half zero primes, 38 𝔊*-zero primes (data/z58/screens/), U₇-LATE primes; the
numerator-8 sub-line (U⁽⁸⁾-zero primes, Z59_CONV2) with the hit set restricted to U⁽⁸⁾ targets.
