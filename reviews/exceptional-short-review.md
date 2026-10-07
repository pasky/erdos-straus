# Hostile review R88 of EXCEPTIONAL_SHORT.md (task O88)

Reviewer: side-agent/review-short. Source reviewed: `EXCEPTIONAL_SHORT.md` and
`reviews/agent-reports/AGENT_REPORT_O88.md` as merged from `side-agent/short-intervals`.
Note = `paper/es-threequarter-note.tex` (internally proved, unrefereed). All verdicts
below are **relative to the note's thm:assembly / lem:identity / lem:CRT**; I did not
re-audit the note's void/moment machinery (outside R88's scope).

## Summary verdict

No FATAL/MAJOR defects. Theorems 1 and 2 are correct relative to the note; 8 MINOR
defects (D1–D8), all wording/constant/label fixes. Full table at the end.

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

## Numbered defects

No FATAL or MAJOR defects found. All MINOR.

**D1 (MINOR) — effectivity.** Theorems 1, 2, Cor 3.1 say "absolute constants c, C". The
note's constants are absolute only after fixing κ, and are *ineffective* (standard BV,
note §1 "Constants are not asserted to be effective"). *Repair:* add "(ineffective, as in
the note)" to Theorems 1–2 and Cor 3.1, and make the X_a / H-threshold dependence explicit.

**D2 (MINOR) — §4 "Shift-uniform methods", "the short-window exponent at length H equals
the long-interval exponent at N = H".** Not an equality: the long interval (0,H] is one
shift; M_𝔊(H) is the max over shifts. What is true: both are bounded by M_𝔊(H), and a
lower bound on M_𝔊(H) obstructs both only for the window problem. *Repair:* replace
"equals" by "is controlled by the same quantity M_𝔊(H) as".

**D3 (MINOR) — Lemma 1.1 statement weaker than its use.** Statement gives
H e^{−c_a t^3} + e^{C_L t^4}; Theorem 2(ii) needs H·E[ν_X 1_{β(Q)}] + T_abs (to insert
Lemma 2.1's 1/Q_2). The proof establishes this. *Repair:* state Lemma 1.1 as
`Σ_{n∈I, n≡β(Q)} ν_X(n) = H·E_{Z/lcm(𝓜,Q)}[ν_X 1_{β(Q)}] + θT_abs, |θ| ≤ 1`, then the
current bound as a consequence.

**D4 (MINOR) — Theorem 2(a) example "q ≤ exp(c'θ^{3/4}(log x)^{3/4}) with H ≥ x^θ".**
At H = x^θ, log(H/q) < θ log x, so q = exp(c'θ^{3/4}(log x)^{3/4}) slightly violates the
hypothesis q ≤ exp(c'(log(H/q))^{3/4}). *Repair:* use c'/2 (or c'θ^{3/4}/2) in the example.

**D5 (MINOR) — Cor 3.1, progression clause.** Theorem 2(a) has saving constant c/2, so the
threshold must be log(H/q) ≥ (4/c)^{4/3}(log log x)^{4/3}, not C_3 = (2/c)^{4/3} as for
integers. *Repair:* use a separate C_3' (or define C_3 with the worst saving constant).

**D6 (MINOR) — Remark 2.2 overclaim + dangling reference.** "the CRT majorant is genuinely
large in that progression" is unproved (only the void lemma's bound breaks); "see §4" —
§4 contains no such discussion. *Repair:* say "the void lemma's bound gives nothing in
that progression (Z(c) ≥ Σ_{y<p≤z} 1/p may exceed η)"; delete or fix the cross-reference;
optionally add the coprime-b observation from this review as the precise open sub-step
(conditional factorial-moment bound).

**D7 (MINOR) — Cor 3.2(a).** BHP is cited as π(x+H) − π(x) ≫ H/log x for all
x^{0.525} ≤ H ≤ x; BHP state the x^{0.525} case. *Repair:* cite the exact BHP statement
(the ≫ x^{0.525}/log x count) and add the tiling of (x, x+H] by [u − u^{0.525}, u],
u ≍ x. Mark the BHP/Huxley statements as checked-from-secondary-sources unless the
originals are consulted (I could not access them).

**D8 (MINOR) — labels in §4.** Prop 4.2 is labelled PROVED rel. note, but 4.2(c)'s
"would need θ_win > 3/4-type input *or* position-dependent input" and the "position
genuinely cannot help" sentence are heuristic dichotomies, not theorems. *Repair:* split:
4.2(a),(b) PROVED; (c) and the shift-uniform paragraph → Assessment.

## Final summary table

| claim | verdict |
|---|---|
| §0 inventory of the note's counts | SOUND (re-checked eq:transfer/eq:termq/eq:space) |
| Lemma 1.1 | SOUND-AFTER-REPAIRS (D3, restatement only) |
| Lemma 1.2 | SOUND |
| Theorem 1 (rel. note) | SOUND (D1 cosmetic) |
| Lemma 2.1 | SOUND |
| Theorem 2 (rel. note) | SOUND-AFTER-REPAIRS (D3, D4; range (b) actually covers all primes q) |
| Remark 2.2 | GAP in wording only (D6); labelled OPEN appropriately |
| Cor 3.1 | SOUND (integers/primes); progression clause SOUND-AFTER-REPAIRS (D5) |
| Cor 3.2 | (a) SOUND-AFTER-REPAIRS (D7); (b),(c) quoted, Assessment |
| Prop 4.1 | SOUND (trivial) |
| Prop 4.2 | (a),(b) SOUND; (c) + shift-uniform paragraph mislabelled (D2, D8) |
| Novelty Assessment | fair and appropriately modest; literature partially checked (Li Delang full text not accessed) |

Everything inherits the 3/4 note's INTERNALLY PROVED (unrefereed) status; nothing here
is stronger than "PROVED relative to thm:assembly + lem:identity". Suggest the parent
back-port the local d·m decomposition into the note §9 as a simplification of the
Rankin/semigroup transfer.

## Scripts / replay
`scripts/review_short_toy.py` (from scratch; output `data/review_short_toy.out`):
1. lem:identity on random (k,ℓ,u,v,w), 20 class members each: 0 failures (exact rationals).
2. Toy LL-atom family (36 atoms, k ∈ {1,5}, ℓ ∈ {11,19,23,31}), selector P_y = 6, r = 2:
   ν ≥ 0, exact period mean E ν = 0.1281; over 20 000 random real windows
   (z up to ±10^12, H up to 10^8) max |Σ_I ν − H E ν|/T_abs = 0.012 ≤ 1 (Lemma 1.1);
   max over *all* shifts for H = 50/500/5000: 22/86/675 vs H·Eν = 6.4/64/640 + T_abs.
3. Lemma 2.1 exact equality for Q = 61, 67·71.
4. Conditioning on small/ℓ-progressions raises the toy mean by ≤ 30% (Remark 2.2 context).
5. Lemma 1.2(b) chain on 2000 random smooth d; −log(1−u) ≤ 2u at u = 2^{−1/2};
   Σ_{p≤y} p^{−1/2} ≤ 2√y; Rankin sum check at y = 13, D_0 = 10^4.
Run: `ulimit -v 8000000; timeout 900 uv run python scripts/review_short_toy.py` (~1 min).
