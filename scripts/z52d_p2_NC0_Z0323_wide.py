import sys; sys.argv=['x','1']
sys.path.insert(0,'scripts')
import importlib.util
spec=importlib.util.spec_from_file_location('z323','scripts/z52d_p2_NC0_Z0323.py')
import bs_ff_es as E
E.Q=5
import time
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
E.Q=5
for P,deg in [((2,2,1,0,1),3),((2,2,1,0,1),4)]:
    t=time.time(); s=m.four_term(P,deg); print(P,'deg<=',deg,'4-term witness:',s, f'{time.time()-t:.1f}s', flush=True)
