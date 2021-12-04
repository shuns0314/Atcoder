N, W = list(map(int, input().split()))
w_l = []
v_l = []

for _ in range(N):
    w, v = list(map(int, input().split()))
    w_l.append(w)
    v_l.append(v)

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(W+1):
        
        if w_l[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_l[i-1]] + v_l[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
            