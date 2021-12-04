from collections import deque

INF = 10**9 + 7
N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

DST = [-1] * N
DP = [0] * N

def bfs():
    que = deque([0])
    DST[0] = 0
    DP[0] = 1

    while que:
        i = que.popleft()
        for j in G[i]:
            if DST[j] == -1:
                que.append(j)
                DST[j] = DST[i] + 1
                DP[j] = DP[i]
            elif DST[j] == DST[i] + 1:
                DP[j] += DP[i]
                
bfs()
print(DP[-1]%INF)
