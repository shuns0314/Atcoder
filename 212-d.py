import heapq
from collections import deque

N = int(input())
l = []
b = 0

for _ in range(N):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(l, q[1] - b)
    if q[0] == 2:
        b += q[1]
    if q[0] == 3:
        ans = heapq.heappop(l) + b
        print(ans)
