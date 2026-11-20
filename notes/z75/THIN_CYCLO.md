## §0
Result: ES holds for every 4^s+k with k=33,273,297 and s≥0, and for 15b^s+1 for every s≥0 for infinitely many even bases b whose exponential sequences admit no finite ET/divisor covering. Label: PROVED (computer-assisted for the offsets, relative to Mordell's prime reduction and the five-slice word identity)
Scope: Four explicit exponential families including the Lean-checked b=2 family of CONJS_GEN; no general ES or prime-distribution result. Only b=2 is formalised.
Review: cross-review owed
Triage: HEADLINE
STATUS delta: replace residual/open exponential families in §1C by ES for all s for 15·2^s+1 (Lean) and for 4^s+k, k=33,273,297 (finite certificates).

### 1. Three all-exponent covers

**Theorem.** For each k in {33,273,297} and every integer s≥0, 4/(4^s+k) is a sum of three positive unit fractions. No primality assumption. The actual proof objects are `data/z75/thin_cyclo/cert_{33,273,297}.json` and `scripts/z75_thin_verify.py` (standard-library Python, no PARI or search imports).

Start with Mordell's six possible hard prime residues M={1,121,169,289,361,529} mod 840. Outside M, ES(n) follows for composite n too: if n has a prime factor in {2,3,5,7} use its solution and scale; otherwise M is the subgroup of unit squares, so some prime factor must be outside M. For s≥2 the residues of 4^s mod 840 have period 6. This leaves s≡3 mod 6 for k=297; s≡4 mod 6 for 33; and **all even s** for 273. Not all earlier ET/divisor work is captured by this first pass; see `EXP_OPEN.md` §4 and `EXP_NEAR_SQUARE.md` §2. Our cutoff is s=32 throughout, not an unverified 'sufficiently large'. The certificates supply direct triples for all 96 smaller inputs and for all auxiliary divisors used.

**Positive witness rules.** A row is (P,j,kind,parameters) and applies to all s≥32 with s≡j mod P. Put n=4^s+k.

- M and D: use the reduction just given, or a named q|n for which the file includes a verified ES(q) triple.
- A: given A,u let t=(A+1)/u, v=(n+u)/A. Require both quotients integral, t,u,v≥2 and 8|(n+t)tuv. This is a good word; the five-slice identities in `DEDEKIND_ES.md` Thm 4.5 give ES for odd n≡1 mod 4. This includes rules discovered from the factorization tn+1=(tu−1)(tv−1); swapping which letter was held fixed does not change the checker.
- II: a fixed f≡−1 mod 4ab with bn≡−a mod f. Set d=(f+1)/(4ab), e=(n+4a²d)/f. Then e is a positive integer (b is a unit mod f); e≡−n mod 4ad and b'=(n+e)/(4ad) is positive integral. We have 4ab'd=n+e and be=a+b' by substitution. Therefore (ab'd,abdn,b'bdn) are ES denominators (multiply out). Here b labels the c-parameter, not b'.
- K and gap (Type I/II divisor window): choose f>0, f≡3 mod 4; set K=(n+f)/4 and N=nK. It suffices to exhibit *any two* positive divisors D,E of N with f|D+E. Use denominators K, (N/D)((D+E)/f), (N/E)((D+E)/f). No D·E|N or coprimality assumed. In K rows, K0|K is a certified constant; each divisor is y n^i (K/K0)^h with y|K0, i,h∈{0,1}.
- In gap rows write k+f=2^m a^d, a odd, m≥2. For odd d and d|2s−m let z=2^{(2s−m)/d}. Then K=2^{m−2}∏_{h|d} Φ_{2h}(z,a), using the homogeneous cyclotomic polynomials (product z^d+a^d). They are positive integers for positive arguments; at z=a the same polynomial identity holds. For d=4 require 2s−m≡2 mod 4 and let z=2^{⌊(2s−m)/4⌋}. Instead K=2^{m−2}(2z²−2za+a²)(2z²+2za+a²). This is the Sophie Germain factorization of **4z⁴+a⁴**. The proposed odd-r identity for 4^r+1 is the case z=2^{(r−1)/2}, a=1. The masks in the certificate select subsets of the factors (including optionally n), and the indicated power of 2, separately for D and E.

**Why the finite certificate proves an infinite assertion.** For each modulus m actually used, the checker takes the *least* s≥32 in the row and verifies 4^s(4^P−1)≡0 mod m. Induction gives the same n mod m for every later s. This handles nonunits at 2 without Euler's theorem. For K0 divisions it freezes modulo 4K0f when the quotient is used; otherwise 4K0 and f separately. For gap rows it checks d|2P and 2^r≡2^{r+2P/d} mod f with r=⌊(2s−m)/d⌋, so each polynomial atom has the same residue; recursive exact quotient evaluation of z^h+a^h handles large degrees without polynomial package dependencies. The first representative verifies positivity/size for A rows using n≥4^32+k; all gap atoms are positive by construction. Every s<32 and every auxiliary divisor is checked by 4xyz=n(xy+yz+zx), no 'all finite small primes satisfy ES' oracle. Finally a bitset marks the *entire* exponent period, asserting exact coverage:

|k|period H|M rows|D|word A|K|cyclotomic/SG gap|II|covered|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|297|5040|5|7|9|3|0|0|5040/5040|
|273|55440|3|7|25|26|2|0|55440/55440|
|33|720720|5|8|9|217|4|10|720720/720720|

**Example (297, the whole last step).** Fixed divisors and words leave precisely 843,3003,3363 mod 5040. In the first and last use f=5183, 26334|K, (D,E)=(7,342n); in the middle use f=539, 43425|K, (D,E)=(1,8685n). All other classes are handled without these windows. Thus variable-degree extraction was *not needed* for 297. For 33 the selected gap factors have degrees 7 and 21; for 273 one row uses the Sophie Germain split with f=51, k+f=324=4·3⁴. The fixed-period search made progress by allowing the factor n itself into the divisor pair and choosing complementary subproducts of K; a single good divisor in one congruence class is not necessary. A successful menu is not claimed minimal or uniquely necessary.

**Reproduction.** `ulimit -v 6000000; timeout 60 uv run --offline --no-project python scripts/z75_thin_verify.py`. No unproved computational hypotheses. The discovery programs (`z75_thin_cyclo`, `z75_thin_smooth`, `z75_thin_ii`, `z75_thin_product`, `z75_thin_pack`) do not enter the proof. See `coverage.txt`. Literature/prior campaign scope: `EXP_105.md`, `EXP_OPEN.md`, `EXP_NEAR_SQUARE.md`; proposal supersedes their **open** cases, not their scoped sterility lemmas. No external priority claim.

### 2. Infinitely many bases past the square obstruction

Let L=lcm(16,7,11,17,19,31,39,61,99,164,248,2992). **For every positive b≡2 mod L and every s≥0, ES(15b^s+1) holds.** No finite collection of ET congruence classes of the seven classical types and fixed prime divisor classes covers all sufficiently large exponents for any such base. In particular this is not just restricting the already proved sequence to a subsequence of exponents: b can have odd prime factors (e.g. 2+L has an odd factor).

*Proof.* For s mod 360 outside {0,240}, the constructive rows in `lean/ES/ES/Proth15.lean` (`s_cls_0` through `_12`) use only the congruence of n=15·2^s+1 modulo a divisor of L, and positive integer solutions for the whole indicated residue class or for a divisor. Therefore the same row remains valid with base b. For s=1,2,3 one can instead scale the smaller solutions for 31,61,11 respectively, since all divide L and n has the same residue there. At s=0 use ES(16). For the remaining s>0, 60|s. In `CONJS_GEN.md` Thm 1 replace x=2^r by x=b^r; b is even and b≡2 mod 7, and that proof uses only 16|x, x≡4 mod 7, and n+14=15(x^{3h}+1) with h odd. These remain true. This argument transfers fixed-output congruences, *not* an arbitrary ES witness for 15·2^s+1.

For the barrier, take any finite menu, let M be a common multiple of its moduli and tested primes, and choose arbitrarily large s divisible by every unit order of b at the prime powers in M coprime to b. At prime powers whose prime divides b we have n≡1 for large s, including at 2. At the other prime powers n≡16. Therefore n is a square unit modulo M (CRT) and is divisible by none of the tested primes. Each ET class is sterile on square units (`EXPONENT_COVERING.md` Thm 1.4, classical square obstruction). This is not a claim that general ES fails at squares. ∎

### 3. Screens and formal status

F1: odd squares can occur at individual s, e.g. 4³+297=19² and 4⁴+33=17². The direct triples/scaling are ES witnesses, not good words at a square. F2: no claim of coverage by the c=1,numerator-8 slice, or uniformity in the numerator. F3: composites are expressly included; divisibility scaling and K rules do not require primality. F4: no rule here claims to cover the star zeros as a family; the original class-map/word controls are in `CONJS_GEN.md`.

`ESProth15.proth15` now proves the full b=2 family in Lean 4.34.1 (`lean/ES/ES/Proth15.lean`, build and axiom report `data/z75/thin_cyclo/lean_proth15_build.txt`). The required MemoryMax=16G build rebuilt the module. Only propext, Classical.choice and Quot.sound; no sorry or native_decide. This Lean verification does *not* cover the offset certificates or base-extension theorem.
