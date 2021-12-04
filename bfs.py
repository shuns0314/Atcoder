from collections import deque

# M = 5  # 都市の数
# root = [[0, 1],[1, 2],[2, 3],[2, 4]]

M = 8
root = [[0, 1],[0, 5],[0, 2],[1, 7],[1, 3], [2, 3], [2, 4], [2, 7], [3, 4], [5, 6], [6, 7]]

graph = [[] for i in range(M)]

for a, b in root:
    graph[a].append(b)
    graph[b].append(a)

print(graph)

dist = [-1] * M

def bfs(start):
    que = deque([start])
    dist[start] = 0
    while que:
        i = que.popleft()
        for j in graph[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                que.append(j)
    return dist

print(bfs(0))
    



