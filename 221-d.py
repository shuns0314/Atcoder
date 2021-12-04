N = int(input())

cnt = []
for _ in range(N):
    a, b = map(int, input().split())
    cnt.append((a, +1))
    cnt.append((a+b, -1))

cnt.sort()
ans = [0] * (N+1)

logins = 0
point = -1

for day, c in cnt:
    ans[logins] += day - point
    logins += c
    point = day

print(*ans[1:])



