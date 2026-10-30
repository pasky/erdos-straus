#!/usr/bin/env python3
"""Build data/z52b/upgrades.jsonl and BRAINSTORM/z52b_upgrades.md from the catalogue + item modules.
Lane `upgrades`, wave z52b.  Run: uv run python scripts/z52b_upgrades_build.py  (or python3)."""
import glob, importlib.util, json, os, re, subprocess, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import z52b_upgrades_catalogue as catm  # noqa: E402

CAT = {c[0]: c for c in catm.CAT}
ITEMS = []


def I(keys, title, connection, why, first_step, tags, conf="med", eff="medium", refs=None, kw=None, seen=None):
    ITEMS.append(dict(keys=keys, title=title, connection=connection, why=why, first_step=first_step,
                      tags=list(tags), conf=conf, eff=eff, refs=list(refs or []), kw=list(kw or []),
                      seen=list(seen or [])))


def load_items():
    for path in sorted(glob.glob(os.path.join(ROOT, "scripts", "z52b_upgrades_items*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        mod.I = I
        spec.loader.exec_module(mod)


_grep_cache = {}


def grep_seen(kw):
    if kw in _grep_cache:
        return _grep_cache[kw]
    try:
        out = subprocess.run(["git", "grep", "-il", "-F", kw, "--", "*.md"], cwd=ROOT, capture_output=True,
                             text=True, timeout=60).stdout.split()
    except subprocess.TimeoutExpired:
        out = []
    out = [f for f in out if "z52b_" not in f]
    _grep_cache[kw] = out
    return out


def build():
    load_items()
    rows = []
    seen_titles = set()
    for n, it in enumerate(ITEMS, 1):
        t = it["title"].strip()
        if t.lower() in seen_titles:
            raise SystemExit(f"duplicate title: {t}")
        seen_titles.add(t.lower())
        keys = [k.strip() for k in it["keys"].split(",") if k.strip()]
        for k in keys:
            if k not in CAT and k != "X":
                raise SystemExit(f"unknown catalogue key {k} in item {t}")
        tags = list(dict.fromkeys(it["tags"] + [f"from:{k}" for k in keys if k != "X"]))
        refs = list(it["refs"])
        for k in keys:
            if k in CAT and CAT[k][5]:
                r = CAT[k][5][0]
                if r not in refs:
                    refs.append(r)
        seen = list(it["seen"])
        for kw in it["kw"]:
            hits = grep_seen(kw)
            if hits:
                seen.append(hits[0])
        for s in dict.fromkeys(seen):
            tags.append(f"seen:{s}")
        rows.append(dict(id=f"upgrades-{n:04d}", title=t, connection=it["connection"].strip(), why=it["why"].strip(),
                         first_step=it["first_step"].strip(), refs=refs, tags=tags,
                         confidence_not_nonsense=it["conf"], effort=it["eff"],
                         upgrade=[CAT[k][1] for k in keys if k in CAT]))
    os.makedirs(os.path.join(ROOT, "data", "z52b"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "z52b", "upgrades.jsonl"), "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    write_md(rows)
    print(len(rows), "items;", len(CAT), "catalogue entries")


def write_md(rows):
    head_path = os.path.join(ROOT, "scripts", "z52b_upgrades_header.md")
    header = open(head_path).read() if os.path.exists(head_path) else "# z52b lane `upgrades`\n"
    tagc = Counter(t for r in rows for t in r["tags"] if not t.startswith(("from:", "seen:")))
    fromc = Counter(t[5:] for r in rows for t in r["tags"] if t.startswith("from:"))
    seenc = sum(1 for r in rows if any(t.startswith("seen:") for t in r["tags"]))
    hist = ("Confidence-not-nonsense: " + ", ".join(f"{k} {v}" for k, v in Counter(r['confidence_not_nonsense'] for r in rows).most_common())
            + "; effort: " + ", ".join(f"{k} {v}" for k, v in Counter(r['effort'] for r in rows).most_common())
            + f". {len(tagc)} distinct free-form tags; top 40: " + ", ".join(f"`{t}` {c}" for t, c in tagc.most_common(40)) + ".")
    header = header.replace("{{TAGS}}", hist)
    out = [header.replace("{{N}}", str(len(rows))).replace("{{NCAT}}", str(len(CAT))).replace("{{NSEEN}}", str(seenc))]
    out.append("\n## Full tag histogram (free-form tags; `from:` and `seen:` excluded)\n")
    out.append(", ".join(f"`{t}` {c}" for t, c in tagc.most_common()) + "\n")
    out.append("Items per catalogued upgrade (`from:` tags): " + ", ".join(f"{k} {v}" for k, v in fromc.most_common()) + "\n")
    out.append("\n## Catalogue of historical upgrades (before → after; the last-step ingredient)\n")
    out.append("Verification status from `data/z52b/upgrades_verify_out_*.md` (research subagents; corrections applied as overrides in "
               "`scripts/z52b_upgrades_catalogue.py`). Items per upgrade in brackets.\n")
    for i, (k, c) in enumerate(CAT.items(), 1):
        out.append(f"{i}. **{c[1]}** [`{k}`, {fromc.get(k, 0)} items] — *before:* {c[2]} — *after:* {c[3]} — "
                   f"*last step:* {c[4]} — *refs:* {'; '.join(c[5]) if c[5] else '—'}")
    out.append("\n## Items\n")
    for r in rows:
        n = int(r["id"].split("-")[1])
        tg = ", ".join(t for t in r["tags"])
        out.append(f"{n}. **{r['title']}** — {r['connection']} — *why:* {r['why']} — *first step:* {r['first_step']} "
                   f"— [{r['confidence_not_nonsense']}/{r['effort']}; {tg}]")
    with open(os.path.join(ROOT, "BRAINSTORM", "z52b_upgrades.md"), "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    build()
