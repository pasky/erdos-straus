# z55 TDCAL: odd squares (2i+1)^2, i = 50600..53599 (sq10b control).
import sys
open(sys.argv[1] + "/sq10b.txt", "w").write("\n".join(str((2*i+1)**2) for i in range(50600, 53600)) + "\n")
