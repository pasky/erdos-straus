#!/usr/bin/env python3
"""Wave z52b merge lane: build the master TODO of ES connections from data/z52b/<lane>.jsonl.

Usage (reproducible build, run from repo root):
    uv run --with numpy --with scikit-learn python scripts/z52b_merge.py validate
    uv run --with numpy --with scikit-learn python scripts/z52b_merge.py pairs   # candidate near-dup pairs -> data/z52b/merge/
    uv run --with numpy --with scikit-learn python scripts/z52b_merge.py build   # master.jsonl + ES_CONNECTIONS_TODO.md

Never drops items except true duplicates. Duplicate decisions = automatic (very high text similarity)
plus manual judgements recorded in data/z52b/merge/dup_decisions.tsv (pair-level: id_a, id_b, verdict, note).
"""
import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "z52b")
MERGE_DIR = os.path.join(DATA, "merge")
LANES = ["analogues", "dividing", "fingerprint", "free_astra", "free_fable", "free_opus",
         "signature", "tools", "translate", "upgrades"]
CORE = ["id", "title", "connection", "why", "first_step", "refs", "tags", "confidence_not_nonsense", "effort"]
CONF = {"low": 0, "med": 1, "medium": 1, "high": 2}
EFFORT = {"cheap": 0, "medium": 1, "med": 1, "big": 2}


def _clean_str(s):
    if s is None:
        return ""
    if not isinstance(s, str):
        s = json.dumps(s, ensure_ascii=False)
    return re.sub(r"\s+", " ", s).strip()


def _clean_list(x):
    if x is None:
        return []
    if isinstance(x, str):
        x = [x] if x.strip() else []
    out, seen = [], set()
    for v in x:
        v = _clean_str(v)
        if v and v not in seen:
            seen.add(v)
            out.append(v)
    return out


def load(report=False):
    """Load + validate + normalise all lane items. Returns list of dicts (with 'lane' and 'extra')."""
    items, problems = [], []
    for lane in LANES:
        path = os.path.join(DATA, lane + ".jsonl")
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if not line.strip():
                    problems.append(f"{lane}:{ln}: blank line (skipped)")
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError as e:
                    problems.append(f"{lane}:{ln}: malformed JSON ({e}) — FIX IN SOURCE")
                    continue
                it = {"lane": lane}
                for k in ("id", "title", "connection", "why", "first_step"):
                    it[k] = _clean_str(o.get(k))
                    if not it[k]:
                        problems.append(f"{lane}:{ln}: empty/missing field {k}")
                it["refs"] = _clean_list(o.get("refs"))
                it["tags"] = _clean_list(o.get("tags"))
                c = _clean_str(o.get("confidence_not_nonsense")).lower()
                e = _clean_str(o.get("effort")).lower()
                if c not in CONF:
                    problems.append(f"{lane}:{ln}: bad confidence {c!r} -> med")
                    c = "med"
                if e not in EFFORT:
                    problems.append(f"{lane}:{ln}: bad effort {e!r} -> medium")
                    e = "medium"
                it["confidence_not_nonsense"] = "med" if c == "medium" else c
                it["effort"] = "medium" if e == "med" else e
                if not it["id"].startswith(lane + "-"):
                    problems.append(f"{lane}:{ln}: id {it['id']!r} lacks lane prefix")
                # lane-specific extra fields (analogues:world, signature:raw_id, upgrades:upgrade) kept verbatim
                it["extra"] = {k: v for k, v in o.items() if k not in CORE}
                items.append(it)
    ids = collections.Counter(it["id"] for it in items)
    for k, v in ids.items():
        if v > 1:
            problems.append(f"duplicate id {k} x{v}")
    if report:
        for p in problems:
            print("PROBLEM", p)
        cnt = collections.Counter(it["lane"] for it in items)
        for lane in LANES:
            print(f"{lane:12s} {cnt[lane]:5d}")
        print(f"{'TOTAL':12s} {len(items):5d}   problems: {len(problems)}")
    return items


# ---------------------------------------------------------------- step 2a: candidate near-duplicate pairs

def _ref_keys(it):
    ks = set()
    for r in it["refs"]:
        for m in re.findall(r"(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", r):
            ks.add("arx:" + m)
        for m in re.findall(r"\bA\d{6}\b", r):
            ks.add("oeis:" + m)
    return ks


def _problem_no(it):
    m = re.match(r"Problem (\d+)", it["title"])
    return m.group(1) if m else None


def candidate_pairs(items):
    """TF-IDF cosine (title+connection) always; bge-small embedding cosine if sentence-transformers is available
    (`uv run --no-project --with sentence-transformers --with scikit-learn --extra-index-url
    https://download.pytorch.org/whl/cpu --index-strategy unsafe-best-match`). Thresholds calibrated by eye."""
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    txt = [it["title"] + " . " + it["title"] + " . " + it["connection"] for it in items]
    vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english",
                          token_pattern=r"(?u)\b\w[\w₀-₉⁰-⁹]*\b")
    X = vec.fit_transform(txt)
    S = (X @ X.T).toarray()
    try:
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer("BAAI/bge-small-en-v1.5", device="cpu")
        E = m.encode([it["title"] + ". " + it["connection"] for it in items], batch_size=64,
                     normalize_embeddings=True, show_progress_bar=False)
        C = E @ E.T
    except ImportError:
        print("WARNING: sentence-transformers unavailable; TF-IDF candidates only", file=sys.stderr)
        C = S * 0
    K = [_ref_keys(it) for it in items]
    P = [_problem_no(it) for it in items]
    out = []
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            e, t = float(C[i, j]), float(S[i, j])
            shared = bool(K[i] & K[j])
            same = items[i]["lane"] == items[j]["lane"]
            if same:  # lanes already removed literal in-lane dups; only very close in-lane pairs are candidates
                ok = e >= 0.90 or t >= 0.40
            else:
                ok = e >= 0.85 or t >= 0.30 or (shared and e >= 0.78)
            if not ok:
                continue
            if P[i] and P[j] and P[i] != P[j]:  # signature lane: distinct Erdős problems are distinct items
                continue
            out.append((items[i]["id"], items[j]["id"], round(e, 3), round(t, 3), int(shared)))
    out.sort(key=lambda r: -max(r[2], r[3] + 0.55))
    return out


def cmd_pairs():
    items = load()
    os.makedirs(MERGE_DIR, exist_ok=True)
    pairs = candidate_pairs(items)
    with open(os.path.join(MERGE_DIR, "candidates.tsv"), "w") as fh:
        fh.write("id_a\tid_b\temb_cos\ttfidf_cos\tshared_ref\n")
        for r in pairs:
            fh.write("\t".join(map(str, r)) + "\n")
    print(len(pairs), "candidate pairs")


# ---------------------------------------------------------------- step 2b: clusters from verdicts + overrides

def _read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("id_a\t"):
                continue
            rows.append(line.split("\t"))
    return rows


def clusters(items):
    """Union-find over DUP verdicts (data/z52b/merge/dup_decisions.tsv), then manual group overrides
    (data/z52b/merge/cluster_overrides.tsv). Returns list of id-lists (singletons included), in lane order."""
    ids = [it["id"] for it in items]
    known = set(ids)
    groups = []
    overridden = set()
    with open(os.path.join(MERGE_DIR, "cluster_overrides.tsv"), encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            g = line.split()
            for x in g:
                assert x in known, f"override: unknown id {x}"
                assert x not in overridden, f"override: {x} listed twice"
                overridden.add(x)
            groups.append(g)
    par = {x: x for x in ids}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for a, b, verdict, *_ in _read_tsv(os.path.join(MERGE_DIR, "dup_decisions.tsv")):
        assert a in known and b in known, (a, b)
        if verdict == "DUP" and a not in overridden and b not in overridden:
            par[find(a)] = find(b)
    comp = collections.defaultdict(list)
    for x in ids:
        if x not in overridden:
            comp[find(x)].append(x)
    allg = list(comp.values()) + groups
    order = {x: i for i, x in enumerate(ids)}
    allg = [sorted(g, key=order.get) for g in allg]
    allg.sort(key=lambda g: order[g[0]])
    assert sum(len(g) for g in allg) == len(ids)
    return allg


# ---------------------------------------------------------------- step 3: merge fields, areas, flags

# Open area vocabulary derived from the lane tags (tags weigh 3, title 2, connection/why 1).
AREAS = [
    ("analytic NT", r"analytic|sieve|character.?sum|exponential.?sum|kloosterman|l-function|\bgrh\b|\brh\b|zero.?density|siegel|"
     r"bombieri|level.?of.?distribution|primes? in (an )?a(rithmetic )?p|linnik|large.?sieve|circle.?method|divisor.?(problem|function|sum)|"
     r"titchmarsh|hooley|erd(o|\u0151)s.?(hall|kac)|anatomy|smooth.?number|short.?interval|exceptional.?set|almost.?all|vaughan|"
     r"barban|chowla|dispersion|bilinear|type.?iii|mean.?value|second.?moment|burgess|least.?(quadratic|prime)|chebotarev|"
     r"pretentious|parity.?(problem|barrier)|equidistribut|deligne|weil.?bound|multiplicative.?function|transference|"
     r"dense.?model|green.?tao|szemer(e|\u00e9)di|primitive.?set|sets.?of.?multiples|diophantine.?approx|sylvester.?schur"),
    ("algebraic NT", r"algebraic.?number|class.?(group|number)|reciprocity|quadratic.?(field|form|residue|character)|ternary.?form|"
     r"binary.?form|quaternion|\bcm\b|heegner|cyclotomic|galois|\bideals?\b|gaussian|z\[i\]|eisenstein|real.?quadratic|"
     r"imaginary.?quadratic|genus|spinor|idoneal|norm.?form|fundamental.?unit|unit.?group|s-unit|legendre.?symbol|jacobi.?symbol|"
     r"quartic|\bartin|primitive.?root|p-adic|2-adic|valuation|pell|cohen.?lenstra"),
    ("arithmetic geometry", r"arithmetic.?geometry|algebraic.?geometry|brauer|manin|integral.?points?|hasse|torsor|cubic.?surface|"
     r"log.?k3|fibration|del.?pezzo|\bu_n\b|surface|variety|(?<!certificate-)\bheights?\b|strong.?approximation|descent|elliptic.?curve|"
     r"rational.?points|lang.?weil|hilbert.?irreducib|thin.?set|\btoric|blow.?up|cayley.?cubic|markoff|neron|severi"),
    ("automorphic & spectral", r"modular.?form|automorphic|theta|spectral|eigen|laplacian|expander|half.?integral|maass|hecke|"
     r"shimura|waldspurger|trace.?formula|homogeneous.?dynamics|ratner|\bque\b|linnik.?ergodic|kuznetsov|metaplectic"),
    ("Egyptian fractions", r"egyptian|unit.?fraction|reciprocal.?sum|m/n|m-over-n|sierpi|schinzel|erd(o|\u0151)s.?problem|"
     r"erdosproblems|greedy|zn(a|\u00e1)m|croot|bloom|breusch|k-terms|numerator|5/n|distinct.?denominator"),
    ("sibling problems & calibration", r"catalog|sibling|calibration|minimal.?pair|feature.?flip|precedent|template|outcome:|"
     r"goldbach|twin.?prime|waring|landau|lehmer|zsigmondy|bertrand|pillai|\bthue\b|catalan|brocard|lonely.?runner|conjecture.?h\b|"
     r"hardy.?littlewood|bateman|solved|analog|pointwise.?precedent|count:"),
    ("combinatorics", r"combinator|ramsey|graph|hypergraph|zero.?sum|davenport.?constant|additive.?comb|freiman|sum.?set|sumset|"
     r"kneser|container|matroid|extremal|sperner|tiling|partition.?regular|hypercube|sensitivity|sandpile|spanning|forest|frieze|"
     r"subset.?product|lov(a|\u00e1)sz|pigeonhole|nullstellensatz|polynomial.?method|poset|\bpartitions\b"),
    ("probability & heuristics", r"probab|random|heuristic|poisson|chen.?stein|stein.?chen|janson|statistic|cram(e|\u00e9)r|"
     r"entropy|large.?deviation|lower.?tail|expectation.?threshold|park.?pham|kahn.?kalai|percolation|branching|martingale|"
     r"stochastic|local.?lemma"),
    ("dynamics & continued fractions", r"dynamic|continued.?fraction|\bcf\b|sl.?2|sl\u2082|zaremba|ergodic|orbit|thin.?group|"
     r"semigroup|apollonian|gauss.?map|farey|stern.?brocot|euclid|collatz|\bflow|horocycle|\bwords?\b|hj3|hirzebruch|engel|"
     r"l(u|\u00fc)roth|numeration"),
    ("geometry & topology", r"topolog|(?<!arithmetic.)(?<!algebraic.)geometr|orbifold|seifert|knot|\blinks?\b|3-manifold|hyperbolic|"
     r"triangle|lattice.?point|polytope|tiling|\btiles?\b|polygon|euler.?char|gauss.?bonnet|plumbing|\blens\b|lens.?space|\btoric|"
     r"convex|\blattices?\b|\blll\b|short.?vector|geometry.?of.?numbers|"
     r"minkowski|persistent.?homology|fractal"),
    ("ES variants, function fields & other rings", r"function.?field|f_q\[t\]|\bf_q\b|\U0001d53d|polynomial.?ring|s-integer|\brings?\b|"
     r"matri(x|ces)|gaussian.?integer|es_q1|number.?field|over.?z\[|signed|p-adic.?es|constraint-world|new-world|\bvariants?\b|"
     r"weighted-es|signed-es|relaxation|strengthen|locali[sz]ation"),
    ("logic, complexity & formal", r"logic|\u03c0\u2081|\u03c0\u2070|\u03c0_1|pi_1|independen|reverse.?math|proof.?complex|"
     r"decidab|tfnp|ppa\b|\bsat\b|smt|\blean\b|formali[sz]|mathlib|complexity|algorithm|nonstandard|model.?theor|\bml\b|"
     r"machine.?learn|neural|llm|\bai\b|automat|alphaproof|funsearch|kolmogorov|walnut|formal.?method"),
    ("physics & other sciences", r"physic|resistor|kirchhoff|electrical|stat.?mech|statistical.?mech|\bising|partition.?function|"
     r"quantum|thermodynam|self.?organi|criticality|chemistry|biology|economics|mechanism.?design|crystal|music|optic"),
    ("ES reformulations & certificates", r"reformulation|new.?form|\btype.?i\b|\btype.?ii\b|c-form|e-slice|\bes5\b|es\u2085|\u2605|"
     r"mordell|\bi3\b|u\(n\)|\bform:|dictionary|polynomial.?ident|identit(y|ies).?famil|\bt1\b|odd.?square|square.?class|\b840\b|"
     r"tied.?modul|4cp|winning-c|c_min|r\(p\)|f\(p\)|exceptions-409-577|hard-primes|certificate.?(famil|graph|count|height)|"
     r"\bidentities\b|\bdivisors?\b|exponential.?famil|thin.?(famil|sequence)|star-count|r-zero"),
    ("computation & data", r"computation|compute|numeric|experiment|\bdata\b|data-|oeis|\bsearch|verification|verify|script|"
     r"enumerat|tabulat|fingerprint|record|sanity|null.?result|compute-and-check|\bscan|brute|\btables?\b"),
    ("history, community & meta", r"histor|community|\bmeta\b|meta-|outreach|contact|ask |mathoverflow|polymath|survey|"
     r"bibliograph|portfolio|strategy|recreational|anecdote|folklore|disproof.?hygiene|people|primary.?source"),
]
# ES-internal and computation vocabulary appears in almost every item; down-weight so the external field leads.
AREA_WEIGHT = {"ES reformulations & certificates": 0.5, "computation & data": 0.6}
_AREA_RX = [(name, re.compile(rx, re.I)) for name, rx in AREAS]


def areas_for(tags, title, body):
    tagtxt = " ".join(t for t in tags if not t.startswith("seen:"))
    scores = []
    for k, (name, rx) in enumerate(_AREA_RX):
        s = 3 * len(set(m.group(0).lower() for m in rx.finditer(tagtxt)))
        s += 2 * len(set(m.group(0).lower() for m in rx.finditer(title)))
        s += min(2, len(set(m.group(0).lower() for m in rx.finditer(body))))
        scores.append((s * AREA_WEIGHT.get(name, 1.0), -k, name))
    scores.sort(reverse=True)
    out = [name for s, _, name in scores[:3] if s >= 2.5]
    if not out:
        out = [scores[0][2]] if scores[0][0] > 0 else ["miscellaneous"]
    return out


RX_COMP = re.compile(r"\b(comput|recomput|script|enumerat|tabulat|numeric|run\b|search for|plot|fit\b|count\b|count the|histogram|"
                     r"simulat|scan|brute|sage|pari|python|test\b|tests\b|testing|check (numerically|for p|on p|all)|census|"
                     r"b-files?|pull\b|for (all |each |every )?(primes? |p |n |q )?[<\u2264]|evaluate|measure|sample|implement|"
                     r"solve .* for|list (all|the)|data|correlat|search (?!(the )?literature))", re.I)
RX_LIT = re.compile(r"\b(read|reread|look up|skim|search (the )?(literature|arxiv|mathoverflow|zbmath|mathscinet|google|for (a |the )?"
                    r"(paper|reference|literature))|literature|survey|paper|reference|email|contact|ask\b|locate|zbmath|"
                    r"mathscinet|book|thesis|cite|citation|arxiv|mathoverflow|oeis|dickson|(check|verify|confirm) (whether|if|that) "
                    r"[^.]{0,80}(known|literature|proved|published|exists in|in the paper|states|claims))", re.I)
RX_PROOF = re.compile(r"\b(prove|proof|lemma|show that|show\b|try to show|derive|attempt|establish|deduce|formulate|write down|"
                      r"write (the|r\(p\)|it|each|out)|expand|estimate|\bbound\b|upper bound|lower bound|state and prove|work out|"
                      r"classify|characteri[sz]e|translate .* (statement|theorem)|adapt|conjecture)", re.I)
CONF_ORDER = {"high": 2, "med": 1, "low": 0}
EFF_ORDER = {"cheap": 0, "medium": 1, "big": 2}
RX_TEMPLATED = re.compile(r"^(Catalog:|Problem \d|Feature:|Feature flip|Between:|Minimal pair:|Transfer:|Connection:)", re.I)
RX_TEMPLATED_BODY = re.compile(r"small-count existence problem|shares F\d|\u2194 ES F\d|share[sd]? F\d", re.I)


RX_NOSTEP = re.compile(r"^none\b", re.I)  # catalog/calibration rows whose lane gave no actionable first step


def _rep_score(it):
    s = 10 * CONF_ORDER[it["confidence_not_nonsense"]]
    if RX_TEMPLATED.search(it["title"]):
        s -= 6
    if RX_TEMPLATED_BODY.search(it["connection"]):
        s -= 6
    if re.search(r"\bF\d\d[wp]?\b", it["connection"]):  # signature-lane feature codes: less readable stand-alone
        s -= 4
    s += min(len(it["connection"]), 450) / 90 + min(len(it["first_step"]), 300) / 100
    s += 1 if it["refs"] else 0
    if RX_NOSTEP.match(it["first_step"]):
        s -= 15
    return s


def merge_items(items, cl):
    by = {it["id"]: it for it in items}
    out = []
    for n, g in enumerate(cl, 1):
        mem = [by[x] for x in g]
        rep = max(mem, key=_rep_score)
        tags, refs, alt, alt_titles = [], [], [], []
        for it in [rep] + [m for m in mem if m is not rep]:
            for t in it["tags"]:
                if t not in tags:
                    tags.append(t)
            for r in it["refs"]:
                if r.lower() not in (x.lower() for x in refs):
                    refs.append(r)
            if it is not rep:
                if it["first_step"] != rep["first_step"]:
                    alt.append(f"[{it['id']}] {it['first_step']}")
                alt_titles.append(f"[{it['id']}] {it['title']}")
        lanes = sorted(set(m["lane"] for m in mem), key=LANES.index)
        conf = max((m["confidence_not_nonsense"] for m in mem), key=CONF_ORDER.get)
        areas = areas_for(tags, rep["title"] + " " + " ".join(m["title"] for m in mem if m is not rep),
                          rep["connection"] + " " + rep["why"])
        flags = []
        if rep["effort"] == "cheap":
            flags.append("cheap")
        fs_all = " ".join(m["first_step"] for m in mem)
        if RX_COMP.search(rep["first_step"]) or any(t.lower() in ("computation", "compute-and-check", "numerics",
                                                                    "experimental", "experiments") for t in tags):
            flags.append("computational")
        if RX_LIT.search(rep["first_step"]):
            flags.append("literature-check")
        if RX_PROOF.search(rep["first_step"]):
            flags.append("proof-attempt")
        if len(lanes) >= 2:
            flags.append("multi-lane")
        if RX_NOSTEP.match(rep["first_step"]):
            flags.append("reference-only")
        if any(t.startswith("seen:") for t in tags):
            flags.append("seen")
        extra = {m["id"]: m["extra"] for m in mem if m["extra"]}
        rec = {
            "mid": f"Z{n:04d}", "title": rep["title"], "connection": rep["connection"], "why": rep["why"],
            "first_step": rep["first_step"], "alt_first_steps": alt, "refs": refs, "tags": tags, "areas": areas,
            "flags": flags, "sources": [m["id"] for m in [rep] + [m for m in mem if m is not rep]],
            "lanes": lanes, "confidence_not_nonsense": conf, "effort": rep["effort"],
        }
        if alt_titles:
            rec["alt_titles"] = alt_titles
        if extra:
            rec["lane_extra"] = extra
        del fs_all
        out.append(rec)
    return out


# ---------------------------------------------------------------- step 4: outputs

def _trunc(s, n):
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",;:") + " \u2026"


def _md_escape(s):
    return s.replace("|", "\\|")


def _rank_key(r):
    return (-len(r["lanes"]), -CONF_ORDER[r["confidence_not_nonsense"]], EFF_ORDER[r["effort"]], -len(r["sources"]), r["mid"])


def _item_md(r, conn_len=260, fs_len=230, show_areas=False):
    src = ", ".join(r["sources"])
    meta = f"{r['confidence_not_nonsense']}/{r['effort']}"
    fl = " ".join("`" + f + "`" for f in r["flags"] if f != "cheap")
    ar = (" \u00b7 also: " + "; ".join(r["areas"][1:])) if show_areas and len(r["areas"]) > 1 else ""
    return (f"- [ ] **{r['mid']} {_md_escape(r['title'])}** \u2014 {_md_escape(_trunc(r['connection'], conn_len))}\n"
            f"  *First step:* {_md_escape(_trunc(r['first_step'], fs_len))} ({src}; {meta}) {fl}{ar}\n")


INTRO_PATH = os.path.join(MERGE_DIR, "todo_intro.md")


def write_outputs(items, merged):
    with open(os.path.join(DATA, "master.jsonl"), "w", encoding="utf-8") as fh:
        for r in merged:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    raw = collections.Counter(it["lane"] for it in items)
    in_multi = collections.Counter()
    for r in merged:
        if len(r["lanes"]) >= 2:
            for s in r["sources"]:
                in_multi[s.rsplit("-", 1)[0]] += 1
    flags = collections.Counter(f for r in merged for f in r["flags"])
    areas_prim = collections.Counter(r["areas"][0] for r in merged)
    areas_any = collections.Counter(a for r in merged for a in r["areas"])
    nmulti = sum(1 for r in merged if len(r["lanes"]) >= 2)
    nclus = sum(1 for r in merged if len(r["sources"]) >= 2)
    sec1 = [r for r in merged if len(r["lanes"]) >= 2 or
            (r["effort"] == "cheap" and r["confidence_not_nonsense"] == "high" and "reference-only" not in r["flags"])]
    top = sorted([r for r in merged if len(r["lanes"]) >= 2], key=_rank_key)[:20]
    L = []
    w = L.append
    w("# ES_CONNECTIONS_TODO \u2014 master list of candidate connections for Erd\u0151s\u2013Straus (wave z52b)\n\n")
    w("> **ES is OPEN.** Nothing here is a proof or a claim of progress; every line is a *candidate connection* to be "
      "tried. Generated breadth-first by 10 lanes; merged by `scripts/z52b_merge.py` (only true duplicates fused, nothing "
      "dropped for being weak, already-screened or barrier-blocked).\n\n")
    if os.path.exists(INTRO_PATH):
        w(open(INTRO_PATH, encoding="utf-8").read().rstrip() + "\n\n")
    w("## Counts\n\n")
    w(f"**{len(items)} raw items \u2192 {len(merged)} distinct** ({nclus} merged clusters absorbing "
      f"{sum(len(r['sources']) for r in merged if len(r['sources']) >= 2)} raw items; {nmulti} items proposed "
      f"independently by \u2265 2 lanes).\n\n")
    w("| lane | raw items | of which in multi-lane items | lane memo |\n|---|---:|---:|---|\n")
    for lane in LANES:
        w(f"| {lane} | {raw[lane]} | {in_multi[lane]} | `BRAINSTORM/z52b_{lane}.md` |\n")
    w(f"| **total** | **{len(items)}** | **{sum(in_multi.values())}** | |\n\n")
    w("Flags: " + ", ".join(f"`{k}` {v}" for k, v in flags.most_common()) + ".\n\n")
    w("Areas (primary / any): " + ", ".join(f"{a} {areas_prim[a]}/{areas_any[a]}" for a, _ in areas_any.most_common())
      + ".\n\n")
    w("## How to use\n\n")
    w("- Each item: `- [ ] **Zxxxx title** \u2014 connection` then *First step* (cheap concrete action), sources (lane ids; "
      "the first is the representative whose wording is shown), `confidence/effort` (confidence that it is not nonsense), "
      "flags. Long texts are truncated here; the full record (why, refs, all tags, alternative first steps from merged "
      "duplicates, lane-specific fields) is in `data/z52b/master.jsonl` (grep the `mid`).\n")
    w("- Flags: `cheap` = first step \u2264 ~1 h (lane's effort=cheap); `computational` / `literature-check` / "
      "`proof-attempt` = nature of the first step (regex on its wording \u2014 approximate); `multi-lane` = proposed "
      "independently by \u2265 2 lanes (a useful signal); `seen` = lane tagged it `seen:<file>` (already discussed in the "
      "repo \u2014 still allowed); `reference-only` = the lane gave no actionable first step ('None.'), typically a "
      "calibration/catalog row kept as context.\n")
    w("- Areas are a light, open vocabulary derived from the tags (1\u20133 per item; items appear in \u00a72 under their "
      "first area). They are for navigation, not a verdict. Tags (\u00a73) are the lanes' free-form tags, unioned over "
      "merged duplicates; signature-lane tags `F01`\u2026`F40` refer to `data/z52b/signature_features.md`.\n")
    w("- Tick an item when its first step is done; record the outcome in a BRAINSTORM memo and reference the `mid`.\n")
    w("- Rebuild: `uv run --with numpy --with scikit-learn python scripts/z52b_merge.py build` (dedupe decisions live in "
      "`data/z52b/merge/`).\n\n")
    w("## Top-20 multi-lane items (most lanes, then confidence, then cheapness)\n\n")
    for k, r in enumerate(top, 1):
        w(f"{k}. **{r['mid']} {_md_escape(r['title'])}** \u2014 {len(r['lanes'])} lanes ({', '.join(r['lanes'])}); "
          f"{r['confidence_not_nonsense']}/{r['effort']}. *First step:* {_md_escape(_trunc(r['first_step'], 200))}\n")
    w("\n## \u00a71 Cheap & multi-lane\n\n")
    w(f"{len(sec1)} items: proposed by \u2265 2 lanes (any effort), or cheap + high-confidence. Multi-lane first.\n\n")
    sec1m = sorted([r for r in sec1 if len(r["lanes"]) >= 2], key=_rank_key)
    sec1c = [r for r in sec1 if len(r["lanes"]) < 2]
    w(f"### \u00a71a Multi-lane ({len(sec1m)})\n\n")
    for r in sec1m:
        w(_item_md(r, show_areas=False))
    w(f"\n### \u00a71b Cheap + high-confidence, single lane ({len(sec1c)}), by primary area\n\n")
    for a, _ in areas_prim.most_common():
        grp = [r for r in sec1c if r["areas"][0] == a]
        if grp:
            w(f"#### {a} ({len(grp)})\n\n")
            for r in grp:
                w(_item_md(r, conn_len=200, fs_len=180))
            w("\n")
    w("\n## \u00a72 Full list by area\n\n")
    w("Every distinct item exactly once, under its first area (secondary areas noted as 'also'). Within an area: "
      "multi-lane first, then confidence, then effort.\n\n")
    for a, _ in areas_prim.most_common():
        grp = sorted([r for r in merged if r["areas"][0] == a], key=_rank_key)
        w(f"### {a} ({len(grp)})\n\n")
        for r in grp:
            w(_item_md(r, show_areas=True))
        w("\n")
    w("## \u00a73 Index by tag\n\n")
    tagidx = collections.defaultdict(list)
    for r in merged:
        for t in r["tags"]:
            tagidx[t].append(r["mid"])
    multi = sorted([t for t in tagidx if len(tagidx[t]) >= 2], key=lambda t: (-len(tagidx[t]), t.lower()))
    single = len(tagidx) - len(multi)
    w(f"{len(tagidx)} distinct tags; the {len(multi)} tags used by \u2265 2 items are indexed below (by frequency); "
      f"{single} single-use tags are searchable in `data/z52b/master.jsonl`.\n\n")
    for t in multi:
        w(f"- `{t}` ({len(tagidx[t])}): {', '.join(tagidx[t])}\n")
    with open(os.path.join(ROOT, "ES_CONNECTIONS_TODO.md"), "w", encoding="utf-8") as fh:
        fh.write("".join(L))
    print(f"{len(items)} raw -> {len(merged)} distinct; multi-lane {nmulti}; sec1 {len(sec1)}; flags {dict(flags)}")
    print("areas primary:", dict(areas_prim.most_common()))


def build():
    items = load()
    cl = clusters(items)
    merged = merge_items(items, cl)
    write_outputs(items, merged)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "validate":
        load(report=True)
    elif cmd == "pairs":
        cmd_pairs()
    elif cmd == "clusters":
        its = load()
        cl = clusters(its)
        sz = collections.Counter(len(g) for g in cl)
        print(f"{len(its)} raw -> {len(cl)} distinct; cluster sizes {sorted(sz.items())}")
        with open(os.path.join(MERGE_DIR, "clusters.json"), "w") as fh:
            json.dump([g for g in cl if len(g) > 1], fh, indent=0)
    elif cmd == "build":
        build()
    else:
        raise SystemExit(f"unknown command {cmd}")
