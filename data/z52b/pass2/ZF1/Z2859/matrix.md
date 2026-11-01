# Z2859 — standard conjectures × ES variants (what each hypothesis is KNOWN to give)

Columns: ES(p) (any solution), (★)/R(p) (c = 1 Type II line), ES₅ (five slices; ⟺ λ(p) ≤ 3 for p ≡ 1 (8), DEDEKIND_ES
Cor 4.6), I3 (n = tuv − u − v, t,u,v ≥ 3, n > 2 433 600). Each cell: density / exceptional-set rate / pointwise.
"—" = no implication known to the repo or to me. Pointers are depth documents; cells marked NEW are filled here.

| hypothesis | ES | (★) / R(p) | ES₅ (λ(p) ≤ 3) | I3 |
|---|---|---|---|---|
| unconditional (reference) | density 1; E(N) ≪ N exp(−c(log N)^{3/4}) (3/4 note); verified 10¹⁷ | fails at 14 primes ≤ 10¹⁰ (FRONTIER §2.1); M_BM ≥ 0.019 L² (Burgess) | λ(p) ≤ (6/π²) ln²p (bsA_farey_lnr_pigeonhole Thm 3); holds p < 10⁶ (DK) | density-1 exceptional set E_I3(N) ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3})-type (EXSET_I3 §§; I3_DEEP_ASTRA) |
| GRH (Dirichlet/Hecke) | density: same CRT cap exp(−C(log N)^{3/4+o(1)}) (CONDITIONAL_ES §5 (c), PRIMELAW Cor 4.2); pointwise: character expansion trivial, misses by p^{1−o(1)} (§3.1); Type II bounded-multiplier mechanisms with moduli ≤ exp((log p)^{1/4−ε}) fail i.o. (OMEGA13 Thm 5.1) | M_BM ∼ M₀ (FRONTIER §2.2; BM_LVALUE: L(1,χ_p) ≍ 1 up to loglog); M_gen(p) ≥ (1−o(1))loglog p only (SINGLE_P_COUNT (J)98); pointwise R(p) ≥ 1: — | NEW: λ(p) ≤ n_p ≤ 2 ln²p (Lemma 1 of bsA_farey_lnr_pigeonhole + Bach) — weaker than the unconditional (6/π²)ln²p by a constant only; λ ≤ 3: — | — (I3_DEEP_FABLE §6.3: GRH controls Σ_n χ(n), not Σ_χ at fixed n) |
| EH / GEH (and BV, BFI, Montgomery, Hooley) | same as GRH (c): averages over p, CRT cap 3/4 (sharp for the architecture, EXCEPTIONAL_KARY3); linear certificates capped at 1/4 (OMEGA15/16) | NEW ("EH for levels"): Σ_{p≤x} D_t⁻(tp+1) is a Titchmarsh-divisor sum in a class mod t — its asymptotic is already unconditional (BV + divisor switching); EH only improves error terms / uniformity in t. Pointwise at one p: — (METAPLECTIC Thm K reduces R_t to D_t⁻(tp+1); EH never sees one integer) | — (same reason) | — (I3_DEEP_FABLE §6.3: "EH averages over moduli with the integer variable free") |
| Schinzel H / Bateman–Horn / Dickson | works AGAINST bounded procedures: every bounded witness menu fails i.o. (POINTWISE_SIZE Thm C) | the bounded-C part of (★) fails i.o. (same) | t_min(p) unbounded under H (DEDEKIND_ES §10.1, via POINTWISE_SIZE Cor C1) | bounded-endpoint coverings fail i.o. (I3_DEEP_FABLE Prop 4.1, CONDITIONAL on H) |
| Chowla (λ/μ correlations; log-averaged odd order PROVED by Tao–Teräväinen) | — : correlations are averages over all n; NEW EVIDENCE (Z2603): λ-patterns on consecutive slices N_e carry no hardness signal at 102 327 primes in [10⁶,4·10⁶] | — | NEW ("Chowla for (·/p) along words"): the naive cancellation Σ_{A∈L₃(p)} (A/p) = o(|L₃|) is FALSE as a heuristic — signs are biased coins, fraction of −1 words: 0.695 (p ≤ 3·10⁵, DK §10.2, reproduced), 0.710 (930 primes ≡ 1 (8) in [10⁷, 1.006·10⁷], sd 0.079, min 0.375), 0.723 (56 primes near 10⁸, min 0.58); the bias is local (mod-4 word classes), so the needed statement is a pointwise "no conspiracy" law on a p-dependent polylog set — not a Chowla-type (interval/average) statement. Character-sum Chowla/GRH short-sum results (Σ_{n≤x}χ(n) = o(x) for x beyond polylog, Granville–Soundararajan, from memory) concern intervals only | — |
| Cramér (prime gaps; random model) | the random model predicts finiteness of failures (Σ_p e^{−c log²p} < ∞), but Cramér's CONJECTURE (gap statement) gives nothing: ES conditions are divisor-class conditions of p-tied integers, not prime locations; Cramér-scale covering statements over arbitrary systems are false (CONDITIONAL_ES Prop 7.2, §7.3) | same; (★) itself is a Cramér-scale-failure example (14 failures with M ≈ 12–20) | coin model predicts 0.67 failures ≤ 3·10⁵, observed 0 (DK §10.2) — heuristic only | — |
| SEL / GLH / Lindelöf (from CONDITIONAL_ES §5) | averages (Σ f_I ≪ N log²N now unconditional); fixed p: power-size errors, Prop 2.3 gap | — | — | — |

## What the matrix says (Assessment)
No row has a pointwise entry in any column. The only nontrivial conditional *positive* cells are main-term statements
(GRH: M_BM ∼ M₀) and averages; the only pointwise conditional statements (Schinzel H rows) are NEGATIVE (bounded
procedures fail). The missing hypothesis is, in every column, a one-sided class-equidistribution statement for the
divisors (or word signs) of ONE p-tied integer/set of polylog size (I3_DEEP_FABLE §6.4; BM_CORRECTED_COUNT §3.1 H⁻_BM).
The ES₅ word-sign data adds one refinement: that statement must be *biased* (local densities ≈ 0.71, rising slowly with p),
not a Chowla-type cancellation.

## Reproduce
gcc -O2 -o z scripts/z52d_p2_ZF1_Z2859_wordsigns.c; ./z 17 300000 (DK check); ./z 10000000 10060000; ./z 100000000 100004000.
Files: wordsigns_1e7.txt, wordsigns_1e8.txt (p |L₃| N₋). Overdispersion: sd 0.079 vs pair-binomial 0.050 at |L₃| ≈ 165.
