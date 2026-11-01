# Z2658 round 3b: within-prime comparison of normalised d-invariant sums S(p,A)/p^2 for QR vs QNR A
# among length-3 A (HJ length 3). Reuses the recursion of z52d_p2_NC2_Z2658_r3.py.
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path
import json
from scipy.stats import binomtest
def primes(N):
 s=bytearray(b'\x01')*(N+1); s[:2]=b'\0\0'
 for i in range(2,isqrt(N)+1):
  if s[i]: s[i*i:N+1:i]=b'\0'*(((N-i*i)//i)+1)
 return [i for i,x in enumerate(s) if x]
def hj(n,a):
 out=[]
 while a:
  b=(n+a-1)//a; out.append(b); n,a=a,b*a-n
 return out
@lru_cache(None)
def d(p,q,i):
 if q==1: return Fraction((2*i-p)**2-p,4*p)
 return Fraction((2*i+1-p-q)**2-p*q,4*p*q)-d(q,p%q,i%q)
diffs=[]; qr_all=[]; qnr_all=[]
for p in primes(1999):
 if p%4!=1 or p<5: continue
 qr=[]; qnr=[]
 for a in range(1,p):
  if gcd(a,p)>1 or len(hj(p,a))!=3: continue
  S=float(sum((d(p,a,i) for i in range(p)),Fraction(0)))/(p*p)
  (qr if pow(a,(p-1)//2,p)==1 else qnr).append(S)
 if qr and qnr:
  mq=sum(qr)/len(qr); mn=sum(qnr)/len(qnr); diffs.append((p,mq-mn))
  qr_all+=qr; qnr_all+=qnr
pos=sum(1 for _,x in diffs if x>0); neg=sum(1 for _,x in diffs if x<0)
out={'primes_with_both_classes':len(diffs),'mean_S_over_p2_QR':sum(qr_all)/len(qr_all),'mean_S_over_p2_QNR':sum(qnr_all)/len(qnr_all),
 'primes_QR_greater':pos,'primes_QNR_greater':neg,'sign_test_p':binomtest(pos,pos+neg).pvalue,
 'mean_per_prime_diff':sum(x for _,x in diffs)/len(diffs),'largest_p':max(p for p,_ in diffs),
 'diff_first_10':[(p,round(x,4)) for p,x in diffs[:10]],'definition':'S(p,A)=sum_i d(L(p,A),i) divided by p^2; A runs over length-3 residues with gcd(A,p)=1; compared within each prime p=1 mod 4 with 5<=p<2000'}
d_=Path('data/z52b/pass2/NC2/Z2658'); d_.mkdir(parents=True,exist_ok=True)
(d_/'norm.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n'); print(json.dumps(out,ensure_ascii=False))
