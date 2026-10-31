"""RESIDUE_HARDNESS §1.1: cross-check of the tuple engine (z52c_rh_types.c, /tmp/rh/t1e6_*) against the solution counter
(z52c_rh_count.c mode 2, output data/z52c/rh/U_counter_2e5_1e6.txt.gz): TI = 2k1, TII = 2k2, U = k1 + k2 at every prime."""
import numpy as np
lo=200001
TI=np.fromfile('/tmp/rh/t1e6_TI.f32',np.float32); TII=np.fromfile('/tmp/rh/t1e6_TII.f32',np.float32)
rows=[]
for f in ['data/z52c/rh/U_counter_2e5_1e6.txt.gz']:
    try: A=np.loadtxt(f,dtype=np.int64,ndmin=2)
    except Exception: continue
    if A.size: rows.append(A)
A=np.vstack(rows); P=A[:,0]
ok=(TI[P-lo]==2*A[:,10])&(TII[P-lo]==2*A[:,11])&(A[:,1]==A[:,10]+A[:,11])
print(len(P),'agree',ok.sum())
