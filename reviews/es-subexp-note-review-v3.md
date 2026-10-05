# Referee report R47 — `paper/es-subexp-note.tex` v3 (exponent 1/5)

Referee: hostile side agent R47 (branch `side-agent/referee-subexp-v3`).
Author branch: `side-agent/subexp-paper-v3` @ 67cda1e (merged non-ff into referee branch; ff-only failed because main moved).

Status: COMPLETE (round 1).

**Recommendation: minor revision.** I found no FATAL defect and no gap in the chain to
Theorem 1.1 (exponent 1/5 with the (log log p)^{−1/5} factor) or Theorem 1.2. Every proof in
§§2–8 was re-derived line by line; C-1 (Thm 6.5), its corollary, and the filtration form
(Thm 6.9) were brute-forced from scratch on random non-uniform product spaces and never
exceed 1 (max 0.9991 / 0.9990 — the constant 1 is essentially attained). The ET inputs match
the archived arXiv text and Thm 4.2 matches the archived MV III draft. One isolated MAJOR
defect: Remark 8.3 cites a lower bound for a *different* density (units, Haar) as a lower
bound for the paper's δ*(T) (all integers). The rest are labelling/wording points.

## Summary verdicts per claim

| Claim | Verdict |
|---|---|
| Lemmas 2.1, 2.2 (atoms, class of one) | SOUND (wording, D4) |
| Lemma 2.4 (reduction, weights, C_1=e²) | SOUND |
| Lemma 2.5 (graded iterated quarantine, cost 1.02𝓛+7+(C_1𝓛/c)Ω_0) | SOUND |
| Thm 3.1 (ET inputs) vs source | SOUND-AFTER-REPAIRS (D2: κ range of (d)) |
| Lemmas 3.2–3.6, Thm 3.7 (S_0≪𝓛⁴, Ω_0≪𝓛⁴log𝓛; unconditional parts) | SOUND (mod ET) |
| Remark 3.8 numerics | reproduced from scratch (2.163, 2.402) |
| Thms 4.1, 4.2 + source caveat | SOUND (statement matches MV III 28.19) |
| Thm 5.1 (linear transfer incl. new (c) split f=f_1f_2) | SOUND |
| Lemmas 6.2–6.4, Thm 6.5 (C-1), Cor 6.6 | SOUND (+ brute force) |
| Remark 6.7 (sharpness) | SOUND |
| Remark 6.8 (Boolean form, influence) | SOUND; LMN/OD constant not checked |
| Thm 6.9, Cor 6.10 (filtration) | SOUND (+ brute force) |
| Lemma 7.1 (Haar means) | SOUND |
| Lemma 7.2, Cor 7.3 (LLL) | SOUND |
| Lemmas 7.4–7.8 (sandwich, error, cells, ℓ¹, twist) | SOUND |
| Thm 8.1 (assembly), proofs of Thms 1.1 and 1.2 | SOUND (D5 wording) |
| Cor 8.2 (Haar side upper bound) | SOUND |
| Remark 8.3 (two-sided Haar bound) | GAP (D1) |
| Remark 8.4, §9 status, labels | SOUND-AFTER-REPAIRS (D3) |
| Bibliography / novelty wording | SOUND-AFTER-REPAIRS (D6, D7) |
| Compile | clean (27 pp, no warnings) |

## Numbered defects

**D1 (MAJOR, isolated; does not affect Thms 1.1/1.2/Cor 8.2). Remark 8.3 compares two different
densities.** Cor 8.2 defines δ*(T) as the natural density of *all integers* n with W(n)>T.
[Haar] (`POINTWISE_HAAR.md` on main, §0) defines δ*(T) as the Haar measure on **Ẑ^× restricted
to n≡1 (24)**, i.e. on units. The two are not comparable in the direction needed: non-units
avoid every event at a prime dividing n (R(M) consists of unit classes), so the all-integer
density can only be larger, and a lower bound for log(1/δ*_unit) does not give one for
log(1/δ*_all). (Upper bounds do transfer, which is why Cor 8.2 is fine.) The displayed
"𝓛³/log𝓛 ≪ log(1/δ*(T)) ≪ 𝓛⁵log𝓛" is therefore unsupported as written.
*Repair:* either define δ*(T) in Cor 8.2 as the Haar density among units in the class
1 mod 24 (the proof of Cor 8.2 only produces units ≡1 mod Q, 24|Q, so the upper bound holds
verbatim for that normalisation, with a harmless change of the log𝓛+O(1) term), and then
Remark 8.3 is consistent; or keep the all-integer δ* and state the [Haar] bound for the unit
density only, without the two-sided display.

**D2 (MINOR). Thm 3.1(d) is stated more generally than ET.** ET derive (7.10) inside the
proof of Prop. 1.4, case A≤B, under the standing hypotheses A,B>1 and k≪(AB)^{O(1)}
(arXiv v6 p. 30). The paper's (d) says "for 2≤A≤B and κ≥1" with no size condition on κ.
Only κ=4 is used, so nothing breaks. *Repair:* write "for 2≤A≤B and κ=4" (or add
κ≪(AB)^{O(1)}).

**D3 (MINOR). Labels and §9 out of sync with the stated convention "every theorem header
carries a label".** (i) Remark 6.7 is headed "Sharpness; proved" but is not in the §9
"Proved" list. (ii) Remark 5.2 (`rem:linear`) has no header label at all, yet §9 lists it as
Assessment; Remark 6.8 has a header ("Boolean form and comparison") but no label, although
it contains proved statements (Boolean tail 4·2^{−(t+1)/k}, total influence (k/ln2)P(F=0),
q-ary literals) and one unchecked citation (the LMN/OD constant). (iii) Lemma 7.2 (classical)
and Thm 4.1 are fine. *Repair:* add "Assessment" to the header of Remark 5.2, "proved"
to Remark 6.8 (marking the LMN constant as cited), and add Remarks 6.7, 6.8 to §9.

**D4 (MINOR). Lemma 2.2, proof.** "Since 4A_M²≡A_M, the map D↦A_M²/D preserves this
congruence" — the fact used is that A_M is a unit and (−A_M)² = A_M², so
A_M²/D ≡ A_M²(−A_M)^{−1} = −A_M. The cited congruence 4A_M²≡A_M is true but not the reason.
*Repair:* replace by the one-line computation.

**D5 (MINOR). Thm 8.1, transfer step.** "By Lemma 7.1, E_H B=μ and E_H|B|/μ≤1.03": Lemma 7.1
is stated for cell combinations; |B| is not given as one. It is one (|B| is a function of
X mod D, hence a combination of point cells of modulus D, all consistent), but say so.
Likewise for Bψ the lemma's second clause is used; fine.

**D6 (MINOR). Bibliography.** [LT] can be taken off the TODO(verify) list: I verified
authors, title, arXiv 2109.04525 (v2, 15 Oct 2021) and "to appear at FOCS 2021" on arxiv.org.
The remaining TODO(verify) entries ([BBMST], [Bourgain], [Green], [Hough], [FFKPY], [LMO],
[TZcheb], [MV1], [RS], [TZ] journal data) and "Anonymous" are still open; fine for internal
circulation, must be closed before submission. The OD §4.4 constant 2·2^{−t/(20k)} in Remark
6.8 and the intro is unverified (O'Donnell's book is not in `sources/`).

**D7 (MINOR). Novelty wording.** The wording ("new to us … literature search partial …
no priority claim") is appropriately cautious, and the description of [LT] is accurate (LT
Fact 9: |f̂(S)|≤2^{|S|}Pr[S covered], unsigned, uniform measure, not used by LT; LT Fact 6:
unspecified C via the switching lemma). Before submission, specifically check: Håstad,
"A slight sharpening of LMN" (JCSS 2001); Tal, "Tight bounds on the Fourier spectrum of AC0"
(CCC 2017); the Fourier-growth line (Chattopadhyay–Hatami–Lovett–Tal and successors), since
G_F(λ) with constant λ is ‖T_{√λ}F‖² (noise operator with ρ>1), exactly the kind of quantity
studied there.

**D8 (MINOR, cosmetic).** Lemma 2.5 assumes c≤1/8, which is not used in its proof (only
c=1/64 is applied). Harmless; drop or explain.

## Checks performed

### Pass 1: §§1–2 (lines 1–425), §3 Lemmas 3.2–3.3 re-derived by hand
* Lemma 2.1 (atoms), 2.2 (class of one): re-derived; correct. (The phrase
  "Since 4A_M^2≡A_M" in the proof of 2.2 is not what is used — the involution
  preserves D≡−A_M because (−A_M)^2=A_M^2; harmless.)
* Lemma 2.4 (i)–(iii): re-derived; correct, incl. |Ω_ℓ|=ℓ^{f−a}, class size
  ℓ^{f−v}, gcd(M,Q)|g, ω(M)≤log M/log 3, (1+1/(𝓛−1))^𝓛≤e^{𝓛/(𝓛−1)}≤e² for 𝓛≥2.
* Lemma 2.5: termination, (a) via a_ℓ+1≤v_ℓ(M) on supports, (b), (c) step
  accounting (each (ℓ,a) once, sum over a<v_ℓ(M) of 1/(a+1) = H_v) re-derived;
  correct. Start cost: log 840+ϑ(𝓛)≤1.02𝓛+7 with ϑ(x)<1.01624x (RS) — fine.
* Lemma 3.2, 3.3 (parametrisation, injectivity, involution preserving g):
  re-derived; correct.

### Pass 2: §3 (Lemmas 3.4–3.6, Thm 3.7) and ET inputs vs `sources/elsholtz-tao-1107.1010.pdf`
* Thm 3.1 vs ET (pdftotext of the arXiv PDF): (a) = Prop. 1.4 (A,B>1, k≪(AB)^{O(1)}) ✓;
  (b) = Thm 7.1 (coefficients non-negative integers ≤N^l, ρ(p^j)≤C, implied constant
  depending on D,l,C) ✓; (c) = Cor. 7.4 (ET do not write N≥2; the paper's N≥2 is a
  harmless sharpening) ✓; (d) = (7.10), which ET state inside the case A≤B of the proof of
  Prop. 1.4 (so with A,B>1, k≪(AB)^{O(1)}); the paper's "2≤A≤B" and κ=4 are inside that
  range ✓. ρ_{κa}(m) = #{x mod m: κax²+1≡0} matches ET's ρ_ka ✓.
* Lemma 3.4: ET variable matching (ET's (a,b,A,B) = our (d,a,2B,2A)), Σ_{c∈[C,2C)}1/c<2,
  τ(P) choices of f, O(𝓛³) blocks; unconditional bound with P≤4T+1 ✓.
* Lemma 3.5: the ℓ|ad exclusion (P≡1 mod ℓ ⇒ ℓ∤f ⇒ ℓ∤N), the count C/q+1≤2C/q for q≤C,
  the C=1 / Y=2 split, Lemma 3.2(b) pointwise, and the dyadic sum Σ_j 𝓛/j ≪ 𝓛log𝓛 ✓.
* Lemma 3.6: Σ_{e|P}h(e)=Σ_{q|P}(1/i)τ(P/q) ✓; P<32Z_0³ ✓; case A≥B: a'≥1 (A≥q>x_0),
  coefficient bounds 8dq≤16A^{3/2}≤N'^5 for A≥16, N'≥A^{1/2}, ρ_{P♭}(2^j)=0,
  ρ_{P♭}(p^j)=ρ_{4d}(p^j)≤2 (p≠ℓ), ρ_{P♭}(ℓ^j)≤2, multiplicativity factor (1+2/(ℓ−1)),
  then (d) with ET's (A,B)=(2B,2A) ✓; case B>A: d_0∈(0,q), b_a≤4a², gcd(4a²,b_a)=1,
  coefficients ≤16B²≤N''^6 for B≥16, Cor 7.4 ✓; Σ_{q≤√Z_0}(1/i)/q ≪ loglog Z_0 ✓.
* Thm 3.7 incl. unconditional Ω_0≤𝓛S_0 and log S_0≤(log2+o(1))𝓛/log𝓛 (HW Thm 317) ✓.
* Verdict §3: SOUND (modulo ET, as labelled).
* From scratch (`scripts/review_r47_moment.py`): Lemmas 2.1, 2.2 for M≤400 (both
  descriptions of R(M) coincide; 1∉R(M)); involution preserves g; Lemma 3.3 identities and
  injectivity of (M,D)↦(a,c,d,f) for M≤20000. Remark 3.8 numbers reproduced:
  mean of h over D≤A_M is 2.163 (T=10⁴), 2.402 (T=10⁵) vs paper's 2.16, 2.40
  (S_0=55.3, 113.3; far below 𝓛⁴ — the bound is not sharp, as the paper says).

### Pass 3: §4 (Gallagher, Landau–Page) and §5 (Theorem 5.1, linear transfer)
* MV3 / Gallagher not available in `sources/` (unpublished MV3 draft; Gallagher 1970 not
  archived): statement of Thm 4.2 NOT checked against a source by me; checked only for
  internal consistency. The κ-enlargement argument in the "Source caveat" is correct
  (the piece (1−β)log x·x log x/(Q_G log Q_G) ≤ (log x/log Q_G)²x/Q_G, not written out,
  is immediate). Exceptional zero ⇒ zero in the Thm 4.1 region since κ≥1/c_1 ✓.
* Thm 5.1, re-derived line by line:
  – c(χ)=E_H[Bχ̄]/φ(Q) (reduction (ℤ/N_0)^×→(ℤ/Q)^× onto, kernel H) ✓;
  – (a) consistency ⇒ cell ∩ {1 mod Q} is one unit class mod lcm(d_i,Q) ✓, conductor ≤Qd_i≤Z ✓;
  – (c) real primitive conductor 2^e·(odd squarefree), e∈{0,2,3}; 8|Q ⇒ f_1|Q ⇒ ψ_1≡1 on H ✓;
    f_2∤d_i ⇒ ∃p|f_2, p∤d_iQ, and by CRT H ≅ (ℤ/p^v)^× × H', cell depends only on H'
    ⇒ twisted mean 0 ✓;
  – parameters (L≥2c≥2, Q_G≥Z, Q_G^{6c}≤x, log x≥(κL)², x≥C_4AZ⁴) ✓; R_1 bound with
    log N_0≤log Q+ψ(max d_i)≤2Z ✓; Case 0 constants 1/400+10⁻⁴ ✓;
  – exceptional case: u≤min(u,1)L, C_GALe^{−κL}≤C_GAe^{−L}≤1/400 ✓; Case A
    λ≥(1−e^{−1}−1/8)min(u,1)≥min(u,1)/2 with log x≥16 ✓, Page bound with q_1|Q≤Z ✓;
    Case B 1−1/2−1/200−1/400>0 ✓.
* Verdict Thm 5.1: SOUND (modulo Thms 4.1/4.2 as labelled).

### Pass 4: §6 Lemmas 6.2–6.4, Theorem 6.5 (C-1), re-derived by hand
* Second form of G (λ^U=Σ_{V⊆U}μ^V, ‖L_Vφ‖²=Σ_{U⊇V}‖φ^{=U}‖²) ✓; (6.2) Markov ✓.
* Trace remark (classes of m equal traces contribute Σ_{j≥1}C(m,j)(−1)^j=−1) ✓; this is
  what makes repeated events / equal supports harmless in Lemma 6.2.
* Lemma 6.2: fibrewise L_V, g_y = avoidance of restricted events, L_V kills cylinders with
  support ⊊ V, ‖L_Vc_y‖²≤E c_y² (L_V orthogonal projection), identification
  c_y(σ)=N_{𝓗(x)}(V) ✓. (V=∅ gives equality E F = P(no event) — consistent.)
* Lemma 6.3: τ̂(V)=(−1)^{|V|}N_𝓗(V) via the Möbius transform of 1[R∩U=∅] ✓; multilinear
  extension, two-point law p_v∈{1,−μ_v} with mean 0, variance μ_v ✓; R⊇P forced,
  Σ_{B⊆P^c∖U}(−μ)^Bλ^{P^c∖B}=λ^U ✓.
* Lemma 6.4: recursion Θ(𝒞)=λ_vΘ(𝒞/v)−μ_vΘ(𝒞−v) ✓, induction on |∪𝒞| incl. the ∅∈𝒞 and
  M=∅ cases ✓, final (w−λ_v)Π'+μ_vΠ'=(w−1)Π' ✓.
* Thm 6.5: independence of {J∩P=∅} over a matching, P(J∩P=∅)=1/w_J,
  E=Π[(1−1/w)+(w−1)²/w]=Π(w−1) ✓.
* Verdict Thm 6.5 (C-1): SOUND as written (pending the brute-force check below).
* From scratch (`scripts/review_r47_energy.py`, exact Efron–Stein on random non-uniform
  product spaces, n≤4 coordinates, alphabets 2–3, ≤5 events of width ≤3, 300 instances,
  weights scaled to max λ^{supp E}=2): G_F≤1 (max 0.9991 — the constant is essentially
  attained), Lemma 6.2 for every V, Lemma 6.3 identity (err ≤6e-16), Lemma 6.4 for every
  matching, Cor 6.6 tail ≤2^{−(t+1)/k} (max ratio 0.50): all pass. The single-event formula
  for G_{1−1_E} also checked (λ=2.2, π=0.01 gives G=1.0019>1, so λ^{supp}≤2 is needed).

### Pass 5: Cor 6.6, Remarks 6.7–6.8, Thm 6.9, Cor 6.10 (hand)
* Cor 6.6 ✓. Remark 6.7 (sharpness): F^{=U} factorisation over disjoint supports,
  ‖(1_E)^{=supp E}‖²=π(1−p)^k, limit e^{−2s}s^j/j!, s=j/2 and j!≤e j^{j+1/2}e^{−j}
  give ≥2^{−j}/(e√j) ✓ — correct and now genuinely proved.
* Remark 6.8: Boolean tail 4·2^{−(t+1)/k} ✓; total influence Σ|U|‖F^{=U}‖²≤(k/ln2)P(F=0)
  from λ^{|U|}≥1+|U|lnλ and Σ‖F^{=U}‖²=P(F=1) ✓; q-ary literals ✓. The LMN/OD constant
  2·2^{−t/(20k)} was NOT checked (O'Donnell's book not in `sources/`).
* Thm 6.9: P_{ℓ,j}F^{=U}∈{F^{=U},0} according to max U_ℓ≥j ✓; telescoping
  1+Σ_{i_0≤j≤max U_ℓ}μ'_{ℓ,j}=λ^{1+max U_ℓ} ✓; coarse space (head/tail per selected ℓ),
  splitting events into disjoint coarse cylinders leaves F unchanged and exactly one piece
  holds at x ✓; trace of coarse support on V' = {(ℓ,j)∈V: j<v_ℓ(E)} = Ê∩V ✓; extension to
  all V (μ'≥0) ✓; per-ℓ factor λ^{i_0+1}Π_{i_0<j<v}(1+λ^j(λ−1)) ≤ λ^{2v} using λ^j≤√2<λ+1 ✓.
* Cor 6.10: Πλ_ℓ^{2v_ℓ}=2^{log Πℓ^{v_ℓ}/𝓛}≤2 and weight 2^{log m_U/(2𝓛)} ✓.
* Verdict §6: SOUND (pending brute force of Thm 6.9).
* From scratch (`scripts/review_r47_filtration.py`): 400 random digit systems (≤3 coordinates,
  ≤6 digits, random i_0∈{0,1,2}, arbitrary digit laws, ≤5 prefix events, weights scaled to
  max Πλ^{2v}=2): the weighted energy of Thm 6.9 never exceeds 1 (max 0.99896). PASS.

### Pass 6: §7 up to Lemma 7.5 (digits, cells, Lemma 7.1 Haar means, LLL, sandwich, u_j)
* Digits of Ω_ℓ: the map x↦(δ_{ℓ,i})_{i≥a_ℓ} is a bijection onto the product of ranges
  ({1..ℓ−1} for i=0 when a_ℓ=0) ✓; E_{M,D} is a digit-prefix event with v_ℓ=v_ℓ(M) ✓.
* Lemma 7.1: CRT factorisation of H, v_ℓ(N_0)=max(a_ℓ,v_ℓ(D))≤f_ℓ, uniform fibres of
  Ω_ℓ→H_ℓ ✓; ψ has conductor prime to Q, so its primes have a_ℓ=0 ✓.
* Lemma 7.2/Cor 7.3 (LLL): x_E=2P(E)≤2w_ℓ≤1/32, Σ_{A∼E_i}x_A≤2Σ_{supp}w_ℓ≤1/32 (repeated
  events counted individually, consistent with w_ℓ) ✓; 1−x≥e^{−1.1x} on [0,1/32] ✓;
  conditional bound via independence of B from ∩_{A∉Γ(B)}Ā and the chain rule ✓;
  e^{1.1/32}=1.035≤1.04 ✓.
* F^{(j)}: restrictions are prefix events for the filtration from i_0^{(j)}=max(a_ℓ,v_ℓ(E_j))
  with the same v_ℓ and Πℓ^{v_ℓ}≤T ✓ (empty restriction ⇒ F^{(j)}≡0, still covered).
* Lemma 7.4 (sandwich): identity 1−F=ΣA_iF_{<i}, both cases, F−B=ΣA_i(Σ_{j<i}A_je_j)², CS
  with factor m, independence of A_j and F^{(j)}−u_j ✓. Validity on ℤ for any real u_j ✓.
* Lemma 7.5: 𝒟_j down-closed, (6.1)+Cor 6.10 per j ⇒ E[F−B]≤m²S·2^{−τ/(2𝓛)} ✓.

### Pass 7: Lemmas 7.6–7.8, Thm 8.1, proof of Thm 1.1 (hand)
* Lemma 7.6: E[F^{(j)}|δ_W] depends only on X_ℓ mod ℓ^{1+max W_ℓ} ⇒ cells of modulus
  m_W≤e^τ; expansion of B has ≤3 events and ≤2 u's per term ⇒ modulus ≤T³e^{2τ} ✓;
  compatibility of cells on Ω ⇔ on ℤ (CRT, consistency) ✓.
* Lemma 7.7 ✓. Lemma 7.8: f odd squarefree with a_ℓ=0 at its primes ✓; factorisation
  F=F'·1[X_{ℓ_0}∉Forb], E_{X_{ℓ_0}}ψ_{ℓ_0}=0 ✓; conditional LLL with J=supp E_i∖{ℓ_0} ✓;
  1.04/64=0.01625≤0.0163, E F'≤δ/0.9837, 0.0163/0.9837=0.01657≤0.0166,
  (0.01+0.0166)/0.99=0.0269<1/4 ✓.
* Thm 8.1: 2^{−τ/(2𝓛)}≤1/(100T⁴(S_1+1)e^{3S_1}) ⇒ E[F−B]≤e^{−3S}/100≤δ/100 (δ≥e^{−2.2S}) ✓;
  E|B|≤(1+2/99)μ≤1.03μ ✓; auxiliary prime ℓ_aux∈(R,2R] (Bertrand) keeps the cells consistent,
  is outside Q∏_{ℓ∈𝒫}ℓ (ℓ_aux>T), forces p>T ✓; Lemma 7.1 for B and |B| (|B| is a function
  of X mod D, hence a cell combination) ✓; log Z≤log Q+log2+2(3𝓛+2τ) ✓; m=0 case ✓;
  p≡1 (840) is the hard class 1² ✓.
* Proof of Thm 1.1: τ≪𝓛(𝓛+S_1)≪𝓛⁵, log Q≪𝓛Ω_0≪𝓛⁵log𝓛 ⇒ log p≪𝓛⁵log𝓛 ⇒
  𝓛⁵≥log p/(C log log p) ✓ (uses 𝓛<log p). Exponent 1/5 with (log log p)^{−1/5} ✓.

### Pass 8: Thm 1.2, Cor 8.2, Remarks 8.3–8.4, §9, bibliography, compile, sources
* Proof of Thm 1.2: log Q≤…+(C_1𝓛/c)𝓛S_0, τ≪𝓛(𝓛+S_1) ⇒ log log p≤log(S_0+1)+O(log𝓛);
  𝓛/log𝓛≥Y ⇒ 𝓛≥Y log𝓛≥Y log Y ✓. Constant 1/log 2 from HW Thm 317 ✓.
* Cor 8.2: density of {n≡1 (Q), X_ℓ(n)∈Ω_ℓ, F(n)=1} = Q^{−1}∏_{a_ℓ=0}(1−1/ℓ)·δ ✓ (CRT), δ≥e^{−2.2S_1},
  Mertens ✓; Gallagher indeed unused ✓.
* Thm 4.2 checked against the archived MV III draft (`sources/omega9/montgomery-mnt3.pdf`,
  Thm 28.19, pp. 229–230): statement matches (thresholds, both right-hand sides) ✓.
* [LT] verified by me on arxiv.org/abs/2109.04525 (V. Lecomte, L.-Y. Tan, "Sharper bounds on the
  Fourier concentration of DNFs", v2 15 Oct 2021, "to appear at FOCS 2021") ✓. The paper's
  description is accurate: LT Fact 9 is |f̂(S)|≤2^{|S|}·Pr[S covered by satisfied terms]
  (unsigned, uniform measure, and LT say they do not use it), and their degree concentration is
  Fact 6 ("there is a constant C>1 … ε-concentrated up to degree Cw log 1/ε", from the switching
  lemma) ✓.
* pdflatex (3 passes, clean copy in /tmp): 27 pp, **no** warnings, no overfull boxes, no
  undefined references ✓.
