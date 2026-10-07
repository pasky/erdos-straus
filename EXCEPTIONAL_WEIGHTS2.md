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
