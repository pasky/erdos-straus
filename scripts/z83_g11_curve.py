"""Root-level scan. Build z83_g11_curve.c alongside outputs, remove after replay."""
import subprocess,sys,os
import z82_gap11_r2_cert as z
S=10**8
floor=lambda x:x//(z.S//S)
ceil=lambda x:-floor(-x)
table=''.join(' '.join(map(str,(floor(z.half(i,z.N)[0]),ceil(z.half(i,z.N)[1]),floor(z.lin(i,z.N)[0]),ceil(z.lin(i,z.N)[1]),ceil(z.Hhi[2][i]),ceil(sum(v[i] for j,v in z.Hhi.items() if j>=int(os.environ.get('G11_H','4')))))))+'\n' for i in range(1,z.T+1))+f'{ceil(z.Au)} {ceil(z.Eu)}\n'
def run(G,J,B,c3,c7,lo):
    s=subprocess.run([os.environ['G11_CURVE_BIN'],*map(str,(G,J,B,c3,c7,lo))],text=True,input=table,capture_output=True,check=True).stdout
    return [list(map(int,l.split())) for l in s.splitlines()]
if __name__=='__main__':
    if sys.argv[1:]==['shapes']:
        for j,b,c3,c7 in [(2400,360,1999,1999),(2480,360,1999,1180),(2640,360,1999,840),(2800,360,1999,801),(2700,360,1999,720),(2880,360,1999,1000),(3200,360,1999,1200),(3000,360,1999,1000)]:print(run(4000,j,b,c3,c7,j)[0],flush=True)
    elif sys.argv[1:]==['rough']:
        assert os.environ.get('G11_H')=='6'
        for G,b,j in [(6000,421,2999),(6000,422,2999),(6000,423,2999),(4000,340,2092),(4000,360,2092),(4000,380,2092)]:print(run(G,j,b,j,j,j)[0],flush=True)
    elif len(sys.argv)>1:rows=run(*map(int,sys.argv[1:]));print(*rows[::max(1,len(rows)//10)],sep='\n');print('first positive',next((r for r in rows if r[-1]>0),None));print('end',rows[-1])
    else:
        G=4000;top=2320
        rows=[r for b in (336,344,352,360,368,376) for r in run(G,top,b,top,top,1999)]
        for j in (1999,2160,2240,2285,2300,2304,2308,2312,2316,2320):print('row',max((r for r in rows if r[1]==j),key=lambda r:r[-1]),flush=True)
        print('first positive',min((r for r in rows if r[-1]>0),key=lambda r:(r[1],-r[-1])))
        for j,b,c3,c7 in [(2480,352,2480,1080),(2600,336,2600,800),(2880,320,2880,480),(2600,352,2480,1080),(2480,352,2360,1200)]:print('rectangle',run(G,j,b,c3,c7,j)[0],flush=True)
