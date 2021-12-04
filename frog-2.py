N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

DP = [0] * N

for i in range(1, N):
    DP[i] = min([DP[i-j] + abs(H[i]-H[i-j]) for j in range(1, K+1) if j <= i])

print(DP[-1])
            