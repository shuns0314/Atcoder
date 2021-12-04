N = int(input())

A = []
B = []
S = [(0, 0)]
total_s = 0
total_l = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    total_s += a/b
    total_l += a
    S.append((total_l, total_s))

s = total_s/2
# print(S)
# print(s)

def serch():
    for i in range(N):
        if S[i+1][1] == s:
            return S[i+1][0]
        if s < S[i+1][1]:
            return S[i][0] + (s - S[i][1])*B[i]

print(serch())








