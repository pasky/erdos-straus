"""Check slope, permutation and exact remainder in the normalized (1,y√n) basis."""

def check(n, x, y, s):
    M = n**s
    assert x*x + 1 == n*y*y and y != 0
    D = n*y*y
    # Coefficients of ε⁴ in this basis, separately from the output Y_m.
    v, w = (x*x+D)**2 + D*(2*x)**2, 4*x*(x*x+D)
    a, b = x % M, 1
    values = []
    for j in range(M):
        values.append(b)
        a, b = (v*a+D*w*b) % M, (w*a+v*b) % M
    assert (a,b)==(x%M,1)
    assert len(set(values)) == M
    for k in range(s):
        h=n**k
        for j,val in enumerate(values):
            assert (values[(j+h)%M]-val-4*h) % (n*h)==0
    # Full integer witnesses (not just residues), including non-coprime anchors.
    a, b = x, 1
    for j in range(17):
        assert a*a-n*(y*b)**2==-1
        u,r=divmod((y*b)%(abs(y)*M),abs(y))
        assert r==0 and u==(1 if y>0 else -1)*values[j%M]%M
        a,b=v*a+D*w*b,w*a+v*b
    return M


if __name__ == '__main__':
    anchors=[(5,2,1,4),(5,682,305,3),(25*5,682,61,2),(65,8,1,2),(5,-682,-305,3)]
    print(sum(check(*row) for row in anchors),'entries checked')
