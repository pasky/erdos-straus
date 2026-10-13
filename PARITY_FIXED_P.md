# PARITY_FIXED_P — hatch H-B: parity-breaking / bilinear structure at a fixed prime (task O165)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.**
Labels as in DISCOVERIES.md. Scripts `scripts/pf_*`.

Goal (brief): a formulation of ES(p) as a sum over a long structured family (length a power of p) with a
non-tiny positive main term and Friedlander–Iwaniec (FI) Type I/Type II structure, where parity is the only
obstruction; say what an FI-type theorem would have to deliver.

## 1. Dictionaries at fixed p (PROVED, elementary; checked by `scripts/pf_dict_check.py`)

Notation: row II{a,d} target `f | N = p + 4a²d`, `f ≡ −1 (mod 4ad)` (count over *all* such f, no range cut);
Type I target `f | p² + 4c²d`, `f ≡ −p (mod 4cd)`.

**Lemma 1.1 (Type II as a three-parameter divisibility).** For every integer n ≥ 1 the map
`(h,k,d) ↦ (a,d,f) = ((hn+k)/(4dhk−1), d, 4adh−1)` is a bijection
`{(h,k,d) ∈ ℕ³ : (4dhk − 1) | hn + k}  →  {(a,d,f) : f | n + 4a²d, f ≡ −1 (mod 4ad)}`.
*Proof.* Given (a,d,f), put q = 4ad, g = N/f. Since f ≡ −1 and N ≡ n (mod q), g ≡ −n (mod q). So
f = qh − 1, g = qk − n with h,k ≥ 1. Expanding fg = n + qa gives `qhk − hn − k = a`, i.e.
`a(4dhk − 1) = hn + k`. Conversely, if m = 4dhk − 1 divides hn + k, put a = (hn+k)/m ≥ 1, f = 4adh − 1,
g = 4adk − n. Then 4adk = n + (k+a)/h > n, so g ≥ 1, and the same algebra gives fg = n + 4a²d. The two maps
are mutually inverse. ∎ (Brute-force bijection check: all n ≤ 119.)

h = 1 is the (A)3 subsystem `(4dk−1) | n + k` (BRAINSTORM/tech_maynard_theta Lemma 1.1). Reducing mod m:
`m | hn + k ⟺ m | 4dh²n + 1`, so the triple is also "4dh²n + 1 has a divisor ≡ −1 (mod 4dh)" (the
divisor form tp+1 = m·m″ with t = 4dh²).

**Lemma 1.2 (Type I is p-free up to one congruence).** For every prime p,
`(d,k,f) ↦ (c,d,f) = ((f+p)/(4dk), d, f)` is a bijection
`{(d,k,f) : f | 4dk² + 1, 4dk | f + p, p ∤ f}  →  {(c,d,f) : f | p² + 4c²d, f ≡ −p (mod 4cd), p ∤ f}`.
*Proof.* On either side, a prime r | gcd(f, cd) divides f + p (as 4cd | f+p, resp. as 4dk | f+p and
c = (f+p)/4dk... directly: r | f and r | 4cdk = f + p), hence r = p, excluded; so gcd(f, cd) = 1.
(←) f = 4cdk − p with k = (f+p)/(4cd). Mod f, p ≡ 4cdk, so p² + 4c²d ≡ 4c²d(4dk² + 1), hence f | 4dk² + 1.
(→) p ≡ 4cdk (mod f) gives p² + 4c²d ≡ 4c²d(4dk²+1) ≡ 0, and f = 4cdk − p ≡ −p (mod 4cd). ∎
(Solutions with p | f force p | cd; they are the non-primitive ones and are irrelevant here.)
(Direction (→) checked for n ≤ 39.) Writing m = dk: **Type I(p) ⟺ ∃ m ≥ 1, k | m, f | 4mk + 1 with
p ≡ −f (mod 4m).** The integers 4mk + 1 do not involve p; p enters only through its residue mod 4m. This is
the B1 frame made exact at fixed p: p must avoid the residue sets −D_m (mod 4m), D_m = {f : f | 4mk+1, k|m},
for *every* m — a sieve in which the single integer p is the sifted object.

**Lemma 1.3 (spin lemma; PROVED).** Let p ≡ 1 (mod 4) be prime.
(i) (Type II) If ℓ is a prime, ℓ | p + 4a²d, ℓ ∤ 2pad, then `χ_{−4d}(ℓ) = (ℓ/p)`.
(ii) (Type I) If ℓ | p² + 4c²d, ℓ ∤ 2pcd, then `χ_{−4d}(ℓ) = +1`.
*Proof.* (i) −4a²d ≡ p (mod ℓ), so (−d/ℓ) = (p/ℓ) = (ℓ/p) by reciprocity (p ≡ 1 mod 4). (ii) −4c²d ≡ p²
is a nonzero square mod ℓ. ∎ (18950 instances checked, 0 violations.)

*Consequence (the sign layer, made explicit).* The genus character χ = χ_{−4d} lifted to q = 4ad (resp. 4cd)
has χ(−1) = −1, so a hit f needs χ(f) = −1.
* Type I: every divisor f coprime to 2cd has χ(f) = +1, but the target class −p has χ(−p) = −χ(p): the
  χ-test is passed iff (−d/p) = −1 — pure congruence data on p (the BL/genus condition). No spin freedom.
* Type II: χ(f) = (f/p) (Jacobi symbol mod p) for f | N coprime to 2ad. So the χ_{−4d}-layer of slice II{a,d}
  is passed iff **N_θ = p + 4a²d has a divisor that is a quadratic non-residue mod p**, i.e. a prime factor
  ℓ ∤ 2ad with (ℓ/p) = −1. Since N_θ ≡ 4a²d (mod p), (N_θ/p) = (d/p): for (d/p) = −1 this is automatic; for
  (d/p) = +1 it is a genuine **spin event** (an even, nonzero number of QNR prime factors). At n = m² the
  symbol (ℓ/n) is replaced by +1 and the event never happens — the T1 mechanism at the level of a single
  character. This is the FI-type object of the problem: Legendre symbols modulo the fixed p evaluated on the
  prime factors of a polynomial family.
