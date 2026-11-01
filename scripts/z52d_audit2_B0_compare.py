# Phase 2: write data/z52d/audit2/compare_B0.jsonl from Haiku Pass-2 records + Opus blind records + verdicts below.
import json
H={json.loads(l)['mid']:json.loads(l) for l in open('data/z52d/audit2/haiku_B0.jsonl')}
O={json.loads(l)['mid']:json.loads(l) for l in open('data/z52d/audit2/opus_B0.jsonl')}
V={
"Z2112":("MISS-MAJOR","Haiku read only the abstract and never formulated the ES semi-integral question. Doing so is cheap: Thm 2.15 applies verbatim (same boundary triangle as Markoff), strict Darmon-2 points are solutions of ES_{nq²} with the q-part in one coordinate, abundant for n ≥ 2, and at n = 1 they are exactly the Type I solutions of odd squares (empty by T1) while Campana points exist. That is a nontrivial calibration, though not an ES lead."),
"Z2764":("HAIKU-BETTER","Haiku built the item's own fixed-p complex (words of p, shared coordinate), found it F₂-acyclic for p ≤ 120 and showed Smith's forced fixed points are trivial σ-invariant edges, which explains more precisely than my off-target all-n' complex why Smith is empty. Haiku did miss that invol_topological.md Lemma T already covers Smith-type arguments."),
"Z1116":("AGREE","Both collapsed the fixed-p solution complex (a forest) to its components; Haiku used a larger range (211 primes ≤ 3000) and I added a share-a-denominator move complex. Same conclusion."),
"Z2210":("MISS-MINOR","Haiku listed the squarefree non-representables of xy+yz+zx but left the ES side undone and missed the repo coverage (bsG_ternary_weinberger E_W vs idoneal; z31 §4). The ES split of the U(n) exceptions (odd squares + 4 squarefree / 2 squareful sporadics) adds nothing of importance."),
"Z0508":("AGREE","Same literature check (Knill 1606.05958, Giannitsi 2309.14249); I also verified Mitsui 1960, which changes nothing."),
"Z2485":("AGREE","Haiku tested the class-number-parity hypothesis empirically (400 (c,d) pairs, 609 primes) and caught its own pseudo-significance artifact; I gave the structural reason (only genus/norm characters see f mod 4cd; covered by gon_fermat (i), bsB_rayclass_norm_pullback §2). The routes differ but are equally informative and reach the same verdict."),
"Z2929":("MISS-MINOR","Haiku ran tangential level-sum numerics and evaluated no Kloosterman sums. The item is covered with a proof (z30_sl2_double_coset Prop 6.1: Σ_c S(m,n;c) with fixed frequencies never arises at fixed p; even Linnik–Selberg loses p^ε), so Haiku's 'nothing' is right but lacks the reason."),
"Z2858":("MISS-MINOR","Haiku did not extract the constants. Plugging in Treviño's 0.9p^{1/4}log p gives an explicit level bound for p ≡ 1 (8) and exposes that for p ≡ 5 (8) ℓ(p) is the least ODD prime QNR, which needs a constant-string argument. Routine bookkeeping, so nothing important lost."),
"Z1849":("MISS-MINOR","Haiku did no word enumeration and gave no pointer. The sought invariant is exactly χ_{−t}(tu−1) = −1 (BL's class), proved in LOWERTAIL_ROUND2_FABLE §1.3 and verified here on 89 590 words; the verdict is unchanged, but the record lost the precise identification."),
"Z2036":("MISS-MINOR","Haiku checked the identity and enumerated signed solutions of 4/13 but did not attempt the move and missed that the programme is covered: the signed seed component is sterile i.o. under H (FORMAL_CLOSURE Thm F), and chords/Cremona moves fail (graph_cayley_moves). Verdict unaffected."),
"Z2667":("AGREE","Identical key finding: Ellenberg–Venkatesh needs codimension ≥ 7, while binary-in-ternary is codimension 1. I added the bsD_genus_vacuity_LDp coverage pointer."),
"Z2726":("MISS-MINOR","Haiku did the T₂ coset multiplication on one word (det 2, not words) and stopped at 'normalisation unspecified'. The only SL₂-preserving move, conjugation by diag(ℓ,1), is the trivial scaling word of p → word of ℓp and never goes ℓp → p, which answers the item; nothing important lost."),
"Z0447":("AGREE","Both treat it as reference-only; I noted the category mismatch (twin primes is an infinitude statement, not an every-n count), a minor addition."),
"Z3053":("MISS-MINOR","Haiku computed hit counts and found no propagation but missed the proof that none can exist: ES is linear in each variable, so it has no Vieta involution and fibres are single points (cayley_markoff_cm P3; apollonian_reciprocity). Same verdict, weaker record."),
"Z2238":("AGREE","Both say this is S₃ bookkeeping; I added that at p ≡ 1 (4) coordinates are always distinct (WINDMILL Lemma 4, 0 repeats among 8 334 solutions), which only strengthens 'nothing'."),
"Z2467":("AGREE","Both find that Skorobogatov–Sofos (100% of polynomials by height) does not transfer to a pointwise ES statement; my extra remark (it cannot unconditionalise POINTWISE_SIZE Thm C) is minor."),
}
assert set(V)==set(H)==set(O)
with open('data/z52d/audit2/compare_B0.jsonl','w') as f:
    for l in open('data/z52d/audit2/blind_B0.jsonl'):
        m=json.loads(l)['mid']; v,why=V[m]
        f.write(json.dumps({"mid":m,"batch":H[m]['batch'],"haiku_outcome":H[m]['outcome'],"opus_outcome":O[m]['outcome'],"verdict":v,"why":why},ensure_ascii=False)+"\n")
from collections import Counter
print(Counter(v for v,_ in V.values()))
