abc = "abcdefghijklmnopqrstuvwxyz"
abc_ = input()

d = {i: j for i,j in zip(abc_, abc)}

n = int(input())

S = [input() for _ in range(n)]

S_ = []
d_2 = {}

for s in S:
    c = ""
    for char in s:
        c += d[char]
    S_.append(c)
    d_2[c] = s

S_ = sorted(S_)

for s in S_:
    print(d_2[s])

