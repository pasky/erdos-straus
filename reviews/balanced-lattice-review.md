# R269 — hostile review of O256 (BALANCED_LATTICE.md, checkpoint 1 incl. R-O256 repairs 1–9)

Reviewer: R269 side agent (branch side-agent/review-balanced-lattice, merged side-agent/balanced-lattice at a5cf0e51).
Scope: BALANCED_LATTICE.md §§1–7, memos BRAINSTORM/z27_*.md, scripts/z27_{dual,eqcheck}.py, data/z27/, AGENT_REPORT_O256.md.
From-scratch scripts: scripts/review_r269_*.py (none reuse the author's code). Sources/ contains none of Banaszczyk 1993,
Serre 1981, Schinzel 1977: citation checks below are from the reviewer's knowledge of the statements and are flagged as such.

**Repairs applied (author quiet ≥ 2 h at review end):** BALANCED_LATTICE.md, marked "(R269 repair)", for D1, D3, D6, D7, D8(i,iii), D10,
D11, D13, D14, D16, D18, D19; BRAINSTORM/README.md z27 row (D17); AGENT_REPORT_O256.md SHARP 2 wording (D14). Not applied
(optional): D2, D4, D5, D8(ii) (constants), D9, D12, D15, D20.

## Overall verdict

**No FATAL and no MAJOR defect.** Every PROVED/CONDITIONAL claim survived a from-scratch re-derivation; the exponents 13/2
(GRH + EQ) and 9/2 (GRH + S) are correct as stated (with an o(1) of size O(log₄p/log₃p), D9); EQ and S are precise, p-free
(S also class-free), and not false for any trivial reason I could find (Brun–Titchmarsh regime, Chebotarev families of
Prop 5.2 type, extreme class a ≡ 1 (mod P)). All §6 EVIDENCE that I re-ran reproduces — the EQ tables at y = 7 and y = 11
exactly. Labels are honest ("bounded cap is not ES" is stated four times; no ES claim). 20 MINOR defects, mostly wording,
statement hygiene and citation precision (D1, D3, D7, D10, D11, D13, D14, D16, D17, D18 should be repaired; the rest optional).

## Summary verdicts (claim by claim)

| claim | verdict | notes |
|---|---|---|
| Lemma 1.1 (Λ*/ℤ^S ≅ Ĥ) | SOUND | re-derived; also checked numerically with an LLL dual basis built from an independent kernel computation (no characters used): λ₁^{(1)}(Λ*) = min(1, 𝔻_min) in 70/70 non-degenerate samples |
| Prop 1.3 (transference) | SOUND | constants re-derived: lower bound exact; upper uses μ_∞ ≤ μ₂, Banaszczyk μ₂λ₁^{(2)}(Λ*) ≤ k/2 (his formal bound, valid for every k, no o(1)), λ₁^{(2)} ≥ λ₁^{(1)}/√k. Discrete consequences via FORCED_WINDOW Prop 4.1(i)/(ii) correct. Numerics: μ_∞·min(1,𝔻) ∈ [0.51, 0.96] (k = 3) and [0.62, 1.11] (k = 4) against the proved window [0.5, k^{3/2}/2]; D1, D2 |
| Cor 1.4 | SOUND-AFTER-REPAIRS | (a), (c) correct; (b) is an "⟺ up to k^{O(1)}" whose two directions carry different constants (D3) |
| Prop 2.1 | SOUND | (a) re-derived (Frob_𝔔 ∈ Gal(K_m/ℚ(ζ_m)) ↪ Hom(⟨S⟩, μ_m); conjugation by σ_u gives b ↦ ub; ψ^m = 1 ⟺ ψ = χ_m^j\|_{U_q}, θ_s = 2jb_s/m since m odd). (b) b = a mod m checked numerically (40 q, all m \| N, m < 200: 0 mismatches). Scope can be widened (D4) |
| Prop 2.2 | SOUND (honestly scoped) | proof complete; the fake has L′_min = N₂ − 1 exactly in 12/12 real-q tests (data/review_r269/prop22_fake.txt; L_true ≈ 20). It is an information statement about abstract vectors and is labelled as such; it is not a barrier for statistical arguments (the text says so). D4, D5 |
| Assessment 2.3 | SOUND as Assessment | the \|C\|-linear GRH error is not the only available form; the conclusion survives the refined forms, but for a different reason (D6) |
| Prop 2.4 | SOUND | trivial; (b) duplicates 2.1(c) |
| Lemma 2.5 | SOUND | degree 2φ(lcm(8P,ℓ))ℓ^k re-derived; \|C\| ≤ 1 and C is a (central) conjugacy class; Serre's Thm 4 form (\|C\|/\|G\|)(log d + n log x)√x = \|C\|√x(log d/n + log x) and Prop 6 (log d/n ≤ Σ_ram log r + log n) quoted correctly (from memory; PDFs not in sources/). Densities match numerically (D7) |
| Prop 3.1 | SOUND | every step re-derived (fibre bound N(2Bε + 1/d), Cauchy–Schwarz, Π ≥ 4(B+1)^k, Fejér identity Σ_h w(h)[q \| N_h], \|N_h\| < P^{2B}); the constants are slack: the proof gives (4/3)B(2B+1)xε log P/log(x/2) and 8(6xε)^{(k+1)/(k−1)}…, stated 4B(2B+1)… and 48(…). Each proof step checked numerically for every Bad₁ prime (D8) |
| Prop 3.2 | SOUND | (wording: "1/d > ε" should be "1/d ≥ ε > 𝔻"; D8) |
| Cor 3.3 | SOUND (as bookkeeping; "PROVED + arithmetic" is fair for the displayed L, the "no class-blind bound can recover" sentence is Assessment) | exponent arithmetic and the y-optimisation to exp(O(√(log₂p log₃p))) re-derived (y ≈ 2√(log₂p log₃p) when log x ≈ 4 log₂p) |
| Hypothesis EQ | precise; not trivially false | p-free; uniform in y (P ≤ √x), ε, class. Not false for trivial reasons: (i) at ε where Bad₁ has positive density it is a Brun–Titchmarsh-type statement; (ii) its Chebotarev-visible part (index-ℓ degeneracy with ℓ > 1/ε) has ℓ > 1/ε > y, so ℓ ∤ 8P and the splitting fields are linearly disjoint from ℚ(ζ_{8P}) (D7's abelianisation argument) — equidistributed mod 8P, consistent with EQ; the class-correlated index part (ℓ ≤ y) lies in Bad₂, as the author's numerics show; (iii) it is trivially true when P ≥ x^{1/2}(log x)^{−A+1} (each class has ≲ √x log y/log x primes), but non-trivial where used (P ≍ √x/log²p). Domain of q unstated (D11) |
| Hypothesis S | precise; not trivially false | p-free and class-free as claimed. Toy test (from scratch, all q ≤ 2·10⁵): y = 5: 1 prime, y = 7: 1 prime in Bad₁(x^{−3/(2k)}), vs x^{1/2} = 447; the uniform-random model with the 1/ζ(k)-primitive and ± corrections predicts O(5). Prop 5.2-type families: the index-degenerate part needs ℓ > x^{3/(2k)}, where GRH-Chebotarev least-prime bounds give q ≲ ℓ^{2k} > x³, so they produce no counterexample. Uniformity over all y is more than needed (D12) |
| Thm 4.1 | SOUND (relative to GRH + EQ) | every inequality re-derived: Bad₂ main ≤ G·Σ_{ℓ≥3}ℓ^{−k}, error/G ≍ z log x/log p → 0; Bad₁ main = 48c₃x/(φ(8P) log(x/2)) by the choice of ε; EQ error/G ≍ (log x)^{A+1}/log²p → 0; 1/ε = 6x^{2/(k+1)}(C log P/c₃)^{(k−1)/(k+1)} = y^{5+o(1)}; L = y^{13/2+o(1)}; FORCED_WINDOW Thm 4.3 applicable (y ≤ log p, L = L(p) not q-dependent per R264 D7, q ≤ X(p)). Exponent evaluated numerically (D9) |
| Thm 4.2 | SOUND (relative to GRH + S) | ε = x^{−3/(2k)}: 1/ε = y^{3+o(1)}, L = y^{9/2+o(1)}; S's total ≤ x^{1/2}(log x)^A ≤ G/8. Hypotheses should be spelled out (D10) |
| Reading after 4.2 ("S ⇒ EQ at the parameters used") | SOUND | only at ε = x^{−3/(2k)} (Bad₁(ε) is not monotone in ε) |
| Remark 4.3 | SOUND (Assessment-level, not new) | Markov over classes + equidistribution of −p mod 8P (needs GRH for primes in progressions to modulus 8P = (log p)^{(1+o(1))log₃p}, beyond Siegel–Walfisz — available since GRH is assumed) and x frozen per dyadic p-block; correctly declared weaker than CAP_INTERPOLATION §2 |
| Prop 5.1 (narrowed) | SOUND | trivial size statement (2^k = P^{o(1)} ≪ \|U_q\| ≍ x ≥ P²) correctly labelled; the counterexample to the unnarrowed version re-verified from scratch: (11/409) = −1, K = (409 + 11)/4 = 105, t = −105 ≡ 5 (11), W₀ = {3^{2j₁}5^{2j₂}7^{2j₃}} = {1, 3, 4, 5, 9} = U₁₁ |
| Barrier screen §5 | SOUND | B5/T1: (q/m²) = 1 for q ∤ m, so no forced windows at squares — correct and algebraic; B2 handled by Prop 5.1 |
| §6 ν statistics | SOUND-AFTER-REPAIRS (EVIDENCE) | reproduced from scratch (600 q, k = 3; 400 q, k = 4); the 1 % quantiles quoted must be conditioned on 𝔻_min > 0 (D13) |
| §6 order statistics | SOUND (EVIDENCE); wording (D14) | reproduced: k = 3: ord = N 0.78 (random 0.75), ≥ N^{0.9} 0.89 (0.88), P⁺(N) \| ord 0.995 (0.997); k = 4: 0.76 (0.80), 0.86 (0.88), 0.995 (0.995); ≤ N^{1/2}: 0 resp. 0.25 % |
| §6 per-class ν (mod 840) | SOUND (EVIDENCE) | reproduced: q ≤ 3·10⁵ (6493 q from q = 11; the author's 6450 start at ≈ 10³): min over classes of the best ν = 1.481, median 1.572 (author 1.481 / 1.575); 29 classes have a degenerate q |
| §6 EQ at y = 7 (mod 840) | SOUND (EVIDENCE), reproduced exactly | from-scratch run over all 19 609 q ≡ 3 (8) in [10³, 10⁶]: Bad₁ counts 250 / 1272 / 3463 and χ² 49.5 / 28.0 / 29.8, full set 653 / 1670 / 3848, χ² 213.9 / 96.1 / 64.7 — identical to data/z27/eqcheck_y7.txt; my permutation p (1000 perms) 0.34 / 0.97 / 0.87 and 0.001 / 0.001 / 0.006 (D15) |
| §6 EQ at y = 11 (mod 9240) | SOUND (EVIDENCE), reproduced exactly; one follow-up (D19) | from scratch, all q ≡ 3 (8) ≤ 2·10⁶ (37 259 incl. 42 q < 10³ that carry no events): Bad₁ 72 / 653 / 2513, full 310 / 889 / 2747, χ² 543.6 / 474.2 / 405.6 — identical to the author's; permutation p 0.034 / 0.455 / 0.937 |
| Labels; "bounded cap is not ES" | SOUND | stated in the header, §5, §7.4 and the report; no ES claim anywhere; CONDITIONAL labels on Thms 4.1/4.2 correct; Assessment 2.3 correctly demoted |

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
(c log M)^k = exp(k log(c log M)) with k ≍ y/log y, y = log₂p·log₃p, M ≥ 1/ε ≥ y, is ≈ exp(log₂p·log₄p) ≫ log p
(and the balance-deciding orders are ≍ N in any case, §6). *Repair:* add one sentence acknowledging the refined error terms and
this computation; otherwise the "(log p)^{O(1)} bad elements" heuristic looks like an artefact of the crude form.

(Addendum to D6: the Kummer-vector count "≤ φ(m)·#{c : |c_s| ≤ εm}" is for characters of *exact* order m (j a unit); for
"order dividing m" the non-unit j contribute b-sets of size g^k·#{…} at gcd(2j, m) = g. Since those characters are counted
at level m/g anyway, say "exact order m".)

**D7 (MINOR) — Lemma 2.5 proof, the √p step.** "(Schinzel again)" for "the maximal abelian subfield of ℚ(ζ_n, S^{1/ℓ}) is ℚ(ζ_n)"
is not what Schinzel's theorem says; the direct argument is two lines: Gal = (ℤ/ℓ)^k ⋊ (ℤ/n)^* with u acting by
multiplication by u mod ℓ; for u ≢ 1 (ℓ) the commutators (u − 1)v exhaust (ℤ/ℓ)^k, so the abelianisation is (ℤ/n)^*; and
ℚ(√p) ⊄ ℚ(ζ_n) as p ∤ n. *Repair:* replace the parenthetical by this argument. From-scratch numerics
(scripts/review_r269_frobenius.py C): q ≤ 6·10⁶ in σ₀ (q ≡ 3 (8), q ≡ −p (P), χ_p(q) = −1): y = 5, ℓ = 3 ∈ S, p = 17:
713/6463 = 0.1103 vs predicted 1/9; ℓ = 7 ∉ S: 23/6463 = 0.0036 vs 1/(6·49) = 0.0034; y = 7, ℓ = 3, p = 41: 30/1056 = 0.028
vs 1/27 = 0.037 (1.5σ). Consistent with the degree count.

**D8 (MINOR) — Prop 3.1 / Prop 3.2 statement hygiene.** (i) Bad₁(ε) is defined for "q prime" but g_s = s² mod q needs
q ∤ 2P (and the notation section restricts to q ≡ 3 (mod 4)); for x/2 < y the set (x/2, x] meets S. *Repair:* define Bad₁ for
odd primes q ∤ P, and say whether q ≡ 1 (mod 4) is included (it matters for Hypothesis S, see D11). (ii) The constants 4 and 48
can be 4/3 and 8; harmless. (iii) Prop 3.2 proof: "1/d > ε" → "1/d ≥ ε > 𝔻_S(ψ)". From-scratch numerics
(scripts/review_r269_fejer.py P): y = 7, x = 2·10⁴, ε = 0.014, B = 33: 8 Bad₁ primes, every proof inequality holds;
Σ_q(Π − (B+1)^k) = 2.3·10⁸ vs the bound 5.2·10¹⁰; y = 5, ε = 0.004, B = 319: 70 Bad₁ primes, 0 failures, 2.1·10⁹ vs 2.0·10¹²
(the per-relation charge 2B log P/log x is the main slack, as the author's Reading says).

**D9 (MINOR, informative) — size of the o(1) in Thms 4.1/4.2.** From-scratch evaluation of the paper's own parameter choices
(scripts/review_r269_exponents.py, data/review_r269/exponents.txt; C₀ = C = 10³, c₃ = 10⁻³): log L/log log₂p equals
12.3, 10.8, 9.9, 9.3, 8.9 (Thm 4.1) and 6.2, 5.8, 5.6, 5.4, 5.3 (Thm 4.2) at log₂p = 10², …, 10⁶; measured against log y the
values are 7.5 and 4.46 at log₂p = 10⁶. The limits 13/2 and 9/2 are right, but the o(1) is O(log₄p/log₃p) (from
log x/y = 2 + O(1/log₃p), y/k = log y − 1 + o(1), and log y = log₃p + log₄p + …). *Repair (optional):* write
(log₂p)^{13/2 + O(log₄p/log₃p)}, or state the bound as y^{13/2+o(1)} with y = log₂p·log₃p.

**D10 (MINOR) — Thm 4.2 statement.** "CONDITIONAL on GRH + S" without saying which GRH. *Repair:* "Assume GRH for Dirichlet
L-functions and for the Dedekind zeta functions of ℚ(ζ_{lcm(8P,ℓ)}, √p, S^{1/ℓ}) (ℓ odd prime ≤ y^{3+o(1)}), and
Hypothesis S."

**D11 (MINOR) — domain of Bad₁ in EQ and S.** The notation section takes q ≡ 3 (mod 4), Prop 3.1 says "q prime", S says
"#{q ≤ x : q ∈ Bad₁}". For q ≡ 1 (mod 4), U_q has even order and the definitions still make sense, but the application needs
only q ≡ 3 (mod 8), q ∤ P. *Repair:* state EQ and S for primes q ≡ 3 (mod 8), q ∤ P (weakest form); this also removes the
doubt whether the 2-part of q − 1 could carry pretentious characters of order > 1/ε.

**D12 (MINOR, optional) — S is stated more uniformly than used.** S quantifies over all y with P(y) ≤ x^{1/2}, but Thm 4.2
uses one y = y(x) (inverse of x = C₀φ(8P(y))² log⁴p, i.e. log x = (2 + o(1))y) and only q ∈ (x/2, x]. *Repair:* record the
minimal form "for y = y(x) with x ≍ P(y)²·exp(O(y/log y)) and q ∈ (x/2, x]" next to the uniform one; the weaker statement is
the one whose plausibility matters.

**D13 (MINOR) — §6 first bullet, ν quantiles.** The quoted 1 % quantiles (k = 3: 0.267 true / 0.265 random) cannot include the
index-degenerate q (ν = 0), which are 52/3000 = 1.7 % > 1 % of the sample by the author's own count; my from-scratch run
(scripts/review_r269_sec6.py nu; data/review_r269/nu_k3.txt) has 9/600 degenerate and 1 % quantile 0.000 unconditionally.
The other quantiles agree: k = 3: 10/50/90 % = 0.550/1.032/1.380 (true) vs 0.547/1.000/1.375 (random); k = 4: 0.736/1.221/1.563
vs 0.749/1.187/1.541 (author: 0.784/1.208/1.532 vs 0.743/1.194/1.535). *Repair:* say "quantiles conditioned on 𝔻_min > 0".

**D14 (MINOR, wording) — "the extremal character has order ≍ N" (§6, §7.1, report SHARP 2, brief's "ord ψ_min ≍ N in > 99 %").**
What is measured in > 99 % is P⁺(N) | ord ψ_min; ord = N holds in ≈ 75 % and ord ≥ N^{0.9} in ≈ 87 %. "≍ N in > 99 %" is not
shown (and P⁺(N) is typically ≈ N^{0.6}). The doc's own sentence in §7.1 ("order ≍ N (§6; P⁺(q−1) | ord in > 99 %)") conflates
the two. *Repair:* "ord ψ_min is divisible by P⁺(q − 1) in > 99 % and equals N in ≈ 75 %". The conclusion drawn (balance is
decided outside the Frobenius-visible small orders) needs only the P⁺ statement, so nothing else changes. Also "ties": several
characters (at least ψ, ψ̄) attain 𝔻_min; the statistic should say which minimiser's order is reported (my run reports the
largest-order minimiser and, for the "small order" rows, the smallest-order one; numbers unchanged).

**D15 (MINOR, interpretation) — §6 EQ test: under-dispersion and what the test can show.** At t = 0.5, 0.7 the Bad₁ χ² (28.0,
29.8 on 47 df) is *below* the permutation null (medians 43.1, 37.9): upper-tail p = 0.97 / 0.87 means a lower-tail p ≈ 0.03 / 0.13,
i.e. Bad₁ is spread *more* evenly than chance at t = 0.5. This is harmless for EQ (an upper-bound statement), and not
significant after the 6 tests, but "no over-concentration" is the only conclusion supported; the text should not read it as
"equidistributed". More importantly the test is at P = 105 ≪ √x = 10³ and each class holds ≈ 400 q, whereas EQ is used at
P ≍ √x/log²p, where a class holds ≍ √x·log²p/log x primes and the hypothesis is about a √x-level error. The author says
"EVIDENCE for EQ only at P ≤ 1155, nowhere near P ≈ √x" — correct; keep that sentence in the report's SHARP 3 as well.

**D16 (MINOR) — Thm 4.1 proof, "Bad₂ main term ≤ G/8".** This compares the Lemma 2.5 main term
((li(x) − li(x/2))/(2φ(8P)))·Σ_{ℓ≥3}ℓ^{−k} (Σ_{ℓ≥3}ℓ^{−3} = 0.0498 — true but with almost no room, prime-zeta P(3) − 1/8) with
G ≥ c₂x/(φ(8P) log x), where c₂ is only the implied constant of FORCED_WINDOW Thm 4.3's "≫". The comparison needs the
asymptotic G = (1 + O(C₀^{−1/2}))(li(x) − li(x/2))/(2φ(8P)) (which the GRH count does give, dyadically, for C₀ large), not just
"≫". *Repair:* state G in that asymptotic form, and use Σ_ℓ ℓ^{−k} → 0 (k → ∞) rather than the 0.05 numerics.

**D17 (MINOR, bookkeeping) — BRAINSTORM/README.md z27 row.** The z27_small_exponent_windows row still says "needs
E ≥ (log p)^{c log₃p}", the pre-repair bound; the memo (R-O256 repair 8) and §0 (I4) now say "cap ≳ log p i.o." (Linnik with
primorial modulus: log p = Θ(T), which I re-derived). *Repair:* update the README row.

**D18 (MINOR, wording) — §4 Reading after Thm 4.2.** "Bad₁ is neither a set of primes in progressions nor a Chebotarev set
(Prop 2.2)": Prop 2.2 is an information statement about abstract vectors and does not prove that Bad₁ is not a (finite union
of) Chebotarev set(s) — trivially any finite set of primes is one. *Repair:* "Bad₁ is not determined by Frobenius data in
Kummer–cyclotomic fields of degree ≤ (log p)^{O(1)} (Prop 2.2, abstract-vector sense)". Similarly §7.1 "the reason is exact"
rests partly on Assessment 2.3; "the reason is explicit" would be accurate.

**D19 (MINOR, evidence follow-up) — the marginal y = 11 cell is the extreme class q ≡ 1 (mod 1155).** The p = 0.033 at
t = 0.3 comes entirely from class 6931 mod 9240, the unique class with q ≡ 1 (mod 3·5·7·11): 3 of its 66 primes are in Bad₁
(4.5 %) against 69/37 193 (0.19 %) elsewhere (q = 1 448 371, 1 623 931, 1 753 291; two minimisers of order N, one of order
1045 = 5·11·19 with ψ(g₅) = ψ(g₁₁) = 1). This class matters conceptually: in Thm 4.1 the class is −p mod 8P, and for
p ≡ −1 (mod P) every candidate window has P | N, i.e. the Frobenius-visible smooth part of N is ≥ P ≍ √x/log²p — the regime
farthest from Prop 2.2's "large rough part". Stratifying by w := #{ℓ ∈ S : ℓ | N}: at y = 7 there is no trend in Bad₁ (rates
0.0137 / 0.0126 / 0.0119 / 0.0096 for w = 0..3 at t = 0.3); a pre-specified re-test of class 6931 vs a w = 0 control class
(3467 mod 9240) on fresh primes q ∈ (2·10⁶, 3·10⁷] (908 primes in each class; data/review_r269/cls*_y11*.txt) gives Bad₁
3 vs 3 (t = 0.3), 19 vs 16 (t = 0.5), 48 vs 69 (t = 0.7): no enrichment (while the *full* set is enriched, 14 vs 3 at
t = 0.3, as the Chebotarev-visible part should be) — the cluster is a fluke (look-elsewhere probability that some class of 480 gets ≥ 3
at mean 0.15 is ≈ 0.25). *Repair:* add this to §6 and name the class a ≡ 1 (mod P) as the natural worst case for EQ in any
future test.

**D20 (MINOR, informative) — Hypothesis S is stated at a threshold with a factor ≈ k^k of unused random-model room.** Under
the uniform model the expected #Bad₁(ε) ∩ [1, x] is ≈ x²(2ε)^k/(4ζ(k)k! log x) (± pairs, primitive vectors). At
ε′ := (k/2e)·x^{−3/(2k)} this is ≈ x^{1/2}/(√k log x) — still inside S's allowance — and gives 1/ε′ = y^{2+o(1)}, hence
L = k^{3/2}/ε′ = y^{7/2+o(1)}; with an ℓ^∞ transference of constant O(1) (numerically μ_∞·𝔻_min ≤ 1.11, D2) it would be
y^{2+o(1)}, exactly Cor 4.4's random-lattice (log₂p)^{2+o(1)}. So "S is the random-model prediction, with room" is right, and
the exponent 9/2 reflects the chosen ε and the k^{3/2} transference, not the random model. *Repair (optional):* add this
remark after Thm 4.2 (no change to the theorem).
