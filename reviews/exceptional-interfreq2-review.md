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
| SPW plausibility | (pending) |

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

## Defects
