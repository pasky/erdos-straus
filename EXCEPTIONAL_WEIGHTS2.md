# EXCEPTIONAL_WEIGHTS2 — CRT alignment and the shift-uniform count (task O90)

Status: **O90, in progress (author draft, not yet reviewed).** Labels follow `DISCOVERIES.md`.
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
