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

## 2. Progressions in short intervals

For `q ≥ 1`, `b ∈ Z` put `E(I; q, b) = #{n ∈ I : n ≡ b (q), n exceptional}`.
For a parameter `X` split `q = q_1 q_2`, `q_1 = ∏_{p^a ∥ q, p ≤ X} p^a`
(so every prime of q_2 exceeds X).

**Lemma 2.1 (independence of large-prime progressions; PROVED rel. note).**
If every prime factor of `Q` exceeds X then, in Lemma 1.1,
`E[ν_X 1_{β(Q)}] = E_CRT ν_X / Q`. More generally for `Q = Q_1Q_2` split as
above, `E[ν_X 1_{β(Q)}] ≤ E_CRT ν_X / Q_2`.
*Proof.* Every prime dividing 𝓜 (eq:space) is ≤ X (primes ≤ y, primes of
L_K ≤ K, and ℓ ≤ X). So `(Q_2, 𝓜) = 1`, and in `Z/𝓜Q_2 ≅ Z/𝓜 × Z/Q_2` the
function ν_X depends only on the first coordinate while `1_{β(Q_2)}` depends
only on the second. Drop `1_{β(Q_1)} ≤ 1` (ν_X ≥ 0). ∎

**Theorem 2 (short intervals in progressions; PROVED rel. note).** There are
absolute `c, c', C, α > 0` with the following property. Let I be any interval
of length H, `q ≥ 1`, `b ∈ Z`, `H/q ≥ 2`, and put
`X_q = exp(α (log(H/q))^{1/4})`, `q_1` = the `X_q`-smooth part of q. Then
`E(I; q, b) ≤ C·q_1·(H/q)·exp(−c (log(H/q))^{3/4})`.
In particular
(a) uniformly for all `b` and all `q ≤ exp(c' (log(H/q))^{3/4})`
(e.g. `q ≤ (log x)^A` with `H ≥ exp((log log x)^{4/3+ε})`, or
`q ≤ exp(c'θ^{3/4}(log x)^{3/4})` with `H ≥ x^θ`):
`E(I; q, b) ≪ (H/q) exp(−(c/2)(log(H/q))^{3/4})`;
(b) for every q all of whose prime factors exceed `X_q` (e.g. q prime,
`exp((log H)^{1/4+ε}) < q ≤ H^{1−δ}`): `E(I;q,b) ≪ (H/q) exp(−c(log(H/q))^{3/4})`.

*Proof.* As for Theorem 1, with `t = log X`. Since d is y-smooth and y < X,
`(d, q_2) = 1`. (i) `d > D_0`: n ∈ I with `d' | n`, `n ≡ b (q)` lie in one
class mod `lcm(d',q)` (or none), a multiple of `d'q_2`; count
`≤ H/(d'q_2) + 1`, total `≤ (H/q_2) e^{-c_a t^3 + 4√B t^{3/2}} + yD_0`.
(ii) `d ≤ D_0`: `n = dm ≡ b (q)` confines m to one class mod
`q/(d,q)`, whose X-rough part is q_2; Lemmas 1.1 and 2.1 give
`≤ (H/(d q_2)) e^{-c_a t^3} + e^{C_L t^4}`. Summing as before,
`E(I;q,b) ≤ C_1 (H/q_2) e^{-c_a t^3/2} + e^{C_2 t^4}`.
Choose `t^4 = log(H/q)/(2C_2)` (i.e. `α = (2C_2)^{-1/4}`), so the error is
`(H/q)^{1/2} ≤ (H/q)e^{-t^3}` for large H/q, and `H/q_2 = q_1·H/q`. Small H/q is
trivial. (a): `q_1 ≤ q ≤ e^{(c/2)(log(H/q))^{3/4}}`. (b): `q_1 = 1`. ∎

Remark 2.2 (what is lost for smooth moduli). The factor q_1 is the honest
cost of the crude bound `E[ν 1_{β(q_1)}] ≤ E ν`. Conditioning on n mod q_1
fixes n mod primes of L_K and of P_y, i.e. it fixes the multiplier-fibre
variable c of the void lemma (lem:void) *partially and adversarially*: the
void bound is an average over c, with bad fibres (large Z(c)) having
probability `e^{-ηy}` only. For q_1 = ∏_{y<p≤z} p and b ≡ 0 (q_1) the CRT
majorant is genuinely large in that progression. (Such progressions are not
dangerous for ES itself: all n ≡ 0 (q_1) inherit representability from any
representable p | q_1; see §4.) Extending (a) to all q ≤ H^{1−δ} needs a
fibre-uniform void bound, which the note's architecture does not provide —
OPEN, not attempted further here.

## 3. Primes in short intervals

**Corollary 3.1 (PROVED rel. note; no prime-distribution input at scale x).**
For `x ≥ 3` and `exp(C_3 (log log x)^{4/3}) ≤ H ≤ x`,
`E_pr((x,x+H]) ≤ E((x,x+H]) ≪ (H/log x)·exp(−(c/2)(log H)^{3/4})`;
for `H ≥ x^θ`: `≪_θ (H/log x) exp(−c_θ (log x)^{3/4})`.
Likewise with `n ≡ b (q)` in the ranges of Theorem 2, with `H/(q log x)`.
*Proof.* Theorem 1 (resp. 2); `(c/2)(log H)^{3/4} ≥ log log x` in the range. ∎

So the brief's prime target needs **no** primes-in-short-intervals input:
the `1/log x` is absorbed by the saving once `(log H)^{3/4} ≫ log log x`.
(Below that range neither form says anything beyond the trivial bound.)
Prime input enters only if one wants a *relative* statement (proportion of
primes in the interval), i.e. a lower bound for the denominator:

**Corollary 3.2 (relative density; PROVED rel. note + cited theorems).**
(a) [Baker–Harman–Pintz 2001: `π(x+H) − π(x) ≫ H/log x` for `x^{0.525} ≤ H ≤ x`.]
For `x^{0.525} ≤ H ≤ x`:
`E_pr((x,x+H]) / (π(x+H) − π(x)) ≪ exp(−c(log x)^{3/4})`.
(Huxley 1972 gives the asymptotic for `H ≥ x^{7/12+ε}`, with the same conclusion.)
(b) [Huxley's zero-density estimate: `π(x+H)−π(x) ∼ H/log x` for almost all
`x ∈ [Y,2Y]` (exceptional measure `o(Y)`), uniformly for `x^{1/6+ε} ≤ H ≤ x`.]
The same ratio bound holds for almost all `x ∈ [Y, 2Y]` when `H ≥ x^{1/6+ε}`.
(c) Progressions: for `q ≤ (log x)^A`, `(a,q)=1`, the prime-in-AP-in-short-
interval asymptotic for `H ≥ x^{7/12+ε}` (Huxley–Iwaniec/Siegel–Walfisz-type
short-interval PNT in APs) gives the relative statement for `p ≡ a (q)`;
with `q` beyond Siegel–Walfisz only a Bombieri–Vinogradov-in-short-intervals
average (Perelli–Pintz–Salerno; Timofeev; Kumchev) is available, giving the
relative statement for all but few q. [Cited ranges to be checked against
the literature before external use — Assessment, not part of the PROVED core.]

The PROVED core of this section is 3.1 and 3.2(a); 3.2(b),(c) are only as
reliable as the quoted ranges.

## 4. The lower end: where short-interval statements stop

**Proposition 4.1 (the target form below `e^{c(log x)^{3/4}}` is ES itself; PROVED, trivial).**
Suppose that for some `x_0, C, c > 0` and some `H_0(x) ≥ 1` with
`C·H_0(x)·e^{−c(log x)^{3/4}} < 1` one has
`E((x, x+H_0(x)]) ≤ C H_0(x) e^{−c(log x)^{3/4}}` for all real `x ≥ x_0`.
Then there is no exceptional `n > x_0`.
*Proof.* Each such window then contains no exceptional integer, and the
windows `(x, x+H_0(x)]`, `x ≥ x_0`, cover `(x_0, ∞)`. ∎

So the brief's target form `E((x,x+H]) ≪ H e^{−c(log x)^{3/4}}` **cannot** be
proved for any `H ≤ e^{c(log x)^{3/4}}/C` (in particular not for polylogarithmic H)
without proving ES for all large n. More generally, in a window of length H a
bound `H e^{−S}` with `S > log H` (+ constant) is already the full conjecture
on that window; the natural scale of savings is `S = (log H)^θ`, with θ = 1 the
trivial ceiling (zero exceptions).

Define the **window exponent** `θ_win` as the sup of θ for which
`E(I) ≪ |I| exp(−c(log|I|)^θ)` holds uniformly over all intervals I.

**Proposition 4.2 (PROVED rel. note).** (a) `θ_win ≥ 3/4` (Theorem 1).
(b) Any `θ_win > 3/4` gives the global exponent `> 3/4` (take `I = (0, N]`);
the short-interval problem is at least as hard as the global one.
(c) For the target form in `(x, x+H]` the three regimes are:
`H ≥ x^θ`: saving `≍_θ (log x)^{3/4}` (Theorem 1, the brief's target);
`e^{c(log x)^{3/4}} ≲ H ≤ x^{o(1)}`: Theorem 1 gives only `(log H)^{3/4} = o((log x)^{3/4})`,
and the full target saving here would need saving exceeding `(log H)^{3/4}`, i.e.
`θ_win > 3/4`-type input *or* position-dependent input;
`H ≲ e^{c(log x)^{3/4}}`: target ⇒ ES (Prop 4.1).

**Shift-uniform methods (relation to (W)).** Lemma 1.1 is shift-uniform: it
bounds `M_{𝔊_X}(H) = max_z #(𝒜_X ∩ (z,z+H])` (this observation is
EXCEPTIONAL_WEIGHTS Prop 5.1(a), for primes; Theorem 1 adds composites and
small primes via Lemma 1.2). Any argument that uses only "exceptional n avoid
the classes of a family 𝔊" and the window length is bounded below by
`M_𝔊(H)`. Hence, for such methods, *the short-window exponent at length H equals
the long-interval exponent at N = H*: position cannot help, and whether
`(log H)^{3/4}` is optimal for them is exactly the open question (W_𝔊) of
EXCEPTIONAL_WEIGHTS at window length H. Known lower bounds for M (Prop 5.1(b),(d)
there; random translates `N e^{−(log N)^{c}}`, greedy `e^{c(log N)^{1/3}}`, toy
family 𝔊_ℛ only) are far from the 3/4 scale, so **no Jacobsthal/Maier-type
construction of windows of length H with ≥ H e^{−C(log H)^{3/4}} avoiders is known**;
for 𝔊_X itself the period 𝓜 = e^{O(X)} far exceeds x, so such windows, even if
they exist as translates, need not occur inside [x, 2x]. Status: OPEN (= (W)).

**What position-dependent input would be.** To beat `(log H)^{3/4}` in
`(x,x+H]` with `H = x^{o(1)}` one must use classes of modulus `q > H` (each
meets the window in ≤ 1 point, so exact CRT counting gives nothing) — i.e.
information about *which* residues the specific integers near x occupy, of
the same non-CRT kind needed for global θ > 3/4 (STATUS "third kind of input").

## 5. Literature and novelty (Assessment)

* Checked: LITERATURE_2026.md (no short-interval or progression-in-short-
  interval exceptional-set result recorded); web searches (Jina, 2026-10-06)
  for "Erdős–Straus short interval(s) exceptional set", "… x+H", "… almost all
  n short interval", Vaughan/Elsholtz–Tao/progressions: nothing found. Salez
  (arXiv:1406.6307) verifies ES for n ≤ 10^17 — a statement about all small
  windows, not a density result. Not checked: Li Delang, Yang Xun Qian, Jia
  Chaohua papers directly (no hits surfaced); this is a gap, flagged.
* Folklore caveat. Every forced class is position-independent (an identity
  valid for all n in the class), and large-sieve/CRT-counting arguments are
  translation invariant. So Vaughan's 1970 argument presumably yields
  `E(I) ≪ |I| exp(−c(log|I|)^{2/3})` for intervals too, and an expert would
  regard "transfer to short intervals" as routine for the *prime/avoider* part.
  The campaign itself already noted shift-uniformity of the 3/4 majorant
  (EXCEPTIONAL_WEIGHTS Prop 5.1(a), primes > max(K,y) only).
* What is (to our knowledge) new here, modestly: (i) Theorem 1 for **all**
  integers in arbitrary windows, via the local smooth-part decomposition
  (Lemma 1.2) which replaces the note's global Rankin/semigroup step;
  (ii) Theorem 2, the progression version with the explicit `q_1` (smooth part)
  loss and the large-prime-modulus independence (Lemma 2.1); (iii) the
  observation that the prime version needs no primes-in-short-intervals input
  (Cor 3.1), prime input entering only for relative densities (Cor 3.2);
  (iv) Prop 4.1 (the target form below `e^{c(log x)^{3/4}}` is equivalent in
  strength to ES on the window) and the window-exponent framing linking the
  short-interval threshold to (W). None of this improves the exponent 3/4.

## 6. Replay

No numerics are needed: every statement is a deduction from thm:assembly
(eq:majorant, eq:ledger, eq:transfer) and lem:identity of the note, plus the
elementary Lemma 1.2. To audit: check (F2) against lem:identity ("every
positive integer in the class … is representable"), that eq:transfer's
counting step `N/q + O(1)` is valid for any real interval, and that all primes
of 𝓜 (eq:space) are ≤ X (used in Lemma 2.1).
