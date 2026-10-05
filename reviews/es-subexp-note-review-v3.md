# Referee report R47 — `paper/es-subexp-note.tex` v3 (exponent 1/5)

Referee: hostile side agent R47 (branch `side-agent/referee-subexp-v3`).
Author branch: `side-agent/subexp-paper-v3` @ 67cda1e (merged non-ff into referee branch; ff-only failed because main moved).

Status: IN PROGRESS.

## Summary verdicts per claim

(to be filled)

## Numbered defects

(to be filled)

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
