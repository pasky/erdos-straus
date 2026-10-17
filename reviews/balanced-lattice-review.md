# R269 — hostile review of O256 (BALANCED_LATTICE.md, checkpoint 1 incl. R-O256 repairs 1–9)

Reviewer: R269 side agent (branch side-agent/review-balanced-lattice, merged side-agent/balanced-lattice at a5cf0e51).
Scope: BALANCED_LATTICE.md §§1–7, memos BRAINSTORM/z27_*.md, scripts/z27_{dual,eqcheck}.py, data/z27/, AGENT_REPORT_O256.md.
From-scratch scripts: scripts/review_r269_*.py (none reuse the author's code). Sources/ contains none of Banaszczyk 1993,
Serre 1981, Schinzel 1977: citation checks below are from the reviewer's knowledge of the statements and are flagged as such.

## Summary verdicts (filled in claim by claim)

| claim | verdict | notes |
|---|---|---|
| Lemma 1.1 (Λ*/ℤ^S ≅ Ĥ) | SOUND | re-derived; also checked numerically with an LLL dual basis built from an independent kernel computation (no characters used): λ₁^{(1)}(Λ*) = min(1, 𝔻_min) in 70/70 non-degenerate samples |
| Prop 1.3 (transference) | SOUND | constants re-derived: lower bound exact; upper uses μ_∞ ≤ μ₂, Banaszczyk μ₂λ₁^{(2)}(Λ*) ≤ k/2 (his formal bound, valid for every k, no o(1)), λ₁^{(2)} ≥ λ₁^{(1)}/√k. Discrete consequences via FORCED_WINDOW Prop 4.1(i)/(ii) correct. Numerics: μ_∞·min(1,𝔻) ∈ [0.51, 0.96] (k = 3) and [0.62, 1.11] (k = 4) against the proved window [0.5, k^{3/2}/2]; D1, D2 |
| Cor 1.4 | SOUND-AFTER-REPAIRS | (a), (c) correct; (b) is an "⟺ up to k^{O(1)}" whose two directions carry different constants (D3) |
| Prop 2.1 | SOUND | (a) re-derived (Frob_𝔔 ∈ Gal(K_m/ℚ(ζ_m)) ↪ Hom(⟨S⟩, μ_m); conjugation by σ_u gives b ↦ ub; ψ^m = 1 ⟺ ψ = χ_m^j\|_{U_q}, θ_s = 2jb_s/m since m odd). (b) b = a mod m checked numerically (40 q, all m \| N, m < 200: 0 mismatches). Scope can be widened (D4) |
| Prop 2.2 | SOUND (honestly scoped) | proof complete; the fake has L′_min = N₂ − 1 exactly in 12/12 real-q tests (data/review_r269/prop22_fake.txt; L_true ≈ 20). It is an information statement about abstract vectors and is labelled as such; it is not a barrier for statistical arguments (the text says so). D4, D5 |
| Assessment 2.3 | SOUND as Assessment | the |C|-linear GRH error is not the only available form; the conclusion survives the refined forms, but for a different reason (D6) |
| Prop 2.4 | SOUND | trivial; (b) duplicates 2.1(c) |
| Lemma 2.5 | SOUND | degree 2φ(lcm(8P,ℓ))ℓ^k re-derived; |C| ≤ 1 and C is a (central) conjugacy class; Serre's Thm 4 form (|C|/|G|)(log d + n log x)√x = |C|√x(log d/n + log x) and Prop 6 (log d/n ≤ Σ_ram log r + log n) quoted correctly (from memory; PDFs not in sources/). Densities match numerically (D7) |

## Defects

**D1 (MINOR) — Prop 1.3 proof, citation "Banaszczyk, Math. Ann. 296 (1993), Thm 2.1".** The PDF is not in sources/ (not
accessible to me). The inequality used, μ(L)λ₁(L*) ≤ n/2 (Euclidean), is indeed the bound Banaszczyk proves formally (the
sharper (1/(2π) + o(1))n is remarked at the end of his paper; cf. Miller–Stephens-Davidowitz, arXiv 1907.09020, Thm 1.1 and the
remark after it). To my recollection the μ·λ₁* statement is his Thm 2.2 (Thm 2.1 being λ_iλ*_{n−i+1} ≤ n); pages 625–635(6).
*Repair:* cite "Banaszczyk 1993, the covering-radius transference bound μ(L)λ₁(L*) ≤ n/2" without a theorem number, or
verify the number. No mathematical consequence.

**D2 (MINOR, informative) — Prop 1.3 constant k^{3/2}.** From-scratch check (scripts/review_r269_transference.py; data in
data/review_r269/transference_k{3,4}.txt: μ_∞ on a 1/m-grid, 𝔻_min by exact integer arithmetic, λ₁^{(1)}(Λ*) from an
LLL-reduced dual basis, L_min by exact sumset covering) finds no violation of any inequality in Prop 1.3 / Cor 1.4(a), and
μ_∞·𝔻_min ≤ 1.11 in all 70 samples, i.e. the k^{3/2}/2 = 2.6 (k = 3), 4.0 (k = 4) upper constant is never close to attained.
The 3/2 in the exponents 13/2 and 9/2 (Thm 4.1/4.2) comes entirely from this ℓ²-detour; an ℓ^∞/ℓ¹ transference with an O(k log k)
or better constant would lower it. Not a defect of correctness; Remark (1) after Thm 4.1 already says "not optimised".

**D3 (MINOR) — Cor 1.4(b).** "balanced at the random-lattice scale (L_min ≤ k^{O(1)}N^{1/k}) ⟺ (up to k^{O(1)}) no ψ ≠ 1 has
𝔻_S(ψ) ≤ N^{−1/k}k^{−C}": the two directions hold with different constants. *Repair:* state as two implications:
𝔻_min ≥ k^{−C}N^{−1/k} ⇒ L_min ≤ ⌈k^{C+3/2}N^{1/k}⌉; L_min ≤ k^{C}N^{1/k} ⇒ 𝔻_min ≥ 1/(L_min + 1) ≥ k^{−C}N^{−1/k}/2
(and 𝔻_min ≤ (k!/N)^{1/k} always, by (a)).

**D4 (MINOR, strengthening) — Prop 2.1(b) / Prop 2.2, scope of "visible data".** The data is restricted to m | N. For odd
m ≤ M with m ∤ N the Frobenius class of q in K_m ⊂ (ℤ/m)^S ⋊ (ℤ/m)^* is (v, q mod m) with v determined modulo
(1 − q)(ℤ/m)^S = gcd(m, q − 1)(ℤ/m)^S, i.e. by c mod gcd(m, q−1) (c = discrete logs of s in F_q^*) up to a unit — again a
function of a mod N₁ plus the quadratic data c mod 2, which does not enter Λ (g_s = s²). Adding any abelian field (q mod n,
χ_p(q)) changes nothing since the fake keeps q. So Prop 2.2 holds for the data {Frob_q in K_m : m ≤ M odd} ∪ {all abelian
data}. *Repair (optional):* state it in this form; it makes the "brief's route" reading airtight.

**D5 (MINOR, reading) — Prop 2.2 is information-theoretic only.** The fake a′ (all s ≠ s₀ are N₂-th powers) is the extreme
Prop 5.2-type degeneracy; real q realise such vectors with frequency ≈ N₂^{−(k−1)}. The proposition therefore excludes only
*per-q uniform* certification from low-order data; any statistical argument (as in §3–4 itself) is untouched. The text says
this ("statement about information, not probability"; "not addressed"), so no repair is required, but §7 Verdict 1's "no
function of that data … certifies" should keep the qualifier "uniformly over compatible abstract vectors" (it does).

**D6 (MINOR) — Assessment 2.3, choice of GRH error term.** The accounting uses Serre's Thm 4 error O(|C|√x(…)), linear in |C|.
Refined GRH-Chebotarev error terms exist (Murty–Murty–Saradha, Amer. J. Math. 110 (1988), |C|^{1/2}-type via a subgroup
H with H ∩ C ≠ ∅; Bellaïche, "Théorème de Chebotarev et complexité de Littlewood", Ann. Sci. ENS 49 (2016), error governed by
the Littlewood complexity λ(1_C)). For the Kummer part (abelian over ℚ(ζ_m)) λ(1_C) is at most the Fourier ℓ¹-norm of a union
of φ(m) ℓ¹-balls of radius εm in (ℤ/m)^k, ≲ φ(m)(c log(2εm + 2))^k — far smaller than |C| ≈ φ(m)(2εm)^k/k!. The conclusion
"GRH in the class controls little beyond the index condition" nevertheless survives at the §4 parameters, because
(c log M)^k = exp(k log(c log M)) with k ≍ y/log y, y = log₂p·log₃p, M ≥ 1/ε ≥ y, is ≥ exp((1 + o(1))log₂p·log₄p/1) ≫ log p
(and the balance-deciding orders are ≍ N in any case, §6). *Repair:* add one sentence acknowledging the refined error terms and
this computation; otherwise the "(log p)^{O(1)} bad elements" heuristic looks like an artefact of the crude form.

**D7 (MINOR) — Lemma 2.5 proof, the √p step.** "(Schinzel again)" for "the maximal abelian subfield of ℚ(ζ_n, S^{1/ℓ}) is ℚ(ζ_n)"
is not what Schinzel's theorem says; the direct argument is two lines: Gal = (ℤ/ℓ)^k ⋊ (ℤ/n)^* with u acting by
multiplication by u mod ℓ; for u ≢ 1 (ℓ) the commutators (u − 1)v exhaust (ℤ/ℓ)^k, so the abelianisation is (ℤ/n)^*; and
ℚ(√p) ⊄ ℚ(ζ_n) as p ∤ n. *Repair:* replace the parenthetical by this argument. From-scratch numerics
(scripts/review_r269_frobenius.py C): q ≤ 6·10⁶ in σ₀ (q ≡ 3 (8), q ≡ −p (P), χ_p(q) = −1): y = 5, ℓ = 3 ∈ S, p = 17:
713/6463 = 0.1103 vs predicted 1/9; ℓ = 7 ∉ S: 23/6463 = 0.0036 vs 1/(6·49) = 0.0034; y = 7, ℓ = 3, p = 41: 30/1056 = 0.028
vs 1/27 = 0.037 (1.5σ). Consistent with the degree count.
