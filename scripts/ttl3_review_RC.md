# RC hostile review: induction, switching, and (EFF)

**Verdict: no FATAL or MAJOR finding in the requested argument, conditional on its
stipulated effective large sieves and effective U-form of Theorem 14.** There is an
endpoint/constant correction below; the currently printed proof is not literally
correct at every endpoint. It does not change the double-exponential envelope or A₀.
This is not an independent certification of the full proofs of those two analytic inputs.

Sources checked directly: DI journal pp. 225–228 and 270–278 (rendered scan),
Drappeau pp. 11–19 (text), both Lemma 8.1 notes, the nebentypus context note,
LOGLOG3 §§2, 7–9, and LOGLOG2's conversion and Thm 4.1(ii)–(iii).
I also inspected the statements/conventions of the effective large-sieve and Thm 14 notes.
No reviewed file was edited.

## Findings and concrete repairs

**MINOR M1 — closed endpoints invalidate the displayed derivation of K₂ = 17K_T2.**
LOGLOG3 §2 uses `[N,N₁]`, while §3 uses `‖1_I‖² ≤ N`, and both Lemma 8.1
notes formally state their inputs for `(N,N₁]`. At N=1, I=[1,2], the norm squared
is 2. Even the printed half-open convention only gives `≤2N` for general real N.
The summed large-sieve majorant at N=1, Q=1000 is approximately 30005.54 K_T2,
whereas the claimed P3 right side with 17 is 17017 K_T2. This is a failure of the
stated deduction, not a counterexample involving actual exceptional forms.
The same issue affects `K₂χ = 17K_LSχ` and the closed-interval assembly in §9.

Repair: explicitly state both Lemma 8.1 inputs for closed intervals and use `≤2N`.
Their support, transform and partial-summation estimates already tolerate this.
For P3 take `K₂=34K_T2`, `K₂χ=34K_LSχ` if the supplied sieves are explicitly
extended to closed supports with their present constants. Alternatively 68 is safe
using two half-open sieve intervals and Cauchy–Schwarz, without that extension.
In the two-variable summation replace lower prefixes `[1,N]` by `[1,N)`;
when N=1 the latter is empty and must be omitted rather than fed to Thm 14 with M=0.
All nonempty prefixes can use integer endpoints ≥1 and ≤2N.
The generous constants in P1/P2 absorb this endpoint repair; H and K₇ should use
the corrected K₂. The envelopes 410/δ and `(24Bχ+30)/ε` still have ample room.

**MINOR M2 — P2's domain is not self-contained in LOGLOG3 §2.**
There S is defined only for Q≥1, although πNY/Q can be <1 in the input statement.
The untwisted note explicitly repairs this, and induction only uses C≥N≥1.
Repair §2 itself by defining S for every Q>0, or declaring the error-only branch
when πNY/Q<1. This is not an obstruction to Prop. 2.1 or Thm 9.1.

## Induction and conversion checks

* (PS) is correct with the **supremum over upper endpoints**. Abel summation for
  closed intervals includes the atom at N; the integral bound costs `(log 2)²≤1`.
  No invalid interchange of supremum and spectral sum is made.
* Prop. 2.1(A),(B) hold with corrected P3: Y≥1, `8·2^δ<10`, and the base is
  bounded by `2K₂Q₀ Q^(1+4δ)N`. In (C), Q₁≥N and Q₁≤Q/2; Y₁≥1.
  The exact Q exponent is `2δ(1−δ)+(1−2δ)(1+4δ)=1+4δ−10δ²`.
  Dropping π^(−1+δ) is permissible; `2√2π·π^1.4=44.127…<45`.
  The 90c threshold and H≥6c close the contraction.
* Thm 2.2's N>Q branch costs `4·2^δ<5`; its N≤Q branches give respectively
  Q^(1+4δ) and Q^(5δ)√(NY). Cor. 2.3's δ⁻² threshold costs only the stated
  extra 3/δ in the double-exponential envelope. Assembly §7's D(δ/4) bound
  is valid throughout δ≤1/10; the 410 allowance survives M1.
* Prop. 8.1(C1) gives `Q^(1−δ)C^(5δ)` and therefore the identical
  `1+4δ−10δ²` exponent, with r^(−5δ). In (C2), P1χ is legitimately applied
  for C<N, including C<1: its bound is at most `10K₁Q^(1+2δ)N`.
  The recurrence error is `≤3cQ^(1+3δ)N`. Since `90cK₁+3c≤93cK₁`,
  H≥200cK₁ suffices for the printed common closing inequality.
* Thm 8.2's Q<1 proof needs an implicit final comparison, which is valid:
  for Q≥1/16, `N^(2δ)≤16^(2δ)(QN+1)^(2δ)≤2(QN+1)^(5δ)`.
  Thus 10K₁ really suffices. Every Y used with (M) is ≥1; no Y<1 branch is missing.
* For Thm 9.1 use cofactor blocks starting `(1/16,1]`, so level r is included.
  Each block has Q≤M₀/r≤M₀. The prefix decomposition includes n=1,
  uses ≤1.5 log(2t) intervals and has Σ2^k≤2t. Converting its single logarithm
  to log²(2t) costs at most 1/log 2<2, including t=1.
  Maximizing `(2+v)e^(−εv/6)` proves the printed logarithm absorption with 12/ε.
  Consequently the 100/ε allowance is valid after the endpoint repair.
* The envelope chain is consistent: Bχ → 4Bχ+1 → 4Bχ+4, followed by δ=ε/6,
  gives 24Bχ+24; absorbing 100/ε inside another 6/ε gives A₀=24Bχ+30.
  For B_W≤3, C_W≤10, A₀≤16728.21<20000. Without numerical Weil constants,
  this remains an explicit formula in absolute black-box constants, not a certified numerical A₀.

## Analytic switching and preliminary bound checks

* DI (1.22) really has the opposite sign from (8.1); Drappeau (4.10) has the
  positive convention used in the twisted note. The two-switch signs cancel;
  P1 takes an absolute value. The twisted identity also supplies a clean r=1 route.
* The exceptional kernel ratio is bounded by `exp(−4σ(log(2/x)−2))` using
  `|ψ|≤2` on [1/2,3/2]. The plateau alone contributes at least
  `(1−e⁻¹)log(4/3)Y^(2σ)=0.181849…Y^(2σ)>Y^(2σ)/8`.
  At Y=2^32 the stated integrated remainder is <8.64·10⁻8 and decreases.
  Hence the /64 lower bound is genuinely uniform as σ→0, after dividing by cos(πσ).
* The subtracted Bessel-order tails cancel their apparent 1/σ singularity.
  Small real parameters require log Y, retained in the notes. For large real
  parameters the normalized kernel is O(r⁻¹/²); moving D_x²+x² twice supplies
  the required fourth-power decay. The integer-order series is uniform in the
  Mellin twist. Fixed derivative orders fit comfortably within H=2^512 and B=2^2048.
* Support division gives exactly `4/((9/4)(17/12))=64/51` and
  `8/((3/4)(11/12))=128/11`, both strictly inside (1,16).
  Mellin inversion uses dx/x and produces `overline(A(t/2)) A(−t/2)`, not a square.
  The two-square inequality and t=±2u substitution justify the claimed recurrence.
  Twisted levels are rc, with the same character modulo r; the scalar phase has modulus 1.
* All four simultaneous enlargements keep C fixed, cost at most 8^(1/2) in
  exceptional weights, and are covered by the advertised constants. The Y<2^32
  direct-sieve branch preserves C. The untwisted C<1 error-only argument uses
  Q>πNY correctly; the twisted note correctly refuses that inference.
  For C<1/16 the destination is empty; otherwise the finite small-C sum is retained.
* P1 uses `8NY<k<32NY`. The mixed derivative formula is correct and yields a
  k-independent variation measure. Prefix conversion must receive M1's endpoint fix.
  Opening Sχ and removing its unit character bounds each rectangle by U; DI p. 276
  indeed majorizes U, not just the untwisted rectangle sum. Dropping r|k is then legal.
  With K=32NY the losses are exactly N^(4e)Y^(2e), bounded by (NY)^δ.
  No sum of k-dependent rectangle maxima is illicitly substituted.

## LOGLOG2 application

The sieve exponent is `−1/4+3/64+1/32=−11/64`. With ε=w/128 and
w=256A₀/log L, `log Cε≤√L`; the remaining saving dominates this and fixed
logarithms eventually. For (iii), `½log Cε≤δL/64` leaves 5δL/32, and
δ≥L⁻¹/² gives an absolute eventual threshold. Bad layers cost
`(wL+1)NL log L`, giving the asserted bounds. No extra ε-dependent constant
is introduced by these uses. Small N can be absorbed in the absolute final constant.
