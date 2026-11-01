#!/usr/bin/env python3
"""Render the <=150-line decision memo from reviewed cluster/audit records."""
import json
from collections import Counter
from pathlib import Path

OUT = Path('data/z52d/avenue/rank_A')

# Deliberately written judgements, not an LLM-grade copied from the source layer.
LINES = {
'A01':'A fixed-p class-filtered cancellation saving is the best analytic target; repair false two-sided polylog estimates to one-sided bounds.',
'A02':'Bounded-exponent Fourier obstruction is an exact handle; need a new inverse theorem AND an arithmetic exclusion, not subgroup generation.',
'A03':'Full Pell-cycle roots remain open; norms-as-windows and the already-tested one-step recipes do not work.',
'A04':'An explicit wrong-class→other-line switch could prove coverage; no map exists yet, but “circular” was an unjustified dismissal.',
'A05':'A growing, character-sensitive LP/identity minorant is not refuted by T1; no nontrivial positive constraint library is supplied.',
'A06':'Eventual polylog winning level C is open; it is stronger than (★), not the false polylog witness-MODULUS claim.',
'A07':'Polylog HC/U-vertex/e-window bounds are distinct open strengthenings; never bound all denominators or both endpoints by polylog.',
'A08':'Bilinear/entropy lower tails might beat the CRT exceptional-set cap; no arithmetic independence/comparison theorem is supplied.',
'A09':'A verified recurrence/forced budget for 15·2^s+1 is the likeliest positive theorem; it covers one family, not general primes.',
'A10':'Full-factor-multiset compatibility is precisely §7.6; no non-CRT axiom A yet separates actual from adversarial factorisations.',
'A11':'Well-founded transport remains open; an explicit non-scaling move exists, but no uniform rank/coverage lemma does.',
'A12':'Integral Y–Δ needs a terminating normal form, not rational network equivalence; no such invariant is specified.',
'A13':'A 4-specific short-gap exception successor would contradict known density bounds; no propagation law is known.',
'A14':'Non-affine parity/group forcing is not universally excluded; no independently countable set with a certificate-producing action is given.',
'A15':'Smith/Morse/index forcing lacks a concrete complex and square-sensitive index computation; keep as unconstructed.',
'A16':'Sparse CM/lattice targets are not refuted by B3; current estimates do not resolve the required target scale.',
'A17':'Complementary hardness regimes need proved success on BOTH sides; least-QNR statistics alone supply neither.',
'A18':'Question R/theta reciprocity is existing §7.11; prime exclusion and integral existence are extra, unproved steps.',
'S01':'Exact exponent-two subgroup/character failure taxonomy is bankable; it stops being equivalent to bounded products outside t|24.',
'S02':'Fixed-level prime/joint failure densities are worthwhile but not automatically known; verify the half-dimensional lower-bound hypotheses.',
'S03':'Chain solutions iff p+1 has a 3 mod4 prime factor: a clean elementary restricted-family theorem, not its conjectural prime-density add-on.',
'S04':'Coprime denominator pair iff p+4 has a 3 mod4 prime factor: an explicit López d=1 subfamily criterion.',
'S05':'No-3 failures {3,241} are a genuine global classification question; all eight 241 solutions checked, but 241 is NOT locally obstructed at 3.',
'S06':'Allowed-denominator residue sets admit finite local classification; local admissibility does not prove global restricted universality.',
'S07':'A uniform growing-Q local-factor floor could calibrate worst cases; first define the joint factor beyond its first-order fitted expansion.',
'S08':'Compute secondary coefficients of M0 with the shifted hyperbolic boundary; useful constants, no actual-count lower bound.',
'S09':'Explicit BM/QNR thresholds are feasible bookkeeping; the divisor class inside the positive coset remains missing.',
'S10':'Effective 3/4 exceptional-set constants need an exceptional-modulus deletion lemma; a concrete partial theorem, not ES.',
'S11':'A two-dimensional sieve for a²+b⁴ could give thin-set almost-all ES; ambient density one does not imply it.',
'S12':'Prove sharp low moments rather than promote numerical variance; positive-density coverage is already weaker than the frontier.',
'S13':'Average-count/AP asymptotics may sharpen constants; fixed-Q secondary depression need not persist as a constant fractional deficit.',
'S14':'Beyond-1/2 progression estimates with moving residues are genuinely difficult and may not improve the CRT supply exponent.',
'S15':'One solved prime per short interval needs matching family/AP hypotheses; unrestricted BHP does not establish the optional mod840 claim.',
'S16':'S-integer positive ES has an elementary Dirichlet/unit proof; unbounded unit powers give no transport back to Z.',
'S17':'Depth-one weighted ℓ/z is proved for ℓ≡3 mod4 only in this layer; ℓ≡1 mod4 is not “easy” without a cover.',
'S18':'Totally-positive unit classification is plausible; a congruence at ONE split prime ideal does not imply divisibility by rational ℓ.',
'S19':'Large-q function-field prime tuples may remove H for a fixed obstruction system; check separability/admissibility and order of limits.',
'S20':'Function-field average counts need a specified model and enough variables; no integer transfer or current matching theorem.',
'S21':'Exponent coverings for new I3 families are cheap positive sibling work; keep small exceptions and the missing ES coordinate restriction.',
'S22':'The complete 9/n exception list is worth a bounded cover search, but absence of T1 does not make universal coverage likely or proved.',
'S23':'A correct long-chain characteristic/Gauss-sum sign formula is concrete algebra; it does not produce a short word.',
'S24':'Triangle sandpile construction is conditional on a small-prime-in-coset bound (GRH suffices eventually), not an established unconditional rung.',
'S25':'Evaluate BM classes on the six negative-deformation failures; a concrete sibling test, not a new ES obstruction.',
'S26':'Bounded-degree curve/identity classification can reach Mordell-hard classes; nonconstant Type I cases remain open.',
'S27':'Sharper witness-scale lower bounds need both a Haar theorem and prime transfer; do not move exponents between coordinates.',
'S28':'Verify Lenstra/Coppersmith thresholds for large-level census acceleration; algorithms decide existence, not ensure it.',
'S29':'One held-out local-hardness/residual-model audit subsumes nineteen correlations; results are EVIDENCE, not positivity.',
'S30':'Exact local densities are finite valuation/Hensel calculations once defined; local main-term data are not a global count.',
'S31':'Certificate-shape averages need a chosen measure; minimal witnesses are not uniformly distributed samples of all witnesses.',
'S32':'Upper-tail order bounds may be refined; matching rough bounds do not establish the source’s exact limiting constant.',
'S33':'Cap transference may improve constants under W; neither the hypothesis nor the cap-0 gap disappears.',
'S34':'Primitive Type-II p=4ab-(a+b)/m is a distinct restricted target; exact parametrisation/census cheap, universal positivity hard.',
'S35':'All-even converse is a genuine transport question; the necessary 2-adic valuation pattern does not prove it.',
'S36':'M=1 power-of-two-denominator failures are certified; all fixed M needs a new argument because the exponent adapts to p.',
'S37':'Prove the six ±square mod4 unit-sum classes in Q(√5); finite-box evidence is not a classification theorem.',
'S38':'Function-field length≤3 is a separate open model target; bounded CF digits are not bounded length.',
'S39':'Polynomial section counts require an actual compactification/count theorem; they are not the same as average target counts.',
'S40':'Identify the cluster fibre and integral boundary exactly before importing Harpaz; non-density is not nonexistence.',
'S41':'Define the G4 short-word sign/square law precisely; a useful sibling only after the dictionary is exact.',
'R01':'Eventual lower tails/SQ/augmented-graph targets without input remain targets; coprime composite SQ has documented counterexamples.',
'R02':'Torsor/BM/ray-class dictionaries and unspecified HIT covers lack integral existence; known-true labels concern only the dictionary.',
'R03':'An unspecified norm order, Selmer group or class-group contradiction is not known-false, but supplies no object to investigate yet.',
'R04':'Gaussian/matrix projections lose unit-fraction integrality; no constructive transport is given.',
'R05':'High fibres just rescale the gap without an independent estimate; the displayed amplifier also demands a false two-sided polylog bound.',
'R06':'No class-sensitive interlacer is constructed; zero-free exp(-β)→0 refutes the proposed finite-temperature inference.',
'R07':'Lucas rank, smoothness, subgroup generation and identity recursion do not yet force the bounded target class; preserve this formal hatch.',
'R08':'Scale/digit induction has no invariant; the proposed blanket Cobham exclusion is also unjustified.',
'R09':'Residue-Haar rigidity fails along Dirichlet square-mimicking subsequences; a new ambient measure would need quantitative sparse-target control.',
'R10':'Bloom/PP/Burgess density inputs miss prescribed sparse three-term targets; a hypothetical new structured lemma is not universally refuted.',
'R11':'Long words/extra terms have no known integral collapse; do not replace “unknown” by “impossible.”',
'R12':'Already-known average coverage is not a new avenue; restricted prime-level/height versions require separate proofs.',
'R13':'Free local, class-free and QNR prerequisites still need the class/lift; source inverse-sum interval thresholds are unverified.',
'R14':'Finite censuses, sibling maps and primes inside thin sequences supply diagnostics, not a new every-prime bridge.',
'R15':'Weak Fermat congruence loses the divisor class: explicit p=409 counterexample; corrected form is only the old dictionary.',
'R16':'Four DISTINCT denominators ≤Cp is a false large-prime target by the elementary p-adic height obstruction.',
'R17':'Maynard does not automatically make the distinguished base variable p prime; withdraw the asserted unconditional many-dead-level corollary.',
'R18':'No valid IOpen countermodel is supplied; polynomial rings and coefficient extensions require independent model-theoretic checks.',
'R19':'Finite QNR-class covering is blocked in scoped r-generic cases; the unrestricted QNR⇒ES implication is not thereby false.',
'R20':'Partition regularity varies the target w and cannot settle prescribed p; killing degenerate colour solutions does not settle regularity.',
}

PLANS = '''## Six 1-day lanes (top six in band i)
- **A01 — fixed-p cancellation.** Hours 0–3: derive the exact smoothed dyadic trial sum and its dual, retaining m=4uC−1, boundaries and p fixed (PARITY_AUDIT §2; ET Prop 1.7). Hours 3–6: track conductor/dual length in one off-diagonal block; 6–8: prove or refute a specific p^{2/5−δ} block bound. Change picture: an actual class-aware power saving; a long dual or an averaged estimate closes only that transform, not the avenue.
- **A02 — inverse obstruction.** Start from Z3003’s already-checked Fourier identity, not a repeat of its random identity test. Enumerate small cyclic groups/exponent boxes to test the NEW claim “every missing −1 with full generated subgroup has an order≤B character carrying ≥η of normalized Fourier mass”; use the known (p,q)=(31121,43) obstruction as a control. Then test the surviving formulation on arithmetic windows. Change picture: a nontrivial inverse lemma plus arithmetic scope; diffuse counterexamples reject bounded-order reduction, not all Fourier methods.
- **A03 — cycle components.** Reuse the six failures of Z0596’s one-step test; first define full-cycle roots and prove a finite bound for the relevant F_p component enumeration. Stream their complete components and size-matched controls, with big-integer bit and vertex caps reported as censored, never as failures. Change picture: an exact prime-sensitive attachment/descent lemma; another small one-step census does not change it.
- **A04 — switch between lines.** Write both divisor dictionaries and parameter bounds from B1_LINE. Choose a low-degree map ansatz on wrong-class factor pairs; solve its coefficient identities and integrality conditions before extending data. Test at all stored (★) zeros and b=1 zeros 193,2521,66529. Change picture: a uniform defect identity with positive residual mass; a fitted bijection on existing successes is insufficient.
- **A05 — positive dual.** Inventory existing W(n)/finite-identity constraints and exclude any row that already encodes the target count. Form a sparse rational LP for one growing-level toy (≤2000 variables), using only separately proved character-sensitive constraints, with a prime and an odd-square control. Extract and verify an exact dual certificate or a feasible zero-target assignment. Change picture: one genuinely new prime-sensitive minorant; T1 alone cannot force the prime LP optimum to vanish.
- **A09 — named thin family.** Read EXP_15’s open u≡7 mod8 branch and recover the ACTUAL proof certificates of 3·2^s+1, not minima. Fit one residue-class recurrence as a guide, then symbolically verify it and its positivity/divisibility; try the same ansatz on 15·2^s+1 or 4^s+297. Change picture: a new all-exponent identity or rigorous obstruction to that ansatz; numerical recurrence fits and unproved primality do not count.
All proposed experiments: ulimit -v 4000000, explicit timeout, streamed/batched data; first inspect existing scripts to avoid repeating tests. An eventual theorem needs an effective threshold and a check reaching it before claiming full ES.
'''


def main():
    data = json.loads((OUT/'clusters.json').read_text())
    selection = json.loads((OUT/'selection.json').read_text())
    audits = [json.loads(l) for l in (OUT/'negaudit.jsonl').read_text().splitlines()]
    assert {c['id'] for c in data['clusters']} == set(LINES)
    lines = [
        '# Independent ranking A — ES remains OPEN',
        'Assessment throughout; exact finite checks are CERTIFIED. No other reviewer’s files were consulted.',
        '',
        '## Selection and negative audit',
        f'- Source: {selection["source_rows"]} rows, PILOTH excluded; gates: 115 / 76 / 53, union 221; audit adds 29 unique rows → **250 candidates, {data["cluster_count"]} clusters**.',
        '- Selection is literal and keep-biased: `none (...)` differs from `none`, so explanatory no-yield/no-ingredient rows survive. They are re-judged, not sold as positive candidates.',
        '- Seed **52041031**; 40 of 1,308 plausibility-0 negatives, stratified over all 28 batches (1 per batch, 12 seeded extra allocations; uniform sampling within batch). No harder-than-open row happened to be sampled.',
        '- **12/40 = 30% strict verdict overturns; 18/40 = 45% partial/scope corrections; 10/40 upheld.** Broad negative-label defect rate: **75%**. Population-weighted estimates: **34.10% strict, 76.91% broad**.',
        '- These are false-negative/overrejection rates for the LABELS, not estimates of successful proof ideas. Some overturns expose a useless wrong dictionary (Z1956); no audit certifies a viable full proof. Small per-batch samples do not support a precise population confidence claim.',
        '- Strong rescues: Z1401 (prime-sensitive LP not refuted by T1), Z2080/Z2933 (failure of current estimates ≠ false theorem), Z3182/Z1964 (a constructive switch/descent ≠ its conclusion), Z2407 (an averaged theorem is not circular).',
        '- Exact checks: (★) has no hit at 409; weak Fermat condition nevertheless holds there; all eight 241 solutions meet 3 but a 3-adic-unit solution exists; an identity covers n≡5881 mod9240⊂1 mod840; non-scaling 4→5 transport exists.',
        '',
        '## Scoring',
        'Ordinal expected-proof-value proxy **S=5R+2H+2I+N−3G**: R relevance (0 none,1 ordinary partial,2 frontier-changing partial,3 full target); H plausibility 0–3; I one-day information 0–2; N novelty 0–2; G unsupported-bridge burden 0–3. Not success probabilities.',
        'Ranks are within bands; bands separate potential proof components, side theorems, and unsupported/invalid/already-known proposals. Source plausibilities are not inherited. Shared targets are clustered; inequivalent parameter restrictions are explicitly distinguished in `clusters.json`.',
        'Each line gives cluster ID, score S, plausibility H, and judgement; member mids, clean statements, FRONTIER §7/§6 mapping, exact obstacles and ingredient assessments are in `clusters.json`.',
        '',
    ]
    headings = {'i':'## (i) Possible proof components — none currently closes ES',
                'ii':'## (ii) Side theorems / bounded calibration worth retaining',
                'iii':'## (iii) Rest — not a universal kill list'}
    for band in ['i','ii','iii']:
        lines.append(headings[band])
        for c in data['clusters']:
            if c['band']==band:
                lines.append(f'- **{c["id"]}** S={c["proof_priority_score"]}, H={c["plausibility"]}: {LINES[c["id"]]}')
        lines.append('')
    lines.extend(PLANS.strip().splitlines())
    lines += ['', '## Bottom line',
              '**No new full-ES proof architecture with a demonstrated gap-closing ingredient emerges.** The source layer overrejects open mechanisms and also overlabels side conjectures “known-true.” Correcting those errors broadens the live question set; it does not make the hard step easier.',
              'Best proof-facing tests: class-aware cancellation, bounded-exponent Fourier obstruction, full-cycle roots, a genuine complementary-line switch, and growing positive minorants. Best positive-theorem bet: a named thin exponential family. ES remains open.',
              'Reproduce: `ulimit -v 4000000; timeout 60s uv run python scripts/z52d_rank_A_<stage>.py` for stages `build`, `checks`, `audit`, `build`, `clusters`, `report`, `validate` (audit requires the build sample).']
    text = '\n'.join(lines)+'\n'
    assert len(text.splitlines())<=150, len(text.splitlines())
    (OUT/'RANKING_A.md').write_text(text)
    print('report lines:',len(text.splitlines()))
    print('sample status histogram:',Counter(json.loads(l)['status'] for l in (OUT/'negative_sample.jsonl').read_text().splitlines()))


if __name__ == '__main__':
    main()
