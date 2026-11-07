# Z61_TRANSPORTO — one explicit factor-or-hit transport for U₇ (astra-1, board F2): rule R1 is DEAD; astra-1 is DORMANT, and all its content sits in the locality clause

**ES is OPEN. CONJECTURE U₇ is open.** This memo proves nothing about U₇ or ES. Lane TRANSPORTO, wave z61. This is the
Opus twin; the other twin's branch (side-agent/z61-transport) was not read. Time used: about 2.5 h of the 4 h box. A
hostile review (gpt-6-astra, deep) was applied: §5.

**Bottom line.**
* **The rule.** One explicit factor-or-hit transport, R1 (the unit-shift Kummer transport), was written down before
  any test. It has moves, an ℓ-flux ledger, a termination potential, and exits only at hits or proper-factor
  certificates (§0).
* **R1 is DEAD by its pre-registered kills.**
  * K1, conservation, fails at primes. Tokens are stranded from p = 17 on, at 830 of the 2261 primes ≤ 2·10⁴. Of these
    830, 429 are p ≡ 3 (mod 4), where U₇ is PROVED.
  * K1 also fails on the falsifier side. Tokens are stranded at every tested odd square ≥ 25 and at all 8 Z₇
    composites, instead of ending at the factor exits.
  * K3 fires on R1's successes. R1 is valid at a prime p ≤ 2·10⁴ exactly when an r = 1 hit (f | p+1) exists, apart
    from the exceptions 3, 5, 7, 11 and 31. That column is a sink in every fibre.
* **Where the content sits (Lemma 2, PROVED; Prop 3, PROVED with stated scope).**
  * At every n with an ordinary column, the ℓ-ledger of the non-hit columns has a surplus.
  * Hence every factor-or-hit transport that is valid on the actual table of a prime routes at least forced(p) ≥ 1
    tokens into hit columns.
  * The formal requirements, other than the locality clause K3, are met by a trivial one-step rule, so they constrain
    nothing.
  * All of astra-1's content is therefore in K3, the demand that the route to a hit be locally forced. Q supplies no
    such step.
* **Valuation-faithful hit sinks (Obs. 4, EVIDENCE).**
  * Nonzero-carrier version: a hit may absorb an ℓ-token only if ℓ divides a *nonzero* local quantity of that hit
    (f, f+1, k, n+k, r, r−1 or a). This fails at 2253 of the 2257 primes in [13, 2·10⁴], and at every hard prime run.
  * Zero-carrier version: a zero quantity (r − 1 = 0 at an r = 1 hit) is allowed to carry every ℓ. This fails at 828
    of the 2257, and its successes again rest on the r = 1 universal sink, apart from 19, 31 and 71.
* **Verdict.** R1 is **DEAD**. astra-1 is **DORMANT**, for the exact reason in §3, and is not fundable. Reopen it only
  if someone states a concrete local step lemma, of the form "non-hit column ⇒ explicit successor of smaller potential,
  or a proper factor".

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

(§0 above is verbatim from commit 56564635; only the file's title and status lines changed. Clarifications, which do
not change the rule:
* EXIT means gcd(n, f) > 1 or gcd(n, k_f) > 1. The certificate is that gcd.
* EXIT takes **precedence** over HIT. A U₇ witness column (a_f = 1) with gcd(n, f k_f) > 1 is typed EXIT; this is
  harmless for routing, since both kinds are sinks.
* `nH` counts HIT-typed columns. `nH_any` counts all columns with a_f = 1.)

## 1. Results for R1 (CERTIFIED by exact computation; `data/z61/transporto/r1_census.jsonl`, `r1_summary.txt`, `walk_traffic.jsonl`)

**Lemma 1 (stranded count in closed form, PROVED).** For each key (ℓ, j), write
* T = #{ORDINARY f: ℓ^j | a_f} (the tokens), and
* C = #{ORDINARY f ∈ S_{ℓ,j}: ℓ^j | a_f − 1} (the capacity).

Then R1 strands exactly max(0, T − C) tokens of key (ℓ, j) if S_{ℓ,j} contains no HIT or EXIT column, and none
otherwise.

*Proof.* All tokens of a key walk the same set S_{ℓ,j}, and each can traverse all of it. Sinks are unlimited, and each
capacity unit is consumed once. So if a sink lies in S, every token ends. If not, a token is stranded exactly when all
C units are used. ∎

Checks and scope:
* The literal walk (`--walk`) gives the same stranded count at every odd n in [3, 1501] (750 inputs,
  `walk_check.txt`).
* Lemma 1 determines only the *stranded* count. When a sink exists, the walk can exit at it before unused capacity is
  reached. The census field `sink_routed_lb` is therefore only a lower bound on sink traffic, and the traffic figures
  below come from the literal walk.

*Consequence.* If n has an **r = 1 hit** (f ≡ 7 (8), f | n+1), then r − 1 = 0 lies in every fibre, so R1 is valid at
n. This is the T-form line g = 1.

**Falsifier table (mandatory).**

| screen | what is required | R1 | label |
|---|---|---|---|
| **F1 odd squares** (m = 3, 5, …, 45, 97, 101, 113; 25 n) | No hit exists (Lemma 7(ii), PROVED). Every surplus token must end at a proper-factor exit. | Valid only at n = 9. At 169, literal walk: 51 tokens; 4 exit at their own column, 13 exit at a factor column on their fibre, 11 deposit, **23 are stranded**. The forced surplus is 20 tokens over 15 primes, the same 15 surplus primes as the board's count. Stranded/tokens: 289 has 46/103 (22 fibre exits), 361 has 64/133 (41), 529 has 85/191 (51), 113² has 1974/5943. **K1 fires.** | CERTIFIED |
| **F2 numerator 8** | A rule must not work verbatim with the U⁽⁸⁾ target set: U⁽⁸⁾ has prime zeros (Z59_CONV2). | Hit set restricted to the U⁽⁸⁾ targets (r \| (f+1)/8, or r = 8a with a \| (f+1)/8) at the 36 U⁽⁸⁾-zero primes **p ≡ 1 (4)** ≤ 2·10⁵. The input file lists only p ≡ 1 (4); the reviewer counts 15 further zeros p ≡ 3 (4) below 2·10⁵, beginning 3, 11, 19, 131, and these were not run. No restricted hit occurs at any of the 36, which is a consistency check of the restriction. R1-u8 is valid only at p = 5, and vacuously so: the only column, f = 7, is the non-liftable U₇ hit r = 2 with a = 1, so it carries no token. The screen passes trivially, because R1 already fails with the full U₇ target set. Of the 26 of these primes that are ≤ 2·10⁴, R1-u7 is valid only at 5. | CERTIFIED |
| **F3 composites** | The 8 U₇-zero composites Z₇ must end at proper-factor exits. | **0/8 valid.** 105, literal walk: 33 tokens; 23 exit at their own column, 4 at factor exits on their fibre, 6 stranded. 67 425: 883 stranded. On the first 60 R-zero composites from `composite_zeros_le8e6.txt`, R1 is valid at 0/60. Of those 60, 54 have U₇ witnesses (`nH_any`). For 8 of them, 57, 177, 345, 1617, 13 041, 20 337, 20 601 and 27 825, the witnesses lie only in EXIT-typed columns. | CERTIFIED |
| **F4 known prime zeros, hard primes** | Valid at every prime. A valid prime must not owe its validity merely to a hit existing (K3). | (★)-zero primes: **0/14**; at 409, 87 of 143 tokens are stranded. 𝔊*-zero primes: 34 of the 38 were run (those ≤ 10⁷; the 4 larger ones were omitted for table size). R1 is valid at 3 of them (157, 12 301, 571 741), and each of the three has an r = 1 hit. A-half zero primes: valid only at 5. U₇-LATE prime 2 031 121: 777 385 of 1 260 386 tokens stranded. **All primes 3 ≤ p ≤ 2·10⁴: valid at 1431 of 2261.** Every valid prime has an r = 1 hit except 3, 5, 7, 11 and 31, and every invalid prime lacks one. There are 830 failures, the first at **p = 17**: its hits have r = 4 and r = 6, and the 13- and 7-tokens find no sink. **429 of the failures are p ≡ 3 (mod 4)**, where U₇ is PROVED via f = 2p+1, r = p+1. **K1 fires, and K3 fires on the successes.** | CERTIFIED (range) |

Tally for primes ≤ 2·10⁴, as (p mod 4, has an r = 1 hit, R1 valid) → count:
* (1, no, invalid) → 401;
* (1, no, valid) → 1;
* (1, yes, valid) → 723;
* (3, no, invalid) → 429;
* (3, no, valid) → 4;
* (3, yes, valid) → 703.

## 2. Where the content of a factor-or-hit transport sits

**Lemma 2 (forced hit traffic, PROVED).**

*Hypotheses.*
* Fix n and a designated hit set.
* Let O be the ORDINARY columns, and assume O ≠ ∅ and a_f ≥ 2 on O. This holds for the U₇ hit set. It fails for the
  U⁽⁸⁾-restricted set at p = 5, where an ORDINARY column has a = 1.
* Consider a transport on the actual table in which:
  * labels are conserved: an ℓ-token stays an ℓ-token;
  * numerator capacity is used injectively: each ℓ-numerator unit absorbs at most one ℓ-token;
  * ℓ-tokens may terminate only in ℓ-numerator units of O, or at HIT or EXIT columns; and
  * no token is stranded.

*Statement.* At least forced(n) := Σ_ℓ max(0, D_ℓ − N_ℓ) ≥ 1 tokens terminate at HIT or EXIT columns, where
D_ℓ = Σ_O v_ℓ(a_f) and N_ℓ = Σ_O v_ℓ(a_f − 1).

*Proof.* P = ∏_O (a_f − 1)/a_f lies in (0, 1), so it is not an integer, and some ℓ has v_ℓ(P) < 0, i.e. D_ℓ > N_ℓ.
Injectivity bounds by N_ℓ the number of ℓ-tokens that can terminate in numerator units. ∎

At a prime there are no EXIT columns, so the ≥ forced(p) tokens terminate at hits. In the census, forced(n) = 0 only
at n = 3, 5, 7, where O = ∅, and at p = 5 under U⁽⁸⁾, where the hypothesis a ≥ 2 fails. For primes in [5000, 2·10⁴]
the mean of forced(p) is 886, against a mean of 17.8 hit columns.

**Proposition 3 (PROVED; scope stated).**

(a) Let a transport satisfy the hypotheses of Lemma 2 and be valid on the actual table of a prime p with O ≠ ∅. Then
some token terminates at a HIT column, which is an explicit U₇ witness. So a proof that such a transport is valid at
all primes proves U₇ at primes directly; the implication does not pass through "Q(p) ∈ ℤ ∩ (0,1)".

(b) Let A be any procedure returning, for each odd n, a HIT column or a proper factor of n. Exhaustive search is one
example. Define the teleport rule T_A: every token moves in one step to A(n)'s column, with potential 1 → 0. T_A
satisfies conservation, termination and the exit restriction, and it is valid at n iff A succeeds. T_A is *excluded*
by K3. The point of (b) is only that the requirements other than K3 constrain nothing. All of astra-1's content
therefore sits in the locality clause K3.

(c) Now take astra's original contradiction architecture: no hit sinks, and prove D_ℓ ≤ N_ℓ on a hypothetical
hit-free prime table. Suppose the proof justifies each move only by the non-hit status of the columns that move
visits, together with the arithmetic of n. Run it on the table of an actual prime p. A token whose route meets no hit
has all its premises true there. By Lemma 2, at least forced(p) routes must meet a hit, so at actual primes the proof
*is* a factor-or-hit transport in the sense of (a). Proofs that use the global hypothesis "no column is a hit" in a
non-local way, for example by counting, are **not** covered by (c). ∎

*Assessment.* (a) to (c) are not a no-go for U₇, and not a no-go for astra-1 in full generality. They show that the
product Q and its integrality contribute no inference of their own. Whatever proves U₇ by this route is a locally
forced hit-finding descent, or else a non-local use of the hit-free hypothesis. In the second case the ℓ-ledger is no
longer the operative tool.

**Observation 4 (foreign flux at primes; EVIDENCE; `scripts/z61_transporto_foreign.py`, `foreign.jsonl`).** Let the
forced primes be Fp = {ℓ: D_ℓ > N_ℓ}. A *valuation-faithful* sink accepts an ℓ-token only when ℓ divides one of the
carrier quantities f, f+1, k, n+k, r, r−1, a of that sink column. Two conventions:
* **NZ: nonzero carriers only.** Results:
  * Primes 13 ≤ p ≤ 2·10⁴: some ℓ ∈ Fp is carried by no hit at 2253 of 2257. The exceptions are 13, 19, 31 and 71.
  * Hard primes: the same holds at every one run, namely 7 (★)-zero primes from 409 to 102 001 and 8 A-half zero
    primes from 193 to 66 529. For example 409 has 26 of 30 forced primes uncarried, 2521 has 125 of 125 with a
    single hit, 9601 has 380 of 384, and 102 001 has 3224 of 3228.
  * Squares: at 169, 11 of 15 forced primes are carried by no sink (fable's board screen, which allowed only a, found
    0 of 15 carried). At 529 it is 31 of 38.
* **Z: a zero quantity is divisible by every ℓ.** Then an r = 1 hit, with r − 1 = 0, is a universal sink. Results:
  * Primes in [13, 2·10⁴]: uncovered at 828 of 2257. The covered primes are exactly those with an r = 1 hit, plus 19,
    31 and 71.
  * The hard-prime and square figures above are unchanged, because none of those inputs has an r = 1 sink.

*Reading.* Under NZ, the forced ℓ-flux at a prime has no valuation-faithful destination; under Z, its only
destinations are r = 1 hits. Every other hit can absorb these tokens only through a zero (a − 1 = 0, which holds at
every hit), i.e. as a wildcard. This is fable's board-r3 "wildcard" objection, verified at the *hit* exits of primes
and not only at the factor exits of squares.

The uncarried forced primes are mostly large, ℓ close to n; for example 101 917 at n = 102 001. Such an ℓ divides
essentially one a_f and no a_g − 1. Within scope this supports fable's side of the board's F2 dispute. It is not a
proof that no admissible rule exists.

**Remark 5 (defect-word form; PROVED algebra, Assessment beyond).**
* **Defect word.** With s_f = (f+1)/d_f, every column satisfies n = d_f·s_f·k_f − a_f·d_f − k_f. So a column is a U₇
  word (x, y, z) = (d, s, k) whose x-term carries the defect a_f, and a hit is defect 1. This was verified symbolically
  and at every column for all odd n < 3000.
* **SL₂ form.** M_f = [[f, s],[n, ks − a]] = −L(k)·[[1, −s],[0, a]]·L(d) has det M_f = a_f, where L(c) = [[1,0],[c,1]].
* **Where a descent would have to act.** A Fermat-type descent would have to lower this determinant while keeping the
  tie s | f+1. At a prime n there are two factorisations M = γ·(Hecke matrix).
  * M = γ·[[1,b],[0,a]] keeps the top-left entry f, and so keeps the column itself.
  * M = [[a,b],[0,1]]·γ replaces f by (f − bn)/a, which does not preserve the tie.
* **Assessment:** no descent was obtained. This is only the precise place where a step lemma would have to act.

## 3. Verdict

* **R1: DEAD.** The pre-registered kills K1 and K3 both fire (§1). Termination (K2) holds. What fails is that tokens
  are stranded at primes, at tested odd squares and at Z₇.
* **astra-1 (board F2): DORMANT, not fundable.** The exact reasons:
  * (i) The one rule written in the box died. The pre-registration forbids broadening after a counterexample.
  * (ii) By Lemma 2 and Prop 3, a valid factor-or-hit transport delivers ≥ forced(p) ≥ 1 tokens to hits. The
    requirements other than K3 are vacuous, so the whole content is a locally forced step lemma, which nobody has
    stated.
  * (iii) By Obs. 4, valuation-faithful hit sinks fail at almost every prime ≤ 2·10⁴ (NZ), or work only through the
    r = 1 universal sink (Z).
* **Reopening condition.** A concrete step lemma: "non-hit ORDINARY column ⇒ explicitly computed successor with
  smaller potential, or a proper factor of n". It must pass this memo's falsifier table.
* **Scope.**
  * Nothing here shows that U₇ lacks a descent-type proof.
  * Prop 3(c) does not cover proofs that use the hit-free hypothesis non-locally.

**Proposed FRONTIER line (§6 dead ends):** "astra-1 (Q = ∏(a_f−1)/a_f, U₇ ⟺ Q = 0, 'factor-or-hit valuation
transport'): DORMANT (z61 TRANSPORTO).
* The pre-registered explicit rule R1 (unit-shift Kummer transport) is DEAD. It strands tokens from p = 17 (830/2261
  primes ≤ 2·10⁴, including 429 with p ≡ 3 (4)), at every tested odd square ≥ 25 and at all of Z₇. Its successes are
  the r = 1 hits.
* The non-hit ℓ-ledger always has a surplus (Lemma 2). So a valid transport at a prime routes ≥ 1 token into a hit,
  and the formal requirements other than locality are vacuous (Prop 3).
* Valuation-faithful hit sinks fail at 2253/2257 primes ≤ 2·10⁴ with nonzero carriers, and at 828/2257 if r − 1 = 0
  counts as a universal carrier.
* Reopen only with a concrete local step lemma."

## 4. Reproduction

All runs used `ulimit -v 4000000` and `timeout` ≤ 1800 s.
```
uv run --no-project python scripts/z61_transporto_r1.py --walk 17 169 289 361 529 105   # single n, JSON lines
uv run --no-project python scripts/z61_transporto_r1.py --walk $(seq 3 2 1501)          # walk = closed form (750 n)
uv run --no-project python scripts/z61_transporto_census.py 20000      # 84 s -> data/z61/transporto/r1_census.jsonl
uv run --no-project python scripts/z61_transporto_foreign.py 20000     # 9 s  -> data/z61/transporto/foreign.jsonl
uv run --no-project python scripts/z61_transporto_r1.py --walk 169 289 361 529 105 1465 3865 4545 10305 12145 \
    > data/z61/transporto/walk_traffic.jsonl                           # literal-walk traffic
uv run --no-project python scripts/z61_transporto_summary.py           # -> data/z61/transporto/r1_summary.txt
```
Inputs:
* `data/z58/screens/{star_prime_zeros,gstar_zeros,composite_zeros_le8e6}.txt`;
* `data/z60/lopez/u7half_tgt2_primes_1e8.txt`;
* `data/z59/conv2/union_K8_primes_1e8.txt` (p ≡ 1 (4) only);
* the LATE prime 2 031 121, from `data/z60/lopez/u7_all_1e8.txt.gz`.

Not run, because a full column table has about n/4 columns:
* the R₈-zero primes near 10¹⁰ (`r8_zeros_1e10.txt`);
* the 4 𝔊*-zero primes > 10⁷;
* the (★)-zero primes > 2·10⁵ in the foreign screen.

Since R1 already fails from p = 17, none of these can change its verdict.

## 5. Hostile review (gpt-6-astra, deep) and responses

| # | severity | finding | response |
|---|---|---|---|
| 1 | BLOCKER | The first version's "Prop 3 ⇒ astra-1 DEAD as a mechanism" overreached. The teleport rule is excluded by K3, and a contradiction proof may use the global hit-free hypothesis. | Accepted. Verdict changed to **DORMANT**. Prop 3 was restated: (b) now says the content sits in K3; the new (c) states its locality hypothesis and excludes non-local uses. FRONTIER text revised. |
| 2 | MAJOR | Obs. 4 skipped zero quantities: at an r = 1 hit, every ℓ divides r − 1 = 0. At p = 41, the uncovered 19 and 37 are admissible. | Accepted. Both conventions are now reported: NZ gives 2253/2257; Z gives 828/2257, with the r = 1 dichotomy. The "carries no information" phrasing was replaced by the scoped reading. |
| 3 | MAJOR | `sink_routed` is a lower bound, not the literal walk's traffic. | Accepted. Field renamed `sink_routed_lb`; the literal walk now reports deposits and exits (`walk_traffic.jsonl`); table numbers corrected (169: 13 fibre exits, 289: 22, 361: 41, 529: 51), matching the reviewer. |
| 4 | MAJOR | EXIT precedence hides U₇ witnesses: 54 of 60 RC composites have hits, not 46. | Accepted. Precedence is documented, `nH_any` added, and the table corrected, listing the 8 exit-only cases. |
| 5 | MINOR | The U⁽⁸⁾ input covers only p ≡ 1 (4). | Scope stated in the table and in §4. |
| 6 | MINOR | Lemma 2 hypotheses; "tested squares"; 17.8 not 17.9; 34 of 38 𝔊*. | All fixed. |
