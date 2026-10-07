# EXCEPTIONAL_WEIGHTS2 — CRT alignment and the shift-uniform count (task O90)

Status: **O90 checkpoint (author draft, not yet reviewed). Verdict §7: (W) open; the CRT-alignment plan provably fails as specified; report `reviews/agent-reports/AGENT_REPORT_O90.md`.** Labels follow `DISCOVERIES.md`.
PROVED means proved here, internal checks only. No θ > 3/4 is claimed. ES is not solved.

Notation of `EXCEPTIONAL_WEIGHTS.md` (W1). 𝔊 a finite family of residue classes, 𝒜 = 𝒜(𝔊)
its avoider set, `M_𝔊(N) = max_{t∈ℤ} #(𝒜 ∩ (t, t+N])`, `count_t := #(𝒜∩(t,t+N])`.
ℛ(M) = {−u/v mod M : gcd(u,v)=1, 4uv | M+1} = {−4D mod M : D | A²}, A = (M+1)/4
(LS7 Lemma 1.1). For a prime ℓ ≡ 3 (4) write `F_ℓ = ℛ(ℓ)`, `p_ℓ = |F_ℓ|/ℓ`.
(W) = (W_{𝔉_A}) of W1 §5.

## 1. Reduction to the maximal family

**Lemma 1.1 (PROVED, trivial).** If 𝔊 ⊆ 𝔊′ then 𝒜(𝔊′) ⊆ 𝒜(𝔊) and `M_{𝔊′}(N) ≤ M_𝔊(N)`.
𝔉_A is closed under finite unions (it is the class of *all* finite families of admissible
classes with moduli ≤ N^A), and for fixed N there are finitely many such classes. Let
𝔊_max(N) be the union of all of them. Then

    min_{𝔊∈𝔉_A} M_𝔊(N) = M_{𝔊_max(N)}(N),

so (W) ⟺ `M_{𝔊_max(N)}(N) ≥ N e^{−C(log N)^{3/4}}` (N ≥ N₀). ∎

So (W) is one concrete question about one avoider set: is there a window of length N in
which a fraction `e^{−C(log N)^{3/4}}` of the integers lies in **no** ℛ(M)-, Case-A or
selector class of modulus ≤ N^A? Every subfamily (e.g. the prime slices `F_ℓ`, ℓ ≤ N^A)
has M at least as large, so a *refutation* may use any subfamily, while a *proof* must
handle 𝔊_max.

*Consequence for refutations (PROVED, from W1 Prop 5.1(a′)).* If 𝔊 ⊇ 𝔊_X then
`E_pr(N) ≤ K + y + M_𝔊(N)`. Refuting (W) with a family containing 𝔊_X, i.e. proving
`M_𝔊(N) ≤ Ne^{−(log N)^θ}` with θ > 3/4, would prove θ > 3/4 for E_pr. A refutation
therefore needs an argument at least as strong as a new exceptional-set theorem.

## 2. What every window must pay (forced costs)

**Lemma 2.1 (period forcing; PROVED).** Let 𝔊′ have period Q′ and avoider density δ′.
For every t, `⌊N/Q′⌋Q′δ′ ≤ #(𝒜(𝔊′)∩(t,t+N]) ≤ ⌈N/Q′⌉Q′δ′`.

*Proof.* (t, t+N] contains ⌊N/Q′⌋ and is contained in ⌈N/Q′⌉ consecutive full periods. ∎

So a subfamily costs its density in **every** window only if its period is ≤ N/k (then the
count is within a factor 1 ± 1/k of Nδ′). Classes with a *single* modulus m ≤ N hit
every window ≈ N/m times, but the *joint* count of several classes is forced only up to
the lcm of their moduli. The brief's heuristic "moduli ≤ N cost their density" is
therefore not a valid lower bound mechanism, and not a valid upper bound either: see §3.

**Lemma 2.2 (forced mass is tiny; PROVED).** Let P′ be any set of primes ℓ ≡ 3 (4) with
`Π_{ℓ∈P′} ℓ ≤ N`. Then `Σ_{ℓ∈P′} p_ℓ ≤ (log N)^{o(1)}`.

*Proof.* `|F_ℓ| ≤ τ(A²) ≤ ℓ^{o(1)}`, so `p_ℓ ≤ ℓ^{−1+o(1)}`. Among sets with
`Σ log ℓ ≤ log N`, `Σ ℓ^{−1+ε}` is maximised (exchange argument: replace a prime by a
smaller unused one) by an initial segment of primes ℓ ≤ y with `θ(y) ≤ log N`, i.e.
y ≪ log N; then `Σ_{ℓ≤y} ℓ^{−1+ε} ≪ y^{ε} ≤ (log N)^{ε}` (any ε > 0). ∎

The same holds for any subfamily with lcm ≤ N (composite moduli, |ℛ(M)| = M^{o(1)}). So
period forcing never costs more than `(log N)^{o(1)}`, far below `(log N)^{3/4}`. The
only known shift-uniform *upper* bounds for M are sieve bounds (large sieve, the 3/4
note), which are position-blind (W1 §5).

## 3. Step (2): the density is far below the 3/4 scale — and irrelevant

**Proposition 3.1 (PROVED; ineffective constant via Bombieri–Vinogradov).** Let 𝔊 contain
the prime slices `F_ℓ`, ℓ ≡ 3 (4), ℓ ≤ Y. Then

    dens 𝒜(𝔊) ≤ Π_{ℓ≤Y, ℓ≡3(4)} (1 − p_ℓ) ≤ exp(−c (log Y)²)      (Y ≥ Y₀).

*Proof.* The prime slices are CRT-independent, so their avoider density is the product, and
𝒜(𝔊) is a subset. For the mass: with A = (ℓ+1)/4 the classes `−4D`, D | A², D ≤ A are
distinct mod ℓ (0 < 4D < ℓ+1), and `#{D | A² : D ≤ A} = (τ(A²)+1)/2`. Coprime pairs
(u,v) with uv = q | A give distinct D = u²·A/q (LS7 Lemma 1.1), and there are 2^{ω(q)} of
them. So for x ≥ x₀,

    Σ_{x<ℓ≤2x, ℓ≡3(4)} |F_ℓ| ≥ ½ Σ_{q ≤ x^{1/3}} 2^{ω(q)} (π(2x; 4q, −1) − π(x; 4q, −1))
                          ≥ c₁ (x/log x) Σ_{q≤x^{1/3}} 2^{ω(q)}/φ(4q) ≥ c₂ x log x,

by Bombieri–Vinogradov with the weight 2^{ω(q)} (Cauchy–Schwarz against
`Σ_{q≤x^{1/3}} 4^{ω(q)} x/φ(q) ≪ x(log x)^4` and the BV saving `x(log x)^{−B}`; the main
term uses `Σ_{q≤z} 2^{ω(q)}/φ(q) ≍ (log z)²`; the pairs (q, D) are counted once each
since D determines (u,v) for fixed A). Dividing by ℓ ≤ 2x and summing dyadically,
`Σ_{ℓ≤Y} p_ℓ ≥ c₃ Σ_{k ≤ log₂Y} k ≥ c(log Y)²`. ∎

**Corollary 3.2 (answer to step (2) of the brief).** Already the prime slices with
`ℓ ≤ Y = exp((log N)^{3/8+ε})` (ε > 0) push the avoider density below
`exp(−c(log N)^{3/4+2ε})`; with ℓ ≤ N it is `≤ exp(−c(log N)²)`. (With all composite moduli
the mass is ≍ (log Y)³ by Elsholtz–Tao, which would suggest Y = exp((log N)^{1/4+ε});
the union of composite classes is not a product, so only the prime-slice statement is
claimed.) So: **yes, moduli between `exp((log N)^{3/8+ε})` and N push the density far
below the 3/4 scale.**

**But this does not refute (W).** `M(N) ≥ N·dens` (average over t), so the density is a
*lower* bound mechanism only, and Lemma 2.1/2.2 show the window maximum is not forced to
pay it. Concretely, for the prime-slice family 𝔊_ℛ with ℓ ≤ N^A, W1 Prop 5.1(d) gives
`M(N) ≥ exp(c(log N)^{1/3})`, while `N·dens ≤ N exp(−c(log N)²) < 1`: the maximum over
shifts beats the density by more than any power of N. The brief's splitting "moduli
≤ N cost their density, moduli > N are moved away by CRT" thus **fails in both
directions**: moduli ≤ N need not cost their density in the best window (they cost it only
on average), and if they did, (W) would be false by Cor 3.2.

So the whole of (W) sits in the *correlation* between the translates `t mod ℓ` of the
medium moduli `exp((log N)^{c}) < ℓ ≲ N`.

## 4. Step (1): random CRT shifts cannot prove (W)

The brief's plan: fix t modulo the small-moduli period and take t random otherwise, then
bound the expected loss from the larger moduli (second moment / Janson). The expectation
is computed exactly by CRT and is far too small.

**Proposition 4.1 (first-moment obstruction; PROVED).** Let 𝔊 ⊇ {F_ℓ : ℓ ∈ L} (L a set
of primes ≡ 3 (4)) and let t be random with `(t mod ℓ)_{ℓ∈L}` uniform, independent of each
other and of `t mod Q_rest` (Q_rest = the part of the period of 𝔊 coprime to Π_L ℓ;
the classes with moduli divisible by some ℓ ∈ L are simply dropped, which only increases
the count). Then

    E count_t ≤ N · Π_{ℓ∈L}(1 − p_ℓ).

*Proof.* For each j ≤ N, the events {t + j ∉ F_ℓ (mod ℓ)}, ℓ ∈ L, are independent of
each other and of t mod Q_rest, each of probability 1 − p_ℓ. ∎

**Corollary 4.2.** Any proof of (W) by "choose t mod (small period) well, then average"
must leave t uniform only on a set L of primes with `Σ_{ℓ∈L} p_ℓ ≤ C(log N)^{3/4}`.
By Prop 3.1 the prime-slice mass in `(Y, N]` is ≍ (log N)² − (log Y)², so for
`Y ≤ N^{1−ε}` the translates of essentially all medium primes ℓ ∈ (exp((log N)^{3/8}), N^{1−ε}]
must be chosen **non-uniformly, jointly**. In particular the planned estimate "expected
loss for random t restricted to a good class mod the small-moduli period" is
`≥ (1 − e^{−c(log N)²})` of the window for ℓ ≤ N alone: step (1) as specified **cannot**
succeed, with or without second-moment/Janson refinements (they control the variance
around this mean, while (W) needs the maximum to exceed the mean by a factor
`exp(c(log N)²)`).

**Proposition 4.3 (size-biasing; PROVED).** For any law of t, `M(N) ≥ E[count²]/E[count]`
(since count ≤ M). For t uniform mod the full period this equals

    Σ_{|h|<N} (1 − |h|/N)·r(h),      r(h) = dens(𝒜 ∩ (𝒜 − h)) / dens 𝒜,

and for the prime-slice family (exact CRT)

    r(h) = Π_ℓ (1 − |F_ℓ \ (F_ℓ − h)| / (ℓ − |F_ℓ|))         (h mod ℓ).        (4.1)

The factor at ℓ is 1 when ℓ | h and otherwise `1 − (|F_ℓ| − |F_ℓ ∩ (F_ℓ−h)|)/(ℓ−|F_ℓ|)`.
*Assessment (not proved):* for fixed h ≠ 0 the self-overlap mass
`Σ_ℓ |F_ℓ ∩ (F_ℓ − h)|/ℓ` is bounded by the number of solutions of
`(u+hv)v′ = u′v` with both uv, u′v′ | (ℓ+1)/4, a convergent sum over (u,v,u′,v′) times
`log log`, i.e. O_h((log log N)^{O(1)}); h has ≤ log N prime factors. So
`r(h) = dens · e^{O((log log N)^{O(1)})}` and the size-biased bound is
`N·dens·e^{o(log N)}`: pair correlations do not help either. Higher moments
`(E count^k)^{1/k} → M(N)` (k → ∞) recover M exactly, but only through the
k-point structure of §5.

## 5. Exact reformulation: a growing-dimension Hensley–Richards problem

**Lemma 5.1 (PROVED).** For the prime-slice family 𝔊 = {F_ℓ : ℓ ∈ P} (P finite),

    M_𝔊(N) = max{ |H| : H ⊆ [1,N], H is F-admissible },

where H is *F-admissible* if for every ℓ ∈ P some residue c has `(c + F_ℓ) ∩ H ≡ ∅ (mod ℓ)`,
i.e. `H − F_ℓ ≠ ℤ/ℓ`. Primes with `ℓ ≥ (N+1)|F_ℓ|` impose nothing (W1 Prop 5.1(b)).

*Proof.* If H ⊆ 𝒜 − t then c = −t works for every ℓ. Conversely choose t ≡ −c_ℓ (mod ℓ)
by CRT; then H + t ⊆ 𝒜. ∎

(For composite moduli the residues c_M must be CRT-consistent; admissibility becomes a joint
condition, and Lemma 5.1 is a lower bound for the subfamily of prime slices only.)

For `F_ℓ = {0}` (all ℓ) this is the Hensley–Richards function ρ*(N), the largest admissible
set in an interval of length N; there `π(N) ≲ ρ*(N) ≤ 2N/log N` (primes in (N, 2N] are
admissible; Montgomery–Vaughan large sieve). The analogue for fixed dimension:

**Proposition 5.2 (fixed dimension: max ≍ density; PROVED).** If `|F_ℓ| = κ_ℓ ≤ κ` for all ℓ
and Σ_{ℓ≤x} κ_ℓ/ℓ = κ log log x + O(1), then `N·Π_{ℓ≤(N+1)κ}(1−p_ℓ) ≤ M(N) ≪_κ N(log N)^{−κ}`
(where defined), and the lower bound is ≍_κ N(log N)^{−κ}.

*Proof.* Lower: W1 Prop 5.1(b) and Mertens. Upper: the large sieve with Q = √N, whose
denominator is `≫_κ (log N)^κ`. ∎

So in bounded dimension random translates are optimal up to constants: the medium primes
`(N^{1/β}, N]` cost only `Π(1−κ_ℓ/ℓ) ≍ β^{−κ}`. In the ES system the dimension grows
(`Σ_{ℓ≤x} p_ℓ ≍ (log x)²` over primes, ≍ (log x)³ over all moduli), and the medium primes
cost `exp(−c(log N)²)` under random translates (Prop 4.1), against the large-sieve limit
`exp(−c(log N)^{2/3})` (primes) / `exp(−c(log N)^{3/4})` (all moduli). **(W) is precisely the
question whether the large sieve of growing dimension is attained by an actual
admissible set of integers (CRT translates), not just by a pseudo-distribution on the
torus.** (The KARY/LS sieve-limit constructions are pseudo-distributions; W1 §5.)

**Proposition 5.3 (quadratic alignment caps at √(N log N); PROVED).** All classes of every
ℛ(ℓ) are quadratic non-residues mod ℓ (for 4uv | ℓ+1, every prime q | uv has ℓ ≡ −1 (4q),
so (q|ℓ) = 1, (2|ℓ)=1 if 2 | uv, and (−1|ℓ) = −1). Hence any H with
`H − c_ℓ ⊆ {squares mod ℓ}` for all ℓ ∈ P is F-admissible ("quadratic alignment": the
mechanism that makes perfect squares avoiders at t = 0). But such H, for all primes
ℓ ≡ 3 (4) up to √N, satisfies `|H| ≪ √(N log N)`.

*Proof.* Large sieve with `ω(ℓ) = (ℓ−1)/2` excluded classes for ℓ ≡ 3 (4), ℓ ≤ √N:
`|H| ≤ (N + Q²)/L`, `L ≥ Σ_{q≤√N} μ²(q)Π_{ℓ|q}ω/(ℓ−ω) ≥ #{q ≤ √N squarefree, all ℓ | q are
≡ 3 (4)} ≫ √N/√(log N)` (Landau). ∎

So the one global structure that makes *all* ℛ-classes vanish simultaneously (residuosity)
is useless at the 3/4 scale: it caps at N^{1/2+o(1)}. A proof of (W) needs a structure
adapted to the small, sparse sets F_ℓ (size ℓ^{o(1)}), not to half the residues.

## 6. Numerical checks (EVIDENCE)

`scripts/weights2_checks.py` (primes ℓ ≡ 3 (4), ℓ ≤ 3·10⁶; F_ℓ = {−4D : D | A²}):
* every class of every ℛ(ℓ) is a quadratic non-residue (0 failures; Prop 5.3 premise, which
  is proved anyway);
* prime-slice mass `S(Y) = Σ_{ℓ≤Y} p_ℓ`: 2.86, 6.03, 10.50, 16.23, 23.17, 26.90 at
  Y = 10², …, 10⁶, 3·10⁶, i.e. `S(Y)/(log Y)² = 0.135 → 0.121`, slowly decreasing and
  consistent with Prop 3.1's ≍ (log Y)²;
* self-overlap mass `O_h(Y) = Σ_ℓ |F_ℓ ∩ (F_ℓ − h)|/ℓ` (h = 1, 2, 3, 6, 10): 0.6–1.0 at
  Y = 10², 1.8–2.9 at 3·10⁶, with decreasing increments per decade (O₁: +0.55, +0.49,
  +0.41, +0.35). It is a vanishing fraction of S(Y) (≈ 10% at 3·10⁶), consistent with the
  Assessment in Prop 4.3 that pair correlations recover only a factor `e^{O(O_h)}`.

The toy translate sieve of W1 §5.1 (N = 300, 1000) remains the only direct numerics for M;
N ≤ 10⁴ cannot separate exponents (log N ≤ 9.2, (log N)^{3/4} ≤ 5.3), so no new run was made.

## 7. Verdict for O90

**(W) is neither proved nor refuted.** What is established:

1. (W) ⟺ a lower bound for the single maximal family 𝔊_max(N) (Lemma 1.1). A refutation
   by a family containing 𝔊_X would itself be a θ > 3/4 exceptional-set theorem
   (via W1 Prop 5.1(a′)), so it cannot come cheaply; no contradiction with KARY3/LS3/LS4
   arises, since those caps concern w ≥ 1 certificates, not the shift-uniform count.
2. Step (2) of the brief: **yes**, the moduli between `exp((log N)^{3/8+ε})` and N push the
   avoider *density* below `e^{−(log N)^{3/4+2ε}}` — already the prime slices do
   (Prop 3.1, BV). This would refute (W) **only if** windows were forced to pay the density;
   they are not (Lemma 2.1–2.2: forcing reaches only subfamilies of period ≤ N, mass
   `(log N)^{o(1)}`), and indeed M(N) ≫ N·dens·N^{100} for the prime slices (Cor 3.2).
3. Step (1) of the brief **fails as specified**: random shifts restricted to a good class mod
   the small period give `E count ≤ N Π_L(1 − p_ℓ)` (Prop 4.1), i.e. a loss
   `e^{−c(log N)²}` from the medium primes; size-biasing/pair correlations recover only
   the self-overlap mass (Prop 4.3, Assessment + §6 EVIDENCE). A proof of (W) must choose
   the translates of essentially all primes in `(exp((log N)^{3/8}), N^{1−ε}]` jointly and
   non-uniformly (Cor 4.2).
4. The one global mechanism that kills all ℛ-classes at once (residuosity: every ℛ(ℓ) ⊆ QNR)
   caps at `√(N log N)` (Prop 5.3).
5. For prime slices, (W) is exactly a **growing-dimension Hensley–Richards problem**
   (Lemma 5.1): the largest F-admissible subset of an interval of length N. In bounded
   dimension the maximum is ≍ the density (Prop 5.2); in the ES dimension
   (`Σ_{ℓ≤x}p_ℓ ≍ (log x)²` over primes) the density is `e^{−c(log N)²}`, the large sieve
   bound `e^{−c(log N)^{2/3}}`, and (W) at the family's own exponent asks whether actual
   admissible sets attain the large-sieve limit (an inverse/attainment problem for the
   large sieve; the sieve-limit objects of KARY/LS are pseudo-distributions on the torus).

*Assessment.* Both directions look as hard as a new sieve theorem: refuting (W) needs a
shift-uniform count below the sieve limit (beyond every known method), proving it needs
an explicit construction of a structured window adapted to the sparse sets ℛ(ℓ), for
which no candidate structure is known (Prop 5.3 excludes residuosity, Prop 4.1 excludes
randomness). The per-frequency door therefore remains formally open but is **not a
practical route to θ > 3/4**: any escape through it requires proving an upper bound for
M_𝔊(N) below the sieve limit, i.e. solving the counting problem uniformly over all
CRT translates (W1 Cor 2.2: the escaping majorant *is* the LP optimum).

## Replay

```
cd scripts
ulimit -v 8000000
timeout 3000 uv run python weights2_checks.py 3000000 > ../data/weights2/checks.txt   # ~15 s, <200 MB, 1 core
```
