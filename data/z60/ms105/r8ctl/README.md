# z60 MS105 — F2 control: kernel census (s ≤ 1000, n = s·m² < 2^64) for the C-even sub-line R₈
`scripts/z60_ms105_r8ctl_run.sh` (`z60_ms105_sm2.c -DR8`, LIM = 10^8; 3 lanes EXIT 0).  Same 6 086 436 506 inputs as
`../sm2/`.  321 UNK (no R₈ witness d ≤ 10^8): 40 with n ≤ 7.5·10^7 (exact R₈ zeros), 281 with n > 10^10 (up to 1.84·10^19;
NOT certified zeros — four s = 29 spot checks with LIM = 10^10 found hits at 1.0–1.45·10^8).  Largest decided first hit
99 944 711.  Engine validated against brute-force R₈ for n ≤ 3000 and against the 12 R₈-zero primes of
`data/z58/screens/r8_zeros_1e10.txt` (UNK with LIM = 1.5·10^10 ≥ (4n+1)/3).
