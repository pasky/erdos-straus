## Summary

**301+ items** (exact count above), breadth-first, nonsense-filter only. Along the way the lane made and
verified (small ranges, `scripts/z52b_free_fable_sanity.py`) several small structural observations that
sharpen how the other items should be read:

1. The "tied-modulus" form most items reach for — **C-form**: 4Cp+1 = ab with a ≡ b ≡ −1 (mod 4C), equivalently
   p = 4Cuv − u − v, equivalently **some p + u has a divisor ≡ −1 (mod 4u)** — is a *sufficient* condition for ES,
   strictly weaker than Type II: **409, 577, 5569, 9601** (all ≡ 1 mod 24; two in Mordell-hard classes) have no
   C-form certificate for C ≤ 60000 although ≈ 52 were "expected" for 409, while each has a Type II certificate with
   c = 2. Type II with (c, d) is exactly the C-form for the multiple n = cp with C ∈ cℤ.
2. **Every C-form certificate divisor a is a QNR mod p** ((a/p) = −1, forced by reciprocity); this reproves T1 for
   the C-form in two lines and is a first entry in the "reciprocity signature" of certificates.
3. The Type I one-parameter sibling (c = 1: f | p² + 4d, f ≡ −p mod 4d) has its own lone exception below 20000,
   **2521 ≡ 1 (mod 840)**, and certifies all four C-form exceptions — the two one-parameter exceptional sets are
   disjoint in range, so two one-parameter families cover everything < 20000.
4. Gate G4 quantified: subgroup-vs-subset-product disagree in ≈ 21% of (p, C); among "rich" failures (Ω ≥ 5) only
   39% are subgroup-type — multiplicity poverty, not Galois structure, is the dominant failure mode.

### Ten items I find most exciting (ids in `free_fable.jsonl`)

1. **Finding: C-form misses 409, 577, 5569, 9601** — and the follow-ups (forensics, obstruction type, OEIS/MO
   publication). A concrete, hand-checkable sub-conjecture that is *false*, with a measurable "expected 52, got 0" gap.
2. **QNR lemma (a/p) = −1** and the "forced-symbol discovery" program: systematically find every constraint that
   certificates must satisfy; T1 is the first; 409 may be the second.
3. **Type I c=1 exception 2521 + disjointness conjecture**: ES for primes ⟸ the additive-shift and
   multiplicative-shift one-parameter exceptional sets are disjoint — a reciprocity-flavoured target.
4. **Shifted-prime reparametrisation**: C-form ⟺ ∃u: p + u has a divisor ≡ −1 (mod 4u). Puts ES next to the
   Hall–Tenenbaum "divisors of shifted integers" literature and makes 409 a crisp elementary puzzle.
5. **Half-dimensional sieve for C = 1** (Iwaniec): the failure set {p : 4p+1 has only factors ≡ 1 mod 4} is
   ≍ x/(log x)^{3/2} — theorem-level sizes for failure sets, and K-fold versions with explicit sieve dimension.
6. **Turán–Kubilius pointwise in p**: for fixed p almost all C have ω(4Cp+1) ≈ log log — the "poor" failures are
   provably rare; what remains is the Davenport-constant / probabilistic regime, now precisely delimited.
7. **Artin/Hooley analogy** (fixed base, varying modulus; GRH-conditional pointwise theorem) — the closest proved
   shape to ES I could find; the exact point where Hooley uses "free q" should be written down.
8. **Lenstra 1984 / Coppersmith–Howgrave-Graham** "divisors in residue classes": ES's existential question is the
   dual of a solved algorithmic one; Lenstra's ≤ 11 bound for large moduli is a pointwise *upper* bound of exactly the
   right shape.
9. **Square-avoiding polynomial families** (n = 4t² + 1 etc.): T1 only kills identities whose parameter polynomial
   hits odd squares — so identities in t are a real loophole in the Mordell–Schinzel/T1 fence; worth a Gröbner search.
10. **Kneser / stabiliser taxonomy of failures** and the LP-duality certificate: two ways of turning "existence"
    into a mechanically checkable structure, both cheap to run on the data.
