# EXCEPTIONAL_SHORT — exceptional sets in short intervals and progressions (task O88)

Status labels as in DISCOVERIES.md. "The note" = `paper/es-threequarter-note.tex`
(INTERNALLY PROVED, blind-audited). Everything below labelled PROVED is proved
*relative to the note's Theorem `thm:assembly` (§8) and Lemma `lem:identity` (§2)* (labels cited, not numbers),
i.e. it inherits the note's internal-only status.

Notation. `n` is *exceptional* if 4/n = 1/a+1/b+1/c has no solution in positive
integers. For an interval `I` put `E(I) = #{n ∈ I : n exceptional}`,
`E_pr(I)` the same over primes.

## 0. Inventory of the note's moduli and counting steps (step 1 of the brief)

Parameters: `t = log X`, `K = ⌊X^κ⌋` (κ < 1/240 fixed), `y = B t^3`,
`r ≍ D_B t^3` (even).

| object | modulus / level | size |
|---|---|---|
| atom `E_A` (A=(k,ℓ,u,v)) | `kℓ`, k ≤ K, ℓ ∈ (X^{1/2},X] prime | ≤ KX = e^{(1+κ)t} |
| fibre variable c | `L_K = lcm{k ≤ K, k≡1(4)}` | e^{O(K)} — **never expanded** (void lemma reveals c inside the exact CRT expectation only) |
| selector `S_y = 1_{(n,P_y)=1}` | `d | P_y`, 2^{π(y)} terms | P_y = e^{O(t^3)} |
| Bonferroni term (j ≤ r atoms + selector) | `q = lcm(d, k_1ℓ_1, …)` | `log q_max ≤ C t^3 + r(1+κ)t = O(t^4)` |
| total coefficient mass | `T_abs ≤ 2^{π(y)} Σ_{j≤r} C(|A_X|, j)` | `log T_abs ≤ C_L t^4` |
| BV / Brun–Titchmarsh / Shiu | used at scale X only, to *construct* atom mass | — |

Counting over `[1,N]` occurs in exactly one place: (eq:transfer) of
thm:assembly, `Σ_{n≤N} ν_X(n) = N E_CRT ν_X + O(T_abs)`, using only
`#{n ≤ N : n ≡ a (q)} = N/q + O(1)` (error ≤ 1, no primality).
Nothing in that step uses that the interval starts at 1. The only other
`[1,N]`-specific step is the integer transfer (Rankin over the semigroup of
exceptional primes, note §9 `sec:all`), which is **not** local and is replaced below.
The prime-counting inputs (BV etc.) live at scale X = e^t ≤ e^{O((log N)^{1/4})}
and never at scale N.

Key structural facts used below (all from the note):
* (F1) `ν_X = S_y · Q_r(H_X) ≥ 0` is a finite signed combination of
  congruence classes, independent of N, with `E_CRT ν_X ≤ e^{-c_a t^3}`
  and ledger (eq:ledger) for all X ≥ X_a.
* (F2) lem:identity holds for **every** positive integer n in an atom class,
  so `H_X(m) = 0` for every exceptional m ≥ 1; hence `ν_X(m) = 1` for every
  exceptional m with `(m, P_y) = 1` (Q_r(0) = 1).

## 1. Integers in arbitrary intervals

**Lemma 1.1 (local mean of the majorant; PROVED rel. note).** Let `X ≥ X_a`
(thm:assembly), `Q ≥ 1`, `β ∈ Z`, and let `I = (z, z+H]` be any real interval
(`z ∈ R`, `H > 0`). Then
`Σ_{n ∈ I, n ≡ β (Q)} ν_X(n) ≤ H·e^{-c_a t^3} + e^{C_L t^4}.`

*Proof.* Expand `ν_X` into its plain congruence terms `±1_{a (mod q)}`
(thm:assembly, total absolute coefficient sum `T_abs ≤ e^{C_L t^4}`).
For each term, `{n ≡ a (q)} ∩ {n ≡ β (Q)}` is empty or one class mod
`lcm(q,Q)`, and `#{n ∈ I : n ≡ a' (lcm)} = H/lcm + θ`, `|θ| ≤ 1`, for every
real interval of length H. Summing with signs,
`Σ = H·E[ν_X·1_{β (Q)}] + O_{≤1}(T_abs)`, the expectation being the uniform
average over `Z/lcm(𝓜, Q)` (𝓜 as in eq:space; ν_X is 𝓜-periodic). Since
`ν_X ≥ 0` pointwise, `E[ν_X 1_{β(Q)}] ≤ E_CRT ν_X ≤ e^{-c_a t^3}` (eq:majorant). ∎

This is literally eq:transfer with `[1,N]` replaced by I; no step of the note
uses the left endpoint. (The case Q = 1 is the one needed now.)

**Lemma 1.2 (smooth-part decomposition; PROVED).** Write each `n ≥ 1` as
`n = d·m` with `P⁺(d) ≤ y` and `(m, P_y) = 1` (d = y-smooth part).
(a) If n is exceptional, so is m (the empty case m = 1 included: 1 is
exceptional). Indeed if m > 1 were representable, `4/m = Σ1/x_i` gives
`4/n = Σ 1/(d x_i)`. (This is the divisor-closure used in note §9.)
(b) If `d > D_0 ≥ 1` then d has a divisor `d' ∈ (D_0, yD_0]` with
`P⁺(d') ≤ y` (strip prime factors ≤ y one at a time; take the last divisor
in the chain that exceeds D_0).
(c) Rankin: `Σ_{d' > D_0, P⁺(d') ≤ y} 1/d' ≤ D_0^{-1/2} Π_{p≤y}(1-p^{-1/2})^{-1}
≤ D_0^{-1/2} e^{4√y}`, using `-log(1-u) ≤ 2u` for `0 ≤ u ≤ 2^{-1/2}` and
`Σ_{p≤y} p^{-1/2} ≤ 2√y`.

**Theorem 1 (short-interval 3/4 bound; PROVED rel. note).** There are
absolute constants `c, C > 0` such that for every real `z` and every `H ≥ 2`,
`E((z, z+H]) ≤ C·H·exp(−c (log H)^{3/4}).`
In particular, for `x ≥ 3` and `x^θ ≤ H ≤ x` (`0 < θ ≤ 1`),
`E((x,x+H]) ≤ C·H·exp(−c θ^{3/4} (log x)^{3/4})`, and for
`H ≥ exp((log x)^λ)` the saving is `exp(−c (log x)^{3λ/4})`.

*Proof.* Let `I = (z, z+H]`, X ≥ X_a to be chosen, `D_0 = e^{2c_a t^3}`.
Split exceptional `n ∈ I` by their y-smooth part d.
(i) `d > D_0`: by 1.2(b),(c) at most
`Σ_{d' ∈ (D_0,yD_0]} (H/d' + 1) ≤ H e^{-c_a t^3 + 4√B t^{3/2}} + yD_0`.
(ii) `d ≤ D_0`: m lies in `I/d = (z/d,(z+H)/d]` (length H/d), m is
exceptional and coprime to P_y, so `ν_X(m) = 1` by (F2). By Lemma 1.1 (Q=1),
the count is at most `Σ_{d ≤ D_0} (H/d·e^{-c_a t^3} + e^{C_L t^4})
≤ H(1 + 2c_a t^3) e^{-c_a t^3} + e^{(2c_a + C_L) t^4}` (t ≥ 1).
Altogether `E(I) ≤ C_1 H e^{-c_a t^3/2} + e^{C_2 t^4}` for X ≥ X_1, with
C_1, C_2 depending only on the note's fixed constants. Take
`t = (log H / (2C_2))^{1/4}`; then `e^{C_2 t^4} = H^{1/2}` and the bound is
`≪ H exp(−c (log H)^{3/4})`. If this t is below `log X_1`, H is bounded and
the trivial bound `E(I) ≤ H + 1` suffices after enlarging C. ∎

Remarks. (1) Theorem 1 contains the note's theorem (I = (0,N]) and gives it
*without* the Rankin/semigroup step of note §9: the transfer to all
denominators is now local. (2) The majorant depends only on H, not on the
location z: the bound is uniform in z, with no requirement H ≤ z.
(3) The prime analogue is automatic in the relevant range, see §3.
