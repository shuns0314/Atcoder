N = int(input())
d = {i+1: 0 for i in range(N)}

for _ in range(N-1):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1

if max(d.values()) == (N-1):
    print("Yes")
else:
    print("No")
