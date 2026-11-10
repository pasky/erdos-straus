# Split the H witness file (/tmp/z69mine/H.wit, from z69_mine_allwit.c) into H_train.wit / H_test.wit per the
# pre-registered hash split (data/z69/mine/H_{train,test}.txt).
T = '/tmp/z69mine/'
blocks = {}; cur = None
for l in open(T + 'H.wit'):
    if l.startswith('W '): cur = int(l.split()[1]); blocks[cur] = [l]
    elif l.strip(): blocks[cur].append(l)
for s in ('H_train', 'H_test'):
    ps = [int(x.split()[0]) for x in open('data/z69/mine/%s.txt' % s) if x.strip()]
    assert all(p in blocks for p in ps)
    open(T + s + '.wit', 'w').write(''.join(''.join(blocks[p]) for p in ps))
    print(s, len(ps))
