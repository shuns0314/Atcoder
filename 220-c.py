N = int(input())
A = list(map(int, input().split()))
X = int(input())

base = sum(A)

t = X // base
s = t * base  # SUM（A）でとれる最大値
t *= N  # SUM(A)までの個数


for i in (A*2):
    if s > X:
        print(t)
        break
    s += i
    t += 1



