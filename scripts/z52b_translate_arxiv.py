"""Verify arXiv ids / title searches for lane translate. usage: ids... or -s 'query'"""
import sys, urllib.request, urllib.parse, re, time
def get(url):
    return urllib.request.urlopen(url, timeout=30).read().decode()
args=sys.argv[1:]
if args and args[0]=='-s':
    for q in args[1:]:
        x=get('https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':4}))
        for e in x.split('<entry>')[1:]:
            i=re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>',e).group(1)
            t=' '.join(re.search(r'<title>(.*?)</title>',e,re.S).group(1).split())
            a=re.findall(r'<name>(.*?)</name>',e)[:3]
            print(f'[{q}] {i} | {t} | {", ".join(a)}')
        time.sleep(3)
else:
    x=get('https://export.arxiv.org/api/query?id_list='+','.join(args)+'&max_results=50')
    for e in x.split('<entry>')[1:]:
        i=re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>',e).group(1)
        t=' '.join(re.search(r'<title>(.*?)</title>',e,re.S).group(1).split())
        a=re.findall(r'<name>(.*?)</name>',e)[:3]
        print(f'{i} | {t} | {", ".join(a)}')
