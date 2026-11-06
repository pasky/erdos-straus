# Z60_TRACE — (★) as the positive divisor-pair terms of a Hecke trace formula on Γ(4C): an identity, and what positivity it does not give

**ES is OPEN; (MS) is open. Nothing here proves or disproves either.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Brief: `z52bbriefs/z60_lanes.md` § TRACE with
`z58_lanes.md` (common rules, falsifier table) and `z53_depth.md`. Scripts `scripts/z60_trace_*`, data `data/z60/trace/`
(≈ 1.3 MB). Literature check: `data/z60/trace/LIT_CHECK.md` (research subagent; confidence levels there). Hostile internal
review: `data/z60/trace/REVIEW_internal.md` (12 defects, all addressed, §9).

**Verdict: narrowed.** No HOT LEAD; no positivity mechanism obtained. Delivered: an identity (Theorem 2) on the Hecke set
Δ_C(N) = {det N, ≡ −I mod 4C} of Γ(4C) in which, for each C, the (★)-solutions at C are the positive divisor-pair terms of the
cusp (hyperbolic) contribution, the class +1 divisors (TRIV) the negative ones, and the elliptic side is a Hurwitz class-number
sum along the line 4Cs − w = n on which the (★)-solutions are the positive split points. Status of Theorem 2: CERTIFIED by
direct spectral computation on a sparse finite list of (C, k, n); for general (C, k, n) CONDITIONAL on one local counting lemma
(Lemma 3, CERTIFIED on 21 044 cases), relative to Cohen–Strömberg's Eichler–Selberg formula. Positivity (§4, all CONDITIONAL
on Thm 2): odd weight gives ES_k exactly as explicit − (8C/μ)·Tr (Prop 4.1); an upper-bound certificate for the trace fires
iff it is sharp to within (number of cusps)/2 × (ES mass) (Prop 4.2, a rearrangement); the worst-case Deligne bound fires only
if the average normalised eigenvalue exceeds 1 − 6/((k−1)Q − 6) (≥ 0.4; → 1 as (k−1)Q → ∞; only at Γ(4), k = 3 is there no ρ-free constraint)
(Cor 4.3); in the empty-elliptic-window regime the trace equals −(ε∞/2)(ES − TRIV) + S, and an explicit family shows that a
level-uniform square-root bound for the trace is false (Prop 4.4). Screens §5.

Notation. R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; R_C(n) its C-slice. Q := 4C, N = N_C(n) := 4Cn + 1.
(★)-solutions at C ↔ ordered divisor pairs dd' = N with d ≡ d' ≡ −1 (mod Q), d = Qu − 1, d' = QB − 1 ("ES pairs", class −1).
"TRIV pairs" (class +1): dd' = N, d ≡ d' ≡ 1 (mod Q); always including (1, N) and (N, 1).
ES_k(C, n) := Σ_{ES pairs} min(d, d')^{k−1}, TRIV_k(C, n) := Σ_{TRIV pairs} min(d, d')^{k−1} (ordered pairs; d = d' counted once).
So R_C(n) = #ES pairs, and ES_k(C, n) > 0 ⟺ R_C(n) ≥ 1. μ_C := [PSL₂(ℤ) : Γ̄(Q)] = (Q³/2)∏_{ℓ|Q}(1 − ℓ⁻²);
ε∞ := μ_C/Q = number of cusps of Γ(Q) (Diamond–Shurman §3.8; LIT_CHECK §6). P_k(t, N) := (ρ^{k−1} − ρ̄^{k−1})/(ρ − ρ̄) with
ρ + ρ̄ = t, ρρ̄ = N (P₂ = 1, P₃ = t, P₄ = t² − N; = Popa's Gegenbauer p_{k−2}(t, N)). H = Hurwitz class number (H(3) = 1/3,
H(4) = 1/2).

## 0. Prior art in the repository (git grep "Eichler", "Kuznetsov", "Hurwitz", "class number relation")

* GROWING_IDENTITIES (O170) §2, DISCOVERIES (J)10: Cohen's Eichler–Selberg formula on Γ₀(q), χ, q = 4C (or 4cd), N ≡ 1 (q):
  ES class −1 enters the split-hyperbolic term only together with class +1, relative sign (−1)^k (Prop 2.1, PROVED rel.
  Cohen); Deligne would need ≍ kq-fold cancellation (Prop 2.2, *Assessment*); KH re-summation over C fails (§3, Assessment).
  **Elliptic side there: the generic Σ_t over all traces with twisted root counts — not tied to the (★) geometry.**
* y1_gamma8_trace (O209): Type I sign is a Γ(8)-class function; three-letter extraction is non-spectral. bsC_eichler_orientation,
  z9_brandt_screen, QUATERNION_ES: Brandt / Eichler-order dictionaries collapse to B2. Z53_HYPKLOOST: Kuznetsov /
  Kloosterman-fraction implementations give no saving (scoped).
* What the repo already has (credit): GROWING_IDENTITIES Prop 2.1 has the ±1 split-divisor term, the parity sign (−1)^k, the
  min-divisor weight and the odd-weight explanation; Prop 2.2 has the level/weight-versus-Deligne scale obstruction (as an
  Assessment); y1_gamma8_trace has class-function visibility versus arithmetic extraction. **New to the repository here (narrow):**
  the principal-level specialisation (Hecke set Δ_C(N) on Γ(4C)) whose elliptic side is the explicit *descended* class-number
  sum along the affine line 4Cs − w = n, on which the (★)-solutions are the positive split points (Lemma 1); the precise
  necessary inequality for Deligne certificates (Cor 4.3); the empty-window analysis and explicit family (Prop 4.4).
* Literature: class-number sums in progressions with congruence-conditioned min-divisor terms exist, **including higher
  weights / moments**: Mertens, Adv. Math. 301 (2016) §7.2, Prop 7.2 (weight 2 + 2ν); Kane–Pujahari, TAMS 376 (2023) Lemma 3.3
  (weight 2 + 2k, any modulus); Kane–Pujahari–Yang, Math. Ann. (2025) Thm 1.7 (weight 2), Thm 1.6 (higher moments incl. odd),
  Cor 1.8 (cusp form vanishes only for M ≤ 5 or (m, M) ∈ {(2,8), (6,8)}) — verified, LIT_CHECK §4. These use level-1 class
  numbers H(4N − t²) with t in a progression; Theorem 2 uses H(4s − w²) = H((4N − t²)/Q²) with Γ(Q)-structure. No literature
  novelty is claimed; a term-by-term comparison with these papers has not been made.

## 1. Precise statements attacked

**(TR-id)** For fixed C ≥ 1 and weight k ≥ 2: an exact identity "elliptic class-number term + hyperbolic term built from
ES_k, TRIV_k + scalar term = Tr(T | S_k(Γ_C))", valid for every n ≥ 1.
**(TR-pos)** Can any spectral input (Deligne, Cauchy–Schwarz / second moments, Sato–Tate-type equidistribution, square-root
cancellation) applied to (TR-id) force ES_k(C, p) > 0 for some C at every large prime p (or p ∈ 𝔐)? If not, prove the
obstruction as a scoped theorem and name the escape.

Why not already closed: GROWING_IDENTITIES Prop 2.2's "kq-fold cancellation" is an Assessment at level Γ₀(q); there was no
identification of the elliptic side with the (★) geometry, no large-C analysis, and no theorem on certificate firing.

## 2. The line dictionary

**Lemma 1 (PROVED, elementary).** Fix C, n ≥ 1, N = 4Cn + 1. Put M_C(n) := {γ ∈ M₂(ℤ) : 4C·det γ − tr γ = n} and
Δ_C(N) := {Γ ∈ M₂(ℤ) : det Γ = N, Γ ≡ −I (mod Q)}.
(i) γ ↦ Γ = Qγ − I is a bijection M_C(n) → Δ_C(N), equivariant for GL₂(ℤ)-conjugation.
(ii) With s := det γ, w := tr γ, the point (s, w) lies on the **line** L_{C,n}: 4Cs − w = n; tr Γ = Qw − 2;
    (tr Γ)² − 4 det Γ = Q²(w² − 4s).
(iii) Γ is elliptic ⟺ w² < 4s; a repeated eigenvalue ⟺ w² = 4s (possible only for even n; includes scalar Γ, e.g.
    C = 1, n = 2, Γ = 3I); split (distinct rational eigenvalues) ⟺ w² − 4s is a positive square.
(iv) At a split or repeated-root point the eigenvalues u, B of γ are integers with 4CuB − u − B = n and either u, B ≥ 1 (an (★)-solution at C,
    i.e. the ES pair (Qu − 1, QB − 1)) or u, B ≤ 0 (with u = −u′, B = −B′: (Qu′ + 1)(QB′ + 1) = N, a TRIV pair; u′ = 0 is (1, N)).
    Mixed signs are impossible. Each ordered ES/TRIV pair arises from exactly one ordered root pair. (This is a dictionary of
    *root pairs*, not of conjugacy classes: e.g. C = 1, n = 5, roots {1, 2} give two ordered ES pairs (3, 7), (7, 3) but one
    SL₂(ℤ)-class, which splits into 24 Γ(4)-classes; in Theorem 2 the ES pairs enter as weighted terms of the cusp contribution.)
(v) (T1 on the line.) For an odd square n = m², L_{C,m²} has no split point with u, B ≥ 1, for every C.
(vi) For fixed (s, w) with w² < 4s, the SL₂(ℤ)-classes of γ ∈ M₂(ℤ) with char. poly. x² − wx + s, each weighted by
    1/|Z_{PSL₂(ℤ)}(γ)|, have total weight **2H(4s − w²)** (two orientations: γ and its "conjugate" correspond to positive and
    negative definite forms; e.g. J = [[0, −1],[1, 0]] and −J are not SL₂(ℤ)-conjugate, total weight 1 = 2H(4)). [Corrected after
    internal review D1; the first version said H.]
*Proof.* (i) Qγ − I ≡ −I (Q); conversely γ := (Γ + I)/Q ∈ M₂(ℤ); det(Qγ − I) = Q² det γ − Q tr γ + 1 = Q(4C det γ − tr γ) + 1;
conjugation commutes with γ ↦ Qγ − I. (ii) (Qw − 2)² − 4(Qn + 1) = Q²w² − 4Q(w + n) = Q²w² − 4Q·4Cs. (iii) from (ii); w = 2r,
s = r² gives n = 4Cr² − 2r, even. (iv) w² − 4s ≡ w² (mod 4), so a square discriminant gives integer roots u, B with
4CuB − (u + B) = 4Cs − w = n, i.e. (Qu − 1)(QB − 1) = N. If B ≤ 0 < u then Qu − 1 > 0 > QB − 1 and the product would be
negative (symmetrically for u ≤ 0 < B). (v) T1 (R(m²) = 0, FRONTIER §2 / Z57_SYNTH Lemma A.1(b)) applied to (iv). (vi) Classical: such
classes ↔ classes of primitive forms of discriminant (w² − 4s)/f² over f² | w² − 4s, positive *and* negative definite, with
weight 1/|Aut⁺/±|; the positive definite ones alone give H. ∎ (`scripts/z60_trace_lemma1_check.py` checks (iv)–(v) only — the
divisor dictionary and T1 — for C ≤ 6, odd n < 1200, 0 mismatches; it does not check (vi).)

**Lemma 2 (class counting; PROVED).** Let Q ≥ 3. Γ(Q) is torsion-free and −I ∉ Γ(Q) (Diamond–Shurman §3.8). Δ_C(N) is
Γ(Q)-bi-invariant and SL₂(ℤ)-conjugation invariant (Γ(Q) ⊲ SL₂(ℤ)). If ξ ∈ Δ_C(N) is elliptic, its SL₂(ℤ)-class is the union
of exactly 2μ_C/|Z_{SL₂(ℤ)}(ξ)| = μ_C/|Z_{PSL₂(ℤ)}(ξ)| Γ(Q)-classes, each with trivial centraliser in Γ(Q). Hence the
Γ(Q)-classes of elliptic elements of Δ_C(N) with given (s, w), each counted once, number 2μ_C·H(4s − w²) (corrected, D1).
*Proof.* [SL₂(ℤ) : Γ(Q)] = 2μ_C; Γ(Q) normal ⇒ the SL₂(ℤ)-class of ξ splits into [SL₂(ℤ) : Γ(Q)Z(ξ)] = 2μ_C/|Z(ξ)| classes
(Z(ξ) ∩ Γ(Q) = 1 since Z(ξ) is finite and Γ(Q) torsion-free without −I). Sum with Lemma 1(vi); ±ξ are distinct and only ξ ∈ Δ
(−ξ ≡ +I). ∎

## 3. Theorem 2 — the Γ(4C) trace identity

Let T_Δ f := Σ_{α ∈ Γ(Q)\Δ_C(N)} f[α]_k on S_k(Γ(Q)), with f[α]_k(z) := (det α)^{k−1}(cz + d)^{−k}f(αz) (Diamond–Shurman §5.1
convention; on S_k(Γ₀(M), χ) this gives the usual T_N, eigenvalues = Fourier coefficients). Δ_C(N) is a finite union of
Γ(Q)-double cosets; T_Δ is the sum of the corresponding double-coset operators. Conjugation by diag(1, Q) identifies S_k(Γ(Q)) ≅ ⊕_{χ mod Q, χ(−1) = (−1)^k} S_k(Γ₀(Q²), χ)
(Q² = 16C²) and Δ_C(N) with −{[[a, b],[c, d]] : det N, Q² | c, a ≡ d ≡ 1 (Q)}; since −I acts by (−1)^k,
**Tr(T_Δ | S_k(Γ(Q))) = (−1)^k Σ_{χ mod Q, χ(−1)=(−1)^k} Tr(T_N | S_k(Γ₀(Q²), χ))** (PROVED, standard; this is how the spectral
side is computed).

**Theorem 2.** For C ≥ 1, k ≥ 2, n ≥ 1, N = 4Cn + 1, Q = 4C:
`Tr(T_Δ | S_k(Γ(Q))) = −μ_C·E_{C,k}(n) − (ε∞/2)·(ES_k(C,n) + (−1)^k TRIV_k(C,n)) + (k−1)μ_C/12·Σ_{λ² = N, λ ≡ −1 (Q)} λ^{k−2} + δ_{k,2}·σ(N)`,
with the **line class-number sum** `E_{C,k}(n) := Σ_{s ≥ 1, w := 4Cs − n, w² < 4s} P_k(Qw − 2, N)·H(4s − w²)`.

**Status.** (A) CERTIFIED (exact rational equality, finite): the sparse list (C, k, n ≤ n_max) = (1, 2, 150), (1, 3, 60),
(1, 4, 150), (1, 5, 150), (2, 2, 80), (2, 3, 1500), (2, 4, 60), (3, 3, 600), (4, 3, 40), (5, 3, 30), plus (2, 3, 3000) and
(1, 3, 20 000) in the screens, plus the reviewer's fresh runs (3, 5, 40) and (7, 3, 2) — every n (odd and even), 0 mismatches.
(B) For general (C, k, n): **CONDITIONAL on Lemma 3 below, relative to Cohen–Strömberg Thm 12.4.11** (Eichler–Selberg for
S_k(Γ₀(M), χ), k ≥ 2; theorem number and A₁ − A₂ − A₃ + A₄ shape confirmed only via two citing papers, LIT_CHECK §2; the
transcription used is GROWING_IDENTITIES §2, checked there by R170).
* Data for (A): spectral side from pari `mftraceform` summed over characters (`scripts/z60_trace_identity.py`,
  `z60_trace_check.py`, `z60_trace_screen.py`; data `data/z60/trace/id_*.json`, `screen_*.tsv`). For C = 1 the k = 2 and k = 3
  cases are re-checked **without any modular-forms package** to n = 50 000 (Cor 2.1; `scripts/z60_trace_c1_check.py`).
* Derivation of (B) (rewritten after internal review D1/D2; the hyperbolic computation is the reviewer's). Apply Cohen–Strömberg
  to each S_k(Γ₀(Q²), χ), χ mod Q, and sum with weight (−1)^k over χ(−1) = (−1)^k, using
  Σ_{χ(−1)=(−1)^k} (−1)^kχ(x) = (φ(Q)/2)([x ≡ −1 (Q)] + (−1)^k[x ≡ 1 (Q)]) and the two identities
  ψ(Q²)·φ(Q)/2 = μ_C, (φ(Q)/2)·Σ_{t|Q²} φ(gcd(t, Q²/t)) = (φ(Q)/2)·Q∏_{ℓ|Q}(1 + 1/ℓ) = ε∞.
  (a) Identity term A₁ = (k−1)/12·ψ(Q²)χ(√N)N^{k/2−1}: the sum gives (k−1)μ_C/12·Σ_{λ=±√N, λ≡−1 (Q)} λ^{k−2}. PROVED rel. C–S.
  (b) Hyperbolic term A₃: for an ES/TRIV pair all cusp divisors t | Q² are admissible (h = gcd(t, Q²/t) | Q | d − d′ and
  h | Q²/f_χ), and the CRT parameter y_t ≡ ±1 (Q) exactly when d, d′ ≡ ±1 (Q); orthogonality gives
  −(ε∞/2)(ES_k + (−1)^k TRIV_k) (diagonal pairs d = d′ under C–S's convention). Pairs with d ≢ ±1 (mod Q) cancel in the
  character sum. PROVED rel. C–S (computation in REVIEW_internal.md, "A concrete repair").
  (c) k = 2 term A₄ (trivial χ only) = σ(N). PROVED rel. C–S. (Also = #Γ(Q)\Δ = #SL₂(ℤ)\M_N, the degree.)
  (d) Elliptic term A₂: the same orthogonality and t ↦ −t, x ↦ −x (P_k(−t) = (−1)^kP_k(t)) give
  −(φ(Q)/2)·Σ_{t²<4N} P_k(t, N)·W(t), with W(t) := Σ_f h_w((t²−4N)/f²)·(ψ(Q²)/ψ(Q²/M_f))·#{x mod Q² : x² − tx + N ≡ 0
  (mod Q²M_f), x ≡ −1 (Q)}, M_f = gcd(Q², f). **Lemma 3 (local lemma; CERTIFIED, not proved):** W(t) = ψ(Q²)·H((4N − t²)/Q²) if
  t ≡ −2 − Qn (mod Q²), and W(t) = 0 otherwise. Checked exactly for Q ∈ {4, 8, 12, 16, 20}, n ≤ 60, all |t| < 2√N: 21 044
  cases, 0 mismatches (`scripts/z60_trace_locallemma.py`). Partial proof: with x = −1 + Qy, x² − tx + N ≡ (t + 2 + Qn) −
  Qy(t + 2) (mod Q²), so a root with x ≡ −1 (Q) exists mod Q² iff t ≡ −2 − Qn (mod Q²), and then all Q lifts are roots mod Q²;
  the f-sum identity (an embedding-number count for orders containing (Γ + I)/Q) is not written. Given Lemma 3, t = Qw − 2 with
  w ≡ −n (Q), (4N − t²)/Q² = 4s − w², and the elliptic term is −μ_C·E_{C,k}(n).
  Cross-check with Lemma 2: Popa, PAMS 146 (2018) Thm 1 (trace on M_k + S_k^c, elliptic weight −p_{k−2}/|Stab|; LIT_CHECK §1)
  has elliptic total −Σ_{Γ(Q)-classes} P_k = −2μ_C·E_{C,k}(n) by Lemma 2; passing to S_k (Remark 3.2 symmetry, Eisenstein trace
  without elliptic part, halving) gives −μ_C·E — consistent, but this route is a sketch.

**Corollary 2.1 (C = 1; CONDITIONAL on Thm 2(B) [i.e. on Lemma 3 at Q = 4] + dim S₂(Γ(4)) = 0, dim S₃(Γ(4)) = 1; CERTIFIED
to n ≤ 50 000 without modular-forms computations — it still uses pari's Hurwitz class numbers).**
(k = 2) `24·Σ_{s: w=4s−n, w²<4s} H(4s − w²) + 3·(ES₂ + TRIV₂)(1, n) = σ(4n + 1) + 2·[4n + 1 = □]`.
(k = 3) `ES₃(1, n) − TRIV₃(1, n) = −8·Σ_{s: w=4s−n, w²<4s} (4w − 2)·H(4s − w²) + (a(4n + 1) + 4λ)/3`,
where a(m) are the coefficients of η(4z)⁶ = q − 6q⁵ + 9q⁹ + 10q¹³ − 30q¹⁷ + … ∈ S₃(Γ₀(16), χ₋₄) (the CM form of ℚ(i):
a(m) = ½ Σ_{x odd, y even, x² + y² = m} (x² − y²)), and λ = ±√N ≡ −1 (4) if N is a square, else 0.
In particular, **if 4n + 1 is not a sum of two squares, ES₃(1, n) = TRIV₃(1, n) − 8E_{1,3}(n) exactly** — a class-number formula
for the ES-weighted count at C = 1. (The k = 2 relation is presumably equivalent to a known progression relation, e.g.
KPY Thm 1.7 with M = 16 via H(16D) ↔ H(D); no novelty claimed for it as a class-number identity.)
*Check:* n = 1: N = 5, ES = 0, TRIV₂ = TRIV₃ = 2, E = 0: 6 = σ(5); 0 − 2 = (−6)/3. ✓

**Remark 2.2 (reading).** For each C, (★) at C = the positive split (or repeated-root) points of the line L_{C,n} in the
(det, tr)-plane; class +1 = its negative ones; the elliptic points carry H(4s − w²). In the Γ(4C) trace formula they give the
positive divisor-pair terms, negative divisor-pair terms and elliptic terms of one Hecke set (weighted terms, not literal
class counts; Lemma 1(iv)). The sign separating ES from TRIV is the sign of the
eigenvalues, i.e. (−1)^k: **odd weight separates them; even weight adds them** — the robust content of GROWING_IDENTITIES
Prop 2.1, now in a form where the separating datum is visibly "−I ∉ Γ(4C) acts by (−1)^k". (Remark, Assessment.) A
generating-function reading (Assessment, not worked out): with F(τ, z) = Σ H(4s − w²)q^sζ^w (Zagier's weight-2 index-1
class-number series, up to the −12 normalisation and its non-holomorphic completion), the series Σ_n E_{C,2}(n)q^{Qn+1} should be
the holomorphic part of q·F(Q²τ, −Qτ) (torsion-point specialisation, Eichler–Zagier Thm 1.3), with the completion living on
the split and repeated-root points; the weight-2 completion and the boundary D = 0 terms were not computed (corrected after D8).

## 4. Positivity: what Theorem 2 does and does not give

Throughout k ≥ 3 is odd (k = 2 and even k: Prop 4.1), dim := dim S_k(Γ(Q)) = (k−1)μ_C/12 − ε∞/2 (Γ(Q), Q ≥ 3, torsion-free
with regular cusps; Diamond–Shurman Thms 3.5.1, 3.6.1, LIT_CHECK §6; matches pari: dim = 1, 5, 20, 72, 208, 408 for
(C, k) = (1,3), (1,5), (2,3), (3,3), (4,3), (5,3)). Write Tr := Tr(T_Δ | S_k(Γ(Q))), S := the scalar term, and
`X := TRIV_k − 2Q·E_{C,k}(n) + (2Q/μ_C)·S`.

All of §4 is CONDITIONAL on Theorem 2(B) (i.e. on Lemma 3), and unconditional wherever Theorem 2 is CERTIFIED.

**Prop 4.1 (exact solution for ES; parity; PROVED from Thm 2).** For odd k: **ES_k(C, n) = X − (2Q/μ_C)·Tr.** For even k:
ES_k = −TRIV_k − 2Q·E_{C,k} + (2Q/μ_C)(S + δ_{k,2}σ(N) − Tr). Since TRIV_k ≥ 2 always (pairs (1, N), (N, 1)), odd k gives the
factorisation-free X ≥ X₀ := 2 − 2Q·E_{C,k}(n) + (2Q/μ_C)S; even k would need an *upper* bound for TRIV_k, a class +1
divisor-in-class count of the same type as ES (Assessment: as hard). So odd weight is the natural carrier; the two classes are
separated by (−1)^k = the action of −I ∉ Γ(Q) (Remark 2.2). *Proof.* Rearrange Thm 2 with ε∞/2 = μ_C/(2Q). ∎

**Prop 4.2 (slack principle; PROVED from Thm 2 — a rearrangement, not an impossibility theorem).** Let k be odd and let B be any number with Tr ≤ B (an "upper-bound certificate":
Deligne, Cauchy–Schwarz with a second moment, a hypothetical equidistribution bound, …). Then ES_k(C, n) ≥ X − (2Q/μ_C)B, and
this lower bound is positive ("the certificate fires") **iff B − Tr < (ε∞/2)·ES_k(C, n).** In particular every certificate
fires only where R_C(n) ≥ 1 (so it is automatically consistent with F1/F4), and only when it is sharp to within
(number of cusps)/2 × (ES mass). *Proof.* By Prop 4.1, X − (2Q/μ_C)B = ES_k − (2Q/μ_C)(B − Tr). ∎ It says nothing about
whether some (yet unknown) bound B with small slack exists.
The same tautology holds for any identity "ES-term = explicit − c·(spectral sum)": Selberg-type versions with a test function
g localising the hyperbolic terms by log(d/d′) and spectral side Σ_j h(r_j)λ_j(N) (weight-1 Maass forms carry the odd
parity), or harmonic-weighted (Petersson) versions — the certificate must be sharp to within the weighted ES mass.

**Cor 4.3 (necessary condition for the worst-case Deligne certificate; PROVED from Thm 2).** Since N ≡ 1 (mod Q) and (N, Q) = 1, T_Δ = −⊕_χ T_N
(k odd) is diagonalisable on S_k(Γ(Q)) with real eigenvalues −λ_f(N) (λ̄ = χ̄(N)λ = λ), |λ_f(N)| ≤ τ(N)N^{(k−1)/2} (Deligne,
newform theory). Put ν_f := −λ_f(N)/(τ(N)N^{(k−1)/2}) ∈ [−1, 1], D := dim·τ(N)N^{(k−1)/2} ≥ Tr and
ρ := ES_k/(τ(N)N^{(k−1)/2}) < 1 (at most τ(N) − 2 ordered ES pairs, each of weight ≤ N^{(k−1)/2}). If the Deligne certificate
B = D fires at (C, k, n), then
`(1/dim)·Σ_f ν_f > 1 − ρ·6/((k−1)Q − 6)` (> 1 − 6/((k−1)Q − 6)).
So for every (k, Q) ≠ (3, 4) firing forces the average normalised eigenvalue above 1 − 6/((k−1)Q − 6) (≥ 0.4 at (3, 8), (5, 4);
→ 1 as (k−1)Q → ∞). Only in that limit does this become "near-total alignment" (all but a vanishing fraction of the
normalised eigenvalues ν_f within o(1) of +1); at a fixed small level it is only the displayed average condition. The
statement concerns B = D only; sharper pointwise bounds are not covered. Only at Γ(4), k = 3 (dim 1 < ε∞/2 = 3) is the ρ-free threshold vacuous (the sharper ρ-dependent necessary condition
1 − 3ρ < ν still applies) — and there the space is the CM line of η(4z)⁶,
so the identity is Cor 2.1 and decides only C = 1. *Proof.* Firing ⟺ D − Tr < (ε∞/2)ES_k ⟺ Σ_f(1 − ν_f) < (ε∞/2)ρ;
divide by dim and use (ε∞/2)/dim = (μ_C/2Q)/((k−1)μ_C/12 − μ_C/2Q) = 6/((k−1)Q − 6). ∎
EVIDENCE (`data/z60/trace/screen_C*_k3*.tsv`; slack ratio r := (D − Tr)/((ε∞/2)ES_k), firing ⟺ r < 1):
| (C, k), range | n with R_C(n) ≥ 1 | fires | min r (at n) | median r | range of Tr/D |
|---|---|---|---|---|---|
| (1, 3), n ≤ 20 000 | 12 229 | 137 | 0.68 (12 655) | 26.0 | — |
| (2, 3), n ≤ 3000 | 990 | 0 | 3.82 (701) | 96.2 | [−0.77, 0.76] |
| (3, 3), n ≤ 600 | 109 | 0 | 6.76 (491) | 66.2 | [−0.52, 0.50] |
(Table re-derived row by row by the internal reviewer.) Heuristic (Assessment): if Tr fluctuated like a sum of dim independent
bounded terms (sd ≍ √dim·N^{(k−1)/2}), the needed event Tr > D − (ε∞/2)ES would be a deviation of order dim ≫ √dim, i.e. rare;
the finite data agree (no firing at C = 2, 3). This is not a theorem about all certificates; an input that knows the *actual*
size of Tr is not excluded — Prop 4.4 shows what that size is in one regime.

**Prop 4.4 (large-C regime: the trace *is* the divisor count; PROVED).** If n ≤ 4C³ − 2C (⟺ 4C² − 1 ≥ √N), the line L_{C,n}
has at most one elliptic point, namely (s_*, w_*) with w_* the representative of −n (mod Q) in (−2C, 2C] and
s_* = (n + w_*)/Q (elliptic iff w_*² < 4s_*; the endpoint w_* = 2C, i.e. n ≡ 2C (mod 4C), is never elliptic by the bound
|w| < 2C below — corrected after D9). Hence for odd k
`(ε∞/2)·(ES_k − TRIV_k)(C, n) = −Tr − μ_C·[w_*² < 4s_*]·P_k(Qw_* − 2, N)·H(4s_* − w_*²) + S.`
*Proof.* Two elliptic points w₁ < w₂ (≡ −n mod Q) need Q ≤ w₂ − w₁ < 4σ, σ := √s_max with s_max = (n + w₂)/(4C); from
w₂ < 2σ: 4Cσ² − 2σ − n < 0, so σ < (1 + √N)/(4C), whence 4C² < 1 + √N. Any elliptic w has |w| < 2σ < (1 + √N)/(2C) ≤ 2C. ∎
Consequences (PROVED from Thm 2 in this form): (a) in this regime, R_C(n) ≥ 1 ⟺ Tr ≠ (ε∞/2)TRIV_k − μ_C·(one class-number
term) + S — the spectral side *detects* (★) at C as a deviation from an explicit value but carries no sign information.
(b) When moreover the window is empty (w_*² ≥ 4s_*; for n ≪ C³ this holds for most residues w_*), Tr − S = −(ε∞/2)(ES_k − TRIV_k)
exactly: there Theorem 2 is a restatement of the divisor count. This does **not** make Tr large at every such n (e.g. n = 1,
Q ≥ 8: ES = 0, TRIV = 2, Tr = ε∞, which is *below* the square-root scale). (c) **Explicit family (corrected after D3; the
family is the reviewer's):** for Q = 4C ≥ 8 and n = 2Q − 3 one has N = (Q − 1)(2Q − 1), the unique candidate (w_*, s_*) = (3, 2) is
not elliptic, S = 0 (gcd(Q − 1, 2Q − 1) = 1, so if N were a square both factors would be squares; but Q − 1 ≡ 3 (4) is not), the only ES divisor ≤ √N is Q − 1, no nontrivial TRIV
divisor ≤ √N exists (Q + 1 would have to divide 6), hence ES_k = 2(Q − 1)^{k−1}, TRIV_k = 2 and
**Tr = −ε∞·((Q − 1)^{k−1} − 1).** CERTIFIED at C = 2 (n = 13: Tr = −1152) and C = 3 (n = 21: Tr = −5760). Since ε∞/(2√dim) ≍
√(Q/(k−1)) and τ(N) = Q^{o(1)}, for fixed k the ratio |Tr|/(√dim·τ(N)N^{(k−1)/2}) grows like Q^{1/2−o(1)}: a square-root
bound |Tr| ≪ √dim·τ(N)N^{(k−1)/2} uniform over all levels Γ(4C) and all n is **false** (conditional on Thm 2; the explicit
values above are certified). This family has n ≡ 5 (mod 8), outside the Mordell-hard domain, so it does not refute such a bound
restricted to primes in 𝔐.

**Remark 4.5 (bounded C; Assessment + CERTIFIED finite examples).** Any argument that uses Theorem 2 only for C ≤ C₀ proves at
most "R_C(p) ≥ 1 for some C ≤ C₀". This fails at every (★)-zero prime (all C), e.g. the 14 primes of `star_prime_zeros.txt`;
whether it fails infinitely often is expected (fixed-menu heuristics, FRONTIER §3) but **no precise theorem is claimed or cited
here** — finite examples establish no infinitude.

**Remark 4.6 (other trace formulas; Assessment).**
* *Positivity in trace formulas* comes from Σ_f |λ_f(N)|²-type sums = Tr(T T*), whose geometric side lives at N² and its
  divisors-squared, not at N; its only use here is as the B of Prop 4.2 (Cauchy–Schwarz B = √(dim·Σλ²)); it fires iff the gap
  √(dim·Σλ_f²) − Σ(−λ_f) is < (ε∞/2)ES, which heuristically means nearly constant eigenvalues; no quantitative statement is
  proved for this B.
* *Kuznetsov / Bruhat cells.* (PROVED, trivial; bijection checked by the reviewer) R(n) = Σ_C #{γ ∈ Γ∞⁺γ_QΓ∞⁺ : b(γ) = n, a(γ), d(γ) > 0} with
  γ_Q = [[Q−1, Q−2],[Q, Q−1]]: (★) at C is a *single* Bruhat cell of modulus c = Q (residues a ≡ d ≡ −1) with the upper-right
  entry fixed. Ordinary Kloosterman sums weight cells by e((ma + nd)/c) and forget the chosen lifts, i.e. the exact
  factorisation ad = Qn + 1 is an archimedean condition (consistent with Z53_HYPKLOOST); this does not exclude trace formulas
  with an archimedean test function.
* *Level-p formulas (Brandt, Γ₀(p))*: z9_brandt_screen and bsC_eichler_orientation already show collapse to B2.

## 5. MANDATORY FALSIFIER TABLE (final)

Theorem 2 is an identity valid for every n; the screens bite on positivity arguments drawn from it.
| Screen | Behaviour (labels) | Consequence |
|---|---|---|
| F1 odd squares | Identity holds with ES_k(C, m²) = 0 for all C (Lemma 1(v), PROVED). Then Tr = −μE + (ε∞/2)TRIV_k + S exactly. CERTIFIED: identity holds with ES = 0 at all screened squares — 49 odd squares 3²…99² (C = 2, list), and the odd squares in the ranges (71 for C = 1, n ≤ 20 000; 27 for C = 2, n ≤ 3000; 12 for C = 3, n ≤ 600); no certificate fires there (Prop 4.2 forbids it). EVIDENCE/Assessment: Tr/D at squares shows no visible separation from primes (C = 2, n ≤ 3000: max 0.33 over odd squares (n = 225), 0.40 over all squares (n = 1296), 0.76 over primes; the 49-odd-square list reaches 0.66 at n = 81²) — a comparison of maxima, not a statistical test. | No step of the identity uses non-squareness; the square-sensitivity of a positivity argument would have to come from an *external* input on Tr or E (none supplied here). |
| F2 C-even (R₈) | The identity is per C; R₈ = Σ_{C even} R_C. Nothing in Theorem 2 or §4 distinguishes C odd from C even (Q = 4C either way). | A positivity argument built on this identity that **transports verbatim to the C-even sub-line** (same steps, restricted to even C) and claims a range containing the 12 + 2 R₈-zero primes (∈ [10¹⁰, 2.33·10¹⁰]) would prove a false statement. Those zeros lie below the (MS) threshold 10¹⁷ and refute only such ranges (FRONTIER §4 item 2), not eventual C-even positivity; they are zeros of one line of 8/p, not failures of 8/p. Nothing in Theorem 2 itself distinguishes C odd from C even. |
| F3 composites | Identity holds for all n; primality is never used (Theorem 2 is uniform in n). The 285 certified non-square composite zeros n ≡ 1 (4) ≤ 7 999 801 (`data/z58/screens/composite_zeros_le8e6.txt`; independently re-enumerated by the cross-model review: no hits) have ES_k(C, n) = 0 for every C, so the identity holds there with no ES term at any level. | A positivity argument would need a primality input beyond the identity (primality is absent from the identity, not necessarily from future estimates). |
| F4 known zeros | **14 global (★)-zero primes** (`star_prime_zeros.txt`, re-confirmed by the cross-review): ES_k(C, p) = 0 for **all** C. At 409, 577, 5569, 9601 (C = 2, k = 3) the identity holds, ES = 0, certificate does not fire (`screen_C2_k3.tsv`; e.g. p = 9601: Tr/D = 0.068). **38 𝔊*-zeros** (`gstar_zeros.txt`): these are zeros of the restricted 𝔊* family only; 24 of them have global (★) hits (cross-review, e.g. 37 = 4·1·2·5 − 1 − 2), so the all-C vanishing does **not** extend to them; they obstruct only arguments confined to the 𝔊* subfamily. | Any spectral lower bound for (★) must fail at the 14 global zeros for every level 4C (or have a threshold above 8 813 281). |
Verdict on the screens: the identity is consistent with all four (it is true; "passes" means consistency, not survival of a
positivity argument); **no positivity mechanism supplied here establishes
the needed square-, parity- or primality-sensitive discrimination** (a negative finding, not a theorem excluding future
arguments that use this identity).

## 6. FRONTIER §4 hard screens for the best idea (the odd-weight Γ(4C) identity + an upper-bound certificate)
1. T1 squares: fails to supply the needed step (identity is square-blind; the certificate cannot fire at squares by Prop 4.2,
   but nothing makes it fire at primes). 2. 8/131 (numerator 8): numerator-blind — the C-even sub-line has the identical
   identity (F2; with the threshold caveat there). 3. Tied modulus: the level *is* the tied modulus 4C, encoded exactly — an
   encoding success, not a pass of the substantive B2 screen (no lower bound for the tied event is produced). 4. Fixed p: the
   identity holds at a single n, but no single-N control of its spectral side is supplied here (Cor 4.3 covers only the
   Deligne bound; Prop 4.4 only the empty-window regime and one uniform bound).

## 7. Verdict

**Narrowed** (no positivity mechanism obtained). (1) Lemma 1 (PROVED): (★) at C = positive split/repeated-root points of the
line 4Cs − w = n in M₂(ℤ), ↔ Hecke set Δ_C(N) = {det N, ≡ −I (4C)} of Γ(4C). Theorem 2 (CERTIFIED on a sparse finite list;
in general CONDITIONAL on the local Lemma 3 relative to Cohen–Strömberg): elliptic side −μ_C × the Hurwitz class-number sum
along the line, hyperbolic side −(ε∞/2)(ES_k + (−1)^k TRIV_k). (2) Odd weight separates ES from TRIV (−I acts by (−1)^k):
ES_k = X − (2Q/μ)Tr exactly (Prop 4.1). (3) Positivity: an upper-bound certificate fires iff its slack is < (ε∞/2)·ES
(Prop 4.2, rearrangement); the worst-case Deligne bound needs average normalised eigenvalue > 1 − 6/((k−1)Q − 6) (Cor 4.3);
in the empty-window regime the trace equals −(ε∞/2)(ES − TRIV) + S and a level-uniform square-root bound for it is false
(explicit family, Prop 4.4(c)). For the worst-case Deligne bound we have only the necessary alignment condition of Cor 4.3
and finite non-firing evidence (C = 2, 3); universal non-firing beyond Γ(4) is **not** established (corrected after the
cross-model review).
Open escapes: single-N bounds for the trace sharper than Deligne with slack ≪ (ε∞/2)·ES (none known; not excluded),
one-sided estimates or restrictions to the Mordell-hard prime domain (Prop 4.4(c) does not cover it), removal of explicit
geometric contributions, other C-ranges, and identities whose spectral side carries an independent positivity (none found).

## 8. Proposed FRONTIER §7 text (do not edit FRONTIER here)
*Trace formulas (z60 TRACE).* For each C, the (★)-solutions at C are the positive divisor-pair terms of the cusp contribution
of the Hecke set {det N, ≡ −I mod 4C} on Γ(4C) (N = 4Cn + 1), and the positive split points of the line 4Cs − w = n. The Γ(4C)
Eichler–Selberg identity (Z60_TRACE Thm 2: CERTIFIED on the sparse list (C, k) ∈ {(1,2..5), (2,2..4), (3,3), (3,5), (4,3),
(5,3), (7,3)} with stated n-ranges; general case CONDITIONAL on a local lemma, relative to Cohen–Strömberg) has elliptic side
−μ_C·Σ_{4Cs−w=n, w²<4s} P_k·H(4s − w²) and hyperbolic side −(ε∞/2)(ES_k + (−1)^k TRIV_k). Odd weight gives ES_k exactly up to a
Hecke trace. Conditional on the identity: an upper-bound certificate fires iff its slack is < (ε∞/2)·ES; the Deligne bound needs
average normalised eigenvalue > 1 − 6/((k−1)Q − 6); a level-uniform square-root bound for the trace is false (explicit family,
n ≡ 5 mod 8). Open: single-N control of the trace with slack ≪ (ε∞/2)·ES; a proof of the local lemma.

**Bottom line.** A clean trace formula carrying (★) is certified exactly on every tested case, and in general holds
conditionally on one unproved local counting lemma (Lemma 3): at each level 4C the (★)-solutions, the class +1 divisors and a Hurwitz class-number sum along one
line are the positive-pair, negative-pair and elliptic terms of a single Hecke trace on Γ(4C), separated by odd weight. We
found no pointwise lower bound from the spectral side: a certificate must be accurate to within the (★)-mass itself, the
Deligne bound would need strong eigenvalue alignment, and where the class-number side disappears the Hecke trace is just the
divisor count. No discriminating (square-, parity- or primality-sensitive) positivity input was supplied; the spectrum and E do
depend on the input n, but we found no way to exploit that. No lead.

## 9. Review log
Hostile internal review (deep-mode reviewer, `data/z60/trace/REVIEW_internal.md`): 12 defects (1 FATAL-to-a-proof, 6 MAJOR,
5 MINOR); the identity itself survived, including fresh spectral runs (C, k) = (3, 5), (7, 3) and a full re-derivation of all
2 320 JSON and 23 702 TSV rows. Fixes applied: D1 (orientation factor 2 in Lemma 1(vi)/Lemma 2; the identity's coefficient is
unchanged because Popa's trace is on M_k + S_k^c) — fixed; D2 (derivation) — rewritten via Cohen–Strömberg with the reviewer's
hyperbolic computation; elliptic part reduced to Lemma 3 (new script, CERTIFIED, not proved); Theorem 2 relabelled CERTIFIED +
CONDITIONAL; D3 — Prop 4.4(b) restated, reviewer's explicit family added as 4.4(c) (checked against our data); D4 — verdict and
Cor 4.3 narrowed; Cauchy–Schwarz remark relabelled; D5 — F2 transport/threshold qualifications restored; D6 — "classes" →
weighted divisor-pair terms, repeated roots; D7 — higher-weight literature credited, novelty narrowed; D8 — Jacobi rescaling
corrected, EZ Thm 2.1 citation dropped; D9 — half-open interval; D10 — 66.2, square maxima; D11 — scripts exit nonzero, exact
integer elliptic enumeration (re-run: identical rows); D12 — size, Prop 4.5 → Remark (no infinitude claim), sparse list in
FRONTIER text. Not re-reviewed after the fixes (but see the cross-model review below). LIT_CHECK.md minor convention issues (D12 bullets 4–6) are recorded in the
review and not edited in LIT_CHECK.

### Cross-model review
`data/z60/xreview/REVIEW_TRACE.md` (verdict ACCEPT-WITH-FIXES; independent audit script `scripts/z60_xrev_trace_check.py`:
2 320 + 202 fresh spectral rows and 23 600 TSV rows reconstructed, Lemma 3 re-run on 21 044 cases, explicit family checked for
C = 2…500, no mismatch). Fixes applied: (1) §7 universal-sounding "does not give (★) beyond Γ(4)" replaced by the necessary
alignment condition + finite non-firing evidence; bottom line now says "no discriminating positivity input supplied" instead of
"the identity is insensitive"; (2) F4 completed with the 38 𝔊*-zeros (24 have global (★) hits, so no all-C vanishing there) and
F3 now names the 285 certified composite zeros; "passes" in §5 means consistency only; (3) Prop 4.4(c): gcd(Q−1, 2Q−1) = 1 step
added; Cor 4.3 / header: Γ(4), k = 3 exception qualified as absence of a ρ-free constraint; bottom line made conditional on
Lemma 3; (4) LIT_CHECK convention errors corrected (projective index in Popa's dimension sentence; k ≥ 3 for the Γ(N) dimension
quotation; KPY divisor conventions d | n vs 2d | 4n). Primary-source limits stand: Cohen–Strömberg, Eichler–Zagier and Serre were
checked only via secondary sources; the EZ weight-2 completion (Remark 2.2) remains an unworked Assessment.
