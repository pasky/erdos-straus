# z57 BFII: check the target-set form against the enumerator.
#   f_II-count(p) = #{(f,a,c,d): f = 4acd-1, f | c p + a}
#                 = sum_{f = 3 (4)} #{(a,c): ac | m_f, (-p mod f)*c == a (mod f)},  m_f = (f+1)/4
# and the c=1 part equals the (★) count.  Also the d=1 form: #{b : p + 4b^2 has divisor == -1 mod 4b} etc.
import sys, numpy as np
def load(path):
    with open(path,'rb') as f:
        X=int(np.frombuffer(f.read(8),dtype=np.int64)[0])
        arr=np.frombuffer(f.read(),dtype=np.uint32).reshape(5,X+1)
    return X,arr
X,A=load(sys.argv[1]); tot,c1=A[0],A[1]
def divisors(m):
    ds=[]; i=1
    while i*i<=m:
        if m%i==0:
            ds.append(i)
            if i*i!=m: ds.append(m//i)
        i+=1
    return ds
def fcount(p):
    t=0; t1=0
    for f in range(3,4*p,4):
        m=(f+1)//4; r=(-p)%f
        for c in divisors(m):
            mc=m//c
            for a in divisors(mc):   # a | m/c  <=> ac | m ; d = m/(ac)
                if (r*c-a)%f==0 and (c*p+a)//f>=a:   # restrict to a <= b (then f < 4p, ET Lemma 2.8)
                    t+=1
                    if c==1: t1+=1
    return t,t1
def direct_ab(p):
    # #(a,b,d,e) with a<=b, e | a+b, 4abd - e = p ; and c=1 part
    t=0;t1=0;a=1
    while 4*a*a-2*a<=p:
        b=a
        while 4*a*b-(a+b)<=p:
            s=a+b; d=1
            while 4*a*b*d-s<=p:
                e=4*a*b*d-p
                if 1<=e<=s and s%e==0:
                    t+=1
                    if e==s: t1+=1
                d+=1
            b+=1
        a+=1
    return t,t1
ps=[int(x) for x in sys.argv[2:]]
for p in ps:
    t,t1=fcount(p)
    u,u1=direct_ab(p)
    print(p,"f-form(a<=b)",t,t1,"direct(a<=b)",u,u1,"enum(all ordered)",int(tot[p]),int(c1[p]),"OK" if (t,t1)==(u,u1) else "MISMATCH")
