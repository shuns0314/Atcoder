N, M = map(int, input().split())
A = list(map(int, input().split()))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            while temp%i==0:
                temp //= i
            arr.append(i) 
    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)
 
    return arr  

s_l = set()
for a in A:
    if a!=1:
        a = set(factorization(a))
        s_l.update(a)
# print(s_l)

m_l = set([i for i in range(1, M+1)])

for s in s_l:
    i = 1 
    t = 1
    while t <= M:
        t = s * i
        m_l.discard(t)
        i += 1

ans = sorted(m_l)
print(len(ans))
for i in ans:
    print(i)
