# R177 — hostile review of O177 (LDP_DEEP.md + BRAINSTORM/bsD_*.md)

Reviewer branch `side-agent/review-ldp-deep` (merged `side-agent/spark-higher-reciprocity`). From-scratch scripts:
`scripts/review_ld_*.py`. Labels as in DISCOVERIES.md. **ES is not solved anywhere; nothing below changes that.**

**Repairs applied (author quiet at end of review — no commits on `side-agent/spark-higher-reciprocity` after
86bdc7b0):** D1, D2a–c, D3a–c, D4a–c, D5, D6a–b, D8a–b, D9, D10a–c applied directly to LDP_DEEP.md,
BRAINSTORM/bsD_{eichler_degree_k,brauer_cores,genus_vacuity_LDp,missed_primes,metaplectic_cubic,artin_conjugation,
frobenius_closure}.md and reviews/agent-reports/AGENT_REPORT_O177.md, each marked "(R177 repair …)". Also the
R176-inheritance items below (D11). No numbers changed (all reproduced).

## Summary verdicts

**Bottom line.** No FATAL defect. Every numerical claim reproduces exactly from independent code; every PROVED lemma
re-derives. The defects are one false-as-written statement (D1, intended content correct), one wording error that
flips the F-Gram construction (D4a), and several label/scope overreaches — chiefly that the global "closed" verdicts
(degree-2 accident, F-rational loophole) are Assessments built on PROVED, scoped pieces (D2c, D4c, D10c). The
"degree-2 accident" can be upgraded to a precise statement about all ℚ-groups compact at ∞ (D2c).

| # | Claim | Verdict |
|---|---|---|
| 1 | bsD_eichler_degree_k Prop 1 / LDP_DEEP Prop A.3.1 | **SOUND-AFTER-REPAIRS** (RHS as written gives f ≡ +1; D1) |
| 2 | bsD_eichler_degree_k Prop 2 / LDP_DEEP Prop A.3.2 + "degree-2 accident" slogan | (i)–(ii) **SOUND** for maximal orders; slogan **SOUND-AFTER-REPAIRS** (scope/label; precise Kottwitz-type form offered; D2) |
| 3 | bsD_brauer_cores Thm 1 / LDP_DEEP Thm A.1 | **SOUND** (BL citations verified in sources/; numerics reproduced) |
| 4 | LDP_DEEP Prop A.4.1, A.4.2, F-Gram construction | A.4.1 **SOUND**; construction **SOUND-AFTER-REPAIRS** ("definite" → "positive definite", uses r even); A.4.2 identity SOUND, "closed" **GAP** as a PROVED claim (D4) |
| 5 | EVIDENCE: split-supported Type II certificates, cd ≤ 30 | **SOUND** (reproduced exactly to 10⁶; caveat: 54% of certificates have a prime side, which is automatically an F-norm; D5) |
| 6 | bsD_frobenius_closure Thm 2 (+ cubic dictionary) | **SOUND** (19934 closure tests); LDP_DEEP wording overreaches (D6) |
| 7 | bsD_missed_primes numbers (71; layers 2/12/0) | **SOUND** (all reproduced exactly) |
| 8 | bsD_genus_vacuity_LDp Prop 1, Remark 2 / LDP_DEEP B.1–B.2 | Prop 1 **SOUND** (rel. DIFF_DEEP Thm 1.1); Remark 2 SOUND as corrected, "O(1) per fixed order" mis-normalised (D8) |
| 9 | LDP_DEEP B.0 Gram form | **SOUND** |
| 10 | spot checks: bsD_metaplectic_cubic, bsD_drinfeld_rank_k, bsD_artin_conjugation | metaplectic: label GAP (PROVED from memory); drinfeld SOUND (Assessment); artin SOUND-AFTER-REPAIRS (D10) |

## Detailed findings

### Claim 5 — EVIDENCE "all but 5 of 9732 primes p ≡ 1 (24) < 10⁶ have a cd ≤ 30 Type II certificate whose f or f′ is an F-norm" — SOUND (numbers reproduced exactly; interpretation needs a caveat)
From scratch (`scripts/review_ld_split.py X 30`; own divisor enumeration from the factorisation; **every certificate is
converted into an explicit ES solution 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp), a = (f+1)/M, b = (f′+1)/M, and checked in
exact rationals**). Two definitions of "F-norm" (F = ℚ(ζ_M)⁺, M = 4cd):
S1 = author's "split-supported" (every ℓ | f has ℓ ≡ ±1 mod M; sufficient), S2 = exact criterion (f = N_{F/ℚ}𝔞 for an
O_F-ideal ⟺ for every ℓ^v ‖ f the residue degree g_ℓ = ord of ℓ in (ℤ/M)^×/{±1} divides v).

| X | #p ≡ 1 (24) | no cert | no S1 cert | no S2 cert | no cert with both sides S1 / S2 | frac certs S1 / S2 | frac with f or f′ prime |
|---|---|---|---|---|---|---|---|
| 2·10⁵ | 2212 | 0 | 3 (3361, 53089, 76441) | same 3 | 338 / 293 | 0.603 / 0.621 | 0.565 |
| 10⁶ | 9732 | 0 | 5 (3361, 53089, 76441, 549553, 967129) | same 5 | **1345** / 1178 | **0.582** / 0.601 | 0.536 |

Odd squares < 4·10⁴: 0 Type II divisor hits (T1 control) — reproduced. All author numbers (9732; 0; the 5 exceptions;
1345; 58%) reproduce exactly with S1; the exact notion S2 changes neither the exception list nor the conclusion.
**Caveat (defect D5):** 0.536 of all certificates have f or f′ *prime*, and a prime f ≡ −1 (mod M) is automatically
≡ ±1, i.e. automatically an F-norm. So "F-norm certificates exist" is ≈ "a certificate with a prime side exists";
the statistic carries essentially no information about the F-structure, which is consistent with (and actually
strengthens) the author's own "tautology" reading in A.4.2.

### Claim 7 — bsD_missed_primes numbers — SOUND (all reproduced exactly)
From scratch (`scripts/review_ld_missed.py 1000000`, 20 s; every hit converted to an explicit ES solution, Type I as
4/p = 1/(abdp) + 1/(acd) + 1/(bcd) with a = (f+p)/M, b = (f′+p)/M, Type II as in claim 5, checked in exact rationals):
9732 primes p ≡ 1 (24) < 10⁶; **0** Type I hits in the nine cd | 6 slices (the BM-blocking remark, checked
numerically as well as by (−1/p) = (2/p) = (3/p) = 1); **71** missed by cd | 6; cd | 60 (54 pairs (c,d)) misses
**2** = {76441, 950401}; cd | 126 (54 pairs) misses **12** = {3361, 62497, 83449, 141121, 144817, 273001, 290761,
298369, 401017, 733321, 806521, 849601}; cd | 16380 (972 pairs) misses **0** (checked on the 14 survivors; the rest
a fortiori since 60, 126 | 16380). Statistics (control = all 9732 primes instead of the author's random 600): mean least
QNR 11.96 vs 7.54; (p/5) = (p/7) = 1: 0.676 vs 0.244; 2 cubic residue 0.380 vs 0.330; 3: 0.352 vs 0.332; p cube mod 7:
0.366 vs 0.335; mod 9: 0.352 vs 0.333 — all as claimed (the cubic deviations are ≤ 1σ at n = 71).
Exponent bookkeeping checked by hand: 4cd | 240 ⇒ exp (ℤ/4cd)^× | 4; 4cd | 504 ⇒ exp | 6; 4cd | 65520 ⇒ exp | 12;
Σ_{m|60} τ(m) = Σ_{m|126} τ(m) = 54. Only presentation defects (D9: the table in the memo is broken markdown — "cd | 6"
inside a table cell splits the column; the layer counts are pairs (c,d), each carrying a Type I and a Type II slice).

### Claim 4 — LDP_DEEP Prop A.4.1, the F-Gram construction, Prop A.4.2 — A.4.1 SOUND; construction SOUND-AFTER-REPAIRS (wording makes it false as written); A.4.2 SOUND as an identity, "closed" is an overclaimed label (GAP in the PROVED tag)
**Re-derivation.** K = ℚ(ζ_M), F = K⁺, r = [F:ℚ] = φ(M)/2, O_F = ℤ[θ], θ = 2cos(2π/M). Gal(K/F) = {±1} ⊂ (ℤ/M)^×; for a
prime 𝔭 ∤ M of F over ℓ, N𝔭 = ℓ^g with g = ord of ℓ in (ℤ/M)^×/{±1}, and Art_{K/F}(𝔭) = Frob_ℓ^g = ℓ^g mod M ∈ {±1};
multiplicativity gives Art_{K/F}(𝔞) = N𝔞 mod M. Hence for f = N𝔞: f ≡ −1 ⟺ η(𝔞) = −1 (A.4.1) — correct and, as the
author says, a dictionary. If 𝔞 = (β), β ≡ 1 (mod M O_F): every conjugate σβ ≡ 1 (mod M O_F) (the ideal is Galois
stable), so the *element* norm N(β) ≡ 1 (mod M O_F ∩ ℤ = Mℤ); and f = N𝔞 = |N(β)| = (−1)^{#neg} N(β) ≡ (−1)^{#neg}.
So f ≡ −1 ⟺ odd number of negative conjugates. ✓. For β ≡ −1 (mod M O_F): N(β) ≡ (−1)^r. ✓.
r odd ⟺ φ(M) ≡ 2 (mod 4) ⟺ M ∈ {4, q^k, 2q^k : q ≡ 3 (4)} (this includes 3, 6), so M = 4cd > 4 ⇒ r even. ✓
**From scratch** (`scripts/review_ld_ray.py`, 6 s): for 16 moduli M = 4cd ∈ {8,…,120} (r up to 16), 60 random
β = 1 + Mγ and 60 random β = −1 + Mγ (γ ∈ ℤ[θ]), exact norms by resultant against the integer minimal polynomial of
θ, signs of the r real conjugates at 80 digits: 0 failures of N(β) ≡ 1, |N(β)| ≡ (−1)^{#neg}, and N(−1 + Mγ) ≡
(−1)^r. Residue degrees: the minimal polynomial of θ factors mod every prime ℓ < 400, ℓ ∤ M, into irreducibles of
degree exactly g_ℓ and ℓ^{g_ℓ} ≡ ±1 (M): 0 mismatches. The r-parity characterisation: 0 mismatches for 3 ≤ M ≤ 5000;
no M = 4cd > 4 has r odd.
**Defects.** (i) The F-Gram paragraph says (−β, −det T_F) "is ramified at the real places where T_F is *definite*"
and then assumes det T_F totally positive. Under that assumption T_F is definite at **every** real place, so the
count would be r (even) for every β and the parity would carry no information. The correct statement: (−β, −det)
ramifies at v ⟺ σ_v β > 0 and σ_v det > 0, i.e. T_F **positive** definite at v; the count is r − #neg ≡ #neg
(mod 2) **because r is even** — so the construction also silently uses r even (D4a). (ii) Sign normalisation drifts:
the construction uses β ≡ 1 (𝔪), the certificate in A.4.2 uses β ≡ −1 (mod 4cd O_F), and AGENT_REPORT's SHARP bullet
writes "f = N_{F/ℚ}(β)" — with the element norm, N(β) ≡ +1 always, so f ≡ −1 is impossible; it must be the ideal
norm |N(β)| (D4b). (iii) A.4.2 is tagged "PROVED" and the section ends "Closed". What is proved is the one-line
identity N(−1) = (−1)^r = +1 (r even); that *the loophole is closed* is an Assessment: it shows only that the
specific descent "take N_{F/ℚ} of an O_F-certificate" loses the target. Other descents (trace forms, restriction of
scalars of the F-Gram lattice to a ℤ-lattice of rank 2r, choosing F′ ⊂ F of odd degree — the author's own Spark 1)
are not excluded (D4c). The SHARP-list phrase "It closes because …" in AGENT_REPORT_O177 should be downgraded
accordingly.

### Claim 3 — bsD_brauer_cores Thm 1 / LDP_DEEP Thm A.1 (corestriction collapse) — SOUND (standard; minor scope/novelty remarks)
**Citations checked against `sources/bright-loughran-1908.02526.pdf`** (§2 works over any field k of char 0):
Prop 2.5 — Br Ũ_{n,k̄} → Br V_{n,k̄} is an isomorphism, Br Ũ_{n,k̄} ≅ ℚ/ℤ(−1), elements (u₁/u₃, u₂/u₃)_ζ, with
σ(α_ζ) = α_{σζ} and a·α_ζ = α_{ζ^{a⁻¹}}; Prop 2.6 — Br Ũ_n → (Br Ũ_{n,k̄})^Γ surjective, Br Ũ_n/Br k represented by
α_ζ = (−u₁/u₃, −u₂/u₃)_ζ, ζ ∈ μ(k); Cor 2.7 (k = ℚ: ℤ/2, α = α₋₁); Cor 2.9 (Br U_n ≅ Br Ũ_n); Thm 1.6
(Br U_n/Br ℚ ≅ ℤ/2, generated by the quaternion algebra). All quoted correctly; the memo's "Prop 2.5–2.6" attributions
are accurate (Prop 2.5 is over k̄; the descent statement is Prop 2.6).
**Re-derivation.** For π: U_{n,K} → U_n (finite étale base change) and u ∈ U_n(ℚ_ℓ), u_K ∈ U_n(K ⊗ ℚ_ℓ), the
cartesian square gives (cores_π β)(u) = cores_{K⊗ℚ_ℓ/ℚ_ℓ}(β(u_K)); inv_ℓ ∘ cores_{K_w/ℚ_ℓ} = inv_w. Br U_n ≅ Br ℚ ⊕
ℤ/2·α splits because U_n(ℚ) ≠ ∅. If mβ = 0 with m odd then m(β₀ + εα) = 0 forces εα ∈ Br ℚ, so ε = 0 (α is not
constant — it is transcendental and gives T1). ✓. Explicit form: with u rational, σ_a(α_ζ(u)) = α_{ζ^a}(u) =
a⁻¹·α_ζ(u) and inv_{σ_a w}(σ_a x) = inv_w(x) give inv_{σ_a w} α_ζ(u) = a·inv_w α_ζ(u); Σ_{a ∈ (ℤ/m)^×} a = mφ(m)/2 ≡
0 (mod m) for m ≥ 3. ✓
**From scratch** (`scripts/review_ld_cubic.py 600`, 4 s; own ES-solution enumerator and own tame-symbol code): all
50 primes p ≡ 1 (3), 7 ≤ p < 600 have non-constant cubic symbol at w | p (p = 79: 13/12/12 over the 37 sorted
solutions, matching the memo exactly; p = 7: 3/2/2). **Note:** the "sum over w | p is identically 0" is *not*
evidence for Theorem 1 — at a split prime the two embeddings read the same 𝔽_p-element against ω and ω², so the
exponents are k and −k by construction (D3a: say so, or drop it as a "check").
**Remarks.** (a) Scope: Theorem 1 concerns *unramified* classes, β ∈ Br U_{n,K}. Classes ramified along curves of
U_n (Br of an open V ⊂ U_n is much larger, with order-m elements over ℚ) are outside it; the standard reason they do not
obstruct (Harari's formal lemma — ramified classes take all local values at infinitely many places) should be cited
rather than left implicit in "beyond constants, only α" (D3b). (b) Novelty: compatibility of the Brauer–Manin pairing
with corestriction is textbook (CT–S §3.8 as cited; Skorobogatov, *Torsors and rational points*, §5.2); the
memo's "the corestriction remark is ours" is fine as "ours to state for ES", not a new result. (c) Cubic
symbol convention: (a,b)_ζ = −(b,a)_ζ, so for order 3 BL's representations (−u_i/u_k, −u_j/u_k)_ζ can only be
cyclic in (i,j,k) (BL's S₃-invariance remark is for the quaternion class only; the memo does not claim otherwise) —
harmless for non-constancy, but class counts like 13/12/12 depend on the ordering convention (u₁ ≤ u₂ ≤ u₃) (D3c, MINOR).

### Claim 1 — bsD_eichler_degree_k Prop 1 / LDP_DEEP Prop A.3.1 — SOUND-AFTER-REPAIRS (statement as written is false; the parenthetical is right)
For ℓ ∤ q·f-denominators with L_χ unramified at ℓ, inv_ℓ (χ, a) = v_ℓ(a)·[χ(Frob_ℓ)] (Serre, *Local Fields* XIV).
So Σ_{ℓ∤M} inv_ℓ A(χ, f) ↔ χ(|f|) (gcd(f, M) = 1), the multiplicativity statement — fine. But −1 is a unit at
every ℓ ∤ M, so **Σ_{ℓ∤M} inv_ℓ A(χ, −1) = 0 for every χ.** The criterion as written ("Σ_{ℓ∤M} inv_ℓ A(χ, f) equals that
of A(χ, −1)") therefore reads χ(f) = 1 ∀χ, i.e. f ≡ +1, not −1. Counterexample: M = 8, χ = χ₋₄, f = 7 ≡ −1:
Σ_{ℓ∤8} inv_ℓ (χ₋₄, 7) = inv₇ = 1/2 ≠ 0 = Σ_{ℓ∤8} inv_ℓ (−1, −1) (Hamilton's quaternions ramify only at 2, ∞). The
parenthetical "(i.e. 0 for χ even, 1/2 for χ odd)" is the *correct* right-hand side: it is inv_∞ A(χ, −1) = χ(−1)
read additively. Repair: "Σ_{v ∤ M} inv_v A(χ, f) = Σ_{v ∤ M} inv_v A(χ, −1) with v running over primes ℓ ∤ M **and
∞**" (f > 0, so inv_∞ A(χ, f) = 0), or simply "Σ_{ℓ∤M} inv_ℓ A(χ, f) = inv_∞ A(χ, −1)". Same error in LDP_DEEP A.3.1
("equals that of (χ, −1)"). Defect D1 (MINOR: the tautology itself is right and is used only as a tautology).

### Claim 2 — bsD_eichler_degree_k Prop 2 / LDP_DEEP Prop A.3.2 / "degree-2 accident of Br ℝ = ℤ/2" — SOUND for maximal orders; the slogan is SOUND-AFTER-REPAIRS (can be made a precise theorem, stronger than written)
**(i)–(ii) re-derived.** A central simple ℚ-algebra A of degree k has A ⊗ ℝ ≅ M_k(ℝ) or M_{k/2}(ℍ); SL₁(A ⊗ ℝ) is
compact only for ℍ (k = 2): SL_m(ℍ) is non-compact for m ≥ 2. So Eichler's condition (relative to S = {∞}) fails
exactly for definite quaternion algebras. ✓ Under Eichler's condition, strong approximation for SL₁(A) (Kneser/
Swan/Reiner §34–35; I could not access Reiner in `sources/`, theorem numbers unverified) gives: locally free right
Λ-ideal classes ↔ ℚ^×_{>0}\𝔸_f^×/nrd(Λ̂^×) via nrd. For a **maximal** order nrd(Λ_ℓ^×) = ℤ_ℓ^× for all ℓ, so the set is
trivial; maximal orders are everywhere locally conjugate, so the type number ≤ class number = 1. ✓ inv_∞ = 1/2 ⇒
odd number of finite ramified places (Hilbert reciprocity). ✓
**Defects.** (a) "one type and one locally free class" (LDP_DEEP A.3.2) and "'some order in the genus has P' =
'every order has P'" are proved only for **maximal** orders (type number ≤ class number = 1). For general orders Λ
(those that encode level structure — exactly what ES certificates produce) nrd(Λ_ℓ^×) can be a proper subgroup:
e.g. Λ = ℤ + ℓM₂(ℤ), ℓ odd, has det(a + ℓX) ≡ a² (mod ℓ), so nrd(Λ_ℓ^×) = ℤ_ℓ^{×2} (index 2) and its locally free
class number is 2 although A = M₂(ℚ) is indefinite (its type number is still 1, so this is a counterexample to
"one locally free class", not to the type statement; for non-maximal genera the type statement is simply not
proved by the cited argument). The correct precise form of "all local–global
content is congruence data" is: *under Eichler's condition, class sets of any order are ray class groups via nrd,
so any class invariant is a function of finitely many Dirichlet characters.* State that instead (D2a, MINOR — the
conclusion survives, the quantifier statement does not). (b) "Definiteness is *exactly* what makes … the supersingular
class set non-trivial": definiteness is necessary, not sufficient (class number 1 for p = 2, 3, 5, 7, 13); "failure of
strong approximation" ≠ "non-trivial class set" (D2b, MINOR). (c) The slogan "Diff-parity and supersingular geometry
are one phenomenon, 2-torsion because Br ℝ = ℤ/2" is labelled PROVED but (ii)–(iii) only treat inner forms of GL_k and
unitary groups; compact-at-∞ ℚ-groups exist in every rank (definite SO(n), compact Sp(n), compact G₂, F₄, E₆, E₈
forms), so "only degree 2" is not established by the listed cases. **It can be repaired into a precise and stronger
statement** (reviewer's derivation, standard ingredients; please verify against Kottwitz, *Stable trace formula:
elliptic singular terms*, Math. Ann. 275 (1986), §1–2, before labelling PROVED): if a semisimple ℚ-group G is
anisotropic (compact) at ∞, complex conjugation acts on the based root datum of G by the opposition involution
−w₀, hence on Z(Ĝ) by inversion; so Z(Ĝ)^Γ ⊂ Z(Ĝ)^{Γ_∞} ⊂ Z(Ĝ)[2], and the Kottwitz incoherence group
π₀(Z(Ĝ)^Γ)^D (the target of Σ_v of local invariants) is 2-torsion. For G = PGL₁(A) this is "A ⊗ ℝ = ℍ ⇒ k = 2";
for unitary groups it is Landherr's ±1. This is the precise content of "the forcing geometry is 2-torsion because
the archimedean place is" and would cover all compact-at-∞ groups, not just GL_k-inner and unitary ones (D2c, MAJOR as
a label/scope issue: replace "PROVED" on the slogan by the precise statement above or by "Assessment").
(d) (iii) KMRT Thm 3.1 (Albert–Riehm–Scharlau: involution of the second kind ⟺ cores_{E/ℚ}[D] = 0) is correctly
quoted from memory; at split ℓ = w w̄, inv_w + inv_w̄ = 0 and at non-split ℓ inv_w = 0. ✓

### Claim 6 — bsD_frobenius_closure Thm 2 (Chebotarev closure) + cubic dictionary + Kummer EVIDENCE — SOUND (scope wording overreaches in LDP_DEEP A.2; one false strengthening)
**Re-derivation.** Type II: ℓ | N = 1 + 4c²dn ⇒ −dn ≡ (2c)^{−2} (mod ℓ), ℓ ∤ 2cdn ⇒ ℓ splits in K = ℚ(√−dn). Type I:
ℓ | n² + 4c²d, ℓ ∤ n ⇒ (−d/ℓ) = 1. Gal(Kℚ(ζ_M)/ℚ) = Gal(K/ℚ) ×_{Gal(K∩ℚ(ζ_M)/ℚ)} Gal(ℚ(ζ_M)/ℚ), and K ∩ ℚ(ζ_M) ∈
{ℚ, K}; Chebotarev then gives every element of Gal(ℚ(ζ_M)/K ∩ ℚ(ζ_M)) as the restricted Frobenius of infinitely many
ℓ ∈ S_K, and the semigroup they generate in a finite group is a group. ✓. K ⊂ ℚ(ζ_M) ⟺ |disc K| divides M (M ≡ 0
mod 4). Type II at n = p ∤ 4cd: p | disc, so never; at n = m²: K = ℚ(√−d), disc | 4d | M, always (T1). Type I:
ψ_{−d}(−n) = −(−d/n), obstructed ⟺ (−d/n) = +1 (BL level condition). ✓ (b) χ(−1)^k = 1 = χ(−1)² ⇒ χ(−1) = 1 for k odd. ✓
**From scratch** (`scripts/review_ld_frob.py`, 2 min): all 111 pairs (c,d) with cd ≤ 30, n ∈ {primes 5 ≤ p < 400} ∪
{odd squares 9 … 39²} coprime to M, Type I and II: subgroup generated by classes of split primes ℓ < 3000 vs the
predicted index (2 iff disc K | M): **19934 tests, 0 mismatches**; the necessary splitting condition holds for every
prime factor of every N computed; "predicted obstructed but has a divisor hit": **0**.
**Kummer EVIDENCE re-tested independently** (`scripts/review_ld_kummer.py 300000`, 41 s; my own design: all primes
11 ≤ p < 3·10⁵, Type I and II separately, Cochran–Mantel–Haenszel z stratified by (p mod 4cd, p mod 24), Kummer data
"2 a cube", "3 a cube" (p ≡ 1 mod 3), "2 a 4th power" (p ≡ 1 mod 8), slices 4cd ∈ {4, 8, 12, 20, 28, 36}): 56
informative tests, max |z| = 2.17 (Type II (1,7), "2 a cube") — consistent with the null (expected max of 56
independent N(0,1) ≈ 2.4) and with the author's "24 tests, all |z| ≤ 2.2". The memo's own claim is reproduced in
substance, not test-by-test (different stratification).
**Defects.** (a) LDP_DEEP A.2 says "So **the only local–global obstruction** is quadratic". Thm 2 only covers the
mechanism "prime factors lie in a Chebotarev set + multiplicativity"; it says nothing about obstructions using
more of the structure (the value of N, the factorisation pattern f·f′ = N, BM obstructions on certificate varieties).
The memo's own scoped phrasing ("visible from 'prime factors split in K + multiplicativity'") is correct; LDP_DEEP
and AGENT_REPORT should use it (D6a, MINOR). (b) LDP_DEEP A.2: "the cubic part of f ≡ −1 (mod q) is 'π | q is a
cube modulo **every** prime of f'". Cubic reciprocity gives (f/π)₃ = ∏_{ℓ|f}(π/ℓ)₃^{v_ℓ(f)}: the condition is that
the **product** of the symbols is 1, not that each factor is (the memo's "π is a cube modulo the prime factors of f" is
ambiguous; LDP_DEEP's "every" is false — e.g. two prime factors with (π/ℓ₁)₃ = ω, (π/ℓ₂)₃ = ω² give a cube) (D6b,
MINOR). The non-abelian "Kummer splitting" reading applies to the individual factors only.

### Claim 9 — LDP_DEEP B.0 Gram form [[Ma−1, Ma],[Ma, Mce]], det = Mcp — SOUND
By hand: with ⟨x,x⟩ = f = Ma − 1, ⟨x,y⟩ = 1, ⟨y,y⟩ = f′ = Mb − 1, the Gram of (x, x + y) is [[f, f+1],[f+1, f+f′+2]] =
[[Ma−1, Ma],[Ma, M(a+b)]] and a + b = ce because 4abcd − a − b = cp. det is basis-invariant: ff′ − 1 = 4c²dp = Mcp;
mod M it is diag(−1, 0). **From scratch** (`scripts/review_ld_gram.py 3000`, 1 s): all 8085 Type II tuples with
cd ≤ 12 of all odd n < 3000 (primes and composites): e ∈ ℤ, Gram identity, det = Mcn, reduction diag(−1, 0), and the ES
solution 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn): 0 failures.

### Claim 8 — bsD_genus_vacuity_LDp Prop 1 (genus vacuity) / LDP_DEEP B.1; Remark 2 / B.2 (fixed order) — Prop 1 SOUND (conditional on DIFF_DEEP Thm 1.1, under R176); Remark 2 SOUND as corrected, but its "O(1)" is mis-normalised (MINOR)
**Re-derivation of Diff(T) = {p}.** B_T = (−f, −det T) = (−f, −dp) up to squares (det = 4c²dp). ∞: both negative,
ramified. ℓ | f odd: −dp ≡ (2c)^{−2} is a square mod ℓ ⇒ split. ℓ | cd odd: −f ≡ 1 (mod ℓ) ⇒ split. ℓ = 2: −f ≡ 1
(mod 4); if 8 | M then −f ≡ 1 (mod 8) is a 2-adic square; if M = 4·odd then −dp is a 2-adic unit and (u, w)₂ = 1 for
u ≡ 1 (4). So only p can ramify among finite places, and Hilbert reciprocity forces it. ✓ (KUDLA_ES Thm 1.4.)
**From scratch** (`scripts/review_ld_gram.py`, own Hilbert symbols incl. ℓ = 2, with a reciprocity self-check on
every algebra): every prime n < 3000 and every Type II tuple with cd ≤ 12: Diff(T) = {n}, 0 failures. (For composite
odd n the Diff set is a single prime divisor of n, varying with the tuple — printed for information.)
**The vacuity argument.** If B_T ≅ B_{p,∞}, embed x, y; ℤ + ℤx + ℤy + ℤxy is an order (xy + yx = −2⟨x,y⟩ ∈ ℤ),
contained in a maximal order O, so T is a Gram matrix in O⁰. The same argument ℓ-adically shows every local density
is positive. So "∃ O" adds nothing to "∃ integer T". ✓ The labels are right: PROVED relative to DIFF_DEEP Thm 1.1 —
note that this is itself only "CLAIMED, under review R176" per LDP_DEEP's header; the C-verdict "PROVED: … B.1"
should carry that dependency (D8a, MINOR).
**Remark 2 / B.2 (Assessment).** The correction of the first draft is right: Duke–Schulze-Pillot is about
representations of *integers* by ternary forms (Invent. Math. 99 (1990), from memory — not in `sources/`); representing
a *binary* form by a ternary one is a different (codimension-2, n − m = 1) problem with no local–global principle in
general. But the replacement heuristic "a given T is represented O(1) times on average by a fixed O⁰" ignores the
p-dependence: by Siegel's formula for (n, m) = (3, 2) the det(T)-exponent is (n − m − 1)/2 = 0, and the genus total
Σ_O r(O⁰, T)/|O^×| is the Gross–Keating/Kudla–Rapoport–Yang degree of the 0-cycle Z(T), a divisor-type function
ρ(T) = p^{o(1)} (reviewer's recollection; please verify before relying on it). Spread over ≈ p/12 orders, a *fixed*
O⁰ represents a given T about 12ρ(T)/p times on average, not O(1). This makes the fixed-order lottery much sparser per
T (consistent with O176 §2.5 only because the number of certificate-shaped T with f′ ≤ 4p grows); the
"O(1) expected hits per T" in LDP_DEEP B.2 should read "O(ρ(T)) over the genus, O(ρ(T)/p) per fixed order" (D8b, MINOR;
Assessment-level text).

### Claim 10 — spot checks of the other memos and of the global framing
* **bsD_metaplectic_cubic** — GAP in labels. Props 1–2 are tagged "PROVED (from the explicit formula / from cubic
  reciprocity)" while the Literature section says "All from memory; page-level details unverified". Prop 1's logic is
  right (for fixed rational V, ε_ℓ, Legendre symbols of fixed unit parts and Hilbert symbols are quadratic characters
  of ℓ by quadratic reciprocity), but it rests on the unverified form of Rao's formula ⇒ CONDITIONAL. Prop 2's
  barrier bullet "n-fold covers (n ≥ 3) have no dual-pair theta correspondence with orthogonal groups" is a
  literature claim stated as fact; there are theta-type constructions for higher covers via exceptional
  representations (Kazhdan–Patterson; Bump–Friedberg–Ginzburg) — the weaker, defensible statement is "no Siegel–Weil
  identity that ingests a quadratic Gram matrix is known" (D10a, MINOR).
* **bsD_drinfeld_rank_k** — SOUND as Assessment. Gekeler's description (End ⊗ K = central division algebra of
  dimension r² with invariants 1/r at 𝔭, −1/r at ∞, End a maximal order) is quoted correctly as far as I can check
  from memory. The "unique setting" claim is robust for number fields for the reason the memo implies but does not
  state: S always contains ∞, and for degree ≥ 3 SL₁(A ⊗ ℝ) is non-compact, so strong approximation holds for every
  S-arithmetic variant too.
* **bsD_artin_conjugation** — SOUND-AFTER-REPAIRS. Dictionary ✓ (f ≡ −1 ⟺ σ_f|_{K⁺} = 1, σ_f ≠ 1). But "the order-≥3
  content R … is precisely 'σ_f trivial on K⁺'" is imprecise: (ℤ/M)^×/{±1} still carries the *even* quadratic
  characters (for M | 24 it is (ℤ/2)², entirely quadratic). The K⁺-part is "everything χ(−1) = +1 sees", not "the
  order-≥3 part" (D10b, MINOR). The superseding correction (η_{K/F} has conductor 𝔪·∞₁⋯∞_r) is right and is the
  basis of A.4.
* **LDP_DEEP framing.** The one-paragraph answer says "(a) No, over ℚ and over every number field, for three
  independent structural reasons, each PROVED with exact scope". The three pieces are proved within their scopes,
  but the "No" is an Assessment: A.1 is about unramified classes on U_n, A.2 about the Chebotarev-closure mechanism,
  A.3 about inner forms of GL_k (+ unitary), and the A.4 door is closed only for norm-descent (D4c). §C already says
  "Assessment" — the intro and AGENT_REPORT SHARP list should match (D10c, MINOR). A.6 (iii) depends on bsC Prop 1
  and bsC Cor 2 (O176, under R176) — state the dependency.

### Inherited reliance on R176 defects (orchestrator request)
* **R176 D1 (vacuous "level G ≥ 2√h" gloss).** LDP_DEEP's *question* (b) quoted the gloss ("level ≥ 2√(covolume/p)").
  The analysis itself does not rely on it: bsD_genus_vacuity_LDp and LDP_DEEP B.1 use the exact condition
  4h | gcd(h, G)² (DIFF_DEEP Thm 2.1). B.3's target "det ≤ pM²/4" is a *necessary* consequence of the exact
  condition, so "Minkowski misses it" stands a fortiori. Repaired by a pointer in the question (D11a, MINOR).
* **R176 D2 (bsC Prop 1 slogan "parity over any base is quadratic" false for F-rational data).** O177 is consistent
  with — indeed independently found — this: LDP_DEEP A.4 and bsD_artin_conjugation's correction state that bsC
  Prop 1 does not apply to F-rational data, and A.6 (iii) is scoped to "ℚ-rational data". Residual reliance: the
  LDP_DEEP title/question phrase "parity sees only quadratic characters" (harmless as the *object* of the question),
  bsD_metaplectic Prop 1 ("extends verbatim", with V rational — fine), bsD_eichler (iii) ("bsC Prop 1 applies" to
  Landherr's ±1 — fine, the invariants are signs). A.6 (iii) now cites bsC Prop 1 "as literally stated" (D11b).
* **R176 D4 (non-existent "ET f(p) ≪ p^{o(1)}").** Not used anywhere in O177 (grep: no occurrence).
* DIFF_DEEP Thm 1.1 (basis of B.1) was judged SOUND by R176, so B.1's dependency is discharged (D8a updated).

## Defects (numbered; FATAL / MAJOR / MINOR) with locations and repairs

None FATAL.

**MAJOR**
* **D2c** (bsD_eichler_degree_k Prop 2 last sentence + Assessment; LDP_DEEP A.3.2 bold sentence and A.6 (iv);
  AGENT_REPORT SHARP 1). "Diff-parity and supersingular geometry are a degree-2 accident of Br ℝ = ℤ/2" is tagged
  PROVED but only inner forms of GL_k and unitary groups are treated; compact-at-∞ ℚ-groups exist in every rank.
  *Repair:* label the slogan Assessment, or replace it by the precise statement in Claim 2(c) (G semisimple,
  anisotropic at ∞ ⇒ complex conjugation acts on Z(Ĝ) by inversion ⇒ Kottwitz's incoherence group is 2-torsion),
  after checking it against Kottwitz 1986.
* **D4c** (LDP_DEEP A.4.2 "(where it breaks; PROVED)" and "Closed."; §C "PROVED: … A.4.1–A.4.2"; AGENT_REPORT
  SHARP 3 "It closes because …"). Only the identity N(−1) = (−1)^r = +1 (r even) is proved; that no descent
  mechanism exists is an Assessment. *Repair:* "PROVED: N_{F/ℚ}(−1) = +1 for every ES modulus M = 4cd > 4, so norm
  descent of an O_F-certificate loses the target. Assessment: no other descent is known (open: trace forms /
  restriction of scalars, odd-degree subfields F′ — Spark 1)."

**MINOR**
* **D1** (bsD_eichler_degree_k Prop 1; LDP_DEEP A.3.1). Σ_{ℓ∤M} inv_ℓ A(χ, −1) = 0 for every χ, so "equals that of
  A(χ, −1)" characterises f ≡ +1. *Repair:* include ∞ in the sum, or write "= inv_∞ A(χ, −1) (0 for χ even, 1/2 for
  χ odd)".
* **D2a** (Prop 2(i); A.3.2 "one type and one locally free class"). True for maximal orders; false for the
  locally-free class set of general orders (ℤ + ℓM₂(ℤ): class number 2). *Repair:* say "maximal orders", and state the
  general fact as "class sets are ray class groups via nrd ⇒ congruence data".
* **D2b** (Prop 2(ii); A.3.2). "Definiteness is exactly what makes … the class set non-trivial": necessary, not
  sufficient (p = 2, 3, 5, 7, 13). *Repair:* "necessary".
* **D3a** (bsD_brauer_cores numerics). "the sum over w | p is identically 0" is automatic (the two embeddings read
  the same 𝔽_p element against ω, ω²); not evidence. *Repair:* drop or flag as a sanity identity.
* **D3b** (bsD_brauer_cores Thm 1 scope sentence). Applies to unramified classes on U_{n,K}; ramified classes on
  opens are excluded and should be dismissed by Harari's formal lemma explicitly.
* **D3c** (bsD_brauer_cores numerics). Cubic class counts depend on the ordering convention (u₁ ≤ u₂ ≤ u₃) since
  (a,b)_ζ = −(b,a)_ζ. *Repair:* state the convention.
* **D4a** (LDP_DEEP A.4 "Construction attempt"). "ramified at the real places where T_F is definite" + "det T_F
  totally positive" makes the count r for every β. *Repair:* "positive definite"; note the parity identity
  #ram_∞ = r − #neg ≡ #neg uses r even.
* **D4b** (LDP_DEEP A.4 normalisation; AGENT_REPORT SHARP 3). β ≡ 1 (𝔪) in the construction vs β ≡ −1 (4cd O_F) in
  A.4.2; "f = N_{F/ℚ}(β)" must be the ideal norm |N(β)| (the element norm is ≡ +1 always).
* **D5** (LDP_DEEP A.4 EVIDENCE; Spark 4). 53.6% of all certificates have f or f′ prime, and a prime f ≡ −1 is
  automatically an F-norm; the "F-norm" statistic is ≈ "a prime side exists". *Repair:* add this sentence; with the
  exact F-norm criterion (residue degrees) the exception list is the same 5 primes.
* **D6a** (LDP_DEEP A.2 "So the only local–global obstruction is quadratic"). Thm 2 covers only the Chebotarev-closure
  mechanism. *Repair:* use the memo's scoped phrase.
* **D6b** (LDP_DEEP A.2 last sentence). "π is a cube modulo every prime of f" is false; the condition is
  ∏_{ℓ|f}(π/ℓ)₃^{v_ℓ(f)} = 1. *Repair:* "the product of the cubic symbols (π/ℓ)₃ over ℓ | f is 1".
* **D8a** (LDP_DEEP §C "PROVED: … B.1"). Add "relative to DIFF_DEEP Thm 1.1 (O176, under R176)".
* **D8b** (LDP_DEEP B.2; bsD_genus_vacuity Remark 2). "O(1) expected hits per T" at a fixed order ignores the
  ≈ p/12 orders sharing a genus total ρ(T) = p^{o(1)}. *Repair:* "O(ρ(T)) over the genus, O(ρ(T)/p) per fixed order
  (heuristic)".
* **D9** (bsD_missed_primes layer table). Broken markdown ("cd | 6" inside cells). *Repair:* write "cd ∣ 6" or
  "cd divides 6".
* **D10a** (bsD_metaplectic_cubic Props 1–2). PROVED from unverified, memory-based formulas ⇒ CONDITIONAL; soften
  "no dual-pair theta correspondence for n ≥ 3 covers".
* **D10b** (bsD_artin_conjugation). K⁺-part ≠ "order-≥3 part" (it contains the even quadratic characters).
* **D11** (LDP_DEEP question (b); A.6 (iii)). (a) Quoted the R176-D1 vacuous size gloss; (b) cite bsC Prop 1 "as
  literally stated" (R176 D2). Both repaired.
* **D10c** (LDP_DEEP one-paragraph answer; AGENT_REPORT verdict). "(a) No … each PROVED" — the "No" is an
  Assessment; match §C. State the dependency of A.6 (iii) on bsC Prop 1 / Cor 2 (O176, under R176).

## Scripts (all from scratch, ≤ 2 min each, ulimit -v 8 GB)
`review_ld_split.py` (claim 5), `review_ld_missed.py` (claim 7), `review_ld_ray.py` (claim 4),
`review_ld_cubic.py` (claim 3), `review_ld_frob.py`, `review_ld_kummer.py` (claim 6), `review_ld_gram.py` (claims 8–9).
