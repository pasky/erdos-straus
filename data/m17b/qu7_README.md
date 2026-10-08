Level-7 Q/U data for POINTWISE_MORDELL17B Comp 3.1 (rho_1), stored by O96 because regenerating them takes
2-3 min per engine (too slow for verify.py).
* `qu7_o93/{Q7,U7}.txt`: O93/O83 engine `scripts/m17_enum.c` (`m17_enum Q 7 | sort -u`, `m17_enum U 7 | sort -u`);
  box residues mod 17^7 (707 Q data, 826 U data).
* `qu7_r83/{S7,U7}.txt`: R83 from-scratch engine `scripts/review_m17_enum.c` (`S 7`, `U 7`, sorted); raw
  parameter data (S: a m d; U: e a b i), 707 resp. 826 lines.
verify.py block (eg) re-validates every stored datum against its defining equations, checks that the two
engines give the same box sets, and recomputes rho_1 with both union scripts.
