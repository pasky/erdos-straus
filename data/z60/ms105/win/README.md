# z60 MS105 — m-windows beyond 2^64 for the 106 kernels s ≤ 1000
Command: `scripts/z60_ms105_win_nsq_run.sh` part (a): engine `scripts/z60_ms105_sm2w.c` (n mod d = s·(m mod d)² mod d;
hits re-verified in 128-bit), LIM = 10^8, LATE = 10^6.  Windows m ∈ [10^k, 10^k + 2·10^7], k = 10, …, 17, odd m coprime
to 105 (n = s·m² from ~1.3·10^21 to ~10^37).  Both lanes EXIT 0.
Result: 848 (s, window) runs, 3 876 571 898 inputs, no UNK.  Largest first hit 2 512 619 (s = 37, m = 10 013 243 339).
Engine cross-check: identical summaries to `z60_ms105_sm2.c` on s ∈ {13, 409, 997}, m ≤ 10^6.
