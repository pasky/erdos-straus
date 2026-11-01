# z52d P2 TO8 Z2935 follow-up: R_t(n) = #{(u,v)>=2 : tuv-u-v = n} = #{u>=2 : (tu-1) | (tn+1), (tn+1)/(tu-1) >= 2t-1}
# least level t>=2 with R_t(n)>0, for the 7 n<=20000 failing at all t in [3,64].
def R(t, n):
    N = t * n + 1; cnt = 0; u = 2
    while (t * u - 1) * (2 * t - 1) <= N:
        if N % (t * u - 1) == 0: cnt += 1
        u += 1
    return cnt
import sys
for n in [126, 3136, 3250, 5922, 6150, 6336, 9090]:
    least = None
    for t in range(2, 20001):
        if R(t, n) > 0: least = t; break
    print(n, "least t with R_t(n)>0:", least, " R_least=", R(least, n) if least else None, " n=", n, "factor check:", [t for t in range(2,65) if R(t,n)>0][:5])
