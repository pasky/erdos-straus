# ES structural signature (lane `signature`, wave z52b)

Each feature has an id; partial/weakened versions are suffixed (e.g. F04w). Items in signature.jsonl tag matches as `F04` etc.

| id | feature | weakened / partial versions |
|---|---|---|
| F01 | ∀n ∃ witness (universal existence statement over integers) | F01w: ∀ sufficiently large n; F01p: ∀ primes in a residue class |
| F02 | multiplicative closure: solution for n ⇒ solution for every multiple; reduces to primes | F02w: closure under some other operation (n→2n+c etc.) |
| F03 | finite congruence covering (Mordell identities) handles all classes except a few (square classes mod 840) | F03w: covering of all but a density-0 set |
| F04 | expected #witnesses at n is polylogarithmic (≍ log²p for primes, log³ on average) | F04w: count grows but sub-polynomially; F04c: "critical" Poisson-scale count |
| F05 | almost-all result known (exceptional set E(N) ≪ N exp(−c(log N)^{2/3..3/4})) | F05w: positive-density result only |
| F06 | no local obstruction (all p-adic conditions hold) | |
| F07 | no Brauer–Manin obstruction (Bright–Loughran), yet integral Hasse not known | F07w: BM present for strong approximation only |
| F08 | natural parametrised subfamilies (Type I/II, certificate lines) fail exactly at squares via a quadratic-reciprocity obstruction (T1) | F08w: failure on a sparse algebraic set (squares, cubes, n=m²k) |
| F09 | no polynomial identity covers the square classes (Mordell–Schinzel) | F09w: no finite covering of a specific family |
| F10 | witness ⟺ divisor of a p-tied integer (4Cp+1, p+4d, …) in one residue class (−1 mod 4C) tied to the same parameter | F10w: divisor in an interval / in a subgroup coset |
| F11 | numerator-specific: 4 conjecturally always works, 8 fails (17, 131, 241); m/n has genuine exceptions for large m | F11w: a parameter threshold separates true/false |
| F12 | unit-fraction / Egyptian-fraction representation with a fixed number (3) of terms; 2 terms fail, 4 terms trivial | F12w: bounded number of terms |
| F13 | affine cubic surface, integral points, family over n (log K3 / rational surface with conic=hyperbola fibration) | F13w: any affine surface family |
| F14 | S₃ symmetry of the witness (x,y,z) | |
| F15 | fixed-x slice is a split hyperbola (a·y−b)(a·z−b)=c : divisor problem in each fibre | |
| F16 | equivalent "word" form n = tuv − u − v (negative-continuant of length 3) with a coordinate in 4ℤ ∪ (8ℤ−p) | F16w: representation of n by a fixed trilinear/bilinear polynomial |
| F17 | continued-fraction length λ(p) ≤ 3 (five-slice form ES₅) | F17w: bounded CF length / bounded partial quotients |
| F18 | SL₂(ℤ) matrix with a prescribed entry and congruence conditions on other entries | F18w: orbit / group-word reachability |
| F19 | theta-quotient / q-series generating function; ES ⟺ a coefficient-positivity (non-vanishing) statement at every prime | F19w: Eisenstein / divisor-sum generating function |
| F20 | count = sum over moduli of character sums; main term from real characters (genus), BM = one Kronecker character | |
| F21 | pointwise (single integer) lower bound needed; averages over n / modulus / character are known (B2) | |
| F22 | parity / sieve problem flavour: lower bound for thin set counts | |
| F23 | verified computationally to enormous height (10¹⁷–10¹⁸) | |
| F24 | random/Poisson heuristic predicts truth (finitely many or zero failures) | F24w: heuristic predicts infinitely many failures of a sub-statement (e.g. (★) fails at 14 primes ≤ 10¹⁰) |
| F25 | sister statements fail on explicit finite sets (U(n): squares + {105, 2961, 3985, 25305, 111969, 978145}; (★) at 14 primes) | |
| F26 | function-field analogue proved (variants over F_q[T]) | |
| F27 | positivity of variables essential (signed version trivial) | |
| F28 | "Type" dichotomy: p divides exactly one or two denominators | |
| F29 | p ≡ 1 (mod 4) / splitting in ℚ(i) is the hard case (2-adic / Gaussian structure) | |
| F30 | thin infinite families proved (3·2^s+1, 4^s+105, …) but no positive-density rung transfers to primes | |
| F31 | quadratic-form / lattice / quaternion-order reformulations exist | |
| F32 | witness has small size (x ≤ p^{O(1)}, certificate length O(log p)); NP-style certificate | |
| F33 | additive equation with multiplicative (reciprocal) structure — sum-product type | |
| F34 | infinitely many "lines"/families each covering a thin set of primes; union must cover all primes (infinite covering) | |
| F35 | bounded procedures provably fail (B1, conditional on Schinzel H): no finite certificate scheme | |
| F36 | GRH / standard equidistribution conjectures not known to imply it | |
| F37 | count has a Linnik-type upper fluctuation (large R(p) infinitely often) but only one-sided bound can hold | |
| F38 | involution / Vieta-type symmetries act on solution sets (R(p) is even) | |
| F39 | equivalent to a statement about forests/trees/graphs of words (connectivity) | |
| F40 | exceptional-set exponent stuck at a "sieve-architecture" barrier (3/4) | |
