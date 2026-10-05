"""R46: recompute POINTWISE_HAAR §3 table from POINTWISE_SIZE §7.2 values (from scratch)."""
import numpy as np
T=np.array([127,511,1023,2047,4095,8191,16383,32767,65535.])
Phi=np.array([5.47,9.40,12.02,15.11,18.77,23.08,27.99,33.4,38.5])
I=np.array([6.17,11.46,15.01,19.19,24.11,29.80,36.35,43.81,52.24])
L=np.log(T); f=L**3/np.log(L)
for i in range(len(T)):
    le = (np.log(Phi[i+1])-np.log(Phi[i-1]))/(np.log(L[i+1])-np.log(L[i-1])) if 0<i<len(T)-1 else float('nan')
    print(f"{T[i]:6.0f} L={L[i]:.2f} Phi/f={Phi[i]/f[i]:.4f} I/f={I[i]/f[i]:.4f} locexp(central)={le:.2f} 3-1/logL={3-1/np.log(L[i]):.2f}")
x=np.log(L); y=np.log(Phi)
for name,yy in [("c L^a",y),("c L^a/logL",y+np.log(np.log(L)))]:
    a,b=np.polyfit(x,yy,1); r=np.max(np.abs(yy-(a*x+b))); print(name,"a=%.3f maxres=%.3f"%(a,r))
# alternative shapes: c L^2 log L, c L^3/logL ... fit ratio constancy over 1023..32767
for name,g in [("L^3/logL",L**3/np.log(L)),("L^2.5",L**2.5),("L^2 logL",L**2*np.log(L)),("L^2.4",L**2.4)]:
    s=slice(2,8); rr=Phi[s]/g[s]; print(name,"ratio spread 1023..32767: %.2f%%"%(100*(rr.max()/rr.min()-1)))
