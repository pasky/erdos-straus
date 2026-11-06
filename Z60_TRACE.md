# Z60_TRACE — (★) as the split points of a Hecke trace formula on Γ(4C): an exact identity, and why it gives no positivity

**ES is OPEN; (MS) is open. Nothing here proves or disproves either.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Brief: `z52bbriefs/z60_lanes.md` § TRACE with
`z58_lanes.md` (common rules, falsifier table) and `z53_depth.md`. Scripts `scripts/z60_trace_*`, data `data/z60/trace/`
(< 1 MB). Literature check: `data/z60/trace/LIT_CHECK.md` (research subagent; confidence levels there).

**Verdict: narrowed.** No HOT LEAD. Delivered: an exact identity (Theorem 2) in which, for each C, the (★)-solutions at C are
literally the positive split classes of a Hecke operator on S_k(Γ(4C)), the elliptic side is a Hurwitz class-number sum along
the same line, and the class +1 divisors (TRIV) are the negative split classes. Positivity analysis (§4): every spectral
upper bound fires only if it is sharp to within (number of cusps)/2 × (ES mass) (Prop 4.2, PROVED); with Deligne this needs
near-total eigenvalue alignment at every level except Γ(4), k = 3 (Cor 4.3, PROVED); where the elliptic side is empty
(C ≳ n^{1/3}) the Hecke trace *is* the divisor count and is not square-root small (Prop 4.4, PROVED); bounded C is a fixed
menu (Prop 4.5, CONDITIONAL on Schinzel H). Screens §5.

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
* Not in the repo: a trace formula whose elliptic side and whose (★)-solutions are two kinds of points of **one** object. That is
  Theorem 2. In the literature, the closest objects are class-number sums in progressions with congruence-conditioned
  min-divisor terms (Mertens, Adv. Math. 301 (2016) Prop 7.2; Kane–Pujahari, TAMS 376 (2023) Lemma 3.3; Kane–Pujahari–Yang,
  Math. Ann. (2025) Thm 1.7, Cor 1.8 — verified, LIT_CHECK §4). Those are weight-2 (even), level-1 class numbers H(4N − t²)
  with t in a progression; Theorem 2 has descended class numbers H(4s − w²), Γ(4C)-structure, and all weights k.

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
(iii) Γ is elliptic ⟺ w² < 4s; a repeated eigenvalue ⟺ w² = 4s, impossible for odd n; split ⟺ w² − 4s is a positive square.
(iv) At a split point the eigenvalues u, B of γ are integers with 4CuB − u − B = n and either u, B ≥ 1 (an (★)-solution at C,
    i.e. the ES pair (Qu − 1, QB − 1)) or u, B ≤ 0 (with u = −u′, B = −B′: (Qu′ + 1)(QB′ + 1) = N, a TRIV pair; u′ = 0 is (1, N)).
    Mixed signs are impossible. Each ordered ES/TRIV pair arises from exactly one ordered root pair.
(v) (T1 on the line.) For an odd square n = m², L_{C,m²} has no split point with u, B ≥ 1, for every C.
(vi) For fixed (s, w) with w² < 4s, the SL₂(ℤ)-classes of γ ∈ M₂(ℤ) with char. poly. x² − wx + s, each weighted by
    1/|Z_{PSL₂(ℤ)}(γ)|, have total weight H(4s − w²).
*Proof.* (i) Qγ − I ≡ −I (Q); conversely γ := (Γ + I)/Q ∈ M₂(ℤ); det(Qγ − I) = Q² det γ − Q tr γ + 1 = Q(4C det γ − tr γ) + 1;
conjugation commutes with γ ↦ Qγ − I. (ii) (Qw − 2)² − 4(Qn + 1) = Q²w² − 4Q(w + n) = Q²w² − 4Q·4Cs. (iii) from (ii); w = 2r,
s = r² gives n = 4Cr² − 2r, even. (iv) w² − 4s ≡ w² (mod 4), so a square discriminant gives integer roots u, B with
4CuB − (u + B) = 4Cs − w = n, i.e. (Qu − 1)(QB − 1) = N. If B ≤ 0 < u then Qu − 1 > 0 > QB − 1 and the product would be
negative (symmetrically for u ≤ 0 < B). (v) T1 (R(m²) = 0, FRONTIER §2 / Z57_SYNTH Lemma A.1(b)) applied to (iv). (vi) Classical: such
classes ↔ classes of primitive forms of discriminant (w² − 4s)/f² over f² | w² − 4s with the usual ±-weighting, which is
the definition of H. ∎ (Checked: `scripts/z60_trace_lemma1_check.py`, C ≤ 6, odd n < 1200, 0 mismatches.)

**Lemma 2 (class counting; PROVED).** Let Q ≥ 3. Γ(Q) is torsion-free and −I ∉ Γ(Q) (Diamond–Shurman §3.8). Δ_C(N) is
Γ(Q)-bi-invariant and SL₂(ℤ)-conjugation invariant (Γ(Q) ⊲ SL₂(ℤ)). If ξ ∈ Δ_C(N) is elliptic, its SL₂(ℤ)-class is the union
of exactly 2μ_C/|Z_{SL₂(ℤ)}(ξ)| = μ_C/|Z_{PSL₂(ℤ)}(ξ)| Γ(Q)-classes, each with trivial centraliser in Γ(Q). Hence the
Γ(Q)-classes of elliptic elements of Δ_C(N), each counted once, number μ_C·Σ_{(s,w) ∈ L_{C,n}, w²<4s} H(4s − w²).
*Proof.* [SL₂(ℤ) : Γ(Q)] = 2μ_C; Γ(Q) normal ⇒ the SL₂(ℤ)-class of ξ splits into [SL₂(ℤ) : Γ(Q)Z(ξ)] = 2μ_C/|Z(ξ)| classes
(Z(ξ) ∩ Γ(Q) = 1 since Z(ξ) is finite and Γ(Q) torsion-free without −I). Sum with Lemma 1(vi); ±ξ are distinct and only ξ ∈ Δ
(−ξ ≡ +I). ∎

## 3. Theorem 2 — the Γ(4C) trace identity

Let T_Δ := Σ_{α ∈ Γ(Q)\Δ_C(N)} (·)|_k α on S_k(Γ(Q)) (normalisation: on S_k(Γ₀(M), χ) it is the usual T_N with eigenvalues =
Fourier coefficients). Conjugation by diag(1, Q) identifies S_k(Γ(Q)) ≅ ⊕_{χ mod Q, χ(−1) = (−1)^k} S_k(Γ₀(Q²), χ)
(Q² = 16C²) and Δ_C(N) with −{[[a, b],[c, d]] : det N, Q² | c, a ≡ d ≡ 1 (Q)}; since −I acts by (−1)^k,
**Tr(T_Δ | S_k(Γ(Q))) = (−1)^k Σ_{χ mod Q, χ(−1)=(−1)^k} Tr(T_N | S_k(Γ₀(Q²), χ))** (PROVED, standard; this is how the spectral
side is computed).

**Theorem 2.** For C ≥ 1, k ≥ 2, n ≥ 1, N = 4Cn + 1, Q = 4C:
`Tr(T_Δ | S_k(Γ(Q))) = −μ_C·E_{C,k}(n) − (ε∞/2)·(ES_k(C,n) + (−1)^k TRIV_k(C,n)) + (k−1)μ_C/12·Σ_{λ² = N, λ ≡ −1 (Q)} λ^{k−2} + δ_{k,2}·σ(N)`,
with the **line class-number sum** `E_{C,k}(n) := Σ_{s ≥ 1, w := 4Cs − n, w² < 4s} P_k(Qw − 2, N)·H(4s − w²)`.

**Status: CERTIFIED (exact rational equality) + derivation PROVED relative to a general trace formula up to the bookkeeping of
the hyperbolic constant.**
* CERTIFIED: exact equality for (C, k, n ≤ n_max) = (1, 2, 150), (1, 3, 60), (1, 4, 150), (1, 5, 150), (2, 2, 80), (2, 3, 1500),
  (2, 4, 60), (3, 3, 600), (4, 3, 40), (5, 3, 30), plus (2, 3, 3000) and (1, 3, 20 000) in the screens — every n (odd and even),
  0 mismatches; spectral side from pari `mftraceform` summed over characters (`scripts/z60_trace_identity.py`,
  `z60_trace_check.py`, `z60_trace_screen.py`; data `data/z60/trace/id_*.json`, `screen_*.tsv`). For C = 1 the k = 2 and k = 3
  cases are re-checked **without any modular-forms package** to n = 50 000 (Cor 2.1; `scripts/z60_trace_c1_check.py`).
* Derivation. Shimura, Acta Math. 132 (1974) Thm 4.5, and Popa, PAMS 146 (2018) Thm 1 (any finite-index Γ ⊂ SL₂(ℤ), any
  double coset; verified, LIT_CHECK §1) express the trace as a sum over Γ-classes in Δ of local terms: scalar (∝ vol), elliptic
  (−p_{k−2}(tr, det)/|Stab|), hyperbolic with cuspidal fixed points, and the k = 2 degree term #Γ\Δ. For Γ = Γ(Q): (a) the
  elliptic local term is the level-1 one, so Lemma 2 gives exactly −μ_C·E_{C,k}(n); (b) the scalar term is (k−1)/12·vol-ratio
  μ_C·λ^{k−2} for λI ∈ Δ; (c) the k = 2 term is #Γ(Q)\Δ = #SL₂(ℤ)\M_N = σ(N) since (N, Q) = 1; (d) SL₂(ℤ) permutes the ε∞ cusps
  transitively and preserves Δ, so the cusp-fixed hyperbolic term is ε∞ times its value at ∞, which involves exactly the
  upper-triangular elements [[d, x],[0, d']] ∈ Δ, i.e. the ordered pairs dd' = N with d ≡ d' ≡ −1 (Q) **of either sign**:
  positive = ES pairs, negative = −(TRIV pairs) (Lemma 1(iv)), the latter with the factor (−1)^k from homogeneity of
  |·|^{k−1}sign^k. The per-pair constant −½·min(|d|, |d'|)^{k−1} is the level-1 value (Zagier/Cohen form) — the reader may
  take the constant −ε∞/2 as certified rather than derived (we did not re-derive Shimura's garbled J(C) constants).
  Assessment: the identity is solid (four independent checks of each term's shape + exact agreement everywhere tested), but
  a line-by-line derivation of (d) from the source has not been written.

**Corollary 2.1 (C = 1; PROVED from Thm 2 + dim S₂(Γ(4)) = 0, dim S₃(Γ(4)) = 1; CERTIFIED independently to n ≤ 50 000).**
(k = 2) `24·Σ_{s: w=4s−n, w²<4s} H(4s − w²) + 3·(ES₂ + TRIV₂)(1, n) = σ(4n + 1) + 2·[4n + 1 = □]`.
(k = 3) `ES₃(1, n) − TRIV₃(1, n) = −8·Σ_{s: w=4s−n, w²<4s} (4w − 2)·H(4s − w²) + (a(4n + 1) + 4λ)/3`,
where a(m) are the coefficients of η(4z)⁶ = q − 6q⁵ + 9q⁹ + 10q¹³ − 30q¹⁷ + … ∈ S₃(Γ₀(16), χ₋₄) (the CM form of ℚ(i):
a(m) = ½ Σ_{x odd, y even, x² + y² = m} (x² − y²)), and λ = ±√N ≡ −1 (4) if N is a square, else 0.
In particular, **if 4n + 1 is not a sum of two squares, ES₃(1, n) = TRIV₃(1, n) − 8E_{1,3}(n) exactly** — a class-number formula
for the ES-weighted count at C = 1. (The k = 2 relation is presumably equivalent to a known progression relation, e.g.
KPY Thm 1.7 with M = 16 via H(16D) ↔ H(D); no novelty claimed for it as a class-number identity.)
*Check:* n = 1: N = 5, ES = 0, TRIV₂ = TRIV₃ = 2, E = 0: 6 = σ(5); 0 − 2 = (−6)/3. ✓

**Remark 2.2 (reading).** For each C, (★) at C = the positive split points of the line L_{C,n} in the (det, tr)-plane; class +1 =
its negative split points; the elliptic points carry H(4s − w²). In the Γ(4C) trace formula the three kinds are the
hyperbolic(+), hyperbolic(−) and elliptic classes of one Hecke set. The sign separating ES from TRIV is the sign of the
eigenvalues, i.e. (−1)^k: **odd weight separates them; even weight adds them** — the robust content of GROWING_IDENTITIES
Prop 2.1, now in a form where the separating datum is visibly "−I ∉ Γ(4C) acts by (−1)^k". (Remark, Assessment.) A
generating-function reading: Σ_n E_{C,2}(n)q^{4Cn+1} should be the holomorphic part of the specialisation of Zagier's weight-2
index-1 class-number Jacobi–Eisenstein series at z = −τ after τ ↦ 4Cτ (Eichler–Zagier Thms 1.3, 2.1; LIT_CHECK §3), whose
non-holomorphic part sits exactly on the split points; not worked out (Assessment).
