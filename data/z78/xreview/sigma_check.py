# sigma(f)(T)=(-1)^deg f * f(-T): check it permutes the s<=17 tuple census and swaps depth at c=1 <-> c=2
import re
def P(s): return tuple(int(ch) for ch in s)
def sig(f):
    d=len(f)-1; return tuple(((-1)**d*((-1)**i)*x)%3 for i,x in enumerate(f))
T={}
for line in open('census_s4_17.txt'):
    kv=dict(re.findall(r'(\w+)=(\S+)',line))
    key=(int(kv['n']),P(kv['m']),P(kv['w']),P(kv['C']))
    T.setdefault(key,{})[int(kv['c'])]=int(kv['depE'])
bad=0
for (n,m,w,C),dep in T.items():
    k2=(n,sig(m),sig(w),sig(C))
    if k2 not in T or T[k2][2]!=dep[1] or T[k2][1]!=dep[2]: bad+=1
print('tuples',len(T),'sigma failures',bad)
