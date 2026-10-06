# Hostile review R61 of POINTWISE_OMEGA16.md (O61, branch side-agent/third-conditional)

Reviewer branch: side-agent/review-omega16. Author files merged at 58cb47e. Scripts: `scripts/review_o16_*.py`.

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| Thm 1.2 (LS ⇒ 1/3 i.o., Mordell-hard) | SOUND (minor citation precision, m1) |
| §5.4 no uniform upper companion | SOUND |
| Prop 4.1(a) | SOUND |
| Prop 4.1(b) (BDH) | SOUND (re-derived; BDH π-form on `(x/2,x]` is a routine corollary) |
| Cor 4.2 | SOUND |
| Prop 2.1(a) | SOUND |
| Prop 2.1(b) | Assessment correctly labelled |
| Prop 3.1 | pending |
| LS consistency / refutation attempts | not refuted; one cheap PROVED special case and a sharper heuristic found (below) |
| N2 (W(133050918961)=5935, hard, least) | CONFIRMED from scratch |

## Claim-by-claim

### Thm 1.2
Re-derived. 𝓔_T = all atoms `M≤T` plus the non-square unit classes mod 840. All events are unit
classes (`gcd(4D,M)=1` since `gcd(M,4A)=1`, `D|A²`). The good realisation `(Q,r)` from the *proof*
of O13 Thm 3.4 (not its statement, which is normalised on `n≡1 (24)` and does not by itself give
squareness mod 5, 7) has `840|Q`, r a square mod 840, and `E_{rH}F≥exp(−(4/3)S_res)`; dead atoms
(`M|Q`, or `−4D≢r mod gcd(M,Q)`) are empty on rH by O13 Lemma 3.1 / by definition. So
`δ(𝓔_T)≥φ(Q)^{−1}exp(−(4/3)S_res)` and `log(1/δ)≪𝓛³(log𝓛)^5`. LS gives `p>T` avoiding 𝓔_T: p is a
square mod 840 (Mordell-hard), and no atom `M≤T` has `p≡−4D (M)`, so `W(p)>T` (including the case
`W(p)=∞`). Inversion: `log p≤K𝓛³(log𝓛)^5`, `𝓛≤log p` ⇒ `𝓛≥(log p/K)^{1/3}(log log p)^{−5/3}`.
Distinctness i.o.: `p_T>T`. The "for every large T" needs O13's range condition (`T≥e^{33}`, O13 §5
Setting), harmless. No circularity: LS is applied to one explicit system per T.

### §5.4 (no uniform upper companion)
Re-derived. For prime `p_0∈(T,2T]`, `p_0` is a unit mod every `m≤T`, so keeping only `p_0 mod m`
uses unit-class events; avoider set = one class mod `L=lcm(1..T)`, `log φ(L)=(1+o(1))T`.
`π_𝓔(2T)≥1` but `2T·e^{−(1+o(1))T/C}T^C<1` for large T. PROVED, sound. (The "would imply ES"
aside depends on the lower bound `log(1/δ*)≫𝓛³/log𝓛` of POINTWISE_HAAR Thm 2.1; not re-checked,
but it is only motivation.)

### Prop 4.1(a)
Re-derived. Atoms with all primes `≤y`: `n∈S` is a square mod every prime of M, so Jacobi
`(n|M)=1≠−1=(−4D|M)` (O13 Lemma 3.1(b)). Every other atom has a unique prime `ℓ>y≥√T`, exponent 1.
`|B_ℓ|≤Σ_{v≤T/ℓ}τ(A_{vℓ}²)≤T^{1/2−ε+o(1)}≤ℓ/2`; tail `Σ_{ℓ>y}T^{1+o(1)}ℓ^{−2}≤T^{1/2−ε+o(1)}`.
`S⊆F_T^{MH}`: `1 mod 8` and squares mod 3,5,7 ⇒ square mod 840. Sound.

### Prop 4.1(b)
Re-derived line by line.
* `ℓ∈(x/2,x]`, `ℓ^2≤T` so `e_ℓ=2` is possible; the projection `Ā_ℓ` handles it
  (`|A_ℓ|/φ(ℓ^e)≤|Ā_ℓ|/(ℓ−1)`). Distinctness of `−4q mod ℓ` for primes `q<ℓ`: yes (ℓ odd).
* Atom: `ℓ_1≡1, ℓ_2≡3 (4)` ⇒ `M≡3 (4)`; `ℓ_1ℓ_2≡c·(−c^{−1})=−1 (q)`; q odd so `4q|M+1`, `D=q|A|A²`.
  `ℓ_1≠ℓ_2`. CRT-product ⇒ `S∩E_{M,q}=∅` iff `−4q∉Ā_{ℓ_1}` or `∉Ā_{ℓ_2}`. The dichotomy and the
  min-inequality `min(u,v)≥(u+v)/2−(|e_u|+|e_v|)/2` are correct; each class mod 4q is used once.
* BDH: ψ-form `Σ_{m≤R}Σ_a(ψ(y;m,a)−ψ(y)/φ(m))²≪yR log y+y²(log y)^{−A}` transfers to π on
  `(x/2,x]` by partial summation + Cauchy–Schwarz in the Stieltjes integral, centring at the
  empirical mean only lowers the variance, restricting to `m=4q` only drops terms. The author's
  bound `xQ log x` for the π-form is weaker than the truth (`xQ/log x`) — harmless.
* With `Q=x(log x)^{−6}`: error `≪Qx(log x)^{−5/2}` vs main `≍Qx(log x)^{−2}`; any `Q≤x(log x)^{−5−ε}`
  works. `log(1/δ)≥x^{−1}Σb_ℓ≫Q(log x)^{−2}`. Sound. BDH is a theorem (Siegel–Walfisz, ineffective
  constant), so "PROVED modulo BDH" is just "PROVED (ineffective)".
* Robustness: the lower bound uses only primes in `(√T/2,√T]`, so it also holds for product sets
  that impose extra conditions at primes `>T` (i.e. applying HL_prod with a larger parameter T′
  cannot escape Cor 4.2(b)). Worth stating.

### Cor 4.2 — sound (direct from 4.1(a) + LS on a product system with moduli `≤T`: 8, ℓ, `ℓ≤T`).

### Prop 2.1(a)
`Φ(x,z)/(δx)→e^γω(u)`; `ω(2)=1/2`; zeros of `e^γω(u)−1` are discrete because ω is analytic on each
`[k,k+1]` and not constant there (`uω′(u)=ω(u−1)−ω(u)`, induct down to `ω=1/u` on `[1,2]`). Sound.
(It is an integer analogue with the non-unit class 0, as the author says.)

### N2 (from scratch, `scripts/review_o16_esleast.py`)
* `W 133050918961`: prime (MR, 12 bases, deterministic below 3.3e24), `≡121 (840)` a square,
  `W=5935` with `D=16` (`A=1484`, `16|A²`), by direct divisor search over all `M≡3 (4)`.
* `scan 4095 1 1e9` and `scan 4095 3e9 133050918962`: atom sieve over the 6 square classes mod 840,
  then MR on survivors: the *only* prime with `W>4095` below `1.3305·10^{11}` is `133050918961`
  ([1e9,3e9) also scanned: none). So it is the least hard prime with `W>4095`. (The table's
  "p≡1 (24)" normalisation agrees with "square mod 840": the other classes in `1 (24)` are killed by
  the atoms M=7, 15.)
* Earlier rows reproduced: least p for T=31,127,511,1023,2047 = 2521, 33289, 2031121 (×3);
  `W(2031121)=2495` (D=576); count of hard `p<10^{11}` with `W>2047` = 107 (author: 107).

### LS: refutation attempts (brief: "it quantifies over ALL unit-class systems")
1. *Single class mod `L=lcm(m≤T)`* (`log(1/δ)=(1+o(1))T`): LS = Linnik for modulus L, true with
   `C≈5` (Xylouris), the `p>T` requirement via Linnik's lower bound `π(x;q,a)≫x/(φ(q)√q log x)`.
   Same for every single-class reduction: no contradiction with Linnik.
2. *Jacobsthal (shifted)*: a gap `(a,a+y)` in the integers coprime to `P(z)` with `gcd(a,P(z))=1`
   is a covering of `(0,y)` by one unit class `−a` mod each `ℓ≤z`; `δ≍1/log z`, `y=z^{1+o(1)}`
   (Ford–Green–Konyagin–Maynard–Tao size). LS with `C>1` absorbs it. Long gaps in sieved sets with
   bounded `|I_p|` (Ford–Konyagin–Maynard–Pomerance–Tao, JEMS 2021) are also `z^{1+o(1)}`. No
   contradiction.
3. *The real danger* is the sieve-limit gap. The lower-bound sieve guarantees an avoider only for
   `log x≫κ_eff log T` where, for events concentrated on primes `ℓ∈(T/2,T]`,
   `κ_eff≍log T·log(1/δ)`, i.e. `log x≫(log T)²log(1/δ)`, while LS claims `log x≪log T+log(1/δ)`.
   So I attacked exactly that regime: `scripts/review_o16_adversary.py` (from scratch): moduli the
   primes in `(T/2,T]`, k unit classes each, greedy (kill the least surviving prime `>T` through the
   modulus whose class holds most surviving primes in a look-ahead window), exact
   `δ=∏(1−k_ℓ/(ℓ−1))`.

   | T | k | log(1/δ) | p_min | LS ratio | `δp/log p` |
   |---|---|---|---|---|---|
   | 300 | 1 | 0.13 | 463 | 1.05 | 66 |
   | 300 | 4 | 0.51 | 1171 | 1.14 | 99 |
   | 300 | 16 | 2.12 | 31337 | 1.32 | 365 |
   | 300 | 32 | 4.42 | 334991 | 1.26 | 317 |
   | 300 | 48 | 6.96 | 4028851 | 1.20 | 253 |
   | 300 | 64 | 9.77 | 71138569 | 1.17 | 224 |
   | 300 | 96, 128 | 12.6, 13.3 | `>10^9` | `>1.13`, `>1.09` | — |
   | 1000 | 4 | 0.41 | 3989 | 1.13 | 320 |
   | 1000 | 16 | 1.64 | 64373 | 1.30 | 1124 |
   | 1000 | 64 | 6.82 | 12935291 | 1.19 | 864 |
   | 1000 | 128 | 11.15 | `>10^9` | `>1.15` | — |

   The adversary gains a factor `≈T^{1.0}` over the random-set prediction (`δp/log p≈T`) and *no
   factor growing with the dimension k*; the LS ratio peaks ≈1.3 and then falls. Different
   adversary from the author's N3 (all primes `3..z`); same conclusion. EVIDENCE only.
4. *Sharper heuristic (suggested addition).* Model the primes in `(T,x]` as `π(x)` independent
   Haar points of `Ẑ^×`. The number of unit-class systems with moduli `≤T` is
   `≤2^{Σ_{m≤T}φ(m)}≤2^{T²}`; a fixed system with density δ misses all points with probability
   `≤e^{−δπ(x)}`. Union bound: *simultaneously for all systems*, an avoider exists once
   `δπ(x)≫T²`, i.e. `log x≥log(1/δ)+(2+o(1))log T` — CR(2+o(1)), hence LS. This replaces the
   vague "log-scale random-set model" by a uniform-over-all-systems statement, predicts `A≈2`, and
   matches the adversarial gains `≈T` seen in item 3 and in N3.
5. *A PROVED special case (suggested addition).* By Brun–Titchmarsh,
   `#{p≤x: p in some event}≤Σ_E 2x/(φ(m_E)log(x/T))`. Hence if the total event mass
   `Σ_E1/φ(m_E)≤(1−ε)/2`, there is an avoiding prime `p∈(T,T^{C(ε)}]`: LS holds unconditionally for
   "light" systems. (ES systems are far from light — mass `≍log(1/δ)·`overlap — so this is only a
   sanity check, but it shows LS is a theorem at the bottom of its range.)
6. Siegel zeros (§5.2) and Maier irregularities: absorbed as the author says. In §5.2 the argument
   needs a prime `>T` in `{χ_1=1}`, which Linnik's *lower bound* (not the least-prime statement)
   supplies at `x=T^{O(1)}`; fine.

Verdict: LS is not refuted by any construction I could find; label CONJECTURE (Assessment:
plausible) is honest.

### N1 (from scratch, `scripts/review_o16_buchstab.py`)
At `x=10^8`, `u=2`: counts 440107, 55545, 4756 and ratios 0.950, 0.910, 0.881 for H=(2),(2,6),
(2,6,8) — identical to `data/omega16/buchstab_1e8.txt`. Note the shift 6 gives the class `0 mod 3`,
not a unit class; it is vacuous for primes `p>3` and must be dropped from δ (the author's δ does
this correctly; my first run did not, δ=0). Mention it, since Def 1.1 requires unit classes.

## Defects

(numbered list follows)
