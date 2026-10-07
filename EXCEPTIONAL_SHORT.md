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
