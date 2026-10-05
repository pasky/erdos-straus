# Hostile review R48a of POINTWISE_OMEGA13.md (reviewer 1 of 2: quarantine machinery)

Reviewer branch: side-agent/review-omega13a (merged side-agent/beyond-fifth @ 4539218).
Scope: Lemma 1.1, Lemma 3.1, Lemma 3.2, the random-vs-deterministic logic of Thm 3.4.
Lemma 3.3 (NT inputs, Ξ) is reviewer 2's scope; only touched where it interfaces.
Scripts: `scripts/review_o13a_*.py` (from scratch; author's scripts not reused).

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### Lemma 1.1 (β-weighted LLL) — SOUND

*Re-derivation.* Dependency graph = "supports meet" (valid on a product space: E is
mutually independent of the σ-algebra of the coordinates outside supp E). For E'∼E
(including E'=E) we have `Σ_{E'∼E}x_{E'} ≤ Σ_{ℓ∈supp E}w̃_ℓ ≤ s(E)η`; each
`x_{E'} ≤ η ≤ 1/4` (needs `logβ≤1/3`, which is assumed), and
`−log(1−x)≤(4/3)x` on `[0,1/4]`. So `∏_{E'∼E}(1−x_{E'}) ≥ β^{−s(E)}` and
`P(E)=x_Eβ^{−s(E)}` gives the asymmetric-LLL hypothesis (even with E itself in the
product, which is stronger than needed). Both conclusions are the standard
Erdős–Lovász/Spencer ones. Checked the inequalities line by line; no hidden
hypothesis other than finiteness of the family (true: M≤T) and `supp E≠∅` (events
with empty support must be dead — this is exactly what Lemma 3.1 supplies in §3).

*Brute force* (`scripts/review_o13a_lll.py`, seeds 1,2): random product spaces with
3–6 coordinates, non-uniform marginals, events with 1–3-coordinate supports and 1–3
accepted tuples, β∈(e^{0.02},e^{1/3}); plus adversarial hill-climbing that adds or
replaces events while keeping (1.1), maximising the violation ratio. 4 844 valid
systems, exact enumeration:
`max exp(−(4/3)Σx)/P(∩Ē) = 0.99889` and `max P(E|∩_𝒮F̄)/x_E = 0.942` (claims ≤1).
No violation. (Ratios near 1 come from near-empty systems, where both sides →1.)

### Lemma 3.1 (event classes are Jacobi non-residues) — SOUND

*Re-derivation.* (a) `gcd(M,4A)=1` since `M=4A−1`; D|A² so ℓ∤2D; `−4D=−d·(2·□)²`.
(b) `(−d|M)=(−1|M)(d|M)=−(d|M)`; each p|d has `v_p(D)` odd ⇒ p|A ⇒ `M≡−1 (p)`;
odd p: reciprocity with `(M−1)/2` odd gives `(p|M)=(−1|p)(−1)^{(p−1)/2}=1`;
p=2: 2|A ⇒ M≡7 (8) ⇒ `(2|M)=1`. Correct, incl. prime powers (Jacobi is
multiplicative in M, `(r|ℓ^v)=(r|ℓ)^v=1` for r a square mod ℓ) and ℓ=3 (squares
mod 3 = {1}; 3|M forces 3∤A, nothing special). The "more generally" clause is also
right: if `a_ℓ≥1` at every ℓ|M (even with `v_ℓ(M)>a_ℓ`), consistency would need
`−4D≡r` to be a square mod every ℓ|M, giving `(−4D|M)=+1`. ℓ=2 is irrelevant (M odd).

*Brute force* (`scripts/review_o13a_jacobi.py 3000 100000`), three independent checks:
1. Direct enumeration of `x² mod M` (no symbols): for all 15 754 atoms with
   M≤3000, `−4D` is never a square mod M; (a) via Euler's criterion: 0 failures.
2. Own Jacobi implementation: `(−4D|M)=−1` on all 1 070 466 atoms with M≤10⁵.
3. Square-class states: 3 000 random `Q=∏ℓ^{a_ℓ}` over ℓ≤23 with `a_ℓ≤4`, r a random
   CRT of unit squares mod `ℓ^{a_ℓ}`; 462 418 (atom with M|Q, state) pairs; fired: 0.

*Consequence check (the logic "random square classes never fire").* Under the
process, at every ℓ with `a_ℓ≥1` the fibre is a class mod `ℓ^{a_ℓ}` that is a square
(a=0 step picks a square mod ℓ; later lifts of a unit square mod ℓ are squares mod
ℓ^{a}, ℓ odd). So the realised r is a unit square mod every odd prime of Q, and every
atom with `rad(M)|Q` is dead. An event with `supp_end E=∅` is exactly such an atom
(`a_ℓ≥v_ℓ(M)≥1` at all ℓ|M). Hence no surviving event has empty support, which is
the only use made in Thm 3.4 / Lemma 1.1. SOUND.

### Lemma 3.2 (bookkeeping for the square-class process) — SOUND (two MINOR wording defects)

*Re-derivation of (a).* a=0 step at ℓ|M: before, the ℓ-factor of p(E) is
`1/φ(ℓ^v)`; after revealing a uniform square s mod ℓ it is `1[s≡−4D]/ℓ^{v−1}`;
`P(s≡−4D)=2/(ℓ−1)·1[(−4D|ℓ)=1]`, so `E[p_new]=(1+(−d|ℓ))p` by Lemma 3.1(a), and
`2^{u}` halves: `E[p2^{u}]_{new}≤p2^{u}`. a≥1: uniform among the ℓ lifts, exact
martingale (all lifts of a unit square are squares, ℓ odd). ℓ=3: the square class
is forced (only {1}); the identity still holds deterministically. Correct. Since
the inequality holds *per event*, any adapted step-selection rule is allowed.

*(b),(c).* `logℓ·1[τ<∞]≤(logℓ/η)w̃_{ℓ,a}(τ)` at the step time; `β^{s_i}≤β^{ω}2^{u_i}`;
`G^{(ℓ,a)}` is a nonnegative supermartingale (φ=1[v_ℓ(M)≥a+1]β^{ω}); the process has
≤`Σ_{ℓ≤Y}f_ℓ` steps, so `E[G(τ∧N)]≤G(0)` and `G(τ)1[τ<∞]≤G(τ∧N)`. Summing over
`(ℓ,a)` with `ℓ≤Y, a<v_ℓ(M)` gives `log M_Y`. `p_0=1/φ(M)` (M odd, fibre mod 8
irrelevant), `u_0=ω_Y(M)` (start Q=8, all odd a_ℓ=0). Correct.

*(d).* I re-derived the pair potential case by case. At a step at level a at ℓ'
that both F,F' constrain with a<j: each p is multiplied by `N·1[match]`, where N is
the number of classes of the *current fibre* at that level (`N=ℓ'−1` if a=0, `N=ℓ'`
if a≥1); ρ (classes mod `ℓ'^j`) is divided by N; so `Π→N·1[match]Π`, mean Π (a≥1) or
`2·1[(−4D|ℓ')=1]Π` (a=0), absorbed by the factor 1/4 from both u's. a=j<min(v,v'):
disagreement ⇒ Π→0. Only one constrains ⇒ a≥min(v,v')≥j ⇒ ρ=1, reduces to (a).
Shared ℓ'>Y never stepped ⇒ ρ constant ≥1. `pp'≤Π2^{−u−u'}` since R≥1. Start:
`R_0=∏φ(ℓ'^{j})≤φ(gcd(M_F,M_{F'}))`, and `gcd(M/ℓ^{v},M'/ℓ^{v'})=gcd(M,M')/ℓ^{min v}`,
so `B_2` is exactly what comes out. `w̃_ℓ(end)²≤(Σβ^{ω}p)²` and Chebyshev. Correct.

*Simulation* (`scripts/review_o13a_process.py`, from scratch; general events
`{ℓ:(v,t mod ℓ^v)}`; reachable states by random walks; **every** admissible step):
* `T=300,Y=13,β=1.3`: (a) one-step `max E[p2^u]_{new}/(p2^u)=1.000000` over 43 220
  (event,state,step); (d) one-step `max E[Π]_{new}/Π=1.000000` over 46 805, incl.
  synthetic partially-agreeing pairs; `max pp'/(Π2^{−u−u'})=1`.
* `T=1200,Y=23,β=1.39`: same, 89 463 / 94 286 checks, max exactly 1.
* Power check: with `ρ≡1` (env `O13A_NORHO=1`) the (d) check fails with ratio 6, so
  the test does detect a missing correction.
* Monte Carlo of the full process (stop rule `w̃_ℓ>η` ⇒ step; T=1200, 300 runs):
  `E[log Q_end]=24.4 ≤ 1290.8`, `E[res mass]=13.8 ≤ S_H^β=86.0`,
  `E[w̃_ℓ(end)²]` for ℓ=29,31,37,41: `0.32,0.94,0.24,0.10` vs `B_2=9.0,11.0,5.7,11.6`.
  All bounds hold (with large slack, as expected from `2^{ω_Y}` and Cauchy–Schwarz).

Defects (MINOR):
* **m1 (§3, Lemma 3.2(d) proof, third bullet).** "both are multiplied by the same
  `F_r·1[match]` (F_r = number of classes revealed among)": at an a=0 step the classes
  revealed among number `(ℓ'−1)/2`, but the factor is `ℓ'−1` (the number of fibre
  classes mod ℓ'); with the literal F_r the stated mean `(1+(−d|ℓ'))Π` would be wrong
  by 2. *Repair:* "multiplied by `N·1[match]`, N = number of classes of the current
  fibre at this level (ℓ'−1 if a=0, ℓ' if a≥1)".
* **m2 (§3, "R1 fix" remark).** My simulation (env `O13A_BUGGY=1`) shows that ρ at
  depth `min(v,v')` is *also* a supermartingale potential (the disagreement step kills
  Π), and both start values are ≤`φ(gcd)`. So the depth-j choice is merely tighter;
  the stated reason ("would gain a factor F_r at low-level steps") does not seem to
  occur. Harmless; suggest rewording or dropping the justification.

### Thm 3.4 logic: random quarantine vs. deterministic δ*(T) — SOUND (modulo Lemma 3.3, reviewer 2)

*The question.* The process is random, but the conclusion is about the fixed number
δ*(T). The proof does not bound an expectation of δ*. It uses three probability
bounds under the process law:
`P(log Q_end>4E[log Q_end])≤1/4`, `P(S_res>4E[S_res])≤1/4`, and
`P(∃ℓ>Y: w̃_ℓ>η)≤1/4`. Their union has probability ≤3/4<1, so a **deterministic**
reachable `(Q,r)` avoids all three. That realisation is a legitimate fibre of Haar
measure, with `P_H(n≡r (Q))=1/φ(Q)` and the coordinates independent on it (CRT). On
it:
* (1.1) holds at ℓ≤Y because the process stopped there (or `a_ℓ=f_ℓ`, in which case
  there is no coordinate);
* (1.1) holds at ℓ>Y by the choice of realisation;
* no live event has empty support (Lemma 3.1).

So Lemma 1.1 applies inside the fibre, and `δ*≥φ(Q)^{−1}exp(−(4/3)S_res)` is a
deterministic inequality. This is a valid probabilistic-method existence argument.
Repeated classes `(M,−4D mod M)` counted twice only weaken the bound. *Verdict:*
SOUND, given Lemma 3.3. I did not check Lemma 3.3 (A)/(B) in depth; that is
reviewer 2's scope.

Defects (MINOR):
* **m3 (normalisation of δ*; Thm 3.4 statement).** O13 defines δ* on all of `Ẑ^×`.
  POINTWISE_HAAR §0 normalises it inside `n≡1 (24)`. The two differ by exactly a
  factor 2: the atom `M=3, D=1` kills `n≡2 (3)`, and mod 8 is irrelevant. This is
  harmless for the exponent. *Repair:* say so, or start the process at `Q=24, r≡1`.
  That start is a forced `a=0` step at ℓ=3, which is a valid supermartingale step:
  the only square mod 3 is 1.
* **m4 (Cor 3.5 / I3: Mordell-hardness).** I3 claims "p is Mordell-hard because r
  is a square mod 840". The process starts at `Q=8` and steps 3, 5 and 7 only if
  `w̃>η`, so a priori `r` need not be defined mod 105.
  * In practice the low-M atoms make `w̃_3, w̃_5, w̃_7` large.
  * Still, nothing in the statement forces it.
  * *Repair:* start at `Q=840` with r a uniformly random square class mod 105
    (three forced `a=0` steps). These steps keep the supermartingales. They cost
    `log 105` in `log Q` and no change to (b)–(d).
* **m5 (apparent circularity in `Y=𝓛^{C_0+4}`).** Ξ contains `H=β^{ω}2^{ω_Y}` and so
  depends on Y. The choice of Y is legitimate only because Ξ's bound `𝓛^{C_0}` is
  uniform in Y, via `2^{ω_Y}≤2^{ω}`. The proof of Lemma 3.3(B) uses this implicitly
  ("f(p)=O(1)"). *Repair:* state the uniformity in Y explicitly.

