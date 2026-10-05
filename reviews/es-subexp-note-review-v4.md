# Referee report R56 — paper/es-subexp-note.tex v4 (hostile referee)

Branch reviewed: side-agent/subexp-paper-v4 @ 5da3fec (merged into side-agent/referee-subexp-v4).
Status: COMPLETE (round 1).

**Recommendation: minor revision (accept after minor changes).** No FATAL or MAJOR defect. Every new proof of v4 (Jacobi lemma, square-class process and supermartingale bookkeeping incl. the pair potential, Haar masses via NT, Haar upper bound, Janson-type inequality, Haar lower bound, coset transfer, new twist lemma, assembly to exponent 1/4, planting, level barrier, class-uniform lemmas, ceiling theorem and its corollaries) was re-derived line by line. From-scratch code: Jacobi lemma on all 2 401 032 atoms with M≤2·10^5; Janson-type inequality + Lemmas 4.1/4.2 by exact enumeration on random non-uniform product spaces; planting lemma by exact rational arithmetic (with a control showing the hypothesis is needed). NT hypotheses checked against the archived NT and Henriot PDFs. Defects are presentational/labelling only.

## Summary verdicts per claim

| Claim | Verdict |
|---|---|
| Compile (pdflatex ×2) | clean: 39 pp, 0 undefined, 3 overfull (<10pt) |
| Lemma 2.1 atoms; Lemma 2.2 Jacobi; Lemma 2.3 | SOUND (+ brute force, M≤2·10^5) |
| Def 2.4, Lemma 2.5 (reduction, weights, hardness) | SOUND |
| Lemma 2.7 LLL; Lemma 2.8 β-LLL | SOUND |
| Square-class process, Lemma 2.9 (a)–(d) | SOUND |
| Thm 3.1 NT transcription vs sources | SOUND (m2) |
| Lemma 3.2 (A),(B) | SOUND |
| Thm 3.3 Haar upper bound | SOUND (mod NT) |
| Lemmas 4.1, 4.2, Thm 4.3 Janson-type | SOUND (+ exact enumeration) |
| Thm 4.4, Lemmas 4.5–4.7 Haar lower bound | SOUND (mod FL; m6, m7) |
| Thm 6.1 linear transfer (coset rH) | SOUND (mod G+LP) |
| §8 changes (digits, Lemma 8.1, eq. lllhyp, twist Lemma 8.7) | SOUND |
| Thm 9.1 assembly, proof of Thm 1.1 (exponent 1/4) | SOUND (mod G+LP, NT) |
| Lemma 10.1 planting | SOUND (+ exact rational check) |
| Lemma 10.2 level barrier | SOUND (m4) |
| Lemmas 10.3–10.5 | SOUND (m5) |
| Thm 10.6 ceiling (= Thm 1.3) | SOUND (mod G+LP, FL) |
| Cor 10.7 (1/4 ceiling, proved implication) + scope | SOUND |
| Cor 10.8 energy tail | SOUND |
| Abstract/intro vs proofs | SOUND-AFTER-REPAIRS (m1, m3) |
| Bibliography TODO(verify) | partly verified (m8) |

## Numbered defects

No FATAL, no MAJOR.

**m1 (MINOR, abstract).** The abstract states the Haar-side two-sided bound and the ceiling without their inputs, while it does list Gallagher+NT for Thm 1.1. The Haar upper bound needs NT, the lower bound the fundamental lemma, the ceiling Gallagher+Landau–Page+FL. *Repair:* add "(under the same inputs, and the fundamental lemma of sieve theory)" after the Haar and ceiling sentences, or one sentence "all results are proved modulo these cited theorems and the fundamental lemma".

**m2 (MINOR, Thm 3.1 / §3).** Henriot (p.5, after (2.10)) notes that NT's own class 𝓜_k asks the submultiplicativity for all a_i,b_i with (a_i,b_i)=1, so the transcribed class is slightly *larger* than NT's, and the transcribed theorem is Henriot's reading of NT's proof. The paper attributes it to [NT, Thm 1]. No gap: F(n₁,n₂)=τ(n₁²)f₂(n₂) (and the variant with τ((n₂)_Y)) is a product of multiplicative functions in separate variables and lies in NT's original class; also NT's own range (ε<1/(8g²), x^{4g²ε}≤y≤x) covers ε=1/200, g=2, y=x. *Repair:* add one sentence saying so, so that the citation stands on NT alone.

**m3 (MINOR, intro "The method", last paragraph).** "The ceiling shows that the level 𝓛S is forced": the construction has level e^{O(𝓛⁴log𝓛)}, the ceiling excludes level e^{c𝓛⁴/log𝓛}. *Repair:* "forced up to a factor (log𝓛)²" (as correctly said in Cor 10.7/10.8).

**m4 (MINOR, §10 "The ES instance").** "everything else is small" should say explicitly that for big ℓ∤Q the higher ℓ-adic digits of n (beyond n mod ℓ) are small coordinates, independent of X_ℓ on the units, and that a level-D function depends on at most the number of *distinct* primes >T^{0.6} of q (≤log D/(0.6𝓛)). The argument is right; this is needed for Lemma 10.2's "independent coordinates" to apply verbatim to functions of n mod qQ with ℓ²|q.

**m5 (MINOR, Lemma 10.5 proof).** "one class modulo vq''/(q'',t) or empty" — give the reason: κ≡b with b a unit mod v, so if a prime of v divides q''/(q'',t) the set is empty, otherwise CRT gives one class mod the product.

**m6 (nit, Lemma 4.5).** The count of M divisible by p² with p≥y is ≤X/(4n(y−1))+π(√(2X)) rather than X/(4ny)+√(2X); immaterial.

**m7 (nit, Lemma 4.6).** (F4) actually gives log(V/v₀)/d≤(𝓛/2)/(4n'); the stated 𝓛/(4n') is a valid but loose bound — fine as is.

**m8 (MINOR, bibliography).** I verified [BGP], [PYY] (journal data), [Henriot] (journal via DOI 10.1017/S0305004111000752), [Tao254A] (date; Thm 5 is the dual sieve problem). *Repair:* move these out of the TODO(verify, v4) comment; still to check: [ErdosSpencer], [Janson], and the [FI] numbering (Lemma 6.3, Cor. 6.10).

**m9 (cosmetic).** Three overfull hboxes (l.274–289, 593, 733), 7.7–9.5pt.

## Work log / checks (from scratch)
* **Compile.** `pdflatex` ×2 on v4: 39 pp., 0 undefined refs/citations, 3 overfull hboxes (9.5pt at l.274–289, 7.7pt l.593, 8.7pt l.733). OK.
* **Lemma 2.1 (atoms).** Re-derived (exponent split u_q,w_q,v_q checked in both cases d≤a, d>a). Brute force `scripts/review_r56_jacobi.py`: `{-u v^{-1}} = R(M)` for all M≤4000. SOUND.
* **Lemma 2.2 (Jacobi).** Re-derived (reciprocity with (M−1)/2 odd; p=2 via M≡7 (8)). Brute force from scratch: (b) and (a) on **all 2 401 032 atoms with M≤2·10^5** (count agrees with the paper exactly), no failures. SOUND.
* **Lemma 2.5.** (i) re-derived: supp ⊂ 𝒫 because ℓ^{v_ℓ(M)}≤M≤T ⇒ v_ℓ(M)≤f_ℓ. (ii) re-derived. (iii) checked: unit squares mod 840 = {1,121,169,289,361,529} = units ≡1 (8) that are QR mod 3,5,7. SOUND.
* **Lemma 2.7 (LLL with conditioning).** Standard (AS 5.1.1; third part re-derived: independence of B from the events not meeting J, then chain rule). SOUND.
* **Lemma 2.8 (β-LLL).** Re-derived: x_A≤w̃_v≤η≤1/4 (since β≤e^{1/3}); −log(1−x)≤4x/3 on [0,1/4]; Σ_{A' meets J}x_{A'}≤Σ_{v∈J}w̃_v; exp(−(4/3)|J|η)=β^{−|J|}. Hypothesis of 2.7 holds (product over A'∼A, A'≠A is ≥ product over all A' meeting supp A). Both conclusions follow. SOUND.
* **Square-class process + Lemma 2.9 (bookkeeping).** Re-derived line by line.
  (a) a≥1 step: martingale (factor ℓ·1[match], match prob 1/ℓ); a=0 step: factor (ℓ−1)·1[match], match prob 2/(ℓ−1)·1[(−4D/ℓ)=1], mean (1+(−d/ℓ))p≤2p, paid by u→u−1 (all stepped primes ≤Y, forced ones 3,5,7≤Y). p_0=1/φ(M) since M odd and the start fibre is n≡1 (8). Choice of the stepped prime is predictable, so the supermartingale property holds. OK.
  (b) At τ_{ℓ,a}: atoms with ℓ∈supp are exactly v_ℓ(M)≥a+1, non-survivors have p=0, so η<w̃_ℓ≤G^{(ℓ,a)}; optional stopping (bounded number of steps; truncate τ at the deterministic step bound, G≥0). Σ_{ℓ≤Y}Σ_{a<v_ℓ(M)}logℓ=log M_Y. Forced steps add log105. OK.
  (c) immediate from (a) and s_end≤ω. OK.
  (d) Pair potential re-derived: ρ divided by N=ℓ'−1 (a=0: φ(ℓ'^j)→ℓ'^{j−1}) or N=ℓ' (a≥1: ℓ'^{j−a}→ℓ'^{j−a−1}); joint factor N·1[match]; disagreement ⇒ Π→0; one-sided case: ρ already 1 because j≤a. R_0≤φ(gcd(M_F,M_F')). Removing the ℓ-condition (ℓ>Y never stepped) gives exactly B_2(ℓ) (ω_Y unchanged as ℓ>Y). Chebyshev + union bound. OK.
  Verdict: SOUND. (Minor presentational point m1 below.)
* **Thm 3.1 (Nair–Tenenbaum) vs sources.** Checked against `sources/nair-tenenbaum-1998.pdf` (Thm 1, p.125: ε<1/(8g²), 0<δ<1, x≥c₀‖Q‖^δ, x^{4g²ε}≤y≤x) and `sources/henriot-1102.1643.pdf` (Thm 1 / (1.1): ε≤αδ/(12g²), x^α<y≤x). The paper's transcription matches Henriot's (1.1). With g=2, α=δ=1/2: αδ/(12g²)=1/192 ≥ 1/200 ✓.; y=x is inside both NT's and Henriot's ranges. Henriot (p.5, after (2.10)) notes that NT's own class 𝓜_k requires the submultiplicativity for all a_i,b_i with (a_i,b_i)=1 (stronger hypothesis than the transcribed one); the paper's F(n₁,n₂)=τ(n₁²)f₂(n₂) is a product of multiplicative functions in separate variables, so it satisfies NT's original stronger condition too — no gap, but see m-NT below. Q=X(4X−1): no fixed prime divisor (Q(1)=3, Q(2)=14) ✓, ρ_{Q₂}(m)=1[m odd] ✓.
* **Lemma 3.2 (A).** Re-derived: F∈𝓜₂(8,B,1/200) uniformly in T,Y (τ(p^{2k})=2k+1≤8^k, f₂(p^k)≤3β≤6; β≤2); Euler products give (log x)^{3}·(log x)^β(log Y)^β·(log x)^{−2}; (log x)^{β−1}≤e because log x≤𝓛. Second bound: log M_Y≤logY·Ω(M_Y)≤logY·τ(M_Y), factor at p≤Y becomes 1+4β/(p−1) ⇒ (log Y)^{3β}(log x)^β. Both bounds ✓.
* **Lemma 3.2 (B).** Re-derived: gcd(M,M')/ℓ^{min}|gcd(m,m'); gcd=Σφ(e); Cauchy–Schwarz with Σ_{k≤T}1/k≤𝓛+1; N=eℓk, φ(e)/(eℓ)≤1/ℓ, ≤τ(N) factorisations, Σ_{ℓ|N,ℓ>Y}1/ℓ≤ω(N)/Y. Ξ via Cauchy–Schwarz with M≥3n and Euler products with f(p)≤256 absolute, uniform in Y ✓.
* **Thm 3.3 (Haar upper).** Re-derived: Y=𝓛^{C₀+4} gives η^{−2}(𝓛+1)𝓛^{C₀}/Y≍(log𝓛)²/𝓛³→0; Markov twice + union bound (3·1/4<1); E log Q≪log𝓛·𝓛³(log𝓛)⁴; δ*≥φ(24)/φ(Q)·δ (24|Q; F depends only on X_ℓ, ℓ∈𝒫, which are independent uniform on Ω_ℓ inside the class). The "exactly half" normalisation remark is right (atom (3,1) kills n≡2 (3); nothing depends on n mod 8). SOUND.
* **Lemma 4.1 (compatible events).** Re-derived (C∩A=A∩C', C'⊇C independent of X_{S_A}). ✓
* **Lemma 4.2 (lopsided LLL).** Re-derived: Lemma 4.1 gives exactly the Erdős–Spencer negative-dependence condition for the conflict graph; the extension to an arbitrary atomic A splits 𝒮 into conflicting/non-conflicting parts. ✓
* **Thm 4.3 (Janson-type).** Re-derived line by line: B_i⊆B_i^d; on E_i, conflicting E_j are impossible, bit-sharing E_j become E_j' on coordinates outside S_i, B_i^d is independent of E_i; Lemma 4.2 applied to A=E_j' (conflicts of E_j' are conflicts of E_j, so factor ≤K); degenerate case S_j⊆S_i (E_j'=Ω) is consistent. Second form: random subfamily, same x_E, K'≤K, p=min(1,μ/(2KΔ)). Remark's sufficient condition (x_E=2P, P≤1/8, ΣΓ P≤1/8 ⇒ K≤e^{1/3}) ✓.
  **From-scratch exact enumeration** `scripts/review_r56_janson.py`: 4000 random small product spaces with *non-uniform* marginals and random atomic events; on the 1749 instances satisfying the LLL hypothesis (x_E∈{1.5,2,3}·P(E)) both Janson bounds, Lemma 4.1 and Lemma 4.2 (random 𝒮) hold exactly; no violation (min slack ≈0, attained in trivial cases). SOUND.
* **Thm 4.4 (Haar lower) and Lemmas 4.5–4.7.** Re-derived every inequality: (F1) D≤n²≤T^{1/5}<M/4 ⇒ distinct residues; D|A²⇔D*|A and 2^{ω(n)} preimages ✓; (F4) by integral comparison ✓; Lemma 4.5: M≡−1 (4n) ⇒ n|A_M, sifting a progression of length ≥X^{4/5}/4 at level X^{1/2} by p<y, p∤2n (s→∞), non-squarefree removal negligible ✓; Lemma 4.6: w_q≤(2/q)Σ_{D'}(𝓛/(4n')+min(1,q/√T)) and the final O(1/(𝓛log𝓛)) ✓ (constants slightly generous: log(V/v₀)≤𝓛/2 suffices); Lemma 4.7: g|D−D', M≠M' by (F1), P(E∩E')=1/(φ(g)φ(v)φ(v'))≤8/(gvv'), case (a) Δ_a≪𝓛⁴/y+𝓛³logN₀/N₀, case (b) all three bracket coefficients re-computed and agree exactly with the paper; Δ_b≪𝓛⁷/y=𝓛² ✓. Conclusion μ−e^{1/3}Δ≥c₁𝓛³/(5log𝓛)−C𝓛² ✓. The fundamental-lemma citation [FI, Lemma 6.3, Cor. 6.10] could not be checked (Opera de Cribro not in sources/) — see m-FI. SOUND (mod FL).
* **§5 (Gallagher/Landau–Page).** Unchanged from v3 (refereed SOUND in R47); new sentence on the range condition re-checked for Lemma 10.4 later.
* **Thm 6.1 (linear transfer, coset rH).** New part re-derived: real primitive characters with f₁|Q (8|Q, odd part squarefree) are products of a real character mod 8 (all =1 at r≡1 (8)) and Legendre symbols at odd primes of Q (=1 at r, a QR), so χ=ψ₂ on H; cells with f₂∤d_i average to 0 on H (p|f₂, p∤d_iQ is uniform/independent on H∩cell); Case A's χ₁ then has conductor |Q; Case B uses only the twist condition. The consistency condition b_i≡r (gcd(d_i,Q)) is exactly what makes cell∩H one unit class mod lcm(d_i,Q). Rest verbatim from v3. SOUND.
* **§8 (sandwich) — v4 changes.** Digits: Ω_ℓ↔(δ_{ℓ,i})_{i≥a_ℓ} bijection for general r ✓. Lemma 8.1 (Haar means with r'≡r (Q), r'≡1 (ℓ')): note ℓ'∤Q∏_{ℓ∈𝒫}ℓ forces ℓ'>T; CRT product structure and v_ℓ(N₀)≤f_ℓ ✓. eq. (lllhyp): η=¾log(1+1/log𝓛)=0.1886 at 𝓛=33 ✓, and β≤e^{1/3} needs only 𝓛≥13 ✓. Twist Lemma 8.7 re-derived: F=F'·1[X_{ℓ₀}∉Forb] with Forb measurable w.r.t. X_{−ℓ₀}; union bound; Lemma 2.8's conditional bound with J=supp E_i∖{ℓ₀} gives β^{s−1}; Σ=β^{−1}w̃_{ℓ₀}EF'≤ηEF'; EF'≤δ/(1−η); 0.01+0.19/0.81=0.2446≤0.245, 0.245/0.99=0.2475<1/4 ✓. Lemmas 8.2–8.6 unchanged from v3 (R47: SOUND). SOUND.
* **Thm 9.1 (assembly) and proof of Thm 1.1.** Re-derived: m²≤T⁴ and the choice of τ give E[F−B]≤e^{−3S₁}/100≤δ/100 (as 4S_β/3≤3S₁); E|B|≤(1+2/99)μ≤1.03μ; log Z≤log Q+log2R+log max d_i≤log Q+4τ+6𝓛+log2 ✓; ℓ_aux∈(R,2R] keeps cells consistent (gcd(d_i,Q')=gcd(d_i,Q)) and gives ℓ_aux|p−1 ⇒ p>T ✓; hardness by Lemma 2.5(iii) ✓; twist condition transfers via Lemma 8.1 ✓. Final chain τ≪𝓛(𝓛+S₁)≪𝓛⁴log𝓛, log Q≪𝓛³(log𝓛)⁵ ⇒ log p≤C𝓛⁴log𝓛 ⇒ log W(p)>𝓛≥(log p/(C log log p))^{1/4} ✓. SOUND (mod Gallagher+Landau–Page, NT).
* **Lemma 10.1 (planting).** Re-derived: σ_J-mass of {x_K=1_z} is (−1)^{|z|+1}[z⊆J]Σ_{y'⊆J∖K}(−1)^{|y'|}=0 for |K|≤k; ν(1_∅)=0; negative charge only on even |y|=j≥2, equal to P₀∏_y r·e_{k+1−j}(s)/e_{k+1}(r); a·e_a(s)≥e_{a−1}(s)(Σs−(a−1)r*), Σs≥R−j r*, j+a−1≤2k+1. ✓
  **From-scratch exact (rational) check** `scripts/review_r56_planting.py`: ν built as in the proof on 635 random instances satisfying (10.1) (N≤9, k≤3): all masses ≥0, ν(0)=0, all k-wise marginals exact. Control: on instances *violating* (10.1) (but with R≥k+1) the same ν has negative mass in 35/172 cases, so the test is not vacuous. SOUND.
* **Lemma 10.2 (level barrier).** Re-derived: under ν, given x_s, the bits on any K with |K|≤k have the true product law, hence so do (X_b)_{b∈K}; E B=E_ν B≤E_ν F=0. Uses r*(x_s)≤r* (the planting hypothesis is monotone in r*). SOUND.
* **Lemma 10.3 (unique small part).** Re-derived: v≡−ℓ^{−1} (4n_D), v≤V≤n_D<4n_D ⇒ unique; |D−D'|<T^{2ε}<ℓ ⇒ distinct classes mod ℓ; p_ℓ≤X(1+L)/(ℓ−1)≤𝓛T^{−0.55}≤T^{−1/2} for ε≤1/20 ✓. SOUND (see m-big for a wording point on "small" coordinates at big primes).
* **Lemma 10.4 (class-uniform primes).** Re-derived: orthogonality with χ→χ* (cost ≤log q), exceptional term sign, both error forms ≤x/16 for ε small (absolute, via C_G, κ), range Q_G^{6c}≤x for ε<0.1/c; q₁≤𝓛^{1.9} ⇒ x^{β₁−1}≤exp(−c𝓛^{0.05}/(log𝓛)²)=o(1). Partial summation: (7/8)log(7/6)=0.1349>0.13 ✓. Remark on q'': checked e∈{0,2,3} cases of q₁=2^e f' ✓; τ(q'')/q''≤4𝓛^{−1.8} ✓. SOUND (mod Gallagher+LP).
* **Lemma 10.5 (class-uniform D).** Re-derived: n_D=κt∈(X^{2/3}t,X]⊆[V,X]; squarefree count in a progression with σ_v≥6/π²; Σ_t t^{−1}log(X^{1/3}/t)≈L²/18−L²/72=L²/24 ✓; H_exc: the "one class or empty" step is right because κ≡b (unit mod v) forbids any common prime of v and q''/(q'',t) — this justification is implicit (m-cuD). Σ_t(q'',t)/t≤τ(q'')(1+L) ✓. Final constant 6/(96π²)=0.00633>1/200 ✓. SOUND.
* **Thm 10.6 (no positive low-level minorant).** Re-derived: big primes of Q subtracted (ω_big(Q)p*≤T^{−0.45}); D≡−x/4 (v) with x a unit ⇒ gcd(v,2n_D)=1; R(x)≥0.13·(L²/200)·c₃(εL/3)/(6log𝓛)≍ε³𝓛³/log𝓛 *for every* x; (k+1)+(2k+1)r*≤(k+1)(1+4p*)≤μ* when c≤0.3c₉ε³; F*'s events have M=vℓ≤T^{0.7+ε/3}≤T so 𝓕*⊆𝓔. Constants c,ε absolute; N_exc depends only on T; uniform in (Q,r) with log Q≤T^{0.05}. SOUND (mod Gallagher+LP, FL).
* **Cor 10.7 (1/4 ceiling, proved implication).** Re-derived; case log Q>T^{0.05} uses the hypothesis Z≥Q; the (loglog p)^{1/2} gap is (c(log p/loglog p)^{1/4}) vs ((log x·loglog x)^{1/4}) ✓. Scope paragraph is accurate and appropriately restrictive. SOUND.
* **Cor 10.8 (energy tail).** Re-derived: τ≪ρ(𝓛+S₁) ⇒ log(level)≤3𝓛+2τ≤c𝓛⁴/log𝓛 for c' small; fibre of Thm 3.3 has log Q≪𝓛³(log𝓛)⁵≤T^{0.05}; B≤F_res≤1[W>T] on all units of the fibre. Labels (xz,G,NT,FL) correct. SOUND.
* **§11 status / labels.** Every header label checked against the proofs above: consistent (Thm 1.1/9.1 mod G(+LP), NT; Thm 3.3 mod NT; Thm 4.4 mod FL; Thm 10.6 mod G(+LP), FL; Cor 10.8 adds NT). No circularity: §10 uses only §§4–5 tools + FL, not Thm 1.1.
* **Bibliography TODO(verify, v4).** Checked online now: [BGP] arXiv:1201.3261 title/authors ✓; [PYY] arXiv:0801.0059, journal ref "Random Struct. Alg. 38, 502–525, 2011" ✓; [Henriot] arXiv related DOI 10.1017/S0305004111000752 (Math. Proc. Camb. Phil. Soc.) ✓; [Tao254A] "254A, Notes 4: Some sieve theory", 21 Jan 2015, **Theorem 5 = "Dual sieve problem"** ✓ (so the citation [Tao254A, Thm. 5] is apt). Not checked: [ErdosSpencer], [Janson] (standard, details look right), [FI] Lemma 6.3/Cor. 6.10 numbering (book not archived).
