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
