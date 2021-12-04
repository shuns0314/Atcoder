import sys
sys.setrecursionlimit(10000)

N, M = list(map(int, input().split()))

def create_graph():
    graph = {i+1: set() for i in range(N)}

    for _ in range(M):
        a, b = list(map(int, input().split()))
        graph[a].add(b)
    return graph

def dfs(graph, seen, i):
    if seen[i]:
        return
    seen[i] = True
    for j in graph[i]:
        dfs(graph, seen, j)

def main():
    ans = 0
    graph = create_graph()
    for i in range(1, N+1):
        seen = {i+1: False for i in range(N)}
        dfs(graph, seen, i)
        ans += sum(seen.values())
    print(ans)

main()







