# Hostile review R25: EXCEPTIONAL_INTERFREQ2.md (task O25)

Subject: branch `side-agent/interfreq-hybrid` (merged ff into
`side-agent/review-interfreq2`). Read: EXCEPTIONAL_INTERFREQ2.md (all),
AGENT_REPORT_O25.md, IF Thm 2.2/Cor 2.3/Lemma 2.4/Thm 2.5/Rem 2.6,
reviews/exceptional-interfreq-review.md, K2 Thm 5.1 (constants W, λ₀, C
absolute). Reviewer scripts: `scripts/review_if2_*.py` (from scratch; no
author code imported).

## Verdicts (filled in claim by claim)

| item | verdict |
|---|---|
| Def 1.2 | SOUND as a formalisation of IF Rem 2.6's last bullet (β* ≤ aN/d+|a| checked both signs); scope remark m1 |
| Prop 2.1 | SOUND |
| Lemma 3.1 | SOUND |
| Ex 3.2 + rigidity + Consequence | SOUND (brute force + LP, `review_if2_ex32.py`) |
| Lemma 4.1, 4.2, 6.1 | SOUND (all listed group elements re-checked) |
| Cor 5.1, Lemma 5.0 | SOUND (given IF Thm 2.5, which R18 found SOUND) |
| Thm 5.2 | SOUND as an implication; constants independent of N and of the family (see C7) |
| Prop 9.1 | SOUND (algebra of θ re-derived; τ = O(1) via Vaaler's K-bound) |
| Lemma 9.2 | SOUND for the proved direction; the 'converse by Farkas' and the §5/§10 readings of it overclaim (M1) |
| SPW plausibility | Reviewer opinion: plausible, with σ* = σ_C(N) of C11 (2/5 at C = 2) exactly at all tested N (EVIDENCE, C10–C11); the author's N-decay is truncation |

## Line-by-line checks

**C1 (Def 1.2).** β*(a,d) = a⌈N/d⌉ (a>0), a⌊N/d⌋ (a<0) is the least
charge ≥ a·c(b,d) over all b, since both l(d), u(d) occur as c(b,d) for
d > N/2 (N consecutive integers, d > N/2). IF Rem 2.6's charge
`aN/d + |a|` dominates it: a>0: ⌈N/d⌉ ≤ N/d + 1; a<0: −|a|(N/d) + |a| ≥
−|a|⌊N/d⌋ since ⌊N/d⌋ ≥ N/d − 1. Cutoff D_s < N/2 remark: correct
(β* ≥ exact count). Naturalness: yes for *per-term* blind charging, which
is exactly what IF Rem 2.6 described. See m1 for grouped charging.

**C2 (Prop 2.1).** Re-derived. Primal on ℤ/Q′: free small coefficients
(cost λ_N(s) = c(b,d) because d | Q′), large a = a⁺ − a⁻ with cost
u a⁺ − l a⁻, constraint ν ≥ 1_𝒜 pointwise (this encodes ν ≥ 0 and ν ≥ 1 on
𝒜). Dual variables μ ≥ 0, equality on small classes, μ(s) ≤ u, μ(s) ≥ l.
Both feasible (ν ≡ 1; μ = λ_N). Weak duality term-by-term correct;
`H* ≥ inf_{Q′} max μ(𝒜)` correct since every representation has some Q′.

**C3 (Lemma 3.1).** For d > N/2, c ∈ {l,u}, u − l ≤ 1, u = l only for
d | N, i.e. d = N among large d. Formula (3.1) follows termwise. SOUND.

**C4 (Ex 3.2).** `review_if2_ex32.py` (output `data/review_if2_ex32.txt`):
the 15-term identity holds on [−2000, 2000); small part exact count = −12,
large β* = +12 (all 12 classes full), total 0; written as itself the class
costs 1. LP over 𝔐(2520) at N = 20: min = max = 0 on `0 mod 21` and
min = max = 1 on each of the other 20 classes mod 21, so 𝔐 is rigid on
the whole of ℤ/21 exactly as claimed. Consequence (N+1 = d₁d₂, coprime,
d_i ≤ N/2): my simpler proof — every nonzero x mod N+1 is ≢ 0 mod d₁ or
mod d₂, and the d₂ (resp. d₁) lifts of a nonzero row are nonzero residues
in [1,N], hence full; rigidity gives μ(x) = 1 for all x ≠ 0, and total mass
N forces μ(0) = 0. LP on ℤ/(N+1) confirms μ(0 mod N+1) ≡ 0 for all 41
such N ≤ 119 (projection to ℤ/(N+1) of any μ ∈ 𝔐(Q′) lies in
𝔐(N+1), so this covers every Q′). The conclusion "no bound
B_hyb(ν) ≥ c·N·Eν for ν ≥ 0" is correct (ν = 1[0 mod 21] ≥ 0, B_hyb = 0,
Eν = 1/21).

**C5 (Lemma 4.1/4.2/6.1).** c(·,d) = ⌊N/d⌋ + 1_{I_d}, I_d = {1,…,N mod d};
so any φ with φ_d(I_d) = I_d for small d ∤ N keeps the small profile, and
large counts stay in [l,u]. Checked: L₀-translations (φ_d = id);
x ↦ N+1−x maps {1..r} to {N..N+1−r} ≡ {r..1} (mod d); a reflection on one
prime p ∈ (N/4, N/2] touches only d = p (p² > N/2 for N > 8, and pm ≤ N/2
forces m = 1); any affine map on p > N/2 touches no small d. Lemma 4.2:
{b − kL₀ mod d : k} is exactly the class b mod gcd(d,L₀), so all μ_k vanish
iff b mod e misses [1,N], impossible for e ≤ N. SOUND.

**C6 (Lemma 5.0, Cor 5.1).** Negative sparse terms with d > N: c = 0 and
β* = a·⌊N/d⌋ = 0, so deleting them changes neither Σ_{n≤N}ν nor B_hyb and
keeps a majorant. After that the large terms are exactly
W⁺ ⊔ (right-signed, N/2 < d ≤ N) ⊔ wrong-signed, B ≥ B_hyb ≥ T_wr, so
T_> ≤ (1+c)B and IF Thm 2.5 applies with c+1; the second form follows by
splitting on B ≥ (N/48)e^{−S_A}. SOUND.

**C7 (Thm 5.2).** Re-derived (5.1): with Eν = Eν_𝒮 + Σ_𝓛 a_i/d_i,
Σ F ν = M·Eν + Σ_𝓛 a_i(F(s_i) − M/d_i). Per-term lower bounds for
d > CN: patch ≥ a s₀ (F3); positive sparse ≥ 0 (F4, using the +|a|
penalty); negative full: |a|(1 + M/d − F(s)) ≥ 0 since F ≤ 0 off [1,N]
gives F(s) ≤ F(n₀) ≤ 1. Medium right-signed ≥ −Δ|a|, medium wrong ≥
(1−Δ)|a| ≥ −Δ|a|, and Σ over wrong ≤ T_wr ≤ B, giving the (1+Δ)B. Then
s₀W⁺_{>CN} ≤ KB because M·Eν ≥ 0; T_{>CN} ≤ KB/s₀ + B; t ≤ 1 is
automatic from (F1)–(F2) (M = ΣF ≤ N). Levels: a projected term of level
> λ ≥ log(CN) comes from d > CN, so IF Thm 2.5's coarsening goes through
with T_{>CN}; log T_{>CN} ≤ (A₁+1)log N + log 2. K2 Thm 5.1's W, λ₀, C
are absolute, so S′ depends only on A, A₁ (and C through log(CN)); t, Δ,
c enter only through log((1+Δ(1+c))/t). No hidden N- or family-dependence
found. Caveat (m2): the hypothesis is per-N, so "the cap" needs Flat at
*every* large N with s₀ ≥ N^{−A₁}, t ≥ e^{−S_A}, Δ ≤ e^{S_A}; the
statement is correct as written but the §0 summary should say so.
Remark (iii) is right: for ν = 1[0 mod N+1] in the form of Ex 3.2,
0 = Σ_{n≤N}ν ≥ ΣFν = M/(N+1) + Σ_patches(F(s) − M/d) contradicts (F3)
at d = N+1 even with s₀ = 0.

**C8 (Prop 9.1).** F_S = −½[B(δ(a−x)) + B(δ(x−b))], a = 1/2, b = N+½,
δ = 2/N, F̂_S(0) = N/2 = M/θ. Vaaler 1985 (Lemma 5: |sgn − H| ≤ K,
B = H + K, K(x) = (sin πx/πx)²) gives 0 ≤ B − sgn ≤ 2K, hence
|F_S(x)| ≤ 2K(δ·dist(x,I)) outside I; the k-th outside point of a class
of modulus d > CN is at distance ≥ (k−1)d, so τ ≤ ‖F_S‖_∞ + O(1 + Σ_k
(N/(2kd))²) = O(1). (F2): Lemma 2.4 exact for d ≤ D = N/2, M = θN/2.
(F3): (1−θ)σ − θτ = σ − θ(σ+τ+1/(2C)) + θ/(2C) = σ/2 + θ/(2C) ≥ s₀ + M/d
since M/d < θ/(2C). (F4): ≥ −1 + θ + σ/2 + θ/(2C) ≥ M/d − 1 (slack θ+σ/2).
(F5): 2(N+D)/D = 6 at D = N/2; |F − M/d| ≤ 6θ + (1−θ)Δ₀. (F1): convex
combination of two functions ≤ 1_{[1,N]}. SOUND. I could not open Vaaler
1985 here (not in sources/); the K-bound is the standard one and is used
the same way in IF Thm 2.2.

**C9 (Lemma 9.2).** Identity Σ_{n≤N}ν = ΣRν + Σz_i(c − R) + Σ_med a(c − R)
re-derived; (P2) gives c − R ≥ σ on full, ≥ −(1−σ) on sparse classes. SOUND.

**C10 (SPW numerics, from scratch: `review_if2_spw.py`).** Two LPs that
bracket the best σ in SPW(C, σ, ·) at N (P3 only measured):
`per` = necessary condition on ℤ/L₀ (any SPW R projects to a measure on
ℤ/L₀ with (P1) and (P2) for all d | L₀, d > CN) → *upper* bound;
`win a` = R supported on [−aN, (a+1)N], (P2) for every d ≤ support length
and pointwise beyond → *lower* bound (a genuine finite-support SPW witness
up to floating point). Results (data/review_if2_spw.txt):

| C | N | per (upper) | win (lower), a |
|---|---|---|---|
| 2 | 12 | 0.500 | 0.400 (5) |
| 2 | 13–21 | 0.400 | 0.400 (5) |
| 2 | 30 | — | 0.400 (5), 0.400 (8) |
| 2 | 40 | — | 0.384 (5), **0.400** (8) |
| 2 | 60 | — | 0.378 (8), **0.400** (12) |
| 2 | 80 | — | 0.374 (10) |
| 1.5 | 13, 16, 20 | 0.20, 0.25, 0.25 | 0.20, 0.20, 0.25 (5) |
| 3 | 13, 16, 20 | 0.70, 0.625, 0.571 | 0.571, 0.571, 0.571 (5) |

Δ₀ ≤ 1.4 throughout. So at every N tested the optimum is pinned at
σ = σ_C(N) of C11 (2/5 at C = 2, 4/7 at C = 3, 1/5 or 1/4 at C = 1.5
depending on N; the `per` values above σ_C(N) are only because ℤ/L₀ lacks
the modulus kq used in C11), the upper and lower bounds coincide for 13 ≤ N ≤ 21, and the
author's decay with N (0.335 at N = 60, a = 5) is a truncation artefact:
it disappears at a = 12. This *strengthens* the author's §9 evidence. My
opinion on SPW: **plausible (EVIDENCE only)** — no sign of N-dependence;
the obstruction to σ > (C−1)/(C+½) looks like a fixed local one, not the
smooth-modulus phenomenon of §9.

**C11 (why 2/5: a simple universal upper bound, PROVED here).** The LP dual
at N = 13, C = 2 on ℤ/60 is supported on one small class and five large
ones: `1 mod 6` has c = 3 points in [1,13] and is the disjoint union of the
five classes 1, 7, 13, 19, 25 mod 30 (30 > 2N), so (P1)+(P2) give
3 ≤ 5(1−σ). In general, for N ≥ 7 pick q ∈ (N/3, N/2) with
c(1,q) = 3 and k = ⌈(CN+1)/q⌉ (≈ 2C+1 for q near N/2): (P1)–(P2) force
**σ ≤ 1 − 3/k**. Generally (`review_if2_c11.py`):
**σ ≤ σ_C(N) := min_{q ≤ N/2} (1 − ⌈N/q⌉/k_q)**, k_q = ⌊CN/q⌋ + 1.
σ_2(N) = 2/5 for every tested N (12 … 10⁵), σ_3 = 4/7 (N ≥ 13), σ_{1.5} ∈ {1/5, 1/4},
σ_1 = 0. Consequences:
(a) SPW with C ≤ 1 is impossible at every N (σ_1 = 0), independently of
Example 3.2 — a cleaner reason for the author's "C = 1 infeasible";
(b) σ_C → 0 as C ↓ 1 (q near N/2: 1 − 3/(⌊2C⌋+1)), so the medium range (N/2, CN] cannot be shrunk to
(N/2, (1+ε)N] at fixed σ; (c) the LP optima in C10 attain this bound
exactly, so nothing beyond this local obstruction is visible up to N = 60.
The win-LP value equals σ_C(N) in every run that reached its plateau
(C = 2: N = 12–21, 30, 40, 60; C = 1.5: N = 13, 16, 20; C = 3: N = 13, 16, 20).
The same argument applies to Flat ((F2)+(F3) on the same five classes).

## Defects

No FATAL or MAJOR defect found. Every PROVED item was re-derived; the
conditional chain SPW ⇒ Flat ⇒ (3/4 cap for hybrids with T_mid ≤ e^{O(S)}B)
is correct, with constants independent of N and of the family.

**M1 (MINOR, overclaim from Farkas on truncated LPs).** §5 ("*Medium moduli
are not freed this way*"), §10 bullet 2 ("By Farkas (finite truncations)
this means there are nonnegative ν whose patches above CN *are* cancelled by
medium-modulus terms"), Lemma 9.2 ("converse holds by Farkas") and
AGENT_REPORT_O25 l.71–72 ("a cap there must use ν ≥ 1 on 𝒜"). A Farkas
certificate of the finite-support LP (R or F supported on [−aN,(a+1)N]) is
a combination ν that is ≥ 0 *only on the support window*, not on ℤ; it is
not a nonnegative function, let alone a majorant. And C10 shows truncation
changes the optimum substantially (0.378 → 0.400 at N = 60). So the `med`
infeasibility does not establish the existence of a nonnegative ν, nor that
a medium-moduli cap "must" use arithmetic. Repair: either rerun `med` in a
*periodic* formulation on ℤ/L₀ (or ℤ/L₀·m) — its infeasibility does give a
periodic ν ≥ 0 on all of ℤ — or weaken the sentences to "finite-support
evidence suggests". (Contrast C11: ν = Σ_{b∈{1,7,13,19,25}} 1[b mod 30] − 1[1 mod 6] ≡ 0 is a
genuine ν ≥ 0 on ℤ with Σ_{n≤13}ν = 0, Z_full = 3, Z_sparse = 2, which is
how (9.1) caps σ at 2/5 at N = 13, C = 2; this is the kind of certificate
the `med` claim would need.)

**m1 (MINOR, scope of Def 1.2).** Def 1.2 is per-term blind charging, which
matches IF Rem 2.6. A method that charges a *group* of same-modulus large
classes by its worst-case count over shifts (shift-blind but not term-blind)
can pay less than Σβ*; it is not covered. Repair: one sentence in §1 saying
such grouped charges are outside the hybrid class (or that Lemma 4.1-type
duals cover them only when the group is shift-invariant).

**m2 (MINOR, presentation).** §0 row Thm 5.2 should repeat that Flat is
needed at every large N with s₀ ≥ N^{−A₁}, t ≥ e^{−S_A}, Δ ≤ e^{S_A}
(the body states this; the table does not). Also add C11's necessary bound
σ ≤ σ_C(N) (resp. its Flat analogue) to §9, since it explains the
pinned LP values 0.4 / 0.25 and the C = 1 failure.

**m3 (MINOR, citation).** Prop 9.1's decay `|F_S(x)| ≤ c₁/(1+δ²dist²)` should
cite the precise statement (Vaaler 1985, Lemma 5 / Thm 6: 0 ≤ B − sgn ≤ 2K,
K(x) = (sin πx/πx)²); not in sources/, so I checked it from memory of the
standard construction only.

Not checked: Lemma 4.2's sampled density "≤ 0.14" and the §7 toy LP table
(both EVIDENCE, not load-bearing).

## Overall

SOUND-AFTER-REPAIRS (M1 wording only). Labels are honest except the Farkas
reading in §5/§10/report. My independent LPs support SPW more strongly than
the author's (no N-decay once support is long enough), and identify the
exact local obstruction σ ≤ σ_C(N) (= 2/5 at C = 2).
