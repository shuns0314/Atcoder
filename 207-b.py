A, B, C, D = list(map(int, input().split()))

blue = A
red = 0
count = 0
flag = True

if blue <= red * D:
    print(count)
else:
    for _ in range(10**5):
        count += 1
        blue += B
        red += C
        if blue <= red * D:
            print(count)
            flag = False
            break
if flag:
    print(-1)
        