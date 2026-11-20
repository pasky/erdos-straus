"""Independent complete x=5 P-hit enumeration at r=17, levels L=1..7, via (a,H) with aH<=CB/2."""
import sys, time
sys.path.insert(0,'data/z78/xreview')
import r17e_hits as R
for L in range(1,8):
    for p,q in [(1,5),(5,1)]:
        t=time.time(); hs=R.P_hits(17,L,p,q)
        print('L',L,'(p,q)',(p,q),'hits',hs,'secs %.1f'%(time.time()-t),flush=True)
print(R.stats)
