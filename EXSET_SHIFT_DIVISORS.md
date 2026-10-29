# EXSET_SHIFT_DIVISORS — divisor classes across shifts and the U exceptional set (wave z50, lane D, `shifts`)

Status: **rounds 1–3 complete; two Astra hostile reviews folded in (§7)**. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. ES is OPEN; nothing here proves or disproves it.

Notation. n ≡ 1 (mod 4); 𝒞_n = 4ℤ ∪ (8ℤ − n), positive part. For v ≥ 3 put
hit_v(m) = 1[∃ d | m, d ≡ −1 (mod v)], fail_v = 1 − hit_v. U(n) holds iff hit_v(n+v) = 1 for some v ∈ 𝒞_n
(z49 CONTEXT §1; scripts/z49_main_ucensus.c). E_U(N) = #{n ≤ N, n ≡ 1 (4) : U(n) fails}.
Convention: the divisor d = n + v (cofactor 1) is allowed, as in the z49 census code; it matters only when v | n + 1,
and nothing below depends on it. L₂ = log log x. Q(β) = β log β − β + 1 (the Hardy–Ramanujan/Sathe–Selberg rate
function). G_v = (ℤ/vℤ)^×. For m ≥ 1, m′ = largest divisor of m coprime to v, S_v(m) = the multiset of residues
mod v of the prime factors of m′ (with multiplicity), Σ*(S) = the set of subproducts of S (empty product 1 included).
Since a divisor ≡ −1 (mod v) is coprime to v: hit_v(m) = 1 ⟺ −1 ∈ Σ*(S_v(m)).

## 0. Summary table

| # | statement | label |
|---|---|---|
| 1 | audit: n ≡ 5 (8) is trivial; U is a mass-L² family; the 3/4 note does not transfer; lane E proved E_U ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}) and the matching CRT cap | PROVED (1.1, inclusion; lane E on main) |
| 2 | single-shift law (unrestricted m): fixed v ∈ 𝒞: P(fail_v) ~ C_v (log x)^{−1/2} (Thm 2.2); P(hit_v) ≪ (log x)^{−Q(β)} for φ(v) = (log x)^{β log 2}, 1<β<2 (Thm 2.3); cost(v) ≤ log log x + O(1) (Prop 2.4) | PROVED; sharp costly side Conj 2.6 |
| 3 | independence across shifts: model Thm 3.1 / Cor 3.2 (NA given the full small-prime-power fibre; in the model, chains lose only through fibre reweighting); integers: joint ≫ product, consistent with a quadratic-profile drift (EVIDENCE); known correlation theorems treat a fixed number of shifts; (D)21 Prop 4.3 confirmed within its CRT scope; χ-polynomial majorants reduce to it for CRT means (both lines) | PROVED (model; CRT-mean reduction) / EVIDENCE / Assessment |
| 4 | assembly: no new exponent (record: lane E's 2/3); fixed-k shifts give only (log N)^{−A}; the sieve implementation stops near θ ≈ 0.41 (Ass. 4.2); the brief's |𝒱| ≍ log N/log log N costly events do not exist | PROVED (V/W) / Assessment |
| 5 | barrier for product-form bounds over whole coordinate events with unconditional marginals: only (log N)^{log 2+o(1)} events cost a factor ≥ C (Thm 5.1), so formulas paying a loss ≥ C > 1 per event give θ ≤ log 2 = 0.693 (Cor 5.2); a uniform loss 1+ε needs ε ≤ (log N)^{−0.0037}, ≥ (log N)^{0.75−o(1)} events and coordinates reaching (log N)^{0.754} for θ = 3/4 (Thm 5.3); chains and refinements NOT covered | PROVED for V/W; CONDITIONAL for T |
| 6 | numerics: single-shift law at x ≤ 10³²; exact joint census n ≤ 10⁸, v ≤ 128: joint failure within 1.1× of the square floor from V = 63; non-square joint exceeds the product by e^{5.6}, about two thirds of it removed by conditioning on a 9-prime quadratic profile; chain ratios fall below the non-square marginals at 45 of 48 steps | EVIDENCE / CERTIFIED (exact counts) |
| 7 | Astra R1: MAJOR repairs, no FATAL; R2: substantial repair accepted, local repairs listed and applied in round 3 (§7) | — |

## 1. Audit: what is known for U, and which barrier applies

**1.1 The class n ≡ 5 (mod 8) is trivial (PROVED).** If n ≡ 5 (mod 8) then 3 ∈ 𝒞_n and A = 2 ≡ −1 (mod 3) divides
n + 3, with 1 < 2 < n + 3. So U(n) holds (word t = 1, v = 3, u = (n+3)/2). Likewise for n ≡ 1 (mod 8) with
n ≡ 2 (mod 3): A = 6 ≡ −1 (mod 7) divides n + 7. Hence E_U(N) counts only n ≡ 1 (mod 8), n ≢ 2 (mod 3).
This is consistent with the census: all six non-square failures ≤ 10⁹ (105, 2961, 3985, 25305, 111969, 978145) are
≡ 1 (mod 8), and so are all odd squares. CERTIFIED as a check (`data/z50_shifts/joint_N1e8.txt`): for n ≡ 5 (mod 8),
n ≤ 10⁸, the marginal failure rate at v = 3 is exactly 0. *From here on n ≡ 1 (mod 8)*, so 𝒞_n = 4ℤ ∪ (8ℤ + 7).

**1.2 U is a mass-L² family; the CRT exponent for U is 2/3 (lane E, PROVED on main); the 3/4 note does not
transfer.**
* A U-certificate at the endpoint v is the class n ≡ −v (mod A), A ≡ −1 (mod v); for odd v, n ≡ −v (mod 8) as well.
  For v = 4k these are the classes −4k (mod A) with k | (A+1)/4, i.e. the D | (A+1)/4 part of
  ℛ(A) = {−4D : D | ((A+1)/4)²}. So the 4ℤ-line of U is a subfamily of the ES forced classes ℛ(M) (PROVED).
* Mass. With the modulus cutoff A ≤ X, the endpoint-class mass is Θ(log² X): the lower bound comes from
  Σ_{A≡3(4)} τ((A+1)/4)/A, the upper bound for both lines from Σ_{A≤X} τ(A+1)/A. This is a first-moment statement,
  not a survival law. The 3/4 note's extra factor log K comes from the third divisor slot of its Vaughan *ratio*
  classes −u/v (mod kℓ), (kℓ+1)/4 = uvw. Their integer labels D = u²w need not divide (kℓ+1)/4. (Residue labels can
  collide: M = 15, (u,v,w) = (4,1,1) gives −4·16 ≡ −4 (mod 15), an endpoint-4 U class. So "u | v" is a sufficient
  criterion for a note atom to be a U class, not an iff. The repair is due to the Astra review.) Forced ℛ(M) hits do
  occur at known U failures: n = 105 lies in −4·9 (mod 47), n = 2961 in −4·36 (mod 23), n = 3985 in −4·25 (mod 19).
  So ES certifies these n through ratio classes that U does not have.
* **Lane E (EXSET_I3.md §7, merged to main; Opus review SOUND)** settles the CRT side for U.
  - Cor 7.1 (PROVED relative to the KARY inputs): for the native U/ES₅ class universe on n ≡ 1 (4), t = 1, 2
    included, every nonnegative CRT majorant of level λ saves ≪ λ^{2/3}/(log λ)^{1/3}.
  - §7.3 (PROVED relative to BV, Brun–Titchmarsh, Mertens):
    E_ES₅(N) ≤ E_U(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}), optimal for the native presentation.
  This supersedes my round-1 Assessment "2/3 expected for U, not proved". It also closes my round-1 gap that the
  odd line was not covered by any cap: Cor 7.1 covers both lines.
  The Astra review pointed out a weaker standard bound for U that round 1 had missed. A prime-local Bonferroni sieve
  uses the classes −4d mod primes ℓ ≡ 3 (4), d | (ℓ+1)/4 (mass ≍ log z), and gives E_U(N) ≪ N exp(−c√log N). This is
  z50 CONTEXT §4(a)'s θ = 1/2 and is now superseded by lane E.
* So for U, Target 3 (θ > 3/4) lies beyond the proved and optimal CRT exponent 2/3 for the native presentation.
  Any θ > 2/3 for U needs a non-CRT door (z50 CONTEXT §3 doors (i) or (vii)), or a non-native presentation (lane E's
  open door: endpoint pairs with non-reduced moduli).

**1.3 Which door this lane uses.** "Joint failure over many shifts" via anatomy and correlations is non-CRT
interval information (door (i)) or a non-linear conditioning argument (door (vii)): the events fail_v(n+v) are
statements about the full factorisation of n + v ≤ 2N, not about its small-prime part. §5 proves budgets that do
not assume CRT evaluation. They constrain only bounds of one precise shape: a product over whole coordinate events,
each used once, of factors min{1, C_e π_e} with π_e ≥ the *unconditional* marginal, plus a remainder R ≥ 0 (§5.2).
Conditional chains, fibre mixtures and refinements are not covered.

## 2. Work item 1: the single-shift law

Literature (checked 2026-10-29, web search). Erdős (Bull. Soc. Math. Grèce 6 (1965) 27–36) proved that almost all
m ≤ x have a divisor in every reduced class mod v when v ≤ (log x)^{log 2 − ε}; Erdős–Hall (Math. Proc. Camb. Phil.
Soc. 79 (1976) 281–287) proved the converse threshold he conjectured. So the **threshold (log x)^{log 2}** is
classical; I use it only through the quantitative bounds below, which I prove. I found no statement of the exact
fixed-v law (Thm 2.2) or of the uniform Janson-side bound (Thm 2.3) in the literature I could access; both use
only standard tools (Wirsing, Shiu, Sathe–Selberg), and no novelty is claimed for them as techniques.

**Lemma 2.1 (structure of −1-free sequences; PROVED).** Let G be a finite abelian group, g ∈ G, S a finite sequence
in G with g ∉ Σ*(S). Let F be the set of elements occurring at least |G| times in S and H = ⟨F⟩. Then
(a) Σ*(S) ⊇ H, so g ∉ H; (b) fewer than |G|² terms of S lie outside H; (c) if [G : H] = 2, every term of S lies in H.

*Proof.* (a) If h₁, …, h_r ∈ F, each occurs ≥ |G| ≥ ord(h_i) times, so every h₁^{a₁}⋯h_r^{a_r} (0 ≤ a_i < ord h_i) is a
subproduct of the F-terms; these exhaust H. (b) Terms outside H are not in F, so each of the < |G| distinct values
outside H occurs < |G| times. (c) If [G:H] = 2 and some term s ∉ H, then s and g both lie in the non-trivial coset, so
g s^{−1} ∈ H. By (a), g s^{−1} is a subproduct of F-terms, none of which is the term s (F ⊆ H), so g ∈ Σ*(S). ∎

**Theorem 2.2 (fixed shift; PROVED).** Fix v ≥ 3, and let r = r_v be the least index of a subgroup H ≤ G_v with
−1 ∉ H. Then, for x ≥ x₀(v),

    c_v x (log x)^{−(1−1/r)} ≤ #{m ≤ x : fail_v(m)} ≤ C_v x (log x)^{−(1−1/r)} (log log x)^{φ(v)²}.

If −1 is a non-square in G_v (equivalently 4 | v or v has a prime factor ≡ 3 (mod 4); this holds for **every
v ∈ 𝒞_n**), then r = 2 and

    #{m ≤ x : fail_v(m)} = (C_v + o(1)) x/√(log x),   C_v = Σ_χ κ_χ > 0,

the sum over the odd quadratic characters χ mod v (χ(−1) = −1), with κ_χ the Landau constant of
𝓛_χ = {m : χ(p) = 1 for every prime p | m with p ∤ v}.

*Proof.* Lower bound: if H ∌ −1 and every prime p | m′ has p mod v ∈ H, then Σ*(S_v(m)) ⊆ H, so fail_v(m). The set of
such m is multiplicative with f(p) = 1 on a set of primes of Dirichlet density 1/[G:H] (plus p | v), so by Wirsing's
theorem it has ~ κ_H x (log x)^{−(1−1/[G:H])} elements, κ_H > 0. Upper bound: by Lemma 2.1, fail_v(m) implies that
either (i) all prime factors of m′ lie in some index-2 subgroup H ∌ −1, or (ii) for some subgroup H ∌ −1 of index
≥ r with [G:H] ≥ 3, the number Ω_{∉H}(m) of prime factors of m′ (with multiplicity) outside H is < φ(v)². For a set
𝒫 of primes of relative density δ, Shiu's theorem with f = y^{Ω_𝒫} (0 < y ≤ 1) gives
Σ_{m≤x} y^{Ω_𝒫(m)} ≪_v x (log x)^{−δ(1−y)}, uniformly in y; with 1[Ω_𝒫 < K] ≤ y^{Ω_𝒫 − K} and y = K/(δ L₂) this gives
#{m ≤ x : Ω_𝒫(m) < K} ≪_{v,K} x (log x)^{−δ} L₂^K. Case (ii) with δ = 1 − 1/[G:H] ≥ 1 − 1/r (and ≥ 2/3 when r = 2)
is therefore ≪ x (log x)^{−(1−1/r)} L₂^{φ(v)²} (resp. ≪ x (log x)^{−2/3} L₂^{φ(v)²} when r = 2). This proves the
two-sided bound. When r = 2, case (i) is the union of the sets 𝓛_χ over odd quadratic χ, each of size ~ κ_χ x/√log x
(Wirsing), and pairwise intersections are sets of type 𝓛_{H∩H′} with index 4, of size O(x (log x)^{−3/4}).
Inclusion–exclusion to first order gives the asymptotic. The equivalence "−1 non-square ⟺ 4 | v or a prime
≡ 3 (4) divides v" is CRT; v ∈ 𝒞_n means 4 | v or v ≡ 3 (mod 4). ∎

For v | 24, G_v is an elementary 2-group and fail_v is exactly the union of the 𝓛_χ (the Landau-exact case of
z50 CONTEXT §4(b)). Theorem 2.2 says that for *every* fixed v ∈ 𝒞_n the law is still Landau-type, (log x)^{−1/2}: the
subset-product structure only adds an error of relative size (log x)^{−1/6+o(1)}. The uniformity in v is poor (the
factor L₂^{φ(v)²}); a uniform version is Conjecture 2.6.

**Theorem 2.3 (Janson side, uniform; PROVED).** For 3 ≤ v ≤ x^{1/4} and fixed κ ∈ [1, 2),

    P_{m≤x}(hit_v(m)) ≪_κ (log x)^{−Q(κ)} + (log x)^{κ(1+log 2−log κ)−1}/φ(v) + (1+log v)/v.

Also P_{m≤x}(hit_v(m)) ≤ (2 + log x)/(v − 1) for all v ≥ 3. Consequently, if φ(v) ≥ (log x)^{β log 2} with
1 < β < 2 fixed, then P(hit_v) ≪_β (log x)^{−Q(β)} + (1+log v)/v (take κ = β). In particular, for every ε > 0 there
is η = η(ε) > 0 with P(hit_v) ≤ (log x)^{−η} for all (log x)^{log 2+ε} ≤ v ≤ x, x ≥ x₀(ε).

*Proof.* Let K = κL₂ and z = κ/2 ∈ [½, 1). Split according to the divisor d ≡ −1 (mod v):
(1) Ω(m) > K: probability ≤ κ^{−K} x^{−1} Σ_{m≤x} κ^{Ω(m)} ≪_κ (log x)^{−κ log κ + κ − 1} = (log x)^{−Q(κ)}
    (Σ κ^{Ω(m)} ≪_κ x (log x)^{κ−1} for fixed κ < 2, by Selberg–Delange; Shiu's theorem does not apply to κ^Ω for
    κ > 1, since κ^{Ω(2^a)} violates f(n) ≪ n^ε).
(2) some d | m, d < v², d ≡ −1 (v): probability ≤ Σ_{j≤v} 1/(jv−1) ≤ (2/v)(1 + log v).
(3) Ω(m) ≤ K and some d | m, d ≥ v², d ≡ −1 (v). Write m = de; Ω is completely additive and 1[Ω(m) ≤ K] ≤ z^{Ω(m)−K},
    so the count is ≤ z^{−K} Σ_{v² ≤ d ≤ x, d ≡ −1 (v)} z^{Ω(d)} Σ_{e ≤ x/d} z^{Ω(e)}. Shiu's theorem (f = z^{Ω}, z ≤ 1)
    gives Σ_{e≤y} z^{Ω(e)} ≪ y (log 2y)^{z−1}, and, for dyadic D ≥ v² (so v ≤ D^{1/2}),
    Σ_{D<d≤2D, d≡−1 (v)} z^{Ω(d)} ≪ (D/φ(v)) (log D)^{z−1}. Summing over D = 2^j,
    count ≪ z^{−K} (x/φ(v)) Σ_{j ≤ log₂x} j^{z−1} (log₂x − j + 1)^{z−1} ≪ z^{−K} (x/φ(v)) (log x)^{2z−1}
    (the Beta-type sum is ≪_z (log x)^{2z−1} for every fixed z > 0). Finally z^{−K}(log x)^{2z−1} = (log x)^{κ(1+log 2−log κ)−1}.
The trivial bound is Σ_{d ≡ −1 (v), d ≤ x} 1/d. For the last claim: if β < 2, κ = β gives exponent −Q(β) in both
terms (since κ(1+log 2 − log κ) − 1 − β log 2 = −Q(β) at κ = β); if v ≥ (log x)^{2 log 2} use κ = 2 − δ for the
first two terms when v ≤ (log x)^{3}, and the trivial bound for v > (log x)^3; φ(v) ≫ v/log log v. ∎

**Proposition 2.4 (failure floor, unrestricted m; PROVED).** For x ≥ x₀ and 3 ≤ v ≤ x^{1/2}:
P_{m≤x}(fail_v(m)) ≥ 1/(4 log x). For v > x^{1/2}, trivially P(fail_v) ≥ 1 − (2 + log x)/(v−1).

*Proof.* A prime m = p ∈ (v, x] with p ≢ −1 (mod v) fails (its divisors are 1 and p). By Brun–Titchmarsh,
π(x; v, −1) ≤ 2x/(φ(v) log(x/v)) ≤ 4x/(φ(v) log x), which is ≤ 0.4 π(x)(1+o(1)) once φ(v) ≥ 10. For the finitely many v
with φ(v) < 10 use the prime number theorem in progressions. ∎

*Caution (repair of round 1).* This is a statement about unrestricted m ≤ x. On the progression m = n + v,
n ≡ 1 (mod 8), primes cannot serve as witnesses on the odd line (8 | n + v for v ≡ 7 (8)), and the statement is false
for v = 3 (2 | n + 3, 2 ≡ −1 (mod 3)). The progression floor needed in §5 is Lemma 5.0(b), proved with 2^a·p
witnesses.

So the **cost** of a shift, cost(v) := log(1/P(fail_v)), is at most log log x + O(1) for every v ≥ 3 (unrestricted m;
for admissible v on n ≡ 1 (8) see Lemma 5.0(b)).

**Proposition 2.5 (few-factor failures; PROVED).** Let 0 < β < 1 be fixed and φ(v) ≥ (log x)^{β log 2},
v ≤ x^{1/4}. Then P_{m≤x}(fail_v(m)) ≥ (log x)^{−Q(β)−o(1)}.

*Proof.* Take β′ < β and k = ⌊β′L₂⌋; by Sathe–Selberg P(Ω(m) = k) ≫ (log x)^{−Q(β′)} L₂^{−1/2}. Let r_v(m) be the
number of divisors ≡ −1 (mod v). For divisors d ≥ v², part (3) of the proof of Theorem 2.3 with K = k and z = β′/2
(valid for any fixed z > 0) gives E[r_v; Ω = k, d ≥ v²] ≪ (log x)^{β′(1+log 2−log β′)−1}/φ(v) ≤ (log x)^{−Q(β′)−(β−β′) log 2}. For d < v², write
m = de (here d < v² ≤ x^{1/2}, so log(x/d) ≍ log x) and bound #{e ≤ x/d : Ω(e) = k − Ω(d)} ≤ β′^{Ω(d)−k} Σ_{e≤x/d} β′^{Ω(e)} ≪ (x/d) β′^{Ω(d)} (log x)^{−Q(β′)}, so
this part is ≪ (log x)^{−Q(β′)}(1 + log v)/v. Both are o(P(Ω = k)) since φ(v) → ∞ polynomially in log x. Hence
P(fail_v | Ω = k) → 1 and P(fail_v) ≥ (1 − o(1)) P(Ω = k). Let β′ ↑ β. ∎

**Conjecture 2.6 (sharp costly-side law).** For v ∈ 𝒞_n with φ(v) = (log x)^{β log 2 + o(1)}, 0 < β ≤ 1:
cost(v) = (min{½, Q(β)} + o(1)) L₂. What is proved: cost(v) ≤ (Q(β) + o(1))L₂ for fixed 0 < β < 1 (Prop 2.5), and
cost(v) = ½L₂ + O_v(1) for each *fixed* v (Thm 2.2). Thm 2.2 is not uniform in v, so it gives nothing for growing
v ≈ (log x)^{β log 2} with β < 0.1867 (where Q(β) > ½). The matching lower bounds on cost(v), i.e. upper bounds on
P(fail_v) uniform in v, are open here. Q(β) = ½ at β = 0.1867, i.e. at v ≈ (log x)^{0.129}.

**Summary of the single-shift law.** With φ(v) = (log x)^{β log 2}:

| range | P(hit_v) | cost(v) = −log P(fail_v) | status |
|---|---|---|---|
| v fixed (unrestricted m) | 1 − (C_v + o(1))(log x)^{−1/2} | ½ L₂ + O_v(1) | PROVED (Thm 2.2) |
| 0 < β < 1 | → 1 (Erdős 1965) | ≤ (Q(β)+o(1)) L₂, and ≤ L₂ + O(1) always | PROVED upper bounds (Prop 2.4, 2.5); sharp form Conj 2.6 |
| 1 < β < 2 | ≤ (log x)^{−Q(β)+o(1)} | ≍ P(hit_v) → 0 | PROVED upper bound (Thm 2.3) |
| v ≥ (log x)^{1+ε} | ≤ (2+log x)/(v−1) | ≍ P(hit_v) | PROVED (trivial) |

Numerics (EVIDENCE; §6.1, `data/z50_shifts/single_1e*.txt`, 2·10⁴ random m per scale, x = 10⁸, 10¹⁶, 10²⁴, 10³²;
binomial standard error ≤ 0.0036 per frequency). For v = 4, 7, 8, 12 the quantity P(fail_v)·√log x is flat (0.65–0.68
for v = 4; 1.26–1.31 for v = 7; 1.29–1.37 for v = 8; 1.62–1.70 for v = 12). Half-point estimator: among the grid
moduli v ≡ 0 (mod 4), sorted by φ(v), take the first adjacent pair straddling P(hit) = ½ and interpolate log φ
linearly. (ties in φ kept in increasing v). It gives log φ_{1/2}/log log x = 0.678, 0.689, 0.691, 0.645 (brackets v = 12|20,
28|36, 40|48, 48|60; values as recomputed by the round-2 reviewer and by `python` from `single_1e*.txt`; round 1
printed 0.65–0.66 from a different tie order). The asymptotic theory says log 2 = 0.693, and
P(hit_v) is not monotone in φ(v) across unrelated moduli, so this is a rough indicator. For v ≥ 2048 the ratio
P(hit_v)·v/log x lies in [0.37, 0.63] at x = 10⁸, [0.73, 0.84] at 10¹⁶, [0.87, 1.01] at 10²⁴ and [0.87, 0.93] at 10³².
This is consistent with the first-moment value ≈ 1 being approached as x grows, and not more than that.

## 3. Work item 2: independence across shifts

### 3.1 What is true in the CRT model: negative dependence given the small-prime fibre

*Model.* Fix y ≥ 2 and caps A_p ≥ 1 (p ≤ y); put Q = ∏_{p≤y} p^{A_p} and let n be uniform in ℤ/Qℤ. For v ≥ 1 the
*y-part* of n + v is m_v = ∏_{p≤y} p^{min(v_p(n+v), A_p)}, a function of n mod Q. Put fail_v^{(y)} = 1[no divisor of m_v
is ≡ −1 (mod v)]. For an actual integer n, m_v divides n + v, and fail_v is
divisor-closed (if m has no divisor ≡ −1 (mod v), neither has any divisor of m), so fail_v(n+v) ≤ fail_v^{(y)}(n).
(The divisibility m_v | n + v holds for every n, because the exponents are capped by a minimum; no assumption on
v_p(n+v) is needed.)
The model density of ∩_v {fail_v^{(y)}} is what a CRT method evaluates.

**Theorem 3.1 (conditional negative dependence across shifts; PROVED, model).** Let V be a finite set of positive
integers, D_V = max_{v,v′∈V} |v − v′|, and Q₀ = ∏_{p ≤ min(y, D_V)} p^{A_p}. For every residue b mod Q₀,

    P(∩_{v∈V} fail_v^{(y)} | n ≡ b (mod Q₀)) ≤ ∏_{v∈V} P(fail_v^{(y)} | n ≡ b (mod Q₀)).

Hence P(∩_v fail_v^{(y)}) ≤ E_b ∏_v P(fail_v^{(y)} | b): in the model, *all* positive dependence between shift events is
carried by the full capped prime-power coordinates n mod p^{A_p}, p ≤ D_V (p = D_V included: for V = {4, 7}, p = 3
divides both shifted integers).

*Proof.* Given b, the residues n mod p^{A_p}, D_V < p ≤ y, are independent and uniform. For such p put
W_p = (min(v_p(n+v), A_p))_{v∈V}. At most one coordinate of W_p is non-zero: p | n+v and p | n+v′ give p | v − v′,
impossible since 0 < |v − v′| ≤ D_V < p. Each m_v is the b-determined part ∏_{p≤D_V} p^{(·)} times ∏_{p>D_V} p^{W_{p,v}}, and
fail_v^{(y)} is a coordinatewise *decreasing* function of (W_{p,v})_p, since raising an exponent only adds divisors.
*Claim:* a random vector X = (X_1, …, X_k) ≥ 0 with at most one non-zero coordinate is negatively associated (NA).
Let A, B be disjoint index sets, f, g bounded and increasing in X_A, X_B, and f₀ = f(0), g₀ = g(0). Always X_A = 0 or
X_B = 0, so f g = f₀ g + f g₀ − f₀ g₀ pointwise, and E f E g − E[fg] = (E f − f₀)(E g − g₀) ≥ 0 because f ≥ f₀, g ≥ g₀.
The same identity with f ≤ f₀, g ≤ g₀ handles decreasing pairs. Unions of independent NA families are NA
(Joag-Dev–Proschan 1983, property P7). So the family {W_{p,v}} is NA given b. For decreasing non-negative functions
on disjoint coordinate blocks, NA gives E ∏_i F_i ≤ ∏_i E F_i by induction (∏_{i≥2} F_i is decreasing on the union of
the remaining blocks). Apply this with F_v = fail_v^{(y)}. ∎

**Corollary 3.2 (chains within a fibre; PROVED, model).** For every fibre b, every v ∈ V and every V′ ⊆ V ∖ {v},
P(hit_v^{(y)} | ∩_{v′∈V′} fail_{v′}^{(y)}, b) ≥ P(hit_v^{(y)} | b) whenever the conditioning event has positive probability.
*Proof.* A = ∩_{v′∈V′} fail_{v′}^{(y)} is a decreasing function of coordinates disjoint from those of fail_v^{(y)}, so NA gives
P(fail_v ∩ A | b) ≤ P(fail_v | b) P(A | b). ∎
So in the model, conditioning on earlier failures never lowers a hit probability inside a fibre. A chain-of-ratios
argument (z50 CONTEXT §4(e)) can only lose through the *reweighting of fibres* by the sifting, i.e. through the drift of
the distribution of n mod p^{A_p}, p ≤ D_V, in the sifted set. This is a statement about the model. On actual
integers, §3.2 and §6.5 show EVIDENCE consistent with a drift of the quadratic profile, but they do not show that
profile drift is the only source of dependence for integers (Assessment). Note also that the comparison is with the
original marginal inside b; it is not a claim that each further conditioning raises an already-conditioned hit
probability.

*Remarks.* (1) The theorem uses only that hit_v is monotone in the prime-power content of n + v. It applies to the
v-indexed events of U, not to the u-indexed events (§5.1), whose condition "cofactor ∈ 𝒞_n" is not monotone.
(2) It is the shift analogue of the 3/4 note's "conditionally on n mod L_K, hits at different primes are
independent". It does not by itself bound anything for actual integers: the transfer from the model is the CRT
problem, capped by the (D)-ledger.
(3) The mixture E_b ∏_v P(· | b) can exceed ∏_v P(·) by a large factor. Heuristically the dominant fibres are
*quadratic profiles*. Let χ_{−v} = (−v/·), the Kronecker character attached to −v. It is odd and nontrivial, so its
kernel is an index-2 subgroup of G_v missing −1. If p ∤ 2nv and p | n + v, then χ_{−v}(p) = (n/p). So if (n/p) = +1,
the prime p is "good" (in ker χ_{−v}) at *whichever* shift it divides, simultaneously for all shifts. The Landau
failure at v is the event that all prime factors of n + v lie in ker χ_{−v}. (Repair: round 1 said "the kernel of
the odd character", but the relevant character is χ_{−v}; e.g. v = 8, p = 3, n = 1 has χ_{−4}(3) = −1 but
χ_{−8}(3) = +1.) Heuristic (Assessment): for k Landau-type shifts the local factor at p ≤ k is ≈ (p+1)/(2p) for the
joint event against ≈ e^{−k/(2p)} for the product, so log(joint/product) ≈ (k/2) log log k. If this is right, even
product bounds with a constant loss per shift are false in the model once k is large. This is a heuristic, not a
consequence of Thm 3.1; NA given full prime-power fibres does not imply NA given only the quadratic profile.

### 3.2 What actual integers do (EVIDENCE)

Exact computation for all n ≡ 1 (mod 8), n ≤ 10⁸ (12.5·10⁶ values; `scripts/z50_shifts_joint.c`, cross-checked against
the independent brute force `scripts/z50_shifts_joint_brute.py` at N = 2·10⁴, identical output). Let J(V) be the
fraction failing at every v ∈ 𝒞_n, v ≤ V, and Π(V) = ∏_{v≤V} P(fail_v), the product of the marginals. Among
non-squares (the 5000 odd squares fail at every shift and are removed):

| V | −ln J_nonsq(V) | −ln Π(V) | excess ln(J/Π) | profile-mixture −ln Σ_b w_b Π_b (9 primes) |
|---|---|---|---|---|
| 16 | 5.11 | 6.36 | 1.25 | 5.04 |
| 48 | 9.45 | 12.18 | 2.73 | 9.73 |
| 80 | 11.39 | 15.38 | 3.98 | 12.16 |
| 124 | 12.53 | 18.11 | 5.57 | 14.42 |

(`data/z50_shifts/profile9_N1e8.txt`, all columns computed over non-squares and renormalised; the profile b is the
*binary* vector 1[(n/p) = −1] for p = 3, …, 29, with p | n merged into the +1 class. The five-prime run
`profile_N1e8.txt` uses the ternary profile. Neither is the full small-prime-power fibre of Thm 3.1, so these
mixtures illustrate Remark (3) but do not test Thm 3.1.) The excess grows steadily, so near-independence fails already at polylog V. Conditioning on the
quadratic profile of n mod 9 small primes removes about two thirds of the excess at V = 124 and all of it for
V ≤ 16, as Remark (3) predicts. At V = 128 the joint failure set consists of 5000 squares and 39 non-squares; above
V = 63 it is within a factor 1.1 of the square floor.

### 3.3 What correlation technology supplies, and the (D)21 Prop 4.3 claim

The brief asks how large |𝒱| can be before uniformity is lost. Sources were read for the first item only; the others
are quoted from memory to place them on the relevant axes, and none is used in a proof.

* **Nair–Tenenbaum (Acta Math. 180 (1998) 119–144); Henriot (arXiv:1102.1643, Math. Proc. Camb. Phil. Soc. 152
  (2012)).** For F with F(ab) ≤ min(A^{Ω(a)}, B a^ε) F(b), (a,b) = 1, and a polynomial (or a product of forms)
  without fixed prime divisor, they bound Σ_{n≤N} F(Q(n)) by the expected Euler product. The constants depend on the
  degree, A, B, ε; Henriot makes the discriminant dependence explicit, not the degree dependence. Our fail_v are
  divisor-closed and ≤ 1, so they lie in the class with A = B = 1. I know of no version uniform in a growing number of
  shifts. Assessment: a growing-k version would have to run its sieve step at z ≈ N^{1/(Ck)}. That is the source of
  the dilution in Assessment 4.2. Whether its output would have the product shape of §5 with a *fixed* loss per
  coordinate is not established: local factors at small primes and the truncation need not distribute as a constant
  per shift. So these theorems are *not* claimed to be instances of the class 𝔐_C below.
* **Matomäki–Radziwiłł–Tao; Tao; Tao–Teräväinen; Hildebrand; Elliott.** These cover two-point correlations averaged
  over the shift, logarithmically averaged correlations at a fixed number of shifts, and fixed-shift results for
  multiplicative functions. Each works under its own hypotheses (boundedness, non-pretentiousness, averaging). The
  error terms are not the obstruction per se: fixed-shift divisor correlations such as Σ τ(n)τ(n+h) have
  power-saving errors, and an error N^{1−δ} is far below N exp(−(log N)^θ). What is missing is the *number* of
  shifts (two, or a fixed k, against the ≥ (log N)^{θ−o(1)} events required by Thm 5.3) and the *functions*: the
  joint indicator ∏_v 1[r_v(n+v) = 0] over many v is not of the treated type. Errors that are only o(N), or
  N/(log N)^B for fixed B, are in addition too large at the densities in question.
* **(D)21 Prop 4.3 re-examined.** The claim there: majorants built from ES witness classes along a fixed set of r
  shifts, *evaluated through CRT main terms*, save ≤ 2r(log log N^A + 3). Verdict: **confirmed within that scope, and
  sharpened along a different axis.**
  (i) For U the true marginal cost of every shift satisfies cost(v) ≤ log log N + O(1) (Prop 2.4 for unrestricted m,
  Lemma 5.0(b) on n ≡ 1 (8)). For each fixed admissible v it is ½ log log N + O_v(1) (Thm 2.2). So Prop 4.3's per-shift
  cap is of the true order and is not an artefact of CRT majorants. For growing v the cost tends to 0 (Thm 2.3).
  (ii) Letting r grow does not help product-form methods with a fixed loss per event (Cor 5.2): only
  (log N)^{log 2+o(1)} shifts cost a factor ≥ C. Methods with finer losses are governed by the precision budget
  (Lemma 5.1′, Thm 5.3).
  (iii) Prop 4.3 took the number of shifts as the axis. For product-form methods the relevant axis is the cost
  profile cost(v).
  Prop 4.3 says nothing about evaluations of such majorants with genuine interval information, and neither does
  this section.
* **The χ-twisted route.** r_v(m) := #{d | m : d ≡ −1 (mod v)} = φ(v)^{−1} Σ_{χ mod v} χ̄(−1)(1∗χ)(m), exactly. The event
  is 1[r_v = 0].
  (a) *Polynomial majorants, CRT evaluation* (PROVED). Work with the truncated, periodic witness count
  r_{v,N}(n) = Σ_{d ≤ N+v, d ≡ −1 (v)} 1[d | n+v], which equals r_v(n+v) for 1 ≤ n ≤ N. Assume v_i ≤ N (otherwise
  replace 2N by Y = N + max v_i throughout; without this the inclusion below fails, e.g. N = 10, v = 47, n = 137,
  d = 46 | 184). If P ≥ 0 on ℕ^r and P(0) ≥ 1,
  then ν = P(r_{v₁,N}, …, r_{v_r,N}) is a finite combination of indicators of intersections of witness classes, and
  ν ≥ 1 on the avoider set. Its CRT mean satisfies Eν ≥ exp(−2r(log log 2N + O(1))).
  - For v_i ∈ 4ℤ this is (D)21 Prop 4.3 (extension) verbatim.
  - For the odd line v ≡ 7 (8) it needs a separate argument. No power of 2 is ≡ −1 (mod v), since (2/v) = +1 and
    (−1/v) = −1. So every witness d has an odd prime factor q ∤ v. Hence the avoider set contains
    {n : no odd prime q ≤ 2N with q ∤ v_i divides n + v_i, for all i}. Its CRT density is
    ∏_{q odd}(1 − r_q/q) with r_q ≤ min(r, q − 1) nonzero residues, and this is ≥ exp(−2r(log log 2N + 3)) by the
    arithmetic of Prop 4.3.
  This lower-bounds the CRT mean Eν, *not* the exact sum of ν over [1, N]. High-period polynomial majorants evaluated
  with non-CRT interval information are **not** barred by this argument; that is one of the campaign's open doors.
  (b) *Correlation theorems for the pieces.* 1∗χ is divisor-bounded, not 1-bounded, so the 1-bounded correlation
  theorems do not apply as stated. Divisor-bounded analogues treat a fixed number of shifts. I do **not** claim that
  every use of χ-twisted sums returns only CRT information. Round 1 said "1∗χ pretends to be 1 + χ" and gave a
  categorical verdict; both are withdrawn after review.

## 4. Work item 3: assembly

**Record for U (lane E, PROVED on main).** E_U(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}) (EXSET_I3.md §7.3),
optimal for CRT methods on the native presentation (Cor 7.1). This lane adds no exponent.

**Remark 4.1 (what the fixed-k shift argument gives; routine, superseded).** Take k shifts v_i = 4·k!·i. These are
admissible, and ∏(n + v_i) has no fixed prime divisor: for p ≤ k all roots coincide at 0, and for p > k there are
< p of them. By Lemma 2.1, fail_{v_i}(n+v_i) forces fewer than φ(v_i)² prime factors outside some subgroup H_i ∌ −1.
Nair–Tenenbaum with the weights 2^{−Ω_{∉H_i}} then gives E_U(N) ≪_k N(log N)^{−k/4}. So E_U ≪_A N (log N)^{−A}.
This is weaker than the prime-local θ = 1/2 bound and lane E's 2/3. It is recorded only because it is what the
anatomy-of-shifts approach yields when run unconditionally.

**Assessment 4.2 (the sieve implementation stops near θ ≈ 0.41).** Suppose a uniform-in-k version of Remark 4.1
evaluates the joint law of k shifts through the z-smooth parts of the n + v, with z ≈ N^{1/(Ck)}, as a sieve of
dimension ≍ k at level ≤ N must. Write k = (log N)^a. Each n + v is then seen through ≈ (1 − a)L₂ prime factors, so
a shift is costly only if φ(v) ≤ (log z)^{log 2} = (log N)^{(1−a) log 2}. Needing k costly shifts gives
a ≤ (1−a) log 2, i.e. a ≤ log 2/(1 + log 2) = 0.409, and a saving ≤ (log N)^{0.41+o(1)}. This is below lane E's 2/3:
costly events are few, and the sieve dilutes each of them. It is a computation for this implementation, not a
theorem about all methods.

**The brief's |𝒱| ≍ log N/log log N scenario.** If that many coordinate events each cost a factor ≥ C > 1 and were
nearly independent, the saving would be ≍ log N/log log N. But only (log N)^{log 2+o(1)} coordinate events cost a
factor ≥ C (Thm 5.1: PROVED for the endpoint families V and W, CONDITIONAL for the level family T). **So such a 𝒱
does not exist.**

**Where squares escape.** Every bound in the class of Cor 5.2 is ≥ N exp(−(log N)^{0.7}) ≫ √N, so squares never
contradict it. They escape because the class charges each shift only its marginal failure probability, while at a
square every shift fails (Theorem E). §3.2 shows the same mechanism, the quadratic profile, making non-square joint
failures exceed the product of marginals.

## 5. Work item 4: barrier theorems for product-form shift bounds

### 5.1 Three coordinate families

For n ≡ 1 (mod 8), n ≤ N, with P_N the uniform measure, and a coordinate c, define
* V_c (endpoint v = c ∈ 𝒞_n, i.e. c ≡ 0 (4) or c ≡ 7 (8), c ≥ 4): n + c has a divisor ≡ −1 (mod c);
* W_c (other endpoint u = c ≥ 1): n + c = B·w with B ≡ −1 (mod c) and w ∈ 𝒞_n;
* T_c (level t = c ≥ 1): some word (c, u, w) of n has u or w ∈ 𝒞_n; then cn + 1 = (cu − 1)(cw − 1).
By the symmetry u ↔ v of words, U(n) = ∪_c V_c = ∪_{c≥1} W_c = ∪_{c≥1} T_c. Write h_c = P_N(F_c).

**Lemma 5.0.**
(a) *(PROVED for V, W.)* For every ε > 0 there is η > 0 with P_N(F_c) ≤ (log N)^{−η} for all c ≥ (log N)^{log 2+ε}.
More precisely P_N(F_c) ≪ (log N)^{−Q(β)+o(1)} when φ(c) = (log N)^{β log 2} with β in a compact subset of (1, 2), and
P_N(F_c) ≪ (log N)/c for all c ≥ 3.
*(Assessment for T.)* The same holds for T. The large-c bound P_N(T_c) ≪ (log N)/c is elementary: n = cuw − u − w
with c ≥ 3 gives (c−2)uw ≤ n, so at most O((N/c) log N) pairs (u, w). The polylogarithmic range needs a progression
moment (1/N)Σ_{n≤N} κ^{Ω(cn+1)} ≪ (c/φ(c))(log N)^{κ−1+o(1)}, uniformly for c ≤ (log N)³ and fixed κ < 2 (a
Selberg–Delange estimate in progressions), plus Shiu modulo c for both factors of cn + 1 = de, d ≡ e ≡ −1 (mod c),
with the 2-adic part split off. I have not written this out.
(b) *(PROVED for V, W, T.)* P_N(¬F_c) ≥ c₀/log N for all admissible c ≤ (log N)³ (c ≥ 1 for W, T), with c₀ > 0
absolute (ineffective for T).

*Proof of (a) for V, W.* Both events imply that n + c has a divisor ≡ −1 (mod c). Apply Theorem 2.3 with x = N + c;
restricting m = n + c to one class mod 8 costs a factor ≤ 16 for c ≤ N. For c > N + 2, a V or W hit with c ≥ 3 is
impossible.
*Proof of (b).* Let M = n + c (V, W) or M = cn + 1 (T). Choosing n mod 16 inside n ≡ 1 (mod 8), we may take M = 2^a p
with p an odd prime and a = v₂(M) ≤ 3. The factorisations of 2^a p are (2^i, 2^{a−i}p), so each event becomes a
congruence condition on p modulo 8c, together with conditions "2^i ≡ −1 (mod c), i ≤ 3". For c ≥ 3 the latter hold
only for c ∈ {3, 5, 9}. All c ≤ 64, including c = 1, 2, are handled by the finite check below, not by this generic
argument.
* *T, c > 64.* p lies in the single class 2^{−a} (mod c), and no factor pair has both factors ≡ −1 (mod c), so
  T_c fails. Siegel–Walfisz (c ≤ (log N)³) gives ≫ N/log N such n.
* *V, W, c > 64.*
  - Even c: a = 0 and only p ≡ −1 (mod c) is excluded.
  - Odd c: the mod-8 and mod-c conditions are on coprime moduli, and at most 4 classes of p mod c are excluded.
  - Since φ(c) ≥ 20 for c > 64 (minimum 20 at c = 66, computed for c ≤ 2·10⁵; φ(c) ≥ √(c/2) beyond), Brun–Titchmarsh
    removes at most a fraction 8/φ(c)·(1+o(1)) ≤ 0.45 of the primes p ≤ (N + c)/2^a in the required class mod 8.
    For even c the forbidden class is counted modulo lcm(8, c); for odd c the moduli 8 and c are coprime.
* *Small c.* For 1 ≤ c ≤ 64 and every family, a witness class (a, p mod 8c) was found by direct search (CERTIFIED,
  `scripts/z50_shifts_floorcheck.py 64 200000` and `… 2 200000 1`; failure depends only on (a, p mod 8c), with
  p > max(2c, 8) so that the class is reduced). PNT in progressions then gives density ≫ 1/log N. ∎

### 5.2 The budget lemma and the costly-event count

**Lemma 5.1′ (budget identity; PROVED, elementary).** Let 𝓔 be a finite set of coordinate events, each used once,
and suppose an upper bound has the form E_U(N) ≤ (N/8) ∏_{e∈𝓔} min{1, C_e π_e} + R(N), with π_e ≥ P_N(¬F_e), any
constants C_e > 0, and a remainder R(N) ≥ 0. (R ≥ 0 is part of the definition: a signed remainder could cancel the
product, and then nothing below applies to the total bound.) Then the product's saving is

    log(1/∏_e min{1, C_e π_e}) ≤ Σ_e log⁺( 1/(C_e (1 − h_e)) ).

In particular an event contributes only if C_e < 1/(1 − h_e), i.e. its loss is below 1 + h_e/(1 − h_e).

**Theorem 5.1 (costly-event count; PROVED for V and W, CONDITIONAL on Lemma 5.0(a) for T).** Fix C > 1. For each
family,

    #{c : P_N(¬F_c) ≤ 1/C} ≤ (log N)^{log 2+o(1)},   and   log(1/P_N(¬F_c)) ≤ log log N + O(1) for all c ≥ 1.

*Proof.* P_N(¬F_c) ≤ 1/C forces h_c ≥ 1 − 1/C, hence c < (log N)^{log 2+ε} by Lemma 5.0(a). For c ≤ (log N)³ the
cost bound is Lemma 5.0(b). For larger c, h_c ≪ (log N)/c gives cost O(1). ∎

**Corollary 5.2 (the class 𝔐_C; PROVED for V/W-events, CONDITIONAL for T-events).** If C_e ≥ C > 1 for every
e ∈ 𝓔, the saving of the product is ≤ (log N)^{log 2+o(1)}. So such a bound gives no θ > log 2 = 0.6931, in
particular no θ ≥ 3/4.

*Scope, stated precisely (repairs of round 1 after review).*
* The class consists of bounds whose formula *pays* a loss ≥ C on every event used. A method whose losses are merely
  *at most* C, with C_e = 1 + o(1) on cheap events, is not in 𝔐_C. It is governed by Lemma 5.1′: its cheap events
  contribute only where C_e < 1/(1 − h_e). Thm 5.3 quantifies this in the uniform case.
* The π_e are upper bounds for *unconditional* marginals. Products of conditional or fibrewise marginals (chains of
  ratios, Thm 3.1-type fibre mixtures) are not in the class.
* Each event is a whole coordinate event, used once. Refinements into sub-events are not covered.
* The hypotheses do not require CRT evaluation. But no strict extension of the (D)17–(D)29 classes, and no
  incomparability with them, is established here: output shape and evaluation mechanism are different axes, and I
  know of **no existing** non-CRT theorem that has been reduced to this shape. Growing-k Nair–Tenenbaum or
  growing-dimension Selberg bounds plausibly could be (§3.3), but this is not shown. **So Cor 5.2 does not meet the
  z50 fallback (a barrier for a demonstrated, strictly larger method class).** It is a design constraint with proved
  arithmetic inputs: a product over whole shift events that pays a constant loss per event cannot pass log 2.

### 5.3 The precision requirement above log 2

**Theorem 5.3 (PROVED for V/W-events, CONDITIONAL for T-events).** Let f(β) = β(1 + log 2 − log β) − 1, which is
increasing on [1,2] with f(1) = log 2 and f(2) = 1. Let 0 < a < Q(2) = 2 log 2 − 1 = 0.386 and let β_a ∈ (1,2) solve
Q(β_a) = a. If C_e ≥ 1 + ε for all e, with ε ≥ (log N)^{−a}, the saving is ≤ (log N)^{f(β_a)+o(1)}.

Equivalently, a saving (log N)^θ with log 2 < θ < 1 requires a uniform per-event loss
ε ≤ (log N)^{−Q(f^{−1}(θ))+o(1)}. It also requires at least (log N)^{θ−o(1)} events (each non-costly one contributes
≤ 2h_e ≤ 1) and coordinates reaching (log N)^{θ′}, θ′ = f^{−1}(θ)·log 2 − o(1). These are two different quantities:
an event count and a coordinate reach.

| target θ | β = f^{−1}(θ) | max. uniform per-event loss ε | coordinates reach |
|---|---|---|---|
| 0.70 | 1.0100 | (log N)^{−0.00005} | (log N)^{0.700} |
| **0.75** | **1.0874** | **(log N)^{−0.0037}** | **(log N)^{0.754}** |
| 0.80 | 1.1751 | (log N)^{−0.0145} | (log N)^{0.815} |
| 0.90 | 1.4018 | (log N)^{−0.0717} | (log N)^{0.972} |
| 0.99 | 1.8034 | (log N)^{−0.260} | (log N)^{1.250} |

(Values recomputed independently by the reviewer.)

*Proof.* By Lemma 5.1′ an event contributes only if h_e > ε/(1+ε) ≥ (log N)^{−a}/2, and then by at most
log(1/(1 − h_e)), which is ≤ log log N + O(1) always (Lemma 5.0(b)) and ≤ 2h_e when h_e ≤ ½. Events with h_e > ½
number (log N)^{log 2+o(1)} (Thm 5.1). For the rest, group coordinates by β_c = log φ(c)/(log 2 · L₂) on a finite mesh
of [1, 2 − δ], using Lemma 5.0(a) uniformly on each mesh interval. For c ≤ (log N)³ with β_c ≥ 2 − δ, the first two
terms of Thm 2.3 with κ = 2 − δ give h_e ≤ (log N)^{−Q(2−δ)+o(1)}; beyond, h_e ≪ (log N)^{−1.9}. Since a < Q(2), δ can
be taken so small that h_e > (log N)^{−a}/2 forces β_c ≤ β_a + o(1). The number of c with β_c ≤ β is
(log N)^{β log 2+o(1)}, so the total is ≤ (log N)^{log 2+o(1)} + max_{1≤β≤β_a} (log N)^{β log 2 − Q(β)+o(1)} =
(log N)^{f(β_a)+o(1)}, since f′(β) = log(2/β) > 0. ∎

**Remark 5.4 (exact independence is false, and fails early).** Take C_e = 1 and exact marginals π_e = P_N(¬F_e)
for all e, and R(N) = o(√N). (With loose π_e ≥ P(¬F_e), e.g. π_e = 1, nothing follows.) Since
E_U(N) ≥ √N/2 (odd squares), a valid such bound needs Σ_e log(1/P(¬F_e)) ≤ ½ log N + O(1). With R unrestricted, R
alone could pay for the squares, and nothing follows. The data of §3.2 show more: among non-squares ≤ 10⁸ the joint
failure over the shifts v ≤ 16 already exceeds the product of marginals by e^{1.25}, and by e^{5.6} at v ≤ 124.

### 5.4 What the barriers leave open (round-1 overreach withdrawn)

Lemma 5.1′–Thm 5.3 constrain **only** product-form bounds over whole coordinate events with unconditional
marginals. Round 1 also asserted that conditional chains and refinements "need this precision". That is withdrawn:
the theorems say nothing about them.
(i) *Chains of conditional ratios*, P(∩¬F_e) = ∏_e (1 − P(F_e | ∩_{e′<e} ¬F_{e′})). Conditional hit probabilities
need not be bounded by marginal ones. The reviewer's abstract mechanism is disjoint hits, which raise conditional
hit probabilities. For U the data go the other way. Along the chain of 𝒞-shifts v ≤ 128 at N = 10⁸, the empirical
conditional hit probability among surviving non-squares is *below* the marginal hit probability among non-squares at 45 of 48 steps (above at v = 12, 44; equal at v = 4),
reaching 0 at v = 120, 124 (EVIDENCE). Assessment: a chain proof for U will have to cope with this downward drift,
which the model (Cor 3.2) attributes to fibre reweighting and the data are consistent with attributing to the
quadratic profile. This is not proved to be the only obstruction for integers.
(ii) *Refinements* of a coordinate event into sub-events: divisor windows, single divisors, (u,v)-classes. The
finest refinement (single divisors d ≡ −1 (mod v)) is the native CRT class family, of total mass ≍ log² N. Its CRT
evaluation is capped at 2/3 by lane E's Cor 7.1; its non-CRT evaluation is open.
(iii) Events not indexed by a coordinate value, e.g. statements about n's own quadratic profile or factorisation.

## 6. Numerics (EVIDENCE unless marked)

All scripts run with `ulimit -v 8000000` and timeouts; data under `data/z50_shifts/` (40 kB).

6.1 **Single-shift law** (`scripts/z50_shifts_single.py`, 2·10⁴ uniform m ∈ (x/2, x] per scale, exact factorisation,
x = 10⁸, 10¹⁶, 10²⁴, 10³²; `single_1e*.txt`). The results are summarised under §2: the Landau law (log x)^{−1/2} for
v = 4, 7, 8, 12 (flat P(fail)·√log x); a half-point exponent of 0.645–0.691 against the asymptotic log 2 = 0.693; and the
trend of P(hit_v)·v/log x towards the first-moment value ≈ 1 at the larger scales (ranges in §2). Binomial standard
error ≤ 0.0036 per frequency (a standard error, not a confidence interval).

6.2 **Joint failure over shifts, exact** (`scripts/z50_shifts_joint.c`, all n ≤ 10⁸, n ≡ 1, 5 (mod 8), v ≤ 128;
cross-checked by the independent brute force `scripts/z50_shifts_joint_brute.py` at N = 2·10⁴, identical tables;
`joint_N1e8.txt`). CERTIFIED: for n ≡ 5 (mod 8) the shift v = 3 never fails (§1.1). For n ≡ 1 (mod 8) the joint
failure fraction J(V) drops from 0.305 (V = 4) to 1.7·10⁻³ (V = 24) and 4.4·10⁻⁴ (V = 60). It then sits on the square
floor 4.0·10⁻⁴: at V = 128 the survivors are the 5000 odd squares and 39 non-squares
(`joint_N1e8_nonsq.txt`, starting 105, 1617, 2961, 3985, 20601, 25305, 111969, …). The non-square survivors are
consistent with the z49 census (whose six non-square failures ≤ 10⁹ all appear). The others are killed by some
v > 128.

6.3 **Joint vs product, and the profile** (`z50_shifts_profile.c`, `z50_shifts_profile9.c`; `profile_N1e8.txt`,
`profile9_N1e8.txt`, all quantities over non-squares and renormalised; table in §3.2). `scripts/z50_shifts_analyze.py`
is a quick variant that subtracts the square fraction without renormalising; its numbers differ in the second
decimal and are not quoted. Among non-squares the joint
failure exceeds the product of marginals by e^{1.25} at V = 16 and e^{5.57} at V = 124. Conditioning on the quadratic
profile mod 5 primes (243 ternary profiles, p | n separate) or 9 primes (512 binary profiles, p | n merged with +1)
removes most of the excess. The
remainder shrinks as primes are added (2.33 nats left with 5 primes, 1.88 with 9 at V = 124).

6.4 **Finite check for Lemma 5.0(b)** (`scripts/z50_shifts_floorcheck.py 64 200000` and `… 2 200000 1`): a 2^a·p
witness of failure (a ≤ 3, p > max(2c, 8) prime) was found for every admissible V_c, 4 ≤ c ≤ 64, and every W_c, T_c,
1 ≤ c ≤ 64 (CERTIFIED; output "no witness found for: []" in both runs; re-run independently by the reviewer for
c ≥ 3).

6.5 **Chain of ratios** (`scripts/z50_shifts_chain.py`, `chain_N1e8.txt`; non-square normalisation on both sides,
as repaired after the round-2 review). Along the 48 shifts v ∈ 𝒞, v ≤ 128, the conditional hit probability among
surviving non-squares is below the non-square marginal hit probability at 45 steps, above at 2 (v = 12, 44) and
equal at 1 (v = 4, the first step). At v = 120, 124 it is exactly 0; at v = 119 it is 0.022 against 0.221. These are
computed from the stored census fractions (EVIDENCE for §5.4(i)).

## 7. Reviews and remaining gap

**Round 1 → hostile cross-model review** (Astra, deep mode; `reviews/z50-shifts-review-astra.md`).
Verdict: MAJOR repairs required, no FATAL. Sound as written: Lemma 2.1, Thm 2.2, Prop 2.5, Thm 3.1 (reviewer
enumerated a 12600-point model, 0 violating fibres), Assessment 4.2, the table of Thm 5.3, and the small-scale
reruns of the C census against the brute force (identical) and of the floor check. Repairs applied in round 2:
* the scope of Cor 5.2 / Thm 5.3 is narrowed to formulas that pay the loss on whole coordinate events with
  unconditional marginals;
* the claims that chains and refinements "need this precision" are withdrawn (§5.4);
* the variable-loss budget is stated as Lemma 5.1′;
* the level family T is downgraded to Assessment/CONDITIONAL in Lemma 5.0(a), Thm 5.1, Cor 5.2 and Thm 5.3;
* Prop 2.4 is restricted to unrestricted m, and the progression floor is now Lemma 5.0(b) with 2^a·p witnesses
  (c ∈ {3,5,9} and φ(c) ≥ 20 for c > 64 corrected; coordinates 1, 2 added to the finite check);
* the χ-reduction is restricted to CRT means, with an explicit truncation and an odd-line argument;
  "pretends to 1 + χ" is withdrawn;
* §1.2 no longer claims a false residue iff; it gives forced-hit examples, cites the prime-local θ = 1/2 bound and
  folds in lane E;
* "Shiu" is no longer cited for κ^Ω;
* Remark 4.1 uses shifts without a fixed prime divisor;
* the numerics prose is fixed (binary/ternary profiles, standard error, half-point estimator, first-moment ranges);
* event count is separated from coordinate reach.

**Round 2 → hostile cross-model review** (Astra, deep mode; `reviews/z50-shifts-review-astra-r2.md`). Verdict:
substantial repair accepted; no FATAL or MAJOR mathematical defect remains. SOUND: Cor 3.2 (reviewer's exhaustive
model check: 24096 conditioning tests, 0 violations), Lemma 5.1′, the V/W versions of Thms 5.1 and 5.3, Remark 4.1,
the lane-E incorporation, and the floors (both finite runs reproduced). T is correctly conditional. Local repairs
applied in round 3:
* R ≥ 0 restored in the class definition;
* the incomparability claim withdrawn: Cor 5.2 is now stated as a design constraint that does *not* meet the z50
  fallback;
* §1.3 narrowed to the exact class;
* the model conclusions (Cor 3.2) separated from the integer profile evidence;
* the χ-reduction cutoff v_i ≤ N added (the reviewer's counterexample N = 10, v = 47, n = 137);
* c = 1, 2 routed through the finite check only;
* exact marginals required in Remark 5.4;
* the chain script normalised on both sides (45 below, 2 above, 1 equal);
* the half-point values recomputed (0.678, 0.689, 0.691, 0.645);
* cost(v) ≍ log log N replaced by the proved upper bound plus the fixed-v statement; Conjecture 2.6 kept as
  CONJECTURE.
The correlation survey in §3.3 remains an Assessment from memory (only Nair–Tenenbaum/Henriot were checked against
the source).

**Final labelled outcome (after round 3 repairs).**
* PROVED: §1.1; Lemma 2.1; Thm 2.2 (fixed-v Landau law); Thm 2.3 (uniform Janson-side bound); Props 2.4–2.5;
  Thm 3.1 and Cor 3.2 (model NA across shifts given the full small-prime-power fibre); the χ-polynomial reduction
  for CRT means (both lines); Lemma 5.0 and Thm 5.1–Cor 5.2–Thm 5.3 for the endpoint families V, W; Lemma 5.1′.
* CONDITIONAL / Assessment: the level-family T versions of Lemma 5.0(a) and Thms 5.1–5.3. Missing: a uniform
  progression Selberg–Delange moment, and the factor-convolution/Shiu and small-factor bookkeeping for cn + 1. The
  T failure floor, Lemma 5.0(b), is proved. Also Assessment: 4.2 (0.41) and the profile heuristic (k/2) log log k.
* CONJECTURE: 2.6.
* EVIDENCE: §§3.2, 6.
* Not achieved: any θ for U beyond lane E's 2/3. No theorem with θ > 3/4. The z50 fallback (a barrier for a
  demonstrated, strictly larger method class) is **not** met: Cor 5.2 is a design constraint with proved arithmetic
  inputs (§5.2 scope).

**Exact remaining gap.** Product-form arguments over coordinate events cannot pass log 2 with constant losses
(PROVED for V/W). Above log 2 they need per-event relative precision finer than each event's own hit probability
(Lemma 5.1′), e.g. (log N)^{−0.0037} at θ = 3/4. That is a one-sided product upper bound over ≥ (log N)^{0.75−o(1)}
shift events with near-exact losses, which no known correlation result provides. The doors not covered are:
* chains of conditional ratios. By Cor 3.2 they lose, *in the model*, only through fibre reweighting. On integers
  the conditional hit probabilities fall below the marginals at 45 of 48 steps (§6.5), consistent with a
  quadratic-profile drift (EVIDENCE/Assessment). Plausibly a chain proof for θ > 2/3 will need lower bounds for hit
  probabilities inside such biased sifted sets (Assessment);
* refinements into divisor-level events, whose CRT evaluation is capped at 2/3 by lane E;
* non-coordinate events.
