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
| LS consistency / refutation attempts | pending |
| N2 (W(133050918961)=5935, hard) | pending |

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

## Defects

(numbered list follows)
