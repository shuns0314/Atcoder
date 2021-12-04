import sys
sys.setrecursionlimit(300000)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):graph[i].sort()

ans = []
def dfs(graph, n, pre):
    ans.append(n)
    for next in graph[n]:
        if next != pre:
            dfs(graph, next, n)
            ans.append(n)

dfs(graph, 1,-1)
print(*ans)
