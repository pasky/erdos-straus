# z17_window — localised counting cannot shrink the sibling window (O242)

## Idea
Feed SD Lemma 3.1 with counts *inside a cylinder V* (depth n) instead of global counts (R248 D3: counts could in principle
suffice). Localisation adds T^n to class-divisor moduli and fixes g' mod T^{n−1} in the Bezout form.

## Literature
SP Lemma 1.6 routes, SS Lemma 4.1 / Cor 4.2 (exponent 2/5 at (1/5,1/5,1/5,2/5)), TC Prop 2.1.

## Barrier screen
B3 in localised form: at the ET point every route has ≍ 3^{2s/5} fixed data, independent of V; relative mass in V is
3^{2s/5 + n − s/2}, < 1 only for s > 10n — the same threshold as the global bound (SIBLING Prop 3.1).

## Cheap numerics
Certified bound terms of SS §5.3 decay ≈ 3^{−0.12 s}: a depth-n cylinder needs complete control to depth ≈ 40 + 4.5n.

## Assessment
PROVED for an explicit route list (R249 repair D1: the localised route R2L — fix m′, then g′w₁ mod T^{n−1} — beats 3^{2s/5}
for n > 2s/5, though its relative mass stays > 1; "counts do not localise" in general is Assessment). The window (n, 5n] inside any cylinder needs positional input; counts do not localise.
