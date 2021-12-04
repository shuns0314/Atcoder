N = int(input())
P = list(map(int, input().split()))

Q = {p: i+1 for i, p in enumerate(P)}
ans = [str(Q[i+1]) for i in range(N)]
ans = " ".join(ans)
print(ans)