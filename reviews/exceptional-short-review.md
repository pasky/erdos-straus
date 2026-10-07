# Hostile review R88 of EXCEPTIONAL_SHORT.md (task O88)

Reviewer: side-agent/review-short. Source reviewed: `EXCEPTIONAL_SHORT.md` and
`reviews/agent-reports/AGENT_REPORT_O88.md` as merged from `side-agent/short-intervals`.
Note = `paper/es-threequarter-note.tex` (internally proved, unrefereed). All verdicts
below are **relative to the note's thm:assembly / lem:identity / lem:CRT**; I did not
re-audit the note's void/moment machinery (outside R88's scope).

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (local mean, shift-uniform) | SOUND (statement slightly weaker than its proof; see D3) |
| Lemma 1.2 (smooth-part decomposition, chain, Rankin) | SOUND |
| Theorem 1 | SOUND (rel. note) |

## Claim-by-claim re-derivation

### Lemma 1.1
Re-derived. thm:assembly expands ν_X = S_y·Q_r(H_X) into ≤ T_abs signed plain
congruence classes a (mod q), every nonempty modulus dividing 𝓜 (eq:termq; atoms at
the same ℓ have distinct projections mod ℓ, lem:CRT, so intersections are empty or one
class). Intersecting with β (mod Q) gives empty or one class mod lcm(q,Q). For *any*
real half-open interval of length H, #{n ∈ (z,z+H] : n ≡ a' (m)} = H/m + θ, |θ| < 1
(checked: floor((z+H−a')/m) − floor((z−a')/m) differs from H/m by < 1). Summation gives
Σ_{n∈I, n≡β(Q)} ν_X(n) = H·E_{Z/lcm(𝓜,Q)}[ν_X 1_{β(Q)}] + O_{≤1}(T_abs). Nothing in
eq:transfer uses the left endpoint; the period 𝓜 (= e^{≍X}, astronomically larger than H)
never needs to be ≤ H, because the count is done class-by-class with O(1) error each, not
period-by-period. The selector period P_y is inside the same expansion. **SOUND.**
Positivity ν_X ≥ 0 (lem:Bonferroni) gives E[ν 1_β] ≤ E ν ≤ e^{−c_a t^3}.

### Lemma 1.2
(a) ES representability is inherited by multiples (4/(dm) = Σ 1/(d x_i)); 1 is
exceptional (4 > 3·1). Correct; n ↦ (d,m) is a bijection, so no double counting.
(b) Chain d = d_0 > d_1 > … > 1 removing one prime ≤ y each step: the last element
> D_0 has successor ≤ D_0 and ratio ≤ y, so lies in (D_0, yD_0]. Correct.
(c) Rankin with exponent 1/2: Σ_{d'>D_0, y-smooth} 1/d' ≤ D_0^{−1/2} Π_{p≤y}(1−p^{−1/2})^{−1};
−log(1−u) ≤ 2u on [0, 2^{−1/2}] (worst at u = 2^{−1/2}: 1.228 ≤ 1.414) and
Σ_{p≤y} p^{−1/2} ≤ Σ_{n≤y} n^{−1/2} ≤ 2√y. Correct (numerically checked, script below).
**SOUND.**

### Theorem 1
(F2) re-derived: lem:identity is stated for every n ≥ 1, so every exceptional m ≥ 1
has H_X(m) = 0 (no restriction m > K or m > ℓ is needed — e.g. m = 1 lies in no atom
class since kℓ ∤ u+v as u+v ≤ 2z_j < ℓ); with (m,P_y)=1 and Q_r(0)=1, ν_X(m) = 1.
The note's own restriction "exceptional prime n > max(K,y)" is merely conservative.

Case (ii), the worry "m ranges over an interval of length H/d, short for large d":
harmless, because Lemma 1.1 has *additive* error T_abs per d irrespective of length,
and there are ≤ D_0 = e^{2c_a t^3} values of d, so the total additive error is
D_0·e^{C_L t^4} = e^{O(t^4)}; H/d may even be < 1 without harm. The main terms sum to
H e^{−c_a t^3} Σ_{d≤D_0} 1/d ≤ H(1+2c_a t^3)e^{−c_a t^3}.

Case (i), the worry "smooth numbers are not equidistributed in short intervals": the
proof never uses distribution of smooth numbers in I. It only uses the trivial
#{n ∈ I : d' | n} ≤ H/d' + 1 for each y-smooth d' ∈ (D_0, yD_0], summed by a union
bound; the +1's total ≤ yD_0 = e^{O(t^3)}. Correct.

Balance: E(I) ≤ C_1 H e^{−c_a t^3/2} + e^{C_2 t^4}, t = (log H/(2C_2))^{1/4} needs
t ≥ log X_a, i.e. H ≥ exp(2C_2 (log X_a)^4) — a fixed threshold; below it trivial.
Since thm:assembly is asserted for *every* X ≥ X_a (not a sequence of X), a
continuous choice of t is legitimate. Uniform in z, no H ≤ z or z ≥ 0 hypothesis.
Corollary ranges (H ≥ x^θ ⇒ saving θ^{3/4}(log x)^{3/4}) are immediate. **SOUND.**

### Lemma 2.1 and Theorem 2
Lemma 2.1 re-derived: primes of 𝓜 (eq:space) are those of L_K (≤ K), P_y (≤ y) and the
ℓ ∈ (X^{1/2}, X]; all ≤ X. CRT in Z/𝓜Q_2 gives exact factorisation; dropping
1_{β(Q_1)} ≤ 1 uses ν_X ≥ 0. **SOUND** (toy: exact equality checked for Q = 61, 67·71
against a 36-atom toy ν, script below).

Theorem 2 proof re-derived. (i) y-smooth d' and q_2 coprime (y < X), so the n ∈ I with
d' | n, n ≡ b (q) are ≤ H/lcm(d',q) + 1 ≤ H/(d'q_2) + 1. (ii) d m ≡ b (q) ⟺ m in one
class mod q/g (g = (d,q), solvable iff g | b); g is y-smooth so q/g has X-rough part
exactly q_2; with Lemma 1.1 *in the form of its proof* (main term H·E[ν 1_{β(Q)}], see
D3) and Lemma 2.1, Σ ≤ (H/(d q_2)) e^{−c_a t^3} + T_abs. The additive errors are *not*
divided by q, but they total e^{C_2 t^4} = (H/q)^{1/2} by the choice of t, so this is
fine. H/q_2 = q_1 H/q. Constants depend only on the note's fixed constants. **SOUND**
modulo the constant-range slips D4, D5.

Ranges: (a) q ≤ (log x)^A with H ≥ exp((log log x)^{4/3+ε}) — checked: log(H/q) ∼ log H,
(c/2)(log(H/q))^{3/4} ≥ A log log x eventually. (b) prime q: any prime q > X_q works,
and every prime q ≤ X_q is covered by (a); so in fact **every prime modulus q with
H/q ≥ 2** gets E(I;q,b) ≪ (H/q)exp(−c'(log(H/q))^{3/4}) — the author's "exp((log H)^{1/4+ε})"
lower restriction in (b) is unnecessary (harmless).

Remark 2.2 (q_1 loss). The loss is honest for the method. But the claim "for q_1 = ∏_{y<p≤z}p
and b ≡ 0 (q_1) the CRT majorant is *genuinely large*" is not proved: what fails is the
void lemma's *bound* (Z(c) ≥ Σ_{y<p≤z, p|L_K} 1/p can exceed η), not demonstrably E[ν | class].
Toy illustration (script, item 4): conditioning on n ≡ 0 (5) raises the toy mean by
14%, on n ≡ b (ℓ) up to 30%; nothing near "genuinely large". See D6. Also a constructive
observation (Assessment, not a defect): for b with (b, q_1) = 1, conditioning makes
p ∤ c for every p | q_1, which only *helps* the bad event {Z(c) > η}; the ℓ | q_1
coordinates change the fibre product by ≤ exp(Σ_{ℓ|q_1} 2ℓ^{−2/3}) = 1+o(1). What is
missing for removing q_1 in coprime classes is only a conditional version of the
factorial-moment bound (thm:moments) — likely routine. The author may want to state
this as the precise open sub-step instead of "fibre-uniform void bound".

### Corollary 3.1
Re-derived: H e^{−c(log H)^{3/4}} ≤ (H/log x) e^{−(c/2)(log H)^{3/4}} ⟺
(c/2)(log H)^{3/4} ≥ log log x ⟺ log H ≥ (2/c)^{4/3}(log log x)^{4/3}. So C_3 = (2/c)^{4/3};
the exponent 4/3 is right and is just the inverse of 3/4. No prime input needed (E_pr ≤ E).
**SOUND.** The progression clause needs C_3 adjusted for the c/2 of Theorem 2(a) (D5).
It is a trivial corollary (Assessment: not worth a separate "result" in the ledger).

### Corollary 3.2
(a) Uses Theorem 1 with θ = 0.525 and BHP. BHP (Proc. LMS 83 (2001) 532–562) is
usually quoted as "[x − x^{0.525}, x] contains a prime for x > x_0"; the ≫ x^{0.525}/log x
lower bound is in the paper (the sieve gives a positive proportion; later refined by
R. Li 2023) but I could **not** access the PDF to confirm the exact constant/statement.
For H > x^{0.525} one must tile (x,x+H] by intervals [u − u^{0.525}, u] — one line,
missing (D7). Huxley 1972 (Invent. Math. 15, 164–170): asymptotic for H ≥ x^{7/12+ε} and
almost-all for H ≥ x^{1/6+ε} confirmed via secondary sources (Watt 1995, Zaccagnini
1998, R. Li 2024 abstracts), not the original. (b),(c) are correctly flagged as
quoted/Assessment. **SOUND-AFTER-REPAIRS (D7)**, (c) Assessment only.

### Proposition 4.1 / 4.2
4.1: trivial and correct (bound < 1 ⇒ zero; windows (x, x+H_0(x)] with H_0 ≥ 1 cover
(x_0, ∞)). 4.2(a),(b) correct. 4.2(c) middle regime: the dichotomy "needs θ_win > 3/4-type
input *or* position-dependent input" is heuristic, not a theorem (D8). "𝓜 + H ≤ x if
H ≤ exp(c(log log x)^4)": checked, log 𝓜 = θ(X) − θ(X^{1/2}) + log lcm(P_y, L_K) ≤ (1+o(1))X
and X = exp(α(log H)^{1/4}). **SOUND** (4.1, 4.2(a)(b)); 4.2(c) and the "shift-uniform
methods" paragraph are Assessment, mislabelled PROVED (D8).

### Literature / novelty (Assessment)
Checked by me (Jina search/visit, 2026-10-07): Yang Xun Qian, PAMS 85 (1982) 496–498:
abstract confirms S(N) ≪ N/log²N for n < N — global count only. Li Delang, JNT 13 (1981)
485–494: paywalled (captcha); search snippet "for any given positive integers N and k the
number of integers n < N for which … unsolvable" — global count, no short-interval claim
visible; **full text not checked**. Jia Chaohua (2012, "estimate for mean values on prime
numbers relative to 4/p") is about mean values of solution counts over primes, not
exceptional sets in short intervals (title/abstract only). Pomerance–Weingartner
(sources/pw.txt): grep shows no short-interval exceptional-set theorem. Vaughan 1970,
Elsholtz–Tao: global. I found no published short-interval/progression ES exceptional-set
result. I agree with the author's folklore caveat: Vaughan's large-sieve route is
translation invariant (large sieve holds on any interval), so an expert would regard
shift-uniformity as routine. The genuinely clean contribution is that the local
d·m decomposition removes the note's global Rankin/semigroup step (a simplification of
the note itself — worth back-porting). Novelty claims are appropriately modest.
