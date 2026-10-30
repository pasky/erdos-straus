#!/usr/bin/env python3
"""Render the independent free_astra idea ledger; no external dependencies."""
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "free_astra"
# title | connection | why | first_step | comma-separated tags | effort? | confidence?
ROWS = r"""
Residual factor pairs|Fixing x turns 4/p−1/x=a/b into (ay−b)(az−b)=b²; connect ES to complementary divisors in simultaneous residue classes.|This is an exact two-unit-fraction reformulation rather than a counting analogy.|For primes below 500, enumerate x up to p and record the successful residue pairs.|algebra,divisors,residues|cheap|high
Moving the first denominator|Connect changes x→x+1 with changes in the residual factor-pair problem, treating consecutive x as coupled rather than independent trials.|Neighboring residual numerators differ by four, so their divisor searches share arithmetic structure.|Tabulate success transitions between neighboring x for 100 primes.|algebra,divisors,dynamics
Denominator gcd stratification|Partition ES triples by the three pairwise denominator gcds and compare the strata with multiplicative parametrizations.|The cleared equation 4xyz=p(xy+xz+yz) imposes exact constraints on every gcd stratum.|Derive the cleared equation after writing x=ga and y=gb with gcd(a,b)=1.|algebra,gcd,parametrization|cheap|high
Primitive projective triples|View denominator triples as rational points up to common scaling, with p recovered from their reciprocal sum.|Scaling explains why prime cases are central and may separate shape from arithmetic size.|Enumerate primitive triples with coordinates below 100 and sort the resulting reduced values of 4xyz/(xy+xz+yz).|geometry,parametrization,scaling
Symmetric coordinates|Use s1=x+y+z, s2=xy+xz+yz, s3=xyz and the relation 4s3=ps2 to connect ES to integer-root cubic polynomials.|The cubic viewpoint keeps all denominator permutations together and exposes discriminant constraints.|Search small integer s1,s2 satisfying integral roots of T³−s1T²+s2T−ps2/4.|algebra,symmetry,discriminants
Discriminant squares|After fixing one symmetric parameter, require the remaining quadratic discriminant to be square; compare with Pell-type searches.|Square conditions can package an infinite family more economically than individual divisors.|Derive the discriminant after prescribing y+z and x, then identify when a Pell equation appears.|algebra,Pell,discriminants
Near-equal denominator perturbations|Write y=z+h and study the exact residual equation as h varies, connecting ES to near-square factorization.|Small h gives structured, checkable subfamilies without claiming they cover every prime.|Enumerate the smallest attainable difference z−y for primes below 1000.|algebra,near-squares,experiments
Denominator ratios as slopes|Parameterize y/z by a reduced rational slope and express the ES condition in terms of its numerator and denominator.|A rational slope organizes triples differently from fixing x and might reveal short covering families.|Derive the divisibility condition for y=ku,z=kv with gcd(u,v)=1.|geometry,parametrization,gcd
Fraction splitting trees|Connect ES identities to the elementary split 1/a=1/(a+1)+1/(a(a+1)), allowing merges as well as splits.|Length-three targets might be reached through longer identities with controlled cancellation or merging.|Generate a bounded graph of positive unit-fraction identities connected by exact splits and inverse merges.|rewriting,egyptian-fractions,graphs
Weighted mediants|Compare residual fractions from neighboring x with Farey mediants, looking for intervals where a two-term decomposition persists.|Farey adjacency controls numerator-denominator determinants exactly.|Compute Farey neighbors of residual fractions for the first 50 difficult primes.|continued-fractions,Farey,residues
Bilinear determinant encoding|Represent uv−r as a two-by-two determinant and translate ES divisor conditions into determinant equations with congruences.|Determinants bring row operations and lattice bases into a directly arithmetic setting.|Write a residual factor-pair certificate as a determinant condition and list congruence-preserving row operations.|linear-algebra,lattices,congruences
Cluster-style mutations|Search for involutions on auxiliary ES parametrizations analogous to replacing one root of a quadratic while fixing other variables.|An exact positive integral mutation could propagate certificates across a connected graph.|For three existing elementary parametrizations, solve for each coordinate and test whether another integral branch exists.|dynamics,mutation,parametrization
Vieta moves on lifted equations|Introduce an auxiliary variable making an ES constraint quadratic, then examine Vieta root exchange.|Lifting may create useful symmetries absent from the original equation, but integrality must be checked.|Try y+z=s and yz=q, derive the lifted equations, and test root-exchange closures.|algebra,mutation,lifts
Resultants between identities|Eliminate shared parameters from two valid ES families to identify their intersections and potential transition rules.|Intersections may show how families cooperate rather than merely duplicate coverage.|Compute a resultant for two small exact families found by direct denominator ansatz.|algebra,elimination,identities
Saturation and boundary components|Study the ideal of 4xyz−p(xy+xz+yz) after excluding zero coordinates and compare its components under congruence restrictions.|Removing degenerate solutions is essential before algebraic parametrizations are interpreted arithmetically.|Compute the saturation by xyz for a small symbolic specialization and inspect the nonzero locus.|algebraic-geometry,ideals,positivity
Birational chart comparison|Cover the ES surface by different rational charts and compare where integer points have manageable denominators.|One chart can hide integrality that another makes explicit.|Write charts obtained by solving for x, y, and a denominator ratio; compare their divisibility conditions.|algebraic-geometry,charts,integrality
Height functions on certificates|Compare max(x,y,z), xyz, and auxiliary-parameter height as costs on the same certificate space.|A proof-producing descent may work for a height unrelated to the smallest denominator.|For bounded triples, build move graphs and test which heights decrease along known identity transformations.|heights,dynamics,search
Logarithmic denominator coordinates|Map triples to log(x),log(y),log(z), comparing thin certificate families with the curved positive ES surface.|Multiplicative scales become additive and can expose regions systematically missed by bounded boxes.|Plot normalized log-denominator triples for primes below 1000 using several search cutoffs.|geometry,visualization,heights
Tropical balance regimes|Separate the cleared equation into regimes according to which of xy,xz,yz dominate, using tropical-style bookkeeping.|Dominant balances may suggest complementary denominator ansatzes, not replace exact arithmetic.|List possible valuation balances at a prime dividing one denominator and derive the corresponding exact divisibility cases.|valuations,tropical,asymptotics
Newton polytope viewpoints|Compare monomial supports of the ES surface and auxiliary divisor equations to find sparse elimination orders.|Sparse structure can reduce symbolic-search complexity without implying integer-point existence.|Draw the exponent support and test elimination with two variable orders in a computer algebra system.|algebraic-geometry,sparsity,elimination
Pell families from denominator gaps|Prescribe an affine relation between two denominators and ask when the resulting square condition yields a Pell family.|An infinite family of certificates could arise from a recurrent rather than polynomial parametrization.|Test y=z−h with h in 1 through 20 and classify the resulting discriminant equations.|Pell,recurrences,parametrization
Elliptic slices|Intersect the ES surface with simple quadratic constraints and check whether the resulting curves have genus one.|A useful slice could carry arithmetic group operations, although positivity and integrality remain separate tasks.|Try xy=z²+k for small k and compute the genus of the resulting plane curve.|elliptic-curves,slices,algebraic-geometry|medium
Conic bundles|Choose auxiliary coordinates that leave a conic equation over one parameter and study its local solvability and integral points.|Conics admit explicit parametrizations once a rational point is supplied.|Search linear substitutions that make one residual equation quadratic in two remaining variables.|conics,parametrization,local-global
Norm equations|Rewrite selected quadratic discriminant conditions as norms in quadratic orders and track the congruences needed for ES.|Multiplicativity of norms may combine certificates in ways raw divisor enumeration misses.|For one Pell-type slice, translate the equation into a norm and record its positivity restrictions.|norms,quadratic-fields,congruences
Class-group bookkeeping|When a divisor condition factors in a quadratic order, distinguish principal from nonprincipal ideal factors.|This identifies an arithmetic constraint that could guide which auxiliary field is useful.|For a small negative discriminant arising from a slice, compare ideal factorizations with actual integral certificates.|class-groups,norms,integrality|medium
Gaussian integer decompositions|Test whether representing auxiliary factors as sums of two squares helps impose the needed residue class.|Norm factors carry extra structure; the connection is a candidate construction, not a universal representation claim.|For small certificates with a sum-of-two-squares auxiliary factor, tabulate how Gaussian factors determine residues.|norms,gaussian-integers,residues
Quaternion multiplication as composition|Ask whether quaternion norm identities compose two partial ES certificates into a full one.|Four-square identities offer explicit polynomial relations whose congruences can be checked.|Choose a small norm identity and symbolically test whether its cross terms match an ES residual equation.|quaternions,composition,identities
Trace identities in SL₂|Connect two-by-two matrix trace identities with the campaign's word formulations and seek trace-preserving congruence moves.|Matrix words package nonlinear integer expressions into exact multiplication laws.|Derive the trace relation for three short elementary matrices and compare it with tuv−u−v.|matrix-words,traces,groups
Continued-fraction surgery|Study local replacements in continued fractions that change a certificate's congruence data without making its length too large.|Equivalent rational expansions can trade coefficient signs, sizes, and parity.|Enumerate short continued-fraction identities and label which preserve positivity and desired coefficient classes.|continued-fractions,rewriting,parity
Continuants modulo powers of two|Analyze short continuant recurrences modulo 8,16,32 and compare reachable states with the admissible coordinate classes.|Finite parity information may guide an otherwise unbounded integer construction.|Build the exact transition graph for continuants modulo 16 with coefficient residues as labels.|continued-fractions,automata,parity
Stern–Brocot ancestry|Attach each residual rational to its Stern–Brocot path and look for common terminal patterns among successful splits.|Path suffixes may encode useful divisibility conditions more compactly than numerator-denominator pairs.|Record path suffixes of length at most eight for successful and unsuccessful bounded residual searches.|Farey,trees,patterns
Euclidean quotient parity|Track parity of Euclidean quotients together with remainder size when processing p and an auxiliary parameter.|Parity-decorated Euclidean descent could interact with the required classes modulo four.|Compute quotient-parity strings for certificates found by a fixed divisor search and compare with controls.|Euclidean-algorithm,parity,dynamics
Reciprocity as a design constraint|Rather than discard square-like obstructions, use quadratic reciprocity to choose parameters with deliberately opposite symbols.|Symbols can guide which certificate family is worth trying at each prime.|For a small family, derive the Legendre-symbol necessary conditions and search complementary parameter choices.|reciprocity,quadratic-characters,search
Higher power residue labels|Decorate auxiliary divisors with cubic or quartic residue data to distinguish classes invisible to quadratic symbols.|Extra labels might reveal a constructive partition even when they do not force existence.|For primes in suitable congruence classes, compare certificate frequencies across power-residue labels.|power-residues,characters,experiments
p-adic denominator balance|Classify valuations of x,y,z at p using the cleared equation and compare branches of the classification.|The valuation constraints are exact and can reduce redundancy in parametrizations.|Derive all possible minimum-valuation patterns before searching examples for each pattern.|valuations,p-adic,gcd|cheap|high
Hensel lifting with size control|Lift auxiliary congruence solutions modulo prime powers while tracking whether representatives stay inside useful positive intervals.|Local lifting is only a component, but controlled representatives could feed a global construction.|Lift one divisor-family congruence from modulus q to q² and measure least positive representatives.|p-adic,lifting,heights
Chinese remainder optimization|Treat parameter selection as a CRT problem with a cost function on the resulting least positive representative.|Congruence compatibility and parameter size are distinct, computable parts of certificate design.|Combine three small valid congruence conditions and optimize the CRT representative by varying their residues.|CRT,optimization,congruences
Rational reconstruction|Use modular solutions plus height bounds to reconstruct candidate rational parametrizations of ES certificates.|Rational reconstruction is an exact computational tool when the bounds are justified.|For a fixed prime, reconstruct small ratios y/z from modular solutions at successively larger moduli.|rational-reconstruction,modular,heights
Lattice basis reduction for residues|Encode simultaneous divisibility and smallness conditions as an integer lattice and use reduced bases to propose auxiliary parameters.|Short vectors can suggest candidates even without an existence theorem.|Build a two-constraint lattice for one residual factor search and compare reduced vectors with brute force.|lattices,LLL,search
Geometry of numbers in moving boxes|Study certificate lattices with anisotropic boxes adapted to denominator size rather than symmetric balls.|The natural coordinates can have very different scales, affecting any useful volume estimate.|For a fixed auxiliary modulus, derive the lattice determinant and plot the feasible box as p varies.|lattices,geometry-of-numbers,heights
Fundamental domain boundary crossings|Follow a moving residue target through lattice fundamental domains as p changes and record when short representatives appear.|Boundary crossings may explain abrupt changes in the cheapest certificate.|Track nearest lattice representatives for consecutive admissible primes in one explicit two-variable model.|lattices,dynamics,experiments
Semigroup holes|Treat attainable certificate parameters under positive identity composition as an affine semigroup and inspect its holes.|Eventual saturation is a meaningful possibility even when small exceptions persist.|Generate the semigroup from a small set of verified composition moves and compute missing points in a bounded region.|semigroups,positivity,composition
Frobenius coin analogies|Compare admissible sums of auxiliary parameters with numerical semigroup conductor problems.|If a certificate construction is additive in one coordinate, conductor bounds could convert families into eventual coverage.|Find an exact ansatz with an additive free coordinate before computing its attainable residues and gaps.|semigroups,additive,coverage
Divisor posets|Organize divisors of each p-tied integer by divisibility and study where the target residue first occurs.|Poset structure may reveal that a few prime-factor toggles suffice to reach the target.|Construct divisor Hasse diagrams for 20 auxiliary integers and color nodes by target residues.|divisors,posets,residues
Subset products in residue groups|Translate selection of a divisor into selecting prime-power factors whose product hits a residue in a finite multiplicative group.|This gives an exact finite combinatorial problem once the factorization is known.|For a factored auxiliary integer, run subset-product dynamic programming and inspect unreachable residue classes.|divisors,finite-groups,subset-product|cheap|high
Zero-sum theory for divisor residues|Take discrete-log coordinates when available and compare target divisor residues with zero-sum sequence phenomena.|Multiplicative divisor selection becomes additive combinatorics in finite abelian groups.|For cyclic unit groups of small moduli, compute the exponent multiset and shortest subsequences hitting the target.|zero-sum,finite-groups,divisors
Nonunit residue handling|Separate auxiliary prime factors sharing the modulus from unit factors before applying group-based divisor heuristics.|Ignoring nonunits would make the group model false; stratifying valuations repairs it.|Implement a residue-state enumeration that tracks gcd with the modulus and compare it with unit-only counts.|residues,valuations,finite-monoids|cheap|high
Complement involutions on divisors|Use d↔N/d as an involution on candidate residues and look for forced pairs or fixed points.|The involution is exact and may reduce search or create parity constraints on failures.|For each residue r modulo a small modulus, calculate how complementary divisors transform r when it is invertible.|divisors,involutions,residues
Cyclotomic factor opportunities|Choose auxiliary parameters making a p-tied expression resemble a cyclotomic value with structured factors.|Algebraic factorization can manufacture divisors, although the required residue must still be checked.|Search low-degree substitutions yielding a difference of squares or a cyclotomic factorization in the residual equation.|cyclotomic,factorization,parametrization
Composition of partial certificates|Define a partial certificate as satisfying the equation and some integrality conditions, then seek operations that complete missing conditions.|Separating algebraic validity from integrality may make complementary constructions visible.|Create a table of rational identities with their exact integrality requirements and test pairwise compatible substitutions.|composition,integrality,identities
"""


def items():
    result = []
    for line in ROWS.strip().splitlines():
        cells = line.split("|")
        if not 5 <= len(cells) <= 7:
            raise ValueError(f"Bad row: {line}")
        title, connection, why, first_step, tags = cells[:5]
        result.append(dict(id=f"{SLUG}-{len(result)+1:04d}", title=title,
                           connection=connection, why=why, first_step=first_step,
                           refs=[], tags=tags.split(","),
                           confidence_not_nonsense=cells[6] if len(cells) > 6 else "med",
                           effort=cells[5] if len(cells) > 5 else "cheap"))
    for key in ("id", "title", "connection"):
        assert len({x[key] for x in result}) == len(result), key
    for x in result:
        assert all(x[k] for k in ("title", "connection", "why", "first_step", "tags"))
        assert x["confidence_not_nonsense"] in {"low", "med", "high"}
        assert x["effort"] in {"cheap", "medium", "big"}
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()
    records = items()
    counts = Counter(t for x in records for t in x["tags"])
    header = ["# z52b free_astra — independent free association", "",
              "ES remains OPEN. These are candidate connections, not claims of a proof or of universal coverage.", ""]
    if args.final:
        assert len(records) >= 300
        header += [f"## Summary — {len(records)} items", "",
                   "Breadth-first generation; only obvious mathematical nonsense and within-list duplicates were filtered. No campaign barrier grading was applied.", "",
                   "**Tag histogram** (overlapping tags): " + "; ".join(f"{t}: {n}" for t, n in counts.most_common()) + ".", "",
                   "**Ten especially exciting leads** (subjective exploration priorities, not correctness rankings):", ""]
        for number in PICKS:
            x = records[number - 1]
            header.append(f"- `{x['id']}` — {x['title']}: {PICKS[number]}")
        header.append("")
    header += ["## Method and coverage", "",
               "Independent free association from exact ES algebra, then neighboring mathematical structures, computational methods, physical analogies, and search organization. Every item specifies a cheap initial action; larger programs remain speculative. Items were generated without consulting the other free-lane outputs. References are empty intentionally: no unverified literature result is asserted; literature items are explicitly requests to check a lead.", "",
               "Coverage spans elementary identities, algebraic and analytic number theory, geometry, combinatorics, dynamics, physics, algorithms, machine learning, formal verification, history, and collaboration. Not attempted: executing each proposed experiment, verifying literature leads, deep feasibility ranking, exhaustive comparison with the existing brainstorm archive, or proving coverage. Bounded-data patterns are not universal evidence.", "",
               "## Candidate connections", ""]
    body = [f"{i}. **{x['title']}** (`{x['id']}`) — {x['connection']} — **First step:** {x['first_step']}"
            for i, x in enumerate(records, 1)]
    data_path = ROOT / "data/z52b/free_astra.jsonl"
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in records))
    (ROOT / "BRAINSTORM/z52b_free_astra.md").write_text("\n".join(header + body) + "\n")
    assert [json.loads(line) for line in data_path.read_text().splitlines()] == records
    print(f"Rendered and validated {len(records)} items; {len(counts)} distinct tags.")


PICKS = {}  # Filled after breadth-first generation, before final rendering.

if __name__ == "__main__":
    main()
