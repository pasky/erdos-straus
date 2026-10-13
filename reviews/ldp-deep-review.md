# R177 — hostile review of O177 (LDP_DEEP.md + BRAINSTORM/bsD_*.md)

Reviewer branch `side-agent/review-ldp-deep` (merged `side-agent/spark-higher-reciprocity`). From-scratch scripts:
`scripts/review_ld_*.py`. Labels as in DISCOVERIES.md. **ES is not solved anywhere; nothing below changes that.**

## Summary verdicts (filled in claim by claim)

| # | Claim | Verdict |
|---|---|---|
| 1 | bsD_eichler_degree_k Prop 1 / LDP_DEEP Prop A.3.1 | (pending) |
| 2 | bsD_eichler_degree_k Prop 2 / LDP_DEEP Prop A.3.2 + "degree-2 accident" slogan | (pending) |
| 3 | bsD_brauer_cores Thm 1 / LDP_DEEP Thm A.1 | (pending) |
| 4 | LDP_DEEP Prop A.4.1, A.4.2, F-Gram construction | (pending) |
| 5 | EVIDENCE: split-supported Type II certificates, cd ≤ 30 | (pending) |
| 6 | bsD_frobenius_closure Thm 2 (+ cubic dictionary) | (pending) |
| 7 | bsD_missed_primes numbers (71; layers 2/12/0) | (pending) |
| 8 | bsD_genus_vacuity_LDp Prop 1, Remark 2 / LDP_DEEP B.1–B.2 | (pending) |
| 9 | LDP_DEEP B.0 Gram form | (pending) |
| 10 | spot checks: bsD_metaplectic_cubic, bsD_drinfeld_rank_k, bsD_artin_conjugation | (pending) |

## Detailed findings

## Defects

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
**Defects.** (a) "'Some order in the genus has P' = 'every order has P'" is true for the genus of **maximal** (or
Eichler) orders only. For general orders Λ (those that encode level structure — exactly what ES certificates
produce) nrd(Λ_ℓ^×) can be a proper subgroup: e.g. Λ = ℤ + ℓM₂(ℤ) has nrd(Λ_ℓ^×) = ℤ_ℓ^{×2}(1 + ℓℤ_ℓ), index 2,
so its locally free class number is 2 although A = M₂(ℚ) is indefinite. The correct precise form of "all local–global
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
