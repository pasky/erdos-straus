"""R83: check the numerical claims of POINTWISE_MORDELL17 §4 (tail sums)."""
# (1) "even granting D_P(K) <= 17^{2K/5}: sum_{K>=11 odd} 2*17^{2K/5}*17^{1-(K+1)/2} ~ 0.84"
s = sum(2 * 17 ** (2 * K / 5 + 1 - (K + 1) / 2) for K in range(11, 4001, 2))
print("P tail with D_P = 17^{2K/5}:", s)
# (2) "D_Q + D_U <= 17^{k/2} (k>=8), D_P(K) <= 17^{K/4} (K>=11) => tail < 0.01"
#     tail = sum_{k>=6} 17^{1-k} B_k, B_k = 8 D_Q + 2 D_U + 2 D_P(2k-1) (+ 2 D_P(2k) = 0)
#     known: D_Q(6)=D_U(6)=0, D_Q(7)=707, D_U(7)=826 (author; reviewer reproduced, see review)
t = 0.0
for k in range(6, 400):
    if k == 6:
        BQU = 0
    elif k == 7:
        BQU = 8 * 707 + 2 * 826
    else:
        BQU = 8 * 17 ** (k / 2) if k < 200 else 0  # worst case: all of D_Q+D_U in D_Q
    pass
    t += 17 ** (1 - k) * BQU + 2 * 17 ** ((2 * k - 1) / 4 + 1 - k)
print("tail under the hypothetical bounds:", t)
# (3) margin: if instead only the P tail were 17^{K/4}, from K = 11
print("P part alone:", sum(2 * 17 ** (K / 4 + 1 - (K + 1) / 2) for K in range(11, 4001, 2)))
