"""z52d rank_O: cluster F by missing theorem, attach reviewer-O re-judgement, score, write clusters.json.
Scoring (explicit): EV = Y * P.
  Y (yield for ES of the strongest statement in the cluster): full ES 1.0; pointwise sub-step a proof would
    need 0.3; structural/thin-family/average/main-term 0.03; none 0.
  P (from reviewer-O plausibility 0..3): 0 -> 0, 1 -> 0.01, 2 -> 0.1, 3 -> 0.4.
    Any statement that is ES-strength (implies ES at large p) gets P = 0.002 if its plausibility is >= 1
    (an ES-strength statement with no handle is not as likely as an open sub-step with no handle).
  Superseded statements (already known in stronger form) have Y = 0 (no marginal yield).
  Ties (EV equal; all ES-strength clusters land at 0.002) are broken by
    h = handle (0 none, 1 formal escape of the named obstruction, 2 specific ingredient that plausibly beats it)
    f = cheap falsifier exists that would kill or promote the cluster (0/1).
  Tier (ii) is ordered by hand: P(provable in a ~1-week lane) x calibration value / cost (EV shown for reference).
  Tiers: (i) could be part of a proof of ES (yield ES or pointwise sub-step);
         (ii) side theorems worth a depth lane (cheap/provable/calibrating);
         (iii) the rest."""
import json, os
from z52d_rank_O_common import OUT

PV = {0: 0, 1: 0.01, 2: 0.1, 3: 0.4}
YV = {'ES': 1.0, 'substep': 0.3, 'side': 0.03, 'none': 0.0}

C = [
 dict(id='C1', name='Cancellation on the height-tied modular hyperbola (trial/dual/Voronoi/spectral forms)',
  statement='For every large prime p: #{(x,y): xy = 4Cp+1, x ≡ y ≡ −1 (mod 4C), C ≥ 1} ≥ 1 (one-sided H⁻ form: ≥ ε·M_BM(p)); first step: any bound |R(p) − M(p)| ≪ p^{2/5−δ}, or a power saving on one dyadic height block, obtained by cancellation rather than the divisor bound.',
  members=['Z1034','Z1855','Z2997','Z0211','Z1480','Z2958','Z3149'],
  frontier='§7.1 (verbatim); PARITY_AUDIT §2–3', new='Nothing new in substance: Voronoi/van der Corput-per-piece and a trace-formula-over-levels phrasing; Z1855 makes explicit that the pieces ⌈p/m⌉ = q are the pair form.',
  yield_='ES for the one-sided form; sub-step (first class-aware single-integer input) for any power saving', ytype='substep', plaus=1, h=1, f=1, tier='i',
  obstruction='tied modulus / height-dependent target (PARITY_AUDIT Remark 3.1); B3 for the full form (polylog main term needs near-total cancellation of a p^{1/2}-scale error)',
  beats='No member has an ingredient that beats it. The only unexploited structure is the coupling C = (xy−1)/4p itself (formal handle).'),
 dict(id='C4', name='Pell / reduction-cycle / E2-primitive roots for the forest or the e-slices',
  statement='For every prime p ≡ 1 (24), p > p₀, some element of the principal reduction cycle of ℚ(√p) (convergent P_k/Q_k of √p, ambiguous form), or another explicit non-quasi-polynomial primitive Φ(p) (fundamental unit, binomial/factorial data), is a root whose forest component contains a bichromatic edge (an ES₅ certificate).',
  members=['Z0596','Z0465','Z1298','Z0385','Z1687','Z1048','Z0378'],
  frontier='§7.2 (Astra open question: Pell/class-group cycle data); §3 B1 hatch E2; (J)84 Prop 4.2 kills the coprime CF-norm WINDOW use only; (J)106 kills fixed and least-QNR roots (Dickson)',
  new='Z0596: Legendre-type descent that uses primality of p (as for N(ε_p) = −1) — the one item whose proof template is a pointwise theorem at primes. CAUTION (review): the period of √p is NOT uniformly power-size: it is ≫ R/log p and can be O(1) (p = m²+1, m²+4), and near-square primes are exactly the hardest (T1 deformation). There the cycle data are a fixed polynomial recipe in m, so a B1/Hypothesis-H construction should defeat them. Reduced convergents have gcd(Q_k, P_k² − pQ_k²) = 1, so the coprime-norm window use is the only one and it is dead ((J)84 Prop 4.2).',
  yield_='ES (via ES₅)', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='B2 (each root is one tied divisor event); (J)84 Prop 4.2 for window uses; the Dickson constructions of (J)106 do not control cycle data (that is the escape)',
  beats='Formal only and only for long-period p: E2 primitives escape B1 Thm M and the (J)106 Dickson root constructions there, but near-square primes have O(1)-length cycles, and nothing ties the cycle to the class.'),
 dict(id='C2', name='One-coordinate polylog witness window (HC, least level C, Vmin, u_min, a_min)',
  statement='∃A ∀ prime p ≡ 1 (24), p > p₀: some ES certificate has its designated coordinate (forest HC(p), least Type II level over all lines, Vmin, I3 interior endpoint u, least e-slice a_min) ≤ (log p)^A.',
  members=['Z0148','Z0534','Z2017','Z3087','Z3167','Z1600','Z0847','Z1335','Z2363','Z1406','Z1850'],
  frontier='§7.2 (one-coordinate target HC(p) ≪ (log p)^A); two-endpoint/witness-modulus versions are dead (H4_NOT_POLYLOG; POINTWISE_OMEGA13 Thm 5.1); (★)-only version false at 14 primes',
  new='Nothing beyond bookkeeping; Z1600 isolates the regime C ≤ (log p)^{log 2} where τ(4Cp+1) can exceed φ(4C).',
  yield_='ES (it implies ES)', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='Landau-type single-integer lower tail; B2 at each window value; possible extension of H4_NOT_POLYLOG energy construction to one coordinate',
  beats='None. Value is as a clean falsification target.'),
 dict(id='C3', name='Parity / count-congruence / topological index (windmill family)',
  statement='For every prime p ≡ 1 (24) a p-dependent finite set S_p with a group action (involution, ℤ/m, S₃) or a mod-2-acyclic complex whose fixed points / critical cells are ES certificates and whose count is ≢ 0 by a formula that sees (·/p) (it must vanish at odd squares).',
  members=['Z2921','Z1386','Z1771','Z2609','Z3094','Z0469','Z2033','Z0556','Z3101','Z2764','Z2765','Z3027','Z0441','Z1650'],
  frontier='§6 dead end for finite affine involution menus ((J)2 Thm 6.1, CONDITIONAL on H); M5 row of B2_ACROSS_FIELDS; WINDMILL.md (~7000 weights tested)',
  new='Z3101: m > 2 group actions (not covered by (J)2); Z3094: class-number parity as the parity source; Z2764/Z2765: acyclicity/Euler-characteristic form (Z2765 notes χ reduces to D⁻ − D⁺, i.e. Theorem K data).',
  yield_='ES', ytype='ES', plaus=1, h=1, f=1, tier='i',
  obstruction='M5/T1 (count must vanish at m², so must see (·/p)); B1-type bar for finite affine menus; genus parity of h(−4p) is congruence data',
  beats='Only formally: the 4-rank of Cl(−4p) is congruential (fixed for p ≡ 1 (8)), but 8 | h(−4p) ⟺ p = x² + 32y² (Barrucand–Cohn) is a non-abelian Chebotarev condition, and the 16-rank has no governing field. Those higher 2-power layers are non-congruential parity sources, although (J)96 calls non-abelian Frobenius inert on finite witness sets. No member builds S_p from them.'),
 dict(id='C9', name='Regime split / exceptional-character dichotomy (Linnik three principles, Deuring–Heilbronn, Fourier character witness)',
  statement='Finitely many regimes covering all large p (by lnr(p), a pretentious distance, or a shared obstructing character), each with its own pointwise existence theorem; in the Linnik form: obstructed windows are killed by ONE exceptional character, which then repels success elsewhere.',
  members=['Z2940','Z3003','Z2941','Z2512','Z3002','Z2964','Z1787'],
  frontier='Reduces to §7.3 (class beyond the BM layer); regime splits by bounded congruence data are B1',
  new='Z3003: an exact Fourier identity giving a quantitative character witness for every obstructed e-slice. Rank_O limited diagnostic (scripts/z52d_rank_O_charobs.py, EVIDENCE; 9 (★)-zeros vs 27 distinct controls, Type II e-slices e ≤ 400): about half of the obstructed windows are poverty-type. Subgroup-type windows are almost all killed by an odd REAL (genus) character mod e, mostly χ_{−e} itself. Only 0–3 windows per prime are killed solely by characters of order ≥ 3, at hard primes and controls alike. The hard-prime excess of subgroup-type windows (5569, 83449, 102001, 712321) sits in the real-character layer. It does not measure Fourier concentration or common characters across windows, so it does not falsify C9; it points C9 toward §7.3/§7.4 (genus layer).',
  yield_='ES', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='B2 in every regime; B1 for congruence-defined splits; poverty (B4) dominates failures (also out_Q11 Z1596: 179/183 rich (★) level failures are poverty-type)',
  beats='No member supplies one. In the diagnostic, the obstructions that differ between hard and control primes are genus-layer (real) characters, i.e. §7.3/§7.4.'),
 dict(id='C14', name='Class forcing beyond parity (full factor multiset, Stickelberger, Lucas primitive divisors, twisted Dedekind reciprocity)',
  statement='A property 𝒜 of the joint factorisations of {4Cp+1}_C (or a Lucas/cyclotomic rank-of-apparition structure, or a twisted reciprocity law involving χ(d) of the divisor itself), provable for all large p, that forces −1 into some D_C.',
  members=['Z2818','Z1649','Z2534','Z1954','Z0250'],
  frontier='§7.6 (full-factor-multiset realisation), §7.7 (general-m Stickelberger); §6 reciprocity/Rédei forcing → parity only',
  new='Z1954: Lucas primitive divisors reduce the class mod n to ±1 with the sign a quadratic character — a genuine class-reduction mechanism, but it needs 4Cp+1 to share a primitive divisor with U_{4C}(P,Q) (restates rank of apparition) and is tautological at C = 1.',
  yield_='ES (if 𝒜 exists); closing lemmas otherwise', ytype='ES', plaus=1, h=1, f=1, tier='i',
  obstruction='CLASS_FORCING Thm 2.1 / TWO_POWER_LADDER (parity, never class); privacy of large primes',
  beats='Partially: the Lucas ±1 reduction is the only class-level (not parity-level) forcing seen in the 2,995 rows; it does not reach linear-in-p integers.'),
 dict(id='C20', name='High-multiplicity lift (B3 Remark 2.4 hatch)',
  statement='A natural lifted variety/weight with fibres ≫ p^δ over each ES solution of 4/p (e.g. solutions of 4/(pk), k ≤ p^δ, k dividing two denominators) whose weighted count has a power-size main term and power-saving error at each p.',
  members=['Z2060'], frontier='B3 "does NOT rule out" (high-multiplicity encodings); not a §7 item',
  new='Names the hatch; no candidate lift.', yield_='ES', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='B3 (fibres must be p^δ); Z3125 (lift needs enough free variables); the collapse to a sum of ES(p) indicators',
  beats='No.'),
 dict(id='C15', name='Amplified second moment over a polylog family around p',
  statement='Σ_{|n−p|≤H}|R(n) − M(n)|²|A_p(n)|² ≤ ½(M(p)A_p(p))² with an amplifier A_p built from (p/ℓ), ℓ ≤ L, H polylog.',
  members=['Z2982'], frontier='§6 fixed-p variance / level-Poisson second moment → critical ((J)103 §3)',
  new='Bookkeeping showing H must be polylog.', yield_='ES (above p₀)', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='B6 at polylog scale; amplifier is congruence data (B1); variance at polylog windows is the pointwise problem',
  beats='No.'),
 dict(id='C10', name='Propagation / closure / induction (Graham-type maps, rule Λ, Y–Δ moves, scale induction, composition descent)',
  statement='A finite set of maps T_i with T_i(n) < n and rules turning ES certificates at T_i(n) (or at smaller scales/levels) into one at n, valid for every large prime n — used with strong induction.',
  members=['Z2095','Z2809','Z1153','Z3028','Z3005','Z2351','Z3022','Z3016','Z3187','Z3115','Z0223'],
  frontier='§6 Propagation/global-positivity shapes (PROPAGATION_CLOSURE: rule Λ, integral Y–Δ "remain open"); (J)86 amplification criterion',
  new='Z3022 overturned in Task A, and Z3016/Z3187/Z3115/Z0223 in the targeted hunt: B1/Mordell–Schinzel and the thin-image argument do not cover strong induction from all smaller n (recursion depth grows with p). The real bars are privacy (affine shifts do not transport divisors; Assessment), numerator 8 (8/131), and T1 for transports that preserve Type I/II.',
  yield_='ES', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='privacy of large primes (SS8 Lemma 2.3); numerator blindness; T1 if outputs are ET-normalised',
  beats='No. Note the Z3016/Z3187 "thin polynomial image" argument is wrong for strong induction from all smaller n; the privacy argument is the valid one (Assessment).'),
 dict(id='C16', name='Positivity of an exact algebraic expression (Shintani ζ(0, 𝔞) combinations, interlacing families)',
  statement='R(p) (or a positive minorant) = Σ_j w_j ζ(0, 𝔞_j) over narrow ideal classes of real quadratic fields attached to word traces (or a real-rooted interlacing average over windows), with an independent positivity proof at non-squares.',
  members=['Z2845','Z3104'], frontier='§6 exact identities (finite fixed-level excluded; growing-level open, (J)10); §6 spectral/interlacing (displayed mechanisms fail)',
  new='Shintani cone decomposition as an exact finite handle (Z2845).', yield_='ES', ytype='ES', plaus=1, h=0, f=1, tier='i',
  obstruction='T1 (identity must see (·/p)); positivity of a signed combination = spin event (B2)', beats='No.'),
 dict(id='C6', name='Thin exponential families by recursion / exponent covering / Diophantine finiteness',
  statement='ES for all n_s = 15·2^s+1 (and 4^s+297, 4^s+33, 4^s+273), and I3 for 3^k ± 2, 5·3^k+1: certificates recurrent in s on residue classes of s, or exponent coverings, or Subspace/Bennett finiteness of the failure branch; similarly (12^m−1)/11, (8^m−1)/7 by cyclotomic factorisation.',
  members=['Z2969','Z3189','Z0417','Z2031','Z2995','Z2776','Z1557'],
  frontier='§7.8 (thin families still open), §7.17 (I3 thin families); §4 line 16 (no transfer to primes)',
  new='Berlekamp–Massey on PROOF certificates of 3·2^s+1/63·2^s+1 (not minimal ones) to find a recurrent template; Niederreiter folding for CF of a/2^k; BHV/Lucas for families with Lucas-like side numbers.',
  yield_='partial (one thin family; no transfer to primes)', ytype='side', plaus=2, h=2, f=1, tier='ii',
  obstruction='(J)22 Cor 1.5 / (J)68 Lemma 3.1 (no finite ET covering — parameters must grow with s); u ≡ 7 (8) valuation branch is a 2-adic approximation problem',
  beats='Yes for the family (recursion in s escapes the finite-covering no-go); irrelevant to primes ((J)84 Thm A).'),
 dict(id='C13', name='Primitive ES (gcd(x,y,z) = 1) as a cleaner ES-strength target',
  statement='PROVED (Z0866, elementary; rank_O re-checked numerically: 0 primitive Type I among 439 Type I solutions, p < 400): at p ≡ 1 (4) Type I is never primitive and primitive solutions are exactly p = 4ab − (a+b)/m, gcd(a,b) = 1, m | a+b. Open: every large prime p ≡ 1 (12) is of that form.',
  members=['Z0866'], frontier='not in FRONTIER (dual of (★): (★) is m = 1, primitive is k = 1)',
  new='The k ↔ m duality between (★) and primitive solutions; explains why all 110 primitive failures ≤ 10⁵ are ≡ 1 (12).',
  yield_='side (structure lemma + census); the open statement is ES-strength', ytype='side', plaus=3, h=0, f=1, tier='ii',
  obstruction='B2 (single-integer lottery with smaller mean)', beats='n/a (side theorem)'),
 dict(id='C8', name='Explicit / effective constants (BM-free layer via explicit Burgess, explicit M_BM, effective 3/4, explicit Vaughan)',
  statement='Explicit (c, p₁) in M_BM(p) ≥ c(log p)² for p ≥ p₁; explicit t ≤ 4ℓ(p) ≤ T_expl(p) with M_t^lev > 0; effective constants in E(N) ≪ N exp(−c(log N)^{3/4}) (remove the Landau–Page modulus from BV).',
  members=['Z2418','Z2858','Z2901','Z2551'], frontier='§5.2, §5.1 (not §7)',
  new='Bookkeeping only; prerequisite for any eventual "large p + finite check".', yield_='partial (explicit main terms / effective averages)', ytype='side', plaus=3, h=0, f=0, tier='ii',
  obstruction='none for the statements (B3/B6 for ES)', beats='n/a'),
 dict(id='C17', name='Numerator 9: finite covering ⇔ no sterile point (is B1 exactly T1?)',
  statement='9/n = 1/x+1/y+1/z for all n ≥ 20 via finitely many polynomial/congruence identities (exceptions exactly {2,5,11,19}); equivalently numerator 9 has no square-mimicking sterile profinite point.',
  members=['Z0735'], frontier='§3 numerator blindness (full T1 only for 4 | M; fails for M = 3,5,6,7,11,19 — 9 not listed)',
  new='Calibration of B1: if numerator 9 (no T1) is finitely coverable, B1 is "exactly T1".', yield_='side (calibration)', ytype='side', plaus=2, h=0, f=1, tier='ii',
  obstruction='a sterile point for m = 9 (unknown)', beats='n/a'),
 dict(id='C5', name='Local-factor floor at pseudosquare-type primes (main term)',
  statement='inf_p F(p) ≥ c > 0 for the RESIDUE_HARDNESS local-density factor, uniformly along p ≡ 1 (mod primorials) and p QR mod all ℓ ≤ (log p)^A; i.e. M_F(p) ≫ log²p everywhere.',
  members=['Z0671','Z2000','Z2981'], frontier='§2.2 (RESIDUE_HARDNESS; z52c); not §7',
  new='Pseudosquares as the native hardest list; first-order factor product → 1 along primorial classes (Z2000 sketch).',
  yield_='partial (main term only)', ytype='side', plaus=2, h=0, f=1, tier='ii',
  obstruction='B3 (main term only); F is itself a CONJECTURE closed form', beats='n/a'),
 dict(id='C7a', name='Non-CRT exceptional-set input from bilinear structure in (u,B)',
  statement='Type II/bilinear asymptotics for primes p = 4uBC − u − B with (u,B) in bilinear boxes giving #{p ≤ X : R(p) = 0} ≪ X^{1−δ}.',
  members=['Z2356'], frontier='§7.12 (θ > 3/4 needs non-CRT input)', new='Bilinear structure at fixed C as candidate non-CRT information.',
  yield_='partial (power-saving exceptional set; nothing at fixed p)', ytype='side', plaus=1, h=1, f=1, tier='ii',
  obstruction='B6; CRT supply cap if bilinear input reduces to forced classes', beats='Possibly (the only member addressing the CRT cap).'),
 dict(id='C7b', name='Almost-all ES on thin prime sets / short intervals',
  statement='ES (or (★)) for almost all primes a² + b⁴ (2-D large sieve, Friedlander–Iwaniec count); a (★)-prime in every [x, x + x^{0.525}].',
  members=['Z0240','Z2947'], frontier='§5.1 (extensions of the averaged results)', new='Thin-set version is new and provable.',
  yield_='partial (averages)', ytype='side', plaus=3, h=0, f=0, tier='ii', obstruction='B6', beats='n/a'),
 dict(id='C18', name='Growing-length digit/CF recursion (B1 E1 hatch)',
  statement='A finite-rule recursion along the base-b digits (or CF) of p, run ≍ log p steps, outputs a certificate for every prime.',
  members=['Z0482'], frontier='B1 "Does NOT rule out" E1', new='Z0482 proposes a Cobham-type closing lemma. It is UNSUPPORTED (review): recursions with growing registers are not finite-state, and non-automaticity of the squares does not stop an automatic set from containing them.',
  yield_='ES (formally)', ytype='ES', plaus=0, h=0, f=0, tier='iii', obstruction='T1 (the recursion must detect non-squareness); B1 if the rules are digit-local', beats='No.'),
 dict(id='C12', name='Relaxation then transport (Gaussian-cone ES, matrix ES, abelian-variety root numbers)',
  statement='(a) a relaxed solution exists at every p and (b) a natural (Galois-equivariant / ℚ-linear) map sends relaxed solutions to ℕ-solutions.',
  members=['Z0084','Z0091','Z0338','Z0424'], frontier='§6 transport of ES^{(S)}, V_φ, ES^□ → no transport; §4 line 12',
  new='Z0338 proposes a closing lemma (equivariant maps factor through the trace ⇒ B2 divisibility 2Re ξ | N(ξ)).',
  yield_='ES only via unknown transport', ytype='none', plaus=0, h=0, f=1, tier='iii', obstruction='B-fin / B2 at the transport step', beats='No.'),
 dict(id='C19', name='Question R / Rickards–Stange local-global for self-levelled SL₂ words',
  statement='Self-levelled SL₂ words obey a local–global principle up to the theta-multiplier obstruction plus a finite sporadic set, primes outside it.',
  members=['Z0416'], frontier='§7.11', new='None.', yield_='ES', ytype='ES', plaus=0, h=0, f=0, tier='iii',
  obstruction='M1a (RS-type theorems need power-size orbits; ES words are polylog)', beats='No.'),
 dict(id='C11', name='Restatements: torsor/Cox ring, BM/strong approximation, U_n ≅ U_1, fixed-level Hasse, singular series, thin-orbit collapse, meta-survey',
  statement='ES(p) ⟺ an integral point on the universal torsor / inside the BM set / with denominators dividing p; no existence input.',
  members=['Z0603','Z1670','Z2029','Z2302','Z2699','Z2700','Z2708','Z0604','Z0476','Z1891'],
  frontier='§6 Brauer–Manin, descent, strong approximation; §2.4; (J)95', new='None (status known-true = dictionary).',
  yield_='none beyond restatement', ytype='none', plaus=0, h=0, f=0, tier='iii', obstruction='B2 / M3', beats='No.'),
 dict(id='C7c', name='Moments / positive proportion / energy (superseded density statements)',
  statement='Paley–Zygmund or moment-LP lower bounds for #{p : R(p) ≫ log²p}; Σf² via incidences/energy.',
  members=['Z2362','Z2432','Z2461','Z1074'], frontier='superseded by §5.1 (density 1 with exp(−c(log N)^{3/4}))',
  new='Z2461: energy at Cauchy–Schwarz minimum (EVIDENCE) — closes decoupling.', yield_='partial (density), superseded', ytype='none', plaus=3, h=0, f=0, tier='iii',
  obstruction='B6', beats='n/a'),
 dict(id='C7d', name='Other averaged inputs (levels beyond 1/2, Type III, sieves at fixed depth, Smith/CKMP spin, Collatz/Tao, Guth–Maynard, value-set counts)',
  statement='Distribution/sieve/density statements averaged over p or n.',
  members=['Z2379','Z2400','Z2372','Z2650','Z0554','Z2490','Z1577','Z2382','Z2575','Z2597','Z2619','Z2636','Z3164','Z2601'],
  frontier='§5.1; §7.12 CRT cap (D)24 not moved by better levels', new='None that moves the 3/4 cap.',
  yield_='partial (averages; constants), superseded or cap-bound', ytype='none', plaus=2, h=0, f=0, tier='iii', obstruction='B6; CRT supply cap', beats='No.'),
]

def main():
    F = {json.loads(l)['mid']: json.loads(l) for l in open(os.path.join(OUT, 'F.jsonl'))}
    seen = [m for c in C for m in c['members']]
    assert len(seen) == len(set(seen)), 'duplicate membership'
    missing = set(F) - set(seen); extra = set(seen) - set(F)
    assert not missing and not extra, (missing, extra)
    for c in C:
        P = (0.002 if c['plaus'] >= 1 else 0.0) if c['ytype'] == 'ES' else PV[c['plaus']]
        c['EV'] = round(YV[c['ytype']] * P, 4)
        c['avenue_plaus'] = {m: F[m]['plausibility'] for m in c['members']}
        c['avenue_status'] = {m: F[m]['status'] for m in c['members']}
    order = {'i': 0, 'ii': 1, 'iii': 2}
    # tier (i) order: EV, then handle, then falsifier, then the manual tie-break encoded by list order
    ranked = sorted(enumerate(C), key=lambda t: (order[t[1]['tier']], -t[1]['EV'] if t[1]['tier'] == 'i' else 0,
                                                 -t[1]['h'] if t[1]['tier'] == 'i' else 0,
                                                 -t[1]['f'] if t[1]['tier'] == 'i' else 0, t[0]))
    out = []
    for r, (_, c) in enumerate(ranked, 1):
        c = dict(c); c['rank'] = r; c['yield'] = c.pop('yield_'); out.append(c)
    json.dump({'scoring': __doc__, 'n_F': len(F), 'clusters': out}, open(os.path.join(OUT, 'clusters.json'), 'w'), ensure_ascii=False, indent=1)
    for c in out:
        print(c['rank'], c['tier'], c['id'], c['EV'], 'h', c['h'], 'f', c['f'], len(c['members']), c['name'][:70])

if __name__ == '__main__':
    main()
