N, K = list(map(int, input().split()))
C = list(map(int, input().split()))

max_c = 0
for i in range(N-K+1):
    max_c = max(max_c, len(set(C[i:i+K])))

print(max_c)
