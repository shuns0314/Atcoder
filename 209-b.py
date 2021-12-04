

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

if (sum(A) - len(A)//2) <= X:
    print("Yes")
else:
    print("No")