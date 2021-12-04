N = int(input())
A = list(map(int, input().split()))
mod = 998244353
K = [[0] * 10 for _ in range(N)]

f = (A[0] + A[1])%10
g = (A[0] * A[1])%10
K[1][f] += 1
K[1][g] += 1

for i in range(2, N):
    for j in range(10):
        K[i][(j + A[i])%10] += K[i-1][j]
        K[i][(j + A[i])%10] %= mod
        K[i][(j * A[i])%10] += K[i-1][j]
        K[i][(j * A[i])%10] %= mod

for i in K[-1]:
    print(i)
