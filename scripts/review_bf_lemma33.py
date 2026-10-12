"""R159: empirical growth of #{|u|,|v|<=X : A/B integral} for some non-polynomial rational g (Lemma 3.3)."""
import numpy as np
tests = {"(u^2+v^2+1)/(u+2v)": (lambda U,V: U*U+V*V+1, lambda U,V: U+2*V),
         "(u^3+v)/(u^2+v^2+3)": (lambda U,V: U**3+V, lambda U,V: U*U+V*V+3),
         "(uv+1)/(u-v^2)": (lambda U,V: U*V+1, lambda U,V: U-V*V)}
for name,(A,B) in tests.items():
    out = []
    for X in [250, 500, 1000, 2000]:
        r = np.arange(-X, X+1, dtype=np.int64)
        U, V = np.meshgrid(r, r, indexing='ij')
        a, b = A(U,V), B(U,V)
        nz = b != 0
        cnt = int(np.count_nonzero(a[nz] % b[nz] == 0))
        out.append((X, cnt, round(cnt/X, 2)))
    print(name, out)
