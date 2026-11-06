# z60 MS105 — n = s·m² family search, run 1 (kernel s ≤ 1000, n < 2^64)

Command: `scripts/z60_ms105_sm2_run.sh` (engine `scripts/z60_ms105_sm2.c`, LIM = 10^8, LATE = 10^5).
Domain: squarefree s ≡ 1 (4), 13 ≤ s ≤ 1000, gcd(s, 105) = 1 (106 values); odd m ≥ 1 with gcd(m, 105) = 1 and
s·m² < 2^64.  Line formats: `S s mlo mhi count maxd argm unk late≥2^10 late≥2^14`; `U s m n` (no d-form hit ≤ LIM);
`L s m n d` (first hit d ≥ 10^5).  All four lanes exit 0.
Result: 6 086 436 506 inputs; UNK exactly at (s, m) = (409, 1), (577, 1) — the known prime zeros 409, 577 (< 10^10,
below the (MS⁺₁₀₅) threshold).  Largest first-hit modulus 3 048 771 (s = 949, m = 121 061 833).
Validation: engine reproduces exactly the 27 zeros n ≤ 10^6 (n ≡ 1 (4), gcd(n,105) = 1, non-square) of the z58 LOGIC
census when run with LIM ≥ (4n+1)/3, and reports all 38 zeros ≤ 10^10 coprime to 105 as UNK with LIM = 10^8 > (4n+1)/3.
