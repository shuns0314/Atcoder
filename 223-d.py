N, M = map(int, input().split())
graph = [set() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)

seen = [False for _ in range(N)]

def dfs(i):
    seen[i] = True
    for j in graph[i]:
        if seen[j]:
            continue
        else:
            dfs(graph[i])


print(graph)