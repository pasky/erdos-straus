# R158 — hostile review of INVOLUTION_ES.md (O158, branch side-agent/involution-depth)

Reviewer branch `side-agent/review-involution`. From-scratch scripts: `scripts/review_inv_*.py`.
ES is not solved here, and the document does not claim it is.

## Verdict table (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 2.1 | SOUND |
| Lemma 2.2 | SOUND |
| Prop 2.3 (parity) | SOUND |
| Prop 2.3(ii) / summary inference | SOUND-AFTER-REPAIRS (wording; see D1) |
| Prop 3.1 | SOUND (scope caveat D2) |
| Lemma 4.1 / Prop 4.2 / Thm 4.4 (mathematics) | SOUND (minor D4, D5) |
| §0/§4 interpretation ("closes the WINDMILL Prop 2 gap", "no cross-slice coupling") | GAP: overclaimed framing (D3, MAJOR) |
| Thm 5.1 | SOUND |
| Lemma 5.2 | SOUND |
| Cor 5.3 | SOUND-AFTER-REPAIRS as a CONDITIONAL sketch (D6); label honest |
| novelty / §6 framing | pending |

## Claim-by-claim

### Lemma 2.1, Lemma 2.2, Prop 2.3

Re-derived. `(tu−1)(tv−1) = t(tuv−u−v)+1` gives the A,B form; X(n) is finite (`A,B ≥ t−1`, `A ≥ 1`).
Lemma 2.2: I redid every step. `A = 4δ ≥ 4` (A = 0 would need `0·B = tn+1`); `t | A+1` gives t odd and
`gcd(t,δ)=1`; `tm²+1 ≡ t+1 (mod 8)` gives `t ≡ 3 (4)`, and `t ≡ 7 (8)` if `8 | A`; so `t ≥ 3` and the Jacobi
symbol `(·/t)` is defined. Primes ℓ | δ₀ divide `tm²+1`, so ℓ ∤ tm and `−t ≡ m⁻² (mod ℓ)`: `(−t/δ₀) = 1`
(multiplicativity covers repeated primes). `(4δ/t) = (−1/t) = −1`, and `(2/t)^s = 1`, so `(δ₀/t) = −1`.
Reciprocity with `(t−1)/2` odd gives `(t/δ₀) = −(−1/δ₀)`, so `(−t/δ₀) = −1`. Contradiction. No coprimality
hypothesis is used. **SOUND.** The E→ES map (CONDITIONAL_ES Lemma 1.1 with (g,f,c)=(t,u,v)) was also checked.

Prop 2.3: the fixed points of ρ are `u(tu−2) = q²`. u = 1 gives t = q²+2; u = q needs `q | q+2`; u = q² needs
`q² | 3`. So exactly one, and |X(q²)| is odd. (iii) holds: for odd n, `gcd(u, n/u) | 2` is odd. **SOUND.**

EVIDENCE (`scripts/review_inv_xsets.py 1200 151`, 22 s, independent enumeration through `A | tn+1`):
* Lemma 2.1 parity and the unitary claim hold for all odd n ≤ 1200.
* Every E(n) element, n ≤ 1200, rebuilds to an exact solution of 4/n.
* E(m²) = ∅ for all odd m ≤ 151. |X(m²)| is odd for 69 of the 75 m, including every odd prime.
* Lemma 5.2: 213 E-elements at p ≡ 1 (8), p ≤ 1200; all have `(δ₀/p) = −1`.

Inference in Prop 2.3(ii) and §0 ("no involution family on X with ES-only fixed points, of any complexity,
exists on a square class"). What is actually excluded is **pointwise**: for each odd prime q, *no* involution
of X(q²) has all its fixed points in E(q²), because the set is odd and E(q²) is empty. "Family" and "any
complexity" add nothing. The statement excludes exactly:
* windmills on X that are required to work at some n = q²;
* by Lemma 1.1, windmills on any sets whose certificates do not exist at odd squares, if they are required
  to work at an odd square with `|X| odd`.

It does **not** exclude windmills on X that are defined only for primes, or only for non-squares. Those are
the only ones ES needs, and §5 handles them. The text after Prop 2.3 says this, so the result is correctly
scoped there. The §0 bullet "T1 kills the O152 odd set" overstates it, though: T1 kills only the extension of
the O152 set to square classes. See D1.

### Prop 3.1 (divisor-type fixed counts)

I recomputed the four pattern expansions in a free model of my own (`scripts/review_inv_prop31.py`, part A).
The rule is that the largest index with `f_i ≠ e_i` decides `d < m²/d`; this is valid as soon as
`q_j > ∏_{i<j} q_i^{e_i}`. My expansions match the table row for row:
P1 `{φ₀,φ₃,φ₋₁,φ₋₂,φ₋₄,ψ}`, P2 `{φ₀,φ₂,φ₋₁,φ₋₂,ψ}`, P3 `{φ₀,φ₁,ψ}`, P4 `{φ₁,φ₂,φ₃,φ₋₄,ψ}`. They sum to `φ₀`, and the
`4c` and `4ψ` terms cancel. The conclusions follow:
* `D(p) = φ(1,h)+c(h)` (p prime: the only pair is (1,p), and there is no square term);
* `D(q²) = φ(1,h)+ψ(q)+c(h)`;
* `ψ(a') = c(h)` for every unit square root a' of h (Dirichlet).

Part B (actual integers): the identity `Σ_i D(m_i²) ≡ φ(1,h)` holds for random tables φ, ψ, c with
(M,a) = (24,5), (120,7), (7,3), (40,3). These are real primes in the prescribed classes with the size
condition, m up to 48 digits, and all divisors enumerated. This also confirms the author's remark that the
classes ā and a² are needed. A GF(2) span search over all patterns of length ≤ 3 with exponents ≤ 3 cannot
reach φ₀ with classes {0,1}, {−1,0,1} or {0,1,2}, but can with {−1,0,1,2}.

The cone extension also checks out. The ratio of a pair is `∏ q_i^{2(e_i−f_i)}`, which is at least
`q_j²/∏_{i<j}q_i^{2e_i}` or at most its inverse. Taking `q_j² > max(λ,μ)^{±1}·q₁·∏_{i<j}q_i^{2e_i}` puts every pair
outside every finite cone, as claimed. Reversed-order contributions fold into the arbitrary φ.

The scope is correct as written: Prop 3.1 is a statement about a formal count D, and it constrains a windmill
only through Lemma 1.1. That requires the windmill to be defined at **every** odd m² of the class, including
the 25–48-digit composite m with prime factors in the classes ā and a². Remark 3.2 is honest: `1+[n=□]` passes.
**SOUND.** The one caveat is the framing (D2).

### Lemma 4.1, Prop 4.2, Lemma 4.3, Thm 4.4, Remark 4.5

**Lemma 4.1.** I went through it step by step.
* (i) If σ(x) = g(x) for a non-symmetry g, then `P(g(x)) = P(x)`, so x ∈ Z₀.
* If g is a degenerate symmetry, then `y = σx` lies in the image `L(P(y))`, so y ∈ Z₁, and `x = σy = g'(y)` lies
  in Z₂.
* Z₁ is proper. Its generic fibre `S_{n₀} ∩ L(n₀)` is proper because S_{n₀} is irreducible and not planar. A
  constructible set with proper generic fibres has proper closure.
* Z₂ is proper: a rational image does not raise dimension.
* (ii) Z = H·(…) is H-invariant (H is a finite group of birational maps, all regular at points of 𝒳 off E),
  so σ(x) = h(x) ∉ Z.

The "symmetries" with ℚ(n)-coefficients are correctly reduced to per-level affine automorphisms of
`S_{n₀}`. Note that "g(n₀) ∈ {id, ρ} for infinitely many n₀" gives `g = id` or `g = ρ` as rational maps.
**SOUND.** Minor (D4): the phrase "invertible symmetries … that can map a point of 𝒳 to a point of 𝒳 outside
Z₃" should say "map some x ∈ 𝒳 ∖ Z₃ into 𝒳".

**Prop 4.2.** The reduction to monomial linear parts is the unique-factorisation argument on the top-degree
part. It is correct for (a)–(c), and for (d) after the polar-divisor step `t' = λt`, which is also correct.
From-scratch check (`scripts/review_inv_sym.py`):
* (a) all 6 permutations, λ = 1, β = 0, for symbolic n.
* (b) a Groebner basis over all 6 permutations with symbolic n, and `λ₁λ₂λ₃n ≠ 0` imposed. It gives exactly
  id and ρ; the other 4 permutations give the ideal (1). Note: `sympy.solve` silently returns no solutions on
  this system, so I used Groebner.
* (c) exactly the scalings `(λa, λb, c/λ², λk)` and the swap, for n-independent maps.
* (d) for **fully general** affine maps in (A,B,t) (12 unknowns, no monomiality assumed), only
  `(αA, B/α, t)` and `(αB, A/α, t)`. The other solutions have `t' = 0` and are not invertible.

I also checked by hand the n-dependent Type II example `(nk,b,c,a/n)`: it preserves F and maps (x,y,z) to
(y,x,z). **SOUND.**

**Lemma 4.3(i)** is re-derived: `s | A`, and `t·s | rA+s ≡ s−r (mod t)`. **Remark 4.5** is re-derived:
`t' ≤ A+1` with `k ≥ 1` forces `k = t = 1`; for `k ≤ −1`, `|k|A ≤ t−1 ≤ A` forces `|k| = 1` and u = 1 (the clause
"or t = 1" is vacuous, since it would force A = 0). Brute force for n ≤ 400 with α = r/s, r,s ≤ 7 and
|k| ≤ 6: 0 violations of Lemma 4.3(i); 4938 unipotent moves found, all on t = 1 or u = 1. **SOUND.**

**Thm 4.4** follows from the above as stated. **SOUND as a mathematical statement.**

**Does "generic" hide the whole problem?** For the existence question, yes, and this is the main defect of
the document (D3). Z is an arbitrary proper algebraic set that depends on the menu, and the theorem says
nothing about what σ does on Z. A windmill may live entirely on Z. Thm 5.1 makes this explicit: the
conclusion is `E(p) ∩ Z ≠ ∅`, which is not a contradiction. The empirical picture shows that ES certificates
sit on a few low planes:

EVIDENCE (`scripts/review_inv_planes.py 40000`, 69 s). For **every** prime `p ≡ 1 (24)` with p ≤ 40000 (501
primes), E(p) meets the 33 planes `{t=c} ∪ {u=c} ∪ {v=c}`, c ≤ 11. The worst case is c = 11 at p = 12289.
CONDITIONAL_ES already records t ≤ 367 for all 4519 Mordell-hard primes below 2·10⁶.

So the "exceptional" set of a finite-menu windmill can contain the entire empirically used part of E(p).
§4 therefore does not show that finite-menu windmills fail. It shows that they reduce to a **bounded-slice
statement** "E(p) ∩ Z ≠ ∅ ∀p", and for coordinate planes the only known refutation of that statement is
conditional (Cor 5.3, Dickson). Unconditionally, §4–§5 exclude **no** windmill defined on primes.

### Thm 5.1, Lemma 5.2, Cor 5.3

**Thm 5.1.** Re-derived. On G(p), τ is pointwise id or ρ, and G(p) is τ- and ρ-invariant (Z is H-invariant).
If `(p+2,1,1)` were in G(p), both id and ρ would fix it, which is impossible because it is not in E(p)
(`A = p+1 ≡ 2 (4)`). So it lies in Z. It is the unique ρ-fixed point of X(p), so ρ is free on G(p), and
`|Fix τ ∩ G(p)| ≡ |G(p)| ≡ 0`, while `|Fix τ| ≡ |X(p)| ≡ 1`. **SOUND.** A side remark worth adding: the
conclusion forces the line `{u = v = 1}` into Z for every such menu.

**Lemma 5.2.** Re-derived. `tp+1 ≡ t+1 (8)` gives `t ≡ 3 (4)`; primes of δ₀ divide `tp+1`, so `(−tp/δ₀) = 1`,
and the Lemma 2.2 computation gives `(−t/δ₀) = −1`. Hence `(δ₀/p) = (p/δ₀) = −1`. Checked numerically: 213
elements, 0 violations. **SOUND.**

**Cor 5.3 (CONDITIONAL, sketch).** I redid the branch bookkeeping. The mechanism works, but one step of the
sketch is wrong as written (D6). Take `p = Mq+1`, with M divisible by high powers of all relevant small
integers.
* `{t=c}`: A divides `cp+1 = (c+1)·r`, where `r = (cM/(c+1))q + 1`.
* `{u=c}`: A divides `p+c = (c+1)·r'`, where `r' = (M/(c+1))q + 1`.
* `{v=c}`: `B | p+c`, so B = d or B = d·r' with `d | c+1`. I checked that **both** branches give A linear in q:
  `cd·A = (d+1)p + c` for B = d, and `cd·A = dp + c + 1` for B = d·r'. In the second branch use
  `p = (c+1)r' − c`; then `(dr'+1)p + c = r'(dp+c+1)`.

So every candidate A is a fixed integer times one value of a linear form `α_i q + 1`. The fixed integers are
c+1, c+d+1, …, whose primes divide M and are therefore residues mod p, and 2 is a residue since p ≡ 1 (8).

The sketch then says "with q in a class making every such prime ≡ 1 modulo 4·(all constants)". That cannot
be done by choosing q when the modulus divides α_i, because the residue of `α_i q + 1` is then fixed.
Correct version: take M so large that `L := 8·∏(c's, d+1's)` divides every α_i. Then each prime is
automatically ≡ 1 (mod L), and its quadratic character at p is
`(−c/r) = 1`, `(−c(d+1)/s) = 1`, `(−d(c+1)/s) = 1`, as required.

Dickson admissibility also holds. All forms are `α_i q + 1`; for ℓ ≤ #forms, ℓ | α_i gives the value 1
(mod ℓ); for larger ℓ, at most #forms classes are excluded. With this repair the sketch is a correct
CONDITIONAL proof. The label "CONDITIONAL; sketch; needs review" is honest. Note that the corollary is
conditional, so §4–§5 give **no unconditional exclusion** of any primes-only windmill (D3).
