# T-D: nebentypus audit of Drappeau 4.9–4.11

**Scope/status.** Read LOGLOG3 §§0–3, LOGLOG2 §1 and the DI audit; checked Drappeau
pp. 10, 13–19 (including images of pp. 17–18), and DI scans pp. 271–277.
Exact twisted trace identities and twisted Weil bounds are black boxes here.
The induction transfers **with repairs, not verbatim**. Its constants have the same
class-𝓔 envelope provided the noninductive estimates are quantitatively implemented.
This is not a numerical certificate for every implicit constant in Drappeau.

## 1. Statements and normalization

Fix an **even** character χ modulo r = q₀, induced to every level divisible by r;
use weight zero and the cusp ∞ with scaling matrix Id. Put b_f(n) = √n ρ_f∞(n)
(DI's coefficient up to an absolute factor), σ_f = |Im t_f| ∈ (0,1/4], and

    E_L(Y,a) = Σ_{f exceptional in B(L,χ)} Y^{2σ_f}|Σ_{N<n≤2N} a_n b_f(n)|².

The endpoint t_f=0 can instead be put into the regular spectrum. All bounds below
are uniform in r, χ. Drappeau's statements allow his parity/weight convention;
only the even, weight-zero case is needed here.

* **Lemma 4.9:** for Y≥1, R≥r,
  `Σ_{L≤R, r|L} E_L(Y,a) ≪ε (RN)^ε(R/r + N + N√Y)‖a‖₂²`.
* **Lemma 4.10:** for interval indicators a,
  `Σ_{L≤R, r|L} E_L(Y,a) ≪ε (RN)^ε(R/r + N + √(NY))N`.
  An interval may be any subinterval of [N,2N] (closed allowed; R121B repair, m2); prefix differences cost an absolute factor.
* For the proof Drappeau **renames the level L=rq** and defines
  `Sχ(Q,Y,N,t;I) = Σ_{Q<q≤16Q} Σ_{f∈B(rq,χ), exc} Y^{2σ_f}|Σ_{n∈I} n^{it}b_f(n)|²`.
  Thus the actual level range is **rQ<L≤16rQ, r|L**, not Q<L≤16Q.
  Write Sχ* for the supremum over I, at t=0.

Here are the precise three inputs, for 0<δ≤1/10 and Q,N,Y≥1:

    (P1χ) Sχ*(Q,Y,N) ≤ K₁χ(δ)(NY)^δ(Q+N+Y)N.                 [4.30]
    (P2χ) Sχ(Q,Y,N,0;I)
            ≤ cχ(δ)∫ℝ Sχ(πNY/(rQ),Y,N,t;I) dt/(1+t⁴)
              + cχ(δ)(QYN)^δ(Q+N/√r+NY/(√r Q))N.            [4.29]
    (P3χ) Sχ*(Q,1,N) ≤ K₂χ(δ)(Q+N^{1+δ}/√r)N.              [Prop. 4.7]

Lemma 4.11 states (P2χ) for arbitrary a, replacing N outside the bracket by ‖a‖₂²
and using a_n n^{it} in the switched sum. Its second assertion is (P1χ).
The printed p. 19 version of (P3χ), `(QN)^δ(Q+N/√r)‖a‖₂²`, is a weakening.
In particular **(P2χ) has an extra Q^δ compared with LOGLOG3 (P2)**.

**Prop. 4.7:** each of the holomorphic, Maaß and Eisenstein large-sieve quantities
(4.23)–(4.25) is at most
`K_LSχ(δ)(T²+√r μ(a)N^{1+δ})‖a‖₂²`, T≥1, N≥1/2,
where μ(a)=(w,L/w)/L for a=u/w, w|L. At ∞, μ=1/L.
For weight zero the Maaß weight is 1/cosh(πt_f); at exceptional parameters its
reciprocal is between 1 and √2. Summing at L=rq gives (P3χ), since
`Σ_{Q<q≤16Q}1≤16Q`, `Σ_{Q<q≤16Q}1/q≤1+log16`.
One can take K₂χ=17K_LSχ for Q≥1.

**Lemma 4.2:** at a singular cusp,
`|S_aa(m,n;c)| ≤ C_W (m,n,c)^{1/2} τ(c)^{B_W}(cr)^{1/2}`,
with absolute C_W,B_W (printed as ≪ and O(1)). These are parameters of the accepted
Weil black box, not ε-dependent constants. Prop. 4.7 retains √r explicitly.

## 2. Switching and the strengthened initial bound

In the first Kuznetsov expansion the arithmetic term is

    Σ_{q,c≥1} g(q)/(rqc) · φ(4π√(mn)/(rqc)) · Sχ(m,n;rqc).

For fixed c this is precisely a Kuznetsov modulus sum for **Γ₀(rc), with the same
χ modulo r induced to rc**, summing moduli (rc)q. Thus r divides every new level.
Neither Γ₀(c) with χ nor a character of modulus rq is involved. No character sum
is being averaged away in the recurrence. The occurrence `S∞∞(m,n;qc)` on p. 17
must read `Sχ(m,n;rqc)`; the denominator and the next group Γ₀(rc) confirm this.

For (4.30), put k=rqc and use the divisor bound for the number of factorizations.
On the support, k≍NY, **independently of r**. Mellin separation and partial
summation reduce to rectangular incomplete twisted Kloosterman sums. Opening
Sχ and applying the triangle inequality bounds these by

    U₂(k;M,H) = Σ_{d mod k,*}|Σ_{m≤M}e(m(d̄/k+α))|
                                    ·|Σ_{n≤H}e(n(d/k+β))|,

with M,H≤2N and fixed phases (Drappeau uses α=ϑ, β=−ϑ).
This nonnegative expression makes sense for every k: discard r|k by positivity.
DI Lemma 8.2 majorizes the two absolute exponential sums by f_M,f_H, then Fourier
expansion gives **untwisted** S(u,v;k), with coefficients multiplied by unit phases.
The **proof** of untwisted DI Thm 14, not its statement alone, gives uniformly
`Σ_{k≤K}U₂(k;M,H) ≪δ (KMH)^δ K(K+MH)`.
Its only spectral input is DI Thm 9 at level one (no exceptional eigenvalues).
Zero frequencies are Ramanujan sums; the nonzero-frequency estimate is insensitive
to these unit phases. Hence T≪δ(NY)^δ(NY+N²), and (P1χ) follows after adding
the Prop. 4.7 error. This is why no positive power of r survives in (P1χ).

## 3. Quantitative induction: what transfers and what does not

Monotonicity in Y and LOGLOG3's partial-summation inequality
`Sχ(Q,Y,N,t;I)≤2(1+t²)Sχ*(Q,Y,N)` transfer exactly. Selberg's numerical
σ≤1/4 applies also to this congruence-character subspace; no ineffective constant enters.
Fix uniform K₁,K₂,c for the three inputs, all ≥1.

To prove `Sχ*(Q,Q^{2−2δ}/N,N)≤H Q^{1+4δ}N` for 1≤N≤Q, take

    Q₀=max((90c)^{1/(10δ²)},(2π)^{1/(2δ)}),
    H=max(2K₂Q₀,10K₁,6c,1000cK₁).

Here constants have been enlarged, if necessary, for the small-cofactor convention
below. The base Q≤Q₀ and the range N>Q^{1−2δ} follow exactly as in LOGLOG3.
In the remaining range let Y=Q^{2−2δ}/N and

    C=πNY/(rQ)=πQ^{1−2δ}/r ≤ Q/2.

**Case C≥N:** put Y_C=C^{2−2δ}/N≥1. The induction applies at C. The coefficient
multiplying H after monotonicity and partial summation is at most

    2√2π c √(NY) C^{5δ}
      = 2√2π·π^{5δ} c r^{−5δ} Q^{1+4δ−10δ²}
      ≤ 45c Q^{1+4δ−10δ²}.

The recurrence error is ≤3c Q^{1+3δ}N, not the Q^{1+2δ}N of LOGLOG3's proof;
it still fits the other half of H Q^{1+4δ}N. This closes the contraction.

**Case C<N:** LOGLOG3's induction hypothesis is unavailable! Smaller switched
level is not automatically beneficial. Apply (P1χ), with Y₁=C+N, and monotonicity:
`Sχ*(C,Y,N)≤5K₁ N^{3δ}(N+√(NY))N` when C≥1.
Since N≤Q^{1−2δ}, this is ≤10K₁ Q^{1+2δ}N. Its partial-summation integral costs
only 2√2π; the term 1000cK₁ in H covers this and the recurrence error.
Thus this branch requires no inductive hypothesis and no positive power of r.

**Small C and cofactor 1:** the printed S is defined for any C>0, although Lemma
4.11 states Q≥1. If 16C<1 it is empty. For 1/16≤C<1, repeat the noninductive
(4.30) argument over the at most sixteen cofactors, replacing C by max(1,C) in
harmless size factors. It gives the preceding C<N bound with, say, 20K₁ instead
of 5K₁, after an absolute enlargement of K₁. The same argument treats cofactor 1
in passage to the prefix level sum, which Q≥1 open dyadic intervals otherwise miss.
No new spectral input is needed, but this endpoint cannot simply be omitted.

The final passage from the special Y to arbitrary Y, and the N>Q case, is exactly
LOGLOG3 Thm 2.2: `Sχ*≤max(H,5K₁)(QN)^{5δ}(Q+N+√(NY))N`.
Dyadic summation to L≤R uses Q≍R/r; all extra logarithms are absorbed with δ a
fixed multiple of the final ε. Thus the claimed `(RN)^ε(R/r+N+√(NY))N` follows.
The phrase “r appears only with negative powers” is correct **after** (P1χ) and
(P2χ) have been established, and the branch C<N is handled as above.

For **Lemma 4.9**, p. 19 refers instead to DI p. 274: induct uniformly over all
coefficient vectors, at `Y=(Q^{1−η}/N)²`, `N≤Q^{1−η}`, with target
`H Q^{1+η}‖a‖²`. The switch is `C=πQ^{1−2η}/(rN)`; when `N≤C^{1−η}`,
weight comparison gives `H Q^{1−η}C^{2η}≤Hπ^{2η}r^{−2η}Q^{1+η−4η²}`.
Outside that range use (P3χ) and monotonicity at C (including the finite-cofactor
endpoint). The n^{it} coefficients preserve ‖a‖₂, so no interval partial summation
is needed. Choose the input tolerance ≤η/10 to absorb (QYN)^δ. This is the first
DI induction, with the same effective threshold mechanism; (P1χ) is not used.

## 4. Effectivity ledger

Use the audit's categories: (a) divisor/gcd, (b) logarithms, (c) induction,
(d) transforms/smoothing, (e) unspecified data. A useful explicit bookkeeping kit is

    D_B(η)=(2B/η)^{B·2^{B/η}},   L_j(η)=(j/(eη))^j,
    J(p)=C^{p+1}(p!)²,          p≤A/δ+2,

using LOGLOG3's Gevrey cutoff and fixed absolute A,B,C. Allocate every intermediate
tolerance as δ/A, **not δ²**. Finite products and fixed powers of these quantities,
and δ^{-O(1)}, lie in 𝓔(B′). The following lists dependencies, not numerical values
of the constants suppressed by the papers.

| Input | δ-dependent costs | Literally DI / new bookkeeping; r-uniformity |
|---|---|---|
| Lemma 4.2 | None before replacing τ^{B_W} by D_{B_W}(η)c^η (a). | New twisted black box; retain √r. Supply C_W,B_W for a numerical certificate. |
| Lemma 4.6 → Prop. 4.7 → K₂χ | D_B, L_j, J(O(1/δ)), geometric sums O(1/δ) (a,b,d). | DI Prop. 3/Thm 2 analytic proof at weight zero. New χ factors have modulus ≤1 off resonance and cancel on resonance (Dr (4.22)); no sum over characters. The only conductor factor is the displayed √r μ. |
| cχ in (P2χ) | K_LSχ at δ/A; four fixed Mellin integrations; small-σ split, O(δ^{-O(1)}) and log absorption (b,d). | DI Lemma 8.1 analytic estimates; new level accounting rq↔rc and χ fixed. Errors are Q+N/√r+NY/(√r Q). |
| K₁χ in (P1χ) | K_LSχ, D_B(δ/A), fixed Mellin derivatives, log/geometric factors, K₁₄(δ/A) (a,b,d). | **Untwisted DI Thm 14 proof**, including Lemma 8.2 and Thm 9 at level 1. New step is removal of χ and r|k by the nonnegative majorant. k≍NY leaves no conductor constant. |
| K₇χ | Q₀ and H above; fixed dyadic/log factors (b,c). | Corrected DI induction. If K₁,K₂,c≤exp(exp(B/δ)), then K₇χ≤exp(exp(B′/δ)) for effective absolute B′. |

Thus no new ε-dependent arithmetic theorem or ineffective L-value estimate is
needed. But Drappeau's “transpose” instructions are not a printed quantitative
proof: one must choose the cutoff, retain the character cancellation, and specify
the fixed Weil constants to turn this ledger into an explicit numerical envelope.

## 5. Alternative: twist into trivial nebentypus?

**The proposed square-root assertion is false for general even χ.** For squarefree
odd r, χ is a square modulo r iff **every local χ_p is even**, not merely their
product. Example: r=21, χ=χ₃χ₇ with both local characters quadratic; χ is globally
even but has no square root modulo 3. Hence this route cannot cover LOGLOG2's
character average. If all local χ_p are even, choose a local square root; at trivial
χ_p choose the nontrivial quadratic character. Their product ψ is primitive modulo r.

In that restricted situation, r²|M, the proposed operator is valid:
`Tf=τ(ψ)^{-1}Σ_{b mod r,*}ψ(b)f(z+b/r)` has coefficients `ψ̄(n)b_f(n)`, character
`χψ̄²=1`, the same eigenvalue, and is cuspidal. The automorphy calculation uses
α_b γ=γ′α_{b′}, α_b z=z+b/r, with b′≡bd² (mod r) and γ′∈Γ₀(M).
It also proves `G=Σ_b|f∘α_b|²` is Γ₀(M)-invariant.

**Norm check:** invariance alone does not prove the proposed integral identity.
Take a common finite-index subgroup H⊂Γ₀(M)∩⋂_b α_b^{-1}Γ₀(M)α_b.
Each conjugate α_b H α_b^{-1} has the same index in Γ₀(M), by equal hyperbolic
covolumes. Integrating on H\H then dividing by the index proves
`∫_{Γ₀(M)\H}G=φ(r)‖f‖²`. Cauchy–Schwarz and |τ(ψ)|²=r yield precisely
`‖Tf‖²≤φ(r)²/r·‖f‖²`. This includes oldforms; no isometry claim is needed.

For a functional supported on (n,r)=1, let ℓ_ψ use coefficients multiplied by
ψ(n). Then ℓ_ψ(Tf)=ℓ(f). Applying the operator bound eigenspace by eigenspace
proves the stated spectral inequality for **nonnegative** h. For general ℓ it does
not: T kills every coefficient with (n,r)>1, and can kill entire oldforms.
Additional bad-prime/oldform operators and their norm/level bookkeeping are needed.

**Periodic coefficients in DI itself are not the main obstacle.** For r-periodic
w with |w|≤1, write `w(n)=Σ_{a mod r}ŵ(a)e(an/r)`; Parseval gives
`Σ_a|ŵ(a)|≤√r`. In (P1), expand both coefficient factors. The DI Thm 14 proof
just used works with *two arbitrary additive shifts* α,β: Fourier majorants acquire
only unit phases, zero frequencies remain Ramanujan sums, and Thm 9 is unchanged.
The cost is at most `(Σ|ŵ|)²≤r`, not a new exceptional-spectrum estimate.
(P2) already allows arbitrary coefficients, (P3) is the ordinary large sieve,
and partial summation handles w(n)n^{it} with the same interval supremum.
In the induction only K₁ gains this factor; c and Q₀ do not. Therefore it yields
a DI7 periodic-coefficient variant with a fixed polynomial r loss, **not**
r^{O(δ^{-2})}. Residue-class indicators are also covered.

**Verdict:** the periodic DI extension is manageable. The proposed twisting route
is nevertheless harder/incomplete for the actual application: globally even
characters need not be squares, noncoprime coefficients are lost, and a polynomial
r loss is not the uniform conductor-free bound required by (EFF).

## 6. Gaps/caveats and concrete repairs

* Dr p. 17's single g(q)=Φ(q/Q) cannot majorize Q<q≤16Q. Restore DI p. 273's
  four applications at (2^jQ,2^jY), j=0,1,2,3; the switched C stays fixed.
  Also the printed support alone does not imply exactly C<c≤16C. One explicit
  repair: take Φ supported in [9/10,21/10], equal to 1 on [1,2], and
  φ(x)=Φ(5Yx/4). Then the support forces `(500/441)C<c<(1000/81)C`, inside
  (C,16C). Exceptional positivity and all derivative bounds change only absolutely.
* In the p. 17 Mellin identity the kernel integral needs **dx/x**, as in (4.10),
  not the printed dx; the second Fourier coefficient has index n, not m.
  Split σ at a fixed multiple of δ; bound the small range by Y^{δ} times an
  effective δ-dependent constant and the rest by δ^{-O(1)}Y^{2σ}.
* Dr p. 18 interchanges N,Y in S(Q,N,Y,0); read S(Q,Y,N,0). Prefix differences
  in its partial summation and the precise support constants cost only absolute factors.
* Neither “smaller C helps” nor “apply Thm 14” is sufficient by itself: §3 supplies
  the missing C<N/small-C branches; §2 uses the positive majorant and Thm 14's proof.
* The ledger establishes the dependency/envelope mechanism, not a numerical A.
  An unconditional numerical certificate still requires auditing the finite analytic
  constants in the transposed large sieve with the selected cutoff and Weil black box.
