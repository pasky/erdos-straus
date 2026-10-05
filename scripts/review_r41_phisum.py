"""R41: check sum_{a<=Z, a=3(4)} phi(a) ~ Z^2/pi^2 and the optimisation constant."""
import math
Z=10**6
phi=list(range(Z+1))
for q in range(2,Z+1):
    if phi[q]==q:
        for m in range(q,Z+1,q): phi[m]-=phi[m]//q
for z in (10**4,10**5,10**6):
    s=sum(phi[a] for a in range(3,z+1,4)); print(z, s/(z*z/math.pi**2))
k=math.log(2)/(4*math.pi**2); Zs=1/(8*2*k); print("Z*/L",Zs, "value", -(Zs/8)+k*Zs**2, -math.pi**2/(64*math.log(2)))
