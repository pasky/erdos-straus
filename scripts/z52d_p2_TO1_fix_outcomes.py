# z52d pass2 TO1 lint-fix: replaces the 34 flagged lines of data/z52b/pass2/outcome_TO1.jsonl with records whose step was actually run.
# Numbers come from scripts/z52d_p2_TO1_fix.py (+fix2/fix3/fix4, fib.py, ff3.py) and the earlier full enumeration.
import json
S = 'scripts/z52d_p2_TO1_'
ES = 'data/z52b/pass2/TO1/es_100000.tsv'
NUM = 'data/z52b/pass2/TO1/fix_numerics.json'
NUM2 = 'data/z52b/pass2/TO1/fix_numerics2.json'
R = {}
def W(mid, outcome, summary, evidence, not_done, nxt):
    R[mid] = dict(mid=mid, outcome=outcome, summary=summary, evidence=evidence, not_done=not_done, next=nxt, prev_outcome='none')

W('Z0314','nothing',"Checked the r4 slice count for Lipschitz quaternions: #{x: N(x)=m} = r4(m) = 8 sigma(m) (m odd), 24 sigma(odd part) (m even) verified by brute force for all m <= 60 (r4(5)=48, r4(13)=112, r4(17)=144, r4(29)=240). The QUATERNION_ES.md dictionary is a norm condition ff' = p^2 + 4c^2 d on divisor data, so a slice has at most r4(m) points and no separate r4-weighted count is produced by that dictionary.",
  [S+'fix2.py', NUM2, 'QUATERNION_ES.md §1'], "No new ES count from the r4 weighting; the quaternion slices are finite but not sum-of-r4 identities.", "Count the ES-quaternion slice points at N(x) = m against the divisor count of p^2+4c^2d.")
W('Z0322','nothing',"Brute-force search over F_3[T] for A/P = 1/X+1/Y+1/Z (X,Y,Z monic) with A in {T^2, T^2+1, T^2+T+2}, deg P <= 3, deg X,Y <= deg P+2. Proper cases (deg P > deg A) are only the 18 monic P of degree 3; there A=T^2 leaves 3 unsolved, A=T^2+1 and A=T^2+T+2 leave 2 each. The degree <= 2 'unsolved' entries are impossible for degree reasons (A/P improper), and the degree-3 results are bounded-search only, not evidence of non-existence.",
  [S+'ff3.py'], "The search is bounded (deg X,Y <= deg P+2) and does not use the bs_ff_es.py procedure, which requires char >= 5; deg P >= 4 not searched.", "Rerun the three degree-3 unsolved P with deg X,Y <= 5 to see whether they resolve.")
W('Z0337','nothing',"Applied the non-uniformity filter to the uniform divisor mechanisms (Type I/II divisor forms, which are polynomial in n): at odd squares n = m^2, m <= 99, c,d <= 12 there are 1621 Type I divisor hits, all with gcd(f,m) > 1, and zero with gcd(f,m) = 1; Type II gives zero hits. So the uniform mechanisms fail exactly at odd squares, as the filter predicts for any argument that works verbatim for polynomial n.",
  [S+'fix2.py', NUM2], "Filter applied to the divisor-form mechanisms only; the C-form and Lemma 3.1 mechanisms were not separately tested.", "Apply the same odd-square test to the C-form identity.")
W('Z0364','nothing',"Checked covering moduli: the Sierpinski/Riesel records use fixed covering sets (78557 with {3,5,7,13,19,37,73}; 509203 with {3,5,7,13,17,241}), while a Brier number needs both coverings at once. Web sources conflict on the smallest known Brier number (MathWorld gives 3316923598096294713661; an OEIS A076336 snippet gives a 41-digit value). For ES the analogous covering is the B2 divisor family with moduli d = -1 (mod 4C) over all C, and 70 of 4783 primes below 10^5 have no B2 certificate with C <= 10 at all.",
  ['BRAINSTORM/z31_small_count_pointwise.md', S+'fix4.py', 'https://mathworld.wolfram.com/BrierNumber.html'], "The sources' conflict on the record Brier number is not resolved; no covering of the 70 primes by a finite modulus set is found beyond C <= 10.", "Resolve the Brier record from the 2025 paper arXiv:2508.05942 and test simultaneous covering on the B2 family.")
W('Z0366','nothing',"Checked the n = p + F_k claim numerically with all Fibonacci values F_k >= 1 for odd n <= 10^5: 9417 of 49999 (18.8%) odd n have no representation, decade-stable (12.0%, 19.4%, 18.9%) with mean 1.43 representations. A web search for the Fibonacci covering/AP-of-failures result found only Sun's 'prime plus two Fibonacci numbers' (a different problem), so the AP claim is unconfirmed.",
  [S+'fib.py', 'web search: Sun, prime plus two Fibonacci numbers (prizeproblems.org/072)'], "The AP-of-failures claim was not confirmed by any source found; the count is only to 10^5.", "Test whether the zero-representation set is a union of residue classes mod the Pisano period.")
W('Z0370','nothing',"Confirmed the anchor against arXiv:1312.7748 ('The ternary Goldbach conjecture is true', 2013): every odd n > 5 is a sum of three primes via the circle method. The ES counts on file are polylogarithmic: mean #ES(p)/log^2 p is 0.88, 1.06, 1.14 in three ranges up to 10^5, while the ternary Goldbach main term is power-size (n^2/log^3 n), so the circle-method main term has no ES counterpart.",
  ['https://arxiv.org/abs/1312.7748', ES], "No ES-side step beyond the count comparison.", "None (anchor only).")
W('Z0371','nothing',"Checked the sibling claim against arXiv:2610.15784 ('6 powers of 2 in the Linnik-Goldbach problem', 2026): six powers of 2 suffice unconditionally and five under GRH. The batch's 'K >= 6 claimed' is therefore a published unconditional statement, not only a claim; Heath-Brown-Puchta (K >= 13) was not re-checked. The reservoir the theorem uses is a Goldbach reservoir, which the ES counts (log^2 p) do not supply.",
  ['https://arxiv.org/abs/2610.15784'], "Heath-Brown-Puchta bound not re-checked against its paper.", "None for ES.")
W('Z0373','nothing',"Calibrated the Lemoine-Levy form n = p + 2q on all odd n in [9, 10^5]: no n is unrepresented, the minimum count is 2 at n = 9, and the minimum of count/(log^2 n) is 0.17.",
  [S+'fix.py', NUM], "Only the odd-n range to 10^5; the expected-count scaling n/log^2 n is not verified asymptotically.", "None for ES.")
W('Z0374','nothing',"Proof attempt on the first lemma: an 'ES-almost' witness with a unit-fraction slack eps = 1/w is trivial, since 4/p = 1/p + 1/p + 1/p + 1/p is already a 4-term representation with slack 0, so any relaxation that allows an unconstrained unit-fraction term carries no content. The only meaningful version is a size bound on w, and the sieve gives no such bound.",
  [], "No sieve calculation for a size-bounded slack.", "Define the slack with a size bound w <= p^A and test the sieve prediction.")
W('Z0375','nothing',"Calibrated n = p + x^2 + y^2 on all odd n in [9, 10^5]: no n is unrepresented, minimum count 2 (at n = 9), minimum of count/(log^2 n) is 0.32.",
  [S+'fix.py', NUM], "Scaling in n/log n not verified asymptotically.", "None for ES.")
W('Z0376','nothing',"Calibrated n = p + squarefree on all odd n in [11, 10^5]: no n is unrepresented, minimum count 1 (at n = 11 = 5 + 6), minimum of count/(log^2 n) is 0.17.",
  [S+'fix.py', NUM], "Only the odd-n range to 10^5.", "None for ES.")
W('Z0377','nothing',"Checked prime in (n^2, (n+1)^2) for all n <= 20000: a prime is always present (zero exceptions), minimum count 2 at n = 2 (primes 5 and 7 in (4,9)), and the minimum of count/(n/log n) is 0.64.",
  [S+'fix.py', NUM], "Only n <= 20000.", "None for ES.")
W('Z0380','nothing',"Tested the 'at least one of three named families works for every p' form: the best triple of B2 classes among C <= 10 (d <= 2000) is {1,2,3}, covering 93.96% of primes = 1 mod 4 below 10^5, so no triple covers everything. The 70 primes left by all C <= 10 have no B2 certificate at all, so Heath-Brown's per-prime argument has no triple to use here.",
  [S+'fix.py', NUM], "Heath-Brown's 1986 argument was not re-checked against its paper.", "None for ES.")
W('Z0381','nothing',"Matched test: within residue classes of p mod 840, primes with above-median phi(p-1)/(p-1) have about 11% more ES solutions (mean log-difference +0.109 over 96 classes, 85% positive). This is a small-prime congruence effect on p-1 (classes mod q >= 11 are not absorbed by mod 840), so it is not evidence about primitive roots as such.",
  [S+'fix4.py'], "The control does not absorb congruences mod q >= 11, so the 11% is not isolated from them.", "Residualise on p mod q for all q <= 100 before reading the effect.")
W('Z0382','nothing',"Tested the form p = x^2 + 2y^2 (equivalently p = 1 mod 8): the raw split gives mean log #ES 4.55 (in) vs 4.89 (out), but x^2+2y^2 representability is exactly determined by p mod 8, so no residue-matched control with the class group is possible. Within the form's own congruence classes there is no separate class-group signal to test.",
  [S+'fix.py', NUM], "No class-group effect separated from p mod 8.", "None for ES.")
W('Z0383','nothing',"Matched control for p = x^2 + 27y^2 (2 a cubic residue) inside residue classes of p mod 72: weighted mean difference +0.021 in log #ES over 6 classes (83% positive). Effect size is about 2%, compared with 10% for the p mod 5 residue effect in the same data.",
  [S+'fix2.py', NUM2], "Significance was not tested formally; six classes only.", "Repeat with the cubic symbol at p mod 9 and 27 added to the classes.")
W('Z0386','nothing',"Residue-matched test of quadratic symbol patterns (p/3, p/5, p/7) inside classes of p mod 24: pattern residuals range from -0.18 to +0.14 in log #ES. OLS with p mod 24 classes plus (p/5),(p/7),(p/11),(p/13) gives coefficients of about -0.10 for (p/5) (SE 0.005), but absorbing p mod 120 (or 840) classes reproduces the same effect, so it is a congruence effect mod 5, 7, 11, not a Redei-matrix invariant.",
  [S+'fix2.py', S+'fix3.py', NUM2], "No Redei-matrix invariant (beyond the symbol patterns) was computed.", "Compute the actual 2-rank of the Redei matrix for the classes and test it inside p mod 840 classes.")
W('Z0387','nothing',"Matched control for p = x^2 + 32y^2 (the 8 | h(-4p) condition) inside residue classes of p mod 96: weighted mean difference +0.018 in log #ES over 8 classes (63% positive), an effect of about 2%. No governing-field signal stronger than the residue effects is visible in the counts.",
  [S+'fix2.py', NUM2], "Significance not tested formally.", "None for ES.")
W('Z0388','nothing',"Checked the Koymans-Milovic reference (arXiv:1705.05505, 16-rank of class groups of Q(sqrt(-2p))). The only signals in the ES counts after residue matching are the 2-4% cubic/quartic splits, so no spin-type oscillation beyond congruence classes is visible; the bilinear sum transfer was not written.",
  ['https://arxiv.org/abs/1705.05505', NUM2], "The bilinear-sum transfer to ES was not carried out.", "None for ES.")
W('Z0392','nothing',"Confirmed against arXiv:1111.0979 ('Quadratic forms representing all odd positive integers', 2011): the theorem is conditional on three ternary forms representing all positive odd integers, as the batch states. No ES-side quantity is produced by it.",
  ['https://arxiv.org/abs/1111.0979'], "No ES-side step exists in the item.", "None for ES.")
W('Z0393','nothing',"Tested the naive composition: for 300 random pairs of ES certificates (p, q <= 400), the product triple (x1x2, y1y2, z1z2) never satisfies 1/(x1x2)+1/(y1y2)+1/(z1z2) = 4/(pq) (0 hits). Quaternion norms multiply (Euler four-square), but the reciprocal identity does not, so the naive composition law is false.",
  [S+'fix2.py', NUM2], "Only naive product triples were tested.", "Search for a bilinear product law over all certificate pairs with a norm condition.")
W('Z0396','nothing',"Computed the tetrahedral sums: every n <= 2000 is a sum of at most five tetrahedral numbers, and 76 of them need exactly five. This matches Pollock's conjecture for this range; it is an arithmetic calibration and carries no ES-side content.",
  [S+'fix.py', NUM], "Only n <= 2000.", "None for ES.")
W('Z0398','nothing',"Tested representability of n <= 3000 as a sum of four signed cubes with |x| <= 60: the unrepresented n all lie in the classes 4 and 5 mod 9 (16 of 333 in each), with first exceptions 148, 284, 356. The cube bound is a limit of the search, so these are not proven exceptions; the four-cube question is open.",
  [S+'fix.py', NUM], "The cube bound 60 is a search limit; larger cubes not searched.", "Extend the cube bound to |x| <= 200 for the ±4 mod 9 classes.")
W('Z0399','nothing',"Checked Demjanenko's classes on the same data (sums of four signed cubes, n <= 3000, |x| <= 60): all n not congruent to ±4 mod 9 are represented (0 exceptions in seven classes), with exceptions only in classes ±4 mod 9. Comparison with ES: polynomial covering of 7 of 9 cube classes against 2 of 4 classes mod 4 for ES (classes 2 and 3 only), so the ES remainder is a larger fraction of the residue space.",
  [S+'fix.py', NUM], "Only n <= 3000 and |x| <= 60.", "Extend to larger n for the ±4 mod 9 classes.")
W('Z0412','nothing',"Checked the Bloom reference (arXiv:2112.03726: positive upper density forces a finite S with sum of 1/n = 1). A 3-term certificate for 4/p with all denominators odd is impossible: the common denominator is odd and the numerator is a sum of three odd products (odd), so v_2 of the sum is 0, while v_2(4/p) = 2. Positive density of odd numbers therefore does not give ES, though it does give the sum-1 identity.",
  ['https://arxiv.org/abs/2112.03726', 'proof in summary'], "The 2-adic lemma is for 3 terms; 4- and 5-term versions were not analysed.", "None for ES.")
W('Z0415','nothing',"Checked the Hensley/Bourgain-Kontorovich literature (arXiv:1107.3776, 'On Zaremba's conjecture', Annals 2014): the Hensley statement with threshold 1/2 is refuted in the stated form, and the corrected thin-orbit results concern continued-fraction denominators. ES denominators are not partial quotients of a fixed thin orbit, so the critical-exponent alphabet search has no ES-side target.",
  ['https://arxiv.org/abs/1107.3776', 'BRAINSTORM/z31_zaremba_thin_orbits.md'], "No alphabet search was run, because the ES question is not a continued-fraction orbit problem.", "None for ES.")
W('Z0422','nothing',"Confirmed arXiv:2508.05347 (squares, three fleas): no square area occurs. The analogue on the ES side is T1: no odd-square certificate appears in the divisor forms (Z0337: 1621 Type I hits at odd squares, all with gcd(f,m) > 1; zero Type II hits). The flea result is a structural parallel, not a transferable proof.",
  ['https://arxiv.org/abs/2508.05347', NUM2], "Analogy only; the flea proof method was not applied.", "None for ES.")
W('Z0427','nothing',"Tested class-number dependence: the partial correlation of log h(-4p) with log #ES(p), after regressing both on log p, is 0.154 over 4703 primes = 1 mod 4 below 10^5. The raw correlation 0.555 is mostly the common growth in p.",
  [S+'fix2.py', NUM2], "Only the discriminant -4p was tested.", "None for ES.")
W('Z0442','nothing',"Checked the Cauchy-Davenport efficiency for reciprocal sets mod prime q: the least H with {1/x + 1/y mod q : x, y <= H} = F_q is about 0.55 q for small q (q = 29: H = 15), and reaches H = 199 at q = 397 (H/sqrt(q) = 10). The sumset of reciprocals is far from the Cauchy-Davenport size, so a sumset argument gives no ES bound.",
  [S+'fix.py', NUM], "Only primes q < 400.", "Test whether the Alon polynomial method reproduces these H(q).")
W('Z0444','nothing',"Checked the Minkowski/Thue lattice first lemma on all 4783 primes p = 1 mod 4 below 10^5: the reduced lattice {(x,y): x = sqrt(-1) y mod p} always contains a vector of norm p, i.e., p = u^2 + v^2 with |u|,|v| <= sqrt(p). The representation is unique up to units, so it gives no extra ES information.",
  [S+'fix4.py'], "No ES statistic was built on the lattice vector.", "None for ES.")
W('Z0447','nothing',"Checked arXiv:1311.4600 ('Small gaps between primes', Maynard, 2013): bounded gaps between primes are proved by the sieve. The parity barrier and the sieve input do not give an ES count; the item has no ES-side step.",
  ['https://arxiv.org/abs/1311.4600'], "None needed for ES.", "None for ES.")
W('Z0459','nothing',"Computed the F_3[T] analogue of Artin's question: the proportion of monic irreducibles P over F_3 for which T is a primitive root is 2/3 (degree 2), 1/2 (degree 3), 0.444 (degree 4), 0.458 (degree 5), 0.414 (degree 6). The values stay near 0.4-0.5, consistent with Bilharz's positive-density theorem; no ES-side quantity is attached.",
  [S+'fix2.py', NUM2], "Only degrees 2 to 6 and the generator T.", "None for ES.")
W('Z0464','nothing',"Tested the composition law on targets with the naive product identity (see Z0393: 0 hits in 300 pairs). Quaternion norms are multiplicative, but certificate reciprocals are not compatible with the product, so the multiplicative norm does not carry certificates.",
  [S+'fix2.py', NUM2], "No composition law beyond naive products was searched.", "None for ES.")
W('Z0468','nothing',"Proof attempt on the fibration: fixing z = t gives (4t - p)xy = pt(x + y), a (1,1)-curve in (x,y), which is rational (genus 0). So the z-fibres of the ES surface have no L-function and no root number; a genuine elliptic fibration would have to come from another model, which was not found.",
  [], "Other fibrations of the ES surface were not searched.", "Search for an elliptic fibration by a different model of the ES surface.")

import sys
path = 'data/z52b/pass2/outcome_TO1.jsonl'
rows = [json.loads(l) for l in open(path)]
out = []
for r in rows:
    if r['mid'] in R: out.append(R[r['mid']])
    else: out.append(r)
with open(path, 'w') as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False)+'\n')
print('replaced', sum(1 for r in rows if r['mid'] in R), 'of', len(rows))
