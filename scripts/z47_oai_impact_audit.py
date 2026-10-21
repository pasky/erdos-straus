#!/usr/bin/env python3
"""Bounded source inventory and reproducible static audit; not a Lean build."""
import argparse, gzip, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILIES = ['003','007','011','012','015','020','021','023','025','026','027','028','029','142','182','279']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--clone', type=Path, default=Path('/tmp/oai-math'))
    args = ap.parse_args()
    clone = args.clone
    out = ROOT / 'sources/oai2026'
    data = ROOT / 'data/z47_oai_impact'
    out.mkdir(parents=True, exist_ok=True)
    data.mkdir(parents=True, exist_ok=True)
    cat = (clone/'CONTENTS.md').read_text()
    blocks = {}
    matches = list(re.finditer(r'^\*\*(\d{3})\.', cat, re.M))
    for i,m in enumerate(matches):
        blocks[m[1]] = cat[m.start():matches[i+1].start() if i+1<len(matches) else len(cat)]
    files = subprocess.check_output(['git','-C',str(clone),'ls-files'],text=True).splitlines()
    manifest = (clone/'lean/formalization.yaml').read_text()
    inventory = {}
    docs = []
    provenance = {'url': 'https://github.com/openai/math',
                  'commit': subprocess.check_output(['git','-C',str(clone),'rev-parse','HEAD'],text=True).strip(),
                  'audit': 'Static source inspection only; no Lean execution.'}
    (data/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    for fam in FAMILIES:
        block = blocks[fam]
        pdfs = list(dict.fromkeys(re.findall(r'\]\((preprints/[^)]+\.pdf)\)',block)))
        record = {'catalogue':block.splitlines()[0], 'papers':[], 'lean_docs':[]}
        excerpts = ['# Family '+fam, '', 'CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.']
        for pdf in pdfs:
            directory = str(Path(pdf).parent)
            tex = [f for f in files if f.startswith(directory+'/') and f.endswith('.tex')]
            record['papers'].append({'pdf':pdf, 'tex':tex, 'catalogued_formalization':('../'+pdf) in manifest})
            excerpts += ['', '## '+pdf]
            for t in tex:
                text = (clone/t).read_text()
                # All theorem statements, not proofs or whole manuscripts.
                environments = 'theorem|thm|maintheorem'
                if fam == '029' and t.endswith('/01a-reduction.tex'):
                    environments += '|proposition'
                thms = re.findall(r'\\begin\{('+environments+r')\}(.*?)\\end\{\1\}',text,re.S)
                if thms:
                    excerpts += ['', 'Source: '+t, '```tex']
                    excerpts += ['\\begin{'+kind+'}'+body+'\\end{'+kind+'}' for kind,body in thms]
                    excerpts += ['```']
        doc = clone/'lean/docs'/f'{fam}.md'
        if doc.exists():
            text = doc.read_text()
            excerpts += ['', '## Lean scope page (verbatim)', text]
            challenges = re.findall(r'\]\(\.\./ComparatorChallenges/([^)]*\.lean)\)',text)
            record['lean_docs'] = challenges
            for ch in challenges:
                cfgpath = clone/'lean/ComparatorChallenges'/ch.replace('.lean','.json')
                if cfgpath.exists():
                    cfg = json.loads(cfgpath.read_text())
                    docs.append((fam,ch,cfg))
        (out/f'{fam}-excerpts.md').write_text('\n'.join(excerpts).rstrip()+'\n')
        inventory[fam] = record
    audit=[]
    for fam,ch,cfg in docs:
        pending=[cfg['solution_module']]; visited=set(); hits=[]; missing=[]
        while pending:
            mod=pending.pop()
            if mod in visited: continue
            visited.add(mod)
            path=clone/'lean'/Path(mod.replace('.','/')).with_suffix('.lean')
            if not path.exists():
                missing.append(mod); continue
            text=path.read_text()
            for num,line in enumerate(text.splitlines(),1):
                if re.search(r'\b(sorry|axiom|admit|sorryAx)\b',line):
                    hits.append({'file':str(path.relative_to(clone)), 'line':num,'text':line})
            for line in text.splitlines():
                if line.startswith('import '):
                    pending.extend(m for m in line[7:].split() if m.startswith('OAI.'))
        audit.append({'family':fam,'challenge':ch,'config':cfg,'local_modules':sorted(visited),'missing':missing,'lexical_hits':hits})
    (data/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    (data/'lean-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    harvest = subprocess.run(['git','grep','-n','-E','GRH|CONDITIONAL on GRH|under GRH|Siegel|ineffective|Artin|Chowla|Jacobsthal','--','*.md',':(exclude)OAI_DUMP_IMPACT.md',':(exclude)sources/oai2026/**'],cwd=ROOT,capture_output=True,text=True,check=False)
    assert harvest.returncode in (0,1)
    with gzip.open(data/'campaign-harvest.txt.gz','wt') as f: f.write(harvest.stdout)
    print('families',len(inventory),'papers',sum(len(x['papers']) for x in inventory.values()))
    for a in audit:
        print(a['family'],a['challenge'],'modules',len(a['local_modules']),'hits',len(a['lexical_hits']),'missing',a['missing'])
    print('excerpts bytes',sum(p.stat().st_size for p in out.glob('*-excerpts.md')))

if __name__ == '__main__': main()
