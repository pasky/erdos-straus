# z60 MS105 — kernel census, run 2 (1000 < kernel s ≤ 10^5, n = s·m² < 2^64)

Command: `scripts/z60_ms105_sm2_big.sh 1000 100000 data/z60/ms105/sm2big` (engine `scripts/z60_ms105_sm2.c`,
LIM = 10^8, LATE = 10^6; 16 jobs, all `EXIT 0`).  Domain: squarefree s ≡ 1 (4), 1000 < s ≤ 10^5, gcd(s,105) = 1
(10 955 kernels); odd m with gcd(m,105) = 1 and s·m² < 2^64.  Job files `jobs/jobNNN.txt` (s, m_max), outputs
`jobs/jobNNN.out` (formats as in `../sm2/README.md`; `L` lines = first hit ≥ 10^6).
Result: 61 785 619 898 inputs.  UNK exactly at the 14 known zeros with kernel in (1000, 10^5]:
1969, 2641, 2929, 5161, 5569, 9601, 12001, 18001, 23881, 23929, 25441, 83449, 90889 (m = 1) and 752 257 = 6217·11²
(s = 6217, m = 11).  Largest first-hit modulus 6 637 967 (s = 92 989, m = 10 060 349); 402 inputs with first hit ≥ 10^6.
