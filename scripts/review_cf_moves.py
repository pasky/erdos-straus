"""R198 from-scratch: scaling and rotation laws (CHI_FLIP Cor 1.4(b), Prop 1.5), in both normalisations.
chi(w) = (-A/n) (uniform), dk(w) = (A/n) (DEDEKIND 8.x normalisation). Jacobi via sympy (independent of cf_lib)."""
from sympy import jacobi_symbol as J
L = 60
K = lambda t, u, v: t * u * v - u - v
# --- scaling: word (a t, u, v) of m  ->  (t, a u, a v) of a m  (DK 8.3 written in (t,u,v) order)
sc = scf = scdk = 0
for a in range(3, 16, 2):
    for t in range(1, 25):
        for u in range(1, 25):
            for v in range(1, 25):
                m = K(a * t, u, v)
                if m < 1 or m % 2 == 0:
                    continue
                n = K(t, a * u, a * v); assert n == a * m
                A = a * t * u - 1; assert A == t * (a * u) - 1
                sc += 1
                scf += J(-A, m) != J(-A, n)
                scdk += (J(A, m) != J(A, n)) != (a % 4 == 3)
print(f"scaling: {sc} cases, chi changes {scf}, (A/n)-flip != [a=3 mod 4]: {scdk}")
# --- rotation (t,u,v) -> (u,v,t)
rot = bad = 0; dkflip_notall_odd = 0; ex = None; cells = set()
for t in range(1, L):
    for u in range(1, L):
        for v in range(1, L):
            n, n2 = K(t, u, v), K(u, v, t)
            if n < 1 or n2 < 1 or n % 2 == 0 or n2 % 2 == 0:
                continue
            rot += 1; cells.add((t % 8, u % 8, v % 8))
            A, A2 = t * u - 1, u * v - 1
            flip = J(-A, n) != J(-A2, n2)
            law = (t % 2 == u % 2 == v % 2 == 1) and (t - u) % 4 != 0
            bad += flip != law
            dkf = J(A, n) != J(A2, n2)
            if dkf and not (t % 2 and u % 2 and v % 2):
                dkflip_notall_odd += 1
                if ex is None or n % 4 == 1 and ex[3] % 4 != 1:
                    ex = (t, u, v, n, n2, J(A, n), J(A2, n2))
print(f"rotation: {rot} positive odd->odd cases on {len(cells)} cells mod 8, law violations {bad}")
print(f"(A/n)-normalisation: rotations flipping (A/n) with NOT all letters odd: {dkflip_notall_odd}, e.g. {ex}")
