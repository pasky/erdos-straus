def e2(p):
    for d in range(1,(p+3)//8+2):
        N=p+4*d; m=4*d
        w=m-1
        while w<N:
            if N%w==0: return (d,w)
            w+=m
    return None
for p in [193,2521,66529,197,1201]:
    print(p,e2(p))
