H, W, N = list(map(int, input().split()))
h_l = []
w_l = []

for _ in range(N):
    h, w = list(map(int, input().split()))
    h_l.append(h)
    w_l.append(w)

sorted_h_l = sorted(set(h_l))
sorted_w_l = sorted(set(w_l))

h_d = {h:i+1 for i, h in enumerate(sorted_h_l)}
w_d = {w:i+1 for i, w in enumerate(sorted_w_l)}

for h, w in zip(h_l, w_l):
    print(h_d[h], w_d[w])
