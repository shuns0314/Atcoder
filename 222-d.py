N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353
L = 3001
DP = [[0]*L for _ in range(N)]

for j in range(L):
    if A[0] <= j and j <= B[0]:
        if j == 0:
            DP[0][j] = 1
        elif DP[0][j-1] == 0:
            DP[0][j] = 1
        else:
            DP[0][j] = DP[0][j-1] + 1
    else:
        if B[0] < j:
            DP[0][j] = DP[0][j-1]

for i in range(1, N):
    for j in range(L):
        if A[i] <= j and j <= B[i]:
            DP[i][j] = (DP[i][j-1] + DP[i-1][j])%MOD
        else:
            DP[i][j] = (DP[i][j-1])%MOD

print(DP[-1][-1])