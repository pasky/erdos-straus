import sys, math
N=int(sys.argv[1])
fails=[]
for n in range(5,N+1,4):
    c = 7 if n%8==1 else 3
    ok=False
    for u in range(1,n+3):
        # v such that uv | n+u+v ; brute over divisors A of n+u with A ≡ -1 mod u
        m=n+u
        for A in range(1,int(math.isqrt(m))+1):
            for AA in {A, m//A} if m%A==0 else ():
                if (AA+1)%u==0:
                    v=m//AA
                    if u%4==0 or v%4==0 or u%8==c or v%8==c: ok=True;break
            if ok:break
        if ok:break
    if not ok: fails.append(n)
print(fails)
