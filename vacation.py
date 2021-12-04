N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
 
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = table[0]
 
for i in range(1, N):
    for j in range(3):
        # j番目以外の幸福度が一番高い予定
        pred_max_plan = max(dp[i-1][:j] + dp[i-1][j+1:])
        dp[i][j] = pred_max_plan + table[i][j]

print(max(dp[-1]))