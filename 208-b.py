
P = int(input())

money = []
for i in range(1, 11):
    coin = 1
    for j in range(1, i+1):
        coin *= j
    money.append(coin)

def fn(P, count):
    if P == 0:
        return count
    for i in range(10):
        if P >= money[-1]:
            P -= money[-1]
            count += 1
            break
        elif P < money[i]:
            P -= money[i-1]
            count += 1
            break
    return fn(P, count)

print(fn(P, 0))
