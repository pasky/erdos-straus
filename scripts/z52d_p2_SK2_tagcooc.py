"""Pass-2 SK2 Z1881: tag co-occurrence over the merged z52b list (data/z52b/master.jsonl, 3192 records).
Lists (a) the most frequent tags, (b) the most frequent tag pairs, and (c) 'blind spots': pairs of
high-frequency tags (top 40) that never co-occur. Output: data/z52b/pass2/SK2/tagcooc.json
"""
import json, itertools, re
from collections import Counter
recs = [json.loads(l) for l in open("data/z52b/master.jsonl") if l.strip()]
TAXON = re.compile(r"^(seen:|gen:|src:|form:|lane:|F\d\d$|F\d\d-)")
def tags_of(r):
    t = r.get("tags") or []
    if isinstance(t, str): t = [t]
    return sorted({x.strip() for x in t if x and x.strip() and not TAXON.match(x.strip())})
T = [tags_of(r) for r in recs]
freq = Counter(t for ts in T for t in ts)
pairs = Counter()
for ts in T:
    for a, b in itertools.combinations(ts, 2): pairs[(a, b)] += 1
top = [t for t, _ in freq.most_common(40)]
blind = [(a, b, freq[a], freq[b]) for a, b in itertools.combinations(top, 2) if pairs[(a, b)] == 0]
out = {"n_records": len(recs), "n_distinct_tags": len(freq), "note": "taxonomy tags (seen:, gen:, src:, form:, F-codes) removed",
       "top_tags": freq.most_common(25),
       "top_pairs": [((a, b), n) for (a, b), n in pairs.most_common(15)],
       "n_top40_pairs": len(top) * (len(top) - 1) // 2, "n_top40_pairs_never_cooccurring": len(blind),
       "blind_spots_sample": blind[:25]}
json.dump(out, open("data/z52b/pass2/SK2/tagcooc.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: out[k] for k in ["n_records", "n_distinct_tags", "n_top40_pairs", "n_top40_pairs_never_cooccurring"]}))
print(out["top_tags"][:12])
print(blind[:12])
