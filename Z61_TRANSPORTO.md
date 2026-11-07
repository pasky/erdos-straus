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

(§0 above is verbatim from commit 56564635 except for the title line of the file. Clarification, not a change: EXIT
means gcd(n, f) > 1 or gcd(n, k_f) > 1. The certificate is that gcd, which is a proper factor since f ≠ n and k_f < n.)

## 1. Results for R1 (CERTIFIED by exact computation; `data/z61/transporto/r1_census.jsonl`, `r1_summary.txt`)

**Lemma 1 (closed form, PROVED).** For each key (ℓ, j), write
* T = #{ORDINARY f: ℓ^j | a_f} (the tokens), and
* C = #{ORDINARY f ∈ S_{ℓ,j}: ℓ^j | a_f − 1} (the capacity).

Then R1 strands exactly max(0, T − C) tokens of key (ℓ, j) if S_{ℓ,j} contains no HIT or EXIT column, and none
otherwise.

*Proof.* All tokens of a key walk the same set S_{ℓ,j}, and each can traverse all of it. Sinks are unlimited, and each
capacity unit is consumed once. ∎

The literal walk (`--walk`) agrees with the closed form at every odd n ≤ 1501 (`walk_check.txt`).

*Consequence.* If n has an **r = 1 hit** (f ≡ 7 (8), f | n+1), then r − 1 = 0 lies in every fibre, so R1 is valid at
n. This is the T-form line g = 1.

**Falsifier table (mandatory).**

| screen | what is required | R1 | label |
|---|---|---|---|
| **F1 odd squares** (m = 3, 5, …, 45, 97, 101, 113; 25 n) | No hit exists (Lemma 7(ii), PROVED). Every surplus token must end at a proper-factor exit. | Valid only at n = 9. At 169: 51 tokens; 4 exit at their own column, 12 reach an exit on their fibre, **23 are stranded**. The forced surplus is 20 tokens over 15 primes, the same 15 surplus primes as the board's count. Stranded/tokens: 289 has 46/103, 361 has 64/133, 529 has 85/191, 113² has 1974/5943. **K1 fires.** | CERTIFIED |
| **F2 numerator 8** | A rule must not work verbatim with the U⁽⁸⁾ target set: U⁽⁸⁾ has prime zeros (Z59_CONV2). | Hit set restricted to the U⁽⁸⁾ targets (r \| (f+1)/8, or r = 8a with a \| (f+1)/8) at the 36 U⁽⁸⁾-zero primes ≤ 2·10⁵: no restricted hit at any of the 36, which is a consistency check of the restriction. R1-u8 is valid only at p = 5, and vacuously so: the only column, f = 7, is the non-liftable U₇ hit r = 2 with a = 1, so it carries no token. The screen passes trivially, because R1 already fails with the full U₇ target set. Of these primes, R1-u7 is valid only at 5 among the 26 that are ≤ 2·10⁴. | CERTIFIED |
| **F3 composites** | The 8 U₇-zero composites Z₇ must end at proper-factor exits. | **0/8 valid.** 105: 33 tokens; 23 exit at their own column, 4 at fibre exits, 6 stranded. 67 425: 883 stranded. On the first 60 R-zero composites from `composite_zeros_le8e6.txt`, R1 is valid at 0/60, although 46 of them have U₇ hits. | CERTIFIED |
| **F4 known prime zeros, hard primes** | Valid at every prime. A valid prime must not owe its validity merely to a hit existing (K3). | (★)-zero primes: **0/14**; at 409, 87 of 143 tokens are stranded. 𝔊*-zero primes ≤ 10⁷: valid at 3 of 34 (157, 12 301, 571 741), and each of the three has an r = 1 hit. A-half zero primes: valid only at 5. U₇-LATE prime 2 031 121: 777 385 of 1 260 386 tokens stranded. **All primes 3 ≤ p ≤ 2·10⁴: valid at 1431 of 2261.** Every valid prime has an r = 1 hit except 3, 5, 7, 11 and 31, and every invalid prime lacks one. There are 830 failures, the first at **p = 17**: its hits have r = 4 and r = 6, and the 13- and 7-tokens find no sink. **429 of the failures are p ≡ 3 (mod 4)**, where U₇ is PROVED via f = 2p+1, r = p+1. **K1 fires, and K3 fires on the successes.** | CERTIFIED (range) |

Tally for primes ≤ 2·10⁴, as (p mod 4, has an r = 1 hit, R1 valid) → count:
* (1, no, invalid) → 401;
* (1, no, valid) → 1;
* (1, yes, valid) → 723;
* (3, no, invalid) → 429;
* (3, no, valid) → 4;
* (3, yes, valid) → 703.

## 2. Why no rule of this kind can carry content

**Lemma 2 (forced hit traffic, PROVED).** Fix n and any designated hit set. Let O be the ORDINARY columns, all of which
have a_f ≥ 2, and suppose O ≠ ∅. Then P = ∏_{f∈O} (a_f − 1)/a_f lies in (0, 1), so P is not an integer, and some
prime ℓ has
D_ℓ := Σ_O v_ℓ(a_f) > N_ℓ := Σ_O v_ℓ(a_f − 1).

Consider any transport whose ℓ-tokens may terminate only in ℓ-numerator units of ORDINARY columns, or at HIT or EXIT
columns. In such a transport at least

forced(n) := Σ_ℓ max(0, D_ℓ − N_ℓ) ≥ 1

tokens terminate at HIT or EXIT columns. At a prime there are no EXIT columns, so at least forced(p) tokens terminate
at hits. ∎

Data: forced(n) = 0 in the census only when no ORDINARY column exists (n = 3, 5, 7). Otherwise forced(n) ≥ 1, as
Lemma 2 requires. For primes in [5000, 2·10⁴], the mean of forced(p) is 886, against a mean of 17.9 hit columns.

**Proposition 3 (the framework is idle, PROVED).**

(a) Suppose a transport in the astra-1 sense is valid at a prime p that has an ORDINARY column. Then by Lemma 2 some
token terminates at a HIT column. That column is a U₇ witness, so validity at p already *is* U₇(p). The deduction
"Q(p) ∈ ℤ, 0 < Q(p) < 1, contradiction" is never used.

(b) Conversely, let A be any procedure returning, for each odd n, either a HIT column or a proper factor of n.
Exhaustive search over F(n) is one example. Define the teleport rule T_A: every token moves in one step to A(n)'s
column, with potential 1 → 0. T_A satisfies conservation, termination and the exit restriction, and it is valid at n
iff A succeeds at n.

Hence "some rule meeting {moves, conserved ℓ-flux, potential, factor-or-hit exits} is valid at every prime" is
equivalent to U₇ at every prime. The only extra content is the K3 demand that the reason tokens reach a hit not be the
existence of a hit. That demand is a requirement on the *form* of a U₇ proof (local descent), and Q does not supply
it. ∎

*Reading.* astra-1 hoped to prove the inequalities Σ v_ℓ(a_f) ≤ Σ v_ℓ(a_f − 1) "prime by prime" at a hypothetical
hit-free prime. Lemma 2 says these inequalities are **false on the non-hit sub-table of every actual prime**. Any proof
of them must therefore use the hypothesis "no column is a hit" in a step that breaks at real primes, which is exactly
a hit-finding procedure. The integrality packaging gives nothing to estimate and nothing to transport.

**Observation 4 (foreign flux at primes; EVIDENCE; `scripts/z61_transporto_foreign.py`, `foreign.jsonl`).** Let the
forced primes be Fp = {ℓ: D_ℓ > N_ℓ}. Call a sink *valuation-faithful* if it accepts an ℓ-token only when ℓ divides
one of f, f+1, k, n+k, r, r−1, a of that sink column. This is deliberately generous; fable's board screen allowed
only a. Results:
* **Primes 13 ≤ p ≤ 2·10⁴:** at 2253 of 2257, some ℓ ∈ Fp is carried by no hit column. The exceptions are
  13, 19, 31 and 71.
* **Hard primes:**
  * 409: 26 of 30 forced primes are uncarried.
  * 2521: 125 of 125, with a single hit column.
  * 9601: 380 of 384.
  * 102 001: 3224 of 3228.
  * The same holds for all 14 (★)-zero and A-half zero primes listed.
* **Squares:** at 169, 11 of 15 forced primes are carried by no exit column (fable found 0 of 15 carried with
  capacity a only). At 529 it is 31 of 38.

So every valuation-faithful rule fails at essentially every prime, whatever its routing. A valid rule must let *hits*
absorb foreign valuations: the ℓ-label of a token carries no information about where it can end.
* The uncarried forced primes are mostly large, ℓ close to n, e.g. 101 917 at n = 102 001.
* Such an ℓ is a prime factor of essentially one a_f, and of no a_g − 1.
* This is fable's board-r3 "wildcard" objection, now verified at the hit exits of primes rather than only at the factor
  exits of squares. It settles the board's unresolved F2 dispute in fable's direction within this scope.

**Remark 5 (defect-word form; PROVED algebra, Assessment beyond).**
* **Defect word.** With s_f = (f+1)/d_f, every column satisfies n = d_f·s_f·k_f − a_f·d_f − k_f. So a column is a U₇
  word (x, y, z) = (d, s, k) whose x-term carries the defect a_f, and a hit is defect 1. This was verified symbolically
  and at every column for all odd n < 3000.
* **SL₂ form.** M_f = [[f, s],[n, ks − a]] = −L(k)·[[1, −s],[0, a]]·L(d) has det M_f = a_f, where L(c) = [[1,0],[c,1]].
* **Where a descent would have to act.** A Fermat-type descent would have to lower this determinant while keeping the
  tie s | f+1. At a prime n there are two factorisations M = γ·(Hecke matrix).
  * M = γ·[[1,b],[0,a]] keeps the top-left entry f, and so keeps the column itself.
  * M = [[a,b],[0,1]]·γ replaces f by (f − bn)/a, which does not preserve the tie.
* **Assessment:** no descent was obtained. This is only the precise place where one would have to act.

## 3. Verdict

* **R1: DEAD.** Pre-registered kills K1 and K3 both fire (§1). Termination (K2) holds, and so does conservation in
  the bookkeeping sense. What fails is that tokens are stranded at primes, squares and Z₇.
* **astra-1 (board F2): DEAD as a mechanism**, for this exact reason.
  * Lemma 2: every valid rule must deliver forced(p) ≥ 1 tokens to hits.
  * Prop. 3: the formal requirements are met by a teleport rule, so they add nothing to U₇.
  * Obs. 4: the natural non-circular restriction, valuation-faithful sinks, fails at 2253 of 2257 primes ≤ 2·10⁴.
  * There is no DORMANT residue beyond CONJECTURE U₇ itself, read with a "local descent" proof-form demand.
* **Scope.**
  * This does **not** show that U₇ has no descent-type proof. It shows that Q, its integrality and its ℓ-ledger
    contribute no inference toward one.
  * Prop. 3 is a statement about the transport framework, not a no-go for pointwise U₇.
  * No other rule was tried after R1 failed, per the pre-registration (no broadening).

**Proposed FRONTIER line (§6 dead ends):** "astra-1 (product Q = ∏(a_f−1)/a_f, U₇ ⟺ Q = 0; 'factor-or-hit valuation
transport'): DEAD as a mechanism (z61 TRANSPORTO). The ledger over non-hit columns always has a surplus (Lemma 2), so
any valid transport routes ≥ 1 token into a hit at every prime, and validity is U₇(p) verbatim. A teleport rule meets
every formal requirement (Prop. 3), so the requirements add nothing. Valuation-faithful sinks fail at 2253/2257
primes ≤ 2·10⁴ (foreign flux), and the explicit pre-registered rule R1 strands tokens from p = 17 and at all squares
≥ 25 and Z₇."

## 4. Reproduction

All runs used `ulimit -v 4000000` and `timeout` ≤ 1800 s.
```
uv run --no-project python scripts/z61_transporto_r1.py --walk 17 169 289 361 529 105   # single n, JSON lines
uv run --no-project python scripts/z61_transporto_r1.py --walk $(seq 9 2 1501)          # walk = closed form (747 n)
uv run --no-project python scripts/z61_transporto_census.py 20000      # 84 s -> data/z61/transporto/r1_census.jsonl
uv run --no-project python scripts/z61_transporto_foreign.py 20000     # 9 s  -> data/z61/transporto/foreign.jsonl
uv run --no-project python scripts/z61_transporto_summary.py           # -> data/z61/transporto/r1_summary.txt
```
Inputs: `data/z58/screens/{star_prime_zeros,gstar_zeros,composite_zeros_le8e6}.txt`,
`data/z60/lopez/u7half_tgt2_primes_1e8.txt`, `data/z59/conv2/union_K8_primes_1e8.txt`, and the LATE prime 2 031 121
from `data/z60/lopez/u7_all_1e8.txt.gz`. The R₈-zero primes near 10¹⁰ (`r8_zeros_1e10.txt`) were **not** run: a full
column table has about 2.5·10⁹ columns. Since R1 already fails from p = 17, they cannot change the verdict.
