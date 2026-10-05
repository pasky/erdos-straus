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
| Lemma 4.1, 4.2, 6.1 | (pending) |
| Cor 5.1, Lemma 5.0 | (pending) |
| Thm 5.2 | (pending) |
| Prop 9.1 | (pending) |
| Lemma 9.2 | (pending) |
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

## Defects
