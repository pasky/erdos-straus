# Z2847 (corrected): level-t monoid transport n3 = t n1 n2 + n1 + n2 with n3 <= 600, words computed on demand.
import sys, functools
sys.path.insert(0,'scripts')
import importlib.util
src=open('scripts/z52d_p2_TO7_words.py').read().split('primes=[p')[0]   # definitions only (no run())
ns={}; exec(src, ns)
words, leg = ns['words'], ns['leg']
@functools.lru_cache(None)
def W(n,t): return tuple(w for w in words(n) if w[0]==t)
for t in [2,3,4]:
    tot=0; n3ex=0; sgn_tot=0; sgn_ok=0; base=0
    for n1 in range(2,60):
        if not W(n1,t): continue
        for n2 in range(n1,60):
            if not W(n2,t): continue
            n3=t*n1*n2+n1+n2
            if n3>600: continue
            base+=1
            if W(n3,t): n3ex+=1
            if n3%2 and W(n3,t) and n1%2 and W(n1,t) and W(n2,t) and n2%2==0 or (n3%2 and W(n3,t) and n2%2 and W(n1,t) and n1%2==0):
                sgn_tot+=1
                s1={leg(u*v,n1) for (_,u,v) in W(n1,t)}; s2={leg(u*v,n2) for (_,u,v) in W(n2,t)}; s3={leg(u*v,n3) for (_,u,v) in W(n3,t)}
                if any(a*b in s3 for a in s1 for b in s2): sgn_ok+=1
    print(f"t={t}: pairs with words at n1,n2 and n3<=600: {base}; of these n3 has a level-t word: {n3ex}; odd sign-tested {sgn_tot}, sign product realised {sgn_ok}", flush=True)
