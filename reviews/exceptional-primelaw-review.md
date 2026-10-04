# Hostile review: EXCEPTIONAL_PRIMELAW.md (task O22, branch `side-agent/primelaw` @ 43f6f32)

Reviewer branch: `side-agent/review-primelaw`. Context files read: K2 (all), EK §§1–4,
ETw §§1.2, 2.1–2.2′, 4.1–4.3, NC §3, ET Lemma 2.9 (via K2 Cor 6.1). Subject replay
`scripts/primelaw_checks.py` reproduced byte-identically (20 s). Independent checks:
`scripts/review_primelaw_checks.py` → `data/primelaw/review_checks.txt`.

## Verdicts

| item | verdict |
|---|---|
| Lemma 1.2 (Dirichlet reduction) | SOUND |
| Lemma 1.3 (E* is a product) | SOUND (brute-force check (b)) |
| Lemma 2.1 (unit-square base, R-term `(π(W)+1)log 2`) | SOUND; comparison remarks wrong (D1) |
| Prop 2.2 (EK Thm 4.1 / ETw Thm 2.3′ under E*) | SOUND |
| "Arithmetic-free" steps: singleton, EK Thm 2.5/Cor 2.6, ETw Lemma 4.2/Cor 4.3, above `e^λ`, leak | SOUND |
| Lemma 2.3 (γ*; four properties) | SOUND (algebra re-derived) |
| Lemmas 2.4–2.5 (moments, leak) | SOUND |
| Thm 3.1 | SOUND (Case A via ElT Prop 1.4, as K2) |
| Lemma 4.1 | SOUND (projection checked by brute force, (a)) |
| Cor 4.2 | SOUND as stated; scope comments overreach (D2, D3) |
| Prop 4.3 (GRH) | SOUND (conditional) |
| §4.4 | SOUND; wording (D5) |
| §5 numerics | reproduced; consistent |

**Overall: SOUND.** The transfer to the unit measure works. No defect affects
Thm 3.1, Cor 4.2 or Prop 4.3 as stated. All defects below are wording or scope.

## Checks of the hot spots

**Arithmetic-free transfer.** I checked each ingredient against its source.
* EK Thm 2.5, Lemmas 2.1–2.4 and Cor 2.6 are stated for any finite alphabets and
  any product law `⊗ν_ℓ`. Lemma 2.4's "if ν(x)=0 both sides vanish" holds
  trivially, since `U*` has full support on `Ω*`.
* Cylinder patterns: a class mod `ℓ^v` meets `Ω*_ℓ` in a union of single
  letters, which is empty if the residue is a non-unit. A pattern with a
  non-unit requirement at any coordinate is therefore void. That only removes
  constraints.
* EK Thm 4.1 / ETw Thm 2.3′. The proof needs `g_j ≥ 0` only on the support of
  the law (units), and `E*ν = E_{(ℤ/Q₀)^×} g_1 ≥ (|R|/φ(Q₀))E_R g_1` needs only
  `R ⊆ (ℤ/Q₀)^×`. λ-locality of `f = g_{j+1}(h,·)` follows from CRT
  independence under `E*`. `g_{J+1} = ν` holds because the blocks cover every
  prime `> W` of L, including those of ν's own moduli, which lie outside 𝔊.
* Singleton (`E f ≥ (1−p)E_σ f`) and the "above `e^λ`" step use no arithmetic.
* Linear (ETw Lemma 4.2): stated for finite state spaces with independent laws.
  In Cor 4.3, a marginal that is uniform on `Ω*∖F` with `U*(F) ≤ δ` has density
  `≤ (1−δ)^{-1} ≤ 1+2δ` and TV defect `≤ δ`. So the cost is unchanged.
* Leak (EK Lemma 2.1(1), ETw Lemma 2.1′): light tops are avoided by
  construction. A class whose top residue is a non-unit is never hit, since
  `Q'` lives on units. Classes whose lower residues are non-units are never
  active. The bound `𝔏 ≤ Σ E[p*1{p*>δ}] ≤ Σ ℓ^{1/2}E p*²` is unchanged.

**γ* and the moment lemmas.** With `x = ℓ^{−1/2}` one has
`γ* = 1/((1−x)(1−x²))`. The algebra gives
`γ*−1 ≤ x/(1−x)² ≤ 2x`, which reduces to `x³ ≤ x²`, and
`γ*² ≤ 1+5x` for `x ≤ 1/4`.

I went through every use of `γ'` in K2 §§3–4, EK Lemma 4.2′ and ET Lemma 3.7's
γ-clause. Each one is one of:
* `γ' ≥ 1`;
* `h ≤ 2p^{−1/2}`;
* `γ'² ≤ 1+5p^{−1/2}`;
* `γ' ≤ 3` (the pointwise bound `Γ ≤ 8·3^ω` in K2 Lemma 4.2);
* the Lemma 3.1 hypotheses for products of these with τ-powers.

All of them hold for γ*. The Euler factors at `p ≤ W` are untouched, so
`C(W) ≤ C(log W)^c` survives. In Step 1, the extra `ℓ/(ℓ−1)` is absorbed
correctly because `ℓ/(ℓ−1) ≤ γ*(ℓ)` and `ℓ ∤ q`. In Lemma 2.5, `p* ≤ 2Σ_v ℓ^{−v}N_{ℓ,v}`
costs only a factor 4.

**Non-unit classes cost nothing.** This holds in both directions.
* They impose no constraint in (1.1). This applies to selector classes, to
  (a,D)-classes with a even or with odd `ℓ | gcd(a,D)` (re-derived), and to any
  class with a non-unit residue anywhere.
* In the proof they contribute 0 to `p*`, to `N_{ℓ,v}` (where over-counting
  them is harmless) and to the leak.

The R-term identity can be verified exactly:

    unit R-term = K2 R-term − log(Q₀/φ(Q₀)) = (π(W)+1)log 2

(check (c), W up to 1009).

**Dirichlet step.** Lemma 1.2 is correct in both directions, with no family
hypothesis. Lemma 1.2 also implies something not stated in the paper: the
finite exceptional set of Def 1.1 automatically lies inside `{p | L}`. If
`ν(p) < 0` with `p ∤ L`, the whole reduced class of p, which contains
infinitely many primes, would violate the definition. So there is no
uniformity issue *for the cap*. Thm 3.1 is a statement about a finite LP, and
Dirichlet is used only to show that Def 1.1 implies (1.1). Uniformity matters
only for the relaxations in §6 item 2 (see D6).

**Cor 4.2.**
* (H1): the level is `Σ_{ℓ|d_i,ℓ>W} log ℓ ≤ A log N` directly. No condition on
  T or on 𝔊 is needed, because `Err ≥ 0` is assumed and Thm 3.1 has no family
  hypothesis. This is the correct reading for EH (moduli `≤ N^{1−ε}`) and GRH
  (moduli `≤ N`): `A = 1` suffices.
* (H2): Lemma 4.1 was checked line by line. The projection coefficient is
  exactly `φ(L)/φ(lcm)`, and `E*`-mean preservation follows from
  `φ(lcm)φ(gcd) = φ(d)φ(L)` (brute force (a)). In the coarsening step, the rise
  is `≤ |a|/φ(r)`, with `r > e^{λ−Λ₀}` and `r/φ(r) ≪ log λ`. The case analysis
  closes.

**Prop 4.3.** I re-derived the GRH conversion `ψ → π` and found the error
`O(√x log x)`. The trivial range `q > x` costs `O(1)` per unit coefficient. The
total error is `O(T√N log N) ≤ N^{1−ε}log N`, which is `o(li(N)E*ν)` by
Thm 3.1. Correct.

## Defects

**D1 (minor; false comparison, §2.1 after Lemma 2.1, and Remark 3.2 last
sentence).**
* The sentence "and smaller than NC Thm 3.2's `log(P/φ(P))`-type selector
  term, which is 0 here …" contradicts itself.
* Remark 3.2 says NC's R-term "is replaced by the absolute `(π(W)+1)log 2`" as
  if this were an improvement.

NC Thm 3.2 states that under `E*` a selector base has R-term **0**. The unit
R-term here, `(π(W)+1)log 2 ≈ W·log 2/log W`, is *larger* than that. The
increase is the price of (R1) against forced W-smooth classes, which NC's
prime-slice setting handled differently. The correct comparison is the exact
identity: unit R-term = K2 R-term − `log(Q₀/φ(Q₀))`. Fix the wording. This
has no effect on any theorem.

**D2 (minor; scope of the headline, Cor 4.2 parenthetical, §4.2 bold line,
AGENT_REPORT ledger wording).**
* The bold line reads "prime-law methods … cannot give θ > 3/4 at any
  equidistribution level `N^{O(1)}`".
* The suggested DISCOVERIES text reads "capped … for any equidistribution
  level".

Both drop the two hypotheses that carry the result:
* `Err ≥ 0`, i.e. absolute-value error accounting;
* global positivity: Def 1.1 requires `ν(p) ≥ 0` at *all* primes, not only at
  `p ≤ N`.

The second hypothesis has teeth exactly in the EH/GRH regime. When the level
is `≍ log N`, L is far larger than N, and most reduced classes mod L contain
no prime `≤ N`. So "ν(p) ≥ 0 for `p ≤ N`" is a strictly larger class of
majorants. §6 item 2 lists this exclusion, but the headline and the ledger
wording must state both qualifiers. Suggested ledger text: "… prime majorants
in the sense of Def 1.1 (nonnegative at all primes), with error terms bounded
in absolute value (Err ≥ 0), at any level `N^{O(1)}` …".

**D3 (minor; validity side of (4.1)).** The parenthetical "This is the form of
every method that evaluates `Σ_{p≤N}ν(p)` …" omits a correction. For
`#(𝒜 ∩ primes ≤ N) ≤ Σ_{p≤N}ν(p)` to hold, one must add
`Σ_{p|L, p≤N}(1+|ν(p)|)`, because ν may be negative, or below 1, at primes
dividing L. NC Lemma 3.1 recorded this correction as `O(ω(L) max|ν|)`.
* Here `ω(L)` is unbounded. With selector classes or large families it can be
  `≥ π(z)`.
* The term only enlarges Err, so the cap is unaffected.
* State it, and state the observation above that the Def 1.1 exceptions lie
  in `{p | L}`.

**D4 (minor; notation).** Def 1.1 defines the level with "W the absolute
constant [of K2 Thm 5.1]". But §2 fixes its own W ("enlarged below if
needed", `W ≥ W₀*` in Lemma 2.5), and Thm 3.1 asserts its own absolute W. The
level must be defined with Thm 3.1's W. Alternatively, note that changing W
shifts the level by at most `θ(W) ≤ 2W`, which is absorbed into λ₀ and C.

**D5 (cosmetic).**
* Prop 2.2 lists the linear cost as `2log(1+3e^{−λ/4})`, which already
  includes the factor 2 of the theorem. The singleton cost `(4/3)p*` is listed
  without the factor 2. Thm 3.1's ledger is correct; make Prop 2.2 consistent.
* §4.4 says "with **no** `(log log N)²` loss … no extra term". For
  unbounded-B mixtures, K2 Thm 5.1 still carries `(log λ)^{3/4}`, so "no
  extra term" means "nothing beyond K2's own cap". For NC Thm 3.3's original
  ET Cor 3.4 families (`B = C < 1`), K2 Thm 5.2 applies, and there is indeed
  no loss at all. Also, K2 Cor 6.1's reading needs `z ≤ N^A`. Say so.

**D6 (suggestion, not a defect; §6 item 2).** Linnik's theorem (Xylouris: the
least prime in a reduced class mod q is `≪ q^5`) closes both finite-range
relaxations when `L ≤ cN^{1/5}`. Under GRH (Bach–Sorenson: least prime
`≤ 2(q log q)²`), they close when `L ≲ √N/log N`. In those ranges, "`ν(p) ≥ 0`
for `p ≤ N`, `ν(p) ≥ 1` on `𝒜 ∩ primes ≤ N`" implies Def 1.1. The regime is
narrow, because L contains every family modulus, so this is only worth a
sentence. It does show that the gap in D2 lives entirely at `L > N^{c}`.

## Replay

```
cd scripts
uv run --with sympy --with scipy --with numpy python -u primelaw_checks.py 1000000 2   # == data/primelaw/checks.txt
uv run --with sympy python -u review_primelaw_checks.py > ../data/primelaw/review_checks.txt
```
