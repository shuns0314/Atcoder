N, M = map(int, input().split())
d = {i+1: list(input()) for i in range(2*N)}
 
NUMBER = {i+1: 0 for i in range(2*N)}
rank = [i+1 for i in range(2*N)]
 
def janken(a, b, a_n, b_n):
    if a == "G" and b == "P":
        NUMBER[b_n] += 1
    elif a == "P" and b == "G":
        NUMBER[a_n] += 1
    elif a == "C" and b == "G":
        NUMBER[b_n] += 1
    elif a == "G" and b == "C":
        NUMBER[a_n] += 1
    elif a == "P" and b == "C":
        NUMBER[b_n] += 1
    elif a == "C" and b == "P":
        NUMBER[a_n] += 1
    else:
        pass
 
for i in range(M):
    for j in range(0, 2 * N, 2):
        a = rank[j]
        b = rank[j+1]
        janken(d[a][i], d[b][i], a, b)
    temp = sorted(NUMBER.items(), key=lambda x: (-x[1], x[0]))
    rank = [i[0] for i in temp]
 
for i in rank:
    print(i)
