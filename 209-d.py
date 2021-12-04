from collections import deque

N, Q = map(int, input().split())

G = [[] for _ in range(N + 1)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] *(N+1)

def bfs(start):
    que = deque([start])
    dist[start] = 0
    while que:
        i = que.popleft()
        
        for j in G[i]:
            if dist[j] == -1:
                que.append(j)
                dist[j] = dist[i] + 1

bfs(1)

for i in range(Q):
    start, end = map(int, input().split())
    d_s = dist[start]
    d_e = dist[end]
    if ((d_s%2 == 1) and (d_e%2 == 1)) or ((d_s%2 == 0) and (d_e%2 == 0)):
        print("Town")
    else:
        print("Road")
