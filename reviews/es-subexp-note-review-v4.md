# Referee report R56 — paper/es-subexp-note.tex v4 (hostile referee)

Branch reviewed: side-agent/subexp-paper-v4 @ 5da3fec (merged into side-agent/referee-subexp-v4).
Status: IN PROGRESS.

## Summary verdicts per claim
(to be filled)

## Numbered defects
(to be filled)

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
