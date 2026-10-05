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
