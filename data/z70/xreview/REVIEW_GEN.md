# Z70 GEN — hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** Reviewed `side-agent/z70-gen` at `49de2aa1c`. ES is OPEN.
Accept the narrow negative findings and the scoped mathematics, not an impossibility of generative maps.
No provider/auth/quota error occurred. Commands used ≤1800 s timeouts, `ulimit -v 6000000`, ≤2 compute processes.

## Per-claim audit

| Claim | Classification | Independent derivation / boundary |
|---|---|---|
| GW(a,b): genus wall | CORRECT-WITH-FIX | Since A divides p+4a²d and gcd(A,2ad)=1, reciprocity gives (A/p)=(p/A)=(−d/A)=−1, using A≡−1 mod 4d and the odd character χ_{−4d}. Multiplicativity then keeps sums, integer multiples and ψ-preserving automorphisms of kernel seeds in ker ψ. This says nothing about maps supplied with ψ=−1 seeds. Explicitly require invertible prime ideals: for nonsquare d, ideals over conductor primes need not define classes. |
| GW(c): norm obstruction | CORRECT-WITH-FIX | For a p-coprime ideal norm, ψ=−1 forces some nonresidue prime factor, hence norm≥n_p. The proof of the minimal-norm corollary silently uses p>4d/3. Supply: G≠∅ implies p=4abd−e≥4abd−a−b≥4d−2; thus α≤√(4dp/3)<p for p≥5. No extra hypothesis on the theorem is needed. |
| GW(d): saturation | CORRECT | Decompose Cl=Cl₂⊕Cl_odd and H=H₂⊕H_odd. Killing the 2-part and inverting 2 on the odd part gives H^sat=Cl₂⊕H_odd. ψ kills Cl_odd and is nontrivial on Cl₂. Saturation commutes with the allowed automorphisms, so taking their closure first is valid. “Only halving exits” is true only for the explicitly enumerated operations; halving a nonzero odd-part seed is not restricted to S_RED. |
| GW(e): squares/composites | CORRECT | At a square, gcd(A,m)=1 follows from A∣m²+4a²d and gcd(A,2ad)=1, so (m²/A)=1 contradicts the same −1 calculation. For nonsquare n≡1 mod 4, reciprocity gives (A/n)=−1 in the stated admissible setting. This is not an all-integer “every n” theorem; the supplied n=15 exception is real. |
| AMB | CORRECT | An ambiguous reduced form has b=0, b=a or a=c. The first two yield norms k or 2k, k∣d; the last requires p≤3d and is excluded. If g is ambiguous, E is too because T_d is 2-torsion. A norm-k representative gives a principal primitive product E·conj(b). Its rational-generator case forces e=k=1, impossible for p≡1 mod 4; otherwise ek≥dp, contradicting ek≤2d(p+4d)/(4d−1)<dp. Squarefree d and both p-inequalities matter. |
| ORD | CORRECT | A is prime to 2dp, and its ideal uses only one prime above each split rational prime. All powers remain primitive. If A^m=(x+y√−dp), y=0 would force a rational primitive principal ideal, hence norm 1; impossible since A≥3. Therefore A^m≥dp. Apply also to the B representative. This is an order/norm lower bound, not a no-generation theorem. |
| WORD | CORRECT | For primitive integral invertible ideals s,t in one class, s·conj(t)=(x+y√−dp). Norm product<dp forces y=0; comparing contents in N(t)s=xt forces s=t. Choose t a least natural representative; SR supplies the stated sufficient uniform cutoff. The bound dp/m(g) is not generally asymptotic to √(dp/2). Identity hits remain possible and can be constructive. |
| REP | CORRECT | In p=x²+4da², gcd(x,2da)=1. Every prime factor of N_a=x²+8da² has χ_{−8d}=+1. If a is even, the tied modulus contains 8d, contradicting A≡−1. If a is odd, p≡1 mod 8 forces d=2d′; use the odd character χ_{−4d′} instead. This kills precisely the named fibre, not shifted fibres, alternate d, or representation-dependent class maps. |
| SLICE / invariant moves | CORRECT, scoped | The three factorisations follow directly from xyz−x−z=n. Swapping and τ preserve the presence of a 1; for z=1 and x,y≥2, τ requires xy−1∣y−x, hence x=y. μ is confined to trivial words. The rational-scaling classification is correctly only Assessment; no non-fibred classification follows. |
| Seed-family/null evidence | CORRECT-WITH-FIX | Counts and the reported full-sample X contrasts reproduce. State explicitly that X covers α≤5000 and is a fitted descriptive contrast, not an equivalence test proving “the rate is fixed by norm.” Coverage is a different statistic: GEN2,d=2 still departs. |
| Item 3 / item 4 exclusions | CORRECT-WITH-FIX | K-GEN3 fires only for d=1 as reported. K-GEN4 is established for the implemented word subgraph, not the registered combined graph. Neither a subgraph disconnection nor a factorisation parametrisation excludes paths through additional Type II vertices. |

Source check: read Cox's original scanned text, Theorem 3.15 and assigned-character discussion (pp.54–57), Theorem 7.7 (p.137), Lemma 7.14 (p.140).
The sources support genus classes modulo squares and the ideal norm/conjugation identities, including nonmaximal orders; no maximal-order hypothesis was silently substituted.
Verified PDF: https://www.math.utoronto.ca/~ila/Cox-Primes_of_the_form_x2+ny2.pdf .

## Numerical reproduction

- `scripts/z70_xrev_gen_audit.py` records the predeclared checks and reproduces the independent audit; export the reviewed branch plus its scripts/screens to `/tmp/xrev_GEN`, unpack the two archives into `raw/` and `screens/`, then run modes `aggregate`, `fresh`, `rep`, `screens` with uv/cypari2.
- Fresh item-1–3 runs: first/middle/last prime of each W1/W2/W3, all five d: **45/45 agree**. PARI generator coordinates can change; compare invariant 2-primary orbit occupancies, not their coordinate labels. Floating sums agree within 10⁻¹⁰, not necessarily byte-for-byte.
- Independent integer enumeration at p=100057 gives h=(168,532,420,476,630) and solution counts (22,16,4,2,0), matching PARI and the small-fibre engine. This checks five groups, not unconditional completeness of every group in the campaign.
- The existing exhaustive-engine validation reruns **249/249**, output identical. Both pooled W12/W3 files reproduce byte-for-byte from the archived records.
- Independently recomputed W3 X hit z, d=(1,2,3,5,7): RED=(−1.297,+.327,+.416,−.753,−.025); CYC=(−.272,+.269,−.917,−1.075,+.600); GEN2=(−.459,−.674,+.574,−.407,+.204). W12 maximum |z|=1.748. These match the memo's rounded bounds.
- W3 dropped α>5000 units: RED=(0,18,1058,1026,1550), CYC=(0,11,507,2059,1798), GEN2=(0,0,0,56,0). In particular X scores 230 of 232 CYC d=3 hit classes and 138 of 142 at d=5: the excluded tail is not literally covered by the claim.
- GEN2 seed identities reproduce: W3=(4062,2762,1214,1874,500), all hits; W12 also all hits. GEN2 unions **584/591**, **1543/1561**, failures entirely in 𝔐. The archived total is **16,078,910** target-genus seed ideals with zero FR violations; the 45 fresh runs independently check a sample, not that entire enumeration anew.
- Direct integer-square enumeration, independent of `qfbsolve`, finds **8088** canonical fibres, all barren: counts (2152,2152,2152,565,1067).
- Recomputed **234/234** F2/F4 pairs' solution and good-class counts, with exact agreement. Checked each raw file against the actual screen input sets. F2,d=2 has no c=1 solution; direct factorisation of 8p+1 also finds none.
- Graph reruns: n=73 has 23 words/8 certificates/0 mixed components; n=409 has 39/8/0. Outputs agree with the stored records. I did not rerun all 34 word graphs.

## Falsifier table

| Screen | Checked conclusion | Impact |
|---|---|---|
| F1 odd squares | Census rerun identical: 648 admissible pairs, zero solutions; GW's contradiction also proves the square obstruction. | A necessary negative control, not positive evidence for a generative mechanism. |
| F2 C-even/R₈ | All 12 have G₂≠∅ away from c=1; 24 pairs give AMB/RED/CYC/GEN2 hits 0/0/30/36. | Empty c=1 does not mean empty Type II fibre. No positivity or odd/even separation follows. |
| F3 composites | Census rerun identical: 281/285 have a solution at a tested coprime d; exceptions 57,345,2305,4545. | Seed families were NOT run. Thus no prime-versus-composite discrimination of those families was measured. |
| F4 hard primes | 42 primes, 59 empty pairs/210; hits 0/36/110/210. All-family, all-d failures are exactly 3361,2094481,85664329. | Concrete counterexamples to these finite menus as universal covering rules. They do not refute other generative maps. |

## Operational definition and deviations

Independence from G, small output and full observed coverage form a reasonable **candidate screen**, not a formal definition of mathematical generation.
Coverage conditional on G_d≠∅ does not prove fibre positivity; a universal construction must select d or separately prove the chosen fibre nonempty.
The criterion must allow an independently specified identity that constructs a natural ideal: WORD cannot turn successful construction into disqualification merely because it realises a divisor event.
“Blind” here means no detected excess against a particular null. Matching exact α can remove a genuine, useful small-norm mechanism; equal average hit counts also do not imply equal coverage or exclude a better selection rule.
A1/A2 code is visibly in `c7a1a785c` before the results commit, so the late prose commit does not invalidate the arithmetic. Git does not prove actual execution order or the claimed tool race.
The D2 exact-α/coverage analyses and W3 entered git together: their purported pre-W3 registration remains author-reported. D9 is a corrected reanalysis, not a new independent confirmation; retain descriptive labels or preregister a fresh window.
D6 is a substantive omission: the full Type II graph/cross-coordinate paths remain open. D5 likewise leaves the promised composite-family screen incomplete. Honest disclosure saves the narrowed verdict, not completion of those tasks.
GRH-conditional completeness is honestly disclosed. Individual ideal equalities are unconditional; aggregate denominators, ranks and exhaustive seed-family claims retain the class-group completeness qualification.

## Uncovered generative candidates — concrete tests, not endorsed leads

1. **Mixed nonresidue words with root-sensitive selection.** At each (p,d), take the first three split primes in each genus; form exponent words in {−2,−1,0,1,2} of support≤3, retain the target genus, and output four distinct classes ranked by |b|/a of their reduced forms. Freeze tie-breaking before a fresh window; test union coverage, output fraction and exact-α contrasts on primes and F1–F4. This is neither CYC nor GEN2; aggregate smooth-orbit deficits do not exclude a selected subset, especially beyond WORD's free region.
2. **Halving with an odd-part anchor.** Choose the least split prime in the principal genus whose class has nonzero odd component; enumerate 2x=h and 4x=h, retaining target-genus classes, with a fixed small root-based ranking. Test coverage on all inputs, including absence of such an anchor as failure. GW(d) permits these shifted 2-primary cosets; S_RED tested only the zero odd-part coset. A subset of S_RED alone cannot repair its already-observed coverage failures.
3. **Representation-neighbour seeds.** For d=1 and p≡1 mod 8, compute p=x²+4a_c²; at positive a=a_c±1 choose the least prime factor q of p+4a² with (q/p)=−1, and output [(q,2a+√−p)]. No tied-residue test is used in choosing q. Test the frozen two-class rule and fixed alternate-d extensions on fresh primes/hard zeros; score absent q as failure. REP excludes a_c, not its neighbours, and WORD permits constructive identity hits. At squares a Jacobi −1 filter gives no seed.

## Required fixes, in priority order

1. Keep the conclusion “no tested rule found,” but distinguish **exclusion** (GW kernel, AMB, REP fibre) from **constraints** (ORD, WORD). Explicitly allow constructive identity hits; remove the §7 blanket statement that “always-present seeds lie in the kernel,” false for the nonresidue seeds and some ambiguous classes already studied.
2. Qualify exact-norm claims by α≤5000 and descriptive/non-calibrated status; mention the coverage exception in compact summaries. Do not promote the author-reported W3 chronology into independently verified preregistration.
3. Label the combined item-4 test incomplete and K-GEN4 as a modified word-subgraph result, including in proposed FRONTIER text. Keep composite seeding untested; completing either omission is optional for this narrowed verdict, mandatory before claiming the original tests passed.
4. Add GW(c)'s missing nonempty-fibre size argument and GW(b)'s invertibility qualifier at conductor primes; distinguish the uniform sufficient √(dp)-scale cutoff from the class-dependent dp/m(g). Replace “primality enters only as existence of a nonresidue” by “the genus obstruction uses nonsquareness; primality also supplies dictionary coprimality.”

**Final: ACCEPT-WITH-FIXES.** The five scoped statements survive hostile checking; the numerical negative result survives. No theorem excludes all generative maps, and no result settles ES.
