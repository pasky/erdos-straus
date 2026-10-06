# POINTWISE_MN — the m/n witness modulus at exponent 1/4 (task O63)

Status: work in progress (branch `side-agent/mn-quarter`). Labels as in DISCOVERIES.md.

## 0. Setting

Fix `m ≥ 4`. As in POINTWISE_TRANSFER §5.1: an *atom* is `(M,D)` with `M ≡ −1 (mod m)`,
`M ≥ 3`, `A = A_M = (M+1)/m`, `D | A²`; its event is `n ≡ −mD (mod M)`;
`R_m(M) = {−mD mod M : D | A²}`; `W_m(n)` is the least M with `n mod M ∈ R_m(M)`.
By TRANSFER Lemma 5.0 these are exactly the Type II solutions of `m/n` (5.1)
`m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)`, `M = m·uvw − 1`, class `−u v^{−1} ≡ −m u² w (mod M)`.
Note `gcd(M, mA) = 1`; every prime of `m` and of `A` is `≡`-congruent: `M ≡ −1 (mod q)` for all `q | mA`.

For `m = 4` POINTWISE_OMEGA13 Lemma 3.1 says the class `−4D` is a Jacobi non-residue mod M.
This is what lets the square-class process (OMEGA13 §3) never fire an event.

## 1. The Jacobi symbol of the event classes for general m

Let `e = e(m,D)` be the squarefree part of `mD` (equivalently of `m·w` in (5.1), since
`−mD = −m u² w`). Write `e = 2^{t} e_o` with `t ∈ {0,1}`, `e_o` odd.

**Lemma 1.1 (PROVED; brute-forced).** Let `(M,D)` be an atom with M odd.

* (a) Every prime `ℓ | M` has `(−mD | ℓ) = (−e | ℓ)`.
* (b) If `M ≡ 3 (mod 4)`: `(−mD | M) = −(2|M)^t`. In particular `= −1` if `M ≡ 7 (8)`,
  and for `M ≡ 3 (8)` it is `−1` iff `t = 0`.
* (c) If `M ≡ 1 (mod 4)`: `(−mD | M) = (2|M)^t · (−1)^{(e_o−1)/2}`.
* (d) **If `m ≡ 0 (mod 4)`, then `(−mD | M) = −1` for every atom** (OMEGA13 Lemma 3.1 verbatim).

*Proof.* (a) `gcd(M, mA) = 1` and every prime of D divides A, so `ℓ ∤ mD`, and `−mD = −e·□` with the square prime to ℓ. (Also ℓ odd as M is odd.)
For (b),(c): every prime `q | e` divides `mA = M + 1`, so `M ≡ −1 (mod q)`. For odd q,
reciprocity gives `(q|M) = (M|q)(−1)^{((q−1)/2)((M−1)/2)} = (−1)^{((q−1)/2)((M+1)/2)}`,
i.e. `(q|M) = 1` if `M ≡ 3 (4)` and `(q|M) = (−1|q)` if `M ≡ 1 (4)`. Multiply with
`(−1|M)` and `(2|M)^t`: for `M ≡ 3 (4)`, `(−1|M) = −1` and all odd q give 1; for `M ≡ 1 (4)`,
`(−1|M) = 1` and `∏_{q|e_o}(−1|q) = (−1|e_o) = (−1)^{(e_o−1)/2}`.
(d) `m ≡ 0 (4)` gives `M ≡ 3 (4)`. If `t = 1` then `v_2(mD)` is odd; if `8 | m` then
`8 | mA`; if `m ≡ 4 (8)` then `v_2(D)` is odd, so `2 | A` and `8 | mA`. Either way
`M ≡ 7 (8)`, `(2|M) = 1`, and (b) gives `−1`. ∎

*Check.* `scripts/mn_jacobi.py 50000 4 5 6 7 8 9 10 11 12 14 18`: the formula (b)/(c) and (a)
hold on every odd-M atom (e.g. 473 842 atoms for m=4, 284 878 for m=5), 0 failures; for
`m ∈ {4,8,12}` every symbol is −1.

**Consequence (square-consistency).** Call an atom *square-consistent* if `−mD` is a
square unit modulo every prime power `ℓ^v ‖ M` (for `ℓ = 2`: `v=1` any; `v=2`: `≡1 (4)`;
`v≥3`: `≡1 (8)`). These are exactly the atoms that the OMEGA13 square-class process can fire.
By (d) there are none for `m ≡ 0 (4)`. For `m ≢ 0 (4)` they are a positive proportion
(`M ≤ 5·10⁴`: m=5: 68 642 of 363 982; m=6: 56 964/293 117; m=7: 38 355/244 129;
m=10: 29 704/159 390). Smallest examples: `m=5: (M,D)=(9,1)` (class 4 ≡ 2² mod 9),
`(29,1)` (class 24 ≡ 13² mod 29); `m=6: (5,1)` (class 4); `m=7: (13,2)` (class 12 ≡ 5²).

## 2. For m ≢ 0 (mod 4) the square-class process fires: a precise obstruction

**Proposition 2.1 (PROVED).** Let `m ≢ 0 (mod 4)`. There are infinitely many primes
`ℓ ≡ −1 (mod m)` such that the prime atom `M = ℓ` has event classes in *both* cosets of the
squares mod ℓ. Hence for any rule that reveals `r mod ℓ` uniformly inside a coset of the squares
(either coset, chosen by any rule), the prime atom `M = ℓ` fires with probability `≥ 2/(ℓ−1) > 0`.

*Proof.* It suffices to find ℓ prime, `ℓ ≡ −1 (m)`, `ℓ ≡ 1 (4)`, and a prime `q | A = (ℓ+1)/m`
with `(q|ℓ) = −1`: then `D = 1` and `D = q` (both divide `A²`) give classes `−m`, `−mq` with
Legendre symbols of ratio `(q|ℓ) = −1`.
* `m` odd: take `q = 2` and `ℓ ≡ −1 (mod m)`, `ℓ ≡ 5 (mod 8)` (compatible). Then `ℓ+1 ≡ 6 (8)`,
  so `2 | A`, and `(2|ℓ) = −1`.
* `m ≡ 2 (mod 4)`: take an odd prime `q ≡ 3 (4)`, `q ∤ m`, and `ℓ ≡ −1 (mod mq)`, `ℓ ≡ 1 (mod 4)`
  (compatible, as `v_2(mq) = 1`). Then `q | A` and, by Lemma 1.1's reciprocity step,
  `(q|ℓ) = (−1|q) = −1`.
Dirichlet's theorem gives infinitely many such ℓ. ∎

Examples: `m=5`, `ℓ=29` (`A=6`, classes `−5D`, `D|36`, contain both residues and
non-residues); `m=6`, `ℓ=5` (`A=1`, class `4 = 2²`, so the squares coset itself is hit).

*Scope.* In the OMEGA13 process every prime `ℓ ≤ Y` whose fibre mass exceeds `η ≍ 1/log 𝓛` is
stepped; the Haar mass through a fixed small prime is `≫ 𝓛³/ℓ`, so fixed small ℓ
(e.g. 29 for m=5) are always stepped. So the square-class process of OMEGA13 §3 does not run for
`m ≢ 0 (4)`, and no "random square class of a fixed quadratic character pattern" replaces it.
More generally, Lemma 1.1(b),(c) show that the Jacobi symbol `(−mD|M)` is a function of
`(M mod 8, e mod 8)`, and for a fixed M it takes both values as D varies whenever A has a prime
`q ≡ 3 (4)` (M ≡ 1 (4)) or `t` varies (M ≡ 3 (8)); a coset `k·□` of the squares has
`(k|M)` depending on M only, so it cannot separate the event classes for those M. What survives
for every m: atoms with `M ≡ 7 (mod 8)` are never square-consistent (Lemma 1.1(b)).

## 3. The case m ≡ 0 (mod 4): OMEGA13 transfers verbatim

**What "hard" means.** For a modulus Q, the *Type-II-hard* classes are
`H_m(Q) = {r ∈ (Z/Q)^× : r mod M ∉ R_m(M) for all M | Q, M ≡ −1 (m)}` (`scripts/mn_hard.py`):
primes `p ≡ r (Q)` have no Type II solution (5.1) of `m/p` with `M | Q`, i.e. are not covered by
any of the finitely many polynomial Type II identities attached to divisors of Q. For `m = 4` the
squares mod 840 are Mordell's hard classes (Mordell's 6 classes also use Type I identities; the
Type-II-hard set mod 840 alone has 24 classes, `mn_hard.py 4 840`). By Lemma 1.1(d), **for
`m ≡ 0 (4)` every class that is a square modulo each odd prime of Q is Type-II-hard modulo Q**
(for every Q); this is the m-analogue of "Mordell-hard". (For `m ≢ 0 (4)` the hard sets are
not unions of square cosets: e.g. `H_5(840) = {r ≡ 1 (mod 4)} ∩ {r mod 7 ∈ {1,3,5}}` (48 classes;
the atom `M = 4, D = 1` kills `r ≡ 3 (4)`), and `{1,3,5}` is 1 together with two of the three
non-residues `{3,5,6}` mod 7 — not closed under multiplication; `mn_hard.py 5 840`.)

*Scope of "hard" (R63 MINOR-1).* All hardness statements in this file concern **Type II only**,
i.e. the witness function `W_m` (complete for Type II by TRANSFER Lemma 5.0). No claim is made about
Type I solutions or about any other identities covering the output primes.

**Theorem 3.1 (m ≡ 0 (4); PROVED modulo the inputs of OMEGA13 Thm 3.4 / Thm 5.1).** Fix
`m ≡ 0 (mod 4)`, `m ≥ 4`; constants depend on m.
* (i) (Haar, modulo NT for the upper bound and the fundamental lemma for the lower bound)
  `𝓛³/log𝓛 ≪ log(1/δ*_m(T)) ≪ 𝓛³(log𝓛)^5`, where `δ*_m(T)` is the Haar probability on `Ẑ^×`
  that n avoids all m-events with `M ≤ T`.
* (ii) (prime side, modulo Gallagher (G), NT and OMEGA10 Thm 3.4) For infinitely many primes p,
  `W_m(p) ≥ exp(c_m(log p)^{1/4}(log log p)^{−1/4})`, and these p can be taken to be squares
  modulo 840 (forced steps), hence Type-II-hard modulo 840 and modulo the whole quarantine
  modulus Q.

*Proof (substitution list).* OMEGA13 uses the ES structure only in the following places; each
holds for `m ≡ 0 (4)`:
1. *Lemma 3.1 → Lemma 1.1.* (a) is Lemma 1.1(a) with `d ↦ e`; (b) is Lemma 1.1(d). The drift
   at an `a=0` step is `1 + (−e_E|ℓ) ≤ 2` (Lemma 3.2(a)); nothing else about d is used.
2. *M odd.* `M ≡ 3 (4)`, so atoms never constrain the 2-adic coordinate and the start
   `Q=8, r≡1 (8)` has `p_0 = P_H` (Lemma 3.2(b)). The forced steps at 3, 5, 7 are `a=0` square
   steps, safe by Lemma 1.1(d).
3. *Lemma 3.3(A) (NT).* Use `Q_1(n)=n`, `Q_2(n)=mn−1` (`n = A`, `M = mn−1`): coprime linear
   forms with fixed coefficients, `ρ(p) = 2` for `p ∤ m`, `ρ(p) = 1` for `p | m` (incl. `p=2`), so
   no fixed prime divisor and `∏_{p≤x}(1−ρ(p)/p) ≍_m (log x)^{−2}`. The function
   `F = τ(n_1²)f_2(n_2)` is unchanged. Both displays hold with m-dependent constants.
4. *Lemma 3.3(B).* Elementary divisor sums over `M ≤ T`; the only change is `M ≤ T`,
   `M ≡ −1 (m)`, `A ≤ T/m`. Unchanged.
5. *Thm 3.4.* Run the square-class process; no event fires by item 1. The conclusion
   `δ* ≥ φ(Q)^{−1}·exp(−(4/3)S_res)` (Haar on `Ẑ^×`) gives the upper bound.
6. *Lower bound.* Prop 3.2 below.
7. *Thm 5.1 / interface checks I1–I3.* I1 (BRW minorant, twist) and I2 (junta via OMEGA10/11)
   concern an abstract system of unit-class events on prime-power coordinates with
   `∏ℓ^{v_ℓ} = M ≤ T`; the ES structure enters only through masses (items 3–5). I3 needs
   `r` square at the odd primes of Q and `r ≡ 1 (8)`, which the process gives, and Property (I)
   uses Lemma 3.1 → Lemma 1.1(d). The auxiliary prime `ℓ_aux` is as in OMEGA13. ∎

This is the same "4 ↦ m" substitution that POINTWISE_TRANSFER Cor 5.2 makes for the 1/7
architecture (reviewed there); the only genuinely m-specific input of the 1/4 architecture is
Lemma 3.1, which is why the dividing line is `m mod 4`.

**Proposition 3.2 (Haar lower bound for every m ≥ 4; PROVED modulo the fundamental lemma).**
`log(1/δ*_m(T)) ≫_m 𝓛³/log𝓛`.

*Proof.* POINTWISE_HAAR Thm 2.1 with `4 ↦ m`: in the family 𝓕 replace `M ≡ 3 (4)` and
`M ≡ −1 (mod 4n)` by `M ≡ −1 (mod mn)` (this gives `M ≡ −1 (m)` and `n | A_M`). (F1) becomes
`mD ≤ m n² ≤ mT^{1/5} < M` for `M ≥ √T`, so the residues `−mD mod M` are distinct. The fundamental
lemma sifts a progression mod `mn` (primes `p | mn` never divide M), giving block contributions
`≥ c_2/(m n log y)`. Lemmas 2.3, 2.4 use only (F2)–(F5) and progressions mod `4n`, which become
`mn` (constants change by `m/4`). Theorem 1.4 (Janson-type) is abstract. ∎
No Jacobi input is used, so Prop 3.2 holds for every m, including `m ≢ 0 (4)`.

## 4. The prime-side transfer does not need r to be a square

OMEGA13's interface check I3 assumes `r` is a square mod every odd prime of Q and `r ≡ 1 (8)`,
so that every real character χ trivial on `H = {x ≡ 1 (Q)}` has `χ(r) = 1`. For general m we
want to allow arbitrary unit classes, so we record:

**Lemma 4.1 (PROVED modulo (G) and the effective Page bound — the inputs of OMEGA9 Thm 1.1).**
OMEGA13 I3 (O11 Lemma 3.1 on the coset `rH`) holds for every unit `r mod Q` with cells consistent
with r (`b_i ≡ r (mod gcd(d_i,Q))`); no quadratic condition on r is needed.

*Proof.* Only Case A of OMEGA9 Thm 1.1's proof (lines "Case A: χ_D trivial") looks at the value
of a real character at r: for χ trivial on H, `c(χ) = χ̄(r)μ/φ(Q)` and `χ(r) ∈ {±1}` for real χ.
* If the exceptional character has `χ_1(r) = +1`, the argument is verbatim.
* If `χ_1(r) = −1`, the exceptional term `−c(χ)x^{β_1}/β_1 = +μx^{β_1}/(β_1φ(Q))` is *positive*,
  so the main term is `λ'μx/φ(Q)` with `λ' = 1 + x^{β_1−1}/β_1 ≥ 1`; the (G) error is
  `≤ μx/(200φ(Q))` and `|R_1| ≤ μx/(400φ(Q))` as in Case 0, so `S(x) > 0` without the
  effective Page bound.
Case B uses only `|ψ_1(r)| = 1`; non-real characters enter only through `|c(χ)|`; cell
consistency and the `ℓ_aux` construction (`r' ≡ r (Q)`, `r' ≡ 1 (ℓ_aux)`) do not use squares. ∎

So the square condition in OMEGA13 serves only the *quarantine* (Lemma 3.1), not the transfer.
"Mordell-hardness" of the output primes becomes: p is Type-II-hard modulo the quarantine modulus.

## 5. m ≢ 0 (mod 4): the admissible-class process and the exact missing input

Since no quadratic structure is available (§2), the natural replacement of the square-class
process is to forbid, at each step, exactly the classes that would fire an event.

**The admissible unit process (AUP).** Start from `Q = 1`. Coordinates, events, fibre masses
`w̃_ℓ`, threshold η and eligibility `ℓ ≤ Y` are as in OMEGA13 §3, with fibre `n ≡ r (Q)`,
except that **for odd m the prime 2 is an ordinary coordinate** (even M exist): unit classes mod
`2^k`, with `N = 2^{k−1}` fibre classes at level `k ≥ 2` and `N = 1` at level 1 (R63 MINOR-4).
OMEGA13's remark "M odd, so `p_0 = P_H`" is not used; the prefix below supplies the factor `1/δ_0`.
A step at `(ℓ,a)` is taken while `w̃_ℓ > η` (any fixed tie-break rule, e.g. the smallest heavy
prime first). Before the step, call a class `x mod ℓ^{a+1}` of the current fibre *forbidden* if
some atom `(M,D)` with `v_ℓ(M) = a+1`, all other prime powers of M already in Q, and
`−mD ≡ r (mod M/ℓ^{a+1})`, has `−mD ≡ x (mod ℓ^{a+1})`. Let `f ∈ [0,1]` be the forbidden fraction
(a predictable quantity). The step reveals `r mod ℓ^{a+1}` uniformly among the non-forbidden
classes. If `f = 1` the process *dies*. Let `Λ(ℓ) := ∏_{steps at ℓ}(1−f)^{−1}`.

By construction no atom ever fires (every atom whose coordinates are all quarantined is
inconsistent with r), so the β-local lemma applies to the residual system, and by Lemma 4.1 the
transfer applies to the fibre `rH`.

**Small-prime prefix.** Fix a constant modulus `Q_0 = Q_0(m)` (e.g. `∏_{ℓ≤L_0}ℓ^{k_0}`). Let
`H_m(Q_0)` be its Type-II-hard set (§3); it is non-empty (`1 ∈ H_m(Q_0)`, TRANSFER Lemma 5.1(ii)),
so its density is `δ_0 ≥ 1/φ(Q_0) > 0`. The *prefixed* AUP starts from `Q = Q_0` with
`r_0 = r mod Q_0` uniform on `H_m(Q_0)` (cost `log Q_0 = O_m(1)`), and then runs the AUP on all
further digits (including deeper digits of the primes dividing `Q_0`). No atom with `M | Q_0`
fires. Since the law of `r_0` has density `≤ 1/δ_0` w.r.t. Haar, every initial mass and pair
mass is at most `1/δ_0` times its Haar value — a constant loss.

**Hypothesis ADM_m(K, Q_0).** For constants `K = K_m`, `Q_0 = Q_0(m)`, uniformly in large T (with
OMEGA13's `β, η` and `Y = 𝓛^{C}` for the explicit `C = C_K + 4` of Thm 5.1's proof, R63 MINOR-2),
with probability `≥ 7/8` the prefixed AUP does not die and
`Λ_end(ℓ) ≤ K` for every `ℓ ≤ Y` (Λ counts the steps after the prefix).

Without the prefix (`Q_0 = 1`) the hypothesis is false-looking for some m: for `m = 7` the
unprefixed process dies at `ℓ = 3` in 2 of 40 runs (`T = 2·10⁴`), because a random 2-adic class
can be incompatible with every class mod 3 (§6).

For `m ≡ 0 (4)` the square-restricted version holds with `K = 2` (it is OMEGA13 Lemma 3.1, i.e.
Lemma 1.1(d): nothing is ever forbidden inside the squares). For `m ≢ 0 (4)` it is open.

**Theorem 5.1 (CONDITIONAL on ADM_m(K, Q_0); the implication is PROVED modulo the inputs of OMEGA13
Thm 3.4/5.1).** Under ADM_m(K, Q_0):
`log(1/δ*_m(T)) ≪ 𝓛³(log𝓛)^{K+4}`, and `W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−B_K})` for
infinitely many primes p (Type-II-hard modulo their quarantine modulus).

*Proof.* Only Lemma 3.2 of OMEGA13 changes; replace `2^{u_i(E)}` by
`Ψ_i(E) := ∏_{ℓ|M, ℓ≤Y} K/Λ_i(ℓ)` and stop the process (declaring failure) *before* a step that
would make some `Λ(ℓ) > K` (possible since f is predictable; death is the case `Λ = ∞`).
* (a) `G_i = Σ_E p_i(E)Ψ_i(E)φ(E)` is a nonnegative supermartingale up to the stopping time:
  at a step at `(ℓ,a)`, atoms with `ℓ ∤ M` (or with `v_ℓ(M) ≤ a`) are unchanged in law; an atom with
  `v_ℓ(M) ≥ a+1` that is not completed by this step has `E[p_new] ≤ p/(1−f)` (its class is
  hit with probability `≤ 1/((1−f)N)` instead of `1/N`), while `Ψ` is multiplied by `(1−f)`;
  a completed consistent atom has `p_new = 0` (its class is forbidden). On the success event
  `Λ ≤ K`, so `Ψ ≥ 1`.
* (b), (c) follow by the same optional-stopping argument, with `2^{ω_Y(M)}` replaced by
  `K^{ω_Y(M)}`, on the success event, and with an extra factor `1/δ_0` from the prefix law
  (`E[p_0(E)] ≤ P_H(E)/δ_0`, `E[Π_0] ≤ Π_0^{Haar}/δ_0`). (d): the pair potential `Π_i Ψ_i(F)Ψ_i(F')` is a
  supermartingale by OMEGA13's case check with `ρ := N` (classes of the current *fibre*; the
  measure `p_i` is Haar on unrevealed digits). An agreeing step gives
  `Π_new = Π·N·1[match]` (the factor ρ = N is removed), `P(match) = 1/((1−f)N)`, so `E[Π_new] = Π/(1−f)`, while
  `Ψ(F)Ψ(F')` is multiplied by `(1−f)²`; a step on a coordinate of only one event multiplies its
  p by `≤ 1/(1−f)` in mean and its Ψ by `(1−f)`; disagreement gives `Π_new = 0`. Hence
  `E[Π_end] ≤ K^{ω_Y+ω_Y'}Π_0` on the success event.
* Lemma 3.3: NT applies with `f_2(p) ≤ Kβ·(p/φ(p))` at `p ≤ Y` (bounded multiplicative), so
  `S_H^β ≪ 𝓛³(log Y)^{K}`, the cost sum `≪ 𝓛³(log Y)^{K+3}`; 3.3(B) is uniform (`Ξ ≪_K 𝓛^{C_K}`).
* Thm 3.4: the four bad events (failure, a heavy late prime, cost `> 8E`, `S_res > 8E`) each
  have probability `≤ 1/8` (`Y = 𝓛^{C_K+4}`), so a good realisation exists; Lemma 1.1 on the
  fibre gives the Haar bound. Thm 5.1: as in §3, item 7, with Lemma 4.1 for I3. ∎

*Post-referee note (2026-10-06, R77 D3).* For **odd m** the pair `n, mn−1` (`n = A`, `M = mn−1`) used in
the Lemma 3.3 step above has the **fixed prime divisor 2** (`n(mn−1)` is even for every n), so NT does not
apply verbatim. Repair: split by the parity of n. For `n = 2t`: forms `Q_1 = t`, `Q_2 = 2mt−1` (product odd
at t = 1, so ρ(2) = 1). For `n = 2t+1`: `M = 2(mt + (m−1)/2)`, forms `Q_1 = 2t+1`, `Q_2 = mt + (m−1)/2`
(`2t+1` is odd and the second form has one root mod 2, so ρ(2) = 1). Neither pair has a fixed prime divisor
(R77 checked odd m ≤ 199, p < 60), both are coprime linear forms with discriminant `≪_m 1`, and the factors
extracted at 2 (`τ((2t)²) ≤ 3τ(t²)`-type, and the bounded factor `f_2(2^a)` of M's 2-part) are absorbed in
the constants (they are multiplicative with values bounded at powers of 2 only). The resulting Euler
products differ from the ones above by a factor `O_m(1)`. For even m (in particular m ≡ 0 (4), Thm 3.1)
nothing changes: `ρ(2) = 1` there. So Thm 5.1's implication is PROVED modulo the same inputs for odd m
with this split (paper v6, Thm 15.7).

So for `m ≢ 0 (4)` the 1/4 machinery is reduced to the single probabilistic input ADM_m:
*a random hard class, revealed prime by prime, never has most of its next digit forbidden*.

## 6. Evidence for ADM_m and why it is plausible (EVIDENCE / Assessment)

*Experiment* (`scripts/mn_greedy.py m T mode seed`). A stronger, simplified variant of the AUP:
*every* prime `ℓ ≤ T` is quarantined to full depth `e_ℓ = max v_ℓ(M)`, in increasing order, and
`r mod ℓ^{e_ℓ}` is drawn uniformly from the non-forbidden units at once; f is the forbidden
fraction, `Λ(ℓ) = 1/(1−f)`. Mode `pref:3` draws the 2- and 3-adic digits uniformly from the hard
set of the {2,3}-smooth atoms (rejection sampling) — the prefix of §5 with `Q_0` of full depth.
This fully constructs a class that is Type-II-hard for every `M ≤ T`.

| m | T | mode | runs | deaths | max Λ(ℓ) over all ℓ |
|---|---|---|---|---|---|
| 5 | 2·10⁴ | pref:3 | 40 | 0 | 3.97 |
| 7 | 2·10⁴ | pref:3 | 40 | 0 | 4.23 |
| 9 | 2·10⁴ | pref:3 | 40 | 0 | 2.25 |
| 5 | 3·10⁵ | pref:3 | 3 | 0 | 3.33 |
| 7 | 3·10⁵ | pref:3 | 3 | 0 | 3.20 |
| 5, 6, 9, 10, 11, 13 | 2·10⁴ | unit (no prefix) | 40 each | 0 | — |
| 7 | 2·10⁴ | unit (no prefix) | 40 | **2 (at ℓ=3)** | — |
| 5, 6, 7, 11 | 3·10⁵ | unit1:3 (class 1 at 2, 3) | 3 each | 0 | ≤ 3.29 |
| 4 | 10⁵ | unit | 1 | 0 | 2 (f = 1/2 at 3, 5, 7: the non-squares) |
| 4 | 10⁵ | sq | 1 | 0 | 1 (nothing forbidden: Lemma 1.1(d)) |

The largest Λ always occurs at a prime `ℓ ≤ 19`; for `ℓ > 50`, `ℓ·f_ℓ/(log ℓ)³ ≤ 0.55` in every run
(the max is attained by deterministic prime-power atoms and is seed-independent). So per-prime
drift is bounded by about 4 and decays like `(log ℓ)³/ℓ`.

*Heuristic.* In increasing order, the atoms completed at ℓ are `M = ℓ^{a+1}M'` with M' composed
of smaller primes, consistent with r with probability `≈ Λ-drift/φ(M')`; hence
`E f_ℓ ≈ Σ_{M' (<ℓ)-smooth} τ(A²)/(ℓφ(M')) ≍ (log ℓ)^3/ℓ`, a convergent smooth-number sum that does
**not grow with T**. In the adaptive OMEGA13 order, completions at a revisited prime involve only
deep digits (`ℓ^{a+1} ≳ 𝓛³`), whose forbidden fractions are `≪ ℓ^{−a}`.

*Why ADM is not proved here.* (i) Small primes (`ℓ ≤ 40` in the data) have `f` up to 0.84 and the
outcome depends on the 2-adic/3-adic digits (m=7 deaths), so a constant prefix is needed and its
effect on later f is a finite but non-explicit computation. (ii) For medium ℓ, a union bound
needs `Σ_ℓ P(f_ℓ > 1−1/K)` small; first moments do not suffice (`Σ_ℓ (log ℓ)³/ℓ` diverges), and the
second moment (OMEGA13's pair potential, restricted to atoms completed at ℓ) leads to averages of
`τ((ℓ^{a+1}M'+1)/m)²` over primes ℓ with smooth M' of unbounded size — a Shiu-type bound in
progressions to smooth moduli larger than the range of ℓ, which we do not have.

## 6b. Unconditional fallback for m ≢ 0 (4): exponent 1/5 via the class of one

OMEGA12 (exponent 1/5, Haar `𝓛^5 log𝓛`) uses the *class of one* (OMEGA11 graded quarantine), not
squares, so Lemma 3.1 is never invoked. A line-by-line check of OMEGA12 (+ the OMEGA11 parts it
uses) for general m was done by a deep-mode subagent and spot-checked here; its findings:

* ET inputs: Prop 1.4 is stated for general `k ≪ (AB)^{O(1)}` (bound `AB log(A+B) log(1+k)`),
  Thm 7.1 is uniform over polynomials of fixed degree with root-count bound C, Cor 7.4 and (7.10)
  are for general k / general coefficients. So `4 ↦ m` is admissible.
* **Root counts.** OMEGA12 uses `ρ ≤ 2` for `4dx²+1`. For `P(x) = m d x² + 1` with `md` odd, the
  count mod `2^k` can be **4** (checked: max over odd `md < 200`, `k ≤ 11` is 4; odd prime powers
  give ≤ 2). So ET Thm 7.1 must be used with `C = 4` and Euler factor `1 + 4/(ℓ−1)` at ℓ = 2 — a
  constant change.
* **2-adic coordinate.** For odd m, `M = mA − 1` can be even, so the quarantine must include the
  prime 2 with graded raises (OMEGA11's event model otherwise misses constraints: e.g. `m = 5`,
  `M = 464 = 16·29`, `D = 3` survives `Q = 840` (`gcd = 8 | 16 = 5D+1`) and still needs
  `n ≡ 1 (mod 16)` — verified). Routine: the charging argument is prime-independent.
* Class-of-one exclusion: TRANSFER Lemma 5.1(ii) (archimedean, valid for every m, M even included).
* Lemma 3.1 / 4.1 parity assertions (`q` odd, `P` odd) are replaced by `ℓ ∤ mad`; the linear
  branch uses `gcd(ma², b) = 1` from `qb − ma²d_0 = 1`.

**Corollary 6.1 (PROVED modulo (G), ET Prop 1.4/Thm 7.1/Cor 7.4/(7.10), OMEGA10 Thm 3.4).** For every
fixed `m ≥ 4`: `log(1/δ*_m(T)) ≪_m 𝓛^5 log𝓛` and `W_m(p) ≥ exp(c_m(log p)^{1/5}(log log p)^{−1/5})`
for infinitely many primes p. (For `m ≡ 0 (4)` superseded by Thm 3.1.) This improves TRANSFER
Cor 5.2's `1/7` for every m, in particular for Sierpiński's `5/n` — **but only for the Type II
witness `W_5`**: the output primes satisfy `p ≡ 1 (mod Q)` with `840 | Q` (so e.g. `p ≡ 1 (5)` for
`m = 5`) and are Type-II-hard modulo Q; whether `5/p` has a Type I or other easy solution is not
addressed (R63 MINOR-5).

*Proof (substitution list for OMEGA12 Thm 6.3 and the OMEGA11 parts it uses; R63 MAJOR-1).*
Throughout, `4 ↦ m`, `M ≡ 3 (4) ↦ M ≡ −1 (m)`, `A = (M+1)/m`, `g = gcd(M, mD+1)`.

(0) *Parametrisation (OMEGA12 Lemma 2.1).* For `D ≤ A`: `D = da²`, `A = dab` (d squarefree, `b ≥ a`),
`P = ma²d+1`, `e = g`, `f = P/e`, `c = (a+b)/e`, `N = M/e`; from `mad(a+b) = P + M` and
`gcd(g, mad) = 1`: `g | a+b`, `macd = f + N`,
`N ≥ (m/2)acd − 1 ≥ acd`, injectivity, and the involution `D ↦ A²/D` preserving g (from
`mA ≡ 1 (M)`: `mA²/D + 1 ≡ (mD)^{−1}(1+mD)`): algebra with 4 replaced by m; brute-forced by R63
(`scripts/review_mn_cor61.py`, m = 4..30, M ≤ 3000, even M included, 0 defects). Lemma 2.2 uses ET
Prop 1.4 with `k = m` (stated for general `k ≪ (AB)^{O(1)}`, bound `≪ AB log(A+B) log(1+k)`).

(i) *O11 Setting 2.0 and Lemmas 2.1–2.2 (graded quarantine), odd m.* Even M occur, so put
`Q := 2^{a_2}∏_{ℓ odd}ℓ^{a_ℓ}` with a 2-adic coordinate `X_2 := n mod 2^{f_2}` (`f_2 = ⌊𝓛/log 2⌋`) on
the fibre `n ≡ 1 (2^{a_2})`, start `a_2 = 3` (so `8 | Q` as before), and let `a_2` be raised by the
same rule `w_2 > c(a_2+1)log 2/𝓛`. Lemma 2.1: the fibre probability at `ℓ = 2 ∈ supp` is
`2^{−(v−a_2)}` (`a_2 ≥ 3`), within the stated `≤ (ℓ/(ℓ−1))ℓ^{min(v,a)}/ℓ^v`; survival is
`gcd(M,Q) | mD+1` and `M ∤ Q`. Property (I): if `n ≡ 1 (Q)` and `n ≡ −mD (M)` then the atom
survives; if `M | Q` then `n ≡ 1 (M)`, impossible by TRANSFER Lemma 5.1(ii) (archimedean: after
`D ↦ A²/D`, `M | D + A` contradicts `0 < D + A ≤ 2A < M`; valid for even M). Lemma 2.2's charging
uses only `Σ_ℓ v_ℓ(M)log ℓ = log M`, prime-independent, so ℓ = 2 is charged like any other prime.
(Without this the event model is incomplete: m=5, M=464=16·29, D=3 survives `Q = 840` and still
needs `n ≡ 1 (16)`.) For `m ≡ 2 (4)` M is odd and nothing changes.

(ii) *OMEGA12 Lemma 3.1, small q.* The sentence "`q = 2` is omitted harmlessly: N divides the odd M"
is false for odd m. Replace by the dichotomy, now for every prime ℓ including 2: if `ℓ | mad` then
`ℓ ∤ N` (as `N ≡ −f (ℓ)` and `f | P ≡ 1 (ℓ)`); otherwise `q | N = mad·c − f` puts c in one class
mod q. The bound `≤ (2/(ad))Σ_{q≤C}1/(iq)` then includes `q = 2^i`; Mertens over all prime powers is
unchanged.

(iii) *OMEGA12 Lemma 4.1.* "Every q | P is odd" and "Q is odd-valued, so `ρ_Q(2^j) = 0`" are false
when `md` is odd. Replace:
* every `q = ℓ^i | P` has `ℓ ∤ mad` (since `P ≡ 1 (ℓ)` if `ℓ | mad`); `q = 2^i` is allowed;
* `P < 8mZ³` (from `P = ma²d+1`, `a < 2A`, `d < 2B`), so the large-q part is
  `Σ_{q|P,q>Z^{1/2}} 1/i ≤ 2log(8mZ³)/log Z ≪_m 1`;
* quadratic case: `P(x) = mdx²+1` has `≤ 2` roots mod odd prime powers and `≤ 4` roots mod `2^k`
  (checked: max 4 over odd `md < 400`, `k ≤ 11`; this is ET's own case "`ρ_{ka}(p^j) ≤ 2` for odd
  `p^j`, `≤ 4` for `p = 2`" in their proof of Prop 1.4). So "two roots" becomes "≤ 4 roots `x_0`";
  `ρ_Q(p^j) = ρ_{md}(p^j)` for `p ∤ q` (bijection), and for `p = ℓ` each root of P mod `ℓ^{i+j}`
  fixes `a' mod ℓ^j`, so `ρ_Q(ℓ^j) ≤ 4`; Euler factor `≤ 1 + 4/(ℓ−1)`; ET Thm 7.1 with
  `(degree, l, C) = (2, 5, 4)`; ET (7.10) with `k = m` (stated for general k);
* coefficients `mdq, 2mdx_0, (mdx_0²+1)/q ≤ 2mdq ≤ 4mA^{3/2} ≤ N'^5` needs `A ≥ 4m`; linear case
  coefficients `ma², b_a ≤ ma²+1 ≤ N^6` needs `B ≥ 4m`, and `gcd(ma², b_a) = 1` because
  `q·b_a − ma²d_0 = 1` (no parity argument). Blocks with `Z < Z_0(m) := max(16, 4m)` have
  `h(P) ≪_m 1` and are absorbed as in the `Z < 16` case.
Everything else in Lemma 4.1 and Cor 4.2, Thm 5.1 (`Ω_0 ≪_m 𝓛^4 log𝓛`) is unchanged.

(iv) *OMEGA12 Lemma 6.2.* Start from `a_ℓ = 1` for odd `ℓ ≤ 𝓛`, `a_ℓ ≥ 1` for `ℓ ∈ {3,5,7}`, and
`a_2 = 3`; the start cost is `log(8·∏_{odd ℓ ≤ max(𝓛,7)}ℓ) ≤ 1.02𝓛 + 7` as before. Every prime with
`a_ℓ = 0` is `> 𝓛` (2 is never unstepped), so the bound `P(E) ≤ e³g/M` holds verbatim.

(v) *Prime side.* OMEGA12 Thm 6.3 / O11 Thm 3.2 use the class of one mod Q; the transfer (O9 Thm 1.1,
O11 Lemma 3.1) needs `8 | Q` (true: `a_2 ≥ 3`) and the twist prime coprime to Q (odd, as before).
The output primes satisfy `p ≡ 1 (Q)`; they are Type-II-hard modulo Q because the class of one is
hard (TRANSFER Lemma 5.1(ii)) — **not** "Mordell-hard", which is an m = 4 notion. Haar side:
`log(1/δ*_m) ≤ log φ(Q) + 4S_1 ≪_m 𝓛^5 log𝓛` (O11 Cor 3.3), modulo ET alone. ∎

## 7. Status

| item | statement | label |
|---|---|---|
| Lemma 1.1 | `(−mD|M)` formula; `= −1` for all atoms iff `m ≡ 0 (4)` (with Prop 2.1) | PROVED (+ check, M ≤ 5·10⁴, 11 values of m) |
| Prop 2.1 | `m ≢ 0 (4)`: infinitely many prime atoms meet both square cosets; square-class process fires | PROVED |
| Thm 3.1 | `m ≡ 0 (4)`: Haar exponent 3 (`𝓛³/log𝓛 ≪ log(1/δ*_m) ≪ 𝓛³(log𝓛)^5`) and `W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o. | PROVED modulo (G), NT, fundamental lemma, OMEGA10 Thm 3.4 (substitution proof; needs review) |
| Prop 3.2 | Haar lower bound `≫ 𝓛³/log𝓛` for every m ≥ 4 | PROVED modulo fundamental lemma |
| Lemma 4.1 | transfer (I3) for arbitrary unit class r | PROVED modulo (G) |
| Cor 6.1 | every m: Haar `≪ 𝓛^5 log𝓛`, `W_m(p) ≥ exp(c(log p)^{1/5}(log log p)^{−1/5})` i.o. | PROVED modulo ET (+G, OMEGA10); substitution proof §6b (0)–(v) (R63 MAJOR-1 repair) |
| Thm 5.1 | `m ≢ 0 (4)`: same conclusions as Thm 3.1 (log-powers depending on K) | CONDITIONAL on ADM_m(K, Q_0) |
| §6 | ADM_m numerics (m = 5, 6, 7, 9, 10, 11, 13): max per-prime drift ≈ 4, `f_ℓ ≲ 0.55(log ℓ)³/ℓ` | EVIDENCE |

**Answer to the task question.** The Jacobi symbol `(−mD | M)` is identically −1 exactly in the
case `m ≡ 0 (mod 4)` (more precisely: for `m ≡ 0 (4)` always; for every `m ≢ 0 (4)` it takes both
values, and the square-class process fires). The 1/4 machinery and the Haar exponent 3 extend
verbatim to `m ≡ 0 (4)`. For `m ≢ 0 (4)` — including Sierpiński's `m = 5` — they break at exactly
one point, OMEGA13 Lemma 3.1, and everything else goes through once a random hard class with
bounded per-prime drift exists (ADM_m), which the numerics support but we cannot prove.

## Replay

```
cd scripts
(ulimit -v 8000000; timeout 900 uv run python mn_jacobi.py 50000 4 5 6 7 8 9 10 11 12 14 18)   # Lemma 1.1, §1 counts
(ulimit -v 8000000; timeout 300 uv run python mn_hard.py 5 840)       # §3 hard sets (also 4 840, 8 840, 5 278460)
(ulimit -v 8000000; for s in $(seq 1 40); do timeout 300 uv run python mn_greedy.py 7 20000 unit $s; done | grep -c "dead_at=[0-9]")   # §6: 2 deaths
(ulimit -v 8000000; timeout 900 uv run python mn_greedy.py 5 300000 pref:3 1)   # §6 table rows
```
