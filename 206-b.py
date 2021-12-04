N = int(input())

money = 0
for i in range(1, N+1):
    money += i
    if money >= N:
        print(i)
        break
