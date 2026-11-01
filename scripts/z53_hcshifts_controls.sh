#!/bin/bash
# z53 HCSHIFTS controls: odd squares m^2 (m odd, 100001..110000) and near-squares p = m^2 + k (k in 1,8,9,16,17,24;
# first 2000 primes = 1 (8) with m >= 10^5).  Needs /tmp/z53hc (gcc -O2 -o /tmp/z53hc scripts/z53_hcshifts_hc.c).
set -e
ulimit -v 2000000
python3 - <<'PY'
def isp(n):
    if n < 2: return False
    for q in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n % q == 0: return n == q
    d = n - 1; s = 0
    while d % 2 == 0: d //= 2; s += 1
    for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
with open('/tmp/z53_nearsq.txt', 'w') as out:
    for k in [1, 8, 9, 16, 17, 24]:
        c = 0; m = 10**5
        while c < 2000:
            p = m * m + k
            if p % 8 == 1 and isp(p): out.write(f'{p} {k}\n'); c += 1
            m += 1
with open('/tmp/z53_squares.txt', 'w') as sq:
    for m in range(100001, 110001, 2): sq.write(f'{m*m}\n')
PY
timeout 900 /tmp/z53hc list 256 4096 < /tmp/z53_squares.txt > /tmp/z53_squares_out.txt
awk '{print $1}' /tmp/z53_nearsq.txt | timeout 900 /tmp/z53hc list 256 4096 > /tmp/z53_nearsq_out.txt
awk '!/^#/{n++; if($2!=0) bad++} END{print "odd squares:", n, "values; any firing line <= 256:", bad+0}' /tmp/z53_squares_out.txt
paste <(grep -v '^#' /tmp/z53_nearsq_out.txt) <(awk '{print $2}' /tmp/z53_nearsq.txt) | awk '{k=$NF; n[k]++; if($2>4) a[k]++; s[k]+=$2; if($2>m[k])m[k]=$2} END{for(k in n) printf "k=%s P(HC>4)=%.3f meanHC=%.2f maxHC=%d\n",k,a[k]/n[k],s[k]/n[k],m[k]}'
