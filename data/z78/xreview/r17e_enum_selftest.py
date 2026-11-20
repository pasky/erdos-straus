import sys; sys.path.insert(0,'data/z78/xreview')
import r17e_hits as R
for line in open('data/m17b/p5.txt').read().split('\n')[:3]:
    a,b,c,d=map(int,line.split()); U=17**3
    for p in (1,2,3):
        q=-p*a*pow(b,-1,U)%U
        hs=R.P_hits(17,3,p,q); print((a,b,c,d),p,q,len(hs),[h for h in hs if h[:4]==(a,b,c,d)])
print(R.Q_hits(13,13,2,1))
