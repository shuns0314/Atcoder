N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

ans = []
for i in range(1, M+1):
    trigger = True
    for j in A:
        r = gcd(i, j)
        if r != 1:
            trigger = False
            break
    if trigger:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)

