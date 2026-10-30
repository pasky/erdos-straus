# Fetch arXiv API records for a list of ids, dump id/version/published/updated/authors/title/summary.
import sys, time, urllib.request, xml.etree.ElementTree as ET
ns={'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom'}
ids=[s.strip() for s in open(sys.argv[1]).read().split() if s.strip()]
out=open(sys.argv[2],'w')
for i in range(0,len(ids),15):
    b=ids[i:i+15]
    url="https://export.arxiv.org/api/query?id_list="+",".join(b)+"&max_results=50"
    for attempt in range(3):
        try:
            data=urllib.request.urlopen(url,timeout=60).read(); break
        except Exception as e:
            print("retry",e,file=sys.stderr); time.sleep(5)
    root=ET.fromstring(data)
    seen=set()
    for e in root.findall('a:entry',ns):
        eid=e.find('a:id',ns).text.split('/abs/')[-1]
        seen.add(eid.split('v')[0] if 'v' in eid else eid)
        au=", ".join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
        t=" ".join(e.find('a:title',ns).text.split())
        s=" ".join(e.find('a:summary',ns).text.split())
        jr=e.find('x:journal_ref',ns); dr=e.find('x:doi',ns)
        out.write(f"== {eid}\nauthors: {au}\ntitle: {t}\npublished: {e.find('a:published',ns).text} updated: {e.find('a:updated',ns).text}\n")
        if jr is not None: out.write(f"journal_ref: {jr.text}\n")
        if dr is not None: out.write(f"doi: {dr.text}\n")
        out.write(f"abstract: {s}\n\n")
    for x in b:
        if not any(x in s for s in seen): out.write(f"== {x} NOT RETURNED\n\n")
    time.sleep(3)
