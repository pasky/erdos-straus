# Hostile review of EXCEPTIONAL_KARY2 (branch side-agent/kary-no-b @ be227df)

Reviewer brief: break Theorem 5.1 (3/4 cap, no B, all three forced-class
types) and Cor 6.1 ("no θ > 3/4"). Inputs re-read: EK Thms 2.5/4.1/4.5,
Lemmas 4.2/4.2′/4.3; ETw Lemmas 1.1, 1.3, 2.1′, 2.2, 2.4, 2.6, 4.0, Prop
4.1, Cor 4.3, Thm 2.3′; ET Lemmas 2.9, 3.1, 3.2, 3.7, Cor 3.4, §4; ET
Prop 1.4 checked against `sources/elsholtz-tao-1107.1010.pdf` (l. 318–321
of the text dump: `Σ_{a≤A}Σ_{b≤B}τ(kab²+1) ≪ AB log(A+B) log(1+k)` for
`k ≪ (AB)^{O(1)}`; cited correctly).

**Bottom line.** The headline survives. I found no defect in the
mathematics of Theorems 5.1, 5.2 or Cor 6.1's derivation. There is one
scope defect, D1: the selector. The architecture claim "contains the 3/4
note's majorant" is false as stated, but the repair is easy. There is
one proof-step defect, D2, in Lemma 3.2, which is local. The rest are
cosmetic or wording.

| item | verdict |
|---|---|
| (1) §1, B enters only via (B1)–(B3) | SOUND |
| (2) Lemmas 2.1–2.3, square base, R-term | SOUND |
| (3) §3 first moments without B, s₁ | SOUND-AFTER-REPAIRS (D2, D3) |
| (4) §4 second moments, leak, W absolute | SOUND |
| (5) Cor 6.1 and its scope | SOUND-AFTER-REPAIRS (D1, D4) |

---

## Item 1 — where B entered EK: SOUND

I re-traced EK Thm 4.5 through every lemma it cites.
* **Thm 2.5 / Cor 2.6.** These are arithmetic-free. No arity bound;
  d-locality comes from the level only.
* **Thm 4.1 and ETw Thm 2.3′.** Also arithmetic-free. Coordinates
  `n mod ℓ^{E_ℓ}`; E_ℓ is finite because the family is finite.
* **(B1) EK Lemma 4.2′.** Step 1 (chain rule, `ℓ^{−v}Γ(q)/q ≤ Γ(M)/M`)
  and Step 2 (Shiu, `S(x) ≪ x log²x`) are B-free. Only Step 3 uses
  `M ≤ e^{2(1+B)s}`. Confirmed.
* **(B2) ETw Prop 4.1.** The sum runs over `M ≤ e^{(1+B)s₁}`. Confirmed.
* **(B3) ETw Lemma 2.4 / 4.0.** These use `q ≤ ℓ^B` in three places:
  the pointwise `τ(A_q²) ≤ ℓ^{o(1)}`, the lcm range `m ≤ ℓ^{2B}` (the
  `(1+2B log ℓ)^9` factor), and `v ≤ 1+B` (the finite v-sum and the
  `(2+B)²`). KARY2 lists only the first. The other two are the same
  "q bounded" fact, and both disappear in KARY2 §4: the AM–GM reduction
  sums over all cofactors, and `Σ_v ℓ^{−7v/8}` converges. So the omission
  is harmless.
* **Everything else is B-free:** base (ETw Lemma 1.3), leak mechanism
  (ETw Lemma 2.1′), linear block (ETw Cor 4.3: one block prime per term,
  because each prime exceeds `e^{λ/2}`), singleton step mechanics.
  `W₀(B)` enters only through (B3).
* **"ω(M) never enters".** Correct. None of these steps counts the primes
  of a modulus.

## Item 2 — no squares, square base: SOUND

**Lemma 2.1.** (1) is ETw Lemma 1.1 plus `gcd(x,M) = 1`; correct.
(2): a perfect square `n = x² ≥ 1` in the class gives `j ≥ 1` and
`M = 4gj−1 ≡ 3 (4)`, `A_M = gj`, `D | g² | A_M²`, and `aM = n + 4D`, so
`n ≡ −4D (mod M)`. That contradicts (1). Passing from "square mod G" to
"perfect square in the class" is also correct: take `x ∈ [1,G]`, so `x = G`
is allowed. Non-unit residues are covered by this route.

**Lemma 2.2.** I re-did every step.
* `gcd(m,2rh) = 1`.
* Mod 8: y is odd, so `m ≡ −1 (mod 4)`, and `m ≡ −1 (mod 8)` when r is
  even. This kills m = 1.
* For `p | r_o`, `(−m|p) = 1`, so `(−m|r_o) = 1`.
* `−r ≡ ((2h)^{−1})² (mod m)`, so `(−r|m) = 1`.
* The reciprocity computation gives `(r_o|m) = (−1)^{(r_o−1)/2}·(−1)^{(r_o−1)/2} = 1`,
  so `(−r|m) = −1`.

The proof is correct, including `r_o = 1` and r even.

**Lemma 2.3.**
* (R1) by CRT: G W-smooth gives `G | Q₀`, and c is a square at every
  `p^e ∥ G`.
* Unit-square fractions: `(p−1)/(2p)` for odd p; `1/8` mod `2^e`, `e ≥ 3`
  (`8 | Q₀` is forced).
* The R-term is `3log2 + Σ log(2p/(p−1)) ≤ 3log2 + π(W)log3 ≤ 2W`.
* (R2) `γ(2) = 8` holds also for the marginals mod 2 and 4.
* Q₀ may be huge, since W-smooth parts are unbounded, but only the
  ratio enters.

**Brute force (my own code, independent of `kary2_square_check.py`).**
`scripts/review_kary2_squares.py` uses a per-prime-power square test that
handles non-units. The test is validated against exhaustive enumeration
for all `G ≤ 400`. No square found in:
* 600,000 (a,D)-classes (`a ≤ 200`, `D ≤ 3000`, G up to 2.4·10⁶);
* 721,989 Case-A classes (all `d ≤ 10⁵`);
* 1,070,466 ℛ(M)-classes (`M ≤ 10⁵`);
* 86,798 random large classes (`a ≤ 10⁶`, `D ≤ 10⁹`; Case A with
  `r ≤ 10⁵` squarefree, `h ≤ 10⁴`).

A direct test, which checks whether `x² ≡ b (mod G)` for `x ≤ 2G`, `a ≤ 30`,
`D ≤ 300`, found 0 hits. The control (shift by +1) finds 280/2000
squares, so the test is live. The branch's own scripts reproduce
`data/kary2/*` exactly, up to timing lines. Output:
`data/kary2/review_squares.txt`.

## Item 3 — first moments without B: SOUND-AFTER-REPAIRS

Checked line by line:
* **Lemma 3.1.** Rankin, `K^{−η} = e^{−u}` for `m > K`, and the Mertens
  sum with `p^η ≤ 1 + (e−1)log p/log y`.
* **Lemma 3.2.** The body is EK 4.2′ with `X = y^{u₀}`, giving `12³` from
  `(log X)³`. For the tail I checked:
  * Cauchy–Schwarz;
  * `Γ² ` has κ = 1 (`(1−x)^{−2} ≤ 1+5x` for `x ≤ 1/4`);
  * `g = τ(·²)²∗μ`, `g(p^k) = 8k ≥ 0`, giving `x(log x)^8`;
  * monotonicity of `e^{−u/2}u⁴` for u ≥ 8;
  * the block count `δ^{−1} = log y/log 2`.

  The total `(log y)^{5.5}u₀⁴e^{−u₀/2} = O((log log y)⁴(log y)^{−1/2})`
  is correct.
* **Lemma 3.3.** `#{D : g(D) = g} = 2^{ω(g)}`, since `v_p(D) ∈ {2k−1, 2k}`.
  Then `Γ(4ag) ≤ 8Γ(a)Γ(g)`, with κ = 1 and κ = 2. Correct, and no loss.
* **Lemma 3.4.** Correct.
  * `n_L` has ≤ 3 prime factors.
  * Greedy chunks have `c_ic_{i+1} > n^{1/4}`, so `⌊m/2⌋ ≤ 3`, `m ≤ 7`.
  * τ is submultiplicative, and `τ(n) = τ(n_L)τ(n_S)`.
* **Lemma 3.5.** Correct.
  * `X^{1/4} ≤ max(R,H)` once `max ≥ 10k`.
  * d is odd, since N is odd and `4 | k`.
  * The case split `d ≤ R` / `d ≤ H` gives the count `≤ 2^{ω(d)+2}RH/d`
    (in fact `+1` suffices).
  * The small boxes total `≤ C k^{2.5} ≤ CK`.
* **Lemma 3.6.** The body applies ET Lemma 3.7's γ-weight clause. Here the
  small primes carry `h(2) = 7` and `h(p) ≤ 2`, a finite modification. The
  tail condition `Σh(n)n^{−3/4} < ∞` is what is needed for δ = 1/2. The
  tail itself:
  * `τ(n)` pairs per `rh = n`, and `Γ(4n)² ≤ 64Γ(n)²`, so κ = 2;
  * Lemma 3.5 with `k = 4`, `2K ≥ 64`;
  * `u₀ = (c₂+8)log log y`, giving `(log y)^{−2}(log log y)^{c₂/2} = O(1)`.

  The constant is absurd but absolute.
* **s₁ choice.** With `s₁ = λ^{1/4}(log λ)^{−3/4}`, both
  `𝔐(e^{s₁}) ≈ s₁³(log s₁)³` and `λ/s₁` equal `λ^{3/4}(log λ)^{3/4}` up to
  constants. The claim that `s₁ = λ^{1/4}` would cost `λ^{3/4}(log λ)³` in
  singletons is correct. Thm 5.1's block arithmetic gives
  `(E M + 4d)/d ≤ 16K₃·16^i + 4`, which I re-derived.

**D2 (minor, proof step, Lemma 3.1).** "Since p ≤ y, `p^{eη} ≤ e^e`, so for
p ≥ 3 the terms e ≥ 2 total ≤ C(H,a)p^{−2}" is false as written. For p = 3,
`Σ_e (e+1)^a e^e 3^{−e}` diverges. The proof itself treats p = 2
correctly; the same argument works for all p.
* *Repair:* use `η ≤ 1/log y₀`, so
  `p^{−e(1−η)} ≤ p^{−e(1−1/log y₀)} ≤ p^{−0.9e}`.
* Then the e ≥ 2 terms are `≤ C(H,a)p^{−1.8}`, which is summable.

The statement is unaffected.

**D3 (cosmetic).** Lemma 3.5: the proof gives `c_q = 2^{7q+1}+1`, not `+2`;
the larger value is harmless. In Lemma 3.2, "u ≥ 1" for `log 2K ≤ 2u log y`
should read "u ≥ u₀ − δ ≥ 1".

## Item 4 — second moments, leak: SOUND

* **Lemma 4.1.** The AM–GM symmetrisation is correct:
  * `μ(q)μ(q') ≤ (μ(q)²+μ(q')²)/2` with a symmetric kernel;
  * `lcm(q, gq'') = qq''` holds for `g = gcd(q,q')`;
  * `q' ↦ (g, q'')` is injective with `g | q`, which gives the `τ(q)`;
  * the `q''`-sum is `≪_W log ℓ`, with the Euler factor at 2 equal to 9.
* **Lemma 4.2, (a,D).** `μ ≤ Σ_{ag=G/4}2^{ω(g)} ≤ τ(G)² ≤ (v+1)²τ(q)²`,
  so the sum is `(log ℓ)^{32}`.
* **Lemma 4.2, ℛ(M).** I checked:
  * A runs over the class `4^{−1} (mod ℓ^v)`, which is coprime to `ℓ^v`;
  * the Shiu range holds, since `ℓ^v < x^{3/4}` when `K ≥ 4ℓ^{v/3}`;
  * `F = τ(·²)⁴` has `F(p) = 81`, giving `(log x)^{80}`;
  * Rankin applies with y = ℓ, since `P(q) < ℓ`;
  * the short blocks are fine by the divisor bound, uniformly in v.
* **Lemma 4.2, Case A.** I checked:
  * `v_ℓ(r) ≤ 1` (r squarefree), and the pairs per q number at most
    `(v+1)τ(q)`;
  * `4 | q` holds since ℓ is odd, so `r'h' = q/4`;
  * `k = 4ℓ^{v₁+2v₂} ≤ 4ℓ^{2v}`, and `K/2 ≥ 64ℓ^{6v} ≥ k³`, so Lemma 3.5
    (q = 4) applies. This part is unconditional, as claimed.
* **Lemma 4.3.**
  * Minkowski over types and over v, with `κ = 1/4`, gives
    `ℓ^{−7/4}polylog`.
  * Markov then gives `Σℓ^{−5/4}polylog`.
  * `C(W) ≤ (log W)^c`: the only W-dependence is the Euler factors at
    `p ≤ W` in Lemma 3.1/4.1, each `1 + O(1)/p`. Shiu's and Lemma 3.5's
    constants do not see W.

  So W is absolute.

## Item 5 — Cor 6.1 and its scope: SOUND-AFTER-REPAIRS

**Derivation: correct.**
* The projection `ν̄ = E[ν | n mod Q]` turns `a1[n≡b (d)]` into
  `a(d'/d)1[n≡b (d')]`, `d' = gcd(d,Q)`, when compatible. This gives
  `ν̄ ≥ 0`, `ν̄ ≥ 1` on the Q-periodic 𝒜, `Eν̄ = Eν` and `T̄ ≤ T`. Every
  prime of every modulus of `ν̄` is then `≤ N^A`.
* ET Lemma 2.9 with `Λ₀ = A log N`, `λ = Λ₀ + log T̄ + S`, gives
  `Eν' ≤ 2Eν`. Its truncation keeps the primes ≤ W, which the level does
  not charge here. That is consistent.
* `s ≤ S` holds because the bound is `≥ N·Eν`.
* The two cases are correct: `λ ≤ 2(A+1)log N`, or `λ < 2S` with S bounded.

So the saving is `≪ (log N)^{3/4}(log log N)^{3/4}`. With bounded B it is
`≪ (log N)^{3/4}`.

*Side note on ET (not a KARY2 defect).* ET's "Consequence" after Lemma 2.9
writes `λ ≤ (A+1)log N + s` with s the saving. Lemma 2.9 actually needs
`S = log(1/Eν) ≥ s` there. ET's conclusion survives by the same case
analysis as Cor 6.1. This is the wrong-direction issue the O14
self-review flagged.

**D1 (scope; the main finding).** Thm 5.1 and Cor 6.1 require `ν ≥ 1` on
all of `𝒜(𝔊)`, the integers in none of the classes. The 3/4 note's
majorant `S_y·Q_r(H_X)` (ET §4: `R = {(c,P_y)=1}`) is `≥ 1` only on
`𝒜(𝔊) ∩ {(n,P_y)=1}`. So "This contains the 3/4 note's majorant" (§6,
"Architecture class covered") is not literally true. The same holds for
any prime-restricted (selector) majorant, i.e. the natural architecture
for prime exceptional sets. The gap is inherited from EK Thm 4.5.

*Repair (I checked that it works).* Admit **selector classes `0 (mod p)`**
for any set of primes p in Def 2.0. Then:
* For `p ≤ W`, `R_W^□` consists of units mod every `p ≤ W`, so (R1) holds.
  The no-square property is needed only for W-smooth classes of the
  three types.
* For `p > W` the class is decided at p with `q = 1`, `v = 1`. It adds
  `≤ Σ_{W<p≤y}Γ(p)/p ≪ log log y` to 𝔐(y), which is negligible against
  `(log y)³`.
* It also adds a deterministic `+1` to `N_{p,1}`. Hence `(E p_ℓ²)^{1/2}`
  grows by at most `ℓ^{−1}`, and the leak stays `≪ W^{−1/4}polylog W`.

So Thm 5.1 holds verbatim with selectors, with R-term still `≤ 2W`. This
is better than ET's `log(P/φ(P))`. §6 item 2's criterion "(i) no class
contains a square mod its modulus" should accordingly be stated for
W-smooth classes only.

**D4 (wording).** Cor 6.1's statement is correctly qualified: "no *such*
method". Two other passages are not:
* the summary table's bold "**no θ > 3/4**";
* AGENT_REPORT_O14: "So no θ > 3/4 is possible."

Both should say "for nonnegative CRT majorants of avoider sets of
ℛ(M)/(a,D)/Case-A[/selector] families, with rounding `Σ|a_i| < N`,
family primes `≤ N^{O(1)}`". §6 "Still excluded" item 3 lists the methods
outside this class, and it should be cross-referenced from both places.
That list covers signed rounding, majorants ≥ 1 only on primes using
prime equidistribution, non-forced small-modulus sets R, and slice primes
`> N^{O(1)}`.

## Defect list

1. **D1** (scope): no selector in Thm 5.1/Cor 6.1; the claim "contains
   the 3/4 note's majorant" is false as stated. Easy repair, above. Apply.
2. **D2** (proof step): Lemma 3.1, `p^{eη} ≤ e^e` does not give convergence
   for small p. One-line repair. Apply.
3. **D3** (cosmetic): `c_q` off by one; "u ≥ 1" justification.
4. **D4** (wording): unqualified "no θ > 3/4" in the §0 table and the O14
   report.

None of these touches the exponent. **Theorem 5.1 stands** (Case A modulo
ET Prop 1.4; ℛ(M)+(a,D) unconditional). After D1, it covers the 3/4
note's selector architecture.

## Replay

```
cd scripts
uv run python review_kary2_squares.py 200 3000 100000 100000   # ~15 s
uv run python review_kary2_squares_random.py                   # ~5 s
```
