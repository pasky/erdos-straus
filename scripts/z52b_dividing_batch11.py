from z52b_dividing_lib import C, I

I("Result: ES certificate families are strongly positively correlated (residue model), yet coverage still decays like exp(−c log³ X)",
  "Observed survivor fraction vs product of marginal miss rates (families with s ≤ X): ratio 1.5 at X = 32, 6.5 at X = 100, 4·10² at X = 316, 8.5·10⁵ at X = 1000. Survivors are far more common than independence predicts, but ln δ/(ln X)³ stays ≈ 0.028 while the independent product has ≈ 0.045–0.07.",
  "Independence fails badly — the dividing-line 'correlation' coordinate for ES is large — but in a way that only rescales the log³ intensity. This is the empirical form of the T1 shadow: families share quadratic-character conditions. EVIDENCE.",
  "Identify the correlation source: group families by the quadratic characters their residue sets lie in (χ_{−4d} cosets) and recompute the independence ratio within/between character groups.",
  ["scripts/z52b_dividing_indep.py", "data/z52b/dividing_indep_qnr.txt"], ["result", "correlation", "computation", "T1-analogue", "EVIDENCE"], "high", "cheap")
I("Result: ES difficulty tracks the least quadratic non-residue n(p) ('pseudosquare-ness')",
  "For hard-class primes < 10⁸ (n(p) ≥ 11 is forced by the classes), corr(log s(p), log n(p)) = 0.42; median least family size is 17, 29, 53, 74 for n(p) in [11,13), [13,20), [20,30), [30,50). But the overall record (s = 2814 at p = 53049049) has n(p) = 17, so n(p) is not the whole story.",
  "Primes that look like squares to many small quadratic characters are harder — T1 at actual squares is the limit of this trend. A proof route: 'ES-hardness ≤ function of quadratic-character pattern', with genuine non-squares eventually escaping. EVIDENCE.",
  "Replace n(p) by the number of primes ℓ ≤ 100 with (p/ℓ) = +1 and by the full character vector; fit s(p) with a regression or tree; look at the residual for the 2814 record.",
  ["scripts/z52b_dividing_qnr.py", "data/z52b/dividing_indep_qnr.txt"], ["result", "least-witness", "QR-shadow", "T1-analogue", "computation", "EVIDENCE"], "high", "cheap")
I("Connection: ES-hard primes ↔ pseudosquares (Lehmer, Williams–Shallit–Sorenson)",
  "Pseudosquares L_ℓ are the least non-square n ≡ 1 mod 8 that are quadratic residues modulo all primes ≤ ℓ; they grow roughly like exp(cℓ) and are used for primality proofs. If ES difficulty is driven by character patterns, then pseudosquares (and primes among them) are the natural candidates for the hardest ES inputs.",
  "Gives a concrete, tabulated family (pseudosquares are known up to large ℓ) to stress-test ES and the T1-shadow hypothesis, and links ES-hardness to a well-studied least-non-residue object.",
  "Take known pseudosquare-like primes (primes p ≡ 1 mod 24 that are QRs mod all ℓ ≤ 50, found by sieving or from published pseudosquare tables) and compute least s(p) and R(p); compare with typical hard primes of the same size.",
  ["Williams–Shallit–Sorenson (pseudosquares, check)"], ["pseudosquares", "QR-shadow", "T1-analogue", "disproof-route", "computation"], "high", "cheap")
I("Prediction: under GRH the 'sign layer' reaches n(p) ≤ 2 log² p, so if s(p) were a function of n(p) alone ES would follow — the data say it is not alone",
  "Bach's bound makes character patterns of p escape square-like behaviour by ℓ ≈ 2 log² p. If ES-hardness were controlled only by n(p) (plus bounded noise), a GRH-conditional pointwise argument would exist. The observed n(p) = 17 record with s = 2814 shows extra (class-layer) difficulty — consistent with the campaign's 'class, not parity' gap.",
  "Separates how much of ES's tail is explained by the sign layer (characters) vs the class layer; quantitative version of FRONTIER's F6/G4 split.",
  "Quantify: fraction of variance of log s(p) explained by the quadratic-character vector of p modulo ℓ ≤ 100 (linear/tree model).", ["BRAINSTORM/z31_small_count_pointwise.md"], ["least-witness", "gate-G4", "computation"], "med", "cheap")
I("Connection: Type I families carry quadratic-character conditions via f | (2a)²d + 1",
  "Every prime factor r of f satisfies (−d/r) = 1, so f lies in the kernel of the genus character attached to Q(√−d) and −f mod 4d lies in a fixed coset. Hence a Type I family at (a,d) only touches primes p with a prescribed value of χ_{−4d}(−p)·… — exactly the mechanism making families correlated and squares (all characters +1 pattern) hard.",
  "Explains both the correlation result and T1 in one line; suggests organising families by the character they test.", "Verify the coset claim symbolically for small d and list, for each d ≤ 30, which sign of (p/q), q | d, the Type I families require.",
  [], ["mech:genus", "T1-analogue", "correlation"], "med", "cheap")
I("Feature: character-sorted family covering — ES as a covering of the 'character cube' {±1}^ℓ",
  "Group certificate families by the quadratic-character pattern they require. ES then needs: for every pattern realised by a prime p (all patterns except 'all +1' for squares), some family compatible with that pattern also hits p's finer class. The coarse layer is a covering of the Boolean cube minus the all-ones corner.",
  "Makes T1 (all-ones corner uncovered) and ES (every other corner eventually covered) two parts of one combinatorial statement; the coarse layer may be provable by finite combinatorics.",
  "Compute, for ℓ ≤ 7 small primes, which corners of {±1}^ℓ are covered by at least one family with s ≤ 1000 (coarse layer), and how the fine layer behaves inside each corner.",
  [], ["feature", "T1-analogue", "combinatorics", "computation"], "med", "cheap")
C("Pseudosquare primality tests (Lukes–Patterson–Williams)", "—", "—", "proved: primality certified by pseudosquare conditions (under hypotheses)", "quadratic residuosity patterns",
  "Pseudosquares are where 'looks like a square to all small characters' is quantified; proofs use them as deterministic certificates.",
  "See pseudosquare connection item.", [], ["pseudosquares", "outcome:proved"], conf="med")
