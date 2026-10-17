# Literature note: the Type II `b=1` slice

## Answer

**Yes: the family is known and characterized in the literature, although I found no paper naming it “Type II with b=1.”** The direct reference is Miguel Ángel López, *Structure and form of the solutions of the Erdős-Straus conjecture*, arXiv:2206.10319 (2022; v4, 2024), Theorem in §2(c): for prime `p=4k+1`, a solution `(du,dv,duv)` exists iff some `t≥0` and divisor `w | k+1+t` satisfy `w ≡ −1 (mod 3+4t)`. That denominator shape is exactly the user's `b=1` ET slice up to permutation: `(ad, acdp, cdp)` permutes to `(ad, cdp, acdp)=(du,dv,duv)` with `u=a, v=cp`. López (2024), *A Complete Congruence System...*, explicitly remarks that Type A solutions of this `(du,dv,duv)` form arise in ET coordinates when `a=1` or `b=1`. See `Lopez-2022.md` and `Lopez-2024.md`.

Thus the divisor characterization is known, and the equivalence to the b=1 line is a straightforward parameter identification (the latter phrasing is my inference from the cited formulas). The user’s divisor condition involving `p+4d` is also an equivalent rewriting of this characterization, not a separate result discovered here.

## Exceptions / computation

**The precise claimed exception set `{193, 2521, 66529}` and verification through `10^8` were not found as a published theorem or reported exhaustive computation in the sources searched.** López 2022 reports that among primes through 4369, the only failures of `(du,dv,duv)` are 193 and 2521. López 2024 reports 193 and 2521 among the first 9000 naturals as lacking Type A, and says 66529 is another Type A failure. That paper's reported larger computation checks the broader Type A-or-Type B conjecture through prime 104729, not the b=1/Type A family alone. It does not give the asserted complete b=1 exception list.

The three numbers are therefore familiar as difficult cases in structural classifications, but **the exact three-exception phenomenon for this slice is not established by the references above**. No contradiction: Type A/b=1 failures still have other Erdős–Straus solutions; López explicitly describes Type B solutions for these numbers. Salez's check through `10^17` concerns the full conjecture, and gives no b=1 exception list.

## Closest results

- Elsholtz–Tao (2013), *Counting the number of solutions...*, §2 / Type II parametrization: general Type II parameter equation and denominators `(abd, acdp, bcdp)`; not a separately isolated b=1 conjecture. See `Elsholtz-Tao-2013.md`.
- López (2022), Theorem §2(c): exact divisor test for the b=1/Type A shape, with initial failures 193 and 2521.
- López (2024), §§2 and 3: explicitly identifies ET parameters `a=1` or `b=1` with Type A; identifies 66529 as another Type A failure; conjectures Type A-or-Type B covers primes and reports its combined computation through 104729. This is the closest literature treatment of the 3-number story, but not the same conjecture.
- Salez (2014), arXiv:1406.6307, Proposition 3 and comparison section: seven “modular equations,” with four attributed to/ equivalent to Rosati (1954) and Yamamoto (1965), and a full-conjecture sieve check through `10^17`. They are not the b=1 restriction of the ET family. See `Salez-2014.md`.
- Ionașcu–Wilson (2011) discusses Mordell-style congruence exceptions and Terzi's residue sieve; these concern possible failures of the full equation, not failures of the b=1 family. See `Ionascu-Wilson-2011.md`.

## Scope / confidence

Research used the required Jina web-search and webpage-reading skills; the key arXiv papers and Ionașcu–Wilson paper were read directly. Searches included denominator-divisibility phrasing, ET/Type II and the three integers, Salez, Mordell/Rosati/Yamamoto, Sander, Guy, and OEIS. OEIS search did not turn up a relevant sequence. I found no direct `z|y` / “x divides y” treatment beyond the equivalent `(du,dv,duv)` characterization, and no matching literature for the exact three-exception statement. These are search findings, not a proof that no obscure or unpublished report exists. The newly written source files contain citations, URLs and short verified excerpts; deductions are labeled as inference.
