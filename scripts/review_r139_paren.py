# R139: numeric check of the parenthetical in 17D Remark 2.4 (X*N = ab(p^2 f* + q^2 f - 2pq), f | 4c^2dp^2+17x^2)
import sys, random; sys.path.insert(0,'scripts')
exec(open('scripts/review_r139_lemmas.py').read().split("fails = 0")[0])
bad=0; tot=0
for K in (3,5):
    N=17**K; W=17**((K+1)//2)
    for (a,b,c,d,e) in Pdata(K):
        if b%17==0: continue
        for _ in range(5):
            q=random.randint(1,1000); p=(q*a*pow(b,-1,W))%W+random.randint(-9,9)*W; z=(q*a-p*b)//W
            X=c*(p*p*b+q*q*a)+17*z*z; f=4*a*c*d-1; fs=4*b*c*d-1
            tot+=1
            if X*N != a*b*(p*p*fs+q*q*f-2*p*q): bad+=1
            if (q*f-p)%W: bad+=1; continue
            x=(q*f-p)//W
            if (4*c*c*d*p*p+17*x*x)%f: bad+=1
print(tot,bad)
