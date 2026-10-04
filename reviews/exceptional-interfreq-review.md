# Hostile review: EXCEPTIONAL_INTERFREQ.md (task O18, checkpoint 1)

Subject: branch `side-agent/interfreq` at 6c12475 (`EXCEPTIONAL_INTERFREQ.md`,
`reviews/agent-reports/AGENT_REPORT_O18.md`, `scripts/interfreq_*.py`,
`data/interfreq/`). Context read: KARY2 Thm 5.1/5.2, Cor 6.1; THETA Lemma 2.9;
NONCRT Prop 2.1, Thm 2.3, Cor 2.4/2.5, §§2.4–2.5, Thm 8.1, Lemma 8.2,
Cor 8.3; DISCOVERIES (D)15, (D)18, (D)19.

Reviewer check: `reviews/exceptional-interfreq-review-check.py` (output
quoted below). Both author scripts were re-run. The output is byte-identical
to `data/interfreq/selberg_check.txt` and `hitpattern_lp_N3000_m12.txt`.

## Verdicts

| item | verdict |
|---|---|
| Obs 1.1, Lemma 2.1 | SOUND |
| **Thm 2.2** | **SOUND** (checks 1–4 below) |
| **Cor 2.3** | **SOUND**. Arbitrary coefficient sizes are legitimate (check 5) |
| Lemma 2.4 | SOUND (constant 6 at D = N/2 verified) |
| **Thm 2.5** | **SOUND as stated**. The case split and the mean side are correct (check 6). The *scope* claims built on it overreach (D1) |
| Prop 3.1, 3.2 | SOUND (finite LP duality; concavity of a minimum plus Jensen) |
| §3.2 numerics | Replayed identically. One sentence is false (D5) |
| §3.3 | Not a proof. The label "PROVED (reduction)" is too strong (D6) |
| Lemma 4.1, 4.2 | SOUND |
| §5 | (i) inherits D1. (ii) and (iii) are fair Assessment |

## Checks that passed

1. **Direction of Thm 2.2.** The theorem gives a *lower* bound on the
   interval sum: `Σ_{n≤N}ν ≥ Σ_n F(n)ν(n) = (N−D)Eν`. It uses `F ≤ 1_{[1,N]}`
   at every integer (`I = [1/2, N+1/2]`) and `ν ≥ 0` at every integer. Any
   valid upper bound B satisfies `B ≥ Σ_{n≤N}ν`, so B is ≥ the same quantity.
   This is the direction a cap needs.
2. **Support and decay.** F̂ is continuous and supported in `[−δ, δ]`, so
   `F̂(±δ) = 0`. For `den(θ) = q ≤ D` and θ ∉ ℤ we get `|k − θ| ≥ 1/q ≥ δ`,
   so the periodised sum vanishes. This covers the edge case q = D. Absolute
   summability of `F(n)` follows from Plancherel–Pólya for L¹ functions of
   exponential type, or from the explicit `O(x^{−2})` decay of Selberg's
   function. That justifies pointwise Poisson and the interchange with the
   finite sum ν. The constant `F̂(0) = |I| − δ^{−1} = N − D` is Vaaler's
   (Bull. AMS 1985, §6).
3. **Numerical reconstruction.** The reviewer script builds F from
   Beurling's B as `F(x) = −½[B(δ(α−x)) + B(δ(x−β))]`, with δ = 2/N:
   * `Σ_n F(n) = 10.00013` (N = 20) and `25.00032` (N = 50), against N − D
     (truncation error only);
   * `F ≤ 0` off [1,N], up to 4·10⁻¹¹.
4. **Author LP check** (`interfreq_selberg_check.py`, D ≤ 8). It is exact
   and passes, but it is weak evidence: the LP minima exceed N − D by a
   wide margin. The proof does not rely on it.
5. **Cor 2.3 and coefficients.** Neither input involves coefficients:
   * Thm 2.2 has no coefficient dependence;
   * KARY2 Thm 5.1 bounds Eν for *every* majorant of level λ;
   * Lemma 2.1(b) gives level ≤ log D.

   So `B ≥ Σ_{n≤N}ν ≥ (N−D)Eν ≥ (N/2)e^{−Cλ^{3/4}(log λ)^{3/4}}` with
   λ = max(log N, λ₀). The saving is measured against N, through the
   proved lower bound `(N − D)Eν`. No Σ|a_i| budget is needed, and none is
   needed on family primes: Thm 5.1 allows arbitrary moduli, and no level
   coarsening is required. Lemma 2.1(a)'s converse uses complex
   coefficients; take real parts.
6. **Thm 2.5.**
   * *Interval side.* Lemma 2.4 is correct: `#{k ≠ 0 : |k| < d/D} ≤ 2d/D`,
     `‖F‖₁ ≤ N + D`, and the error is 0 for d ≤ D. At D = N/2 this gives
     `ΣFν ≥ (N/2)Eν − 6T_>`.
   * *Case split.* For `s > log(2+12c)` we get `T_> ≤ cB < N/12`, hence
     `log max(T_>,1) ≤ log N`. This is the only place the split is used,
     and it is correct.
   * *Projection to the family modulus.* `d ↦ gcd(d, Q)` cannot raise a
     level, and it scales coefficients by `d'/d ≤ 1`. So the terms of ν̄ of
     level `> log(N/2)` come from terms with `d_i > N/2`, and their mass is
     ≤ T_>.
   * *ET Lemma 2.9.* Its proof changes only the terms of level > λ, so the
     mean increase is ≤ `T_> e^{Λ₀−λ} ≤ e^{−S}`, including when T_> < 1.
   * *Bootstrap.* KARY2 Cor 6.1's bootstrap applies verbatim with
     `λ ≤ (A+1)log N + S + λ₀`.
   * *Constants.* N₀ and C_A are independent of c, as claimed. K2 Cor 6.1
     is the case c = 1, because `N·Eν + Σ|a_i| ≥ Σ_{n≤N}ν` termwise.
7. **Lemma 4.1.**
   * `s_ℓ = log(3/(8p⁺))` gives `2p ≤ (3/4)e^{−s}`. Also
     `Πp ≤ Π(4/3)p ≤ Π2p(1−p)` because p ≤ 1/4.
   * The tails are therefore `≤ e^{−λ}N^A Σ|d_S|M_S ≤ e^{−λ}N^{A+1}` (using
     `B_Φ < N`), which is 1/N at λ_A. Then NC Cor 2.4 applies.
   * (H_eq^A) is a genuine weakening of NC (2.6) at λ ≍ log N.

   **Lemma 4.2.** `y^S` has transform `Π 1̂_{F_ℓ}(h_ℓ)` on Θ_S. The bound is
   the triangle inequality, so the lemma is correct.

## Defects

**D1 (MAJOR, scope; Thm 2.5 itself unaffected).** The file claims that
Theorem 2.5 contains "every *hybrid* method". The claim appears in the Scope
bullet 3 under Thm 2.5, in the Verdict's gloss, in §5(i) ("any evaluation …
together with trivial charging above N/2, is capped"), in the summary row
for §5, in AGENT_REPORT item 3 and in its suggested ledger text. The method
in question evaluates classes of modulus ≤ N/2 in any way and charges each
class of modulus > N/2 its trivial count `N/d_i + O(1)` per unit
coefficient. **This is not proved.** Theorem 2.5 needs hypothesis (2.2),
`T_> ≤ cB`, and nothing shows that the hybrid bound satisfies it with a
c small enough to keep the cap (D4).

Exactly, with `r_i = #{n≤N: n≡b_i (d_i)} − N/d_i ∈ (−1,1)`:

    B_hyb = Σ_{n≤N}ν_≤ + N·Eν_> + T_> = Σ_{n≤N}ν + Σ_{d_i>N/2} (|a_i| − a_i r_i).

The last sum can be ≪ T_>. It is about `a_i N/d_i` for a positive
coefficient on a class with `d_i ≫ N` that meets [1,N] (`r_i = 1 − N/d_i`).
The Selberg bound `Σ_{n≤N}ν ≥ (N/2)Eν − 6T_>` is then useless. There is a
second gap: for such methods nothing bounds `log T_>` by `O(log N)`, and the
mean side (ET Lemma 2.9 at `λ ≥ Λ₀ + log T_> + S`) needs exactly that. No
counterexample has been constructed. In natural sieves, positive
large-modulus terms typically miss [1,N] and are charged ≈ |a_i|. This is a
proof gap, not a refutation.

*Repair (minimal).* State the hybrid class as "hybrid methods whose bound is
≥ T_>/c". The Verdict paragraph already phrases it this way ("whose bound
dominates a fixed multiple of the coefficient mass"), but Scope/§5(i)/the
report do not. Alternatively, prove the inclusion. A route, with numerics
only: by the reviewer script, F ≥ 0 on [1,N] (min 0.054 at N = 20, 0.021 at
N = 50). Also `G(b,d) := Σ_{n≡b (d)}(1_{[1,N]} − F)(n) ≤ 1 + N/(2d)` for all
`N < d < 40N` (max excess −0.066 and −0.033). That gives
`B_hyb ≥ (N/2)Eν − ½Σ_{a_i>0, N/2<d_i≤N} a_i`: the excess reaches 0.39/0.46
only for d ∈ (N/2, N], where a class has two points in [1,N]. Even so, the
mean side still needs `T_> ≤ N^{O(1)}`.

**D2 (minor).** T_> is representation-dependent, and the "door"
statements are phrased as if it were intrinsic. Any class of modulus ≤ N/2
splits into k classes of modulus kd > N/2 without changing ν, which inflates
T_> arbitrarily. Thm 2.5 is valid for every representation, so it should be
applied with `T_>^* = inf_{repr} Σ_{d_i>N/2}|a_i|`. The sentence "escapes
Theorem 2.5 only if B ≪ T_>" (and §3.3's "error far below T_>") should read
`B ≪ T_>^*`. The same applies to (2.3)/(3.2): how the sum splits between
the two parts depends on the representation.

**D3 (minor).** "Thm 2.5 contains Cor 2.3 (T_> = 0)" is not literally
true. Cor 2.3 has no bound on family primes ("any primes"). Thm 2.5 assumes
primes ≤ N^A, which it needs only for Λ₀ in Lemma 2.9, and that step is
idle when T_> = 0. It contains Cor 2.3 only for such families. Restate the
inclusion or drop the prime hypothesis when T_> = 0.

**D4 (remark, not an error).** The c-parametrisation undersells Thm 2.5.
From `B ≥ (N/2)e^{−S} − 6T_>`, with S capped whenever `T_> ≤ N`, the cap
holds as soon as `T_> ≤ (N/24)·exp(−C(log N)^{3/4}(log log N)^{3/4})`,
whatever B is. So "a fixed multiple" in the Verdict can be any
`c ≤ exp(O((log N)^{3/4}(log log N)^{3/4}))` without changing the order of the cap. The binding quantity is T_>/N, not T_>/B.

**D5 (minor, numerics text).** §3.2 says "[1,N] is never the best of the
three", and AGENT_REPORT item 8 repeats it. This is false: at Q = N, [1,N]
saves the most (1.6713 vs 1.6690, 1.6642), and at Q = N^{3/4} it ties for
best (1.3496). Also, "within 0.005 … (consistent with Theorem 2.2)" is
vacuous at Q = N, since D = N gives N − D = 0. Thm 2.2 constrains the table
only for Q < N; at Q = N^{1/2} it allows an excess ≤ 0.018. The squares
explanation of the void excess is plausible but unverified (54 squares ≤
3000 against an excess of about 25 voids); label it as such.

**D6 (minor, labels/scope).** The §3.3 "reduction" is labelled PROVED, but
it is not a theorem. "Must evaluate (3.2) with error far below T_>" is a
reading of the contrapositive of Thm 2.5, and it inherits D1 and D2. It
also combines Thm 2.5 (KARY2 mixtures) with NC Thm 8.1 and Cor 8.3
(prime-slice / Case-B hit-pattern families only), which have different
scopes. Label it Assessment. Similarly, in the discussion after Prop 3.2,
"for the full ES family … `e^{−c(log N)^3}`" is a heuristic (a CRT product
over composite-modulus classes is not `Π(1−p_ℓ)`) placed inside PROVED
text. Label it heuristic.

**D7 (cosmetic).**
* (a) §5(ii) uses "8B²" without defining B. It is NC Lemma 8.2's
  `⌊(N+1)/3⌋`, which clashes with B (the bound) in Thm 2.5 and with B in
  Thm 5.2.
* (b) Thm 2.2 Remark (ii): the large-sieve constant `N − 1 + δ^{−1}` comes
  from the *majorant*. The minorant here has `|I| − δ^{−1}` with
  `|I| = N` (half-integer endpoints).
* (c) The `interfreq_hitpattern_lp.py` docstring contains a literal `\n`.
* (d) AGENT_REPORT proposes ledger entry "(D)19", but (D)19 already exists
  (large sieve). The new entry should be (D)20, and its text must carry the
  D1 restriction.

## Reviewer-check output

```
N=20: sum F=10.00013 (N-D=10.0), min F on [1,N]=0.0536, max F outside=-1.99e-11
   d in [11,21): max G-1-N/(2d) = 0.3908 at (d,b,G)=(19, 1, 1.917)
   d in [21,800): max G-1-N/(2d) = -0.0661 at (d,b,G)=(799, 1, 0.946)
N=50: sum F=25.00032 (N-D=25.0), min F on [1,N]=0.0206, max F outside=4.11e-11
   d in [26,51): max G-1-N/(2d) = 0.4586 at (d,b,G)=(49, 1, 1.969)
   d in [51,2000): max G-1-N/(2d) = -0.0331 at (d,b,G)=(1999, 1, 0.979)
```

## Overall

**SOUND-WITH-REPAIRS.** The mathematical core is correct: Thm 2.2, Cor 2.3,
Lemma 2.4, Thm 2.5 as stated, Props 3.1/3.2 and Lemmas 4.1/4.2. Cor 2.3
legitimately closes level-≤ N/2 majorants with arbitrary coefficients and
any evaluation of the interval sum. One repair is required before ledger
entry: D1. "Every hybrid method with trivial charging above N/2" is *not*
proved to be capped. Only methods whose bound dominates T_>/c are capped
(and, per D4, c may be as large as `exp(O((log N)^{3/4}(log log N)^{3/4}))`). D2–D7 are
wording and label fixes.
