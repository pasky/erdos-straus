# z60 MS105 — near squares n = m² + c
Command: `scripts/z60_ms105_win_nsq_run.sh` part (b): engine `scripts/z60_ms105_nsq.c`, LIM = 10^8, LATE = 10^6;
c ∈ ±{8, 16, …, 200} (50 values; c ≡ 0 mod 8 so n ≡ 1 mod 8 for odd m); odd m ≤ 10^9; inputs n > 0, n ≡ 1 (4),
gcd(n, 105) = 1, n not a square (n ≤ 10^18 + 200).  Both files EXIT 0.
Result: 11 361 904 661 inputs; 27 UNK lines, whose n are exactly 15 distinct known zeros ≤ 10^10 (409, 577, 1969, 2641,
2929, 5161, 5569, 9601, 12001, 23881, 23929, 25441, 83449, 1 134 241, 12 538 801; all in `../zeros105_1e10.txt`).
Largest first hit 15 110 783 (c = 48, m = 760 301 293).
