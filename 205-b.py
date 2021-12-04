N = int(input())
A = list(map(int, input().split()))

t_1 = set([i for i in range(1, N+1)])
t_2 = set(A)

if t_1 == t_2:
    print("Yes")
else:
    print("No")
