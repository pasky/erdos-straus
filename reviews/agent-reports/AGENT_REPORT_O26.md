# AGENT REPORT O26: HC_Π / FT_a corner residuals (branch `side-agent/hcpi-corner`)

Deliverables: `POINTWISE_OMEGA7.md`, `scripts/omega7_residual.py`,
`data/omega7/residual_1e9.txt`, `data/omega7/residual_1e11.txt`.

## Outcome: partial. HC_Π is NOT proved. The residual is moved and sharpened.

HC_Π, HC* and `log W(p) ≥ c(log₂p)^{3/2}` remain **open**. The proved
rate is still O4 Cor 3.1. Nothing is claimed for ES.

## What is new and PROVED

1. **Lemma 1.1 (complementary-divisor class).** For an atom, put
   `j=(a+b)/m` and `m*=(4sa²+1)/m`. Then:
   * `qn′=4saj−m*` and `m*b=aqn′+j`;
   * `a·m*≡κj` and `jm≡(1+κ^{−1})a` (mod q);
   * `mm*≡1 (mod 4a²)`;
   * the atom ↦ `(a,j,m,m*)` map is injective;
   * for `a≤b`, `2/n′≤8aq/(jmm*)≤(4/3)q/(jsa)`.

   So FT's "location of divisors mod 4sa" becomes "divisors of `4a²s+1`
   in the fixed class `κjā` mod q", where q is the fixed modulus.
2. **Lemma 2.0 / 2.5.** Primes of `g_0=gcd(κ+1,q)` divide j. The case
   `gcd(j,q)>1` forces `g=g_0≥y` and is closed. The factor g cancels
   against `Σ_{g|j}1/j`.
3. **Prop 2.3 / Cor 2.4 (elementary).** In any `(s,a)`-box with
   `S≥max(A²,q)H^{2a}`, all atoms (corner or not) with `a≤b`, `m>H^{1/3−a}`
   weigh `≪𝓛²H^{−a}` (`a≤1/6`). Ingredients:
   * an AP count in s, with switching at `√F` (Lemma 2.1);
   * the first-term sum `Σ_{a,j}1/(j·d_0(a,j))`, bounded by the hub
     condition `h_3>H` for small a and by averaging over a for large a
     (Lemma 2.2).

   No corner reduction and no Shiu/Henriot are used. Only `h_3>H` is
   used.
4. **Modulo the Weil–Estermann Kloosterman bound:** Lemma 1.2 (modular
   hyperbola count, error `τ(c)²c^{1/2}log²`), Prop 1.3, Lemma 3.1 and
   Cor 3.2. These cover a-dominant boxes with `S≥𝓛^{10}AqH^a`, with
   `Σ_a τ(4a²)²≪A𝓛^8` absorbing the divisor loss.
   **Correction to my step-1 message:** the range is `S≫A·q·H^a`
   *summed over a*, not `S≫qH^a a^ε`. The file states it correctly.
5. **Thm 3.3.** For O with no saturated H-hub, `4^k≤H≤y`, `a≤1/6`:
   `Σ^{>H^{1/3−a}}≪2^k𝓛⁴H^{−a}` plus the atoms in residual boxes
   `S<H^{2a}𝓛^{10}·max(q,min(A²,Aq))` (with `(S,A)` the box of
   `(s,min(a,b))`).

## Exact residual (open)

* **(R1) short s:** `S<qH^{2a}𝓛^{10}`. For each a, s takes
  `≪H^{2a}𝓛^{10}` values. This contains:
  * O6's (b1);
  * the small-s part of O6's (b2);
  * the numerically heaviest corner configurations (O6's `(341,1)`).
* **(R2) a-dominant:** `A>√q` with
  `qH^{2a}𝓛^{10}≤S<H^{2a}𝓛^{10}min(A²,Aq)`.

Both types occur for every `q∈[y²,T]`. So no family of vertex sets is
closed, and no intermediate rate follows.

*Assessment (obstruction).* Two equidistribution inputs are missing.
* **(R1), `A<q`.** The divisors of `4s(a)a²+1`, with
  `s(a)≡κ(4a²)^{−1} (q)`, must avoid one class mod q on average over a.
  This is a Kloosterman-type family.
* **(R1), `A≥q`, and (R2).** The roots of `4sq²ω²+1≡0 (mod d)` must be
  equidistributed at scale `A/(qd)` for d restricted to one class mod q.
  The discriminant grows with q.

Hooley, DFI 1995 and Tóth average over all moduli for a fixed
polynomial. I know no version uniform in modulus-q progressions. These
citations are from memory and were not checked against the PDFs.

## EVIDENCE

Every atom (14756 at T=10⁹, 271490 at T=10¹¹) passes asserts of
Lemma 1.1, Lemma 2.0 and the weight bound. At these sizes (`q≈T^{0.55}`)
§§2–3 remove only about 15% of the atoms and almost none of the
high-height corner mass. That is honest scope; it proves nothing
asymptotic.

## For the reviewer: check hardest

* Lemma 2.2(2): the hub argument needs `gcd(ad_0r,q)=1`, and that
  `(ad_0,r)` is a valid `h_3` witness.
* Lemma 2.1 / 2.5: the CRT compatibility when `g>1`.
* Lemma 1.2: the bookkeeping of the Ramanujan-sum terms.
* Lemma 3.1: the dyadic `(M_0,M_1)` bookkeeping, and the
  `Σ τ(a²)²≪x(log x)^8` average.
* Thm 3.3: the symmetry `(a,b,κ)↔(b,a,κ^{−1})` preserves `h_3`.

## Suggested ledger line (DISCOVERIES (H)14, not applied by me)

"POINTWISE_OMEGA7: the complementary divisor `m*` lies in the class
`κj/a` mod q. Hence HC_Π(a), `a≤1/6`, holds for all atoms in boxes with
a long s-variable (`S≥max(A²,q)H^{2a}`, elementary), or with
`S≥AqH^a𝓛^{10}` (modulo Weil–Estermann). The residual is short-s /
a-dominant boxes, and needs quadratic-root equidistribution in
progressions mod q. HC_Π remains open."

Stopping here for parent review.
